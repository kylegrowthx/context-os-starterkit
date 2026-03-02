# Competitors Raw Data

Raw API outputs from competitive landscape analysis for Flodesk.

## Files

| File | Source | Description | Pulled |
|---|---|---|---|
| `semrush-domain-rank-all.csv` | SEMRush `domain_rank` (US database) | SEMRush Rank, organic keywords, organic traffic, organic traffic value, Adwords metrics for all 34 domains (32 competitors + Marigold alternate domains) | 2026-02-28 |
| `dataforseo-domain-rank-overview.json` | DataForSEO `domain_rank_overview` (US/English) | Keyword position distribution (pos 1 through 91-100), ETV, keyword count, rising/declining/new keyword counts for 11 key competitors | 2026-02-28 |

## Notes

- SEMRush data is from the US database only
- DataForSEO position data covers US/English queries with `ignore_synonyms: true`
- Substack (substack.com) and Zoho (zoho.com) metrics include platform/suite-wide data, not just their email marketing products
- Marigold Engage was checked across three domains: marigold.com (no data), meetmarigold.com (984 keywords), sailthru.com (111 keywords)
- DataForSEO backlinks_bulk_ranks was not available (requires separate subscription)
