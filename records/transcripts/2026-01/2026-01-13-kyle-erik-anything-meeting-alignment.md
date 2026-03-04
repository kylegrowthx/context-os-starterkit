# Kyle/Erik - Anything meeting alignment

<metadata>
date: 2026-01-13
time: 19:01 UTC
duration: 40 minutes
organizer: katya@growthx.ai
participants: Kyle Gaudreau, Erik O'Brien, Katya Luscomb
fathom_recording_id: 113955390
fathom_url: https://fathom.video/calls/531470557
share_url: https://fathom.video/share/h4mceiLzoeVkQepL2yvb1G_-pzJSnsx2
source: fathom
enriched_on: 2026-02-28T14:32:00Z
enriched_by: Claude
</metadata>

---

## Summary

Kyle, Erik, and Katya prepared for a critical client meeting by reviewing the technical migration issues, reporting gaps, and communication strategy. The team aligned on leading with a concrete migration plan focused on fixing incorrect canonical tags, securing GSC access, and clarifying GA4 reporting, while positioning optional PSEO as a strategic upgrade if the client pushes for faster growth.

---

## Context

GrowthX is managing the Anything.com project, a B2B content marketing engagement focused on domain migration and organic growth. The client has implemented a multi-domain strategy (anything.com, createanything.com, create.xyz) but has made critical technical errors in the migration setup—specifically, canonicals incorrectly point all domains to createanything.com instead of consolidating on anything.com as the primary domain. Additionally, the client's analytics setup lacks the proper GA4 configuration and GSC access to report on organic-to-revenue performance, creating a reporting gap that limits the team's ability to demonstrate ROI. The client has expressed frustration in prior calls, and this meeting is critical to reestablish confidence and alignment on a clear roadmap forward.

---

## Relevance

- **Client Relationship Repair:** The client has had two negative calls previously; this meeting is critical to rebuild trust and demonstrate forward momentum through concrete, actionable plans.
- **Technical Blocker:** The canonical tag misconfiguration is actively undermining the migration and must be addressed before meaningful progress can be measured.
- **Reporting Foundation:** Without proper GSC access and GA4 domain isolation, the team cannot measure organic-to-revenue performance, limiting the ability to demonstrate ROI and validate strategy.
- **Growth Strategy Trade-offs:** PSEO is positioned as a high-potential option (faster volume, higher conversion rates per Lovable project) but requires careful framing as an investment with upfront complexity, not a quick add-on.
- **Internal Alignment:** The team needs to stay action-oriented and avoid circular venting sessions; clear roles (Katya leading, Kyle on technical details, Erik on strategy context) help manage the client dynamic.

---

## Overview

- **Migration Fix is Top Priority:** The client's incorrect canonical tags point all domains to `createanything.com`, undermining the migration to the primary `anything.com` domain. Fixing this is the most critical technical task.
- **Reporting is Blocked:** Organic-to-revenue reporting is impossible without GSC access and a GA4 setup that isolates traffic by domain. Kyle’s upcoming projections will be traffic-only until these are resolved.
- **PSEO is a Strategic Option:** Programmatic SEO (PSEO) can deliver faster scale and higher conversion rates (per Lovable project data) but requires pausing editorial work and a significant upfront investment, which must be framed carefully.
- **Meeting Strategy is Action-Oriented:** The team will lead with a concrete migration plan and roadmap to counter client frustration and maintain a productive, forward-looking discussion.

---

## Key Topics

### Technical SEO & Migration Issues

  - The client's migration to the primary `anything.com` domain is stalled by critical technical errors.
  - **Incorrect Canonical Tags:**
      - **Problem:** All pages across all domains (e.g., `createanything.com`, `create.xyz`) point their canonicals to `createanything.com`.
      - **Impact:** This sends Google conflicting signals, preventing the consolidation of authority on `anything.com`.
      - **Solution:** Implement cross-domain canonicals pointing all non-homepage pages to their `anything.com` equivalent.
  - **Content Duplication:**
      - New content is published simultaneously across all three domains, creating unnecessary duplication.
      - **Action:** Ask the client if future content can be published exclusively to `anything.com`.
  - **Sitemap Issue:**
      - All sitemaps now list `anything.com` URLs, which is technically functional for the migration but confusing.
      - **Decision:** Prioritize the canonical tag fix; the sitemap issue is a lower priority.

### Reporting & Performance Measurement

  - Organic-to-revenue reporting is blocked by two key issues:
  - **Missing GSC Access:**
      - Access to the `anything.com` GSC profile is required for accurate traffic projections and performance analysis.
  - **Flawed GA4 Setup:**
      - The current GA4 profile aggregates data from all three domains, making it impossible to isolate performance for `anything.com`.
      - **Action:** Request a GA4 setup that allows domain-specific reporting.
  - **PostHog Discussion:**
      - The team will ask the client for a walkthrough of their PostHog setup to understand their current measurement framework.
      - **Rationale:** Segment (a data pipeline) is not the reporting tool; PostHog is the visualization layer. Understanding their setup is crucial to proposing a viable organic-to-revenue reporting solution.

### Strategic Options: PSEO vs. Editorial

  - PSEO was discussed as a path to faster scale, but it requires careful framing.
  - **PSEO Benefits:**
      - Higher conversion rates (per Lovable project data).
      - Faster volume output once the initial setup is complete.
  - **PSEO Challenges:**
      - **Investment:** Requires pausing editorial work and a significant upfront investment (e.g., 3-4 weeks for a team of three on the Lovable project).
      - **Expectation Management:** Must be framed as a strategic shift, not an add-on to the current scope.
  - **Decision:** PSEO will be presented as a strategic option if the client pushes for faster scale.

### Client Meeting Strategy

  - The team will lead with a concrete, action-oriented plan to counter client frustration and maintain a productive discussion.
  - **Agenda Focus:**
      - **Migration Plan:** Present the canonical tag fix as the top priority.
      - **Reporting Needs:** Clearly state the requirements for GSC access and a GA4 setup that isolates traffic by domain.
      - **Roadmap:** Present Kyle's traffic-only projections and a potential PSEO strategy.
      - **Ongoing Work:** Briefly mention the steady cadence of editorial content production.
  - **Team Roles:**
      - **Katya:** Lead the meeting, focusing on the roadmap and action items.
      - **Kyle:** Explain the technical details of the migration plan and reporting needs.
      - **Erik:** Provide strategic context and acknowledge any past misalignments on expectations.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Add agenda item for Drew re: future-post-only to anything.com; confirm Sanity/canonical setup
- Update agenda wording re: analytics/reporting; include 'pending access' clarity
- Add agenda note re: ongoing content production

**Kyle Gaudreau (GrowthX Labs)**
- Review prior call transcripts re: PostHog/GA4/GSC + traffic projections
- Validate GA4 property scope; start migration-aware reporting (domain split, canonical monitoring)

---

## Transcript
**Katya Luscomb:** This meeting is being recorded.

**Katya Luscomb:** I was looking back through their space to see if we linked to that strategy that you had just brought up in the internal channel.

**Katya Luscomb:** I don't see it linked anywhere.

**Katya Luscomb:** I can go back and look at the call transcript later, too.

**Kyle Gaudreau:** Yeah, I'm just curious.

**Kyle Gaudreau:** Like, you know, it's framed as like, I need to dig into it more deeply.

**Kyle Gaudreau:** Like, um, oh, here.

**Erik O'Brien:** Hey.

**Katya Luscomb:** Hey, hi.

**Kyle Gaudreau:** We were just talking about, I don't know if you saw the thing I dropped in the channel just a handful of minutes ago, but I was, I had a question for the team about that, like, content strategy doc we put together and whether we actually, like, ever reviewed that with him.

**Kyle Gaudreau:** Just knowing that we've had all this, like, telephone game and, like, him saying we did something or we didn't,

**Kyle Gaudreau:** So I wasn't sure where that fell in, but I don't know if you have any knowledge of that.

**Kyle Gaudreau:** Like, I was trying to look at the viewers, and I can't see him, but Notion does this annoying thing where it says, like, one more viewer and won't let me see who that person is.

**Kyle Gaudreau:** So maybe that's Drew.

**Erik O'Brien:** Anything editorial content strategy?

**Kyle Gaudreau:** Yeah.

**Erik O'Brien:** Yeah, we reviewed that with him live, and he gave feedback.

**Erik O'Brien:** I don't know if he ever jumped in to...

**Kyle Gaudreau:** It's hard if he never jumped in.

**Kyle Gaudreau:** More just, like, yeah, kind of, like, you know, the way this has gone, he might not even remember reviewing that, but...

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Okay, that's good.

**Kyle Gaudreau:** Because, yeah, basically, for the projections, what I'm, you know, going to be doing is just one, trying to see what, like, kind of story that tells.

**Kyle Gaudreau:** I'm guessing it's not going to be one that he's going to be maybe as thrilled with, but we need to kind of, anchor him on, like, some...

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Level of, you know, what's realistic but aggressive, things of that nature, and then depending on what that story tells, we might need to supplement with, like, you know, you kind of framed it in the doc, although I'm like, I'm hesitant to, like, frame it as, like, a strategy refresh, although there's, like, some give or take here, right?

**Katya Luscomb:** Like, want to demonstrate urgency.

**Kyle Gaudreau:** We have some positive signals, but these projections should really give us a better point of alignment of, like, what path are we really on?

**Kyle Gaudreau:** And we just need to continue to push emergently on, like, just cleaning up this  of migration.

**Kyle Gaudreau:** It's so poorly done.

**Kyle Gaudreau:** You know, like, I don't know if you saw my latest note, but they implemented canonicals, and they did it completely wrong.

**Kyle Gaudreau:** And it's almost, like, it's confusing, because, like, they're pointing to createanything.com.

**Kyle Gaudreau:** So, you know, basically, like, everything should...

**Kyle Gaudreau:** would be pointing to anything is the future.

**Kyle Gaudreau:** That's the primary domain.

**Kyle Gaudreau:** We want to solidify that.

**Kyle Gaudreau:** And so we want to just make sure he's continually focused on that.

**Katya Luscomb:** There's one of the questions I had about agenda-related.

**Katya Luscomb:** I found that the keyword research from competitive trailblazer marketing, I think it is, and was looking at that.

**Katya Luscomb:** And they update that every day.

**Katya Luscomb:** And their most recent version, even through December, all the URLs that they're linking back to from completed work, they're still linking back to create anything as well.

**Katya Luscomb:** And I think we publish on Sanity the same way that they do.

**Katya Luscomb:** And right now, everything gets published to create anything and anything.

**Katya Luscomb:** And I wasn't sure if that becomes problem.

**Kyle Gaudreau:** Now it duplicates across all of them, it appears, at least from the spot checks I could see.

**Kyle Gaudreau:** Like, I think that's just basically how he has it set up.

**Kyle Gaudreau:** Because he was kind of referencing it in the past call that it's kind of like one app, if you will.

**Kyle Gaudreau:** ...

**Kyle Gaudreau:** ...

**Kyle Gaudreau:** ...

**Kyle Gaudreau:** So it just propagates everything out.

**Kyle Gaudreau:** And so, like, similarly, these canonical tags, they set up a single canonical that they just applied across all the pages, across all the domains.

**Kyle Gaudreau:** And so I think that's what's happening is, like, you could go publish to anything.

**Kyle Gaudreau:** And I believe what would happen, but we should validate this with some of, like, the technical setup is that would implement that same blog post across all three domains today.

**Kyle Gaudreau:** We should ask him actually explicitly, is there anything, is there anything we can do to just post those URLs to the new domain?

**Kyle Gaudreau:** Like, is there a way to kind of, like, separate that now moving forward?

**Kyle Gaudreau:** That would be ideal to not continue to create more content on the old domains.

**Katya Luscomb:** That's what I was thinking.

**Katya Luscomb:** Like, it seemed odd to continue to publish, like, if...

**Katya Luscomb:** If we're trying to actually migrate, it was odd to me to be publishing across all of them.

**Katya Luscomb:** So, cool.

**Katya Luscomb:** That was one of the things that I had flagged.

**Katya Luscomb:** I'll add that a more specifically.

**Kyle Gaudreau:** And I think the thing that's just challenging with this situation is like the technical SEO foundation of this is going to continue to add some friction to our success.

**Kyle Gaudreau:** So anytime we need to think about the story we're telling in performance, we don't want to just always make excuses or anything like that.

**Kyle Gaudreau:** But we want to continue to make sure we are framing in the reality of what we're trying to do.

**Kyle Gaudreau:** And that's why we want to do some of these things with urgency.

**Kyle Gaudreau:** And my feeling is this plan that we just sent him is the best of both worlds.

**Kyle Gaudreau:** And, you know, hopefully he's...

**Kyle Gaudreau:** It's apprehensive about something and that continues to slow us down, but that's just so critical for our content.

**Kyle Gaudreau:** So anytime we're kind of like talking about this and setting expectations, we just need to always think about that balance of how we bring that in without not sounding like we're making excuses, we're adapting, but also being mindful that that's a real thing.

**Kyle Gaudreau:** Regardless of who he goes to, what he does, who he does it with, like, it's just the reality of the SEO setup.

**Katya Luscomb:** Mm-hmm.

**Katya Luscomb:** Or, like, you know, working forward from our starting point, making sure that we're leveraging everything the best way we can to move the needle in an actionable way for him and trying to do so with some rapid execution.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** And perhaps, I mean, you know, the way I frame the projections, it probably just needs to be in some sort of, like, yeah, current state, you know, roadmap timeline perspective, regardless if we're not even changing plan.

**Kyle Gaudreau:** It's probably going to need to have some layer of that for him to feel satisfied.

**Katya Luscomb:** That makes sense.

**Katya Luscomb:** Let me share my screen really quick with the agenda.

**Katya Luscomb:** I honestly feeling, where am I?

**Katya Luscomb:** There we go.

**Katya Luscomb:** I was feeling a little bit stuck with some of the things I was putting on here.

**Katya Luscomb:** At this point, we've got the migration plan, which feels really actionable.

**Katya Luscomb:** I know you're working on a longer potential roadmap for Friday.

**Katya Luscomb:** Otherwise, I figured we could spend some time making sure that we really understand his priorities.

**Katya Luscomb:** He's talked a lot about linking to revenue and things.

**Katya Luscomb:** I wasn't sure how much it was worth digging into.

**Katya Luscomb:** I had some questions for him outside of having Looker.

**Katya Luscomb:** Are there ways that we can report on this that would be helpful for you on a regular basis?

**Katya Luscomb:** I don't want to get us into a rabbit hole where we're committing to...

**Katya Luscomb:** Sending like insane reports every week, but like snapshots or things and like, you know, what, what would be most helpful for him to see in those highlights to feel like we're making progress.

**Katya Luscomb:** I don't know if we wanted to ask it so open-ended or if there were specific recommendations that we could offer.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And admittedly feeling nervous going into this call, having had two bad ones with him.

**Katya Luscomb:** Yeah.

**Kyle Gaudreau:** Well, understandable, what I would say is, you know, easier said than done, but, you know, you want to, like, you want him to feel solid about, as he should, you as the, the, the go-to person here, you know, you know, the subtle ways of like, just it.

**Kyle Gaudreau:** And I'm trying to be mindful with my communication with him as well, of just like, little things that could communicate kind of like, uncertainly.

**Kyle Gaudreau:** Uncertainty, lack of confidence and whatever, like we just, we don't want to introduce that like doubt into his mind.

**Kyle Gaudreau:** Related to like, that first bullet, I mean, I think we can confidently say he's going to say revenue, right?

**Kyle Gaudreau:** Like, based off what he said thus far, that does appear to be counter to what he said in the early days of disengagement.

**Kyle Gaudreau:** But that appears to be like, will he get frustrated by that framing, you know?

**Katya Luscomb:** Right, like I've already told you this.

**Kyle Gaudreau:** Because clearly he has some sensitivity around that, right?

**Kyle Gaudreau:** Of like, for example, still under the same section.

**Kyle Gaudreau:** One of the things I was kind of like kicking around in my mind that we could propose is like, could you do like a brief walkthrough of how you...

**Kyle Gaudreau:** Measure success of your channels and how you think about that, what that looks like in post-hog.

**Kyle Gaudreau:** The question I have is, didn't he seem to almost infer that he's already done that with us?

**Katya Luscomb:** And is that true?

**Katya Luscomb:** He inferred that he has brought up tracking in post-hog.

**Katya Luscomb:** I wasn't sure.

**Katya Luscomb:** Yeah, don't know if he said that had, like, given us a walkthrough of it yet.

**Katya Luscomb:** Erik, do you remember post to my knowledge.

**Erik O'Brien:** Like, yeah, I don't remember post-hog.

**Kyle Gaudreau:** I know, like, when we did the product deep dive, he may have talked about it.

**Kyle Gaudreau:** Like, that's where they do a lot of product analytics.

**Erik O'Brien:** But for, like, us specifically, we had at least one conversation about how we use GSC and Google Analytics.

**Erik O'Brien:** And he was potentially going to set up tracking events in GA4.

**Erik O'Brien:** And I think that was, like, one of the last meetings I was at.

**Kyle Gaudreau:** Got it.

**Kyle Gaudreau:** Yeah, can we just, like, before the meeting, just double check the transcript and see how it's framed?

**Kyle Gaudreau:** Like, it feels like something that would be useful for our time and understand where, how he thinks about it and what the potential gaps are, because, yeah, he was, like, not, I was, like, trying to pull it out of him in the last meeting of, like, of, like, what they have in place to track this, and it didn't sound like there was anything, and so it would love to understand.

**Kyle Gaudreau:** I know he mentioned segment, and this and that.

**Kyle Gaudreau:** The reason I'm not asking for segment access, just to, like, make this clear, unless segment has changed since I've been hands-on with it, which is certainly possible, think of what segment is doing as largely, like, connecting pipes together of different systems, and then the people moving through those pipes, they're creating attributes, reproducing IDs, around?

**Kyle Gaudreau:** Milpl

**Kyle Gaudreau:** Things of that nature.

**Kyle Gaudreau:** And it provides a unified system to allow you to understand your data across these systems and connect them.

**Kyle Gaudreau:** Some similarities to, like, an Airbyte to a degree, but it's different.

**Kyle Gaudreau:** And so the utility for, like, when I was at Trey, for example, is, like, we had Segment across all our platform, like, all our web properties.

**Kyle Gaudreau:** And when we would think about, like, hey, I wonder if we can measure this or what happened in this situation, whatever it may be.

**Kyle Gaudreau:** A lot of times it would come back to, like, oh, well, there's going to be an ID associated to that person.

**Kyle Gaudreau:** There's going to be attributes tied to that ID, such as, like, the referring domain that they came in from, whether that's Google or ChatGPT or whatever it may be.

**Kyle Gaudreau:** And that we could use that to work back and create reports off of that data to, like, work back to what happened.

**Kyle Gaudreau:** Segment, though, is not the place that you're building those reports and doing that.

**Kyle Gaudreau:** It is the thing that is helping provide you the foundation to do that reporting elsewhere more often than not.

**Kyle Gaudreau:** So usually what that's doing is writing into, like, a database or something like that.

**Kyle Gaudreau:** This depends on, you know, their setup.

**Kyle Gaudreau:** And then a posthog is the visualization of that.

**Kyle Gaudreau:** And so if we want to report on organic search to revenue, the question then is, is, like, do you even have that set up now to identify, like, organic traffic?

**Kyle Gaudreau:** And do you have that tied to your metrics in some way?

**Kyle Gaudreau:** And if you don't, then that's how could we possibly report on your revenue because you don't have a source of truth for that yet.

**Kyle Gaudreau:** But now I would expect he has some sort of chain of reporting.

**Kyle Gaudreau:** He's got all these different agencies and things like that.

**Kyle Gaudreau:** So, you know, it's a question of, like, what is actually in place.

**Kyle Gaudreau:** So hopefully.

**Kyle Gaudreau:** Hopefully that's helpful.

**Kyle Gaudreau:** just wanted to frame this a little bit because I don't know where he'll push it, but to me it's not necessarily useful for us to get segment access because we're not going to set up or tweak your segment implementation or anything like that.

**Kyle Gaudreau:** Honestly, that's not even my expertise.

**Kyle Gaudreau:** Maybe we have some people that have done that here, but that's a world we don't want to be usually touching.

**Kyle Gaudreau:** Nor do we want to necessarily tweak his post hoc.

**Kyle Gaudreau:** It's usually like, this is what we would want to see.

**Kyle Gaudreau:** Here's how we've seen some teams set this up.

**Kyle Gaudreau:** You guys should do this.

**Katya Luscomb:** Makes sense.

**Katya Luscomb:** Cool.

**Katya Luscomb:** I'll see.

**Katya Luscomb:** I'll fine tune this wording a little bit and flag.

**Kyle Gaudreau:** The other thing too is like just for the pending access, anytime we ask for this just to make it like super clear for him is just calling out So...

**Kyle Gaudreau:** Thank

**Kyle Gaudreau:** And I did check this morning, we still don't have anything, GSC profile, which that would be very helpful for me to see, as I think about projections, like, it's a lot harder to do that without that.

**Kyle Gaudreau:** That makes sense.

**Kyle Gaudreau:** The other thing in terms of projections, by the way, like, I'm not planning on projecting, like, revenue at the moment, like, I don't even know if we can measure it, you know, maybe he can give us some assumptions and some other things we can reference later on to add to the projections, but these are going to be about traffic.

**Katya Luscomb:** Okay, are there questions related to that that would be helpful within our meeting with him today to add into this agenda?

**Katya Luscomb:** right.

**Kyle Gaudreau:** Related to the projections, or let me think about that.

**Katya Luscomb:** I don't think so.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Could always chat about some of that live, you know, and I might probably be good for me just to go back and refresh my memory on the past call and how he framed some of it.

**Kyle Gaudreau:** I know he said some things around, like, is this going to be a 2 to 3x channel is how he kind of thinks about these channels.

**Kyle Gaudreau:** I can't remember if he may have said something in terms of, like, time horizons related to that.

**Kyle Gaudreau:** So it's like, yeah, that's an important thing just to make sure I get right.

**Kyle Gaudreau:** So I can double check.

**Katya Luscomb:** And then I saw, I saw your notes on, like, the migration.

**Katya Luscomb:** So I figured I'd flag, um, I typed up some of the, like, my core understanding of the canonical piece here.

**Kyle Gaudreau:** Quite simply, anything non-homepage, there are today three versions of that URL.

**Kyle Gaudreau:** Every single domain should have a canonical URL on it that is the anything.com version of that URL.

**Kyle Gaudreau:** That individual URL, um, that is the most ideal setup.

**Kyle Gaudreau:** So on anything.com, that would be thought of as a self-referring canonical, and then, and the, uh, other two are point, are cross-domain, pointing to the correct domain, which is just helping Google think through, well, I'm getting confusing signals here.

**Kyle Gaudreau:** What's happening?

**Kyle Gaudreau:** Oh, this is the priority.

**Kyle Gaudreau:** You're telling me this is the priority page.

**Kyle Gaudreau:** Uh, and we're just not wanting to do that for the homepage.

**Kyle Gaudreau:** Um.

**Kyle Gaudreau:** Because that will just minimize the risk to losing those, like, pretty important rankings they have for create.xyz on their homepage currently.

**Kyle Gaudreau:** But over time, as anything.com matures, the hope is that that becomes less and less of a risk and that we can more officially do that migration.

**Kyle Gaudreau:** We can put in the canonicals on those pages and then anything.com becomes that source.

**Kyle Gaudreau:** And as this progresses, depending on what we see, and I'll need to kind of work with you on, like, how to work this into our reporting that we share with them.

**Kyle Gaudreau:** It doesn't have to be too complicated.

**Kyle Gaudreau:** I can set up some kind of, like, automated reporting.

**Kyle Gaudreau:** Is, you know, like, just monitoring, is this happening at the velocity we want to see?

**Kyle Gaudreau:** And if we're seeing any concerns, we could then recommend redirects later on.

**Kyle Gaudreau:** So that should be balanced.

**Kyle Gaudreau:** Fathom his concerns and speed and things of that nature.

**Kyle Gaudreau:** So if we had the luxury of sitting down with him from day one when he thought about all this, I definitely would have recommended he not take the approach he did.

**Kyle Gaudreau:** But where we are, where we are.

**Katya Luscomb:** Yeah, exactly.

**Katya Luscomb:** Okay.

**Katya Luscomb:** And then the other piece, because I know we've talked about it with Al about, like, you know, potentially realigning with him.

**Katya Luscomb:** I'm like, you what does, what does our communication and coordination among us look like that would be supportive?

**Katya Luscomb:** I pretty much, like, hesitant to offer weekly calls because I don't necessarily want just go, like, round and round.

**Katya Luscomb:** But I think it might be helpful going forward.

**Katya Luscomb:** I mean, some of these are the things we already do, but I wanted to make sure that, like, he has a chance to share if there's anything else that would be helpful.

**Katya Luscomb:** And I have these, like, weekly performance snapshots because, like, he's so performance focused.

**Katya Luscomb:** And this was a piece where...

**Katya Luscomb:** I just want to make sure in offering this that I am not potentially walking us into an insane amount of work.

**Kyle Gaudreau:** I mean, I suppose there's always the possibility.

**Kyle Gaudreau:** just depends on to what degree he wants data on, but we should work to align him on that.

**Kyle Gaudreau:** Like, generally what we should be aiming for is, like, whether it's weekly, bi-weekly, that, like, updating that should not take any more than an hour of time.

**Kyle Gaudreau:** If it is greatly higher than that, then there's, you know, maybe just too much complexity or something like that.

**Katya Luscomb:** Or something's not separate or, yeah.

**Kyle Gaudreau:** I was looking at, you know, their data and Looker.

**Kyle Gaudreau:** It looks like it's continuing to look pretty good.

**Kyle Gaudreau:** You know, the thing

**Kyle Gaudreau:** The though, is, like, this is all set up for, like, createanything.com.

**Kyle Gaudreau:** And so what basically, let me just show my screen real quick.

**Kyle Gaudreau:** This will make it a little bit clearer just to make sure we're super clear.

**Kyle Gaudreau:** Because I don't think I really appreciate this nuance when I was looking at this before.

**Kyle Gaudreau:** So when we look at a view like this, and we're looking at sessions, oops, this is GA4 data, just to be super clear.

**Kyle Gaudreau:** In the way they have GA4 set up currently, it is the same profile across all three domains.

**Kyle Gaudreau:** And, oh, you know what?

**Kyle Gaudreau:** Actually, I'm not 100% sure.

**Kyle Gaudreau:** I believe, don't quote me on this, but I believe, right?

**Kyle Gaudreau:** Now I can validate this.

**Kyle Gaudreau:** Essentially what this is showing us is traffic across all three domains.

**Kyle Gaudreau:** I'm fairly certain because if you look at the URLs here, they don't have a domain attached.

**Kyle Gaudreau:** And then, of course, there's three versions of it.

**Kyle Gaudreau:** So that's essentially what that's telling us, which is like a, you know, good to see this continuing to go up into the right.

**Kyle Gaudreau:** Now, this also does include referral traffic.

**Kyle Gaudreau:** I just got rid of CPC.

**Kyle Gaudreau:** So this.

**Kyle Gaudreau:** This is going to be like AI visibility based things, things of that nature, but like, that's, you know, that makes sense.

**Kyle Gaudreau:** So that's good.

**Kyle Gaudreau:** While we go to this view, the non-branded view, part of this, what this view is helpful for is to look at non-branded traffic because they have, you know, a decent amount of branded traffic that comes through.

**Kyle Gaudreau:** But this is only going to show data for createanything.com currently.

**Kyle Gaudreau:** But we need access.

**Kyle Gaudreau:** So it's.

**Kyle Gaudreau:** This would be anything.com, yeah, but also, like, then it's, like, we should show some sort of reporting that's, like, across all three domains, I think we certainly need to figure that out, bringing them to lookroom might be challenging, so that's part of what we'll need to figure out, but just, like, as you think about, like, these URL clicks, that's what's important to kind of keep in mind here, and so a of view of what's actually happening across these domains, and then it's healthy.

**Kyle Gaudreau:** How much traffic is coming from each one of these domains from this view is not super clear.

**Kyle Gaudreau:** I can maybe see if I can build that in, but that's just, like, bit of nuance that, like, might not be super clear if you're, like, looking at the data and talking about it, and then you may ask questions.

**Kyle Gaudreau:** The way this is currently set up is, you know, the GA4v will actually tell us what's happening across all these pages since you're all putting content everywhere, so.

**Katya Luscomb:** So.

**Katya Luscomb:** So.

**Katya Luscomb:** Yeah, that is actually super helpful.

**Katya Luscomb:** Also thinking through, like, I'm sure he's going to have questions about, like, well, I want to see specifically, like, anything.com, GSC, and GA4.

**Katya Luscomb:** So we just, yeah, like you said, working on splitting up, if we can, the GA4 data, and then actually getting access to GSC.

**Kyle Gaudreau:** Yeah, so what I'll probably do as a quick follow-on from the projections is trying to figure out some of that.

**Kyle Gaudreau:** It's like, okay, like, how do we need to evolve this reporting to be able to be mindful of this migration and all the complexity here and something that's a little bit more repeatable?

**Kyle Gaudreau:** So I can probably start doing that.

**Kyle Gaudreau:** I don't have a good pulse on how long these projections are going to take me right now.

**Kyle Gaudreau:** Sometimes they're pretty easy, but this one has so many variables that I think it's going to be longer.

**Kyle Gaudreau:** So I can maybe start with the reporting this week, but it's probably more likely early next week, which should still give us time before the next meeting, right?

**Kyle Gaudreau:** So your next meeting with him outside of time.

**Katya Luscomb:** Today is not this Thursday that's following.

**Kyle Gaudreau:** Correct.

**Kyle Gaudreau:** That should be fine then.

**Kyle Gaudreau:** We should have time.

**Katya Luscomb:** Okay, cool.

**Katya Luscomb:** Sitemap updates.

**Katya Luscomb:** Looks like you said those are done the right way, so we don't need to worry about that as an action item for him.

**Kyle Gaudreau:** So, share my screen again.

**Kyle Gaudreau:** By the way, it be a good thing to download considering all this that's happening with this account.

**Kyle Gaudreau:** It's helpful for other accounts as well, but it just gives you, like, quick stuff.

**Kyle Gaudreau:** You can see this Chrome extension, right?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** This is, what is this one called?

**Kyle Gaudreau:** SEO Pro extension.

**Kyle Gaudreau:** That's the company.

**Kyle Gaudreau:** But I think if you search for this, you'll find it.

**Kyle Gaudreau:** it.

**Kyle Gaudreau:** MRS for actually learned.

**Kyle Gaudreau:** And But I'm

**Kyle Gaudreau:** What's just helpful about this is like you can quickly see a couple of things.

**Kyle Gaudreau:** can see their sitemap, can see their robots.txt if they have one, can see their canonical tags, can see their meta-titles and stuff like that, and like a really helpful just like what's happening on this page.

**Kyle Gaudreau:** So here's anything.com.

**Kyle Gaudreau:** And so you can see like, okay, cool, like we have anything.com URLs.

**Kyle Gaudreau:** Let me actually validate, this is true.

**Kyle Gaudreau:** Oops.

**Kyle Gaudreau:** Yeah, these are all anything.com URLs.

**Kyle Gaudreau:** Okay, cool.

**Kyle Gaudreau:** I think what they did is they have now all the other domains pointing to the crate, or to anything.

**Kyle Gaudreau:** Which is weird because the site map points to the canonical tags.

**Kyle Gaudreau:** It's not, it's just like, why did you do that?

**Kyle Gaudreau:** Uh.

**Kyle Gaudreau:** Okay, so here's the create anything sitemap, anything URLs, okay, so, honestly, I don't think it's a huge deal if they leave it as it is, but I do recommend that they, like, just point it to the domain it's actually on, just to, like, avoid confusion for Google, look less shady, things like that.

**Kyle Gaudreau:** Yeah, okay, so they just applied it across the board, so all their sitemaps now point to that.

**Kyle Gaudreau:** So it's better than it was for the migration purposes, we could certainly push to say, you know, this should say create.xyz, because that's the domain run, and then, of course, it didn't create anything, but I don't know if it's Maybe pick our, yeah, maybe pick our battle.

**Katya Luscomb:** And focus on the canonical tags.

**Kyle Gaudreau:** Certainly the canonical is like the priority.

**Kyle Gaudreau:** Like that's just like a no-due thing that should be like canonicals are like, you know, very common, less aggressive than the 301 redirect stuff we talked about.

**Kyle Gaudreau:** So there's really should be very little reason to not do them right now, especially with how much deep content we have.

**Katya Luscomb:** That makes sense.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Trying to think through, know I, we're basically at time.

**Erik O'Brien:** My- guess for the next like strategic recommendations, are we planning to propose any like PSEO ideas?

**Erik O'Brien:** Because I know he wants scale faster and that's basically the only way we can get there without him upselling.

**Kyle Gaudreau:** Potentially.

**Kyle Gaudreau:** I mean, it's logically seems like the path to go.

**Kyle Gaudreau:** What that is in particular, I'm not sure at the moment.

**Kyle Gaudreau:** But-

**Kyle Gaudreau:** think some of the things that are actually proposed in the, like, editorial content strategy actually could be, like, there's, like, programmatic versions of those, perhaps.

**Kyle Gaudreau:** So that's part of what I was thinking of just, like, from a time-saving standpoint, because, like, some of the stuff in there seemed to make sense.

**Kyle Gaudreau:** But, yeah, I think that's, the challenge is going to be, like, does he want, do we find ourselves in the situation where we, he expects the same amount of editorial output?

**Kyle Gaudreau:** Plus, PSEO for the same cost.

**Kyle Gaudreau:** And so, you know, depending on where that goes and how we want to handle that, we can maybe pick that up internally and, like, how we want to, you know, it all depends on the level of complexity, I would say, probably.

**Kyle Gaudreau:** There's a, there's a argument to be said of, like, just kind of, like, saving the account, but, I don't know.

**Kyle Gaudreau:** It's kind of a slippery slope with these type of situations.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So, yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** A long way of saying, I'm not 100% sure yet, to be honest.

**Kyle Gaudreau:** I'm still trying to think through it.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I mean, I think it'd be fair just to flat out say, like, we wouldn't do both at the same time.

**Erik O'Brien:** But, like, if you want scale, like, PSEO will get you there faster than five per week editorial.

**Erik O'Brien:** And if we just want to pull the, you know, we're seeing double the conversion rate on the PSEO opportunities that we're doing with Lovable compared to their editorial.

**Erik O'Brien:** So, like, if you want a data point, that's working.

**Kyle Gaudreau:** We just have to prioritize replacing editorial with that for a period of time.

**Kyle Gaudreau:** I worry about there, I mean, that's, I generally like that.

**Kyle Gaudreau:** One thing I worry about there is, like, he hasn't come out and said it, but, you know, we've been working with, given we're not working with Bubble anymore, but, like, you know, we are so loud.

**Erik O'Brien:** on all three at the same time.

**Kyle Gaudreau:** Yeah, well, we're so loud of these things that we're doing for Lovable.

**Kyle Gaudreau:** And then we're not doing this for these other brands.

**Kyle Gaudreau:** Like, how are they going to...

**Erik O'Brien:** Well, they're also paying us significantly more than he is, but...

**Kyle Gaudreau:** Exactly.

**Kyle Gaudreau:** So, like, you know, maybe that's the...

**Kyle Gaudreau:** So anyways, like, I'm not saying that's not something to explore, but, like, that's just the worry I have a little bit in this situation.

**Kyle Gaudreau:** I think it's manageable with the right framing, for sure, to your point.

**Katya Luscomb:** Does that seem like something that would be...

**Katya Luscomb:** Do we want to mention PSEO in today's meeting, since he...

**Katya Luscomb:** I mean, he brought it up on the last call that...

**Kyle Gaudreau:** Did he, though?

**Kyle Gaudreau:** I thought I did.

**Katya Luscomb:** I could be wrong.

**Katya Luscomb:** It came up a couple different times.

**Katya Luscomb:** I think he mentioned that we had said something about PSEO in the strategy sprint and then hadn't actually executed on it, which was, yeah, one of the misses and disconnects on our side.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I think we basically, like, framed it as, like, you know, we'll build your authority.

**Kyle Gaudreau:** We'll tackle PSEO later on when it makes sense.

**Kyle Gaudreau:** What we didn't do is frame it as when does that make sense?

**Katya Luscomb:** When would that happen?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So it's certainly something worth exploring.

**Kyle Gaudreau:** think the thing we'll have to level set with them is those projects do take some time to get off the ground, as you've seen, Erik, with a variety of projects.

**Kyle Gaudreau:** Even if with a lot of urgency, they can take some time and just have a lot of complexity.

**Kyle Gaudreau:** Once they get going, they can move a lot faster in terms of volume output.

**Kyle Gaudreau:** So certainly we can maybe do some of this in parallel potentially, but it wouldn't be like pause editorial this week, next week, and then just all of a sudden we're doing a bunch of PSEO.

**Kyle Gaudreau:** So for whatever reason he starts going that route, we just need to maybe share some examples.

**Kyle Gaudreau:** Like, Erik, this might be...

**Kyle Gaudreau:** Like, that might be an opportunity for us to introduce the things with level one.

**Kyle Gaudreau:** don't know how much you have the details on, like, the evolution of that work.

**Kyle Gaudreau:** But, like, just, like, at a high level speaking to the complexity, because I know that was quite an effort to get off the ground.

**Erik O'Brien:** Yeah, I mean, that was, like, a team of three people full-time for still three to four weeks just to get it in a place where we could hit publish for the first couple.

**Erik O'Brien:** And they were, like, okay, is this good enough?

**Erik O'Brien:** And then now we're going to scale it.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** They started at the same time as a little bit earlier than anything, but we're just now getting to the point where we can scale it effectively.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** For their PSEO?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I mean, it's a super complicated one, like, more complicated than anything that we'd probably do with them.

**Erik O'Brien:** But, yeah.

**Kyle Gaudreau:** Yeah, and that's the thing you want to be careful of.

**Kyle Gaudreau:** It's, like, we don't want to just, like, oh, we'll do the same thing we did with Lovable.

**Erik O'Brien:** You know, I don't think you'll do Yeah, that's where it's, like, we have to have a firewall between teams of, like, we can't.

**Kyle Gaudreau:** Just go and steal ideas of what's working for other people.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Katya Luscomb:** As far as this meeting goes, anything that you guys would flag to add in the agenda currently?

**Katya Luscomb:** And then I guess like thinking through, you know, I'm happy to take lead and by all means, like jump in if there's specifics, figure like migration plan, like if he's got questions, Kyle makes sense there.

**Katya Luscomb:** I'm a little bit worried that he's going to want to just like vent frustration at us again, which seemed like the last call where we ended up so circular.

**Katya Luscomb:** So I like personally, I really want to try and make sure for myself that I'm staying like action oriented in terms of roadmap forward.

**Katya Luscomb:** I don't know if I'll always have like.

**Katya Luscomb:** The answer on exactly what we need to do there, but just trying to call it like for all three of us to try and keep that focus so it's not just event session for him again.

**Kyle Gaudreau:** Yeah, fair.

**Kyle Gaudreau:** I think that makes sense.

**Erik O'Brien:** Yeah, guess frame it as like, you know, we had the conversation last week.

**Erik O'Brien:** We're here to kind of mitigate and respond.

**Erik O'Brien:** So like, want to be very action forward, like you said, Katya, just like, so help us understand like, what's going to help it get back to what you feel is on track, given that you feel like we're behind.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** That makes sense.

**Katya Luscomb:** Yeah, and flag that like, you know, I've got these points that if there's more that he wants to discuss.

**Kyle Gaudreau:** I mean, what is not necessarily in here right now is like, what's active in flight outside of this from like a content perspective, like you kind of call it out.

**Kyle Gaudreau:** Action items a little bit, continue content production, but, you know, I'm not sure exactly where that stands, but, like, you know, the queue for review he may have, what's coming next, like, just making sure that is clear, because we don't want him to just assume, like, that's the only thing that's been worked on, you know, that there's other things happening in parallel, right?

**Kyle Gaudreau:** Like, we're trying to assess is, you know, solidifying the foundation, and then, you know, aligning on the roadmap from here, as we continue to operate, which we are continuing to see some strong signals, right?

**Katya Luscomb:** It's just aligning on where do those signals lead us to, and are we aligned on that?

**Katya Luscomb:** Mm-hmm.

**Katya Luscomb:** Makes sense.

**Katya Luscomb:** Um, yeah, and I can, I can definitely add in, what I wanted to avoid, like, he, he's kind of allergic to the, like, oh, we've got, we've got five articles coming for you again, and we're, we're at that really steady cadence.

**Katya Luscomb:** So I can, maybe I'll just like have a written note in there for visibility, but I don't necessarily want to like, call out.

**Katya Luscomb:** So, but yeah, that's a good call.

**Katya Luscomb:** It doesn't feel like we've just paused on production either.

**Kyle Gaudreau:** Yeah.

**Katya Luscomb:** So.

**Kyle Gaudreau:** I'll let you know if I think of anything else in the interim, but.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And see how it goes.

**Katya Luscomb:** I'll try and channel all my confidence.

**Kyle Gaudreau:** I believe in you.

**Katya Luscomb:** Thanks.

**Katya Luscomb:** Appreciate it guys.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Anything else top of mind before we hop off?

**Katya Luscomb:** I know we went a little over.

**Kyle Gaudreau:** I think just the only thing we haven't really talked about is like, where are the areas that it makes sense to like, just not have like to have Eric have some level of contribution.

**Kyle Gaudreau:** No, want to be careful with that.

**Kyle Gaudreau:** You know, like we don't want to set this expectation that Eric is taking this on.

**Kyle Gaudreau:** Right.

**Erik O'Brien:** But is here for some sort of.

**Erik O'Brien:** here to be like still here.

**Erik O'Brien:** Um, you know, remember when we talked about long-term efforts and this is going to take a while, but it's an investment.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Um, no, I mean, happy to play kind of whatever part, but I think I'm, I'm here to be kind of, uh, just be like, you know, we set the strategy.

**Erik O'Brien:** We've talked through a lot of different things.

**Erik O'Brien:** I don't recall post hog being part of the conversation.

**Erik O'Brien:** I know a lot of different strategy and agencies were all coming in at the same time.

**Erik O'Brien:** So that might've been a conversation you had with somebody else, but, you know, it's our badge for missing it.

**Erik O'Brien:** should have done a deeper dive on that, um, to be able to track against conversions since we know that was a priority.

**Erik O'Brien:** Um, obviously we just had a miss on that one, but, you know, things I can own versus other parts that it's just like, you know, you came into this with ambitions of a long-term program, building SEO foundation, things that we're doing pretty well at.

**Erik O'Brien:** Um, but somehow there was a disconnect on both of our ends of life.

**Erik O'Brien:** Like what.

**Erik O'Brien:** That actually looked like within three to six months.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Makes sense.

**Kyle Gaudreau:** wouldn't get too caught up in like a mea couple or whatever, but, you know, yeah, generally.

**Kyle Gaudreau:** Okay, cool.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** Well, I got to run.

**Kyle Gaudreau:** I'll let you know if I have some additional bright ideas in the meantime.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Sounds good.

**Kyle Gaudreau:** Thank you, guys.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** See ya.
