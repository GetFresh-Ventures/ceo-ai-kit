---
name: dedupe-entities
description: "Resolve duplicate entities across CSV datasets using machine-learning record linkage. Use when CRM data has duplicates, data sources need reconciliation, or entity names are inconsistent."
---

# Entity Deduplication

Mathematically resolve duplicate records in datasets where the same entity appears under different names, spellings, or formats. Uses the `dedupe` library for active-learning record linkage.

## When to Use

- CRM has duplicate contacts or companies ("Acme Corp" vs "ACME Corporation")
- Merging data from two systems with different naming conventions
- Post-import cleanup of a large CSV
- User says "deduplicate", "find duplicates", "clean up this data"

## Prerequisites

```bash
pip install dedupe csvkit
```

Also requires `tools/gfv-dedupe.py` from this kit.

## Step 1: Assess the Data

```bash
# Inspect the CSV
head -5 input.csv
wc -l input.csv

# Check for obvious duplication signals
csvcut -c "Company Name" input.csv | sort | uniq -ci | sort -rn | head -20
```

**Key questions:**
- How many rows total?
- Which columns identify an entity? (Name, email, phone, company)
- What kind of duplicates? (Typos, abbreviations, missing fields)

## Step 2: Choose Matching Fields

Select columns that, together, should uniquely identify an entity:

| Use case | Recommended fields |
|----------|-------------------|
| **Contact dedup** | `First Name`, `Last Name`, `Email`, `Company` |
| **Company dedup** | `Company Name`, `Domain`, `Phone` |
| **Product dedup** | `Product Name`, `SKU`, `Category` |
| **Address dedup** | `Street`, `City`, `State`, `Zip` |

**Rules:**
- Use at least 2 fields (single-field matching has too many false positives)
- Include at least one high-cardinality field (email, phone, domain)
- Don't include IDs — they're unique by definition and won't help

## Step 3: Run Deduplication

**This step is interactive** — the `dedupe` library uses active learning, which requires the user to answer "Is this a match?" questions in the terminal. You cannot do this on the user's behalf.

Provide this command to the user:

```bash
python tools/gfv-dedupe.py \
  --input data.csv \
  --output deduplicated_data.csv \
  --fields "Company Name" "Email" "Phone"
```

**What happens during active learning:**
1. The tool presents pairs of records
2. The user presses `y` (match), `n` (not match), or `u` (unsure)
3. After ~15-20 labels, the model trains and clusters
4. Output CSV has a `GFV_Cluster_ID` column grouping duplicates

**Tell the user:**
> "Run this in your terminal. It will ask you to compare ~20 record pairs — press y/n/u for each. This trains the model. It should take about 2 minutes."

## Step 4: Analyze Results

Once the user completes the flow, read the output:

```python
import pandas as pd

df = pd.read_csv("deduplicated_data.csv")

# How many clusters (unique entities)?
n_clusters = df["GFV_Cluster_ID"].nunique()
n_total = len(df)
n_dupes = n_total - n_clusters
print(f"Found {n_dupes} duplicates across {n_clusters} unique entities")

# Show the clusters with duplicates
dupes = df.groupby("GFV_Cluster_ID").filter(lambda x: len(x) > 1)
for cluster_id, group in dupes.groupby("GFV_Cluster_ID"):
    print(f"\n--- Cluster {cluster_id} ({len(group)} records) ---")
    print(group[["Company Name", "Email", "Phone"]].to_string(index=False))
```

## Step 5: Merge Strategy

For each duplicate cluster, decide how to merge:

| Strategy | When to use | How |
|----------|-------------|-----|
| **Keep newest** | Time-series data with updates | Sort by date, keep last |
| **Keep most complete** | Records with varying fill rates | Pick the row with fewest nulls |
| **Merge fields** | Each record has different data | Combine non-null fields across rows |
| **Manual review** | High-value records (top accounts) | Present to CEO for decision |

```python
# Example: Merge by keeping most complete record per cluster
def merge_cluster(group):
    """Keep the record with the most non-null fields."""
    completeness = group.notna().sum(axis=1)
    return group.loc[completeness.idxmax()]

merged = df.groupby("GFV_Cluster_ID").apply(merge_cluster).reset_index(drop=True)
merged.to_csv("final_clean.csv", index=False)
```

## Output

```markdown
## Deduplication Results

- **Input:** [N] records from [filename]
- **Unique entities:** [M]
- **Duplicates found:** [N-M] ([percentage]%)
- **Merge strategy:** [which strategy was used]
- **Output file:** `deduplicated_data.csv`

### Top Duplicate Clusters
| Cluster | Records | Entity Name |
|---------|---------|-------------|
| 1 | 4 | Acme Corp / ACME Corporation / acme |
| 2 | 3 | Jane Doe / J. Doe / jane.doe@... |
```

## Integration

- Used by `/hubspot-architect` after CRM data imports
- Used by `/pipeline-pulse` to clean pipeline before analysis
- Pairs with `tools/gfv-dedupe.py` for the interactive flow
