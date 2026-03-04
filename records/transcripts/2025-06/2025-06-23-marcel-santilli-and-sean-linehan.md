# Marcel Santilli and Sean Linehan

<metadata>
date: 2025-06-23
time: 20:35 UTC
duration: 30 minutes
organizer: Andi Bailey
participants: Marcel Santilli (GrowthX), Sean Linehan (Exec), Andi Bailey (GrowthX)
fathom_recording_id: 70016385
fathom_url: https://fathom.video/calls/331932508
share_url: https://fathom.video/share/7sFxc98ZY-oa65VAsZb6ry4mtRshvA7r
source: fathom
enriched_on: 2026-03-03 12:30 UTC
</metadata>

---

## Summary

Marcel and Andi caught up with Sean Linehan (CEO of Exec) to review GrowthX's content delivery and Exec's remarkable success in LLM visibility—dominating their AI roleplay category through fresh, long-tail content production. The team discussed how GrowthX's focus on personalized, frequently-published content aligns with Exec's ambition to expand search TAM by 10x through LLMs, and explored a major expansion: GrowthX building 200+ customized use case landing pages (targeting specific roles, industries, and company sizes) for Exec's new self-serve flow, complete with AI voice agents and workflow automation.

---

## Context

Exec is an AI roleplay and practice platform that helps sales teams, managers, and enterprises train with AI agents. Sean Linehan, Exec's CEO, has known Marcel for five years and originally partnered with GrowthX to drive SEO results and explore a larger vision: ranking Exec's content in LLMs through long-tail content production—a strategy that's now paying dividends as LLMs expand search TAM and favor fresh, personalized, niche content. Andi Bailey recently joined GrowthX to lead customer operations and is conducting partnership feedback calls; this call served both as a satisfaction check-in and a strategic planning session for a major new expansion opportunity.

---

## Relevance

**To GrowthX Delivery:**
- Exec's success demonstrates the power of high-velocity, long-tail content production for LLM visibility—key operational methodology GrowthX can replicate for other clients
- Elvis and Nem are the core drivers of Exec's results; Sean specifically praised their creativity, engagement, and execution, suggesting strong product-market fit in the delivery model
- Opportunity to scale the VAPI voice agent + landing page workflow (already proven on VAPI) to Exec's custom use case pages (200+ planned pages)
- Technical decision point: Exec prefers Postgres + admin panel over Contentful CMS for scalability—relevant for future high-volume deliverables

**To CheckThat:**
- Exec uses Profound (a competitor to CheckThat's competitor Crunch) for LLM visibility tracking; Exec sees this as critical infrastructure for the future of search
- GrowthX has Crunch data integrated and could potentially integrate Profound as well; Sean noted Profound is funded by one of Exec's investors
- LLM visibility tracking is now table stakes for high-growth B2B—strong market signal for CheckThat's strategic direction

**To GrowthX Business Development:**
- Account expansion: Exec is moving from content-only engagement to a major platform/page generation engagement—potential $50k+ expansion opportunity
- Renewal signal: Sean explicitly stated "I'm pretty satisfied" and sees GrowthX output as "at least as good as in-house"; high reference potential
- Customer success: Exec went from "no visibility" to "dominating our category"—strongest case study narrative available
- Market momentum: Exec's success in LLM ranking is happening in real-time and is differentiated from competitors; GrowthX is the engine

---

## Overview

- Exec is seeing strong results in LLM visibility, dominating their category for AI roleplays
- GrowthX's content strategy aligns well with Exec's goals for long-tail content and LLM ranking
- Potential collaboration on creating customized use case landing pages for Exec's self-serve flow
- High satisfaction with GrowthX's work, particularly praising Elvis and Nem's contributions

---

## Key Topics

### LLM Ranking Strategy

  - Exec's goal: Rank in LLMs through long-tail content production
  - Using Profound (competitor to Crunch) for LLM visibility tracking
  - Seeing dominance in their category, attributed to:
      - Focus on new, frequently published content
      - LLMs' bias towards fresh content
      - Expansion of search TAM by 10x due to LLMs' ability to handle complex queries

### Content Performance and Strategy

  - Customers attributing finds to SEO
  - Focus on roleplays niche showing success
  - Statistics-type posts getting good engagement
  - Content serving as both direct conversion and brand touch for enterprise sales
  - Plan to create self-serve flow with customized use case pages
      - Targeting specific roles, industries, and company sizes
      - Aiming for highly personalized content

### GrowthX's Performance and Value

  - High satisfaction with GrowthX's work, particularly Elvis and Nem
  - Praise for engagement, creativity, and execution
  - Content quality and results meeting expectations
  - Output comparable to in-house team, though slightly less in volume

### Future Collaboration Opportunities

  - Potential partnership on creating customized landing pages for Exec's self-serve flow
  - Discussion of using Supabase instead of Contentful for better scalability
  - Consideration of integrating voice agent functionality on landing pages
  - Exploring ways to generate highly detailed prompts and configurations for different use cases

---

## Action Items

**Marcel Santilli**
- Schedule demo of GrowthX platform & workflow engine for Sean re: custom use case page generation

- Prepare proposal for GrowthX to create Exec's custom use case pages (incl. content model, workflows, QA process)


**Sean Linehan**
- Prepare database integration plan for custom use case pages (Postgres DB instead of Contentful)

- Design custom use case pages for self-serve flow (sales onboarding, manager development, new product launch training, etc.)

---

## Transcript
**Andi Bailey:** A little bit late, but this meeting is being recorded. Get us started. I lead customer operations for GrowthX. I've been here for about a month. So I'm jumping into these feedback calls with Marcel to get an understanding of how our partnership is going, thinking about process, how you're measuring and thinking about our deliverables, where we can improve. So there are no wrong answers and you can feel free to be as candid as you want to be on these calls. That's the purpose of these sessions. I'd love to learn a little bit more about you as a partner. What would you like me to know about you?

**Andi Bailey:** So I'd love to know how you found out about GrowthX and the strategy that Exec is thinking about as you're approaching our partnership, and maybe the focus of your role.

**Sean Linehan:** I'm a CEO and I do everything. I've known Marcel for like five years. Marcel has been very helpful for me in SEO in particular over the years. He taught me how to run a human-driven publishing operation a number of years ago, which I operationalized for my previous company. And then he started GrowthX and I was like, yeah, let's do that.

**Andi Bailey:** Was there any specific goal when you started working with us that you were trying to solve, or where were you guys in the business evolution?

**Sean Linehan:** Yeah, I actually just did a call with your case study team about all of this. But my goal—the TLDR is that the banner headline is SEO, but I actually had a bigger vision around ranking in LLMs, which is now becoming popular with all the recent fundraisers. The real goal is that SEO is good—I've been doing SEO for 15 years—but I was really excited about the opportunity of producing long-tail content that would get us ranked in LLMs.

**Marcel Santilli:** What up, dude? It's so good to see you. Sorry I'm late—I was wrapping up with a customer kickoff that ran a bit longer.

**Sean Linehan:** Welcome to the party.

**Marcel Santilli:** You got to drop by our office sometime, man. If you want to come by, even if you just want to drop by for the first hour of the dinner, that works too. It's in LA, but I know it's kind of far. If you wanted to drop by on Wednesday...

**Sean Linehan:** Yeah, I might do that. I have a 4:30, but maybe I'll swing by. I was going to show up to your office warming thing, but I got completely destroyed by work.

**Marcel Santilli:** All good, man. All good. But we're here. This week, all the directors are here starting today. Andi's here too. So if you're walking by anywhere at any point, just drop by. By the way, how big is the company now?

**Marcel Santilli:** We're like 60, 65 people.

**Sean Linehan:** That's insane.

**Marcel Santilli:** Yeah, it's been nuts. But if we have a few minutes at the end of the call, I want to show you the platform and what we're working on behind the scenes. We're officially 100% off offshore resources and I think it's pretty cool. And then later on, we can grab some time. I'd love to get your feedback.

**Marcel Santilli:** But sorry, Andi, didn't want to cut your flow.

**Andi Bailey:** No, all good. I think that was actually a really good time for you. Sean, was that context about the case studies from the call with Mara and Elvis from last week?

**Sean Linehan:** No, I did a call with whoever's writing your case studies.

**Sean Linehan:** Genevieve.

**Marcel Santilli:** That's right. Yeah, that's a new thing we're doing.

**Andi Bailey:** All right, perfect. So we have a lot of context.

**Andi Bailey:** So I'm curious—you said you had a bigger vision around ranking in LLMs, and given where we are now, how are we executing against that piece? Do you feel like we're getting there?

**Sean Linehan:** Yeah, pretty good. I shared access to a platform we use called Profound for LLM visibility tracking. Profound is funded by one of our investors and they just raised a big round. I think it feels like the clear place the future is going. They started as full service but became a visibility tool—like a Semrush or Ahrefs for LLM platforms. I shared this with you a while back, Marcel—I figured you guys might compete somehow.

**Marcel Santilli:** Super quick—just so you have context, we have data for one of their competitors, Crunch. They're the only one with APIs and they all get data from the same place because VCs were asking us about it. Profound went from charging $3,000-4,000 a month down to $500 a month because Crunch is $500 a month. We have data for Crunch and it's already included in what you're getting. We're integrating it all now. But if what you're using is working, hopefully you can save that $500 a month.

**Sean Linehan:** I don't have huge love for Profound, but I got a sweetheart deal when they launched so it's cheap. I gave Elvis access and he's been using it to monitor our competitors and see what articles are showing up for our keywords and queries. It's a bit fuzzy since it's not actual analytics—they're running queries against the engines—but Elvis has been really good at adapting to what we're seeing and winning on that. We went from basically no visibility to being dominant in our category. And we're just really early. The stats show that LLMs are strongly biased towards new content, and we're only producing new content. We're publishing a lot and frequently, which is also very helpful.

**Marcel Santilli:** It's almost like the early days of Google, where you could refresh your content every day and iterate. Right now we're in a phase where the more personalized, long-tail, and fresh content you have, the more likely it shows up as a solution in an answer. For example, if you search for "voice agent," you won't rank, but "voice agent for wellness clinics" where you're the only page hitting that intent—you'll be there.

**Sean Linehan:** Exactly. The way I frame what's happened here is that LLMs have basically expanded the TAM of search by 10x. That hasn't fully materialized in the numbers yet, but I think it will. The way it's done that is by expanding the number of queries you can ask that you'd never ask before. Instead of being limited to four keywords and 10 blue links, you can now type a whole paragraph and it figures it out. The TAM for extremely long-tail content went from effectively zero to not effectively zero. You just have to produce a lot of long-tail content. And the only way to do that meaningfully is with LLMs, which is funny—you have to use that because otherwise you can't afford to produce insanely nuanced long-tail content for the five users a year who'll see it.

**Marcel Santilli:** And the way you talk about your product in that long tail has to be very different, nuanced, and personalized. You still need to apply the knowledge and context of your company, product, and use cases to it. It's not just good content—it has to be good content on brand, with the knowledge of what your company actually does.

**Sean Linehan:** Yeah, and your unique POV, because that's the critical thing. What are we bringing to the table other than generic stuff? We're bringing our point of view. That point of view, our brand, product, and offerings are all guiding the ultimate output that answers the user's query.

**Marcel Santilli:** Yeah, that makes sense. Andi, I'll let you keep going. I have a few things I want to ask too, but let me know if you have anything else.

**Andi Bailey:** So I'm curious to see that we're responding to your pushes for us. But how do you feel we're doing in terms of leading the strategy? Is there anything that you wish we were doing differently or had done differently in the evolution of our partnership?

**Sean Linehan:** I'm pretty satisfied, to be honest. Elvis is good. I like him. We've had a couple other people pop in and out, but Elvis is pretty much the guy. I don't know that the other people in the meetings have done much. Not that they're bad people, but Elvis and Nem are my guys—they do the work. I don't quite know what the other people's roles are supposed to be. I think Elvis does a pretty good job. He's really engaged, creative, and coming up with more keyword strategies. We spend a lot of time iterating on visuals and tone. I don't have any complaints on content quality. We're seeing results. I feel pretty good about it. It's at least as good as I'd expect from somebody in-house. I'd expect more output if they were in-house, but that's the nature of the beast. And I'm happy with the output we're getting.

**Marcel Santilli:** So no real complaints.

**Andi Bailey:** Love to hear that. Before you jump into the demo, Sean, what are you thinking of and prioritizing in the next three to six months in terms of your strategy?

**Sean Linehan:** More of the same. We've been really focused on our roleplays niche, which is very important to us. We've done a lot of good content around roleplays—we're showing up big time for roleplays. We've done some good statistics-type posts, which are getting good play. Customers are mentioning they found us through SEO. That's direct attribution. I'd say overall, this work is closer to a brand touch than a direct conversion funnel for us because we're doing big enterprise sales. But some do convert, which is interesting. We want to do more landing page type content. Actually, this is interesting—I want to share something with you all. We were planning to do it in-house, but there might be a way for you all to help. We're basically creating a self-serve flow. Right now we mostly sell to big companies with hand-to-hand sales-led deals, but we're planning to launch an end-to-end self-serve flow. At the top of the funnel, we want to create super-customized use case pages—like "sales onboarding for mid-market pharmaceutical companies." At that level of niche, where we're talking about the Exec platform in the context of a functional role and use case we solve. Things like sales onboarding, manager development, new product launch training. There's about a dozen of these. Then there are industries and company sizes. We basically want to generate all the permutations, speak the language of our buyer, and have all the examples on the page customized.

**Marcel Santilli:** That's literally everything we've done for VAPI.

**Sean Linehan:** Yes, please. I'd love to see it because we were going to do it ourselves. We have a landing page we're designing, but it would be better if we didn't also have to figure out all the content to put through that pipe.

**Marcel Santilli:** We design and build these pages, build custom workflows, QA them, launch them. This is the index page of all these agents. You click healthcare, for example.

**Marcel Santilli:** We should definitely make this for Exec. Here's an example—an AI voice agent for account activity queries. The agent says, "Hi there, I'm Ava. How can I assist you with your account activity today?" And if a customer says, "Hey, I saw this random transaction. What's going on?" the agent responds, "I understand that sounds frustrating."

**Marcel Santilli:** Did you guys also generate the prompt that drives this? We generated the full JSON—the configuration and the basic prompt. They already had some of it built, so we mostly built the UI. Everything here is extremely specific. For example, this banking page says "banks often struggle with limited resources to address every customer query," while the Wellness Clinic page says "healthcare providers often face constraints in terms of time and human resources." Every part of it is personalized—like the compliance language shifts from "adhere to strict privacy regulations" to "prioritize user confidentiality with compliant data handling." We've done 200 of these pages, and we have 2,600 more ready to go. We're just consistently requesting indexing and creating index pages. But the really cool part is the workflow behind it—this is our workflow engine. It does all of these things in parallel. Let me show you the VAPI example. It's literally the same inputs: use case, category, industry, context.

**Sean Linehan:** It's literally the same thing.

**Marcel Santilli:** Yeah. You could say "hospital front desk" or anything like that. I haven't run this workflow yet, but we batch it so it goes through everything. Live demos are scary, man.

**Sean Linehan:** Totally.

**Marcel Santilli:** This voice agent answers calls with sensitivity and understanding, and here's the simulator, the configuration, the feature pages, the about section, and then a CSV export.

**Sean Linehan:** Yeah, this is great. We'll partner with you on it. We want to do it for these industries, research what's important to those industries. The thing we haven't figured out is how to hook it up to our CMS. We use Contentful for everything—it's our blog platform.

**Marcel Santilli:** Contentful is fine, but it gets expensive. We hooked this all up to Supabase instead. You can point a directory to Supabase, which makes it a lot easier. We connect Supabase to Airtable. With hundreds of pages, you probably don't need this, but with thousands of pages, headless CMSs become a nightmare. You have to figure out which pages to statically generate when you're modifying hundreds every day. Your build times get crazy, and you hit API limits. Most headless CMS APIs are super limited—they can't handle 5,000 pages being updated daily.

**Sean Linehan:** Actually, for this use case, the content is all in our blog via Contentful, and that's not changing. But for these pages, we'd sync to our admin panel and could give your team a login to update just those pages directly in our Postgres database. Our website is already hooked up to our Postgres database.

**Marcel Santilli:** Yeah, that's perfect. We'd do the content model to mirror your database, the workflows fill out all those fields, and we build a QA process on top. Let's say the QA is in Airtable—we can batch if needed. Once done with batches, we export and give you CSV, JSON, XML, whatever. We can upload it ourselves. The only hard part is if it's one-by-one, but batching works great.

**Sean Linehan:** I love it. So we need to get those pages designed. What's cool is that on those pages, we think the entry point is "create a custom roleplay." Users start on the page, like "start making a sales onboarding roleplay" or "build an objection handling roleplay." Then to try it out, they build the thing, and when they want to play it, they give us their email.

**Marcel Santilli:** So is the idea for it to be a fully functioning voice agent—the product experience—on the pages, or something else?

**Sean Linehan:** We haven't decided. It's expensive, but high value. We haven't decided if it's a voice agent or a text input box yet.

**Marcel Santilli:** Andi, I know you might need to jump, but let me show you something. This is a huge lesson learned—super early stage, but look at these click-through rates.

**Sean Linehan:** Yeah, those are crazy.

**Marcel Santilli:** This is a brand new section of our site. It's insane.

**Sean Linehan:** That's funny—Exec actually uses VAPI, which is our underlying voice infrastructure.

**Marcel Santilli:** No way. You know the team?

**Sean Linehan:** Yeah, I have mixed feelings about them. Their product is useful but has some issues. I was actually talking with DeepGram about this. I think you might have introduced me.

**Marcel Santilli:** I went to college with their VP of Product, Natalie. Yeah, I introduced you two. But DeepGram isn't good enough for some use cases. It's a bit too DeepGram-specific and not platform-agnostic.

**Sean Linehan:** Yeah, I'll learn from these pages because this is basically what we want to do. I feel like this is the way of the future.

**Marcel Santilli:** Here's what's really cool about this approach. When you're targeting zero-volume keywords with a fully functioning tool, the signal you're sending Google is incredible. If someone spends 10 minutes on your page, Google sees that as a massively valuable page. That's why tools perform so well. But you're essentially programmatically creating tools with custom configurations.

**Sean Linehan:** Exactly.

**Marcel Santilli:** Here's the really cool thing—we built a prompt generator for Bolt. For Bolt, we built starter kits where you give it a simple input like "tool builder, website, whatever," and the output is an insanely detailed prompt for building an entire end-to-end app. We built one for Augment Code where you input cursor rules and it generates full documentation. We can apply this approach to anything, but the uniqueness is the voice piece—the know-how that you have that we apply to our workflows to get from use case all the way to a fully functioning configuration, plus page, plus experience.

**Sean Linehan:** Totally. Yeah, we're definitely interested.

**Marcel Santilli:** I appreciate the partnership and friendship. I value the relationship so much, and I'm glad you're having a good experience. Whatever I can do to continue being helpful, just let me know.

**Sean Linehan:** Yeah, we're definitely happy. These things take time. Our SEO isn't getting tons of traffic, but we are hearing results. We're dominating mindshare. Our category of AI roleplays is increasingly hot, and we're winning on the mindshare side. We can't rest on our laurels—we just keep going.

**Marcel Santilli:** Let's crank, man. Let's crank. Well, let me know if you want to come by for the dinner or anything. I totally get it—we've all got a lot going on. The team is on site this week, and I'm doing team building. I'm trying to be home by 4:30 but I'm always running late. I leave the house at 6, get to the office by 6:30, and try to leave by 4, which is a pretty solid day. Then if I can, after we put her down, I try to get a little more work in. Some days I just give up and plan to get up extra early tomorrow.

**Sean Linehan:** I can only do one thing a week. I've got a six-month-old at home, so it's tough. My wife lets me work until 6, but I'm usually not home by then. I basically work 7:30 to 6.

**Marcel Santilli:** Yeah, I'm right there with you. I'm glad everything is going well. Let's exchange notes and stay in touch. Good to chat with you. I'll talk to you soon. Take care.
