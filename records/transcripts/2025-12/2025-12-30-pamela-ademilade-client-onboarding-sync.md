# Pamela / Ademilade Client Onboarding Sync

<metadata>
date: 2025-12-30
time: 14:07 UTC
duration: 90 minutes
organizer: ademilade@growthx.ai
participants: Pamela Weber, Ademilade Shodipe-dosunmu
fathom_recording_id: 111211468
fathom_url: https://fathom.video/calls/518880664
share_url: https://fathom.video/share/3dDbUJXXZC9f_xHSDxTo-Jg1vowkcBFW
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Ademilade onboarded Pamela Weber as a new content operations lead by walking through end-to-end workflows for three B2B clients: Disern (26 articles/week, highly automated PSEO pipeline), Yoko (6 articles/week, manual editorial with custom checklists), and Diligent (5 articles/week, refresh-heavy). The team decided to propose reassigning Diligent to another team member to reduce cognitive load on Pamela, with her starting at half Disern capacity for weeks 1-2, ramping to full 32-article/week load by week of January 12. Ademilade will remain available for post-handover support, and Pamela's first deliverables are 5 articles (3 Disern, 2 Yoko) due this week for detailed feedback.

---

## Context

Pamela Weber is a new content team member at GrowthX who joined to manage editorial workflows across multiple B2B clients. This meeting with Ademilade Shodipe-dosunmu, a GrowthX delivery lead, was the core client handover and onboarding session. Ademilade led Pamela through the content generation workflows for three assigned clients: Disern (26 articles/week via automated Atlas pipeline), Yoko (6 articles/week with manual editorial processes), and Diligent (5 articles/week, primarily refreshes). The call also served as a deep-dive training on Airtable, Atlas, and client-specific processes for publishing and analytics.

---

## Relevance

- **To GrowthX Delivery:** Disern uses a highly automated PSEO Atlas pipeline requiring minimal editing; Yoko is more manual with custom editorial checklists; Diligent may be reassigned to reduce new hire cognitive load. Airtable status tracking (Ready to Start → Article Generation → Ready for Staging → Published) is critical for publisher handoffs. Publishing workflow differs by client: Disern uses Webflow with Linear ticket + Slack notification; Yoko uses Prismic CMS. Both require careful image compression (<200 KB) and metadata management. Looker Studio tracking varies: Disern uses a hard-coded prompt for GA4/GSC formatting; Yoko has more complex setup detailed in operating manual videos.
- **To GrowthX Business Development:** Pamela's ramp-up plan (half Disern load weeks 1-2, then full load week 3+) is designed to manage risk on a high-volume client. Early feedback on Atlas usability (UI refresh issues, image generation bottlenecks) should be tracked. Client-specific friction points noted: Yoko is detail-oriented with frequent minor change requests; Diligent's refresh pipeline requires "significant massaging" of outputs.



---

## Overview

- **Client Handover:** Pamela will start with Disern (26 articles/wk) and Yoko (6 articles/wk). Ademilade will propose moving Diligent (5 articles/wk) to another team member, as its pipeline requires extensive manual work.
- **Ramp-Up Plan:** To manage the high volume, Pamela's Disern workload will be halved for the first 1–2 weeks, with Ademilade covering the rest. The full 26-article/week load begins the week of Jan 12.
- **Workflow Differences:** Disern uses a highly automated Atlas pipeline, requiring minimal editing. Yoko's workflow is more manual, using Claude for outlines and a separate editorial checklist for revisions.
- **Initial Assignments:** Pamela will complete 5 articles this week: 3 Disern edits (from pre-generated drafts) and 2 Yoko articles (1 new, 1 "Enriched" refresh). Ademilade will provide detailed feedback.

---

## Key Topics

### Client Handover & Workload

  - **Initial Plan:** Pamela was assigned Disern (26 articles/wk), Yoko (6 articles/wk), and Diligent (5 articles/wk).
  - **Proposed Change:** To ensure a smooth start, Ademilade will ask Pansa to reassign Diligent.
      - **Rationale:** Diligent's pipeline is not yet effective for refreshes, requiring significant manual "massaging" of the output.
  - **Revised Plan:** Pamela will manage Disern and Yoko.
      - **Disern:** Workload will be halved for the first 1–2 weeks, with Ademilade covering the remainder.
      - **Yoko:** Full workload starts immediately.

### Disern Workflow (26 articles/wk)

  - **Airtable (Content OS):** The central hub for all assignments.
      - **Key Statuses:** `Ready to Start` → `Article Generation` → `Ready for Staging` → `Published`.
      - **Crucial Step:** When moving an article to `Ready for Staging`, tag it as "New" or "Refresh" in the Airtable field. This tells the publisher (Sulaiman) whether to create a new file or update an existing one in Webflow.
  - **Atlas Pipeline (PSEO):** Highly automated, requiring minimal input.
      - **Process:** Enter topic → Run pipeline.
      - **Manual Checks:**
          - **Internal Links:** Verify the agentic workflow links to correct Disern landing pages.
          - **Meta Data:** Copy generated meta title/description from Atlas to Airtable.
          - **Images:** Select cover image from Atlas, then compress it to \<200 KB (e.g., via iLoveIMG) to prevent slow page loads. Upload the final image to Airtable.
  - **Editing & Publishing:**
      - **Editing:** Paste the final output into a Google Doc using "Paste from Markdown" to preserve formatting. Focus is on remedial edits (flow, language, adding external links).
      - **Publishing:**
          - Update Airtable status to `Ready for Staging`.
          - Notify publisher (Sulaiman) via the recurring Linear ticket for the week.
          - Post a summary in the internal Slack channel with the Linear ticket link.
  - **Looker Studio Updates:**
      - **Purpose:** Manually update the Looker dashboard every Monday to track performance of new articles.
      - **Process:** Use the hard-coded "Looker tasks" prompt in Claude to auto-format published URLs and clusters for GA4 and GSC.

### Yoko Workflow (6 articles/wk)

  - **Overview:** More manual and client-specific. Pamela must review the Yoko Operating Manual and associated Loom videos for full context.
  - **New Article Generation:**
      - **Outline:** Use Claude to create a detailed SEO outline from the Airtable assignment (title, keywords, pain points).
      - **Assignment Direction:** Ask Claude to convert the outline into an assignment direction, using an existing Yoko spec plan as a template.
      - **Atlas Input:** Paste the assignment direction into the Atlas pipeline.
      - **Outline Override:** In the Atlas brief, delete the auto-generated "Proposed content structure" and paste in the Claude-generated outline.
      - **Editorial Checklist:** Run the Atlas output through the Yoko editorial checklist prompt in Claude for a revised draft.
      - **Final Edits:** In a Google Doc, add external links (sourced from the manual), verify statistics, and format for readability.
  - **"Enriched" Refreshes:**
      - **Process:** Create a new tab in the article's Google Sheet called "Enriched." Paste the original content and make revisions.
      - **Changes:** Update titles, fix broken links, add 2–3 new internal links, add FAQs, and improve flow.
      - **Summary:** Add a comment at the top detailing all changes made.
  - **Staging & Looker:**
      - **Staging:** Pamela stages articles directly in the Prismic CMS (15-minute process per article).
      - **Looker:** The process is more complex than Disern's; Pamela must watch the Loom video in the operating manual before attempting.

---

## Action Items

**Ademilade Shodipe-dosunmu**
- Confirm Diligent reassignment w/ Panza; update Pamela
- Send Pamela Looker/Prismic how-to links; she watches before updates
- Send Pamela Yoko personal prompts/resources

**Pamela Weber**
- Edit 3 Discern articles; send to Ademilade for review
- Review Yoko operating manual + videos
- Write Yoko new article Mastering Internal Engagements; send to Ademilade for review
- Check Cloud access; if blocked, ping Youssef
- Enrich Yoko article Understanding All-New; send to Ademilade for review

---

## Transcript
**Pamela Weber:** Okay, I'll put it up higher.

**Pamela Weber:** Sorry, I think it's a headset.

**Pamela Weber:** I'm going to get a different one, but sorry.

**Pamela Weber:** That's we have for now.

**Ademilade Shodipe-dosunmu:** Let me switch to my headset so I can hear you clearly.

**Ademilade Shodipe-dosunmu:** Well, can you hear me clearly like this?

**Ademilade Shodipe-dosunmu:** Yeah, I can.

**Ademilade Shodipe-dosunmu:** Perfect.

**Ademilade Shodipe-dosunmu:** Let me wear this so I can also hear you.

**Ademilade Shodipe-dosunmu:** Let's connect these.

**Ademilade Shodipe-dosunmu:** Let's Let's

**Ademilade Shodipe-dosunmu:** I'm trying to figure this out.

**Ademilade Shodipe-dosunmu:** It's one weird reason it always boils down UX.

**Ademilade Shodipe-dosunmu:** Yep, can you hear me?

**Pamela Weber:** Yep, I can hear you perfectly well.

**Pamela Weber:** That's perfect.

**Ademilade Shodipe-dosunmu:** How's it going?

**Ademilade Shodipe-dosunmu:** How's the week?

**Ademilade Shodipe-dosunmu:** How's the holidays?

**Ademilade Shodipe-dosunmu:** Good, good.

**Pamela Weber:** We just had a blizzard, so we're digging out from that, so it's fun.

**Pamela Weber:** I've still all the way up my office window.

**Pamela Weber:** It's hilarious.

**Pamela Weber:** But yeah, it's fun.

**Pamela Weber:** I mean, I love Atlas.

**Pamela Weber:** I did some test articles, but one of them got stuck on the image thing for forever.

**Pamela Weber:** So if that happens, is there a way to stop that part and then get the actual article?

**Pamela Weber:** Because I couldn't get it to give me the article, even without the images.

**Pamela Weber:** So I was wondering if could talk me through that, too, when you go through this.

**Ademilade Shodipe-dosunmu:** What pipeline was it?

**Pamela Weber:** Oh gosh, it's like a test one.

**Pamela Weber:** It's Metrodome or something, I think it was.

**Pamela Weber:** Maybe that's why, maybe it's in the sandbox, but maybe you're doing real— do you have a link?

**Ademilade Shodipe-dosunmu:** Do you have a link to the sandbox?

**Ademilade Shodipe-dosunmu:** Hold on a second.

**Pamela Weber:** Oh, wait, did it come now?

**Pamela Weber:** Oh, shoot.

**Pamela Weber:** Oh, maybe it ran overnight.

**Pamela Weber:** Hold on one sec.

**Pamela Weber:** Oh, no, it's still here.

**Pamela Weber:** Hold on.

**Pamela Weber:** Okay, that's the one that I have.

**Pamela Weber:** I was thinking maybe because it's in the sandbox, maybe it's conflicted with, like, something in it.

**Pamela Weber:** It's not, like, real or something.

**Pamela Weber:** I don't know.

**Pamela Weber:** And it's okay, you're going to give me real ones to do, so.

**Ademilade Shodipe-dosunmu:** So I can see that, like, the images were actually generated.

**Ademilade Shodipe-dosunmu:** Oh, mine's showing it's, like, spinning still.

**Pamela Weber:** Maybe we just have to refresh or something.

**Pamela Weber:** Yeah, so sometimes, sometimes.

**Ademilade Shodipe-dosunmu:** Sometimes it's like a UI thing, so like if you're here and like it seems to run forever, either refresh the page or like go out, then come back in and refresh like the main menu here and you will see that, hey, it's actually done here.

**Ademilade Shodipe-dosunmu:** Okay, cool.

**Pamela Weber:** Thank you so much.

**Pamela Weber:** Okay, awesome.

**Ademilade Shodipe-dosunmu:** And if you want like the actual contents, you probably would just go to the last, I'm trying to, yeah, you just probably go to the last output.

**Ademilade Shodipe-dosunmu:** So the last output that makes sense here isn't SEO tags because SEO tags doesn't really, SEO tags just sticks in like your input being like your topic and all of that and gives you, you know, SEO tags.

**Ademilade Shodipe-dosunmu:** So the last one would probably have to be final quality and compliance because this does like compliance checks and all and it gives returns and outputs, which is the entire article.

**Ademilade Shodipe-dosunmu:** So this would probably be the final article.

**Ademilade Shodipe-dosunmu:** I didn't know it's fair.

**Ademilade Shodipe-dosunmu:** I was going to.

**Pamela Weber:** The bottom where it said output and I didn't see anything, I thought it was just stuck because the images, it wasn't releasing the article.

**Pamela Weber:** So I didn't know I could find it in earlier steps.

**Pamela Weber:** That makes sense.

**Pamela Weber:** Okay, thank you.

**Pamela Weber:** Yeah, you can.

**Pamela Weber:** totally unlocked me.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** You would, like, figure out, like, you'd run into, like, little, little things like that, like this, where you use Adplas.

**Ademilade Shodipe-dosunmu:** So, like, always feel free to, like, shoot me a DM or something.

**Ademilade Shodipe-dosunmu:** You know, even after your handover is done, like, you know, just shoot me a message.

**Ademilade Shodipe-dosunmu:** I'm happy to jump in and check it out for you.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** That was an easy fix.

**Pamela Weber:** I was, like, staring at it for, like, a day.

**Pamela Weber:** Like, why isn't this finishing?

**Ademilade Shodipe-dosunmu:** Yeah, like, really, like, so easy.

**Ademilade Shodipe-dosunmu:** But, like, I can understand because, like, when we first started using Adplas, like, we had, like, all of these little problems as well.

**Ademilade Shodipe-dosunmu:** But, like, you know, we just built, like, muscle memory and, like, you know, you just have, like, a knack for it now.

**Ademilade Shodipe-dosunmu:** You know, you know, okay, hey, I can probably refresh this and it should be normal.

**Ademilade Shodipe-dosunmu:** So, you know, just knowing, like, when to refresh and when to check somewhere else as opposed to getting stuck.

**Ademilade Shodipe-dosunmu:** Because not everything requires a ticket.

**Ademilade Shodipe-dosunmu:** So I wanted to ask, before diving into everything today, wanted to ask if you had any questions so far with just all the current content that I'm giving you to digest, because it's actually been a lot.

**Ademilade Shodipe-dosunmu:** No, that was the biggest thing.

**Pamela Weber:** I'm running test articles to get ready for this.

**Pamela Weber:** I love Atlas.

**Pamela Weber:** It's super cool, and I like seeing all those steps.

**Pamela Weber:** So, no, I just want to see how it works, how it goes and everything.

**Pamela Weber:** Yeah, thanks.

**Ademilade Shodipe-dosunmu:** I'll just turn off the camera for a second, because Wi-Fi is pretty shoddy here.

**Ademilade Shodipe-dosunmu:** So let's make sure we're good on that.

**Ademilade Shodipe-dosunmu:** Okay, perfect.

**Ademilade Shodipe-dosunmu:** We can start.

**Ademilade Shodipe-dosunmu:** Before I actually proceed with these, I wanted to just get a gut check from you in terms of like,

**Ademilade Shodipe-dosunmu:** How, what's the word, how maybe you could give me like a more complete answer after you've run some, you know, tests, but like, why don't you get like a vibe check on how confident you're feeling in like doing like article generation for like all these clients, like the next week and the week after, like, in a sense, like, do you feel comfortable taking on these three clients at once?

**Ademilade Shodipe-dosunmu:** It's like, in my mind, it's a lot to start off with.

**Ademilade Shodipe-dosunmu:** And like, I'm just trying to be sure that like, I'm setting you up for success, as opposed to like, just don't be like, it should work on you.

**Ademilade Shodipe-dosunmu:** So yeah.

**Pamela Weber:** Yeah, well, the two that are like, like five and six, yeah, for sure.

**Pamela Weber:** I mean, the articles in general, I think it'll be easier.

**Pamela Weber:** And when I see the output, I know exactly the changes I want to make, like language and structure.

**Pamela Weber:** So that's like the easiest part, obviously, the editing, which is more learning how to, where the things or they are, and then getting them into the pipeline.

**Pamela Weber:** And then once it's generated, then that's the easy part for me.

**Pamela Weber:** So I'm learning the other steps.

**Pamela Weber:** So I'm learning the other

**Pamela Weber:** I asked Matt about the 26-whatever client, if there's like a different one I could use instead, or I haven't heard back, so until I hear him, you know, I'll keep going, like I'm using that one, and I'll learn that one today too with you.

**Pamela Weber:** But yeah, I thought it'd be easier instead of starting right away with one that has 26, like two, five, six, and another woman has like, you know, a little, you know, less, because I'm learning all the moving parts, plus like huge volume for one client.

**Pamela Weber:** So, I asked if was a possible switch, but I mean, I assume I won't hear back to next week when everybody's back.

**Pamela Weber:** But yeah, for now, I'll learn that one too.

**Pamela Weber:** Yeah, yeah, if that was possible.

**Ademilade Shodipe-dosunmu:** So, I was actually thinking about it, because like, it's actually like a lot of workload, and the problem is, right, like, I'm going still give you like some support, like even next week when the handover is there, but like, I'm moving to strategy sprints.

**Ademilade Shodipe-dosunmu:** Yeah, we're going to that thing, and like, there's already like a lot of work that I'm going to be taking on.

**Ademilade Shodipe-dosunmu:** When I get there, because they're starting like a couple of clients' kickoffs next week, like brand new clients, and I already know the amount of work I'll have to do for those.

**Ademilade Shodipe-dosunmu:** So I'm just trying to create a situation where neither of us feels overworked, if that makes sense.

**Ademilade Shodipe-dosunmu:** Discern, I'll work with you like how, like in this call, I'll work with you like content gen for all of them, so you know like where to go for it.

**Ademilade Shodipe-dosunmu:** Like, we do start to finish for like all of them, so you don't worry about that, and like this call is recorded, so you can always go back.

**Ademilade Shodipe-dosunmu:** So just, you know, getting that one out there.

**Ademilade Shodipe-dosunmu:** But I was thinking, like, Diligent actually is like another five to six clients, like five articles weekly.

**Ademilade Shodipe-dosunmu:** However, it's mainly refreshes, and I was just thinking of like how it would be to give like someone that's like relatively new to like the system, like three relatively complicated accounts.

**Ademilade Shodipe-dosunmu:** I would say that like, in terms of content generation, the easiest in the list is probably your call, relatively short.

**Ademilade Shodipe-dosunmu:** It's It doesn't have any quirks.

**Ademilade Shodipe-dosunmu:** I actually just took on that account two weeks ago.

**Ademilade Shodipe-dosunmu:** It was just handed over to me two weeks ago.

**Ademilade Shodipe-dosunmu:** But yeah, content is pretty easy.

**Ademilade Shodipe-dosunmu:** The other two have a ton of quirks and things you need to keep track of.

**Ademilade Shodipe-dosunmu:** So I actually reached out to one of my friends and colleagues within Growthx.

**Ademilade Shodipe-dosunmu:** He's also worked on a client before that.

**Ademilade Shodipe-dosunmu:** They had to do a lot of refresh and they asked him whether he could take on that client.

**Ademilade Shodipe-dosunmu:** That's diligent because I feel like it might be smoother for you to start off with.

**Ademilade Shodipe-dosunmu:** Ideally, to be smoother for you to start off with like two clients that it's just like five or six, suppose, then ramp up to three clients and keep going like that.

**Ademilade Shodipe-dosunmu:** However, I don't know how possible that would be, based off of like your sports are available and like capacity for everybody.

**Ademilade Shodipe-dosunmu:** However, I think like the only way to probably meet in the middle would be, I want to reach out to fans and ask him if it would make sense to, give.

**Ademilade Shodipe-dosunmu:** Maybe diligent, to see whether he can take on diligent, because he has a bit of less interrupted right now.

**Ademilade Shodipe-dosunmu:** And I called him earlier today, and he said, yeah, that's fine.

**Ademilade Shodipe-dosunmu:** Yeah, he's down for that.

**Ademilade Shodipe-dosunmu:** So I want to reach out to see if that's possible.

**Ademilade Shodipe-dosunmu:** And if that works, that will probably give you with your code and discern.

**Ademilade Shodipe-dosunmu:** Discern is the 26 per week.

**Ademilade Shodipe-dosunmu:** But on that note, you might not have to do 26 per week immediately.

**Ademilade Shodipe-dosunmu:** I would try to give you a bit of support for, like, a couple of weeks, you know, while you learn.

**Ademilade Shodipe-dosunmu:** But for your crew, you probably would take on the full workload immediately, because that's just six per week.

**Ademilade Shodipe-dosunmu:** So that's easy.

**Ademilade Shodipe-dosunmu:** And the content is, like, pretty easy, to be honest.

**Ademilade Shodipe-dosunmu:** The hard part is, like, just a quick segue.

**Ademilade Shodipe-dosunmu:** How familiar are you with Airtable?

**Ademilade Shodipe-dosunmu:** I'm sorry, what was the last question?

**Ademilade Shodipe-dosunmu:** I was, like, a quick segue.

**Ademilade Shodipe-dosunmu:** Like, how familiar are you with Airtable?

**Ademilade Shodipe-dosunmu:** I'm not.

**Pamela Weber:** I've gone in there and looked at it and on board.

**Pamela Weber:** So, not really.

**Ademilade Shodipe-dosunmu:** No problem.

**Ademilade Shodipe-dosunmu:** I'll walk you through a few quirks.

**Ademilade Shodipe-dosunmu:** The most difficult part of the Yoko is not the content.

**Ademilade Shodipe-dosunmu:** It's managing all of the clients' little requests.

**Ademilade Shodipe-dosunmu:** Like, this link is like, oh, hey, every little thing.

**Ademilade Shodipe-dosunmu:** She points out every little thing, and it's a good annoying, but what can you do?

**Ademilade Shodipe-dosunmu:** But yeah, the content itself is not difficult.

**Ademilade Shodipe-dosunmu:** pretty easy.

**Ademilade Shodipe-dosunmu:** And I'll walk you through that.

**Ademilade Shodipe-dosunmu:** Okay, go on, go on.

**Ademilade Shodipe-dosunmu:** No, thank you.

**Pamela Weber:** So thank you for checking on that.

**Pamela Weber:** Yeah, so I'm just a little confused.

**Pamela Weber:** So Yoko is six.

**Pamela Weber:** I'm going to do that for sure.

**Pamela Weber:** And then the other two, you said one of them I may start and someone else may take it, or I'm just part of that.

**Ademilade Shodipe-dosunmu:** Yeah, so that's Dilijan.

**Ademilade Shodipe-dosunmu:** I want to ask Pansa today if Dilijan can go see me instead.

**Ademilade Shodipe-dosunmu:** I don't think it would be fair to give you these three accounts to start off with right off the bat.

**Ademilade Shodipe-dosunmu:** But like I said, I want to make sure that you set up for success as much as possible.

**Ademilade Shodipe-dosunmu:** So like I don't think...

**Ademilade Shodipe-dosunmu:** It's fair.

**Ademilade Shodipe-dosunmu:** If I just joined ProText and someone was giving me these three accounts, I'll probably go crazy.

**Ademilade Shodipe-dosunmu:** That's what I asked him yesterday.

**Pamela Weber:** I said, if I have to, it's okay.

**Pamela Weber:** But I said, just learning everything plus data volume, said that it would just be smoother to do it with the two less.

**Pamela Weber:** So yeah, I'm fine either way.

**Pamela Weber:** But yeah, that would be fantastic.

**Pamela Weber:** I appreciate your trying to help with that too.

**Pamela Weber:** Thank you.

**Pamela Weber:** Yeah, I asked him yesterday.

**Ademilade Shodipe-dosunmu:** Okay, So like, just like, opinion on that.

**Ademilade Shodipe-dosunmu:** So what probably happened, like, what I think, ideally what would happen is like, you would do discern and Yoko.

**Ademilade Shodipe-dosunmu:** Do discern is the 26 per week, but you would probably not be doing 26 per week every week.

**Ademilade Shodipe-dosunmu:** Like, at the beginning, like, it would like sort of get you slowly ramped up, if that makes sense.

**Ademilade Shodipe-dosunmu:** So probably, you would probably like, maybe half of that load, maybe on a week or for like two weeks.

**Ademilade Shodipe-dosunmu:** Then I would see about helping you with the other half.

**Ademilade Shodipe-dosunmu:** Right?

**Ademilade Shodipe-dosunmu:** Just to make sure that, like, you're still fine and, like, things are still working out the way they should be.

**Ademilade Shodipe-dosunmu:** Then, like, after, like, maybe two, three weeks, you can see about, like, having the full load.

**Ademilade Shodipe-dosunmu:** So it's like, you know, you're still, like, learning the processes and everything.

**Ademilade Shodipe-dosunmu:** But does that make sense to you?

**Ademilade Shodipe-dosunmu:** Oh, I get it.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So I keep the discern.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** So I was confused on who is which.

**Pamela Weber:** So discern is a 26.

**Pamela Weber:** So keep that one.

**Pamela Weber:** But you would, but you're, like, less of a workload in the beginning, but you're co.

**Pamela Weber:** And then diligent would maybe go to someone else.

**Ademilade Shodipe-dosunmu:** That one is less.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I see what mean.

**Pamela Weber:** Yeah.

**Pamela Weber:** was thinking to get, to take the turn off my plate, but you're saying take, um, okay, now I get it.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So whatever, however you guys work it out.

**Pamela Weber:** I mean, you guys know the workload for the whole company.

**Pamela Weber:** That's why I just asked him whatever, if it works.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** Whatever you guys figure out, of course.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Perfect.

**Ademilade Shodipe-dosunmu:** The main fact is that, like, diligent is, like, a bit more, how would I put it?

**Ademilade Shodipe-dosunmu:** But, for your, for discern, like, can use the pipelines easily to get the contents you want.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Pipelines are pretty okay, right?

**Ademilade Shodipe-dosunmu:** Which is why I want you to have those accounts.

**Ademilade Shodipe-dosunmu:** Diligent, this pipeline is a bit more confusing in that it's refreshing.

**Ademilade Shodipe-dosunmu:** So the pipeline isn't really giving the results we need.

**Ademilade Shodipe-dosunmu:** So we have to do a lot of massaging and cloud and all of that.

**Ademilade Shodipe-dosunmu:** And like, I've been trying to crack the pipeline to get to a place where it can actually work properly well for intelligent content.

**Ademilade Shodipe-dosunmu:** But it's not there yet.

**Ademilade Shodipe-dosunmu:** So I'd rather give you two accounts that have really good pipelines already, as opposed to giving you one account with a good pipeline and one account with a pipeline that you're not doing a lot of work on.

**Ademilade Shodipe-dosunmu:** see what you mean.

**Pamela Weber:** It looks scarier because it's more, but the pipeline is more.

**Pamela Weber:** Yeah, exactly.

**Pamela Weber:** The pipeline is probably the best pipeline I have.

**Ademilade Shodipe-dosunmu:** worse, but it's not.

**Ademilade Shodipe-dosunmu:** Yeah, precisely.

**Ademilade Shodipe-dosunmu:** Great, great, great.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** So I think as of now, we can just pretty much.

**Ademilade Shodipe-dosunmu:** So what we're going to do is that I'm going to dive into the day-to-day of each of the clients from like article gen and like what you're responsible for.

**Ademilade Shodipe-dosunmu:** Then.

**Ademilade Shodipe-dosunmu:** I'll walk you through like article gen for one article for each of these accounts, like the process.

**Ademilade Shodipe-dosunmu:** Then we, then, you know, I assign you articles across all of the accounts.

**Ademilade Shodipe-dosunmu:** Then we see how that works.

**Ademilade Shodipe-dosunmu:** So you're going to probably have like a total of seven articles to do.

**Ademilade Shodipe-dosunmu:** That's this week.

**Ademilade Shodipe-dosunmu:** That is in total, right?

**Ademilade Shodipe-dosunmu:** And the idea of that is to give you an experience across each client so that you just sort of have like some practice.

**Ademilade Shodipe-dosunmu:** Then we see where it goes from there.

**Ademilade Shodipe-dosunmu:** Then I will edit each of these articles.

**Ademilade Shodipe-dosunmu:** once you're done with any of them, just send them my way and I'll take a look and give you like detailed feedback so that like you sort of know what to look out for in the others.

**Ademilade Shodipe-dosunmu:** The way I think works best is that like I probably edit the first articles across the board for all of them.

**Ademilade Shodipe-dosunmu:** Give you really detailed feedback.

**Ademilade Shodipe-dosunmu:** Look at the second one.

**Ademilade Shodipe-dosunmu:** The feedback will be as detailed, obviously, because, you know, we would have applied the changes and we take it from there.

**Ademilade Shodipe-dosunmu:** How does that sound?

**Pamela Weber:** Yeah, sounds good.

**Pamela Weber:** Thank you.

**Pamela Weber:** All right, perfect.

**Ademilade Shodipe-dosunmu:** Let's dive in.

**Ademilade Shodipe-dosunmu:** Do you have a preference with which one you want?

**Ademilade Shodipe-dosunmu:** So I was just playing around with like the pipelines, trying to set up something for you, but I'm going to pull up, let's pull up the INS channel, so going to the internal discern, like I said, if you want to know what you're supposed to do every week, I have this weekly recurring tasks, plus habits, in, so it's a list of like everything I do every single day of the week.

**Ademilade Shodipe-dosunmu:** You can edit this however you feel, you can't use it, you can't set not to use it, but this is the clearest outline of like what you're expected to do every day for this client.

**Ademilade Shodipe-dosunmu:** So, you can obviously read this at your own time, but we're going to go through three things now, which is, article generation, okay, so we'll go from picking topics, so we'll do Airtable, picking topics, article generation,

**Ademilade Shodipe-dosunmu:** Editing and publishing, then we do look up.

**Ademilade Shodipe-dosunmu:** Does that sound good?

**Ademilade Shodipe-dosunmu:** Yep.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** What did you say?

**Ademilade Shodipe-dosunmu:** Alright.

**Ademilade Shodipe-dosunmu:** So starting with article gen.

**Ademilade Shodipe-dosunmu:** So typically what happens with assignments is I'm going to give you access to this spreadsheet.

**Ademilade Shodipe-dosunmu:** So you have editing access here.

**Ademilade Shodipe-dosunmu:** So this is just my content planner.

**Ademilade Shodipe-dosunmu:** Like I said, 26 per week is a bit crazy.

**Ademilade Shodipe-dosunmu:** So like I use this to have like a clear view of like what I'm supposed to do.

**Ademilade Shodipe-dosunmu:** Well, let's just start off with the air table.

**Ademilade Shodipe-dosunmu:** So this is Descent Content OS.

**Ademilade Shodipe-dosunmu:** This is where all the assignments live in.

**Ademilade Shodipe-dosunmu:** Let me just move this.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** This is where all the assignments live.

**Ademilade Shodipe-dosunmu:** And there are different views for all of these.

**Ademilade Shodipe-dosunmu:** But where you need to pay attention to is assignments.

**Ademilade Shodipe-dosunmu:** So I'm going

**Ademilade Shodipe-dosunmu:** I'm rename this as a handover, so this will probably read Pamela's assignments, and I'll assign you this personal view.

**Ademilade Shodipe-dosunmu:** Let me just, just sort of trying to, trying to make sure that you can see the view.

**Ademilade Shodipe-dosunmu:** So, I would make this collaborative, so you can see the view.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Alright, so this is published articles.

**Ademilade Shodipe-dosunmu:** Let's do the same for assignments.

**Ademilade Shodipe-dosunmu:** Then, I'll add this to favorites.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Are you able to, yeah, so you can view all these three.

**Ademilade Shodipe-dosunmu:** So, let's start with getting assignments.

**Ademilade Shodipe-dosunmu:** So, here is where you see all the assignments you have, and I'll explain what each of these statuses mean from the beginning.

**Ademilade Shodipe-dosunmu:** So one is backlog.

**Ademilade Shodipe-dosunmu:** Backlog is just like, it's a backlog essentially.

**Ademilade Shodipe-dosunmu:** Probably topics that the client has not approved yet.

**Ademilade Shodipe-dosunmu:** Topics that maybe we're still thinking about whether we want to even send to the client.

**Ademilade Shodipe-dosunmu:** Considering is topics that the client is considering, like we've sent to the client to review and like, oh, hey, does this work?

**Ademilade Shodipe-dosunmu:** Does this make sense?

**Ademilade Shodipe-dosunmu:** Ready to start is topics that are ready to start.

**Ademilade Shodipe-dosunmu:** So anything here has been approved and it's ready for you to take on, right?

**Ademilade Shodipe-dosunmu:** So anything on that we need to start, you can work on it.

**Ademilade Shodipe-dosunmu:** ASCII generation, this is all for you.

**Ademilade Shodipe-dosunmu:** So ASCII generation is when you're generating the article, you put it here, like you're probably working on it.

**Ademilade Shodipe-dosunmu:** Image generation, same thing.

**Ademilade Shodipe-dosunmu:** You're generating images for it.

**Ademilade Shodipe-dosunmu:** These two, I typically do these two at the same time.

**Ademilade Shodipe-dosunmu:** So no need to have them in separate statuses, but it's here for the moment.

**Ademilade Shodipe-dosunmu:** Grotex editing used to be for when, so before the structure of Grotexes is, was that like clients clients are

**Ademilade Shodipe-dosunmu:** The Emmys did not own end-to-end content production, so what we had was we had a content manager, then on that, above that content manager was a managing editor, so the content manager would work on the art schools, then the managing editor would now review them, the art schools, so that was the entire point of the text editing.

**Ademilade Shodipe-dosunmu:** So when I was still a content manager, I would, when I'm done with an art school, I'll put it into the text editing so that my editor, my managing editor knows that, oh, hey, she takes a look at it and like edits or gives me feedback, then I work on it.

**Ademilade Shodipe-dosunmu:** Right, does that make sense?

**Ademilade Shodipe-dosunmu:** Just want to be sure that I like you.

**Ademilade Shodipe-dosunmu:** Okay, great.

**Ademilade Shodipe-dosunmu:** Then holiday backlog was just for this December.

**Ademilade Shodipe-dosunmu:** I'm going to remove the status.

**Ademilade Shodipe-dosunmu:** The idea of this was the extra articles we were generating to cover for the December period where people are out of office, so I will just put articles that have been approved here.

**Ademilade Shodipe-dosunmu:** Seven is ready for discern and review.

**Ademilade Shodipe-dosunmu:** This is usually for articles that we want to get the clients to read on, so we'll tell them, oh, hey, this article is ready for review.

**Ademilade Shodipe-dosunmu:** I'll put it in the status.

**Ademilade Shodipe-dosunmu:** This was...

**Ademilade Shodipe-dosunmu:** used to use the status a lot more before, when the client last night was still reviewing articles bit by bit.

**Ademilade Shodipe-dosunmu:** Well, now we've viewed a lot of crust, so we rarely use the status.

**Ademilade Shodipe-dosunmu:** Literally, only the first article in a new cluster, that's what he reviews.

**Ademilade Shodipe-dosunmu:** So we're pretty much good to go on that one.

**Ademilade Shodipe-dosunmu:** Then ready for staging is the status that we put it in when it's ready for staging.

**Ademilade Shodipe-dosunmu:** So this just indicates to our, so if you go to this view called ready to stage here, that's where the articles would be.

**Ademilade Shodipe-dosunmu:** So that's where our publisher goes, so that he knows what he's supposed to publish, if that makes sense.

**Ademilade Shodipe-dosunmu:** So anything that's ready to stage is more like, okay, hey, he's allowed to take the articles here and put them into workflow.

**Ademilade Shodipe-dosunmu:** So that's typically the approach for that.

**Ademilade Shodipe-dosunmu:** Then publishes for articles that obviously are published.

**Ademilade Shodipe-dosunmu:** So once the publisher publishes it, you change the status to published.

**Ademilade Shodipe-dosunmu:** On hold, reverse.

**Ademilade Shodipe-dosunmu:** Topics where maybe there's an issue or maybe the client doesn't want us working on that cluster for now.

**Ademilade Shodipe-dosunmu:** We just put it on a hold so we know that, okay, we're not doing these right now.

**Ademilade Shodipe-dosunmu:** Refreshing is AdSchools that we're refreshing.

**Ademilade Shodipe-dosunmu:** Easy.

**Ademilade Shodipe-dosunmu:** Approve for creation.

**Ademilade Shodipe-dosunmu:** This is actually a new status.

**Ademilade Shodipe-dosunmu:** We don't use any of these two.

**Ademilade Shodipe-dosunmu:** use AdSchools that clients have approved.

**Ademilade Shodipe-dosunmu:** This approval for creation here is the same thing as like pretty much ready to start.

**Ademilade Shodipe-dosunmu:** So, yeah, well, usually move them from approved to creation to ready to start.

**Ademilade Shodipe-dosunmu:** I definitely have to, because of so much has changed the last couple of weeks and how like we interact with like operations and growth effects, I have to just sort of tidy these up.

**Ademilade Shodipe-dosunmu:** But that's just generally what all of them mean.

**Ademilade Shodipe-dosunmu:** So that's the idea.

**Ademilade Shodipe-dosunmu:** And usually for staging, I always indicate, I always try to indicate when I'm putting articles in staging, what type of articles they are.

**Ademilade Shodipe-dosunmu:** So instead you would see something like, I'm trying to...

**Ademilade Shodipe-dosunmu:** to...

**Ademilade Shodipe-dosunmu:** So to...

**Ademilade Shodipe-dosunmu:** So So So

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So it doesn't show up here, but it does show up.

**Ademilade Shodipe-dosunmu:** Let me check if we have any article in the bottom.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** It's not showing up here.

**Ademilade Shodipe-dosunmu:** I wanted to show you something.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I'll just move on and scroll back and I'll move it back.

**Ademilade Shodipe-dosunmu:** So let's just scroll down to...

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Let's move this to staging.

**Ademilade Shodipe-dosunmu:** Just for example.

**Ademilade Shodipe-dosunmu:** And if you come in here to ready to stage, I always indicate here what content type it is.

**Ademilade Shodipe-dosunmu:** So if it's a new article, I'll indicate it here.

**Ademilade Shodipe-dosunmu:** If it's a refresh, I'll indicate it here.

**Ademilade Shodipe-dosunmu:** That's very important for our publisher because if it's a new article, has to create a new file in Webflow.

**Ademilade Shodipe-dosunmu:** But if it's a refresh, he just has to search for the existing file.

**Ademilade Shodipe-dosunmu:** So make sure to tag these anytime like an article is ready for staging.

**Ademilade Shodipe-dosunmu:** So when you're an article, this is where you drop it.

**Pamela Weber:** So when you're done with an article, this is what, well, now I'm going to give it to you, but later this is where I would drop it?

**Ademilade Shodipe-dosunmu:** Yeah, pretty much it would be in a table, yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So moving this back to published.

**Ademilade Shodipe-dosunmu:** So that's just like a tool of a table and like the statuses you need to keep an eye on.

**Ademilade Shodipe-dosunmu:** Right, so like I said, I explained the flow is picking an article up from a table here.

**Ademilade Shodipe-dosunmu:** So what I typically would do ideally is, for example, as I'm working on these articles this week, I would pretty much add them to my content planner so I know what I'm looking at, then update it as it goes.

**Ademilade Shodipe-dosunmu:** For example, let's just say, hey, we're working on best CT Corp alternatives for tech startups in 2025, right?

**Ademilade Shodipe-dosunmu:** So what I typically would do is, I would take this, this is the assignment.

**Ademilade Shodipe-dosunmu:** For the document for this, what I will do is...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** I would go here.

**Ademilade Shodipe-dosunmu:** This is the discern drive.

**Ademilade Shodipe-dosunmu:** I'll go to the appropriate folder.

**Ademilade Shodipe-dosunmu:** So right now, this is the folder for competitor for this cluster.

**Ademilade Shodipe-dosunmu:** So this cluster is competitor comparisons.

**Ademilade Shodipe-dosunmu:** So let me just make them.

**Ademilade Shodipe-dosunmu:** Let's make it comp comparisons.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** So it's visible.

**Ademilade Shodipe-dosunmu:** So I'll go into this folder and I'll just like create the documents.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** So I'll create a Google Doc from this.

**Ademilade Shodipe-dosunmu:** Then I would, upon creating that Google Doc, I would come here.

**Ademilade Shodipe-dosunmu:** I'll paste it into the regular section here in the sheets.

**Ademilade Shodipe-dosunmu:** And I'll also paste it into a table.

**Ademilade Shodipe-dosunmu:** So I would place it here.

**Ademilade Shodipe-dosunmu:** Then assign to, I would assign it to myself.

**Ademilade Shodipe-dosunmu:** For the slug, I would, the approach for the slug is pretty much just the primary keywords.

**Ademilade Shodipe-dosunmu:** So in this case to be about the best city for the slug.

**Ademilade Shodipe-dosunmu:** Alternatives, and I'll start with the forward slash for this log here.

**Ademilade Shodipe-dosunmu:** That's easy enough.

**Ademilade Shodipe-dosunmu:** Then after this, I would fill metadata and meta description.

**Ademilade Shodipe-dosunmu:** These can be filled in Atlas.

**Ademilade Shodipe-dosunmu:** So in Atlas, you just go to, well, let me actually walk you through the Atlas Gen process.

**Ademilade Shodipe-dosunmu:** So for PSEO articles, you'll be hit with this input when you, oh, yeah, you'll hit with this input when, well, you've already generated articles, right?

**Ademilade Shodipe-dosunmu:** I just want to confirm that so I know what I have to do and what I don't have to do.

**Pamela Weber:** test ones, not like any real ones, but yeah, I've generated them.

**Pamela Weber:** Just test.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Maybe we just run a test here.

**Ademilade Shodipe-dosunmu:** So what I would do is like, let's say I wanted to work on these articles.

**Ademilade Shodipe-dosunmu:** So I would add, I've already pre-populated this particular pipeline with stuff.

**Ademilade Shodipe-dosunmu:** So it already fact checks the proper domains.

**Ademilade Shodipe-dosunmu:** So you don't have to fill

**Ademilade Shodipe-dosunmu:** It has a decent image arch direction already.

**Ademilade Shodipe-dosunmu:** I'm thinking of changing this because of, I don't really like the pictures you've given me for this cluster above, CDD.

**Ademilade Shodipe-dosunmu:** The internal link site has already been pre-populated, so you don't need to add anything here.

**Ademilade Shodipe-dosunmu:** Research domains to ignore, I've already pre-populated it from the pipeline, so you don't need to do anything here.

**Ademilade Shodipe-dosunmu:** Vita guidelines, you can ignore this.

**Ademilade Shodipe-dosunmu:** The only thing you need to add is just the topic.

**Ademilade Shodipe-dosunmu:** All right, so that's how much I've customized the template so far.

**Ademilade Shodipe-dosunmu:** So just the topic.

**Ademilade Shodipe-dosunmu:** So the topic here is best CD-Corp.

**Ademilade Shodipe-dosunmu:** So I think 2026, because 2026, so ideally you would just copy this, then you would put it in the pipeline here, and you would create.

**Ademilade Shodipe-dosunmu:** And you save, then you just run the step.

**Ademilade Shodipe-dosunmu:** Pretty simple process for this cluster.

**Ademilade Shodipe-dosunmu:** And it's running.

**Ademilade Shodipe-dosunmu:** It's going to take a bit of time, but yeah.

**Ademilade Shodipe-dosunmu:** So it's running.

**Ademilade Shodipe-dosunmu:** When it gets to templated draft, it will show you a draft of the article, right?

**Ademilade Shodipe-dosunmu:** And you just compare that to what we already have.

**Ademilade Shodipe-dosunmu:** So you already have like a standalone.

**Ademilade Shodipe-dosunmu:** You don't really have to compare this.

**Ademilade Shodipe-dosunmu:** They will be fine because it's using the templates, but you just confirm that like, oh, does this look like, what it's supposed to look like?

**Ademilade Shodipe-dosunmu:** If it does, you would save and continue.

**Ademilade Shodipe-dosunmu:** Then it would fact check.

**Ademilade Shodipe-dosunmu:** Then it will run the internal linking workflow.

**Ademilade Shodipe-dosunmu:** I just added an agentic, sorry, let just confirm.

**Ademilade Shodipe-dosunmu:** Yes, I just added an agentic internal linking workflow.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Let me see.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** So I added an agentic internal linking workflow.

**Ademilade Shodipe-dosunmu:** And I'm trying to, I'm suggesting it anyways, but, for it up.

**Ademilade Shodipe-dosunmu:** you

**Ademilade Shodipe-dosunmu:** Apparently, it probably isn't working the best, yeah, because it's linking to specific, for example, to this keyword, one-click foreign registrations, ideally it's supposed to link to design service for foreign registrations, but it's to that, so I guess the agentic one isn't doing the best of work, so it is just one of the manual checks you'll have to do.

**Ademilade Shodipe-dosunmu:** Anyways, after it adds internal links, it will generate meta descriptions, so you'll just take a look at these, whether they fit, usually they're fine, maybe you just have to change the date, this should be 2026, and you save, you just copy all of these, you copy them into these two fields, right, for Airtable, then after that, it will generate cover images, so at this point, So this is very important, with like this pipeline, I think

**Ademilade Shodipe-dosunmu:** They have started automated publishing, I think, but they have not sent me any message that's ready.

**Ademilade Shodipe-dosunmu:** So we try not to automatically publish.

**Ademilade Shodipe-dosunmu:** Currently, it's on automatic execution.

**Ademilade Shodipe-dosunmu:** If you leave it on automatic execution after its richness generates blah, blah, blah points, it's going to run all the way to publishing.

**Ademilade Shodipe-dosunmu:** So it's just going to publish the article like that to the client's website, and we don't want that.

**Ademilade Shodipe-dosunmu:** We want situations where we can control when we want to publish, you understand?

**Ademilade Shodipe-dosunmu:** So every time when we choose this generate SEO tags, I turn it off from automatic execution.

**Ademilade Shodipe-dosunmu:** And what this allows me to do is that it allows me to validate each step from here.

**Ademilade Shodipe-dosunmu:** So I would just save and continue.

**Ademilade Shodipe-dosunmu:** I'm fine with this, and it would generate the cover image, and I'll start that.

**Ademilade Shodipe-dosunmu:** So while we're generating the cover image here, we just wait for that to generate.

**Ademilade Shodipe-dosunmu:** It takes like a minute.

**Ademilade Shodipe-dosunmu:** It

**Ademilade Shodipe-dosunmu:** Right, so at this point, do you have any questions with like the process for asking Jen for the same so far?

**Ademilade Shodipe-dosunmu:** Yeah, I'm just curious for the images.

**Pamela Weber:** So the document has the text.

**Pamela Weber:** So how do the images get to the client?

**Pamela Weber:** it?

**Pamela Weber:** Great, good question.

**Ademilade Shodipe-dosunmu:** There's a space for images in Webflow as well.

**Ademilade Shodipe-dosunmu:** I mean, sorry, in the air table.

**Ademilade Shodipe-dosunmu:** So I didn't even paste the images here and we upload them to Webflow.

**Ademilade Shodipe-dosunmu:** So typically our publisher, Suma Man, handles that.

**Ademilade Shodipe-dosunmu:** But they're trying to automate the publishing.

**Ademilade Shodipe-dosunmu:** So the idea is like just add the image here and you take care of it.

**Ademilade Shodipe-dosunmu:** But since they're trying to automate publishing, that might change.

**Ademilade Shodipe-dosunmu:** But they will send like a message when it's actually ready.

**Ademilade Shodipe-dosunmu:** And I'll let you know what you have to do and how this workflow will change at that point in time.

**Ademilade Shodipe-dosunmu:** But for now, yeah, just add the images here and you should be good to go.

**Ademilade Shodipe-dosunmu:** So, so let's check that.

**Ademilade Shodipe-dosunmu:** We could just refresh to see whether, yep, so refreshing it.

**Ademilade Shodipe-dosunmu:** It's done, so you open the cover images, and these will be the images that will be like, these images will be the backdrop, essentially, of the article, if you get what I mean.

**Ademilade Shodipe-dosunmu:** So you need to pick the ones that make the most sense, right?

**Ademilade Shodipe-dosunmu:** So I would usually like deselect all of them first and pick the ones that look good.

**Ademilade Shodipe-dosunmu:** I like this one.

**Ademilade Shodipe-dosunmu:** It's giving like file legal.

**Ademilade Shodipe-dosunmu:** I like this one as well.

**Ademilade Shodipe-dosunmu:** We'll add one more of these.

**Ademilade Shodipe-dosunmu:** I don't really like these ones.

**Ademilade Shodipe-dosunmu:** They look a bit tacky.

**Ademilade Shodipe-dosunmu:** We'll add one of these.

**Ademilade Shodipe-dosunmu:** Anyways, when you're done with that, just save and continue.

**Ademilade Shodipe-dosunmu:** It will run to the next step.

**Ademilade Shodipe-dosunmu:** And you have to do that.

**Ademilade Shodipe-dosunmu:** So while that is running, remember that this is the final article you're going to take.

**Ademilade Shodipe-dosunmu:** So it's this one here.

**Ademilade Shodipe-dosunmu:** So what you would do is that you would copy this.

**Ademilade Shodipe-dosunmu:** So

**Ademilade Shodipe-dosunmu:** Or if you prefer, however you prefer, you could paste it to Markdown.

**Ademilade Shodipe-dosunmu:** You already know how to like, you know how to paste for Markdown into your Google Doc already, just to confirm.

**Pamela Weber:** No, is it just the same thing, that little copy icon?

**Ademilade Shodipe-dosunmu:** Okay, so like, you copy this, then, if you open a Google Doc, let's just, in a random Google Doc, you would have to right click, then paste from Markdown.

**Ademilade Shodipe-dosunmu:** So, for example, if I just like, paste it like this, it's going to appear with all these asterisks, and like, this is how you think it's going to appear.

**Ademilade Shodipe-dosunmu:** Yeah, so like, but if you, paste from Markdown, it's going to appear formatted properly.

**Ademilade Shodipe-dosunmu:** The thing you have to do at this point is change these dashes to actual bullets, then maybe add space before.

**Ademilade Shodipe-dosunmu:** Go on after paragraph, then eliminate any double spaces, and it should be good to go.

**Ademilade Shodipe-dosunmu:** just, you know, light stuff, honestly, just to make sure this is clean.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Takes like a minute or less to do all these.

**Ademilade Shodipe-dosunmu:** Yep, yeah, good to go from here.

**Ademilade Shodipe-dosunmu:** Yep, so from here, you can, like, start editing the article for, you know, adding internal links, removing links that don't make sense.

**Ademilade Shodipe-dosunmu:** For example, here, Descend Provider Registered Agent Services, this should take you to, ideally, this should be to Descend's Registered Agent Service, which is this landing page.

**Ademilade Shodipe-dosunmu:** So this should be the page that should get linked there.

**Ademilade Shodipe-dosunmu:** So maybe, you know, updating that link, edit that link, and that's good.

**Ademilade Shodipe-dosunmu:** You know, checking out the links, making sure they're good.

**Ademilade Shodipe-dosunmu:** Reading the articles for flow and all of that.

**Ademilade Shodipe-dosunmu:** But the great thing about this,

**Ademilade Shodipe-dosunmu:** The pipeline is so good that if you get your templates right, that's like a PSEO template that you put into Atlas, if you get that template right and you align it properly, those are easy from outside when they leave the pipeline.

**Ademilade Shodipe-dosunmu:** The edits are just remedial, so you probably just have to add in some external links and some internal links and just like adjust languages to A-V places.

**Ademilade Shodipe-dosunmu:** I usually spend like 15 to 20 minutes on this analysis, but sometimes five minutes if there's not that much to do.

**Ademilade Shodipe-dosunmu:** So yeah, it's really good.

**Ademilade Shodipe-dosunmu:** You would have to add all the external links for each of these clients.

**Ademilade Shodipe-dosunmu:** So obviously discern, you add the links to discern here.

**Ademilade Shodipe-dosunmu:** would add the link to CSC here, survivor compliance, to Northwest.

**Ademilade Shodipe-dosunmu:** So all of them honestly.

**Ademilade Shodipe-dosunmu:** And yeah, just give you like another read.

**Ademilade Shodipe-dosunmu:** Then you would compare these to...

**Ademilade Shodipe-dosunmu:** So there's already a sample.

**Ademilade Shodipe-dosunmu:** I've already generated the first article under this cluster and the clients have...

**Ademilade Shodipe-dosunmu:** As approved of it.

**Ademilade Shodipe-dosunmu:** So this is what the ask which you would look like when you're done.

**Ademilade Shodipe-dosunmu:** I left in some of the comments here so that you could take a look at like what he commented on.

**Ademilade Shodipe-dosunmu:** Right, I didn't even resolve the comments.

**Ademilade Shodipe-dosunmu:** Like I've already fixed them, but like I didn't resolve the comments.

**Ademilade Shodipe-dosunmu:** Just so that like you have like an idea of like what he commented on and how we can work on it moving forward.

**Ademilade Shodipe-dosunmu:** So yeah, one click first, Shoshosh takes you to the Seren's product page.

**Ademilade Shodipe-dosunmu:** NC Formations takes you to the Seren's product page for Formations.

**Ademilade Shodipe-dosunmu:** And our report takes you to the Seren's product page for that.

**Ademilade Shodipe-dosunmu:** Franchise Tax takes you to our resource page for Franchise Tax for Delaware and all of that.

**Ademilade Shodipe-dosunmu:** So yeah, that's honestly the approach with these articles.

**Ademilade Shodipe-dosunmu:** Yep, and you should be good to go.

**Pamela Weber:** That's the client commenting there?

**Ademilade Shodipe-dosunmu:** Yeah, it is the client's comment in there, yeah.

**Ademilade Shodipe-dosunmu:** Okay, got it.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** All right, so let's go back to our pipeline and see where we're at.

**Ademilade Shodipe-dosunmu:** I think we're in this pipeline, so we're in test pipeline.

**Ademilade Shodipe-dosunmu:** Yeah, so final cover images, you would see that, like, when we're inside the pipeline, it was showing, like, four minutes or something, but, like, it's showing for five seconds.

**Ademilade Shodipe-dosunmu:** So sometimes, like, UI bugs, you just have to refresh it, you go out and come back in.

**Ademilade Shodipe-dosunmu:** So final cover images are here.

**Ademilade Shodipe-dosunmu:** Let's see how they look.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I guess, like, this one, the rocket got cut out, so I probably wouldn't want to use this or this.

**Ademilade Shodipe-dosunmu:** I think this one is fine.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So what we'll do in this case will be you would save this image, right?

**Ademilade Shodipe-dosunmu:** Let's see downloads.

**Ademilade Shodipe-dosunmu:** Save this image.

**Ademilade Shodipe-dosunmu:** about 332 kilobytes.

**Ademilade Shodipe-dosunmu:** That's a bit large for Webflow, and we don't want the pages to lose.

**Ademilade Shodipe-dosunmu:** So ideally, these images, none of them should be over 200 kilobytes, because it does add up.

**Ademilade Shodipe-dosunmu:** So what I do is that I just go to this, I love IMG page, and I compress them.

**Ademilade Shodipe-dosunmu:** We're trying to add a compression workflow to our image gen.

**Ademilade Shodipe-dosunmu:** That's not been added.

**Ademilade Shodipe-dosunmu:** I asked them to do that months ago, but that hasn't been done yet.

**Ademilade Shodipe-dosunmu:** So I may resurface that.

**Ademilade Shodipe-dosunmu:** But this just takes like half a minute, and I download the images.

**Ademilade Shodipe-dosunmu:** It's 37 kilobytes.

**Ademilade Shodipe-dosunmu:** So when that's done, I just come here.

**Ademilade Shodipe-dosunmu:** And I put the image here in, I put the image here in, what do you call it, in Airtable.

**Ademilade Shodipe-dosunmu:** Then meta title, I would come to my test workflow, go to the meta tags, okay.

**Ademilade Shodipe-dosunmu:** And I will take my meta description.

**Ademilade Shodipe-dosunmu:** I'll put it here.

**Ademilade Shodipe-dosunmu:** If I want to make any changes, I will make.

**Ademilade Shodipe-dosunmu:** But I think this is pretty fine.

**Ademilade Shodipe-dosunmu:** Come here as well.

**Ademilade Shodipe-dosunmu:** Take my meta title.

**Ademilade Shodipe-dosunmu:** So once you have meta data.

**Ademilade Shodipe-dosunmu:** All of these, and you're finishing editing your article, you're good to go.

**Ademilade Shodipe-dosunmu:** So ideally, what you would do in this situation, because for now, you are sending me the articles to review.

**Ademilade Shodipe-dosunmu:** So what you would do in this situation is that you would go to here, for the corresponding article here, you would paste the link here, and make sure it's a chip.

**Ademilade Shodipe-dosunmu:** So ideally, it would probably look like this.

**Ademilade Shodipe-dosunmu:** Then you use Fath, put it as a chip.

**Ademilade Shodipe-dosunmu:** Okay, then you would, instead of good to go, you would put ready for review here.

**Ademilade Shodipe-dosunmu:** And you would just let me know that, oh, hey, Ademilade Shodipe-to-for-review, it's already on the spreadsheet.

**Ademilade Shodipe-dosunmu:** All right?

**Ademilade Shodipe-dosunmu:** And here, you would put it as, you would change the status of Masculent Gen to growthx editing.

**Ademilade Shodipe-dosunmu:** Right, and I'll find it.

**Ademilade Shodipe-dosunmu:** Because if you didn't want, however, when you take over the account, nobody's reviewing your work, do you understand?

**Ademilade Shodipe-dosunmu:** So it would immediately go from growthx editing.

**Ademilade Shodipe-dosunmu:** Thanks.

**Ademilade Shodipe-dosunmu:** So And I'd

**Ademilade Shodipe-dosunmu:** So maybe I'll change the name of this holiday in backlog to just maybe Buffer Articles.

**Ademilade Shodipe-dosunmu:** So it's a move to Buffer Articles, or it's a move to Ready for Staging.

**Ademilade Shodipe-dosunmu:** If you want to send it immediately to the publisher, you just put it as Ready for Staging.

**Ademilade Shodipe-dosunmu:** I like to send it to the publisher in batches, so I wouldn't send it one by one.

**Ademilade Shodipe-dosunmu:** So I'll wait until I've done like 10 or 5 of them, and I'll send it all at once to him.

**Ademilade Shodipe-dosunmu:** So after I've sent it, after I've put it in Ready for Staging for the publisher, what I would do is I would go into Linear.

**Ademilade Shodipe-dosunmu:** Have you used Linear before?

**Ademilade Shodipe-dosunmu:** Just want to confirm.

**Ademilade Shodipe-dosunmu:** No.

**Ademilade Shodipe-dosunmu:** But, hey, pretty easy to use.

**Ademilade Shodipe-dosunmu:** All I would do here is that I would.

**Ademilade Shodipe-dosunmu:** So there's already a discern ticket.

**Ademilade Shodipe-dosunmu:** It is recurring.

**Ademilade Shodipe-dosunmu:** I set it to come up every week.

**Ademilade Shodipe-dosunmu:** So you don't have to post a new ticket for the Saturday week, right?

**Ademilade Shodipe-dosunmu:** He has all the details here for him, and he knows what to do.

**Ademilade Shodipe-dosunmu:** So what I would do would be to go to the ticket.

**Ademilade Shodipe-dosunmu:** This should be the ticket for this week because it always comes back up.

**Ademilade Shodipe-dosunmu:** So you would get the ticket for the actual week and you would just honestly tag him here.

**Ademilade Shodipe-dosunmu:** So maybe add Sulaiman, I've added six articles or blah, blah, blah, right?

**Ademilade Shodipe-dosunmu:** And you would send him a message here.

**Ademilade Shodipe-dosunmu:** Then you would copy this at the beginning of the week.

**Ademilade Shodipe-dosunmu:** would copy this URL of the ticket and you would go into Slack, go into the internal channel, and you would send a message like this to him.

**Ademilade Shodipe-dosunmu:** So, hey, here's the six publishing tickets all refreshed on our table.

**Ademilade Shodipe-dosunmu:** So I was able to send that everything is on our table because I had already sent him all the answers for the week from Monday, right?

**Ademilade Shodipe-dosunmu:** Because I was one week ahead, so I just send him.

**Ademilade Shodipe-dosunmu:** But if you're not ahead, you would say something that looks like this.

**Ademilade Shodipe-dosunmu:** trying to find a regular one.

**Ademilade Shodipe-dosunmu:** So maybe something else, like, okay, hey, I've added the first articles for the week, first nine articles for the week, shares the tickets, and you send that to him, and you will get the tickets.

**Ademilade Shodipe-dosunmu:** Then in a thread here, as you add more articles for staging, just let him know, hey, more articles are added, and then the final batch, and you're good to go.

**Ademilade Shodipe-dosunmu:** Does that make sense?

**Pamela Weber:** Yeah, so when you go in linear, and you're tagging him, he will go back to Airtable to find it.

**Pamela Weber:** that?

**Pamela Weber:** Yeah, yeah, yeah.

**Pamela Weber:** You're not putting anything in linear, you're just tagging him.

**Pamela Weber:** Okay, got it.

**Pamela Weber:** Yeah, you don't just tag it in.

**Ademilade Shodipe-dosunmu:** Because he knows that he just has to go to the content OS, then he will go to ready to stage, then he will see all the articles he's supposed to stage here.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** And that's pretty much it.

**Ademilade Shodipe-dosunmu:** Great.

**Ademilade Shodipe-dosunmu:** So after this, for the sale, the next step is local updates.

**Ademilade Shodipe-dosunmu:** So, are you familiar with Luker?

**Ademilade Shodipe-dosunmu:** I don't know whether I need to explain from scratch or...

**Ademilade Shodipe-dosunmu:** yeah.

**Ademilade Shodipe-dosunmu:** I'm so familiar with what?

**Pamela Weber:** With Luker Studio.

**Ademilade Shodipe-dosunmu:** No.

**Pamela Weber:** Okay, great.

**Ademilade Shodipe-dosunmu:** So, what happens is that Luker Studio is just where all our performance reporting is done.

**Ademilade Shodipe-dosunmu:** This is eventually going to be moved into R-Class, but for now it's always in Google's Luker Studio.

**Ademilade Shodipe-dosunmu:** So, this is the Luker Report for T-SERN.

**Ademilade Shodipe-dosunmu:** This is where we just get our performance analytics, so, you know, we know which numbers are climbing, you know what's going on with your content, you know what's going on with LLM, disability, and all of that.

**Ademilade Shodipe-dosunmu:** In follow-up with this, for it to track and evaporate data, we need to put specific URLs for it to track.

**Ademilade Shodipe-dosunmu:** So, ideally, what happens is that every Monday, it's also added all the URLs that are published to me.

**Ademilade Shodipe-dosunmu:** Do you understand?

**Ademilade Shodipe-dosunmu:** So all the assets published from the previous food sheet, the updated on Monday.

**Ademilade Shodipe-dosunmu:** Before, there was an automation on air table that would, as soon as you put something that's published, it would automatically be updated in later.

**Ademilade Shodipe-dosunmu:** However, because of some issues with Luca and the table, the inspiration, and the fact that not everybody's air table was the same configuration, things kept breaking in the Luca dashboard.

**Ademilade Shodipe-dosunmu:** So now we have to add these things manually.

**Ademilade Shodipe-dosunmu:** What this means is that every Monday, you're going to come into resources here.

**Ademilade Shodipe-dosunmu:** You're going to go to manage added resources.

**Ademilade Shodipe-dosunmu:** Then you're going to update the article links and the clusters that were published for the week prior.

**Ademilade Shodipe-dosunmu:** You're going to update them in, this is GA4, Google Analytics.

**Ademilade Shodipe-dosunmu:** You're going to update them in Google Analytics.

**Ademilade Shodipe-dosunmu:** So you scroll all the way to, oh, by the way, there's a video that explains how to do this.

**Ademilade Shodipe-dosunmu:** I'm just going to work with you first.

**Ademilade Shodipe-dosunmu:** And that video is already linked here.

**Ademilade Shodipe-dosunmu:** go.

**Ademilade Shodipe-dosunmu:** Loopers theooxid

**Ademilade Shodipe-dosunmu:** The standard operating manual, I think, so by chance, have you seen that video?

**Ademilade Shodipe-dosunmu:** So if you go into, let me just bring that, we go into Yorco.

**Ademilade Shodipe-dosunmu:** The process of updating Lucas across clients is similar.

**Ademilade Shodipe-dosunmu:** Yorco is just a bit different.

**Ademilade Shodipe-dosunmu:** But we go to clients, operating.

**Ademilade Shodipe-dosunmu:** Yeah, so it should be in any of these client operating manuals on XP.

**Ademilade Shodipe-dosunmu:** Let me just be sure.

**Ademilade Shodipe-dosunmu:** Let me You can look at her.

**Ademilade Shodipe-dosunmu:** It's weird that the person here.

**Ademilade Shodipe-dosunmu:** It's actually very, very strange.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** I'll probably add it here, but I know it's in Yorco's.

**Ademilade Shodipe-dosunmu:** Is that the loom walking?

**Ademilade Shodipe-dosunmu:** Is that one?

**Ademilade Shodipe-dosunmu:** Yeah.-hmm.-hmm.

**Ademilade Shodipe-dosunmu:** that a Are You used to

**Ademilade Shodipe-dosunmu:** It's like a new, it's this one, so I'm going to put it, so this is new, so this is like the standard for updating procedure, so this is like the main, so just like click watch video, like it's taking to, this video that explains how to update the code.

**Ademilade Shodipe-dosunmu:** So, I advise that you watch this, before starting any local updates.

**Ademilade Shodipe-dosunmu:** We have a pretty short video, so yeah, just watch that, and then if you have like issues, like it's in the background.

**Ademilade Shodipe-dosunmu:** Could you please drop that in that link for that video?

**Pamela Weber:** I don't know if I saw it yet.

**Pamela Weber:** Okay, what meaning is that you're going to get out of the screen?

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Sad was saying.

**Ademilade Shodipe-dosunmu:** What a dick.

**Ademilade Shodipe-dosunmu:** We'll also put this into cell.

**Ademilade Shodipe-dosunmu:** yep that makes sense now all right you should be good to go but i think these different things are already the actual checkers as well so that's pretty much the flow so every Monday you would update the looker

**Ademilade Shodipe-dosunmu:** I'm just going to do processes in that video, but the idea is that you're coming into this URL field, and you're pasting the, essentially this is in like a specific code format for each client.

**Ademilade Shodipe-dosunmu:** So what you have to do is like, you have to format, this is the link, essentially, and this is the cluster.

**Ademilade Shodipe-dosunmu:** So you just have to format all the articles you have done in this exact way, do understand?

**Ademilade Shodipe-dosunmu:** So it's how you put in like, oh, this whole text, blah, blah, blah, landing page, all of this, the link, the colon, the parenthesis, the then, the inverted commas, then the name of the cluster.

**Ademilade Shodipe-dosunmu:** Does that make sense?

**Pamela Weber:** No, so you're like copying the whole line, or you're copying this whole block, like the whole page?

**Ademilade Shodipe-dosunmu:** Let me bring it in in here.

**Ademilade Shodipe-dosunmu:** For example, let's say we want to do a looker update for, let's see, this has been our web, right?

**Ademilade Shodipe-dosunmu:** So what you need is you need a link to the articles to the URL.

**Ademilade Shodipe-dosunmu:** So let's go to where the URL is.

**Ademilade Shodipe-dosunmu:** The URL is here.

**Ademilade Shodipe-dosunmu:** So you need the URL and you need the cluster, right?

**Ademilade Shodipe-dosunmu:** So the URL is this.

**Ademilade Shodipe-dosunmu:** This URL here has to be formatted in the exact way that this one is formatted in, right?

**Ademilade Shodipe-dosunmu:** So resources, blah, blah, blah, blah, blah, blah, But like, you have to reformat this particular URL.

**Ademilade Shodipe-dosunmu:** So instead of the BWDOT, it will start from resources.

**Ademilade Shodipe-dosunmu:** Does that make sense?

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Then for the cluster, it has to be in this exact format as well.

**Ademilade Shodipe-dosunmu:** Then what would be here would just be the new cluster.

**Ademilade Shodipe-dosunmu:** So in this case, the cluster has NSInformations, but for this one, the cluster has foreign registrations, right?

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So you have to do that for all the articles you publish to be required.

**Ademilade Shodipe-dosunmu:** But you do have to do that for refreshes since refreshes would have already been added a while back to the ULOCA.

**Ademilade Shodipe-dosunmu:** When did you invest for this?

**Ademilade Shodipe-dosunmu:** So you have to do that for all of them, so all 26% you have to do that for all six of them, and in your case it would be a bit more of a complex process because that one has like three different lookers you update.

**Ademilade Shodipe-dosunmu:** However, upon understanding how ridiculously tedious this process is, thank God for AI, we essentially have automated the entire process in cloud.

**Ademilade Shodipe-dosunmu:** So if you send it to cloud B, you would just go into this looker tasks here, and I've already hard-coded this to just convert it to the format.

**Ademilade Shodipe-dosunmu:** So for example, what you would do here is you would just say, for example, discern, then you would go to this air table, and you would just highlight the aspects that you published out.

**Ademilade Shodipe-dosunmu:** So for example, let's see.

**Ademilade Shodipe-dosunmu:** Let's say I published this 26 this week, right?

**Ademilade Shodipe-dosunmu:** I would copy the publish URL and the topic cluster, right?

**Ademilade Shodipe-dosunmu:** I would copy that and I would just paste it into the cloud project.

**Ademilade Shodipe-dosunmu:** So I'll just say discern, then I'll paste this here and I'll enter.

**Ademilade Shodipe-dosunmu:** And because it's hard-coded to do that, it's going to spin out the...

**Ademilade Shodipe-dosunmu:** Right, so it's going to format it already for you.

**Ademilade Shodipe-dosunmu:** So it's going to format it for GA4, that's Google Analytics.

**Ademilade Shodipe-dosunmu:** Then it's going to format it for...

**Ademilade Shodipe-dosunmu:** So it's doing this for everything.

**Ademilade Shodipe-dosunmu:** Then it's going to do that for Google Search Console as well.

**Ademilade Shodipe-dosunmu:** Format to Google Search Console.

**Ademilade Shodipe-dosunmu:** It's very easy.

**Ademilade Shodipe-dosunmu:** All you need to do at this juncture is just copy this, go into GA4.

**Ademilade Shodipe-dosunmu:** Then you would just like paste it here.

**Ademilade Shodipe-dosunmu:** Like you would paste everything here.

**Ademilade Shodipe-dosunmu:** Then you would just format the formula and you...

**Ademilade Shodipe-dosunmu:** Well, I don't want do that, so I'm just going to control Z that because I've already updated this for this week.

**Ademilade Shodipe-dosunmu:** Does that make sense?

**Ademilade Shodipe-dosunmu:** Then you would go to the same thing for search console.

**Ademilade Shodipe-dosunmu:** You go to the URL list 4, the latest one, always use the most updated one.

**Ademilade Shodipe-dosunmu:** URL list 3 is a previous one, so use the most updated one, and you would paste the links either at the bottom here before this else statement, or you can just do it after the case statement here.

**Ademilade Shodipe-dosunmu:** But yeah, that's honestly, it's, you don't really need to stress on this.

**Ademilade Shodipe-dosunmu:** This takes like two minutes.

**Ademilade Shodipe-dosunmu:** Just copy what has been published and put it here.

**Ademilade Shodipe-dosunmu:** Same goes for Diligent, same goes for Yoko.

**Ademilade Shodipe-dosunmu:** Yoko is a bit more complex, so we're going to, we'll dive into that next.

**Ademilade Shodipe-dosunmu:** Well, yeah, that is the local updates for the week.

**Ademilade Shodipe-dosunmu:** Once you've done the local updates on Monday, that's essentially the entire process.

**Ademilade Shodipe-dosunmu:** So I'll walk you through picking a topic, to generating an article, to images, to local updates.

**Ademilade Shodipe-dosunmu:** updates?

**Ademilade Shodipe-dosunmu:** So I'm

**Ademilade Shodipe-dosunmu:** The same process applies widely for most of our clients, but Yoko just has some quirks, which we can run through.

**Ademilade Shodipe-dosunmu:** But as of right now, I want to just pause for a second so you can ask any more questions that you might have because of all this.

**Pamela Weber:** No, I don't have questions now.

**Pamela Weber:** Probably once I start doing it myself, things will pop up.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** That's perfect.

**Ademilade Shodipe-dosunmu:** So that's the process.

**Ademilade Shodipe-dosunmu:** That's the Looker.

**Ademilade Shodipe-dosunmu:** Oh, yeah.

**Ademilade Shodipe-dosunmu:** For the Looker, make sure you're logged into the Teams account.

**Ademilade Shodipe-dosunmu:** It might not work for your personal account.

**Ademilade Shodipe-dosunmu:** So make sure you're logged into Teams when you're doing Looker updates because the Teams account has the necessary permissions to manage digital resources.

**Ademilade Shodipe-dosunmu:** And when I'm done with the Looker for the week, I would, I don't have to.

**Ademilade Shodipe-dosunmu:** don't to.

**Ademilade Shodipe-dosunmu:** Thank

**Ademilade Shodipe-dosunmu:** Depending on your relationship with your engagement manager, my relationship with him was that, like, he knows that I do it every Monday, so I don't have to tell him on Monday that I've done it.

**Ademilade Shodipe-dosunmu:** Like, he knows.

**Ademilade Shodipe-dosunmu:** It's only if I'm unable to do it, I'll tell him, hey, I was not able to do this, but, like, I just should be thinking, like, it takes, like, two minutes, so you shouldn't really have so much difficulty with that.

**Ademilade Shodipe-dosunmu:** So, yeah, and you rinse and repeat for each article that you're working on.

**Ademilade Shodipe-dosunmu:** That's the article gen process.

**Ademilade Shodipe-dosunmu:** Yep, so this would be the current pipeline that you should use for, what do you call it, for discern.

**Ademilade Shodipe-dosunmu:** I've already got a head to generate about nine articles, I guess.

**Ademilade Shodipe-dosunmu:** This one is done.

**Ademilade Shodipe-dosunmu:** I've edited this one already, so it's good to go.

**Ademilade Shodipe-dosunmu:** So I didn't even have to work on these other ones.

**Ademilade Shodipe-dosunmu:** So I've already generated 10.

**Ademilade Shodipe-dosunmu:** So you probably just have to maybe check the code.

**Ademilade Shodipe-dosunmu:** And we generate what needs to generate in, in terms of images, I guess, because these images are just, they're all the same cover image, so you want some variety, and then like copying this to a Google Doc, opening a Google Doc in this place, copying it there, and like completing a table, as the case may be.

**Ademilade Shodipe-dosunmu:** So for discern, I'm going to, I've already done this one, so this one is good to go, this one is on the, I'm just going to put it in the Olivier backlog for now, because it's done.

**Ademilade Shodipe-dosunmu:** But like, I'll leave it here for now, so if you need like a sample of like how it should look like once you have a few deep, necessary things, I'll just leave it here.

**Ademilade Shodipe-dosunmu:** So for now, I'm going to assign you a couple to run, so I'm going to assign you three of these to work on this week.

**Ademilade Shodipe-dosunmu:** So if I assign you this one, so these three, Power Compliance, CT Corp.

**Ademilade Shodipe-dosunmu:** So this one is what CT Corp, for tech startups, and this is for venture capital funds.

**Ademilade Shodipe-dosunmu:** So this would be similar to this for like a different focus, this one being VC funding.

**Ademilade Shodipe-dosunmu:** And I just want to make sure this fund manager has private equity.

**Ademilade Shodipe-dosunmu:** So fund manager has private equity.

**Ademilade Shodipe-dosunmu:** So this code works with this.

**Ademilade Shodipe-dosunmu:** So it's under article generation already because I've generated the articles already.

**Ademilade Shodipe-dosunmu:** So you just have to edit them and fill in the gaps and send them to me when they're ready.

**Ademilade Shodipe-dosunmu:** So this would be the first three, I suppose, that you would work on for the CERN.

**Ademilade Shodipe-dosunmu:** You already have access to the content OS, is that correct?

**Ademilade Shodipe-dosunmu:** I'm sorry, the content what?

**Pamela Weber:** The content OS.

**Ademilade Shodipe-dosunmu:** The air gaming, essentially.

**Ademilade Shodipe-dosunmu:** I don't know.

**Ademilade Shodipe-dosunmu:** I don't think so.

**Ademilade Shodipe-dosunmu:** It's so I some of going so.

**Ademilade Shodipe-dosunmu:** and that's to thing.

**Ademilade Shodipe-dosunmu:** Do

**Ademilade Shodipe-dosunmu:** Yeah, I've invited you to the server, you already have access to it, and the link to the OS is already in the client operating manual, this, let me just re-dive into your DM, this manual had everything, like operating manual, check is like, these are all the links you need to, you know, because if you open it, for example, for this, okay, this is diligent, so I was looking for discern, so for discern, you can see it's here, I guess, yep, so, yeah, links and resources at the bottom, yep, so these are reference materials, so one time, or

**Ademilade Shodipe-dosunmu:** So for all of them, you can find the content OS, the operating material, and articles samples, and probably, oh yeah, the Luka dashboard is here as well for all of them, and Atlas Workspace is here as well.

**Ademilade Shodipe-dosunmu:** Yep, you're pretty good on that.

**Ademilade Shodipe-dosunmu:** So when you open this Atlas Workspace, you know the workspace you're supposed to use for the three articles.

**Ademilade Shodipe-dosunmu:** You come to this one, this is a test I'm running, so you know this.

**Ademilade Shodipe-dosunmu:** You come to this one from competitor comparisons alternatives, and you will run a couple articles here.

**Ademilade Shodipe-dosunmu:** I've already run some of the ones that I assigned to you.

**Ademilade Shodipe-dosunmu:** So you can run the articles from scratch if you want, it doesn't matter.

**Ademilade Shodipe-dosunmu:** Or you can just edit what I've already done here.

**Ademilade Shodipe-dosunmu:** So anything that floats your boat, to be honest.

**Ademilade Shodipe-dosunmu:** I will walk you through, later I will walk you through like, how we create templates for programmatic pipelines.

**Ademilade Shodipe-dosunmu:** I think some of your training earlier would have been like, how to operate pipelines and all of that.

**Ademilade Shodipe-dosunmu:** I will walk you through how we essentially create new pipelines for different clusters.

**Ademilade Shodipe-dosunmu:** a bit an back.

**Ademilade Shodipe-dosunmu:** I'll walk you through that maybe next week.

**Ademilade Shodipe-dosunmu:** Does that sound fine?

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Sorry if this is like a lot I want, but like you do build muscle memory for it as you go.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Trying to figure out what next I've to cover.

**Ademilade Shodipe-dosunmu:** I've covered all of this.

**Ademilade Shodipe-dosunmu:** I've told you what you need to look out for for editing.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** So for your call, yeah, so we can actually do some stuff in your call right now.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So this was, I was editing a pipeline here.

**Ademilade Shodipe-dosunmu:** It is another pipeline I want to edit.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So let's close discern for now.

**Ademilade Shodipe-dosunmu:** If you have questions for me to ask, well, I've assigned you those three already and your name's on them.

**Ademilade Shodipe-dosunmu:** But I'm just going to put this in your DM so you know what you're doing when you open your table.

**Ademilade Shodipe-dosunmu:** I'll add seconds for the week.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** let's close week.

**Ademilade Shodipe-dosunmu:** So let's So let's So let's

**Ademilade Shodipe-dosunmu:** So I probably will get you to do one diligence.

**Ademilade Shodipe-dosunmu:** don't know if Panzer is going to agree on that.

**Ademilade Shodipe-dosunmu:** So if you're able to do these three this week, then maybe two from your call, then one from the agenda should be fine.

**Ademilade Shodipe-dosunmu:** Does that seem like a fair work or does that seem to not on you?

**Ademilade Shodipe-dosunmu:** It's just like getting blood check.

**Pamela Weber:** Well, just for the short week, I could probably do it.

**Pamela Weber:** There's a holiday in there, but yeah.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** These three shouldn't take so much time.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So So

**Ademilade Shodipe-dosunmu:** might take a bit more time on this, I'll probably give you two of these, maybe one new and one refreshed, and maybe just one of these, but diligent, like you don't have to get it done this week, because like it's still pending, you probably get it done like earlier next week, that's fine.

**Ademilade Shodipe-dosunmu:** Okay, let's move on to Yurko and see.

**Ademilade Shodipe-dosunmu:** Just what's going on there.

**Ademilade Shodipe-dosunmu:** Oh, darn.

**Ademilade Shodipe-dosunmu:** Okay, I sent you an invite to the, um, to the content planner, so you can, you'll be able to, you know, access that there.

**Ademilade Shodipe-dosunmu:** In your mail, so let's just go into Yurko.

**Ademilade Shodipe-dosunmu:** Yurko's a bit trickier in terms of like, what they want, that, I don't know, it's like the typical low-paying clients that just like want so much more stuff, so, um, You'll all known for it.

**Ademilade Shodipe-dosunmu:** You know, you get into it, there's like a ton of stuff to do.

**Ademilade Shodipe-dosunmu:** If you look into, like, the internal channel for Yoko.

**Ademilade Shodipe-dosunmu:** So if you go into the internal channel for Yoko, you'd see that, like, you check this is, like, significantly more than, like, other clients because of...

**Ademilade Shodipe-dosunmu:** She just wants us to do so many housekeeping things.

**Ademilade Shodipe-dosunmu:** Sorry, excuse me.

**Ademilade Shodipe-dosunmu:** It doesn't get me a tired.

**Ademilade Shodipe-dosunmu:** I've been talking nonstop on...

**Ademilade Shodipe-dosunmu:** Sorry, give me a second.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** So, like, it's, like, a ton of stuff here.

**Ademilade Shodipe-dosunmu:** But some of the major things would be to run a site audit.

**Ademilade Shodipe-dosunmu:** Have you run a site audit in SEMrush before?

**Ademilade Shodipe-dosunmu:** No.

**Pamela Weber:** I've just used it for keyword research.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Too simple, I can show you that sometime, but Vivek has been doing this so far, so, but I think I did this one this week, though, because he's out of office, so I had to do it for him.

**Ademilade Shodipe-dosunmu:** Just to be sure, have you gone through, like, the client operating manual for your call already?

**Ademilade Shodipe-dosunmu:** So that would be this one.

**Ademilade Shodipe-dosunmu:** No.

**Ademilade Shodipe-dosunmu:** Okay, you're going to go through the operating manual, okay.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So, you would need to go through that, and the interaction question, like, a bunch of videos that explain different parts of the workflow.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So, we need to go through those first.

**Ademilade Shodipe-dosunmu:** Like, the idea of this, like, ideally, like, what I was even asked to do was just to meet with you for, like, an hour and give you all this documentation, and you also go through them and watch the videos.

**Ademilade Shodipe-dosunmu:** And once you've done that, I can now, like, give you more guided instructions.

**Ademilade Shodipe-dosunmu:** But, here's what we'll do.

**Ademilade Shodipe-dosunmu:** Because of time.

**Ademilade Shodipe-dosunmu:** time.

**Ademilade Shodipe-dosunmu:** So, let's just make sure that we're able to nail article generation, right?

**Ademilade Shodipe-dosunmu:** Let's just make sure we're able to nail it first.

**Ademilade Shodipe-dosunmu:** So, I'm going to, this, the link to this area table is in the, it's in the editorial checklist as well.

**Ademilade Shodipe-dosunmu:** So, let me just make sure you're added here.

**Ademilade Shodipe-dosunmu:** Let me invite you to this.

**Ademilade Shodipe-dosunmu:** Yep, you already have access to this, so you're good to go.

**Ademilade Shodipe-dosunmu:** So, yeah, so, what you need to do is, like, I'll do a proper work through later on, like, what all of these things mean.

**Ademilade Shodipe-dosunmu:** Prior week, next week, all of that.

**Ademilade Shodipe-dosunmu:** I would also send you links to some videos.

**Ademilade Shodipe-dosunmu:** So, I have, like, I think I linked this as well.

**Ademilade Shodipe-dosunmu:** See, there's some resources here.

**Ademilade Shodipe-dosunmu:** This was a call I had with Joseph.

**Ademilade Shodipe-dosunmu:** It was a former ME on this account.

**Ademilade Shodipe-dosunmu:** There's a loom that explains, there's an audit sheet.

**Ademilade Shodipe-dosunmu:** There's a loom.

**Ademilade Shodipe-dosunmu:** The that, you want to watch that.

**Ademilade Shodipe-dosunmu:** The Loom that like of us, like Carrie was explaining, that was the previous manager for user account, was explaining a couple of things.

**Ademilade Shodipe-dosunmu:** So I put the Loom there.

**Ademilade Shodipe-dosunmu:** This is the local updates.

**Ademilade Shodipe-dosunmu:** And I had a single carry, but this was like, okay, this was like admin tasks, don't worry about this one.

**Ademilade Shodipe-dosunmu:** All right, so you need to just go to the operating manual.

**Ademilade Shodipe-dosunmu:** This is also linked in your Google, I'll just add this to you.

**Ademilade Shodipe-dosunmu:** I'll just send this as a message to you.

**Ademilade Shodipe-dosunmu:** In case you need to, it's like my personal prompts and resources for this client.

**Ademilade Shodipe-dosunmu:** Like I said, I just took over the account, so I'm still a bit new to it.

**Ademilade Shodipe-dosunmu:** Well, so far, I've done like two weeks of content, and the client hasn't had any complaints with quality of content, so I would say that like here in a decent spot.

**Ademilade Shodipe-dosunmu:** All right, so if look at this, you'll see articles in priority for next week.

**Ademilade Shodipe-dosunmu:** I'm already handing all of these.

**Ademilade Shodipe-dosunmu:** These are articles that we're expected to deliver next week.

**Ademilade Shodipe-dosunmu:** I've generated all of them already.

**Ademilade Shodipe-dosunmu:** I'm just editing them today, so I'll done with all of these today.

**Ademilade Shodipe-dosunmu:** So you essentially have one week of content, and I'm giving you a one week of our content, do understand?

**Ademilade Shodipe-dosunmu:** So that next week, you don't have to deliver anything per se.

**Ademilade Shodipe-dosunmu:** You can just spend time like understanding more and more of like article generation processes and all of that.

**Ademilade Shodipe-dosunmu:** But, yeah, but this is where you're going to start from, these two weeks out.

**Ademilade Shodipe-dosunmu:** So I'm going to assign you two articles here.

**Ademilade Shodipe-dosunmu:** So this is on that production with production priority view.

**Ademilade Shodipe-dosunmu:** So there are just like a lot of things with like this article.

**Ademilade Shodipe-dosunmu:** And I would have to walk you through this has to be a separate call for your workers.

**Ademilade Shodipe-dosunmu:** It's just like so much stuff.

**Ademilade Shodipe-dosunmu:** But yeah, for now, go to the operating manual and watch the videos there.

**Ademilade Shodipe-dosunmu:** And once you're done with that and you have questions, I will answer those.

**Ademilade Shodipe-dosunmu:** So yeah, and I will assign you two articles to work on for you as well.

**Ademilade Shodipe-dosunmu:** So I will send you one new article and yeah, so I'll send you this one, Mastering Internal Engagements.

**Ademilade Shodipe-dosunmu:** The articles for Europe are typically around like 1.6 to 1.8, so you should look at improving strategies for HR leaders.

**Ademilade Shodipe-dosunmu:** So this is a brand new article, so we are working on it from scratch.

**Ademilade Shodipe-dosunmu:** For the process on how to execute this, just watch the videos.

**Ademilade Shodipe-dosunmu:** in the operating manner, there's a video on like the article generation process.

**Ademilade Shodipe-dosunmu:** But the process is pretty much like this.

**Ademilade Shodipe-dosunmu:** Let me bring this.

**Ademilade Shodipe-dosunmu:** Process is pretty much.

**Ademilade Shodipe-dosunmu:** Asking Claude or maybe Perplexity to make you an optimized SEO outline and give you some information.

**Ademilade Shodipe-dosunmu:** So this is the prompt that I usually use here.

**Ademilade Shodipe-dosunmu:** So I'll just say, oh, hey, make me a detailed outline for an article title.

**Ademilade Shodipe-dosunmu:** I'll put the title.

**Ademilade Shodipe-dosunmu:** I'll put the primary keyword.

**Ademilade Shodipe-dosunmu:** I'll put the target audience.

**Ademilade Shodipe-dosunmu:** I'll put the pain points.

**Ademilade Shodipe-dosunmu:** So the pain points on your code is indicated by this.

**Ademilade Shodipe-dosunmu:** So this is the cluster of pain points.

**Ademilade Shodipe-dosunmu:** So I'll put the pain points and it's already filled for you.

**Ademilade Shodipe-dosunmu:** And I'll put the subcluster or use case as well in the prompts.

**Ademilade Shodipe-dosunmu:** Use your use case to include.

**Ademilade Shodipe-dosunmu:** And I'll put any additional context.

**Ademilade Shodipe-dosunmu:** So additional context here would be this.

**Ademilade Shodipe-dosunmu:** You would see there's an assignments column.

**Ademilade Shodipe-dosunmu:** So you would see, you can see my screen.

**Ademilade Shodipe-dosunmu:** would see this.

**Ademilade Shodipe-dosunmu:** So this is the additional context that I'll put here.

**Ademilade Shodipe-dosunmu:** So once I have this, going to generate like an outline for me.

**Ademilade Shodipe-dosunmu:** Then I'll pop into Atlas.

**Ademilade Shodipe-dosunmu:** So once it generates, so if you read this message.

**Ademilade Shodipe-dosunmu:** Also.

**Ademilade Shodipe-dosunmu:** So do you have access to the Port B Cloud Pro?

**Ademilade Shodipe-dosunmu:** I don't know.

**Pamela Weber:** I don't, I haven't even been to Cloud.

**Pamela Weber:** I've been before the test and onboarding stuff.

**Pamela Weber:** Where do you find Cloud?

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Um, you just, let me just send you a link.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** But you should have logins.

**Ademilade Shodipe-dosunmu:** If you don't have access to Port B, I would ping Youssef about it.

**Ademilade Shodipe-dosunmu:** But like he's not, I think he's out of office.

**Ademilade Shodipe-dosunmu:** I don't know.

**Ademilade Shodipe-dosunmu:** But I would ping Youssef about it.

**Ademilade Shodipe-dosunmu:** So your code, you always start to Cloud?

**Pamela Weber:** You don't go just start to Atlas?

**Ademilade Shodipe-dosunmu:** Um, yeah.

**Ademilade Shodipe-dosunmu:** So, Cloud helps for the outline.

**Ademilade Shodipe-dosunmu:** But like, we also use Atlas.

**Ademilade Shodipe-dosunmu:** But like, I was going to explain how that works.

**Ademilade Shodipe-dosunmu:** Yeah, I'll just add the Cloud Charts here so that you know what's going on.

**Ademilade Shodipe-dosunmu:** If you can access this link, let me know.

**Ademilade Shodipe-dosunmu:** So what happens is that like, after I do this in Cloud, I get like an optimized outline, then I edit the outline to see, you know, if it makes sense to me, right?

**Ademilade Shodipe-dosunmu:** Then from this outline, I ask it to create an assignment direction.

**Ademilade Shodipe-dosunmu:** So I'll just say, oh, hey, based on the above, create an assignment direction similar to this, then I give it an assignment direction that I've created in the past.

**Ademilade Shodipe-dosunmu:** So for this, you can just use an example from any of these.

**Ademilade Shodipe-dosunmu:** So these are your code spec plans.

**Ademilade Shodipe-dosunmu:** So this is the one you're supposed to use.

**Ademilade Shodipe-dosunmu:** This one that says article check.

**Ademilade Shodipe-dosunmu:** So I'll just ask it to, you know, use one of these.

**Ademilade Shodipe-dosunmu:** Then when I'm done, I will come in here.

**Ademilade Shodipe-dosunmu:** Wait, one second.

**Ademilade Shodipe-dosunmu:** For let's see if that's all up.

**Pamela Weber:** What was the step between the Cloud and then, and that green box where you were in Atlas?

**Pamela Weber:** Did you enter it there?

**Ademilade Shodipe-dosunmu:** How did it get from there to there?

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So once I have the outline here, I'm going to add.

**Ademilade Shodipe-dosunmu:** Ask AdCloud to create an assignment direction based on an example and based on this outline, right?

**Ademilade Shodipe-dosunmu:** So once it gives me this assignment direction, I edit it to make sure it makes sense.

**Ademilade Shodipe-dosunmu:** For example, this is saying 2,500 words, and we want about 1,500 to 1,800 words, so I will edit that, and anything else that makes sense.

**Ademilade Shodipe-dosunmu:** Then I will paste this assignment direction, will go from here, I will take it to Atlas from here.

**Ademilade Shodipe-dosunmu:** So I will go here to Atlas.

**Ademilade Shodipe-dosunmu:** In the input, will put your code as a fact-check domain, will put your code as an internal link site, I will put the topic, then I will just paste it in the assignment direction here.

**Ademilade Shodipe-dosunmu:** Then it will generate a brief.

**Ademilade Shodipe-dosunmu:** After generating the brief, what I will do is I will scroll into the brief, I will come to the proposed content structure.

**Ademilade Shodipe-dosunmu:** For this entire content structure, I am going to delete the entire outline that it gives me because each year doesn't give you a outline.

**Ademilade Shodipe-dosunmu:** Then I will paste

**Ademilade Shodipe-dosunmu:** Here's the outline I already created using Claude here.

**Ademilade Shodipe-dosunmu:** So this is the entire outline.

**Ademilade Shodipe-dosunmu:** Let me look for, for example, this is the entire outline here from Claude.

**Ademilade Shodipe-dosunmu:** So it can be Claude, can be ChatGPT, it can be Perplexity.

**Ademilade Shodipe-dosunmu:** All three of them work well for outlines, but I just prefer Claude.

**Ademilade Shodipe-dosunmu:** So I'll paste this entire outline that I from Claude.

**Ademilade Shodipe-dosunmu:** Obviously I would have edited it and all of that, but I'll paste, except the SEO notes.

**Ademilade Shodipe-dosunmu:** I'll paste this entire outline here.

**Ademilade Shodipe-dosunmu:** Oh, and also this internal link recommendations, I'll remove that.

**Ademilade Shodipe-dosunmu:** I'll stop our FAQs.

**Ademilade Shodipe-dosunmu:** So I'll this entire outline, delete this entire section here and paste it instead.

**Ademilade Shodipe-dosunmu:** So I'll go to the proposed content structure and just delete everything here and paste my own outline instead.

**Ademilade Shodipe-dosunmu:** Then I will run the pipeline.

**Ademilade Shodipe-dosunmu:** So the pipeline will research, to do an outline, to do a drafts, to fact check, do some internal links, generate tags, and give you an output when it's done.

**Ademilade Shodipe-dosunmu:** So now for this output, what I do when it reaches this output.

**Ademilade Shodipe-dosunmu:** It's really simple.

**Ademilade Shodipe-dosunmu:** I copied the entire output here.

**Ademilade Shodipe-dosunmu:** There's some things that don't just sit around with me, like with this output and all.

**Ademilade Shodipe-dosunmu:** But thankfully, we have an editorial checklist in Yorkel.

**Ademilade Shodipe-dosunmu:** So what I would do at this point would be, I would paste this article here, run this article through our editorial checklist.

**Ademilade Shodipe-dosunmu:** And Yorkel's product capabilities.

**Ademilade Shodipe-dosunmu:** So I'll just do that.

**Ademilade Shodipe-dosunmu:** And it would run through the entire flow.

**Ademilade Shodipe-dosunmu:** As it's doing that, for example, let's say this is the one you're working on.

**Ademilade Shodipe-dosunmu:** Mushroom, blah, blah, blah, blah, blah.

**Ademilade Shodipe-dosunmu:** I would only say add the Google Doc link here.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** No.

**Ademilade Shodipe-dosunmu:** I would add, there's a place for metadata, so I think it's low.

**Ademilade Shodipe-dosunmu:** That's just all, I'm looking for you.

**Ademilade Shodipe-dosunmu:** Yeah, metadata, metadata, description should be here.

**Ademilade Shodipe-dosunmu:** Then cover image.

**Ademilade Shodipe-dosunmu:** So cover image, you get them from Unsplash.

**Ademilade Shodipe-dosunmu:** All this is in the client operating manual, so I don't feel like you need to, like, memorize all of this.

**Ademilade Shodipe-dosunmu:** I'm just walking you through, so you have, like, a recording to the client.

**Ademilade Shodipe-dosunmu:** So, you get an image from here.

**Ademilade Shodipe-dosunmu:** The image size should be 1920 by 1280.

**Ademilade Shodipe-dosunmu:** This is, like, the minimum size.

**Ademilade Shodipe-dosunmu:** So you just get that, and you paste it there.

**Ademilade Shodipe-dosunmu:** So we have, like, an Unsplash premium account, so we use Unsplash from your phone.

**Ademilade Shodipe-dosunmu:** We don't generate images for them.

**Ademilade Shodipe-dosunmu:** Put image there.

**Ademilade Shodipe-dosunmu:** And go back to Claude to see if...

**Ademilade Shodipe-dosunmu:** Yeah, so it's been running these guys through.

**Ademilade Shodipe-dosunmu:** It's doing the checks.

**Ademilade Shodipe-dosunmu:** It's telling that, you know, server-need revision, actually overuse, internal lease extension, formatting, it's just talking like a lot of issues, the product capabilities, statistics verification, doing that as well, and all.

**Ademilade Shodipe-dosunmu:** So, I'll say yes, create a revised version, and it's going to run the editing checklist, and create, it's going to create a revised version of the article for you, which will paste into a Google Doc, and run your final edits, so during your final edits, you would add internal links, you would check product capabilities, you would break up the text, use your bullets where you need bullets, and just, you know, obviously, edit it to your own capabilities, while you're editing a user.

**Ademilade Shodipe-dosunmu:** So if you go to the YoCo site, you can always use these articles as benchmarks for how the article is supposed to be, like, here you see, oh, hey, we don't put it in the introduction, so you obviously know, no links you can in the introduction, right?

**Ademilade Shodipe-dosunmu:** You know, verify statistics, the types of sources that we use and all of that.

**Ademilade Shodipe-dosunmu:** And this is actually another thing we will have to do with YoCo.

**Ademilade Shodipe-dosunmu:** We will have to add external links.

**Ademilade Shodipe-dosunmu:** The workflow doesn't always give the best external links, so we will have to source for some of these.

**Ademilade Shodipe-dosunmu:** There's, you know, there's this thing about, like, texting.

**Ademilade Shodipe-dosunmu:** The 98% huge rate of SMS texts.

**Ademilade Shodipe-dosunmu:** We have four resources for this statistic.

**Ademilade Shodipe-dosunmu:** All of this is in decline at the Zimano, by the way.

**Ademilade Shodipe-dosunmu:** And, yeah, for these images, I think she added this herself, so that's what I guess.

**Ademilade Shodipe-dosunmu:** But yeah, that's honestly the divide for this.

**Ademilade Shodipe-dosunmu:** Then for the links, for the conclusion, there are, there's a link for the demo, there's a link for those.

**Ademilade Shodipe-dosunmu:** It's the same one for each article.

**Ademilade Shodipe-dosunmu:** This city is like relatively the same for every article.

**Ademilade Shodipe-dosunmu:** We just make tiny adjustments from time to time.

**Ademilade Shodipe-dosunmu:** Well, yeah, that's basically what it's for content-gen.

**Ademilade Shodipe-dosunmu:** So once you ask Claude to do all of this, it's a creative document, creating the details, and you just adjust it from there.

**Ademilade Shodipe-dosunmu:** Make sure it's compared with the standards and the blogs and, you know, ask any questions if any questions.

**Ademilade Shodipe-dosunmu:** But yeah, that's how you all put it up, reaching a net in your article.

**Ademilade Shodipe-dosunmu:** So, for context, Lisa has to do some stuff, so that's I find out.

**Ademilade Shodipe-dosunmu:** Thank Thank you.

**Ademilade Shodipe-dosunmu:** These guys, I spent about 20 minutes on them after they gave that class.

**Ademilade Shodipe-dosunmu:** yeah, it doesn't really take a lot of long, but like you are just starting to say, think you're going to have that.

**Ademilade Shodipe-dosunmu:** So don't worry about it, you're taking 30 minutes or even more, or an hour, because it's like the first one.

**Ademilade Shodipe-dosunmu:** I the first yoga class could have been hard to do, but like subsequently wants to spend 20 minutes, because I really want to spend everything.

**Ademilade Shodipe-dosunmu:** So yeah, that's honestly, it's for Nuka updates and for Nuka updates, for staging and publishing, when you're doing an article, we need to have a separate point of this.

**Ademilade Shodipe-dosunmu:** It's a pretty irritating client when it comes to all of that, to be honest.

**Ademilade Shodipe-dosunmu:** There's like, just a way they prefer things to be done.

**Ademilade Shodipe-dosunmu:** We don't even publish, we just stage it, so we just put it into the CMS Prismic.

**Ademilade Shodipe-dosunmu:** So we have to do that.

**Ademilade Shodipe-dosunmu:** And it takes like 15 minutes for article to stage in Prismic.

**Ademilade Shodipe-dosunmu:** So you have to do that yourself.

**Ademilade Shodipe-dosunmu:** So.

**Ademilade Shodipe-dosunmu:** Another thing is there are some contextual things you would have to do in present as well.

**Ademilade Shodipe-dosunmu:** I don't want to bombard you too much, so we'll probably stop here.

**Ademilade Shodipe-dosunmu:** I want to make sure at least you have, because like, once you have the content down, like everything else is just, everything else is easier to train you on, right?

**Ademilade Shodipe-dosunmu:** Or how to manage your table, what the automations do, what to do in different situations, all of those you can just, you can be trained on those.

**Ademilade Shodipe-dosunmu:** However, content itself is a bit more difficult, so once you have the content down, everything else falls pretty fast.

**Ademilade Shodipe-dosunmu:** So, I'll pause here and ask if you have any other questions.

**Pamela Weber:** Yeah, it's like you said, it's just a lot of steps.

**Pamela Weber:** mean, the easy part is the editing and the fun part is the content, but it's all the little steps to get to there, and then after, that has to get straight.

**Ademilade Shodipe-dosunmu:** It's like a  ton of, like, admin, but I would say that, like, you're guessing these in a good state, because that's not...

**Ademilade Shodipe-dosunmu:** First off, like, lookup data, about this subject, like, some, like, you know, automation for that, all you have is copy and paste, so that's easy.

**Ademilade Shodipe-dosunmu:** I just, like, try to find, like, easier ways to review things, especially these repetitive stuff.

**Ademilade Shodipe-dosunmu:** So, that's one of the things that's helped me.

**Ademilade Shodipe-dosunmu:** The second aspect I would give this work on would be adding any reach.

**Ademilade Shodipe-dosunmu:** So, an any reach answer to is, all you're doing is, like, you're adding FAQs, and you're just revising the language.

**Ademilade Shodipe-dosunmu:** Are you adding one or two internal links to updated content?

**Ademilade Shodipe-dosunmu:** So, for these articles, these were written, like, a long time ago from, like, when we used to use freelancers, right?

**Ademilade Shodipe-dosunmu:** So, you know, some of them are not, like, the best quality.

**Ademilade Shodipe-dosunmu:** So, that's why they made it silly.

**Ademilade Shodipe-dosunmu:** I think I would hold up on the digital accounts.

**Ademilade Shodipe-dosunmu:** I'm talking about the digital next week.

**Ademilade Shodipe-dosunmu:** I think just having these two for now is absolutely fine, honestly.

**Ademilade Shodipe-dosunmu:** I think I reach the best of it, think.

**Ademilade Shodipe-dosunmu:** to job.

**Ademilade Shodipe-dosunmu:** So you're supposed to create a new tab, so you create a new tab, and you call that tab Enriched, so you essentially have to paste what these guys have here, put it here, then you would make the edits here.

**Ademilade Shodipe-dosunmu:** So you're making edits to the titles, to the links, making sure the links are correct, making sure the flow makes sense, and all of that, there are no FAQs to go, so you have to add FAQs, these should not be italicized, those types of changes essentially, making those changes that correspond, adding more internal links, like two or three more to the content, and it should be put from there.

**Ademilade Shodipe-dosunmu:** Then when you have joined, would come and get the title, and you would

**Ademilade Shodipe-dosunmu:** And put something there, so you put that changes made, then you just use them out.

**Ademilade Shodipe-dosunmu:** we added five FAQs, changed, you know, intro, blah, blah, blah, you understand, right?

**Ademilade Shodipe-dosunmu:** Just like highlighting the changes you made.

**Ademilade Shodipe-dosunmu:** And an easy way to do that is you can take this article when you are not making your changes, then take this article, the initial version, and just ask Claude to create a list like that for you.

**Ademilade Shodipe-dosunmu:** So Claude will miss the internal links you added, so you have to add those manually.

**Ademilade Shodipe-dosunmu:** Okay, I it.

**Ademilade Shodipe-dosunmu:** I added it the enriched one.

**Ademilade Shodipe-dosunmu:** Is that the one where you want to work?

**Ademilade Shodipe-dosunmu:** Yeah, in enriched one.

**Ademilade Shodipe-dosunmu:** Okay, I got Yeah, this is where you're going to do one, in the enriched version.

**Ademilade Shodipe-dosunmu:** Yep, you just add the comment at the top stating the things you changed.

**Ademilade Shodipe-dosunmu:** And once you're done, you can just mark it as, you just come here and mark it as ready for.

**Ademilade Shodipe-dosunmu:** Sorry, you just come here and put it as any review, and you just let me know that it's ready for you, and I'll take a look.

**Ademilade Shodipe-dosunmu:** But yeah, regarding how to stage, that's like a 30-minute conversation, but there's a video on how to do that.

**Ademilade Shodipe-dosunmu:** So for how to stage and how to update Jimiloko, I would leave that to you to watch the videos.

**Ademilade Shodipe-dosunmu:** There are videos covering all of these things already, so you have to watch those.

**Ademilade Shodipe-dosunmu:** The one you have questions, I can not answer those, just to make sure that our calls are a bit faster, you know, it takes quite a bit of time to get them.

**Ademilade Shodipe-dosunmu:** Okay, I think we'll stop here for now.

**Ademilade Shodipe-dosunmu:** So for now, I work on these two, the set-up space this week, work on these two.

**Ademilade Shodipe-dosunmu:** One is in NetNew, and one is in Enrich, so just because it's here, this is in Enrich.

**Ademilade Shodipe-dosunmu:** So we have, like, understanding all these are new.

**Ademilade Shodipe-dosunmu:** So for this image, don't worry about it for now, I will figure out how we want to get you started on this, or if you're going to get started on this, so I will reach out to Pamza and ask him about how we would go about that.

**Ademilade Shodipe-dosunmu:** Okay, and the other article?

**Pamela Weber:** Yeah, sure.

**Pamela Weber:** And that sounds good.

**Pamela Weber:** In your code, there's one, the Enriched tab, and what's the other article?

**Pamela Weber:** Is that same thing, editing?

**Ademilade Shodipe-dosunmu:** Oh, new, that's a new one, okay.

**Ademilade Shodipe-dosunmu:** absolutely.

**Ademilade Shodipe-dosunmu:** So they are under two weeks out, so all these ones, I'll put it on them, so we can start from here.

**Ademilade Shodipe-dosunmu:** Cool, I get to do a new one.

**Ademilade Shodipe-dosunmu:** Good.

**Pamela Weber:** And then do you want go back to Slack, and the other three were?

**Ademilade Shodipe-dosunmu:** Is that the same?

**Ademilade Shodipe-dosunmu:** And those are editing?

**Ademilade Shodipe-dosunmu:** These are...

**Ademilade Shodipe-dosunmu:** Okay, so I was confused.

**Pamela Weber:** Okay, I thought those were editing.

**Pamela Weber:** this one is...

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** I've already generated...

**Ademilade Shodipe-dosunmu:** I've already generated discerns, like if you see...

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** Let me just pull up discerns.

**Ademilade Shodipe-dosunmu:** You look here, I've already generated them in the background.

**Ademilade Shodipe-dosunmu:** So they're all here, I guess?

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** they're all here, you know, them.

**Ademilade Shodipe-dosunmu:** So you need to open, for example, think you're doing pod managers, I guess.

**Ademilade Shodipe-dosunmu:** So you open this one and just make sure all of this makes sense.

**Ademilade Shodipe-dosunmu:** Do your fact check in.

**Ademilade Shodipe-dosunmu:** Okay, it's already in the pipeline generated.

**Ademilade Shodipe-dosunmu:** Okay, got it.

**Ademilade Shodipe-dosunmu:** Yeah, that's what thought they kind of...

**Ademilade Shodipe-dosunmu:** Okay, good.

**Ademilade Shodipe-dosunmu:** I thought they weren't like completely...

**Pamela Weber:** No, got it.

**Ademilade Shodipe-dosunmu:** Okay, thank you.

**Ademilade Shodipe-dosunmu:** So you can decide to generate them from scratch if you want.

**Ademilade Shodipe-dosunmu:** No, no, Just get a few...

**Ademilade Shodipe-dosunmu:** I think you've gone with that.

**Ademilade Shodipe-dosunmu:** Thank

**Ademilade Shodipe-dosunmu:** Yeah, but the other one, for sure, I want to do a new one.

**Pamela Weber:** I would definitely want to try a new one in the real world instead of the sandbox and see how it goes.

**Pamela Weber:** Okay, cool.

**Ademilade Shodipe-dosunmu:** Yeah, so, I mean, you could just even, for one day I've already done, you could just generate it from scratch, just to compare the results, see it on the network, and you could take that off.

**Ademilade Shodipe-dosunmu:** But yeah, all the other tools are already in the documentation, but if you go through documentation and you feel like there's something missing, just ping me on Slack, and I'll take a link to this one.

**Ademilade Shodipe-dosunmu:** So, I said, for all these three clients, for at least, hopefully you get, hopefully Panzer agrees and he allows you to, like, get started on, like, the first, yeah, hopefully, like, he allows that to go out.

**Ademilade Shodipe-dosunmu:** So, regardless for all of the accounts, you wouldn't have to, you'd have, you'd be one week ahead, essentially, like, I'll make sure you have all the other tools you need for them.

**Ademilade Shodipe-dosunmu:** So, probably she knows.

**Ademilade Shodipe-dosunmu:** So you will be good on that front.

**Ademilade Shodipe-dosunmu:** So your obligations will start the week after.

**Ademilade Shodipe-dosunmu:** That will be the week of the 12th.

**Ademilade Shodipe-dosunmu:** So even though you are thinking about the announcement next week, you wouldn't have to start the weekend until the week of the 12th.

**Ademilade Shodipe-dosunmu:** I think that will help you accelerate the first time.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Do have any questions?

**Ademilade Shodipe-dosunmu:** Do you want to get started?

**Ademilade Shodipe-dosunmu:** Yeah, for sure.

**Pamela Weber:** probably have questions when I start.

**Pamela Weber:** But yeah, thank you for all this.

**Pamela Weber:** I appreciate how thorough you are.

**Ademilade Shodipe-dosunmu:** So just like shoot me a DM if you run into anything.

**Ademilade Shodipe-dosunmu:** I wanted to keep track of the content across the board for these accounts.

**Ademilade Shodipe-dosunmu:** The good news is that they are not particularly difficult.

**Ademilade Shodipe-dosunmu:** It's stuff you can relate to it.

**Ademilade Shodipe-dosunmu:** And I think it also helps that you're based in the US.

**Ademilade Shodipe-dosunmu:** So like a lot of like the terminology, especially for discern, like registered agents or like state specific nuances.

**Ademilade Shodipe-dosunmu:** It's common naturally to you.

**Ademilade Shodipe-dosunmu:** It was a bit harder for me when I started working on compliance clients some years back because all the compliance companies I used to work for were all U.S.

**Ademilade Shodipe-dosunmu:** based and compliance works a bit differently in my country.

**Ademilade Shodipe-dosunmu:** So I had to do a lot of research to understand how compliance works in the U.S.

**Ademilade Shodipe-dosunmu:** so that I could write confidently about it.

**Ademilade Shodipe-dosunmu:** But you probably wouldn't have to do all of that and you probably would go faster so you have an advantage there.

**Ademilade Shodipe-dosunmu:** But honestly, feel free.

**Ademilade Shodipe-dosunmu:** One piece of advice I'll give you, managing editor to managing editor, is ask questions as much as possible.

**Ademilade Shodipe-dosunmu:** If something is confusing, you can literally spend an entire day trying to figure something out when you can ask the question and figure it out in two minutes.

**Ademilade Shodipe-dosunmu:** It's happened to me.

**Pamela Weber:** I'm speaking from experience.

**Ademilade Shodipe-dosunmu:** Feel free to ask questions is no stupid questions.

**Ademilade Shodipe-dosunmu:** But my DMs are always open.

**Ademilade Shodipe-dosunmu:** Like I told you, even after the handover is done, feel free to ask me anything.

**Ademilade Shodipe-dosunmu:** It doesn't even make sense.

**Ademilade Shodipe-dosunmu:** I would jump in.

**Ademilade Shodipe-dosunmu:** Okay, thank you.

**Ademilade Shodipe-dosunmu:** appreciate that.

**Ademilade Shodipe-dosunmu:** No problem.

**Ademilade Shodipe-dosunmu:** Enjoy the rest of the week and talk to you on Slack, I guess.

**Ademilade Shodipe-dosunmu:** Okay, thank you.

**Pamela Weber:** Yeah, you too.

**Pamela Weber:** Have a great week.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** You too.

**Ademilade Shodipe-dosunmu:** Thanks.
