# Checkthat Overview

<metadata>
date: 2025-11-26
time: 19:00 UTC
duration: 37 minutes
organizer: Marcel Santilli (GrowthX, CEO)
participants:
  - Marcel Santilli (GrowthX, CEO)
  - Talal Syed (GrowthX, CheckThat lead)
source: fireflies
fireflies_id: 01KAWE62M41R6PPXWZSY9VX2D5
transcript_url: https://app.fireflies.ai/view/01KAWE62M41R6PPXWZSY9VX2D5
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Onboarding call with Talal joining as CheckThat lead. Marcel outlined CheckThat's core strategy: standardized, data-driven category research that separates real AI behavioral shifts from visibility-tool noise. Talal will immediately upload prompts for critical clients (Augment Code, Lovable) to begin data collection; the team agreed evaluation and comparison stages are highest ROI. Critical blockers: SEO indexing (pages not ranking), prompt methodology standardization using persona-driven frameworks, and immediate workspace setup before data becomes irreplaceable.

---

## Context

This is a strategic onboarding call for Talal Syed, who recently joined GrowthX to lead CheckThat product development. Talal previously knew GrowthX through Marcel's public LinkedIn presence and had followed the company's workshops and building-in-public approach. CheckThat is GrowthX's strategic software bet: a B2B visibility and decision-support platform that uses standardized category frameworks, LLM prompting, and large-scale experimentation to answer the question "which AI service gives the best answer for [specific use case]?" across 1,200+ product categories and funnel stages. The core insight is that the market wrongly conflates AI behavioral change (real) with analytics visibility tools (often BS), and CheckThat aims to be the authoritative, data-backed research layer for B2B software buying. The conversation focuses on unblocking immediate data collection, establishing prompt methodology, and resolving SEO/indexing issues.

---

## Relevance

**CheckThat Product & Platform**
- Strategic platform architecture: separating behavior change narrative from visibility tools
- Category framework design (1,200+ categories vs. G2's 1,500; meaningful subset)
- Funnel stages (awareness → decision) and differential ROI by stage
- Data moat strategy: 128+ probes per category, $200K/month burn at scale
- SEO play: creating brand summary and comparison pages to rank for high-intent queries

**Immediate Execution**
- Prompt uploading for critical clients (Augment Code, Lovable) is time-sensitive
- Workspace setup and tagging/view features needed to organize prompts
- Bug fixes and reporting workflow (Linear integration)
- Notion access restrictions after data security incidents

**Methodology & Research**
- Persona-driven prompt generation (jobs to be done, fears, KPIs, skills, work products)
- Unified approach to avoid duplicated prompt creation across teams and clients
- Focus on evaluation and comparison stages (highest intent, brand mentions)
- De-prioritization of awareness, advice, and post-purchase stages

**Cost & Data Efficiency**
- Probe cost optimization: $0.06 per probe, potential reduction to $0.03
- Scheduling heuristics: daily probes for priority categories, less frequent for others
- Data collection timing: irreplaceable once missed; cannot backfill from third-party sources
- Relationship management with Scrunch (avoid alienation during beta)

**Thought Leadership & Market Position**
- Public launch strategy: validate with pilot customers first, then announce
- Research and study generation using large-scale experiments ($100K+)
- Targeted dev-rel outreach using 6-month data insights
- Building trust through standardized, transparent methodology

---

## Decisions & Commitments

**Talal Syed's Key Commitments**
- Immediately identify high-profile clients with Jason and Andy for prompt upload priority
- Begin uploading all prompts for Augment Code and Lovable into CheckThat workspaces within short timeline
- Develop and document AI-driven persona methodology for consistent prompt generation across categories and companies
- Create internal best-practice guide for prompt creation (audience, job description, fears, metrics, work products, etc.)

**Marcel Santilli's Key Commitments**
- Re-add Talal to CheckThat Notion doc and restore appropriate access permissions (after recent export incidents with departing staff)
- Confirm prompt uploading and execution workflow is functional; establish Linear-based issue reporting process
- Advise on SEO strategy for category and brand pages (H1 tags, page structure, ranking intent)
- Facilitate workspace tagging and view features to organize prompts and clients

**Team / Unassigned**
- Resolve SEO indexing issue (pages currently not ranking; need technical strategy)
- Continue conversations with Katya and recruit additional data scientists for predictive modeling of answer quality and category correlation
- Define and implement scheduling heuristics to optimize probe frequency and reduce $200K/month baseline cost

---

## Open Questions

- **SEO & Technical Strategy:** What is the correct page structure and H1 strategy? Should primary pages be "What are the best [category] tools?" (current approach), category overviews, or brand-specific pages? Why are pages not indexing?
- **Prompt Methodology Standardization:** What is the definitive best-practice framework for generating company-specific and subcategory prompts without duplication? How do we scale this across teams?
- **Workspace Tagging & Organization:** How should prompts be tagged, filtered, and visualized so Talal and customers can navigate thousands of prompts efficiently?
- **Data Collection Timing:** Which high-profile clients should be prioritized first for immediate workspace setup? (Augment Code, Lovable are explicit; others TBD)
- **Funnel Stage Value:** Is there trackable ROI for awareness and advice stages if brands are rarely mentioned? Should those be de-prioritized or shelved?
- **Scrunch Partnership Risk:** How much promotion can CheckThat sustain without triggering Scrunch to revoke platform access?
- **Cost Optimization:** What specific scheduling heuristics will reduce $200K/month burn without sacrificing data quality for evaluation and comparison stages?

---

## Action Items

**Marcel Santilli (GrowthX, CEO)**
- Re-add Talal Syed to CheckThat Notion workspace and restore write access for strategic docs (revoked after data export incidents)
- Validate prompt uploading and execution workflow in CheckThat admin panel; establish Linear-based issue reporting process with development team
- Partner with Talal on tagging, filtering, and view features to organize thousands of prompts by client, category, and funnel stage
- Provide SEO strategy guidance: validate H1 structure ("What are the best [category] tools?"), page organization, and technical indexing setup; diagnose current ranking issues
- Maintain CheckThat Slack channel presence and unblock Talal on platform decisions

**Talal Syed (GrowthX, CheckThat Lead)**
- Immediately identify and prioritize high-profile clients with Jason and Andy for prompt workspace setup (Augment Code, Lovable confirmed as critical)
- Begin uploading all existing prompts for Augment Code and Lovable into their CheckThat workspaces to activate data collection
- Document the persona-based prompt generation methodology (audience analysis, job definitions, fears, KPIs, metrics, work products) as best-practice guide for team
- Create standardized prompt templates for subcategory and company-specific prompts to eliminate duplication across teams and clients
- Manage workspace configuration, coordinate with teams generating new prompts, and flag issues through Linear

**Unassigned / Team**
- Resolve SEO indexing blocker: validate H1/page structure, check robots.txt, test crawlability, coordinate with Marcel on strategy
- Hire and consult with data scientists (continue conversations with Katya; expand team) to build predictive models for answer quality correlation and category ROI
- Define and implement scheduling heuristics to reduce $200K/month baseline probe cost without sacrificing evaluation and comparison stage data quality

---

## Transcript

**Marcel Santilli:** Hello, my friend. How's it going?

**Talal Syed:** Hey. It's going well. How about you? So glad to finally meet you.

**Marcel Santilli:** Yeah, yeah, you too. I'm hearing great things about you. Said you're here and helping us, and part of this. Man. How has it been so far for you?

**Talal Syed:** It's been great. Super interesting to see things in person. Like, I have been an admirer of GrowthX from a distance for a while, so it was really good to see we work together. So pretty excited.

**Marcel Santilli:** That's really cool. How did you first run into us out of curiosity?

**Talal Syed:** LinkedIn. I think you were pretty prolific on LinkedIn, just like sharing progress, building in public. Then you guys started doing a lot of workshops and I knew Jason just from LinkedIn as well, so I had lots of little touchpoints for you guys.

**Marcel Santilli:** That's really cool. Yeah, it's so funny because on the downside of building publicly, I see some of our competitors fundraising and then literally copying how we talk about things like Air Ops and others. They didn't even used to use the word context and now they're using the word context for everything. But on the flip side, there's so many people now like, man, I really want to work with you all in some capacity. And it's really, really cool. We just gotta keep moving fast, you know, because if you're building public, you better be moving fast because everybody knows everything you're doing all the time.

**Talal Syed:** I feel like it's built a lot of trust in the market for GrowthX, so I would see it as a net positive, at least from my perspective.

**Marcel Santilli:** That's awesome. And that's good to hear. Cool. Well, we'd love to spend some time and just take you through how we're thinking on CheckThat and the work we've done so far, and find ways to get you as involved as possible. Maybe we can start with the big picture. Have you had a chance to read the overview doc for CheckThat?

**Talal Syed:** If it's the one you shared in Notion a few days ago, then I did go through that.

**Marcel Santilli:** Okay, cool. I just dropped the link, but I think my access got removed again recently. So let me re-add you. We had some incidents where folks from the delivery team, after leaving, exported our entire Notion and shared with competitors. So I've been restricting access to strategic docs. Most editors don't need that information anyway.

**Talal Syed:** Okay, that makes sense.

**Marcel Santilli:** So at a high level, the main issue with how the AEO space is happening right now is that there are like 163 or 164 vendors conflating real behavioral change—driven by AI technology like ChatGPT—with visibility tools. That's different. Profound was smart to create that narrative. But they're very different things. What we're trying to do is separate the two. One is human behavior driven by technology. That's real. But many of these visibility tools are just BS. It's like asking every city to run their own election research instead of using standardized polling. What we're doing is standardizing that. We know it's not perfect science, but it's way better than the alternative.

**Talal Syed:** That makes complete sense.

**Marcel Santilli:** So when you think about the funnel stages: awareness and advice, evaluation, comparison, decision, and post-purchase. We decided to focus on B2B software first—that's most of our companies. We defined buying categories. G2 has 1,200 to 1,500. We did a whole exercise to come up with meaningful ones. We're creating the best questions that represent each category at each funnel stage. We're also studying the correlation between substance and citation likelihood to build a predictive model. Katya, a data scientist, is consulting with us. We're actively hiring more data scientists too.

**Talal Syed:** That's cool.

**Marcel Santilli:** Most brands coming in have to figure out questions from scratch, which is silly. The second problem is they're starting data collection from zero. What we're doing instead is saying: look, we're already collecting data. For example, we've done 128 probes on a category. If you sign up, you can add a shared library to your tracker and get all this data.

**Talal Syed:** Right.

**Marcel Santilli:** But here's the challenge: this is expensive. It's about $0.06 per probe across all our services. If you're doing 1,200 categories, 100 prompts per category, probing daily across five or six services, you're looking at about $200K monthly. That's significant. The key is making sure these questions are the best for each category. We prioritize the categories people actually buy from. Over time, we'll put some on different schedules—maybe every other day instead of daily, some weekly. We'll weight certain probes higher than others.

**Talal Syed:** That makes sense.

**Marcel Santilli:** For brands, our context generator is really good. If you look at LangChain, our workflow generates context and creates a summary that's way better than what you'd get from Scrunch or others. We're trying to create an SEO play. Semrush figured out the data moat but never did the SEO play. Crunchbase did. G2 did. We can't afford to buy clicks for B2B SaaS—they cost $20 a click. But because we're making this data available, if we have the surface area of brands and categories, we create a massive moat. We could rank for "LangChain pricing," "LangChain alternatives," etc. We become the best answer source and eventually a judge of which AI service gives the best answer. End users can see: "Claude versus Gemini versus ChatGPT—which has the better answer for MLOps platforms, and which ones are missing things?"

**Talal Syed:** I think this also provides a big moat if you turn it into research and studies. Not many companies run large-scale experiments costing $100K+. If you target dev rel, we could create a report using six months of data and do targeted outreach. Makes sense.

**Marcel Santilli:** That's a great idea. Yeah, you can come up with key insights and things like that. But here's the challenge—we effed up some stuff and none of the pages got indexed. I don't even know if they're indexing yet. So that's a big thing for us to solve. On one end, we need to set this up for success so it's truly an SEO play. What are the technical things we should do? Is our strategy correct? Right now, the H1 is "What are the best MLOps platforms?" Is that right? Or should it be categories or brand pages? There's a lot of that.

**Talal Syed:** Right.

**Marcel Santilli:** On the other end, we need a strong opinion and thought process on how we create the right questions. I saw the doc you started writing on that. Then we form a strong public opinion and dogfood the crap out of our own tools. The idea is we have different funnel stages, and we're trying to make this internal experience seamless. It's mostly working—just need to improve so we can add prompts, run probes, catch issues, and validate. The goal is to validate with a couple of customers first and work through rough edges. Once we feel good, we can give customers access. Then after a week or so, we can tell the whole world. Because the second we start promoting this heavily, it's going to hurt our relationship with Scrunch and others, and they might kick us off their platform. If our customers don't have all their data here and it's not collecting, then we lose what we're delivering.

**Talal Syed:** So we work closely on finding a place to upload prompts, document thinking, load workspaces, starting with critical customers like Augment Code and Lovable because they want to promote CheckThat?

**Marcel Santilli:** Exactly. We build workflows and iterate. We need to auto-generate a lot of these questions too. The admin panel is way more feature-rich than the public interface.

**Talal Syed:** Just a random question. Eventually, do we want to set up all clients within CheckThat? I know we had requirements for Augment Code where we needed prompts right away and duplicated work. When is that merger happening?

**Marcel Santilli:** Every day we don't put prompts for our customers in here is a day we're not collecting data. It's less about what you're showing them, it's more about if you come up with a thousand prompts—hopefully less—we should just put them all in here and make sure it's working. How we tag it, visualize it, show it can evolve easily. But if we're not collecting data, you can't go back in time. We won't be able to export data from other places like Scrunch. It's going to be messy. This is urgent. We've done high-profile work for Augment Code and Lovable. We should upload all those prompts now. Start collecting data now.

**Talal Syed:** One other question. I looked at the documentation on how prompts are populated. They're populated at a subcategory level. How do we do it for a particular company? There are category-relevant prompts, but some are only relevant to that company. So some are relevant to the product category, but some are only relevant to them as a company. We also want to populate those. I don't know if we have a way of generating those right now, and that seems like the biggest blocker to uploading prompts.

**Marcel Santilli:** Let's take Ramp as an example. You should be able to add custom prompts and select the funnel stage. I noticed the ones I uploaded yesterday haven't run—need to check why. We'll be able to create tags too. Just getting all the prompts in here will help. Come up with prompts, overdo it if needed—it should be easy. Copy and paste them per line, organize by funnel stage, create prompts, and it should work. We'll find bugs. There's one with line breaks creating issues. I flagged it. We can report feedback through Linear.

**Talal Syed:** Question about methodology. If you take 10 different people, they'll come up with 10 different prompt sets. We need an informed opinion on how to design custom prompts. Every board does it differently. Some use Scrunch, some use ChatGPT or Claude. What have you thought through? What's the best practice flow for creating prompts for subcategories? How can we apply that to individual companies without duplicating work?

**Marcel Santilli:** Fundamentally, the way to think about it is understanding the audience. We had to focus on category first because audience-based questions were hard. But audience-based questions seed the right questions. Jobs to be done, skills, backgrounds, work products. In awareness and advice, there's internal stuff: KPIs, metrics. That drives content strategy. External stuff: terminology, definitions, tools, templates, how-tos. For each funnel stage, come up with questions, but focus on higher intent and work backwards. If you start too broad, what value do you get? I did this for Ramp in the CFO club project. A finance manager at a fast-growing B2B startup. Write a job description. Think through their fears. What gets them fired or promoted? Who do they work with? What are all their questions around their job? Like: how can I automate financial reporting? How do I prepare a 409A evaluation? Who should I benchmark? How should I model sales capacity planning? What's the standard SaaS metrics dashboard? How do I calculate working capital requirements? What should my month-end close checklist be? These are high-quality questions. Then you go into Perplexity and type them in. But I don't know if there's value tracking this. Not many brands mentioned. It's more surfacing opportunities. In evaluation prompts further down the funnel, you see accuracy. Do we have good post-sales answers? But teams don't care much about post-sales. Evaluation is really important. Maybe we create comparison ones. I don't know how much value awareness and advice tracking have if there's no brands mentioned.

**Talal Syed:** For awareness, I think it's a one-off thing. The only thing we need to track is if a brand shows up as a cited source. If they see us mentioned when looking for solutions they might need a year down the line, it builds trust. But the ROI isn't there.

**Marcel Santilli:** Right. It drives traffic but brands won't be mentioned much. Sometimes it happens, but it's very minor.

**Talal Syed:** Similarly for post-purchase, I don't think it makes sense. Evaluation and comparison is where the money lies. I've been doing it by taking context artifacts, feeding them into Claude, creating a digital twin of the persona, then asking questions across specific features. If you were this persona and wanted this feature, what's the impetus to search? What language would you use? The results have been good.

**Marcel Santilli:** Yes. We can take that and create workflows to generate those questions. The most important thing is to load up all the questions, even if unsure about usefulness. Get them into workspaces and make sure customers have access. Start with Augment and others. Get it loaded up and working. We can figure out tagging and views as we go. We'll work through bugs. The time-sensitive thing is: get all the prompts loaded. It's okay if we archive them later or run differently. I'd rather spend a couple grand on wasted probes but have data in the next 30 days than not have it and wish we had that question sooner.

**Talal Syed:** Yeah, that makes sense. So Augment Code is one I can check with Jason and Andy. What are the high-profile clients we have that I want to set up immediately?

**Marcel Santilli:** Yes. And set up those workspaces, create prompts, load them up so we start tracking them.

**Talal Syed:** Cool. Awesome. Sounds good. I gotta run. But let me know if you think of anything else. Feel free to drop questions in the CheckThat channel and tag me. I'm fairly involved with this one, but I'm really excited to have your help. Thank you so much and have a great rest of your day.

**Marcel Santilli:** Yeah, you too. Let's find time for you to come out to SF.

**Talal Syed:** Yeah, definitely. I'm actually going to Pakistan for my sister's wedding tomorrow, so I'll be back early January.

**Marcel Santilli:** Well, enjoy that. That's a very happy time. One of those that takes several days to celebrate.

**Talal Syed:** When I'm back, I'm definitely going to fly and meet the team in person.

**Marcel Santilli:** Yeah, I love that, man. Enjoy your time, brother.

**Talal Syed:** Take care.

**Marcel Santilli:** Bye.

---

## Overview & Key Themes

**Market Positioning & Narrative**
- Core insight: market conflates AI behavioral change (real) with analytics visibility tools (noise). CheckThat separates the two.
- Competitors like Profound use the conflation to their advantage; CheckThat aims to be the standardized, data-driven alternative
- Analogous to election polling: instead of each city running its own research, use standardized methodology. 163+ vendors currently exist; most lack credibility.

**Product & Data Strategy**
- Focuses on B2B software; uses standardized category frameworks (subset of 1,200-1,500 possible categories)
- Defines best questions per category per funnel stage (awareness → advice → evaluation → comparison → decision → post-purchase)
- Data collection: 128+ probes per category; $0.06 per probe; $200K/month at scale (probes daily across 5-6 LLM services)
- Potential cost reductions: scheduling heuristics, weighted probes, tiered probe frequency

**SEO and Content Moat**
- Creates brand summaries and category comparison pages designed to rank for high-intent B2B queries ("LangChain pricing," "LangChain alternatives," etc.)
- Current blocker: pages not indexing; need to validate H1 strategy and technical setup
- Long-term vision: become authoritative answer source; judge which AI service gives best answer for specific use case
- Semrush has data moat but no SEO play; Crunchbase and G2 did both. CheckThat aims to replicate that combination.

**Immediate Execution Priorities**
- Prompt uploading for critical clients (Augment Code, Lovable) is urgent because data collection cannot be backfilled; every day delayed is lost historical data
- Workspace setup, tagging, and view features must be functional before full launch
- Bug fixes (line breaks in prompt creation) must be resolved via Linear reporting
- Beta strategy: validate with pilot customers first, then announce to avoid Scrunch alienation

**Prompt Methodology & Standardization**
- Key blocker: 10 people create 10 different prompt sets. Need unified, documented approach.
- Framework: understand audience → define persona (role, jobs, fears, KPIs, metrics, work products) → write questions per funnel stage
- Audience-based questions seed better questions than category-first (discovered during methodology development)
- High-quality example: finance manager at fast-growing B2B startup. Questions: "How do I automate financial reporting?", "How do I prepare a 409A evaluation?", "What should my month-end close checklist be?"
- Focus on evaluation and comparison stages (high intent, brand mentions, measurable accuracy). De-prioritize awareness and post-purchase (low brand mention rate).

**Funnel Stage ROI**
- Awareness & advice: low ROI; minimal brand mentions. Only value is building long-term trust if brand cited.
- Evaluation: high ROI; strong brand citation; accuracy measurable; clients care deeply.
- Comparison: high ROI; where purchasing decisions made; direct brand competitive positioning.
- Post-purchase: low ROI; clients don't track heavily; not priority for most.

**Research & Thought Leadership**
- Generate studies and reports using 6-month data ($100K+ experiments). Rare for competitors to run at that scale.
- Targeted dev-rel outreach to growth professionals, engineering leads, fintech buyers based on data insights
- Dogfooding internal tools; seamless funnel experience validates product before customer access

**Risk Management**
- Notion security: restrict access to strategic docs after incidents where departing staff exported and shared with competitors
- Scrunch partnership: don't over-promote CheckThat during beta to avoid alienation or platform access revocation
- Data irreplaceability: data collection windows cannot be retroactively filled; timing is critical
