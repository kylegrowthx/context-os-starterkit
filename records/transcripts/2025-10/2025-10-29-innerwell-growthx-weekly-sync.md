# Innerwell <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-29
time: 15:30 UTC
duration: 19 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Akina Tran, Jakub Rudnik, Matthew Alves-Hill, Noa Cornberg
fathom_recording_id: 97690422
fathom_url: https://fathom.video/calls/455382624
share_url: https://fathom.video/share/kmu7ikHkp4NBoYq2vHuoV24By3EvkFcY
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX and Innerwell aligned on solutions for three critical blockers preventing ketamine content launches: broken redirects on state/city pages (Prismic-based fix being tested tomorrow), ~30 broken footer links requiring URL replacement, and establishing a new publishing workflow where GrowthX stages content in Prismic for Innerwell's Shanali to review and publish on low-traffic days. The team approved the "Therapy4" template for the ketamine content cluster (focusing on "ketamine first" positioning with condition/demographic/situation flexibility) and Innerwell will provide preferred research papers for content reference.

---

## Context

Innerwell is a telehealth provider specializing in ketamine therapy. GrowthX is delivering content marketing services to Innerwell, focusing on building out content clusters around ketamine therapy and related treatments. This is an active, ongoing engagement where the teams are aligned on content strategy and working through technical site infrastructure issues that are blocking content launches. The meeting focused on resolving redirect broken links, implementing a new publishing workflow to prevent site breaks, and establishing the content template and strategy for the ketamine therapy cluster.

---

## Relevance

**To GrowthX Delivery:**
- New publishing workflow: GrowthX stages content in Prismic, Innerwell's Shanali reviews and publishes to prevent site breaks. Requires coordination and Slack notifications to trigger QA on low-traffic days.
- Critical blocker: Broken redirects on ketamine state/city pages are preventing new content launches. Prismic-based solution being tested with external expert; testing starts tomorrow.
- Footer link fix is high-priority: ~30 dead links in footer pointing to old ketamine pages. Simple copy-paste replacement but visible impact on UX and SEO.
- "Therapy4" template for ketamine content cluster in review with Innerwell's medical team. Template approach allows "ketamine first" positioning with flexible targeting by condition, demographic, or situation.

**To CheckThat:**
- CheckThat prompts for home services verticals (General Contracting, HVAC) being audited as part of content strategy pivot mentioned in previous Marcel call.

**To GrowthX Business Development:**
- Strong account health signals: Weekly alignment meetings, proactive communication, medical team engaged in template review. Opportunity for expansion into other Innerwell therapy verticals beyond ketamine.
- Innerwell prioritizing content infrastructure (Looker dashboards now track purchases by content cohort). Suggests data-driven content expansion roadmap conversations.

---

## Overview

- **Redirects Blocked:** Broken redirects for ketamine state/city pages are blocking new content launches. GrowthX is testing a Prismic solution tomorrow; Innerwell will also investigate replicating a working blog redirect.
- **Critical Link Fix:** High-priority task to replace \~30 broken footer links to ketamine pages. This is a simple copy-paste fix to remove dead links from a high-visibility area.
- **New Publishing Workflow:** To prevent site breaks, GrowthX will stage content in Prismic for Innerwell's Shanali to review and publish. This centralizes QA and allows for batch publishing.
- **Content Strategy:** A new "Therapy4" template for the ketamine cluster is in review. Innerwell will also provide a list of preferred research papers for GrowthX to reference in articles.

---

## Key Topics

### Critical Site Issues

  - **Broken Redirects**
      - **Problem:** Ketamine state/city pages fail to redirect to new URLs, creating 404 errors.
      - **Impact:** New city pages are paused to prevent creating more 404s.
      - **Solution Paths:**
          - **GrowthX:** Testing a Prismic-based solution tomorrow with a Prismic expert.
          - **Innerwell:** Investigating replicating a working blog redirect process.
  - **Broken Footer Links**
      - **Problem:** \~30 footer links to ketamine pages point to old, dead URLs.
      - **Impact:** High-visibility broken links negatively affect user experience and SEO.
      - **Solution:** Replace old URLs with new ones. This is a simple copy-paste fix, not a redirect.

### Workflow & Reporting

  - **New Publishing Workflow**
      - **Problem:** Multiple teams publishing in Prismic without coordination risks breaking the live site.
      - **Solution:** GrowthX will stage content in Prismic → Innerwell's Shanali will review and publish.
      - **Rationale:** Centralizes QA and enables batch publishing on low-traffic days.
  - **Looker Dashboard Update**
      - **Enhancement:** The Looker dashboard now tracks purchases by content cohort (e.g., editorial, city level).
      - **Next Step:** Further segment city/state cohorts for more granular analysis.

### Content Strategy

  - **Ketamine "Therapy4" Template**
      - **Status:** A new template for the ketamine content cluster is in review.
      - [**Concept:** Pages will focus on "ketamine first" (e.g., "Ketamine Therapy for \[Condition\]"), allowing for flexible targeting by condition, demographic, or situation.](https://fathom.video/share/kmu7ikHkp4NBoYq2vHuoV24By3EvkFcY?tab=summary&timestamp=813.0)
  - **Preferred Research Papers**
      - **Request:** GrowthX asked for a list of Innerwell's preferred research papers to reference in articles.
      - **Rationale:** Ensures content aligns with internal standards and uses authoritative sources.

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Check blog redirect status; report to Akina
- Send blog redirect thread + spreadsheet to Akina
- Create Looker tickets: break out state/city/subsections; add blog cohort
- Break out and track state/city/index dependencies

**Akina Tran (Innerwell)**
- Replicate blog redirect approach for ketamine state/city pages
- Compile and share preferred research paper list w/ Matt
- Replace broken footer links w/ correct ketamine state/city URLs
- Update site index page to use new template

**Matthew Alves-Hill (GrowthX)**
- Fix 'Written by'/'Reviewed by' fields on recent blog posts
- Implement Slack staging notifications; coordinate w/ Shanali for QA/publish

**Noa Cornberg (Innerwell)**
- Establish new publishing workflow: coordinate with Matthew to have GrowthX stage content in Prismic for Shanali to review and publish on low-traffic days

---

## Transcript
**Akina Tran:** Hello.

**Jakub Rudnik:** Hey Akina.

**Noa Cornberg:** Hello.

**Jakub Rudnik:** Noah, hello.

**Noa Cornberg:** I'm here, I'm here.

**Matthew Alves-Hill:** Hello.

**Akina Tran:** How's it going?

**Matthew Alves-Hill:** Good, how was your time off?

**Akina Tran:** It was good.

**Akina Tran:** I lost my voice, so I sound like a chain smoker right now.

**Noa Cornberg:** It's because you're in Amsterdam right now and you smoke weed all day, that's why.

**Akina Tran:** Secondhand smoke.

**Matthew Alves-Hill:** I'll get you.

**Akina Tran:** Okay, let's go through it. I think there's a lot we can catch up on. One, I saw the redirects you mentioned, Jakub.

**Akina Tran:** It looks like they're not doing a proper redirect right now.

**Jakub Rudnik:** Yes.

**Akina Tran:** For both — the blog and the mental health pages or just one of them?

**Jakub Rudnik:** The ketamine pages, state and city. Both old states and new states have their own issues, but neither are set up with redirects. For cities, it's the same issue, but we paused those so we don't create a bunch of 404s in the meantime. We need that redirect process first so we don't kill pages with organic traffic without showing Google where they go. I'd assume blogs are the same issue — I actually haven't looked into those yet. This was focused on city and state level stuff.

**Akina Tran:** Okay.

**Akina Tran:** Can you check that one and see?

**Akina Tran:** If that one has an issue, too, because we were redirecting the old reflections blog posts.

**Jakub Rudnik:** Yeah, yeah, yeah.

**Jakub Rudnik:** Yes, we'll do that.

**Jakub Rudnik:** I can probably do that while we're chatting.

**Akina Tran:** Okay, cool.

**Jakub Rudnik:** I don't know if anyone on your side has looked at this yet. Matt, I might need you to help translate some of the technical details. We have someone on our end with Prismic experience who believes he's found the solution. He's taken the documentation I sent from various forums and built a test repository. This is where I'll get lost in the technicals, but he's going to test it tomorrow external to your site, so it's not touching anything live right now. If it works, we should be able to bring that into Innerwell's backend and set up the redirects. If you've been working on this simultaneously, we can merge approaches or pause, but we think we have a solution we can start testing tomorrow.

**Jakub Rudnik:** Matt, is that all correct?

**Matthew Alves-Hill:** Yeah, that's right. He's an expert in Prismic, which can be a little funky as a CMS/TMS, but he's very positive that he can figure this out. Like Jakub said, he's setting up a separate space to test that it's working. We'll have a demo tomorrow and share more on what we think we can do. We'll also translate some of his work for you.

**Akina Tran:** Um, we sent it to our dev team, but they only just started looking at it yesterday.

**Akina Tran:** So if you guys have something together tomorrow, it'll probably be faster anyway.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** We've tasked him with, like, any asks that he, right now he's deep in figuring out exactly how he's going to do it, and then we'll translate, like, any asks or support that he might need, and maybe we need to connect him with your team to get things through.

**Matthew Alves-Hill:** But, yeah, it's a little bit above my head, the inner workings of Prismic, but, yeah.

**Akina Tran:** Yeah, feel free to connect us directly if that's faster.

**Matthew Alves-Hill:** Cool.

**Jakub Rudnik:** One thing to note — the blog redirects that were set up are all working properly. I'd have to dig into why those work but the others don't. I'll send over the thread and spreadsheet. I've only spot-checked, but all that's working properly, so I don't know what the difference is, but it can be done.

**Akina Tran:** Okay, yeah, it can be done, but clearly they didn't do it, so I'll just have them replicate what they did for the blog post.

**Jakub Rudnik:** Cool, okay.

**Akina Tran:** Okay, what's next?

**Matthew Alves-Hill:** Akina, I saw Shanali's note about the "Written by" and "Reviewed by" fields. Israel, who's working on the Prismic side, will be publishing going forward. It was a bit of a translation issue when we swapped over to publishers, but he'll rectify that today and knows the proper process going forward.

**Noa Cornberg:** I have questions about the workflow. Right now you send things for development on your end, and I need to know when you're pushing things. Sometimes when we push things, we can break things. I want you to ping me on Slack whenever you push, so I can ask the team to do fast QA and make sure nothing breaks. There are a lot of people at Innerwell using Prismic, so I want to start tracking all of this. Another option is you set up everything and I ask Shanali to push it live. That way we can batch all our website development into one day — like Wednesday or another low-traffic day — so everything is more coordinated.

**Matthew Alves-Hill:** Yeah, in terms of publishing the blog, either way works for us. We have a new publisher on our end and he knows the ins and outs, so it shouldn't be an issue. The articles all went up live fine — it was just the allocation of the "Written by" and "Reviewed by" fields. So we're happy to continue publishing.

**Noa Cornberg:** You're doing a great job. I'm establishing this new policy because there are so many people touching the website, and it's our growth engine — our funnel. I think the best approach is your team sets up everything and Shanali pushes it live so she can QA everything.

**Matthew Alves-Hill:** Got it, that's completely fine. We can easily set up a notification process to let you know when blog articles have been staged. Typically as soon as Akina approves them, we schedule for publishing, so it aligns with your process. We'll start working that way.

**Akina Tran:** Okay, sounds good.

**Noa Cornberg:** And thank you.

**Jakub Rudnik:** Sorry, added an extra screen and now I'm figuring out where to put it.

**Noa Cornberg:** By the way, Jakub, I can see that your house is starting to evolve. There's lines, there's a picture. Maybe next call you'll surprise us.

**Jakub Rudnik:** You should see underneath me — it's chaos, and I can't work like this. But when I have 20 minutes between calls, I try to set up a light or figure out a better setup. It's a work in progress.

**Noa Cornberg:** I think we're all with you on that. It's looking better.

**Jakub Rudnik:** Let me show you the Looker dashboard update. Under the conversion events tab, you can filter to purchase only, and the new piece is we can now look at it by cohorts. We've added cohorts so you can see what we've done specifically. In the last two weeks, we've had a ton of purchases — I'm not sure if something changed on the tracking end or if one or two of our pages have taken off, but we're starting to see conversions. We can now track to any page we've created. One thing we should do at some point is break out state and city level to make the analysis more granular, even though that's lower priority right now.

**Akina Tran:** We should also add a blog section for the Reflections page.

**Jakub Rudnik:** Reflections exists, but I think it only shows data if there are actual purchases coming from the blog. We're not seeing those yet. This dashboard does take a bit longer to load than some others, but if you filter by first visit, it's faster. We have editorial, city, and state cohorts now. I'll put in a ticket to break those out even further with other subsections, so don't worry about it on your end.

**Akina Tran:** Yeah, okay.

**Akina Tran:** Thank you, that looks better.

**Jakub Rudnik:** Yeah, Matt, I don't know where you want to jump to next on the agenda.

**Matthew Alves-Hill:** I shared a question in the chat earlier. When we're writing articles and referencing specific research papers, do you have an internal repository of preferred research papers that Innerwell would prefer blogs to reference? We're using our judgment right now, but if you have papers that are preferred or used elsewhere in the company, we could incorporate those into our workflow and prioritize referencing them.

**Akina Tran:** Got it.

**Akina Tran:** I don't have one off the top of my head, but let me poke around and see if I can get something for you.

**Matthew Alves-Hill:** We also chatted about the Therapy4 template as we build out the Ketamine cluster. Akina, I put one in review for this week. The idea is pretty cool — instead of going "condition first," we're going "ketamine first," and then we'll vary the condition around that. So we'll have conditions, but also demographic or situation-based variations. This informs our keyword plan for these pages, which I've shared with you. The template is done and ready for your medical team review. Once approved, we can ramp up these pages by defining conditions and how ketamine therapy works for each. The output is really good, and our ketamine cluster roadmap is looking solid.

**Akina Tran:** I have that out with our medical team to review. I'll let you know when it's approved.

**Matthew Alves-Hill:** Okay, amazing.

**Matthew Alves-Hill:** That's all I really had on my end.

**Matthew Alves-Hill:** Jakub, is there anything else that you wanted to raise?

**Jakub Rudnik:** Yes. The redirects are a big thing — we need to fix a bunch of stuff once we have that solution in place. But pending that, I just saw that our ketamine therapy URLs point to old pages that are all dead right now with application errors. Do you know if we have access to change these?

**Akina Tran:** Let me flag that to the team and see what's going on. Those are supposed to redirect to localized pages.

**Jakub Rudnik:** Right. We have those URLs set up, but those redirects are broken in a different way than the new ones. Either way, we can replace them with the new URLs — they don't need to be redirected. This one worries me more than the other issues because they're in the footer. All the correct URLs are right here and working. It's just a copy-paste for 30 links or so. I'd prioritize this because of how visible footer links are. I tagged you in the technical recommendations doc.

I'm also curious if we've made progress on things like the mental health high-level page, index pages, or state-level pages on your side.

**Akina Tran:** The breadcrumbs and links to cities are being worked on this week. For the index page, since you have someone who created the template that works tomorrow, we'll use that moving forward. We'll also update the site with the new URLs today.

**Jakub Rudnik:** Cool. I'll break these out so we have better tracking. These are the big pieces on my end. Just keep us posted when those come through and we'll check them off. Some of these have dependencies, so we want to keep everything moving as they cross the finish line on your side.

**Akina Tran:** We want to wrap this up in about a week.

**Jakub Rudnik:** Yeah, for sure. There will probably be additional things on top of these, but these are the priorities — the ones that are blocking everything. These will have the biggest impact and then we can move forward from there.

**Akina Tran:** Sounds good. Thank you all.

**Jakub Rudnik:** Thank you. Talk soon.
