# Blaxel Kickoff Call

<metadata>
date: 2025-12-12
time: 18:04 UTC
duration: 49 minutes
organizer: william@growthx.ai
participants: William Leborgne, Kathy Lam, Nicolas Lecomte
fathom_recording_id: 108439573
fathom_url: https://fathom.video/calls/504891921
share_url: https://fathom.video/share/TQsLgRz5AyHrN4ziRrv_3W6m-M-cveYg
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Blaxel kicked off their content marketing engagement with a deep dive into Blaxel's core product—a perpetual sandbox platform that gives AI agents secure, high-performance environments for code execution. William and Kathy learned how Blaxel differentiates through MicroVMs (not containers), 25ms resume times, and perpetual standby capabilities, then walked through the Strapi CMS publishing workflow for content. The team agreed that GrowthX will develop product artifacts and a data-driven content strategy by next Friday, leading to calibration articles and full-scale content production in January.

---

## Context

Blaxel is an infrastructure platform for AI agents founded by Nicolas Lecomte and a co-founder (CEO). They're on the cusp of significant growth—landing major customers like Webflow (whose AppChain uses Blaxel for code execution) and courting Strapi as a new customer. GrowthX was engaged to drive awareness and SEO visibility for Blaxel's perpetual sandbox platform, addressing their core business problem: lack of market awareness despite product-market fit. Nicolas is technical and product-focused; William and Kathy manage the GrowthX engagement. The relationship is strategic and multi-quarter, with regular syncs planned and a content strategy kick-off scheduled for the following Friday (Dec 19).

---

## Relevance

- **To GrowthX Delivery:** Core SEO and content strategy engagement; Blaxel uses Strapi CMS for publishing, requiring clear markdown → CMS workflows and schema markup integration. GrowthX will produce both calibration articles and scaled content production. Content categories align with Blaxel's positioning: Guides (GrowthX), not news or engineering blogs.

- **To GrowthX Business Development:** $200k+ SaaS engagement; Blaxel is acquisition-focused with strong product-market fit (Webflow, Strapi relationships) and venture backing. Regular syncs and ongoing collaboration signal account expansion potential. Reference case study opportunity if engagement drives measurable SEO wins.

- **To Content & Positioning:** Clear messaging hierarchy: "Perpetual Sandbox Platform" > "AWS for agents" or "a computer for your agent." Avoid "containers," "framework," or vague "agent platform." Primary use cases: coding agents, PR review agents, data analyst agents. Key differentiator: MicroVM security + 25ms resume + perpetual standby vs. container-based competitors like Daytona.

- **To CheckThat / AI Visibility:** Data-driven content strategy will combine keyword research with CheckThat insights (LLM visibility). Next Friday's strategy meeting should incorporate LLM-based search data alongside Google search trends to identify high-potential, low-difficulty topics.

---

## Overview

- **Blaxel is a "perpetual sandbox platform"** for AI agents, offering secure, high-performance MicroVMs that resume from standby in 25ms.
- **The platform has two products:** Sandboxes (the core offering) and Agent Hosting. Hosting agents on Blaxel eliminates network latency to sandboxes, enabling optimal end-to-end performance.
- **Primary use cases** include coding agents (e.g., Webflow's AppChain), PR review agents, and data analyst agents.
- **Key differentiators are security and speed.** Blaxel uses MicroVMs for superior isolation over containers, and its unique "perpetual standby" feature enables near-instant resumes.

---

## Key Topics

### Blaxel's Core Offering: The Perpetual Sandbox

  - **What it is:** A secure, high-performance environment for AI agents to run code.
  - **Technology:** MicroVMs (Micro-Virtual Machines), which are faster to start than traditional VMs.
  - **Key Differentiators:**
      - **Security:** MicroVMs provide superior isolation over containers, preventing agent "escapes" to the host server and protecting other tenants' data.
      - **Speed:** Sandboxes enter a low-cost standby state after inactivity. They resume in **25 milliseconds** with their full state intact, enabling an instant, persistent user experience.
      - **Perpetual Standby:** Unlike competitors, Blaxel allows sandboxes to remain in standby indefinitely, eliminating the need for manual deletion and recreation.

### The Platform: Sandboxes + Agent Hosting

  - **Two Products:**
    1.  **Sandboxes:** The core offering, solving for secure and fast code execution.
    2.  **Agent Hosting:** A serverless platform for the agent's main logic.
  - **Value of Integration:** Hosting agents on Blaxel eliminates network latency to sandboxes, enabling optimal end-to-end performance.
  - **Additional Tools:**
      - **Jobs:** For parallelizing background tasks.
      - **MCP Servers:** For hosting custom tools that agents can discover and use via the MCP protocol.

### Customer Voice & Use Cases

  - **Primary Use Cases:**
      - **Coding Agents:** Agents that generate and execute code (e.g., Webflow's AppChain).
      - **PR Review Agents:** Agents that analyze code changes in pull requests.
      - **Data Analyst Agents:** Agents that generate and run scripts (e.g., Python, SQL) to answer natural language queries.
  - **Why Customers Switch:**
      - **Reliability:** Webflow switched from an internal prototype due to downtime.
      - **Support:** High-touch support (1-min response times) is a key differentiator.
  - **Customer Pain Points:**
      - **Onboarding UX:** The initial setup process is not intuitive, requiring significant support. This is a current focus for improvement.

### Content Strategy & Publishing Workflow

  - **Content Strategy:**
      - **Data-Driven:** GrowthX will use keyword data to identify high-potential topics with low difficulty.
      - **Product-Driven:** Blaxel's team will provide insights on emerging use cases and product direction.
  - **Publishing Workflow (Strapi CMS):**
      - **Process:** Write in Markdown → Paste into Strapi → Add metadata (title, excerpt, author, category) → Publish.
      - **Category:** All GrowthX content will be published under the "Guides" category.
      - **Missing Feature:** Strapi lacks a native field for schema markup; Nicolas will investigate adding it.

### Messaging & Positioning

  - **Key Positioning:** "Perpetual Sandbox Platform."
  - **Terms to Avoid:**
      - **"Containers":** Not the underlying technology.
      - **"Framework":** Not a tool for building agents (like LangChain).
  - **Useful Analogies:**
      - **"AWS for agents":** Cloud infrastructure for agents to run on.
      - **"A computer for your agent":** Giving an agent the tools it needs to work efficiently.

---

## Action Items

**Nicolas Lecomte (Blaxel)**
- Fix sandbox preview/terminal demo
- Add schema markup to Strapi; confirm image workflow with William

**William Leborgne (GrowthX)**
- Introduce Nicolas to AirDNA contact regarding data-analysis agents
- Inform Paul regarding product artifacts and calibration article; send content strategy by next Friday (Dec 19)

---

## Transcript
**William Leborgne:** The company context artifact, the writing guidelines artifact, and those three things combined are put into our AI content workflow, which allows us to have that extremely high quality content.

**William Leborgne:** So all of that said, this is both how does your product work, what does it do, why is it important, as well as anything that you can add around the actual customer voice.

**William Leborgne:** So I have some questions in here that I can kind of trigger things.

**William Leborgne:** But also, like I said, like, I'm happy to like, let you go and share, however, you know, that makes the most sense.

**William Leborgne:** Yeah, okay, of course.

**Nicolas Lecomte:** So I think maybe what I can do is, I guess, give the quick intro, which is mostly stuff that we already talked about, the good stuff, refresher, show you.

**Nicolas Lecomte:** The thing is, you know, all demos are sort of different, and we keep like adjusting a bit, obviously, the flows.

**Nicolas Lecomte:** So I can do like a basic sort of demo.

**Nicolas Lecomte:** And then, you know, we can go through your questions and obviously, if you have stuff that you want to ask.

**Nicolas Lecomte:** Perfect.

**Nicolas Lecomte:** I love that.

**Nicolas Lecomte:** And I will share with you.

**William Leborgne:** Sorry, I'm just cleaning it up.

**William Leborgne:** I'm still somewhat new to using Notion.

**William Leborgne:** So I added, I moved it all from Google Docs into Notions and I was like, oh man, this is a mess.

**William Leborgne:** So go ahead and get started and I'll share this document with you shortly.

**William Leborgne:** Sure.

**Nicolas Lecomte:** Yeah, I think I received an application from Notion just before the meeting.

**Nicolas Lecomte:** But yeah, okay.

**Nicolas Lecomte:** Let me share the whole screen, I think, would be better.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** All right.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** So, yeah, Blaxel, like we were saying, so we're the perpetual sandbox platform where what you get as a user is almost instant latency for your agents when they need to run code and which

**Nicolas Lecomte:** We this by two main ways.

**Nicolas Lecomte:** One is our Sandbox product, which is the core offering.

**Nicolas Lecomte:** So it's a whole platform and we have several products, which I'm gonna go through them, but Sandbox is the core offering.

**Nicolas Lecomte:** That's where the code runs and I can get into more details after.

**Nicolas Lecomte:** But essentially what a Sandbox is, is it's an isolated environment.

**Nicolas Lecomte:** I like to describe it as also like the computer of the agent and I like to think about it as like, you know, humans, they have computer, you know, workers, when you get somebody to work in your company, usually you give them a laptop.

**Nicolas Lecomte:** Same goes for agents is, you know, agents can, they can resume by themselves or you can give them their own computer where they have unlimited freedom.

**Nicolas Lecomte:** And it's best if you give them unlimited freedom on the computer with the restricted access that you want.

**Nicolas Lecomte:** And Sandbox is like, you do that.

**Nicolas Lecomte:** They're essentially, again, that isolated runtime.

**Nicolas Lecomte:** But think I I can't

**Nicolas Lecomte:** It's a micro-VM.

**Nicolas Lecomte:** It's a micro-virtual machine, which is a specific type of VM where you've removed some part of the BIOS and the OS and everything to make it faster to start, where agents get access to it via an API.

**Nicolas Lecomte:** They can spawn it by themselves.

**Nicolas Lecomte:** They get access to it via an API, and they can do whatever they want.

**Nicolas Lecomte:** Again, it's a full computer, Linux computer.

**Nicolas Lecomte:** So they have access to a full file system.

**Nicolas Lecomte:** They can read files.

**Nicolas Lecomte:** They can run code.

**Nicolas Lecomte:** This is the main usage to run.

**Nicolas Lecomte:** So they generate files just like your cursor would do.

**Nicolas Lecomte:** They would generate files, and then that entire code base would be living inside of the sandbox.

**Nicolas Lecomte:** And then the good thing is that you can also run it because it's isolated.

**Nicolas Lecomte:** So that means that we are in charge of ensuring that there's no way, never, that your agent can escape the sandbox and access other people's sandboxes or mess up stuff.

**Nicolas Lecomte:** So that's the purpose of the sandbox and isolation.

**Nicolas Lecomte:** That's what is ensured by MicroVM.

**Nicolas Lecomte:** Can you pause there just one second?

**William Leborgne:** Because I just want to clarify the escaping part.

**William Leborgne:** Being a very non-technical person, don't completely understand the concept of an agent escaping.

**William Leborgne:** Like it's in a prison and it's like, okay, let me go and mess around and break other things.

**William Leborgne:** What does that mean exactly?

**Nicolas Lecomte:** Yeah, well, it's basically when you...

**Nicolas Lecomte:** So a MicroVM is something virtual which runs on a server which hosts multiple MicroVMs of multiple people.

**Nicolas Lecomte:** so you have multiple codebases of other people.

**Nicolas Lecomte:** And usually companies that sell AI, they have multiple customers, which means multiple repos and codebases.

**Nicolas Lecomte:** And so it is possible with certain virtualization technologies, it is possible to escape from that virtual environment and, you know, go back into the host, which is the server, the underlying server first for that virtualized environment.

**Nicolas Lecomte:** It's supposed to be isolated, but you can sort of, you know, access permissions at the server level, which give you access in turn to the rest of, you know, whatever is on that server, which usually is other tenants.

**Nicolas Lecomte:** Maybe it's just, know, like ultimately on the server.

**Nicolas Lecomte:** And if it's just on the server, then, you know, you can't really escape the server.

**Nicolas Lecomte:** But, you know, if you have other tenants on there, then that's a problem.

**Nicolas Lecomte:** And this is something really important because, I mean, one, you know, that's one of the problems with sandboxes is if you do it bad or if you, and some of our competitors are using higher level virtualization technologies, like Daytona, for example.

**Nicolas Lecomte:** Daytona is one of the competitors on the list that we shared, one of the main ones.

**Nicolas Lecomte:** They use a different kind of virtualization technologies, which is containers.

**Nicolas Lecomte:** So you have traditionally micro VMs and containers.

**Nicolas Lecomte:** And so containers is more virtual, like it's a higher level virtualization layer.

**Nicolas Lecomte:** So it's easier to escape versus a micro VM is ensures full isolation.

**Nicolas Lecomte:** That's the technology that's.

**Nicolas Lecomte:** used by AWS for most of their serverless runtimes.

**Nicolas Lecomte:** That's the gold standard for isolation.

**Nicolas Lecomte:** Okay.

**Kathy Lam:** To a lot of these agents escaping, is that intentional or sometimes just unintentional?

**Kathy Lam:** Both.

**Kathy Lam:** It can be both.

**Nicolas Lecomte:** It can be both, yeah.

**Nicolas Lecomte:** But I guess, yeah, the big risk is if it is intentional because somebody, you know, let's say you're using Lovable, if you're familiar with that product, know, like anybody can sort of prompt the coding agent and, you most people will like, hey, generate a website for X, Y, Z.

**Nicolas Lecomte:** then, you know, some, you know, bad people could say, hey, you know, and prompt it exactly the way that you should to get access to those things and other people's basis.

**Nicolas Lecomte:** So that, and I think, you know, CodeRabbit, they're an AI that watches your code, PRs, your pull requests, so.

**Nicolas Lecomte:** And then that suggests changes, so it does reviews for you.

**Nicolas Lecomte:** And I think that they got exposed, I think, a month ago for having a big security breach where everybody could access everybody else's code bases, which was pretty bad.

**Nicolas Lecomte:** I think it was CodeRabbit that had this.

**Nicolas Lecomte:** So, yeah, what we do is that's, again, the main offering is those sandboxes.

**Nicolas Lecomte:** You can really create them.

**Nicolas Lecomte:** You start from a base template that includes, you know, everything that you need to start.

**Nicolas Lecomte:** You create the sandbox, I can show you here.

**Nicolas Lecomte:** So you create the sandbox, you choose the size, you choose, you know, wherever the sandbox is going to get deployed.

**Nicolas Lecomte:** And the creation, so there's a few things.

**Nicolas Lecomte:** creation takes a couple of seconds, like I think two seconds at the time, so it's already deployed.

**Nicolas Lecomte:** And then now it goes back to standby.

**Nicolas Lecomte:** And so, again, that's the key thing for us, which goes back to the initial value proposition that I was telling you, which is ultimate speed, you know, the fastest end-to-end speed possible for your coding agent workflow.

**Nicolas Lecomte:** And the first reason, the first way that we achieve this is by having those sandboxes, which have a standby state by default, which is quite unique.

**Nicolas Lecomte:** I think we're literally the only competitors to really have that standby state so powerful and so infinite as you can keep your sandbox in standby forever if you're willing to pay the price.

**Nicolas Lecomte:** And so here it's in standby, which you're not paying for compute, you're only paying for the snapshotting. So we restored the snapshot of your sandbox.

**Nicolas Lecomte:** And then as soon as somebody connects to the sandbox using this API endpoint, this will sort of spin up the sandbox.

**Nicolas Lecomte:** And this is a really, really fast operation because of the way we do it, we're able to resume it in 25 milliseconds with exactly the way that it was before.

**Nicolas Lecomte:** So I guess I can show you this is a new feature actually that we introduced, which will make it very easy for me.

**Nicolas Lecomte:** So there was a really quick connect here. And so I guess what's going on in this sandbox, they changed that image.

**Nicolas Lecomte:** Okay, this is supposed to be an application.

**Nicolas Lecomte:** So here I'm navigating inside of the Sandbox, kind of like an agent would.

**Nicolas Lecomte:** And basically to show you what is usually one of the main use cases that our users do is when the agent is previewing, is having a preview on the Sandbox.

**Nicolas Lecomte:** Because usually their AI products, they want to show it to other people.

**Nicolas Lecomte:** And so they're showing this, or they're having the Sandbox, and then they're creating the application inside the Sandbox.

**Nicolas Lecomte:** The agent iterates, and then you want to preview it.

**Nicolas Lecomte:** And so, I mean, there are plenty of ways that you can run a preview server inside of a Sandbox.

**Nicolas Lecomte:** So, for example, this one here, this is a very new demo.

**Nicolas Lecomte:** Literally, this feature came on yesterday, so I hope it works.

**Nicolas Lecomte:** Let's try it if it doesn't work.

**William Leborgne:** Live demo, you know, you never know.

**William Leborgne:** Not only is it a live demo, it's a live demo on a feature that I've never tried live.

**Nicolas Lecomte:** And so, when I open the preview, hopefully it will work. It starts the preview server the first time. And it doesn't work. So that was not the correct way to do it. Anyways, forget about it.

**Nicolas Lecomte:** The way that I can do it, I can just remove that sandbox and I have a better way of doing it.

**Nicolas Lecomte:** Because usually I've shown you the console, but most people, ultimately, again, our customers, they are engineers. It's a technical product. We sell to engineers from AI companies that build agents that need to run code.

**Nicolas Lecomte:** Again, that's the ICP: AI agents or AI companies where the product is an agent that needs to run code. So, obviously, those people, you know, the console is great to test or to visualize metrics and stuff, but they usually use their IDE and whatever dev tools they're used to.

**Nicolas Lecomte:** So I can just run here. This is a demo script that I know works, where I'm creating a sandbox, again, just like an agent would using scripts.

**Nicolas Lecomte:** This uses our SDK, so we have a Python, we have a TypeScript SDK to interact with the Azure platform.

**Nicolas Lecomte:** So here I just created a sandbox, and so what I can do is I have the same sort of terminal option. I can remotely connect to the sandbox using that same terminal interface, just like we were seeing before.

**Nicolas Lecomte:** Here in the interface, so if I go into cd here, Blaxel, I think it is, okay, so here I can redo what I wanted to do before, just to show you what I meant. And then, if I create my preview URL, this will create a preview. I can put a custom domain, so this means that people, let's say that we sold to Lovable, they could have a .lovable.dev domain. That's a way to white-label Blaxel with your branding.

**Nicolas Lecomte:** It's not working. Well, I'll try to debug this after, but imagine that you are seeing the app is essentially what the user would see ultimately from this.

**Nicolas Lecomte:** I think we broke something with that terminal feature. This is the sandboxes. This is really the core of the offering.

**Nicolas Lecomte:** And usually people that come to the platform, they come for sandboxes because that's what they are looking for. The key problem to solve for them is, okay, I need somewhere safe. It has to be safe and secure.

**Nicolas Lecomte:** So meaning all the isolation stuff that I was talking about. It needs to be very fast and very easy to use, like not a lot of heavy infrastructure lifting where my agent can run code. That's the main thing.

**Nicolas Lecomte:** And we see more and more agent companies where the agent will need to run code because it needs to be more intelligent. So they come for the sandboxes and then they sort of realize, okay, but I can expand. I can see that I can host the rest of my agent logic.

**Nicolas Lecomte:** And this is really the way that you can benefit from all the Blaxel features: on top of the sandbox core product, we have this entire hosting section. For us, it's easy to do because it uses the same backbone, the same compute engine that we have for the sandboxes. Underlying any agent hosting is basically its own sandbox; it's run in a sort of sandbox.

**Nicolas Lecomte:** And because we control the networking, because we control everything on that infrastructure path, we're able to optimize the way that your agent talks to your sandbox to make sure that obviously authentication is handled, but more specifically that the latency between your agent and sandbox is absolutely minimal in terms of network overhead and authentication steps.

**Nicolas Lecomte:** And the agent hosting, I would say in itself, is more basic. I think that the true strength of it is if you combine it with sandboxes and the rest.

**Nicolas Lecomte:** Because it's really just about hosting whatever agent logic that you have—host it as a serverless API. That's really what it is.

**Nicolas Lecomte:** And when you host it on Blaxel, you get that endpoint, which lets you call the agent. So we can sort of do a test here.

**Nicolas Lecomte:** Again, I don't really know if that agent is supposed to answer anything to Hello World.

**Nicolas Lecomte:** But you can sort of prototype it here.

**Nicolas Lecomte:** Again, this is fully custom code that a person deploys.

**Nicolas Lecomte:** This is a serverless hosting platform.

**Nicolas Lecomte:** The good thing is you get all the logs.

**Nicolas Lecomte:** so through the console, we give you all the metrics regarding your requests.

**Nicolas Lecomte:** But more specifically as well for everything related to AI and the fact that it's an agentic workflow.

**Nicolas Lecomte:** So I'm thinking about, for example, the end-to-end latency, including the LLM generation, including the, you know, like the calls to the- to

**Nicolas Lecomte:** So you would see traces.

**Nicolas Lecomte:** I don't really have an example of trace, but I think there are some on the documentation where a trace would show you the waterfall.

**Nicolas Lecomte:** So this is a good way to dig into why a certain request is taking some time.

**Nicolas Lecomte:** So here, that request took 32 seconds, which is insanely long.

**Nicolas Lecomte:** So you can see that there's some stuff happening here because it took 27 seconds to route.

**Nicolas Lecomte:** Then, you know, whatever here happens here.

**Nicolas Lecomte:** So you can dig into, okay, there's, you a search happening here.

**Nicolas Lecomte:** There's like a focal.

**Nicolas Lecomte:** So it can connect tools to an agent.

**Nicolas Lecomte:** That's usually how agents, you know, traditionally work.

**Nicolas Lecomte:** They're really an LLM connected to tools.

**Nicolas Lecomte:** So here, for example, it has a tool, which is Google Maps.

**Nicolas Lecomte:** So it's able to connect to Google Maps.

**Nicolas Lecomte:** And here you can see that, you know, that specific Google Map request took that amount of time compared to the rest.

**Nicolas Lecomte:** You can see the logs.

**Nicolas Lecomte:** You have the full log.

**Nicolas Lecomte:** So we give you the full telemetry on whatever is going on in your agent.

**Nicolas Lecomte:** And then that's one of the tools.

**Nicolas Lecomte:** We give you a whole bunch of tools to be all your agents.

**Nicolas Lecomte:** You don't have to use all of them.

**Nicolas Lecomte:** Agents is if you want to host as an API, when jobs is if you want to host and parallelize tasks.

**Nicolas Lecomte:** So maybe some part of your agents will be hosted as agents.

**Nicolas Lecomte:** Maybe some parts will be hosted as jobs.

**Nicolas Lecomte:** But think of jobs more like if you need to, I don't know if I have a good example.

**Nicolas Lecomte:** Maybe if I go in the test workspace, I will see some.

**Nicolas Lecomte:** Think of jobs more like if you need to run a lot of, you know, like thousands of parallel tasks, like in the background, or if your agent is spawning subtasks, that's what jobs will be for.

**Nicolas Lecomte:** So that specific job, which takes inputs and has outputs.

**Nicolas Lecomte:** But job is something that the agent is doing, just to clarify.

**William Leborgne:** Yeah, yeah, exactly.

**Nicolas Lecomte:** It could be an agent, you know, the entry point of the whole system could be an agent.

**Nicolas Lecomte:** hosted here and the agent itself as part of the processing would be like, okay, you know, like that request, I need to trigger a job execution, you know, like 10 tasks in parallel to process it.

**Nicolas Lecomte:** Some people also have this as the entry point.

**Nicolas Lecomte:** It's, we, the point for us is to give you all the tools and the flexibility, give you some like best practices, and then you build your as you want, kind of like, you know, you would do on the cloud, it's on the cloud provider.

**Nicolas Lecomte:** Okay.

**William Leborgne:** And, and, yeah, sorry, go ahead.

**Kathy Lam:** Would someone use like something like Lovable or something like whatever to kind of build their app, but then deploy it on Blaxel?

**Kathy Lam:** Like I'm trying to think of where.

**Kathy Lam:** Yeah, it's an excellent question.

**Nicolas Lecomte:** So non-Lovable, I guess this is more related to the persona, but yes, in general, not for Lovable specifically, Lovable is targeted to non-technical people, mostly hobbyists or, you know, non-devs.

**Nicolas Lecomte:** And it's precisely their thing is they're bringing, you know.

**Nicolas Lecomte:** Software development to people who are not software engineers initially.

**Nicolas Lecomte:** But Cursor, for example, or Cloud Code or any of those tools which are AI for devs, definitely you can use them to code stuff on Blaxel.

**Nicolas Lecomte:** And I think this is one of the growth or one of our growth channels that we're trying to grow the most because it's, I mean, that's the easiest, obviously.

**Nicolas Lecomte:** And that works the same as all the reason why we're doing all of this is to make sure that, you whenever somebody codes and, you know, let's say a developer is like, hey, you know, I'm making an agent.

**Nicolas Lecomte:** What's the best way to, you know, run the code that the agent generates?

**Nicolas Lecomte:** You know, you want the cursor agent or the Cloud Code agent to say, hey, you know, you could use Blaxel or that technology or that technology.

**Nicolas Lecomte:** And then, you know, let me generate a code for how it would run on Blaxel.

**Nicolas Lecomte:** And then you just you can just push it in one quick to us.

**Nicolas Lecomte:** And so for this.

**Nicolas Lecomte:** have a few things, including an MCP server, which I don't know if this is something that you're familiar with.

**Nicolas Lecomte:** So MCP is a big buzzword in the AI community, but what it is essentially is a protocol for LLMs to interact with other stuff.

**Nicolas Lecomte:** And so an MCP server specifically is a server of tools.

**Nicolas Lecomte:** So I was talking about the Google Maps tool, which is probably here somewhere or on another page.

**Nicolas Lecomte:** But you have MCP servers for anything, really, which is a system that you want to expose.

**Nicolas Lecomte:** And MCP is a protocol that standardizes the way that an agent or an LLM would talk to that system.

**Nicolas Lecomte:** So, for example, think of Twilio or Telegram, you know, whatever. You have this server that you can connect to the agent, and that means the agent will be able to access whatever tools are available. You can have a look at what tools are available, and then that gives the tools to the agent.

**Nicolas Lecomte:** And what we do with this feature is we let you host your own custom MCP servers on the platform.

**Nicolas Lecomte:** So again, you don't have to use it. There's a whole bunch of people who don't really want to use MCP. They code the capabilities and the tools of their agents directly in the agent.

**Nicolas Lecomte:** And basically everything is contained in the agent, including the LLM calls. But you can also sort of split it architecturally and use everything. So you see the tools here.

**Nicolas Lecomte:** Apparently, you can notify somebody, send a file, or zip a project.

**Nicolas Lecomte:** But this is custom. You can choose whatever tools.

**Nicolas Lecomte:** You decide which tools you put in your server when you create your server. And again, the reason why we do all of this is for the end-to-end thing.

**Nicolas Lecomte:** So if you want to orchestrate all of this, you don't get a lot of value by just hosting an MCP server. You could do this on any platform like Render, Vercel, Heroku, or AWS.

**Nicolas Lecomte:** There's a whole bunch of serverless hosting platforms. But if you want to have stuff that's integrated with your sandbox and have the full end-to-end, fully optimized setup, this is what it will be good for.

**William Leborgne:** Okay.

**William Leborgne:** Just keeping in mind our time, and also that, I know it's a very quick one, but we're going to need to do a quick publishing walkthrough with you as well in this session.

**William Leborgne:** If we don't get to it, we can always set something up next week.

**William Leborgne:** Not a big deal.

**William Leborgne:** But I did have a couple of other high-level product questions I just want to make sure I hit, because I think they're going to have a big impact on the content.

**William Leborgne:** One of which is, what types of AI agents are customers actually running on Blaxel right now?

**William Leborgne:** Can you give me some examples?

**William Leborgne:** Because that already would help us a lot.

**William Leborgne:** Of course.

**Nicolas Lecomte:** So, the main use case is a coding agent where the end user knows it's a coding agent. Lovable-like products, anything lovable-like.

**Nicolas Lecomte:** We have Webflow as a customer. They just launched their coding platform called AppChain, their coding agent.

**Nicolas Lecomte:** So that runs on us. We have Vibe, Bloom, and a whole bunch of companies that have similar products to Lovable, with different targets and nuances.

**Nicolas Lecomte:** Another example is PR review agents. So it's not the agent that codes, but the agent reviews changes before they get merged into the codebase.

**Nicolas Lecomte:** They run it inside of a sandbox and then they give you suggestions to improve. PR review agents is another example, again, one that works with code.

**Nicolas Lecomte:** Data analyst agents, that's also a big use case. Any agent that needs to work with data. They would generate a script in the background and execute it like a Python script or a SQL query.

**Nicolas Lecomte:** Think of like, you know, all those, there are, you know, a whole bunch of new companies that do, you know, like...

**Nicolas Lecomte:** Analytics through natural language, you know, instead of creating querying points and quick, you can just say, hey, you know, what's the revenue for that product line in 2024 stuff.

**Nicolas Lecomte:** you know, these are examples of AI data analysts.

**Nicolas Lecomte:** These are the main use cases, yeah, that I can, you know, come up with that we traditionally have.

**William Leborgne:** You should talk to my old company, AirDNA, because they're literally looking at that right now.

**William Leborgne:** They're trying to create, because they're a data company for short-term rentals, but they just have an immense amount of data.

**William Leborgne:** And they're trying to figure out how to create sort of an agentic flow, which will then be able to understand the data for, let's say, a certain market.

**William Leborgne:** And then the person can use natural language to ask it questions, and then it'll spit it out.

**William Leborgne:** So, a little tip for you, go after AirDNA.

**Nicolas Lecomte:** Okay, well, I'll continue after, and maybe if have an intro with somebody that you can intro, that would be awesome.

**Nicolas Lecomte:** Yeah, yeah, those are essentially the use cases.

**Nicolas Lecomte:** We have a bunch of use cases from before, but I don't really necessarily want to spend too much time on them, because they're not really the...

**Nicolas Lecomte:** The direction they want to take, like people that only use jobs, I don't think that's what we want to focus on.

**William Leborgne:** I think, yeah.

**William Leborgne:** Do you have hard stop at the half hour?

**William Leborgne:** I do not.

**William Leborgne:** No, I can go a bit over.

**Nicolas Lecomte:** Okay, Kathy, you okay if we go over a bit?

**William Leborgne:** Cool.

**William Leborgne:** All right.

**William Leborgne:** How should we think about agent hosting versus sandboxing?

**William Leborgne:** Is this one product or are these two products?

**William Leborgne:** And I would say this is a broader question.

**William Leborgne:** Are you splitting up Blaxel's product or features into different pieces?

**William Leborgne:** Or is it really one unified product that you're selling?

**Nicolas Lecomte:** No, we sell it as a platform with at least two products.

**Nicolas Lecomte:** So I would say sandboxes, guess those are the two main products.

**Nicolas Lecomte:** And then, you you could argue that even the agents and jobs is like a specific sub products.

**Nicolas Lecomte:** don't, but let's simplify and say that it's, you know, one main product, which is sandboxes and one main product, which is everything related to the hosting.

**Nicolas Lecomte:** And so we do both.

**Nicolas Lecomte:** I would say it's sandboxes first.

**Nicolas Lecomte:** Sandboxes is the core offering.

**Nicolas Lecomte:** With the option.

**Nicolas Lecomte:** option.

**Nicolas Lecomte:** Of using hosting, I don't want it to sound like you have to use hosting for sandboxes, because again, most people will just arrive and they need to short term, you know, fix up sandboxes.

**Nicolas Lecomte:** And then we upsell through hosting.

**Nicolas Lecomte:** For us, it's more because we can't limit ourselves to sandboxes.

**Nicolas Lecomte:** We need to have, you know, we need to obviously grow usage and stuff.

**Nicolas Lecomte:** And the customer, the more the customer uses, the harder it is for them to get out essentially, but also the more value they get because they, we can optimize much more.

**Nicolas Lecomte:** So, so yeah, for us, it's two different products.

**Nicolas Lecomte:** And we, we, we, in the value prop, you know, that, that we say, it's like, okay, how do we let you achieve, like, the highest speed possible?

**Nicolas Lecomte:** It's, you can keep infinitely many sandboxes on standby, while also hosting your agent next to your sandboxes for no network overhead.

**Nicolas Lecomte:** Got it.

**Nicolas Lecomte:** Got it.

**William Leborgne:** All right.

**William Leborgne:** Great.

**William Leborgne:** Okay, I have a couple questions around like customer voice, specifically things like what do customers say when they switch over to Blaxel?

**William Leborgne:** Is there anything that they specifically stand on?

**William Leborgne:** I think this came up a little bit in our last conversation because you had talked about another client that had come.

**William Leborgne:** I think it was lovable maybe because the security was an issue.

**William Leborgne:** I think it was Webflow.

**William Leborgne:** Yeah, was Webflow.

**Nicolas Lecomte:** We unfortunately do not have lovable, though I would love to, but they're working with Modal, which is a competitor.

**Nicolas Lecomte:** But yeah, security is one big thing.

**Nicolas Lecomte:** Often people, I mean, what will make somebody switch from a competitor is usually downtime, if they have a reliability issue.

**Nicolas Lecomte:** And so that was the main thing for Webflow.

**Nicolas Lecomte:** That was the main reason they would switch from something that they prototyped on their end, either...

**Nicolas Lecomte:** By themselves, like building in themselves or on another vendor is reliability.

**Nicolas Lecomte:** They have reliability issues.

**Nicolas Lecomte:** It's a big no-no.

**Nicolas Lecomte:** Support is also like something that's very important, making sure that as an infra business, we're able to assist customers when they need.

**Nicolas Lecomte:** And then I think for people, if people come to us for the first time, which is different than if they already tried and failed to implement sandboxes, if that makes sense.

**Nicolas Lecomte:** If they come to us for the first time, I think it's really about when they get, I think there's something that happens when they get that, there is this sort of like automated lifecycle that happens where they can just create a sandbox and they don't think about it and then it stops using compute when they don't use it.

**Nicolas Lecomte:** They don't have to think about turning it off and deleting it and turning it back on and then they reconnect to it and then it goes back up.

**Nicolas Lecomte:** You know, that's general serverless practice.

**Nicolas Lecomte:** But the fact that it's all so fast that...

**Nicolas Lecomte:** The shutdown happens one second after inactivity, basically.

**Nicolas Lecomte:** Well, don't necessarily quote me on the one second because we're thinking of extending this to 15 seconds to increase usage a bit.

**Nicolas Lecomte:** But, you know, it shuts down almost instantly and then it turns back on in 25 milliseconds.

**Nicolas Lecomte:** So for then, everything is instant and the app resumes exactly how it was.

**Nicolas Lecomte:** So as soon as anybody reopens that preview that I never made work in my demo, it would reappear immediately like it was before.

**Nicolas Lecomte:** So I think the speed and ease of setting up something that is so fast is what they would be very happy to see.

**Kathy Lam:** So is there a huge, like, number of people who are using AWS switching to Blaxel just because that capability to very quickly, yeah, just very quickly have so many sandboxes and not have it continue to run compute and all that?

**Kathy Lam:** Debt.

**Kathy Lam:** Yeah, yeah, yeah.

**Nicolas Lecomte:** Yes, there are.

**Nicolas Lecomte:** What's interesting is that among the new companies that get created, you see less and less people using AWS, which is also interesting.

**Nicolas Lecomte:** Younger founders or new companies usually immediately go to more modern platforms, like maybe Vercel or Render.

**Nicolas Lecomte:** Webflow, I think, runs on AWS, so that's an older company. But if you're trying to set it up on AWS, you literally have no way to set up something that shuts down so fast and spins back up so fast with those kinds of performances.

**Nicolas Lecomte:** It's very, very hard.

**Nicolas Lecomte:** I would say for the people that we talk to, it's about half and half between people who prototyped by themselves on a cloud and people who tried a vendor.

**Nicolas Lecomte:** Maybe half and half, or maybe two thirds have tried a competitor sandbox provider.

**William Leborgne:** Okay, here's a broader question.

**William Leborgne:** What's surprisingly hard about using Blaxel?

**William Leborgne:** Like, what do customers sometimes struggle with?

**Nicolas Lecomte:** The onboarding experience. The onboarding experience is something that we're not really good at. We have to set up a Slack channel with customers to make sure we can respond whenever they have a question—we respond in one minute. But it's probably because it's not yet extremely intuitive. People wonder, "How do I get started? What do I do? What's the best way?" We're improving on this, and it's our key focus over the past month or two. It's getting better, but that's one area where people struggle for sure—those first few steps on Blaxel.

**William Leborgne:** Okay, we are really coming up on time, so I'm going to wrap it up. I think we got a lot of really good stuff. I can go 10 minutes if you want, but I don't really have that.

**William Leborgne:** I guess I just have two guardrail questions. Are there any phrases or words that we need to make sure we avoid when we discuss your product? Or any claims that could be legally dubious? Anything that comes up for you?

**Nicolas Lecomte:** There is one that comes to mind on the language specifically of sandboxes. I think we want to be careful to not call them containers because that's a mistake that is easily made. "Container" can be thought of abstractly as an environment that contains stuff, but it also has a very precise meaning in infrastructure—a virtual container technology—which is not what we use.

**Nicolas Lecomte:** Our sandboxes are based on micro VMs and not containers. I think we want to be careful about what Blaxel is. The latest positioning work we've done has coined the category of "perpetual sandbox platform." A year ago, there was no category of sandbox providers, which is crazy.

**Nicolas Lecomte:** In the past year, it's become very popular. People know that sandbox providers are a thing now. We're not just a sandbox provider; we're the only perpetual sandbox provider where you can keep your sandboxes on standby forever without deleting them after you use them. That's why we get such good performance. We should focus on that language instead of saying we're a framework. A framework in the agentic world is something very precise—like LangChain or Google ADK. We're not a framework.

**Nicolas Lecomte:** We're not an agent platform.

**Nicolas Lecomte:** I think, I don't know, regarding agent platform, and then, you know, after that, we were an agent platform, but it's very broad, but specifically, yeah, we're not a framework, and we don't do containers.

**Nicolas Lecomte:** So I can try to think if I think of some others.

**Nicolas Lecomte:** Sure, sure, sure.

**William Leborgne:** And you'll have this notion doc, so you'll see all the other questions that we didn't get through.

**William Leborgne:** Some, you'll be like, oh, yeah, this is a good one.

**William Leborgne:** Some, you'll be like, no, I don't want to answer this, and that's perfectly fine.

**William Leborgne:** And last one on this is, like, because this is so very relevant, you know, relevant.

**William Leborgne:** It's to what we just talked about.

**William Leborgne:** We're talking about like what not to call it.

**William Leborgne:** When you are talking to people about this, do you ever use any like analogies or any phrases or even metaphors to explain what Blaxel is to somebody who may not completely understand it immediately?

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** You know, other ways to think about it is infrastructure, you know, computing infrastructure that, you know, if somebody doesn't know that, I guess sandbox platforms are known in the coding agent builder's space, but not everybody knows what a sandbox is.

**Nicolas Lecomte:** So yeah, infrastructure, cloud infrastructure, computing infrastructure, cloud for agents.

**Nicolas Lecomte:** That was our previous tagline before we did this work was AWS for agents.

**Nicolas Lecomte:** We were like, okay, we're, we're building the AWS for the agents as in, you know, for agents to use.

**Nicolas Lecomte:** AWS was built for humans to build SaaS, we're building Blaxel for agents to use to run whatever they want.

**Nicolas Lecomte:** And it had the dual meaning of, you know, you can also host your agents like it was for running agents, not just for them to use it.

**Nicolas Lecomte:** So that's something that we can say that's maybe more higher level.

**Nicolas Lecomte:** I like sometimes as well to say, guess this is when the person is very non-technical to say, that the computers, you know, the computer analogy that I said, you know, you want to give, you would give somebody a computer for them to do work, you would give an agent computer for the agents to do work efficiently.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Yeah, those are the ones I can think of.

**Nicolas Lecomte:** Okay.

**William Leborgne:** Anything else, Kathy, that we want to make sure we okay, good.

**William Leborgne:** Let's go ahead and if it's okay, switch over to your CMS.

**William Leborgne:** And if you want to give us a quick walkthrough of how you would publish

**Nicolas Lecomte:** This will be a live demo because we, so we're in the process of getting Strapi as a customer and I think they should launch on us very, very soon.

**Nicolas Lecomte:** So for that reason, we, to make it easier for them to say yes, we migrated from Sanity to Strapi as a CMS at the beginning of the week.

**Kathy Lam:** So I'm kind of new to it.

**Nicolas Lecomte:** I'll be very honest with you.

**Nicolas Lecomte:** We migrated all the articles.

**Nicolas Lecomte:** We didn't have a lot of articles, but we migrated everything.

**Nicolas Lecomte:** Yeah, I think I invited PodZero to the instance, I think, yesterday.

**Nicolas Lecomte:** But yeah, so this is the, are you guys familiar with Strapi?

**Nicolas Lecomte:** Is this something that you've worked with before?

**William Leborgne:** No.

**William Leborgne:** No?

**William Leborgne:** Okay.

**Nicolas Lecomte:** So, I mean, I think it's fairly intuitive.

**Nicolas Lecomte:** So yeah, this is the admin panel, which I think I invited you to.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** So inside of the content manager, this is where we'll find everything.

**Nicolas Lecomte:** So authors, categories, versus what we're saying last time, we'll need to figure out how we publish you guys' content.

**Nicolas Lecomte:** I had those tags set up where news, case studies, engineering, which is the engineering blog that we talked about last time, and then guides, where I was thinking maybe you guys can sort of publish under the umbrella of the guides, and then we find a way in the UI to display it.

**Nicolas Lecomte:** Maybe that's what would make the most sense.

**Nicolas Lecomte:** And then posts are all here.

**Nicolas Lecomte:** So yeah, we have about like 10 or 15 specifically.

**Nicolas Lecomte:** And then yeah, usually what I will do is, I will write it on the side.

**Nicolas Lecomte:** You know, if I have to write something myself, I'll write it on the side, maybe Notion or Google Docs.

**Nicolas Lecomte:** I think our content writer uses Google Docs.

**Nicolas Lecomte:** And then paste everything here.

**Nicolas Lecomte:** So title, slog, excerpt, main image.

**Nicolas Lecomte:** We need to figure out a flow for the main image.

**Nicolas Lecomte:** How do we give you guys illustrations?

**Nicolas Lecomte:** I'm also open to suggestions of how you guys have worked in the past with people to get those assets.

**Nicolas Lecomte:** We add the read time, which I think is in that format, four minutes to read, and then the body.

**Nicolas Lecomte:** So it's full markdown.

**Nicolas Lecomte:** You can format it like that, and then you can preview it.

**Nicolas Lecomte:** So we'll start the rendering here.

**Nicolas Lecomte:** TLDR is a custom section, which allows you, so I can show you on the blog, TLDR lets you, it's optional on an article, but it, oh God.

**Nicolas Lecomte:** It lets you, I don't know if I want.

**Nicolas Lecomte:** So yeah, I think it's an example where there is not one.

**Nicolas Lecomte:** So this would be the article and they would have basic metadata here.

**Nicolas Lecomte:** And then if I find one that has, I think maybe this one has a TLDR.

**Nicolas Lecomte:** So yeah, if there is a TLDR, it will.

**Nicolas Lecomte:** So.

**Nicolas Lecomte:** Or go here.

**Nicolas Lecomte:** I see.

**William Leborgne:** Okay.

**William Leborgne:** Yep.

**Nicolas Lecomte:** So yeah, again, optional, author, choose an author, choose a category.

**Nicolas Lecomte:** So I think in your case, guides would be where you guys go.

**Nicolas Lecomte:** Tags.

**Nicolas Lecomte:** I forgot what that is.

**Nicolas Lecomte:** I don't know if we use it.

**Nicolas Lecomte:** Do we use that?

**Nicolas Lecomte:** Let me have a look.

**Nicolas Lecomte:** I don't think we do.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** And so do you have a place to add meta description, meta title, schema markup?

**William Leborgne:** Well, so I think that would be here.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** So SEO, you're thinking FCO.

**William Leborgne:** Yeah.

**William Leborgne:** Meta description keywords.

**Nicolas Lecomte:** If there are more, I think we can probably add them.

**Nicolas Lecomte:** Okay.

**William Leborgne:** Yeah.

**William Leborgne:** The only thing I'm seeing that's missing is schema, which we want to make sure we include as well.

**William Leborgne:** Okay.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** I'm going to have a look if this is something that we need to add custom or if they have it.

**Nicolas Lecomte:** And user, what is user?

**Nicolas Lecomte:** I don't know.

**Nicolas Lecomte:** So yeah.

**Nicolas Lecomte:** This is literally the only thing that the posture, so yeah, pretty simple on that, and then we publish, and so as soon as, so you can save locally, so this will create a draft inside of Strapi, does it, or it's second page, okay, yeah, so this creates a draft that you can come and edit, and then as soon as you hit publish, it will bring it on production, like on the live website production version.

**William Leborgne:** Okay, well that's good, yeah, we don't have to do like a push on the website, and for imagery, any kind of media, anything like that, that's just within the, the rich text editor, in the body, correct?

**William Leborgne:** Yes.

**Nicolas Lecomte:** Yeah, okay, great.

**William Leborgne:** Yeah, pretty straightforward.

**William Leborgne:** Super.

**William Leborgne:** By the way, I just realized, I never introduced Kathy, I apologize, Kathy is another managing director, like myself.

**William Leborgne:** She started quite recently, and she has a very technical background as well.

**William Leborgne:** So everything you're talking about, she has much far deeper understanding than I do.

**William Leborgne:** Okay.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Nice to meet you, Kathy.

**Nicolas Lecomte:** So how does that work?

**Nicolas Lecomte:** So the team that we'll work with is you, William, you, Kathy, George, plus other people?

**William Leborgne:** George is going to hand this off.

**William Leborgne:** So it'll be primarily Kathy and I.

**William Leborgne:** And then there's going to be another person that's going to be brought in who's going to be really the content strategist, who's going to be really focused more on the execution of the content and the publishing and everything else.

**William Leborgne:** While, you know, Kathy and I are really, I would say, more generally focused on the strategy and making sure that you're getting exactly what you need.

**William Leborgne:** Okay.

**Kathy Lam:** That makes sense.

**Kathy Lam:** Okay.

**William Leborgne:** Awesome.

**William Leborgne:** Well, yeah.

**Nicolas Lecomte:** Great to meet you guys.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** Excited to, like, start working with you.

**Kathy Lam:** Yeah.

**Nicolas Lecomte:** It's amazing.

**William Leborgne:** Well, I shared this with you in the, in the.

**William Leborgne:** So feel free to jump in at any point to look through some of the questions that we maybe did not get through.

**William Leborgne:** If you want to add some comments or anything like that, any additional details.

**William Leborgne:** And also, if there's something unrelated to this, feel free to, you know, put whatever information you want.

**William Leborgne:** Obviously, we have this recording as well, which is super helpful.

**William Leborgne:** We're going to take all of this information and create a product matrix as well as the sort of deep dive on the product.

**William Leborgne:** And as I mentioned, this is all going to be then converted into a product artifact, which will go into our pipeline.

**William Leborgne:** Okay.

**William Leborgne:** All right.

**William Leborgne:** Well, thank you so much, Nico.

**William Leborgne:** I really appreciate your time.

**William Leborgne:** Of course.

**William Leborgne:** Yeah.

**Nicolas Lecomte:** Thank you.

**Nicolas Lecomte:** Thank you, guys.

**Nicolas Lecomte:** Appreciate yours, too.

**Nicolas Lecomte:** And yeah.

**William Leborgne:** Let's have a look at the document.

**Nicolas Lecomte:** can access it.

**Nicolas Lecomte:** So yeah, we are meeting next Friday, I believe.

**William Leborgne:** And by yes, we are.

**Nicolas Lecomte:** I won't be able to be there before my co-founder and CEO that you met last time will be here.

**Nicolas Lecomte:** So it will be the meeting.

**Nicolas Lecomte:** getting married on that day, so I'd like to Oh, wow.

**Kathy Lam:** Congrats.

**Nicolas Lecomte:** Thank you.

**Nicolas Lecomte:** Are you going to go for a honeymoon shortly after, or are you going to do that on Christmas?

**Nicolas Lecomte:** Just a weekend, a very, very mini honeymoon over the weekend, and then I'll probably plan this next year sometime, yeah.

**Nicolas Lecomte:** Congratulations again.

**Nicolas Lecomte:** It's Christmas, so I guess, yeah.

**Nicolas Lecomte:** Are you getting married in France or in New York?

**William Leborgne:** Yeah, in France, yeah, in Paris.

**Nicolas Lecomte:** And this is the civil wedding, and then we'll plan a more party and stuff next summer.

**Nicolas Lecomte:** We want it for, amongst other things, visa reasons, to the wedding as early as possible.

**Nicolas Lecomte:** That's fantastic.

**Kathy Lam:** Well, congrats.

**William Leborgne:** Thank you.

**Nicolas Lecomte:** Yeah, thank you.

**Nicolas Lecomte:** Thank you, guys.

**Nicolas Lecomte:** But yeah, so I won't see you next week, and I believe I think our next session will be early Jan.

**William Leborgne:** Yeah, early Jan, exactly.

**William Leborgne:** Yep, yep.

**William Leborgne:** Okay.

**William Leborgne:** Well, so if you do talk to Paul, just let him know that we're working on all these artifacts, including this one.

**William Leborgne:** We'll get all those.

**William Leborgne:** Done early next week, then we will start the content production process.

**William Leborgne:** And so what that looks like is we're going to create an initial article, which you will then review.

**William Leborgne:** It's called a calibration article.

**William Leborgne:** And you'll be able to review it, see if this fit what we're trying to do.

**William Leborgne:** This is our voice.

**William Leborgne:** Is this representing our product correctly?

**William Leborgne:** Go back and forth however much we need to to make sure it's at the standard that you need.

**William Leborgne:** Because once we have it at the standard that you need, then we turn on the engines.

**William Leborgne:** And we start to really produce a lot of content.

**William Leborgne:** So by the...

**William Leborgne:** ahead.

**Nicolas Lecomte:** No, I guess my only question was, and then I assume we'll have regular, you know, syncs called...

**William Leborgne:** Yeah, everywhere.

**Nicolas Lecomte:** ...all to be like...

**Nicolas Lecomte:** So, you know, if we want to...

**Nicolas Lecomte:** Because I assume you guys will be like, okay, maybe we should write about this.

**Nicolas Lecomte:** Maybe we should write about this.

**Nicolas Lecomte:** And then maybe we'll be like, you know, for example, what I was saying about how you can use sandboxes for data analysis agents, which is a sort of emerging use case, you know.

**Nicolas Lecomte:** You know, we can be like, okay, it could be great if we produce some content around, you know, how sandboxes are so great for data analysis agents.

**Nicolas Lecomte:** Like, I guess, how do you guys usually work the, you know, choosing the directions that we go to, like, with your suggestions and our suggestions, how does that usually work?

**William Leborgne:** Yeah, so your suggestions, I think, are going to be really pivotal because you have the ear to the ground.

**William Leborgne:** You know the customers better than we do, and you also know the future of the product and of your industry.

**William Leborgne:** So I think that's really, really crucial for us information-wise.

**William Leborgne:** Our perspective is always going to be driven by data, meaning that we're going to look at, like, what is currently being searched for and look for those options where it's, you know, low keyword difficulty, where we have the best ability to rank and to start to drive meaningful traffic, impressions, visibility.

**William Leborgne:** Because that was one of the core things that you guys talked about is, like, our biggest issue at BlackSoul is people don't know about us.

**William Leborgne:** So that's what we got to fix,

**William Leborgne:** Right?

**William Leborgne:** So we're looking at that.

**William Leborgne:** It's going to be very data-driven.

**William Leborgne:** And when we come to you next Friday with this content strategy, it's going to have a number of keywords and suggested pieces of content around that that's all data-backed, all behind what's being searched for in Google as well as LLMs.

**William Leborgne:** And then your perspective on like, hey, I think we should also be doing this type of content.

**William Leborgne:** That's in addition.

**William Leborgne:** So they're not competing.

**William Leborgne:** They're kind of stacking on top of each other.

**William Leborgne:** That makes sense.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Awesome.

**Nicolas Lecomte:** Great.

**William Leborgne:** Cool.

**William Leborgne:** Super.

**William Leborgne:** All right, guys.

**William Leborgne:** Thank you so much.

**William Leborgne:** Talk to you soon.

**William Leborgne:** Bye-bye.
