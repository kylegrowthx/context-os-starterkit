# Marcel Santilli and James Winter

<metadata>
date: 2025-12-29
time: 21:30 UTC
duration: 36 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, James Winter
fireflies_id: 01KDHFVJ9M8CNZH5RTRWA1AFKS
transcript_url: https://app.fireflies.ai/view/01KDHFVJ9M8CNZH5RTRWA1AFKS
</metadata>

---

## Summary

Marcel and James caught up on personal updates and discussed the development of GrowthX's AI visibility tracking platform. The platform invests $200,000 monthly to collect data across 168 buying categories with an open prompt library and editorial oversight. Marcel is preparing to launch publicly in the coming weeks and offered James access to test the platform with his portfolio companies. James raised skepticism about deterministic prompt tracking as AI models evolve, but Marcel explained the sampling methodology and suggested connecting marketing actions to visibility metrics.

---

## Action Items

**Marcel Santilli**
- Share access or create free account on AI visibility platform for James to test with companies he supports
- Enable multi-tenancy feature and set up accounts/workspaces for James's companies
- Reconnect with James in the new year to collect feedback on platform usage

**James Winter**
- Send list of companies to Marcel for account creation on AI visibility platform
- Provide feedback on platform features and usability

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

**Marcel Santilli:** Yeah dude. Okay, so it's kind of crazy. We needed to track AI visibility data for our customers. We started using Scrunch, but we realized they do zero on coming up with the right prompts. And then we're like, this is dumb for us to be paying for all this data. And we signed up for all of them and we're like, this is really dumb. Then we're like, well, let's build this into our services. But for you to do this, you need to own the data, at least a subset of the data. But then we're like, if we're going to do that, there's really no way to make that work unless you have some organic growth around it. And we use that as organic growth. Looking around, there's about 170 vendors out there all doing the same thing. You sign up, you have to come up with your own prompts. You don't get any backfill data. So what we did is we built essentially a library of shared prompts. We're making it the biggest open index, very focused on B2B brands mostly and B2B buying categories. We started with about 168 buying categories. We're spending like 200 grand a month in this data.

**James Winter:** Wow. Have you heard of EXA?

**Marcel Santilli:** Yeah. So off the record, we use EXA for a lot of the deep research. Yeah, they're crazy expensive and crazy slow. We use Tavli and a bunch of other things. We've been using X actually for like six months. It's kind of like a secret thing.

**James Winter:** Have you checked out Gina?

**Marcel Santilli:** Yes. We're spending close to 100. We just had a conversation about it today. Our credit card got maxed out yesterday and 45k out of those 150k was from Gina.

**James Winter:** Yeah, that's a lot.

**Marcel Santilli:** So we essentially created every single category. We're editorially generating, and for each category we're coming up with workflows and an editor reviewing the prompts. So there's a bunch of categories, right, that we're editorially generating. And for each category we're coming up with like workflows to do this. An editor goes through and reviews the prompts to create the index. So think of this as the stuff most people wouldn't see. But like we have an admin panel. And so let's say you're looking at CEP. These are the brands that have been flagged. And there's all these prompts essentially. And our systems are generating a bunch of additional prompts and then our editors can go in and constantly review and approve additional ones.

**James Winter:** Are you using like cosine similarity across the different categories to figure out which ones belong together?

**Marcel Santilli:** So right now it's very much buyer based, keyword based, and then reverse engineering the brands themselves that we're finding. And we have a data scientist doing a massive study. For all of the ones that are here, we are also tagging a lot of them into our study. The study is going to figure out a bunch of different features as well as what predicts something being cited or mentioned.

**James Winter:** I've gone through G2's whole schema.

**Marcel Santilli:** Yeah. So anyway, so that's kind of like what we're doing. And then we're launching in a couple of weeks. It's public, available, you just can't sign up right now. And I want to get feedback on like if you've looked into different things out there. I think this is going to have pretty close to feature parity and I can give you access or create a free account for you to use with one of the companies you're helping.

**James Winter:** Yeah, that'd be sick. But I've only really used Peakfail that much. My issue with this space in general is that I'm still skeptical about how deterministic this prompt tracking really is. And like as the LLMs memory gets bigger and results are more personalized, like how much of this is actually what the average searcher is going to see? Is it like 70% the same? Is it 80%? Like who knows?

**Marcel Santilli:** It's building on sand pretty much.

**James Winter:** Yeah. And then every time I see some best practice or something that Profound publishes or Scrunch publishes, and I look at the data myself and I look at what's working for Fathom versus what's working for Engine versus what's working for Care Feed, the data sources, the prompts, like who knows? And the buyer behavior is totally different. The data sources are so wildly different. So I'm like okay, you have to do a bare minimum for some categories. It's more important than others. But there's a lot of people who are just over-indexing on it.

**Marcel Santilli:** Yeah, I agree 100%. My mental model here: you need to know who's going to win the presidential election, right? That doesn't mean you have a 30 minute conversation with 200 million citizens, right? It's like that's impossible. Instead what you do is figure out what is the best way to probe the right people in the right way. And then try to be within a margin of error. And then try to do it in a way where you're asking just enough people in enough places to be representative of a bigger thing.

**James Winter:** Yeah.

**Marcel Santilli:** So for instance, no one will ever come up with the 500 word prompt that people are using. But on average, if you say hey, what are the best platforms for business, right? And then you say hey, give me which ones are the best value, which ones are best for this, whatever, right? Like can you come up with the kind of questions based on deep research that are legit just a one question thing? And then you probe it just enough to understand roughly where the edges are. Then at least you know. And then you can start to correlate this with actually your content strategy to know if your content strategy is actually driving any impact here.

**James Winter:** Yeah. Maybe you could sell it to G2 and license the data back to yourself.

**Marcel Santilli:** Yeah. Webflow said they want a license from us because they're an investor and customer. They're building an AO solution.

**James Winter:** Did you ever talk to the X Funnel guys?

**Marcel Santilli:** They got acquired by HubSpot. HubSpot is a pretty smart investor in us now too.

**James Winter:** Cool.

**Marcel Santilli:** It's kind of like they're pretty smart, but I didn't quite get it. When I talked to them, they were kind of like, hey, you were a huge inspiration. But they were a little bit secretive. And then HubSpot stopped giving access to the platform. And we just presented to the HubSpot CEO and their entire leadership team. And like it doesn't seem to me like they bought it for the technology. Multiple people have told me that. So it's like they bought it for the team. But it felt like they bought it more for the PR and the insight from the founders.

**James Winter:** The reason I ask is because the one thing I liked about their platform was they had a UI component tracking experiments over time. You could have this panel that's like okay, we started posting on Reddit in this or whatever. And you could see like tracking the prompt over the last certain periods of time.

**Marcel Santilli:** Would be insanely helpful. Was the experiment based on pages published on your site or is based on like just random?

**James Winter:** It was a bunch of stuff. Let me see if I can find it.

**Marcel Santilli:** Because there's like visibility increases and those visibility increases have to be influenced. Right. And so you have to track a page, a change to a page ideally. Right. Or am I thinking about it the wrong way?

**James Winter:** Yeah. So like you have all these queries saved, but these are sorry, not queries, like experiments. So I think you're just like manually adding these essentially. I don't know that there's like automatic detection. Because a lot of these are different. Like okay, we posted this thing to Reddit or we added an additional page here or whatever. But I just like that you could actually see, okay I did this thing on this date and now I can see like how it actually affected inclusion rate or like position or sentiment or whatever.

**Marcel Santilli:** Yeah, that makes. That's helpful. I got it.

**James Winter:** That's all there was. But the rest of it I mean the rest of their platform is like pretty similar to what everyone else.

**Marcel Santilli:** If any of the companies you're helping with, you want to run this and we can set up the workspace for you. It's just literally just show up and it's all done. Because we love feedback, in this early stage with people I trust like you. There's very few like that I'm like I kind of respect their opinion and I feel like they are involved in enough things to know.

**James Winter:** Yeah, I'd love to play around with it. How would multi tenancy work? Like if I wanted to do it for a bunch of phone...

**Marcel Santilli:** Super super easy. We just haven't enabled that in the settings, but we can enable that in your account. We just created accounts for all our customers. So it's pretty simple. We can just create all the accounts. You just give us a list of all the accounts we can create and give you access. And it's mostly for feedback on the structure and everything else. We've done a lot of the work to handle terabytes of data and calculate so many charts and things to make this thing fast.

**James Winter:** Cool, sounds good, man. I'll send you a list.

**Marcel Santilli:** All right, sounds good, man. Talk soon. Thanks for the time.

**James Winter:** Good to see you.

**Marcel Santilli:** See you too.
