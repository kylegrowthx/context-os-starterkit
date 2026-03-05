# Fossa <> GrowthX Strategic Session

<metadata>
date: 2025-04-03
time: 18:01 UTC
duration: 31 minutes
organizer: kyle@growthxlabs.com
participants: Kyle Gaudreau (GrowthX), Jakub Rudnik (GrowthX), Andy Drukarev (Fossa), Aaron Williams (Fossa)
fathom_recording_id: 55418776
fathom_url: https://fathom.video/calls/267181296
share_url: https://fathom.video/share/obzqvUJ_MSERXQQ8YeSKjoRSGydTxNR_
source: fathom
enriched_on: 2025-04-04 14:32 UTC
</metadata>

---

## Summary

GrowthX and Fossa identified critical SEO issues from Fossa's recent website migration: blog URLs are losing trailing slashes, causing redirect problems and potential ranking loss. Kyle will diagnose the root cause and provide remediation steps. The team aligned on a registry launch strategy—starting with 9 live pages out of 300,000, then scaling through careful sitemap management and GSC indexing monitoring. Looking forward, GrowthX will evaluate the registry page structure for SEO recommendations, and work with Fossa on three content pillars: competitive comparisons, OWASP Top 10 vulnerabilities, and CWE Top 25 weaknesses.

---

## Context

Fossa is a security and vulnerability management platform. GrowthX is providing SEO and content strategy support as part of an ongoing engagement. The company recently completed a major website migration (from Ghost + Webflow multi-system architecture to markdown-based static pages) and is now launching a large-scale registry of vulnerability and security content—300,000 pages with only 9 currently live. This strategic session brought together Andy Drukarev and Aaron Williams (Fossa product/content leadership) with Kyle Gaudreau and Jakub Rudnik (GrowthX SEO leads) to review migration health, plan registry rollout, and define content initiatives that leverage Fossa's AI-generated library.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic SEO methodology directly applied: managing 300,000-page registry launch through phased rollout, sitemap strategy, and batch indexing
- Cross-domain URL handling (trailing slashes) emerging as key technical requirement for future client migrations
- Content placement decision framework (blog vs. resource library) documented for reuse across similar projects
- Registry/database-driven content strategy validated as effective for large-scale vulnerability/comparison content

**To GrowthX Business Development:**
- Account expansion potential: content work stream just initiated (competitive, vulnerability, CWE pages)
- Early positive signal: Fossa experienced organic traffic uptick post-migration despite technical issues
- Renewal/continuation signal: multi-workstream engagement (migration support, registry strategy, content creation) indicates deepening relationship

**To CheckThat:**
- Fossa's AI-generated registry content (9 live pages, 300,000 ready) is high-volume vulnerability/security intelligence—relevant for CheckThat's security vertical visibility
- Competitive content strategy (Fossa vs. Snyk, etc.) may surface CheckThat opportunities in AEO audits

---

## Overview

- Site migration revealed redirect issues, particularly with blog URLs losing trailing slashes
- Registry launch plan: start with 9 live pages, then scale to 300,000 pages
- Content strategy to focus on competitive comparisons, vulnerability topics, and interactive experiences

---

## Key Topics

### Website Migration Issues

  - 25 404 errors identified; 20 resolved, 3 pending, few scattered issues remain
  - SEMrush audit revealed redirect chains and loops, particularly with blog URLs
  - Blog URLs lost trailing slashes post-migration, causing potential SEO issues
  - Non-blog pages maintained their URL structure (without trailing slashes)
  - Action: GrowthX to investigate redirect loops, crawlability concerns, and provide detailed diagnosis

### Registry Launch Strategy

  - 300,000 pages ready, 9 currently live
  - Plan: Index and optimize initial 9 pages, then scale production
  - GrowthX to evaluate page structure, content, and make SEO recommendations
  - Consider leveraging Stack Share for logical cross-linking
  - Develop sitemap strategy for manageable indexing by Google
  - Explore external linking opportunities for early promotion

### Content Initiatives

  - Three main content buckets identified:
    1.  Competitive content (e.g., "FOSSA vs. Snyk")
    2.  OWASP Top 10 vulnerabilities (11 pages)
    3.  CWE Top 25 security weaknesses
  - Discuss optimal content placement: blog vs. resource library
  - Consider interactive or application-like experiences for target audience engagement

---

## Action Items

**Kyle Gaudreau**
- Investigate redirect loops/crawlability issues. Check GSC for indexing problems. Send synopsis of forward slash issue diagnosis + examples to Andy via Slack.

**Jakub Rudnik**
- Rerun Screaming Frog crawl on live site. Check GSC for indexing issues. Investigate redirect loops/crawlability. Evaluate DevOps tools/guides in resource library.
- Analyze Registry pages, provide SEO structure recommendations. Research content placement (blog vs resource library) for new topics. Evaluate competitive/vulnerability content ideas.

---

## Transcript
**Jakub Rudnik:** That looks really good, obviously really clean design and a lot of the issues I found from that initial pass seemed cleaned up and fixed so I'm sure there's more to check but yeah it looks a lot progress there.

**Andy Drukarev:** Yeah, we had somewhere in the vicinity of 25 404s that were created during the transition.

**Andy Drukarev:** We've cleaned up 20 of them. I have a note to fix three more, and there are just a handful of scattered weird ones that are going to require some more nuance. There's a whole bunch of images in our blog that got screwed up—the feature image was broken or replaced—so that's been a big focus. But yeah, good to hear that the performance testing you've done has been positive, and we also love the design. Really very modern looking.

**Andy Drukarev:** Definitely.

**Jakub Rudnik:** So that's, I think, a good transition into the main agenda items. There's a ton to cover. Also, just acknowledging—with so much of this migration, we're slightly off our normal schedules. I want to get a sense of where you're at and how we can best use this week and going forward.

**Jakub Rudnik:** I'll share my screen. So, this will probably become normal after a week or two, but in our meetings, we've got "week one" items. I grabbed some tweaks, some additional questions, and some next steps I thought of immediately. We can definitely set on those, but I'm sure you'll add to it.

**Jakub Rudnik:** So I think we start with site migration and how we can support right now.

**Andy Drukarev:** So for the technical stuff, obviously the 404s are straightforward. But we're seeing a few other kind of errors come up in the audits—a shitload of new redirect chains and loops. When I go to validate the errors, it seems fine to me, but it's still concerning.

**Andy Drukarev:** Yeah, I'm curious what you're finding.

**Kyle Gaudreau:** What tool are you identifying those redirect loops from?

**Kyle Gaudreau:** I'll show you here in SEMrush.

**Andy Drukarev:** So lots of these couldn't reach the final URL. But when you actually click through to the initial redirect URL, it seems to work. So I just couldn't quite make sense of all these. Are these false positives or something?

**Kyle Gaudreau:** SEMrush is known to make things look a lot worse on site audits than reality, but that doesn't mean legitimate things aren't flagged either. So you took some of the first column where the redirect link is, and you said you weren't able to see the looping. Could you drop those URLs in the chat for me?

**Kyle Gaudreau:** The initial redirect URL. Yeah, basically, what we're trying to figure out is whether there's a link somewhere else to this or if it's in Google's index. Then we can follow that pattern.

**Kyle Gaudreau:** Let me take this screenshot.

**Andy Drukarev:** I'm putting a screenshot in a shared Slack channel as well.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** I'm not in the loop on every detail. What was that particular thing that you changed in the migration that would have caused redirects?

**Andy Drukarev:** There shouldn't have been any. We added a handful of manual 301 redirects for pages that broke, but nothing that we did should have impacted redirect chains.

**Kyle Gaudreau:** One thing standing out in the expanded view is that the old version had a forward slash and now it doesn't.

**Andy Drukarev:** We wouldn't have made that change.

**Kyle Gaudreau:** Was the CMS migration a piece of this?

**Andy Drukarev:** We don't technically have an open running CMS.

**Kyle Gaudreau:** I've seen this before—the forward slash is easy to miss. When we migrated from WordPress to Webflow, Webflow couldn't handle the forward slash. It can be easy to overlook. If there's a rule that changed the logic of "is there a forward slash or not," that might be causing the loop.

**Andy Drukarev:** Yeah, if you could look into that. Separately, the internal images that are broken is a known issue we're fixing. I've opened tickets and will continue to work on them. We also had some 500 errors that seem to have been resolved, so that's good.

**Andy Drukarev:** Most of the duplicate title tags and meta descriptions are not on our core site—they're in docs and things like that. But just to come back to site hygiene, we'd love your help investigating the redirect loops and crawlability concerns.

**Andy Drukarev:** I think the rest of the, the rest of the issues that are flagged like are known and straightforward and flexible.

**Jakub Rudnik:** I didn't get my initial next steps—rerun Screaming Frog now that it's live and out of staging. We'll do that and look through what we find. We can also look in SEMrush and GSC to see what's coming up straight from the source, if Google's giving us different versions. I think getting as much data and crawls as we can get our hands on will help us flag anything we find, especially those redirect chains. That does make sense, Kyle.

**Kyle Gaudreau:** I'm trying to find where the source would start. I was just looking at GA and one of the top logs, and it's very weird. Usually these things are quick to find, but I'm not picking up on the pattern yet. It's a bit of a mystery.

**Jakub Rudnik:** I have one more thing—a note on crawlability. If possible, put registry somewhere in the site footer as we're launching this. As that expands, we'll need to think through crawlability. Another thing is to check if there's anything orphaned. I'll take a look at that as well.

**Andy Drukarev:** Yeah, so that's most of the migration. One other piece—Kevin also launched around nine new DevOps tools plus long-form guides that were all AI-generated. We're QA-ing them now and would be super interested in understanding how they perform. It's not our highest priority, but if you had any thoughts on the DevOps guides or tools—both accessible under the resource library section—that would be interesting.

**Jakub Rudnik:** Yeah, that's great. I'm happy to do that as well.

**Andy Drukarev:** I think we can then shift to registry. So the current status—Aaron, chime in if I'm not representing this correctly. We have 300,000 pages basically ready to go. We have nine that are live now, and we want to start with these nine, get them indexed, make sure we're all on the same page about the contents, and then come up with a plan to scale production moving forward.

**Jakub Rudnik:** Yeah, the general playbook makes sense. Looking at the page structure and content—if you have questions right away or if you want us to evaluate what you have, we can do that.

**Andy Drukarev:** Ada had a question about the pulse section. I have a question out to Kevin since he built all these. Everything on these pages is AI-produced, so I'm not sure what process or combination of tools were used.

**Jakub Rudnik:** We'll give feedback. Everything on the page is pulled from third-party or your own data, so we won't need to create anything—just optimize structure and additions.

**Andy Drukarev:** With the caveat that if there are elements to these pages that would strengthen them from an SEO perspective, even if it means new modules being added, we're absolutely open to that.

**Andy Drukarev:** Could I show my screen?

**Kyle Gaudreau:** So I think I found an issue related to the forward slash thing I was flagging. Can you see my screen? OK. This is just top pages from the last seven days. Let's take this blog post for example. If I paste it in and keep close attention to the URL bar—the forward slash is being removed. From Google's perspective, the history shows the forward slash being there, but now it's not.

**Andy Drukarev:** That's odd.

**Kyle Gaudreau:** I was having trouble with the screen share, but here's what I pulled from GSC of one of your top blog posts from the last seven days. When I go to it, the forward slash is removed. When I check this in one of my Chrome extensions, the redirect that occurred was not a 301.

**Kyle Gaudreau:** To be crystal clear: adding or removing forward slashes means Google sees them as different URLs. That's quite critical. There are two options. There could have been a technical reason to remove the forward slash—like with Webflow migrations where it's necessary. But since you're not using Webflow, it could have been an oversight. The best case is going back and re-including the forward slashes. But if there's a reason you need to remove them, we definitely want to put in proper 301 redirects to tell Google we're moving the SEO value to the new URL. It's not too late to do this, but every day counts.

**Andy Drukarev:** I'm not clear where the issue originates. A year or six months ago, we were seeing 404s for fossa.com/blog because of the slash issue, but that was just the blog landing page—it didn't impact individual posts. I'm trying to find if there's anything in our codebase that would have caused this.

**Kyle Gaudreau:** What was the exact date of the migration?

**Andy Drukarev:** This Monday.

**Kyle Gaudreau:** It looks like the standard across the board was that you had the forward slash. It would be quite rare for a website to inconsistently have or not have forward slashes. It's usually one or the other.

**Andy Drukarev:** My challenge is just figuring out how this happened, because we didn't intentionally make this change.

**Kyle Gaudreau:** Focus your time on figuring out the cause, and then we can talk about mitigation.

**Andy Drukarev:** Can you send a brief synopsis of your diagnosis after we wrap? We can work internally to figure it out.

**Kyle Gaudreau:** We can send examples and clarify what's happening. For what it's worth, I've been part of countless migrations—this stuff happens. It's not too late to minimize any negative impact. I was looking at your data, and you've had an uptick in sessions since the migration. Every hour counts though.

**Andy Drukarev:** I think we're on the same page. My concern is just what caused this and how we can see it, because there's no obvious explanation.

**Andy Drukarev:** We're getting close to time, so let's talk through registry next steps and the bigger picture work streams.

**Jakub Rudnik:** Yeah, we'll look at those registry pages. That's obviously the priority. If you get answers to that one section, we'll look SEO structure-wise and make recommendations. I'd also like to chat with others on our team who have experience launching this many pages at once in a new subdomain. We'll need to get our sitemap in order to break it down into manageable chunks for Google, then roll out batches to ensure they're being indexed and crawled, then expand. I think that can go fairly quick once we validate things.

**Jakub Rudnik:** I also had a thought about Stack Share—there could be some logic to leverage it for cross-linking while adding value and helping with crawlability and indexing. I definitely want to know how you're handling the sitemap, as that will be key to Google finding all those pages. I also thought about external links—maybe automated press releases to jump-start promotion in the early days. Links will generate over time, but what could accelerate that?

**Andy Drukarev:** So as for next steps in our overall engagement, the website migration and registry have been the two priorities. Does it make sense to start a conversation about a content work stream as well?

**Jakub Rudnik:** Yeah, I think so. That's our bread and butter. With 300,000 pages already automated, that's where we normally step in with programmatic and other content streams. We'd love to know what you're thinking and how we can support. I think we can start thinking about that right now and add new content as well.

**Andy Drukarev:** We have a few buckets of content. One is competitive content—Fossa versus Snyk, Fossa versus other tools. That has search volume. Then there are vulnerability-type content: OWASP Top 10 vulnerabilities—probably 11 pages for the top categories—and CWE Top 25 for the most common security weaknesses. All of those have search volume.

**Jakub Rudnik:** Where would those live—blog or resource library? That's one option. We don't need to decide right now, but we'll evaluate that. With the competitive ones, we can note both "Fossa versus X" as well as "X competitors or alternatives," which can be really good too. There's some standard playbooks we can follow. I'll sync with Aida on these as well—they're in her wheelhouse.

**Aaron Williams:** We talked about this at the kickoff as well. One theory we have is that content that feels more interactive or like an application experience—rather than just text—will be more effective for our audience. Look at what we've produced with the registry.

**Kyle Gaudreau:** Yeah, one quick thing. I looked a bit more at the before/after. Previous to the migration, your non-blog pages did not have forward slashes, but your blog did. Now your blog doesn't. I'm not sure why.

**Andy Drukarev:** We used a few separate systems—Webflow for course site pages and our blog. There's probably some disparity in how those are set up.

**Kyle Gaudreau:** Webflow doesn't handle forward slashes—I learned that migrating from WordPress. That's just how it's built.

**Andy Drukarev:** Now everything is a collection of markdown pages—we're trying to build a CMS on top of it. For now, it's just markdown and individual static pages.

**Kyle Gaudreau:** So something in the blog side changed specifically. All your other pages are staying the same. Just your blog. Hopefully there's a single redirect rule that can address all of them at once.

**Andy Drukarev:** Let's continue on Slack. I think we have a sense that it was caused by the shift from Ghost to our new content hosting system. We'd be interested in your suggested fixes.

**Jakub Rudnik:** We'll send over examples and next steps. We'll continue working on the migration and fixes. Aida's back Monday—she'll work on the new work streams, and we'll both evaluate the registry pages. Thanks so much!

**Kyle Gaudreau:** Bye.
