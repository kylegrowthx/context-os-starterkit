# Rimkus <> GrowthX | CMS & Publishing Walkthrough

<metadata>
date: 2025-09-25
time: 20:00 UTC
duration: 36 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien (GrowthX), Jennifer Bulmash (Rimkus), Alishia Natiello (Rimkus)
fathom_recording_id: 89955905
fathom_url: https://fathom.video/calls/421160644
share_url: https://fathom.video/share/BZMMXCsUwAkgmmySMN24pstEuxFCS3gd
source: fathom
enriched_on: 2026-03-03 03:14 UTC
</metadata>

---

## Summary

Alishia walked the GrowthX team through Rimkus' WordPress CMS and publishing workflow, covering content structure (articles vs. blog posts), WordPress blocks-based formatting, SEO metadata handling (title, description, URL slug), and image selection responsibilities. The team agreed on a gradual ramp-up: GrowthX drafts content with full SEO metadata, starting with one calibration piece per week, then moving to three and five weekly, while Rimkus initially reviews and publishes. Erik will report back on image generation options; once trust is established and both teams are confident in the workflow, GrowthX can publish directly. The team also confirmed reporting capabilities to track both GrowthX-produced content and Rimkus' organic content separately by topic cluster.

---

## Context

Rimkus is an engineering and construction consulting firm that GrowthX recently contracted to produce content for their website and blog. This call kicked off the execution phase of a multi-week strategy sprint where GrowthX will write articles and blog posts focused on four key service clusters (identified the day before), while Rimkus handles publishing, review, and refinement. Jennifer Bulmash and Alishia Natiello lead Rimkus' content operations; they're transitioning from a heavily centralized review process (that previously involved board-level approval) to a more streamlined approach with GrowthX. The CMS walkthrough was necessary because GrowthX would be granted direct WordPress access and the team needed to align on submission format, metadata requirements, and the phased rollout schedule.

---

## Relevance

**To GrowthX Delivery:**
- Rimkus workflow aligns with GrowthX's content production model: GrowthX authors + submits with full SEO metadata (title, description, URL slug), Rimkus reviews and publishes.
- CMS uses WordPress blocks (no strict templates), allowing flexibility similar to GrowthX's approach to article formatting.
- Phased rollout (1 calibration → 3 → 5 per week) provides clear testing and feedback cycles, reducing deployment risk.
- Image selection responsibility split: Rimkus holds images initially for domains requiring review (e.g., Life Sciences), but GrowthX can provide or generate later.

**To GrowthX Business Development:**
- Rimkus' new operating structure (reduced review layers, no board approval required) signals streamlined decision-making and faster content velocity post-strategy sprint.
- Performance reporting via Looker dashboard will track GrowthX content lift by topic cluster, providing measurable ROI evidence for Rimkus and replicable reporting for other accounts.
- Distinct tracking of GrowthX-produced vs. Rimkus-organic content enables comparative analysis to demonstrate content quality impact.
- Account shows healthy initial trust trajectory: direct WordPress publish access possible within 8-week sprint if content quality holds.

---

## Overview

- GrowthX will draft content in WordPress, with Rimkus team initially reviewing and publishing
- Gradual ramp-up: 1 calibration blog, then 3, then 5 per week
- Rimkus to handle image selection; potential for GrowthX to assist later
- GrowthX will provide full SEO metadata (title, description, URL slug)
- GrowthX to track performance of both their content and Rimkus' organic content

---

## Key Topics

### CMS Access and Publishing Process

  - GrowthX team granted WordPress access via <team@growthxlabs.com>
  - Content types: articles (rimkus.com/article/title) and blog posts (rimkus.com/blog/title)
  - WordPress blocks used for formatting; no strict templates, but guidelines exist
  - GrowthX to draft content, Rimkus to review and publish initially
  - Potential for GrowthX to publish directly after trust is established

### Content Creation and Formatting

  - GrowthX to handle article writing, SEO metadata, and formatting
  - Rimkus to manage image selection initially (using Shutterstock)
  - Potential for GrowthX to assist with image generation in later stages
  - Consideration needed for specific image requirements (e.g., Life Sciences content)

### Performance Tracking and Reporting

  - GrowthX to track performance of both their content and Rimkus' organic content
  - Reporting capabilities to show lift by individual pieces and topic clusters
  - GrowthX to provide a Looker dashboard for analytics in coming weeks
  - Ability to distinguish between GrowthX-produced and Rimkus organic content

### Review Process and Workflow

  - Rimkus transitioning from heavy review process to more streamlined approach
  - Jennifer and Alishia to refine internal review process
  - Gradual implementation of new workflow during 8-week strategy sprint

---

## Action Items

**Alishia Natiello (Rimkus)**
- Check with Vitaly re GrowthX publishing permissions; confirm he's okay with gradual ramp-up process (1 → 3 → 5 articles/week)

**Erik O'Brien (GrowthX)**
- Report back to team re image selection/generation options; discuss with Rimkus on feasibility and timeline for scaled image generation
- Confirm with Ada re reporting capabilities for non-GrowthX content; relay findings to Rimkus team so they understand analytics scope

**Jennifer Bulmash (Rimkus)**
- Finalize internal content review process with Alishia; streamline workflow to remove unnecessary approval layers for GrowthX collaboration

---

## Transcript
**Jennifer Bulmash:** I think we're just waiting on Alicia, but she also had like a soccer injury yesterday.

**Jennifer Bulmash:** She tore some kind of muscle.

**Jennifer Bulmash:** So I think there's a small chance she might not be here, but oh, nope, she's pinging me.

**Erik O'Brien:** I think she might be here.

**Erik O'Brien:** Okay.

**Erik O'Brien:** I saw she got us access earlier.

**Jennifer Bulmash:** Awesome.

**Jennifer Bulmash:** She also, Nora said that you should now have Google Analytics access as well.

**Jennifer Bulmash:** She just didn't follow up in the chat.

**Jennifer Bulmash:** So I can follow up if y'all need anything.

**Jennifer Bulmash:** But she said she granted access.

**Jennifer Bulmash:** then Alicia actually should be the person to get you the console access.

**Jennifer Bulmash:** so I think she's doing that sooner than later.

**Jennifer Bulmash:** Let me confirm with her.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Looks like we've got analytics access.

**Jennifer Bulmash:** Cool.

**Jennifer Bulmash:** Oh.

**Jennifer Bulmash:** She said, yeah, she's, poor thing, moving slowly.

**Jennifer Bulmash:** But she will be here.

**Jennifer Bulmash:** Okay.

**Jennifer Bulmash:** I also have been meeting with several people this week to get more details about client personas and all sorts of info.

**Jennifer Bulmash:** So I'll have, I think, thank you, by the way, for being flexible, moving Tuesday's call to tomorrow.

**Jennifer Bulmash:** But I'll try to have everything uploaded for you ahead of that in case it's helpful context for while we're speaking about all the forensics things.

**Jennifer Bulmash:** And the forensics call, I mean, we could have like a lot to cover and it wouldn't cover everything.

**Jennifer Bulmash:** that one will just, I think, be you and me, unless there's someone else from the growthx side.

**Jennifer Bulmash:** So feel free, you know, to rein me in, as you can tell now, I'm chatty.

**Erik O'Brien:** So yeah, it works at all.

**Jennifer Bulmash:** Okay, I appreciate that.

**Erik O'Brien:** Yeah, more context, the better, especially for that one that we know is very broad.

**Jennifer Bulmash:** Yeah, exactly.

**Jennifer Bulmash:** Hi, Alisha.

**Jennifer Bulmash:** Thanks for joining.

**Jennifer Bulmash:** I already told Erik about your sad injuries.

**Alishia Natiello:** Okay, I was, I was figuring you would.

**Alishia Natiello:** I'm getting used to taking a little more time hobbling around post-lunch to get back set up.

**Alishia Natiello:** I've got to keep my leg elevated here.

**Alishia Natiello:** So I'm like delicately balancing while on the couch and all these things.

**Alishia Natiello:** So, yeah, yeah, but diagnosis is successful.

**Alishia Natiello:** Eight weeks until the full recovery, so I'm glad it's hopefully not going to be much longer.

**Alishia Natiello:** But yeah.

**Erik O'Brien:** All things considered, not too bad.

**Alishia Natiello:** Yep, yep.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** I know I booked 45 minutes for this.

**Erik O'Brien:** I don't think we'll need all that much time.

**Alishia Natiello:** Okay.

**Erik O'Brien:** So yeah, typically what we do here is just have you run us through kind of the typical publishing process through WordPress, just so our team makes sure we don't have anything that we miss as we kind of get up and running with publishing in the next couple weeks.

**Erik O'Brien:** So yeah, it's mainly for us just to get a view on how you guys do it and gives me the chance to ask any questions to clarify any points that we might run into.

**Alishia Natiello:** Okay.

**Alishia Natiello:** Yeah, do you mind if I wasn't able to attend the call yesterday as I was out? So I'm not sure what all was discussed in terms of how it works and what you guys need CMS access for and whatnot.

**Alishia Natiello:** Is that like you're going to go over that or if I could get like a brief synopsis before I walk through our process, that would be helpful.

**Erik O'Brien:** Yeah, so for the most part, it'll be us.

**Erik O'Brien:** After we create the articles or blog posts, we will set those up in WordPress and then be able to publish on your guys' behalf.

**Erik O'Brien:** So that once we get to a little bit higher velocity of, you know, five per week, we're not kind of holding the bottleneck or kind of waiting for you guys to publish everything.

**Erik O'Brien:** So I think for us, it's just another way for us to kind of take some of the load off for you guys once we get to publishing.

**Jennifer Bulmash:** Alisha, just so you know, sorry to interrupt you, We do have the option if you'd prefer, they said they could always set it up in the CMS and then just basically get it ready to go for you'd be the one to hit publish.

**Jennifer Bulmash:** So it really is up to you, but to kind of speak to what he just said, if it's, you know, a high volume amount of content, and you obviously have a full-time job, otherwise, if it gets to a certain point where it's like, no, there's that trust there, or we understand that the content has all been reviewed, and it's just, you know, in the CMS, we're waiting for the publishing point, I said I have no problem giving them permission to do that.

**Jennifer Bulmash:** But we'll just kind of, I feel like, navigate the process and get that familiarity and that trust built.

**Alishia Natiello:** Yeah, we'll start with my next, yeah, kind of question.

**Alishia Natiello:** Yeah, and Jen, I don't know if Vitaly joined or not, or if he's aware of this process. I just want to run it by him to make sure he's good. I think if he says it's good, I just want to have enough testing time to make sure we get a few different post types up and it's looking good with the whole review process as well. And then, like I said, I'll just check in with Vitaly to make sure he's okay with that. But that's perfect. He will probably just be like, "go for it."

**Erik O'Brien:** We'll, we'll make sure like we start off with one calibration blog and I think we'll get into that next week.

**Erik O'Brien:** So we'll have you guys fully review, give feedback, update and edit the article.

**Erik O'Brien:** So before we ever move to like staging and WordPress, it'll be, have to be approved by you guys.

**Erik O'Brien:** And so we'll start with one and then the week after we try to get to three and then we get to five after that.

**Erik O'Brien:** So it's definitely a gradual ramp up and make sure you guys have plenty of time to give feedback and do, do all the edits and everything.

**Jennifer Bulmash:** Okay.

**Alishia Natiello:** And when you say staging, do you want access to our staging environment as well, or do you mean just drafting in the prod environment before it publishes?

**Erik O'Brien:** Yeah, drafting in the prod environment is kind of where we sit. And yeah, if you guys want to hit publish, we are fine with that too.

**Alishia Natiello:** Yeah, just checking because I know some people prefer to put it in staging and then transfer it. But honestly, I think the best way to do it is to put it as draft.

**Alishia Natiello:** And like I said, we'll go through a few examples first.

**Alishia Natiello:** And then when it feels good, like, and I'll be the one to publish or if I need to, like, enlist Nicole or someone else on our team, then we'll do that.

**Alishia Natiello:** And then when we feel confident, we can move to your team's publishing abilities.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Wonderful.

**Alishia Natiello:** Great. I guess my first question is, will these be utilizing new styling as well, like formatting templates?

**Alishia Natiello:** Will these be utilizing like new styling as well, like formatting templates?

**Alishia Natiello:** Jen, was that like discussed or is this more like we've just talked about the copy itself?

**Jennifer Bulmash:** On yesterday's call?

**Jennifer Bulmash:** Yesterday was more just a discussion of kind of the capabilities and sort of the way that the process will ramp up.

**Alishia Natiello:** We looked at, and I can connect with you offline if it's easier.

**Jennifer Bulmash:** I can show you some of the things we talked about, but basically, no, yeah, no, you're fine.

**Jennifer Bulmash:** Basically talking about, you know, the initial, I've written this up here.

**Jennifer Bulmash:** Talking about kind of the initial clusters of topics that we'll focus on for BES and then sharing some example, basically like article supporting topics.

**Jennifer Bulmash:** And then, um, is it, Eric, sorry.

**Jennifer Bulmash:** Aida or Ida?

**Erik O'Brien:** Aida?

**Jennifer Bulmash:** Aida.

**Jennifer Bulmash:** Aida, thank you.

**Jennifer Bulmash:** Aida was, she's kind of a content editor and she basically was showing, discussing kind of how more the content process would work.

**Jennifer Bulmash:** So I'd say we talked about, you know, would be articles and blog posts, but that there wouldn't maybe be expanded capabilities to some other formats.

**Jennifer Bulmash:** So if you have interest in understanding like format here, I think this might absolutely be the appropriate place, at least to give Eric questions to go back to the team with if he can't answer.

**Jennifer Bulmash:** Or Eric, if I'm speaking out of turn, please feel free.

**Jennifer Bulmash:** We may have covered that.

**Jennifer Bulmash:** had a lot of calls that day.

**Erik O'Brien:** Yeah, no, we have not gone that deep yet.

**Alishia Natiello:** Okay, so then I'll incorporate that and we can kind of see as well, kind of, whose responsibilities is it?

**Alishia Natiello:** How do we, like, are we going to continue working together on those points, et cetera, et cetera.

**Alishia Natiello:** Okay, thank you for letting me set that up.

**Alishia Natiello:** Apologies as I'm catching up, but I appreciate it.

**Alishia Natiello:** Okay, let me share my screen. You see that okay?

**Erik O'Brien:** Yep.

**Alishia Natiello:** Great. I'll go between the back end and the front end. Let me start by showing you how it looks on the front end.

**Alishia Natiello:** So all of our resources — articles, blog posts, and some other standalone pages — are found via the main menu at the top. If you scroll down to resources, you can click on the Resource Center, which is a search container where you can look across all content. Users can filter by type like blog posts, publish date, sort order, and so on. We have it all designated here. We don't actually have podcasts. So you'll be dealing with articles and blog posts — just those two, right Jen?

**Jennifer Bulmash:** Um, we didn't, yeah, we didn't discuss it.

**Jennifer Bulmash:** I think it's definitely more, um, the content related just articles.

**Jennifer Bulmash:** And blog posts and then maybe like new content from them as well as refreshing existing.

**Jennifer Bulmash:** I did a kind of a poor job yesterday, but I was trying to talk about the differences between kind of what we label an article and then what's actually an article with like a teaser paragraph to a third party page versus like an actual article on the blog.

**Jennifer Bulmash:** So we'll probably have to delve back into that at some point.

**Jennifer Bulmash:** But yeah.

**Jennifer Bulmash:** I was following you. I'm good at comms, but I've been in meetings all week and I'm having screen fatigue. So thank you.

**Alishia Natiello:** Okay.

**Alishia Natiello:** So I'll just kind of open a few of these to visually show what Jen was talking about yesterday and now.

**Alishia Natiello:** So this is where we get into formatting. At the heart of it is: what is the content, who's writing it, who's the audience, and the casualness of it versus the authority kind of viewpoint, right?

**Alishia Natiello:** Like casual, I guess, meaning more opinion-based for blog posts, articles being more fact-based, kind of used as a third-party resource by whoever's, you know, viewing it, whether it be clients, competitors, interested parties, etc.

**Alishia Natiello:** And what I'll do then is I'll also show you in the background how that looks.

**Alishia Natiello:** In this case, I think we have at the end of this function, should know.

**Alishia Natiello:** Yeah, so this is kind of referencing a full article, and that's why we've like labeled it as a blog post, because it's an entity that's kind of set up severance.

**Alishia Natiello:** Separately, but we wanted to have our own take on it, and how not just a bunch of companies can utilize this new resource, but it's like, what's rimkus' perspective on it?

**Alishia Natiello:** So when we get into the back end, and once you're logged into the CMS, you can directly go to the edit page.

**Alishia Natiello:** I'll also show you on the dashboard here.

**Alishia Natiello:** When you log in, you'll see on the left-hand side all the different designations.

**Alishia Natiello:** So articles will take you just to those post types.

**Alishia Natiello:** Blog posts are a separate type, and it's important to make sure we know which is within it's posted there for the search, as well as you can see, when I click in here, they have a distinguished URL.

**Alishia Natiello:** So everything that's labeled as an article.

**Alishia Natiello:** It'll have that in the URL string, here, so, I should go to see the blog, I think it said click here, yeah, so you'll see rimkus.com slash article slash title, blog post, it's blog slash title.

**Alishia Natiello:** So that's why I have those separate to create, and back to kind of the format here, we have everything in blocks, we don't have, I would say, we have some template guidelines around the formatting, we don't have specific pattern in place to say, we have to have this and this exact spot, like, a header here.

**Alishia Natiello:** Here, an image there, you know, we rarely just take that approach based on how long the content is, does it need visual aspects, you know, all those sort of things.

**Alishia Natiello:** But for the main part, yeah, when you add the page title, that's automatically the H1.

**Alishia Natiello:** We do have H2, we need to update some of the, I would say, back-end styling for the following headers.

**Alishia Natiello:** But a good approach that Jen and others have done is to clone an existing article and recreate it with new content, or you could make a template and then use that template to plug and play the updated content.

**Alishia Natiello:** Is this making sense so far?

**Alishia Natiello:** Any questions?

**Erik O'Brien:** That makes sense.

**Alishia Natiello:** So all of this is at the liberty of our discussion during review — we can tweak formatting, add color, emphasize things. But Erik, a key question is: will you finalize the formatting, headers, and styling recommendations for your team, and who will be in charge of selecting photos — will that come from GrowthX or our side? I think we need to be clear on who owns and is responsible for each piece.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yeah, because we don't do like image selection if you guys want to use stock photos, but we do image generation.

**Erik O'Brien:** So that's an option we can explore and that would essentially use your brand guidelines that you've shared with us.

**Erik O'Brien:** And then it would be kind of relevant to what that article is or blog post to generate those images.

**Erik O'Brien:** So we can definitely like generate a few without building a whole pipeline for it and just kind of get your thoughts on if this is something you guys want to do.

**Erik O'Brien:** Otherwise, you know, we're happy to kind of defer to you guys if you guys have image selection or you guys have subscriptions to those services.

**Alishia Natiello:** We do.

**Jennifer Bulmash:** Cool. Yeah, when we discussed this with our Shutterstock call, it felt like we were probably moving in that direction to use something of that nature.

**Jennifer Bulmash:** So if it's candidly, if this is like an additional cost or a big additional lift, I assume we'll probably want to be the ones choosing the images just to kind of eliminate some of the length that the technical review of that would take.

**Jennifer Bulmash:** I think I went into this a little bit with Ada before as well.

**Jennifer Bulmash:** For some blog posts and articles, it won't matter what photo we use — it can be generic and it'll be great. But for others, like the Life Sciences group in particular, it'll be so specific that it has to be reviewed, approved, and selected by their team. So it just feels like it would be a huge extra step for everyone.

**Erik O'Brien:** So we might as well just handle most of it on our side is the way I'm leaning.

**Alishia Natiello:** Okay.

**Alishia Natiello:** Yeah, I'm in agreement there, Jen.

**Alishia Natiello:** And then same thing, like once kind of.

**Alishia Natiello:** It's like, I like seeing it in, rolling out in stages, right?

**Alishia Natiello:** Of, right, we're in the stage one soon of the testing, the basic content, we're going to hit publish, and then like stage two, maybe we transition to growthx hitting publish, and then from there, maybe we are comfortable, you know, handing over the image generation for certain use cases, so on and so forth.

**Erik O'Brien:** Yeah, that works for us.

**Alishia Natiello:** Great.

**Alishia Natiello:** Okay.

**Alishia Natiello:** And I'll as well kind of show you from scratch, like the same kind of premise for formatting content length, like all that for the article side holds the same as what I kind of showed through the blog post.

**Alishia Natiello:** But what you would go ahead and do, if you're not, you know, cloning something that, cloning a template or an article that closely mirrors like the.

**Alishia Natiello:** That's Great.

**Alishia Natiello:** Format up the new piece of content, just go ahead, click Add Article, and essentially you'll just be, you know, given the blank slate with the blocks in CMS.

**Alishia Natiello:** Like I said, when you add the title, that's automatically, oh my gosh, I can't spell, but you'll see it fill in in the page title, it's the header one, it'll automatically be added into the blog.

**Alishia Natiello:** Will that be something as well, your team will like consider, you know, sometimes we have quite lengthy articles, titles, and the like.

**Alishia Natiello:** So we try to, you know, for SEO efforts as well, kind of like sometimes shorten them or change them slightly to fit in.

**Alishia Natiello:** Is that something that will be considered as the content is built?

**Erik O'Brien:** Yeah, we'll, yeah, along with the article, we'll do the full title, meta description, URL slug, everything.

**Alishia Natiello:** Awesome.

**Alishia Natiello:** Sounds good.

**Alishia Natiello:** And then, yeah, you know, your team is familiar with WordPress or other, you know, CMSs, you know, the whole blocks and patterns, how you add those in and whatnot from here.

**Alishia Natiello:** Or, you know, once you have this, copy and paste from Word or wherever, dump it right in and then format from there.

**Alishia Natiello:** I think as well, Jen, other things to consider on our side are if we need to select anything with these options here, like if we want it assigned to a region. Joe's team handles that a lot, or other designations, so we can figure that out internally.

**Alishia Natiello:** But yeah, Eric, you see here, this is where the Yoast SEO data, metadata can be entered from there, and then you shouldn't have to worry about any of this section, Eric, that's all internal stuff, and can mostly just be left untouched.

**Erik O'Brien:** All right.

**Alishia Natiello:** Any questions on adding these, navigating the CMS, anything like that?

**Erik O'Brien:** No, pretty straightforward.

**Alishia Natiello:** Great. I added the one email user. I'm assuming everyone will log on through that, or do I need to add additional accounts?

**Erik O'Brien:** Nope, that'll be between me, Ada, and our content manager should have access all through that email.

**Alishia Natiello:** Okay, awesome, great.

**Alishia Natiello:** I think that's it for now, but the next step is figuring out ownership. I like the phased approach to start from there. I'll make sure to be involved, Jen, and the two of us will be there along the way to figure out how we process that internally.

**Jennifer Bulmash:** Yeah, that's perfect.

**Jennifer Bulmash:** Erik, what Alisha is professionally hinting at is that we may have a more streamlined approach in the future. With our new CMO and shifting priorities, we were a very review-heavy organization where content would sometimes go all the way to the chairman of the board, which is pretty intense. With the new operating structure, there's a lot more freedom and trust. Once the two of us figure out our process for how far review needs to go now that we don't need board approval, we should be able to give you a more streamlined approach in the future. For now, it'll be a little clunky, but it should be smooth sailing once we ensure things look good technically.

**Erik O'Brien:** Yeah, absolutely. That's what the strategy sprint is for — to make sure we get all these things ironed out in the first eight weeks so that by phase two, we have an understanding of what steady state looks like. If improvements are coming, fantastic. Otherwise, we adjust to your process.

**Jennifer Bulmash:** Love that.

**Alishia Natiello:** Sounds good.

**Alishia Natiello:** The other outstanding item was access to Google Search Console. Nora did the Google Analytics, so I have access to Search Console. I'll add team@growthxlabs.com to Search Console now and confirm in Slack. I can see right now if it works. Do you know what permission level you need — owner, full, or restricted?

**Alishia Natiello:** Do you know if you need like full?

**Erik O'Brien:** I think full permission is fine.

**Alishia Natiello:** definitely not an owner.

**Alishia Natiello:** Okay.

**Alishia Natiello:** Great.

**Erik O'Brien:** Yeah, so a lot of it is just for us, once we get to publishing, being able to kind of track both lift of individual pieces, you know, by topic clusters that we're doing as well.

**Erik O'Brien:** So in a couple weeks, we'll be able to show you guys the Looker dashboard. That's why we're getting into Google Analytics and Search Console for publishing and reporting purposes.

**Alishia Natiello:** Great.

**Alishia Natiello:** Well, it took that email just fine, so that's good. Sometimes it gives kickback if it thinks it's a group email or shared inbox, but that worked.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** I'm sure it'll come through on my end eventually.

**Alishia Natiello:** Yeah, and just let us know if not, I can send the direct links as well.

**Erik O'Brien:** Okay, perfect.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Well, this is super beneficial for us. I'll share this with the team so they're aware of the content publishing process. If we have questions or run into issues, it'll be a week or two before we get to staging and the first article. But if we do run into any issues, I'll reach out and make sure we don't break your website.

**Jennifer Bulmash:** Promise.

**Jennifer Bulmash:** We really appreciate that.

**Alishia Natiello:** Yeah. There's a lot of other projects and new vendors joining, so I'm taking things step by step. Everything's good, everything's smooth.

**Jennifer Bulmash:** Since we have a few minutes, I wanted to ask: in addition to GrowthX contributing the majority of fresh content, we have several other initiatives that will add organic content. Alisha and I have our own process for that. But will GrowthX be tracking lift on those pieces, and will what we're doing organically impact your process or tracking? I'd love to know how we should indicate that so we can compare. Basically, how do we integrate when we're adding new content at the same time as you?

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** The short answer is we'll be able to tell specifically what our pieces are doing. We'll have everything from Rimkus and be able to show page visits and traffic to those. For our pieces that we publish, we'll be able to track them individually to see traffic and lift. We can even do it by topic cluster. So for the four clusters we showed you yesterday, we'll be able to track which cluster is moving and double down on success early on.

**Jennifer Bulmash:** That makes sense. So for example, in one of those topic clusters — we identified four BES service groups, like structural engineering and code compliance related to the facade ordinances page. If we added additional articles from that technical team at Rimkus, because they produce fresh content, can you distinguish what we added organically from what GrowthX produced? Is that included in the lift view if it's on the same topic, or do you have an indicator on your side and won't be including that in your overall view? Are you guys tracking that at all?

**Jennifer Bulmash:** Or will you have reporting capabilities for us to understand how our organic content not produced by GrowthX is doing?

**Jennifer Bulmash:** So we can compare and say, hey, it's worth it to have GrowthX handle all of our content going forward, and we just make updates, or nope, it's a healthy comparison, it doesn't matter who it comes from, it's just we're making positive strides all around, or you know what I'm asking?

**Jennifer Bulmash:** Will we be able to see any feedback from you all on content that you didn't produce?

**Erik O'Brien:** Yeah, I believe we should. I think we should be able to track what's performing on any page, even if we don't have anything to do with it. It should be within our reporting capabilities once we get that set up.

**Jennifer Bulmash:** Okay, perfect.

**Alishia Natiello:** I appreciate that. I was going to say, is there maybe an indicator in the metadata, or is it just that you know the URLs you created because you created them?

**Erik O'Brien:** Yeah, much so the latter. Nothing that we put in there for tracking purposes — no JSON files, no embedded text files. There's no secret sauce there.

**Alishia Natiello:** And the other thing is, Jen, no matter what, you guys will be the drafters of it. WordPress will show who created it, so we can see this was initiated by a specific user account.

**Jennifer Bulmash:** Perfect. Yeah, I figured we'd be able to tell because GrowthX will be the source by volume. But I keep thinking of articles from Tom Kadaris or the Legacy Sullivan team, and I wanted to see if I need to set up different analytical capabilities to compare them so we can show the impact we're having. But this preliminarily answers my question. If you think of anything else pertinent to what I was asking, tie it in. But I think that answers what I needed to know.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** Yeah, I'll definitely bring it back to Ada in case she wants to correct me. But from everything I've seen, we should be able to spot the difference between who created content, but overall track lift on any page.

**Jennifer Bulmash:** Sure.

**Jennifer Bulmash:** Okay.

**Jennifer Bulmash:** Thank you.

**Jennifer Bulmash:** And I know an Ida who spells her name like Ada. I have an inclination to call her Ida, so please correct me. I hate when people get names wrong, so please feel free to interrupt me.

**Alishia Natiello:** It's AIDA — A-I-D-A.

**Jennifer Bulmash:** Got it. I knew an Ida and she beat me into submission, so now I'm working the opposite direction.

**Erik O'Brien:** Awesome. Well, happy to give you guys back nine or ten minutes.

**Jennifer Bulmash:** Yeah, we'll take it.

**Erik O'Brien:** Thank you for this walkthrough. We'll talk to you guys soon.

**Alishia Natiello:** We'll talk tomorrow, Jen. I'll see you next week, Erik. Thanks, Erik.

**Jennifer Bulmash:** Thanks, Erik. Bye y'all. Thanks, Alisha.
