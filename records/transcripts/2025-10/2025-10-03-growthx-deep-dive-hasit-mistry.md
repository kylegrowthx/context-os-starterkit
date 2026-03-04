# GrowthX Deep Dive (Hasit Mistry)

<metadata>
date: 2025-10-03
time: 18:00 UTC
duration: 41 minutes
organizer: Erik O'Brien
participants: Erik O'Brien (GrowthX), Hasit Mistry (CodeRabbit)
fathom_recording_id: 91792580
fathom_url: https://fathom.video/calls/430090126
share_url: https://fathom.video/share/Un4kri3wjhq2VTtykM9EiGzxtXthUsfz
source: fathom
enriched_on: 2026-03-02 03:15 UTC
</metadata>

---

## Summary

Hasit Mistry, founding engineer and enterprise engineering lead at CodeRabbit, provided GrowthX with a comprehensive product walkthrough covering CodeRabbit's core functionality as an AI-powered code review tool, including pull request summaries, technical walkthroughs, interactive chat, pre-merge checks, and documentation generation. The conversation highlighted CodeRabbit's primary competitive advantages: comprehensive context building (cloning entire repos and probing multiple code sections), efficient cost management through per-seat pricing at $20/seat versus usage-based competitors, and intelligent model routing that assigns larger LLM models to complex tasks while using smaller models for simpler work. Key opportunities for GrowthX include creating feature comparison content, case studies around enterprise implementation, and educational content about CodeRabbit's technical capabilities and customer use cases.

---

## Context

GrowthX is a B2B content marketing agency working with CodeRabbit to develop editorial content that resonates with engineering teams and prospects. This meeting was arranged through Amanda (CodeRabbit's Head of Content or similar), who connected GrowthX's team with Hasit to understand CodeRabbit's product deeply — what it does, how teams use it day-to-day, and the value proposition for engineering organizations. Hasit structured the call as a standard customer-facing product demo, walking through CodeRabbit's platform via a live or recorded walkthrough and answering questions about features, competitive positioning, and customer reception. The goal was to gather primary-source product knowledge and customer insights that would inform content strategy and messaging.

---

## Relevance

**To GrowthX Delivery:**
- Feature comparison content opportunity: CodeRabbit's differentiators vs. Replite, BugBot, GitHub Copilot, and others can be structured into educational content for engineering audiences. Hasit flagged specific gaps in competing products (Copilot's poor review quality, Replite's popularity in enterprise, BugBot's emerging threat).
- Case study and ROI justification angle: CodeRabbit has dashboards showcasing usage metrics and ROI — this is a content hook for demonstrating value to engineering leaders and procurement teams evaluating the tool.
- Technical depth content needed: Comprehensive context building via CodeGraph analysis, pre-merge checks, and web search integration are sophisticated capabilities that require explanation through demos, walkthroughs, or comparison guides.

**To GrowthX Business Development:**
- Account expansion signal: Hasit is managing enterprise customers and building an enterprise engineering team — CodeRabbit is moving upmarket. GrowthX should position for higher-value engagements and long-term content strategies.
- Product maturity and momentum: Chat functionality and pre-merge checks are gaining traction; recent additions like web search and severity tagging suggest an active product roadmap. This signals stability and opportunity for sustained content work.
- Pricing model leverage: Per-seat at $20/seat is a core competitive advantage. GrowthX content should emphasize this positioning vs. usage-based competitors, which helps CodeRabbit close deals with cost-conscious enterprises.

**To CheckThat:**
- AI model efficiency and routing: CodeRabbit's engineering approach to cost management (model selection, context building, secure sandboxing) represents real-world AI optimization in a production B2B tool. This is relevant to CheckThat's visibility into AI implementation patterns and cost efficiency.

---

## Overview

- CodeRabbit is an AI-powered code review tool that automates and enhances the review process, offering features like pull request summaries, technical walkthroughs, and interactive chat.
- Key differentiators include comprehensive context building, competitive $20/seat pricing model, and integration with various development tools and platforms.
- Popular features among users include the chat functionality, pre-merge checks, and the ability to generate documentation automatically.

---

## Key Topics

### CodeRabbit Overview and Core Functionality

  - Automates code review process across multiple Git providers (GitHub, GitLab, Azure DevOps, Bitbucket)
  - Free for open-source projects, driving adoption and word-of-mouth growth
  - Key features:
      - Pull request summarization and technical walkthrough
      - AI-powered code review comments with committable suggestions
      - Interactive chat for clarifications and improvements
      - Learning capability to adapt to team preferences over time

### Advanced Features and Integrations

  - Web search capability to update AI knowledge in real-time
  - Integration with project management tools (JIRA, Linear) for ticket-based context
  - Pre-merge checks to ensure pull request quality and adherence to standards
  - Automatic documentation generation
  - External integrations with Notion and other knowledge bases via RAG

### Technical Capabilities and Performance

  - Language and framework agnostic due to use of frontier LLM models
  - Handles large, complex repositories through secure sandboxing and CodeGraph analysis
  - Comprehensive context building by cloning entire projects and probing different code parts

### User Experience and Interface

  - Primary interface is the pull request page within Git providers
  - Configurable at organization and project levels
  - Custom instructions and guidelines can be easily incorporated

### Competitive Advantages

  - Comprehensive context building capabilities
  - Competitive pricing model ($20/seat) enabled by efficient LLM call management
  - Interactive chat functionality not available in some competing products

### Customer Favorites and Feedback

  - Chat functionality highly appreciated and widely used
  - Pre-merge checks gaining popularity
  - Pull request summaries and walkthrough comments well-received
  - Committable suggestions and reduced noise in reviews

### Reporting and ROI Justification

  - Dashboards available to showcase usage metrics and justify ROI to decision-makers

---

## Action Items

- **Erik O'Brien (GrowthX):** Build feature matrices as artifacts for the content generation system, comparing CodeRabbit against key competitors (Replite, BugBot, GitHub Copilot) across dimensions like pricing, context building, chat, pre-merge checks, documentation generation, and integrations.
- **Erik O'Brien (GrowthX):** Follow up with Hasit Mistry or Amanda at CodeRabbit if additional product questions arise during content creation process or if GrowthX needs clarification on technical capabilities, customer use cases, or messaging angles.

---

## Transcript
**Hasit Mistry:** It's fine.

**Hasit Mistry:** Have a busy Friday.

**Hasit Mistry:** Somehow, a lot of things come up every Friday only.

**Hasit Mistry:** Yeah.

**Hasit Mistry:** Same here.

**Erik O'Brien:** I had not much on the calendar, and then all of a sudden, the last two days, no free time.

**Erik O'Brien:** So, well, appreciate you taking the time today.

**Erik O'Brien:** I'll try not to use the whole hour so I can give you some time back and get you on your way.

**Erik O'Brien:** But for context, we do these deep dives really just to better understand kind of the product and the business.

**Erik O'Brien:** And I don't know if you have context on GrowthX, but we're a content agency.

**Erik O'Brien:** So working with CodeRabbit to develop editorial content, it connects really with your customers and prospects.

**Erik O'Brien:** And so to do that well, we really like to understand the product from your perspectives, kind of what it does, how teams use it day to day.

**Erik O'Brien:** So like if you were introducing CodeRabbit to a new engineering team, like how would you describe the platform and its core value?

**Erik O'Brien:** And then maybe even get into some of kind of what it looks like in the product itself.

**Hasit Mistry:** Sure.

**Hasit Mistry:** Yeah, I can do that.

**Hasit Mistry:** I spoke to Amanda yesterday about this, and she said, just get some time with the growthx team so you can talk about the product.

**Hasit Mistry:** So I'm happy to do that.

**Hasit Mistry:** I'm Hasit, just you have the background.

**Hasit Mistry:** I'm one of the founding engineers at CodeRabbit.

**Hasit Mistry:** I'm also leading the enterprise engineering side of things at CodeRabbit now.

**Hasit Mistry:** So building a team, serving large enterprise customers as well.

**Hasit Mistry:** And at any point, just stop me and ask me questions.

**Hasit Mistry:** I don't know.

**Hasit Mistry:** I don't have a structure for this.

**Hasit Mistry:** Do you want to go through like a normal demo that I do with customers, or how do you want to do this?

**Erik O'Brien:** Yeah, a normal demo would be perfect.

**Hasit Mistry:** Okay.

**Hasit Mistry:** All right.

**Hasit Mistry:** So let me just, I have some links bookmarked.

**Hasit Mistry:** Let me do this.

**Hasit Mistry:** All right, so I'm sharing my screen.

**Hasit Mistry:** Can you see it?

**Hasit Mistry:** Yep.

**Hasit Mistry:** Okay, so this is, so just for background, CodeRabbit is a code review tool.

**Hasit Mistry:** It is grown to be a lot more than a code review tool now.

**Hasit Mistry:** But the bread and butter of what CodeRabbit does is it automates your code review process.

**Hasit Mistry:** So from the time that you write your code to the time that you open a pull request in GitHub or any other Git providers, so there's GitHub, GitLab, Azure DevOps, Bitbucket.

**Hasit Mistry:** tool tool tool tool

**Hasit Mistry:** We support all of these.

**Hasit Mistry:** You open the pull request.

**Hasit Mistry:** Pull request means, I don't know how familiar you are and how detailed you want me to be with this process.

**Erik O'Brien:** Yeah, just do it like you normally would.

**Erik O'Brien:** I would say I'm not a developer.

**Hasit Mistry:** know enough to be dangerous, but.

**Hasit Mistry:** Okay, got it.

**Hasit Mistry:** So I mean, I'll use the simpler terms, at least the terms that would not be to do in depth.

**Hasit Mistry:** pull request is something that we commonly use in the development world to show changes made to the code.

**Hasit Mistry:** So at any point in time we make changes to the code, we need it to be reviewed by fellow developers or seniors on the team.

**Hasit Mistry:** So a pull request essentially allows for that review to happen.

**Hasit Mistry:** It's a place where reviews happen.

**Hasit Mistry:** All of these platforms, GitHub, GitLab, they have a concept of a pull request.

**Hasit Mistry:** They would call it different things, but.

**Hasit Mistry:** But.

**Hasit Mistry:** It's a pull request, right here.

**Hasit Mistry:** So there's a tab right here, pull request.

**Hasit Mistry:** You open a pull request, you then add reviewers over here, and you essentially let the reviewers know that, hey, please review my code, and you can leave comments on the code.

**Hasit Mistry:** So now what happens is I look at the comments as a developer, as an author of this pull request.

**Hasit Mistry:** I go back to my editor, I make these changes, and then I push a change again on top of it to address their comments.

**Hasit Mistry:** It's similar to a document editing workflow, right?

**Hasit Mistry:** Like you would write a document, you would pass it to someone to review it, and go back and forth.

**Hasit Mistry:** So CodeRabbit is free for open source users.

**Hasit Mistry:** So GitHub has a large community of open source users.

**Hasit Mistry:** One of our initial go-to-market strategies was to keep it free for open source users because it drives adoption, and it spreads the word.

**Hasit Mistry:** In the open source communities, there are some extremely large open source projects currently using CodeRabbit because of that exact reason.

**Hasit Mistry:** It's free and easy to use.

**Hasit Mistry:** All right.

**Hasit Mistry:** So background aside now, what does CodeRabbit do and what does it look like?

**Hasit Mistry:** So as soon as you open a pull request in GitHub or any of these platforms that I mentioned, CodeRabbit will, first of all, start summarizing your pull request, your changes.

**Hasit Mistry:** So think about it as a description, like a high level description of what is changed in this, in this pull request, right?

**Hasit Mistry:** The first comment that CodeRabbit makes is a walkthrough comment.

**Hasit Mistry:** This is more like a technical summary.

**Hasit Mistry:** So this is like, okay, what files changed and what changed in those files?

**Hasit Mistry:** We built this entire technical summary.

**Hasit Mistry:** I was on a call with a customer and they said, oh, so this is more like a map, right?

**Hasit Mistry:** Like, this is like a map of .

**Hasit Mistry:** Inks that I need to look at as a human reviewer, and that made sense, like that stuck in my head, and I always use it with other customers.

**Hasit Mistry:** So if you go through this walkthrough, you as a human reviewer that comes in after CodeRabbit is done reviewing your code, you know what to look at.

**Hasit Mistry:** You know what is important.

**Hasit Mistry:** So it can track issues.

**Hasit Mistry:** There's a cute little poem that we give out.

**Hasit Mistry:** is a fun thing.

**Hasit Mistry:** You can turn this off.

**Hasit Mistry:** There is another...

**Hasit Mistry:** I'm trying to find one second.

**Hasit Mistry:** Repeat this one.

**Hasit Mistry:** Yeah, so we can also generate diagrams of changes.

**Hasit Mistry:** So in the walkthrough comments, if there is like a large change in flow happening in the code, we can generate a diagram to represent that.

**Hasit Mistry:** This is also people...

**Hasit Mistry:** I find this very helpful.

**Hasit Mistry:** All right, so let's look at the bread and butter of CodeRabbit.

**Hasit Mistry:** This is what a review looks like.

**Hasit Mistry:** CodeRabbit not only understands the context of the function that are like what is being reviewed, but it also gives you a description of what you need to change.

**Hasit Mistry:** So here, 400 is the wrong status code.

**Hasit Mistry:** It's CodeRabit suggesting use 404, not just that, it's also giving you a committable suggestion.

**Hasit Mistry:** So you as an author of the pull request can actually commit these changes directly from here.

**Hasit Mistry:** You can just literally copy paste this, take it to your editor, and this would mean you've implemented the change.

**Hasit Mistry:** It makes it very easy for users.

**Hasit Mistry:** You get a glimpse of the interaction with CodeRabbit here.

**Hasit Mistry:** So this is also possible.

**Hasit Mistry:** You can chat with a bot.

**Hasit Mistry:** I'll show you a few more.

**Hasit Mistry:** I'll

**Hasit Mistry:** So without going into the code changes here, what it is, the author actually looked at this code and suggestion and said, okay, just create an issue for me, I'll handle it later.

**Hasit Mistry:** So this is the agentic side of CodeRabbit.

**Hasit Mistry:** CodeRabbit also has a way to take commands or rather instructions from you and act on your behalf.

**Hasit Mistry:** So it actually created an issue right here with these changes in the description of the issue.

**Hasit Mistry:** So like you can go back to it, you can keep track of it and then implement it some other time, right?

**Hasit Mistry:** These are things that are possible.

**Hasit Mistry:** You can also work with a bot to like improve the suggestion.

**Hasit Mistry:** So if bot gave you some suggestion, you can chat with it like you would do with a human.

**Hasit Mistry:** And you can ask it to like find out more information from different parts of your code.

**Hasit Mistry:** You can ask it, hey, can you.

**Hasit Mistry:** Do this.

**Hasit Mistry:** Where is this used?

**Hasit Mistry:** And it can do the analysis for you and reply with a lot of information.

**Hasit Mistry:** It can even tell you what scripts it ran to come to that conclusion.

**Hasit Mistry:** Any questions so far?

**Hasit Mistry:** All good so far?

**Hasit Mistry:** All good so far.

**Hasit Mistry:** Yep.

**Hasit Mistry:** All right.

**Hasit Mistry:** Okay.

**Hasit Mistry:** Let's see what this is.

**Hasit Mistry:** Yeah.

**Hasit Mistry:** This is another example of just the user pushing back on the suggestion.

**Hasit Mistry:** Like, okay, hey, that makes sense, but blah, blah, blah.

**Hasit Mistry:** So the bot is then, okay, here's an improved suggestion.

**Hasit Mistry:** So then they eventually fixed it going forward.

**Hasit Mistry:** So this pushback helped in improving CodeRabbit's suggestion.

**Hasit Mistry:** Let's see.

**Hasit Mistry:** What else?

**Erik O'Brien:** And does it learn over time, kind of your preferences for that?

**Erik O'Brien:** Yes.

**Hasit Mistry:** So I'm about to show you something around that as well.

**Hasit Mistry:** So that is a feature that we call learnings.

**Hasit Mistry:** We'll right back.

**Hasit Mistry:** So when you chat with a bot, CodeRabbit maintains learnings about you, about this repository in GitHub, and about this project, with some metadata around it, and it recalls it whenever it needs to do the review again in a similar situation.

**Hasit Mistry:** So at some point, details aside, but in some point, the authors would have said that if you see more than a few of the same kinds, like same packages of imports, suggest a star import.

**Hasit Mistry:** Star just means all in most languages.

**Hasit Mistry:** So CodeRabbit did that, exactly that, in this pull request.

**Hasit Mistry:** But for some reason, the author is like, okay, no, we changed that.

**Hasit Mistry:** We don't want to do that anymore.

**Hasit Mistry:** Can you get rid of star import?

**Hasit Mistry:** This is called a star import.

**Hasit Mistry:** So CodeRabbit, recall the old learnings, and you can actually read the learning right there.

**Hasit Mistry:** It's literally a natural language sentence.

**Hasit Mistry:** It says, It says,

**Hasit Mistry:** The team agreed that more than four imports justifies the use of a star import.

**Hasit Mistry:** It removed those old learnings and it added a new one saying now they prefer to not use wildcard imports.

**Hasit Mistry:** So now the bot is learning over time about your preferences and how you like to write code.

**Hasit Mistry:** And this is updated in real time.

**Hasit Mistry:** All you have to do is chat with the bot.

**Hasit Mistry:** It updates these learnings in real time.

**Hasit Mistry:** You can also manage them on the web portal.

**Hasit Mistry:** We have a web UI where you can go look at the learnings that were generated, edit them, or delete them.

**Hasit Mistry:** That is also possible.

**Hasit Mistry:** All right, let's look at another example.

**Hasit Mistry:** So back to the agentic side of things, CodeRabbit has this ability to agentically generate documentation around your code.

**Hasit Mistry:** Developers are a breed that hate writing documentation.

**Hasit Mistry:** We absolutely, that's like one of the things that we, we, we.

**Hasit Mistry:** We.

**Hasit Mistry:** He put off as much as we can, right?

**Hasit Mistry:** So there's this feature in CodeRabbit that there's a single click of a button, there's a check mark on your walkthrough, you see.

**Hasit Mistry:** You press that, CodeRabbit opens.

**Hasit Mistry:** Similarly, how this pull request is, right?

**Hasit Mistry:** I think it was a concept of pull request.

**Hasit Mistry:** CodeRabbit now opens a pull request on your behalf.

**Hasit Mistry:** So it writes the documentation for you, and this is what it looks like.

**Hasit Mistry:** This is all code generated documentation from CodeRabbit.

**Hasit Mistry:** So at this point, you can merge it in your code or edit it and then merge it.

**Hasit Mistry:** It's up to you.

**Hasit Mistry:** But it gives you a great starting point for filled-in documentation.

**Hasit Mistry:** There's a new feature that we had recently added called web search.

**Hasit Mistry:** So because a lot of these reviews that we do, the back end of that is still LLM technology, right?

**Hasit Mistry:** We use LLM for doing reviews.

**Hasit Mistry:** But most LLM models have cut off.

**Hasit Mistry:** reviews.

**Hasit Mistry:** LLM.

**Hasit Mistry:** We use

**Hasit Mistry:** At least today or sometime in the past.

**Hasit Mistry:** So they wouldn't know the state of the world that is more recent.

**Hasit Mistry:** So how do you update the knowledge of an LLM model in real time?

**Hasit Mistry:** That was the question that came up again and again.

**Hasit Mistry:** So we added the web search capability to CodeRabbit.

**Hasit Mistry:** What happens is at any point of time, using the agentic chat that I showed you, you can chat with it and ask it to update its knowledge.

**Hasit Mistry:** Or sometimes if CodeRabbit thinks that, okay, I do not know enough about this, it preemptively does a web search on its own and presents its results.

**Hasit Mistry:** So I'll show you an example of that.

**Hasit Mistry:** Some drastic example, even I cannot read it, but I can just walk you through what is happening here.

**Hasit Mistry:** So CodeRabbit suggested a change in the code for some locking mechanism that the user made.

**Hasit Mistry:** Does it say?

**Hasit Mistry:** Valid, but it depends if some other condition, and said, okay, we are thinking of using this other locking mechanism.

**Hasit Mistry:** So CodeRabbit did an analysis on that new locking mechanism.

**Hasit Mistry:** It even cited what websites it referred to, and then had a discussion with the user at the end.

**Hasit Mistry:** So like, okay, here it has some improvements, blah, blah, blah, and then added learning at the end.

**Hasit Mistry:** So this is how CodeRabbit updates its own knowledge, even if the model might not know about it.

**Hasit Mistry:** The LLM model might not know about this.

**Hasit Mistry:** Here's a fun example.

**Hasit Mistry:** So this is some Minecraft developer.

**Hasit Mistry:** The author added some lighting properties of a block.

**Hasit Mistry:** And I don't exactly know what's happening here, but I can guess from what CodeRabbit suggested that it thought that the lighting properties...

**Hasit Mistry:** ...

**Hasit Mistry:** of a side shifting plates was wrong.

**Hasit Mistry:** So it suggested you remove these two lines and add these, right?

**Hasit Mistry:** But the author's like, no, here's your Wiki link.

**Hasit Mistry:** I read it over there and that has the most latest information.

**Hasit Mistry:** Can you refer to that?

**Hasit Mistry:** So CodeRabbit did exactly that, right?

**Hasit Mistry:** So it went through that link.

**Hasit Mistry:** It went through even more links than just that.

**Hasit Mistry:** And then it said, no, author, you are right.

**Hasit Mistry:** The changes you made were correct at the end and then added a learning.

**Hasit Mistry:** So this is so much more dynamic.

**Hasit Mistry:** This is almost like having a senior reviewer on your team who knows a lot more about many things.

**Hasit Mistry:** And it's always on.

**Hasit Mistry:** There's never a time where you have to wait for a review.

**Hasit Mistry:** The reality of development is that teams are distributed in the world.

**Hasit Mistry:** But if I open a pull request today and I want it to be reviewed, some.

**Hasit Mistry:** soon.

**Hasit Mistry:** Other people want

**Hasit Mistry:** Sometimes I get a review tomorrow.

**Hasit Mistry:** It naturally adds a delay of a day, but CodeRabbit is always on.

**Hasit Mistry:** It's going to give me a review in the next 10 minutes.

**Hasit Mistry:** It's automatic.

**Hasit Mistry:** I don't even have to trigger it.

**Hasit Mistry:** So yeah, this, and we're adding a bunch more features, but I don't want to go into that much detail because it would be a lot more technical, but I hope this was helpful.

**Hasit Mistry:** Yeah, absolutely.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Is there any kind of issues that CodeRabbit doesn't detect?

**Erik O'Brien:** Like, looks like bugs in style, security stuff, but like any logical correctness or anti-patterns or?

**Erik O'Brien:** It does actually.

**Hasit Mistry:** There's, we categorize these comments into logical errors, security issues, refactor comments, or even like stylistic ones, like nitpicky ones.

**Hasit Mistry:** So we do detect the whole range of issues.

**Hasit Mistry:** So

**Hasit Mistry:** It could be like best practices also, it could be a simple G factor, like, hey, let's make it a little more efficient, right?

**Hasit Mistry:** Like, this is how you do it.

**Hasit Mistry:** So, yeah.

**Erik O'Brien:** One question I had was in the agentic chat, but I think answered most of that through learnings.

**Erik O'Brien:** Is there any languages or frameworks that you guys don't support currently?

**Hasit Mistry:** No, we are agnostic of languages.

**Hasit Mistry:** Because we use frontier models from both OpenAI and Anthropic, whatever they are trained on, we benefit from that.

**Hasit Mistry:** Plus, we have this whole deterministic side of CodeRabbit that runs tools on the code of the put request.

**Hasit Mistry:** So, that is...

**Hasit Mistry:** It's more deterministic, and that depends on the kind of tools we have.

**Hasit Mistry:** But that also helps detect a lot of static analysis issues, security, vulnerabilities.

**Hasit Mistry:** And then we not only post that issue, but we also give you a fix for it.

**Hasit Mistry:** So imagine you as a developer were by mistake leaking a secret, like some web secret that was not meant to be in the code.

**Hasit Mistry:** CodeRabbit can actually catch that, detect it, and point it out in your pull request.

**Hasit Mistry:** Like, hey, you shouldn't be doing this.

**Hasit Mistry:** Please remove it.

**Erik O'Brien:** If a team already has, like, coding guidelines or style rules, are they able to kind of just upload those right when they start using it?

**Hasit Mistry:** Yeah.

**Hasit Mistry:** Let me show you what that looks like.

**Hasit Mistry:** This is a good time to go into the config, and I'll show you how to do that.

**Hasit Mistry:** So, first of all, you can configure CodeRabbit at the org level, or you can do it at...

**Hasit Mistry:** Each project level as well, right?

**Hasit Mistry:** So what I'm going to show you is some project config, but like assume the same thing is possible at the org level as well.

**Hasit Mistry:** So there's a few ways you can do that.

**Hasit Mistry:** There's something called path instruction.

**Hasit Mistry:** So you can give it some path.

**Hasit Mistry:** Say, for example, if you want it for all JavaScript files in your project, and then you can start writing some instructions for it.

**Hasit Mistry:** Right?

**Hasit Mistry:** So this would be one way to do it.

**Hasit Mistry:** The second way you could do it is, of course, learnings.

**Hasit Mistry:** I showed you that.

**Hasit Mistry:** That is more dynamic.

**Hasit Mistry:** That is when you chat with it, it would learn.

**Hasit Mistry:** But that's more, I think of learnings as more like a little note, like a sticky note on your desk that you keep.

**Hasit Mistry:** You write it down, you recall it, you look at it, and then throw it away.

**Hasit Mistry:** Whereas instructions are more like you storing it away for long-term memory.

**Hasit Mistry:** You're always going to recall it.

**Hasit Mistry:** It's more

**Hasit Mistry:** Or like a proper book that you keep, and you're writing it down, notes in it.

**Hasit Mistry:** The third way I think about a more long-term and a more ever-evolving way is the code guidelines.

**Hasit Mistry:** So there are other tools, like I'm sure you've heard of Cloud Code and Gemini and Cursor.

**Hasit Mistry:** All of these tools allow you to write certain rules and guidelines.

**Hasit Mistry:** Because that is how you would provide extra context about your project to these tools.

**Hasit Mistry:** So people have already well-written documentation, MD files, Markdown files, text files, and they exist in their project already by default.

**Hasit Mistry:** So we had an idea, like why don't we just take that and just spec that and build path instructions from it.

**Hasit Mistry:** So we look at all these files by default.

**Hasit Mistry:** But if you had custom instructions in some other file, like, for example, Hasit.txt, or like, whatever, Erik.md, fine, you can add these, that's fine.

**Hasit Mistry:** You can provide custom files as well.

**Hasit Mistry:** So this is more like a long-term, ever-evolving instruction set for CodeRabbit.

**Hasit Mistry:** Yep.

**Hasit Mistry:** And while we're here, I'll show you some external integrations we have as well, right?

**Hasit Mistry:** Usually developers organize their work in tickets.

**Hasit Mistry:** So we have these external systems of Cheetah, Linear.

**Hasit Mistry:** That is where you would write issues and tickets, right?

**Hasit Mistry:** So you form that first, and then you start working on that.

**Hasit Mistry:** So it's like a task.

**Hasit Mistry:** I don't know how guys I can explain it.

**Hasit Mistry:** So you can integrate with JIRA and linear within CodeRabbit, and in the pull request, for example, you can add a link to that ticket, saying, hey, this pull request addresses this ticket.

**Hasit Mistry:** So CodeRabbit can now go read that ticket, build objectives out of it, and tell you which objectives were met.

**Hasit Mistry:** This is helpful, again, as a map, right, like for the next fellow human reviewer to come in and see, oh, does this pull request actually adhere to what was planned?

**Hasit Mistry:** So these are external systems that we connect to.

**Hasit Mistry:** And this all feeds into a central context enrichment engine we have.

**Hasit Mistry:** We call it the context enrichment.

**Hasit Mistry:** But that is where all these extra pieces of information come together.

**Hasit Mistry:** We build a package and then.

**Hasit Mistry:** We send it to the LLM model for review.

**Hasit Mistry:** And MCPs are the new hot thing in this AI world right now.

**Hasit Mistry:** So we integrate with external NCP servers as well.

**Hasit Mistry:** So if you had a lot of knowledge in some external Notion project, right?

**Hasit Mistry:** Like people, a lot of development teams maintain text in Notion documents about the reasons behind why things are being done.

**Hasit Mistry:** So you can connect to Notion and when CodeRabbit is reviewing it, it's going to pull information from your Notion server in real time and add it to the context enrichment and then eventually send it out.

**Hasit Mistry:** So your context is that much more rich and your review will be that much more relevant instead of being some garbage.

**Hasit Mistry:** Yeah.

**Erik O'Brien:** Then how do you guys perform kind of at scale, like very large repos or very complex code, modern repos?

**Hasit Mistry:** Yeah, so one of the first things we do is we clone the entire project.

**Hasit Mistry:** Cloning is just downloading.

**Hasit Mistry:** It's a word that we use called clone where we take that project, download it to a local sandbox.

**Hasit Mistry:** So it's a secure environment.

**Hasit Mistry:** We call it a sandbox environment.

**Hasit Mistry:** That is where a lot of analysis happens on the code.

**Hasit Mistry:** So when we download that entire code base, we run tools on it.

**Hasit Mistry:** We build something called CodeGraph.

**Hasit Mistry:** That builds an understanding in CodeRabbit about who is calling what from different.

**Hasit Mistry:** The code side.

**Hasit Mistry:** So all of this goes into context enrichment as well.

**Hasit Mistry:** That means even in large monorepos, where people organize projects in different directories, we can, on our side, agentically probe into different parts of the project to gather more information.

**Hasit Mistry:** Gotcha.

**Erik O'Brien:** Any other kind of high-level features we should know about?

**Hasit Mistry:** Oh, yes.

**Hasit Mistry:** Actually, there's a lot of stuff in Flux.

**Hasit Mistry:** I can show you some things.

**Hasit Mistry:** Let me see if I can find an example of it.

**Hasit Mistry:** What the hell is here?

**Hasit Mistry:** Yeah.

**Hasit Mistry:** Something we recently released is a Prima check.

**Hasit Mistry:** So...

**Hasit Mistry:** So...

**Hasit Mistry:** A lot of teams have standards of how their pull request should look like, title should be of a certain format, the description has to be of a certain format, or like some tests have to be part of the code every time we make changes, right?

**Hasit Mistry:** So, we introduced this idea of a pre-merge check.

**Hasit Mistry:** So, before you merge your pull request, these are checks, these are a list of checks that need to pass before you're ready to merge.

**Hasit Mistry:** Think about it that way.

**Hasit Mistry:** So, we have a set of pre-merge checks already defined, and I can show you that list.

**Hasit Mistry:** Let's go to config.

**Hasit Mistry:** So, we have some pre-merge doctrine coverage, pull request title, description, issue assessment, you can mark it as a warning.

**Hasit Mistry:** or an error, or you can completely turn that check off.

**Hasit Mistry:** Sorry, I was here.

**Hasit Mistry:** Yes.

**Hasit Mistry:** Or you can even write your own custom pre-merge checks.

**Hasit Mistry:** So you can tell CodeRabbit what kind of check that CodeRabbit needs to do in order to, you know, okay or not okay this pull request.

**Hasit Mistry:** And here are some examples that we have a list of, you know, the pre-merge checks that we've added, how many fail, okay, two errors, four warnings, and four passed.

**Hasit Mistry:** So this gives an idea to the next fellow human reviewer, like, hey, should this, should I allow this PR to go forward or not?

**Hasit Mistry:** The finishing touches, it's good to see it because we spoke about it.

**Hasit Mistry:** This is how you would generate the doc strings.

**Hasit Mistry:** So you would, you click this button and CodeRabbit will automatically write documentation for you.

**Hasit Mistry:** Gotcha.

**Hasit Mistry:** Gotcha.

**Hasit Mistry:** And we show a lot of information about errors and whatnot on the pull request.

**Hasit Mistry:** So the main interface of a developer to CodeRabbit is this pull request.

**Hasit Mistry:** They don't go to the UI as much.

**Hasit Mistry:** They mainly live and breathe on this page that I'm showing you.

**Hasit Mistry:** Okay.

**Erik O'Brien:** And then I guess more generally, what have you heard from customers or kind of their favorite features?

**Erik O'Brien:** I think Amanda mentioned those sequence diagrams were one that like customers mentioned, but you guys probably wouldn't say that's one of the top features.

**Erik O'Brien:** Yeah.

**Hasit Mistry:** Yeah.

**Hasit Mistry:** It's a whole range of things, but...

**Hasit Mistry:** People actually, this top-level features, high-level features, I would say chat is amazing.

**Hasit Mistry:** People actually, when CodeRabbit leaves a comment, people, I do not think it would be this way, but people chat with the bot diligently.

**Hasit Mistry:** People reply to the bot as if it's like a fellow human reviewer, like, oh, this is garbage.

**Hasit Mistry:** No, I'm not doing this.

**Hasit Mistry:** Or like, oh, wow, that's a nice suggestion.

**Hasit Mistry:** Let me do this.

**Hasit Mistry:** You know, like, they would actually reply to a bot, which is amazing to me.

**Hasit Mistry:** So chat, I would say, is one of the top features.

**Hasit Mistry:** It's a very old feature, but people love that chat exists.

**Hasit Mistry:** A lot of our competitors do not have chat.

**Hasit Mistry:** Even GitHub Copilot, which is GitHub's own feature, that doesn't support chat.

**Hasit Mistry:** So we do that, and we do it well.

**Hasit Mistry:** We integrate this learnings into it.

**Hasit Mistry:** The agentic chat is in it.

**Hasit Mistry:** So it opens up a lot of different modes of interaction with CodeRabbit.

**Hasit Mistry:** I would say the Prima check has been doing well so far, but in full disclosure, we just added it like a few weeks back, like last week or two weeks ago.

**Hasit Mistry:** So I can't say for certain how well this is performing, but people seem to like it.

**Hasit Mistry:** They started using it.

**Hasit Mistry:** So we get that metrics and seems to be a well-loved feature.

**Hasit Mistry:** People also really enjoy the summary that is generated.

**Hasit Mistry:** I think this is the first thing they see on the pull request.

**Hasit Mistry:** And typically, developers used to write this by hand every single time they open a pull request.

**Hasit Mistry:** Now CodeRabbit generates this and it generates it well, like it does a good job at it, which is impressive.

**Hasit Mistry:** The walkthrough, I would say, is something that people complain a lot about because they say, oh, it's too noisy, it's giving me too much information.

**Hasit Mistry:** There's like a big wall of text in front of me.

**Hasit Mistry:** I don't want to see it.

**Hasit Mistry:** How do I turn it off?

**Hasit Mistry:** Poem is one of the most polarizing feature ever.

**Hasit Mistry:** People absolutely hate it or people absolutely love it.

**Hasit Mistry:** There's no in-between.

**Hasit Mistry:** I think people appreciate the fact that the review comments are less noisy in the fact that they are relevant.

**Hasit Mistry:** By noise, I mean they're not like completely away from what it is reviewing.

**Hasit Mistry:** So it's contextual and it gives you these committable suggestions.

**Hasit Mistry:** I think people really appreciate this part.

**Hasit Mistry:** So a lot of times I can just like copy paste this into my code and like that is the suggestion that CodeRabbit intended.

**Hasit Mistry:** We keep track of these metrics as well, so we understand how many people are accepting suggestions given by CodeRabbit, and that's been well-received.

**Hasit Mistry:** This is something we recently did.

**Hasit Mistry:** We were always doing the categorization of the problem, so it would say it's a potential error, is it a refactor comment, is it a security vulnerability, is a nitpick comment?

**Hasit Mistry:** But we started now giving it severity.

**Hasit Mistry:** So this is the type of the issue, and this is the severity of the issue.

**Hasit Mistry:** So if I'm going through a list of comments, I know which ones to address first.

**Hasit Mistry:** And apart from that, I think we've put in a lot of effort into reducing noise, reducing nitpicky comments.

**Hasit Mistry:** Like, you see, all the nitpicky comments are actually bunched up.

**Hasit Mistry:** together here so we don't we don't make a comment on it we just throw it away just in case if you want to go through that list yeah uh so people are being here that we use that that noise um we integrate a lot of tools as I mentioned so the output of the tool not only give we give you what the issue is but we give you a fix for it as well which is nice um yeah then who would you say like is your closest competitor right now i know amanda mentioned like reptiles graphite um bugbot who's kind of at the top of the list for at least like capability and uh performance i would say reptiles uh reptile has been especially because i'm in a lot of enterprise conversations uh reptiles name comes up a lot uh bugbot has been coming

**Hasit Mistry:** Up recently because it's a brand new product.

**Hasit Mistry:** People always want to try it.

**Hasit Mistry:** BugBot is by Kurser, if I believe.

**Hasit Mistry:** So people who already have Kurser licenses, they're bound to try that as well.

**Hasit Mistry:** Copilot is pretty much out of the picture.

**Hasit Mistry:** Like it's the review comments by Copilot are just so bad.

**Hasit Mistry:** They're so bad.

**Hasit Mistry:** They're like, they're out of context and sometimes not as detailed.

**Hasit Mistry:** So Creptide would be my answer to the closest, like the top most competitive.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** And then would you say, like, what would you say is kind of your, like, if you had to pick one biggest unique differentiation or moat that CodeRabbit has?

**Erik O'Brien:** The biggest mod is that we...

**Hasit Mistry:** You can do all this at a $20 price.

**Hasit Mistry:** This is one of the, there's a lot of engineering that goes behind this because LLM costs are not cheap.

**Hasit Mistry:** A lot of our competitors charge by usage, which doesn't hold up.

**Hasit Mistry:** We charge by seat, per seat pricing.

**Hasit Mistry:** So if you open a pull request, you are one seat.

**Hasit Mistry:** And the engineering, the quirky things that we do on the back end is how do we manage where the call goes?

**Hasit Mistry:** Like what model do we pick for the task?

**Hasit Mistry:** All of that helps in reducing the cost overall.

**Hasit Mistry:** More complex tasks go to more larger and more comprehensive models.

**Hasit Mistry:** Smaller tasks, like for example, the summary that I showed you is done by a smaller model.

**Hasit Mistry:** So that's how we manage the.

**Hasit Mistry:** The other thing is, the context building that we do is quite comprehensive.

**Hasit Mistry:** That is something that our competitors haven't matched yet.

**Hasit Mistry:** This is because we've added a lot of external configurations.

**Hasit Mistry:** We can, in a secure manner, clone their code, probe into different parts of the code, build that context, and then send it to LLM, versus only looking at the disk, right?

**Hasit Mistry:** Like, what has changed?

**Hasit Mistry:** That's not the only thing we look at.

**Hasit Mistry:** So that's also a big differentiator compared to our competitors.

**Erik O'Brien:** So mainly price and points of context.

**Erik O'Brien:** Yes.

**Erik O'Brien:** I mean, yes.

**Hasit Mistry:** The context, I would say, would be the biggest one in the price.

**Hasit Mistry:** The engineering makes the price happen, right?

**Hasit Mistry:** It enables us to cost so less because we do well on management of the LM calls.

**Erik O'Brien:** Yeah, because you guys, the revenue model is completely different than competitors.

**Erik O'Brien:** Yes.

**Erik O'Brien:** Yeah.

**Hasit Mistry:** Wonderful.

**Erik O'Brien:** Those are the big questions I had.

**Erik O'Brien:** Is there anything else you feel like I should know?

**Erik O'Brien:** Any other parts of the product that we didn't cover?

**Hasit Mistry:** Yeah, there's a lot.

**Hasit Mistry:** I'm sure I'm missing something.

**Hasit Mistry:** Like reports, didn't even touch on reports, but it's fine.

**Hasit Mistry:** We have dashboards.

**Hasit Mistry:** We show the usage of CodeRabbit to justify the ROI.

**Hasit Mistry:** Because oftentimes the people trying it and making the case for CodeRabbit are different from the people who are in charge of making the decision of buying the code, of buying the tool.

**Hasit Mistry:** So, So,

**Hasit Mistry:** So dashboards like this help to make that case.

**Hasit Mistry:** And then there's subscription page.

**Erik O'Brien:** A lot of open source users then kind of go back to work and they're like, I need the same thing I was using on the open source project.

**Erik O'Brien:** And then they tap their manager to be like, hey, we need to go buy this.

**Erik O'Brien:** Exactly.

**Hasit Mistry:** Right.

**Hasit Mistry:** So that was our early GTM motion, right?

**Hasit Mistry:** Our entire motion was based around ground up, open source adoption, people using it on their open source projects and then going back to their companies and like, hey, why don't we use this?

**Hasit Mistry:** It's a good tool.

**Hasit Mistry:** But at that point, these conversations come up like, why should I pay $20?

**Hasit Mistry:** Like, what is the case for it?

**Hasit Mistry:** How do you make the case for it?

**Hasit Mistry:** Because at the end of the day, a budget has to be allocated for it.

**Hasit Mistry:** So all of that is possible using the dashboard metrics.

**Hasit Mistry:** You can manage feeds very easily.

**Hasit Mistry:** That's another thing we've worked on.

**Hasit Mistry:** This is the per-seat pricing that I was talking about.

**Hasit Mistry:** So you as an organization purchase seats, and then you enable it for the people on your organization.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Awesome, well, yeah, nothing else that comes to mind.

**Erik O'Brien:** I think I've got enough to at least build a, we kind of build these feature matrices that are artifacts that go into our content generation system.

**Erik O'Brien:** So I've got enough to go off of, but if any other questions come up, I might ping you or Amanda and just get a question to go through.

**Erik O'Brien:** But appreciate the time and happy to give you 20 minutes back in your Friday.

**Hasit Mistry:** Awesome.

**Hasit Mistry:** Have a good weekend, man.

**Hasit Mistry:** All right, you too.

**Erik O'Brien:** See ya.

**Erik O'Brien:** All right.

**Erik O'Brien:** Thank
