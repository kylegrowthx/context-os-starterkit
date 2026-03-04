# make outline generation better.

<metadata>
date: 2025-04-02
time: 17:02 UTC
duration: 58 minutes
organizer: jason@growthx.ai
participants: Sydney Go, Jason Gong
fathom_recording_id: 55151982
fathom_url: https://fathom.video/calls/266717232
share_url: https://fathom.video/share/upMaeHTiDqg3irKZpxEqsaJTkii_P5oV
source: fathom
enriched_on: 2026-03-04 17:30 UTC
</metadata>

---

## Summary

Jason and Sydney identified critical flaws in GrowthX's outline generation system—H2 sections are too fluffy, ignore assignment brief structures, and lack logical flow. They decided to implement Looker Studio dashboards to replace manual Airtable updates, allowing clearer visibility into content performance by website path and GrowthX-generated vs. existing pages. Sydney will document specific outline generation issues with examples, and Jason will explore pricing changes to include traffic analysis as a product offering.

---

## Context

This is an internal GrowthX operations meeting between two delivery team members. Sydney Go manages reporting and client analytics infrastructure, while Jason Gong oversees content delivery and pricing strategy. They discussed two interconnected problems: (1) their AI outline generation system is producing suboptimal article structures that violate client assignment briefs, and (2) manual reporting workflows (using Airtable and outdated weekly snapshots) are time-consuming and incomplete. The conversation reveals that GrowthX is managing multiple clients (including RunPod, Strapi, Abnormal Security, and potential enterprise clients like Webflow) with varying content requirements and SLAs. The meeting happens at a point where GrowthX needs to scale content delivery while improving quality—suggesting pressure from growing client demand and hints at team hiring needs.

---

## Relevance

**To GrowthX Delivery:**
- Outline generation algorithm needs urgent fix: H2 headings must respect assignment brief structures, build logically, and avoid filler language. This affects all client projects (RunPod, Strapi, Abnormal Security).
- Manual reporting workflows are breaking down—Andre's weekly updates stopped in mid-March, blocking visibility into performance. Looker Studio implementation will enable real-time client dashboards and reduce labor overhead.
- Content quality issues vary by client: RunPod struggles with keyword vagueness and over-structuring; Abnormal Security content is too flowery with poor scannability. Client-specific outline rules needed.

**To GrowthX Business Development:**
- Expansion opportunity: Jason exploring pricing changes to package "AI traffic analysis" (LLM referral + AI summary traffic) as a standalone product tier. Looker dashboards are the enabling infrastructure.
- Team capacity at risk: Current projects + potential large deals (Webflow) require hiring additional full-time Content Managers. Freelancers not preferred due to quality/consistency concerns.
- Reporting gap indicates delivery maturity issue—Sydney and Jason doing operational troubleshooting that should be handled by delegation or automation. Hiring/tools investment needed.

---

## Overview

- Outline generation is ignoring proposed structures in assignment briefs, leading to suboptimal content organization
- Strapi's content mix (programmatic vs. editorial) needs clarification to better define scope and deliverables
- Looker Studio reports will be implemented to improve data visualization and reporting for clients
- Additional content manager hiring is needed to handle increasing client workload

---

## Key Topics

### Outline Generation Issues

  - Assignment briefs' proposed structures are being ignored in outline generation
  - H2s in generated outlines are often too fluffy and don't build upon each other logically
  - Outlines sometimes include irrelevant sections or poor organization
  - Generated articles occasionally have structural issues (e.g., H3s directly following H2s without text in between)

### Client-Specific Content Workflows

  - Strapi's content mix (programmatic vs editorial) needs clarification
  - RunPod outline generation struggled with vague keywords and over-structuring
  - Abnormal Security's generated content tends to be too flowery and lacks scannable headers

### Reporting and Data Visualization

  - Implementing Looker Studio reports for improved data presentation
  - Reports will include metrics like impressions, clicks, and conversions
  - Data will be sliced by website path and content origin (client's existing vs. GrowthX-produced)

### Team Expansion and Workload Management

  - Need for an additional Content Manager identified
  - Preference for full-time writers over freelancers to maintain quality and consistency
  - Potential large clients (e.g., Webflow) necessitate increased team capacity

---

## Action Items

**Sydney Go (GrowthX)**
- Create Looker Studio report for GrowthX. Include impressions, clicks, conversions. Slice by website path, our content vs. theirs. Top performing pages, GrowthX content, GrowthX performance.
- Ask Emily re Abnormal Security image guidelines. Query general guidelines, generation process, templating (icon+background). Request Figma/Canva style guide/template if exists.
- Complete feedback on outline generation in shared doc. Detail issues w/ fluffiness, non-building H2s. Provide context, examples of good/bad outlines. Aim for 15min task.
- Generate new article, provide feedback on outline generation. Add to shared doc w/ spam email example. Extract generalized conclusions from 3 examples.

**Jason Gong (GrowthX)**
- Update Strapi weekly report. Use Looker to change outdated screenshot (from week 24). Ensure current data reflected.

---

## Transcript
**Jason Gong:** It sounds like we're just kind of ranking, getting clicks for things that say strappy anyway, which I guess we can dig into.

**Sydney Go:** Yeah, the other thing I noticed from all of our weekly meetings is that I don't think, and maybe Andre kept it somewhere else, but I don't think Andre's been updating the week-on-week and month-on-month reports, at least for the past couple of weeks that we've been doing this.

**Sydney Go:** It's all from March 4 to March 15 is the last one that we did, and then we've stopped.

**Sydney Go:** And I also don't know where he's getting this data, because I tried looking at the blog, and it seems that this data is from, I think it's just all GrowthX articles, but I don't know where we keep a list of GrowthX articles.

**Sydney Go:** And Andre was also manually updating the Airtable with all the clicks and impressions going through it one by one, which is a lot of time, which is why I figured Looker Studio would be a little easier to deal with that, since we can set up.

**Sydney Go:** specific pages in Looker Studio.

**Sydney Go:** And then I also, I don't know why there are no new articles in the article that he, in the page that he was updating.

**Sydney Go:** So it feels like there, I think the last article, the ID that I saw was at 700 and they do like sequentially the articles that they've had and they're currently at 900 something.

**Sydney Go:** So there might be about 200 articles missing from here.

**Sydney Go:** I don't know that for sure.

**Sydney Go:** So I'm digging into that as well.

**Sydney Go:** I have messaged Andre because this is, I did try to dig and look through everything.

**Sydney Go:** And it's just, unless he had the doc, which he's not referenced.

**Jason Gong:** What does a Looker look like?

**Jason Gong:** Can you show me just like that we report?

**Jason Gong:** So we don't currently have one for them.

**Sydney Go:** I'm going to build it.

**Sydney Go:** And what's going to happen is a

**Jason Gong:** I'm come up with one.

**Sydney Go:** It's easy enough, probably because I've done it before, so it's probably going to be easy enough.

**Sydney Go:** see.

**Sydney Go:** Smith.ai has something.

**Jason Gong:** Sorry, Smith.ai what?

**Sydney Go:** One of the other customers that we have has something, so let's...

**Jason Gong:** I think it's also a good time for us to think about that.

**Jason Gong:** can actually help.

**Jason Gong:** Because I think the challenging part in this is you have their traffic, and then us trying to surface how the content we're producing is doing, and trying to balance that.

**Jason Gong:** Because at the end of the day, I don't care if we just steal a bunch of clicks from their other pages, which it sounds like he was alluding to.

**Jason Gong:** We care everything's moving.

**Sydney Go:** I think we were a little bit on the nose when we said they were in management mode, but not...

**Sydney Go:** They might be soon to be not so happy if they're not...

**Jason Gong:** I mean, looking at their comparison pages, I'm fully confident to make that better.

**Jason Gong:** think we definitely need a workflow specifically for listicles and comparisons, I think.

**Jason Gong:** Because that's coming up with everybody.

**Sydney Go:** This is what we have for Smith.ai, which is probably what I'm going to try to do as well.

**Sydney Go:** And this is all data, I think, from Google Analytics.

**Sydney Go:** So just clicks, impressions, blah, blah, blah, then category, date, range.

**Jason Gong:** What's in category?

**Jason Gong:** What's in category?

**Jason Gong:** Oh, they don't have any categories.

**Sydney Go:** I think for us, that would be the different tags.

**Sydney Go:** So they've got a lot.

**Jason Gong:** LLM referral traffic.

**Jason Gong:** I think it's worth...

**Jason Gong:** Okay, I mean, feel free to do a V1.

**Jason Gong:** I guess, candidly, what I was thinking about, because right now I'm trying to redo our pricing.

**Jason Gong:** And packaging, and I think there's an opportunity.

**Jason Gong:** And to like almost create this into a product where they have to pay like a decent amount every month to get like their traffic, their traffic from LLMs and their traffic from like AI summaries, like basically just breaking that apart a little bit better for them.

**Jason Gong:** So let's see here.

**Sydney Go:** I can do a V1 of this and then we can figure it out from there.

**Sydney Go:** It's not going to look like this because URL clicks and impressions are important.

**Sydney Go:** There'll be some kind of what's it called?

**Sydney Go:** There'll be some kind of allusion to them in the doc.

**Sydney Go:** But then what we're going to focus on is conversions week over week.

**Sydney Go:** I also noticed actually that their content has actually gone down, I'm not mistaken.

**Sydney Go:** Yeah, overall, that's what it looked like to me too.

**Jason Gong:** But then also if you look at the URLs, I should...

**Jason Gong:** I like their website ranked for some really weird stuff that's like, I don't know what the 's going on.

**Jason Gong:** Like, I don't, yeah, I was really confused.

**Jason Gong:** It seems like people are posting, like, explicit content in their forums and, like, that's skyrocketing.

**Jason Gong:** I don't really understand.

**Sydney Go:** Yeah, I will say, I don't know how it works, but I remember we had, at SEMrush, we were ranking for, like, Pornhub or something to that effect.

**Sydney Go:** Like, was one of our biggest impression getters is because one of our articles referenced it as one of the top pages on the internet because it was an automated report or an automated article.

**Sydney Go:** We didn't notice it and we were like, oh, where's all this traffic coming from?

**Sydney Go:** And we looked into it.

**Sydney Go:** It was that.

**Sydney Go:** It was because it was a generated report.

**Sydney Go:** And then we had to put in stops saying filter out explicit content basically so that we stop ranking for weird keywords.

**Jason Gong:** I want to see if I even have access to Looker.

**Jason Gong:** Do you just access it through the team account?

**Sydney Go:** I also can't do it through my account because you can create one of your own on your account, but we don't have access on our personal accounts to GA4 and Google Search Console.

**Sydney Go:** So if you just report data from those data sources, it has to be made with an account that doesn't have access to those data sources.

**Jason Gong:** Okay, so it's going to be a mess.

**Jason Gong:** Honestly, I haven't used Looker too much before.

**Jason Gong:** What is the value of it?

**Jason Gong:** Is it just like more flexible kind of manipulation of GA stuff, or can you stitch in Search Console?

**Sydney Go:** Yeah, so the way that I used it before is I had a report.

**Sydney Go:** So I used Google Search Console data, and then I had a report that I maintained as an Excel sheet.

**Sydney Go:** And it would present the data in the Excel sheet beside Google Analytics stuff.

**Sydney Go:** And it's just easier because it looks better, if that makes sense.

**Sydney Go:** It's easier to digest instead of having everything in a Google spreadsheet and just...

**Sydney Go:** It's

**Sydney Go:** That being what the customer sees or the client sees, you can share specific data and it will chart everything for you and all that and just makes it easier to tell our customers.

**Jason Gong:** I mean, I guess, like, high level, what I would love to get to is, like, just, like, impressions, clicks, and maybe some version of a conversion.

**Jason Gong:** Like, it doesn't have to be very consistent.

**Jason Gong:** It could just be visited the Get Started page or clicked on the, you know, scheduled demo.

**Jason Gong:** To have that and then be able to slice that a little bit.

**Jason Gong:** I think the things I care about is, like, by kind of, like, website path a little bit.

**Jason Gong:** Okay.

**Jason Gong:** And by what's our content and what's stuff they've had.

**Jason Gong:** To start, I feel like that would be helpful and then we can get kind of more detailed after.

**Jason Gong:** Yeah.

**Sydney Go:** Yeah.

**Sydney Go:** That's, yeah, that's similar to what I built at Animals where it's got the table on top of all of your content.

**Sydney Go:** And then...

**Sydney Go:** Like your top performing pages, then specifically animals content, and then animals performance.

**Sydney Go:** And that's kind of what I was thinking of doing as well.

**Sydney Go:** I will say, have you seen their events?

**Sydney Go:** They've got like 48 events, and 20 of them are clicks.

**Sydney Go:** I don't know which ones are conversions.

**Jason Gong:** Okay, let me look right now.

**Jason Gong:** Okay, so I have, I see their events.

**Jason Gong:** Events.

**Jason Gong:** Let's get there.

**Jason Gong:** Where's that?

**Jason Gong:** Let's see if we have your sales link.

**Jason Gong:** I mean, I don't know how easy it is to work with this in Mixerum and Looker, but I feel like what we probably want is...

**Jason Gong:** I could just aggregate the data.

**Sydney Go:** I think Looker can do that, data aggregation.

**Jason Gong:** Does GA let you define a new event and then apply it retroactively?

**Jason Gong:** I don't think so.

**Jason Gong:** So it's always going forward.

**Sydney Go:** Yeah, as soon as you set a new event, that's when it starts tracking.

**Jason Gong:** So, even if the event is just a wrapper around like a page view that's been happening forever.

**Sydney Go:** If you rename the page view event that you set into a new thing, it'll continue.

**Sydney Go:** But yeah, a new event.

**Jason Gong:** Maybe we need like a custom event.

**Jason Gong:** And I think the custom event is essentially just a bucket of like clicks and pages.

**Jason Gong:** So the, and I think the rough view paths for them, they have like two tiers.

**Jason Gong:** I think the one that's scheduled demo is like the higher intent one.

**Jason Gong:** So I think I would like an event for the page view on their demo form.

**Jason Gong:** And then an event on just clicking the like schedule a demo button.

**Jason Gong:** So that'll be like kind of the sales side of their business.

**Jason Gong:** And then the other one is, let me see, their quick start.

**Jason Gong:** I think the other one is like viewing their quick.

**Jason Gong:** Start page.

**Jason Gong:** And they have install as well.

**Jason Gong:** Like the other one, basically, I'm trying to get to like a, some proxy for like somebody getting the open source version.

**Jason Gong:** I don't know if you need context there, but like open source is like, I mean, actually, this relates to the stuff we're doing for RunPod, where it's like, you know, you're deploying their service on your own infrastructure.

**Jason Gong:** Like generally all the software we use is like cloud hosted on the customer or on the, on the company side.

**Jason Gong:** So they see everything, right?

**Jason Gong:** Like, so like Airtable sees everything, Europe sees everything, but like open source for the most part is like, I have my server on AWS and then I install Strapi on there and I don't have to even talk to Strapi or pay them or do anything with them.

**Jason Gong:** They just give me their software for free.

**Jason Gong:** There might be some features that are locked behind a gate, but like for the Fridays for free.

**Jason Gong:** And it seems like in those cases, Strapi doesn't really have good visibility.

**Jason Gong:** So do you serve?

**Jason Gong:** Just that is just trying to think like what to do.

**Jason Gong:** Because I feel like they have multiple pages in their docs that relate to installing.

**Jason Gong:** So we can either just include all of those.

**Jason Gong:** Yeah, so the second event, so the first event is sales stuff.

**Jason Gong:** The second event I think is just a list of page views and buttons.

**Jason Gong:** And then the page views are simply any page on the docs that relates to installing.

**Jason Gong:** And then the button is, like you see on their homepage, they have this like copy button next to that script.

**Jason Gong:** It'll be that button.

**Jason Gong:** So those are our kind of conversion events for Stratview.

**Sydney Go:** Okay.

**Sydney Go:** Yeah.

**Sydney Go:** Yeah, that makes sense.

**Sydney Go:** Yeah, okay, I'll try to get that data.

**Sydney Go:** I do have to, I still have to send a.

**Sydney Go:** Okay.

**Sydney Go:** Okay.

**Sydney Go:** Bye.

**Sydney Go:** Oh, what's it called?

**Sydney Go:** A list of action items to them after this call.

**Sydney Go:** Oh, before we jump into the outline generation thing, is there anything specifically you want me to ask, Emily, about their, about abnormal securities image guidelines?

**Sydney Go:** Because I was going to ask about general image guidelines, how they generate it, if they do generate it, because it looked very, like, templated, like an icon and then a background.

**Sydney Go:** So if there's a way that they currently generate it, how do they do it?

**Jason Gong:** So is this meant more for, like, what's an acceptable image, or is this more about, like, how do we actually upload it for you?

**Jason Gong:** How do we create it for you so that you can have it?

**Jason Gong:** So, like, what's acceptable?

**Jason Gong:** No, not really.

**Jason Gong:** I mean, just ask them what's acceptable, and then ask for if they have, like, a style guide or a template in Figma or Canva or some design tool to, like, share that with us.

**Jason Gong:** Okay.

**Sydney Go:** Okay, yeah.

**Sydney Go:** Um, yeah.

**Jason Gong:** Yeah.

**Jason Gong:** I don't really have time.

**Jason Gong:** Is that tomorrow?

**Jason Gong:** Or abnormal call?

**Jason Gong:** Yeah, guess I'll have do that this afternoon.

**Jason Gong:** Let just block my calendar.

**Sydney Go:** Yeah, there's a, yeah, this has been a fun week.

**Sydney Go:** Just figuring out everything that I have to get done.

**Sydney Go:** And also still learning the rules while I'm at it.

**Sydney Go:** This has been interesting.

**Jason Gong:** I'm starting next week.

**Jason Gong:** already let people know that we definitely need another one.

**Jason Gong:** I think most pods, the structure is like two CMs.

**Jason Gong:** then it seems like some pods to like just hire contractors to kind of fill in when needed.

**Jason Gong:** But I think for us, I don't know.

**Jason Gong:** I mean, like, maybe that's something you can think of, I guess, not super urgent, but just like, what is the best structure for us?

**Jason Gong:** Because I've heard that, like, Okay, so I guess growthx has been growing really fast.

**Jason Gong:** I think at the early stages.

**Jason Gong:** We hired people without any specific role, and a lot of them got to a point where they either only wanted to do writing or they only wanted to do content generation, but not both.

**Jason Gong:** So some of them would hire an Upworker to edit the writing that they generated or vice versa, which is just kind of weird.

**Jason Gong:** I think for us, I want everyone to do things almost end-to-end as much as possible, at least on the writing part.

**Jason Gong:** I think strategy is different, but I don't want this hand-off happening and having a million liquors.

**Sydney Go:** Yeah, I also don't want, from experience, I want to lean on freelancers as little as possible.

**Sydney Go:** Okay.

**Sydney Go:** Because it's nice having a good freelancer when you work with them, but it's just so hard because there's no commitment on either side because they are freelancers.

**Sydney Go:** A freelancer isn't, they're not going to learn your tone.

**Sydney Go:** I'm going to invest 100% of their energy into your customers because they don't have any stake in that customer.

**Sydney Go:** Whereas an in-house person, we can train, can get them to a point where they can handle things on their own.

**Sydney Go:** So if we do need a writer and they only want to do writing, I'm down to work with someone full-time who only wants to do writing versus hiring a freelancer for just writing, if that makes sense.

**Sydney Go:** That's fair.

**Jason Gong:** Let's see.

**Jason Gong:** Yeah, let's think about what that looks like.

**Jason Gong:** So we have a CM starting.

**Jason Gong:** I really do think we need another one as our next client ramps on.

**Jason Gong:** I think we're having a conversation about who that next client is.

**Jason Gong:** I think Unstructured is one, but I guess yesterday I was talking to Carl and he wants to maybe give us Webflow, which would be a gigantic one, which we really do need help for.

**Jason Gong:** If we have two giant clients, then we do need.

**Sydney Go:** Because Abnormal is also quite big.

**Jason Gong:** Yeah, that was really big too.

**Sydney Go:** Though I do think for the high-touch clients or the clients who are...

**Sydney Go:** Used to.

**Sydney Go:** Actually, I think we worked with Webflow at Animals now that I'm thinking about it.

**Jason Gong:** I feel like some of these bigger companies work with everyone, like our competitors included.

**Jason Gong:** So I know that works.

**Sydney Go:** Yeah, I knew someone who worked at it because she was at, yeah, we did.

**Sydney Go:** We did work with Webflow because she was at Animals before and I worked very closely with her.

**Sydney Go:** And then after Animals, she went to Webflow.

**Jason Gong:** She's left.

**Jason Gong:** Did you work with Webflow at all?

**Sydney Go:** So a couple of, I think I only generated, I only wrote three articles for them, if I'm not mistaken, that I remember.

**Sydney Go:** But I can't even remember them off the top of my head because it's been so long.

**Sydney Go:** How much traffic Webflow has?

**Jason Gong:** I guess I'm trying to decide whether we want Webflow because it seems like we have a choice whether we want unstructured or Webflow.

**Jason Gong:** So I remember Webflow.

**Sydney Go:** I remember Webflow's team being very easy to work with because.

**Sydney Go:** I

**Sydney Go:** We, they were within my pod, pod.

**Sydney Go:** We were, we were both.

**Sydney Go:** So I was on Team Narwhal and they were a customer of Team Narwhal.

**Sydney Go:** So we did have some insight into them and they weren't one of the customers that we were scared of.

**Sydney Go:** We had a couple of those that nobody wanted to deal with and they weren't one of those.

**Sydney Go:** So I do remember them being pretty good to deal with.

**Sydney Go:** But I don't know if the team's changed because it's been three years.

**Sydney Go:** Got it.

**Jason Gong:** Just look at Webflow real quick.

**Jason Gong:** What's Webflow's website?

**Jason Gong:** it .io?

**Jason Gong:** No, it's .com.

**Jason Gong:** Oh, I think they just, they just don't use www.

**Jason Gong:** They have so much traffic.

**Jason Gong:** Okay, let's see.

**Jason Gong:** Where is that traffic?

**Jason Gong:** Okay.

**Jason Gong:** This is thing.

**Jason Gong:** Okay.

**Jason Gong:** Thank you.

**Jason Gong:** Okay.

**Jason Gong:** everything.

**Jason Gong:** Thank you.

**Jason Gong:** Thank Thank Thank you.

**Jason Gong:** Good with Thank Thank You

**Jason Gong:** Yeah, I guess I'm trying to think, like, what our kind of pod is uniquely good for.

**Jason Gong:** I think, like, with the smaller companies, it's kind of, they're a little bit more scrappy and they move quickly on, like, new strategies.

**Jason Gong:** I think with the big companies, a lot of the work is kind of just navigating their processes to try to, like, do something new if that's what we want us to do.

**Sydney Go:** And I remember with Webflow, we were, we leaned heavily on, we created some new content, but it was a lot of refreshes because they had so much content that was already underperforming.

**Sydney Go:** So when we were working with them, it was a lot of refreshes.

**Jason Gong:** Yeah, I mean, they've got these, like, templates.

**Jason Gong:** guess their blog's the main place.

**Jason Gong:** They've made in Webflow, they have templates.

**Jason Gong:** Wow.

**Jason Gong:** Okay.

**Jason Gong:** Yeah, feel like it would be very, like, programmatic.

**Sydney Go:** Yeah, I feel like this one, I don't know.

**Jason Gong:** I think it's a little, at least on the strategy side, like something I'm less familiar with.

**Jason Gong:** Just the sheer size of it.

**Jason Gong:** So I'll let them decide.

**Jason Gong:** I think just getting the sheer size, I feel like the strategy part is kind of like something I'm not as familiar with.

**Jason Gong:** But they probably, like, scoped it, too, where it's not like, hey, make our whole SEO better.

**Jason Gong:** It's like, make our glossary better.

**Sydney Go:** On the strategy side, I can help with that, because that was what I was doing at Animals.

**Sydney Go:** It was working with the bigger companies, making sure that we're not doing any cannibalization.

**Sydney Go:** you know, kind of what you mentioned before about what most agencies do.

**Jason Gong:** We should definitely figure out how to automate.

**Jason Gong:** Yeah, good, actually.

**Jason Gong:** actually.

**Jason Gong:** An analysis or like a check somewhere, because if you don't really do that right now.

**Jason Gong:** Okay, cool.

**Jason Gong:** So let's try to spend our time on the outline generation.

**Jason Gong:** Maybe to start, do you have an example of just an I was actually going to show you.

**Sydney Go:** So this one is the one that we generated for Aerox.

**Sydney Go:** For Aerox, God, brain.

**Sydney Go:** This is the one that I generated for Strappy.

**Sydney Go:** That's the name.

**Sydney Go:** And I've generated most of them because they actually did well.

**Sydney Go:** This, ha, this doesn't even have an outline step.

**Sydney Go:** Oh, because this is on the old, this one's on the old system.

**Sydney Go:** I missed that.

**Sydney Go:** So it just goes assignment brief straight to output.

**Sydney Go:** Yeah, but I honestly found that this one understood the assignment better.

**Sydney Go:** Like, I'm sorry.

**Sydney Go:** Still not.

**Sydney Go:** It's still not perfect.

**Sydney Go:** Like for a top 10 chart, it doesn't make a lot of sense to have this down here if you do have and how to choose and that could probably come higher.

**Sydney Go:** Otherwise, just remove it.

**Sydney Go:** you know, things like that.

**Sydney Go:** But the what's it called?

**Sydney Go:** The article it generated wasn't terrible.

**Sydney Go:** That's when I started editing first and this wasn't bad.

**Sydney Go:** This actually produced pretty good results.

**Sydney Go:** then let me just double check.

**Jason Gong:** You're saying this is like our old workflow?

**Jason Gong:** Yeah, that was our old workflow.

**Sydney Go:** Yeah, I think.

**Sydney Go:** I know that Daniel Daniel was supposed to port them over.

**Sydney Go:** But I still I don't see.

**Sydney Go:** I guess he just the assignment brief change and then research done changed as well, because I think those are the two that he was working on.

**Sydney Go:** Oh, wait, no.

**Sydney Go:** Here's the outline.

**Sydney Go:** Never mind.

**Sydney Go:** What am I doing?

**Sydney Go:** you.

**Sydney Go:** Yeah, here's the outline.

**Sydney Go:** I just didn't have it as a, yeah.

**Sydney Go:** Yeah, this is not bad.

**Sydney Go:** This is the one I generated.

**Sydney Go:** Like this, I don't, I may have removed it.

**Sydney Go:** Wait, nope, that's not the one.

**Sydney Go:** That's the one that, what's his name, generated.

**Sydney Go:** Where's mine?

**Sydney Go:** So, sorry, Aerox has been doing this thing where if I don't refresh the page, it doesn't show me the last few columns where my stuff is.

**Sydney Go:** Just try that again.

**Sydney Go:** Okay, there, it should be here.

**Sydney Go:** Okay, so these are mine.

**Sydney Go:** Um, yeah, so, oh, okay, well, there's an error there anyways.

**Sydney Go:** Um, so here, so, it's not bad.

**Sydney Go:** But here, unlocking chat to peaceful potential, not bad.

**Sydney Go:** Understanding mechanics.

**Sydney Go:** This,

**Sydney Go:** Be about code generation architecture prompts.

**Sydney Go:** And then we get into the advanced prompts, which I think makes sense.

**Sydney Go:** So this could work.

**Sydney Go:** And then code optimization and debugging prompts should also work.

**Sydney Go:** And it did a good job in making this an article that's actually structured well.

**Sydney Go:** And then the one that I was working on, where is it?

**Sydney Go:** It wasn't.

**Sydney Go:** I did work on this because what's it called?

**Sydney Go:** I didn't see that.

**Sydney Go:** It was already uploaded because it wasn't in our table.

**Sydney Go:** But yeah, so I remember working on this one, the top 10, and it was also not bad.

**Sydney Go:** Like the article here is mostly what we have in there in Strapi CMS, and they didn't complain about it.

**Sydney Go:** On my end, I think this is too long of an intro, but that's not a structural problem.

**Sydney Go:** But yeah, the key criteria is also...

**Sydney Go:** Like it's, it's all there basically.

**Sydney Go:** But when I started to do this for, let just open for you.

**Jason Gong:** Seriously, I guess in general, it seems good for Strappy right now.

**Sydney Go:** Yeah, I think so.

**Sydney Go:** But if I, from a me point of view, I, I still want to change it, if it makes sense.

**Sydney Go:** It's not quite up to where I would want it to be.

**Sydney Go:** This is the one.

**Sydney Go:** So for RunPod, I did the bare metal thing in the instant clusters.

**Sydney Go:** I'm not sure if the reason that our outline came out as it was, was because, what do I reset to original value?

**Sydney Go:** Yeah.

**Sydney Go:** So.

**Sydney Go:** So.

**Sydney Go:** That wasn't the original.

**Sydney Go:** Anyway, yeah, so maybe it's because the keywords I'm giving it is too vague, but what came out was understanding bare metal and traditional VMs and performance comparison, cost considerations, and it doesn't make sense for the title that it was going for, if it makes sense.

**Sydney Go:** And just from scanning this, I can get some idea of what this is for, but the whole picture is a little bit jagged, and it's way too many H2s.

**Jason Gong:** So how would you change the one particular?

**Jason Gong:** Like, are you just saying it doesn't really answer the question?

**Jason Gong:** It doesn't answer the question.

**Sydney Go:** It's too over-structured.

**Sydney Go:** I don't know.

**Sydney Go:** It's not what appeared on the SERPs either, because the SERPs...

**Sydney Go:** I did have the search for mostly comparison pages versus pages, and they were very straightforward with the whole table and everything.

**Sydney Go:** So I don't know where the over-structuring comes from.

**Sydney Go:** I'm going to rerun it just so that we can see what it is.

**Sydney Go:** But I don't know where it breaks, if that makes sense, because I checked on this one.

**Sydney Go:** And the assignment brief is not going be one.

**Sydney Go:** I checked on the assignment brief, and most everything makes some sense.

**Sydney Go:** Maybe it's because of the reference URL.

**Sydney Go:** The other keyword opportunities make sense.

**Sydney Go:** Do you know where this data is coming from, by the way?

**Jason Gong:** I could check.

**Jason Gong:** So this is, what's this, the assessment or assignment brief?

**Jason Gong:** Yes.

**Jason Gong:** I get to assignment.

**Jason Gong:** Let's see, could you share this link with me?

**Jason Gong:** For the most part, I think the only APIs we use is either SEMrush, SIRP API, and yeah, think those are the main things we use.

**Jason Gong:** Okay, so I think the proposed structure here was actually one.

**Jason Gong:** Okay, SEMrush, SIRP API, and then data for SEO.

**Jason Gong:** Those are like the three services we use.

**Sydney Go:** Yeah, I was just curious.

**Sydney Go:** So proposed content structure here wasn't bad.

**Sydney Go:** So what's the difference?

**Sydney Go:** And then bare metal for LLM, traditional VMs for LLM, and then run pods tape.

**Sydney Go:** I think I may have said it.

**Sydney Go:** That.

**Sydney Go:** But yeah, it was very simple.

**Sydney Go:** And then when I got to the outline part, suddenly it was very it was a lot.

**Sydney Go:** So there's the first two, the infrastructure choice for LLM training and then understanding bareman.

**Sydney Go:** And it doesn't build correctly.

**Sydney Go:** And then there's performance comparison, cost structure analysis.

**Sydney Go:** And we don't really get into what what are these things like?

**Sydney Go:** Why?

**Sydney Go:** Why are they here?

**Sydney Go:** And then suddenly we have a case study.

**Sydney Go:** And then we're back to run pods infrastructure.

**Sydney Go:** And then we're back to criteria, which probably should have been at the beginning at all.

**Sydney Go:** And then for the conclusion, we're mentioning performance, cost and flexibility.

**Sydney Go:** But at this point, it's been so far gone that the reader is probably like, where did this come from?

**Sydney Go:** And then security and isolation is also not there at home.

**Sydney Go:** So it's just it's messy.

**Sydney Go:** It doesn't quite build.

**Sydney Go:** It doesn't answer each other, if that makes sense.

**Sydney Go:** The H2s don't build.

**Sydney Go:** And there's way too many.

**Jason Gong:** That's kind of reasonable feedback.

**Jason Gong:** mean, let me just see how that's done.

**Jason Gong:** So you're saying the assignment brief is pretty good.

**Jason Gong:** Could you look at the assignment brief again?

**Jason Gong:** I'm trying to think for a comparison page, what should the assignment brief look like?

**Sydney Go:** I think I may have fed it this, to be completely honest.

**Sydney Go:** I think I may have fed it because this is the exact structure in my template.

**Sydney Go:** Let's see this one.

**Sydney Go:** I fed it as well.

**Sydney Go:** Yeah, I fed it this.

**Sydney Go:** I actually...

**Jason Gong:** Your template meaning what, like your chat GPT conversation?

**Jason Gong:** Um, the template that I proposed.

**Sydney Go:** It's supposed Yeah.

**Sydney Go:** I'm supposed to

**Sydney Go:** Yeah, I just went into the code and then I changed it so that the input for the next step would be different.

**Jason Gong:** I don't know what you mean, because your template is just like kind of things in brackets, right?

**Jason Gong:** Like headings essentially, or like what the heading should be.

**Jason Gong:** Yeah, and then I changed it manually and then added all of it manually as well.

**Jason Gong:** So you copied, like what does that mean just like specifically?

**Jason Gong:** Like did you generate this first, then you copied it on ChatGPT and you gave it your template and it pieced it together?

**Jason Gong:** how did you actually do that?

**Sydney Go:** So I generated this.

**Sydney Go:** I looked at everything, looked okay.

**Sydney Go:** When I got to the proposed content structure, it was way too much.

**Sydney Go:** So when you say you generated this, you mean you generated this in AirOps?

**Jason Gong:** This is the generated in AirOps.

**Sydney Go:** Um...

**Sydney Go:** I changed this.

**Sydney Go:** I erased it and then replaced it with the template that we preferred.

**Sydney Go:** Got it.

**Jason Gong:** Yeah, I mean, OK, so I guess for context, this is, you know, programmatic.

**Jason Gong:** So, like, we kind of have a structure that we're with, but nowhere in this can you kind of, like, feed that, right?

**Jason Gong:** I think, actually, it still used this.

**Sydney Go:** Like, it took out, like, future trends in AI infrastructure.

**Sydney Go:** We don't need that.

**Sydney Go:** Making the right choice for AI workloads.

**Sydney Go:** Don't need that.

**Sydney Go:** Decision framework.

**Sydney Go:** Don't need that.

**Sydney Go:** I think it still used some of this, like, security and compliance for AI data, even if I had already changed it.

**Sydney Go:** And it was supposed to be using the new, like, structure that I had put in.

**Jason Gong:** if you change it, like, where do you feed that new structure in?

**Jason Gong:** So you have the assignment brief.

**Sydney Go:** Yeah, it goes into the assignment brief.

**Sydney Go:** And I have the research, not the research.

**Sydney Go:** Well, have the outline, this one.

**Sydney Go:** Mapped to this column, not this one.

**Jason Gong:** Oh, so you added a new column called Assignment Brief?

**Jason Gong:** Isn't that the Assignment Brief?

**Jason Gong:** Yeah, so...

**Jason Gong:** guess I'm just confused.

**Jason Gong:** Okay, so the Assignment Brief fits out in Assignment Brief, and you're saying that Assignment Brief wasn't very good, so you kind of changed it.

**Jason Gong:** But where did you change it?

**Jason Gong:** Just at the bottom.

**Sydney Go:** Structure.

**Sydney Go:** I changed the proposed structure.

**Sydney Go:** So you can change it here in the code.

**Jason Gong:** Okay, so you basically just, like, modified this directly, and then saved it.

**Jason Gong:** And then...

**Jason Gong:** And then Rath, outline generation.

**Sydney Go:** Yeah, and then the research and the outline generation.

**Sydney Go:** I watched Daniel's walkthrough, and that's what he said, to do, like, change parts that you needed to change.

**Sydney Go:** If you want to change some of the outline, can also do that so that before the article draft is generated, it'll pull from the outline that you set.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** I mean, I guess the takeaway for me is, like, in general, for programmatic pages, we need some sort of structure to adhere to, but, like, this workflow doesn't really kind of do that.

**Sydney Go:** Yeah, I also find that my proposed structure is more often than not ignored, so I have to redo it in the actual outline.

**Jason Gong:** And when you say your proposed structure, you are kind of, like, inputting that by modifying the assessment, or sorry, the assignment brief.

**Jason Gong:** But, like, in this case, like, this assignment brief, is this the one you modified, or did it, like, overwrite it or something?

**Jason Gong:** I redid it.

**Sydney Go:** This is not the one I wrote, so I redid it.

**Sydney Go:** I redid the thing so that it would go to this one.

**Sydney Go:** I'm not sure if I can...

**Sydney Go:** get my version back, actually.

**Sydney Go:** Yeah, so why did it overwrite that version?

**Jason Gong:** Like, shouldn't that version be in here?

**Jason Gong:** I clicked...

**Sydney Go:** So we could see what the one looked like.

**Jason Gong:** Oh, okay.

**Jason Gong:** Do you have your version anywhere?

**Jason Gong:** I guess that's gone.

**Jason Gong:** I think it's gone.

**Sydney Go:** Sorry.

**Sydney Go:** Unless I can get it somewhere here.

**Jason Gong:** mean, you, if you, can you share this?

**Jason Gong:** Or did you share this link with me?

**Jason Gong:** I should have.

**Jason Gong:** Oh, you did?

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Let me just take a look at it.

**Sydney Go:** Oh, yeah, I did.

**Jason Gong:** Okay.

**Jason Gong:** me just click.

**Jason Gong:** Okay.

**Jason Gong:** So this one, bare metal.

**Jason Gong:** Yeah.

**Jason Gong:** Let's see.

**Jason Gong:** So the assignment brief, is the assignment brief fed into research gen and title gen and all this stuff?

**Jason Gong:** Right.

**Jason Gong:** The assignment briefs mentioned there.

**Jason Gong:** Yeah.

**Jason Gong:** The assignment brief.

**Jason Gong:** Thank you.

**Jason Gong:** Bye.

**Jason Gong:** I've also mentioned the outline.

**Sydney Go:** Research guidance is optional to map it to the assignment brief, but I did.

**Jason Gong:** Right.

**Jason Gong:** Okay.

**Jason Gong:** So let's see.

**Jason Gong:** Oh, God.

**Jason Gong:** Yeah, this is probably run a million times across all our clients.

**Jason Gong:** Um, grid table.

**Sydney Go:** Let's look at keyword.

**Jason Gong:** So we're looking at bare metal.

**Jason Gong:** Uh, today at, oh, this is just now when you've ran it again.

**Sydney Go:** Um, you can check out instant clusters.

**Jason Gong:** No, I want to look at that one specifically because you said you changed it.

**Jason Gong:** So I just want to see.

**Jason Gong:** Okay.

**Jason Gong:** So here are the two times it's run.

**Jason Gong:** Presumably, this is like the.

**Jason Gong:** That was the first time, yeah.

**Jason Gong:** So this should have a different assignment brief, right?

**Sydney Go:** Ideally, it should be the same because I just ran it again because I didn't change it.

**Jason Gong:** But didn't you say you changed the assignment brief and then you ran it previously?

**Jason Gong:** I changed the actual text.

**Jason Gong:** Right, but when you change the text of the assignment brief, that output gets fed into this step, which is the outline generation.

**Jason Gong:** Yeah, then it should be different.

**Jason Gong:** You're right.

**Jason Gong:** So I just want to look at it.

**Jason Gong:** Let's see.

**Jason Gong:** Is this the assignment brief?

**Jason Gong:** RunPod is a part...

**Jason Gong:** No, that's their...

**Jason Gong:** It's the AI context.

**Jason Gong:** ...and stuff.

**Jason Gong:** That's the output.

**Jason Gong:** Or research.

**Jason Gong:** No.

**Jason Gong:** Actually, it's there.

**Sydney Go:** It is sent.

**Jason Gong:** Does this look like your assignment brief?

**Sydney Go:** Yes.

**Sydney Go:** So under proposed contents, after keyword difficulty 26.

**Sydney Go:** Proposed content, the first H2 is what's the difference between bare metal and traditional bands.

**Sydney Go:** And then I put the bullet points underneath.

**Sydney Go:** So it is there, like at the very end.

**Sydney Go:** Like one, two, three, four, five lines at the bottom.

**Sydney Go:** Yeah, that's the one I put in.

**Sydney Go:** Got it.

**Jason Gong:** Okay.

**Jason Gong:** So...

**Sydney Go:** That was largely ignored.

**Jason Gong:** Interesting.

**Jason Gong:** Okay, so you're saying this?

**Jason Gong:** Okay, this is your input.

**Jason Gong:** That makes sense.

**Jason Gong:** But you're saying...

**Jason Gong:** Yeah.

**Jason Gong:** Output, which is this, ignored the input.

**Jason Gong:** Is that what you're saying?

**Jason Gong:** Yeah.

**Jason Gong:** Okay, so let's take a look at that.

**Jason Gong:** So we have...

**Jason Gong:** Pros, structure.

**Jason Gong:** What's the difference between bare metal and traditional VMs?

**Jason Gong:** Understanding bare metal.

**Jason Gong:** Okay, so it talks about performance right away.

**Jason Gong:** Cost, flexibility, and scalability.

**Jason Gong:** Right, yeah, I basically completely ignored.

**Jason Gong:** Interesting.

**Sydney Go:** I changed the first, because I remember...

**Sydney Go:** I may have run it...

**Sydney Go:** No, I didn't run it before changing it.

**Jason Gong:** Context, assignment, brief, remodel.

**Jason Gong:** Um...

**Jason Gong:** Yeah, interesting, okay.

**Jason Gong:** So we have this API.

**Jason Gong:** Okay, cool.

**Jason Gong:** So this is great.

**Jason Gong:** Let's see.

**Jason Gong:** I just want to include this somewhere so they get access to this.

**Jason Gong:** How do I share?

**Jason Gong:** Oh, I guess this is the URL.

**Jason Gong:** Okay, so let's write this down somewhere.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** you.

**Jason Gong:** you.

**Jason Gong:** Thank you.

**Jason Gong:** I mean, because I think completely ignoring is interesting because presumably people are editing and if that's just happening somehow, it doesn't make any sense.

**Jason Gong:** Like I said, I'm learning how the generation seems to be ignoring the assignment briefs.

**Jason Gong:** Or at least the proposed structure in the assignment briefs.

**Jason Gong:** Is proposed structure something that the assignment brief usually has, that section?

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** So, this is a problematic page.

**Jason Gong:** important.

**Jason Gong:** It's important to keep it consistent.

**Jason Gong:** It's just a white, which you can't really feed.

**Jason Gong:** Do the assignment brief, um, in this case, Sydney updated the assignment briefs.

**Jason Gong:** Ignored by, um, it's just interesting.

**Sydney Go:** Um, the other thing I wanted to bring up with you was I don't know how programmatic Strapi's content is.

**Sydney Go:** Oh, are they also on programmatic?

**Jason Gong:** I don't know.

**Sydney Go:** That part to me was very unclear if they were on programmatic or not.

**Jason Gong:** I mean, comparison and integration pages are programmatic, right?

**Jason Gong:** The editorial is not, definitely.

**Jason Gong:** I also think they're on 9K a month, so I don't know how that works exactly.

**Sydney Go:** Yeah.

**Sydney Go:** So this, I will have to ask.

**Sydney Go:** I don't know about the backlog, because I don't know about that.

**Sydney Go:** But so the ones that I just generated, and I'm not sharing my screen because I don't do that.

**Sydney Go:** What's it called?

**Sydney Go:** This one.

**Sydney Go:** So I don't know that these topics are programmatic.

**Sydney Go:** These are the ones that I showed Victor on our call earlier.

**Sydney Go:** And then we have a complete guide, which is definitely not programmatic.

**Sydney Go:** Well, think for them, these are supposed to be editorial, right?

**Jason Gong:** Did they call them programmatic?

**Jason Gong:** Do they have an editorial workstream?

**Jason Gong:** I mean, it seems like from what Jimmy said in that thread, it seems like we just kind of gave them what they wanted to some degree in this workstream.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** So that's why they have a mix of programmatic and editorial.

**Jason Gong:** But as a logo, they're really good.

**Jason Gong:** So I think our goal is just to keep them happy, which I think is good for now.

**Jason Gong:** I mean, this is something I'm thinking about right now with Marcel.

**Jason Gong:** Like, how do we draw lines around what our scope is?

**Jason Gong:** Because right now, we can't really upsell because if they don't know what our scope is, it kind of asks us where they want and we do it, you know?

**Jason Gong:** Yeah, okay.

**Sydney Go:** And then this is the other issue that's running in with their account is that for, I think, from week 24, it's been the same screenshot.

**Sydney Go:** Okay.

**Jason Gong:** I mean, for next week, let's just do, like, an actual one.

**Jason Gong:** Let's do it from...

**Jason Gong:** I'm going to look at Looker and change that.

**Sydney Go:** But, yeah, okay.

**Sydney Go:** That was the only thing I wanted to clarify for Shrapi.

**Sydney Go:** I just popped into my head.

**Sydney Go:** Cool.

**Jason Gong:** Let's just close the loop on this.

**Jason Gong:** have a few more minutes.

**Jason Gong:** Okay.

**Jason Gong:** So this is...

**Jason Gong:** Definitely an interesting problem.

**Sydney Go:** I'm going to get my charger real quickly, sorry.

**Jason Gong:** But I can hold you.

**Jason Gong:** I guess what I was looking for was more like a generalized feedback on the outlining or the assignment brief in general.

**Jason Gong:** Have you noticed other issues that seem to kind of appear across all the outlines that you're creating?

**Jason Gong:** It's not maybe as just a matter of taste.

**Jason Gong:** It's more kind of like, this just kind of looks wrong.

**Sydney Go:** Okay, so with abnormal, the problem on their end is it's too flowery.

**Sydney Go:** The headers or the H2s are not scannable.

**Sydney Go:** And like this one, they don't answer each other.

**Sydney Go:** There's no one clear picture.

**Jason Gong:** Okay, let's spread that.

**Sydney Go:** can get even more context on that tonight as I start generating more of their articles.

**Jason Gong:** So H2s are too fluffy and do not film upon each other.

**Jason Gong:** I mean, if you have a specific example, would help a lot.

**Jason Gong:** I mean, we could just take a look.

**Sydney Go:** I don't know why my bookmark pages don't work.

**Sydney Go:** Okay, here.

**Sydney Go:** Here I can share my screen.

**Sydney Go:** Normal security.

**Sydney Go:** Okay, so here.

**Sydney Go:** Here with spam email, so you got the AI context, time it brief, everything's fine, and then when you get to the outline, did I also change this?

**Sydney Go:** Yeah, changed this.

**Sydney Go:** Here, this one's the one I didn't touch.

**Sydney Go:** Okay, so evolution cyber security, how AI is transforming cyber security defense.

**Sydney Go:** Here, things like this, the double-edged sword of AI-powered cyber threats.

**Sydney Go:** And I don't think it should be in here.

**Jason Gong:** Do you have one where you ended up making a better one?

**Jason Gong:** Yeah, I think all of them.

**Sydney Go:** I see that this one has the, what's it called, the reset to original values.

**Sydney Go:** So

**Sydney Go:** So I probably changed this one.

**Sydney Go:** And then I remember after generating the article draft, I think my final article was even more different.

**Jason Gong:** I mean, let's just talk about this.

**Jason Gong:** Okay, so we have...

**Jason Gong:** Oh, we're going through the outline, sorry.

**Jason Gong:** How do I find this thing?

**Jason Gong:** Normal security, article generation.

**Jason Gong:** And so when I look at the ones you've written, and we have...

**Jason Gong:** Okay, so you're saying the spam email one is like a good example?

**Sydney Go:** I think I remember the spam email one being...

**Sydney Go:** Actually, both the first two ones were pretty...

**Jason Gong:** Spam email...

**Jason Gong:** Let me just take a look at this.

**Jason Gong:** Okay, so we have this.

**Jason Gong:** this.

**Jason Gong:** Okay, You

**Jason Gong:** And then we have, which one is that?

**Jason Gong:** That's this one?

**Jason Gong:** Spam email?

**Sydney Go:** The first one.

**Jason Gong:** And you're saying for this one, well, I guess the proposed structure will be here already.

**Jason Gong:** I see.

**Jason Gong:** Okay.

**Jason Gong:** So I don't want to press that yet.

**Sydney Go:** I'm not sure that I did change that one.

**Sydney Go:** Cause I did, I wanted to see how it would do.

**Jason Gong:** Okay.

**Jason Gong:** And then just open up the window.

**Jason Gong:** Um, so.

**Jason Gong:** What are spam emails, the business impact, security implications, I mean honestly, I feel like just in general, this section is just being ignored like everywhere.

**Jason Gong:** I may have changed the outline.

**Sydney Go:** Sorry, this was last week when I did this.

**Sydney Go:** Oh, you changed, okay, so you managed to change the outline.

**Sydney Go:** But like, you're one of the eight, I don't know, but from spam to serious compromise doesn't sound like something that I did, so.

**Jason Gong:** And what is this one called, spam?

**Jason Gong:** OK, sure.

**Jason Gong:** Thank you.

**Sydney Go:** OK.

**Sydney Go:** Thank you.

**Sydney Go:** Yeah.

**Jason Gong:** Do you remember when you did this?

**Jason Gong:** What day?

**Sydney Go:** Last Wednesday or Thursday, it would have been.

**Sydney Go:** That was a while ago.

**Sydney Go:** There it is.

**Jason Gong:** And, uh, you have all links for spam emails.

**Jason Gong:** Yeah, I did change it.

**Jason Gong:** OK, so I mean, I think for me, like the problem is happening in the assignment brief and not the outline generation, because the outline generation for this part, I mean, if it's working follows the assignment brief, like, pretty closely.

**Jason Gong:** Absolutely.

**Jason Gong:** Yeah.

**Jason Gong:** So let's see, okay, so let's grab, what do I want the input?

**Jason Gong:** And here's what I'm doing on the side, grab the, let's just try to give like comparison, like, you know, like here's what's good, here's what's bad.

**Jason Gong:** That looks accurate, right?

**Jason Gong:** I'm just going to see what it is.

**Jason Gong:** So, and then here, fluffy and do not build on each other.

**Jason Gong:** Sample with spam email.

**Jason Gong:** And I'll invite you, you might have accessed already.

**Jason Gong:** I just want you to like add your comments later, but okay, so we have, it says, Simon Grief, that generated, give the example, so we have Simon Grief, you.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** you.

**Jason Gong:** Okay, so the one that generated, which we didn't like, was this one.

**Sydney Go:** I think that might have been the outline, though.

**Sydney Go:** Huh?

**Sydney Go:** I was serious.

**Sydney Go:** No, I think that might have been the outline.

**Sydney Go:** That's not in the assignment brief.

**Jason Gong:** Wait, isn't it?

**Jason Gong:** This is, I think it's the assignment brief.

**Jason Gong:** That's it?

**Jason Gong:** Okay, sorry.

**Jason Gong:** Like, I grabbed it from this, the assignment brief in this execution step.

**Jason Gong:** So, updated H2s.

**Jason Gong:** Thank you.

**Jason Gong:** you.

**Jason Gong:** And if you can, just kind of like, maybe I'll leave this to you, like, is this an H2, or is this, like, the whole, is, like, an H1?

**Jason Gong:** I don't really know.

**Sydney Go:** I don't think it is an H1.

**Sydney Go:** I think it's just telling you what the introduction should be.

**Jason Gong:** I hate how this doesn't, like, render Markdown properly, Howard.

**Jason Gong:** You could copy the code, maybe.

**Sydney Go:** Maybe that would work.

**Sydney Go:** It's the state markdown, but it doesn't actually...

**Jason Gong:** Yeah, but I guess to do that, I'll have to find this in the other history, which is too lazy.

**Jason Gong:** I'll do that.

**Jason Gong:** Okay, we'll just let that run.

**Jason Gong:** Okay, yeah, same with me.

**Jason Gong:** So I think this is already good.

**Jason Gong:** I mean, maybe I'll leave it to you.

**Jason Gong:** I would talk to maybe just 15 minutes to just give your feedback.

**Jason Gong:** But as you're giving feedback, I think it's very important to try to generalize it.

**Jason Gong:** I think what we said here, too fluffy.

**Jason Gong:** What does that mean exactly?

**Jason Gong:** It does not build on each other.

**Jason Gong:** think it's good, but just giving some more context.

**Jason Gong:** You need the article to flow, the H2s to the flow into each other.

**Jason Gong:** But right now, they're all separate sections.

**Jason Gong:** If you took them out and just reshuffled, it wouldn't make a difference.

**Jason Gong:** Because, like, there's no kind of logical order to it or something.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Sydney Go:** And I'll generate another article, too, and I'll give you feedback on that.

**Sydney Go:** So you can have at least three in there that'll do the same thing.

**Sydney Go:** So that we can, so I can extract some generalized conclusions from that.

**Jason Gong:** Got it.

**Jason Gong:** Okay.

**Jason Gong:** think it doesn't really, didn't actually take this for some reason building.

**Jason Gong:** Oh, that's mine.

**Sydney Go:** The one on top is the one in there, I think.

**Sydney Go:** Oh.

**Jason Gong:** That's fine.

**Jason Gong:** Yeah, How does this work?

**Jason Gong:** Does it give you, like, an introduction paragraph, like, with an H2 right below the H1, or does it just ignore the list?

**Sydney Go:** It does give me an H2 right at the top, and I just remove it.

**Sydney Go:** Okay.

**Sydney Go:** That is also a problem.

**Jason Gong:** So where's, um, uh, H2.

**Jason Gong:** does give you an Well...

**Jason Gong:** Well...

**Sydney Go:** Yeah, and I've also had the articles generated, where the H2 has an H3 right after it, and there's no text in between the H2 and H3.

**Sydney Go:** Okay, cool.

**Jason Gong:** I'll let you kind of fill this out, but I think, yeah, I want to ship this over.

**Jason Gong:** Apparently Kirkland's like looking at this today, so.

**Jason Gong:** All right, I'll try to get it from today.

**Jason Gong:** Okay, all right, thank you.

**Jason Gong:** I'll talk to you later.

**Jason Gong:** Awesome, see you, bye.

**Sydney Go:** Thank you.
