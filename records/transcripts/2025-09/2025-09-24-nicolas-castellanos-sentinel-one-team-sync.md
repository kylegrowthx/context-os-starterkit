# Nicolas Castellanos / Sentinel One Team - Sync

<metadata>
date: 2025-09-24
time: 16:02 UTC
duration: 10 minutes
organizer: team@growthxlabs.com
participants: Nicolas Castellanos (GrowthX), John Nederveld (SentinelOne), Joery van Druten (SentinelOne), Ankit Pahuja (SentinelOne)
fathom_recording_id: 89529327
fathom_url: https://fathom.video/calls/418855633
share_url: https://fathom.video/share/uhE5DPaRFPjPf4sF9x9PtzrTA6cCjDEB
source: fathom
enriched_on: 2026-03-03 02:30 UTC
</metadata>

---

## Summary

GrowthX frontend developer Nicolas Castellanos synced with the SentinelOne team on CVE database implementation, focusing on frontend development, GitHub access onboarding, and integration points with SentinelOne's Search, SEO components, and sitemaps. The project is targeting go-live in the 3rd week of October 2025 — about 2 weeks after SentinelOne's October 7th release. John Nederveld will request GitHub access for Nicolas today, and designs are nearly complete pending review with George.

---

## Context

SentinelOne is building a CVE (Common Vulnerabilities and Exposures) database platform with GrowthX supporting frontend development and content strategy. Nicolas Castellanos, a frontend developer from GrowthX, is joining the project to build the frontend for the CVE database using a Next.js codebase with Tailwind CSS. The SentinelOne team (Joery van Druten, John Nederveld, and Ankit Pahuja) are responsible for backend work, search infrastructure (Algolia), and SEO components. Ankit mentioned that GrowthX leadership (Aida and George) approved the project timeline in a separate meeting, setting the tentative go-live date for the 3rd week of October 2025. The meeting was called to clarify dependencies and unblock Nicolas's onboarding so he can start frontend development efficiently.

---

## Relevance

**To GrowthX Delivery:**
- New client engagement: GrowthX has a services commitment with SentinelOne for CVE database frontend development, targeting Oct 15-22, 2025 go-live.
- Frontend architecture: SentinelOne uses a Next.js + Tailwind CSS stack with custom components (no component libraries). GrowthX team needs to align on component patterns and reusability with SentinelOne's existing codebase.
- ContentStack integration: Nicolas planning to use ContentStack's JSON RTE field with custom components (e.g., timeline), requiring coordination with SentinelOne on content modeling.

**To CheckThat:**
- No direct CheckThat involvement mentioned; however, SEO components are a shared consideration for the CVE database platform, touching on content visibility and AI-driven search.

**To GrowthX Business Development:**
- Strong early signal on project execution: GrowthX leadership (Aida and George) already approved timeline and milestones, indicating good relationship momentum with SentinelOne.
- Account expansion opportunity: If CVE database goes well, potential for additional content strategy or AI visibility work on the security/compliance side of SentinelOne's platform.

---

## Overview

- Nicolas (GrowthX) needs GitHub access to start frontend work; John to initiate request
- Project timeline: aiming for go-live \~3rd week of October (post-SentinelOne's Oct 7 release)
- Designs near completion; Nicolas meeting George tomorrow to finalize filters and small changes
- ContentStack setup: using JSON RTE field for custom components; Algolia integration planned

---

## Key Topics

### ContentStack Implementation

  - Nicolas explored ContentStack, planning custom types + JSON RTE for body content
  - Custom components (e.g., timeline) to be embedded in JSON RTE field
  - SEO components likely part of ContentStack; pipeline needed to generate SEO tags/info

### Frontend Development

  - Next.js codebase with Tailwind CSS for styling
  - No component libraries used; mix of existing and new custom components
  - Nicolas needs repo access to leverage existing components/styles
  - John to set up directory for Nicolas to work in

### Project Timeline and Dependencies

  - SentinelOne releasing on October 7th
  - CVE database implementation targeted for \~2 weeks post-release
  - Tentative go-live set for 3rd week of October (per Ankit's meeting with Aida/George)

### Design Status

  - Designs near completion with only small changes pending
  - Nicolas meeting George tomorrow to discuss filters and finalize details
  - Marisol provided mandatory filter requirements; review needed

### Access and Onboarding

  - John initiating GitHub access request for Nicolas today
  - Additional team member access may take 1-2 weeks due to onboarding process
  - Decision to prioritize Nicolas' access, then address other team member

### Integration Considerations

  - Search functionality using Algolia
  - SEO components and sitemaps in development by SentinelOne team
  - Need to avoid redundant components while allowing independent work

---

## Action Items

**John Nederveld (SentinelOne)**
- Request GitHub access for Nicolas Castellanos via IT. Set up directory for Nicolas to work in.
- Prepare documentation on search (Algolia), SEO components, and sitemaps for Nicolas to understand integration points for CVE database work.

**Nicolas Castellanos (GrowthX)**
- Provide names of additional GrowthX team members needing GitHub access to Joery/John today or tomorrow. Note: Onboarding may take 1-2 weeks for team members without SentinelOne email addresses.

---

## Transcript
**Joery van Druten:** We are doing a lot of things.

**Joery van Druten:** This meeting is being recorded.

**Joery van Druten:** So we are doing a lot of things.

**Joery van Druten:** For instance, we're going to implement Algolia Search.

**Joery van Druten:** And then I was like, yes, also the CVE database is going to make use of Algolia.

**Joery van Druten:** Then we have a big thing for us.

**Joery van Druten:** It's like sitemaps that we're also not working on.

**Joery van Druten:** So there are some dependencies that we would like to know like where are you, what is your plan, what are you going to work on so that we also can help you out and keep you in the loop of like, hey, when you do the search, this is where it is.

**Joery van Druten:** And then John can probably do a better job than I do.

**Joery van Druten:** And same thing with sitemaps.

**Joery van Druten:** We're working on some SEO components.

**Joery van Druten:** Yeah, so there will be some dependencies.

**Joery van Druten:** And like I said, for us, we are now one sprint away for the first release.

**Joery van Druten:** So we wanted to get a better feel of like.

**Joery van Druten:** Do you need any help from us?

**Joery van Druten:** How close are you to actually start working in ContentStack?

**Nicolas Castellanos:** I was looking at ContentStack last week.

**Nicolas Castellanos:** I got access to your ContentStack.

**Nicolas Castellanos:** And I was thinking how to build this new ContentType.

**Nicolas Castellanos:** What I got was a few custom types.

**Nicolas Castellanos:** And then for the body of the page, ContentStack has like a RTE — I think a JSON RTE type, which is JSON-based.

**Nicolas Castellanos:** And inside that, you can have like embed custom stuff.

**Nicolas Castellanos:** So I was thinking of using that to embed some of the custom stuff we might have, like the timeline we have.

**Nicolas Castellanos:** I don't know if you saw the designs already.

**Joery van Druten:** I've seen some designs, yeah.

**Joery van Druten:** Yeah, they were not, yeah, they were not too complicated.

**Joery van Druten:** Well, you're going to build.

**Nicolas Castellanos:** I'll build them out, so I'm not too worried about complexity.

**Nicolas Castellanos:** For custom components that will go on the body, I was thinking of building that using that JSON RTE field, and then integrating the search fields and filters with Algolia after that's done.

**Nicolas Castellanos:** I didn't think about SEO, but if you're adding SEO components, I think that's part of a content type, of content stack, something like that.

**Nicolas Castellanos:** Then, if that's the case, then we can have our pipeline to generate those SEO tags and that information to get into that too.

**Nicolas Castellanos:** So yeah, we can do that.

**Nicolas Castellanos:** And yeah, the main question I have is, where do I write that frontend?

**Nicolas Castellanos:** I'm guessing I'm going to get access to a GitHub or something.

**John Nederveld:** Well, yeah, it would have to be in the code base.

**John Nederveld:** Yeah, yeah, we'll have to work through some red tape, so I'll put in a request with IT to onboard Nicolas to our repository, and then we'll set up a directory that you can work in.

**Joery van Druten:** Is there anyone else besides you we need to add?

**Nicolas Castellanos:** We might, yes, but I'll get that to you either today or tomorrow.

**John Nederveld:** Yeah.

**Joery van Druten:** But you're not locked, because you just work on your local, you're not blocked with anything?

**Nicolas Castellanos:** No, but if there's stuff you already have, I'm going to need access to that to start. Like you said, that's a Next.js codebase. So I'm thinking there's some components and styles I'm going to have to reuse from there.

**John Nederveld:** Yeah.

**John Nederveld:** There are likely some components that you'll need to use, then you'll have to create some as well.

**John Nederveld:** We're not using any component libraries at the moment.

**John Nederveld:** We're just creating our own as we go.

**Nicolas Castellanos:** You're using Tailwind or something like that?

**John Nederveld:** Yeah, we're using Tailwind.

**John Nederveld:** Yeah, we are using Tailwind for our styles.

**Nicolas Castellanos:** Awesome.

**John Nederveld:** Yeah.

**Nicolas Castellanos:** Yeah, that's great.

**Nicolas Castellanos:** And then we're going to have all the generation pipeline that runs on our own.

**Nicolas Castellanos:** So I'm not blocked by that.

**Nicolas Castellanos:** And then if you're saying you're releasing October 7th, that makes sense for timing. So this will go about a couple of weeks after that?

**Joery van Druten:** That's fine.

**Nicolas Castellanos:** Okay.

**Nicolas Castellanos:** Cool.

**Joery van Druten:** Yeah, no, it's even better because we will be busy.

**Nicolas Castellanos:** Cool.

**Nicolas Castellanos:** So I'm guessing this will go through a review process and everything. I'll send pull requests through GitHub, and we'll have code reviews to make sure everything aligns.

**Ankit Pahuja:** Yeah, just to set the tone and expectation, right?

**Ankit Pahuja:** So I was, I did meet Aida and George a couple of hours back from the GrowthX team and we were discussing the timelines for the project.

**Ankit Pahuja:** We're targeting the third week of October for go-live. And I mean, this is more up for discussion, but this is the timeline we're looking at right now.

**Nicolas Castellanos:** Yeah, yeah, yeah, that makes sense.

**Nicolas Castellanos:** Yeah, that's good.

**Nicolas Castellanos:** Cool.

**Ankit Pahuja:** And also one outcome from the meeting was that the designs are near completion.

**Nicolas Castellanos:** I think it's just really small changes. I'm meeting with George tomorrow to discuss that and also review the filters and other details.

**Nicolas Castellanos:** So yeah, we are on track.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** And if you need anything in terms of filters for content and what types of filters we want, just reach out — Marisol from my team and I can help provide more context.

**Nicolas Castellanos:** Yeah, I think it was Marisol who sent me a few of the mandatory stuff we want in there.

**Nicolas Castellanos:** I'll review the designs with George tomorrow and see if we need anything else besides Marisol's mandatory requirements.

**Ankit Pahuja:** Alright.

**Nicolas Castellanos:** Cool.

**Nicolas Castellanos:** So yeah, I'll be waiting for access to GitHub and will post updates on progress.

**Joery van Druten:** Yeah, we will put in a request today.

**John Nederveld:** Yeah.

**Joery van Druten:** At least for you, and then let us know as soon as possible on the person.

**Joery van Druten:** But now that I think about it, if the other person doesn't have a SentinelOne email address, we have to go through the whole onboarding process.

**Nicolas Castellanos:** Yeah, true.

**Nicolas Castellanos:** Okay.

**Nicolas Castellanos:** Yeah.

**Joery van Druten:** Fun times.

**Nicolas Castellanos:** That's probably a week, right?

**Joery van Druten:** Yeah.

**Nicolas Castellanos:** Yeah, okay.

**Nicolas Castellanos:** I'll keep that in mind.

**Joery van Druten:** Yep.

**Joery van Druten:** Yeah, it could take up to two weeks, depending on when we submit the request.

**John Nederveld:** Right, yeah.

**Joery van Druten:** But yeah, let's move forward, John.

**Joery van Druten:** Let's do Nicolas first so that we don't, yeah, and then we will see how fast we can onboard the other team member.

**John Nederveld:** Yeah.

**Joery van Druten:** Cool.

**Joery van Druten:** All right.

**Joery van Druten:** Yeah, and also for you, John, let's prepare a couple of things, right?

**Joery van Druten:** Because we have the search, we have the SEO component, we have sitemaps to see, like, what we need to think about, like, because I want them to be able to work as independent as possible, but I don't want to have, like, redundant components and whatnot.

**Nicolas Castellanos:** Yeah, let me think about that. First, I'll make sure to send all the UI components and styles, and once you have those, send them to me. I'll make adjustments to ensure we also handle sitemaps and SEO data integration properly.

**Joery van Druten:** Cool.

**Joery van Druten:** All right.

**Joery van Druten:** Thank you.

**Nicolas Castellanos:** Thank you.

**Joery van Druten:** Bye.
