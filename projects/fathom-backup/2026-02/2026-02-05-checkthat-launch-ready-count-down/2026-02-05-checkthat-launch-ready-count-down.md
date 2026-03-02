# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-05
time: 16:00 UTC
duration: 26 minutes
organizer: Stevie Kim (stevie@growthx.ai)
speakers_active: Jose Farias (CheckThat Engineering Lead), Stevie Kim (Product/Growth), Pedro Steimbruch (Backend Engineer), Estevão Mascarenhas (Frontend Engineer), Jason Gong (Launch Lead)
speakers_invited_not_active: Marcel Santilli (GrowthX CEO, on other call), Daniel Lopes (GrowthX, on other call), Leonardo Carpenedo Steffen (not active in recording)
fathom_recording_id: 120058367
fathom_url: https://fathom.video/calls/556128938
share_url: https://fathom.video/share/CHZhgPqJnkxybRpv9fgWLsGBQz4WYzHy
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Engineering team confirmed launch is proceeding as planned, with system stability verified and no launch blockers identified. The `/sources` endpoint performance issue (up to 22s for high-usage customers) is not blocking launch and will be monitored post-launch. Critical action items include deploying the onboarding cap, resolving the Customer.io EU server regulatory issue for welcome emails, and setting up Intercom automation for user support.

---

## Context

CheckThat is preparing for a major launch after an intensive engineering sprint. The team had deployed analytics functionality immediately before this meeting, which surfaced some new errors requiring monitoring. The engineering team (Jose Farias, Pedro Steimbruch, Estevão Mascarenhas) is focused on stabilizing the system while Jason Gong and Stevie Kim handle launch coordination and customer communication. Marcel and Daniel were on a separate launch amplification meeting, reflecting the split between product/engineering and go-to-market activities. The mood is cautiously optimistic—the team has built substantial new functionality and tested it well, but acknowledges that a feature-rich launch will inevitably surface edge cases once real users start using the product.

---

## Relevance

**Engineering & Product Development:**
- System performance tuning and monitoring strategy for launch day
- Post-analytics deployment error tracking and resolution
- Onboarding flow optimization and cap implementation
- Webhook reliability and Cloudflare security rule management

**Launch Operations:**
- Email delivery infrastructure constraints (Customer.io EU/US server mismatch)
- Customer support readiness (Intercom automation, PostHog analytics setup)
- Team communication and issue escalation protocols during launch

**Risk & Incident Management:**
- Frontend infinite loop detection and monitoring (Sentry)
- `/sources` endpoint performance degradation under load
- Personal email domain blocking (potential user support friction)

---

## Overview

- **Launch Proceeding:** The team is confident in the build's stability and will proceed with launch, focusing on system monitoring and minor fixes.
- **Performance Bottleneck:** The `/sources` endpoint is slow (up to 22s) for workspaces with many prompts. This is not a launch blocker, as it only affects existing, high-usage customers.
- **Email Complication:** Welcome emails via Customer.io are blocked by a regulatory issue (EU server for US users). Jason will send emails manually as a workaround.
- **Intercom Automation:** Stevie will add an auto-reply and a proactive pop-up message to improve the user support experience.

---

## Key Topics

### System Health & Performance

  - **Sentry Errors:**
      - `maximum call stack exceeded`: A new frontend error (likely an infinite loop) appeared after the analytics deployment. Not user-facing; requires monitoring.
      - Onboarding template errors: Resolved. Caused by a temporary database replication lag.
      - Inertia error in `context_controller`: A single, non-reproducible event.
  - **`/sources` Endpoint Performance:**
      - **Problem:** The endpoint is slow for some users (up to 22s).
      - **Cause:** Aggregation of data from many prompts in high-usage workspaces.
      - **Status:** Not a launch blocker. The team will monitor feedback from existing customers.
  - **Webhook Failure:**
      - **Problem:** A recent deploy of the "internal URL" feature broke the flow webhook.
      - **Cause:** Cloudflare's security rules blocked the webhook path.
      - **Resolution:** Reverted the deploy. The team will whitelist the webhook path to prevent future issues.

### Launch Readiness & Blockers

  - **Customer.io Welcome Emails:**
      - **Problem:** A regulatory issue (EU server for US users) blocks automated welcome emails.
      - **Resolution:** Jason will send emails manually. This is not a launch blocker.
  - **Onboarding Enhancements:**
      - **Subcategory Cap:** Estevão will deploy a cap on subcategories to prevent performance issues from excessive data.
      - **Personal Email Block:** A block for personal email domains is live. The generic error message from Clerk (`this email is blocked`) may cause user confusion and support tickets.
  - **Intercom Support:**
      - **Goal:** Improve support responsiveness and proactively help users.
      - **Actions:** Stevie will add an automated welcome message and a proactive pop-up ("Are you running into trouble?").

### Team Focus & Work Completed

  - **Jose:** Monitor system stability; passively work on the probing cadence.
  - **Pedro:**
      - Added user email to Sentry reports for better context.
      - Moved context and percentage generation to background jobs.
      - Fixed overview stats tab-switching bug.
  - **Estevão:**
      - Refactored the complex onboarding "brand" step into simpler controllers.
      - Will cap subcategories and competitors in onboarding.
      - Will hold off on non-critical UI merges until after launch.
  - **Stevie:**
      - Coordinate on the Customer.io email issue.
      - Set up Intercom automation.
      - Invite the team to PostHog.

---

## Action Items

**Estevão Mascarenhas (CheckThat Frontend Engineer)**
- Deploy onboarding cap on competitors/subcategories to prod

**Pedro Steimbruch (CheckThat Backend Engineer)**
- Tag Stevie in Customer.io thread re: EU instance/welcome emails

**Jose Farias (CheckThat Engineering Lead)**
- Keep plate clear; monitor systems; handle launch-day issues
- Work on probing cadence (passive priority)

**Stevie Kim (CheckThat Product/Growth)**
- Create Intercom welcome automation (auto-reply + pop-up)
- Invite engineering team to PostHog analytics

**Jason Gong (CheckThat Launch Lead)**
- Call Yusuf to set up @checkthat.ai inbox for Jason and Marcel

---

## Transcript
### Opening & Stevie's Scheduling Conflict (00:00 - 02:30)

**Stevie Kim:** Hey, I just realized that I have a meeting conflict and there's a launch ready meeting right now with Marcel and Daniel and some other folks. So if you guys want to just do stand up without me, I'll watch the recording.

**Jose Farias:** I wonder if we should join that, though.

**Stevie Kim:** Well, I think it's post-amplification, so it's more content stuff. Go ahead and just do it without me. I think the only thing was that 404 error that a user saw—I haven't ever seen it during onboarding, but it's something to look into. But yeah, I'll watch the recording.

**Jose Farias:** That was the output downtime. I thought it might be around the same time.

---

### Jose's System Status Overview (02:30 - 09:00)

**Jose Farias:** Okay, hello everyone. Stevie let me know she has a scheduling conflict. I think we'll have feedback from users and internal folks once we launch. We built a ton of stuff, way more than I would have advised, but it's all good—it just means the surface area is quite big. Something is probably going to happen, but I do think we did enough testing that whatever happens, we should be able to handle it. Let's just keep a level head and stay in communication. I'm optimistic.

**Pedro Steimbruch:** I have some meetings this afternoon, but I'll be back.

**Jose Farias:** There's enough of us that I think we can cover everything. We should do the standup as usual, but I want to call out that ever since we deployed the analytics stuff, error rates went up a little bit in Sentry. This is frontend stuff.

**Estevão Mascarenhas:** Yeah, specifically maximum call stack exceeded.

**Jose Farias:** There's an infinite loop somewhere. Just something to keep an eye on. Another thing—we started getting some missing template errors around onboarding. But I think that was either related to the output outage or the replication lag this morning. Has anyone looked at those?

**Estevão Mascarenhas:** I think it was the replication lag. Every page I was trying to navigate, it was sending me to the Clerk sync room with a synchronous request. But after the replication lag got fixed, I didn't get it anymore.

**Pedro Steimbruch:** We got one Inertia error in a context controller.

**Jose Farias:** I couldn't reproduce it. If it's only the one time, I think we're fine. Just something to keep an eye on. And then the last thing—the sources endpoints are quite slow, sometimes like 12 seconds, 22 seconds in some instances. I have no clue what to do about it.

**Pedro Steimbruch:** It was slower before. Last week I did the index thing. It should be two to five seconds now, mostly.

**Jose Farias:** Maybe we should reduce the number of sources displayed at once?

**Pedro Steimbruch:** That might help, but we still need to aggregate. That's the aggregation that takes time.

**Pedro Steimbruch:** We've had a regression in alerts lately. It might be just volume because the table size has increased. All the slow requests in Sentry are for the sources page.

**Jose Farias:** You know what it probably is? Some amount of workspaces are following so many prompts that we just have more data for them. That won't stop launch.

**Stevie Kim:** That's not a blocker. That's only going to affect our current customers. They're the only ones that have that many prompts in their workspaces.

**Jose Farias:** We are capping the number of subcategories in onboarding. Have we deployed that?

**Estevão Mascarenhas:** Not yet. I was trying to hold off deployments during this period.

**Jose Farias:** I think it's a small enough change that's probably fine. If someone adds a ton of subcategories, it could have other repercussions. Okay, we'll do that then.

---

### Customer.io Email Delivery Issue (09:00 - 13:00)

**Pedro Steimbruch:** Jason and Yusuf are figuring things out regarding Customer.io. Yusuf pointed out that our instance is in Europe, and this is a major regulatory issue for sending emails through a European server. They may need to change it to the US.

**Jose Farias:** What instance is in Europe?

**Pedro Steimbruch:** The Customer.io instance configured for sending welcome emails. Jason asked this morning to verify DNS entries for a customer. I added mails for Jason and Marcel, and I tagged Yusuf to spin up inboxes for Jason and Marcel. Then Yusuf figured out that Customer.io instance was in Europe.

**Stevie Kim:** Okay, got it. So everybody is aware. I'm not sure what the next step is.

**Pedro Steimbruch:** The welcome emails would use the tracking events that Daniel set up, sent to customers through Customer.io, which would then trigger the welcome emails.

**Jose Farias:** Yeah, I think let's expect that it won't delay the launch, and then if it does, that's fine. I'm going to try to keep my plate relatively empty today to have bandwidth to tackle anything. I'll just work on the probing cadence and keep an eye on things. That's my plan for today.

---

### Pedro's Work Summary (13:00 - 16:00)

**Pedro Steimbruch:** On my side, I started earlier because I knew I'd be off in the afternoon. I set up DNSs. I added user email to Sentry reports—we had the user ID but were missing the email. Now we have user email in Sentry logs and errors. I tried to merge the internal URL feature, which was breaking the flow webhook. I had to revert it because Cloudflare was blocking it. I spent an hour reverting and making sure we could receive webhooks again. I moved context generation and percentage generation to background jobs. I did QA on onboarding, fixed a few page generation issues, and fixed the overview stats when changing tabs. This is merged now.

---

### Estevão's Work Summary & Webhook Issue (16:00 - 20:00)

**Estevão Mascarenhas:** Just a comment on the webhook being blocked by Cloudflare—we had that in the CMS part. Cloudflare was thinking it was a .NET injection attack because of custom rules. I think we can whitelist that path as a solution. On my side, this morning I was testing onboarding a lot. Yesterday I was working on the brand step of onboarding—the first step after signup. I did some refactoring because it's a complex step. There's lots that can happen: the user can input an existing brand, pick similar brands, reject them, or add a brand that doesn't exist. So I broke it down into multiple controllers and multiple pages, each one simpler now. I did a lot of testing with Pedro's help. It looks good. I tested it in production when it went live. Stevie will want to take another look as well, but I think it's fine. I will do the cap on competitors and subcategories. I will also try not to do anything else—I was going to do some UI pushes, but I'll leave those in a branch until the peak of traffic settles down.

**Jose Farias:** That sounds good. We can deploy to preview instances, but let's take a slow day today in terms of merging and deploying to prod.

---

### Stevie's Launch Coordination & Support Setup (20:00 - 23:00)

**Stevie Kim:** I'll figure out the Customer.io thing. I just skimmed that thread. Looks like Daniel's out of office today, but I'll ping Jason and flag it for Marcel. I can't imagine we'll suspend launch for it. I'll keep an eye on the site. I need to create some automated messaging for Intercom. Just a heads up from past experience—I've gotten some weird messages on Intercom once people find out I'm a girl. So I'll forward any of those your way if they seem real. I should add that I want us to include ourselves in the amplification. We should be getting on LinkedIn, socials, etc. Also, about PostHog—I'll invite you guys. I don't know the rollout status exactly.

**Jose Farias:** I don't think I have PostHog access. Could you add me?

**Stevie Kim:** Yeah, I'll invite you guys. Whoever wants access, I'll give all of you access—we don't have to pay extra for that.

**Pedro Steimbruch:** The GrowthX Labs team has access.

**Stevie Kim:** Let me know if that doesn't work and I'll send an email invite.

**Estevão Mascarenhas:** Just before I wrap up—I added a block for personal emails. I added a comprehensive list of Gmail, Outlook, etc.—more than 100 entries. The thing is, it's very subtle how we tell the user. Right now it's just the label and placeholder saying "this is a work email during sign up." Because the message Clerk tells the user is just "this email is blocked from access," which is very generic. We might get support questions like "I cannot use my email here." Just a heads up on that.

**Jose Farias:** Sounds good.

---

### Final Wrap-Up: Jason's Inbox Setup & Intercom Automation (23:00 - 26:00)

**Jose Farias:** Jason, we're just about to wrap up. There is nothing on our minds that would block the launch. Did you have anything to go over?

**Jason Gong:** There's a thread on Customer.io apparently. We're just going to manually do it. Is there a way to send from @checkthat.ai or just Jason@checkthat.ai?

**Jose Farias:** I would have to check. Is anyone familiar with that setup?

**Pedro Steimbruch:** Yusuf said @checkthat.ai is added as an alias. Yusuf should be able to create an inbox for you guys.

**Jason Gong:** Yusuf was here earlier but just left. I'll call him. And then on Intercom—what about the welcome message?

**Stevie Kim:** I didn't realize we didn't have any automation for the first response. When I was at Algorithm, we set up at least a welcome message saying we'll get to you soon.

**Jason Gong:** I think the only impactful thing would be if we can get it to pop and say "Are you running into trouble?" I think it's somewhat hidden. There are corners you can run in the product.

**Stevie Kim:** Yeah, I'm sure you can have it pop up. I can look into it if I have time today.

**Jason Gong:** Is there any high priority thing for the launch? I want to make sure people have a good experience once they get in.

**Stevie Kim:** We're focused on making sure we have all eyes on the site, keeping everything stable and performant. I missed part of it because I was on the other meeting.

**Jose Farias:** Basically we're doing tiny merges today. We're aware the sources endpoint is slow sometimes for some workspaces. Our working theory is it happens when workspaces follow a lot of prompts. That's the larger thing. Other than that, it's tiny things like not choosing too many subcategories in onboarding. No big merges, no database migrations. Just keeping an eye on the system.

**Jason Gong:** I'll be planning around 9 AM but keep you updated.

**Jose Farias:** Sounds perfect. Thanks, y'all.

**Estevão Mascarenhas:** Bye-bye.

**Stevie Kim:** Bye.
