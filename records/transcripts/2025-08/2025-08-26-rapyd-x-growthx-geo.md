# Rapyd x GrowthX: GEO

<metadata>
date: 2025-08-26
time: 15:30 UTC
duration: 32 minutes
organizer: vivek@growthxlabs.com
participants: Mara Leighton, Vivek Shankar, Mark Stiltner, Nicolette Mychajluk
fathom_recording_id: 82972600
fathom_url: https://fathom.video/calls/389893136
share_url: https://fathom.video/share/i6VzJ7u-Dj7f6xLW_V4-7zy-MypYSFsv
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX and Rapyd aligned on a content strategy for AI-powered search (GEO/AEO), focusing on high-intent product evaluation queries where users turn to LLMs like ChatGPT instead of Google. The team discussed monitoring ~200 targeted prompts using GA4 and Scrunch, emphasized that SEO remains foundational to LLM visibility, and identified three content repurposing opportunities: flagging blog content suitable for Reddit and community forums, converting articles to videos/podcasts using Notebook LM, and creating comparison content. Mark tasked the team with flagging Reddit candidates in Airtable, investigating GrowthX's Reddit capability, and adding Ari (Rapyd's social media lead) to relevant channels.

---

## Context

Rapyd is a fintech payment platform that recently engaged GrowthX for content strategy work. Mark Stiltner (Rapyd's web manager) is focused on increasing organic visibility and preventing competitive disadvantage — specifically, he wants to stay ahead of industry trends and ensure Rapyd's content strategy is at parity with what peers are doing. This meeting was called to deep-dive on GEO/AEO strategy after an initial conversation Mark had with Mara the previous week about content strategy for the next few months. The broader context is that traditional SEO traffic is shifting: users increasingly go to LLMs (ChatGPT, Claude, etc.) instead of Google for product research, so Rapyd needs a dual strategy of maintaining strong SEO fundamentals while also optimizing for LLM referrals.

---

## Relevance

**To GrowthX Delivery:**
- GEO/AEO strategy requires monitoring specific high-intent prompts (~200 for Rapyd) using Scrunch and GA4, establishing a replicable monitoring pattern for other fintech clients
- Content must balance SEO fundamentals with LLM-friendly formatting: clear structure, practical tactics, and comparison content perform best
- Content repurposing (blog → Reddit, blog → video/podcast via Notebook LM, blog → infographics) expands surface area without proportional content creation overhead

**To CheckThat:**
- Prompt monitoring at scale (200 targeted product-evaluation prompts) demonstrates real-world AEO validation opportunities for CheckThat's AI visibility index
- Fintech companies are actively managing LLM referral sources, validating the business case for AI-powered search visibility tooling

**To GrowthX Business Development:**
- Rapyd is actively investing in content strategy (multiple vendors, internal tools like Octopost for sales enablement, dedicated social media lead Ari), suggesting account expansion opportunities
- Mark's attention to staying competitive on emerging trends (GEO/AEO, Reddit distribution, video repurposing) indicates willingness to invest in new workstreams
- Nicolette is now responsible for driving sales content strategy outcomes, expanding GrowthX's internal champion network at Rapyd

---

## Overview

- GEO/AEO strategy focuses on high-intent searches, monitoring LLM referrals, and tracking \~200 specific prompts
- SEO remains crucial as a foundation for LLM visibility; competitor comparisons and recent content perform well
- Content repurposing (e.g., videos, podcasts) and distribution on platforms like Reddit can expand Rapyd's digital footprint
- Incorporating social proof and customer use cases in content is highly effective for engagement and lead generation

---

## Key Topics

### GEO/AEO Strategy and Monitoring

  - Focus on high-intent product evaluation searches most likely to lead to referrals
  - Using GA4 to track LLM referrals and Scrunch to monitor \~200 specific prompts
  - Visibility in AI Answers is finicky; same prompt can yield different results for different users
  - SEO remains crucial for being the "most popular answer" in probabilistic LLM responses

### Effective Content Types for LLM Visibility

  - Competitor comparisons perform well (e.g., "Rapyd vs. Stripe")
  - Content should be structured for easy LLM crawling, practically useful, clear, and tactical
  - Recent content and presence in community forums (e.g., Reddit) boost LLM visibility
  - High-opportunity industry content works well on Reddit, addressing common pain points

### Content Repurposing and Distribution

  - Explore turning blog posts into videos using tools like Notebook LM
  - Consider creating podcasts from blog content, interlinking between blog, podcast, and video
  - Repurpose content for newsletters, focusing on trends, comparisons, and opinionated pieces
  - Utilize tools like Hunch.tools for creating modular content blocks for various platforms

### Social Media and Sales Team Content

  - Case studies and use cases perform best on social media and generate leads
  - Implement a "case study, use case" alternating pattern for social media posts
  - Leverage Octopost for creating content pillars for the sales team
  - Focus on social proof and pain point content for better sales team engagement

---

## Action Items

**Mara Leighton (GrowthX)**
- Flag content suitable for Reddit/forums in Airtable (starting point for expanding Rapyd's community presence)
- Flag blogs good for Notebook.LM video/podcast conversion in Airtable (priority: trend pieces and comparison content)
- Add Ari (Rapyd's social media lead) to Rapyd Airtable/Slack channels for operational visibility
- Investigate GrowthX Reddit workstream capability and report back on feasibility

**Nicolette Mychajluk (Rapyd)**
- Schedule call with Mara to discuss social media content strategy for Rapyd's sales team (focus: social proof, case studies, pain point content)

---

## Transcript
**Mark Stiltner:** Hey, how are you? I'm doing pretty well.

**Mara Leighton:** It is my last week in Paris, which is nice in a way. I'm excited to get back to New York. How are you doing? Oh, I'm doing pretty good.

**Mark Stiltner:** Cool. Love to hear it.

**Mara Leighton:** Well, I know we're waiting for a couple more folks to join, but I figured today, well, first and foremost, we'd be interested, like, specifically in what would be most helpful for you, Mark, but I figured we could just do, like, kind of a brief chat around how we're thinking about Geo, and then kind of let any questions that you might have naturally pop up.

**Mara Leighton:** We can respond to those and just have it be a little bit more free-flowing.

**Mara Leighton:** Okay.

**Mara Leighton:** That's what I was kind of hoping for.

**Mark Stiltner:** Cool.

**Mara Leighton:** Okay, great.

**Mara Leighton:** Would you prefer we wait for some folks to join or just kind of dive right in?

**Mark Stiltner:** I'm checking with Kristen right now to see if she is going to join. Let me see here and take a look at my calendar to see who is on the meeting. I should wait for Nicolette — I would like her on this. And there she is. Nicolette, you're on. We can probably just go ahead and jump into it. Okay, great.

**Mara Leighton:** Also, I know that this will be an ongoing conversation and we can continue talking about this within our weekly syncs. But it's also helpful to have a concerted conversation around it when needed. Basically, to set the tone for you, Nicolette, so you have visibility: we were chatting with Mark last week about content strategy for the next few months, discussing how search is changing.

**Mara Leighton:** And that includes GEO is kind of what we've been, the acronym that we've been using the most internally, also like AEO or AI answers.

**Mara Leighton:** And that's just essentially, also apologies if I'm over explaining at any point, I just figure if I'm on the other side of this, I would prefer someone to do that versus assume that I know something.

**Mara Leighton:** So essentially, it's just, you know, if you're, if you've noticed your own search behavior changing, instead of going into Google and typing, you know, what is rapid, instead going to an LLM and asking, you know, what is the best tool for XYZ use case?

**Mara Leighton:** Obviously, we're just seeing across clients, and we anticipate seeing more that like, traffic that we're getting by just playing SEO straight, is going to dip a little bit because people are getting some of their information from LLMs.

**Mara Leighton:** And for us, the way that we think about LLMs, and I'll get into like, monitoring a little bit later on.

**Mara Leighton:** What we're really trying to peek into is the high intent searches.

**Mara Leighton:** So the ones that are less like educational, informational, because those are less likely to get someone actually onto your site or to make the decision to work with Rapyd.

**Mara Leighton:** But instead, it's a little bit more long tail and specific.

**Mara Leighton:** So it'd be more about like, what is the persona we're thinking of?

**Mara Leighton:** Who's the audience?

**Mara Leighton:** And then what their specific use case is?

**Mara Leighton:** What problems do they have?

**Mara Leighton:** Pain points, objections, things that they might actually go to an LLM search and then make a some type of purchase decision or something that might be a little bit further in that funnel.

**Mara Leighton:** That's an initial monologue.

**Mara Leighton:** But are there any questions that either of you have that might help, like, direct us in one direction or the other or anything that might be most useful to discuss?

**Mark Stiltner:** So one thing that I do want to cover is surface area.

**Mark Stiltner:** We've talked about that before.

**Mark Stiltner:** It would get out way.

**Mark Stiltner:** Ability to generate blog posts as we can.

**Mark Stiltner:** I'm always telling you about like, oh, we can't talk about this or, you know, like we need to talk about this a certain way.

**Mark Stiltner:** One of the things I was wondering is like, you know, or one of the strategies that I'm seeing people do is actually starting to like build out their own syndicated websites.

**Mark Stiltner:** So in other words, instead of like just having like the rapid.net blog, like they have another almost like influencer blog just like built on the same topic that maybe like promotes their products and services, but is a separate URL like dedicated totally to like one topic.

**Mark Stiltner:** Maybe that topic is just how gaming companies can accept payments or whatever.

**Mark Stiltner:** I'm wondering if you're seeing any of that, if you've tried any of that with other companies, if there's other strategies for, you know, increasing that surface area of search online that we could be pursuing as well as the best practices for just what everybody's kind of calling GEO and what we're seeing with those.

**Mark Stiltner:** basically, like, know it's still a little bit up in the air.

**Mark Stiltner:** What I don't want to have happen is that, like, the CMO comes to me and says, hey, I just went to this conference, and then they say all the other web managers are doing this thing, and you haven't done that thing yet.

**Mark Stiltner:** I want to know what that thing is and be doing it.

**Mark Stiltner:** For sure.

**Mara Leighton:** Well, okay.

**Mara Leighton:** So let me answer it maybe from back to front.

**Mara Leighton:** Vivek, if you have any specific experience on the syndication side, would also be interested in your thoughts on surface area.

**Mara Leighton:** But just to pick up on trends or what we should be doing, the top level is that we are doing as much as we can in good faith.

**Mara Leighton:** And the industry standard currently is a little bit of a black box.

**Mara Leighton:** So what we're doing is monitoring.

**Mara Leighton:** And I could spend, you know, a decent amount of time discussing that, but I want to get to the surface area portion.

**Mara Leighton:** Basically, what we should be doing is monitoring the prompts that we can be and then LLM referrals.

**Mara Leighton:** So LLM referrals, we're already tracking through GA4.

**Mara Leighton:** And then we're using

**Mara Leighton:** We're a tool called Scrunch, where we will be pulling together about 200 prompts that are specifically designed for that high intent product evaluation, most likely to lead to a referral, and then what we'll be doing is we'll be tracking those prompts to tell what Rapids' presence is, what the sentiment is, is it positive, is it negative, and then we'll use that to inform our content strategy.

**Mara Leighton:** The caveat that I'll share, and that I would, I think is important for conversations around, like, what should we be doing, is that right now, visibility into AI Answers, GO, AEO, is really finicky, because sometimes the same prompt will return an entirely different answer, depending on the user.

**Mara Leighton:** There's also no equivalent to SEO, where you can tell, like, the specific search value, or search volume for a particular...

**Mara Leighton:** Instead, it's kind of like there's an infinite number of terms, and we just need to be really concerted about which ones we care the absolute most about showing up in, and then that's the track.

**Mark Stiltner:** It is not linear. People are trying to apply a system of logic that doesn't work. Google, even though it's very complex and interesting, is a linear binary model — you've got a bunch of answers over here, and when your thing matches that answer, you get it. AI is a stochastic probabilities model — it's looking at what's the most likely thing to say next based on what you gave me and what I've been given. That creates an infinite universe of possibilities that even the AI companies can't tell you what it's going to say.

**Mara Leighton:** Exactly, and I'm so glad to hear that because that's honestly the thing that's hardest to communicate in these conversations — we can't treat it like SEO. But just on how we think about it, SEO is still really important because when we're thinking about probability, what the most popular answer is, being at the top of the fold and being the most popular recommendation is still really important.

**Mark Stiltner:** So that's still a fundamental building block.

**Mara Leighton:** Right. So when we're thinking about content strategy, it needs to be the SEO part — making sure we're highly visible and a popular recommendation — and then also satisfying the formatting needs for an AI answer. Vivek, feel free to jump in.

**Vivek Shankar:** Just to build on, you know, what Mara said regarding tactics.

**Vivek Shankar:** We're, you know, to Mara's point about the SEO, like SEO itself is a huge tactic for LLM visibility, because they seem to be prioritizing that.

**Vivek Shankar:** So in that regard, we are doing everything.

**Vivek Shankar:** thing already, which is just executing good SEO principles, like talk about stuff that, you know, is closely tied to your product, so that Google can figure out what you do, and by extension, the LLMs figure out what you do as well.

**Vivek Shankar:** In terms of specific content types, something that seems to be working well is competitor comparisons.

**Vivek Shankar:** So, for example, Rapid versus Stripe, Rapid versus, you know, Airwalex, etc.

**Vivek Shankar:** That sort of content works very well, but the caveat there is, like, it needs to be, obviously, we don't want to be saying the wrong things, because, you you don't want to be on the wrong end of regulatory concerns or a lawsuit or something.

**Vivek Shankar:** The syndication — starting a new domain and a focused industry magazine — it's been hit or miss so far. I saw one company that had good success with it. I don't know how to pronounce it, but it's spelled K-A-N-D-J-I. So they kind of stumbled upon it. They just wanted to start a place to have conversations with their ICP. Because it's deep in security, SEO content doesn't work well over there — it was very product-driven content. And they found that because they were talking about this stuff, that domain started getting picked up by a lot of the LLMs. LLMs measure how often phrases occur next to each other, so this company's name was coming up a lot next to security terms. They ended up getting picked up.

**Vivek Shankar:** Within the payment processing world, I don't know if that would work because we already have journals like payments and then there's a broader field of your FinTech journals like FinTech Weekly, etc.

**Vivek Shankar:** And then there's the association websites like American Banker Association and so on.

**Vivek Shankar:** There's the EU regulation websites as well.

**Vivek Shankar:** So there's a lot of competition over there.

**Vivek Shankar:** So I'm not necessarily sure that that approach would work in payment ops.

**Vivek Shankar:** And since we don't have much data, it's not something we would feel comfortable recommending at this point, but it's something we're keeping our eye on.

**Vivek Shankar:** So that's just something I wanted to add on tactics.

**Mara Leighton:** Another thing is that the general wisdom is that LLMs are giving more priority to recency, which is part of the refresh strategy. Through community forums — showing up in listicles by other publications is super important. But also just showing up where your users are and being part of those conversations, particularly on Reddit or other community forums, tends to be really useful as well. We're still figuring out how to optimize that and turn it into a strategy. Some clients have posted directly to Reddit and found that it occasionally bumps up their LLM presence, but it's not really tried and true yet. So that's one other element to consider — showing up in community forums.

**Nicolette Mychajluk:** So for the competitor comparisons, is it coming up more in LLMs because now you have two names associated? Like, if we didn't do just a Rapyd versus competitor piece, but instead created something like "platforms that accomplish XYZ outcome" — platforms that help you sell into Latin America, for example — is that why it's helping? Because you have two names associated with the same product feature? Can we create more stuff that includes our competitors without necessarily trashing them?

**Vivek Shankar:** It's more tied to how people search. Someone might say, "I'm expanding into Latin America, which payment provider should I work with?" Our existing content should take care of queries like that, but it's still a good idea from a conversion standpoint to have direct competitor comparisons, since people do search for things like "Rapyd versus Stripe."

**Mara Leighton:** One conceptual piece that applies to the other content we're producing is that those pieces work really well because they're structured so easily for an LLM to crawl. They can take that information and if it's the average kind of aggregate, which it should be, it's easy to spit that back. Also, they tend to be really practically useful, clear, and tactical, which all tend to work really well.

**Mark Stiltner:** All right, I've got a thought. So I was just wondering actually, if we're seeing things on Reddit and forums work, could we just say that some of the content we're going to write is for the blog and some other content we're actually going to write for Reddit, with a different tone and thought leadership focus?

**Mara Leighton:** I know there are conversations happening internally around that. I don't want to speak out of turn, but as a workstream it's not something we currently offer. Let me figure out what that would look like and we can keep the conversation going. But at minimum, what we could do is help figure out which content would perform best on Reddit — we could flag pieces that would be a really good one to repurpose. Whether we do that or Rapyd does that, that's something we could absolutely do, and it would look the same as what we're talking about with the comparison pieces.

**Mark Stiltner:** Yeah, I think at the bare minimum, that would be a good place to start. Just flag a couple of things, maybe even add a content bucket where it's like, this is good stuff for Reddit. Let's put a couple out there and just see what happens.

**Vivek Shankar:** The current content pillar that we have, which is on high opportunity industries, I think all of that will do it really well on Reddit.

**Vivek Shankar:** Because if you go on Reddit, if you check like e-commerce or even our entrepreneur or any of these subreddits, all of them are talking about how Stripe suspended their accounts, Shopify held back their payments, you know, they're growing and they can't like whatever, accept payments all of a sudden, there's lots of complaints about PayPal.

**Vivek Shankar:** So instead of copy-pasting articles or repurposing at a thought leadership level, even just having a presence there and giving information would be super helpful. That's great input.

**Mara Leighton:** We can also share best practices. I think the clients who've seen the most success post from the company account — LLMs prefer it because it's so heavy on authenticity. The content that will do best has to be really useful and neutral. If it's posted from the company account versus even in comments, it'll perform better. We can share basic guidelines of do's and don'ts for Reddit. Any other questions that are top of mind?

**Mark Stiltner:** Let me look at my schema — I've got that with my developers now. The schema thing is just a technical optimization point. I'll probably have you look at it again once we update it. I don't think there's really anything else beyond what we talked about. I think we're really just looking at how we can take what we're doing with you guys and spread it out a little bit. Flagging articles for Reddit and other forums is a good idea. If you come across other forums like Medium or things in the payment world that would work, that would be useful. I'm also curious if you have any experience with other clients taking the blogs we're doing and turning them into podcasts, infographics, or eBooks. Are you seeing best practices or suggestions for what we could do?

**Mark Stiltner:** Nicolette, you're going to say something, too.

**Mark Stiltner:** Yeah, I'm helping Ari.

**Nicolette Mychajluk:** She's, we have someone who leads our social strategy, and she's working with Octopost to create more content pillars for our sales team and any, like, customer-facing role to post.

**Nicolette Mychajluk:** And we were just discussing, like, what do we have outside of blogs?

**Nicolette Mychajluk:** Like, blogs are helpful.

**Nicolette Mychajluk:** Like, she's like, do we have enough for certain reps and certain geos to post about Latin American stuff?

**Nicolette Mychajluk:** So maybe potentially having some infographics about, like, geos-specific stuff or product stuff would be super helpful as well.

**Nicolette Mychajluk:** Yeah, so.

**Mara Leighton:** I, Vivek, is there?

**Mara Leighton:** Oh, love that you raised your hand.

**Mara Leighton:** I was going to say, and not to, like, sign you for this, but if there's content that we think in particular would be good to be filtered into an infographic, maybe we can also just, like, flag that as well.

**Mara Leighton:** well.

**Mara Leighton:** That should be relatively easy.

**Mara Leighton:** Vivek, feel free to check out if there's something else.

**Vivek Shankar:** Yeah, I'd actually think more in terms of video.

**Vivek Shankar:** We have clients who are taking existing blogs, and this depends on their audience, right?

**Vivek Shankar:** They're taking existing blogs, like pushing them through Notebook LM, and then they also have a podcast, and what we're doing is we're kind of interlinking between the three of those.

**Vivek Shankar:** So the podcast gets highlighted in the blog, the blog gets turned into a Notebook LM video, which kind of spits out this podcast kind of video.

**Vivek Shankar:** It has a background, has a narration, et cetera.

**Vivek Shankar:** I've seen the podcast in Notebook, I haven't seen videos.

**Vivek Shankar:** It generates like some sort of a static background, so you can actually put it into a video editor and have like image stills in there.

**Mark Stiltner:** So it's still that podcast format, but with a static background.

**Vivek Shankar:** Yeah, it's a podcast and editor, and then you can release an audio version if you want.

**Vivek Shankar:** They're not doing

**Vivek Shankar:** They have still images in the background. The really fancy ones generate actual people, but it changes every five seconds, which isn't practical. No one has cracked that yet.

**Mara Leighton:** Yeah, there's no good video version yet in those cases.

**Vivek Shankar:** For Rapyd, I think a lot of the articles around trends that we've done so far do pretty well on SEO. I think they'd be a hit on YouTube as well, and your sales team can definitely use that. Since we're doing Stablecoin and LATAM topics, especially the country guides that we'll be creating, repurposing those into video is great. There's a really nice tool called Hunch (hunch.tools). It's kind of like Aerobs but far more modular. You just create blocks, enter your blog article, tell it what task you want done, and it chooses the right model and spits out output. You can generate pretty good four or five minute videos from this. It expands your footprint because you can upload to YouTube, chop it up for Twitter video or even TikTok, since a lot of merchants hang out there. So trends and high-level articles would work quite well — not just "what is a payment gateway," but more "here's the truth about what people are using it for" and trends in the space.

**Mara Leighton:** Anything with an opinion or comparisons and a lot of useful info that isn't just informational is a good way of thinking about whether it will work. The last thing I'd mention is newsletters — another popular repurposing channel. It depends on whether you already have one and how interested you are in maintaining it.

**Mark Stiltner:** Yeah, we're definitely doing that.

**Mark Stiltner:** I'm working on a newsletter project right now myself. I might pull you guys in on it once I get it further along. Essentially, I'm building an automated newsletter that pulls from a swipe file of third-party content — aggregating relevant content every day, pulling from the swipe file, putting it into a template, rewriting in our voice, and having AI generate a fresh newsletter for us. I'm starting with once a week and then moving it to daily. Once it's automated, it should be a good process. And then we can start pulling some of our own content into it as well.

**Mara Leighton:** A newsletter is also a great place to put social proof — case studies and customer use cases.

**Mark Stiltner:** Yeah, that's good for the newsletter, but also for the stuff we're doing with Ari. Just take all the case studies we generated and put them in there. At my last company at Verbatim, we used a formula that worked really well on socials: every month or two, alternating case study, use case, case study, use case. That's what performed best and led to the most leads.

**Mara Leighton:** I can DM her about that social media strategy discussion. If Nicolette wants to chat about it, we're happy to.

**Mark Stiltner:** So here's what I got, like what I wrote down for takeaways, for next steps.

**Mark Stiltner:** In terms of things we could start doing, we should flag content for Reddit and other forums, so we can start generating requests for content to put in there. We should also flag blogs that would be good candidates to push through Notebook LM to make into video or audio podcasts. A lot of these will be trends, articles, and comparisons — things with opinion.

**Mark Stiltner:** For the country guides, I think there's a couple of things we could do. Let's really blow those out — we should do a country guide for every country we're targeting. Then we can have those be individual blog posts, individual videos and podcasts. And we can aggregate those together into regional gated e-books as well. Then more comparison blogs that we can use on Reddit and in other places. Those are the actionable things I took away from this call. What do we need to do to make sure those things happen?

**Mara Leighton:** Great question.

**Mara Leighton:** Well, my question for you would be: who will be the person actioning the Notebook LM aspect and the Reddit aspect, if it stays within Rapyd? That way we can determine if we should be signaling that in a tab in Airtable or putting it in Slack.

**Mark Stiltner:** Put it in Airtable, but we're going to need to add Ari — not as a paid editor, just as somebody who can see it. Ari is our social media person and she's the one who will action the stuff into Reddit and post to social media. Can you make sure that she is added everywhere, both in Airtable and in our Slack? I'll put her contact information in the chat. We just call her Ari, but it's Ariana.

**Mara Leighton:** That's the main piece in terms of actioning. Thank you for compiling the notes — we'll share a recap as well. For me, I'll see how far we are in developing the Reddit workstream and whether that's a capability we might be able to offer. I just sent an invite to Ari for the Rapyd channel.

**Nicolette Mychajluk:** Sorry, my internet made me leave the call. I just came back.

**Mara Leighton:** We figured. The only thing you missed, Nicolette, was if you ever want to chat about socials, we'd be happy to. I used to work on it more in depth at Verbatim, my last position.

**Nicolette Mychajluk:** think, yeah, the sales team is like, we really just invested a lot of money into this Octopost thing.

**Nicolette Mychajluk:** So now it's like, she's kind of on the hook for it.

**Nicolette Mychajluk:** And she's, she's leaning on me to figure out what kind of content we can use.

**Nicolette Mychajluk:** And I'm like, oh, I don't think, I don't think we could just keep sending people links to blogs all the time.

**Nicolette Mychajluk:** That's not so fun as a consumer standpoint.

**Mara Leighton:** That's the main issue. It's a tough one to solve, but I did this for a lot of clients at Verbatim and we had a relatively good formula. I'm happy to chat whenever you guys want — this week or next. I'll follow up with her.

**Nicolette Mychajluk:** That's so exciting. That makes me feel better.

**Mara Leighton:** Honestly, the main point is what works best is social proof — customers sharing what they loved or their experience. If you do a 15-minute interview, you can pull three different quotes from it and recycle that on a routine basis. And then pain point content, because when someone reads it, they're like "oh, this is something I've dealt with" and they reach out. That's better for sales.

**Nicolette Mychajluk:** I'll follow up with you to find some time.

**Mara Leighton:** This will be an ongoing conversation, so we can keep talking about it. We have action items and we'll share a recap of this conversation. If you guys have any questions, feel free to ask async, and we're always available to hop on a call. I just confirmed that I shared an invite with Ari. Thanks so much, everyone. Nice to see you.

**Mark Stiltner:** Bye.
