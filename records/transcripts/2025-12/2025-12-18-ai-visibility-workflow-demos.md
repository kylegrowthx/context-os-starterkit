# AI Visibility + Workflow Demos

<metadata>
date: 2025-12-18
time: 21:03 UTC
duration: 60 minutes
organizer: george@growthx.ai
participants: Marcel Santilli, George Haikal, Jon Kowieski, Arudyak
fathom_recording_id: 109916877
fathom_url: https://fathom.video/calls/510348564
share_url: https://fathom.video/share/im2qm1b3KYx8g9yc2Sfxt1MxTwbBGRj8
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX demonstrated their new AI visibility platform and conducted a product feedback session with Brex's Jon Kowieski and Arudyak. The platform provides a standardized index of 100k+ B2B evaluation prompts across 1.5k categories, addressing critical gaps in AI citation tracking for platforms like ChatGPT, Gemini, and AI Overviews. Brex will receive early access to the "Check That" tool to validate core needs around platform-specific tracking, citation pattern analysis, and hallucinated URL detection, with potential expansion to GrowthX's integrated "OS" platform as a lighthouse customer.

---

## Context

Brex is a leading financial technology company providing expense management, payment processing, and cash flow solutions to mid-market and enterprise businesses. This call brought together Jon Kowieski (representing Brex's AI visibility strategy) and Arudyak (product/operations) from Brex with Marcel Santilli and George Haikal from GrowthX to evaluate GrowthX's new AI visibility research platform and discuss strategic alignment around platform-specific tracking and citation analysis.

The meeting was driven by Brex's urgent need to understand how AI engines cite their brand and content across different platforms. Jon outlined specific requirements: tracking disparate growth rates between ChatGPT (10%), Gemini (30%), and AI Overviews; identifying hallucinated URLs in AI-generated citations that cause 404 errors; and benchmarking citation share against competitors like Profound. GrowthX positioned their new shared-library approach (funded by a freemium model) as a differentiated alternative to expensive, API-less competitor tools.

---

## Relevance

**To GrowthX Business Development:**
- Brex is a qualified lighthouse customer for the "OS" platform — requires custom prompt tracking, hallucinated URL detection, and matrix-view competitive benchmarking.
- Jon indicated existing customer churn from Profound, positioning GrowthX as a replacement with better tooling and lower cost.
- Expansion pathway: free "Check That" access early → feedback integration → paid "OS" tier within Q1 2026.
- Strategic value: Brex's scale (Series A+ companies, Y Combinator network) offers distribution and reference potential for the 100k+ prompt library.

**To CheckThat / AI Visibility Product:**
- Top prioritized features per Jon's feedback: 7-day trailing average smoothing, top-50 citations view, hallucinated URL detection, platform-specific filters (ChatGPT vs. Gemini vs. AI Overviews).
- Citation pattern discovery validated: Brex confirmed that specific copy changes ("10x-20x" → "20x-30x") are reflected in AI citations within hours, proving content influence measurement is viable.
- Competitive benchmarking (matrix view) is a must-have for C-suite reporting at Brex.
- Gem: Brex uses domain rating (DR) as a spam filter signal — may inform CheckThat's training data quality.

**To GrowthX Delivery & Product Strategy:**
- Productized workflows resonated strongly: Jon expressed interest in simple web apps (receipt classifier, sales projection, RFP generator) that abstract product logic and capture lead data.
- Content strategy insight: Create content solving user problems ("How to negotiate better pricing with HubSpot") over product features ("Brex ROI").
- Early access roadmap: Grant Jon access next week, collect feedback, prioritize engineering tickets, offer "OS" preview in January 2026.

---

## Overview

- **New AI Visibility Model:** A shared library of 100k+ prompts across 1.5k B2B categories provides a free, standardized index for tracking, replacing the need for each brand to build research from scratch.
- **Brex's Core Needs:** Platform-specific tracking (ChatGPT, Gemini, AI Overviews), citation pattern analysis, and a tool to detect hallucinated URLs in AI citations.
- **Integrated "OS" Platform:** A private "OS" platform is being built to close the loop between AI visibility, content execution, and performance analytics, with Brex as a potential lighthouse customer.
- **Pilot Program:** Brex will receive free, unlimited access to the public "Check That" tool to provide feedback, with the goal of becoming a lighthouse customer for the full "OS" platform.

---

## Key Topics

### Brex's AI Visibility Needs

  - **Platform-Specific Tracking:** Must optimize for ChatGPT, Gemini, and AI Overviews, which have different growth rates and citation patterns.
  - **Citation Pattern Analysis:** Identify specific content elements (e.g., keywords, sentence structure) that influence citations.
      - **Example:** A change on Brex's site from "10x-20x" to "20x-30x" credit limits was quickly reflected in AI citations, proving the direct impact of specific phrases.
  - **Hallucinated URL Detection:** A critical feature to identify and fix non-existent URLs in AI citations, which can cause 404s and lost conversions.
  - **Competitive Benchmarking:** A matrix view showing citation share vs. competitors is a key C-suite requirement.

### New AI Visibility Model

  - **Problem:** Current tools require each brand to build research from scratch, are expensive, and lack APIs.
  - **Solution:** A shared, standardized index of B2B buying evaluation prompts.
      - **Prompt Library:** 100k+ prompts across 1.5k B2B categories.
      - **Brand Context:** Deep research on 6k+ brands to enable highly relevant, auto-generated prompts.
      - **Free Tier:** Access to the shared library for visibility, serving as a massive SEO play.
      - **Paid Tier:** Custom prompt tracking funds the library's expansion.
  - **Predictive Modeling:** Data scientists are building models to identify content features that predict citation success.

### Integrated "OS" Platform

  - **Vision:** A private, AI-native system of work that connects visibility, execution, and analytics.
  - **Workflow:**
      - **Discovery:** Programmatically finds content opportunities (e.g., citation gaps).
      - **Execution:** Custom pipelines (e.g., how-to, comparison) use the brand kit to generate unique content.
      - **Analytics:** Correlates content activities with outcomes (traffic, conversions).
  - **Core Technology:** Built on `output.ai`, a proprietary, open-source workflow-as-code framework.

### Content Strategy & Product Ideas

  - **Focus:** Create content that solves user problems, not just product features.
      - **Example:** "How to negotiate better pricing with HubSpot" vs. "How much does Brex spend on Airtable?"
  - **Productize Workflows:** Build simple, valuable web apps that abstract product features.
      - **Examples:** A receipt classifier, a sales projection model, or an RFP generator.
      - **Benefit:** Captures user domain info for lead generation.

---

## Action Items

**Marcel Santilli**
- Process call; share Jon's feedback w/ team; prioritize platform filters, 7-day trailing average, top-50 citations, hallucinated-URL detection
- Grant Jon Kowieski (Brex) Check That access early next week; request feedback

---

## Transcript
**Arudyak:** It's okay, we have plenty of AI lurkers, so me lurking is not okay.

**Jon Kowieski:** Oh, that's funny.

**Arudyak:** Okay, are we waiting on anyone else?

**Arudyak:** No, I think Alex was optional.

**Jon Kowieski:** Cool.

**Jon Kowieski:** It's probably just me.

**Jon Kowieski:** I'm like the only one that ever goes to AI visibility tool meetings.

**Arudyak:** How many have been to thus far?

**Jon Kowieski:** Too many?

**Jon Kowieski:** I would have to look at my calendar.

**Jon Kowieski:** I've been basically meeting with anyone that's got Series A funding, and then I tend to have to, I have to meet with anyone coming from Y Combinator.

**Arudyak:** It's not really a choice because we're Brex.

**Arudyak:** Yeah, working with them and, like, helping them, and, you know, like, yeah, hopefully they're successful so they give Brex more transactions.

**Arudyak:** yeah, yeah, yeah,

**Jon Kowieski:** Yeah, they want to use some of our relationships.

**Arudyak:** I don't know.

**Arudyak:** Like, that's just, I meet with a lot of companies coming out of there that are doing a lot of random things.

**Arudyak:** Well, let me jump in.

**Arudyak:** Just my only caveat here is please, please don't share this publicly or with other vendors.

**Arudyak:** And if you're okay with that, then I can be super transparent about everything.

**Arudyak:** That's cool.

**Arudyak:** AKA, don't copy and paste and send the link to this meeting to, like, a direct competitor, you know?

**Arudyak:** Yeah.

**Jon Kowieski:** I don't plan on doing that.

**Jon Kowieski:** I can tell you right now, the plan is actually to churn already from Profound.

**Arudyak:** Music to our ears.

**Arudyak:** So I'm going to, while I'm showing you, I'm going to, like, walk you through, you know, and just give you the full context, right?

**Arudyak:** So.

**Arudyak:** So.

**Arudyak:** All

**Arudyak:** We are approaching the market and why we're not tipping our hands right now is because I think our approach, I haven't seen anyone else do this approach.

**Arudyak:** So the way I kind of think about it is right now, we talked about this, like what matters the most from an AI visibility perspective is for you as a brand to understand how AI engines overall see your buying category, right?

**Arudyak:** Because buying categories, when you say, hey, best expense management platform, right?

**Arudyak:** You want to understand, you want to probe how these AI engines understand those categories, but the one that matters the most within those categories are evaluation criteria for those buying groups, right?

**Arudyak:** Or those buying topics or categories, however you want to see it, right?

**Arudyak:** And so like the approach we took was like, hey, Crunchbase created this amazing database for startup funding, right?

**Arudyak:** SEMrush did it.

**Arudyak:** G2 search data, right?

**Arudyak:** G2 for reviews for the most part.

**Arudyak:** And then for AI visibility, all these vendors are essentially asking every single brand to build a brand new research project from the ground up.

**Arudyak:** And we're like, that's kind of silly, right?

**Arudyak:** And we needed to collect this data for our customers no matter what, right?

**Arudyak:** Because we don't want to depend on somebody else's tools.

**Arudyak:** None of these tools even have an API, to be honest.

**Arudyak:** The one or two that does have an API is garbage.

**Arudyak:** And it's like, we can't just do it one off.

**Arudyak:** So what we did instead is we essentially, this is behind the scenes, by the way, like we came up with an entire like study and we came up, said, let's just narrow the scope down to B2B buying categories mostly, right?

**Arudyak:** And, and then what we did is like, we went through these categories and we're continuously doing that.

**Arudyak:** We have editors going through these categories and then selecting like, like for instance, like, let's see, think it's been a loss or something.

**Arudyak:** Like, let's just take one of these, for example, right?

**Arudyak:** We're coming up with, like, the top prompts, and we have, like, a bunch of, like, workflows that goes and generates the best prompts based on keywords, based on persona, based on a bunch of things.

**Arudyak:** And then you have editors that go in here and pick the ones that are having, like, strong relevance in the evaluation stage.

**Arudyak:** All these were approved already, right?

**Arudyak:** And then it says, you know what, like, this is the right kind of question that is relevant to someone evaluating this category.

**Arudyak:** And then they will approve that, and then that will go into the active, like, queue for that category, right?

**Arudyak:** And so what we're building is essentially a shared library database of, like, over 100,000 prompts that we're tracking already.

**Arudyak:** And then if you're a customer, like, like, Bratz, for example, like, you want to go here and ideally get, like...

**Arudyak:** You want to make sure, first of all, that there's good context about your company.

**Arudyak:** So we enrich over 5,000 brands.

**Arudyak:** As we're monitoring these prompts, any brand that pops up in the answers, we're automatically running this insanely good deep research on it.

**Arudyak:** And so we have like an insane database of like amazing context on these companies, right?

**Arudyak:** And we have all this data now.

**Arudyak:** So then when you sign up, you know, and you add this to your tracker and you say, I'm Brex, all this data will get automatically pulled in.

**Arudyak:** All the historical data are ready.

**Arudyak:** And I'll show you that in a second, right?

**Arudyak:** But also like we're essentially building a knowledge graph of all these categories.

**Arudyak:** And we've narrowed it into, again, B2B, buying, evaluation stage, right?

**Arudyak:** Like buying categories of like mostly software categories, right?

**Arudyak:** AKA kind of like G2 categories, product hunt categories, right?

**Arudyak:** The categories that people think of, right?

**Arudyak:** But we're constantly evolving.

**Arudyak:** And it's both AI as well as like editorial approach to curate those.

**Arudyak:** And then what we're doing here is we're giving that away for free almost, meaning anything that's in your shared library, you're going to be able to sign up and get the visibility into that.

**Arudyak:** There'll be some limits, but it's free, and we're using that as a massive SEO play for ourselves as well, so that we start ranking for a bunch of things.

**Arudyak:** for instance, the actual answers, and we show all of those.

**Arudyak:** So, for instance, what is the best business bank with no transaction fees, and then it will be a page about that.

**Arudyak:** And so, hopefully, we're creating knowledge on that.

**Arudyak:** And as a customer, the benefit to you, in addition to tracking all this, is that we're doing this massive study of data scientists that used to work for, or that has done work for Mercury, for example, right?

**Arudyak:** And what we're doing is, like, essentially feature engineering and figuring out, like, predictive models of, like, what will predict that your content will get cited and mentioned, you know?

**Arudyak:** And then we're bringing those insights to how we generate content for you, right?

**Arudyak:** Right.

**Arudyak:** So that's the public area.

**Arudyak:** Think of it as a shared library of 100,000-plus prompts that we're tracking across 1,500 buying categories and over 6,000 brands that's constantly growing.

**Arudyak:** The more brands are mentioned by the answers, the more we're cataloging that and enriching that, right?

**Arudyak:** Then the experience for you that will give you access is essentially, like, just the basics, honestly.

**Arudyak:** Like, there's not a lot of crazy bells and whistles here, to be quite honest.

**Arudyak:** It's mostly, like, tracking and visibility, and we're building.

**Arudyak:** have seven engineers on this, so, like, we're improving and fixing things very quickly.

**Arudyak:** And it's a massive amount of data that we're already doing, right?

**Arudyak:** And just the ability to just, like, you know, look at all of these.

**Arudyak:** You know, these are from the library, so all of these you can add unlimited, so you can essentially, like, say, hey, select from the library.

**Arudyak:** And so then you can go here into payments and say, like, what are alternative credit card payment processors, you know, and you can, like.

**Arudyak:** Review an ad and hope that there's no bugs because I'm doing this.

**Arudyak:** And there you go.

**Arudyak:** Now it's added.

**Arudyak:** So now all that data automatically gets pulled here because we were going to be tracking that data.

**Arudyak:** And then we're trying to improve the tooling as well so that you can easily tag and create a taxonomy around it.

**Arudyak:** tagged by persona, tagged by state of the funnel.

**Arudyak:** You can retire or activate.

**Arudyak:** And any historical data we have gets automatically pulled into here.

**Arudyak:** So, like, the second you add a prompt for our share library, you don't need to start tracking only that day.

**Arudyak:** So if we have 90 days of responses, you get 90 days of responses, right?

**Arudyak:** And then you can just add custom prompts.

**Arudyak:** And then, you know, for our customers, like, they would only pay for the custom prompts that they're getting.

**Arudyak:** And this is, like, essentially, like, the last leader for us.

**Arudyak:** And the benefit is, like, the more we grow and the more customers we have, the more that helps fund this share library.

**Arudyak:** And then we already have companies like Webflow that...

**Arudyak:** Not for like Scrunch or Profound, you know, and you look at their brand kit and you read the description, it's garbage, right?

**Arudyak:** I'm sure you've seen this before.

**Arudyak:** Like you read this, this is not the one we have in that OS for you.

**Arudyak:** This is just the auto-generated one.

**Arudyak:** Like it's like so much more detail, right?

**Arudyak:** And then you go into the products and features, it tends to be substantially better.

**Arudyak:** Not perfect yet, but like substantially better, you know?

**Arudyak:** And what will constantly improve this, but the idea is like this first shot is already way better.

**Arudyak:** And then like we're also creating these personas as well that also are way better.

**Arudyak:** The reason this is all important is because without this context, you can't go auto-generate really good prompts that are the types of questions that your personas would ask within the domain and context of your company, you know?

**Arudyak:** And so, and then there's a bunch of other things here.

**Arudyak:** Like for instance, like these are like your short list of competitors.

**Arudyak:** So if there's another competitor here that you're like, you know what?

**Arudyak:** I really want.

**Arudyak:** We were talking about how many mentions it's coming up, you know, so then you can say, okay, I want to track this one, and I want to track this one as well, and this one, for example, right?

**Arudyak:** So this is just basic, like, this is just feature parity with a lot of the stuff out there.

**Arudyak:** I think our biggest advantage is, one, we have a way better deep researcher context engine.

**Arudyak:** Two, we have a much better way to generate prompts.

**Arudyak:** And three, we have over 100,000 prompts that we're tracking that companies will get access to that.

**Arudyak:** So then when they're saying, hey, I'm a leader in this category, it's not you coming up with 100 random prompts, it's you referencing a legit index, right, for that category, you know, that has some thought process behind it.

**Arudyak:** And then the more brands we have within those categories, the better that index gets, the more comprehensive it gets, the more accurate it gets as well, you know, and then anything we charge is really to just try to fund that so that we can make the index better.

**Arudyak:** Because that's not the main business we have, right?

**Arudyak:** So I know that was a lot, and that was way more than I would tell anybody else, by the way.

**Arudyak:** But hopefully that helps.

**Jon Kowieski:** I understand your whole strategy and what you're doing.

**Jon Kowieski:** It makes a lot of sense.

**Jon Kowieski:** Get more customers, get more data.

**Jon Kowieski:** You have a significant advantage, especially during a time when we just saw Profound cut their prices by 50% year over year.

**Jon Kowieski:** And everyone, all the top SEOs know that these prices will go down.

**Jon Kowieski:** And so it then becomes a pricing war and data like this has actually become more and more valuable, especially when you have that much.

**Jon Kowieski:** So I get it.

**Jon Kowieski:** I guess the biggest thing would be for us, we try to optimize by platform.

**Jon Kowieski:** As you were walking me through that, like if I wanted to see the citation via AI mode, citation via chat should be T.

**Jon Kowieski:** Okay, it filters.

**Jon Kowieski:** That was...

**Jon Kowieski:** Yeah, AI, AI, Gemini, and ChatGPT are probably the three most important to us.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So, Claude, not so much.

**Jon Kowieski:** I'm not sure.

**Jon Kowieski:** People aren't sure do research, but if you use Claude enough, you're probably not doing your research on there.

**Arudyak:** Yeah, yeah, exactly.

**Arudyak:** There's a lot of, honestly, rough corners right now, you know, so I don't want to, like, be like, hey, this is ready, we're going to launch, we're going to tell the whole world.

**Arudyak:** If we aren't confident that it's collecting really good data, and that we have really good ways to come up with the right prompts, but there's, like, that's where we can use feedback is, like, what are we missing here?

**Arudyak:** Like, for instance, right, like, if you go to, like, our prompts, and let's just take one from the library, like, I think I played around with all the tools, like, one of the things I noticed is, like, a way to visualize things, like, better.

**Arudyak:** And so this gives you, like...

**Arudyak:** And we need to add more services as well.

**Arudyak:** Like right now we're only doing like Gemini, but we're adding like AI overview and AI mode as well, right?

**Arudyak:** Like there's like things like that that are very fast and we're just waiting for feedback a little bit.

**Arudyak:** But like you can digitally see like, hey, Brex is, you know, getting, seeing presence in chat GPT, but literally in Gemini is, you know, again, we need to validate this, is not getting like citations, you know, and then hopefully like you can go here and like see that and kind of, you know, see the results.

**Arudyak:** But there's a lot of like corners there that we can tweak really fast and that hopefully like, like for example, this visualization, this is a ticket right now that's open, which is like, we're doing only a snapshot and then it looks really spiky because of that.

**Arudyak:** So we're changing this to like a Saturday trailing average so that it looks a little bit easier for you to see the trend versus like this doesn't work like anything.

**Arudyak:** So little things to increment, simple find experience, and all of that, and then validating that everything's there.

**Arudyak:** We're confident we're collecting the right data, but definitely this is nowhere near ready for showtime, but we have insanely good engineers and people on this, so it's a top investment right now.

**Jon Kowieski:** Yeah, even have one person in the C-suite that likes to see, like, are we doing a Grok?

**Arudyak:** I'm like, no, who uses Grok?

**Jon Kowieski:** So, yeah, that's where, for us, I definitely like to see things like the top 50 citations for certain prompts.

**Jon Kowieski:** I'm one of those people that loves finding patterns, I guess you could say, across everything I do.

**Jon Kowieski:** And there are absolute patterns in which I've identified, but that's true.

**Jon Kowieski:** Just down the road since, I mean, you're just coming out and I do, I've not seen anyone else with data like this.

**Jon Kowieski:** So I see the value and I understand the value too.

**Jon Kowieski:** The ability to basically have all these prompts auto-generated too, saves me an enormous amount of time.

**Jon Kowieski:** And even these auto-prompt generators for some of these companies, I do not find the prompts to be very useful.

**Jon Kowieski:** So what they're suggesting.

**Arudyak:** context, right?

**Arudyak:** Like all this, like if you don't have good this, like in good this, then like the prompts are just going to be super generic and , you know?

**Jon Kowieski:** Yeah, and that's part of it.

**Jon Kowieski:** I mean, I'm also thinking around things like, what are the specific keywords that are influencing the most questions?

**Jon Kowieski:** Because typically, these models are looking at multiple queries and then they come up with their answers.

**Jon Kowieski:** Therefore, their output through that, I guess you could call it, what is it, grounding?

**Jon Kowieski:** So there's stuff like that that I'm thinking through at this moment.

**Jon Kowieski:** I mean, query search fanout, I feel like people are starting to think about that more, but I'm not sure how valuable that is.

**Jon Kowieski:** I know of free tools out there that are already doing it.

**Jon Kowieski:** Like, and I think I see them much.

**Arudyak:** It's like, there's no way, if you look at, just go look at your history in chat to BT or plot, right, or whatever you use, and then go look at the thread, like the entire thread of a question and answer, question and answer, question and answer.

**Arudyak:** And, and like, there's, it is impossible to try to replicate that.

**Arudyak:** Just impossible.

**Arudyak:** It would never happen, right?

**Arudyak:** And so what we're trying to do is say like, hey, can we probe it enough and be comprehensive enough you know, not hyper specific, but just like comprehensive enough to create an index that over time becomes more

**Arudyak:** Or more, you know, accurate because with more data and the more we grow, the more that index may be.

**Arudyak:** Instead of 100 questions per category, could be 1,000 questions per category.

**Arudyak:** Instead of probing every question every day, maybe it's like some questions are probed every other day or whatever.

**Arudyak:** And you find like the right and that's why it was study and figuring out what's predictive and not.

**Arudyak:** Right?

**Arudyak:** and then outside of that it's like ultimately around like how do you map what topics your audience cares about and that's what we're trying to do is kind of like figure out like how do we map the topics that really matter to your audience as opposed to the prompts that they're going to actually type into chat dpt and then how do you prove that you're like up there on a consistent basis on the high level one right because if you're there in the high level and you map out you're pretty good about mapping out what questions like your customers care about and your audience cares about and you're consistently finding a path to become cited and mentioned and become the best answer then like that will direction you

**Arudyak:** If had in the right place, otherwise it just, I mean, it's just that these companies are so financially incentivized for you to track 1 million prompts.

**Arudyak:** And that's just like silly, in my opinion, you know?

**Arudyak:** And so that's kind of like what we're focused on a bit more, but also like we're very early.

**Arudyak:** We've only been building this for like two, three months, you know?

**Arudyak:** And for me, like self-explanatory is like, like the most important thing is get feedback from people like you and earn your trust that this could be like, you don't need to go sign a big contract with Pete or Profound or any one of those.

**Arudyak:** And then if there's any major gaps, like I will get seven engineers to drop whatever the  they're doing today and go focus on that.

**Jon Kowieski:** I think you did call it out at one point.

**Jon Kowieski:** It's the actions.

**Jon Kowieski:** It's what should we do outside of just the content, outside of the content on our website to influence the citation.

**Jon Kowieski:** We already do.

**Jon Kowieski:** I'm that right now.

**Jon Kowieski:** Some people are aware of it.

**Jon Kowieski:** Some are not.

**Jon Kowieski:** But at the end of the day, it's like, how do you influence the algorithms?

**Jon Kowieski:** What do they look for?

**Jon Kowieski:** What's important to them?

**Jon Kowieski:** And that's like, Gemini is different from ChatGPT.

**Jon Kowieski:** Do we have to build content in a certain way for each?

**Arudyak:** Maybe on different websites, like we're talking through.

**Jon Kowieski:** So it's that kind of stuff like I'm thinking through at this moment as we see Gemini growing at 30%, while ChatGPT grows at 10%.

**Jon Kowieski:** So granted, they also have memory.

**Jon Kowieski:** And that is also something I'm trying to think through.

**Jon Kowieski:** I don't know how anyone would do anything with memory.

**Arudyak:** Yeah, like it's like, there's two things in that, right?

**Arudyak:** Like, we're kind of tackling it in different angles.

**Arudyak:** And then everything I just showed you, eventually, this is our OS that might ideally end it.

**Arudyak:** January, we'll give you full access as well, so you can at least see, but this is what we're executing, right?

**Arudyak:** And then think of search visibility as what will be full from check that.

**Arudyak:** So check that is just a distraction of this.

**Arudyak:** But this is our opportunities place, and a lot of what we're doing is exactly what you said.

**Arudyak:** It's like, how do we find those topics based on a bunch of different patterns, right?

**Arudyak:** So think of the patterns as ways for us to find the right opportunities, right?

**Arudyak:** And so it could be persona-based, it could be URL-based, it could be based on gaps based on domain, it could be, you know, like, there's a bunch of different ways.

**Arudyak:** then AI visibility and citation gaps or, you know, social listening, those are just like additional ones that we're continuing to develop.

**Arudyak:** So we know how to do it manually, and we do that manually, but then like this is more programmatic.

**Arudyak:** so you come here, and then we'll pick, like, let's say, like, an engineer, an engineer,

**Arudyak:** Figure out, okay, cool, let's go, like, way deeper on this and then start the research.

**Arudyak:** And it kicks off, like, a hundred different agents and researchers and workflows.

**Arudyak:** And it's, like, but it's also pulling, like, all the context we already have.

**Arudyak:** And then it's finding, like, topics and then turning those topics into opportunities.

**Arudyak:** And then you go in here and you see these opportunities.

**Arudyak:** And then it's categorizing and tagging those to opportunities, right?

**Arudyak:** Like, like, accept those opportunities.

**Arudyak:** And then if we accept those opportunities, then don't turn them into assignments, you know?

**Arudyak:** And those are the priorities that our team is going to go execute for you, you know?

**Arudyak:** Using a very specific pipeline that's custom built with this content type for you and with the context of your brand.

**Jon Kowieski:** Does that make sense?

**Arudyak:** And then, like, like, artifact is all here, but...

**Arudyak:** Then what we're doing next is building like a taxonomy auto-classifier.

**Arudyak:** So it's like creating taxonomies of like my persona, my stage, my group type, my segment, my topic.

**Arudyak:** It's like essentially like creating a taxonomy for your entire business.

**Arudyak:** And then that taxonomy can then be applied everywhere.

**Arudyak:** can be applied to opportunities, classification, pages.

**Arudyak:** So for pages, like we're scraping and indexing every single page on your site.

**Arudyak:** And then starting to classify and create collections for those pages.

**Arudyak:** And then also like surfacing any issues.

**Arudyak:** You know, we're moving super fast.

**Arudyak:** There's like a round of like probably a lot of like, like, like rough edges right now.

**Arudyak:** Right?

**Arudyak:** Like, but the whole idea is like, so the whole idea as this pulling up is like on the pages, is is like, whole idea like,

**Arudyak:** I don't know why it's being so slow, it is like, it's grabbing all the, like, for every single page, like, the content of that page, right?

**Arudyak:** And so, like, it's correlating with the traffic, it's looking at, like, the actual content, it's taking a screenshot, it's looking at the markdown, it's extracting the HTML, it's, like, looking at the tech report, and, you know, you can, like, refresh it and look at, like, you know, the performance of that page.

**Arudyak:** And so, it's creating, like, this whole inventory, right, of signals.

**Arudyak:** That way, we have, like, the context of your brand, the taxonomy of your business, all the signals from AI visibility, search console, and traffic, as well as the tech report, as well as the actual output and content of the page, and then, like, then we can close the loop and this be your OS or, like, your content engine, you know, or a content that sits on your website.

**Arudyak:** So that's the craziness of it.

**Arudyak:** It's like, we're like, I think a month away, right?

**Arudyak:** Like, you can see, like, there's bugs, you know, like, just super rough around the edges, like, the opportunities, you know, are like, where it's like, check that, we can give you access now.

**Arudyak:** And, and then, like, hopefully, you can kind of go through, and if you're open to, essentially, like, think of this as, like, we're giving you unlimited access for check that, tell us what, what else we could do in order for you to not sign a contract with Pete or whatever.

**Arudyak:** And then hopefully, with the intent of, like, if we knock it out of the park, you would be excited to be, like, a Lighthouse customer for us, you know, on check that.

**Arudyak:** While we're pulling in, closing the loop on this OS side, and then this is, like, you know, you already came for this, right, essentially.

**Arudyak:** So it's just a matter of, like, closing the loop to be able to give you access to it.

**Jon Kowieski:** And hopefully by the end of the day, right?

**Jon Kowieski:** Do you know what the pricing would be already for this?

**Arudyak:** Or do you have any idea?

**Arudyak:** I mean, you're already paying for it.

**Jon Kowieski:** Oh.

**Arudyak:** Like it's yours.

**Arudyak:** You know, it's just mostly right now we're executing it for you because there's a lot of rough edges, you know?

**Arudyak:** And then we're publishing on your behalf and we're doing all the work for you, you know?

**Arudyak:** But think of this, like right now we're surfacing these opportunities in an Airtable, whereas later on I can be able to like filter this and use it a lot and you accept the opportunities and then the assignments are just going to be executed, right?

**Arudyak:** Like so today, the way we're executing these assignments is like, I'll just show you a newer environment, right?

**Arudyak:** I think this is, let the opportunity set up for you.

**Arudyak:** So like, well, let's just do it personally.

**Arudyak:** Let's do it personally.

**Arudyak:** Let's personally.

**Arudyak:** personally.

**Arudyak:** So I'll start to do the research on this, right, and this is like your environment right now, you see like it's finding topics, you know, you see how quickly it's like finding much, and then the opportunities will be here once it's like done processing, and then I can show you like behind the scenes, generate opportunity workflows, you see this is what's kicked off right now, but like this is the opportunity workflow that's generating right now, and then like once it's done running, and then on the execution front, these are the pipelines that we're building for you, right, like right now, right, it's been like the deep researcher, you know, it goes in and does like research on the topic, generate the plan, and then it's always the research.

**Arudyak:** So think of it as, like, every content type that we have, let's say a how-to, a comparison, or whatever, is an opportunity type, and then for each one of those, there's, like, a custom pipeline for that for you, right?

**Arudyak:** So then when you hit execute, right, or accept that opportunity, it'll turn it into, ideally, like, an editor or someone, I think this process is a lot more, Because it's not just, like, zero-shot, hold your app, and take over all the strategy.

**Arudyak:** There's still, like, nuances of it that you want people to make sure it's good, you know, if that makes sense.

**Jon Kowieski:** Yeah, I guess for, like, drafting the article is basically what would separate us from authors using your software, what would be, like, the brand kit?

**Arudyak:** It's a combination of things, right?

**Arudyak:** Like, there's a lot of instructions, there's a lot of, like, contacts to get in the brand kit, there's also, like,

**Arudyak:** You, like, how you prioritize which opportunities you go after, and there's obviously, like, a ton of other factors that make brex brex, right, for example.

**Arudyak:** And so, like, for instance, like, if you look at the current artifacts the way we have it today, like, there's a lot of nuances, right, the writing guidelines, the audience personas, the, you know, how you talk about things.

**Arudyak:** Then in the execution layer, there's a lot of custom instructions that we can have, right, like, which is, like, the kind of sources, the structured topics to cover, like, sources to use or not use.

**Arudyak:** Like, there's, like, there's, so much here, you know, tool calling, like, there's, like, an insane amount here, right, that can be tweaked.

**Arudyak:** And in other words, like, between that and some of the pipeline here, it's extremely unlikely, impossible, let's not even say unlikely, impossible that two brands picking a...

**Arudyak:** A similar opportunity would have the same output, you know?

**Jon Kowieski:** Yeah, I understand.

**Jon Kowieski:** Using AI, I don't know if I understand how it would work.

**Jon Kowieski:** I guess, and then can people connect like their analytics to this as well?

**Jon Kowieski:** Like, let's say, if all sites are seeing traffic to certain pages, and maybe there's leads coming from those pages from like chat at Chibi-T?

**Arudyak:** Yeah, exactly.

**Arudyak:** So, you know, like you can do that.

**Arudyak:** And so what have is just like a analytics view, right?

**Arudyak:** It's pretty basic, but it just plugs into either Google Analytics Fathom or PostHog, right?

**Arudyak:** We're not yet ingesting like conversion events, you know?

**Arudyak:** And so like if you have custom conversion events and things like that, I mean, we're ingesting the data, but we're not displaying the data.

**Arudyak:** And then there's like LLM traffic, and so that you can see like LLM traffic by page and things like that.

**Arudyak:** And then there's like search visibility, which is connected to your search console as well.

**Arudyak:** So, and then that AI visibility, we haven't built it yet, or we built it and checked that, but we haven't yet integrated into this.

**Arudyak:** But it would be essentially this, right?

**Arudyak:** Like this view, but integrated there, essentially.

**Arudyak:** So then that closes the full loop of analytics, you know?

**Arudyak:** Obviously, there's conversion data.

**Arudyak:** Conversion data is really messy because a lot of people measure conversions, attribution, like that's hard.

**Arudyak:** And then between you and I, then our goal is in Q1, build our own pixel as well.

**Arudyak:** So one of our engineers was the top engineer at Koala.

**Arudyak:** I don't know if you remember Koala.

**Arudyak:** I do.

**Arudyak:** So there's, yeah, so he built this content report.

**Arudyak:** And so that's like what we're building late in Q1, most likely, you know, but we're kind of like, you know, we don't have FD money in the bank, like.

**Jon Kowieski:** We were like, you know, like, we're moving as fast as possible, but also don't want to, like, oversell.

**Arudyak:** But that's our plan is to then build a pixel event so that we can do attribution kind of like this, know, content attribution like this, you know.

**Jon Kowieski:** I know some VCs that would be interested.

**Arudyak:** We're just trying to tip our hands too much, you know, because I really, like, this is the  I've been doing my whole career.

**Arudyak:** And so I know what we need to do and how we need to do it.

**Arudyak:** It's just, like, we are trying to build it in the right primitives.

**Arudyak:** And it's pretty gnarly problems, man.

**Arudyak:** Like, we have terabytes and terabytes of data daily.

**Arudyak:** Just protect that, you know.

**Arudyak:** It's, like, it's not an easy, like, data problem to solve.

**Arudyak:** Like, these are hard things to build, you know.

**Arudyak:** Not impossible.

**Arudyak:** Just, like, it's not a, like, we have, like, really seasoned infra and, you know, principal engineers.

**Arudyak:** You know, so luckily we're able to, like, know what to build because they've built things that scale before.

**Arudyak:** But, um...

**Arudyak:** It's a big surface data with tackling, you know?

**Jon Kowieski:** So right away, I could tell you, like, one thing I want to know is if I do create an article, like, if it has an impact, like, 30 days later on a certain citation, because you're almost making that correlation from what you just said anyway, like, did that article actually work?

**Jon Kowieski:** And if it didn't, I can make that assumption, but if there was, like, a checkbox, like, if you had actions or opportunities, where it's, like, here's your opportunity, I want my team to be working in your product, not outside of your product, in a Google sheet, like, here's what we did on this date, and here's kind of what happened, it would be much more preferable to have it all in there.

**Arudyak:** I think we hit the, we hit this, but give me a second, just to show you, like, look at this.

**Arudyak:** We're tracking everything, like, down to even the user level, the pipeline executions, what they did in the intervention, who they did it for, you know, like, you know, it's just a matter of, like, how do we use these activities and start to overlay these activities.

**Arudyak:** So the way we think about it is, like, the outcome you care about is AI disability, search visibility, traffic, and intervention conversion.

**Arudyak:** The output that you can control is pages on your site to either create new pages or improve the existing pages, right?

**Arudyak:** Then there's all these inputs of, like, contacts, opportunity, and things like that.

**Arudyak:** There's all these executions, which is both, like, AI executions as well as human interventions, and that then work towards, like, an output.

**Arudyak:** Like, selected an opportunity, executed that opportunity, and then you hit publish.

**Arudyak:** Then you're trying to correlate all the inputs, all the activities, and to the output, and that the output had an impact.

**Arudyak:** The outcome you care about, positive or negative, you know?

**Arudyak:** it's like, but right now, like, that's a pretty gnarly thing.

**Arudyak:** It's like, I like to call it a system of work, an AI-native system of work.

**Arudyak:** And so, you know, not a system of record, not a system of engagement, but it's like, there's a lot of things here to connect, you know?

**Arudyak:** And so, like, that's why we're building.

**Arudyak:** We have the big picture in our heads.

**Arudyak:** It's just like, we have to build one by one in order to not be so shallow that, like, if the execution is garbage or we didn't have, like, workflow as code, you know?

**Arudyak:** For sure.

**Arudyak:** Like, for instance, like, this is our output framework that we're launching next month, and we're open sourcing this.

**Arudyak:** called output.ai.

**Arudyak:** And it's essentially, like, how it's our workflow as code framework, you know?

**Arudyak:** And so it has workflows and orchestration, promises code, built-in evaluation, complete traceability, plot code integration, and then it's like a tag script framework, you know?

**Arudyak:** And, like, literally, this is what the tag that our entire company is built on.

**Arudyak:** doing.

**Arudyak:** we какие

**Arudyak:** This is like, you know, and we're open sourcing this month, right?

**Arudyak:** So we have to build this the right way.

**Arudyak:** You know, it's like, build an LLM as a judge, an application, see everything, replay everything.

**Arudyak:** And so it's like, anyways, and with like a super production enterprise grade, we're on time later on top of that.

**Arudyak:** So it's like a, instead of NAN, it's really like a workflow as code framework.

**Arudyak:** And that will power everything, it powers everything.

**Arudyak:** And then this is the system of work that we built for this specific use case, which is content that goes on your website, you know?

**Arudyak:** And so, anyways, and so the only way we were able to fund all of this was by doing service, because the tech wasn't there and the tech's being evolving, you know?

**Jon Kowieski:** But it's just...

**Jon Kowieski:** Oh.

**Jon Kowieski:** Can lose you?

**Jon Kowieski:** Uh-oh.

**Jon Kowieski:** Oh, no.

**Jon Kowieski:** no.

**Jon Kowieski:** Oh, no.

**Jon Kowieski:** Oh, no.

**Jon Kowieski:** Oh, Oh, no.

**Jon Kowieski:** Oh, Oh, no.

**Jon Kowieski:** Oh, You

**Jon Kowieski:** I think, can you hear me?

**Jon Kowieski:** Yeah, I can hear you, perfect.

**Marcel Santilli:** Okay, something froze in the meeting room, but hopefully you got what I said.

**Jon Kowieski:** Yeah, I'll also bring up a feature I've seen no one do that is extremely important, and even today, I'd rather not bring up this feature to our competitors.

**Jon Kowieski:** AI is hallucinating URLs.

**Jon Kowieski:** They already were, and I already knew this would happen anyway.

**Jon Kowieski:** But just this morning, came across URLs being hallucinated for all of us.

**Jon Kowieski:** So if I could have a way where I could detect that, it would also be extremely useful because what we are now talking about is I'm losing a conversion.

**Jon Kowieski:** Um...

**Jon Kowieski:** ...

**Jon Kowieski:** So we already fixed it this morning.

**Marcel Santilli:** Can I clarify really quickly?

**Marcel Santilli:** Are you talking about hallucinating URLs that then is used for research, so it's using bad research?

**Marcel Santilli:** Or are you talking interlinking or linking to something that doesn't exist?

**Jon Kowieski:** Or are you talking something else?

**Jon Kowieski:** Linking to 404s, linking to URLs that the AI models just simply made up.

**Marcel Santilli:** This morning, it was pretty bad when I came across it.

**Marcel Santilli:** Yeah, so let me show you what we do that's pretty, I think, effective overall.

**Marcel Santilli:** And we'll do it for you as well.

**Marcel Santilli:** But it's like, you look here, there's like, call it add internal links post processor.

**Jon Kowieski:** And then what this does is like, it validates every single URL before cross links.

**Jon Kowieski:** So I don't mean that.

**Jon Kowieski:** I mean, for example, I was in a model this morning, just searching, looking at the actual citation, and notice that every single URL blue link.

**Jon Kowieski:** Fathom a made-up URL.

**Jon Kowieski:** Really?

**Jon Kowieski:** did not exist.

**Marcel Santilli:** They all went to 404s.

**Marcel Santilli:** In the answer or in the citation?

**Jon Kowieski:** In the citation.

**Jon Kowieski:** That's what I mean.

**Jon Kowieski:** If I had some kind of citation software to identify that immediately, like, I would have fixed it.

**Jon Kowieski:** Now, I'm pretty sure I'm the only one who bought it.

**Marcel Santilli:** So, like, just to understand.

**Marcel Santilli:** So, are a user in ChatGPT, you put in a prompt, and that triggers a search tool, and that answer includes citations that, for whatever reason, that service indexed and no longer exists, or indexed and made up?

**Jon Kowieski:** It's just made up.

**Jon Kowieski:** These URLs never existed.

**Marcel Santilli:** Well, that's wild.

**Marcel Santilli:** I've never seen that.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** When I caught it this morning, I had to check.

**Jon Kowieski:** Multiple prompts across the board because I've known this to happen before and before my time at Brex, I was working on a company that kind of helped solve that issue.

**Jon Kowieski:** So, but that information is something no one talks about that I believe will probably become a bigger problem because then what it led me to thinking is like, you know what?

**Jon Kowieski:** I could actually manipulate my competitors right now.

**Jon Kowieski:** I could just start creating links that don't exist going to board portion.

**Jon Kowieski:** So, which we're talking about Black Hat, which I don't do, but at the end of the day, technically that could be happening at a much more rapid rate because of stuff like that.

**Marcel Santilli:** Yeah, there's a lot of stuff like that that like we get asked about all the time.

**Marcel Santilli:** Like, hey, can you just brute force these models to index your pages faster and then force like fake conversations that then ask about specifically like, you know, like Ramp is doing it, right?

**Marcel Santilli:** Like if you go to like a Ramp blog, it's.

**Marcel Santilli:** I like, this in chat GPT.

**Marcel Santilli:** I'm like, why would we be sending traffic away from your page?

**Marcel Santilli:** But maybe it works.

**Marcel Santilli:** I don't know.

**Marcel Santilli:** Like, it's just like, we kind of try to stay away from like either gray hat or things that are not super proven because what you can control that always wins at the end, like I said it last time, right?

**Marcel Santilli:** were talking, it's like systematically becoming the most useful, best answer to people's question that your audience cares about.

**Marcel Santilli:** And then like you should, as a company and as a marketing team, you should still experiment the crap out of this.

**Marcel Santilli:** And we're not trying to be the end all be all for everything.

**Marcel Santilli:** You know, we're trying to focus on an important problem and an important thing that if we get right, would be really valuable to companies.

**Marcel Santilli:** But it's not the only thing that would be valuable to companies, you know?

**Jon Kowieski:** Yeah, we actually created something similar to that.

**Jon Kowieski:** And the only reason why is because we realized the memory in chat GPT AI mode, as well as Gemini.

**Jon Kowieski:** If you start impacting that and it starts looking at your website specifically through a prompt, technically you are now influencing the rest of the prompts that go through that specific person's ChatHPT instance.

**Marcel Santilli:** So the memory itself.

**Marcel Santilli:** Okay, that makes sense.

**Marcel Santilli:** So it's more like impacting the context that service has about that specific user.

**Jon Kowieski:** I do not think they did it for that reason.

**Jon Kowieski:** I think they just saw another company do it, but they didn't fully understand the actual reason behind it.

**Jon Kowieski:** The only thing that could happen, though, is you could actually be impacting your rankings in a bad way because Google might see you, that your scroll death goes down, that your time on page goes down, that things that actually looks at for every Google user, like that goes into the algorithm.

**Marcel Santilli:** So technically, it seemed like a great experience, like a good experience for a user would be I land on this page and there's like a chat with.

**Marcel Santilli:** That's native to my site, that then I can ask questions.

**Marcel Santilli:** That feels like a better maybe experience, or like, that, then like, take me to ChatGPT, and I might not come back to your site, like, you know?

**Jon Kowieski:** Yeah.

**Marcel Santilli:** Like, maybe you're getting a 5% increase in AI visibility because of that, but you're for sure taking a 10% hit on conversion rate.

**Marcel Santilli:** So it's like, I don't know which one is worse or better, you know?

**Jon Kowieski:** So that's, we thought through that already, and we would only do it on like, super top of funnel pages that in general never generate conversions.

**Jon Kowieski:** And never put something like that on a page where you have a good conversion rate because actually what you just said, like, you would actually just blow up your conversion rate most likely.

**Jon Kowieski:** Because even ChatGPT with a prompt we put in through that was like, identifying right away, this is bias.

**Jon Kowieski:** This is, I'm like, oh man, like, if they have people actually going to ChatGPT, it's actually not good.

**Marcel Santilli:** What we did for Lovable was like, yeah, what we did for Lovable for the template stuff that we built for them, it's like, if you go here, then, like, it integrates more into, like, the projects, so then, like, you can preview it, and then once it finishes loading, because it's, like, super slow to load the project, you can click create your own, and it forks this whole project.

**Marcel Santilli:** So, it's like, this is a programmatic page that then gets integrated into the product, so then if I click this, like, it's going to literally, like, it takes a little while, because, like, their system's a little slow, but it will literally, like, load that project into here, and then you can fork that project from there is kind of, like, the whole idea, you know, like, you can see, like, it's, like, kind of slow, because their systems are slow, like, so we can't control that too much, but, like, if you click preview, it's, like, fully functioning website that you can fork, essentially, you know, and then the same templates, if you go to their templates within the product, these are all our templates that we created for them.

**Jon Kowieski:** Oh gosh, that's crazy.

**Marcel Santilli:** I'm surprised their own in-house team didn't do this.

**Jon Kowieski:** That's wild.

**Jon Kowieski:** I mean, this is basically like the Canvas strategy, templates galore, which we have thought about exploring.

**Jon Kowieski:** The only thing that's gone through my mind is like, can ChatGPT and Claude start making templates?

**Jon Kowieski:** Because I'm starting to think through that and it seems like that could be a direction.

**Jon Kowieski:** But that's where I don't know what your team has seen through that or tried actually.

**Jon Kowieski:** Like, because if you can and you can do it simply, do you really have any reason to get a template through a website anymore outside of like a website like lovable?

**Jon Kowieski:** But I mean, like a Binance template or something like that, if you know what I mean.

**Marcel Santilli:** Like, like, yeah, why would you do it through there?

**Marcel Santilli:** Like, I think workflows, productize workflows as like full-on media apps.

**Marcel Santilli:** Apps could be, like, a good path where you're abstracting away, like, a subset of, like, your, like, what your product can do.

**Marcel Santilli:** Yeah, that's what I was thinking through a little bit, Like, for instance, like, sorting through transaction or, like, a receipt classifier or, like, a, like, you know, like, one-off things.

**Marcel Santilli:** That, sure, you can copy and paste the receipt into ChatGPT, but hopefully, like, Brex has better logic and a better prompt and a better experience and a better output, you know what mean?

**Marcel Santilli:** Or, like, import a CSV and it outputs, like, a table full of whatever or, you know, hey, analyze this and you put this and it gives me that.

**Marcel Santilli:** Like, you know, like, like, build me a sales projection model, you know, like, and it has, like, a pre-prompt and how to think about how to build a projection and whatever.

**Marcel Santilli:** And then the output is, like, you give all this and it's, like, you put the domain of your company.

**Marcel Santilli:** You know, and it like outputs like a company researcher or it outputs a like financial model for this company.

**Marcel Santilli:** Like  that's like feels like, whoa, this is like, it is a prompt and it is using these models, but it's like a legit workflow that is valuable, you know?

**Jon Kowieski:** Yeah, that makes sense too.

**Jon Kowieski:** Maybe that's even an article actually in itself.

**Jon Kowieski:** I was trying to think of like creative articles that no one's ever written before that could actually just go kind of crazy and get popular.

**Jon Kowieski:** And it's that kind of stuff we've thought through a little bit, just haven't even created, but there's no search volume around stuff that doesn't exist like that.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** I mean, like, I think the vendor stuff could be really interesting as well, because like it did do a decent job for RAMP.

**Marcel Santilli:** And they literally hire full-time data scientists after we like did a lot of that.

**Marcel Santilli:** Content, you know, but, but I think there's like better, more unique angles to take as well, or not better, but it's like, I think there's like, I don't know, like, like vendor, like the website vendor, like we were going through with them because they were thinking of like getting our help, but whatever.

**Marcel Santilli:** And I think like they had it right, but then they don't have a marketing team anymore and they're not doing , but it's like, I think it's like doing things like this is way more valuable, like, you know, than with better content because there's just like outdated, but like this is a better potential than like, than, than they redesigned it recently, but it's like, than this, you know.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like how much does it cost versus like, how much do businesses spend?

**Marcel Santilli:** It's like, who's searching for that?

**Marcel Santilli:** Like, I don't care how much Brex spends on Airtable.

**Jon Kowieski:** I care how much Airtable is going to cost me, you know?

**Jon Kowieski:** Just some general SEO research would tell you, yeah, this is not.

**Marcel Santilli:** Like, and so it's like, how do you negotiate better pricing with HubSpot?

**Marcel Santilli:** Okay, that's a good thing, right?

**Marcel Santilli:** Like, so that's where, like, vendors went.

**Marcel Santilli:** And I can tell you this because they're not a customer, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so it's like, that, like, the negotiation tactics, like, the things like that, like, what do people care about if they're using Brex?

**Marcel Santilli:** Not because they're using Brex, but they care about?

**Marcel Santilli:** It's like, saving money, right?

**Marcel Santilli:** Like, optimizing their vendors, like, reducing overlap in vendors, like, similar vendors, like, you know, like, alternatives, yeah, sure, they care about that.

**Marcel Santilli:** Like, costs, how to negotiate costs, like, how to understand, like, you know, what's a reasonable cost or whatever, you know?

**Marcel Santilli:** And so, like, that feels like...

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Or value.

**Jon Kowieski:** Essentially, better user value is clear.

**Jon Kowieski:** It's the information I actually want, and I'm not going to read a bunch of garbage that I really don't care about, because you'll probably lose me after the first fold.

**Jon Kowieski:** So I get what you mean right there.

**Jon Kowieski:** That's just good content marketing, essentially.

**Marcel Santilli:** Yeah, or like a, like, RFP, like auto generate an RFP, like pick a vendor, you know, and then put the domain of your website, by the way, like anything you can do to have people put their domain, you know, in the experience is awesome, because now you're like, you know, who to work for, you know, in a lot of ways, and then you get them to input something.

**Marcel Santilli:** And it's like, cool, use that domain, you can use our deep researcher that we already ran, like, we can give you that data as well.

**Marcel Santilli:** You know, we have that deep researcher on 6,000 companies that cost us over 300 grand to do.

**Marcel Santilli:** Like, so, you know, if you want that, like, you know, we can give you that.

**Marcel Santilli:** I don't know, like, there's maybe some creative things.

**Marcel Santilli:** Like, for me, I just want Brex to be, like, our badass, like, Brex and Lovable to be our two, like, badass, like, house customers that we're like, okay, cool, you know.

**Jon Kowieski:** I was like, everyone's ramp, but it's just been me versus all of you.

**Jon Kowieski:** That's where it's funny.

**Jon Kowieski:** Yeah, that's where I totally understand where your product's at and where you're heading to.

**Jon Kowieski:** And that's where, if you even want to see what Profound is doing, I really don't care.

**Jon Kowieski:** Like I told you, I'm just going through multiple products and understanding, is this valuable for me or is this not valuable?

**Jon Kowieski:** At the end of the day, I don't think it's that valuable for SaaS companies.

**Jon Kowieski:** Maybe for retail, because some of their features are going to retail.

**Marcel Santilli:** Yeah, like, consumer stuff, like super long tail.

**Marcel Santilli:** What kind of questions people are asking about, like, if you're researching best headphones, you're, you know, over-year headphones within $200, $300 range.

**Marcel Santilli:** Like, okay, you probably want to know.

**Marcel Santilli:** You probably want to be recommended.

**Marcel Santilli:** Like, there's a big market there, I think, you know, but, like, we're not doing that.

**Marcel Santilli:** Like, that's not our wheelhouse at all, you know.

**Jon Kowieski:** Yeah, and that was also where I'm trying to find citation patterns and, like, what's actually being cited, to be honest.

**Jon Kowieski:** And I'm probably, I haven't really come across anyone that's doing that.

**Jon Kowieski:** So, like, what sentence should I change within my content that would actually influence this?

**Jon Kowieski:** Or let's say I wanted to say something different, which I literally just did this to, like, our high-limit business credit card.

**Jon Kowieski:** Or, like, we moved it from, like, 10 to 20 to 20 to 30, and it's already being cited that way.

**Jon Kowieski:** So, it's that kind of stuff that we've had to what to what, you said?

**Jon Kowieski:** My PMM team moved it from 10 to 20 to 20 to 30.

**Jon Kowieski:** So, I don't know what the data, whatever data that they have.

**Marcel Santilli:** 20 to 30 what?

**Jon Kowieski:** Oh, I'm sorry.

**Jon Kowieski:** I should have just been real clear.

**Jon Kowieski:** 10x to 30x, like, higher credit card limits.

**Jon Kowieski:** Like, that sentence is what these models care about.

**Jon Kowieski:** So,

**Jon Kowieski:** I think you've said it before.

**Jon Kowieski:** It's clearly, like, you need to look at multiple pieces of content.

**Marcel Santilli:** so what we're doing in this study, just so you understand, it's like we are taking all these prompts, right, that are already in our data set.

**Marcel Santilli:** For every single one of them, we take the citation and we scrape the entirety of those sites, right?

**Marcel Santilli:** Like, and then we're also doing a ton of post-processing to extract both of the responses as well as, like, the content itself that's on those pages and the domain and things like that.

**Marcel Santilli:** And then we're essentially coming up with, like, predictive models on all these, like, features, if you will, or these hypotheses of, like, you know, length or, you know, mention or content type or, like, a bunch of those.

**Marcel Santilli:** I'm not doing justice in explaining, but it's, like, hundreds of those, right?

**Marcel Santilli:** And then the more data we have, the better the predictive models can be, and what we're trying to figure out is, like, what is predictive of, you know, citation, mentions, you know, what will impact?

**Marcel Santilli:** How will it impact?

**Marcel Santilli:** What exactly is impacting this over here?

**Marcel Santilli:** And things like that, you know, and then having both like, if you have a massive, a big data set enough, then you can kind of hold things, have training versus testing and, you know, but it's mostly like predictive modeling overall in the study.

**Marcel Santilli:** So then like, there's questions like that, like, I'll double check if like, we're like, making sure we're like, asking all those right questions, you know.

**Marcel Santilli:** But, but that's kind of like the design of the, of it, you know, right now that we're running through.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** that's where we're also trying to figure out like the citations that are maybe ranking 50 to 100 that we can reach out to and influence.

**Jon Kowieski:** At the same time, we're creating some of those ourselves on other websites.

**Jon Kowieski:** So though, what you told me.

**Jon Kowieski:** Ramp is building out these new websites that actually won't work from what I've seen, unless you put in like hundreds of thousands of dollars into backlinking, and then you might actually have a pattern go off, then Google might be alerted.

**Marcel Santilli:** Yeah, I agree with that.

**Marcel Santilli:** Like, honestly, like, it's a lot better to do that if you see it as a content play and maybe even a newsletter, and then, like, organic traffic becomes, like, a bonus that, like, once you build the credibility and backlinking and things like that, it does better, you know, like, but unfortunately, like, that's a direction we pushed them on, and they didn't want to go in, you know, between us.

**Marcel Santilli:** Like, it was just like, this is garbage.

**Marcel Santilli:** Like, why would you want this to be garbage?

**Marcel Santilli:** Like, we don't really care.

**Marcel Santilli:** We just wanted to see if it

**Marcel Santilli:** Influences this is like, okay, like, it's like one of those things was like, we almost said no, and we're like, all right, it's good learning for us anyway.

**Marcel Santilli:** So we're getting paid to learn.

**Jon Kowieski:** From what I've learned, websites under a certain DR domain rating do not influence.

**Jon Kowieski:** Once you get to a certain domain rating, yes, you kind of begin to see that influence.

**Jon Kowieski:** Because when you're under, you're essentially looked at as spam.

**Jon Kowieski:** Like, your website is not valuable.

**Jon Kowieski:** And that's why Google to this day still looks at backlinking.

**Jon Kowieski:** ChatGPT somewhat looks at it.

**Jon Kowieski:** Granted, is it possible they're looking, they're just using Google, and just because Google's looking at it.

**Jon Kowieski:** Like, if you have to talk about ways to detect spam, that's probably the number one way.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** But I don't know.

**Jon Kowieski:** Like, I try to think through that.

**Jon Kowieski:** Like, what if people, like, three articles come out and they're basically the same?

**Jon Kowieski:** How do you determine what's the best one and the actual source or something like that?

**Jon Kowieski:** But, but yeah.

**Marcel Santilli:** Cool.

**Marcel Santilli:** I got to run, but, so super quickly, like, what I'd love to do is maybe, like, like, early next week, give you access.

**Marcel Santilli:** I just want to make sure, like, there's a couple of things I want to make sure, like, it's working and whatnot.

**Marcel Santilli:** If you're down for it, for check that.

**Marcel Santilli:** And, and if you want to, right, like, get access and, like, play around with it.

**Marcel Santilli:** And then, like, you know, give us any feedback.

**Marcel Santilli:** I already got some of the feedback you mentioned.

**Marcel Santilli:** So I'll, I'll process this call and, and, like, share with the team and prioritize those.

**Marcel Santilli:** And, and, and then hopefully, and then in the meantime, also, like, this was good feedback for the OS experience.

**Marcel Santilli:** And, like, and I'll make sure, like, you're, like, one of the first customers we ever give access to it.

**Marcel Santilli:** Once we're.

**Marcel Santilli:** Ready to share that access, you know, right now we don't have a way to share access without giving you access to every other workspace.

**Jon Kowieski:** And so like that's in the roadmap, you know.

**Jon Kowieski:** Yeah, that sounds great.

**Jon Kowieski:** Another thing that could be somewhat helpful is something like this by topic or whatever.

**Jon Kowieski:** Just showing share.

**Jon Kowieski:** My C-suite likes looking at this.

**Jon Kowieski:** They like to see how we compare to competitors and this is like one of the easiest ways to do it.

**Marcel Santilli:** So that makes sense.

**Marcel Santilli:** And this matrix view, I've used Profound before, it's just across every prompt, right?

**Marcel Santilli:** Like so if you inserted a bunch of prompts here that had the word Brex in it, you could like, you know, you can talk with it pretty easily, right?

**Jon Kowieski:** Yeah, and I don't track brand.

**Jon Kowieski:** Like I don't generally care, like if we aren't showing up for brand, like actually I might have bigger problem.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** I might have.

**Jon Kowieski:** have like a group set up just for brand, but I'm not trying to measure it.

**Jon Kowieski:** And granted, a lot of the stuff we're doing will impact brand traffic, but I actually do have to hop to.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** And when you give me access, I'll probably jump in when I get a chance, but we got the holiday.

**Jon Kowieski:** So I appreciate it.

**Jon Kowieski:** Talk soon.

**Jon Kowieski:** All right.

**Jon Kowieski:** Have a good one.

**Jon Kowieski:** Bye.
