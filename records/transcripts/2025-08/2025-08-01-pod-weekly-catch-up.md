# Pod weekly catch up

<metadata>
date: 2025-08-01
time: 14:01 UTC
duration: 11 minutes
organizer: oluwatimilehin@growthx.ai
participants: Oluwatimilehin Ademosu, Vivek Shankar, Nika Narimanidze, Mara Leighton
fathom_recording_id: 77947877
fathom_url: https://fathom.video/calls/367828891
share_url: https://fathom.video/share/2MrxaQWSZCj-xC8ToqyT8cpgThKstZd4
source: fathom
enriched_on: 2026-03-03 22:15 UTC
</metadata>

---

## Summary

The GrowthX Labs pod held their weekly status meeting to review progress on multiple platform integrations (DataGrid, Galileo, Zan, Papid, Strapi) and identify blockers. Key decisions included deprioritizing the PSEO pipeline request until SSL changes are clarified early the following week, and needing separate Linear tickets for Zan alternatives and version stage work. Critical blocker: Oluwatimilehin needs to obtain a Strapi API key from Paul and the CEO to unblock publishing automation.

---

## Context

This is an internal GrowthX pod sync (the Labs team working on platform integrations and content infrastructure). The team manages multiple proprietary and third-party tools (DataGrid for content metadata, Galileo for publishing, Zan for vendor/page management, Papid for content creation, Strapi for CMS features) to support the broader content operations. The meeting reviews weekly progress, surfaces blockers, and aligns on priorities. Mara Leighton appears to be an engineering manager or technical lead overseeing delivery; Oluwatimilehin is the internal GrowthX owner (organizer); and Vivek, Nika, and Ismail (not speaking in transcript) are Labs team members. The conversation reflects typical content ops challenges: vendor dependencies, API access delays, and scope clarification with external development partners.

---

## Relevance

**To GrowthX Delivery:**
- PSEO pipeline automation request deprioritized pending SSL infrastructure changes — decision to re-evaluate early the following week based on impact analysis
- Zan vendor/pages publishing workflow requires detailed video documentation and clear dependency sequencing to prevent scope creep and rework
- API access blockers (Strapi key) directly impacting publishing automation timelines — escalation to CEO/Paul required

**To GrowthX Operations:**
- CMS category mapping inconsistencies between scenarios causing specification gaps in platform work — training/documentation opportunity
- Content editorials (RAM editorials) behind schedule — Vivek planning to catch up 3 articles the following week
- Publishing mode issues (automatic vs. draft) detected and flagged for correction — operational QA process observation

**To GrowthX Business Development:**
- Labs team managing multiple external vendor integrations (engineering partner for Strapi) with typical project friction (scope clarification, timeline adherence, communication delays)

---

## Overview

- Multiple platforms (DataGrid, Galileo, Zan, Papid, Strapi) discussed; various tasks in different stages of completion
- Publishing automation and API key issues need immediate attention
- Team encouraged to follow processes and escalate blockers when necessary

---

## Key Topics

### DataGrid Updates

  - Publishing criteria not interchangeable; H1 and MetaTitle remain the same
  - PSEO pipelines: Follow-up planned for Monday, but deprioritized due to potential SSL changes
  - Internal fixes implemented

### Galileo and Publishing Automation

  - No urgent Galileo tasks
  - Vivek to follow up on publishing automation ticket with Sivanan this week

### Zan Development Progress

  - Markus close to completion; small details remaining (e.g., data wrapper IDs)
  - Separate Linear requests needed for alternatives and version stages
  - Video explanations required for vendor vs. pages publishing workflow

### Papid and Strapi Requests

  - Inline images feature for Papid planned for next week
  - Strapi staging automation request pending (3 weeks old); importance communicated
  - Medium redistribution task assigned to Marcos, follow-up needed
  - Code formatting being addressed by Marcus
  - Image redesign awaiting Figma guidelines from Guzar and Victor

### API Key and Publishing Issues

  - Oluwatimilehin to reach out to Paul and CEO for Strapi API key
  - Nika discovered automatic publishing instead of draft status; Markus to be notified

### Content and Editorial Updates

  - Vivek behind on RAM editorials; plans to catch up next week
  - Nika working on a draft requiring internal linking

---

## Action Items

**Vivek Shankar (GrowthX Labs)**
- Follow up on publishing automation ticket for Sivanan

**Nika Narimanidze (GrowthX Labs)**
- Open Linear requests for Zan — alternatives & version stages
- Record videos for Zan — vendor vs. pages publishing workflow and alternatives, highlighting dependency order
- Inform Markus about Zan automatic publishing issue (should be draft)

**Oluwatimilehin Ademosu (GrowthX)**
- Ping Paul and CEO for Strapi API key in a new thread

---

## Transcript
**Vivek Shankar:** I'm going into DataGrid first.

**Vivek Shankar:** I don't think we had any requests there, right, Nika?

**Nika Narimanidze:** Yeah, one is about publishing, but a week and a half didn't pass.

**Nika Narimanidze:** H1 and MetaTitle are the same.

**Nika Narimanidze:** So when the publishing happens, the criterias are not interchangeable.

**Nika Narimanidze:** So that's the first one.

**Nika Narimanidze:** The second one is about the PSEO pipelines.

**Nika Narimanidze:** And I think a week has already passed, so we can, from Monday, we can just follow them up and ask to handle this.

**Nika Narimanidze:** And yeah, that's it, I guess.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Internally, it's fixed.

**Vivek Shankar:** Yeah, I saw that, yeah.

**Vivek Shankar:** The PSEO pipelines.

**Vivek Shankar:** Mara, so for context, you know, the pseudo, whatever, SEO articles we were doing, the request that Nika put in was basically to create individual pipelines for each of those articles based on templates that we just click and it goes.

**Vivek Shankar:** Given the, I'm wondering, is this, should we push them to do this?

**Vivek Shankar:** Because, you know, given that the SSL might change the analysis.

**Vivek Shankar:** Yeah, that's a great question.

**Mara Leighton:** And also thanks for giving me the context.

**Mara Leighton:** I would say there are other, there are other priorities probably that they should focus on in the meantime.

**Mara Leighton:** If like, and it's not like we're waiting that long.

**Mara Leighton:** Early next week, we might hear that things are shifting drastically.

**Mara Leighton:** So I would say that's when we can probably just like leave.

**Mara Leighton:** And then hopefully we get some clarity at the beginning of next week and we can go from there.

**Mara Leighton:** Yeah.

**Mara Leighton:** Okay.

**Vivek Shankar:** So Nika, I'd say like maybe follow up on it next.

**Vivek Shankar:** But it's not an urgent.

**Vivek Shankar:** Okay.

**Nika Narimanidze:** Yeah.

**Mara Leighton:** Feel free, Nika, to tag Vivek or I and ask also if we have an update, you know, before you feel like you have to go bump it to next week.

**Mara Leighton:** Feel free.

**Mara Leighton:** Sure, we'll do.

**Nika Narimanidze:** Okay.

**Vivek Shankar:** Next one is Galileo.

**Vivek Shankar:** I don't believe there was anything for Galileo.

**Vivek Shankar:** Publishing automation — I need to follow up on that. I have opened the publishing ticket for Sivanan, so I'll get that done this week.

**Mara Leighton:** All right.

**Vivek Shankar:** I have opened the publishing ticket for Sivanan, so I will do that.

**Vivek Shankar:** That's going to get done for this week.

**Vivek Shankar:** Zan, this is the big one.

**Vivek Shankar:** I think there were, well, there was only one, but there's a bunch of things, right?

**Vivek Shankar:** Okay.

**Nika Narimanidze:** Yeah, I'm just running the flow for this.

**Nika Narimanidze:** I think Markus is very close. We have some small details left.

**Nika Narimanidze:** I saw that he added the part for data wrapper IDs, and I'm waiting for a third flow to finish.

**Nika Narimanidze:** So I'll have a better context on this.

**Nika Narimanidze:** But I think that we are very close.

**Nika Narimanidze:** Okay, cool.

**Vivek Shankar:** Do you...

**Vivek Shankar:** I think we should open the separate...

**Vivek Shankar:** Sorry, the follow-up request as well.

**Vivek Shankar:** It's a separate linear request for the alternatives and for the version stages.

**Nika Narimanidze:** Yeah, exactly.

**Nika Narimanidze:** Please put it in there.

**Nika Narimanidze:** Yeah.

**Vivek Shankar:** And why is he missing so many little details?

**Vivek Shankar:** Like, I don't understand.

**Vivek Shankar:** Because he took the document.

**Vivek Shankar:** I remember when you were off, I gave him the document, the template.

**Vivek Shankar:** Even then, he's missing a lot of little things.

**Vivek Shankar:** Like, do you know why he's missing it?

**Vivek Shankar:** Or any way to prevent that?

**Nika Narimanidze:** The miss was about the CMS categories, and it is always adding up.

**Nika Narimanidze:** So when we mapped, we had a different scenario, and now it's a different scenario.

**Nika Narimanidze:** The same thing was with data properties, so it's a different issue.

**Nika Narimanidze:** Okay, cool.

**Vivek Shankar:** All right, so yeah, for those follow-up requests, I think you'll need to maybe record a couple more videos or something.

**Nika Narimanidze:** Yeah, basically to explain how the vendor versus pages publishing work and alternatives.

**Vivek Shankar:** Yeah, and just make sure you highlight the dependency there, like, you know, which order it needs to go, like, the versus comes first and the alternatives, so that he doesn't start working on the alternatives before.

**Vivek Shankar:** Okay, that was good.

**Vivek Shankar:** Papid, we didn't have any.

**Vivek Shankar:** There was this one which I wanted to get in, which was the inline images, similar to what we have in Strapi, but I don't think it's urgent, so I didn't find it.

**Vivek Shankar:** I'll do it next week.

**Vivek Shankar:** We have Strapi, I think we had a couple, right, over here?

**Oluwatimilehin Ademosu:** Okay, we had the staging automation request, and I don't know, we submitted that like three weeks ago, and you told me to follow up on Wednesday, and I did follow up on Wednesday, talking about how urgent it was, because Kirkland was asking, he said they didn't include it in the sprints, and he was asking how important it was to us, or whether it was like a nice to have, and I told him it wasn't, but I'm not written anything on that front yet, and which other ones we have open, okay, the medium redistribution.

**Vivek Shankar:** Just going back to the publishing, looking at the comments, you mentioned the API key. Did you reach out for the Strapi API key?

**Oluwatimilehin Ademosu:** No.

**Oluwatimilehin Ademosu:** Okay.

**Oluwatimilehin Ademosu:** Can you please do that?

**Vivek Shankar:** I think you can ping Paul and CEO for that.

**Vivek Shankar:** So just create like a new thread and you can just ping them.

**Nika Narimanidze:** Okay.

**Oluwatimilehin Ademosu:** For the medium one, Marcos has been on it since like last week and I followed up again this week, but nothing again.

**Oluwatimilehin Ademosu:** So I don't know how many times I can't follow up.

**Vivek Shankar:** No, you can follow up.

**Vivek Shankar:** This thing is really old.

**Vivek Shankar:** like a month old.

**Vivek Shankar:** So yeah, it needs to.

**Vivek Shankar:** Yeah, they have it in one of their cycles.

**Vivek Shankar:** So cycle six.

**Vivek Shankar:** So I think we may see it like, yeah, it says seven weekdays left.

**Vivek Shankar:** So okay.

**Vivek Shankar:** They have it in their sprint.

**Vivek Shankar:** But yeah, just make sure you check the linear ticket itself because the status says over there, like, you know, whether they've moved it into the.

**Vivek Shankar:** Then the code formatting.

**Vivek Shankar:** I know you followed up on that.

**Vivek Shankar:** So Marcus is looking at that now, right?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Then the image redesign, I've been following up.

**Vivek Shankar:** I think they needed like a Figma, whatever, guideline or something.

**Vivek Shankar:** So I've checked with Guzar and Victor.

**Vivek Shankar:** I don't know.

**Vivek Shankar:** They haven't responded yet.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So the only open item there is, yeah, let's just get that API key publishing.

**Vivek Shankar:** That's pretty much it.

**Vivek Shankar:** Okay.

**Vivek Shankar:** I don't think we have any more accounts, right?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Quick, quick addition to our ramp.

**Nika Narimanidze:** I have run it.

**Nika Narimanidze:** And I think that the flow has...

**Nika Narimanidze:** Published this automatically.

**Nika Narimanidze:** It's weird.

**Nika Narimanidze:** I'm drafting this.

**Nika Narimanidze:** I'm going to tell it to Markus as well.

**Nika Narimanidze:** So it was supposed to be in draft, right?

**Nika Narimanidze:** Yeah, yeah, yeah, and it was published automatically, so I'm going to fix that.

**Nika Narimanidze:** OK, cool.

**Vivek Shankar:** I can follow up with that.

**Oluwatimilehin Ademosu:** All right.

**Vivek Shankar:** Don't think there's anything outstanding.

**Vivek Shankar:** Nika, I know you have that one draft that will come in.

**Vivek Shankar:** Yeah, it needs internal linking, yeah.

**Vivek Shankar:** Miles, this is an update I couldn't get to the RAM editorials, two of them, so I'll try to maybe do three next week or something.

**Vivek Shankar:** Yeah, I think, I imagine that will be just fine.

**Mara Leighton:** Yeah.

**Vivek Shankar:** Yeah, we kind of mentioned it either in the post-all update, so I just, you know, slide it in there.

**Vivek Shankar:** OK, that was pretty much it.

**Vivek Shankar:** Just a reminder again, guys. Make sure you follow all processes and escalate blockers when necessary.

**Vivek Shankar:** Mara, was there something?

**Vivek Shankar:** I don't think so.

**Vivek Shankar:** don't think there's anything else.

**Mara Leighton:** But, yeah, if any, like, if you're facing any continual blockers or you feel like linear tickets aren't getting the response that you need them to, as always, feel free to ping me in the channel and I can help escalate it also and just make sure that it becomes a priority for the engineering sprints.

**Mara Leighton:** But, yeah, this has been great.

**Mara Leighton:** Yeah.

**Mara Leighton:** All right.

**Mara Leighton:** So, yeah.

**Vivek Shankar:** Do you guys have anything to bring up or?

**Nika Narimanidze:** No.

**Nika Narimanidze:** All good, I guess.

**Nika Narimanidze:** No.

**Oluwatimilehin Ademosu:** Yeah.

**Oluwatimilehin Ademosu:** Okay.

**Oluwatimilehin Ademosu:** Cool.

**Oluwatimilehin Ademosu:** Great.

**Vivek Shankar:** All right.

**Mara Leighton:** Well, I hope you guys have a great weekend.

**Vivek Shankar:** You too.

**Nika Narimanidze:** Nice.

**Nika Narimanidze:** Bye-bye.

**Nika Narimanidze:** Bye, everyone.

**Oluwatimilehin Ademosu:** Thank you.

**Mara Leighton:** Thanks.
