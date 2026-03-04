# Vercel AI Gateway: Questions for Friday Meeting

---

## Why We're Here

GrowthX is partnering with your growth marketing team to build out the AI Gateway's content and SEO footprint. Before we start building, we need to align on what's possible, specifically around data, page scope, and how we work together.

We spent the past week researching the competitive landscape and the current state of the AI Gateway pages. Here's what we found.

### Competitive Landscape

The AI Gateway currently has ~170 model pages with minimal content. The pages are functional, but competitors are already dominating "model search" traffic with significantly richer experiences:

- **OpenRouter** (~2,000 model pages). Tabbed sections for overview, providers, performance (latency/throughput charts with proprietary data), pricing, and top apps using each model. They also have a [model comparison tool](https://openrouter.ai/compare) and activity/popularity visualizations backed by their own usage data.
- **Ollama** (~4,800 model pages). Every model variation with detailed specs, tags, and usage instructions.

Both are ranking for high-intent developer queries: "[model name] pricing," "[model name] vs [model name]," "best model for [use case]." These are queries that should be landing on Vercel.

### The Vercel Advantage

The biggest gap in what competitors offer is trustworthy, first-party data. OpenRouter surfaces its own usage stats, but Vercel's gateway, with 35+ providers, 100+ global PoPs, and real production traffic from apps like Cline, has a fundamentally stronger data set.

If we can surface proprietary usage data (app attribution, latency benchmarks, model popularity trends, use-case patterns), these pages go from "catching up" to "the only place you can get this." That's the core question for today.

### What We Want to Walk Away With

1. What proprietary data is available and usable
2. Whether the model catalog is fixed or expandable
3. How much latitude we have on page design and content
4. Who on your team will partner with us on data integration
5. What you've been wanting to build but haven't had bandwidth for

---

## 1. Proprietary Data Access

Everything else depends on the answer here. Without clarity on data, we can't scope the enrichment work.

**Lead question:** What proprietary/internal data does Vercel have from the AI Gateway that we could surface on model pages?

Break it down into specifics:

- **App attribution.** Which opted-in apps are making requests to which models? Can we show "top apps using this model" on each model page?
- **Token usage volume.** How many tokens of usage are happening daily/weekly/monthly, by model? Can we show relative popularity or trending data?
- **Model popularity and trends.** Are models becoming more or less popular over time? Do you have time-series data we could visualize (like OpenRouter's activity charts)?
- **Latency and performance.** Do you have TTFT, P75/P99 latency, or throughput data by model? If across thousands of requests, is one model measurably faster? That's a compelling data point for developers choosing a model.
- **Uptime and reliability.** Do you track uptime or error rates per provider/model through the gateway? The Cline case study references a 43.8% error rate reduction. Is that kind of data available at the model level?
- **Use case / category data.** Out of all prompts sent to a given model (e.g., Opus 4.6), can you determine what percentage are for coding vs. writing vs. other broad categories? Even rough categorization would enable "best model for X" pages backed by real data instead of opinion.

Follow-ups:

- What data can we legally and practically use on public-facing pages? Any restrictions on surfacing usage data, even in aggregate?
- How would we access this data? Direct database/API? Regular exports? Specific engineer we need to work with to get it piped in?

---

## 2. Model Catalog Completeness

If the current list is the full list, we can't create new model pages. This bounds the entire project scope.

- According to your docs, the models page is the canonical list of available models in the AI Gateway. **Is this actually the full list, or are there supported models that aren't listed?**
- **How often are new models/providers added?** What's the cadence? Is there a pipeline we should be aware of so we can have pages ready when new models go live?
- Are there deprecated or sunset models that should be removed or archived?

---

## 3. Page Enrichment: Scope and Format

What can go on each model page, and how much latitude do we have?

- **Do you want us to redesign/restructure the model pages, or are we working within the current template?** The current layout has room for a lot more. Is page redesign in scope, or just content enrichment?
- **What's the current CMS/publishing workflow for AI Gateway pages?** Are these generated programmatically from a data source, or individually authored? Can we push content updates directly, or does an engineer need to deploy?
- **Can we add new sections or tabs to model pages?** e.g., a pricing tab, an apps tab, a performance tab, a comparison widget, similar to OpenRouter's tabbed approach.
- **Pricing data.** Can we add per-model pricing (input/output token costs) to each page? Is that data already structured somewhere internally, or do we need to pull it from provider docs?
- **Playground / chat box.** How often is the playground chat box actually getting used on model pages? Is it driving value, or is it taking up real estate that could be better used?

---

## 4. Comparison and "Best Model For" Content

The longer-tail opportunity. Hinges on data access from Section 1.

- **Would you want a model comparison tool on the site?** Similar to [OpenRouter's compare tool](https://openrouter.ai/compare). If so, what data points should comparisons include?
- **Are you open to "best model for [use case]" landing pages?** e.g., "Best AI model for coding," "Best model for content generation." These would need to be backed by data to be credible and avoid the risk of rapid obsolescence.
- **Do you have any internal benchmarking or evaluation data** (beyond the LLM visibility tool) that compares models against each other for specific tasks?

---

## 5. Leaderboards

- The leaderboards page currently shows top apps and top providers. **What's the vision for this page?** Is it meant to grow into something more comprehensive?
- **Can we create model-level leaderboards?** e.g., "Most used models this month," "Fastest models by TTFT," "Most reliable models by uptime."
- **How is the leaderboard data currently calculated?** Purely from opted-in app attribution, or does it include all gateway traffic?
- The activity chart on the leaderboards page appears to have rendering issues (large blank/black sections in the historical data). Is this a known issue?

---

## 6. App Attribution and Ecosystem

- **How many apps have opted into app attribution?** Is it a significant percentage of gateway traffic, or a small subset?
- **Can we create individual pages for opted-in apps?** e.g., "How Cline uses Claude Opus on Vercel AI Gateway." Rather than just linking to the app, a dedicated page describing the app and its model usage would be more valuable for SEO and user experience.
- **Can we show which apps use a specific model on that model's page?** The inverse of the current leaderboard. Instead of "top apps overall," show "top apps for this model."

---

## 7. Technical Access and Workflow

- **Can we get access to the AI Gateway repo** (or the relevant portion of the vercel.com codebase) to understand the current page templates and data model?
- **Who is the engineering point of contact** for wiring data into pages? Is there a specific person on the AI Gateway team who will partner with us on data integration?
- **What's the deployment process for AI Gateway pages?** PR-based? Automatic from a data source? What's the review/approval cycle?

---

## 8. Competitive Positioning

- **Are you aware of what OpenRouter, Ollama, and other aggregators are doing with their model pages?** Do you see them as direct competitors for "model search" traffic?
- **Is there any content or data angle you've wanted to pursue but haven't had bandwidth for?** What's the AI Gateway team's wish list?
- **Are there specific search queries or keywords you're trying to rank for** with the AI Gateway pages?

---

*Prepared by GrowthX | February 27, 2026*
