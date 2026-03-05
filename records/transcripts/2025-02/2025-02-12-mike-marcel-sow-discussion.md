# Mike <> Marcel - SOW Discussion

<metadata>
date: 2025-02-12
time: 21:32 UTC
duration: 26 minutes
organizer: Marcel Santilli (fwd.digital)
participants: Mike Anderson (Hims), Marcel Santilli (fwd.digital)
fathom_recording_id: 46980055
fathom_url: https://fathom.video/calls/231654461
share_url: https://fathom.video/share/x4A_776LcyKxAXZQQ6_Ri5qNW7ZbZKhY
source: fathom
enriched_on: 2026-03-05 02:20 UTC
</metadata>

---

## Summary

Marcel Santilli (fwd.digital) and Mike Anderson (Hims) refined the scope of work for a content creation partnership focused on developing scalable medical content. The team agreed to restructure the proposal to increase volume ranges (moving from monthly to yearly commitments), add flexibility for content refreshes, and emphasize the calibration-scale-refresh phases to better align with Hims' internal medical review capacity. Marcel committed to doubling content volume without increasing scope as a goodwill measure, while both parties acknowledged the challenge of finding medical professionals willing to endorse content without thorough review. The next step is for Marcel to send the updated SOW by end of week and for Mike to connect with internal stakeholders for a final decision by end of the following week.

---

## Context

fwd.digital is a content creation and AI automation agency working with Hims, a major direct-to-consumer telehealth platform. The partnership involves developing large-scale medical content (targeting 300-500+ articles monthly) using complex AI workflows for research, generation, and quality assurance. Hims is evaluating how to scale content production while managing internal medical review capacity—a critical compliance requirement for healthcare content. The challenge centers on balancing fwd.digital's ability to automate content creation (at 10-20 cents per word) with Hims' need for trusted medical professionals to review and endorse the content. This meeting focused on restructuring the SOW to give Hims more flexibility to phase in content volume as internal processes mature.

---

## Relevance

**To fwd.digital Delivery:**
- Complex AI workflows for research and content generation demonstrate scaling medical content at 10-20 cents per word with automated QA and fact-checking—a replicable framework for phased client onboarding
- Structured calibration-scale-refresh phases provide clear capacity planning models for clients managing editorial bottlenecks
- Editorial review remains the primary cost driver even with automation; setting clear standards for source validation and medical processes is critical for quality at scale

**To fwd.digital Business Development:**
- Hims is committing to $200k+ annual content spend with significant expansion potential if quality and delivery scale well
- Mike's flexibility negotiation signals strong intent but also internal resource constraints; medical review capacity is a potential churn risk if it becomes a bottleneck
- Opportunity to prove value in first 3-6 months and unlock much higher volume commitments once workflows are battle-tested in production

---

## Overview

- fwd.digital will adjust the proposal to increase volume range and flexibility, allowing for scalability and content refreshes
- The focus will be on balancing automation with necessary human review, aiming for 10-20 cents per word cost
- Hims needs to solve for internal medical review capacity to match potential content output
- Both parties are committed to finding a mutually beneficial structure that allows for quality at scale

---

## Key Topics

### Proposal Adjustments and Scalability

- Marcel will update the SOW to increase volume range, move from monthly to yearly commitments, and add language for content refreshes
- Restructuring around three phases: calibration, scale, and refresh—giving Hims the flexibility to ramp up as internal workflows mature
- fwd.digital is doubling the volume without changing scope as an incentive to move forward
- Mike emphasized the need for flexibility to dial up volume once workflows are proven and internal medical review capacity improves

### Content Creation Process and Quality Assurance

- fwd.digital uses complex, multi-step AI workflows: research agent breaks down topics, generates research questions, parallel-processes sources, chunks data, and performs fact-checking
- Editorial review remains the primary cost driver—even with AI, humans must validate research, check facts, review outlines, and provide thoughtful critical review
- The approach achieves 80% efficiency gains vs. traditional human-only content creation
- Automated QA and fact-checking are being built into the first work stream, but cannot fully replace human review

### Cost Structure and Efficiency

- Target cost range: 10-20 cents per word
- Some research workflows cost several dollars in compute alone; fwd.digital aims for the lowest-cost model without sacrificing quality
- The value proposition: cheapest possible cost with quality output approaching the most white-glove model possible
- Future cost reductions possible through fine-tuning models and workflow optimizations as more editors provide feedback data

### Medical Review and Compliance

- Hims' primary internal constraint: finding capacity for medical professionals to review and endorse content (a regulatory/reputational requirement)
- The challenge is not AI accuracy but the fact that medical professionals with credible reputations require thorough review before signing off
- Marcel shared precedent: in healthcare/landlord space, fwd.digital published thousands of pages with only 3 complaints after millions of page views—all nuanced edge cases (law updates, local variations) not factual errors
- Agreement to set clear standards for source validation and medical processes; AI can automate fact-checking against trusted sources, but what constitutes "trusted" requires human input

### AI Models and Technology

- fwd.digital primarily uses GPT-4 and GPT-3.5 models; also uses O1 for tasks requiring larger output tokens
- Using OpenAI API keys; not currently exploring Gemini or planning a transition
- Architecture is deliberately flexible: workflows can adapt quickly to new models when they appear, faster than low-code tools can
- Focus is on building the runtime layer—the complex orchestration and automation—which is harder to replicate than swapping models

---

## Action Items

**Marcel Santilli (fwd.digital)**
- Update SOW proposal: increase volume range (move from monthly to yearly), add language for content refreshes, increase flexibility for scaling, and double the content volume without changing scope. Send updated version by end of week.

**Mike Anderson (Hims)**
- Connect with internal stakeholders (VP of Site, editorial team, medical review team) next week to review updated proposal and gauge internal alignment. Target final decision by end of the following week.

---

## Transcript

**Marcel Santilli:** Marcel, how you doing?
**Marcel Santilli:** Really good, Ian.
**Marcel Santilli:** Happy Wednesday.
**Marcel Santilli:** don't even know what day of the week it is.
**Marcel Santilli:** Where?
**Marcel Santilli:** Trying to hold on, right?
**Marcel Santilli:** Yeah, yeah, pretty much.
**Marcel Santilli:** So in like due diligence for a series A, so it's like, you know, just like context switching to the max these days.
**Marcel Santilli:** Hopefully we're like a week or two away from being done with that.
**Marcel Santilli:** Yeah.
**Mike Anderson:** Way to the end of the tunnel, hopefully.
**Mike Anderson:** Yeah, yeah, exactly.
**Marcel Santilli:** How's your week so far?
**Mike Anderson:** It's good.
**Mike Anderson:** Been a busy one, but all good.
**Marcel Santilli:** Awesome, and that's good.
**Marcel Santilli:** Yeah, so I'm starting to mix up essentially like we use Panda Doc and Panda Doc doesn't allow you to just like download a previous version.
**Marcel Santilli:** And so I had to like duplicate the Panda Doc and then restore to the previous version.
**Marcel Santilli:** And then create a new version essentially, you know, so it's like, at least now we have two versions that.
**Mike Anderson:** Yeah, all good.
**Mike Anderson:** I appreciate the help with that.
**Marcel Santilli:** Sorry for the headache.
**Marcel Santilli:** Oh, good.
**Marcel Santilli:** How are you thinking like, yeah, let's we can dig in or whatever you want to it would be helpful.
**Mike Anderson:** Yeah, let's dig in.
**Mike Anderson:** Well, first off, just wanted to thank you for the adjustments to the scope.
**Mike Anderson:** I think the update, the updated proposals is much closer to our target.
**Mike Anderson:** There I wanted to go through in terms of how the structural lines with kind of our strategy and knowing that we're we're looking at problematic.
**Mike Anderson:** And then also just, you know, I think we've had to do a little bit of a a little bit of a rethink on like the cost implications for our side, assuming that we'll be dialing back on things like the medical review on your side.
**Mike Anderson:** So just wanted to go through that in a little bit more detail if we could.
**Marcel Santilli:** Yeah, let's do it.
**Mike Anderson:** All right.
**Mike Anderson:** I guess one of the biggest questions that we have right now totally understand the adjustments in in spend as far as the like the page count.
**Mike Anderson:** So for what is that section two on the programmatic piece?
**Mike Anderson:** Just trying to understand like the the levers that are going into like they're being a fixed cap.
**Mike Anderson:** I think from our perspective what our hope and going into like the programmatic realm has been you know as much as possible you know we hope that a model can scale up you know I think like the way that that you and the team have outlined the proposal here makes total sense like going through initial discovery calibration phase.
**Mike Anderson:** from there or like hoping that we would expect there to be some cost efficiencies once we can at nail that.
**Mike Anderson:** So just curious like is that something that we can tie more to like search opportunity as opposed to a page count?
**Marcel Santilli:** Yeah like I think so just understand like a little bit that the ball net here is not the compute costs or like our ability to deliver the volume it's really like ultimately like knowing how important editorial is like you do need to have someone that looks at like the the research that's coming back in and validate some of that looks at like some of the facts looks at the outline or looks at the you know like a lot of those things along the way with a much more like kind of look and and thoughtful look as opposed to just like reading really quickly it's like okay let's say like we're good right and then like there's the editorial pass at the very end like so
**Marcel Santilli:** So that's really like the cost driver, where, you know, it's still like 80% more efficient than if you had zero, like AI work, close powering all of this, right?
**Marcel Santilli:** but like for us, like we're, I tell people all the time in programmatic, like we can go a lot higher.
**Marcel Santilli:** Like it's just like a matter of like the, you know, if you like how wide of a process wants to be feel good, do you want it to be?
**Marcel Santilli:** And it's ultimately coming down to think more of like a business decision on like the trade off there, right?
**Marcel Santilli:** Like where, and that's what I saying, like what we could do is like for some programmatic, like we can scale to like pretty aggressively, right?
**Marcel Santilli:** It's just really hard for us like upfront to say like, yes, like we can commit to like a much bigger number right away without knowing like what are going to be the nuances that come up.
**Marcel Santilli:** Right.
**Marcel Santilli:** Like so, for example, when we did.
**Marcel Santilli:** the DUI stuff, it was like, ended up being a lot more human work on verifying every single source than we originally had thought it was gonna be, right?
**Marcel Santilli:** And the bottleneck was that.
**Marcel Santilli:** then, but also the bottleneck was like, even if we had 10x the volume, like there was a still internal bottlenecks because they wanted their legal team to review, you know?
**Marcel Santilli:** And so I think like anything that can be automated and streamlined, we will do.
**Marcel Santilli:** It's just like a matter of like, so if we wanna tweak the language so that you feel better about like, hey, like we can also let you self-serve into a lot of the volume if needed, you know?
**Marcel Santilli:** It's just more of like, if you tell us like, hey, there's four steps here to review.
**Marcel Santilli:** And on average, it's gonna take like two, three hours of inventory review, plus checking everything's changing and whatnot, like we can't to 10,000, you know, if you will.
**Mike Anderson:** Exactly.
**Mike Anderson:** And I think that that's kind of, that would give us a lot of peace of mind if we have the ability to.
**Mike Anderson:** restructure.
**Mike Anderson:** Like, for instance, I think, you know, after discussing it with our editorial team, I think something like, because I think like our assumption is, you know, the majority of our investment is going to be on the up front.
**Mike Anderson:** And once we're up and running, like we should do, we won't be able to throttle up.
**Mike Anderson:** So, you know, if we're able to structure it like, kind of the way that you have the, like, each of the main kind of phases, like calibration, scale, and refresh, something like that feels a little bit more in line with how we would need to resource it internally.
**Mike Anderson:** ultimately, I think, like, how tactically we'll need to go about building out each of the workflows.
**Mike Anderson:** So, that I think then would give us a better read on, like, I think there's going to need to be higher level.
**Mike Anderson:** involvement from our medical review team on the upfront calibration, but then also like as a line item under, you know, as we're scaling content, then we'll need to figure out, you know, how much ability we have to, how much content we can review over the course of, you know, a given month, and that I think after a conversation last week is just something that we're going to need to solve from a research standpoint on our end, above and beyond what we currently have placed, most likely.
**Marcel Santilli:** Yeah, and like, I think the way I've always, like the way we're approaching things that you understand as well is like, we're aiming to always be between like 10 to 20 cents a word, roughly it, or like, you know, in the tens of dollars worth of costs, and just to understand, like, just like some of our research workflows alone are a few dollars, just a compute alone, like, and so, like, we're, we're keeping like our cost, like, fairly like competitive,
**Marcel Santilli:** Because the whole version that we're trying to have here is like, hey, this should be close to the least expensive model possible.
**Marcel Santilli:** But with an output that is closer or higher than the most white level model possible, or very close to that, right?
**Marcel Santilli:** the thing is, there is a level of bare minimum that going beyond that, because we're not like, like, we're not scaping like five sources, right?
**Marcel Santilli:** Like our research agent, for example, you kind of see a little bit, I might have showed you this before, but like, you know, to research a single topic, right?
**Marcel Santilli:** Like it's like, hey, we're vellin' in an input, we're breaking down the research, we're generating research questions, then we're parallel processing that, we're searching for all the sources.
**Marcel Santilli:** And then it's going through this whole process, chunking it, doing all these things.
**Marcel Santilli:** so it's like, where, as I think a lot of the cheaper ways to do it,
**Marcel Santilli:** that would allow you to do like 10,000 or for like a lot cheaper, like they're not going as in debt.
**Marcel Santilli:** But like the main thing is like the reputation of risk for you all, right?
**Marcel Santilli:** as a public company, but also trade off off of the alternative, which is like, you know, hey, like one single click on an ad is probably like the equivalent of a single page ready.
**Marcel Santilli:** Like so if that page gets more than one click over period of time when average, then it's like, should have a really good comment about why for your team overall, hopefully, you know, yeah.
**Mike Anderson:** I guess one quick question on that before we shift gears, in terms of the models that you guys are using, is that something that you're also looking to adapt over time?
**Mike Anderson:** Also just wondering, like if you guys anticipate there being cost productions on your end, and just like how you kind of plan to model that as part of some of these longer and longer term engagements.
**Marcel Santilli:** Yeah, like so for us, like we haven't started.
**Marcel Santilli:** to fine-tune models was definitely like on our roadmap now line, and what it mean by fine-tune, it's not fine-tuning on any proprietary data that, you know, because we're only using like data out there, but it's like, let's say an editor is going through and reviewing an outline, right?
**Marcel Santilli:** Like if we have 50 editors doing that across 50 accounts, eventually there's enough data there to fine-tune a model that is cheaper and better, specific task only, right?
**Marcel Santilli:** And then that could be like help scale things better, but today like we're not, like where we're gaining additional like quality and it's ultimately like our ability to take these workflows and make them even more complex without adding complexity to how we maintain and run them, right?
**Marcel Santilli:** And that's why like the the runtime layer is the part that's like really hard to replicate, I would say, you know, where, you know, like if you're like some of these processes that we're running, you know, like if you do some of these, right?
**Marcel Santilli:** um,
**Marcel Santilli:** And it's going through like all of these different steps, know, and then you look at the workflow underneath it, just the hundreds of like thousands of processes like running, like this is the that local tools would be able to do, you know?
**Marcel Santilli:** And this is just like in the last hour, worth of like, you know, processes running, know?
**Mike Anderson:** Yeah, but you guys aren't like running on like 4.0 and then like exploring a transition to Gemini or something like that.
**Marcel Santilli:** No, like not right now.
**Marcel Santilli:** mean, we do use O1 quite a bit because O1 has a much bigger max output.
**Marcel Santilli:** And so that allows us to do a lot.
**Marcel Santilli:** Like we're using our own like API keys, you know, so, but I don't think we don't like for anything right now, but obviously like we're always assessing if there's like better things that come out, we use mostly like on-profit and open AI.
**Marcel Santilli:** And like we're building a lot of too.
**Marcel Santilli:** So that like when new models come out or there's like,
**Marcel Santilli:** like a kind of change in paradigm and these models like are workflows can adapt way faster than like the low code tools, you know.
**Mike Anderson:** Yeah, makes sense.
**Mike Anderson:** Okay.
**Marcel Santilli:** But just to understand, just to close the point on the previous thing we mentioned, like essentially like what we could do that could work here is just like have the cap based on number of pages with heavy editorial review, but then do a much bigger cap on like using our workflows, you know, and self-serving and scaling or like how would you want to position this to be a little bit more comfortable for you all?
**Mike Anderson:** Yeah, I mean, I think like spelling that out a little bit of like, you know, if we can position it as like we will commit to, you know, x number of calibration periods to establish, you know, why number of workflows over the course of the engagement, then like.
**Mike Anderson:** Something like that then gives us an idea of like how many cycles we'll need to roll through Till till like reach level of confidence that okay, you know, we're now at we've reached a Keep up front kind of editorial in mid review Lift aren't internally we'll we'll be negated And then from there like we'll have an automated workflow running that will require minimal You know reviews from from our end so yeah, if we can kind of frame it in those terms of like, you know Yeah, like calibration On like minimal review on your end except for Having the after the calibration period except for having medical Professional Stick their name next to it The thing that like it's gonna be really hard to find any medical professional
**Marcel Santilli:** with any remote reputation that would allow you to use their name without them actually reading it and checking things, right?
**Mike Anderson:** But that may be fine too.
**Mike Anderson:** mean, you know, if we're committed to let's just say 500 articles a month, like that will undoubtedly be in excess of what we're able to support out of the gate.
**Mike Anderson:** But I think we can scale to get there.
**Mike Anderson:** Again, it's going to be something that we're solving for.
**Mike Anderson:** But like, as long as we have that flexibility and the engagement to, you know, that we have the ability to dial that up as necessary and also to refresh, then I think we'll, you know, we'll need to place a comfort there.
**Marcel Santilli:** Okay, I think like putting numbers of workflows as contra or like it wouldn't be productive for you either because like we have so many constantly evolving and what we're trying to solve for is like sometimes we're the fact check or sometimes there's additional workflows and like that's part of what we need to deliver.
**Marcel Santilli:** in order to meet the quality bar at scale.
**Marcel Santilli:** But I think what I can do is I can tweak the language so that we put more of a range in the volume.
**Marcel Santilli:** And we say, hey, or any workflow we're using will make it available to the team, to leverage.
**Marcel Santilli:** And we'll just put some kind of caps, like you're not running a million things in one day and crashing everything.
**Marcel Santilli:** But that's part of what we're building already anyways, so that we can expose more of that.
**Marcel Santilli:** And but then I think part of our hope, too, is as hopefully we can prove the volume, prove the quality, prove the results.
**Marcel Santilli:** And then it's working so well that you also want to scale things.
**Marcel Santilli:** So I think it'll be awesome to do that as well, right?
**Marcel Santilli:** Because like I said, even if no matter who you go with, if you go to anywhere in the public,
**Marcel Santilli:** plan it and you say, hey, I need you to develop 500 pages for me, like, and I need you to do it for less than 10 cents a word.
**Marcel Santilli:** Like, and I need you to check all the sources and I want you to come up with only trusted sources.
**Marcel Santilli:** Like, I would be really like skeptical that anyone can do it, you know?
**Mike Anderson:** No, and to be to be totally transparent too.
**Mike Anderson:** I mean, I think what what we're just grappling with is like, if this model is truly going to like unlock a level of scale for us to justify the investment.
**Mike Anderson:** so, you know, I think like as much as we can establish that flexibility in the agreement to give us confidence that like, we do truly kind of have this lever that we just don't fundamentally have the ability to tap into with internal kind of linear resource scaling.
**Mike Anderson:** And I think that's ultimately what we're going to need to make the case.
**Marcel Santilli:** Okay, that sounds good.
**Marcel Santilli:** so, so, so just to recap, I'll increase the volume range.
**Marcel Santilli:** I'll put some language there that includes like refreshing content as well, you know, and like just so you know, like every single one of our clients, like when they ask us to refresh content in a targeted way, like we have workflows that do that and those are like, we're like for RAM, like we've refreshed like hundreds of pages in a week, you know, and it's fairly targeted.
**Marcel Santilli:** If it's a full rewrite, then it's a little different, but like when they're like, can you enrich this part or can you add this type of CTA at the bottom of every page or like those things like we can, I'll make the language a little bit better and then that way kind of have both and then like and then we can kind of go from there if you think like we need to kind of tweak a little bit further, you know, but I feel really confident.
**Marcel Santilli:** I can also change it instead of per month.
**Marcel Santilli:** Like I can do like a bigger range for the whole year and then like we have more flexibility to go like, hey, let's go super hard up front and just like, you know, like
**Marcel Santilli:** My commitment is like, we want us to succeed, obviously, as much as you do, and we will not hold back on anything, you know, on our end, you know.
**Mike Anderson:** That'd be helpful.
**Mike Anderson:** And I agree.
**Mike Anderson:** mean, I think that, you know, from our side, I think flexibility is going to be most important.
**Mike Anderson:** So, you know, as long as we have a pretty, you know, pretty extended range, then I think that we want to make sure that we have, like, enough structure that like you guys can kind of project, you know, our needs over the course of the year, but still making sure that we have the ability to really scale up once we can nail the workflows.
**Marcel Santilli:** Okay, perfect.
**Marcel Santilli:** That sounds good.
**Marcel Santilli:** Sweet the language right now.
**Mike Anderson:** And then I also want to ask too, so the the first version compared to the second version.
**Mike Anderson:** I think like what we could also use some some additional clarity on is just.
**Mike Anderson:** like what specifically we would be trading off by excluding the third keep forgetting what these sections are called.
**Marcel Santilli:** Yeah, so I added language, the first work stream around the automated QA effect checking.
**Marcel Santilli:** I'm not sure it's there.
**Marcel Santilli:** I think that the main thing that was driving the other one was building up and recruiting a ton of medical experts to go skill the hell out of it.
**Marcel Santilli:** know, and I think like when you're trying to do it at like thousands and thousands of pages a month, potentially like then there's no other way to do it than to build an even more robust system.
**Marcel Santilli:** But you know, like if we're doing like, you know, three, four hundred a month, then I think like, there's other ways to tackle it as well, right?
**Marcel Santilli:** So I think like that's the main trade off there where, you know, we do,
**Marcel Santilli:** We can even after we kick things off, like, if we get to a point where you feel like that's a part of a bottleneck, we can run a small bit of the pilot to test it out on our end as well to take that off of your play, but I think it's like, keep things a little bit simpler too, you know, so that we get this through, like, try to get things published as quickly as possible with quality.
**Marcel Santilli:** And then from there, we can go and say, Hey, Marcel, like, these are the bottlenecks that are putting too much burden on my team.
**Marcel Santilli:** How can we solve them, know, and, like, obviously, like, we're highly incentivized to solve them because if we publish more with the higher quality, that means more traffic growth, which means you're even more incentivized to continue to work with us.
**Mike Anderson:** And then in terms of, like, the accuracy and compliance, you know, for relying more on automation.
**Mike Anderson:** What's your level of confidence there that we're setting aside kind of the medical review stamp.
**Mike Anderson:** You know, in terms of the, in terms of the AI capability of achieving.
**Mike Anderson:** you know, a similar level of accuracy, know, how do you kind of see that?
**Marcel Santilli:** So, at the end of the day, like, you need source of truth to check against anything, right?
**Marcel Santilli:** And the challenge with anything that's scientific or medical is that there's, it's not black and white, right?
**Marcel Santilli:** So, so even like, if you say, Hey, I want a medical paper, I need two medical papers to say the same thing.
**Marcel Santilli:** Okay, like, right, like, it's just a matter of like setting what your actual bar is regardless of a AI.
**Marcel Santilli:** then it's figuring out like, okay, how much can we streamline the process?
**Marcel Santilli:** And then over time, you build confidence, right?
**Marcel Santilli:** whereas just like, hey, this is getting 98 percent, right?
**Marcel Santilli:** Then we feel maybe confident enough that like, the two percent are very like, long tail, right?
**Marcel Santilli:** So just to give an idea, steadily, they've, they've published like thousands and thousands of pages within landlord kind of space and, and so far, after getting millions
**Marcel Santilli:** millions of page views.
**Marcel Santilli:** They've only had like three complaints for like on information that was wrong or misleading and all three were very nuanced things like where it was like a local law, nuance where the law was updated and the article didn't get updated fast enough and it was like slight nuances on something but none of them were like crazy way off right like so we've done it before and we don't have to do it you know like so it is just like the biggest thing is like with medical like with law as like hey there's one source of the law it's usually for each city and you just got to go find those and reference against it whereas like with medical research or side effects and things like that like there's like studies coming out all the time but even those studies have different levels of quality right like that that like and even if you had 20 medical experts all 20 might have slightly different opinions so that's more the challenge it's like what is the bar that we want to send that we feel good about or at least we have time.
**Marcel Santilli:** onto disclaimers, where a ton of explanations about the sources we use, you know, but it's not black and white where it's just like, hey, there's only these side effects, or hey, there's only these things, you know, like, it's just like kind of an infinite thing that's impossible to like boil down to a black and white, you know, on every topic.
**Marcel Santilli:** But like, we can automate so much of it in the sense of like, if we have the trust, once we have the trust of sources, we can fact check against those trust of sources.
**Marcel Santilli:** And we can put things in place to understand what those sources are and understand which ones we're going to use.
**Marcel Santilli:** And that's where we need help on like, how would Germanic experts do it?
**Marcel Santilli:** know, do they look for ones that are mostly cited more?
**Marcel Santilli:** Are they only looking for certain types of publications?
**Marcel Santilli:** What do they look for in order to validate that they follow really strong like medical processes or scientific processes or statistical processes?
**Marcel Santilli:** these are removed by us from the whole thing, know, like, and we can follow whatever they follow and try to replicate as much as possible, you know?
**Mike Anderson:** Well, I think that all sounds good, then.
**Marcel Santilli:** Awesome.
**Mike Anderson:** Okay, so I'll change the language right now on the word stream to what are you thinking as far as like, once we sort that out, like, as far as like timeline for you all, just trying to figure out like kickoffs and, you know, make sure like, yeah, depending on if you're able to shoot over the agreement by end of this week, then I think we have a VP of site this week, so I'd like to connect with a couple of folks internally next week, just to make sure just kind of gauge how everyone's feeling.
**Mike Anderson:** And then from there, hopefully get a, hopefully get a final decision by tail under next week.
**Marcel Santilli:** Okay, perfect.
**Marcel Santilli:** That sounds good.
**Marcel Santilli:** I'll change it.
**Marcel Santilli:** I'll be very generous on the volume.
**Marcel Santilli:** I'm here, like, essentially, what I'm going to do is, like, double the volume, um, without changing this scope, which was, like, you know, just know that, like, um, my biggest thing is, like, as we prove ourselves in this, like, you love the opportunity to grow with you all as we prove ourselves, you know, over the years.
**Marcel Santilli:** Um, and so, like, we're, we're taking a lot off just to be able to work with you guys, you know, so hopefully that, um, you know, you can, you can position that internally, maybe, as well.
**Mike Anderson:** We appreciate that.
**Marcel Santilli:** Awesome.
**Marcel Santilli:** Thanks, Mike.
**Marcel Santilli:** I'll send something over here shortly.
**Marcel Santilli:** All right.
**Marcel Santilli:** Thanks a lot, Marcel.
**Marcel Santilli:** Appreciate it.
**Marcel Santilli:** Bye.
