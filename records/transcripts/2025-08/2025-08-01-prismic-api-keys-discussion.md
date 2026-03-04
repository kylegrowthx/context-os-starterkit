# Prismic - API Keys Discussion

<metadata>
date: 2025-08-01
time: 19:01 UTC
duration: 15 minutes
organizer: kirkland@growthx.ai
participants: Benjamin Meyer, Jessica Yip, Kirkland Gee
fathom_recording_id: 78047849
fathom_url: https://fathom.video/calls/368244428
share_url: https://fathom.video/share/yFRk4y9AYs6h5HZMVrzwXo73FqtD8ATk
source: fathom
enriched_on: 2026-03-03 14:45 UTC
</metadata>

---

## Summary

Yourco's CTO Benjamin Meyer met with GrowthX's Kirkland Gee and Yourco's Jessica Yip to explore automation options for syncing content from GrowthX's content pipeline into Yourco's Prismic CMS. The core problem: Prismic's API key grants access to both the Migration API (needed for content uploads) and the Custom Types API (for schema changes), and Benjamin was uncomfortable granting full access without security assurances. GrowthX proposed three paths forward: (1) full API access, (2) a JSON file transfer method where GrowthX prepares formatted JSON files that Yourco uploads manually, or (3) a custom proxy service on Yourco's side with restricted authentication. Benjamin agreed to discuss the options internally with Yourco's CEO before deciding.

---

## Context

Yourco, a client, uses Prismic as their CMS for managing blog content. Their blog structure is simple: a single repeatable slice that contains a title, image, and rich text content. GrowthX is helping automate the content creation pipeline, but the handoff to Yourco's CMS currently requires manual copy-pasting of content into Prismic's UI. To speed up the workflow, GrowthX proposed automating the staging process using Prismic's Migration API. However, Benjamin Meyer (Yourco's CTO) raised a security concern: Prismic doesn't allow separate API key permissions for content migration versus schema changes (custom types), meaning any API key with migration access also grants the ability to modify Yourco's content model. This meeting was a technical discussion between GrowthX and Yourco about finding a secure, workable path forward for automation.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed Yourco's Prismic blog uses a simple, single-slice structure (title, image, rich text), making content migration straightforward once permissions are resolved
- Identified that Prismic lacks both granular API permissions and a direct UI import feature, limiting automation options for clients
- Learned that GrowthX's early-stage status (no SOC 2 certification yet) impacts client comfort with API key access — a pattern to watch with other security-conscious prospects

**To GrowthX Business Development:**
- Yourco is actively automating their content workflows with GrowthX, indicating healthy engagement and opportunity for expanding scope once automation is solved
- Benjamin's pushback on security is reasonable and professional — signals a well-managed client who values risk assessment
- Pending decision from Yourco's CEO on path forward; follow-up engagement opportunity in 1-2 weeks

**To Prismic / Product Insights:**
- Prismic's unified API permissions (migration + custom types) are a documented pain point for clients wanting to grant contractors/vendors limited access
- Lack of direct import/export UI forces developers to build custom solutions, creating friction in typical content workflows

---

## Overview

- Yourco's current Prismic API key grants access to both migration and custom types APIs, raising security concerns
- Three main options discussed: 1) Provide full API access, 2) Manual process, 3) JSON file transfer with Yourco handling uploads
- No immediate hybrid solution available; Yourco to internally discuss the best path forward

---

## Key Topics

### Current Prismic Setup and Concerns

  - Yourco uses Prismic for content management, particularly for blog posts
  - Blog structure: Simple setup with one repeatable slice (title, image, rich text content)
  - Main concern: API key grants access to both migration and custom types APIs
  - Benjamin (CTO) hesitant to provide full access without security assurances

### Automation Options Discussed

  - Full API access: Fastest but raises security concerns
  - Manual process: Current method, time-consuming
  - JSON file transfer: growthx.ai provides formatted JSON, Yourco uploads
  - Potential proxy service: Yourco could create a custom endpoint with different authentication

### Security and Compliance

  - growthx.ai lacks formal certifications (e.g., SOC 2) due to early-stage status
  - They store API keys as environment variables in shared team storage and on Render for deployments
  - Yourco needs to evaluate the risk and decide on comfort level with providing API access

### Prismic Limitations

  - No separate permissions for content migration and custom types modification
  - Lack of direct import option in Prismic UI
  - Discussed potential feature upgrades from Prismic to address these issues

---

## Action Items

**Benjamin Meyer (Yourco)**
- Discuss Prismic API access options with Yourco team and CEO; decide on best path forward (full API key, JSON file method, proxy service, or keep manual); report back to GrowthX

---

## Transcript
**Jessica Yip:** Hi, Ben.

**Benjamin Meyer:** Jessica, how's it going?

**Jessica Yip:** Doing well.

**Kirkland Gee:** How are you guys?

**Jessica Yip:** Oh, doing great. I like your hat.

**Kirkland Gee:** Thank you. My son is only 13 months old and doesn't watch Bluey yet, but I think it's great.

**Jessica Yip:** One day he'll grow into it. Okay, let me kick off this meeting. So we had a meeting last week and basically the team is doing manual staging right now in Prismic. We want to automate it from the pipeline to Prismic.

**Jessica Yip:** Ben is our CTO at Yourco. I know you guys have done this for several clients, and we want you to explain the walkthrough, step by step, especially when it comes to the API keys. We don't want to give all access to GrowthX — we want to restrict the staging, which I know you've done before.

**Jessica Yip:** Ben probably will ask more technical questions about how to implement this on our side.

**Kirkland Gee:** Yeah, sure, that all makes sense. Sorry, I'm having a keyboard issue, but I'll move on. Basically, there are different ways of dealing with Prismic. With the most recent client I did this for, they have a pretty complex content model — like 30 different slices on a single page. I spent a lot of time picking out what those components needed to be and built a workflow that translates whatever content we want into the slice JSON object format and sends it to Prismic.

**Kirkland Gee:** As far as staging versus live, are you talking about two different instances, like a staging site and a production site?

**Benjamin Meyer:** No. I looked into this on our end. Basically, I can give you an API key that has access to what they call the migration API.

**Kirkland Gee:** Migration API, yeah, that's basically the only way to do it.

**Benjamin Meyer:** Right. My concern is that I can't separate the API key between the migration API and our custom types API. If I give you this key, you'll be able to update our types as well.

**Kirkland Gee:** So you'd have access to both.

**Benjamin Meyer:** Exactly. That's my concern. Let me share my screen to clarify.

**Kirkland Gee:** Yeah. I didn't even know those were the same permission. Custom types and migration API are the same key?

**Benjamin Meyer:** Yes, it's the same. With that access, you can change whatever you want, pretty much.

**Kirkland Gee:** Okay. So if you guys aren't comfortable with that, another option would be...

**Kirkland Gee:** It's a little more manual and slower, but we could create a JSONL file of the posts we want to upload — one at a time or in batches — and give you those JSON files. You can either run them through the API or use the CLI, which would be easier.

**Kirkland Gee:** The headache is figuring out the exact structure without being able to export an existing page as JSON to see what's needed. But we can figure that out.

**Kirkland Gee:** I haven't seen your Prismic setup, so I don't know how complex it is. Prismic can be so different with different setups. Do you have mostly separate components wired together, or is it more like a header, big rich text block, and footer?

**Benjamin Meyer:** For the blog, it's pretty simple — just a big rich text block. Let me show you. We have the page with the first slice being the heading, page data, slug, etc., and then everything below that is the same slice over and over.

**Benjamin Meyer:** Each slice can have a title, an image, and the content, which is just rich text. It's the same slice configured multiple ways.

**Benjamin Meyer:** I'm not totally against providing the API key, but if we do, I need some assurances. How are you guys storing this key? Do you have any security compliance we can rely on, like SOC 2?

**Kirkland Gee:** We don't have formal certifications yet because we're so early on. We store API keys as environment variables — we have a shared team storage, and then Render for deployments where everything's stored as environment variables for our workflows.

**Kirkland Gee:** If you're not comfortable with that, totally fine. I just need to get the schema for the blog post page type — all the field names — otherwise I'm shooting in the dark.

**Kirkland Gee:** The last time I did this, it took about an hour of sending requests, getting error messages, changing things, and trying again to get everything to line up. But this setup is way simpler.

**Kirkland Gee:** It's a slight inconvenience — we provide a JSON file, you push it up. There's no import option in Prismic, but I'm not sure there are other options beyond what we've discussed.

**Benjamin Meyer:** So it's either we give you an API key or we don't. Is there no option to keep it manual for now?

**Kirkland Gee:** We can definitely keep it manual. We're just trying to automate the copy-pasting. With Prismic, it's inconvenient because each section is its own slice — you have to input title, text, title, text. With API staging, you can do it in one call and then edit as needed.

**Kirkland Gee:** I'm trying to help our team move as fast as possible. I totally understand if you're not comfortable sharing the key. I wish I could show you our SOC 2 certification, but we don't have it yet.

**Jessica Yip:** So there's no hybrid option we can explore?

**Kirkland Gee:** It's either you give us an API key with an HTTP client hitting the migration endpoints — I don't have anything set up for the types endpoints — or the in-between would be we provide you JSON files instead of a Google Doc, and your team can upload them. We can share code on how we've done this before, or Prismic might have a CLI tool.

**Jessica Yip:** So if we use JSON files instead, the process would be the same? Once we finalize content, your team converts it to JSON, and our engineering team automates the conversion?

**Kirkland Gee:** Exactly. We'd add a step to our workflows that separates the content into title and content blocks based on the slice schemas, and get it into Prismic one way or another. I can't think of any other options that don't involve giving us API access.

**Benjamin Meyer:** We could potentially set up a proxy service with different authentication. But I'm not sure we can afford to spend the time on that. I need to think through this.

**Kirkland Gee:** That's another option — a custom endpoint with different auth that proxies over. We've thought about it but haven't implemented it. I don't want to ask your team to build all of that.

**Benjamin Meyer:** It depends on how difficult it would be. I think I have all the information I need. I'll talk to the team and the CEO to figure out the best path forward.

**Kirkland Gee:** I don't know why Prismic made content and custom types the same permission level. It doesn't make sense.

**Benjamin Meyer:** It's ironic because this is exactly the scenario where separate permissions would help. You can only upload content, can't publish, but someone could destroy all the types. It doesn't make sense.

**Kirkland Gee:** Yeah. I understand why they'd let you fetch the types to understand the structure for migration, but allowing updates is crazy. Prismic has always struck me as this weird CMS caught between being for engineers and content people, trying to please both so much that it ends up confusing everyone.

**Jessica Yip:** Do you think Prismic would upgrade their feature permissions soon? That could be a solution.

**Kirkland Gee:** We could ask. I'm good with whatever you decide. If it's a security concern, I can talk with Daryl about it. It's not going to break anything with how things work now, but it would speed things up.

**Kirkland Gee:** Even if you're doing publishing with 10 or 15 articles at a time, if there's code we can write to make your workflow easier, maybe that's something too.

**Benjamin Meyer:** Right, cool. Give it some thought and let us know.

**Kirkland Gee:** Yeah, just think it through and let us know.

**Benjamin Meyer:** We'll discuss and get back to you. Thanks for this conversation.

**Kirkland Gee:** Of course. Sure thing. Thanks, guys.

**Jessica Yip:** Have a good one. Bye.
