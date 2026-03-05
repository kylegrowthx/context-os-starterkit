# Augment Code Technical Deep Dive

<metadata>
date: 2025-06-06
time: 20:00 UTC
duration: 35 minutes
organizer: George Haikal (GrowthX)
participants: Anshuman Pandey (Augment), Kirkland Gee (GrowthX), George Haikal (GrowthX)
fathom_recording_id: 67052750
fathom_url: https://fathom.video/calls/318568869
share_url: https://fathom.video/share/4St6Exr2kwn23-z3xkQxjb5po6KLuToe
source: fathom
enriched_on: 2025-03-03 14:30 UTC
</metadata>

---

## Summary

George and Kirkland from GrowthX conducted a technical deep dive with Anshuman Pandey, Solutions Architect at Augment Code, exploring the platform's enterprise-grade architecture and key differentiators. Augment differentiates through its proprietary context engine that understands code shape and interdependencies, hyper-scale real-time indexing (handling 400k-500k files simultaneously), and intelligent multi-model routing across 6+ models—positioning it for complex enterprise use cases like database migrations, language upgrades, and large-codebase onboarding rather than quick prototyping. The team identified key value drivers for content strategy: solving enterprise pain points (onboarding timelines, code quality, testing, infrastructure-as-code, PR reviews) and highlighting concrete outcomes like a Spring Boot version upgrade completed in 2 hours instead of 3-4 weeks.

---

## Context

Augment Code is a GCP-based coding assistant founded two years ago by a team of enterprise-experienced engineers (including a CEO with four IPOs). The company competes with Cursor, Windsurf, and GitHub Copilot but targets large enterprises with complex codebases rather than individual developers. GrowthX connected with Augment's head of research, Sill, through CEO Marcel's existing network (CMO breakfasts and marketing communities) and kicked off a growth awareness engagement last week. This technical deep dive was part of GrowthX's content strategy work—Kirkland Gee has been testing Augment on a project for 24+ hours alongside Cursor, and George is conducting user interviews to understand positioning and differentiation. The goal is to identify concrete, enterprise-specific pain points and use cases that resonate with GrowthX's content and GTM strategy.

---

## Relevance

**To GrowthX Delivery:**
- Enterprise AI for code is an emerging GTM vertical: Augment's positioning around SDLC-wide coverage (not just IDE completion) suggests content opportunities for infrastructure-as-code, migrations, and PR reviews—beyond typical "AI pair programmer" messaging.
- Differentiation narrative focus: Kirkland's insight about "cursor rules" being proprietary framing suggests GrowthX can help Augment position their context engine and multi-model routing as technical advantages in content, not just marketing language.
- Client interview insights: Anshuman's examples (Spring Boot upgrade 2 hours vs. 3-4 weeks; onboarding timelines; test-case generation) provide concrete metrics and use cases to anchor content strategy around ROI and efficiency gains.

**To GrowthX Business Development:**
- Account expansion signal: Team's investment in this deep dive (George's user interviews, Kirkland's hands-on product testing) suggests Augment is a strategic account for larger GTM/content engagement.
- Reference potential: Kirkland's positive user experience ("intuitive," "comfortable," "don't feel like I'm missing anything") after 24+ hours of real product use indicates early-stage reference potential once content deliverables ship.
- Messaging clarity gap: Discussion of niche language support (COBOL, Fortran) and roadmap items (dynamic webhooks, SDLC workflow integration) reveals where Augment's story needs sharpening—GrowthX can help clarify "what we're not" to strengthen positioning.

**To CheckThat:**
- Emerging AI code quality problem: Anshuman's core differentiation (context engine understanding code shape, not treating as flat text) overlaps with visibility/indexing—potential AEO research angle around how AI coding tools impact code search and discoverability.

---

## Overview

- Augment focuses on enterprise-grade coding assistance, emphasizing large, complex codebases and full SDLC support
- Key differentiators: hyper-scale real-time indexing, proprietary context engine, multi-model routing, and remote agents
- Future direction: Expanding beyond IDE to become a comprehensive coding awareness platform across the entire SDLC

---

## Key Topics

### Augment's Technical Architecture

  - Full GCP stack built as a proper SaaS offering, not limited to local machine storage
  - Hyper-scale real-time index capable of handling 400k-500k files simultaneously
  - Proprietary context engine understands code shape, interdependencies, and nuances
  - Multi-model routing system using 6+ models (proprietary and open-source) for different tasks

### Key Features and Differentiators

  - Native integrations with JetBrains, VS Code, Vim, and terminal
  - Agent mode with auto and manual options, task lists, and parallel processing
  - Remote agents for cloud-based code execution and PR reviews
  - Augment Memories for persistent context across agent threads
  - Prompt enhancer to improve user input quality

### Security and Compliance

  - SOC 2 Type 2 and ISO 42001 certified
  - Customer-managed encryption keys and proof-of-possession architecture
  - No training on customer data or code to prevent IP leakage and data pollution

### Future Roadmap and Vision

  - Expanding beyond individual developers to support entire SDLC
  - Potential for business logic to code translation
  - Dynamic deployments with event listeners and webhooks for continuous agent processes
  - Aiming to become the de facto coding awareness platform across the SDLC

### Target Audience and Use Cases

  - Organizations with 100-5,000 developers
  - Expanding value to non-developers (e.g., product managers, marketers) interacting with code
  - Solving complex enterprise challenges like onboarding, large migrations, and code upgrades

---

## Action Items

**Anshuman Pandey (Augment)**
- Send detailed materials (slides/docs) on Augment features/differentiators to George Haikal

---

## Transcript
**George Haikal:** Good, man.

**George Haikal:** Busy, busy, but it's better than the alternative.

**George Haikal:** Yep.

**Kirkland Gee:** Yeah, I get it.

**George Haikal:** Did you have some time to play around?

**George Haikal:** You've already used Augment, right?

**Kirkland Gee:** I've been using it for the last 24 hours, it feels like, maybe a little longer, basically to build out a lot of this whole project.

**Kirkland Gee:** So, it's great.

**Kirkland Gee:** I mean, from a user experience, it's very similar to using something like Cursor or any of the other, I mean, they're all AI coding agents.

**Kirkland Gee:** So I'm curious just to talk to them more and understand, like, what the real differentiators are.

**Kirkland Gee:** I mean, I know their kind of selling point is we do more on larger code bases, but it'll be good to just chat with them a little bit.

**Kirkland Gee:** But I feel good, like, I understand most of how it works.

**George Haikal:** Love it.

**George Haikal:** Yeah, it's super interesting because I've been doing user interviews with their head of research, too. I mean, you're one of their users, right?

**George Haikal:** It's someone who's like a level above a vibe coder, essentially, at least a level above, right?

**George Haikal:** It varies, but the switching cost is so low for these tools because it takes a couple clicks to get a new one plugged in.

**Kirkland Gee:** I'm using Augment in Cursor, right?

**Kirkland Gee:** That's what's so funny is, you know.

**George Haikal:** Did you see a $900 million raise?

**Kirkland Gee:** Do what?

**George Haikal:** Cursor's $900 million raise.

**Kirkland Gee:** Yeah, I did see that.

**George Haikal:** Oh, my God.

**Kirkland Gee:** It's crazy.

**Kirkland Gee:** Cursor gets a $9 billion valuation in like two weeks.

**Kirkland Gee:** That's crazy.

**George Haikal:** Good for Augment. Hopefully, people get a little FOMO.

**George Haikal:** How are you doing, Anshuman? Thanks for joining.

**Anshuman Pandey:** Yeah, no worries. How do you guys know Sill? What's the background there?

**George Haikal:** Yeah, so Marcel, our CEO, and Sill go back a year, maybe a little longer.

**George Haikal:** They've been part of the same CMO breakfasts and in the same marketing communities, so that's how they initially met.

**George Haikal:** And then here at GrowthX, Sill reached out because he wanted, you know, to grow awareness for the product.

**George Haikal:** And the relationship was already there.

**George Haikal:** So now last week, we kicked off trying to figure out every single way possible that we can help drive awareness to augment for you all.

**Anshuman Pandey:** Cool.

**Anshuman Pandey:** Cool.

**Anshuman Pandey:** Just a bit of background on me.

**Anshuman Pandey:** So Anshuman, I'm the third solutions architect.

**Anshuman Pandey:** I joined the team, probably the sixth person on the go-to-market team, so joined back in September.

**Anshuman Pandey:** Started off my career as a full-stack developer, then I was at Palo Alto Networks, where I was doing some solutions consulting for their strategic accounts, so I covered like Intel, Oracle, and Meta, and then decided to screw it, let's do the whole startup thing in Silicon Valley.

**Anshuman Pandey:** And yeah, been here since September.

**George Haikal:** Nice, man.

**George Haikal:** Really, you guys have been great to work with so far, and we're excited for what we have planned.

**George Haikal:** And I guess now I'll let Kirkland kind of take over.

**George Haikal:** Marisol, please feel free to jump in as well, just to kind of, we want to better understand, you know, the differences of Augment, what you think you all do better.

**George Haikal:** Kirkland's become an expert quickly on the product, and so just as much as we can learn technically in this session, it's going to be great because it informs all of the different avenues, content, et cetera, that we want to create for you guys in terms of growth and strategy, so.

**Kirkland Gee:** Expert might be a stretch, but yeah, so I, you know, I'm familiar with Augment, I've seen a lot of the influencer.

**Kirkland Gee:** Ads with people like Theo Brown and other guys on YouTube and that sort of thing.

**Kirkland Gee:** I've been using Cursor for like a year and a half-ish, and I decided we're doing this kind of whole project to spin up this website as a potential lead magnet for you guys and just playing around some ideas.

**Kirkland Gee:** So I've been using Augment to do all of that on a free trial, just to like sort of get a feel for how the tool works.

**Kirkland Gee:** And, you know, as someone who's been doing this sort of coding work, it's very intuitive.

**Kirkland Gee:** It's very comfortable.

**Kirkland Gee:** Like, I don't feel like I'm missing anything.

**Kirkland Gee:** But I would be curious, you know, my perspective on this is like, one, thinking about what are the things that differentiate Augment.

**Kirkland Gee:** Obviously, like large code bases and large contacts seems to be like the marketing push, right, of what makes it different.

**Kirkland Gee:** I'd love to hear a little more about how that works.

**Kirkland Gee:** And then thinking about like how we're positioning content, what kinds of strategies we're going to go after.

**Kirkland Gee:** Like we want to do anything that we can do to make Augment as, you know, up front as possible.

**Kirkland Gee:** So as an example, what I do be playing around with is like, okay, do we do it?

**Kirkland Gee:** Directory with a ton of configurations for different AI coding environments, right?

**Kirkland Gee:** An alternative to cursor rules.

**Kirkland Gee:** Like, is there a way to position that or talk about that that's more unique to augment or makes augment more featured versus, you know, obviously rules is kind of like a cursor thing, right?

**Kirkland Gee:** Like that term is very much capitalized on, even though it's essentially just a fancy system prompt that maybe gets rag called sometimes instead of just getting entirely pulled in.

**Kirkland Gee:** But that's a little context of where I come at this from.

**Anshuman Pandey:** Okay, cool.

**Anshuman Pandey:** Let's do a super high-level slideware that talks about differentiators and then can go into the product and talk through some differences as well.

**Anshuman Pandey:** But, yeah, I'm not going to make this very pitchy.

**Anshuman Pandey:** Just going to kind of go high level and you guys let me know where you want me to lead.

**Kirkland Gee:** Yeah.

**Anshuman Pandey:** Cool.

**Anshuman Pandey:** So when we're talking about differentiating, right, Ogden was founded, you know, two years ago, pre-chat GPT, with the people with a bunch of enterprise experience, right?

**Anshuman Pandey:** Right.

**Anshuman Pandey:** A lot of peer storage people, our CEO had four IPOs, and everyone who's working at Augment from the research side or the engineering side, the difference I would say is they're not just a bunch of, you know, super smart college, like this is our first dive into an enterprise and building a company.

**Anshuman Pandey:** Everyone's come from like your FANG, from your snowflakes and Databricks, so they've seen how to scale enterprises and they understand all the stuff that's necessary for enterprise coding specifically.

**Anshuman Pandey:** So when you look at how these first-gen AI for code tools like Cursor, Windsurf, GitHub Copilot are architected, they take your user prompt and they do some basic content gathering.

**Anshuman Pandey:** They'll do like a grep search, Cursor does Merkle trees, Windsurf does like AST, so essentially off-the-shelf algorithms where they think that, you know, context gathering with RAG and these basic algorithms is all you need.

**Anshuman Pandey:** And then they have the user...

**Anshuman Pandey:** The model that they want to use at the end, and they use the same prompt for whatever model, assume that it's going to incrementally give you a better output.

**Anshuman Pandey:** What we figured out is LLMs are great at generating output, but it's a garbage in, garbage out problem.

**Anshuman Pandey:** So we're focusing on the input layer, and this is how Augment was essentially architected.

**Anshuman Pandey:** So we're a full GCP stack built to be a proper SaaS offering.

**Anshuman Pandey:** We didn't fork the IDE, so we're not limited to storing embeddings on a machine, and it allows us to do a few things.

**Anshuman Pandey:** So one is, you know, developers don't have to switch their battle-hardened environments.

**Anshuman Pandey:** JetBrains, VS Code, and now Vim were supported as a plugin.

**Anshuman Pandey:** And because we built out this SaaS infrastructure, we can do a hyper-scale real-time index.

**Anshuman Pandey:** So some of our biggest customers, have about 400,000 500,000 files open in one workspace simultaneously.

**Anshuman Pandey:** And we actually re-indexed at every keystroke, and we're able to take all of

**Anshuman Pandey:** Files into context.

**Anshuman Pandey:** The crux of the entire operation is really this context engine.

**Anshuman Pandey:** This is what differentiates Augment for a few reasons.

**Anshuman Pandey:** So instead of doing those basic searches, we've built a host proprietary sort of secret sauce, you might call it.

**Anshuman Pandey:** And we don't treat code as flat text.

**Anshuman Pandey:** We understand that TypeScript is different from JavaScript, which is different from Java.

**Anshuman Pandey:** So, you know, for marketing terms, we understand the shape of code.

**Anshuman Pandey:** And because of that, we can look at things like interdependencies, nuances, your SQL, your schemas, your test cases, libraries.

**Anshuman Pandey:** And on top of that, there's no model picker as well, which you've seen, Kirkland.

**Anshuman Pandey:** That's not the developer's problem, right?

**Anshuman Pandey:** There's new models coming out all the time.

**Anshuman Pandey:** How are you supposed to keep that mental map of, if I'm doing Kotlin, I'm going use this thing, and then I need to figure out pricing?

**Anshuman Pandey:** What we actually do is we gather all the right data.

**Anshuman Pandey:** We gather all the right data, we're the quality prompt, and we route between multiple models depending on the task at hand.

**Anshuman Pandey:** So we actually have over half a dozen models.

**Anshuman Pandey:** Some are proprietary, some are open source, and there's Frontier that we fine-tune and post-train.

**Anshuman Pandey:** And so for completions, you want that snappiness and quickness in response, so we'll go through smaller models.

**Anshuman Pandey:** For chat, we have your more complex use cases, your architecture discussions.

**Anshuman Pandey:** We'll go through larger modalities to give you that verbosity and specificity in response.

**Anshuman Pandey:** Like NextEdit itself, there's three models that go through NextEdit.

**Anshuman Pandey:** There's like an inference model, there's a description generation model, and then there's the output model as well.

**Anshuman Pandey:** So we're going to do that intelligent routing and, you know, take the onus off the developer and let them do what they do best, which is coding.

**Anshuman Pandey:** This also applies to our agent mode.

**Anshuman Pandey:** So we have native integrations via OAuth, we have MCP support, and, you know, Cursor, when served, they have a nice little UX, which is why they forked the code, but we figured it out.

**Anshuman Pandey:** Like, now we integrate natively with the terminal and VS Code and JetBrains.

**Anshuman Pandey:** We can do web search, URL fetching.

**Anshuman Pandey:** And so we're kind of at par.

**Anshuman Pandey:** And the beauty of, you know, putting in all this work to do that SaaS infrastructure is the ability to do an actual platform play, right?

**Anshuman Pandey:** So when it comes to agents, there's this incorrect notion in the world where people think an agent will replace an entire part of the SDLC, like I'm going to have an agent for the create phase or the operate phase.

**Anshuman Pandey:** What we figured out is agents are really good at certain tasks in the SDLC.

**Anshuman Pandey:** Now, things like Cursor, Windsor, and Copilot, because they're limited to storing embeddings on a machine, they're a fork, all they can really do is this sort of, you know, create and test phase and plan phase.

**Anshuman Pandey:** Augment's set up to do phases across the entire SDLC because we can abstract that context engine.

**Anshuman Pandey:** So we have some customers we're playing around with having a sidecar for workspace context where they have an API.

**Anshuman Pandey:** We're thinking about, you know, having a merge review bot.

**Anshuman Pandey:** We're thinking about A2A protocols.

**Anshuman Pandey:** Because we built out this large infrastructure and we didn't do a fork and make everything hosted on the user machine, the goal is to do a full platform. This is kind of going in with our remote agents, right?

**Anshuman Pandey:** We have background agents where now they're running the cloud where we spin up the infrastructure outside of the user's machine.

**Anshuman Pandey:** And that lets us parallelize multiple different agents, right?

**Anshuman Pandey:** So you're controlling a fleet of agents, essentially.

**Anshuman Pandey:** I can turn off my laptop, grab a coffee, go to a meeting, go to sleep.

**Anshuman Pandey:** But the agents are just going to continuously work for me.

**Anshuman Pandey:** So that's kind of that first step into abstracting outside of the IDE and using that context engine to really expedite the whole SDLC.

**Anshuman Pandey:** A lot of blurbs of information.

**Anshuman Pandey:** So before we go into the product, any questions, anything I can clarify there?

**Kirkland Gee:** No, that all makes sense to me.

**Kirkland Gee:** And at this point with Augment, like obviously there's JetBrains, VS Code, Vim.

**Kirkland Gee:** Is there any sort of command line way to access it, or are you just using it as a plug-in in these other ecosystems?

**Anshuman Pandey:** Currently a plug-in.

**Anshuman Pandey:** We have a SlackBot integration as well.

**Anshuman Pandey:** We partnered with Glean to bring that Glean context inside of the IDE as well. No CLI or API exposed endpoint, but that's a super common request we get.

**Kirkland Gee:** Yeah, I'm just thinking about from the marketing perspective, right?

**Kirkland Gee:** What are we targeting?

**Kirkland Gee:** And at the end of the day, it's people that are going to use this in one of those.

**Kirkland Gee:** I saw a Chrome logo—you could just use this in the browser also?

**Anshuman Pandey:** So that's something we were beta testing. We're exploring a Chrome extension for PR reviews, but there's no formalized roadmap to be delivered, so I wouldn't harp on it too much.

**Kirkland Gee:** Yeah, okay.

**Kirkland Gee:** Yeah, that makes sense.

**Kirkland Gee:** I'm thinking about, like, for example, if we did a directory of MCP servers and we want to directly have an install button for JetBrains, VS Code, and Vim, that's all we need, right? Because that's what Augment is supported in.

**Anshuman Pandey:** Yep.

**Kirkland Gee:** Okay, cool.

**Anshuman Pandey:** I know you played around with the product, so I'm going to keep it pretty high level.

**Anshuman Pandey:** So extension, you know, we can index the entire workspace.

**Anshuman Pandey:** We can actually go in and you're not limited to just what you have in workspace, right?

**Anshuman Pandey:** So really common usage is this context tab, where I can actually go in and bring additional folders.

**Anshuman Pandey:** So I'm not limited to just what I'm looking inside VS Code.

**Anshuman Pandey:** I can bring in additional microservices.

**Anshuman Pandey:** Like if I have documentation, I can just add those folders to be indexed.

**Anshuman Pandey:** We have, you know, user guidelines, but we're actually bringing in the whole rules format as well, which can be selective per thread.

**Anshuman Pandey:** And then we have our native integrations.

**Anshuman Pandey:** So I think this is a really positive feature for a lot of enterprises, right?

**Anshuman Pandey:** A OAuth link to grab.

**Kirkland Gee:** Great. I already set up the Supabase one to get this site going, and it worked flawlessly.

**Kirkland Gee:** So, you know, my background was in marketing before coming into engineering and this sort of, like, weird AI GTM type stuff.

**Kirkland Gee:** And, like, MCP servers have historically just given me not a hard time, but they've just been, like, sort of fiddly and finicky from time to time.

**Kirkland Gee:** And so I think that, like, already set up made it super easy to just try it versus other times if I'm doing something small, like, well, I'll just figure it out myself.

**Kirkland Gee:** So, if it's working, it's great.

**Anshuman Pandey:** Yep.

**Anshuman Pandey:** So, data migrations, MCP, we integrate with the terminal itself, and we can actually select a specific shell.

**Anshuman Pandey:** So, if you have your environment set up in a certain way, just pick that to go.

**Anshuman Pandey:** So, yeah, that's kind of the whole setup scenario.

**Anshuman Pandey:** What other features?

**Anshuman Pandey:** So, I think agents and remote agents are kind of the, you know, big spiel of what we do.

**Anshuman Pandey:** So, we have agent auto, and we have agent manual.

**Anshuman Pandey:** So, run the tools automatically or don't.

**Anshuman Pandey:** So, we're working on logic, actually.

**Anshuman Pandey:** What a lot of people say is they're inside a chat thread and want to keep that context before they go to agent.

**Anshuman Pandey:** So we're working on that logic now where I can actually go in and switch from chat to agent.

**Anshuman Pandey:** I don't know if it's GA, but that's, you know, sort of what we're doing.

**Anshuman Pandey:** The other piece is a task list, right, where now instead of having the agent sort of go on its own, it can actually give a deep little task plan where I can go in and edit tasks.

**Anshuman Pandey:** The agent will start to smartly spin off remote agents to do these in parallel to really expedite the time to PR.

**Anshuman Pandey:** We have something different—Augment Memories. I don't know if you played around with memories at all.

**Anshuman Pandey:** Yeah, so similar to guidelines, but for the agent itself where I can give it specific details, the differentiator memories is the agent actually goes in and updates these automatically.

**Anshuman Pandey:** So you share that context between different agent threads.

**Anshuman Pandey:** You're not starting from scratch.

**Kirkland Gee:** And those augment memories, they're shared across any new agents you spin up.


**Anshuman Pandey:** Inside the workspace, yes, they're workspace specific.

**Kirkland Gee:** Yeah, obviously if I go, yeah, if I start a whole new thing, then no, but.

**Anshuman Pandey:** Yeah, yeah, multimodal support, I'm trying to think.

**Anshuman Pandey:** I have the prompt enhancer, which has been really useful for a lot of enterprises.

**Anshuman Pandey:** So we kind of expedite the whole adoption curve and enablement curve.

**Anshuman Pandey:** Have you played with the prompt enhancer?

**Kirkland Gee:** I haven't, no.

**Kirkland Gee:** I didn't even notice the little icon until it had been, like, I'd already been sort of in the groove of things.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** But it's probably worth, I mean, just doing some sort of prompt transformation to make this more.

**Anshuman Pandey:** Yeah, so if I do something super simple, like "write tests for this," it can kind of go awry. It's like going to Google and saying "find a cat"—you might be looking for heavy machinery, but you see pictures of cats. That's where the prompt enhancer comes in.

**Anshuman Pandey:** For people who are just understanding AI, however it was, write tests for this.

**Anshuman Pandey:** And then, you know, in three seconds, it gave like a full proper prompt to make sure the agent is steered exactly what it should be.

**Kirkland Gee:** Yeah, that's great.

**Anshuman Pandey:** And last but not least, remote agents is sort of what we just GA'd.

**Anshuman Pandey:** So right now we're connected to GitHub SaaS, where it connects directly to a PR.

**Anshuman Pandey:** It's going to clone the code base, spin up the infrastructure in a Docker container in our infrastructure, so you're not hosting any costs or any, you know, computer, whatever it might be.

**Anshuman Pandey:** And then I don't know if you played around with it yet.

**Kirkland Gee:** I haven't used the remote one, no. I was just doing everything locally.

**Anshuman Pandey:** Yeah, so you can do like a generation script.

**Anshuman Pandey:** You can look at your builds.

**Anshuman Pandey:** You can auto-generate a script or you can write the script by hand.

**Anshuman Pandey:** You can create a different branch.

**Anshuman Pandey:** But what I really like is this remote agents panel where I can kind of...

**Kirkland Gee:** Ah, very good, okay.

**Anshuman Pandey:** All the different agents I've started, I can open the thread and see the changes that have been made.

**Kirkland Gee:** Now that's really sick.

**Kirkland Gee:** I've done this with quad code, something like this, where I'll have, you know, four or five different terminal windows open, working on different things.

**Kirkland Gee:** I've played around with that a little bit.

**Kirkland Gee:** But this is really nice with everything.

**Kirkland Gee:** Just, yeah, that's sick.

**Anshuman Pandey:** Yeah.

**Anshuman Pandey:** And the beauty of it is I can actually SSH into the remote environment and edit files inside of that remote dev environment, bring them locally, or just create a PR directly from the IDE.

**Anshuman Pandey:** So this is kind of where everything's headed.

**Anshuman Pandey:** Towards remote agencies, where the big push is internally and for engineering.

**Anshuman Pandey:** And, you know, I think we were kind of de facto first to market to advertise this before Jules and Codex and all that.

**Anshuman Pandey:** That was kind of the first time where, you know, instead of going for parity, we were actually first to market in innovation.

**Kirkland Gee:** Yeah, that's very cool.

**Anshuman Pandey:** Yeah, and lastly, we have a Slack integration, right?

**Anshuman Pandey:** Same scenario—you connect it with GitHub repositories.

**Anshuman Pandey:** Per channel, we can give it a subset of repositories to have access to, and it's sort of a feature parity with chat.

**Anshuman Pandey:** Asking questions, it gives you details.

**Anshuman Pandey:** So a lot of our non-technical developer folks have the most value from it.

**Anshuman Pandey:** So things like support, now they can ask specific questions about the product.

**Anshuman Pandey:** Sales engineers, where they can understand the product at a more technical depth.

**Anshuman Pandey:** Can I do this integration?

**Anshuman Pandey:** And then PMs, right?

**Anshuman Pandey:** Instead of having a two-hour planning session, now they just ask, I need to add this button.

**Anshuman Pandey:** Okay, here are the three changes that need to be made.

**Anshuman Pandey:** I have three stories.

**Anshuman Pandey:** Give it to the appropriate developer.

**Anshuman Pandey:** All that's done in five minutes.

**Anshuman Pandey:** So the productivity gains are no longer just for developers.

**Anshuman Pandey:** It's actually for anyone involved with product or code, because we're able to abstract outside of the IDE.

**Anshuman Pandey:** Yeah, I'll leave it to you to kind of drive what you want to see.

**Anshuman Pandey:** Any questions you might have?

**Kirkland Gee:** No, this is all making sense.

**Kirkland Gee:** I'm just trying to think.

**Anshuman Pandey:** So I'll highlight a couple of other technical differentiators.

**Anshuman Pandey:** One is when it comes to security.

**Anshuman Pandey:** So security-wise, we had SOC 2 Type 2.

**Anshuman Pandey:** We just got ISO 42001.

**Anshuman Pandey:** So if you're not aware, that's the new standard of measuring how not just data is handled, but how AI systems are configured and the data between them is handled.

**Anshuman Pandey:** So what a lot of people don't understand is outside of just your frontier models, you have a lot of sub-processors in some sort of AI setup.

**Anshuman Pandey:** So like Cursor, Windsurf, have like 25 sub-processors with very vague statements on what data is going to be looked at, how it's going to be trained or not trained.

**Anshuman Pandey:** And the whole thing is, oh, well, the embeddings are stored locally.

**Anshuman Pandey:** Actually, what happens is all the code and data is sent to the sub-processes in the cloud where the embeddings are calculated, and then it's stored on a local machine.

**Anshuman Pandey:** Our belief is embeddings can't be reverse-engineered, which, you know, there's been a lot of theoretical papers saying that it definitely can.

**Anshuman Pandey:** Instead, we're like, yeah, we scan your code, those embeddings are stored in the cloud, but what we did is we just made it super secure.

**Anshuman Pandey:** So we have customer-managed encryption keys, we have ISO 42001, and we never train on any customer data or code.

**Anshuman Pandey:** So that reduces, you know, IP leakage, that reduces data pollution.

**Anshuman Pandey:** And then we also have what's called proof of possession, which serves two purposes.

**Anshuman Pandey:** One is quality and speed, and also security.

**Anshuman Pandey:** So the way it works is, like, Kirkland, you and I say we're working on the same branch.

**Anshuman Pandey:** We both pull down the code into our workspace.

**Anshuman Pandey:** Now, if you pull it down first, Augment's going to scan the files, send it to the cloud for indexing and storing the embeddings.

**Anshuman Pandey:** If I come in secondly, Augment's going to realize I'm in the same tenant, and I don't need to do duplication. So we reduced the amount of copies of code that is out there and reduced the index timing for every subsequent user.

**Anshuman Pandey:** Now, say you and I are working on the same file, we make different changes in our workstation.

**Anshuman Pandey:** Augment's going to assign each of us unique hashes.

**Anshuman Pandey:** So all the suggestions coming in are relevant to me and what I'm doing, and it's not going to conflict with what's going on on your side.

**Anshuman Pandey:** And that's that proof-of-possession architecture that we built.

**Kirkland Gee:** Yeah, very cool. I was wondering why I hadn't tried the remote agents yet. I still have to get the request approved for our GrowthX GitHub org—I haven't had time to look at it yet. Because I was like, "Oh, let me go see this for a second," and then that's why it hasn't happened yet.

**Anshuman Pandey:** Yeah.

**Anshuman Pandey:** The next phase is right now sort of all user-iterative—give it an input, it produces output, which is an end state.

**Anshuman Pandey:** What we're trying to get to next is dynamic deployments, right?

**Anshuman Pandey:** So instead of me just giving it, look for my tickets, work on this ticket, work on that ticket, then it's going to be like, let's set up event listeners, webhooks, GitHub actions where I deploy agents with a specific prompt.

**Anshuman Pandey:** It's continuously listening for changes in states and then go in and take the actions continuously, communicate with the next step of agents and have like a whole fleet of, you know, agent processes set up by Augment.

**George Haikal:** Can you expand a little more on that?

**George Haikal:** I know at the beginning, you kind of gave a little bit of the vision of where you want to go, but give us some more language on things that are coming in next coming months and how, like how that's positioned you all.

**Anshuman Pandey:** How are you thinking about it?

**Anshuman Pandey:** Oh, I can't speak specifically to roadmap because it's changing so much all the damn time.

**Anshuman Pandey:** You know, we're running on clicking notes and whiteboards over here.

**George Haikal:** Us too.

**Anshuman Pandey:** Yeah.

**Anshuman Pandey:** Like, the best way I could say it is, one, we're set up to, you know, focus on the individual developer by giving the best IDE experience by understanding these enterprise code bases.

**Anshuman Pandey:** They're large, they're messy, there's a lot of nuance, and for that, you need a few things.

**Anshuman Pandey:** One is that hyper-scale index, and two is a context engine that's able to gather the right data, not the most data.

**Anshuman Pandey:** It's not about the size of the context window, it's truly about getting the right context.

**Kirkland Gee:** 100%.

**Anshuman Pandey:** So that's a differentiator when it comes to just producing quality code.

**Anshuman Pandey:** We also have what's called recency information, I don't know if you've heard of this, where, say you're writing code, it's not just going to keep giving you the same sort of suggestions, it's going to understand the state of code.

**Anshuman Pandey:** So if right now, string equals ABC, I'm just going to realize that it was a string equals AB two iterations before.

**Anshuman Pandey:** So the more you write, the more it actually starts adapting to how you perform.

**Anshuman Pandey:** Yeah, so it's not just, you know, looking at context as a whole.

**Anshuman Pandey:** It's actually looking at what the user is doing continuously.

**Anshuman Pandey:** With that recency information, it will adapt to suggestions accordingly as well.

**Kirkland Gee:** Yeah, I mean, I've been really impressed at what it's been able to do for me, you know, like I said, in a day and a half, basically.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** So that all makes sense.

**Kirkland Gee:** And I'm working on, like, a super small code base, too.

**Kirkland Gee:** It's like a brand new, you know, marketing site, essentially, versus something big in enterprise.

**Kirkland Gee:** We don't have anything big enough to be in enterprise around here yet.

**Anshuman Pandey:** Fair enough.

**Anshuman Pandey:** But in terms of next steps, right, it's like once we've kind of gotten this whole context engine set up, where you're giving great output for the individual developer, having them not leave the IDE and environment of choice, what's next?

**Anshuman Pandey:** It's how do we help enterprises across the SDLC?

**Anshuman Pandey:** How do we help with documentation?

**Anshuman Pandey:** How do we help with, you know, looking at tickets?

**Anshuman Pandey:** How do we help with PRs and PR reviews?

**Anshuman Pandey:** How do we automate all of that?

**Anshuman Pandey:** Because Augment's set up the way it is, we're, you know, we have actually a lot of options, how to branch out from the context engine and build on top of it.

**Anshuman Pandey:** Right now, our primary offering is IDE and agents in the IDE, then we're able to abstract that out into the Slack bot.

**Anshuman Pandey:** So moving forward, we're looking at the best ways to help, you know, abstract that layers above.

**Anshuman Pandey:** If I can explain it, the best way would be when coding first came out, it was, you're doing assembly language.

**Anshuman Pandey:** You're going at the very bare metal and doing like the actual registers and whatnot.

**Anshuman Pandey:** Then you abstract the layer plus, you get into C, you know, OS programming, abstract the layer plus, you get Java, TypeScript.

**Anshuman Pandey:** Same thing with AI with Augment, right?

**Anshuman Pandey:** We got down to the base level, understands how code works.

**Anshuman Pandey:** Then the IDE level where we're pairing with developers. And then Augment is set up in the future to abstract at a level higher where we can do business logic to code because of how we understand code.

**Anshuman Pandey:** So whatever that might take, that's TBD, but the differentiator is Augment's the only one who can get to that stage from where everyone else is at in the industry.

**Kirkland Gee:** And you've talked about target audience. I know we talked a little bit about it.

**Kirkland Gee:** It's like that person that's not just like a vibe coder, right?

**Kirkland Gee:** That's a step above that, but maybe they're, you know, whatever place they are.

**Kirkland Gee:** Maybe they're more experienced, but they probably don't have to be, right?

**Kirkland Gee:** To be an ideal customer.

**Kirkland Gee:** Do you see that expanding to people who like don't code at all, who are now going to be able to, your, you know, to your example, say a Slack bot, right?

**Kirkland Gee:** Some marketer at a company who's doing SEO stuff, who's tired of waiting on their team to just go change a header on a page in an XJS repo, right?

**Kirkland Gee:** That kind of person I'm imagining that's even now, but especially in six months, 12 months, right?

**Anshuman Pandey:** Yeah. Our ICP in general is organizations with 100 to 5,000 developers.

**Anshuman Pandey:** But in terms of value gain from product, yeah, now it's no longer just developers in the IDE.

**Anshuman Pandey:** It's anyone who's related to code at all, whether it's product, whether it's marketing who wants to understand how this code works better.

**Anshuman Pandey:** For example, Emma from our marketing team, when applying for Gartner, Magic Quadrant, when looking at questions to give influencers, she just asked a Slack bot.

**Anshuman Pandey:** How does that work?

**Anshuman Pandey:** So it's anything that's related to code and product, that's where everyone's able to help because, again, we're not just confined to the IDE.

**Kirkland Gee:** Yep.

**Kirkland Gee:** That makes sense.

**Kirkland Gee:** Yeah, George, I don't know.

**Kirkland Gee:** I don't have the exact thing, but there's got to be.

**Kirkland Gee:** I know our first kind of plays are targeted just towards developers, but there's got to be some interesting things there.

**Kirkland Gee:** And not even just PMs.

**Kirkland Gee:** Again, like anybody in a more technical organization who has these non-technical roles.

**Kirkland Gee:** Additional context of how the code base works or want to make very small changes, you know, I don't have all the ideas, but there's some there.

**Anshuman Pandey:** The other thing I've been just kind of playing with, but that seems to stick with engineering leaders.

**Anshuman Pandey:** So this whole vibe coding phase, right?

**Anshuman Pandey:** Everyone's super hype about it.

**Anshuman Pandey:** Hype is great.

**Anshuman Pandey:** I can do these zero to one apps, but there's no such thing as vibe engineering, right?

**Anshuman Pandey:** Like coding, everyone thinks is, I just need to write a couple of lines of code, and then I can deploy on local host.

**Anshuman Pandey:** But when it comes to enterprise, it's very different.

**Anshuman Pandey:** How do I set up a CICD pipeline?

**Anshuman Pandey:** How do I make sure I do load balancing?

**Anshuman Pandey:** How do I set up like cloud infrastructure?

**Anshuman Pandey:** How do I deploy that?

**Anshuman Pandey:** That is what Augment is good at.

**Anshuman Pandey:** We work with the engineering aspect of software development, not just the coding aspect.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Yeah, I have, you know, years ago ran into that.

**Kirkland Gee:** I took that exact path of being like, I can do this.

**Kirkland Gee:** And then you get an app working and then actually it takes you twice as long just to get it deployed somewhere as it did to actually write the code.

**Kirkland Gee:** For those people who've never done it before.

**Kirkland Gee:** It's a very common pitfall.

**Kirkland Gee:** Okay.

**Kirkland Gee:** I mean, I know we have an hour booked, but I feel pretty clear on everything.

**Kirkland Gee:** I think all of this makes sense.

**Kirkland Gee:** I feel like I have a good vision of what makes this different.

**Kirkland Gee:** I don't know, George, or if you guys have any other questions or things that would be helpful for you.

**George Haikal:** Yeah, I have a few.

**George Haikal:** I guess just like what are the most, what are the biggest requests or pain points that you're getting from your users?

**George Haikal:** Like what do they want to be next or where are they struggling most?

**Anshuman Pandey:** Struggling currently and what Augment solves for or what's coming next?

**George Haikal:** Struggling currently and what Augment solves for.

**Anshuman Pandey:** Gotcha.

**Anshuman Pandey:** Onboarding is a big one, right?

**Anshuman Pandey:** I have this super complex 10-year-old code base.

**Anshuman Pandey:** It's taking developers three to six months to just figure out what's going on before they can become productive.

**Anshuman Pandey:** Augment solves that quickly, right?

**Anshuman Pandey:** Quickly find out how the code base is structured, understand where I need to go.

**Anshuman Pandey:** I have a ticket.

**Anshuman Pandey:** It lets me go there as quickly as possible.

**Anshuman Pandey:** When it comes to just code output in general, oh, you know, these other coding systems are giving super generic output.

**Anshuman Pandey:** It's not matching the style and syntax.

**Anshuman Pandey:** Augment solves for that.

**Anshuman Pandey:** Writing test cases.

**Anshuman Pandey:** Writing, you know, infrastructure as code, like deploying to the cloud, doing migrations.

**Anshuman Pandey:** A lot of people use AI for code traditionally as like doing really small steps.

**Anshuman Pandey:** Augment is now starting to become associated with larger business initiatives.

**Anshuman Pandey:** Like I need to do this huge database migration.

**Anshuman Pandey:** How do I expedite that?

**Anshuman Pandey:** Augment can help with the documentation phase, the information discovery phase, writing the code, testing the code, all autonomously as well, right?

**Anshuman Pandey:** Doing PR reviews. For example, language upgrades.

**Anshuman Pandey:** So another example is one of our customers, they had this pretty big Spring Boot version upgrade project, which they thought was going to take three to four weeks.

**Anshuman Pandey:** One developer using Augment did that in two hours and it worked perfectly.


**Anshuman Pandey:** And there's some customer stories like out on our website that kind of highlights some of these metrics.

**Anshuman Pandey:** But it's like these bigger initiatives.

**Anshuman Pandey:** How do I expedite these bigger initiatives without losing quality of code?

**Anshuman Pandey:** That's where you use Augment.

**Anshuman Pandey:** Oh, let me do a quick POC or let me, you know, vibe code out a website over the weekend.

**Anshuman Pandey:** Sure.

**George Haikal:** Use something else.

**George Haikal:** Got it.

**George Haikal:** What is Augment not doing right now that people are asking for?

**Anshuman Pandey:** Niche cases like COBOL or Fortran—there's not enough data out there and we're never claiming to be good at that. For COBOL to Java upgrades, go use IBM WatsonX.

**Anshuman Pandey:** Another thing is how do I dynamically incorporate this into my custom SDLC workflows?

**Anshuman Pandey:** How do I, you know, access the power of the context engine outside of the IDE?

**Anshuman Pandey:** How do I do more dynamic stuff like I was mentioning with the web hooks and whatnot?

**Anshuman Pandey:** And so that's all things that are being considered as roadmap items right now.

**Anshuman Pandey:** There are a few projects being worked on internally to address that next phase of growth.

**Anshuman Pandey:** Where it's, okay, we're no longer just a coding assistant, but we are your de facto coding awareness platform that you can customize and modularize across the SDLC.

**George Haikal:** I love that.

**George Haikal:** I love that.

**George Haikal:** Thank you.

**George Haikal:** This was great. We can all get a little time back as well.

**George Haikal:** Anshuman, do you have any materials you could share with us as well that go into the same, if not more, level of depth on everything we talked about? Like slides or anything we can share externally?

**Anshuman Pandey:** Yeah, I'm sure I can wrangle some things together.

**Anshuman Pandey:** For sure.

**Anshuman Pandey:** Yeah, I'll look.

**George Haikal:** Amazing.

**George Haikal:** We'll share this recording with our team, obviously, but it would be helpful to have content that they can look over.

**Anshuman Pandey:** For sure.

**Anshuman Pandey:** Yeah, I'll send that over probably right after this.

**George Haikal:** Great.

**George Haikal:** Great.

**George Haikal:** Really appreciate your time and this helped bring a lot of clarity.

**George Haikal:** And so we're excited to get moving on it.

**Anshuman Pandey:** Awesome.

**Kirkland Gee:** Appreciate you, brother.

**Kirkland Gee:** Yeah, thanks very much.

**Anshuman Pandey:** All right.

**Anshuman Pandey:** Cheers. Bye, guys.
