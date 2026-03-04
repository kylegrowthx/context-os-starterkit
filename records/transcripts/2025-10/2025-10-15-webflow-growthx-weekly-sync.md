# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-15
time: 18:00 UTC
duration: 25 minutes
organizer: liz@growthx.ai
participants: Jason Gong (GrowthX), Liz Kushnereit (GrowthX), Sydney Arin Go (GrowthX), Luke Stahl (Webflow), Vic Plummer (Webflow), Vivian Hoang (Webflow), Kelly We (Webflow), Meg Murray (Webflow), Kirat Chhina (Webflow), Colin Lateano (Webflow), Michael Huard (Webflow), Anushri Gupta (Webflow), Darin LaFramboise (Webflow), Rachel Wolan (Webflow), Zach Plata (Webflow)
fathom_recording_id: 94426452
fathom_url: https://fathom.video/calls/441107445
share_url: https://fathom.video/share/9PjaA9eMSyYuXersZevXDvcoXuuG3u_H
source: fathom
enriched_on: 2026-03-02 06:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on content and integration page production, with SEO content pieces trending upward and 30 integration pages per week in progress. The team paused new SEO article creation to evaluate performance of the initial five pieces, shifting focus toward code components and example apps instead. A key discussion centered on where to publish new integration use case guides (main Webflow site vs. dev site), with Jason Gong tasked to propose design options balancing SEO benefit against developer navigation experience and site capacity constraints.

---

## Context

GrowthX is engaged with Webflow on a strategic content and integration initiative. Sydney Arin Go leads the GrowthX side, managing SEO content creation and integration page production. Vic Plummer and Vivian Hoang lead on the Webflow side, overseeing technical implementation and developer documentation. The relationship encompasses two parallel streams: (1) SEO content creation and integration pages (which ship at 30/week and are trending upward), and (2) developer documentation and educational guides (integration use case guides like the WeGlot and Trustpilot examples). The weekly sync is a tactical alignment session reviewing production progress, technical blockers, and prioritization decisions across both streams.

---

## Relevance

**To GrowthX Delivery:**
- Integration page production at 30/week with 213 pages shipped by week end; tracking performance and reporting metrics via Amplitude exports to Colin
- SEO content paused after initial five articles to evaluate performance before scaling; shifting team capacity to code components and example apps
- New integration use case guides (WeGlot v5, Trustpilot) in final review stage with Vic; templates and structure being tested for replicability

**To GrowthX Business Development:**
- Integration page performance trending upward, indicating strong strategic fit with Webflow developer audience
- Placement decision for use case guides will drive discoverability; main site SEO benefit vs. dev site navigation experience trade-off affects long-term visibility
- Code components project identified as slow-moving but strategically important; scoping and prioritization in progress

**To GrowthX Operational:**
- FAQ schema implementation blockers on integration pages; Vivian to investigate Webflow CMS field constraints and report back
- Form integration for page submissions created and live (open access, password-protect if spam occurs); reduces manual intake work for Vic
- Dev site capacity concerns flagged by Vic; need to follow up with Fern on what can fit in existing documentation infrastructure

---

## Overview

- Integration pages shipping at 30/week with 183 published, reaching 213 by week end; performance trending upward with data requests for Amplitude analysis
- SEO content production at 1-2 pieces/week with 2 live and 3 pending; pausing after current batch to evaluate performance before scaling
- Integration use case guides: WeGlot (v5) and new Trustpilot guide ready for Vic's review; decision pending on placement (main Webflow site vs. dev site)
- Code components project scoped and prioritized; shifting team focus from SEO content to code components and example apps

---

## Key Topics

### SEO Content and Integration Pages Progress

  - 1-2 SEO content pieces/week; updating in Airtap
  - Integration pages: 30/week, currently at 183, will be 213 by week's end
  - Results trending upward; tracking ongoing
  - Data asks for Amplitude exports (for Colin)

### Integration Page Submissions

  - New form created for submissions, uploads to separate Airtable
  - Currently open access; can password-protect if spam becomes an issue
  - Vic to add form link to Marketplace docs for app marketing

### Integration Use Case Guides

  - WeGlot guide (v5) and new Trustpilot guide ready for Vic's review
  - Discussing optimal placement: main Webflow site vs. dev site
  - Considerations:
      - SEO benefit (main site) vs. better navigation (dev site)
      - Dev site search functionality vs. potential overload
      - Possible new section/tab on main site
  - Next steps: Team to propose options, investigate other companies' approaches

### Code Components Project

  - Acknowledged as moving slowly due to focus on other projects
  - Team to scope project and determine next steps

### SEO Content Strategy Adjustment

  - Currently have 5 articles (2 live, 3 pending publication)
  - Pausing creation of new articles to evaluate performance
  - Shifting focus to code components and example apps

---

## Action Items

**Vivian Hoang (Webflow)**
- File bug for web team re breadcrumbs error on blog posts

- Check feasibility of adding FAQ schema to integration pages


**Vic Plummer (Webflow)**
- Review updated WeGlot + new Trustpilot integration guides

- Ask Fern re possibility of adding use case guides to dev site search

- Follow up w/ docs team re dev site capacity for integration guides


**Jason Gong (GrowthX)**
- Propose options for integration use case guides location on website

- Create design mockups for integration use case guide pages

---

## Transcript
**Sydney Arin Go:** Hey, good evening.

**Sydney Arin Go:** This meeting is being recorded.

**Sydney Arin Go:** It's morning for you, right?

**Liz Kushnereit:** It is.

**Liz Kushnereit:** I'm trying to be considerate of your...

**Sydney Arin Go:** Thank you.

**Sydney Arin Go:** I was just curious.

**Sydney Arin Go:** People probably always forget.

**Sydney Arin Go:** No.

**Sydney Arin Go:** Yeah, no.

**Sydney Arin Go:** But it's fine.

**Sydney Arin Go:** Are you in California?

**Liz Kushnereit:** Austin, Texas, some central standard.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** I know.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** And so, your work hours, though, that you put on Google Calendar are accurate, right?

**Liz Kushnereit:** Yes.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Great.

**Sydney Arin Go:** So, I put something up quite late yesterday for you, so...

**Liz Kushnereit:** Well, for tomorrow.

**Liz Kushnereit:** So, we'll have that Webflow Q4 planning.

**Liz Kushnereit:** Yeah, we'll go over the code components agentic pipeline request, and then what Jason wants to put into the Webflow Q4.

**Liz Kushnereit:** you, Bia.

**Sydney Arin Go:** Awesome.

**Sydney Arin Go:** Hi Vivian, how's it going?

**Vivian Hoang:** Good, how are you?

**Sydney Arin Go:** I'm good.

**Vivian Hoang:** I saw your note about the updated images.

**Vivian Hoang:** So I'll get the remaining blog post staged and published later this week.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** I'm not sure if you know this, but I did notice that in Search Console there's a small breadcrumbs error on the blog posts. I figured you'd probably be aware of it, but I wanted to flag it just in case.

**Vivian Hoang:** Yeah, I've been seeing that come up. I haven't had a chance to dig into it, but it's probably something to do with the template itself. So I can just file a bug for our web team.

**Sydney Arin Go:** Yeah, I don't think it should affect things too much, but it would be nice to have it fixed because breadcrumbs are nice to have.

**Sydney Arin Go:** Actually, on that note, do you know how we can add FAQ schema to the integration pages?

**Sydney Arin Go:** that have to be something we ask your team to do?

**Vivian Hoang:** Yeah, do you have FAQs on all of the integration pages?

**Sydney Arin Go:** Yes.

**Vivian Hoang:** Okay.

**Vivian Hoang:** What about the old ones that were migrated?

**Sydney Arin Go:** The old ones, oh, the empty ones don't have anything.

**Vivian Hoang:** Uh-huh.

**Sydney Arin Go:** But everything that has a full description will also have FAQs.

**Vivian Hoang:** Okay.

**Vivian Hoang:** I am not sure how to add it to a CMS collection item if all of the items don't have FAQs because we would need to add custom code into, like, the template itself.

**Vivian Hoang:** Let me check to see if there is...

**Vivian Hoang:** A way to add in like a separate field where we can add in code, the FAQ schema in like a encode.

**Vivian Hoang:** Let me get back to you on that.

**Sydney Arin Go:** Okay, awesome.

**Sydney Arin Go:** Thank you so much.

**Sydney Arin Go:** Hey, Luke.

**Luke Stahl:** Hello.

**Luke Stahl:** Hi, everyone.

**Vivian Hoang:** Hey.

**Sydney Arin Go:** Jason said that he was going to be a little bit late.

**Sydney Arin Go:** I figure we can wait for Colin or let me just double check.

**Sydney Arin Go:** Oh, Colin's out of office.

**Luke Stahl:** So he's declined this call.

**Luke Stahl:** Oh, got it.

**Luke Stahl:** Sorry.

**Sydney Arin Go:** I totally missed that.

**Luke Stahl:** No, no.

**Luke Stahl:** It's okay.

**Sydney Arin Go:** Okay, so I'm just going to pull up the notes here and share my screen.

**Sydney Arin Go:** Is everybody seeing my screen?

**Sydney Arin Go:** Yep.

**Sydney Arin Go:** Okay, awesome.

**Sydney Arin Go:** So just a little bit of an update.

**Sydney Arin Go:** So on all the things that we're doing on the SEO content, we're still doing one to two a week.

**Sydney Arin Go:** And I've been updating that in Airtap, and I'll send you the docs ready for review.

**Sydney Arin Go:** We've got two for this week.

**Sydney Arin Go:** Webflow X integration pages are also just ongoing.

**Sydney Arin Go:** So we're doing 30 a week now.

**Sydney Arin Go:** So we're currently at 183, and we'll have 213 published by the end of the week.

**Sydney Arin Go:** We do have, you know, the same initial results that we have.

**Sydney Arin Go:** It's still trending upward, still looking good.

**Sydney Arin Go:** And we're just continuing to track that.

**Sydney Arin Go:** And later on, like, there are some data asks there.

**Sydney Arin Go:** For the integration guides, we're...

**Sydney Arin Go:** In the final steps of calibration, we have another article for review for your team.

**Sydney Arin Go:** So we edited the last one that we did, the WeGlot translation one, based on your feedback, Vic.

**Sydney Arin Go:** And then I added another one with Trustpilot to the list, just so that we can see if everything that you gave us for the WeGlot page has transferred to the new one as well.

**Sydney Arin Go:** So just more specificity, more details, more actionability, and all of that.

**Sydney Arin Go:** So that's the quick rundown of everything that doing.

**Sydney Arin Go:** So again, integration pages are trending upwards, so we're still seeing that steady state of it's going up.

**Sydney Arin Go:** And we did have a couple of data asks.

**Sydney Arin Go:** I think these would be for Colin, because these are amplitude exports.

**Luke Stahl:** Yeah, probably.

**Sydney Arin Go:** Yeah, okay.

**Sydney Arin Go:** Well, then we can ask for that on the next column, I'll message in Slack as well.

**Sydney Arin Go:** Vic, I did create a form for the integration page submissions.

**Sydney Arin Go:** Amazing, amazing.

**Sydney Arin Go:** So this way, like I feel like that would lighten the load on you as well.

**Sydney Arin Go:** When somebody wants to send in a submission, you can just send them the form and then it will upload to our Airtable.

**Sydney Arin Go:** There is a separate Airtable for it so it doesn't clutter like our pipeline, but that'll just make it easier for all of us to track.

**Sydney Arin Go:** And then I can just add it into a regular Airtable for tracking.

**Vic Plummer:** Okay, that's perfect.

**Vic Plummer:** Thank you so much.

**Vic Plummer:** And I can like throw that, I can throw that in our docs around Marketplace of like marketing your app.

**Vic Plummer:** Let me just, sorry.

**Vic Plummer:** Oh, there we go.

**Vic Plummer:** I see.

**Sydney Arin Go:** I was just trying to find you in the doc.

**Sydney Arin Go:** So right now I have a set for anyone with the link can access the form.

**Sydney Arin Go:** If you want me to password protect it, let me know.

**Vic Plummer:** But I, like I don't.

**Vic Plummer:** I'm trying to bring it up now.

**Vic Plummer:** I don't see an issue unless.

**Sydney Arin Go:** You guys get spam.

**Sydney Arin Go:** Yeah.

**Vic Plummer:** Yeah.

**Vic Plummer:** So let me know if you guys get spam and then we can, if we need to, then we'll password protect it.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** Awesome.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** And then on the integration use case guide.

**Sydney Arin Go:** So I've marked this one as ready for publishing because this one was the first one that we did.

**Sydney Arin Go:** We are now on version five of this document, which has all the comments you left on the previous doc.

**Vic Plummer:** Okay.

**Vic Plummer:** So I'll review both and then give you a heads up.

**Sydney Arin Go:** The new one is about automating Trustpilot review displays on Webflow product pages. So these are the two we have for you for review this week.

**Sydney Arin Go:** And then we wanted to wait for Jason on the discussion.

**Jason Gong:** I'm here, by the way.

**Sydney Arin Go:** Oh, there you are.

**Vic Plummer:** Yeah, I'd love to know what your initial ideas were for that.

**Vic Plummer:** And then from our side, understanding what we can do to link them correctly or to make them discoverable.

**Jason Gong:** That makes sense. I guess my thought is we could give some suggestions.

**Jason Gong:** I do think the actual guides would probably make more sense on the dev side. The use cases will link to the guide and then the guide might link back to the integration page.

**Jason Gong:** At least that's how I was thinking about it.

**Jason Gong:** Did you guys give it much thought whether it's on the main Webflow site or the dev site?

**Vic Plummer:** No, I didn't. I only read the WeGlot one.

**Vic Plummer:** Do you think there would be a lot of code snippets in there?

**Jason Gong:** We're trying to avoid having too much code snippets and just point to the get started guide on their site or your actual documentation.

**Jason Gong:** So we don't have to update it.

**Vic Plummer:** I think what could be cool is having a section with suggestions. Is there a doc that shows suggestions built out already, with a natural progression of what you can do with this integration?

**Sydney Arin Go:** The list of integration use case guides that we're going to build.

**Vic Plummer:** Maybe we have something that links these as well, to make them a little more discoverable versus down here.

**Vic Plummer:** But that's my initial thought.

**Jason Gong:** That would be cool. For SEO, the experience of navigating is nicer on the dev site, but to capture organic traffic, it's probably still better on the main site. We'll give some thought.

**Vic Plummer:** Propose something.

**Vic Plummer:** Can you explain the navigation experience on the dev site?

**Jason Gong:** The dev site has search functionality. You can command K and type in something like "membership site" and it'll pop up, but I don't think that experience would be there on the Webflow site.

**Vic Plummer:** So if there was a search, that would be ideal.

**Jason Gong:** Yeah, that's a good question for how developers generally navigate. If they spend a lot of time on the dev site searching for things, it'd be nice to have it there.

**Vic Plummer:** Absolutely. The only thing I'm worried about is our search.

**Vic Plummer:** My dev doc site is already struggling to support the weight of our docs right now. So you probably don't want hundreds of docs dumped onto there. We publish from a repo as individual markdown docs. But I'm concerned about how that would work if it's coming from an external source.

**Vic Plummer:** So this is the Webflow site, but if you go to the second nav...

**Luke Stahl:** You need to go in the nav bar of the hub.

**Jason Gong:** Yeah, there you go.

**Vic Plummer:** Okay, got it.

**Vic Plummer:** Yeah, this is a different platform. This is not Webflow, but you do have search. I can ask our docs people what that could look like, especially if it's coming from an external source and not straight from our markdown docs. That's the open question for me because I'm worried about the stability.

**Jason Gong:** I guess you would have a section with a lot of entries. When we first pitched the idea, we were looking at how Firm handles it. Colin and I work there too, and they nest everything in their docs. It does get a little complicated.

**Vic Plummer:** It is a little hidden.

**Vic Plummer:** There is a search on the integrations hub. It has different card types. So if you type Weglot, you get results. If there were three integration pages about Weglot, could we tag them as "integration guide" or something?

**Jason Gong:** Yeah, mixing different entities might be confusing. Do you have any thoughts for keeping it on the main site? Would we create a new section for guides?

**Vivian Hoang:** It would have to be in a separate CMS collection. I don't know if search would work across multiple collections.

**Jason Gong:** Okay, maybe you could propose something.

**Jason Gong:** I'm going to look around to see how other people handle this. My first thought was putting it here, but nesting it into the existing structure would be clunky. Maybe it'd be a different tab, but if this is overloaded, we can take it offline. It sounded like Colin might have had an idea already.

**Vic Plummer:** Yeah, I'm sure he will share his ideas.

**Vic Plummer:** I'm happy to explore in real time. This conversation was helpful about where it could go. Maybe highlight use case guides a little more in the integration page?

**Jason Gong:** We've been calling them integration use case guides.

**Vic Plummer:** It's a bit long. So highlight use case guides more in the integration page, figure out how they show up in search if we choose to post them on the Webflow site. And on the guide itself, will it just copy the existing integration page structure?

**Jason Gong:** I was imagining the page would be a little bit more content-like. But I guess this isn't that different from the integration page itself.

**Vic Plummer:** Is there a TOC on the page?

**Jason Gong:** No.

**Vivian Hoang:** We're adding a TOC on the blog template between the hero and the main body.

**Vic Plummer:** The open question is how highlighted the integration page is for the link back.

**Jason Gong:** I feel like it would just be a breadcrumb type thing or maybe a floating sidebar on the right saying "this is the Stripe integration." Maybe we can throw some design together to visualize it.

**Jason Gong:** Yeah, we can go from there. But just a little context—is the delay just because of the sheer size of it?

**Vic Plummer:** Yeah, I actually have a conversation with him.

**Vic Plummer:** We originally had just the Designer APIs, then built out Webflow Cloud, browser APIs, code components, and so on. I need to ask what's really affecting us and how big we can make it. The docs are generated from a repo with a markdown file for every doc and a YAML file that determines the structure. It's gotten more complex—it used to take five minutes to create the site, now it takes about 20 minutes.

**Jason Gong:** So these are all the same instance of the searches across?

**Vic Plummer:** Yeah, each one is a different base path.

**Vic Plummer:** You've got data, designer, and so on. The search can go across all of these.

**Jason Gong:** So my initial suggestion would have been something like "integration guides," the same way you have code components. But if that still gets grouped together and bogs everything down, that's interesting. We'll just propose some options and see where it lives.

**Jason Gong:** So we're moving forward. Integrations seem good, SEO content we talked about. The last thing is code components—I apologize for how slow we're moving there, but we've been investing a lot into the guides. We do want to scope that project.

**Vic Plummer:** Anything else to flag?

**Luke Stahl:** I wanted to circle back on the SEO content.

**Luke Stahl:** I had chatted with Vivian about taking the five we have and staging them in production to see how they perform before we churn out more. We have two live and Vivian has three to publish. Let's see how those are performing and whether we want to continue. The focus should then move to code components and example apps.

**Jason Gong:** Okay, so we'll pause on this to see how things do and shift resources to code components. Thank you all for your time. Good catching up. Bye, guys.
