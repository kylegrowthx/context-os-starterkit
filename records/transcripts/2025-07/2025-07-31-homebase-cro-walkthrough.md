# Homebase CRO walkthrough

<metadata>
date: 2025-07-31
time: 15:01 UTC
duration: 30 minutes
organizer: jakub@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Jess Scott (GrowthX), Philip Siu (Homebase), Zeeshan Habib (Homebase)
fathom_recording_id: 77701259
fathom_url: https://fathom.video/calls/367360225
share_url: https://fathom.video/share/ixtizgRXYZLRBKPoSNPcyEzuVj7CQi7j
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Jakub Rudnik, newly promoted Managing Director on the Homebase account, walked through Homebase's conversion analytics infrastructure with Philip Siu (Website Growth Lead) and Zeeshan Habib (Analytics). Homebase prioritizes sign-ups (free account creation) as the primary conversion metric, with 500k blog visitors driving only 0.3% sign-ups, and Philip shared two dashboards: a high-level Looker dashboard segmented by funnel stage and marketing channel, plus Amplitude for URL-level conversion analysis. GrowthX and Homebase committed to a 12-month Amplitude export, Databricks dashboard screenshots, and exploration of Webflow API integration for auto-publishing, with potential additional customization and cost analysis needed.

---

## Context

Homebase is a workforce management SaaS platform founded to streamline scheduling, payroll, and team communication for small businesses. GrowthX has been creating 30-50 pieces of blog and related content monthly for Homebase over a long period and holds a large role in their content strategy. Jakub Rudnik recently joined as Managing Director on the account (less than two months at the time of this call) and was brought in to add deeper, more strategic account management than the previous model allowed. This meeting was triggered by Jakub's need to understand Homebase's conversion funnel—specifically which content and site sections drive revenue—so he can identify patterns and replicate success across future content initiatives. Philip Siu manages the entire website function including experimentation and CRO, and Zeeshan Habib provides analytics and insights aligned with the growth team.

---

## Relevance

**To GrowthX Delivery:**
- Homebase's conversion funnel is sophisticated: sign-ups (account creation) are the primary metric, followed by paying locations as the true North Star. Understanding this multi-step PLG motion is critical for content strategy going forward.
- Blog performance is surprisingly low relative to other site sections (0.3% sign-up rate from 500k visitors). This signals opportunity to identify which content topics convert best (top performers: free payroll software, scheduling, small business payday content) and replicate those patterns.
- Webflow migration in September impacted URL structure and data consistency — any historical analysis should account for this date as a break point. GrowthX may face similar technical issues with other Webflow clients.
- Amplitude provides powerful URL-level funnel analysis and CSV export capabilities. GrowthX should explore Amplitude integrations for other clients requiring granular content performance data.

**To GrowthX Business Development:**
- API integration project creates expansion opportunity: Homebase is interested in GrowthX building auto-publishing bridges from GrowthX's internal tools to Webflow. This represents a potential services add-on beyond content creation.
- Jakub's explicit interest in replicating content patterns and running experimentation suggests account growth potential if GrowthX can deliver on CRO recommendations and site-wide optimization ideas beyond the blog.
- Homebase has mature analytics infrastructure and data access — relationship opportunity to deepen if GrowthX can leverage these insights to drive measurable ROI on content investments.

**To CheckThat:**
- Homebase's use of Amplitude for product analytics suggests potential CheckThat use case: AI visibility into how SaaS site content performs across the funnel, especially valuable for PLG companies optimizing sign-up flows.

---

## Overview

- Homebase prioritizes sign-ups (account creation) as the primary conversion metric, with paid conversions as the ultimate goal
- Blog content drives \~0.3% sign-up rate, lower than other site sections
- Amplitude provides granular conversion data by URL, but external access is limited
- Recent migration to Webflow impacts data consistency before September

---

## Key Topics

### Conversion Metrics and Attribution

  - Primary conversion events:
      - Sign-ups (account creation) - heavily prioritized
      - Paid conversions (paying locations) - North Star metric
      - Contact sales form submissions - secondary focus
  - Attribution model favors last touch, with higher weighting for paid channels
  - Full customer journey data available, but not easily accessible

### Analytics Dashboards and Tools

  - Marketing website dashboard in Looker:
      - Segments traffic by funnel stage (ToFu, MoFu, BoFu)
      - Groups by marketing channel and page type
      - Tracks sign-ups, sign-up rate, and web engagement rate
  - Amplitude for granular URL-level conversion data:
      - Can create custom funnels (e.g., blog visit → sign-up flow → conversion)
      - Allows for time-based analysis and CSV export

### Blog Performance Insights

  - \~500,000 blog visitors in last 6 months
  - 1.26% entered sign-up flow, 0.3% completed sign-up
  - Top converting blog posts include topics like free payroll software and scheduling
  - Blog conversions are lower compared to core site sections

### Potential Content Performance Metrics

  - Web engagement rate: visitors viewing 2+ pages (3x more likely to convert)
  - Sign-up flow entries: larger sample size than completed sign-ups
  - Core page visits from blog: indicator of interest in product pages

### Technical Considerations

  - Webflow migration in September affected URL structures and data consistency
  - API access for auto-publishing content to be explored

---

## Action Items

**Philip Siu (Homebase)**
- Pull & share 12-month Amplitude data with metrics: blog performance, sign-ups, sign-up flow entries, core page visits from blog

- Screenshot Databricks dashboard showing organic traffic and site section performance (highest-level view for pattern identification)

- Investigate Webflow API key access requirements for GrowthX auto-publishing integration


**Jakub Rudnik (GrowthX)**
- Send Webflow API key request instructions and customization requirements documentation to Philip Siu

- Confirm potential additional Webflow costs associated with API integration and report back to Philip Siu

---

## Transcript

**Jakub Rudnik:** From home and all sorts of hours, so.

**Philip Siu:** Very cool, very cool.

**Philip Siu:** I worked with Kyle before, I think, I'm not sure if you guys know, like, Kyle came from Homebase, and I was reporting to him.

**Philip Siu:** I actually just caught up with him last Friday, so I heard about, like, you guys growing a lot, but yeah, that's cool.

**Jakub Rudnik:** Yeah, Kyle, we both worked with him pretty closely, just before, like, before I came in, honestly, like, we had no managing directors, that's my title.

**Jakub Rudnik:** And Kyle was, like, doing that for every account, which is absolutely bonkers in hindsight.

**Jakub Rudnik:** Like, I saw his schedule when I came in, it was just, like, meeting, meeting, meeting, meeting, meeting, getting 20 accounts at once, just impossible type of stuff.

**Jakub Rudnik:** And so then they brought in a layer of, like, folks like myself to do some, like, to try to do what Kyle was doing, but with more depth to fewer clients.

**Jakub Rudnik:** And then, yeah, but Jess, you worked with him, you worked with him on a few accounts, right, really close to, like, seat and stuff.

**Jakub Rudnik:** So, yeah, he was great.

**Jakub Rudnik:** I finally met him in person when I was in San Francisco.

**Jakub Rudnik:** Go for a week, so, but it seems super smart.

**Philip Siu:** Yeah, it's amazing.

**Philip Siu:** Yeah.

**Philip Siu:** It's taller than I expected.

**Jess Scott:** Definitely.

**Jakub Rudnik:** Well, thank you for taking some time.

**Jakub Rudnik:** Appreciate it, especially with, like, a little bit of an agenda, but it's certainly kind of loose.

**Jakub Rudnik:** I can give a little background on what we're looking for and then how that was set up and then you can go from there.

**Jakub Rudnik:** But, you know, so we're creating mostly blog and related content for Homebase.

**Jakub Rudnik:** Ends up being, like, somewhere in the 30 to 50 pieces a month that we've been doing this for, you know, a long time at this point.

**Jakub Rudnik:** And we're not the only ones touching things on the blog and other subfolders, but have a large role there.

**Jakub Rudnik:** So I'm coming in.

**Jakub Rudnik:** As a new managing director, I've been on the account for less than two months and trying to understand, like, we have a few work streams and strategies going.

**Jakub Rudnik:** But I know roughly how traffic is going for those pieces and we can get that through just.

**Jakub Rudnik:** But to me, the black box is like, what works from a conversion standpoint, like what's truly driving leads, trials, signups, revenue for you all.

**Jakub Rudnik:** And both with like the content that we're doing, of course, we want to prove that ROI like in a really one-to-one way.

**Jakub Rudnik:** Like we did this and our revenue comes out the other end.

**Jakub Rudnik:** But for me, even more is like from the ideation and connecting dots standpoint of like site-wide, but especially on organic driving content.

**Jakub Rudnik:** What does turn into revenue right now?

**Jakub Rudnik:** And what can I identify as something that's replicable across other pieces of content or other campaigns or something like that?

**Jakub Rudnik:** So Carrie directed me to you all on, I think, understanding that funnel like loosely.

**Jakub Rudnik:** If I know when someone comes in, what they do, that would be helpful.

**Jakub Rudnik:** But even more so is like where there's been success historically and across the site.

**Jakub Rudnik:** And that I can like do the pattern matching to new individual topics.

**Jakub Rudnik:** But even themes of topics and stuff.

**Jakub Rudnik:** So that's where my head goes.

**Jakub Rudnik:** don't know, like, access-wise, it seems like you have the access and can pull those type of things.

**Jakub Rudnik:** But that's where I'm looking.

**Jakub Rudnik:** I gave a couple of bullets on, like, types of information that would be useful if any of that is available.

**Jakub Rudnik:** I'll stop there.

**Jakub Rudnik:** But does that make sense?

**Jakub Rudnik:** What, you know, what would be the next best way to get some of that information?

**Philip Siu:** Yeah, that's all super clear.

**Philip Siu:** My only question is, in terms of the scope of what you're trying to impact and change, is it mainly going to still be content-related?

**Philip Siu:** Or are you thinking about other stuff as well in terms of optimizations?

**Jakub Rudnik:** Really, primarily content and mostly organic, like, first touch is organic, is the bulk.

**Jakub Rudnik:** I think there are other insights I can get if people are converting to one certain type of content from what's called social or email.

**Jakub Rudnik:** Like, there's learnings to be had there.

**Jakub Rudnik:** And there's learnings to be had on, you know, there's certain landing pages or a site section that even if we don't touch, they're really doing well.

**Jakub Rudnik:** Like, I know a pricing page is going to convert a ton.

**Jakub Rudnik:** Like, I don't need that data.

**Jakub Rudnik:** I don't need, like, homepage necessarily.

**Jakub Rudnik:** But, like, there's anything else that is in that organic ballpark that converts outside of, like, blog.

**Jakub Rudnik:** There's still that.

**Jakub Rudnik:** Those insights would be helpful.

**Jakub Rudnik:** But truly, like, 90% of what we're going to touch is organic.

**Jakub Rudnik:** And 75 to 80 is on that blog and anything.

**Jakub Rudnik:** There's a couple, like, we're creating a folder on, like, how to start a business.

**Jakub Rudnik:** Like, that won't be a blog, but that's blog adjacent.

**Jakub Rudnik:** Gotcha, gotcha.

**Philip Siu:** I was just going to say, if you do have any, like, CRO-related ideas that has to do with, like, leveraging some of the things that you see, like, I'm definitely open to it in terms of ideas.

**Philip Siu:** So it doesn't have to be strictly, like, limited to the blog and content.

**Philip Siu:** But I just want to make sure that we're on the same page or like what you're thinking.

**Jakub Rudnik:** No, that's – so my focus is certainly on the blog and, like, first touch attribution there.

**Jakub Rudnik:** But we just kind of outlined some things for Kerry and the rest of the –

**Jakub Rudnik:** Team on what we want to do, and some of that analysis for me and experimentation would go beyond that.

**Jakub Rudnik:** So I would love to continue that part.

**Jakub Rudnik:** Knowing that you'd be working in the partnership this way, that's really good to know, and we'll keep those things in mind.

**Jakub Rudnik:** think our SOW is organic in that stuff, but from the way that I've looked, like how Kyle approached this, and I tried to go in his footsteps, like, what can we add?

**Jakub Rudnik:** What are the extra values?

**Jakub Rudnik:** If we're seeing things, we should be sharing that and have that experience.

**Jakub Rudnik:** So I think that this makes a ton of sense.

**Jakub Rudnik:** Glad to be working with you on those things.

**Jakub Rudnik:** That sounds good.

**Jakub Rudnik:** Okay, how about we jump into it?

**Philip Siu:** But maybe before that, I'll give, like, maybe a two-line intro of, like, who I am.

**Philip Siu:** And then maybe Zee could also, like...

**Philip Siu:** Yeah, thank you.

**Philip Siu:** So my name is Phil.

**Philip Siu:** I am the website growth lead here at Homebase.

**Philip Siu:** So I basically manage the website function as a whole.

**Philip Siu:** So a mix of, I think of it as, like, website experimentation slash CRO, what we're going to be sort of, like, walking through, as well as, like, website, like, ops.

**Philip Siu:** So anything when it comes to actioning.

**Philip Siu:** Building, developing, anything on the website, like that's sort of like my terrain, and I've been here for about two and a half years.

**Philip Siu:** I'll pass it off to Zeeb for a quick intro.

**Philip Siu:** Hey everyone, my name is Zeeshan.

**Zeeshan Habib:** I'm the analytics guy, supporting marketing team.

**Zeeshan Habib:** I've been around the same time as Phil, and the whole time I've been with the growth team specifically.

**Zeeshan Habib:** My area is basically aligned with marketing ops and marketing analytics, so I work very closely with data science, data ops, and the numbers that we have.

**Zeeshan Habib:** And if you have any questions around what numbers we should use, I can help you out about that.

**Zeeshan Habib:** Awesome.

**Jakub Rudnik:** Thank you, and thank you for stopping me and my impetus to go forward to do those intros.

**Jakub Rudnik:** It's really helpful.

**Jakub Rudnik:** All good.

**Philip Siu:** Should we jump into it?

**Philip Siu:** Yeah, for sure.

**Philip Siu:** Cool.

**Philip Siu:** Okay, so I did see all the questions that you asked.

**Philip Siu:** How about we sort of just bang out a couple of those?

**Philip Siu:** I have two views that I thought would be a good, good views to share with you that sort of captures a lot of the questions that you have.

**Philip Siu:** But for starters, in terms of context, like you asked about what specific events are tracked in terms of conversion.

**Philip Siu:** I'd say that the two main ones are sign up by far.

**Philip Siu:** We definitely heavily prioritize sign up.

**Philip Siu:** So account creation in particular is what we define as a sign up.

**Philip Siu:** I'm creating an account.

**Philip Siu:** It is a free account originally.

**Philip Siu:** And then, of course, the North Star for the company as a whole is getting them to pay.

**Philip Siu:** So like a paying location, right?

**Philip Siu:** And then in addition to that, we do have contact sales forms.

**Philip Siu:** You can find that through our contact sales page.

**Philip Siu:** We also have other lead capture forms and all that.

**Philip Siu:** Contact sales in particular is something that we care about to feed leads for our sales team, of course, to work in terms of inbound.

**Philip Siu:** And then apart from that, well, contact sales form plus a calendar.

**Philip Siu:** So like that's also.

**Philip Siu:** Within the sales experience, if you were to ask me how do we think about a sign up versus the sales flow, honestly, there isn't really a good way in terms of measuring the value of those things.

**Philip Siu:** We currently have both as an option.

**Philip Siu:** Call it 80 to 90% of my time, I'm always just focusing on sign up.

**Philip Siu:** When it comes to lead capture as a motion and lead nurture as a motion, that's something that we've been talking about for a while and tested in different ways.

**Philip Siu:** It has not really materialized.

**Philip Siu:** Now we've been beginning those conversations again.

**Philip Siu:** So all said, I think one thing that is consistent has always been sign up.

**Philip Siu:** I could sort of put it in that way.

**Philip Siu:** Awesome.

**Philip Siu:** Really helpful context.

**Jakub Rudnik:** I like this because more of my experience is on the PLG and free sign up to pay motion.

**Jakub Rudnik:** So this is, I'm glad to be hearing this.

**Jakub Rudnik:** I'm better here.

**Jakub Rudnik:** So this is all good.

**Philip Siu:** Definitely in favor of PLG, although like there are a lot of things that we've been trying to test out with SLG, but I think we could focus on PLG.

**Philip Siu:** probably helps you.

**Philip Siu:** In terms of first touch and last touch, we have visibility into like both like or like basically any touch.

**Philip Siu:** First touch, last touch, I think Zee could probably like talk about it in further detail as well.

**Philip Siu:** But in terms of our attribution model, we favor last touch or specifically last touch.

**Philip Siu:** And we also favor like a paid touch.

**Philip Siu:** So whenever there's like a paid ad that is in that journey, we sort of favor towards weighing those heavier.

**Philip Siu:** Anything that you would add in terms of context there, Zee?

**Philip Siu:** You're on mute.

**Zeeshan Habib:** I think like you covered that completely.

**Zeeshan Habib:** The only thing is we have two views right now.

**Zeeshan Habib:** So the first touch is they're not in Looker, but in a different dashboard.

**Zeeshan Habib:** Last touch is what we...

**Zeeshan Habib:** We usually report on, on all of our numbers when we are reporting anywhere.

**Zeeshan Habib:** And as Phil said, that it's a bit convoluted where we look at paid touch and within paid touch, we give reference to Google first, then Bing and other paid channels coming in.

**Zeeshan Habib:** Having said that, we do have records of every interaction that a user has.

**Zeeshan Habib:** So in case you need to see that, okay, how many touches does a customer have, or we want to talk to customers who have touched a specific page or work with specific product at any stage in their life, we have the capability to put it, pull it, but not immediately, like the last touch or first touch.

**Zeeshan Habib:** Okay, really helpful.

**Jakub Rudnik:** Yeah, this is pretty advanced.

**Jakub Rudnik:** So this is good.

**Jakub Rudnik:** Sometimes we have clients that don't know any of this.

**Jakub Rudnik:** So this is really, really helpful.

**Philip Siu:** Okay, how about we jump into the two views, which relates to basically the conversion reports that you're talking about.

**Philip Siu:** And I think it's sort of like bring over to anything.

**Philip Siu:** So this is the marketing website dashboard that Zee over here created, thankfully.

**Philip Siu:** And this is something that we refer back to on a pretty regular basis.

**Philip Siu:** We sort of broke it down by, this is a new view that we created with Tofu, MoFu, BoFu.

**Philip Siu:** So breaking it down by funnel stages when it comes to traffic and how much it's driving in terms of signups and signup.

**Philip Siu:** So this would be Tofu, MoFu, BoFu by signups, and then top of funnel, middle funnel, and bottom funnel when it comes to signup rate.

**Philip Siu:** What I did here, and we could also filter it by different ways.

**Philip Siu:** I thought I already did it here.

**Philip Siu:** But anyways, we could sort of filter it by page groups and all that.

**Philip Siu:** If we want only blog in particular, then as of right now, I think our categories isn't completely done for.

**Philip Siu:** Correct me if I'm wrong, Zee.

**Philip Siu:** I think we saw that out.

**Philip Siu:** The reason is because the blog in particular has a lot of custom nuanced.

**Philip Siu:** Categorization when it comes to Tofu, Mofu.

**Philip Siu:** As an example, our paid pages usually include free as a URL string or LP, meaning landing page.

**Philip Siu:** We literally have it just in the URL.

**Philip Siu:** So it's very easy to identify.

**Philip Siu:** We spoke with Kerry.

**Philip Siu:** There's no way for us to be any type of identifier within the URL.

**Philip Siu:** That means that they're Tofu.

**Philip Siu:** And that means that they're Mofu.

**Philip Siu:** So we legit just have an error table of, I guess, over 1,000 rows.

**Philip Siu:** And Z needs to work through what's the best way to query that based off of the URL, of that specific URL, that's going to be either Tofu or Mofu for the most part.

**Philip Siu:** Because it's the blog, there's usually no Mofu.

**Philip Siu:** But yeah, anyway, so that's something that I think is in the background.

**Philip Siu:** Z just has a lot of other assets that he's been prioritizing.

**Philip Siu:** And so we just haven't been able to sort of categorize that.

**Philip Siu:** But apart from that, I think this is a good visibility of things that are outside of the blog as well.

**Philip Siu:** So going down a little bit further.

**Philip Siu:** This would be like some of the main groups of how we think about growth marketing as a whole.

**Philip Siu:** So in terms of like paid, organic, and some of the paid groups that we think about.

**Philip Siu:** like organic home, organic product, organic non-product.

**Philip Siu:** So I did a little bit of an exercise with like the entire growth marketing team that includes like Carrie as well, the paid team, and others as well as just like our director.

**Philip Siu:** And then this is how we're sort of grouping sort of the views of how we're thinking about the segments of the site.

**Philip Siu:** So like, hey, like paid traffic onto like certain page groups, and then organic traffic onto certain page groups as well, right?

**Philip Siu:** And then like that signup rate, and I believe there should have been, yeah, like traffic, signups.

**Philip Siu:** So anyways, like those are the main things that we're looking at in terms of like the metrics, and then also the segment.

**Philip Siu:** So call it in summary, like funnel stage is one big cut, and then the other cut is page groups slash marketing channel, marketing channel.

**Philip Siu:** So we do both.

**Philip Siu:** And then we could always filter it by a certain one.

**Philip Siu:** if we're only interested in organic only, as an example in this conversation, then this would also change.

**Philip Siu:** And then this would also change too, in terms of all the numbers.

**Philip Siu:** And then we could also see signups.

**Philip Siu:** We also have a web engagement rate metric up top.

**Philip Siu:** That might be actually something that's pretty interesting for us to measure the blog on.

**Philip Siu:** So what web engagement rate means, in terms of our definition of it, is just anyone that has visited two or more pages.

**Philip Siu:** Just like, in other words, call it like an inversion of a bounce.

**Philip Siu:** Yeah.

**Philip Siu:** Right.

**Philip Siu:** And the reason why we did this too, is like, we noticed that when someone visits more than two pages, like not a surprise, they tend to convert at about, I forget the specific number now.

**Philip Siu:** think it's about like 3x more than anyone that only visits one page.

**Philip Siu:** Because the one page visits also includes people that have bounced.

**Philip Siu:** Right.

**Philip Siu:** And so as a result, I feel like that's something that we've been sort of toying with as like maybe a middle of funnel KPI or middle funnel goal or a leading indicator towards like sign up.

**Philip Siu:** So that's something that we've been talking about and I'm trying to push us towards that direction.

**Philip Siu:** We have not actually landed on explicitly what is that MoFu goal that we want.

**Philip Siu:** I think that's the next step of something that I'm trying to test of what would be a good MoFu goal.

**Philip Siu:** for the team, but then it would be different depending on sort of the channel and the team member.

**Philip Siu:** Like paid MoFu goal would probably be different than organic or like carries, right?

**Philip Siu:** Yeah, definitely.

**Philip Siu:** So anyways, like that's some of the context there.

**Philip Siu:** Any questions?

**Philip Siu:** Happy to dive into like, oh, and there's also like device cuts, of course.

**Jakub Rudnik:** Yeah, the different panels and areas of the site I think are most interesting, but I also think that engagement-to-visit metric is really compelling. I think there's opportunity there for us to dig in and understand why things are working.

**Jakub Rudnik:** I think with some of the on-page recommendations and tests that I want to stand up or recommend, that metric makes a ton of sense to look at and help us experiment on.

**Jakub Rudnik:** So no questions, that's really good. Those insights are more than I've had at most stops. These reports would go a long way. As long as we have the ability to double-click in and see the actual URLs, that's the piece I haven't seen yet, but I'm sure it's there. This is all really useful.

**Philip Siu:** Correct me if I'm wrong, Zee.

**Philip Siu:** I feel like this view is probably not the best to do that as of right now, although that would be ideal when we talked about it.

**Philip Siu:** Amplitude is probably the best way to do it.

**Philip Siu:** And so I prepared that to show the team here.

**Philip Siu:** You agree?

**Philip Siu:** Yeah, I agree.

**Philip Siu:** So yeah, a high level view, that would be the dashboard that we used right there in terms of what's driving, what's not, all the different groups.

**Philip Siu:** then once you're like, we want to sort of zoom in to any particular segment or cut, what we would do is we usually use Amplitude.

**Philip Siu:** And so what I did right here as a quick example would be like, so actually for context, our entire site is instrumented on Amplitude, which is a product analytics tool.

**Philip Siu:** I'm not sure if you guys are super familiar with it.

**Philip Siu:** Yeah, cool.

**Philip Siu:** We use it for web analytics.

**Philip Siu:** then so what I did here was I just created a funnel of anyone that has visited any blog page, and then they ended up signing up.

**Philip Siu:** They entered our signup flow, and then ended up signing up.

**Philip Siu:** So like that's the, let me show you the funnel.

**Philip Siu:** It's a three-step funnel.

**Philip Siu:** Sometimes I even remove this.

**Philip Siu:** Let me remove this right now so it's a little bit more clear.

**Philip Siu:** It's like what this shows is like.

**Philip Siu:** In the last six months, there's about 500,000 visitors on the blog, and only 1.26% entered the signup flow, with less than 0.3% actually signing up. This is good context — I actually don't focus on the blog too much. I definitely partner with Carrie in different ways and want to unblock the team as much as possible, but when it comes to the total amount of signups, if we go back to the Databricks dashboard, it doesn't materialize to a lot compared to the rest of the site. I call it core versus blog. So I end up focusing a lot of my attention on core. But for this view, once we do the group-by filter path, we have a breakdown of the page URLs driving most of the signups. It's a little finicky depending on how you manipulate it, but you get a sense. If I do over-time analysis and total conversion count, you can see the top pages that are signing up.

**Jakub Rudnik:** That's really helpful.

**Philip Siu:** And then like there's a table here, you could always export it into a CSV, right?

**Philip Siu:** In the last six months, you could group it and change like the different time series that you want.

**Philip Siu:** But that would be my view of it.

**Philip Siu:** So like just to show the visual, I guess that shows, call it last month, the top converting blogs would be this one right here.

**Philip Siu:** Free payroll software, make small business payday, et cetera, schedule and then et cetera.

**Philip Siu:** Yeah, like some of these, you could throw a dick into

**Philip Siu:** Do you have Amplitude access?

**Philip Siu:** I don't believe I do, yeah.

**Philip Siu:** We don't.

**Jess Scott:** Carrie said that there was, like, a lot of hoops and clearances we would have to jump through, and essentially their director said it's not worth it for us to have the access, but I don't know, perhaps you have different insight.

**Philip Siu:** They probably know better in terms of trying to go through that.

**Philip Siu:** I haven't actually tried to share Amplitude with anyone externally either, so it might be good to just, like, pull a report of this.

**Philip Siu:** And then share it with you.

**Philip Siu:** Maybe there's just a CSV file to start?

**Philip Siu:** Yeah.

**Philip Siu:** I mean, that's a great start.

**Jakub Rudnik:** This exact thing by month would be a massive, like, start.

**Zeeshan Habib:** One of the things that I can do is, if you have a specific need, say, for example, you want to track traffic and behavior coming to a specific page or from a specific URL, what I can do is I can create a pipeline through which maybe every day.

**Zeeshan Habib:** Or every two days, I can update a file that is shared with you, and that would have all the clicks, all the links available, and you can then use the file as needed.

**Jakub Rudnik:** That would be great, especially if it's automated. Depending on what that lift is, we wouldn't need anything updated that frequently. Even every other week or monthly is enough to get a sense of trends right now. I think when we get to the experimentation side, we'd want to know more frequently. But right now I'm really just looking at historical data. I appreciate you being mindful of not adding extra lift if it's not necessary.

**Philip Siu:** Yeah.

**Philip Siu:** Yeah, I could pull this.

**Philip Siu:** Like, let me know what, like, number of months you want and all that in terms of the cut.

**Philip Siu:** And then we could also align on what metrics to pull.

**Philip Siu:** And then we could also, I could just pull it as you or myself.

**Jakub Rudnik:** Yeah, this right here, probably 12 months, and then I don't know if you can add one more step to the funnel to add that paid conversion or something along, I know that's going to be a small number, but I would love to see where, like, the users that have upgraded to paid, and, you know, depending on what metrics, how you measure that, open, if possible, that's nice to have.

**Jakub Rudnik:** We don't have that here.

**Philip Siu:** Oh, no problem.

**Philip Siu:** Sorry.

**Jakub Rudnik:** I use Mixpanel more than Amplitude, and we had that.

**Jakub Rudnik:** Anyway, that's fine.

**Jakub Rudnik:** Just the signup, that's the most important metric on the blog anyway, and that is a great starting place.

**Jakub Rudnik:** yeah, 12 months, this exact report, this would take me pretty far.

**Jakub Rudnik:** Cool.

**Philip Siu:** Keep in mind, anything before September, it's because we migrated from WordPress to Webflow, so all the data is a little different, and then in terms

**Philip Siu:** Like some of the blog performance, our URL is also contained a forward slash at the end before and then got removed since we migrated to Webflow.

**Philip Siu:** So like, that's why you might see some like funkiness in terms of the data here, like pre.

**Philip Siu:** Yeah, that's so annoying.

**Jakub Rudnik:** And we had another client that had the exact same thing that moved to Webflow.

**Jakub Rudnik:** Oh my gosh.

**Jakub Rudnik:** No worries. That data from September onwards is more than enough — nine months is good.

**Philip Siu:** I'll export the same thing for you. In addition to signup success, I thought it'd be interesting to include how many people enter the signup flow — you get a bigger number and quicker signal. There's also the web engagement metric we mentioned, and a cool indicator is anyone who visited a product page from a blog page, since people often visit product pages before converting. Let me know what would be valuable for your work.

**Jakub Rudnik:** I'd say both of those. It's a really good point. I'm so focused on conversion, but since you attribute on last touch, that core page makes a ton of sense. I also like the idea of tracking who entered the signup flow because that definitely increases and probably does so pretty significantly. I'll take both of those metrics.

**Philip Siu:** Great suggestion.

**Philip Siu:** No problem.

**Philip Siu:** Pull it for you right now.

**Philip Siu:** And then apart from that, any questions I could answer or like anything that I didn't cover that you had on your list?

**Philip Siu:** I just want to make sure that.

**Philip Siu:** These are the big things.

**Philip Siu:** I'm sure we'll have some as I get in and

**Jakub Rudnik:** You know, I'll make sure to be really mindful of the ask, but if there's like small things, if you don't mind ping in Slack as I come across them, you know, there's always like just history of websites that we won't be aware of it, like intimately, like you will, and the analytics side too.

**Jakub Rudnik:** From the, what was the Databricks?

**Jakub Rudnik:** Dashboard?

**Jakub Rudnik:** Yeah, well, I'd be at the highest level, you know, the site section view, I'm going stack.

**Philip Siu:** Dashboard, can you remove this filter?

**Philip Siu:** Because I was filtering it by organic only, for now.

**Philip Siu:** Yeah, not that one, not that one.

**Jakub Rudnik:** Dashboard, think it's this, does it have like compare, it was one of them that had a marketing category.

**Jakub Rudnik:** If you could just give me a screenshot of the Databricks dashboard, that would be helpful. I just want to know where I should be looking for organic success, and at the highest level, where else on the site I should be getting ideas. That will be more than enough.

**Philip Siu:** I can filter it by organic for you. That sounds good.

**Philip Siu:** Thank you.

**Jakub Rudnik:** But yeah, I think we'll get more just on the amplitude side.

**Jakub Rudnik:** Like we can already see those listicles, like as three or four of those top articles.

**Jakub Rudnik:** And like, that's what we wanted to double click into.

**Jakub Rudnik:** So I think it's, it adds.

**Jakub Rudnik:** I'll

**Jakub Rudnik:** It's validity to some of those strategies.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** And that validates some of our strategies when we're targeting refreshes. Those are my core questions.

**Jakub Rudnik:** You've answered a ton.

**Jakub Rudnik:** This was extremely productive.

**Jakub Rudnik:** So thank you for just doing it live and walking us through all this stuff.

**Philip Siu:** Yeah, no problem.

**Philip Siu:** Glad I could help.

**Philip Siu:** I'll send those to you right after this.

**Philip Siu:** And then, yeah, awesome.

**Jess Scott:** Phil, slightly off topic — do you think we could get the Webflow API key? We're trying to build out some auto-publishing, and Carrie mentioned you were the person who could provide that.

**Jakub Rudnik:** We need the Webflow API keys. I think we'll have to give specifics on what's needed, but we basically want to auto-publish from our internal tool to Webflow, and we'd require the Webflow API key to do so.

**Philip Siu:** Oh, yeah, I think that's what Carrie was mentioning. Are you guys building a CMS bridge?

**Jakub Rudnik:** Essentially, yeah. It's sort of similar to that.

**Philip Siu:** Okay, got it.

**Philip Siu:** I don't, to be honest, off the top, I don't know exactly where to pull that for you guys, but I can look into it.

**Philip Siu:** Yeah, thank you.

**Philip Siu:** If have more resources or instructions on exactly where I pull that, like, that might be helpful for me as, like, a start of, like, what exactly you guys need and all that.

**Philip Siu:** But I generally get the sense of what you're saying.

**Philip Siu:** It's, like, it's almost like an air table and you populate, and, like, when you update the air table, it's going to update the CMS, right?

**Philip Siu:** Like, that's the idea, right?

**Philip Siu:** Yeah, that's generally it.

**Philip Siu:** We'll get those instructions.

**Jakub Rudnik:** There are slight customizations depending on how you have Webflow set up, but we can pull what we've needed for past clients and send that over. We can get 90% of the way there, and then there'll be small tweaks depending on your setup.

**Philip Siu:** Do you know if that's going to be an additional cost on the Webflow front?

**Jakub Rudnik:** Good question. I don't think so, but we'll confirm that before we proceed.

**Philip Siu:** If you share the info over, we'll figure it out.

**Jakub Rudnik:** Awesome. I think that's everything.

**Jess Scott:** Thank you both so much for the time.

**Jess Scott:** Really appreciate it.

**Jakub Rudnik:** Let's know how we can help.

**Zeeshan Habib:** Yeah, it's awesome.

**Philip Siu:** No problem.

**Philip Siu:** Pleasure meeting you guys.

**Jakub Rudnik:** Thanks so much, guys.

**Jakub Rudnik:** Bye.

**Zeeshan Habib:** Bye.
