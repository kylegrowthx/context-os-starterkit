# Logic <> Growth X - Weekly Sync

<metadata>
date: 2026-02-04
time: 18:29 UTC
duration: 60 minutes
organizer: team@growthxlabs.com
participants: Azzam Aijazi (Logic), Bailey Seybolt (GrowthX), Steve Krenzel (Logic)
fathom_recording_id: 119774666
fathom_url: https://fathom.video/calls/554059457
share_url: https://fathom.video/share/s-j6AewsEyvEjWMv3eEHj7PLjVAcxo76
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Logic and GrowthX aligned on a new content pipeline delivering two articles this week with significant quality improvements, and established a 3-month refresh cadence for all articles to keep pace with the product's rapid evolution. Early SEO signals are strong—the "LangGraph Alternatives" post already ranks #8—and the team committed to launching an ungated "How to Build an Agent" guide as a premium SEO asset.

---

## Context

This is a weekly sync between Azzam Aijazi (founder/CEO, Logic) and Bailey Seybolt (GrowthX Head of Content), with Steve Krenzel (Logic CTO) joining on technical questions. The partnership centers on Logic's content strategy and SEO performance. Bailey's team recently completed a content strategy recalibration and built a new content generation pipeline that Logic's engineering team is now delivering through. The conversation focuses on validating the new pipeline's output quality, establishing content maintenance processes to keep pace with Logic's fast-moving product roadmap (e.g., new agent capabilities, positioning shifts), and integrating content performance data with Logic's internal conversion tracking (Statsig) and new LLM visibility monitoring tool (CheckThat, replacing Scrunch). The engagement is strategic—content is a lead generation and authority-building channel, not a direct conversion driver.

---

## Relevance

**Content Operations & GTM Strategy**
- New content pipeline signal of quality improvement and faster delivery; validates content strategy shift toward technical agentic keywords
- 3-month refresh SLA establishes predictable content ops cadence and prevents messaging decay in fast-moving product category
- Strong early SEO signals (fast indexing, #8 ranking for high-intent keyword) validate content-led GTM approach

**CheckThat & LLM Visibility**
- Transition from Scrunch to CheckThat improves contextual accuracy of LLM visibility scoring (0.5% current visibility is likely underestimated)
- Citation tracking reveals which content assets drive LLM citations (e-commerce content moderation, case studies) — actionable for future content planning

**Alternatives & Listicle Content**
- "Alternatives" and listicle posts show outsized impact on both organic traffic and conversion lifts — key content format to prioritize
- Validates GrowthX strategy of targeting high-intent comparison keywords

**Content-to-Conversion Attribution**
- Statsig integration with Looker dashboard will enable win-rate tracking on content pieces and shift content investment from impressions/clicks to direct conversion impact

---

## Overview

- **New Content Pipeline:** A new pipeline is live, delivering two articles this week with a "step change improvement" in quality.
- **Aggressive Refresh Cadence:** A 3-month refresh cadence was set for all articles to ensure content stays current with Logic's fast-moving product and industry.
- **Strong Early SEO Signals:** New articles are indexing in hours, and the "LangGraph Alternatives" post already ranks \#8, validating the new content strategy.
- **New Content Asset:** A long-form "How to Build an Agent" guide will be published as an ungated, premium asset to drive SEO and establish authority.

---

## Key Topics

### Content Pipeline & Quality

  - A new content pipeline is live, delivering two articles this week.
  - The first new article is due tomorrow; Rachel (Logic) noted a "step change improvement" in quality.
  - **Action:** Azzam to review \~5 articles in the old pipeline.
      - If quality is poor → flag for Rachel to rerun through the new pipeline.
      - Rationale → Avoid wasting time on granular edits for content that doesn't align with the new strategy.

### Content Refresh Strategy

  - This week's content will mix net-new articles with refreshes of high-performing pages.
  - **Goal:** Test the refresh pipeline's ability to update content with new positioning without hurting existing SEO rankings.
  - **Decision:** Prioritize correct messaging over preserving outdated SEO performance.
      - Rationale → The primary goal is to tell the right story, and these articles aren't direct conversion drivers.
  - **New SLA:** A 3-month refresh cadence was set for all articles.
      - Rationale → Logic's product and industry move too quickly for content to stay relevant longer.
      - Process → Airtable reminders will trigger the refresh cycle.
  - **SEO Tactic:** Update the `published_at` date in StoryBlock during refreshes to signal freshness to search engines.

### "How to Build an Agent" Guide

  - Logic is creating a long-form guide to establish authority and drive SEO.
  - **Format:** An ungated, premium asset (like the Aeroops report example) living outside the main blog.
  - **Goal:** Outrank the current \#1 Google result for the target keyword.
  - **Action:** GrowthX to review the guide and provide feedback on structure and SEO.

### Reporting & Integrations

  - **Statsig Access:** Azzam will add Bailey as a Statsig user to track content-to-conversion attribution.
  - **Image API:** Logic will provide an API key for the image generation service to automate content creation.
  - **Check That Tool:** A Loom walkthrough is coming this week, with logins next week.
      - Rationale → Check That's superior contextual understanding will provide more accurate LLM visibility scores than the previous tool (Scrunch).

### January Performance & SEO Signals

  - **Fast Indexing:** New articles are indexing within hours, a strong positive signal.
  - **Strong Keyword Rankings:**
      - "LangGraph Alternatives" → \#8
      - "Make.com Alternatives" → \#14
  - **LLM Visibility:** 0.5% visibility is driven by citations of specific blog posts (e.g., "e-commerce content moderation") and case studies.
  - **Key Insight:** "Alternatives" and listicle-style posts are driving outsized traffic and conversion lifts.

---

## Action Items

**Azzam Aijazi (Logic)**
- Review ~5 legacy articles in old pipeline; flag poor-quality pieces to Rachel for rerun through new pipeline
- Add Bailey to Statsig as user to enable content-to-conversion tracking
- Investigate feasibility of Statsig-to-Looker integration for consolidated reporting (or manual monthly export)
- Enable and share image-generation API key with Bailey; Logic can consume via API or web UI per GrowthX preference
- Confirm with Steve/team that external parties can hit Logic's API with API key from Logic org

**Bailey Seybolt (GrowthX)**
- Set Airtable reminders for 3-month refresh SLA on all articles (trigger refreshes based on publication date)
- Review "How to Build an Agent" guide; provide SEO structure feedback, hanging fruit suggestions, and length/depth assessment
- Confirm Storyblok and Atlas support for updating `published_at` date fields during refresh workflow, then incorporate into refresh process
- Record async Loom walkthrough of CheckThat tool and send to Azzam; provide logins next week
- Send detailed LLM citation list (specific queries and article URLs) to Azzam showing which content is being cited in LLM responses
- Update agentic keyword cluster strategy with director input; update Looker visualization and content priority plan this week

---

## Decisions & Commitments

**Content Refresh Strategy & SLA**
- Commit to 3-month refresh cadence for all blog articles (no article should be >3 months without refresh)
- Rationale: Logic's product and industry move too fast for older content to remain relevant; even secondary positioning changes require messaging updates
- Trigger process: Airtable reminders based on publication date will flag articles for refresh

**Messaging Priority Over SEO Rankings**
- Decision: Prioritize correct, current messaging over preserving outdated SEO performance on refreshed articles
- Rationale: These articles are lead-generation channels, not direct conversion drivers; wrong messaging is worse than lower rankings
- Approach: Reframe articles for engineering persona where applicable; light refresh for CEO persona articles; full rewrites where needed

**"How to Build an Agent" Guide as Premium Asset**
- Format: Ungated, premium long-form guide (like Aeroops report model); not a gated lead magnet
- Placement: Separate from main blog (possibly new "Guides" section or Resources subsection); gets priority internal linking from blog posts
- Goal: Outrank current #1 Google result for target keyword; establish Logic as authority on agent development
- Rollout plan: Make this a regular cadence (frequency TBD based on topic importance)

**Published Date Updates During Refreshes**
- Commit: Update `published_at` date field in Storyblok during all refresh cycles to signal freshness to search engines
- Approach: Confirm with Storyblok/Atlas support for updatable fields; integrate into standard refresh workflow

**Content-to-Conversion Tracking**
- Add Bailey to Statsig to track which articles and content pieces drive actual sign-ups, not just impressions/clicks
- Stretch goal: Integrate Statsig data into Looker dashboard for centralized reporting
- Fallback: Manual export and review monthly/weekly as baseline

---

## Open Questions

- What cadence makes sense for the "How to Build an Agent" guide rollout? (One per quarter, twice a year, or strategic one-offs?)
- Can Statsig data be pulled directly into Looker, or will manual export be the standard workflow?
- For articles originally written for "no-code automation" persona: reframe completely for engineering audience, or keep as dual-persona content?
- Does Google penalize frequently updated `published_at` dates if refreshed more aggressively than the actual content changes?
- What other topics (beyond "How to Build an Agent") are strategic enough for the premium guide treatment?

---

## Transcript
**Bailey Seybolt:** All right.

**Bailey Seybolt:** Well, a lot's going on.

**Bailey Seybolt:** So I'll share our notion.

**Bailey Seybolt:** Is Steve joining today or should we just jump in?

**Azzam Aijazi:** We can jump in, but he is joining.

**Bailey Seybolt:** So yes, and.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So blog updates.

**Bailey Seybolt:** So I want you to know that sort of noting your feedback throughout this recalibration process, our engineering team was back in your pipeline yesterday, and they have built a new pipeline today.

**Bailey Seybolt:** So for this week, we'll be delivering two new articles.

**Bailey Seybolt:** So far, I haven't seen them.

**Azzam Aijazi:** Rachel's taken a look and she says she thinks that's a step change improvement.

**Bailey Seybolt:** So I'm going to take a look as well, but we should be delivering the first of the new articles tomorrow.

**Bailey Seybolt:** Okay, cool.

**Azzam Aijazi:** I know that there's like five that are currently in pipe for like me to review or like there's a canful.

**Azzam Aijazi:** Oh, yeah, says about five million client reviews.

**Bailey Seybolt:** Should I still go ahead and review those as they are, should I expect those might get redone, or what should I do with those?

**Azzam Aijazi:** I think you should review them, but if you feel, like, it seems like we've had, it's better, like, I feel like we're in the right direction enough.

**Azzam Aijazi:** Yeah, has been that, like, there's been, like, fits and starts, but by and large, we're, like, moving in the right direction.

**Bailey Seybolt:** Yeah, so what I would say, I would say go in and review them, because I think the more we can get published, the better.

**Bailey Seybolt:** If you start reading and you feel like this is one of these ones that feels off, just leave that as a comment and tag Rachel in that topic specifically.

**Bailey Seybolt:** She'll just run it through this new pipeline, because it seems like it's pretty specific in terms of the things it's missing and the kind of topics it seems to be struggling with.

**Bailey Seybolt:** So, yeah, I would just do it that way.

**Bailey Seybolt:** Don't waste your time if you feel like you're in there having to give, like, super granular line edits.

**Bailey Seybolt:** Just flag that, and then we'll just rerun that topic specifically.

**Azzam Aijazi:** Cool.

**Bailey Seybolt:** I'm also proposing that this week, instead of just doing NetNew, we do a mix.

**Bailey Seybolt:** Of refreshes as well, because I want to test how the refresh pipeline handles this positioning change, and I wanted to start it with pages that are kind of already gaining organic traction, because I think with the new positioning, that'll be a good test to see if we can kind of accelerate the ranking test there with the new angle and positioning to see if they're going to connect with the target audience and give those ones a boost.

**Bailey Seybolt:** So my proposal was we do a few new articles, allow you to, like, view the new pipeline, and then also kind of start with the refreshes, so you can take a look and see how it's doing there as well.

**Azzam Aijazi:** Okay, cool.

**Azzam Aijazi:** So I have, like, two or three questions here.

**Bailey Seybolt:** Yeah.

**Azzam Aijazi:** So one is, like, I'm actually, like, I'm happy we're talking about refreshes, because this is one the questions I had coming into this.

**Azzam Aijazi:** I guess my broadest question, we don't have to answer first, is, like, what should be our strategy around refreshes generally?

**Azzam Aijazi:** I know we've talked about it as a thing that we're going to be covering.

**Azzam Aijazi:** Considering especially our new positioning, our new approach, we have new image tiles, all these things.

**Azzam Aijazi:** Is there like a timeline by when we are targeting to hit everything?

**Azzam Aijazi:** Are we just starting with the most, you know, effective ones, like the highest achieving ones first, then we're going our way down?

**Azzam Aijazi:** I'm just curious, like, what is our approach?

**Azzam Aijazi:** Because we do have like a relatively large-ish number of articles on our blog right now that are, that feel sort of out of date, that I'd love to do something about as soon as possible.

**Azzam Aijazi:** Yeah, for sure.

**Azzam Aijazi:** As far as starting with these ones, like, yeah, that seems reasonable enough.

**Azzam Aijazi:** The thing I'm like, I'm not clear in my head about is like, these keywords would not have been chosen by us today, given our new positioning.

**Azzam Aijazi:** And so I definitely want to like update our stance on these keywords and like make them more almost like engineering focused.

**Azzam Aijazi:** And even when we talk about no-code automation, would that like change how well we're doing?

**Azzam Aijazi:** Like, might that like tank performance because it's no longer written for the

**Azzam Aijazi:** The kind of people that search for no-code automation, like what's your take on how do these survive a messaging pivot?

**Bailey Seybolt:** So I think for content, if it's already ranking pretty well, I mean, the general guideline is the less you change it, the better.

**Bailey Seybolt:** Like you want to deepen context, you know, make sure it's accurate, update links.

**Bailey Seybolt:** But the answer is yes, it can hurt your performance if you go in and rewrite the article from ground zero.

**Bailey Seybolt:** So one of the reasons I wanted to test with these is because they're already ranking.

**Bailey Seybolt:** I think trying to find that balance between not hurting the ranking, but also making sure that it's relevant and accurate, I think is kind of the test case for these.

**Bailey Seybolt:** And in terms of refreshes, I think, yeah, we want to refresh everything, right?

**Bailey Seybolt:** You don't want to have any content on your blog that feels like it's not speaking properly to your persona or to, you know, correctly presenting.

**Bailey Seybolt:** Your product.

**Bailey Seybolt:** I am aware that, I mean, I think when we originally talked about the pivot to, like you did sort of have that more CEO business oriented persona as a kind of not even secondary, like secondary or tertiary persona.

**Bailey Seybolt:** And I think some of these articles are probably intended for that persona, like they might not be as relevant for the engineering persona.

**Bailey Seybolt:** So I think probably what we want to do is like take a look at the keyword and think about the search intent and decide, like, is this an article that should be reframed for this more technical persona?

**Bailey Seybolt:** Because we want to capture that keyword from like a different intent.

**Azzam Aijazi:** Yeah.

**Bailey Seybolt:** Is it one that's just more relevant to that CEO persona?

**Bailey Seybolt:** In which case it's probably just like a light refresh to make sure that Logic's positioning makes sense.

**Bailey Seybolt:** And then, you know, where is it ranking now or do we want to try to kind of preserve that position?

**Bailey Seybolt:** Or is this an exercise in just starting over and essentially running it as a new article?

**Azzam Aijazi:** It almost feels like if we were to choose to refresh these, this would almost be like a slightly different version of the pipeline.

**Azzam Aijazi:** If it's like, hey, you are a senior executive working with engineering counterparts and trying to introduce no-code automation to your business, what does that look like?

**Azzam Aijazi:** What are your options?

**Azzam Aijazi:** But I want to be clear as well that if the choice is between high-performing with out-of-date messaging or messaging that doesn't align with our current audience and lower-performing with better messaging, I actually would choose the latter.

**Azzam Aijazi:** I don't want to optimize for performance at the expense of compromising what we're trying to sell and what the story actually is that we tell folks, especially considering these aren't converting directly yet.

**Azzam Aijazi:** So like, yes, they are, like, these are, it's nice to have like leading indicators about what's working well, but it's not like we would be losing business by plugging, you

**Azzam Aijazi:** So updated messaging into these and these slightly, slightly dropping.

**Bailey Seybolt:** Yeah, 100%.

**Bailey Seybolt:** You want to prioritize unoptimized for having the right messaging that we think tells our story.

**Bailey Seybolt:** Yeah, I think that definitely makes sense.

**Bailey Seybolt:** And so, I mean, my recommendation for refreshes, like the reality is that refreshes, when you start from the beginning, it's essentially like you're running a new article, but can be just as valuable or even more valuable, especially if they've already started to kind of like make their way up in terms of like visibility.

**Bailey Seybolt:** So I would probably just propose doing like a certain number of new articles and refreshes every week.

**Bailey Seybolt:** Probably what I could do is once we get a sense of the refresh pipeline, kind of how well it's working, how long it's taking, how much it's like a simple update versus kind of rare.

**Bailey Seybolt:** Writing something from scratch, from ground zero, I could just kind of just make us like a project plan and plan how long it would take us, you know, per week.

**Azzam Aijazi:** I mean, could I request like a slightly different framing of this?

**Azzam Aijazi:** Like what I would love to have is almost like an SLA on article, like freshness.

**Azzam Aijazi:** So it's like anything, no article should be more than three months out of date.

**Azzam Aijazi:** Like if it should have been three months and it hasn't been refreshed, we should do something.

**Azzam Aijazi:** And I think that's like maybe a better approach to start from just because as like the number, as like the denominator increases in quantity over time, if we're just doing like N refreshes per week, eventually that's not going to be enough to hit all of them within like a three-month window.

**Azzam Aijazi:** And so like, is that like a reasonable goal do you think for us to have?

**Azzam Aijazi:** It's like a no article should have gone three months without being refreshed in some way?

**Bailey Seybolt:** Yeah, I would say it depends on the industry.

**Bailey Seybolt:** Like I'd say six months is probably standard, but if you're in an industry that's moving quickly with a lot.

**Bailey Seybolt:** And I think anywhere from one month to three months makes sense.

**Azzam Aijazi:** Okay.

**Azzam Aijazi:** I would love for our target to be three months because not just like the industry, but also our product is moving so quickly that anyone that's read messaging from more than three months ago, like I will have had like an outdated view of our product at this point.

**Azzam Aijazi:** And so I do think it's important that we hit like a somewhat aggressive like timeline on that.

**Bailey Seybolt:** Yeah, I think that makes sense.

**Bailey Seybolt:** So we can certainly do that.

**Bailey Seybolt:** And then what we do is we usually just like set a reminder on Airtable based on the publication date and it will let us know like what, when to work things into the refresh cycle.

**Azzam Aijazi:** Cool.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** So in terms of everything we talked about last week, I brought in our directors.

**Bailey Seybolt:** So I updated the strategy and the KPIs and our kind of content priority plan.

**Bailey Seybolt:** And I wanted to bring in more sort of expert technical support.

**Bailey Seybolt:** to validate that agentic cluster, because I think that so much of the search intent there is going to require that technical knowledge of engineering communities.

**Bailey Seybolt:** So they're taking a look at that strategy and kind of making any suggestions around how to approach it.

**Bailey Seybolt:** And so then once I get feedback there, I will update kind of all that documentation and also add more article topics for you to review more focused, around the agentic keywords that we had talked about.

**Bailey Seybolt:** So that hopefully will come, either way, I'll update you this week.

**Azzam Aijazi:** Okay, cool.

**Bailey Seybolt:** And then also, I will also update Looker once we have that to make sure that the new kind of, the new cluster organization is reflected there going forward.

**Bailey Seybolt:** So you'll see in the report this month, it's outdated, because I'm just waiting to hear back on that.

**Bailey Seybolt:** And then we'll update that as well for visibility.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Oh, I did try to sign in to Statsig.

**Azzam Aijazi:** It wasn't working.

**Azzam Aijazi:** I think I saw on a message.

**Azzam Aijazi:** Yeah, I think that the approach we need to take is probably just add you as a user to Statsig as opposed to trying to create some published sharing way of doing it.

**Azzam Aijazi:** I can go ahead and do that.

**Azzam Aijazi:** And remind me, the thing that we wanted to have here was we wanted to have you have this ability on, like, which articles or which content is leading to actual convergence, correct?

**Bailey Seybolt:** Yeah, basically, we want to be able to connect content to your conversion pipeline and just get a sense of, you know, not just what's performing in terms of impressions or even clicks, but, like, directly what's leading to sign-ups and what that flow looks like to give you a better sense of where to invest in content.

**Azzam Aijazi:** Okay, sweet.

**Azzam Aijazi:** I'm not sure to what extent we can track, like...

**Azzam Aijazi:** That through line, I'm still trying to figure that out on StatSign myself, but yeah, I'll keep you posted on easy access.

**Bailey Seybolt:** Yeah, keep us posted, and I mean, if you want to export data, it might be, I wanted to see if it was even possible to pull anything directly into Looker, just so it's all in one place and more visible.

**Bailey Seybolt:** I'm not sure if that's possible, but we can certainly investigate once we have access.

**Azzam Aijazi:** I'm fine, too, start doing this manually, just because, like, the numbers are so low that maybe, like, once a month or a week or so is probably fine.

**Azzam Aijazi:** And then if this turns out to be quite helpful, then, yeah, we can look at automating that in some way.

**Bailey Seybolt:** Okay, perfect.

**Bailey Seybolt:** That sounds great.

**Bailey Seybolt:** Oh, yeah, and for the images, if you want to expose it as an API, can see, talk to our team and see if we can add that directly to our pipeline.

**Bailey Seybolt:** We're also fine for now adding those images manually.

**Azzam Aijazi:** Yeah, I mean, it's your call.

**Azzam Aijazi:** It's the same for us, the same expense for us.

**Azzam Aijazi:** Make much difference as far as we're concerned.

**Azzam Aijazi:** So it's up to you in terms of how you all would rather consume that.

**Bailey Seybolt:** If it's through like the web UI or through the API, it shouldn't make much Yeah, if you want to share it, that would be great.

**Bailey Seybolt:** I like having everything in one place for us wherever possible.

**Bailey Seybolt:** That way it's less chance for communication to fall through the cracks.

**Azzam Aijazi:** Okay.

**Azzam Aijazi:** Maybe this is a question for Steve, actually.

**Azzam Aijazi:** I'm not sure how this would work.

**Azzam Aijazi:** But is there a way for someone who's not part of the Logic org to hit the Logic API to select the API for like an agent and have it work?

**Azzam Aijazi:** Or do they have to like create it in their org for it to work as an API?

**Steve Krenzel (Seattle):** If they're just calling the API, yeah, we can give them, I mean, can just give them an API key from our org.

**Azzam Aijazi:** Okay.

**Steve Krenzel (Seattle):** Yeah.

**Azzam Aijazi:** Okay, cool.

**Steve Krenzel (Seattle):** Happy to do that.

**Azzam Aijazi:** All right, sweet.

**Azzam Aijazi:** We'll figure it out.

**Steve Krenzel (Seattle):** Yeah.

**Azzam Aijazi:** Okay, so that's an action for me on our side to figure out how to get you the API working for image generation.

**Bailey Seybolt:** Yeah, perfect.

**Bailey Seybolt:** That'd be great.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I think the other thing I wanted to make sure that we talk about before I chat through reporting and check that is the, I know you saw the how to build an agent guide.

**Bailey Seybolt:** I was wondering what kind of feedback kind of would be most useful for you or like if you have specific open questions or like how you're thinking about positioning the document strategically just to sort of give a little more context there.

**Azzam Aijazi:** I mean, I guess the things that I was hoping to hear from you, if anything, would be like, what might we do that might help this rank higher more effectively?

**Azzam Aijazi:** Like, is there anything that you see as a little hanging fruit?

**Azzam Aijazi:** Anything that you're seeing that's like, hey, this is like, this is way too long.

**Azzam Aijazi:** This is way too in the weeds.

**Azzam Aijazi:** Like you need better structure.

**Azzam Aijazi:** Anything like that sort of advice would be really, really helpful.

**Azzam Aijazi:** Otherwise, it's I think it's more just a general like FYI.

**Azzam Aijazi:** I mean, if you have.

**Azzam Aijazi:** If you any particular, you know, concerns or questions, I'm happy to answer them.

**Bailey Seybolt:** How are you planning on sort of surfacing it or serving it?

**Bailey Seybolt:** I know it's going to be a lot longer than kind of just, you know, a standard blog post.

**Bailey Seybolt:** How are you planning on, like, is it going to be a download link on your website?

**Azzam Aijazi:** No, I wanted it to be an ungated, like, in my head, I've been calling it like a pseudo landing page.

**Azzam Aijazi:** I'll give you an example of one that I like, which is, like, this Aeroops report.

**Azzam Aijazi:** Hold on.

**Azzam Aijazi:** There you go.

**Azzam Aijazi:** I dropped it in the Zoom chat.

**Azzam Aijazi:** But it's just, like, an original piece of content that lives on its own somewhere.

**Azzam Aijazi:** It's findable by Google on Index.

**Azzam Aijazi:** It's nicely, like, visually laid out and designed.

**Azzam Aijazi:** Yeah.

**Azzam Aijazi:** Gets premium treatment.

**Azzam Aijazi:** It sort of looks and feels like a blog.

**Bailey Seybolt:** Yeah.

**Azzam Aijazi:** I think it's actually important that it not just live on our blog as a blog post, but feel more...

**Azzam Aijazi:** We might even want to add this to our website, footer as a separate primary asset that's linked from more places, but I want to pull out all the stops essentially to make this feel really special and high level and not gate this just so that it does its work on SEO and AEO and gets us as high ranking as possible.

**Azzam Aijazi:** I specifically wrote this looking at what was number one on Google today and trying to beat that just so we can get all the way up there.

**Bailey Seybolt:** No, I think that definitely makes sense.

**Bailey Seybolt:** And we can take a look at it thinking about that.

**Bailey Seybolt:** And I think some of it too is like making it a priority to link to it from blog posts so you get those internal links.

**Bailey Seybolt:** I'm wondering if you plan to do this on a regular basis, like if you want to create a new category under your resources.

**Azzam Aijazi:** Yeah, was thinking about that exact question.

**Azzam Aijazi:** So I think that...

**Azzam Aijazi:** I do want to do it on a regular basis.

**Azzam Aijazi:** I don't know what else, like what other topics we'd want to own that are this important.

**Azzam Aijazi:** I can't think of any other ones on top of my head.

**Azzam Aijazi:** But yeah, I think that there is value in there being like long form content living in some other place.

**Azzam Aijazi:** That probably ideally would have been called resources, but we're already using that for our blogs.

**Azzam Aijazi:** Maybe it's something, maybe it's like assets or something like that.

**Azzam Aijazi:** Guides, maybe it's guides, yeah, guides could work.

**Azzam Aijazi:** But yeah, I would love for that to look and feel in some way different and be somewhere different.

**Bailey Seybolt:** Yeah, I think that makes a lot of sense.

**Bailey Seybolt:** And especially if you plan on doing it on a more regular basis, having that more, those more in-depth pieces, hopefully like ones that can include, you know, more primary sources or, you know, quantitative and qualitative insights that are unique to your business.

**Bailey Seybolt:** Having those be stored somewhere separate, like under resources, and making sure that we call those out as a priority link from within all the blog posts feel like a good way to kind of contribute to the SEO attraction there.

**Azzam Aijazi:** Yeah, fair enough.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Yeah, so happy to take a look at that too and see if we have other recommendations as well.

**Azzam Aijazi:** yeah, please do, please do.

**Azzam Aijazi:** I think that this is the time for it to be shaped in whatever way is meaningful and helpful.

**Azzam Aijazi:** So if you have small feedback, large feedback, medium-sized feedback, let me know.

**Bailey Seybolt:** All three of the Goldilocks and three bears.

**Azzam Aijazi:** Just let me know.

**Azzam Aijazi:** I'm not married to anything in there.

**Azzam Aijazi:** It's very flexible right now, so it would be a great time.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Okay, we will do that.

**Bailey Seybolt:** And CheckThat—our tool is rolling out this week. It wasn't quite ready for a walkthrough this morning, so what I'm going to do is try to record an async Loom and send it to you, and then hopefully answer any questions, and hopefully logins will be going out next week as well.

**Bailey Seybolt:** In terms of January, I know some of this is like less relevant because, you know, cluster performance matters less when we're about to change them all, but there were some, you know, positive signals here.

**Bailey Seybolt:** One, the articles are indexing really quickly, which is like a good, a good signal, like within, you know, hours, there was nothing sitting there lingering for a few days, which is great.

**Bailey Seybolt:** I think the other thing that was exciting as we started, we're already ranking for the Landgraf Alternatives keyword at position eight, which is an awesome, yeah, awesome early signal.

**Bailey Seybolt:** And make.com Alternatives is also now at position 14.

**Bailey Seybolt:** So, but yeah, that lane graph one was exciting and kind of validating that, you know, the new content lane is being picked up and is valuable.

**Bailey Seybolt:** So we'll keep an eye on that and we'll get better visibility into it on Looker as a visualization once we update those clusters.

**Bailey Seybolt:** In terms of LLM visibility, I also wanted to call out once you get into Looker, the numbers here may look different than Scrunch, just because we're tracking slightly different prompts and have organized the competitors and landscape a little bit differently. So we can kind of talk through that once we're in the tool, but just so you're not surprised if it looks different. We haven't seen a ton of movement over the last few weeks yet, but I think as this content indexes and the new content indexes, there'll be more movement here.

**Bailey Seybolt:** One thing that I think is also a good sign is right now, I notice on Check That versus Scrunch comparing them, Check That is doing a much better job at contextual understanding of what Logic does, whereas I think some of the Scrunch prompts, you'd get, like, Logic the concept in there.

**Bailey Seybolt:** I didn't totally understand semantically all the time, and I think that also skewed the numbers.

**Bailey Seybolt:** So far from what I've seen in the prompt tracking in Check That, it's, like, hasn't let any of that slip through, so I think the visibility scores there will give a more accurate idea.

**Azzam Aijazi:** that's awesome.

**Azzam Aijazi:** Do we know what that 0.5% is coming from?

**Azzam Aijazi:** Like, what kinds of queries are we ranking for?

**Azzam Aijazi:** Like, are they, like, I guess I'm surprised to see that that number is that high, to be honest.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** So I can dig in.

**Bailey Seybolt:** Once you have access to the tool, you'll be able to actually go in and see your prompts and exactly what questions you are appearing in.

**Bailey Seybolt:** I know looking at citations specifically, there were a number of blog posts that were being cited, the ones around content moderation, the N8 alternatives.

**Bailey Seybolt:** Things mentioned in case studies tended to be like the things that I think were getting cited more often.

**Bailey Seybolt:** So I think it was, I didn't, most of the prompts I saw was more around the original content and use case and not kind of anything that was more updated.

**Bailey Seybolt:** But I think hopefully as that.

**Azzam Aijazi:** Okay.

**Azzam Aijazi:** But it's likely like our blog posts that are being picked up here, not necessarily like Logic's homepage, which is fine.

**Azzam Aijazi:** That's great.

**Azzam Aijazi:** I'm just, but does that seem accurate?

**Bailey Seybolt:** I think so, yeah.

**Bailey Seybolt:** I So I

**Bailey Seybolt:** I can go in and actually after this I can follow up and just give you a list that gives you a better sense of exactly what's being picked up.

**Azzam Aijazi:** Sure thing, yeah.

**Bailey Seybolt:** And so, yeah.

**Bailey Seybolt:** Oh, yeah.

**Bailey Seybolt:** I was going to say the automate, the e-commerce content moderation was the one that they were landing on the most, but there was also homepage, yeah, the DroneSense case study, and then the zero-touch automation, that was the other article.

**Azzam Aijazi:** Great, okay.

**Bailey Seybolt:** We talked about content attribution, so I think we're good there.

**Bailey Seybolt:** I think those were the things that I wanted to point out for now.

**Azzam Aijazi:** Okay, cool.

**Azzam Aijazi:** Yeah, I was poking through the numbers yesterday, and I had noticed that that LangGraph article was pulling in some traffic, it seems like the numbers that I'm seeing on StatsAger.

**Azzam Aijazi:** Yeah.

**Azzam Aijazi:** It

**Azzam Aijazi:** Ever so slightly different from what you're seeing, and I'm not sure why that might be, because I think you're tied into Google Analytics.

**Azzam Aijazi:** But regardless, from what I was seeing, it was our number one or two traffic sourcing blog posts already, which was surprising and good to see.

**Bailey Seybolt:** Yeah, well, makes sense why you're ranking at number eight already, which is...

**Azzam Aijazi:** Yeah, that's awesome.

**Azzam Aijazi:** And it could be, I was pulling data just from January 1st to 31st, so that also could be a reason if you're looking at a slightly different...

**Azzam Aijazi:** Yeah, I I was looking at the last, like, three days or so, so maybe that's...

**Bailey Seybolt:** Yeah, okay.

**Bailey Seybolt:** It could be that then that's skewing it.

**Azzam Aijazi:** Cool.

**Bailey Seybolt:** But that's great.

**Bailey Seybolt:** That is good to know, and yeah, good to keep an eye off.

**Bailey Seybolt:** And we've seen just in terms of, like, trends we're seeing across accounts, we're seeing those, like, comparison posts, the alternative posts, anything that feels like a listicle is having, like, a hugely outsized impact in terms of LLM visibility and traffic.

**Bailey Seybolt:** So I think those are really good, it's a good lean of content to prioritize as well because we're seeing it give such a lift to really high intent traffic too.

**Bailey Seybolt:** Like it's also, we've seen where we're tracking conversion, we've seen it give like a big lift there as well.

**Azzam Aijazi:** Yeah, sweet.

**Azzam Aijazi:** That's awesome.

**Azzam Aijazi:** I appreciate that.

**Azzam Aijazi:** One of the things I wanted to call out is that one of the reasons that articles seem to do well nowadays is like super recent edited ad or published ad dates.

**Azzam Aijazi:** So as we do make edits to articles, I want make sure that we're also refreshing the dates on them, whether that's like, don't know, whether that's somewhere in like the meta fields or the story blog support that I can't recall as a thing that we can edit.

**Azzam Aijazi:** But I want to make sure that these always feel super up to date even at this level on a search result on Google.

**Bailey Seybolt:** Yeah, that's a very, it's a good call out and I'll make sure that that is a field that gets updated when we do those refreshes.

**Bailey Seybolt:** Either manually or from Atlas, I'll have to check in and see, since we haven't done it for you yet, what's the best way to do it.

**Azzam Aijazi:** And like, even for myself, if I'm doing research on like, what LandGraph does, like, I don't want to have an article from 2024.

**Azzam Aijazi:** That's almost useless at this point.

**Azzam Aijazi:** It's so old for something that's moving so fast.

**Bailey Seybolt:** A hundred percent.

**Bailey Seybolt:** Yeah.

**Steve Krenzel (Seattle):** Just confirming, that is a field in StoryBlock we can set, so.

**Azzam Aijazi:** Can we just like, always set it to being three weeks ago or something?

**Azzam Aijazi:** Is that like, a good thing that we could do?

**Steve Krenzel (Seattle):** Uh, no, but, I mean, we, we, we can program whatever we want, but, uh.

**Azzam Aijazi:** I gotta, I don't know, I don't know if Google would actually like, punish that or like, read through it in some way also, so maybe we shouldn't mess with that, um, willy-nilly, but, yeah.

**Azzam Aijazi:** I would love if we could actually work in a way that, that, that was never, you know, more than three-ish months Saturday.

**Bailey Seybolt:** Yeah, I mean, I think if we're, if we're making sure we're refreshing things on that three-month cadence, and then we're always updating.

**Bailey Seybolt:** But I think that's all the good signals that, you know, Google needs.

**Azzam Aijazi:** Cool.

**Bailey Seybolt:** Okay, that was it for me.

**Bailey Seybolt:** Was there anything else you all wanted to touch base about today?

**Azzam Aijazi:** No.

**Steve Krenzel (Seattle):** Good.

**Steve Krenzel (Seattle):** good.

**Azzam Aijazi:** Yeah, looking forward to seeing the articles with the version, I don't know, 3.0 or so.

**Bailey Seybolt:** I know what version we're at now.

**Azzam Aijazi:** I'm excited to see them.

**Bailey Seybolt:** Yeah, so we will get those to you tomorrow.

**Azzam Aijazi:** Okay, cool.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** All right.

**Azzam Aijazi:** Thank you both.

**Steve Krenzel (Seattle):** Thank you.

**Azzam Aijazi:** Thank you, Bailey.

**Bailey Seybolt:** Bye.
