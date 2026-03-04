# Town/GrowthX Weekly Sync

<metadata>
date: 2025-08-06
time: 18:00 UTC
duration: 23 minutes
organizer: ehtisham@growthx.ai
participants: Darrell Etherington (GrowthX), Ehtisham Hussain (GrowthX), Ryan Johnson (Town), Jean-Denis Greze (Town)
enriched_on: 2026-03-03 18:45 UTC
fathom_recording_id: 78918112
fathom_url: https://fathom.video/calls/371514892
share_url: https://fathom.video/share/c-BwCKbzbjCh9K4VdqyMydFNQzjQfYCv
source: fathom
</metadata>

---

## Summary

GrowthX and Town aligned on three critical workflow improvements: adding a final proofreading step before publishing to catch errors from multiple editors, establishing Figma-based header image creation with GrowthX handling design and Town approving visual style, and resolving a GA4 tracking issue that caused a multi-day analytics blackout. The team also discussed moving Town's blog URL structure back from /resources to /blog with appropriate 301 redirects for SEO preservation, and clarified that Jean-Denis's team can make minor content edits directly in the CMS while major revisions require re-review before publishing.

---

## Context

This is a weekly sync between GrowthX's delivery team and Town, an external client. Town is a content platform company that GrowthX is supporting with blog content production and website optimization. The meeting focused on operational workflow improvements, asset creation processes, and technical SEO implementation as Town scales its content publishing pipeline. The GrowthX team (Darrell and Ehtisham) acts as the primary delivery partners, while Town's team (Ryan, Jean-Denis, and their web team) handles content review, publishing, and website infrastructure.

---

## Relevance

- **To GrowthX Delivery:** Quality control process improvement (added final proofreading step) demonstrates the need for collaborative workflows with external editors. Multi-editor collaboration creates potential for errors that require manual verification before publishing. Figma permission management is a coordination point for visual asset creation.

- **To CheckThat:** Website URL structure decisions (/blog vs /resources) impact SEO metrics and long-term discoverability. The team is tracking Google Analytics and Google Search Console data; analytics setup errors can hide performance data. Fresh content publishing is ongoing with staggered schedule to maintain impression growth.

- **To GrowthX Business Development:** Town account shows steady content production (3 new blog posts weekly) and positive metrics (impressions growing despite analytics gaps). Team is moving from bulk publishing to staggered releases, suggesting maturity and operational sophistication. Risk flagged: analytics tracking gap lasted several days; account health depends on reliable measurement.

---

## Overview

- New proofreading step added to workflow to catch errors from multiple editors
- Image handling process clarified; GrowthX to create header images using Figma
- Website structure changes discussed; considering reverting from /resources to /blog
- Analytics issues identified and being addressed

---

## Key Topics

### Content Production and Quality Control

  - Three new blog posts published since last meeting
  - Identified source of caption issues (meta descriptions pulled forward)
  - New final proofreading step added to workflow to catch errors from multiple editors
  - Town team given permission to make minor edits directly in CMS for accuracy

### Image Handling Process

  - GrowthX team to create header images using Figma, pending editor permissions
  - New text-on-graphic format to be used instead of people images
  - Future plans to integrate image creation into production pipeline

### Website Structure and SEO

  - Discussing potential reversion from /resources back to /blog URL structure
  - Need for redirects (301) from /blog to /resources or vice versa
  - Importance of maintaining consistent URL structure for SEO and user experience

### Analytics and Tracking

  - Google Analytics tracking was broken for a few days due to wrong key implementation
  - Google Search Console data unaffected, showing continued impression growth
  - Team to monitor analytics closely as new content is published

### Publishing Schedule and Workflow

  - Discussion on staggering publish dates instead of bulk publishing
  - Clarification on review process: minor changes approved with comments, major changes require re-review

---

## Action Items

**Ehtisham Hussain (GrowthX)**
- Add final proofreading step to workflow before publishing articles. Check for missing spaces, headings, formatting issues.
- Begin using Figma to create header images with text for blog posts. Use existing templates, vary styles.

**Darrell Etherington (GrowthX)**
- Contact Tony via Slack to discuss removing visible image captions from blog posts and moving alt text to proper meta tag.
- Verify editor permissions in Figma for pod B account. If not resolved, coordinate with Town team for access.

**Jean-Denis Greze (Town)**
- Discuss with Tony: determine whether to revert to /blog URL structure or set up /blog to /resources redirect. Consider SEO impact and implement appropriate permalinks.

---

## Transcript

**Darrell Etherington:** It was very long, and I don't know where to start.

**Darrell Etherington:** Let's see.

**Darrell Etherington:** About the images, like, I removed them because then I thought, yeah, just, we're just not going to have any, but we can work that out on this call.

**Darrell Etherington:** But I think for now, the best process is to just deliver them with none, and then they can add them if they need to, unless there's an easy way to just clip the template or whatever.

**Ehtisham Hussain:** I requested access to that Figma as well.

**Darrell Etherington:** Okay, you can use, I did it on the pod account, so you can use the pod account if you want, and that will give you access.

**Darrell Etherington:** Hi, Ryan.

**Ryan Johnson:** Hey, guys, I don't know why I was blurred for a second, but.

**Ryan Johnson:** Yeah.

**Ryan Johnson:** Yeah, yeah.

**Darrell Etherington:** It's like, you're part of the background.

**Ryan Johnson:** Yeah.

**Ryan Johnson:** Yeah.

**Ryan Johnson:** It doesn't make me feel very special or unique.

**Ryan Johnson:** But hey, finish your conversation.

**Darrell Etherington:** Oh, no, no.

**Darrell Etherington:** We were just talking about the technical details of how we use a shared account for the Figma.

**Ryan Johnson:** So Ehtisham should be able to get access.

**Ryan Johnson:** Okay, cool.

**Ryan Johnson:** And now that I have, like, now I'm not blurred and I've got your faces on my screen, I'm realizing that you are blurred for me because I have my glasses on.

**Darrell Etherington:** So let me grab my glasses.

**Ryan Johnson:** Okay.

**Ryan Johnson:** Yeah.

**Ryan Johnson:** All right.

**Ryan Johnson:** Cool.

**Ryan Johnson:** Um, yeah.

**Ryan Johnson:** I think maybe we can just hang tight for a minute.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Sure.

**Ryan Johnson:** We'll just jump in between meeting rooms and all that good stuff.

**Darrell Etherington:** I'm also responding to a ticket.

**Darrell Etherington:** We use Linear.

**Darrell Etherington:** I don't know what you guys use, but I...

**Ryan Johnson:** We do as well.

**Darrell Etherington:** Yeah, yeah, yeah.

**Darrell Etherington:** It was a, I was, this is the first time I've used it here.

**Darrell Etherington:** And I was a little bit like, oh, okay, there's a lot.

**Darrell Etherington:** But it's very easy once you get the hang of creating issues.

**Ryan Johnson:** They're all good.

**Ryan Johnson:** Once you figure it out, it's pretty slick.

**Ryan Johnson:** Honestly, our engineering team uses it more than I do.

**Ryan Johnson:** Yeah.

**Ryan Johnson:** They like, they tag me and stuff in there.

**Ryan Johnson:** And then I'm like putting it in my own notes list or task list or stuff like that.

**Ryan Johnson:** So I'm not, certainly not a power user at this point.

**Ryan Johnson:** I'm sure they'd be disappointed if they saw how I use it.

**Darrell Etherington:** Oh, yeah.

**Ryan Johnson:** Same here.

**Ryan Johnson:** Yeah.

**Darrell Etherington:** It's an engineering-led tool choice.

**Darrell Etherington:** Then I'm in there like, okay.

**Ryan Johnson:** The team loves it though.

**Darrell Etherington:** Like the engineering team.

**Ryan Johnson:** Oh, I know.

**Ryan Johnson:** I mean, they're just picking up Steam, Linear, I mean, specifically, and our engineering team uses it a ton.

**Ryan Johnson:** And just like, I think it's like their preferred way of seeing the world.

**Darrell Etherington:** Like Linear really clicks into that.

**Darrell Etherington:** It's like exactly their language.

**Darrell Etherington:** It's how they think and speak and prioritize things.

**Darrell Etherington:** This has always been like, there's, I mean, I forget what some of the earlier ones were.

**Darrell Etherington:** Maybe Jira or something, but there's always a ticketing system thing, and then Eng will push the ticketing system, and then the rest of the org tries to accommodate, but ends up being like, I'm just going to use Trello or something, something where I understand what's going on.

**Darrell Etherington:** Yeah, exactly.

**Ryan Johnson:** Well, I mean, it's just a funny thing, too, because I feel like the more I work with engineers, like, the more I respect the fact that they just want a tool that gets the job done, as opposed to one that looks nice and is pleasant to work with, which is something I appreciate, but they're like, nah, it should be black with white text and no frills kind of thing, and you know, that actually makes sense.

**Darrell Etherington:** I respect that.

**Darrell Etherington:** Like, just get it done.

**Darrell Etherington:** No, I do like it, and I'm trying to be like, oh, I should change my thinking rather than the other way around, because I think it will benefit me better in the future.

**Darrell Etherington:** I think they're right.

**Ryan Johnson:** I think they're right.

**Ryan Johnson:** It's more streamlined and efficient and not so heavy, so yeah, got it, got it.

**Ryan Johnson:** Okay, we're of like minds on that.

**Darrell Etherington:** Yep.

**Darrell Etherington:** Is that Jean-Denis?

**Darrell Etherington:** It's a little small on my screen, I can't see.

**Jean-Denis Greze:** Yeah, that's me.

**Darrell Etherington:** Yep.

**Darrell Etherington:** Hello.

**Jean-Denis Greze:** Hi, how are you?

**Darrell Etherington:** Pretty good, yourself?

**Jean-Denis Greze:** Good.

**Darrell Etherington:** Busy, but good.

**Darrell Etherington:** Good, okay.

**Darrell Etherington:** Well, we can try to make this quick, maybe get you back some time.

**Darrell Etherington:** But Ehtisham, you want to kick us off here?

**Ehtisham Hussain:** Let me share my screen.

**Ehtisham Hussain:** So, since our last meeting, we've published three more blog posts and we found out where the caption under the image was coming from.

**Ehtisham Hussain:** It's the description box for the meta descriptions in the back.

**Ehtisham Hussain:** I think with the new design, that may have been pulled forward.

**Ehtisham Hussain:** It's supposed to give a quick overview for search engines of what the article is all about, and that's pretty much the update. We are following all the feedback from Tony, and I saw how some of those missing spaces and stuff were in there, because there were multiple people who edited the documents. So we're going to add another step in our workflow where we're going to do one final proofread before publishing, because, for example, there's one article that has 25 headings in it, and heading number 14 is missing. That heading was there up until the last moment, but then it was edited out as part of the back and forth between the two teams.

**Ehtisham Hussain:** We can add one final proofreading before publishing because every article is being edited by multiple people, there are comments on it, and then I go in, resolve the comment, add something or delete something. So we have to make sure that these things don't happen again.

**Darrell Etherington:** Yeah, and also I think those were some older products, is that right, Ehtisham?

**Ehtisham Hussain:** Some of them are newer, some of them are older, yeah. What I did was go into the content OS and look at the Google Doc, and I saw different versions of it. That kind of helped me see where the missing space is or where the bold character was coming in from.

**Jean-Denis Greze:** Oh, using revision history?

**Ehtisham Hussain:** Yeah, that's not the AI, that's the human error part of it.

**Darrell Etherington:** Yeah, it's human.

**Ehtisham Hussain:** But our team and Town's team have had some back and forth. Those are the sections where the mistakes are.

**Jean-Denis Greze:** Yep.

**Jean-Denis Greze:** We'll extract clean and then we'll load it into CSS.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** So just to go back to the caption, whose responsibility is it to make that into like a meta tag or something like that so it doesn't appear?

**Darrell Etherington:** So we will do that.

**Darrell Etherington:** I think, Ehtisham, you can correct me if I'm wrong, but I think this was just how it translated into the new format.

**Ehtisham Hussain:** Yeah, then it started coming in.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** So we'll have to talk to Town's design team to not pull this forward.

**Darrell Etherington:** Yeah.

**Ehtisham Hussain:** Because it's just the alt tag, right?

**Darrell Etherington:** It's what you use for ADA compliance and optimization for assistive technologies and screen readers, but also it has an SEO purpose because that's discoverable.

**Darrell Etherington:** That's something we do—you put in the ADA thing that describes what's going on in the image, and then you put in a little tag that is descriptive of the article to help with SEO and discovery.

**Darrell Etherington:** So that's why. But it's not supposed to be visible unless you're using a screen reader. Whatever was in the alt tag was then translating into image caption in the new interface or publishing format.

**Jean-Denis Greze:** Yeah, it's like a full paragraph tag in HTML right now.

**Darrell Etherington:** It's not in an alt.

**Jean-Denis Greze:** It's not like in the image tag.

**Jean-Denis Greze:** Oh, okay.

**Jean-Denis Greze:** So who, okay.

**Darrell Etherington:** I just want to make sure, what is the concrete next step?

**Darrell Etherington:** You're going to email me?

**Darrell Etherington:** Do you want me to do something?

**Darrell Etherington:** Well, we can talk to your website team, and maybe that's Tony, or?

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** That's fine.

**Jean-Denis Greze:** You can talk to Tony on Slack, and we can go from there.

**Jean-Denis Greze:** So I see, it's in the description, and it's here on the list.

**Ehtisham Hussain:** It's supposed to live in the back.

**Ehtisham Hussain:** Yeah, it's not supposed to be visible on the front end.

**Jean-Denis Greze:** Okay, all right.

**Jean-Denis Greze:** So Tony will do that.

**Jean-Denis Greze:** I had a question about the publishing schedule.

**Jean-Denis Greze:** So if you look at the website, we have eight pieces that were published on July 28th.

**Ehtisham Hussain:** But in fact, they were not all published.

**Jean-Denis Greze:** Yeah, I've moved them.

**Ehtisham Hussain:** Like I initially published them on the 28th, remember, last week.

**Ehtisham Hussain:** And then I moved a few of them back.

**Ehtisham Hussain:** So we only had five for last week.

**Ehtisham Hussain:** And then I moved them back to publishing this week.

**Jean-Denis Greze:** Should we just have them on different dates?

**Jean-Denis Greze:** Like it's just so weird to me that we have this giant batch of things that's all July 28th.

**Darrell Etherington:** You know...

**Darrell Etherington:** Yep, because we talked about staggering over the week, Ehtisham. Maybe that's not yet action, but going forward, I think we'll stagger them like one per day, right?

**Darrell Etherington:** We can backdate these too.

**Jean-Denis Greze:** Yeah, we can do that.

**Jean-Denis Greze:** Yeah, and by the way, the only reason I'm telling you this is that if it were me, I would just change the dates.

**Jean-Denis Greze:** Like, you know, I would have one on the 29th, one on the 30th, one on the 31st, like one on August 2.

**Jean-Denis Greze:** But I'm not doing it because I don't actually feel like I have the agency to do that.

**Jean-Denis Greze:** I don't know what agency I have.

**Jean-Denis Greze:** Like, I'll give you another example. There's some mistakes in some of the posts and right now we're just pointing them out, right?

**Darrell Etherington:** And I think the reason we're doing that is because when I talked to Aida way back, it was important and it remains important.

**Jean-Denis Greze:** Yeah, yeah, yeah, yeah, yeah.

**Jean-Denis Greze:** But there's some content edits we might make on the accuracy of the text stuff, for example.

**Jean-Denis Greze:** If I want to make that change, I'm thinking...

**Jean-Denis Greze:** It's something that I should have caught in the review.

**Jean-Denis Greze:** So it has nothing to do with you.

**Jean-Denis Greze:** Do you want me to go in the CMS and just edit the language?

**Jean-Denis Greze:** Is that okay?

**Jean-Denis Greze:** Or do you prefer for me to do that and then tell you, hey, I caught an error, just FYI, I think it's a typo, so it's not on you?

**Darrell Etherington:** Or do you want me to just tell you when you do it?

**Darrell Etherington:** What's the right way for that? As long as it's not a thing that is happening consistently and you're thinking this looks systemic, then it should be fine for you to make the change.

**Jean-Denis Greze:** That's just yeah.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** Okay, cool.

**Jean-Denis Greze:** And then, okay, those are those, and I think we're back to your agenda.

**Darrell Etherington:** Yes.

**Darrell Etherington:** I think the other thing, actually, well, I don't want to hijack, but I did want to talk about the images, because if you'll notice, we're now just leaving the images for the time being.

**Darrell Etherington:** And I wanted to confirm on your side, like, we're just not publishing images, right?

**Darrell Etherington:** And we're assuming, and this is where I don't want to assume.

**Darrell Etherington:** So how do you want to proceed with the images going forward?

**Darrell Etherington:** Like, do you want us to, I think there was an issue where we didn't initially have editor permissions with the Figma, so I couldn't actually make the change to the graphic document to produce the new titles.

**Darrell Etherington:** But we can happily take that on if that is a thing you would like us to do when you're using this new text-on-graphic format, as opposed to the people image format.

**Jean-Denis Greze:** So we can change the text and add those header images on our side, if you would like to grant us those editor permissions.

**Jean-Denis Greze:** Yeah, so that's what we thought. We thought you were going to work with the Figma and pick a random style every time and just change the text.

**Darrell Etherington:** Happy to do that.

**Darrell Etherington:** Yeah, and I think it was just the technical issue where the pod B account was only authorized as a viewer in the original Figma, which I think we resolved.

**Darrell Etherington:** I have to go check.

**Darrell Etherington:** But I'll just double check if that's resolved and coordinate with your team, and then we can do that going forward. We'll add the text for the images, and I think we can properly judge what to put in for those things. But if we need recalibration, we'll calibrate that going forward.

**Jean-Denis Greze:** Yeah, and if you don't have access, just ask us on the GrowthX side to give you access to it. And then soon, like, in a week or three weeks, we're going to have versions of those that have images. So when you go and choose, you'll have some that are just colors, and then you'll have some with images, and you just pick what you think makes sense.

**Jean-Denis Greze:** Yep, that's great.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** And then once that's more fixed, like, once we're, well, this is our creative style, this is our toolkit, we're in a locked position at least for the quarter or whatever, we can take that back to our tech team and think about integrating it back into the production pipeline, so it's not even a manual process, and it respects all of your design specifics.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** That'd be great.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** Okay.

**Darrell Etherington:** I had a thought.

**Darrell Etherington:** We broke analytics.

**Jean-Denis Greze:** Oh, go ahead.

**Jean-Denis Greze:** We broke analytics.

**Jean-Denis Greze:** So when we moved to the new website, we had the wrong key.

**Jean-Denis Greze:** So I don't have analytics data for a few days, by the way, just letting you know.

**Jean-Denis Greze:** So I don't know if you saw that, but basically the first, the second, the third, and half of yesterday, we had no analytics going.

**Darrell Etherington:** Oh, that sucked.

**Darrell Etherington:** Oh, that was on Google Search Console, probably?

**Jean-Denis Greze:** I'm seeing it on Google Analytics.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Oh, yeah.

**Jean-Denis Greze:** GA4?

**Jean-Denis Greze:** Yeah, yeah.

**Jean-Denis Greze:** Yeah.

**Darrell Etherington:** Okay.

**Jean-Denis Greze:** I haven't looked at the other dashboard, actually.

**Jean-Denis Greze:** And then I did approve.

**Jean-Denis Greze:** Approve.

**Jean-Denis Greze:** There's two blog posts that are approved from me.

**Jean-Denis Greze:** You will see that they have some comments for small changes.

**Jean-Denis Greze:** So in the past when I read something and I was like, it's good to go, but there was like one more change for you, I wasn't approving them.

**Jean-Denis Greze:** I was keeping them in my to-review bucket.

**Jean-Denis Greze:** Now what I'm doing, and I just want to make sure we're all on the same page on this:

**Jean-Denis Greze:** If I read something and I see big mistakes and I feel like my team has to fix things or whatnot, and it's big changes where I want to read the output, I'm putting comments in the doc.

**Jean-Denis Greze:** And then I'm waiting to see that things are addressed.

**Jean-Denis Greze:** And then I'm rereading.

**Jean-Denis Greze:** And then I approve.

**Jean-Denis Greze:** If it's a small change where I'm like, you know, you will do it.

**Jean-Denis Greze:** I just put the comment.

**Jean-Denis Greze:** I'm moving it as ready to publish.

**Jean-Denis Greze:** But I do think that you're taking one quick look to see if there's any comments.

**Darrell Etherington:** That's cool.

**Darrell Etherington:** So before publishing.

**Darrell Etherington:** Is that correct, assumption-wise?

**Darrell Etherington:** Yes.

**Jean-Denis Greze:** Yeah, we're not addressing any comments before proceeding to either re-review or publish.

**Jean-Denis Greze:** OK, cool.

**Ehtisham Hussain:** And if it's just minor stuff, like, should I just make the change on the spot and then reply to the comment and then move ahead with publishing?

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** And if there's some, I'll just make the changes in line, too.

**Jean-Denis Greze:** Like, I'm just still operating in the feedback loop where more feedback is better than no feedback.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** OK, cool.

**Darrell Etherington:** Ehtisham, did you want to talk about the site structure elements at all?

**Darrell Etherington:** Because that was the other thing that we were...

**Ehtisham Hussain:** Yeah, that was the last thing on the agenda for us.

**Ehtisham Hussain:** Like, so we noticed that you moved it from blog to resources instead.

**Ehtisham Hussain:** So right now, the /blog URL, I feel like it should have a redirect, and it should go straight to resources.

**Ehtisham Hussain:** Right now, it's a 404.

**Jean-Denis Greze:** So /blog and /blog.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** Yeah, /blog.

**Ehtisham Hussain:** Because most people, like, if someone were to manually type in your URL, if they were looking for your blog, they would look for /blog.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** Do you wish it were blog instead of resources?

**Ehtisham Hussain:** Personally, I've experimented with this on a couple of websites in the past, and the /resources thing didn't work for me.

**Ehtisham Hussain:** But it's just one small sample size.

**Ehtisham Hussain:** So I just went back to using blog for the websites that I've worked on.

**Jean-Denis Greze:** I see.

**Jean-Denis Greze:** Do you think it matters, or is it a preference thing?

**Jean-Denis Greze:** Do you mean, like, are you recommending that we move it back to /blog, or?

**Ehtisham Hussain:** Well, it's your call.

**Ehtisham Hussain:** You, or it...

**Darrell Etherington:** I think we talked about this earlier too, but I think it's kind of anecdotal and you don't know the sample size, but I think it is impactful how many people will go and literally manually type the URL into the search bar as town.com/blog.

**Darrell Etherington:** Like even speaking as a former journalist, I did that countless times when I was looking for own editorial property, source of truth stuff for a publication, right?

**Darrell Etherington:** So it's like that. I would then go find it cause I'm highly motivated to find it, even if that didn't resolve. But the redirect kind of takes care of that either way.

**Darrell Etherington:** But yeah, I think there's no strong impact either way, but I tend to agree with Ehtisham. My preference would be to go back to the simpler blog folder structure versus resources.

**Darrell Etherington:** And then the opportunity you have there is that in the future, if you're thinking about architecture, you reserve the right to also have resources as a separate folder structure that has more like white paper content or reference content.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** All right.

**Jean-Denis Greze:** Let me talk to Tony about it.

**Jean-Denis Greze:** But we'll do either way. We'll either move it back to blog or we'll have /blog link to /resources.

**Jean-Denis Greze:** If we move it all to blog, do we need to make permalinks for all the /resources/... URLs that have been indexed?

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Either way, you'll have to do the...

**Jean-Denis Greze:** The permalinks, both directions.

**Darrell Etherington:** Permalinks, the reader.

**Jean-Denis Greze:** Yeah.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** All right.

**Jean-Denis Greze:** I'll talk to Tony about it right after this.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** But the good news is you're still very early, so you're not making a huge impact on the footprint of properties.

**Jean-Denis Greze:** No, the impressions have been, you know, going up.

**Darrell Etherington:** That'll be good.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** That's why.

**Jean-Denis Greze:** I did find, I went into GSC just to check if you had that issue for the couple of days, but the GSC is not impacted the same way that Google Analytics is, so it still shows the trajectory. We don't have as much analytics on what happened once people got on the website, but yeah, we still have the impressions and click tracking from the search engine stuff, so that's good.

**Jean-Denis Greze:** Okay.

**Darrell Etherington:** That's great.

**Darrell Etherington:** I think that's all we had to cover this week, but yeah, we can proceed apace, and hopefully we won't have any copy edit errors going forward.

**Jean-Denis Greze:** Yeah, I feel good about it.

**Jean-Denis Greze:** Okay.

**Jean-Denis Greze:** Cool.

**Darrell Etherington:** Thank you.

**Darrell Etherington:** Great.

**Darrell Etherington:** Thanks very much.

**Jean-Denis Greze:** Appreciate it.

**Jean-Denis Greze:** See you around.

**Ehtisham Hussain:** Bye, folks.

**Darrell Etherington:** Bye.

**Darrell Etherington:** Bye-bye.

**Darrell Etherington:** Bye
