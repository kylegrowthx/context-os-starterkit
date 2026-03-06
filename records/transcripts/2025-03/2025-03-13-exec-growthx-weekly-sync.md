# Exec <> GrowthX Weekly Sync

<metadata>
date: 2025-03-13
time: 20:59 UTC
duration: 30 minutes
organizer: Elvis Goren
participants: Elvis Goren, Kyle Gaudreau, Sean Linehan
fathom_recording_id: 51855139
fathom_url: https://fathom.video/calls/252348958
share_url: https://fathom.video/share/Ut1jbU6ekyVHhuKffpJM1iXkpzt6sK88
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

GrowthX and Exec aligned on three strategic priorities for their content partnership: adjusting article tone to empower rather than criticize the L&D audience (moving away from LLM tendencies to "punch down"), implementing GPT-powered tools for objection handling and call script generation on Exec's platform, and developing a taxonomy for article categorization to improve SEO and content hierarchy. Sean demonstrated the platform's capabilities and confirmed GrowthX has CMS access; articles will remain in draft for his review before publishing, with Sean preferring to monitor and iterate post-publication rather than blocking the process.

---

## Context

GrowthX is providing content marketing services to Exec, a talent development software platform. The partnership involves producing articles for Exec's website (30+ articles planned initially, scaling to 1,200+) with GrowthX handling article drafting and Exec's team (Sean Linehan) overseeing strategy, tone, and platform configuration. Sean's emphasis on audience sensitivity reflects Exec's positioning: their customers are L&D professionals who feel under-resourced rather than incompetent, so content must empower rather than criticize. This is the standing weekly sync between Elvis Goren (GrowthX) and Sean Linehan (Exec), with Kyle Gaudreau (GrowthX leadership) providing strategic input on content strategy, personas, and templating.

---

## Relevance

- **To GrowthX Delivery:** LLM-generated content requires tone adjustment, particularly avoiding "punching down" language toward audiences (e.g., "useless metrics"). Kyle noted the need to build persona-specific templates and separate content tone/structure for different audience segments (L&D vs. sales) within Exec's platform. GrowthX now has CMS access and can draft articles for review rather than requesting access per article.

- **To GrowthX Business Development:** Strong account momentum—30+ articles already drafted, scaling to 1,200+. Sean is comfortable auto-publishing once configuration is correct, suggesting confidence in the partnership. Exec's integrated learning management system reveals product depth and sophistication; potential for cross-selling or showcasing this capability to other clients.

- **To CheckThat / AI Quality:** GPT model selection matters (Sean showed updating from 3.5 turbo to 4.0), and LLM tendencies toward certain tones are observable and correctable through prompt engineering. Kyle flagged the challenge of balancing empathy, directness, and aspiration in prompts—a key AEO consideration for brand voice consistency across AI-generated content.

---

## Overview

- Adjust tone in articles to avoid "punching down" on L&D professionals; focus on empowering rather than criticizing
- Implement GPT-powered tools for objection handling (two-input boxes: customer objection + broad answer, generates call script)
- Develop a taxonomy for categorizing articles and series to improve SEO and content organization
- GrowthX team now has CMS access; articles can be drafted for Sean's review before publishing
- Sean prefers to monitor and iterate post-publication rather than blocking; images are acceptable for blog content at scale

---

## Key Topics

### Content Tone and Audience Sensitivity

  - Sean emphasized never implying customers/target audience are incompetent; Exec's L&D audience feels under-resourced, not incapable
  - LLMs tend to "punch down" and criticize L&D teams, which is counterproductive for Exec's positioning
  - Shift tone to: "You're smart and strategic; you're not doing effective things because you lack tools and resources" instead of "You're stupid and useless"
  - Different audience personas (L&D vs. sales) require different tones; need to avoid one-size-fits-all approach

### GPT Integration for Content

  - Sean demonstrated that adding GPT tools to Exec's platform is simple and fast (15-20 minutes)
  - Objection handling tool design: "Workshop your objection handling" with two inputs: (1) Customer objection, (2) Your broad-strokes answer → generates polished call script
  - Sean recommended using GPT-4.0 instead of 3.5 Turbo for better quality outputs
  - Secondary use case: Generate lists of common objections by business type, allowing users to select and workshop responses one at a time
  - Sean will send Elvis specific requirements (title, subtext, input fields, output shape); Elvis will provide GPT ideas via Slack

### Content Categorization and SEO

  - Exec's platform supports nested hierarchies: articles → series → parent series, enabling strong site structure and spider-ability for Google
  - Exec populates homepage with most-viewed series; older/low-traffic content appears in reverse chronological order
  - GrowthX needs to propose article taxonomy and category structure to Sean (topics, groupings, other organizational layers)
  - Categories are easy to set up (title, at least one article, slug); Sean has already created baseline categories for published articles
  - Integration with Exec's learning management system allows articles to be embedded directly in learning programs

### CMS Access and Publishing Process

  - Elvis confirmed GrowthX team now has CMS access to Exec's platform
  - Articles should be left in draft for Sean's review before publishing
  - Sean focuses on verifying configuration is correct so articles publish properly when they go live
  - Sean's publishing philosophy: Close enough on tone, focus on configuration, then monitor post-publication and iterate rather than blocking; he's comfortable with auto-publishing once configuration is proven solid
  - This approach trades off some pre-publication review for speed and ability to optimize high-traffic content

### Image Quality and Optimization Strategy

  - Current image quality is acceptable for blog content at scale (1,200+ articles)
  - Sean's approach: Use Google Analytics to identify high-traffic articles, then invest in higher-quality images for those pieces
  - Not worth polishing images for low-traffic content; optimization ROI matters
  - Future tweaks: Consider adjusting prompts for more color variability in generated images

---

## Action Items

**Elvis Goren (GrowthX)**
- Update content workflows and prompts to avoid "punching down" on L&D audience; shift to empowerment framing ("you lack resources" not "you're incompetent")
- Send GPT tool ideas to Sean via Slack for rapid implementation
- Workshop objection handling GPT tool requirements with Sean—define inputs (objection, broad answer), output format (call script), and use cases
- Develop article category taxonomy for Exec; consider topic groupings, persona-based separation, and SEO-friendly hierarchy; share with Sean for feedback

---

## Transcript

**Elvis Goren:** Okay interesting. Home life is just sometimes chaotic, it can be. I'm sure you've got a kid.

**Kyle Gaudreau:** Well, Daisy's sick, especially. Is he sick now? No. Yeah, I mean, we just jinxed it, so he's definitely going to be soon. Yeah, it's not good.

**Elvis Goren:** Stay away from those topics.

**Kyle Gaudreau:** Yeah he's doing good. Cool.

**Elvis Goren:** I was going to say, I think someone found a writer. We can trial them whenever. So we'll talk about what that looks like another time. We're definitely hiring folks and I've got support on the recording side now, which makes it easier. We're also leveraging a staffing agency for some of this. Sean, what's up—how are you doing?

**Kyle Gaudreau:** I'm doing great.

**Sean Linehan:** Good to hear.

**Elvis Goren:** Let's dive right in, shall we? Let me share the agenda. Essentially, I want to talk about the GPT tool idea we had last time and develop it a bit. It's a good opportunity to do some programmatic stuff and lead capture. We have over 30 articles at this point, so we want to get to a point where you're comfortable with the tone and cover images. We also want to confirm how you'd like us to reference Exec in the articles—whether as "Exec" or "exec.com."

**Sean Linehan:** Either is fine. Just use whatever's most appropriate in context.

**Elvis Goren:** In terms of the overall tone of the articles—are you okay with where we're at? Is there anything you're noticing that we could do better?

**Sean Linehan:** There's one thing I'm very sensitive about. I try very hard to never imply our customers and target audience are stupid. LLMs love to punch down on L&D teams, and we never want to do that. For example, one article said "most L&D programs are measured on useless metrics." But our audience uses those metrics—so saying "you're stupid and useless" is not the right tone. Instead of criticizing, we should say: "You're smart and strategic. You'd be doing more effective things if you had the tools. That's what we're here to help with." The reason you're not succeeding isn't because you're stupid; it's because you lack tools and resources. That's the message.

**Kyle Gaudreau:** We could play with prompts around being empathetic, balanced, and aspirational to capture that flavor.

**Sean Linehan:** Yes, exactly. Aspirational rather than inspirational—inspirational can make LLMs hokey. I also see this in my LinkedIn content with AI. It says things like "Your talent development strategies are awful," which is not how program leads talk. That's learner-level criticism. It's an interesting balance because the training data is mostly learners complaining about these things, not decision makers.

**Elvis Goren:** When we synthesized the source material, that might have picked up that tone. We'll adjust.

**Sean Linehan:** It's different from Julian's approach, who does "punch down"—"You're writing landing pages; you're an idiot; do it my way." That works when people know they're not good at something. But Exec's audience feels under-resourced, not incompetent. That's the key distinction.

**Kyle Gaudreau:** Right, and we need to be careful not to treat all personas the same. L&D and sales audiences need different tones. We're building persona-specific templates and testing different approaches so we don't apply a one-size-fits-all tone.

**Sean Linehan:** Yeah, and different levels of experience too. I'm aligned on that.

**Kyle Gaudreau:** We'll build out those persona templates.

**Elvis Goren:** One last thing—how difficult is it to create a GPT tool and redeploy it across different content pieces?

**Sean Linehan:** Super easy on both sides. First, define the job to be done. Once we have that, it's about 15-20 minutes to configure. I'll need from you: title, subtext, available input fields, and desired output shape. Then I can set it up quickly. What I'd suggest: "Workshop your objection handling"—two inputs: customer objection and your broad-strokes answer. Output: a polished call script. Users can keep generating different versions, and each version is saved.

**Elvis Goren:** We could also have a generator for common objections by business type?

**Sean Linehan:** Exactly. One tool generates a list of objections by business; users pick one and move to the second tool to workshop it. You can put them back-to-back. The model is configurable too. I'll show you—this example uses GPT-3.5 Turbo. I just updated it to GPT-4.0, which is faster and better.

**Elvis Goren:** Got it. I'll send you GPT ideas on Slack with specific requirements.

**Sean Linehan:** Perfect. Now, on the taxonomy front—articles go into series, series into parent series, creating nested hierarchies. This gives us the structure and spider-ability for Google. I need to see what category taxonomy you think makes sense. I've already set up baseline categories for published articles, but we can make as many as we want. They're super easy: title, at least one article, slug, and you're done.

**Kyle Gaudreau:** We should think about it holistically—topics, personas, experience levels. Different audiences need different grouping logic.

**Sean Linehan:** Right. Let's put together a basic taxonomy proposal and go from there. On the homepage, we rank popular series by viewership; the rest are reverse chronological. This integrates with our learning management system too, so articles embed directly in learning programs. It's all very polished because we built it with SEO in mind from the start.

**Kyle Gaudreau:** That's a really elegant product.

**Sean Linehan:** One challenge—I wish they'd expose a WYSIWYG component library so our customers could publish directly to our learning center. Instead, I have to build custom WYSIWYG bridges to their data model. Not a blocker, just tedious.

**Elvis Goren:** We just got CMS access, so we can draft articles directly instead of requesting access per article.

**Sean Linehan:** Perfect. Leave them in draft. I'll review to make sure configuration is correct before we publish. My take on publishing: we're close enough on tone. Once configuration is solid, I'm comfortable with auto-publishing. I'll monitor periodically and iterate post-publication if needed rather than blocking upfront.

**Kyle Gaudreau:** That's smart—we can optimize impact for effort and leverage fast signal.

**Sean Linehan:** On images, they're good enough for blog content. If it's a hot-lead piece for a CIO, I'd invest more. But for 1,200 articles? We monitor Google Analytics, put love into high-traffic pieces, and let low-traffic content ride. Not worth the ROI otherwise.

**Kyle Gaudreau:** Same approach we're taking.

**Sean Linehan:** I'm pumped to get these articles live.

**Elvis Goren:** So am I.

**Kyle Gaudreau:** Let's go.

[After wrapping the main discussion, conversation shifts to casual topics about Sean's office setup in the city, before Elvis and Sean exchange final points.]

**Sean Linehan:** Elvis, send me those GPT ideas on Slack. Adding tools to articles is simple. Choose where to place it in the publishing view, select the GPT tool, publish. Done.

**Elvis Goren:** Got it. Thanks for walking through all of this.

**Sean Linehan:** No problem. See you soon.
