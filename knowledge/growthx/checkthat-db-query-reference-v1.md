# CheckThat DB Query Reference via Render MCP

<metadata>
purpose: Reusable query reference for analyzing CheckThat data via Render MCP
audience: GrowthX team, AI agents
related_files: products/checkthat/architecture.mdx, products/checkthat/metrics.mdx
domain: product, data-analysis
confidence: high
last_updated: 2026-02-23
</metadata>

## Connection Details

| Parameter | Value |
|-----------|-------|
| MCP Tool | `query_render_postgres` |
| Postgres ID | `dpg-d2sbu3odl3ps73ebrvkg-a` |
| Database Name | `checkthat_pg` |
| Render Workspace | GrowthX (`tea-csp5nhl6l47c73b2vip0`) |
| Plan | Pro 128GB, 2TB disk |
| Read Replica | `dpg-d2sbu3odl3ps73ebrvkg-b` |

All queries are **read-only** (wrapped in a read-only transaction by the MCP tool).

---

## Schema Overview

### Entity Relationship Map

```
workspaces
  ├── brand_id → brands (primary brand)
  ├── workspace_competitors → brands (competitor brands)
  ├── prompts → topics
  ├── snapshots
  │     ├── BrandPerception (workspace-level or subcategory-level)
  │     ├── BrandPromptPerformance (prompt-level)
  │     ├── CitedUrl (URL-level citations)
  │     └── CitedDomain (domain-level citations)
  ├── brand_contexts
  ├── personas
  ├── tags
  └── topics

probes (AI responses)
  ├── prompt_id → prompts
  ├── probe_mentions → brands
  └── probe_citations (URLs)
```

### Snapshot Architecture

Snapshots use Rails delegated types. The `snapshots` table is the container; the metrics live in the linked type table.

| scope_type | snapshotable_type | What It Tracks | Volume (Webflow) |
|------------|-------------------|----------------|------------------|
| `Workspace` | `BrandPerception` | Overall brand scores per day | 1,030 |
| `Subcategorization` | `BrandPerception` | Subcategory-level brand scores | 720 |
| `Prompt` | `BrandPromptPerformance` | Per-prompt brand metrics | 59,756 |
| `Workspace` | `CitedUrl` | URL-level citation tracking | 199,046 |
| `Workspace` | `CitedDomain` | Domain-level citation tracking | 82,043 |

### AI Engines Tracked

| Vendor | Model |
|--------|-------|
| Anthropic | claude-haiku-4-5 |
| Google Gemini | gemini-2.0-flash |
| Google AI Overview | ai-overview |
| OpenAI | gpt-5-mini |
| Perplexity | sonar |

---

## Core Tables

### workspaces

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| name | varchar | Workspace display name |
| brand_id | uuid | FK → brands (primary brand) |
| pricing_plan | varchar | e.g. `unlimited_v1` |
| trial_started_at | timestamp | Nullable |
| trial_duration_days | integer | Nullable |
| deleted_at | timestamp | Soft delete |
| created_at / updated_at | timestamp | |

### brands

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| name | varchar | Brand display name |
| url | varchar | Primary URL |
| domain | varchar | Primary domain |
| slug | varchar | URL-safe identifier |
| description | text | |
| location | varchar | |
| aliases | array | Alternative brand names |
| secondary_urls | array | |
| secondary_domains | array | |
| mentions_count | integer | Global mention count |
| featured | boolean | |
| is_growthx_client | boolean | |
| public | boolean | |
| primary_color | varchar | |
| flagged_at / flagged_reason | | Content moderation |

### snapshots

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| workspace_id | uuid | FK → workspaces |
| brand_id | uuid | FK → brands |
| captured_date | date | The measurement date |
| scope_type | varchar | `Workspace`, `Prompt`, `Subcategorization` |
| scope_id | uuid | FK → the scope entity |
| snapshotable_type | varchar | `BrandPerception`, `BrandPromptPerformance`, `CitedUrl`, `CitedDomain` |
| snapshotable_id | uuid | FK → the metrics entity |
| developed | boolean | |
| subject | varchar | |

### brand_perceptions

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK (joined via snapshots.snapshotable_id) |
| visibility_score | float | 0-100, primary metric |
| sentiment_score | float | 0-100 |
| citation_rate | float | % of probes with brand citations |
| citation_share | float | % of all citations belonging to brand |
| avg_position | float | Average mention rank |
| top3_percentage | float | % mentions in positions 1-3 |
| middle_percentage | float | % mentions in middle positions |
| bottom_percentage | float | % mentions in bottom positions |
| positive_sentiment_percentage | float | |
| neutral_sentiment_percentage | float | |
| negative_sentiment_percentage | float | |
| total_probes | integer | Total probes in scope |
| total_mentions | integer | Brand mentions found |
| total_citations | integer | Brand citations found |
| scope_citation_count | integer | Total citations across all brands in scope |

### brand_prompt_performances

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK (joined via snapshots.snapshotable_id) |
| visibility_score | float | 0-100 |
| citation_rate | float | |
| citation_share | float | |
| share_of_voice | float | Brand's share vs competitors |
| sentiment_score | float | |
| avg_position | float | |
| top3_percentage | float | |
| middle_percentage | float | |
| bottom_percentage | float | |
| total_probes | integer | |
| total_mentions | integer | |
| total_citations | integer | |
| responses_with_citations | integer | |
| positive_count / negative_count | integer | |
| prompt_total_mentions | integer | All brand mentions for this prompt |
| prompt_total_citations | integer | All brand citations for this prompt |

### probes

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| prompt_id | uuid | FK → prompts |
| vendor | varchar | AI engine vendor |
| model | varchar | Specific model |
| raw_response | text | Full AI response |
| response | varchar | Processed response |
| captured_date | date | |
| run_id | varchar | Batch identifier |
| mentions_s3_url | varchar | S3 link to extracted mentions |
| citations_s3_url | varchar | S3 link to extracted citations |
| raw_results_s3_url | varchar | S3 link to raw results |

### probe_mentions

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| probe_id | uuid | FK → probes |
| brand_id | uuid | FK → brands |
| brand_name | varchar | As mentioned in response |
| product | varchar | Specific product mentioned |
| sentiment | varchar | positive/neutral/negative |
| rank | integer | Position in response |
| out_of | integer | Total brands mentioned |

### probe_citations

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| probe_id | uuid | FK → probes |
| url | varchar | Cited URL |
| domain | varchar | Cited domain |
| name | varchar | Citation title |
| rank | integer | Citation position |
| scraped_url | varchar | Resolved URL |
| scraped_domain | varchar | Resolved domain |
| jina_content | text | Scraped page content |
| jina_title | varchar | |
| jina_description | varchar | |
| jina_tokens | integer | Token count |

### prompts

| Column | Type | Notes |
|--------|------|-------|
| id | uuid | PK |
| workspace_id | uuid | FK → workspaces |
| topic_id | uuid | FK → topics |
| content | text | The prompt text |
| funnel_stage | varchar | Buyer journey stage |
| likelihood | varchar | |
| specificity | varchar | |
| relevance | varchar | |
| active | boolean | Currently tracked |
| branded | boolean | Contains brand name |
| leaderboard | boolean | Used in leaderboard |
| pending_review | boolean | |
| llm_visibility_study | boolean | |
| source_metadata | jsonb | |

### categories / subcategories / subcategorizations

Categories are hierarchical. Brands and prompts connect to subcategories via the polymorphic `subcategorizations` join table.

| Table | Key Columns |
|-------|-------------|
| categories | id, name, slug, description |
| subcategories | id, category_id, name, slug, featured, description |
| subcategorizations | id, subcategory_id, subcategorizable_type, subcategorizable_id, primary |

---

## Ready-to-Use Queries

Replace `'WORKSPACE_ID'` with your target workspace UUID.

### 1. Workspace Overview

```sql
SELECT
  w.name AS workspace,
  b.name AS primary_brand,
  b.url,
  w.pricing_plan,
  w.created_at,
  (SELECT COUNT(*) FROM prompts WHERE workspace_id = w.id) AS prompt_count,
  (SELECT COUNT(*) FROM workspace_competitors WHERE workspace_id = w.id) AS competitor_count,
  (SELECT COUNT(DISTINCT captured_date) FROM snapshots WHERE workspace_id = w.id) AS tracking_days,
  (SELECT MIN(captured_date) FROM snapshots WHERE workspace_id = w.id) AS first_tracked,
  (SELECT MAX(captured_date) FROM snapshots WHERE workspace_id = w.id) AS last_tracked
FROM workspaces w
JOIN brands b ON w.brand_id = b.id
WHERE w.id = 'WORKSPACE_ID';
```

### 2. Competitors List

```sql
SELECT b.name, b.url, b.domain
FROM workspace_competitors wc
JOIN brands b ON wc.brand_id = b.id
WHERE wc.workspace_id = 'WORKSPACE_ID'
ORDER BY b.name;
```

### 3. Latest Brand Leaderboard (All Brands, Workspace-Level)

```sql
SELECT
  s.captured_date,
  b.name AS brand,
  bp.visibility_score,
  bp.sentiment_score,
  bp.citation_rate,
  bp.citation_share,
  bp.avg_position,
  bp.top3_percentage,
  bp.total_mentions,
  bp.total_citations,
  bp.total_probes
FROM snapshots s
JOIN brand_perceptions bp
  ON s.snapshotable_id = bp.id
  AND s.snapshotable_type = 'BrandPerception'
JOIN brands b ON s.brand_id = b.id
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.scope_type = 'Workspace'
  AND s.captured_date = (
    SELECT MAX(captured_date)
    FROM snapshots
    WHERE workspace_id = 'WORKSPACE_ID'
  )
ORDER BY bp.visibility_score DESC;
```

### 4. Primary Brand Trend Over Time

```sql
SELECT
  s.captured_date,
  bp.visibility_score,
  bp.sentiment_score,
  bp.citation_rate,
  bp.citation_share,
  bp.total_mentions,
  bp.total_citations
FROM snapshots s
JOIN brand_perceptions bp
  ON s.snapshotable_id = bp.id
  AND s.snapshotable_type = 'BrandPerception'
JOIN workspaces w
  ON w.id = 'WORKSPACE_ID'
  AND s.brand_id = w.brand_id
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.scope_type = 'Workspace'
ORDER BY s.captured_date DESC;
```

### 5. Competitor Trend Comparison (Visibility Over Time)

```sql
SELECT
  s.captured_date,
  b.name AS brand,
  bp.visibility_score,
  bp.sentiment_score,
  bp.citation_rate
FROM snapshots s
JOIN brand_perceptions bp
  ON s.snapshotable_id = bp.id
  AND s.snapshotable_type = 'BrandPerception'
JOIN brands b ON s.brand_id = b.id
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.scope_type = 'Workspace'
ORDER BY s.captured_date DESC, bp.visibility_score DESC;
```

### 6. Top Prompts by Visibility (Primary Brand, Latest Date)

```sql
SELECT
  p.content AS prompt,
  bpp.visibility_score,
  bpp.share_of_voice,
  bpp.sentiment_score,
  bpp.citation_rate,
  bpp.total_mentions,
  bpp.total_probes
FROM snapshots s
JOIN brand_prompt_performances bpp
  ON s.snapshotable_id = bpp.id
  AND s.snapshotable_type = 'BrandPromptPerformance'
JOIN prompts p
  ON s.scope_id = p.id
  AND s.scope_type = 'Prompt'
JOIN workspaces w
  ON w.id = 'WORKSPACE_ID'
  AND s.brand_id = w.brand_id
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.captured_date = (
    SELECT MAX(captured_date)
    FROM snapshots
    WHERE workspace_id = 'WORKSPACE_ID'
  )
ORDER BY bpp.visibility_score DESC
LIMIT 20;
```

### 7. Worst Performing Prompts (Primary Brand, Latest Date)

```sql
SELECT
  p.content AS prompt,
  bpp.visibility_score,
  bpp.share_of_voice,
  bpp.sentiment_score,
  bpp.citation_rate,
  bpp.total_mentions
FROM snapshots s
JOIN brand_prompt_performances bpp
  ON s.snapshotable_id = bpp.id
  AND s.snapshotable_type = 'BrandPromptPerformance'
JOIN prompts p
  ON s.scope_id = p.id
  AND s.scope_type = 'Prompt'
JOIN workspaces w
  ON w.id = 'WORKSPACE_ID'
  AND s.brand_id = w.brand_id
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.captured_date = (
    SELECT MAX(captured_date)
    FROM snapshots
    WHERE workspace_id = 'WORKSPACE_ID'
  )
ORDER BY bpp.visibility_score ASC
LIMIT 20;
```

### 8. AI Engine Breakdown (Which Models Are Tracked)

```sql
SELECT DISTINCT pr.vendor, pr.model
FROM probes pr
JOIN prompts p ON pr.prompt_id = p.id
WHERE p.workspace_id = 'WORKSPACE_ID'
ORDER BY pr.vendor, pr.model;
```

### 9. Top Cited Domains (Latest Date)

```sql
SELECT
  s.captured_date,
  cd.domain,
  cd.citation_count,
  cd.probes_count,
  cd.citation_rate
FROM snapshots s
JOIN cited_domains cd
  ON s.snapshotable_id = cd.id
  AND s.snapshotable_type = 'CitedDomain'
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.scope_type = 'Workspace'
  AND s.captured_date = (
    SELECT MAX(captured_date)
    FROM snapshots
    WHERE workspace_id = 'WORKSPACE_ID'
  )
ORDER BY cd.citation_count DESC
LIMIT 25;
```

### 10. Top Cited URLs (Latest Date)

```sql
SELECT
  s.captured_date,
  cu.url,
  cu.page_title,
  cu.domain,
  cu.citation_count,
  cu.probes_count,
  cu.citation_rate
FROM snapshots s
JOIN cited_urls cu
  ON s.snapshotable_id = cu.id
  AND s.snapshotable_type = 'CitedUrl'
WHERE s.workspace_id = 'WORKSPACE_ID'
  AND s.scope_type = 'Workspace'
  AND s.captured_date = (
    SELECT MAX(captured_date)
    FROM snapshots
    WHERE workspace_id = 'WORKSPACE_ID'
  )
ORDER BY cu.citation_count DESC
LIMIT 25;
```

### 11. Prompt List with Classification

```sql
SELECT
  p.content,
  p.funnel_stage,
  p.likelihood,
  p.specificity,
  p.relevance,
  p.branded,
  p.active,
  t.name AS topic
FROM prompts p
LEFT JOIN topics t ON p.topic_id = t.id
WHERE p.workspace_id = 'WORKSPACE_ID'
ORDER BY p.content;
```

### 12. Raw Probe Data (Sample)

```sql
SELECT
  pr.vendor,
  pr.model,
  pr.captured_date,
  p.content AS prompt,
  LEFT(pr.response, 500) AS response_preview
FROM probes pr
JOIN prompts p ON pr.prompt_id = p.id
WHERE p.workspace_id = 'WORKSPACE_ID'
ORDER BY pr.captured_date DESC
LIMIT 10;
```

### 13. Mention Sentiment Distribution by Brand

```sql
SELECT
  b.name AS brand,
  pm.sentiment,
  COUNT(*) AS mention_count
FROM probe_mentions pm
JOIN probes pr ON pm.probe_id = pr.id
JOIN prompts p ON pr.prompt_id = p.id
JOIN brands b ON pm.brand_id = b.id
WHERE p.workspace_id = 'WORKSPACE_ID'
GROUP BY b.name, pm.sentiment
ORDER BY b.name, mention_count DESC;
```

---

## Known Workspace IDs

| Workspace | UUID | Primary Brand |
|-----------|------|---------------|
| Webflow | `db07e5a9-6236-44ba-836e-5ca12138960d` | Webflow |

To find other workspaces:

```sql
SELECT w.id, w.name, b.name AS brand, w.pricing_plan, w.created_at
FROM workspaces w
JOIN brands b ON w.brand_id = b.id
WHERE w.deleted_at IS NULL
ORDER BY w.name;
```
