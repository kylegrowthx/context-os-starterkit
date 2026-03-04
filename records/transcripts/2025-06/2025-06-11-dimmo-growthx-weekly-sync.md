# Dimmo <> GrowthX Weekly Sync

<metadata>
date: 2025-06-11
time: 19:01 UTC
duration: 16 minutes
organizer: megan@growthx.ai
participants: Prateek Gupta, Jenn Peters, Megan Dickey
fathom_recording_id: 67868827
fathom_url: https://fathom.video/calls/324537346
share_url: https://fathom.video/share/h4dmmzfyFkcpXuTYZ16D6mB-q4pofaJN
source: fathom
enriched_on: 2026-03-03 14:30 UTC
speaker_note: Troy Munson and Lucas Swartsenburg were on the calendar invites but did not attend the call. Lucas was expected to join to discuss technical issues but never appeared.
</metadata>

---

## Summary

Prateek Gupta flagged a critical bug affecting all Dimmo articles: duplicate content and irrelevant links are appearing after the "cons" section, likely stemming from the Webflow CMS migration. Jenn Peters agreed to adjust the article outline to match Prateek's recommended structure (company overview → pricing → benefits/features → pros/security/compliance/support → user reviews/competitors), removing the extra "how to use" and "legal info" sections. Prateek also highlighted a publishing bottleneck: manually reformatting takes 40 minutes per article because formatting is lost when pasting from Airtable to the CMS, and he asked Lucas to investigate whether Markdown input would retain formatting.

---

## Context

Dimmo is a content platform where GrowthX is working as a delivery partner to generate and publish product comparison and review articles at scale. This weekly sync is part of ongoing delivery work where GrowthX handles content creation (via Jenn Peters) and Dimmo handles the technical platform (Lucas Swartsenburg as CTO). The engagement focuses on streamlining content generation workflows and fixing bugs in the publishing pipeline that are slowing down production and creating quality issues.

---

## Relevance

**To GrowthX Delivery:**
- Critical content quality bug (duplicate sections, incorrect links) affecting all articles generated for Dimmo — requires urgent investigation and fix from Dimmo's engineering team
- Publishing workflow bottleneck: 40 minutes per article due to formatting loss during Airtable-to-CMS paste — potential solution to explore is Markdown input retention
- Established standard article structure (6 core sections) that Jenn Peters will enforce going forward, reducing revision cycles and rework

**To GrowthX Business Development:**
- Dimmo engagement showing operational friction points around content-to-publish workflow; addressing these blockers could unlock faster scale and higher volume output
- Article generation at scale (6000+ word pieces) is hitting Airtable performance limits (slowdowns, API timeouts); may signal need for alternative tooling or API optimization with Dimmo

---

## Overview

- Critical bug discovered: duplicate content and irrelevant links appearing in articles due to possible migration issues from Webflow CMS
- Content structure refinement needed: standardize headers and remove unnecessary sections
- Publishing process inefficient: formatting lost when pasting content, requiring manual fixes (40 mins/article)

---

## Key Topics

### Technical Issues with Content Display

  - Duplicate sections appearing after 'cons' in articles (e.g., company overview, pricing repeated)
  - Irrelevant links showing up (e.g., Salesforce link in Wormforge article)
  - Likely caused by migration from Webflow CMS or data fetching issues
  - Bug needs urgent investigation and fix

### Content Structure Optimization

  - Prateek shared ideal article structure:
    1.  Company overview (establish trust)
    2.  Pricing
    3.  Benefits and functionalities
    4.  Pros, security, compliance, customer support
    5.  User reviews and competitors
    6.  How to use (optional extra section)
  - Legal info section at bottom to be removed
  - Jenn to adjust outline based on Prateek's screenshot

### Publishing Process Inefficiencies

  - Current process takes \~40 minutes per article
  - Formatting (H1, H2, H3, bullet points) lost when pasting from Airtable to CMS
  - Manual reformatting required, significantly slowing down the process
  - Potential solution: Investigate if Markdown input retains formatting
  - Lucas (CTO) to look into publishing support and formatting retention

### Content Generation Challenges

  - Jenn working on streamlining workflow for faster content generation at scale
  - Large content pieces (6000+ words) causing Aerofs to slow down and API timeouts

---

## Action Items

**Jenn Peters (GrowthX)**
- Adjust article outline to match Prateek's screenshot; remove extra "how to use" and "legal info" sections from generated content

**Prateek Gupta (GrowthX)**
- Inform Lucas (Dimmo CTO) about duplicate content and incorrect links issues in articles; inquire about Markdown input for content to retain formatting to reduce 40-minute publishing time

---

## Transcript

**Prateek Gupta:** I like your cafe background.

**Jenn Peters:** Very smart.

**Prateek Gupta:** So Troy is not joining us today. Troy is the CEO at Dimmo. We have Lucas — Lucas would be joining us. He's a CTO, and he looks after all the tech fixes and all.

**Megan Dickey:** Sounds good.

**Prateek Gupta:** Let's just give Lucas a couple of minutes. Let me just text him.

**Jenn Peters:** My cat is very needy, so apologies if you hear any random cat sounds. I have two dogs actually, but the other one, he can't be trusted when I'm on a video call, so he's sequestered to a safer area.

**Prateek Gupta:** Yeah, they got to get right up in your face sometimes.

**Jenn Peters:** They just require constant attention.

**Prateek Gupta:** Mine requires attention from pretty much 5:30, 6 a.m.

**Megan Dickey:** Do you think he's actually joining?

**Megan Dickey:** Actually, he did Slack in the morning.

**Prateek Gupta:** He wanted to discuss a few tech issues. Till then I'll also discuss with Megan since we have just a couple of minutes. Just wanted to discuss the tech issue that we are facing.

**Prateek Gupta:** So this is the main thing — there's a repeated section issue. Everything is good till the "cons" section. But what happens is, let me just pick up any articles, right? It's happening across all the articles right now. So, for example, we have the intro, company overview, pricing, benefits, features and functionality, integrations. Everything is good till the cons. But then we don't have what's supposed to be there. Instead, we have company overview, price estimate, who is it for, again — duplicate content, features, functionality, and benefits. So this is the duplicate content.

**Jenn Peters:** Okay, so it's something to do with the migration from Webflow to the CMS, there's some bugs in there somewhere?

**Prateek Gupta:** I think there's some tech issue that has to be resolved. It's happening across all the articles. Along with that, we also have some incorrect links in the article. So it's not only content, but the article is about Wormforge, but we are linking it to Salesforce, right?

**Megan Dickey:** Right, and we didn't input that information.

**Prateek Gupta:** So in the previous content, which was already there, Webflow CMS is fetching it from somewhere — I'm not sure. It's not done by us. It's fetching the old content.

**Jenn Peters:** Okay, so you're saying in this new generated content — because we're going off the ZoomInfo article — there's some extra headers in there that don't need to be in there?

**Prateek Gupta:** Yeah, it did look a bit repetitive towards the end. So the idea is, the way the headers should be structured is: whenever a visitor comes in, first we want to earn their trust on the product by giving them information about the company — how many years it's been established, what are its employees. People are very interested in knowing the pricing of the product, and then we give them benefits and functionalities. Then we go on to the other important questions in terms of pros, security, compliance, customer support — do they give daily support, chat support, email support? And then we talk about user reviews and competitors. An extra section, not needed, is "how to use" — how to use a particular product. Right now, when someone is viewing a review, they're definitely not yet signed up for the product. They're just trying to understand if the product is useful for them. So the structure is: company overview, pricing, benefits and features, then pros, security, compliance, support, then user reviews and competitors.

**Jenn Peters:** I think the last H2 I have currently is for "legal info" at the bottom of the page without an actual conclusion. Is that something you don't do on all of them?

**Prateek Gupta:** So we don't need that. This is the structure.

**Jenn Peters:** Because I'm getting really good results with the outline that I designed, so I'll just adjust this for these H2s and make some corrections.

**Prateek Gupta:** Yeah, if you send me that screenshot of that, then I'll adjust our outline to reflect that.

**Jenn Peters:** Sending that right over. Anything from Lucas?

**Prateek Gupta:** I haven't heard anything from him yet, but his status is on. I'll just text him. So I've got a green light right now. That's the first step. Thanks for sending that.

**Jenn Peters:** Yeah, I'll adjust our outline and then presumably some of the notes you had on the one that I generated have to do with these extra sections. So I'll clean that up as well. I wish I could go faster. It's just taking me a little bit of time to make a workflow that will do this at scale a bit quicker. And also Airtable being as slow as it is — because these are really big pieces, right? Anytime you get into content that's like 6,000 words long, you're going to get Airtable going really slow. And like API timeouts. Hopefully a little quicker as we go along.

**Prateek Gupta:** Also, I have personally done the publishing. It takes almost 40 minutes to publish one. That's not good. So what happens is in this new template, when I paste the content, the bullet points, everything goes off. The H2s, H3s, everything I want to add, everything disappears. So I have to manually select it and name it H1, H2, H3. When I paste from Airtable to the CMS, because it gets erased, we have to re-add the bullet points, H2s, and entries. That's a pain.

**Jenn Peters:** So you have someone doing that for you?

**Prateek Gupta:** Yes, and I also do it multiple times. I've already flagged it to Lucas in terms of publishing support. In terms of formatting being lost, he will be looking into it. We've been pushing a lot of tech fixes that we have to do. That's where a lot of the time is going. Reducing the publishing time from 40 minutes to 10 or 5 minutes is very important.

**Jenn Peters:** Especially when we're dealing with essentially programmatic pieces, the whole process should be a lot faster. I wonder if inputting it in Markdown makes a difference, if it'll retain some of the formatting.

**Prateek Gupta:** I'll just have a check with Lucas on there.

**Jenn Peters:** Yeah, that's not an ideal solution, but I've had to do some publishing in Markdown for another account. And it sometimes can retain some of the bullets and that kind of thing. But it depends on the platform and how it's set up.

**Megan Dickey:** Yeah, we'll just ping when you hear back from him. And then we can always jump on a call later.

**Prateek Gupta:** Yep, perfect. I'll keep you guys updated.

**Jenn Peters:** All right. Thank you.
