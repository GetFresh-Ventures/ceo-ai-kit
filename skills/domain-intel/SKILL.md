---
name: domain-intel
description: Domain registration intelligence for competitive analysis. WHOIS, DNS, nameserver, and expiry tracking.
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Revenue Enablement
---

# /domain-intel

**Usage**: Research domain ownership, registration history, DNS configuration, and expiry dates for competitive intelligence and deal research.

## Capabilities

### 1. WHOIS Lookup
- Registrar, registration date, expiry date, nameservers.
- Registrant organization (when not privacy-protected).
- Domain status codes (clientTransferProhibited, etc.).

### 2. Competitive DNS Analysis
- Identify hosting providers (AWS, Cloudflare, GoDaddy, etc.).
- Detect CDN usage and email providers (MX records).
- Map technology stack from DNS footprint.

### 3. Expiry Monitoring
- Track competitor domain expiry dates.
- Alert when domains in your niche become available.
- Monitor newly registered domains in your industry category.

### 4. Deal Research Application
- Before any partnership or acquisition discussion, pull domain intel.
- Cross-reference with CRM data for enrichment.
- Feed findings into `meeting-prep` dossiers.

## Implementation
- Uses RDAP protocol (modern WHOIS replacement). No API key required.
- Fallback to traditional WHOIS via CLI tools.
- Results cached for 24 hours to avoid rate limiting.
