# CI: Marcel / Georgemaine

<metadata>
date: 2025-06-25
time: 16:03 UTC
duration: 21 minutes
organizer: Marcel Santilli
participants: Georgemaine Lourens, Marcel Santilli
fathom_recording_id: 70486624
fathom_url: https://fathom.video/calls/334780078
share_url: https://fathom.video/share/VbgGhPLYZ6UxtcYeUhwwxBt8erJY13u8
source: fathom
enriched_on: 2026-03-03 00:22 UTC
</metadata>

---

## Summary

Marcel and Georgemaine discussed content inventory strategies for Atlas, GrowthX's content analysis and planning platform. Marcel outlined how to consolidate SEMrush and Airtable workflows within Atlas by focusing the MVP on the post-setup experience rather than self-serve configuration, and demonstrated his approach to content tagging, opportunity clustering, and assignment creation using Engine as a worked example. The team agreed that configuration and taxonomy design should be done by GrowthX experts (not self-serve), with automated tagging of large content volumes, and that opportunity scoring should combine relevance, search volume, and keyword difficulty into a single 0-100 score for prioritization.

---

## Context

This is an internal GrowthX strategy call between Marcel Santilli (CEO/product builder) and Georgemaine Lourens (Atlas team). Georgemaine had previously reviewed a product concept doc from Renato about content inventory features and wanted Marcel's input on how to translate his current manual Airtable workflows into automated Atlas features. Marcel is the expert practitioner on this workflow—he's been using SEMrush and Airtable together for years to deliver GrowthX's content strategy consulting—so this call captured his thinking on what should be replicated in Atlas versus what can be left as expert configuration outside the UI. The context is Atlas's product evolution toward handling content planning end-to-end, starting with MVP positioning focused on the monitoring and analysis experience once a site's content is properly set up.

---

## Relevance

- **To CheckThat / Atlas Product:** MVP scope decision to focus on post-setup monitoring experience rather than self-serve site configuration UI (defer complex setup to manual/expert workflow). Confirmed opportunity scoring framework combining relevance, volume, and difficulty into 0-100 scale. Content tagging taxonomy should be admin-configured, not user-facing, with automated LLM-based classification for bulk content items.

- **To GrowthX Delivery:** Marcel's current workflow (SEMrush for competitive research + Airtable for clustering and tagging) will be consolidated into Atlas, reducing tool switching. Validated that the core value is in post-analysis (page monitoring, assignment tracking, performance trending) rather than complex setup. Engine is established as the reference client/dataset for prototyping (already has clusters and assignments, good volume of existing pages for live analysis).

- **To Business Development / Account Health:** Engine flagged as a mature opportunity for Atlas pilot—they have assignments being hand-curated by the team and substantial existing content, making it ideal for validation. Interwell mentioned as secondary reference (ketamine-assisted therapy verticals, working examples of personas and content themes). Growth potential in expanding this workflow to other accounts once Engine validates the approach.

---

## Overview

- Content inventory process involves two main components: site analysis (sitemap/subdirectories) and competitive research
- MVP focus should be on core experience post-setup, not on creating a complex self-serve setup process
- Tagging system crucial for categorizing content and communicating content strategy
- URL-based keyword clustering is an efficient shortcut for assignment creation and opportunity analysis

---

## Key Topics

### Current Workflow and Tools Replacement

  - Replacing SEMrush and Airtable functionalities within Atlas
  - Concerns about replicating SEMrush's data capacity in Atlas
  - Marcel's custom Airtable workflows are complex but manual; focus on replicating core functionalities

### Content Inventory Process

  - For sites with many pages: analyze sitemap, identify evergreen content and relevant subdirectories
  - Monitor page performance, rankings, and enrich with LLM queries over time
  - Track impact of work on client's metrics (e.g., 40 refreshes out of 1000 URLs)

### Tagging and Metadata Enrichment

  - Create custom classifiers and taxonomies for content categorization
  - Tag both assignments and pages based on research and client needs
  - Examples: topic clusters, group types, personas, content themes
  - Automate tagging for large volumes (e.g., 5000 items) with human review capability

### Competitive Research and Keyword Analysis

  - Conduct keyword gap analysis between competitor domains and client's domain
  - Use competitor URLs as shortcuts for keyword clustering
  - Example: 1000 potential assignments totaling 5 million searches/month for Interwell

### Assignment Creation and Scoring

  - Use URL-based keyword clusters to define assignment keywords
  - Calculate opportunity volume and average difficulty from keyword data
  - Incorporate existing scoring frameworks (e.g., lead generation value, persona fit, search intent)
  - Develop an opportunity score (0-100) based on relevance, volume, and difficulty

### Data Visualization and Insights

  - Monitor page performance, titles, rankings, and traffic
  - Provide insights on content themes, audience groups, and topic clusters
  - Enable custom attribute addition and data shuffling for flexible analysis

---

## Action Items

**Georgemaine Lourens (GrowthX)**
- Obtain Engine dataset from Marcel and use it for content inventory prototype/analysis

---

## Transcript

**Marcel Santilli:** Just one minute. I need more coffee. The coffee grinder was jammed, and I just fixed it.

**Georgemaine Lourens:** That's fine. I'll go grab my airbox.

**Marcel Santilli:** I'll be back. This meeting is being recorded.

**Marcel Santilli:** How are you?

**Georgemaine Lourens:** Yeah, I'm doing really well. How are you? Are you feeling confident for your meeting with Augment Code?

**Marcel Santilli:** Yeah, yeah, feeling really good.

**Marcel Santilli:** Great job on the work and the site is looking so good.

**Marcel Santilli:** I'm just like, let's get it out, get it out.

**Marcel Santilli:** It's less like, it's more of a...

**Marcel Santilli:** Telling Jason, when it's a brand new domain, it takes a long time to get indexed, and so you just want to get it out, even if it's rough, like nobody's going to see it anyways, like the first day, but obviously we're doing a product-like launch as well, so it'll be fun tomorrow to kind of like brag about it a little bit, but it looks really beautiful, so great job there.

**Georgemaine Lourens:** What time do you have your meeting with the team?

**Marcel Santilli:** In 24 minutes.

**Georgemaine Lourens:** Okay, I won't keep you that long.

**Georgemaine Lourens:** So I wanted to chat with you and pick your brain about content inventory.

**Georgemaine Lourens:** Obviously, Renato walked me through his ideas, and he wrote a doc, and I went through it.

**Georgemaine Lourens:** Because you're kind of like the superpower, I kind of want to get your thoughts as well, especially around kind of like how your current workflow goes, because the way that I understand it now is that we're basically going to...

**Georgemaine Lourens:** We replaced, say, SEMrush and Airtable, and then kind of, like, do it all within Atlas.

**Marcel Santilli:** Yeah.

**Georgemaine Lourens:** And obviously some question marks there, because SEMrush, like, do we even have the capacity to get all of the data that they can give you into Atlas?

**Georgemaine Lourens:** And the second thing is, like, I watched you go through Airtable, and, like, you're a magician there.

**Georgemaine Lourens:** Like, you're doing so many things, and I think, like, that's so great.

**Georgemaine Lourens:** But on the other hand, like, it's highly custom stuff, right?

**Georgemaine Lourens:** Like, you're adjusting keywords in Airtable, mixing them up, clustering them all.

**Georgemaine Lourens:** Like, what are your thoughts on bringing over that functionality over to Atlas?

**Georgemaine Lourens:** Or are you kind of, like, envisioning that we just do that in the background, and there's, like, no way?

**Marcel Santilli:** Yeah, I think it looks complicated because it's so manual, right? So normally what happens is you start with a lot of competitive research. There are kind of two sides to it.

**Marcel Santilli:** If a site has a lot of pages like Engine, you go through the sitemap and find the sections with evergreen content and relevant subdirectories you want to monitor. Like a tree—you see all the subdirectories, each with X number of pages, and ideally the user selects which ones to index.

**Marcel Santilli:** The MVP focus is less about getting the setup right. Assume the setup is done by me or someone who can follow very complex instructions or an engineer. Creating a self-serve experience is too complex—we could spend six months and still not get it right. So assume we have a really good experience once it's all set up. Then what you want to be able to do is monitor what's happening with your pages.

**Marcel Santilli:** Like, so a lot of this is like, it's just an inventory of like, these are your pages.

**Marcel Santilli:** These are the titles of the pages.

**Marcel Santilli:** These are the like, how well this page is doing.

**Marcel Santilli:** And in all of these, it's like, what keywords this page is ranking for, you know?

**Marcel Santilli:** And over time, we can start to enrich it with more things around like, let's say like LLM queries, you know?

**Marcel Santilli:** So that's the inventory piece. These are all the URLs we're monitoring, the ones we refresh—the ones that have assignments behind them. The reason we want to know is because if they have a thousand URLs and we've done 40 refreshes, over time we want to know the impact our work has had on their numbers.

**Georgemaine Lourens:** So just from my understanding, like we're now at the stage where you already ran a query on the domain and you kind of like got the output as CSV or you just basically got it to Airtable.

**Georgemaine Lourens:** And now we're just kind of like syncing and just constantly watching like, hey, how is it performing?

**Marcel Santilli:** And maybe you want to add an attribute or kind of like change or shuffle around.

**Marcel Santilli:** But this part is basically after we got all of this sitemap data from SEMrush.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** I have the V0 and Lovable prototypes showing how pages look over time and serve more insights. The goal is to know if something needs to be changed—how to tag pages by last change, versions, traffic, word count. We're also trying to create clusters where you can categorize and enrich the metadata.

**Marcel Santilli:** There are concepts like topic clusters. For Engine, they care about group types—their audiences like sports teams, construction crews, disaster relief crews. They want to tag content by industry and group type. You can also tag by personas and different categories. The idea is to tag both assignments and pages, define the taxonomy, and build an opportunity list.

**Marcel Santilli:** Take Interwell as an example. I'm building an OS for them in shaping phase. The content themes are Academy and Assistive Therapy with breathing techniques. The audience groups are caregivers, elderly, family members, first responders. For each, you see topic, content theme, condition, treatment approach. This is a custom AI column tagging content based on categories. We scrape content once, not five times a day, and have SEMrush data via API to classify categories and subcategories given the page context. You essentially get custom classifiers. The data model and taxonomy are set at the admin level by GrowthX based on research, then assignments and pages get tagged by this taxonomy—that's how you communicate content strategy.

**Georgemaine Lourens:** This part definitely needs human review, right?

**Marcel Santilli:** So the tagging piece—coming up with the list—should be us carving it. We should configure the tags, but tagging 5,000 items should be automated with the ability to edit them. It's like creating a taxonomy: tag groups, sub-tags, tag categories.

**Marcel Santilli:** Then the other part is the external part.

**Marcel Santilli:** The way we've been doing it is you have the context and understanding of their users and business. Interwell is a therapy platform focused on ketamine-assisted therapy. Like Hone for hormone therapy, they pair users with a psychiatrist for therapy. Competitors include Mindbloom and Growth Therapy. You come up with topics based on personas and audience groups, then search those. For example, licensed clinical social worker (LSUW). You find references like Growth Therapy that have good related content. Then the shortcut to find all these is doing keyword gap analysis between competitor domains and the client's domain.

**Marcel Santilli:** So we did a keyword gap analysis between competitor domains and the client's domain, found 1,000 potential assignments totaling 5 million searches per month. For example, 200,000 people search for depression ICD-10 codes monthly. You can take a competitor URL like Growth Therapy and create an assignment from it—much easier than clustering 500 keywords manually. URLs give you the clustering shortcut. For example, if a competitor URL ranks for 49 keywords, that becomes your assignment's keyword cluster. You sum up the search volume and average the difficulty to get opportunity volume and difficulty scores. So a cluster with 1,300 total volume and average difficulty of 16 is super easy to tackle. That's how we create an inventory of relevant opportunities.

**Georgemaine Lourens:** Okay.

**Marcel Santilli:** Right now, assignment creation already gives you scoring—lead generation value, persona fit, search intent match. The idea is taking that scoring plus opportunity volume plus keyword difficulty and combining it into an opportunity score, 0-100, based on relevance times volume times difficulty.

**Georgemaine Lourens:** That makes sense. Something that would be super helpful is to have at least one dataset to work with. Do you have a particular client in mind, like Augment Code?

**Marcel Santilli:** Engine is probably the best. We're hand-carving every assignment, tagging it by cluster. It's not overly produced, and they have a lot of pages already.

**Georgemaine Lourens:** That would give a nice internal dataset. Thank you—this is more than helpful. I'll let you go and ping you with more questions.

**Marcel Santilli:** Sounds good.

**Georgemaine Lourens:** Thanks. Talk soon. Bye.
