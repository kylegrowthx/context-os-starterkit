# ✨ Paul and Daniel Lopes

<metadata>
date: 2025-03-13
time: 20:01 UTC
duration: 61 minutes
organizer: andrej@growthxlabs.com
participants: Daniel Lopes (GrowthX), Paul Bratslavsky (Strapi), Victor Coisne (Strapi)
fathom_recording_id: 51844437
fathom_url: https://fathom.video/calls/252197107
share_url: https://fathom.video/share/xvZSZXmKmeqX7ZYqyqEGQcHx1X22vysx
source: fathom
enriched_on: 2026-03-04 12:15 UTC
</metadata>

---

## Summary

GrowthX and Strapi reviewed the current AI-powered content generation workflow, identifying several improvements to strengthen the process: implementing URL blacklisting to exclude specific sources, adding structured context fields to guide article creation, and exploring third-party integrations like Kappa AI for fact-checking and Recraft for image generation. The team discussed near-term wins (adding an "Additional Context" column to Strapi's Airtable) and longer-term initiatives (content internationalization leveraging a new engineer with ClickUp experience, and ingesting video transcripts as knowledge sources).

---

## Context

Strapi is a headless CMS company engaged with GrowthX on a content marketing engagement. Paul Bratslavsky heads Strapi's marketing and developer advocacy team, which produces both external blog content (for SEO and traffic) and internal technical documentation. Victor Coisne is the marketing director overseeing the content team. This call continues a previous session with Andrej Vidovic to dive deeper into GrowthX's content generation process — moving beyond a high-level overview to discuss technical implementation details, customization options, and integration opportunities.

Daniel Lopes led the discussion, walking through the multi-step workflow (keyword analysis, brief generation, research, outline, draft, post-processing) and explaining how AirOps serves as a UI over GrowthX's custom APIs. The conversation revealed that Strapi wants more control over research sources and greater flexibility in how article context is specified, both of which GrowthX can already support or is actively building.

---

## Relevance

**To GrowthX Delivery:**
- URL blacklisting is now a supported capability — Strapi can exclude specific domains or URL patterns from research (e.g., excluding older Strapi articles or GrowthX-generated content)
- Extending the "Additional Context" field in client Airtables is a quick win that improves brief quality without major engineering effort
- The workflow is built on custom APIs over AirOps, giving GrowthX flexibility to add features (Kappa AI integration, video transcript ingestion) without vendor lock-in
- Strapi plans to move from Airtable to an internal platform, which presents an integration opportunity for GrowthX

**To CheckThat:**
- No direct AI visibility or AEO discussion in this call, but the content generation process is foundational to Strapi's SEO strategy
- As Strapi expands to multiple languages (planned internationalization project), CheckThat could provide insights into how Strapi's branded content appears in AI visibility across different markets

**To GrowthX Business Development:**
- Account health positive: Strapi is investing in deeper integration of GrowthX's workflow and asking for more advanced features (Kappa, video ingestion, internationalization)
- Expansion opportunity: The planned localization/translation project (11+ languages) could justify a scope increase or new SOW
- Reference potential: Strapi's multi-language content strategy and AI-powered workflow is a compelling case study for international B2B companies

---

## Overview

- GrowthX will implement blacklisting for specific URLs to exclude certain content from research and internal linking
- The research process will be updated to allow input of specific resource URLs for each article
- Integration with Kappa AI for fact-checking is planned to improve content accuracy
- Image generation capabilities will be explored, with Strapi providing style guidelines
- Future plans include developing a localization workflow and ingesting video content as knowledge sources

---

## Key Topics

### Current Content Generation Process

  - Uses AirOps for workflow management and custom APIs for content generation
  - Process includes: assignment brief creation, keyword analysis, research, outline generation, draft writing, and post-processing
  - Recently switched from OpenAI to Claude 3.7 for improved writing quality
  - Fact-checking currently uses AirOps agents, but integration with Kappa AI is planned

### Improvements to Research and Sources

  - Will implement URL blacklisting to exclude specific content (e.g., older Strapi articles, GrowthX-generated content)
  - Updating researcher to accept specific resource URLs for each article
  - Exploring integration of video transcripts and podcasts as knowledge sources
  - Planning to develop an internal/external knowledge base system for more efficient research

### Content Customization and Context

  - Added field for user context to provide more specific audience information for each article
  - Strapi team can add additional context and resource links in Airtable to guide content creation
  - GrowthX is developing an internal platform to replace AirTable and AirOps for better workflow visibility

### Image Generation

  - GrowthX uses Recraft AI for image generation with customizable styles
  - Strapi to provide style guidelines and example images for developer-friendly illustrations
  - Will explore adding image generation to the content creation process

### Localization and Translation

  - GrowthX has experience with Spanish and Portuguese localization
  - Proposed starting with a one-page overview of Strapi in multiple languages as a test
  - Discussing potential for developing a Strapi plugin for AI-powered content internationalization

---

## Action Items

**Daniel Lopes (GrowthX)**
- Implement blacklisting for internal linking + specific URLs in content generation process
- Investigate integration of Kappa AI for fact-checking in content generation workflow
- Research feasibility of content internationalization project with new engineer from ClickUp

**Paul Bratslavsky (Strapi)**
- Send Daniel exact URL structure for excluding GrowthX articles from research (e.g., strapi.io/ecosystem)

**Victor Coisne (Strapi)**
- Provide 5-10 sample images matching Strapi's desired AI image generation style to Daniel
- Add 'Additional Context' column in Strapi's Airtable for GrowthX article briefs

---

## Transcript
**Paul Bratslavsky:** Questions that I may have and if it's possible to record this for other teammates, they'll be amazing if possible Yeah, let me just make sure I'm recording Yeah, there we are Nice.

**Daniel Lopes:** Okay, sounds good.

**Daniel Lopes:** Maybe we wait a few minutes for Victor while we're waiting.

**Daniel Lopes:** I'm Running some of the things here in background.

**Daniel Lopes:** So if you see me looking around, that's why no worries I'm taking off some of the workflows for strategy Be able to show everything.

**Daniel Lopes:** Yeah, no worries Where are you baseball?

**Paul Bratslavsky:** I'm Typically, I'm in Texas.

**Paul Bratslavsky:** So I'm not too far from Austin But now I travel to Connecticut to visit my family.

**Paul Bratslavsky:** So in the States Oh, nice.

**Daniel Lopes:** Yeah, nice and remind me again, like the the team structure and how you guys and Like which part of the the process are you only and Yes

**Paul Bratslavsky:** I'm on the marketing team, so like Victor is the head manager who tells everybody what to do, which is important, it gives us keeps us busy, and then as part of our developer advocacy, have a content team where part of we write internal articles and to kind of help out with that, this is where Andrej comes in with everything that you guys do to kind of create AI generated content.

**Paul Bratslavsky:** And for us, we basically try to split our time between, you know, working with GrowthX and making sure that we're publishing content that helps us get improvements in our SEO and drive traffic to a website.

**Paul Bratslavsky:** then we work on internal content, which is like very specific, maybe code heavy, very technical content that, you know, make sense for us to write.

**Paul Bratslavsky:** right.

**Paul Bratslavsky:** That makes sense.

**Daniel Lopes:** See if everything is running here.

**Daniel Lopes:** I was just kicking off a few generations, and then we can use it as an example.

**Paul Bratslavsky:** Yeah, let me just think, like, just to double check if you could let me know if he's going to be able to come in.

**Paul Bratslavsky:** Yeah, I'm happy to answer anything offline as well if he can it.

**Daniel Lopes:** Yeah, always.

**Daniel Lopes:** We can record and summarize and send it to him.

**Daniel Lopes:** Yeah, I have so many note, so many note taker that I don't know why I have like four.

**Daniel Lopes:** And they're all white.

**Daniel Lopes:** Yeah, I can always do it with my browser extension.

**Paul Bratslavsky:** I just know everybody that has kids, there's always something that comes up at some point.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Most people on the team have kids, and I'm the only one from my team without kids. It's always something that comes up.

**Daniel Lopes:** Yeah, yeah.

**Paul Bratslavsky:** It's funny.

**Paul Bratslavsky:** I started, you know, young when I had my daughters, but now for me, she's like out of the house.

**Paul Bratslavsky:** So I'm like, yeah, freedom.

**Daniel Lopes:** I think I have everything done for one article a couple more steps but yeah like if you want to start I can just walk you through everything and then yeah yeah whatever you prefer yeah I guess we could just start because I want to be mindful of your time as well and if he joins in he joins in if not they'll share the notes with him and like you said if he has any follow-up questions he could ask you in Slack.

**Daniel Lopes:** Sounds good yeah I don't know like have you ever had a have we ever showed you like the process and how we how we work or?

**Paul Bratslavsky:** Andrej showed us like the very high-level process from GrowthX but very big picture overview. But I just want to get more of that technical detail, kind of

**Paul Bratslavsky:** like where the search is getting pulled from, what sources are we using, one of the things I think would be helpful for us is if we could automate a process to either point to a knowledge base that already exists as Strapi or have a way to review the sources and maybe even have an option to opt out of certain sources, I don't know if that's like is the case at the moment but just to have us a little bit more control.

**Daniel Lopes:** Yeah, yeah, okay, let me walk you to how the process works now and I think some of the things you said we can already do.

**Daniel Lopes:** Okay.

**Daniel Lopes:** so like I'm always using this, like we use air ops as the grid but with like all of our flows are using our own APIs.

**Daniel Lopes:** we use air ops just as like a UI.

**Daniel Lopes:** So I'm testing, I was testing things on this like 283, this last row, and so we have a company about like this we should

**Daniel Lopes:** It could expand and be more detailed — describing what the company does, who your target users are, what personas you're targeting. If you have a specific article, like one for e-commerce, you could expand that section just for e-commerce users. Or if you're targeting executives making e-commerce decisions, versus developers looking for headless CMS integrations, you'd customize that too. Right now we use a standard two paragraphs, but it's fully customizable and influences the assignment brief.

**Daniel Lopes:** So the first step we do is an assignment brief, and the assignment brief looks like this.

**Daniel Lopes:** We changed it yesterday, so now it will do more than what we were doing before, before it was going similar.

**Daniel Lopes:** But before I was doing it, let me show you before.

**Daniel Lopes:** Before we didn't have the competitor URLs and the links that they're comparing things against, we didn't have like the scoring of the competitors who had just like one competitor.

**Daniel Lopes:** But now we added two way, we added a bunch of top-tier organic results and suggested type of article, the search volume of the primary keyword, and we're adding more to this, so that's something we're improving right now.

**Daniel Lopes:** But the brief will be essentially which content we're competing against, what kind of points we wanna make, so we can customize here, it can change everything we want here.

**Daniel Lopes:** And we have brought you to the content, what are you considering about the users?

**Daniel Lopes:** So a lot of this was pulled from the context, but also from the content when it was going through the research of generating the brief.

**Daniel Lopes:** And the research for the brief is this process that I can show you.

**Daniel Lopes:** So the brief starts as like the guideline.

**Daniel Lopes:** for the whole process and we'll go down to like generate a new a research using u.con and replace u.con to perplexity sonar, perplexive pro, which is pretty much the same as OpenAI research.

**Daniel Lopes:** So we're replacing this week actually.

**Daniel Lopes:** u.con is pretty good but we don't use their answers.

**Daniel Lopes:** use the sources that they use and we scrape the sources and we're going to change it.

**Daniel Lopes:** I can show you that the next step.

**Daniel Lopes:** the first thing we do is the brief.

**Daniel Lopes:** Let me get here the sec.

**Daniel Lopes:** I had this one.

**Daniel Lopes:** So the brief when we click that button what's happening makes an API call to our back end our back end will receive this.

**Daniel Lopes:** So it's only receiving the topic that had less commerce platforms that was the topic that we had in the first call of the grid.

**Daniel Lopes:** And then the first sale of the role 283 receiving the company as active summary and receiving a duplicate of the same content as the user context.

**Daniel Lopes:** So we can

**Daniel Lopes:** at another cell, there would be more detail about the target person for this content.

**Paul Bratslavsky:** Yeah, I quickly wanted to add, like you mentioned before, like if we wanted to have like a quick low hanging fruit win is maybe for every blog post, we give a little bit more context at this piece to kind of guide the creation of the brief.

**Paul Bratslavsky:** Yeah, that would probably be like a good approach to play around with.

**Paul Bratslavsky:** Yes, it would.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like, for example, that I can even add here already to the, so make sure I don't forget, but one column that we're not using, don't know if you saw that in the input, we have company executive summary, we have user context and we're just duplicating the user context as the executive summary.

**Daniel Lopes:** So yeah, user context, I'm going to put it next to the to this and we can map in the workflow input, we can map the user.

**Daniel Lopes:** context to that specific parameter.

**Daniel Lopes:** So move forward, we can say, we can describe here, we want to target with this article, and that will do a better job.

**Daniel Lopes:** this is what I was talking about.

**Daniel Lopes:** We're duplicating.

**Daniel Lopes:** And then the first thing we do is to validate and analyze the keywords, let me go back one second.

**Daniel Lopes:** So we go like, essentially search this, on Google, find all the top performing URLs, and then we hit the top performing URL, and we do a keyword analysis on that.

**Daniel Lopes:** So we get like, what are the top performing keywords, and we check if these keywords are relevant to your ICP into that user context or not.

**Daniel Lopes:** If it does, in this case, will be because we're doing it manually.

**Daniel Lopes:** So sometimes we don't do manually, then we have a relevance check.

**Daniel Lopes:** But, and then we fetch the top performing organic results.

**Daniel Lopes:** And we look at why they're performing.

**Daniel Lopes:** And then we read the articles.

**Daniel Lopes:** We read the top performing ones, clean it up, and then we combine with the points of the brief that we think could be like competitive advantage for an article that would not try to out-compete those top three.

**Daniel Lopes:** We're improving this, so the people change quite a bit.

**Daniel Lopes:** like we're just to give you an idea.

**Daniel Lopes:** Like this is one of the things that we noticed that the more effort we put in the brief, the better the whole process will be.

**Daniel Lopes:** So we have the EP, one of our engineers working on that today, actually.

**Daniel Lopes:** And the brief will look like this.

**Daniel Lopes:** We have the target audience will be more detailed.

**Daniel Lopes:** We're gonna have the primary keywords and secondary keywords.

**Daniel Lopes:** I'll show you the top two pages we already have.

**Daniel Lopes:** And then we're gonna have suggestions for SEO metadata and snippets.

**Daniel Lopes:** also going to go much deeper into the kind of topics we want to cover.

**Daniel Lopes:** So, like, so we're extending our brief to look like this word document.

**Daniel Lopes:** A request came from Reddit, but applies to everybody.

**Daniel Lopes:** So we've been doing this manually for Reddit, and now we're going to apply that to everyone.

**Daniel Lopes:** Hopefully, by the end of this week, we have most of this ready.

**Daniel Lopes:** Right now, the brief looks like this, so that the brief that you just saw was, let me open up again.

**Daniel Lopes:** We have this, so we're going to extend it to be more detailed, and extend the content strategy to be more of like the full content.

**Daniel Lopes:** At this point, like, if we also wanted to customize this, we could customize here as well, and like change whatever you want, change the entire brief to be like, however you want, and be like, what kind of topics you want to cover.

**Daniel Lopes:** And what will happen is the next step, we have a researcher that will receive the brief.

**Daniel Lopes:** So this is the next column here.

**Daniel Lopes:** The researcher receives the input — the brief and context, which includes the company summary. We break down the brief into topics we need to research, essentially running deep research on 10-20 research questions. We store the results and the sources that are used for that research.

**Daniel Lopes:** So we've vectorized, we clean up the source, like we scraped the source, vector, clean it up, and then vectorized it in VBA, and we add like some semantic chunking.

**Daniel Lopes:** Like we go like each section of the article, we extract and add why we think that is relevant to the article, so we can look that up from the vector database.

**Daniel Lopes:** The main thing we're thinking now as well is that instead of just doing the sources, we're also going to have the buttons to switch to perplexity, and see if we can store the whole result of deep research.

**Daniel Lopes:** It's their result of like, it will take minutes to run, but their result is as good as open AI, and it's like this really long article, it will be better, many times it will be better than skipping all the URLs and trying to vectorize them.

**Daniel Lopes:** So I think this will be a significant change, some of the things that you're concerned about.

**Daniel Lopes:** One thing we support already, that we're not using,

**Daniel Lopes:** here is black listing URLs.

**Daniel Lopes:** So one of the steps that I'll show you, sorry, I have so many tabs of ours looking into this.

**Daniel Lopes:** So as we searched for sources, one step that we do is just check if we have any domain that is black listed.

**Daniel Lopes:** If it is black list, we'll remove from the research.

**Daniel Lopes:** So, but we are not using it in your game, so we can I have an interesting question for you.

**Paul Bratslavsky:** So because we're creating a lot of, like, content with GrowthX, and we also have our internal content, our traffic.a website is becoming something that is being searched.

**Paul Bratslavsky:** some of these previous articles that we've written are coming up as resources.

**Paul Bratslavsky:** And so I think it would be nice if we could kind of exclude, let's say, previously written GrowthX articles or articles that we feel may not make sense for us to use.

**Paul Bratslavsky:** as data, we would like to exclude it.

**Paul Bratslavsky:** So do you do that, like, just the domain, or are you able to, like, Strapi slash, let's say, you know, we had slash ecosystem, which has only GrowthX articles in it.

**Paul Bratslavsky:** And can we like exclude just that portion?

**Paul Bratslavsky:** So you still get access to our internally written blog posts that may be relevant for what GrowthX does.

**Paul Bratslavsky:** But at the same time, it omits GrowthX articles that were written to be a screen.

**Paul Bratslavsky:** Yeah, we can do that.

**Daniel Lopes:** We can do that.

**Daniel Lopes:** It's just adding this call.

**Daniel Lopes:** then we can just type it here, this URL is spaced with common.

**Daniel Lopes:** So if you send us the, so is this Strapi slash ecosystem?

**Daniel Lopes:** That's the, I'll have to use that as an example.

**Daniel Lopes:** But I'll find out what Sarah and I'll put it in Slack.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** we can totally put that here.

**Paul Bratslavsky:** And then we will not scrape that and we're not going to store in the vector database.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Let me just write that down to make sure the blacklist works. I can use your case as a test case for blacklisting this domain or URLs. So the next step, we get all the URLs and then process the relevant ones. Not all of them are relevant, but the ones that are relevant to the research question get vectorized and stored in the database.

**Daniel Lopes:** That's another system we're building.

**Daniel Lopes:** Actually, hiring people can build the whole thing.

**Daniel Lopes:** We want to have a system that will be, that retain the research as well, for the stuff that you write about over and over, or for stuff that you give us.

**Daniel Lopes:** Like the example you're talking about, I think, was kappa.ai.

**Daniel Lopes:** Ideally, you would be getting all of your data from kappa and putting in this shared knowledge base we have.

**Daniel Lopes:** So we have some of that, but like some of it is still like inside of not great.

**Paul Bratslavsky:** we're moving to our own system.

**Daniel Lopes:** So we're going to have like both external and internal sources.

**Daniel Lopes:** And we're we're architecting and building that already.

**Daniel Lopes:** I think the engineer that will work on this start next week.

**Daniel Lopes:** So we're little bit behind on the face that I wanted for that.

**Daniel Lopes:** So right now we do like every topic here, we'll do its own research, store, and we have like a giant amount of stuff on, on with the eight and it's getting used just for that article.

**Daniel Lopes:** So like we.

**Daniel Lopes:** You need every every couple of weeks we clear that research and so we are doing the research deleting.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's like spending a ton of resource.

**Daniel Lopes:** So then we do the research and then we do the title generation.

**Daniel Lopes:** The title generation is optional like you could just type the title if you want, but it has a workflow that checks for SEO and competitors do a Google on that topic and see like what's the what are the titles that are doing well and come up with like five titles and you can choose from the human review.

**Daniel Lopes:** So I came up with like this four titles and I chose that in this process and then the first year you can just edit and the title will be applied into the other parts.

**Daniel Lopes:** But then from the from the combination of the brief and the stuff that we have in the database we have the outline generation.

**Daniel Lopes:** The outline generation is super important.

**Daniel Lopes:** So when I click on this what we'll do is

**Daniel Lopes:** this.

**Daniel Lopes:** Let me see here where I have the outline.

**Daniel Lopes:** So we will receive as an input on whole brief.

**Daniel Lopes:** And then we'll go, like, come up with what are the search queries based on that brief that we need to look up in our vector database.

**Daniel Lopes:** And for each one of these, if we don't find enough results from the database, we'll do a perplexity deep research to find the alternative.

**Daniel Lopes:** So we're doing this fall back.

**Daniel Lopes:** So if the initial research didn't enough or didn't store enough, then we do a deep research on that topic.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** So like the research you're manually scraping that content, and they're not enough of it, then you're doing like the backup of using perplexity.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** That will happen at the sorry.

**Daniel Lopes:** Oh, no, wait.

**Paul Bratslavsky:** Yep.

**Daniel Lopes:** So like that will happen at the generation of the draft.

**Daniel Lopes:** So at the line, we're just like, can we have a good one?

**Daniel Lopes:** stuff and try to generate an outline, and then we'll do the deep research at the generation of the draft.

**Daniel Lopes:** So in this case, it came up with these questions, and then it received the brief and all the questions, and then we run the execution of them in parallel, and then we come up with an XML at the end that has the brief.

**Daniel Lopes:** So it has the outline.

**Daniel Lopes:** Let me just open this in a different thing that's easier for you guys to read, and look for a map that's actually about the previous format, because it has all the escaping.

**Daniel Lopes:** I think it can just open in Arabs, going to be easier to read.

**Daniel Lopes:** So in this case, for example, let me switch this to Markdown.

**Daniel Lopes:** Let me see can see it, and let me switch to code.

**Daniel Lopes:** So the outline...

**Daniel Lopes:** you switch to full screen and switch back to cold.

**Daniel Lopes:** So the outline is an XML that has the sections that we will generate.

**Daniel Lopes:** the section, it's like a bunch of h2s with jh3s as the subtopics, and we have a rough number of word count, and we have the subtopics.

**Daniel Lopes:** So this is another opportunity where you could just remove sections, create new sections here, delete the subtopics, add new ones.

**Daniel Lopes:** And one thing we do is we usually have pretty high word count, and we can make it shorter.

**Daniel Lopes:** But one thing that we learn is that it's better to generate a ton, and then at the end of the process, you have a step to make it shorter.

**Daniel Lopes:** you have more better data to make it shorter, and the last chance of hallucinating.

**Daniel Lopes:** So yeah, so that's the outline.

**Daniel Lopes:** This is a great place to customize a ton and make the quality of the

**Daniel Lopes:** And then once you run that, what we'll do is let me open the draft.

**Daniel Lopes:** So this is the draft, so this is the next step, one second just.

**Daniel Lopes:** So we would hit play here and it will take the outline, the title, and we'll do this.

**Daniel Lopes:** So just do a cleanup on the XML in case like we didn't close a tag or something like this.

**Daniel Lopes:** And then we, for each one of the sections, so then we split all the sections, and we process each one of them in parallel.

**Daniel Lopes:** So if the article has like 50 sections, it's usually like four, five, six, at most.

**Daniel Lopes:** But we split them in a process in a parallel.

**Daniel Lopes:** The first step we do is like generate the search queries you would have to look for that section.

**Daniel Lopes:** And in this case, it's like what is a headless, the input was on this section.

**Daniel Lopes:** So top 10 headless commerce performs 1,000 words, so pretty high.

**Daniel Lopes:** So like introduce the.

**Daniel Lopes:** the concept definition of architecture, it will generate queries, search queries from that, and we will look up and alleviate.

**Daniel Lopes:** So if that doesn't return enough, that's how you see here, searching with the idea.

**Daniel Lopes:** So these are the questions.

**Daniel Lopes:** This was the output from the deviate, and if we get a point where we didn't get enough, it will hit perplexity and put deep researchers perplexity.

**Daniel Lopes:** So that's another place where if we do something that's, let's say, type something here that we haven't had researched before, you would trigger the research and then try to go deeper.

**Daniel Lopes:** And at the end, then we're gonna assemble all the sections and polish everything in one long article.

**Daniel Lopes:** that's another thing we did with couple of like, I was last week, like we switched everything from OpenAI to Cloud 3.7.

**Daniel Lopes:** Yeah, so we are seeing...

**Daniel Lopes:** better results on the quality of the article from the start.

**Daniel Lopes:** What we were doing before, it would generate like not great wording and like kind of robotic, like opening eyes on really great for like quality of writing.

**Daniel Lopes:** They're great for like research and for answering things fast, but not really great writing style.

**Daniel Lopes:** we had like a heavy step at the end that would try to polish the article, but now we're getting better quality from the start because we're searching to cloth.

**Daniel Lopes:** And so that's the outline process that generates the draft and then from the draft to have this post-processing staff and the post-processing will do the SEO analysis and will do like a check on the quality of the writing again.

**Daniel Lopes:** So we'll be like, we're using too many buzzwords, it's the text to dance and I'm cleaning that up.

**Daniel Lopes:** So this is a spot where we have to like read the draft and look if the the thing is the content is.

**Daniel Lopes:** good.

**Daniel Lopes:** And depending on what we do here, we can adjust before we go to the post-processing.

**Daniel Lopes:** And then the post-processing, we have essentially the final article, and we have a last step here where we can have a bunch of feedback that we can give to the content.

**Daniel Lopes:** So you can say, add a hook, or add an in-brief section at the top, or in the conclusion, add a CTA for that.

**Daniel Lopes:** So you can write free form, whatever the things that you want to change, and or maybe add a table of contents to the top or something like that.

**Daniel Lopes:** And the last thing we do is the internal linking that will use what we scraped from your side map to try to find the opportunities for internal linking.

**Paul Bratslavsky:** And that's another place.

**Daniel Lopes:** If you have places that you don't want to be linked, we can have a black list.

**Daniel Lopes:** And so the last thing we do is the fact checking.

**Daniel Lopes:** So the fact checking is the place that I think we could use.

**Daniel Lopes:** where we could replace the fact-checking we have here.

**Daniel Lopes:** Fact-checking is just using your docs and having an agent in the AirOps, using all the AirOps infrastructure to check their agents, like their Q&A based on your docs, but their agent is not good at all.

**Daniel Lopes:** So that's one part that we could remove this entirely creator for just for you that will be integrated with Kappa.

**Daniel Lopes:** And now we have the infrastructure for that.

**Daniel Lopes:** So that's the thing that we were struggling with.

**Daniel Lopes:** Last time I met with Victor and the guys, like we didn't have, like we're still heavy in AirOps, but now we have the system where we can just call whatever API we want to run in our system.

**Daniel Lopes:** So we could do that for sure.

**Daniel Lopes:** That would be probably like, in less than a week we can have that integrated.

**Daniel Lopes:** Yeah, no, that would be awesome.

**Paul Bratslavsky:** So like to just kind of internal linking.

**Paul Bratslavsky:** So basically one, like,

**Paul Bratslavsky:** One of the improvements you're saying, if there's something that we don't want to kind of use as resource, make sure to be blackless.

**Paul Bratslavsky:** Because we do have some older content on our website, which sometimes comes up as links in the blog post.

**Paul Bratslavsky:** So this is something that Theo, one of our who is responsible for working with growth ex closely, reviewing the articles where some of the linking that we get is for updated articles.

**Paul Bratslavsky:** And so part of that could be fixed by us updating the site map to exclude him.

**Paul Bratslavsky:** Is that kind of that's going to be too hard for you guys to do like that.

**Daniel Lopes:** That's another feedback that we received from other clients is like linking to your content isn't great.

**Daniel Lopes:** And obviously, so we were thinking about that already.

**Daniel Lopes:** So it's good to hear that.

**Daniel Lopes:** So I have that ticket in our backlog already.

**Daniel Lopes:** But let me make sure I don't forget this.

**Daniel Lopes:** And then we we had a step to like look like remove old stuff.

**Daniel Lopes:** Like, if you have specific URLs that you don't want, that's something we could add as well.

**Daniel Lopes:** I don't think we have support for that, but it wouldn't be hard to add.

**Victor Coisne:** So, I thought you just said there's a kind of a block list and like an exclusion list.

**Victor Coisne:** we just like add like a bunch of articles.

**Victor Coisne:** Specifically for us, instead of the stuff that's like the previous version, the V4.

**Victor Coisne:** So I believe it.

**Paul Bratslavsky:** Yeah, sorry, go ahead, Victor, sir.

**Paul Bratslavsky:** And maybe my ADHD kicking hard.

**Paul Bratslavsky:** I was gonna say, I think what we talked about before, like if you have a specific URL slash a blog, let's say archive or old, like whatever.

**Paul Bratslavsky:** And we tag all the articles in that URL and move them all under that kind of URL structure.

**Paul Bratslavsky:** Like I think we could pass that URL and it will exclude old posts.

**Paul Bratslavsky:** So we could probably do that to like right now with the technical capabilities.

**Paul Bratslavsky:** Cause.

**Paul Bratslavsky:** Earlier before I jumped on the call, I kind of talked about how we're creating a lot of articles with GrowthX, and some of those GrowthX articles are now popping up as the research article when we write new articles.

**Paul Bratslavsky:** so I kind of wanted to see if there's a way to basically blacklist all the GrowthX articles, so they're never used in the research to write new articles.

**Paul Bratslavsky:** And so that's what Daniel said is to, we could blacklist the URL where those articles live under, for instance, like it gets drafted out to ecosystem, I think it's what we decided, but I'll double check and give you the exact details for that, Daniel.

**Daniel Lopes:** Yeah, like the things that we have both hands, like at the beginning of the process, which articles we use as the foundation to generate the article, so that we support blacklisting already.

**Daniel Lopes:** And at the end of the process, when we do the internal linking, we are just ingesting your entire site map that you give us.

**Daniel Lopes:** Oh, that there, we don't have a blacklisting.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Probability already, but it wouldn't be hard to add, especially if you're, if you're doing like you're saying, if there's like a path in your URL, like there is like a prefix in the path or something like that, then we make it a lot easier.

**Daniel Lopes:** Like we can add that today and, and then we can have that as a step in internal thinking that will strip out everything that, that is under that, that path, does that make sense?

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** And I think that would be like the quick path to like getting the thing that we want them and getting it implemented fast.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** That makes sense.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** Yeah.

**Daniel Lopes:** can do that.

**Daniel Lopes:** We can do that today for sure.

**Daniel Lopes:** And if you also have like anything that's like date based, because I assume like, that your guys have, if you guys have like a timestamp, do you remember with, to blog, yeah, go to, uh, develop, uh, and, yeah, you, you found it.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** So there's time stamps here.

**Paul Bratslavsky:** we could, like, if we are able to.

**Paul Bratslavsky:** filter like you had the blog open in just a second now in the left right there we do have the dates like created at Like right there you see you can see so we could If you're able to filter Like on the date.

**Paul Bratslavsky:** That's it's implying.

**Daniel Lopes:** think that'll be great too cuz if you just focus on the most recent articles that've been written I was thinking if you if you had the date in the URL, but you don't inside the URL gotcha.

**Daniel Lopes:** Yeah, none of it.

**Paul Bratslavsky:** Don't do that Yeah, we have yeah, it's not a property in the world.

**Paul Bratslavsky:** No, you got it.

**Victor Coisne:** Okay Yeah, but it we have a date field in the strategy API, so maybe you know Maybe you can come to the API directly.

**Paul Bratslavsky:** Yeah Yeah, I think I think like I was like I think when they do the research of our site Maybe I'm confusing like are you hitting our exactly or are you doing?

**Paul Bratslavsky:** Okay, web search.

**Paul Bratslavsky:** Okay, that's what I just wanted to ask asking why

**Paul Bratslavsky:** but like if you have date, timestamp.

**Paul Bratslavsky:** yeah, so the way they're creating our website, they wouldn't have access to, yeah, that type of Yeah, they got it.

**Daniel Lopes:** If you would probably not want to have your own articles as research material, right, for?

**Paul Bratslavsky:** So that's the thing that I think like it's interesting is because you have internal articles that sometimes have very valuable like specific things to scrappy that might be useful for GrowthX.

**Paul Bratslavsky:** But at the same time, maybe like, like, should it be a resource?

**Paul Bratslavsky:** Should it be more specific to things that follow more of our best practices, which is the documentation and then Kappa AI implementation and not previously written the articles.

**Paul Bratslavsky:** I don't know, like, you know, which one is which, but I think what?

**Paul Bratslavsky:** Yeah, me talk about that.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, because like we're rewriting our researcher this week to switch to sonar, to perplexity.

**Daniel Lopes:** And...

**Daniel Lopes:** I think I could have a way to input certain URLs.

**Daniel Lopes:** So if you have an article that you know you want to cover, let's say, migration or you want to cover a new version or something like that, you can input the URLs that you want to have and then include it in the research.

**Daniel Lopes:** And then we can have a copy at the end as well as the fact checker.

**Daniel Lopes:** we make sure whatever syntax, whatever code snippets we generate will be validated against a copy.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** I think that would cover both ends of the spectrum.

**Daniel Lopes:** Yeah, I think that would be awesome.

**Paul Bratslavsky:** And another question I had, because I think like, you know, it's awesome to think of like everything doing us like, it works for every type of content, but you know, certain content that's very technical, obviously writing it, you know, with AI, although it be a good start, it might hallucinate some things, it might be difficult.

**Paul Bratslavsky:** So from your perspective, do you think there's certain type of articles we could just not try like.

**Paul Bratslavsky:** to do with AI like I know it's like this is the service you provide but at the same time to kind of help everybody you know not to have this back and forth where we try to fix an article that realistically could have been generated by us.

**Daniel Lopes:** Yeah it depends on the if the it on the source that's why I was thinking like if we get the researcher right and you know the URLs you want to cover then it would be essentially and making and like an adaptation of like a documentation that's like the GWT with versus OAuth here for example.

**Daniel Lopes:** If you got like a like a Mozilla API reference on how to do like JWT for example or if you get and then you or you get this back of OAuth last version and you put for those as like I want to start here yeah and then it would do much better than just like Googling it so because I know we're essentially essentially running

**Daniel Lopes:** let's say, similar to opening IT research on the result of the googling of this, and you don't have that much control of what you're getting out as the first results.

**Daniel Lopes:** the way you're running today, you're right.

**Daniel Lopes:** if we have certain topics that are super technical or things that are refreshingly launched, something specific to Strapi that you guys launched a week ago, it would not perform well.

**Daniel Lopes:** So, but the way that we're talking about, like, if we can't actually fast direct URLs, I think you're going to pretty well.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** So, I was going to say, like, should we have like a step, like, because right now, all this kind of happens automatically to the added step where, like, if we do have, let's say, four-year-olds, let me feel like going to be really helpful for this particular blog post, that we could just add them, like, in the flow here in the table, that could pull, like, I'm assuming that would improve the process, and that would

**Paul Bratslavsky:** kind of give us that thing like what Victor and I talked about with the growth extreme is to have that ability to point to specific resources that could help to guide the AI to accomplish little bit more better content.

**Victor Coisne:** Yeah, exactly.

**Victor Coisne:** what we discussed is like doing the topic, some of the topic research and then curating like a couple of Yeah, no, that makes sense.

**Daniel Lopes:** Yeah, I'm supposed to be the one rewriting our researcher so I will take that into the scope.

**Daniel Lopes:** I add that to the scope because that will solve a lot of the like your challenge is not unique and we want to have that covered for everyone.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** Yeah.

**Daniel Lopes:** All right, that makes sense.

**Victor Coisne:** I added a quick, I don't know if you wanted to continue on this topic as a slight link.

**Victor Coisne:** different topic which is related to images.

**Victor Coisne:** I didn't respond to your method yesterday, but you had a good time to talk about that now, or you.

**Daniel Lopes:** Yeah, I don't know, I wanted to show you, like we don't have images, I think we cover everything from the grid that we have now for you guys.

**Daniel Lopes:** So like it would be like we print the fact check for a kappa and then we have today, around images, like I was checking you like all your blog posts and everything, you guys have the cover image already.

**Daniel Lopes:** And this is, like there are ways to do cover images like this, but it's not, it's kind of like, it's lot of work.

**Daniel Lopes:** I don't think it's like super helpful, like because you guys already have the theme.

**Daniel Lopes:** But so I wasn't sure, like if you wanted to have images, if you wanted to have replacing the cover image, or if you wanted to have things in the body of the article.

**Daniel Lopes:** Yeah, I mean like body of the article.

**Victor Coisne:** And that's where, you know, think like it's, it's often to hear.

**Victor Coisne:** that you are open to using not give because I think like architecture diagram is really what we're after here.

**Victor Coisne:** I think it will help a lot to just even if it's high level just having some kind of off-stage diagram.

**Victor Coisne:** But for like the, I forgot the name of the one that you mentioned but the one I tried is Lasko and and for Lasko the idea is to we're trying to have images that are more in the realm of our branding.

**Victor Coisne:** see like it's like Past Hog I think is a really good experience, is a group of examples of a brand that you know that is nailing it with their mascot.

**Victor Coisne:** So obviously we don't have a mascot to play with but we have like a team around like the space spacing that we want to lean on that a bit more.

**Victor Coisne:** So that's where my head's at with this one.

**Victor Coisne:** Yeah that sounds good.

**Daniel Lopes:** Let me show you something that we do for some other clients that I think we'll work here.

**Daniel Lopes:** really well.

**Daniel Lopes:** We have an integration with recraft and recraft, let me show you this.

**Daniel Lopes:** we use recraft for web stacks and web stacks and we also use it for execs.com and we also use stability AI for data green, but I don't think that's going to work for what you're saying.

**Daniel Lopes:** So exec, for example, they have articles, they want always something that's like 2D and has this black and white style.

**Daniel Lopes:** So we have the, so we read the article, come up with a bunch of ideas and so like there was a step in between here like generates like four different images and

**Daniel Lopes:** Our editor chooses from the style.

**Daniel Lopes:** So we create this style ahead based on whatever image they sent us.

**Daniel Lopes:** So they sent us like 10 different images and we like clean it up and adjust and create this style in the recraft and then recraft is part of the process.

**Daniel Lopes:** So like the way we generate the image here is, let me show you.

**Daniel Lopes:** So this case was, so we generated three images.

**Daniel Lopes:** Let me just open the execution.

**Daniel Lopes:** So we receive the articles and input and generate a bunch of image ideas like this.

**Daniel Lopes:** So 10 different image ideas.

**Daniel Lopes:** have a step that chooses the best one based on your company context and the content of your article.

**Daniel Lopes:** then we generate the images and store in our S3.

**Daniel Lopes:** So like in this case, we have these three versions for this article about performance management.

**Daniel Lopes:** So this is the kind of very relevant to the team.

**Daniel Lopes:** But they

**Daniel Lopes:** It came off of the style that they wanted.

**Daniel Lopes:** So if you have like a style that you like, we could create that and have that be part of like, generate this part of the process.

**Daniel Lopes:** And then you can see through life there.

**Daniel Lopes:** Yeah, it sounds great.

**Victor Coisne:** But we'll take that as an action item to kind of give you like 10 images as a, like five images of the other.

**Daniel Lopes:** Let me show you another example from another client that's completely different.

**Daniel Lopes:** So I don't know if you're familiar with craft, the craft is a new product, but they can do super realistic stuff from like images, photos to the illustration to vector, to hand-drawn stuff to 3D looking.

**Daniel Lopes:** So in this case, for example, it's more, it's a style that one of their designers had.

**Daniel Lopes:** was a kind of 3D looking, always blue and white on the dark background.

**Daniel Lopes:** So we were able to replicate the design pretty well.

**Daniel Lopes:** No, it's it's the same idea.

**Daniel Lopes:** So we read the article, come up with a bunch of ideas.

**Daniel Lopes:** have it.

**Daniel Lopes:** So it's the exact same work.

**Daniel Lopes:** just receiving a different style ID that we create in the recap.

**Daniel Lopes:** So we're like, we could do that.

**Daniel Lopes:** So you can find a bunch of different styles.

**Daniel Lopes:** Doesn't work with all kinds of styles, but for certain things, it works really well.

**Daniel Lopes:** So we might have to find like, what works well for.

**Victor Coisne:** You need to make it a bit more developer friendly. The images you're showing us — I think you need something that looks like code or more technical styling. Like the one you just showed — with the virtual and linear branding, that's more what I'm looking for.

**Daniel Lopes:** Yeah, exactly. If you have some references, that would be a very helpful starting point for me. And I'll look into the Kappa integration as well — that's another thing all our clients want. We can set you up with a user and API key.

**Daniel Lopes:** I'll follow up on that with Victor and Paul.

**Paul Bratslavsky:** One thing though — the Kappa search works way better than our current documentation implementation. It's a much better experience.

**Victor Coisne:** Yeah, Kappa isn't cheap, but it does a good job.

**Daniel Lopes:** They should look into caching commonly asked questions to reduce costs.

**Daniel Lopes:** I was going to say, they should come up with a way of caching commonly asked questions.

**Paul Bratslavsky:** So that's the first thing they serve, you know, I think that's a good idea for sure.

**Victor Coisne:** So like I have my two dudes here, let me see if I forgot anything.

**Daniel Lopes:** Blacklist domains, Blacklist internal linking, update the researcher to be able to take specific URLs, kappa, learn if we can integrate it and map them.

**Daniel Lopes:** We also have Victor who will help with illustrations or style and we can try to add image generation.

**Daniel Lopes:** Anything else?

**Paul Bratslavsky:** I kind of cut out for a second, did you mention also like add ability to add resource links to point to specific content, to use that, okay, yeah, that's part of the researcher, make sure you have that in the book, yep, yeah, perfect.

**Paul Bratslavsky:** And Victor, one of the things Daniel told me that because you already from our end that could help us a lot is

**Paul Bratslavsky:** for every article that you write, there's this context portion about our company.

**Paul Bratslavsky:** We could add with additional context of what we want to guide the article with to get slightly better brief on from the start.

**Paul Bratslavsky:** So that's kind of cool.

**Victor Coisne:** Yeah, that's the thing.

**Daniel Lopes:** don't know if you saw that.

**Daniel Lopes:** I think we were not here, this is essentially what I was telling all.

**Daniel Lopes:** That we have a lot of steps in the process where you can intervene.

**Daniel Lopes:** So that would be at the beginning of the process, we generate assignment brief is a core part of the process, the assignment brief has key points to cover.

**Daniel Lopes:** We just added the stop to the comparative URLs, articles that we need to compete against.

**Daniel Lopes:** added the style of the article and stuff like this, and we also have the topics and the user consideration that's all coming from like reading.

**Daniel Lopes:** articles based on the topic that was chosen and taking consideration description of the company.

**Daniel Lopes:** So we have just two paragraphs you're describing the company.

**Daniel Lopes:** Ideally, we would extend this further, but also we have the ability to ask information about the audience that you want for this article.

**Daniel Lopes:** So we haven't used that in your case.

**Victor Coisne:** So let's say you're doing a migration.

**Daniel Lopes:** In this case, we have less commerce platforms.

**Daniel Lopes:** You could say here, like we're doing this for this kind of user, but this person, like maybe they're like shopping for users and they want to switch to the only integrative strategy or something like, or I don't know, like whatever in the realm, you know what I mean?

**Daniel Lopes:** So that's the place that if we had this information would be super helpful for Andre and the team.

**Daniel Lopes:** I don't know how they see that integrating with the work, they today work with you guys, but that is an information that if we had an agreement, would perform better generation of the brief.

**Daniel Lopes:** Yeah.

**Victor Coisne:** Well, maybe in our table, Paul, like where we

**Victor Coisne:** You should do is like, I have a column in the air table.

**Victor Coisne:** Yeah, that makes sense.

**Paul Bratslavsky:** like he just added little Daniel today added that uses content field.

**Paul Bratslavsky:** And so we could have that field in the air table where whenever Theo or I add articles, we add additional contacts that could help them.

**Paul Bratslavsky:** And maybe in the future when we implement the resource links that could also be another air table item that we prepare for GrowthX and they have all that information.

**Victor Coisne:** Yeah, that would be great.

**Daniel Lopes:** We're building an internal platform to replace Airtable and AirOps — you'll be able to log in and see everything in a simpler interface without needing to understand all the different workflows. It's going to take a couple of months, but once it's ready, you'll have full visibility without us disrupting anything.

On localization and translation — we've got a lot going on. We're integrating with other workstreams, and I was also touching on competitor comparison.

**Victor Coisne:** competitor comparison, like the list of all our competitors, that's another kind of work stream that we might think about.

**Victor Coisne:** So I'm hesitant to introduce another yet another stream, but I do want to start to experiment a little bit and see if it's worse investing more.

**Victor Coisne:** So is that something that you've done with other clients?

**Victor Coisne:** Yeah, we've done.

**Daniel Lopes:** We have one client that we have on all the articles that are both in English and Spanish and has some things that are like it works really well, but the main thing is like dealing with the different URLs.

**Daniel Lopes:** So if you have a system where the URLs are always mapped, so like for them it's becoming a little bit of a manual work, just matching the links, because they don't always have, let's say you have an article in English, and then they create a Spanish version

**Daniel Lopes:** that article.

**Daniel Lopes:** If you have a bunch of internal links that don't have the equivalent in Spanish, they have to go there and adjust the links to whatever they think is the best match or remove the links.

**Daniel Lopes:** That we don't have automated, but the generation of the article generation of the keywords and stuff like that we have.

**Daniel Lopes:** So we have it working in Spanish for sure, but I don't think it would be hard to do other things.

**Daniel Lopes:** know we haven't tried a bunch of different languages, and we only have people in the team that speak Spanish and Portuguese.

**Daniel Lopes:** I think there might be people that speak other languages, but the person in charge of the translation, she is both fluent in English, Spanish, and Portuguese, so she's in charge of checking the quality.

**Daniel Lopes:** I don't know if that helps, but we can do something together if you want.

**Daniel Lopes:** We can put a grid just to generate the same article than you guys see.

**Daniel Lopes:** Well, I'm thinking maybe at first what would be good.

**Victor Coisne:** Start with a one-pager overview in multiple languages — like a landing page with language flags. It's one article providing a big overview that gets translated, not every article translated into 10 languages. We could include major languages plus Chinese. Quality assurance might be a challenge, but it's more manageable than full multilingual content.

**Daniel Lopes:** Yeah, I think we can, yeah, if it's something that you want to try, like maybe you can, like, put on the technical side, we can definitely do that, we just have to check with the guys, like, what they're thinking, you know, where he would fit, but yeah, we can do that for sure.

**Daniel Lopes:** And that's much more doable than having 10 different languages for every article, because that's also a challenge on the CMS, your URLs and all

**Daniel Lopes:** the stuff that I'm talking about, images, and...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Although that'd be a really cool, like, talk or ask for, like, how to do this with Strapi.

**Victor Coisne:** Like, this, you know, we handle localization in Strapi.

**Victor Coisne:** So I think, like, I'd love to see...

**Victor Coisne:** I'm sure, like, some people are thinking about that.

**Victor Coisne:** I really think, oh, that can be something we add to our...

**Victor Coisne:** So, backlog of content.

**Victor Coisne:** How do you do content internationalization at scale in the AI era?

**Victor Coisne:** Yeah, that'll be interesting.

**Daniel Lopes:** Like, we have one of the engineers that are joining this mug, because he did that at ClickUp.

**Daniel Lopes:** And so every article that they published was published in 11 languages.

**Daniel Lopes:** that could be an interesting project for him to, like, figure that out.

**Daniel Lopes:** And we could expose the translation as an API endpoint, we could integrate that with Strapi as, like, not like a plugin.

**Daniel Lopes:** guys want to translate to whatever languages?

**Daniel Lopes:** And that would be a cool project that we can do, like, as a join.

**Victor Coisne:** blog first, know, like we should talk to, um, yeah, when that person is, uh, is on board, like, you know, I think we could use that as a way to, like, uh, position, grace, like, the international content, you know, AI powered content agency.

**Victor Coisne:** Yeah, that would be very cool.

**Daniel Lopes:** I'm making sure I'm right down here.

**Daniel Lopes:** Don't forget.

**Daniel Lopes:** So I'm sure myself would like that one.

**Victor Coisne:** Yeah.

**Victor Coisne:** Oh, chat to him.

**Daniel Lopes:** Sounds great.

**Paul Bratslavsky:** I was going to say, well, this meeting is going, like, for a while, all the interesting stuff, by the way, but I just wanted to quickly mention, uh, I know we've talked about possibly taking videos from YouTube and using them as knowledge faces.

**Paul Bratslavsky:** Is that something that, uh, you're currently thinking of doing or working on?

**Paul Bratslavsky:** Is there other people that ask kind of for that ability to use YouTube transcripts and have that be a source of knowledge base to write articles?

**Paul Bratslavsky:** Yeah, that's the thing.

**Daniel Lopes:** Like,

**Daniel Lopes:** Today, we have the option to take in videos and have to turn them into articles.

**Daniel Lopes:** So the workflow right now, like it takes like whatever size of the it's like a two hour long article, it was recommend like, hey, there's enough content here for like maybe four artists here, the potential articles, and then the editor chooses from there, and it creates an article out of that.

**Daniel Lopes:** So that we have what you're, I think, if I understand correct, like what you're saying that ideally we'll just ingest a bunch of different transcripts and how that is a data source for potential art that we don't have.

**Daniel Lopes:** It's a lot, it's kind of what we were saying before that we're doing this data source with intern and external, like external would be like researched, Google or perplexity, whatever, and internal would be like sources that you give us.

**Daniel Lopes:** video would be one of those like I'm, I'm, I'm, I'm staffing this project already.

**Daniel Lopes:** So it would be something I think it would take like probably a couple of

**Daniel Lopes:** But it will replace a lot of the research that I'm showing you, it would be the next step of this.

**Daniel Lopes:** So why I hope we can have that as a functionality.

**Daniel Lopes:** Yes.

**Daniel Lopes:** That was a couple of months.

**Daniel Lopes:** Yeah.

**Paul Bratslavsky:** Because that's a lot of features like notebook and lamb has where you put points a bunch of different resources and they'll generate like a podcast based on those resources.

**Paul Bratslavsky:** If you had a tool where you put in four or five resources and it automatically generates a blog post, that would be cool. It would allow teams to create curated content based on what's trending. The tool I'm thinking of is Notebook LM — you can put resources in there, it generates a podcast, and then you can take that transcript and turn it into a blog post. That would be an interesting workflow.

**Daniel Lopes:** Oh that that would work already so like because you're doing the work heads to do that let me show you like real quick so for got a little we do the repurpose of their podcast because you're generating a podcast that's actually cool in this case I never thought about that so once I find there I have a couple of clients that do the repurpose from their live podcast so what guest article generation so it takes in the URL of audio we transcribe the audio and we generate we look for opportunities so in this case for example the opportunity was just was four opportunities one so

**Daniel Lopes:** This is a company, I don't know if you've got any of those evaluations, other than evaluations.

**Daniel Lopes:** So it was like four potential articles and the confidence of that article being like a good article for the user base, estimated work count that can be used.

**Daniel Lopes:** then the editor chooses one of those or like all of those and would generate a brief similar to the kind of brief you saw before.

**Daniel Lopes:** And then at the end, it goes into the same flow where we generate the sections based on the outline, but using just that data source.

**Daniel Lopes:** So the final result is something like this.

**Daniel Lopes:** So this came from their podcast.

**Daniel Lopes:** So I had a special introduction saying like, who are the people involved?

**Daniel Lopes:** And then the article based on the podcast.

**Daniel Lopes:** So if you're already generating podcasts, we could ingest that and generate an article.

**Daniel Lopes:** But if you're thinking like just based on the whole podcast in July.

**Daniel Lopes:** Something like ChatGPT or doing a good job too, like that's probably not worth it.

**Daniel Lopes:** Yeah, yeah, that's something to explore.

**Paul Bratslavsky:** Yeah, I'll keep that in mind a lot of cool stuff.

**Paul Bratslavsky:** Yeah.

**Daniel Lopes:** Awesome.

**Victor Coisne:** Well, thanks Daniel.

**Victor Coisne:** We appreciate your time.

**Victor Coisne:** Exciting maximum items.

**Victor Coisne:** Yeah.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** I have the to do here.

**Victor Coisne:** I'll follow up with you guys and Andrej.

**Daniel Lopes:** Awesome.

**Victor Coisne:** I already thanks to the API keys.

**Victor Coisne:** All right.

**Victor Coisne:** Awesome.

**Victor Coisne:** Thank you.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** Have a good day.

**Daniel Lopes:** Bye.

**Daniel Lopes:** Bye.
