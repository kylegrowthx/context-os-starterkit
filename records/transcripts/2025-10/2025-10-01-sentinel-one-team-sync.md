# Sentinel One Team - Sync

<metadata>
date: 2025-10-01
time: 16:01 UTC
duration: 7 minutes
organizer: nicolas.castellanos@growthx.ai
participants: Nicolas Castellanos, John Nederveld, Joery van Druten
fathom_recording_id: 91152060
fathom_url: https://fathom.video/calls/426456014
share_url: https://fathom.video/share/ndJCX4eAcBo3tWSMyRers6syJ_2hkG5y
source: fathom
enriched_on: 2026-03-02 20:30 UTC
</metadata>

---

## Summary

Nicolas Castellanos onboarded to the Sentinel One CVE database project, reviewing technical stack requirements (Next.js, TypeScript, Tailwind CSS, vanilla React, Vercel) and access workflows. John Nederveld committed to expediting Nicolas' GitHub access, setting up a separate Algolia index for the CVE database with automation from ContentStack, and including Nicolas' name in future access request summaries. Nicolas will start development in parallel while awaiting GitHub access and create a new ContentStack branch for testing new content types.

---

## Context

Nicolas Castellanos is being onboarded as a developer on GrowthX's Sentinel One project, a CVE database platform managed by John Nederveld and Joery van Druten from Sentinel One. The sync focused on unblocking Nicolas with the access credentials and technical documentation he needs to begin work while infrastructure provisioning is underway. This is part of a broader onboarding wave at Sentinel One, with multiple contractors (Marcus) also being added simultaneously.

---

## Relevance

- **To GrowthX Delivery:** Defined tech stack for Sentinel One project (Next.js + TypeScript + Tailwind CSS + vanilla React on Vercel); Nicolas can start development work immediately; established ContentStack + Algolia workflow for content management and search indexing.
- **To GrowthX Business Development:** Nicolas assigned to active Sentinel One engagement; Sentinel One managing multiple contractor onboardings concurrently, indicating scaling of project scope; team receptive to process improvements (e.g., adding names to access request summaries for tracking).

---

## Overview

- GitHub access for Nicolas pending; John to expedite request
- Project tech stack: Next.js, TypeScript, Tailwind CSS, vanilla React, hosted on Vercel
- ContentStack branch creation approved for Nicolas' new content types
- Algolia integration planned for CVE database with separate index

---

## Key Topics

### Access Management

  - John experiencing Slack login issues (SSL loop problem)
  - GitHub access for Nicolas and Marcus pending
      - John to submit/expedite Nicolas' request
      - Marcus' access part of IT cycle, expected Monday
  - ContentStack access already granted to Nicolas
  - Algolia access not required; John to set up separate index

### Project Technical Stack

  - Frontend: Next.js with TypeScript
  - Styling: Tailwind CSS (no component libraries like Shadcn)
  - State Management: Vanilla React (no additional libraries)
  - Hosting: Vercel platform

### ContentStack Workflow

  - Nicolas created testing environment in ContentStack
  - Approval given to create new branch for content types
  - Option to add new content types to main branch if non-disruptive
  - Automation exists to populate Algolia index from ContentStack

### Algolia Integration

  - Separate index to be set up for CVE database
  - No direct login needed for Nicolas
  - Automation to be configured for populating index from ContentStack
  - Existing API connection can be leveraged

---

## Action Items

**John Nederveld (Sentinel One)**
- Submit GitHub access request for Nicolas. Ping IT contact to expedite.
- Add Nicolas' name to ContentStack request summary/title for easier tracking.
- Set up Algolia index for CVE database. Create API key for Nicolas.

**Nicolas Castellanos (GrowthX)**
- Create new branch in ContentStack for testing new content types.

---

## Transcript
**John Nederveld:** Hey, how are you doing, Nick?

**Joery van Druten:** I was just going to text him because I didn't see you on Slack.

**John Nederveld:** No, my Slack has locked me out.

**John Nederveld:** It's like throwing me in a loop with the SSL.

**John Nederveld:** I'm getting annoyed.

**John Nederveld:** How's it going?

**Nicolas Castellanos:** You're good.

**John Nederveld:** How are you?

**John Nederveld:** I'm doing all right.

**Nicolas Castellanos:** Nice.

**Nicolas Castellanos:** Did you get the GitHub request?

**Nicolas Castellanos:** I think that was the access to GitHub.

**Joery van Druten:** For you or for the other person?

**Nicolas Castellanos:** For me and Marcus.

**Joery van Druten:** Yeah, so the thing with Marcus is I put in the IT request. But they run in this cycle, so I don't get that until Monday.

**Nicolas Castellanos:** Okay, that's fine.

**Joery van Druten:** And then I can move on.

**Joery van Druten:** But I thought, John, didn't you put the GitHub request for Nicolas in?

**John Nederveld:** I can't remember.

**John Nederveld:** might not have.

**John Nederveld:** Which is my fault, if so.

**Nicolas Castellanos:** That's fine. If it's going to take some more time, can you tell me which kind of tech you're running so I can start working on something?

**John Nederveld:** Yeah, so it's all Next.js, and it's hosted on Vercel. So if you just build with Next and TypeScript, then any UI libraries? ChatGPT?

**Nicolas Castellanos:** No, we're using Tailwind for our styles.

**John Nederveld:** Tailwind classes are cool, but we're not using Shadcn or any component libraries.

**Nicolas Castellanos:** Okay, and then for state management?

**John Nederveld:** Just React. Yeah, vanilla React stuff.

**Nicolas Castellanos:** Okay, I'll start with that, and then I'll get it into the repo when I get access.

**John Nederveld:** Okay, I will open that as soon as I get this, and I'll ping our contact on the IT side to expedite it.

**Nicolas Castellanos:** And the other thing—can I create another branch inside ContentStack? I created my own testing environment for testing, but I'm ready to send content types. I don't want to send it to the main branch.

**John Nederveld:** Yeah, you can create a branch, that's okay.

**John Nederveld:** If it's a new content type and doesn't mess with existing content types, you can just add it to the main branch. But if you want to keep it separated, that's great.

**Nicolas Castellanos:** Yeah, I think that's better.

**Nicolas Castellanos:** That's all I have. Do you have anything?

**John Nederveld:** No. I'll get you that GitHub access—making a note of that. Once you have access, we can look at things visually, do some UI, UX, QA work, and move forward. Let me know if there's anything else you need and I'll unlock you.

**Nicolas Castellanos:** Cool.

**John Nederveld:** That's it for me. Anything on your end?

**Joery van Druten:** We need to add a user to ContentStack. When you submit that request, can you put Nicolas' name in the summary and title?

**John Nederveld:** Of course.

**Joery van Druten:** It's easier to find. We have so many of these requests—copy and paste, copy and paste. All the titles blur together.

**John Nederveld:** Noted.

**Joery van Druten:** Nicolas, we have so many people onboarding from all over. I thought we'd done this already.

**Nicolas Castellanos:** I should have pinged you earlier, but I figured it was just the process taking time. It's fine.

**Joery van Druten:** Yeah, yeah. You're aware of the red tape at Sentinel One.

**Joery van Druten:** Okay, cool. Actually excited to see some work coming in.

**John Nederveld:** Yeah, that's really cool. It's a cool project.

**Nicolas Castellanos:** Yeah, it's nice.

**Joery van Druten:** All right.

**Nicolas Castellanos:** One more thing before I forget—do I need access to Algolia, or can we sync that later?

**John Nederveld:** Yeah, I can set up an index for you. You won't need to log in. We'll set up a separate index for the CVE database with automation from ContentStack to populate it. We already have that connected for another part of the site, so just another API key for the index.

**Nicolas Castellanos:** Awesome. Thank you.

**John Nederveld:** Have a good one.

**Nicolas Castellanos:** Have a great one. Bye.

**Joery van Druten:** Bye.
