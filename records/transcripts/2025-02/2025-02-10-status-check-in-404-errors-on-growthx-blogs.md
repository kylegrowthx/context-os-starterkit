# status check-in / 404 errors on GrowthX blogs

<metadata>
date: 2025-02-10
time: 20:31 UTC
duration: 8 minutes
organizer: Prateek Gupta
participants: Prateek Gupta, Curtis Cartier, Mark Heynen, Emily Winsauer, Allison Diroll
fathom_recording_id: 46498960
fathom_url: https://fathom.video/calls/230517282
share_url: https://fathom.video/share/p2TMF8tLLxCSSutczbRs82F-TWb9bsze
source: fathom
enriched_on: 2026-03-05 14:30 UTC
</metadata>

---

## Summary

During a Webflow-to-Sanity migration, approximately 250 GrowthX blog posts (70-80%) failed to migrate, resulting in 404 errors that significantly impacted organic search traffic and keyword rankings. Curtis Cartier (Webstacks) committed to uploading the remaining blogs via script within hours, while Emily Winsauer confirmed all URLs remain unchanged and outlined a post-launch monitoring plan including sitemap resubmission in Search Console after a 24-hour wait. The root cause: an internal communication gap over whether the migration would be handled by script or manual import.

---

## Context

GrowthX hired Webstacks (Curtis Cartier, Emily Winsauer, Allison Diroll) to migrate the blog platform from Webflow to Sanity CMS. This was a critical project for content consolidation and performance improvement. During implementation, a discrepancy emerged between initial site crawls (~300 blogs) and the content inventory sheet used for migration (~50 blogs), leaving 250 blogs unmigrated and returning 404 errors. Mark Heynen (Knap, external stakeholder/advisor) joined the call to understand the situation and ensure rapid resolution. The issue required immediate attention due to SEO impact — organic traffic had dropped significantly, and prolonged 404s risked permanent keyword ranking loss.

---

## Relevance

**To GrowthX Delivery:**
- Critical CMS migration caught mid-implementation with process gap between teams. Demonstrates need for clear handoff documentation and shared assumptions during vendor transitions.
- URL preservation strategy (all 250 unmigrated blogs maintain original slugs) preserved SEO value but required technical verification before bulk import.
- HTML-to-Portable Text format conversion complexity managed by Webstacks; similar migration patterns should be documented for future content platform transitions.

**To GrowthX Business Development:**
- Webstacks responded quickly with accurate root cause analysis and credible fix within hours — solid vendor partner signal.
- Internal communication gap (migration method assumption) highlights need for clearer project briefs and status check-ins with external partners on complex implementations.

**To CheckThat / AI Visibility:**
- 404 surge represents temporary content visibility loss across both Google and AI engines. Post-migration sitemap resubmission and crawl monitoring (Emily's 24-hour plan) should recover visibility within 1-2 weeks if URLs are unchanged.

---

## Overview

- \~70-80% of blogs (250) not migrated from Webflow to Sanity, causing 404s and SEO decline
- Curtis (Webstacks) expects to upload remaining blogs via script today, using provided CSV
- Emily (Webstacks) to monitor analytics, resubmit sitemap, and conduct post-launch checks
- Issue root cause: internal communication gap during migration process

---

## Key Topics

### Migration Issue and SEO Impact

  - 70-80% of blogs (\~250) not migrated from Webflow to Sanity
  - Resulting 404 pages significantly impacting SEO performance
  - Risk of losing keyword rankings if not addressed promptly
  - CSV file with T\&D article dump shared with Julie for resolution

### Current Status and Action Plan

  - Webstacks team identified exact cause and solution
  - Curtis converting CSV to JSON for Sanity import
  - Script being written to upload remaining blogs (ETA: couple of hours)
  - Precautions to avoid overwriting existing, updated blog content
  - HTML formatting to be converted to Sanity's Portable Text format

### SEO Considerations

  - URLs/slugs confirmed to remain unchanged (critical for SEO)
  - Emily compared CSV against recent live blog crawl to ensure URL consistency
  - Post-upload plan: 24-hour wait, then resubmit sitemap to Search Console
  - Ongoing monitoring of analytics (GA) and additional crawls planned

### Root Cause Analysis

  - Discrepancy between initial site crawl and content inventory sheet
  - Internal communication issue: assumption about migration method (script vs. manual)
  - Ongoing investigation for complete understanding

---

## Action Items

**Curtis Cartier**
- Upload remaining ~250 blogs to Sanity via script from provided sheet. Ensure existing blogs aren't overwritten. Convert HTML to Portable Text.

**Emily Winsauer**
- After blog upload (24h): Resubmit sitemap in Search Console. Check sitemap completeness. Monitor GA analytics. Perform post-launch crawls over next few days.

---

## Transcript

**Mark Heynen:** I'm making time on short notice. Let me just catch up on the latest status. Have we diagnosed the problem? Do we have any obstacles trying to solve it? So whoever feels they have the most information, go ahead and jump in.

**Prateek Gupta:** So basically what's happened is during a migration from Webflow to Sanity, most of the blogs — around 70-80% — did not get migrated, which is why we're seeing 404 pages. That's significantly impacted our SEO — we were seeing a great amount of clicks, and we've seen a major fall. The pages are still 404, and soon we might start losing rankings on keywords we've gained. I discussed this with Julie, and she wanted the T&D article dump. I've shared that CSV file with her.

**Mark Heynen:** I want to interrupt briefly — we need to be careful about terminology here. We're talking about Webstacks, not Webflow, right? Webflow is an agency we use.

**Prateek Gupta:** Right, exactly. I wanted to understand next steps, timelines, and any blockers we have to move forward with uploading the content.

**Emily Winsauer:** I'll set the high level and then hand it over to Curtis. We spent a lot of time this morning identifying exactly what happened and how to fix it. I think the path forward is importing directly from the CSV. I don't think we have any blockers currently to getting this resolved promptly. Mark, thank you for analytics access so I can monitor as this resolves. We also ran three or four crawls this morning to test various things. As for timing today, I'm writing a script to help with the upload.

**Curtis Cartier:** I've already converted the sheet you sent to a JSON file. I'm going to parse that and get it uploaded. I need to make sure everything is uploaded and readable to Sanity. I'm about halfway through right now. I'm expecting to run a test version in a couple of hours, and I'd be surprised if this takes me the rest of the day. My main priority is getting the remaining 250 blogs uploaded via script from that sheet.

**Prateek Gupta:** That would be good. Do you need any Sanity access or help with anything coming up?

**Curtis Cartier:** No, I think I have everything. Yeah, if everything in that sheet is accurate, I'll run with that.

**Curtis Cartier:** I'm not too worried about anything outside of that. The main thing I want to avoid is the current blogs you already have migrated — I'm writing logic to not update or change those, because we've made updates to different parts of them. So I don't want to touch those. We'll watch for the slugs and say don't upload if the slug already exists. Just basic stuff.

**Mark Heynen:** Are we sure the spreadsheet includes all the formatting when you do the update?

**Curtis Cartier:** I'm going to keep all the formatting. From what I see, it's HTML, so I have to convert it to Portable Text — that's what Sanity calls it. I'm not too worried. I'm looking at all this and you have semantic tagging in here. This should be all good.

**Mark Heynen:** What about the URLs and slugs? They'll be maintained, right? This is really important from an SEO point of view.

**Emily Winsauer:** When we got that CSV file, I compared it to our most recent crawl of the blogs currently live. None of the URLs have changed — they're exactly the same. There was one post published outside of the GrowthX site, and Curtis and I already discussed that. He's making sure that individual post isn't affected.

**Emily Winsauer:** Once Curtis finishes and everything is published and live with no 404s, I'll wait about 24 hours to make sure everything is populated, then go back into Search Console to resubmit the sitemap. I'll also do a quick check of the sitemap to make sure everything is there. I'll keep a close eye on the analytics in GA and do a couple of post-launch crawls over the next few days to make sure everything looks right.

**Mark Heynen:** Any blockers? Anything I can help with at this point?

**Curtis Cartier:** No blockers that I'm aware of. I'm just going to keep cruising, and if there are blockers, I'll find you on Slack.

**Mark Heynen:** Well, I think I should give everyone their time back and get out of the way. I do want to understand how this happened at some point — is there a one-line version I should know about?

**Curtis Cartier:** It's still being investigated on our end, but here's what we know: I went off the content inventory sheet when creating the site, and I only saw about 50 blogs in there. But it's somewhere between the initial crawl we did of your site and the content inventory sheet — something just didn't align.

**Emily Winsauer:** I'll add some context. We knew GrowthX was publishing new posts fast. Usually we migrate blogs by script. So the strategy team decided not to update the sheet with a bunch of new posts — we said we're migrating by script from the CMS, so we don't need to list them off manually. But then down the road, someone said "if there are only 50, maybe we handle it differently." Honestly, it was an internal communication issue.

**Mark Heynen:** Okay, I'm glad we're sorting this and it sounds like we'll get it done today. I appreciate you flagging the time sensitivity. Let's let you guys get back to work. Let us know if you hit any issues or obstacles.

**Prateek Gupta:** Thanks everyone.

**Allison Diroll:** Thank you.

**Mark Heynen:** Bye.
