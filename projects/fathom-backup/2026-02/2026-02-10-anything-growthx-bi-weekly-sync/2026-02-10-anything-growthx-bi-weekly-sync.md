# Anything <> GrowthX - Bi-weekly Sync

<metadata>
date: 2026-02-10
time: 21:29 UTC
duration: 37 minutes
organizer: team@growthxlabs.com
participants: Dhruv Amin (Anything), Kyle Gaudreau (GrowthX), Zaria Zinn (Anything), Katya Luscomb (GrowthX)
fathom_recording_id: 121375782
fathom_url: https://fathom.video/calls/561182209
share_url: https://fathom.video/share/e3g-An-XmGWYY1NijWdxpsnEnEkbD14r
source: fathom
enriched_on: 2026-02-27T18:31:50Z
</metadata>

---

## Summary

Anything and GrowthX aligned on a two-phase website migration strategy to consolidate SEO authority by moving to anything.com, reviewed programmatic SEO (PSEO) plans targeting mobile app builder keywords with a 50–100 page MVP, and introduced Dubb as a new content attribution tool to track revenue signals from content performance.

---

## Context

This bi-weekly sync brought together the product and content teams from Anything (Dhruv Amin, Zaria Zinn) and GrowthX (Kyle Gaudreau, Katya Luscomb) to align on technical and strategic initiatives. The meeting focused on resolving a critical SEO headwind caused by domain fragmentation, which has suppressed non-brand homepage traffic by 10% over six months. The team also discussed a new content strategy using programmatic SEO to capture long-tail keywords and expand traffic potential through a template-based approach.

---

## Relevance

- **Product Strategy:** Website migration affects product visibility and organic growth for Anything; two-phase approach balances risk with authority consolidation.
- **Content & SEO:** PSEO initiative represents a major tactical shift toward scalable, template-based content production; potential 50–70k monthly visitor gain depends on MVP execution.
- **Attribution & Analytics:** Dubb integration enables revenue-driven prioritization of content versus traditional traffic metrics; directional data guides faster decision-making.
- **Execution:** Clear ownership and action items assigned; Dhruv's increased Slack responsiveness reflects commitment to faster iteration cycles.

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

**Dhruv Amin** (Anything)
- Set canonicals to anything.com on homepage + docs; then monitor daily and schedule DNS 301s

**Kyle Gaudreau** (GrowthX)
- Create Dubb sitelinks folder for GrowthX; then review Dubb attribution + request sitemap poll if needed
- Validate mobile app builder search volume; then scope PSEO MVP (50–100 pages) + share timeline/cost w/ Dhruv

---

## Transcript

**Katya Luscomb:** Hey.

**Kyle Gaudreau:** How's it Your background's always funny. Maybe I'm just used to yours.

**Katya Luscomb:** Uh-huh.

**Kyle Gaudreau:** Is it the way that you can't see you?

**Katya Luscomb:** And then you just appear? It's probably because my video always starts off, and then I turn it on when I come in, and the first thing to load is the background, so it looks like I'm a ghost.

**Kyle Gaudreau:** Yeah. It's like a neat parlor trick.

**Katya Luscomb:** Got to throw a little magic in there every once in a while, right?

**Kyle Gaudreau:** I've never met in person, so, you know, what's to say?

**Katya Luscomb:** I could just, yeah, I could just be a ghost.

**Kyle Gaudreau:** I could just be an AI twin.

**Katya Luscomb:** Uh-huh. Oh, that'd be pretty wild. My husband teases me sometimes that I sound like AI. And so when I got work, like when I started getting into AI content production, yeah, it was not very nice when he told me that. But yeah, that was pretty good. Hi, how's it going?

**Zaria Zinn:** Hi, good. How are you?

**Katya Luscomb:** Good, thanks.

**Zaria Zinn:** How's your week been? It's been good so far. We have a big event tonight at the office that we're hosting. We're doing a women in AI happy hour. So we're about to have like 200 people in the office.

**Katya Luscomb:** So we're like, getting everything ready for that. Yeah, yeah.

**Kyle Gaudreau:** exciting.

**Katya Luscomb:** Sounds like a big day for sure.

**Zaria Zinn:** Yeah, it'll be fun. We've done two of them before, but the last one is last year. This is the first one in the new office. And this one's like twice the size as the other one. So it'll be fun.

**Kyle Gaudreau:** I've been meaning to ask, where are you guys based in the city?

**Zaria Zinn:** Because you're in the city, right? Yeah, we're right by Union Square, kind of by like the Gates of Chinatown.

**Kyle Gaudreau:** Okay. Okay. We're over by South Park.

**Zaria Zinn:** So South Park is kind of just like right back here. Nice. Yeah, yeah. So not too far away, I suppose. Yeah, not far at all.

**Katya Luscomb:** Hey, Drew. How are you?

**Dhruv Amin:** How are you guys doing?

**Katya Luscomb:** Good. Thanks. Are we going well so far?

**Dhruv Amin:** Yeah.

**Katya Luscomb:** Awesome. Cool. Also, thank you guys for your flexibility in moving stuff around. I know we had to finagle meeting times a little bit. But really primarily wanted to make sure we had some time to connect and talk about migration. And then we've got a PSEO strategy to go over as well. So a couple different things. We've got performance overview we can go over. A lot of what we're noticing relates back to really wanting to align on a decision around the migration. Big picture, we're starting to see some headwinds week over week that we see as pertaining to the migration. Before I get too, too far in the weeds... Do you have initial thoughts, gut reaction? Because I know we've sent a couple of messages around migration pieces.

**Dhruv Amin:** Yeah, sorry. So I actually did some initial cloud code analysis with having it do, where was this, post your message. Sorry for not responding in Slack. Um, basically, I think what we do is canonicals, um, across the board, let's do, uh, anything.com. Um, thanks for calling out that the homepage is not there, um, on when to do this traffic spike, uh, changeover. It's going to end up being anything.com at any given time. I'm, I, I could basically see from the, like search console and post hog and a bunch of other things as well. Um, let me see if I can get this in view form, um, from our internal data that. But you know, the other ones are basically, I guess I ran this a week ago, you know, AI's recommendation was like, you know, 301 redirects, but like four to six weeks recovery is like probably optimistic. It's probably going to be like three to six months. It also picked up by looking at RREFs, like the same data you guys are looking at as well in terms of like backlinks and also momentum kind of finally shifting over to create anything. And then we just changed in December. It was interesting seeing it, seeing it basically also look at the create X, Y, Z traffic, which is that like finally it seems like the create X, Y, traffic is actually dropping. And so that's actually not a huge amount of like lift. And then the question is if keeps dropping and you migrate too late, like what's the, what's the like relative issues? And then, yeah, anything, create anything is overlapping with anything by keyword overlap. So my honest take is that the biggest thing we're going to feel is, so I'm trying to remember when I looked at this. The biggest thing we're going to feel is, what was the, I guess we're like already pretty low in January. Like we're dropping in like overall Google organic traffic.

**Kyle Gaudreau:** Yeah, so like right now it's basically happening because I just started jumping. I've been digging into it as well. Like it's, to your point, really shifting to create anything. Anything's picking up a bit, but it's like pretty small. Part of that is like the mixed signal and like so much of your traffic goes to your homepage, especially in a non-brand.

**Dhruv Amin:** Like that is still like the lion's share of your non-brand traffic.

**Kyle Gaudreau:** So what's basically happening there, if you like back it out over several months, it's like best case you're flat over like six months to non-brand to the homepage. Worst case, trending down 10%. So not like massive, but at the same time, it's like how much headroom do you have for growth in that? And the fact that it's like that split signal of that homepage pointing to one domain and then your blog pointing to another. It's like. That separation of authority that's creating a bit of noise. And so, yeah, I think there's a fair argument to be made to what you're getting to is the canonicalization approach to just pointing the homepage to anything. It's certainly a slower path. It's hard to say one is necessarily right or wrong, honestly. The variable is just the three domain effect. Part of the logic I have been applying, but again, like I can't say this for certain, is like I tend to think about it less, like over a three-month period, what drives the most aggregate growth? My assumption that I'm operating based off of us doing other migrations is that the 301 redirect approach kind of has the rip the band-aid. may lead to, you know, that four-week, but in the aggregate over three months, it's maybe higher growth overall. But I cannot say that for certain, like no migration is always going to perform the same way. mean, as I... I think I mentioned in the past, like, I think this is, while I've done many, many migrations, I haven't done one with a three domain layer to it in this way. So anything I would be saying would be presumptuous. So I would say, like, the canonical is, like, a fair argument to say it's the safest.

**Dhruv Amin:** Yeah. I looked at some other, like, case studies of, like, things as well. And, like, the migrations. So, yeah, I don't know. I was looking at, like, the average to actually get back to, like, similar traffic. I don't think it really matters because I, my honest take is that all homepage traffic is, like, when you're seeing these big, like, homepage ramps through the end of the year, you're basically seeing the effect of, I'm sorry, it's a little bit different because, like, Google organic traffic, I don't know how Google overcounts why it's so much overstated from what we actually see in post-hog on, like, raw numbers. I think your post-hog has attribution issues when it comes to down to the channel level. Because you. you. You have a lot that just falls into unattributed. Got it. Yeah. So the refer might be not being captured in the Google thing as well. I guess what was this looking at? This was looking at like from post-hog, page view, path name, slash, and then I probably did a cut in the query on like whatever was direct Google-ly attributed. But like the traffic is mainly driven, like the growth in traffic in Create Anything through this time period is mainly the result of other off Google marketing efforts. It's not anything else. So my feeling is if we just move the canonicals right now, now the fact that traffic is declining across the board is probably the result of in January pulling back on marketing spend. But like if we switch the canonicals to anything and then, yeah, the question is like when to do the 301s and probably soon. But I think at the very least, like we should just have everything on the site pointing towards anything. then, yeah, and then at some point we'll rip the banion I don't know when the right quote-unquote time to do it is. I'm expecting that that's a like 20%, potentially more catastrophically if anything's not big enough traffic. But my hope would be that like Zaria, all of the marketing stuff you're doing towards anything is just building up anything's traffic and not like not the other one's traffic.

**Kyle Gaudreau:** Yeah, think that's valid. Like, you know, what you talked about, about that sequential approach of canonicals to 301 is a fairly common practice. So, yeah, I think if you can, right now you have your sitemap pointing to anything, even though that is a little bit weird, but I don't think that's a huge deal that each one says anything URLs. Your blog's pointing to anything. If you just switch the homepage to point to anything.com, that I believe is the fix. can't quite recall what your docs is pointing to. I feel like it's anything, but also. So your docs doesn't generate a ton of organic search traffic either. Yeah. So it's primary the homepage is like the main action here is a long way of saying.

**Dhruv Amin:** Yep. Okay, let's do that. And then just like when we're going to do the 301s, I don't know, but it should be pretty easy. Yeah.

**Kyle Gaudreau:** one thing I wasn't sure about is, is there any complexity given the way you have it built in a single app? Like, is there any reason that you would have, there'd be complexity of like having two domains point to one where that one doesn't have the redirect on it, you get what I'm saying?

**Dhruv Amin:** No, because the way we would implement 301s would be at the DNS level. At the DNS, okay, So that we, so that we end up getting like perfect, like every single page that was historically like a duplicate would be done. And then the core web app would be, would be fine. It's just that like, and actually like today for the most part, that is the way it works. So if you actually look at. How the site works, you land on a homepage that is like create XYZ or create anything. But then the moment you sign in, it redirects you over to anything land. And then the one other thing that like maybe it does respect like whatever you are currently, like whatever you route from. So like to which you're like already a login user and you're like, hey, I'm like going to go into a create anything link. You'll go to that link, but that's it.

**Kyle Gaudreau:** Yeah. Okay.

**Dhruv Amin:** Fair enough. Yeah.

**Kyle Gaudreau:** Yeah, so I think that like if possible for you all to make that canonical change ASAP, that's the main thing I think slowing us down. And we can just continue to look at it daily and see.

**Dhruv Amin:** The homepage is the only one that you caught?

**Kyle Gaudreau:** Correct. I mean, let me just since we're live, just double check the docs. But again, like the influence there is minimal. Yeah, it's a little weird that. So, yeah, on your docs, what you have is canonicaling to the XYZ site.

**Dhruv Amin:** I think I fixed that, but let me just make sure. Okay, should we talk about the, thanks so much, thanks for stepping up the article content. One other thing I think you guys might like or use, there is, what's the right email to invite to this?

**Katya Luscomb:** Team at growthxlabs.com.

**Dhruv Amin:** Okay, here is, um... Okay, one second. We'll give you everything you need. Okay. So I invited you guys. In Dubb, this just heads up. So it's generally short link attribution tracking. We're experimenting with, so like this number is not accurate, but it is directional. And I'm trying to figure out exactly why it's not like 100% accurate, but in the ways that it's not accurate should be inaccurate across everything. So I think that's fine for what the purpose is. Basically, it's a short link creator for other marketing campaigns. We usually use go.anything.com, and then they mirrored basically every domain. um, on site.anything.com, um, and then the route. So, um, and then what it will typically track is downstream, um, clicks, which in the site tracking case is typically views. Um, you can imagine it rather than clicks. It's like someone who actually like went to that page and looked leads, which is like a cookie set on the user's device. And then long-term, if they sign up later, that's it. So like one reason I might be depressed is like, you know, 40% of the internet uses some sort of ad blocker or a browser that doesn't have a cookie set. So like, that's it, but it gives you a directional sense of like, okay, how many, how many signups did this content drive at any point? And then, um, ultimately sales, um, of like, is this content particularly, really good? So I think it's a faster way for you guys to prioritize content early signals on, Hey, is this actually driving like revenue, um, beyond just like, is it getting ranked? Obviously has to rank in order to, and get views to even have a shot. Uh, uh, But then downstream, I don't know, maybe there is content that's extremely deep and interesting and good from a sales perspective, but is not necessarily when we're in an early growing SEO authority going to actually be super high from a traffic level. There's these folders called sitelinks. Feel free to make whatever folders you want for the GrowthX content as well. It should be pretty fast to do a script if you guys know all of your canonical URLs that you guys have already done. so we can just look at GrowthX content under the hood. And then, yeah, just pay attention to sitelinks. I think it's automatically captured. One heads up is that this pulls from sitemaps. And I did the last poll last week. Right now, they have to manually run that poll, but they're working on just a daily cron that gets it from the sitemap. And then I think the blog sitemap is updated daily anyway. So soon it will be live, but to the extent to which you guys look at this initial cut and are like, interesting, these URLs are like, these blog posts are doing well. Now we're going to go make a bunch of content changes with that data on sales and then want a new poll. Just let me know. Any questions on that?

**Kyle Gaudreau:** Yeah. Yeah. Just to make sure I'm interpreting it correctly, users, if in a scenario where a user is blocking cookies, are you also not getting the attributed sales alongside of that? Because, I mean, like, you know, on the one hand, there is a thinking about this from like a session view standpoint. And then there is obviously a multi-session view where the cookie, you know, comes into play. But in a single session, if they're blocking cookies, are you not getting that revenue attributed to like a page?

**Dhruv Amin:** This is operating on last touch attribution from anything that. Sends a go link or drops that cookie. So in some ways, you might pick up more attribution if you get a user who reads a blog post and then doesn't convert then, but then sees some launch and then comes back. It's a multi-channel. It's very hard to actually get. But the reason I'm saying it's directional, not like take it as like fact of like we drove this, is that there's just, if you like think about attribution, there's just a million things that start cutting people down. And so I still think it's like just, I think it's like the signal it gives you on top of traffic, which we can see traffic is just like, well, is any of this blog content actually leading to any sort of like conversion? If we start standing up programmatic landing pages as well, like dedicated landing pages to certain types of funnels, it could like, it would also be, it would also be a really fast way to see that, which is like, I always set up dedicated landing page for building an app. For hospitals, you know, and that actually is a lot of conversion.

**Kyle Gaudreau:** Makes sense. Cool. Yeah, we'll dig in. I'm sure we may have some follow questions, but yeah, I'm sure there's also some things we can figure out from their docs to figure out what we need. So yeah, better posts would definitely be helpful.

**Dhruv Amin:** Cool. Yeah, I think it just saves the question that we were talking about two weeks ago, which is, you know, we have GSC data, which has clicks in Google, and then we have like really annoying joins. It should just make it really automatic to, in post-hog, to the revenue thing. That's all this does. It just likes, it just very quickly gives you revenue stats off of content.

**Kyle Gaudreau:** Makes sense. Cool.

**Dhruv Amin:** Should we talk about the programmatic?

**Katya Luscomb:** Yeah, jump right in. Let me open it up. Hang on. I'm sorry. I only shared... I hate it when Zoom decides that it is going to dictate what screen shows up. All righty. So there's a couple different layers to this strategy that's outlined. The idea is that we would operate in phases to build it out over time. And the core idea is looking at how we can break down programmatically different types of app development and then build out content from those topic areas on those various types of apps. So one of the things that we looked at was like different verticals that have a variety of volume that we could make some strategic bets on that could potentially drive a lot of traffic. Looking at, you know, there's quite an extensive amount of volume and opportunities here that we can build out, as well as some long tail opportunities that can continue to enhance that. And, you know, obviously with PSEA. So the idea is that this would be really templated so we could build out like an exact formula and just execute across all these different verticals as we really get things dialed in. Kyle, anything specific that you wanted to call out in this piece?

**Kyle Gaudreau:** So, you know, we've purchased in a variety of different ways for different customers. You know, we have some fortunate to have some folks who have built some pretty badass PSEO programs in their past. And one of which also leads our kind of an aspect of our engineering team that focuses on the client side. And so what we can do with them is, you know, with some of our customers, we can get access to like, say, repos and then other places where we can source data from, align with you on the template. And then really just start to jam fairly fast on this. The mindset is like trying to create a bit of like a web semantically of different layers. And so where that... Back and go is, you know, eventually we could do things around like you start with like the broader industry, vertical, whatever, and then we could build into things like app teardowns and like how you would build this and what is their model and just like people who are basically exploratory. Like I'm thinking about building this thing and it seems like there's a variety of different intents out there in and around that that aligns with what you all do. There's a variance we could also explore around, you know, build an app like X or similar themed like variants. And so essentially it's like the key here and we were going a little bit back and forth of the right like URL structure and I think that could evolve over time. But essentially it's like trying to find that right URL structure where you're creating that nice semantic web, but also not creating all these like crazy nested folders. And so there's aspects of this in the site architecture, which is basically just trying to. To think of like how do you not create too many folders and use things like tags as well that kind of like so you could think of rather than putting everything that fits under healthcare under that healthcare URL, you can more treat that as a hub page and then you can tag different apps that fit under healthcare to that later on. And then if you were to click on those tags, would go to that healthcare page and so you're not like putting it under the same URL structure, but you're creating a lot of that internal linking in and around that in a really repeatable way. And so it's a bit of like, how do we fit these different Lego pieces together? And like, for me, the key to always making this work is as well as possible is like, it's one thing to talk about like the high level strategy, you know, the types of keywords we're going after. Obviously, this is an SEO play, but user experience should really be the main driver of this for it to really work well. We can... Find that right user experience that's truly useful for the type of intent that is out there, and we can address that in a repeatable way. Like, that is when programmatic really works well. We don't want to fall into this trap of, like, really thin pages. Like, Base44 is doing this a little bit. It's okay. Okay is pretty generous. It's very thin. It's doing okay. That's not a model we want to replicate here. But first, it's, like, thinking about, like, what is the core, like, step one that we build around and kind of thinking around first that vertical hub section is where to start, and then we can layer it in some of these other bets later on. And naturally, this could evolve in different directions as we have more data to supplement, like, what's working, what's not. So, there's definitely other plays we could explore, but, like, you know, just trying to think about blending the different things we've heard from you and what could drive some conversion. There's some search volume and relevant intent around this. This was one of the primary that came to mind. As far as next steps on something like this would go, you know, of course, we would love your feedback of, like, where does this hit the mark, not hit the mark. We can more bring this to life visually, get your team's feedback on that. We would need to think about, like, how do we scope something like this and, like, what is the actual need for what we're building? And so, as you can imagine, like, there can be wide varying degrees of complexity for some of these efforts. Some of them were, like, we did something for Airbyte recently that was, like, pretty fast to get going and relatively low complexity. But we have done some things that are super, super high complexity. It is not uncommon for us to do this end-to-end. So build the web experience, you know, align with you on the design needed and build that out. But some teams want to take that on. I'm guessing, you know, with you all being busy, you know, if you're bought into a strategy, you know, what that Cost, et cetera, that, you know, my assumption is you'd probably want us to do that and then just be able to sprint and run and like have, you know, updates on performance and like how we're pivoting strategy and get your feedback, you know, here and there.

**Dhruv Amin:** Okay. So this, yeah, I mean, I think if we feel like all really good about like whatever the strategy is and like decent confidence that like it's worth investing in both at like our current domain authority and that we think the queries are pretty aligned, this should be pretty fast to like just the raw blocking and tackling of pages. Now, like it depends on how much content is actually on those pages. I think that's where honestly the GrowthX help would be most helpful is honestly in just generating, especially if we're going to start doing this at scale, you know, this like long tail of app creation, builder landing pages is like on the mind of like, even if all you did. Let's just take our homepage, reskinned it with better H1 and H2, and then had the same prompt box get going with maybe a pre-filled prompt.

**Kyle Gaudreau:** That's essentially what Base44 seems to be doing.

**Dhruv Amin:** I think Lovable did a similar thing, and you just have long tail queries. It's fine. I think the question I have is, I've sometimes seen slightly more, to your point on a good user experience, when you actually go through the app, a slightly more innovative one. One data point that I just read was that when we compete on Google Ads for Web App Builder as traffic, it's extremely, I don't know, competitive and also doesn't convert that much. But when we compete in the mobile app builder category, there's where our conversions are so much higher and the cost per click is so much And I can't tell if that's just because no one really goes to Google and searches for mobile apps. just go straight to the app store and search for mobile app builders. But I could imagine an SEO play that was like, I don't know, we just take all the top-ranking apps in the app store. And then we build a beautiful page about what the app is, how many downloads it gets, how you would actually build it. And then like a one-click build in anything that would like, you know, build a custom prompt and like, and like kick you into the builder with like a mobile app. And that'd be interesting. Or like I saw Devin do, I think they did like an NPM package registry, which was like a, but what they tried to like connect their Devin agent to it so that the agent could then explain to you, like we would just generate like on the fly how to use that package. And for Devin, it was like clearly a play to go after kind of like the long tail of devs. And I don't know how effective it was at actually going after every single NPM package. But I. wonder, is there, like, is there, like, unique tie-in to app building that's, like, maybe that can hit scale or we can make the pages seem really interesting that's, that's, that's, that's maybe, like, I don't know, harder, easier to go through. I don't know how much search volume there's on mobile app building when I first kind of, like, started, like, thinking about that idea. I think we're, I think we're thinking similarly.

**Kyle Gaudreau:** It's, like, just different kind of versions of, like, because I was thinking there would be an aspect of that to this. It was a bit more, like, where does that get introduced into the mix? I did explore a little bit around search volume around that, but I didn't probably go as deep on that, so I can validate that a bit. But to the, to the fit to, you know, you've been talking about this being a key wedge for you all, you know, I can certainly see that being a play. And, I mean, at the end of the day, like, these things can work super well to, like, find the happy medium of what is light lift. It high impact and like, what is the right way? Where can you fall into that spectrum? Like, again, we don't want to create like very thin content that's a user experience. But if we can find that right balance of scale and value, yeah, something like what you're walking through could certainly help here. So I think it's similar. Like, this would be like different things that we could add in around that just to kind of almost build these mini microsites around these in different layers over time. But it's just what is that right starting place to build around first? Certainly, you know, focusing on like, how do you build this or like, you know, two different popular mobile apps that it does kind of lead more into like that, like teardown mindset that we had within here. Yep. But yeah, I do like that. I do like I can do a little bit more research around that to see how that what's possible. The next step then for me to internally would be working with our Engineering team, just to kind of like scope this out a little bit further, how we would kind of plug in our systems with your systems. And then we can kind of talk about like relative timeline cost and things like that. Related to the migration piece of that, this is something to like think about for sure of like how much scale to throw out there. How we can approach that though is just kind of like if we get something, an MVP out that isn't too heavy lift, just figuring out that right scale of that first experiment. You know, for example, like don't start with like 2,000 pages. It's more like start with like 50 to 100 ballpark or something of that effect. And then closely monitoring like how quickly are these getting indexed? Are they actually getting the kind of queries we want to see? What are we learning from that? If we see some good signal, then we can just continue to like open. That volume up more and more is typically how we would think about it.

**Dhruv Amin:** Yep.

**Kyle Gaudreau:** So certainly like doing that alongside the editorial and then also finding different ways we can weave these two things alongside each other, internal links, things of that nature should help from like a topical relevance standpoint. But also I would probably have higher conviction in these things, this PSEO play driving conversions for you. It's important.

**Dhruv Amin:** Okay. Do you guys, have you guys seen like total, like, like what is the, what's the size of prize we're going for? Like in any of these where like, like grab a rough cut, like, I saw this in that notion doc.

**Kyle Gaudreau:** Yeah, there's some at the bottom here, but I think this, yeah, like we would need to like dig in a little bit more to add some other layers. Katya, if you could scroll to the bottom, I have some of that down here, but I think this is probably on the conservative side. Um, so like, you know, if we're adding in. All layers, like just thinking about it, like it does feel like a little on the conservative side, I probably like put it more like 50-70 range, but it could certainly grow beyond that on like a aggregate monthly basis. But we've certainly seen players that can get well above that, like 2x plus over that, but that certainly takes some time. Like typically when you're going to get to that range, it's going to be like six plus months of a pretty high domain authority site. And the delicate balance here is like we want to be really aggressive, but we also want to, again, make sure this isn't super thin content. We want this to be sticky results. So it's always about like how hard can we hit the gas and like maintain what we're building.

**Dhruv Amin:** Yep.

**Kyle Gaudreau:** So I can, I'm happy to take some of that back and like let you know. So... What I have in addition to how we may modify the plan, I'll circle back internally with the team. And then we can talk about like roughly like how we would think about pricing this out. Because generally, you know, like we have the editorial layer that is a bit of a different motion than the PSEO. But definitely want to make sure we aren't, you know, we're moving relatively fast with this. And so, you know, if we can get something live in like, say, March, you know, at the latest, that would be probably a good ballpark like timeline to the group home.

**Dhruv Amin:** Okay. Sounds good.

**Kyle Gaudreau:** Cool. Awesome.

**Katya Luscomb:** Let hop back in here. The one other thing that I kind of wanted to flag just in case, I think Kyle mentioned it a bit in terms of like PSEO and us just kind of being able to take the reins and execute. Noticing, like, really appreciate. The super constructive calls and things we have. And curious if there's a way for us to maybe support communication like in Slack to help with any like fast-paced decisions that we need to make to kind of execute rapid fire on some different elements. Yeah, curious how you guys are feeling about Slack communication and if there's something that we can do there to help push anything through when we need decisive action or where we can maybe jump in and help take the reins in certain areas.

**Dhruv Amin:** I can be more responsive on Slack, comment-wise, on things as well. It helps sometimes if, let me just look at our last couple of comms.

**Katya Luscomb:** Yeah, certainly not wanting to put it all on you, mostly trying to make sure that we're communicating in a way that is most helpful for you and your team as well.

**Dhruv Amin:** Yeah, I mean, I think the update has been, I think we've like moved away from... From, from, sorry, I think I missed giving you guys, I got you at the sanity API key, should have given you, dub was not set up then, and so I should have just followed up. And then website migration, I kind of just gave you the quick thoughts, which is like, after I'd done that analysis of like canonical versus not, and I think we got pushed back. But you can feel free to tag me if you need a decision on like, this will change this or that. I probably could have missed here on my part, and I'm sorry guys, because it's been like, yeah, the canonicals are an easy fix, and then we'll rip the band-aid at some point, but only question is, yeah.

**Kyle Gaudreau:** Yeah, makes sense.

**Katya Luscomb:** All good.

**Kyle Gaudreau:** Sweet. Yeah, we can keep that in mind. Hope the event goes well today, it sounds like you guys have a lot of people showing up.

**Dhruv Amin:** Yeah, it'll be fun. It'll be nice recruiting, and then kind of fun to do something a little bit different. So thanks, guys.

**Katya Luscomb:** Yeah, appreciate the time.

**Kyle Gaudreau:** Well, sometime in the not-too-distant future, Dhruv, we should have you over in the office over here for lunch, or we can come over there or something like that.

**Dhruv Amin:** So, you know, Marcel and I are local, so we should make that happen sometime soon. That'd be great. Yeah, I'd love that.

**Kyle Gaudreau:** Are you guys, where are you guys in the city? We're just by South Park. So, like, the entrance to South Park is, like, right behind our office. We're on Federal Street, 2nd and Federal. So we have a pretty awesome space here. But, again, we're always happy to come by you guys.

**Dhruv Amin:** I know you're busy, so. Cool. Yeah, we're right by Union Square outside of Marcel.

**Kyle Gaudreau:** So, love to have you guys. Bye. Awesome. Awesome. All right, appreciate the time, Dhruv. See ya. Have a good one.