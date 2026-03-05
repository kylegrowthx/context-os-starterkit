# Strapi Sync for publishing

<metadata>
date: 2025-06-27
time: 11:31 UTC
duration: 29 minutes
organizer: oluwatimilehin@growthx.ai
participants: Oluwatimilehin Ademosu, Usman Ghani
fathom_recording_id: 70938903
fathom_url: https://fathom.video/calls/338477876
share_url: https://fathom.video/share/WQPWca_xxVhFgNUHfiBWM1yzFgdQKgYM
source: fathom
enriched_on: 2026-03-03 22:00 UTC
</metadata>

---

## Summary

Usman trained Oluwatimilehin on the Strapi CMS workflow for publishing blog posts to growthx.ai, covering the complete process from accessing the CMS through login credentials to publishing. Key areas covered include SEO optimization with meta titles and descriptions, content formatting in Markdown, appropriate CTA (Call-to-Action) placement based on funnel stages (top/middle/bottom), and category/tag management via Airtable. The team emphasized the importance of completing all fields in a single save to avoid leaving partial entries in the CMS and to prevent confusion with the Strapi review team.

---

## Context

Oluwatimilehin Ademosu is a GrowthX team member being trained on the internal publishing workflow for growthx.ai blog content. Usman Ghani, also from GrowthX, is leading the training. This is an internal onboarding session designed to enable Oluwatimilehin to independently publish blog posts to the company's website. The process involves using a Strapi CMS instance that the GrowthX team uses for content management, with the Strapi team handling final review and publishing decisions.

---

## Relevance

- **To GrowthX Delivery:** Standardized CMS publishing process for blog content ensures consistent SEO optimization (meta titles, descriptions, social metadata) and proper CTA placement based on funnel positioning. New content managers must follow the complete end-to-end workflow and avoid partial saves that confuse the Strapi review team.

- **To GrowthX Business Development:** Content publishing workflow is foundational to content marketing delivery. Proper categorization and tagging via Airtable integration supports content strategy execution and blog performance tracking on growthx.ai.

- **To Content Quality:** Character limits for social metadata (60 characters for title, 65 for description) must be strictly observed. OpenGraph preview feature helps catch formatting issues before publishing. "In Brief" sections are required in all articles.

---

## Overview

- Strapi CMS workflow: content manager > blog post > create new entry > fill details
- SEO optimization crucial: meta title/description, social media metadata, keywords
- Content in Markdown format; use Cursor or online converter for formatting
- CTAs categorized by funnel stage; select appropriate CTA for each post
- Save all details at once; don't leave incomplete entries in the CMS

---

## Key Topics

### Strapi CMS Navigation and Basic Setup

- Access Strapi CMS via provided login credentials
- Navigate to Content Manager > Blog Post > Create New Entry
- Fill in title and select category for the blog post
- SEO section: Add meta title and meta description (optimized for character limits)
- Meta social: Add titles and descriptions for Facebook and Twitter (60-65 char limit)
- Add keywords, set structured data to null, input canonical URL

### Content Formatting and Upload

- Content should be in Markdown format
- Use Cursor app or online text-to-markdown converter
- Remove H1 from content (already defined in title field)
- Add appropriate CTA at the end of the content (based on funnel stage)
- Use "Add a component to slices" to include related blog posts

### Category and Tag Management

- Use Airtable to generate category and tags
- Paste generated category and tags into respective CMS fields

### Final Steps and Quality Check

- Review all fields and click "Save"
- Use OpenGraph preview to check how the post appears in search results
- Ensure "In Brief" section is included in the article
- Leave status as "To Do" for Strapi team to review

### Best Practices and Warnings

- Always save complete entries; avoid partial saves
- Don't change the status of the post; let Strapi team handle it
- Be cautious of character limits, especially for long-tail keywords
- Use appropriate CTAs based on the article's funnel stage (Top, Middle, Bottom)

---

## Action Items

**Oluwatimilehin Ademosu**
- Review CTA categories & notion doc for top/middle/bottom funnel understanding

**Usman Ghani**
- Send required links (CTA doc, notion, etc.) to Oluwatimilehin via Slack

---

## Transcript

**Usman Ghani:** Okay, so do you have access to Strapi's content list?

**Oluwatimilehin Ademosu:** Strapi's stream it. Yes, do you have access to it?

**Usman Ghani:** I don't know. Let me check.

**Oluwatimilehin Ademosu:** Should I check now? I think it's in the handbook doc.

**Usman Ghani:** Can you see my screen right now?

**Oluwatimilehin Ademosu:** Let me check.

**Usman Ghani:** Can you check your Slack? This is the ID password for the CMS, and this is the page for it. Do you want to log in to check it yourself?

**Oluwatimilehin Ademosu:** I am trying to log in. Okay, I'm in.

**Usman Ghani:** Have you logged in? Can you go to the content manager? You should see something like my screen.

**Oluwatimilehin Ademosu:** Okay. Can you see it? I can see collection types, blog posts.

**Usman Ghani:** So this will be your main screen from where you will have to upload your post. You will always have to go to content manager, then click on blog post on the left, and then create a new entry.

**Oluwatimilehin Ademosu:** Okay.

**Usman Ghani:** Here we will add all our article details. First of all, we will have to add the title. Our main title, for example, I am working on this at the moment, so this will be my title. Actually, let me show you something that I uploaded today. I uploaded this article today, so this was my title.

**Oluwatimilehin Ademosu:** This was my select.

**Usman Ghani:** Next, when you will create new entry, can you see SEO written here?

**Oluwatimilehin Ademosu:** Yeah, I can see the SEO part. I just want to check it on my own screen. Okay, blog post, create new entry. Yeah, I can see the SEO. Then you will click on this plus button and then it will create this thing.

**Usman Ghani:** And so when it is this thing, then you have to add meta title and meta description. For meta title and meta description, we have discussed with the Strapi team. They will be optimized based on certain limits. In the publishing checklist, you can see the website with those limits.

**Oluwatimilehin Ademosu:** Okay, yeah, yeah, okay.

**Usman Ghani:** So, with this SERP website, we optimized our meta title, meta description, and then we upload it here in these fields. After that, we do two things. There is something called meta social. We have to add two titles and two descriptions here. First, for Facebook, you add a title like "best practices for software," and then you will add a description. This title can be a maximum of 60 characters and description can be of 65 characters.

**Oluwatimilehin Ademosu:** Check the limits. It should be under 65 characters.

**Usman Ghani:** Now, if you add more than these limits, then CMS will give you a validation error when you upload it in the end. And for meta social description, even if you cross the limit, Strapi CMS will not give you an error. But you should always try to remain in the limits. So we add two descriptions like this. Meta-social, Facebook, and then we will add another entry on Twitter. Like for here, I add first for Facebook, 60 characters in titles, 65 characters in meta descriptions, and then I added Twitter.

**Oluwatimilehin Ademosu:** Is it going to be the exact same title and description?

**Usman Ghani:** Sometimes I used a different title, but now I sometimes have similar titles. One thing you will also struggle with is that if an article title is long, then the description, you will find it hard to limit it under 60 or 65 characters.

**Oluwatimilehin Ademosu:** Okay.

**Usman Ghani:** Next, we have keywords. Then there is a structured data thing, just set it to null. All these steps are written here in the publishing channel. So, structured data should be null. Then add a canonical URL here.

**Oluwatimilehin Ademosu:** Is that a slug?

**Usman Ghani:** I just add this in the beginning. And after that, it will be my select from here. And after canonical URL comes the content. Content is in the Markdown format.

**Oluwatimilehin Ademosu:** Can you copy and paste it directly from docs or do you have to use like an LLM to convert it to Markdown?

**Usman Ghani:** I go to download and create a markdown and then open it in Cursor. And then, do you have Cursor stored in your PC?

**Oluwatimilehin Ademosu:** I don't think so, but you can show me how to do it.

**Usman Ghani:** If you don't have Cursor, I don't think it's 100% necessary. It's actually a software development tool. I already had it stored in my PC, so I was using it. One thing you can do is use an online text to markdown converter. How have you been converting your text to markdown until now?

**Oluwatimilehin Ademosu:** I think I just asked ChatGPT to give me a markdown and it does it. I don't know, we don't usually submit stuff in markdown, but I'll figure that out. You can continue.

**Oluwatimilehin Ademosu:** Okay, I will give you Cursor link. Cursor is very easy. You just have to install it and then you just have to open your document. Similarly, you just have to open that document in Cursor after downloading it.

**Usman Ghani:** Once we have uploaded the markdown, one thing to notice is that you don't add your H1 in the markdown here. Because we already defined it in the title. So just when you upload it here, just remove your H1. And then after that, go to the bottom. And then you will pick a CTA for your blog. You have to add a CTA for all blogs.

**Oluwatimilehin Ademosu:** Could you send me the CTA document or whatever? I think it should be in the handbook.

**Usman Ghani:** Yes, this is the Notion. And these are the CTAs. So, you can ask me any question between my conversation. I don't have any issues. In Notion document, we have like three categories. Top of Funnel, Middle of Funnel, and Bottom of Funnel. You will go through this text and see which category your article belongs to. In many articles, you might not find the category. For that, I mostly use Top of the Funnel. Sometimes you might be writing on plugin or tool that is related to Strapi, then you will use middle of the funnel. For example, if you are writing on Angular, then it belongs to the Launchpad CTA. You will go to your CTA list and you can see the Launchpad demo CTA. We have to copy this at the end of our markdown post in the CMS.

**Oluwatimilehin Ademosu:** Yeah. That is for support for now, right?

**Usman Ghani:** Similarly, we will write a lot of articles on APIs, webhooks, mobile development, like how to build this and that, JavaScript development. For that, we'll have middle of the funnel. Download CTA communication.

**Oluwatimilehin Ademosu:** Can you use it to check on either of these?

**Usman Ghani:** So can I move forward from CTA?

**Oluwatimilehin Ademosu:** Next.

**Usman Ghani:** Next you have to do this thing. Can you see, okay, this was our content where we uploaded the markdown. Here is the option, "add a component to slices," click on that. You can see the "related blocks" option. Now, you have to use this option to add three similar blog posts. For example, for my software articles, since this was related to security, I search here, security, and it will give me articles, and then I will paste them. That's how I uploaded three articles. When you come here, you go to the Airtable. So in the Airtable, we should always fill in cluster field and you paste your article here in the full article field. And after that, you go to category and tags. There's a run button here. When you click on it, it will generate the tags. You can rerun it by clicking that. So, when you run this, then this will create your category and it will create your tags. You will paste them. Category will be pasted here. Tags will be pasted one by one. When you will add cloud computing, then it will show cloud computing. Similarly you will add other things.

**Oluwatimilehin Ademosu:** Okay.

**Usman Ghani:** When you follow all the steps, you will go to the top and click on save. When you click on save, on the right hand, it will give you the OpenGraph preview. You don't have to worry about the native text, it will be always okay. You have to worry about keyword density, but the founder will be always alright. Keyword density will be sometimes an issue when we have a very long tail keyword, because in that case we can't stuff it. Meta social text will be there, canonical URL will be there, JSON schema data is set to null. And you don't have to add the meta robots. And also, can you see this OpenGraph preview?

**Oluwatimilehin Ademosu:** Yeah.

**Usman Ghani:** When you click on it, it should give you the preview of how your page looks on the search results. So if you want to see if something is wrong. Now, the CTA that we added in the end, it's showing like this. So that's how you added it in the script. Did you add the "In Brief" to the article?

**Oluwatimilehin Ademosu:** Vivek says something about always adding an in brief section.

**Usman Ghani:** I think in brief section is important. So, you should add in brief section to the article.

**Oluwatimilehin Ademosu:** Okay.

**Usman Ghani:** One thing that I forgot to mention is that, can you see on the right hand here the status? Don't change the status of this. Let it remain "To Do." When you will create any article, it will always be at this stage, but don't change it from your side. The Strapi team will change it. And yes, when you click on save at any point, for example, let's say you only add a title here and save it, the record will come here and then Strapi's team can go through it. I did this mistake once. I created my record and thought that I would publish it and save all the details at the end of the day. But then Strapi's team asked me why there was an empty field in Strapi. So, after that, I only upload all the details at once.

**Oluwatimilehin Ademosu:** When I drafted it in the CMS, I just save it as a draft, right?

**Usman Ghani:** What do you mean? Do you publish immediately or fill in all the fields or you just save it as a draft for review?

**Oluwatimilehin Ademosu:** Oh, I'm guessing I should save it as a draft.

**Usman Ghani:** So, when I edit my article, I send it for editing, but when editing is done, I get approval to upload the draft to CMS, and then I upload it. Let's say you have uploaded a draft right now, and after five hours or next day, you might want to make some changes to it.

**Oluwatimilehin Ademosu:** In the CMS.

**Usman Ghani:** Then, Strapi team will know. Does the CMS save automatically? Like, if you refresh, are you going to lose all your fields?

**Usman Ghani:** I don't think it saves automatically. Let's say you have filled everything until the end, and if you forgot to click on the save button and close the window, everything will be gone. You have to save it, then you are completed. Don't save it before, like for example, let's say you add some details and you are thinking maybe I will upload the rest after three hours. Don't do it, because once you save it, your article will show up here. So once you save it, the Strapi team can see it. Now, any other questions?

**Oluwatimilehin Ademosu:** No, that's everything. I kind of understood everything. The documents are fairly easy to follow. I guess the hardest part of it was understanding the top of the funnel, bottom of the funnel, and CTA. So I think I would have to actually read a bit more about that Notion document. So please send me the required links.

**Usman Ghani:** So when you are uploading, you might have questions when you start to do stuff. So when you have any questions, you can ask me.

**Oluwatimilehin Ademosu:** All right. That makes sense. Thank you.

**Usman Ghani:** Thank you.
