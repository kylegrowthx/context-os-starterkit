# Shaping with Ryan Singer

<metadata>
date: 2025-12-18
time: 16:00 UTC
duration: 180 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Daniel, Ryan Singer
fireflies_id: 01KCR1GCBQ9708B16NEMJNK9FR
transcript_url: https://app.fireflies.ai/view/01KCR1GCBQ9708B16NEMJNK9FR
</metadata>

---

## Summary

The meeting centered on addressing challenges in scaling high-quality content production by integrating AI workflows into the editorial process. Marcel highlighted the transition from manual article production (slow and costly) to AI-powered workflows that have significantly reduced costs to 10-20 cents per word and increased output. However, the team identified bottlenecks in editorial capacity, with editors spending excessive time per article (up to 5 hours vs target of 15-30 minutes), and the need for a structured client feedback system to ensure quality. Discussions included developing a hybrid feedback mechanism, establishing a formal editorial sign-off process, and enhancing client access to streamline communication. The meeting emphasized prioritizing urgent issues and setting clear goals to improve operational efficiency by January, while ensuring editorial quality and client satisfaction remain paramount.

---

## Action Items

**Marcel** - Provide detailed context documents and structured calibration inputs for clients; implement tracking mechanisms for editor time; integrate client feedback capture directly into platform; build formal client sign-off and staging process; collaborate on monitoring dashboard

**Daniel** - Optimize text editor with comment and revision features; develop agents for style, research, and structural feedback; contribute to client feedback experience design; define status management and submission flows; explore lightweight client access models

**Ryan Singer** - Facilitate identification of prioritization and scope boundaries; propose "new editor on task monitor" solution for throughput monitoring; advocate for building digital twin for client reviews; lead design brainstorming for client feedback integration; coordinate definition of "done" criteria

---

## Transcript Summary

The meeting was a strategic session with Ryan Singer, a renowned product strategist, discussing how to improve GrowthX's content production platform and editorial processes.

**Opening and Context**

Ryan Singer opened with observations about the number of recording tools in use (Fathom, Fireflies, etc.), noting there's little downside to capturing content in multiple ways. Marcel introduced the core challenge: scaling high-quality content production while managing editorial efficiency.

**AI Workflow Integration and Cost Efficiency**

Marcel explained the previous model involved manual article production with multiple editors and freelancers, costing $2 million annually, producing only 20 articles per week. The transition to AI-powered workflows at clients like Deepgram has enabled production of 3,000 pages with minimal editorial overhead and monthly contract values of $10-20k.

The business model achieves 70% gross margin while reducing content costs to 10-20 cents per word, a 90% reduction compared to traditional agencies charging $1.50 per word. However, AI alone cannot guarantee quality; effectiveness depends on expert input and process design.

**Editorial Capacity Bottleneck**

The core bottleneck identified: editors spend up to 5 hours per article, whereas acceptable targets are 15-30 minutes to maintain throughput. Editors currently lack:
- Centralized tracking of time spent per piece
- Consistent tools (mixing Google Docs with internal systems)
- Formalized client sign-off workflow
- Clear "publish-ready" criteria

This lack of transparency makes it hard to train new editors or reproduce quality, threatening growth and client satisfaction.

**Client Feedback and Calibration Process**

Calibration is multi-step: input/context setting, writing guidelines creation, and iterative sample reviews by clients to define "publish-ready" standards. Failure to properly calibrate leads to churn, especially with complex clients like Biologica and Clerk.

Current reliance on Google Docs for feedback results in:
- Lost context and inconsistent comment tracking
- Inability to measure editorial effort or quality trends
- Multiple stakeholders causing confusion about approval

The team envisions a hybrid system:
- In-place comments on specific text blocks for localized errors
- Higher-level structured feedback (quiz or survey) for broader strategic input on style, tone, accuracy, and missing topics

**Platform and Tooling Solutions**

The team discussed implementing:
- Rich text editor with inline commenting (leveraging Tiptap editor)
- Structured feedback forms/quizzes guiding clients to provide clear, actionable responses
- Submission control points triggering client review and enabling tracking of revision rounds
- Tokenized/whitelisted links for client access without full accounts (inspired by Airtable, Figma, Basecamp)
- Monitoring dashboard tracking simulation runs and editorial throughput

**Feedback Processing and AI Training**

Feedback collected feeds into supervised fine-tuning for AI models, including reinforcement learning to continuously improve accuracy. Feedback is categorized into style, voice, factuality, and research quality, with AI agents handling post-processing.

The current manual approach of converting feedback into prompt adjustments is unsustainable; the goal is an AI-driven system interpreting and applying corrections automatically.

**Strategic Prioritization**

Key priorities identified:
1. Editorial transparency and capacity (most urgent)
2. Client calibration and feedback capture (key enabler)
3. Defer complex client sign-off and legal review workflows
4. Success criterion: new editors don't repeat previously identified mistakes

**Ryan Singer's Key Insights**

- Emphasized importance of capturing editorial feedback in structured, trackable way
- Proposed breaking feedback into two layers: specific text comments and higher-level structured feedback
- Highlighted need for submission control point enabling enforcement and visibility
- Suggested tokenized link access for clients, minimizing friction
- Recommended "digital twin" framing to motivate client investment in feedback
- Identified success metric as preventing new editors from repeating known mistakes
- Advocated balancing simplicity with richness in client feedback experience
- Suggested monitoring dashboard for editors' simulation and editing activity to catch bottlenecks
- Encouraged avoiding premature focus on legal/final sign-off flows to keep scope manageable for January
