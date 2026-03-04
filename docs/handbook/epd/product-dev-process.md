<metadata>
purpose: How the product lane ships software using Shape Up — cycles, sizing, staging, and team structure.
source: https://handbook.growthx.ai/epd/product-dev-process
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Product dev process

The product lane runs on a process inspired by [Shape Up](https://basecamp.com/shapeup) from 37signals, with **4-week build cycles** and **2-week cooldowns**. This gives us focused execution time plus space for planning, retros, and rollout.

<Note>
This only applies to the product lane. The AI infrastructure and client operations lanes run their own processes.
</Note>

## Product quarterly vision

### Primary track: ContentOS (Atlas)

**Mission:** Transform every managing editor into a CMO through our platform — no training required.

ContentOS consolidates our proven content method into a single platform encompassing **strategy**, **production**, and **measurement**.

<Info>
CheckThat is a separate product from ContentOS, but runs in the same process, uses the same tech stack, and is built by the same team. Both are dogfooded internally.
</Info>

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

<Steps>
  <Step title="Roadmap">
    Linear project under EPD, with one nominated project lead responsible for keeping the project up to date.
  </Step>
  <Step title="Pitch document">
    Detailed scope and approach. First version always written by the shaping team lead.
  </Step>
  <Step title="Handoff">
    During the cooldown period. Team reviews the pitch, clarifies scope, and sets up project infrastructure.
  </Step>
  <Step title="Development">
    Feature branch deployed to staging environment first — no continuous integration. This ensures UX/product quality and code alignment review before merging into main.
  </Step>
  <Step title="Weekly reviews">
    Progress check with the shaping team to catch misalignment early.
  </Step>
  <Step title="Release">
    Four stages:

    1. **QA period** — Linear tickets or spreadsheets for tracking
    2. **Dogfood rollout** — Deploy to the internal blog first
    3. **Documentation** — Guides for the delivery team
    4. **Production rollout** — Monitor with a handful of clients initially
  </Step>
</Steps>

<Tip>
Why no continuous integration? The volume of AI-generated code makes continuous product-direction review unsustainable. We review UX/product quality and code alignment before merging. Sprinting in the wrong direction is painful to revert. See DHH's [The advantages of large, long-running pull requests](https://world.hey.com/dhh/the-advantages-of-large-long-running-pull-requests-c33d913c).
</Tip>

#### Small batch projects (1–2 weeks)

Quick wins and incremental improvements that can ship rapidly.

<Steps>
  <Step title="Small batch board">
    Linear tracking for the work.
  </Step>
  <Step title="Development">
    Continuous integration if scope allows, otherwise feature branch / staging.
  </Step>
  <Step title="Weekly review">
    Present to the shaping team.
  </Step>
  <Step title="Dogfood">
    Deploy to production and test with real data using the internal blog first.
  </Step>
  <Step title="Announcement">
    Notify the delivery team.
  </Step>
</Steps>

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
