# Engine Weekly Sync

<metadata>
date: 2025-08-14
time: 18:31 UTC
duration: 31 minutes
organizer: carrie@growthx.ai
participants: Carrie Chowske (GrowthX), James Winter (Hotel Engine), Joel Murphy (Hotel Engine)
fathom_recording_id: 80690864
fathom_url: https://fathom.video/calls/379493700
share_url: https://fathom.video/share/bTjyECutdusxdmDcM9faBQB9qntYtzsz
source: fathom
enriched_on: 2026-03-03 11:45 UTC
</metadata>

---

## Summary

Hotel Engine's content production is 5 weeks ahead with this week's content live and 5 pieces in review, positioning the team to experiment with LLM.txt and robots.txt optimization strategies while shifting focus from broad top-of-funnel content to product feature specificity. The team discussed how explicit robots.txt rules for LLMs are showing more promise than LLM.txt files alone, and agreed to move forward with filtering curse words from generated content and converting image-based CTAs to Webflow components for better accessibility and easier updates. James Winter introduced the new RoomBlocks.com domain strategy to build an inbound organic funnel for wedding room block bookings, separate from the main Hotel Engine brand, and requested a content plan including publishing cadence and SEO forecasting.

---

## Context

Hotel Engine is a B2B business travel platform that verifies business emails to provide discounted hotel rates to corporate travelers. GrowthX is delivering content production and SEO strategy services as part of a larger engagement. This weekly sync between Carrie Chowske (GrowthX's content lead), James Winter (Hotel Engine product/strategy), and Joel Murphy (Hotel Engine content/product) covers content production status, SEO experimentation, and new business opportunities. The team is in regular production mode after an initial sprint phase, with content banking strategy and analytics tracking becoming increasingly important as they prepare to scale multiple content initiatives including a new wedding-focused domain.

---

## Relevance

**To GrowthX Delivery:**
- Content production process needs explicit filters for profanity and brand-voice refinement. Carrie is refining prompts to ensure product feature mentions are explicit and contextually appropriate.
- Image-based CTAs should be replaced with Webflow components for accessibility compliance and easier future updates. This addresses a technical debt item that impacts sustainability.
- Query parameter tracking strategy (non-UTM) being implemented to avoid overwriting existing attribution data while enabling content performance measurement.
- Atlas-to-Webflow automated publishing prototype in development to reduce manual errors (broken links, spacing) and improve operational efficiency.

**To GrowthX Business Development:**
- Hotel Engine's wedding room block market shows strong organic growth potential. RoomBlocks.com domain represents a strategic expansion opportunity with new scope (content planning, domain architecture, SEO forecasting).
- Account health signals positive: content production cadence stable, team engaged in strategic discussions, willingness to invest in new initiatives suggests account expansion potential.
- Amplitude dashboard creation by Hotel Engine indicates their analytics maturity and interest in measuring content ROI.

**To CheckThat / AEO Research:**
- LLM.txt file creation with top 25-30 performing pages provides real-world data on content selection for LLM optimization. Explicit robots.txt rules showing more impact than LLM.txt alone.
- Shadow site approach discussion (LLM-friendly parallel content versions excluded from human search) signals emerging multi-version content strategy that may have broader implications for AEO.
- Social signals (Reddit, forums) confirmed as most influential for LLM recommendations by workshop speaker, validating community-driven content amplification strategy.

---

## Overview

- Content production is on track with 5 weeks ahead and regular weekly output
- Experimenting with LLM.txt and robots.txt strategies for SEO optimization
- New RoomBlocks.com domain planned for wedding-specific content and marketing
- Adjustments needed for content specificity, CTA components, and tracking

---

## Key Topics

### Content Production Status

  - 5 weeks ahead in content production, with this week's content already live
  - 5 additional pieces in review queue for Joel
  - Prioritizing content from Graphite list, evaluating recommendations

### SEO and LLM Strategies

  - Implemented LLM.txt file with top 25-30 performing pages
  - Exploring "shadow site" approach for LLM-friendly content versions
  - Mixed reports on LLM.txt effectiveness; explicit LLM allowance in robots.txt showing promise
  - Emphasis on writing for humans first, algorithms second
  - Social signals and Reddit/forum mentions remain influential

### Content Specificity and Product Alignment

  - Efforts to align content with product features more explicitly
  - Challenges in verifying product details, especially for new team members
  - Adjusting content to remove inappropriate language (e.g., curse words)

### CTA and Tracking Improvements

  - Discussion on replacing image-based CTAs with Webflow components for easier updates
  - Plans to implement query parameters for tracking, avoiding UTM overwrites
  - Prototype for automated publishing from Atlas to Webflow in development

### Analytics and Reporting

  - Increase in clicks and impressions observed in Search Console
  - Amplitude dashboard created but not yet shared
  - Ongoing work on data sync and potential new reporting capabilities

### Scrunch Query Adjustments

  - Updates to persona associations and feedback implementation in progress
  - Recalibration of category and persona buckets for improved analytics

### RoomBlocks.com Initiative

  - New domain acquired for wedding-specific room block bookings
  - Aims to build inbound organic funnel and separate B2C marketing from main Hotel Engine brand
  - Content banking and strategy development for the new domain requested

---

## Action Items

**Carrie Chowske (GrowthX)**
- Share links to this week's live content with Joel and James
- Send full analytics report to Joel and James
- Update Scrunch queries with new persona associations and feedback from Joel
- Develop content plan for RoomBlocks.com including publishing cadence and SEO forecasting

**Joel Murphy (Hotel Engine)**
- Investigate source of image-based CTA in blog posts; determine if should be Webflow component instead
- Review content specificity in generated articles, particularly product feature alignment

**James Winter (Hotel Engine)**
- Share Amplitude dashboards for blog post performance with Carrie and team

---

## Transcript
**Carrie Chowske:** Dog is chasing something in his sleep.

**James Winter:** Hey, folks.

**Carrie Chowske:** Hello.

**Carrie Chowske:** I think you're on mute if you're trying to talk.

**Carrie Chowske:** Yes, sorry. It's been one of those days. I've left myself on mute the whole meeting.

**Carrie Chowske:** How are you doing, James?

**James Winter:** Good. How about you?

**Carrie Chowske:** Good, good, good. We had another meeting run right back up to this one, so I was trying to quickly finish my last few things in our agenda. I'm sorry I didn't share that.

**James Winter:** No worries.

**Carrie Chowske:** Brain shift. Also challenging.

**Carrie Chowske:** Should we wait for Joel or do you want me to go ahead and get started?

**James Winter:** Yeah.

**Carrie Chowske:** Speak of the devil and he shall appear. How are you, Joel?

**Joel Murphy:** I'm good, thank you for asking. I have been the late devil a couple times this week.

**Carrie Chowske:** Don't worry about it. I was working on the agenda, which is why I hadn't shared it yet. I was just telling James, we had another meeting right before this one and I was still working on it.

**Carrie Chowske:** I was still working on the analytics report during a quick last-minute sync. But we're in a really good spot — we're in regular content production now, five weeks ahead. This week's content is already live on the site, and I'll share those links. We have another five pieces in the hopper for you to review, Joel, so we're ready to keep moving forward next week.

**Carrie Chowske:** I've gone through the Graphite list you mentioned and prioritized content to make sure we have good content coming in and build up that flow.

**Carrie Chowske:** I'll continue going through that and see if there's anything else to be done with the ones they recommended to delete. I don't think most of it aligns with our current state in terms of blue collar travel content. Some of their recommendations seem odd — if we're going to delete it, let's commit to it.

**Joel Murphy:** But then we need another page about that.

**Carrie Chowske:** Darrel, did you deliver the LLM.txt?

**Darrell Etherington:** I am just about to drop it in the channel.

**Carrie Chowske:** We produced that through our pipeline. The process was to take the top 25-30 performing pages on the site and articulate them clearly in markdown format, tweaked slightly for LLM digestibility. It's experimental, but we're also investigating another approach we haven't implemented yet: parallel generation for articles that produces a very LLM-friendly version, which would live on a shadow site pointed to by LLM.txt but excluded from robots.txt, so humans wouldn't want to read them if they find them in search.

**Joel Murphy:** Speaking of that, James and I were in a workshop earlier this week with a speaker who shared that LLM.txt didn't move the needle for them. But what did move the needle was explicitly allowing LLMs in robots.txt.

**Carrie Chowske:** Interesting. I think that's a fairly easy one for you to action on your side. But I'd want to run those in serial rather than in parallel so we could tell what's going on. Otherwise we'll just see that things were crawled, which doesn't tell you anything about how they're served. It's an interesting time in terms of experimentation — did we do something that worked? We did so many things. Which one of these levers actually was effective? I'll take your lead on that. That's a super interesting finding, and I want to do more research on it. The LLM stuff is still very early, and I've seen anecdotal reports in both directions.

**Carrie Chowske:** We have one client that's super new in terms of their entire content body — they don't really have any existing content. So they're an interesting use case for what happens when you're starting from scratch and trying some of these approaches. I think we're learning a lot from them, and they're the ones we're going to try this shadow site experiment with, which will be a third type of approach I can bring back.

**Joel Murphy:** I came away from that workshop with some interesting takeaways. There's a lot of stuff that's apparently working — at least for now — that's like old SEO tricks that became invalid at a certain point but are working again.

**Carrie Chowske:** I've talked a lot about that, but I'm always questioning: is this just my bias creeping in? You're saying old school good content production wins, which I would naturally have affinity towards because I'm an editorial person. Am I skewing my own results just because that's what I want to hear? I'm also curious who gave the workshop and what their source is. Are they someone trying to sell traditional SEO expertise? That would skew the message.

**Joel Murphy:** I didn't get that impression, but that's a fair question.

**Carrie Chowske:** I mean, I'm selling you guys something too. But it does seem almost ironic to do all this so the algorithm thinks we have better information, when really the answer is you're writing for the human doing the query. If the answer engine's working like it should, then those traditional SEO tactics of "write for humans first, algorithm second" actually work. I'm still largely of that opinion because the most influential factor is social signal. If your stuff gets read and discussed in communities populated by real humans that LLMs consider authoritative, that's the best signal you can get.

**Joel Murphy:** Those kinds of mentions were definitely in the workshop materials.

**Joel Murphy:** I haven't had a chance to go through it in absolute detail, but I did walk away with a few things. There are definitely some action items for us that we can take, ranging from simple stuff to more complicated things. It was already on my radar, but this gave it more reason to prioritize it. Things like content specificity, particularly on the product page side — we're not specific enough. We're not talking enough about certain product features. I'll probably have more to share next week about what we can address in this work.

**Carrie Chowske:** From a production standpoint, I've been trying to get more specific with how we're prompting and aligning content with product features. That's one of the persistent weaknesses regardless of the model — tying that connection back. If you explicitly say, "Wherever it makes sense logically within what you're talking about, bring up these product functions," you have to tell it explicitly. And then we tend to get much better results. Hopefully you're seeing more of that, where the content naturally mentions that our product does that. Flag anything you're not seeing.

**Joel Murphy:** I did pick up on that reading through last week's content — you're discussing pretty explicit product details. Of course, being new, it's still a challenge verifying that's actually how the product works.

**Carrie Chowske:** It's a never-ending challenge. You're like, "Wait, do we actually do that?" We're always having internal discussions about expenses, receipts, all that. And my brain immediately thinks, "That sounds like they should have used Engine." Which is funny — that's what makes me susceptible to marketing too. Even though I know all these tricks, I fall for them.

**Joel Murphy:** Understood.

**Joel Murphy:** One thing I wanted to flag — I tagged it in one of the posts — there was a curse word in there. Is there a way we could filter that stuff out so I don't have to flag it so granularly?

**Carrie Chowske:** Yeah, for sure. I think we maybe already modified the artifacts, but we can definitely add explicit instruction. Honestly, I left it in intentionally to see what you thought. I wasn't sure if this was me overreacting or if it was maybe the voice we wanted. The content does try to capture blue collar speech patterns sometimes.

**Joel Murphy:** I curse like a sailor, but it might be a little too much for the brand.

**Carrie Chowske:** It was easy to change "pain in the..." to "pain in the neck" and it means the same thing. We can add the filter to the generation process. And if we want to use the acronym PITA instead, that works too.

**Joel Murphy:** Works for me.

**Carrie Chowske:** We went back and got all the links fixed on those images. With delivering five pieces and being five weeks ahead, we have more time to address deeper needs. If you find something that really needs deeper attention beyond a quick read-through, we can make the time for it.

**Joel Murphy:** On the image thing — it looks like an actual component with text and a button versus an image contained within a link. What's the source of that?

**Carrie Chowske:** Did we set that up or did you guys drop it in? I'm not sure off the top of my head. That was something passed to us during the handover. I think we assumed you guys provided it. Either way, I agree it's not accessible best practices to have an image like that with a link.

**Joel Murphy:** Not a major deal, but if you want to change what it says, it's easier for us to create a Webflow component to drop in than an image we have to switch out.

**Carrie Chowske:** Yeah, and if it's a consistent component that we can reuse, that would be great. We could even add secondary CTA moments in articles if we want. I'll work with you on figuring out what's best there.

**Joel Murphy:** I'll figure out the source of that for us.

**Carrie Chowske:** It's always a tiered triage thing — we've got a CTA, we're good. We're at a phase now where we can revisit it. And we need some way to track CTA performance, which was on our to-do list.

**Joel Murphy:** I don't want to do UTM parameters since that overwrites existing attribution. But we could do some kind of query parameter outside of that.

**Carrie Chowske:** That makes sense. We could do that all together — convert the images to Webflow components and add query parameters for tracking. Since there aren't very many posts with images yet, it's an easy fix.

**Carrie Chowske:** We have a prototype on our end for automated publishing. With our Atlas tool, we're building in a step that creates the file in Webflow. After you review, we copy it back into our workflow and it automatically publishes. It's a cleaner way to get content from Google Docs into Webflow without manual errors like broken links or extra spaces. It's still manually reviewed by us, but it saves us time. We're also looking at Amplitude Dashboard to track blog post performance.

**Joel Murphy:** I created those dashboards but forgot to share. My bad.

**Carrie Chowske:** I had another meeting run up to this one and was still working on the Looker report. I want to make sure I'm giving you the right data and that it's pulling data correctly before I share it. I did a quick check on Search Console and we're seeing an increase in clicks and impressions. Clicks increased by the same percentage as last week, impressions are going up a bit faster, but click-through rate is about the same.

**Joel Murphy:** I'll share those dashboards. They give us some directional idea, though not many people click through blog posts and sign up immediately. We also have a data sync before our next meeting with a team working on some early-stage reporting that might be valuable for us. Still TBD on that.

**Carrie Chowske:** That's great. There are so many moving pieces, sometimes I lose track. I wanted to confirm a couple things before sharing the Looker report, but I'll get that to you soon.

**Carrie Chowske:** Yeah, see, it's, it's just, we're just forgetting things left and right, but no, it's okay.

**Carrie Chowske:** Yeah, but I would love to see that because I think, too, that gives us a little bit more, it might even give us a little more clue into what, even if we don't see direct from any of the blogs, you know, just kind of understanding to, and this kind of leads me into what I think, Daryl, we were talking about the Scrunch queries and that information we did get from Joel about the sentiment stuff.

**Carrie Chowske:** Yep, yeah, yeah, we are going to action the changes in, like, the persona associations and the other feedback you had on those, so stay tuned for that, but I was trying to do it myself in Scrunch and then realized I don't have the ability to change those associations.

**Carrie Chowske:** I think I just have to net new, upload a whole new CSV, like, I'll make the changes in the original CSV file.

**Carrie Chowske:** don't want to upload that batch, but yeah.

**Carrie Chowske:** And I like the, I think, I don't know if you saw my note, but I left a little note in there, like the little summary at the end about those personas and stuff.

**Carrie Chowske:** I added that to our context.

**Carrie Chowske:** And so I let the CM know, like, you know, hey, keep an eye on this.

**Carrie Chowske:** tell me if you notice a difference here in terms of, like, how it's talking.

**Carrie Chowske:** Because we've had to make some manual corrections a couple times.

**Carrie Chowske:** And so I'd be interested to see how well it kind of aligns with that.

**Joel Murphy:** I know the LLM stuff is experimental and a bit of a black box. As far as Scrunch itself, when you make those changes, what impact do they have?

**Carrie Chowske:** The changes are mostly organizational rather than affecting how Scrunch serves them. They help us inform our analytics better. Right now it's giving us overviews by persona bucket, but I think the category and persona buckets are calibrated wrong, so we're not getting good information about how searches show up for each buyer type and category combination.

**Carrie Chowske:** The LLM stuff reminds me of early-day attribution tracking — trying to figure out what happens between first and last touch. Over time, attribution tools like Amplitude have gotten better because of AI. I think we'll see LLM tracking evolve similarly — it'll learn more data and become more accurate, though it probably won't ever be one-to-one like traditional SEO.

**Carrie Chowske:** As costs come down and tools like Scrunch send massive query volumes, answer engines will eventually have to expose what they know or they'll waste too many cycles handling bot traffic trying to fudge the numbers. The big problem now is I don't think the model makers themselves have good metrics on actual query returns. They need to figure out how to find and track that before they can expose it. But they will eventually because it'll make them money.

**Carrie Chowske:** Another issue — based on my work with Perplexity and others — is how they handle tracking permissions and data storage. Perplexity's default is not to store information. I anticipate LLM tracking will evolve similarly to how attribution did.

**Carrie Chowske:** I think that's pretty much everything. We're business as usual for this week. Nothing too crazy.

**Joel Murphy:** I did want to flag a couple of things with you.

**Joel Murphy:** So the chart card stuff is still pending.

**Joel Murphy:** We have something basically yesterday, but it got moved a little bit.

**Joel Murphy:** Okay.

**Joel Murphy:** Nothing to share quite yet there.

**Joel Murphy:** So, James, can you help me explain to this group the Roomblocks idea and what we want to do with that?

**James Winter:** Yeah.

**James Winter:** So I brought this up early on in our engagement, but...

**James Winter:** How do do this without going down a big rabbit hole?

**James Winter:** so our core platform, business travelers only.

**James Winter:** Like, to use Engine, you have to have a business email that we can verify is attached to a real company.

**James Winter:** That's because...

**James Winter:** Because...

**James Winter:** The relationship that we have with the hotels, they're willing to offer us discounted rates as long as we verify that people that are using the platform, the only people that will see those discounted rates are verified business travelers.

**James Winter:** That's true if you're booking flights, rental cars, hotels.

**James Winter:** It is not true if you are booking a room block of, let's say, 15 rooms.

**James Winter:** So for whatever reason, the hotel industry has all agreed upon this sort of standard where if you are booking more than eight to 10 rooms, you have to go through a whole separate process because they don't want to incur a bunch of risk of like, I'm going to go book 50 rooms on someone's web, on some hotel's website, and then I'm just going to cancel them the week before.

**James Winter:** course, they have sort of like a different terms and conditions and like sales, you basically go through a sales process where you'd have to reach out to a hotel, contact them, get a quote, say for how many days you need the rooms, like think about getting married, you've got to go secure a room block for all of your guests.

**James Winter:** You can't just, like, do that online.

**James Winter:** So we launched the Groups product last year, which is for room blocks of 10 or more.

**James Winter:** That unlocked this whole new B2C motion for us, so we can actually sell room blocks to consumer customers, and that's been an incredibly fast-growing part of the business.

**James Winter:** The issue is weddings are the number one use case for room blocks, just across the board, but especially on the B2C side.

**James Winter:** Most of our acquisition of weddings is either through partnerships or through paid search and social.

**James Winter:** The issue with paid social specifically is that ads are being served by our Engine account. If you see the ad, click on Engine's profile, and go to engine.com saying "make work travel less work," it doesn't make sense for wedding room block bookings.

**James Winter:** On top of that, weddings are such a specific topic that I don't want to dilute our main domain with wedding content. So we bought RoomBlocks.com and HotelsForWeddings.com. We're standing them up as separate domains with a couple of goals. One is to build an inbound organic funnel that's not reliant on paid search and social. Two is so that when we target ads from paid social, we have a separate social handle and website, so we're not fighting this battle of relevance where we have to dilute the message or positioning on our main website for this specific use case.

**James Winter:** When I talked to Marcel early on, he said you guys would be able to support the additional domain and spin up wedding-related content for it. We've acquired the domain and are working on site infrastructure. It's still early, but I want to start generating articles to get it populated.

**Carrie Chowske:** Great. Are RoomBlocks.com and HotelsForWeddings.com pointing to the same content?

**James Winter:** I don't think we're launching HotelsForWeddings quite yet. RoomBlocks is the better domain, so I want to stand that up first and then do HotelsForWeddings once it's in good shape.

**Carrie Chowske:** That solves the problem we were talking about with creating a new collection in the CMS. I noticed we were publishing wedding content that was still going in the business travel guides folder.

**Joel Murphy:** Yeah, that's not right.

**Carrie Chowske:** Should we hold wedding content until you're closer to kicking this off, or do you want to bank it now?

**James Winter:** Banking it would be good.

**Carrie Chowske:** Great, we can do that. Can you put together a plan for the fresh domain — what publishing cadence makes sense and how long until we'd expect the site to start ranking?

**James Winter:** That would be super helpful. We're still in exploration phase on the content strategy.

**Carrie Chowske:** Absolutely. Group bookings have a lot of opportunity since people have to make phone calls and can't set it up online. There's a lot of market there.

**James Winter:** We've already seen a ton of success with the Groups product, and you're not even optimized for it yet. There's a lot of opportunity.

**Carrie Chowske:** I'll bring this back to Marcel directly since he'll probably want to give you a strategic pitch on maximizing this opportunity. There will probably be scope discussion, but we have a menu of deliverables depending on what you want to do.

**James Winter:** Sounds good. Thanks, guys.

**Carrie Chowske:** Thanks a lot. It was nice talking to you guys.

**Joel Murphy:** Bye-bye.

**Carrie Chowske:** Bye-bye.

**Joel Murphy:** Bye-bye.
