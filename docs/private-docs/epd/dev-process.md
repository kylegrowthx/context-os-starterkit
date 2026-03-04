<metadata>
purpose: Documents the EPD team structure, lanes, and Shape Up-based product development process
audience: EPD team members, new hires, leadership
summary: How the EPD org is structured across three lanes and how the product lane ships software using Shape Up with 4-week build cycles and 2-week cooldowns.
domain: engineering
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

# Engineering, Product & Design

How we build product, structure teams, and operate across EPD.

**What great looks like** — The performance bar — what we expect from every person on this team.

EPD has three lanes:

1. **Product lane** — Design engineers and full-stack engineers building ContentOS (Atlas) and CheckThat.ai
2. **Client ops engineering lane** — Forward-deployed marketing and AI engineers creating custom workflows and covering client needs
3. **AI infra lane** — Team responsible for the internal AI framework Output

## Product

- **Product lane** — Overview of the product lane — team, scope, and key links.
- **Product dev process** — Shape Up methodology, cycles, betting table, and team structure.
- **Product vision** — High-level product direction and roadmap.

## Engineering

- **Client ops engineering** — Forward-deploy team vision, operating model, and workflows.
- **Client ops team lead** — Team lead role, responsibilities, and success metrics.
- **AI-driven development** — AI-native development philosophy, tools, and practices.
- **Agentic pipelines** — How to build client AI pipelines end to end.

## Design & process

- **Design** — Design principles, roles, and operations across product, brand, and GTM.
- **One-on-ones** — Framework for leadership check-ins and feedback.
- **Tech blog** — Publishing guide for technical content.

## Team

- **Hiring** — Interview guides and ideal candidate profiles.
- **Onboarding** — New hire checklist and first-week guide.
- **GitHub repos** — Technical architecture and repository structure.

---

## Quick start by role

### New EPD hire

1. Onboarding — Your first-week checklist
2. AI-driven development — How we work with AI
3. Your lane doc: Product dev process or Client ops engineering

### Product lane (building CheckThat / Atlas)

1. Product dev process — Shape Up process
2. GitHub repos — Technical architecture

### Client ops engineering (forward-deployed)

1. Client ops engineering — Operating model
2. Agentic pipelines — Building pipelines
3. Client ops team lead — Team expectations

### EPD leadership

1. One-on-ones — Leadership framework
2. Hiring — Building the team

---

# Product Dev Process

How the product lane ships software using Shape Up — cycles, sizing, staging, and team structure.

The product lane runs on a process inspired by [Shape Up](https://basecamp.com/shapeup) from 37signals, with **4-week build cycles** and **2-week cooldowns**. This gives us focused execution time plus space for planning, retros, and rollout.

> **Note:** This only applies to the product lane. The AI infrastructure and client operations lanes run their own processes.

## Product quarterly vision

### Primary track: ContentOS (Atlas)

**Mission:** Transform every managing editor into a CMO through our platform — no training required.

ContentOS consolidates our proven content method into a single platform encompassing **strategy**, **production**, and **measurement**.

> **Info:** CheckThat is a separate product from ContentOS, but runs in the same process, uses the same tech stack, and is built by the same team. Both are dogfooded internally.

### Important context: we're not searching for product-market fit

Unlike typical startups, we have a proven process that we want to codify and scale. Our mandate is to build the exact platform to support this process.

The shaping team serves as the feedback and approval committee. No features pass to the delivery team until cleared and dogfooded internally.

## Development process

### Cycle structure

- **Build cycles:** 4 weeks of focused development
- **Cooldown periods:** 2 weeks between cycles for pitch presentations, scope clarification, planning, retrospectives, rollout and training, buffer tasks, and sidequest time

### Project sizing

#### Big batch projects (full 4-week cycle)

Complex or risky features requiring deep focus and careful QA and rollout.

1. **Roadmap** — Linear project under EPD, with one nominated project lead responsible for keeping the project up to date.
2. **Pitch document** — Detailed scope and approach. First version always written by the shaping team lead.
3. **Handoff** — During the cooldown period. Team reviews the pitch, clarifies scope, and sets up project infrastructure.
4. **Development** — Feature branch deployed to staging environment first — no continuous integration. This ensures UX/product quality and code alignment review before merging into main.
5. **Weekly reviews** — Progress check with the shaping team to catch misalignment early.
6. **Release** — Four stages:
   1. **QA period** — Linear tickets or spreadsheets for tracking
   2. **Dogfood rollout** — Deploy to the internal blog first
   3. **Documentation** — Guides for the delivery team
   4. **Production rollout** — Monitor with a handful of clients initially

> **Note:** Why no continuous integration? The volume of AI-generated code makes continuous product-direction review unsustainable. We review UX/product quality and code alignment before merging. Sprinting in the wrong direction is painful to revert. See DHH's [The advantages of large, long-running pull requests](https://world.hey.com/dhh/the-advantages-of-large-long-running-pull-requests-c33d913c).

#### Small batch projects (1–2 weeks)

Quick wins and incremental improvements that can ship rapidly.

1. **Small batch board** — Linear tracking for the work.
2. **Development** — Continuous integration if scope allows, otherwise feature branch / staging.
3. **Weekly review** — Present to the shaping team.
4. **Dogfood** — Deploy to production and test with real data using the internal blog first.
5. **Announcement** — Notify the delivery team.

### Staging and rollout strategy

All projects should be heavily dogfooded internally before being rolled out to clients.

## Team structure

### Roles and responsibilities

**Shaping team** — Defines the work, prepares the project/pitch/handoff, and runs weekly reviews with project teams.

**Execution team:**
- **Design engineering** — Design engineers who blend product design with engineering
- **Full-stack engineering** — Engineers building the Rails + React platform
- **QA** — Handled by the shaping team lead for now

### Team composition per cycle

- 1 design engineer + 1–2 full-stack engineers
- Flexible allocation based on project needs

### On-call schedule

One person is on-call per 4-week cycle to handle bugs or issues. During cooldown, anyone who shipped a feature is on-call for that feature during the 2-week cooldown period.
