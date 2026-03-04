# Patricia/Lawrence (Siit)

<metadata>
date: 2026-01-08
time: 20:07 UTC
duration: 44 minutes
organizer: lawrence@growthx.ai
participants: Patrícia Contreiras, Lawrence Neves
fathom_recording_id: 112897676
fathom_url: https://fathom.video/calls/526803387
share_url: https://fathom.video/share/FgZFiFMHEgBFQ8FE_aMwM7yp-sAz9UzZ
source: fathom
enriched_on: 2026-02-28 12:30 UTC
</metadata>

---

## Summary

Lawrence walks Patrícia through the Siit content account operations, explaining the two primary content workflows (blog articles at 5/week and tool pages at 10/week), quality control requirements including manual verification of AI-generated tool integrations, and the importance of maintaining consistency across published content. The call addresses pipeline setup, naming conventions, archival of unused editorial resources, and next steps for Patrícia's onboarding as the new content lead for the account.

---

## Context

Patrícia Contreiras is onboarding to GrowthX's Siit content account following recent team transitions. Lawrence Neves, who joined GrowthX roughly three months prior to this call, is leading the onboarding and has been managing Siit deliverables for approximately two months. Siit is characterized as a high-quality, collaborative client that relies heavily on GrowthX for content marketing—they expect consistent output (15 articles/week across two content types) and maintain a positive working relationship with minimal rejection rates.

The operational context centers on managing an editorial pipeline that generates two distinct content formats: blog articles (5 per week) and tool pages (10 per week). The client's success metrics focus on SEO rankings and content consistency, with Matt serving as the primary point of contact for editorial direction and final review. The infrastructure includes Notion documentation, Airtable editorial pipelines, and Claude-based post-processing workflows to ensure quality and brand alignment.

---

## Relevance

- **Content Operations**: Detailed walkthrough of GrowthX's editorial pipeline infrastructure, templating systems, and post-processing workflows for high-volume content delivery.
- **Quality Assurance**: Critical guidance on identifying and correcting AI hallucinations (fabricated tool integrations), the most common error type requiring manual intervention.
- **Client Management**: Insights into Siit's collaborative nature, expectations for turnaround and consistency, and the role of editorial leadership (Matt) in quality control.
- **Process Documentation**: References the Notion document as the authoritative source for detailed step-by-step instructions; outlines reasoning for pipeline organization and naming conventions.
- **Competitive Strategy**: Establishes rules for handling competitor mentions in content (e.g., Siit placement in ITSM tool listicles and alternatives pages).
- **Onboarding Framework**: Applicable to new content leads joining GrowthX, covering both tactical workflow knowledge and cultural/client relationship context.

---

## Overview

- **Two Content Types:** Blogs (5/wk) require manual post-processing for consistency. Tool Pages (10/wk) are highly templated, needing only quick edits for factual accuracy.
- **Critical AI Hallucinations:** The AI frequently fabricates tool integrations. This must be manually verified and corrected, as it is the most common error.
- **Post-Processing for Consistency:** Use Claude to enforce a consistent style. Prompt it to mimic the structure and tone of the last 3 published articles of the same type.
- **Competitor Strategy:** For listicles featuring Siit competitors (e.g., ITSM tools), always list Siit as the \#1 option.

---

## Key Topics

### Blog Articles (5/wk)

  - **Workflow:** Matt assigns topics in the Airtable editorial pipeline.
  - **Process:**
    1.  **Generation:** Use the "Article Generation with new artifacts" pipeline.
    2.  **Input:** Enter only the topic. Select the correct article type (e.g., "listicle") to prevent incorrect formatting (e.g., a "how-to" article).
    3.  **Post-Processing (in Claude):**
          - **Consistency:** Prompt Claude to match the style of the last 3 published articles of the same type.
          - **SEO:** Generate meta titles and URL slugs in Claude, as the pipeline's generator is unreliable.
  - **Editing & Verification:**
      - **Factual Accuracy:** Verify all stats and numbers.
      - **Sourcing:** Use only credible sources (.org, .gov, .edu, major research firms). Avoid competitor blogs and studies sponsored by competitors.
      - **Competitor Listicle Rule:** If a listicle covers a category where Siit is a competitor (e.g., ITSM), list Siit as the \#1 option.
      - **Convergence Reports:** Treat these as suggestions for improvement, not mandatory fixes. Do not update writing guidelines based on them.

### Tool Pages (10/wk)

  - **Overview:** Highly templated articles requiring minimal post-processing.

  - **Process:**
    
    1.  **Generation:** Input the tool name (and domain for Overviews).
    2.  **Post-Processing:**
          - **Consistency:** Prompt Claude to match the style of the last 3 published articles of the same type.
          - **Factual Accuracy:** Verify links and stats.
          - **Integrations:** Manually remove any hallucinated integration claims.
          - **Competitor Rule:** For alternatives pages, if the tool is a Siit competitor, prompt Claude to list Siit as the \#1 alternative.

  - **Types & Specifics:**
    
      - **Tool Overview with Images:**
          - **Input:** Requires the tool's domain (e.g., `rippling.com`) to generate the logo and prevent the pipeline from failing at the "brand search" step.
          - **Structure:** Includes a standard "When the tool isn't enough, meet Siit" section for tools that don't integrate.
      - **Tool Comparison:**
          - **Input:** Enter two tool names (e.g., `PagerDuty`, `Incident.io`).
          - **Structure:** Includes a side-by-side comparison table and a section on how Siit can help, even if no direct integration exists.
      - **Tool Alternatives:**
          - **Input:** Enter one tool name (e.g., `Zapier`).
          - **Structure:** Lists alternative tools. If the subject tool is a Siit competitor, prompt Claude to list Siit as the \#1 alternative.

---

## Action Items

**Lawrence Neves** (GrowthX)
- Archive unused SEAT Editorial pipelines in Notion/Airtable
- Review Patrícia's new campaign pipeline

**Patrícia Contreiras** (GrowthX)
- Ask Matt (Siit) re: SEAT Guides; update Notion doc if needed

---

## Transcript
**Patrícia Contreiras:** Like jumping aboard a new client is always messy, is always all over the place.

**Patrícia Contreiras:** So thank you.

**Patrícia Contreiras:** And I know day-to-day business is complicated as well.

**Patrícia Contreiras:** So thank you for this time.

**Lawrence Neves:** It's actually, if you were going to ever get a client, this would be the best one to get.

**Lawrence Neves:** They're just, they're really easy to take care of.

**Lawrence Neves:** They're very, very nice people.

**Lawrence Neves:** The woman that I've seen her interaction with Matt and with me, whenever I send articles to them, they're very much like, oh, thank you for that.

**Lawrence Neves:** I appreciate it.

**Lawrence Neves:** She doesn't have a lot of reviewing of the articles.

**Lawrence Neves:** They pretty much take them as they are.

**Lawrence Neves:** Matt does review them, and I'm sure he's going to review yours the first couple of times.

**Lawrence Neves:** But they're really, really easy to do.

**Lawrence Neves:** So there are two types of articles.

**Lawrence Neves:** That's their blog articles, which you'll find in the editorial.

**Lawrence Neves:** Oh, did you get a chance to get into that Notion doc?

**Lawrence Neves:** Did that work for you?

**Lawrence Neves:** Yeah, yeah.

**Patrícia Contreiras:** I reviewed it, but I also had a campaign to go through and to create an architect for that.

**Patrícia Contreiras:** So I didn't get really in the depth.

**Patrícia Contreiras:** no, that's okay.

**Patrícia Contreiras:** That's okay.

**Lawrence Neves:** So there's basically two kinds of articles for Seat.

**Lawrence Neves:** There's their blog articles, which are five a week.

**Lawrence Neves:** They expect five a week.

**Lawrence Neves:** And then there's their tool pages, which I'm going to walk through.

**Lawrence Neves:** I think it'd be best if I just walk through it while we're on the call.

**Lawrence Neves:** I'll share my screen and we'll go through that because they're really, really easy to do.

**Lawrence Neves:** There's a lengthy explanation in the Notion doc that shows you how to go step-by-step for each of the tool pages.

**Lawrence Neves:** So there's three types of tool pages.

**Lawrence Neves:** There's the tool overview.

**Lawrence Neves:** There's a tool comparison.

**Lawrence Neves:** And then there's something called a tool alternative.

**Lawrence Neves:** So the great thing about these is all of those are templated.

**Lawrence Neves:** You are basically, like, so for the tool overview, you just type in what tool you're talking about.

**Lawrence Neves:** That's it.

**Lawrence Neves:** You don't look for, you don't do any searching for keywords or anything like that.

**Lawrence Neves:** So I just did one for Jenkins.

**Lawrence Neves:** You just type in Jenkins and the whole back end of the pipeline takes care of it.

**Lawrence Neves:** They find Jenkins.

**Lawrence Neves:** They were.

**Lawrence Neves:** Realize that Jenkins is part of the I.O.

**Lawrence Neves:** space.

**Lawrence Neves:** They write the whole thing of what Jenkins are.

**Lawrence Neves:** All of the tools pages follow a template that they all should follow.

**Lawrence Neves:** And they're really, like I said, I'll walk you through it, but they're really easy to do.

**Lawrence Neves:** The blog.

**Lawrence Neves:** So I just started on Seat maybe two months ago.

**Lawrence Neves:** I think I've only been here for like three months.

**Patrícia Contreiras:** I feel like it's been a year for me.

**Patrícia Contreiras:** And I think it's been like five months at Topps and I'm already, oh my God.

**Patrícia Contreiras:** Yeah, I know.

**Patrícia Contreiras:** It can be a lot.

**Lawrence Neves:** That's why I'm so glad you're asking questions.

**Lawrence Neves:** You know, when you said you're pestering me, you're not pestering me.

**Lawrence Neves:** Trust me.

**Lawrence Neves:** I've asked so many questions of so many people and I realize that's the only way to get anything done around here because if you don't ask questions, you're not going to know.

**Lawrence Neves:** And a lot of this is overwhelming.

**Lawrence Neves:** Look, I don't even know how to set up meetings right now.

**Lawrence Neves:** So I'm still learning a bunch of stuff.

**Lawrence Neves:** There's so many good stuff to learn.

**Patrícia Contreiras:** It's incredible.

**Patrícia Contreiras:** It is.

**Patrícia Contreiras:** It is.

**Lawrence Neves:** So the blog articles, basically they'll, you know, you've seen the Enable Content OS.

**Lawrence Neves:** Matt will pick out five articles for the week.

**Lawrence Neves:** You're going to go right into their editorial.

**Lawrence Neves:** Pipeline.

**Lawrence Neves:** I archived all the editorial pipelines that we don't use.

**Lawrence Neves:** the only thing that should be up there now, let me just double check this real quick.

**Lawrence Neves:** The only one, let's see, artifacts.

**Lawrence Neves:** Yes, the only, yeah, so there are, yeah, actually, I didn't archive these other two because I don't know what they are.

**Patrícia Contreiras:** But if we're not using them, you can just archive them and then if we eventually need to use them, we just un-archive them, you know, it's less confusing even if someone else steps in, if I have to take time off and you can't help, so someone wouldn't get as confused as we usually do whenever we're looking at pipeline.

**Patrícia Contreiras:** Right.

**Lawrence Neves:** Okay, let me, let me just, I'm sorry.

**Lawrence Neves:** Okay, let me just share my screen real quick.

**Patrícia Contreiras:** So you mentioned you did run some conflict checks with the artifacts.

**Patrícia Contreiras:** yes.

**Patrícia Contreiras:** And found several issues with several artifacts.

**Patrícia Contreiras:** But did you get the chance?

**Patrícia Contreiras:** I noticed you updated the writing guidelines.

**Patrícia Contreiras:** I think there's three.

**Patrícia Contreiras:** I'm not sure which one was it.

**Patrícia Contreiras:** Right.

**Patrícia Contreiras:** And the 29th of December.

**Patrícia Contreiras:** I think that's the general one.

**Patrícia Contreiras:** Did you have a chance to update the other ones?

**Patrícia Contreiras:** So I have not had a chance to update the other ones.

**Lawrence Neves:** A big reason for that, too, is that because the pipelines work the way they're supposed to work, I haven't really had to make any changes.

**Lawrence Neves:** But you're going to find as we walk through this, you're to find there are certain things that you're probably going to want to alert somebody about that nobody has been alerted about.

**Lawrence Neves:** So I've been doing a lot of the backend work in Claude.

**Lawrence Neves:** of I've

**Lawrence Neves:** And it actually should be done through the pipeline.

**Lawrence Neves:** Let me just see if I can share this.

**Lawrence Neves:** Pipelines editorial, here we go.

**Lawrence Neves:** Okay, so do you see my, the screen says article gen, there it goes, yes.

**Lawrence Neves:** So this is the seat, the seat thing.

**Lawrence Neves:** You go to editorial, and then those are the only two there.

**Lawrence Neves:** I'll leave article refresher up there because I had a question about that that I want to ask.

**Lawrence Neves:** I mean, actually, we can archive it.

**Lawrence Neves:** Like you said, if you need it, you can always go back to it.

**Lawrence Neves:** So article generation with new artifacts, and then this works like any other article generation.

**Lawrence Neves:** You just add the thing, you put the topic in there, and then you give it the assignment direction.

**Lawrence Neves:** What Matt likes to do is Matt likes to take the keyword and then do a search for the search engine result page for the keyword and see what other people are talking about that.

**Lawrence Neves:** However, I do notice he has also given direction that a lot of.

**Lawrence Neves:** These things should look like the other pages on the site.

**Lawrence Neves:** So he doesn't want us to stray too far from what the other pages have looked like.

**Lawrence Neves:** So I'm just going to take an example.

**Lawrence Neves:** Actually, let me just go into the Airtable and see what we're working on for C.

**Lawrence Neves:** Actually, yeah, so this is the one I worked on.

**Lawrence Neves:** So basically, the assignment direction was craft an article.

**Lawrence Neves:** You want the 12 best company, include the intro.

**Lawrence Neves:** And then this, the direction I gave it here, what is a company wiki?

**Lawrence Neves:** Why do you need one?

**Lawrence Neves:** What happens if you don't want to have one?

**Lawrence Neves:** What makes it?

**Lawrence Neves:** These are all taken from another article.

**Lawrence Neves:** And I'm going to just really quickly go to that and show you.

**Lawrence Neves:** And Matt just really, because they're such a great client, they work with us really well.

**Lawrence Neves:** So it's basically doing CERP results, checking the CERP results.

**Patrícia Contreiras:** CERP, CERP results.

**Patrícia Contreiras:** go.

**Patrícia Contreiras:** And compile all that's necessary, what that's ranking well, and putting it all together in the same article and creating that with the ton of our client.

**Lawrence Neves:** Right.

**Lawrence Neves:** So that article was, sorry, was 12 Best Company Wiki Softwares.

**Lawrence Neves:** So 12 Best Employee Audit, we're going to use this as an example.

**Lawrence Neves:** They all follow up pretty much the same thing.

**Lawrence Neves:** It's the title, what is it?

**Lawrence Neves:** Best Employee Onboarding Software, Quick Comparison.

**Lawrence Neves:** So these listicles, the template creates all of this.

**Lawrence Neves:** So, and then it goes through, again, goes through the whole listing of it.

**Lawrence Neves:** The only thing you need to check is to make sure if they actually integrate with Seat, we want to make sure that we put the, the D, can have do see um, it

**Lawrence Neves:** I'm sorry.

**Lawrence Neves:** Where it integrates with SITS.

**Lawrence Neves:** Oh, maybe none of this does.

**Lawrence Neves:** So if it integrates with SITS, I'll find another one that actually integrates with SITS.

**Lawrence Neves:** There should be a little thing here that says integrates with SITS, or sometimes they put it in the key features integrates with SITS, and then you just want to make sure that you link that to SITS integration page.

**Lawrence Neves:** Mm-hmm.

**Patrícia Contreiras:** So it's it's very close to what I'm already doing with my current client, so.

**Patrícia Contreiras:** Right, right, right.

**Patrícia Contreiras:** Who are you watching with now?

**Patrícia Contreiras:** Tavern.

**Lawrence Neves:** Oh, Tavern.

**Lawrence Neves:** Oh, he just sent me some examples of that.

**Lawrence Neves:** He wants me to use those in something else that we're doing.

**Lawrence Neves:** It's actually really good stuff on Tavern.

**Lawrence Neves:** So that's, yes, you're set for that.

**Lawrence Neves:** But the only thing you need to do, and again, let me just go into the Airtable and see.

**Lawrence Neves:** Editorial blogs, and production.

**Lawrence Neves:** So I actually did all of these.

**Lawrence Neves:** He hasn't looked at them yet.

**Lawrence Neves:** Okay.

**Lawrence Neves:** I'm just going to open up this one, 11 Best Facility Management Software.

**Lawrence Neves:** I'm going to go into it.

**Lawrence Neves:** So basically, what this is, what is this?

**Lawrence Neves:** Here's the quick look.

**Lawrence Neves:** Again, you don't even have to make this chart.

**Lawrence Neves:** When you go in.

**Patrícia Contreiras:** I think you're not sharing that screen.

**Patrícia Contreiras:** I think you're in another screen.

**Patrícia Contreiras:** I don't know.

**Lawrence Neves:** Yeah.

**Lawrence Neves:** So there we go.

**Lawrence Neves:** So basically, it's the title, what it is.

**Lawrence Neves:** to is.

**Lawrence Neves:** This table, the comparison table.

**Lawrence Neves:** Do you always have a lot of tables?

**Lawrence Neves:** I think there's a table in everything that Seat does.

**Lawrence Neves:** Just because they like that.

**Patrícia Contreiras:** Whatever the client wants.

**Patrícia Contreiras:** Right, basically.

**Patrícia Contreiras:** I'm just clearing it up because Tavern doesn't rarely.

**Patrícia Contreiras:** Doesn't like tables?

**Patrícia Contreiras:** Okay.

**Lawrence Neves:** Yeah, you're going to find that Seat actually has tables in almost everything that they do.

**Lawrence Neves:** Let me just share this screen now.

**Lawrence Neves:** So here are their blogs.

**Lawrence Neves:** So these listicles, anytime there's a listicle, there's a table.

**Lawrence Neves:** Of comparisons and all of that.

**Lawrence Neves:** Comparisons, right, and then the list of the things there.

**Lawrence Neves:** We just want to make sure in the template that you use for this, it'll say integrating, how you integrate these.

**Lawrence Neves:** Matt likes us to put whatever the tools are.

**Lawrence Neves:** So these are performance management tools.

**Lawrence Neves:** These are all performance management tools.

**Lawrence Neves:** If they are a competitor to SEAT, and this is in the Notion doc, if they're a competitor to SEAT, we want to make sure that SEAT is always the first alternative.

**Lawrence Neves:** I'm sorry, that's for alternatives.

**Lawrence Neves:** That's not for management performance tools.

**Lawrence Neves:** But if it is, if this is like, let's say, five best ITSM, because SEAT is an ITSM, if it is five best ITSMs, we want to make sure that SEAT is listed as number one in there.

**Lawrence Neves:** And then, you know.

**Patrícia Contreiras:** Yeah, great.

**Patrícia Contreiras:** It's going to be easier to integrate that.

**Patrícia Contreiras:** Cool.

**Patrícia Contreiras:** Let me go back to this.

**Patrícia Contreiras:** Let me share this now.

**Patrícia Contreiras:** Similarities.

**Lawrence Neves:** Yeah.

**Lawrence Neves:** Okay.

**Lawrence Neves:** So getting back to this now.

**Lawrence Neves:** Yeah, you give it a very simple assignment direction.

**Lawrence Neves:** And then when you actually get down to the...

**Lawrence Neves:** When you run the post-processing on it, what I always like to do is say, match this against the writing guidelines, I put in all the artifacts that it's going to need for that, and then I also say, please check these links for format and structure, and then just give them the last three blogs that we've published that aren't, if it's a listicle like this, just give them the last three listicle blogs in the Cloud Project.

**Lawrence Neves:** Just say, try it.

**Lawrence Neves:** And the reason we do that is because, like, I'm the third person on this account.

**Lawrence Neves:** So there's been some inconsistency across the account with how things are done.

**Lawrence Neves:** Now Matt just wants it kept consistent.

**Lawrence Neves:** So we just say, look at this article.

**Lawrence Neves:** This is exactly how this article is laid out.

**Lawrence Neves:** This is how this article should be laid out.

**Lawrence Neves:** There's not a lot that we do in these, you know, of course, you're going to do all of your editing on this.

**Lawrence Neves:** You're going to look and make sure that all of this stuff is factually correct.

**Lawrence Neves:** I always blanch whenever I see numbers.

**Lawrence Neves:** Because number one, this isn't linked, and it should have been.

**Lawrence Neves:** But also, Atlas just never gets them right.

**Lawrence Neves:** And I always have to go through and change all that.

**Lawrence Neves:** So this one actually has not been submitted yet.

**Lawrence Neves:** So I'm going to have to go through that when I do the editing on that to make sure that all of those are checked.

**Lawrence Neves:** But there's not a lot of links in there.

**Lawrence Neves:** There shouldn't be a lot of links in there.

**Lawrence Neves:** Of course, we're going to want to link any numbers and stats.

**Lawrence Neves:** But when you get down to here, like, you know, like the link here is to, according to Invigate's ITSM statistics, Invigate is a competitor.

**Lawrence Neves:** So we don't want to use that.

**Lawrence Neves:** So we're going to have to find some other source for that.

**Lawrence Neves:** Or I tell Claude to make them stat agnostic, make the statement stat agnostic, and it'll take the stat out and it'll just say, you know, ITMs do this and not give you a thing for it.

**Patrícia Contreiras:** Sorry, do we have the same thing for mentioning blogs?

**Patrícia Contreiras:** We avoid mentioning blogs and only alternative sources or...

**Lawrence Neves:** It should be in the guideline, but I think that they only want, I know most of my clients only want .org, .gov, .eu or mentions of their own statistics if they do their own statistics.

**Lawrence Neves:** But I know a lot of my blogs will accept, a lot of my clients will accept Gartner, Forrester, IDC, like really big name research firms.

**Lawrence Neves:** The problem with that is a lot of those research firms do statistical studies in partnership with one of the competitors.

**Lawrence Neves:** So like in this case, Invigate is a partner with us.

**Lawrence Neves:** That may be a Gartner study, but Invigate asked for them to make that study, and then we don't want to quote that if that's the case.

**Lawrence Neves:** That's always the tricky part.

**Lawrence Neves:** Of course, working with Atlas and...

**Patrícia Contreiras:** It's just avoid it.

**Lawrence Neves:** Oh, it's just avoid it.

**Lawrence Neves:** I always just try to avoid it if I can.

**Lawrence Neves:** But that's basically it for that, for the blogs.

**Lawrence Neves:** So they're like...

**Lawrence Neves:** Like I said, they're pretty simple.

**Lawrence Neves:** I, Matt Panzer, Matt Panzerino has been telling us to keep the article, to keep the article research, not research topics, the input really brief if we can't and let Atlas do the work.

**Lawrence Neves:** Matt Hill, our, our team.

**Patrícia Contreiras:** really depends for someone to try that and that didn't work.

**Patrícia Contreiras:** Right, right, right.

**Lawrence Neves:** So Matt, our, yeah, Matt, um, Alvis Hill, he does not believe that, um, Atlas is, is really great at a lot of that stuff.

**Lawrence Neves:** So I run a lot of the projects through Claude and just ask Claude to fix it up.

**Lawrence Neves:** What I try to avoid is having Claude rewrite everything because of what's the point of that?

**Lawrence Neves:** mean, I shouldn't have been doing that in Atlas, but yeah, if you run these through Claude and through the Claude, um, guidelines and everything, you'll, you'll come out with cleaning up, you know, articles that are clean, that are ready to go.

**Patrícia Contreiras:** Yeah, I mentioned earlier in a, in a new pipeline that I created for the campaign.

**Patrícia Contreiras:** Yes, I saw it.

**Patrícia Contreiras:** I copied the way you are doing it.

**Patrícia Contreiras:** And I think it was all right.

**Patrícia Contreiras:** Okay.

**Patrícia Contreiras:** All right.

**Patrícia Contreiras:** Those are ready.

**Lawrence Neves:** I really want to look at those because I'm really interested to know about that new campaign that they're doing.

**Lawrence Neves:** So let's just quickly go into this.

**Patrícia Contreiras:** I want you another question about that past pipeline, please.

**Patrícia Contreiras:** Could you go back?

**Patrícia Contreiras:** Yeah.

**Patrícia Contreiras:** Yes.

**Patrícia Contreiras:** I wanted to question you about the – click on any topic.

**Patrícia Contreiras:** I just want to see the pipeline, the input.

**Patrícia Contreiras:** Oh, the input, sure.

**Patrícia Contreiras:** Yeah.

**Patrícia Contreiras:** Do you – is there any time that you use – put in a subtitle, an alter name, or when have I used that?

**Lawrence Neves:** No.

**Lawrence Neves:** Yeah.

**Lawrence Neves:** I don't – I have never done that for SEAT.

**Lawrence Neves:** I have not – I have not seen us – Yeah, because I noticed all

**Patrícia Contreiras:** These fields empty, and I was wondering, are we ever going to use that?

**Patrícia Contreiras:** Should I use that?

**Patrícia Contreiras:** Oh, you're talking about up here.

**Patrícia Contreiras:** Oh, no, I never.

**Lawrence Neves:** The only thing I feel up here is the topic.

**Lawrence Neves:** Yeah.

**Lawrence Neves:** And I don't use the, Matt said not to use their generator.

**Lawrence Neves:** Again, you can see why, because he says he says to never use these meta titles or meta titles.

**Lawrence Neves:** I always run that through Claude, and when I do the checking Claude, I said, please provide the meta title for that.

**Lawrence Neves:** And then, of course, the URL slugs are always going to be whatever the keywords were.

**Lawrence Neves:** So smart tours are going to be for that.

**Patrícia Contreiras:** Yeah, I just wanted to know that, because I'm going to have to generate new pipelines and all that, and I want to make sure I'm doing the right layout, so whenever someone else takes the account or helps out, they aren't like, should I put in something in here?

**Patrícia Contreiras:** What should I do with these fields, you know?

**Lawrence Neves:** I've never done this.

**Lawrence Neves:** I've never been asked to do this.

**Lawrence Neves:** I've...

**Lawrence Neves:** I've never done this and had somebody say, oh, you need to fill that out.

**Lawrence Neves:** There is going to be a thing I'm going to show you that's a weird thing that was bothering me for weeks on this account because I didn't know what was going on.

**Lawrence Neves:** But for this, yeah, I think it's important that in this info here that you pick out one of these.

**Lawrence Neves:** Because what happens is because it's so templated, it will pick whatever it thinks is the right one and you're going to come up with the wrong article.

**Lawrence Neves:** If you don't pick listicle when it's a listicle, it'll give you a how-to article.

**Lawrence Neves:** And I noticed that that's the one thing that probably holds me up the most.

**Lawrence Neves:** I don't pick personas for this because it's basically all the same audience.

**Lawrence Neves:** It's people looking for, I believe their main persona are people looking for short-term solutions or solutions to integrate software tools.

**Lawrence Neves:** So I'd never pick that.

**Lawrence Neves:** I don't pick the topic either because it's usually, you can do this, but it takes it from the keyword anyway.

**Lawrence Neves:** And the keywords are pretty easy.

**Lawrence Neves:** And then secondary keywords, it comes up with that on its own.

**Lawrence Neves:** The weird thing is when you get to the draft article stage, I was going into the convergence reports and seeing like what things like, you know, it tells you, here's some recommended fixes and this, right?

**Lawrence Neves:** And then I was in a meeting yesterday with the managing editor group and they were like, this is just, these are just suggestions.

**Lawrence Neves:** Like going in and changing the writing guidelines to match this, it will always find something wrong with what you do.

**Lawrence Neves:** So my only concern here is if I get down to the convergence scores and the writing score, like that's low for a writing score, but if I made all of these convergence changes in the post-processing, then that writing score, of course, will be much better than that.

**Lawrence Neves:** So I leave this mostly to the post-processing now.

**Lawrence Neves:** I was going in and what happened is, like it says, this is what it says in the, where is this?

**Lawrence Neves:** This is in writing guidelines, right?

**Lawrence Neves:** Yes, so in the writing guidelines, this is what it says.

**Lawrence Neves:** This is

**Lawrence Neves:** Convergence report says this is what it should say, and I was doing that for a little bit, not for SIPA, and what happened was the writing guidelines were filled with things that didn't make, there was no reason to put that much into the writing guidelines.

**Lawrence Neves:** And these are going to be specific article to article anyway.

**Lawrence Neves:** So Matt Panzarino told the ME group yesterday, the writing, the convergence reports are only there to show you where things are going wrong if you want to correct them, but they don't have to be corrected on the fly.

**Lawrence Neves:** Because I did this with an article, I changed eight things in the writing guidelines, I re-ran the article again, I checked the convergence report, and there were four more things that still hadn't, that had to be put in, and I thought it would go on and on and on.

**Patrícia Contreiras:** So if you question the AI, it's in a cloud, GPT is going to say, okay, let me check that again.

**Patrícia Contreiras:** Oh, I found this.

**Patrícia Contreiras:** I told you that.

**Patrícia Contreiras:** I told you AI, and it's IT.

**Patrícia Contreiras:** So we really need to trust our judgment here.

**Patrícia Contreiras:** Right, right, right.

**Patrícia Contreiras:** It's like trust, it's like trusting your kids to pick out dinner.

**Lawrence Neves:** They're never.

**Lawrence Neves:** They're going to pick the thing you want, and they're always going to have different choices.

**Lawrence Neves:** Nobody's ever going to agree on anything.

**Lawrence Neves:** Do you have any other questions about the blog things?

**Patrícia Contreiras:** No, I think so far it's very similar to Tavern.

**Patrícia Contreiras:** I'm giving it a go.

**Patrícia Contreiras:** I'm going to see how it turns out.

**Patrícia Contreiras:** And if anything else, I'm going to pester you as I told you.

**Patrícia Contreiras:** Absolutely.

**Lawrence Neves:** And if you want me to look at articles before you send them out to me, just to give them a brief look.

**Lawrence Neves:** I'll absolutely do that for you.

**Lawrence Neves:** Matt makes changes.

**Lawrence Neves:** He was editing a lot of the See It stuff himself, and I'm reading the changes that he made.

**Lawrence Neves:** And they're all smart stuff.

**Lawrence Neves:** I get where he was coming at with that.

**Lawrence Neves:** But it was really hard for me to keep track of all the changes at one time.

**Lawrence Neves:** So now he's saying, now that I'm coming off of a seat, he's saying, oh, you're much closer to what we need it to be.

**Lawrence Neves:** So I would look at the last slide in here and just see where you're at.

**Patrícia Contreiras:** That's when I was...

**Patrícia Contreiras:** was...

**Patrícia Contreiras:** Just getting the pipeline for Homebase, which was the other client that just ended the contract with us, it was basically all done.

**Patrícia Contreiras:** It would take me like five minutes and no, it's done.

**Patrícia Contreiras:** We don't have a contract anymore.

**Patrícia Contreiras:** Yeah, I feel like that's going to happen a lot around here.

**Patrícia Contreiras:** Yeah, it's going to happen.

**Patrícia Contreiras:** We're here basically to fix the pipelines and get them working and make the clients happy with it and move on to somewhere else.

**Patrícia Contreiras:** Great.

**Lawrence Neves:** There's a thing in here called guides.

**Lawrence Neves:** I have to be honest with you, I've never used this.

**Lawrence Neves:** I've never been asked to create a guide, so I don't know what that is.

**Lawrence Neves:** I don't even have it in the Seat Notion doc because I've never used this.

**Lawrence Neves:** So you may want to ask Matt what that is and if we ever do it.

**Lawrence Neves:** may be something we don't do anymore.

**Lawrence Neves:** I'm not sure, but I've never been asked to do You told me about the blogs and the tool space.

**Patrícia Contreiras:** The blogs and the tool space.

**Lawrence Neves:** Okay, great.

**Lawrence Neves:** The other great thing about Seat are these tool pages.

**Lawrence Neves:** So if you go into your content.

**Lawrence Neves:** I'm sorry, let me share this again.

**Lawrence Neves:** So in the content thing, the blogs will be here, they'll be in production, that's what you're going to be working on.

**Lawrence Neves:** You click on tool pages, and he usually selects 10 tool pages.

**Lawrence Neves:** Tool pages are endless.

**Lawrence Neves:** I think there's thousands or hundreds of them, and he usually puts 10 per week.

**Lawrence Neves:** I used to freak out and think, God, that's a lot of writing.

**Lawrence Neves:** But when you see how this is done, it's a lot easier than we think.

**Lawrence Neves:** I'm going to take a couple of ones we've already done, because there's different types of tool pages.

**Lawrence Neves:** That's the other thing, too, is that the tool pages, these are all alternates.

**Lawrence Neves:** You'll usually see alternates, comparisons, and overviews.

**Lawrence Neves:** Those are the three types, the main three types of tool pages.

**Lawrence Neves:** So for Zapier alternatives, what we're going to do is this.

**Lawrence Neves:** Let me go back.

**Lawrence Neves:** So...

**Lawrence Neves:** The pipeline.

**Lawrence Neves:** Okay.

**Lawrence Neves:** So let's start with alternatives.

**Lawrence Neves:** That's tool alternatives.

**Lawrence Neves:** Basically what these articles are is they're just, they show you, they do give you a brief overview of what a tool is, and then they give you what other alternatives there might be for that.

**Lawrence Neves:** I'm going to just create one here.

**Lawrence Neves:** Show you how easy this is.

**Lawrence Neves:** You hit add.

**Lawrence Neves:** The topic is Zapier.

**Lawrence Neves:** And that's it.

**Lawrence Neves:** Then you hit create.

**Lawrence Neves:** And that's that.

**Lawrence Neves:** And the only thing to do after this is editing.

**Lawrence Neves:** Because what you're going to see is I'm going to run this just so we can see.

**Lawrence Neves:** I'm going to run this and then I'll delete it afterwards.

**Lawrence Neves:** But it's going to go through this whole process.

**Lawrence Neves:** And when you get to the output, it's probably going to be very close to what you're going to need.

**Lawrence Neves:** After that, it's basically just making sure it looks like the other alternate pages.

**Lawrence Neves:** You got to make sure that if Seat is.

**Lawrence Neves:** So if Seat is a, if they are a competitor to Seat, you just have to be aware of that.

**Lawrence Neves:** Oh, and then the other thing that this thing will do a lot, I may have changed it already because I just edited these.

**Lawrence Neves:** But another thing this thing does a lot is, so top alternates to Jira.

**Lawrence Neves:** There's Linear, there's ClickUp, there's Asana, there's Monday.

**Lawrence Neves:** Okay, so you go through here.

**Lawrence Neves:** So Linear.

**Lawrence Neves:** How Linear works with Seat?

**Lawrence Neves:** Well, they're lucky on this one because Linear does work with Seat.

**Lawrence Neves:** But you are many times going to find how it's not integrated with it.

**Lawrence Neves:** What I do, instead of asking, ask AI to remove it, I just go in and remove it and then save the article.

**Lawrence Neves:** So because if you, let's just say this, this does work with Seat, but Seat did.

**Lawrence Neves:** If I just take this and delete it, that's all you need to do.

**Lawrence Neves:** That's all that ask AI needs to do.

**Lawrence Neves:** When I, I noticed that when I ask AI to do it, it takes forever for them to do it.

**Lawrence Neves:** When I could just go in there and cut it out myself.

**Lawrence Neves:** Then, as...

**Lawrence Neves:** As far as these articles go, you just want to make sure, so this will say normally how SEAT supports these tools.

**Lawrence Neves:** You just want to make sure you put the subject of what those tools are, and then you'll see down here that they're talking about project management alternatives, and you're fine.

**Lawrence Neves:** You may want to give these a quick read, but I'm telling you, Patricia, this stuff is written, I don't understand this pipeline, how it's written so well that it almost never makes mistakes in what they say.

**Lawrence Neves:** The only thing is that it completely fabricates whether something integrates with SEAT or not.

**Lawrence Neves:** Now, I've heard from Matt that he's working with Kirkland to try to get that fixed.

**Lawrence Neves:** It used to be that it never did that, but as SEAT starts to add more, I guess it's harder to update what SEAT works with and what doesn't, and a lot of times the Atlas will just hallucinate and say, oh yeah, it works with SEAT.

**Lawrence Neves:** And it's funny to read too, because sometimes if you read how SEAT works with it, you think, oh, that's great that SEAT does that.

**Lawrence Neves:** And so you realize, wait a minute, that doesn't do that at all, and you realize.

**Lawrence Neves:** I oh, the AI just made up that it works.

**Patrícia Contreiras:** One time I wrote an entire article for Fathom, or it was a listicle or something.

**Patrícia Contreiras:** And I said, yeah, it integrates well with this and that.

**Patrícia Contreiras:** And Matt was like, I don't think so.

**Patrícia Contreiras:** I'm going to check with them.

**Patrícia Contreiras:** The first time that happened to me was...

**Patrícia Contreiras:** got a feedback, and we don't know.

**Patrícia Contreiras:** The first time that happened with me was with Seat.

**Lawrence Neves:** Matt got an article, and he said, okay, this is great, except it doesn't integrate with this.

**Lawrence Neves:** And I thought, oh.

**Lawrence Neves:** And I told him, I said, oh, the AI lied?

**Lawrence Neves:** And he said, yeah, the AI will lie.

**Lawrence Neves:** You just have to be careful.

**Patrícia Contreiras:** The AI doesn't lie.

**Lawrence Neves:** So mostly with that, it's just editing after that and making sure.

**Lawrence Neves:** Let me just go back to this real quick.

**Lawrence Neves:** This thing usually moves way faster than this.

**Lawrence Neves:** I put 10 at a time in here, and it goes through all 10 in like less than an hour.

**Lawrence Neves:** That's the alternative, but we'll come back to that.

**Lawrence Neves:** The tool comparison with agentic research.

**Patrícia Contreiras:** So basically for the post-processing for the alternative client, is just for...

**Patrícia Contreiras:** Betting, cutting out eventual incorrect flies that the AI comes up with, and that's it.

**Patrícia Contreiras:** And that's it.

**Lawrence Neves:** And then you always tell it, use the following articles as comparisons.

**Patrícia Contreiras:** Comparisons, right.

**Patrícia Contreiras:** And then you should take the last three.

**Lawrence Neves:** Again, so sometimes it'll say how these tools compare, and then other articles would say these tools compare by because nobody ever took care of that.

**Lawrence Neves:** So we want to make sure that we're doing that.

**Lawrence Neves:** Where's tool comparisons?

**Lawrence Neves:** Why isn't there anything in here?

**Patrícia Contreiras:** And when it comes to word count, is it okay?

**Patrícia Contreiras:** Because Tavern does what it wants.

**Patrícia Contreiras:** Yeah.

**Lawrence Neves:** So I've never had to worry about word count because it's never gone over.

**Lawrence Neves:** So as long as it doesn't go over, I should be fine with that.

**Lawrence Neves:** Why is this tool comparison not working?

**Lawrence Neves:** Tool comparison.

**Lawrence Neves:** Oh.

**Lawrence Neves:** So I'm using the wrong one, I think.

**Lawrence Neves:** Oh, that might be new.

**Lawrence Neves:** I've never seen that tool comparison with agentic research.

**Lawrence Neves:** I mean, you could try that if you want.

**Patrícia Contreiras:** I can run on both the same.

**Lawrence Neves:** Yeah, because I've always just used tool comparison.

**Lawrence Neves:** So tool comparison, again, ridiculous.

**Lawrence Neves:** You'll get, let me just share again.

**Patrícia Contreiras:** But for word count, again, is it just the same as a normal blog?

**Lawrence Neves:** Yeah, usually says, I think it says in the directions, in the input directions, it says 1,500 words, and it usually never goes over that.

**Lawrence Neves:** And then when you do the post-processing, it's in there too as well to keep it to 1,500 to 2,000 words.

**Lawrence Neves:** And I never get anything back that says you went over the word count.

**Lawrence Neves:** So in this, again, in this, we're going to go to stuff that we've already published.

**Lawrence Neves:** we're all Eric embossed.

**Lawrence Neves:** And

**Lawrence Neves:** These are tools, comparison page.

**Lawrence Neves:** So you'll see that it's pager duty versus incident I.O., incident I.O.

**Lawrence Neves:** versus rootly.

**Lawrence Neves:** All you need to do then is you go into this.

**Lawrence Neves:** You go into this.

**Lawrence Neves:** You hit add.

**Lawrence Neves:** Okay.

**Lawrence Neves:** That always remains the same.

**Lawrence Neves:** Tool one is incident I.O.

**Lawrence Neves:** And tool two was, I forgot what it was already.

**Lawrence Neves:** Oh, that's pager duty.

**Lawrence Neves:** Let's just use that as an example.

**Lawrence Neves:** And then you hit create.

**Lawrence Neves:** And again, does all the work by itself.

**Lawrence Neves:** You don't do anything until post-processing with this.

**Lawrence Neves:** I would go, I always go in.

**Lawrence Neves:** This is another one.

**Lawrence Neves:** Where you want to go in and make sure that it has the table that it shows.

**Lawrence Neves:** These comparison tables will always be the same.

**Lawrence Neves:** They usually give an overview of both things.

**Lawrence Neves:** You may want to check links in there.

**Lawrence Neves:** Again, anytime there is a link to something, anytime that the tool integrates or they mention any other tool that integrates with SEAT, you want to put that from the integration page.

**Lawrence Neves:** You want to put the link to that in there.

**Lawrence Neves:** It gives you an overview of both things, a side-by-side feature comparison, when to choose one over the other.

**Lawrence Neves:** Again, this is all there.

**Lawrence Neves:** And then how SEAT integrates with both tools.

**Lawrence Neves:** So this is probably – let me just – I'm just going to go offline for just a second and check something.

**Lawrence Neves:** Mm-hmm.

**Lawrence Neves:** Uh-hmm.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Okay.

**Lawrence Neves:** It doesn't integrate with either one of those.

**Lawrence Neves:** Why is that in there?

**Lawrence Neves:** Let me see something else.

**Lawrence Neves:** Alternatives.

**Lawrence Neves:** Comparisons.

**Lawrence Neves:** Oh, here goes a good one.

**Lawrence Neves:** I'm just trying to find one where I know that doesn't integrate.

**Patrícia Contreiras:** Hmm.

**Lawrence Neves:** That's interesting.

**Lawrence Neves:** Matt left those in there, how SEAT integrates with both tools, but it doesn't integrate with either tool.

**Lawrence Neves:** I wonder if this is just a generic.

**Lawrence Neves:** I wonder

**Lawrence Neves:** There's no evidence.

**Lawrence Neves:** See, says, though there is no evidence, it integrates luckily with IncidentIO or Brutely.

**Lawrence Neves:** So if that's the case, why would we even include this?

**Patrícia Contreiras:** It's very strange.

**Lawrence Neves:** Oh, no.

**Lawrence Neves:** So what it's doing is it's telling you, even though it doesn't integrate with it, if you wanted to do it, so for organizations that use this, you can automatically create follow-up workflows.

**Lawrence Neves:** So it's basically saying Seek can help you with that, but it doesn't help you with it right now.

**Patrícia Contreiras:** Here's the alternative.

**Patrícia Contreiras:** Right.

**Patrícia Contreiras:** Exactly.

**Lawrence Neves:** Exactly.

**Lawrence Neves:** And that's tool comparison.

**Lawrence Neves:** And again, that's mostly post-processing and running through that.

**Lawrence Neves:** And then the last one is the tool alternatives.

**Lawrence Neves:** So this one.

**Lawrence Neves:** Yeah, this is the one I had trouble with.

**Lawrence Neves:** No.

**Lawrence Neves:** with.

**Lawrence Neves:** no, no,

**Lawrence Neves:** No, wait, there's one.

**Patrícia Contreiras:** I think the one that's missing is the overview.

**Lawrence Neves:** Tool overview with images.

**Lawrence Neves:** Thank you.

**Lawrence Neves:** Yes, this was...

**Lawrence Neves:** Just for this one, because I noticed the blog doesn't have one.

**Patrícia Contreiras:** The blog doesn't have what?

**Patrícia Contreiras:** Images.

**Patrícia Contreiras:** Yes, no, yeah, no.

**Lawrence Neves:** But images will be created.

**Lawrence Neves:** Let me show you, because this was a weird thing I found, too, because it says that there's no images, but...

**Lawrence Neves:** There's a step there, creating images.

**Patrícia Contreiras:** right, right.

**Lawrence Neves:** So...

**Lawrence Neves:** No, this isn't it.

**Lawrence Neves:** There's another one here, too.

**Lawrence Neves:** Let me show you.

**Lawrence Neves:** Thank

**Lawrence Neves:** Where it compares, is it, let's see.

**Lawrence Neves:** Oh, this isn't it either.

**Patrícia Contreiras:** Yes, this is it.

**Patrícia Contreiras:** Okay.

**Patrícia Contreiras:** Let me just share this with you real quick.

**Lawrence Neves:** I don't, I've never seen where this is created in the actual pipeline.

**Lawrence Neves:** But I know that they do do this.

**Lawrence Neves:** So, for the alternatives pages, so you see this here, this JIRA logo, and this table that they create, that's all created by the template.

**Lawrence Neves:** Like, I don't, we don't create that.

**Lawrence Neves:** But this is what was throwing me off for the longest time.

**Lawrence Neves:** And again, this is all, this all follows pretty much the same thing.

**Lawrence Neves:** What?

**Lawrence Neves:** What?

**Lawrence Neves:** It threw me off for a long time was when we get into overview with images, this is the only added step, but I'm pretty sure this is in the Notion doc.

**Lawrence Neves:** I just added this.

**Lawrence Neves:** So let's say we're going to do a new one.

**Lawrence Neves:** We're going to do, I'm going to add, so we said rippling, right?

**Lawrence Neves:** Now, this is the only one where you have to add the domain for rippling because that's how it creates the image.

**Lawrence Neves:** I was literally tearing my hair out because I was going to...

**Patrícia Contreiras:** Because doesn't explain everything, right?

**Lawrence Neves:** And I couldn't understand why it was getting stuck at branding.

**Lawrence Neves:** I'll show you where on the pipeline.

**Lawrence Neves:** Let me just put this in here real quick.

**Lawrence Neves:** Okay, so I go to the domain, I put the domain in there, and I'll hit create.

**Lawrence Neves:** What happened was I wasn't putting the domain in there, and I didn't understand.

**Lawrence Neves:** This would stop at brand search.

**Lawrence Neves:** Like it would go red and then I couldn't advance in any farther than that.

**Lawrence Neves:** And I didn't find out until after literally maybe a week of battling with it that it can't do the brand search unless it has the logo for the brand.

**Lawrence Neves:** And that's why you have to put that in.

**Lawrence Neves:** So I just found that out is that you have to make sure that when you're doing tool overview with images that you put the domain in there and then just who it is.

**Lawrence Neves:** And again, this is another one.

**Lawrence Neves:** You put it in, you hit create, and then you just wait for the magic to happen and then you go check that at the end.

**Lawrence Neves:** I'll go to Jenkins real quick and just make sure.

**Lawrence Neves:** So there's the overview.

**Lawrence Neves:** What is Jenkins?

**Lawrence Neves:** What is Jenkins used for?

**Lawrence Neves:** Key features, pros and cons.

**Lawrence Neves:** These are all pretty standard.

**Lawrence Neves:** The pricing is pretty standard.

**Lawrence Neves:** The pricing And then when, so this is what happens if, if they are a competitor to see it or.

**Lawrence Neves:** Or they, not just a competitor, if they are a competitor or they don't integrate with SEAT, there's a section called when the tool isn't enough, meet SEAT.

**Lawrence Neves:** This is a standardized thing, and basically it's just generic wording in here, and then it just gives you a list of things that SEAT can do.

**Lawrence Neves:** For Jenkins alternatives, I have never put SEAT first in these because, well, I know that Jenkins is not a, Jenkins is not, it's a CICD automation.

**Lawrence Neves:** It's not an ITSM.

**Lawrence Neves:** If it's an ITSM, you want to make sure that for the alternatives, for the Jenkins alternatives that, or for whatever tools alternatives, that SEAT is listed first.

**Lawrence Neves:** You just tell it, oh, SEAT is, this is a competitor to SEAT, and please list SEAT first as the first alternative.

**Lawrence Neves:** And then that's that.

**Lawrence Neves:** Even the FAQs are done really well, and I never really have to do anything else with that.

**Lawrence Neves:** And that's the reason that he has it assigned as 10 at a time, because these literally...

**Lawrence Neves:** Literally, you put them in, you let them run, and it takes you maybe, again, depending on your workflow and how you do things, it usually takes you about 10 minutes per to get through them.

**Lawrence Neves:** And then once they're done, we've got these to the point where he doesn't even look at them anymore.

**Lawrence Neves:** He just tells you to send them on because they're all going to look the same.

**Lawrence Neves:** And again, when you do the post-processing, say, make sure this looks like all the other similar links, and then you put in the links for that, and it'll just make sure that everything like Jenkins Alternatives and all that are named correctly and that everything appears in the same place.

**Lawrence Neves:** The weird thing about these pipelines is if you don't check it, I don't know why this is, but if you don't check it, that's when it makes mistakes.

**Lawrence Neves:** It's like it knows you're not going to check it.

**Patrícia Contreiras:** Exactly.

**Lawrence Neves:** It knows you're not going to check it and says, you know what, I'm going to get one over on you.

**Lawrence Neves:** So it's always real good.

**Lawrence Neves:** You don't want to spend a lot of time on it, though, because Matt told me once, and it's actually true, you don't really need to read through a lot of this.

**Lawrence Neves:** I would just double check.

**Lawrence Neves:** Check links and double check any numbers, any stats that are written.

**Lawrence Neves:** But like this key features of Jenkins, that's all taken from the research.

**Patrícia Contreiras:** That has nothing.

**Lawrence Neves:** I wouldn't even know if this is wrong, you know, unless I checked it.

**Lawrence Neves:** And I don't have the time to check every one of these every time we put these through.

**Lawrence Neves:** Yeah, a lot of tools.

**Patrícia Contreiras:** It's impossible checking all of them every time.

**Patrícia Contreiras:** Right.

**Lawrence Neves:** But you do, again, you know, when you give it a quick glance, you just want to make sure they're not saying anything stupid.

**Lawrence Neves:** But like, you know, great for great for dancing.

**Lawrence Neves:** OK, I know that's a lie.

**Lawrence Neves:** got to go in there and check that.

**Lawrence Neves:** But you'll rarely find that.

**Lawrence Neves:** I think I found that maybe once or twice.

**Lawrence Neves:** But again, it's the times I don't check it that I that it decides that that's what it's going to do.

**Lawrence Neves:** So, yeah, he'll usually assign 10 of those a week.

**Lawrence Neves:** And again, once you get them down, they're they're they're like nothing.

**Lawrence Neves:** You do them, you set them aside and then we send them off every week.

**Lawrence Neves:** They don't I don't even know if seat checks them.

**Lawrence Neves:** Actually, I would not want to be caught.

**Lawrence Neves:** I'm not doing it wrong, I'm but.

**Lawrence Neves:** I don't, I believe Matt just sends them along.

**Lawrence Neves:** The blogs are more important to him because the blogs, we want to standardize how we're doing the blogs and make sure the blogs kind of follow the same curriculum all the time.

**Lawrence Neves:** But even that, once you get that down, it's going to be easy.

**Lawrence Neves:** It's going to be nothing.

**Lawrence Neves:** It's really going to be nothing to do.

**Lawrence Neves:** I'll stop that.

**Lawrence Neves:** I'm going to get rid of that.

**Lawrence Neves:** Okay.

**Lawrence Neves:** Do you have any questions?

**Patrícia Contreiras:** No, I think you'll answer everything.

**Patrícia Contreiras:** As I said, I think it's very close to Tavern, at least the blog ones.

**Patrícia Contreiras:** And I already had a meeting with Matt earlier, and he explained it to me that we are going to try and focus more on SEO, which is what I've been doing for Tavern.

**Patrícia Contreiras:** So we're going to do a few changes on that.

**Patrícia Contreiras:** But other than that, I really don't think there is anything else to change.

**Patrícia Contreiras:** Maybe tweak the pipeline just for making it more friendly.

**Patrícia Contreiras:** But other than that, it really looks.

**Patrícia Contreiras:** Okay.

**Patrícia Contreiras:** And really easy to do.

**Patrícia Contreiras:** Okay.

**Patrícia Contreiras:** If you have any questions, contact me.

**Lawrence Neves:** I will let you know anything.

**Patrícia Contreiras:** Like I said, I'm pretty new in this one.

**Lawrence Neves:** So I don't know if I can answer a lot of things in depth.

**Lawrence Neves:** I do like that they're actually going for more SEO in that because there was no SEO to this.

**Lawrence Neves:** I mean, we never researched these articles.

**Lawrence Neves:** We just put them up and basically made them look like each other.

**Lawrence Neves:** But now I think they want a little bit more than that.

**Lawrence Neves:** So that's great.

**Lawrence Neves:** Yeah.

**Patrícia Contreiras:** It's more for structure and the SEO thing because they are ranking well.

**Patrícia Contreiras:** So they want to make sure that keeps happening.

**Lawrence Neves:** Right.

**Lawrence Neves:** Right.

**Lawrence Neves:** Right.

**Patrícia Contreiras:** Thank you very much for your time.

**Patrícia Contreiras:** No, not at all.

**Lawrence Neves:** I'm so very happy to help you.

**Lawrence Neves:** But again, you have any questions, look over the Notion doc.

**Lawrence Neves:** And if there's any questions about the Notion doc, let me know.

**Lawrence Neves:** Because again, I filled out that Notion doc basically just by what I knew.

**Lawrence Neves:** And I don't know if things changed in that or if Matt had other ideas about that.

**Lawrence Neves:** I mean, he's seen the Notion doc.

**Lawrence Neves:** If he had any ideas, he would have told me by now.

**Lawrence Neves:** But yeah.

**Lawrence Neves:** And then in

**Patrícia Contreiras:** Tons of information to fill in, right?

**Patrícia Contreiras:** I was like, I'm so tired.

**Patrícia Contreiras:** I was like, I can't.

**Patrícia Contreiras:** I don't understand what this means anymore.

**Patrícia Contreiras:** And I just dropped it the last time and I've finalized it the next day.

**Patrícia Contreiras:** But thank you.

**Patrícia Contreiras:** I will do that.

**Patrícia Contreiras:** Okay.

**Lawrence Neves:** And like I said, if you have any other questions, let me know.

**Lawrence Neves:** Absolutely.

**Lawrence Neves:** Thank you.

**Lawrence Neves:** Have a great day.
