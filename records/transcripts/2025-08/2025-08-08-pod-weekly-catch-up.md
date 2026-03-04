# Pod weekly catch up

<metadata>
date: 2025-08-08
time: 14:01 UTC
duration: 27 minutes
organizer: Oluwatimilehin Ademosu
participants: Oluwatimilehin Ademosu (GrowthX), Mara Leighton (GrowthX Labs), Nika Narimanidze (GrowthX Labs), Ismail Ajagbe (GrowthX Labs), Vivek Shankar (GrowthX Labs)
fathom_recording_id: 79380909
fathom_url: https://fathom.video/calls/374179579
share_url: https://fathom.video/share/a2TEXcCaE6aWby-CjzxABZ72Nj5EUMTZ
source: fathom
enriched_on: 2026-03-03 14:23 UTC
</metadata>

---

## Summary

The GrowthX Labs pod held a weekly check-in to review progress across multiple client accounts (DataGrid, Galileo, RAMP, Rapid, and Strapi), tracking open tickets and design work while coordinating sprints and dependencies. Key decisions included maintaining Rapid's current combined persona approach rather than fragmenting into multiple personas, escalating the Strapi Octave integration as a priority for immediate quality improvements, and adjusting the RAMP video creation timeline. The team also aligned on leveraging Claude's new project capabilities for centralized content collaboration and clarified assignment brief requirements for a client-facing platform being developed.

---

## Context

GrowthX Labs is the content delivery arm of GrowthX, an AI-driven B2B content marketing agency. This weekly pod meeting brings together the core Labs team—Vivek (technical lead), Mara (leadership), Nika (design and content execution), Ismail (design and implementation), and Timmy (Oluwatimilehin, integration and operations)—to synchronize on concurrent client work. The team manages multiple accounts at different maturity stages: DataGrid and Galileo (established projects moving through publishing automation), RAMP (transitioning to full video-based documentation), Rapid (high-profile account navigating persona specificity challenges), and Strapi (long-tail account dealing with multiple technical debt items). Timmy noted this week was particularly intense with multiple open issues. Nika was recovering from illness but catching up from a café, and Ismail had just returned from a planned absence.

---

## Relevance

**To GrowthX Delivery:**
- Rapid persona consolidation approach (combining 10+ personas into one "least common multiple" persona) is working but creating edge-case issues—team tracking whether fragmentation into specific personas will become necessary
- RAMP video-based documentation workflow requires template refinement; Vivek to adjust templates for partner context before Nika records videos on Monday
- Galileo publishing automation and inline image features in flight; Ismail opening design tickets today
- Strapi facing code formatting dependency issue (tied to Atlas configuration bug) requiring Marcus follow-up; code quality degradation requiring prioritization

**To GrowthX Business Development:**
- Rapid's attention shifted to stablecoin vertical; team flagging need to maintain persona clarity with client as new verticals emerge
- RAMP account moving to more sophisticated video-based delivery model; requires closer collaboration on template design

**To CheckThat / AI Capabilities:**
- Claude's new project capability (centralized artifact creation) enabling more systematic content production workflow
- Potential feature-specific artifact approach being explored for Rapid (prompted by client feedback on feature specificity); Mara investigating whether developing granular prompts for individual features will improve output quality

---

## Overview

- Title/Atlas linking and PSEO template issues in DataGrid; publishing automation and inline image features progressing in Galileo
- RAMP template refinement needed for partner context; design tickets in progress for alternative and overview pages
- Rapid article persona specificity challenges emerging (too narrow on marketplace operations in one piece); team tracking pattern before fragmenting personas
- Strapi code formatting issue blocking progress (Atlas configuration dependency); Octave integration to be prioritized next week
- Claude project capability enabling centralized artifact creation; assignment brief specification project underway

---

## Key Topics

### DataGrid Updates

  - Title field and Atlas linking issue: Kirkland tagged another person to complete the 12-day-old task
  - PSEO pipeline template issue: Kirk responded, Vivek clarified the need to use personal GrowthX accounts for Linear
  - Design ticket opened for RAMP

### Galileo and RAMP Updates

  - Publishing automation ticket in progress
  - Ismail to open design ticket for inline images in Galileo articles
  - RAMP design ticket for alternatives and overview pages pending; Vivek to review templates

### Strapi Updates

  - Four open tickets: staging automation, medium redistribution, octave integration, and code formatting
  - Code formatting issue facing challenges; Marcos working on fixing Atlas code configuration
  - Design updates pending response from KTI

### Claude Upgrade and Content Improvements

  - New Claude upgrade allows for centralized project creation and collaboration
  - Discussion on developing specific artifacts for content features to improve specificity
  - Mara to follow up on details and potential resource needs

### Rapid Account Persona Discussion

  - Debate on updating audience persona document for Rapid
  - Current persona is a combination of multiple target audiences
  - Team to monitor if persona issues become a consistent pattern before considering changes

### Octave Integration for Strapi

  - Timmy emphasized the need for immediate improvements in Strapi articles
  - Mara offered to help prioritize the integration if progress is slow

---

## Action Items

**Vivek Shankar (GrowthX Labs)**
- Review RAMP overview page templates and adjust for partner context; prep revised templates for video creation with Nika by Friday end-of-day
- Open design ticket for Strapi staging automation (in progress with Kirk)

**Nika Narimanidze (GrowthX Labs)**
- Open design ticket for RAMP alternative & "what is" pages (no assignee pre-selected; design team to self-assign)
- Reply under thread re: B2B virtual cards article persona issue for Rapid; tag Ismail and notify team of narrowness concern

**Ismail Ajagbe (GrowthX Labs)**
- Open design ticket today for Rapid inline images feature
- Track article edits related to persona specificity issues for Rapid; monitor whether narrow persona targeting becomes a pattern

**Oluwatimilehin Ademosu (GrowthX)**
- Follow up Monday with Marcus on Strapi code formatting issue (Atlas configuration dependency); confirm timeline
- Track Strapi design Figma update next week (sent to KTI, awaiting response)
- Follow up on Octave integration for Strapi next week; escalate as high priority if no progress by Monday to unlock article quality improvements
- Set reminder for out-of-office week following next week (exam schedule)

**Mara Leighton (GrowthX Labs)**
- Research and follow up on Rapid feature-specific artifacts discussion; dig through Fathom calls to confirm whether proposal is to develop granular prompts for individual features
- Coordinate with team on ideal assignment brief specifications and provide examples to George's platform development team next week
- Monitor Rapid account attention shift to stablecoin vertical; ensure persona clarity maintained with client

---

## Transcript
**Vivek Shankar:** Hey, Nika.

**Nika Narimanidze:** Hi.

**Vivek Shankar:** How's everything?

**Vivek Shankar:** You can hear me, right?

**Oluwatimilehin Ademosu:** Yeah, I can hear you.

**Oluwatimilehin Ademosu:** Yeah, all good, all good.

**Nika Narimanidze:** Thanks for asking.

**Nika Narimanidze:** Hi, Mara.

**Nika Narimanidze:** Hey, guys.

**Nika Narimanidze:** I'm working from a cafe, so apologies if you can hear some background noise, but hopefully not too much.

**Mara Leighton:** It's a nice change from the Air France map.

**Vivek Shankar:** I know I needed the change.

**Vivek Shankar:** How's everyone doing?

**Mara Leighton:** How was the week?

**Mara Leighton:** Um, fine.

**Oluwatimilehin Ademosu:** Good to hear.

**Oluwatimilehin Ademosu:** Glad to hear it.

**Oluwatimilehin Ademosu:** This week has been a lot, actually.

**Oluwatimilehin Ademosu:** But, yeah, fine.

**Nika Narimanidze:** Yeah, congrats, Timmy.

**Nika Narimanidze:** Good to hear that.

**Nika Narimanidze:** I had a short week because of sickness.

**Oluwatimilehin Ademosu:** Glad to hear it.

**Oluwatimilehin Ademosu:** How are you doing, Nika?

**Mara Leighton:** Oh, okay, okay.

**Nika Narimanidze:** Better than on Monday, but in between, I still have microphones, but not now, so that's good.

**Nika Narimanidze:** That's good, yeah.

**Vivek Shankar:** All right, I think we can just go over the linear issues real quick.

**Vivek Shankar:** I know you guys have been filling out updates.

**Vivek Shankar:** I'll start with DataGrid.

**Vivek Shankar:** The first one, the title field and Atlas linking to H1 and Meta.

**Vivek Shankar:** Nika, know you pinged them, today?

**Nika Narimanidze:** Yes, and Kirkland tagged another person and asked to complete this, so I think they will start working on it.

**Nika Narimanidze:** It was created approximately 12 days ago, so I think it's time to handle it.

**Nika Narimanidze:** That's why I pinged him.

**Vivek Shankar:** Okay, the second one, PSEO pipelines not following.

**Vivek Shankar:** Going to the template, Kirk actually responded to you, and I responded back to him just on Linear.

**Vivek Shankar:** I think the issue is you're creating issues in Linear under the team account.

**Vivek Shankar:** So just make sure you're logging in with your own GrowthX account.

**Vivek Shankar:** Okay.

**Nika Narimanidze:** I meant that ticket when I said that Kirk has replied for PSO.

**Nika Narimanidze:** Really?

**Vivek Shankar:** I thought it was for something else, actually.

**Vivek Shankar:** It was the...

**Vivek Shankar:** No, I don't think you've checked it, Nika.

**Vivek Shankar:** He responded just a couple of hours ago.

**Vivek Shankar:** He hasn't assigned it to anybody.

**Nika Narimanidze:** Just a sec.

**Nika Narimanidze:** Cursor, can you add this additional mapping to the DataGrid Webflow publishing workflow?

**Nika Narimanidze:** Cursor is an app.

**Nika Narimanidze:** So it's not a person, sorry.

**Nika Narimanidze:** Uh...

**Nika Narimanidze:** And yeah, my ticket was about the Atlas publishing that has the same H1 and Meta title, yes.

**Vivek Shankar:** No, I'm talking about the second issue, the PSEO, where it's not following the template.

**Vivek Shankar:** It still mentions task in the title.

**Nika Narimanidze:** Yeah, yeah, yeah, yeah, yeah.

**Vivek Shankar:** So for that one, yeah, that one he responded a couple hours ago, and then I responded back to him.

**Vivek Shankar:** He just needs to see the template.

**Vivek Shankar:** He had some questions about what Atlas meant.

**Vivek Shankar:** So yeah, that's it.

**Vivek Shankar:** You had the design ticket as well.

**Vivek Shankar:** saw you just opened it, but that was for RAMP.

**Vivek Shankar:** Sorry, my bad.

**Vivek Shankar:** Anything else for DataGrid?

**Vivek Shankar:** think that's it, right?

**Vivek Shankar:** No, not for DataGrid.

**Vivek Shankar:** That's all.

**Nika Narimanidze:** Okay, cool.

**Vivek Shankar:** Ismail, was there anything for Galileo?

**Ismail Ajagbe:** So yeah, we had one for the publishing automation, and I think before the end of the day today, I want to open a design ticket for the inline images for Galileo articles.

**Ismail Ajagbe:** Okay, cool.

**Vivek Shankar:** Yeah, so you can just, yeah, just follow up on that, and then on Monday, just drop a thread with the updates or whatever.

**Vivek Shankar:** And then I'm going to open a ticket for Slamas Publishing as well.

**Vivek Shankar:** Yes, we don't need to add the publishing ones, those are like daily, so it's not much of an issue.

**Vivek Shankar:** All right, on RAMP, so we have that big one that got cleared.

**Vivek Shankar:** I saw the design thing, we need to do the alternative and what is it?

**Nika Narimanidze:** We need to record the video to explain how the publishing of versus and alternative pages work.

**Nika Narimanidze:** Before that, for the design tickets, who should be the assignee?

**Nika Narimanidze:** Just asking because it's a design-related thing.

**Nika Narimanidze:** Is it still Marcus?

**Vivek Shankar:** No, I don't think we assign anybody.

**Vivek Shankar:** They sort of look at it and they assign it themselves.

**Vivek Shankar:** Okay, yeah, correct.

**Nika Narimanidze:** And Vivek, about the videos that you mentioned, what's the deadline for creating this Monday, today?

**Nika Narimanidze:** You can do it on Monday.

**Vivek Shankar:** The reason I delayed it is because I want to look at the templates.

**Vivek Shankar:** And because he was having issues with the template that we gave him for the overview pages, he wasn't understanding where the data was coming from.

**Vivek Shankar:** Obviously, because we created it for the freelancers, not for partners.

**Vivek Shankar:** I'm seeing if we can maybe change that a little bit.

**Vivek Shankar:** So I'll do that today.

**Vivek Shankar:** And by Monday, so we can, I'll bring you once it's done, and then we can get it.

**Vivek Shankar:** Yeah, okay.

**Vivek Shankar:** Sure, clear.

**Nika Narimanidze:** All right, cool.

**Vivek Shankar:** Now for Rapid, Ismail, I think the main issue was the inline images, right?

**Ismail Ajagbe:** Yeah, that was the image.

**Vivek Shankar:** Okay, I'm going to open that design ticket today for the inline images.

**Vivek Shankar:** Nika also opened a ticket for internal linking flow issues.

**Vivek Shankar:** Now Strapi. Let's go through those open tickets.

**Oluwatimilehin Ademosu:** So we have four tickets open: staging automation, medium redistribution, Octave integration, and code formatting. For staging automation, Kirk is working on that with CMS changes. For the medium redistribution, I'm checking on updates by next week. For the code formatting issue, we've been having trouble because Marcus said it was fixed earlier this week, but testing showed it wasn't fixed. He then said it's actually a general Atlas code configuration issue, which is a dependency on something else. We should follow up with Marcus on Monday to understand the timeline better.

**Vivek Shankar:** Okay, so there's a dependency issue. Let's tag Marcus to follow up on that Monday. And we had a design thing as well?

**Oluwatimilehin Ademosu:** Yeah, we sent the Figma update for that. KTI is looking at it, awaiting her response.

**Vivek Shankar:** Okay, track that for next week. If she doesn't respond, we can ping her.

**Oluwatimilehin Ademosu:** For the Octave integration, I'd like to see some immediate improvements in the Strapi articles soon.

**Vivek Shankar:** Yeah, let's prioritize that. I think we've covered all the accounts now.

**Mara Leighton:** One thing I wanted to add: we got the upgrade for Claude, so we can now create projects and have everything centralized. All of you are using Claude anyway to add the natural language element and final polish on articles, but now it's more systemic and easier for everyone. Let me know if you have any questions.

**Mara Leighton:** And the other thing I wanted to follow up on: I know we discussed in the Rapid call potentially having artifacts for specific features. Are we pursuing that actively? Do we need resources from them on that?

**Vivek Shankar:** Which features are we talking about?

**Mara Leighton:** I think it was mentioned in a Rapid call—there were particular features that they thought lacked specificity sometimes, and they were wondering if developing specific artifacts might help. I can hunt down the call and follow up.

**Vivek Shankar:** It sounds like it was Rapid. I can also go through the Fathom calls to confirm.

**Mara Leighton:** Yeah, I'll do some digging and follow up next week. I think it's a half-baked idea, but I want to make sure we explore it if it will actually improve the content.

**Oluwatimilehin Ademosu:** Timmy here—I wanted to ask about your call with George. Do you have clarity on what he's looking for?

**Mara Leighton:** So George is building a content inventory platform that scans pages to identify opportunities—keywords, new content topics, SEO tweaks. The platform would then automatically generate an assignment brief for someone to polish. He's asking two things: What makes an ideal assignment brief? And what does an ideal first generated draft look like? I think the assignment brief spec is the more universal question—the draft question is more client-dependent. So I'd love your thoughts on what an ideal assignment brief looks like, and I'll share it with him.

**Vivek Shankar:** This sounds a lot like what SEMrush does. That's the main thing I'm thinking—he might be recreating SEMrush's capability here.

**Mara Leighton:** That's a good point. I'll ask him if I've understood correctly. But if you all have examples of really good assignment briefs or strong thoughts on what makes one work, feel free to share and I can pass them along.

**Vivek Shankar:** That was pretty much all I had from my end. Floor is open—anyone have blockers or other things to cover?

**Vivek Shankar:** I can see Nika wants to say something.

**Nika Narimanidze:** Yeah, I wanted to ask about the Rapid audience personas. Are we updating the persona document? We had a case where the audience wasn't clear—payment operations leader vs. marketplace operations vs. payment professionals—and I wanted to understand if we're fragmenting into more personas.

**Vivek Shankar:** I brought this up with them a couple weeks ago. They have 10 different personas and 15 verticals, so it's all over the place. If we add all of those, nothing gets taken into account. So what we decided is to keep the current persona, which is a combination of everything they're looking for—the least common multiple. It tends to hit everything, but we'll occasionally get edge cases where we need to be more general. The article you mentioned was an edge case, and we just deal with those as they come.

**Nika Narimanidze:** I had replied under two articles. There's another article issue—the B2B virtual cards article was too specific on marketplace operations. The client said B2B cards aren't relevant for them, so they want to cancel that section. The problem is we were too narrow because we gave the audience persona to Claude and it chose that narrow marketplace angle. So I'll reply in the thread and notify the team.

**Vivek Shankar:** Okay, can you tag Ismail on that as well?

**Nika Narimanidze:** Yeah, of course.

**Vivek Shankar:** And we need to track if this is becoming a pattern. If it's happening a lot, we need another conversation with them about who exactly they want to target.

**Vivek Shankar:** All right.

**Mara Leighton:** Would it be feasible to flesh out those artifacts and then call a specific one to isolate in the workflow? Would that be worth the uplift?

**Vivek Shankar:** The issue is that for each article, we'd need to map which persona we want to target. From what they said, there are a lot of personas. So it might not be worth it.

**Mara Leighton:** Right. Let's keep an eye on it and if it becomes a consistent pattern, maybe that's the next step. Ideally, we'd auto-apply the generalized persona and then manually override when needed.

**Vivek Shankar:** We can do that now by manually overriding in the assignment brief. We've done it a few times. The main issue is Rapid needs to tell us which three or four personas to target, or else we're asking for each article which one to focus on.

**Nika Narimanidze:** Interestingly, the general article got approved, so maybe going too narrow is the bigger problem.

**Mara Leighton:** Yeah, there's a lot happening in parallel. Let's add this to next week's agenda and check in on what Rapid's thinking is. They've been focusing on stablecoin, but we still need to solidify the personas with them.

**Vivek Shankar:** Ismail, can you keep track of these persona issues in the article edits and we'll add that to the agenda as well?

**Oluwatimilehin Ademosu:** One last thing: I'm not sure how long the Octave integration will take, but it would be nice to see some immediate improvements in the Strapi articles.

**Mara Leighton:** Next week, if there isn't much progress on that ticket, feel free to mark it as higher priority or ping me and I can message Andy to get it prioritized.

**Oluwatimilehin Ademosu:** Also, if I'm not reminded about my out-of-office the week after next for my exams, please remind me Monday.

**Mara Leighton:** Does anyone else have anything? Nika, tell us about your vacation!

**Nika Narimanidze:** I'm going to the seaside in Georgia first—it's good for kids' health with the mineral content—then Abu Dhabi and Cyprus. I'm taking my four-year-old daughter.

**Mara Leighton:** That sounds wonderful. Have a great time, and feel free to share photos!

**Vivek Shankar:** Ismail, welcome back! We're happy to have you back on the team.

**Mara Leighton:** Thanks everyone for the great work this week. Enjoy your weekend!

**Vivek Shankar:** Bye, everyone!

**Oluwatimilehin Ademosu:** Bye.
