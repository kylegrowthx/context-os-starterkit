# Impromptu Google Meet Meeting

<metadata>
date: 2025-12-01
time: 18:13 UTC
duration: 24 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill, Israel Beni
fathom_recording_id: 105310458
fathom_url: https://fathom.video/calls/492505250
share_url: https://fathom.video/share/ECUFXXxMwbyDv8vs1E9xq7Bn5MpswafC
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew and Israel diagnosed and resolved a critical 500-error blocker in the Batch 3 redirect project. The InnoWell dev team had changed city-level page URLs in Prismic two months ago without implementing redirects, causing both a massive traffic drop and Israel's local build failures. They agreed on a two-phase solution: Israel will implement urgent code-based redirects from old broken URLs to current live versions tonight (~1 hour), then execute the planned Batch 3 redirects afterward. Matthew will message InnoWell to request urgent production deployment.

---

## Context

Matthew Alves-Hill (GrowthX) is working with Israel Beni on the InnoWell Batch 3 redirect project, which involves restructuring URLs for city-level ketamine pages. The Batch 3 project is a phased URL redirect initiative to improve site structure and SEO. However, the project has been blocked by critical 500 errors that appeared roughly two months ago when the InnoWell dev team made unannounced URL changes in Prismic without implementing redirects. These errors are causing both a significant traffic drop (visible in analytics since September) and local build failures on Israel's development machine.

---

## Relevance

**To GrowthX Delivery:**
- Critical SEO impact: 500 errors serving for ~2 months signal broken pages to Google, causing measurable traffic losses that need urgent remediation
- Two-phase redirect strategy demonstrates technical pragmatism: fix immediate errors first (Phase 1), then execute planned redirects (Phase 2)
- Client communication challenge: InnoWell dev team made changes without consultation; GrowthX must now balance account management with getting urgency on production deployment

**To GrowthX Business Development:**
- Account health risk: Uncoordinated changes on InnoWell's dev team suggest communication gaps and lack of process discipline around URL/site structure changes
- Expansion opportunity: Process improvements and clearer change management procedures could be bundled into future engagements

---

## Overview

- **Critical 500 Errors:** InnoWell dev team changed page URLs in Prismic ~2 months ago without redirects, causing 500 errors and a massive traffic drop.
- **Immediate Fix:** Israel will implement an urgent code-based redirect tonight to fix the 500s, pointing old URLs to their current live versions.
- **Blocker Resolved:** The 500 errors are the source of Israel's local build failures, which previously blocked deployments.
- **Phased Rollout:** The fix will be deployed first, followed by the planned Batch 3 redirects from current live URLs to the new, desired structure.

---

## Decisions & Commitments

**Immediate Decision:**
- Implement a two-phase redirect strategy to resolve both the immediate 500 errors and the planned Batch 3 redirects.

**Committed Actions:**
- **Israel Beni:** Implement code-based redirect from old, broken 500 URLs to current live URLs tonight (~1 hour). Will also review InnoWell codebase to understand the URL structure changes and confirm dynamic redirect feasibility for Phase 2.
- **Matthew Alves-Hill:** Message InnoWell to request urgent production deployment of the Phase 1 fix. Will seek clarification from InnoWell on why the original URL changes were made.

---

## Open Questions

- Why did the InnoWell dev team change the URLs without redirects? Was it truly necessary for their ad campaign, or was it an oversight?
- Can the dynamic redirects (live → new URL structure) be implemented as a safe code-based solution, or will they require Prismic-level changes?
- What is InnoWell's production deployment timeline? Matthew will communicate urgency, but approval speed is unknown.

---

## Key Topics

### The Problem: Unannounced URL Changes & 500 Errors

- The Batch 3 redirect project is blocked by critical 500 errors on city-level ketamine pages.
- **Cause:** InnoWell dev team changed page URLs in Prismic ~2 months ago to support an ad campaign.
- **Impact:** No redirects were implemented → 500 errors for all old URLs → massive traffic drop since September.
- **Significance:** The 500 errors are the source of Israel's local build failures, which previously blocked deployments.

### The Solution: Phased Redirect Strategy

- Israel will implement a two-phase redirect strategy to fix the errors and complete the project.
- **Phase 1 (Tonight): Fix 500s**
    - **Action:** Code-based redirect from old, broken URLs → current live URLs.
    - **Timeline:** Code complete tonight (~1 hour).
    - **Rationale:** An urgent fix to stop serving 500s and prevent further SEO damage.
- **Phase 2 (Post-Deployment): Complete Batch 3**
    - **Action:** Redirect from current live URLs → new, desired URL structure.
    - **Rationale:** This is the original scope of the Batch 3 project, which can proceed once Phase 1 is live.

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Add Israel to growthx Fathom
- Message InnoWell re: Batch 3 redirects; request prod deployment urgency

**Israel Beni**
- Implement 500→live redirects for Batch 3 city ketamine pages; then redirect live→new path
- Review InnoWell codebase for Batch 3 URL/build issues; confirm dynamic redirect feasibility

---

## Transcript

**Matthew Alves-Hill:** Hey, how are you doing?

**Israel Beni:** I'm doing good. It's a bit cold here, but that's fine.

**Matthew Alves-Hill:** Winter, winter cold.

**Israel Beni:** Yeah, last week it's been raining all week. It got really cold, but it's kind of moderate today.

**Matthew Alves-Hill:** Okay, let me introduce you to the craziness of what's happening. So this is Batch Three — these are the city-level ketamine pages. This is what they currently look like.

**Israel Beni:** I can see the screen.

**Matthew Alves-Hill:** I would like to add Fathom to our account. Let me add you. Okay, so this is Batch Three. Currently, this is what the page looks like. You can see here — this is the problem with "availability." That's what we need to get rid of. It should just be this. Yeah, because in Batch One we did Ketamine to Arizona. Now we're going to add city-level foldering. Here's where it gets kind of stupid.

**Matthew Alves-Hill:** So this is the live version right now. Until about two months ago, this was the correct pathway. Now it's a 500 error. Someone on the InnoWell dev team went through and changed all these URLs in Prismic to the new ones without doing a redirect. That means traffic has dropped massively. Someone didn't understand that if you just change the URL without a redirect, you tell Google your pages are 500s and the pages disappear.

**Israel Beni:** Kind of.

**Matthew Alves-Hill:** This is high priority. We can't afford pages returning 500s. So basically, from an account management point of view, we need to tell them this is crazy. We've told them before. I don't know how this happened, but what we need to do now is redirect these 500s. Originally Batch Three was supposed to be just one redirect from here to here, but because of what they've done, we now need to redirect both the old broken URLs and the new ones to the desired state. We need to redirect both of these because we don't want 500s on the site either.

**Israel Beni:** If the changes are in the codebase, we'll need to handle that differently than if it's just in Prismic.

**Matthew Alves-Hill:** Sorry, can you explain that again? Do you think maybe the change hasn't been made in the codebase?

**Israel Beni:** What I'm saying is some changes have been made to the page structure in Prismic, right?

**Matthew Alves-Hill:** I think so. I think it's in Prismic, but I'm not actually sure for sure. I don't know if it was in Prismic or the codebase itself.

**Israel Beni:** Probably there's something happening on the server, not just on the client side. There's a high chance this is a code-based issue. This needs testing before going to production. When it comes to the redirect, I was pretty sure of the functionality, but I need to confirm that on staging. These changes came to production without being tested.

**Israel Beni:** So going forward, what would you recommend? Should we communicate this to them for them to work on, or would you like me to look at the code?

**Matthew Alves-Hill:** Well, the damage traffic-wise has been done now. It's been almost two months of this since September. The clicks started dropping.

**Israel Beni:** Yeah, I understand now. You remember in one of my updates I told you that the deployment was blocked by a build issue? Well, I think there's a link between those two. When I tried to build the production version of the website locally before pushing my code to their repository, I'm not able to get a successful build.

**Matthew Alves-Hill:** So because of this change, that's why your local wasn't mapping correctly.

**Israel Beni:** Yeah. Any experienced developer, before pushing any changes to a repo, has to test their code first. There's a pipeline I have to go through. On my local, when I try to have the build version — which is what's going to be on the live server — I simulate that on my local, but I'm not able to get that to work. There are some issues that come up during that build process. I believe this might be related to this.

**Matthew Alves-Hill:** That's good to know. So basically, we want to keep moving. We want to keep working through the redirects. If we raise this issue right now as part of this project, it potentially causes bigger issues, because we're basically going to tell them, hey, you did this crazy thing, and now we have to deal with it. It opens up a whole other discussion.

**Israel Beni:** Do you mean our team or InnoWell?

**Matthew Alves-Hill:** No, I'm saying if we show this to InnoWell eventually, it's going to be me pointing a finger at someone on the InnoWell dev team saying, hey, this is crazy. You guys just changed URLs on all these pages, and now all the traffic is gone.

**Matthew Alves-Hill:** So this morning I sent InnoWell a message saying we want to do Batch Three — we want to redirect these pages, but there's a 500 error on them. We don't know why. Can you please fix the pages so they're live, and then we can do the redirects?

**Matthew Alves-Hill:** When I asked them, she replied saying, "I don't see a 500 error. This is the correct URL. This is where you can find them."

**Matthew Alves-Hill:** I'm like, okay, that's bizarre. So I dig deeper and start to see the issue. Then I asked them, what happened? And she said, yeah, they changed the URLs. They didn't redirect them. They just changed the URLs to help with an ad campaign they ran. They ran an ad campaign for city-level ketamine pages and just changed the URLs at that time because it fit with their campaign.

**Matthew Alves-Hill:** I still don't know why they did this. But the point is, what I thought was going to be just one redirect in Batch Three, is now much more complex. We have a load of 500 errors that we need to fix. We have all these URLs they created, which are the exact same as what the pages used to look like — they literally just changed the URL. There's nothing different in the content.

**Matthew Alves-Hill:** So now you have this one, which is folded incorrectly, and this one, which is a 500 error. Priority-wise, the one that's 500ing needs to be redirected here, but these ones causing 500 errors are telling Google our site is a mess. Both need to be done basically at the same time. Does that make sense?

**Israel Beni:** You all need to redirect the live line if that hasn't been done yet.

**Matthew Alves-Hill:** So we need to redirect those 500s and then afterwards redirect from the live URL to the new pathway.

**Israel Beni:** Yeah, you'll need to do that. I'll check that.

**Matthew Alves-Hill:** So essentially what we want to do is redirect those 500s and then afterwards redirect from the live URL to the new pathway. Does that work?

**Israel Beni:** I can get rid of the 500 errors tonight. That's not a big deal. I can set a redirect in the codebase. At least while we figure this out.

**Matthew Alves-Hill:** Yeah, I think so. Just immediately redirect this batch.

**Israel Beni:** Let me see that real quick. It probably won't take more than an hour.

**Matthew Alves-Hill:** So how would they redirect?

**Israel Beni:** Instead of having a 500, anyone who uses the previous URL will redirect to the current live one.

**Matthew Alves-Hill:** Okay, so the currently live one, right. And then we redirect the current live one to the new path afterwards. Yeah. And that's the best solution, you think?

**Israel Beni:** That at least will help us to not have 500s for now. Because this is high risk no matter what approach we take. It's going to take time. But meanwhile, we shouldn't have 500s.

**Matthew Alves-Hill:** That's great. Do you want me to try and find out why they did this? In your experience as a developer, does this seem like it could have been justified?

**Israel Beni:** No, it's always good to hear from that perspective. I can have some speculations, but it's really nice to hear from them. Personally, I think there hasn't been thorough testing of this. It might depend on the developer. A lot of developers like to take shortcuts. There might be various reasons, but I like to give the benefit of the doubt here. Yeah.

**Matthew Alves-Hill:** Okay. So basically we go and redirect those 500s and then afterwards we redirect from the live URL to the new pathway. Cool. And timeline-wise, what do you think?

**Israel Beni:** I can get that done tonight. Now, the time for it to go into production, that's also a question.

**Matthew Alves-Hill:** I'll make it clear to them that it's urgent. So would that be for the complete Batch or just the 500s tonight?

**Israel Beni:** Right now I'm looking at the dynamic redirects. I need to confirm that, but I'll just go with the first one first. That's what I'm focusing on right now.

**Matthew Alves-Hill:** Okay, all right. I'm going to message them in the group. I'll see if I can find any more information about why this was done, just to help you. If you can, maybe you can look at their codebase just to confirm whether you think it's a code-based issue. Anything you can see from your side would be helpful, because they aren't great at communicating. So I'll figure it out and let you know if I find anything. Let's start with this stuff. Give me like the next half hour or so. Is that fine?

**Israel Beni:** Yeah.

**Matthew Alves-Hill:** Cool. Okay, thanks.
