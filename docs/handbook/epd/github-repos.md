<metadata>
purpose: Technical architecture and repository structure across GrowthX products.
source: https://handbook.growthx.ai/epd/github-repos
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# GitHub repos

## Repositories

<CardGroup cols={2}>
  <Card title="Flow" icon="bolt">
    **AI workflow framework and runtime**

    Powers all AI/LLM and regular API needs. Contains the API, workflow runtime, all workflow code, and the framework for creating new workflows (generators, meta-prompts, etc).

    TypeScript + Next.js on top of Temporal using our proprietary workflow style. The README is always up to date to help both Cursor and new team members.
  </Card>
  <Card title="Flow Studio" icon="desktop">
    **GUI for Flow**

    Visual interface for managing and monitoring Flow workflows.
  </Card>
  <Card title="Atlas" icon="grid-2">
    **Web app platform (ContentOS)**

    The web platform built with Rails + React (Inertia.js). Triggers workflows in Flow, hosts the database with client data, and replaces legacy tools. Still in early development but the foundation is solid.
  </Card>
  <Card title="Website" icon="globe">
    **Public-facing website**

    Next.js frontend consuming a headless Strapi CMS API.
  </Card>
</CardGroup>

## Tech stack summary

| Repository | Tech stack | Purpose |
|------------|-----------|---------|
| **Flow** | TypeScript, Next.js, Temporal | AI workflow framework and runtime |
| **Flow Studio** | — | GUI for Flow |
| **Atlas** | Rails, React, Inertia.js | Web app platform (ContentOS) |
| **Website** | Next.js + Strapi | Public website |
