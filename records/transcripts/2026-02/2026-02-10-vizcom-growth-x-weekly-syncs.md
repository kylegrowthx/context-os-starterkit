# Vizcom <> Growth X - Weekly Syncs

<metadata>
date: 2026-02-10
time: 17:30 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants: Carly Piekos, Sophia Silver, Kim Lu
fathom_recording_id: 121257893
fathom_url: https://fathom.video/calls/561182206
share_url: https://fathom.video/share/hmA3ezWeyc4o1u7zj8osXUQ8hqvzb6yb
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Carly presented critical technical SEO findings from a recent site crawl and aligned with Kim on blog strategy and content publication cadence. The team discovered a server loopback issue affecting all indexed pages, 22 404 errors, 44 orphaned URLs, and missing H1 tags, with Carly to provide remediation steps. Kim approved a blog redesign plan using category subpaths (e.g., `/blog/product-updates/`) to improve UX and SEO hierarchy, plus a publishing schedule of 10 articles/week to clear backlog. GTM schema implementation is blocked on variable configuration; Kim to grant Carly view-only access to debug and complete setup.

---

## Context

Vizcom is a GrowthX client working to optimize their content marketing presence and technical SEO performance. This weekly sync is a standing meeting between Carly Piekos (GrowthX SEO and content strategist) and Kim Lu (Vizcom's product and content lead), with Sophia Silver (Vizcom) observing. The team is focused on executing a blog content publishing strategy, resolving technical site issues discovered during a recent migration, and implementing structured data markup for improved search engine visibility.

---

## Relevance

**To GrowthX Delivery:**
- Expanded technical SEO scope for Vizcom: uncovered server loopback issue, 22 404 errors, 44 orphaned URLs, and missing H1s requiring immediate remediation
- Blog redesign strategy using category subpaths (e.g., `/blog/product-updates/`) aligns with LLM-friendly content architecture and SEO best practices
- GTM schema implementation blocked on variable configuration — Kim to grant Carly view-only access for debugging
- Publishing cadence increased to 10 articles/week to clear backlog, then revert to 5/week maintenance pace

**To CheckThat:**
- Structured data and semantic hierarchy improvements support AI visibility and model comprehension of blog content
- Category-based URL structure and breadcrumb navigation create clearer content signals for LLM indexing

**To GrowthX Business Development:**
- Vizcom showing strong engagement: 14 drafts approved for review, 5 new drafts in progress, active content pipeline
- Risk: Comparative listicle content on hold pending internal strategy alignment — potential expansion opportunity if competitive benchmarking becomes priority

---

## Overview

- **GTM Schema Blocked:** Dynamic schema setup is blocked by undefined variables in GTM. Carly will investigate after receiving view-only access.
- **Blog Redesign Approved:** The blog will be restructured with category subpaths (e.g., `/blog/product-updates/`) to improve UX and create a clear SEO hierarchy.
- **Critical Site Issues Found:** A technical audit revealed a server loopback issue, 22 404s, and 44 orphaned URLs requiring immediate attention.
- **Content Pipeline Paused:** 14 drafts are ready for review, but comparative listicles are on hold pending internal alignment on competitor-focused content strategy.

---

## Key Topics

### Technical SEO Audit Findings

  - A technical crawl identified several critical issues post-migration.
  - **Major Issues:**
      - **Server Loopback:** A rare server issue affecting all indexed pages. Carly is researching a fix.
      - **404 Errors:** 22 pages return 404s; Vizcom must decide whether to redirect or restore them.
      - **Orphaned URLs:** 44 pages exist in the sitemap but have no internal links, preventing them from being crawled and ranked.
      - **Missing H1s:** Several URLs lack H1 tags, a key SEO element.
      - **Empty Content Pages:** Indexable pages with placeholder content were found, suggesting they were published accidentally.
  - **Warnings:** Minor issues like links without internal outlinks were noted but are not high priority.

### GTM Schema Implementation

  - **Problem:** Dynamic schema setup in GTM is failing due to undefined variables (e.g., `page title`, `meta description`).
  - **Diagnosis:** The GTM preview and Google's Rich Results Test both confirm the variables are not being pulled correctly.
  - **Action:** Carly will investigate the correct dynamic variable configuration after receiving view-only GTM access.
  - **Note:** The `Organization` schema tag must be restricted to the homepage only.

### Blog Strategy & Redesign

  - **Problem:** The current blog hub page is visually overwhelming due to large featured posts and a flat structure, creating a poor user experience.
  - **Solution:** Restructure the blog around category subpaths.
      - **Hub Page:** Feature one hero post and small grids for each category (e.g., Product Updates, Community).
      - **Category Pages:** Each category becomes a dedicated page with its own URL (e.g., `/blog/product-updates/`).
      - **Breadcrumbs:** Implement breadcrumb navigation on individual articles to show the user's path (e.g., Home \> Blog \> Category \> Article).
  - **Rationale:** This creates a clear hierarchy for users and search engines, improving UX and SEO.

### Content Pipeline & Publishing

  - **Status:**
      - 14 drafts are ready for review.
      - 5 new drafts are in progress.
      - 4 articles are being revised today based on Vizcom's feedback.
  - **Publishing Plan:**
      - **Cadence:** Publish \~10 articles/week to clear the backlog, then return to the standard 5/week.
      - **Blocker:** Comparative listicles are on hold pending internal alignment on competitor-focused content strategy.
  - **Next Step:** Vizcom to approve topics in the "Considering" tab of the content tracker.

---

## Action Items

**Carly Piekos**
- Upload meeting recording to call notes
- Set listicle/comparative blog drafts to 'waiting' status
- Re-check Google indexing for published articles
- Upload technical crawl report to shared Drive; send Kim 404s + H1-missing lists
- Investigate server loopback; send step-by-step fix to Kim
- Investigate placeholder-content indexable pages; report findings to Kim

**Kim Lu**
- Grant Carly GTM view-only access (carly@growthx.do.ai); then Carly review schema/variables
- Approve blog topics in 'Considering' doc; then Carly finish editing listicles
- Email Carly roadway, signups, demo request reports

---

## Transcript
**Sophia Silver:** This meeting is being recorded.

**Carly Piekos:** Hello, everyone.

**Carly Piekos:** Happy Tuesday.

**Sophia Silver:** Happy Tuesday.

**Carly Piekos:** How's everything going with everyone?

**Sophia Silver:** So far, so good, I think.

**Sophia Silver:** We might have our CEO, Jordan, join us today.

**Sophia Silver:** But TBD, because he's in an on-site in Oregon, right?

**Sophia Silver:** So, okay.

**Sophia Silver:** Yeah.

**Sophia Silver:** He might pop in.

**Sophia Silver:** He might not, but yeah.

**Carly Piekos:** All right.

**Carly Piekos:** Well, then I will get to our agenda.

**Carly Piekos:** Share my screen.

**Carly Piekos:** Is there anything top of mind that has come up in the last week?

**Kim Lu:** That's me too.

**Kim Lu:** One call that I added to the agenda is I set up the, I was setting up the Google Tag Manager things.

**Kim Lu:** Yeah.

**Kim Lu:** And did run into an error with the variables.

**Kim Lu:** I screenshot it.

**Kim Lu:** Validate container.

**Kim Lu:** Yeah.

**Kim Lu:** Right there.

**Kim Lu:** So I was just curious if I need to go in and add the variables for like featured image, meta description, if I had to do that in Google Tag Manager.

**Carly Piekos:** Let me see.

**Kim Lu:** Yes.

**Kim Lu:** I'm also going to record this.

**Carly Piekos:** Oh, perfect.

**Carly Piekos:** It's already.

**Carly Piekos:** Yeah, yeah, it's recording.

**Carly Piekos:** And I'll put the recording in our call as well.

**Kim Lu:** Okay, sweet.

**Kim Lu:** Yeah, because I think Jordan wanted to take a beep.

**Carly Piekos:** Why is this not letting me get out of here now?

**Carly Piekos:** Hold on one second.

**Kim Lu:** If it's easier, I can also share my screen as well.

**Carly Piekos:** Yeah, let's share your screen and then.

**Kim Lu:** Sweet.

**Kim Lu:** Let me do that.

**Kim Lu:** Okay, sweet.

**Kim Lu:** So I set up the schemas for the tags here.

**Carly Piekos:** Okay.

**Kim Lu:** So I just followed the Google Doc, which was very helpful.

**Kim Lu:** Thank you.

**Carly Piekos:** No problem.

**Carly Piekos:** Yeah.

**Kim Lu:** But when I run preview, it gives an error around like the variable, I think, in the HTML snippet is not defined, I believe.

**Kim Lu:** So I'm just curious if I need to go in and actually set each of these variables.

**Carly Piekos:** Can you open the variables?

**Carly Piekos:** I just want to see how it's, what it looks like.

**Carly Piekos:** Yeah.

**Carly Piekos:** All right.

**Carly Piekos:** So let's go into configuration.

**Carly Piekos:** Okay.

**Carly Piekos:** So it says data variable not defined, and then there is no meta variable.

**Kim Lu:** Yeah, I think all of them, like even like page title, everything is not defined.

**Kim Lu:** So I can go in and add them.

**Kim Lu:** I just wanted to make sure that's the right.

**Carly Piekos:** I don't feel like that should be a big issue.

**Carly Piekos:** Would you mind going back to the tags?

**Kim Lu:** Yes.

**Carly Piekos:** And then I'll just, if you could just open up one of the schemas.

**Kim Lu:** Yeah.

**Carly Piekos:** Okay.

**Carly Piekos:** Okay.

**Carly Piekos:** So what we need to do for this one, this is the tag configuration for.

**Kim Lu:** This is for.

**Kim Lu:** This is for.

**Kim Lu:** Thank

**Kim Lu:** The blog pages path.

**Carly Piekos:** Okay, so it's blog pages path.

**Carly Piekos:** Vizcom, Team, Date Published.

**Carly Piekos:** So we're going to...

**Carly Piekos:** All right, and can we open the other one, please?

**Kim Lu:** Yeah.

**Carly Piekos:** Same as that.

**Carly Piekos:** Okay.

**Carly Piekos:** Did you test these?

**Carly Piekos:** Did you...

**Carly Piekos:** Well, the preview, yes.

**Carly Piekos:** So it says preview.

**Carly Piekos:** When you go to preview, what does it say?

**Carly Piekos:** Okay.

**Carly Piekos:** Page title not found.

**Carly Piekos:** All right.

**Carly Piekos:** So within this schema, it says blog path pages custom HTML.

**Carly Piekos:** We need to fill out a couple of things within the actual schema.

**Kim Lu:** For the blog pages path.

**Kim Lu:** Okay, just pull that back up again.

**Carly Piekos:** All right, so page title, description, meta description, featured image, publisher.

**Carly Piekos:** Okay, it should be end script.

**Carly Piekos:** So that should be good.

**Carly Piekos:** I'm not sure.

**Carly Piekos:** Let's go back.

**Carly Piekos:** And you're, like, I know that this probably is, like, really just overwhelming with all of the different variables and types of triggers.

**Carly Piekos:** Have you done this before?

**Carly Piekos:** Have you?

**Carly Piekos:** Okay, so you're, yeah.

**Carly Piekos:** So don't worry.

**Carly Piekos:** This is not going to mess up the site at all.

**Carly Piekos:** What we just need to do is we need to kind of take, did you publish it yet or no?

**Kim Lu:** No, not yet, but I'm happy.

**Carly Piekos:** No, no, you don't, don't publish it quite yet.

**Carly Piekos:** What I'd like to do is, let's say, blog pages, view, page view, blog page.

**Carly Piekos:** Pages 20 minutes ago.

**Carly Piekos:** Yep.

**Carly Piekos:** Let's preview those again.

**Carly Piekos:** Yeah.

**Carly Piekos:** So if we're going to do like a generalized for the blog path pages for the meta descriptions, we need to figure out how to dynamically pull that in.

**Carly Piekos:** Let me look into this a little bit further.

**Carly Piekos:** I just want to make sure you're setting it up right before you publish it.

**Carly Piekos:** And then I'm going to run.

**Carly Piekos:** Did you test it in Rich Snippets?

**Kim Lu:** No.

**Carly Piekos:** All right.

**Carly Piekos:** So if you could go to another tab and put in Rich Validation, Google.

**Carly Piekos:** It should.

**Kim Lu:** Rich Text Validation?

**Carly Piekos:** Yeah.

**Carly Piekos:** Yeah.

**Carly Piekos:** Rich results.

**Carly Piekos:** So what this will do, you could put in if you just.

**Carly Piekos:** Just click on Code, and what you can do is paste the code in first, and what it will do is it will tell you where the errors are.

**Carly Piekos:** So this is like a really good way for, because it's basically telling you exactly what you're going to be pulling.

**Kim Lu:** Sweet.

**Kim Lu:** So I'll put in like a schema.

**Carly Piekos:** Yeah, so let's put in the schema, okay, for that, yep.

**Carly Piekos:** Let's see, no items detected.

**Carly Piekos:** All right, so I think it's because we have the logo, LinkedIn, Twitter, and we have the organization.

**Carly Piekos:** So the organization schema is supposed to be on one page only.

**Carly Piekos:** That's your homepage, right?

**Carly Piekos:** So we have to configure that just to the homepage.

**Carly Piekos:** Is that how it is within the...

**Kim Lu:** I think the organization is for all.

**Kim Lu:** Sorry, it's right here.

**Kim Lu:** So organizations, organizations, all pages.

**Kim Lu:** So

**Kim Lu:** And then the second one is just a software application.

**Carly Piekos:** Yes, that's right.

**Carly Piekos:** 100%.

**Carly Piekos:** All right.

**Carly Piekos:** So let's scroll down.

**Carly Piekos:** See, I would always did this by page.

**Carly Piekos:** So I'm trying to figure out how to do it dynamically so it will publish.

**Carly Piekos:** Let me look a little bit further into this before you go any further and put any more effort into this.

**Carly Piekos:** And I will get back to you today on that.

**Kim Lu:** Yeah, no worries.

**Carly Piekos:** I just don't want you to do more work than you have to.

**Kim Lu:** Did you have access to our tag manager?

**Carly Piekos:** I do not have access.

**Carly Piekos:** But if you want to give me access, that would be super helpful.

**Kim Lu:** So then I can just go in.

**Kim Lu:** I'm not going to publish anything or do anything in there.

**Kim Lu:** I just want to make sure that everything is set up properly.

**Kim Lu:** Okay.

**Kim Lu:** I will.

**Kim Lu:** should I?

**Kim Lu:** Okay.

**Carly Piekos:** Just my GrowthX email should work.

**Kim Lu:** Okay.

**Kim Lu:** Got it.

**Carly Piekos:** Carly at growthx.do.ai, I will need to do that after because I don't have admin access, but.

**Sophia Silver:** That might be a Kaylin request, Kim, that I can, he might be an admin in Tag Manager.

**Carly Piekos:** Yeah, you can give me view only so that way nothing or just so they don't feel like I'm going to do anything weird in the background.

**Carly Piekos:** I just want to be able to see it so that way I can look a bit further into it without having to inspect the actual code on the site.

**Carly Piekos:** Because if it's not published, I'm not going to be able to see it on the site.

**Kim Lu:** Cool.

**Carly Piekos:** All right.

**Carly Piekos:** So we will get that sorted.

**Carly Piekos:** And this is like priority is like medium to low.

**Carly Piekos:** It's just for the LLL models to kind of have just like a little bit of a booster.

**Carly Piekos:** So that's good.

**Carly Piekos:** What I did uncover are a couple of technical things today.

**Carly Piekos:** So I wanted to go over that.

**Carly Piekos:** We have the blog layout recommended.

**Carly Piekos:** recommendations.

**Carly Piekos:** I have the revisions that, and those will be complete today.

**Carly Piekos:** So all the notes that you made on the revisions that are needed for the articles, I think there was like four or so of them.

**Carly Piekos:** She's working on that today.

**Carly Piekos:** And then we need additional topics to be approved in the considering.

**Carly Piekos:** That was pretty much it for that.

**Carly Piekos:** But we are working on these five new drafts this week.

**Carly Piekos:** You have 14 drafts that are ready for review, so we'll open that.

**Carly Piekos:** I did break out everything by week.

**Kim Lu:** I don't know how much you want to go off of that, or if that even works for you.

**Carly Piekos:** Just let me know.

**Carly Piekos:** It takes a second to load.

**Kim Lu:** I have reviewed those 14 drafts, and I just been commenting on the drafts.

**Carly Piekos:** here?

**Carly Piekos:** Okay.

**Carly Piekos:** Yeah.

**Kim Lu:** Or no, I've been commenting on the specific Google Doc itself.

**Carly Piekos:** But let me know if you want me to like.

**Carly Piekos:** Oh, no, this specific Google Doc is perfect because then any note that you make within that, we can go into the version history.

**Carly Piekos:** So if I go into file version history, C version, I can see the last time you commented.

**Kim Lu:** And then when we update it, we can go back to the previous version and go back and forth.

**Carly Piekos:** So, yeah, Google Doc is perfect.

**Carly Piekos:** How to track those changes.

**Carly Piekos:** And Jenny gets that right away.

**Carly Piekos:** So she'll be able to make those edits like almost immediately.

**Kim Lu:** She gets an alert.

**Carly Piekos:** So the staged in CMS, we have these.

**Carly Piekos:** Oh, yeah.

**Carly Piekos:** So that's what I did.

**Carly Piekos:** I did the priority on like the weeks, two weeks out, three weeks out, next week.

**Kim Lu:** I'm not sure if you wanted to go by this schedule.

**Kim Lu:** What are your thoughts on that?

**Kim Lu:** And these are in terms of like publishing, right?

**Carly Piekos:** Yes.

**Carly Piekos:** Just things for you to look over for that week, just so we're not like completely overflowing the blog pages with all.

**Carly Piekos:** So.

**Carly Piekos:** of the blogs at once.

**Carly Piekos:** So we're like maybe posting like 10 a week until we get all of these kind of solidified and then we can be back on our regular like five per week publishing schedule.

**Kim Lu:** Yeah, this looks good to me.

**Kim Lu:** One small call out is just like around, I know in this recent batch we'd had a few that were kind of listicle like comparative style content.

**Kim Lu:** Those we might want to hold off on publishing just given like we're not sure their current stance on like publishing comparative content.

**Kim Lu:** So that just might be a small call out.

**Carly Piekos:** Okay.

**Carly Piekos:** So is there is this something that just came up recently or is it something that you need like a more thought around or more like proof behind the pudding kind of thing on why the why behind it?

**Kim Lu:** I think we're just it's been like a theme that came up around like how we want to talk about our competitors, at least in our written blog content.

**Kim Lu:** So until we're just confident.

**Kim Lu:** As a team around publishing content in that area, I think we'll just hold off on pushing those live for now.

**Carly Piekos:** Okay, perfect.

**Kim Lu:** But everything else should be good to be published.

**Carly Piekos:** So did you want the listicles, did you want me to put them as a different status, like they're staged in CMS, but maybe put them under a different priority, like we're waiting on those?

**Kim Lu:** Yeah, that actually would be helpful.

**Kim Lu:** But regardless, we'll be able to see it in Webflow before we publish.

**Kim Lu:** So, yeah.

**Carly Piekos:** All right, perfect.

**Kim Lu:** Yeah.

**Carly Piekos:** All right, so we have those ready.

**Carly Piekos:** She commented on those.

**Carly Piekos:** And then we have our published articles.

**Carly Piekos:** I ran all of them through Google Search Console.

**Carly Piekos:** I requested indexing for the pages that did not, and they came up fine.

**Carly Piekos:** I will do another run through and make sure that they are indexed and everything is coming up like it's supposed to in Google within the next week.

**Carly Piekos:** Because I did it on Friday, it should take about a week or so to get any kind of traction.

**Carly Piekos:** or so to If we

**Carly Piekos:** Get it before then?

**Carly Piekos:** Great.

**Carly Piekos:** If we don't, it's par for the course.

**Carly Piekos:** Let's see.

**Carly Piekos:** So I did go in, I'm going to share this.

**Carly Piekos:** I did a technical crawl and I'm going to be putting this into our shared Google Drive under the technical.

**Carly Piekos:** I just wanted to take a look at what issues might have come up since the migration.

**Carly Piekos:** Um, and one of these, which is like a kind of a rare issue.

**Carly Piekos:** Um, so this is about like your server and your loopback.

**Carly Piekos:** I have to go a little bit deeper into how to fix this because I've only come across this like twice in my career.

**Carly Piekos:** So, um, and I'm not like a server engineer or anything, so I'm, I'm not really sure how to go about, um, fixing this exactly.

**Carly Piekos:** So I will have a more detailed analysis on how we can go like a step-by-step process on how to fix this.

**Carly Piekos:** Um, but essentially it's just like a loop back.

**Carly Piekos:** Um.

**Carly Piekos:** Address and it might be affecting like 100 or so pages and it's, let me see what specifically, so it's just going back to your server as, and then looping back to like another type, it might not be able to be found on the internet, which would be very, very bad.

**Carly Piekos:** So once I look a bit further into this issue and how to actually resolve it and what the lift will look like from your end, we can go a little bit deeper into this, but it is for all of your pages as of right now that are being indexed.

**Carly Piekos:** You have 22 pages that are 404 and I'm not sure if these pages are, just need to be redirected or if these are pages of value.

**Carly Piekos:** So I'm going to send you these, this page list, the description and how to fix it for these.

**Kim Lu:** Yeah.

**Carly Piekos:** The sitemap, you said dynamically updates.

**Carly Piekos:** So it should dynamically update.

**Carly Piekos:** I crawled this again this morning.

**Carly Piekos:** So I didn't see anything change with the 44 URLs, with the orphaned URLs.

**Carly Piekos:** So we just need to review them and link them internally from the website.

**Carly Piekos:** That way they'll actually rank their results.

**Carly Piekos:** And then any of the ones that we just have to make sure that they're all in there.

**Carly Piekos:** So it's just like a quick, like, check for those 44 sitemap or those URLs within the sitemap.

**Carly Piekos:** What I'm finding with other clients is that when your sitemap is dynamically updating or when their sitemap is dynamically updating, it's not removing any of the URLs from the sitemap.

**Carly Piekos:** It's just adding.

**Carly Piekos:** So I just want to make sure that these are not maybe URLs that have been redirected or they no longer exist.

**Carly Piekos:** So we just have to make sure we do a spot check on all of these.

**Carly Piekos:** Um, you have H1s missing on these specific, uh, URLs.

**Carly Piekos:** So I will send this over.

**Carly Piekos:** So I'm only sending over these main issues.

**Carly Piekos:** Right.

**Carly Piekos:** That's all that needs to be fixed.

**Carly Piekos:** Your warnings, you're fine.

**Carly Piekos:** Uh, JavaScript, you can't really, you have no control over that.

**Carly Piekos:** Um, this one I would like to take a look at.

**Carly Piekos:** It says there, you have like a placeholder there.

**Carly Piekos:** But these pages are indexable.

**Carly Piekos:** So I have to look a bit further into why this is happening.

**Carly Piekos:** Um, it's basically like you're, you don't have any content on the page it's saying, but.

**Sophia Silver:** I wonder if it's a page that's published, that's not meant to be published.

**Carly Piekos:** That could be.

**Carly Piekos:** Could be.

**Carly Piekos:** So I will add like the other warnings like that I find that are an issue.

**Carly Piekos:** Not a lot of them are.

**Carly Piekos:** Um, the canonicalized, these, I mean, they're like nobody.

**Carly Piekos:** Um, we have links without internal outlinks, not a huge issue at all.

**Carly Piekos:** So basically we have like seven major issues and like a couple of warnings we might want to take a look at, um, that are high priority.

**Kim Lu:** Okay.

**Carly Piekos:** All right.

**Carly Piekos:** Um, what else did we want to go over today?

**Carly Piekos:** Oh yes, the blog layout.

**Carly Piekos:** So I put your UX improvements and recommendations.

**Carly Piekos:** Now this is just based off of what other clients are doing.

**Carly Piekos:** Um, I also like ran it, uh, through AI and did like best practices for blogs specifically in Webflow.

**Carly Piekos:** Um, so there were a couple of recommendations.

**Carly Piekos:** I did the proposed solution.

**Carly Piekos:** So the current issue, there's like four large feature posts with like massive images and author headshots and long excerpts.

**Carly Piekos:** Um, so it's like a visual overload as you were talking about what we would like to do is kind

**Carly Piekos:** Kind of pare that down a little bit.

**Carly Piekos:** I'm not sure if you can use like one hero featured post and then kind of it goes kind of feeds into that specific category page.

**Carly Piekos:** And then you might want to move like the main article grid below instead of having it all on one, like the blog hub page, maybe have like mini grids for the blog page, if that makes sense.

**Sophia Silver:** Yeah, by like mini grid, do you mean like the other, like, because right now we have them in like little cards below.

**Sophia Silver:** Are you saying like move that up more on the page?

**Carly Piekos:** let's here, let's, let's pull it up.

**Carly Piekos:** Yeah, that might be helpful.

**Carly Piekos:** Oh, there she goes.

**Carly Piekos:** Block.

**Carly Piekos:** Right.

**Carly Piekos:** So you have the cards here, right?

**Carly Piekos:** These cards, but maybe per category.

**Carly Piekos:** So the all might be a little bit redundant because we are on the all page right now.

**Carly Piekos:** And we could do that, but we could make like product updates, one image, insight, community, creators, and that way, then those are their own separate hub pages.

**Sophia Silver:** Gotcha.

**Sophia Silver:** Yeah.

**Carly Piekos:** So like product updates would be blog slash product updates slash whatever that blog is.

**Sophia Silver:** Yeah.

**Carly Piekos:** So that way the breadcrumb would be more of a flow and you're not just going, okay, product updates, and then it's just updating like this, right?

**Sophia Silver:** Yeah.

**Carly Piekos:** We could just have one image, one image, one image, and then it goes into those actual category pages.

**Sophia Silver:** Yes, that makes sense.

**Sophia Silver:** Yeah.

**Carly Piekos:** So that might...

**Carly Piekos:** Be one of the ways we can get just a better user experience.

**Carly Piekos:** The expected impact from what I was doing the research on would be a 50% reduction in initial, like, whoa, this is a lot of stuff going on on this site, right?

**Carly Piekos:** The cognitive overload.

**Carly Piekos:** And then the LLM and SEO, I wanted to make sure that it was also going to fit in line with what our goals are.

**Carly Piekos:** So the content is just will be more distinct, it will have a hierarchy, and it will have those breadcrumbs leading you back to that blog page.

**Kim Lu:** Are bread, like, is having that hierarchy more helpful for LLM versus like, because right now, the filter is a tag on the URL, right?

**Carly Piekos:** Yeah.

**Kim Lu:** Okay, is it better, like, structurally to just have, like, the subpaths?

**Carly Piekos:** Um, yes, it is for a lot of cases.

**Carly Piekos:** I wouldn't say.

**Carly Piekos:** For every single case in the world.

**Carly Piekos:** But I think in your case, the path would be really useful to navigate back and forth.

**Carly Piekos:** So for instance, I will just bring up Red Crumb Best Practices.

**Carly Piekos:** Not Red Crumb, Chicken Breast.

**Carly Piekos:** Um, so, uh, let's do UX navigation and sure.

**Carly Piekos:** Um, so this is essentially how it would look.

**Carly Piekos:** You'd have your, your homepage and then it would have like the arrow that points and it would be located from a design perspective.

**Carly Piekos:** A lot of people don't like the breadcrumbs, but for a blog, I feel like it is really, um, it's really good for that user experience.

**Carly Piekos:** So people don't get overwhelmed one by all.

**Carly Piekos:** The content because you're going to have more content and two, they'll be able to navigate back and forth.

**Carly Piekos:** So it would look, not only would the URL structure be the breadcrumb, so it would be blog slash, for instance, you would fit another, like here are the vizcom blogs, right?

**Carly Piekos:** So you would have your product solutions or product updates, and then you would have blog slash insight, blog slash community would be the breadcrumb and then creator stories would be another breadcrumb.

**Carly Piekos:** So you know they're all going back to this hub page.

**Carly Piekos:** And essentially what it would look like if you were to have, it would be like home industries, Microsoft, and you should have a page for each breadcrumb you're putting.

**Kim Lu:** Like you shouldn't just have a industry and clients, a page doesn't exist for that.

**Kim Lu:** Yeah.

**Kim Lu:** Yeah.

**Kim Lu:** Sweet.

**Kim Lu:** Okay.

**Kim Lu:** Makes sense.

**Carly Piekos:** So yeah, usually like breadcrumbs are located at the top of the screen, you could probably because the blog.

**Carly Piekos:** It looks nice like this.

**Carly Piekos:** I wouldn't change what that looks like actually on the screen.

**Carly Piekos:** I would just have it within the URL path.

**Kim Lu:** Got it.

**Sophia Silver:** Yeah.

**Sophia Silver:** Yeah, that makes sense.

**Carly Piekos:** And then maybe like if you were to click into the products and updates, right, if it turns into a new page, then have the actual at the top of the page have this home breadcrumb, breadcrumb, breadcrumb.

**Sophia Silver:** Yeah.

**Kim Lu:** Yeah.

**Sophia Silver:** That makes sense.

**Sophia Silver:** And so essentially the tags would become the individual pages themselves.

**Carly Piekos:** Yes.

**Sophia Silver:** Yep.

**Sophia Silver:** Okay.

**Carly Piekos:** Yeah.

**Carly Piekos:** Just because if you're going to have that much content, breaking it up into mini hubs, category pages would make a lot of sense.

**Sophia Silver:** Yeah.

**Kim Lu:** Yeah.

**Sophia Silver:** Is it because like, and I guess like with the clients that you've worked with, when their sites are like visually like a lot, like ours are, is that just like helpful, like to have the separation out?

**Sophia Silver:** That's like, yeah.

**Carly Piekos:** Yeah.

**Carly Piekos:** Very much so.

**Carly Piekos:** Yeah.

**Carly Piekos:** So obviously like here, this is very clean and, but once you scroll down, right, you have, yeah.

**Carly Piekos:** And it, if you click on all, it's nothing is changing.

**Carly Piekos:** So they're a little confused and then you go product and then that one thing changed, right?

**Carly Piekos:** So being able to go to another screen and then have that path, because once, let's say we want to click into this blog, having a path at the top of the page and how they got there is also good for you to track that user journey.

**Sophia Silver:** Yeah.

**Sophia Silver:** That makes sense.

**Kim Lu:** Sweet.

**Carly Piekos:** Yep.

**Carly Piekos:** So this I put within our shared folder.

**Carly Piekos:** So I see that you're already in there.

**Carly Piekos:** Yeah.

**Carly Piekos:** Awesome.

**Carly Piekos:** And then the effort level, how long it'll take to do and the last.

**Carly Piekos:** Last one would be like, you're going to create like new pages, it might take a little bit to do.

**Carly Piekos:** So just, it's not like, oh my God, we got to get this done tomorrow or everything's going to be ruined.

**Carly Piekos:** You could always like reconfigure.

**Carly Piekos:** can always do redirects.

**Carly Piekos:** We just want to make sure that it's the best user experience for not only our users, but also LLM models.

**Kim Lu:** Cool.

**Kim Lu:** Thank you.

**Carly Piekos:** Appreciate this.

**Carly Piekos:** Yeah, of course.

**Carly Piekos:** Um, so those drafts are in process, uh, process.

**Carly Piekos:** We needed the additional topics to be approved.

**Kim Lu:** You know how to go in and do that, correct?

**Kim Lu:** Yeah.

**Carly Piekos:** All right.

**Carly Piekos:** I'm going to actually, I want, didn't want to do that.

**Carly Piekos:** I want to go to data, uh, blog topics for review.

**Carly Piekos:** Yes.

**Carly Piekos:** So the considering, we just got to go in here and figure out which ones that you are okay with doing.

**Carly Piekos:** And then I'll go back and finish editing, um, out those listicles.

**Kim Lu:** So that way we'll just wait on those.

**Kim Lu:** Yep.

**Kim Lu:** All right.

**Kim Lu:** All

**Kim Lu:** Sweet.

**Carly Piekos:** I didn't do any performance data for today because we're still waiting on the blog articles to kind of gain a little bit of traction.

**Kim Lu:** So that will be for next week.

**Kim Lu:** Okay, perfect.

**Kim Lu:** Yeah.

**Kim Lu:** We'll also look to publish the next batch so we can kind of like cascade that.

**Carly Piekos:** Yep, absolutely.

**Carly Piekos:** So I will look into your schema markup, make sure everything is good.

**Carly Piekos:** I will look into your revisions, make sure those are all good to go.

**Carly Piekos:** Once I get access, what was the third thing that I needed to do for you?

**Carly Piekos:** I'm just going to keep an eye on that performance.

**Carly Piekos:** And then I did keep your goals right here that we discussed last week.

**Carly Piekos:** So we can kind of feed that into our conversations every single week on how your blog pages are doing.

**Kim Lu:** Perfect.

**Kim Lu:** Yes.

**Kim Lu:** I will also share with you to your email, like just some of the roadway reports.

**Carly Piekos:** Oh, yeah.

**Kim Lu:** Thank you.

**Kim Lu:** Thank you.

**Kim Lu:** you.

**Kim Lu:** you.

**Kim Lu:** Thank Thank you.

**Kim Lu:** And signups.

**Kim Lu:** Yeah.

**Kim Lu:** I think that'll be the main one.

**Kim Lu:** And then demo request.

**Kim Lu:** Yeah.

**Kim Lu:** That one, I think we'll, I'll just monitor it just given as we don't have proper tracking for that setup yet.

**Carly Piekos:** Okay.

**Carly Piekos:** Perfect.

**Carly Piekos:** Are there any other questions, concerns, comments, maybe any adjustments you want to make?

**Kim Lu:** No, I don't think so.

**Carly Piekos:** Yeah.

**Carly Piekos:** That's wonderful to hear.

**Carly Piekos:** All right.

**Carly Piekos:** So if you need anything this week, please let me know.

**Carly Piekos:** I will get on trying to test that schema out and I will talk to you, probably give you an update by the end of the week.

**Kim Lu:** Okay.

**Sophia Silver:** Sounds great.

**Sophia Silver:** Thank you.

**Kim Lu:** Thank you.

**Carly Piekos:** a great rest of your week.

**Carly Piekos:** Yep.

**Kim Lu:** Bye.
