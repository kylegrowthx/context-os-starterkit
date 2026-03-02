# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-13
time: 17:31 UTC
duration: 27 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević (GrowthX), Erik O'Brien (GrowthX), Alexis Ruiz-Pedregon (Redis), Fung-Lin Wu (Redis), Cody Henshaw (Redis)
fathom_recording_id: 101490999
fathom_url: https://fathom.video/calls/472178081
share_url: https://fathom.video/share/74LmLmWPmjsdRKsPsTx6EGCAAMisxW-y
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX presented the initial content calendar for Redis with 71 new article ideas organized across 6 topic clusters covering foundational, mid-funnel, and bottom-funnel content. The team discussed competitor content strategies (Pinecone, Mongo, and Dragonfly using separate sites for technical vs. SEO content), reviewed the new "agentic" AI pipeline that self-evaluates research and drafts to ensure quality, and aligned on next steps: Redis will review and approve the 71 ideas in Airtable, GrowthX will add a checkbox approval column, and initial focus will be on new content to establish voice and tone before moving to refresh articles.

---

## Context

Redis is a large-scale infrastructure software company investing in content marketing to improve SEO visibility and authority. GrowthX was engaged for a strategic content initiative to refresh Redis's blog and glossary strategy. The relationship kicked off with a strategy call the day before, and this follow-up sync focused on operational delivery: reviewing the initial content calendar, aligning on approval workflows, and discussing the AI pipeline that will generate articles. The meeting included content strategists from Redis (Fung-Lin Wu, Alexis Ruiz-Pedregon, Cody Henshaw) and the GrowthX team (Aida Knežević as lead, Erik O'Brien contributing early context).

---

## Relevance

**To GrowthX Delivery:**
- The agentic AI pipeline represents a significant operational change — this self-evaluating approach reduces human editing burden and is being positioned as a key differentiator for complex, technical verticals like Redis.
- Writing guidelines and proofreading checklists must be tuned carefully because LLMs can over-index on certain instructions; GrowthX should plan for iteration cycles on the first 2-3 articles before scaling.
- Checkbox workflows in Airtable hit limitations with commenting-only access (Airtable restricts features to paid seats); GrowthX may need to manage workarounds or escalate to paid access if this becomes friction.

**To CheckThat:**
- Redis's content strategy involves deep coverage of LLM-related topics (context window management, token optimization), which is directly relevant to CheckThat's AI visibility positioning.
- The conversation highlighted the importance of SEO-first content strategy for technical products; this validates CheckThat's core value proposition around AI visibility and search ranking.

**To GrowthX Business Development:**
- Redis is actively investing in content (71 articles approved for initial build-out), signaling strong budget commitment and likely expansion scope after this first phase.
- The refresh strategy (auditing 6-month traffic data to optimize underperforming articles) suggests a multi-phase engagement; GrowthX should monitor for opportunities to expand into performance analytics and ongoing optimization.
- Pending access to the "cache modernization" cluster document indicates Redis may add 7+ more content clusters beyond the initial 6, expanding scope significantly.

---

## Overview

- **Content Calendar Ready:** 71 new article ideas are in the Airtable "Content OS" for review, covering 6 core clusters and a mix of TOFU/MOFU/BOFU topics.
- **Competitor Strategy:** Top competitors (Pinecone, Mongo) use separate sites for technical vs. SEO content, a model Redis should consider for its blog vs. glossary.
- **AI Pipeline:** GrowthX will use a new "agentic" AI pipeline that self-evaluates its research and drafts, ensuring higher quality and reducing human editing.
- **First Articles:** The initial focus is on new content to align on voice/tone. Refreshes of underperforming articles will follow, guided by a content audit.

---

## Key Topics

### Competitor Content Strategy

  - Top competitors use separate sites for distinct content types to maximize search visibility.
      - **Pinecone:** "Blog" for technical content, "Learn" for SEO-focused foundational topics.
      - **Mongo:** "Blog" for news, "Resources" for SEO articles.
  - **Redis Context:**
      - The "Glossary" was created by an SEO specialist for fast content launches, separate from the main content team.
      - The "Blog" and "Learn" sites have undefined distinctions.
  - **Action:** Redis should define clear roles for its various content sites (Blog, Glossary, Learn) to optimize for both technical depth and SEO traffic.

### New Content Calendar & Review Process

  - **Content OS (Airtable):** The central hub for managing the content pipeline.
      - **Views:** `Ideas for Review`, `Drafts for Review`, `Published Docs`.
      - **`Ideas for Review`:** Contains 71 new article topics.
          - **Grouping:** By 6 topic clusters (e.g., Industry Solutions, LLMs).
          - **Topic Mix:** Includes foundational ("what is"), MOFU (e.g., "optimize payment processing"), and BOFU (e.g., "improve app UX with Redis") content.
  - **Review Process:**
      - **Action:** Review ideas in the `Ideas for Review` view.
      - **Feedback:** Use Airtable comments or emojis (👍/👎) on each record.
      - **Goal:** Align on voice, tone, and product messaging before scaling.

### Content Generation Pipeline

  - **"Agentic Pipelines":** A new, self-evaluating AI system to ensure high-quality content.
  - **Process:**
    1.  **Research:** AI generates questions, finds answers, and self-evaluates its research quality.
    2.  **Drafting:** AI writes the article using writing guidelines and a proofreading checklist.
    3.  **Self-Correction:** AI evaluates its own draft against the guidelines and revises it.
  - **Product Accuracy:** A separate artifact can be added to the pipeline to fact-check all product claims, ensuring technical accuracy.

### Content Audit & Refresh Strategy

  - **Audit in Progress:** GrowthX is analyzing 6-month traffic data for the blog and glossary to identify underperforming articles for refresh.
  - **Prioritization:**
      - **Phase 1 (Now):** Focus on new content to align on voice/tone.
      - **Phase 2 (Steady State):** Combine new content with refreshes.
  - **Data Provided:** Alexis shared 12-month traffic data (sessions, sign-ups) for the top 10 blog posts and the `/learn` subdirectory to guide the audit.

---

## Action Items

**Aida Knežević (GrowthX)**
- Add checkbox column to Airtable for Redis team to mark approvals

**Fung-Lin Wu (Redis)**
- Review 71 Airtable ideas in the Content OS; approve/reject, add comments, and tag Aida
- Review audience personas and company context documents

**Alexis Ruiz-Pedregon (Redis)**
- Review 71 Airtable ideas in the Content OS; approve/reject, add comments, and tag Aida

**Cody Henshaw (Redis)**
- Review 71 Airtable ideas in the Content OS; approve/reject, add comments, and tag Aida
- Review audience personas and company context documents

---

## Transcript

**Erik O'Brien:** So apparently the images we showed field guide were just not run by Katya. Those are just like the ones auto-generated by the identity pipeline.

**Aida Knežević:** I think Hassan set it up. He did it like he did for Fleet.

**Aida Knežević:** She can change it, but we do have to say that the colors are a little bit tricky to get.

**Fung-Lin Wu:** We had a leadership off-site, so a lot of people might be traveling today. I actually flew in yesterday because of the government shutdown.

**Aida Knežević:** So I'm just going to go ahead and share my screen. There are a couple of things to cover today. Since last week we updated the artifacts using the team's feedback, but we're going to continue folding in any additional comments that you leave.

**Aida Knežević:** The writing guidelines are probably going to get the most attention as we start creating content. There are a lot of small tweaks that we have to make because we never really quite know how an LLM is going to react to the writing guidelines. We have a specific structure that works well, but sometimes an LLM kind of over-indexes on one instruction and ignores others.

**Aida Knežević:** The good thing is that we now have these new article generation pipelines called agentic pipelines. Where the AI evaluates itself at the research stage. When we give it an outline and title, it asks questions that it needs to answer to create a research document that will be used to generate the article. Then it actually evaluates whether that research document answered the questions and evaluates the quality of the research.

**Aida Knežević:** At the end of the article, when it generates the draft, it's going to use the writing guidelines and a proofreading checklist with any rules you have around punctuation, capitalization. Then it evaluates the article draft to see if the AI actually followed the guidelines and the proofreading checklist, and it fixes anything that doesn't follow the guidelines.

**Aida Knežević:** The output is a lot better because it actually repeats certain steps twice and evaluates its own work. Because you are in an industry that is complex and the subject matter is quite advanced, we made sure to get this set up before we start generating so that you have less human editing to do.

**Aida Knežević:** Last week, Fung-Lin, you were wondering about a breakdown of competitor content along technical lines. In the blog content strategy, in the competitor topic analysis, for each of the competitors, you can see what are the core topics and what is the technical focus. For some of your competitors, like Pinecone, they have a separate section on their site for SEO non-technical content, and then the blog hosts their more product-focused, very technical content written for subject matter experts by subject matter experts.

**Aida Knežević:** The non-technical content does have higher search visibility, so Pinecone, Mongo, and Dragonfly all do a lot better in search with the SEO blogs rather than the more technical blogs.

**Alexis Ruiz-Pedregon:** Are those SEO blogs differentiated? Do they call it something else other than blogs on their site?

**Aida Knežević:** Yes, exactly. For Mongo, if you go to the blog, it's announcements, updates, news, and then they have the resource section. Mongo does it in a weird way — they have these basics that the URLs are discoverable, but the actual blogs are difficult to discover on the site. They have e-books and articles, but only when you get into the URLs can you find these basics. For example, they have "data centers explained," which is an SEO blog post about data centers, but these basics are difficult to find on the actual site.

**Alexis Ruiz-Pedregon:** So it's almost just for SEO. But they do rank very well and get a lot of traffic.

**Aida Knežević:** For Pinecone, the blog is more product-focused and way more technical, and then they have the Learn section of their site, which focuses more on "what is" and foundational content, similar to your glossary. But I also think your blog isn't just for SEO — some SEO content does live on your blog, but the glossary is more foundational. In the industry, there's a distinction, especially among companies that get more traffic from SEO and Google search. They divide this type of content into two different parts of the website.

**Fung-Lin Wu:** Yeah, we've kind of thought about it also because we have a Learn site, a resource site, the glossary, and the blog. I think we're slowly starting to have a distinction between them. The glossary was created because we needed a fast path to launching articles, but we didn't intentionally think about what goes on the blog versus the glossary.

**Cody Henshaw:** It was run by completely different people. There was an SEO person who literally generated just his own glossary content that worked outside of the content teams completely separately. Everything that he would work on would just go on the glossary. There was never any plan for what would go there. He would do a deep dive on what we needed to rank for and then generate the content. It wasn't like a structured "what should go where" approach. We've got resource hub for learning how to buy something or why you would buy something. And the Learn center and tutorials are how to do a thing with it, not related to buying it.

**Aida Knežević:** Is anybody working on the glossary right now?

**Fung-Lin Wu:** Alexis, have we posted anything on the glossary lately?

**Alexis Ruiz-Pedregon:** The last one we did was "what is database," one of the memo database ones, but that was maybe a month ago and was the first one we had posted in a while. We've mostly been posting on the blog.

**Aida Knežević:** That is something to consider for where we will publish our content. If you want to have a separate section on your blog for content that's more SEO focused, it's not going to be glossary style always, but it does fit in with what you've been publishing lately. The more AI-related topics have been published on the blog, but it's something to consider if you want to divide the blog in the future.

**Aida Knežević:** The clusters we have right now — the six — map quite well to what competitors are covering. We're making sure to capture search traffic while also building on additional topics for Redis. Last week we focused primarily on keyword research based on the content strategy. The keyword research process is very manual. We use keyword gap analysis with your competitors to understand where opportunities are, and we also try to understand the use cases of your product, the pain points of your audience, and map them to search queries. We use SEMrush to do keyword research and then upload all of those keywords into our platform, Atlas.

**Aida Knežević:** We have a workflow that takes a keyword, connects to the SEMrush API, analyzes the top-ranking content, and then generates a title as a starting point. The title is almost always changed once we pick an assignment and start working on it. We adjust the title based on the outline and what's currently ranking on the SERP. This expedites the ideation process because sometimes we're generating 50 to 60 ideas at a time.

**Aida Knežević:** This is your content calendar — we call it a content OS. It's an Airtable base that you all should have access to. There are three different views: ideas for review, drafts for review (empty for now), and published docs. We also have editor views that we use internally to track the status of individual assignments. The topic cluster view includes a list of the clusters along with a description. The URL tab includes the keyword gap analysis. You can see all of the organic and direct competitors we researched and the keywords — there are about 11,000 of them mapped to URLs so it's easier to parse through.

**Aida Knežević:** Right now we have 71 assignments ready for your review, grouped into individual clusters. It's a mix of foundational content focused on "what is" or "how to," but we also incorporated middle of the funnel and bottom of the funnel assignments. For example, in the Industry Solutions cluster, we have ideas like "optimize payment processing," "automate sales processes," and "fintech app features." These map to use cases where companies use Redis to modernize their apps and improve app performance. We also have an assignment on how to improve the user experience on your app, where we could talk about Redis and how to improve responsiveness. And there are topics around LLMs like context rot, context window management, and how to optimize token usage when using different LLMs. We try to get a mix that allows us to get search volume, further develop authority, and explore additional topics in detail.

**Fung-Lin Wu:** This is very helpful. For next steps, where should we be marking what is approved, not approved?

**Aida Knežević:** In Airtable, you should have commenting access, so you can expand a record and leave a comment or just leave an emoji like thumbs up or thumbs down.

**Alexis Ruiz-Pedregon:** Could there also be maybe a column added where we can check a box? Maybe that might be easier. I don't know if Airtable would allow that with our access.

**Aida Knežević:** It does not, but I will add it. Let me know if it works because Airtable has been limiting how much people can do with just commenting access because they want people to pay for seats. Let's try to do a checkbox and let me know if you're able to use it.

**Alexis Ruiz-Pedregon:** Do we have access to the table yet?

**Aida Knežević:** Yes, you should have. I linked it in the agenda. Feel free to tag me in your comments so I get an email notification. Like I said, this is not the final calendar. The calendar is something that we iterate on. Any ideas that you feel like aren't something you want to talk about or are too general, just let me know. Or if there are topics you were hoping to see that we haven't added, let me know and we'll do additional research. This is just a first pass to show you all of the options that we're thinking about.

**Alexis Ruiz-Pedregon:** We'll definitely have to comment. I just tried to click on the checkbox column, so we'll comment.

**Aida Knežević:** Once you review the assignments, we want to generate a blog. Considering you already have content on your website, we can also pick an existing blog post and refresh it. The first blog doesn't have to be something we publish right away. It can be an existing blog post or one from the list we're suggesting. We generate it primarily to align on voice and tone. It's very important to get that right and make sure it follows the brand, but we also want to make sure the information depth is right and the product messaging is correct.

**Aida Knežević:** We have the company context to guide the LLMs on how to talk about Redis, but if that proves not to be enough, we can add an additional step in the article generation pipeline that verifies product claims. We can give it a completely different artifact that covers all the different aspects of the Redis platform and breaks down all the different features, and it uses that artifact to fact-check any product mentions. We can see with the initial first couple of articles if the article generation pipeline is doing a good job.

**Aida Knežević:** I'm also working on your content audit. I started that last week, but we're focusing primarily on keyword research right now. I am going through your glossary traffic performance and blog performance over the last six months to identify which articles are the biggest losers and what we can refresh and optimize. I'm hoping to get you that next week.

**Alexis Ruiz-Pedregon:** Would we focus on refreshes first and then new blogs? How do you suggest we prioritize them?

**Aida Knežević:** For the first couple of weeks, the purpose of this first phase is to really nail the voice and tone and make you comfortable with the content. I do recommend starting with new content first. Once we get into a steady state, it can be a combination.

**Aida Knežević:** I'm also going to work on a potential seventh cluster focused on cache modernization. I requested access to the doc but don't have it yet.

**Fung-Lin Wu:** You don't have access?

**Alexis Ruiz-Pedregon:** I think Katie might have added that one.

**Fung-Lin Wu:** Let me see if I have access. I'm just checking what it is.

**Alexis Ruiz-Pedregon:** We're on this doc too, Aida. Below on the very bottom, I added some traffic data for the last 12 months. I did the `/learn` subdirectory on the first table, and then the top 10 blog posts by session. Those are also the most sign-ups and browsers we've received.

**Aida Knežević:** This is helpful. Okay, totals are fine. It's just to understand what to prioritize for refreshing and helps with prioritizing new topics. Sometimes blogs you think won't get a lot of sign-ups do.

**Fung-Lin Wu:** I can see the doc but don't have access to it.

**Aida Knežević:** I'm asking the person who owns it to give you access. All right, I think those are all the updates I had this week. We are working on setting up your Looker dashboard with your Search Console and Google Analytics 4 data that should be ready this week. I'll share that when it comes in.

**Fung-Lin Wu:** On our end, we still have items pending. I believe Allison reviewed the writing guidelines already. Cody and I have been away due to an off-site. We still have the audience personas and company context documents to look through, and reviewing the content calendar.

**Aida Knežević:** Yes, I think that's all that's pending because the writing guidelines — we went through them today and handled all of the comments.

**Fung-Lin Wu:** Perfect.

**Aida Knežević:** I'll wait for your feedback on the content calendar. Let me know if you have any questions in the meantime.

**Cody Henshaw:** Awesome.

**Aida Knežević:** Thank you.

**Alexis Ruiz-Pedregon:** I'll see you next week. Thank you.

**Aida Knežević:** Thank you. Bye.
