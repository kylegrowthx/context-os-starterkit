# CheckThat Weekly Check In

<metadata>
date: 2026-02-09
time: 18:00 UTC
duration: 76 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Daniel Lopes, Jose Farias, Stevie Kim, Pedro, Steven
fireflies_id: 01KGFT0XKAY8WWQT39V9SB4RYV
transcript_url: https://app.fireflies.ai/view/01KGFT0XKAY8WWQT39V9SB4RYV
</metadata>

---

## Summary

The Check That product team worked through onboarding drop-off (900+ users at brand selection), overview page improvements, taxonomy automation, and brand/category management. Key decisions: replace overview tabs with filters (matching prompts page); redesign onboarding to allow multiple category selection (Spotify-style) instead of single autocomplete; deploy taxonomy auto-tagger; automate brand approvals based on mention thresholds. Five priorities: overview filters, onboarding recalibration, taxonomy auto-tagging, brand auto-approval, and category management. Learn area (blog) deprioritized. Meeting cadence restructured: strategy discussions moved to Fridays.

---

## Context

This is the weekly Check That product/engineering check-in, happening days after launch (~200 signups). The team is addressing immediate user experience issues surfaced from session recordings and analytics. The product is in early "0 to 1" phase with significant onboarding friction and overview page confusion undermining demos and user trust. Daniel, Jose, Stevie, and Pedro/Steven are the core engineering team; Marcel provides product direction.

---

## Relevance

**To CheckThat Product:**
- 900+ users drop off at brand selection during onboarding; biggest exit point.
- Onboarding redesign: shift from single category to multiple category selection (calibration mindset).
- Overview page: remove confusing "category" tab; add filters (brand vs. non-brand, funnel stage, category grouping).
- Taxonomy generator deploying: auto-tags prompts with categories, personas, funnel stages.
- Brand auto-approval by mention thresholds feasible; auto-creating categories not advisable (cost/complexity).
- Only ~200 users upgraded post-launch; value gap not yet clear to users.
- Prompt recommendations depend on taxonomy; wait until tagging infrastructure is ready.
- Learn area (blog/educational content) deprioritized; minimal MVP later.

**To CheckThat Operations:**
- Workspace calibration for demos/prospects still manual; better admin tools needed.
- Support tickets mostly about missing subcategories; session recordings key for spotting pain points.
- Meeting cadence: strategy discussions to Fridays with core leadership; tactical meetings optional/canceled.
- Product analytics dashboards in PostHog (Pedro) and Stevie's dashboards available.

---

## Overview

- 900+ users drop at brand selection; onboarding redesign to multiple categories planned.
- Overview page: remove tabs, add filters matching prompts page (brand/non-brand, funnel stage).
- Taxonomy auto-tagger deploying; enables grouping and filtering.
- Brand auto-approval by mention threshold; category auto-creation too costly.
- Five priorities: overview filters, onboarding, taxonomy, brand approval, category management.
- Blog/learn area deprioritized; prompt recommendations wait for taxonomy.
- Meeting cadence restructured: Friday strategy sessions.

---

## Key Topics

### Onboarding flow

- 900+ users drop off at brand selection (not category as expected); tracking accuracy being verified.
- Current flow pins users to single category → misleading dashboards when default misses brand attributes.
- Redesign: allow multiple category selection (Spotify genre analogy); "calibrate your workspace" framing.
- Will reduce friction and create more accurate, personalized workspaces faster.

### Overview page and filtering

- Marcel: overview page "embarrassing" when showing irrelevant data; no way to exclude brand prompts.
- Consistent filters matching prompts page: brand vs. non-brand, funnel stage, category grouping.
- Remove legacy "category" tab; rely on filters and grouping.
- Jose to implement incrementally; snapshotting system constraints noted.
- Grouping by tags essential for deriving trends (individual prompts not meaningful alone).

### Taxonomy and categorization

- Taxonomy generator auto-tags prompts with categories, personas, funnel stages; backend ready, deploying shortly.
- Brand auto-approval by mention threshold feasible and low-risk; category auto-creation not advisable.
- Only 2 new categories added in 2 months — too manual; need dynamic brand pulling based on usage.
- "Potential approvals" tab within categories for admin vetting.
- Cost per deep brand research being tracked to optimize volume vs. depth.

### Prioritization

- Five near-term priorities: overview filters, onboarding redesign, taxonomy auto-tagging, brand auto-approval, category management.
- Learn area (blog) deprioritized; minimal MVP with pillar/article pages later using existing CMS.
- Prompt recommendations wait for taxonomy infrastructure.
- Meeting cadence: strategic Fridays with core members; tactical meetings optional.

---

## Action Items

**Daniel Lopes**
- Draft document on reframed onboarding flow, taxonomy improvements, and overview filter proposals (10:10)
- Finalize and deploy taxonomy generation and prompt tagging workflows; merge PRs (15:28)
- Write tickets to fix onboarding and overview filters (23:59)

**Marcel Santilli**
- Locate and share UI mockup ticket for overview filters (29:02)
- Continue creating subcategories and approving prompts as short-term fix (39:02)
- Act as DRI for workspace creation for demos and prospect engagement (01:10:28)

**Jose Farias**
- Implement overview page filtering similar to prompts screen; deprioritize probing cadence for pricing tiers (30:02)
- Evaluate filter feasibility with snapshotting system (33:19)

**Stevie Kim**
- Pause categorization work until product vision clarified (25:54)
- Follow up with Tyler on workspace creation process (01:09:11)
- Share product analytics dashboards with team (01:04:36)

---

## Transcript

**Leonardo Carpenedo Steffen:** Sam.

**Daniel Lopes:** There.

**Marcel Santilli:** Hey.

**Daniel Lopes:** Good morning.

**Marcel Santilli:** Hey, good morning.

**Leonardo Carpenedo Steffen:** How doing today?

**Daniel Lopes:** Pretty good, thanks.

**Leonardo Carpenedo Steffen:** Who's hosting the recording here?

**Leonardo Carpenedo Steffen:** Fathom says it's initializing.

**Daniel Lopes:** Hey.

**Marcel Santilli:** I'm not the host so I can't kick that kick out anything.

**Leonardo Carpenedo Steffen:** Thanks.

**Leonardo Carpenedo Steffen:** Davy.

**Leonardo Carpenedo Steffen:** Yes.

**Stevie Kim:** Sorry, I was on mute.

**Stevie Kim:** What are you trying to do now?

**Leonardo Carpenedo Steffen:** I was just trying to look at Fathom keep saying it's try.

**Leonardo Carpenedo Steffen:** Try to start recording for me but I'm not the host.

**Leonardo Carpenedo Steffen:** And it says it can find the host.

**Leonardo Carpenedo Steffen:** Just try to now it went away now.

**Marcel Santilli:** We are way overdue to the le Fathom.

**Stevie Kim:** So I do like the summaries, I think.

**Stevie Kim:** Sorry.

**Stevie Kim:** My dog's got a cone on his on her head right now and she.

**Stevie Kim:** When she hits something, it's just really.

**Daniel Lopes:** This meeting is being recorded.

**Marcel Santilli:** All right, well we made it through launch week folks.

**Stevie Kim:** Congratulations everybody.

**Leonardo Carpenedo Steffen:** That's you all.

**Leonardo Carpenedo Steffen:** I joined kind of late for the game, late to the party but.

**Marcel Santilli:** Well I, I think the maybe before jumping in.

**Marcel Santilli:** I. I'm just looking at the notes.

**Marcel Santilli:** Any TLDR big takeaway from.

**Marcel Santilli:** From the metrics.

**Marcel Santilli:** It looks like other like.

**Marcel Santilli:** Like drop off or any.

**Marcel Santilli:** Anything surprising or that worth calling out from what we're seeing so far, nothing.

**Stevie Kim:** Surprising to be honest.

**Stevie Kim:** It's like we.

**Stevie Kim:** We knew we like, we knew category we had tickets for like to improve subcategories.

**Stevie Kim:** You know, whether it was like improving how we're categorizing or improving how users can create or to ask for a new category if we don't have one or change their category.

**Stevie Kim:** So those things were known.

**Stevie Kim:** The.

**Stevie Kim:** So the metrics just kind of support that.

**Stevie Kim:** Like I mean it's the longest step that people are spending their time on during the onboarding flow.

**Stevie Kim:** I think one thing that surprised me is that more people are actually dropping off during brand selection for the onboarding flow.

**Stevie Kim:** So I want to investigate like what's happening there.

**Marcel Santilli:** What's brand selection?

**Stevie Kim:** It's the.

**Stevie Kim:** It's the first, you know, major step in the onboarding flow where you, you know, submit your domain and so I don't quite understand like why that such a drop, you know, big drop off.

**Stevie Kim:** So that's some worth investigating and is a little bit surprising.

**Stevie Kim:** I thought it would have been the categories app.

**Daniel Lopes:** There was basically no difference in like in the other steps.

**Daniel Lopes:** It's just that all the 900 people drop at the sign up to brand selection.

**Stevie Kim:** Sorry, what was that?

**Daniel Lopes:** There's very little difference once they go into the brand selection on that.

**Daniel Lopes:** On the other steps of the funnel.

**Stevie Kim:** Yeah, there's.

**Stevie Kim:** There's A little bit between categories and competitors, but yeah, I mean, and I can share my screen.

**Stevie Kim:** Um, so we're all looking at the same thing.

**Stevie Kim:** But yeah, there's, Like you said, it's not a huge difference between the other steps.

**Stevie Kim:** Sorry.

**Daniel Lopes:** I guess I wonder if it's counting.

**Stevie Kim:** Covering it a little bit.

**Daniel Lopes:** Could it be counting duplicate?

**Daniel Lopes:** See, because page views is.

**Daniel Lopes:** It's a page event and the other one is a legit.

**Daniel Lopes:** You select the brand.

**Daniel Lopes:** That's like an action.

**Daniel Lopes:** That's an event versus a page view.

**Daniel Lopes:** But there might be a difference there.

**Daniel Lopes:** So like somebody refreshing the page or somebody coming back to sign up multiple times.

**Daniel Lopes:** This is a big.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** And also the page view doesn't mean.

**Stevie Kim:** Is it.

**Stevie Kim:** Did I set it for page view or.

**Stevie Kim:** No, no.

**Stevie Kim:** Plan chosen is an event.

**Stevie Kim:** Those are all events.

**Stevie Kim:** The only one that's a page view is the first one.

**Daniel Lopes:** Right, right, right.

**Daniel Lopes:** Yeah, but like.

**Daniel Lopes:** It'S going to secure the entire metric.

**Daniel Lopes:** But.

**Stevie Kim:** But yeah, I mean, so we'll, as I said, investigation is worth investigating.

**Stevie Kim:** Making sure like, we're tracking things correctly and seeing like, especially as I said around here where the drop off is.

**Stevie Kim:** So this is just, you know, initial stat at, you know, creating these charts and making sure like, we.

**Stevie Kim:** How we're tracking.

**Stevie Kim:** So the investigation might be, you know, might tell us, hey, we need to fix something and how we're tracking or how I'm creating some of these dashboards.

**Stevie Kim:** But yeah, that was kind of like the only thing that stood out.

**Stevie Kim:** As I said, we're, you know, pretty aware of this step needing, you know, some, some improvement and just our categories overall.

**Marcel Santilli:** Yeah, I think like, overall for me, um, I, I haven't been able to take someone live through the flow, like when someone's sitting next to me or like I'm presenting through a brand and at the end of it, get to a dashboard where I'm like, oh, this actually makes sense.

**Marcel Santilli:** It looks legit.

**Marcel Santilli:** Like.

**Marcel Santilli:** And what I mean by that is like, it's usually either because of the category or because it's like not pulling all of it with an overview or the like, there's something still that doesn't get to a viewer's like, whoa, like, this is legit.

**Marcel Santilli:** Good data.

**Marcel Santilli:** Like, this is good.

**Marcel Santilli:** Right?

**Marcel Santilli:** And.

**Marcel Santilli:** And I think there's a few, like, little tweaks that we can, we can make that.

**Marcel Santilli:** I think most of them are already kind of like submitted where, when.

**Marcel Santilli:** When we get it right or, or at least like communicating with people kind of like what this is as far as like pulling the categories.

**Marcel Santilli:** Because it's just essentially if the categories are not perfectly aligned to the brand and the.

**Marcel Santilli:** And we don't select the right categories to begin with or any of those things are slightly off, the whole thing is like completely off.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like.

**Marcel Santilli:** And so like the Confluence example was a good one of like when I created it because it defaulted to project management instead of wikis.

**Marcel Santilli:** Everything about the experience was super off, you know, and, and so that you.

**Daniel Lopes:** Might have to rethink the entire onboarding because the.

**Daniel Lopes:** What the category does is the same as a competitor could do.

**Daniel Lopes:** As in like we're just getting the things that could.

**Daniel Lopes:** That will bootstrap your workspace.

**Daniel Lopes:** It's not pinning it, you know, so just to load the prompts.

**Marcel Santilli:** But because like we're defaulting to one always.

**Marcel Santilli:** Like in an overview, for example, we are only defaulting to one when the, when the dashboard is loaded, it only loads from one of those categories.

**Marcel Santilli:** Like everything defaults to one.

**Marcel Santilli:** It becomes very like dependent on that one being the perfect one and the only one.

**Marcel Santilli:** But because a lot of brands are, you know, not necessarily just one when we get it wrong, which is.

**Daniel Lopes:** Yeah, that's.

**Daniel Lopes:** That's the thing that I had in.

**Daniel Lopes:** The UI that I think like we changed over time and I think kind.

**Daniel Lopes:** Of fucked up the whole thing.

**Daniel Lopes:** Just like it used to be called Leaderboard on the overview.

**Daniel Lopes:** It was just the only thing that that tab was just meant to be like, this is why you show in this.

**Daniel Lopes:** This is just the prompts that you show in the public area.

**Daniel Lopes:** And then we could have taken.

**Daniel Lopes:** And I think it's still like this.

**Daniel Lopes:** So we can like, if we reframe the onboarding to be like, help us find the categories you think it's more relevant to you and then pick the competitors that you think it's more relevant.

**Daniel Lopes:** And that is just the thing that.

**Daniel Lopes:** And then that goes into a flow to like define the prompts, pull the prompts from the shared library and we don't pin so hard on the categories.

**Daniel Lopes:** It's like I always, when I started putting Leaderboard and Shared library everywhere, I always already assuming that we would never going to be able to get the right categories.

**Marcel Santilli:** Yes.

**Daniel Lopes:** There's so much overlap, it's going to boil the ocean.

**Daniel Lopes:** So we can't make Category a big deal in the, in the private area, you know.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And that's why like a lot I've submitted a few tickets on this on like Overview shouldn't be tabs on like Leaderboard or Category or whatnot.

**Marcel Santilli:** They should be Filters just like prompts.

**Marcel Santilli:** That's how all of them peak everybody else works, right?

**Marcel Santilli:** It's just like, for instance, if I'm an overview and I have no way to turn off brand like prompts, it's just a completely useless view because it's just making the data completely biased towards my brand, right?

**Marcel Santilli:** Like, or, or if I can only see one category, not another, or if I can't, like, it just becomes like, just not, not relevant, you know, and then you lose trust with the whole thing because you're just like, there's no way I'm more popular than open AI.

**Marcel Santilli:** For example, I'm using a silly example, right?

**Marcel Santilli:** Like, and then when someone says, sees that they're like, okay, this must be off because they don't understand that there's no filter.

**Marcel Santilli:** So I think that's what I'm saying, that there's a few things of like in the onboarding allowing people to sell like opt out or at least like, select some things that will influence how we like which categories we pull from maybe until we get the full like auto suggesting prompts and pulling and loading up everything more dynamically later on.

**Marcel Santilli:** And then the other thing is just making sure like the, in the overview we can expose filters, some basic filters, like brand versus non brand and like very basic things.

**Marcel Santilli:** And then the last one is I've been finding that the prompt full prompt view is not as useful as the group by views and so grouping by category as the default potentially is a nice solve for that.

**Marcel Santilli:** Where like when you first go to prompts, like defaulting to some level of grouping, it makes it.

**Daniel Lopes:** That's what I'm working on, Marcel.

**Daniel Lopes:** I just, I finished the workflow to generate the taxonomy, just to give you all context.

**Daniel Lopes:** On contentos we had the taxonomy system with categories and values and we, we were generating the planners.

**Daniel Lopes:** You generate automatically the taxonomy.

**Daniel Lopes:** So like your industry, your verticals off of your company overview and your product document.

**Daniel Lopes:** So I ported that over to check that yesterday.

**Daniel Lopes:** So we have the taxonomy generator and we have a workflow that will receive prompts and apply the taxonomy, the Personas and the stage to all the prompts.

**Daniel Lopes:** So we can have a button that will tag all the prompts and then you can do the grouping off of that.

**Daniel Lopes:** So I'll finish the workflows today and I'll push the backend live and then I can define how the UI could look like in like a PRD and create a ticket.

**Daniel Lopes:** But that would solve for that.

**Daniel Lopes:** But I still think, Marcel, we might have to take an Hour or so, maybe off of this meeting to think about the bootstrapping of a workspace because I think we kind of tag things too hard in the category.

**Daniel Lopes:** But if you guys can correct me if I'm wrong, but I think Jose or Pedro, I think the backend, the overview is all about your prompts.

**Daniel Lopes:** The only switch to be about the category when you click on that tab or the category that is on the top section.

**Daniel Lopes:** So if we get rid of that tab and put the filters that Marcel is saying and reframe the onboarding to be like, we're calibrating our workspace, like, I'll pick the things that will create the right prompts for you.

**Daniel Lopes:** That is, that would change the analytics, right?

**Daniel Lopes:** The overview.

**Daniel Lopes:** Like that first step is.

**Stevie Kim:** Yeah, we have a ticket for that for, you know, I mean, Marcel, you've created, you know, some filtering tickets and I created a ticket to be able to add tags to like, on the competitors page.

**Stevie Kim:** Like, you know, because people want to filter and you know, view their competitors by, you know, their different product lines and, you know, area.

**Marcel Santilli:** So giving that more competitors makes no, no sense.

**Marcel Santilli:** Like the word competitors makes no sense as a, as a, like people understand filters.

**Marcel Santilli:** The.

**Marcel Santilli:** The AO category is becoming more like a well defined thing.

**Marcel Santilli:** And so we can't invent too much new language.

**Stevie Kim:** Like saying, oh no, I'm talking about our competitor page.

**Marcel Santilli:** Like, it, like, I, I have no idea.

**Marcel Santilli:** Even me as the person involved in this, I just don't know what competitors means.

**Marcel Santilli:** Like, I just really don't know what it means.

**Marcel Santilli:** Like, are you saying it's only competitive prompts?

**Marcel Santilli:** Like, meaning me comparing to others, or are we saying something else?

**Marcel Santilli:** Like, it's just really hard to understand what it is.

**Marcel Santilli:** And then this is like every single demo I've done, this is what happens.

**Marcel Santilli:** It's like it pulls the wrong word here and I have no way to change it.

**Marcel Santilli:** And it's really like kind of embarrassing a little bit.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That is literally what I'm saying, that we fucked up.

**Daniel Lopes:** That's like a UI thing that we changed.

**Daniel Lopes:** As in like before was just my workspace and leaderboard.

**Daniel Lopes:** So the leaderboard and it had like an explanation saying, this is how you show up on the public here.

**Daniel Lopes:** So like, we should get.

**Daniel Lopes:** Just get rid of the second tab.

**Marcel Santilli:** I can try to find the ticket that I submitted with the mock up and the UI essentially saying, like, please make all the filters consistent.

**Marcel Santilli:** I think like, if we do that, like, there's no need for tabs and overviews.

**Marcel Santilli:** It's just it's either filters or nothing, essentially, you know.

**Marcel Santilli:** Cause it's.

**Daniel Lopes:** Yeah, that makes sense.

**Marcel Santilli:** Like, like right now, for example, the.

**Marcel Santilli:** The only view that I can actually communicate to people that make a little bit more sense is when I go into.

**Marcel Santilli:** And then I go by categories and then people kind of understand what's happening a little bit.

**Marcel Santilli:** You know, they're like, oh, okay.

**Marcel Santilli:** But then when I do that and I see this and I'm like, go into overview.

**Marcel Santilli:** I'm like, where are you guys getting content marketing platforms from?

**Marcel Santilli:** You know, it's just.

**Marcel Santilli:** And so those are some of the things that like, I think will.

**Marcel Santilli:** Will help us just so we never show something that people don't know where we're pulling it from, you know, Whereas like with filters.

**Marcel Santilli:** And then the other thing that I noticed is like, and this is what I've been doing when I'm setting up workspaces for people, I almost always will come and pull from the selected library and in the categories that.

**Marcel Santilli:** That kind of makes sense and kind of preloaded.

**Marcel Santilli:** Like, essentially the more we preload, the better it is.

**Marcel Santilli:** You know, that's what I'm saying that.

**Daniel Lopes:** The onboarding should flip to not be.

**Daniel Lopes:** Like pinning you to a category.

**Daniel Lopes:** We're not trying to fix the public area.

**Daniel Lopes:** You know, we should.

**Daniel Lopes:** It should just be like what you just did.

**Daniel Lopes:** As in, like, we're picking the categories that might have the prompts that might make sense to you.

**Daniel Lopes:** Remove the former leaderboard, that's now the name of the category from the tab.

**Daniel Lopes:** And even that alone without adding the grouping and the filters.

**Daniel Lopes:** I think it would like, get us there, you know, and then add the grouping and filters after grouping and filters a little harder to do.

**Daniel Lopes:** Just doing that, I think would solve the problem of never landing on the page that you don't make sense on the overview.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** This is a hard.

**Marcel Santilli:** A hard thing.

**Marcel Santilli:** Because individual prompts don't mean anything in of itself.

**Marcel Santilli:** Right.

**Marcel Santilli:** The only like insights that you can get it until we have like an insights or reports tab is by having a group that, you know.

**Marcel Santilli:** And so like, which means you need to tag it by something, right?

**Daniel Lopes:** Like, yeah.

**Marcel Santilli:** And that's why, like, I think.

**Daniel Lopes:** But I think we're jumping to jumping forward where I'm like, I'm talking about the step of today.

**Daniel Lopes:** And if we just get a thousand or five thousand prompts that are actually closer to what the person wants, then we can do the auto tagging after.

**Daniel Lopes:** And if you do that in the onboarding, you land on the overview with people that you Actually recognize.

**Daniel Lopes:** And then if you go into the prompt area, the prompts will make sense.

**Daniel Lopes:** It would just be a ton.

**Daniel Lopes:** And then we can guide people.

**Daniel Lopes:** We generate your company context and we'll generate your taxonomy.

**Daniel Lopes:** Here's all the tags that you can press a button to group by.

**Daniel Lopes:** You know, so it's steps towards getting there because a lot of these things will be.

**Daniel Lopes:** But we do need to get people to pick the right categories.

**Daniel Lopes:** As in categories is the only grouping.

**Daniel Lopes:** We have to just funnel the prompts.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** So during the onboarding, categories and competitors.

**Daniel Lopes:** So you can also, if competitors are in the system, then we can also use that, I guess, to find the categories of the competitors.

**Daniel Lopes:** But categories would be easy enough, but we might have to add a bunch of aliases to categories and things like that, you know, so people, when they type, they find the right categories.

**Daniel Lopes:** Maybe not.

**Daniel Lopes:** But like, that's what I can, I can write down what I'm.

**Daniel Lopes:** Because I think I'm like, you're talking at high here, I'm talking here.

**Marcel Santilli:** And there's, yeah, yeah, I guess, like.

**Daniel Lopes:** What is something that we can do?

**Jose Farias:** We're a line.

**Marcel Santilli:** Like, the gap here is if I personally created like 20 or 30 workspaces and have not gotten to a place where it kind of clicked and I could show the data to the person.

**Marcel Santilli:** Right.

**Marcel Santilli:** That means we have a gap and that's the gap that we're trying to fill, which is like from sign up to something that makes people click and go, okay, this actually makes sense.

**Marcel Santilli:** The story, though, really clicked.

**Marcel Santilli:** Like, everyone I've talked to, like, the story we're telling is clicking.

**Daniel Lopes:** My point is that.

**Daniel Lopes:** Yeah, my point is that there is a way to get there in three weeks.

**Daniel Lopes:** There's a way to get there in three weeks.

**Daniel Lopes:** In three days.

**Daniel Lopes:** Let's do the three days first and then we get to the, we navigate towards the three weeks because there is a way to like, go make a few small changes in your board that you're going to land with like a couple thousand prompts that are more accurate to you.

**Marcel Santilli:** So what will be the best way to like, for us to look at what we're prioritizing?

**Marcel Santilli:** Because for me, I have a really difficult time.

**Marcel Santilli:** Like, you know, like, there's a lot going on and, and I, I, I can go take the time to just like, try to.

**Leonardo Carpenedo Steffen:** Yeah.

**Marcel Santilli:** A bit more.

**Daniel Lopes:** Maybe you can keep this meeting as a, like, give us the, the state of what's happening now and whether everybody's working on like the stuff that Marcel is talking about and the stuff that you identify in the funnel is like strategic and super high priority, but it's a new thing from the learn learnings from the launch.

**Daniel Lopes:** And then there's all the bugs, all the things we have to do anyway, like the content generation being blocked and all the things.

**Daniel Lopes:** So we give us the list of tickets that are high priority and then I can take a stab on like taking Marcel's idea and align with the stuff that I'm doing and write a set of tickets for fixing the onboarding and fixing the overview area.

**Daniel Lopes:** It shouldn't take more than 30 minutes for me because I already did a ton of stuff on this.

**Stevie Kim:** Okay.

**Stevie Kim:** Yeah.

**Stevie Kim:** So, yeah, the intention was going to be on that categorization.

**Stevie Kim:** I did list out some of the user stories and stuff, but it sounds like you guys have a different perspective on it and so, yeah, I'll let you tackle that.

**Stevie Kim:** So that kind of changes what we were going to talk about today.

**Stevie Kim:** I changed my, change my filters.

**Marcel Santilli:** Yeah, I, I, for me, what would be kind of interesting is to just know, like, I think there's a lot of things we were trying to stabilize.

**Marcel Santilli:** So for two weeks I just kind of took a step back and didn't suggest anything.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so now though, that we're post that.

**Marcel Santilli:** I don't know what happened to all the other things that I've submitted over time and then, but I think some of them are very, very still relevant, others might not.

**Marcel Santilli:** And so that we need to do a little bit of grooming or at least like prioritization.

**Marcel Santilli:** But I don't even know where to look at in linear to even know what's still there versus what got lost or what got archived or deleted versus what's next up?

**Marcel Santilli:** Essentially?

**Daniel Lopes:** Yeah, pretty much everything is up the stabilized weeks.

**Daniel Lopes:** Nothing was archived.

**Stevie Kim:** Yeah, yeah, we haven't, I don't think any of the ones that you submitted unless something just completely changed, like the homepage or the public, you know, branding page.

**Stevie Kim:** Like, there were a lot of changes, but nothing I don't think has become irrelevant or anything.

**Stevie Kim:** So I can tell you what, you know, is being worked on right now and that is like that subcategory selection.

**Stevie Kim:** And we did want to talk a little bit about the categorization, but we might want to take us like a pause on, on that work that we're doing there until you get, until you guys kind of figure out your vision for that.

**Stevie Kim:** Does that sound like the right step to take a pause on what we're doing for what is.

**Daniel Lopes:** Can you, can you give Us if Pedro or Stephen.

**Daniel Lopes:** Like, what is the gist of the work there?

**Daniel Lopes:** Is that the same PR that we.

**Daniel Lopes:** Had from before that was changing public categories or did we adapt to what.

**Daniel Lopes:** We discussed to be.

**Jose Farias:** We adapted.

**Jose Farias:** It's at the workspace level.

**Jose Farias:** So it was basically re.

**Jose Farias:** Implemented.

**Daniel Lopes:** Got it.

**Jose Farias:** And it's almost done.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Like, I think that we can roll out so.

**Daniel Lopes:** Because I don't think that changes what I'm saying.

**Daniel Lopes:** Like, what am I saying is just like preloading the workspace with the right.

**Daniel Lopes:** Doing the onboarding, you know.

**Daniel Lopes:** So does it still make sense?

**Daniel Lopes:** I can take a look just to make sure.

**Daniel Lopes:** Don't catch meeting that I'm okay.

**Stevie Kim:** Yeah, we, you know, the.

**Stevie Kim:** The doc that I put together for, you know, the improvements we need to make with the categories of subcategory or the subcategories.

**Stevie Kim:** It was, you know, it's layered, you know, like it's all.

**Stevie Kim:** All those different things that you guys were talking about.

**Stevie Kim:** And this is kind of the.

**Stevie Kim:** One of the.

**Stevie Kim:** These two tickets, I'm sorry, are part of that kind of bigger picture about what we were considering for improving that whole experience.

**Daniel Lopes:** But.

**Daniel Lopes:** Is he working despite on improving brand categorization?

**Daniel Lopes:** That's the workflow change, right?

**Jose Farias:** Yes.

**Jose Farias:** Yeah.

**Daniel Lopes:** For the own party.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** I think like the filter one for overview is super critical.

**Marcel Santilli:** As.

**Daniel Lopes:** Do you think that is higher?

**Marcel Santilli:** It is really, really embarrassing when I'm demoing and I get to an overview that is just completely wrong because I have no like content marketing for lovable.

**Daniel Lopes:** Yeah, like that.

**Daniel Lopes:** That is about.

**Daniel Lopes:** That's what I'm saying.

**Daniel Lopes:** Like that's.

**Daniel Lopes:** That is the fucking tab that I added there just for like, hey, this is just your public area.

**Daniel Lopes:** And then we really.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** I wasn't even sure that I.

**Marcel Santilli:** Right now you get two views.

**Marcel Santilli:** You get overview and you get prompts.

**Marcel Santilli:** Prompts is just a flood of hundreds of things you have no insights from because it's just a bunch of charts.

**Marcel Santilli:** Ups and downs.

**Daniel Lopes:** Yeah, that is my whole point.

**Marcel Santilli:** But then like, if you don't.

**Daniel Lopes:** Overview.

**Daniel Lopes:** Overview.

**Daniel Lopes:** We shipped the fucking bug basically because we didn't.

**Daniel Lopes:** Because of my.

**Marcel Santilli:** You still need filters, man.

**Marcel Santilli:** Like, you still need filter.

**Marcel Santilli:** I'm telling you, like, what's at the overview level.

**Daniel Lopes:** I remember you sent like a ticket with like a bunch of filters and groups.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** And it's super simple.

**Marcel Santilli:** It's just exact ones as the prompts.

**Marcel Santilli:** I mocked it up.

**Marcel Santilli:** I had the arrows, the descriptions, everything.

**Marcel Santilli:** So I'm just looking for that ticket because that ticket is like I spend like a Good two hours.

**Marcel Santilli:** Like thinking through it and mocking it up in the overview.

**Marcel Santilli:** We need filters and overviews.

**Marcel Santilli:** Like, I. I need to be able to at least turn off brand like prompts in the overview.

**Marcel Santilli:** Otherwise, like, I have no way to know.

**Marcel Santilli:** Like if things are going up and down on an aggregate level, you know, if it's just like a dump of a thousand prompts, you know, like, it's.

**Marcel Santilli:** That it's essentially the same filters as we have in prompts.

**Marcel Santilli:** Yeah.

**Jose Farias:** I can tackle that.

**Jose Farias:** Just because it seems so important.

**Jose Farias:** I can.

**Jose Farias:** I'm currently working on tying probing cadence to pricing tiers, which we haven't mentioned ever.

**Jose Farias:** I'm just working on it because it cuts our spend, but I can deprioritize that and tackle the filters.

**Stevie Kim:** Do we know where that was?

**Stevie Kim:** Was that one of Pedro's tickets or.

**Daniel Lopes:** I don't think we took it.

**Daniel Lopes:** I think it might be past the.

**Daniel Lopes:** It's the next P2.

**Daniel Lopes:** It's not.

**Jose Farias:** It's either there or I might know what happened with it because I won't go into the weeds on this.

**Jose Farias:** But the overview works different.

**Jose Farias:** So whoever took that ticket, I think maybe he didn't.

**Jose Farias:** He assumed that the filters applied to other screens and not the overview.

**Jose Farias:** So because we did homogenize the filters on all other screens except for the overview, which works different.

**Jose Farias:** So.

**Daniel Lopes:** Yeah, I think that was the name of the ticket.

**Daniel Lopes:** Normalize the filters.

**Daniel Lopes:** Yeah, I remember the ticket.

**Daniel Lopes:** But like, I think we can get rid of the.

**Daniel Lopes:** The category tab on the overview.

**Daniel Lopes:** That's like immediately.

**Daniel Lopes:** We can get rid of that.

**Daniel Lopes:** That was my legacy leaderboard that got renamed.

**Daniel Lopes:** I was.

**Daniel Lopes:** Even when I was doing that, I also shared that was a good idea, you know, so like.

**Daniel Lopes:** And a boot camp there and we improved.

**Leonardo Carpenedo Steffen:** Improved.

**Daniel Lopes:** My shitty idea.

**Jose Farias:** No, it's a good idea.

**Jose Farias:** It's just.

**Jose Farias:** Yeah, yeah, we.

**Jose Farias:** I can tackle that.

**Jose Farias:** I'll.

**Jose Farias:** Let's just say I'll do that.

**Jose Farias:** So just to be clear, prompts, the.

**Jose Farias:** The filters on the prompt screen, you want those on the overview screen.

**Jose Farias:** That's the gist of it, right?

**Jose Farias:** Yeah, okay, I got it.

**Jose Farias:** I'll take it.

**Marcel Santilli:** Because then.

**Marcel Santilli:** Because right now a few other tools, like when they are in the prompt, you can still see some summary overviews.

**Marcel Santilli:** Whereas right now the only way for us to see summary overviews and prompts is if you group by.

**Marcel Santilli:** That's why I said, like, group by is the only other one you can get insights from.

**Marcel Santilli:** So if you don't know if your ranking or citation reads going up or down, the only way to know that is, you know, if you apply filters to, you know, a subset of them, you know, so as you start to add like a bunch of.

**Marcel Santilli:** The idea is like right now tagging is in creating kind of tags is manual but because it's easy to check a bunch and apply them.

**Daniel Lopes:** Cool.

**Marcel Santilli:** But then the only other way to draw insights is if once you've tagged prompts then you can go in overview and essentially filter by a tag or filter by brand versus non brand or filter by stage of funnel.

**Marcel Santilli:** Those are the only ways you can draw insights from today from the product, which is the, the main thing you're trying to, to do.

**Marcel Santilli:** You know, until we make that super easy, which I think we're not as like far from it, you know.

**Daniel Lopes:** Yeah, no, that's, that's the thing I.

**Daniel Lopes:** Worked on the weekend.

**Daniel Lopes:** So we.

**Daniel Lopes:** It will generate tags automatically based on your taxonomy.

**Daniel Lopes:** But if we add the filter the way, the way we're thinking that Jose, if you take the seven days futures and group buy from prompts and put in the overview once I finish the workflows, then you can essentially group by anything.

**Daniel Lopes:** Yeah.

**Jose Farias:** Sorry, real quick technical note.

**Jose Farias:** It makes me nervous to be able to like filter by anything because of the snapshotting system that we have in place which in lieu of the data warehousing solution that we're close to but haven't finished.

**Jose Farias:** So I think we'll end up in a useful way.

**Jose Farias:** Like Daniel said, the three days versus three weeks thing, let's tackle the three day version and then we can talk about like filter and group by absolutely anything in the world which will take longer.

**Daniel Lopes:** Yeah, one, so like the text will generate tags basically.

**Daniel Lopes:** Okay, yeah.

**Marcel Santilli:** To clarify Jose, like the ask here is to do the like these for now, right.

**Marcel Santilli:** And, and then like later on it can be other filters so that like you can go like non branded, you know.

**Marcel Santilli:** And it's just that right now I.

**Marcel Santilli:** There's no aggregate view.

**Marcel Santilli:** Whereas like if there was a way to have an aggregate view like this, then it actually makes it like easier to know if it's going up or down, you know what I mean?

**Marcel Santilli:** And where.

**Marcel Santilli:** But the overview is the only view that you can actually see.

**Marcel Santilli:** More details chart.

**Marcel Santilli:** And so so then if you go here and you were able to filter by non brand only in evaluation only.

**Marcel Santilli:** Right.

**Marcel Santilli:** You would know if like this is truly what's happening or not, you know, as far as like your competitive presence and, and things like that, you know.

**Marcel Santilli:** And so I think this will be a, a quick, a quick win and and then like the.

**Marcel Santilli:** On the other side, like I. I'm wondering Daniel, if there's a way to like auto set some things in the admin side as far as like getting brands auto approved.

**Marcel Santilli:** You know, like some things to just like as we're getting more and more so.

**Marcel Santilli:** So that.

**Marcel Santilli:** Because right now I don't think anyone is going through and reviewing the queue and doing anything, you know, or auto generating more categories and filling them up with prompts.

**Marcel Santilli:** It's almost like the workflows are good enough and it's better to have some data and some more categories than not.

**Marcel Santilli:** But I don't know like, because I try to create some subcategories and it's.

**Marcel Santilli:** It's barely manual so I don't know if there's like a, A quick judo move there because if we do the pre work now essentially that also is like a quick solve.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like, which is in other words like go.

**Marcel Santilli:** As we're seeing brands.

**Marcel Santilli:** As we're seeing things like it's auto adding brands candidates into it without having to approve but also like if it's identifying like auto approving prompts.

**Marcel Santilli:** I don't know what the right like thing here, but we had 172 categories two months ago.

**Marcel Santilli:** Today we have 174.

**Marcel Santilli:** And those two were the like the two that I added, which is the vibe coding and another one.

**Marcel Santilli:** And so it's like at that pace, you know, it's too maybe a little bit too manual for us to add.

**Daniel Lopes:** Category, category like out of proving brands.

**Daniel Lopes:** That's easy.

**Daniel Lopes:** Like that's kind of like that was the natural path we wanted to follow.

**Daniel Lopes:** When I created the brand candidate stuff would be like whenever you start to get mentioned a ton of yeah, you automatically get a profile.

**Daniel Lopes:** And then because we create the categories we know we don't have like any like 80 categories so you're not going to get mentioned.

**Daniel Lopes:** So there's like a very low risk of like wrong like bad brands showing up automatically.

**Daniel Lopes:** That is doable.

**Daniel Lopes:** Creating categories automatically.

**Daniel Lopes:** That is not a good idea.

**Daniel Lopes:** For the same reason as you have like G2 and the other ones like they have a taxonomy team and they care about their categories and all that because you're gonna.

**Daniel Lopes:** And then for us it's even worse because we will run this prompts.

**Daniel Lopes:** So we created leaderboards for either each subcategory that's created.

**Daniel Lopes:** So that increases the cost quite a lot until we figure out, until we move to a bedrock and use open source models and the cost quite a bit.

**Daniel Lopes:** Figure out the frequency out of creating categories or creating categories, like, in kind of like a free form way, or, like, even creating more, like, tripling the number of categories here will triple the number of our cost.

**Marcel Santilli:** That's fair.

**Daniel Lopes:** But, like, brands understand, like.

**Marcel Santilli:** Like, I created this.

**Marcel Santilli:** I spend 30 minutes, like, because this is a customer that signed up and their category was bad.

**Marcel Santilli:** You know, it's overly generalized.

**Marcel Santilli:** They're essentially like a Panda Doc competitor kind of thing, you know, but with a.

**Marcel Santilli:** A sales room.

**Marcel Santilli:** And I. I went into the prompts and approved a bunch of them.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, did a bunch of work, essentially.

**Marcel Santilli:** Right.

**Marcel Santilli:** But then, like, what would we need to do to actually allow people to select this and have brands here?

**Daniel Lopes:** So, like, manage prompt.

**Daniel Lopes:** Sorry, I didn't see that.

**Daniel Lopes:** They're approved.

**Marcel Santilli:** They're active approved.

**Marcel Santilli:** I generated them.

**Marcel Santilli:** So that worked really well.

**Marcel Santilli:** The auto generate worked well.

**Marcel Santilli:** I approved them.

**Marcel Santilli:** So all of that worked really well.

**Marcel Santilli:** And that wasn't actually hard.

**Marcel Santilli:** But.

**Marcel Santilli:** But then this part, I'm not sure.

**Marcel Santilli:** Like, do we need to rerun 6,000 against it or.

**Daniel Lopes:** No, no, this is because we have the.

**Daniel Lopes:** The.

**Daniel Lopes:** We only list the brands that are approved.

**Daniel Lopes:** So, like, my hunch here is that we don't have a lot of the brands.

**Marcel Santilli:** We do, like, Panda Doc.

**Marcel Santilli:** Like, a bunch of them are here for sure.

**Daniel Lopes:** They're already approved as a. Yeah.

**Marcel Santilli:** And I know this also because the same thing happened, like, two months ago when I created this one still.

**Marcel Santilli:** There's, like, no brands here and there's only these two duplicates.

**Daniel Lopes:** Yeah, this is a workspace brand, probably.

**Daniel Lopes:** There's so.

**Marcel Santilli:** So it just seems like it's like a static snapshot of brands.

**Marcel Santilli:** Whereas, like, as we're probing and finding new and new brands in these categories and, like, we need to dynamically have them pulled, right?

**Marcel Santilli:** Like, ideally.

**Marcel Santilli:** But I just think this is probably.

**Daniel Lopes:** Not going backwards, you know, as in, like, it's not exactly right.

**Jose Farias:** Okay, you're right, Daniel.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So.

**Marcel Santilli:** So this feels like an important one to prioritize as well, because essentially, as we're collecting brands, we should be getting smarter about what brands are in those categories, you know, and then the subcategories I can keep creating, I'll just take like, a.

**Marcel Santilli:** Like four or five hours doing it because we asked the teams to do it for the tutorial teams, but no one did it.

**Marcel Santilli:** So.

**Marcel Santilli:** So then it's like, it's.

**Marcel Santilli:** It's kind of like, you know, even though they knew, for example, vibe coding wasn't a category, and it was very clear it didn't fit into anything Else lovable didn't fit into anything else.

**Marcel Santilli:** Like no one created it.

**Marcel Santilli:** So unless I do it, I don't think like it's going to happen.

**Marcel Santilli:** But it's okay because like I already have like the mental model for kind of like where to, to kind of add a little bit and then the prompt generation workflows are pretty good already.

**Marcel Santilli:** They're like 80% good there.

**Marcel Santilli:** And so then if we auto pull the brands into those categories like dynamically essentially like on a daily schedule or something, you know, and have.

**Marcel Santilli:** And I think what I suggested, I'm pretty sure I created a tick on this.

**Marcel Santilli:** I suggested like some kind of threshold to pull it, you know, and in other words, like it's not on first mention but maybe there's like when it crosses like some kind of threshold and then within the brand, for the category, within this brand view, there could be a tab that's just like potential potentially for approval essentially.

**Marcel Santilli:** Right.

**Marcel Santilli:** Because right now when you go into the brands tab in admin, it's really hard to make sense of 10,000 brands.

**Marcel Santilli:** But when you're within the context of a category, right.

**Marcel Santilli:** It's a lot easier to like look at, at those and be like, okay, no, this one should be in this category, you know, because you have the context of the category, you know.

**Daniel Lopes:** Yeah.

**Jose Farias:** That makes sense.

**Jose Farias:** Basically it's, it's currently only retroactive.

**Jose Farias:** We need to make it recurring is the change that we need to do.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Dan, do you have a sense like when we run the deep research on one brand, like what that cost is?

**Marcel Santilli:** Like, is it like a dollar per brand is a little less, A little more page check?

**Daniel Lopes:** Now I have a way to check that with the workflow.

**Daniel Lopes:** I can measure X, I can measure everything.

**Marcel Santilli:** Okay.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Pick up the cost.

**Marcel Santilli:** We might have to do like.

**Daniel Lopes:** A.

**Daniel Lopes:** Cheap research in volume.

**Daniel Lopes:** It's just like Perplexity or xfs.

**Daniel Lopes:** Which one is cheaper and faster and then we have a button to go deeper to the overviews becomes.

**Daniel Lopes:** Because it's also like it takes 10.

**Daniel Lopes:** Minutes to generate the.

**Daniel Lopes:** Takes like 10.

**Daniel Lopes:** It can take 30 minutes to generate the page.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Okay, so let me, I, I owe everybody like a little bit more of like a bigger mental picture of kind of like everything because there's a lot of tickets and what I don't want us to do is like go through this week just like aimlessly like you know, trying to like close tickets versus like figuring out what will actually move the, the needle.

**Marcel Santilli:** The.

**Marcel Santilli:** For me the biggest sense of urgency is the, like the, the sign up to wow is still not an easy path even when we're personally doing it on behalf of someone while sharing our screen.

**Marcel Santilli:** And so like that is the.

**Marcel Santilli:** The thing to solve.

**Marcel Santilli:** And then the next one is the fact that no one obviously upgraded.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like out of almost 200.

**Marcel Santilli:** And so there is a value gap there that's kind of like what I'm shaping without trying to boil the ocean.

**Marcel Santilli:** But our superpower is workflows.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like no other tool in this category has the ability to do the things we can do that we know how to do.

**Marcel Santilli:** And it's mostly just like a cost and latency game.

**Marcel Santilli:** So let me shape that.

**Marcel Santilli:** I have some thoughts on.

**Marcel Santilli:** On the whole thing and without kind of like boiling the ocean.

**Marcel Santilli:** But I think in the meantime, the, the filter, the taxonomy and these are the two things.

**Marcel Santilli:** Yeah, the filter taxonomy, the filter on overview taxonomy and then the approving brands or auto backfilling brands into the categories to.

**Marcel Santilli:** Yeah, I think that's second priority.

**Marcel Santilli:** Right.

**Daniel Lopes:** Compared to the taxonomy and the overview grouping and stuff.

**Daniel Lopes:** It's important.

**Daniel Lopes:** But if we can only tackle.

**Daniel Lopes:** Jose is on this.

**Daniel Lopes:** I'm on this and I'm going to.

**Daniel Lopes:** Hand it off to Steven or Pedro.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** We also have.

**Daniel Lopes:** What do we do with the learn area?

**Daniel Lopes:** Like that.

**Daniel Lopes:** Maybe we don't do that now.

**Jose Farias:** Right.

**Daniel Lopes:** What's the.

**Daniel Lopes:** What do you think is the prioritization there?

**Daniel Lopes:** The.

**Marcel Santilli:** Say that again.

**Daniel Lopes:** What do you do with the learn area?

**Daniel Lopes:** What do you think it's prioritization there?

**Daniel Lopes:** Do we care about that?

**Daniel Lopes:** There's also work on the.

**Daniel Lopes:** On the workflows for improving the content pages that we're creating.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I think the learn area will unlock more growth so that we can start taking a shot of being sighted when people search for this category for us itself.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so it's more like essentially like create a blog area that is super mvp.

**Marcel Santilli:** But I don't think it's necessarily more important than unlocking some of these things because we won't get to any revenue this month if we don't like get to a thing that's like super clear value.

**Marcel Santilli:** Right.

**Jose Farias:** Yeah.

**Daniel Lopes:** We could.

**Daniel Lopes:** Could likely get George Main on this.

**Daniel Lopes:** Right.

**Marcel Santilli:** Start designing what the learning would look.

**Daniel Lopes:** Like with a pillar page and the article page.

**Daniel Lopes:** Pretty easy lift and it can create that static and then we come in after and because the CMS part is there already, so it's probably.

**Daniel Lopes:** If we have the design, it's pretty straightforward.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Is there anything else, Stevie, that's like that I haven't stayed on top of.

**Daniel Lopes:** What we're the last week.

**Daniel Lopes:** So it sounds like the two main priorities.

**Daniel Lopes:** This can be divided between Pedro or Stevon and.

**Daniel Lopes:** This as well.

**Daniel Lopes:** So those are all doable.

**Daniel Lopes:** We can probably do all this this week, you know, so.

**Daniel Lopes:** And then the other stuff that we had in motion, like pricing and all that stuff can take a backseat for now.

**Daniel Lopes:** And I can get.

**Daniel Lopes:** We could get George Main on this as well.

**Daniel Lopes:** Essentially just create a blog or.

**Marcel Santilli:** Yeah, and I have a lot more time tomorrow because I want to shape essentially, like.

**Marcel Santilli:** Like working backwards from what we want to kind of announce each week, you know, to keep the.

**Marcel Santilli:** The drum beat going.

**Marcel Santilli:** Like, with things like this, it's really important.

**Marcel Santilli:** Like, you got like, our Tweet got like 1.4 million views.

**Marcel Santilli:** Like, we got, like, good attention.

**Marcel Santilli:** And now it's like every week you kind of got to stay with it for a little bit to.

**Marcel Santilli:** To keep hammering home, you know, people that saw it but maybe didn't quite take the, you know, and then we'll.

**Marcel Santilli:** We'll get also a lot of feedback from the strategy sessions that we're doing on.

**Marcel Santilli:** On behalf of people as well.

**Marcel Santilli:** So.

**Stevie Kim:** Yeah, there was something else that we were gonna.

**Stevie Kim:** That we talked about in the standup that we were gonna.

**Marcel Santilli:** I just realized I'm 15 minutes late to this other meeting, but.

**Marcel Santilli:** But I'll follow.

**Daniel Lopes:** Yeah, go ahead.

**Daniel Lopes:** I think we can spend another 15 here.

**Daniel Lopes:** 10 minutes just to.

**Daniel Lopes:** What are you saying, Steve?

**Stevie Kim:** Okay, so as I said, we, you know, I started that shaping doc for the.

**Stevie Kim:** Improving the categorization, but we were also talking about moving the prioritization up for recommended custom prompts, you know, thinking about, you know, how to get people to.

**Stevie Kim:** To increase their use or, you know, even start their use of creating custom prompts.

**Stevie Kim:** I think it's hard to know where to start there.

**Stevie Kim:** So if we have those recommended, some recommended for them, that'll still count towards their count of custom prompts, but they won't have to start from scratch and do that research themselves and investigation.

**Stevie Kim:** And so that's.

**Stevie Kim:** We have a ticket already for that.

**Stevie Kim:** And it's on.

**Stevie Kim:** It's on the notion doc that I linked to the calendar invite.

**Stevie Kim:** But yeah, so that was the one thing that I wanted to kind of get a beat on as far as prioritization, besides the categorization improvements that we want to make.

**Daniel Lopes:** Recommended prompts touch the stuff.

**Stevie Kim:** Yeah.

**Daniel Lopes:** For the.

**Daniel Lopes:** The generation.

**Daniel Lopes:** I'm just taking notes for me here.

**Marcel Santilli:** And then I can.

**Daniel Lopes:** It's a lot of the stuff.

**Daniel Lopes:** That's the stuff that I did.

**Stevie Kim:** Okay.

**Daniel Lopes:** All right.

**Marcel Santilli:** Got a Call.

**Leonardo Carpenedo Steffen:** Talk to you guys later.

**Daniel Lopes:** Okay, I'll.

**Daniel Lopes:** I'll read all this stuff.

**Daniel Lopes:** Yeah, this is.

**Daniel Lopes:** This is.

**Daniel Lopes:** I have the workflows.

**Daniel Lopes:** I'll share more today.

**Leonardo Carpenedo Steffen:** And.

**Daniel Lopes:** The creation of recommended prompts is kind of related to this because once.

**Daniel Lopes:** You have the Personas basically the prompt generation in the admin is totally packed to your category so you need something to narrow down the research.

**Daniel Lopes:** So it has to be a competitor or has to be a category or something like this.

**Daniel Lopes:** But once we have the taxonomy you get there and the taxonomy you get like verticals and industry and topics.

**Daniel Lopes:** We generate like a cloud of tags basically that we can use to recommend generating prompts and recommend then from there it's probably better to wait for creating recommended prompts until we have the.

**Daniel Lopes:** I think there's two things that are more important and this I'm going to hand off to anybody that has been with today because the backend is ready.

**Daniel Lopes:** I'm just merging the pr.

**Stevie Kim:** Yeah the prioritization was to do the improvements to categorization and then the next was kind of thinking about these product or prompt recommendations.

**Stevie Kim:** So it wasn't something that we were focused on right now, just something that we're thinking about that needs to be prioritized next.

**Daniel Lopes:** Is there anything else that's like big stuff from the launch that we like?

**Daniel Lopes:** There's the stuff that we just filed.

**Stevie Kim:** Yeah, I was wearing need to get.

**Stevie Kim:** There's a couple of those.

**Stevie Kim:** The pricing one I think the pricing workflow and then the.

**Stevie Kim:** There's just a couple of tickets around adding some.

**Stevie Kim:** I don't know, they're not release I guess they're sections to improve the brand page from a growth and cross linking perspective.

**Stevie Kim:** And I did say that, you know.

**Daniel Lopes:** There'S a ton of to.

**Daniel Lopes:** Yeah, there's a ton of stuff on growth.

**Stevie Kim:** Yeah.

**Stevie Kim:** And we do need to make some progress on those because.

**Stevie Kim:** Yeah I forgot to mention that in standup.

**Stevie Kim:** So I'm glad.

**Stevie Kim:** Yeah I thought now but I was going to try to carve out some time to tackle those if possible.

**Stevie Kim:** But yeah, those are some that we need to make some progress on to help support the growth team.

**Daniel Lopes:** Yeah, I can do a pass on them and like see because I wrote the whole thing so I can figure out how to hand it off all the content types and all that stuff.

**Daniel Lopes:** It was actually a prototype for the stuff that we're doing in the content os but now that the workflows are migrated and out of the other system then we can do whatever we want on this side of things.

**Daniel Lopes:** I Will take a pass on that.

**Stevie Kim:** Yeah, I think I tagged a couple of their higher priority tickets.

**Stevie Kim:** I. I can't remember if I tagged them as P1 like stabilize or launch.

**Stevie Kim:** I just wanted to make sure that we were, you know, keeping them in mind to prioritize those.

**Daniel Lopes:** I think I will write also write.

**Daniel Lopes:** A doc or what I was describing during the cause.

**Daniel Lopes:** I'm not sure if Marcel understood what I was saying.

**Daniel Lopes:** As in like you don't really have to pick your category as you go through the onboarding flow more like this is the categories you have which one you think makes more sense to you.

**Daniel Lopes:** And right now it's almost like this autocomplete that just narrows it super aggressively.

**Daniel Lopes:** So it can be just like pick 10 categories if you want.

**Daniel Lopes:** That's completely unrelated and that will just load the workspace.

**Stevie Kim:** If I remember correctly, the way the onboarding flows that when the user selects a category on the next step for the competitors that we suggest is based on the category category that they selected.

**Jose Farias:** The prompts too.

**Stevie Kim:** And prompts.

**Daniel Lopes:** Yeah, yeah, the prompts for sure.

**Marcel Santilli:** But I mean like you could technically.

**Daniel Lopes:** Pick because we are relying on the workflow and the workflow returns one really good category most of the time and then a handful of shitty ones and then we only cap at like three and then you see three, you know, and then one is reselected.

**Daniel Lopes:** But if we have.

**Daniel Lopes:** If we change the UI to be like maybe like.

**Daniel Lopes:** I don't know if the UI would be user interface would there would make a big difference.

**Daniel Lopes:** But I think it would as in like it's not an autocomplete.

**Daniel Lopes:** We load.

**Daniel Lopes:** We sort them by the order that the researcher our workflow returns and then you can select as many as you want.

**Daniel Lopes:** You know, as long as maybe you should cap it like something like five or something.

**Daniel Lopes:** So you don't load the workspace with like a thousands.

**Daniel Lopes:** But even if they did it wouldn't be a problem.

**Daniel Lopes:** So the cate and then we change the copy to be like less about getting the category right and it's more like what are the faces that you think your product relates to?

**Daniel Lopes:** You know, because if we're doing like full categorization then it's just I need to get my perfect category but I just pick to the ones that you're interested in, you know.

**Stevie Kim:** Yeah, there's.

**Stevie Kim:** For the.

**Stevie Kim:** The doc that I created, it was just like a draft of the basic.

**Stevie Kim:** Like the basic scenarios where you know, the.

**Stevie Kim:** The lack of categories causes trouble.

**Stevie Kim:** So I kind of put like it and framing it in two ways of, like, what are the opportunities and what are their problems?

**Stevie Kim:** Just because we kept missing stuff in different areas that, you know, we were tackling.

**Stevie Kim:** And so I wanted to get this kind of documented.

**Stevie Kim:** And so I asked, you know, engineering on Friday to take a look and add or edit things as needed so we could kind of discuss it today.

**Stevie Kim:** But it sounds like you guys have a different way of looking at it where.

**Daniel Lopes:** No, I don't think so.

**Daniel Lopes:** Let me.

**Daniel Lopes:** Let me read it first.

**Daniel Lopes:** But.

**Stevie Kim:** Well, I think.

**Stevie Kim:** I mean, I.

**Stevie Kim:** It's like you, like, I. I was approaching it from like, what exists right now, thinking that.

**Stevie Kim:** That.

**Stevie Kim:** Because that's how it's always existed from when I started, you know, working on this, that that was, like, very much intentional.

**Stevie Kim:** And so just your Marcel's discussion opened up that.

**Stevie Kim:** Oh, okay.

**Stevie Kim:** So maybe this way that we are leaning on categories maybe wasn't as intentional as I, you know, initially thought and stuff.

**Stevie Kim:** So it kind of opens up to, you know, to think about it in a wider sense and not force ourselves into just fixing what currently exists.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, I can take a read on what Europe.

**Daniel Lopes:** Just like I didn't read before the meeting.

**Daniel Lopes:** Yeah, then.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** But essentially it.

**Daniel Lopes:** Categories to me, when you log in, they are just like, there to bootstrap the prompt.

**Daniel Lopes:** You have to help group things.

**Daniel Lopes:** That's it.

**Marcel Santilli:** And.

**Daniel Lopes:** But not to pin the workspace to a specific.

**Daniel Lopes:** You can only have one or two or whatever.

**Stevie Kim:** Yeah.

**Stevie Kim:** I mean.

**Stevie Kim:** And one of the questions I put in this doc is like.

**Stevie Kim:** Is like, why do we have primary subcategories?

**Stevie Kim:** So these are questions that, you know.

**Daniel Lopes:** Yeah, that was for the public area only, so I gotcha.

**Daniel Lopes:** The primary is whatever you show up in your leaderboard.

**Daniel Lopes:** So you're not showing multiple categories.

**Daniel Lopes:** But we could have.

**Daniel Lopes:** Because that was literally.

**Daniel Lopes:** Because I just didn't want to have.

**Daniel Lopes:** When you go into something like this, I didn't want to have like a bunch of stuff here.

**Stevie Kim:** Yeah, yeah, yeah, that makes sense.

**Daniel Lopes:** But it's not because of the private area.

**Daniel Lopes:** So you would be like, like a hint, like, I think does that.

**Daniel Lopes:** So you have like dozen things here, you know.

**Daniel Lopes:** Yeah, they put that at the footer.

**Daniel Lopes:** But, like, a lot of the stuff is just because of the public area.

**Daniel Lopes:** The private area is almost like the category is just a scaffold, like a beginning, like a template to start.

**Stevie Kim:** Okay, right.

**Daniel Lopes:** That's how.

**Daniel Lopes:** How I was thinking.

**Daniel Lopes:** So that's why I'm saying, like, if you.

**Daniel Lopes:** If you person like this point that you may.

**Daniel Lopes:** May hear, you get just close enough that User doesn't find bigger category and then you find the one that's close enough.

**Daniel Lopes:** It's almost like that is.

**Daniel Lopes:** Fine, you.

**Stevie Kim:** Know, and if that's debatable, I don't know.

**Stevie Kim:** Jason, Jason was pretty adamant about like if, if he's like if they, if he or someone like him doesn't find their category that they're going to, that they're going to balance their, you know, from the drop off, from the onboarding flow.

**Stevie Kim:** I haven't seen that so far.

**Stevie Kim:** As I said, like the brand selection is where most people drop off, which doesn't really make sense to me.

**Stevie Kim:** But unless they don't have a brand, you know, maybe they're just like exploring, you know, probably that's what I'm saying.

**Daniel Lopes:** You know that I think there is.

**Daniel Lopes:** Here the, the work of just like changing the design to like reframing the.

**Daniel Lopes:** Sign up to be about like I'm.

**Daniel Lopes:** Not going to be able to sign up but to be about.

**Daniel Lopes:** Not pick your category but help us load your workspace and pick the topics that you think that are relevant to you that you want to monitor and then, and then you're not going to be like, oh, what is my category?

**Daniel Lopes:** It's just like.

**Stevie Kim:** Yeah, so you're, you're just looking Spotify closing.

**Stevie Kim:** You're closing the job to be done basically.

**Stevie Kim:** Yeah, more.

**Stevie Kim:** More in the sense of.

**Stevie Kim:** Than this arbitrary.

**Stevie Kim:** Yeah.

**Daniel Lopes:** Group that we have in the pooping that weird.

**Stevie Kim:** Yeah.

**Stevie Kim:** Okay.

**Daniel Lopes:** It's essentially like a Spotify choose the genres that you like kind of thing.

**Daniel Lopes:** You know, so.

**Daniel Lopes:** Or Apple Music and then they don't feel trapped.

**Daniel Lopes:** Yeah, yeah, yeah.

**Daniel Lopes:** And then if we add the stuff that, that we.

**Daniel Lopes:** You were talking about in the recategorization, all that then it makes sense that you can just go back there and say ah, I don't like about add more you know, and add random like almost like I don't care.

**Daniel Lopes:** Like I'm in vibe coding space and I'm now adding mba all kind of things, you know, so we don't have to be like that constrained and let people do that.

**Daniel Lopes:** But if affects your public area then it's like we need to actually pin you correctly.

**Daniel Lopes:** But if it's just a workspace, you're just messing up your own workspace, who cares, you know?

**Stevie Kim:** Yeah, yeah, yeah, that makes a lot of sense.

**Daniel Lopes:** Let me write that down in the document and then I just share.

**Daniel Lopes:** But I'll, I'll.

**Daniel Lopes:** Yeah, I'll read yours and I'll share.

**Daniel Lopes:** This with you in a bit.

**Daniel Lopes:** I had the now that everybody dropped.

**Daniel Lopes:** Like, I put another meeting on Fridays for us to be just like, maybe you just you, me and Marcel.

**Daniel Lopes:** And then you can have the other guys optional.

**Daniel Lopes:** So we can have this kind of conversation there.

**Daniel Lopes:** Because we kind of derailed your whole tactical meeting with all.

**Stevie Kim:** I mean, we honestly, so.

**Stevie Kim:** Yeah, I mean, so engineering.

**Stevie Kim:** Like, we.

**Stevie Kim:** We have a lot of these discussions during our standups and I'm going to talk with the guys to see if they want to continue those.

**Stevie Kim:** They've actually been pretty helpful because they, we just, you know, they're not traditional standups, which I don't feel are very useful, but they're.

**Stevie Kim:** They're discussing, like we are constantly discussing things and working through things, and so they've been pretty helpful.

**Stevie Kim:** I think the weekly, the today's meeting sometimes gets like that this one becomes the most confusing, I think, for people because, like, everything that we've kind of talked about and prioritized, we don't really get around to.

**Stevie Kim:** And so I think it would be helpful breaking that up, that discussion up.

**Stevie Kim:** Like you said, on Fridays.

**Stevie Kim:** Yeah.

**Stevie Kim:** And I, and I can really just honestly do the same, take notes, like, really try to get, you know, pick your guys's brains and really kind of get that clarity about what is the highest priority.

**Stevie Kim:** Because Marcel does have more of like, you know, the, the sales field kind of experience of like, of that which, you know.

**Daniel Lopes:** Trying to use and all that in the context of demos.

**Daniel Lopes:** That's super valuable.

**Stevie Kim:** It is, yeah.

**Stevie Kim:** And so getting that distilled on Friday would be really helpful.

**Stevie Kim:** So what I'm actually not sure of is like, what would Monday be used for?

**Stevie Kim:** Because, like, we think we should cancel.

**Stevie Kim:** Yeah, because that's what I'm thinking too.

**Stevie Kim:** Like, we don't.

**Stevie Kim:** A lot of times we're just repeating what we talked about in stand up or it gets completely derailed.

**Daniel Lopes:** Yeah, we can do this.

**Daniel Lopes:** So like we have the Friday meetings, which is like you, me and Marcel and I can play the engineer.

**Daniel Lopes:** So Marcel doesn't pitch something.

**Marcel Santilli:** That's.

**Daniel Lopes:** The right solution, but fucking hard to do.

**Daniel Lopes:** Like, we're just talking about.

**Daniel Lopes:** And I'm like, I think we can just remove the things here and add futures.

**Daniel Lopes:** And he's like, we should auto categorize.

**Daniel Lopes:** That's going to take.

**Daniel Lopes:** So like, I can do that job.

**Daniel Lopes:** And I'm also going to be setting up the.

**Daniel Lopes:** Some workspaces for myself here.

**Daniel Lopes:** Like, we're going to be launching the frameworks I'm going to be creating the workspace on.

**Daniel Lopes:** Check that for me so I can to manage the framework AI.

**Daniel Lopes:** But anyway, so we can have Friday meeting as our strategy.

**Daniel Lopes:** High level meeting for the product.

**Daniel Lopes:** Anything about roadmap.

**Daniel Lopes:** Sometimes we can bring in Jason, see if we're going to announce something the following week.

**Daniel Lopes:** We'll bring in Jason for him to be aware of what we're talking about and we can use the kidney of the meeting to just go through what happened in the week and then we have the second half of the meeting of high level forward looking features and.

**Daniel Lopes:** Ideas and stuff like that.

**Daniel Lopes:** And then.

**Daniel Lopes:** Yeah, cancel this meeting and then have the data send out.

**Daniel Lopes:** Probably a good idea because the guys are also pretty smart.

**Daniel Lopes:** So they have product ideas.

**Daniel Lopes:** They have.

**Stevie Kim:** Oh yeah, Pedro created.

**Stevie Kim:** So I think he did it either over the weekend or Friday night or something like he created so many different dashboards and like identified, you know, users that we might want to actually talk to.

**Stevie Kim:** And so they.

**Stevie Kim:** I mean I have my own product analytics, you know, that I. Dashboards that I created.

**Stevie Kim:** But he went through and created everything under the sun and so.

**Stevie Kim:** Or not dashboards, but insights, whatever.

**Stevie Kim:** Post hog.

**Daniel Lopes:** Post hog.

**Daniel Lopes:** Oh, nice.

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** So if you look at insights, there's just a huge amount that Pedro created and then I have my product analytics dashboard that has the insights that I created.

**Stevie Kim:** And so yeah, there's just a ton of stuff.

**Daniel Lopes:** This is.

**Daniel Lopes:** No, this is not our.

**Stevie Kim:** No, this is.

**Stevie Kim:** That's different.

**Stevie Kim:** That's not a dashboard.

**Daniel Lopes:** Can you send me the link after so I can take a look?

**Stevie Kim:** Yeah, it's really.

**Stevie Kim:** So if you go to project and then.

**Stevie Kim:** Oh wow.

**Stevie Kim:** So you're in the default project.

**Stevie Kim:** That's why.

**Stevie Kim:** So if you go to the check that.

**Stevie Kim:** Or is that how you get there?

**Daniel Lopes:** I think, I mean the team account.

**Stevie Kim:** Let's see here.

**Stevie Kim:** Yeah, so you need to be.

**Stevie Kim:** You were in the, I think the Growth X project.

**Stevie Kim:** So you need to go to the check that project.

**Daniel Lopes:** I don't have.

**Daniel Lopes:** It's the team account.

**Daniel Lopes:** Are you.

**Stevie Kim:** Yeah, it's under the same.

**Stevie Kim:** Yeah, it's the same account.

**Daniel Lopes:** So let's mess up my cooking.

**Daniel Lopes:** I'll check after.

**Stevie Kim:** Yeah, but under.

**Stevie Kim:** It's under the.

**Stevie Kim:** As I said, it's under the check that project.

**Daniel Lopes:** I'll check after.

**Daniel Lopes:** But anyway, it's like that.

**Daniel Lopes:** Organize the stand up however you think.

**Daniel Lopes:** It'S best and change the time if you want to.

**Daniel Lopes:** And Marcel doesn't have to be there.

**Daniel Lopes:** I don't have to be there.

**Daniel Lopes:** Maybe I join sometimes.

**Stevie Kim:** But yeah.

**Daniel Lopes:** And then the Friday one is the actually one that we, the two of us discussed and we can share the videos with the guys afterwards so they can watch and we can keep it open, like, optional for them to join.

**Daniel Lopes:** So if they want to join, they can join.

**Daniel Lopes:** But no, that would be confusing and.

**Daniel Lopes:** And, yeah, a little bit.

**Daniel Lopes:** But it's gonna be like this.

**Stevie Kim:** No, that sounds great.

**Stevie Kim:** I think that'll be a lot more efficient.

**Daniel Lopes:** So how's the support doing?

**Daniel Lopes:** Like, do we get a lot of questions?

**Daniel Lopes:** I didn't check.

**Stevie Kim:** I haven't had time to check this morning, but I know Pedro, like, has done it.

**Stevie Kim:** I've done like, five.

**Stevie Kim:** So if you go to unassigned.

**Stevie Kim:** Yeah, there's like, one unassigned, but yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So we're getting something.

**Daniel Lopes:** We gotta send some people messages.

**Daniel Lopes:** That's a start.

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** And some of it is just.

**Stevie Kim:** They're like, oh, duh, that, you know, like, that's how you do that, you know, and it is kind of like an obvious thing.

**Stevie Kim:** And they're just like, oh.

**Stevie Kim:** But then there's, you know, again, like, the subcategory.

**Stevie Kim:** Like, hey, I didn't see my subcategory there, you know, during onboarding, and now I'm stuck on this one and that type of thing.

**Stevie Kim:** So there's been a little bit of that.

**Stevie Kim:** But, yeah, I haven't.

**Stevie Kim:** I'm kind of behind on watching the recordings, which have been really helpful to watch.

**Stevie Kim:** I didn't get to.

**Stevie Kim:** I had too much to do on Friday, so I didn't get a bunch of looked at.

**Stevie Kim:** But that's where a lot of, you know, the tickets that, you know, we've, like, whether they're bugs or, you know, little improvements that you can see people kind of struggling in certain areas.

**Stevie Kim:** And then I'm just kind of like, monitoring time on page, you know, to, like, are there any areas, especially during the onboarding flow, but also, you know, like, throughout the.

**Stevie Kim:** The app, like, where are people spending their most time on and are they having trouble in any areas?

**Stevie Kim:** And then just watching recordings there.

**Stevie Kim:** But I've been randomized a lot lately, so I haven't been able to sit down and focus on any one thing.

**Daniel Lopes:** Yeah, that's super important.

**Daniel Lopes:** So I think that's the thing that.

**Daniel Lopes:** Like.

**Daniel Lopes:** Everybody should be doing post launch.

**Daniel Lopes:** So it's nice that now that things.

**Daniel Lopes:** Are starting to stabilize a little bit so, like, Marcel can keep an eye on what's happening on Demoland.

**Daniel Lopes:** And these are the things that I need to wall people in 10 minutes.

**Daniel Lopes:** And that can be more manual work.

**Daniel Lopes:** So we can create a category before we can load the workspace.

**Daniel Lopes:** If we see a Good lead.

**Daniel Lopes:** Come in.

**Daniel Lopes:** We can calibrate the workspace for them and send a message afterwards.

**Daniel Lopes:** Hey, I saw that you came in and got stuck.

**Daniel Lopes:** We did this for you.

**Daniel Lopes:** And then there's the bottom.

**Daniel Lopes:** So there's the top down there, the bottom up.

**Daniel Lopes:** And we need people doing both.

**Stevie Kim:** So, Marcel, I. Yeah, I actually wanted to talk about that because I was.

**Stevie Kim:** We had, I thought, a plan on the sprint side of things where Tyler was going to, like, I gave him admin access and stuff, too, so he could create workspaces for prospects.

**Stevie Kim:** And then, like, if they convert, then, you know, the.

**Stevie Kim:** I can't remember what.

**Stevie Kim:** What.

**Stevie Kim:** What are we calling them now?

**Stevie Kim:** Account manager or, you know, whoever's Engagement manager.

**Stevie Kim:** Yeah, engagement manager.

**Stevie Kim:** They are.

**Stevie Kim:** You know, they've got something already started and, you know, they can work with the client to improve their.

**Stevie Kim:** The workspace and everything.

**Stevie Kim:** So there's.

**Stevie Kim:** We have kind of a.

**Stevie Kim:** A process there set up, and there might be a disconnect between, like, Marcel and Tyler about, you know, maybe, like, maybe Marcel is assuming those are done.

**Stevie Kim:** And maybe, like, so I don't know, I'll talk to Tyler to kind of figure out, like, hey, is.

**Marcel Santilli:** Are.

**Stevie Kim:** Is that being done or are you guys.

**Stevie Kim:** Are you and Marcel tackling different prospects or how is that working?

**Marcel Santilli:** Then?

**Stevie Kim:** Now we have Nigel, so we need to kind of figure out, like, how that's.

**Stevie Kim:** Who's.

**Stevie Kim:** Who's the DRI for creating workspaces for the demo reasons for, you know, sales, and then moving that on those workspaces on as the customer or prospect continues in the funnel.

**Daniel Lopes:** Yeah, yeah, I think that's.

**Daniel Lopes:** That's good to clarify.

**Daniel Lopes:** I think it's also that Marcel is just trying to create ahead, like, knowing.

**Daniel Lopes:** Which ones are coming in, and he checks before and, like, tries to create regardless of who's in charge of it, just to make sure there's one.

**Daniel Lopes:** And then he's hitting this like, oh, I can't create the way I want kind of thing.

**Daniel Lopes:** So, yeah, I think that us doing the.

**Daniel Lopes:** Doing the change that we discussed today will cover his ability to do that.

**Daniel Lopes:** So even if it's not set up.

**Marcel Santilli:** When he does it real quick right before.

**Stevie Kim:** Yeah, yeah, yeah.

**Stevie Kim:** That makes a lot of sense.

**Stevie Kim:** And the reason why that's been paused is because of the.

**Stevie Kim:** I mean, what he talked about, like, he.

**Stevie Kim:** He created the vibe coding category, but nobody knew that.

**Stevie Kim:** And like, I. I have the delivery team make tickets for us because it takes a very focused, concentrated effort to.

**Stevie Kim:** When you make a new subcategory, to make sure there's enough brands in there, there's enough, you know, prompts that it.

**Stevie Kim:** Because you don't want to make one and just have like one brand in there.

**Stevie Kim:** And so it is very much like this, this concentrated effort.

**Stevie Kim:** And so I.

**Stevie Kim:** And then we paused all that during the last couple of weeks up to launch because we didn't want any, you know, anything forgotten about where there's like an empty category.

**Stevie Kim:** And then I saw one for five coding.

**Stevie Kim:** I'm like, no, where'd that come from?

**Daniel Lopes:** Yeah, I think the things we talked about today cover all of those things.

**Daniel Lopes:** So in different orders of priorities, one.

**Daniel Lopes:** Is just clear the short term pain of the overview page, maybe confusing people and adding the groups.

**Daniel Lopes:** And then fast follow would be like figure out turn the onboarding from selector category to pick your preferences.

**Daniel Lopes:** And then third then we have all.

**Daniel Lopes:** The taxonomy stuff for auto grouping that.

**Daniel Lopes:** You auto organize your prompts.

**Daniel Lopes:** And somewhere in there like fourth priority.

**Daniel Lopes:** Is making the management of categories easier.

**Daniel Lopes:** And probably even before that there is.

**Daniel Lopes:** A lot before there, there's auto approving brands.

**Daniel Lopes:** That again mentioned a ton.

**Stevie Kim:** Yeah, yeah.

**Daniel Lopes:** That to me it's almost like one day of work.

**Daniel Lopes:** Probably the auto approval of brands.

**Daniel Lopes:** Like if the brand shows up more than ten, like a hundred times and proven our research.

**Daniel Lopes:** I just need to figure out the cost.

**Daniel Lopes:** Yeah, the cost of approval.

**Daniel Lopes:** Yeah, I think that's like, that's if we, if we did all these five things, pretty much like we solved all the things that you're already getting from like looking at sessions and people's confusion and Marcel's.

**Daniel Lopes:** All data points for like those five things.

**Daniel Lopes:** I think.

**Stevie Kim:** Yeah, absolutely.

**Stevie Kim:** It's going to help a lot.

**Stevie Kim:** Especially just as I said, there were, there's, there's layers to it that we just need to, to tackle.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right.

**Daniel Lopes:** I think we have our bases covered.

**Daniel Lopes:** I'll just send the document.

**Daniel Lopes:** We have a plan.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And that's our.

**Daniel Lopes:** That's like feel free to message the guys in that we organize the calendar and they would.

**Daniel Lopes:** The three of us would do the Friday ones.

**Stevie Kim:** Sounds good.

**Daniel Lopes:** All right, thank you.

**Daniel Lopes:** Good job on the launch of this.

**Stevie Kim:** Yeah.

**Stevie Kim:** I feel, I feel like it's one of those strange things where you just like don't feel like you're getting anything done because you're so just like hurting cat and you know, in a traffic playing traffic cop, like stop, go.

**Stevie Kim:** You know, and you don't feel like.

**Stevie Kim:** Yeah, it's one.

**Stevie Kim:** Yeah.

**Stevie Kim:** One of those strange feelings of just like, am I helping here or am I making things harder?

**Daniel Lopes:** You also landed on the thing with.

**Daniel Lopes:** The plane in midair.

**Daniel Lopes:** I think, like.

**Daniel Lopes:** Moving forward, like, from launch forward.

**Daniel Lopes:** Now, like, for example, like, now we.

**Daniel Lopes:** Can see all the five things that matter now.

**Daniel Lopes:** And then you're gonna keep getting bored up and start.

**Daniel Lopes:** Yeah.

**Stevie Kim:** Hindsight.

**Stevie Kim:** Right?

**Stevie Kim:** Yeah.

**Stevie Kim:** It's.

**Stevie Kim:** We've.

**Stevie Kim:** Yeah.

**Stevie Kim:** We're in a place where we're actually like, oh, right.

**Stevie Kim:** That we knew that was gonna bite us in the ass.

**Stevie Kim:** And it.

**Stevie Kim:** And it is.

**Stevie Kim:** And we didn't have time to do it.

**Stevie Kim:** And now we can have time to do it.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right.

**Marcel Santilli:** Thank you.

**Stevie Kim:** Thanks.

**Stevie Kim:** Bye.
