<metadata>
purpose: Every HubSpot object type at GrowthX — contacts, companies, deals, and custom objects — with their key property groups.
source: https://handbook.growthx.ai/systems/hubspot/objects-and-properties
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Objects and properties

## Contacts

~700+ properties across 23 groups. Every person GrowthX interacts with lives here — prospects, clients, partners, event attendees.

### Key custom property groups

<Tabs>
  <Tab title="Default Enrichment">
    **31 properties** — Enriched via Default.com's inbound workflow and Clay tables.

    When a prospect fills out a form, Default routes them and Clay enriches the record:

    | Property | Type | What it captures |
    |----------|------|-----------------|
    | Annual Revenue (via Default) | string | Company revenue from enrichment |
    | Company Domain (via Default/Clay) | string | Company website domain |
    | Company Name (via Default) | string | Company name from form |
    | Organic Search Visits (via Clay) | number | Monthly organic search traffic |
    | Organic Social Visits (via Clay) | number | Monthly organic social traffic |
    | Total Users (via Clay) | number | Monthly website visitors |
    | Average Pages Per Visit (via Clay) | number | Engagement depth |
    | Traffic Rank (via Default) | string | Website traffic ranking |
    | Meeting Booked via Inbound Flow | enum | Whether a meeting was booked |
    | Date of Initial Sales Form Submission | date | First form fill timestamp |
    | Context for Discussion (via Default) | string | What the prospect wants to discuss |
  </Tab>
  <Tab title="Luma Events">
    **9 properties** — Event attendance tracking from Luma via Hapily.

    | Property | Type | What it captures |
    |----------|------|-----------------|
    | Attended - AI GTM Exec Dinner | enum | Specific event attendance |
    | Attended - GrowthX & Understory Breakfast | enum | Specific event attendance |
    | Attended - Inbound HH | enum | Specific event attendance |
    | Attended - Own the AI Front Pg Webinar | enum | Specific event attendance |
    | Attended Physical Event | enum | Any in-person event |
    | Attended Virtual Event | enum | Any virtual event |
    | Date of Most Recent Luma Activity | date | Last event interaction |
  </Tab>
  <Tab title="OutboundSync">
    **52 properties** — Outbound campaign tracking from Instantly and HeyReach.

    Tracks every touchpoint across email and LinkedIn outbound:

    | Category | Properties tracked |
    |----------|-------------------|
    | Email campaigns | Campaign name, send time, subject, message body |
    | Opens | Open time, opened message, opened subject |
    | Clicks | Click time, clicked URL |
    | Replies | Reply time, reply message, reply subject, reply sender |
    | LinkedIn | Like time/post, follow time/sender, connection status |
    | Bounces | Bounce time, bounced message |
    | Unsubscribes | Unsubscribe time |
  </Tab>
  <Tab title="AI-Led Growth">
    **3 properties** — Lead magnet and content delivery.

    | Property | Type | What it captures |
    |----------|------|-----------------|
    | Content Name | string | Name of requested content |
    | Content URL | string | URL to the content (hidden form field) |
    | Marketing Consent | enum | Consent status |
  </Tab>
  <Tab title="Calendly">
    **20 properties** — Meeting booking form data.

    10 question/answer pairs from Calendly booking forms.
  </Tab>
</Tabs>

### Key custom fields

| Field | Type | Description |
|-------|------|-------------|
| Company Fit Score | enum | ICP alignment (Good / Medium / Low) — synced from company |
| Company # of Employees | number | Employee count — synced from company |
| Company Funding | number | Funding amount — synced from company |
| Contact Tags | enum | GTM filtering tags |
| beehiiv Subscriber | bool | Newsletter subscriber flag |
| Competitor | enum | Whether the contact is a competitor |
| Best Performing Channel | enum | Best attribution channel |
| First Touch Channel | enum | First-touch attribution |
| Clay Enrichment Date | date | Last Clay enrichment timestamp |
| Employment Seniority Tier | enum | Seniority level |

<Note>
Several contact fields are synced from the associated Company record via workflows: Fit Score, Employee Count, Managing Director, Deal Count, and Company Name.
</Note>

---

## Companies

~234 properties across 20 groups. Every client and prospect organization.

### Key custom property groups

<Tabs>
  <Tab title="Health Score">
    **7 properties** — A 5-dimension client health scoring system.

    Each dimension is scored 0.5 to 5:

    ```mermaid
    mindmap
      root((Health Score))
        Relationship
          Trust level
          Partnership vs vendor
        StrategyConfidence["Strategy/Confidence"]
          Plan clarity
          Actions to outcomes
        Fulfillment["Quantity/Fulfillment"]
          Contractual delivery
          Proactive ideas
        PerformanceROI["Performance/ROI"]
          Results vs goals
          ROI tracking
        ContentQuality["Content Quality"]
          Feedback volume
          Review efficiency
    ```

    | Dimension | 1 | 5 |
    |-----------|---|---|
    | Relationship | No trust, churn risk | Full trust, partners not vendors |
    | Strategy/Confidence | Directionless | Everyone aligned, data supports plan |
    | Quantity/Fulfillment | Significantly under-delivering | Meeting everything + proposing ideas |
    | Performance/ROI | Not hitting ROI goals | Exceeding ROI goals |
    | Content Quality | Excessive feedback needed | Full trust, minimal feedback |

    **Health Tier** is derived from the sum, weighted by dimension.
  </Tab>
  <Tab title="SEMRush Data">
    **12 properties** — Traffic analytics from SEMRush.

    | Property | Type | What it captures |
    |----------|------|-----------------|
    | Total Users | number | Monthly unique visitors |
    | Total Visits | number | Monthly total visits |
    | Traffic Rank | number | Global traffic ranking |
    | Organic Search Visits | number | Organic search traffic |
    | Organic Social Visits | number | Organic social traffic |
    | Paid Search Visits | number | Paid search traffic |
    | Paid Social Visits | number | Paid social traffic |
    | Referral Visits | number | Referral traffic |
    | Average Pages Per Visit | number | Engagement depth |
    | Average Time on Site | number | Session duration |
  </Tab>
  <Tab title="Event Information">
    **3 properties** — Event engagement at the company level.

    | Property | Type |
    |----------|------|
    | Event Attendance Trigger | string |
    | Latest Event Attended | string |
    | Latest Event Attended Date | date |
  </Tab>
</Tabs>

### Key custom fields

| Field | Type | Description |
|-------|------|-------------|
| Account Stage | enum | Prospect / Pipeline / Customer / Churned / Lost Deal / Competitor |
| Fit Score | enum | ICP alignment (Good / Medium / Low) |
| Engagement Manager | string | Assigned Engagement Manager name |
| Active Annualized MRR | number | Sum of active deal MRR (rollup) |
| Funding | number | Funding amount |
| Domain Authority | number | SEO domain authority score |
| Slack Channel - Internal | string | Internal Slack channel for the client |
| Sales Prospecting Tier | enum | Sales targeting priority |
| Billing Address / Email | string | Billing details |

---

## Deals

~444 properties across 23 groups. Every revenue opportunity, active contract, and renewal.

### Key custom property groups

<Tabs>
  <Tab title="Account Potential">
    **7 properties** — Scoring matrix for evaluating new business potential.

    | Dimension | 1 | 3 | 5 |
    |-----------|---|---|---|
    | Content Track Record | No content | Some content, sporadic | 2+/week or 500+ pages |
    | Domain Authority | DA less than 20 | DA 20-39 | DA 40+ |
    | Funding/Establishment | Less than $2M or 100 employees | $2-10M or 100-500 | $10M+ or 500+ |
    | Growth Trajectory | Flat/declining | Stable, modest | Recent raise or 20%+ growth |
    | Logo Value | Unknown | Niche but respectable | Well-known brand |
  </Tab>
  <Tab title="Contract Information">
    **13 properties** — Full contract lifecycle tracking.

    | Property | Type | Description |
    |----------|------|-------------|
    | Contract Start Date | date | When service begins |
    | Contract End Date | date | When service ends |
    | Contract End Date (Calculated) | date | Auto-calculated from start + term |
    | Renewal Date | date | Contract end + 1 day |
    | Term (months) | number | Contract duration in months |
    | Term (weeks) | number | Contract duration in weeks |
    | Billing Frequency | enum | Monthly / Quarterly / Semi-Annually / Annually |
    | Billing Timing | enum | When payment is due |
    | Payment Terms (Net Days) | number | Days to pay after invoice |
    | Auto Renewal | enum | Whether contract auto-renews |
    | Billing Details | string | Free text billing notes |
    | Renewal/Cancellation Details | string | Renewal or cancellation context |
  </Tab>
  <Tab title="Engagement Score">
    **5 properties** — BANT-style deal engagement scoring.

    Budget, Authority, Trust, Enthusiasm, Urgency — each scored to assess deal readiness.
  </Tab>
  <Tab title="Attio Migration">
    **9 properties** — Historical data from the Attio CRM migration (June 2025).

    Deal record IDs, names, stages, values, close dates, and days-to-close from the prior CRM.
  </Tab>
</Tabs>

### Deal types and contract types

| Deal Type | When used |
|-----------|----------|
| New Business | First engagement with a company |
| Expansion | Upsell on existing account |
| Renewal | Contract renewal |
| Renewal - Upsell | Renewal with increased scope |
| Renewal - Downsell | Renewal with reduced scope |

| Contract Type | Description |
|---------------|-------------|
| Sprint + Growth Execution | Strategy sprint followed by ongoing execution |
| Pilot + Workstream | Trial period then workstream |
| Standard Terms | Ongoing engagement without sprint |
| Other | Non-standard arrangement |

### Deal naming convention

Deals are auto-named by a workflow:

```
{Company} - {Type} - {Month Year}
```

Examples: `Tavus - Strategy Sprint - July 2025`, `Diligent - Growth Execution - Aug 2025`

---

## Custom objects (Hapily / Luma)

Three custom objects power the event integration:

| Object | What it is |
|--------|-----------|
| **hapily_event** | Events synced from Luma — name, date, status |
| **hapily_session** | Sessions within an event |
| **hapily_registrant** | Individual registrants — linked to HubSpot contacts |

Events flow from Luma through Hapily into HubSpot, where workflows handle:
- Registrant-to-contact linking
- Company association
- Attendance tracking
- Deal attribution (influenced creation and influenced close)
