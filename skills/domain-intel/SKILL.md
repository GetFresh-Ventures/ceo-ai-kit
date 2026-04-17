---
name: domain-intel
description: "Perform domain registration intelligence — WHOIS lookups, DNS analysis, SSL certificate inspection, and competitive domain research. Use when researching a prospect, auditing a client's domain infrastructure, or performing competitive intelligence."
short_description: "WHOIS lookups, DNS, and domain research"
---

# Domain Intelligence

Extract actionable infrastructure intelligence from domain names. Every data point should inform a business decision.


## Quick Start
Just say any of these:
- "Who owns [domain.com]?"
- "Research all domains registered by [company]"
- "Check DNS and hosting for [domain]"


## When to Use

- Pre-meeting research: "What can you tell me about [company].com?"
- Competitive analysis: "What domains do they own?"
- Client audit: "Check our domain setup"
- Due diligence: "Is this a legit company?"

## Step 1: WHOIS Lookup

```bash
# macOS/Linux (built-in)
whois example.com
```

```python
# Python (more structured)
# pip install python-whois
import whois

w = whois.whois("example.com")
print(f"Registrar:    {w.registrar}")
print(f"Created:      {w.creation_date}")
print(f"Expires:      {w.expiration_date}")
print(f"Name Servers: {w.name_servers}")
print(f"Status:       {w.status}")
print(f"Org:          {w.org}")
```

**What to extract:**

| Field | Intelligence value |
|-------|-------------------|
| `creation_date` | Company age indicator. Post-2023 = startup/new venture |
| `expiration_date` | Short renewals (1yr) = uncertain commitment. 5-10yr = established |
| `registrar` | GoDaddy/Namecheap = SMB. CSC/MarkMonitor = enterprise |
| `name_servers` | Reveals hosting: Cloudflare, AWS Route53, etc. |
| `org` | Registrant organization (if not privacy-protected) |
| `status` | `clientTransferProhibited` = locked down (good security) |

## Step 2: DNS Records

```bash
# A records (where the site hosts)
dig +short A example.com

# MX records (email provider)
dig +short MX example.com

# TXT records (SPF, DKIM, domain verification)
dig +short TXT example.com

# CNAME (CDN/proxy detection)
dig +short CNAME www.example.com

# All records
dig ANY example.com +noall +answer
```

**What DNS reveals:**

| Record | What it means |
|--------|--------------|
| A → Cloudflare IPs (104.x, 172.x) | Using Cloudflare CDN/proxy |
| A → AWS IPs | Hosting on AWS |
| MX → `aspmx.l.google.com` | Using Google Workspace |
| MX → `*.mail.protection.outlook.com` | Using Microsoft 365 |
| TXT with `v=spf1` | Email authentication configured |
| TXT with `_dmarc` | Email security policy set |
| CNAME → `*.shopify.com` | Shopify storefront |
| CNAME → `*.hubspotpagebuilder.com` | HubSpot CMS |

## Step 3: SSL/TLS Certificate

```bash
# Check certificate details
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -dates -subject -issuer
```

```python
import ssl, socket

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname="example.com") as s:
    s.connect(("example.com", 443))
    cert = s.getpeercert()
    print(f"Subject: {cert['subject']}")
    print(f"Issuer:  {cert['issuer']}")
    print(f"Expires: {cert['notAfter']}")
    # Check for wildcard, SAN entries
    for san in cert.get('subjectAltName', []):
        print(f"SAN: {san[1]}")
```

**Intelligence from certs:**
- Let's Encrypt = automated, budget-conscious
- DigiCert/Comodo = enterprise, paid SSL
- SAN entries reveal other domains/subdomains on same cert

## Step 4: Technology Detection

```bash
# HTTP headers reveal tech stack
curl -sI https://example.com | grep -iE "server:|x-powered-by:|x-cache:|via:"
```

| Header | Reveals |
|--------|---------|
| `Server: nginx` | Web server |
| `X-Powered-By: Express` | Node.js backend |
| `X-Cache: HIT` | CDN caching active |
| `Via: 1.1 varnish` | Varnish cache layer |

## Output Format

```markdown
## Domain Intelligence: [domain.com]

### Registration
- **Registrar:** [name]
- **Created:** [date] ([N] years old)
- **Expires:** [date] ([N]-year registration)
- **Privacy:** [Protected/Visible — org if visible]

### Infrastructure
- **Hosting:** [Provider] ([IP range])
- **CDN:** [Cloudflare/None/etc.]
- **Email:** [Google Workspace/M365/Other]
- **CMS:** [WordPress/Shopify/Custom/etc.]
- **SSL:** [Issuer, expiry]

### Security Posture
- SPF: [✅ Configured / ❌ Missing]
- DKIM: [✅ Configured / ❌ Missing]
- DMARC: [✅ Configured / ❌ Missing]
- Transfer Lock: [✅ / ❌]

### Assessment
[2-3 sentences: Is this a real, established company? Is their infrastructure
enterprise-grade or SMB? Any red flags?]
```

## Integration

- Feeds into `/competitive-intel` for market analysis
- Used by `/meeting-prep` for prospect research
- Used in due diligence for `/fundraise` and `/deal-review`

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| Client CRM | Real-time pipeline state | `hubspot-api` / `salesforce-api` |
| Local Memory | Client-specific facts | `gfv-brain-search.py` |

> **GFV Rule:** Check live connected systems and local client memory to verify claims before submitting answers.

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:
- **Missing Data** → Flag explicitly if a decision relies on unknown external variables.
- **Scope Creep** → Alert if the requested operation spans beyond immediate context goals.
- **Executive Bottlenecks** → Warn if the action plan relies entirely on unassigned human approval gates.
- **Financial Risk** → Call out actions that may trigger unexpected OPEX burn (e.g. infinite LLM agent loops).

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Process Map | A mermaid.js chronological diagram |
| Executive Decision | BOTTOM LINE FIRST layout with options + trade-offs |
| Data Audit | A structured table grouping issues by severity |
| Code Execution | Isolated, copy-ready code blocks + terminal commands |

## Confidence Tagging

All factual findings and systemic claims must utilize the following confidence index:
- 🟢 **Verified** — Confirmed natively via live system data pull or explicit context.
- 🟡 **Medium** — Deduced from local memory logs or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next:
- "Try `competitive-intel` — Track competitors and market positioning"
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `hubspot-architect` — Build HubSpot CRM integrations and pipelines"
