# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-28
time: 16:00 UTC
duration: 27 minutes
recording_id: 117822122
fathom_url: https://fathom.video/calls/546444360
share_url: https://fathom.video/share/69Lz4-qUiGggNxfzP8dho_RsMGwDtoUK
source: fathom
enriched_on: 2026-02-28 00:00 UTC

## Participants

- **Stevie Kim** (stevie@growthx.ai, GrowthX) — Product Manager, meeting organizer
- **Pedro Steimbruch** (pedro@growthx.ai, GrowthX) — Engineer
- **Jose Farias** (jose@growthx.ai, GrowthX) — Engineer
- **Estevão Mascarenhas** (estevao@growthx.ai, GrowthX) — Engineer
- **Leonardo Carpenedo Steffen** (leonardo@growthx.ai, GrowthX) — QA / Testing
- **Marcel Santilli** (marcel@growthxlabs.com, GrowthX) — CEO / Observer
- **Daniel Lopes** (daniel@growthxlabs.com, GrowthX) — Observer
- **Jason Gong** (jason@growthx.ai, GrowthX) — Observer
</metadata>

---

## Summary

The team conducted a final launch readiness sync covering critical P0 onboarding bugs, QA findings, billing system deployment, and metrics validation. Key deliverables discussed: P0 category validation fix, onboarding failsafe implementation, duplicate brand cleanup, and Citation Share metric verification ahead of launch.

---

## Context

This meeting represents the final coordination checkpoint before CheckThat's go-live. The team reviewed blockers and near-term priorities across engineering, QA, and product. A P0 bug preventing single-subcategory onboarding completions required immediate attention, along with supporting measures to make the onboarding flow more resilient to workflow failures. Separately, the team addressed accumulated technical debt in brand deduplication and metrics calculations, preparing the analytics layer for production use.

The team also confirmed that billing infrastructure was live in production (connected to Stripe sandbox for safe testing) and that the overall feature set was ready for launch pending resolution of identified QA and engineering tasks.

---

## Relevance

**CheckThat Launch:** Directly addresses final readiness checks before go-live; documents critical bugs, QA priorities, and engineering deliverables.

**Product Quality:** Onboarding friction and metrics accuracy are core to user experience and trust; decisions here shape the initial launch impression.

**Technical Debt:** Brand deduplication and metrics review prevent post-launch support burden and ensure analytics reliability.

---

## Overview

- **Onboarding Blocker (P0):** A validation guard bug prevents users from completing onboarding when selecting only one subcategory. The form submits the selection as `primary_subcategory_id`, but the guard checks `subcategory_ids`. Fix: concatenate both parameters in the validation guard. Estevão will implement.
- **Onboarding Resilience:** Workflows (e.g., deep research) can fail silently during onboarding, leaving users stuck on a "loading" screen with no escape path. Proposed failsafe: allow users to proceed manually and retry workflows later from the Context section.
- **QA Priorities (P1 Tickets):** Stevie created 3-4 P1 tickets for prompt-related issues degrading user experience. One search throttling bug (page reload, input unfocus) was already fixed by Pedro. Additional fixes needed for Context section copy: "Company Overview" and "Product Features" incorrectly reference "prompt recommendations" (feature does not exist). These fields actually feed the persona generator and will eventually feed prompt recommendations; copy needs clarification.
- **Billing Live:** Billing system deployed to production, connected to Stripe sandbox environment. Safe testing allowed via test cards; no real transactions. Upgrade/downgrade flows tested and functional.
- **Brand Duplication:** Deployed new `adopt_brand` method eliminating future duplicates. A cleanup script will remove existing private duplicates; public duplicates retained pending future merge feature. Possible side effect: may have triggered onboarding bug if workspace already had adopted categories.
- **Citation Share Metric:** Denominator decision finalized: use all tracked brands (public and private) rather than only snapshotted public brands. This prevents misleading 100% share reporting when true universe is larger. However, metrics math requires full review; Jose will audit against Notion metrics document and AI, then create ticket.
- **Overview Charts:** Ready to merge pending Citation Share decision (now resolved to all brands).
- **Aggregate Analytics:** Jose building charts for grouped prompt tables. Strategy: first attempt non-snapshotting approach for speed; if too slow, add new snapshot type. Backfill plumbing already in place.

---

## Key Topics

### Onboarding Bug (P0)

- **Problem:** Users stuck on "confirming categories" step when selecting single subcategory.
- **Root Cause:** Validation guard checks `subcategory_ids` array, but form submits single selection as `primary_subcategory_id` parameter.
- **Solution:** Concatenate both in guard: `unless [params.subcategory_ids, params.primary_subcategory_id].join.any?`
- **Owner:** Estevão Mascarenhas
- **Related Issue:** Onboarding workflows can fail silently, leaving users on loading screen with no workaround. Proposed failsafe allows manual category selection and deferred workflow retry from Context section.

### QA & UX Improvements

- **Search Throttling Bug (Fixed):** Page reloaded and input lost focus after search throttling. Pedro deployed fix.
- **Context Section Copy:** "Company Overview" and "Product Features" descriptions incorrectly claim these fields enable "prompt recommendations" (feature not launched). Actual use: feed persona generator; will eventually feed prompt recommendations. **Decision:** Fix verbiage, don't hide feature. Stevie owns.
- **P1 Tickets:** 3-4 P1 tickets in system. Medium priority: Stevie will address if bandwidth allows.

### Brand Management

- **Brand Duplication:** New `adopt_brand` method deployed; prevents duplicate creation going forward. Existing private duplicates will be cleaned up via script; public ones kept for future merge functionality.
- **Potential Side Effect:** Adopting categories may have triggered onboarding bug if workspace already had categories.

### Metrics & Analytics

- **Citation Share Metric:** Denominator includes all tracked brands (public + private). Prevents misleading high share percentages when true universe is much larger. Example: if only tracking 2 brands, don't show 100% share when there are 50+ brands in reality.
- **Metrics Audit Due:** Jose flagged that metrics math was ported without full understanding; multiple iterations via AI have obscured original intent. **Action:** Full audit against Notion metrics document and AI review; create ticket for follow-up.
- **Overview Charts:** Ready to merge with all-brands denominator decision.
- **Aggregate Analytics (WIP):** Charts for grouped prompt tables. Non-snapshotting approach attempted first for performance; if slow, new snapshot type may be added. Backfill infrastructure ready.

---

## Action Items

**Stevie Kim (GrowthX)**
- Update onboarding/context copy to clarify "Company Overview" and "Product Features" purpose; remove incorrect claims about prompt recommendations

**Estevão Mascarenhas (GrowthX)**
- Fix onboarding category validation guard: concatenate `primary_subcategory_id` with `subcategory_ids` in check
- Add failsafe to allow users to manually select categories if onboarding workflows fail; enable workflow retry from Context section

**Jose Farias (GrowthX)**
- Run script to remove duplicate private brands from database
- Create ticket to audit Citation Share and other metrics math against Notion metrics document and AI; verify correct implementation
- Merge overview charts PR using all brands for Citation Share denominator

---

## Transcript

**Leonardo Carpenedo Steffen:** Thank you. Morning, team.

**Pedro Steimbruch:** Morning.

**Pedro Steimbruch:** How are you doing today?

**Leonardo Carpenedo Steffen:** Something good.

**Pedro Steimbruch:** Thanks.

**Pedro Steimbruch:** Good as well.

**Leonardo Carpenedo Steffen:** Morning.

**Stevie Kim:** Hi.

**Leonardo Carpenedo Steffen:** Hi.

**Estevão Mascarenhas:** Hi.

**Pedro Steimbruch:** I'm going to share my screen.

**Leonardo Carpenedo Steffen:** Perfect.

**Leonardo Carpenedo Steffen:** Did any of you also test things in Safari, or was it only Chrome?

**Leonardo Carpenedo Steffen:** Oh, that's a good call.

**Pedro Steimbruch:** I'm always in Chrome.

**Leonardo Carpenedo Steffen:** Same. I'm doing Safari, and that's okay.

**Stevie Kim:** I guess I could start. So for me, I did quite a bit of QA, mostly on prompts, and then a little bit in other areas. But I did create some tickets, I think two or three tickets for prompts, and then one for another area that I can't recall at this moment. But anyway, they're in the P1 label. And I think because some of them degrade the user experience to the point where I think we should try to get to them. They're not critical, I wouldn't say that, but at the same time, they're sufficiently annoying enough or confusing enough to do something about.

**Pedro Steimbruch:** Yeah, I tackled the one you created about search resulting after it passed a few seconds, right? After it throttled, it would reload the page and unfocus the input. It's fixed now.

**Stevie Kim:** Awesome.

**Pedro Steimbruch:** And I saw that this one and this one you also created, right?

**Stevie Kim:** Yeah. This one, these three. Yeah, so there's a few, and then there's the UX one, yeah, so there's some incorrect verbiage. And then I think like one of them, especially the company overview, it's not clear what that's even used for. So like as a user, I wouldn't know the importance of filling that out. But they, a few of them, like the product features and the personas say that it helps for product or prompt recommendations. And that's not a feature we have. So I think we don't recommend prompts yet. So we should change the verbiage on that. So those ones are pretty, very easy. If I can get to it, I'll get to that.

**Pedro Steimbruch:** Should we hide this until we make some changes?

**Estevão Mascarenhas:** Can you guys hear me? Yeah. So this, Daniel started this. And the idea is to use this for our enterprise customers to generate prompts for them. So this is not being used indeed. The idea is to use them, but we don't have any other feature consuming from this.

**Stevie Kim:** I thought the company overview, isn't that being used by personas when we automatically generate personas?

**Estevão Mascarenhas:** Yeah, the idea is to generate this brand context, the company overview, the product features, and then we feed those to generate the personas. And the idea is to use the personas to generate prompts.

**Stevie Kim:** Okay, we're just not there yet. Yeah, yeah.

**Estevão Mascarenhas:** Yeah, yeah.

**Stevie Kim:** So we just need to clean up the verbiage there. Not a big deal, just something that, you know, we want people to understand, like, what it's used for, why they should fill it out, and then also get rid of any language that is incorrect.

**Pedro Steimbruch:** I'm wondering if we should hide context from the launch.

**Stevie Kim:** Well, they need to be able to fill it out, though, if we can't generate it for them.

**Estevão Mascarenhas:** Yeah, good question. We can still keep filling it during onboarding, but we hide those until it's used for something.

**Stevie Kim:** Well, it is used for personas now, and personas are automatically generated.

**Estevão Mascarenhas:** Yeah, but we are not using personas for anything at the moment.

**Estevão Mascarenhas:** Oh, yeah, no, you can tag prompts with personas.

**Pedro Steimbruch:** So that it is being used, yeah.

**Stevie Kim:** Oh, yeah, that's cool, though, yeah. I don't know how helpful that is, but, yeah, I don't think it's worth, just because the verbiage is off, I don't think it's worth hiding. But, yeah.

**Leonardo Carpenedo Steffen:** Perhaps. Go ahead.

**Estevão Mascarenhas:** Maybe it's not difficult to add a workflow, maybe not like this week, but maybe the following, that we can automatically tag the prompts that it's in. The workspace based on the personas, like we can have like a quick workflow that feeds all the personas that the workspace has and, yeah, and categorize them. Yeah, just thinking about how to make it more useful, but just thinking out loud.

**Stevie Kim:** I think, yeah, I mean, I think that that would be kind of difficult because it takes a lot of domain knowledge to understand. Like your persona would have to be like really accurate for it to tag right. And I don't think that's as useful as, say, us focusing on prompt recommendations. And it is like the EMs have asked for it, like prompt recommendations, for instance, to help their customers. And I'm assuming that customers will want that. And I think we have a ticket somewhere in the backlog for that, too.

**Pedro Steimbruch:** Yeah, I can go. That's okay. I started today working on P0s. I was able to move a few of them to production already, and I will just keep working on them in the afternoon. I hope, hopefully, I will tackle a few more today. So I'm not prioritizing P0s, I'm just grabbing them. So I know something happened in the channel today, which generated a few more P0s. When about onboarding, Estevão? That JSON reported. I'm not sure if you are aware of that. P0, actually, this one, onboarding. He's trying to move on from the categories step, but it keeps saying that. And one thing that I also noticed on onboarding, I can tackle both, if that makes sense, is if I am doing the onboarding and the workflows fail to categorize my brand, for example, then I am stuck in the onboarding. I can, you know, it just says loading if the workflows fail. It doesn't allow me to move on. I think we should have a failsafe in place, too. To allow the user to move on and manually select everything that the workflows are doing. Like, even if I, for some reason, if I put the domain wrong, the workflow will fail and I don't have feedback of what's going on.

**Estevão Mascarenhas:** Yeah, that's a good point. Yeah, I think it should be more resilient. But also the basic research should, like, it could fail due to network issues or something, but the workflow should also, like, be, like, not fail. But I get what you mean. Like, I think we should not block the user. I'm just thinking, like, if there's any impact, we want to be able to do research then, like, but I think that's, maybe that's fine.

**Pedro Steimbruch:** Yeah. I'm not sure what we are doing on this. I'm thinking about workflows, onboarding-wise, like the deep research, basic research, and so on. But I think we should allow the user just to move on, right? Select categories manually, and then they will have the same experience as if the onboards, the workflows were successful, right? Or is there anything that they will lose?

**Estevão Mascarenhas:** No. They'll lose fidelity.

**Jose Farias:** Like, it'll be a worse experience, for sure. In terms of, like, we can't generate user personas, we can't, and all because you inputted your domain wrong, like that. I think there's, like, separate levels here, like, inputting your domain wrong, I think we might want to block, be like, hey, this webpage doesn't even exist, like, are you sure? Anything else? Like, if the workflows fail, though, like, I think that might be fine to continue. They'll have a worse experience, but an acceptable one, I think.

**Stevie Kim:** Yeah, because they can manually kick those off, too, in their workspace. Yeah. Oh, yeah. Yeah, that's right.

**Pedro Steimbruch:** Oh, nice. Yeah, if I manually, let's say the onboarding fail for some reason, I moved on, I manually select subcategories, and then, as you mentioned, Stevie, I can trigger workflows again.

**Stevie Kim:** So in the company, no, in the overview, in the context, I don't know why I never remember the name of that, but anyway, in the context, you can either do it manually, or you can generate, it gives you the option, oh, do you want us to generate this for you, or you can do it manually, so there's that option. Oh, I see. Okay. And, um, and then. This one, will this update subcategories or what?

**Pedro Steimbruch:** I don't think it will work.

**Stevie Kim:** No, no, no. That again. Yeah. So, um, but you, they, they still, if they select their subcategory in the onboarding, will we lose that if the workflow fails?

**Pedro Steimbruch:** Oh, I don't think so. Yeah.

**Stevie Kim:** If those are separate, then I don't see the problem.

**Leonardo Carpenedo Steffen:** So how did you get past this part, uh, on the onboarding? I was there and that's, uh, what I was going to share. I didn't see that there was an issue for that already, but onboarding, uh, it gets stuck. He can't move on from this confirming categories. I was there, uh, I see the bug for what it's worth.

**Jose Farias:** We have a check. It says unless params subcategory IDs any. Please select one category. But what I'm seeing there is that's probably being submitted as the primary category ID, primary subcategory ID, and not in the subcategory IDs params. So the fix is really simple. Just need to concatenate the two arrays. So the guard would become, unless, array, params subcategory IDs join, params primary subcategory ID, that's the guard. So the fix is straightforward. But there's no workaround, right?

**Leonardo Carpenedo Steffen:** If I'm trying to add the brand here and it gets stuck.

**Jose Farias:** It's a legit bug. No workaround. We need to fix it.

**Leonardo Carpenedo Steffen:** Why did I not see this yesterday? Was it that it changed since? So I was able to add the brand yesterday. Why did I...

**Jose Farias:** You've probably had more than one category.

**Estevão Mascarenhas:** Yeah, that's...

**Leonardo Carpenedo Steffen:** But I tried to add more than one category. Let's see. Marketing analytics, BI, digitalization. We'll see. Yeah.

**Stevie Kim:** Well, we can fix that bug and then test it. Whoever fixes the bug, please test it again to make sure it's fixed in this scenario.

**Estevão Mascarenhas:** Pedro, unless you're already on that, like, I can tackle those. My plan for now is to get back to onboarding, so I can tackle those bugs. Okay. Sounds good.

**Pedro Steimbruch:** Can I move this one to that they are merged, they are reviewed already, or what do you guys still? For the billing, at least, let's keep in review.

**Estevão Mascarenhas:** I just want to leave a message there. Let's... Yeah, because that's... Yeah, that task is pretty empty. Like, there's... I want to fill a bit of description of what got done there.

**Pedro Steimbruch:** Okay.

**Jose Farias:** Should I go? Yeah.

**Jose Farias:** So yesterday I deployed, what did I deploy yesterday? Oh, yeah. We're not duplicating brands anymore. Yay. Which might be a, maybe that's what broke the onboarding. I don't know. Because what we're doing currently is we're now, when you create the brand, or when we identify that the brand is pre-existing, there's a method, a new method on the workspace called adopt brand. And what that'll do is set the brand and also adopt its subcategories. It copies over the subcategories from the brand to the workspace. So it might be that when we're reaching that screen, the workspace already has categories and that messed up the card somehow. So that's it could be that too. But yeah, that's deployed. We're not duplicating brands anymore. And I'll run a script probably later today to remove any duplicate brands that are private. The public ones I won't remove yet because we might want to legitimately choose between them. We don't, we haven't programmed that merge functionality yet. Yeah, and then I finished the overview charts stuff. I didn't merge it because something did come up. I think Pedro will have the most context, so I'll just ask right now. In calculating things like the citation share, we were, the denominator, we were using all brands in the scope. Which is different to the brands that we snapshot. So for example, in displaying the... The subcategory charts in the public pages. The brands that we snapshot are only the public ones because private ones don't have public pages. But then with Citation Share, do we consider all brands or just public ones? We were previously considering all brands.

**Pedro Steimbruch:** Yeah, I would say we should consider all brands because we want to give a truly understanding of... Imagine that we don't have any public brands or only our brand, then you have 100% Citation Share. But let's say, in fact, you won't have like 5%, then we are giving you a very misleading number, right?

**Jose Farias:** Yeah, this number is weird because I don't think there's a straightforward way to display it accurately one way or the other. Because even if we use all brands, which I agree makes the most sense... We're still limited to the brands that we're tracking. So really, this is citation share between all brands tracked by CheckThat specifically, not all brands in your subcategory, in the universe of your subcategory. Okay, yeah, makes sense.

**Pedro Steimbruch:** Shouldn't we actually denominate or be the citations, not just citations with brands?

**Jose Farias:** I need to, maybe, maybe. So how we arrived at this, it was me porting the, of course, we've gone through multiple iterations of how we render these charts. So I blocked the math without fully understanding it, to be honest, when I was refactoring into the snapshot system. And then that went through multiple rounds of AI. So I think all that to say, we're due. AI review of all the metrics. There's a document that Marcel shared at some point in Notion describing, like, all the metrics. I think it's about time that we give that as context to, like, an LM and ask it to, like, double check our math. Yep, that's the one.

**Pedro Steimbruch:** I remember, yeah, I remember fixing the citation share maybe two weeks ago to the denominator.

**Jose Farias:** Yeah, but.

**Stevie Kim:** So are we, sorry, are we talking about the public pages or the workspace?

**Jose Farias:** Everything, really. Everything.

**Stevie Kim:** Yeah. Well, I mean, the workspace, though, is, I mean, I think it's, Marcel has repeatedly said it's okay to have different metrics in the public space versus the workspace. Because it's scoped differently.

**Jose Farias:** Yeah, it makes sense. It's just, like, things like the citation share. Yeah, look, I'm not ready to, like, discuss the actual math, which is the real question that I'm posing. So let's check it offline. I'll reread this document that Estevão just linked, and I'll double check all the metrics. I was going to say I'll ask AI, but I'll do both. I'll ask AI and also do some manual QAing there. I'm saying AI, but really it's a ticket. Anyone can do it. Yeah, I'll create a ticket. Okay, so that's about ready to merge. I'll just use all brands for now, which is what we've been using, and I'll merge that. And then I'm working on the aggregate analytics, the charts for when you're grouping the prompts table, when you're grouping by any number of dimensions. We used to display those trend lines. Some trickiness there. I'm going to... I'm going to try to do it without any snapshotting. And if it's fast enough, we'll just ship that. And if it's not, then we might have to add a new type of snapshot and backfill. The plumbing is all there, so I'm not super worried about it, but it'll add some amount of seconds to the onboarding, for example. It's all good. I'm not worried. And that's it for me.

**Stevie Kim:** Yeah, can go next.

**Estevão Mascarenhas:** Sorry, Stevie? Oh, I just said thanks.

**Stevie Kim:** Oh, okay.

**Estevão Mascarenhas:** Yeah, so on my side, yesterday I was focused on wrapping up the billing and deploying it to production, so it's already there. I shared the message on the channel with a quick video that I recorded for Leo, but if you guys want to test as well, you can either test in production, just follow some guidelines. Like not... Maybe not testing in the workspaces that our team is working, or you can test locally, like it's the same experience. So in production, it's still connected to Stripe's sandbox environment. So that way we can test the test card, use test cards. It's not going to do any real transactions. We can simulate the subscriptions, like go forward and back in time. That's cool to test downgrade and upgrade flows. So it's there. So my plan for today is to get back to onboarding, fix those bugs. I have some on my plate here. I think it was working at least until yesterday, but I will go through it again and keep working on the fixes. And yeah, if everything is okay, like if we don't get any other onboarding issues, then I can pick something else. But that's pretty much my plan.

**Stevie Kim:** Thanks. Yeah, so I'm just going to continue QA work, prompts, QA prompts took a lot longer than I thought.

**Leonardo Carpenedo Steffen:** I can join you with that. Oh, it's done now. I have a new prompt that I created that I don't know if it's how far it went. Wait, what? I created a new prompt yesterday when one of the brands, don't know what happened with it. Let's take a look. Oh, I think, yeah.

**Stevie Kim:** We can take that offline. But, yeah, if you want, I can kind of take you through the prompts. But it's also good for a first-time user to go through it. And if anything's confusing, it'd be good to have a ticket. But just check the tickets that are already, that I created yesterday. And they're in the P1 label. Um, so yeah, I'm going to continue, um, queuing, following just the rest of that doc and that Daniel put together. And if I can get to some of those tickets, like the description tickets and stuff, I'll get to that. Um, any of the low-hanging fruit. Um, yeah. And I think, yeah, we've got a new AE that we hired for CheckThat. Um, and so he's going to be onboarding and I think Carrie is going to work with him on getting him onboarded. And so, yeah, it'll be good to get his take on the, you know, end-to-end experience as well. Cause he's familiar with the business domain. Yeah, that's it for me.

**Jose Farias:** Perfect. I think that's all of us. Is that it?

**Jose Farias:** Yep.

**Pedro Steimbruch:** Yeah.

**Jose Farias:** Have a great day, everybody. See you all tomorrow.

**Jose Farias:** Goodbye.
