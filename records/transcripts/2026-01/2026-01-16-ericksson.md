# Ericksson / Leonardo — Cost Reconciliation & Year-End Financials

<metadata>
date: 2026-01-16
time: 18:29 UTC
duration: 24 minutes
organizer: leonardo@growthx.ai
participants:
  - name: Ericksson Abad
    email: ericksson@growthx.ai
    affiliation: GrowthX
    role: Finance/Operations
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: GrowthX
    role: CTO
fathom_recording_id: 114981773
fathom_url: https://fathom.video/calls/535950927
share_url: https://fathom.video/share/Vit8rWamiMg5P3g_QzUUHVCvJ-Es1kks
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

Ericksson and Leonardo worked through a $4.5k discrepancy in December Anthropic costs between the Ramp charge ($64.5k) and the cost tracker report (~$60k). Leonardo granted Ericksson direct billing access to Anthropic, OpenAI, and Gina AI to pull invoices and resolve the gap. They also discussed cost allocation strategy, deciding that all CheckDat-related spend will be booked as R&D, pending Leo's identification of the specific tools used.

---

## Context

GrowthX is finalizing year-end financials for December 2025, and accurate cloud cost tracking is critical for calculating gross margin. Ericksson discovered a significant gap between what Ramp shows ($64.5k for Anthropic) and what the internal cost tracker reports (~$60k). The root cause is unclear—it could stem from multiple team members (Yusuf, Daniel, Jason, Marcel) using separate payment cards for Anthropic accounts, making it impossible to reconcile a single Ramp charge to a single usage report. To solve this, Leonardo provided direct billing access to the top vendors, allowing Ericksson to pull invoices directly. They also began establishing a cost allocation framework to properly categorize development versus production spend.

---

## Relevance

- **Finance & Accounting:** Year-end closure, gross margin calculations, audit trail reconciliation
- **Finance & Accounting:** Ramp-to-vendor invoice matching, billing access permissions and best practices
- **Product & Engineering:** CheckDat cost allocation, distinguishing R&D from production spend
- **Operations:** Multiple cardholder management, account consolidation strategy

---

## Overview

- **December Anthropic cost discrepancy:** ~$4.5k gap between the $64.5k Ramp charge and ~$60k reported by the cost tracker.
- **Root cause:** Multiple cardholders (Yusuf, Daniel, Jason, Marcel) using separate accounts, obscuring total usage across a single vendor.
- **Resolution:** Ericksson received direct billing access to Anthropic (Owner), OpenAI (Standard API), and Gina AI (shared tools credential) to pull invoices and reconcile.
- **Cost allocation strategy:** All CheckDat-related spend will be categorized as R&D; Leonardo will map specific tools to this project for proper allocation.

---

## Key Topics

### Problem: December Cost Discrepancy

Ericksson discovered a ~$4.5k gap for Anthropic: Ramp charged $64.5k while the internal cost tracker showed ~$60k. The discrepancy stems from multiple cardholders (Yusuf, Daniel, Jason, Marcel) having separate Anthropic accounts on different payment cards. This makes it impossible to reconcile a single Ramp charge to a single vendor usage report, and it directly impacts gross margin calculations needed to close year-end financials.

### Solution: Direct Billing Access

Leonardo granted Ericksson direct access to vendor platforms to pull invoices directly:

- **Anthropic:** Owner access (full visibility to invoices and usage history)
- **OpenAI:** Standard API access (allows billing review without modifying API keys)
- **Gina AI:** Shared "tools" credential (low risk for account blocks)

This access enables Ericksson to reconcile each vendor's invoices against the corresponding Ramp charges.

### Cost Allocation Strategy

GrowthX needs to categorize cloud spend across production, development, and product lines (CheckDat vs. other work). Initial decision: all CheckDat-related spend will be booked as R&D. Leonardo will identify which tools from the vendor list are used for CheckDat to enable this allocation. Full vendor list requiring allocation: Anthropic, OpenAI, Gina AI, SEMrush, Exa, Render, Perplexity, Temporal, World Technologies, AWS, Datadog, Snowflake, Google Cloud, Cursor, Clerc.dev.

---

## Action Items

**Ericksson Abad (GrowthX)**
- Accept Anthropic billing invite; pull December invoices and usage data; reconcile against Ramp charge; share findings with Leonardo
- Analyze Yusuf and Daniel's Anthropic charges; compare against dashboard usage; determine if related to project work or separate accounts; share findings with Leonardo

**Leonardo Carpenedo Steffen (GrowthX)**
- Request Gina AI billing access; pull December invoices and usage; reconcile against Ramp; share findings with Ericksson
- Complete cost analysis on top-3 vendors (Anthropic, OpenAI, Gina AI); identify which tools are used for CheckDat; share allocation framework with Ericksson

---

## Transcript

**Leonardo:** Hey, how's it going?

**Ericksson:** Pretty good. How are you, Leo?

**Leonardo:** Doing great. I'm trying to get all of the meetings that I have scheduled. I'm focused on one-on-ones right now, but the cost tracker is a priority too.

**Ericksson:** This is hitting me on the accounting side with Bridget. We're trying to wrap up year-end December financials, and this is impacting our gross margin numbers. So I can't fully produce the financials without getting the right numbers.

**Leonardo:** This is critical. Let me prioritize it.

**Ericksson:** I have all the transactions posted from credit cards into our accounting center. Ramp shows a total of $64.5k, but when I try to match that to actual usage, I'm coming up about $4.5k short. The cost tracker is only showing around $60k.

**Leonardo:** Let me show you what I have. December 1st through 31st. [Looks at data] So we're short about four grand?

**Ericksson:** Yeah, about $4.5k. I think the issue is we might have multiple Claude accounts hitting different credit cards. Yusuf has charges on his card, Daniel has charges on his card, Jason has some, Marcel has some. So there's confusion about which card is associated with which account we're tracking.

**Leonardo:** That's a good call. I didn't know that.

**Ericksson:** If we look at just Yusuf and Daniel's spend, we might get closer to the number.

**Leonardo:** I can look into the dashboard and see what's going on. But to solve this, let me give you billing access directly to Anthropic. You can pull invoices yourself.

**Ericksson:** Yes, that would be helpful.

**Leonardo:** I'm giving you Owner access to Anthropic and Standard API access to OpenAI. That way you can view billing history and payments without modifying API keys. For Gina AI, you can use the shared tools credential.

**Ericksson:** OK, this will help me weed out true API usage versus people using the card for micro subscriptions or little team plans.

**Leonardo:** Right. And we need to sort out the cost allocation. Everything that's associated with CheckDat is going to be R&D.

**Ericksson:** But which tools are those? That's what I'm trying to figure out.

**Leonardo:** I don't have that answer right now. Things aren't clear yet. But I have an idea for Anthropic and Gina. Daniel started the CheckDat keys and he's managed them from the beginning. Gina is mostly for CheckDat and it's well organized.

**Ericksson:** So is there any vendor where we can confidently say 90% of it is all R&D?

**Leonardo:** I don't have that answer for you. If I tell you anything, it would be a lie. But let me identify the specific tools used for CheckDat and communicate that to you.

**Ericksson:** OK. Here's the list of vendors we need to allocate: Anthropic, OpenAI, Gina AI, SEMrush, Exa, Render, Perplexity, Temporal, World Technologies, AWS, Datadog, Snowflake, Google Cloud, Cursor, and Clerc.dev.

**Leonardo:** That's the same list Daniel gave you?

**Ericksson:** Yes. I think the top three is a good start for us.

**Leonardo:** Yeah. I'll let you know what I come up with.

**Ericksson:** Thank you so much for your time.
