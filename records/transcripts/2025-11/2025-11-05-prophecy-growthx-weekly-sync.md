# Prophecy <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-05
time: 18:00 UTC
duration: 33 minutes
organizer: kyle@growthxlabs.com
participants: Kyle Gaudreau, Ehtisham Hussain, Cody Carmen, Kyle Doherty, Wilton Kuffel, Raveena Kapatkar, Ashleigh Blalock, Roderick Bishop, Matt Turner, Saskia Wartnaby, Darrell Etherington
fathom_recording_id: 99447613
fathom_url: https://fathom.video/calls/463482582
share_url: https://fathom.video/share/gNQLwkdDszS3uiUyavq4KUQaZ9tgt-hW
source: fathom
enriched_on: 2026-03-02 12:00 UTC
</metadata>

---

## Summary

Align on content strategy, publishing workflow, and technical issues.

---

## Context

GrowthX is creating content marketing for Prophecy, an AI-powered data engineering and analytics platform. This was a weekly operational sync between Kyle Gaudreau and Ehtisham Hussain (GrowthX) and Cody Carmen (Prophecy's product leadership). The goal is to align on content strategy, publishing workflow, and technical execution to scale from one published article to a pipeline of five articles. Prophecy recently migrated to a new domain and Webflow instance, creating logistical challenges around staging, review workflows, and site structure clarity that the team is working through.

---

## Relevance

**To GrowthX Delivery:**
- Content strategy pivot confirmed: focus on later-stage, ad-hoc data cleaning where analysts get stuck, positioning Prophecy's agentic capabilities as the solve. This frames the narrative differently than earlier-stage ETL work.
- Publishing workflow is now under `/guides` (not `/blog`), with staging and review handled by Cody and Will. GrowthX needs fast-tracked Webflow access to stage content directly.
- AI-generated images approved to avoid designer bottlenecks; GrowthX should integrate this into the content pipeline with templates based on Prophecy's brand assets (gems, agent icons, generate/refine/deploy elements).
- Feedback log process established: reusable feedback from Cody and Will will be documented to reduce iteration on future articles.

**To GrowthX Business Development:**
- Prophecy's competitive positioning is clear: direct competitors are Alteryx and Informatica; Tableau and Power BI are positioning partners (customers use them *with* Prophecy, not instead of it).
- Thought leadership opportunity: Kyle emphasized the value of seeding Prophecy's framing into LLMs through content, citing examples from Augment Code (their language now appears in LLM outputs). This is a long-term market-shaping strategy.

**To GrowthX Technical Execution:**
- Nine article topics pending Cody's approval; once approved, GrowthX can proceed with production.
- Prophecy has technical debt on their site (invalid pages in sitemap that don't 404, likely from post-migration sales requests). Cody will address internally. GrowthX should continue flagging structural or SEO issues found during content review.

---

## Overview

- **First Article Approved:** The first article is approved for publishing under `/guides`. Cody will fast-track GrowthX's Webflow access to enable direct staging.
- **Competitor Strategy Defined:** Direct competitors are Alteryx/Informatica. BI tools (Tableau/Power BI) are partners, not targets, as they are used *with* Prophecy.
- **Content Goal → Shape the Narrative:** The core strategy is to publish content that shapes how LLMs understand the market, seeding Prophecy's framing into search results.
- **Tech Debt:** Cody will address a critical issue of invalid pages in the sitemap that are not 404ing, which could harm SEO.

---

## Key Topics

### Content Strategy & Framing

  - **Data Cleaning vs. Transformation:**
      - **Framing:** Group "data cleaning" under the broader "data transformation" topic to avoid semantic debates with technical stakeholders (e.g., Raj).
      - **Prophecy's Angle:** Focus on later-stage, ad-hoc cleaning. This is where analysts get stuck and must send work back to engineering. Prophecy's agentic capabilities solve this by letting analysts self-serve.
  - **Competitor Landscape:**
      - **Direct Competitors:** Alteryx, Informatica.
      - **Partners (not competitors):** Tableau, Power BI. These are tools customers use *with* Prophecy.
      - **Strategic Content:** Cody proposed an article on market convergence, explaining how tools are expanding into each other's spaces.
          - **Rationale:** This positions Prophecy as a thought leader and helps users understand the complex ecosystem.

### Publishing Workflow & Logistics

  - **First Article Status:**
      - All feedback from Cody and Will is implemented.
      - GrowthX will maintain a running log of reusable feedback to improve future articles.
  - **Publishing Process:**
      - **Location:** Articles will be published under the `/guides` directory, not the blog.
      - **Access:** Cody will fast-track GrowthX's Webflow access to the new domain, as the team cannot stage content.
      - **Review:** Cody will streamline the final review process with Will and Raj.
  - **Image Generation:**
      - **Decision:** Use AI-generated images to avoid designer bottlenecks.
      - **Direction:** Align with Prophecy's brand (stylized "gems," simple agent icons).
      - **Assets:** Cody will provide Figma files with design elements for reference.

### Technical SEO & Site Health

  - **Sitemap Issue:**
      - **Problem:** The XML sitemap contains invalid pages that do not 404.
      - **Impact:** These pages display a generic template (same image, old H1) and could negatively affect SEO.
      - **Context:** Likely a result of the recent site migration, possibly from sales requests to restore pages.
  - **Site Structure:**
      - Cody noted general confusion around the new site structure, with blog-style content appearing in the wrong sections.
      - GrowthX will continue to flag any technical or structural issues found.

---

## Action Items

**Cody Carmen (Prophecy)**
- Accept changes in first article; set Ready to publish
- Confirm with Will: AI images OK; staging access; review/publish workflow
- Send Figma files (gems, agents, generate/refine/deploy) to GrowthX
- Review/approve 9 topics in shared doc
- Share competitor/framing doc with GrowthX (direct competitors vs. BI tools vs. cloud platforms)

**Ehtisham Hussain (GrowthX)**
- Create ticket to integrate AI image generation into content pipeline
- Send sample AI-generated images to Cody for approval
- Forward sitemap/bad-page issue blurb to Cody for internal cleanup

---

## Transcript
**Ehtisham Hussain:** So the aimbit team, they kept on moving the meeting, and it's after this one.

**Kyle Gaudreau:** I saw that.

**Kyle Gaudreau:** All good.

**Ehtisham Hussain:** But that gave me some time to publish more stuff for them.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** So I'll start this off, but I'll hand it to you, and then we'll jump in.

**Cody Carmen:** Hey, guys.

**Ehtisham Hussain:** Hi, Cody.

**Kyle Gaudreau:** How you doing?

**Cody Carmen:** Doing pretty good.

**Cody Carmen:** How are you guys?

**Ehtisham Hussain:** Good.

**Kyle Gaudreau:** It'd be better if I wasn't sick for, like, literally, I feel like the fourth time over, like, the past four weeks.

**Cody Carmen:** That's brutal, man.

**Cody Carmen:** Yeah.

**Cody Carmen:** It's been a while, but I've been there, you know, in recent enough memory, and just the...

**Cody Carmen:** The never feeling like you're back fully on your game thing that just starts psychologically adding up on you too, that's a...

**Kyle Gaudreau:** I mean, that's just parenthood in general, you know?

**Kyle Gaudreau:** So, like, you kind of get used to operating at whatever level.

**Cody Carmen:** I'm definitely not 100% of what I was pre-parenthood, I'll say that.

**Cody Carmen:** How many kids do have?

**Kyle Gaudreau:** Just one, or...?

**Kyle Gaudreau:** Just one, yeah.

**Kyle Gaudreau:** And so he's a little under the weather, he's fine enough to be at school.

**Kyle Gaudreau:** My wife's sick, she got it way worse, and I was...

**Kyle Gaudreau:** You know, fine for a bit, and it just started hitting me last night, but I'll be fine.

**Kyle Gaudreau:** What I'm stressing about is, literally just heard this morning that I picked him up from school yesterday, he's playing with this kid he loves to play with there.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Middle time, and I just heard today that kid had...

**Kyle Gaudreau:** Woke up with, like, bad hand, foot, and mouth, and I'm like, no.

**Cody Carmen:** Cool.

**Kyle Gaudreau:** Yeah.

**Cody Carmen:** No, please.

**Cody Carmen:** Yeah.

**Cody Carmen:** Well, yeah, I...

**Cody Carmen:** My, you know, I've got...

**Cody Carmen:** I've got friends with, you know, toddlers.

**Cody Carmen:** There's...

**Cody Carmen:** All that.

**Cody Carmen:** And it's like you think you can handle whatever kind of sickness they're bringing in.

**Cody Carmen:** The hand, foot, mouth one seems like that nails everybody at least once and everyone's just bummed.

**Kyle Gaudreau:** Yeah, it does not seem fun.

**Cody Carmen:** And, you know, I mean, it's hard with kids that age.

**Kyle Gaudreau:** You know, they put everything in their mouth.

**Cody Carmen:** Right.

**Cody Carmen:** They want to put everything in their mouth.

**Cody Carmen:** And, like, you know, you don't want to, like, kill joy and curiosity by turning them into germaphobes.

**Cody Carmen:** Like, you kind of can't.

**Cody Carmen:** They're not young enough to, like, figure.

**Cody Carmen:** They're not old enough to figure out where the line is on that yet.

**Cody Carmen:** So, like, you kind of just, you know, bite down on the mouthpiece and deal with it.

**Kyle Gaudreau:** But.

**Kyle Gaudreau:** Somewhat related.

**Kyle Gaudreau:** I do feel like we can learn a thing or two from how kids approach life.

**Cody Carmen:** The one that's been top of mind for me recently is just how they interact, how excited they are to see each other.

**Cody Carmen:** I'm like, yeah, we as people need to act like this more often when we see people that we haven't seen.

**Cody Carmen:** And they're just, like, pumped and excited.

**Cody Carmen:** Exactly.

**Cody Carmen:** Exactly.

**Cody Carmen:** Yeah, man, kids are awesome.

**Kyle Gaudreau:** Yeah, nice.

**Cody Carmen:** Should we wait for Will?

**Cody Carmen:** Yeah, he'll be here any second.

**Cody Carmen:** His Wednesday calendar is approaching his Thursday in craziness.

**Kyle Gaudreau:** I guess me proposing moving to Thursday would not help them.

**Cody Carmen:** No, I would not.

**Cody Carmen:** It looks like Will did just say no on this one.

**Cody Carmen:** Something got added to it.

**Cody Carmen:** All right, so we can roll then.

**Kyle Gaudreau:** Yeah, it looks like, yeah.

**Cody Carmen:** Yeah.

**Cody Carmen:** In general, it looks like this time for him, there's usually going to be a conflict that he can't always get out of.

**Cody Carmen:** Yeah.

**Cody Carmen:** Yeah, his Thursday he's intentionally created is his, like, just all of my meetings day.

**Cody Carmen:** And it's, you know, he's been at the company long enough now that it's creeping into other days.

**Cody Carmen:** So, as we all, as we all understand.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I can go, for sure.

**Kyle Gaudreau:** Got to protect that calendar.

**Cody Carmen:** Yeah.

**Kyle Gaudreau:** After said and done.

**Kyle Gaudreau:** So main theme, I'll let Ehtisham cover most of this, but I think really the main theme I want to, like, center us on here and been talking about the same with Ehtisham is just, like, let's get to the momentum of publishing, let's get the first app live, let's ramp up to five eventually.

**Cody Carmen:** And so I just want to, like, think about this from the frame of reference of what then needs to happen for us there.

**Kyle Gaudreau:** And so that's largely what we want to talk about today.

**Kyle Gaudreau:** Of course, like, nailing the first article, key first piece, and so let's talk about that.

**Kyle Gaudreau:** But, yeah, that's the rough theme for today, and I would say, like, you know, the coming weeks.

**Kyle Gaudreau:** So we feel like we're getting to a good place where you're super confident in, like, what we're writing each week.

**Kyle Gaudreau:** It's feeling easier and easier, and we're just getting at that good case.

**Kyle Gaudreau:** You know, just want to continue to look at it from that framing.

**Cody Carmen:** Cool.

**Kyle Gaudreau:** Yeah, makes sense to me.

**Kyle Gaudreau:** Cool.

**Ehtisham Hussain:** Yeah, so we went through all of your comments and Will's comments as well, and we implemented all the changes.

**Ehtisham Hussain:** We are also going to maintain a running talk with all your feedback in it, so every time you comment over here that we believe will apply to future articles as well, we're going to record it and we're going to make sure that you don't have to give the same feedback for two different articles or three different Yeah, yeah.

**Ehtisham Hussain:** So this one, I think with all the changes and everything, this is ready to go.

**Ehtisham Hussain:** It was, like, we were kind of really confident when we sent this to you, and it was good to see that there was nothing major.

**Ehtisham Hussain:** Like, there were a couple of videos where we should have focused on AI, but other than that, I think we would go around this.

**Ehtisham Hussain:** So context, just real quick, Cody, like, what we're doing with this now is we have...

**Kyle Gaudreau:** We've developing these more agentic-based pipelines where they tend to run a bit slower because it just goes through so much sequentially.

**Kyle Gaudreau:** But we've been finding the quality of that is just night and day for a lot of developers, so we're starting to roll it out.

**Kyle Gaudreau:** But as we roll out that pipeline, this sort of feedback is very helpful for us to just continue to come back and refine it.

**Kyle Gaudreau:** So we don't expect it to be nailed out of the box.

**Kyle Gaudreau:** Right.

**Kyle Gaudreau:** So that's what we're doing a bit in the background.

**Kyle Gaudreau:** Yeah, yeah.

**Cody Carmen:** No, I mean, and honestly, like, I felt like pretty much everything I added was, like, context tweaks for sections, but the, like, substance was there.

**Cody Carmen:** And then I sent it to Will, and Will was like, I thought it was a really good first one.

**Cody Carmen:** I think your comments are all spot on.

**Cody Carmen:** Just run with that.

**Cody Carmen:** So, yeah, I mean, the process, I'm very happy with.

**Cody Carmen:** And, yeah, I mean, obviously, we'll still keep tweaking some stuff as we go.

**Cody Carmen:** And the early ones, there'll be more feedback, but I'm confident.

**Cody Carmen:** I'm confident that the team will handle that.

**Cody Carmen:** mean, historically, I've seen the ability and, you know, this first one was already very good.

**Kyle Gaudreau:** Awesome.

**Kyle Gaudreau:** Love to hear it.

**Kyle Gaudreau:** I had a particular question, if you could just jump back to the doc real quick.

**Kyle Gaudreau:** There was the thread about data cleaning, cleansing, and transformation.

**Kyle Gaudreau:** Can you just help me make sure I'm understanding this correctly?

**Kyle Gaudreau:** So from a very, like, I think I'm generally following it.

**Kyle Gaudreau:** You know, just a point of alignment that I want to think about probably where this goes in future articles is there's definitely, like, some pretty strong intent around you.

**Kyle Gaudreau:** So, like, where does that fall in?

**Cody Carmen:** Yeah.

**Cody Carmen:** So a couple of thoughts.

**Cody Carmen:** One, I know one of the times we had talked, I had asked Will, and that might have been one of the last calls.

**Cody Carmen:** It might have been a call with somebody else.

**Cody Carmen:** I don't even know.

**Cody Carmen:** But I was on a call with Will, I like, I flagged it real quick.

**Cody Carmen:** I'm like, Will, where's our line here?

**Cody Carmen:** Because we are, you know, thinking about at the highest level, we're trying to be analytics and data analysis pipelines, not the, you know, data engineering pipelines.

**Cody Carmen:** Data transformation happens in both of those.

**Cody Carmen:** In those data engineering pipelines, which is a lot more like classic ETL, that's where there's going to be a lot of those, like, we know every single time this transformation has to happen.

**Cody Carmen:** When we're combining these data sources, this is how we're going to write transforms that's going to get user ID in this to match with user ID in this one.

**Cody Carmen:** So in one chart, like, you know, they're all there.

**Cody Carmen:** So there's all of that data transformation stuff that, like, yeah, you could use prophecy to do, but that's not where we're emphasizing things.

**Cody Carmen:** So a lot of that stuff is where a lot of data cleaning does happen.

**Cody Carmen:** On the analytics pipeline side, there still is cleaning because in ad hoc querying of...

**Cody Carmen:** You're going to end up doing things in ways that, like, on one-offs, it's like, ah, I want to change this.

**Cody Carmen:** You are going to run into new, I guess, probably some, like, data quality issues, just on, like, new use cases, and they're going want to do some cleaning.

**Cody Carmen:** So because of that, there is the, like, standardized every single time data cleaning stuff that's probably being done by the engineers.

**Cody Carmen:** But for us, we are still very much thinking of data cleaning as something that prophecy users will be doing, not just getting done before prophecy's involved.

**Cody Carmen:** And then really, it's just, like, you know, data cleaning, data transformation, it's, like, squares and rectangles here, where it's, like, all data cleaning is data transformation, not all data transformation is data cleaning kind of things.

**Cody Carmen:** So, in general...

**Cody Carmen:** general...

**Cody Carmen:** Um...

**Cody Carmen:** Yeah.

**Cody Carmen:** Yeah, okay, so I did see that comment here.

**Cody Carmen:** Like, I would wrap, I would put it under data transformation when we talk about it in these guide length things, just because I don't want, that's one of those things that like, if a Raj type person sees it, he gets hung up on the like, well, it's technically part of this.

**Cody Carmen:** And it's like, yeah, it's like, technically, they are separate enough topics, but like, it's not wrong, but it's not 100% right.

**Cody Carmen:** So in general, when we're doing a list of things, I would fold it under the data transformation, and include it in there.

**Cody Carmen:** And then longer run, when we're talking topics, I'm still very interested in us having some things that are touching data cleaning or data cleansing keywords and queries.

**Kyle Gaudreau:** Because that's definitely there.

**Kyle Gaudreau:** You know, semantically cleansing, cleaning very close, although, you know, cleaning seems to be more...

**Cody Carmen:** We're used.

**Kyle Gaudreau:** But yeah, there's definitely, like, there's definitely search volume for us to capture there.

**Cody Carmen:** It's just a matter of, like, really making sure we're nailing the framing when we talk about it with what you're talking about.

**Cody Carmen:** And that's why I do think that, like, when we talk about it, one of the things for prophecy as thought leader here is, like, we can recognize that a lot of important cleaning, cleansing, whatever one we're talking about at the time, a lot of that work is happening early on in the process.

**Cody Carmen:** So, and that's great, as it should be happening then.

**Cody Carmen:** Like, that is the goal.

**Cody Carmen:** So I think we can, like, you know, when we get into these topics, we can talk about, like, hey, a lot of this is happening here.

**Cody Carmen:** Awesome.

**Cody Carmen:** What are the use cases?

**Cody Carmen:** What are the challenges of when it pops up later?

**Cody Carmen:** And I think that is also where we historically, data analysts who are not very SQL savvy, get caught up here.

**Cody Carmen:** They can't do a good job.

**Cody Carmen:** It's either very slow or not done right or it gets

**Kyle Gaudreau:** It's back to engineering for like late stage data cleaning.

**Cody Carmen:** So we want with prophecy because of all of our agentic capabilities where we can, you know, you can tell an agent, hey, I need, I need to do this.

**Cody Carmen:** Like, and it, and it will, and it knows SQL and it's going to go write it.

**Cody Carmen:** We are a good solution for that.

**Cody Carmen:** When we do talk about the later down the stage cleaning that tended to either be more work than people expected or fully like, you know, screech a process to a halt.

**Cody Carmen:** Yeah.

**Cody Carmen:** You know, so that's when I think about thought leadership on, on this, that's kind of where I think prophecy is coming in is, you know, what, let's, we, we are, we are talking mostly about later stage stuff with our tool, but setting the scene with the earlier stage is how we can also genuinely talk about problems that like analysts and analytics leaders are facing.

**Kyle Gaudreau:** Got it.

**Ehtisham Hussain:** Cool.

**Ehtisham Hussain:** All right, so that's going to have an impact on some of the future articles that we're planning.

**Ehtisham Hussain:** So the process, I assume, going to remain the same now once all the feedback has now been implemented.

**Ehtisham Hussain:** So if you move it to ready to publish, then we get on publishing, and that brings me to the next question.

**Ehtisham Hussain:** Should we follow the same old procedure of publishing, where we stage the article and we contact people from the team and everything?

**Cody Carmen:** So two things.

**Cody Carmen:** One, on the review process, at least for now, and I talked to Will in like 45 minutes, so I'll make sure on this.

**Cody Carmen:** I will go through and accept all these changes.

**Cody Carmen:** Obviously, there's any other feedback.

**Cody Carmen:** I'll do that.

**Cody Carmen:** But I'll get it to the point where I used to say good to go.

**Cody Carmen:** Right now, I think Will and maybe Raj are still going to want

**Cody Carmen:** So I will figure out how to streamline that process as much as possible.

**Cody Carmen:** On the staging it, these are going to get published under slash guides, not as blogs.

**Cody Carmen:** And also, because we're on the new domain, we also built this in a separate, I think, Webflow instance.

**Cody Carmen:** So I need to figure out how to get you guys access to the real website to stage these.

**Cody Carmen:** Because, right, that's a, that is an outstanding one.

**Cody Carmen:** Let me put, I'm making a note real quick.

**Cody Carmen:** Because I don't, I don't think I even have full access again right now.

**Cody Carmen:** They haven't done that yet.

**Cody Carmen:** So I need to fast track that.

**Cody Carmen:** So I'll talk, I'll talk about that with Will today and then I'll chase that down.

**Cody Carmen:** The goal is yes, for you guys to get in there and stage it in guides or where, you know, and however, however that's going to look.

**Cody Carmen:** And then we will hit publish on it, I believe.

**Cody Carmen:** But I'll

**Cody Carmen:** I will, I'll chase that down.

**Cody Carmen:** We basically have, like, had to re-answer questions on how we're going to do things like this internally with all the team and technology changes.

**Cody Carmen:** But I'll have answers on that, like, today.

**Cody Carmen:** I'm out tomorrow and Friday, so I will also loop will in on that.

**Cody Carmen:** So if we are ready, that, you know, people are not dropping this until Monday.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** We also need to figure out the images side of things.

**Kyle Gaudreau:** And so it looked like what you guys had in the blog was probably, like, AI generated.

**Cody Carmen:** Yeah.

**Cody Carmen:** I don't have any concerns on AI generated images.

**Kyle Gaudreau:** I'll stay to Sean.

**Kyle Gaudreau:** Yeah.

**Cody Carmen:** Okay, cool.

**Cody Carmen:** I'll ask Will in, you know, the hour if we're still good with that.

**Cody Carmen:** So my thought process is that I don't want a gummy process where I'm asking a designer to one-off create images or start doing it.

**Cody Carmen:** I don't want to deal with it.

**Cody Carmen:** So particularly, I don't know, when I look at what you guys were doing, like Augment Codes website, I mean, it looks cool in general, but that guides page or whatever you guys are calling it there, when you scroll through that, that looks good.

**Cody Carmen:** Like, it doesn't, the AI-generated images are good enough now that as long, like, you guys are clearly good enough at the consistency where it doesn't look like a brand-new prompt with no training every time, and they're, like, ran to them.

**Cody Carmen:** It looks better than stock photos used to when we used that for our thing, so.

**Kyle Gaudreau:** Oh, 100%, man.

**Kyle Gaudreau:** Yeah, basically, we can work it into our workflows.

**Kyle Gaudreau:** Ehtisham, I don't think we have it built properly yet into the current pipeline we're using.

**Kyle Gaudreau:** We've run some of

**Kyle Gaudreau:** So that's just something we need to make sure there's a ticket for.

**Kyle Gaudreau:** And I want to get that going pretty quick because I just don't want to be blocked on something so basic like that.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** So should we send some sample images first and decide on some kind of a...

**Kyle Gaudreau:** Yeah, we can send a few options and if there's anything inspiration-wise that you guys like, you know, that's always helpful.

**Cody Carmen:** Yeah.

**Cody Carmen:** We tend to like doing things that are kind of...

**Cody Carmen:** Like if you look at a lot of our marketing material has used even like our...

**Cody Carmen:** Is it still there?

**Cody Carmen:** Just a second.

**Cody Carmen:** Like our...

**Cody Carmen:** Even the LinkedIn banners we put on our page and we give to our employees to put up.

**Cody Carmen:** Oh, I have an update in mind.

**Cody Carmen:** Jeez.

**Cody Carmen:** But, you know, it's like a lot of the stuff we end up doing is our like kind of stylized, like our little like gems that we call them.

**Cody Carmen:** Those...

**Cody Carmen:** Those little elements that are on our like visual pipelines.

**Cody Carmen:** And then if you look like on our like prophecy.ai, you can also, you can see those floating around places, but you can also see like, if you get down on like that, like early on in our homepage on the AI agent powered data life cycle, like we've got those little kind of stylized generate, refine, deploy.

**Cody Carmen:** Like we'd like those little simple images that, um, that kind of just show what we do.

**Kyle Gaudreau:** Um, cool.

**Cody Carmen:** And then I can even probably, I could probably get you guys some Figma files that have, I don't know if that's useful or not, but like, if you want actual design elements.

**Kyle Gaudreau:** Definitely is.

**Cody Carmen:** Okay.

**Cody Carmen:** Yeah.

**Cody Carmen:** Um, I'll, I'll make a note for myself to drop you guys some of those later today.

**Cody Carmen:** Um, yeah.

**Cody Carmen:** Uh, growth X team, take my files.

**Cody Carmen:** Um, because yeah, going from there.

**Cody Carmen:** Like that's in general, that's, that's good.

**Cody Carmen:** And yeah, we tend to, other than that, our visual brand is pretty, uh, you know, do it as we go right now.

**Kyle Gaudreau:** So, you know, no, it's all good.

**Kyle Gaudreau:** I mean, and like, we can always adapt this later on.

**Cody Carmen:** It's just one of those things that's just like, you know, spend all this time nibbling the content.

**Cody Carmen:** No crap.

**Cody Carmen:** We don't have the images.

**Cody Carmen:** Yeah.

**Cody Carmen:** We've got these little guys now who are like our agents, I guess.

**Cody Carmen:** Um, and these are also useful in place of, and I can get you a file for this.

**Cody Carmen:** I know I have one somewhere.

**Cody Carmen:** Um, but these are useful in place of also, I think like when we're talking about agentic features slash like sometimes you need a character that's human like in something that's, that's, uh, yeah, that's a good one.

**Cody Carmen:** We can do that kind of stuff too.

**Cody Carmen:** And then I don't think there's anything else.

**Cody Carmen:** Yeah.

**Cody Carmen:** mean, we're, we're pretty basic.

**Cody Carmen:** So yeah.

**Cody Carmen:** All I'll draw, I'll drop all those off.

**Kyle Gaudreau:** Um,

**Kyle Gaudreau:** We can work with that.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Let me get back to this.

**Kyle Gaudreau:** Ehtisham, are you still here?

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** Yeah, yeah.

**Kyle Gaudreau:** All right.

**Ehtisham Hussain:** So, next thing, we need to, like, I've placed a bunch of topics in here, nine of them.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** then we have pretty detailed descriptions.

**Ehtisham Hussain:** It says short description, but these are pretty detailed.

**Ehtisham Hussain:** These are all based on the keywords that you have to.

**Ehtisham Hussain:** Cool.

**Ehtisham Hussain:** You make on the site.

**Ehtisham Hussain:** So, if you can go through them and approve them or leave comments or anything, that would be really helpful for us.

**Cody Carmen:** Yeah.

**Ehtisham Hussain:** That will get done today.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** And then another thing, like, you left a comment in there for Tableau and I think Power BI, it said these are not our direct customers.

**Cody Carmen:** I meant to say direct competitors.

**Cody Carmen:** competitors.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Yeah, yeah, yeah.

**Ehtisham Hussain:** I miss both.

**Ehtisham Hussain:** So, like, can we get, like, a list?

**Ehtisham Hussain:** Of the competitors that you're going after, and how do you want us to address, because Power BI is going to come up, like, even in some of the topics where we discuss AI tools for business analytics.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Yeah, it's a matter of, like, there's, like, that they're not, like, necessarily always direct, and I think it's valid to be, like, because I guess we have, we have, we have competition over the LLM results and search results that are not your competitors, because it's a category creation problem that we're all fighting over.

**Kyle Gaudreau:** And then if you think about, like, Tableau, they have, I forget what it's called now, Tableau Prep or something like that.

**Kyle Gaudreau:** Okay, yeah.

**Kyle Gaudreau:** They have a data prep solution.

**Kyle Gaudreau:** I didn't have a chance to, like, dig in super deep to it, but, like, just, like, from that, it's, like, of like.

**Cody Carmen:** That's good to know.

**Cody Carmen:** See, I, yeah, that one slipped by me.

**Cody Carmen:** So we'll leave, I can drop off, I will probably just, like, of consciousness into a Google Doc and share it with you guys.

**Cody Carmen:** But basically.

**Cody Carmen:** It's going to be the Alteryx-type tools are direct head-to-head, but then also the BI tools are kind of encroaching on our space a little bit.

**Cody Carmen:** Domo's been doing that for a very long time, where they've been trying to be everything.

**Cody Carmen:** So anyway, there is all of that going on.

**Cody Carmen:** So in theory, we are much more going up against an Alteryx or an Informatica than we are directly against a Tableau or a Power BI.

**Cody Carmen:** And we tend to see Tableau and Power BI as tools that our customers will still be using after Prophecy.

**Cody Carmen:** And we are going to have that little internal tension where we're not trying to directly steal deals from each other, but we're both going to be telling our customers to do some of that overlapping work in our tool, well, not another tool.

**Cody Carmen:** So, yeah, I will map out at least the basics of that.

**Cody Carmen:** And that will be hopefully helpful.

**Kyle Gaudreau:** Yeah, because, I mean, it just, stuff like this and listicles does seem to consistently work.

**Cody Carmen:** Yeah, and that's where I do think that, like, I am very open to some content that even talks about, like, let's write a piece at some point about the kind of, like, the expansion of all of these tools into each other's space, all trying to carve out, share in, like, the AI-powered world where everybody's better at doing stuff.

**Cody Carmen:** Like, all of these, every single tool on the market right now can do a hell of a lot more than it could two years ago.

**Cody Carmen:** And two years ago, we were already starting to see, like, Domo and some of these tools that used to be on the BI side kind of getting into the prep side of things.

**Kyle Gaudreau:** So, I think...

**Kyle Gaudreau:** I really like that because it helps to just, like, hey, I am overwhelmed with, like, all the different options that are out there and how far, or how should I think about the coverage of how they can help me with these problems?

**Kyle Gaudreau:** And...

**Kyle Gaudreau:** And...

**Kyle Gaudreau:** Breaking it down from a, like, hey, you know, here's how to think about it.

**Cody Carmen:** Here's where you're going to get stuck if you use these tools.

**Cody Carmen:** And I think that right now the world is still centered around really a cloud data platform.

**Cody Carmen:** Like, you're still going to be based off of, at least for now, a Databricks, a Snowflake, a BigQuery, something like that.

**Cody Carmen:** And how do you make all the tools in that ecosystem work well together?

**Cody Carmen:** It's certainly cloud-based.

**Cody Carmen:** Like, Alterix just launched a cloud-based competitor, finally, to, like, what we've been doing and other people have been doing to encroach in their space.

**Cody Carmen:** And it's, you know, we still think they're not going to, they're not, like, best in class yet, but they're going to try to be.

**Cody Carmen:** But anyway, it's, like, it's going to be cloud-based.

**Cody Carmen:** And I think that there is a, like, you know, you used to be able to buy tools to do, you bought tools for a specific set of tasks, and then you bought, you know, and you checked that box.

**Cody Carmen:** Then you checked the new box, and now they're all, if you've got five boxes, you can check it probably with, like, three tools instead of five tools.

**Cody Carmen:** So, I do.

**Cody Carmen:** You think that when we start getting into buying guide type stuff or, you know, how should you be approaching unique data problems, whatever, I'm good with just openly talking about there's more overlap than there used to be.

**Cody Carmen:** Play the strengths don't, you know, and I think part of that is in the world of like with rapid feature expansion, people are still actually selling on a core set of features.

**Cody Carmen:** Like they're not selling all hundred features they have.

**Cody Carmen:** They've got their like 10 or 20 that are their bread and butter.

**Cody Carmen:** And I think that that is super relevant as well, that to play the strengths, because frankly, in the AI race, everybody's going to catch up on like laundry list of features.

**Cody Carmen:** So figure out what's really good at what you need.

**Kyle Gaudreau:** And then all the nice to haves are going to happen eventually anyway.

**Kyle Gaudreau:** I really feel like it is being underrated the ways you can kind of like seed.

**Kyle Gaudreau:** it.

**Kyle Gaudreau:** good.

**Kyle Gaudreau:** We're we're You're Those Thank

**Kyle Gaudreau:** The LLMs with that kind of perspective in a way that should be helpful for you all.

**Kyle Gaudreau:** And so you're also going to combat, these LLMs are naturally going to, in current state, going to be thinking about you in the old way.

**Kyle Gaudreau:** Right.

**Kyle Gaudreau:** And so, you know, this is one of many ways of thinking about, you know, shaping that in a different way.

**Kyle Gaudreau:** Like a very different example, we work with Team App Engine.

**Kyle Gaudreau:** They used to be called Hotel Engine.

**Kyle Gaudreau:** And, like, there's all this, like, just, you can see just the different framing and different name.

**Cody Carmen:** And even the LLMs think they're two different companies.

**Kyle Gaudreau:** like, it just, it can become a little bit sticky.

**Kyle Gaudreau:** And so, anyways, it just, it helps to show in some degrees.

**Kyle Gaudreau:** Or, like, take an augment code.

**Kyle Gaudreau:** Like, we've literally seen the phrases we've written be referenced in that way.

**Kyle Gaudreau:** Not as a quote, but just in the way these LLMs are speaking.

**Kyle Gaudreau:** And so, if we think about that from that framing, that.

**Kyle Gaudreau:** And then where you all want to go and how you see the market, like, how do we ensure your content is reflecting that?

**Cody Carmen:** And do we start to see that come into the LLMs in a meaningful That's super helpful.

**Cody Carmen:** I would also, when I'm thinking about, like, internal debate on, like, is this at our standard or not?

**Cody Carmen:** That's really helpful for me to share with, like, Will and Raj on the, like, you know, the growthx team is seeing, some of their customers, including, like, Augment Code, literally the way they're framing topics is popping up in the LLMs.

**Cody Carmen:** So that's part of why we need to be expansive and basically go plant our flag places because it's going to be a little bit of a race to do that.

**Cody Carmen:** But if we can get people thinking of, you know, it's everybody in marketing always wants people to think about it the way you think about it.

**Kyle Gaudreau:** If we can go make other sources think about it the way we think about it, that would be sweet.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So...

**Kyle Gaudreau:** 100%.

**Kyle Gaudreau:** So, you know, outside of just visibility, I think that's, like, some of the qualitative benefits we can kind of consider here that should have some halo effects from improving your visibility over time that kind of just shows in different ways.

**Kyle Gaudreau:** Real quick on this sitemap thing I added, I was taking with you your XML sitemap.

**Kyle Gaudreau:** Good that it's there and it says prophecy.ai and so, like, some of those initial checks are good.

**Kyle Gaudreau:** What I noticed, and this is a hard one to audit at scale, luckily there's not a max amount of URLs, but, like, you have these pages that don't 404, but if you could click that example, Ehtisham, the link at the bottom, like, this isn't really a valid page and they all look like this, the same image of these people.

**Kyle Gaudreau:** It has a H1 that actually is the old right H1, and so it's hard to, like, I mean, it's not a 404.

**Cody Carmen:** But it's clearly appropriate.

**Cody Carmen:** Right.

**Cody Carmen:** And it's interesting.

**Cody Carmen:** So we, since we migrated, we had sales start asking for some of these pages to come back that had been killed, basically.

**Cody Carmen:** Like, all the stuff that I thought was going to happen, happened.

**Cody Carmen:** Where, like, we killed a bunch of .

**Cody Carmen:** Some of it was intentional.

**Cody Carmen:** Some of it was unintentional.

**Cody Carmen:** And, like, it was not communicated.

**Cody Carmen:** So I wonder if some of these are pages that there have been requests to come back and the work's not done.

**Cody Carmen:** Like, I think we're going have that.

**Cody Carmen:** And we're going to have just, like, actual, I didn't mean to do this at all.

**Cody Carmen:** So I think that that, could you send me the, like, the literally just, I've got it in notion.

**Cody Carmen:** I'm going to copy paste that blurb into, like, a message with a bunch of people and be like, hey, growthx flagging this for us.

**Cody Carmen:** I don't know what the solution is.

**Cody Carmen:** I'm off for the next two days.

**Ehtisham Hussain:** Good luck.

**Cody Carmen:** But, you know.

**Kyle Gaudreau:** Yeah, yeah, yeah.

**Kyle Gaudreau:** Yeah, I mean, it's one of those things that it.

**Kyle Gaudreau:** It's worthwhile cleaning up.

**Kyle Gaudreau:** I wouldn't put it as like a P0, P1 necessarily, but it's tech that you want to address.

**Cody Carmen:** Yeah, I would like to before we start adding a ton of pages to this and don't have a way to get to work through it manually.

**Cody Carmen:** I'd like to clean this up.

**Cody Carmen:** So, yeah, I mean, like this is I don't even know what weird page style.

**Kyle Gaudreau:** I don't even know why it looks like that.

**Cody Carmen:** Like you can't play the video.

**Ehtisham Hussain:** It's very weird.

**Ehtisham Hussain:** Yeah, it's a very interesting thing.

**Ehtisham Hussain:** It's a screenshot.

**Kyle Gaudreau:** Of the video.

**Kyle Gaudreau:** Yeah, exactly.

**Kyle Gaudreau:** I was so confused when I saw this.

**Cody Carmen:** screenshot of the video with the cursor over there.

**Cody Carmen:** So they did the whole page screenshot and then clipped it.

**Cody Carmen:** I don't know how that even – I don't know what thought process went into that.

**Cody Carmen:** But so, okay.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** That's fun.

**Kyle Gaudreau:** It's weird one.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I didn't notice it.

**Kyle Gaudreau:** I didn't notice

**Kyle Gaudreau:** Any other major issues?

**Kyle Gaudreau:** mean, generally, you know, there was a site-wide redirect for the things that you did for blogs that I probably wouldn't have recommended, but at this point, I don't think it's big deal.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** You know, obviously, traffic is tanking now, but.

**Cody Carmen:** Right.

**Cody Carmen:** Yeah.

**Cody Carmen:** You know, which we knew it would.

**Cody Carmen:** It's also, like, we have stuff.

**Cody Carmen:** So Will and I explained to our guy that, sorry, I know we're over, but just a second.

**Cody Carmen:** Yeah.

**Cody Carmen:** So we explained to our guy that it's like, we're going to put a lot of stuff in guides that's kind of bloggy.

**Cody Carmen:** And then he put, like, a new resource, like, an old resources page just under blog now.

**Cody Carmen:** So he's like, in his head, I guess it'd be flipped it.

**Cody Carmen:** I don't know.

**Cody Carmen:** So I, we're going to have a, so in general, what I'm saying is, is we've got a lot of weird stuff going on with how we're using the site currently that we're going to to fix.

**Cody Carmen:** So please do keep flagging any weird things you see, because I don't know how much of it is a, like, in translation problem versus.

**Cody Carmen:** Like genuinely no one knows why this happened, but we're going to have, that's going to be a spectrum for us to address.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Yeah, yeah.

**Kyle Gaudreau:** No worries.

**Kyle Gaudreau:** Happy to help.

**Kyle Gaudreau:** I mean, I've seen small things, nothing that I've, it's kind of like, I, the beholder, you know.

**Kyle Gaudreau:** Right.

**Kyle Gaudreau:** But generally, like major issues, I haven't uncovered any, but we'll definitely find any if we do run into them.

**Kyle Gaudreau:** So, yeah.

**Kyle Gaudreau:** Well, enjoy your long weekend.

**Kyle Gaudreau:** I will similarly be having a long one, although mine is on the latter half.

**Cody Carmen:** It's Monday, Tuesday next week.

**Cody Carmen:** So.

**Cody Carmen:** Gotcha.

**Cody Carmen:** Gotcha.

**Kyle Gaudreau:** Cool.

**Cody Carmen:** Sweet.

**Ehtisham Hussain:** Awesome.

**Kyle Gaudreau:** Thanks, guys.

**Kyle Gaudreau:** Talk soon.

**Kyle Gaudreau:** All Take care.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Bye.

**Kyle Gaudreau:** Bye.
