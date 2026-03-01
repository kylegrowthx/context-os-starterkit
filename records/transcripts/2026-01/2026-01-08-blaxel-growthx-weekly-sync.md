# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-08
time: 19:29 UTC
duration: 39 minutes
organizer: Kathy Lam (GrowthX)
participants:
  - Paul Sinaï (Blaxel, CTO/CEO)
  - Aida Knezevic (GrowthX, Senior Editor)
  - Nicolas Lecomte (Blaxel, Product/Engineering)
  - Kathy Lam (GrowthX, Account Lead)
  - William Leborgne (GrowthX, Developer)
fathom_recording_id: 112874348
fathom_url: https://fathom.video/calls/524334765
share_url: https://fathom.video/share/CCLDs_AoCjs2S2fcXzyXzBxScj65RRTK
source: fathom
enriched_on: 2026-02-28 11:37 UTC
</metadata>

---

## Summary

GrowthX approved the "Browser Sandboxing" article for publication this week and demoed its Atlas AI platform, which uses research, drafting, and fact-checking workflows plus a "Products & Services" artifact to prevent AI hallucination. Blaxel confirmed the next batch of five article topics (including "Got Sandbox," "Moodle Cost Comparison," and "What is Tenant Isolation?") to build topical authority, while GrowthX committed to providing AI visibility reports and PostHog access to replace Blaxel's canceled Profound subscription.

---

## Context

This is a weekly sync between GrowthX and Blaxel to align on content production, Atlas platform capabilities, and reporting infrastructure. Blaxel is GrowthX's primary SaaS client on a content marketing engagement; the goal is to build topical authority in the browser sandboxing, compliance, and infrastructure spaces through high-quality, AI-assisted content that drives product adoption. The relationship is in active production phase: the first article (Browser Sandboxing) is ready to publish, three more drafts are under review, and the workflow has stabilized enough to plan the next five topics.

Key business drivers for Blaxel: demonstrating thought leadership, establishing SEO presence in competitive keywords (difficulty <40), and building a content engine that scales. GrowthX's Atlas platform is the execution layer, automating research via EXA, drafting, and fact-checking while maintaining accuracy through human review and product-specific artifacts. Reporting is shifting from Blaxel's own Profound subscription to GrowthX's internal AI visibility platform (still in development) and PostHog for traffic metrics.

---

## Relevance

- **Content Strategy & SEO**: Blueprint for topical authority approach, keyword difficulty thresholds, and content mix (awareness + lower-funnel comparison). Reusable framework for future client engagements.
- **Atlas Workflow & AI Guardrails**: Deep dive into agentic content generation, EXA-powered research, fact-checking with cautious language flags, and artifact-based accuracy checks. Demonstrates how to prevent AI hallucination in product mentions.
- **Client Operations**: Example of sync cadence, artifact management (Products & Services matrix), cross-functional handoffs (GrowthX to Blaxel), and status change permissions. Model for ongoing client engagement post-contract signature.
- **Reporting & Analytics**: Transition from third-party (Profound) to internal tools (GrowthX AI visibility + PostHog). Addresses client pain point of visibility while platform is under development.
- **Product Feedback Loop**: Mechanism for Blaxel to notify GrowthX of roadmap changes via Slack/Notion. Important for keeping artifact data fresh and preventing obsolete product claims in content.

---

## Overview

- **First Article Approved:** The "Browser Sandboxing" article is approved for publication this week. GrowthX will handle staging in Strapi and will use the selected "speed gauge" cover image.
- **Atlas Demo:** GrowthX demoed its internal Atlas platform, which uses an agentic workflow (research, draft, fact-check) and a "Products & Services" artifact to prevent AI hallucination about Blaxel's capabilities.
- **Next Topics Set:** The next batch of articles is confirmed: "Got Sandbox," "Moodle Cost Comparison," "What is Tenant Isolation?," and two other comparison articles.
- **Reporting Access:** GrowthX has PostHog access for traffic tracking and will provide regular AI visibility reports, replacing the need for Blaxel to resubscribe to Profound.

---

## Key Topics

### First Article Review & Publication

  - **Feedback:** The "Browser Sandboxing" article was approved. The initial opener, which felt "clickbaity," was improved to better match the article's high quality.
  - **Cover Image:** The "speed gauge" design was selected.
      - **Action:** GrowthX to ensure the Blaxel logo is not cropped by the website's asset format.
  - **Publication:** GrowthX will publish the article this week.
      - **Process:** Stage content in Strapi → Tag with "guides" → Notify Blaxel via Slack.

### Atlas: AI Content Generation Process

  - Aida demoed the internal Atlas platform, detailing its agentic workflow:
    1.  **Assignment Direction:** Manual research defines the article's structure, required topics, and a unique Blaxel angle.
    2.  **Research:** An EXA-powered agent finds high-quality sources, including gated reports, and provides links for verification.
    3.  **Drafting:** The initial draft is created, followed by manual internal linking and source citation.
    4.  **Fact-Checking:** An agent verifies claims against the research. Unverifiable claims are rewritten with cautious language (e.g., "While industry best practices support this claim...") to flag them for human review.
    5.  **Blaxel Mention Validation:** A "Products & Services" artifact ensures AI accuracy by preventing it from hallucinating features Blaxel doesn't have.
  - **Artifact Updates:**
      - Blaxel must notify GrowthX (e.g., via Slack, Notion tag) of any product or roadmap changes to keep the "Products & Services" artifact current.

### Reporting & Analytics

  - **AI Visibility:** Blaxel canceled its Profound subscription, expecting GrowthX to provide this data.
      - **Solution:** GrowthX will provide regular AI visibility reports. Direct user access to the platform is in development.
  - **Website Traffic (PostHog):** GrowthX has access to PostHog (`team@growthxlabs.com`) and will create views to track blog traffic.

### Next Article Topics

  - **Strategy:** The goal is to build topical authority.
      - **Method:** Target keywords with a difficulty score under 40.
      - **Mix:** Combine high-volume awareness topics with lower-funnel, ICP-relevant comparison articles.
  - **Approved Topics:**
      - "Got Sandbox"
      - "Moodle Cost Comparison"
      - "What is Tenant Isolation?"
      - Two other comparison articles
  - **Rejected Topic:** "Lambda GPU Support" was deprioritized.
      - **Rationale:** Blaxel does not offer GPU support, so the topic wouldn't drive product adoption.

---

## Action Items

**Kathy Lam (GrowthX)**
- Publish 'Browser Sandboxing' in Strapi; tag "Guides"; Slack Nicolas/Paul; verify Blaxel logo is not cropped in asset format; set PostHog views; send reporting links
- Check Notion for Products & Services artifact; add if missing
- Replace 'Lambda GPU support' with 'What is Tenant Isolation?' in next batch; send topic list to Nicolas/Paul
- Build approval interface with Carly; enable Nicolas/Paul to change draft statuses directly (vs. commenting)

**Nicolas Lecomte (Blaxel)**
- Add Kathy to Blaxel newsletters and internal messaging for product updates
- Confirm PostHog edit access for team@growthxlabs.com; notify GrowthX if permissions issue persists

---

## Transcript

### Opening: Note-Taking Alignment (procedural—removed)

### First Article Feedback & Publication Workflow

**Nicolas Lecomte (Blaxel):** Yeah, honestly, the Browser Sandboxing article was really good. The tone and depth were exactly what we wanted—filled with factually correct information. My initial feedback was that the opener felt a bit clickbait, but I saw you've already fixed that. The rest was really strong.

**Kathy Lam (GrowthX):** We moved quickly on the opener so we'd be quoted by search engines immediately, but I agree making it meatier was crucial. We've systemized that feedback and will apply it to the next three articles.

**Aida Knezevic (GrowthX):** For publishing, we have Strapi access and can stage the content directly. We'll tag it "Guides" and notify you via Slack.

**Nicolas Lecomte:** Great. We'll place it on the blog. You should tag these with "Guides" and we'll handle the visual separation from our engineering blog.

**Kathy Lam:** Excellent. Now let's review the cover images—which resonates most?

**Paul Sinaï (Blaxel):** I like the speed gauge option. Clean and relevant.

**Nicolas Lecomte:** I agree. Good choice. But be careful—the asset format on the main page might crop the Blaxel logo. The image focuses on the center, which could cut it out.

**Kathy Lam:** Good catch. I've seen that issue before with that ratio. We'll verify it doesn't happen.

---

### Atlas Platform Demo: Agentic Article Generation Workflow

**Kathy Lam:** Should we dive deeper into how we generate articles through Atlas?

**Nicolas Lecomte:** We only had a brief overview during sales conversations, but never a full demo. I'm interested.

**Aida Knezevic:** So Atlas is our internal agentic article generation platform. You have one workflow set up for now—we call it V1 because we iterate constantly. Every client is unique in industry and content requirements, so we tailor workflows. For specialized content types like comparison articles, we sometimes create separate workflows.

**Aida Knezevic:** All our artifacts live here—company context, audience personas, proofreader checklist. The Products & Services artifact is critical: we don't want Atlas relying on third-party information about Blaxel. We feed it internal documentation so content is accurate.

**Aida Knezevic:** Here's how the workflow breaks down. First, Assignment Direction: we manually research your topic on Google and list what the article must cover. We say: don't limit yourself to these topics, but this is the minimum. We specify unique Blaxel angles and what the conclusion and FAQ should include. Most LLMs don't know what good article structure looks like—they don't go to Google's first page and ask "What should this cover to rank and meet search intent?"

**Aida Knezevic:** Second, Research: we use EXA, which is more powerful than Perplexity. It finds high-quality information, even in gated PDFs. It creates research questions for each topic, finds answers with links, and summarizes findings. If we can't verify a stat, we either find a way to access the source or we remove it.

**Paul Sinaï:** So EXA also does OCR and PDF analysis?

**Aida Knezevic:** Exactly. It's crucial for finding verified, high-quality research.

**Aida Knezevic:** Third, Drafting: the agent creates the initial draft using writing guidelines. We reserve intense edits for the end—we just check structure and assignment alignment. Then we add internal links programmatically or manually, plus source links for any statistics or third-party claims. All links go to official documentation, peer-reviewed research, or authoritative sources—never competitors or promotional content.

**Aida Knezevic:** Fourth, Fact-Checking: the agent breaks the draft into chunks, extracts key passages, asks questions about each, and verifies against the research. If something's wrong, it rewrites it. If it can't verify something 100%, it signals that with cautious language like "While industry best practices support this claim, there's no third-party research confirming..." That's our signal for human review.

**Aida Knezevic:** Fifth, Blaxel Mention Validation: this step compares every Blaxel mention against your Products & Services matrix to prevent hallucination. AI doesn't intentionally make things up, but it can infer things from tone. For example, with Hex, we tried a conversational tone, but the AI started dropping information depth. We had to ensure it wasn't assuming Blaxel has features just because competitors do.

**Paul Sinaï:** How do we update the Products & Services artifact? Should we feed you our roadmap, blog posts, or internal docs?

**Aida Knezevic:** Your Notion base should include the artifact—it's like a feature matrix. If it's not there, we'll copy and paste it. Whenever you update it, just tag us in Notion or Slack. We'll sync it to Atlas. Format doesn't matter—blog posts, PDFs, internal docs, visuals—as long as it's not a video.

**Kathy Lam:** Just Slack us and I'll get added to your newsletters so I catch product updates.

**Paul Sinaï:** On our side, we need to make sure this info is well-framed and communicated. That's a separate challenge we're working on. But what you're doing here can really influence the content, so we need to stay on top of it.

**Aida Knezevic:** From experience, a lot of product feedback comes during the calibration phase, especially when we start competitive keywords. You'll probably have feedback on how we position Blaxel. That's part of the process.

**Paul Sinaï:** After onboarding, how does the update rhythm work throughout the year? Do we use Slack, give you newsletters?

**Aida Knezevic:** You have an editor assigned to your account who generates content and updates artifacts. When you comment on a draft, if it's broader feedback, they update everything accordingly. You can communicate over Slack or meetings. Their job is to stay on top of artifacts and keep them accurate.

**Nicolas Lecomte:** If I update the feature matrix in Notion directly, do you automatically sync from Notion to Atlas, or should I ping you separately?

**Aida Knezevic:** You can tag us in Notion. Unfortunately, Notion and Atlas don't speak to each other yet, so we need that manual notification.

**Nicolas Lecomte:** And do we get access to Atlas? I notice it might contain AI visibility data. I'm really interested in that view. We used to pay for Profound, but I thought you'd provide that data.

**Aida Knezevic:** Right now, the overview in Atlas is a placeholder. We're building an AI visibility platform internally that's in late development stages. You should have access soon.

**Kathy Lam:** I've been working to add your brand to our tool, but it's taking longer than expected. I've escalated it. It's more about giving you access to reports rather than direct user access to the platform, but I want to make sure you get regular updated reports. I don't want you picking up a Profound subscription again.

**Paul Sinaï:** Yeah, we'd rather avoid the recurring bill and setup hassle.

**Aida Knezevic:** There are two parts: Kathy is setting up your prompts in our tool so you get reports; user access is a separate thing in development.

---

### Reporting & Analytics: PostHog Access

**Kathy Lam:** For PostHog tracking—we're not installing GA4, so we're using your tool. Can you set us up with access to create views? As we upload new blogs, we want to track traffic explicitly.

**Nicolas Lecomte:** I gave access to team@growthxlabs.com. You should have your own PostHog project.

**Kathy Lam:** And we can create views and reports from that?

**Paul Sinaï:** You have your own instance.

**Nicolas Lecomte:** You should have permissions. PostHog can be finicky with access control—sometimes there are quirks. Let me know if you can't edit, and I'll fix it.

**Kathy Lam:** Perfect.

---

### Next Article Topics: Topical Authority Strategy

**Kathy Lam:** For the next set, we're thinking about five articles. How does this look?

**Paul Sinaï:** "Got Sandbox" is great for next. "Moodle Cost Comparison" is interesting. "Lambda GPU Support"—it's interesting, but not a priority. If people are searching for GPUs and we don't offer GPU support, I don't see how that drives product adoption. I wouldn't prioritize it.

**Kathy Lam:** Let me pull up the backlog and find a replacement. What about "What is Tenant Isolation?" That's more aligned with your ICP.

**Paul Sinaï:** Yes, that's better. Tenant isolation, code execution, sandboxing—those topics matter for our buyers.

**Nicolas Lecomte:** Maybe something on security like SOC 2?

**Paul Sinaï:** Let's focus on what drives product understanding first.

**Kathy Lam:** Our strategy is to build topical authority by targeting keywords under difficulty 40. We're mixing high-volume awareness topics with lower-funnel, ICP-relevant comparisons. That balance is working.

**Paul Sinaï:** How do you prioritize when scheduling publication—keyword difficulty or search volume?

**Kathy Lam:** We're deliberately mixing both. Higher awareness pulls high volume; comparisons target your ICP. We're tilting slightly toward awareness while keeping comparison articles that matter to your buyers. We're not doing just top-of-funnel—we're also hitting lower-funnel, ICP-relevant topics.

**Nicolas Lecomte:** Sounds good.

**Kathy Lam:** Once we raise your topical authority score, we'll target higher difficulty keywords. For now, we're building authority in topics where you can become the leader.

---

### Approval Workflow & Status Permissions

**Nicolas Lecomte:** So we have three articles to review. Will you publish to Strapi or should we?

**Aida Knezevic:** We can handle publishing as well.

**Paul Sinaï:** Just Slack us when it's live.

**Kathy Lam:** Also, Nicolas, I know you've been leaving comments on drafts. You should be able to change statuses directly instead of commenting.

**Paul Sinaï:** I tried that but it didn't work.

**Aida Knezevic:** You have commenting access, not status-change access. Kathy, we can build an interface with Carly. She's creating interfaces that let commenting-access users change statuses directly.

**Paul Sinaï:** That would be easier—just approve it directly rather than commenting and having you parse the feedback.

**Kathy Lam:** I'll check with Carly on getting that access set up.

---

### Closing

**Kathy Lam:** Once you have PostHog dashboards or analytics views set up, let us know.

**Paul Sinaï:** Including PostHog, once that's done.

**Kathy Lam:** Perfect. Thanks so much.

**Aida Knezevic:** Thank you.

**Nicolas Lecomte:** Bye.

**Paul Sinaï:** Thank you, guys.

**Kathy Lam:** Have a great one. Bye.
