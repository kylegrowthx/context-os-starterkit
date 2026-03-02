# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-20
time: 17:31 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien (GrowthX), Aida Knezevic (GrowthX), Reet Mand, Alexis Ruiz-Pedregon, Bekah Reddis, Fung-Lin Wu, Andy Varshneya, Allison Gregory, Cody Henshaw, Megan Boone
fathom_recording_id: 103219788
fathom_url: https://fathom.video/calls/480042610
share_url: https://fathom.video/share/-ZVAKsrrWjUX76qKMp_v6jZcWCzshS3Q
source: fathom
enriched_on: 2025-11-20 18:45 UTC
</metadata>

---

## Summary

Review content audit findings and align on a refresh strategy.

---

## Context

Redis is a data platform company and a strategic client of GrowthX, engaging on SEO and content strategy. The purpose of this meeting was to review content audit findings (blog and glossary) and align on next steps for content refresh, pruning, and optimization for both Google search and AI visibility. GrowthX had delivered comprehensive audits using Google Search Console and GA4 data, identifying outdated content from 2013-2014 that was dragging down site authority and preventing newer content from ranking effectively.

---

## Relevance

- **To GrowthX Delivery:** Defined a structured content auditing and refresh workflow combining metric-driven prioritization (traffic loss, engagement rates, publish date) with manual review of expert-authored content. Introduced LLM visibility optimization tactics (clear H2s, immediate answers, TLDRs, FAQ schema) as standard refresh criteria. Established content OS integration (Airtable) for tracking refresh priorities and automating content review triggers (e.g., >9 months old).

- **To GrowthX Business Development:** Strong client engagement and active feedback loop on calibration content (voice and tone test for "What is an AI agent?"). Redis team approved methodology and is iterating on execution. Demonstrates GrowthX's ability to solve for both SEO and AI visibility simultaneously, a differentiator as LLMs become primary content consumers.

- **To CheckThat:** Redis blog is a real-world test case for AI visibility strategies. Team discussed how LLMs prefer recent content (6-8 months old) and specific structural elements (FAQs, TLDRs, comprehensiveness). Practical validation of CheckThat's focus on content discoverability across both search engines and generative AI.

---

## Overview

- **Prune the Blog:** Delete/redirect \~10-year-old, low-performing content to improve overall site authority and help new content rank.
- **Refresh Strategically:** Prioritize refreshing recent (post-2021) articles with high traffic loss or bottom-of-funnel intent. Preserve expert-authored content by adding comprehensiveness, not replacing it.
- **Adapt for LLMs:** Structure all content for AI visibility by using clear H2s, immediate answers, TLDRs, and FAQ schema.
- **Review Calibration:** The "What is an AI agent?" refresh is ready for review to validate the new, more conversational voice and tone.

---

## Key Topics

### Content Audit Findings

  - GrowthX delivered blog and glossary audits using GSC & GA4 data (engagement, bounce rate, publish date).
  - **Primary Issue:** The blog contains content from 2013-2014.
      - **Rationale:** This outdated, low-performing content signals irrelevance to Google, hindering new content from ranking.
  - **Audit Priorities:**
      - **P1 (Delete/Redirect):** Old, low-performing URLs.
      - **P2 (Refresh/Redirect):** Old (pre-2021), low-performing articles.
      - **P3 (Refresh):** Recent (post-2021) articles needing updates.
      - **P4 (Monitor):** High-performing or new content.

### Content Strategy & Workflow

  - **Pruning Process:** GrowthX will manually review the P1 list to ensure no valuable, expert-authored content is removed.
      - **Rationale:** Preserves topical authority, a key ranking factor.
  - **Refresh Process:**
      - Prioritize articles with high traffic loss or bottom-of-funnel intent.
      - Integrate refresh tasks into the Airtable content OS.
  - **Future Workflow:** Automate content review triggers based on age (e.g., \>9 months) or performance thresholds.

### Authority & LLM Visibility

  - **Maintaining Authority:**
      - **Problem:** New content may lack the authority of pieces written by Redis technical experts.
      - **Solution:** Use Redis technical marketers as bylined authors for GrowthX-written content, a practice already in use.
  - **Optimizing for LLMs:**
      - **Rationale:** LLMs prefer recent content (6-8 months old).
      - **Tactics:**
          - Structure with clear H2s and immediate answers.
          - Add TLDRs/key takeaways.
          - Implement FAQ schema.
          - Ensure server-side rendering (already in place).

### Calibration Blog Review

  - GrowthX refreshed the "What is an AI agent?" blog post to demonstrate the new voice and tone.
  - **Feedback:** The draft is more conversational and less "AI-sounding" than previous examples.
  - **Process Clarification:**
      - Feedback on writing guidelines is implemented manually by a human editor.
      - The AI generation pipeline uses a multi-step process: draft → validate against guidelines → fix non-compliant paragraphs.

---

## Action Items

**Aida Knezevic**
- Integrate audit refresh priorities into Redis Airtable content OS
- Record and share article generation platform walkthrough w/ Redis team
- Double-check blog/glossary pruning lists; label keepers; share final lists w/ Redis

**Allison Gregory**
- Review 'What is an AI agent' calibration blog; send feedback to Aida

---

## Transcript
**Erik O'Brien:** This meeting is being recorded.

**Erik O'Brien:** Got a deep dive with Nivon right after this, so don't mind me if I'm a little distracted.

**Aida Knezevic:** Okay, no worries.

**Aida Knezevic:** Hi.

**Alexis Ruiz:** How are you all?

**Aida Knezevic:** I'm good.

**Alexis Ruiz:** How are you?

**Alexis Ruiz:** All good.

**Alexis Ruiz:** We're just coming off a big market in QBR, so I'm sure everyone else will join in a bit.

**Aida Knezevic:** Sure.

**Bekah Reddis:** Hello.

**Aida Knezevic:** Hi.

**Cody Henshaw:** Hello, everyone.

**Fung-Lin Wu:** Sorry, I'm here.

**Aida Knezevic:** Hi, how are you?

**Fung-Lin Wu:** Good, how are you?

**Aida Knezevic:** Great.

**Aida Knezevic:** All right, I think we have everybody, right?

**Aida Knezevic:** I don't think anybody else is supposed to join.

**Aida Knezevic:** All right, perfect.

**Aida Knezevic:** Well, thank you for joining today.

**Aida Knezevic:** So we have a couple of updates that we wanted to run by you.

**Aida Knezevic:** So last week when we met, we were discussing the content audit, among other things, specifically the glossary and the blog.

**Aida Knezevic:** And those audits are ready for you to take a look at.

**Aida Knezevic:** So we've provided the links in the agenda.

**Aida Knezevic:** But if you also go to our notion base, and you can just find a document that says audits, and those links should be in there as well.

**Aida Knezevic:** So I can show you.

**Aida Knezevic:** They're very similar.

**Aida Knezevic:** The approach is identical.

**Aida Knezevic:** So what we did was we pulled data from your Google Search Console and GA4 just to have more data around engagement and bounce rate.

**Aida Knezevic:** And then we applied some formulas to understand, okay, like what is, you know, the overall performance of all of these articles.

**Aida Knezevic:** And we also took into account when they were published.

**Aida Knezevic:** So as we were looking through the blog, we noticed that you have content on your website that goes back all the way to 2013, 2014, which is probably very outdated and something that we do recommend pruning from your website.

**Aida Knezevic:** We did provide, so there are different tabs in each audit.

**Aida Knezevic:** So this tab includes a list of URLs that we recommend deleting and redirecting. It's important to note that this is up for you to decide whether you think it's worth deleting. When it comes to some announcements, you might want to keep them on your website, depending on how important they are.

**Aida Knezevic:** Then there are, in P2, we have a list of old articles that aren't performing well.

**Aida Knezevic:** By old articles, we mean articles that were published before 2021.

**Aida Knezevic:** And these articles, we can either refresh them or just set up a redirect to the blog or another article that we want to send traffic to.

**Aida Knezevic:** You can see, you know, we provided like a reason for action.

**Aida Knezevic:** But you can also see the overall click change in the past six months, the impressions change, as well as, you know, how the percentage change for engaged sessions.

**Aida Knezevic:** Do you...

**Aida Knezevic:** I'm happy to explain what Engage Sessions means if anybody doesn't know.

**Fung-Lin Wu:** We're using like J4, right?

**Aida Knezevic:** Yeah, Okay, yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, and then P2 is content that is relatively recent that we recommend updating.

**Aida Knezevic:** Again, this is content that was published after 2021.

**Aida Knezevic:** We, you know, provided some reasons here for why we recommend refreshing these.

**Aida Knezevic:** And then P3 and P4 are those that we want to monitor.

**Aida Knezevic:** So they're either performing well or they are, it's new content that you published that, you know, we should wait to see how it performs in the coming period.

**Aida Knezevic:** And then in the glossary, it's quite similar. So we have reasons and actions, and then it's divided into different priorities.

**Aida Knezevic:** So the first one is to refresh or update content.

**Aida Knezevic:** And then there is some content here in the glossary.

**Aida Knezevic:** This is very, like, just a couple of URLs that is declining more slowly.

**Aida Knezevic:** But we might, you know, see a traffic spike in the next couple of months, depending on any Google core updates or anything like that.

**Aida Knezevic:** Any questions, feedback, we're happy to kind of adjust the report, depending on what you're looking for.

**Reet Mand:** You know, what is, what's your TLDR here?

**Reet Mand:** Like, what's the takeaway?

**Aida Knezevic:** So the takeaway is for the glossary and the blog, we want to, so specifically for the blog, I think the biggest takeaway is pruning content.

**Aida Knezevic:** So you do have a lot of content on the blog, some that's over 10 years old, and that does impact and weighs down the website.

**Aida Knezevic:** This isn't like a confirmed ranking factor, but there are a lot of people also at GrowthX and just people who have been in SEO for a while who have observed that websites that have a lot of content, and when a lot of that content isn't performing that well, it sends a signal to Google that a lot of the content is irrelevant or unhelpful.

**Aida Knezevic:** And that kind of makes it also harder for new content to rank.

**Aida Knezevic:** So by pruning old content or content that isn't performing, we can kind of boost the performance of the overall blog and the glossary.

**Aida Knezevic:** So that would be kind of my big takeaway is to identify what we want to delete, what we want to redirect.

**Aida Knezevic:** that's a great perspective.

**Aida Knezevic:** Particularly from this list.

**Aida Knezevic:** And then the same goes for the glossary.

**Aida Knezevic:** When it comes to refreshing content, that's something that we can help with.

**Aida Knezevic:** So as we're creating new content every week, we can also pick one or two articles that we want to refresh.

**Aida Knezevic:** A refresh can sometimes mean a full rewrite, depending on the state of the existing content.

**Aida Knezevic:** Perhaps it's like very outdated or it's like super short and we can expand it.

**Aida Knezevic:** But those would be like my two big takeaways here.

**Reet Mand:** Gotcha.

**Reet Mand:** Do you recommend a process for us to ensure like all this new content we're going to create, it's going to get stale at some point?

**Reet Mand:** So we're not like we're constantly refreshing or constantly, you know, unpublishing?

**Aida Knezevic:** Yeah, that's a great question. I think as we're publishing new content, it helps to do a mini audit like this at least once every six months to understand what content is doing particularly well.

**Aida Knezevic:** And then we can also identify blog posts that never really quite took off.

**Aida Knezevic:** There's always going to be content that ranks well, like it might rank on page three or four.

**Aida Knezevic:** And that's the type of content that we can consider refreshing to kind of push it forward.

**Aida Knezevic:** But the content that's, you know, never performed that well is something that we might consider removing.

**Aida Knezevic:** However, we want to, it's more concerning when I see websites that have a lot of content and a lot of that content is actually irrelevant to their main product and what their, you know, what their audience cares about.

**Aida Knezevic:** So in that case, that's when you have to do like a little bit more pruning, but I would recommend like an audit every six months.

**Reet Mand:** Understand what's performing and what needs to be refreshed.

**Reet Mand:** I'm just thinking, like, I think you could put in some automation in place, like, you know, any, any, like, views or whatever the metric is that is below that threshold, like, highlight that, you know?

**Aida Knezevic:** Yeah, yeah, certainly.

**Aida Knezevic:** And I think also we can do that even with the published dates.

**Aida Knezevic:** Um, anything that's older than maybe nine months can trigger a review, um, and, and kind of make sure that we refresh it.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Cody Henshaw:** And we're actually building, like, a refresh workflow into the other assets that we're doing right now with Laura.

**Cody Henshaw:** So maybe we can put that into that workflow, like, it's slightly different, but, like, that's for all the resource hub stuff.

**Cody Henshaw:** Um, maybe it should be evaluated like this also, um, but they basically just kind of put an arbitrary, like, re-evaluate every year.

**Cody Henshaw:** But I like it being driven by.

**Cody Henshaw:** Okay.

**Cody Henshaw:** Like, more as needed if something's flagged like this.

**Reet Mand:** Yeah.

**Reet Mand:** But we can track it there in that same place.

**Reet Mand:** Yeah.

**Fung-Lin Wu:** I think, Fung-Lin, you were going to say something, were you?

**Fung-Lin Wu:** No, I was going to say it makes sense.

**Fung-Lin Wu:** Like, because we're about to do it annually, so we just add that in.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** But, you know, like, I've also worked at companies where every year they just update all their blog in the back end to look like it's a brand new one.

**Fung-Lin Wu:** Like, they literally just change the year from 2025 to 2026, and then that's how they kind of took Google.

**Fung-Lin Wu:** I don't know if, I mean, obviously, that's, like, the easier way, because if we can't guarantee a certain amount of content production on a regular basis, like, that would be, like, the next easy way.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah, that's one way of doing it.

**Reet Mand:** Yeah.

**Reet Mand:** Sorry?

**Reet Mand:** Yeah, I was going to say that, you know, the authority, right?

**Reet Mand:** It matters as well on some of these blogs.

**Reet Mand:** If you have a, like a dev person, their name is on that blog, like that has more value than somebody that doesn't have any, there's no, you know, writers on it.

**Reet Mand:** How are you thinking about that as you're thinking about refreshing these, this content?

**Aida Knezevic:** Um, that's a good question.

**Aida Knezevic:** We actually had a similar situation recently where we're going through a blog for a different client and deciding what we want to refresh and what we want to remove from the blog.

**Aida Knezevic:** Um, and if the content was written, especially we had developers who had published on their blog, um, and it was very tutorial based or just very expert, like it was clearly written by an expert, that type of content, um, we are hesitant to remove precisely because it adds to the overall topical authority of the website.

**Aida Knezevic:** So we can slightly refresh it by adding additional content. It depends on the topic, but we might provide additional content while preserving the original blog post and adding new sections to make the information more comprehensive.

**Aida Knezevic:** But it really depends, like this is, we never really, when we recommend pruning, we would always go into each blog post and kind of double check and confirm, okay, is this blog post like truly like supposed to be removed or is it something that has value even though it's not getting a lot of clicks from Google search.

**Reet Mand:** But I think those are the ones like where there is some authority, right?

**Reet Mand:** Like that's what AI is, is prioritizing more even if it is older, but if it has authority, it, it pulls from that.

**Aida Knezevic:** Yes, exactly. That's exactly why we don't recommend removing blog posts that were written by developers or any subject matter experts that are really well-written and in-depth pieces of content.

**Reet Mand:** So the ones that you've highlighted here, you have already removed all of that.

**Reet Mand:** So these were more of a lack of a better word, general generic blogs.

**Aida Knezevic:** So these are the ones that we have selected purely based on metrics.

**Aida Knezevic:** So the next step would be to go through and kind of double-check and make sure that the blogs fit that criteria.

**Reet Mand:** Gotcha.

**Aida Knezevic:** Yeah.

**Alexis Ruiz:** So in terms of, like, prioritizing these, like, for the refresh, update content, how do you suggest we do that?

**Alexis Ruiz:** Or should we go in and check off which ones that we'd like to prioritize refreshes first?

**Alexis Ruiz:** Or how would that work?

**Aida Knezevic:** Um, we...

**Aida Knezevic:** would take a look at, there are a couple of things that we want to look at, obviously, like how much traffic it's lost in the past six months, anything that had a huge amount of, like a huge traffic loss, we would want to prioritize, but we also take into account whether it's like more of a bottom of the funnel piece versus top of the funnel.

**Aida Knezevic:** So if it's something that's more closely related to your product and it's bringing in a highly specific audience, we would want to prioritize that, but we want to pull in, so once we start incorporating this content into production, we're actually going to pull in this into your content OS in your table, so it's all going to be here.

**Aida Knezevic:** So we're going to label, like, these are our refresh priorities, like, for the next two months.

**Alexis Ruiz:** Got it, okay, that makes sense, I was going to ask how it related to the air table.

**Alexis Ruiz:** Yeah, yeah.

**Reet Mand:** Yeah, we definitely want to merge.

**Reet Mand:** Cody, um...

**Reet Mand:** Cody, does it, I don't know how to, okay, my, my, I'm going to tell you what's, what's kind of my concern is, and then you'll tell, you'll tell me, like, how do we go about answering that.

**Reet Mand:** My concern is that we're going to generate a lot of content that's going to be fresh, but, or it's going to be refreshed, but may not have that authority to it, right?

**Reet Mand:** So when it's written from, like, a, somebody who's technical, because it is technical audience, it, it has, they have that domain authority, it ranks better.

**Reet Mand:** So I don't, I, there's two pieces to when the content ranks better, right?

**Reet Mand:** One is how fresh it is, how relevant, and then also there's, like, what is the authority of the person who's writing it?

**Reet Mand:** So I think we, I believe, correct me if I'm wrong, but I believe that.

**Reet Mand:** We are solving for the freshness of the equation.

**Reet Mand:** How are we thinking, especially when we are creating new content or refreshing, like high-performing content, how are we thinking about that we get that authority on it?

**Reet Mand:** I don't know if it makes sense.

**Reet Mand:** Go ahead, Fung-Lin.

**Fung-Lin Wu:** No, no, go ahead.

**Reet Mand:** That's just something I'm just not checking out in my head.

**Reet Mand:** So I just wanted to say it out loud.

**Fung-Lin Wu:** Wouldn't we assign right authors to it?

**Aida Knezevic:** Yes, so that depends.

**Fung-Lin Wu:** So sometimes companies will publish under specific names on the blog, which is something that is recommended for good SEO.

**Cody Henshaw:** I was going to say, our technical marketers could give sign-off to each one of them and then you just, you know, give them the byline.

**Fung-Lin Wu:** That's how we do it today.

**Fung-Lin Wu:** Like, today, these, like, authority, they're not really, yeah, these authorities, some of them aren't.

**Fung-Lin Wu:** We've been actually writing it today.

**Fung-Lin Wu:** It's actually like our technical, like Nick Moore is writing it, and we just have John Noonan be the quote-unquote author of it.

**Fung-Lin Wu:** Like essentially we have ghostwriters.

**Fung-Lin Wu:** So I'm imagining growthx would be the ghostwriter, and we would just assign people, the person who reviewed it, to be the author.

**Aida Knezevic:** Yeah, yeah, Okay.

**Aida Knezevic:** And to your point, Rege, so yes, there's the freshness, there's the authority, but there's also a third aspect, which is comprehensiveness.

**Aida Knezevic:** And sometimes articles, they are written by an expert, and they are super insightful, but they might not be as comprehensive as the top-ranking content.

**Aida Knezevic:** So that's where we would kind of like, if we were to refresh an older blog post that was written by a domain expert, we wouldn't be like removing sections or like cutting out the very valuable information that they provided.

**Aida Knezevic:** We would just be adding like new information to make the blog post more comprehensive, but their original insight would still be there. So that's one way we approach it.

**Reet Mand:** Gotcha.

**Reet Mand:** One more question.

**Reet Mand:** Thank you.

**Reet Mand:** I think that that's very helpful, Fung-Lin, like, and, you know, Cody, I think that authority on this.

**Reet Mand:** The other question I have is around, how are you thinking about how chat GPTs, how they are, you know, pulling content from our websites to answer that, like, nobody, I know, I understand that, like, nobody has it, the answers yet, because it hasn't been, people are still trying to figure it out.

**Reet Mand:** But how are you thinking about that, what we refresh is easy to pull for the chat GPTs?

**Aida Knezevic:** So, one of the reasons that we do recommend refreshes...

**Aida Knezevic:** Is that there have been a couple of studies, and I'm sure you've already heard about this, that LLMs do prefer more recent content, so between six to eight months old.

**Aida Knezevic:** There are also some technical elements that are a part of LLM visibility.

**Aida Knezevic:** Erik has some experience in that regard because he's been helping our other clients with their AI visibility.

**Aida Knezevic:** Erik, I know that there's something about JavaScript that I'm not that well-versed in, but maybe you could speak to that.

**Erik O'Brien:** Yeah, that one's more specific to just how the content is rendered, whether client-side or server-side.

**Erik O'Brien:** So probably not applicable here, as I assume Redis has server-side rendering set up for their blog.

**Cody Henshaw:** Yeah, we server-render JavaScript.

**Cody Henshaw:** mean, yeah, we're next site with server-rendering.

**Erik O'Brien:** Yeah, yeah.

**Erik O'Brien:** So I don't think that would be an issue.

**Erik O'Brien:** I think a lot of what we're finding through third-party and first-party research is the overall structure of the content.

**Erik O'Brien:** So are we leading with questions in H2s?

**Erik O'Brien:** Are we answering the question immediately right after that H2?

**Erik O'Brien:** Do we have FAQ schema set up on the site?

**Erik O'Brien:** And so some of those are kind of things that we can make into the content itself or the blog posts.

**Erik O'Brien:** Some of it's like, can we add a TLDR or key takeaways at the top?

**Erik O'Brien:** Some of those are really well-cited for kind of LLL visibility.

**Erik O'Brien:** And so I think as we look at refreshes, it's more about kind of what makes sense for that specific piece.

**Erik O'Brien:** Like, does it make sense to add those key takeaways at the top?

**Erik O'Brien:** And if it is a more complex topic or a very long post, is there a way to kind of incorporate FAQs to kind of boost visibility there?

**Erik O'Brien:** But as Aida mentioned, comprehensiveness is one of the core pieces of LLM visibility and rankings for citations.

**Erik O'Brien:** And then just overall site structure and schema, which it sounds like I would assume Redis is pretty modern and set up well for that.

**Erik O'Brien:** So happy to kind of put more thoughts together.

**Erik O'Brien:** As Aida mentioned, I'm doing this across multiple clients right now of just what are the best practices that we can look to for both blog content and just overall site structure.

**Erik O'Brien:** So happy to share some of those kind of high-level insights as we dig a little bit deeper.

**Reet Mand:** Yeah, I mean, because we're going to like refresh the content anyways, right?

**Reet Mand:** Like might as well refresh for both Google and for LLMs.

**Aida Knezevic:** Yeah, yeah, exactly.

**Aida Knezevic:** All right, and then the other update that I had for you is that we were working on a calibration.

**Aida Knezevic:** yeah, yeah,

**Aida Knezevic:** So we decided to go with an existing blog on your website that was published last year in February, and the topic is what is an AI agent, and it's a pretty, like, in the grand scheme of things, like, from the blog post that we might see for this topic, it's pretty brief, and we decided to, like, go ahead and refresh it.

**Aida Knezevic:** Just to see, you know, just to be able to show you what the voice and tone is from our article generation pipeline, and, you know, just so you can evaluate kind of from that point of view.

**Aida Knezevic:** So you can find it in this Google Doc.

**Aida Knezevic:** I provided it in the, I provided a link to it in the agenda.

**Aida Knezevic:** But, yeah, so we did preserve a lot of the things from the original blog post, particularly, for example, like, the first person point of view.

**Aida Knezevic:** But we also expanded it with additional sections.

**Aida Knezevic:** We also added a Frequently Asked Questions section at the bottom for LLM visibility.

**Aida Knezevic:** And the goal here would be for your team to review not just for the voice and tone and the writing style, but also just on the information that's presented, how comprehensive it is, and just to make sure that it's meeting your quality bar.

**Aida Knezevic:** Can, is there anything?

**Fung-Lin Wu:** don't know if this is helpful for you to review, like, in terms of tone of voice.

**Allison Gregory:** Yeah, yeah, we'll definitely take a look.

**Fung-Lin Wu:** I feel like the last two days were just piling on to your work.

**Fung-Lin Wu:** I know, sorry.

**Reet Mand:** Can we use that AI, the agent that was previewed in the.

**Fung-Lin Wu:** Oh, the Atom?

**Reet Mand:** Yeah.

**Allison Gregory:** Yeah, I mean, it would just give a different version of what's here, so I don't know that it would critique the inputs here.

**Allison Gregory:** But at first glance, this looks good.

**Allison Gregory:** I think my, just to talk about it as a group, my feedback on the voice in general was that the rules were right, but the output felt very AI, which I realize it is AI, but we don't want it to sound that way.

**Allison Gregory:** So I think at first glance, this looks much more conversational than what was in the guidelines.

**Allison Gregory:** I think my main question was just, because some of the revisions in the guidelines felt like they were, I don't know if it was output or if it was a person making edits based on the comments I was leaving.

**Allison Gregory:** So I just wanted to make sure that we've got the right inputs, but we'll take a look at this and that'll probably help answer that question too.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** I think with the writing guidelines, we update them.

**Aida Knezevic:** Pretty heavily, especially in the first couple of weeks once we start generating content.

**Aida Knezevic:** You know, sometimes AI will listen to some instructions more than others.

**Aida Knezevic:** We do have multiple steps in the article generation process. So when it drafts, I'll give you a walkthrough next week.

**Aida Knezevic:** Actually, maybe not next week since you all will be out, but I can record a walkthrough of our article generation platform and the process, and I can walk you through it step by step.

**Aida Knezevic:** So the writing guidelines are applied when the article is being drafted, and then once we have the draft, there's a step that validates the writing guidelines and the proofreading checklist.

**Aida Knezevic:** So it basically uses the draft, and then it grades the draft against the writing guidelines, and then it finds paragraphs where the AI did not follow the writing guidelines or the proofreader, and then it's going to go back in and fix it.

**Aida Knezevic:** So we do apply them in multiple steps.

**Aida Knezevic:** And we can also tailor the article generation pipeline, like to your specific needs.

**Aida Knezevic:** So we've done this, for example, there's a client where, you know, they thought, they felt that the product mentions in the articles that we were creating for them were a little too, like, brief.

**Aida Knezevic:** They wanted more, like, information just about their different products.

**Aida Knezevic:** So we added an extra step in the article generation pipeline that finds a good place to, you know, incorporate a product mention.

**Aida Knezevic:** And then it generates a paragraph that, you know, provides more information.

**Aida Knezevic:** And it pulls from a completely separate artifact that just contains, like, a very in-depth breakdown of their platform and what it can do.

**Aida Knezevic:** So there are different ways that we can tailor this pipeline according to, like, what you need and what your requirements are.

**Aida Knezevic:** So it's just kind of a starting point.

**Aida Knezevic:** But I did want to say that there's, like, multiple, there are multiple ways we.

**Allison Gregory:** We take into account the writing guidelines.

**Allison Gregory:** Great.

**Allison Gregory:** Okay.

**Allison Gregory:** That all sounds good.

**Allison Gregory:** I think my main question was just like, I don't, I can't remember the name of the person who's been making that.

**Allison Gregory:** Yeah.

**Allison Gregory:** I wish I had.

**Allison Gregory:** I didn't want to make her go crazy by giving lots of edits there if it wasn't going to end up being an input in that way.

**Allison Gregory:** So I'll, it sounds like yes.

**Aida Knezevic:** So I'll keep going.

**Allison Gregory:** Yeah, yeah, yeah.

**Aida Knezevic:** Tell her I'm sorry.

**Aida Knezevic:** Definitely.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** All the, yeah, we're happy to get feedback.

**Aida Knezevic:** And it's typically implemented manually.

**Erik O'Brien:** it's not like.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So we can keep coaching them on.

**Erik O'Brien:** I know specifically a lot of the examples are what need some tuning.

**Erik O'Brien:** So I think, yeah, we'll keep working on those because if we get those right, then that is the kind of core piece that gets pushed into the review process during the article generation pipeline.

**Allison Gregory:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, we're almost at time.

**Aida Knezevic:** Do you have any?

**Aida Knezevic:** Last-minute questions before we go.

**Aida Knezevic:** No?

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So, yeah, we'll be on the lookout for your feedback on the calibration blog.

**Aida Knezevic:** We will also go through the articles that we recommend pruning from your website and double-check to make sure that the content is suitable for pruning.

**Aida Knezevic:** If not, we will label it as such.

**Aida Knezevic:** And, yeah, if you need anything else, you can reach me on Slack.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** See you next week.

**Reet Mand:** Bye-bye.

**Alexis Ruiz:** Thank you.

**Fung-Lin Wu:** Bye.

**Fung-Lin Wu:** Thank you.

**Fung-Lin Wu:** Bye-bye.
