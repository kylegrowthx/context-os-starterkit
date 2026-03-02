# Atlas Walkthrough with Sydney

<metadata>
date: 2026-01-07
time: 16:48 UTC
duration: 55 minutes
organizer: william@growthx.ai
participants: William Leborgne, Sydney Arin Go, Kathy Lam, Nathalie Schrans
fathom_recording_id: 112462243
fathom_url: https://fathom.video/calls/525163637
share_url: https://fathom.video/share/_4Vd8fzriikAin3d1ysUFao5skCPLJHR
source: fathom
enriched_on: 2026-02-28 13:43:27 UTC
</metadata>

---

## Summary

William gave Sydney an in-depth walkthrough of Atlas, GrowthX's pipeline UI for content generation. They covered the two-tier architecture (Studio for YAML workflow authoring, Atlas for ME execution), the standard Hex pipeline workflow (research → draft → style validation → linking → proofread → metadata), and critical customization patterns. Key discussion points included the limitations of automated content refreshes, the special-project nature of PSEO work, and artifact management strategies to prevent infinite validation loops.

---

## Context

William conducted this meeting to onboard Sydney to the Atlas system and pipeline architecture that powers GrowthX's content generation for clients. The session was exploratory and pedagogical in nature—Sydney is getting up to speed on how pipelines work, how they're customized, and where manual intervention is required. The discussion revealed both the maturity of the pipeline system (it works well for standard content generation) and key gaps (automated refreshes are unreliable, PSEO requires special engineering).

This meeting is critical context for anyone building or debugging pipelines, optimizing client onboarding processes, or planning new features for the Atlas platform.

---

## Relevance

- **Engineering / Product:** Understanding the two-tier architecture (Studio/YAML backend vs. Atlas UI) and how pipeline customization works at scale
- **Delivery / Pipeline:** Real-world constraints on automation (refreshes, PSEO) and when manual work is necessary
- **Content Operations:** How artifacts (style guides, customer stories, product info) flow through pipelines and when conflicts cause failures
- **Client Success:** Customization patterns (research tools, competitor exclusions, validation steps) that address client-specific needs

---

## Overview

- **Core Pipeline:** The standard pipeline drafts a research-based article, then applies client-specific style and product details in a separate validation step. This two-step process prevents the AI from creating well-written but disconnected sections.
- **Pipeline Customization:** Pipelines are built by copying a proven template (e.g., Hex) and customizing its YAML code. Claude is a key tool for debugging and optimizing this code.
- **Content Refreshes:** The automated refresh pipeline is unreliable, often requiring manual work. This is a significant gap, as refreshes can yield faster, higher-impact SEO wins than net-new content.
- **PSEO as a Special Project:** Programmatic SEO (PSEO) is not a standard Sprint offering due to its complexity and calibration time. However, the engineering team can build robust, end-to-end PSEO systems as special projects.

---

## Key Topics

### Pipeline Architecture: Studio vs. Atlas

- The system has two main components:
    - **Studio:** The engineering backend where core workflows (functions) are programmed in YAML.
    - **Atlas:** The user-facing UI where MEs assemble and run pipelines by pulling functions from Studio.
- **Analogy:** Studio is the library of building blocks, and Atlas is the workspace where MEs combine them into a pipeline.
- **Standard Build Process:** MEs copy a proven pipeline template (e.g., Hex) into a new client workspace and then customize its YAML code.

### Standard Pipeline Workflow (Hex Example)

- The pipeline is a sequence of steps designed to produce a high-quality, client-specific article.
- **1. Input:** ME defines the assignment (topic, keywords, etc.).
- **2. Research Topic:** An AI agent (e.g., Tavily, Exa) gathers information, avoiding specified competitors.
- **3. Draft Article:** An LLM (e.g., Opus) writes a research-based draft.
    - **Rationale:** This step focuses on structure and flow. Applying the full style guide here would result in disconnected sections, as the AI validates each chunk in isolation.
    - **Artifacts:** The drafter receives artifacts like the audience persona and product info to ensure foundational accuracy.
- **4. Validate Writing Style Guide:** The article is rewritten to match the client's voice and incorporate product messaging.
- **5. Add Internal Links:** Scrapes the client's sitemap to find relevant internal links.
- **6. Add Source Links:** Identifies claims and adds external sources from the research step.
    - **Known Issue:** This step is imperfect; it can add irrelevant links or miss existing sources.
- **7. Final Proofread Checklist:** A final validation step for grammar and specific word choices.
- **8. Meta Tags & Header Image:** Generates metadata and prepares for image integration.

### Pipeline Customization & Debugging

- Pipeline customization is done by editing the YAML code in Atlas.
- **Key Customization Points:**
    - **Research:** Specify tools (Exa for technical topics, Tavily for speed) and add competitor exclusions.
    - **Drafter:** Select the LLM (e.g., Opus 4.5) and provide instructions to pull specific artifacts (e.g., customer stories).
- **Debugging with Claude:** Paste the pipeline's YAML code into Claude to ask why a specific result is occurring or to generate a new step.
- **Artifact Management:**
    - Long or conflicting artifacts (e.g., a style guide that contradicts a "good example") can cause the pipeline to fail or run for 30–45 minutes as it hits its `max_iterations` limit.
    - Strict client rules (e.g., NetRisk's "AI-isms" prompt) require a dedicated validation step to ensure adherence.

### Article Refreshes & PSEO

- **Article Refreshes:**
    - The automated refresh pipeline is unreliable, often requiring manual work.
    - **Rationale:** It struggles with poor website structure and may add unverified information.
    - **Significance:** This is a major gap, as refreshes can deliver faster, higher-impact SEO wins for clients with large content library.
- **Programmatic SEO (PSEO):**
    - Not a standard offering for Strategy Sprints due to its complexity and calibration time.
    - **Capability:** The engineering team can build robust, end-to-end PSEO systems as special projects (e.g., SentinelOne's CVE pages, Webflow's integration guides).

---

## Action Items

- **Sydney Arin Go:** Find and share Notion link to Panzer's Claude pipeline updater/optimizer with William, Kathy, and Nathalie (00:37:36)
- **Kathy Lam:** Upload NetRisk style guide + AI-isms doc to internal docs for Sydney and Nathalie (00:46:43)

---

## Transcript

**William Leborgne** (00:00:01): This meeting is being recorded.

**Sydney Arin Go** (00:00:03): Hey, how's it going?

**William Leborgne** (00:00:05): Good, how are you?

**Sydney Arin Go** (00:00:06): I'm good.

**Sydney Arin Go** (00:00:08): I feel like we've been on a lot of calls together, but we've actually not talked one-on-one.

**William Leborgne** (00:00:13): That is true, that is true.

**William Leborgne** (00:00:15): Why don't we actually just start with that, little introduction.

**William Leborgne** (00:00:18): I'd love to know a little bit more about you, like where you're based, what your background is, what your favorite color is.

**Sydney Arin Go** (00:00:26): My favorite color is blue, most important.

**Sydney Arin Go** (00:00:28): Okay, good, good, good, good to know.

**Sydney Arin Go** (00:00:34): Background, so I'm based in Manila half the year, Vancouver half the year, because my husband's from Vancouver and my family's here in Manila.

**Sydney Arin Go** (00:00:41): And when we got married, we decided we'll do the back and forth.

**Sydney Arin Go** (00:00:44): Grew up in the States, which is why I sound the way that I do, in California.

**Sydney Arin Go** (00:00:50): And then, so my background is largely, I grew up just outside of LA, in Arcadia.

**William Leborgne** (00:00:56): Oh, , okay, I know Arcadia.

**Sydney Arin Go** (00:00:58): My best friend is from Arcadia.

**Sydney Arin Go** (00:00:59): Oh nice.

**Sydney Arin Go** (00:01:02): I think I remember one of the first few calls that you're in the LA area too, right?

**William Leborgne** (00:01:09): I was.

**William Leborgne** (00:01:10): My wife and I are now living in Mexico temporarily.

**William Leborgne** (00:01:16): We just wanted to mix it up.

**William Leborgne** (00:01:19): I think when, not to get too political, but when Trump came back into power, were like, you know, I don't know if I want to do another four years of this nonsense.

**William Leborgne** (00:01:28): Yeah.

**William Leborgne** (00:01:29): So we, we escaped, but it's, it's temporary.

**William Leborgne** (00:01:32): don't know when, how long we're going to stay, but I was living in Long Beach.

**Sydney Arin Go** (00:01:35): Oh, very cool.

**Sydney Arin Go** (00:01:36): Yes.

**Sydney Arin Go** (00:01:37): I think I remember that.

**Sydney Arin Go** (00:01:38): Well, some of cousins are in Long Beach.

**William Leborgne** (00:01:40): Oh, cool.

**Sydney Arin Go** (00:01:42): What part of Mexico are you in?

**William Leborgne** (00:01:45): I'm in a town called San Miguel de Allende.

**William Leborgne** (00:01:48): It's honestly the prettiest place I've been to in Mexico so far.

**William Leborgne** (00:01:52): Um, we love it.

**William Leborgne** (00:01:53): It's very like medieval Spanish.

**William Leborgne** (00:01:56): Um, it's been voted like best town in the world.

**William Leborgne** (00:01:59): Yeah.

**William Leborgne** (00:01:59): Thank you.

**William Leborgne** (00:02:00): Multiple years.

**William Leborgne** (00:02:02): So, yeah.

**William Leborgne** (00:02:04): Sorry, I cut you off earlier.

**William Leborgne** (00:02:07): You were saying that you grew up in LA, but then you were in Vancouver.

**Sydney Arin Go** (00:02:11): That's where you met your husband?

**Sydney Arin Go** (00:02:14): No.

**Sydney Arin Go** (00:02:15): So I did a study abroad in China, language exchange, and we met there.

**Sydney Arin Go** (00:02:20): He's Canadian.

**Sydney Arin Go** (00:02:20): Or he's, yeah, European-Canadian, kind of.

**Sydney Arin Go** (00:02:25): So he's not Chinese.

**Sydney Arin Go** (00:02:26): And it just struck a look.

**William Leborgne** (00:02:29): European in what way?

**Sydney Arin Go** (00:02:32): I think his background is English-Scottish or whatever, and he's like half Japanese or something, or a quarter Japanese.

**Sydney Arin Go** (00:02:39): Okay.

**Sydney Arin Go** (00:02:40): He's something.

**Sydney Arin Go** (00:02:41): He's a mix.

**Sydney Arin Go** (00:02:42): And he wanted to learn Mandarin.

**Sydney Arin Go** (00:02:44): I wanted to learn Mandarin.

**William Leborgne** (00:02:45): We were classmates, and that's where we met.

**William Leborgne** (00:02:47): Oh, that's so cool.

**William Leborgne** (00:02:49): Love story in the foreign lands.

**Sydney Arin Go** (00:02:53): Really?

**Sydney Arin Go** (00:02:53): We were the only two English speakers in the class, so it was the actual connection there.

**Sydney Arin Go** (00:02:59): cool.

**Sydney Arin Go** (00:02:59): Oh, Oh,

**Sydney Arin Go** (00:02:59): Um, but that was a long time ago now.

**Sydney Arin Go** (00:03:02): Um, yeah.

**Sydney Arin Go** (00:03:04): Um, but yeah, so my background's mostly in SEO.

**Sydney Arin Go** (00:03:09): So before here, I was working at SEMrush.

**Sydney Arin Go** (00:03:11): Um, that's where Marcel kind of found me.

**Sydney Arin Go** (00:03:13): I was on the content team and kind of, if you were on the production weekly, um, call just now, Panzer was saying something along the lines of, if you're a startup because you want it to move fast, um, if you're, if, if things aren't challenging, any more than you're not growing.

**Sydney Arin Go** (00:03:31): that's kind of where I was at SEMrush where, because it was a big established company, very secure, safe.

**Sydney Arin Go** (00:03:36): Um, but it was so repetitive, same thing over and over and then over again, um, day in day out, you had the same things.

**Sydney Arin Go** (00:03:45): Um, and we had some innovation when I started because we were building a new team, but enterprise.

**Sydney Arin Go** (00:03:53): So legal kind of, it's fun to deal with and then project marketing.

**Sydney Arin Go** (00:03:58): And at some point I.

**Sydney Arin Go** (00:03:59): Got into a fight with the product marketing team because I was like, I can't have you screenwriting each and every single article.

**Sydney Arin Go** (00:04:05): I will do all the courses, learn all the tools, and I will be the product marketing expert on the team.

**Sydney Arin Go** (00:04:12): And that's what I did.

**Sydney Arin Go** (00:04:13): Wow.

**Sydney Arin Go** (00:04:14): That's cool.

**Sydney Arin Go** (00:04:15): I'm so sick of it.

**Sydney Arin Go** (00:04:17): Really, I'm just stubborn.

**Sydney Arin Go** (00:04:20): But yeah, it was just, if you've been in Summers, there's so many tools and they were like, you have to mention this tool and that tool and that tool and this tool.

**Sydney Arin Go** (00:04:27): And we're like, this will kill the article.

**Sydney Arin Go** (00:04:30): Also, this is not a great tool to mention.

**Sydney Arin Go** (00:04:31): It doesn't really work.

**Sydney Arin Go** (00:04:33): Yeah.

**Sydney Arin Go** (00:04:33): So I was a little bit more in touch with what we had to do and our goals.

**Sydney Arin Go** (00:04:40): And at that point, the product marketing team just trusted me because we went back and feed them so much.

**Sydney Arin Go** (00:04:48): I'm glad they were patient with me, to be completely honest, because I was just so tired of it.

**Sydney Arin Go** (00:04:53): But yeah, and then that's how I got here.

**Sydney Arin Go** (00:04:55): Marcel found me and now I'm here.

**William Leborgne** (00:04:58): Wow.

**William Leborgne** (00:04:58): Okay.

**Sydney Arin Go** (00:04:59): Okay.

**William Leborgne** (00:05:00): And are you, like, how long have been now with GrowthX?

**William Leborgne** (00:05:03): I started in March of last year, so 10 Okay, you're a veteran, basically.

**Sydney Arin Go** (00:05:09): Yeah, it feels like I started yesterday, though.

**Sydney Arin Go** (00:05:12): Like, I can't believe it's been 10 months because it's been so fast.

**Sydney Arin Go** (00:05:17): And time has been, I don't know how you feel about it, but time has been so relative.

**William Leborgne** (00:05:21): It feels like, I don't know what day of the week it is at any given time.

**William Leborgne** (00:05:26): Mm-hmm, mm-hmm, yeah, yeah, no, I feel that you, I honestly, like, I feel like, I've worked in a lot of different startups, and I've definitely had similar feelings of, like, whoa, this is a lot.

**William Leborgne** (00:05:40): But this one feels like it's a lot to start with, but that's, like, just scratching the surface.

**William Leborgne** (00:05:47): You don't even know how much more it's going to be.

**William Leborgne** (00:05:49): Like, just looking at Ada and all these other people, I'm like, oh, my God, like, I got to prepare myself mentally.

**William Leborgne** (00:05:55): So I've been spending a lot of time trying to get super organized.

**William Leborgne** (00:06:00): And one of my tasks today is to create my own Trello board so I can just easily and quickly see what the  I'm supposed to be doing and when.

**William Leborgne** (00:06:11): By the way, if you have any other tips and tricks for keeping yourself sane at GrowthX, then from an internal product management, just making sure you're crossing all your T's, I welcome it.

**Sydney Arin Go** (00:06:27): Yeah, I did the same thing.

**Sydney Arin Go** (00:06:29): did Asana just because Asana has a time tracking thing and I wanted to know how much time I was spending on each task because like before the whole restructure, the reason why, one of the reasons that this kind of relationship happened with Ada and the MEs is because when I first started with Sprint says, like I don't, I have five customers, Ada right now, seven.

**Sydney Arin Go** (00:06:52): Can you handle all the comms because I can't, I can't do this.

**Sydney Arin Go** (00:06:56): I can't be doing the back end and the front end and she's like, I got this.

**Sydney Arin Go** (00:07:00): So she did all the communicating with the customers, and I was like, here is what we did, why we did it, make it pretty.

**Sydney Arin Go** (00:07:07): And she did it, and it was amazing.

**Sydney Arin Go** (00:07:09): Honestly, it is amazing.

**Sydney Arin Go** (00:07:12): Like, I can't, no words to describe how amazing she is and the work that she does.

**Sydney Arin Go** (00:07:17): She keeps it all straight in her head.

**Sydney Arin Go** (00:07:19): I confuse clients all the time.

**Sydney Arin Go** (00:07:21): She's just like.

**William Leborgne** (00:07:22): She's a freaking superstar.

**Sydney Arin Go** (00:07:23): It's unbelievable.

**William Leborgne** (00:07:24): Oh, yeah.

**Sydney Arin Go** (00:07:25): She's a machine.

**William Leborgne** (00:07:26): Yeah.

**Sydney Arin Go** (00:07:29): Yeah, no, but it is, it is a lot of fun working at GrowthX.

**Sydney Arin Go** (00:07:34): It's a lot of change.

**Sydney Arin Go** (00:07:36): Like, when I started, we were still on AirOps.

**Sydney Arin Go** (00:07:38): That was fun.

**Sydney Arin Go** (00:07:40): That was also fun.

**Sydney Arin Go** (00:07:41): Just trying to wrangle AirOps to do what you want.

**William Leborgne** (00:07:45): Yeah, so I was a big power user of AirOps before I came here.

**William Leborgne** (00:07:49): I think it's maybe one of the reasons that Marcel was interested in me.

**William Leborgne** (00:07:53): And I know exactly what you're talking about.

**William Leborgne** (00:07:55): AirOps really is a beast.

**William Leborgne** (00:07:56): It's, it's, it's so not user friendly.

**William Leborgne** (00:07:59): It's almost.

**William Leborgne** (00:08:00): Almost on purpose, not user-friendly.

**William Leborgne** (00:08:01): For people like us, when I talk to an engineer's type, they're like, oh yeah, I get it.

**William Leborgne** (00:08:07): But for their actual target audience, it's not user-friendly.

**Sydney Arin Go** (00:08:11): Yeah.

**Sydney Arin Go** (00:08:12): Because of growthx, it's the only reason why I became, or I, stubbornness again, tried to become as technical as I could be.

**Sydney Arin Go** (00:08:22): Because I do have an okay base in some languages.

**Sydney Arin Go** (00:08:27): So I did C a little bit, and then HTML, CSS, and all that, trying to get back into JavaScript.

**Sydney Arin Go** (00:08:34): But it's just been so long.

**Sydney Arin Go** (00:08:37): But it is, Aerox was, I would say it was a little bit more intuitive than Atlus.

**Sydney Arin Go** (00:08:47): But Atlus is just, it just works so much better.

**William Leborgne** (00:08:51): Like, it's just, at least what I've seen.

**Sydney Arin Go** (00:08:55): I'm not sure how Aerox is now, to be fair, because I think the last time you...

**Sydney Arin Go** (00:09:00): Air Ops was maybe me.

**Sydney Arin Go** (00:09:02): But I remember with Air Ops, it was just trying to get having your multi-step grids and then just having so many research steps and validation steps and then all the context in there.

**Sydney Arin Go** (00:09:15): And you're not sure if it's actually pulling the whole thing.

**Sydney Arin Go** (00:09:17): And there was a little bit of a black box situation where you don't know how it gets to where it gets because you don't have control over which researcher it uses or which model it wants to use at the moment.

**Sydney Arin Go** (00:09:29): Right.

**Sydney Arin Go** (00:09:29): It was fun.

**William Leborgne** (00:09:32): This is so fascinating to hear.

**William Leborgne** (00:09:34): Hi, Kathy.

**Sydney Arin Go** (00:09:35): Hey, Kathy.

**Kathy Lam** (00:09:36): Hey, sorry.

**Kathy Lam** (00:09:37): I wish I saw the note earlier.

**William Leborgne** (00:09:39): No worries.

**William Leborgne** (00:09:40): We've just been kind of introducing each other because we realized we've never actually talked one-on-one.

**William Leborgne** (00:09:45): And just so Sydney was giving me a little bit of background.

**William Leborgne** (00:09:49): She's also a SoCal person, Arcadia.

**William Leborgne** (00:09:53): So we had that little thing in common and she spends half her time in Canada and half her time in the Philippines.

**William Leborgne** (00:09:58): thing of uh

**William Leborgne** (00:10:00): She has this little arrangement with her husband, which I think is super cool, by the way.

**William Leborgne** (00:10:03): I love that you guys are like, no, we want both.

**William Leborgne** (00:10:06): So let's just do both.

**Sydney Arin Go** (00:10:08): Yeah, it's cool.

**Sydney Arin Go** (00:10:09): it's so great in Vancouver right now.

**Sydney Arin Go** (00:10:14): So we flew off and we're in sunny Manila.

**William Leborgne** (00:10:18): Nice.

**William Leborgne** (00:10:19): Yeah, that's a good way to do it.

**William Leborgne** (00:10:22): I'll give a quick intro of myself as well.

**William Leborgne** (00:10:26): Yeah, yeah, for sure.

**William Leborgne** (00:10:27): So I've been working specifically in marketing for a while now, for like 17 or 18 years or something.

**William Leborgne** (00:10:37): But content marketing and SEO, more specifically, a little over a decade.

**William Leborgne** (00:10:43): And I have worked for large companies, have worked for lots of startups, and I've also started my own agency at one point, like just a little boutique agency and worked with some clients.

**William Leborgne** (00:10:56): And I've always been really interested in...

**William Leborgne** (00:11:00): And sort of technology, generally, I think it's something I inherited from my dad.

**William Leborgne** (00:11:06): And when ChatGPT came on the scene, you know, late 2023, it was like an absolute light bulb for me.

**William Leborgne** (00:11:14): Of everything I've ever experienced in my life, I've never been as passionate as I was about this technology.

**William Leborgne** (00:11:20): I think I got just so excited about the possibilities.

**William Leborgne** (00:11:23): And I'm somebody who's very much like, I really like to move fast.

**William Leborgne** (00:11:30): And I'm more of a big picture person and more strategic than I am very like in the minutiae perfectionist.

**William Leborgne** (00:11:37): It's one of the reasons why my wife and I get along well, because she is the perfectionist.

**William Leborgne** (00:11:41): And I'm the other side of things.

**William Leborgne** (00:11:43): She will over-research.

**William Leborgne** (00:11:45): I will over-decide quickly, if that makes sense.

**William Leborgne** (00:11:49): Although I would always argue that it's good to decide quickly.

**William Leborgne** (00:11:54): But all to say, when that technology came into play, it was an...

**William Leborgne** (00:12:00): A huge unlock for me because I like, oh, I get to just be fully strategic and have this tool that makes me a perfectionist, allows me to do so much more, and then start to grow beyond that.

**William Leborgne** (00:12:10): Anyway, fast track, I've worked in all these different companies, and every time I would, I would typically be the primary content SEO person, and I would hire agencies or I'd hire freelancers and do the typical thing, right?

**William Leborgne** (00:12:24): Most of SCM Rush's clients are probably people like myself, and then when ChatGPG came into play, I immediately implemented that with my freelancers.

**William Leborgne** (00:12:37): I reduced my freelancer team, and then once this AirOps came about, I was like, wow, this is like the biggest game changer.

**William Leborgne** (00:12:43): So that was back in December of last year, and then like February is when I got it all locked in, and we started paying for AirOps and transformed how we were creating content, and I got really deep into it.

**William Leborgne** (00:12:56): That was actually in AirOps' very first cohort, their like universe.

**William Leborgne** (00:13:00): Where they're like teaching people how to use it, which was actually kind of bad because that first cohort sucked.

**William Leborgne** (00:13:07): Their next ones were much better.

**William Leborgne** (00:13:10): But I still, I learned a lot about air ops and all that stuff.

**William Leborgne** (00:13:16): Anyway, that's kind of like the broad strokes of like the career side of things.

**William Leborgne** (00:13:20): My mom is American.

**William Leborgne** (00:13:22): My dad is French.

**William Leborgne** (00:13:22): So I have that mix as well.

**William Leborgne** (00:13:25): But yeah, I lived in the LA area for like 11 years, 12 years, a long time.

**William Leborgne** (00:13:32): And yeah, that's, I think that's pretty much it.

**William Leborgne** (00:13:36): And my favorite color is green.

**Sydney Arin Go** (00:13:38): Nice.

**Sydney Arin Go** (00:13:39): I was just going to ask.

**William Leborgne** (00:13:42): Gotcha.

**William Leborgne** (00:13:46): Yeah, I don't know, Kathy, if you want to share a little bit, you know, whatever you feel comfortable.

**Kathy Lam** (00:13:51): Yeah, yeah, definitely.

**Kathy Lam** (00:13:53): I know Sydney and I, we've had this chat, but Natalie, seeing that you're on here, I don't think we had a chance to do that.

**Kathy Lam** (00:13:59): So, yeah.

**Nathalie Schrans** (00:14:00): No, not yet.

**Nathalie Schrans** (00:14:01): And sorry, everyone.

**Nathalie Schrans** (00:14:01): I just saw the message about meeting earlier.

**Nathalie Schrans** (00:14:03): I was like doing some morning stuff and I was like, I know I'll be on time for a meeting for once.

**William Leborgne** (00:14:09): then I was the same thing.

**Kathy Lam** (00:14:12): I was like, just, you know, getting my breakfast and all that.

**Kathy Lam** (00:14:16): So, yeah.

**Kathy Lam** (00:14:18): Funnily enough, I grew up in Vancouver and then moved to the States and then actually planning a move to Hong Kong later this year.

**Kathy Lam** (00:14:27): So, I don't think I'll be doing the split where I'm going back and forth, but never know.

**Kathy Lam** (00:14:34): Let me see.

**Kathy Lam** (00:14:35): So, my background prior to GrowthX was actually at a couple of like startups.

**Kathy Lam** (00:14:42): Very tiny people, like 20 people.

**Kathy Lam** (00:14:45): Last one was at a YC startup.

**Kathy Lam** (00:14:47): So, uh, I think along with my responsibilities was like, not only figuring out like marketing and messaging, but also doing content.

**Kathy Lam** (00:14:56): And I also, I think, um, BA.

**Kathy Lam** (00:14:59): Thank Thank

**Kathy Lam** (00:15:00): I looked into AirOps, but then I saw Marcel do a couple of his workshops, and I was blown away.

**Kathy Lam** (00:15:05): I was like, ah, this is the future.

**Kathy Lam** (00:15:07): So that's how I got introduced to GrowthX.

**Kathy Lam** (00:15:13): My background back in the day is a lot of DevOps and security tools, so feel free to lean on me for those things.

**Kathy Lam** (00:15:26): And then, what else?

**Kathy Lam** (00:15:30): Yeah, my favorite color is blue.

**Sydney Arin Go** (00:15:33): So, yeah.

**William Leborgne** (00:15:35): just like Sydney.

**Sydney Arin Go** (00:15:38): Excellent.

**Kathy Lam** (00:15:38): Natalie, would you like to go next?

**Kathy Lam** (00:15:41): Although you know Sydney, but have you introduced yourself to William already?

**Kathy Lam** (00:15:45): You probably have.

**William Leborgne** (00:15:47): Oh, you're unmuted.

**William Leborgne** (00:15:47): unmuted.

**Nathalie Schrans** (00:15:50): Sorry, there was just background noise, and I muted myself.

**Nathalie Schrans** (00:15:53): Yeah, William and I have talked.

**Nathalie Schrans** (00:15:54): We both discovered that we speak French, although I think he definitely speaks French better than me, considering he grew up.

**Nathalie Schrans** (00:15:59): Yeah,

**Nathalie Schrans** (00:16:00): In France.

**Nathalie Schrans** (00:16:01): And I did not.

**Nathalie Schrans** (00:16:02): So yeah, just an overview.

**Nathalie Schrans** (00:16:08): I mean, I guess, I'm sorry, I don't know.

**Nathalie Schrans** (00:16:10): Did we start like career wise or whatever you like example to follow?

**Nathalie Schrans** (00:16:15): Okay.

**Nathalie Schrans** (00:16:16): Well, I'm based in Los Angeles.

**Nathalie Schrans** (00:16:18): I was born and raised here and I've lived here most of my life, except for when I went to university in Northern California.

**Nathalie Schrans** (00:16:24): Career wise, I kind of like accidentally fell into marketing, starting from kind of like a writing background, which is what I was wanting to do and interested in college.

**Nathalie Schrans** (00:16:34): And then I started working for like a marketing agency, doing mostly branding and identity stuff for small businesses.

**Nathalie Schrans** (00:16:41): And then from there, kind of got into content marketing in B2B.

**Nathalie Schrans** (00:16:46): And then I've kind of been in this space ever since.

**Nathalie Schrans** (00:16:49): Although, of course, you know, that, as we all know, marketing has really changed in the past few years.

**Nathalie Schrans** (00:16:54): So now it's involved or it's like a lot less writing and a lot more of like other things and more.

**Nathalie Schrans** (00:17:00): More versatile, like, skills and learning new tools and more technical skills.

**Nathalie Schrans** (00:17:06): Yeah, so I would say my focus has definitely been on the past few years of, like, figuring out how to use AI in our work and find those efficiencies there.

**Nathalie Schrans** (00:17:16): And naturally kind of ended up at a place like GrowthX where that's the core of what we do.

**Nathalie Schrans** (00:17:23): Yeah, my favorite colors are pink, blue, and purple.

**Nathalie Schrans** (00:17:28): Cool.

**William Leborgne** (00:17:28): It's hard to choose one.

**Nathalie Schrans** (00:17:31): Depends on the day.

**William Leborgne** (00:17:34): I love it.

**Nathalie Schrans** (00:17:36): I don't personally have any pets, but my roommate has a cat, so I'm like his auntie.

**Nathalie Schrans** (00:17:40): So sometimes you may see a cat in the background.

**Nathalie Schrans** (00:17:44): I don't know what else to share.

**William Leborgne** (00:17:46): My first meeting with Kathy, her cat was, like, right behind her and was just sitting perfectly just staring at me.

**William Leborgne** (00:17:53): I was like, wow.

**Nathalie Schrans** (00:17:55): That's so cute.

**Nathalie Schrans** (00:17:56): Oh, my God.

**Kathy Lam** (00:17:57): But unfortunately, unfortunately, she just said...

**Kathy Lam** (00:18:00): So she's napping somewhere.

**Nathalie Schrans** (00:18:02): The dream.

**Nathalie Schrans** (00:18:04): Yeah, a few weeks ago, or like, no, not more than that, like in September.

**Nathalie Schrans** (00:18:08): Where?

**William Leborgne** (00:18:10): It disappeared.

**Nathalie Schrans** (00:18:11): No, oh my god.

**Nathalie Schrans** (00:18:14): Oh my god, it's the background, doesn't like that.

**Nathalie Schrans** (00:18:17): It's I was cat-sitting in September for my friend, and he's like a really fluffy white Persian, like one of the flat-faced cats.

**Nathalie Schrans** (00:18:26): And at times, he would sit on the top of the chair right behind me, so his head would be, like, right here next to mine.

**Nathalie Schrans** (00:18:32): It was just a good surprise for people in calls with me.

**Nathalie Schrans** (00:18:37): Yeah.

**William Leborgne** (00:18:43): Awesome.

**William Leborgne** (00:18:44): Thank you.

**William Leborgne** (00:18:45): appreciate everyone sharing.

**William Leborgne** (00:18:47): Honestly, I feel like this is one of the things that has been missing a little bit for me at GrowthX, as getting to have, like, some real connection and, like, conversation with people to get to

**William Leborgne** (00:19:00): Know them a little better.

**William Leborgne** (00:19:00): So I appreciate you coming along the road with us, Sydney and Natalie.

**Sydney Arin Go** (00:19:05): Natalie and I have a recurring one-on-one-on once every other week.

**Sydney Arin Go** (00:19:11): It's supposed to be on Wednesdays, but we move it every now and then.

**Sydney Arin Go** (00:19:14): Natalie and I worked together at Animals before.

**William Leborgne** (00:19:18): Oh, okay.

**William Leborgne** (00:19:19): There's a lot of things to mention.

**Nathalie Schrans** (00:19:20): Yeah.

**Nathalie Schrans** (00:19:22): Yeah, Ada's also from Animals.

**Nathalie Schrans** (00:19:25): Carrie.

**Nathalie Schrans** (00:19:27): Carrie, Jessalyn, yeah, a lot of people.

**Sydney Arin Go** (00:19:28): Well, yeah, a bunch of people.

**Sydney Arin Go** (00:19:31): So we do.

**Sydney Arin Go** (00:19:32): I do have some recurring chats with them.

**Sydney Arin Go** (00:19:33): So definitely feel free to, you know, connect with people, us, if you want to.

**Sydney Arin Go** (00:19:40): Yeah.

**Sydney Arin Go** (00:19:41): Okay.

**Sydney Arin Go** (00:19:41): So how did you, did you have any specific questions on the pipeline or anything that you want to answer first?

**William Leborgne** (00:19:47): Or do you just want me to show you the Hex pipeline and how we built it and all that?

**William Leborgne** (00:19:52): Yeah, mean, high level, the goal for me is, like, twofold.

**William Leborgne** (00:19:57): One, as I mentioned, like, I'm just very deeply curious.

**William Leborgne** (00:20:00): You know that I've used Aerox.

**William Leborgne** (00:20:03): I'm super interested in this technology and understanding.

**William Leborgne** (00:20:05): And what you said earlier really sparked something for me when you're like, you've obviously gone into both and you're like, I just think growthx is better.

**William Leborgne** (00:20:13): I'm super curious to understand why, what's better about it, how it works, et cetera.

**William Leborgne** (00:20:19): That's just from a curiosity perspective.

**William Leborgne** (00:20:21): But from a more tactical perspective, it's if I ever have a client, which I'm sure at some point will happen, says, okay, cool.

**William Leborgne** (00:20:28): Like, you produce these five articles, but how did you do it?

**William Leborgne** (00:20:31): Like, what was the reasoning?

**William Leborgne** (00:20:32): Like, what were the steps that happened?

**William Leborgne** (00:20:34): I have no way to answer that.

**William Leborgne** (00:20:36): I'll probably just be bullshitting if they ask me that.

**William Leborgne** (00:20:38): And I don't want to be in that position.

**William Leborgne** (00:20:40): So I think that's a core element.

**William Leborgne** (00:20:42): Also, I don't know if at some point I'm going to use it myself.

**William Leborgne** (00:20:46): Maybe at some point I'll, who knows with the growthx, like what roles you're going to be taking.

**William Leborgne** (00:20:51): But ultimately, like being pretty clear on the step after we built the content OS and we know what the topic clusters are and what you're going to create.

**William Leborgne** (00:20:59): Okay.

**William Leborgne** (00:20:59): you.

**William Leborgne** (00:21:00): What happens after that?

**William Leborgne** (00:21:01): Like, number one, yeah, how does it get built?

**William Leborgne** (00:21:03): Because I saw Natalie in a lot of her messages was writing like, oh, I built it, but like it's not working right, and I'm struggling with this and stuff.

**William Leborgne** (00:21:11): Like, I feel like I need to understand what that looks like and why maybe it's a struggle with certain clients and not as much with another one.

**William Leborgne** (00:21:19): So the building part and the tweaking it part is super interesting.

**William Leborgne** (00:21:23): And then the actual just like seeing it run and produce content.

**William Leborgne** (00:21:29): Maybe that's too much, but that's what I'd love to understand.

**Sydney Arin Go** (00:21:35): Natalie, are you okay with me sharing my screen?

**Nathalie Schrans** (00:21:38): Yeah, go for it.

**Nathalie Schrans** (00:21:39): I was also going to suggest maybe we could show the new, I think, what is it, V5 of the, I don't know if you're, do you mean showing Hex or Brex?

**Nathalie Schrans** (00:21:49): Oh my God, it's confusing.

**Sydney Arin Go** (00:21:51): Brex.

**Sydney Arin Go** (00:21:54): I was going to show the Hex pipeline.

**Sydney Arin Go** (00:21:57): How do I hide this?

**Sydney Arin Go** (00:21:58): Okay.

**Sydney Arin Go** (00:22:02): Yeah, so I was going to show the Hex pipeline just because I know how to talk to it and all the intricacies that went into that.

**Nathalie Schrans** (00:22:08): I know the Brex pipeline, Kirkland just built it, right?

**Nathalie Schrans** (00:22:13): So I actually haven't dug into that.

**Sydney Arin Go** (00:22:14): newest version?

**Sydney Arin Go** (00:22:16): Yeah.

**Sydney Arin Go** (00:22:16): Yeah, I think he did.

**Sydney Arin Go** (00:22:17): So I think what he did, and it looks very similar to the Hex pipeline, even the assignment direction was pulled almost directly from what we did with Hex, or the default one that he put in there.

**Sydney Arin Go** (00:22:28): So I think it is based on that one as well.

**Sydney Arin Go** (00:22:31): So, yeah.

**Sydney Arin Go** (00:22:33): But to answer your question for the first part, William, so Atlas pulls from Studio.

**Sydney Arin Go** (00:22:40): So all the workflows that Atlas runs, the engineering team programs them in Studio.

**Sydney Arin Go** (00:22:46): So this is the GrowthX Studio, and this is the library where all of those workflows live.

**Sydney Arin Go** (00:22:53): So, like here, there's the deep research content generator.

**Sydney Arin Go** (00:22:56): If you want to know, like, what specifically is

**Sydney Arin Go** (00:23:00): This This is probably where you'll find it.

**Sydney Arin Go** (00:23:02): And if you need to add like a specific, like an FAQ workflow, you might be able to find one here.

**Sydney Arin Go** (00:23:09): And that's what you would put into here.

**Sydney Arin Go** (00:23:10): So SEO content, FAQ generator.

**Sydney Arin Go** (00:23:13): So this is something that you could pull into Atlas if you want like a specific FAQ generator.

**Sydney Arin Go** (00:23:18): And then the research generator will also be here.

**Sydney Arin Go** (00:23:21): Personal keyword generate.

**Sydney Arin Go** (00:23:23): So it's all here.

**Sydney Arin Go** (00:23:24): So if you need specific ones, you can build using this.

**Sydney Arin Go** (00:23:29): But basically, the agentic article generation already has all of the ones that you need in there.

**Sydney Arin Go** (00:23:35): So what we usually do is when we have a new customer, we'll just copy and paste a good agentic article generation that we know is good.

**Sydney Arin Go** (00:23:41): So for me, it's Hex.

**Sydney Arin Go** (00:23:43): It used to be metronome.

**Sydney Arin Go** (00:23:45): And I know that they're all very similar.

**Sydney Arin Go** (00:23:47): So it's just what you're most familiar with at the moment.

**Sydney Arin Go** (00:23:49): So for me, currently, it's Hex.

**Sydney Arin Go** (00:23:50): I just copy paste this into the new workspace and then tweak it to that company.

**Sydney Arin Go** (00:23:58): It's Hex.

**William Leborgne** (00:23:59): Perfect.

**William Leborgne** (00:24:00): Yes.

**William Leborgne** (00:24:00): We'll quickly pause.

**William Leborgne** (00:24:02): I think I need to just make sure I understand, because this is quite different than the Aerox experience.

**William Leborgne** (00:24:08): So you're saying, you're like, oh, in studio, what I understood what you said earlier was that Atlas is like the production layer and studio is the UI where I go and play with things.

**William Leborgne** (00:24:21): But then you also said, I find the things in studio, like the Kubernetes or whatever, and then I put it into Atlas.

**William Leborgne** (00:24:28): So I'm a bit confused.

**William Leborgne** (00:24:30): Like what is Atlas and what is studio and how are you using it exactly?

**Sydney Arin Go** (00:24:37): Okay.

**Sydney Arin Go** (00:24:37): So here is, I'll show you the pipeline so that I can kind of just demonstrate it to you a little bit easier.

**Sydney Arin Go** (00:24:44): So this is the hex pipeline.

**Sydney Arin Go** (00:24:47): So one of the things that you'll see here, for example, is, where is it?

**Sydney Arin Go** (00:24:52): This one.

**Sydney Arin Go** (00:24:53): The function name is SEO content, identic article, draft workflow.

**Sydney Arin Go** (00:24:56): And then here, we should also have a.

**Sydney Arin Go** (00:25:00): SEO, content, agentic article, draft workflow.

**Sydney Arin Go** (00:25:03): So it's pulling this workflow into here.

**William Leborgne** (00:25:09): Oh, okay.

**Sydney Arin Go** (00:25:11): So they're hooked up to each other.

**Sydney Arin Go** (00:25:12): So engineers will build everything here.

**Sydney Arin Go** (00:25:14): So generally, you don't need to do anything in studio.

**Sydney Arin Go** (00:25:17): But if you want to see how something works, then you could go into it and then look at the overview of what's happening here.

**Sydney Arin Go** (00:25:22): And then it will tell you this is how it starts.

**Sydney Arin Go** (00:25:24): So this is kind of like if your customer asks you, how did we get there?

**Sydney Arin Go** (00:25:27): This is where you can figure out how each workflow works and answer that question of how we got there.

**Sydney Arin Go** (00:25:33): And then each of those workflows you will see as a function name in Atlas here or in the – so if you don't want to look at the YAML code, you should also be able to see it here.

**William Leborgne** (00:25:45): Okay.

**Sydney Arin Go** (00:25:46): These are like the simplified names as well.

**William Leborgne** (00:25:49): So studio, every piece that's in studio is like the equivalent of an Aerofs workflow.

**William Leborgne** (00:25:54): And then Atlas is like the equivalent of the grid.

**William Leborgne** (00:25:58): And so you – Exactly.

**William Leborgne** (00:25:59): So – Exactly.

**William Leborgne** (00:25:59): So

**William Leborgne** (00:26:00): You pull workflows, you put them into the grid.

**William Leborgne** (00:26:01): Got it.

**Sydney Arin Go** (00:26:02): Okay.

**Sydney Arin Go** (00:26:02): Now I get it.

**Sydney Arin Go** (00:26:03): Yeah.

**Sydney Arin Go** (00:26:04): And then what I usually do is just copy paste because this has all of the workflows that we need generally.

**Sydney Arin Go** (00:26:10): Okay.

**Sydney Arin Go** (00:26:11): And then, so the generic default, God, Sydney words, the default steps in the pipeline is the research topic.

**Sydney Arin Go** (00:26:22): So always have the input.

**Sydney Arin Go** (00:26:25): So this is the input step.

**Sydney Arin Go** (00:26:28): So this is where the writer or the managing editor can shape what this assignment will look like.

**Sydney Arin Go** (00:26:34): And then when they hit play, the first thing that runs is the research topic.

**Sydney Arin Go** (00:26:38): And then it drafts an article based on what's been researched.

**William Leborgne** (00:26:41): So this part, this doesn't have any of the artifacts feeding it yet.

**Sydney Arin Go** (00:26:44): This is just a fully AI written article.

**Sydney Arin Go** (00:26:47): And then after that, we get into the validating of the writing style guide.

**Sydney Arin Go** (00:26:51): And this is where we now turn this article into an article written for the customer.

**Sydney Arin Go** (00:26:57): So all of the good research and the bare...

**Sydney Arin Go** (00:27:00): The article structure, it's all done.

**Sydney Arin Go** (00:27:02): Now we're turning it into what could sound like a human written article or, you know, as close as we can get to that using the style guide and the artifacts and all the things that go into that.

**Sydney Arin Go** (00:27:11): After that, adds internal links based on the input.

**Sydney Arin Go** (00:27:14): So in the input, it asks you what's the website of your customer.

**Sydney Arin Go** (00:27:18): So it will look at that customer's sitemap or that website's sitemap.

**Sydney Arin Go** (00:27:23): And then that's where it'll pull the internal links from.

**Sydney Arin Go** (00:27:26): I know there's a way that you can specify if you have specific internal links that you want in your article.

**Sydney Arin Go** (00:27:29): You can specify as well.

**Sydney Arin Go** (00:27:31): And then it'll add source links.

**Sydney Arin Go** (00:27:33): So this step pulls from research.

**Sydney Arin Go** (00:27:35): And then what it does basically is it looks for all the claims in your article and then determines whether those claims need a source.

**Sydney Arin Go** (00:27:44): And if it says, yes, this claim needs a source, then it'll look at research and then put that external link into your article.

**Sydney Arin Go** (00:27:50): I think the reason why this happened originally was because if we just had the research and then the draft, it would start making up links.

**Sydney Arin Go** (00:27:58): So this step still isn't perfect.

**Sydney Arin Go** (00:28:00): Perfect.

**Sydney Arin Go** (00:28:00): That's the back and forth that we had with Brex, is that, or Natalie, correct me if I'm wrong, is that it would pull external links, but then sometimes the stat was not in the internal link that it added in, you know, and all that fun stuff.

**Sydney Arin Go** (00:28:13): Or claim with absolutely no link.

**Nathalie Schrans** (00:28:17): Even though the link existed in the research, yeah.

**Sydney Arin Go** (00:28:23): So this is one of the things that I think Eng is working on that MEs are also constantly working on and looking at and watching.

**Sydney Arin Go** (00:28:30): But yeah, so that's something that we do have to figure out at some point.

**Sydney Arin Go** (00:28:34): And then, final proofread checklist.

**Sydney Arin Go** (00:28:37): This is another validation step.

**Sydney Arin Go** (00:28:38): So now all of the, this is now to the tone of the customer that you're writing for.

**Sydney Arin Go** (00:28:43): Now we're going to go through the final proofreader, which is just looking at the commas, the periods, the wording.

**Sydney Arin Go** (00:28:48): Do we have anything in there that is not, that the target reader won't like?

**Sydney Arin Go** (00:28:53): And this is, we have a proofreader artifact as well, separate, that is a lot more pared down compared to the writing guidelines.

**Sydney Arin Go** (00:29:00): So this is just quick hits, like use data analysis over data analytics, that kind of thing.

**Sydney Arin Go** (00:29:05): And this will catch those.

**Sydney Arin Go** (00:29:07): Don't use them dashes.

**Sydney Arin Go** (00:29:08): This step will catch those.

**Sydney Arin Go** (00:29:09): And the meta tags, fact checking, header image.

**Sydney Arin Go** (00:29:11): We've actually validated the fact checking step doesn't really do a ton.

**Sydney Arin Go** (00:29:15): What happens in the research step is it will pull all of the research and then it will kind of give you a confidence report of some sort saying, we're pretty sure, like 85% sure that this is true or that this section is true.

**Sydney Arin Go** (00:29:30): And so this is, this kind of has a fact checker built in, which is why we went back and forth with Kirkland a couple of times.

**Sydney Arin Go** (00:29:38): And in one of our pipelines, we actually accidentally forgot to hook up the fact checking step.

**Sydney Arin Go** (00:29:44): So it was in the pipeline, but it wasn't really doing anything because we didn't add it.

**Sydney Arin Go** (00:29:49): We didn't connect it to anything else in the YAML code by accident.

**Sydney Arin Go** (00:29:54): So, and it didn't the output very much.

**Sydney Arin Go** (00:29:58): So we kind of saw that it didn't really do anything.

**Sydney Arin Go** (00:30:00): But it is one of the default ones that are included.

**Sydney Arin Go** (00:30:02): And then the header image will depend.

**Sydney Arin Go** (00:30:03): Usually you have to work with Katya on the header image and the hero image.

**Sydney Arin Go** (00:30:09): And then she'll add it usually as a, so we have it here.

**Sydney Arin Go** (00:30:13): So we had it as a separate step and I just added it in because I wanted to clean up a little bit.

**Sydney Arin Go** (00:30:20): Yeah.

**Sydney Arin Go** (00:30:21): So before I go on any questions, yes.

**William Leborgne** (00:30:23): Yeah.

**William Leborgne** (00:30:24): Why do it this way where you draft an article, just AI article based on research, without the use of artifacts from the beginning?

**Sydney Arin Go** (00:30:35): That doesn't make sense to me right now.

**Sydney Arin Go** (00:30:38): So one of the things that used to happen was because we wanted to have like one big step all at once, is the drafter would write the article in chunks to make sure that every single step is validated all across the board.

**Sydney Arin Go** (00:30:52): So what we got, the result was well-written paragraphs and sections that didn't really connect.

**Sydney Arin Go** (00:31:00): To each other, because the AI was going, this section, great, and then validating against the style guide, validating, and then, you know, so we got in chunks that weren't, I'm not sure if you remember this, Natalie, but it was, it was a lot of disconnected sections, one after the other.

**Sydney Arin Go** (00:31:15): And then, so this solution kind of worked better, where we have the bare bones, we have the structure, and then we can start adding in all the tone and style things that the customers want.

**William Leborgne** (00:31:26): Mm, okay.

**William Leborgne** (00:31:28): And then, including also, like, the article plugging their product in the right place, like saying, you know, Brex's savings account, blah, blah, blah, blah, blah, would come into the validating writing style guide section.

**Sydney Arin Go** (00:31:45): Yes, it would depend, though, on how your pipeline is set up.

**Sydney Arin Go** (00:31:49): So, that was the next thing that I wanted to show you in the pipeline, is that you can customize your drafter.

**Sydney Arin Go** (00:31:55): So, anything here is customizable.

**Sydney Arin Go** (00:31:58): So, here's the inputs.

**Sydney Arin Go** (00:32:00): Where is it?

**Sydney Arin Go** (00:32:03): Properties here.

**Sydney Arin Go** (00:32:03): So input schema.

**Sydney Arin Go** (00:32:04): So this is all of the things, this will list all the things that your writer or your ME will need to add into HEX.

**Sydney Arin Go** (00:32:11): So this is the default assignment direction.

**Sydney Arin Go** (00:32:14): I'm just going to open this.

**Sydney Arin Go** (00:32:16): It works here as well.

**Sydney Arin Go** (00:32:17): So this is the default assignment direction that will appear here.

**Sydney Arin Go** (00:32:21): So this is the YAML code.

**Sydney Arin Go** (00:32:23): So anytime you create a new article, this is what will pop up.

**Sydney Arin Go** (00:32:26): Where's my cursor?

**Sydney Arin Go** (00:32:28): And you can change this.

**Sydney Arin Go** (00:32:29): Like all of this can be changed.

**Sydney Arin Go** (00:32:32): Then, so this is still input.

**Sydney Arin Go** (00:32:35): So this is the first step.

**Sydney Arin Go** (00:32:36): First step is research.

**Sydney Arin Go** (00:32:38): Here are the instructions for your researcher.

**Sydney Arin Go** (00:32:40): This you can change.

**Sydney Arin Go** (00:32:42): This is what we've found works for HEX.

**Sydney Arin Go** (00:32:44): So this is what we keep in here.

**Sydney Arin Go** (00:32:46): But if you need any specific, like don't mention competitors, this is where you'd put it.

**Sydney Arin Go** (00:32:49): So for us, it's Tableau, Power BI, Looker, Mode, Databricks.

**Sydney Arin Go** (00:32:54): We don't want you to mention or link to these articles.

**Sydney Arin Go** (00:32:57): So don't use these.

**Sydney Arin Go** (00:33:00): is what we've said.

**Sydney Arin Go** (00:33:01): And the researcher does a pretty good job of steering clear of these.

**Sydney Arin Go** (00:33:06): We also have specific, like, good examples of what we want, of data that we want the researcher to pull.

**Sydney Arin Go** (00:33:12): We want you to pull specific stats, not just, you know, I actually don't know what this is.

**Sydney Arin Go** (00:33:17): This is, Kavishka changed this recently.

**Sydney Arin Go** (00:33:23): Yes.

**Sydney Arin Go** (00:33:23): So we have two criticals here.

**Sydney Arin Go** (00:33:25): I did this one.

**Sydney Arin Go** (00:33:26): He did this one.

**Sydney Arin Go** (00:33:27): But yeah, so you can add in all of the stuff that you want to add in here in the instructions.

**Sydney Arin Go** (00:33:32): And then your researcher will do that.

**Sydney Arin Go** (00:33:34): We have a couple of research tools that we use.

**Sydney Arin Go** (00:33:36): Exa and Tavoli are the ones that we use the most.

**Sydney Arin Go** (00:33:38): Exa is better for technical topics.

**Sydney Arin Go** (00:33:40): Research, Kathy, I think for Panther, we'll probably use Exa because security is a little bit more technical.

**Sydney Arin Go** (00:33:48): For Hex, because even though they are technical, our content was a little bit more top of funnel.

**Sydney Arin Go** (00:33:52): So like, what are data apps, that kind of thing we decided to have is a little bit faster.

**Sydney Arin Go** (00:33:56): And so, you know, the trade-off was better and it's still accurate.

**Sydney Arin Go** (00:33:59): way it is.

**Sydney Arin Go** (00:34:00): just, it's not as good on the technical topics.

**Sydney Arin Go** (00:34:02): But if you do have a technical customer, then just change it to Excel, and you just have to type it and hit save.

**Sydney Arin Go** (00:34:09): And the next step here would be the article drafter.

**Sydney Arin Go** (00:34:12): So this is the workflow.

**Sydney Arin Go** (00:34:14): I tested, so this used to be Sonnet.

**Sydney Arin Go** (00:34:17): I tested Opus, Opus 4.5, and that worked better, so I just kept it as Opus.

**Sydney Arin Go** (00:34:23): And then here is the direction again.

**Sydney Arin Go** (00:34:26): So you've got the instructions and the directions.

**Sydney Arin Go** (00:34:28): And so here's where the customization happens.

**Sydney Arin Go** (00:34:29): so if you want specific features to be put in here, this is where you'd put it.

**Sydney Arin Go** (00:34:33): So here are, so here's the directions to follow.

**Sydney Arin Go** (00:34:36): This is pulling from the assignment direction at the very beginning, the input that the ME will put in.

**Sydney Arin Go** (00:34:41): And who we typically write for, so always look at your artifact, the audience persona.

**Sydney Arin Go** (00:34:45): And then if you want to pull in your artifacts, product services, this is where you would also add that instruction.

**Sydney Arin Go** (00:34:51): If this is like completely empty, then it will ignore all of the artifacts.

**Sydney Arin Go** (00:34:56): And so here, here's the positioning that we do for hex.

**Sydney Arin Go** (00:34:59): And then we also also have.

**Sydney Arin Go** (00:35:00): We a specific thing that we did for Hex is we want the customer stories integration.

**Sydney Arin Go** (00:35:04): We tried this as a separate step, and it works better here in the article drafter, which is why we just added it in under directions, and then also linked it to our customer spotlights artifact that will inform this stuff.

**Sydney Arin Go** (00:35:16): So if anything, if you want to do specific instructions for your article drafter, this is where it would go.

**William Leborgne** (00:35:24): Just to clarify on this, what you're looking at, though, is the article creation step.

**Sydney Arin Go** (00:35:29): It's not the following step with the writing guidelines, or is this the writing guidelines?

**Sydney Arin Go** (00:35:34): Nope.

**Sydney Arin Go** (00:35:35): This is the draft article step.

**William Leborgne** (00:35:37): Okay, okay, okay.

**William Leborgne** (00:35:39): But in there, you are giving it artifacts.

**William Leborgne** (00:35:41): I thought that the idea was that you gave them the artifacts in the following step.

**William Leborgne** (00:35:44): So they just create like a clean AI content, and then we give it the artifacts.

**Sydney Arin Go** (00:35:49): I guess, sorry, so I may have misspoke.

**William Leborgne** (00:35:52): We don't give it the writing guidelines.

**William Leborgne** (00:35:55): Oh, it's just the writing guidelines.

**William Leborgne** (00:35:57): But we do give them the artifacts in the article drafts.

**Sydney Arin Go** (00:36:01): Anything that will be related to research, basically.

**Sydney Arin Go** (00:36:04): So audience persona, you need to know who you're writing for.

**Sydney Arin Go** (00:36:07): So that one will put it in.

**Sydney Arin Go** (00:36:09): Products and services, so you can represent.

**Sydney Arin Go** (00:36:11): So it does know what company you're writing for.

**Sydney Arin Go** (00:36:14): So if it's going to mention products and services anyways, you can add in the products and services artifact, or you can tell it to not do it entirely.

**William Leborgne** (00:36:21): Okay, okay, okay.

**Sydney Arin Go** (00:36:23): Got it.

**Sydney Arin Go** (00:36:23): But these are things that it will not do if you don't put this in the instructions.

**Sydney Arin Go** (00:36:28): So the article drafter itself is not hooked up to any of your artifacts, from my understanding.

**Sydney Arin Go** (00:36:34): Though you may need to ask if that's changed.

**Sydney Arin Go** (00:36:37): Because anything that's changed in studio, I don't really follow too closely anymore.

**Sydney Arin Go** (00:36:44): But from the last time, well, it was a week, two weeks ago, but things changed so fast.

**William Leborgne** (00:36:48): Before the break, I talked to Kirkland, and that was my understanding of how this works.

**William Leborgne** (00:36:54): Okay, this is great.

**Sydney Arin Go** (00:36:55): But yeah, so customization can happen here.

**William Leborgne** (00:36:58): Yeah.

**Sydney Arin Go** (00:36:59): Yeah, no.

**William Leborgne** (00:37:00): I'm also a little surprised that the UI is just this long thing that you have to kind of scroll down and try and find the right place versus more like chunky block boxes or something.

**William Leborgne** (00:37:09): But, I mean, I know that they're still building it while we're, they're building the train tracks while the train is going, so.

**Sydney Arin Go** (00:37:15): Yeah.

**Sydney Arin Go** (00:37:16): Yeah.

**Sydney Arin Go** (00:37:16): Well, one of the easiest ways actually to customize this pipeline is just to do it in Claude.

**Sydney Arin Go** (00:37:21): Because this is YAML code, it will understand us.

**Sydney Arin Go** (00:37:24): So you can just ask it, hey, I actually want an extra step for the researcher.

**Sydney Arin Go** (00:37:28): Here's the function.

**Sydney Arin Go** (00:37:28): You don't even need to give it the function name.

**Sydney Arin Go** (00:37:31): So, honestly, another thing, if anything's happening in your pipeline that you're like, why is this happening?

**Sydney Arin Go** (00:37:36): Just paste your YAML code in Claude and say, hey, this is the result I'm getting.

**Kathy Lam** (00:37:40): Is there anything in here that is causing that to happen?

**William Leborgne** (00:37:43): Oh, .

**William Leborgne** (00:37:44): That's, that's awesome.

**William Leborgne** (00:37:46): Okay.

**Sydney Arin Go** (00:37:47): So, I think Panzer has it in Ocean, but we do have a, like, pipeline updater optimizer personalization.

**Sydney Arin Go** (00:37:57): So, I he has guidelines.

**Sydney Arin Go** (00:37:58): I think it's a notion I can change.

**Sydney Arin Go** (00:38:00): Try to look it up for you of how, like what he, how he set up his cloud project to make this easier.

**William Leborgne** (00:38:09): Okay.

**William Leborgne** (00:38:09): I know we're almost on time.

**William Leborgne** (00:38:11): Is there any chance you could just give us a quick peek on the workflow for article optimizations?

**William Leborgne** (00:38:17): Because that's the other most common use case.

**William Leborgne** (00:38:21): And I'm just trying to understand how you can do that.

**Sydney Arin Go** (00:38:24): So what do you mean article optimizations?

**William Leborgne** (00:38:26): So instead of creating something net new, which is what this pipeline does, it's taking an existing article that they have and optimizing and making it better, basically.

**Sydney Arin Go** (00:38:37): So the refresh pipeline?

**William Leborgne** (00:38:39): Yes.

**Sydney Arin Go** (00:38:41): Redis has one, I think.

**Sydney Arin Go** (00:38:43): Redis Atlas Editorial.

**Sydney Arin Go** (00:38:50): So we've been testing the refresh pipeline for a while, and it's actually with Redis, even what we've started doing is just doing, or what they've started doing, because I'm not on Redis anymore.

**Sydney Arin Go** (00:38:59): I should just do do

**Sydney Arin Go** (00:39:00): We it manually, because what the pipeline does is it pulls, so you just have to put in a URL, and it will scrape that whole page, understand the HTML, and then pull all the text into it.

**Sydney Arin Go** (00:39:15): And then from there, it will analyze the SEO, and then do some research, and then refresh the article based on that.

**Sydney Arin Go** (00:39:22): But it really is a hit or miss, so the scraping actually is really good, it gets every single part of the article.

**Sydney Arin Go** (00:39:32): But if you do have a customer that has a really not great website, like understory, what wasn't great to begin with, the H2s were all over the place because they weren't really H2s, that kind of thing, then this will have trouble with that.

**Sydney Arin Go** (00:39:46): But so SEO analysis usually does, I know it looks for primary keywords and secondary keywords, but I'm not 100% if it looks for semantic keywords, which is where the problem comes in here.

**Sydney Arin Go** (00:39:57): Like if you're refreshing an article, you probably want to add in some...

**Sydney Arin Go** (00:40:00): semantic keywords, make sure the sections are all good, look at search intent and all that, and this doesn't take it all the way there.

**Sydney Arin Go** (00:40:07): I think it takes it like 50% of the way there, in my opinion, sometimes 60, but you still do need that human, is this actually better to be in there?

**Sydney Arin Go** (00:40:21): So when I asked Kavishka if he uses this pipeline, he said that they are still doing manually, which is why this is empty.

**William Leborgne** (00:40:29): This is really surprising to me, because I guess just a simple question, like do we not do a lot of article refreshes for clients?

**Sydney Arin Go** (00:40:38): I think we, I actually don't think that we do, although like Redis does, like I did a full content audit on Redis, and they had like stuff from 2015, so they need a ton of refreshes.

**Sydney Arin Go** (00:40:56): They had over like 400, they had a thousand pages, 400 pages were still usable.

**Sydney Arin Go** (00:41:00): And then like about 200 of them need refreshes.

**Sydney Arin Go** (00:41:02): So like we do do a ton of refreshes, but because some of those articles are really old, it's really just light touches.

**Sydney Arin Go** (00:41:09): Just update here, update here, and then, you know, go on your way.

**Sydney Arin Go** (00:41:14): I have used the refresher.

**Sydney Arin Go** (00:41:16): Sorry.

**William Leborgne** (00:41:16): Sorry, more of that is done manually than with a pipeline.

**Sydney Arin Go** (00:41:23): They do it manually now, from my understanding.

**Sydney Arin Go** (00:41:26): I have tried the pipeline and it does, it works.

**Sydney Arin Go** (00:41:30): Maybe it's in the archive.

**Sydney Arin Go** (00:41:32): Nope, there's no archived here.

**Sydney Arin Go** (00:41:34): Oh, here.

**Sydney Arin Go** (00:41:35): Nope.

**Sydney Arin Go** (00:41:36): Yeah, I don't know.

**Sydney Arin Go** (00:41:36): I don't know where my pipeline went because I have done it and it does work.

**Sydney Arin Go** (00:41:41): Like it will take you 60% of the way there.

**Sydney Arin Go** (00:41:42): It's just, you do have to verify if it is making things better.

**Sydney Arin Go** (00:41:46): And it's the same with a human writer though.

**Sydney Arin Go** (00:41:48): A human writer refreshes a piece.

**Sydney Arin Go** (00:41:50): You do have to verify if this is making things better or if it's just adding things that don't really need to be there.

**William Leborgne** (00:41:54): So.

**William Leborgne** (00:41:55): Totally.

**William Leborgne** (00:41:55): Yeah, yeah.

**William Leborgne** (00:41:57): That's really interesting to me because I feel.

**William Leborgne** (00:42:00): Like that's like almost more important for certain companies, especially like NetRix, for instance, that has like a  ton of content.

**William Leborgne** (00:42:08): I feel like content refreshes, you're going to get faster, better wins than net new content.

**William Leborgne** (00:42:15): And so, yeah, it just surprises me that that's not a bigger part of our business.

**William Leborgne** (00:42:19): I understand how AI pipeline works better for net new.

**William Leborgne** (00:42:22): It's easier in every way possible.

**William Leborgne** (00:42:24): But like when I was using AeroOps, like the optimizations, the refreshes, as you call them, was what got us the most bang for our book.

**Sydney Arin Go** (00:42:35): Yeah, no, refreshing is very important, especially, again, customers like Redis with 2015 articles in 2015, 2014.

**Sydney Arin Go** (00:42:42): And the biggest worry is if we remove this, are we going to get penalized by Google?

**Sydney Arin Go** (00:42:46): And we're like, no, but it'll make you work better.

**Sydney Arin Go** (00:42:50): So I do think it works.

**Sydney Arin Go** (00:42:51): I would, if you are creating a refresh pipeline, I would ask Kirkland and Edge for help on that one, just to see if there's anything new with that pipeline.

**Sydney Arin Go** (00:43:00): They've optimized it even better because I don't, it wasn't that bad to be completely honest.

**Sydney Arin Go** (00:43:05): It's just for specific customers, it might be a bit much to add in all that information because it does add new information and sometimes it's a 50-50.

**Sydney Arin Go** (00:43:16): Sometimes the new information is good.

**Sydney Arin Go** (00:43:18): Sometimes you're wondering where it came from and it's from an unrepeatable source or something.

**William Leborgne** (00:43:22): Yeah, gotcha.

**William Leborgne** (00:43:24): Okay, last question I promise and I'll let you guys go.

**William Leborgne** (00:43:27): So the primary pipeline that we use is new content generation.

**William Leborgne** (00:43:33): Are there any other pipelines that were very strong that we use across a lot of different clients, like landing page creation or something else?

**William Leborgne** (00:43:43): Like what other pipelines do we use very often?

**Sydney Arin Go** (00:43:48): Often, not none that I know of.

**Sydney Arin Go** (00:43:50): Okay.

**Sydney Arin Go** (00:43:52): Yeah.

**Sydney Arin Go** (00:43:53): Okay.

**Sydney Arin Go** (00:43:54): do have a very strong, oh, we do have, what's it called?

**Sydney Arin Go** (00:43:59): The The

**Sydney Arin Go** (00:44:00): The programmatic SEO pipeline, though, Kathy told me that we don't do programmatic SEO anymore in Sprintz because they're a little bit more custom.

**Sydney Arin Go** (00:44:10): I think Ada told you, right, Kathy?

**Sydney Arin Go** (00:44:12): Is that right?

**Kathy Lam** (00:44:13): That we don't do SEO anymore?

**Kathy Lam** (00:44:15): It was one of the things we were considering, but yeah, I think unless it's like a special project, then it's not our standard approach anymore, unfortunately.

**William Leborgne** (00:44:27): Okay.

**William Leborgne** (00:44:28): But we do have strong programmatic pipelines.

**William Leborgne** (00:44:30): That's good to know.

**William Leborgne** (00:44:32): Okay.

**Sydney Arin Go** (00:44:33): The ENG team is good at building the programmatic pipelines because they have all the building blocks.

**Sydney Arin Go** (00:44:38): It's just customizing them for the customers.

**Sydney Arin Go** (00:44:42): Like one of our customers is SentinelOne.

**Sydney Arin Go** (00:44:44): They have a pipeline that does end-to-end from like beginning CVE pages all the way to the end.

**Sydney Arin Go** (00:44:49): So it looks for the CVE pages, updates itself, and then publishes to SentinelOne's website.

**Sydney Arin Go** (00:44:54): So there's really very little oversight from our team, and because it's very objective, they're just CVEs.

**Sydney Arin Go** (00:45:01): It just goes end-to-end.

**Sydney Arin Go** (00:45:03): For Webflow, we've done their integration pages are all PSEO.

**Sydney Arin Go** (00:45:08): It took us a couple of weeks, about a month to calibrate it.

**Sydney Arin Go** (00:45:12): then after calibration, it just did its thing.

**Sydney Arin Go** (00:45:15): So it's just because the customer is very particular.

**Sydney Arin Go** (00:45:17): And if you're doing it at scale, then you really have to get it right.

**Sydney Arin Go** (00:45:21): So that's the only challenge with PSEO, which is why I don't think we do it with Strategy Sprint.

**Sydney Arin Go** (00:45:25): But the engineering team can build PSEO pipelines really well.

**Kathy Lam** (00:45:29): Okay.

**Kathy Lam** (00:45:30): Yeah, think because the Sprint is so short, this is something we can tackle in the next phase, rather than in the initial eight-week Sprint.

**Kathy Lam** (00:45:39): So it's still possible, but just not until phase two.

**William Leborgne** (00:45:43): Okay.

**Sydney Arin Go** (00:45:44): Yeah.

**Sydney Arin Go** (00:45:45): I like if you want to see Webflows integrations, this is their integration guide, and it's literally just one step.

**Sydney Arin Go** (00:45:58): As soon as it loads.

**Sydney Arin Go** (00:46:00): Um, these are, so this, the research tool and integration, I actually don't, didn't see that before.

**Sydney Arin Go** (00:46:06): Um, and then we just added a validate links, um, but it's just hit play and then add in whatever you want to integrate with, hit play, and then done.

**Sydney Arin Go** (00:46:14): Um, this is all generic.

**Sydney Arin Go** (00:46:16): It doesn't need to change.

**Sydney Arin Go** (00:46:17): Um, and then it drafts a really good guide that I think they take 10 minutes to edit just to add in links and stuff.

**Kathy Lam** (00:46:25): Um, and then publish.

**Kathy Lam** (00:46:28): awesome.

**Sydney Arin Go** (00:46:29): Um, yeah, this is, um, so yeah, yeah, before I joined Sprints, I was the only person working on Webflow.

**Sydney Arin Go** (00:46:40): Um, and I batted out 35 articles a week for these pages.

**Sydney Arin Go** (00:46:44): Um, I did another 10 on their, um, what's it called another type of page that they wanted.

**Kathy Lam** (00:46:49): Um, and it was a lot of work, but it was completely doable.

**William Leborgne** (00:46:53): Cool.

**Kathy Lam** (00:46:54): Okay.

**Kathy Lam** (00:46:54): I have a question.

**Kathy Lam** (00:46:55): Um, think in one of the customers, they have like an AI, uh, rule.

**Kathy Lam** (00:47:00): Do we just flag it or we will just add it to the Atlas instructions?

**Kathy Lam** (00:47:08): Is that something I need to flag if I've seen it in their shared docs or will you and Nathalie automatically see it once I share it in the internal docs?

**Sydney Arin Go** (00:47:20): We should be able to see it.

**Sydney Arin Go** (00:47:21): So is it like a style guide with AI-isms that they want to avoid?

**Kathy Lam** (00:47:25): It's two things.

**Kathy Lam** (00:47:27): They have like a style guide, which is ridiculously long, but then they also have this thing called AI, I forgot what it's called.

**Kathy Lam** (00:47:34): I'll send it to us.

**Kathy Lam** (00:47:38): And it was specifically like, here's what AI should not do so that it doesn't look very AI-generated.

**Sydney Arin Go** (00:47:48): Okay, so what we usually do for those is those will go into the writing style guide and then when the validate writing guidelines step happens, then that's where.

**Sydney Arin Go** (00:48:00): That's where it'll catch those AI-isms and stuff that customers don't want.

**Sydney Arin Go** (00:48:05): So they'll go in the writing style guide.

**Sydney Arin Go** (00:48:07): The writer, the drafter will validate that.

**Sydney Arin Go** (00:48:10): And then what we did for HEX, because there were some technical terms that because the writing style guide will sometimes get long, the validator doesn't do a great job at picking everything up every single time.

**Sydney Arin Go** (00:48:21): And usually you'll see in the convergence report that it has like a 92% adherence or like an 80% adherence or something.

**Sydney Arin Go** (00:48:28): You had another step that was very specifically, here are five things that I need you to look for in this article and make sure it doesn't happen.

**Sydney Arin Go** (00:48:36): So that is something that we could do.

**Sydney Arin Go** (00:48:38): So it's just how many artifacts do we have to build to inform the pipeline that this is happening?

**Sydney Arin Go** (00:48:43): But generally it's just, it'll go into the writing guidelines and that is usually more than enough.

**Kathy Lam** (00:48:48): Cool.

**Kathy Lam** (00:48:49): Yeah, I just shared it in our like Zoom chat, but they, NetRisk was funny in that they have like a very, yeah, like a different voice and

**Kathy Lam** (00:49:00): Guide plus a specific, like, prompt chunk, they called it.

**Sydney Arin Go** (00:49:05): Nice.

**Sydney Arin Go** (00:49:06): Yeah, I think this would go into, this would probably go into another validation step.

**Sydney Arin Go** (00:49:10): If they're super strict on this, then this would probably go into another validation step just to make sure that it really is in there.

**Sydney Arin Go** (00:49:16): And then testing the pipeline to see if it's too much.

**Sydney Arin Go** (00:49:19): And if it's too much, then we can pull back.

**Sydney Arin Go** (00:49:23): Yeah, this would be another artifact.

**William Leborgne** (00:49:25): I've seen people write about that in Slack where they're like, oh, this is this many tokens or this, I think it was tokens, but they were like, it's too long.

**William Leborgne** (00:49:35): Like, it's, and is that a pretty common issue?

**Kathy Lam** (00:49:38): Like, if your pipeline has too many things, then it kind of breaks it?

**Sydney Arin Go** (00:49:43): Well, the problem is, is if it's too long, then there's a higher probability that there are things in there that are conflicting.

**Sydney Arin Go** (00:49:49): So if you have an instruction that's like, don't use em dashes, and then one of your good examples has an em dash.

**Sydney Arin Go** (00:49:54): Um, what the validation step does is it goes through the whole document and.

**Sydney Arin Go** (00:50:00): And validates your article against that document.

**Sydney Arin Go** (00:50:02): So everything, every single word, it will validate it against it.

**Sydney Arin Go** (00:50:06): And so in the YAML pipeline, you'll see I have a max iteration of 10 times.

**Sydney Arin Go** (00:50:10): It'll try over and over until it hits 10, and then it will tell you.

**Sydney Arin Go** (00:50:14): So I wasn't able to do this, this, and this.

**Sydney Arin Go** (00:50:18): So I've only adhered to the writing guidelines, like 90% or something like that.

**Sydney Arin Go** (00:50:22): And because there's something in there that's not kind of linking up, it can take like 30, 45 minutes to do that if there is something in there.

**Sydney Arin Go** (00:50:33): So the longer you're writing guidelines, the higher probability that something will mess with the pipeline, forcing it to do the max iterations and then making it run for a really long time.

**Sydney Arin Go** (00:50:45): But other than that, like you can have long writing guidelines.

**Sydney Arin Go** (00:50:50): It's just not super ideal either because usually you can just have it in short.

**Sydney Arin Go** (00:50:57): But you can see it here in the artifacts, like if it's long.

**Sydney Arin Go** (00:51:00): So it will tell you that these are 4.9,000 tokens, so it will tell you.

**Sydney Arin Go** (00:51:06): These are, we don't have these in the pipeline, which is why it's fine.

**Sydney Arin Go** (00:51:08): So the company research, customer spot, this one is actually quite long.

**Sydney Arin Go** (00:51:11): This should probably get condensed.

**Sydney Arin Go** (00:51:13): It's just, we can't lessen the number of customers that they have in their spotlights.

**William Leborgne** (00:51:20): Yeah, yeah.

**Sydney Arin Go** (00:51:22): Okay.

**Sydney Arin Go** (00:51:23): But yeah.

**William Leborgne** (00:51:24): This was super helpful, Sydney.

**William Leborgne** (00:51:26): mean, honestly, like just now I feel like I kind of have a clear understanding broadly of like what you guys are talking about when you're talking about building the pipeline, which what my understanding now is like most of the time when you're building a pipeline, you're going to an existing one that works well.

**Sydney Arin Go** (00:51:40): You're kind of doing a copy paste into yours and then you're going into that code and then making specific instructions for that new client.

**Sydney Arin Go** (00:51:46): And that's really where you're doing it.

**William Leborgne** (00:51:48): And then you're testing it, testing it, seeing, am I getting really high quality for this new client?

**William Leborgne** (00:51:53): Okay, I'm not.

**William Leborgne** (00:51:54): And so that's what Natalie was struggling with with Brex is like, I'm, I copied it.

**William Leborgne** (00:52:00): I put the right instructions, but I'm not getting what I need.

**William Leborgne** (00:52:02): need to keep tweaking it to get it to where it needs.

**Nathalie Schrans** (00:52:06): Yeah, and a lot of the time, it's not always something that we can fix.

**Nathalie Schrans** (00:52:09): Like, it's something that a genuine, like, engineering expert who can make sure that we're not doing things, because that's my concern is, like, I feel like the edits I'm making, they make sense to me, and I've worked with them in Claude, but what if it's creating conflict that's not solving the problem, and it's just adding new problems.

**Nathalie Schrans** (00:52:27): So there's kind of, like, a limit to what we can do in terms of the pipelines.

**Nathalie Schrans** (00:52:31): And also, in the end, especially for strategy sprint clients, Kirkland is supposed to audit all of our pipelines anyway to make sure that they're, like, fully optimized and working correctly.

**William Leborgne** (00:52:42): Okay.

**Nathalie Schrans** (00:52:45): But it is helpful to know what's happening in the back end and what variables we have control over.

**William Leborgne** (00:52:51): Kirkland is kind of like the inspector and the plumber, you know?

**Nathalie Schrans** (00:52:54): He's like, yeah, up here and let me go, fix it.

**Nathalie Schrans** (00:52:58): Right, exactly, exactly.

**Nathalie Schrans** (00:53:01): Yeah, Kirkland's still struggling with the Brex pipeline.

**Sydney Arin Go** (00:53:08): Here is, if you want to see what an exit audit looks like, this one is hexes.

**Nathalie Schrans** (00:53:16): Oh, yeah.

**William Leborgne** (00:53:19): So Kirkland wrote this or created this?

**Sydney Arin Go** (00:53:22): Yep.

**William Leborgne** (00:53:24): Okay.

**Sydney Arin Go** (00:53:26): And then I think Redis also has one.

**Sydney Arin Go** (00:53:28): Actually, here are all of the Sprint audits.

**Sydney Arin Go** (00:53:30): we've got hex, Redis, and ReadAI currently.

**Sydney Arin Go** (00:53:33): And I'll send this link here.

**Sydney Arin Go** (00:53:35): There you go.

**Sydney Arin Go** (00:53:35): And then you can see, like, what Kirkland's notes are so that you can see where they're conflicting stuff.

**Sydney Arin Go** (00:53:43): What's it called?

**Sydney Arin Go** (00:53:43): Identified.

**William Leborgne** (00:53:46): Nice.

**William Leborgne** (00:53:47): Thanks.

**Sydney Arin Go** (00:53:49): I hope this was helpful.

**Sydney Arin Go** (00:53:50): feel like I was just talking for 30 minutes and I apologize.

**Kathy Lam** (00:53:54): We were absorbing it all.

**Sydney Arin Go** (00:53:56): So it was all gold.

**Sydney Arin Go** (00:53:58): No.

**Sydney Arin Go** (00:53:59): No.

**Sydney Arin Go** (00:53:59): I feel like...

**Sydney Arin Go** (00:53:59): talking what

**Sydney Arin Go** (00:54:00): Brain starting to slow.

**Sydney Arin Go** (00:54:02): Like it hit 1.30, so it's 1.42 a.m.

**Sydney Arin Go** (00:54:05): for me.

**Sydney Arin Go** (00:54:05): And I could feel it going, hmm, we're starting.

**William Leborgne** (00:54:08): Gears are starting to slow down.

**Sydney Arin Go** (00:54:11): Words aren't wording.

**Nathalie Schrans** (00:54:13): Yeah.

**Nathalie Schrans** (00:54:14): No, I feel like I've always learned so much from you, Sydney, even when it's like 2 a.m.

**Nathalie Schrans** (00:54:18): your time.

**Nathalie Schrans** (00:54:19): So it's impressive.

**Sydney Arin Go** (00:54:22): No, truly, thank you so much.

**Sydney Arin Go** (00:54:24): This is super helpful.

**William Leborgne** (00:54:25): And I will definitely hit you up in the future.

**Sydney Arin Go** (00:54:30): Yeah, I'm glad this was helpful.

**Sydney Arin Go** (00:54:34): Awesome.

**Sydney Arin Go** (00:54:35): Okay, I will let all of you go.

**Sydney Arin Go** (00:54:38): All right.

**Sydney Arin Go** (00:54:38): Thank you so much.

**Sydney Arin Go** (00:54:40): Bye-bye.

**Sydney Arin Go** (00:54:40): Have a great day.

**Sydney Arin Go** (00:54:41): Bye.

**Sydney Arin Go** (00:54:42): You too.
