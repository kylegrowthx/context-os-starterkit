# Example Submission: Live Working Session Format

*This simulates what a strong candidate would walk through in a collaborative, less polished working session. Written as a transcript/guide of how they'd talk through their thinking, including questions back to the panel.*

---

## How This Would Flow

The candidate shares their screen with a rough notes doc or whiteboard. They talk through their thinking, pause to ask questions, and adapt based on the panel's reactions. It feels more like a working meeting than a presentation.

---

## Opening (2-3 minutes)

"Thanks for sharing this. I want to be upfront: I spent a full day on this and I have opinions, but I also have a lot of questions. You've been building this for four months. I've been looking at it for a day. I'd rather have a real conversation than pretend I know more than you do.

Here's what I want to walk through:

1. What I noticed using the product and what I think you got right
2. How I read the strategy doc through the lens of what's shipped
3. What I'd focus on next, given the team you have
4. Questions I need answered before any of this becomes a real plan"

---

## Part 1: Product Observations (8-10 minutes)

"Let me share my screen. I took notes as I used the product.

First thing I want to say: the shared prompt library is really well done. Most B2B tools make you configure everything before you see value. CheckThat inverts that. I was seeing how AI perceives brands in my category within minutes. That's a strong foundation for organic growth. People land on a category page, see real data, and have a reason to sign up.

That tells me you prioritized the open index first. Which makes sense. You need traffic before you need monetization features."

**[PAUSE - Question to panel]**

"Am I reading that right? Was the open index and the tracking infrastructure the deliberate first bet?"

*This shows the candidate checking their assumptions rather than bulldozing ahead with a critique.*

"So here's where I got curious about what's next. I tracked [brand] and I could see my recall rate across engines. Good data. But I kept asking myself: what am I supposed to do with this?

The strategy doc has this beautiful vision of alignment scoring. 'We tell you if AI is right.' That's the feature that would have kept me in the product for another hour. Right now, I understand what AI says about my brand. I don't yet understand whether it's right or what to do about it."

*Opens the strategy doc*

"The thing I appreciate about this document is the three-layer model. Context, Instruments, Measurement. And when I map it against the product, the sequencing makes total sense."

*Draws on whiteboard/shared doc*

```
SHIPPED (strong):
  Layer 2: Instruments ✓ (shared library, custom prompts, tracking)
  Layer 3: Measurement (partial) ✓ (recall, basic sentiment)

NEXT:
  Layer 1: Context (brand truth = the "answer key")
  Layer 3: Measurement (alignment, composites, recommendations)
```

"You built bottom-up. Instruments first because that's the organic growth engine. Recall metrics because that's the most straightforward measurement. And you deferred Context and Alignment because they're connected: you can't measure alignment without context.

With three engineers in four months, I think that was the right call."

**[PAUSE - Question to panel]**

"What did you have to cut that was hardest to let go of? I'm curious what was on the bubble."

*This question reveals a lot. It shows the candidate thinks about prioritization as giving things up, not just choosing what to build.*

---

## Part 2: What I'd Focus On Next (10-12 minutes)

"OK, so here's where I want to think out loud with you. The team is three engineers, a designer as needed, and a PM. That's real constraints. We can't do three things in parallel. Maybe two if we're careful."

### Focus 1: Brand Context

"The strategy doc says context is the foundation. I agree. But I'm thinking about this practically.

If we ask users to fill in a full brand context profile before they get value... they won't do it. The product already works without it. So we can't gate anything on context.

Here's what I'd experiment with:"

*Sketches on whiteboard*

```
Current flow (works well):
  Signup → See shared library data → Track your brand → See recall

New flow (additive):
  Signup → See shared library data → Track your brand → See recall
                                                           |
                                              "Want to know if AI
                                               is RIGHT about you?"
                                                           |
                                              3-field brand context:
                                              - Your positioning
                                              - Top differentiators
                                              - Key competitors
```

"Three fields. Not fifteen. Not the full brand context from the strategy doc. Just enough to run a basic alignment check. We can progressively ask for more context over time.

The key insight: context isn't onboarding friction if it's positioned as an upgrade path. 'You've been tracking your brand for a week. Want to see if AI actually gets you right? Tell us who you are.'"

**[PAUSE - Question to Daniel]**

"Is the data model ready for this? Could you layer a structured brand context on top of what's built, or would it require rethinking the schema?"

*This is a technical feasibility question that shows the candidate thinks about implementation, not just strategy.*

### Focus 2: Alignment (Basic)

"Once we have even basic context, we can do something nobody else does. Take a branded prompt like 'What is [Brand]?' and compare the AI response against the user's stated positioning.

I'd start super simple. Not the full alignment scoring system from the strategy doc with six sub-metrics. Just:"

*Draws on whiteboard*

```
You say:    "We're a finance automation platform"
AI says:    "Ramp is an expense management tool"
Gap:        Positioning mismatch

You say:    "Free, Plus ($12/user/mo), Enterprise"
AI says:    "Ramp pricing starts at $15/user/month"
Gap:        Pricing inaccuracy
```

"That's it. Show specific gaps in plain language. No composite scores yet. No weighted algorithms. Just: here's what you said, here's what AI said, here's where they don't match.

**Question for Marcel:** When you wrote the alignment section of the strategy doc, were you thinking this needed to be sophisticated from day one? Or could a simple 'does AI match what you told us?' be the v1?"

*Engaging the CEO directly on his vision, showing the candidate can push back respectfully.*

### Focus 3: Competitive as Default

"This one might be the quickest win. The data already exists to show my brand alongside competitors. If we just change the default dashboard to show the competitive view..."

*Pauses*

"Actually, I want to check something. Does the product already support adding competitors when you sign up?"

**[Question to panel]**

*Adapting based on real-time information rather than presenting a rigid plan.*

"If competitors are already in the data model, this could be a 1-2 week project. Just rearrange what's shown by default. Big perception impact, small engineering lift."

---

## Part 3: Things I'm Genuinely Uncertain About (5 minutes)

"Here's where I want to be honest about what I don't know.

**I don't know what early traction looks like.** You launched two weeks ago. Are people signing up? Which pages drive traffic? Are users coming back? The answers to these questions could completely change my priorities. If nobody's signing up, we have a distribution problem, not a feature problem.

**I don't know the team's velocity.** 'Three engineers, four months' gives me a rough sense of what's possible. But I don't know what's load-bearing in the codebase, what's quick to change, and what would require significant refactoring. The alignment pipeline in particular could be a week or a month depending on the architecture.

**I'm uncertain about LLM-as-judge reliability.** The strategy doc proposes it for alignment scoring. It's the right approach conceptually. But in practice, I've seen LLM-as-judge produce inconsistent results, especially for nuanced evaluations like 'does this positioning match?' I'd want to run a calibration study before committing to this approach.

**I don't know how the editorial function works.** A lot of what makes CheckThat special is editorial quality. The shared prompt library, category pages, quality scoring. If the editorial team is one person, that changes how I'd think about features that need editorial judgment, like alignment evaluation."

---

## Part 4: What I'd Want to Do in Week 1 (3-5 minutes)

"If you hired me, here's what my first week looks like:

**Monday-Tuesday:** Sit with Daniel and go through the codebase. Not to write code yet, but to understand what's built, what's easy to extend, and what's fragile. I need to know what 'two-week project' actually means here.

**Wednesday:** Talk to early users. Five to ten calls. 'Why did you sign up? What did you do first? What confused you? Would you pay? Why or why not?' I want their language, not my assumptions.

**Thursday:** Sit with each engineer one-on-one. Understand what they're proud of, what frustrates them, what they'd build next if it were up to them. They've been living in this codebase for four months. They know things I don't.

**Friday:** Write the actual plan based on what I learned. Not this assignment, which is based on a day of exploration. The real plan, informed by the codebase, the users, and the team."

---

## Closing

"That's my thinking. I deliberately didn't try to have all the answers. You've been building this for four months and thinking about it longer. I've had a day. What I wanted to show you is how I'd approach it: respect what's been built, understand why you made the choices you made, and build on that foundation with the team you have.

What questions do you have for me?"

---

## Why This Format Works

The working session format reveals things the other formats don't:

- **Respect for existing work.** The candidate opens with "you built the right thing first" and asks "what was hardest to cut?" rather than listing failures.
- **How they handle "I don't know."** They admitted uncertainty four times without being defensive.
- **How they collaborate.** They asked 5+ questions to the panel, adapting their thinking in real-time.
- **Product instinct in action.** The progressive context idea (3 fields, not 15, as an upgrade path rather than onboarding friction) showed real UX thinking.
- **Team awareness.** They referenced the specific team composition multiple times and allocated work to specific engineers by strength.
- **How they'd actually work with you.** This session is a preview of weekly product discussions.

The trade-off: less polish, less depth on any single topic, and quality depends heavily on the candidate's verbal communication skills.
