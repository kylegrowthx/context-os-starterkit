# Mohitdeep Singh - Panel Interview | AI Engineer (Applied AI Scientist)

<metadata>
date: 2025-12-19
time: 20:30 UTC
duration: 35 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    role: CEO, GrowthX
  - name: Mohitdeep Singh
    role: Candidate - AI Engineer
fireflies_id: 01KCS8KJHJ7SD3CC737YRKRTXX
transcript_url: https://app.fireflies.ai/view/01KCS8KJHJ7SD3CC737YRKRTXX
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Candidate interview for first GrowthX AI engineering hire. Mohitdeep Singh walked through 7+ years building ML systems at ID Research Labs, Coupang, and Roku—focused on recommender systems, feature stores, and personalization ranking. When presented with GrowthX's core problem (optimizing data labeling and prompt engineering via human preference signals), Mohit immediately mapped it to recommender systems and proposed a hybrid architecture: fine-tuned models + reinforcement learning + re-ranking with factuality/structure checks. Marcel framed hiring priorities: customer empathy, pragmatic problem-scoping, and timing accuracy. Mohit acknowledged this aligns with his engineering instincts. Outcome: Marcel committed to regroup with Daniel (CTO) and move decision forward quickly.

---

## Context

Mohitdeep Singh is a candidate for GrowthX's first AI engineering hire. He has 7+ years of applied ML experience building recommendation systems and ranking models at ID Research Labs (signal processing), Coupang (product recommendations, payment systems, object detection), and Roku (multi-access recommendation systems, feature stores). He previously interviewed with Katya (Head of Product/Research) and Daniel (CTO), who flagged strong technical fit. This final interview was Marcel's opportunity to assess problem-solving approach, cultural fit around customer empathy, and pragmatism. Relationship stage: Late-stage candidate interview, decision pending CTO/CEO alignment.

---

## Relevance

**AI Product & Research**
- Deep experience with recommender systems, ranking, and personalization—directly applicable to GrowthX's core problem: using human preference data to optimize LLM output quality.
- Proposed hybrid architecture (fine-tuned models + RL + re-ranking) maps cleanly to GrowthX's need to frame data labeling as a signal optimization problem.
- Feature store design from Roku role demonstrates understanding of data infrastructure for ML systems at scale.

**GrowthX Services & Delivery**
- Problem-scoping discipline ("identify the problem very clearly") aligns with GrowthX's need to help clients frame their AI challenges correctly.
- Experience translating customer signals (click data, time-on-page, behavior trees) into model improvements mirrors how GrowthX approaches data labeling and RLHF.

**Culture & Hiring**
- Proposed culture-building role for first AI hire: Mohit asked directly about expectations for establishing AI team norms.
- Peer feedback suggests strong communication, mentoring, and team morale—valuable for scaling AI function.
- Learning approach (Notebook LM, paper reviews, LinkedIn content creators) shows continuous curiosity.

---

## Decisions & Commitments

**Marcel's commitment:** Regroup with Daniel (CTO) to review technical assessment and move decision forward quickly. Goal: unblock next steps (offer, additional interviews, etc.).

**Mohit's implied commitment:** Ready to discuss first-hire AI role, culture-building, and team structure if offer extended.

---

## Open Questions

- What is Daniel's technical assessment of Mohit's recommender systems expertise vs. GrowthX's specific AEO/data labeling stack?
- Timeline for decision: Does Marcel want to loop Katya in before final call?
- Compensation/role scope: Is this a senior IC role, tech lead, or director-track position?
- Start date expectations if offer extended?

---

## Overview

- **Date:** 2025-12-19, 20:30 UTC
- **Duration:** 35 minutes
- **Interviewer:** Marcel Santilli (CEO)
- **Candidate:** Mohitdeep Singh (AI Engineer, Applied ML background)
- **Purpose:** Final-stage hiring interview for first GrowthX AI engineering hire
- **Outcome:** Strong cultural and technical fit; Marcel to regroup with CTO for decision

---

## Key Topics

1. **Career Arc:** Signal processing (ID Research Labs) → recommender systems at scale (Coupang) → feature stores & cold-start problem (Roku)
2. **Problem Mapping:** How data labeling parallels recommender system optimization; human preference signals as primary training data
3. **Proposed Architecture:** Fine-tuned models + reinforcement learning + re-ranking with factuality/structure checks
4. **Leadership & Mentoring:** Mohit's approach to pair coding, team morale, problem-solving mindset
5. **Learning Approach:** Use of Notebook LM, paper reviews, continuous engagement with AI research (Meta blogs, LinkedIn creators)
6. **Hiring Philosophy:** First AI hire must build culture, framing, customer empathy; pragmatism over scope creep
7. **Problem-Scoping Framework:** Right problem + right way + right time; avoiding false starts and misaligned solutions

---

## Action Items

**Marcel Santilli (GrowthX)** - Regroup with Daniel (CTO) to review technical fit and align on offer/next steps

**Mohitdeep Singh (Candidate)** - Awaiting feedback from Marcel/Daniel on hiring decision

---

## Transcript

**Marcel Santilli:** Hey, how are you?

**Mohitdeep Singh:** I'm doing good, how are you?

**Marcel Santilli:** Pretty good. Happy Friday before the holiday. Tell me more—in what sense is the interview process different?

**Mohitdeep Singh:** Job interviews are really difficult now. It's not the same as it used to be.

**Marcel Santilli:** The bar is higher, that's for sure. You have a lot of good experience. I've reviewed your background and heard great things from Daniel and the team. Would love to hear your journey in your own words, then we can dig in from there.

**Mohitdeep Singh:** I started my career at ID Research Labs working on signal processing—that was before we had modern image processing pipelines and hardware. I did signal analysis work, including radio signal processing with Pandora. Then I moved to recommendation systems. Coupang is most recent; I worked on payment systems, product recommendations, and architected object detection pipelines. I've primarily worked with small, high-impact teams. My journey went from research background to applied machine learning pipeline work. That's the short version.

**Marcel Santilli:** You've had several conversations already. What excited you about the problem domains Daniel shared?

**Mohitdeep Singh:** The problem Katya and I discussed was very interesting—my case studies mapped to it directly. I had a well-structured idea about how to handle it. Katya talked about their current problems: getting results to feed the LLM so it sees the right patterns consistently. That's critical when you're working with many clients—you need to hit the bullseye every time. The core problem is what every company tries to do: optimize how prompts hit the LLM.

That got me excited. I presented an initial solution, we discussed what's possible and what's not, and talked through architecture. I really like how Daniel approaches the problem—he brings deep experience. The conversation felt productive.

**Marcel Santilli:** Your background in recommender systems and personalization ranking is really interesting. On the surface, our work might not seem directly related, but I come from the world of data labeling and post-training, supervised fine-tuning. The parallels are strong. Serge AI, one of our customers, is a perfect example. Serge's founder worked on recommender systems at Meta, Facebook, Twitter, and YouTube—optimizing signals to decide what to show in feeds, on YouTube, in your timeline.

What they discovered was that human preference data is fundamental. Humans vote with their attention on what they prefer. The bottleneck was always data labeling and finding the right experts. They realized they couldn't just hire random people off the street—they needed to source the specific people who understood the domain, give them tasks, and build the ranking system. That's how Serge became profitable, over a billion in revenue.

**Mohitdeep Singh:** I see the relevance now. That's one way to think about it. But you could also use reinforcement learning—set up policies and actions. It won't be instant; it'll take time and we'd need a solid reward equation. We could combine a fine-tuned model with RL to adjust policies dynamically. A good ranker or re-ranker improves results significantly. I know Daniel showed me you have agent frameworks for this. I'd add factuality checks and structure checks—those came to mind immediately.

**Marcel Santilli:** Walk me through your Roku or Pinterest experience. Can you share a project where the business was optimizing for a big target—user behavior, engagement—and how you approached it?

**Mohitdeep Singh:** At Coupang, we had product summaries from clients on the platform. We'd push products based on usage patterns. We captured click-level data, time-on-page data. I built user behavior graphs as trees, then compared overlap between users. Instead of traditional collaborative filtering, I used tree-based retrieval—much more precise than similarity search. That's what made it robust.

At Pinterest, they encode images, create embeddings, then generate recommendations. The core insight is similar: structure user behavior as a graph, not just raw similarity metrics.

**Mohitdeep Singh:** At Roku, we built a multi-access recommendation system—similar to Netflix's approach. The main challenge was the feature store: how to structure it, how to use it. We needed to capture user engagement data—time spent on content, browsing time, genre interest. And we had to solve the cold-start problem: what do you recommend when you have no history on a user? That was critical.

I built feature stores across multiple dimensions and simplified the retrieval pipeline. I didn't use LLMs because the scope was different, though we used SLMs for description generation. The core was the feature store itself. Once you have that, you can layer on collaborative filtering or encoders for other signals.

The harder part was determining the scoring metric—what to optimize for. Over time we added many features. Technical challenges aside, most of our battles were about data governance: GDPR compliance, regional restrictions, data sourcing. That was the real bottleneck.

**Marcel Santilli:** How would your manager describe you at the end of that project?

**Mohitdeep Singh:** He'd be happy with my work. I'm not a thought leader in the traditional sense—I'm hands-on technically. But I'm a problem solver. I tackled issues methodically. I had two engineers reporting to me; I mentored them actively. When someone was stuck, I'd do pair coding sessions to unblock them.

**Marcel Santilli:** How would your peers describe you?

**Mohitdeep Singh:** I keep the work environment light and make sure morale is high. They'd probably say I'm friendly and approachable.

**Marcel Santilli:** What's your superpower? Why are you effective at what you do?

**Mohitdeep Singh:** I build a strong foundation first. I identify the problem clearly, then solve it methodically. Over time I've learned to break complex work into smaller tasks. Communication is key—I keep peers, superiors, and engineers informed so there are no surprises and everyone's aligned. On the technical side, I do lots of paper reviews and follow AI research blogs heavily. Meta's AI blog is exceptional.

**Marcel Santilli:** How do you like to learn? What sparks your curiosity?

**Mohitdeep Singh:** Learning is easier now. I use Notebook LM—I upload a paper, it creates notes, visuals, explains equations. It's a good ranker, finds exact information, and doesn't inflate things or hallucinate from the internet like other LLMs do. I follow code and AI content creators on LinkedIn, Meta's AI blog, and run small experiments to understand what they achieved. Theory is one thing, but applying it reveals new dimensions of thinking.

**Marcel Santilli:** We don't have tons of time, but happy to answer questions.

**Mohitdeep Singh:** I've spoken with Daniel and Katya about the AI work. I understand this is the first AI hire—Katya's currently outsourced. I'd be building the culture, laying groundwork for the team. What are your expectations for the first few months?

**Marcel Santilli:** Context and customer empathy. Understand what we're trying to achieve, what matters to our customers. It's easy for builders and researchers to lose sight of that—to build for the sake of building instead of asking what problem we're actually solving for this customer. Once you frame that, figure out what we need to build versus learn, and how to be pragmatic. Don't boil the ocean.

The framing matters: solve the right problem, in the right way, at the right time. Solve the wrong problem—bad. Solve the right problem the wrong way—bad. Solve the right problem the right way at the wrong time—still bad. Context is critical. Don't jump to solutions. Validate the problem first.

**Mohitdeep Singh:** That's crucial. The timing, the approach, the problem definition—they all define what comes next. You can't mess up any of those. Thanks for sharing that framework.

**Marcel Santilli:** I appreciate it. Great conversation. I'll regroup with Daniel and move things forward quickly.

**Mohitdeep Singh:** Thanks. It was really nice talking with you. Have a great weekend.

**Marcel Santilli:** You too.
