<metadata>
purpose: Documents the technical architecture, repository structure, and tech stack across GrowthX products
audience: EPD engineers, new hires
summary: Overview of GrowthX's GitHub repositories and tech stack — Flow (AI workflow framework), Flow Studio (GUI), Atlas (ContentOS web app), and Website.
domain: engineering
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

# Tech Stack & GitHub Repos

Technical architecture and repository structure across GrowthX products.

## Repositories

**Flow** — AI workflow framework and runtime. Powers all AI/LLM and regular API needs. Contains the API, workflow runtime, all workflow code, and the framework for creating new workflows (generators, meta-prompts, etc). TypeScript + Next.js on top of Temporal using our proprietary workflow style. The README is always up to date to help both Cursor and new team members.

**Flow Studio** — GUI for Flow. Visual interface for managing and monitoring Flow workflows.

**Atlas** — Web app platform (ContentOS). The web platform built with Rails + React (Inertia.js). Triggers workflows in Flow, hosts the database with client data, and replaces legacy tools. Still in early development but the foundation is solid.

**Website** — Public-facing website. Next.js frontend consuming a headless Strapi CMS API.

## Tech stack summary

| Repository | Tech stack | Purpose |
|------------|-----------|---------|
| **Flow** | TypeScript, Next.js, Temporal | AI workflow framework and runtime |
| **Flow Studio** | — | GUI for Flow |
| **Atlas** | Rails, React, Inertia.js | Web app platform (ContentOS) |
| **Website** | Next.js + Strapi | Public website |
