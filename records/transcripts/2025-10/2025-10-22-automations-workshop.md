# Automations Workshop

<metadata>
date: 2025-10-22
time: 18:31 UTC
duration: 52 minutes
organizer: Bailey Seybolt
participants: Bailey Seybolt, Carrie Chowske, Ehtisham Hussain, Jenn Peters, Jessalynn Jones, Katya Luscomb, Marisol Smith, Sydney Arin Go, Nathalie, Nika Narimanidze
fathom_recording_id: 96079344
fathom_url: https://fathom.video/calls/448502127
share_url: https://fathom.video/share/eCVuLNt48CsofBvvUwyY892ZbR56wD-k
source: fathom
enriched_on: 2026-03-02 10:15 UTC
</metadata>

---

## Summary

GrowthX's content operations team shared Airtable and Google Workspace automation patterns for client approval workflows, CM handoffs, and content production tracking. Carrie Chowske introduced a centralized Notion database to catalog reusable automations by complexity level, while Sydney Arin Go demonstrated her full automation suite for LightSource, including client-facing interfaces, Slack notifications, and automated Google Doc generation. Key technical challenges discussed: using personal Google Drive folders to work around shared-drive permission restrictions, conditional Slack tagging for specific editors, and CSV parsing for content export from Atlas.

---

## Context

This is an internal GrowthX team workshop on content operations automation. Carrie Chowske, a delivery leader managing content production workflows, organized the session to document and standardize automation patterns being developed across different client accounts. Sydney Arin Go, who manages content operations at GrowthX, demonstrated advanced automation setups being used for high-volume content clients like LightSource. The team works with Airtable as their content management backbone, Slack for notifications, Google Workspace for document creation, and Notion for internal documentation. This meeting reflects GrowthX's shift toward process automation to reduce manual toil and improve transparency for clients in multi-week content sprints.

---

## Relevance

**To GrowthX Delivery:**
- Standardizing automation patterns (Airtable interfaces + Slack notifications + Google Docs) reduces manual setup per client and improves onboarding speed for new content accounts
- The shared Notion database of automations by skill level (beginner/intermediate/advanced) creates a reference library to upskill delivery teams faster
- Key technical workaround: using personal Google Drive folders with shortcuts to shared drives solves a critical blocker where Airtable automations lack write access to client shared drives
- Client approval workflows using Airtable interfaces bypass permission issues and eliminate comment-based approval chaos

**To GrowthX Business Development:**
- Demonstrated client-facing automation features (status visibility in interfaces, Slack pings, clickable briefs) improve perceived service delivery quality and client experience
- Sydney's LightSource setup shows the operational sophistication GrowthX can bring to content management, valuable for differentiation against competitors
- Multi-client automation standardization creates efficiency gains that improve margin on retainer accounts

**To Process and Tools:**
- Team flagged pain points with existing tools: Looker reporting unreliability (Carrie noted it "never loads correctly"), absence of analytics in Atlas, manual Markdown formatting in Google Docs
- Opportunity to build or integrate better reporting/analytics layer for content performance (Carrie mentioned excitement if Atlas adds this feature)
- Potential for AI agents to auto-summarize content exports from Zapier/Make (Marisol flagged this as next-step need for changelog automation)

---

## Overview

- **Automate Client Approvals:** Use an Airtable Interface with a simple checkbox to trigger status changes (e.g., `Approved` → `Ready to Start`), bypassing client editing permissions and simplifying their workflow.
- **Streamline CM Handoffs:** An Airtable automation can auto-generate a Google Doc brief from a template and ping the assigned CM in Slack with direct links, eliminating manual setup and reducing mental load.
- **Bypass Drive Permissions:** To enable automations to create Google Docs, create a folder in a personal or team account and add a shortcut to the client's shared drive. This works because automations often lack write access to shared drives.
- **Tag Editors in Slack:** To tag a specific editor, use a conditional automation that watches the `Assigned To` field. Each condition maps a specific editor's name to their Slack User ID, which is then used in the message.

---

## Key Topics

### Automating Client Approvals with Airtable Interfaces

  - **Problem:** Clients need to approve content but lack the editor permissions required to change statuses or check boxes, forcing them to leave comments instead.
  - **Solution:** Create a client-facing Airtable Interface with a simple checkbox.
      - **Mechanism:** An Airtable automation watches the checkbox. When checked, it automatically updates the record's status (e.g., `Approved` → `Ready to Start`).
      - **Permissions:** This works because clients can interact with Interface elements (like checkboxes) even with limited access, as it triggers an automation rather than a direct edit.
      - **Testing:** Use the "View as" feature to confirm the client's exact permissions and experience.

### Streamlining CM Handoffs with Airtable & Slack

  - **Problem:** Manually creating Google Doc briefs and notifying CMs is time-consuming and disruptive.
  - **Solution:** An Airtable automation that triggers on a status change (e.g., `In Production`) to:
    1.  **Create a Google Doc:** Generates a brief from a template, pulling data (keyword, description) from the Airtable record.
    2.  **Notify CM in Slack:** Pings the assigned CM with a direct link to the new Google Doc and the Airtable record.
  - **Workaround for Drive Permissions:**
      - **Issue:** Airtable automations often lack write access to create files directly in shared Google Drives.
      - **Fix:** Create the automation's target folder in a personal or team account (e.g., `team@growthx.ai`) and add a shortcut to the client's shared drive. The automation writes to the personal folder, which is then accessible via the shortcut.

### Tagging Editors in Slack Notifications

  - **Problem:** An Airtable automation sends assignment notifications, but it fails to tag the assigned editor in Slack.
  - **Solution:** Use a conditional automation that maps editor names to their Slack User IDs.
      - **Mechanism:** The automation watches the `Assigned To` field. For each possible editor, a separate condition checks their name and sends a message using their specific Slack User ID.
      - **Finding the ID:** Get a user's ID by clicking their profile in Slack and selecting "Copy ID."
      - **Formatting:** Use the format `<@U1234567890|Name>` to create a clickable tag in the Slack message.

### Automating Content Export & Formatting from Atlas

  - **Problem:** Exporting content from Atlas (which uses Markdown) and formatting it into client-ready Google Docs is a manual process.
  - **Solution:** A multi-step workflow using Google Apps Scripts.
    1.  **Export:** Export content from Atlas as a CSV.
    2.  **Parse:** An Apps Script splits the CSV data into columns based on H1s (`#`).
    3.  **Generate Docs:** Another Apps Script creates individual Google Docs from the parsed columns.
    4.  **Format:** A final Apps Script converts the raw Markdown in the new Docs into plain text.
  - **Simpler Alternative:** For basic Markdown, you can skip the final script. After creating the Doc, right-click and select "Paste Markdown" to automatically format the content.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Confirm Airtable Interface seats/permissions for clients

**Carrie Chowske (GrowthX)**
- DM Sydney re: Markdown paste in Google Docs
- Schedule recurring automations office hours/jump-in sessions
- Post automations Notion link in Slack

**Ehtisham Hussain (GrowthX)**
- Implement Airtable→Slack @-tagging for InBit reviewers; test w/ Sydney's screenshot

---

## Transcript
**Carrie Chowske:** Yeah, it's like some, it's, yeah.

**Carrie Chowske:** All right, well, I'm gonna, I'm gonna start, I'll go ahead and get started while we wait for Sydney, because she's going to show us her automation, because I'm also, I also think hers is really, really useful.

**Carrie Chowske:** I, I don't know if you guys saw this, I'm going to share this really quickly, is I, I'm I've dropped this link in the, in the, in our Slack channel.

**Carrie Chowske:** I'll make sure that it's a little more visible, but I basically just set this up so we can drop in like our automations and literally, but we can sort them.

**Carrie Chowske:** So like, if you're looking for something that's like, how the heck do you deal with this?

**Carrie Chowske:** You know, we can kind of sort them.

**Carrie Chowske:** This just goes to the tutorial that's already in Notion.

**Carrie Chowske:** So if you've already got something somewhere, it's just, you know, really great way to kind of get them all in one place.

**Carrie Chowske:** And I didn't do the upvote.

**Carrie Chowske:** I as a popularity contest, I did it really as a, if you try this automation out and you decide to incorporate it into your daily, like, work routine, give it an upvote because that'll tell us, like, I think that'll give us some good information on, like, maybe we should standardize some of these things or, like, you know, maybe we can convince people to make them standard.

**Carrie Chowske:** No, but just, and, and then the beginner, intermediate, and advanced categories that I picked are really just based on, like, how much experience you have with those types of, like, software, so like, like this one here uses linear, I feel like what Joe has created, I don't know if anybody else saw this, but what Joe has created looks to me like you'd need to be pretty familiar with linear to replicate what she's done, but it's not going to be too common, but it might be really easy for somebody who's really familiar with linear.

**Carrie Chowske:** I hate linear, the way most of you hate Airtable, so I don't like this at all, and I'm going to close it now, but I'm sure Joe does something very genius.

**Carrie Chowske:** The one that I...

**Carrie Chowske:** What was going to share was literally my, I've kind of created a faux content calendar for myself.

**Carrie Chowske:** And I say faux because I don't have like a set schedule for, like it's not like I have an actual calendar of what date these things are going to publish or anything, but I do manage like how I decide week to week, like what I'm going to sign out and like what, you know, to get all that management done.

**Carrie Chowske:** Um, I, because we don't really operate that way and the content OS isn't designed this way, I kind of did a little workaround where I created a, um, uh, what do you call it?

**Carrie Chowske:** Um, I'm trying to remember what your table calls them, but basically a column, a column.

**Carrie Chowske:** I'm just going to call it a column.

**Carrie Chowske:** Does that work for everybody?

**Carrie Chowske:** Um, where you can actually see, um, sorry, I'm trying to talk and think at the same time and it's just not going to work.

**Carrie Chowske:** So what we're going to do is we're going to stop talking for two seconds and we're going to open the thing we're trying to open.

**Carrie Chowske:** So, what I have for my clients is I have this, like, it's just literally another column that I've added to the single select.

**Carrie Chowske:** It's like the easiest thing in the world.

**Carrie Chowske:** And I have these labeled, like, current week, next week, buffer, and pool.

**Carrie Chowske:** I know what these mean, and the client knows what these mean.

**Carrie Chowske:** That's all that matters here because this is just for you.

**Carrie Chowske:** You're not messing up anything in Airtable by doing this.

**Carrie Chowske:** It's just adding a field that anyone can hide in any view if they don't want to see it.

**Carrie Chowske:** So you're not screwing anything up.

**Carrie Chowske:** And literally, I know what they mean.

**Carrie Chowske:** Now, I've gotten better at this since then because the problem is you can't set the order, right, because you've already got a status column.

**Carrie Chowske:** In Airtable, have to, like, it only allows one status at a time.

**Carrie Chowske:** So I can't tell it which one's the first status and which one's the last status.

**Carrie Chowske:** So I alphabetize them.

**Carrie Chowske:** So that's why they're current week, next week, on deck and up next.

**Carrie Chowske:** Because alphabetically, they'll be in the right order for me, right?

**Carrie Chowske:** Current week and next week are really obvious.

**Carrie Chowske:** And those are the ones that I usually, only ones that I have, the CMs have visibility to. Those are the ones that I'll assign them at those stages.

**Carrie Chowske:** I don't assign them before that, so they don't have to worry about what my code means.

**Carrie Chowske:** I have my own secret code for me.

**Carrie Chowske:** No one else needs to know.

**Carrie Chowske:** It's not going to hurt anything if somebody stumbles upon it.

**Carrie Chowske:** And then from there, I actually have an automation set up that moves all of those forward at like 2 a.m.

**Carrie Chowske:** Saturday.

**Carrie Chowske:** So when, at the end of the week, it changes that priority from current week to published.

**Carrie Chowske:** And I just, it's literally like, this is one of the easiest things you can do because it's doing it at a scheduled time and it can monitor like when certain fields change.

**Carrie Chowske:** The AI assistant in Airtable is really good actually at creating these automations too.

**Carrie Chowske:** So you can actually just tell it what you want to do and it'll probably create it for you.

**Carrie Chowske:** But that's my, that's probably my biggest trick because I have a bunch of CMs that they're, their Monday morning is my Sunday evening and you better believe I'm not giving up my Sunday evening to assign things to them.

**Carrie Chowske:** I'm sorry.

**Carrie Chowske:** And I don't always have time on Friday, or sometimes the client hasn't approved something, so I can't assign it.

**Carrie Chowske:** So I do that, it's done automatically.

**Carrie Chowske:** So I plan it out ahead of time and kind of get it there.

**Carrie Chowske:** And it works even if you don't, you know, you can change these.

**Carrie Chowske:** It's not like the client moved these around, because she has an interface for these.

**Carrie Chowske:** So the client actually has a view into this.

**Carrie Chowske:** And I've given her access to only certain fields.

**Carrie Chowske:** So, like, in the interface, she can change this.

**Carrie Chowske:** So if she wants to make it two weeks from now instead of this week, she can do that.

**Carrie Chowske:** But she doesn't have access, and she can change, like, who we're targeting, you know, but she doesn't have access to change, like, the assignment type or the cluster or anything like that.

**Carrie Chowske:** Like, I don't, you can give people just access to just what you need them.

**Carrie Chowske:** And you can also only show them what they need.

**Carrie Chowske:** Like, I've, obviously, my Airtable has a ton more categories than this.

**Carrie Chowske:** But anyway, yes, Bailey.

**Bailey Seybolt:** I wanted wanted to know.

**Bailey Seybolt:** How, on your Airtable, you route the client approval process, because one of the things that I think has been hard, and I think Katya even might have asked a question on Slack about this, is especially when you're, like, presenting 70 new assignment topics or something, and then they're going through and having to leave comments on everything, but then I recently discovered that they can't actually, like, check a box because you have to have more advanced editing capabilities than we give clients.

**Bailey Seybolt:** So I was wondering if you found a workaround that allows them to either just approve things or to kind of leave comments on topics using the interface capability.

**Carrie Chowske:** Yeah, if you, if you, if they don't have edit capabilities because you're, they've only got view, like you're saying they only have view permissions for the interface, right?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Because the interfaces are part of your, well.

**Carrie Chowske:** Can they interact with it in the same, in a way that they can't?

**Carrie Chowske:** It's my understanding that it's, if they're an editor on the base itself, so like what you're looking at right now, my content OS, if they're an editor on that content OS, they're an editor on all the interfaces, the same as you are.

**Carrie Chowske:** They have the same permissions that you do.

**Carrie Chowske:** However, if you create an interface and you share it with someone who is not an editor or even a member of your base, then they just get access to what you give them access to.

**Carrie Chowske:** And you can assign it by person, same way as you can the internal stuff.

**Carrie Chowske:** I do not think that that impacts the seats.

**Bailey Seybolt:** I can double check, but I'm pretty sure it doesn't.

**Carrie Chowske:** But even if it does, there's some, they can still comment.

**Carrie Chowske:** Commenting is open regardless of what level I think somebody is at.

**Carrie Chowske:** They can leave comments because it doesn't affect any of the data, right?

**Carrie Chowske:** So here's, this is a good example of one of those that, that I have, which we're doing like, we do anywhere between like 14 up to 100 pieces a week for them.

**Carrie Chowske:** So it's a lot.

**Carrie Chowske:** And the client wants to approve every client day.

**Carrie Chowske:** wants single And

**Carrie Chowske:** There's got to be the exact match to the keyword in the title because it's 2008 and, you know, just little stuff like that.

**Carrie Chowske:** So there's like lots of layers of approval, right?

**Carrie Chowske:** He wants to approve the topic, wants to approve the keyword, wants to approve the content itself.

**Carrie Chowske:** So their interface looks a little bit different than the one I just showed you.

**Carrie Chowske:** This one here is, so he wanted to be able to still see all the content because this was being kept in a master spreadsheet before this.

**Carrie Chowske:** God help the former managing editor on this account.

**Carrie Chowske:** And so I was like, hell no.

**Carrie Chowske:** And so I gave him access to everything that's in production.

**Carrie Chowske:** So anything that's beyond, you know, anything that's in here is available for him to look at.

**Carrie Chowske:** He can see at any point in time what we're working on.

**Carrie Chowske:** I don't think he's ever checked it, but it's still there if he wants it.

**Carrie Chowske:** Then I have a tab for proposed topics.

**Carrie Chowske:** This is just pulling from considering.

**Carrie Chowske:** And then you can also say like only if there's a primary keyword because he obviously wants me to have that.

**Carrie Chowske:** So these are the ones that he hasn't.

**Carrie Chowske:** But I sent him like 70, but these are the only ones he didn't approve.

**Carrie Chowske:** So I have, I created a little check box and this is in Airtable.

**Carrie Chowske:** It's just a check box that I added.

**Carrie Chowske:** Like I added a column, I set it as a check box.

**Carrie Chowske:** And then in the automations, when he checks that box, it changes the status of that item to ready to start.

**Carrie Chowske:** So, and you can, and I've done the same thing for when he approves the content, right?

**Carrie Chowske:** So there's like, articles to review.

**Carrie Chowske:** So I don't have any in here right now.

**Carrie Chowske:** But if there were some in there, then he can go and he can read them.

**Carrie Chowske:** can access the, like for these, he doesn't have any edit capabilities really.

**Carrie Chowske:** It's literally just, he can open it and he can check this box.

**Carrie Chowske:** That's pretty much it.

**Carrie Chowske:** Oh, and he could change the status if you really want to do.

**Carrie Chowske:** Like if he wanted to say, hey, let's not do this one.

**Carrie Chowske:** Let's archive it.

**Carrie Chowske:** He could redo that.

**Carrie Chowske:** He doesn't.

**Carrie Chowske:** But he could.

**Carrie Chowske:** Does that answer your question, Bailey?

**Bailey Seybolt:** Yeah, it does, mostly.

**Bailey Seybolt:** I think I have spreadsheets where I think people only have commenting access, so they can't change the status on anything, and they can't check boxes.

**Carrie Chowske:** Yeah, so they can still, they should still have access to this.

**Bailey Seybolt:** But it sounds like they can do the interface, so that might solve the problem.

**Carrie Chowske:** think they can, and even if they, and again, even if they can't, they can leave a comment in the Airtable if you've invited them to the interface, and you can preview it as them.

**Carrie Chowske:** So you can see exactly what they're going to see.

**Carrie Chowske:** So like, this is my client contact here, and I can see exactly what he sees, where he has no access to click any of these things, but he can leave a comment, and he can check this box, and he can change the status.

**Bailey Seybolt:** Yeah, that's great.

**Carrie Chowske:** That definitely answers it.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** That's my favorite tool, is that view it as.

**Carrie Chowske:** I saw you pop on, Sydney.

**Sydney Arin Go:** I didn't mean to, like, just take over, but.

**Sydney Arin Go:** No, all good.

**Sydney Arin Go:** Yeah, no, client call went long.

**Sydney Arin Go:** There's this.

**Sydney Arin Go:** the story of my life.

**Carrie Chowske:** What I love about Sydney's automation is my favorite one so far, but I couldn't get it to work the other day, so I want her to show us her fun stuff.

**Sydney Arin Go:** What I will say, though, for your question, Bailey, is sometimes in the interface itself, you can just give them access, like editor access within that interface, and only for that interface.

**Sydney Arin Go:** I don't know how that would work with SEATS, but it is possible to give them access to just one interface, and not the entire data set.

**Bailey Seybolt:** Okay, interesting.

**Carrie Chowske:** And you can limit what the interface shows, you can rename things, it doesn't affect our side of it at all, it doesn't affect the content OS, it only affects what they're looking at.

**Carrie Chowske:** So it's like a view instead of an actual, like, you know, spreadsheet or anything.

**Jenn Peters:** to add to that, like, I don't think the guidance, unless I'm totally mistaken, was not around, like, was not, we cannot give clients access or seats.

**Jenn Peters:** Like, I think the issue was, is that we had, like, however many air tables out there.

**Jenn Peters:** We with, like, clients that were, like, churned are no longer with us, and then there was, like, each one had, like, five seats with editor access, and we were paying for, like, all these seats that clients weren't even using because we were just giving them out, not knowing, like, what, you know, like, before we had strategy sprint process, before all this kind of stuff was more, like, honed, and so they recently sent out a spreadsheet where they were like, hey, can you go into your air table and see, like, how many of these people do you actually need to have access?

**Jenn Peters:** So, I don't think the guidance was, like, there's nobody on the client's name list that could get, like, editor access, or we pay, we don't want to pay for a seat, it's just that I think we were paying for, like, a lot of seats we weren't using, basically.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And I, in general, not many people go in and edit things, so.

**Jenn Peters:** Totally, like, they just need, like, view access, but we were giving, like, editor access for, like, six people on their team, and, like, most of them don't even use air table or even look at it or anything.

**Jenn Peters:** Like, that's, I think that was the issue.

**Sydney Arin Go:** Would it be helpful if I just showed you what the automation should look like?

**Sydney Arin Go:** Yeah?

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** So to be completely transparent, is 2.40 in the morning for me.

**Sydney Arin Go:** And this is my fifth hour of calls.

**Sydney Arin Go:** So my brain is a little bit fried.

**Sydney Arin Go:** So please just don't be too critical about my presentation skills at the moment.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** So this is the interface that I have for LightSource.

**Sydney Arin Go:** And so if you launch this interface, I have the ideas for approval.

**Sydney Arin Go:** A full list of ideas here that they can go through and kind of like what carries a setup.

**Sydney Arin Go:** These are, I don't allow them to edit any of this here.

**Sydney Arin Go:** I have all the content in production here because I have a couple of statuses in Airtable.

**Sydney Arin Go:** So I have a ready for ME status, ready for CM status, but I don't want them to see all that.

**Sydney Arin Go:** But any of those statuses here.

**Sydney Arin Go:** So if you'll see, I think, actually, no.

**Sydney Arin Go:** This is in launch, so I can't show you what the data is like.

**Sydney Arin Go:** What's the help to, think?

**Sydney Arin Go:** Automations and interfaces.

**Sydney Arin Go:** Okay, so here I have this set up for this content production is filtered by.

**Sydney Arin Go:** it's in production or ready for CM or ready for ME review, it all just shows up in the content in production.

**Sydney Arin Go:** If they want to see revising, this is in revisions.

**Sydney Arin Go:** We don't have any yet ready to publish content production is, all of them is all in here.

**Sydney Arin Go:** Just so they have full visibility in the content pipeline and what's currently in flux.

**Sydney Arin Go:** Anything that's ready for review would go in here.

**Sydney Arin Go:** Um, and I do have this set up so that if they don't want to message us on Slack at all, they can just click on what they want us to do if it's ready to publish or if it needs revisions.

**Sydney Arin Go:** Um, this will also ping in Slack, um, and it will change the status in our air table as well.

**Sydney Arin Go:** Um, and then published articles here so they can see the whole view.

**Sydney Arin Go:** Um, I think this is week five for light source.

**Sydney Arin Go:** So we actually don't have any.

**Sydney Arin Go:** bit Bye.

**Sydney Arin Go:** Bye.

**Sydney Arin Go:** I to publish for them yet, but yeah, so just a full view into that, into the content production pipeline was the goal with this interface, and then I did have some information in here, but mostly it's in the individual cards, and then same as Carrie's is that it's got the approve and delete button here, the delete column, actually, they asked for it because they kept just commenting, delete, delete, delete, and so the reason I have it set up here with customer comment, is because it's because a lot easier for me to pull this data into Google Doc, because I do have an automation set up, so that if I set anything to, in production, I, Airtable will ping Tamara, who is the CM on this account, in Slack, with a link to the, to Google Doc that it created in the internal draft, in this internal draft column, and a link to this Airtable record, so that she, when she's done editing, all she

**Sydney Arin Go:** All do is click on the record, it'll send her into the record view, basically into this view, and then all she needs to do is change this back to me and then I'll get a ping in Slack.

**Sydney Arin Go:** The dot that generates looks like this, so this is the what is direct procurement, this is all automated, so it pulls a target keyword, article description, secondary keywords, I have a column for that air table as well, and then it also adds in, this is my editing checklist, and then this is usually blank and it has placeholders here, and then just notes for Tamina to add this in, and the way that I have set this up is here.

**Sydney Arin Go:** Okay, so this is the content production bot that I set up, and so I just put it all in here.

**Sydney Arin Go:** Sorry, it's not very big.

**Sydney Arin Go:** I'm not sure if you can actually see what this looks like.

**Sydney Arin Go:** But it's here in the bottom corner, all of the information is all in here, so the title pulls their primary keyword short description.

**Sydney Arin Go:** If you want to add.

**Sydney Arin Go:** If a link to someone in Slack, you just have to get the client ID or their profile ID.

**Sydney Arin Go:** Put it here as an at with the things.

**Sydney Arin Go:** And then file URL if you want to link to something as an anchor text and not like have the link on display in the Slack message.

**Sydney Arin Go:** You can use this little line thing and then also the carrot thingies on the side.

**Sydney Arin Go:** Is that kind of what you're wanting to see?

**Carrie Chowske:** Yeah, no, that's helpful.

**Carrie Chowske:** This is all just pulling from Airtable.

**Carrie Chowske:** It looks super complex when you look at it.

**Carrie Chowske:** I literally went in and recreated this exact automation by just putting it up side by side and copying each step because you have to rearrange it for your own base.

**Carrie Chowske:** You can't just copy the automation and move it over to another base.

**Carrie Chowske:** You have to actually create it.

**Carrie Chowske:** But you also can just tell the AI assistant in Airtable to create you a workflow that does these things.

**Carrie Chowske:** It's our teams.

**Carrie Chowske:** It's

**Carrie Chowske:** Our team at GrowthX Google account is already attached to Airtable, so you should be able to have access to anything that the team's account has access to.

**Carrie Chowske:** And if you attach your own Slack, you can use actually people's, just their handle, you don't need to have their ID.

**Sydney Arin Go:** Oh, you can?

**Sydney Arin Go:** It didn't let me do.

**Sydney Arin Go:** I tried multiple times, I just sent it as plenty.

**Carrie Chowske:** Well, maybe, maybe, maybe it didn't, maybe I did, maybe I did it wrong, I don't don't, don't hold me to that.

**Sydney Arin Go:** probably did it wrong, I probably did it wrong, um, Carrie, I remember you saying that you couldn't get this to work, was it the creation of the Google Doc?

**Carrie Chowske:** Yeah, yeah.

**Sydney Arin Go:** Okay, so I did have a workaround for that, I just realized now, um, that, so what I did was, I created a folder in my own personal account, and then just added a shortcut to the shared company, um, drive.

**Sydney Arin Go:** Because I think there are permissions in the company drive where automations cannot create docs, um, the way I have the light source.

**Sydney Arin Go:** Thank

**Sydney Arin Go:** The light source drive set up is, so I have the internal light source and the external here.

**Sydney Arin Go:** This folder is a shortcut, but it is in my personal account.

**Carrie Chowske:** Oh, so it's, you're telling it to create the file in that shortcut?

**Carrie Chowske:** Like you selected that shortcut?

**Carrie Chowske:** Oh, okay.

**Sydney Arin Go:** Wow, I'm surprised that works.

**Sydney Arin Go:** That's awesome.

**Sydney Arin Go:** Yeah, it actually, so it's linked to, I think you're going see my messy drive.

**Sydney Arin Go:** It is linked to this, this in my drive, in my personal drive.

**Sydney Arin Go:** And I use my account to create, to create, I link this to my account.

**Sydney Arin Go:** You can also do it in the team at GrowthX Labs.

**Sydney Arin Go:** If you make a folder in the team at GrowthX Labs account that is outside of the shared account, yeah, then it will work as well.

**Sydney Arin Go:** And then you can just add a shortcut to whatever folder it needs to be in.

**Sydney Arin Go:** And yeah, it's, it's still fully accessible by everyone.

**Sydney Arin Go:** And so just make sure the permissions are the same.

**Sydney Arin Go:** And that way, you know, anybody can make a copy of that folder as well.

**Sydney Arin Go:** So, but yeah, that's the workaround that I had.

**Carrie Chowske:** I love that.

**Carrie Chowske:** I got so sick of asking CMs, like, can show your doc with me?

**Carrie Chowske:** Like, well, everybody I'm working with right now is great at it, but I did get sick of that for a while where I was like, hi, I need access to your doc.

**Sydney Arin Go:** Yeah.

**Sydney Arin Go:** Yeah, that's actually the motivation why I have this set up is because it does take a lot of brain space.

**Sydney Arin Go:** Like, it does disrupt a day or, you know, a workflow to ask the CM to create a doc in a specific folder and then add that link to that doc back into Airtable and look for that specific Airtable.

**Sydney Arin Go:** It does take some mental load.

**Sydney Arin Go:** So just taking that off of them.

**Carrie Chowske:** Also, like, and just in case anyone's looking at this going, oh, my God, I have to do all that.

**Carrie Chowske:** No, because you also can just set, like, like how Sydney has this, like, 3.1 status.

**Carrie Chowske:** She created a new status and you can literally just create an automation that when something goes to that status, like ready for ME review. She could just create just one automation that all it does is every time something gets changed to that status, it sends her a Slack message or an email or something like that.

**Carrie Chowske:** So you can do it that simple or you can do hers is all in one, which is nice.

**Carrie Chowske:** It's a big, long workflow, but, you know, one thing breaks, they all break.

**Carrie Chowske:** So, you know, if you're feeling less comfortable with the automations, you can start small.

**Sydney Arin Go:** Yeah.

**Sydney Arin Go:** And I did do that actually for the needs.

**Sydney Arin Go:** This is just one thing.

**Sydney Arin Go:** This is just if somebody checks delete, it deletes.

**Sydney Arin Go:** And this is something if somebody checks the approved, it approves.

**Sydney Arin Go:** So you can do that.

**Sydney Arin Go:** The other one that at least for communication customers was helpful was the next step column.

**Sydney Arin Go:** I just create a whole new column for them to access.

**Sydney Arin Go:** And if you just want an isolated workflow, like you can just do that as well.

**Sydney Arin Go:** Katya, see your hand is up.

**Katya Luscomb:** Yeah, I was curious because I know part of your process, you've got the internal doc and then you usually copy and move content over into like Like

**Katya Luscomb:** more polished final version so that the client can't see all our comments and everything.

**Katya Luscomb:** Is that part of your workflow as well?

**Katya Luscomb:** Like, does Airtable, can it copy content from one doc into another?

**Katya Luscomb:** Or is that still more of a manual process for you guys?

**Sydney Arin Go:** It can, and I just found it fast to just do it myself.

**Sydney Arin Go:** It can though, Airtable does have a, where is it?

**Sydney Arin Go:** It does have a, so if you want to do this, create a Google doc thing.

**Sydney Arin Go:** And Google doc has a thing where you can update the doc.

**Sydney Arin Go:** And then from there, you can tell it to copy from whatever.

**Sydney Arin Go:** I've not played around with it too much because it just, it felt like a lot.

**Sydney Arin Go:** So what I did instead is I have a link to the external folder in the Slack message that pings me.

**Sydney Arin Go:** So that I can just open the external folder directly from Slack without having to look for it.

**Sydney Arin Go:** And then create a new, a new file from there.

**Sydney Arin Go:** can send will hit goal just,

**Sydney Arin Go:** I'm going to stop sharing.

**Carrie Chowske:** Does anybody have anything that they're wanting to automate that they're like, I have no idea how to do this or where to start, that they would want help?

**Carrie Chowske:** Maybe somebody or anybody have an idea that they're doing that they want to share that they're like, that's great.

**Carrie Chowske:** I can do it better because I thought my automations were fine.

**Carrie Chowske:** And then I saw Sydney's and I was like, OK, I'm going to quit.

**Carrie Chowske:** You can have my job and I'm going to go home.

**Sydney Arin Go:** I'm home.

**Carrie Chowske:** I can't go home.

**Sydney Arin Go:** And I do remember someone asking about how exporting from Atlas works.

**Sydney Arin Go:** Did you want me to show how that workflow works for me at least?

**Sydney Arin Go:** So the way that I export from Atlas is it's a lot of app scripts, which you can just create with ChatGPT.

**Sydney Arin Go:** You don't even need to program it.

**Sydney Arin Go:** Just tell ChatGPT exactly what you want and it will spew out something for you.

**Sydney Arin Go:** I've not tried Cloud Code, but Cloud Code might actually be better now that I'm thinking about it.

**Sydney Arin Go:** So with Webflow, the biggest challenge is that we have to do.

**Sydney Arin Go:** want Ichdao.

**Sydney Arin Go:** can won't see dad I No.

**Sydney Arin Go:** Where I have to do 30 pages for them every week, and I don't have a CM on this account, so it's, I have to make sure that all the workflows in this account are as optimized as possible.

**Sydney Arin Go:** So what I do is, after generating all of the content, I select which ones I want to export, and then export this into a CSV, and then so, and then that CSV goes into basically this doc.

**Sydney Arin Go:** And then I have an app script, oh, not sharing my screen at all.

**Jenn Peters:** Nope, just checking.

**Jenn Peters:** Thank you.

**Jenn Peters:** And now I'm sharing the wrong screen.

**Sydney Arin Go:** Okay, so yeah, I've done that for all of my calls today, which is fun.

**Jenn Peters:** I mean, it isn't okay for you.

**Sydney Arin Go:** Oh, yeah, it's, brain isn't, it's starting to fizz.

**Sydney Arin Go:** Anyway, so it goes into all of the things that I expected.

**Sydney Arin Go:** So you can just export it as CSV, I just paste it into here, and I have an app script set up that recognizes the H1s, so because these are very templated, but it recognizes the H1s, the pound sign, and then splits it into columns based on that, and I just run it.

**Sydney Arin Go:** And then from there, if I want to turn this into a doc, what I do is, I actually don't know which one has it, but I have an app script set up that transforms this into a doc.

**Sydney Arin Go:** It might actually be my blank spreadsheet.

**Sydney Arin Go:** Sorry.

**Sydney Arin Go:** I promise I'm not crazy, I use a lot of spreadsheets, so I just need one default one with all of my sheets in here.

**Sydney Arin Go:** But anyway, so what I do here is, I have an app script, yeah, okay, so this is the one that turns.

**Sydney Arin Go:** This in here, column A and B, anything in column B and C, into its own doc in a folder.

**Sydney Arin Go:** So I'm just going to double check that this is not a client folder now that I'm demonstrating this.

**Sydney Arin Go:** Drive.google.com.

**Sydney Arin Go:** Okay, that's a random folder.

**Sydney Arin Go:** Okay, so this, using this Apps Script, I just have to save and then run it.

**Sydney Arin Go:** And I have it set up, so it pulls column B and column C into its own doc, and then it'll execute, and it'll tell me when it's done, but there might be some stuff showing up in here now.

**Sydney Arin Go:** Yeah, so there, it, it'll pull that, whatever was in here, so it is in Markdown because Atlas only exports to Markdown.

**Sydney Arin Go:** Whatever is in here will go into this random folder.

**Sydney Arin Go:** And then here, so from here, obviously this is not client presentable.

**Sydney Arin Go:** What I do is I have another Apps Script set up.

**Sydney Arin Go:** I'm not sure if it's this or that, completely honest.

**Sydney Arin Go:** I think it's this one.

**Sydney Arin Go:** Yes, it's this one.

**Sydney Arin Go:** I have another app script set up here so that if I just paste the doc ID into here, it'll reformat that into plain text.

**Sydney Arin Go:** And then run that.

**Sydney Arin Go:** And that should reformat.

**Sydney Arin Go:** Opening, done.

**Sydney Arin Go:** There you go.

**Sydney Arin Go:** And then, so now you have a fully formatted doc, just directly from whatever you exported from Atlas.

**Sydney Arin Go:** So this is actually not, sorry.

**Carrie Chowske:** Oh, I'm sorry.

**Carrie Chowske:** I was just going to say, also, if you didn't want to go the extra step, you could literally copy what was already in the doc, cut it, right click, paste it, and you can paste the mark down and it'll paste it.

**Carrie Chowske:** Like, do you what saying?

**Carrie Chowske:** It's fine.

**Sydney Arin Go:** It's not a big deal.

**Katya Luscomb:** I think you have to have a, you can paste it.

**Katya Luscomb:** Sorry.

**Katya Luscomb:** I to say, I think you have to have a mark down and name.

**Carrie Chowske:** But you only have to do that in one doc the very first time, and then it is just standardized across everything.

**Carrie Chowske:** Yeah, and then you can paste directly in Markdown.

**Carrie Chowske:** So this is why we all should talk more often.

**Sydney Arin Go:** I know.

**Carrie Chowske:** Does it also do HTML?

**Carrie Chowske:** No.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** Because that was my big challenge with this one is the, it didn't understand the HTML part, the table was in HTML.

**Carrie Chowske:** Oh, it'll do, it'll do, yeah, it won't do that, it won't do that, but it will, like, your links will be okay and everything.

**Carrie Chowske:** But if, as long as the Markdown is there, you can paste it and it'll come up like this.

**Carrie Chowske:** But then all you have to do is right-click, paste to do it.

**Sydney Arin Go:** Okay, I'm going to ask you how to do that after the call.

**Carrie Chowske:** Sydney, Sydney, Sydney, your brain must work like mine because I over-engineer everything, too.

**Carrie Chowske:** Like, people tell me things and I'm like, wait, yeah, yeah.

**Carrie Chowske:** Wait, you mean I could have taken a shortcut around my shortcut?

**Sydney Arin Go:** Thanks, thanks.

**Carrie Chowske:** That's really handy, though.

**Carrie Chowske:** I like that.

**Carrie Chowske:** I'm not sure I could.

**Sydney Arin Go:** You can do it in Chachibiki, honestly.

**Sydney Arin Go:** All of it can be done in Chachibiki.

**Sydney Arin Go:** No, I was going to say.

**Sydney Arin Go:** That's me what you want.

**Sydney Arin Go:** want.

**Carrie Chowske:** Yeah, no, I was just going to say, I'm not sure I could have thought of that myself, is what I was just going to say.

**Carrie Chowske:** I don't think I would have thought to do all this.

**Sydney Arin Go:** The big thing for me was having them repeatable.

**Sydney Arin Go:** So I do recommend just asking the Apps Script, if you're going to export from a doc into another Google Doc, is having the links in here.

**Sydney Arin Go:** I would even ask it to not purify it, because the most important part of this is having the URL, so that you can just paste it into an Apps Script.

**Sydney Arin Go:** I think one of these Apps Scripts is I can just paste the whole URL, I don't even need the Doc ID, and then the Apps Script will extract the Doc ID from there, and then identify which Docs need to reformat.

**Sydney Arin Go:** The other thing that I would recommend is if you do this for a huge batch of Docs, is having a max per run, just so that it doesn't fail.

**Sydney Arin Go:** Because if you're, I did it for like 200 Docs, and it took like three hours, and then it failed two, three times, and it was painful.

**Sydney Arin Go:** So have a max 15, and just run it every 15 kind of thing.

**Sydney Arin Go:** So, and then it'll tell you, like, which batches are done.

**Sydney Arin Go:** Um...

**Sydney Arin Go:** But that's basically it, I don't know how to stop sharing my, there it is, okay, I can stop sharing the scripting.

**Carrie Chowske:** I mean, I hope that was helpful.

**Carrie Chowske:** Very, I think Ehtisham said he had an automation that works, but it wants it to be better, so he's going to get some, see if we had, any of us had opinions on it.

**Ehtisham Hussain:** Let me see if I can share my whole screen.

**Ehtisham Hussain:** All right, so do you guys see Slack right now?

**Ehtisham Hussain:** Yes.

**Ehtisham Hussain:** All right, so, so, InBit has three different people who edit articles that we send them, and they leave comments, and they, you know, they give us feedback, et cetera.

**Ehtisham Hussain:** What they wanted was for, like, an automatic message to go out, something like this, and I've set it up.

**Ehtisham Hussain:** It says the article title has been assigned to the person.

**Ehtisham Hussain:** But the thing is, the person's name is not really tagging them in Slack, so I added an email address, but it looks really weird now.

**Ehtisham Hussain:** article.

**Ehtisham Hussain:** And it still doesn't tag them.

**Ehtisham Hussain:** What they ideally want to do is title has been assigned to and then tag the person that it has been assigned to in their channel.

**Ehtisham Hussain:** The automation that I've set up is this.

**Ehtisham Hussain:** So the initial, the condition that it's ready to review, that works.

**Ehtisham Hussain:** Title, dropdown, dropdown, like I got it over here, assigned to.

**Ehtisham Hussain:** I'm only getting like, if I look at it, edit token.

**Ehtisham Hussain:** And I'm only getting email here and name.

**Ehtisham Hussain:** So how do I like tag them?

**Carrie Chowske:** So you need to tag their Slack ID.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So it should, it's because you're doing this in the, in the, the channel already.

**Carrie Chowske:** Like, cause I, how I've gotten around it before is just sending somebody like a DM.

**Carrie Chowske:** But you also, I think I'm, I'm guessing that what Sydney showed earlier with her.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Um, where she'd use the, like the ID, like their user ID number, which you should be able to see on their profile, that you should be able to use that, like, instead of using.

**Sydney Arin Go:** Oh, I sent you the ID in the chat.

**Carrie Chowske:** But you would have to, you would probably, if you want to be able to sync it with, um, like, are these going to change from one to the next, or do you have set people that it goes to?

**Ehtisham Hussain:** So, they are going to decide the person who's going to edit on their site.

**Ehtisham Hussain:** So, I move it to, to Ready to Review.

**Ehtisham Hussain:** They have their own, like, view over here called Ready to Review.

**Ehtisham Hussain:** And then, one of their people goes in.

**Ehtisham Hussain:** And then, so, for example, there's no name over here.

**Ehtisham Hussain:** Apoorba will most likely go in, and he's going to assign it to Dan, and Asher, and himself, and so on.

**Ehtisham Hussain:** So, what do you want to so you're just trying to tag.

**Ehtisham Hussain:** Yeah, and then he wants a message to go out as soon as...

**Carrie Chowske:** He puts a name in here.

**Carrie Chowske:** He wants a message to go out.

**Ehtisham Hussain:** Okay.

**Carrie Chowske:** And tag that person in Slack.

**Carrie Chowske:** Do you remember, you remember the automation that we had at animals that would like tag the editors when you would move like an assignment around?

**Carrie Chowske:** Do you remember that one?

**Ehtisham Hussain:** Where it would like message us.

**Carrie Chowske:** It's ages ago.

**Carrie Chowske:** Yeah.

**Ehtisham Hussain:** But you remember how that worked.

**Carrie Chowske:** That's what you're trying to do here, right?

**Carrie Chowske:** That's what you're trying to do.

**Carrie Chowske:** Okay.

**Carrie Chowske:** So I think what you just need to do, you might need, you need a, you need a column in your Airtable for their Slack ID.

**Carrie Chowske:** And then if you put the number in there, then you can just use it as, because it'll be a field then, right?

**Ehtisham Hussain:** So you just map it.

**Ehtisham Hussain:** You just map your message here to that field.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** And how do I see it?

**Carrie Chowske:** I think, I think you can click on their name.

**Sydney Arin Go:** I think you can see it.

**Carrie Chowske:** Yeah.

**Sydney Arin Go:** was, I was like, yeah, you can go to the dots and copy ID.

**Sydney Arin Go:** I was thinking, I don't think you need to add a new column.

**Sydney Arin Go:** You could just have Airtable, watch that column with the assignments and then have a different automation based on the names.

**Ehtisham Hussain:** don't know.

**Sydney Arin Go:** You don't need to create a new column.

**Sydney Arin Go:** Does that make sense?

**Carrie Chowske:** Oh, can set the automation for that column, for the watching column.

**Sydney Arin Go:** Yeah, that name.

**Sydney Arin Go:** Yeah.

**Carrie Chowske:** All right.

**Ehtisham Hussain:** So I'll try two or three different ways.

**Carrie Chowske:** see.

**Carrie Chowske:** Yeah, it can definitely be done.

**Carrie Chowske:** But that's essentially, I think, how they probably did that one that they had at animals, is my guess.

**Carrie Chowske:** Because I know that we were all listed in that Airtable like that.

**Carrie Chowske:** Sorry.

**Carrie Chowske:** This is now the third agency where Edisham and I have worked together.

**Carrie Chowske:** We just keep traveling around, dragging the other one along.

**Carrie Chowske:** It's pretty fun.

**Carrie Chowske:** I highly recommend.

**Carrie Chowske:** Anybody else have anything that they want to throw out there, or anything they want to ask about?

**Nathan Navidzadeh:** Super noob here.

**Nathan Navidzadeh:** I'm like a very recent hire.

**Nathan Navidzadeh:** I don't even have any accounts yet, and I'm just being moved over to one of the accounts like next week.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** I just wanted to see how it works.

**Nathan Navidzadeh:** Everybody was doing this, and it's, like, really cool to see all this collaboration, so, like, awesome, so excited to be part of this team.

**Nathan Navidzadeh:** I had a question just about exactly what we were doing right now, because my thought was, okay, can we do, like, if-then logic, which is also what Katya was saying.

**Nathan Navidzadeh:** So, like, what does that look like in Airtable?

**Nathan Navidzadeh:** Like, how do you add the if-then logic?

**Nathan Navidzadeh:** What language, like, do you have to put that in?

**Carrie Chowske:** Like, how is that done?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So, I have done some of this.

**Carrie Chowske:** I think Sydney's has a little bit more, but they can get, like, really complex.

**Carrie Chowske:** I'm trying to remember off the top of my head which client I have this for, and I want to say it's for your go.

**Carrie Chowske:** Let me just hold it.

**Carrie Chowske:** Why is your internet always slower when you're trying to show somebody something, by the way?

**Carrie Chowske:** Always.

**Carrie Chowske:** It's always slow.

**Carrie Chowske:** Go ahead.

**Carrie Chowske:** So, I, I, this, if you know how to do a basic,

**Carrie Chowske:** If then, like, you'll, you'll have no problem doing this, it, they, the problem that I have with Airtable sometimes when I'm trying to automate is that they, the limited, like, triggers that they have, I feel like they can have more and they don't really have, you know, a ton, I mean, they're definitely, you know, you can get complex with it if you know how to do a bunch of stuff, like, you know, you want to create a webhook, great, you know, like, you can do a bunch of stuff.

**Carrie Chowske:** I don't know that, or, like, when a record is updated or at a scheduled time, like, those are the easiest ones, but once you do those, you can actually, like, do an if then, so you can do conditional logic on something, and you can do a repeating group, so, like, if you look at, like, this is a repeating group, so you'll ask it to find all the ones where the priority is next week, because I'm asking it to do it once a day, so it's not like it's whenever it updates, it's just once a day, at this time, once a week at this time, do this, find all these records, and then repeat it for each one.

**Carrie Chowske:** I want you to update this and move, you know, change this column to that column.

**Carrie Chowske:** But you can get really complex with this then.

**Carrie Chowske:** So, like, you can do a whole, like, let's say my, oh, I didn't set up the trigger.

**Carrie Chowske:** Anyway, I didn't set up my trigger yet.

**Carrie Chowske:** But basically, I could be like, if my status is this, then do this.

**Carrie Chowske:** But if it's this, then do that.

**Carrie Chowske:** Like, yeah, you could get really complicated with it.

**Nathan Navidzadeh:** I try to keep it simple or I forget what I've done and I can't.

**Nathan Navidzadeh:** Yeah, no, my noobness is showing because I didn't even realize there was, like, a no-code, like, kind of drag-and-drop pic stuff, like, if-then.

**Nathan Navidzadeh:** I was wondering, like, did we have to literally, like, type that in the box where you were putting the Slack ID, like, what language do we have to do the if-then statements or whatever?

**Carrie Chowske:** No, it's really great.

**Carrie Chowske:** Yeah, so, like, this, what, the one that's the, I think, the trickiest to figure out is, like, when you're doing, all right, this one's a good one to show you.

**Carrie Chowske:** Like, when you're adding these tokens, like, you're telling it where to pull this information from, it's always going to start.

**Carrie Chowske:** Start with asking you, like, the URL and the record ID, but what it's doing is it's always going to give you the most recent thing that you asked it to do.

**Carrie Chowske:** So, like, I asked it to look for ones where the priority is set to buffer, and so it's giving me the columns for each of the, so if I wanted to display, you know, the assignment name here, or I wanted to, but this is what the Airtable record ID is going to be, like, you know, that's telling it where to pull this from.

**Carrie Chowske:** Like, literally, I need to pull the record ID, I can't give it anything else, but if I'm, like, like, here, I'm pulling in the assignment name, I'm pulling in the document link, and that is coming from whatever Airtable records, that very first column, that left, far left column in Airtable is the record, whatever that is, it's pulling that, and I can pull any of the columns on that page.

**Carrie Chowske:** So, if I wanted to tell him what the competitor URLs are for some reason, I could put that in here.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So it's, it's literally just whatever you've asked it to look for.

**Carrie Chowske:** It's going to give you sample data and you can see.

**Carrie Chowske:** What I like is I don't, I just, you can see what the actual, like, what it's actually going to put in there.

**Carrie Chowske:** When you click on it, it'll show you, like, if you, if you've told it, when you run the test, it'll pull the actual data from the test and it'll show it as, um, suggestion text, like under here.

**Carrie Chowske:** So you'll be able to see.

**Carrie Chowske:** And then this, um, this is what I was saying, Sydney, like when you, if you connect your personal Slack, like I, this just I can message Joe directly without having to put his user ID in.

**Carrie Chowske:** Like, I can just pick him like I can.

**Carrie Chowske:** So I can change this so that it messages you.

**Sydney Arin Go:** Do you want to get more, do you want to get more Slack messages?

**Sydney Arin Go:** Actually, if you want, um, I set up the automation that Ersham wanted.

**Sydney Arin Go:** So if you want me to show you that real quick, I can do that.

**Sydney Arin Go:** Show off.

**Sydney Arin Go:** Um, yeah.

**Sydney Arin Go:** just interested me, um, on how that would work, and I think it does work, uh, so I'm still sharing the wrong screen, um, what's the problem with two desktops, uh, okay, I think this is the right screen, yeah, okay, um, so the way you do this is when a record is updated is what you want it to watch for, don't select a view, and then just hit, so for me it's reviewer, um, this is on the ambient account, so basically they have a, I'll do this later, um, they've got a reviewer, here, uh, nope, that's assigning, um, here, and ready for review, they've got a reviewer column here, and they're the ones who assign that as well, so if you want to do that, it would have to be, um, when it's updated, and then select if the reviewer is, whoever that reviewer is, and then add the Slack message in there, um, and then you can also add if the reviewer is someone else, um, reviewer, me, typing, um, and then so the other ones are Alberto, you for doing that.

**Sydney Arin Go:** Mal, you could do that as well, Slack message, send message, then, so the, kind of like what we talked about earlier, the copy, the member ID should go here, and you can get that from Slack, I'll just, I can send you a screenshot, how'd do that, and then the draft URL, and then have the little line thing in the middle, and then the carrots on the side, and then the title, and that should be a link, I'm going to delete that for now, and then what I usually do is when I test the step, I send it to myself, so, I have so many Slack automations, in my personal, in my personal messages, and I seem like a psychopath, but yeah, so that's what I do, and if you generate the preview, I don't want to run the test, I don't want to generate the preview, okay, it's not going to send anyways, sure, I don't think that has anything, so I don't think it's going to, oh there, and so that link should work, because I didn't put the ad, there's no ad, but this is what the message will look like, um,

**Carrie Chowske:** Yeah, that reminds me, though, to, like, be very careful when you're setting up automations, that if you test them, it will run the actual automation, so you have to make sure that you go back.

**Carrie Chowske:** So I always, just to save my own , I always create, there's, like, five different ones in each one of my content OSs, but it's, like, test article, and I just use that to test my automations, because you can put whatever you want in there.

**Carrie Chowske:** You can fill every field out and test out what each, what everything does.

**Carrie Chowske:** I created a sandbox for automations, too, by the way, so, like, in interfaces, like, so if you don't want to mess up your own content OS, and you want to just see what you can do, and don't, there's this, there's one, it's just called sandbox OS, I think, in the, in the Airtable.

**Carrie Chowske:** That's for anybody to use, it's just there.

**Carrie Chowske:** I am always open to ideas for how, like, we can be more efficient, and how we can, like, automate things, because, to be honest, we're all doing so much in a day, and, like.

**Carrie Chowske:** I think the reality is, like, I know we work for a software company, but the people on this call, like, we're running an agency while they're trying to stand up a software.

**Carrie Chowske:** And, like, we're not the priority in the sense that they're trying to build the product, right?

**Carrie Chowske:** So we don't have those engineering resources at our disposal that we do for content, you know, creation, to manage our workloads.

**Carrie Chowske:** And so, like, I think it, I think it's a good idea for us to be, you know, to talk to each other as much as we can so that we have, you know, all the tools at our disposal, all the brains in this, in this team.

**Carrie Chowske:** So it sounds like you've got some really smart freaking people around here.

**Carrie Chowske:** And, and, you know, we can all benefit from that because as you can see, like, you know, we can, Sydney's like, yeah, I got this automated.

**Carrie Chowske:** And I'm going, yeah, you can just do this.

**Carrie Chowske:** And she goes, oh, dang.

**Carrie Chowske:** And I'm looking at it going, man, I could have done that.

**Carrie Chowske:** We're all, like, so we're using our brains so many times for so many different problem solving moments in a day that I think, like, sometimes we forget the simplest things.

**Carrie Chowske:** And so having someone else's eye.

**Carrie Chowske:** It's a great way to maybe figure something out and we can perfect these before they try to standardize anything and make us do things that don't make any sense.

**Carrie Chowske:** Right?

**Carrie Chowske:** You know what I'm talking about.

**Carrie Chowske:** know what I'm talking about, right?

**Carrie Chowske:** Or suddenly there's like a new pot, there's a new like a procedure and you're like, this makes zero sense.

**Carrie Chowske:** I'm so terrified of them just shoving us into Atlas to manage all this stuff and then I lose all my air data automations.

**Carrie Chowske:** Anything else?

**Katya Luscomb:** I was just going to kind of piggyback off that and say like, I don't know if an actual like standing like every other week meeting would make sense, but just being able to like get on and throw ideas at each other has been so helpful, even to like unlock automations that I hadn't even thought of trying that are going to make my life a lot easier.

**Katya Luscomb:** So yeah, huge thank you for having this and would love to figure out an informal way to have this more often, a little bit more consistently.

**Carrie Chowske:** It'd be great.

**Carrie Chowske:** I think, um, maybe we do like an office hours type situation um, where there there's

**Carrie Chowske:** Just like a standing jump in if you have a problem and jump in if you've got five minutes to spare because I feel like we're all in so many meetings all the time and we're all like so busy, but I feel, I don't know, I don't know if that would work or, you know, even if we can do impromptu or I don't know how it would work best, but I agree, I think we need more like, and just so we feel like we're part of a freaking team, guys, like I'm sitting here by myself all day just going, how the heck am I going to get all this crap done?

**Carrie Chowske:** I don't know how I'm doing it, but somehow I'm getting it done.

**Carrie Chowske:** So I'll think about it.

**Carrie Chowske:** If anybody has any ideas on that one, I'm open to it too.

**Ehtisham Hussain:** Yeah, mean, we should discuss ideation, should discuss strategy, we should discuss how we create assignment briefs and how we edit stuff, like how we automate editing.

**Ehtisham Hussain:** So for example, I know we deal in bulk, so I'm going to do...

**Ehtisham Hussain:** I think I did 25 articles for AIMBit yesterday, I'm supposed to do 25 for Sunbit tomorrow, so obviously we're not going to edit that the old-fashioned way, right?

**Ehtisham Hussain:** So we are all doing our really smart tricks using AI tools to edit that stuff and get it to a point where the customer likes it, and I'm sure like a lot of us have many things to share about that.

**Carrie Chowske:** Yeah, definitely.

**Carrie Chowske:** Yeah, I like that.

**Carrie Chowske:** I dropped the link to the Notion that I created, so if you guys want to write a quick little, like, here's my automation, here's what it does, here's a quick, you know, even if it's just a screenshot of how, like, how Sydney was showing us what that flow, that if-then flow looks like, even just a screenshot can help somebody else set one up similar, or a link to the automation itself.

**Carrie Chowske:** But just drop in there.

**Carrie Chowske:** I did set, like I said, set those, like, intermediate, basic, whatever, beginner, advanced, really just about how burst you are in the thing that

**Carrie Chowske:** You're doing and any, you know, oh, if this is easy, you can, you know, claw to write the code for you or whatever you want, you know, that kind of thing.

**Carrie Chowske:** I have not played with that one, Marisol.

**Carrie Chowske:** Does anybody, has anyone done anything with that?

**Carrie Chowske:** Is that, how do you say that?

**Marisol Smith:** It's for creating agents more than automating, but I'm not sure if we have an account.

**Marisol Smith:** I've been trying to use it locally.

**Marisol Smith:** You can just set it up in your local machine, but we need, I mean, if you want to use it, you need the API tokens from GPT.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I'm, I wish I had the time in the day, too, to just learn, like, figure all these things out, because I would have it all, like, I think between Sydney and I, we could just figure it all out.

**Carrie Chowske:** It might be overly complex, but I don't if you guys, you guys know what a Rube Goldberg machine is, right?

**Carrie Chowske:** Like, I, Rube Goldberg, lord the heck out of every.

**Carrie Chowske:** Like, it's just over-engineered and just crazy, but I'll get it to work and it will work, so, and I'm always, I don't, I can't speak for anybody else, but I'm always happy to, like, if you're stumped and you're, like, trying to figure out if there is a way to do it or you want an easy way to do it or something, do an automation, like, I'm happy to try to help.

**Carrie Chowske:** I say try, because.

**Marisol Smith:** I would like to automate Fathom calls to bring the summary into Notion, like, to update the artifacts, but for that we would be an agent in between, like, to have the LLM summarizing and combining with the content that we already have and putting it all together.

**Carrie Chowske:** I wonder if you could do, like, I'm just thinking the easiest possible way, because I know you can, like, send that to, like, Google Doc, because I know it doesn't go directly to Notion, I wish it did, and then do something like what Sydney did with, like, having, like, a.

**Carrie Chowske:** A quick little script that just populates it, but, hmm, I'd to think on that one a little bit more.

**Marisol Smith:** That would work.

**Carrie Chowske:** Maybe a Zapier?

**Sydney Arin Go:** Yeah, that's what I Zapier can pull things.

**Sydney Arin Go:** Zapier can pull things from Fathom.

**Carrie Chowske:** Can it pull from Fathom?

**Carrie Chowske:** Okay.

**Sydney Arin Go:** Yeah.

**Sydney Arin Go:** That was the only question had an automation set up.

**Sydney Arin Go:** We had an automation set up where it pulled all of the to-do docs and then assigned the right people to those docs within Notion for our workflow internally.

**Sydney Arin Go:** It worked quite well.

**Sydney Arin Go:** So I know it can do it.

**Sydney Arin Go:** Updating the docs using that transcript, I don't know.

**Sydney Arin Go:** Like, you'd have to stick that in Claude, I think.

**Carrie Chowske:** Yeah.

**Marisol Smith:** I'm using Zapier or something, or Make, like Will, to bring the, for Augment Code, for example, the Change Log.

**Marisol Smith:** They are releasing new product features every week, so, but it's raw.

**Marisol Smith:** So, I would like an agent.

**Marisol Smith:** And to summarize and format it.

**Marisol Smith:** But that's the next step, I think.

**Carrie Chowske:** Sometimes I'm just grateful that Fathom gives you all the action items, and they're largely correct.

**Carrie Chowske:** Some days that's all I can be thankful for, is that I don't have to write them myself.

**Carrie Chowske:** I just could copy them over.

**Carrie Chowske:** But yeah, I don't know.

**Carrie Chowske:** There's a way so we can, if we can, I'm so excited for them to add this analytics piece to Atlas, and that it will work.

**Carrie Chowske:** Because I am just so sick of, anyway.

**Carrie Chowske:** I don't like reporting.

**Carrie Chowske:** Anyway, anybody else happy?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Looker's the bane of my existence right now.

**Carrie Chowske:** I hate it.

**Carrie Chowske:** Never loads correctly.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Anyway.

**Carrie Chowske:** See, we all need to commiserate more often.

**Carrie Chowske:** Even if it's just so we can go.

**Carrie Chowske:** But it will be like, instead of like, old man screams at cloud, we'll be like, you know, entire managing and editing team screams it.

**Carrie Chowske:** we'll we'll we you.

**Carrie Chowske:** All right.

**Carrie Chowske:** Well, I think we're over time, but no, not.

**Carrie Chowske:** Never mind.

**Carrie Chowske:** I think I did 45.

**Carrie Chowske:** Yeah, we're over 45.

**Carrie Chowske:** I can't tell time anymore, guys.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Thank you guys so much.

**Carrie Chowske:** I shared the notion in the chat, but I'll also put it on Slack, too.

**Carrie Chowske:** So if you would, drop your stuff in there.

**Carrie Chowske:** And like I said, Upvote is just for if you use it and you think it's useful and you love it and you're using it.

**Carrie Chowske:** I just want to know what people are doing to automate because then that'll help other people pick things that are like, yes, this is good.

**Carrie Chowske:** And it's not a popularity contest.

**Carrie Chowske:** Although I know everybody loves everyone.

**Carrie Chowske:** All right.

**Carrie Chowske:** I'll see you guys later.

**Jessalynn Jones (she/her):** Thank you so much, Carrie and Sydney.

**Marisol Smith:** Bye.

**Katya Luscomb:** Thank you.

**Sydney Arin Go:** This was great.
