# Anything <> GrowthX - Bi-weekly Sync

<metadata>
date: 2026-02-10
time: 21:29 UTC
duration: 37 minutes
organizer: team@growthxlabs.com
participants: Kyle Gaudreau, Katya Luscomb, Dhruv Amin, Zaria Zinn
fathom_recording_id: 121375782
fathom_url: https://fathom.video/calls/561182209
share_url: https://fathom.video/share/e3g-An-XmGWYY1NijWdxpsnEnEkbD14r
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Anything aligned on a two-phase website migration strategy to consolidate SEO authority across three fragmented domains (create-anything.com, create-xyz.com, anything.com), starting with canonical tag updates to anything.com before executing full 301 redirects later. The team also reviewed a Programmatic SEO (PSEO) initiative targeting long-tail keywords in app development, with a planned 50–100 page MVP focusing on mobile app builders, and secured new Dubb attribution tooling to link content performance directly to revenue signals.

---

## Context

Anything is a no-code app builder founded by Dhruv Amin and Zaria Zinn (Anything/create.xyz), currently operating across three domains that are fragmenting SEO authority and revenue visibility. GrowthX is providing content strategy and SEO execution support for Anything's content marketing engine, including website architecture decisions, content attribution, and programmatic SEO rollout. This is a strategic engagement focused on helping Anything scale organic traffic and establish direct attribution between content and revenue, addressing both immediate migration headwinds and longer-term programmatic growth.

---

## Relevance

**To GrowthX Delivery:**
- Website migration strategy: Two-phase approach (canonicals first, then DNS 301s) demonstrates GrowthX's risk-mitigation expertise with multi-domain SEO consolidation
- PSEO execution model: Designing repeatable, templated pages with strong UX rather than thin content—differentiates GrowthX's approach and sets expectations for client quality standards
- Mobile app builder vertical: Identified as high-intent, lower-CPC segment vs. broader "web app builder" queries, guiding scope and prioritization of the 50–100 page MVP
- Attribution tooling setup: Connecting Dubb short-link tracking to content performance enables faster signal-to-revenue feedback loops for iterative optimization

**To GrowthX Business Development:**
- Account health: Anything is actively investing in paid marketing (pulling back in January, ramping Women in AI event) and committed to aggressive scaling—signals expansion potential beyond base engagement
- Referenceability: PSEO success at Anything (50–70k monthly visitors potential) becomes referenceable case study for programmatic scaling in SaaS
- Dhruv's responsiveness commitment: Flagged communication as potential bottleneck; secured explicit agreement to improve Slack responsiveness, reducing friction for fast-paced execution

---

## Decisions & Commitments

**Migration Decision:**
- Update canonical tags on homepage and docs to point to anything.com immediately
- Schedule DNS 301 redirects for later (timeline TBD), with expectation of 4–6 week recovery window before aggregate growth outperformance
- Monitor daily via GSC and PostHog before pulling the trigger on 301s

**PSEO Initiative:**
- Scope MVP at 50–100 pages, starting with mobile app builder vertical (higher conversion intent than web app builder)
- Prioritize user experience over thin content to avoid Base44-style traps
- Target launch in March 2026 (cost and timeline to be finalized)
- Begin with hub pages for verticals (healthcare, etc.) and tags for apps to create semantic web without deep folder nesting

**Dubb Attribution Setup:**
- Kyle to create sitelinks folder structure for GrowthX content in Dubb
- Anything team to set up manual polling for sitemap updates (automated daily cron in progress)
- Use Dubb data as directional signal to validate content-to-revenue attribution

---

## Overview

- **Migration Decision:** Implement a two-phase migration: first, update the homepage and docs canonicals to `anything.com` to consolidate authority; second, execute a full 301 redirect at the DNS level later.
- **PSEO Strategy:** Launch a Programmatic SEO (PSEO) initiative, starting with a 50–100 page MVP to test the model before scaling.
- **New Attribution Tool:** GrowthX now has access to Dubb, a short-link tool providing directional revenue attribution for content to guide prioritization.
- **Communication:** Dhruv will be more responsive on Slack for rapid decisions to accelerate execution.

---

## Key Topics

### Website Migration Strategy

  - **Problem:** The three-domain setup (`create-anything.com`, `create-xyz.com`, `anything.com`) is splitting SEO authority, causing traffic headwinds.
      - Non-brand homepage traffic is flat or down 10% over six months.
  - **Solution:** A two-phase migration was agreed upon.
    1.  **Phase 1 (Immediate):** Update canonical tags on the homepage and docs to point to `anything.com`.
          - **Rationale:** This is the safest, lowest-risk first step to consolidate authority.
    2.  **Phase 2 (Later):** Execute a full 301 redirect at the DNS level.
          - **Rationale:** This "rip the band-aid off" approach is expected to cause a temporary traffic dip (4–6 weeks) but drive higher aggregate growth over 3–6 months.

### Programmatic SEO (PSEO) Strategy

  - **Goal:** Build a scalable content engine for long-tail keywords around app development.
  - **Execution:** GrowthX will build templated pages, focusing on user experience to avoid thin content.
      - **Structure:** Use hub pages for verticals (e.g., healthcare) and tags for apps to create a semantic web without deep folder nesting.
  - **Idea:** Dhruv proposed a "mobile app builder" play.
      - **Rationale:** Google Ads for this category show higher conversions and lower CPCs than "web app builder."
      - **Concept:** Create pages for top App Store apps with teardowns and a "one-click build" prompt for Anything.
  - **Rollout:** Launch a 50–100 page MVP to test indexing and query performance before scaling.
  - **Potential:** Estimated traffic gain of 50–70k monthly visitors, with long-term potential for 2x+ growth.

### Content Attribution with Dubb

  - **Tool:** GrowthX has access to Dubb for short-link attribution tracking.
  - **Functionality:** Tracks downstream metrics (views, leads, signups, sales) to provide directional revenue signals for content.
  - **Limitation:** Relies on last-touch attribution and cookies, so data is directional, not definitive.
  - **Benefit:** Enables faster prioritization by linking content performance to revenue, not just traffic.

---

## Action Items

**Dhruv Amin (Anything)**
- Set canonicals to anything.com on homepage + docs; then monitor daily and schedule DNS 301s
- Set up manual Dubb sitemap poll; then iterate once automated daily cron is live

**Kyle Gaudreau (GrowthX)**
- Create Dubb sitelinks folder for GrowthX content; then review Dubb attribution data and coordinate with Anything on additional sitemap polling
- Validate mobile app builder search volume with deeper research; then scope PSEO MVP (50–100 pages) and share timeline + cost estimate with Dhruv by early March

---

## Transcript
**Katya Luscomb:** This meeting is being recorded.

**Katya Luscomb:** Hey.

**Kyle Gaudreau:** How's it Your background's always funny.

**Kyle Gaudreau:** Maybe I'm just used to yours.

**Katya Luscomb:** Uh-huh.

**Kyle Gaudreau:** Is it the way that you can't see you?

**Katya Luscomb:** And then you just appear?

**Katya Luscomb:** It's probably because my video always starts off, and then I turn it on when I come in, and the first thing to load is the background, so it looks like I'm a ghost.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** It's like a neat parlor trick.

**Katya Luscomb:** Got to throw a little magic in there every once in a while, right?

**Kyle Gaudreau:** I've never met in person, so, you know, what's to say?

**Katya Luscomb:** I could just, yeah, I could just be a ghost.

**Kyle Gaudreau:** I could just be an AI twin.

**Katya Luscomb:** Uh-huh.

**Katya Luscomb:** Oh, that'd be pretty wild.

**Katya Luscomb:** My husband teases me sometimes that I sound like AI.

**Katya Luscomb:** And so when I got work, like when I started getting into AI content production, yeah, it was not very nice when he told me that.

**Katya Luscomb:** But yeah, that was pretty good.

**Katya Luscomb:** Hi, how's it going?

**Zaria Zinn:** Hi, good.

**Zaria Zinn:** How are you?

**Katya Luscomb:** Good, thanks.

**Zaria Zinn:** How's your week been?

**Zaria Zinn:** It's been good so far.

**Zaria Zinn:** We have a big event tonight at the office that we're hosting.

**Zaria Zinn:** We're doing a women in AI happy hour.

**Zaria Zinn:** So we're about to have like 200 people in the office.

**Katya Luscomb:** So we're like, getting everything ready for that.

**Katya Luscomb:** Yeah, yeah.

**Kyle Gaudreau:** exciting.

**Katya Luscomb:** Sounds like a big day for sure.

**Zaria Zinn:** Yeah, it'll be fun.

**Zaria Zinn:** We've done two of them before, but the last one is last year.

**Zaria Zinn:** This is the first one in the new office.

**Zaria Zinn:** And this one's like twice the size as the other one.

**Zaria Zinn:** So it'll be fun.

**Kyle Gaudreau:** I've been meaning to ask, where are you guys based in the city?

**Zaria Zinn:** Because you're in the city, right?

**Zaria Zinn:** Yeah, we're right by Union Square, kind of by like the Gates of Chinatown.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** We're over by South Park.

**Zaria Zinn:** So South Park is kind of just like right back here.

**Zaria Zinn:** Nice.

**Zaria Zinn:** Yeah, yeah.

**Zaria Zinn:** So not too far away, I suppose.

**Zaria Zinn:** Yeah, not far at all.

**Katya Luscomb:** Hey, Drew.

**Katya Luscomb:** How are you?

**Dhruv Amin:** How are you guys doing?

**Katya Luscomb:** Good.

**Katya Luscomb:** Thanks.

**Katya Luscomb:** Are we going well so far?

**Dhruv Amin:** Yeah.

**Katya Luscomb:** Awesome.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Also, thank you guys for your flexibility in moving stuff around.

**Katya Luscomb:** I know we had to finagle meeting times a little bit.

**Katya Luscomb:** But really primarily wanted to make sure we had some time to connect and talk about migration.

**Katya Luscomb:** And then we've got a PSEO strategy to go over as well.

**Katya Luscomb:** So a couple different things.

**Katya Luscomb:** We've got performance overview we can go over.

**Katya Luscomb:** A lot of what we're noticing relates back to really wanting to align on a decision around the migration.

**Katya Luscomb:** Big picture, we're starting to see some headwinds week over week that we see as pertaining to the migration.

**Katya Luscomb:** Before I get too, too far in the weeds...

**Katya Luscomb:** Do you have initial thoughts, gut reaction?

**Katya Luscomb:** Because I know we've sent a couple of messages around migration pieces.

**Dhruv Amin:** Yeah, sorry.

**Dhruv Amin:** So I actually did some initial cloud code analysis with having it do, where was this, post your message.

**Dhruv Amin:** Sorry for not responding in Slack.

**Dhruv Amin:** Um, basically, I think what we do is canonicals, um, across the board, let's do, uh, anything.com.

**Dhruv Amin:** Um, thanks for calling out that the homepage is not there, um, on when to do this traffic spike, uh, changeover.

**Dhruv Amin:** It's going to end up being anything.com at any given time.

**Dhruv Amin:** I'm, I, I could basically see from the, like search console and post hog and a bunch of other things as well.

**Dhruv Amin:** Um, let me see if I can get this in view form, um, from our internal data that.

**Dhruv Amin:** But you know, the other ones are basically, I guess I ran this a week ago, you know, AI's recommendation was like, you know, 301 redirects, but like four to six weeks recovery is like probably optimistic.

**Dhruv Amin:** It's probably going to be like three to six months.

**Dhruv Amin:** It also picked up by looking at RREFs, like the same data you guys are looking at as well in terms of like backlinks and also momentum kind of finally shifting over to create anything.

**Dhruv Amin:** And then we just changed in December.

**Dhruv Amin:** It was interesting seeing it, seeing it basically also look at the create X, Y, Z traffic, which is that like finally it seems like the create X, Y, traffic is actually dropping.

**Dhruv Amin:** And so that's actually not a huge amount of like lift.

**Dhruv Amin:** And then the question is if keeps dropping and you migrate too late, like what's the, what's the like relative issues?

**Dhruv Amin:** And then, yeah, anything, create anything is overlapping with anything by keyword overlap.

**Dhruv Amin:** So my honest take is that the biggest thing we're going to feel is, so I'm trying to remember when I looked at this.

**Dhruv Amin:** The biggest thing we're going to feel is, what was the, I guess we're like already pretty low in January.

**Dhruv Amin:** Like we're dropping in like overall Google organic traffic.

**Kyle Gaudreau:** Yeah, so like right now it's basically happening because I just started jumping.

**Kyle Gaudreau:** I've been digging into it as well.

**Kyle Gaudreau:** Like it's, to your point, really shifting to create anything.

**Kyle Gaudreau:** Anything's picking up a bit, but it's like pretty small.

**Kyle Gaudreau:** Part of that is like the mixed signal and like so much of your traffic goes to your homepage, especially in a non-brand.

**Dhruv Amin:** Like that is still like the lion's share of your non-brand traffic.

**Kyle Gaudreau:** So what's basically happening there, if you like back it out over several months, it's like best case you're flat over like six months to non-brand to the homepage.

**Kyle Gaudreau:** Worst case, trending down 10%.

**Kyle Gaudreau:** So not like massive, but at the same time, it's like how much headroom do you have for growth in that?

**Kyle Gaudreau:** And the fact that it's like that split signal of that homepage pointing to one domain and then your blog pointing to another.

**Kyle Gaudreau:** It's like.

**Kyle Gaudreau:** That separation of authority that's creating a bit of noise.

**Kyle Gaudreau:** And so, yeah, I think there's a fair argument to be made to what you're getting to is the canonicalization approach to just pointing the homepage to anything.

**Kyle Gaudreau:** It's certainly a slower path.

**Kyle Gaudreau:** It's hard to say one is necessarily right or wrong, honestly.

**Kyle Gaudreau:** The variable is just the three domain effect.

**Kyle Gaudreau:** Part of the logic I have been applying, but again, like I can't say this for certain, is like I tend to think about it less, like over a three-month period, what drives the most aggregate growth?

**Kyle Gaudreau:** My assumption that I'm operating based off of us doing other migrations is that the 301 redirect approach kind of has the rip the band-aid.

**Kyle Gaudreau:** may lead to, you know, that four-week, but in the aggregate over three months, it's maybe higher growth overall.

**Kyle Gaudreau:** But I cannot say that for certain, like no migration is always going to perform the same way.

**Kyle Gaudreau:** mean, as I...

**Kyle Gaudreau:** I think I mentioned in the past, like, I think this is, while I've done many, many migrations, I haven't done one with a three domain layer to it in this way.

**Kyle Gaudreau:** So anything I would be saying would be presumptuous.

**Kyle Gaudreau:** So I would say, like, the canonical is, like, a fair argument to say it's the safest.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** I looked at some other, like, case studies of, like, things as well.

**Dhruv Amin:** And, like, the migrations.

**Dhruv Amin:** So, yeah, I don't know.

**Dhruv Amin:** I was looking at, like, the average to actually get back to, like, similar traffic.

**Dhruv Amin:** I don't think it really matters because I, my honest take is that all homepage traffic is, like, when you're seeing these big, like, homepage ramps through the end of the year, you're basically seeing the effect of, I'm sorry, it's a little bit different because, like, Google organic traffic, I don't know how Google overcounts why it's so much overstated from what we actually see in post-hog on, like, raw numbers.

**Dhruv Amin:** I think your post-hog has attribution issues when it comes to down to the channel level.

**Dhruv Amin:** Because you.

**Dhruv Amin:** you.

**Dhruv Amin:** You have a lot that just falls into unattributed.

**Dhruv Amin:** Got it.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** So the refer might be not being captured in the Google thing as well.

**Dhruv Amin:** I guess what was this looking at?

**Dhruv Amin:** This was looking at like from post-hog, page view, path name, slash, and then I probably did a cut in the query on like whatever was direct Google-ly attributed.

**Dhruv Amin:** But like the traffic is mainly driven, like the growth in traffic in Create Anything through this time period is mainly the result of other off Google marketing efforts.

**Dhruv Amin:** It's not anything else.

**Dhruv Amin:** So my feeling is if we just move the canonicals right now, now the fact that traffic is declining across the board is probably the result of in January pulling back on marketing spend.

**Dhruv Amin:** But like if we switch the canonicals to anything and then, yeah, the question is like when to do the 301s and probably soon.

**Dhruv Amin:** But I think at the very least, like we should just have everything on the site pointing towards anything.

**Dhruv Amin:** then, yeah, and then at some point we'll rip the banion

**Dhruv Amin:** I don't know when the right quote-unquote time to do it is.

**Dhruv Amin:** I'm expecting that that's a like 20%, potentially more catastrophically if anything's not big enough traffic.

**Dhruv Amin:** But my hope would be that like Zaria, all of the marketing stuff you're doing towards anything is just building up anything's traffic and not like not the other one's traffic.

**Kyle Gaudreau:** Yeah, think that's valid.

**Kyle Gaudreau:** Like, you know, what you talked about, about that sequential approach of canonicals to 301 is a fairly common practice.

**Kyle Gaudreau:** So, yeah, I think if you can, right now you have your sitemap pointing to anything, even though that is a little bit weird, but I don't think that's a huge deal that each one says anything URLs.

**Kyle Gaudreau:** Your blog's pointing to anything.

**Kyle Gaudreau:** If you just switch the homepage to point to anything.com, that I believe is the fix.

**Kyle Gaudreau:** can't quite recall what your docs is pointing to.

**Kyle Gaudreau:** I feel like it's anything, but also.

**Kyle Gaudreau:** So your docs doesn't generate a ton of organic search traffic either.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So it's primary the homepage is like the main action here is a long way of saying.

**Dhruv Amin:** Yep.

**Dhruv Amin:** Okay, let's do that.

**Dhruv Amin:** And then just like when we're going to do the 301s, I don't know, but it should be pretty easy.

**Dhruv Amin:** Yeah.

**Kyle Gaudreau:** one thing I wasn't sure about is, is there any complexity given the way you have it built in a single app?

**Kyle Gaudreau:** Like, is there any reason that you would have, there'd be complexity of like having two domains point to one where that one doesn't have the redirect on it, you get what I'm saying?

**Dhruv Amin:** No, because the way we would implement 301s would be at the DNS level.

**Dhruv Amin:** At the DNS, okay, So that we, so that we end up getting like perfect, like every single page that was historically like a duplicate would be done.

**Dhruv Amin:** And then the core web app would be, would be fine.

**Dhruv Amin:** It's just that like, and actually like today for the most part, that is the way it works.

**Dhruv Amin:** So if you actually look at.

**Dhruv Amin:** How the site works, you land on a homepage that is like create XYZ or create anything.

**Dhruv Amin:** But then the moment you sign in, it redirects you over to anything land.

**Dhruv Amin:** And then the one other thing that like maybe it does respect like whatever you are currently, like whatever you route from.

**Dhruv Amin:** So like to which you're like already a login user and you're like, hey, I'm like going to go into a create anything link.

**Dhruv Amin:** You'll go to that link, but that's it.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Okay.

**Dhruv Amin:** Fair enough.

**Dhruv Amin:** Yeah.

**Kyle Gaudreau:** Yeah, so I think that like if possible for you all to make that canonical change ASAP, that's the main thing I think slowing us down.

**Kyle Gaudreau:** And we can just continue to look at it daily and see.

**Dhruv Amin:** The homepage is the only one that you caught?

**Kyle Gaudreau:** Correct.

**Kyle Gaudreau:** I mean, let me just since we're live, just double check the docs.

**Kyle Gaudreau:** But again, like the influence there is minimal.

**Kyle Gaudreau:** Yeah, it's a little weird that.

**Kyle Gaudreau:** So, yeah, on your docs, what you have is canonicaling to the XYZ site.

**Dhruv Amin:** I think I fixed that, but let me just make sure.

**Dhruv Amin:** Okay, should we talk about the, thanks so much, thanks for stepping up the article content.

**Dhruv Amin:** One other thing I think you guys might like or use, there is, what's the right email to invite to this?

**Katya Luscomb:** Team at growthxlabs.com.

**Dhruv Amin:** Okay, here is, um...

**Dhruv Amin:** Okay, one second.

**Dhruv Amin:** We'll give you everything you need.

**Dhruv Amin:** Okay.

**Dhruv Amin:** So I invited you guys.

**Dhruv Amin:** In Dubb, this just heads up.

**Dhruv Amin:** So it's generally short link attribution tracking.

**Dhruv Amin:** We're experimenting with, so like this number is not accurate, but it is directional.

**Dhruv Amin:** And I'm trying to figure out exactly why it's not like 100% accurate, but in the ways that it's not accurate should be inaccurate across everything.

**Dhruv Amin:** So I think that's fine for what the purpose is.

**Dhruv Amin:** Basically, it's a short link creator for other marketing campaigns.

**Dhruv Amin:** We usually use go.anything.com, and then they mirrored basically every domain.

**Dhruv Amin:** um, on site.anything.com, um, and then the route.

**Dhruv Amin:** So, um, and then what it will typically track is downstream, um, clicks, which in the site tracking case is typically views.

**Dhruv Amin:** Um, you can imagine it rather than clicks.

**Dhruv Amin:** It's like someone who actually like went to that page and looked leads, which is like a cookie set on the user's device.

**Dhruv Amin:** And then long-term, if they sign up later, that's it.

**Dhruv Amin:** So like one reason I might be depressed is like, you know, 40% of the internet uses some sort of ad blocker or a browser that doesn't have a cookie set.

**Dhruv Amin:** So like, that's it, but it gives you a directional sense of like, okay, how many, how many signups did this content drive at any point?

**Dhruv Amin:** And then, um, ultimately sales, um, of like, is this content particularly, really good?

**Dhruv Amin:** So I think it's a faster way for you guys to prioritize content early signals on, Hey, is this actually driving like revenue, um, beyond just like, is it getting ranked?

**Dhruv Amin:** Obviously has to rank in order to, and get views to even have a shot.

**Dhruv Amin:** Uh, uh,

**Dhruv Amin:** But then downstream, I don't know, maybe there is content that's extremely deep and interesting and good from a sales perspective, but is not necessarily when we're in an early growing SEO authority going to actually be super high from a traffic level.

**Dhruv Amin:** There's these folders called sitelinks.

**Dhruv Amin:** Feel free to make whatever folders you want for the GrowthX content as well.

**Dhruv Amin:** It should be pretty fast to do a script if you guys know all of your canonical URLs that you guys have already done.

**Dhruv Amin:** so we can just look at GrowthX content under the hood.

**Dhruv Amin:** And then, yeah, just pay attention to sitelinks.

**Dhruv Amin:** I think it's automatically captured.

**Dhruv Amin:** One heads up is that this pulls from sitemaps.

**Dhruv Amin:** And I did the last poll last week.

**Dhruv Amin:** Right now, they have to manually run that poll, but they're working on just a daily cron that gets it from the sitemap.

**Dhruv Amin:** And then I

**Dhruv Amin:** think the blog sitemap is updated daily anyway.

**Dhruv Amin:** So soon it will be live, but to the extent to which you guys look at this initial cut and are like, interesting, these URLs are like, these blog posts are doing well.

**Dhruv Amin:** Now we're going to go make a bunch of content changes with that data on sales and then want a new poll.

**Dhruv Amin:** Just let me know.

**Dhruv Amin:** Any questions on that?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Just to make sure I'm interpreting it correctly, users, if in a scenario where a user is blocking cookies, are you also not getting the attributed sales alongside of that?

**Kyle Gaudreau:** Because, I mean, like, you know, on the one hand, there is a thinking about this from like a session view standpoint.

**Kyle Gaudreau:** And then there is obviously a multi-session view where the cookie, you know, comes into play.

**Kyle Gaudreau:** But in a single session, if they're blocking cookies, are you not getting that revenue attributed to like a page?

**Dhruv Amin:** This is operating on last touch attribution from anything that.

**Dhruv Amin:** Sends a go link or drops that cookie.

**Dhruv Amin:** So in some ways, you might pick up more attribution if you get a user who reads a blog post and then doesn't convert then, but then sees some launch and then comes back.

**Dhruv Amin:** It's a multi-channel.

**Dhruv Amin:** It's very hard to actually get.

**Dhruv Amin:** But the reason I'm saying it's directional, not like take it as like fact of like we drove this, is that there's just, if you like think about attribution, there's just a million things that start cutting people down.

**Dhruv Amin:** And so I still think it's like just, I think it's like the signal it gives you on top of traffic, which we can see traffic is just like, well, is any of this blog content actually leading to any sort of like conversion?

**Dhruv Amin:** If we start standing up programmatic landing pages as well, like dedicated landing pages to certain types of funnels, it could like, it would also be, it would also be a really fast way to see that, which is like, I always set up dedicated landing page for building an app.

**Dhruv Amin:** For hospitals, you know, and that actually is a lot of conversion.

**Kyle Gaudreau:** Makes sense.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Yeah, we'll dig in.

**Kyle Gaudreau:** I'm sure we may have some follow questions, but yeah, I'm sure there's also some things we can figure out from their docs to figure out what we need.

**Kyle Gaudreau:** So yeah, better posts would definitely be helpful.

**Dhruv Amin:** Cool.

**Dhruv Amin:** Yeah, I think it just saves the question that we were talking about two weeks ago, which is, you know, we have GSC data, which has clicks in Google, and then we have like really annoying joins.

**Dhruv Amin:** It should just make it really automatic to, in post-hog, to the revenue thing.

**Dhruv Amin:** That's all this does.

**Dhruv Amin:** It just likes, it just very quickly gives you revenue stats off of content.

**Kyle Gaudreau:** Makes sense.

**Kyle Gaudreau:** Cool.

**Dhruv Amin:** Should we talk about the programmatic?

**Katya Luscomb:** Yeah, jump right in.

**Katya Luscomb:** Let me open it up.

**Katya Luscomb:** Hang on.

**Katya Luscomb:** I'm sorry.

**Katya Luscomb:** I only shared...

**Katya Luscomb:** I hate it when Zoom decides that it is going to dictate what screen shows up.

**Katya Luscomb:** All righty.

**Katya Luscomb:** So there's a couple different layers to this strategy that's outlined.

**Katya Luscomb:** The idea is that we would operate in phases to build it out over time.

**Katya Luscomb:** And the core idea is looking at how we can break down programmatically different types of app development and then build out content from those topic areas on those various types of apps.

**Katya Luscomb:** So one of the things that we looked at was like different verticals that have a variety of volume that we could make some strategic bets on that could potentially drive a lot of traffic.

**Katya Luscomb:** Looking at, you know, there's quite an extensive amount of volume and opportunities here that we can build out, as well as some long tail opportunities that can continue to enhance that.

**Katya Luscomb:** And, you know, obviously with PSEA.

**Katya Luscomb:** So the idea is that this would be really templated so we could build out like an exact formula and just execute across all these different verticals as we really get things dialed in.

**Katya Luscomb:** Kyle, anything specific that you wanted to call out in this piece?

**Kyle Gaudreau:** So, you know, we've purchased in a variety of different ways for different customers.

**Kyle Gaudreau:** You know, we have some fortunate to have some folks who have built some pretty badass PSEO programs in their past.

**Kyle Gaudreau:** And one of which also leads our kind of an aspect of our engineering team that focuses on the client side.

**Kyle Gaudreau:** And so what we can do with them is, you know, with some of our customers, we can get access to like, say, repos and then other places where we can source data from, align with you on the template.

**Kyle Gaudreau:** And then really just start to jam fairly fast on this.

**Kyle Gaudreau:** The mindset is like trying to create a bit of like a web semantically of different layers.

**Kyle Gaudreau:** And so where that...

**Kyle Gaudreau:** Back and go is, you know, eventually we could do things around like you start with like the broader industry, vertical, whatever, and then we could build into things like app teardowns and like how you would build this and what is their model and just like people who are basically exploratory.

**Kyle Gaudreau:** Like I'm thinking about building this thing and it seems like there's a variety of different intents out there in and around that that aligns with what you all do.

**Kyle Gaudreau:** There's a variance we could also explore around, you know, build an app like X or similar themed like variants.

**Kyle Gaudreau:** And so essentially it's like the key here and we were going a little bit back and forth of the right like URL structure and I think that could evolve over time.

**Kyle Gaudreau:** But essentially it's like trying to find that right URL structure where you're creating that nice semantic web, but also not creating all these like crazy nested folders.

**Kyle Gaudreau:** And so there's aspects of this in the site architecture, which is basically just trying to.

**Kyle Gaudreau:** To think of like how do you not create too many folders and use things like tags as well that kind of like so you could think of rather than putting everything that fits under healthcare under that healthcare URL, you can more treat that as a hub page and then you can tag different apps that fit under healthcare to that later on.

**Kyle Gaudreau:** And then if you were to click on those tags, would go to that healthcare page and so you're not like putting it under the same URL structure, but you're creating a lot of that internal linking in and around that in a really repeatable way.

**Kyle Gaudreau:** And so it's a bit of like, how do we fit these different Lego pieces together?

**Kyle Gaudreau:** And like, for me, the key to always making this work is as well as possible is like, it's one thing to talk about like the high level strategy, you know, the types of keywords we're going after.

**Kyle Gaudreau:** Obviously, this is an SEO play, but user experience should really be the main driver of this for it to really work well.

**Kyle Gaudreau:** We can...

**Kyle Gaudreau:** Find that right user experience that's truly useful for the type of intent that is out there, and we can address that in a repeatable way.

**Kyle Gaudreau:** Like, that is when programmatic really works well.

**Kyle Gaudreau:** We don't want to fall into this trap of, like, really thin pages.

**Kyle Gaudreau:** Like, Base44 is doing this a little bit.

**Kyle Gaudreau:** It's okay.

**Kyle Gaudreau:** Okay is pretty generous.

**Kyle Gaudreau:** It's very thin.

**Kyle Gaudreau:** It's doing okay.

**Kyle Gaudreau:** That's not a model we want to replicate here.

**Kyle Gaudreau:** But first, it's, like, thinking about, like, what is the core, like, step one that we build around and kind of thinking around first that vertical hub section is where to start, and then we can layer it in some of these other bets later on.

**Kyle Gaudreau:** And naturally, this could evolve in different directions as we have more data to supplement, like, what's working, what's not.

**Kyle Gaudreau:** So, there's definitely other plays we could explore, but, like, you know, just trying to think about blending the different things we've heard from you and what could drive some conversion.

**Kyle Gaudreau:** There's some search volume and relevant intent around this.

**Kyle Gaudreau:** This was one of the primary that came to mind.

**Kyle Gaudreau:** As far as next steps on something like this would go, you know, of course, we would love your feedback of, like, where does this hit the mark, not hit the mark.

**Kyle Gaudreau:** We can more bring this to life visually, get your team's feedback on that.

**Kyle Gaudreau:** We would need to think about, like, how do we scope something like this and, like, what is the actual need for what we're building?

**Kyle Gaudreau:** And so, as you can imagine, like, there can be wide varying degrees of complexity for some of these efforts.

**Kyle Gaudreau:** Some of them were, like, we did something for Airbyte recently that was, like, pretty fast to get going and relatively low complexity.

**Kyle Gaudreau:** But we have done some things that are super, super high complexity.

**Kyle Gaudreau:** It is not uncommon for us to do this end-to-end.

**Kyle Gaudreau:** So build the web experience, you know, align with you on the design needed and build that out.

**Kyle Gaudreau:** But some teams want to take that on.

**Kyle Gaudreau:** I'm guessing, you know, with you all being busy, you know, if you're bought into a strategy, you know, what that

**Kyle Gaudreau:** Cost, et cetera, that, you know, my assumption is you'd probably want us to do that and then just be able to sprint and run and like have, you know, updates on performance and like how we're pivoting strategy and get your feedback, you know, here and there.

**Dhruv Amin:** Okay.

**Dhruv Amin:** So this, yeah, I mean, I think if we feel like all really good about like whatever the strategy is and like decent confidence that like it's worth investing in both at like our current domain authority and that we think the queries are pretty aligned, this should be pretty fast to like just the raw blocking and tackling of pages.

**Dhruv Amin:** Now, like it depends on how much content is actually on those pages.

**Dhruv Amin:** I think that's where honestly the GrowthX help would be most helpful is honestly in just generating, especially if we're going to start doing this at scale, you know, this like long tail of app creation, builder landing pages is like on the mind of like, even if all you did.

**Dhruv Amin:** Let's just take our homepage, reskinned it with better H1 and H2, and then had the same prompt box get going with maybe a pre-filled prompt.

**Kyle Gaudreau:** That's essentially what Base44 seems to be doing.

**Dhruv Amin:** I think Lovable did a similar thing, and you just have long tail queries.

**Dhruv Amin:** It's fine.

**Dhruv Amin:** I think the question I have is, I've sometimes seen slightly more, to your point on a good user experience, when you actually go through the app, a slightly more innovative one.

**Dhruv Amin:** One data point that I just read was that when we compete on Google Ads for Web App Builder as traffic, it's extremely, I don't know, competitive and also doesn't convert that much.

**Dhruv Amin:** But when we compete in the mobile app builder category, there's where our conversions are so much higher and the cost per click is so much

**Dhruv Amin:** And I can't tell if that's just because no one really goes to Google and searches for mobile apps.

**Dhruv Amin:** just go straight to the app store and search for mobile app builders.

**Dhruv Amin:** But I could imagine an SEO play that was like, I don't know, we just take all the top-ranking apps in the app store.

**Dhruv Amin:** And then we build a beautiful page about what the app is, how many downloads it gets, how you would actually build it.

**Dhruv Amin:** And then like a one-click build in anything that would like, you know, build a custom prompt and like, and like kick you into the builder with like a mobile app.

**Dhruv Amin:** And that'd be interesting.

**Dhruv Amin:** Or like I saw Devin do, I think they did like an NPM package registry, which was like a, but what they tried to like connect their Devin agent to it so that the agent could then explain to you, like we would just generate like on the fly how to use that package.

**Dhruv Amin:** And for Devin, it was like clearly a play to go after kind of like the long tail of devs.

**Dhruv Amin:** And I don't know how effective it was at actually going after every single NPM package.

**Dhruv Amin:** But I.

**Dhruv Amin:** wonder, is there, like, is there, like, unique tie-in to app building that's, like, maybe that can hit scale or we can make the pages seem really interesting that's, that's, that's, that's maybe, like, I don't know, harder, easier to go through.

**Dhruv Amin:** I don't know how much search volume there's on mobile app building when I first kind of, like, started, like, thinking about that idea.

**Dhruv Amin:** I think we're, I think we're thinking similarly.

**Kyle Gaudreau:** It's, like, just different kind of versions of, like, because I was thinking there would be an aspect of that to this.

**Kyle Gaudreau:** It was a bit more, like, where does that get introduced into the mix?

**Kyle Gaudreau:** I did explore a little bit around search volume around that, but I didn't probably go as deep on that, so I can validate that a bit.

**Kyle Gaudreau:** But to the, to the fit to, you know, you've been talking about this being a key wedge for you all, you know, I can certainly see that being a play.

**Kyle Gaudreau:** And, I mean, at the end of the day, like, these things can work super well to, like, find the happy medium of what is light lift.

**Kyle Gaudreau:** It high impact and like, what is the right way?

**Kyle Gaudreau:** Where can you fall into that spectrum?

**Kyle Gaudreau:** Like, again, we don't want to create like very thin content that's a  user experience.

**Kyle Gaudreau:** But if we can find that right balance of scale and value, yeah, something like what you're walking through could certainly help here.

**Kyle Gaudreau:** So I think it's similar.

**Kyle Gaudreau:** Like, this would be like different things that we could add in around that just to kind of almost build these mini microsites around these in different layers over time.

**Kyle Gaudreau:** But it's just what is that right starting place to build around first?

**Kyle Gaudreau:** Certainly, you know, focusing on like, how do you build this or like, you know, two different popular mobile apps that it does kind of lead more into like that, like teardown mindset that we had within here.

**Kyle Gaudreau:** Yep.

**Kyle Gaudreau:** But yeah, I do like that.

**Kyle Gaudreau:** I do like I can do a little bit more research around that to see how that what's possible.

**Kyle Gaudreau:** The next step then for me to internally would be working with our

**Kyle Gaudreau:** Engineering team, just to kind of like scope this out a little bit further, how we would kind of plug in our systems with your systems.

**Kyle Gaudreau:** And then we can kind of talk about like relative timeline cost and things like that.

**Kyle Gaudreau:** Related to the migration piece of that, this is something to like think about for sure of like how much scale to throw out there.

**Kyle Gaudreau:** How we can approach that though is just kind of like if we get something, an MVP out that isn't too heavy lift, just figuring out that right scale of that first experiment.

**Kyle Gaudreau:** You know, for example, like don't start with like 2,000 pages.

**Kyle Gaudreau:** It's more like start with like 50 to 100 ballpark or something of that effect.

**Kyle Gaudreau:** And then closely monitoring like how quickly are these getting indexed?

**Kyle Gaudreau:** Are they actually getting the kind of queries we want to see?

**Kyle Gaudreau:** What are we learning from that?

**Kyle Gaudreau:** If we see some good signal, then we can just continue to like open.

**Kyle Gaudreau:** That volume up more and more is typically how we would think about it.

**Dhruv Amin:** Yep.

**Kyle Gaudreau:** So certainly like doing that alongside the editorial and then also finding different ways we can weave these two things alongside each other, internal links, things of that nature should help from like a topical relevance standpoint.

**Kyle Gaudreau:** But also I would probably have higher conviction in these things, this PSEO play driving conversions for you.

**Kyle Gaudreau:** It's important.

**Dhruv Amin:** Okay.

**Dhruv Amin:** Do you guys, have you guys seen like total, like, like what is the, what's the size of prize we're going for?

**Dhruv Amin:** Like in any of these where like, like grab a rough cut, like, I saw this in that notion doc.

**Kyle Gaudreau:** Yeah, there's some at the bottom here, but I think this, yeah, like we would need to like dig in a little bit more to add some other layers.

**Kyle Gaudreau:** Katya, if you could scroll to the bottom, I have some of that down here, but I think this is probably on the conservative side.

**Kyle Gaudreau:** Um, so like, you know, if we're adding in.

**Kyle Gaudreau:** All layers, like just thinking about it, like it does feel like a little on the conservative side, I probably like put it more like 50-70 range, but it could certainly grow beyond that on like a aggregate monthly basis.

**Kyle Gaudreau:** But we've certainly seen players that can get well above that, like 2x plus over that, but that certainly takes some time.

**Kyle Gaudreau:** Like typically when you're going to get to that range, it's going to be like six plus months of a pretty high domain authority site.

**Kyle Gaudreau:** And the delicate balance here is like we want to be really aggressive, but we also want to, again, make sure this isn't super thin content.

**Kyle Gaudreau:** We want this to be sticky results.

**Kyle Gaudreau:** So it's always about like how hard can we hit the gas and like maintain what we're building.

**Dhruv Amin:** Yep.

**Kyle Gaudreau:** So I can, I'm happy to take some of that back and like let you know.

**Kyle Gaudreau:** So...

**Kyle Gaudreau:** What I have in addition to how we may modify the plan, I'll circle back internally with the team.

**Kyle Gaudreau:** And then we can talk about like roughly like how we would think about pricing this out.

**Kyle Gaudreau:** Because generally, you know, like we have the editorial layer that is a bit of a different motion than the PSEO.

**Kyle Gaudreau:** But definitely want to make sure we aren't, you know, we're moving relatively fast with this.

**Kyle Gaudreau:** And so, you know, if we can get something live in like, say, March, you know, at the latest, that would be probably a good ballpark like timeline to the group home.

**Dhruv Amin:** Okay.

**Dhruv Amin:** Sounds good.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Awesome.

**Katya Luscomb:** Let hop back in here.

**Katya Luscomb:** The one other thing that I kind of wanted to flag just in case, I think Kyle mentioned it a bit in terms of like PSEO and us just kind of being able to take the reins and execute.

**Katya Luscomb:** Noticing, like, really appreciate.

**Katya Luscomb:** The super constructive calls and things we have.

**Katya Luscomb:** And curious if there's a way for us to maybe support communication like in Slack to help with any like fast-paced decisions that we need to make to kind of execute rapid fire on some different elements.

**Katya Luscomb:** Yeah, curious how you guys are feeling about Slack communication and if there's something that we can do there to help push anything through when we need decisive action or where we can maybe jump in and help take the reins in certain areas.

**Dhruv Amin:** I can be more responsive on Slack, comment-wise, on things as well.

**Dhruv Amin:** It helps sometimes if, let me just look at our last couple of comms.

**Katya Luscomb:** Yeah, certainly not wanting to put it all on you, mostly trying to make sure that we're communicating in a way that is most helpful for you and your team as well.

**Dhruv Amin:** Yeah, I mean, I think the update has been, I think we've like moved away from...

**Dhruv Amin:** From, from, sorry, I think I missed giving you guys, I got you at the sanity API key, should have given you, dub was not set up then, and so I should have just followed up.

**Dhruv Amin:** And then website migration, I kind of just gave you the quick thoughts, which is like, after I'd done that analysis of like canonical versus not, and I think we got pushed back.

**Dhruv Amin:** But you can feel free to tag me if you need a decision on like, this will change this or that.

**Dhruv Amin:** I probably could have missed here on my part, and I'm sorry guys, because it's been like, yeah, the canonicals are an easy fix, and then we'll rip the band-aid at some point, but only question is, yeah.

**Kyle Gaudreau:** Yeah, makes sense.

**Katya Luscomb:** All good.

**Kyle Gaudreau:** Sweet.

**Kyle Gaudreau:** Yeah, we can keep that in mind.

**Kyle Gaudreau:** Hope the event goes well today, it sounds like you guys have a lot of people showing up.

**Dhruv Amin:** Yeah, it'll be fun.

**Dhruv Amin:** It'll be nice recruiting, and then kind of fun to do something a little bit different.

**Dhruv Amin:** So thanks, guys.

**Katya Luscomb:** Yeah, appreciate the time.

**Kyle Gaudreau:** Well, sometime in the not-too-distant future, Dhruv, we should have you over in the office over here for lunch, or we can come over there or something like that.

**Dhruv Amin:** So, you know, Marcel and I are local, so we should make that happen sometime soon.

**Dhruv Amin:** That'd be great.

**Dhruv Amin:** Yeah, I'd love that.

**Kyle Gaudreau:** Are you guys, where are you guys in the city?

**Kyle Gaudreau:** We're just by South Park.

**Kyle Gaudreau:** So, like, the entrance to South Park is, like, right behind our office.

**Kyle Gaudreau:** We're on Federal Street, 2nd and Federal.

**Kyle Gaudreau:** So we have a pretty awesome space here.

**Kyle Gaudreau:** But, again, we're always happy to come by you guys.

**Dhruv Amin:** I know you're busy, so.

**Dhruv Amin:** Cool.

**Dhruv Amin:** Yeah, we're right by Union Square outside of Marcel.

**Kyle Gaudreau:** So, love to have you guys.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Awesome.

**Kyle Gaudreau:** Awesome.

**Kyle Gaudreau:** All right, appreciate the time, Dhruv.

**Kyle Gaudreau:** See ya.

**Kyle Gaudreau:** Have a good one.
