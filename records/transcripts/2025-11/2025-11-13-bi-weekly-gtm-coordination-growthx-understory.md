# Bi-Weekly GTM Coordination — GrowthX & Understory

<metadata>
date: 2025-11-13
time: 19:31 UTC
duration: 46 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Alex Fine (Understory), Mark Lim (Understory)
fathom_recording_id: 101545897
fathom_url: https://fathom.video/calls/472885475
share_url: https://fathom.video/share/zV_UcKs6sz8w8ibjLWhs9wXspMRvB7-p
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

GrowthX and Understory reviewed strong GTM performance—LinkedIn outreach exceeded benchmarks (30 replies, ~20% acceptance/reply rates) and email generated 63 opportunities in two weeks—then aligned on an evergreen community campaign to convert prospects using a free month trial. Mark Lim will build a new Clay automation to replace SIFT, enabling advanced lead segmentation by source for personalized messaging across HeyReach (LinkedIn) and email. Understory committed to creating community content showcasing pre/post engagement metrics from their GrowthX engagement, positioning tactical GTM engineering insights as high-value membership content.

---

## Context

GrowthX recently launched a member community on Circle ($30/month, waived setup fees) and achieved 140 paying members in days, validating the business model. Understory (a GTM and AEO services partner) is collaborating on content and co-marketing to drive membership. Both teams see the community as a scalable lead-gen and product flywheel—a free-month promo paired with targeted outreach to community members, event registrants (Profound, AirOps, Pavilion, Exit 5), and competitor followers. The meeting focused on optimizing this motion, improving the lead-processing automation, and defining content strategy for the partnership.

---

## Relevance

- **To GrowthX Business Development:** Community achieved 140 members ($30/mo, ~$4k MRR) in days with strong unit economics (~$20 ACQ). Free-month trial offer is converting Lovable webinar responders. Expansion opportunity: B2B seat licensing (e.g., 5-seat teams at bulk discount) with large accounts. Partnership with Understory provides SEO/GEO validation content and co-marketing to qualified GTM audiences.

- **To GrowthX Delivery:** Evergreen campaign automation (Clay) replaces SIFT for superior lead segmentation, enabling source-based personalization and multi-touch workflows. New architecture ingests LinkedIn signals (post engagers, comments, profile views, new followers) and enriches ICP fit (country, industry, company). Segmented messaging increases reply rates for both HeyReach (LinkedIn, high-intent) and Instantly (email, high volume ~10k/week).

- **To GrowthX Sales Motion:** Community becomes demand-generation engine: webinar recording → free month → paid member. Lovable workshop (Dec) and Webflow partnership completed; new integrated content from Understory (pre/post dashboards, tactical GTM engineering) drives engagement. Team scaling production capabilities (thumbnails, video, copy) via Braze agency partnership.

---

## Overview

- **Community Growth:** GrowthX's new community has grown from 70 to 140 paying members ($30/mo) in days, validating the model.
- **New Campaign Strategy:** An evergreen campaign will drive leads to the community, using a free month trial to convert prospects.
- **Automation Overhaul:** A new Clay automation will replace the current SIFT setup, enabling advanced lead segmentation (e.g., by source) for personalized messaging.
- **Partnership:** Understory will create content for GrowthX's community, showcasing SEO/GEO results and offering tactical GTM engineering insights.

---

## Key Topics

### GTM Campaign Performance

  - **LinkedIn (HeyReach):** Performance exceeds client averages.
      - **Connections Sent:** 758
      - **Messages Sent:** 139
      - **Replies:** 30
      - **Acceptance Rate:** \~20%
      - **Reply Rate:** \>20%
  - **Email (Instantly):** Launched Oct 31; 63 opportunities generated.
      - High deliverability (not landing in spam).
      - Strategy → Double down on the highest-performing copy.

### New Evergreen Community Campaign

  - **Goal:** Create a scalable, "always-on" campaign to drive leads to the new community.
  - **Offer:** A free month of community access via promo code.
      - **Rationale:** Directly converts leads instead of just offering a recording.
  - **Lead Sources:**
      - Pavilion, Exit 5, Profound, AirOps member/registrant lists
      - Competitor LinkedIn followers
      - Lists can be reused every \~2 months.
  - **Initial Test:** Offer the free month to the 60+ people who replied to the current Lovable webinar campaign.
      - **Action:** Jason will instruct Hesus to update the reply sequence.

### New Lead Automation Architecture

  - **Problem:** The current SIFT setup is clunky and lacks advanced segmentation.
  - **Solution:** Mark will build a new Clay automation to create a more sophisticated lead-processing engine.
  - **Workflow:**
    1.  **Ingest:** Webhooks from SIFT (post reactions, comments, profile views, new followers).
    2.  **Process:** Deduplicate against a suppression list (clients, competitors).
    3.  **Validate:** Extract country and industry to confirm ICP fit.
    4.  **Enrich:** Find contact info and emails.
    5.  **Segment:** Label leads by source (e.g., GrowthX content vs. competitor content).
    6.  **Route:** Push to HeyReach (LinkedIn) or Instantly (email) with personalized copy.
  - **Strategic Routing:**
      - **HeyReach (LinkedIn):** Higher response rates; reserved for high-intent leads (e.g., AirOps registrants).
      - **Instantly (Email):** Higher volume capacity (\~10k emails/week); used for broader campaigns.

### Community & Partnership Strategy

  - **GrowthX Community:**
      - **Platform:** Circle
      - **Model:** $30/mo + waived $150 setup fee
      - **Content:** \~70% of value is recordings, live sessions, and courses.
  - **Partnership:** Understory will create content for the community.
      - **Topics:**
          - "Pre vs. Post GrowthX" SEO/GEO dashboards.
          - Tactical GTM engineering insights.
      - **Goal:** Provide high-value content to attract and retain members.

---

## Action Items

**Jason Gong (GrowthX)**
- Set up 5-seat access for customer in GrowthX community
- Draft evergreen campaign copy w/ 1-mo free; share w/ Mark; Mark launches on targeted list
- Create 1-mo free promo code; send to Hesus to offer all 60 Lovable webinar responders; update Aziz reply template
- Email SIFT support re: improved filtering for LinkedIn listening automations

**Mark Lim (Understory)**
- Scrape Luma registrants (Profound, AirOps) by name; enrich; add to Clay
- Build Clay/SIFT always-on LinkedIn lead flow; de-dupe against suppression list; segment by source; add scoring; notify Jason to disable old workflows
- Add Pavilion member lists to evergreen email campaign
- Run AirOps registrant list via LinkedIn outreach (HeyReach)

---

## Transcript
**Alex Fine:** Hey, Mark.

**Alex Fine:** Are you saying something?

**Alex Fine:** Hold on.

**Alex Fine:** No, I think it's you this time.

**Jason Gong:** Okay, so it is you, Mark.

**Alex Fine:** I can hear Jason.

**Jason Gong:** How's it going?

**Jason Gong:** Good, how are you?

**Alex Fine:** I'm doing good.

**Jason Gong:** I finally got the community out the door and it's growing, you know, it's doing good.

**Jason Gong:** We have, how many, we have 140 paying members now.

**Jason Gong:** In one day?

**Alex Fine:** No, I think we had 70 at the beginning of the week.

**Mark Lim:** So, you know, last couple of days have just been like, that's amazing.

**Alex Fine:** All the time.

**Jason Gong:** And how much are you charging for it?

**Alex Fine:** We, I mean, we're discounting a little bit right now.

**Jason Gong:** I think people are paying, it's like 30 bucks a month.

**Jason Gong:** And then there's a upfront fee that we're basically like discounting to zero, but usually it's like 150 bucks.

**Alex Fine:** Okay.

**Alex Fine:** Very nice.

**Alex Fine:** It's almost.

**Jason Gong:** It's almost a third of a customer in an aggregate, but it seems much more scalable.

**Alex Fine:** Yeah, for sure.

**Alex Fine:** you can get that, I mean, when you think about Exit 5, would they have how many?

**Jason Gong:** They're crazy.

**Jason Gong:** I mean, I think they're like low single digit millionaire, I think, maybe like four or five.

**Jason Gong:** And they charge, I think they charge like a hundred bucks a year.

**Alex Fine:** They make a lot of money on speaking engagements and stuff like that too.

**Alex Fine:** Like I did a webinar for them and they asked me to do it for free.

**Alex Fine:** So I did it and we got a ton of booked calls from it.

**Alex Fine:** And then I was like, okay, this is so good.

**Alex Fine:** We need to do it again.

**Alex Fine:** It's like, how much is it?

**Alex Fine:** And they're like, well, we can give you a slot in a newsletter if you want for 7,500.

**Alex Fine:** And then if you want to do a webinar, it's 30 grand.

**Alex Fine:** And I was like, okay, wait, how big is their newsletter?

**Alex Fine:** I have no idea, but I just.

**Alex Fine:** I couldn't believe what they were trying to charge me.

**Alex Fine:** my God.

**Alex Fine:** Dude, should do something.

**Jason Gong:** I'm trying to figure out, like, a model that's, like, a little bit less work, you know, on our end.

**Jason Gong:** And we get to kind of, like, partner with people.

**Jason Gong:** So, like, we demoed one with Webflow that went really well.

**Jason Gong:** And now we're doing one with Lovable in, like, three weeks.

**Jason Gong:** I got punted.

**Jason Gong:** But let me do something with you.

**Jason Gong:** It'd be sick.

**Jason Gong:** I don't know what topic would be cool.

**Jason Gong:** I mean, honestly, just, like, everything GTM engineering, I think.

**Alex Fine:** Well, that and then something I'm actually planning to do, and this is not even something that, like, we've talked about in an arrangement or anything.

**Alex Fine:** I just think it's going to make for really good content is I want to share the dashboards of pre and post working with you guys on the SEO and GEO side.

**Alex Fine:** Because we are starting to see results.

**Alex Fine:** But there are nothing indicative of, like, ROI yet.

**Alex Fine:** But what we're seeing is increases in traffic from LLMs.

**Alex Fine:** We're seeing increases in traffic from Google as a referrer.

**Alex Fine:** So,

**Alex Fine:** We're seeing big-name companies like Meta on our website.

**Alex Fine:** So all kinds of really cool stuff like that.

**Alex Fine:** Like I said, nothing is actually ROI positive for us yet, like nothing measurable.

**Alex Fine:** But just seeing the uptick in at least visibility has been nice.

**Alex Fine:** So I want to make one month into working with GrowthX, two months into working with GrowthX, like that type of content.

**Alex Fine:** We'll promote the hell out of that.

**Jason Gong:** But I was thinking like, so like one thing we've been experimenting or I want to do is like the first experiment.

**Alex Fine:** It's this guy.

**Alex Fine:** I'm moving you to a bigger screen so I can see it.

**Alex Fine:** Because right now I have you on my teleprompter so I can look directly at the camera.

**Jason Gong:** Do you know this guy? He has a great series. I don't want to copy it, but he basically does kind of brand hijacking. He'll post something from a brand and screenshot it—like a CTA or pricing page formatted differently. His whole thing is A-B testing, essentially. We were going to do a webinar together, but it doesn't have to be that heavy. What he does is create content, and I have this tool that looks at all the previous iterations of a webpage to see what people have tested.

**Jason Gong:** And then he has this tool that goes and looks at all the previous iterations of a web page to see what people have tried to test.

**Jason Gong:** And it's like, you know, if you go to, like, HubSpot's blog page and looked at that for the last 10 years, like, you'll probably see just, like, all the insane experiments they've run to, like, try to improve conversion, you know?

**Jason Gong:** And it'll just be, like, this really tactical thing.

**Jason Gong:** Like, it's not super big or super vague.

**Jason Gong:** It's just, like, hey, if you want to improve conversion, here's the resource in our community for you.

**Jason Gong:** And then, yeah, I mean, think the interesting part is, like, we get to put a little piece of that behind the community paywall.

**Jason Gong:** Like, maybe it's, like, charity.

**Jason Gong:** Right up for most of the video, and then I want to make that the flywheel for people joining the community.

**Jason Gong:** So what do you guys actually do in the community?

**Alex Fine:** Is just going to be like a Slack channel where people can have conversation and you guys are posting?

**Jason Gong:** It's a good question. I want to say, like, everything's still flexible. You can still shape it.

**Jason Gong:** But I would say the community is probably, like, 70% content-based.

**Jason Gong:** So we have, you know, recordings of previous workshops that we've done.

**Jason Gong:** We have live work sessions. This is the app—Circle. Exit 5 runs their community on Circle as well. So we have live build sessions, like building an app with Lovable.

**Jason Gong:** This is me just, like, writing content for 40 minutes, like, with ChatGPT.

**Jason Gong:** We have these podcasts.

**Alex Fine:** Who's making your thumbnails?

**Alex Fine:** What else?

**Jason Gong:** We have a designer, they're the same ones that are making pieces of your website. They're called Braze, and they essentially work full-time for us. They have a designer and one or two devs.

**Jason Gong:** It took a while to get these to look, I mean, are you saying they look cool or they look weird?

**Alex Fine:** Oh, I like them, yeah, I like them.

**Jason Gong:** Okay.

**Alex Fine:** They're, to me, they're, like, do you know Stephen Bartlett, Diary of the CEO?

**Alex Fine:** Yeah, this guy.

**Jason Gong:** Oh, this guy, yeah, yeah, yeah, I've seen this guy.

**Alex Fine:** Yeah, yeah, so if you go on his YouTube, his thumbnails are really good, and it's, like, the reason I like his thumbnails is they're catchy, but they're also, like, buttoned up and professional, you know?

**Alex Fine:** Yeah, I've been trying to get the team to, like, do more stuff like this.

**Alex Fine:** Like, this type of stuff looks really good, but honestly, I think yours actually look better.

**Alex Fine:** They look, like, more creative, but these ones just, you know, like, the big red, like, lines.

**Alex Fine:** I love it.

**Jason Gong:** I like this more.

**Jason Gong:** I want all of our stuff to go more in this direction.

**Jason Gong:** It's just like engagement, hook building thing.

**Jason Gong:** We're not that good at it.

**Jason Gong:** That could be a video, honestly.

**Jason Gong:** Yeah, so right now it's mostly content.

**Jason Gong:** We have courses, you know.

**Jason Gong:** See, I think that right there looks amazing.

**Alex Fine:** That graphic.

**Alex Fine:** This one?

**Jason Gong:** That.

**Alex Fine:** That looks amazing to me.

**Alex Fine:** Cool.

**Jason Gong:** It's so simple.

**Alex Fine:** Yeah.

**Alex Fine:** People like faces, and it's just very simple.

**Jason Gong:** Also, you guys have incredibly good HD cameras.

**Jason Gong:** Well, we have a full-time production, guys, so, you know.

**Alex Fine:** We have dinner next week.

**Jason Gong:** Yeah, yeah, exactly.

**Jason Gong:** And then we have, it looks like people are actually posting now, which is kind of nice.

**Jason Gong:** You know, so, yeah.

**Jason Gong:** I mean, we'll have to do something with you guys that's like, I don't know.

**Jason Gong:** I mean, I want it to be something that you guys kind of speak to.

**Jason Gong:** to.

**Jason Gong:** Two all the time and like you guys are experts in and then I'm sure you'll generate business.

**Jason Gong:** mean, there's so many people in this community now and a lot of them are like senior-ish.

**Jason Gong:** So, yeah, that's great.

**Alex Fine:** Makes me want to build my own community too.

**Jason Gong:** I shouldn't go after exit five and I don't even know who, what are like the big sales ones?

**Jason Gong:** Like is RepGenius the thing or is it just kind of?

**Jason Gong:** I don't think anyone really uses RepGenius, but Pavilion's big.

**Alex Fine:** And then our events person used to run events for Pavilion.

**Jason Gong:** Gloria?

**Jason Gong:** Yeah, Gloria.

**Jason Gong:** Oh, really?

**Alex Fine:** Oh, yeah.

**Alex Fine:** You told me that actually.

**Alex Fine:** Yeah, yeah.

**Alex Fine:** No, Pavilion's big.

**Alex Fine:** They're really big in sales.

**Alex Fine:** I'd say in good market engineering, there's like all these little WhatsApp groups and a couple different Slack communities.

**Alex Fine:** Like honestly, people use the Clay Slack community for a lot of stuff regarding good market engineering.

**Alex Fine:** And then there's also like Clay Cafe.

**Alex Fine:** they haven't started a community, honestly.

**Jason Gong:** I mean, they have a community, but it doesn't feel like it has a home.

**Jason Gong:** Like would you say that?

**Jason Gong:** The Slack community is the home for like the Clay community or do they have like a circle or forum?

**Jason Gong:** Well, they kind of own LinkedIn too.

**Alex Fine:** That's true.

**Jason Gong:** I guess that's better than having it in some random platform.

**Alex Fine:** Mark and I met on LinkedIn.

**Alex Fine:** Well, we met through Clay Bootcamp, which is a course program type thing that Mark did.

**Alex Fine:** And I met him through the founder of Clay Bootcamp.

**Alex Fine:** And then we connected first on LinkedIn.

**Alex Fine:** It's like LinkedIn is definitely the place where Clay, Clay Wizards.

**Jason Gong:** Yeah.

**Alex Fine:** Is that run by Clay?

**Alex Fine:** No, they partner with Clay, but Nathan Lippey is the one who founded it.

**Alex Fine:** And Mark, unfortunately, you were too late for this, but I think I'm going to start adding as a benefit for understory employees where they get access to Clay Bootcamp, basically at like a very discounted rate.

**Alex Fine:** So I'm trying to work on that with Nathan.

**Alex Fine:** it's like, basically you can have it as a benefit.

**Alex Fine:** Like, you know, if you work at a company and you have a 401k, you can have...

**Alex Fine:** Then match your 401k or something like that.

**Alex Fine:** It's basically like we'll match your clay bootcamp costs.

**Alex Fine:** So like, let's say the program is five, five K, we'll give you $2,500 towards it.

**Alex Fine:** Something like that.

**Alex Fine:** But we're thinking about doing something like that.

**Jason Gong:** We had a few people asked for AI to do that.

**Jason Gong:** You know, what's really cool?

**Jason Gong:** The GTM engineering school.

**Jason Gong:** Like, I don't know if the content's cool, but like just the way they positioned it and gotten all these people to talk about it.

**Alex Fine:** It's Mateo, right?

**Alex Fine:** Like Mateo.

**Alex Fine:** Mateo, yeah.

**Jason Gong:** this other guy, Jared.

**Alex Fine:** Okay, I don't know Jared, but I've spoken to Mateo before.

**Alex Fine:** Yeah, it is cool.

**Alex Fine:** It's cool what they're doing.

**Alex Fine:** Yeah, they get people to speak.

**Alex Fine:** They asked me to speak at it.

**Alex Fine:** I forgot to respond to them, to be honest with you.

**Alex Fine:** But I will.

**Alex Fine:** But yeah, Mark, unfortunately, you were a little too late for that one.

**Alex Fine:** You started too early.

**Mark Lim:** But in the future.

**Alex Fine:** Mark, we'll give you a subsidized membership to our community.

**Mark Lim:** I don't know.

**Mark Lim:** don't even have I don't don't But it does.

**Mark Lim:** People that's going to work in understory, like, they won't need the bootcamp anymore, right?

**Mark Lim:** Like, they have to have the skills already, so.

**Alex Fine:** Yeah, I know.

**Alex Fine:** I know.

**Alex Fine:** Well, I think maybe I'll even take it myself.

**Alex Fine:** I don't know.

**Alex Fine:** It's one of those things that you can always refresh your skills, and frankly, the way Nathan's teaching it now, it's more so really technical about, like, JSON structure, APIs, and stuff like that, and then how to build it into Clay and N8N.

**Jason Gong:** And how many people per cohort do they get for that thing?

**Jason Gong:** I don't if it's, like, a cohort system.

**Alex Fine:** think they, maybe it is.

**Alex Fine:** Mark would know better than me.

**Mark Lim:** There's a one-on-one.

**Alex Fine:** One-on-one.

**Alex Fine:** Okay.

**Alex Fine:** It's a one-on-one.

**Jason Gong:** Wait, what?

**Jason Gong:** It's expensive.

**Jason Gong:** It's one-on-one?

**Jason Gong:** But with who, though?

**Jason Gong:** Like, do they have a whole group of people that do these one-on-ones, or is he the main instructor doing one-on-ones for a six-week period?

**Mark Lim:** So, yeah, there are coaches, like, I think, like, 10 or something, I don't know, like, maybe more.

**Jason Gong:** Yeah.

**Mark Lim:** And, yeah, those are the people that does the sessions.

**Mark Lim:** And how much is it?

**Mark Lim:** It's 7K, the program I took, and it gets even more expensive if you go on, like, a one-on-one session with Nathan.

**Mark Lim:** And then, like, it's, like, a 12K or something.

**Mark Lim:** Yeah, 12K, 12K.

**Alex Fine:** So I had a call with Nathan yesterday.

**Alex Fine:** He broke it down for me.

**Alex Fine:** So there's a 12K, a 7.5K, and then a 5K.

**Alex Fine:** And, like, the difference is basically the one-on-one support that you get.

**Alex Fine:** And then on the 12K package, you get multiple different sessions with Nathan himself.

**Alex Fine:** So the 7K package, what did you get from that?

**Mark Lim:** It's, like, like, an aid mentoring session with, like, some business mentor.

**Mark Lim:** And, uh...

**Mark Lim:** 10 clay technical coaching sessions.

**Mark Lim:** So like about like 15 to 18 sessions.

**Jason Gong:** Holy crap.

**Mark Lim:** And it's like two to three months engagement.

**Jason Gong:** Two to three months.

**Jason Gong:** Okay.

**Jason Gong:** And each session is what, like 30 minutes, you think, or an hour?

**Mark Lim:** An hour for the coaching session and like 30 minutes for the mentor session.

**Jason Gong:** I'm trying to see how the math of works, I guess.

**Jason Gong:** You should be charging for him.

**Jason Gong:** That's a crazy amount of lifetime.

**Alex Fine:** Yeah.

**Alex Fine:** No, I mean, he's doing well.

**Alex Fine:** He's had, he told me he's had over 200 students so far and they're scaling.

**Alex Fine:** And I'm trying to pitch him the idea of he needs to start doing exactly what I asked him to do at it as a company benefit, but with big companies, like imagine a Salesforce that says, okay, Nathan, we want to send all of our go-to-market hires that come through for the next year to you.

**Alex Fine:** We'll give you a million dollars, something like that.

**Jason Gong:** I wonder what the format, I mean.

**Jason Gong:** For his format now, it seems painful to do that because it's all live time.

**Jason Gong:** But for us, I wonder what the unlock is there.

**Jason Gong:** What do big companies want that isn't already there?

**Jason Gong:** Do they just want a nice certificate?

**Jason Gong:** Do they want something a little bit more structured?

**Jason Gong:** Do they just want some invoice they can pay?

**Alex Fine:** Well, I think about it for you guys.

**Alex Fine:** the same way.

**Alex Fine:** It's like imagine if Salesforce bought a package from you, right?

**Alex Fine:** Where they just said, I don't know, like we want all of our clients or all of our employees to have access to AI-led growth and expect 500 people total to be in the program.

**Alex Fine:** You guys typically charge $30 a month for it.

**Alex Fine:** We'll pay you $20 per month per employee, but we'll give you $500 immediately.

**Alex Fine:** I think I got to dig into that.

**Jason Gong:** Honestly, that seems more scalable than any of this other stuff.

**Alex Fine:** I love that.

**Alex Fine:** I mean, we already had a customer ask.

**Jason Gong:** Yesterday, and they wanted, let me see, I think they wanted five, which is not a lot, but I was like, okay, I'm not even sure how to actually give you five seats and not have it be clunky, so I was going to do that today.

**Alex Fine:** Look, if you ever want to shoot the  about this stuff, this is like my bread and butter.

**Alex Fine:** I love talking about this stuff.

**Alex Fine:** I have a million ideas around this.

**Jason Gong:** Well, I mean, I would love to like, just have your thing in here, and then whatever, you know, like, whoever signs up to it will just pay you, like, whatever they're paying us, or, you know, a percentage of that.

**Jason Gong:** Let's do it.

**Jason Gong:** And then you can use it to demo whatever I'm sure you'll want to do, like, separately in the future.

**Jason Gong:** Let's do it.

**Alex Fine:** And then we'll create an incestual community, and you guys can be a part of that one, too.

**Jason Gong:** Yeah.

**Jason Gong:** I mean, yeah, it seems like the sales space needs one that's, like, more hands-on, or maybe I'm just not finding where that is.

**Jason Gong:** Well, I think what people would really get a lot of value from that we do is, like, you don't see much of the behind-the-scenes stuff.

**Alex Fine:** That we constantly do for you and for all of our other clients.

**Alex Fine:** But it gets pretty technical pretty quickly.

**Alex Fine:** You just see the outputs, which is the whole goal.

**Alex Fine:** We don't want you to have to do the behind-the-scenes work.

**Alex Fine:** That's why we're here.

**Alex Fine:** But that type of stuff, those types of tactics, that's the type of stuff people really get a lot of value from.

**Alex Fine:** When I post that type of content on LinkedIn, people go crazy about it.

**Jason Gong:** Is that what the Cold IQ guys do more of?

**Jason Gong:** Like they try to do more like one-to-many or are they somewhat similar to you anyway?

**Jason Gong:** The Cold IQ guys—at this point they just have other people.

**Alex Fine:** Like those guys don't do much.

**Alex Fine:** They just have other people making content and creating the designs for them.

**Alex Fine:** So I think their whole play is like they talk about different flows and then they talk about how they have a lot of followers and those types of things.

**Alex Fine:** To be honest, their whole play is they're creating a content company as well.

**Alex Fine:** So they're trying to position it to be content IQ.

**Jason Gong:** Yeah, when I talked to them a year and a half ago, they were making a course series—I can't remember what they called it, but it was like an accelerator program to teach people.

**Alex Fine:** Oh, that's what it is.

**Jason Gong:** Okay.

**Jason Gong:** Yeah.

**Alex Fine:** So they did that.

**Alex Fine:** They were actually pretty successful at first with that.

**Alex Fine:** And then it just stopped.

**Alex Fine:** It wasn't working very well.

**Alex Fine:** And so they shifted the focus away to it.

**Alex Fine:** I mean, they're a competitor of ours, but they never come up, to be honest, in competition.

**Alex Fine:** And then, yeah, honestly, I don't know if they're doing great in that regard.

**Alex Fine:** But I think on the content side, they're trying to pick it up.

**Alex Fine:** And then on ads, too.

**Alex Fine:** And frankly, they tried to have a call with me about how we're doing ads.

**Alex Fine:** And I told them, no way.

**Alex Fine:** I'm not having that conversation with you.

**Alex Fine:** They're friends of mine.

**Alex Fine:** But, yeah, they've definitely tried to steal some of our stuff.

**Alex Fine:** So I have to be careful.

**Jason Gong:** Cool.

**Jason Gong:** Okay.

**Jason Gong:** I mean, let's talk about our stuff.

**Alex Fine:** Yeah, let's do it.

**Jason Gong:** The lovable workshop got punted to the second week of December.

**Jason Gong:** But now that...

**Jason Gong:** The community is live.

**Jason Gong:** think, yeah, like that's kind of on my mind, just like how to do something for the community.

**Jason Gong:** But yeah, but anyway, let's.

**Mark Lim:** Yeah, I prepared some ideas on the slide and you can take a look and let me know what you think.

**Mark Lim:** So and also I had some questions about building the Luma list and also like what type of city signals that I should use to build a SIPs automation and all of that.

**Jason Gong:** So we can talk about it after the slides.

**Mark Lim:** Let me share the screen.

**Mark Lim:** Okay, can you guys see it?

**Jason Gong:** Yep, yes.

**Mark Lim:** Yeah, so, yeah, I'm just going to start off with HeyReach stats, so 758 connections sent, 139 messages sent, and 30 replies, and the stats are looking good.

**Mark Lim:** They're above our goals, connection acceptance rate, about 20%, so yeah, that's a good number, and also, message reply rate is also above 20%, so yeah, we are seeing that it's above what the other clients are seeing with HeyReach stats, so yeah, it's looking good on that side, and also instantly stats, we have gathered about 63 opportunities so far, ever since we launched on October 31st, so it's been a

**Mark Lim:** About, I guess, like a week and a half, probably.

**Mark Lim:** So, yeah.

**Mark Lim:** And the reply rate is looking good, too.

**Mark Lim:** It's landing in the inbox as well, not in the spam filter.

**Mark Lim:** So, yeah.

**Mark Lim:** Planning to launch more and also double down on the copy version that is generating more leads.

**Mark Lim:** So, that way we maximize the amount of positive replies.

**Mark Lim:** And, yeah.

**Mark Lim:** And I also wanted to talk about Evergreen Campaign.

**Mark Lim:** So, basically, since you just recently launched Community, it's basically now really active.

**Mark Lim:** So, I was thinking that we can do an Evergreen Campaign to basically provide, like, past webinar recordings link.

**Mark Lim:** yeah.

**Mark Lim:** We can get them into the GrowthX ecosystem, and it will run even without planned webinars. We just ask people if they want past webinar recordings, and this angle is working well with the Lovable webinar campaign.

**Mark Lim:** So I think that it could generate some good traction.

**Jason Gong:** I think an always-on campaign that drives to something free in the community is interesting. From that page, people see all the other paid stuff and think, "Oh, I can pay and get all this." We can keep it simple at first, then segment. Everything you're doing for the workshop, LinkedIn, the lists you're scraping, and SIFT signals from people engaging with our content can feed into that.

**Jason Gong:** We could build this like the one I showed you that we run for ourselves.

**Alex Fine:** It's always on—always scraping content and funneling leads in.

**Alex Fine:** This will always run.

**Alex Fine:** And then everything else we do will just be in addition to.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** That sounds good.

**Jason Gong:** What would be the next step for that one?

**Jason Gong:** Like I know we're kind of using all the current emails for the workshop, which I think we should just keep it like that.

**Jason Gong:** But yeah, like how do we.

**Alex Fine:** We just have to switch whatever infrastructure we want.

**Alex Fine:** Oh, go ahead, Mark.

**Mark Lim:** Oh, yeah, yeah.

**Mark Lim:** So we can source this additional list.

**Mark Lim:** So.

**Mark Lim:** Thank

**Mark Lim:** From like Pavilion, Exit 5 members list, Profound Air Ops, event registrant list, and competitor LinkedIn follower list.

**Mark Lim:** There are some lists that are not included in the Lovable campaign yet.

**Mark Lim:** So we can use that too.

**Mark Lim:** And also we can reuse the list every like two months.

**Mark Lim:** And people don't really remember if they have gotten an email from GrowthX.

**Mark Lim:** It's just one of the cold emails, so they forget.

**Mark Lim:** So we usually just reuse the list every two months.

**Mark Lim:** So yeah, that's the whole strategy to source leads for this campaign.

**Mark Lim:** And, but obviously driving more registrants to the Lovable campaign is a priority.

**Mark Lim:** But I think like we can also start on a smaller scale.

**Mark Lim:** Because we obviously want to maximize the lovable campaign results.

**Jason Gong:** Yeah, mean, as an offer, that one seems, like I imagine some of the higher response reach is just because lovable is more interesting.

**Jason Gong:** Hot name.

**Jason Gong:** I think that makes, yeah, that makes sense.

**Jason Gong:** I guess what's the right way to think about bandwidth of how much email or messages we can send?

**Jason Gong:** Like on LinkedIn, I guess it's pretty obvious.

**Jason Gong:** It's like it's limited by number of accounts, but on email, like what's the right way to think about that?

**Jason Gong:** Is there like a number of emails per week that like kind of were roughly bottlenecked on where we have to pick, you know, hey, if we're only sending like 2,000 or something?

**Jason Gong:** Unless you guys want to add more infrastructure, which we could absolutely do.

**Jason Gong:** Yeah.

**Jason Gong:** There is a number right now.

**Alex Fine:** But like.

**Alex Fine:** How does that work?

**Jason Gong:** I guess it's like, I mean, like, clearly you don't want like a million inboxes, but like, is it in general?

**Jason Gong:** Like, I don't know.

**Jason Gong:** You guys just can't support more than like 10 or 20.

**Jason Gong:** Like, is there?

**Alex Fine:** We can support unlimited, honestly.

**Alex Fine:** So it really just matters for you because it costs us money to buy more inboxes and support more inboxes.

**Alex Fine:** But if you guys, we can give you a quote for what it would look like to add more inboxes and we can do it.

**Alex Fine:** It's not going to be expensive at all.

**Alex Fine:** We'll basically bill you for costs.

**Alex Fine:** Okay.

**Jason Gong:** No, that's pretty interesting.

**Jason Gong:** How much do we have right now?

**Jason Gong:** Like the ability to send per week?

**Mark Lim:** So that is about 10,000 emails per week.

**Mark Lim:** Okay.

**Jason Gong:** Got it.

**Jason Gong:** Per week?

**Jason Gong:** That's what we have, Mark?

**Alex Fine:** Yeah.

**Mark Lim:** Per week.

**Mark Lim:** 10,000.

**Mark Lim:** Okay.

**Jason Gong:** And I guess once you, so like, as far as new people goes, I guess,

**Jason Gong:** That would be what, like a few thousand, like maybe three or four thousand, because I know you like follow up and then that counts for an email, I guess.

**Jason Gong:** Like how many new people are you hitting up every week?

**Alex Fine:** That's also just a math question.

**Alex Fine:** So we can say if we wanted to send two messages, not three, if we want to send one message, not two, then we can just divide by number of messages.

**Jason Gong:** That makes sense.

**Jason Gong:** I guess I'm trying to think how the sequence would be any different, like for the lovable one.

**Jason Gong:** Like I guess the lovable one is a future event, so there's no real kind of urgency to pay or get access to something.

**Jason Gong:** Like I wonder if we can experiment with something that's like more, give them access to something in the community right now and see if that causes anyone to sign up for it.

**Jason Gong:** Why don't just give them a free month?

**Jason Gong:** Yeah, we could give them a promo code for a free month.

**Alex Fine:** Just say, hey, I'll give you a free month.

**Alex Fine:** If you're happy with it, can sign up for month two.

**Alex Fine:** If you're not, no sweat.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** I guess maybe as the next step, we can do this with one of the targeted lists you scrape.

**Jason Gong:** With one of those, we can do a new campaign.

**Jason Gong:** I guess if you can get a doc started, I can think about copy, and then I can just write that in.

**Jason Gong:** I guess I have a pretty good idea already of what I want to say.

**Jason Gong:** Does that work?

**Jason Gong:** Yeah, sure.

**Mark Lim:** Yeah, just prepared a copy example based on what we've been sending.

**Mark Lim:** And yeah, it's pretty similar to how you wrote before.

**Mark Lim:** And we were just basically offering past the webinar recording.

**Mark Lim:** Oh, is this?

**Jason Gong:** Yeah, listing people, like your customers.

**Mark Lim:** And yeah.

**Mark Lim:** A guest company on the webinar and everything.

**Mark Lim:** Okay, so that's the campaign right now.

**Jason Gong:** It's like it asks them if they want something existing.

**Jason Gong:** And then in the reply, you're like, oh, here's an upcoming webinar with Lovable.

**Jason Gong:** Is that how the sequence is going?

**Mark Lim:** Yeah, exactly.

**Mark Lim:** So if you read this copy, it's basically asking if they want to see the past webinar recording.

**Mark Lim:** And when Hesus replies, he can also mention something like, here's a link to the previous recording.

**Mark Lim:** And by the way, we have a community that has all the other past webinar recordings regarding on creating and sharing content with AI.

**Mark Lim:** So would you like a free month with this as well?

**Mark Lim:** Like, yeah, join this link too.

**Mark Lim:** Like something like that.

**Jason Gong:** Got it.

**Jason Gong:** Okay.

**Jason Gong:** Actually, okay.

**Jason Gong:** That I think is the experiment.

**Jason Gong:** I'm just going to ask Hesus to follow up with the, he said there are 60 people that replied.

**Jason Gong:** And I'm just

**Jason Gong:** I'm to offer all of them in discount code, and let's see how many of them take it, and then I'll also just change the reply.

**Jason Gong:** So I guess there's nothing you actually need to change that.

**Jason Gong:** I'll just ask Aziz to update the reply.

**Jason Gong:** Okay, sounds good.

**Mark Lim:** Yeah, and also there were, like, before we go, just I had, like, two quick questions.

**Mark Lim:** So first, I tried registering for Profound and Airhoff's Luma events, and then I noticed that I can see the list of registrants, but they only have, like, their full name.

**Mark Lim:** So, like, I was wondering if, like, if there are any other ways to scrape their LinkedIn profiles or whatever.

**Jason Gong:** I think that is the only way.

**Jason Gong:** That's why I think it's, like, a little bit tricky, but I think generally for a given name, there's, like...

**Jason Gong:** I mean, I'm fine if you have an ICP definition and then all the people with that name you just grab, but it's generally pretty safe if you find somebody with a marketing or sales background and has that name, that's probably the person.

**Jason Gong:** And if there's five people with the name, like John Smith, who's a marketer, let's just add all of them to the list.

**Jason Gong:** It's not like our messaging is that targeted anyway.

**Jason Gong:** Okay.

**Jason Gong:** Would you be able to do something like that?

**Jason Gong:** Just go by name and kind of filter that down, I guess, by profile afterwards?

**Mark Lim:** Okay.

**Mark Lim:** Yeah.

**Mark Lim:** I can try that.

**Mark Lim:** Yeah.

**Mark Lim:** But like, honestly, like, I don't know how accurate it will be, but still like, it's possible to scrape by full name and see if they are in our ICP company.

**Mark Lim:** And yeah, that works.

**Mark Lim:** And also, uh, I looked up on the system.

**Mark Lim:** And there were some signals that we can scrape.

**Mark Lim:** So, like, I noticed that on the video you wanted to scrape the post reactions and post comments.

**Mark Lim:** But I was wondering if you also want to scrape profile views and new followers for ourselves and your account.

**Jason Gong:** Yeah, I think that all works.

**Jason Gong:** I think what I was trying to think through is, like, what the campaign looks like that kind of uses that information.

**Jason Gong:** Because, so, I guess how I'm imagining it is, like, LinkedIn in general is just a source.

**Jason Gong:** And, like, any engagement gets sent here, right?

**Jason Gong:** I think it makes sense to segment it a little bit.

**Jason Gong:** But, like, right now, the way I've set it up is, like, you have everything where somebody liked our content.

**Jason Gong:** Content, whether it's me, Marcel, or our company pages, that's this one.

**Jason Gong:** And then everything else, that's not exactly our content.

**Jason Gong:** And the way that works is like, I can just go on LinkedIn, and if I click this, it'll just start scraping everybody here.

**Jason Gong:** Like everything there comes into this bucket, and like some of the things here, I don't know.

**Jason Gong:** Like I'm pretty sure I clicked like something from, from profound, for example, like, oh, wait, this is Marcel's post.

**Jason Gong:** Okay, so there's something, something to clean up here for sure, but like, for sure one of these is like a profound post that I was like, oh, yeah, I want to monitor.

**Jason Gong:** Why is all this?

**Mark Lim:** Yeah, actually, um, yeah, like this, for example, right?

**Jason Gong:** Yeah, yeah.

**Jason Gong:** Um, so, yeah, go ahead.

**Jason Gong:** Yeah, well, I guess what I had in mind was like, for these two buckets, like this one, you would.

**Jason Gong:** Try to kind of de-duplicate, make sure they're not in some existing campaign.

**Jason Gong:** And then everybody here just gets added to this, like, always on campaign from me, let's say, on LinkedIn.

**Jason Gong:** And, like, I would just add them.

**Jason Gong:** I would say, like, you know, hey, thanks for, you know, like, supporting us.

**Jason Gong:** You know, we had a lot of people that found this webinar we did recently really valuable.

**Jason Gong:** I just wanted to send over the recording in case it helps you.

**Jason Gong:** And then for this bucket, guess we think of something else.

**Jason Gong:** But, like, I wanted that to be the machine that was just, like, always on.

**Jason Gong:** Yeah, I actually built, like, a series of tables that does exactly what you wanted.

**Mark Lim:** So, like, I can just go over, like, really briefly and then, like, give you a little bit of idea, like, how we can pull this off.

**Mark Lim:** So, if you don't mind, I can share the screen.

**Jason Gong:** Yeah.

**Jason Gong:** So.

**Mark Lim:** So.

**Mark Lim:** so

**Mark Lim:** So, yeah.

**Mark Lim:** So, basically, yeah, just, like, imagine, like, there are, like, webhook that are coming in, and then we have their company website URL and also their LinkedIn profile URL and everything.

**Mark Lim:** And what it does is basically just deduplicate against a suppression list, like, removing all your competitors or existing customers, and then extracting country to validate if they are in your ICP country and just, like, finding what industry are they in and something like that.

**Mark Lim:** And then we just go ahead and then enrich contact information as well, and email as well.

**Mark Lim:** So, yeah, just, yeah, these, like, and then at the end, we can decide if you want to just push it.

**Mark Lim:** Do instantly for email or to HeyReach.

**Mark Lim:** And also we can segment by if the people that engage or commented on the post commented on your growthx content or other content and then change the messaging accordingly too.

**Mark Lim:** So, yeah, like this is how I'm planning to do it at the moment.

**Mark Lim:** So, yeah, I will get back to you on this like when once I build it and yeah.

**Jason Gong:** Sounds good.

**Jason Gong:** So I guess where does the segmentation happen?

**Jason Gong:** So it's like I have just this like pool of people and then I see you're kind of like you're seeing if they're in the do not contact, you're like enriching them.

**Jason Gong:** And then there's like something it's like based on some signal, I'm sending them a different message.

**Jason Gong:** Like where does that happen in this table you're just showing?

**Mark Lim:** Yeah, so.

**Mark Lim:** So that I can build it.

**Mark Lim:** And basically what it does is it can pull data from the first initial table where it showed the content URL of the person that I engaged with.

**Mark Lim:** And then we can create a formula to segment by growthx content or competitor content or whatever.

**Mark Lim:** And then just give a label of all the context that like which source they come from.

**Mark Lim:** And then with those label, I can create a personalized message afterwards.

**Mark Lim:** So, yeah, it doesn't make sense.

**Mark Lim:** Okay.

**Jason Gong:** And then the message, like, will this work for both email and like LinkedIn?

**Mark Lim:** Yeah, yeah.

**Mark Lim:** We can push a different copy.

**Mark Lim:** And each email and LinkedIn.

**Jason Gong:** Okay.

**Jason Gong:** Cool.

**Jason Gong:** That sounds good.

**Jason Gong:** So I guess next step is kind of hooking this up.

**Jason Gong:** And then once you hook it up, I guess we can think about, or I'll just think about separately, like what the campaigns could be that are always on and I'll shoot you over like a doc or something.

**Jason Gong:** Yeah, that works too.

**Mark Lim:** And yeah, just one last thing, when you scrape the signals, like post engagers and comments from other people's content on LinkedIn, like where does it populate like on SIFT and like how I can see them?

**Mark Lim:** Yeah.

**Jason Gong:** So SIFT, I feel like I should ask them for this feature, but let's see.

**Jason Gong:** Oh.

**Jason Gong:** Oh, he's stuck here.

**Jason Gong:** Uh.

**Jason Gong:** Uh.

**Jason Gong:** So, feel free to use this too.

**Jason Gong:** I haven't had that much time.

**Jason Gong:** So, like, so the listening happens here.

**Jason Gong:** Like, here are the three accounts that it's using to listen to LinkedIn.

**Jason Gong:** Oh, okay.

**Jason Gong:** Don't change that.

**Jason Gong:** And then, like, here are the profiles it's tracking.

**Jason Gong:** So, like, these are, like, always on tracking.

**Jason Gong:** And you can see, you know, it's got Marcel's posts and my posts.

**Jason Gong:** I don't see my posts.

**Jason Gong:** Oh, this is my post from this morning.

**Jason Gong:** It's, like, all being scheduled to, like, I guess essentially, like, grab leads from.

**Jason Gong:** And then the leads all get grabbed.

**Jason Gong:** And then here are the two automations that essentially, like, pipe it into clay.

**Jason Gong:** So, this one I have.

**Jason Gong:** have.

**Jason Gong:** I don't

**Jason Gong:** And what it's doing is that I just have this filter where it's like only from these four accounts.

**Jason Gong:** I will add them on LinkedIn and also put them, I guess, ping this webhook so they get sent to that clay table.

**Jason Gong:** And then I have the same thing for this one, but because they don't have like a nice filter here, I just do like did not comment on this.

**Jason Gong:** So I guess that makes it so that like if I click this, you know, as long as it's not one of our accounts, it'll always go into this other filter and then it'll get added to this table.

**Jason Gong:** But it looks like, you know, maybe at some point I clicked Marcel's post and I don't know that that can also get caught here.

**Jason Gong:** So I need to fix that, but you can see here, like I clicked this, you know, profound guy's post and then everyone that reacted basically.

**Jason Gong:** It got pulled into here.

**Jason Gong:** Does that make sense?

**Jason Gong:** Yeah.

**Mark Lim:** So on the motions page, is that on Zip?

**Jason Gong:** Yep.

**Mark Lim:** So the trigger section, I see that you just selected to, okay, so not in Marcel.

**Jason Gong:** Yeah.

**Jason Gong:** I wish they had some better filtering here.

**Jason Gong:** We can ask them for that.

**Jason Gong:** But they also have this stuff if we want to get really nuanced.

**Jason Gong:** I feel like we just start simple, but you can also filter by specific posts, it looks like.

**Mark Lim:** Okay.

**Mark Lim:** Yeah.

**Mark Lim:** Yeah.

**Mark Lim:** That makes sense.

**Mark Lim:** Then, yeah, I think I can, yeah, start building and let you know.

**Mark Lim:** And once I'm done, you can, I can maybe ask you to like disable.

**Mark Lim:** sense.

**Mark Lim:** Okay.

**Mark Lim:** hope So background.

**Mark Lim:** background.

**Mark Lim:** There's

**Mark Lim:** The existing workflows so that it doesn't collide with the one that we were building.

**Mark Lim:** Like colliding, like it's like adding people on LinkedIn and stuff.

**Jason Gong:** don't know.

**Mark Lim:** Yeah, like if there are like two campaigns towards the same leads, then it's...

**Mark Lim:** Oh, okay, got it.

**Jason Gong:** I mean, right now, like there are no campaigns.

**Jason Gong:** They all just kind of get added here.

**Jason Gong:** So whatever campaign you make will be the only one.

**Jason Gong:** So I think we should be good.

**Jason Gong:** Yeah, sounds good.

**Jason Gong:** Okay, cool.

**Jason Gong:** I think that's it.

**Jason Gong:** then...

**Jason Gong:** Yeah, so like one last question.

**Jason Gong:** Like what you're doing with the pavilion lists at the moment is like you're...

**Jason Gong:** Just adding.

**Jason Gong:** them into the existing campaign.

**Jason Gong:** Is that right?

**Mark Lim:** Yeah, I actually haven't added them to any campaign, but I think I'm going to, I can try with the Evergreen campaign that I just showed you earlier.

**Mark Lim:** Yep.

**Jason Gong:** And start from there.

**Mark Lim:** That makes sense.

**Jason Gong:** Yeah, I mean, I think from last week, it's like, if they seem more VIP or like high intent, like, it seems like LinkedIn just has higher response rates.

**Jason Gong:** So I would sort of like that.

**Jason Gong:** Like, for example, the AirOps list, like, I would probably just run it through LinkedIn because those people are pretty like, I mean, if they went to an AirOps workshop, they, you know, are pretty likely to come to ours.

**Jason Gong:** So like, we can use LinkedIn for that one if possible.

**Alex Fine:** Mark, we can just set a filtering criteria in a clay column that literally just understands based on the context that we give it, who to add and who not to add to a HeyReach campaign.

**Alex Fine:** And then just.

**Alex Fine:** Factor it as like a, we could even do like a scoring model.

**Alex Fine:** So it's like, if these five things are true, add them to Hayreach first, and then do it that way, given that we are limited by volume on Hayreach.

**Mark Lim:** Yeah, sure.

**Mark Lim:** Yeah, I can do it.

**Alex Fine:** That's crazy.

**Alex Fine:** Wojciak is in your community.

**Jason Gong:** Who?

**Jason Gong:** That gets everywhere.

**Alex Fine:** Wojciak, the guy at the top.

**Alex Fine:** It's his Wojciak, Patrick.

**Alex Fine:** Oh, who is this guy?

**Jason Gong:** He's a, he's this really funny Polish dude.

**Jason Gong:** He's at every event ever in the world.

**Alex Fine:** And he's just really funny.

**Jason Gong:** Interesting.

**Jason Gong:** Yeah, that's really cool.

**Jason Gong:** I mean, I also see this guy from Eros, but like, it's like, can't really kick people out of the community.

**Jason Gong:** So I'll just let him in here.

**Alex Fine:** Well, you could in theory.

**Alex Fine:** But yeah, I feel like.

**Jason Gong:** Yeah, it wouldn't be a good look.

**Alex Fine:** I just want to steal what we're doing, which is fine.

**Alex Fine:** Yeah.

**Alex Fine:** All right, I'm 16 minutes late to another call, so I'm going to jump.

**Alex Fine:** Mark, you have anything else, or Jason, you have anything else, feel free to stay, but I do have to jump.

**Jason Gong:** All right, see you later, Alex. I think I'm good.

**Jason Gong:** Anything you're blocked on from our side that I can help with?

**Mark Lim:** Yeah, not at the moment.

**Mark Lim:** Like, I asked all the questions I wanted to ask, so all good.

**Mark Lim:** Okay, sounds good.

**Jason Gong:** All right, ping me if you need anything. See you later.

**Alex Fine:** Bye.
