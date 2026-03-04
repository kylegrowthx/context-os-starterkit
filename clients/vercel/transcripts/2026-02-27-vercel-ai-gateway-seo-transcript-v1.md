# Gateway SEO — Vercel AI Gateway Team Sync
**Date:** February 27, 2026
**Duration:** 31 minutes
**Participants:** George Haikal (GrowthX), Dignory (GrowthX), Marcel Santilli (GrowthX), Jerilyn Zheng (Vercel), Cody Henshaw (Vercel), Josh Wolk (Vercel), Matthew Lenhard (Vercel)
**Source:** Fireflies

---

## Summary

First working session with the Vercel AI Gateway team focused on SEO strategy and competitive positioning. George presented competitive analysis of Open Router and Ollama, identifying gaps in content depth, proprietary data usage, and keyword targeting on existing AI Gateway model pages. The team discussed enriching pages with pricing, performance, uptime, and use-case data while being cautious about exposing raw token volumes (Vercel's scale is lower than Open Router's). Key opportunities include Q&A tabs, model comparison tools, and a leaderboard page. Jerilyn confirmed most data is available live — the constraint is presentation, not availability. Matthew and Jerilyn discussed granting frontend (Next.js) access for programmatic page work while keeping backend console access internal. The group aligned on a phased approach: fix low-hanging SEO fruit first, reach parity with competitors, then differentiate with proprietary data and novel page elements.

## Action Items

**George Haikal:**
- Take a first pass at consolidating meeting transcript and discussion points into a detailed summary document
- Break down all opportunities by competitive URL, keywords, and search volume
- Present prioritized SEO roadmap with ROI estimates and access requirements

**Jerilyn Zheng:**
- Review and fill gaps in the summary document after George's initial draft
- Provide detailed answers on data access and internal capabilities for content enrichment and metric displays
- Discuss internally and coordinate the level of frontend (Next.js) access for external AI engineer

**Matthew Lenhard:**
- Coordinate with engineering on frontend access feasibility and editing rights for AI tooling involvement
- Contribute to establishing SEO keyword targeting and page structure improvements on existing model pages

**Josh Wolk:**
- Continue development of standalone playground with multi-instance model comparison
- Support for publishing user evaluations (future SEO opportunity)

**All Participants:**
- Maintain regular communication via Slack and schedule follow-up syncs as project milestones define

---

## Transcript

### Introductions

**George Haikal:** Hey, Josh, how's it going?

**Josh Wolk:** Good. I just wanted to jump on to make sure everyone get into the waiting room. I have to jump off for another urgent call, but just wanted to say hi.

**George Haikal:** Appreciate it. Sounds good.

**Matthew Lenhard:** Hey, George, how's it going, man?

**George Haikal:** Not too bad. How about yourself?

**Matthew Lenhard:** Yeah, not too bad. Busy morning, but I feel like even bug fixing incidents, but it's been productive to say the least.

**George Haikal:** Is a busy morning on a Friday better than a busy afternoon?

**Matthew Lenhard:** Yes, I'll take a busy morning. Actually. Most days. I think I'd rather have a busy morning. More of a morning person anyway. So, like, I don't know, I'd rather knock stuff out while I'm still on my game.

**George Haikal:** I totally agree. The first two mornings when I have like deep work block early in the morning uninterrupted. It's like my favorite part of the day.

**George Haikal:** Hey, Jerilyn, how are you?

**Jerilyn Zheng:** I'm doing well. How are you?

**George Haikal:** I'm doing great as well. Happy Friday. It's good to meet both of you. I know Cody spoke very highly. So excited to jump in and see how we can help and get to know a little bit better and understand, you know, if you had all the time in the world, what you'd want on the AI Gateway and all of these things. Are you both based in SF as well or no?

**Jerilyn Zheng:** Yeah, we're both in SF. Joshua should also be joining. He's based out of New York.

**Matthew Lenhard:** Josh, he just jumped because he said he had an urgent call. So, yeah, we got like 30 seconds of Josh.

---

### Setting the Context

**George Haikal:** I caught Matthew and Jerilyn up to speed a little bit, Cody. But is there anything top of mind or actually, probably anything top of mind before I kind of jump into the research that we've done this week and our thoughts and then have a ton of questions for you all. So curious about how you're currently working and what you'd love for this to look like and any constraints. So I definitely have plenty to take up all the time. I want to make sure anything that's top of mind for you all or that I could help build context for, I'd lead with that.

**Matthew Lenhard:** I'm excited to see the keyword strategy. So I don't know, I'll let you jump into things.

**Jerilyn Zheng:** Yeah, on my end it's really just like we're very open minded about what we can do in SEO on Gateway and we think there's hopefully a lot. But yeah, I'm curious to see what you think.

**Matthew Lenhard:** There's so many good long tails. I'm excited.

---

### Competitive Analysis — Open Router & Ollama

**George Haikal:** We are as well. And I met with our engineering team earlier this week and basically for a ton of clients in the past, we built out programmatic workflows for things similar to this. Think like Ramp's vendor database where we pulled all the vendors that they work with and filtered, categorized, enriched all the pages. So we're very familiar with different custom programmatic plays. But super excited about this one here. I guess let me just start by showing you the digging around that I did if that's helpful and I'll share this link with you all as well.

**George Haikal:** So a little bit what I did and what we did is look through with the goal of — how can we make the AI Gateway come up for the most common things like O4 mini pricing or best model for X or these general terms. Like how can we make Vercel one of the first options or among the top for developers searching for these answers. And so that's kind of the way we framed how we're looking at this. What we did was look through competitors in the space. Open Router and Ollama are the ones I linked here. Ones that are doing well, have a ton of pages to see what are they doing, what is different right now than the current AI Gateway, and where is the gap that we need to close. One, just to get on their competitive level, but two and more importantly, where's the information gain that you all have that we can build in outside of brand name, because that's clearly one as well, that we can make sure we're winning across the board.

**George Haikal:** And so what I wanted to show you are Ollama and Open Router. There's a few things they do a good job on — specifically the depth of content. They just have a little bit more in almost all of the places. By tab they have pulled in a lot of data — proprietary data on performance, on pricing, on activity, on uptime. And each one of these pages is either cross linked to somewhere else. More models from ByteDance has some more content on every single page. So it just gives you so many more shots on goal. And these are really quality ones because it's backed by their proprietary data.

**George Haikal:** Ollama is another example. Obviously not the exact same thing, but looking at what they're doing — nice flat tagging and filtering across the entire thing. Everything has a nice tag. They're front loading the applications. And when you click, these aren't clickable, which is another option — having Claude Code be its own page within the Vercel AI Gateway that explains Claude Code and cross links versus just linking directly to Anthropic. List out all the different models. The readme. I think the other big differentiator here was on usage and use cases.

**George Haikal:** That's the high level. Okay, they're doing a lot. None of it is impossible for Vercel to compete with. It's more — let's go through all the questions, understand where we want to be competing, what's already in the works, and what in terms of access or data you already have that we can incorporate into building out these new pages.

---

### Proprietary Data & Scale Constraints

**Jerilyn Zheng:** Yeah, I can jump in to start. This is all stuff that we want to bring in and we're actively working on bringing in. So Josh has already built out charts around throughput and latency and we're working on uptime right now. The biggest call out I have right now is in terms of our proprietary data. We haven't felt comfortable showing the actual token numbers yet because our scale is lower than Open Router so we don't want to have a direct comparison. So usually most of the time when we do things like leaderboards, it's in terms of percentage of total traffic rather than a hard token number. And we would like to show token numbers, but we basically have to reach enough scale where it makes sense.

**Jerilyn Zheng:** There's a little bit of a problem there — we actually have really useful data. It's just that the scale of data isn't at the level of Open Router. So we don't want to surface that until we are at similar scale to them. Because I think that'll be the first thing that gets called out. And then in terms of the apps too, we want to link more to our apps and customer apps. Sometimes our customers aren't comfortable with showing their token volume. But yeah, I think data here and just being like, if you have interesting data, showing that to people will result in a lot more clicks and useful information on the pages. And it seems like we have it. It's just — we want to show it in a way where it doesn't expose us, essentially.

**George Haikal:** Yeah, that's helpful. I think there's a lot of great things we can do in the meantime without exposing that. A lot of really cool things that I've seen that I would love to explore — like best use cases by model. Or what are different apps using different models for? That was a really cool view. And you can imagine the search volume there. Coming out of this conversation, once we get a better understanding of what's possible, we'll break everything down by search volume as well. And where the highest impact, lowest complexity opportunities are by search volume.

---

### Keyword Targeting & Long Tails

**Matthew Lenhard:** I had a question. So basically the head term is the model name and then the long tail keywords you'll target underneath are like, what — pricing, uptime? Well, I guess what are the core long tails on the model pages?

**George Haikal:** Yeah, pricing, uptime, performance. We can even go use case long tail as well. Basically whatever you all have access to — what internal data you have access to that you're comfortable sharing or exposing — we can tailor for each one of these pages. But if the data is there, we can do everything Open Router is doing and more in terms of every single one of these tabs, we can make it better. We can break it down by use case. Common questions people are asking for each model as well. Like a Q&A tab around each model. So the highest volume and highest intent questions people are asking around Opus 4.6, for example — that could be another tab within the clickable model here.

**George Haikal:** Because right now, this is good and valuable and you're getting some traffic, but there's just so much room here to build and enrich and enhance.

**Matthew Lenhard:** Are they missing long tails on their model keywords? Open Router. Like, I saw they have pricing, performance, uptime.

**George Haikal:** I mean, it's thin. The content's thin. They have, you know, they're hitting a few of the good ones. But it's not like each one of these pages is extremely enriched or valuable. But it is getting pulled into answers and we're going to break all that down.

**Matthew Lenhard:** Do they have comparison keywords? Open Router. Like, are they doing X model versus Y model? Probably not.

---

### Open Router Comparison Tool

**George Haikal:** Yeah. So they have this comparison tool here, which we're going to talk about today. This is on Open Router Compare. You can select the different model types and you can stack them against each other.

**Jerilyn Zheng:** Josh, this reminds me of what Tom built out for the new revamp of the model page.

**Matthew Lenhard:** What does that populate to the URL? Are they ranking these pages individually?

**Matthew Lenhard:** Have you looked at this subfolder on Ahrefs to see how much volume they're getting compared — like, how many of these are indexed and how much traffic the subfolder is getting?

**Josh Wolk:** I was wondering the same thing. I know like, for instance, one time I built out docs for a little side project and I had like a thousand pages and I was hyped about that for SEO — none of them were getting indexed.

**Matthew Lenhard:** Yeah, that's the problem with programmatic. You really have to lean on domain authority.

**George Haikal:** That will all break down as well. I'm less concerned about that, but more like — that is a really good experience for someone who's actively trying to compare these tools, and we can even make that easier for the user to reach.

---

### Playground & Evaluation Features

**George Haikal:** Do you have usage data on how many people are actually using the playground on each one of these model pages?

**Jerilyn Zheng:** Yeah, we should. We have the user agent and how much of this is coming through. I don't know if it's that much. Josh can speak more on the playground too, because we actually want to build out a dedicated playground where you'll be able to run multiple instances of each model and have a live comparison the same way Open Router does. We're cooking on something there.

**Jerilyn Zheng:** But I think we still want to keep the individual model page playgrounds too, because that's valuable from an experimentation perspective and maybe from SEO as well.

**Josh Wolk:** And also a goal is to allow people to publish their evals. So that should hopefully be a good path to SEO. But that's all in the future, so I wouldn't focus on that until we have it.

**Matthew Lenhard:** There's probably a ton of good eval keywords.

**Jerilyn Zheng:** Yeah, evals is probably a later thing. But right now, in terms of playground overall, we also have a lot of just random v0 or different apps that have been built off of AI Gateway, and I think an idea was we could showcase those and that would help a lot too. There's one thing that's kind of going viral right now, which is the v0 Grok Imagine playground that someone from Vercel built out and Elon tweeted it. So it's been going kind of gangbusters.

**Matthew Lenhard:** Do we link back from theirs?

**Jerilyn Zheng:** I don't think so. We don't have anywhere to. It says Powered by AI Gateway on it, but I don't know if we have anything on our site linking to it.

**Matthew Lenhard:** That's probably a pretty powerful link.

**George Haikal:** Yeah, that would be pseudo gold right there.

---

### Page Structure & Access

**George Haikal:** How flexible are you all in terms of this experience now? Like, the structure, how everything's set up, the context? We have a designer / Framer — really great. He does a lot of our programmatic tools and custom web work, and so happy to get him some time here to experiment with different ways of visualizing this. It's all depending on what your constraints are now and how you're currently pulling everything and publishing these pages. But just curious on the flexibility there.

**Jerilyn Zheng:** I think we're flexible. Josh, what do you think? Josh is kind of cooking on some stuff here too, so I'll let him decide more in terms of what we're prioritizing with the model pages.

**George Haikal:** I'm thinking through — what level of access could we give our AI engineer who handles the programmatic work? Or would that all go through your team and we would kind of just provide it to you in a specific way? Have you thought through that or dealt with that before? We're happy to do either. Obviously it's easier if we can get plugged in, but open to your thoughts.

**Matthew Lenhard:** I mean, probably wouldn't give them access to the console. Jerilyn, we'll probably regroup on this, but we could probably give them access to Front.

**Jerilyn Zheng:** Yeah, I think it would be like access to Front. And then if you wanted to redesign the page, then it would just go live as soon as we publish. The context is that right now the pages automatically generate when a new model comes out. We usually have some heads up so we'll be ready to go. And then as soon as we toggle the model to work in AI Gateway, then the page in Front will also appear. And so everything goes live at the same time within minutes of the model showing up. So if we have a template edited, then that would be good.

**Matthew Lenhard:** Yeah, Front is just a Next.js app. So I would ask the engineering team if they're fine — they wouldn't be able to touch the underlying data store, but could probably give them access to the Next.js app where they could make changes. We probably have to talk to other people on the team to see what level of access we're allowed to give.

**Jerilyn Zheng:** Yeah, we can talk about it. I think the console probably doesn't make sense because it's just the underlying data. Like, it'd be us adding in prices or adding in the description. So if you wanted to edit the description or something like that, you could just let us know beforehand — like, you should put in these words in the description, or make it like this. We literally usually just copy and paste from the provider, which is the same way that Open Router does it. So in terms of the content there — if you just let us know, then we can make those changes live. But in terms of the actual structuring and things like that, yeah, I would go with Front access rather than console access.

---

### Leaderboard Opportunity

**Jerilyn Zheng:** I actually had a question on the leaderboard side. Not like the SEO perspective, but we've been hearing a lot from customers or just marketing people that the Open Router leaderboard is a really big driver of their traffic. And in terms of just everyone looking at the source and being like, wow, this model has trillions of tokens today. And, you know, saying like, we are continuously growing in the AI space because of the model leaderboard. It's not even showing up, I guess, if you search it, but if you look up Open Router leaderboard, that goes viral on X fairly often. And then on our end, when we've been talking to other people about it — we don't have the token volume that they do. So we don't want to surface the exact same leaderboard, but I'm wondering if there's anything we can do here to make it better from an SEO perspective.

**Matthew Lenhard:** What's the keyword? Is AI model rankings? Is that the top term?

**George Haikal:** This leaderboard page is doing as much as Vercel's Gateway as a whole. But I mean, to me, I see this — this is totally winnable. My eyes are lighting up. This is everything we're seeing on models and pricing next to it. Every single model, every variation with the word pricing or costs. There's just so much room. I mean, Reddit is fifth on the list. Obviously having a face could be a little harder, but this feels wide open for improvement. These are not great experiences or pages at all. Nothing's even clickable.

**Matthew Lenhard:** Yeah. Vercel is going to be able to rank just based on domain authority alone.

---

### Priorities & Low-Hanging Fruit

**George Haikal:** I guess what might be even more helpful is some answers to these questions. It sounds like we're flexible enough in terms of page structure. So if we recommend or come with a few different variations — one within the existing constraints and then a few different ones — it doesn't sound like that is going to be a massive issue, especially when we justify it based on search.

**Matthew Lenhard:** I want to make sure we're targeting all the correct head terms and long tails on all the pages we already have. I feel like that's such an easy win. Like I haven't looked but are the model pages hitting the correct H2s, H3s for the long tails? Is page structure fine? That's at least me.

**Jerilyn Zheng:** Yeah, I think let's start with the lowest hanging fruit. And then we have aspirations for all of these things and they're kind of in mind. But even just based off of our existing state, if there's super simple changes we can make.

**Matthew Lenhard:** First off, like, do we have a title tag? There's probably a lot of small things that we haven't even looked at.

**Jerilyn Zheng:** And then after that it's like, which of the things that you listed here would be the highest ROI? Because then we can dedicate more capacity to that. We have a million different priorities and we want to do all of them. But if you let us know this is going to be an immediate improvement, then we will start there.

---

### Phased Approach & Next Steps

**George Haikal:** Completely aligned. I think table stakes is getting to the same level as an Open Router or Ollama. And we can do that very easy just by enriching the pages, building it out programmatically and adding a few sections. And then that's where we're already going to focus most of our time — let's get to that level and then figure out how to skyrocket beyond it with all the proprietary stuff that Vercel has and how to visualize it and then building out different sections that nobody has yet. Like best use cases for this type of model — there's just so many variations. So we'll put that all together and show it to you all. This is what we want to do, here's why, here's how long it's going to take, here's what we need in terms of access.

**George Haikal:** On our end, we have one AI engineer dedicated to this full time and he can basically programmatically build out all of these pipelines, which is why I was asking about access. Understood if we need to talk to you — hey, change these portions. But we're also super happy handling it ourselves as well eventually, if that makes it easier for you all.

**George Haikal:** So what I'll do after this is go through, and if any of these questions still need clarity from our engineering team, I'll just reach out and ping you all if that's fine just to clarify them. But to me it seems pretty clear — let's get to equal ground as the competition and then in doing that, let's build the foundation to go far above and beyond. And then here are the three or four bets we're going to make now for the next month. And what are the highest impact based on actual search volume and keywords that we're targeting.

---

### Communication & Collaboration

**Jerilyn Zheng:** And then how do we make this collaboration as easy and effective as possible? Is it like we just communicate a lot in Slack? Should we set up a sync every so often? What is the best way to work with each other?

**George Haikal:** Yeah, it's a good question, Cody. That's probably valuable for us to think through as well. But at the very least, we're going to run this in parallel to /i and these other lanes that we're working with you all on. But we're running it as its own project as well. So we can talk in Slack. We'll give really constant updates, and we can meet on a frequent basis as well. I think for now it probably makes sense to meet at least weekly or bi-weekly. But let me scope out everything, understand what questions we still have, and present the project, and then we can figure out what cadence makes sense. But in short, I'm always available over Slack, so is our team. And in the interim, before we set up and formalize something, for any questions we'll shoot things over.

**Jerilyn Zheng:** Sounds good. Do you want for next steps — do you need me to update anything in the doc? Because I'm happy to answer any questions or provide more specific details here. If you want me to take a pass at it or if you think you're good to go without it, let me know.

**George Haikal:** Let me take a first pass with the transcript and with what we talked about, and then I'll shoot it over to you and then any gaps you can fill.

**Jerilyn Zheng:** Awesome.

**Matthew Lenhard:** Appreciate you all.

**George Haikal:** We'll be in touch soon. This is exciting. Let's go.

**Jerilyn Zheng:** Thank you.
