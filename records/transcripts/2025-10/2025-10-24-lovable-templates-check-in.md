# Lovable Templates Check-In

<metadata>
date: 2025-10-24
time: 17:14 UTC
duration: 62 minutes
organizer: George Haikal
participants: George Haikal, Georgemaine Lourens, Nicolas Castellanos
fathom_recording_id: 96681508
fathom_url: https://fathom.video/calls/451595491
share_url: https://fathom.video/share/hhdgdx_dpeNxoCWGp-XBC7T6hvZQwio-
source: fathom
enriched_on: 2026-03-02 22:15 UTC
</metadata>

---

## Summary

GrowthX finalized the Lovable template gallery MVP for launch, stripping the initial 7 templates down to bare essentials—removing navigation, search, and filters to accelerate deployment by Tuesday. The team aligned on the next strategic push: Portfolio Websites, which competitive analysis identified as the highest-volume keyword category for quick SEO wins. Content pipeline setup and unlimited Lovable credits emerged as key blockers requiring immediate attention.

---

## Context

GrowthX is building a high-performance template gallery for Lovable (a web builder product) as part of a $200k+ engagement. The client is impressed with progress through week six of the project, starting from week two. George Haikal leads the initiative with Georgemaine Lourens (designer/developer) and Nicolas Castellanos (engineer) executing core work. Marcel Santilli (external) provides broader context. The team has shifted from polishing initial templates to rapid-fire production of portfolio website variations, requiring both technical workflow optimization and clarity on resource constraints like API credits.

---

## Relevance

- **To GrowthX Delivery:** MVP-first approach reducing feature scope to accelerate launch by removing UI complexity for small template sets. Content pipeline now critical bottleneck; requires documented workflow and unlimited credits from Lovable to achieve planned velocity of multiple portfolio variations weekly. Team established Thursday recurring sync to manage daily blockers efficiently.
- **To GrowthX Business Development:** Client (Lovable CMO Cece and head of growth Rachel) showing strong satisfaction signals mid-project. Competitive analysis framework (keyword mapping, search volume analysis, intent classification) directly applicable to other CheckThat/AEO opportunities. Portfolio websites identified as immediate expansion vector based on data-driven template prioritization.
- **To CheckThat:** Template SEO strategy relies on individual page indexability and GSC performance tracking (clicks, impressions by page/category). Requires `lovable.dev` domain GSC access to track early wins and iterate. Setup and performance monitoring directly inform broader AEO visibility and ranking methodology validation.

---

## Overview

- **MVP Launch:** The initial gallery will launch with 7 templates, stripped of navigation, search, and filters to simplify the user experience and accelerate deployment.
- **Next Strategy:** The next content push will target "Portfolio Websites," identified via competitive analysis as the highest-volume keyword category for quick SEO wins.
- **Content Pipeline:** A scalable pipeline is required to generate unique content for similar templates (e.g., two food blogs), avoiding repetition and ensuring SEO effectiveness.
- **Tracking:** GSC access for `lovable.dev` is needed to track template performance (clicks, impressions), as the current `lovable.app` domain access is insufficient.

---

## Key Topics

### Template Gallery MVP

  - **Goal:** Launch the template gallery by Tuesday with a simplified MVP experience.
  - **Rationale:** The full UI (navigation, search) is unnecessary for a small initial set of 7 templates and would delay launch.
  - **MVP Scope:**
      - **Remove:** Category navigation bar, search bar, and "Latest/Popular" filters.
      - **Keep:** Individual template detail pages for SEO indexing.
  - **Content Generation:**
      - **Problem:** Similar templates (e.g., "Culinary Culture" & "Food Stories") require unique content to avoid repetition.
      - **Solution:** Use distinct prompts in the content pipeline to generate unique descriptions, highlights, and features.
      - **Example Prompts:**
          - "Culinary Culture": Newsletter signup angle for food stories.
          - "Food Stories": Traditional recipe blog angle.

### Next Content Strategy: Portfolio Websites

  - **Rationale:** Competitive analysis revealed "Portfolio Websites" as the highest-volume keyword category, offering the best opportunity for early SEO wins.
  - **Action:** Prioritize creating templates for this category next week.
  - **Execution:**
      - **Focus:** Scalability over perfection. The goal is to produce many variations quickly, leveraging the team's established trust in quality.
      - **Process:** Define a repeatable page structure (e.g., Home, About, Work, Contact) and use a component-based workflow.
      - **Content:** Use high-quality Unsplash collections for images.
      - **Credits:** The current 1-2k credit limit is insufficient for this high-volume strategy; unlimited credits are required.

### Logistics & Blockers

  - **Lovable Account Credits:** The account is out of credits, blocking new template generation.
      - **Workaround:** Georgemaine is using Claude for now.
      - **Action:** George Haikal will request more credits from Sebastian.
  - **Client Feedback:**
      - **Felix:** Provided minor UI edits (button/icon changes).
      - **Nat:** Requested polish round, but the Loom recording is inaccessible.
      - **Action:** Georgemaine will implement Felix's edits and await Nat's feedback.
  - **Gallery Access:**
      - **Request:** Cece (CMO) requested the gallery link.
      - **Action:** George Haikal will DM Cece the password, per Furkan's security directive to use 1Password for external sharing.
  - **Performance Tracking:**
      - **Need:** GSC access for `lovable.dev` to track impressions and clicks.
      - **Rationale:** Access to `lovable.app` is insufficient for tracking the `lovable.dev` domain.
      - **Action:** George Haikal will request access from Rachel.
  - **Meeting Cadence:**
      - **New Time:** Thursdays, to allow for same-day resolution of any client-side blockers.

---

## Action Items

**George Haikal**
- Finalize internal Kanban tracker for Fathom
- Send Cece 1-time password link; prompt 1Password
- Request GSC access for lovable.dev from client
- Add growthxlabs.com team access to Lovable; ensure Georgemaine & Nicolas included
- Ask Sebastian re: unlimited/higher Lovable credits
- Attend content pipeline working session w/ Nicolas; document workflow
- Schedule recurring Thu sync w/ Georgemaine & Nicolas

**Georgemaine Lourens**
- Finish remaining templates via Claude; apply Felix edits; prep for MVP launch

**Nicolas Castellanos**
- Strip gallery to MVP; remove nav/tags/filters/search; keep indexable pages
- Ask Yusuf for 'nico@growthx.ai' alias

---

## Transcript
**Georgemaine Lourens:** So, happy Friday.

**Georgemaine Lourens:** I can't hear you.

**George Haikal:** You're on mute.

**George Haikal:** Oops.

**George Haikal:** You know, it's at least once every other day that I accidentally mess up something on the tech side for joining a meeting.

**Georgemaine Lourens:** Oh, no worries.

**George Haikal:** I mess up all the time.

**George Haikal:** How are you doing, man?

**Georgemaine Lourens:** I am doing good.

**Georgemaine Lourens:** I am doing good.

**Georgemaine Lourens:** I actually did a fun surprise today for my partner.

**George Haikal:** Oh, tell us.

**Georgemaine Lourens:** Tell us.

**Georgemaine Lourens:** Well, we're this year, we're together for 10 years, and she's been nagging me about having a kid since forever.

**Georgemaine Lourens:** And I think this year will be the year, or maybe next year, actually.

**George Haikal:** Let's go.

**Georgemaine Lourens:** But I haven't told her yet.

**Georgemaine Lourens:** But instead, like in the Netherlands, in Amsterdam, there's this trend where like all of the parents, put their kid in like a cargo bike, and then they come to fly.

**Georgemaine Lourens:** I write a kid around, and the cargo bike is pretty expensive, but it's like an e-bike, and she always bought it in one of those.

**Georgemaine Lourens:** So today I went to the store and I ordered one, and it will be here in two weeks, and that's going to be the way that I'm going to break the news to her.

**George Haikal:** So, yeah.

**George Haikal:** Wait, wait, I'm confused.

**George Haikal:** Wait, wait.

**George Haikal:** You mentioned having a kid, but then you bought an electric cargo bike?

**Georgemaine Lourens:** Yeah, as kind of like the...

**George Haikal:** Is this our kid for now?

**Georgemaine Lourens:** No, as in, let's have a kid, and here's the gift.

**Georgemaine Lourens:** Nice.

**George Haikal:** Let me look it up.

**George Haikal:** don't know what a cargo bike.

**Georgemaine Lourens:** It's basically an electric bike with a big bucket of...

**George Haikal:** Oh, got it.

**George Haikal:** It's for carrying a kid around on the bike.

**Georgemaine Lourens:** Yeah, exactly.

**Georgemaine Lourens:** What did you have in mind?

**George Haikal:** I just thought you were talking about a regular electric bike.

**George Haikal:** That's why I was confused.

**Georgemaine Lourens:** No, no, no, no, no.

**George Haikal:** That's awesome.

**Georgemaine Lourens:** I sure love that.

**Georgemaine Lourens:** Yeah, I think so.

**Georgemaine Lourens:** How about you?

**George Haikal:** Do you have any plans for the weekend?

**George Haikal:** For the weekend, no, but I'm in a good mood.

**George Haikal:** I'm usually in a decent mood.

**George Haikal:** I'm in a good mood because before this job, like I always worked out early in the mornings before the day.

**George Haikal:** was like my favorite way to start the day.

**George Haikal:** And it was like usually sports related.

**George Haikal:** It was either rugby or MMA or something like that.

**George Haikal:** And then having started, Marcel and I are in the office early, like 6.30 a.m.

**Georgemaine Lourens:** And it's like a really good time to get work done before the day starts.

**George Haikal:** So the tradeoff I've made was like working out later in the day.

**George Haikal:** And so this morning, I finally got back into like an MMA class that I haven't been in probably like a month.

**George Haikal:** And so for like an hour and a half this morning, I was getting choked out and trying to choke people.

**George Haikal:** It's just like the best feeling after.

**George Haikal:** I don't know.

**George Haikal:** I can't really explain it.

**George Haikal:** But, you know, just like the contact plus the workout plus.

**George Haikal:** You're learning too.

**George Haikal:** It's like a puzzle and like problem solving.

**George Haikal:** So it was like a great, a great start to the morning that I haven't had in a while.

**Georgemaine Lourens:** No, I can totally relate to that.

**Georgemaine Lourens:** Like I've been doing that routine for like over two years now, I think.

**George Haikal:** Yeah, your movement score, Yeah, I just, just go down, drink my coffee, do the dishes, and then I'm out on my bike for an hour.

**Georgemaine Lourens:** Kind of like getting your blood rate up and running, your heart rate up and running in the morning is the best way to start the day.

**Georgemaine Lourens:** Like I'm always energetic and so I could totally relate to it.

**Georgemaine Lourens:** And doing MMA and the puzzle solving, that must be a lot of fun too.

**Georgemaine Lourens:** So, yeah.

**George Haikal:** Yeah, it's amazing.

**George Haikal:** What about you, Nico?

**Nicolas Castellanos:** No, I write some cards.

**George Haikal:** Let's go.

**George Haikal:** That's awesome.

**George Haikal:** You were on the plane last week, right?

**George Haikal:** Thank

**Nicolas Castellanos:** Yeah, again, what did you say?

**George Haikal:** And you were on the plane last weekend, right?

**Nicolas Castellanos:** Yeah, yeah, I had that.

**Nicolas Castellanos:** And I need to schedule the next class.

**Nicolas Castellanos:** I don't when that's going to be.

**Nicolas Castellanos:** But for this weekend, yeah, probably go-karts.

**Nicolas Castellanos:** And I might also go to the beach and be on the water.

**George Haikal:** Nice.

**George Haikal:** Nico likes to go fast.

**George Haikal:** I love it.

**Nicolas Castellanos:** I love it.

**Nicolas Castellanos:** Yeah.

**George Haikal:** Cool.

**George Haikal:** Let me pull up the stuff.

**George Haikal:** I feel pretty good about where we're at in terms of the work and then the next steps, especially on, like, the templates and then working with Nico on the pipeline.

**George Haikal:** So we can talk about all that.

**George Haikal:** But is there anything top of mind for either of you before I kind of, like, jump in?

**Georgemaine Lourens:** No, let's jump in on my end.

**Georgemaine Lourens:** Anything for you, Nico?

**Nicolas Castellanos:** I'm thinking, I think I have stuff, but it's probably related to the pipeline.

**Nicolas Castellanos:** Because it's about the highlights and keywords and all that kind of stuff that will probably be part of the pipeline.

**Georgemaine Lourens:** Yeah, I think I added that to the agenda.

**George Haikal:** What do mean?

**Georgemaine Lourens:** As a talking point.

**Georgemaine Lourens:** Oh, got it, got it.

**George Haikal:** Yeah, sorry, I'm just writing a few of the things I'm going to forget.

**George Haikal:** Yo.

**George Haikal:** Looking cadence.

**George Haikal:** Next steps.

**George Haikal:** Next set of templates.

**George Haikal:** Okay, cool.

**George Haikal:** So let's start with it.

**Nicolas Castellanos:** There's one thing.

**Nicolas Castellanos:** Credit the, we need credits on the account.

**Nicolas Castellanos:** I know you've been, Sebastian.

**Nicolas Castellanos:** No.

**Nicolas Castellanos:** But I don't think, I checked, like, a few hours ago, it was still nothing.

**George Haikal:** I think I'm right now again.

**George Haikal:** We can probably just pay it and then, like, pass it through as well if it's blocking you.

**Nicolas Castellanos:** I think right now, Georgemaine got a workaround using Claude, so now I'm not a blocker.

**Nicolas Castellanos:** And I'm focusing on the gallery, so don't need to be generating anything for now.

**George Haikal:** Boy, I just think we're going to be DMing him in case he hasn't seen it.

**Georgemaine Lourens:** And in which document are you?

**Georgemaine Lourens:** In the Lovable GrowthX Week 6 sync?

**George Haikal:** No, here, let me, that's probably a good idea.

**George Haikal:** We could just make, so I'm on Lovable.

**George Haikal:** This is our internal where they can't see, right?

**George Haikal:** So, like, whenever we're just doing stuff for us or I'm thinking to things, I go into the internal docs behind the client workspace.

**George Haikal:** And then I kind of just, like, make some stuff up.

**George Haikal:** But I can make it more.

**George Haikal:** Yeah.

**George Haikal:** I'll make it more presentable for Fathom, so I'm 1024 right now.

**George Haikal:** That's okay.

**George Haikal:** And then this will look good.

**George Haikal:** finish this today, but I basically am breaking down everything that we're doing into these Kanban cards that we can see pretty quickly where they're at.

**George Haikal:** Because there's already a lot of moving parts.

**George Haikal:** I have probably four more to add.

**George Haikal:** So we'll be able to review it like this.

**George Haikal:** I think it would be more helpful, kind of linear-esque.

**George Haikal:** But for now, I'm stitch it together.

**George Haikal:** Boom, boom, boom.

**George Haikal:** I'm to see you guys, too, just in case.

**George Haikal:** I don't know.

**George Haikal:** Before I forget, me just bring Sebastian DM them.

**George Haikal:** It's tough because of the time difference.

**Georgemaine Lourens:** Okay, I'm in.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Well,

**Georgemaine Lourens:** Oh, from top to bottom?

**George Haikal:** Just checking in on our lovable account and seeing if we can get some more credits for the templates.

**George Haikal:** So, yeah, if we want to bucket it back, this top-down is still all templates, so yeah, that's fine.

**George Haikal:** How did that meeting go with Felix?

**Georgemaine Lourens:** Good.

**Georgemaine Lourens:** He didn't really have any feedback.

**Georgemaine Lourens:** He was just kind of like switch the buttons around and change some icons.

**Georgemaine Lourens:** He's basically working on a very similar page, but for projects.

**Georgemaine Lourens:** So I think Nat just kind of wanted us to sync just for the sake of syncing.

**George Haikal:** Did you incorporate the minor edits, basically?

**Georgemaine Lourens:** Yeah, minor edits.

**Georgemaine Lourens:** I do not know what the changes are that Nat is requesting because I can't get access to his own recording.

**Georgemaine Lourens:** Um...

**Georgemaine Lourens:** I'm not sure if you have access to it.

**Georgemaine Lourens:** I can ping him later.

**Georgemaine Lourens:** It's not that urgent, I think.

**George Haikal:** Well, we want to get to publishing here, so this will be good to unblock.

**George Haikal:** Let's see.

**Georgemaine Lourens:** I don't think it's blocking.

**George Haikal:** Yeah, true.

**George Haikal:** Which I'll just pull it on the screen so we can see.

**Georgemaine Lourens:** It's in the external chat.

**Georgemaine Lourens:** Do you see that original message there before the yesterday?

**Georgemaine Lourens:** Yeah, that one.

**Georgemaine Lourens:** This one is paywall or email wall.

**Georgemaine Lourens:** Oops.

**Georgemaine Lourens:** Thank you.

**George Haikal:** Thank you.

**George Haikal:** All right, cool, good, so we're pending, pending nads, loom to see if there's any changes, but he basically deferred to Felix, so like we could just operate as if we're good to go.

**Georgemaine Lourens:** Yeah, I think in terms of the library, well, maybe we could finish with the templates first and then move to the library.

**Georgemaine Lourens:** So the templates, I think there are three that are publish ready, and I'm working on the other ones, and I'll probably pull in Saturday to finish those as well, because I had some, I had to work on the Sentinel account, but I think the seven templates will be done by the end of the weekend, and those will be ready to publish.

**Georgemaine Lourens:** But for the templates, and the gallery itself, and the

**Georgemaine Lourens:** Me and Nico, we spoke earlier today, and I think if we want to ship that quickly, then we need to make a few changes there.

**Georgemaine Lourens:** So right now we have the category navigation, right?

**Georgemaine Lourens:** And if we're going to ship seven templates, then having all of the categories and search and all of that doesn't make any sense because it's seven.

**Georgemaine Lourens:** So our idea was to strip it down to a bare minimum experience.

**Georgemaine Lourens:** And we keep all of the pages that are indexable, and we remove the tags as well.

**Georgemaine Lourens:** Essentially, we're just stripping it down to the MVP experience.

**Georgemaine Lourens:** If you want to push back on that, then let me know, but I think that's the best way forward, and then we just keep adding until we have enough.

**George Haikal:** Yeah, we can just add by category as we go, and like starting with websites, and then the websites can branch down.

**George Haikal:** So this is a blog, like publication or blog template or something.

**George Haikal:** And then the next one that we're doing that I can jump into is portfolio websites and I can show you like how we were thinking about the branch out.

**George Haikal:** But yeah, whatever you all need to do to cut down to get it launched is fine because it's going to be hidden anyway to start.

**George Haikal:** We already have to agree to that this week.

**George Haikal:** Okay, cool.

**George Haikal:** Totally agree.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** And then there were two other parts.

**Georgemaine Lourens:** I think Nico could speak better to that.

**Georgemaine Lourens:** I think so to the templates is one part, stripping down to the bare essentials is another, and then the content.

**Georgemaine Lourens:** So I saw the content that Ada shared, and that's great.

**Georgemaine Lourens:** But we still need some other content.

**Georgemaine Lourens:** We have the feature list on the right, and that's currently hard-coded.

**Georgemaine Lourens:** I think we can probably, like worst case scenario, we can just rip off what

**Georgemaine Lourens:** What the Webflow has, best case scenario, we come up with something better.

**Nicolas Castellanos:** Yeah, for that, I mean, for this set of templates, I was thinking to grab the artifacts and write something quickly on Cloud to get those.

**Nicolas Castellanos:** But there's another problem, which is we have, like, I don't know how many, but it's what George made, three travel blog posts?

**Nicolas Castellanos:** Something like that?

**Nicolas Castellanos:** At least a couple.

**Nicolas Castellanos:** Then for food, there is a couple.

**Nicolas Castellanos:** So those are going to get repetitive.

**George Haikal:** That's a problem.

**George Haikal:** Well, I think we have architecture, fashion, food, newsletter, travel, right?

**Nicolas Castellanos:** And then two more?

**Georgemaine Lourens:** Yeah, but...

**Georgemaine Lourens:** There's two more.

**Nicolas Castellanos:** But do we, like, for food, we have a couple.

**Nicolas Castellanos:** Like, we have, it's, let me check the names, but we have...

**Nicolas Castellanos:** It's Culinary Culture and Perspective Food, both templates are for food.

**Nicolas Castellanos:** Do we copy, like, the content?

**Nicolas Castellanos:** No, right?

**Georgemaine Lourens:** We can change them, I guess.

**Georgemaine Lourens:** I mean, changing the content isn't as difficult as...

**George Haikal:** Yeah, as long as it's optimized for the keyword, it's fine.

**George Haikal:** It can, like, read different, like, if they're two different ones, like, they're slightly different styles.

**George Haikal:** So if the way, like, it goes down to, like, right now we can do whatever we want for them, but, like, how is it going to work in the pipeline?

**George Haikal:** Like, where are the inputs going to be, right?

**George Haikal:** Because then everything will flow down from that.

**George Haikal:** And so, like, if it's going to be the keyword we're searching for, like, the name of the template, the keyword we're trying to optimize for, and then a description of the template, then everything that's generated after will be different regardless of it would solve for this, right?

**Nicolas Castellanos:** Yep.

**Nicolas Castellanos:** No, no, for a template, we're clear.

**Nicolas Castellanos:** Parameter are these seven templates.

**George Haikal:** Got it.

**Nicolas Castellanos:** Got it.

**George Haikal:** But to be honest, I don't think it's multiple templates under the same category, that's okay.

**George Haikal:** Yeah, I agree.

**George Haikal:** But what Nico's saying is he doesn't want it to read the exact same, which I also agree with.

**George Haikal:** Oh, yeah, that's right.

**George Haikal:** Yeah, the content under it, yeah.

**George Haikal:** Being in the same category, totally fine.

**George Haikal:** Like, it should be in the same category, but reading exactly the same.

**Nicolas Castellanos:** yeah, yeah, I think it was, I didn't want to, like, copy and paste the same.

**George Haikal:** 100%.

**George Haikal:** Yeah, so, like, the example here is, like, Voyager and then Perspective, right?

**Nicolas Castellanos:** Yeah, but not that perspective.

**Nicolas Castellanos:** There's another one, I think.

**Nicolas Castellanos:** There's two Perspective.

**Georgemaine Lourens:** One is for food and another is for...

**Georgemaine Lourens:** Yeah, we have food stories and we have culinary cultures.

**Nicolas Castellanos:** you much.

**Nicolas Castellanos:** Thank

**Nicolas Castellanos:** And then for travel, I think there are also a couple.

**George Haikal:** But this is more of like a newsletter.

**Georgemaine Lourens:** Yeah, more recipes.

**Georgemaine Lourens:** It was just me winging it.

**George Haikal:** No, but that's the nuance we can capture in, and that's how we can make it different is for these.

**George Haikal:** Like, we can prompt it, and like, this can come from more of like a sign-up newsletter angle to get the stories on the food and culture.

**George Haikal:** And this one seems more like a traditional blog, right?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think that's a good way of distinguishing them.

**George Haikal:** And we got to get the remix to work too, right?

**Nicolas Castellanos:** Yeah, I have that, I think, working on another PR.

**Nicolas Castellanos:** Because thank you very

**Nicolas Castellanos:** A new one with only our templates.

**Nicolas Castellanos:** So we didn't lose this one, which has all the content.

**George Haikal:** Oh, nice.

**George Haikal:** Is there anything blocking there from on their side?

**Nicolas Castellanos:** The remix, but it should be working.

**Nicolas Castellanos:** have the PR is failing because I'm still fixing stuff.

**Nicolas Castellanos:** But once it's up, I'll be able to test the remix.

**Georgemaine Lourens:** I didn't see that.

**George Haikal:** It was last night late.

**George Haikal:** Don't they have the 1Password?

**Nicolas Castellanos:** Yeah, they need to get it from their own.

**Nicolas Castellanos:** We cannot share it to them.

**Georgemaine Lourens:** Yeah, then...

**Nicolas Castellanos:** Yeah, we should just tell them to ask for can or go to their own 1Password.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So have they not seen the template yet?

**George Haikal:** They have.

**George Haikal:** Wow.

**George Haikal:** She probably just wants to show it to people.

**Georgemaine Lourens:** Okay, yeah, I know that's a good sign.

**George Haikal:** We can just send us the message in the external.

**Georgemaine Lourens:** Yeah.

**George Haikal:** And then is the...

**George Haikal:** I'm sure.

**Georgemaine Lourens:** Oh, and Nico, do we have a...

**Georgemaine Lourens:** Can we use...

**Georgemaine Lourens:** Do we have a pipeline for the page meta descriptions?

**Georgemaine Lourens:** Or do they handle those on their end?

**Nicolas Castellanos:** No, we need to handle those.

**Nicolas Castellanos:** We don't have anything.

**Nicolas Castellanos:** For content, we don't have a pipeline yet.

**George Haikal:** Okay.

**George Haikal:** Yeah.

**Georgemaine Lourens:** probably reuse something.

**Nicolas Castellanos:** Yeah, we will use...

**Nicolas Castellanos:** Like, I mean, we have pipelines all over.

**George Haikal:** So here, Georgemaine, for CC's response, is there an easy way to just have this and then have the gallery linked as well, just so they can all see it, all in one, and then have the password?

**Georgemaine Lourens:** Yeah, well, it's all linked to the detail pages.

**Georgemaine Lourens:** So I think if we just, they have the password and one password, right?

**George Haikal:** But she's asking.

**Georgemaine Lourens:** Yeah, I think what Nico said is probably the easiest way to handle it, like, refer her to the password.

**Nicolas Castellanos:** Yeah, that's what Furkan asked us to do, like, not to share with them, just tell them to go to one password or ask for it.

**Georgemaine Lourens:** Where did he say that?

**Georgemaine Lourens:** Maybe we can...

**Nicolas Castellanos:** a thread, like, it's in a thread, like, two weeks ago, when I asked if we could share that password, he told me that it's fine to share

**Nicolas Castellanos:** Share for us internally, but for the channel, with them, they need to go to their own one password.

**George Haikal:** This is freaking boss.

**George Haikal:** This is like the top.

**Georgemaine Lourens:** Here we go.

**George Haikal:** I found it.

**George Haikal:** Nice.

**Georgemaine Lourens:** No, I didn't.

**Georgemaine Lourens:** Sorry.

**Nicolas Castellanos:** I can look for it.

**Nicolas Castellanos:** But yeah, I mean, it's probably fine.

**George Haikal:** We can just DM her.

**George Haikal:** We can just DM her the password and say, hey, check your one password.

**Nicolas Castellanos:** also DMed it to you.

**Nicolas Castellanos:** Yep.

**Georgemaine Lourens:** Yeah, could we just kind of like just pin the gallery deploy link to the channel?

**Georgemaine Lourens:** Because I feel like we should all just use the same link so that everyone can just get to Ooh, what about files here?

**George Haikal:** No.

**George Haikal:** I've never used Canvas.

**Nicolas Castellanos:** I haven't I

**Georgemaine Lourens:** I never will.

**George Haikal:** Yeah, I don't think I will.

**George Haikal:** Honestly, that kind of is a good way to pin it, though.

**George Haikal:** This is just like, here's the most updated version of the stuff we're working on.

**George Haikal:** We could do it, I guess.

**George Haikal:** No, we're going to worry about that right now.

**George Haikal:** I'll just send a message here.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** But yeah, to summarize, I think in order to ship this, we need the templates ready, which is on my plate, and we need final content for, I think the descriptions are there, but we're lacking two.

**Georgemaine Lourens:** And we need a way to populate the key highlights and the features and capabilities.

**Georgemaine Lourens:** I'm not sure how to go about that one, but you had an idea, right, Nico?

**Nicolas Castellanos:** go.

**Nicolas Castellanos:** Right.

**Nicolas Castellanos:** Can you repeat that?

**Georgemaine Lourens:** Sorry.

**Georgemaine Lourens:** For the key features, the key features and the highlights.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Highlights and key features, I can get those.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** So why don't just kind of make like a little to-do list here?

**George Haikal:** Thank you.

**George Haikal:** That's helpful.

**George Haikal:** I mean, I'll clear all of this on the chat there.

**George Haikal:** Sorry, was there a password link you were sending me, Nico, or?

**George Haikal:** It's the name of the password.

**George Haikal:** Oh, it's the same.

**George Haikal:** Okay.

**George Haikal:** Well, I don't know if there's a different one.

**George Haikal:** No.

**George Haikal:** There's the county.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** Let's move this for.

**Nicolas Castellanos:** I can send one to you that it's only allowed to be open one time, that works.

**George Haikal:** What would, you mean, so I could send it to Cece, or what do you, what do you mean?

**Nicolas Castellanos:** Yeah, so you can send it, yeah.

**George Haikal:** Sure.

**George Haikal:** Yeah, mean, Cece can have the concept link, like, she's trustworthy, she's, like, the number one person.

**George Haikal:** And we're working with.

**George Haikal:** Yeah, it's pretty cool.

**George Haikal:** Look, I think the link we, unless there's any concerns there, Nico, but I think the link we use, it's fine to DM it to Cece.

**Nicolas Castellanos:** I'm not concerned at all for anyone having access.

**Nicolas Castellanos:** I'm just trying to be cautious, because they, I mean, Ford can tell me not to share it.

**George Haikal:** So, God, but Cece, so.

**George Haikal:** I'm going DM it to CC.

**Nicolas Castellanos:** I won't share it externally in the channel, though.

**Nicolas Castellanos:** Yep.

**George Haikal:** Yeah, if you could shoot that to me, that'd be great.

**George Haikal:** Password should be in your org.

**George Haikal:** That's what you're doing here.

**George Haikal:** Cool.

**Nicolas Castellanos:** I sent you to Slack.

**Nicolas Castellanos:** Yeah, through Zoom, sorry.

**George Haikal:** Oh, sorry.

**George Haikal:** Thank you, sir.

**George Haikal:** Yeah.

**George Haikal:** I don't say that you said the not-taker by accident.

**Nicolas Castellanos:** I always do that.

**George Haikal:** Yeah, I hate this.

**Nicolas Castellanos:** I always do that.

**George Haikal:** What can you even say?

**Nicolas Castellanos:** Oh, you can just tell what to leave.

**George Haikal:** I do it all the time.

**George Haikal:** I think people are ignoring me sometimes.

**George Haikal:** They don't respond.

**George Haikal:** Just the not-taker eating it.

**Nicolas Castellanos:** Not the first it happened to me, though.

**Nicolas Castellanos:** It's like, I don't know why it did.

**Nicolas Castellanos:** It's it's default when you go there.

**Nicolas Castellanos:** there.

**Nicolas Castellanos:** go.

**Nicolas Castellanos:** Oh, wait.

**Nicolas Castellanos:** If you're sharing it to two people, that won't work.

**Nicolas Castellanos:** Let me send you...

**Nicolas Castellanos:** It won't work?

**Nicolas Castellanos:** No, because it's set to be open one time only.

**Nicolas Castellanos:** I can keep it free.

**Nicolas Castellanos:** The thing is, there's going to be a link to a password that's not ours out there.

**Nicolas Castellanos:** That's the only...

**Nicolas Castellanos:** But they can do whatever you think is best.

**George Haikal:** So, okay, help me understand, because Cece and Rachel are like the CMO and then like the head of growth or something, so they are two direct stakeholders.

**George Haikal:** So, to me, it would be fine if they have this thing, but if they send it out, then like we can't manage.

**Nicolas Castellanos:** Yeah, once we send this link to Slack, it's out in the internet, holding a password window now.

**Nicolas Castellanos:** So that's...

**George Haikal:** Okay, so I'll send it just to CC.

**Nicolas Castellanos:** They are being careful with the password, then, yeah.

**Nicolas Castellanos:** Okay.

**Georgemaine Lourens:** Great photo.

**George Haikal:** Hairs?

**Georgemaine Lourens:** Yeah, kind of like the lighting and the flapping hair.

**George Haikal:** Oh.

**Georgemaine Lourens:** Great for mock-ups.

**Georgemaine Lourens:** Totally unread.

**Georgemaine Lourens:** I am a designer, after all.

**George Haikal:** Thank you.

**George Haikal:** Cool.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** I kind of made a little to-do list for what we need in order to ship the library, gallery, or whatever.

**Georgemaine Lourens:** I think this should be pretty complete.

**Georgemaine Lourens:** Right, Nico?

**Georgemaine Lourens:** Or am I missing anything here?

**Nicolas Castellanos:** No, it should be-

**Nicolas Castellanos:** It should be there.

**Nicolas Castellanos:** We're, like, stripping stuff out.

**Nicolas Castellanos:** We need to replace content.

**Nicolas Castellanos:** And there are some changes we need to make to, like, make the code good and being able to pass the review.

**Nicolas Castellanos:** But we're good.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think this should be, like, two days of work, three max, right?

**Nicolas Castellanos:** I can probably get it done today, yeah, two max.

**Nicolas Castellanos:** Yeah, I don't think they're going to hold us much there, because it's, like, it doesn't touch anything else on the platform.

**Georgemaine Lourens:** You never know.

**George Haikal:** Yeah.

**Nicolas Castellanos:** Oh, one thing, George.

**Nicolas Castellanos:** We removed the...

**Nicolas Castellanos:** The view count, because we don't have a way to track view count.

**Nicolas Castellanos:** If we want the view count, we need to think how we're going to build that out.

**Nicolas Castellanos:** Because for that, we will need them.

**George Haikal:** What's the benefit?

**Nicolas Castellanos:** I don't think there is.

**Nicolas Castellanos:** Just a number to track popularity, maybe.

**Nicolas Castellanos:** But that's it.

**Nicolas Castellanos:** I guess the view count on how many people have seen this template.

**George Haikal:** So would we be able to see that in GSC for the next?

**Nicolas Castellanos:** Yes, I think so.

**Nicolas Castellanos:** We need a way to get that from GSC and put it on the site.

**Georgemaine Lourens:** That's a good call.

**Georgemaine Lourens:** We should probably make sure that we can track this stuff.

**George Haikal:** Oh, yeah.

**George Haikal:** I mean, I already set up there.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** By the way, George, your calendar, Jesus Christ.

**George Haikal:** Oh, dude, this is the best it's been.

**George Haikal:** I feel amazing about it.

**George Haikal:** It usually gets bad.

**George Haikal:** Like some of the prospects, and like this is not even, like these are meetings, this is not even like work to be done.

**George Haikal:** But I've chilled it out, which is good.

**George Haikal:** I've got a lot of time back, and like a lot of these were, like this was work sessions, and color coding it and organizing it a bit more, but definitely no lack of work, man.

**George Haikal:** Oh, why can't I?

**George Haikal:** I'm all of my code, that's why.

**George Haikal:** What's the, there's the road trail.

**Georgemaine Lourens:** Let me try deleting your cookies.

**Nicolas Castellanos:** What's up?

**Nicolas Castellanos:** up?

**George Haikal:** I think that's, I'll show you, it's cool, but this should just work, what the , one sec, because it's important, this is how we're going to track all the progress, moving forward.

**Georgemaine Lourens:** Ah, here we go.

**George Haikal:** Ah, I took this, that's fine.

**George Haikal:** Dude, every 14 days, I know.

**Georgemaine Lourens:** So annoying.

**George Haikal:** Ah, one sec.

**George Haikal:** Ah,

**George Haikal:** This should be lovable love dev, right?

**Nicolas Castellanos:** Yeah.

**George Haikal:** This is not even going to come up.

**George Haikal:** Awesome passion for that.

**George Haikal:** Right?

**Georgemaine Lourens:** This won't come up if it's different.

**Georgemaine Lourens:** Yeah.

**George Haikal:** But what you would do is you'd go to Pages, and then you'd go to Add Filter by Page, URLs containing slash guides.

**George Haikal:** Obviously, there's none now, but you'd be able to see if the pages are getting impressions or clicks.

**George Haikal:** Thank you.

**George Haikal:** Thank you.

**George Haikal:** And how many, the same for templates, too, so.

**George Haikal:** I'll ask them for GSE access for lovable.dev.

**George Haikal:** Those are two separate things, right?

**Nicolas Castellanos:** I think so, yeah.

**Nicolas Castellanos:** The app domain, I think it's for the apps, like the projects, will.

**Nicolas Castellanos:** The database, the landing page.

**Georgemaine Lourens:** I'm just going to pin your message to the channel.

**Nicolas Castellanos:** It has a direction from app to dev, though.

**Nicolas Castellanos:** I don't know.

**Nicolas Castellanos:** Maybe it works anyway.

**George Haikal:** Right now, I have a client that gave me access to their Google Search Console for, their .app.

**George Haikal:** But they also have a .dev domain, which we're actually posting the guides on with articles I want to track.

**George Haikal:** If I have access to the lovable.app on their Google Search Console, will I be able to see what happens, impressions, clicks, et cetera, on the stuff we're doing on their lovable.dev, or do I need to get access to that separately?

**George Haikal:** Even if it redirects, you'll only start seeing data on the app properly.

**George Haikal:** Yeah, so.

**George Haikal:** Half of this life is just like asking questions of the  you don't know, figuring it out.

**Nicolas Castellanos:** You probably use audio, though.

**Nicolas Castellanos:** I usually just write.

**George Haikal:** Yeah, Whisperflow, W-I-S-P-R, so helpful.

**George Haikal:** That's what I just use.

**George Haikal:** You just click a button on your laptop and it dictates and it's so good.

**George Haikal:** It like organizes it and it can tell when you're asking questions and it formats everything very well.

**Nicolas Castellanos:** That's cool.

**Nicolas Castellanos:** Yeah, I think I only use, like, I only talk to it when trying to, like, talk, like, I don't know, crazy things.

**Georgemaine Lourens:** Crazy things?

**Nicolas Castellanos:** No, but ideas that come to mind.

**Nicolas Castellanos:** Like, questions, like, I don't know.

**Nicolas Castellanos:** But whenever I'm serious, I just start writing.

**Nicolas Castellanos:** I don't know why.

**Nicolas Castellanos:** I don't know why.

**Nicolas Castellanos:** You

**George Haikal:** Do you remember who gave it to us before?

**George Haikal:** Perkin.

**George Haikal:** Perkin might as well add him, right?

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** She's from Sweden, right?

**George Haikal:** Rachel?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Oh, no, Rachel's from America, I think.

**Georgemaine Lourens:** I was confused with CC.

**Georgemaine Lourens:** CC was from Sweden, I believe.

**Georgemaine Lourens:** Just thinking about time zones here, like Europe, she's probably going to be off.

**Georgemaine Lourens:** But Rachel was US, right?

**George Haikal:** Correct.

**Nicolas Castellanos:** Yeah, it's usually on around this time.

**George Haikal:** Cool.

**George Haikal:** In the future, would just go.

**George Haikal:** Each one of these would be a ticket, right?

**George Haikal:** there's going to be so many moving parts that I'll add them here.

**George Haikal:** So each meeting will be able to run against these more efficiently.

**George Haikal:** Cool.

**George Haikal:** able to run to to to

**George Haikal:** That makes sense.

**Georgemaine Lourens:** You wanna talk over?

**George Haikal:** Templates.

**Georgemaine Lourens:** The after we ship part?

**George Haikal:** Yeah, so the setting of the pipeline for the template, the content on the templates.

**Nicolas Castellanos:** Yeah, but first let's just to be the three of us on the same page, the stuff we are stripping out for, like, the first seven, ten templates.

**Nicolas Castellanos:** We are not gonna have, like, the category bar in the site, because it doesn't make sense.

**Nicolas Castellanos:** We're gonna have the category page, and that will get indexed, but we won't have the bar, because we will only have only one category, which will be blogged.

**George Haikal:** I don't know what mean here, just we're on the same page.

**Nicolas Castellanos:** That bar won't be there.

**Nicolas Castellanos:** Those, yep.

**George Haikal:** Jessica, can websites be there?

**George Haikal:** Yeah, we can, yeah.

**George Haikal:** Because we'll go to templates, websites, and then everything we're doing is just a sub or branch off of website right now, right?

**George Haikal:** Yeah, it's a blog, yeah.

**George Haikal:** And then in the future, we'll be able to add under...

**Georgemaine Lourens:** So you would keep one item there?

**George Haikal:** Does that look worse since it's all templates?

**Georgemaine Lourens:** It's just...

**Georgemaine Lourens:** I think we don't even need it, right?

**Georgemaine Lourens:** I think we can just get rid of it because it will always be there.

**Georgemaine Lourens:** Like, the only way that you would get here would be if you were to navigate from the detail page or if you have a direct URL.

**Georgemaine Lourens:** But even if you get there, there's like six templates and that's it.

**Georgemaine Lourens:** I think we should just get rid of all of the categories.

**Georgemaine Lourens:** the only trade-off there is we wouldn't be able to see...

**George Haikal:** Well, if they click into each one...

**George Haikal:** Y- Y Y You

**George Haikal:** And we wouldn't be able to see it by category, but that doesn't matter yet because we don't have enough to, because what we want to do here is we want to see what's working best and we want it to double down on what's working.

**George Haikal:** And so if we're able to see the individual pages, then that solves for it.

**George Haikal:** Like we don't need a bucket of category.

**George Haikal:** That's more like a visual thing to help people like mentally organize it.

**George Haikal:** And so I don't think it's, yeah, it's not needed for the MVP right now.

**Nicolas Castellanos:** Agreed.

**Nicolas Castellanos:** The filter on latest and popular thing you have, drop-down you have, yeah, that's gone too.

**Nicolas Castellanos:** Because we don't have anything to filter on right now.

**Nicolas Castellanos:** And the search bar, it's also gone.

**Nicolas Castellanos:** Because for seven templates, no point to have a search bar.

**Nicolas Castellanos:** So, section.

**Nicolas Castellanos:** We're the next section.

**Nicolas Castellanos:** Let's If we're going to go next section.

**Nicolas Castellanos:** We're to next section.

**George Haikal:** Now let's take a little And I'm

**George Haikal:** Makes sense.

**George Haikal:** Cool.

**George Haikal:** Any other questions here at end?

**George Haikal:** Like, we're just going to solve for, like, the two remaining ones that are similar.

**George Haikal:** One is more of newsletter angle, and the other travel one is Voyager, right?

**George Haikal:** Like, we're to see whatever the difference is here and just, like, highlight it in a prompt, and it'll make a difference.

**Nicolas Castellanos:** Does that make sense?

**George Haikal:** Cool.

**George Haikal:** Cool.

**George Haikal:** Anything else on there, Nico?

**Nicolas Castellanos:** I think not, unless you just make and think of anything else.

**Nicolas Castellanos:** I think that's all we are removing.

**Georgemaine Lourens:** I think if you just strip this down while I work with Claude to finish the templates, then I'll do the changes from Felix on your branch.

**Georgemaine Lourens:** And all details.

**Georgemaine Lourens:** If Nad has this feedback done, then I'll fix those, and otherwise, whenever he gives access, we'll do his polish round.

**Nicolas Castellanos:** Cool.

**Georgemaine Lourens:** And then we work with Ada to get the features and the remaining content.

**George Haikal:** If you can give team access, that would be ideal.

**George Haikal:** Team at growthxlabs.com.

**George Haikal:** But if you need individual users, you can just duplicate the ones who have access on the lovable.

**George Haikal:** Basically, George.

**George Haikal:** Yeah.

**George Haikal:** And there.

**George Haikal:** Yeah.

**George Haikal:** Okay.

**George Haikal:** Okay.

**George Haikal:** Okay.

**George Haikal:** Thank

**George Haikal:** So, that's growth, bobs.com, like you both as well.

**George Haikal:** George, ma what's your email?

**Georgemaine Lourens:** Is it George, G-E-O or G-E-M-A?

**Georgemaine Lourens:** ma'am, G-E-O, yeah, ma'am, yeah, frontname, at George, at growthx.ai.

**Georgemaine Lourens:** Oh, you can tell that it's late for me.

**George Haikal:** Yeah, we'll do these earlier too, and then Nico, is yours just Nico?

**Nicolas Castellanos:** No, it's the full name, I'll send it to you.

**George Haikal:** Nicolas?

**Nicolas Castellanos:** Yeah, Nicolas.Castellanos, W-O.

**George Haikal:** Oh, there.

**Nicolas Castellanos:** This one?

**Nicolas Castellanos:** Yeah.

**George Haikal:** How come your .last name?

**Nicolas Castellanos:** I I should get an alias in there.

**George Haikal:** Why are you, why is it first .last for you?

**Georgemaine Lourens:** Yeah, you're the only Nicolas we have, right?

**Nicolas Castellanos:** I don't know, I just got that one.

**Nicolas Castellanos:** So, Nico at growthx would have been sweet.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** I can ask who's managing, Yusuf.

**George Haikal:** I can ask Yusuf.

**George Haikal:** Yeah, yeah, definitely ask Yusuf if it looks cleaner.

**George Haikal:** Cool, and then quickly, then I'll give you guys the time back.

**George Haikal:** So then on the templates, Georgemaine and Nico, just so like we're all on the same page moving forward.

**George Haikal:** This is what we ran them through last meeting.

**George Haikal:** So here's like our plan for the templates.

**George Haikal:** We're already on track here.

**George Haikal:** We told them we would publish under a website's category.

**George Haikal:** But that's not really like a deal breaker, right?

**Georgemaine Lourens:** I mean.

**Georgemaine Lourens:** No, I think it's fine.

**Georgemaine Lourens:** I think the idea that Ada passed with the first trial is kind of like you have websites, a main category, and under that you kind of have a blog.

**George Haikal:** Yeah, yeah.

**George Haikal:** So that's a perfect segue.

**George Haikal:** Because basically I spelled out the ones we're going to target first.

**George Haikal:** I'm just going to kind of show you guys the why behind it.

**George Haikal:** We'll just say Airtable loads.

**George Haikal:** So basically we looked up and pulled in all of the competitive templates that like Wix, Webflow, any other competitors were doing, and then rolled it up into actual keywords.

**George Haikal:** What keywords were these URLs, these templates targeting?

**George Haikal:** And were those templates category pages or were they actual templates themselves?

**George Haikal:** And so all of that kind of just search volume, difficulty, and then the intent.

**George Haikal:** And then you can see here, we also mapped them by difficulty level, but like AI generated categories as well.

**George Haikal:** like what are the actual topics these are covering under, like within a website, right?

**George Haikal:** So like one level deeper, two levels deeper.

**George Haikal:** And then what we did was organize that and bucket it all into the high level categories, which would be like either the first level website or one below, and then prioritize that by search volume for the next set of templates that we want to start executing on, like for the next month, right?

**George Haikal:** We want all the low-hanging fruit of search volume.

**George Haikal:** And what's the easiest to start getting clicks for and traffic for?

**George Haikal:** And what that showed us was let's prioritize websites right now.

**George Haikal:** We're on the same page with Lovable there.

**George Haikal:** We don't need to get into many apps.

**George Haikal:** They're a little more complex and the search volume is not even anywhere close to the same as...

**George Haikal:** And the number one by far were portfolio websites.

**George Haikal:** And so that's where we should start next week.

**George Haikal:** And here I broke down a list with some examples too.

**George Haikal:** So portfolio itself, right?

**George Haikal:** There's a lot within it and that can be broken down into a few different variations.

**George Haikal:** And then other categories like resume and CV and then personal website all fall into that bucket too.

**George Haikal:** And I thought a good example to show just to help ground everything was Wix, right?

**George Haikal:** So this is where you land when you're on portfolios.

**George Haikal:** And then there's the three different buckets that you can go into, right?

**George Haikal:** Resumes, CVs, and then just personal.

**George Haikal:** And then within each one, there's the different types.

**George Haikal:** artist, portfolio, photographer, I thought they did a really good job here.

**George Haikal:** And it's an easy way for us to get variations of this up quickly, all in the mindset of this already has the most search volume.

**George Haikal:** And so...

**George Haikal:** So if we can start here next week, I think that's going to be the most impactful to show them the earliest wins that we could.

**Georgemaine Lourens:** Yeah, no, I think that makes sense.

**Georgemaine Lourens:** So our strategy will be to target, to drive traffic to the category pages, right?

**Georgemaine Lourens:** Not the individual template page.

**George Haikal:** Yeah, I mean, that's, yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right, makes sense.

**George Haikal:** But I mean, both will be done, right?

**George Haikal:** Like, this will be specific for our list, and then portfolios in general, like, it could do both.

**Georgemaine Lourens:** Yeah, it could do both, yeah.

**George Haikal:** But to me, that's where I think, like, the best place to start is.

**George Haikal:** You could all, like, root it in this.

**Georgemaine Lourens:** Yeah, I think makes sense.

**Georgemaine Lourens:** The only concern that I would have would be around designers.

**Georgemaine Lourens:** do.

**Georgemaine Lourens:** There's a that's

**Georgemaine Lourens:** Because designers are very picky and not very converting, but all the other ones are, let's do it.

**George Haikal:** Nice, okay, cool.

**George Haikal:** So we know the next set to go after.

**George Haikal:** Photographer would be super easy.

**George Haikal:** These, I think, Nico, how hard are variations of these going to be with the workflow?

**Nicolas Castellanos:** I don't think that hard at all, right?

**Nicolas Castellanos:** No, it's not.

**Nicolas Castellanos:** No, it should, I mean, yeah, it's essentially great, so.

**Georgemaine Lourens:** Yeah, I think we just need to figure out kind of like what the page structure is for most of these, but to me, it seems like a homepage, an about page, a contact page, and probably a work page, and that's it.

**Georgemaine Lourens:** Yeah, let's have a second.

**George Haikal:** Cool.

**George Haikal:** Yeah.

**George Haikal:** That's weird.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** We just need to find, like, great images on Unsplash.

**Nicolas Castellanos:** And, yeah.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Or we need to cut out Unsplash and just kind of make an image workflow for it.

**George Haikal:** Or it might be hard to match, right?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** maybe.

**Georgemaine Lourens:** But these are very simple.

**George Haikal:** Yeah.

**George Haikal:** I mean, we could do better than this, too.

**George Haikal:** Like, you all use your expertise to, like, come up with whatever is most feasible for the workflow and also, like, looks the best.

**George Haikal:** But ideally, Georgemaine, like, I don't, like, we don't want you spending two hours on each one.

**George Haikal:** Like, that's not sustainable for your time, right?

**George Haikal:** And so, two, three hours plus.

**George Haikal:** And so.

**George Haikal:** And

**George Haikal:** I guess, just, and you're already doing it, but like, think about it, like, up front from the lens of, we want to do a bunch of these, right?

**George Haikal:** The variations are what matter here, and so we already have their trust on quality.

**George Haikal:** So as long as we hit a similar type of quality, then let's just solve for how repeatable can we make this, that it still looks good.

**George Haikal:** So the trade-off is, let's do more, and, like, they'll look good enough.

**George Haikal:** Like, your quality bar is massively high, and they love it.

**George Haikal:** Like, they're blown away.

**George Haikal:** And so if we think of, like, the scalability piece now, like, I think we'll be in a good spot.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** No, I'm with you on that.

**Georgemaine Lourens:** Like, I feel like we have to trust now, and now it's just a matter of, like, how do we set up a workflow here so anyone else can know this.

**George Haikal:** Yeah.

**George Haikal:** So what is most helpful here?

**George Haikal:** I mean, it sounds like you all have to think through it.

**George Haikal:** I sounds through through I like through I mean, mean,

**George Haikal:** Just figure out, do you need, like, any more help?

**George Haikal:** Is it just, like, a time thing?

**Nicolas Castellanos:** No, it's probably time.

**Nicolas Castellanos:** We need to figure out, like, I don't know, Georgemaine, for this, I'm thinking the collections you found in Unsplash are great for these pages because it's just images from those great collections, and that's it.

**Nicolas Castellanos:** And then for, like, designs and ideas, I think we got the recipe last Wednesday.

**Nicolas Castellanos:** So that's a way, which is just giving it, like, the sample components we need, launch a few iterations, and that's it.

**Georgemaine Lourens:** Yeah, yeah, exactly.

**Georgemaine Lourens:** I think we just need to figure out the page structure and then make sure that we have the right components for it, and then gather a bunch of inspiration and some themes that it can use, and then when we have enough credits, we just blow their credits away and to do.

**Nicolas Castellanos:** Yeah, yeah.

**Georgemaine Lourens:** Thank you.

**George Haikal:** Go from there, and then either it is.

**George Haikal:** Yeah, yeah, and we can do a few of each category.

**Georgemaine Lourens:** Yeah, but I think we need way, is there a way that we can kind of get like unlimited credits in a way?

**George Haikal:** Yeah, let me ask, yeah.

**Georgemaine Lourens:** Because if we're going to rapid fire a bunch of these, like 1K or 2K credits is not enough.

**George Haikal:** Yeah, I agree.

**George Haikal:** I agree.

**George Haikal:** I'll ask.

**Georgemaine Lourens:** But, yeah, no, other than that, like, it's looking good.

**Georgemaine Lourens:** I don't think we'll be able to ship today, but we can definitely ship them, like, or have it shipped ready by Tuesday.

**Georgemaine Lourens:** And after that, we can work on the template..波 we'll

**Georgemaine Lourens:** That's for that batch this week.

**George Haikal:** Totally fine.

**George Haikal:** How do you all feel time-wise, workload-wise, energy-wise?

**Nicolas Castellanos:** It's great.

**Nicolas Castellanos:** Fine.

**Georgemaine Lourens:** I'll try to get fun.

**Nicolas Castellanos:** Yeah, yeah, we're great.

**Georgemaine Lourens:** I mean, I think the only thing on my end is that I have to help Marcus for two days next week with SentinelOne.

**Nicolas Castellanos:** I can help with that if you need.

**Georgemaine Lourens:** You're doing, like, mostly front-end, right?

**Georgemaine Lourens:** No, I think this is more of a design thing now, so I have to tell.

**Nicolas Castellanos:** Yeah, if you need help with the code, I can tell.

**Georgemaine Lourens:** Yeah, thanks for offering, but I think we should be good.

**George Haikal:** Cool.

**George Haikal:** And then, Nico, when you set up the, or think through the setting up the pipeline for the content for the templates, can you ping me?

**George Haikal:** Like, I'd love to just, like, be on the call and learn.

**George Haikal:** And kind of how you're doing it, like, and then ask you questions.

**George Haikal:** Like, I think we could turn it into a resource for the whole team.

**Nicolas Castellanos:** About that, where do I can get, like, context for it?

**Nicolas Castellanos:** I know we have, like, the artifacts, but then, like, context for, I don't know, the input it needs and everything.

**Nicolas Castellanos:** It's that, like, on our table, or is there somewhere else?

**George Haikal:** What do you mean?

**George Haikal:** Like, what do you need for context?

**Nicolas Castellanos:** Like, I'm guessing we, for the content, we need to tailor the content we want based on the search and keywords and everything.

**George Haikal:** Yeah.

**George Haikal:** What time is it by?

**Nicolas Castellanos:** Do you have time today?

**Nicolas Castellanos:** do you want to, like, just send it to a week?

**Nicolas Castellanos:** Yeah, it's 3 p.m.

**Nicolas Castellanos:** here.

**Nicolas Castellanos:** Like, yeah, I have time.

**George Haikal:** Cool.

**George Haikal:** If I move this, do you want to do it from, like, how long do think it's, like, 30 minutes?

**George Haikal:** Yeah.

**George Haikal:** Cool.

**George Haikal:** You want to do 12 p.m.?

**George Haikal:** Okay.

**Nicolas Castellanos:** Okay.

**Nicolas Castellanos:** Okay, PSD.

**Nicolas Castellanos:** Yep.

**George Haikal:** Cool.

**George Haikal:** Cool.

**George Haikal:** We kind of just jump in and anything we don't get done there, can like split it up.

**George Haikal:** Cool.

**George Haikal:** Cool.

**George Haikal:** I feel pretty decent about the rest of the stuff, the stuff we got going, a lot of progress.

**George Haikal:** And they love it, by the way, like the feedback we're getting in the calls is amazing.

**George Haikal:** So they're super impressed.

**George Haikal:** And essentially, like, this is week six, we really started working week two, three, going to last two weeks.

**George Haikal:** So great stuff, guys.

**George Haikal:** Really appreciate it.

**George Haikal:** Awesome.

**George Haikal:** Cool.

**George Haikal:** And then, George, what time is best for you moving forward?

**Georgemaine Lourens:** Because I don't want to kill your Friday nights.

**Georgemaine Lourens:** No, it's fine.

**Georgemaine Lourens:** I think if you do – what time is it for you now?

**George Haikal:** I'm good.

**George Haikal:** I get up at 6.30, so I'm at the app at 6.30, so any time after that's fine.

**Georgemaine Lourens:** If you can do the time around the strategy sprint, that would be awesome.

**Georgemaine Lourens:** Otherwise, a Thursday, I'm available all day.

**George Haikal:** So Thursday is – That might be better.

**George Haikal:** So we're more likely to get responses for the things that are blocked, and we have a day.

**George Haikal:** So let's – I like that.

**Georgemaine Lourens:** You just tagged yourself, I think.

**George Haikal:** Nope.

**George Haikal:** Such a good name, I just, you know.

**Georgemaine Lourens:** Just,

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** You know, it's funny.

**Georgemaine Lourens:** My second name is Nico.

**Georgemaine Lourens:** Oh.

**Nicolas Castellanos:** So I'm on a call with two people in situation.

**George Haikal:** That's pretty crazy.

**George Haikal:** So random.

**George Haikal:** Are you cool?

**Georgemaine Lourens:** Same time Thursday, though?

**Georgemaine Lourens:** Yeah, that's fine.

**Georgemaine Lourens:** Maybe it's time to kick Marcel out.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** It sounds weird to say, seeing how he's already there, but.

**Georgemaine Lourens:** What is this?

**Georgemaine Lourens:** It's bizarre, huh?

**Georgemaine Lourens:** It's like calendars in the loop.

**George Haikal:** No, I mean, I catch up with them ad hoc in the office, so.

**Georgemaine Lourens:** Yeah, I thought so.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah.

**George Haikal:** Yeah.

**George Haikal:** Yeah.

**George Haikal:** You

**George Haikal:** Cool.

**George Haikal:** Cool.

**George Haikal:** Thanks, guys.

**George Haikal:** Great stuff.

**Georgemaine Lourens:** Great stuff.

**Georgemaine Lourens:** Awesome.

**Nicolas Castellanos:** All right.

**Nicolas Castellanos:** Thank you, guys.

**Nicolas Castellanos:** Have a great weekend and talk to you guys soon.

**George Haikal:** Likewise.

**Nicolas Castellanos:** Talk soon, Nico.

**Nicolas Castellanos:** Bye.

**Nicolas Castellanos:** Yep.

**Nicolas Castellanos:** Bye.

**Nicolas Castellanos:** Bye.
