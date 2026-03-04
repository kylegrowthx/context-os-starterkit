# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-04-11
time: 16:01 UTC
duration: 34 minutes
organizer: aida@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Aida Knežević (GrowthX), Aaron Williams (FOSSA), Andy Drukarev (FOSSA), Kevin Wang (FOSSA)
fathom_recording_id: 56878562
fathom_url: https://fathom.video/calls/273627377
share_url: https://fathom.video/share/LB8K9H2Cx-qWJpV-gGZs3JURXK9SoyeX
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

GrowthX and FOSSA synced on three core initiatives: the website migration is showing positive early signals with keywords picking up and strong Core Web Vitals on desktop, though mobile performance needs optimization and cleanup work remains (404 fixes, old blog subdomain, duplicate tags). The team decided to focus on a new content work stream around "Alternatives" pages (e.g., Snyk alternative, Black Duck alternative) rather than refining existing OWASP Top 10 content, with Jakub and Aida to propose 2 initial alternatives in Slack. For the registry launch, GrowthX recommended starting with a conservative batch of 500-1,000 pages themed if possible, using no-index tags initially to de-risk inaccurate content, then removing no-index once pages meet quality thresholds.

---

## Context

FOSSA is a B2B SaaS company in the open-source software management space. GrowthX is delivering content marketing and SEO services as part of an ongoing engagement. This weekly sync is part of GrowthX's regular cadence with FOSSA to align on content strategy, website performance, and go-to-market initiatives. FOSSA recently completed a major website migration and is planning to launch a registry product—both strategic initiatives that require close collaboration on SEO strategy and content production between the two teams. The meeting happened after Aaron Williams returned from attending an event in Raleigh, and the team was working through action items from previous calls with GrowthX stakeholders.

---

## Relevance

**To GrowthX Delivery:**
- New content work stream on "Alternatives" pages represents methodological pivot from refining existing OWASP Top 10 content to creating original comparison content, which may impact scope and timeline of future work streams.
- Registry launch strategy uses no-index approach to de-risk inaccurate content while getting site speed benefits and SEO infrastructure in place—a pragmatic methodology that balances speed with accuracy.
- Mobile Core Web Vitals need optimization on FOSSA site; desktop looks good, suggesting device-specific performance issues to investigate.

**To GrowthX Business Development:**
- FOSSA is actively deploying new content and registries, indicating strong engagement and appetite for additional work streams; Andy Drukarev signaled willingness to focus on new initiatives rather than refinement, suggesting confidence in GrowthX delivery.
- Website migration showing positive early signals (keyword pickup, desktop CWV improvements) without new content live yet—strong validation of GrowthX SEO work and potential proof point for similar migration clients.
- Registry is expected to drive significant organic traction once launched at scale (300,000+ pages planned); early results from 500-1,000 page batches will be important signal for account expansion.

---

## Overview

- New content work stream to focus on "Alternatives" pages (e.g., Snyk alternative, Black Duck alternative)
- Website migration showing positive early signals; some cleanup still needed (e.g., mobile performance, old blog subdomain)
- Registry page structure feedback provided; next steps include making tweaks and planning for batch releases

---

## Key Topics

### Content Work Streams

  - Decided to focus on a new work stream ("Alternatives") rather than refining existing OWASP Top 10 content
  - Will start with obvious comparisons and expand to adjacent tools
  - Team to propose 2 initial alternatives in Slack for review

### Website Migration Progress

  - Positive early signals: keywords picking up, desktop Core Web Vitals look good
  - Areas for improvement:
      - Mobile performance needs optimization
      - Old blog subdomain (blog.fossa.com) still being crawled
      - Some duplicate title tags and descriptions to address

### Registry Page Feedback

  - Structure suggestions:
      - Enhance title tag with relevant keywords (e.g., license, vulnerability, popularity)
      - Include package name in more headers
      - Improve meta description with layman's terms
  - Content enhancements:
      - Add internal linking to related packages
      - Consider adding FAQ section
      - Explore interactive elements (e.g., timeline of updates, package comparisons)

### Registry Launch Strategy

  - Start with a conservative batch (500-1,000 pages)
  - Theme batches if possible (e.g., all Ruby gems)
  - Ensure proper sitemap implementation and submission to Google Search Console
  - Manually force indexing of sitemap and individual pages
  - Add registry to site footer and possibly top navigation
  - Implement manual interlinking from other site areas

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Send 2 alternative comparisons for new content work stream in Slack
- Validate 404 fixes and broken image resolutions on FOSSA site
- Confirm slash URLs working correctly on FOSSA site
- Investigate sitemap issues, focus on subfolders/subpages not indexing

**Aaron Williams (FOSSA)**
- Review registry feedback list with Kevin Wang, plan implementation

---

## Transcript

**Aida Knežević:** That's like my number one priority today—just enriching the articles on their site.

**Jakub Rudnik:** Yes, yeah. Well, they're ahead on everything, it feels like, so that's good. You're almost done.

**Aaron Williams:** How's your week going?

**Aida Knežević:** Busy week.

**Aaron Williams:** We were at an event in Raleigh and I just got back late last night, so long week.

**Jakub Rudnik:** Any event or off-site throws everything off. Travel doesn't get accounted into your normal work week and time changes and all that. Hopefully the weekend can be somewhat relaxed.

**Aaron Williams:** I'm going to see the Golden State Warriors final game against the Clippers on Sunday. I don't know if it'll be less anxiety-inducing, but it'll be fun at least.

**Jakub Rudnik:** Yeah, the Warriors are hot right now. The Clippers are kind of back with Kawhi. They've got to beat them to get out of the playoffs. Both teams feel like they could win—I didn't think that two months ago.

**Aaron Williams:** Yeah, that's a good game to go to.

**Jakub Rudnik:** Alright, we've got a lot here. Let me jump into the agenda. I tried to organize all our notes, reports, and conversation topics into core buckets. We've got the migration—I want to check in on status and see where we can support. Then registry feedback, which is kind of priority 1B. And then new content work streams, probably priority three. But we have Aida ready to create content and get an MVP up, so once we figure out which work stream to go after, we can move with that simultaneously. That would be one of our goals coming out of this call.

**Andy Drukarev:** I wouldn't even say it's necessarily priority three. It's evolved, but we're definitely eager to get our first work stream up with you and see what we learn from it, get more insight into the process. I will say there's one existential question that came up—something I was talking to Kevin about before the call. Kevin posted the whole OWASP pillar page and bunch of cluster pages, but a lot of that is just hallucinated, inaccurate information. To be blunt, the parts about how we fix security issues—that's where I like your perspective. My philosophy has been you really don't want to delete content from the site unnecessarily. Introducing a 404 and then 301 redirecting it in our case would mean delete, fix, then put it back up—maybe a 302 redirect. It just gets messy. My approach has always been: get to staging, make edits, then go live and take down the page. Kevin's argument is it's dangerous to slow down and have speed compromised. I'm wondering about the internal debate on how damaging deleting a bunch of pages and 301ing them is, and these release considerations.

**Jakub Rudnik:** Yeah, good questions. I think there's a couple different layers here on where the risks are.

**Jakub Rudnik:** Yeah, a couple different layers on where the risks are. There's SEO risks, and I think there's audience trust risks, especially in your space—those are probably bigger than in some other industries I've worked with. If we stand up the OWASP Top 10 pillar and cluster pages, I love that we can see it in staging right away and get feedback quickly. The risk is that pulling down, putting back up, changing URLs adds technical debt and potential errors. I don't want to do that if we can avoid it. I think there are steps we can take. One approach is to start with no-index so we can see it in production and get the views without risk of it getting into Google. The other thought—my belief on this has evolved—if we publish this even if it's slightly inaccurate, as long as it's not in the footer and not ranking, it's not being read. It takes time to get clicks, and those clicks are small at the beginning. Early in my career at Scribe, we published quickly and updated over time, and we never had issues with people coming back saying content was off. But I understand the risk here. So the best of both worlds would be staging without deletion, no technical debt, then removing the no-index once we feel really good about the content.

**Andy Drukarev:** So starting with no-index and then removing it once it meets our correctness and credibility threshold. Kevin, I know you're listening—thumbs up? The question on our end is making sure pages come with proper no-index tags when we deploy.

**Jakub Rudnik:** Cool. So what's the first work stream to tackle? We should be doing these simultaneously. Since we have the OWASP infrastructure already set up and it looks great, that's a good spot to start—get MVPs of the content, make sure the structure feels right, then figure out how to nail the accuracies, especially around vulnerabilities. That's where we'll want your oversight. What additional content pieces would you produce in that work stream?

**Andy Drukarev:** That's a good question. Well, if we were doing this without the MVP, we'd use our work streams to create outlines, V1 content, calibrate with you on structure and accuracy. But my preference—Aaron and I agree—is to focus on a newer work stream we haven't started yet, just to see what the process is like end-to-end. Kevin has really built out a lot of the OWASP Top 10 content already. The areas I think are priorities are helping to prevent the correct issues—we need to relay that because there's some correctness stuff there. Some of the H2s probably have room for optimization. But that's so far along, I'd rather focus on a new work stream. That way we learn the process from end-to-end.

**Aaron Williams:** I agree. Seeing the process end-to-end is important, so starting with something new gives us a chance to get involved in it fully.

**Jakub Rudnik:** I like that there's medium volume with alternatives—it spreads wider, doesn't have to be one-to-one comparisons, and there are more targets and overall traffic volume. Aida, wasn't that in your original research?

**Andy Drukarev:** I believe so. Alternatives feels like it makes sense. We have some obvious ones—Black Duck alternative, Snyk alternative, standard types. That would be good for calibration.

**Jakub Rudnik:** Yeah, I'd start with really obvious alternatives—someone always compared to you—and then one that's half a step removed where it makes sense, so FOSSA can be in that conversation. Someone might not be aware your tool exists. We'll come up with two of those and post them in Slack, then move on to V1 and calibrate.

**Andy Drukarev:** Great. Then we can talk through the new site and registry.

**Jakub Rudnik:** Yeah, first thing—the migration is working well. Keywords are picking up and Core Web Vitals look really good on desktop. The site is working generally. There's cleanup to do, but we're already seeing improvement overall. Without even new content going live, this is a positive signal. Desktop has dramatically improved. On mobile, there's more sluggishness—we've seen some URLs drop from good to needs improvement. Nothing is a red flag, just some optimization needed on mobile. Not priority one with everything else going on, but worth looking into if anyone has bandwidth.

**Andy Drukarev:** We've been focused on fixing broken stuff—lots of 404s and image issues. That's been the main focus.

**Jakub Rudnik:** Where are you with the URLs and 404 fixes? Anything we can support on?

**Jakub Rudnik:** So where are you with the 404 stuff? Can we support on anything there?

**Andy Drukarev:** I've been laser-focused on 404s and broken images. If you want to validate them from your end, that would help.

**Jakub Rudnik:** I'll check the slash and confirm everything's working. Also, I found something weird—the old blog subdomain (blog.fossa.com) is still being indexed. It was surprising to find in GSC. They're still being crawled as of April 9th. It's not dangerous since there are no impressions or clicks, but Google's still crawling it and taking from your crawl budget. They don't need redirects since there's no traffic, but they're still existing to Google. It might be in an old sitemap that needs research, but cleaning this up will help. We also have a Screaming Frog report with similar secondary issues. There are some minor errors to clean up, but nothing is a red flag.

**Andy Drukarev:** That had to do with pulling stuff from Ghost initially. That shouldn't be part of this.

**Jakub Rudnik:** I'm trying to do regular checks, but especially with this migration, I want to do weekly checks digging into specific errors. If I can find batches we can move on, that's helpful. But the positive signals early after a migration—that's why this is positive to me. Typically migrations show a drop right away, so I feel good that everything we fix will be incremental lifts.

**Andy Drukarev:** I'm interested in tier-one errors—duplicate title tags, duplicate descriptions—those are on our to-do list. Keep flagging things as they come up.

**Jakub Rudnik:** Absolutely. Now let's move to registry and feedback. I have some feedback in different buckets—some small tweaks to page structure and keywords for crawlability, and some bigger ideas that might add value. I'll walk through the high level. Some minor things on structure: if this is our H1 with the software name, I wonder what else should be in the title tag. I suggested license, vulnerability, popularity—keywords that give long-tail searches and show what the page is about. Use layman's terms. Include the package name in headers like About, License Information, Pros and Cons—use judgment to avoid keyword stuffing, but the average reader won't notice and it helps Google understand the page. For meta descriptions, add more layman's terms that could be searched—what would you want this page found for? Coordinate with me on these edits.

**Aida Knežević:** My feedback was mostly on the actual text content rather than structure.

**Jakub Rudnik:** On internal linking, look at adding related packages—compare this package to that package, or show packages often used together. That shows relevance for the user coming in from one search and helps with crawlability when launching 300,000 pages. I'd put that module low on the page. Focus on relevance for viewers rather than forcing links to important pages. Consider adding FAQs—what else would someone search in Google? Add these at the bottom in collapsible sections so they're accessible. Some ideas could be programmatic without needing an AI writer. I've also seen interactive elements work well—timelines of updates, package comparisons, dependency graphs. I'm over-indexing on G2 here, but it's worth exploring. Some ideas might go into V2. The page has valuable information already and could launch now with tweaks.

**Aaron Williams:** What does batching actually mean? What does it physically look like?

**Jakub Rudnik:** Make the structural tweaks first, then decide when we feel good. Cluster or theme the pages if possible—for example, all Ruby gems if there's enough volume. The first batch could be 1,000 to 10,000. I'd err lower because of FOSSA's historical indexing issues, so start conservatively. Batch them, build that into a sitemap, make sure it's in GSC and indexing properly. Release 500-1,000 pages, watch for signals in GSC, make sure indexing is happening. Do forced manual indexing of the sitemap and individual pages—even small doses help speed up indexing and show Google the signals. Get the registry into the site footer and possibly top navigation. Do manual interlinking from other site areas. That's my rough approach. Most important is getting indexing and seeing positive signals so we can scale.

**Aaron Williams:** I don't think there are any questions. You and I need to look at that list with Kevin and start actioning it this week or next week.

**Jakub Rudnik:** If you're having issues with subfolders and sub-pages not indexing, that's my instinct on why. I'll look at the sitemap and get other eyes on it. Let's get that fixed. There's so much positive momentum. The site is working—that's not the issue. Let's nip this out and launch the registry to see a bunch of new organic traction.

**Andy Drukarev:** Cool, appreciate it. Lots of work to do on our end, but looking forward to the new content work stream you'll be producing. We'll continue the conversation.

**Jakub Rudnik:** Thank you all. Let us know if anything else comes up, and I'll work on the programmatic and technical pieces.

**Andy Drukarev:** Thank you, appreciate it.

**Jakub Rudnik:** Thank you.
