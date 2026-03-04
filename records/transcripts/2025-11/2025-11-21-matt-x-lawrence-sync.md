# Matt x Lawrence Sync

<metadata>
date: 2025-11-21
time: 14:29 UTC
duration: 26 minutes
organizer: lawrence@growthx.ai
participants: Matthew Alves-Hill, Lawrence Neves
fathom_recording_id: 103457649
fathom_url: https://fathom.video/calls/483906425
share_url: https://fathom.video/share/J9DW6qkivE1DoPoMcUxsWVwxc6VA4zZr
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

Matthew walked Lawrence through the complete Rimkus Airtable workflow for managing content assignments — including how to import keywords, generate assignments in Atlas, import to Airtable, set up client views, and manage the approval process to build a 100+ topic content roadmap. The team agreed to shift to using the best available sources for citations (not just .gov/.org) and Matthew will propose a formal exception process to Rimkus, while Lawrence will take over the Seat account (5 articles/week) from departing CM Moses starting next week.

---

## Context

This is an internal GrowthX sync between Matthew Alves-Hill (Content Manager) and Lawrence Neves (new team member). Lawrence recently joined and is ramping up across multiple content accounts including Rimkus (forensic insurance content), Enable (5 articles/week), and Real City (programmatic tool pages). Rimkus is a key account with strict 5-article/week cadence and demanding client expectations. The meeting was called to clarify the Airtable workflow and content assignment process that Lawrence will own going forward, and to confirm his transition to the Seat account as Matthew reshuffles team capacity around departing team members.

---

## Relevance

**To GrowthX Delivery:**
- Airtable workflow standardization improves onboarding and reduces friction — Matthew documented full process from keyword import → Atlas generation → client approval → production cadence
- Citation policy shift reduces unnecessary back-and-forth with client reviews — using best available sources instead of strict .gov/.org rule will accelerate Rimkus content velocity
- Seat account handover (5 articles/week) consolidates Lawrence's workload — avoids complex information exchange by keeping Patricia on Tavern, sets up structured handover plan with Moses

**To GrowthX Business Development:**
- Rimkus account shows strong production momentum — built 100+ topic roadmap, maintaining strict 5-article/week cadence despite client review bottleneck
- Account consolidation readiness — Enable (5/week, delayed by PM/marketing alignment issues), Real City (10 programmatic pages, minimal lift), Seat (5/week takeover), positioning for stable delivery schedule

---

## Overview

- **Rimkus Workflow:** Lawrence will use Atlas to generate 100+ new forensic topics from his keyword research, importing them into Airtable for client approval to build a long-term content roadmap.
- **Rimkus Cadence:** To meet the client's strict 5-article/week requirement, Lawrence's 3 extra articles will be prioritized for next week's batch.
- **Rimkus Reviews:** To reduce friction, Lawrence will use the best available source for citations (even if non-.gov/.org), and Matthew will propose a formal process for these exceptions to the client.
- **Account Handover:** Lawrence will take over the Seat account (5 articles/week) from Moses, starting with a partial handover next week.

---

## Key Topics

### Rimkus Airtable Workflow

  - **Client Views:**
      - `Reviewing`: Auto-populates when status is set to "reviewing."
      - `Published`: Shows all published articles.
  - **Assignment Approval Process:**
      - **Goal:** Generate 100+ new forensic topics to build a long-term content roadmap.
      - **Steps:**
        1.  **Import Keywords:** Add new keywords to the `Target Keywords` view.
        2.  **Generate Assignments:**
              - In Atlas, use the `Assignments` pipeline to import a CSV of keywords.
              - Atlas generates titles and descriptions based on SERP analysis.
              - Export the Atlas output.
        3.  **Import to Airtable:** Add the Atlas output to the `Raw Assignments` view.
        4.  **Set Status:** Change status to `Considering` → populates `Assignments for Approval` view.
        5.  **Client Approval:** Client reviews and comments.
        6.  **Final Status:** Change status to `Approved to Start`.
      - **Note:** Matthew will fix broken lookup fields (e.g., volume, difficulty) after import and record a Loom tutorial.

### Rimkus Production & Cadence

  - **Production Cadence:** Lawrence's 3 extra articles from this week will be prioritized for next week's batch to maintain the client's strict 5-article/week cadence.
  - **Review Bottleneck:** The client's slow review process is a bottleneck.
      - **Action (Matthew):** Investigate an Airtable automation to tag the team in Slack when a client leaves a comment.
  - **Citation Policy:** The client's `.gov/.org` rule is too restrictive.
      - **Action (Lawrence):** Use the best available source for citations, even if it violates the rule.
      - **Action (Matthew):** Propose a formal exception process to the client to reduce back-and-forth.
  - **Company Context:** The company word count is 900, not 1,400. Lawrence will update this in Atlas to prevent incorrect AI-generated copy.

### Account Handover: Seat

  - **Plan:** Lawrence will take over the Seat account from Moses, who leaves at the end of next week.
  - **Reason:** This avoids a complex information exchange that would be required if Lawrence took over Tavern from Patricia.
  - **Handover:**
      - **Next Week:** Lawrence will receive a brief and complete a few pilot articles with Moses.
      - **Following Week:** Full takeover.
  - **Workload:**
      - **Seat:** 5 articles/week.
      - **Enable:** 5 articles/week (currently paused due to internal client disagreements).
      - **Real City:** 10 programmatic tool pages (minimal lift).

---

## Action Items

**Lawrence Neves (GrowthX)**
- Import forensic keywords to Rimkus Target Keywords; cluster
- Generate Rimkus assignments in Atlas; import to Raw Assignments; set Considering; fix lookups; record Loom
- Use best available links in Rimkus articles; if recurring issue, add to Wed agenda

**Matthew Alves-Hill (GrowthX)**
- Generate Rimkus assignments in Atlas; import to Raw Assignments; set Considering; fix lookups; record Loom
- Add 2 topics to Rimkus production; send weekly roundup to Rimkus w/ next-week titles
- Ping Rimkus re: pending reviews today
- Investigate Slack automation for Rimkus Airtable comments; update Lawrence
- Use best available links in Rimkus articles; if recurring issue, add to Wed agenda
- Update Rimkus company context to 900-word target
- Update Rimkus Looker dashboard today
- Confirm Seat CM assignment w/ Adida; brief Lawrence; coordinate w/ Moses; assign pilot articles

---

## Transcript
**Matthew Alves-Hill:** Okay, I thought this would just be easier than doing this on Slack, so apologies for slamming you straight away.

**Matthew Alves-Hill:** But yeah, everyone uses Airtable a little bit differently, maybe I do too, but I think the main thing is like, Rimkus definitely feel very like, kind of they want to see what's going on.

**Matthew Alves-Hill:** Some clients don't even look at Airtable, Rimkus is like, what's going on?

**Matthew Alves-Hill:** So let me just show you what, how I kind of think about it.

**Matthew Alves-Hill:** Okay, yeah, because I saw you dropped a question in Slack about it, so let's just clarify everything here.

**Matthew Alves-Hill:** Okay, so basically like it's split, right?

**Matthew Alves-Hill:** So client views are, that's for them, it makes like life really easy for them.

**Matthew Alves-Hill:** So whenever, basically, like at the end of the week, whenever we submit assignments, like we just change the status to reviewing and it goes straight into this view.

**Matthew Alves-Hill:** We don't have to touch anything else.

**Matthew Alves-Hill:** And then Rimkus get the tag in Slack and they can just go straight in here and they see all the assignments.

**Matthew Alves-Hill:** In an ideal world, this basically every week, every Friday, we'll have five.

**Matthew Alves-Hill:** I know it's like a little bit off at the moment because I think we're like, there's a little bit of, yeah, so this one needs to be, oh yeah, this is one they fixed.

**Matthew Alves-Hill:** Yeah, so we're like a little bit off, but it's, I mean, it's fine.

**Matthew Alves-Hill:** I think they're quite like nitpicky, but actually like they're also very, they're also being quite slow with us.

**Matthew Alves-Hill:** So that's kind of on them.

**Matthew Alves-Hill:** And then publish is like, this is just so they can see like, hey, this is how many we publish.

**Matthew Alves-Hill:** So that's all good.

**Matthew Alves-Hill:** I think one of the questions you had was like assignments for approval, right?

**Matthew Alves-Hill:** So this section here is basically like this will only be populated really when we've created new assignments that we need them to like sign off on the titles. The keyword research that you're doing around the new forensic topics — once you've generated those, have you done that?

**Lawrence Neves:** Yes, that's the result.

**Matthew Alves-Hill:** Yeah, okay, cool. I know GrowthX moves fast and there's loads of tools, so if you're stuck just let me know. So basically, now you have that sheet, we can go ahead and import that. It's actually pretty straightforward. You can go into the raw assignments view — this has everything. You can group it however you like and then you just import the CSV file.

**Matthew Alves-Hill:** And when it prompts to upload, you can map the fields correctly.

**Matthew Alves-Hill:** In the past, depending on how many assignments it is, I actually find it can be quicker just to do it manually. It's a bit tedious, but you can just go in here and copy the title or copy the short description.

**Matthew Alves-Hill:** Once those are in, you can then change their status.

**Matthew Alves-Hill:** So once they're in and the logic works, then you can change their status to considering.

**Matthew Alves-Hill:** So, no, hang on, assignments for approval.

**Matthew Alves-Hill:** What is this filtered by?

**Matthew Alves-Hill:** Oh, yeah, considering.

**Matthew Alves-Hill:** Okay, yeah, that's a little bit confusing.

**Matthew Alves-Hill:** But basically, these are mirrors of each other.

**Matthew Alves-Hill:** This should really be called considering, too.

**Matthew Alves-Hill:** It's a little bit confusing because the status doesn't match.

**Matthew Alves-Hill:** But it basically means, like, we've generated.

**Matthew Alves-Hill:** A load of assignments.

**Matthew Alves-Hill:** We need you to sign off on them now.

**Matthew Alves-Hill:** They'll leave a comment in there saying, like, cool or no.

**Matthew Alves-Hill:** And once they've gone through all of those in here, then we'll change their status to Approve to Start.

**Matthew Alves-Hill:** And then they'll live with all the other topics we have Approve to Start.

**Matthew Alves-Hill:** So that's the only thing that this view is really for.

**Matthew Alves-Hill:** And in theory, like most of the time, it should be empty because we'll send them a load of topics.

**Matthew Alves-Hill:** They'll approve them.

**Matthew Alves-Hill:** We'll move them all into Approve to Start.

**Matthew Alves-Hill:** And then this view will be empty again.

**Matthew Alves-Hill:** then, yeah, mean, like new assignments, in theory, like we should get to a point with them that like we're choosing the topics and we don't have to get sign off from them.

**Matthew Alves-Hill:** I mean, I assume like with all the assignments you've generated, we're going to have like over 100.

**Matthew Alves-Hill:** So that's a pretty good roadmap.

**Matthew Alves-Hill:** And I want.

**Matthew Alves-Hill:** Kind get heads down on just like getting into a good steady state with them.

**Matthew Alves-Hill:** So, yeah, go ahead and like upload them.

**Matthew Alves-Hill:** If you want, you can actually like, if you get a bit like stuck with getting them into this view or making sure the logic is there, then just leave them in raw assignments, put them as backlog, and then we can like do, we can do that next week.

**Matthew Alves-Hill:** There is kind of a funky thing that like the way these, the way these link.

**Matthew Alves-Hill:** So with all the keywords, you'll need to put the keywords in the, these are new, no, these aren't the new ones.

**Matthew Alves-Hill:** So the key, the new keywords that you found, you'll have to load these in to this view under the right cluster.

**Matthew Alves-Hill:** Once they're, once they're in, you can then go generate the assignments.

**Matthew Alves-Hill:** You plug all the assignments into raw assignments.

**Matthew Alves-Hill:** And then what you have to do to like get the, where is it?

**Matthew Alves-Hill:** Let me give you an example. Hmm, some of this isn't working.

**Matthew Alves-Hill:** But to get, like, the volumes and keyword difficulty into here, it's actually a lookup field.

**Matthew Alves-Hill:** So you actually have to copy the title from here, go back to target keywords, and then copy the title into this cell here.

**Matthew Alves-Hill:** And then the logic, like, works together.

**Matthew Alves-Hill:** But I think the best thing to do is, like, if you upload the keywords in the assignments, then I can, like, I can tidy it up.

**Matthew Alves-Hill:** And I'll record a loom just so that you know for future, like, this is kind of, it took me a while to figure out what was going on.

**Matthew Alves-Hill:** But there's so many linked fields in Airtable.

**Matthew Alves-Hill:** It's really handy, but sometimes it's, like, super just confusing and it's a bit of a mess.

**Lawrence Neves:** So I have a question just quickly.

**Lawrence Neves:** When I upload these keywords, am I also supposed to be giving suggested titles for the topics?

**Lawrence Neves:** Ah, okay.

**Matthew Alves-Hill:** Okay, so once you put the keywords in, you can then go to...

**Matthew Alves-Hill:** Atlas.

**Matthew Alves-Hill:** So have you generated assignments in Atlas before?

**Matthew Alves-Hill:** No.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Okay.

**Lawrence Neves:** That's good to know.

**Matthew Alves-Hill:** That's the gap.

**Matthew Alves-Hill:** So what you do is get the keywords in here, get them clustered correctly to start with.

**Matthew Alves-Hill:** Let's keep this.

**Matthew Alves-Hill:** Let's try and keep this target keywords like tidy as possible.

**Matthew Alves-Hill:** Once you've done that, what you do is go into Atlas or Rimkus.

**Matthew Alves-Hill:** And then in the pipeline, you'll see this assignments pipeline.

**Matthew Alves-Hill:** So when you go in here, you can actually import.

**Matthew Alves-Hill:** So what all you need to do is from that CSV that you've generated with the keywords, you actually don't even need to pull this out of Airtable.

**Matthew Alves-Hill:** You can pull it straight out of that CSV.

**Matthew Alves-Hill:** You have to create a new CSV with like a keyword as the title column, and then all the, all the keywords below it, save that as a CSV file.

**Matthew Alves-Hill:** You upload it into here.

**Lawrence Neves:** I'm still seeing the OS.

**Lawrence Neves:** No, I'm not sharing.

**Matthew Alves-Hill:** Okay, hang on, hang on.

**Matthew Alves-Hill:** Classic, classic Google Sheets.

**Matthew Alves-Hill:** Google me, okay, let me share my entire screen.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Yeah, sorry, this isn't like the best.

**Matthew Alves-Hill:** I should have a better like presentation of this, but okay.

**Matthew Alves-Hill:** So, okay, so from that, let me see if I can give an example.

**Matthew Alves-Hill:** So you go into Atlas's pipelines. This pipeline here, assignments — you go in here and basically you add them one by one.

**Matthew Alves-Hill:** So, let's say it was like the keyword was construction forensics.

**Matthew Alves-Hill:** You can ignore assignment direction unless you already have an article idea, and then you can prompt the pipeline.

**Matthew Alves-Hill:** This pipeline basically just generates an article title and a short description based on top-ranking content in the SERP for that keyword.

**Lawrence Neves:** Wow, okay. That makes sense.

**Matthew Alves-Hill:** And honestly, some of the titles are really not good.

**Matthew Alves-Hill:** It has gotten better, but it is worth, once you get the output, have a look at these.

**Matthew Alves-Hill:** Often, look for dates.

**Matthew Alves-Hill:** Sometimes it'll be best tools of 2023 or something like that.

**Matthew Alves-Hill:** But yeah, the titles aren't really something that we're wedded to, because you'll know when it comes to writing the article, you might find, actually, this title needs to be changed.

**Matthew Alves-Hill:** We don't need to go with exactly what's in the Airtable.

**Matthew Alves-Hill:** It's more for the client just to get an idea, like, this is the kind of angle we can always do later.

**Matthew Alves-Hill:** So you can go one by one, or what you can do is you import — pull that CSV file with all your keywords and open it here. Basically, this thing pops up that lets you map.

**Matthew Alves-Hill:** So it will say like you need to map this field to that field in your CSV.

**Matthew Alves-Hill:** It's really easy.

**Matthew Alves-Hill:** You just like, I think it's even a drag and drop.

**Matthew Alves-Hill:** That's all you need to do.

**Matthew Alves-Hill:** And then open this here and then import.

**Matthew Alves-Hill:** And then you'll have all 50 or however many keywords you found will load into here.

**Matthew Alves-Hill:** And then you just need to run them.

**Matthew Alves-Hill:** Run them for like, I don't know how long they take.

**Matthew Alves-Hill:** These ones are quite long.

**Matthew Alves-Hill:** And this is the output.

**Matthew Alves-Hill:** So now you have your title and short description.

**Matthew Alves-Hill:** Now what you can do is you can export this and then upload it into Airtable.

**Matthew Alves-Hill:** You'll have to map some fields, et cetera, or you can do it manually.

**Matthew Alves-Hill:** Literally just like copying the title into a new box here.

**Matthew Alves-Hill:** Just copy the title, the short description.

**Matthew Alves-Hill:** That's where this is coming from.

**Matthew Alves-Hill:** Here and here.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** And then the keyword list — clearly some logic is broken down in here.

**Matthew Alves-Hill:** But I would just do that.

**Matthew Alves-Hill:** Like I would say if we get the keywords in and assignments generated, that's really the blocker.

**Matthew Alves-Hill:** We don't need to worry too much about the logic.

**Matthew Alves-Hill:** That'll be a quick fix.

**Matthew Alves-Hill:** But I do want to share like the new assignments because they've been hot on the forensics.

**Matthew Alves-Hill:** So that's that.

**Matthew Alves-Hill:** Again, if you have any questions, I might have even recorded some looms on some of this Airtable stuff.

**Matthew Alves-Hill:** I'll see if I can dig it out for you.

**Lawrence Neves:** Yeah.

**Matthew Alves-Hill:** Once you've used it for a few weeks, have you used it before Airtable?

**Matthew Alves-Hill:** Yes.

**Matthew Alves-Hill:** I used it when I was in animals.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Yeah.

**Lawrence Neves:** Cool.

**Matthew Alves-Hill:** All right.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Now the other question I had is...

**Matthew Alves-Hill:** So in production at the moment, I'm a little bit, so I'm just slightly confused.

**Matthew Alves-Hill:** Is this, so I loaded in five earlier this week.

**Matthew Alves-Hill:** There's eight in here now, and I'm not sure where the other three have come from.

**Lawrence Neves:** Right.

**Lawrence Neves:** So I may have loaded them, not knowing that you had already preloaded, because I went through the thing and figured out which ones would be the easiest to win, you know, the easy wins.

**Lawrence Neves:** So I added, actually, I didn't know you were going to, you were going to add to that.

**Lawrence Neves:** So I added more.

**Lawrence Neves:** When I saw that there were yours in there, I think I prioritized it, but I may have, I may have skipped one or two just to get in.

**Lawrence Neves:** Okay.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** That's fine.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** So again, just normally with other clients, I wouldn't really worry too much, but Rimka seemed to like one, like we want five this week, then you publish five, then we want five.

**Matthew Alves-Hill:** It's like very corporate, not a vibe.

**Matthew Alves-Hill:** So that's completely fine.

**Matthew Alves-Hill:** Like the main point.

**Matthew Alves-Hill:** We deliver five this week, so I can see that you've got, that's great.

**Matthew Alves-Hill:** And then, so these three, what I'm going to do is say, these three, I'm going to add to our, so I'll send what we're going to write next week in this, like, on basically every Friday, I'll send them a message with like a weekly roundup, and then telling them the titles that we're going to work on next week.

**Matthew Alves-Hill:** Since you've done these five, I'm going to make sure that these three are in for next week, and then I'm going to add two, two more.

**Matthew Alves-Hill:** can see we've even got a refresh in here, which is great.

**Matthew Alves-Hill:** So I'll add two more topics in there.

**Matthew Alves-Hill:** Or if you have, if you have ideas already about topics that you want to do, that's fine.

**Matthew Alves-Hill:** I don't mind setting them.

**Matthew Alves-Hill:** I'll pick them and we can, we'll like work that out as we go, maybe.

**Matthew Alves-Hill:** Yeah, okay, cool.

**Matthew Alves-Hill:** So then basically there will be five, and then each week we have.

**Matthew Alves-Hill:** Five in production.

**Matthew Alves-Hill:** It's super clear for them.

**Matthew Alves-Hill:** Again, this isn't one of their views, but they may pop into this to see what's going on.

**Matthew Alves-Hill:** So that clears that up.

**Matthew Alves-Hill:** That's great.

**Matthew Alves-Hill:** And then ready to publish.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** So that's there.

**Matthew Alves-Hill:** They have been slow on reviewing.

**Matthew Alves-Hill:** So I'm going to push them today.

**Matthew Alves-Hill:** I'm going to see if I can set an automation that like tags us when they comment.

**Matthew Alves-Hill:** Yes, that would be really helpful.

**Matthew Alves-Hill:** Yeah, it's really not good.

**Matthew Alves-Hill:** This like setup is good.

**Matthew Alves-Hill:** Yeah, I need to have a look because I might be able to.

**Matthew Alves-Hill:** Okay, I'll let you know.

**Matthew Alves-Hill:** And then it will ping us in Slack and be like, hey, they left a comment because otherwise, like, it's a lot of manual checking.

**Matthew Alves-Hill:** It's actually really annoying.

**Matthew Alves-Hill:** I don't know why we can't actually just add them to a table.

**Matthew Alves-Hill:** But anyway, that's about my station.

**Matthew Alves-Hill:** Yeah, let me see if I can wait.

**Matthew Alves-Hill:** wait.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Otherwise, like, we're in a good spot.

**Matthew Alves-Hill:** basically means we'll have, yeah, we'll basically be back on track with this, like, five by five by five cadence.

**Lawrence Neves:** Cool.

**Matthew Alves-Hill:** I think that's everything.

**Matthew Alves-Hill:** Is there anything, do you have any questions while we're on, like, Rimkus-wise that I can help with or anything?

**Lawrence Neves:** No, so my priority today is to get them these five, which are, right now, they're just in the fact-checking state.

**Lawrence Neves:** Like, they're written, I've pared them down to what they need to be, but because we had problems with the links, I'm having some agentic AI problems with the links, so I'm trying to figure that out, but I'm going over that meticulously, so we don't have any repeat of them asking for things.

**Lawrence Neves:** Now, their writing guidelines say that they want .org, .gov, or Rimkus only, yeah, for their citations, but every once in a while,

**Lawrence Neves:** We'll put one in that we know speaks exactly to what they're talking about.

**Lawrence Neves:** Should I notate in that article?

**Lawrence Neves:** I know that this isn't one of the links you asked for, because they're asking for test cases, and they don't have the test cases on RIMCIS.

**Lawrence Neves:** So they asked us to anonymize it, which we have, but the link to what that test case actually goes to is from the Seattle Times.

**Lawrence Neves:** It's from a newspaper.

**Lawrence Neves:** It's not .gov or .org or RIMCIS.

**Lawrence Neves:** She's been, Alicia has been back and forth with that.

**Lawrence Neves:** Like, sometimes she'll accept it, and sometimes she'll say, no, take this link out.

**Lawrence Neves:** Absolutely fine, but I don't want to keep annoying her by putting links in that I know she's going to have an issue with.

**Lawrence Neves:** So I thought, do we get ahead of that and just make a comment in the document?

**Lawrence Neves:** Hey, I know this isn't the right link, but it's the only one that goes to this story.

**Matthew Alves-Hill:** Yeah, I hear what you're saying.

**Matthew Alves-Hill:** To be honest, I would rather

**Matthew Alves-Hill:** Like, try and reduce the amount of back and forth with them because I feel like they're the type that might, we might just end up like in an endless, you know, it's not, it's not helpful for you to have to be like tracking tiny edits that they've made, you know, a week later.

**Matthew Alves-Hill:** It's just like, that's not efficient.

**Matthew Alves-Hill:** So I'm in the camp that's like, we're the experts here.

**Matthew Alves-Hill:** We're making the calls.

**Matthew Alves-Hill:** If I will raise, I think for now, like, let's, in those situations, use, just use the link, use the best link.

**Matthew Alves-Hill:** If they keep raising it, I will add it to the agenda on Wednesday and say, hey, like, we know this is the rule, but in certain cases, it's the only source.

**Matthew Alves-Hill:** So would you rather us, like, ditch it completely or put it in because we can't have the back and forth, like, every single time?

**Lawrence Neves:** Okay.

**Matthew Alves-Hill:** Yeah, but otherwise, like, it's the same with edits, you know, like, they, in my view, they get...

**Matthew Alves-Hill:** They get one shot.

**Matthew Alves-Hill:** Ultimately, we're judged on our cadence and the performance of the blogs, and that means we have to publish.

**Matthew Alves-Hill:** And so they're paying us for that.

**Matthew Alves-Hill:** So when it comes to review, it's like, hey, here's your chance to review.

**Matthew Alves-Hill:** You've seen it.

**Matthew Alves-Hill:** Now it's in.

**Matthew Alves-Hill:** Accept their suggestions, make their edits, and then we push it to publish.

**Matthew Alves-Hill:** And if we come later on and say, oh, we would have wanted more rounds of review on this, we can pull the page.

**Matthew Alves-Hill:** Which, like, worst case, we pull the page live, but I don't think it's ever going to get to that.

**Matthew Alves-Hill:** They get a chance to look, that's our, like, buffer zone, now we publish.

**Matthew Alves-Hill:** We have to, like, show progress on this.

**Matthew Alves-Hill:** And I don't want you, like, just buried and, you know, like, changing punctuation and stuff like that.

**Matthew Alves-Hill:** On that point, the 1,400 figure, that's in the company context, right?

**Matthew Alves-Hill:** The 1,400.

**Matthew Alves-Hill:** Yes.

**Lawrence Neves:** Now they're saying 900, right?

**Lawrence Neves:** Okay.

**Matthew Alves-Hill:** Yeah, so I'll change that.

**Lawrence Neves:** I'll make sure to change that today.

**Matthew Alves-Hill:** Yeah, yeah, let's change that because Atlas loves just like, I don't know if you've noticed, but even in the copy, like whatever is in the company context, like there are certain phrases that just get repeated over and over again that taken straight out of the company context, which is kind of actually kind of frustrating, but cool.

**Matthew Alves-Hill:** Cool, okay.

**Matthew Alves-Hill:** What else?

**Matthew Alves-Hill:** I'm updating Looker today too, because we have new articles in there, so.

**Matthew Alves-Hill:** Yes, yeah, let's do that on, basically like we have, because we sync on Wednesday, I just want like the most up-to-date Looker Dash by Wednesdays.

**Matthew Alves-Hill:** So whether you, like I think to do it on Friday is great.

**Matthew Alves-Hill:** Let's see how the cadence goes.

**Matthew Alves-Hill:** If we start getting a quick review phrase and we're publishing on a Monday, you know, they're reviewing over the weekend or they're reviewing on Monday and we publish on Tuesday, then the more.

**Matthew Alves-Hill:** The data we get into Looker before the sync, the better the reporting looks, but that's completely fine.

**Matthew Alves-Hill:** Yeah, yeah.

**Matthew Alves-Hill:** Okay, so that's Rimkus.

**Matthew Alves-Hill:** Next week, so I've seen the layout of the new structure.

**Matthew Alves-Hill:** Patricia, I think I'm going to put you on seat instead of Tavern just because Patricia, who's another CM, she joined and basically went straight on to Tavern.

**Matthew Alves-Hill:** So she's been working on that account for like 13 weeks and there's like a lot of, it will be easier for I think both of you guys to like not have to do that information exchange.

**Matthew Alves-Hill:** So I want to keep her on there, which means you'll probably take over seat.

**Matthew Alves-Hill:** The current CM Moses, he's leaving at the end of next week.

**Matthew Alves-Hill:** So I do.

**Matthew Alves-Hill:** I think you're done with LightSource, right?

**Matthew Alves-Hill:** It's just Enable.

**Matthew Alves-Hill:** LightSource is out.

**Lawrence Neves:** It's just Enable and Remkes right now.

**Lawrence Neves:** Okay, rad.

**Lawrence Neves:** Yeah.

**Matthew Alves-Hill:** So next week, I'll probably give you a couple of...

**Matthew Alves-Hill:** I'll brief you on Seat a little bit, and then maybe we can do a few tasks and split the work with Moses because he is working.

**Matthew Alves-Hill:** But it will give you a chance to just get familiar with the brand and maybe one or two pilot articles just to help you get up to speed.

**Matthew Alves-Hill:** But I'll confirm that probably on Monday.

**Matthew Alves-Hill:** I just need to double-check with Adida.

**Lawrence Neves:** That's fine.

**Matthew Alves-Hill:** What do you...

**Matthew Alves-Hill:** What's the capacity for Enable?

**Matthew Alves-Hill:** What's the delivery amount for them?

**Lawrence Neves:** So they're five a week, but they're still having issues with the calibration blog, and they're going back and forth with Ada.

**Lawrence Neves:** One of the issues is that they...

**Lawrence Neves:** We asked for something to be added to the objective pipeline, that talks about...

**Lawrence Neves:** Their product because there was no product description or product overview, not an in-depth one.

**Lawrence Neves:** The other issue with them is that we wrote blogs for them because we had thought the calibration blog was good.

**Lawrence Neves:** And then they decided to bring in PMs to look at the blogs.

**Lawrence Neves:** And the PMs and the marketing people do not agree on what these blogs should be like.

**Lawrence Neves:** So we're kind of still, we're just waiting for that one piece and then for the ejected pipeline to be done.

**Lawrence Neves:** And then Ada says that they're going to get the, we already produced five for them that they never looked at.

**Lawrence Neves:** And she's going to, she said that after we get all of this in, we may rerun the stories and then they can, they can go from there, but there'll be five a week.

**Lawrence Neves:** Okay, cool.

**Matthew Alves-Hill:** So they're, okay.

**Matthew Alves-Hill:** What week are they in now?

**Matthew Alves-Hill:** Like six or something?

**Lawrence Neves:** Yeah, you know, they, they came out of strategy sprints.

**Lawrence Neves:** So yeah.

**Lawrence Neves:** Oh, okay.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** All right.

**Matthew Alves-Hill:** Um, okay.

**Matthew Alves-Hill:** So that's fine.

**Matthew Alves-Hill:** Then seat is also five articles.

**Matthew Alves-Hill:** And then there's like real city.

**Matthew Alves-Hill:** 10 of these tool pages, but it's, like, programmatic, so the pipeline's actually great.

**Matthew Alves-Hill:** Like, it's a very minimal lift.

**Matthew Alves-Hill:** It's basically, like, checking the internal links when we go to publish.

**Matthew Alves-Hill:** So that's a pretty, like, one.

**Matthew Alves-Hill:** So I will, yeah, I need to chat to Moses.

**Matthew Alves-Hill:** So on your radar, like, probably a couple of things to do for Seed next week just to try and get you up to speed.

**Matthew Alves-Hill:** And then from the following week, then it will be, like, a full takeover.

**Matthew Alves-Hill:** I'll make sure everything is documented for you from Moses for the handover.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** I think that's it.

**Matthew Alves-Hill:** Okay.

**Lawrence Neves:** If I have any questions, I'll make sure to tag you in Slack.

**Lawrence Neves:** I appreciate all the help.

**Lawrence Neves:** I mean, I know it's kind of a lot of hand-holding right now, but I think I'm getting it down, and I think that this is all very, very helpful.

**Matthew Alves-Hill:** No, no, seriously, like, I started in March, I think, and it was, like, I remember my...

**Matthew Alves-Hill:** The first month, I was just like, what the hell is all of this?

**Matthew Alves-Hill:** And we weren't even on Atlas yet.

**Matthew Alves-Hill:** We were still on Aerofs, and it was like, and I was really lucky.

**Matthew Alves-Hill:** had, like, a couple of people just helped.

**Matthew Alves-Hill:** Like, I just asked stupid questions, and it made me learn, like, way quicker.

**Matthew Alves-Hill:** So please, like, if you have questions, get me on Slack.

**Matthew Alves-Hill:** I'll do all I can to help.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Thanks, Matt.

**Lawrence Neves:** I appreciate that.

**Lawrence Neves:** All right, Lawrence.

**Lawrence Neves:** Thank you, Ethan.

**Lawrence Neves:** Go.

**Lawrence Neves:** Thank you.
