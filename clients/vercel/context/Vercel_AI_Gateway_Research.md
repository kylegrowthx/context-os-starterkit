# Vercel AI Gateway: Deep Research Analysis

**Prepared by GrowthX | February 2026**
*Sources: vercel.com (official documentation, blog, and product pages)*

---

## 1. Executive Summary

Vercel AI Gateway is a unified API proxy that routes AI inference requests to over 35 providers through a single endpoint. It launched in alpha on May 20, 2025 and reached general availability on August 21, 2025. The gateway sits between applications and AI providers, handling routing, failover, authentication, caching, and observability without requiring provider-specific SDKs or API keys.

The core value proposition is operational simplification: developers use one API key and one endpoint to access hundreds of models across text, image, video, and embedding modalities. Vercel charges zero markup on token costs, monetizing instead through platform stickiness and credit-based pricing.

> **Key Stats:** 35+ supported providers · Hundreds of models · 100+ global PoPs · Sub-20ms routing overhead · 2M+ AI SDK downloads/week · Zero token markup

---

## 2. Architecture and How It Works

### 2.1 Core Mechanism

The AI Gateway functions as a proxy layer between the calling application and the underlying AI provider. All requests route through a single base URL:

```
https://ai-gateway.vercel.sh/v1
```

The gateway accepts requests in OpenAI-compatible format and translates them to the appropriate provider API. This means existing code using the OpenAI SDK can switch to the gateway by changing only the base URL and API key, regardless of whether the target model runs on Anthropic, Google, Mistral, or any other supported provider.

### 2.2 Provider Routing and Failover

The gateway dynamically routes requests based on real-time provider health, considering uptime, latency, and error rates across its global network of 100+ Points of Presence. Developers can also control routing explicitly:

- **order:** An array of provider slugs defining the preferred routing sequence. The gateway tries providers in order, failing over automatically.
- **only:** Restricts routing to a specific set of providers, useful for compliance or data residency requirements.
- **Model-level fallbacks:** Separate from provider routing, allowing fallback from one model to another within or across providers (e.g., Claude Sonnet to GPT-4o).

```javascript
providerOptions: {
  gateway: {
    order: ['bedrock', 'anthropic', 'google-vertex'],
    only: ['bedrock', 'anthropic'],
  }
}
```

The gateway returns detailed metadata about routing decisions, including which providers were attempted, latency per attempt, and cost breakdown per provider.

### 2.3 Global Infrastructure

Vercel compares the AI Gateway to a CDN for AI inference. Requests enter the nearest of 100+ global PoPs and are routed over a private backbone to the optimal provider endpoint. The Cline case study reported P99 latency improvements of 10-14% and error rate reductions of 43.8% after migrating to the gateway, with sub-20ms routing overhead.

---

## 3. Supported Providers and Models

The gateway supports 35+ providers spanning text generation, image generation, video generation, and embeddings:

| Provider | Slug | Category |
|---|---|---|
| Anthropic | `anthropic` | Text |
| OpenAI | `openai` | Text, Image |
| Google AI (Gemini) | `google` | Text |
| Google Vertex AI | `google-vertex` | Text, Image, Video |
| AWS Bedrock | `bedrock` | Text |
| Azure OpenAI | `azure` | Text |
| Mistral | `mistral` | Text |
| Groq | `groq` | Text |
| xAI (Grok) | `xai` | Text |
| DeepSeek | `deepseek` | Text |
| Perplexity | `perplexity` | Text + Search |
| Together AI | `together` | Text |
| Fireworks | `fireworks` | Text |
| Cohere | `cohere` | Text, Embed |
| Replicate | `replicate` | Text, Image, Video |
| DALL-E (via OpenAI) | `openai` | Image |
| KlingAI | `kling` | Video |

Additional providers include Cerebras, Lambda, Novita, Luma, Fal, and others. The full list continues to expand.

---

## 4. Capabilities

### 4.1 Multi-Modal Generation

- **Text generation:** Streaming and non-streaming completions across all text providers, with tool/function calling support.
- **Image generation:** DALL-E, Imagen, and other image models through a unified API.
- **Video generation:** Veo 3.1, KlingAI, Wan, and other video models.
- **Embeddings:** Vector embedding generation for search and RAG pipelines.

### 4.2 Web Search

The gateway provides two provider-agnostic search tools that work with any model:

- **Perplexity Search:** $5 per 1,000 requests. Uses Perplexity as the search backend but works with any model.
- **Parallel Search:** $5 per 1,000 requests. An alternative universal search option.

In addition, native provider search tools are supported (Anthropic web search, OpenAI web search, Google search grounding). For enterprises requiring zero data retention compliance on search, Enterprise Web Grounding is available.

### 4.3 Automatic Caching

The `caching: 'auto'` option applies provider-appropriate cache strategies automatically. For Anthropic models, this inserts cache_control breakpoints at optimal positions. This is distinct from standard HTTP caching and reduces costs by avoiding redundant processing of repeated prompt prefixes.

### 4.4 Zero Data Retention (ZDR)

By default, the gateway deletes all prompts and responses after request completion. ZDR can be enforced at the provider level by setting `zeroDataRetention: true`, which ensures that even the upstream provider does not retain data. This is a significant compliance feature for enterprises handling sensitive data.

### 4.5 Observability

The built-in observability dashboard tracks four core metrics:

- **Requests by model:** Volume and distribution across models and providers.
- **Time to First Token (TTFT):** Latency tracking with P75 summaries (not just averages).
- **Token counts:** Input and output token usage per request.
- **Spend:** Cost tracking per model, per provider.

Metrics are available at both project and team scope. Summaries include P75 duration and P75 TTFT. Log export is available for external analysis. Observability Plus provides extended data retention for teams needing longer historical access.

### 4.6 App Attribution and Leaderboards

Developers can tag requests with custom headers (`X-Vercel-AI-App-Name` and `X-Vercel-AI-App-Url`) to identify which application generated the request. This feeds into observability dashboards and public leaderboards showing top apps and models by usage.

---

## 5. Authentication and BYOK

### 5.1 Standard Authentication

The primary authentication method is a Vercel AI Gateway API key, generated in the Vercel dashboard. This key authenticates all requests regardless of the target provider, abstracting away individual provider credentials.

### 5.2 Bring Your Own Key (BYOK)

BYOK allows developers to use their own provider API keys through the gateway while retaining all routing, failover, and observability features. BYOK credentials can be configured at two levels:

- **Team-scoped:** Configured in the Vercel dashboard. Applied to all requests from the team by default.
- **Request-scoped:** Passed per-request via `providerOptions.gateway.byok`. Overrides team-scoped credentials for that request.

```javascript
providerOptions: {
  gateway: {
    byok: {
      anthropic: [{ apiKey: process.env.ANTHROPIC_API_KEY }],
      openai: [{ apiKey: process.env.OPENAI_API_KEY }],
    }
  }
}
```

Multiple credentials per provider are supported. If a BYOK credential fails, the gateway automatically falls back to system (Vercel-managed) credentials. BYOK requests also carry zero markup on token costs.

---

## 6. SDK and Language Support

The gateway is language-agnostic. While the primary SDK is the Vercel AI SDK (TypeScript, versions 5 and 6), the OpenAI-compatible endpoint means any language with an OpenAI client library can use the gateway.

**TypeScript (AI SDK)**

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Hello world'
});
```

**Python (OpenAI SDK)**

```python
from openai import OpenAI

client = OpenAI(
  api_key=os.getenv('AI_GATEWAY_API_KEY'),
  base_url='https://ai-gateway.vercel.sh/v1'
)

response = client.chat.completions.create(
  model='anthropic/claude-sonnet-4.5',
  messages=[{'role': 'user', 'content': 'Hello'}]
)
```

**cURL / Direct HTTP**

```bash
curl https://ai-gateway.vercel.sh/v1/chat/completions \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "anthropic/claude-sonnet-4.5", ...}'
```

---

## 7. Ecosystem Integrations

### 7.1 Framework Integrations

The gateway integrates with major AI development frameworks, extending its reach well beyond the Vercel AI SDK:

| Framework | Integration Details |
|---|---|
| **LangChain** | Direct integration via OpenAI-compatible endpoint |
| **LlamaIndex** | Dedicated package: `llama-index-llms-vercel-ai-gateway` |
| **Mastra** | Native integration support |
| **Pydantic AI** | Native `VercelProvider` class |
| **LiteLLM** | Route through gateway endpoint |
| **Langfuse** | Observability integration for tracing and evaluation |

### 7.2 Chat Platform Integrations

Several open-source chat interfaces can use the AI Gateway as a backend, providing a UI layer on top of the gateway's routing and model access:

- **LibreChat:** Open-source ChatGPT alternative with multi-model support.
- **OpenClaw (Clawdbot):** Claude-focused chat interface.
- **Open WebUI:** Extensible web interface for LLM interaction.
- **Chatbox:** Desktop/mobile chat client.

All route through `ai-gateway.vercel.sh` as the backend endpoint.

### 7.3 Developer Tool Integrations

The Cline VS Code extension uses the AI Gateway as its recommended backend, and Claude Code integration is referenced in the official documentation.

---

## 8. Pricing

> **Zero Markup:** Vercel charges no markup on token costs. Developers pay the same per-token rate as going directly to providers, including when using BYOK credentials.

### 8.1 Free Tier

Every Vercel account receives a $5/month credit, which resets every 30 days from the date of the first request. This credit covers token costs at provider rates. No credit card is required.

### 8.2 Paid Tier

Once a developer makes their first credit purchase, the free monthly credit stops. The paid tier is pure pay-as-you-go: purchase credits, use them until depleted, and configure auto top-up thresholds to avoid service interruptions.

### 8.3 Additional Costs

- **Web Search:** $5 per 1,000 requests for both Perplexity Search and Parallel Search.
- **Observability Plus:** Additional cost for extended data retention (pricing not publicly listed).
- No per-request fees, no minimum commitments, no seat-based pricing.

---

## 9. Case Study: Cline

Cline, a popular AI coding assistant VS Code extension, migrated to Vercel AI Gateway as its recommended backend. The published results:

| Metric | Result |
|---|---|
| **P99 Latency Improvement** | 10-14% reduction |
| **Error Rate Reduction** | 43.8% drop |
| **Routing Overhead** | Sub-20ms |
| **Global Coverage** | 100+ PoPs, private backbone |

The case study emphasizes that the gateway's value is not just cost savings but operational reliability: automatic failover, reduced error rates, and consistent latency across geographies.

---

## 10. Known Limitations and Gaps

- No self-hosted or on-premise deployment option. The gateway runs exclusively on Vercel infrastructure.
- Observability is built-in but relatively basic compared to dedicated platforms like Langfuse, Helicone, or Datadog. Langfuse integration exists for teams needing deeper tracing.
- Provider support, while broad, depends on Vercel maintaining each integration. New provider models may have a delay before appearing in the gateway.
- The model-fallback documentation page returned a 500 error during this research, suggesting this feature may still be under active development or documentation updates.
- No public SLA documentation was found during this research. Enterprise reliability guarantees are unclear.

---

## 11. Timeline

| Date | Event |
|---|---|
| **May 20, 2025** | Alpha launch announced via blog |
| **August 21, 2025** | General availability announced |
| **February 2026** | 35+ providers, 100+ PoPs, ecosystem integrations mature |

---

## 12. Research Methodology and Notes

This analysis was compiled from the following vercel.com sources, accessed in February 2026:

- vercel.com/ai-gateway (product landing page)
- vercel.com/docs/ai-gateway (main documentation hub)
- vercel.com/docs/ai-gateway/capabilities (capabilities overview)
- vercel.com/docs/ai-gateway/models-and-providers/provider-options (provider routing)
- vercel.com/docs/ai-gateway/capabilities/web-search (web search tools)
- vercel.com/docs/ai-gateway/pricing (pricing details)
- vercel.com/docs/ai-gateway/authentication-and-byok/byok (BYOK mechanics)
- vercel.com/docs/ai-gateway/capabilities/observability (observability features)
- vercel.com/docs/ai-gateway/ecosystem (framework integrations)
- vercel.com/docs/ai-gateway/chat-platforms (chat platform integrations)
- vercel.com/blog/ai-gateway (alpha announcement, May 2025)
- vercel.com/blog/ai-gateway-is-now-generally-available (GA announcement, August 2025)
- vercel.com/blog/cline-on-ai-gateway (Cline case study)

> **Accuracy Note:** One claim from an earlier draft (OIDC token authentication) could not be verified from any scraped source and has been removed from this document. The model-fallbacks documentation page returned a 500 error and could not be fully reviewed. All other claims have been cross-referenced against at least one primary source.
