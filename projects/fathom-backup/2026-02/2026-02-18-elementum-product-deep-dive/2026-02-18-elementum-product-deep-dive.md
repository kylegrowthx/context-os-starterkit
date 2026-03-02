# Elementum product deep dive

<metadata>
date: 2026-02-18
time: 18:00 UTC
duration: 32 minutes
organizer: Aida Knežević (aida@growthxlabs.com)
participants:
  - Vlad Usatin (Elementum Co-founder/CTO, vusatin@elementum.com)
  - Andrew Bennett (Elementum, abennett@elementum.com)
  - Kyle Westwood (Elementum, kwestwood@elementum.com)
  - Aida Knežević (GrowthX, aida@growthxlabs.com)
fathom_recording_id: 123425581
fathom_url: https://fathom.video/calls/570075963
share_url: https://fathom.video/share/Gjaftdj77W9kEb-EnFKefMRyZiNi9pf6
source: fathom
enriched_on: 2026-02-27T19:37:08Z
</metadata>

---

## Summary

Vlad Usatin (Elementum CTO) and Andrew Bennett conducted a comprehensive product demo showing how Elementum combines deterministic workflows with probabilistic AI agents to create a hybrid platform for enterprise automation. The platform operates as a "Switzerland" for both AI models and data clouds—customers bring their own LLM contracts and run Elementum directly in their existing data infrastructure (e.g., Snowflake) to ensure security and compliance. Key differentiators include native agent-workflow integration with deterministic guardrails, a unified chat interface across multiple channels (web, Slack, Teams, phone), and cost optimization by allowing task-appropriate agent selection.

---

## Context

Elementum is solving the fragmentation problem in enterprise workflow automation. While pure LLMs (ChatGPT, Claude) are unreliable for regulated business processes due to their probabilistic nature, and traditional workflow tools (ServiceNow, UiPath) bolt-on agent capabilities as afterthoughts, Elementum was built from the ground up to merge both approaches. The company targets regulated industries (pharma, insurance, financial services) where compliance and auditability are non-negotiable—customers have data in Snowflake or Databricks and existing contracts with OpenAI or Anthropic for AI services. Elementum's key insight is that not all workflow steps need sophisticated models; deterministic logic handles routing and branching more reliably and cost-effectively, while agents tackle complex, unstructured tasks like document parsing and context extraction.

This meeting was part of GrowthX's content development engagement with Elementum, following an earlier positioning discussion with Nader. Aida sought to understand the product deeply to ensure accurate, compelling content around the platform's messaging and capabilities.

---

## Relevance

**Content Creation & Messaging:**
- Differentiator messaging on agent/data agnosticism is strong for CIO audiences—avoids vendor lock-in and aligns with enterprise procurement preferences
- "Use the right tool for the job" framing (expensive model for complex tasks, cheap models for simple ones) resonates with CFOs focused on AI cost control
- Unified interface replacing fragmented systems is tangible value prop for end users

**Product Strategy:**
- Hybrid deterministic + probabilistic architecture is novel positioning against pure-play AI agents and legacy automation vendors
- In-cloud deployment model (Snowflake, Databricks) is major selling point for regulated industries on compliance/data residency
- Multi-persona interface (Employee chat, Builder/developer, Fulfiller/actioner) demonstrates platform breadth

**Customer/Market Insights:**
- Pharmaceutical reps using phone-based workflow (Sanofi example) shows real-world B2B use cases beyond knowledge work
- HIPAA/GDPR compliance story is critical for healthcare/EU-regulated clients
- Cost analytics per LLM provider is emerging buying factor for enterprise customers

**GrowthX Opportunity:**
- Clear hook: "Deterministic guardrails for agents" + cost optimization could anchor content series
- Platform flexibility (multiple agents, multiple data clouds, multiple channels) enables multiple customer verticals and use cases
- Positioning as "Switzerland" is defensible and differentiated in crowded AI automation space

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

- **Aida Knežević (GrowthX):** Use this product deep dive to inform content creation around Elementum's differentiators, particularly agent/data agnosticism, deterministic guardrails, and cost optimization messaging. Key points to highlight: hybrid architecture, in-cloud compliance model, unified interface across multiple channels.
- **Andrew Bennett (Elementum):** Finalize updated messaging framework around deterministic logic + agent optimization and share with Aida for content alignment.

---

## Transcript

**Vlad Usatin:** Meeting is being recorded.

**Aida Knežević:** Thank you for jumping on today. So we're hoping to get a product demo and ask a couple of follow-up questions. We want to understand how the platform works because we're going to be writing content related to it, so we want to make sure it's accurate from a product perspective.

**Andrew Bennett:** Yeah, and Vlad, just a little more context. We've done a few onboarding calls with GrowthX already—we had Nader a few days ago covering overall company story and positioning. They've done a lot of work documenting company positioning and ICP, so this is just showing the product.

**Vlad Usatin:** All right, let's show you what we've got. I'm going to share my screen.

**Vlad Usatin:** So we fulfill the sweet spot between traditional workflows and pure AI agents. We build workflows with agents in the middle. Today, companies have a choice: use something like ChatGPT or Copilot alone, or rely on traditional players like ServiceNow or UiPath. But pure LLMs don't work for enterprise—they're unreliable for regulated workflows because they don't do the same thing every time and are hard to audit. Traditional workflow tools added agents as bolt-ons. We started building when agents came online, so we're native to this hybrid approach.

Here's an example: an employee requests PTO. The request gets routed to an agent, which processes it. Then we put it back into a deterministic workflow that validates the response matches our expectations, then writes it to systems like Workday. This positions us as a gateway for all corporate actions. Instead of a jungle of agents scattered across Workday, SAP, and other systems, we're the unified front door—we route to their agent, get the response back, and create one entry point for organizations.

**Vlad Usatin:** I'm going to show three personas. First is traditional corporate workers like us. You might ask for PTO, submit a contract, or requisition a new laptop. We provide a front door that looks like ChatGPT but behind the scenes routes to different systems. We're like a corporate portal. At the end of the day, the front door is just a text box—in a web browser, Slack, Teams, or even a phone call. They all lead to the same unified entry point within Elementum that routes the requests.

**Vlad Usatin:** Now let me show how it works. I'm going to say: "Process this contract. Also, I want to take PTO from March 1st through 5th. My laptop is old, so can you put in a requisition for a new laptop?" The system processes all three requests. The PTO request goes into an approval cycle with a human in the loop. The contract goes to the contracting system, and the laptop request goes to IT. For any modern corporation that needs deterministic workflows, agentic workflows, and human-in-the-loop approval, we bring it all together in one system. Instead of three different chats or agents, you get one simple interface through web, SMS, Teams, or any channel. That's persona one—a traditional corporate employee having a pleasant working experience.

**Vlad Usatin:** Second persona is a builder. How do you make this happen? We have a drag-and-drop interface and an agent-driven builder. When you upload a PDF, the system asks you questions about what you're trying to build—like planning a trip. You describe what you need, hit submit, and it builds the first module and asks follow-up questions. As it builds, you see green triggers (what starts the workflow), purple agent tasks (what AI does), and blue deterministic processes (validation logic). Notice the purple tasks are sandwiched in blue rectangles—that's how we keep agents honest. It eventually asks a few more questions, you approve it, and the workflow appears in the platform.

**Vlad Usatin:** The final persona is the fulfiller. Let's skip the details of that for now.

**Vlad Usatin:** The fulfiller role handles approval and execution. Once a request comes in, a legal person needs to review the contract, an IT person needs to pull a laptop, or a manager needs to approve PTO. The contract we uploaded gets parsed—all that legal text is extracted into specific categories: contract type, terms, costs, associations with systems. It's as if a paralegal worked with the lawyer. Now the lawyer reviews the nicely parsed contract and provides feedback: "90-day termination is too short, do 180 days," or "24-month terms don't work for us, use 36 months." For the PTO request, a manager reviews and approves it, then it syncs to the calendar after human approval.

We offer a full ecosystem: a modern chat experience for employees, a low-code builder for developers, a traditional UI for people familiar with classic interfaces, and analytics for governance. This is a full platform with transparency, visibility, and audit capabilities. We log all conversations and can flag out-of-policy activity in real time. We provide version control and cost analytics showing spending per agent provider. It's a complete platform with role-based access, security, and everything you'd expect from enterprise software.

**Vlad Usatin:** Let me show another example. The system takes an invoice, digitizes it, and produces a report on any problems. If an invoice has issues, we parse it and explain why it mismatches with SAP. Behind the scenes, we can send notifications multiple ways—email, Slack, Teams, SMS, or API calls. For example, if there's a problem with an invoice, we might send a Slack message to the finance team. The flexibility is built in: whatever notification method you need, we support it.

**Vlad Usatin:** We have another customer, Sanofi. Drug reps visit doctors. After the rep leaves, our system knows from the schedule. Ten minutes after departure, it initiates a phone call: "Did you see Dr. Kadavi?" The rep responds yes or no, then says how it went. The system takes that unstructured input and creates a beautifully formatted CRM entry—populating Salesforce fields, suggesting the next action, and providing commentary. We support multiple methods: email, Slack, Teams, SMS, and APIs. The API trigger is universal—you can connect to any system, even if it doesn't exist yet today.

**Aida Knežević:** I noticed you were using Opus 4.5 when building the workflow. Does Elementum just use other models, or do you have your own agents?

**Vlad Usatin:** Great question. One of our competitive advantages is that we're the Switzerland of the platform. We don't have our own agents. Customers bring their own agents. I'm an administrator here, and I can go to AI services and see a list of agents the customer is already working with—whether Anthropic, OpenAI, Google, or others.

The second piece is the database. Many of our customers are in regulated industries like pharma or insurance. They choose us because we don't copy data out of their system—we work inside their system. When we install, we connect to systems like Snowflake, Databricks, or Postgres. The customer owns the database, and we install and live in their cloud. This gives them security and performance benefits.

The same applies to agents. Most corporations already have contracts with ChatGPT and Anthropic with specific privacy clauses negotiated. When we connect to those platforms, the customer provides their API key, and interactions happen according to their terms. That's huge for us. Our competitors—Google, OpenAI, Microsoft, Amazon—they only let you use their own agents. You can't mix OpenAI with Google or Bedrock with others. But we're the Switzerland of agents and databases. We support whatever you own and bring it into one unified UI with governance.

**Vlad Usatin:** You can see cost analytics showing spending per provider. This is very attractive to our customers.

**Andrew Bennett:** We're working this week on refined messaging. Key point: when building a workflow, certain pieces are perfect for agents, but others should use deterministic logic for routing and branching. You could use an agent for routing, but it's dramatically more expensive and unreliable due to the probabilistic nature of LLMs. Use agents only where you really need them, then pick the most appropriate LLM provider and model—Snowflake, ServiceNow, ChatGPT, or others.

What's landing really well with CIOs is this: if you need the newest, most sophisticated, most expensive model, use it. But if the task doesn't require that, use DeepSeq or an older, cheaper, lighter-weight model. Only apply the big, sophisticated agent hammer where you really need it, and use cheaper, more efficient processing otherwise. It's resonating well, and we're refining the messaging to be more succinct.

**Aida Knežević:** I completely understand. This is great. I think one of the biggest criticisms of the AI industry is using AI for things that don't need it. So that's powerful messaging we can incorporate into content. The platform itself is going to be fun to write about because it works and it's so simple. The fact that you can use a single chat interface and tell it to do multiple things and it does it—that's really impressive.

Anything else I should know? You've answered all my questions. My biggest question was around agents, and I got clarity on that.

**Vlad Usatin:** Let me summarize what resonates with customers. We don't provide any agents—we're agent agnostic. Everyone else tries to offer their own agent marketplace. Second, we live in the customer's data cloud. That's a huge comfort and performance point. From security, data never leaves. From performance, when a contract is uploaded or a PTO request submitted, we see it in real-time in their database. We act extremely fast and efficiently. Working from outside systems costs extra money. These are the endpoints customers really love.

Also from compliance: if your data is in Snowflake and you're GDPR-compliant, adding Elementum is nothing from a GDPR standpoint because we don't have a data store.

**Aida Knežević:** From a compliance standpoint, would healthcare companies need business associate agreements?

**Vlad Usatin:** For healthcare companies with patient records, we enable HIPAA compliance. Ultimately the customer owns the compliance, not us. But when they work with us, many of our customers are HIPAA compliant. We don't ship data anywhere. Other vendors act as pass-throughs using their agents. In our case, data is theirs, agents are theirs—we live in their system.

**Aida Knežević:** Exactly. The issue with HIPAA is storing data. Here, it's not an issue.

**Andrew Bennett:** Same with GDPR. If your data is in Snowflake and you're GDPR-compliant, adding Elementum is nothing from a GDPR standpoint because we don't have a data store.

**Aida Knežević:** This is great. It was a really great session. Thank you so much for your time. Andrew, I know we have a meeting after this, so I'll see you in a bit.
