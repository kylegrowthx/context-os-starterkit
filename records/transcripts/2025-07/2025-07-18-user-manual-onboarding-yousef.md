# User Manual Onboarding - Yousef

<metadata>
date: 2025-07-18
time: 15:26 UTC
duration: 22 minutes
organizer: alice@growthxlabs.com
participants: Yousef Hamade, Alice Ochieng
fathom_recording_id: 75096965
fathom_url: https://fathom.video/calls/356243501
share_url: https://fathom.video/share/yzVY7-7gBswWx4JaxXYgSB3178d16jn8
source: fathom
enriched_on: 2026-03-03 14:22 UTC
</metadata>

---

## Summary

Yousef walked Alice through GrowthX's automated onboarding tool, which creates new hire accounts and sends welcome emails through an integrated workflow accessed via Slack bookmarks. The tool supports both automatic weekly runs (Thursdays at 9am PST) and manual onboarding for early access or off-cycle hires, with Tyler serving as a test case. During the demo, the team encountered and resolved a "duplicate user" error, successfully triaged an email delivery delay, and Alice agreed to monitor for Tyler's welcome email while Yousef committed to creating a Loom video documenting the process.

---

## Context

Yousef Hamade is walking Alice Ochieng through the manual onboarding process — specifically how to trigger early access for new hires who need to start before the automatic Thursday 9am PST run. This is internal GrowthX operations work. Yousef developed the onboarding automation tool and is training Alice (likely someone in people ops) on how to use it independently. The need arose because Tyler, a new hire starting in 2 weeks, requested early access to log in and prepare before his official start date.

---

## Relevance

- **To GrowthX Operations:** Documented workflow for manual onboarding now trainable to operations team. Yousef needs to create Loom video for self-service documentation. Identified system behavior issue (duplicate user error) that may need investigation for reliability.
- **To People Team:** Automation handles Google Workspace, Okta, Teams, Slack, and calendar invites in one workflow. Manual override available when early access or off-cycle starts are needed. Alice now has independent access to trigger onboarding as needed.

---

## Overview

- The onboarding tool automates account creation, welcome emails, and system access for new hires via a Slack-based interface
- Automatic onboarding runs every Thursday at 9am PST for hires starting within the next week
- Manual onboarding is needed for early access requests or employees added after the Thursday cutoff
- Tool encountered a "duplicate user" error for Tyler during demo, but successfully completed account creation and sent welcome email after resend

---

## Key Topics

### Onboarding Tool Walkthrough

  - Access via Slack bookmarks in the onboarding channel
  - "Refresh onboarding list" fetches latest user data from deal
  - "Onboard user now" initiates manual onboarding process
  - Tool sends authentication link via Slack (valid for 15 minutes)
  - Allows selection of one or multiple users to onboard
  - Verifies user information before proceeding

### Automated vs. Manual Onboarding

  - Automatic onboarding runs Thursdays at 9am PST for next week's starts
  - Manual onboarding needed for:
    1.  Early access requests (e.g., Tyler, starting in 2 weeks)
    2.  Late additions to the system (added after Thursday, starting before next auto-run)

### Troubleshooting

  - Encountered "Entity already exists" error for Tyler
  - Possible causes: manual account creation or system glitch
  - Resolution: Manually triggered email resend
  - Best practice: Wait \~1 minute for Slack confirmation; if issues persist, contact Yousef

### Welcome Email Process

  - System generates and sends welcome email automatically
  - Email contains essential onboarding information
  - Delay experienced in this session, but email eventually arrived
  - Both Alice and Yousef should receive copies for verification

---

## Action Items

- **Alice Ochieng (GrowthX)** — Monitor for Tyler's welcome email arrival in next few minutes and ping Yousef if not received
- **Yousef Hamade (GrowthX)** — Create a Loom video documenting the manual onboarding process for future reference
- **Alice Ochieng (GrowthX)** — Use manual onboarding tool only for off-cycle hires or early access requests; rely on automatic Thursday 9am PST runs for regular onboarding
- **Yousef Hamade (GrowthX)** — Investigate the cause of the "Entity already exists" error for Tyler to prevent future occurrences

---

## Transcript

**Alice Ochieng:** Hi, how are you?

**Yousef Hamade:** I'm doing well, how are you?

**Alice Ochieng:** I'm doing well as well.

**Yousef Hamade:** All right, so this should actually be pretty fast, I think. And I'd actually like you to drive, if you don't mind, so that way you can get the full experience. So if you go into the onboarding channel in Slack, at the top of the screen there's bookmarks — go ahead and click that.

**Yousef Hamade:** All right, so this is the onboarding tool. We're probably going to have to click that link a couple of times, but that's fine. The first thing we want to do is make sure that the onboarding tool has all the latest data. So go ahead and click "Refresh onboarding list."

**Alice Ochieng:** What is that?

**Yousef Hamade:** That one. Hit continue.

**Yousef Hamade:** This will take a minute. What this is doing is going out to Deal and fetching all of the latest users and things like that to make sure it has the latest data.

**Yousef Hamade:** Now that that's done, close this tab and then click the link again back in Slack. We'll launch the tool again, and this time you want to do "Onboard user now." Click the dropdown for "Onboard user now" and hit continue.

**Alice Ochieng:** Okay.

**Yousef Hamade:** Now this is going to ask who you are. Go ahead and select you from there. Hit the button.

**Alice Ochieng:** Okay?

**Yousef Hamade:** Now what's going to happen is you just got a Slack message. This is why I use Slack — it's faster than the GrowthX assistant. Just go ahead and click that link. That link is good for 15 minutes, and it's basically authentication to make sure that just anyone can't access this tool.

**Alice Ochieng:** Yeah.

**Yousef Hamade:** So now go ahead and hit the user to onboard. It allows you to onboard more than one user, but right now we're only going to onboard Tyler. So just click the check link next to Tyler and then hit continue.

**Alice Ochieng:** Okay.

**Yousef Hamade:** And then hit continue. Now verify the information — this is what it's going to create. Tyler at growthx.ai, so you can make sure that the user is right. Just continue.

**Alice Ochieng:** Okay.

**Yousef Hamade:** And that should be it. Now if you go check the onboarding channel in Slack. If you give this a minute, you should get a notification that the new hire creation is complete for Tyler. We'll just wait for it to complete. It's so quick and easy.

**Alice Ochieng:** You could have just sent me a Loom.

**Yousef Hamade:** I know. I need to go and create a Loom for these things.

**Yousef Hamade:** So now we're just waiting for it to run. While it's doing that, I'm going to go see what it's doing behind the scenes.

**Alice Ochieng:** How long does it take?

**Yousef Hamade:** It should only take like a minute to do it. The fact that it hasn't popped up yet makes me wonder if something broke, so I'm just making sure nothing broke. It's been a minute since I've done it like this.

**Yousef Hamade:** Is this still running? Okay, let me check.

**Yousef Hamade:** Oh no, we actually got an error.

**Alice Ochieng:** Oh, where?

**Yousef Hamade:** Error: "Entity already exists." Duplicate.

**Alice Ochieng:** The user already exists?

**Yousef Hamade:** That's what it thinks. It shouldn't exist already. Let me just take a look.

**Alice Ochieng:** Is it because the onboarding channel said Tyler is already onboarded?

**Yousef Hamade:** Well, he hasn't been onboarded yet. That's the thing. But he's now been created. So that is weird.

**Alice Ochieng:** Yeah.

**Yousef Hamade:** It's really weird. Unless someone manually went in and created him, but I don't know if they would do that.

**Alice Ochieng:** We could have gotten a notification if that happened, right?

**Yousef Hamade:** Yeah. So I don't know why it says Tyler was already created. But that's okay. I can check this really quick. It's fine. So again, I don't know how someone had already created him manually. But that's okay.

**Alice Ochieng:** So do we have to do what we did before all over again?

**Yousef Hamade:** No. It's complete now. It says it's complete, so you should be okay now. Again, I'm just not sure why it said his account already existed. But that's okay.

**Alice Ochieng:** Sorry, I had a question. At what point will it send the welcome email?

**Yousef Hamade:** It just created the welcome email, so he should have gotten it just now.

**Alice Ochieng:** Okay. I usually see it, but I can't see it today.

**Yousef Hamade:** I don't know why. Let me keep checking because it may have done something else unusual. The system says it sent the email — add to calendar, invite Slack, add user to Teams, send email. Yeah, so it said it sent the email. Maybe it's just taking a minute for it to come in.

**Alice Ochieng:** Okay.

**Yousef Hamade:** Yeah, so it says it sent the email. I don't know why it thought there was already a user created for him, or who might have manually created the user in Google, but it should be complete now. It's just a matter of waiting for the email to come through, because it does say it sent it.

**Yousef Hamade:** If it doesn't come through in the next few minutes, just let me know and we can resend that.

**Alice Ochieng:** Yeah, I'll ping you.

**Yousef Hamade:** Did we get the welcome email yesterday from Suleman?

**Alice Ochieng:** Yeah, I started working on that yesterday.

**Yousef Hamade:** Yeah, the one for Tyler should be fine. It does say it sent the email.

**Alice Ochieng:** Yeah, I'll keep an eye out and let you know if it didn't come. Did you see it on your side or don't you get the email?

**Yousef Hamade:** I should be getting it too and I have not gotten it yet. But I got the one yesterday from Suleman. I have not gotten the one for Tyler yet. I can always do this — give me one second.

**Alice Ochieng:** Okay.

**Yousef Hamade:** I'm just going to trick it to send again, so worst case he gets a duplicate.

**Alice Ochieng:** Okay, yeah, I can see it now.

**Yousef Hamade:** Okay, awesome. Yeah, I don't know if that's the new one or the original one just finally came through.

**Alice Ochieng:** Yeah, but at least we're sure it went through.

**Yousef Hamade:** Yeah, sounds good. So I don't know why this was so quirky with him, but it should be all set going forward. If you run it and you run into problems like this, let me know and I'll take a look at it. But within a minute, it should come back to the Slack channel and say everything's good. If it doesn't, reach out to me.

**Alice Ochieng:** Yeah, and last question. Should I be doing this every Thursday because it sends the notification every Thursday?

**Yousef Hamade:** No, it automatically does that at 9am PST every Thursday for people who are going to start in the next week. The only time we need to do this is if we want someone to create the accounts sooner. Because Tyler doesn't start for another two weeks, his account won't be created until next Thursday. But in this case, he said he wants to log in and have access beforehand, and we agreed that's fine. So we can trigger it sooner.

**Yousef Hamade:** The other time we would need to do this is if someone was added today and they're going to start Monday or Tuesday or Wednesday of next week. We'd add them to Deal and then use this to create their Google and Okta accounts. So it's only when we need to do something off-cycle.

**Yousef Hamade:** If they start within the next week and they're already in the system on Thursday, it'll create them automatically Thursday morning. But if they're not in the system yet on Thursday, or they've got a much later start date and we want to create them sooner, we just go in here, run the tool, and it'll create them now.

**Alice Ochieng:** Got it.

**Yousef Hamade:** Thanks, Alice. Have a good evening and have a good weekend.

**Alice Ochieng:** Bye.

**Yousef Hamade:** Bye.
