<metadata>
purpose: Reference guide for the HubSpot deal object — all property groups, key fields, and business logic embedded in the GrowthX HubSpot setup
audience: AI assistant, ops team, anyone using HubSpot MCP
related: docs/business/, records/customers/
domain: operations, crm, hubspot
confidence: high
last_updated: 2026-02-19
</metadata>

# HubSpot Deal Object Reference

This document maps the complete deal object in GrowthX's HubSpot account. Load this when using the HubSpot MCP server to query, create, or update deals. It covers every property group, key fields within each group, and the business logic embedded in the setup.

---

## How to use this reference

When writing HubSpot API calls:
- Use the `name` value (e.g., `dealname`, `hs_mrr`) as the property key — not the label
- Enumeration fields require specific option values — check the field descriptions for valid values
- System fields prefixed with `hs_` are set automatically by HubSpot; don't try to write to read-only ones
- Custom fields (no `hs_` prefix, no standard HubSpot description) are GrowthX-specific

---

## Property groups overview

| Group name | What it contains |
|---|---|
| `dealinformation` | Core deal fields, lifecycle, system metadata |
| `deal_activity` | Sales activity, BANT, pipeline/stage, contact counts |
| `deal_revenue` | Amount, MRR, ARR, ACV, TCV, currency |
| `contract_information` | Contract dates, billing, terms, auto-renewal |
| `icp_matrix` | Custom ICP scoring dimensions (Zapier-calculated) |
| `engagement_score` | Custom pre-sales engagement scoring |
| `partnership_fit` | Custom partnership fit scoring |
| `account_potential` | Custom account potential scoring |
| `prior_deal_information` | Renewal context — prior deal financials and dates |
| `next_renewal_deal_information` | Renewal automation — cycle tracking for workflow logic |
| `dealstages` | Stage timing: entry/exit dates, cumulative time per stage |
| `dealscripted` | HubSpot computed fields (read-only) |
| `hubspotmetrics` | HubSpot pipeline metrics (read-only) |
| `analyticsinformation` | UTM/traffic source attribution |
| `predictive_deal_score_feature_properties` | HubSpot AI deal scoring inputs |
| `recurring_revenue_information` | MRR tracking for revenue reporting |
| `semrush_data` | SEMrush integration: organic/paid traffic data |
| `attio_deal_info` | Legacy — migration data from Attio (prior CRM) |
| `koalify_duplicates` | Koalify app: duplicate detection flags |
| `multiaccountmanagement` | Cross-sell and multi-account fields |
| `event_information` | Event attribution fields |
| `services_qualification_matrix` | Qualification matrix output fields |
| `todo_-_archive` | Deprecated fields — do not use |

---

## Core deal fields (`dealinformation`)

| Field name | Label | Type | Notes |
|---|---|---|---|
| `hs_object_id` | Record ID | number | HubSpot's unique ID — read-only |
| `dealname` | Deal Name | string | Convention: "Company - Type - Month Year" e.g. "Arkose Labs - New Biz - July 2025" |
| `dealtype` | Deal Type | enum | New Business or Existing Business |
| `pipeline` | Pipeline | enum | See pipelines section below |
| `dealstage` | Deal Stage | enum | Stage within the pipeline — use stage IDs |
| `description` | Deal Description | string | Free-text |
| `hubspot_owner_id` | Deal Owner | enum | Assigned sales rep |
| `hubspot_team_id` | HubSpot Team | enum | Owner's primary team — auto-set |
| `createdate` | Create Date | datetime | Auto-set by HubSpot |
| `closedate` | Close Date | datetime | Expected or actual close date |
| `days_to_close` | Days to close | number | Auto-calculated |
| `contract_active` | Contract Active? | bool | True if today is between start and end date — computed |
| `engagement_manager` | Engagement Manager | string | EM assigned to delivery |
| `kickoff_date` | Kickoff Date | date | When client work started |
| `slack_channel` | Slack Channel - Internal | string | Internal Slack channel for this client |
| `sow` | SoW | enum | Statement of Work flag |
| `source_channel` | Source Channel | enum | How the deal originated |
| `inbound_lead_details` | Initial Inbound Lead Details | string | Notes on inbound lead |
| `icp_matrix_score` | ICP Matrix Score | number | Zapier-calculated score from ICP Matrix dimensions |
| `renewal_confidence` | Renewal Confidence | number | EM's % confidence in renewal (0-100) |
| `renewal_risk` | Renewal Risk | enum | Risk level flag |
| `renewal_risk_reason` | Renewal Risk Reason | string | If <100% confidence, EM explains why |
| `renewal_type` | Renewal Type | enum | Flat / Upsell / Down-sell |
| `line_item_s__set` | Deal has Line Item(s)? | enum | Must = true before closing a deal |
| `associated_sprint_deal_id` | Associated Sprint Deal ID | string | Links to Sprint deal record |
| `associated_growth_execution_deal_id` | Associated Growth Execution Deal ID | string | Links to Growth Execution deal |
| `associated_sprint_growth_record_id` | Associated Sprint/Growth Record ID | string | Required before closing new biz |
| `associated_with_prior_deal` | Associated with Prior Deal | number | Count > 0 means this is a renewal |
| `associated_with_renewal_deal` | Associated with Renewal Deal | number | Count > 0 means this deal has been renewed |
| `associated_with_expansion_deal` | Associated with Growth Execution Deal | number | Has expansion deal attached |
| `num_associated_contacts` | Number of Associated Contacts | number | Auto-set |
| `hs_next_step` | Next step | string | Short description of next action |
| `hs_deal_score` | Deal Score | number | HubSpot AI deal health score |
| `hs_likelihood_to_close` | Likelihood to close by close date | number | AI-predicted close probability (0-1) |
| `hs_forecast_probability` | Forecast probability | number | Custom forecast % |
| `hs_forecast_amount` | Forecast amount | number | Forecast probability × amount |
| `hs_is_closed` | Is Deal Closed? | bool | True if won or lost |
| `hs_closed_won_count` | Closed won count | number | 1 if closed won, else 0 |
| `hs_manual_forecast_category` | Forecast category | enum | Manual forecast classification |

---

## Revenue & financial fields (`deal_revenue`)

| Field name | Label | Type | Notes |
|---|---|---|---|
| `amount` | Amount | number | Total deal value |
| `hs_mrr` | Monthly recurring revenue | number | MRR |
| `hs_arr` | Annual recurring revenue | number | ARR |
| `hs_acv` | Annual contract value | number | ACV |
| `hs_tcv` | Total contract value | number | TCV |
| `annualized_mrr` | Annualized MRR | number | Custom field |
| `workstream_type` | Contract Type | enum | Contract type classification |
| `deal_currency_code` | Currency | enum | Defaults to USD |
| `amount_in_home_currency` | Amount in company currency | number | Exchange-rate converted |
| `hs_exchange_rate` | Exchange rate | number | Rate used for conversion |

---

## Contract fields (`contract_information`)

| Field name | Label | Type | Notes |
|---|---|---|---|
| `contract_start_date` | Contract Start Date | date | When engagement begins |
| `end_date` | Contract End Date | date | Manually set end date |
| `contract_end_date__calculated_` | Contract End Date (Calculated) | date | Computed from start + term |
| `renewal_date` | Renewal Date | date | End date + 1 day |
| `term____months_` | Term (# months) | number | Contract duration in months |
| `term__weeks` | Term (# weeks) | number | Contract duration in weeks |
| `billing_frequency` | Billing Frequency | enum | Monthly / Quarterly / Semi-Annually / Annually |
| `billing_timing` | Billing Timing | enum | Upfront vs. arrears |
| `billing_details` | Billing Details | string | Free-text billing notes |
| `payment_terms__net_days_` | Payment Terms (Net Days) | number | Net-30, Net-45, etc. |
| `auto_renewal` | Auto Renewal | enum | Does contract auto-renew? |
| `cancellation_details` | Renewal/Cancellation Details | string | Notes on terms |

---

## Pipelines and stages

GrowthX has four active pipelines. Stage names below; the IDs are numeric and used in `dealstage`.

### New Business (`pipeline` = `default`)
1. 👋 Intro (`1610642385`)
2. ✅ Engaged (`1610642387`)
3. 📝 Proposal (`1610642388`)
4. ✍️ Contract (`1610642389`)
5. 🎉 Won (`1610642390`)
6. ❌ Lost (`1610642391`)
7. ❌ Debook (`1610642392`)

### Renewal
1. ⏳ Not Started (`1842240492`)
2. 💻 Renewal Prep (`1842240493`)
3. 🔎 Scope & Options (`1842240494`)
4. 📑 Proposal (`1842240495`)
5. 🎉 Closed Won (`1842240497`)
6. ❌ Closed Lost (`1842240498`)

### Expansion (Existing Business)
Standard stages: Appointment Scheduled → Qualified To Buy → Presentation Scheduled → Decision Maker Bought-In → Contract Sent → Closed Won → Closed Lost → Debook

### Renewal (Existing Business) — older pipeline, same stages as Expansion

---

## Sales activity fields (`deal_activity`)

| Field name | Label | Notes |
|---|---|---|
| `budget` | Budget | BANT — free-text |
| `authority` | Authority | BANT — free-text |
| `need` | Need | BANT — free-text |
| `timing` | Timing | BANT — free-text |
| `closed_lost_reason` | Closed Lost Reason | Free-text |
| `closed_won_reason` | Closed Won Reason | Free-text |
| `primary_closed_lost_theme` | Primary Closed Lost Theme | Enum — categorized reason (added July 2025) |
| `notes_last_contacted` | Last Contacted | Auto: last call/email/meeting |
| `notes_last_updated` | Last Activity Date | Auto: any activity |
| `notes_next_activity_date` | Next Activity Date | Next scheduled activity |
| `num_contacted_notes` | Number of times contacted | Auto-count |
| `num_notes` | Number of Sales Activities | Auto-count, all activity types |
| `hs_is_stalled` | Is Stalled | True if 20%+ over owner's avg time in this stage |

---

## Renewal management fields

### Prior deal info (`prior_deal_information`)
Used on renewal deals to carry forward context from the deal being renewed:

| Field name | Label | Notes |
|---|---|---|
| `prior_amount` | Prior Amount | Previous deal total value |
| `prior_mrr` | Prior MRR | Previous MRR |
| `prior_arr` | Prior ARR | Previous ARR |
| `prior_contract_end_date` | Prior Contract End Date | When prior deal ends |
| `prior_renewal_date` | Prior Renewal Date | Renewal date from prior deal |
| `days_to_renewal` | Renewal Due In | Days until renewal must close — computed |

### Next renewal automation (`next_renewal_deal_information`)
Controls HubSpot workflows that auto-create the next renewal deal:

| Field name | Label | Notes |
|---|---|---|
| `renewal_cycle` | Renewal Cycle | Which iteration: 1 = first renewal, 2 = second, etc. |
| `next_renewal_cycle` | Next Renewal Cycle | Auto-calculated: current cycle + 1 |
| `renewal_cycle_type` | Renewal Cycle Type | Even/Odd — alternates to prevent workflow infinite loops |
| `renewal_due_in__for_zapier_` | Renewal Due In (for Zapier) | Numeric copy of the calculated field — HubSpot formula fields don't emit API events |

---

## Custom qualification scoring

All four scoring systems are custom-built. Scores are computed via Zapier and written back to HubSpot.

### ICP Matrix Score (`icp_matrix` group)
Trigger recalculation: update `date_of_last_icp_matrix_calculation` or set `recalculate_icp_matrix_score`.

| Field name | What it scores | Scale |
|---|---|---|
| `budget_alignment` | Is $10-15k/mo reasonable for their situation? | 1/3/5 |
| `revenue_funding_stage` | Financially stable enough for long-term? | 1/3/5 |
| `decision_authority` | How quickly can decisions get made? | 1/3/5 |
| `content_complexity` | Can pods handle their subject matter? | 1/3/5 |
| `content_production_history` | Do they already value content? | 1/3/5 |
| `content_strategy_buy_in` | Does leadership champion content? | 1/3/5 |
| `domain_strength` | How easy is it to rank their content? | 1/3/5 |
| `market_difficulty` | How hard to show content ROI in their space? | 1/3/5 |
| `approval_layers` | How many rounds before publishing? | 1/3/5 |
| `impact_timeline_expectations` | Do they understand SEO timelines? | 1/3/5 |
| `volume_sweet_spot_for_net_new` | Does their need match pod capacity? | 1/3/5 |
| `volume_content_gtm_fit` | Does their GTM benefit from high-volume? | 1/3/5 |
| `competitive_benchmark` | Are their expectations aligned with the service? | 1/3/5 |
| `content_team_capacity__theirs_` | Who will work with delivered content? | 1/2/3/5 |
| `publishing_control` | How much friction in getting content live? | 1/3/5 |

### Engagement Score (`engagement_score` group)
| Field name | What it scores | Scale |
|---|---|---|
| `budget_authority` | Controls budget, can decide | 1/3/5 |
| `enthusiasm_level` | How excited/proactive on calls | 1/3/5 |
| `internal_alignment` | Whole team onboard vs. conflict | 1/3/5 |
| `trust_in_expertise` | Partner mindset vs. control freak | 1/3/5 |
| `urgency_timeline` | Clear timeline vs. just exploring | 1/3/5 |
| `engagement_score` | Calculated total | number |
| `engagement_score_decision` | Recommended action | string |

### Partnership Fit Score (`partnership_fit` group)
| Field name | What it scores | Scale |
|---|---|---|
| `approval_process` | Fast vs. slow/complex approvals | 2/6/10 |
| `champion_dri_quality` | Quality of the internal champion | 2/6/10 |
| `content_philosophy` | Values content as growth channel | 2/6/10 |
| `execution_complexity` | How complex is their content to produce? | 2/6/10 |
| `internal_maturity` | Clear messaging/positioning defined? | 2/6/10 |
| `partnership_fit_score` | Calculated total | number |

### Account Potential Score (`account_potential` group)
| Field name | What it scores | Scale |
|---|---|---|
| `content_track_record` | Publishing cadence/volume | 1/3/5 |
| `domain_authority` | DA score (Ahrefs/Moz) | 1/3/5 |
| `funding_establishment` | Funding raised / headcount | 1/3/5 |
| `growth_trajectory` | Headcount/revenue growth trend | 1/3/5 |
| `logo_values` | Brand recognition/prestige | 1/3/5 |
| `account_potential_score` | Calculated total | number |
| `account_potential_decision` | Recommended action | string |

---

## Stage timing fields (`dealstages`)

For every pipeline stage, HubSpot auto-tracks three sets of fields:

- `hs_v2_date_entered_[stageId]` — datetime when the deal entered this stage
- `hs_v2_date_exited_[stageId]` — datetime when the deal exited this stage
- `hs_v2_cumulative_time_in_[stageId]` — total seconds spent in this stage across all visits
- `hs_v2_latest_time_in_[stageId]` — seconds in this stage since it last entered
- `hs_v2_date_entered_current_stage` — when deal entered its current stage
- `hs_v2_time_in_current_stage` — time in current stage so far

---

## Integrations

### SEMrush data (`semrush_data` group)
Pulled automatically from SEMrush for the associated company domain:

| Field name | Label |
|---|---|
| `organic_search_visits` | Organic Search Visits |
| `paid_search_visits` | Paid Search Visits |
| `organic_social_visits` | Organic Social Visits |
| `paid_social_visits` | Paid Social Visits |
| `search_visits` | Search Visits |
| `referral_visits` | Referral Visits |
| `total_users__semrush_` | Total Users |
| `average_pages_per_visit` | Average Pages Per Visit |
| `average_time_on_site` | Average Time on Site |

### Outbound tools
| Field name | What it tracks |
|---|---|
| `first_heyreach_touch_date` | First LinkedIn outreach touch via HeyReach |
| `first_instantly_touch_date` | First email outreach touch via Instantly |

### Attio legacy (`attio_deal_info` group)
Migration data from the previous CRM (Attio). Fields include `attio_deal_record_id`, `attio_deal_stage`, `attio_deal_value`, `attio_deal_close_date`, `attio_deal_closed_lost_detail`, etc. These are historical reference only — do not write to them.

### Koalify (`koalify_duplicates` group)
Third-party duplicate detection app:
| Field name | What it is |
|---|---|
| `koalify_duplicate_properties` | Properties flagging this as duplicate |
| `koalify_duplicate_rules` | Rules that triggered the flag |
| `koalify_is_primary_duplicate` | Is this the primary record? |
| `koalify_main_duplicate` | ID of the primary duplicate |
| `koalify_number_of_duplicates` | Count of duplicates found |

---

## Key business logic to know

**Closing a new business deal requires:**
1. `line_item_s__set` = true (line items attached)
2. `associated_sprint_growth_record_id` populated
3. Deal must be in Closed Won stage

**Renewal deals are auto-created by HubSpot workflows.** The `renewal_cycle_type` (Even/Odd) alternates with each cycle to prevent workflows from triggering themselves in a loop. Don't manually change this.

**The ICP Matrix Score triggers via Zapier.** Updating `date_of_last_icp_matrix_calculation` fires the Zapier workflow that recalculates all 15 dimensions and writes back `icp_matrix_score`.

**`renewal_due_in__for_zapier_`** exists because HubSpot formula fields don't fire API events. This numeric copy field enables Zapier to detect changes to the renewal timeline.

**Slack channel notifications** can be suppressed per deal using `don_t_include_in_slack_ping`.

**Deal name convention:** `[Company] - [Type] - [Month Year]` — e.g., "Arkose Labs - New Biz - July 2025". Closed won deals get a ✅ appended.

---

## Most commonly queried fields

When pulling deal data via MCP, these are the fields to request:

```
dealname, dealtype, pipeline, dealstage, amount, hs_mrr, hs_arr,
contract_start_date, end_date, renewal_date, term____months_,
billing_frequency, hubspot_owner_id, engagement_manager,
renewal_confidence, renewal_risk, renewal_type, renewal_cycle,
prior_amount, prior_mrr, prior_contract_end_date,
icp_matrix_score, partnership_fit_score, engagement_score,
closed_lost_reason, closed_won_reason, primary_closed_lost_theme,
source_channel, closedate, createdate, hs_is_closed_won, hs_is_closed_lost,
notes_last_contacted, notes_next_activity_date, hs_next_step,
contract_active, kickoff_date, slack_channel
```
