# Elementum product deep dive

<metadata>
date: 2026-02-18
time: 18:00 UTC
duration: 32 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević (GrowthX), Andrew Bennett (Elementum), Vlad Usatin (Elementum), Kyle Westwood (Elementum)
fathom_recording_id: 123425581
fathom_url: https://fathom.video/calls/570075963
share_url: https://fathom.video/share/Gjaftdj77W9kEb-EnFKefMRyZiNi9pf6
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Vlad Usatin and Andrew Bennett gave GrowthX a comprehensive product walkthrough of Elementum, demonstrating how the platform combines deterministic workflows with probabilistic AI agents to create a unified corporate "front door." The demo showed Elementum's three-persona model (employees submitting requests, builders creating workflows, fulfillers actioning requests) and key differentiators: agent-agnostic architecture (bring-your-own LLM contracts), data-agnostic deployment (lives in customer's cloud like Snowflake with no data export), and cost optimization through selective agent use (sophisticated models for complex tasks, cheaper models like DeepSeq for simple work). Key takeaway for content: the "only use agents where you need them" messaging is resonating strongly with CIOs and represents a powerful counter to AI overuse in enterprise workflows.

---

## Context

GrowthX is preparing to produce significant content and marketing material about Elementum as part of a broader content engagement. Aida Knežević led the call to deepen GrowthX's product understanding before beginning content creation. Elementum (represented by Vlad Usatin, VP/founder, and Andrew Bennett, Head of Sales) is positioning itself at the intersection of traditional workflow automation and modern agentic AI—solving for enterprise reliability, auditability, and compliance concerns that pure LLM tools and legacy workflow systems fail to address. Andrew noted that Elementum had already conducted onboarding calls with GrowthX covering overall company positioning and messaging, and this call was specifically focused on product architecture and capabilities. The timing was important for content accuracy: Elementum was actively refining its messaging around selective agent use and cost optimization.

---

## Relevance

**To GrowthX Delivery:**
- Core messaging opportunity: "Only use agents where you need them" is resonating strongly with enterprise CIOs and directly counters the industry-wide criticism of AI overuse. This is a powerful differentiator to feature in all content.
- Product architecture requires explaining three distinct user personas (employee, builder, fulfiller) across multiple channels (web, Slack, Teams, phone, SMS)—content must demonstrate this unified experience vs. fragmented systems.
- Compliance and data governance are key selling points (HIPAA-enabled, GDPR-compliant via in-cloud deployment in customer's Snowflake/Databricks)—content should emphasize "no data export" as security moat.

**To CheckThat:**
- Elementum's agent-agnostic architecture (bring-your-own LLM contracts) is directly relevant to AI visibility and LLM selection strategies—prompt auditing for cost optimization is a natural fit for CheckThat's value prop.
- The demo highlighted cost analytics tracking spending per agent provider—this is a CheckThat use case worth exploring.

**To GrowthX Business Development:**
- High-confidence prospect fit: regulated industries (pharma, insurance explicitly mentioned) are primary targets, suggesting expansion into those verticals.
- Aida identified key messaging leverage: positioning Elementum as solving the "you're using AI for things it doesn't need to be" criticism—this has broad appeal across enterprise software buyers.

---

## Overview

- **Hybrid Workflow Engine:** Elementum combines deterministic logic with probabilistic AI agents, using deterministic guardrails to ensure agent reliability and auditability—a key differentiator from pure LLM tools.
- **Agent & Data Agnostic:** The platform is "Switzerland" for agents and data. Customers use their own LLM contracts (e.g., OpenAI, Anthropic) and Elementum runs directly in their existing data cloud (e.g., Snowflake), ensuring data security and compliance.
- **Unified Corporate Gateway:** A single chat interface acts as a "front door," routing complex, multi-system requests (e.g., PTO, contract processing) to the correct backend systems, replacing fragmented user experiences.
- **Cost-Optimized AI:** The platform enables cost control by allowing users to select the most efficient agent for each task. This means using expensive, sophisticated models only when necessary and cheaper, lighter-weight models for simpler jobs.

---

## Key Topics

### The Problem: Unreliable AI & Fragmented Workflows

  - **Pure LLMs (e.g., ChatGPT):** Unreliable for enterprise workflows due to their probabilistic nature, making them hard to audit and govern.
  - **Traditional Workflow Tools (e.g., ServiceNow):** Their agent integrations are often bolt-ons, lacking native, reliable AI capabilities.
  - **Result:** A fragmented user experience where employees must navigate multiple systems (Workday, SAP) and internal agents for simple tasks.

### The Solution: Elementum's Hybrid Platform

  - **Core Architecture:** Combines deterministic logic (for routing, branching) with probabilistic AI agents (for complex tasks like parsing).
  - **Deterministic Guardrails:** Agent tasks are "sandwiched" by deterministic logic, ensuring reliability, auditability, and compliance.
  - **Unified Chat Interface:** A single entry point (web, Slack, Teams, phone) for all corporate actions.
      - **Demo:** A single prompt ("Process this contract... take PTO... requisition a new laptop") triggered three separate workflows.
      - **Outcomes:**
          - **PTO:** Sent to a manager for approval.
          - **Contract:** Parsed for key data (terms, costs) and sent to legal for review.
          - **Laptop:** Created a requisition in the IT system.

### Platform Personas & Capabilities

  - **1. Employee (User):**
      - Interacts via a simple chat interface to submit multi-system requests.
  - **2. Builder (Developer):**
      - Creates workflows using a drag-and-drop interface or an agent-driven builder.
      - The agent builder asks questions to generate workflows, including triggers (green), agent tasks (purple), and deterministic logic (blue).
  - **3. Fulfiller (Actioner):**
      - Uses a traditional UI to review and action requests.
      - **Contract Example:** Legal reviews a pre-parsed contract, quickly providing feedback on specific terms.
      - **PTO Example:** A manager approves a PTO request, which then updates the calendar.

### Key Differentiators: Agnostic & In-Cloud

  - **Agent Agnostic:**
      - Customers "bring their own agent" via API keys, leveraging their existing contracts and privacy clauses with providers like OpenAI and Anthropic.
      - This avoids vendor lock-in and allows users to select the best agent for each task.
  - **Data Agnostic (In-Cloud):**
      - Elementum runs directly in the customer's existing data cloud (e.g., Snowflake, Databricks).
      - **Why it matters:**
          - **Security:** Data never leaves the customer's environment.
          - **Compliance:** Simplifies adherence to regulations (HIPAA, GDPR) as Elementum doesn't store data.
          - **Performance:** Real-time access to data enables faster, more efficient workflows.

### Platform Governance & Cost Control

  - **Full Platform Features:** Includes role-based access, version control, and comprehensive analytics.
  - **Auditability:** Logs all conversations and actions, flagging out-of-policy activity in real-time.
  - **Cost Analytics:** Tracks spending per agent provider, enabling cost optimization.
  - **Optimized Agent Use:** The platform encourages using the most cost-effective agent for each task.
      - **Example:** Use a sophisticated model (e.g., Opus 4.5) for complex analysis, but a cheaper, lighter-weight model (e.g., DeepSeq) for simple tasks.

---

## Action Items

- **Aida Knežević (GrowthX):** Use the product deep dive to inform accurate and compelling content creation. Focus on the "selective agent use" and cost optimization messaging, along with the three-persona workflow model.
- **Andrew Bennett (Elementum):** Finalize and share the updated messaging framework with Aida, emphasizing the comparison between Elementum's deterministic + agentic hybrid approach and pure LLM or legacy workflow tools.

---

## Transcript

**Vlad Usatin:** I knew that. I said your name wrong. I said Aida. The meeting is being recorded.

**Aida Knežević:** Yeah, Aida is how it's pronounced in my native language, but when I speak English, I default to Aida. I think it's easier for people to pronounce.

**Vlad Usatin:** Very cool. All right, so I got it right. In Russian, you would be Aida as well.

**Aida Knežević:** Yeah, so you don't have issues pronouncing it then. That's good. Thank you for jumping on today. So today we were just hoping to get a product demo and I would ask a couple of follow-up questions.

**Andrew Bennett:** Hi, Aida.

**Aida Knežević:** Hi, Andrew.

**Andrew Bennett:** How are you doing?

**Aida Knežević:** Good.

**Aida Knežević:** Good.

**Aida Knežević:** I was just explaining to Vlad what we're kind of here to do today just to give a little bit of context.

**Aida Knežević:** Um, but yeah, it's just like a product demo explaining.

**Aida Knežević:** We want to understand how the platform works because we're going to be writing a

**Aida Knežević:** lot of content related to the platform, so we want to make sure that it's accurate from a product perspective, and that we also understand how it works so that, you know, we know what we're writing about.

**Aida Knežević:** So, yeah, I think that, is that helpful?

**Andrew Bennett:** I'm happy to answer any other questions.

**Andrew Bennett:** Yeah, and Vlad, just a little more context.

**Andrew Bennett:** So, we've done a few onboarding calls with GrowthX already, so we had Nader on a few days ago, sort of covering overall sort of company story and positioning, so it already has all that context.

**Andrew Bennett:** They've done a lot of work documenting the sort of the company positioning and ICP and the like, so this is, yeah, just showing the product.

**Vlad Usatin:** All right, let's show you what we got. So I'm going to share my screen. I'm just turning off all the noise.

**Andrew Bennett:** All right, no problem.

**Vlad Usatin:** All right. Here we go. So I know maybe Nader already kind of given the background of the app, but I'll still give you just a tiny framing in terms of where we are. So where we are, we fulfill this kind of sweet spot, the Goldilocks intersection spot between building traditional workflows, which is simplified low-code or no-code workflows. So we build workflows with agents in the middle, and that's what you kind of see here right now on my screen.

**Vlad Usatin:** So the classic way, or at least a lot of people today have a choice.

**Vlad Usatin:** Do they go with something like Google or they go with Copilot or they go with Anthropic or ChatGPT alone?

**Vlad Usatin:** And in those cases, they wind up getting an agent, and they write paragraphs of text, and it kind of works.

**Vlad Usatin:** It's great for maybe if you have some questions and answers, but if you want to build any business-centric workflow, especially in regulated industries, they don't do the same thing every time, and it's very difficult to audit what they do.

**Vlad Usatin:** So unlike traditional code where you can step through it...

**Vlad Usatin:** That block of text just gets absorbed into those billions of parameters of the GPT or whatever the LLM behind the scenes is, and it just doesn't work for American enterprise.

**Vlad Usatin:** Then on the flip side, we have these traditional players like ServiceNow or UiPath, which build regular workflows, and they've been around for years.

**Vlad Usatin:** And recently, they started adopting agents into their workflow, but they're kind of bolt-on, and we really fit into the spot natively because we coincidentally started building out our platform when agents came online.

**Vlad Usatin:** So we have this, what you see on the screen, an example of a traditional workflow with an agent in the middle.

**Vlad Usatin:** So this is a workflow for an employee coming in and asking for, hey, can I take a beer?

**Vlad Usatin:** It's your request, which gets routed to an agent.

**Vlad Usatin:** Once agent processes it, then we go ahead and put it back into a workflow that goes ahead, make sure that the response matches our expectations and then writes it out to the system like Workday.

**Vlad Usatin:** And what this is, this is a gateway for, puts us into a very good position to be a gateway for corporate actions.

**Vlad Usatin:** So there's a lot of, there's a sprawl of agents, even though they're not performing well.

**Vlad Usatin:** There's still a lot of agents.

**Vlad Usatin:** if you remember back in the day, there were a lot of websites.

**Vlad Usatin:** People would have internal websites and then they would start building portals.

**Vlad Usatin:** So we have this portal for agents.

**Vlad Usatin:** So instead of having this wild, wild jungle of agents all over the place, one in Workday, one in SAP, one in you name it.

**Vlad Usatin:** So everyone has an agent these days.

**Vlad Usatin:** We allow companies to create not only just these deterministic workflows, we're well positioned to create this front door or the golden entry for organizations to have us as a front door where we route to their agent, get the response back, and then create this unified front door.

**Vlad Usatin:** So what I'm going to begin, I'm going to show you three different personas.

**Vlad Usatin:** So the first persona is your traditional corporate workers.

**Vlad Usatin:** It's like us.

**Vlad Usatin:** So you may want to ask for a PTO.

**Vlad Usatin:** You may want to submit some contract.

**Vlad Usatin:** Let's say we are your customer, right?

**Vlad Usatin:** We have a contract that you need to go ahead and put in through your system and or anything else.

**Vlad Usatin:** For example, get a new laptop, right?

**Vlad Usatin:** So these are the things I'm going to do.

**Vlad Usatin:** So we provide this.

**Vlad Usatin:** Front door.

**Vlad Usatin:** Looks like ChatGPT, right?

**Vlad Usatin:** But behind the scenes, we're not the authority.

**Vlad Usatin:** We, just like a portal, we'll have you go to sports, weather, and whatever else you'll have in your portal.

**Vlad Usatin:** We do this at a corporate level, and we are focusing in this case on agentic workflows.

**Vlad Usatin:** Obviously, the other thing that we do, we also allow to replace existing systems like ServiceNow or Workday with an agent.

**Vlad Usatin:** So whether it's kind of a pass-through or just a true new way to consume them.

**Vlad Usatin:** But at the end of the day, the front door is just a text box like this in this web browser, or it could be Slack, or it could be Teams, or it can be even a phone call, right?

**Vlad Usatin:** So they ultimately lead all to the same front door within Elementum that routes the requests, right?

**Vlad Usatin:** So what I'm going to do now is I'm going to show you how it works.

**Vlad Usatin:** So I'm going to go ahead and pull up a contract. And I'm going to say, process this contract, period.

**Vlad Usatin:** Also, I want to take PTO, March 1st through 5th, and my laptop is old, so can you put in requisition for a new laptop?

**Vlad Usatin:** So I dictated it here just to demonstrate it.

**Vlad Usatin:** Again, this is not Elementum feature.

**Vlad Usatin:** That was just my MacBook feature.

**Vlad Usatin:** But we do have a phone number that you can dial in, and it would be very similarly input into it.

**Vlad Usatin:** You can, they're very intelligent.

**Vlad Usatin:** It will be able to...

**Vlad Usatin:** Also, just a quick peek, what this contract looks like, right?

**Vlad Usatin:** So this is kind of your classic contract with money and payment terms, right?

**Vlad Usatin:** So something that typically would require a human to go ahead and process.

**Vlad Usatin:** So it processes it.

**Vlad Usatin:** It puts it into the appropriate system.

**Vlad Usatin:** So the PTO request goes into, well, it goes into approval cycle.

**Vlad Usatin:** So we have an approval cycle before with a human in the loop.

**Vlad Usatin:** The contract goes into our contracting system.

**Vlad Usatin:** And then my request for a laptop goes into our IT system that does hardware, right?

**Vlad Usatin:** So for any modern corporation that needs this intersection of deterministic workflows, agentic workflows, and human in the loop, we bring this all together in one system.

**Vlad Usatin:** So this is...

**Vlad Usatin:** This is it, right?

**Vlad Usatin:** So it's that simple.

**Vlad Usatin:** I could have done three different requests.

**Vlad Usatin:** could have had a Q chat, but it really replaces not only going to three different agents or maybe two agents and a traditional user interface.

**Vlad Usatin:** And it gives you a single quick way to do this through a variety of methods.

**Vlad Usatin:** And again, I'm just doing it here in a web browser.

**Vlad Usatin:** We can do it through anything, SMS, Teams.

**Vlad Usatin:** I already said those things.

**Vlad Usatin:** All right.

**Vlad Usatin:** So that's persona one.

**Vlad Usatin:** So just a traditional corporate employee like us having a pleasant working experience.

**Vlad Usatin:** Second persona is a builder.

**Vlad Usatin:** So how do you make all this happen, right?

**Vlad Usatin:** So we started off with kind of a drag and drop interface, which was pretty easy.

**Vlad Usatin:** So, for example, when somebody uploads, it begins when you upload a PDF file, go ahead and look inside of it, extract the content, and you kind of, as I'm narrating, you would drag and drop blocks.

**Vlad Usatin:** With an agent, as if you're planning a trip to Italy or wherever you want to go, and it starts asking you questions, what do you like?

**Vlad Usatin:** In this case, it would ask you questions about what you're trying to build.

**Vlad Usatin:** So in this case, again, we're building an IT service management system.

**Vlad Usatin:** I'd ask you what I want to do.

**Vlad Usatin:** So I'm going to pick, I'm going to try to do maybe a small component of it.

**Vlad Usatin:** I'm going to hit submit.

**Vlad Usatin:** It's going to start working on the first module of it.

**Vlad Usatin:** It may ask me some follow-up questions.

**Vlad Usatin:** How, for example, I want to interact with it.

**Vlad Usatin:** So perhaps I want to do these first three use cases.

**Vlad Usatin:** I'm going to hit submit.

**Vlad Usatin:** So, and as it builds it, so you can see now it's building it.

**Vlad Usatin:** So I'm going expand it.

**Vlad Usatin:** So now, this is kind of a more.

**Vlad Usatin:** So,

**Vlad Usatin:** More modern user interface to it, but it begins with these triggers and it's building out these components that otherwise a human would have to drag and drop in our interface.

**Vlad Usatin:** So again, so just like with most agents, it would make a decision.

**Vlad Usatin:** So the green ones are the triggers.

**Vlad Usatin:** What starts off, remember when I uploaded the PDF file, it was the trigger.

**Vlad Usatin:** In this case, somebody submits a request for a laptop or they're having an issue.

**Vlad Usatin:** Then we would decide, it decides what to do.

**Vlad Usatin:** So these purple tasks are agents.

**Vlad Usatin:** So it will build an agent to do things.

**Vlad Usatin:** And the blue ones are deterministic processes to make sure that the agents perform as needed.

**Vlad Usatin:** So notice how these purple tasks are sandwiched in these blue rectangles, meaning that this is how we keep agents honest.

**Vlad Usatin:** It continues building out the app. This is more involved than this demo is going to show, but eventually it's going to build out and ask me a few more follow-up questions. Then I would approve it, and the first version of this app would appear in the Elementum platform, very similarly to what I was just using for the corporate employee demo.

**Vlad Usatin:** The final persona, so let's skip over this.

**Vlad Usatin:** So the final persona I have here is the fulfiller, so it's that boring job.

**Vlad Usatin:** Or maybe not, not to insult anyone.

**Vlad Usatin:** So once the request is submitted, the agent took it in.

**Vlad Usatin:** Somebody maybe needs to go and pull a laptop from the desk or somebody from the warehouse, or somebody may need to, a legal person needs to go and look at the contract.

**Vlad Usatin:** So, for example, that contract that I just uploaded, all that mumbo-jumbo of legal text was parsed, right? So even though it looked like just a mess of words, the contract gets broken down into very specific categories like contract types, terms, costs, associations with other systems, right?

**Vlad Usatin:** So this has all been nicely parsed as if a paralegal was working with a lawyer.

**Vlad Usatin:** And now the fulfiller, the lawyer, will review the specific of contracts, nicely parsed, and have a first pass of feedback.

**Vlad Usatin:** It's like, oh, no, termination 90 days is too long or too short, or the contract term 24 months, we don't do 24 months, do 36, right?

**Vlad Usatin:** Whatever feedback is, it's a very quick way to get things going for the fulfiller.

**Vlad Usatin:** And again, so I submitted the PTO request. If you go further down, there's going to be a request for a manager. So here's a PTO request that needs approval.

**Vlad Usatin:** Again, somebody would approve my PTO.

**Vlad Usatin:** Again, I don't approve my own.

**Vlad Usatin:** But again, if it was approved, it would go in and eventually will show up on the calendar, but after the human in the loop.

**Vlad Usatin:** So not only we offer an agent building experience, we also offer a traditional UI for people who are familiar with it and need to action on things, stage it through a variety of approvals, and capture data in a classic or traditional format.

**Vlad Usatin:** So we offer this full ecosystem that offers a modern agentic experience through a chat, whatever your mode is. We offer a traditional low-code opportunity to build applications for builders or this agentic interface. And then this classic interface where people can continue working with it, with all the bells and whistles. This is not just an agent or a developer tool. This is a full platform with full transparency, visibility, and audit, meaning that you could see who did what. We log all the conversations and if there's some conversation happening that's outside of the parameters of your corporate governance, we can flag it in real time. We provide version control.

**Vlad Usatin:** We also create an audit in terms of how much money is being spent with each agent if there's a cost associated with it.

**Vlad Usatin:** So we provide not just an ability to build and execute, but we also are a full platform with role-based access security and all the things that you would expect from a platform.

**Vlad Usatin:** So that's...

**Vlad Usatin:** So what it does, takes an invoice, just like that contract that I uploaded, it digitizes it.

**Vlad Usatin:** And the output of it is a reason why there's a problem with this invoice.

**Vlad Usatin:** So specifically, the invoices that have problems, they get routed to here, and we produce a report on why there is a problem with this.

**Vlad Usatin:** So here's a sample contract, okay?

**Vlad Usatin:** Okay, sorry, not contract, sample invoice, and there's something wrong with it.

**Vlad Usatin:** So we will go ahead and parse it out, and then we will say why it mismatches with the SAP.

**Vlad Usatin:** Okay.

**Vlad Usatin:** That's kind of the end of it.

**Vlad Usatin:** But I'm going to go into kind of behind the scenes and say, so in this case, it sends out an email, right? But let's say I want to do something more than just an email. I can send a message to Teams, I can send an email, or I can send an SMS message.

**Vlad Usatin:** We have another customer.

**Vlad Usatin:** This one, I can actually say their name is Sanofi.

**Vlad Usatin:** So very similar.

**Vlad Usatin:** Again, something happens and that something is for their salespeople.

**Vlad Usatin:** Once they visit the customer and that customer is a doctor.

**Vlad Usatin:** So I'm a drug rep visiting a doctor.

**Vlad Usatin:** And after I walk out of the office, our system has visibility into the schedule.

**Vlad Usatin:** So it knows that I walked out of the office at 10 minutes after me walking out, it will initiate a phone call and call me and say, Vlad, did you see Dr.

**Vlad Usatin:** Kadavi?

**Vlad Usatin:** And I'll say yes or no.

**Vlad Usatin:** And if I say yes, it will say, so how did it go?

**Vlad Usatin:** And then I will just talk to it.

**Vlad Usatin:** And then it will take that mind dump and create a beautiful form. If you work with Salesforce or any other CRM system, it will populate all the fields, next action, and also provide some commentary on what would be the next best action.

**Vlad Usatin:** So we do have a variety of methods, kind of in and out. We can also trigger APIs, and that's a universal thing—whatever you can think of, this send API request would reach any system, any time, even if it doesn't exist yet today.

**Vlad Usatin:** So whatever you can think of, this send API request would be any system, any time, even if it doesn't exist yet today.

**Aida Knežević:** One thing that I wanted to clarify, just on the AI agent part.

**Aida Knežević:** So I noticed when you were, for example, building the workflow, you were using Opus 4.5.

**Aida Knežević:** Does Elementum just use other models?

**Aida Knežević:** Or do you have your own, like, I mean, like when it comes to agents, like, do you have, can you integrate with others?

**Vlad Usatin:** Yeah, great question.

**Vlad Usatin:** We don't have, here, this is the coolest.

**Vlad Usatin:** So I didn't go into the...

**Vlad Usatin:** Technical details.

**Vlad Usatin:** So we, one of our competitive advantages is that we, we're like the Switzerland of, of the platform.

**Vlad Usatin:** So specifically, we don't have our own agents.

**Vlad Usatin:** So a customer has to bring your own agent.

**Vlad Usatin:** So specifically, so for example, I'm going to, I'm an administrator here on the platform.

**Vlad Usatin:** So I can go into this AI services.

**Vlad Usatin:** And once it loads, you're going to see a list of variety of agents that a customer will connect that they already working with, whether it's tropic or whatever is.

**Vlad Usatin:** And the second piece is the database.

**Vlad Usatin:** So a lot of our customers, interestingly enough, are from regulated industries like pharma or insurance.

**Vlad Usatin:** And the reason they pick us is because we don't copy the data out of their system.

**Vlad Usatin:** We work in their system.

**Vlad Usatin:** So when we install our application, this cloud link thing will usually get like the most popular system like Snowflake.

**Vlad Usatin:** Or Databricks or Postgres.

**Vlad Usatin:** So these are kind of the most frequently used systems with us.

**Vlad Usatin:** But ultimately, the customer owns the database or the data cloud, and we install and live in their cloud.

**Vlad Usatin:** So and that seems like, wait, why are you doing this?

**Vlad Usatin:** But it's the comfort.

**Vlad Usatin:** So the customer has their own database, and we live in there, and we provide that security and also a lot of performance from that.

**Vlad Usatin:** And the same thing with the agents, right?

**Vlad Usatin:** So they will have, so most corporations already have contracts with ChatGPT and Anthropic, and they have negotiated a lot of very specific privacy clauses, right?

**Vlad Usatin:** So we will, so when we go into this AI services piece and I connect to any of these platforms, we are going to, the customer will provide the API key that they own.

**Vlad Usatin:** And...

**Vlad Usatin:** Interactions with the Anthropic agents will be according to the terms of that customer.

**Vlad Usatin:** So that's a huge win for us.

**Vlad Usatin:** Also, our competitors, they, like, for example, if you go with Google, they will not offer, you can't build an agent that leverages something from OpenAI.

**Vlad Usatin:** Or if you go to OpenAI or Microsoft, they will only offer OpenAI, but they will not offer the Google.

**Vlad Usatin:** Same thing with Bedrock from Amazon.

**Vlad Usatin:** They will only offer a certain subset of agents.

**Vlad Usatin:** But again, we are like the Switzerland of agents and databases.

**Vlad Usatin:** And we offer whatever you own.

**Vlad Usatin:** We just bring it into this one unified UI with governance.

**Vlad Usatin:** So here you can even see how much money is being spent with each provider.

**Vlad Usatin:** And again, this is very attractive to our customers.

**Andrew Bennett:** Yeah, and Aida, I mentioned yesterday that we're working this week on a slightly new rev of the messaging.

**Andrew Bennett:** And a couple of the really important points are first, fundamentally, when you're building a workflow, there are specific pieces of the workflow that agents are really good at, and we allow you to build deterministic logic for things like routing or branching logic or anything that's really rules-based, where you could maybe get an agent to do the same thing, but it's dramatically more expensive.

**Andrew Bennett:** And it's probably not as reliable because of the probabilistic nature of LLMs.

**Andrew Bennett:** So it's first, only use agents generally, where you need to use an agent in the workflow.

**Andrew Bennett:** And then we allow you to pick which of the LLMs, which of the service providers, which of, you know, is it a Snowflake agent, is it a ServiceNow agent, is it ChatGPT, and use the agent that's most appropriate for that step.

**Andrew Bennett:** And then...

**Andrew Bennett:** And one of the pieces of messaging that's resonating really well with CIOs is, like, if you need the newest, most sophisticated, most expensive model, great, use it.

**Andrew Bennett:** If it's a task that doesn't require that, use DeepSeq, right?

**Andrew Bennett:** Use an older model that's a lot cheaper and lighter weight.

**Andrew Bennett:** And that idea of only apply the big, sophisticated agent hammer where you really need it and otherwise use agent processing that's a lot more efficient and cheaper, that's landing really, really well.

**Andrew Bennett:** Obviously, we're working on the words to say that in a lot more succinct way.

**Andrew Bennett:** Yeah.

**Aida Knežević:** No, I completely understand.

**Aida Knežević:** mean, this is great.

**Aida Knežević:** And I think one of the biggest things that we are like an AI company and we work with a lot of companies that also use AI and there's always this criticism.

**Aida Knežević:** Of the industry, which is like you're using AI for things that like it doesn't need to be used.

**Aida Knežević:** So I think that's a really powerful messaging, like a piece of messaging that we can incorporate into content.

**Aida Knežević:** And I mean, the platform itself, like this is going to be really fun to write about because it works and it's so simple.

**Aida Knežević:** And like the fact that you can just use a single chat interface and just tell it to do multiple things and it does it.

**Andrew Bennett:** It's really, really impressive.

**Aida Knežević:** Anything else that I should know?

**Aida Knežević:** I mean, you've answered all of my questions.

**Aida Knežević:** Like my biggest answer, like my biggest question was around the agents because I wanted to get clarity on that.

**Aida Knežević:** Is there anything else that I should know from maybe your customer conversations or anything that's come up recently?

**Vlad Usatin:** I think just to summarize.

**Vlad Usatin:** So like what makes, what really resonates with the customers is the question.

**Vlad Usatin:** Yeah, so we don't provide any agents and we are agent agnostic where everyone else will try to kind of offer you the marketplace of their own agents and whatever they have contracts with.

**Vlad Usatin:** And then the second piece is that we live in the customer's data cloud.

**Vlad Usatin:** That's a very big comfort point and performance points.

**Vlad Usatin:** So from security standpoint, data is not leaving.

**Vlad Usatin:** I don't know if you have a housekeeper, but it's a cleaning lady coming to you or a cleaning person coming to you, then you bring yourself out to be cleaned, right?

**Vlad Usatin:** So that's kind of the security part, but the other part is also the performance, right?

**Vlad Usatin:** When, for example, the contract being uploaded or somebody submitting a PTR request, we see their real time in the database.

**Vlad Usatin:** So we act on things extremely fast and efficiently from kind of delivery standpoint and monetary.

**Vlad Usatin:** So when you're working from the outside system, it also costs you extra money.

**Vlad Usatin:** So I think these are like customers really, really love these, these endpoints.

**Vlad Usatin:** Yeah, absolutely.

**Aida Knežević:** Yeah.

**Aida Knežević:** And I think also from like a compliance standpoint, you're not, for example, you wouldn't need to, would you need to sign like business associate agreements with healthcare companies?

**Aida Knežević:** It's just a question.

**Vlad Usatin:** Like if, if, if you were working with like a healthcare company, like a, you know, that had patient records, would you need a, it might be a question that, you know, we are HIPAA compliant or we, we, we, so again, so when it comes to HIPAA, we, so they're like, we enable HIPAA compliance.

**Vlad Usatin:** So ultimately the customer owns the HIPAA compliance, not us, but when they work with us, a lot of our customers are HIPAA compliant. And we don't ship data anywhere. So when you work with other vendors, they wind up being kind of the pass-through and using their agents. In our case, the data is theirs, the agents are theirs, and we are visiting them and performing this integration.

**Aida Knežević:** Yeah, exactly. The issue with HIPAA specifically is when you're storing the data, but in this case, it's not even an issue.

**Vlad Usatin:** Correct.

**Andrew Bennett:** Yeah, and same thing with GDPR, right? If your data is in Snowflake and you're GDPR compliant, adding Elementum to the stack is nothing from a GDPR standpoint. We literally don't have a data store.

**Aida Knežević:** Yeah, makes total sense. This was a really great session. Thank you so much for your time, Vlad and Andrew. I know we have a meeting right after this, so I'll see you in a bit.

**Vlad Usatin:** Are you in Europe, Aida?

**Aida Knežević:** Yes, I am. It's 7:30 p.m. here in Bosnia, in Sarajevo.

**Vlad Usatin:** Oh, very cool. Thanks for the time, both of you.

**Aida Knežević:** Thanks, all. Cheers.
