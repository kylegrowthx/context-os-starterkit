# Marcel Santilli and James Winter

<metadata>
date: 2025-12-29
time: 21:30 UTC
duration: 36 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    role: Founder & CEO, GrowthX
    email: marcel@growthxlabs.com
  - name: James Winter
    role: Partner, investor in portfolio companies
source: fireflies
fireflies_id: 01KDHFVJ9M8CNZH5RTRWA1AFKS
transcript_url: https://app.fireflies.ai/view/01KDHFVJ9M8CNZH5RTRWA1AFKS
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Marcel showed James GrowthX's unreleased AI visibility index (CheckThat), a B2B buying category data platform with $200k/month investment across 168 categories, editorial prompt curation, and sampling methodology. James agreed to test with his portfolio companies and raised valid concerns about prompt determinism as LLM behavior changes. Marcel will enable multi-tenancy access and James will send a company list for account setup.

---

## Context

Marcel and James are long-time friends and collaborators. James is a successful investor and operator with deep experience in B2B software and growth, currently advising 4-5 portfolio companies after wrapping up a VP role at Engine. Marcel reached out to show James GrowthX's new unreleased AI visibility index product (CheckThat) in early beta, seeking feedback from someone with strong technical judgment and multi-company exposure. This is a trust-based advisory relationship — James's perspective on deterministic tracking challenges and multi-company needs directly shapes product decisions.

---

## Relevance

**CheckThat / AI Visibility Index**
- Early user feedback and multi-tenancy testing with real portfolio companies
- Validation of sampling methodology vs. deterministic prompt tracking concerns
- Feature requests: experiment tracking and visualization over time (inspired by X Funnel)
- Go-to-market strategy refinement with early trusted advisor

**GrowthX Services**
- James runs multiple portfolio companies that could benefit from AEO content strategy and visibility tracking

---

## Decisions & Commitments

- Marcel will enable multi-tenancy feature on James's account for CheckThat
- James will send list of companies for account creation by GrowthX
- Marcel will reconnect in the new year to gather feedback on platform usage and features
- James will test the platform across his portfolio companies and provide critical feedback

---

## Open Questions

- How will CheckThat handle the evolving personalization of LLM results over time?
- Should experiment tracking UI be built in as a core feature for visibility correlation?
- How will multi-tenancy account structure work with different company profiles and data access?
- What's the go-to-market strategy for selling data licenses (e.g., to G2, Webflow)?

---

## Overview & Key Topics

- **Personal life updates**: Marcel's daughter (2.5 years, multilingual household), James's wedding in April with 80-100 guests
- **James's career move**: Wrapped up VP role at Engine (30M budget, 15 direct reports) after inheriting trauma-affected team; now spreading time across 4-5 portfolio companies
- **CheckThat platform**: GrowthX's unreleased AI visibility index
  - $200k/month data investment
  - 168 B2B buying categories
  - Editorial prompt curation + automated generation
  - Sampling-based methodology vs. deterministic prompt tracking
  - Admin panel with brand flagging and prompt management
- **Data infrastructure & tools**: EXA, Tavli, Gina (spending $45k of $150k credit), X (6-month testing)
- **Competitive context**: Peakfail, X Funnel (acquired by HubSpot), 170+ vendors in visibility space
- **Investor validation**: Webflow and HubSpot have licensing interest
- **James's concerns**: Prompt determinism degradation, personalization effects, buyer behavior variance across companies
- **Product roadmap**: Public launch in ~2 weeks, multi-tenancy setup, experiment tracking UI as future consideration

---

## Action Items

**Marcel Santilli (GrowthX)**
- Enable multi-tenancy feature on James's account for CheckThat
- Create accounts for companies once James provides list
- Follow up in early 2026 for platform feedback and usage data

**James Winter**
- Send list of portfolio companies to Marcel for CheckThat account setup
- Test platform across companies and provide feedback on usability, feature gaps, prompt accuracy

---

## Transcript

**Marcel Santilli:** What's up, sir?

**James Winter:** What's going on, man? Merry Christmas.

**Marcel Santilli:** You too, man. I feel like it's been a minute.

**James Winter:** Yeah, no kidding. How's the kiddo doing?

**Marcel Santilli:** Good. There's like set that age now, two and a half, where it's just slightly harder until it gets hopefully a little bit easier or maybe not. She has like more days where they're like cranky. But overall, she was a good baby and super happy. Talking a bunch and all that stuff.

**James Winter:** Are you guys also pregnant again?

**Marcel Santilli:** No. No, we were IVF, so we're probably one and done.

**James Winter:** Catch me up in the throes of wedding planning. Our wedding's in April, so still got some stuff to figure out.

**Marcel Santilli:** How many people?

**James Winter:** Probably we're trying. We have to be under like a hundred, so it has to be pretty small, which is kind of the goal.

**Marcel Santilli:** That's good. That's good.

**James Winter:** We're basically booking out this like small hotel, and it's got like 19 rooms, nothing crazy. We're booking that out for like Friday, Saturday, Sunday. So we're gonna have the wedding on Saturday. Big pool party, beach party on Sunday, and then people fly on Monday.

**Marcel Santilli:** That's awesome, man. The crazy thing is the day of goes by so freaking fast. That's why I'm trying to be in the moment when it arrives. Because it's just gonna go by so fast.

**James Winter:** That's why I'm so excited to do like the pool party the day after. Because that way we get the ceremony and all that out of the way, and then Sunday, everyone can just hang and have fun.

**Marcel Santilli:** We did courthouse in January, and then we did a reception in Dearborn, Michigan. We paid under ten grand and gave her no budget. It was just a hall with a bunch of good Middle Eastern food for like 125 people.

**James Winter:** I feel like I'd have a hard time picturing two cultures that would clash more poorly than Brazilian and Middle Eastern.

**Marcel Santilli:** Yeah, she's Lebanese, and so it's like you have the old school boater mentality, and then the cousins don't care kind of. But like the old school people are just kind of formal. Brazilians, we hug. And in Middle Eastern culture, women are not supposed to hug or have any physical touch.

**James Winter:** Is your daughter learning Portuguese or Arabic?

**Marcel Santilli:** Tiny little bit of Arabic. Not enough. And then our nanny speaks Spanish. And then I try to do a little bit, but I'm bad at it. All her books are in English.

**Marcel Santilli:** But how are things going work wise?

**James Winter:** I'm like done with Engine. I wrapped that up a couple months ago.

**Marcel Santilli:** Was that like an oh thank God I'm done, or was that okay yeah I'm done?

**James Winter:** A little bit of both. It was a nice change of pace to be super embedded and be part of the team and running the whole team. But I mean at one point I had 15 directs. It was just me and a bunch of junior people. I had no leadership until I hired Luke. So I was basically just running the entire team with a big budget, like 30 million.

**Marcel Santilli:** That's insane that they're running all of that with almost no director level either, right?

**James Winter:** Yeah, it was a tricky situation because I inherited the team from Keith. Things didn't work out, and I basically inherited a bunch of ICs that had PTSD. I didn't want to hire too many people because I wanted the VPs or senior directors that I was going to hire to build out their teams more.

**James Winter:** So now I'm spread out across like four or five other portfolio companies. So I'm less embedded, still involved, but not as deeply as I was with Engine.

**Marcel Santilli:** Yeah, that's awesome. Well like I think the main thing was someone mentioned one of the companies you're helping about AEO stuff. And I want to show you what we built that's not yet launched.

**James Winter:** Super curious to hear about what you built.

**Marcel Santilli:** Yeah dude. Okay, so it's kind of crazy. We needed to track AI visibility data for our customers. We started using Scrunch, but we realized they do zero on coming up with the right prompts. Then we realized this is dumb for us to be paying for all this data. We could build this into our services instead. But for you to do this, you need to own the data, at least a subset of the data. And if we're going to do that, there's really no way to make that work unless you have some organic growth around it. Looking around, there's about 170 vendors out there all doing the same thing. You sign up, you have to come up with your own prompts, you don't get any backfill data. So what we did is we built essentially a library of shared prompts. We're making it the biggest open index, very focused on B2B brands and B2B buying categories. We started with about 168 buying categories and we're spending like 200 grand a month in this data.

**James Winter:** Wow. Have you heard of EXA?

**Marcel Santilli:** Yeah. So off the record, we use EXA for a lot of the deep research. Yeah, they're crazy expensive and crazy slow. We use Tavli and a bunch of other things. We've been using X actually for like six months. It's kind of like a secret thing.

**James Winter:** Have you checked out Gina?

**Marcel Santilli:** Yes. We're spending close to 100. We just had a conversation about it today. Our credit card got maxed out yesterday and 45k out of those 150k was from Gina.

**James Winter:** Yeah, that's a lot.

**Marcel Santilli:** So we essentially created every single category editorially. For each category we're coming up with workflows and an editor reviews the prompts. Think of this as the backend work most people wouldn't see. We have an admin panel where, say, if you're looking at a specific category, you see the brands that have been flagged, all the prompts, and our systems are generating additional prompts. Our editors can go in and constantly review and approve new ones.

**James Winter:** Are you using like cosine similarity across the different categories to figure out which ones belong together?

**Marcel Santilli:** So right now it's very much buyer-based, keyword-based, and then reverse engineering the brands themselves that we're finding. We have a data scientist doing a massive study. For all the categories, we're tagging them into our study to figure out different features and what predicts something being cited or mentioned.

**James Winter:** I've gone through G2's whole schema.

**Marcel Santilli:** So that's what we're doing, and we're launching in a couple of weeks. It's going to be public, but you can't sign up right now. I want to get your feedback since you've looked into different things out there. I think we'll have pretty close to feature parity with the rest of the space, and I can give you access or create a free account for you to use with the companies you're helping.

**James Winter:** Yeah, that'd be sick. But I've only really used Peakfail that much. My issue with this space in general is that I'm still skeptical about how deterministic this prompt tracking really is. As LLMs get bigger memory and results become more personalized, how much of this is actually what the average searcher is going to see? 70% the same? 80%? Who knows?

**Marcel Santilli:** It's building on sand pretty much.

**James Winter:** And every time I see some best practice that Profound or Scrunch publishes, and I look at the data myself across Fathom, Engine, and Care Feed, the buyer behavior is totally different. The data sources are so wildly different. So I think you have to do a bare minimum for some categories—it's more important than others. But a lot of people are just over-indexing on it.

**Marcel Santilli:** Yeah, I agree 100%. My mental model: you need to know who's going to win the presidential election, right? You don't have a 30-minute conversation with 200 million citizens. Instead, you figure out the best way to probe the right people in the right way, try to be within a margin of error, and ask just enough people in enough places to be representative of a bigger thing.

**James Winter:** Yeah.

**Marcel Santilli:** So for instance, no one will ever come up with the 500-word prompt that people are using. But on average, if you ask "what are the best platforms for business?" and then "which ones are the best value? Which ones are best for this or that?" you're asking targeted questions based on deep research. You probe just enough to understand where the edges are. Then you can correlate this with your content strategy to know if your content strategy is actually driving any impact.

**James Winter:** Yeah. Maybe you could sell it to G2 and license the data back to yourself.

**Marcel Santilli:** Yeah. Webflow said they want a license from us because they're an investor and customer. They're building an AO solution.

**James Winter:** Did you ever talk to the X Funnel guys?

**Marcel Santilli:** They got acquired by HubSpot. HubSpot is a pretty smart investor in us now too.

**James Winter:** Cool.

**Marcel Santilli:** They're pretty smart, but I didn't quite get it. When I talked to them, they said we were a huge inspiration, but they were a little secretive. Then HubSpot stopped giving access to the platform. We just presented to the HubSpot CEO and their entire leadership team. It doesn't seem like they bought it for the technology—multiple people have told me that. They bought it for the team, but it felt more like they bought it for the PR and the insight from the founders.

**James Winter:** The reason I ask is because the one thing I liked about their platform was they had a UI component tracking experiments over time. You could have a panel that shows: we started posting on Reddit, and you could see tracking the prompt over different time periods.

**Marcel Santilli:** That would be insanely helpful. Was the experiment based on pages published on your site or just random?

**James Winter:** It was a bunch of stuff. Let me see if I can find it.

**Marcel Santilli:** Because visibility increases have to be influenced, right? So you have to track a page, a change to a page ideally. Am I thinking about it the wrong way?

**James Winter:** Yeah. So like you have all these experiments saved. I think you're manually adding these essentially, I don't know that there's automatic detection. But a lot of these are different—like, we posted this thing to Reddit or we added an additional page here or whatever. But I just liked that you could actually see: okay, I did this thing on this date and now I can see how it actually affected inclusion rate, position, or sentiment.

**Marcel Santilli:** Yeah, that makes sense. That's helpful. I got it.

**James Winter:** That's all there was. The rest of their platform is pretty similar to what everyone else.

**Marcel Santilli:** If any of the companies you're helping with, you want to run this and we can set up the workspace for you. It's literally just show up and it's all done. We love feedback in this early stage with people I trust like you. There's very few people whose opinion I respect and who are involved in enough things to know what they're talking about.

**James Winter:** Yeah, I'd love to play around with it. How would multi-tenancy work? Like if I wanted to do it for a bunch of companies...

**Marcel Santilli:** Super easy. We just haven't enabled that in the settings, but we can enable it in your account. We created accounts for all our customers, so it's pretty simple. You just give us a list of companies and we'll create the accounts and give you access. It's mostly for feedback on the structure and everything else. We've done a lot of the work to handle terabytes of data and calculate so many charts to make this thing fast.

**James Winter:** Cool, sounds good, man. I'll send you a list.

**Marcel Santilli:** All right, sounds good, man. Talk soon. Thanks for the time.

**James Winter:** Good to see you.

**Marcel Santilli:** See you too.
