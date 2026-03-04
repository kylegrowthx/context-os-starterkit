# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-06-11
time: 17:31 UTC
duration: 34 minutes
organizer: Aida Knežević (GrowthX)
participants: Mark Stiltner (Rapyd), Marc Winitz (Rapyd), Aida Knežević (GrowthX), Rachel Pasche (GrowthX)
fathom_recording_id: 67834587
fathom_url: https://fathom.video/calls/322348093
share_url: https://fathom.video/share/Fkj5HjsxsSr1J_mTDn25sgYsL_Jcj4Ff
source: fathom
enriched_on: 2026-03-03 15:45 UTC
</metadata>

---

## Summary

Rapyd and GrowthX reviewed content production processes and SEO performance during GrowthX's scheduled audit week (June 16-20). GrowthX published 8 new articles in the past week with strong SEO results—"What is PIX?" now ranks #1 and appears in AI overviews, with 30 keywords showing ranking improvements and 2 new keywords entering the top 3. The team discussed XML file technical adjustments (URL slug implementation, proper contact URLs), a recurring list of content errors to avoid (smart payment routing claims, "100+ countries" phrasing, fee mentions), and explored expanding the content strategy beyond the current three clusters into a new high-value area: referral partnerships content (how to become a partner, sell Rapyd, onboard merchants).

---

## Context

Rapyd is a global fintech company offering payment processing and related services across 100+ markets. This is a weekly operational sync between Rapyd's content and product team (Mark Stiltner, Marc Winitz) and GrowthX (Aida Knežević, Rachel Pasche), who handles their content marketing. The meeting occurs during GrowthX's internal audit week—a planned pause in content production to migrate platforms, optimize workflows, analyze performance, and conduct QA across all client projects. Marcel Santos, GrowthX's CEO, is conducting a listening tour of all clients the following week (June 16), with Rapyd's CMO (Mark) planning to attend.

---

## Relevance

**To GrowthX Delivery:**
- Audit week process is transparent with clients; momentum maintained even during 7-day production pause.
- XML file integration requires technical refinements: URL slugs must use Airtable slug field (not full title), contact URLs must include /blog suffix for proper form attribution.
- Content error guidelines from Rapyd inform LLM prompts: remove smart payment routing claims (not a Rapyd capability), replace "100+ countries" with "worldwide," delete fee/pricing comparisons.
- High-velocity publishing (8 articles in one week) generating rapid SEO wins; content strategy discussion signals readiness for deeper audience research and expanded topic clusters.

**To CheckThat:**
- Rapyd content is optimizing for AI overviews through basic SEO + AI-friendly formatting (bullet points, short paragraphs, strategic headers)—article on "What is PIX?" now appears in AI overview results alongside #1 ranking.
- Marc Winitz raised direct question: "Is there a way to optimize to show up in AI overviews based on what you're learning?" Opportunity to define CheckThat positioning around LLM/AEO optimization for clients.
- Aida flagged ongoing CheckThat team work on AI optimization with Jacob (mentioned as having scheduling conflict); insights coming in "weeks to come."

**To GrowthX Business Development:**
- Rapyd account is healthy: high-volume content production ongoing, proactive about strategy refinement, planning for next strategic phase.
- Referral partnerships cluster identified as expansion opportunity—potential for custom/specialized content even without keyword volume (targeting LLM search use cases).
- Rachel Pasche already has proven track record on niche audience content (dental staffing app example); demonstrates capability for Rapyd partnership vertical work.

---

## Overview

- GrowthX is conducting an audit week next week, pausing content production temporarily
- SEO performance for Rapyd content is showing positive trends, with improvements in keyword rankings
- Rapyd team to review content clusters and prioritize future topics, potentially including referral partnerships
- Several minor content and technical adjustments identified for ongoing optimization

---

## Key Topics

### GrowthX Audit Week

  - Next week (June 16-20) GrowthX will pause content production for an internal audit
  - Audit goals: transition to new platform, analyze content performance, optimize AI workflows, conduct QA
  - Content production will resume after the audit week

### SEO Performance Update

  - 8 new articles published recently (4 last Thursday, 4 on Monday)
  - Potential issues with Google Search Console data in Looker reports identified
  - SEMrush report shows improvements: 30 keywords improved in position, 2 new keywords in top 3
  - Notable ranking: "What is PIX?" now ranking \#1 and appearing in AI overviews
  - Currently tracking 216 keywords for Rapyd-GrowthX collaboration

### Content Strategy Discussion

  - Current focus on three clusters: payment processing, niche payments, cross-border payments
  - Considering expansion into new clusters or deepening existing ones
  - Potential new cluster suggested: referral partnerships (how to become a partner, sell Rapyd, etc.)
  - Discussion on creating specialized content for LLM searches, even without obvious keywords

### Technical and Content Adjustments

  - URL slugs in XML files need adjustment (use slug from Airtable, not full title)
  - Errors to watch for: remove mentions of smart payment routing, update "100+ countries" to "worldwide"
  - XML file updates needed: add topic as plain text, use correct contact URL for blogs

---

## Action Items

**Aida Knežević (GrowthX)**
- Check Looker dashboard Friday. If no data appears, change to GA4
- Discuss AI/LLM optimization approach with Jacob
- Follow up with Jacob on referral partnership content value and search strategy
- Share Andreessen Horowitz AI content optimization article with Mark Stiltner (Rapyd)

**Mark Stiltner (Rapyd)**
- Strategic discussion with Marc Winitz about content clusters and expansion strategy
- Develop detailed audience profile for referral partnership content to support keyword research
- Share common content errors list with Rachel Pasche (GrowthX)

**Marc Winitz (Rapyd)**
- Strategic discussion with Mark Stiltner about content clusters and expansion strategy

---

## Transcript

**Mark Stiltner:** I wanted to talk through cadences for batches. I got some requests from my web manager on how many XML documents to include per batch, when and where to send them. I wanted to run that by you and let you know that's fired up and ready to go. I've been making a list of things that come up over and over again that we want to improve, so I can share that with you on this call.

**Aida Knežević:** We have a couple of updates on the performance side, but before we get into that, I wanted to let you guys know that next week is going to be audit week at GrowthX. We're moving away from Aeroflow to our own internal platform, which will take some time for our team to adjust to. During that audit week, our team is going to be analyzing all of the content we do for you, analyzing the performance metrics to identify strategic opportunities, and optimizing our current processes to make them more efficient in the AI workflows. We're also doing QA across all active projects. So next week we're not going to be delivering new content. We're going to resume publishing when we come back. I think you're meeting this week or next week?

**Mark Stiltner:** Marcel is doing a listening tour. He's meeting with all clients, and our CMO, Mark, would like to be in on the meeting. Yeah, so our meeting with Marcel is going to be June 16th.

**Aida Knežević:** So that is next week.

**Mark Stiltner:** Yeah, Mark said anytime except for June 13th, so I think we're good. I'm on the call by the way, Sarge's not on video yet. So that's what's going to be happening next week, and when we come back, content production is going to resume. I was looking at your Airtable today and I'm glad to hear that the XML files are working.

**Aida Knežević:** One thing I would say to watch out for is some of these URL slugs are too long. We recommend keeping them to five to seven words. The URL slug should come from Airtable—this is what you use when publishing the content. When Tom uploads the XML files, WordPress automatically sets the URL slug as the article title, but what it should be is the slug column from Airtable. So when Tom does the XML import, he needs to change it from the title to the slug from your Airtable.

**Mark Stiltner:** I thought we weren't writing the slugs. I thought you guys were feeding us this, and I told Tom not to change the URLs because they need to track in Looker.

**Aida Knežević:** Right, that's what should happen. When he imports the XML files, it's automatically setting the URL as the title, but he needs to change it to the slug from Airtable.

**Mark Stiltner:** Got it. I'll just tell him to go to Airtable and change that for now.

**Aida Knežević:** Thank you. On the performance side, we published eight new articles—four last Thursday and four on Monday. I've added those to Looker. One thing we're seeing with Looker reports is there are issues with Google Search Console sending data to Looker reports. For example, in your performance report from last week (week 22), there's a marked decrease in traffic, but we're not seeing any data for this week, which shouldn't be happening. I spoke with Jacob today about this and with another team member who experienced the same issue. He switched his Looker dashboard to pull from Google Analytics instead and resolved the problem. I'm going to check on Friday, and if the data still isn't showing, we'll need to change it to GA4.

**Mark Stiltner:** I'd love to see the growth we're experiencing reflected in there.

**Aida Knežević:** I can set up a GA4 filter to exclude our own blogs and share that with you. In terms of position tracking, I looked at the SEMrush report. Last week, 30 keywords improved in position and we have two new keywords in the top three, though we lost three. Swift Alternatives dropped from position one to position three, but that's not a strategically key keyword for us. What's really good is that we're getting articles indexed quickly and ranking highly. Overall growth is looking good. Once we get more data now that we're publishing at higher velocity, we'll be able to see which content verticals get the most traction and tailor our approach accordingly.

**Aida Knežević:** Do you have any questions?

**Marc Winitz:** I wasn't on video at the start. Let me understand what we're looking at. For example, where it says "What is PIX?"—position in Google was 14, so it appeared in search results?

**Aida Knežević:** Yes, and now it's showing up at number one, and it also appears in AI overviews. When AI overviews show up, your link appears next to the description. Considering AI overviews are taking up a lot of search traffic these days, that's pretty good.

**Marc Winitz:** So it's both the first SERP result and in the AI overview area?

**Aida Knežević:** Yes. The star icon means featured snippet—that's a link with a brief description that gets a lot of clicks.

**Marc Winitz:** How many keywords are in this table? Are these just blog posts?

**Aida Knežević:** We're tracking 216 keywords in SEMrush that we identified during initial keyword research. This is not all keywords Rapyd tracks—it's the keywords we're optimizing for with GrowthX.

**Marc Winitz:** How long did it take to see these results?

**Aida Knežević:** Pretty quickly. We published our first content about a month and a half into the engagement, and Swift Alternatives started ranking highly right away. We're in week 13 now and started publishing around week six, so about six weeks total.

**Marc Winitz:** Is there a way to optimize specifically to show up in AI overviews? Are we actively doing that?

**Aida Knežević:** That's a great question, and many clients are interested in LLM optimization. Following basic SEO principles with good content structure gets you good rankings and AI overview inclusion. AI and LLMs favor digestible content—bullet points, short paragraphs, strategic use of H2s and H3s. We're already doing that. We have an internal team tackling AI optimization specifically, so we'll have more info in the weeks to come.

**Marc Winitz:** What does the "I" and "C" mean for intent?

**Aida Knežević:** Intent means search intent. "I" is informational—the user wants an answer to a question. "C" is commercial—they want to investigate brands or services. SEMrush analyzes the top-ranking content and assigns this programmatically. We want to rank for informational and commercial keywords, not navigational or transactional, because those bring useless traffic.

**Marc Winitz:** What does KD percentage mean?

**Aida Knežević:** Keyword difficulty shows how hard it is to rank for a keyword. It's calculated by SEMrush and other companies—not from Google. It shouldn't be taken as gospel. Sometimes it's worth targeting difficult keywords even if your site isn't as authoritative.

**Marc Winitz:** What about volume? Some keywords show 50, others show zero. Are there really zero searches?

**Aida Knežević:** Volume estimates monthly searches based on 12 months of historical data. It's almost always underestimated because there's not enough historical data for emerging trends. Also important: this data is based on UK searches, which is a smaller set. Factor in US and Europe searches and you get much more traffic. You'd be presenting yourselves in those searches too.

**Aida Knežević:** I'm a freelance writer for SEMrush and have explained these concepts in many articles, so I'm happy to answer. Will you send us that Andreessen Horowitz article on AI content optimization?

**Mark Stiltner:** Yes, I will.

**Aida Knežević:** Now, on content clusters—when we started, you prioritized three clusters: payment processing, niche payments, and cross-border payments. We've covered most of the obvious topics in these three, but there's always room to expand. We could also explore long-tail keywords and additional angles to build more authority, or we could move into other clusters.

**Marc Winitz:** Is it better to go deeper on these three or start expanding?

**Aida Knežević:** One approach is to look at what's working well and find long-tail variations and additional angles. We could also set aside time for other clusters since we're publishing at high velocity.

**Mark Stiltner:** I know one cluster I'd love to develop: referral partnerships. We've heard from Kristen Lee multiple times—referral partners sign up but don't know how to sell Rapyd. We're pushing for partners in the US and other regions. I see potential for content on how to get started referring, what to do once you're a partner, how to become one, how to onboard merchants successfully. There's real depth there.

**Marc Winitz:** That's interesting. You might be onto something. Before the HubSpot cutover, I used to get every lead from partner contact forms—seeing how they come in and what they say. It's not just referral partners either, there are ISO paybacks, and how they view themselves. From an SEO perspective, is there search volume for that? People are searching for how to work with companies like yours?

**Mark Stiltner:** Maybe it's an experiment worth trying.

**Aida Knežević:** There's a lot of discussion about how SEO will evolve with people using LLMs. I'd like Jacob's input on this—he had a conflicting meeting—but I believe there's real value in creating specialized content even without obvious keywords, because people ask ChatGPT and Perplexity those questions. There could be untapped search volume, so it's worth testing. Mark, we can develop audience profiles—here's what this audience looks like, what they care about, how it relates to Rapyd. That context could help find keywords that bring the right people, even if they're not payment-specific.

**Aida Knežević:** Rachel has experience with this kind of specialized content. She created pieces for a dental staffing app targeting dental hygienists with employment tax content, and those performed really well. We've done this kind of work for other clients before.

**Mark Stiltner:** So let's follow up with Jacob on the referral partnership strategy, and we'll work on developing those detailed audience profiles to help guide the keyword research. I have a list of content errors we've been seeing that I wanted to share with you, Rachel. These are things we need to watch for and fix as we're editing.

We keep talking about smart payment routing. This is one thing we don't actually offer. It's come up because we have case studies where payment orchestrators who use Rapyd have smart routing, but we don't want to promote it to someone looking for a solution. And I'm starting to see in articles that we're even saying Rapyd offers smart payment routing. We don't. That's not a capability we have. So watch out for that and remove it.

I'm still seeing "100+ countries." Anytime you see that, just change it to "worldwide."

Lower processing fees comes up a lot. Whenever you see anything talking about fees, just delete it. We're not going to be the cheapest, but we're going to be the best. We don't compete on fees. So lose that.

One other important thing for the XML file: we need to add the topic as plain text. Whatever the topic of the blog is, which should match our content bucket, needs to be added in plain text between the tags. Also, for the contact URL in blogs, we actually track a separate contact URL that is slash contact slash blog. That's so it's easy for us to know anybody who fills out a form that comes from the blog. Right now it's filling in just slash contact, which we don't want. So keep an eye on that.

**Aida Knežević:** That's not a big deal. It's not going to go to a 404 page?

**Mark Stiltner:** No, slash blog is the exact same form as slash contact. It's just that we made a separate one for the blog so it's easy for us to know everybody who comes through from the blog.

**Aida Knežević:** Okay, that's perfect. Not a big deal at all. Just add blog at the end of the URL.

**Mark Stiltner:** Yeah, so that's my list of things. None of this is big stuff. It's all fine tuning.

**Aida Knežević:** Well, thank you so much for your time. I'll send over the link to that Andreessen Horowitz article in Slack. And yeah, hope you have a great meeting with Marcel next week. Let us know how it goes. And yeah, we'll be in touch.

**Aida Knežević:** We have a couple of updates on the performance side, but before we get into that, I wanted to let you guys know that next week is going to be audit week at GrowthX. We're doing this for the first time. We're moving away from Aeroflow to our own internal platform, which will take some time for our team to adjust to. During that audit week, our team is going to be analyzing all of the content we do for you, the clients, analyzing the performance metrics to identify strategic opportunities, and optimizing our current processes to make them more efficient in the AI workflows. We're also doing QA across all active projects. So next week we're not going to be delivering new content. We're going to resume publishing when we come back.

**Aida Knežević:** I think you're meeting this week or next week?

**Mark Stiltner:** Marcel is doing a listening tour. He's meeting with all clients, and our CMO, Mark, he responded and said he would also like to be in on the meeting.

**Mark Stiltner:** Yeah, so our meeting with Marcel is going to be June 16th.

**Aida Knežević:** So that is next week.

**Mark Stiltner:** Yeah, Mark said anytime except for June 13th, so I think we're good. I'm on the call by the way, Sarge's not on video yet.

**Aida Knežević:** So that's what's going to be happening next week, and when we come back, content production is going to resume. I was looking at your Airtable today and I'm glad to hear that the XML files are working.

**Aida Knežević:** One thing I would say to watch out for is some of these URL slugs are too long. We recommend keeping them to five to seven words. The URL slug should come from Airtable—this is what you use when publishing the content. When Tom uploads the XML files, WordPress automatically sets the URL slug as the article title, but what it should be is the slug column from Airtable. So when Tom does the XML import, he needs to change it from the title to the slug from your Airtable.

**Mark Stiltner:** I thought we weren't writing the slugs. I thought you guys were feeding us this, and I told Tom not to change the URLs because they need to track in Looker.

**Aida Knežević:** Right, that's what should happen. When he imports the XML files, it's automatically setting the URL as the title, but he needs to change it to the slug from Airtable.

**Mark Stiltner:** Got it. I'll just tell him to go to Airtable and change that for now.

**Aida Knežević:** Thank you.

**Aida Knežević:** On the performance side, we published eight new articles—four last Thursday and four on Monday. I've added those to Looker. One thing we're seeing with Looker reports is there are issues with Google Search Console sending data to Looker reports. For example, in your performance report from last week (week 22), there's a marked decrease in traffic, but we're not seeing any data for this week, which shouldn't be happening. I spoke with Jacob today about this and with another team member who experienced the same issue. He switched his Looker dashboard to pull from Google Analytics instead and resolved the problem. I'm going to check on Friday, and if the data still isn't showing, we'll need to change it to GA4.

**Mark Stiltner:** I'd love to see the growth we're experiencing reflected in there.

**Aida Knežević:** I can set up a GA4 filter to exclude our own blogs and share that with you. In terms of position tracking, I looked at the SEMrush report. Last week, 30 keywords improved in position and we have two new keywords in the top three, though we lost three. Swift Alternatives dropped from position one to position three, but that's not a strategically key keyword for us. What's really good is that we're getting articles indexed quickly and ranking highly. Overall growth is looking good. Once we get more data now that we're publishing at higher velocity, we'll be able to see which content verticals get the most traction and tailor our approach accordingly.

**Aida Knežević:** Do you have any questions?

**Marc Winitz:** So, I do, sorry, this is my first chance to see this, because I was not on video.

**Marc Winitz:** So, just so I can understand what I'm looking at, Aida, like, for example, here, hey, Marc, can you go back, or whoever is surfing, go down a little bit on this graph, right, stop right here.

**Marc Winitz:** So, okay, where it says, like, what is PIX?

**Marc Winitz:** So, position G in second was 14.

**Marc Winitz:** Does that mean, like, in Google search results it came up?

**Marc Winitz:** Yes.

**Marc Winitz:** Okay.

**Aida Knežević:** And now you're saying.

**Marc Winitz:** That it's shown up in the number one search ranking?

**Marc Winitz:** Yeah, yeah, exactly.

**Aida Knežević:** Except this icon right here, it says AI overviews.

**Aida Knežević:** So it's referenced, you know, when AI overviews show up, it shows up as one of the links next to the description, which is, considering AI overviews is like eating up a lot of search these days, this is pretty good.

**Aida Knežević:** Yeah, so I want to make sure I understand that, and totally agree, by the way.

**Marc Winitz:** So, yes or no, first question is, is it showing up as the first SERP?

**Marc Winitz:** Yes.

**Marc Winitz:** And it's also a link in the AIO area?

**Marc Winitz:** Yes.

**Aida Knežević:** Yeah, yeah.

**Marc Winitz:** How many, how many, what's the difference between the, like, the little Star King thing, you know, hat, and what's the difference between that and that other icon?

**Mark Stiltner:** Mm-hmm.

**Aida Knežević:** So, this icon right here means it's featured snippet.

**Aida Knežević:** So, when you Google something, and it, you see, like, like,

**Aida Knežević:** A link and a brief description, not an AI overview, but a brief description, that is a featured snippet, and those get a lot of clicks.

**Marc Winitz:** And then if we look at this air table, how far down does this list go?

**Marc Winitz:** Is this just blog posts?

**Marc Winitz:** This is all keywords that we're tracking in SEMrush.

**Aida Knežević:** So these are all the keywords that we identified during our initial keyword research.

**Aida Knežević:** And we just uploaded them into this SEMrush project and we're tracking our performance week over week.

**Mark Stiltner:** And this is not all keywords that Rapyd is tracking, this is all keywords that we're tracking that we're optimizing with GrowthX.

**Marc Winitz:** Okay.

**Marc Winitz:** Got it.

**Marc Winitz:** How many keywords do we have in this table?

**Marc Winitz:** I'm sorry.

**Aida Knežević:** I think we have 216.

**Marc Winitz:** And then is there a way to sort it that shows if you...

**Marc Winitz:** Scroll down to the keyword tables, is there a way to show, is it like in priority ranking, like one, like position eight, is that like showing like, you know, its position.

**Marc Winitz:** So for here, sorry, if you just scroll down, I just wanted to see this.

**Marc Winitz:** Got it.

**Marc Winitz:** Got it.

**Marc Winitz:** Okay.

**Marc Winitz:** So we start to cut out there.

**Marc Winitz:** Okay.

**Marc Winitz:** And, and, um, Aida, how long did it take for us to start to see these kinds of results?

**Aida Knežević:** Um, I think pretty quickly, if I, if I can, like, to look back when we published our first pieces of content, which was, I think about a month and a half into the engagement.

**Aida Knežević:** Okay.

**Aida Knežević:** Swift Alternative was ranking pretty highly right away.

**Aida Knežević:** So this isn't, I mean, right now we are in week 13 and we started publishing maybe in week six.

**Aida Knežević:** Okay.

**Aida Knežević:** Well, about six weeks.

**Aida Knežević:** Yep.

**Marc Winitz:** Okay.

**Marc Winitz:** And then last question here, had to do with the rankings.

**Marc Winitz:** Sorry, was looking at this more closely.

**Marc Winitz:** Really, it's about what are we actively, and is there a way to get yourself into those AI overviews based on what you're learning, seeing, understanding?

**Marc Winitz:** Like, are we optimizing to show up into those?

**Marc Winitz:** Is there a way to even do that?

**Marc Winitz:** I've read that there are, but I should know what we're doing.

**Aida Knežević:** Yeah, so that is, that's a great question.

**Aida Knežević:** And a lot of our clients are really interested in it and generally in optimizing for different LLMs.

**Aida Knežević:** So what we can tell you for sure is that just following like basic SEO principles when just structuring content.

**Aida Knežević:** out Thank

**Aida Knežević:** That gets you good rankings.

**Aida Knežević:** So we were able to get into these AI overviews just by following those best practices.

**Aida Knežević:** AI and LLMs, typically, they also favor, based on some research, I think there's a good article by Andreessen Horowitz that kind of goes into how AI, you like content that is easy to read, so digestible, so it uses bullet points, short paragraphs, like, strategically using, like, H2s, H3s, which is something, we already do that.

**Aida Knežević:** So we do have, like, an internal team that's tackling just AI optimization, so we're going to have more info about this, like, in the weeks to come, but this is what we're doing already for, just to optimize for LLMs and SEO.

**Aida Knežević:** I actually have three more questions.

**Marc Winitz:** Sorry, I lied.

**Marc Winitz:** I'm big on one more question.

**Marc Winitz:** First thing is, where it says intent, and then there's an I and a C, what does I and what does C mean?

**Aida Knežević:** Yeah, so intent means search intent.

**Aida Knežević:** So basically, I means informational, and it means that a user that's Googling this query, they want to find an answer to a specific question.

**Aida Knežević:** And then C is commercial, so it means that they want to investigate brands or services.

**Aida Knežević:** A big caveat here is that...

**Aida Knežević:** How do you know that, though?

**Aida Knežević:** Yeah, SEMrush, they do an analysis of the top-ranking content, and they assign this programmatically.

**Aida Knežević:** So usually, if the first page or the search results are mostly how-to guides or informational blog posts, then the search intent is informational.

**Aida Knežević:** It basically boils down to, like, what does this person want to do when they're looking up this query?

**Aida Knežević:** And some queries can have multiple search intents, so, like, they can have both a...

**Aida Knežević:** Commercial and informational search intent, but I find that SEMrush does do a good job of assigning the intent like a human would, and our blog posts, we really want to just rank for informational and commercial keywords, not like navigational or transactional, those are the other two types of search intent, we don't really want to rank for those, because that's useless traffic, basically.

**Aida Knežević:** Sorry, which were the ones?

**Aida Knežević:** Navigational and transactional.

**Marc Winitz:** Okay, what does the KD percentage stand for, and what are the little dot colors mean?

**Aida Knežević:** So keyword difficulty, that just shows you how hard it is to rank for a specific keyword, but this is a number that SEMrush, Ahrefs, and other companies, they come up with this themselves, so this doesn't come from Google or Bing or any other search engine, so this is kind of, it's a number that is....

**Aida Knežević:** It's but we shouldn't take it as gospel.

**Aida Knežević:** Sometimes it's worth targeting more difficult keywords, even if your website isn't as authoritative.

**Aida Knežević:** Yeah, gotcha.

**Marc Winitz:** And then the last question, and this really is the last question, which is volume.

**Marc Winitz:** So, for example, in trends in cross-border payments, it says 50, but then let's say zero.

**Marc Winitz:** Why are they zero?

**Marc Winitz:** And here is it, there just really is, they truly are zero, like there's not enough based on the definition?

**Aida Knežević:** Yeah, so volume is, they estimate how many searches a keyword gets per month, based on historical data for the last 12 months.

**Aida Knežević:** From what I've seen, just like working with clients, this number is almost always underestimated, because there are a lot more searches, especially if you're talking about like AI and like emerging trends.

**Aida Knežević:** There's all, because, they...

**Aida Knežević:** Don't have enough historical data to go off of.

**Aida Knežević:** And one important thing to note that this data is based on the UK.

**Aida Knežević:** So we are tracking UK search data.

**Aida Knežević:** So this is like a smaller, like a smaller set of data.

**Aida Knežević:** Once you factor in like the US searches, the Europe searches, you get a lot more traffic.

**Marc Winitz:** And would we be potentially presenting ourselves in those searches too?

**Marc Winitz:** Yes.

**Marc Winitz:** Yes.

**Aida Knežević:** Yeah.

**Aida Knežević:** we're using the UK as our.

**Mark Stiltner:** Ah, okay.

**Mark Stiltner:** That's important to understand that.

**Mark Stiltner:** Okay.

**Marc Winitz:** Okay, cool.

**Marc Winitz:** Got it.

**Marc Winitz:** Okay.

**Marc Winitz:** Sorry for all the questions.

**Marc Winitz:** Thank you.

**Mark Stiltner:** No problem.

**Mark Stiltner:** I'm happy.

**Mark Stiltner:** Actually, right.

**Aida Knežević:** I'm like a freelance writer for SEMrush and I like have explained these concepts in like many articles.

**Aida Knežević:** So it's not a difficult thing to answer at all.

**Aida Knežević:** Oh, wow.

**Aida Knežević:** Yeah.

**Marc Winitz:** Oh, Y'all have to go look at your stuff.

**Marc Winitz:** If there's stuff I think is worth getting smart on, send it over.

**Marc Winitz:** I'd love to see.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah, for sure.

**Aida Knežević:** They have.

**Aida Knežević:** We could really have a lot of good blogs on like different SEO topics, but yeah, so that's the position tracking report.

**Aida Knežević:** I did have, I was going to ask, will you send us that Amdreason Horvitz article?

**Mark Stiltner:** Yes, I will.

**Mark Stiltner:** Thanks.

**Aida Knežević:** And then one other thing is we should align on like the clusters that we want to cover for future content.

**Aida Knežević:** I already kind of, I messaged you about this in this channel, but basically when we first started working together, you picked three content clusters that you wanted to prioritize.

**Aida Knežević:** Those were payment processing, niche like payments, and cross-border payments.

**Aida Knežević:** And those clusters are kind of not empty, but they are kind of like, we do need to replenish them if we, if you want to continue prioritizing those.

**Aida Knežević:** We're empty.

**Aida Knežević:** When look the stack and give

**Aida Knežević:** The clusters.

**Mark Stiltner:** We're emptying them.

**Mark Stiltner:** They're empty yet, but they're getting there.

**Aida Knežević:** Okay, good.

**Aida Knežević:** So we are kind of like, we should, if you want to continue focusing on those clusters, we do have to do like additional content research for those.

**Aida Knežević:** But there are other, there are like three other clusters that we haven't really touched at all.

**Aida Knežević:** So if you want, you can take a look and see if those are worthwhile.

**Aida Knežević:** We seem to be doing really well in the ones that we have prioritized so far.

**Aida Knežević:** So if you want to continue, like, down that road, we can, but just to flag that.

**Mark Stiltner:** So, hmm, I mean, Marc, I think this almost merits like a higher level strategic discussion of what we want to point them at next.

**Mark Stiltner:** Yeah.

**Marc Winitz:** Yeah, for sure.

**Marc Winitz:** I feel like maybe you and I should maybe sink, and then I know we're talking later, and then kind of come back.

**Marc Winitz:** But sorry, just remind me, what were the three buckets together?

**Marc Winitz:** Yeah, let me just share my screen really quickly.

**Aida Knežević:** Okay.

**Aida Knežević:** So, cross-border payments, that's one.

**Aida Knežević:** Then payment infrastructure, that was the second one.

**Aida Knežević:** And high-risk and niche industry payments, that was the third one.

**Aida Knežević:** So we have, like, these three are all, like, we haven't done any content in these three.

**Aida Knežević:** Got it.

**Aida Knežević:** Okay.

**Marc Winitz:** Okay.

**Marc Winitz:** So we're basically at a point where we're, like, kind of saturated this first three pretty well?

**Marc Winitz:** Sort of, is that fair?

**Marc Winitz:** Yeah.

**Aida Knežević:** Yeah, I mean, we've covered, like, the most, like, obvious, probably, contenders in all three.

**Aida Knežević:** So, but there is, like, always just, like, room to expand.

**Aida Knežević:** So it's not, like, we just, we have to move on.

**Aida Knežević:** We don't have to, like, if you feel, like, there are other things, you still want to, like, focus on these clusters.

**Aida Knežević:** So, sorry.

**Marc Winitz:** So, like, that would.

**Marc Winitz:** I mean, like maybe looking at another list of things we haven't yet addressed and seeing if it's worth doing.

**Marc Winitz:** Yeah.

**Marc Winitz:** Well, okay, maybe you can advise us here, like, what makes more sense?

**Marc Winitz:** Is it better to go deeper on these three or is it better to start expanding?

**Aida Knežević:** One thing I really want to do is we can look at the content that's done really well so far and see if there are any sort of long tail keywords or just like additional angles that we can create content around just to build more authority on that subject.

**Aida Knežević:** Obviously, those blogs would have to be like aligned with what like your business priorities and things like that.

**Aida Knežević:** And also like avoid mentioning like high opportunity industries like gambling and stuff like that.

**Aida Knežević:** So we do have to like optimize there, but I do think that there's a lot of value and just like doubling down on what's already working and we can because we're publishing.

**Aida Knežević:** At a high velocity, we can also like set aside some time to just like expand into other clusters if you want to.

**Mark Stiltner:** Marc, I know one cluster that's came up in a couple of conversations recently that I would love to blow up, which is all around referral partnerships.

**Mark Stiltner:** So I've heard from Kristen Lee twice now, we have a bunch of referral partners that sign up that just don't know how to sell Rapyd.

**Mark Stiltner:** And we're continually pushing for referral partners in the U.S.

**Mark Stiltner:** and in other regions.

**Mark Stiltner:** I could see articles around how to get started referring business to payment companies, what to do once you're a referral partner, how to become a referral partner, you know, even things into like how to help them successfully onboard merchants and that kind of thing.

**Mark Stiltner:** I think there's a lot of depth that we could go into there.

**Marc Winitz:** It was interesting.

**Marc Winitz:** Actually, you might really be on something and maybe there's some research that Mikael could help.

**Marc Winitz:** video.

**Marc Winitz:** Thank

**Marc Winitz:** So, you know, I used to, before we did the HubSpot cutover, I used to get every single lead that was generated as a contact test form for a partner.

**Marc Winitz:** And it's interesting, like, how they come in and, like, what they say.

**Marc Winitz:** And maybe there's, like, it's also not just referral partners.

**Marc Winitz:** That's also, like, ISO paybacks.

**Marc Winitz:** And it's also, like, how they view themselves.

**Marc Winitz:** So maybe there's something there you could look at.

**Marc Winitz:** But that would be, all those things you said are interesting, I guess, like, maybe this doesn't matter.

**Marc Winitz:** I guess the question is, from an SEO perspective, is that good?

**Marc Winitz:** I could see it being useful on the blog, like, is to help people work with us.

**Marc Winitz:** I guess the question is, people searching for that type of thing?

**Marc Winitz:** Maybe we try and see.

**Mark Stiltner:** I don't know.

**Mark Stiltner:** Maybe it's just an experiment, and that's right.

**Aida Knežević:** Yeah.

**Aida Knežević:** I mean, because there's a lot of just, like, discussions recently about how SEO is going to evolve, considering a lot of people are using LLMs to search.

**Aida Knežević:** search.

**Aida Knežević:** there's a you.

**Aida Knežević:** I think, and I would like to hear Jacob's input, he has a conflicting meeting today, so he wasn't able to join, but I would love to hear Jacob's input on this, I believe that there's a lot of value in creating that type of really specialized content, even if it doesn't have an obvious keyword to target, just because this is the stuff that people will go to ChatGPT or Perplexity and ask, like that's sort of what I would, so I do feel like there's, some value in like just trying to like target a couple of those, like doing a couple of those articles, even if there is no like perceived search volume, but there could be, I have to like do some digging into that.

**Marc Winitz:** Listen, that's a great observation, that's kind of like we're looking for you to help us figure that out.

**Marc Winitz:** Yeah.

**Marc Winitz:** Yeah, maybe you could follow up with Jacob and see who it is.

**Aida Knežević:** Yeah, yeah.

**Mark Stiltner:** So, let's do that, and the other thing that we can do to help out is really develop, I think, you

**Mark Stiltner:** As you're looking at this, for us to go in and say, like, here's what this audience looks like, here's what they care about, here's how this relates to it, and give you, like, a good, solid understanding of the audience could maybe help you to go find those keywords that maybe don't even necessarily relate, obviously, to payments, but are bringing in the right people.

**Mark Stiltner:** Yeah, yeah, definitely, we can do that.

**Aida Knežević:** Rachel has experience, I mean, she's already done pieces for another client that is, it was, like, super, super tailored to, like, it was something related to, like, employment taxes, or dentist, dental offices, so, and those did really, really well, so, we've already, like, done that type of stuff for other clients.

**Aida Knežević:** Is it, like, a payroll company or something?

**Aida Knežević:** It's a dental staffing app.

**Aida Knežević:** Okay.

**Aida Knežević:** For dental hygienists, specifically.

**Aida Knežević:** Long time?

**Mark Stiltner:** No.

**Mark Stiltner:** Yeah, yeah.

**Aida Knežević:** Interesting.

**Aida Knežević:** Okay.

**Aida Knežević:** Yeah.

**Aida Knežević:** Cool.

**Aida Knežević:** All right.

**Aida Knežević:** Great.

**Aida Knežević:** Mark, do you have any other question, comment?

**Mark Stiltner:** Yeah, actually, Big Mark, do you have anything before I go into a couple of specifics?

**Marc Winitz:** I usually don't get referred to as Big Mark.

**Marc Winitz:** I don't have any other questions.

**Marc Winitz:** This has been super useful.

**Marc Winitz:** Other than, did we get the time schedule then?

**Marc Winitz:** Sorry, with the Microsoft next week or no?

**Aida Knežević:** I think Mark said...

**Aida Knežević:** I'll respond back to his Slack.

**Mark Stiltner:** think it's going to be June 16th.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** Okay, cool.

**Marc Winitz:** I'm going to drop it now.

**Marc Winitz:** Thanks, you guys.

**Marc Winitz:** Appreciate it.

**Marc Winitz:** Thanks.

**Mark Stiltner:** All right, quickly.

**Mark Stiltner:** I know we're already at time, so I will make this very quick.

**Mark Stiltner:** I have a little list of things here that I need to just run by you guys.

**Mark Stiltner:** So, you had asked for, you know, maybe aggregating some errors.

**Mark Stiltner:** These are the ones that I've seen coming up.

**Mark Stiltner:** I will share this document with you, Rachel.

**Mark Stiltner:** you.

**Mark Stiltner:** you later.

**Mark Stiltner:** see later.

**Mark Stiltner:** I'll see you later.

**Mark Stiltner:** You

**Mark Stiltner:** And I will update this each week.

**Mark Stiltner:** Rachel, you'd be the right one to share this with, right?

**Mark Stiltner:** Or should I share with both of you still?

**Mark Stiltner:** Because Aida, you're changing your...

**Aida Knežević:** Yeah, yeah.

**Mark Stiltner:** So some of these might be able to be addressable by the LLM.

**Mark Stiltner:** Some of these may just be things to keep in mind as we're editing.

**Mark Stiltner:** And they're just the things that I've seen come up recently.

**Mark Stiltner:** So we keep talking about smart payment routing.

**Mark Stiltner:** This is one that we don't actually offer.

**Mark Stiltner:** This has come up because we've had some case studies and some things we've talked about with payment orchestrators who use Rapyd.

**Mark Stiltner:** If you're a payment orchestrator, you aggregate a bunch of companies like Rapyd and sell it as a bundle to a merchant so that they're always going to the one who has the best approval rates.

**Mark Stiltner:** That's awesome.

**Mark Stiltner:** We love being part of that.

**Mark Stiltner:** It's this business, but we don't want to promote it to somebody who comes to us looking for a solution.

**Mark Stiltner:** don't want to say, hey, don't come to us.

**Mark Stiltner:** Go to this other company that tells us as a third party with others.

**Mark Stiltner:** And I started noticing in the article sometimes it's even saying that Rapyd offers smart payment routing.

**Mark Stiltner:** We don't.

**Mark Stiltner:** It's not a capability that we have.

**Mark Stiltner:** So watch out for that.

**Aida Knežević:** Remove it.

**Mark Stiltner:** Now.

**Mark Stiltner:** There exceptions to this.

**Mark Stiltner:** Actually, I'm proofing an article right now where there will be an exception where if you're in an article that's like, hey, how do I improve my authorization rate?

**Mark Stiltner:** We might want to say include multiple acquirers through an orchestrator because maybe there's somebody who already has an acquirer and we want them to add it up.

**Mark Stiltner:** So there's exceptions to every rule, but for the most part, let's remove these when we see it.

**Mark Stiltner:** I'm still seeing this one country or 100.

**Mark Stiltner:** Anytime you see that, just change it to one country or worldwide or just change it to worldwide.

**Mark Stiltner:** Lower processing fees.

**Mark Stiltner:** This one continues to come up.

**Mark Stiltner:** I don't know if you're going to be able to get it out of the LLM.

**Mark Stiltner:** Whenever you see anything talking about fees, just delete it.

**Mark Stiltner:** We don't, our whole model is like, we're not going to be the cheapest, but we're going to be the best.

**Mark Stiltner:** And so we don't compete on fees.

**Mark Stiltner:** We're rarely going to win on fees.

**Mark Stiltner:** So lose that.

**Mark Stiltner:** And then the other thing is actually something I would like you to pass along to your tech team.

**Mark Stiltner:** This is one thing that we just saw in the.

**Mark Stiltner:** XML file, we need to add the topic as plain text, so whatever the topic of the blog is, which should match our content bucket, needs to be added in plain text between these tags.

**Mark Stiltner:** So this one right here is just one you could maybe pass along to your guy, and then I'm going to tell Tom about this one right here for me.

**Mark Stiltner:** Yeah, so that's just my list for today.

**Mark Stiltner:** Oh, one other thing actually that's come up.

**Mark Stiltner:** This is important for the XML.

**Mark Stiltner:** We're using the wrong URL.

**Mark Stiltner:** So for blogs, we actually track a contact URL that is slash contact slash blog.

**Mark Stiltner:** That's so that it's really easy for us to know anybody who fills out a form that comes from the blog, and right now it's filling in that hyperlink is just slash contact.

**Mark Stiltner:** Which we don't want.

**Mark Stiltner:** So if we can keep an eye on that.

**Aida Knežević:** Okay.

**Aida Knežević:** It's not going to like, it's not going to go to like a.

**Aida Knežević:** Like a 404 page, it's not going to air?

**Mark Stiltner:** No, slash blog is, it's the exact same form, exact same page actually as our contact sales form, which is just slash contact.

**Mark Stiltner:** It's just, we just made a separate one for the blog so that it's easy for us to know everybody who comes through from the blog.

**Mark Stiltner:** Okay, that's perfect.

**Aida Knežević:** That's not a big deal at all.

**Aida Knežević:** Just add blog at the end of the URL.

**Aida Knežević:** Okay, exactly.

**Aida Knežević:** So that's my list of things.

**Mark Stiltner:** I mean, none of this is big stuff.

**Mark Stiltner:** It's all fine tuning, so.

**Mark Stiltner:** Okay, great.

**Aida Knežević:** Well, yeah, thank you so much for your time.

**Aida Knežević:** I'll send over the link to that article in Slack.

**Aida Knežević:** And yeah, well, hope you have a great meeting with Marcel next week.

**Aida Knežević:** Let us know how it goes.

**Aida Knežević:** And yeah, we'll be in touch.

**Aida Knežević:** All right, thanks very much.

**Aida Knežević:** Bye.

**Aida Knežević:** Bye.
