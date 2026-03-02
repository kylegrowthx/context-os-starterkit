# Strapi <> GrowthX - Listening Tour

<metadata>
date: 2025-10-21
time: 18:34 UTC
duration: 28 minutes
organizer: Marcel Santilli (GrowthX)
participants: Marcel Santilli (GrowthX), Victor Coisne (Strapi)
fathom_recording_id: 95746520
fathom_url: https://fathom.video/calls/446968389
share_url: https://fathom.video/share/e46uXATXrqNmHPxGvUsDxFgjZRkhU8ED
source: fathom
enriched_on: 2026-03-02 19:45 UTC
</metadata>

---

## Summary

Marcel conducted a listening tour health check with Victor Coisne at Strapi, uncovering critical pain points: the new Atlas platform lacks the self-serve capabilities that AirOps provided, creating bottlenecks and slowing delivery on custom engineering work — compounded by a pricing mismatch ($230/mo legacy vs. $18k/mo current average) that deprioritizes Strapi's requests relative to larger customers. In response, GrowthX will open-source its workflow engine as "ContentOS," enabling Strapi to self-serve within one month, while positioning ContentOS as a strategic asset that aligns with Strapi's open-source DNA and could deepen partnership through beta testing, launch support, and potential strategic investment.

---

## Context

Strapi is an open-source headless CMS founded by Victor Coisne, focused on enabling developers to build and run custom content platforms. The company has raised Series B funding ($31 million, ~1.5 years ago) and competes in a crowded market that includes WebFlow and other headless CMS platforms. GrowthX has been a content marketing partner to Strapi for over a year, helping with developer-focused content strategy around emerging tools like Next.js and generative AI. This call was part of Marcel's listening tour at key accounts to assess account health, understand customer pain points, and identify opportunities to strengthen partnerships. Victor was traveling to the Next.js Conference and had limited availability, making this a quick-turnaround sync to address urgent feedback on workflow capabilities and pricing alignment.

---

## Relevance

**To GrowthX Delivery:**
- **Platform Architecture Shift:** Transitioning from Atlas as a closed, GrowthX-internal platform to ContentOS as an open-source, customer-owned framework fundamentally changes how GrowthX delivers self-serve capabilities — requires GitHub-based workflow architecture, decoupled runtime layer, and customer environment isolation (major technical lift, ~1 month timeline).
- **Pricing Model Misalignment:** Legacy contract at $230/mo (vs. current $18k/mo average) creates unsustainable service delivery expectations — need clear policy for de-prioritizing custom engineering requests at lower price tiers to avoid resource drain.
- **Team Transition Impact:** Recent account management changes (Vivek and Mara now leading) show improvement, but knowledge loss during transitions (e.g., image generation project delays) signals need for better onboarding and context transfer processes.

**To CheckThat:**
- **AI Visibility Validation:** GrowthX AI visibility platform (AEO) research is directly validating with Strapi: Victor confirmed Strapi appears in AI overviews for "headless CMS" + "Next.js" searches, validating strategy of targeting emerging tool + developer audience intersections.
- **Competitive Intelligence:** Comparison with Graphite's $800k/year Webflow engagement and Hypergrove's Webpro positioning reveals sophisticated competitive landscape for developer-focused content — informs CheckThat's AI visibility benchmarking for this vertical.

**To GrowthX Business Development:**
- **Renewal Risk & Account Health:** Despite strong relationship scores (9/10), performance concerns (7-8/10, slower growth after 1 year) and bottleneck frustrations signal potential renewal risk — ContentOS beta access and launch partnership are direct interventions to re-engage and strengthen stickiness.
- **Strategic Investment Opportunity:** Strapi open to exploring strategic investment partnership (similar to HubSpot's recent investment in GrowthX) — position ContentOS launch as joint go-to-market opportunity and potential deepening of partnership equity.
- **Reference & Launch Support:** Victor and Strapi are positioned as marquee launch partner for ContentOS — strong open-source alignment, technical credibility, and Victor's willingness to support launch publicly and support GrowthX intros (e.g., OSS Capital, Heather at OSS Capital for legal/licensing).

---

## Overview

- **Performance Gap:** Strapi's growth is below expectations, with the Atlas platform's lack of self-serve capabilities creating workflow bottlenecks.
- **Pricing Mismatch:** Strapi's legacy pricing ($230/mo) is misaligned with the current average contract ($18k/mo), causing its custom engineering requests to be de-prioritized.
- **Solution → Open Source:** GrowthX will open-source its workflow engine as "ContentOS" to enable Strapi's self-serve needs and align with its open-source DNA.
- **Partnership Opportunity:** Strapi will beta-test ContentOS and support its launch, with a potential strategic investment and legal collaboration on the open-source license.

---

## Key Topics

### Account Health Review

Marcel's 4-vector health check revealed mixed results:

  - **Quality:** 7–8/10
      - **Rationale:** Recent account management changes created a learning curve, but the current team (Vivek, Mara) is strong.
  - **Output Volume:** 9/10
      - **Rationale:** Consistent and high.
  - **Performance:** 7–8/10
      - **Rationale:** Growth is slower than expected after one year, though macro factors (e.g., Google's shift to SGE) may be a cause.
  - **Relationship:** 9/10
      - **Rationale:** The current team is a significant improvement.

### Core Problem: Atlas Bottlenecks & Pricing Mismatch

  - **Workflow Bottlenecks:** The Atlas platform lacks the self-serve capabilities of its predecessor, AirOps, creating dependencies on GrowthX's engineering team that slow down projects.
      - **Example:** An image generation project took \~6 months for a "fine" but not "mind-blowing" result.
  - **Pricing Mismatch:** Strapi's legacy pricing ($230/mo) is a fraction of the current average contract ($18k/mo).
      - **Impact:** This forces GrowthX to de-prioritize Strapi's custom engineering requests, as they are not scalable across the customer base.

### Solution: Open-Sourcing the Workflow Engine

  - **The Plan:** GrowthX will open-source its core workflow engine as "ContentOS" to enable Strapi's self-serve needs.
  - **Technical Details:**
      - **Architecture:** Workflows as code, hosted in GitHub repos owned by the customer.
      - **Runtime:** Customers can run workflows on their own infrastructure or use GrowthX's cloud-hosted runtime.
      - **Cost Efficiency:** Avoids the high costs of platforms like AirOps (e.g., a single article could cost $1k in credits) by allowing customers to use their own API keys.
  - **Timeline:** Self-serve access for Strapi is expected within one month.

### Partnership & Collaboration

  - **Beta Testing:** Strapi will be an early beta tester for ContentOS.
  - **Launch Support:** Strapi will help amplify the public launch of ContentOS.
  - **Legal Collaboration:** GrowthX needs open-source licensing expertise.
      - **Action:** Victor will connect GrowthX with JJ from OSS Capital.
  - **Strategic Investment:** Marcel mentioned a recent strategic investment from HubSpot and suggested Strapi could consider a similar, smaller investment to deepen the partnership.

---

## Action Items

**Marcel Santilli (GrowthX)**
- Add Strapi to ContentOS beta; notify Victor Coisne when ready
- Have Bridget reach out to Victor Coisne re: open-source licensing and IP; request introductions to JJ from OSS Capital and Heather (OSS Capital legal partner)

---

## Transcript

**Victor Coisne:** What’s going on, sir?

**Victor Coisne:** Hey, Marcel, how you doing?

**Marcel Santilli:** Really good, man.

**Victor Coisne:** I am driving, that’s why I’m off camera, but yeah, I’m going to San Francisco for next GSConf tomorrow, and yeah, CPI on Thursday.

**Marcel Santilli:** Nice, nice, man.

**Marcel Santilli:** That's awesome.

**Marcel Santilli:** Do you want to maybe, like, plan to connect live, then, on Thursday?

**Victor Coisne:** I am coming, I think, to your CMO breakfast.

**Victor Coisne:** I don't know how much I'll be able to stay, because I have to go to that other conference after, but yeah, up to you, whatever works best.

**Marcel Santilli:** Like, either we can chat quickly now, or...

**Marcel Santilli:** Yeah, let's do both.

**Marcel Santilli:** Yeah, that sounds good.

**Marcel Santilli:** Let's do both, I think, like, would...

**Marcel Santilli:** I think the way I usually like to start these...

**Marcel Santilli:** I've been trying to do a lot of them as well, and it's a way to get feedback and sync up and things like that.

**Marcel Santilli:** We're trying to measure account health based on four vectors, quality of the work product that we're delivering to you, output, and the volume given in relation to the alternative.

**Marcel Santilli:** Meaning, like, if you were doing this with another vendor or in-house and spending a comparable amount of money on that, like, how much output would you get?

**Marcel Santilli:** And, you know, and then the quality of output that we're delivering, and then performance, like, the actual results that that's driving for you based on your expectations, and then overall relationship, how much your team and you enjoy working with us and, you know, want to continue to work with us, you know?

**Marcel Santilli:** So then the way we're doing is, like, one to ten, just to start, and then we'll dig in.

**Marcel Santilli:** One being complete garbage, couldn't be worse, ten being best possible.

**Marcel Santilli:** And so maybe we can start with, like, just going one by one really quickly just with the score, and then we'll dig in, you know, but maybe starting with quality, like, from one to ten, how do you feel the quality of the work product that we're delivering?

**Victor Coisne:** Yeah, give, like, seven or eight.

**Victor Coisne:** We've had some issues that, like, I think the team is catching.

**Victor Coisne:** So it's, and we also had, I think, a lot of changes in terms of account management.

**Victor Coisne:** So I think, like, there's a little bit of a learning curve for each folks.

**Victor Coisne:** So, yeah, I'd say, like, yeah, seven or eight, depending on the week.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** Depending on how good of a day we're having.

**Victor Coisne:** Yeah, exactly.

**Marcel Santilli:** That's funny.

**Marcel Santilli:** What about volume of output?

**Victor Coisne:** I think volume's been pretty consistent.

**Victor Coisne:** Yeah, I'd say, like, yeah, I'd like, a nine.

**Marcel Santilli:** Cool.

**Marcel Santilli:** And then...

**Victor Coisne:** Performance is probably like, yeah, it's seven or eight.

**Victor Coisne:** think like we've seen growth over time, but I feel like it's, I don't know if it's, I don't know what it is.

**Victor Coisne:** I feel like he hasn't, you it's been a year and so, I don't know, maybe my expectation was too high.

**Victor Coisne:** But in terms of like the volume, I was expecting a bit more.

**Victor Coisne:** But then again, like you have to put things into context, right?

**Victor Coisne:** Like with the whole world shifting to, away from Google and into GEO.

**Victor Coisne:** So like, you know, I don't know how much of it is macroeconomic or like, you know, macro level changes versus like growthx performance.

**Marcel Santilli:** That makes sense.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like one, one little anecdotal thing is.

**Marcel Santilli:** Um, I've been doing a lot of, um, like, just overall, like, research for CMSs for my own and things like that.

**Marcel Santilli:** And, um, but then also, like, Webflow is a customer, but we don't work on the kind of content that's similar to the content we do for you.

**Marcel Santilli:** And another agency called Graphite works on that kind of content for Webflow.

**Marcel Santilli:** And I, I've heard from multiple people from Webflow that they're like, oh, and, and brought up strapi specifically.

**Marcel Santilli:** And a lot of the searches they wish they could come up for, because they're going after developers more, uh, they're like, strapi comes up quite a bit.

**Marcel Santilli:** I know there are customer reviewers, like, and it's like, yeah, you're, um, and so, like, for instance, I just search, uh, in AI overview or AI mode for Bass headless CMSs for Next.js.

**Marcel Santilli:** For example, since you're going to the Next.js conference and you are both mentioned and cited there and that, um, you know, in, um.

**Marcel Santilli:** And so it's like, I think there's a lot of good stuff there, but you're right, like, I think there's even more we can probably do to try to make sure, like, we're optimizing and we're actually launching an AI visibility platform that's going to be open that will hopefully also help to correlate the work we're doing with the impact it's having on your AI visibility as well as, like, LLM referrals, you know.

**Victor Coisne:** Yeah, that sounds good.

**Victor Coisne:** Yeah, it's funny because, you know, Josh is also the partner at Hypergrove, so we do see, you know, Webpro, obviously, as a competitor.

**Victor Coisne:** But, yeah, no, overall, like, you know, like, some of the work that we do, like, I think, like, page that comes up is, like, our Next.js landing page, which was, we predest growthx, right?

**Victor Coisne:** So, like, these wheels are, like, trying to measure.

**Victor Coisne:** What DevRel is doing internally versus the contribution of ProSax is bringing, and I think, to me, there is some quicker wins that I'm trying to get to, which is making sure we get the fundamentals right, making sure we have the right metas, and making sure we have FAQ on all pages.

**Victor Coisne:** And I think that's what's, having those fundamentals right, I think it's what drives success in the long run.

**Victor Coisne:** So, you know, first, maybe let's finish your rating scale of 1 to 10, and then I can share a bit more of, like, what I see with this crosshack at the moment.

**Marcel Santilli:** Yeah, let's do that.

**Marcel Santilli:** I think the last one is just relationship, and that's mostly 1 to 10 on, like, the team that's currently you're working with.

**Marcel Santilli:** You know, and then it's overall just...

**Marcel Santilli:** Like, you know, your level for both you and the team, how much you enjoy working with the team you have, essentially.

**Victor Coisne:** Yeah, I'd say I'd put it nine.

**Victor Coisne:** Like, think Vivek and Mara, they're doing a great job.

**Victor Coisne:** Yeah, overall, like, you know, we've had a lot of changes, so that was a challenge in and out of itself.

**Victor Coisne:** But at the same time, like, we got, I feel like we got a stronger team.

**Victor Coisne:** So I'm definitely happy with the folks we have now versus before.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So you've seen an improvement with the team managing things compared to before.

**Victor Coisne:** Correct.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** That's super, that's great to hear.

**Marcel Santilli:** Yeah, like, tell me more, like, dump on me on any feedback, the good, the bad, the ugly, things to improve, you know, things to double down on.

**Marcel Santilli:** We'd love to hear more.

**Victor Coisne:** Yeah, so, like, for me, like, at the moment, like, I'm struggling with, there's a couple of workflows that I feel like your team has dependencies with your engineering team.

**Victor Coisne:** And so this is where, like, some of.

**Victor Coisne:** Frustration comes because my team is like, yeah, this is super quick.

**Victor Coisne:** Like, we should be able to do it.

**Victor Coisne:** And I think we lost a little bit of, like, the self-serve that we, I think, we have initially thought we would have with Air Ops.

**Victor Coisne:** And I think as you guys transitioned to Atlas, I think there, we lost a little bit of that ability to self-serve.

**Victor Coisne:** And it creates a bit of bottleneck because we're, like, my team is like, hey, like, we want to, you know, we can do this.

**Victor Coisne:** Quickly, but we also don't want to make sure that we, we want to make sure we stay integrated with the other workflows.

**Victor Coisne:** So I think that's one point of frustration, especially on the, yeah, the workflow that requires, like, dependency with your engineering team, because that we see a bunch of bottlenecks there where, like, it's taking longer than, than we hope.

**Marcel Santilli:** Got it.

**Victor Coisne:** To give you a specific example, we had one around image generation. It took like almost six months to get something that’s still like, it’s not like mind blowing, right?

**Victor Coisne:** So that was, I think it's also due to the change in the team.

**Victor Coisne:** think there was some information that was probably lost in the transfer.

**Victor Coisne:** But yeah, so that's a specific example.

**Marcel Santilli:** Is the image good now?

**Marcel Santilli:** The image generation?

**Victor Coisne:** Yeah, yeah.

**Victor Coisne:** That one is, we addressed it.

**Victor Coisne:** But like, it's the indication, which is like, yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So like, just to understand on the, in the image stuff, like, how do you feel about the image generation piece now, where it is now?

**Victor Coisne:** Yeah, I'd say like, it's like, it's, it's fine.

**Victor Coisne:** I think like, it's on, on brand.

**Victor Coisne:** But it's, I was hoping for a little more given the time, you know, we had like a lot of back and forth.

**Victor Coisne:** So like, I guess my expectation was, where, you know,

**Victor Coisne:** Because we waited so long, I was expecting for something a little bit more, yeah, significant.

**Marcel Santilli:** Yeah, like one of the things just to like give you kind of like context is like the, it wasn't until very, very recently, like two months ago, even three months ago, that some of the image gen stuff started getting substantially better on text, you know.

**Marcel Santilli:** But then layout following is still extremely difficult.

**Marcel Santilli:** And so the way we had to do it before was like, you had multiple steps where it's like, you're ingesting like 2000 words, and then you're coming up with multiple ideas, then you're having to create HTML layouts essentially of every single potential layout, right?

**Marcel Santilli:** And then the LLM has to then decide, based on the content ideas, which layouts makes the most sense, and then create what texts go in each element of that layout, and then adapt that layout to your brand, and then create any additional assets like

**Marcel Santilli:** I have to go into that layout.

**Marcel Santilli:** so like to get that right, you're essentially like rebuilding entire apps or entire like companies, essentially, that like that's all they do, essentially, like recraft and others, right?

**Marcel Santilli:** And even those, like the output is pretty garbage when you try to use them, in my opinion, right?

**Marcel Santilli:** And so like it's one of the reasons like we do it, but it's like not the core of our offering, you know?

**Marcel Santilli:** But there, I can show, remind me if you come on to the breakfast, like I want to show you some of the stuff we're doing for Lovable and others on the image gen side, that is like more like one shot.

**Marcel Santilli:** And it gets pretty decent, you know?

**Marcel Santilli:** It's just not going to get like crazy nuance, you know?

**Marcel Santilli:** But that's good feedback.

**Marcel Santilli:** And so essentially like, the speed from we need this idea, right?

**Marcel Santilli:** To actually having a workflow that does it, is like where some of the pain points are right now.

**Victor Coisne:** Yes.

**Victor Coisne:** And the ability to self-serve, because like, I don't know, like...

**Victor Coisne:** For me, that's also, like, it's so core to what we do, especially because, you know, we are CMS.

**Victor Coisne:** So, like, that's, we have to also think about, like, what, where the roadmap is for us, the product, and what should be, like, you know, done within Strapi versus done in, outside of Strapi.

**Victor Coisne:** And so, I want to make sure my team is also, like, able to self-server in some capacity.

**Victor Coisne:** But that's where I'm struggling a little bit with, you know, not having access to Atlas the way we add access to Airsoft.

**Victor Coisne:** So, I'm curious, what's your philosophy on that?

**Marcel Santilli:** Yeah, yeah, like, we're planning to open that up quite a bit in the next, like, month or so.

**Marcel Santilli:** the main thing is, like, there's, until, like, like, now, the learning curve is pretty high because, like, you need to get the artifacts right.

**Marcel Santilli:** You need to.

**Marcel Santilli:** We set the right pipelines of the right workflows.

**Marcel Santilli:** The workflows are on code, right?

**Marcel Santilli:** And so there wasn't like a lot of value in having customers operating it because the likelihood of frustration was actually higher than us delivering it.

**Marcel Santilli:** But that is changing because now most of our workflows are agentic and you don't need to stitch together a bunch of workflows.

**Marcel Santilli:** It's mostly like any instruction and it can loop through.

**Marcel Santilli:** And, you know, and then we have like MCP server for workflows, essentially, so that like it can access our workflow builder and build workflows and execute workflows.

**Marcel Santilli:** So it's like very close to getting there to be more like a lovable for building workflows, if you will.

**Marcel Santilli:** And there's a bunch of other things that we'll release soon.

**Marcel Santilli:** And the, what I would say is like the, like what would be ideal scenario for you as far as like, you know, the, I have an idea for a workflow or something.

**Marcel Santilli:** One, two, like, dot, dot, dot, what's next?

**Marcel Santilli:** Like, what is the best case scenario for you?

**Victor Coisne:** Yeah, so.

**Marcel Santilli:** Like, the image gen one, for example, right?

**Marcel Santilli:** Like, okay, I want to create an image gen workflow.

**Marcel Santilli:** Like, what would be your expectation of ideal scenario?

**Victor Coisne:** Yeah, so, like, maybe, like, trying to understand, like, a bit more, like, what's the context you shared about the image gen?

**Victor Coisne:** Like, that's really good context that the team didn't provide.

**Victor Coisne:** So, that would be good to know, like, because maybe, like, you know, if we had known that it was so much work on your end, like, maybe we'd have focused on something else and, you know, eventually, like, not prioritize it in our discussion.

**Victor Coisne:** Because it felt like we still spent a bunch of cycles talking about it.

**Victor Coisne:** And so, like, it was fine for me, like, if the team would have said, okay, like, it's, you know, it's something that we've identified as critical across customers.

**Victor Coisne:** It's just not there yet.

**Victor Coisne:** Let's not focus on this, and we'll let you know when it's ready.

**Victor Coisne:** That's totally fine.

**Victor Coisne:** It just felt like we ended up talking about it too much when you had a bunch of dependency work.

**Victor Coisne:** So in terms of ideal workflow, maybe aligning a bit more on priority, understanding how much work is required on your end.

**Victor Coisne:** Because my understanding as well is because we're on legacy pricing, we have to be very careful with what work stream we prioritize.

**Victor Coisne:** So if we focus on that, that means we're not focusing on something else.

**Victor Coisne:** So I'd rather just the team tells me like, okay, like this is, yeah, this is basically too much work for like, you know, your level of pricing and where, you know, where the team is at in terms of R&D internally.

**Victor Coisne:** so much.

**Victor Coisne:** So we have to focus on lower effort, higher impact.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** That makes a ton of sense because one of the reasons we're kind of – so I guess taking a bit of a step back, what we're trying to figure out is you are an early customer, early believer in us, and so we want to reward that quite a bit.

**Marcel Santilli:** And at the same time, it's been tricky on our end as essentially the kind of customers we have.

**Marcel Santilli:** Just to give you – because you know Josh, Josh will tell you, they're paying Graphite $800,000 a year for essentially very similar work.

**Marcel Santilli:** And our average customer contract now is like $18,000 a month, but we're okay.

**Marcel Santilli:** Like we don't want to like go in one year and one renewal cycle and there's a lot of things.

**Marcel Santilli:** That, you know, early customers like you kind of had the patience to, you know, so we like want to reward that, you know, in a lot of ways.

**Marcel Santilli:** It's really difficult for us is that like when we get like custom engineering work from like, let's say your team, right?

**Marcel Santilli:** Prioritizing that at the exchange of a customer, let's say one of them is paying us $230 a month, right?

**Marcel Santilli:** And so like, how would you, like, what would you do if you were in my shoes, you know, like on, on like managing expectations?

**Marcel Santilli:** Because part of us, want to say yes to everything and do it, but then that means it might be super slow because it's like not the highest priority queue in our engineering queue, essentially, you know?

**Victor Coisne:** Yeah.

**Victor Coisne:** Yeah.

**Victor Coisne:** To me, it's like be very candid with us as far as like managing expectation for like where like this stands in terms of feasibility and, you priority in other, other people's like, just because you're not saying you mutualize across, across customers, just being very transparent.

**Victor Coisne:** And candid about that.

**Victor Coisne:** then ideally giving us a way to self-serve.

**Victor Coisne:** So some of those things is like, hey, the team doesn't have the bandwidth to do it.

**Victor Coisne:** We can go ahead and try to figure it out ourselves.

**Marcel Santilli:** Got it.

**Marcel Santilli:** That makes sense.

**Marcel Santilli:** And I think we're very, very close.

**Marcel Santilli:** So I'll make sure to put you guys as very, very early.

**Marcel Santilli:** Like beta testers, if you will, if you're game.

**Victor Coisne:** You know, give us and things like that and create an environment.

**Marcel Santilli:** I think we're like, at most, I want to say, without overpromising, like a month away from being able to, the main distinction here is like making sure like we can transfer the environments to a place where, you know, today it's just like one environment, right?

**Marcel Santilli:** Like ever in, because it's like all internal teams, you know, and there's like, and then it's just who has access to other environments, like meaning within the teams, but like, it's not.

**Marcel Santilli:** So there's some of that work.

**Marcel Santilli:** And so it's not a matter of.

**Marcel Santilli:** Like, is the functionality there to self-serve?

**Marcel Santilli:** It is there.

**Marcel Santilli:** It's mostly, like, essentially, like, recreating the environment separately for a separate instance of the entire environment.

**Marcel Santilli:** So that, like, when you're, if someone comes in and then decides they want to try to do a million executions, there's, like, nothing that keeps you from doing that, you know, and then breaking everything.

**Marcel Santilli:** You know, like, so it's more of that, of, like, our ability to move faster has been because it's an internal platform, you know.

**Victor Coisne:** Okay.

**Victor Coisne:** Got it.

**Victor Coisne:** So, in all transparency, I was, like, thinking, like, you know, should we look at AirOps for, like, some of the workflow and, like, keep working with GrowthX on some stuff and work with AirOps for other things?

**Victor Coisne:** Like, or should we, so I'm really glad to hear it sounds like we'll have the ability to self-serve and I should probably not go down the path of, like, duplicating work with AirOps workflows.

**Marcel Santilli:** Yeah, like, I would really, really love the chance to, like, make sure that.

**Marcel Santilli:** We can deliver on that front, right?

**Marcel Santilli:** Like, the main, have you gotten a demo of Atlas overall, like end-to-end?

**Victor Coisne:** Yes, we did, yeah.

**Marcel Santilli:** Okay, okay.

**Marcel Santilli:** Because we're going to, we're in the process, just hire a lawyer, we're doing all the IP stuff to open source our framework.

**Marcel Santilli:** So what that means is, like, today, if you go into Aerofs, for example, and you spend, you know, four or five grand a month on the platform, and you put in your API key, right?

**Marcel Santilli:** If you run the kind of workflows we're running, because we were doing that before, like, last year, our bill was almost 30K a month for them.

**Victor Coisne:** Yeah, yeah.

**Marcel Santilli:** And part of it is because, like, just, let's say, the fact checker that we run, like, it's about, like, a thousand different calls, you know, and it's processing so many things, and it's doing research on every single sentence almost, every single passage.

**Marcel Santilli:** Like, so one single article would probably cost you $1,000 in credits in Aerofs.

**Marcel Santilli:** And that's if you...

**Marcel Santilli:** Put your API keys in there, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** There's a lot of tool calling and things that we do on deep research and services that, like, are not natively integrated.

**Marcel Santilli:** You know, like, so what we're doing is, under the hood, what powering all of this is our workflow engine.

**Marcel Santilli:** And that workflow engine is the workflow as code.

**Marcel Santilli:** And so it's all hosted in GitHub, right?

**Marcel Santilli:** So by open sourcing the framework, and then later on giving people access to Atlas, like, it completely separates the workflows.

**Marcel Santilli:** From people that want to use Atlas, which I think we're going to call it ContentOS.

**Marcel Santilli:** But, like, let's just call it Atlas for now.

**Victor Coisne:** Okay.

**Marcel Santilli:** Which that means, like, your workflows can be encoded in a GitHub repo that you own, that is yours.

**Victor Coisne:** Okay.

**Marcel Santilli:** It's run by an open source framework, you know, that is open sourced, right?

**Victor Coisne:** I love it.

**Marcel Santilli:** You just can't sell it, right?

**Marcel Santilli:** Like, you just can't turn around and sell our own framework, right?

**Victor Coisne:** Yeah, I love it.

**Marcel Santilli:** And a runtime layer, if you want to run in our runtime layer, like, that's available if you want to, what I wanted.

**Marcel Santilli:** That's

**Marcel Santilli:** Be cloud-hosted and run it on a runtime layer, right?

**Marcel Santilli:** And then the Atlas platform is more like the system of work, but then everything else is reusable and you can use it and you can run it yourself and it's open source, right?

**Marcel Santilli:** And so it enables anyone to do anything, even beyond marketing and content.

**Marcel Santilli:** And so this platform is more like, I think, a better version than Mastra or LangGraph or Crew.ai, you know?

**Marcel Santilli:** And it has all the primitives of like evals and traceability for both human interventions as well as the executions, ability to replay the executions, all of that stuff.

**Marcel Santilli:** And so it gives people more flexibility than like, let's say, like using NAN, where you would have to use like chat GPT or claw to generate a JSON and then import that JSON into NAN, you know, even though NAN is open source.

**Marcel Santilli:** But it's like, if you were to consider anything, as a friend, I would tell you to consider NAN, not air ops, if you are going to go that path, know, which, you know, has...

**Marcel Santilli:** Thousands of extensions, and it's open source, and has a much bigger ecosystem, whereas Aerofs has pivoted five times in the last two years, you know?

**Victor Coisne:** Yeah, yeah, makes sense.

**Victor Coisne:** Thanks so much for the context.

**Victor Coisne:** I'm excited about this, and we should talk about, like, potentially the launch, because I think we would be happy to, you know, as a big open source project, we kind of love to support and see how we, you know, make sure.

**Victor Coisne:** Because you have the kind of strapi integration out of the box.

**Victor Coisne:** And, you know, NA10, we work with them.

**Victor Coisne:** They use strapi as well.

**Victor Coisne:** And so I feel like for us, we definitely see that kind of, like, workflow orchestration as leaving, it's out of scope.

**Victor Coisne:** But we obviously want to integrate very tightly with those frameworks.

**Victor Coisne:** And so if you open source, that's, like, perfect in terms of, you know, DNA.

**Marcel Santilli:** So happy to talk about how we can amplify that launch.

**Marcel Santilli:** Yeah, that would be amazing, and I know this is kind of, like, a little bit out there, and it's not, like, what series, like, when was your last fundraise?

**Victor Coisne:** I'm just trying to remember.

**Victor Coisne:** Series B, $31 million, like, a year and a half ago.

**Marcel Santilli:** Okay, one thing, like, I don't know if you guys have ever done, but have you guys ever done a strategic investment at all?

**Marcel Santilli:** The reason I ask is just because we just, you know, off the record, just closed a strategic investment from HubSpot, and then there's a few others that are interested, and it's, like, it's not a huge check, but we could think of, like, deepening the relationship in that perspective, essentially.

**Marcel Santilli:** And, but regardless, right, like, I'm just, like, I would love to, as we launch, like, work with you closely on, like, both feedback, how...

**Marcel Santilli:** We can, like, talk about it more publicly as well.

**Marcel Santilli:** And then, like, and also, if there's anyone on your end on that is knowledgeable about open source licenses and things like that, like, we're just kicking off the patent process and then the open source license process.

**Marcel Santilli:** So if you know anyone at all, please let us know.

**Victor Coisne:** Oh, I do.

**Victor Coisne:** I do.

**Victor Coisne:** I do.

**Victor Coisne:** I mean, that's, you know, that's my bread and butter.

**Victor Coisne:** So I know a lot of people that, I know a lot myself about open source license, and I know a lot of people that, you know, actual lawyers that could help, you know, like, obviously, I'm thinking about JJ from OSS Capital.

**Victor Coisne:** I don't know if you know him.

**Victor Coisne:** But, yeah, he would be a good person to talk to.

**Victor Coisne:** He has, like, one of his GP is, he's a lawyer, Heather.

**Victor Coisne:** So I'm happy to connect you guys if you want.

**Marcel Santilli:** Let me have Bridget reach out to you because, like, she's just kicking off that process with, like, there's a couple people she used, one shows that.

**Marcel Santilli:** And I'm talking to Jean on Thursday as well, but yeah, like I'll have her reach out to you if that's okay.

**Victor Coisne:** Yeah, totally.

**Marcel Santilli:** Have you met her?

**Marcel Santilli:** Or have you connected with her before?

**Victor Coisne:** She used to be at AirBite.

**Victor Coisne:** AirBite, yeah, yeah, I've connected with them quite a bit.

**Victor Coisne:** I mean, I know Jean really well.

**Marcel Santilli:** I actually invested into AirBite.

**Marcel Santilli:** Oh, nice.

**Marcel Santilli:** Yeah, I love Jean, and AirBite is a really good customer, and then Mario is a close friend now, you know.

**Victor Coisne:** I know, I know.

**Victor Coisne:** I remember you guys being connected to each other.

**Marcel Santilli:** We're going to do a, we got to do a barbecue.

**Marcel Santilli:** But I got to run, but like, good luck at the Next.js conference, and then hopefully I'll see you Thursday, because I'll love to like show you some things live really quickly too, just to get your feed too.

**Victor Coisne:** Yeah, that sounds great.

**Victor Coisne:** And one last thing, I was on the Scaling DevTool podcast.

**Victor Coisne:** was Scaling DevTool I was

**Marcel Santilli:** This week, and talking a lot about growth, so hopefully, that brings you to the end of I really appreciate it, and I know you sent us a lot of intros and things like that, and it means a lot, like, how much you've supported us, you know, so very, very soon, like, we'll give you the ability to self-serve, and so we'd love to show you stuff Thursday, too, to get your feedback.

**Victor Coisne:** Awesome.

**Victor Coisne:** Appreciate it.

**Marcel Santilli:** Thanks, Marcel.

**Marcel Santilli:** All right.

**Marcel Santilli:** Thanks, man.

**Marcel Santilli:** See ya.

**Victor Coisne:** Bye.
