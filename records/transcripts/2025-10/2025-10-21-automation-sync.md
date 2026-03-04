# Automation sync

<metadata>
date: 2025-10-21
time: 15:00 UTC
duration: 23 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt, Sydney Go
fathom_recording_id: 95635954
fathom_url: https://fathom.video/calls/448924600
share_url: https://fathom.video/share/YjsrodvPk8C4kvGtMTXxPfGc8XkWufBB
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

Bailey Seybolt (GrowthX) worked with Sydney Go to solve a critical workflow problem: Hyperexponential (the client) cannot access Google Docs, so their content review process is fractured across Docs, Teams, and Notion. The solution involved three key components: using Zapier to automate the Airtable-to-Notion workflow since Airtable's native automation doesn't write to Notion, leveraging Airtable Interfaces to let clients approve content without paid editor seats, and setting up Slack notifications with direct Airtable links to streamline handoffs between the CMS and Sydney.

---

## Context

Sydney Go is a specialist at GrowthX who manages complex content automation workflows for multiple clients, including Hyperexponential and LightSource. Bailey Seybolt recently inherited the Hyperexponential account midway through a content strategy sprint and is working to standardize processes that Sydney pioneered. Hyperexponential operates under strict tool constraints — no Slack, no Google Docs, email-only communication — which forces unconventional solutions. The meeting focused on solving a foundational problem: how to create a unified content production workflow (planning → SME review → final approval → external handoff) when the client's technical restrictions eliminate standard tools like Docs and Slack.

---

## Relevance

**To GrowthX Delivery:**
- **Zapier as the bridge for Notion automation:** Airtable's native automation cannot write to Notion, making Zapier essential. Sydney has already set this up for LightSource; Bailey can adapt the existing setup to Hyperexponential's workflow (create Google Doc in Airtable, then push to Notion on status change).
- **Airtable Interfaces for client approvals without paid seats:** Clients can be granted editor access to interfaces while remaining commenter-level on the base, avoiding Airtable's per-seat costs. This is already live for LightSource; Bailey needs to implement for Hyperexponential's content review.
- **Separation of internal (Google Doc) and external (Notion) drafts:** Risk mitigation to prevent accidentally sending clients internal drafts. Sydney has been hit with this; Bailey is designing it in from the start.
- **Slack notifications with Airtable links for faster handoffs:** A simple automation that sends a Slack message with a direct Airtable record link lets the CMS update status without searching for records. Accelerates review cycles.

**To GrowthX Business Development:**
- **Account health signal — Hyperexponential constraints:** Client's inability/unwillingness to use standard tools (no Slack, email-only) is a friction point that indicates either very conservative internal processes or potential integration challenges. May affect future feature adoption.
- **Expansion opportunity — automation workshop:** Sydney and Carrie are running a workshop on these automation patterns (Airtable → Notion → Slack). This could become a service offering or at least a training asset for onboarding new clients.

**To CheckThat:**
- No direct relevance to AI visibility or AEO identified in this meeting.

---

## Overview

- **Automate the Airtable → Notion workflow using Zapier.** Airtable's native automation cannot write to Notion, making Zapier the necessary bridge.
- **Use Airtable Interfaces for client approvals.** This enables clients to interact with the database without needing paid editor seats, which they cannot access.
- **Create separate "Internal Draft" (Google Doc) and "External Draft" (Notion) links in Airtable.** This prevents sending clients the wrong version and is triggered by status changes.
- **Set up a Slack notification with a direct Airtable link.** This allows the CMS to instantly update a record's status, streamlining the review handoff.

---

## Key Topics

### Problem: Disjointed Content Workflow

  - A client (Hyperexponential) cannot access Google Docs, forcing a manual, disorganized workflow across Notion, Teams, and Google Docs.
  - **Goal:** Create a single source of truth in Airtable by automating content creation and status updates in Notion.

### Solution 1: Airtable → Notion Automation

  - **Tool:** Zapier, as Airtable's native automation cannot write to Notion.
  - **Workflow:**
    1.  **Trigger:** An Airtable record's status changes (e.g., "Ready for Notion").
    2.  **Action:** Zapier creates a new Notion page and populates it with content from the corresponding Google Doc.
    3.  **Action:** Zapier updates the original Airtable record with the link to the new Notion page.

### Solution 2: Streamlined Client Approvals

  - **Problem:** Clients with "Commenter" permissions cannot interact with Airtable fields (e.g., check an "Approved" box). Upgrading them to "Editor" is not allowed, as it requires a paid seat.
  - **Solution:** Use an Airtable Interface.
      - **Mechanism:** Share an interface with "Editor" access, while the client's base permission remains "Commenter."
      - **Result:** The client can interact with the interface's fields without needing a paid seat.

### Solution 3: Efficient Handoffs

  - **Problem:** Manually finding and updating records in Airtable for status changes is inefficient.
  - **Solution:** Use a Slack notification to streamline the handoff.
      - **Mechanism:** An automation sends a Slack message with a direct link to the Airtable record.
      - **Result:** The CMS can click the link and instantly update the status, eliminating the need to search for the record.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Add Airtable columns for Internal Draft Link and External Draft Link to separate internal (Google Doc) and external (Notion) drafts for Hyperexponential, preventing wrong versions from being sent to clients

---

## Transcript

**Bailey Seybolt:** Yeah, you're actually right on time, so. This meeting is being recorded. So, basically the background is that we have a client who can't access Google Docs, and they also have a really extensive subject matter expert review of every piece of content right now. It's just been a disaster because some people are in Google Docs, and they're creating copies of Docs in their Google Teams, and putting stuff in Notion.

**Bailey Seybolt:** And what I've done is create a space in Notion where we can route all their content. But I think the challenge is connecting the content OS.

**Bailey Seybolt:** So I think the way I've set it up now, I just did this yesterday, is that the planning would be stuff that's in production right now or about to be in production, because they want their subject matter experts to be able to add comments to things that might be closer to product. And then it would move into subject matter expert review, and then it would go to the final CMO review.

**Bailey Seybolt:** So what I've been trying to do is when we move something, basically to create the article. Like, I don't even know if it's possible in Airtable to have it automatically create the document when the status changes, like you would in Google Docs. And then also have it so that as it moves through, the status gets updated in Airtable, just so there's always one source of truth.

**Bailey Seybolt:** I've used both Airtable and Notion. I'm not a super pro user. So if it feels like there's a better way to organize this, I'm open to anything.

**Sydney Go:** Oh, yeah, 100% you can. So basically, Airtable's automation is one way — it can automate things in Notion, but Notion cannot automate things in Airtable. So we can use Zapier to kind of bridge those two things. I don't think it'll take too much, to be completely honest with you.

**Sydney Go:** What I did for my CMS was, anytime I added anything to idea pending, it would go into here. These are all automations from Airtable. So I know that this is 100% possible in Zapier. I'm almost certain it's possible in Airtable because I have the same setup for Google Docs now. I just have Airtable put it into the Google Doc that it creates, and then it also keeps a record in Airtable.

**Bailey Seybolt:** And did you do this directly or did you use Zapier?

**Sydney Go:** I did this before Airtable had the AI automations. So I know Zapier works.

**Bailey Seybolt:** And when you're doing editing, do you do it in Google Docs, or do you do it directly in Notion with that setup?

**Sydney Go:** I've been doing it in Google Docs. Most my customers are okay with Google Docs. And I actually had one of my customers who wasn't okay with Notion or Airtable.

**Bailey Seybolt:** I feel like no Slack, no Google Docs. That would drive me crazy.

**Sydney Go:** Well, there's that one customer that doesn't do Slack, right?

**Bailey Seybolt:** Just email? That's the same customer?

**Sydney Go:** Oh, is this Hyperexponential?

**Bailey Seybolt:** Yes, it's Hyperexponential.

**Sydney Go:** Yeah, so when I was trying to set this up yesterday, their AI assistant wasn't working either. So I couldn't tell if I was breaking things or if it just couldn't do what I was asking. My assumption was I'd have to go through Zapier.

**Sydney Go:** Then you would have to do it through Zapier. What do you want to do to create the Notion and Doc? Do you want it to pull from a Google Doc, or just for recording purposes?

**Bailey Seybolt:** Can it pull from Airtable? Actually, if we're editing in Google Docs, it probably makes more sense to pull from Google Docs. I'm trying to figure out how we can eliminate having Airtable, then doing internal editing on Google Docs, and then having to move everything to Notion.

**Sydney Go:** Maybe there's no way around that. That might just be what we have to do. So the way you want to do this is you're going to have Airtable watch your records so that every time you update a record with a specific status, it creates an item in Notion, right?

**Bailey Seybolt:** Yep.

**Sydney Go:** And then you can put in the name, the title, and the content. The way I would set this up is that as soon as it creates — as soon as it senses something — you would want to create a Google Doc. So I would just create a document in a specific folder. And then here's where you'd put in the markdown. You do this thing first, and then you would insert all the stuff that you want. And then I think there's a way for you to add another listener to filter for another status change. So if it goes into "move to Notion" or something, instead of having it create data from text, you'd create a data source item.

**Sydney Go:** So instead of having the data source here, you can select the Google Doc that you created, and then use the content from there. Just use the text.

**Bailey Seybolt:** Oh, yeah. Okay.

**Sydney Go:** So the content can just use the text in here and that'll port everything over into Notion. And then if you want a record in Airtable, what I have set up for LightSource is I have a separate table for internal and external drafts. So what you can do is after the doc is created, link it back to Airtable and add it to that column. So create the Google Doc and then add the internal link to Airtable. And then when you move it to the next status, like "Ready for Notion" or "Ready for Review," create the Notion, append all the text from the Google Doc, and add the link to Notion back into Airtable. That's something you can do through Zapier.

**Bailey Seybolt:** Can I ask you one question while we're in your Airtable? I see you have the approval checkmark. Have you figured out how to let clients check it? We tried to set that up but I couldn't figure out how to let clients interact with that column.

**Sydney Go:** When you go to publish or launch the interface, click the share button. You should be able to see who has access. This is probably still on commenter or view only.

**Bailey Seybolt:** This was for Relay. I thought I was being smart creating less work for them, and then the box didn't work.

**Sydney Go:** What's happening is your permissions are all on commenter. We're not actually allowed to switch it to editor.

**Bailey Seybolt:** Because they have to pay for the seat?

**Sydney Go:** Yes, because you have to pay for the seats. Which is why we usually put an interface in here.

**Bailey Seybolt:** So if I add an interface, then they can interact with it that way instead?

**Sydney Go:** Yes. So what I have set up for LightSource is I only share the interface. They have editor access, but only to the interface and not the base or the data. They only have commenter permission on the actual data source, but on the interface they have editor status. And I think it's just easier for them to see what articles are ready for review. They can go in and tell you immediately if they want it revised or published. So it's easier for us as well.

**Bailey Seybolt:** Just keep it all in one place. That's way easier.

**Sydney Go:** Now the next step is for them to use it, because they didn't watch the video I sent them on how to use it. I spent 30 minutes automating everything and setting it up for them. But when we got on the call they said, "I don't know how to use this." And I was like, the video is two minutes.

**Bailey Seybolt:** I feel like for Hyperexponential, I'm not even going to bother. There's no way they're going to engage. They need everything pushed to email in their inbox to interact with. But they do use Notion.

**Sydney Go:** That seems weird, especially to be Notion users but not use Slack.

**Bailey Seybolt:** Yeah. Notion isn't the simplest interface. It's such a blank slate, which is what's amazing about it, but it's easy to get lost in there.

**Sydney Go:** I love Notion. But I also like nerding out about these tools. If I wasn't on Slack, I mean if I was on email, I feel like that would be crazy.

**Bailey Seybolt:** Exactly. To not be on Slack and be doing emails feels crazy. Okay, well, thank you. This was super helpful. I'm going to try to set this up. Maybe I'll bring my questions to you when I have them.

**Sydney Go:** The other thing you may want to do, which just popped into my mind, is if you want to make it easier on your CMS to move statuses — especially if you're setting up the trigger for porting everything from Google Doc to Notion — is in the internal channel I have it set up so that it tells whoever is handling it when something is ready. It has a link to the draft and a link to Airtable. And then if they click the Airtable link, it automatically opens an Airtable record so they can immediately move to the next stage without having to search for the record.

**Bailey Seybolt:** I think that's what I have set up. I really like it. But I think I should make a new column for the internal and external drafts so we don't risk sending clients the wrong thing.

**Sydney Go:** I learned that the hard way. I sent an internal draft and they said, "Oh, we can't access it." And I was like, oops, wrong link.

**Bailey Seybolt:** With Hyperexponential, their content is super focused right now. Every keyword feels like a slight variation of itself. And right now I'm trying to keep track of what article is what. I'm just waiting for us to make a dumb mistake.

**Sydney Go:** No, I'm pretty sure you're great. Honestly, all the new team members seem really solid. Both you and Katya are doing amazing. I can't believe how fast you've adjusted and started producing so much content and performing at such an amazing rate already.

**Bailey Seybolt:** Well, it's nice to hear that. It doesn't feel like that from the outside.

**Sydney Go:** Katya keeps saying that too. You're an engine. I don't know what else you can improve here.

**Bailey Seybolt:** Oh, there's space.

**Sydney Go:** Well, you know, all of us have space.

**Bailey Seybolt:** All right, well, thank you for this. I'm going to attempt to build this myself. And then maybe I'll reach out when I have questions or if anything goes wrong.

**Sydney Go:** I'm sure nothing will go wrong. But if you need what I had already set up before, it's in the tools sign-in. There should be something in one password.

**Bailey Seybolt:** Okay. I'll try it from there. Thank you so much.
