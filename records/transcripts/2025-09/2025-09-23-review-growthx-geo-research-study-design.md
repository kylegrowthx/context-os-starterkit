# Review GrowthX GEO Research Study Design

<metadata>
date: 2025-09-23
time: 21:02 UTC
duration: 44 minutes
organizer: jason@growthx.ai
participants: Daniel Lopes, Katja Wittfoth, Jason Gong
fathom_recording_id: 89330378
fathom_url: https://fathom.video/calls/418679925
share_url: https://fathom.video/share/enbhWBaLmPrz7vtzGzJxZru_DcEYdnSw
source: fathom
enriched_on: 2026-03-03 14:32 UTC
speaker_note: "Golden Gate" display name in Fathom matched to Jason Gong based on action item assignments and meeting dynamics (Jason assigned tasks to self and owned project decisions).
</metadata>

---

## Summary

GrowthX and Katja Wittfoth aligned on the overall design for a GEO (AI citation) research study that will analyze how different AI platforms cite sources across industries, funnel stages, and prompt types by running 40 prompts per variation over 14 days. The team agreed to use forced search API calls (rather than regular LLM calls) to ensure consistent web search triggering, and will pilot the full pipeline with a single industry (likely FinTech) before scaling to multiple industries. Remaining open questions include finalizing counterfactual setup (defining what citations should have been included), investigating whether all citations come from top search results, and determining differences between manual app usage versus API calls.

---

## Context

GrowthX is designing a major research study to understand how AI platforms (Claude, ChatGPT, Gemini, etc.) determine which sources to cite when answering questions. This is core to CheckThat, GrowthX's AI visibility product that tracks which sites appear in AI-generated responses. Katja Wittfoth is the lead researcher driving this work; Jason Gong and Daniel Lopes are supporting from GrowthX. The study will generate empirical data on how citation patterns vary across industries (starting with FinTech), buyer funnel stages (problem identification, solution evaluation, provider comparison), and prompt characteristics (question type, length). This research will directly inform CheckThat's ranking algorithm and help the team publish findings that position GrowthX as a thought leader in AI-powered search visibility.

---

## Relevance

**To CheckThat:**
- Core data infrastructure for CheckThat's ranking algorithm: empirical understanding of how Claude, ChatGPT, Gemini, and other platforms select which sites to cite from search results
- Key insight: APIs behave differently than manual app usage (forced search API vs. optional web tool toggle) — will need to document which mode is tested in any published findings
- Reverse engineering opportunity: determine if all citations come from top 5-10 search results or if platforms access deeper/different search indexes
- Prompt rewrites: investigate whether platforms modify user queries before searching, which could affect citation patterns significantly

**To GrowthX Delivery:**
- Methodology for building large-scale research studies: 40 prompts per variation × 14 days × multiple categories creates manageable sample sizes with statistical rigor
- Feature engineering for content analysis: lessons from this study will apply to client work on understanding how their content performs in AI visibility
- Pilot-first approach: running FinTech pilot before full rollout helps identify pipeline issues early and controls costs

**To GrowthX Business Development:**
- Potential reference content: study findings can become a published report positioning GrowthX as the authority on AI citation patterns
- Competitive positioning: understanding citation mechanics before competitors do creates knowledge advantage for prospecting B2B SaaS and software clients
- Cost visibility: Daniel confirmed cost structure is acceptable, enabling full project greenlight without budget surprises

---

## Overview

- Agreed on overall study design approach: analyzing prompts across industries, funnel stages, and prompt categories
- Need to further investigate counterfactual setup and reverse engineer citation sources
- Will start with a pilot using one industry (likely FinTech) to test pipeline and learn before full implementation
- Team to collaborate on defining prompt categories, funnel stages, and other study parameters

---

## Key Topics

### Study Design and Methodology

  - Using 40 prompts per industry/funnel stage combination (240 total) as minimum, multiplied by 14 days
  - Will use search API calls to force web searches, not regular LLM calls
  - Need to create features for prompts (e.g., question type, length) in addition to content features
  - Counterfactual setup requires more investigation (Google top 20, known competitors, regular background searches)

### API and Search Behavior

  - Different AI platforms (Claude, ChatGPT) use various search providers (Brave, Bing)
  - Search process: detect intent, generate query, return results, re-rank semantically, select top results
  - Need to investigate differences between manual searches, regular API calls, and forced search API calls

### Next Steps and Task Division

  - Jason: Handle funnel stages and prompt categories
  - Katja: Focus on industries, platforms, and creating the pipeline
  - Daniel: Oversee plans and cost considerations
  - Team: Collaborate on defining prompt variations and study parameters
  - Consider setting up regular sync meetings for updates and alignment

### Open Questions and Investigations

  - How to effectively set up counterfactuals and reverse engineer citation sources
  - Investigate if all citations come from first few search result pages
  - Compare manual app usage vs API calls for potential differences
  - Explore how different prompt types might trigger web searches

---

## Action Items

**Jason Gong (GrowthX)**
- Send study design doc to Jose for review
- Define funnel stages & prompt categories for study
- Define plans to include in study
- Check with Zach regarding pipeline creation; take on if Zach is unavailable
- Set up recurring sync meetings for study team

**Katja Wittfoth**
- Investigate counterfactual setup options for study (determine which sources should have been cited but weren't)
- Define platforms to include in study
- Create initial pipeline for study execution

---

## Transcript
**Katja Wittfoth:** Hey, Jason, you're on mute.

**Jason Gong:** Hello.

**Jason Gong:** Hey, Jason.

**Katja Wittfoth:** Hey, Daniel.

**Jason Gong:** I've read through it a little bit.

**Katja Wittfoth:** I see you're halfway through. Should we take another 10 minutes for the methodology section?

**Jason Gong:** I can scan it really fast. The first half makes sense to me.

**Jason Gong:** How about you, Daniel?

**Katja Wittfoth:** I'll grab water for a few minutes. We'll reconvene at 2:15 to start the discussion.

**Jason Gong:** Okay.

**Katja Wittfoth:** Since we don't have a lot of time, let's talk about the study design overall and align on direction. Are there any concerns or issues you see? Is everything clear in the document?

**Jason Gong:** The design makes sense. You're picking a bunch of prompts across industry and product category, tracking them through various funnel stages, creating features, and finding correlations. That all works. But I'm not sure how you pick which prompts to search. Actually, it probably doesn't matter as long as you have a good sample.

**Jason Gong:** I noticed the 40 prompts per variation (240 total) — I was expecting a bigger number initially, but I think that's probably the minimum we should aim for statistically.

**Katja Wittfoth:** We need to think about the combination of variables. One part is industry — say, FinTech. Then we have buyer funnel stages (three variations), and we'll have 40 prompts per industry/funnel combination.

**Jason Gong:** That makes sense. And just thinking out loud — like we engineer features for content, we should probably create our own features for the prompt itself. Not just industry and category, but things like: Is it a question? Is it a statement? Question length? That kind of prompt categorization.

**Katja Wittfoth:** Yes, exactly. We could have a full question, a keyword search, longer text, a how-to question, idea questions — different prompt categories.

**Jason Gong:** Right, so the assumption is that if you track 40 samples per category, you should understand how citations work for that category without exhaustively testing all combinations.

**Katja Wittfoth:** Exactly. 40 is the statistical minimum, but more is always better. And we multiply that across 14 days to get many more samples per variation.

**Jason Gong:** That makes sense.

**Jason Gong:** We need to think about API usage. Different platforms have two APIs: a normal chat API with optional web search, and a dedicated search API. For Claude and ChatGPT, the search API guarantees forced web search. Most people don't use it because it's expensive. For this study, we should use the search API, not the traditional LLM call, to ensure web search is triggered consistently.

**Jason Gong:** Free versus pro versions could matter from a user experience standpoint, but we can't control that for API calls. We're using APIs that aren't accessible to free users, so we should disclose that if we publish findings.

**Katja Wittfoth:** We tested this briefly with one prompt. There are limitations on when web search triggers with the non-pro version, but we didn't get conclusive results.

**Jason Gong:** The approach we're taking will reflect paid user behavior, which is what we want. We need to document this methodology clearly for any paper or public findings.

**Jason Gong:** How we segment prompt types is important. We should think about this carefully with the full team and make sure we have a consistent methodology.

**Katja Wittfoth:** We need to think through the prompt categories carefully. We have industries, company stages, platforms, and plans. We need to be very clear about the setup before we start, and the whole team should work through this together.

**Jason Gong:** On the CheckThat project we're working on separately, we built a leaderboard system with categories and subcategories for B2B SaaS. For example, in AI development tools, Google, Cursor, and Winsurf compete. We run about five prompts per subcategory daily to see who shows up.

**Jason Gong:** But that approach is optimized for a leaderboard, not for research methodology. Your study needs broader categories to understand how citations work across the market, not just who's winning today. The categories probably shouldn't be the same as what we use for the leaderboard.

**Katja Wittfoth:** That makes sense. This research study is more about understanding the underlying patterns in how citations work.

**Katja Wittfoth:** The counterfactual is a list of what should show up — sites that could have been cited but weren't. We need a clear design for how to fetch those candidates.

**Jason Gong:** So counterfactuals are the links that were cited, plus the ones that had the potential to be cited but didn't get selected. Is that pool just the top Google results, like the first five pages of search results? Or are there other sources we should consider?

**Katja Wittfoth:** This is something we need to figure out with the team and possibly outside experts. One approach: fetch Google's top 20 results at the start of the study, document what's there, then see which sites actually get cited. For example, if a FinTech prompt cites Ramp but not Mercury, and Mercury was in our initial list, then Mercury is a counterfactual.

**Jason Gong:** I like the idea of capturing counterfactuals regularly, not just once, because search rankings change constantly and that would give us richer data.

**Katja Wittfoth:** Right. A one-time snapshot won't capture how rankings evolve.

**Jason Gong:** When we use the API, it shows what searches run in the background and returns only the citations used. Perplexity behaves differently — it shows additional questions and pre-fetches citations. The key question is whether all citations come from the first five search result pages, or if platforms access deeper indexes.

**Katja Wittfoth:** I've done some research on this. All platforms use search providers. Claude uses Brave Search. The workflow is: detect intent, generate query, get results with URLs and snippets, re-rank semantically, select top results, and insert into the LLM prompt.

**Jason Gong:** Gemini and other platforms work similarly. This opens up interesting reverse-engineering opportunities. We could call the search APIs directly to compare what the APIs return versus what actually gets cited.

**Jason Gong:** This could produce valuable content — understanding how platforms select and rank search results reveals insights for content strategy. For example, if a site isn't being scraped because its meta description is weak or title is wrong, that's actionable intelligence.

**Jason Gong:** Yep.

**Jason Gong:** Yeah, like, we're going to, um, the...

**Jason Gong:** The augment prompt they really care about, like, what is the best AI coding tool, like, basically everything cited as, like, in 2025 in the title, like, originally, the main search is just, what's the best AI coding tool in 2025 or something, so.

**Jason Gong:** Yeah, there's also a good thing about, like, I think tracking the bearings, the way it has, it's going to be super interesting, because if they are doing prompt rewrites for anything, at least, a web search, then it will be interesting to see if the bearings actually matter or not, you know.

**Jason Gong:** So, when you say prompt rewrites, you mean the thing that you're searching for is not the prompt?

**Jason Gong:** The query that you, the thing that you typed, it's not the thing that you sent to delete, you know.

**Jason Gong:** One key question: does all citation come from the first five pages of search results, or are platforms accessing deeper indexes? We should test this with the APIs.

**Jason Gong:** We could also do manual testing to compare how people actually use the apps versus the API approach. If it's 40 prompts, we could hire contractors to manually test some of these scenarios. The normal API call might trigger search automatically, so it might behave like the manual web search button.

**Katja Wittfoth:** The search button is hidden — it's under "more" in the menu. Most people probably don't use it.

**Jason Gong:** Right. Another issue with manual testing: the app doesn't expose the search queries sent to Google or Bing. You can inspect network requests to see a few of them, but not all.

**Katja Wittfoth:** We should do some manual checks to understand the real-world behavior better.

**Jason Gong:** These are good open questions to investigate. Overall, though, we're aligned on the big picture direction.

**Katja Wittfoth:** For the pilot, once we finalize the approach, we should run the full pipeline for a couple of days with just one industry to see if it's working and what we learn before scaling up.

**Jason Gong:** And Daniel can assess the cost to make sure it's reasonable for the company.

**Katja Wittfoth:** Costs look fine. Let me break down the parameters: Funnel stages (problem identification, solution evaluation, provider comparison), prompt categories (full question, keyword, how-to, etc.), industries (starting with FinTech), and platforms (Claude, ChatGPT, etc.). Everyone needs to align on these variables.

**Jason Gong:** I'll send this document to Jose for visibility. We should be picking the actual prompts as the next step, and that should happen upfront before we start running data collection. Feature engineering can happen in parallel.

**Katja Wittfoth:** Ideally, we finalize most details upfront, but some can be done iteratively. I want to set up counterfactual collection as a separate workstream since that's more complex.

**Jason Gong:** I'll check with Zach about pipeline creation and handle it if needed. I'll also set up recurring sync meetings for the team.

**Katja Wittfoth:** Good. Let me document what I'm researching in one place so we can publish it later. I'll add pages as I find useful information.

**Jason Gong:** Great. Let's regroup regularly to stay aligned.

**Katja Wittfoth:** Yes, I'll get those recurring meetings on the calendar. Thanks, everyone.
