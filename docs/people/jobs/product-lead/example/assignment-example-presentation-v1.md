# Example Submission: Presentation Format

*This simulates what a strong candidate would present in a 30-45 minute session with slides or a doc walkthrough.*

---

## Slide 1: My Take in 30 Seconds

You built the right thing first.

The strategy doc describes a three-layer system: Context, Instruments, Measurement. After four months with three engineers, you shipped a strong Instruments layer and solid Recall metrics. That was the right call. You needed the tracking infrastructure and the open index to prove organic traction before building the higher-order features.

Now you have a foundation. The question is: what do we build on top of it next to unlock the vision in this strategy doc, with the team we have?

My recommendation: **Context first, then Alignment.** Those two things together turn CheckThat from a tracking tool into the brand research platform this document describes.

---

## Slide 2: What I Observed Using the Product

I spent several hours with CheckThat. Tracked two brands across different categories. Explored the open index. Here's what stood out.

**What you nailed:**
- **Immediate value.** I was seeing how AI perceives brands in my category within minutes of signing up. No setup friction. The shared prompt library does the heavy lifting. That's the open index strategy working exactly as designed.
- **Category pages.** Well-structured, data-rich, and clearly built for organic discovery. These should compound over time.
- **Tracking infrastructure.** Multi-engine probing works reliably. Data updates are consistent. The core plumbing is solid.

**Where I got curious about what's next:**
- I see my recall rate is 65%. I want to know: is that good? How does it compare to competitors in my category? The data is there but the competitive framing isn't the default view yet.
- The relationship between shared prompts and custom prompts could be clearer. When should I add my own vs. rely on what's there?
- I finished my session understanding what AI says about my brand. I didn't yet understand what to DO about it. That feels like the next unlock.

**What I think you intentionally deferred:**
- Brand context capture (Layer 1). You prioritized getting the tracking engine running first. Makes sense with the team size.
- Alignment scoring (Layer 3). Can't build this without context. Right sequencing.
- Composite scores. These depend on the layers below them. You can't skip ahead.

I read the strategy doc after using the product, and the prioritization logic clicked.

---

## Slide 3: Where We Are vs. Where We're Going

| Layer | Strategy Doc Vision | What's Shipped | What's Next |
|---|---|---|---|
| **Context** | Structured brand truth (positioning, personas, differentiators) as the "answer key" | Basic company info auto-populated | Guided context onboarding |
| **Instruments** | Multi-dimensional classification, prompt clusters, quality scoring | Shared library, custom prompts, multi-engine tracking | Clustering, quality tiers visible to users |
| **Measurement** | Recall, Sentiment, Alignment, Lift + composites | Recall metrics, basic sentiment | Alignment scoring, composites, recommendations |

The Instruments layer is strong. That's the foundation. The next big unlock is connecting Context (Layer 1) to Measurement (Layer 3) through Alignment scoring. That's the feature nobody else has.

---

## Slide 4: What I'd Build Next (With This Team)

Three engineers, a designer as needed, one PM. That's real constraints. I'd sequence tightly and ship incrementally.

### Phase 1: Brand Context (Weeks 1-4)

Start small. Three fields, not fifteen:
- Your positioning in one sentence
- Top 3 things you want AI to know about you
- Your top 2-3 competitors

Pre-populate what we can from public data and existing index data. Make it completable in under 5 minutes. This creates the "answer key" for alignment without blocking activation.

**Team allocation:** One engineer builds the data model and API. Designer creates the onboarding flow. PM coordinates with editorial on what fields matter most.

### Phase 2: Alignment Scoring (Weeks 3-7)

With even basic brand context, we can run alignment checks. Start with branded prompts ("What is [Brand]?", "[Brand] pricing") and compare AI's response against what the user told us.

Use LLM-as-judge with structured evaluation. Start with three dimensions: Feature Accuracy, Positioning Match, Factual Accuracy. Show specific gaps: "AI says you're an expense tool. You say you're a finance platform."

**Team allocation:** Backend/architecture engineer builds the evaluation pipeline. Generalist engineer builds the UI for showing alignment results. UI engineer improves the dashboard to surface scores.

### Phase 3: Competitive View + Recommendations (Weeks 6-10)

Make the default dashboard show your brand alongside competitors. Then add simple recommendations based on the biggest gaps: "Your recall is strong but AI gets your pricing wrong. Here's what to update."

**Skip for now:**
- Multi-turn tracking (strategy doc agrees: defer to v2)
- Custom-to-shared promotion (not enough volume yet)
- Prompt clustering (important but not blocking the core value unlock)

---

## Slide 5: The Big Bet

**Brand context becomes competitive intelligence.**

When users fill in their brand context, they're creating structured data about how they position themselves. Over time, with permission, this creates a layer of data that doesn't exist anywhere else: what brands SAY they are vs. what AI SAYS they are.

Imagine a category page that shows not just AI perception, but stated positioning for every tracked brand. That's the G2/Glassdoor dynamic: companies contribute data because the ecosystem benefits them.

The context feature we build now is the seed for this. Design the data model to support it from day one, even if we don't expose it publicly yet.

---

## Slide 6: Questions I'd Want to Answer First

1. **What does early traction look like?** You launched two weeks ago. What are the signup numbers? Which category pages are getting traffic? This tells me if the organic thesis is proving out.

2. **Why did you sequence the way you did?** I have a hypothesis (instruments first to prove organic traction) but I want to hear the actual reasoning. There may be constraints I'm not seeing.

3. **What's the engineering team's velocity like?** "3 engineers, 4 months" gives me a rough sense, but I'd want to understand what a "2-week project" actually means in this codebase.

4. **How are you thinking about the editorial function?** Alignment scoring needs judgment calls (what counts as a "correct" positioning match?). Is this automated, editorial, or hybrid?

5. **What's the relationship between CheckThat and GrowthX's services business?** If Business tier customers become GrowthX service clients, that changes which conversion path matters most.

---

## Slide 7: Summary

| What | Why | Timeline | Team |
|---|---|---|---|
| Brand Context | Creates the "answer key" for alignment | Weeks 1-4 | 1 eng + designer |
| Alignment Scoring | The killer differentiator | Weeks 3-7 | 2 eng |
| Competitive View + Recs | Makes the product actionable | Weeks 6-10 | 1 eng + designer |
| Context-as-Intelligence | Long-term moat | Design now, build later | Architecture eng |

You shipped the tracking engine. Now connect it to meaning. Context gives us the answer key. Alignment tells users if AI is right. Recommendations tell them what to do about it.

One sentence: **The product tracks what AI says. The next step is telling users whether AI is right, and what to do about it.**
