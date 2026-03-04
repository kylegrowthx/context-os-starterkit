# Alex <> Growth X - Weekly Sync

<metadata>
date: 2026-01-20
time: 18:29 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants:
  - name: Carrie Chowske
    affiliation: GrowthX
  - name: Donald Donckers
    affiliation: Alex
  - name: Aaron Wang
    affiliation: Alex
  - name: Max
    affiliation: Alex
  - name: Carly Piekos
    affiliation: GrowthX
fathom_recording_id: 115691309
fathom_url: https://fathom.video/calls/536817540
share_url: https://fathom.video/share/45Bikv7QpixA5whgKz8FxRshjhoszvz7
source: fathom
enriched_on: 2026-02-28 12:00 UTC
</metadata>

---

## Summary

Weekly sync between GrowthX and Alex to resolve SEO and branding issues blocking the site from proper search visibility. Key focus: fixing favicon/company name confusion in Google search results, addressing a ranking drop for "AI recruiter," and validating schema markup and indexing status.

---

## Context

Alex is working with GrowthX's SEO specialist Carly Piekos to optimize their site for search visibility. Following recent optimization work (favicon update, schema implementation, and noindex removal), the team discovered that Google is still displaying the old "Apriora" company name and favicon in search results, likely due to conflicting branding signals in Webflow. Additionally, the homepage's ranking for the target keyword "AI recruiter" dropped from page 5 to 7 after optimization, requiring a strategic internal linking fix to rebuild page authority.

---

## Relevance

**SEO & Technical**
- Favicon/branding confusion affecting search appearance
- Search ranking decline for target keyword "AI recruiter"
- Google indexing delays post-optimization
- JSON-LD schema implementation validation

**Product & Messaging**
- Site rebranding from "Apriora" to "Alex" in search signals
- Product messaging alignment ("AI recruiter" vs "AI interviewer" keywords)

**Content & Link Strategy**
- Internal linking strategy for keyword authority building
- Blog content updates reflecting new product messaging

---

## Overview

- **Favicon/Branding Issue:** The site shows the old "Apriora" favicon and company name in search results. The root cause is likely conflicting branding signals in Webflow settings and footer text.
- **Ranking Drop:** The homepage's rank for "AI recruiter" dropped from page 5 to 7 after optimization. The fix is a new internal linking strategy to build authority for the page.
- **Indexing Status:** Pages are no longer `noindex`, but Google has not yet indexed them. Carly will investigate in Google Search Console (GSC).
- **Schema Validation:** Carly will validate the JSON-LD schema Donald added to ensure it's correct and doesn't conflict with her own recommendations.

---

## Key Topics

### Favicon & Branding Confusion

  - **Problem:** Google displays the old "Apriora" favicon and company name, not "Alex," in search results.
  - **Investigation:**
      - The correct favicon is uploaded in Webflow settings, but the old one is hardcoded in the site's header.
      - The footer text "Apriora doing business as Alex" creates conflicting branding signals.
  - **Hypothesis:** Google's bots are confused by the conflicting branding signals.
  - **Proposed Solutions:**
      - **Test 1 (Donald):** Change footer text to "Alex" and set the Open Graph site name to "Alex."
      - **Test 2 (Carly):** Investigate hidden Webflow settings for a company name field.
      - **Escalate (Donald):** Use a scheduled Google Ads call to report the search issue, leveraging potential ad spend as a motivator for support.

### Ranking Drop for "AI Recruiter"

  - **Observation:** The homepage's rank for "AI recruiter" dropped from page 5 to 7 after optimization last Friday.
  - **Diagnosis:** The drop is a normal, temporary fluctuation as Google re-evaluates the page's relevance against new competitors.
  - **Solution:** Implement a new internal linking strategy.
      - **Action:** Link all mentions of "AI recruiter" on other site pages (e.g., blog posts) back to the homepage.
      - **Rationale:** This builds authority for the homepage, signaling its importance for the target keyword to Google.

### Indexing & Schema Status

  - **Indexing:**
      - **Status:** `noindex` tags are removed, but pages (e.g., interviews) are not yet indexed in GSC.
      - **Action (Carly):** Investigate the indexing status in GSC.
  - **Schema:**
      - **Status:** Donald added JSON-LD schema via Webflow last Friday.
      - **Action (Carly):** Validate the existing schema to ensure it's correct and doesn't conflict with her recommendations.

---

## Action Items

**Carly Piekos (GrowthX)**
- Check Alex JSON-LD schema in Rich Results; advise Donald on replacement if needed
- Monitor Alex indexing in GSC; follow up w/ Donald
- Investigate Webflow company-name settings; advise Donald
- Confirm w/ Carrie (GrowthX) inclusion of "AI recruiter" in internal-linking; update Donald; implement if missing
- Send meeting summary to Donald w/ action items

**Donald Donckers (Alex)**
- Convert Alex favicon/web clip to ICO; upload in Webflow; publish; clear cache; verify incognito
- Change Webflow site name to Alex; publish; clear cache; verify incognito
- Set OG site name to Alex in Webflow; publish; clear cache; verify incognito
- Raise favicon/indexing issues w/ Google Ads rep; request Search team support
- Review Carrie's (GrowthX) updated articles; approve or request revisions

---

## Transcript

**Carly Piekos:** So let's get to it.

**Carly Piekos:** So I completed your schema recommendations and basic templates to put into Webflow. Who is going to be implementing that, and do I need more explanation?

**Donald Donckers:** Can you show me what it is?

**Carly Piekos:** I added JSON-LD schema, and I'll check yours to see what it looks like. Did you do it in GTM or Webflow?

**Donald Donckers:** I did it in Webflow on Friday. I can update it with yours if needed.

**Carly Piekos:** It's going to take a couple weeks to show up in rich snippets. I'll validate yours and do a spot check.

---

**Carly Piekos:** Index update—did you resolve those noindex tags?

**Donald Donckers:** I updated the pages to be indexable and checked in Google Search Console, then submitted an index request. But when I check GSC, it says the pages are not available on Google.

**Carly Piekos:** It's not showing noindex anymore—that's good news. Let me check search console and see if there's anything else I can do on my end.

---

**Donald Donckers:** I'm trying to rank for "AI interviewer" and "AI recruiter." I optimized the homepage and it's in the H1 and title tag, but I'm waiting for Google to index it.

**Carly Piekos:** I'll monitor indexing in GSC. The main issue is the Favicon/branding problem—Google is still showing "Apriora" instead of "Alex."

---

**Donald Donckers:** Why does it keep showing the old icon and why is it saying Apriora?

**Carly Piekos:** The correct favicon is uploaded in Webflow settings, but the old one is hardcoded in the header. The footer says "Apriora doing business as Alex," which creates conflicting signals.

**Donald Donckers:** Should we change the footer to just say "Alex"?

**Carly Piekos:** I'd test it. I also suspect there's a company name field in Webflow we might be missing. Let's look at the site settings.

**Donald Donckers:** The favicon is a PNG. Maybe I need to convert it to ICO. And we should set the OG site name to "Alex" too.

**Carly Piekos:** Yes. As far as the image showing with the company name, it must be somewhere in Webflow settings. We might have to actually escalate this to Google—use your Google Ads meeting tomorrow as leverage.

**Donald Donckers:** I have a meeting with Google Ads tomorrow, but they'll say Google Search is a different division.

**Carly Piekos:** Tell them: "If I was showing up properly in Google, maybe I'd spend more money." I had a customer who got their Google Business Profile fixed quickly once they mentioned spending on ads.

**Donald Donckers:** That's a good angle. I'll do that tomorrow. But we've only got four minutes left. One more thing—I optimized the homepage for "AI recruiter" and noticed we dropped from page 5 to page 7 in rankings. Is that normal?

**Carly Piekos:** That's a temporary fluctuation. You're competing with many AI recruiting platforms now. The fix is internal linking—link every mention of "AI recruiter" on your blog back to the homepage.

**Donald Donckers:** Is that something you guys can automate, or do I need to go through the blog manually?

**Carly Piekos:** I'll talk to Carrie and confirm if "AI recruiter" is in the automated internal linking strategy. I'll let you know today.

**Donald Donckers:** I'll review the content pieces. You said one was ready and you're updating the others for new product messaging?

**Carly Piekos:** Carrie updated the artifacts in Notion and Atlas and will deliver the other articles today for approval.

**Donald Donckers:** Beautiful. Any other issues?

**Carly Piekos:** I'll keep looking into the favicon issue and send you a summary with both our action items.

**Donald Donckers:** Sounds good.
