# Logic <> Growth X - Weekly Sync

<metadata>
date: 2025-09-17
time: 17:31 UTC
duration: 37 minutes
organizer: team@growthxlabs.com
participants: Steve Krenzel, Azzam Aijazi, Erik O'Brien, Aida Knezevic
fathom_recording_id: 87959787
fathom_url: https://fathom.video/calls/412193515
share_url: https://fathom.video/share/Ykd6sdsDyFPxxcGnov-Cdc6tvX391wWY
source: fathom
enriched_on: 2026-03-03 14:30 UTC
speaker_note: Joe and Jess Garms were invited but did not speak during the recording.
</metadata>

---

## Summary

GrowthX presented Atlas, their AI-powered content generation platform, and walked Logic through the end-to-end workflow for creating workflow automation content targeting SEO and AI visibility. The teams aligned on a four-cluster content strategy focusing on general workflow automation, business user tools, industry-specific automation (fintech, e-commerce, logistics), and thought leadership. Logic needs to finalize CMS options and grant access to Google Search Console and GA4, while GrowthX will prepare a content calendar with 40-50 keyword assignments due the following week.

---

## Context

Logic is a workflow automation platform competing in the growing AI-powered automation market. They approached GrowthX for content marketing and AI visibility services to build topical authority and differentiate from competitors like Zapier. This was a working session to introduce GrowthX's Atlas platform, content generation workflow, and proposed content strategy. Aida Knezevic (Senior Managing Editor at GrowthX) led the technical walkthrough, with Erik O'Brien providing context on GrowthX's delivery approach, while Steve Krenzel and Azzam Aijazi (from Logic's team) asked implementation questions about CMS options, content review timelines, and publishing workflows.

The relationship is beginning; GrowthX is onboarding Logic as a client, and this meeting focused on getting alignment on strategy and tool setup before content production starts. Key decision point: Logic's website is currently programmatic/in-house, which complicates publishing, so the teams explored hybrid solutions (proxying through Webflow or manual markdown publishing) rather than a full CMS migration.

---

## Relevance

**To GrowthX Delivery:**
- Atlas platform is core to Logic's engagement; demonstrated working end-to-end on a keyword (research → outline → draft → fact-check).
- Two-round revision cycle is standard; Logic should expect to provide feedback in first month, declining thereafter.
- Publishing workflow challenge: Logic lacks a CMS (in-house programmatic site); GrowthX offered markdown/Google Docs alternatives and hybrid Webflow solutions. This may require custom integration work.
- Image generation pipeline needs Figma/Google Drive access for brand fonts and colors (action item: Steve Krenzel).

**To CheckThat:**
- Heavy focus on AI visibility alongside SEO. Logic is tracking via Scrunch tool (prompt-based LLM visibility monitoring) — 140-150 custom prompts will be set up to monitor how many LLM responses mention Logic vs. competitors.
- Looker dashboard setup (requires GA4 + Google Search Console) will track LLM referrer reports separately from traditional search traffic.
- Four-cluster strategy explicitly designed for both SEO ranking and LLM association (e.g., workflow automation content helps LLMs associate Logic with these topics).

**To GrowthX Business Development:**
- Logic is a solid mid-market fit: they have in-house dev capacity, founder network (Azzam and Steve are decision-makers), and willingness to invest in content. Expansion potential if initial content performs well.
- First content calendar (40-50 assignments) due next week; momentum indicates healthy project kickoff.
- LinkedIn promotion support is a future ask (Aida to follow up); this could open a new service line if viable.

---

## Overview

- GrowthX presented their AI-powered content generation platform (Atlas) and workflow
- Content strategy focuses on workflow automation, targeting both SEO and AI visibility
- Next steps: Logic to review content strategy, GrowthX to prepare content calendar and keyword research
- Logistics around CMS, publishing, and performance tracking were discussed

---

## Key Topics

### Content Generation Process

  - Atlas platform used for AI-assisted content creation
  - Workflow: Assignment generation → Article generation (including research, outlining, drafting)
  - Two rounds of revisions typically needed, aiming for minimal edits over time
  - GrowthX handles publishing; CMS access needed (alternatives discussed for Logic's setup)

### Content Strategy

  - Primary focus: Workflow automation keywords
  - Four topic clusters identified:
    1.  Workflow and process automation (top/middle funnel)
    2.  Automation for business users (bottom funnel, product-focused)
    3.  Industry-specific automation (e.g., fintech, e-commerce, logistics)
    4.  AI and automation trends (thought leadership)
  - Strategy aims to build topical authority and differentiate Logic from competitors

### Performance Tracking and Visibility

  - SEMrush used for keyword tracking and growth reports
  - Looker dashboard to be set up (requires Google Search Console and GA4 access)
  - Scrunch tool introduced for tracking AI visibility across LLMs

### Visual Content and Promotion

  - GrowthX can generate featured/hero images for blog posts
  - LinkedIn promotion of content to be explored further

---

## Action Items

**Steve Krenzel (Logic)**
- Investigate CMS options; consider hybrid solution w/ Webflow for blog content
- Set up basic blog infra — index page, post template w/ author & breadcrumbs
- Share Figma/Google Drive w/ brand fonts & colors for image generation
- Grant GrowthX access to Google Search Console & GA4 for Looker dashboard
- Review content strategy doc in Notion; comment on additional angles/topics

**Azzam Aijazi (Logic)**
- Review content strategy doc in Notion; comment on additional angles/topics

**Aida Knezevic (GrowthX)**
- Prepare content calendar in Airtable with 40-50 keyword assignments (due next week)
- Follow up on LinkedIn social post support capability with GrowthX team
- Check with GrowthX team on hybrid blog setup and CMS alternatives for Logic

---

## Transcript
**Azzam Aijazi:** I think it's the first time I've seen you with no hat, Steve.

**Steve Krenzel:** This meeting is being recorded.

**Azzam Aijazi:** I think that there was a top of your head.

**Azzam Aijazi:** It's glorious.

**Steve Krenzel:** It's very efficient.

**Azzam Aijazi:** The shaving thing?

**Steve Krenzel:** Yeah, I'm not going to lie, I've considered it a couple of times, just like sheer convenience.

**Erik O'Brien:** Hey, guys.

**Steve Krenzel:** Hey, Eric, how's it going?

**Erik O'Brien:** Too bad.

**Erik O'Brien:** Apologies for being a couple minutes late.

**Erik O'Brien:** We've just got another meeting wrapped.

**Erik O'Brien:** No worries.

**Erik O'Brien:** Ada should be joining as well.

**Erik O'Brien:** She is our managing editor, so she'll be working really closely with me, so I'll let her introduce herself, though.

**Aida Knezevic:** Hi!

**Aida Knezevic:** Sorry I'm late.

**Aida Knezevic:** We were back to back.

**Steve Krenzel:** No worries.

**Aida Knezevic:** Yeah, it's great to meet you.

**Aida Knezevic:** I was out of office last week, but my name's Aida.

**Aida Knezevic:** Like I said, on Slack, I'm a Senior Managing Editor at GrowthX.

**Aida Knezevic:** So I work with Erik and the rest of the team to set you up with a content strategy.

**Aida Knezevic:** I also set you up in Atlas.

**Aida Knezevic:** And then once we start creating content, it's my job also to make sure that it's following content quality guidelines and it's something that you'd be excited to publish on your website.

**Aida Knezevic:** I joined GrowthX in December, which back then we were only 15 people, I think, or 18.

**Aida Knezevic:** So it's been a while here.

**Aida Knezevic:** But before this, I was working at another content marketing agency called Animals.

**Aida Knezevic:** So I've been in content for five or six years.

**Aida Knezevic:** I worked with a lot of different B2B SaaS companies all across different verticals.

**Aida Knezevic:** And I'm also a freelance writer.

**Aida Knezevic:** I write for Semrush, you've probably read some of my blog posts, and I still love freelance writing because I have to keep that muscle alive.

**Aida Knezevic:** I refuse to use ChatGPT when I'm actually writing my freelance content because I do not want that muscle to deteriorate.

**Azzam Aijazi:** Nice.

**Azzam Aijazi:** That's awesome.

**Azzam Aijazi:** I'm glad to have you here in our corner, Aida.

**Aida Knezevic:** Nice to meet you.

**Aida Knezevic:** Yeah, it's great to meet you as well.

**Aida Knezevic:** All right, so let me just pull up everything that I want to show you today.

**Aida Knezevic:** So, I know you took a look at the artifacts, and I wanted to get just, like, your high-level thoughts on, you know, what they look like, and if there's anything else that you want to add.

**Azzam Aijazi:** No, I think I dropped in the Slack.

**Azzam Aijazi:** I was quite impressed by what you all put in here.

**Azzam Aijazi:** I thought it was pretty on point.

**Azzam Aijazi:** I dropped in a couple comments, but it's, you know, partially my job is to drop in comments, so I do that.

**Azzam Aijazi:** Regardless, but I thought that you had taken a couple of ideas that we'd already had internally and taken them way, way past and extended them and did a really good job of elaborating and articulating some important points.

**Aida Knezevic:** thank you.

**Aida Knezevic:** All right.

**Aida Knezevic:** Nice.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Love to hear that.

**Aida Knezevic:** All right.

**Aida Knezevic:** So I'm going to go ahead and share my screen.

**Aida Knezevic:** So this is sort of an overview of the agenda that I wanted to talk through today.

**Aida Knezevic:** So the artifacts that you read through, so we create them using publicly available information about your company.

**Aida Knezevic:** And we also take the transcript from our meetings and we feed all of that to create them and make sure that they're as tailored and unique as possible because they're really important for the content generation process.

**Aida Knezevic:** So I wanted to show you where they actually live and how they impact, um,

**Aida Knezevic:** The article generation process end-to-end, so this is Atlas, which is our content generation platform, and right now we are in the context artifacts, and no, actually, we're not, we're in the assignment generation pipelines.

**Aida Knezevic:** These are the context artifacts, so the three standard ones that everybody starts with are the audience personas, the company context, and the writing guidelines, and we can add additional artifacts depending on need, so let's say you, you we generate a calibration blog for you, and it turns out that the content kind of talks about a very, something very nuanced in a way that you really don't want it to talk about that, so we can create an additional artifact that, you know, reads an article, draft, draft, and then goes back and fixes those errors.

**Aida Knezevic:** Or, you know, in very highly regulated industries, for example, we have some clients that are in healthcare, and we really need to make sure that there are some things that their content never mentions.

**Aida Knezevic:** For example, there might not be allowed to refer to patients as consumers or customers.

**Aida Knezevic:** So we might build a custom artifact that just contains instructions to read through the blog and replace all mentions of customers with patients and things like that.

**Aida Knezevic:** So this is, you know, just the starting kit, but we can expand it as need arises.

**Aida Knezevic:** And then I wanted to show you the article generation workflow.

**Aida Knezevic:** So the usual, the two pipelines that we use, the starting ones are the assignment generation and the article generation.

**Aida Knezevic:** Assignment generation is very simple, and it just allows us to upload a list of keywords or topics.

**Aida Knezevic:** And then the tool.

**Aida Knezevic:** We'll do an SEO analysis using SEMrush, and then it will generate assignment titles, briefs, which makes our jobs a whole lot easier because we don't have to do this manually.

**Aida Knezevic:** And then the article generation one is much more complex.

**Aida Knezevic:** So I already ran a keyword through this process today just so I can show you what it looks like.

**Aida Knezevic:** But keep in mind, I didn't do any sort of manual editing, so the content isn't going to be as polished as it usually is.

**Aida Knezevic:** So we start with a keyword or a title, and we usually give it an assignment direction.

**Aida Knezevic:** This can be as basic as write a listicle, write a how-to guide, write, I don't know, a 10-step checklist, whatever it is.

**Aida Knezevic:** And this can be very, very detailed.

**Aida Knezevic:** We could include what to add.

**Aida Knezevic:** But not to add, like, we can really shape the complete angle here.

**Aida Knezevic:** Once this is ready, we proceed with the assignment brief.

**Aida Knezevic:** At this stage, Atlas is going to use SEMrush to analyze the top-ranking content for that topic or the target keyword.

**Aida Knezevic:** And it returns a brief that outlines who the target audience is, what is the SEO metadata, and it also analyzes the keyword, and it finds other related keyword opportunities, which helps us rank for more keywords.

**Aida Knezevic:** At this stage, the company context and the audience personas come into play.

**Aida Knezevic:** But the writing guidelines aren't applied until the article draft stage.

**Aida Knezevic:** And then it kind of generates a proposed content structure.

**Aida Knezevic:** We edit it pretty heavily.

**Aida Knezevic:** And then when we're happy with, like, just the bare-bone content structure, we run the research step.

**Aida Knezevic:** This research step, it uses, I believe...

**Aida Knezevic:** Perplexity to research the topic in great detail.

**Aida Knezevic:** So it uses the assignment brief and then it asks questions that it needs to get the answers to to actually write an article about this.

**Aida Knezevic:** I think if you've ever tried to write an article using ChatGPT or Claude and you didn't provide it any sort of research, the content can be pretty thin.

**Aida Knezevic:** You know, the sections are all very, very short.

**Aida Knezevic:** So that's what we're trying to avoid here.

**Aida Knezevic:** And then when the research step is done, we run the outline generator.

**Aida Knezevic:** And this is when it will, you know, provide a word count for each section.

**Aida Knezevic:** And it contains bullet points of all of the key points that it's going to include.

**Aida Knezevic:** We heavily edit this.

**Aida Knezevic:** I don't think we've ever, we never really generate content without editing the outline.

**Aida Knezevic:** We make sure, you know, if we have, for example.

**Aida Knezevic:** Sometimes we might notice that a specific section could use a product mention, so we might, you know, say, like, mention logic here in this way.

**Aida Knezevic:** And then when we're happy with the outline, we just generate the draft, and then we run the fact checker, the internal links, and then we will do another round of editing.

**Aida Knezevic:** If we do the outline right, the last round of editing is usually a lot faster, but that's kind of our process end-to-end, and then we will take this document, paste it in a Google Docs, send it over to you, and then you review it.

**Aida Knezevic:** So Atlas right now is an internal tool, so only we're using it, but we take all of your feedback, especially in the beginning, and we tailor the artifacts accordingly.

**Aida Knezevic:** So, yeah, that's Atlas.

**Aida Knezevic:** Do you have any questions?

**Steve Krenzel:** This is pretty awesome.

**Steve Krenzel:** Thank you. I love seeing the flow, so since this is an internal tool, are you also enumerating the topics, or are we involved at the start and at the end, or are you just kind of enumerating content and sending us docs that we review?

**Azzam Aijazi:** That was going to be my question, is like, who decides what goes into this machine?

**Aida Knezevic:** Great question.

**Aida Knezevic:** That's actually something that we're also going to discuss today, which is your content strategy.

**Aida Knezevic:** So we, our process is to create a content strategy, present it to you, get your thoughts, approval, and then we do a pretty detailed keyword research.

**Aida Knezevic:** We generate the assignments, meaning just the titles and the sort of the briefs, and we upload them to a content calendar in Airtable.

**Aida Knezevic:** And after that, um, you will take a look at those assignments, decide which ones you want to do, which ones you don't want to do, um, and then we will generate them.

**Steve Krenzel:** It's a collaborative effort.

**Steve Krenzel:** Cool.

**Steve Krenzel:** And how far up is the content calendar?

**Aida Knezevic:** It's due next week.

**Steve Krenzel:** Oh, sorry.

**Steve Krenzel:** mean, like, generally, how far up do we, like, do we enumerate, like, a month's worth of content?

**Aida Knezevic:** Yeah, that's a, so we typically like to present the first round of keyword research.

**Aida Knezevic:** So we try to present around 40 to 50 ideas, which could last about a month, month and a half, depending on how fast we publish.

**Aida Knezevic:** In the past, we've done a lot of keyword research in the beginning.

**Aida Knezevic:** And I think once someone, like, having 100 assignments to review at once, it can be pretty, it can be a lot.

**Aida Knezevic:** So it's better, I think, to do it in chunks.

**Steve Krenzel:** What's a typical flow — how many iterations does a final draft typically go through? Are you generating a bunch of articles and we pick which ones to publish, or do all pieces go through multiple revision rounds?

**Aida Knezevic:** So we do two rounds of revisions on every blog post.

**Aida Knezevic:** It might not need two.

**Aida Knezevic:** It might need just one, or it might not need any at all.

**Aida Knezevic:** I think in the beginning, I think probably the first month of us creating content for you, you will usually have some feedback.

**Aida Knezevic:** Um, but it, this also depends on the topic, on the industry.

**Aida Knezevic:** It varies.

**Aida Knezevic:** Um, but it usually, most content goes through one round of feedback in the beginning, like, the first month.

**Aida Knezevic:** And then it goes down.

**Aida Knezevic:** Um, and.

**Aida Knezevic:** And the idea is to get to a point where you can just get a piece of content, you read through it, and you're like, okay, this is good to go.

**Steve Krenzel:** Great, thanks.

**Steve Krenzel:** Yeah, and that's what I'm trying to get a sense of, like, what's the time commitment?

**Steve Krenzel:** Like, if we're doing, you know, five pieces a week or something, what's the time commitment we should be thinking about on our side?

**Aida Knezevic:** Yeah, I think it depends on how much time you have.

**Aida Knezevic:** And, like, I would say, I don't, I mean, it really depends, like, because it takes me, it could, it could, when I'm editing, it could take me 30 minutes, could take me two hours, depending on how deep I want to get into it.

**Aida Knezevic:** So, I would say you can maybe 15 to 30 minutes to review a piece of content.

**Steve Krenzel:** Yeah.

**Steve Krenzel:** Great, thank you.

**Steve Krenzel:** And one of the things that y'all had access for was CMS.

**Steve Krenzel:** Does that suggest that you actually publish the content as well?

**Steve Krenzel:** Or when you give us the Google Doc, do we then put it into some system?

**Aida Knezevic:** We handle the publishing. We usually get access to a client's CMS with an email address you provide, then we log in, stage the content, and publish it. Some clients prefer to review staged content before we push it live, but we take care of the publishing.

**Steve Krenzel:** Okay, thanks.

**Steve Krenzel:** We currently don't have a CMS right now, but we're looking into what our options there are.

**Azzam Aijazi:** Okay, all right.

**Azzam Aijazi:** Do you have recommendations for, like, blog platforms or CMSs that you found clients are able to get up with and go in with pretty quickly that do a good job?

**Aida Knezevic:** So I think Erik recommended Webflow.

**Aida Knezevic:** Webflow is a good one, and I think it's easy to set up.

**Aida Knezevic:** I don't know, Erik, do you have any other recommendations?

**Azzam Aijazi:** My understanding of Webflow is that it's a whole website builder, which may not be needed just to host long-form written content. Why Webflow versus something that's just a blog platform?

**Aida Knezevic:** Yeah, because we, so we want your website to gain authority.

**Aida Knezevic:** And we, in order for your domain to gain authority, the content has to be published on your domain.

**Aida Knezevic:** So to get like rankings and, you know, in Google and other search engines, but also to gain visibility in AI search.

**Aida Knezevic:** How is your website hosted right now?

**Steve Krenzel:** It's programmatic — an in-house thing we deploy.

**Steve Krenzel:** And so that's kind of the tricky bit.

**Steve Krenzel:** Like migrating over to Webflow, we spent a little bit of time on it last week.

**Steve Krenzel:** It's a little bit of a lift.

**Steve Krenzel:** It's not impossible, but we might be able to come up with some hybrid where like logic.ink slash content or blog or something kind of proxies through to Webflow, or there might be something we can do there.

**Aida Knezevic:** Okay, yeah, yeah.

**Aida Knezevic:** Let me talk about this to our team because we can, in some instances, help you set up a blog on your website.

**Aida Knezevic:** And the fact that you don't have a CMS, I'm not sure how big of an issue that is.

**Aida Knezevic:** I think sometimes a CMS is a bigger blocker than not having one.

**Aida Knezevic:** But let me, let me check and get back to you.

**Aida Knezevic:** Because I do know like migrating to a CMS, it's a process.

**Aida Knezevic:** Like it's not something that you can get hooked up in like a week.

**Steve Krenzel:** So yeah.

**Steve Krenzel:** If we did, you know, in the short term, if we did just want to take those Google Docs and kind of publish them ourselves.

**Steve Krenzel:** Because we could wire up something hacky through our existing system if we needed to.

**Aida Knezevic:** Would that be an acceptable flow?

**Aida Knezevic:** Yeah, mean, we have a couple of clients who don't have a CMS and they publish just using like markdown files or whatever we provide.

**Aida Knezevic:** So we can do that.

**Aida Knezevic:** The one thing, the most important thing is you need a blog like index page on your website so that someone can click and like see all of the blogs.

**Aida Knezevic:** Um, that's important for just crawl, like for Google crawlers.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** and then the template for the blog posts, it should include an author, um, and it should include breadcrumbs.

**Aida Knezevic:** Um, but other than that, I think we don't really need anything more fancy.

**Steve Krenzel:** Cool.

**Steve Krenzel:** And you mentioned, uh, markdown.

**Steve Krenzel:** Um, are there ever any visual artifacts generated as part of this process?

**Steve Krenzel:** Are there diagrams or complementary images, or is it always prose?

**Aida Knezevic:** So we actually generate featured or hero images for blog posts.

**Aida Knezevic:** Right now, we don't have the ability to generate inline images, although that is something that we want to work on.

**Aida Knezevic:** But we do generate these images.

**Aida Knezevic:** We have in-house designers who integrate image generation into the article pipeline. There will be a step at the end that says image generation.

**Aida Knezevic:** And we run it, and it generates a couple of options.

**Aida Knezevic:** And we can tailor it to your visual identity, like any fonts that you're using.

**Aida Knezevic:** Typically, we just need access to like a Figma file or just a Google Drive with all of your fonts and colors so that the designer knows what to use.

**Aida Knezevic:** And then we will typically, I mean, I can do graphs.

**Aida Knezevic:** We could do, what we end up doing a lot of times is just doing like an image that includes the title of the blog and then there are graphics behind it.

**Aida Knezevic:** I think that can also be done depending on what you end up liking in the end.

**Steve Krenzel:** Okay, thank you.

**Aida Knezevic:** All right, great.

**Azzam Aijazi:** Sorry, just one more related question here is, I don't know if this is covered in the scope of like our arrangement at all, but would like LinkedIn promotion of the written content be something that we can look to y'all for help with or is that something that we would own on our end?

**Azzam Aijazi:** And if you have any advice on how to manage that as well, that'd be helpful.

**Aida Knezevic:** Yeah, I think with LinkedIn, we've done it in the past, I'll have to check with the team and see how we can support that, if we can support that.

**Aida Knezevic:** The thing with LinkedIn and social media, like would this be published on your company page or from a person?

**Azzam Aijazi:** Okay.

**Azzam Aijazi:** Thank

**Azzam Aijazi:** I was thinking from our company page, like in the past I've had success with like kind of amplifying new blog content on social, if there's no other content happening on social, A, just to kind of create like a constant drumbeat of content on socials, but then B, to find new audiences, you know, new, you know, offer some perspectives, some summary, whatever the case might be, and just find ways of repurposing that content to reach a broader audience.

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Yeah, yeah, I get what you mean.

**Aida Knezevic:** All right, yeah, I can talk to, I can talk to the team and see, see what we can do.

**Aida Knezevic:** That would require us like hooking up a different pipeline in addition to article generation that would just generate like LinkedIn social posts from a blog post.

**Aida Knezevic:** But yeah, I'll let you know.

**Azzam Aijazi:** Yeah, let us know.

**Azzam Aijazi:** Thank you, Paul.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right, perfect.

**Aida Knezevic:** So yeah, so in addition to the artifacts, Atlas, we also worked on your content strategy.

**Aida Knezevic:** And it lives in this document in Notion.

**Aida Knezevic:** I'm going to send you a link after our call.

**Aida Knezevic:** But at this stage, what we do is we analyze your biggest pain points as a business and what you're trying to do, your goals, and then try to identify what are the best topic clusters that we want to target that would give you the best results.

**Aida Knezevic:** And we compiled all of this into this document.

**Aida Knezevic:** So you can find the primary business objective at the top.

**Aida Knezevic:** So we want to create content that's going to rank for top of the funnel, but also very high-intent bottom of the funnel queries to support LLM discovery, to support traditional SEO, and eventually just getting conversions, obviously.

**Aida Knezevic:** Right now, you know, your current challenges is that you are

**Aida Knezevic:** Founder Network dependent, and you have competitors that are highly present in search results, and they have very developed SEO strategies, which is not that big of an issue if you know what kind of keywords you want to target.

**Aida Knezevic:** And, you know, you have a really great competitive advantage, and it allows us to create content that is really, like, we can really differentiate you very well, because this is very, I mean, the value prop is insane, so it's not going to be easy, not going to be hard to highlight those benefits in content.

**Aida Knezevic:** So, the goals that we have, they center around dominating workflow automation keywords.

**Aida Knezevic:** I know in the kickoff call, you were also talking about process automation, but just looking at sort of the search landscape, workflow automation is...

**Aida Knezevic:** Is probably keywords that are most aligned with what you do.

**Aida Knezevic:** We were also looking at document automation, but document automation, what actually shows up in search results is something that's quite different from what you do.

**Aida Knezevic:** So we landed on workflow automation as kind of a, that's most aligned with what you do.

**Azzam Aijazi:** I'm curious, were you able to see anything around like terms like AI automation in terms of that feature of the word or the term AI?

**Azzam Aijazi:** I'm curious if there's like a different market for that, if it's just kind of assumed that workflow automation is powered by AI nowadays or what?

**Aida Knezevic:** Yeah, I think that's, let's, let's actually take a look.

**Aida Knezevic:** I think when I was looking at, for example, if we're looking at workflow automation.

**Aida Knezevic:** It's usually, yeah, that's, here it is, AI workflow automation.

**Azzam Aijazi:** AI is the number one keyword on the column on the left.

**Aida Knezevic:** Yeah.

**Azzam Aijazi:** Yeah.

**Aida Knezevic:** So it's very much associated with the workflow automation that was present before AI.

**Azzam Aijazi:** Yeah.

**Aida Knezevic:** And there's, your competitors are right here.

**Azzam Aijazi:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** But yeah, so it's more of a long tail version of workflow automation.

**Azzam Aijazi:** Okay.

**Azzam Aijazi:** Makes sense.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Steve Krenzel:** Yeah.

**Steve Krenzel:** And we also.

**Steve Krenzel:** Random question around SEMrush.

**Steve Krenzel:** That's a, that's a tool that y'all have put up a few times on, on calls.

**Steve Krenzel:** I'm curious, it's got like this, it's like a treasure trove of data.

**Steve Krenzel:** How does, how does this data get surfaced to us?

**Steve Krenzel:** Or like in terms of like, as our, as our keyword rankings and things change, like how do you, is this kind of a snapshot that you, you'll occasionally share with us?

**Steve Krenzel:** Or do we in any way get like regular kind of updates on, on kind of the data present in SEMrush?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** We can set up a position tracking report in SEMrush. Once we do keyword research, we'll upload target keywords and track your rankings. We can also generate growth reports showing keyword rankings over time, which we can share as PDFs.

**Aida Knezevic:** For performance monitoring, we use Looker, which requires access to your Google Search Console and GA4. We'll generate a dashboard with different metrics about your website, including an LLM referrer report showing pages getting traffic from LLMs, plus general search traffic from Google and other search engines. We also use Scrunch, an AI visibility tool, and we'll set up a dashboard there too. You'll have access using your email and can view data week over week. Do you know how Scrunch works?

**Steve Krenzel:** No, I've used Looker a whole bunch, but never Scrunch.

**Aida Knezevic:** Scrunch is kind of reverse engineering what your audience is looking up in AI tools. We upload a list of prompts — usually 140-150 to start — guessing what your audience might ask ChatGPT, Perplexity, or similar tools.

**Aida Knezevic:** And then Scrunch throughout the day, it will ping different LLMs with these prompts, and then it collects the responses, analyzes them, and then it sees, okay, like how many responses include your company or your competitors.

**Aida Knezevic:** Scrunch then pings different LLMs throughout the day with these prompts, collects responses, and analyzes how many mention your company versus competitors. We're setting it up this week to show you next week. It's an AI visibility workaround since OpenAI and Anthropic don't share user data.

**Azzam Aijazi:** This sounds really clever, actually.

**Aida Knezevic:** And if you come up with any prompts that you think are good to track, we can add them for you. Beyond workflow automation keywords, we also want to do industry-specific process automation searches. Let's go over the topic clusters — that's probably the most important part of the strategy.

**Aida Knezevic:** So we've identified four different clusters for you that we want to target, and these all, they have different priorities, and they also, like, target different keyword volumes.

**Aida Knezevic:** So the first one is obviously workflow and process automation, and this is really just targeting that more top of the funnel, middle of the funnel content, which is more, you know, related to, like, what is workflow automation software, how do I create an automated workflow, how to automate HR workflows, and we really want to target these common pain points that people, that your audience experiences in their day-to-day life.

**Aida Knezevic:** It's important to note that this cluster is very, like, the keywords in this cluster are pretty

**Aida Knezevic:** They're pretty competitive, but we do need, and ranking for these keywords might be more difficult because there's just a lot of competition here, a lot of websites are publishing content about this, but it's important to establish your topical authority and to signal to Google like, hey, this is what we do, and it's also going to help in AI visibility as well because LLMs are going to start associating you with these topics as well.

**Aida Knezevic:** So, the initial rankings here might not be that high, but it does help in the long term.

**Aida Knezevic:** And yeah, this, you know, this cluster also allows us to kind of not just build topical authority, but for the people that do come to your website, we can point out, you know, your core speed differentiator compared to your competitors.

**Aida Knezevic:** The second cluster would just cover automation for business users.

**Aida Knezevic:** I know in the kickoff call, you mentioned how kickoff call.

**Aida Knezevic:** go.

**Aida Knezevic:** Like people in operations might almost be kind of the people that you don't want to target because there might be gatekeeping some of this, like some of these tools for automating these processes.

**Aida Knezevic:** And this cluster would target regular users who just need to know how to do a specific action.

**Aida Knezevic:** For example, how to automate workflows without coding, process automation tools for business users.

**Aida Knezevic:** And also this cluster would include keywords that are pretty competitive and pretty, I mean, competitive in the sense that they would talk about your competitors.

**Aida Knezevic:** Um, and they're more bottom of the funnel, so we'll talk about Zapier alternatives, um, or maybe even like some comparison blog posts if, if that's something that you want to do.

**Aida Knezevic:** Um, but this would really, um, allow you to talk about your product in the way that you want to talk about it.

**Aida Knezevic:** Um, and it's very important that this content.

**Aida Knezevic:** and very important.

**Aida Knezevic:** It's kind of on point in terms of like the product messaging and positioning, because it's going to inform LLMs as well.

**Azzam Aijazi:** Yeah.

**Aida Knezevic:** The third one is more industry specific.

**Aida Knezevic:** So it's going to, the content under this cluster is going to be related to topics like e-commerce, content moderation, automating in fintech or in logistics processes.

**Aida Knezevic:** So this would kind of capture those searches where people are coming from different industries.

**Aida Knezevic:** The ones that I highlighted here, the ones that you highlighted in the kickoff call, which were, I think, fintech, e-commerce, and logistics.

**Aida Knezevic:** But we can, you know, expand into as many as you want as, you know, as your audience changes as well.

**Steve Krenzel:** Cool.

**Aida Knezevic:** Makes sense.

**Azzam Aijazi:** I'll spend some time going through it soon. Just a quick impression: really positive. You've hit the key priorities on our end.

**Aida Knezevic:** Okay, perfect.

**Steve Krenzel:** Nice.

**Steve Krenzel:** It's, like, actually really remarkable how quickly you zeroed in on, like, the key things we were thinking about, so thank you.

**Erik O'Brien:** The link will post in the channel.

**Aida Knezevic:** Great, I shared the link. This is just an idea of where we want to go.

**Aida Knezevic:** If you think of any additional angles, any additional topics, like, whatever comes to mind.

**Aida Knezevic:** Any idea or topic you think your audience could be interested in is valuable. Leave comments in the doc and we'll incorporate them into the keyword research.

**Aida Knezevic:** Let's see if there's anything else outside the content strategy. We've covered images and Scrunch.

**Aida Knezevic:** The next steps: once you review the content strategy, we'll make edits as needed and move forward with keyword research and blog ideas. Then we'll upload everything to an Airtable content calendar.

**Aida Knezevic:** You'll have access to it — it's the single source of truth for content moving forward. You'll see everything in production, up for review, and published.

**Aida Knezevic:** We hook Airtable up to Looker so we can track blog performance by cluster and see which ones are doing best.

**Steve Krenzel:** I don't have anything on my agenda.

**Azzam Aijazi:** No, I think that's it. I'm looking forward to seeing the content calendar proposal — everything we discussed here has been great, and I'm excited.

**Aida Knezevic:** Great. I think we have a good idea of what we need to do for you.

**Aida Knezevic:** I'm going to get back to you regarding the LinkedIn social posts.

**Aida Knezevic:** And yeah, anything else you need, I'm available over Slack.

**Aida Knezevic:** I'm based in Europe, but I usually work evenings because most of my coworkers are based in the U.S.

**Aida Knezevic:** So I'm usually here in the PM.

**Aida Knezevic:** Thanks so much for your time.

**Steve Krenzel:** Yeah, I'll see you next week.

**Azzam Aijazi:** Thank you. Have a good one.
