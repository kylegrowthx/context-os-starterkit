# SpecterOps <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-06
time: 18:30 UTC
duration: 18 minutes
organizer: erik@growthx.ai
participants: Aida Knezevic, Erik O'Brien, Bryce Hein, Jason Wolfe, Kirsten Gibson, Meshach Cisero
fathom_recording_id: 99812389
fathom_url: https://fathom.video/calls/464892382
share_url: https://fathom.video/share/2xe6hon5pCAn37eGpHhAUFr_ysnczY_v
source: fathom
enriched_on: 2026-03-02 19:45 UTC
speaker_note: "enguyen@specterops.io" and "tgomez@specterops.io" appear in the participant list but do not speak in the transcript; all speakers are identified by real names.
</metadata>

---

## Summary

Sync on blog content progress, review processes, and production pipeline.

---

## Context

SpecterOps is a cybersecurity company that engaged GrowthX for a content marketing project focused on security research and threat analysis. This weekly sync is part of an ongoing engagement where GrowthX produces blog articles on security topics for SpecterOps' audience, with Meshach Cisero (SpecterOps) and Aida Knezevic (GrowthX) leading the coordination. The meeting was convened to review progress on the "calibration" blog article, establish a scalable review process for multiple articles per week, and demonstrate GrowthX's content generation pipeline to build confidence in the technical accuracy and efficiency of the production workflow.

---

## Relevance

**To GrowthX Delivery:**
- Argentic pipeline (self-correcting research agent with advanced fact-checking) is now production-ready and being used for SpecterOps content; demonstrates differentiation in technical accuracy vs. standard content generation.
- Scaling model from 1 blog per week to 5 blogs per week; requires 2-of-3 reviewer approval to unblock bottlenecks in review cycle.
- AI-generated imagery (graphics/illustrations) outperforms AI-generated photos; brand tone feedback (castle images too playful) suggests need for prompt refinement to maintain professional tone.

**To GrowthX Business Development:**
- SpecterOps account shows strong engagement signals: approval of review process, scaling content volume, requesting pipeline demos, and active feedback on quality (image tone, topic uniqueness).
- 16 approved topics (2-week backlog) suggests account has clear editorial roadmap; risk of topic duplicates flagged by Meshach requires audit to maintain content calendar quality.
- Product walkthrough rescheduled mid-sync indicates SpecterOps team (Meshach, Erik) actively managing multiple initiatives; potential expansion signals if Atlas/Argentic pipeline adoption leads to broader content strategy.

---

## Overview

- The "calibration" blog is approved for staging; GrowthX will implement feedback and prepare it for SpecterOps to publish.
- GrowthX is drafting three new blogs ("lateral movement," "laps exploit," "golden ticket attacks") to test the review process before scaling to five per week.
- A new Airtable automation will notify reviewers (Sev, Kirsten, Jason) when an article is ready, requiring feedback from only two of the three to prevent bottlenecks.
- GrowthX demoed its "Argentic" content pipeline, which uses a self-correcting research agent and advanced fact-checking to ensure technical accuracy.

---

## Key Topics

### Blog Content & Review Process

  - **"Calibration" Blog:**
      - Feedback implemented; comments will remain open for potential final input from Sev.
      - Status in Airtable → "ready to publish."
      - Next: Staging in SpecterOps' CMS for final review before publishing.
  - **New Blogs in Progress:**
      - "Lateral movement"
      - "Laps exploit"
      - "How to detect golden ticket attacks"
      - Delivery target: early next week.
  - **Review Workflow Automation:**
      - An Airtable automation will email reviewers when an article's status is "reviewing."
      - **Reviewers:** Sev, Kirsten, Jason.
      - **Rationale:** Requires feedback from only two of the three to prevent bottlenecks from busy schedules.
      - Meshach will also review for brand tone.
  - **Topic Backlog:**
      - 16 approved topics provide a 2-week backlog.
      - Kirsten flagged potential duplicates; GrowthX will audit the list.
      - **Context:** Draft titles are AI-generated based on SEMrush data; final titles are manually refined to ensure uniqueness.

### AI-Generated Images

  - GrowthX's new pipeline generates graphics and illustrations, which perform better than AI-generated photos.
  - **Feedback:** The "castle" images may appear too playful and require refinement for a professional tone.
  - **Next:** GrowthX will share examples in Slack for feedback from Rick, Kirsten, and Bryce.

### Content Generation Pipeline Demo

  - Aida demoed the "Argentic" pipeline in the Atlas platform, designed for technical accuracy.
  - **Process:**
    1.  **Research Plan:** Generates an objective and questions for a topic (e.g., "Zero Trust vs. Least Privilege").
    2.  **Self-Correction:** Collects answers, then evaluates them for gaps (e.g., missing cost breakdowns, vendor specifics).
    3.  **Iteration:** If quality is low, the agent asks new questions to fill gaps, repeating until the research passes.
    4.  **Advanced Fact-Checking:** Verifies statements and flags unverified claims, allowing manual review.
  - **Benefit:** This process provides high confidence in the technical accuracy of the final draft.

### Admin & Logistics

  - **Product Walkthrough:** Rescheduled to 5:15 PM ET today (2:15 PM PT) due to a last-minute customer call for the SpecterOps SE.
  - **Looker Dashboard:** Access is pending. Meshach will follow up with the team if the issue is not resolved today.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Close Notion comments on "Calibration" blog; set Airtable status to "Ready to publish"; stage in SpecterOps CMS
- Set up Airtable automation to email Sev, Kirsten, and Jason when article status changes to "Reviewing"; configure to require feedback from 2 of 3 to prevent bottlenecks
- Audit 16-topic backlog for potential duplicates; verify all keywords are unique
- Share AI-generated image examples in Google Drive; post Slack link for Rick, Kirsten, and Bryce to review tone and feedback on castle imagery
- Verify Looker dashboard access is working; if not resolved by end of day, Meshach will follow up with Looker team

**Meshach Cisero (SpecterOps)**
- Follow up on Looker dashboard access with team if not resolved by end of day

---

## Transcript
**Erik O'Brien:** Hey, there.

**Meshach Cisero:** Hello.

**Aida Knezevic:** Hi.

**Meshach Cisero:** How are you doing?

**Aida Knezevic:** I'm good.

**Meshach Cisero:** And Erik, I hope you saw — sorry for moving the schedule of our product walkthrough so much. Our SE, who's going to lead it, had a couple of customer calls that happened last minute, so I shifted it to 5:15 p.m. East Coast time. I think that's 2:15 your time?

**Erik O'Brien:** I'm Midwest, so still before 5.

**Meshach Cisero:** Okay, awesome.

**Meshach Cisero:** Yeah, sorry for the late call, but it was the only time to get it done, and I'd rather have it sooner than later.

**Erik O'Brien:** Yeah, no worries. I've actually got a call at 6 o'clock tonight with a different client, so they're the ones making me stay up late.

**Meshach Cisero:** Duly noted.

**Erik O'Brien:** I'm glad I'm on your good side.

**Aida Knezevic:** Are they on the West Coast?

**Erik O'Brien:** Yeah.

**Aida Knezevic:** Well, I think we can get started. I've added you to the agenda, so you should get it in your email from Notion. So, updates from last week.

**Aida Knezevic:** We did get feedback from the team on the calibration blog that we delivered. We've gone through and implemented feedback and responded to every comment. We haven't resolved the comments yet, just in case anybody else wants to provide feedback. Let us know if that's it, or if anybody else is supposed to provide feedback.

**Meshach Cisero:** I think that's it. I know I tagged in Sev in the Slack channel yesterday. But if he hasn't got feedback, I don't want to hold up the process any further. He could probably be part of the review process moving forward.

**Aida Knezevic:** Okay, that makes sense.

**Aida Knezevic:** All right, I think then we can just close out the feedback and change the status in Airtable to "ready to publish," and then we can move forward with staging that blog in your CMS. We're working on three additional blogs at the moment: lateral movement, lapse exploit, and how to detect golden ticket attacks. We're hoping to deliver those early next week, and then we can start scaling. We want to get to five per week. Doing three blogs helps us get enough feedback without overwhelming you with five blogs at a time.

**Aida Knezevic:** And I think we can also set up an automation in Airtable to make these reviews easier. It will send emails to a specific list of people every time an article is labeled as "reviewing." So who should I add to that list?

**Meshach Cisero:** Probably Sev, Kirsten, and Jason will be the best. I wouldn't necessarily rely on all three of them to review, but if you could get two out of the three, that would be good. Depending on the week, people are pretty slammed, so I don't want to hold up the process too much. And I'll try to review as well — probably not to the level of technical expertise, but just looking at overall brand tone and feel.

**Aida Knezevic:** Yeah, sounds good.

**Aida Knezevic:** Perfect. We can do that moving forward just to make things easier. You've approved 16 topics to get us started, so we have a backlog of about 13 for the next two weeks, which is pretty good. Kirsten flagged that there could be some potentially duplicate topics, so I'm going to double-check. The keywords should all be unique. We do try to provide keywords that are related to each other, but we verify that there aren't any duplicates.

**Meshach Cisero:** The titles could sometimes be similar.

**Aida Knezevic:** In the content OS, they're draft titles. When we actually create blog ideas, we upload a list of target keywords that we manually research. Then we use our article generation pipeline, which is connected to a SEMrush API. The API gives us information about the top-ranking content, and the AI generates a title that meets the search intent and matches the top-ranking content. It's gotten a lot better — a year ago, I had to rewrite the titles every single time, but these days they're much better right off the bat. We still do change them because we adjust the structure, add or remove things, and want to ensure the title is accurate. Just wanted to flag that.

**Aida Knezevic:** So I'll go through and make sure there's nothing potentially duplicative. We're also working on three blogs and have set up an image generation pipeline for the blog posts. We used the existing imagery from your blog. This is what it looks like right now. Let me expand a couple so you can see better.

**Meshach Cisero:** I like these.

**Aida Knezevic:** I think when we say images are AI-generated, sometimes people get a little hesitant. We tried to stick to graphics because AI does a lot better at graphics and illustrations than AI-generated photos. Per article, we generate at least five or 10 different options, and we pick the best option from the bunch. We upload it to your CMS, so you don't have to provide images yourself.

**Aida Knezevic:** If this looks good to you, I can also share these examples in Slack and the rest of the team can weigh in. If you have a designer on your team, they can share feedback too. These images are generated using a detailed prompt that our designer Katja creates, and then GPT creates them. If the castles look a little too playful or childish, we can add instructions to make sure the imagery is professional and doesn't include playful elements.

**Meshach Cisero:** Yeah, if any of those images were to get scrutiny, it would probably be the castles. Please run that by Rick and Kirsten, and maybe Bryce — he probably will have a strong opinion about the images as well. I do like the other ones.

**Aida Knezevic:** Okay, that's helpful. I can share them in a Google Drive.

**Aida Knezevic:** Did I ever show you how the article generation process works? I can do a quick walkthrough because we have the Argentic pipeline set up right now. This is Atlas, our in-house content generation platform. We've had it for about three to four months, and we're constantly improving it as we get new clients and use cases. We basically have two article generation pipelines set up: the Argentic one and the standard one. We've been using the standard one for a lot of our clients, but where it fell short was the research step. Until now, we've been using Perplexity to do the research. The process is divided into multiple steps. The input is a keyword — it could be anything like a golden ticket attack, for example.

**Aida Knezevic:** We click through the steps, and at first it generates a draft brief. It connects to a SEMrush API, researches the top-ranking content, and gives suggestions on keywords and sections the article should cover. We heavily audit this step and might completely change the outline based on our own manual research. Then we run the deep research step, which uses Perplexity to find the information the AI needs to write an in-depth article. It generates an outline we review, then the draft, and we deliver it. But the Argentic Pipeline — which is the one we've been using for you — does the research step differently.

**Aida Knezevic:** We give it a keyword, and then it uses a different researcher — it's a more advanced research tool than Perplexity and can find a lot more information. What's really interesting is that it researches a topic, and then asks itself questions about the answers. It's grading its output at the same time. Let me show you what the process looks like. We give it specific instructions: we're writing an article about this topic with this direction. It then generates a research plan and identifies the objective — for example, to create a comprehensive technical guide explaining the differences between Zero Trust and Least Privilege. Then it generates questions it assumes it needs answered, collects the answers, and evaluates the research quality.

**Aida Knezevic:** For example, the first question scored 0.88 — it meets criteria, but also identified gaps. It realized it was missing specific cost breakdowns, could benefit from more detailed vendor integration specifics beyond Microsoft, and had limited discussion of change management and stakeholder buy-in strategies. If it doesn't pass, it goes back and tries to find more information to fill those gaps. It's basically generating questions for research, collecting answers, grading them, and figuring out what other questions to ask. Our fact-checker step is also more advanced than the regular pipeline. It can catch statements that are inaccurate or cannot be verified. If a statement cannot be verified, it changes the paragraph to say something like: "While industry practitioners recommend this course of action, there is no documentation supporting the claim that X will result in Y." We can then spot that and decide if we want to remove the section or do something else with it. This allows us to have much more confidence in the output.

**Meshach Cisero:** It's pretty cool.

**Aida Knezevic:** It basically runs from the research, adds internal links, and generates the draft. The end-to-end process is very controlled by us. I like to show it to the people we work with because you never really know what we do behind the scenes. Now that you see where we work, it gives you a better idea of how we generate content. If you have any ideas for content you want to create on the website, you're always welcome to share. Since you know how our process works, it might be even easier to come up with ideas.

**Meshach Cisero:** Yeah, this is very helpful.

**Aida Knezevic:** I'm going to step out because someone's generating and I don't want to mess anything up. So, we shared the images. I need to check if the Looker dashboard is working properly.

**Aida Knezevic:** It might not be validated yet.

**Meshach Cisero:** I'll double-check. We just need to be granted access again. I think someone tried to do it this morning.

**Aida Knezevic:** He said he approved it.

**Meshach Cisero:** If you don't see changes this afternoon, I'll follow up with them. Provide me whatever instructions you think are needed to get it done.

**Aida Knezevic:** Great.

**Aida Knezevic:** So, yeah, next steps.

**Aida Knezevic:** We're going to resolve the comments on the calibration blog.

**Aida Knezevic:** We're going to...

**Aida Knezevic:** Draft it in your CMS.

**Aida Knezevic:** We're not going to publish — we're just going to leave it there so you can take a look and see if it looks good, and you can push it live. We'll also be in touch soon with the new blogs.

**Meshach Cisero:** Perfect. Anything else you wanted to cover today?

**Meshach Cisero:** Nope, not on my end. I'll see you this afternoon — or this evening for you, Erik.

**Erik O'Brien:** Yep, absolutely.

**Meshach Cisero:** Thank you so much.

**Erik O'Brien:** Thank you. Bye.
