# CheckThat Weekly Check In

<metadata>
date: 2025-12-15
time: 18:00 UTC
duration: 41 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    company: GrowthX
    role: Founder
  - name: Stevie Kim
    company: CheckThat
    role: Engineering Lead
  - name: Jose Farias
    company: CheckThat
    role: Engineer
  - name: Leo Steffen
    company: CheckThat
    role: Engineer (new, joined 2025-12-08)
  - name: Joe Beschi
    company: CheckThat
    role: Engineer
  - name: Estevão Mascarenhas
    company: CheckThat
    role: Engineer
fireflies_id: 01KC4VVPYN3XDS95D9G6560AV6
transcript_url: https://app.fireflies.ai/view/01KC4VVPYN3XDS95D9G6560AV6
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

CheckThat is pursuing two sequential validation milestones before launch: (1) proving organic traffic growth in the public area, and (2) validating that existing customers succeed with checked-out accounts for AI visibility tracking. The team committed to SEO strategy execution, CMS/editorial workflow improvements, and infrastructure optimizations (admin performance, JavaScript error logging, Brandfetch API caching) to unblock these milestones in the next 3-4 months.

---

## Context

CheckThat is GrowthX's strategic AI product bet — an open AI visibility index for B2B SaaS. The team is six weeks into execution of a "launch validation sprint" that prioritizes rapid proof-of-concept over polish. Currently, only internal and private beta users access the product. The strategy involves building 100-200k public pages (brand/category/pricing variants) over 3-4 months to drive organic SEO traffic, then orchestrating a coordinated launch splash once organic growth and core feature parity are validated. Marcel is meeting with HubSpot leadership this week to discuss strategic positioning.

---

## Relevance

**CheckThat / Product Development**
- Launch readiness: Two-step validation milestone (organic traffic + customer success) before full market launch
- Core feature parity: Ensuring existing customers can track AI visibility end-to-end in checked-out accounts
- Editorial/CMS workflows: Enabling editors to execute SEO strategy at scale (public pages, prompt management, subcategory tagging)
- Infrastructure: Admin performance bottleneck (23-second load times), JavaScript error tracking, Brandfetch API caching strategy

**GrowthX Strategic Interests**
- Product-market fit validation: Organic traffic signals from public area as proof point
- Scale assumptions: 100-200k pages + 1-10 variants per brand = infrastructure and content management at scale
- Brand/category taxonomy evolution: Flexible prompt categorization to adapt as market categories evolve (e.g., "coding agents" as emerging category)

---

## Decisions & Commitments

1. **Launch Milestones Locked**: (1) Validate organic traffic growth in public area; (2) Validate customer success with checked-out accounts. Both must pass before market launch. Launch window: 1-2 weeks after validation complete.

2. **Roadmap Priorities** (through 3-4 months):
   - Organic growth infrastructure: 100-200k public pages across brands, categories, pricing variants
   - Onboarding/CMS shaping: Marcel, Jose, Stevie, Leo to collaborate on signup flow and editorial experience
   - Admin performance: Target <5 second load times (currently 23 seconds); <1 second on public

3. **Bug/Issue Process**:
   - Sentry-first for error triage (Slack alerting enabled)
   - Anyone can assign and fix; Leo's approach: triage, assess, escalate if needed
   - Speed favored over process (no external users yet)
   - JavaScript error logging + slow-request filtering will be enabled alongside Rails monitoring

4. **Brandfetch API Strategy**:
   - Logo/brand data caching required to avoid cost explosion (currently free tier; will hit tens of thousands $ quickly at scale)
   - Explore Cloudflare caching or pre-processing logos during brand research queue
   - Separate API keys for search vs. logo endpoints

5. **Prompt Categorization Model**:
   - Shift from rigid category/subcategory hierarchy to flexible shared library + tagging
   - Prompts can belong to multiple subcategories (evolving as market categories change)
   - Categories are holding groups, not boundaries—categories like "CRM" and "AI for Sales" can overlap and co-exist

---

## Open Questions

- Which Brandfetch account/API key is in production? (Marcel may own separate account for CheckThat)
- How aggressive should we be with pre-processing/caching Brandfetch data? (Daily refresh? On-demand trigger?)
- Will JavaScript error logging be too noisy? Need to finalize alerting rules before enabling
- Onboarding flow scope: How prescriptive should forced domain + brand association be? (User choice vs. required)
- Timeline: When is the HubSpot leadership presentation and how does it affect product roadmap?

---

## Overview & Key Topics

- **Launch Validation Strategy**: Two-step milestone (organic growth + customer success) before market launch
- **Infrastructure Scaling**: 100-200k public pages in 3-4 months; admin area performance bottleneck (23s → <5s target)
- **Onboarding/CMS Shaping**: Session scheduled (Marcel, Jose, Stevie, Leo) to design signup flow and editorial experience
- **Bug/Monitoring**: Sentry process clarified; JavaScript error logging + slow-request filtering to be added
- **Prompt Categorization**: Shift to flexible tagging model to accommodate evolving market categories
- **Brandfetch API**: Caching strategy needed to control costs at scale; explore CDN/pre-processing options

---

## Action Items

**Stevie Kim** (CheckThat)
- Add summary and detailed descriptions to milestone documents
- Create necessary tickets for onboarding flow and SEO-related work
- Schedule 1-hour shaping session (with Marcel, Jose, Leo) for calendar

**Jose Farias** (CheckThat)
- Attend 1-hour onboarding/CMS shaping session (2-3 PM same day)
- Submit PR for major backend refactor (portrayals and prompt rankings)—notify team to avoid merge conflicts

**Leo Steffen** (CheckThat)
- Attend onboarding/CMS shaping session
- Coordinate with team on Brandfetch API key usage (separate keys for search vs. logo endpoints)

**Joe Beschi** (CheckThat)
- Configure JavaScript error logging in Sentry with alerting rules
- Optimize admin area performance: target <5 second load times (currently 23 seconds); <1 second on public area

**Estevão Mascarenhas** (CheckThat)
- Verify which Brandfetch account/key is in production; share details with Leo
- Assist in onboarding experience shaping (standby for session outcome)

**Marcel Santilli** (GrowthX)
- Share shaping doc with team before 1-hour session
- Schedule 1-hour shaping session (2-3 PM) with Jose, Stevie, Leo to design onboarding/CMS experience
- Prepare for HubSpot leadership presentation (12:30 PM same day)

---

## Transcript

**Estevão Mascarenhas:** This meeting is being recorded.

**Marcel Santilli:** What up? Happy Monday. I need to get more coffee. Be right back. Okay.

**Leo Steffen:** Morning.

**Stevie Kim:** Morning.

**Jose Farias:** Good morning. It's great to see your face, man. It's been a while.

**Joe Beschi:** Hey yeah likewise. Good to see you all.

**Leo Steffen:** Good to see you all. This is my first weekly check in with you. I joined last Monday.

**Jbeschi:** Yeah I saw your face in the record.

**Leo Steffen:** Yeah that's me Leo. Nice to meet you all. And please add me as a reviewer to your pull requests. If you submit any I would like to just follow up whatever is going on.

**Jose Farias:** Will do.

**Marcel Santilli:** All right I think we have everybody. Stevie do you want to kick us off?

**Stevie Kim:** Sure. So I was out Friday so before Friday though I created after talking to Marcel like we created these lanes of focus areas that we wanted to keep everybody aligned on. I had put some tickets already in those lanes and I just want to thank everybody who picked up you know tickets that were prioritized around organic growth and especially. And so I just wanted to give a shout out to everybody who just took the initiative there to grab things that were in those buckets and looks like there's you know about three at least that are in progress. All right I'm just gonna share my screen real quick.

**Marcel Santilli:** Yeah. In a quick context that we're trying to move towards this make sure we keep in mind kind of the milestones and outcomes we're trying to optimize for. Right. And some of these check ins like keeping the focus on that essentially like at the end of the day the main things keeping us from trying to make a massive splash on this thing is one validating that the public area can grow organically. Right. So keep posting updates. But and there's like a major set of kind of changes if you will of the kinds of pages publicly and a whole organic strategy. So Jose I'll set up time with you and Stevie later this afternoon just to kind of get your thoughts on the. I guess you can call it PRD or just the shaping docket pull together before we share with everybody else.

And so there it's mostly like we don't want to go out to the market and say hey everybody look at this thing. And then tip our hand on this kind of like share library plus SEO play strategy that we have. Right. Milestone number one. It's like go as fast as possible and validating that input to output being traffic organic traffic. And if we get that validated then we're good. Right. We're getting impressions not quite clicks yet but the signals I think are pretty positive. And then the second one is validating that our existing customers can be successful using our their checked out accounts essentially validating that through our teams first. Right. And so end to end we have feature parity or at least an end to end experience for tracking their AI visibility. Once those two things are validated then we can say we are launch ready. From being launch ready then we can add let's say a week or two to actually make a big splash. Right.

So we can think about this phase as sprinting as hard as possible towards that. And then there's a couple of big buckets that we haven't focused on that are also going to be we're going to need to tackle which are mostly around the onboarding flow signup flow that some of the missing things. Right. And so this week I'm hoping to we can all shape that a little bit more and and start to prioritize as well. So that's the big picture I guess.

**Stevie Kim:** Yeah no that's perfect. That way I don't have to go through this doc but this is the overview page and I did put some descriptions in the milestones and Marcel if you want to excuse me. Take a look at this and you know change anything that you know you think needs to be updated and then I'll add up at the top in the short summary that the two like highlighted areas of focus that Marcel just covered.

**Marcel Santilli:** Cool. Yeah. Any any thoughts from folks on. On kind of. And also what how to make the most out of these check ins.

**Stevie Kim:** Crickets.

**Leo Steffen:** Crickets.

**Stevie Kim:** All right well so as I mentioned I did you know add some of the some tickets from Triage and and other ones that I noticed that were SEO related into these buckets like the organic growth strategy. If you know of any other ones that fall into these focus areas definitely you know add them to the milestone. I haven't gone through every single ticket in here and then some of them just are titles and I don't have all the context yet. And so if you know more of what those tickets are about know that they're related go ahead and add them to the milestone. So so yeah just there's you know a couple of ways that people like to work. One is to pick up tickets that they're kind of interested in doing and and working on and that that was my ways preferred as an engineer. But also some people like you know to be assigned tickets. So they just want you know like at the beginning of the week they just want to know what they're working on. So feel free to you know tell me like your preferred way of working and I can accommodate that.

But right now I'm just letting people pick things up that are prioritized into these milestones around the organic growth getting ready for that. And then yeah as once Marcel gets that shaping doc in in a place where we can start creating tickets we'll want to prioritize that because we want to enable editors to be able to execute on our plan. Our growth strategy around creating all these different pages for SEO.

**Marcel Santilli:** I think we can jump into. Yeah sorry go ahead Leo.

**Leo Steffen:** I would like to ask how you guys manage issues such as Sentry alerts or any CI/CD failures and bugs. Do you add it to the board or just wait for an alert to come in Sentry and assign it to someone? How does that work?

**Jose Farias:** I think because Sentry is already sort of like a board in and of itself. Duplicating it in linear might be repetitive but I think let's all just agree to keep an eye on Sentry. If anything high priority comes in we should all be capable of identifying it as a high priority issue and just like jump on it and fix it. Usually they're quick. If it's not quick we can create the ticket ourselves. That sounds good.

**Leo Steffen:** Sounds good. So it is an agreement that we're all going to assign or whoever wants to look at any of the issues just assigned to them on Sentry and we work from there.

**Jose Farias:** That's good.

**Marcel Santilli:** And Jose right now would you say there are any division of areas when you see a bug? Like meaning like if you see something come up in Sentry is the goal for anyone to be able to tackle any bug or that there are certain types of bugs or issues that might be better tackled by someone that worked more.

**Leo Steffen:** I mean there are two levels, right? First you get an alert, you take a look at it, assign it to yourself, and triage it. You look into it and see if it's something you can fix. If not, then you determine if it belongs to someone else or another team or if someone else is more likely to solve it successfully.

**Marcel Santilli:** I'm asking more for Jose or for anyone else that's been on the team a little longer—have there been cases where something comes up and it's like, "Well, this is probably best handled by someone else"? You know, asking for context.

**Jose Farias:** Yeah. So I think let's just handle it on a case-by-case basis. If you see something, take a look. Everyone can use the criteria like, "Oh yeah, this is a Jose bug. I'm just going to tag him," and essentially what Leo said. We could take it one at a time for now.

**Marcel Santilli:** Okay.

**Joe Beschi:** Yeah. Let me add that we have already Atlantic alerting for Sentry errors on Slack. So you don't need to proactively check Sentry every day or every hour or something. If there is any new issue unassigned, you get the alert on Slack. And also we have alerting for reoccurring issues. So if you have an issue that is occurring too often, you have an alert no matter if it's assigned to someone or not. So you don't need to check Sentry—just check Slack and it's enough.

**Jose Farias:** One other thing to add: I think let's not worry about stepping on toes right now. If you see the solution, submit a PR. If it's a one-liner, maybe even merge it and CC the person that has the most context, and they can take a look in their own time. If whichever engineer is like, "Oof, I don't know about this solution—it fixes it, but I don't know if it's good," then you can wait to merge and wait for a review.

**Marcel Santilli:** Perfect.

**Jose Farias:** And I think that's enough process. So that sounds good.

**Marcel Santilli:** Yeah that sounds great. Yeah definitely leaning towards speed given we have no external audiences using anything right now in private areas. So definitely moving towards speed. Makes sense I guess. On the. I'm just curious for the one that we had last week around I think it was the BREX workspace where one of the screens was blank. Was that actually a bug was there just like a. Because the user didn't do this thing first. This thing was a known screen. I'm just trying to understand those types of issues or friction points. Like a blank screen for example.

**Estevão Mascarenhas:** So the BREX workspace was created by the admin panel feature. When you create a new workspace, it doesn't start with any prompts—so it starts blank. What we can do is change it so that when you create a new workspace, it starts with the subcategory prompts already, so it doesn't start blank. I can change that—it's simple. What I did to fix it was add all the subcategories and prompts for BREX, and then the data starts picking up. This is part of the onboarding flow as well. Maybe we want to give users a choice like, "Do you want to import everything from the shared library or start just with custom prompts?"

**Marcel Santilli:** Yeah I think like on the onboarding flow what I was hoping is I want to spend a lot of time with Jose and Stevie on shaping a lot of the what I call like the CMS changes because they're pretty pretty significant and you know Daniel reviewed it and was pretty good with it you know so I don't want to over shape essentially. I think it's at a place now where we need engineering input. But then on the onboarding flow if. I don't know if like maybe Leo or Style like one of you wanted to shape it a little bit as well that would actually probably like help quite a bit. And working closely with Stevie on that just because I think we already have a pretty good idea of the kind of. At least from a technical perspective which like the company context the Personas like all of that works really well. It's just mostly the experience of signing up. We don't want it to be like why force someone to go in the panel and click like contacts right? Like we want to require a domain to be given as a primary domain. You want to associate a brand with it whatever you know so.

So I think that that could be a good. Because I'm. I don't want to be the bottleneck I can be the reviewer there. But it seems like a lot of the issues are going to happen on an experience perspective from us not the defining what the minimum requirements of inputs are to create a workspace all the way to what a good experience should look like you know.

**Estevão Mascarenhas:** Yeah, I discussed this a couple of weeks ago with Daniel, and he told me to wait for when Jose was back because he'd already started working on the onboarding flow. He had put something together for the first version. But I can help. Jose is busy with other parts, but if we can split work, that's fine. I can sync with him as well.

**Marcel Santilli:** So let's hold off for today and plan this out. I was going to book an hour for us this afternoon. I have a presentation with the entire HubSpot leadership team at 12:30, but then after that, I'm pretty flexible. I'll block an hour for you, me, and Stevie to go through the doc I've put together and plan how we want to shape the onboarding experience as well. If that works.

**Jose Farias:** That works.

**Leo Steffen:** Include me in this meeting as well.

**Marcel Santilli:** Perfect. Yeah, see if you can add it to the calendar? I put a block on my calendar for 2-3 PM (an hour), and you can include Jose and Leo as well. I'll share the doc with everyone as well. I just don't want anyone distracted until it's properly shaped.

**Stevie Kim:** Sounds good.

**Marcel Santilli:** Cool.

**Joe Beschi:** There's one thing I'd like to ask about bugs. Right now we are only catching Rails/Ruby bugs in Sentry. So that means we're not going to catch every possible issue. What we could do is also start collecting JavaScript errors and reporting them. But it's going to be noisy—we'll have errors that aren't important mixed with ones that are. So we need to balance the signal-to-noise ratio correctly. Even if we do that, we won't catch every bug because Sentry only catches errors, not bugs that aren't runtime errors in Ruby or JavaScript. So as a next step, I can set up JavaScript Sentry with configuration and we can see how it feels. It's going to be noisy, so I can set up alerting rules and we see how it goes. But I just wanted to clarify that we're not going to catch every issue with Sentry no matter how we configure it. We'll still need to do QA and visualize stuff because otherwise it's not possible to catch everything.

**Marcel Santilli:** Yeah that makes sense. And I think like a couple of things that for me are are I think important. Turning it on I think is good or tracking more I think helps because we can always filter the alerts right? Like to exclude those but at least like capturing so that we can. And then what I was thinking is mostly like extremely slow load times. Right. Like if a screen or something is just taking like really long time to load but also including the admin area in that ideally as well as we start to like. Because I noticed like I think that that's one of the areas where it feels like three to four times slower than everywhere else which is understandable. And then if there's a way at all to know if like there were blank screens or things that just from a user experience were like friction then that would be really great too because as we go down the next several weeks or so knowing that like the number of screens that were just either blank or just took a long time to load or reduced overall that's already like a good outcome to at least try to like see if we're making progress towards you know.

**Stevie Kim:** Yeah I noticed the same thing. It was on. Yeah on Thursday I was going to create some tickets around that around the admin area where it was. The slow load times will affect editors being able to you know work on the. The pages and then trying to get that data quality like if you have to go in every day to brands or you know prompts and stuff and it takes you know you're just waiting for the page to load for a while. Yeah it's. It's going to be an issue just with their productivity.

**Joe Beschi:** I haven't optimized the admin pages because I thought it wasn't necessary, but I will do some work on that. We do have alerting already for slow requests, so we're notified if the app is behaving badly in general. We have granular filters we can use to check for every endpoint. I've done some optimization on the public area mainly, but I will take a look at the admin. For example, we have 23-second requests sometimes on admin profile controller index right now. So I will make sure everything is under 5 seconds in admin and below 1 second in public. I will work on that.

**Marcel Santilli:** That'll be great. And it will make sense once I share the doc and finish shaping it. But we should assume that there's going to be anywhere from 100 to 200,000 public pages on the site in the next three or four months. That's a good assumption to have because we're already at 23,000 brand pages and each brand page is going to have potentially 1-10 variants for pricing, reviews, or other things. Then you have category lists and all the other areas that I put in the organic strategy doc. Hopefully if anyone hasn't read it, definitely read that one for sure.

**Stevie Kim:** So I did have a question around this this ticket I made last week around the each prompt should be associated with more than one subcategory and I wanted to see if there were any questions on this ticket or.

**Marcel Santilli:** The extra context here too just for everyone. I talked to Daniel quite a bit on Friday like we should and look at the thread as well. I posted a comment of a mental model in the thread but the idea is that things evolve over time. I don't know if you captured that part.

**Stevie Kim:** No I'll put it. Yeah I'll put the thread in.

**Marcel Santilli:** But the way to think about it is like legal AI wasn't a category until like six months ago right? But there might be prompts over time that we know for a fact we want to add it to the shared library right? We might not want to have that associated with the category necessarily or maybe multiple categories that prompt might belong to because those categories might be evolving right? And so we should think of categories as really just like a holding group or a group of prompts that might be evolving. And you might want to be testing different categories right? For instance CRM and sales might be a category but you know AI for sales might be an emerging one right? And some of the prompts in one should be in that other one. That doesn't mean this one's going to get deleted necessarily. You know it just might might be different.

And so the concept of categories as a holding group for subcategories is going to really corner ourselves into like a really rigid structure where at the end of the day we want this to be more and more closer to how brands and buyers think of these categories if you will as really like hey when I'm buying like for instance like when I'm buying a piece of software for our company right? Like I think about it in a certain way right? And the way I think about it changes and evolves right? I wasn't thinking about like coding agents you know like a year ago necessarily as a buying group right? Or category. And so we want to try to keep it as flat as possible and also just have the ability to manage a shared library of prompts. The best mental model is that what we're building is a shared library of prompts. And and then we're tagging those prompts if you will in different ways that make sense you know for our audiences or our customers with. That makes sense.

**Stevie Kim:** Yeah. And I'll add that some of them don't make sense right now and it'd be an easier way to edit them by adding them to the subcategory that they actually should belong to. We're also changing or you know adding subcategories like Marcel said. So that added flexibility will be really really helpful for people that are going in all the time and having to review all the prompts that are in subcategories that we have.

**Jose Farias:** I think this should be relatively straightforward barring any surprises. So we can just prioritize this as up next and any any one of us can tackle it.

**Marcel Santilli:** Perfect.

**Stevie Kim:** I think that's the only one that I wanted to to get some focus on just. And clarity. I think most of the other ones are pretty straightforward and a little bit smaller. But if anybody else has questions on tickets that they want clarity on feel free to. To ask now.

**Marcel Santilli:** Yeah I think the one in my mind is just making sure the. Especially the the charts. I think we have a ticket on just like the overview charts and things like that. Like some of these things are like first impression things you know and we.

**Stevie Kim:** Have a lot of tickets on those. So yeah Kyle I think made a lot of tickets. So I was actually going to take a little bit of time with you during our. Our call but to. To kind of figure out what we wanted to do there. Marcel. But we can. I can do like a. Create maybe one ticket instead of just having all those piecemeal ones to talk about to shape the experience a little bit and then have you review it. If you'd rather do that.

**Marcel Santilli:** No I think we're. It should be pretty straightforward like the ticket I submitted with examples you know and explaining like what. Like just the experience. It's just like. I think it's fairly like common sense of like hey if you see a chart that has like 50 lines on it and it's hard to read and you're not really sure where you're looking at or which line and which color to associate with which brand like that's just like an overwhelming experience. And then I just gave examples of what profound as well what peak does well and kind of like in the screenshots and the tickets. So I think like anyone can tackle that just because we're going to have that chart like visualization everywhere in the app. And so just making that a common Component that we feel really good about is going to make a big difference everywhere.

**Stevie Kim:** Yeah yeah I just meant more of like the. The smaller tickets that have been created more recently. Some of them are you know just to be able to filter on like model prompts. Like there's a lot of scrunch parody that we're missing. And so those are kind of more of the. The tickets. I wasn't sure if you guys wanted them in one ticket or if it's fine them being separate for them.

**Estevão Mascarenhas:** I.

**Jose Farias:** For what it's worth I think generally I personally do prefer separate tickets for separate issues. The one thing that does jump up to me is there's like a fidelity concern here in linear where there are milestones and there are tickets in those milestones and then these smaller ones like if we put them there like it's a lot of noise so maybe we just add a bugs milestone or like.

**Marcel Santilli:** A lot of these are going to be under the experience one I think which I think is fair. You know like.

**Jose Farias:** Yeah that works.

**Marcel Santilli:** Yeah.

**Jose Farias:** If they're all grouped together then that works just to differentiate them between like oh this actually like is a big one and needs shaping and engineering input versus another one that's like a quick one layer.

**Marcel Santilli:** Okay that sounds. That sounds good. And the the only other one that I haven't posted yet but I'm just curious. Like one thing I notice is right now the way we're working on the broader like CMS and how we manage pages and slash profiles for brands and kind of like public pages. Because today there's not a lot of controls over almost most of the aspects of those pages like the meta description or the meta title and things like that. So I might suggest some small tweaks to those while we're working on the bigger one. For instance like the fact that our H1 and meta title for all the brands is just the name of the brand and then a dash check that AI is not great. And so even little tweaks like that to have overview pricing and blah blah blah in that makes a huge difference potentially on it getting ranked. And so might be a couple of those kind of in between things. The. That will. That will help. Any. Do we want to go around really quickly or anything that folks are either unclear or want to share. As far as like just to share context on any work from last week.

**Jose Farias:** I'm about to merge or put a PR up for a significant refactor. It has to do with all the data stuff—the portrayals and the prompt rankings. Just a heads up in case anyone is touching that code in the backend or frontend. It's probably best to ping me so we can coordinate because it's going to be a big one in terms of conflicts and surface area for git conflicts.

**Leo Steffen:** And workflows. Repo or check? Just check that.

**Jose Farias:** Oh check that. Just check that.

**Marcel Santilli:** Cool.

**Estevão Mascarenhas:** I have a quick question. I was checking which account we are using for Brandfetch and the API key we're using—I couldn't find it. It's not the account we have in our password manager. Do you know if you created an account just for CheckThat? My idea was to use Brandfetch to get the brand color so we can put it in the chart. Brandfetch already gives us that. So it would be nice. But yeah, just confirming which account/key we're using.

**Marcel Santilli:** No but Leo this would be a good one for you to help.

**Leo Steffen:** We have separate keys for different purposes.

**Marcel Santilli:** Yeah. And anything we can do to cache as much as possible so we're not pinging the Brandfetch API—the cost will go up quite a bit. Like if you have a logo, we do one API call, grab everything, cache and store it, and then maybe set a trigger to repaint the API if it's outdated. Otherwise, we'll hit tens of thousands of dollars pretty quickly. Brands don't tend to change their logos that frequently, so I think that approach would be good.

**Leo Steffen:** Yeah I'm gonna ping you later still.

**Estevão Mascarenhas:** All right.

**Marcel Santilli:** And they have two different APIs. There's the search API versus the logo API. The search API is easier to use for search experiences versus where we're filling out logos. For grabbing data, we have Data Labs. The firm graphics API is useful too. Okay, let me change speakers here. Okay, you guys hear me?

**Jose Farias:** Yep.

**Marcel Santilli:** Got a special guest over here. Yeah. And Estevão, for what you're saying—is it mostly to fill out the logos, right? Not for grabbing data, or is it for grabbing additional data?

**Estevão Mascarenhas:** No no for additional data. We discussed. I created a task but I'm prioritizing other tasks that Stevie discussed with us on the milestones.

**Marcel Santilli:** I was on the wrong speaker. Can you say that again?

**Estevão Mascarenhas:** Yeah no no worries. No it's not for it's not for data reachment for that what we discussed. I created a task but I I I'm prioritizing the charts the SEO bugs and other stuff. So.

**Marcel Santilli:** Do you remember if you have an account? Did you create an account for Brandfetch just for CheckThat? Because we're using a key that I think I might have created.

**Estevão Mascarenhas:** If you can share that later, that would be nice.

**Marcel Santilli:** Yeah, because we're going to use it quite a bit. I think we're on the free tier, which lets you do a bunch of calls. I can create another one if needed, but I think I did. It should be under tools.

**Estevão Mascarenhas:** I think the key we're using client-side is different from what I found.

**Marcel Santilli:** Yeah, I think we can swap it. Leo, you can work with both sources to see if anything else is hitting our limits. Their logo API has very high throughput on the free tier. So we can just swap to whatever works. Just to understand—right now, when we're monitoring prompts or someone sets up a workspace and we identify new brands, those brands get put into a queue to do deep research. When and how are logos fetched from Brandfetch in that process?

**Joe Beschi:** They're fetched from their CDN every time you hit the endpoint. We use their own CDN. We could even maybe use our own CDN and cache theirs if that's going to work. We do zero work on that. I'm not sure if it'll work, but maybe if we set up something on Cloudflare we can cache it, or maybe we can just store the logo when we process the brand. That could work too, but then we'd need to update them daily or something. We have those two options mostly.

**Marcel Santilli:** Yeah, I think we just decide when those triggers happen so that as we expand, knowing the more we pre-process those things that come up in the experience, the less likely people are going to run into blank logos because we haven't fetched yet or we're waiting for Brandfetch. Their logo CDN is open, so we can pass the API key because they asked, but we don't even have to. We could have a fallback on the server. The more we can rely on our own stuff—in case their API goes down, would every logo on our site go down?

**Leo Steffen:** No, it's a CDN, so it would be unlikely to go down everywhere. It's distributed, so it can't happen globally. Unless Cloudflare goes down, but that would take everyone down.

**Leo Steffen:** Yeah.

**Marcel Santilli:** Right. Cloudflare took down GitHub at one point. I don't know if you all remember. Yeah, they were talking about it in a webinar. Yeah, cool. Awesome. That sounds good. I'll share the doc and then we'll do the session a little bit later. All right, thanks everyone. Talk soon. Cheers.

The recording has stopped.
