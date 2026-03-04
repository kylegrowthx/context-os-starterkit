# Lightsource <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-30
time: 18:00 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Spencer Penn, Ben Hoehn, Aida Knezevic, Erik O'Brien (GrowthX)
fathom_recording_id: 98109642
fathom_url: https://fathom.video/calls/458181545
share_url: https://fathom.video/share/qgJw4tWbKdv6nYy3xY4YZYsLcwssxZpY
source: fathom
enriched_on: 2026-03-02 15:30 UTC
speaker_note: Sydney Go (GrowthX) was on vacation and did not attend. Sam Tearle (LightSource) was on the calendar but does not appear to have spoken during the meeting.
</metadata>

---

## Summary

GrowthX and LightSource reviewed progress on 11 SEO articles and finalized strategy around AI-generated content: accepting volume-based, "good enough" material for topical authority rather than polished thought leadership. Spencer approved the Calibration article V2 for publication and gave detailed feedback on enhancing generic content with specific case studies (e.g., Toyota's TPS system). The team addressed a critical image quality blocker by committing to a "code-gen" workflow using LLMs to output diagram code (e.g., Sankey diagrams) for deterministic graphics instead of relying on AI image generation hallucinations.

---

## Context

LightSource is a GrowthX content client running a major content initiative around sustainable supply chain management. GrowthX is producing 11 SEO-focused articles (with glossary entries) targeting topical authority in procurement, supplier risk, and AI applications. This is a weekly sync between Spencer Penn (LightSource), Ben Hoehn (LightSource), and the GrowthX team (Aida Knezevic, Erik O'Brien). The meeting happened to align content strategy with editorial reality: Spencer wanted to understand whether the team could deliver polished, case-study-rich thought leadership, but the discussion clarified that the goal is to publish volume-driven SEO content quickly and iterate based on traffic signals rather than aim for perfection on the first pass.

---

## Relevance

**To GrowthX Delivery:**
- Defined clear editorial bar: volume-driven, SEO-optimized, "good enough to publish" vs. highly curated thought leadership (which will remain separate for sales enablement)
- Established image generation workflow shift from direct AI image generation (prone to hallucinations) to "code-gen" approach (LLM → diagram code → deterministic builder like Sankeymatic)
- Identified blocker on hex color accuracy in AI-generated graphics; workaround is manual picker tool verification or designer post-processing
- 11 articles in production: 1 (Calibration V2) approved, 3 in Ben's review, 5 in editing (share by EOW)

**To CheckThat:**
- Spencer's interest in procedural diagram generation and code-based image creation aligns with deterministic, data-driven content workflows (potential AEO signal)
- Discussion of LLM fact-checking workflow shows client is aware of hallucination risk in AI content

**To GrowthX Business Development:**
- LightSource is moving fast on content production despite editorial quality concerns; good expansion signal if they're satisfied with volume approach
- Glossary and Looker dashboard blockers (GSC/GA4 access, designer return) are non-critical but tracking items for account health
- Spencer's detailed feedback and iterative approach indicates engaged stakeholder and room for refinement conversations post-launch

---

## Overview

- **Content Strategy:** The goal is to publish SEO-focused articles for topical authority, accepting they are "good enough" for web traffic but not polished thought leadership pieces for sales.
- **Image Quality:** AI-generated images are failing on two fronts: incorrect brand colors and generic visuals. The solution is to manually verify hex codes and use a "code-gen" workflow for data-driven graphics.
- **Article Feedback:** The "Calibration" article's V2 is approved for publication. Feedback includes adding more specific, digested case studies (e.g., Toyota's TPS system) and using procedural tables for visual breaks.
- **Blocker:** The Looker dashboard is on hold pending GSC/GA4 access from LightSource IT.

---

## Key Topics

### Content Review & Strategy

  - **Article Status:**
      - **Approved:** "Calibration" V2 is approved for publication.
      - **In Review:** Ben is reviewing "Supplier Risk Management" and two others.
      - **In Production:** Five new articles are in editing and will be shared by EOW.
  - **Content Strategy:**
      - **Goal:** Publish SEO-focused articles to build topical authority and drive web traffic.
      - **Rationale:** This volume-based approach is distinct from highly curated, sales-enablement thought leadership.
      - **Outcome:** Spencer approved this strategy, prioritizing launch and iteration over initial perfection.

### Image Generation & Quality

  - **Problem:** AI-generated images are failing on two key metrics:
      - **Brand Colors:** Incorrect hex codes for LightSource orange.
      - **Visuals:** Generic, abstract graphics that don't represent article content.
  - **Solution:**
      - **Brand Colors:** Manually verify hex codes with a picker tool post-generation.
      - **Visuals:** Adopt a "code-gen" workflow for data-driven graphics.
          - **Process:** LLM outputs code → Code feeds into a diagram builder (e.g., Sankeymatic) → Builder creates a deterministic image.
          - **Rationale:** This avoids the "hallucinations" of direct image generation, which often produces nonsensical text.

### Glossary & Blockers

  - **Glossary:**
      - **Status:** Topics approved.
      - **Next Step:** Sydney (GrowthX) to create description mockups upon return from vacation.
  - **Blockers:**
      - **Image Approvals:** On hold until the LightSource designer returns (next week).
      - **Looker Dashboard:** On hold pending GSC/GA4 access from LightSource IT.

---

## Action Items

**Ben Hoehn**
- Send article doc to Spencer for thumbs-up

**Aida Knezevic**
- Share 5 edited articles w/ Ben & Spencer by Oct 31
- Enforce LightSource orange hex; use picker; no upload if off-brand
- Stage Calibration blog w/ placeholder featured image; publish when approved
- Discuss procedural diagram workflow w/ Sydney; propose approach to Spencer
- Ping LightSource IT re: GSC/GA4 access; set up Looker when granted

---

## Transcript

**Ben Hoehn:** Just got the weekly sync notes. I was on with Spencer before, and he said he had to jump. Let me see what that looks like on his count. Yeah, I'm thinking he should be over soon.

**Aida Knezevic:** Yeah, Sydney is out this week.

**Aida Knezevic:** She's on vacation.

**Aida Knezevic:** So she's unable to join the call, but she's going to be back next week and give you updates on the glossary as well.

**Ben Hoehn:** I know that you went through and approved a bunch of topics. I read through the revision on the first article and was good with it. I just wanted to see if Spencer had a chance to go through. Our designer is also out this week and next, so we won't be able to get approval on imagery until he's back. What I'll do is just send over the doc and see if we can get a thumbs up. I'm still in the middle of reviewing Supplier Risk Management and the other two docs as well. However, with these first few articles, I think it's going to take us a while to get them out, because Spencer wants to really get the use case and the technical content accurate.

**Ben Hoehn:** Okay, so walk me through then just what is kind of in the pipe. Let me know how the glossary is going, too.

**Aida Knezevic:** For the glossary, once Sydney is back from vacation, she can mock up some examples for you of how the descriptions would look like. The blogs are longer, and the glossary would be shorter, but not just a paragraph—it would be a substantial amount of content. So to give you an update on what's in production, we are working on five articles right now. They are currently being edited by an editor, so I think we'll start sharing those by the end of the week. Katya updated the image generation pipeline based on the conversation with your designer. For featured images, they look like graphics now with lots of options.

**Ben Hoehn:** Yeah, we just want to make sure that the LightSource orange is on brand.

**Ben Hoehn:** seeing, like, a few different variants of it.

**Ben Hoehn:** Maybe it's just my monitor picking up Zoom, but.

**Aida Knezevic:** No, no, I think it's, yeah, this one is, like, a little more blood orange, and this one is, like, orange, orange.

**Aida Knezevic:** So, yeah, I do think there are some differences there.

**Erik O'Brien:** Yeah, and that's one thing I was talking to one of our engineers about—getting the exact hex colors is pretty difficult to remain consistent. Yeah, for some reason, when we generate, it just won't listen to the instructions to stick on brand with the hex colors.

**Erik O'Brien:** So I think we can be at least selective of which ones we go after that are closest aligned to LightSource's true orange.

**Ben Hoehn:** Yeah, it's really important for us that these are the new brand colors.

**Ben Hoehn:** So what I would say is, you know, let's not even upload images that don't have them.

**Ben Hoehn:** Maybe we just use a picker tool after it's generated to double check or, you know, manually have a designer go in and revise it.

**Ben Hoehn:** What tool are you guys using for this?

**Spencer Penn:** Yeah, go ahead.

**Spencer Penn:** I was going to ask, like, what process you guys are using and, like, is there any way to go away from it being, like, a sort of, like, graphic and more towards something that, like, describes the, with the content of the article?

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So from what I know from Katya, and this is a very high-level description, so she uses GPT-5 to generate these.

**Aida Knezevic:** She will use, like, she has a very detailed prompt that's part of the generation.

**Aida Knezevic:** And I'm not sure where the, like, precisely, like, where the colors come in and the brand elements, but that's also a factor.

**Aida Knezevic:** It is possible to change these so that I think they're more related to the actual content of the article.

**Aida Knezevic:** I think these are, yeah, this one is also related to an article, but I think we can ask Katya to kind of go back in and make sure that these are a little closer to the topic at hand.

**Spencer Penn:** These are not going to be header images, right? They're going to be in the body, dispersed throughout the article. Because I think we want something that's a little bit higher resolution or maybe more specific for the header and also like wide format, not square, you know?

**Aida Knezevic:** Yeah, so we can change the format. That's very easy to adjust. The featured images are going to be more like this. Some of our clients go with header images that have the title of the article with a text overlay, which is also something we can do.

**Spencer Penn:** I mean, I'm okay if it's procedural to some degree, but I just want to make sure it looks good. Maybe the article title or something would be a good incorporation.

**Ben Hoehn:** Oh, did you guys see Aida's comments in the Slack?

**Spencer Penn:** Yeah, like last week. I had given detailed feedback on an example article that got sent to us. I felt it was a little bit lacking. I provided feedback on things that I liked in our version, including the way that the graphics are used throughout the article. I think that would radically improve it from more like a C minus to at least like a B plus or A minus.

**Aida Knezevic:** Yes, we did see the infographics that you shared. That level of detail right now is impossible with AI. So we can generate more abstract infographics, which is something Katya experimented with. Spencer, did you get the chance to take a look at the second version of the Calibration article? That's the draft V2.

**Erik O'Brien:** It's going to look a little weird because you're on dark mode.

**Spencer Penn:** Okay, cool. This is helpful. I like this. This is a great graphic, and obviously something that you made. So is there a way to get these consistently in future articles, something like this? I like this table. Are you guys procedurally creating this table?

**Aida Knezevic:** With AI, no. These would have to be created manually. We'd have to discuss that with Andy to see if that's something we could add in.

**Spencer Penn:** I think this is interesting because it's different than a block of text that can be added to the article. I don't believe there was a table in the last one, right?

**Aida Knezevic:** No, the section was more bullet points or H3s. It's a visual break, which is good.

**Spencer Penn:** Yeah, I agree. Here it starts to feel a little bit generic. There's a little bit of redundancy here.

**Spencer Penn:** So procurement challenges, direct material challenges, indirect challenges, strategies. I like the idea of including examples, but these should be more like case studies. Instead of just here's a link to Toyota, I would say more like: Toyota is famous for their TPS production system—a way of working that includes supplier collaboration. In 1980, they pioneered this and found they were struggling with problem X, implemented solution Y, and were able to reduce their line stoppages by 30%. Something like that could be digested from other articles or case studies online. That feels more interesting because it shows the actual interesting elements and the outcomes. Overall, I think this is a reasonably good article. The question is, where should we be setting the bar? If somebody came to me and said, "I used AI to produce this," I'd be like, hell yeah. If someone said they wrote this themselves, I might say there's things that could be done better. But I'm not sure where the bar should be for us.

**Aida Knezevic:** No, I think we want to get to a point where you're happy with the voice and the tone. Human-generated content from experts is always going to be harder for AI to emulate, because you have vast experience you can pull from and AI is more generic. But that doesn't mean we can't improve it over time as you give us feedback. For us, the question is: is this good enough to publish and start collecting signals—clicks, impressions—so we can see what's working and driving traffic to your site. The SEO content we create is good at getting clients visibility in LLMs and organic search. So it's going to improve over time, but right now we want to get it to a spot where you're happy to push it to the website.

**Spencer Penn:** Yeah. Is this a place where I would be okay to push it to the website? It's good enough that I wouldn't be upset to have it on the website, and I believe it could be good for SEO. But I wouldn't say it's a content piece that I'm proud to mail to people that we're talking to, you know what I mean?

**Aida Knezevic:** Yeah, I get it.

**Spencer Penn:** That might not be the right metric. Maybe those have to be very highly curated, crafted thought leadership pieces that we enable our sales reps with. But this might just serve a different purpose—get people to the site. I'm okay with that. And we can keep iterating. I'd rather just launch and then fix.

**Aida Knezevic:** Yeah, exactly. We're on the same page. With the content that we do create, some of it is really about building topical authority. Some of it you can't exactly send to a prospect because they already know those things. But at the same time, the content helps you build topical authority. So you do want it on your site. I think in the future we'll create content that's more niche and talks about topics that would be really interesting to the people you're talking to.

**Spencer Penn:** But we'd want to establish a nice foundation first.

**Aida Knezevic:** Yeah, I finally found the last image-gen pipeline that Katya created for infographics. Here's what they look like right now.

**Ben Hoehn:** These are less full infographics and more just stat graphics to me.

**Aida Knezevic:** Exactly.

**Spencer Penn:** I think there's a way to do this better. It has to be a multi-step process. First, something ingests the article and creates three ideas for graphics that could be included. Then you pick which of these three ideas is the best, describe the graphic, and compile it down to code and an image generation tool. If you just ask ChatGPT to make a graphic, it won't spell words right. But something that procedurally creates the graphic would be more interesting. I like these as small in-body images, but the issue is that they're not representing the article content. For example, "10x margin impact" is meaningless—what does that even mean?

I'll give you an example of something I've done: a Sankey diagram. There's a thing called Sankeymatic that shows stuff going in and stuff going out. I feed ChatGPT an example of Sankeymatic code and say, "Now make this for Apple's income statement." ChatGPT generates the code, I paste it in, and boom—there's the income statement for Apple as a chart showing iPhone, Mac, iPad, accessories. Perfect sense.

I'm not saying you guys should make Sankey diagrams specifically, but I bet there are platforms for making diagrams where they expose a procedural way. Can we use LLMs to create the code that then generates a chart? The nice thing is it's actually putting text in the chart, not trying to generate an image with text hallucinations.


**Ben Hoehn:** Spencer, I'm fine with those infographics being used as supplementary images to call out specific stats.

**Spencer Penn:** Yeah, I'm okay with it too. If it's calling out specific statistics.

**Ben Hoehn:** In this way, we're not trying to over-engineer a blog post with perfect infographics. We can do that later.

**Aida Knezevic:** When we stage the Calibration article, we can pick a featured image—pick a couple that feel like the best of the bunch—and just use that as a placeholder. Once your designer is back in office, they can give additional feedback. We just want to get content live on the site.

**Ben Hoehn:** Absolutely. Okay, so there are three articles from last week that we have to review?

**Aida Knezevic:** Yes, there are three from last week, and I think you reviewed one.

**Spencer Penn:** Thanks, guys.

**Ben Hoehn:** I do have someone visiting the office that I need to receive. So to recap, we have three articles to review: How AI Transforms Sustainable Supply Chains, What is Direct Procurement, and What is Supplier Risk Management.

**Aida Knezevic:** Yeah, exactly. We still need GSC and GA4 access from LightSource IT. I know you filed a ticket for the IT team. As soon as we get that, we'll set up the Looker dashboard. I'll ping them again.

**Ben Hoehn:** Team, thanks so much for the sync.

**Erik O'Brien:** Talk soon.

**Aida Knezevic:** Thank you. See you next week.

**Ben Hoehn:** Bye.
