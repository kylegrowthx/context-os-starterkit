# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-07-10
time: 15:30 UTC
duration: 19 minutes
organizer: saskia@growthx.ai
participants: Matthew Panzarino, Saskia Wartnaby, Nem Simic, Jenn Peters
fathom_recording_id: 73382531
fathom_url: https://fathom.video/calls/347619113
share_url: https://fathom.video/share/7ofwofJurQpX1SdPZ4LZPzHpkxb5jqKZ
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

The GrowthX content team discussed persistent issues with the Atlas workflow: bullet point formatting that is over-weighted toward text, article archetype selection heavily favoring how-to formats, and walls of text in article generation. Matthew outlined immediate workarounds including using explicit topic titles (e.g., "comparison of X vs Y") and the direction field to guide format selection. He also noted that an archetype picker is in development as a medium-term solution, with longer-term plans for prompt-based schema generation. The team reported mixed results with the Ask.ai chatbot formatting feature and flagged issues with external link hallucination, which are being addressed.

---

## Context

This is a weekly standup for the GrowthX content operations team working on Atlas, the company's AI-powered content generation and optimization system. Atlas is a core product being used internally to generate briefs and articles based on SERP analysis and keyword research. The team reports on workflow issues, blockers, and product improvements needed to scale content production. The standup was organized by Saskia Wartnaby and led by Matthew Panzarino, who manages prompt development and workflow optimization alongside Jason.

---

## Relevance

**To CheckThat:** Atlas is a proprietary AI visibility tool that demonstrates prompt optimization and SERP analysis capabilities; the archetype selection mechanism and brief generation reflect AEO principles and schema generation strategies that could inform CheckThat product development.

**To GrowthX Delivery:** Bullet point detuning, text density, and format rigidity are limiting Atlas usability and slowing internal content production; immediate workarounds (explicit titling, direction field) offer tactical relief while Matthew and Jason work on prompt semantics for medium-term fixes.

**To GrowthX Business Development:** Atlas maturity is improving but still has rough edges (Ask.ai formatting inconsistency, external link hallucination) that should be resolved before showcasing to prospects as a core product differentiator; the archetype picker coming soon will meaningfully improve user control and satisfaction.

---

## Overview

- Bullet point formatting issues persist; update pushed but needs further tweaking
- Article archetype selection heavily favors "how-to" format; immediate workaround via explicit topic/direction input
- Walls of text problem stems from recent prompt adjustments; fix in progress
- Internal linking improvements underway, addressing hallucinated external links

---

## Key Topics

### Bullet Point Formatting Issues

  - Recent update by Kirkland aimed to address the problem
  - Current state: "too well up-texty", needs further refinement
  - Temporary solution: leave bullet points as-is for now

### Article Archetype Selection

  - Atlas consistently choosing "how-to" format due to SERP analysis and archetype weighting
  - Immediate workaround: Use explicit titles (e.g., "comparison of X vs Y") and leverage direction field
  - Medium-term plan: Implement archetype picker for user selection
  - Long-term vision: Prompt-based schema creation and expanded format library

### Walls of Text Problem

  - Recent prompt tweaks led to overcorrection from skeletal outlines to dense text
  - Current state preferable to previous skeletal version but not ideal
  - Fix in progress to find balance between bullet points and paragraphs

### Ask.ai Chatbot Feature

  - Mixed success reported for reformatting content (e.g., creating bullets or tables)
  - Matthew's experience: Generally effective for bullet point reflowing
  - Ongoing formatting glitches (e.g., incorrect sentence encapsulation in bullets)
  - Recent fix implemented for cursor jumping issue during editing

### Internal Linking Improvements

  - Fix in review for hallucinated external links at end of articles
  - External linking still "wonky" with 404 errors reported
  - Validator issues noted for external linking

---

## Action Items

**Nem Simic (GrowthX)**
- Document specific issues w/ Ask.ai chatbot feature not following instructions (e.g. bullets, tables). Include examples. File ticket w/ details for dev review.

---

## Transcript
**Matthew Panzarino:** Good morning.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** How's everybody's, uh, everybody's workflows working?

**Matthew Panzarino:** Are the pipelines piping?

**Matthew Panzarino:** Hit me with any issues, ongoing stuff.

**Matthew Panzarino:** Um, I can share a couple of things from my side.

**Matthew Panzarino:** Anybody have anything specific?

**Saskia Wartnaby:** Um, I wanted to ask you if there's been any updates on the, uh, um, um, um, um,

**Saskia Wartnaby:** Bullet points, like a bullet list issue.

**Matthew Panzarino:** Kirkland pushed an update that was supposed to address this, I believe, yesterday or the day before.

**Matthew Panzarino:** If it's still happening, then we just need to tweak further, but I'm aware of it.

**Saskia Wartnaby:** I've encountered it myself, so.

**Saskia Wartnaby:** Okay, cool.

**Matthew Panzarino:** Track it down.

**Matthew Panzarino:** The concept is basically, or the underlying cause here is basically that we detuned the bullet points, but I think detuned it too far.

**Matthew Panzarino:** So we'll get to work on that.

**Matthew Panzarino:** I don't think it's in a good place currently.

**Matthew Panzarino:** I think it's too well up-texty still, so we'll chip away at it.

**Matthew Panzarino:** For now, just leave the bullet points.

**Saskia Wartnaby:** Okay.

**Saskia Wartnaby:** And then, sorry, my camera's off because it was really lagging, but I had another question.

**Saskia Wartnaby:** I've noticed, I think somebody's also brought it up.

**Saskia Wartnaby:** I wanted to check with you if there's been like a linear ticket about it, but how the outline...

**Saskia Wartnaby:** Always wants to give steps, and it always wants to give you like a quick guide, like a quick like overview, and then it wants to give you steps, and then it wants to give you like a timeline.

**Matthew Panzarino:** Yeah, this is the cause of this is pretty straightforward.

**Matthew Panzarino:** When the workflow does a SERP, a keyword gap analysis, basically a SERP analysis of the desired keywords, it goes out to the web and looks at the top ranking articles for that topic, decides what kind of article that is, and then picks from a list of archetypes.

**Matthew Panzarino:** There's about seven or eight of them, maybe a little bit more.

**Matthew Panzarino:** Those archetypes include things like how-to's, which include steps, common pitfalls, all this stuff.

**Matthew Panzarino:** It also includes other formats, listicles, news articles, you know, various other schemes.

**Matthew Panzarino:** That it can choose from to pick what kind of article it's about to write.

**Matthew Panzarino:** Unfortunately, it seems to be almost always just choosing how-to.

**Matthew Panzarino:** And whether that's a result of the fact that a lot of the content on the web that is built for SEO is built in how-to formats because it can keyword stuff and include a bunch of sections that rank well.

**Matthew Panzarino:** Or whether it's an internal thing, an us thing where it is, the how-to is weighted in a way where it picks it more than it should.

**Matthew Panzarino:** Regardless, that's what's happening.

**Matthew Panzarino:** It's picking the how-to article as an archetype that then applies to the brief that it generates.

**Matthew Panzarino:** And that brief that's generated includes those sections, which would be appropriate in a specific how-to type schema.

**Matthew Panzarino:** I actually didn't think there's an argument about whether or not those sections should even be in that schema.

**Matthew Panzarino:** But that's really a different conversation.

**Matthew Panzarino:** That's like, okay, what is the how-to feel like?

**Saskia Wartnaby:** Yeah, that makes sense.

**Matthew Panzarino:** Is there a way to, um, okay, so you can't like stop it from doing that basically, you can't stop it from doing it, the way to stop it from doing that is to change your brief, so if you see your brief is a how-to article, grab the brief and refactor it, either use the Ask AI tool or you can use an external tool for now, but you can use the Ask AI tool to reflow the brief section of your brief, not the keyword analysis section, but the actual structure of the article, just say, hey, make this a comparison article, or make this a list article, right, and, um, that, at the brief, don't go beyond the brief, if you see it's the wrong format, um, you can delete sections from the brief and go from there if you still want steps, that sort of thing, but if you see that it's a wildly different archetype than the one you want, reflow the brief, that's the way to solve it.

**Saskia Wartnaby:** I think, I think the most, sorry, I think the most frustrating thing is that, like, I will give, like, ChatGPT all the same artifacts that Atlas has, um, and it will give me, like, a pretty decent brief, but Atlas just isn't.

**Saskia Wartnaby:** It's that.

**Saskia Wartnaby:** It's giving me something, like it has maybe similar information, but it's just structured in the complete wrong way.

**Matthew Panzarino:** And I think that's like the most frustrating part right now.

**Matthew Panzarino:** So the Atlas is giving you a really good brief, but it's giving you a really good single type of brief, basically.

**Matthew Panzarino:** That's what's happening.

**Matthew Panzarino:** And it's like, hey, this is a pretty good, pretty solid how-to article brief.

**Matthew Panzarino:** The solution to this, there's probably a branching set of solutions or solves here.

**Matthew Panzarino:** The one immediate step that you can do is you can, there are two major things that will influence pretty heavily the type of article that it wants to do.

**Matthew Panzarino:** One of those is, as I mentioned, sort of handled by the workflow.

**Matthew Panzarino:** It's, it's analysis of what articles are ranking well.

**Matthew Panzarino:** The second one is the title that a lot of people are still just using keywords.

**Matthew Panzarino:** Don't do that.

**Matthew Panzarino:** You know, use a very explicit.

**Matthew Panzarino:** The title that puts, you remember that title or that topic in the input field does not have to be what you want the eventual title to be.

**Matthew Panzarino:** And it certainly does not or should not be just a raw keyword.

**Matthew Panzarino:** So if you want a list of things, type, I want a list of things.

**Matthew Panzarino:** So, I mean, that's part of the prompt, right?

**Matthew Panzarino:** That topic.

**Matthew Panzarino:** And right now, I think a lot of people are just being like, keyword, and then it's very hands off the wheel.

**Matthew Panzarino:** And they're being surprised by the fact that it is very unpredictable or not being driven in the direction that they want.

**Matthew Panzarino:** Okay.

**Saskia Wartnaby:** That makes a lot of sense.

**Matthew Panzarino:** Thank you.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** If you've got, like, one that you really want to compare as an article and it keeps giving you the step-by-step guide, as an example, make sure that you're putting in your topic comparison of X versus Y, right?

**Matthew Panzarino:** And whatever keywords you have.

**Matthew Panzarino:** I think you'd be surprised by.

**Matthew Panzarino:** Some of the positive results have come out of that.

**Matthew Panzarino:** did some testing yesterday.

**Matthew Panzarino:** Also, you can, in the description, describe what you want.

**Matthew Panzarino:** I've had some success describing what I want in the direction field and just saying, I'd like a brief overview of this topic or I would like a summary of this topic or whatever you want there.

**Matthew Panzarino:** So you can double up by adding that into the direction field.

**Matthew Panzarino:** That's the immediate, you know, what can you do today?

**Matthew Panzarino:** Longer term, Jason and I are looking at all the prompts and analyzing how all of this could be better.

**Matthew Panzarino:** And one of the things that we came up with was that the archetype selection needs to be more transparent.

**Matthew Panzarino:** So we are working on a way to expose the archetypes for now, at the very least, so that you can pick between them.

**Matthew Panzarino:** So you might be able to select those artifacts very soon.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** Okay.

**Saskia Wartnaby:** That's really awesome.

**Saskia Wartnaby:** Thank you for that.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Because, yeah, it's, you know, if generating a wildly different kind of brief, you just have to reflow that brief.

**Matthew Panzarino:** That stinks, you know.

**Matthew Panzarino:** Anything that you have to do over and over, you know, to course correct, it's obviously something's arrived, so we'll figure it out.

**Matthew Panzarino:** But, yeah, it's pretty well known.

**Matthew Panzarino:** Everybody gets the same formats back almost always, unless you succeed in instructing it otherwise via your topic or direction.

**Matthew Panzarino:** At the moment, you're sort of, like, pushing against, though, the title force, which is the underlying prompt, doing that analysis and seeing those articles and picking the how-to.

**Matthew Panzarino:** So, give that a try.

**Matthew Panzarino:** I think you'll have some success there in the near term.

**Matthew Panzarino:** And then, longer term, yeah.

**Matthew Panzarino:** We want, like, the short, the medium term solve is probably to just have an archetype picker, so you can.

**Matthew Panzarino:** Choose from the list of a dozen or so schemas.

**Matthew Panzarino:** Down the road, I want more schema.

**Matthew Panzarino:** I want, you know, more options to pick from.

**Matthew Panzarino:** And then theoretically, at some point, we would have basically a prompt that created schemas.

**Matthew Panzarino:** So this is similar to, like, the assignment generation prompt, but it would be, like, a format generator where you can say, oh, I'd like this kind of format.

**Matthew Panzarino:** And then we have a library of formats that it will flow your articles into.

**Matthew Panzarino:** And Daniel's working on something like this for the PSEO work streams that we have.

**Matthew Panzarino:** But obviously, as you can imagine, it would be useful in a lot of cases because you kind of want a cluster of content that's in a very similar schema.

**Matthew Panzarino:** So we've got to build some tooling around that.

**Saskia Wartnaby:** But that's where we are.

**Saskia Wartnaby:** Amazing.

**Saskia Wartnaby:** Thank you so much for all that information.

**Saskia Wartnaby:** I need to head out, but thank you so much.

**Matthew Panzarino:** Thank you so much for that.

**Saskia Wartnaby:** Cool.

**Saskia Wartnaby:** Bye.

**Saskia Wartnaby:** Bye.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Any other questions, concerns, specific issues that I can help troubleshoot, et cetera?

**Nem Simic:** Yeah, one thing, Panzar, and I'm curious, I'm sure somebody's brought it up, but I've been running into the problem of, you know, just constant walls of text.

**Nem Simic:** Um, and even when I'm completely redoing the brief and really outlining where I want bullets, where I want the table, things like this, it's not transferring over when the actual article is generated.

**Nem Simic:** I'm curious if I should also be doing the same thing to the outline itself, maybe kind of doubling up the instructions to see if it would take it.

**Nem Simic:** But like, I don't know if there's much you can do at this point.

**Matthew Panzarino:** You just have to reflow it.

**Matthew Panzarino:** Um, I think at the end, uh, after, after article gen, um, it is a prompt thing, right?

**Matthew Panzarino:** That's a prompt thing.

**Matthew Panzarino:** Um,

**Matthew Panzarino:** I was telling Saskia at the top, it's the same issue that she's having.

**Matthew Panzarino:** It's described in a different way, I guess, but it's basically like, hey, the prompt originally was producing incredibly skeletal outlines with a lot of bullet points, and so we tweaked the prompt.

**Matthew Panzarino:** I didn't pick it, but Kirkland did.

**Matthew Panzarino:** I'm not blaming Kirkland.

**Matthew Panzarino:** We tweaked it, we're like, give me feedback, and he's like, tweaking, and now we've got walls of text.

**Matthew Panzarino:** Which, honestly, is better.

**Matthew Panzarino:** Like, you know, at least you have meat to work with, but somewhere in between is probably ideal.

**Matthew Panzarino:** So, need to just get with him, and we need to chop it up on, like, the semantics of that prompt, because basically it just got tweaked, the instructions for writing, its base instructions for writing got tweaked in a way that is producing very few bullet points.

**Matthew Panzarino:** And it basically, the prompt basically says, like, hey, don't use bullets unless you really need to, and the LLM's like, I never need to, like, what are you talking about, right?

**Matthew Panzarino:** And I think that's kind

**Matthew Panzarino:** So we just need to find a place in between, but that's what's going on.

**Matthew Panzarino:** So I don't know that you'll have a lot of success, to be honest, right? Because the article generation flow, which comes at the mid-juncture of the process, is the one that the underlying prompt of that generation step is saying, basically, chill out on bullet points. And so you're almost never going to be able to override that. You'll have to add it in as a polishing step.

**Nem Simic:** Okay, so has anybody had a lot of success with using that Ask.ai chatbot feature? Because often I'll try to tell it to put it in bullets or make it a table, and it just sometimes does, sometimes doesn't. I'd say more than 50% doesn't follow the instruction. So I'm curious if other people are running into the same issue.

**Matthew Panzarino:** I've generated a couple of dozen articles over the past week for AIMBIT and used the Ask.ai feature probably three to five times on each one. My experience with it has been that it will reflow bullets for the most part. However, there are still some issues with bullet point formatting where it encapsulates the following sentence incorrectly — you'll have five bullet points and then the sentence after will also be a bullet, and you can't escape out of it. I think there's a ticket on that. The cursor jumping issue when you edit has been fixed, so that's been resolved.

**Jenn Peters:** I haven't personally used it that much.

**Jenn Peters:** It's done well for me for, yeah, the bullet factor.

**Jenn Peters:** I haven't tried it like to change something to a table, quite honestly.

**Jenn Peters:** But I haven't used it like extensively, I would say, to get enough info to make a definitive decision on its scalabilities.

**Matthew Panzarino:** But if you, I think the best thing to do, Nika, you don't have to go crazy, but like some documentation of the issue.

**Matthew Panzarino:** And we can file it in a ticket and you can look at it because that feature is being driven pretty hard by one person.

**Matthew Panzarino:** So I would say he's going to want it out, you know, if there's something going on.

**Matthew Panzarino:** I wanted to mention, she's probably not on this call, but if some of the others of you have been experiencing this, I haven't.

**Matthew Panzarino:** I actually think it's pretty good, but some of the internal linking workflows were, have been hallucinating external links, like at the very end, even though they were, they were kind of fighting, finding the right links, then they would just kind of throw in like random links, even though there were opportunities to link on the client site.

**Matthew Panzarino:** And there's a fix being in for that one now being reviewed.

**Matthew Panzarino:** So I just want to flag that because somebody mentioned it to me yesterday.

**Matthew Panzarino:** And I activated NG on it, and they're working on fixing it.

**Matthew Panzarino:** The internal work, internal linking has been pretty good for me.

**Matthew Panzarino:** The external linking is still wonky.

**Matthew Panzarino:** Somebody mentioned yesterday, I can't remember who it was, maybe Moses, I'm sorry, a lot of calls.

**Matthew Panzarino:** But anyhow, we were talking about an external linking flow that was hitting 404s, as an example.

**Matthew Panzarino:** And that validator, something's up with that validator.

**Matthew Panzarino:** So, I hadn't filed a ticket on that.

**Matthew Panzarino:** But I just want to flag that internal linking one for folks, in case you saw that.

**Matthew Panzarino:** Because they're working on it.

**Matthew Panzarino:** All right, anything else?

**Matthew Panzarino:** My admonition is to bring things like that to these meetings, which will happen on a weekly cadence now. You can collect things that are nebulous — if you don't know if it's an exact bug or an underlying issue — and I'll work on those. Jason and I are working hard to update the prompts and get things in a better place to handle some of the bigger structural issues, like the rough structures of the articles being very similar and bullet points being absent. So we're cranking on that.

**Matthew Panzarino:** Thanks, folks.
