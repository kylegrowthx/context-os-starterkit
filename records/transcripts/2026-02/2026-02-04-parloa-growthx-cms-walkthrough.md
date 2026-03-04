# Parloa <> GrowthX CMS Walkthrough

<metadata>
date: 2026-02-04
time: 14:59 UTC
duration: 18 minutes
organizer: team@growthxlabs.com
participants: Dora (Parloa), Tom Nguyen-Phuoc (Parloa), William Leborgne (GrowthX)
participant_count: 3
fathom_recording_id: 119651749
fathom_url: https://fathom.video/calls/554059476
share_url: https://fathom.video/share/u1j-57daGKs2mDL-fuzuD78_fmGBj3QM
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Parloa aligned on a streamlined CMS workflow where GrowthX stages content in Storyblok and Parloa reviews and publishes it. Three action items emerged: Parloa will investigate adding schema markup fields (critical for LLM visibility), provide approved blog images by EOW, and GrowthX will document an author strategy mapping writers to content clusters to improve credibility and rotation.

---

## Context

GrowthX is producing SEO content for Parloa, a conversational AI platform, as part of a content marketing engagement. Rather than Parloa's team handling all CMS work, they want to streamline the workflow: GrowthX stages complete drafts in Storyblok, populates all fields (topics, author, image, excerpt, body copy, SEO metadata), and Parloa's team simply reviews and publishes. The goal is to reduce friction and accelerate publication while maintaining design and editorial standards. This call was a technical walkthrough to show GrowthX how to properly set up posts in Storyblok and identify any missing features (like schema markup) that would strengthen SEO performance.

---

## Relevance

**For GrowthX:**
- **CMS Workflow & Content Publishing:** Operationalizes how we stage content for Parloa; defines the interface and fields we must populate for every blog post
- **SEO & LLM Visibility:** Schema markup gap identified; critical for improving citation rates and organic visibility
- **Content Assets & Design Standards:** Sets expectations for imagery; informs how we source and prepare visual assets for partners

**For Parloa:**
- **Author Strategy & Credibility:** Opportunity to improve content perception by rotating authors and mapping them to topic clusters
- **Technical SEO Configuration:** Missing schema markup field limits on-page SEO; needs developer effort to add
- **Editorial Efficiency:** Streamlined intake reduces review overhead and accelerates time-to-publish

---

## Overview

- **Workflow:** GrowthX will stage content in Storyblok; Parloa will review and publish.
- **Schema Markup:** A critical SEO feature for LLM visibility is missing. Parloa will investigate adding it.
- **Imagery:** GrowthX's AI-generated images were rejected. Parloa will provide a new batch by EOW to meet the project's high design standards.
- **Authors:** Dora is creating a new author strategy (e.g., assigning authors to content clusters) to improve credibility and rotation.

---

## Key Topics

### CMS Publishing Workflow

  - **Goal:** GrowthX stages content in Storyblok for Parloa to review and publish, streamlining the workflow.
  - **Process:**
    1.  **Locate Content:** Navigate to `Content` → `EN` or `DE` → `blog`.
    2.  **Create Post:** Clone an existing post to preserve the template.
    3.  **Populate Fields:**
          - **Topics:** Select from existing tags.
          - **Author:** Select from the dropdown.
          - **Image:** Upload the main blog image.
          - **Excerpt:** Write a short summary.
    4.  **Format Content:**
          - Use the rich text editor for the main body.
          - **Critical:** Use `H2` tags for section headers to auto-generate the on-page table of contents.
    5.  **Add SEO & CTAs:**
          - **SEO Section:** Add meta title/description and link to the corresponding translated post.
          - **CTAs:** Use the `form section` or `button` components to add interactive elements.
  - **Status Indicators:**
      - **Green:** Published
      - **Half-green:** Saved but not published

### Schema Markup Gap

  - **Problem:** The CMS lacks a field for schema markup.
  - **Rationale:** This is a key SEO feature for improving content visibility and citation by large language models (LLMs).
  - **Solution:** Parloa will ask its web developer about the feasibility and effort required to add this field.

### Blog Imagery

  - **Problem:** GrowthX's AI-generated image examples were rejected for not meeting Parloa's high design standards.
  - **Constraint:** Storyblok uses the main blog image as the social media thumbnail; a separate thumbnail cannot be set.
  - **Solution:** Parloa will provide a new batch of approved images by EOW.

### Author Strategy

  - **Problem:** The current author list in Storyblok is outdated and lacks a clear strategy.
  - **Goal:** Create a new author strategy to improve content credibility and rotate authorship.
  - **Potential Model:** Assign specific authors (e.g., Head of Product Paul for technical topics) to content clusters defined in the SEO strategy.

---

## Decisions & Commitments

- **Content Staging Model:** GrowthX will populate complete Storyblok drafts; Parloa team reviews and publishes only.
- **Author Strategy:** Dora will map author identities to content clusters (per GrowthX's SEO strategy) to improve credibility and enable rotation.
- **Schema Markup Gap:** Escalated to Parloa's web developer for feasibility assessment; not mission-critical but recommended for LLM citation improvement.
- **Imagery Approval Cycle:** GrowthX's initial AI-generated images will be reviewed by Parloa's designer; feedback sent to William; new batch required by EOW.

---

## Open Questions

- Will Parloa's designer approve GrowthX's imagery direction, or will substantial rework be needed?
- How complex is adding a schema markup field to Storyblok? Timeline and effort?
- Is the author rotation strategy feasible within Parloa's editorial team capacity?

---

## Action Items

**William Leborgne (GrowthX)**
- Email Dora to align on Storyblok author rotation/cluster mapping strategy

**Tom Nguyen-Phuoc (Parloa)**
- Email web developer to assess feasibility and effort for adding schema markup field to Storyblok SEO section

**Dora (Parloa)**
- Review GrowthX blog image examples with designer; send feedback and direction to William
- Provide GrowthX with approved batch of blog images by end of week

---

## Transcript
**Dora:** Hey, can you hear me?

**William Leborgne:** Yes, hi.

**Dora:** Hi, how are you?

**William Leborgne:** I'm doing pretty good, how are you?

**Dora:** I'm doing good.

**Dora:** I just hope the snow in New York City could nail it away.

**William Leborgne:** It just caused a lot of vessels.

**William Leborgne:** I can imagine.

**Dora:** The travel times take forever because the street becomes, it's already very packed and narrow the streets.

**William Leborgne:** And then now...

**Dora:** With the snow, like, when people collect the garbage, it takes forever.

**Dora:** I feel bad with them because they have to climb on the ice and then they will have to wait for forever.

**Dora:** It's a crazy winter.

**William Leborgne:** Yeah, that's crazy.

**Dora:** That's rough.

**William Leborgne:** Is there some part of you that likes it, though, that's kind of like magical New York with the Christmas tree and the snow falling?

**Dora:** Usually that start, it only lasts like for 30 minutes.

**Dora:** And then when there's just too many people and cars and then, like, all the snow actually became, like, black with the grease on it.

**Dora:** It's not very pretty.

**William Leborgne:** No, that's not so pretty.

**Dora:** Let me pin Tom really quick.

**Dora:** I might have to hop up of the call halfway because I'm double booked, but I think that's okay because Tom is the expert.

**Dora:** I am relatively useless here.

**Dora:** Let me just pin here.

**Dora:** Let me just pin here.

**William Leborgne:** Well, see him on the call.

**Tom Nguyen-Phuoc:** Yeah.

**Dora:** Is he here?

**Dora:** Oh, I've been talking, trying to hold the floor.

**Dora:** Tom, I didn't know you were here.

**Dora:** Yeah, so Tom, I think my internet.

**Dora:** So I just want to give you a context I think I shared with you a little bit before, like GrowthX is our SEO agencies, and then William is our point of contact and leading the whole SEO event project with us.

**Dora:** And he had some questions about like how we track with CMS.

**Dora:** I cannot stay in this meeting for the entire time, but I will just stay for like 10 minutes.

**Dora:** yeah, Because as I say, really, like Tom is the expert.

**Dora:** I don't have the expertise and knowledge as he does, but I'll be around for a little bit.

**William Leborgne:** Yeah, no problem.

**William Leborgne:** Honestly, Tom, really what we're doing here is just getting a brief.

**William Leborgne:** Walkthrough of how you would publish content, because the idea here is that we would be producing content and then staging it, so going into your CMS and actually setting it up, and then you guys just have to press the publish button, simplify everyone's job, make sure that everything goes smoothly.

**William Leborgne:** So if you just want to open up, share your screen, show me your process for publishing blog posts, that's what we needed.

**William Leborgne:** We should be in and out in 10 minutes.

**Tom Nguyen-Phuoc:** Yeah, okay, that's super fast, and I can show it to you.

**Tom Nguyen-Phuoc:** So basically, once you will have access to StoryBlog, you'll just have to select the account, then you will arrive on that page.

**Tom Nguyen-Phuoc:** On the left side, you will have the content section, and then you will see two folders, E and E, so E for German website, E and for the English one.

**Tom Nguyen-Phuoc:** So when you click, you have new folders here.

**Tom Nguyen-Phuoc:** You just have to find the blog one, I believe, which is just here.

**Tom Nguyen-Phuoc:** Otherwise, you can just put it in the search bar just there.

**Tom Nguyen-Phuoc:** So, all right, let me just open it.

**Tom Nguyen-Phuoc:** So if I go in the blog one, then here you will see all of the blog posts that we have on the website.

**Tom Nguyen-Phuoc:** If they are green, it means that it's published.

**William Leborgne:** If they are half green, there were some changes that have been saved, but it was not published.

**Tom Nguyen-Phuoc:** What we do usually is we just clone one.

**Tom Nguyen-Phuoc:** So we just select it, clone, and then I'll call it test.

**Tom Nguyen-Phuoc:** Then we duplicate it.

**Tom Nguyen-Phuoc:** Once you're there, it's pretty simple, right?

**Tom Nguyen-Phuoc:** You can select the topic that we have.

**Tom Nguyen-Phuoc:** If you need new ones that I believe Brad can help Dora to create some, or I could have a look, but it should not be that long.

**Tom Nguyen-Phuoc:** Then you have the author that you could select.

**Tom Nguyen-Phuoc:** have multiple ones.

**Tom Nguyen-Phuoc:** If you need to add some.

**Tom Nguyen-Phuoc:** At some point, you can also ask us.

**Tom Nguyen-Phuoc:** It's just in another folder where you would have to duplicate an old one and just change the text.

**William Leborgne:** I don't think we're going to need to duplicate, but what we will need to do, Dora, is just clarify which author is for what type of content.

**William Leborgne:** Or you could just have one author for everybody.

**Dora:** That's really good.

**Dora:** That's actually what I'm working on.

**Dora:** So I asked our current freelancer to pull out the pull of the authors in Storyblocks.

**William Leborgne:** And you could see some of them, they're actually not working on Parloa anymore.

**William Leborgne:** So I'm going to categorize that and then we'll do a rotation.

**Dora:** Because if you go to our website, you might see that it's being ungeneral, like our single content marketer.

**Dora:** But I think it would be good to rotate and then that's a side project that I'm working on now.

**Dora:** So I will share that information with you too.

**William Leborgne:** So what some of our clients will do is they'll go through those clusters that I shared with you in the content strategy and just say, this cluster is this author.

**William Leborgne:** You know, and this cluster is this author and so on and so forth.

**William Leborgne:** And this is basically...

**William Leborgne:** So if it's something that's very technical, then maybe you would have your head of product, Paul, and maybe if it's something else, it would be somebody else, if that makes sense.

**Tom Nguyen-Phuoc:** Right.

**Tom Nguyen-Phuoc:** So once you're there, you can select the image and select another one or just upload one that you will probably receive from our design team.

**Tom Nguyen-Phuoc:** You have the excerpt here that you can edit.

**Tom Nguyen-Phuoc:** And then here, so it's basically just like a normal like field that you can just add.

**William Leborgne:** rich text editor.

**Tom Nguyen-Phuoc:** Yeah.

**Tom Nguyen-Phuoc:** The only thing that you have to know is that if you want to have this little table on the left side, you will have to always put the H2.

**Tom Nguyen-Phuoc:** Like here, it's H1 for the first one, but I'm also confused why is it an H1 because the H1 should be this one, but we can take that later.

**Tom Nguyen-Phuoc:** And basically, we'll call the H2 on the left side.

**Tom Nguyen-Phuoc:** Okay.

**William Leborgne:** I don't know if it creates the index.

**Tom Nguyen-Phuoc:** Great.

**Tom Nguyen-Phuoc:** Yeah.

**Tom Nguyen-Phuoc:** And then it's just like...

**Tom Nguyen-Phuoc:** A normal editor if you want to add some bold or bullet points and stuff.

**Tom Nguyen-Phuoc:** You have the SEO section here where you can add the meta file to a meta description.

**Tom Nguyen-Phuoc:** And if you need to link an English version to a German one, then you will just have to select the German blog post and save it.

**Tom Nguyen-Phuoc:** And then your connection will be done.

**Tom Nguyen-Phuoc:** But other than that, that's pretty much like if you have to add a form somehow, you can just add one by clicking here and then select form section.

**Tom Nguyen-Phuoc:** Same for the button that we have here.

**Tom Nguyen-Phuoc:** And then just select the page that we want to be used as the redirect of the CTA.

**Tom Nguyen-Phuoc:** But other than that, yeah, that's pretty straightforward. If you have any questions, you can send me a mail or a Slack message and I'll definitely help out.

**William Leborgne:** No, this is great.

**William Leborgne:** StoryBlock is very, very simple.

**William Leborgne:** So I'm glad that that's what you guys are using.

**William Leborgne:** I just have one question, which is typically for SEO purposes, we will include a schema markup.

**William Leborgne:** And in your SEO section, I don't see a place for that.

**William Leborgne:** This is not mission critical, but it's something that is really ideal, especially for getting cited by LLMs.

**William Leborgne:** So maybe there's something, could you look into that and just see like how difficult would it be to add a schema markup section in the SEO part?

**Tom Nguyen-Phuoc:** Yeah, we'll just have to ask our web developer for that.

**William Leborgne:** Okay.

**Tom Nguyen-Phuoc:** And I see Dora also saying yes.

**Dora:** Yeah.

**Tom Nguyen-Phuoc:** Okay.

**Dora:** I could, I could either take it.

**Tom Nguyen-Phuoc:** And the only thing too, is that the, um, thumbnail will be taken from, uh, the image that we add here.

**William Leborgne:** Okay.

**William Leborgne:** Well, that's great.

**William Leborgne:** That makes it easy.

**Tom Nguyen-Phuoc:** Yeah.

**Tom Nguyen-Phuoc:** So we don't have like, you basically.

**Tom Nguyen-Phuoc:** You cannot have a different thumbnail than the image that you have on the website.

**William Leborgne:** That's fine.

**William Leborgne:** Yep.

**Tom Nguyen-Phuoc:** Okay.

**William Leborgne:** Great.

**William Leborgne:** Well, actually, Dora, we did actually put together, I was going to share this with you later, but since I have you here, I'll just show it to you real quickly.

**William Leborgne:** We file a ticket internally for the imagery that we're going to be working on.

**William Leborgne:** Where is it?

**William Leborgne:** One second.

**Dora:** Yeah.

**Dora:** Can you remind me again the request you're going to have?

**Dora:** I just want to make sure I don't, I don't.

**William Leborgne:** Remind you of what type?

**Dora:** The LLM scheme, like.

**William Leborgne:** Oh, schema markup.

**William Leborgne:** Yeah.

**Dora:** Okay.

**William Leborgne:** It's like this.

**William Leborgne:** Schema markup.

**Dora:** I want make sure I spell that code up.

**William Leborgne:** Okay.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** Okay.

**William Leborgne:** Just open this to get.

**William Leborgne:** And then this pipeline.

**William Leborgne:** Okay.

**William Leborgne:** Okay, here we go.

**William Leborgne:** So, here you are.

**William Leborgne:** So we, based off of the imagery that's already existing on your website, we created our own image generator.

**William Leborgne:** So here's some examples of images that we would use for the blog.

**William Leborgne:** I just, since I have you on the call, I just want to check.

**William Leborgne:** Does this feel like the right direction?

**William Leborgne:** Would you want to change it?

**Dora:** I think we might need to change a little bit.

**Dora:** Would you mind sharing this with me?

**Dora:** I would like to have our designer also take a look.

**Dora:** I think this looks like what we have.

**Dora:** That's right.

**Dora:** We have a very, very high standard.

**Dora:** Okay.

**Dora:** the design.

**Dora:** Thank

**Dora:** And the image on our website, so maybe at the end we will have to provide our own, but please share that with me, I'll double check, and I don't know if, since you're here, I responded to you on the conversational AI.

**William Leborgne:** I saw.

**Dora:** Yeah.

**William Leborgne:** Yes, we got the, go ahead.

**William Leborgne:** Yeah, that's great.

**William Leborgne:** I'm very excited about that.

**William Leborgne:** Here are the blog images that we put together.

**William Leborgne:** Let me know.

**Dora:** Thank you a lot.

**William Leborgne:** Okay, I'm just putting this in the, in our chat together on Slack.

**William Leborgne:** And, and then, yeah, if there's no, if there's no, like, delay, that's, that's our biggest concern, obviously, is like, if we can just get, like, a batch of images, and there's no specific correlation between the image and the blog, you know, it's sort of abstract, then, then we're, we're happy.

**Dora:** Okay.

**Dora:** Okay.

**Dora:** I think we should be able to give you by end of this week.

**Dora:** Okay.

**Dora:** Okay.

**Dora:** We do have an inventory of all those languages, so it should be fine.

**William Leborgne:** Okay, super.

**William Leborgne:** Great.

**Dora:** Cool.

**Dora:** Anything else?

**William Leborgne:** That's it.

**William Leborgne:** Well, I'm going to see you in a little bit.

**Dora:** Yes.

**Dora:** Tom, thank you a lot for jumping in.

**William Leborgne:** Appreciate it.

**Dora:** If you have questions, send it to me.

**William Leborgne:** I'll answer.

**William Leborgne:** Okay.

**Dora:** Sounds good.

**Dora:** Bye-bye.

**William Leborgne:** Bye-bye.
