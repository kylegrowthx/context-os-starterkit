# Airbyte <> GrowthX | Agent Connectors Pages

<metadata>
date: 2026-01-22
time: 18:30 UTC
duration: 31 minutes
organizer: Erik O'Brien (erik@growthx.ai)
participants:
  - name: Tanmay Sarkar
    email: tanmay@airbyte.io
    affiliation: Airbyte
    role: Product/Engineering Lead
  - name: Ian Alton
    email: ian.alton@airbyte.io
    affiliation: Airbyte
    role: Engineer
  - name: Kirkland Gee
    email: kirkland@growthx.ai
    affiliation: GrowthX
    role: Lead Engineer
  - name: Erik O'Brien
    email: erik@growthx.ai
    affiliation: GrowthX
    role: Product Lead (Organizer)
fathom_recording_id: 116442483
fathom_url: https://fathom.video/calls/541167717
share_url: https://fathom.video/share/1cvuomzcsuwxAc95pg2tyxqa8zxDSzEP
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

GrowthX and Airbyte discussed automating the creation and deployment of connector landing pages from Airbyte's open-source GitHub repository to Webflow CMS. The team will build a cron job that polls the GitHub changelog, transforms Markdown content into structured JSON, and pushes updates to Webflow—avoiding manual page creation as connectors scale from 20 to 1,000+.

---

## Context

Airbyte auto-generates connector documentation as Markdown files from an open-source GitHub repository and publishes them via Docusaurus. These docs exist but are not currently on Airbyte's main landing pages. The team wants to build dedicated landing pages for each connector on the main domain, with content pulled from the same GitHub source. GrowthX will handle the automation; Airbyte will support the Webflow CMS template updates needed to make fields editable and support dynamic content like variable entity/action counts.

---

## Relevance

- **For GrowthX**: Automation engineering project with clear scope; demonstrates workflow automation from source to CMS; knowledge transfer on Webflow API and connector data structures.
- **For Airbyte**: Scales connector marketing from manual creation to automated publishing; enables rapid iteration as the connector ecosystem grows; reduces operational overhead for developer documentation and landing pages.
- **Strategic**: Validates the approach for auto-generating marketing content from product data; applicable to future product marketing at scale.

---

## Overview

- **Goal:** Automate Webflow landing page creation for \~20 current connectors (scaling to 1,000s) using content from an open-source GitHub repo.
- **Method:** A GrowthX-managed cron job will poll the GitHub repo for changes (using the `changelog` file as a trigger), transform the content, and push updates to Webflow.
- **Blocker:** The Webflow CMS template requires updates to support dynamic content (e.g., `Example Prompts`, `Entities & Actions`).
- **Timeline:** GrowthX will deliver a working automation by next week (Mon/Tues).

---

## Key Topics

### Problem: Manual Page Creation

  - **Goal:** Create dedicated landing pages on the main domain for each agent connector.
  - **Current State:** Content is auto-generated as Markdown from an open-source GitHub repo and published to a Docusaurus docs site via GitHub Actions.
  - **Challenge:** The current manual process for creating Webflow pages is not scalable for the expected growth from \~20 to 1,000+ connectors.

### Solution: Automated Workflow

  - **Architecture:** A GrowthX-managed cron job will poll the open-source GitHub repo directly, eliminating the need for complex GitHub Action integrations.
  - **Trigger:** The cron job will use the `changelog` file to detect meaningful updates, preventing unnecessary pushes.
  - **Content Transformation:** An LLM will parse the Markdown content and structure it into a JSON object that matches the Webflow API's required format.
  - **Update Cadence:** A daily update is sufficient, as the docs site already refreshes every two hours.

### Blocker: Webflow CMS Template

  - The current Webflow template is not configured for the required automation.
  - **Required CMS Updates:**
      - **`Example Prompts`:** Must be made editable via the CMS (currently hard-coded).
      - **`Entities & Actions`:** Must support a dynamic, flexible number of items (e.g., Asana has 22 entities).
      - **`Logo`:** The field must be changed from a static image upload to a reference field that pulls from the existing "Connectors" collection.
  - **Logo Source:** Kirkland will investigate if logos can be pulled from an S3 bucket, which would simplify the workflow by avoiding cumbersome Webflow API lookups.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Add Copland to GrowthX Slack channel

**Tanmay Sarkar / Ian Alton (Airbyte)**
- Check if connector spec includes logo image; share source with Kirkland
- Provide access/details about S3 bucket for logo images (if available)

**Kirkland Gee (GrowthX)**
- Build manual Webflow sync (Markdown→CMS)
- Run 2–3 manual tests with single connector
- Set up cron job with 2-hour cadence (monitor changelog for changes)
- Verify all CMS fields are editable before full automation

---

## Transcript

**Kirkland Gee:** Hello.

**Erik O'Brien:** Hey, Kirkland.

**Kirkland Gee:** What's up?

**Erik O'Brien:** Oh, just another day in paradise. This meeting is being recorded.

**Tanmay Sarkar:** Hi.

**Erik O'Brien:** I brought Kirkland with me here.

**Tanmay Sarkar:** Yes, okay.

**Kirkland Gee:** I can see you guys.

**Tanmay Sarkar:** Okay, cool. I can give some context of what we're trying to discuss here.

We have connector pages in our docs and data repo, and we want to build actual landing pages for those connectors on our main domain. When code gets updated in the GitHub repo and docs, it should automatically update in Webflow CMS.

How can we automate the whole process to generate connector landing pages from GitHub and our docs, which are hosted in Docusaurus?

Currently we have about 20 connectors, but in time we'll probably have 100 and then 1,000. We don't want to manually create webpages for all of them.

The docs for these connectors are auto-generated. We have a template, then we spit out a markdown file based on whatever the connector does. That markdown file gets imported into Docusaurus.

The question is: what's the best way to bridge the gap between what we're spitting out and what Webflow needs to automate this?

I don't think the format has to be Markdown. Markdown might be the wrong format—a more structured import like a JSON file might be better.

**Kirkland Gee:** Can I share my screen to make sure I know what we're looking at?

**Tanmay Sarkar:** Yeah, if you want to navigate to the AI agents section on docs and then agent connectors, you'll see the auto-generated connector pages. These are the ones coming from our GitHub repo.

**Kirkland Gee:** Okay, so these files are already connected, or is there a manual step?

**Tanmay Sarkar:** There's another automation that takes whatever's in the repo and puts it into Docusaurus. We can totally cut Docusaurus out of the equation if needed—it's just how we present it to end users.

We have created one landing page with a structure in mind and generated it manually. We want to automate the whole process so that whenever code gets submitted to our GitHub repo, it automatically updates in Webflow.

Everything on the landing page already exists in the docs in some form—we just need to parse, organize, and structure it the right way.

**Kirkland Gee:** So there are already automations doing this on the docs site. We just need to set up the same for Webflow. All those automations—where do they live? Is it a cron job or GitHub Actions?

**Tanmay Sarkar:** GitHub Actions.

**Kirkland Gee:** So in theory, we could set up another GitHub Action that connects to Webflow with an AI step in the middle. The key is having a strong opinion about what the final landing page looks like and where content gets pulled in.

**Tanmay Sarkar:** I'm not a Webflow expert, but ChatGPT was emphatic that we shouldn't use Markdown for this purpose.

**Kirkland Gee:** It's impossible. What we'll do is build a request object that matches what Webflow needs. AI is pretty good at turning Markdown into that structure. So we figure out the GitHub Action, do a transformation, then push to Webflow.

Let me look at the Webflow page structure.

**Tanmay Sarkar:** I can share my screen and explain the landing page structure we have in mind.

The page has several components: version information (static tags created during publishing), installation/usage code (pulled from docs and updated frequently), supported entities and actions (dynamic list that changes with the connector), messaging and positioning (static, same across all pages), and FAQs (same five questions on every page, just different answers per connector).

**Kirkland Gee:** Looking at the CMS template, the example prompts field is hard-coded into the page and not editable through the CMS. That needs to change. Also, the logo is currently an image upload, but it should be a reference field so we can pull it from the Connectors collection.

**Tanmay Sarkar:** I've asked our Webflow developer to make the example prompts editable. Should be done by tomorrow or Friday.

As for entities and actions—these change frequently. The connector team is very productive, and in early stages. We might add new entities, new actions, or even change the entire code interface. So we need to be flexible, not rigid. The entities and actions list will have a limited number, probably around 8 different verbs at most (Asana has about 22 entities, so we need to handle variable-size lists).

**Kirkland Gee:** We need a flexible number of fields for entities. We could have many static fields and only show the ones with content, or set up something more dynamic. The blocker is getting the CMS changes done first, then building a workflow that transforms the docs format into Webflow format and figures out the automation trigger.

**Tanmay Sarkar:** What's the ideal input format for you? Would JSON be better than Markdown?

**Kirkland Gee:** Markdown is fine. I'll still need to process it with an LLM for things like FAQs anyway, so perfect structuring won't save a step. The main thing I need is for the CMS to have all the fields we want to edit. For the logo, the connector specification might include an image—do you have that in an S3 bucket?

**Tanmay Sarkar:** I'm not sure. I'll check. The logos are visible on our platform, so they're not manually uploaded for each connector.

**Kirkland Gee:** If you can find an S3 bucket, that's easier than Webflow API lookups by ID. But the main architecture is: set up a cron job (instead of GitHub Actions), have it monitor the GitHub repo, do the transformation, and push to Webflow. Since it's an open repo, we can pull directly. That actually makes way more sense—I can just hit the repo and Webflow from our end.

**Tanmay Sarkar:** So what's the next step? Do you need anything from us?

**Kirkland Gee:** Just the CMS changes to make sure all fields are editable. After that, I think we can do everything ourselves. I'll set up a workflow we can run manually first—fire it on a single connector, push to Webflow, and test it two or three times. The key is monitoring the changelog file to know when something's changed.

**Tanmay Sarkar:** That makes sense. Pick one connector, automate it, publish it. We can fix the page anytime. Once you push it live, we can see how it looks and take it from there.

**Kirkland Gee:** What's the timeline?

**Tanmay Sarkar:** Next week, Monday or Tuesday. Right now we're publishing manually, but as we scale from ~20 to 100+ connectors, automation is essential.

**Kirkland Gee:** I think we can have this done sometime next week.

**Tanmay Sarkar:** Great. Feel free to ping us on Slack if you need anything. Thanks for joining—I know it was short notice, but this should unblock things.

**Kirkland Gee:** Yeah, I don't think this is too complex. I can feed the transcript to Claude and get 80–90% of the way there, then clean it up.

**Tanmay Sarkar:** Sounds good. Thanks for your time.

**Erik O'Brien:** Awesome.

**Kirkland Gee:** Thanks, everybody.
