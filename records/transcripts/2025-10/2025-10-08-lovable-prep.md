# Lovable Prep

<metadata>
date: 2025-10-08
time: 15:36 UTC
duration: 26 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, George Haikal, Georgemaine Lourens, Nicolas Castellanos
fathom_recording_id: 92745458
fathom_url: https://fathom.video/calls/435902548
share_url: https://fathom.video/share/vWSe7ZDXRLyLA3xcbHBUCZtoDdZX7o2f
source: fathom
enriched_on: 2026-03-02 01:15 UTC
</metadata>

---

## Summary

The team clarified the scope and direction of the Lovable template library after a week of confusion around which version to build. With four weeks remaining, they decided to prioritize launching a functional template gallery MVP over perfecting individual templates—focusing on getting a working experience deployed rather than meeting Sebastian's higher quality bar. Cece (head of marketing) has superseded Sebastian's feedback and supports the team's MVP-first approach, meaning they can move forward with Nico's existing render preview and adapt Georgemaine's design work into it, shipping the gallery within 3.5 weeks with a weekly check-in cadence to avoid future misalignment.

---

## Context

The Lovable template library is a critical deliverable for the client within an eight-week engagement with only four weeks remaining. GrowthX is building a gallery experience that showcases construction and home services website templates, optimized for SEO queries like "construction website examples." Marcel created an initial prototype that was validated by Rachel (client-side) and Cece (head of marketing). However, after a week of parallel work, three different versions existed: Marcel's original prototype, Nicolas's render preview with login functionality, and Georgemaine's new Figma designs and Origami prototype. The team confused the client about what had been shown and aligned on. This meeting resolved the confusion: with four weeks left to deliver, shipping a working gallery MVP is more important than achieving Sebastian's (quality reviewer's) perfectionist bar.

---

## Relevance

- **To GrowthX Delivery:** Critical process alignment issue—lacked clear communication on which version was shared with the client, leading to a week of wasted parallel work. Need weekly 15-minute check-ins to prevent future divergence. Learned that weekly sync cadence is essential on complex, multi-team projects.

- **To GrowthX Business Development:** Cece has superseded Sebastian's feedback, removing a key blocker and empowering the team to ship. This signals strong account health and trust at the decision-maker level. Timeline is tight (3.5 weeks to delivery), so shipping an imperfect MVP is better than missing the deadline and losing the client entirely.

- **To CheckThat / AEO:** The gallery is being optimized for SEO keywords like "construction website examples" using filter landing pages. This is a concrete example of CheckThat visibility strategy in production.

---

## Overview

- Critical communication breakdown: Three versions existed (Marcel's prototype, Nico's render preview, Georgemaine's Figma designs) with no shared links to track progress, leaving Marcel (CEO) unable to brief the broader team
- Decision made: Prioritize the working gallery MVP (4-week deadline) over template perfection—ship what works, improve iteratively after launch
- Team will adapt Georgemaine's design work into Nico's existing render preview, incorporating Lovable branding elements (colors, fonts) as post-MVP improvements
- Cece (head of marketing) has superseded Sebastian's quality concerns, clearing the path for MVP-first approach and reducing decision-making overhead

---

## Key Topics

### Project Status and Confusion

  - Multiple versions exist: Marcel's prototype, Nico's render preview, Georgemaine's Figma/Origami designs
  - Lack of clear communication on what was shown to the client (Felix/Sebastian)
  - Uncertainty about which version to proceed with and show to the client

### Prioritizing MVP Launch

  - 4 weeks remaining before potential project end
  - Need to show tangible progress to the client immediately
  - Focus on launching a functional template gallery, even if not perfect
  - Emphasis on having something deployable over perfecting individual templates

### Template Quality Concerns

  - Sebastian (client-side) raised concerns about template quality
  - Team decides to proceed with gallery development, addressing template quality iteratively
  - Cece (client-side) supports the team's direction, bypassing Sebastian's feedback

### Technical Approach

  - Nicolas has a working render preview (on Render.com) with email/password login functionality already implemented
  - Georgemaine created designs in Figma and interactive prototypes in Origami (not code—a quick prototyping tool)
  - Decision: Adapt Georgemaine's Figma designs into Nicolas's existing render preview rather than rebuilding from scratch
  - Plan to improve look and feel and incorporate Lovable branding (colors, fonts) after initial launch
  - Key insight: Lovable's import functionality and design tool are limited compared to alternatives like Bolt, so templates may require manual bytecoding to achieve quality results

### SEO Considerations

  - Goal to optimize for search queries like "construction website examples"
  - Focus on creating filter landing pages similar to competitors (e.g., Wix)

---

## Action Items

**George Haikal (GrowthX)**
- Schedule 15-minute weekly check-in with Marcel, Georgemaine, and Nicolas to track Lovable template gallery progress and prevent future communication breakdowns

**Georgemaine Lourens**
- Create and post a screen recording of the Origami prototype of the template gallery in the project Slack channel for async review

**Nicolas Castellanos**
- Share the link to the Render preview of the template gallery in Slack
- Update the existing render preview prototype to incorporate Lovable branding elements (colors and fonts)

**Marcel Santilli (GrowthX)**
- Clear calendar to dedicate time to the follow-up discussion and hands-on work on the template gallery implementation

---

## Transcript
**Marcel Santilli:** How's it going?

**Marcel Santilli:** I was just wrapping up the stand-up for the team.

**George Haikal:** No problem.

**Marcel Santilli:** How's that go?

**Marcel Santilli:** And how are feeling about lovable overall?

**George Haikal:** Good.

**George Haikal:** I feel good.

**George Haikal:** I think the main thing I need from you is, and if it isn't there, it's fine, but any progress made on the template that you were vibe coding with Daniel.

**George Haikal:** We can even just add whatever you have and you can speak to it and run through it.

**Marcel Santilli:** Yeah, like, I think George was working on something, too.

**Marcel Santilli:** I saw it on the project channel.

**George Haikal:** I haven't looked at it yet. Yeah, I added it.

**George Haikal:** That was more for the blog.

**George Haikal:** So we added that.

**George Haikal:** So, like, the blog page and structure to be one of that is done.

**George Haikal:** Oh, the structure of the blog you're seeing.

**George Haikal:** Yeah, like, yeah, like, if we want to post a ton of editorial.

**Marcel Santilli:** This doesn't look good at all for what was just for the blog.

**Marcel Santilli:** It doesn't look like them.

**Marcel Santilli:** I'm not following.

**George Haikal:** Yeah, I mean, it wasn't the best.

**Marcel Santilli:** Yeah, I looked at it. Wait, we're going to show them this and say that's what their blog is going to look like?

**George Haikal:** That's the V1 that he sent, and he said it's very early, so he wasn't even expecting probably to show it to them.

**Marcel Santilli:** Yeah, this is awful. It's not on their brand.

**George Haikal:** No, I think he did it very quickly because what he was doing before was the experience from the template experience all the way down to the individual template.

**Marcel Santilli:** That's all in the Figma. Lovable is garbage for building a lot of things.

**Marcel Santilli:** There's no reason for blogging used to be in Lovable.

**George Haikal:** I'm not partial to Lovable, but I don't know where else he prefers doing it.

**Marcel Santilli:** Like, there's so many blog templates out there that we can just use and then get it to make it look better.

**Marcel Santilli:** Yeah, this is one of the examples I have, but it's still using Lovable, but it breaks a lot of things, you know?

**George Haikal:** Mm-hmm.

**Marcel Santilli:** But it's an example of a single page, you can kind of see it's missing some things—Lovable just sucks. It just is not good at all.

**Marcel Santilli:** Like, essentially, if you don't start with lovable and you try to import a design, it just gets so many things wrong and every other service gets it right in, like, one shot.

**George Haikal:** Yeah.

**George Haikal:** It's way better, you know?

**Marcel Santilli:** By the way, did they give us credit?

**George Haikal:** Yep, yep.

**George Haikal:** So, Estaval, they just juiced up his existing account with a ton of credit, and he added all of us as users.

**George Haikal:** I'll make sure you're on that as well.

**Marcel Santilli:** It should already be, but.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah, like, I guess, I guess I'm kind of confused with Georgemaine.

**George Haikal:** Me too, and he, I mean, he is too.

**George Haikal:** Like, he stopped when the confusion happened yesterday with Sebastian and Cece.

**George Haikal:** Cece's checking with Rachel.

**George Haikal:** They're on our side, right?

**George Haikal:** So then when you and Daniel were talking, he was trying to figure out.

**Marcel Santilli:** I've been asking for, like, where, what did we share with Sebastian?

**Marcel Santilli:** Because, like, I don't have a link at all.

**Marcel Santilli:** And, like, I, and then I look at the project channel, and there's not a single link to the preview of it.

**Marcel Santilli:** So I'm like, what is the exact thing that's been built so far?

**Marcel Santilli:** And if it's worse than what I had already prototyped?

**Marcel Santilli:** It's like really annoying that we're regressing and spend like two weeks, essentially, like instead of taking a prototype that was already kind of somewhat working to just work, aka like there's this link that like in here from earlier version that Nico had done, but then the designs from Georgemaine were so different.

**Marcel Santilli:** And then Tuesday last week, so that's like nine days ago, he posted a progress update on lovable templates.

**Marcel Santilli:** And then like, there's been not a single link.

**Marcel Santilli:** So I'm like, where is the latest templates like to show what we've done in the last 10 days, essentially, right?

**Marcel Santilli:** Like this is the hype for him.

**Marcel Santilli:** So I'm like, is there a link somewhere?

**Marcel Santilli:** It's like, what is the point of having like a project channel if like we're not posting  for people like me to read?

**George Haikal:** There's a meeting I have with Felix, and I have the link. I'm sending it right now—it's what Georgemaine showed Felix on the template UI.

**Marcel Santilli:** I don't need a Figma.

**Marcel Santilli:** We had a working prototype.

**Marcel Santilli:** I'm super confused as to what is the working site.

**Marcel Santilli:** If we had a working prototype that I created, and then Nico had created a version that just worked, and then we're all of a sudden showing a Figma file instead of a working version that was already working that was already very close to the final thing.

**Marcel Santilli:** I'm very confused.

**Marcel Santilli:** Like, where are we? And what are George and I doing exactly?

**Marcel Santilli:** Because I don't understand.

**George Haikal:** Yeah, let me get it like right now.

**Marcel Santilli:** Because I had to update the whole strategy sprint team today on what's happening with Lovable, but I didn't have all the information and there was no updates there.

**Marcel Santilli:** And then I go into the project channels and I don't see any updates either on like, so I'm like, who's doing what?

**Marcel Santilli:** Like, I'm very confused and who's managing this?

**Marcel Santilli:** Like.

**Marcel Santilli:** Like, you know, sorry, I don't mean to sound frustrated.

**Marcel Santilli:** No, you're good.

**Marcel Santilli:** Like, why are we overcomplicating this?

**Marcel Santilli:** Like, we had a thing that was working.

**George Haikal:** I hear you.

**George Haikal:** It's not overcomplicating. Georgemaine is sending me the link right now, and we're going to be in a good spot for it. Once she sends it, I can show it to you.

**George Haikal:** Do you want to just run through the rest of this so you're ready to speak on it all?

**Marcel Santilli:** Yeah, that sounds good.

**Marcel Santilli:** But just so I understand, like, what did we show Sebastian?

**Marcel Santilli:** I'm very confused.

**Marcel Santilli:** Like, I have no idea what we showed him.

**George Haikal:** It was the...

**Marcel Santilli:** Who showed what to whom?

**Marcel Santilli:** Like, I'm like, there's a link that Nico built.

**George Haikal:** It was just an expansion of what you had already built. Like the V1 prototype—Nicolas took that and expanded on it.

**Marcel Santilli:** What I built looks extremely different from what this is—which is fine if this is done and built, but what is this?

**Marcel Santilli:** Is this a Figma or is this a working thing?

**Marcel Santilli:** Like, I'm kind of confused.

**Marcel Santilli:** Like, is this what we showed, Sebastian?

**George Haikal:** No, what we showed—and it was to Felix, who's the designer—is the prototype that you built.

**George Haikal:** We showed both of them. The first one was the template that you built, and then the second thing is what Georgemaine sent in the chat.

**Marcel Santilli:** Wait, I don't see a link. What are we talking about?

**George Haikal:** Scroll up to where you were, all the way up, to where the on-brand stuff is.

**Marcel Santilli:** Yes.

**Marcel Santilli:** It's just a vague.

**Marcel Santilli:** There's no links.

**Marcel Santilli:** Okay.

**Marcel Santilli:** I'm very confused.

**Marcel Santilli:** Why are we presenting two options to the client?

**Marcel Santilli:** Like, who's making the decision that what we prototyped and people are mostly happy with is not good enough, that we need to design a completely new experience and get approval on something, and then bait and switch them to something else? Who is deciding that that's what we need to do?

**George Haikal:** And that's the part.

**George Haikal:** Yep.

**George Haikal:** We don't need to bait and switch them.

**George Haikal:** And we do need to decide.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Can George and Nico join?

**Marcel Santilli:** Because I'm just confused.

**Marcel Santilli:** Like, if I'm confused, I can't communicate with confidence.

**Marcel Santilli:** Because, like, I have no idea what we show them.

**Marcel Santilli:** Like, where is the link to what we show them?

**Marcel Santilli:** Like, I have no idea what we show them.

**Marcel Santilli:** Like, and so, like, and it's, like, I don't know.

**Marcel Santilli:** Like, what is this blog? Did Georgemaine just spend a whole day building this blog?

**Marcel Santilli:** Like, or is he spending, are we creating a thing in Figma to begin with?

**Marcel Santilli:** Like, it's, like, I'm trying to understand, like, are we working on two projects?

**George Haikal:** Like, Nicolas is working on one project and Georgemaine is on a different one.

**George Haikal:** Like.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like, I'm confused.

**Marcel Santilli:** And no one communicates clearly here.

**Marcel Santilli:** Here's a solution.

**Marcel Santilli:** Like, I had in mind.

**Marcel Santilli:** For what?

**Marcel Santilli:** A solution to what?

**Marcel Santilli:** Like, it's like, what are we doing here?

**George Haikal:** Yeah, okay.

**George Haikal:** So, I mean, two things.

**George Haikal:** We'll get everything you need answered.

**George Haikal:** But I also need you at least, like, once a week to check in on this project with them, too.

**George Haikal:** We can do, like, a 15-minute thing with all of them.

**George Haikal:** Because all I'm doing right now is, like, you and Daniel are figuring out things.

**George Haikal:** They're doing things.

**George Haikal:** Because I'm talking to CeCe and trying to, like, put all the piece together with incomplete information, which is fine.

**George Haikal:** But we can avoid this in the future.

**Marcel Santilli:** Yeah, like, in the future, like, we had a very clear meeting with Rachel that I clearly communicated the prototype and showed her.

**Marcel Santilli:** And she was happy with that. Everybody was aligned with that. Right?

**Marcel Santilli:** And the goal is to, like, build that out to production.

**Marcel Santilli:** At last week's meeting, we were blocked by getting access to the Lovable codebase. The goal was to get access and then take the prototype we had already shown, get it production-ready, and ship it in a section of the site.

**Marcel Santilli:** It was not to build a net new experience altogether.

**Marcel Santilli:** If there are improvements needed—like skinning it to be more on brand because they pushed back—that's different, right?

**Marcel Santilli:** But what I don't understand is where along the way did that change, and why? Who decided that we should build a net new experience instead of sticking with the prototype we already showed the client?

**Marcel Santilli:** Like, you know, and so now I'm kind of confused as, like, who's doing what and why and, like, where is the latest version of the thing that was already working, you know?

**Marcel Santilli:** there we, like...

**Marcel Santilli:** But anyways, like, we don't have the stakeholders here, so this meeting is kind of useless without the people doing the work.

**Marcel Santilli:** Because there were so many updates to this project, like, in the previous meeting of the strategy sprints, too.

**Marcel Santilli:** And there are updates that I didn't have. So I'm trying to piece it together, but if the people doing the work aren't here, I can't understand what's happening. But let me get the rest of the team on here.

**Georgemaine Lourens:** Thank you.

**Marcel Santilli:** Hey, sorry, we just got everyone here. I have about 10 minutes before I'm back-to-back meetings for the rest of the day.

**Georgemaine Lourens:** Okay.

**Marcel Santilli:** I, what I'm trying to piece together is, like, I'm seeing a bunch of looms, but I'm not seeing any links.

**Marcel Santilli:** And then there's, like, the prototype that I had built that then Nico, I kind of, like, took it a little bit further.

**Marcel Santilli:** But then the designs I'm seeing, I think, are, like, so, so miles different from, from that experience.

**Marcel Santilli:** I'm not saying they're bad, but it's also, like, we're presenting this thing over here, but then I'm not sure what this other thing is in Figma, like, that we're building towards, like, and are we building, and what should we present to the client today, you know?

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** OK, so the way I looked at this: you had a vision of what templates could look like from an SEO perspective. In week one, I tried to translate that into Lovable's design system in Figma. In week two (this week), I wanted to build that into the codebase. I explored it in Figma and Origami, but then we hit the wall with Sebastian, and we switched to focusing on templates, which is where we are now.

**Marcel Santilli:** Sebastian's pushback was about the quality of the app, not the overall experience. But Cece is the head of marketing, not him. He's just giving inputs. Cece and Rachel were super aligned to the prototype. Look, let's put this behind us—whether we wasted time or not, we need to show them something working.

**Marcel Santilli:** We have four weeks before we're fired, essentially, right? And we have to deliver something live. So now we're down to three and a half weeks. We had a prototype that was working. So what I'm not sure of: is the thing you built in Figma close to it and ready to show? What's the delta? And what should we show them today? We're filling in the content and templates, but the experience is what we need to nail.

**Georgemaine Lourens:** Yeah, I don't think we have anything to show today in terms of the gallery.

**Georgemaine Lourens:** Because we essentially just stopped working on that to focus on templates. That was the game plan we and George came up with yesterday.

**Marcel Santilli:** But if we have templates and no experience, we can't publish.

**Marcel Santilli:** If we have an experience and an okay template, we can publish and show them results, right?

**Marcel Santilli:** And so our goal is to launch the template site.

**Marcel Santilli:** Our goal is not to have production-ready apps that are better than fully built apps that engineers and designers work on, right?

**Marcel Santilli:** Which is Sebastian's, like, unrealistic bar.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Okay, that's fine.

**Marcel Santilli:** Nicolas, you had built a version of the prototype.

**Nicolas Castellanos:** Yeah, we were focusing on templates.

**Nicolas Castellanos:** Yeah, I'll get what Georgemaine built in Figma integrated into the render preview prototype. I should have that working probably by Friday. So I have a render preview that's working—you can log in with email and password, and it has the embedded experience. But it has the old look and feel from the bytecoded version. It doesn't look like the new stuff Georgemaine built.

**Marcel Santilli:** okay.

**Marcel Santilli:** So, Georgemaine, so the, can you show me, or is there something that I can at least show our clients, like, today, even if it's not production-ready?

**Marcel Santilli:** We've gone a whole week—we have to show something that we did. It's okay to say we had to slow down because we're getting conflicting feedback.

**George Haikal:** Yeah, and you did make progress, it just isn't perfect, which is, which is fine.

**Marcel Santilli:** We can still show them something, Georgemaine. But it's hard for us to review a Loom, right?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** I prototyped this in origami where it's kind of like you have the filters, it's kind of working, and you can select multiple ones.

**Georgemaine Lourens:** But this was mostly around like filling in the interactions and the visual design.

**Georgemaine Lourens:** And if you click on one, you can go to the page and you can change the styles of the template and get a different look.

**Georgemaine Lourens:** And it kind of has the page structure here.

**Georgemaine Lourens:** And this was the thing that I was going to build.

**Georgemaine Lourens:** But I guess like the only way that you could show this is to have a screen recording of it and just kind of like scrub through it.

**Georgemaine Lourens:** If that makes sense and you want to share it, you can do that.

**Marcel Santilli:** Is Origami creating the code or is it more like Figma?

**Georgemaine Lourens:** It's a quick prototyping tool that I'm very good at.

**Georgemaine Lourens:** Would it help if I make a screen recording?

**Marcel Santilli:** No, screenshots would be fine, or just share it in the project channel. Nicolas, can you reshare the link to the render preview?

**Marcel Santilli:** But it still feels like, like, I would much rather take what's already built and find ways to clean that experience up than build something that's substantially different.

**Marcel Santilli:** Unless, like, the thing that's different is, like, not super hard to do, right?

**Marcel Santilli:** Like, just because, like, we don't have time, right?

**Marcel Santilli:** I would rather launch something and improve it iteratively than get fired and never have the chance to make it the way we want it. The templates library is part of our eight-week deliverable, and we only have four weeks left. We need to ship something—a site that's ready to deploy on the /templates route. Launching something imperfect is better than losing the client entirely.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** No, I think that makes sense.

**Georgemaine Lourens:** If we focus on the template library and ignore Sebastian's quality concerns, I think that's the right call. The idea was that we pitch them the template library and build it—and at a certain point, it becomes so good that they want it, rather than us trying to get buy-in from Sebastian or prove we can make high-quality work.

**George Haikal:** Yep.

**George Haikal:** And after you and I spoke about that, Georgemaine, I met with Cece later that day and she's superseded Sebastian.

**George Haikal:** She's on our side on us taking the direction.

**George Haikal:** She's just going to try to basically push it through straight to the CEO versus having to take in all of Sebastian's feedback.

**George Haikal:** So what you're saying is accurate.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So the next steps for us and Nicolas are to focus on the gallery and get it running.

**Nicolas Castellanos:** Exactly, focus on the gallery.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Just to be clear, so we don't, like, it's totally okay if we don't get super high-end templates, like, in three weeks.

**Nicolas Castellanos:** Like, what needs to have, like, the great experience is, like, the gallery, and then we figure out templates.

**Marcel Santilli:** I'm confident we can hustle our way to good templates. I'm not worried about that, even if we spend several hours bytecoding to make it look good, sync the code to GitHub, and run it through a cloud function to reverse engineer the repo as a sample prompt. Then we create a workflow that describes the page in an SEO-friendly way. Sebastian doesn't understand that's possible—he doesn't know how limited Lovable is under the hood compared to Bolt. You can't one-shot Lovable because it doesn't have a good planner and agent to plan and execute tasks.

**Marcel Santilli:** So having the experience and the scaffolding that works is what we need to nail. Nicolas, do you have a link to the render preview?

**Nicolas Castellanos:** I should send it to Slack.

**Marcel Santilli:** For MVP, it's okay if the brand colors aren't perfect. The version you have should feel more like it's part of the Lovable site with the right colors and fonts. What we're optimizing for is SEO—when people search "construction website examples," they find pages like Wix templates—filter landing pages, index pages. That's what we need. Everything else is re-skinning and cleaning up the UI. Georgemaine's design concept is good; we just need to integrate it into the gallery and make it feel like Lovable.

**Marcel Santilli:** Let me cancel a bunch of my meetings so I have time to work on this. I'll check the project channel, but I'm clearing my calendar.

**Georgemaine Lourens:** Okay, cool. Thanks.

**Georgemaine Lourens:** All right.
