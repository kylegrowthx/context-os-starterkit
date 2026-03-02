# Brex <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 20:30 UTC
duration: 31 minutes 59 seconds
organizer: team@growthxlabs.com
participants: Jon Kowieski (Brex), George Haikal (GrowthX), Marcel Santilli (GrowthX), Aida Knezevic (GrowthX), Arudyak (Brex)
fathom_recording_id: 120204946
fathom_url: https://fathom.video/calls/556077750
share_url: https://fathom.video/share/_UrPTKGS6BCwdnWZ3hugg2TrYhmwW-jx
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX presented the Charge Finder tool (approved for development with critical data corrections required) and V1 of the Brex Resources Hub UI, addressing design feedback and establishing implementation patterns for tools, content hubs, and case studies pages.

---

## Context

GrowthX is building a suite of content and visualization tools for Brex to drive traffic and user engagement. Jon raised a critical data quality issue with the Charge Finder tool the day before this meeting: the underlying data contains customer-identifying numbers in charge variations and includes a problematic "customers charged per month" metric that creates legal risk. George confirmed the tool was built programmatically and walked through the full Brex Resources Hub redesign, which consolidates fragmented content into a single navigable hub with tagging, featured sections, and dedicated areas for tools, case studies, and trends. Jon emphasized the need to prepare for internal design review with Bingo (Chief Design Officer), noting that previous redesign attempts were denied and signaling likely pushback on the magnitude of change.

---

## Relevance

**Product & Tools:**
- Charge Finder is a programmatically-built tool with legal compliance requirements that must be vetted before launch
- Resources Hub consolidation addresses fragmented user experience and sets the template for future content organization
- Case Studies page redesign extends beyond this hub—applies to eBooks, blog, and other content pages

**Design & Process:**
- Internal design review with Bingo will likely be contentious given magnitude of redesign and prior denials
- Multiple stakeholders on Jon's team create approval bottlenecks; Jon is actively managing this
- Brex's global navigation strategy needs realignment to remove links to deprecated content (webinars, events)

**Content & Performance:**
- Spend Trends categories should be limited to top performers rather than showing all categories
- Outdated podcast and webinar content should be pruned from featured sections
- Industry filter for Case Studies was a new request from Segment Marketing, not previously planned

---

## Overview

- **Charge Finder Approved:** The tool is approved for development, but with critical data corrections. The team must remove customer-identifying numbers from charge variations and delete the "customers charged per month" metric to avoid legal risks.
- **Resources Hub V1 Reviewed:** The new hub UI was reviewed. Key feedback includes adding "View All" buttons to content sections and preparing for a potentially contentious internal review, as the design represents a major site overhaul.
- **Case Studies Page Redesign:** The current page will be redesigned to fix its poor UX and add a requested "industry" filter, creating a new template for other content pages like eBooks.

---

## Key Topics

### Charge Finder Tool

  - **Status:** Approved for development.
  - **Critical Data Corrections:**
      - Remove customer-identifying numbers from charge variations (e.g., `AMZN MKTPL IND-PRIVIA`).
      - Delete the "customers charged per month" metric.
      - **Rationale:** To avoid legal risks and provide a cleaner, more accurate user experience.
  - **Design Feedback:**
      - Approved the overall design, layout, and "Instantly" orange color.
      - **Suggestion:** For large companies (e.g., Amazon), show only the top 10–20 most common charge variations.
  - **Implementation:**
      - Built programmatically by GrowthX.
      - Will be hosted in the Brex repo, with Kirkland gaining necessary Slack access.
      - [**URL Structure:** `brex.com/tools/charge-finder/[company-name]`](https://fathom.video/share/_UrPTKGS6BCwdnWZ3hugg2TrYhmwW-jx?tab=summary&timestamp=551.0)

### Brex Resources Hub V1 UI Review

  - **Goal:** Consolidate all Brex content into a single, navigable hub.
  - **Key Features:**
      - Breadcrumbs and sticky nav for easy navigation.
      - Content tagged by category, topic, and persona.
      - Sections for featured articles, topics, tools, and trends.
  - **Feedback & Revisions:**
      - **Hero Section:**
          - Reduce font size of "Insights, Tools, and Guides" subtitle.
          - Make article CTAs (e.g., "Read Now") more prominent.
      - **Content Sections:**
          - Add "View All" buttons to each section (e.g., Topics, Tools, Webinars).
          - Increase image size in the "Explore Topics" section.
      - **Content Strategy:**
          - Remove outdated content (e.g., old podcasts, webinars).
          - Add a dedicated "Case Studies" section.
          - Consider limiting "Spend Trends" categories to the top 4 performers.
  - **Internal Review Strategy:**
      - **Challenge:** The hub's design is a major site overhaul and will require approval from the Chief Design Officer (Bingo).
      - **Action:** Jon will prepare for the review by comparing the new design to the current site to justify the changes.

### Case Studies Page Redesign

  - **Problem:** The current case studies page has poor UX and significant white space.
  - **Requirement:** Segment Marketing requested an "industry" filter be added.
  - **Solution:** Redesign the page to fix its UX and add the filter. This new, improved layout will then serve as a template for other content pages (e.g., eBooks, blog).

---

## Decisions & Commitments

- **Charge Finder approved for development** with mandatory data corrections: remove customer identifiers from charge variations and delete "customers charged per month" metric before launch.
- **Resources Hub URL structure confirmed:** `/brex.com/tools/charge-finder/[company-name]`
- **View All buttons** will be added to all content sections (Topics, Tools, Webinars, Podcasts, Case Studies) to improve discoverability.
- **Case Studies page redesign** will serve as the template for other content pages (eBooks, blog).
- **Design review with Bingo** will be necessary before launch; Jon will prepare comparative analysis against current site to justify magnitude of redesign.
- **Global navigation overhaul** proposed to remove webinars/events links and align with Resources Hub structure.

---

## Open Questions

- **Charge variations for large companies:** Should the tool show only top 10–20 variations for companies like Amazon, or should there be a different approach to surfacing hundreds of variations? (Jon considering how to surface patterns without overwhelming users.)
- **Spend Trends categories scope:** Should all categories be displayed, or only the top 4 performers? Jon indicated odds are low for including all categories; needs to decide on final scope.
- **Per diem tool opportunity:** Jon surfaced interest in building a per diem calculator for international (especially Europe/UK) comparisons but noted uncertainty on whether to pursue.
- **Podcast and webinar content:** Should these sections remain in the Resources Hub, given that current podcasts are outdated and the team hasn't produced webinars recently?
- **Article CTA prominence:** Do "Read Now" CTAs need to be more prominent, or do they work as styled buttons alongside the download guide CTA?
- **Design approval timeline:** When will Bingo be available to review, and what is the likely feedback cycle?

---

## Action Items

**George Haikal (GrowthX)**
- Build Charge Finder in Brex repo; exclude customer counts; cap variations; add Google-check; use /tools/charge-finder/vendor
- Build 3rd tool; demo next week to Jon
- Update Resources Hub: smaller subhead; oval CTAs; larger topic images; add 'View all'; add Case Studies; remove old webinars/podcasts
- Fix Case Studies/eBooks: add industry filter; remove large whitespace; align layout
- Propose global nav changes to Jon; remove webinars/events links

**Jon Kowieski (Brex)**
- Decide Spend Trends categories; inform George
- Share Resources Hub/Charge Finder w/ Bingo; include comparison; request feedback

---

## Transcript
**George Haikal:** This meeting is being recorded.

**George Haikal:** Hey, Jon.

**Jon Kowieski:** Yeah, how's it going?

**George Haikal:** Good, man.

**George Haikal:** I think when I, right after I sent you the message about your daughter being sick and you getting over your sickness, I caught something like within an hour after.

**George Haikal:** It bizarre.

**George Haikal:** So a bit under the weather, so just, you know, excuse my voice for this meeting.

**Jon Kowieski:** Oh, no worries.

**Jon Kowieski:** I mean, when someone's coughing in your face and they're sick, you're, like, I'm not that bad compared to last week.

**Jon Kowieski:** She was, like, often herself awake at, like, four or five in the morning for, like, three straight days, which then she is just, like, up.

**Jon Kowieski:** And I was, like, oh, I'd love to sleep.

**Jon Kowieski:** Like, please.

**Jon Kowieski:** Yeah.

**George Haikal:** Yeah, no, that's brutal.

**George Haikal:** How's everything going?

**Jon Kowieski:** It's good.

**Jon Kowieski:** It's super busy.

**Jon Kowieski:** We are cranking out content right now and publishing at a pretty fast rate, probably one to two a day.

**Jon Kowieski:** So that's where I saw what you created.

**Jon Kowieski:** That looks really good.

**Jon Kowieski:** And then I spoke with someone on my team yesterday, and he made me aware that, like, some of the statement, ChargeFinder data might not be right or something like that.

**Jon Kowieski:** So I was like, oh, great.

**Jon Kowieski:** Didn't know that the quality of that data might not be the greatest.

**Jon Kowieski:** I was like, thank you for making me aware of that, because we're going to have to probably go through and, like, look at the most common, what is it, charges or how they normally are.

**George Haikal:** Yep.

**Jon Kowieski:** So that's, like, one thing I realized yesterday.

**Jon Kowieski:** was like.

**Jon Kowieski:** I would have assumed that the statement charges are pretty normal and that he made me aware the numbers at the end of most of them are actually like company identifiers.

**Jon Kowieski:** So we even went through that ramp example and he's like, yeah, we should not do anything like that or even say how many we're doing per month, which we don't know how many we're doing per month anyway.

**Jon Kowieski:** So that was something I was not aware of until yesterday.

**George Haikal:** Okay.

**Jon Kowieski:** So that's just something to keep in mind for that.

**Jon Kowieski:** And then, yeah, we'll be out next week.

**Jon Kowieski:** So I thought this looked really good.

**Jon Kowieski:** didn't like the orange on the instantly.

**Jon Kowieski:** I thought that was really nice because it will definitely pop.

**George Haikal:** Yeah.

**George Haikal:** The different categories are here.

**George Haikal:** Um, what I really like is...

**George Haikal:** is...

**George Haikal:** This page, right, you have the statement variations, you have the about, call to action, and then the what is section, right, then how to actually contact ADT, and then a login as well.

**George Haikal:** And then where the company's founded, the category that we bucketed in, when it was founded.

**George Haikal:** So we added a few different things that I think are going to be valuable to anyone hitting this site.

**Jon Kowieski:** Absolutely.

**George Haikal:** And we built it out programmatically.

**Jon Kowieski:** Oh, that's awesome.

**Jon Kowieski:** Yeah, I like everything I'm seeing here, just as long as we're, yeah, we're not even seeing it, so.

**George Haikal:** Saying what?

**Jon Kowieski:** How many people are being charged this at Brex?

**Jon Kowieski:** How many Brex customers are being charged this?

**Jon Kowieski:** Yeah, I realized that that was on the rampage, and that was like a big no-no, and I was like.

**Jon Kowieski:** Oh, gosh.

**Jon Kowieski:** I better make sure that's not on ours because there's some legal stuff that we might have to go through with something like that.

**Jon Kowieski:** So that was interesting to find out.

**George Haikal:** Yeah.

**George Haikal:** Is there anything?

**George Haikal:** mean, this looks great.

**George Haikal:** We're already working on the next tool as well.

**George Haikal:** Kirkland is now getting like the final access in some of your private Slack channels to run some different commands.

**George Haikal:** So we will build this out in your repo directly.

**George Haikal:** Are there any things you'd like to see, any design changes you made, would love just to get your sign-off overall on?

**Jon Kowieski:** I think I'm way good with what you have, actually.

**Jon Kowieski:** The one thing I was thinking through was, maybe it's already on here.

**Jon Kowieski:** There's so many different Amazon, like certain larger companies have so many different charges.

**Jon Kowieski:** That was something I didn't think through until yesterday.

**Jon Kowieski:** So.

**Jon Kowieski:** So that was just one fun thing to think about.

**George Haikal:** Like the same variations is what you're referring to?

**Jon Kowieski:** Yeah.

**George Haikal:** Like, for example, India, Privia, like, what does that mean?

**Jon Kowieski:** It's probably normally just Amazon Pay or Amazon Pay.

**Jon Kowieski:** And I was like, oh, gosh, is there a way to, like, actually Google stuff like this outside of just this to make sure it's, like, accurate?

**Jon Kowieski:** So that was a fun thing.

**Jon Kowieski:** And, yeah, those are, like, the identifiers, I guess, where, like, the average customer is not going to be – Doesn't need the identifiers at the end of Marketplace.

**Jon Kowieski:** Yeah, what it's really going to be is likely that Amazon, M-K-T-P-L.

**George Haikal:** P-L, or, and then this variation with the full spelling.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** And I was like, how do we do that?

**Jon Kowieski:** Or do we do, like, the top ten in theory?

**Jon Kowieski:** Or the top 20.

**Jon Kowieski:** I'm still trying to think through this.

**Jon Kowieski:** So that was just one thing.

**George Haikal:** That's helpful.

**Jon Kowieski:** I think that was about...

**George Haikal:** Looks great, though, doesn't it?

**Jon Kowieski:** Yeah, it does.

**Jon Kowieski:** And other people actually liked it as well.

**Jon Kowieski:** So the categories, I think, were good.

**Jon Kowieski:** I don't think I had anything with those.

**Jon Kowieski:** So, yeah, everything looks good to me.

**Jon Kowieski:** And I think it's like, yeah, it's alphabetical.

**Jon Kowieski:** So, yeah, everything makes a lot of sense.

**Jon Kowieski:** But, yeah, it was just that small comment.

**Jon Kowieski:** And I didn't realize it.

**George Haikal:** Yeah, so it's essentially never saying the number of Brex customers that are actually getting transactions.

**Jon Kowieski:** That and not showing also like a hundred.

**George Haikal:** Different variations.

**George Haikal:** Yeah, yeah, yeah.

**Jon Kowieski:** It's more or less if this is the pattern.

**Jon Kowieski:** And I was trying to think through how do we put that on the page.

**Jon Kowieski:** Like if it starts with this, it's most likely Amazon Marketplace because technically if someone actually Googles what theirs is, it probably should not be showing up.

**George Haikal:** Yeah, I agree with you.

**Jon Kowieski:** Yeah, so, but this is stuff I had no idea about.

**George Haikal:** I'm just making it here a second.

**Jon Kowieski:** And he was also telling me, like per diem in Europe, which I never plan on doing anyway, is like one of the things that we might have an edge on with.

**Jon Kowieski:** And I was like, I don't, I don't know if I want to touch that in a Purdue and Calculator.

**Jon Kowieski:** you.

**Jon Kowieski:** much.

**Jon Kowieski:** But the ability to show like a per diem for like a per diem for potentially someone that's in like the UK or someone in Europe in comparison to like the US.

**Jon Kowieski:** So I don't know about that, though.

**Jon Kowieski:** So I'm trying to think through it.

**Jon Kowieski:** But yeah, that was just another thing that came up yesterday.

**Jon Kowieski:** So we'll see how that goes.

**George Haikal:** Okay.

**George Haikal:** Yeah, we need a little more information there.

**George Haikal:** It's something that we want to explore.

**George Haikal:** But for now, I'll consider this good to go and I'll let the team sprint on actually getting it built.

**George Haikal:** And your repo will follow all these design elements as well for the other tools.

**George Haikal:** The tools.

**George Haikal:** The

**George Haikal:** will look unique and different as well.

**George Haikal:** And you'll interact, the user will interact with them differently as well on the page.

**George Haikal:** But like overall brand and style, I feel like we hit the mark here if I'm hearing it right.

**Jon Kowieski:** And so we'll follow similar.

**Jon Kowieski:** And then the URL structure would be like Brex.com slash tools slash charge finder and then slash would it be like, let's just say Amazon, Amazon or Uber.

**Jon Kowieski:** Would that be how that goes?

**George Haikal:** Yes.

**Jon Kowieski:** Can you look at that?

**George Haikal:** Yeah.

**George Haikal:** Okay, perfect.

**George Haikal:** That's just one of those things.

**George Haikal:** Yeah.

**George Haikal:** There's a question there, which is actually like a perfect segue.

**George Haikal:** So tools we're running on the next couple as well.

**George Haikal:** And so next week, I'll be able to show you those.

**George Haikal:** Super exciting.

**George Haikal:** The second is the resources hub.

**George Haikal:** So like connecting the entire Brex experience, right?

**George Haikal:** And optimizing it.

**George Haikal:** I wanted to show you a V1 of the UI that we built out for the Brex Resources Hub.

**George Haikal:** Key things to note, and again, open to feedback, right?

**George Haikal:** But breadcrumbing here on the left, the sticky nav here on the right.

**George Haikal:** We just kept the global nav for now because that was just in the original mockup, but we can adjust it as well.

**George Haikal:** But there's the big hero here, and then it's pulling in the featured and then different highlighted types of content.

**George Haikal:** And you can see what we added were the categories, but also different tags.

**George Haikal:** So persona-level tags as well as category-level tags, and you can have as many as you want.

**George Haikal:** Then there's an author, a date, a read, and then below here, we broke everything out into topics.

**George Haikal:** These images are placeholders, right, but we pulled them from your site.

**George Haikal:** But then you're able to click into each one of these topics, and it will be its own hub.

**George Haikal:** So around that topic as well.

**George Haikal:** expense management, financial planning, travel and spend, et cetera.

**George Haikal:** And you scroll down and the indexes will be here as well.

**George Haikal:** Right.

**George Haikal:** There's a section for tools here.

**Jon Kowieski:** And then.

**Jon Kowieski:** At least three tools before we can add it.

**Jon Kowieski:** There's only two.

**George Haikal:** Well, we can get you three tools.

**George Haikal:** I mean, you already had the mileage reimbursement.

**George Haikal:** I mean, we'll have three tools up by next week, easily.

**George Haikal:** Okay.

**George Haikal:** Pulling in trending and popular articles from this week.

**George Haikal:** Again, the tagging system here is huge is bringing everything together.

**George Haikal:** And then we're calling out spend trends specifically here as well.

**George Haikal:** Pulling in top articles there.

**George Haikal:** And again, just, then it just goes by topic category.

**George Haikal:** So the idea here is let's tag everything to make it easily navigable and searchable and also within one click.

**George Haikal:** Right.

**George Haikal:** And so,

**George Haikal:** Someone could come in and this is the experience that they get.

**George Haikal:** We can pull in any other types of content, but we wanted to lead with the most relevant, most valuable, and most recent.

**George Haikal:** So things like the podcasts were a little outdated, so we haven't included them here, but we're happy to.

**George Haikal:** If that's something that you want to do.

**George Haikal:** The next thing I want to share is this article section that we built out here that's always available through the StickyNav.

**George Haikal:** And again, everything's just coming off of slash resources here.

**George Haikal:** All the topics are broken out here.

**George Haikal:** Same thing with the roles as well.

**George Haikal:** fix a bit of the stickiness in the navigation and the UI.

**George Haikal:** Whether you're able to click into any role or anything that's tagged across, agnostic of topic or type will show up for this tag.

**George Haikal:** And so we've done that on the category level as well as the topic level.

**George Haikal:** And then when you click into each.

**George Haikal:** in the chat, And And

**George Haikal:** This you have the topic, which is navigable.

**George Haikal:** this isn't built out yet, right?

**George Haikal:** But it will be clickable and navigable.

**George Haikal:** Obviously, the title, the image, scroll through.

**George Haikal:** It looks beautiful.

**George Haikal:** This really pops.

**George Haikal:** I love how these quotes kind of hit.

**George Haikal:** And then down at the bottom is what I want to show you.

**George Haikal:** So you have the FAQs like you normally do.

**George Haikal:** just feels very clean.

**George Haikal:** Very nice experience.

**George Haikal:** Again, have the table of contents here.

**George Haikal:** And then you have the topics that you can bounce back into after you're done reading the article if you're interested.

**George Haikal:** And then you have related articles as well.

**George Haikal:** These images will replace, obviously, to make them beautiful.

**George Haikal:** But then you have related articles to this topic type for the reader to go and click through.

**George Haikal:** And then the CTA down at the bottom.

**George Haikal:** And then

**George Haikal:** That was a lot.

**George Haikal:** So your, excuse me, thoughts, feedback?

**Jon Kowieski:** Yeah, you want to go back to the resource hub page first, and then we can go through all three.

**George Haikal:** The top here.

**George Haikal:** I don't want to give you the spins by scrolling too fast.

**Jon Kowieski:** Yeah, so if you have an example of a similar website that has something like this, that will help right away, I'll tell you that.

**Jon Kowieski:** There seem to be a lot of comparisons when we do designs for some reason, but I like the design of this.

**Jon Kowieski:** The only thing about the title, if you scroll up, I'm kind of thinking the font size of Insights, Tools, and Guides might need to be a little bit smaller than the actual Brex Resources Hub text.

**Jon Kowieski:** And I'm only thinking about, like, I'd have to go through, like, even the page I gave you that got denied, essentially, like, April of last year.

**Jon Kowieski:** Mm-hmm.

**Jon Kowieski:** Because they might prefer, I don't even know if they will want the insights, tools, and guides for modern finance team.

**Jon Kowieski:** And I'll just have to think through that.

**Jon Kowieski:** But that is probably one thing I think that sticks out for me.

**Jon Kowieski:** There will be, there will absolutely be notes from that team.

**Jon Kowieski:** So, but that's just one thing I'm thinking off the top of my head.

**Jon Kowieski:** So, you scroll down, I think this looks good.

**Jon Kowieski:** It just may.

**George Haikal:** I kind of want these to pop a little more.

**Jon Kowieski:** Yeah.

**George Haikal:** These, almost like this download guide button, right?

**George Haikal:** We can keep the colors, but we can make it highlighted and oval around.

**George Haikal:** I want to experiment with that.

**George Haikal:** What were your thoughts there?

**George Haikal:** Little things.

**Jon Kowieski:** I I'm literally doing a comparison as to what exists now versus those.

**Jon Kowieski:** I do like the style of this.

**Jon Kowieski:** It doesn't really matter sometimes what I like though.

**Jon Kowieski:** I guess when I'm looking at it, like, yes, you got a download guide CTA, but for the other ones, you don't technically have a CTA.

**Jon Kowieski:** Like, read now, I think they're probably fine as is, but keep in mind that maybe a comment that comes up for this design.

**George Haikal:** Got it.

**George Haikal:** Well, I'm just going to pull up my notes on my second screen so I can type them as you go.

**Jon Kowieski:** So, yeah, more and stuff.

**George Haikal:** Yep.

**Jon Kowieski:** If we're up to something similar to this, it might be easier for me to highlight that during the comparison.

**Jon Kowieski:** Hey, you should look at this.

**Jon Kowieski:** As crazy as that sounds, like, sometimes it helps me get things across the line.

**Jon Kowieski:** But, yeah, then scrolling down.

**Jon Kowieski:** Scroll down.

**Jon Kowieski:** I like this.

**Jon Kowieski:** Explore topics.

**Jon Kowieski:** Explore

**Jon Kowieski:** So I have no issues with that.

**Jon Kowieski:** Little images, maybe they need to be just a little bit bigger because there's a bunch of white space, I guess.

**Jon Kowieski:** That would be my only comment, but I'm actually fine as is anyway.

**Jon Kowieski:** At the end of the day, I got a feeling that amount of notes they'll hand over to me that I'll hand over to you will probably be what we'd need to do.

**Jon Kowieski:** And then going down, I like what you have for the index.

**Jon Kowieski:** I'm just thinking through how it'll look.

**Jon Kowieski:** And I don't know.

**Jon Kowieski:** I'd be super curious if there was like some kind of CTA if that led to people clicking, but I'm fine with this.

**Jon Kowieski:** I don't know for the index if we want to have a view all button to the right or something like that of, yeah, to the right of that or somewhere, all the way to the right.

**Jon Kowieski:** Like I'm doing a comparison of your page.

**Jon Kowieski:** I know we don't on our site, but we have a see all button.

**Jon Kowieski:** My guess is they're going to want something view all, see all somewhere in these sections.

**George Haikal:** Okay.

**Jon Kowieski:** So that would probably be one thing to just be prepared for, I guess.

**Jon Kowieski:** And then I think just going down, it's probably like the same for each one.

**George Haikal:** Yeah, we can add a view all button.

**Jon Kowieski:** Yeah, my guess is that will be what they want.

**George Haikal:** Yeah, no problem.

**George Haikal:** Oh.

**George Haikal:** All right, let me get this over here.

**George Haikal:** Okay.

**George Haikal:** I'm super excited for these tools.

**George Haikal:** I'm super excited.

**Jon Kowieski:** These are good, I guess.

**Jon Kowieski:** Yeah, just, well, they'll probably have more color to them, but I'm just thinking like too much white.

**Jon Kowieski:** White space, but maybe that's how we have it on our website.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** We do, I guess.

**George Haikal:** Yeah, we'll make these better because like if you look at the charge finder, right, we can add a little more color to this gradient, at least in the thumbnail.

**George Haikal:** But even the gradient itself will pop more.

**George Haikal:** So it's not white on white when it's the actual tool and the preview of the actual individual tool itself.

**Jon Kowieski:** Ah, that's helpful to know, actually.

**Jon Kowieski:** And I would make that clearer if I share this or when I share this.

**Jon Kowieski:** So, but yeah, and then I don't think there's anything crazy that gives you scroll down.

**Jon Kowieski:** I'm a big fan of EAT, but the author of most of our pages would be me.

**George Haikal:** Yeah, I know.

**George Haikal:** You just get a constant shout out.

**Jon Kowieski:** So for these, yeah, this makes sense.

**Jon Kowieski:** And I guess the question would be like, are we manually putting the most part?

**Jon Kowieski:** Popular or just the newest, I guess?

**Jon Kowieski:** The newest articles or how is that working?

**George Haikal:** We can think through it.

**George Haikal:** mean, what I want to do is highlight the best performing, right?

**George Haikal:** And have it easily accessible, the best performing.

**George Haikal:** But we're able to do anything.

**Jon Kowieski:** Change it.

**George Haikal:** Okay.

**Jon Kowieski:** So that might be a little bit of a manual thing.

**Jon Kowieski:** I'm just thinking through it.

**Jon Kowieski:** Good with this.

**Jon Kowieski:** I feel like I'm probably good with, as you scroll down, probably a lot.

**Jon Kowieski:** Yeah, that makes sense.

**Jon Kowieski:** Same thing.

**Jon Kowieski:** Spend trends.

**Jon Kowieski:** Expense management.

**Jon Kowieski:** Oh, you're doing the categories.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** It's so funny how my newest image just sticks out like a sore thumb with me.

**Jon Kowieski:** Oh, gosh.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** But, yeah, this looks good.

**Jon Kowieski:** go, Thank you.

**Jon Kowieski:** I'm with this.

**Jon Kowieski:** mean, these are all, like, the same.

**Jon Kowieski:** So I don't see anything wrong with these at all.

**Jon Kowieski:** You can keep scrolling through the whole...

**Jon Kowieski:** I guess this will have to think through.

**Jon Kowieski:** And then, is the thought to put every spend trends category?

**Jon Kowieski:** Because I realize this is only a few.

**George Haikal:** On this page?

**Jon Kowieski:** Yeah, have, like, corporate cards, business banking.

**George Haikal:** Yeah, we can break down every category.

**Jon Kowieski:** Like, we would have to think through that, and I'll let you know that.

**Jon Kowieski:** Like, certain categories don't do as much for us.

**Jon Kowieski:** And that's more or less because, like, accounting, for example, good example, like, doesn't do as much as our credit card category, for example.

**George Haikal:** Mm-hmm.

**Jon Kowieski:** Certain categories are more important to us than others.

**Jon Kowieski:** Mm-hmm.

**Jon Kowieski:** So if we only had to put four, that's how I'd do it.

**Jon Kowieski:** don't, odds of us being able to put the categories on there, be prepared for this, is probably low.

**Jon Kowieski:** So, and I shared my example with you that we came up with, even though it's most of the content on this website.

**Jon Kowieski:** Absolutely.

**Jon Kowieski:** So, yeah, just be prepared to have to scrape that, guess, like each category, but leave this spend transaction that you have right now.

**Jon Kowieski:** So I'll try to fight tooth and nail for this at the very least.

**Jon Kowieski:** I would love to have each category on there.

**Jon Kowieski:** I just got a sneaking feeling having been through so many different reviews, what it will be like.

**George Haikal:** Yeah, you definitely know, you know better than me.

**George Haikal:** It's helpful.

**Jon Kowieski:** And then going all the way down.

**Jon Kowieski:** Yeah, the podcasts are all super old.

**George Haikal:** Yeah.

**Jon Kowieski:** I don't.

**Jon Kowieski:** It doesn't make sense to mention on the quote.

**Jon Kowieski:** Yeah, I like it.

**Jon Kowieski:** We'll see what they say.

**Jon Kowieski:** If that is mimicking like what we have on the website, it should be like completely fine.

**Jon Kowieski:** I don't see why it wouldn't be.

**Jon Kowieski:** And then webinars, same all, like view all or whatever webinars.

**George Haikal:** Yeah, we'll add a view all to each one of these sections.

**Jon Kowieski:** Granted, as I'm looking at these webinars, they're all very old.

**Jon Kowieski:** I don't know the last time we did a webinar.

**George Haikal:** So the reason I included these is because, and we're not married to it, right?

**George Haikal:** But when you, sorry, when you go to your slash resources, it is now.

**Jon Kowieski:** Yeah, they got some old stuff on there now.

**George Haikal:** Yeah.

**Jon Kowieski:** stuff.

**George Haikal:** I mean, look at just, yeah, even just comparing like the initial experience overall.

**George Haikal:** But if I remember correctly, webinars was pretty high up.

**George Haikal:** And so not necessary at all.

**George Haikal:** Especially because they're a little outdated, so we can choose to prune.

**Jon Kowieski:** Case studies, I think they'll want on this page, something like this.

**Jon Kowieski:** So keep that in mind.

**George Haikal:** Yeah.

**Jon Kowieski:** I already know.

**Jon Kowieski:** Yeah, we'll have a case studies.

**Jon Kowieski:** Yeah, talking to someone today about case studies, and there's probably someone else on my team, but there's a feature they want on the case study page for the filter.

**Jon Kowieski:** Search by industry.

**Jon Kowieski:** So this is the page.

**Jon Kowieski:** If you go to like, what is the filter?

**Jon Kowieski:** Yeah, they want to add an industry to this.

**Jon Kowieski:** This is not a great case.

**George Haikal:** This is not good at all.

**George Haikal:** I mean, yeah, like the tags should be here by all three of these different types, topic, segment, and industry.

**Jon Kowieski:** Yeah, I personally hate this page.

**George Haikal:** Um, we can make this better though.

**George Haikal:** We can make this better.

**George Haikal:** We can make, we can definitely.

**Jon Kowieski:** So was just one thing.

**Jon Kowieski:** So, yeah, I don't understand this huge white space, right?

**Jon Kowieski:** Where actually you were, right?

**Jon Kowieski:** Like, what is this?

**Jon Kowieski:** Right where your mouse is.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** What is going on there?

**Jon Kowieski:** Like, like, if you know how people actually look at websites and read side to side, that makes zero sense.

**George Haikal:** Totally.

**Jon Kowieski:** But, I might need approval before you, I don't know.

**Jon Kowieski:** I just think that looks goofier than all.

**Jon Kowieski:** I probably would have to prove it with like some kind of UX.

**Jon Kowieski:** But the filter was a today request from segment marketing.

**Jon Kowieski:** Gosh, all these, even the eBooks page, that's like basically the same layout.

**George Haikal:** Yeah, we can go ahead and fix that once Kirk gets access.

**George Haikal:** Nope, that's no issue.

**Jon Kowieski:** So the layout that you would design for this, we probably would want to design across like the eBooks page across, or I mean the main eBooks page, the main web, we would probably have to do it across all of those.

**Jon Kowieski:** Which is annoying.

**Jon Kowieski:** The Brex blog page actually needs a filter by industry, but I don't know.

**Jon Kowieski:** They don't, probably don't take any of it.

**Jon Kowieski:** So I would keep in mind the design.

**Jon Kowieski:** If you've seen the new images, my design team...

**Jon Kowieski:** has been making in articles, like the newest blog articles, it's almost a different design.

**Jon Kowieski:** So if you did slash journal, it does not mesh.

**Jon Kowieski:** It's like they had a kind of grayness.

**Jon Kowieski:** So if you scroll down, you kind of begin to see it across like multiple new articles.

**Jon Kowieski:** Probably the one that's weird is like, you keep scrolling, because these are logos.

**Jon Kowieski:** The cash one right there is like the style that I've been seeing on like LinkedIn ads and things like that.

**Jon Kowieski:** It's, yeah, very much AI.

**Jon Kowieski:** When you look at that, you're like, yeah, it's AI.

**George Haikal:** 100%.

**Jon Kowieski:** So hopefully we're fine.

**Jon Kowieski:** Sometimes they're actually using images I make.

**Jon Kowieski:** Good journey.

**Jon Kowieski:** Well, yeah, that should be good.

**Jon Kowieski:** And I hope they approve it.

**Jon Kowieski:** So it makes a lot of sense to me.

**Jon Kowieski:** And probably – and we're actually linking, when you click on the resources nav, to, like, the webinars page when we don't do webinars, to the events page when we're No, yeah, we're going to wreck them.

**George Haikal:** So we're going to – so this is what I want to talk to you about as well, the global nav.

**George Haikal:** We're going to recommend just, like, best practice here or, like, where – what we think it should look like as well.

**Jon Kowieski:** Yeah, and sadly, I've only been able to give advice on the global nav, and most of it never gets followed.

**Jon Kowieski:** So I fight tooth and nail for the footer.

**Jon Kowieski:** Yeah.

**George Haikal:** Yeah.

**Jon Kowieski:** Yeah, there's a lot of things that don't make sense.

**Jon Kowieski:** Like,

**Jon Kowieski:** Why is customer stories under, oh, that's weird.

**Jon Kowieski:** We have a customers tab and then a customer stories tab in resources, but it's very confusing.

**Jon Kowieski:** So, but I do need a hot, but yeah, the charge finder looked good.

**Jon Kowieski:** I'm just being prepared for, there'll be a lot of comments.

**Jon Kowieski:** That's how they do these reviews with design.

**Jon Kowieski:** The one thing I'm going to try to do is make sure there's not too many cooks in the kitchen because they all have these different recipes and then it turns into a conflict that takes too much time.

**George Haikal:** Yeah.

**Jon Kowieski:** And it is one of the number one reasons why we move so slow.

**Jon Kowieski:** It's like, oh, we should do this.

**Jon Kowieski:** Oh, we should do that.

**Jon Kowieski:** Oh, I came up with four designs for this.

**Jon Kowieski:** Guys, we just need to come together and decide like what we need.

**Jon Kowieski:** So, we have a lot.

**Jon Kowieski:** lot of creative directors here.

**George Haikal:** Got it.

**George Haikal:** Yeah, I would love if you could help us streamline that.

**George Haikal:** And as you can see, we can move super fast on any of this and hit a really high quality.

**Jon Kowieski:** So, like the tools pages and stuff like that, I don't necessarily need as much approval.

**George Haikal:** Like the spend trends, stuff like that, don't get the resources up.

**Jon Kowieski:** Because it's a main page, I need that approval.

**Jon Kowieski:** So, it's one of the reasons why we move super, super quick.

**Jon Kowieski:** But, yeah, they may want to see these layouts, and I will have to share them to at least Bingo.

**Jon Kowieski:** He's the chief design officer, by the way.

**Jon Kowieski:** So, at the end of the day, he does have final call.

**George Haikal:** Yeah.

**Jon Kowieski:** I need to hop in and get to another meeting.

**George Haikal:** If you have anything else, just feel free to Slack me.

**George Haikal:** Thank you, sir.

**George Haikal:** Great progress.

**George Haikal:** I appreciate you.

**George Haikal:** Talk soon.

**George Haikal:** Awesome.

**George Haikal:** Thank you.

**George Haikal:** Bye.

**George Haikal:** Bye.

**George Haikal:** Bye.

**George Haikal:** Bye.

**George Haikal:** Bye.
