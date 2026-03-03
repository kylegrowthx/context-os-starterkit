# Sulaman - Looker Dashboard Review

<metadata>
date: 2025-08-06
time: 14:35 UTC
duration: 38 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar (GrowthX), Sulaman Ahmed (GrowthX)
fathom_recording_id: 78828752
fathom_url: https://fathom.video/calls/372438934
share_url: https://fathom.video/share/7kMKcc9zzHi3NxzPTD4yQKzRyS8RAL2w
source: fathom
enriched_on: 2026-03-03 14:25 UTC
</metadata>

---

## Summary

Vivek and Sulaman debugged Looker dashboards across six client accounts (Monograph, Discern, Firework, Metronome, Blossom, Home Base) and updated dashboard links in the Notion database. They decided to standardize regex matching from "contains" to "match" in Google Search Console (GSC) data to prevent broad-match errors, delegating responsibility for URL accuracy to MEs (Marketing Engineers). Sulaman will remove conditional formatting colors from table cells, update the Notion links for all client dashboards, and coordinate with Isra on splitting publishing workload during peak hours (Thursdays/Fridays).

---

## Context

Vivek is a senior analytics engineer at GrowthX labs responsible for Looker dashboard architecture, while Sulaman is a GrowthX team member managing dashboard updates and client implementation. This was a working session to review and fix technical issues across six active client Looker instances that GrowthX has built and maintains. The immediate driver was discovering that regex "contains" matching in GSC data was pulling in overly broad URL matches (e.g., matching both "blog/ai-personalization-conversion-tactics" and "blog/ai-personalization-examples" when filtering for the second one), which distorts performance data. The session evolved to also address ME confusion about which dashboard links to use and dashboard styling issues that were degrading visibility of data.

---

## Relevance

- **To GrowthX Delivery:** Standardizing regex matching logic to "match" instead of "contains" in GSC filters prevents data inflation and ensures accurate performance attribution to client content. Cleaning up Looker interface (removing dark red conditional formatting, fixing dashboard links in Notion) reduces ME confusion and support load. The decision to make ME data accuracy (correct URL input in Airtable) a shared responsibility clarifies accountability rather than over-engineering dashboard logic.

- **To GrowthX Business Development:** Looker dashboard quality and accuracy directly impacts client trust in GrowthX analytics work and renewal signals. A single broad-match error (pulling 1000 URLs instead of 200) compounds across multiple clients and damages credibility. MEs now understand the Notion-to-Looker link system, reducing client-facing delays.

---

## Overview

- Change regex contains to regex match in Google Search Console (GSC) data for more accurate URL matching
- Update Looker dashboard links in the Notion database to ensure MEs access correct reports
- Remove conditional formatting colors from tables for better visibility
- Collaborate with Isra to manage publishing workload during peak times (Thursdays/Fridays)

---

## Key Topics

### URL Matching in Looker Dashboards

  - Identified issue with regex contains potentially causing broad matches
  - Decided to change GSC data to use regex match for more precise URL matching
  - EMIs responsible for providing correct URLs in Airtable
  - Action: Update all client dashboards to use regex match for GSC data

### Dashboard Presentation and Accessibility

  - Removed dark red conditional formatting colors from URL Flux and Delta tables
  - Updated Looker dashboard links in Notion database to prevent confusion
  - Deleted irrelevant data sources (e.g., DataGrid from Flossom dashboard)
  - Action: Ensure all MEs receive the instructional video for using Looker dashboards

### Publishing Workflow Management

  - Discussed challenges with high volume of publishing requests on Thursdays/Fridays
  - Suggested collaboration with Isra to distribute workload during peak times
  - Action: Sulaman to connect with Isra to establish a workload-sharing system

### Linear Template Creation

  - Sulaman seeking guidance on creating and using templates in Linear
  - Vivek unsure about the process; suggested consulting with Andy

---

## Action Items

**Sulaman Ahmed (GrowthX)**
- Change regex contains to regex match for GSC in all Looker dashboards (Monograph, Discern, Firework, Metronome, Blossom, Home Base)
- Remove conditional formatting colors from URL Flux and Delta tables
- Update all Looker dashboard links in Notion database for clients where GrowthX built dashboards
- Contact Isra about splitting publishing workload on Thursdays/Fridays based on capacity
- Consult with Andy about creating and using templates in Linear
- Ensure all MEs receive the Looker dashboard instructional video

**Vivek Shankar (GrowthX)**
- Verify regex match changes across all six client Looker dashboards are standardized

---

## Transcript
**Vivek Shankar:** Okay, now can you go to the second tab, please?

**Sulaman Ahmed:** Okay.

**Sulaman Ahmed:** And in the second graph, see the patterns for the URLs.

**Sulaman Ahmed:** Yeah, there is something you would spot, some of the URLs are starting with WWW, some of them are not.

**Sulaman Ahmed:** I researched on it a bit and I think there is a possibility if we use the same structure that we use in Google Analytics, it can work for Google Search Console too.

**Sulaman Ahmed:** Because the way regex works is, I reckon it identifies the pattern.

**Sulaman Ahmed:** So if that particular part exists within the URL, it will be considered as a match.

**Sulaman Ahmed:** So if we just had...

**Sulaman Ahmed:** The slug after the domain, it should ideally work in this case.

**Sulaman Ahmed:** Am I missing something?

**Sulaman Ahmed:** Yeah, it will work.

**Vivek Shankar:** The reason I have the entire URL and I say regex match is because regex contains can be a little broad sometimes. If we say regex contains just "blog", it should be fine in theory.

**Vivek Shankar:** The issue is if they have two pages with similar long slugs, it's not going to be a problem for each individually.

**Sulaman Ahmed:** So if common slug is used in two different pages.

**Sulaman Ahmed:** No.

**Vivek Shankar:** If this is a good example, actually, these two here.

**Vivek Shankar:** So the first one is AI personalization conversion tactics.

**Vivek Shankar:** I'd confirm if it's two S's or one. There might be an error in their Airtable. But let me show you the actual problem.

**Vivek Shankar:** So we have "blog/ai-personalization-conversion-tactics" and "blog/ai-personalization-examples".

**Vivek Shankar:** Now, both of these are growthx URLs, which is fine.

**Vivek Shankar:** But let's say for some reason, this one here or one of these was not a growthx URL.

**Vivek Shankar:** That's right.

**Vivek Shankar:** If you use "contains" and just say "blog/ai-personalization-examples", it might incorrectly pick up performance from "blog/ai-personalization-conversion-tactics" as well.

**Vivek Shankar:** In fact, the way it is right now, it will still pick it up because we're saying contains, we're not saying matches.

**Vivek Shankar:** So that's the, that's usually the issue with contains.

**Vivek Shankar:** Like, it'll, it doesn't look for exact matches.

**Vivek Shankar:** It does a broad match, basically.

**Sulaman Ahmed:** So even if from the complete string, it can still match a subset, that could be an issue.

**Sulaman Ahmed:** But I think just for the protocols, like for HTTPS and www.

**Sulaman Ahmed:** if we skip them, that would, I think, make it better.

**Sulaman Ahmed:** On Search Console, some URLs have www and some don't. If the pattern is "www.example.com" but the actual URL doesn't have www, it would fail to match.

**Vivek Shankar:** It won't match. Actually, they don't seem to have redirected these URLs, so they're just inconsistent in Search Console. Yeah, I see your point though.

**Sulaman Ahmed:** I think we need to check with Jen about this. I didn't know there was a problem initially until you pointed out the pattern. I understand now that we need to change the regex handling. When ChatGPT gives me configurations, I'll review the complete output, especially the conditional logic. Right now we have these dashboards: Flossom, Engine, Interval, Firework, Discern, Monograph, Metronome, School AI, Outreach, and Home Base.

**Sulaman Ahmed:** So we have quite a few, but I was thinking like, well, let's, let's do this.

**Vivek Shankar:** I mean, first thing what I would do is I would, yeah, you can, you can shorten it to blog slash whatever, the slug.

**Vivek Shankar:** I think you can do that, right?

**Vivek Shankar:** The next thing is I would actually change the regex contains to regex match if you're doing that.

**Sulaman Ahmed:** Understood.

**Sulaman Ahmed:** I will actually do a bit of experiment on this one.

**Sulaman Ahmed:** Considering our case study, what would work best for us?

**Sulaman Ahmed:** Like if we want to match it, a complete string or what can be the ideal case in this one?

**Vivek Shankar:** You can take slash blog, actually.

**Vivek Shankar:** I think it will be fine.

**Vivek Shankar:** Because, yeah, because like you said, the www and non-ww URLs are a bit of a problem here.

**Vivek Shankar:** Like some of these have a www, some of them don't.

**Vivek Shankar:** I think we can just go with slash blog.

**Vivek Shankar:** Well, actually, you can't use regex match alone, because it needs the entire URL.

**Sulaman Ahmed:** One more thing, if you would see here, we have Webflow links too.

**Sulaman Ahmed:** So they are staging links, the real ones.

**Sulaman Ahmed:** Yeah, Webflow.

**Sulaman Ahmed:** And if you just had to start from domain, those could have been skipped over, because the real URLs would be without the Webflow.

**Vivek Shankar:** Yeah, of course.

**Vivek Shankar:** Yeah, that's a good point.

**Vivek Shankar:** Like, look, at some point, we need to draw the line, and we need to say, like, you know, we can't fix it.

**Vivek Shankar:** This is how it is in their Airtable, so that's how it is.

**Vivek Shankar:** I need to think about what to do here.

**Vivek Shankar:** I think it's best if we kick this back to Jen for two reasons.

**Vivek Shankar:** One is, we cannot use a Regex match, because the Regex match looks for the entire string, right?

**Vivek Shankar:** And Search Console returns the entire URL, so we cannot use a slash blog.

**Vivek Shankar:** If we use, I guess, contains and then slash log, we're going to have that issue with what I just showed you, like the personalization tactics, the personalization examples, like this broad match sort of thing.

**Vivek Shankar:** My guess is that's going to become a problem.

**Vivek Shankar:** So that's why I'm, you know, I'm a bit iffy about using it.

**Sulaman Ahmed:** What if, what if before comparison, we add one more cleaning thing here, like any function that cleans the landing page URL we are getting back.

**Sulaman Ahmed:** If that trims it down to the part without the domain, like I worked with projects, there is a possibility to do that.

**Sulaman Ahmed:** Just drop the domain part, have the remaining part left, and then do a comparison using regex.

**Sulaman Ahmed:** That way we will be sure both of them are in same syntax.

**Sulaman Ahmed:** But if you want, I can give it a try.

**Vivek Shankar:** No, I think that's over-engineering it because...

**Vivek Shankar:** The Airtable, the correct URL, pasting the correct URLs, that is the EMI's responsibility.

**Vivek Shankar:** It's not our responsibility.

**Vivek Shankar:** So if they are pasting the wrong URLs in there, that's on them.

**Vivek Shankar:** For example, these web flow things over here, if the EMI, who's the EMI?

**Vivek Shankar:** I think it's Jen.

**Vivek Shankar:** If she comes back and says, oh, we're not getting correct data, say, well, your URLs are incorrect.

**Vivek Shankar:** There's nothing we can do, right?

**Vivek Shankar:** So I think at some point, they have to take responsibility.

**Vivek Shankar:** We can build as many fail-safes as possible, but yeah, how much can we build, right?

**Vivek Shankar:** Exactly.

**Vivek Shankar:** So there will always be a human that's possible in this one.

**Vivek Shankar:** Yeah, like over here, can see URLs are incorrect.

**Vivek Shankar:** I was going to say update.

**Vivek Shankar:** But yeah, in this case, what I would say is she needs to figure this out.

**Vivek Shankar:** From what I would

**Vivek Shankar:** What I then do is, I would change, I would still change the regex contains to regex match.

**Vivek Shankar:** I think a regex match just makes more sense.

**Vivek Shankar:** Got it.

**Sulaman Ahmed:** Like, if, just saying on an abstract level, considering there will always be an error condition, do you think if we just copy the Google Analytics script, same to the Google console, it would kind of work, would make the process easy, they don't have to separately create the URLs, the protocol's problems would be resolved, and like, only the problem of, like, matching with a different subset of string would exist, that still exists in this case.

**Vivek Shankar:** Yeah, but then you won't get accurate data, right?

**Vivek Shankar:** Because, like, if you, if you do that, if you use the same sort of case statement for both GA4 and for GSE, the, you cannot use regex match.

**Vivek Shankar:** You have to use.

**Vivek Shankar:** So if you use regex contains, and if there is a large number of broad match URLs, then the data is going to be incorrect.

**Vivek Shankar:** And that's a bigger problem.

**Sulaman Ahmed:** That is correct.

**Sulaman Ahmed:** But still we are using regex contains.

**Sulaman Ahmed:** Yes.

**Vivek Shankar:** So that's why we need to change this to regex match.

**Vivek Shankar:** Got it.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** So we are planning to change this to regex mag, and then it would be the responsibility of team to make sure we have the correct URLs in there.

**Sulaman Ahmed:** Yes.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** That makes much more sense.

**Vivek Shankar:** Got it.

**Vivek Shankar:** Yes.

**Vivek Shankar:** The reason I'm pushing back on it is because I had a similar problem.

**Vivek Shankar:** When I first built the lookers for RAMP, we had that problem.

**Vivek Shankar:** They have about, I don't know, 4000 URLs or something.

**Vivek Shankar:** And I was using regex contains for our 200 URLs.

**Vivek Shankar:** But we were pulling in performance data for about 1000 URLs, because the broad phrase match was pulling in everything.

**Vivek Shankar:** And it was embarrassing.

**Vivek Shankar:** So, yeah, so I think it's partially my fault.

**Vivek Shankar:** I didn't tell you this before because I asked you to copy Galileo.

**Vivek Shankar:** then, yeah, so you see, for here, we're using regex match.

**Vivek Shankar:** This is correct.

**Vivek Shankar:** Just for GSC, I think we need to change that.

**Vivek Shankar:** So already using regex match.

**Sulaman Ahmed:** But the Google search console, we need to use the same function, got it?

**Sulaman Ahmed:** Understood.

**Vivek Shankar:** And just leave the URLs as is because it's, that's the, that's on the ME, like they need to give us the correct URLs.

**Vivek Shankar:** Understood.

**Vivek Shankar:** So basically, we need to do it for all of these monograph, discern, firework, metronome, blossom, and home base.

**Vivek Shankar:** Let me check home base.

**Vivek Shankar:** I did this yesterday.

**Sulaman Ahmed:** A home base is the one that just had Google search console.

**Sulaman Ahmed:** So.

**Sulaman Ahmed:** Yes, correct.

**Vivek Shankar:** So, I changed all this.

**Vivek Shankar:** Is that school yet?

**Sulaman Ahmed:** See the resource that it is putting?

**Sulaman Ahmed:** It is analytics.

**Sulaman Ahmed:** this is GA4.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So, this needs to be hidden.

**Vivek Shankar:** Hmm.

**Vivek Shankar:** How did I miss this page?

**Vivek Shankar:** I think everything else is fine.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Oh, yeah.

**Vivek Shankar:** So, I just need to change this tool.

**Vivek Shankar:** Sorry, I'll do it right now.

**Vivek Shankar:** before he just notices.

**Vivek Shankar:** medium goes away.

**Vivek Shankar:** Yes.

**Vivek Shankar:** This.

**Vivek Shankar:** Okay, two of course, takes, yep.

**Vivek Shankar:** Four, ten.

**Vivek Shankar:** We got a leaf pillar.

**Vivek Shankar:** Service.

**Vivek Shankar:** We don't need this.

**Vivek Shankar:** Let me just check the resource real quick.

**Vivek Shankar:** I don't know why this traffic keeps showing up, like I keep deleting it, but.

**Sulaman Ahmed:** I think the copy, I used to, I have actually started cleaning them now, but for the initial ones, I used to keep the original tape just in.

**Sulaman Ahmed:** No, I cleaned it yet.

**Vivek Shankar:** today, but it still doesn't.

**Vivek Shankar:** OK, so even I have made this thing, I'll just put contain lower here.

**Vivek Shankar:** Yeah, I think we just need to maybe say match for home base.

**Vivek Shankar:** Just need to replace it.

**Vivek Shankar:** We don't have too many URLs, so it's a good thing.

**Vivek Shankar:** So yeah.

**Vivek Shankar:** Got it.

**Vivek Shankar:** Cool.

**Sulaman Ahmed:** There was a ticket today that was from Was it outreach?

**Vivek Shankar:** I reckon it was from Dilijay.

**Sulaman Ahmed:** They had some feedback regarding LLM.

**Vivek Shankar:** Yeah, this is not our responsibility.

**Vivek Shankar:** She's like LLM and integrating scrunch and all this, that is with Dave.

**Vivek Shankar:** So we're not doing it.

**Vivek Shankar:** I already responded to that ticket.

**Sulaman Ahmed:** There's one small thing, if you can kindly help me with that.

**Sulaman Ahmed:** Yesterday, was trying to...

**Sulaman Ahmed:** To create a template on Linear, since I have never created a template on Linear, I was unsure, like, how can someone create a template and then use that template to create a ticket?

**Sulaman Ahmed:** Good question.

**Vivek Shankar:** I'm not sure how you create templates, to be honest.

**Sulaman Ahmed:** I can share what I found.

**Sulaman Ahmed:** On the analytics section, click on three dots, team settings, templates, this one, yeah, the one template you're saying, this is what I'll try to do.

**Sulaman Ahmed:** This is what ChatGPT recommended, and I followed what it guided me to do.

**Sulaman Ahmed:** But if this template existed, how can someone use it while raising a ticket?

**Sulaman Ahmed:** Yeah.

**Vivek Shankar:** Let me just go back.

**Vivek Shankar:** So basically, you create a new ticket, then you click on it in analytics.

**Vivek Shankar:** I was trying this, and it says template over here.

**Vivek Shankar:** So when I click template, it shows up, but it's not doing that for analytics.

**Vivek Shankar:** We'll check why.

**Vivek Shankar:** It's in the settings.

**Sulaman Ahmed:** We might have to move to workspace to make it kind of live or something like that.

**Vivek Shankar:** The template isn't showing up for analytics.

**Sulaman Ahmed:** I have a meeting later with Andy.

**Sulaman Ahmed:** Maybe I'll ask her then.

**Vivek Shankar:** Yeah, Andy knows this stuff.

**Vivek Shankar:** She helped me out with Linear before. Let's just take a quick look at some of these Looker dashboards.

**Vivek Shankar:** I was thinking we can maybe just make a checklist because I noticed some small issues here and there.

**Vivek Shankar:** I just want to check for any issues.

**Vivek Shankar:** Okay.

**Vivek Shankar:** I can change this to match. One issue I found — instead of "non-growthx", it says "non-monograph URL" in some places. It's not a major issue, but worth standardizing.

**Vivek Shankar:** A filter called "strappy" keeps showing up, even after I delete it.

**Vivek Shankar:** This also needs to be changed to match.

**Vivek Shankar:** In some places it says "match" and in others "contains", so I want to standardize it. Similar issue — a "Stats" filter keeps reappearing.

**Vivek Shankar:** Got it.

**Sulaman Ahmed:** I think it's linked in some way that's pulling it back. As we can see in the data, there's traffic from it.

**Vivek Shankar:** Monograph.

**Vivek Shankar:** So that brand filter was another one with some issues.

**Vivek Shankar:** Go ahead.

**Vivek Shankar:** So discern.

**Vivek Shankar:** Here it's using regex match,

**Vivek Shankar:** Okay.

**Vivek Shankar:** So all GSC filters need to change to match.

**Vivek Shankar:** Like in GSC, like all the GSCs need to change to match essentially.

**Vivek Shankar:** Then this one.

**Vivek Shankar:** Yeah, that's fine.

**Vivek Shankar:** Just give everything a once over to make sure it's consistent.

**Sulaman Ahmed:** I'll review the issues we spotted and check for different URL patterns.

**Sulaman Ahmed:** I'll make sure to review everything once it's done.

**Sulaman Ahmed:** There's one thing I wanted to discuss. Last week, I kept getting publishing tickets come in on Thursday and Friday. Usually Thursdays I'll get them, but since Friday is the last day, everything piles up and I get overrun.


**Sulaman Ahmed:** Do you have any suggestions on how to avoid this?

**Vivek Shankar:** Yeah, I really don't have a solution for you, because the reason everything comes in on Thursday and Friday is because Monday to Thursday is when articles get created, and then Friday we stage and we send it to the clients, the reviews.

**Vivek Shankar:** That's why everything comes on Thursday and Friday. On a weekly basis, every account in the company publishes on Friday.

**Vivek Shankar:** What I can suggest is, you know, there's another publisher, Isra, I don't know if you've ever spoken to him, you can maybe ask Andy if you can push some of your requests to him.

**Vivek Shankar:** You can DM him and send the Linear ticket details.

**Sulaman Ahmed:** So we could collaborate based on workload.

**Sulaman Ahmed:** If he has a heavier workload some days, I could help, and vice versa.

**Vivek Shankar:** You can discuss it.

**Vivek Shankar:** Isra is a he, by the way.

**Sulaman Ahmed:** I think I had a discussion with him before.

**Sulaman Ahmed:** Jessalyn messaged me about two things. One, the dark red colors in the dashboard make it difficult to visualize the content.

**Vivek Shankar:** Which dashboard is this?

**Sulaman Ahmed:** Flossom.

**Vivek Shankar:** Flossom.

**Vivek Shankar:** Okay, we can remove the coloring.

**Sulaman Ahmed:** I carried the coloring over from somewhere. She should be seeing the data grid. Data grid isn't on my list.

**Vivek Shankar:** I'm pretty sure she's looking at the wrong report.

**Vivek Shankar:** This is something I wanted to address with you too — a lot of the MEs are confused about which Looker dashboard to use. In the Notion database, I have all the client Looker links. I think MEs are just clicking the link without checking which client it's for. That's why she's confused.

**Sulaman Ahmed:** She's seeing Flossom results on the DataGrid dashboard. That's wrong.

**Vivek Shankar:** DataGrid is my account. She's definitely looking at the wrong one. I think she's looking at the wrong URL. I'll send her the correct Flossom link and update the Notion database.

**Sulaman Ahmed:** Can you show me how to remove those red colors?

**Vivek Shankar:** Click on the table, go to Style, then Conditional Formatting, and remove the color rules.

**Sulaman Ahmed:** Got it. I'll do the same for the other tables.

**Vivek Shankar:** Now let me update all the Looker dashboard links in Notion. We should only update the links for dashboards we actually created.

**Sulaman Ahmed:** ...

**Vivek Shankar:** Let me update the links for Blossom, Metronome, Firework, and the others.

**Vivek Shankar:** I'm updating everything now for all clients where we've delivered Lookers.

**Sulaman Ahmed:** We have Flossom, Engine, Interval, Firework, Discern, Monograph, and Metronome.

**Vivek Shankar:** School AI is done. I need to update Engine, Interval, and check the others.

**Sulaman Ahmed:** There's also Interval in EPD.

**Vivek Shankar:** Let me check that.

**Sulaman Ahmed:** You can just send me the Looker link for it.

**Vivek Shankar:** I've updated: Engine, School AI, Home Base, Flossom, Metronome, Firework, Discern, and Monograph.

**Sulaman Ahmed:** What about Outreach? Is that one we created?

**Vivek Shankar:** Let me check. We may not have created that one.

**Sulaman Ahmed:** About Jessalyn's message, I've shared her the Flossom link. Let me share my screen.

**Vivek Shankar:** It looks clean. Oh, she's asking about the data sources.

**Vivek Shankar:** No, she can just leave it in there.

**Sulaman Ahmed:** I see DataGrid is in this one. I can delete it.

**Vivek Shankar:** We can delete the DataGrid source for her. The colors look like they've been changed to orange and blue — that wasn't us.

**Sulaman Ahmed:** I'll delete both the DataGrid and the colors.

**Vivek Shankar:** Just a reminder — send all the MEs the Looker instructional video. It's very important.

**Sulaman Ahmed:** I've already sent them the URL and video link.

**Vivek Shankar:** Good. Whenever you deliver dashboards, send that video as well. For publishing, check with Isra about splitting the workload.

**Sulaman Ahmed:** Got it. Thank you.

**Vivek Shankar:** All right, thanks everyone. Bye.

**Sulaman Ahmed:** Have a nice day. Bye.
