# Prophecy Chat

<metadata>
date: 2026-02-17
time: 16:01 UTC
duration: 29 minutes
organizer: andrew@growthx.ai
participants: Andrew Bishara (GrowthX), Sucheta Biswas (GrowthX)
fathom_recording_id: 122992097
fathom_url: https://fathom.video/calls/571128831
share_url: https://fathom.video/share/4cs2cyHQ59x1FQo8XrQ7AqPmjLndsQ9-
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Handover of the Prophecy client account and content workflow.

---

## Context

Andrew Bishara handed off the Prophecy client account to Sucheta Biswas. Prophecy is an AI data preparation and analysis platform where GrowthX is executing a content marketing engagement focused on long-form articles and guides. Andrew walked Sucheta through the complete content workflow, including pipeline configuration, post-processing reviews, Webflow staging, and performance tracking requirements. This was a comprehensive operations handoff meeting to ensure Sucheta understands the client's high-touch requirements, inconsistent strategy changes, and the multi-step review process before publication.

---

## Relevance

**To GrowthX Delivery:**
- Prophecy requires a three-stage post-processing review (Atlas → Claude → Atlas) that differs from standard workflows; all articles must pass branding and formatting checks before staging
- Critical domain migration issue: All links in Prophecy articles must be updated from `prophecy.io` to `prophecy.ai` to prevent broken links
- Article staging happens exclusively in Webflow's "Guides" section (not Blog Posts), with a specific workflow: draft → Prophecy Team assignment → "Client Review" status → Cody handoff for final publication
- New "Article Agents Test Pipeline" is in beta and available for customization (YAML editing, engineering requests) to improve output quality

**To GrowthX Business Development:**
- Prophecy account faces recurring bottleneck: 18 articles awaiting Cody's approval (representing 3.5 weeks of work), with his review cycles determining publishing pace rather than GrowthX delivery
- Client strategy changes every 2-4 weeks (recent pivots: "Alteryx alternatives"), which destabilizes the 5-article-per-week quota and requires production holds until explicit approval
- Lucas Studio tracking required weekly: add newly published article URLs to Google Analytics 4 and Search Console URL Cohorts to track content performance
- Important contract note: Do not move articles from "Considering" to "In Production" without Cody's explicit approval; this protects GrowthX from publishing misaligned content

---

## Overview

- **Client Bottleneck:** Prophecy's inconsistent strategy has created a backlog of \~18 unreviewed articles, stalling the 5-article/week quota. Do not publish anything without Cody's explicit approval.
- **New Pipeline:** Use the "Article Agents Test Pipeline" for all new content. It's a test run, so you have full autonomy to edit its YAML code or request engineering changes to improve output.
- **Post-Processing:** All articles require a multi-step review (Atlas → Claude → Atlas) to enforce branding, fix formatting, and correct broken `prophecy.io` links.
- **Webflow Staging:** Stage articles as drafts in Webflow's "Guides" section for Cody's review. Do not publish; Cody handles the final step.

---

## Key Topics

### Client Context & Bottleneck

  - **Client:** Prophecy, an AI data prep/analysis company.
  - **Challenge:** Strategy changes every few weeks, creating an unpredictable workload (e.g., a sudden focus on "Alteryx alternatives").
  - **Bottleneck:** \~18 articles are awaiting review from Cody (main contact), representing \~3.5 weeks of work.
      - **Action:** Do not move any article from "Considering" to "In Production" without Cody's approval.
      - **Rationale:** This protects our team from client-side delays. If asked about the quota, cite the backlog as proof we've delivered.

### Content Workflow: Generation & Post-Processing

  - **Generation:**
      - Use the "Article Agents Test Pipeline" for all new content.
      - **Autonomy:** Edit the pipeline's YAML code or request engineering changes to improve output.
      - **Fallback:** The old pipeline is available but requires heavy editing for its 5,000-word output.
  - **Post-Processing (Multi-Tool Review):**
      - **1. Atlas:** Use Andrew's "post-processing process" prompts to enforce branding, revise sections, and format elements like intros, conclusions, and FAQs.
      - **2. Claude:** For client feedback, use the "Prophecy editorial section" tool to analyze comments. Then, manually verify all changes in the "Prophecy Claude" channel.
      - **3. Atlas (Final Check):** Run the revised article through Atlas again.
          - **Compare to Artifacts:** Check against the "Test Run" audience personas and the writing guide.
          - **Regenerate Summaries:** Re-create the intro, conclusion, and TL;DR, as the content will have changed significantly.
  - **Critical Fix:** All links must be updated from the old `prophecy.io` domain to the current `prophecy.ai` domain to prevent broken links.

### Publishing & Performance Tracking

  - **Webflow Staging:**
      - **Location:** Stage articles in Webflow's "Guides" section (not "Blog Posts").
      - **Process:** Create a draft, assign to "Prophecy Team," and set its status to "Client Review."
      - **Handoff:** Tag Cody and comment, "Created a draft on Webflow. Please finalize. Do not publish."
      - **Note:** Cody will review and publish the article himself.
  - **Performance Tracking (Lucas Studio):**
      - **Task:** Weekly, add new article URLs to the "URL Cohorts" sections in Google Analytics 4 and Search Console.
      - **Tool:** Use Claude to format the URLs correctly for each data source.

---

## Action Items

**Andrew Bishara (GrowthX)**
- Post Prophecy channel comment tagging Carrie + Sucheta regarding 18 articles in "Considering" status; hold all from moving to "In Production" until Cody's explicit approval
- Send Prophecy + Sunbit Fathom recordings to Sucheta

**Sucheta Biswas (GrowthX)**
- Generate 1 test article in Article Agents Test Pipeline; do not send to Cody (test run only for process validation)
- Send 25 Sunbit articles to upline backend by February 19

---

## Transcript

**Sucheta Biswas:** Hello. Hi. Can you hear me? Yes, I can. How are you doing?

**Sucheta Biswas:** I'm great, but not my Google Meet. I don't know what happened. It's asking for all the permissions and asking me to go to my settings. Oh, my God. Even the camera is not working.

**Andrew Bishara:** It's all right. I'll be here super quick today. I won't take up too much of your time.

**Sucheta Biswas:** Yeah, do you have any questions?

**Andrew Bishara:** I'm still around until roughly when you wrap up tomorrow. I see the camera now. Yeah, I'll be available sort of until you're around midnight your time, roughly, and then I'm at 12:00. So today I'm just going to go through Prophecy. It's a bit of an involved handoff, but I'll give you the details. I've prepped everything for you. Obviously, if you have any questions, let me know.

**Andrew Bishara:** So this client basically is an AI data prep and analysis client.

**Andrew Bishara:** Now, the big thing with them is that they seem to change their strategy or their approach every couple of weeks. Sometimes leadership gets involved and things change, then they go back and forth. It's a bit frustrating. So you might find that there's so many new articles to write at one point, or maybe no articles to write at all.

**Andrew Bishara:** You'll deal directly with Cody — he's the main point of contact. Carrie will probably liaise with him more day-to-day, but Cody is your main contact for content decisions.

**Andrew Bishara:** We're trying a whole bunch of new things with pipelines and processes. I've updated the operating manual on all the pipelines and publishing. You have all the details and resources there. If you find things that can be improved or want to change, just list it and we can get engineering involved.

**Andrew Bishara:** The new Article Agents Test Pipeline is relatively new and might not work exactly as the client wants just yet. It might, it might not — partially because the client is a little finicky. But we do want to make it work long term.

**Andrew Bishara:** This is a new test pipeline called Article Agents Test Pipeline. You can use it. Feel free to change the YAML code or ask engineering to edit things. You have permission to go for it. Speak with Carrie, but don't feel like you couldn't touch it because this is a test run, and we do want to make it work long term. You have the freedom to do that. You don't have to worry about asking Carrie or myself.

**Andrew Bishara:** You can still use the old pipeline if the new one isn't working. If you go back to the old one and put in the details for the assignment, you'll get your 5,000 words. So you'll have to do quite a bit of editing, but in some cases it might work.

**Andrew Bishara:** I've created a post-processing process. It's a mix of feedback from the client over the last week and what FtShine had probably used. I've given you prompts that you can use. It's basically about enforcing branding and language rules, revising sections, what to do with the intro, conclusion, TL;DR, and formatting. And then there's the FAQ section, and for CTA links, you have to link to their main page.

**Andrew Bishara:** Now, a critical thing: when you get an article, check the links to make sure they're accurate. What you will find is that they will have the old link, which is prophecy.io. It was their old website that we created all this copy for, and then they decided to destroy it and get rid of it without properly migrating it. So basically, if you do find any link like prophecy.io, it goes to the old website, which doesn't exist and might not have a redirect. Make sure it's prophecy.ai instead. That's critical for CTA and for internal and external links.

**Andrew Bishara:** Everything should be fine in the pipeline and in the assignment details. I've made the changes and we've run through it. I've given you the prompts here for Atlas.

**Andrew Bishara:** Final check is pretty standard. Just read the article and make sure it makes sense. There's a structural guideline and article structure requirements that they provided, though that's from November, so it might be a little antiquated. I've tried to embed everything already into the pipeline and processes, but it's there if you want to take a look.

**Andrew Bishara:** This is where the intro, conclusion, FAQ, and TL;DR come in — this is exactly what they want. When you put it in the content initially, it doesn't necessarily come out exactly the way Atlas formats it. So if you want to modify the pipeline, please go ahead. This just irons it out a little better for you.

**Andrew Bishara:** Now, the client does give feedback. I've created a client review and checks process using the Prophecy editorial section tool. Once the client gives comments, you download the Google Doc they've left comments on, copy all the content (not the brief or meta), and put it in markdown. The tool extracts the information and analyzes the comments. When you get the output, it gives you an evaluation report and a summary of changes it made. For example, if Cody's comment says "do not use this term throughout the article," it'll make those changes for you. But you have to double and triple check it because it is finicky sometimes.

**Andrew Bishara:** Here's the workflow: First, upload the Google Doc and tell Claude to review the comments, then paste the article. The tool generates a new article version. Copy the new article across — just the article itself, not the metadata. Then post it into the Prophecy Claude channel. Go through it manually: ask Claude if it made the changes, what the comments were, whether they've been updated, and what else is missing.

**Andrew Bishara:** Then go through post-processing again, double-checking everything: Is the branding right? Are the tones right? Is the intro correct? All those things. Then once it's all done in Claude, take it and put it into Atlas again. Paste the content from Claude to Atlas, run it through Atlas again to make sure.

**Andrew Bishara:** The specific thing I do with Atlas is compare the document to the artifact. Compare it to the audience personas — specifically the ones called "Test Run" because that's the one we're using for the pipeline — and the writing guide. I want to see if it aligns. Sometimes it would not align, or sometimes it's just a little off. Atlas might suggest adding a couple more sentences to make it really hit the audience you need. I do that. Then I scan: Does it make sense narratively? Is the flow logical?

**Andrew Bishara:** What happens is after all these changes, the TL;DR and conclusion might be quite different. So I just ask it to redo them because that way it makes sense. After all those changes, I go through the same post-processing one more time on Atlas just to make sure. So it's a little bit of a hassle, but they are a bit picky and they keep changing.

**Andrew Bishara:** Now for the final step: Webflow. Have you used Webflow before?

**Sucheta Biswas:** Webflow, no, but I can try.

**Andrew Bishara:** Great. There's a video here for how to stage it. The basic process: Log into your team's account, not your personal account — the team growthx account. You might get logged out sometimes, but don't stress. Just log in at a quieter time.

**Andrew Bishara:** Once you log in, go to Prophecy, then Prophecy AI (that's the main one), then go to CMS and select Guides (not Blog Posts) — they've been posting on the Guides section since November. Add a new guide at the top, fill in the name and slug, then copy and paste the body over. Webflow will do the URLs for you. Add a post summary (a couple of lines). Grab whatever image you used from the Atlas pipeline and upload it as both the main feature and thumbnail.

**Andrew Bishara:** For the guide category, select "AI native analytics" or whatever they specify. Assign it to "Prophecy Team" but don't give it to anyone specific. Then create a draft — don't publish it. Go back and change the status to "Client Review." Then tag Cody and leave a comment: "Created a draft on Webflow. Please finalize. Do not publish." He will check it, and he will publish it himself.

**Andrew Bishara:** At the end of the week, check the Prophecy Guides page to see what was published. Then keep an eye on Lucas Studio for performance tracking. I've already updated Lucas Studio, so going forward, just keep an eye on it weekly.

**Andrew Bishara:** For Lucas Studio, the process is actually quite simple. Grab the link from the recently published blogs, use Claude to convert it in a specific format, then paste it into both Google Analytics 4 and Search Console. In Search Console, go to Manage Data Sources, click Edit, and look for URL Cohorts with the FX. Click on that and you'll see all the blogs. Grab the latest post and ask Claude to format it. Then just update it.

**Andrew Bishara:** Do the same for Google Analytics 4 — click Edit, scroll to the blog section, and you'll see URL Cohorts with the FX. Same process.

**Andrew Bishara:** It's got the but the format is different.

**Andrew Bishara:** It was...

**Andrew Bishara:** So it's the same thing, tell Claw to make you a version.

**Andrew Bishara:** Now, this is on the assumption they publish their blogs, they might not actually do that.

**Andrew Bishara:** So that is basically the process for both.

**Andrew Bishara:** That's the process for prophecy.

**Andrew Bishara:** Now, so I'll give you a little bit of an update.

**Andrew Bishara:** I did leave it on the OOO sheet, but I figured I'd just hit you in.

**Andrew Bishara:** Now, they have all these articles ready to publish.

**Andrew Bishara:** So Cody will get to it.

**Andrew Bishara:** He might just change the term.

**Andrew Bishara:** They're all saved.

**Andrew Bishara:** There's drafts on the back end on the web flow.

**Andrew Bishara:** He will basically just handle that, publish it, and he'll move it.

**Andrew Bishara:** So keep an eye.

**Andrew Bishara:** There's currently six years.

**Andrew Bishara:** It might be published at the end of the week, on the Friday.

**Andrew Bishara:** Okay.

**Sucheta Biswas:** How many are we doing?

**Sucheta Biswas:** This week, how many are we doing?

**Sucheta Biswas:** every week?

**Sucheta Biswas:** Every week, there's five articles.

**Andrew Bishara:** And this is where it gets a little tricky. There are currently 18 articles awaiting Cody's review. Because they keep changing their strategy, some articles haven't been reviewed — they're just sitting there. I've updated each article's status. He might review some, might not, because at one point they were focusing on different topics. Now they're doing "Top Alteryx alternatives." I've created those two and sent them for review this morning. He might come back with feedback, which you can implement using the flow I gave you. He might send them straight to publish, or he might publish them himself.

**Andrew Bishara:** Everything's sort of up in the air because you're supposed to do five a week, but there are also 18 in "Considering." Don't put anything from "Considering" to "In Production" without Cody's approval. Until you hear from him on next steps, I wouldn't worry. Carrie will give you updates since there are articles from November or December that still haven't been reviewed.

**Andrew Bishara:** The most likely outcome is you'll probably do edits on the two Alteryx alternatives articles or load them to Webflow to schedule publishing.

**Andrew Bishara:** If they ask where the five articles a week are, here's what you say: "There are actually 18 articles awaiting Cody's review that need to be finalized by him. Once Cody finalizes them, we can go ahead and publish them. Those 18 technically cover three and a half weeks." If the bottleneck is on their end, that's on them, not us. The fact that we have three and a half weeks of articles ready for Cody to approve shows that we've done the work.

**Andrew Bishara:** I'll leave a comment on the Prophecy channel tagging Carrie, since these things are up in the air and she knows it, so it shouldn't be a surprise. Carrie will give you updates on what should be moved from "Considering" to "In Production." When that happens, you'll have the details in the brief, which you can use with the new pipeline, and just follow the post-processing.

**Sucheta Biswas:** I was thinking, since I'm also busy with Sunbit and two other accounts, I'm going to start on it and catch up. And you're here tomorrow, right?

**Andrew Bishara:** Yeah, half day tomorrow because I'm flying out in the afternoon. It's currently 10 p.m. your time, so I'll be available until about 1:30 a.m. your time — that's about 12:30-1 a.m. my time, so roughly three hours from now. Let's make it 1:30 a.m. your time, and I'll be available to help with any questions.

**Sucheta Biswas:** I'm thinking I might want to generate one test article and see how it feels — just to make sure I'm going in the right track. That's my main apprehension. If I generate one and it looks good, I'll be more confident.

**Andrew Bishara:** For Prophecy, you can definitely give it a test run. Just don't send it to Cody since he wants to do his own approval. I'll leave a comment for Carrie and we can see the process from there.

**Sucheta Biswas:** How much time does it take on average to generate articles for Sunbit and Prophecy?

**Andrew Bishara:** For Sunbit, it's written down for you. The 25 this week, I already prepped them — they just need editing. Grab them from the upline backend. For Sunbit, put in the 25 by Friday so they're ready next Monday. That's the best way — you won't be scrambling. You can do them Thursday if you're off Friday.

**Andrew Bishara:** For Prophecy articles, it takes about an hour to an hour and a quarter, depending on the topic. When you get whatever article Cody wants you to do, just throw it in the pipeline and go from there. It shouldn't take long because we've narrowed down the fields and what goes into the pipeline.

**Andrew Bishara:** Grab any topic from "Considering" and just give it a whirl to see what comes out.

**Sucheta Biswas:** Let me try generating one.

**Andrew Bishara:** If you have any other questions, please reach out. I'm happy to help.

**Sucheta Biswas:** I'm not sure if I have recorded it because of the technical issue, but if you have the recording, that would be great.

**Andrew Bishara:** Yeah, Fathom should be recording it. It says it's online, so hopefully it is. I'll send you the recording. Do you have the Sunbit recording?

**Sucheta Biswas:** Just send both to me, that would be helpful.

**Andrew Bishara:** Sure, I'll send them over. If anything else comes up, let me know.

**Sucheta Biswas:** Thanks, Andrew. Have a good day.

**Andrew Bishara:** Bye.
