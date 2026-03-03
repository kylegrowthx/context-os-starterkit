# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-09-03
time: 16:30 UTC
duration: 13 minutes
organizer: vivek@growthxlabs.com
participants: Mara Leighton, Vivek Shankar, Paul Bratslavsky, Theodore Onyejiaku, Golzar Yaghoubpour
fathom_recording_id: 84708989
fathom_url: https://fathom.video/calls/397521617
share_url: https://fathom.video/share/ygjFdHXt2Ma14RCp1zWiYRoygTtYPk8-
source: fathom
enriched_on: 2026-03-02 14:30 UTC
speaker_note: Victor Coisne was invited but declined to join. Usman and Team GrowthX entries removed as they did not participate.
</metadata>

---

## Summary

GrowthX and Strapi completed their weekly sync focused on content production, performance metrics, and SEO optimization. GrowthX delivered 6 new content pieces last week with 6 more planned for this week, while performance hit new highs in sessions for GrowthX-generated blogs. Strapi's LLM presence remains strong relative to competitors (Contentful, Sanity, HyGraph), but citations lag at 4% — an area the teams agreed to address through content enrichment. Theodore agreed to publish latest blog posts to Medium working backwards chronologically, while Vivek will investigate batch metadata updates for integration pages with engineering.

---

## Context

Strapi and GrowthX maintain an ongoing content partnership where GrowthX creates and optimizes content for Strapi's website to drive traffic and AI visibility. This weekly sync is their core coordination meeting for content production, performance reviews, and next-week planning. Strapi's business model centers on their headless CMS platform; the partnership aims to improve Strapi's visibility in LLM results and AI overviews, particularly as Google organic traffic declines. The team tracks multiple metrics including blog sessions, non-branded impressions, conversion events, LLM referrals, and citations across Strapi's content and third-party comparison pages.

---

## Relevance

- **To GrowthX Delivery:** Content production velocity is high (6 pieces/week) and meeting targets. Blog content is driving stronger sessions than integration pages, suggesting a shift toward content-driven rather than comparison-driven SEO. The citation gap (4% vs. expected higher rates) indicates content may lack proper attribution structures for LLM ingestion — consider revisiting content format, metadata, and internal linking.
- **To CheckThat:** Strapi's presence in LLMs is positive relative to competitors, but declining LLM referrals to Strapi's own KB and homepage suggest AI overviews may be preferring external (GrowthX) content. Use this signal to audit CheckThat prompts for home services verticals and GA4 access to track which content sources drive the most AI traffic.
- **To GrowthX Business Development:** Account health is strong — content on track, performance metrics positive, team engaged on optimization. Victor Coisne (presumably product/strategy) skipped the call, suggesting Strapi is delegating operations to Theodore and Paul. Paul's move to Vegas may affect decision-making velocity; monitor for any delays in approvals or staging.

---

## Overview

- Content production on track: 3 pages refreshed last week, 4 scheduled for this week; 6 new pieces delivered, 6 planned
- GrowthX-generated blogs hit new session highs; integration pages staged by Friday
- Blog performance strong, non-branded impressions slightly down; demo clicks up significantly
- LLM referrals to Strapi KB/homepage declining, but Strapi's competitive position strong vs. Contentful, Sanity, HyGraph
- Citations lag at 4%; batch metadata updates for integration pages recommended to improve SEO
- Medium distribution workflow completed; blog posts to be published working backwards chronologically

---

## Key Topics

### Content Updates

- 3 pages refreshed last week, 4 scheduled for this week
- 6 new content pieces delivered last week, 6 planned for this week
- 5 competitor comparison pages to be staged by Friday (Payload, Butter CMS, Keystone, Tina, and others)
- Medium distribution workflow completed; will publish latest blog posts working backwards chronologically, excluding AI-written content

### Performance Metrics

- New high in sessions for GrowthX-generated blogs
- Top performing pages primarily from blog section; integration pages show strong results
- Non-branded impressions slightly down month-over-month but trending positive
- Conversion events show mixed results: Demo clicks increased significantly, other conversion events declined
- Google organic traffic steadily declining but offset by growth in AI overviews and LLM referral traffic

### LLM Performance

- LLM referrals to Strapi homepage and KB pages decreased in August
- GrowthX blog LLM referrals increasing week-over-week
- Strapi's presence in LLM results positive compared to competitors (Contentful, Sanity, HyGraph)
- Citations at 4% — identified as critical area for improvement to increase attribution in LLM outputs
- Next steps: await data from Scrunch team to identify which prompts show declining presence and enrich content accordingly

### Integration Pages & SEO Optimization

- Comparison pages list confirmed (Payload, Butter CMS, Keystone, Tina)
- Theodore suggested adding SEO metadata to all integration pages to improve search performance
- Vivek to check with engineering team on feasibility of batch metadata updates similar to previous AOP grid workflow
- Challenge: batch update tool requires backend access that Strapi doesn't currently expose

---

## Action Items

**Theodore Onyejiaku (Strapi)**
- Publish latest blog posts to Medium, working backwards chronologically (excluding AI-written content)

**Vivek Shankar (GrowthX)**
- Check with engineering team regarding batch updating metadata for all integration pages; report findings back to Theodore

---

## Transcript

**Mara Leighton:** Hey! How's it going?

**Paul Bratslavsky:** Good.

**Mara Leighton:** Love to hear it. Vivek, how is the weather?

**Vivek Shankar:** It's fantastic over here.

**Mara Leighton:** Paul, what about you? How's yours?

**Paul Bratslavsky:** Yeah, pretty hot, but it's nice. I'm actually moving to Vegas this weekend, so more heat. Pretty exciting.

**Mara Leighton:** Yeah, yeah, it's going to be fun.

**Paul Bratslavsky:** That's great.

**Mara Leighton:** Hi, everyone.

**Golzar Yaghoubpour:** How's it going? Are you back in New York?

**Mara Leighton:** I am, actually. Yeah, thanks for asking. I'm back in New York. And I was telling Vivek that I recently moved before going to Paris for the month. And so I came home to a decent amount of boxes, which is not an excellent experience. But yeah, I can't complain too much. It's nice to be back.

**Mara Leighton:** New York in the fall is the best. It's so nice. It's the weather we were just talking about it, and it's really quite lovely right now. It's the U.S. Open, you know, so a lot of friends are at the tennis matches. And every year it's been sweltering, but this year it's actually pleasant.

**Golzar Yaghoubpour:** Friday, the heat will be over, but it's been bad. We've had many heat waves and a lot of haze from the wildfire smoke. You can't see outside very well, so it's just not great.

**Mara Leighton:** I do feel like there are three weeks of perfect weather, and then it tips into quite cold. So I'm trying to enjoy this period while it lasts. I'm assuming we're waiting for Victor?

**Vivek Shankar:** He won't be joining.

**Mara Leighton:** Okay, well, lovely. We can just jump right in. Let me share my screen.

**Vivek Shankar:** So just running through the updates real quick. We had three pages refreshed last week, and we have four scheduled for this week. In terms of new content, we delivered six pieces last week, six for this week. And this week, we'll also be staging the initial five competitor comparison pages. So we'll be doing that by this Friday.

**Vivek Shankar:** The medium distribution workflow is done. The flow will basically just push it into your Medium account and then you can publish it.

**Theodore Onyejiaku:** Yeah, I think you could start with the latest ones and then go back through the dates. The last one I published on Medium were the ones from StrapiConf and the ones before then.

**Vivek Shankar:** Okay, so we will publish the latest blogs and then just keep working our way backwards then.

**Theodore Onyejiaku:** We are already publishing the blog posts from the first section and not the AI-written content.

**Vivek Shankar:** Understood. All right, moving on to the performance update. So following Victor's point last week about the integration pages, we divided the ones that you have generated versus the ones we have. So we hit a new high in terms of sessions for the blogs that GrowthX has generated. But even if we include the integration pages that Strapi generated, we hit a new high this past week. So generally all around good news.

**Vivek Shankar:** These pages over here perform the best. And as you can see, a lot of them are from the blog. And then over the past week, these five pages performed the best. Again, all of them from the blog.

**Vivek Shankar:** Looking at the non-branded impression performance, there was a slight drop, not a major one, but still pretty positive signs. Conversion events seem to have stalled out a bit. On a monthly basis, we have seen a drop compared to July. Demo clicks increased by a significant percent, but the rest seemed to have declined a little bit to various degrees.

**Vivek Shankar:** On Google traffic has been declining generally, it's been a steady decline, but overall traffic to some of our cohorts have increased, and one of the reasons for this is we're seeing greater presence in AI overviews and in LLM traffic.

**Vivek Shankar:** Speaking of LLM traffic, we've reached a stage with Scrunch where we can start digging deeper into some of the data. LLM referrals to Strapi's homepage and KB pages, other than the ones that we've created, have decreased in August. LLM referrals to GrowthX blogs seem to be increasing week on week.

**Vivek Shankar:** We went into Scrunch to see if we could isolate some of the prompts where Strapi's presence is decreasing. We couldn't quite isolate it just because of the way Scrunch presents that data. But overall, Strapi's presence in LLMs for all the prompts that we are tracking is pretty positive. We seem to be showing up more compared to Contentful, Sanity, HyGraph, et cetera.

**Vivek Shankar:** Citations are lagging at 4%, which is something we do need to work on. The next steps is really to see the data that the Scrunch team gives us back and see if we can enrich our content and create new content pieces from that.

**Vivek Shankar:** So as we're building out the comparison pages, I just wanted to confirm — is this the full list that you want us to follow? Payload, Butter CMS, Keystone, Tina, et cetera. Just want to confirm we're going to go ahead and create these. Is that fine?

**Theodore Onyejiaku:** Yeah, that's perfect. Thank you.

**Vivek Shankar:** Great. So I guess that's pretty much it for this week. If there's any other questions we can answer or clarifications.

**Paul Bratslavsky:** I think this was pretty straightforward. I don't have any questions on my end.

**Theodore Onyejiaku:** Just some suggestions. I noticed that the integration pages were kind of slowing down. So we suggested if we could add in some metadata to the integration pages. For example, when you try to publish one, or you take a look at one, you notice the SEO metadata are kind of missing. That would be a good idea to add this metadata and see if it will help with SEO.

**Vivek Shankar:** Metadata will certainly help. Do you want us to look at every single integration page?

**Theodore Onyejiaku:** Yeah, all the integration pages. So like before now, we kind of created a batch workflow on AOP that updated all our blog metadata using the AOP grid. So if it's something similar to that, but I just want to know if we could give access to that. Because when you view it from your own end, it's not accessible, right?

**Vivek Shankar:** I think we would have to check with engineering if that's possible because we're not on AOP anymore, but we can check and get back to you on that.

**Theodore Onyejiaku:** Yeah, thank you. That was pretty much it.

**Vivek Shankar:** Thanks, everyone. Great to see you.

**Mara Leighton:** Thank you. Bye, everybody.

**Golzar Yaghoubpour:** Thanks.
