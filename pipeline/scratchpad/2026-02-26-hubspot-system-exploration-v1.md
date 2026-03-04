# HubSpot System Exploration — Raw Notes

<metadata>
purpose: Raw exploration notes from HubSpot MCP deep dive for GrowthX
audience: Internal — Marcel, engineering, operations
related_files:
  - knowledge/hubspot-crm-system-guide-v1.md
domain: operations
confidence: high
last_updated: 2026-02-26
</metadata>

## Account Info

- **Portal ID**: 341940338
- **Owner**: Marcel Santilli (marcel@growthx.ai), Owner ID 259928054
- **Account Type**: STANDARD
- **Time Zone**: America/Los_Angeles (UTC-8)
- **Currency**: USD
- **UI Domain**: app-na3.hubspot.com
- **Data Hosting**: na3

---

## Object Types

### Standard Objects (Active)
- **Contacts** (0-1) — ~700+ properties, 23 property groups
- **Companies** (0-2) — ~234 properties, 20 property groups
- **Deals** (0-3) — ~444 properties, 23 property groups
- **Leads** (0-136) — separate lead object
- **Tickets** — no API access (missing scope)
- **Line Items** — associated with deals for revenue tracking

### Custom Objects (via Hapily integration)
- **hapily_registrant** (2-159540856) — Event registrants from Luma
- **hapily_session** (2-159540861) — Event sessions
- **hapily_event** (2-159540866) — Events from Luma

---

## Association Definitions

### Contact → Company
- Primary (typeId: 1)
- Billing Contact (typeId: 931)
- Unlabeled (typeId: 279)

### Contact → Deal
- Unlabeled (typeId: 4)

### Deal → Company
- Primary (typeId: 5)
- Unlabeled (typeId: 341)

### Deal → Line Item
- Unlabeled (typeId: 19)

---

## Pipelines and Stages

### 1. New Business Pipeline (default, "New Business")
| Order | Stage | Emoji |
|-------|-------|-------|
| 1 | Intro | 👋 |
| 2 | Engaged | ✅ |
| 3 | Proposal | 📝 |
| 4 | Contract | ✍️ |
| 5 | Won | 🎉 |
| 6 | Lost | ❌ |
| 7 | Debook | ❌ |

### 2. Expansion Pipeline ("Expansion (Existing Business)")
| Order | Stage |
|-------|-------|
| 1 | Appointment Scheduled |
| 2 | Qualified To Buy |
| 3 | Presentation Scheduled |
| 4 | Decision Maker Bought-In |
| 5 | Contract Sent |
| 6 | Closed Won |
| 7 | Closed Lost |

### 3. Renewal Pipeline ("Renewal (Existing Business)")
| Order | Stage |
|-------|-------|
| 1 | Appointment Scheduled |
| 2 | Qualified To Buy |
| 3 | Presentation Scheduled |
| 4 | Decision Maker Bought-In |
| 5 | Contract Sent |
| 6 | Closed Won |
| 7 | Closed Lost |

---

## Key Enumerations

### Deal Type
- New Business
- Expansion
- Renewal
- Renewal - Upsell
- Renewal - Downsell

### Contract Type (workstream_type)
- Sprint + Growth Execution
- Pilot + Workstream
- Standard Terms (Just Workstream)
- Other

### Contact Lifecycle Stage
- Subscriber → Lead → MQL → SQL → Opportunity → Customer → Evangelist → Other

### Contact Lead Status
- New → Open → In Progress → Open Deal → Unqualified → Attempted to Contact → Connected → Bad Timing

### Company Account Stage
- Prospect → Pipeline → Customer → Churned → Lost Deal → Competitor

### Company Fit Score
- Good / Medium / Low

---

## Contact Property Groups (Custom)

### ai-led_growth (3 props)
- `content_name` — Name of content requested (lead magnet)
- `content_url` — URL/link to requested content
- `marketing_consent` — Marketing consent status

### default_(inbound)_enrichment (31 props)
Enriched via Default.com inbound workflow + Clay:
- Company info: `annual_revenue__via_default_`, `company_domain__via_default_`, `company_name__via_default_`
- Traffic data (via Clay): `organic_search_visits__via_clay_`, `organic_social_visits__via_clay_`, `total_users__via_clay_`, `average_pages_per_visit__via_clay_`, `average_time_on_site__via_clay_`, `traffic_rank__via_default_`
- Meeting tracking: `meeting_booked_via_inbound_flow__via_default_`, `booked_meeting_owner__via_default_`
- Form data: `date_of_initial_sales_form_submission__via_default_`, `context_for_discussion__via_default_`
- Automation triggers: `trigger_did_not_book_outreach_via_zapier`, `trigger_dq_outreach_via_zapier`

### luma_events (9 props)
Event attendance tracking:
- `attended___ai_gtm_exec_dinner`
- `attended___growthx___understory_breakfast`
- `attended___inbound_hh`
- `attended___own_the_ai_front_pg_webinar`
- `attended_physical_event`
- `attended_virtual_event`
- `date_of_most_recent_luma_activity`
- `date_of_most_recent_luma__approved__activity`

### calendly (20 props)
- 10 question/answer pairs for Calendly booking forms

### outboundsync_custom_properties (52 props)
OutboundSync (Instantly/HeyReach) tracking:
- Email campaign tracking: `os_last_campaign_name`, `os_last_email_campaign_name`
- Reply tracking: `os_last_reply_message`, `os_last_reply_subject`, `os_last_reply_time`
- Engagement tracking: `os_last_open_time`, `os_last_link_click_url`, `os_last_sent_message`
- LinkedIn tracking: `os_last_like_post_url`, `os_last_follow_sender`

### event_hapily_triggers (6 props)
Hapily event integration trigger properties

### rb2b_properties (9 props)
RB2B website visitor identification

### koalify_duplicates (5 props)
Duplicate detection and management

### Key custom fields on contacts
- `company_fit_score` — ICP alignment (Good/Medium/Low), synced from company
- `company___of_employees` — Employee count (number type, synced from company)
- `company_funding` — Funding amount, synced from company
- `contact_tags` — GTM filtering tags
- `beehiiv_subscriber` — Newsletter subscriber flag
- `competitor` — Competitor flag
- `best_performing_channel` — Attribution
- `first_touch_channel` — First attribution touch
- `clay_enrichment_date` — Last Clay enrichment timestamp
- `employment_seniority_tier` — Seniority level
- `gtm_role` — GTM role classification

---

## Company Property Groups (Custom)

### health_score (7 props)
Client health scoring system:
- `relationship_score` (0.5-5) — Trust and stakeholder relationship strength
- `strategyconfidence_score` (0.5-5) — Confidence in 3-6 month plan
- `qualitycontractual_fulfillment_score` (0.5-5) — Delivering on promises
- `performanceroi_score` (0.5-5) — Driving results they care about
- `content_quality_score` (0.5-5) — Quality of content produced
- `health_score_calculated` — Sum of all 5 dimensions
- `health_tier` — Classification based on health score

### semrush_data (12 props)
SEMrush traffic analytics:
- `semrush__total_users`, `semrush__total_visits`, `semrush__traffic_rank`
- `organic_search_visits`, `organic_social_visits`, `paid_search_visits`, `paid_social_visits`
- `referral_visits`, `search_visits`, `average_pages_per_visit`, `average_time_on_site`

### event_information (3 props)
- `event_attendance_trigger`, `latest_event_attended`, `latest_event_attended_date`

### Key custom fields on companies
- `fit_score` — ICP alignment (Good/Medium/Low)
- `account_stage` — Prospect/Pipeline/Customer/Churned/Lost Deal/Competitor
- `managing_director` — Assigned Engagement Manager
- `funding`, `funding__raw_` — Funding data
- `domain_authority` — SEO domain authority
- `company_site_traffic` — Website traffic
- `billing_address`, `billing_email` — Billing info
- `slack_channel__internal` — Internal Slack channel for client
- `active_annualized_mrr` — Rollup of active deal MRR
- `of_contacts_w__luma__approved__status` — Luma event engagement count
- `relationship_type` — Company relationship classification
- `sales_prospecting_tier` — Sales targeting tier

---

## Deal Property Groups (Custom)

### account_potential (7 props)
ICP scoring matrix for new deals:
- `content_track_record` (1-5) — Publishing frequency/volume
- `domain_authority` (1-5) — SEO domain authority score
- `funding_establishment` (1-5) — Financial stability
- `growth_trajectory` (1-5) — Company growth signals
- `logo_values` (1-5) — Brand recognition value
- `account_potential_score` — Calculated total
- `account_potential_decision` — Final decision

### contract_information (13 props)
- `contract_start_date`, `end_date`, `contract_end_date__calculated_`
- `renewal_date` — Contract end date + 1
- `billing_frequency` — Monthly/Quarterly/Semi-Annually/Annually
- `billing_timing` — When payment is due relative to service delivery
- `billing_details` — Free text
- `auto_renewal` — Auto-renew flag
- `payment_terms__net_days_` — Net days for payment
- `term____months_` — Contract term in months
- `term__weeks` — Contract term in weeks
- `cancellation_details` — Renewal/cancellation notes

### engagement_score (5 props)
BANT-style engagement scoring:
- Budget, Authority, Trust, Enthusiasm, Urgency scoring

### icp_matrix (scoring dimensions)
ICP scoring with dimensions like:
- Approval layers, budget alignment, content complexity
- Domain strength, exec sponsor access, ICP industry fit
- Market position, organic maturity, team readiness

### partnership_fit (scoring dimensions)
Partnership fit scoring:
- Approval process, champion quality, content philosophy
- Execution complexity, growth trajectory, revenue potential

### services_qualification_matrix
Services qualification scoring dimensions

### prior_deal_information
- Prior deal amount, ARR, MRR, contract dates, renewal dates

### next_renewal_deal_information
- Next renewal cycle tracking

### recurring_revenue_information
- MRR/ARR tracking properties

### attio_deal_info (9 props)
Migration fields from Attio CRM:
- `attio_deal_record_id`, `attio_company_record_id`
- `attio_deal_name`, `attio_deal_stage`, `attio_deal_value`
- `attio_deal_close_date`, `attio_deal_created_at`, `attio_deal_days_to_close`
- `attio_deal_closed_lost_detail`

### Key custom fields on deals
- `workstream_type` — Contract type (Sprint, Pilot, Standard, Other)
- `closed_lost_reason`, `closed_won_reason`
- `don_t_include_in_slack_ping` — Exclude from Slack notifications
- BANT fields: `budget`, `authority`, `need`, `timing`

---

## Workflows (88 total, 50+ active)

### Sales Inbound (Contact-based)
1. **New Sales Inbound Submission (via Default)** — ACTIVE, 109 revisions — Main inbound flow
2. **New Sales Inbound Submission - Did Not Complete 2nd Form** — ACTIVE — Follow-up for incomplete forms
3. **Push Default Enrichment to Contact Main Fields** — ACTIVE — Copy enrichment data to standard fields
4. **Push Default Enrichment to Company Main Fields** — ACTIVE — Copy enrichment data to company
5. **AI-Led Growth Resource Request** — ACTIVE, 34 revisions — Content/lead magnet delivery
6. **Send follow-up email after form submission** — ACTIVE

### Deal Pipeline Management
7. **Stamp Close Date on Won/Lost Deals** — ACTIVE — Auto-set close date
8. **Based on Pipeline, set Deal Type** — ACTIVE — Auto-classify deal type
9. **Deal - New Biz Pipe - Update Deal Name** — ACTIVE — Auto-format deal names
10. **Push Company SEMrush data to Newly Created New Biz Deal** — ACTIVE — Enrich new deals
11. **Plug in Value for Associated Sprint/Growth Record ID** — ACTIVE — Link related deals
12. **Confirm Line Items value for Closed Won New Biz** — ACTIVE — Revenue validation
13. **Set Line Items for Closed Won Validation** — ACTIVE
14. **Auto Generate Growth Deal for Sprint when entering Contract Stage** — ACTIVE — Create growth deal from sprint
15. **Update Associated Sprint/Growth Execution Deal ID** — ACTIVE — Cross-reference deals
16. **Make primary contact MQL when deal is created** — ACTIVE — Lifecycle stage promotion
17. **Create lead when MQL created** — ACTIVE — Lead object creation
18. **Contract is Active - T/F** — ACTIVE — Active contract flag
19. **Populate Contract End Date** — ACTIVE — Calculate end dates
20. **Data Update - Attribution Valid?** — ACTIVE — Validate attribution data

### Renewal Automation
21. **Create Renewal - WF #1 | Closed Won New Business** — ACTIVE, 34 revisions
22. **Create Renewal - WF #2 | Renewal Cycle = Odd** — ACTIVE, 22 revisions
23. **Create Renewal - WF #3 | Renewal Closed Won - Cycle = Even** — ACTIVE
24. **90 Day Renewal Alert** — ACTIVE — Slack notification
25. **60 Day Renewal Alert** — ACTIVE — Slack notification
26. **30 Day Renewal Alert** — ACTIVE — Slack notification
27. **Closed Lost Renewals** — ACTIVE

### Company Data Sync
28. **One-off | Set Company Name on Contact** — ACTIVE
29. **Set Enrichment Status | Company | Clay Enrichment Date Set** — ACTIVE
30. **Sync Deal Count to Contacts | Company** — ACTIVE
31. **Set Company Fit Score | Revenue or Funding Updated** — ACTIVE — ICP scoring
32. **Sync Company Fit Score to Contacts** — ACTIVE
33. **Sync Company # of Employees to Contacts** — ACTIVE
34. **Sync Company Managing Director to Contacts** — ACTIVE
35. **Set Account Potential - Funding/Establishment** — ACTIVE
36. **Set Account Stage to "Customer"** — ACTIVE

### Outbound/Channel Tracking
37. **First Instantly Touch Date Timestamp** — ACTIVE
38. **First HeyReach Touch Date Timestamp** — ACTIVE
39. **Best Performing Channel** — ACTIVE
40. **First Touch Channel** — ACTIVE
41. **Active on HeyReach and Instantly Update** — ACTIVE
42. **Has Replied tag** — ACTIVE

### Contact Record Management
43. **Contact Record - Set Location** — ACTIVE
44. **Temp - set attended event fields** — ACTIVE

### Event (Hapily) Workflows
45. **event•hapily | New Registrant Created** — ACTIVE, 14 revisions
46. **event•hapily | Registrant Attends** — ACTIVE
47. **event•hapily | Company Associated to Event** — ACTIVE
48. **event•hapily | Deal Attribution** — ACTIVE
49. **event•hapily | Deal Closed Won | Set Event Influenced Close Trigger** — ACTIVE
50. **event•hapily | Associate Event to Deal (Influenced Close Won)** — ACTIVE
51. **event•hapily | Associate Event to Deal (Influenced Creation)** — ACTIVE
52. **event•hapily | Deal Created | Set Event Influenced Creation Trigger** — ACTIVE
53. **Events - Copy Luma data from contact to company** — ACTIVE
54. Various webhook workflows for event/session/registrant sync — ACTIVE

### Disabled/Archived
- OutboundSync workflows (6) — Disabled
- Slack notification workflows — Disabled
- Old inbound submission flow — Disabled
- Various test/unnamed workflows — Disabled

---

## Integration Stack (visible in HubSpot data)

### Active Integrations
- **Default.com** — Inbound form routing, enrichment, meeting booking
- **Clay** — Contact and company enrichment (traffic data, firmographics)
- **Hapily** — Luma event sync (registrants, sessions, events → HubSpot)
- **Calendly** — Meeting booking data (20 custom properties)
- **OutboundSync** — Instantly + HeyReach outbound campaign tracking (52 properties)
- **RB2B** — Website visitor identification (9 properties)
- **Koalify** — Duplicate detection and management
- **Syft** — Website analytics, intent signals, purchase intent tracking
- **SEMrush** — Traffic analytics data pushed to company records
- **Luma** — Event management (synced via Hapily)
- **beehiiv** — Newsletter subscriber flag on contacts

### Historical/Migration
- **Attio** — Previous CRM, migration fields still present on contacts, companies, deals
- **Zapier** — Used for some automation triggers (Default workflow)

---

## Deal Naming Convention
Pattern: `{Company} - {Type} - {Month Year}`
Examples:
- "Tavus - Strategy Sprint - July 2025"
- "Diligent - Growth Execution - Aug 2025"
- "LILT - New Biz - May 2025 ✅" (checkmark for won)
- "Mejuri - New Biz - June 2025"
