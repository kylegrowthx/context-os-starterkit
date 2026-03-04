# Flosum <> GrowthX Weekly Sync

<metadata>
date: 2025-05-21
time: 15:30 UTC
duration: 28 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević (GrowthX), Jakub Rudnik (GrowthX), Beau Beamon (Flosum), Brian Evans (Flosum), Drew Noel (Flosum), Matt Lyman (Flosum), Saakshi Jain (Flosum)
fathom_recording_id: 63914996
fathom_url: https://fathom.video/calls/305535727
share_url: https://fathom.video/share/iCjVVTjnQtoV357jvPDcjzvRGhT8aXiV
source: fathom
enriched_on: 2026-03-04 08:45 UTC
</metadata>

---

## Summary

Flosum and GrowthX reviewed performance reporting infrastructure, content production status, and technical setup for their ongoing content partnership. Aida demonstrated a custom Looker Studio dashboard tracking blog performance via Google Search Console and GA4 data, with plans to filter by GrowthX-created content and track LLM referral traffic. The team aligned on reporting cadence (monthly preferred over weekly), discussed leveraging Webflow's custom CTA and banner capabilities, and confirmed Beau will adjust editor-level Webflow access for the GrowthX team. Jakub is advancing the no-index page cleanup project (expected multi-week timeline) while Beau builds a tool to identify high-intent visitors; calibration article feedback is due from Matt's team by week-end, and the group discussed creating a comprehensive "best data backup and archive tools" comparison article.

---

## Context

Flosum is a customer of GrowthX's B2B content marketing services on a $200k+/year engagement. The partnership launched recently (roughly 4 weeks before this May 21 call), with GrowthX managing content creation and publication, and Flosum owning the Webflow CMS and product messaging. This was the team's second weekly sync to review progress on eight new blog posts aimed at capturing search traffic and LLM referral traffic. Aida Knežević (GrowthX) is leading the engagement as account manager but will be out of office the week of May 26 for her first extended time off since joining GrowthX. Jakub Rudnik (GrowthX) is the primary technical lead and will handle escalations while Aida is away.

---

## Relevance

**To GrowthX Delivery:**
- Flosum's Webflow setup supports dynamic CTAs and banners within the same blog collection template, enabling per-article optimization without design-level access — this opens a new content refinement lever beyond copy and structure.
- LLM referral traffic is now measurable via the Looker dashboard, establishing a CheckThat-adjacent KPI that can inform future AEO strategies for this and other accounts.
- Monthly vs. weekly reporting preference aligns GrowthX's client expectations: week-to-week noise doesn't drive decisions; month-over-month and impressions/ranking movement are the real signals.
- Clarity heatmap data (existing on Flosum's site) can be cross-referenced with content performance to guide layout and CTA placement on future articles.

**To GrowthX Business Development:**
- Early-stage partnership maturity: Eight blog posts in progress, calibration articles under review by Flosum's internal content team, and willingness to invest in custom comparisons ("best data backup tools" article) signal strong engagement and expansion potential.
- Aida's extended absence mid-engagement is a risk flag; documentation and Jakub's proactive communication will be critical to maintain momentum.
- Flosum's "high-intent visitor" tracking tool (Beau's project) could become a case study if successful — positioning GrowthX as a partner who enables B2B lead quality measurement, not just traffic volume.

**To CheckThat:**
- LLM referral traffic now visible and trackable through GA4; this is direct AI visibility data that CheckThat could highlight as a case study (with permission) or use to refine SEO+AEO bundling arguments.
- Competitor comparison articles (like "data backup tools") are AEO-friendly and likely to be cited by AI engines — opportunity to embed CheckThat thinking into that piece.

---

## Overview

- GrowthX set up a Looker Studio report for tracking blog performance, including Google Search Console and Google Analytics 4 data with filters to isolate GrowthX-created content
- Looker dashboard includes LLM referral traffic tracking (ChatGPT, Gemini, Perplexity, DeepSeek) to measure AI visibility impact
- Team agreed monthly reporting cadence makes more sense than weekly as content matures and initial impressions build
- Flosum's Webflow CMS supports custom CTAs, banners, and integration with Clarity heatmap data for content optimization
- Beau Beamon building a high-intent visitor tracking tool to identify companies with multiple site visitors
- Jakub Rudnik advancing no-index page cleanup project (estimated multi-week) and will separate reporting for refreshed vs. new content
- Flosum team to provide feedback on calibration articles by end of week; eight new blog posts in progress
- GrowthX team needs editor-level Webflow access (design-level access not required); Beau to adjust permissions

---

## Key Topics

### Performance Reporting Setup

  - Looker Studio report created to track blog performance
  - Includes data from Google Search Console and Google Analytics 4
  - Features filters to isolate GrowthX-created content
  - Tracks metrics like clicks, impressions, CTR, and LLM referral traffic
  - Team discussed preference for monthly vs. weekly performance tracking as content matures

### Content Creation and Optimization

  - GrowthX working on 8 new blog posts
  - Flosum team to review calibration articles and provide feedback
  - Discussion on incorporating custom CTAs and banners in blog posts
  - Potential to leverage Clarity heatmap data for optimizing content layout
  - Consideration for creating competitive comparison content without direct competitor bashing

### Technical Access and Permissions

  - GrowthX team needs proper access to Webflow for blog post creation
  - Beau to adjust Webflow permissions to editor-level access (not design access)

### Ongoing Projects

  - Jakub working on no-index page cleanup, expected to be a multi-week project
  - Beau developing a tool to track visitors with high intent

---

## Action Items

- **Matt Lyman (Flosum):** Ensure calibration articles are reviewed and feedback provided by end of week (delegated to Keith for content review)
- **Beau Beamon (Flosum):** Adjust Webflow permissions for GrowthX team from design-level access to editor-level access for blog collection updates
- **Aida Knežević (GrowthX):** Hand off engagement to Jakub Rudnik for week of May 26 while out of office; continue work on eight blog posts and calibration edits
- **Jakub Rudnik (GrowthX):** Continue no-index page cleanup project; provide update next week on actionable redirects and scope; collaborate with Flosum on custom CTA and banner strategy
- **Team:** Explore custom CTA and banner implementation in Webflow blog posts using Clarity heatmap insights; create comprehensive "best data backup and archive tools" comparison article without direct competitor criticism

---

## Transcript
**Jakub Rudnik:** That's great.

**Jakub Rudnik:** A little stroke of luck on a Wednesday.

**Jakub Rudnik:** Nice.

**Aida Knežević:** Brian, how are you?

**Aida Knežević:** No, how's it going, Brian?

**Aida Knežević:** Not too bad.

**Brian Evans:** Just cranking away.

**Brian Evans:** Never a shortage of things to work on.

**Jakub Rudnik:** I feel you.

**Jakub Rudnik:** Totally feel you.

**Brian Evans:** How about y'all?

**Brian Evans:** How are you guys doing?

**Brian Evans:** Good, good.

**Aida Knežević:** I'm going on vacation on Saturday, so I'm not going to be here next week.

**Aida Knežević:** It's my first serious time off since I joined Growthx, so I'm just trying to get all my ducks in a row and make sure that there are no surprises while I'm away.

**Brian Evans:** Okay.

**Brian Evans:** Yeah, huge.

**Jakub Rudnik:** But it is already ahead of stuff.

**Jakub Rudnik:** It feels really good.

**Jakub Rudnik:** Not everyone's like that.

**Jakub Rudnik:** I wouldn't be like that.

**Jakub Rudnik:** So it's really nice to have that on our end.

**Jakub Rudnik:** Hey, Matt.

**Aida Knežević:** Are we waiting for Sakshi or maybe it's too late for her?

**Matt Lyman:** We can move without she had something come up this morning, so she may make it if she has an opportunity, but she's not.

**Matt Lyman:** Okay, perfect.

**Aida Knežević:** So before we get into the content and like the more detailed stuff, I logged into Webflow and I, you know, I know Sakshi, she shared like walkthrough video that I think your web agency shared.

**Aida Knežević:** The issue is that I cannot access the blog posts, so I don't have permissions.

**Aida Knežević:** I think I can only see.

**Aida Knežević:** So I'm going to share my screen with you.

**Aida Knežević:** So when I'm in editor and I'm on like your site in the video, I can see.

**Aida Knežević:** Blogs here, but they're not showing up for me.

**Aida Knežević:** So I'm thinking that it's probably something to do with the user permissions.

**Aida Knežević:** Yeah.

**Drew Noel:** Beau, can you help accelerate this point potentially?

**Drew Noel:** I know that the line with Axio is a little bit discombobulated to a certain degree, but I think we need to just, like, run this so that we can help facilitate this work done.

**Brian Evans:** Thank you.

**Beau Beamon:** Yes, let me contact them.

**Beau Beamon:** What is the username?

**Beau Beamon:** It's team at growthxlabs.com.

**Aida Knežević:** So I'm going to share it in the channel.

**Aida Knežević:** Thank you.

**Beau Beamon:** Let me do the chat.

**Beau Beamon:** Thank you.

**Beau Beamon:** Awesome.

**Drew Noel:** Yeah.

**Drew Noel:** Okay.

**Drew Noel:** Perfect.

**Aida Knežević:** Just wanted to get that out of the way.

**Aida Knežević:** So today there are a couple of things I wanted to show you, but I first wanted to see if you had any other feedback on the calibration articles.

**Matt Lyman:** I promised you they'd be done today.

**Matt Lyman:** That's a little tiny bit delayed.

**Matt Lyman:** And that's only because I sent them over to a guy on our team named Keith, who is very, he actually, I guess, helped copyright some of our stuff.

**Matt Lyman:** But he's like a really good person to review for the overall content and not messaging, but the content.

**Matt Lyman:** And so he said he's happy to do it.

**Matt Lyman:** He should have it today or tomorrow.

**Matt Lyman:** That's what he said, just based off of his timelines.

**Matt Lyman:** Okay.

**Matt Lyman:** So that's, that's the update.

**Matt Lyman:** And so if we want to give it like, I'll make sure that it's, it's all in there and that all of our stuff is fine.

**Matt Lyman:** Okay, okay, that makes sense.

**Aida Knežević:** Thank you for your patience.

**Aida Knežević:** The truth is I thought somebody had sent it to him and nobody had sent it to him.

**Matt Lyman:** So I'll take that, but yeah.

**Matt Lyman:** Okay, okay, no problem.

**Aida Knežević:** We are working on eight new blogs right now, but depending on his feedback, we can go back and like make some changes.

**Aida Knežević:** I mean, the documents that you shared, was able to kind of plug them into Aerofs and we were able to get, I think the product messaging should be on point.

**Aida Knežević:** Obviously, you know, make sure to flag anything that sounds, you don't want to emphasize, you know, some clients, their product might have certain features, but they don't want to always talk about them for, you know, various reasons.

**Aida Knežević:** So you can just flag that stuff as it comes up.

**Aida Knežević:** Sounds good.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** So today...

**Aida Knežević:** I wanted to show you your looker report.

**Aida Knežević:** So for each and every one of our clients, we do performance reporting.

**Aida Knežević:** And as we publish blogs, every week when we meet up, we review the performance report.

**Aida Knežević:** We take a look at like if there are any changes, any blogs are doing particularly well, or if any blogs are getting less traffic.

**Aida Knežević:** And because we publish a lot, so we typically publish like at least six or seven blogs per week, ideally, finding a way to track the performance just of those blogs is a little bit tricky because clients usually have like you have your own blog posts.

**Aida Knežević:** And like, we want to make sure that we're just tracking our efforts.

**Aida Knežević:** First and foremost, you have like a good idea of like whether like the stuff's making an impact.

**Aida Knežević:** So we do that using a looker studio report.

**Aida Knežević:** This is, this is

**Aida Knežević:** So I already, I added the link to it in the agenda.

**Aida Knežević:** You all should have access to it and you have editing access.

**Aida Knežević:** That means that you can like adjust the timelines, things like that.

**Aida Knežević:** But if you feel like you really want to make some big changes, just let us know so that I'm not, I don't think that like something changed overnight, basically.

**Aida Knežević:** So right now, this report contains the data from your entire website because we haven't published anything yet.

**Aida Knežević:** But once we start publishing, we're going to use this filter right here to filter out all of our just our blog posts.

**Aida Knežević:** And this chart right here, it's showing the data from your Google Search Console.

**Aida Knežević:** So that's the data source for this particular for this particular graph.

**Aida Knežević:** And then this table is also pulling data from your Google Search Console.

**Aida Knežević:** So you can see like URL clicks, impressions, overall click-through rate.

**Aida Knežević:** We can also modify this table so that it shows, like, week-over-week performance.

**Aida Knežević:** Like, you can see whether a blog is doing better or worse, so you can see, like, changes in traffic.

**Aida Knežević:** The next page, so it's three pages, the next page combines data from Google Analytics 4, which is this table right here.

**Aida Knežević:** And this is GSC data.

**Aida Knežević:** This is just the query data, so it helps to know, like, what type of queries are, like, driving the most traffic to your site.

**Aida Knežević:** Obviously, this is just your entire website at the moment.

**Aida Knežević:** We're also going to filter this out.

**Aida Knežević:** And then the last page of the report is LLM referral traffic, so this page basically has a filter on it that it only includes referral traffic from LLMs such as ChatGPT, Gemini, Perplexity, and DeepSeek. Typically we don't filter this page for our blog posts, as a lot of clients just want to see the impact on their entire site from LLMs. This pie chart right here is incorrect right now. I'm going to have to fix it later because it should be showing ChatGPT, Gemini — a breakdown between different LLMs — but I'm going to tackle this later because I really couldn't figure it out in time.

**Aida Knežević:** So it's great to have this data.

**Brian Evans:** Thanks for pulling that.

**Brian Evans:** No problem.

**Matt Lyman:** Quick question on the query strings in there for the search from the search console. I think it's on the weekly performance page. It's GA4 potentially.

**Brian Evans:** Yeah.

**Matt Lyman:** Just based off of how I'm looking at this right now, I see that it's the query.

**Matt Lyman:** Oh, is the query below?

**Matt Lyman:** I see.

**Matt Lyman:** OK.

**Matt Lyman:** Yeah.

**Matt Lyman:** So down below is going to be who's searching.

**Matt Lyman:** I just I was looking at this on these are all the landing pages right now, which I also want to see.

**Matt Lyman:** So please don't feel like you have to get rid of those because that's something I look at frequently.

**Matt Lyman:** I was just wondering how we were looking at that to identify what they were searching for.

**Matt Lyman:** But it looks like if we scroll down to the next section of this, that's the query. So right now we're dominating when people search for your brand name.

**Matt Lyman:** So this is branded search traffic.

**Matt Lyman:** Yeah.

**Matt Lyman:** Yeah.

**Matt Lyman:** Yeah.

**Aida Knežević:** Like a lot of people are interested in jobs at Flosum.

**Matt Lyman:** Yeah.

**Matt Lyman:** Yeah.

**Aida Knežević:** But yeah, sometimes I mean, the query.

**Aida Knežević:** These are interesting because I'll give you an example.

**Aida Knežević:** So one of my clients, they have a dental staffing platform, and they noticed that they got a ton of traffic from a query that was basically their brand name, plus reviews and complaints.

**Aida Knežević:** And they didn't have any content on their website.

**Aida Knežević:** So we literally created a blog post that was just like a compilation of different reviews.

**Aida Knežević:** I mean, they're like consumer facing, so it's different.

**Aida Knežević:** And now they're like capturing that traffic that otherwise would be wasted.

**Aida Knežević:** So it's good to check in once in a while and see if there are any opportunities for...

**Aida Knežević:** Oh my God, did you hear that?

**Aida Knežević:** There was like a thunder strike.

**Aida Knežević:** That was so loud.

**Aida Knežević:** Oh, wow, no.

**Matt Lyman:** there's a thunderstorm here.

**Matt Lyman:** So I was like, what is that?

**Aida Knežević:** It sounds like a bomb went off.

**Aida Knežević:** So yeah, it's good to check in on the queries once in a while.

**Aida Knežević:** Yeah, this is super helpful.

**Matt Lyman:** Yeah.

**Matt Lyman:** I appreciate that.

**Matt Lyman:** I do like the idea of change over time.

**Matt Lyman:** I don't know if it's a week-to-week change or if it's month-to-month.

**Matt Lyman:** I know things change quickly and then can go back.

**Matt Lyman:** So however that fits based off of the stuff that you guys have had with other customers.

**Beau Beamon:** Matt, just to quickly interrupt. You guys don't need design access to Webflow, do you?

**Aida Knežević:** So I don't believe I'm seeing Jakub shake his head.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** So I'm pretty positive that we wouldn't need because we'll just be updating content within a collection and not doing the design of the page and the collection styling.

**Jakub Rudnik:** So I believe it's no.

**Jakub Rudnik:** Uh, we'll obviously let you know if that doesn't work too.

**Jakub Rudnik:** I believe it's a no from my Webflow experience. Thank you. Sorry to interrupt.

**Matt Lyman:** I think I'm the one that gave you that, by the way, because it was a it was a full license that we had available and I was just like, oh, that should make it simple.

**Matt Lyman:** So we'll adjust however that needs to be adjusted.

**Matt Lyman:** Yeah, thank you.

**Jakub Rudnik:** Well, Aida, I'm unmuted.

**Jakub Rudnik:** Just a couple things on the reports.

**Jakub Rudnik:** One, Matt, I also like when I do this internally, like the time over time and I think month over month, you know, when we zoom forward, a couple months makes a ton of sense.

**Jakub Rudnik:** That's where I usually start to look.

**Jakub Rudnik:** And then if we get, you know, 6 or 12 months beyond, we'll start looking quarters, obviously, but with like the amount of traffic and then how this should be growing, I think month over month will make the most sense. Just we'll zoom forward a little bit. But we could even duplicate that view and then do a month over month view too, so we can see it both ways — the raw impressions and clicks and also month over month. So that could be useful. And then the only other addition is, I know we're starting obviously with new content. That should be the bulk as we've kind of discussed, but as we start to do refreshes too, we'll want to separate those. We've got a couple different ways to report on those, but since they will have some existing impressions and traffic, we'll still want to separate that because the moment we refresh, we haven't necessarily changed anything on their metrics. We want to see that over time, but we'll take a look at that separately. There's a little bit different reporting, but just wanted to call that out that this is specific to the new content.

**Matt Lyman:** So, yes, totally.

**Matt Lyman:** I'm on board with that.

**Matt Lyman:** just for, I guess, a little bit of clarity from my end, since we've all, everyone on this has only worked with me for a month.

**Matt Lyman:** You all started at the exact same time working with me.

**Matt Lyman:** There are a lot of those leading indicators that are nice to look at for the weeklies, but there's so many of them that it doesn't make a lick of difference.

**Matt Lyman:** Like, I'll say this to Drew and Beau, like, don't ever expect me to ask you how many demos we have week over week because I can't.

**Matt Lyman:** It's just a silly number.

**Matt Lyman:** And so like it's sort of the same way I see with these is week over week might be good up front just so we can see how it goes so we can understand what's what's working short term.

**Matt Lyman:** But as we get into it monthly, it's just it's going to be perfect.

**Matt Lyman:** So especially with all other variables being considered, like once we get into the rhythm of, yes, it's X number every week, it's X number every week, it's X, it's just going to be that.

**Jakub Rudnik:** Yeah, the impression, like just in the first four or six weeks or something, it's like did that index to that rank?

**Jakub Rudnik:** Do we see impressions?

**Jakub Rudnik:** And so we should see like batch of content within a certain number of days.

**Jakub Rudnik:** Like then we'll see us like impressions because stuff is starting.

**Jakub Rudnik:** Right.

**Jakub Rudnik:** And so as long as that's there, that for me, like that's how I always choose.

**Jakub Rudnik:** We have we're seeing growth and we zoom back a little bit and we can slowly zoom back as like the timeline extends a little bit.

**Jakub Rudnik:** But as long as it is going up more at the monthly level and then I lost my train of thought.

**Jakub Rudnik:** But that's exactly how I think about it.

**Jakub Rudnik:** then, yeah, it's growing.

**Jakub Rudnik:** We'll see those spikes.

**Jakub Rudnik:** But then if we're looking week over week, we see a 10 percent.

**Jakub Rudnik:** Traffic drop when we have 100 clicks, like that doesn't matter compared to the longer term, like impression growth.

**Jakub Rudnik:** As long as we're seeing that and keywords move into the right position, that's more of an indicator of future traffic than, you know, the week to week, small changes.

**Jakub Rudnik:** So totally on board.

**Jakub Rudnik:** I just wanted to echo it and plus one.

**Jakub Rudnik:** Yeah.

**Beau Beamon:** I have a question.

**Beau Beamon:** So as we're starting to see more and more growth here and more and more visitors, et cetera, can you guys provide on a weekly basis a list of domains and unique visitors?

**Beau Beamon:** Would that be possible?

**Aida Knežević:** You mean, like the, what do you mean by domains, like page URLs?

**Aida Knežević:** No.

**Aida Knežević:** So Flosum, for instance.

**Beau Beamon:** Well, people from the company, a number of people, and it can be more than three.

**Beau Beamon:** OK, and I don't want anybody who went to employment pages or anything, you know, I don't want people who are looking for a job.

**Beau Beamon:** What I'm looking for is I'm looking for a number of people, unique people from a domain that is more than three.

**Beau Beamon:** It's of like intent-ish data.

**Jakub Rudnik:** Yeah, but we don't have that capability in our, like, generally...

**Jakub Rudnik:** Well, Looker, you don't have that capability.

**Jakub Rudnik:** So we're, and Looker is just pulling in, like, reframing the data from GCNGA4.

**Jakub Rudnik:** So we, we're, we're just taking the data you all have access to already and gave us and putting it into a way that's more accessible and doable for our purposes.

**Jakub Rudnik:** So we're not adding, we're not supplementing with any...

**Jakub Rudnik:** I do think that's something that everybody wants more of and would be theoretically part of some offering in the future that we have, but it's definitely not what we're doing with this, and it's not even in our tech right now.

**Jakub Rudnik:** So maybe more of an add-on from another tool and how that integrates with what we're doing.

**Beau Beamon:** Yeah, I was asking because I'm building basically something that provides data from those coming to our site with intent.

**Beau Beamon:** So yeah, I'll reveal it later on, but this is a project I'm working on this quarter.

**Beau Beamon:** Awesome.

**Jakub Rudnik:** Well, we would love to see what comes out of that and what is available and comes from this type of content, because that will only make what we're choosing for topics and what conversion we do on those pages more impactful.

**Jakub Rudnik:** So collaboration on the other direction would be very helpful.

**Jakub Rudnik:** Yeah, absolutely.

**Jakub Rudnik:** And that's why I was asking you if you guys had that, because then we can do the comparison.

**Beau Beamon:** But we'll figure it out and have this conversation later.

**Beau Beamon:** I didn't want to interrupt or anything, but I was just curious.

**Beau Beamon:** Thank you.

**Beau Beamon:** No problem.

**Aida Knežević:** Yeah, I know some clients have used Koala in the past for that type of tracking, but it depends.

**Aida Knežević:** Another thing I wanted to talk about, I mean, I couldn't access, once I get access to like the actual blog, I'm going to be able to see like the layout better.

**Aida Knežević:** One thing I did notice, and I want to kind of talk about it early, I know that we're tracking like organic traffic for like the first couple of months as we're working together.

**Aida Knežević:** But I didn't want to, I didn't want to ask if, for example, your blog has, if you have like any custom CTAs that you could like plug into the blog posts.

**Aida Knežević:** Like not just, for example, here we have like the newsletter sign up and then we have like like a CTA at the top to like talk to an expert and a phone call.

**Aida Knežević:** But like sometimes we might have, depending on like the customer's CMS, we might be able to plug in like a CTA here, like check out the product page for data backup and archive or to download an e-book or something.

**Aida Knežević:** So is that something that like your CMS supports?

**Saakshi Jain:** Yes, CMS supports that.

**Saakshi Jain:** That's something that we haven't done and we haven't kept up with.

**Saakshi Jain:** But yes, CMS can definitely support it.

**Saakshi Jain:** The other thing that we can do is we can also insert a banner, a relevant one, like read the case study or something of that sort.

**Saakshi Jain:** It just breaks away from so much text.

**Saakshi Jain:** That's also something that we can do through Webflow, but that's a capability that we haven't really explored at all.

**Saakshi Jain:** Okay.

**Saakshi Jain:** Okay, perfect.

**Jakub Rudnik:** Yeah, with my experience with Webflow, that sounds like that's similar to what I've done at Scribe.

**Jakub Rudnik:** I've been...

**Jakub Rudnik:** I've been...

**Jakub Rudnik:** been...

**Jakub Rudnik:** Other places where I've used it.

**Jakub Rudnik:** We could also, Aida brings up a great point, and we could then consider over time, should we have, you know, what's on that right side area?

**Jakub Rudnik:** How should we be using that?

**Jakub Rudnik:** Like, we would want to look at, like, are we converting to newsletters and what happens downstream?

**Jakub Rudnik:** Like, obviously, we're just trying to generate traffic right now and get people onto the site so we can learn and do more things.

**Jakub Rudnik:** But I think over time, we should be analyzing that will be part of like a collaboration with us will be only, we'll get more impact by having that collaboration with you on the conversion front, step in line.

**Jakub Rudnik:** think we can probably have some of this already, but can be done with short codes or design on the, you know, banner over the top and stuff.

**Jakub Rudnik:** So I think that'll be a lot of future discussion, especially once we have a lot of traffic will be spent there and how to better utilize that traffic.

**Jakub Rudnik:** So, but good that you have a lot of those mechanisms in place.

**Jakub Rudnik:** We just have to utilize them a little bit more.

**Saakshi Jain:** Yeah, we do have clarity in place as well.

**Saakshi Jain:** And we did notice that people actually tend to go on the right a lot.

**Saakshi Jain:** So we would think that we'd probably put insert a banner right down.

**Saakshi Jain:** An e-book or something of that sort.

**Saakshi Jain:** We haven't done any of it.

**Saakshi Jain:** It's just the insights that we've collected, but we haven't re-reactioned on that.

**Saakshi Jain:** It has to be upfront there.

**Saakshi Jain:** Just when we were transitioning to this website, we thought that we were transitioning to Webflow so that we can incorporate all of that, but it never came to that point that we would incorporate all of this.

**Saakshi Jain:** So, yeah, in case you were analyzing any of it and in case you think that there is something relevant, we can always supplement it with that clarity database of what the heat maps are saying and what everything, like what the recordings are saying.

**Saakshi Jain:** And seeing if there's any relevant keywords or if there's any relevant banners that we can insert anywhere.

**Jakub Rudnik:** Yeah, Webflow is a little bit funky depending on, like, you all have so much tech and operations that I think we will overcome this better than places I've been before.

**Jakub Rudnik:** But because, like, you have one collection for the blog and typically you have one design for that.

**Jakub Rudnik:** And then how do you make that custom or how do you make, you know, get the right CTA because we're going to have content for different types of people with different problems.

**Jakub Rudnik:** So the one CTA won't necessarily fit all in the way that some other.

**Jakub Rudnik:** Blogs will.

**Jakub Rudnik:** So it'll be something to figure out and think on.

**Jakub Rudnik:** But with, like, again, the tech stack you're mentioning, there's a lot we can do in action.

**Jakub Rudnik:** So we'll start to put thoughts together on that and then collaborate on how to, like, actually execute that, given all the tech you do have.

**Jakub Rudnik:** But that's all good to know.

**Saakshi Jain:** If I can't do anything, we can always do the text once.

**Saakshi Jain:** So we could actually incorporate it in the text.

**Saakshi Jain:** Yeah, yeah, absolutely.

**Aida Knežević:** So those are all the updates that I had.

**Aida Knežević:** So in case someone joined later, I am going to be out of office all of next week.

**Aida Knežević:** The content is going to be produced and delivered.

**Aida Knežević:** And also, if you decide, like, if you approve something for publishing, we will also publish it next week.

**Aida Knežević:** So there's a CM that's going to do that.

**Aida Knežević:** For any sort of questions or comments, you can reach out to Jakub.

**Aida Knežević:** He's like the right person, pretty much, like for everything.

**Aida Knežević:** That you want to know.

**Saakshi Jain:** Aida, I just wanted to know, there were a bunch of documents that I'd sent across.

**Saakshi Jain:** Were they helpful?

**Saakshi Jain:** Do you need something more?

**Saakshi Jain:** They were very helpful.

**Saakshi Jain:** Yes, thank you.

**Aida Knežević:** We were talking about it in the beginning of the meeting.

**Aida Knežević:** I was able to use them and then I kind of shortened them a little bit, like just extracted like the key points and I added them to our polishing instructions.

**Aida Knežević:** So now I think the product messaging is a lot clearer.

**Aida Knežević:** Also, we incorporated like, I think it was like what the customer is looking for, like their main pain points.

**Aida Knežević:** So this is also what we incorporated into the polishing instructions.

**Aida Knežević:** And also I, for this week, we have an article that compares like that.

**Aida Knežević:** It's about own backup alternatives or actually own alternatives.

**Saakshi Jain:** And I, for

**Aida Knežević:** There was a lot of valuable stuff in that doc regarding OWN and how it's different from Flosum, but I was a little bit hesitant to include it because some clients don't want to talk badly about their competitors, at least in a blog post where it's like everyone can see.

**Aida Knežević:** So I ended up removing some of it just to kind of tone it down.

**Saakshi Jain:** Yeah, I understand.

**Saakshi Jain:** Okay, perfect.

**Saakshi Jain:** Good time.

**Saakshi Jain:** You got that insight.

**Saakshi Jain:** It's Bubba.

**Saakshi Jain:** Thank you so much.

**Saakshi Jain:** Yeah, yeah, no problem.

**Aida Knežević:** Thank you for sharing that.

**Jakub Rudnik:** Only one other item to add — apologies to go off script, but the no-index pages cleanup has not been forgotten. I started it. I just need to marry in some of the data from real pages so I can make more recommendations on where to go. Sometimes it's very simple, like we should just redirect here. Other times getting a larger scope of all of your pages is more difficult. So I'm still in that process and I'll have more next week. I don't know exactly how many pages we're talking about, but I'll be able to get through that entire list within the next week and have more actionable items we can start to whittle down. Probably be a couple week project would be my guess, but thanks for the patience on that as I was coming back from vacation and just didn't get to it as much as I would have another week. So I'll keep you updated on that one.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** Anybody else?

**Aida Knežević:** Any questions?

**Aida Knežević:** Nope.

**Matt Lyman:** I was just going to say that internally, if it makes more sense that way, it could be good for us to do a competitive where it's one of those best data backup and archive tools that lists all of them, and then it's not a bashing on them.

**Matt Lyman:** It's more of the comparison.

**Matt Lyman:** So I don't know which team that would be on, but we can talk about that.

**Jakub Rudnik:** I think overall, you'd want the total best list and any variants on that.

**Jakub Rudnik:** Then you want your alternatives.

**Jakub Rudnik:** to own backup, then you want the, you know, own backup versus Flosum, if that makes sense, like, and for all of your type of lists, and then also like any kind of synonyms to that larger original list, if there's anything that people call it that's not like the category name, like you'd see at G2, and so that's my typical play when you're looking at the MoFu kind of down software plays, like there's so much meat on the bone, and usually we can find more than the instincts say up front, so I agree with that, but you can, you can like not bash while still being honest, and leading the reader to why you are the better option, where, you know, what they truly need, and setting up, setting the table for that post, so we do that too, but a good call.

**Aida Knežević:** Okay, perfect, yeah, thank you so much for your time, looking forward to seeing the feedback, and yeah, any questions, just send me a message in Slack.

**Aida Knežević:** Thank you, see you next week.

**Saakshi Jain:** Thanks everyone.
