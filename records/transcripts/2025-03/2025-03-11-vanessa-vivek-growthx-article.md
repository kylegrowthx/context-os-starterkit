# Vanessa <> Vivek GrowthX article

<metadata>
date: 2025-03-11
time: 17:56 UTC
duration: 21 minutes
organizer: ismail@growthxlabs.com
participants: Vivek Shankar, Ismail Ajagbe (GrowthX), Vanessa Sauter (PromptFoo)
fathom_recording_id: 51317029
fathom_url: https://fathom.video/calls/250154715
share_url: https://fathom.video/share/L69gbUqxwnFx5zw6wdR7HksyDKhL7zdg
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Vanessa Sauter reviewed GrowthX's AI-generated PromptFoo security articles and provided detailed feedback on audience misalignment. The team discovered that articles were overly focused on code implementation and technical details when security professionals actually need risk awareness, identification methods, and mitigation strategies. Vivek and Ismail committed to refocusing content on the security professional perspective while experimenting with GPT-4.5 for improved writing quality, with Vanessa to continue reviewing remaining articles and providing feedback.

---

## Context

GrowthX is creating security-focused articles for PromptFoo, a platform focused on LLM prompt engineering and testing. Vanessa Sauter is a security professional at PromptFoo who reviews content to ensure it aligns with their audience. The relationship began with GrowthX using AI models (GPT and Claude) to generate initial drafts, then Vanessa providing feedback on content quality and audience fit. The challenge has been consistent: GrowthX's AI-generated articles are "almost there" but miss the mark for a security professional audience, typically overemphasizing code implementation and technical details when audiences need high-level risk awareness and actionable security guidance. This meeting served as a feedback session to align on audience-specific writing direction and explore new models (GPT-4.5) to improve content generation quality.

---

## Relevance

**To GrowthX Delivery:**
- Shift content writing methodology: Lead with risk awareness and security professional perspective, not code implementation and technical details
- Consider model upgrades: GPT-4.5 shows better emotional intelligence and writing quality than GPT-4.0; test its effectiveness for audience-specific content generation
- Implement new content review process: Pass existing PromptFoo articles as context prompts to LLMs to mirror established persona and writing style
- Recognize LLM knowledge cutoff limitations: Recent security research (3-week-old papers) won't be captured by models; plan for manual fact-checking and updates

**To CheckThat:**
- Potential product feedback: LLMs struggle with granular audience-specific generation without extensive context (opportunity for CheckThat's targeting capabilities)
- Industry validation: Security professionals value risk identification and mitigation strategies over code-level implementation details

---

## Overview

- Content angle needs adjustment: Focus on security professionals' perspective, not code implementation
- LLM limitations: Recent research may not be captured, requiring manual updates
- Improvement strategy: Use GPT-4.5 for writing, GPT-4.0 for judging; pass existing PromptFoo articles as context

---

## Key Topics

### Content Rewrite and Feedback

  - Vanessa rewrote parts of the article to better suit the target audience (security professionals)
  - Reframe: Focus on risks, root causes, identification, and mitigation rather than code snippets
  - Time efficiency: Vanessa found it quicker to rewrite than provide detailed feedback
  - Persistent issue: Content is "almost there" but doesn't quite hit the mark for the target audience

### Target Audience Needs

  - Security professionals need: risk awareness, root causes, identification methods, mitigation strategies
  - Less focus on code, more on outputs and configurations
  - Example: Show LLM outputs demonstrating sensitive information disclosure, not the underlying code

### Content Structure Refinement

  - Maintain focus on common attack vectors and security measures
  - Earlier sections: Mention risks without diving into code details
  - Emphasize subject matter over code implementation

### Industry Challenges

  - Fast-moving field: New research (e.g., 3-week-old papers) may not be captured by LLMs
  - Manual effort sometimes necessary due to rapidly evolving industry knowledge

### Content Generation Improvements

  - Currently using GPT and Claude for two passes, including style mirroring
  - Challenge: Zeroing in on audience-specific needs in a granular way
  - Suggestion: Experiment with GPT-4.5 for better emotional intelligence and writing quality
  - Use GPT-4.0 to judge GPT-4.5's output for potential improvements

### Guidelines and Context

  - OWASP guidelines remain the primary reference
  - Recommendation: Pass previous PromptFoo articles as context for LLM to mirror persona and writing style

---

## Action Items

**Ismail Ajagbe (GrowthX)**
- Send agenda for prophecy call to Vivek (not directly to prophecy team)

**Vivek Shankar (GrowthX)**
- Experiment with GPT-4.5 for article generation. Compare results with GPT-4.0 as judge. Report findings to Vanessa

**Vanessa Sauter (PromptFoo)**
- Review remaining GrowthX articles. Provide feedback on necessary changes and audience-specific improvements

---

## Transcript

**Vivek Shankar:** I checked the latest version that Vanessa had in there. She included other sections, and the methods itself I think included that. We had the section called preventing, just scrolling through it.

**Ismail Ajagbe:** Yeah, I was checking all the articles from other blogs and the thoughts were different. That's why what she posted in here is different.

**Vivek Shankar:** We can try to understand why she decided to rewrite it as opposed to having us edit it. Anyway, before we say anything else, just a gentle reminder — the prophecy call got shifted. If you can send the agenda to me, not directly to them, and they can do that. The Looker stuff I think Nika should be able to run it, but I told him that you're also familiar with it, so I'll let you guys decide who wants to run that.

**Vanessa Sauter:** Hi guys, how's it going? How are you?

**Vivek Shankar:** Hi, Vanessa. I don't think you've met Ismail before, but he's my content writer and he's been playing a huge role in generating from Cools content. So we just thought it'd be good to connect and walk us through what you thought of the article itself. We noticed that you rewrote a lot of it. So we just want to get your thoughts on where the content is at and what was missing.

**Vanessa Sauter:** Yeah, let me take a look at this. I think you guys are on the right path, but when I was reading it, I thought about what information someone in my position at another company would need to secure LLMs and what they needed to know. I wanted to reframe it more around these are the risks that if you are a security engineer or security professional, you should be aware of — less about what's in the code or the different techniques, but more about the root cause of the issue and what you should be concerned about. What I did was take what GrowthX provided, what you guys did, which I thought was good, and then I tweaked and reframed it so it was more catered to the format I'm used to as someone on the other side of the house reading it.

**Vivek Shankar:** OK, that's good to know. I was concerned this was like where we were back in December. But it sounds like that's not the case and we weren't kind of there. But I just wanted to check if we want to reduce the burden on you. So is there any way that if this happens again where the angle is not quite correct, would you like to just give us feedback saying "here's what I want to see" and having us edit that? Would that be helpful for you, or would it be less helpful?

**Vanessa Sauter:** Yeah, to be honest, when I was looking at it, I thought to myself that the amount of time it would take for you guys to go through the feedback and redo it was going to be more time than it would take me to just quickly write it up, pull the wording and format, and craft the article accordingly. So in my head, if we want to check this out in a way that I know is going to totally hit the mark, let me take the content and tweak it based off what I know is going to hit. I'm always happy to give you guys that feedback, but I thought the back and forth would take more time than the hour and a half, two hours I took to massage it into a place I know the readers would resonate with on the other side of the house.

**Vivek Shankar:** Yeah. And just wanted to check — the previous articles you reviewed over the past few weeks. Were there similar issues like this where the information was there but the angle was off? Is that a persistent issue?

**Vanessa Sauter:** Yeah, so I'm seeing that where it's almost there, but it doesn't quite hit the mark in terms of who the target audience is. It goes a little bit into the engineering or application engineering side — like the code snippets, for example, or here's how you implement differential privacy. Whereas the security side of the house — they're not going to really see that or have visibility. What they need to know is: this is the root cause, this is how to identify it, this is the way to mitigate it. It's less about the code itself and more about what you need to know about what could potentially be happening with it.

**Vivek Shankar:** I think one of the reasons Ismail started including code snippets was because we see feedback in some earlier articles where people mentioned it would be good to have code snippets here. Is there some guidance you could give us in terms of when we should show examples of code in specific scenarios?

**Vanessa Sauter:** So I think for what we're trying to target, it's less about that. In some cases yes, but typically what we would want to see would be the output of the LLM, right? So looking at the output of what would be considered sensitive information disclosure — for example, this is the output showing one identical image and another that was created. That's an example of the output. Or if we're talking about personal data that LLM has memorized, this is an example of what you would see from the output. Then you can go into how this is the configuration that would help you identify that. But in terms of the code that causes it, I don't think that's going to be super helpful for some folks because right now they just want to figure out: is it even there? Does it even exist? The first stage is: this is the risk you need to be concerned about, this is how you identify it. Then once it gets to that point, they go back with their teams and figure out how it's producing it. In certain cases, it's not even about the code — it's about the system prompts, the guard rails, so there are other things that would cause that output.

**Vivek Shankar:** That's really helpful. So in these articles then, the general structure would be: these are the common attack vectors, here's how you secure against it, et cetera. So if I'm understanding correctly, what you're saying is in the first sections we don't really need to mention the risks and how it could happen without diving into the code. We need to focus more on the subject as opposed to the code itself in those earlier sections.

**Vanessa Sauter:** Exactly. Yeah, I think you guys are doing well and I'm really seeing improvement. I think just tweaking and focusing more on the security side of the house where they might not have visibility into the code — general education about what the risk is, how to identify it, and what next steps to take. I don't think we need to get too granular on the engineering mitigation side. Just stick to more of the informative education and broader awareness, I think would be really useful.

**Vivek Shankar:** Yeah, that makes sense.

**Vanessa Sauter:** And to be fair, right, this stuff is on new research. Sometimes you guys will create content and it's not that you're doing anything wrong. It's just that the research is still coming out, right? Like, there's a new research paper that's come out — it's like three weeks old. You guys aren't going to have that. The LLM's not going to have that context. So it's not your fault at all. It's just that the industry moves very fast. So this might be a use case where it might take a little bit more effort on my side, not because GrowthX is not doing a good job, but because the industry's moving so fast that there's just no way the LLM would even know that.

**Vivek Shankar:** Yeah, that was something we knew about as well. So it's a bit of a concern in terms of whether we include it or not. But yeah, thank you for that. So if you have any questions or clarifications you wanted to bring up?

**Ismail Ajagbe:** Thank you for taking the time, Vanessa. So the question I have is about the sensitive information disclosure article. We looked at it based on the OWASP guideline, and from research and other blogs, it expanded on the app for example. So do you think there is any approach we should take to have a common grant on article outlines outside the OWASP guideline?

**Vanessa Sauter:** I think the only other thing I can think of for you guys is to pass PromptFoo articles as context. When you're generating the content, passing previously written PromptFoo articles as context and tell the LLM to mirror the persona and writing style that's been published before. Then use that as part of the criteria for judging the quality of the output. OWASP is great. There's nothing else I can think of that's going to be our North Star besides what PromptFoo is already writing. So that would be my recommendation — take what we're looking at and pass that. See if there's any difference in what the LLM is producing or if it's able to tweak the writing for the audience accordingly.

**Vivek Shankar:** We have been using them as a judge quite a bit. We're actually using GPT and Claude, running them in two passes. One of the issues we had with passing PromptFoo's existing content through it and mirroring it for style — it's able to pick up the style quite well. But it's not able to really zero in on the audience-specific needs in a granular way, and that I think is our biggest challenge. So yeah, I'm not asking for a solution here, but just giving more context that's where our element is falling short.

**Vanessa Sauter:** Yeah, my suggestion too, if you guys have the budget for it, is try experimenting with GPT-4.5. So GPT-4.5 is a lot better in terms of emotional intelligence and writing and communication. It does a better job than 4.0. It's more expensive, much more expensive. But it might be worth trying that out to see if you guys get better results that way using the same tactics. What you could do is try using a model that's better suited for writing, then using 4.0 or something else as a judge for what 4.5 is producing. That might help on that side of the house.

**Vivek Shankar:** That was all I had. Is there anything else, Ismail?

**Ismail Ajagbe:** Thanks a lot, Vanessa.

**Vivek Shankar:** Yeah, this is one last thing — given the feedback, do you want us to go back and fix the other articles or do you still want to go ahead and review them?

**Vanessa Sauter:** Let me go ahead and review them. I'll let you guys know if there's anything I think you can change. That's on my backlog. I did the sensitive information disclosure article and I was off on Friday. I did the sensitive information disclosure and I'll go through and see what's going on with the other ones.

**Vivek Shankar:** Yeah, this was super helpful. So yeah, thank you so much. And yeah, thank you for the patience again.

**Vanessa Sauter:** Yeah, absolutely. Really appreciate your communication, your transparency, and working together. So thanks for helping on this call.

**Vivek Shankar:** Thanks, Vanessa. Nice to see you guys. Bye.
