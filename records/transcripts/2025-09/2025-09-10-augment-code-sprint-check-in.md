# Augment Code Sprint Check-In

<metadata>
date: 2025-09-10
time: 16:34 UTC
duration: 17 minutes
organizer: Jason Gong
participants: Jason Gong (GrowthX), Sylvain Giuliani (Augment Code), Molisha Shah (Augment Code), Nathalie Schrans (GrowthX)
fathom_recording_id: 86329778
fathom_url: https://fathom.video/calls/405031966
share_url: https://fathom.video/share/NWQP2h-h8LtkMBxq6xYh5AMyPCNyu4eU
source: fathom
enriched_on: 2026-03-02 11:45 UTC
</metadata>

---

## Summary

GrowthX and Augment Code reviewed two months of content marketing progress, with Jason reporting ~10% week-over-week growth, 30 new product evaluation articles, and 30-40 backlinks delivered that lifted domain rating by 5 points. Sylvain outlined a new custom command feature for the Augment website to drive community engagement and SEO value through user-generated submissions. The team aligned on delivering a comprehensive performance report covering signups, content ROI, and insights to justify the investment, setting up Slack automation for newsletter updates, and iterating on the custom command workflow.

---

## Context

This is an Augment Code (external client) biweekly sprint check-in with GrowthX's content and product teams. GrowthX was engaged roughly two months prior to deliver content marketing services to accelerate Augment's organic growth and SEO visibility. Sylvain Giuliani is the product lead at Augment Code, working with Jason Gong (GrowthX content lead) and Nathalie Schrans (GrowthX writer) on content delivery and strategy. The relationship is focused on proving ROI from content — Sylvain mentioned needing transparent metrics because his CFO was asking how they'd know the engagement was working. This meeting happened as GrowthX transitioned from broad content production (comparisons and listicles) toward more strategic, agentic-focused content that targets Augment's senior buyer audience.

---

## Relevance

- **To GrowthX Delivery:** GrowthX successfully shifted from exhausting low-intent content (comparisons/listicles) to higher-intent, agentic and explanatory content targeting C-level buyers — this validates the EPD methodology of moving up the funnel as the account matures. Batch publishing with revision cycles is adding quality control and boosting backlink ROI. Need to establish a robust reporting cadence and dashboard to support client confidence in ROI.

- **To GrowthX Business Development:** Augment Code engagement is at 2-month inflection point where client is asking for ROI transparency. Delivering a comprehensive performance report (signups, content metrics, learnings, what's working) is critical for renewal confidence and expansion. Client is investing in community engagement tools (custom commands) that overlap with GrowthX's content — opportunity to position GrowthX as partner in demand gen, not just content production.

- **To CheckThat:** No direct mention, but custom command feature and user-generated content at scale (targeting hundreds of submissions) presents an opportunity for AI visibility and prompt optimization research.

---

## Overview

- Content growth: ~10% increase week-over-week with 30 new product evaluation articles; strategic shift from comparisons/listicles to agentic and explanatory content targeting senior buyers
- Domain authority: 5-point increase in 3 weeks from 30-40 delivered backlinks; early keyword ranking signals emerging
- Newsletter: Maintaining ~5% click-through rate and 30% open rate; plan to add API integration for tracking valid signups and Slack automation for send notifications
- Custom command feature: New website section for user-submitted Augment commands with built-in categorization, manual review/credit granting, and GitHub repo integration under evaluation; targeting community engagement and SEO benefits from hundreds of user submissions
- Reddit initiative: Contractor hired for automation; planning targeted scraping of keywords like "Augment is expensive" with auto-commenting bot for new pricing tier announcements
- Deliverables needed: Comprehensive 2-month performance report (signups, content metrics, learnings, ROI justification) and API key for Beehive integration

---

## Key Topics

### Content Strategy Progress

  - \~10% content growth from previous week
  - 30 new product evaluation articles
  - Focus on exhausting comparisons and listicles
  - Shifting to agentic topics, explanatory content for senior audience
  - Weekly publishing batch, with increased article revisions
  - 30-40 backlinks delivered, boosting domain rating by 5 points in 3 weeks
  - Early signals of keyword ranking for some content

### Analytics and Reporting

  - Current dashboard shows signups by day/week
  - Need for more detailed trend analysis over time (downloads over time from content, cohort tracking in Amplitude)
  - Request for comprehensive 2-month performance report covering signups, early ranking signals, content performance, learnings on what's working/not working, and ROI justification for CFO approval
  - Reddit scraping analysis to inform keyword targeting and subreddit lists for bot-comment strategy

### Newsletter Performance

  - Maintaining \~5% click-through rate and 30% open rate
  - Request to automate newsletter updates to Slack channel
  - Plan to add valid signups to newsletter list (pending API integration)

### Custom Command Feature (PRD)

  - New website section showcasing custom Augment commands with command format display and categorization by use case
  - User-generated content submission process with manual review and credit granting (no blocker for launch without this)
  - GitHub repo integration under evaluation: concern about user friction (website → PR workflow) and content sync from PR → Sanity CMS; decided to start simple with form submission → Sanity integration first, iterate based on learnings
  - Implementation through Sanity CMS to serve content to CLI and website
  - Target: hundreds of community-submitted commands (not all internal)
  - Strategy: Community engagement and SEO benefit; combats fraud risk by requiring sign-in for submissions; community manager can handle submissions ad-hoc initially
  - Cross-functional: engineering team building form infrastructure, content/product defining command display

### Reddit Scraping Initiative

  - Contractor hired to automate scraping and sampling
  - Scraping Reddit for specific pain-point keywords (e.g., "Augment is expensive")
  - Auto-commenting bot strategy: trigger comments on posts mentioning expense concerns with announcement of new cheaper pricing tier
  - Need: curated subreddit list relevant to Augment's audience (Molisha to request from Archan, who has existing subreddit monitoring list)
  - Integrated with broader content/demand gen effort to capture price-sensitive buyer conversations

---

## Action Items

**Jason Gong (GrowthX)**
- Create comprehensive report on 2 months of content performance covering signups, early keyword ranking signals, content performance breakdown, learnings on what's working/not working, and ROI metrics to justify investment

**Jason Gong (GrowthX)**
- Set up Slack automation to notify team when newsletter is sent to track visibility

**Jason Gong (GrowthX)**
- Provide API key for Beehive to Sylvain for tracking new user signups from content

**Molisha Shah (Augment Code)**
- Request curated subreddit list from Archan for Reddit scraping initiative targeting "Augment is expensive" and related pain-point keywords

---

## Transcript
**Jason Gong:** All right, thanks.

**Jason Gong:** This meeting is being recorded.

**Jason Gong:** All right, I'll get started.

**Jason Gong:** Let's see, anything top of mind before I dive in?

**Sylvain Giuliani:** So, hold on.

**Sylvain Giuliani:** There we go.

**Sylvain Giuliani:** I have the PLD stuff to review today too, but like, yeah, that's it.

**Jason Gong:** Okay, yeah, I'm ready to go on that once you send that over.

**Jason Gong:** Cool, so content, I mean, you know, it's still growing.

**Jason Gong:** I think we're like 10% or more than last Monday.

**Jason Gong:** Still, all the product evaluation stuff is doing well.

**Jason Gong:** We have 30 new ones from last week.

**Jason Gong:** What's the latest on the dashboard? Is this still the latest one?

**Jason Gong:** Like, is this still the most current version?

**Jason Gong:** Can you show me quickly?

**Jason Gong:** Yeah.

**Jason Gong:** I have a little link.

**Jason Gong:** There, it's called growthx.main.

**Jason Gong:** I'm still looking at this.

**Jason Gong:** I think I want to look at, like, downloads over time from our content, but yeah, I think that one's, like, a little trickier to set up.

**Sylvain Giuliani:** I guess there's, like, what's, like, I mean, as you see, like, you know, sign up by a day, by a week, you know, from that source link, not just, like, like, I like the trend over the time.

**Jason Gong:** Yeah, yeah.

**Jason Gong:** I gotta spend time to do that, I think.

**Jason Gong:** I mean, Amplitude has a chart for it.

**Jason Gong:** For this one, I think I need to make a cohort or do something similar.

**Jason Gong:** Let's see.

**Jason Gong:** 30 new articles from last week.

**Jason Gong:** You can take a look here.

**Jason Gong:** But a mix of listicles and more informational things.

**Sylvain Giuliani:** What's the, what's the, again, what's the focus lately?

**Jason Gong:** Have we changed?

**Jason Gong:** We're still trying to, like, just fully exhaust comparisons and listicles.

**Jason Gong:** And then we're moving on to more agentic content.

**Nathalie Schrans:** Yeah, I think this week will probably fully exhaust that list unless we find something else in our research.

**Nathalie Schrans:** And then next steps, we're building out new topic clusters around more agentic topics, kind of like explanatory and how to content around that to target your, you know, the senior level target audience.

**Sylvain Giuliani:** Got it.

**Jason Gong:** And then just, I guess, on generally what we're doing.

**Jason Gong:** So we're still publishing.

**Jason Gong:** Yeah.

**Jason Gong:** A batch every week, with the help of Nathalie, going back and revising more articles than before.

**Jason Gong:** And then doubling down by building backlinks to some, somewhere.

**Jason Gong:** All the backlinks, I think we have like 30 to 40 that have been delivered now.

**Jason Gong:** So, your domain rating has gone up like five points in the last three weeks, which is really helpful.

**Jason Gong:** It'll mean, I guess, you know, content ranking faster and just doing better generally.

**Jason Gong:** And then we have some early signals on this one just starting to rank for a few keywords that we've been at on signups or traffic.

**Jason Gong:** And yeah, I could share a lot of the season review with that.

**Sylvain Giuliani:** I guess it would be nice, like, you know, now that we've published hundreds of pieces of content, right?

**Sylvain Giuliani:** Like, I have, like, deep dive breakdown of, like, what's working, what's not working, like, you know, what's the learning, like, you know, two months in.

**Sylvain Giuliani:** Like, if you can do that, like, reporting would be nice.

**Sylvain Giuliani:** Like, you know, like, we've been using growthx for two months.

**Sylvain Giuliani:** This is where we are today, like, kind of like, you know.

**Jason Gong:** Yeah, sign-ups, early signals on where we're going.

**Sylvain Giuliani:** Yeah, exactly.

**Sylvain Giuliani:** What we've learned, what piece of content is working, like, what it looks like, you know, like, all that.

**Jason Gong:** That sounds good.

**Sylvain Giuliani:** Let me explain — we've got the invoice to pay, and my CFO was asking, how do we know that this thing is working?

**Jason Gong:** Yeah.

**Jason Gong:** Cool, so that's content on the other lanes, and to check the newsletter, but I think that roughly is still sitting at like 5% click-through and 30% open.

**Sylvain Giuliani:** It's still driving sign-ups.

**Sylvain Giuliani:** Can we do the work that we talked about last time — every time we send a newsletter, can you set up an automation that links it to the Slack channel so we know what's going on?

**Jason Gong:** Do you check the content that goes into the newsletter, Molisha?

**Molisha Shah:** I've been checking it regularly, like once a week. It's mainly to see content I can pull for socials.

**Sylvain Giuliani:** Okay.

**Sylvain Giuliani:** It would be good to get to do that, and then like we said last time, like, you know, let's add all the valid sign-ups.

**Jason Gong:** If you can give us the API key, we can add it to track new signups. This is in our engineering backlog, but I can set up the Slack automation first.

**Jason Gong:** That sounds good.

**Jason Gong:** And then as far as other link-building goes, we're mostly doing campaigns around the articles that get cited most, to help you guys get mentioned.

**Jason Gong:** We're waiting on the PRD updates right now.

**Sylvain Giuliani:** We can talk about the PRD. The VS Code update is going to go live — I saw it got merged. It's part of our weekly extension deployment, so it should ship this week.

**Jason Gong:** Sounds good.

**Jason Gong:** I think that'll actually be material, so hopefully that helps the downloads a little bit.

**Jason Gong:** But, um, then, I think we're still in the process of, like, adding more things to the blog.

**Jason Gong:** But, again, our engineers have been slow, so I gotta check in on that.

**Jason Gong:** Um, yeah, I think that's mostly it for us.

**Jason Gong:** And it's been a consistent week and nothing crazy that's new.

**Jason Gong:** Um, anything top of mind for you?

**Jason Gong:** Like, it sounds like just kind of being a little bit better at communicating, uh, activity and metrics every week, so I'll focus on that.

**Sylvain Giuliani:** Yeah, good,

**Sylvain Giuliani:** Yeah, so the PRD, I'll share my screen now real quick, just to secure you.

**Sylvain Giuliani:** So basically, you know, I'll share the doc after this meeting, too, but just kind of running you through it real quick.

**Sylvain Giuliani:** So really the idea is, like we talked about, is having this kind of custom command part of our website, right?

**Sylvain Giuliani:** I talked to the engineering team, and so we'll have this kind of like command format that people can copy, from the website.

**Sylvain Giuliani:** The goal is to have this layout, so this is kind of a mock-up that I have here, thing, but like, this is kind of a different layout that you guys showed me last time, just so you have it, and then you have like kind of a categorization of prompts.

**Sylvain Giuliani:** So you get the idea, then it's like, you how does it look like, you know, single command, you get the idea, it's pretty straightforward, that stuff.

**Sylvain Giuliani:** And the key thing I want to kind of chat to you about is like, so we want to do like user-generating.

**Sylvain Giuliani:** We want our users to be able to submit a comment, and if they get approved, basically, we can reward them.

**Sylvain Giuliani:** The review and credit granting is kind of like a manual process, so you don't have to worry too much about it.

**Sylvain Giuliani:** But I think what Chris was mentioning yesterday in this comment here is how can I go and check back on my submission, things like that.

**Sylvain Giuliani:** There's this kind of thing that we can scope out more.

**Sylvain Giuliani:** This is not a blocker we could launch without the submission side of the house.

**Jason Gong:** What do you think about doing that in a repo, where people can submit a PR?

**Sylvain Giuliani:** I get the idea, but I'm worried about the workflow. If someone goes to the website, finds a call to action, and has to go to a GitHub repo to do a PR, that's friction. Plus, the PR becomes content that needs to be pushed to Sanity, which is how we serve it to the CLI. So we'd need to figure out how to sync PRs to Sanity.

**Jason Gong:** That makes sense. So maybe we start with a form submission workflow that goes straight to Sanity?

**Sylvain Giuliani:** Yeah, if we can automate PR to Sanity sync, I'm down to try it. But let's start simple and iterate.

**Sylvain Giuliani:** For now, let's focus on just displaying the commands on the website with categorization. We can build out the submission workflow separately through Sanity. We don't need the action items or rules — just the commands and categories for now.

**Jason Gong:** And are you imagining like, you guys review it internally and make sure it's not like a duplicate or doesn't work?

**Jason Gong:** Like, how many are you imagining?

**Jason Gong:** Like, this is like tens or hundreds or?

**Sylvain Giuliani:** No, it's probably a couple of hundreds, right?

**Sylvain Giuliani:** The purpose is to show people what else you can do with an AI agent. A lot of people in our sales calls ask about this — they want to just tell the agent to sort tickets or fix bugs.

**Jason Gong:** Oh, yeah, no, that part I get.

**Jason Gong:** I guess I was thinking user submissions.

**Sylvain Giuliani:** It's like, what are you, oh, yeah, user submissions, you know, it's probably going to be.

**Jason Gong:** Like, mean, I'm sure people will be trying to fraud things like that since we give stuff away.

**Sylvain Giuliani:** That's why we need a more robust system. Ideally, only signed-in users can submit. But this isn't a blocker — we can ship without the submission system and have our community manager handle submissions manually for now.

**Jason Gong:** Yeah, yeah.

**Jason Gong:** I guess I was thinking, like, if it's hundreds and hundreds, you know, it needs to be a little bit more robust.

**Jason Gong:** But, like, it sounds like something simple just to kind of have an outlet for somebody to share.

**Sylvain Giuliani:** Yeah, yeah, exactly.

**Sylvain Giuliani:** It's more like, it's more for us, for the community aspect, to do, like, engagement.

**Sylvain Giuliani:** Like, hey, who's using AI, like, augment in different ways, submit your custom command.

**Sylvain Giuliani:** You'll get some credit to it.

**Sylvain Giuliani:** We'll put your name on it. It benefits us across the whole front — community engagement, content generation, and SEO.

**Jason Gong:** Cool.

**Jason Gong:** Yeah.

**Jason Gong:** Whenever we send that over, I think we can turn that around.

**Jason Gong:** We can check.

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** I have another meeting about this thing in, like, an hour, so I'll probably send it to you at lunch or something.

**Sylvain Giuliani:** By the end of the day, basically.

**Jason Gong:** That's good.

**Jason Gong:** Great.

**Jason Gong:** So action-items-wise, we need to handle a few things. We owe you an API key for Beehive to track new user signups.

**Jason Gong:** And we'll work on a comprehensive report — a state-of-the-business review showing what's working so we can prioritize future work.

**Sylvain Giuliani:** Yeah, that would be really helpful.

**Jason Gong:** Great, thanks.

**Sylvain Giuliani:** Thanks.

**Sylvain Giuliani:** Any ideas or things you want to run by them?

**Molisha Shah:** The only new thing that comes to mind is some of the Reddit scraping work that we're doing.

**Molisha Shah:** I don't know if the overlap makes sense, though.

**Molisha Shah:** I basically hired this contractor who's building automation for some of our samples, and one of the projects that we're working on is, like, scraping Reddit for specific keywords.

**Molisha Shah:** So, like, one example would be, like, we're launching, like, a cheaper pricing tier.

**Molisha Shah:** So anyone that's mentioned that Augment is expensive, like, having kind of a bot auto-comment that, we have a new pricing plan sort of thing.

**Molisha Shah:** And so right now, like, I'm just trying to figure out, like, the right keywords or potentially subreddits to go into.

**Molisha Shah:** So I don't know if, like, you guys have started a list there.

**Molisha Shah:** So that would be helpful.

**Molisha Shah:** But then other than that, I'm just working on content.

**Molisha Shah:** So just getting, like, the metrics of, like, everything.

**Molisha Shah:** That we're putting out and its performance would be super helpful to me because then I can just use that.

**Jason Gong:** We don't do much subreddit monitoring ourselves, but Archan should have a list of relevant subreddits from previous work.

**Sylvain Giuliani:** Yeah, ask Archan — they've got a list of subreddits we've been working with. That should give you what you need.

**Sylvain Giuliani:** All right, so Jason, you owe us a comprehensive report and API key. See you in Slack.

**Jason Gong:** Sounds good. Thanks, everyone.

**Jason Gong:** Bye.
