# Image sync w GrowthX

<metadata>
date: 2026-01-20
time: 21:00 UTC
duration: 20 minutes
organizer: team@growthxlabs.com
participants:
  - name: Aida Knezevic
    affiliation: GrowthX
    email: aida@growthxlabs.com
    role: Engagement Manager
  - name: Steve Raikow
    affiliation: Cresta
    email: steve.raikow@cresta.ai
    role: Creative Director
  - name: Katia Pembayun
    affiliation: GrowthX
    email: katia@growthx.ai
    role: Designer
fathom_recording_id: 115764225
fathom_url: https://fathom.video/calls/536817541
share_url: https://fathom.video/share/ZkmyQwW5q4MFg5B12yqHtfF-HQkxuecx
source: fathom
enriched_on: 2026-02-28 15:30 UTC
</metadata>

---

## Summary

GrowthX and Cresta aligned on a scalable AI image generation workflow for the new cresta.com/guides section, publishing 5 guides per week. The team will test two visual tracks—abstract (data/tech textures, icons) and photographic (NanoBanana with muted palette)—using 6–10 focused reference images per pipeline to maintain consistency and avoid style dilution, with rapid iterative feedback via a shared Figma workspace.

---

## Context

Cresta launched a new guides section on cresta.com to publish educational content targeting different customer pain points, with 5 posts per week. GrowthX is executing the content strategy, but needed to establish a scalable, on-brand visual identity for the guide posts. Previously, the site used generic stock imagery, creating inconsistency with Cresta's brand and failing to communicate technical credibility. This meeting brought together GrowthX's content and design leads with Cresta's Creative Director to define the image generation pipeline, identify visual constraints (avoiding contact-center clichés), and establish a collaborative workflow using AI models (NanoBanana and GPT) steered by curated reference assets and templated art direction.

---

## Relevance

**Content Operations & Brand**
- Defines visual consistency strategy for Cresta's guide section, essential for brand alignment across high-volume publishing cadence
- Addresses technical credibility signals through deliberate visual language (data textures, abstract technical motifs vs. contact-center stereotypes)

**Design & Creative Direction**
- Establishes repeatable AI image generation pipeline to scale design output to 5 posts/week without proportional design effort
- Tests dual visual approaches (abstract vs. photographic) to identify which performs better for Cresta's audience and reduces iteration time

**Client Collaboration & Process**
- Models collaborative feedback loop with external Creative Director using shared Figma workspace, enabling rapid iteration and client buy-in
- Demonstrates practical constraints of AI image generation (reference set size, style dilution, prompt strategy) and workarounds for scalability

---

## Overview

- Volume + lead time → 5 guide posts/week; 1-week content calendar available to plan image batches
- ImageGen pipeline → NanoBanana + GPT with templated art direction; steer via 6–10 focused reference images to avoid style dilution
- Direction test plan → Explore two tracks: abstract (more purely abstract, data/tech textures, icons) vs photography (NanoBanana; muted palette, controlled lighting); avoid “contact center” clichés (no headsets), prefer “knowledge workers” or customers on phone/chat
- Collaboration loop → Shared Figma for assets, examples, and outputs; Steve to supply larger asset/guidance set; Katia to iterate and post outputs for fast feedback

---

## Key Topics

### Publishing cadence and planning

  - Target cadence → 5 images/week for cresta.com/guides
  - Lead time → At least 1 week of topics via GrowthX content calendar
  - Practicality concern → Approach must scale with minimal per‑post design time

### Current ImageGen workflow (GrowthX)

  - Models/APIs → NanoBanana and GPT
  - Input strategy → Topic title as mini‑prompt by default; switchable to full-article content prompt
  - Art direction → Templated baseline + small set of reference images guide outputs
  - Reference images count → 6–10 recommended; more causes style dilution and inconsistency

### Reference assets needed from Cresta

  - Asset types → Human imagery style refs (lighting, muted palette), abstract textures, icons, waveform/chat motifs, do/don’t examples
  - Scope → Larger set than 6–10 for team context; Katia will select a focused subset for the pipeline
  - Goal → Tighten alignment with Cresta brand; reduce variability vs current mixed blog styles (2D, 3D, photos)

### Style direction and constraints

  - Human imagery → Possible via NanoBanana; quality improved recently
      - People depiction → “Knowledge workers” or customers (phone/chat/text); avoid headsets and call-center tropes
      - Look/feel → Neutral/muted palette; specific lighting direction
  - Abstract track → If abstract, lean fully abstract (avoid quasi‑literal graphics that suggest specific objects without relevance)
      - Visual language → Data/technical textures, waveforms, chat bubbles, up‑and‑to‑the‑right graphs, icons over abstract backgrounds
  - Decision approach → Run both tracks (abstract vs photographic) and compare outputs for fit, speed, and consistency

### Feedback on current outputs

  - Issue → Too literal without semantic tie-in to article topics; creates confusion
  - Adjustment → Either increase abstraction (non-representational) or ensure clear, topic-relevant visual metaphors
  - Practical simplification → Consider photography or abstract backgrounds with one or more brand icons overlayed for clarity + scalability

### Collaboration workflow

  - Workspace → Figma as the single shared surface
      - Steve → Populate assets, references, do/don’t notes
      - Katia → Post iterative outputs, maintain two pipelines (abstract vs photo), tweak lighting/art direction, annotate changes
  - Review loop → Share small batches; Steve provides rapid, specific feedback to converge on a repeatable template

---

## Action Items

**Aida Knezevic (GrowthX)**
- Share the 1-week content calendar with Steve Raikow (Cresta)

**Steve Raikow (Cresta)**
- Send Katia Pembayun (GrowthX) a larger collection of reference images, including human imagery style references (lighting, muted palette), abstract textures, icons, waveform/chat motifs, and specific do/don't guidance
- Build out and share Figma file with Katia Pembayun (GrowthX) containing additional assets, examples, and notes on preferred overlays and strict exclusions (e.g., no contact-center headset imagery)

**Katia Pembayun (GrowthX)**
- Set up Figma page to drop in image generation results for Steve Raikow (Cresta) review and feedback
- Configure and test two parallel pipelines: abstract/illustrative track (GPT-based, data/tech textures, icon overlays) and photographic track (NanoBanana, muted palette, controlled lighting)

---

## Transcript

**Aida Knezevic:** Hi, everyone. The meeting is being recorded. Thank you for hopping on.

**Steve Raikow:** Hi, Katia. Yeah, it's nice to meet you all.

**Katia Pembayun:** Nice to meet you, too.

**Aida Knezevic:** Just to do a quick intro—I'm Aida, the Engagement Manager at GrowthX. I'm the main point of contact for everything content-related for Cresta.

**Steve Raikow:** You know me from Slack, and Katia is our designer here. I'm Steve, Creative Director at Cresta. Thank you for putting time together. I have some fundamental questions because I haven't been very involved in the GrowthX project. I want to make sure I understand some basic things before trying to come up with a solution. So we'll be posting content on a regular basis—are these blog posts?

**Aida Knezevic:** Yeah, five per week on the guide section. So you have a new guide section on your website. Right now we're using free stock images.

**Steve Raikow:** Is this live now?

**Aida Knezevic:** Yes. If you go to cresta.com/guides, you should be able to see it.

**Steve Raikow:** I didn't even know this was up yet. Okay, and how much lead time do we have before these go live? Do we know the roadmap for the coming month?

**Aida Knezevic:** Yes, we have a content calendar. At least a week before articles go live, we know which ones we're working on.

**Steve Raikow:** Can that be shared with me? Because we can talk about specific imagery and guidance.

**Aida Knezevic:** Yeah, let me pull it up for you. As part of our content strategy, we're publishing educational content targeting different pain points, plus commercial content like product comparisons. As part of our workflows, we build AI image iteration at the end. We typically use the brand guidelines to guide that. We've found that AI still doesn't do a good job with realistic human imagery, so we do graphics or abstract illustrations instead. We shared some examples in Slack a few weeks back. I think this is version 23, Katia. These felt closest to Cresta's brand guidelines, so I thought they'd be a good baseline.

**Steve Raikow:** The challenge is coming up with a simple approach to meet this volume. Five posts a week is a lot. How do we know what's practical to keep up with this volume without doing massive design effort each time?

**Aida Knezevic:** We categorize the content under different thematic clusters. There are seven clusters we're targeting. We want a template that is repeatable without being too repetitive. The content itself is where we pay a lot of attention. The AI Gen workflow needs to be on brand, but I'll let Katia speak to how we build it out.

**Katia Pembayun:** I'm happy to. I'll share my screen. Our ImageGen workflow uses two APIs: NanoBanana or GPT. We use reference images your team shared as a baseline. Our workflow takes the topic title for each article and generates an image based on that text. We could also use the actual article content. We have a templated art direction that guides the imagery. I'd recommend around 6 to 10 reference images maximum, because more gets diluted. Currently, Cresta's blog images are pretty varied in style—some are 2D illustration, some 3D rendering. I have a pre-selection of reference images with a mix of that.

**Steve Raikow:** So in terms of steering the model, we can feed it more sample imagery?

**Katia Pembayun:** Yes. I'd recommend 6 to 10 max, because it gets diluted if you add too much. Currently your blog images are really varied in style.

**Steve Raikow:** If we put too much in there, it's not focused enough?

**Katia Pembayun:** Yeah, definitely. I do have a test pipeline with photography using NanoBanana if that's something interesting.

**Steve Raikow:** The photography looks honestly a lot closer. It's gotten a lot better recently. I can provide a larger set of reference images—human imagery, abstract textures, icons, all on brand. It's more than 6 images, but would that be useful to help steer this?

**Katia Pembayun:** Yeah, definitely. If we're closer to your ideal approach and those specific assets, that would be super helpful. I've mostly gotten a few and taken what I can reference from the website.

**Steve Raikow:** Regarding the current images, I feel like we're not quite there. It's almost like we're too abstract. I'm not seeing the connection to what we're showing. If we're going to create abstract stuff, it needs to be more purely abstract so viewers aren't trying to decipher what it is. Let me send you a larger collection with more specific notes on what we can include and what we definitely don't want. On the stock photography currently, there's a lot of emphasis on traditional contact center imagery. We're really trying to avoid that. Instead of showing agents, just show knowledge workers—or customers on the phone, chat, or texting. I have icons, waveforms to represent conversations, chat icons, and abstract representations of data or technical concepts. Or maybe just an image with an icon on top—like a knowledge worker with an up-and-to-the-right graph. That could be simple.

**Katia Pembayun:** That's super helpful to see and visualize what you're thinking. That'll help when I'm tweaking the pipeline.

**Steve Raikow:** I'll add more assets about abstract textures. I'm not sure if we want to go more abstract or more realistic. Maybe we can see what kind of output we get when we try both directions and see which works better. I'll build this out and share it with you directly. If you send me examples of results, I can give much quicker feedback. We can iterate until we're happy with where it lands.

**Katia Pembayun:** That sounds great. I'll set up a Figma page on my end and drop in results once you share the assets. Do you want to share your Figma with me and I just put my stuff in there?

**Steve Raikow:** I could definitely do that. Just share that with me and I'll start populating it. Send me a note when there's something ready for me to look at.

**Katia Pembayun:** Sounds good.

**Aida Knezevic:** We're trying to figure this out as we go. Every client we work with is different. Thank you so much for your time.

**Steve Raikow:** We'll follow up with the Figma file and then take it from there.

**Aida Knezevic:** Thank you, Steve.

**Katia Pembayun:** Bye.
