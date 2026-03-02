# Buddy check-in: Katya x Sydney

<metadata>
date: 2025-11-21
time: 16:48 UTC
duration: 12 minutes
organizer: katya@growthx.ai
participants: Sydney Arin Go, Katya Luscomb
fathom_recording_id: 103522389
fathom_url: https://fathom.video/calls/482064597
share_url: https://fathom.video/share/Sm_Y2LCZS6oZqR3_Es96ThpsJgxvJsjJ
source: fathom
enriched_on: 2026-03-02 13:45 UTC
</metadata>

---

## Summary

Sydney demonstrated a fully automated content audit framework that transforms multi-day manual work into a repeatable process, using Google Sheets formulas and Apps Scripts to categorize hundreds of pages for action (Refresh, Redirect, Keep, Monitor) based on GSC and GA4 performance data. Katya will adapt the framework for the Sentinel-1 client, enabling Bailey to lead delivery conversations without doing the audit herself. Sydney emphasized the critical importance of automating publish date extraction and instructing ChatGPT to consider absolute values, not just percentage changes, when generating reasoning formulas.

---

## Context

This is a working session between Katya Luscomb (Content Operations Lead at GrowthX) and Sydney Arin Go (Content Strategist at GrowthX), part of their ongoing buddy check-in cadence. Katya is building operational capacity across GrowthX's content delivery by training Simran to take over ongoing content work for Understory and Udemy clients, freeing her to focus on client strategy. Sydney developed this content audit framework because she was repeating manual audits from scratch for each client—a process that typically took days—and recognized it needed to be systematized. The framework is the foundation for how GrowthX will deliver repeatable, scalable content audits going forward, starting with the Sentinel-1 engagement.

---

## Relevance

- **To GrowthX Delivery:** Sydney's repeatable content audit framework eliminates multi-day manual work per client and becomes the standard playbook for audits. Automating publish date extraction via Apps Script (tested on Redis and Strapi blogs) is now codified. ChatGPT formula generation requires explicit instruction to evaluate absolute values, not just percentage changes (e.g., 1,306% increase from 0 to 1 is a poor signal). The framework reduces Katya's workload on deep-dive content audits, enabling focus on strategy.

- **To GrowthX Business Development:** Adapting the audit framework for Sentinel-1 allows Bailey to own the client conversation around recommendations without relying on Katya to perform the analysis. This pattern supports faster scaling of content delivery across the pipeline and positions Sentinel-1 for early success through clear, data-backed recommendations.

- **To Team Operations:** Katya is training Simran to take over Understory and Udemy content management, with support from Andy and Panzer on communication/feedback. This scales content delivery and frees Katya for more strategic work, reducing last-minute deep-dives and client approval delays that have previously slowed delivery.

---

## Overview

- Sydney built a repeatable content audit framework in Google Sheets to automate analysis, reducing a multi-day task to a few hours.
- The framework uses `IF-THEN` logic to categorize pages for action (e.g., `Refresh/Update`, `Redirect`), providing clear, data-backed recommendations.
- A custom Apps Script automates pulling article publish dates, a critical step that bypasses manual review and enables analysis of content age.
- Katya will adapt the framework for the Sentinel-1 client, enabling Bailey to lead the conversation without needing to perform the audit herself.

---

## Key Topics

### Content Audit Framework

  - **Goal:** Create a repeatable, automated audit process to replace manual work.
  - **Data Inputs:**
      - **GSC (6-month & prior 6-month periods):** Clicks, impressions, CTR, position.
      - **GA4 (6-month & prior 6-month periods):** Engaged sessions, organic sessions, avg. engagement time, bounce rate.
      - **GA4:** Page title data (for customer context).
  - **Automation:** `VLOOKUP` and `SUMIFS` formulas combine all raw data into a single analysis sheet.

### Automated Action Recommendations

  - The framework uses `IF-THEN` logic to assign a "Recommended Action" and "Reasoning" for each page.
  - **Action Categories & Logic:**
      - `Potentially New Content`: Previous 6-month data is zero.
      - `Refresh/Update Content`:
          - High clicks → low engagement (mismatch between search intent and content).
          - Falling impressions.
          - Overall performance decline not severe enough for deletion.
          - Old content that is still performing.
      - `Keep Performing Well`: Trending upwards (low priority to monitor).
      - `Monitor Performing Okay`: Stable performance (P3 priority).
      - `Old Article Update or Redirect`: Low/no performance. Requires manual client review to decide between refresh or redirect.

### Technical Implementation

  - **Publish Date Automation:** A custom Apps Script pulls article publish dates, a key metric for identifying old content.
      - **Process:** Use ChatGPT to generate the script. If it fails, provide ChatGPT with the raw data the script pulls to help it identify the date format.
  - **Reasoning Formula Generation:** ChatGPT can generate the reasoning text formulas.
      - **Critical Prompting:** Instruct ChatGPT to consider absolute values, not just percentage changes. A 100% increase from 0 to 1 click is not a positive signal.

---

## Action Items

**Sydney Arin Go**
- Share audit template link in chat for Katya; she'll copy and adapt for Sentinel-1
- Send test Apps Script for date extraction to Katya

**Katya Luscomb**
- Message Sydney re: Apps Script; then use script + ChatGPT to pull dates for Sentinel-1

---

## Transcript

**Sydney Arin Go:** So, this is the raw data sheet. Full URL, put it in here.

**Sydney Arin Go:** This is a formula to extract just the slug, and you need this for GA4.

**Sydney Arin Go:** Full URL is for GSC.

**Sydney Arin Go:** Clicks, impressions, CTR, position, GSC data, engage sessions, organic sessions, average, engage in time, event count, and bounce rate, GA4 data.

**Sydney Arin Go:** Event count, not sure if Sentinel-1 will have it, but even if they do, I'm not sure if it's relevant data, so it's entirely up to you if it makes sense or not to use it.

**Sydney Arin Go:** And then, so here, the only thing that's really pasted into this document is the GSC data. And this one is pulled from last six months and previous six months, and I just added the CTR position stuff on top.

**Sydney Arin Go:** GA4 last six months is here, and then GA4 previous six months is here, and then that all gets pulled in through VLOOKUP into this sheet. Yeah, and then the title data—this one's the VLOOKUP. Title data is here.

**Sydney Arin Go:** So I have this.

**Sydney Arin Go:** And this one, I don't even really need any of the data here.

**Sydney Arin Go:** I just exported this because I wanted to see the page path and the page title.

**Katya Luscomb:** And you exported that?

**Sydney Arin Go:** That was from GA?

**Sydney Arin Go:** This is GA.

**Katya Luscomb:** Okay.

**Katya Luscomb:** From GA4.

**Sydney Arin Go:** Yeah, it's good for the customer to see, too.

**Sydney Arin Go:** GA4 raw data.

**Sydney Arin Go:** Okay.

**Sydney Arin Go:** And then from here, what I did was I have a recommended action and I've got a couple of different, what's called, if-then statements, basically.

**Sydney Arin Go:** So potentially new content.

**Sydney Arin Go:** I got that from if the previous six months is zero, then that means either it wasn't performing at all or it just didn't exist.

**Sydney Arin Go:** So that is potentially new data for me or potentially new content. And then if it's across the board, potentially new content, then it will show here that this is its new content monitor and keep it as new.

**Sydney Arin Go:** And then, so it's here marked as new content, no previous period to compare.

**Sydney Arin Go:** Refresh update content.

**Sydney Arin Go:** I gotta say, I don't remember which corresponds to what, but basically it's, if it's, I think I've got three for the refresh or update content.

**Sydney Arin Go:** If your engagement is weak, which means you've got tons of clicks, but then not a lot of engaged sessions and high bounce rate.

**Sydney Arin Go:** If impressions are falling, or if like it's falling across the board, but not significant enough to be a delete, then it will go under refresh or update. I have four conditions for refresh or update.

**Katya Luscomb:** One of them, if it's old and still performing, then refresh on update.

**Katya Luscomb:** Okay.

**Sydney Arin Go:** And then keep performing well as if it's still trending upwards and keep it.

**Sydney Arin Go:** That's a low priority.

**Sydney Arin Go:** You can monitor it down the line.

**Sydney Arin Go:** Monitor performing okay is it's still doing good.

**Sydney Arin Go:** So I think for this one, it's doing good, but compared to here, the CTR isn't.

**Sydney Arin Go:** Oh, no, the CTR is okay.

**Sydney Arin Go:** Yeah, so this one's still doing good.

**Katya Luscomb:** So it's, what's it called?

**Katya Luscomb:** Down the line.

**Sydney Arin Go:** And this is what you need to refresh. So this is like a P3 kind of thing—Priority 3.

**Sydney Arin Go:** And then old article update or refresh this one or redirect.

**Sydney Arin Go:** This one is basically it's old.

**Sydney Arin Go:** It's still kind of performing or maybe not performing at all.

**Katya Luscomb:** This one is not performing.

**Sydney Arin Go:** And it depends on the customer if they want to just remove it entirely or refresh it. These ones you would have to manually identify which ones you want to keep or not.

**Sydney Arin Go:** Because included in these older articles are also announcements and product releases that they may want to keep. And the reason why I have all the reasoning here is because, for this one, clicks are 326 with weak engagement.

**Sydney Arin Go:** That means that you are getting some clicks, but you're not keeping those clicks, which means your content is probably not retaining readers. So you're not meeting search intent, and this would be an update for search intent.

**Sydney Arin Go:** For this one, clicks are relatively flat with no major change—I think this one's just a monitor one. But for another one, clicks are down while impressions are up.

**Sydney Arin Go:** That means the problem is probably just a meta title issue, because you're still ranking, so you're probably still kind of meeting search intent.

**Katya Luscomb:** But I was actually talking with Understory about this just the other day.

**Katya Luscomb:** So it makes sense.

**Sydney Arin Go:** Yeah, it is.

**Sydney Arin Go:** It's important for people to make this distinction because, you know, there's so many different kinds of ways you can refresh an article, but that's why all this data is here.

**Sydney Arin Go:** And if it's old, then you just need to update it. So weak engagement, old clicks—it's all there, and it's all formulas.

**Katya Luscomb:** That's great.

**Katya Luscomb:** Can you share this with me?

**Sydney Arin Go:** Um, uh,

**Sydney Arin Go:** We'll just like link it in our chat.

**Katya Luscomb:** Yes, I will.

**Katya Luscomb:** That would be amazing.

**Sydney Arin Go:** And then from here, I just filtered it out by category, so it's easier to present to customers.

**Katya Luscomb:** For sure.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And this could be compiled into more of a report by Claude. Did you put together a Notion page, kind of like Marisol had, that gave a high-level overview, or did you just give them the sheet?

**Sydney Arin Go:** I gave Ada the sheet.

**Sydney Arin Go:** But I did send her a Loom video.

**Sydney Arin Go:** I did send her a loom on how to explain all this.

**Sydney Arin Go:** I did leave comments on where I think customers might need clarifications.

**Sydney Arin Go:** These are all for redirect or updating, but they aren't performing. Click changes are down completely, impressions are up a little bit or down, so CTR change is also down. Position isn't terrible, but the click change isn't great, so they're not performing.

**Sydney Arin Go:** But, and it's also easier just to see, like, are these actually not performing, or just did the AI pull something wrong?

**Sydney Arin Go:** I think this one's a 404.

**Sydney Arin Go:** There's no date, and this is probably a 404.

**Sydney Arin Go:** Who knows?

**Sydney Arin Go:** I also have the published dates here. Honestly, the thing I'm most proud of in this audit is that I finally figured out how to pull the dates. There are like 800 articles on this site.

**Katya Luscomb:** I'm not doing that manually. That would be a nightmare.

**Katya Luscomb:** So that was the Apps Script you wrote?

**Sydney Arin Go:** Yes, and I'll send you the test Apps Script that you can use. Different blogs have their data presented differently, so ChatGPT needs to know how that data is being read so it can give you the dates.

**Sydney Arin Go:** The first approach I tried was an XML import, but it didn't work with Redis's blog. Sometimes XML import will work, and then you're golden and just need a formula. If it doesn't work, you need to test what kind of data the Apps Script is pulling, then show ChatGPT the data and ask "Can I pull dates from this?" and it should be able to do that.

**Sydney Arin Go:** I tested it on Strapi too and it worked well. Finally figured it out after months of trying.

**Katya Luscomb:** I really appreciate getting your cheat codes on this. This seems like something that could become a fairly repeatable process for a lot of clients.

**Sydney Arin Go:** That's why I started doing it.

**Sydney Arin Go:** That's why I started doing it.

**Katya Luscomb:** This is the third time I'm doing this and I'm starting from scratch each time. I can't keep doing this from scratch. How long did it take you to pull this together?

**Sydney Arin Go:** It took a couple of hours.

**Sydney Arin Go:** The only thing you'll need to tweak is the reasoning based on the content you'll pull, but you can do that in ChatGPT. I fed it what I wanted it to say. The first time I did this, I built it manually and already had the formula. I told ChatGPT to follow it but make it better. I think ChatGPT can generate it too—just give it the data.

**Katya Luscomb:** So it needs a baseline of what's your high and what's your low?

**Sydney Arin Go:** Yes, so it can tell you. A 1,306% increase sounds great, but it needs to know your limits. I exported it to CSV and it read that really well. Then I asked it to give me all the formulas.

**Katya Luscomb:** I'll need to play with what makes sense for recommending things for Sentinel-1. I'd like to have this done so I can give it to Bailey, so she can take on that conversation without needing to do a big audit herself. I could also sync with her to see how she wants to coordinate. We have an agentics pipeline meeting next, and so many meetings today.

**Sydney Arin Go:** I've been on meetings since 11:30 AM my time, and now it's 1 PM and we'll end at 2, so that's two and a half hours of back-to-back meetings.

**Katya Luscomb:** I have this, then the agentics meeting, then a meeting about a project coming out of strategy sprint. I wish they'd held it until December because I don't have time next week. The project seems in decent shape, but getting approvals from the client is slow—that's something I'll need to watch. Hopefully this is the last time I'm doing a deep dive on content delivery, and it'll be better because I'm training Simran to take over the ongoing work.

**Katya Luscomb:** I'm working with Simran to get her up to speed on Understory and Udemy, so she'll be holding all of their content.

**Sydney Arin Go:** How is Simran doing?

**Katya Luscomb:** She's okay. I just have to give really explicit feedback. Andy and Panzer are coordinating to help communicate some of that. We're trying to support her through the transition.

**Katya Luscomb:** We should probably go to the next call. Good to see you.

**Sydney Arin Go:** The link I sent you is external-facing, so just create a copy. One more thing with ChatGPT: when you ask it to create the formulas, remind it that percentage change isn't the only column it should look at. If the percentage change is 1% but it went from 0 to 1, that's still a bad signal. I'll send you the test Apps Script.

**Katya Luscomb:** Remind me, please. I'll send you a message right after this.

**Sydney Arin Go:** Sounds good.

**Katya Luscomb:** Thanks. See you in the next call.
