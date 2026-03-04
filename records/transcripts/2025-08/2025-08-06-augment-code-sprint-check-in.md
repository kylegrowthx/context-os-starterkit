# Augment Code Sprint Check-In

<metadata>
date: 2025-08-06
time: 16:30 UTC
duration: 34 minutes
organizer: jason@growthx.ai
participants: Marcel Santilli, Jason Gong, George Haikal, Molisha Shah, Syl, Aida Knezevic
fathom_recording_id: 78879242
fathom_url: https://fathom.video/calls/371945585
share_url: https://fathom.video/share/pLEy8NSEr-smN-yLvJqv5syCzjug5jiT
source: fathom
enriched_on: 2026-03-03 12:45 UTC
speaker_note: "Board Room" and "Basic" were device/display names. Mapped to Jason Gong and Syl respectively based on content, context clues, and action item assignments.
</metadata>

---

## Summary

Jason (GrowthX) and Syl (Augment Code) reviewed the SlashGuides content initiative, which has achieved exceptional early performance with 30 published articles ranking #1 in search results within days of publication, and decided to double down on editorial content (30/week target of comparisons and listicles) while pausing programmatic content. The Augment Code newsletter is performing strongly (36-37% open rate, 8% CTR), and they explored strategies to repurpose content and grow subscribers through Beehive, newsletter CTAs on guide pages, and social media promotion. With bandwidth constraints limiting full course development, the team discussed alternative content experiments and potential new community content initiatives where GrowthX could serve as a production house for mid-tier community interviews.

---

## Context

This is a sprint check-in between the GrowthX content marketing team and Augment Code (a developer-focused platform). Augment Code recently launched SlashGuides—a content initiative focused on AI-related guides that has generated remarkably fast organic traffic and search visibility. The meeting represents a strategic pivot point where early results are validating the editorial content strategy, leading to a resource reallocation from programmatic content generation to high-quality editorial pieces. Both teams are exploring how to leverage this momentum through complementary channels: organic search, newsletter growth, community content, and backlink strategy.

---

## Relevance

- **To GrowthX Delivery:** SlashGuides represents exceptional case study for AEO strategy—30 articles published, achieving #1 search rankings within days for competitive queries (e.g., "Most secure AI coding platforms for enterprises"). This validates the comparison/listicle content format for AI visibility. Recommend GrowthX apply same methodology to CheckThat and other client initiatives.

- **To GrowthX Business Development:** Augment Code is actively exploring content production partnership with GrowthX for community initiatives (interviews, video production, media training for company spokesperson). Potential expansion opportunity to formalize this into a retainer or project-based engagement focused on community content creation.

- **To CheckThat:** Direct relevance to AEO visibility. SlashGuides performance demonstrates that editorial content format (comparisons, feature lists) drives rapid LLM and search discovery. Newsletter performance (36-37% open rate, 8% CTR) shows engaged audience interested in developer tools and AI platforms—valuable data for CheckThat positioning.

---

## Overview

- SlashGuides content showing strong early performance; shifting focus to more editorial content (30/week target)
- Newsletter performing well (36-37% open rate, 8% CTR); exploring ways to repurpose content and grow subscribers
- Pausing full course development due to bandwidth constraints; exploring alternative content experiments
- Discussing potential for GrowthX to support new community content initiatives

---

## Key Topics

### SlashGuides Performance

  - Published 30 articles, seeing fast indexing and strong click-through rates
  - Example: "Most secure AI coding platforms for enterprises" ranked \#1 in search within days
  - Recommendation: Shift focus to more editorial content, especially comparisons and listicles
  - New weekly target: 30 editorial pieces (up from 20), pausing programmatic content temporarily

### Newsletter Performance

  - Second edition: Slightly lower but still strong metrics (36-37% open rate, 8% CTR)
  - Action items:
      - Add newsletter CTA to guides pages
      - Share top-performing content on social media
      - Explore Beehive for subscriber growth (pending further discussion)

### Video Content Strategy

  - Pausing full course development due to Daniel's limited bandwidth
  - Focusing on other video experiments and supporting existing content

### Community Content Initiatives

  - Developing three-tier community program
  - Exploring GrowthX's potential role in producing content with mid-tier community members
  - Considering media training for company spokesperson (e.g., Guy)

### Backlink Strategy

  - Discussing importance of creating "beachhead" editorial content for backlink efforts
  - Plan to invest in backlinks for high-quality content in coming weeks

---

## Action Items

**Jason Gong (GrowthX)**
- Send weekly newsletter performance breakdown every Friday with most engaged content and prioritized links

- Add newsletter subscriber CTA to SlashGuides pages (sticky rail or top of page)

- Follow up on Google Analytics signup event tracking issues (currently not triggering properly)


**Syl (Augment Code)**
- Discuss Beehive newsletter subscriber acquisition campaign in Slack this week

- Share document with GrowthX re: automation ideas for community and social side

- Share community content generation project details with GrowthX for potential production support (interview production, video, media training for company spokesperson)

---

## Transcript

**Jason Gong:** All right. So we, or Jason, I should say, and team pulled together a bit of a board just to keep us on the big lanes, if you will, right? Everything that we're working on, have worked on, and things that we're kind of prioritizing. And so the way to think about it is the support and research area are the things that we're constantly doing. And there's some things here and there that will go a little bit above and beyond, like, for instance, standing up a new section of the website. Then the content and SlashGuides is where we're seeing the most success. That's where we really want to double down. The MCP directory, we're finally starting to get some of that indexed. Newsletter has huge signals and uplifted more subscribers, so we'll discuss what we can do there. And then there's the experimental, and we've got a ton of different bets. Some that we're actively working on and some others that we can discuss how we want to prioritize.

**Jason Gong:** So I think today we can go through each of the lanes, and then the idea would be to check through some of the big bets in addition to what's already working that we're executing.

**Jason Gong:** Any thoughts, Syl?

**Syl:** Yeah, I have one thing that I would probably add. We put it on the radar—maybe you can put it on experimental right now.

**Syl:** It's basically, last week we shipped the CLI stuff.

**Syl:** I mean, nothing crazy there.

**Syl:** But it's going to be GA, hopefully, pretty soon, to all of our...

**Syl:** And one of the things that we're exploring right now is to, I mean, basically the concept of like, it's kind of like a variation on rules, basically, it's like creating subagent that you can buy there, right?

**Syl:** Like, it's kind of very similar to Cloud Code subagent that we're going to ship.

**Syl:** And so one of the ideas we have is we want to ship it with like, you know, a template, you know, a library of templates, right?

**Syl:** If you think about it this way, so an example of that would be like, hey, this subagent is really good at PRR, oh, subagent is really good at writing, like, Vue.js code, right?

**Jason Gong:** Like, I'm making characters.

**Syl:** Like, it's very, it's, yeah, it's like rules plus plus.

**Syl:** I would say there's like a couple of new ones that we're working on it, but like, so yeah, so it's basically a way to import those rules.

**Syl:** But it's about rules, it's basically rules slash a prompt, right?

**Syl:** It's kind of like a combination of the two put together, if that makes sense, right?

**Syl:** And the interesting thing is, like, these prompts are essentially tools that the agent can use, right?

**Syl:** So they're kind of like self-discovery.

**Syl:** So you have this list of prompts.

**Syl:** It's like, you know, this is Marcel's best prompt to write tests on UJS.

**Syl:** This is Jason's best prompt to do security assessment of change, right?

**Syl:** And these are kind of like micro tools.

**Syl:** And so the agent will be like, oh, before I deploy, I should really run Jason's security check, you know?

**Syl:** And they'll just do it themselves.

**Syl:** Or you can assign it to the work.

**Syl:** And so that's something that we're thinking of building, I mean, of working on.

**Syl:** And we're like, cool, can we get, like, you know, growthx to generate, like, 40 of those rules for us, right?

**Syl:** Like, basically.

**Syl:** So when we launch the features, like, cool, here's the best one from our customers, but also, you know, some from old men made by you guys, right?

**Jason Gong:** That makes sense.

**Jason Gong:** And so are you imagining something kind of similar to this that we built?

**Syl:** Yeah.

**Syl:** So I think there's a web version that is similar to this, and then it's like having that loaded up or accessible by the agent.

**Syl:** I mean, both, that's like kind of like a crisp idea since he's been working on CLI and Nathan, who's not here today.

**Syl:** But like, this is something they shared with me over the weekend.

**Syl:** like, oh, we're thinking of doing this thing.

**Syl:** Is growthx could do that for us?

**Syl:** So again, I'm just putting it as like, hey, heads up, next week we're probably going to talk more about that stuff.

**Jason Gong:** Okay.

**Jason Gong:** Perfect.

**Jason Gong:** Okay.

**Jason Gong:** Sounds good.

**Jason Gong:** I think we can easily take what we've done here and make it look more like, well, your brand, if you will, right?

**Jason Gong:** Yeah, yeah, yeah.

**Jason Gong:** And, but I do think with like rules, we might want to reconsider a little bit of this format.

**Jason Gong:** So that's a little

**Jason Gong:** little bit easier to find, you know, otherwise, it might be a little bit, but anyways, like, everything works, and so that's helpful.

**Jason Gong:** Okay, so maybe we can, two places to start, I think, one, we can start with both the newsletter, the backlinks, or we can start with what's working and go through that.

**Syl:** Yeah, let's go for what's working.

**Syl:** Like, you know, like, metrics and things like that, like, first, like, go and get us, like, what are we learning week over week?

**Jason Gong:** Let's start with that.

**Jason Gong:** Yeah, yeah, okay, so what we're seeing, and I can dig into some of the numbers, but we published 30 articles on SlashGuides, and it's been pretty impressive how quickly we're getting the signals, and so that's very, very encouraging.

**Jason Gong:** The click-through rate is actually pretty strong as well for...

**Jason Gong:** And so our recommendation right now is for us to put as much horsepower behind us as humanly possible because what we're seeing is immediately things get ranked and show up in some of the searches.

**Jason Gong:** So we're seeing pretty immediate results for some of the prompts we're monitoring.

**Jason Gong:** And we're continuing to add more and more prompts, right?

**Jason Gong:** But it's like pretty – there are a couple of examples that I have pulled, but like let's just use this as an example, right?

**Jason Gong:** It's like what are the most secure AI coding platforms for enterprises?

**Jason Gong:** We publish on the 29th, on the 30th, and it starts turning up, you know?

**Jason Gong:** And look at number one, you guys.

**Jason Gong:** And what it's cited, our article, right?

**Syl:** Like, it's working, essentially, you know?

**Jason Gong:** Like, you guys weren't showing up on anything whatsoever, on any LL, on any search, or anything, right?

**Jason Gong:** And it's been pretty consistent.

**Jason Gong:** I haven't tried this one, but just to kind of show you a little bit as well.

**Jason Gong:** Like, there you go.

**Jason Gong:** Like, number one in search.

**Jason Gong:** And then we're, right now, it might not be showing up here, but then the other day when I was trying AI mode, you guys showed up pretty consistently in AI mode as well, you know?

**Jason Gong:** But it's kind of like a hit or miss.

**Jason Gong:** These things are pretty inconsistent.

**Jason Gong:** But it's a pretty good signal overall if it's showing up already in chat.gpt, you know?

**Jason Gong:** And so because of that, we make a lot of sense here, which is go really, really aggressive on comparisons and listicles, more listicles.

**Jason Gong:** And then start to...

**Jason Gong:** Come up with a list of all the other URLs that are getting cited in similar queries and use the way we're thinking through kind of like the backlinks instead of just the backlink exercise, a little bit of an outreach.

**Jason Gong:** this one we need to develop a little bit more as part of an experimentation lane, but think of it as a lot of these sites that show up, these URLs, they're actually like either garbage URLs or URLs that are not like, they're not like super reputable, right?

**Jason Gong:** And so like what we want to do is reach out to these types of websites and try to get placement, right?

**Jason Gong:** And this will, we think this will help, you know, lift up the mentions and get backlinks as well.

**Syl:** So it will help both sides.

**Jason Gong:** So that's pretty much it on the, on here, like, it's really about continuing to...

**Jason Gong:** Do it, do it more aggressively, and then pretty soon start to cross-link a little bit more.

**Syl:** we go back to the goal tracker that you have, like, the old tables, right, you know, it's like, when we say going, I don't know if you have it, do you have it, like, when you have the goals, like, week of await goals, you know, you have a table somewhere.

**Jason Gong:** I'm just going to paste it in, this is the top page I know.

**Syl:** Okay.

**Syl:** Cool.

**Syl:** I just quickly, like, yeah, thank you.

**Syl:** Like, so when we say going more aggressive, it's like, what does that mean, you know, like, like, in terms of, like, input, right, like you said, right now, we're saying, we were doing, like, you know, assignment in production 30, right?

**Syl:** You know, so we, you know, is that, like, 50, 35, 40, like, what's, like, are we just increasing input, or it's, like, same input, but different quality?

**Syl:** You know, more aggressive means, like, what is the expected result?

**Syl:** Like, you know, I know we haven't talked too much about, like, tracking.

**Syl:** Like, if we invest more, like, I expect organic traffic, right, to go up, right?

**Syl:** Or, like, I won't point, right?

**Jason Gong:** Let's answer the hook here.

**Jason Gong:** Yeah, so think of it as, like, right now we're doing about 30 or so programmatic is what we're planning in 10 or 20 editorial in any week.

**Jason Gong:** And so, like, I really think we should shift more towards editorial and potentially even, I don't know if we're going to go, like, 100% editorial and zero on programmatic.

**Jason Gong:** But right now, editorial is working a lot more than anything programmatic.

**Jason Gong:** And we can still develop programmatic ideas pretty soon.

**Jason Gong:** But maybe for a couple more weeks, try to go towards, like, zero programmatic additional pages and then, like, maybe 40 editorial or something like that.

**Jason Gong:** But more importantly, even just the volume is the kind of stuff we're doing.

**Jason Gong:** instead of doing kind of like more like simpler articles, I'm saying let's go do way more comparisons and listicles and things that kind of mention things.

**Jason Gong:** They're really like more bottom of funnel things essentially because they really work.

**Jason Gong:** Like the one bottom of funnel listicle we did, which is like the 13 listicle, is the one getting cited the most, you know, and that's what we're seeing in a lot of the queries we're monitoring, you know.

**Syl:** Okay, so we're not really changing the input that we're doing.

**Syl:** We're just shifting from one to the other, right?

**Syl:** Like on the work stream, it's like, are we still expecting to do like the goal that like Joel added like 20 and 30 here?

**Syl:** Is this still what we want to aim for every week then in terms of targets?

**Jason Gong:** Yeah, that's what we've been aiming for and then we're on track for that.

**Jason Gong:** But the programmatic one is the MCPs and so this week we're having one of our SEO directors dig in because...

**Jason Gong:** There's some of the NCP pages weren't getting indexed after several weeks.

**Jason Gong:** And so we made a few tweaks, and then I believe it started getting indexed.

**Jason Gong:** Yeah, we're already in page two after the tweaks.

**Jason Gong:** Yeah, so we made a few tweaks, and now it's finally getting indexed.

**Jason Gong:** And so I think it's worth putting a quick pause on it, because we have plenty of pages here.

**Jason Gong:** Let it get indexed a little bit more for a few more weeks, and then shift some of those inputs, if you will, into focusing more on editorial and going as aggressive as possible on editorial.

**Jason Gong:** Just because it's working perfectly.

**Jason Gong:** I mean, this is probably the fastest time-to-clicks that I've seen on any of our customers ever.

**Jason Gong:** Or a new section of the site.

**Jason Gong:** And then on the LLMs, you guys are seeing the fastest results on LLMs of any of our clients.

**Syl:** I mean, yeah, that's good news.

**Syl:** Because now we need to continue building that and then converting those things.

**Syl:** Okay.

**Syl:** So basically, we're not changing much.

**Syl:** Like, from a...

**Syl:** For a week-to-week KPI.

**Jason Gong:** No, I mean it's working. We wouldn't shift. It's really just load balancing towards what's working because it's working so fast.

**Syl:** What's the new number?

**Syl:** What are the new numbers at the top?

**Jason Gong:** Then go back to the top.

**Jason Gong:** The volume is staying the same.

**Jason Gong:** We're just writing more listicles.

**Jason Gong:** Yeah.

**Jason Gong:** So what I'm saying is for the next two to three weeks, focus, not focus on MCP servers.

**Jason Gong:** We have, like, 90 or so already and shift as much of that focus as possible on a tutorial and go as aggressive as possible because it's working really well.

**Jason Gong:** that's what I would do with policy.

**Syl:** Yeah.

**Syl:** Okay.

**Syl:** Well, then let's go back to the top and update the weekly target, I guess.

**Jason Gong:** Yeah.

**Jason Gong:** All right.

**Jason Gong:** How does that cost 20 for me?

**Jason Gong:** I think we can, we can, I want to say close to double.

**Syl:** Like 40, like 35, 35 editorial is what we're saying.

**Syl:** And.

**Syl:** And like, 0 or 5 problematic?

**Syl:** Or like, what's the fit?

**Jason Gong:** Yeah, like, I honestly, like, we're going to try to go as hard as possible.

**Jason Gong:** I don't want us to get so focused on, like, is it 35 or 32?

**Jason Gong:** Because, like, if we need to spend an extra five hours on a listicle or a comparison to just make it amazing, but that thing is returning, you know, 10x the clicks and intent, you know, like, we are, you know, we've got multiple people fully focused on this every single day, right?

**Jason Gong:** Like, and getting as many high-quality pieces out every single day.

**Syl:** so, like...

**Syl:** Then let's put 30, like, let's go 30, right?

**Jason Gong:** So, like, let's say we want to get more than what we're doing right now.

**Syl:** 30 seems to be, like, good number.

**Syl:** hopefully, sometime it's going to be 31, sometime it's going to be 39, you know, and that's okay, right?

**Syl:** Like, it's just a...

**Syl:** I just want to see the change, like, you know, of strategy, in fact, like, reflected in the...

**Syl:** The KPIs, right?

**Jason Gong:** Yeah.

**Jason Gong:** Does that make sense?

**Jason Gong:** Cool.

**Syl:** That's so exciting.

**Jason Gong:** I mean, I would consider this above expectations for when we started, for me personally, of like what I thought we were going to be right now.

**Jason Gong:** So we're very happy about that, including also in the newsletter.

**Jason Gong:** The second edition was slightly lower open rates and slightly lower click-through rates, but 8% is still at absolutely insane click-through rate for a newsletter.

**Jason Gong:** And it's definitely above average.

**Jason Gong:** 36%, 37% is also above average for most newsletters.

**Jason Gong:** Obviously, if get to 50%, that's like an insane quality newsletter.

**Jason Gong:** like that's like top, top, top, right?

**Jason Gong:** So being between 35% and 40% is you're pretty much in the highly engaged newsletter.

**Jason Gong:** And so we ran some numbers.

**Jason Gong:** And I don't if, Jason, want to talk through, or George, on the MSR board.

**Jason Gong:** By the top, that kind of relation.

**Syl:** Let's do that today.

**Syl:** I'm just going to have a bunch of things to run out.

**Syl:** I think one of the questions that Monisha had was like, how can we repurpose that content?

**Syl:** We would love to be able to also promote the newsletter on social, that things like that, to get more subscribers there.

**Syl:** So, I think that's like, yeah, I think we should, like, you know, if the content is there, it's good, and people are clicking on it, it's like, you know, let's make sure we get the most out of it.

**Syl:** So, I think this is like, I don't know if you have any ideas on how to, you know, repurpose the newsletter content.

**Syl:** Well, I don't know if it's highest, like, three or whatever performing newsletters, if you share the content with me, then I can just repurpose it, like, on my end.

**Syl:** But it's just like setting up a cadence where we're communicating what's performing well, so I can reuse it.

**Jason Gong:** Yeah, and at the end of each week, I can send you...

**Jason Gong:** The weekly edition of the newsletter, and it's also broken down by which links within the newsletter got clicked more, so it prioritized the most engaged content.

**Jason Gong:** So I can shoot that over every Friday.

**Syl:** I think that's how we can drive people to subscribe to the newsletter, too, right?

**Syl:** By saying, like, hey, we have this, this is a quality call, whatever, this is from our latest newsletter, if you want to get it straight to inbox, subscribe to the newsletter, right?

**Jason Gong:** So I that's, I don't know if it's up.

**Jason Gong:** Yeah, we can, we can add it, I don't know if you, okay, but we could add it to, like, kind of a sticky rail here.

**Syl:** Yeah, I think guide, go nuts, you know, like, I would say guides for now, you can, you guys can go nuts.

**Syl:** I think, let's think about the, all the blog stuff, like, we can definitely, yeah, exactly.

**Jason Gong:** Like, this is our best practice, like, WebSax is our best practice, like, one of our best

**Jason Gong:** They have a newsletter, CTA, and then they have different lead magnets, and they're the highest performing as far as driving opportunities from time.

**Syl:** Yeah, no, that makes sense.

**Syl:** I mean, I think let's, as an action point, let's make sure we add the subscribers to the guide page, just kind of a testing ground, and we can kind of add it everywhere else, like as we continue to run above.

**Syl:** I think, let's make sure we share the content, again, on social, things like that, and then drive to, like, a way to subscribe.

**Syl:** So I don't know if, like, Beehive gave us, like, a  form to subscribe, or even to start with.

**Jason Gong:** It's super easy.

**Syl:** So we can just say, hey, if you want to subscribe, go here to put your email address, it's that easy, right?

**Syl:** Again, that's like, let's get more out of the newsletter, I would say.

**Jason Gong:** So that sounds good.

**Jason Gong:** Yeah, and that's our main recommendation: putting a little bit of money behind buying subscribers. It's not a huge commitment, it's really high quality.

**Jason Gong:** I did this before.

**Jason Gong:** There's so many coding AI, coding in AI newsletters on Beehive, and what you're doing is anytime somebody's subscribing to those, your newsletter gets recommended, and you only pay if they subscribe and are verified to be, to actually open one of your emails.

**Jason Gong:** So it's like such a no-brainer, you know, and we can delay it, but it's like the sooner we start, because it's not an infinite thing.

**Jason Gong:** It's not like you're going to get 10,000 in one day.

**Jason Gong:** It's kind of like a constant thing, and it's really like a campaign.

**Jason Gong:** You put out an offer out there, and newsletters bid on that offer to recommend a newsletter.

**Syl:** Yeah, think let's, like, let's talk about it more this week in Slack.

**Syl:** Okay.

**Syl:** I'm not against the idea.

**Syl:** I think it's just like, you know, just want to keep iterating on the newsletter.

**Jason Gong:** We can invest 20 grand, but that's a little bit.

**Jason Gong:** And then, after this week, when we send it to the longer, bigger list, 60,000,

**Jason Gong:** I would recommend after this week, assuming we continue to see the numbers we are, which is very low unsubscribe rate, we've had zero spam complaints after two editions.

**Jason Gong:** Yeah.

**Jason Gong:** So that's very, very positive.

**Jason Gong:** But actually, we'd like to stay with that.

**Jason Gong:** Yeah.

**Jason Gong:** We want to go up 10,000 per week subscribers to not hurt that because we did start with a slightly higher unsubscribe rate.

**Jason Gong:** The second edition was great.

**Jason Gong:** We're, like, under 7%.

**Jason Gong:** But scaling 10,000 per week is the right thing here.


**Jason Gong:** The only other thing we want to focus on is the video content strategy. We're currently bottlenecked on the full course development. With Daniel's bandwidth constraints, there's no way we're going to be able to prioritize a full multi-week course project right now. We've recorded some content we're editing, and with Daniel using Augment Code, trying to commit to a five to ten hour course would be impossible given our fundraising timeline and other priorities.

**Jason Gong:** But I do feel like between the launch video we did with the video shoot and editing, multiple rounds of editing and supporting that, plus a couple of these other experiments, like there's a ton of different lanes we can keep supporting.

**Syl:** so we're not doing the course content anymore.

**Jason Gong:** Correct.

**Jason Gong:** Yeah.

**Jason Gong:** Not that like the full course right now, just because the bottleneck is like Daniel's time and ability to just spend a ton of time in augment, which he has been.

**Jason Gong:** But doing the full course is going to be like probably like a 40 hour commitment of his time.

**Jason Gong:** And but we have a few other experiments here.

**Jason Gong:** There's definitely the library.

**Jason Gong:** But the other one was like earning the citations, that's another one, and then continue to develop a couple of additional sections of programmatic, you know, for on the site, like for instance, like glossary and come up with additional sections of the site in addition to guides.

**Syl:** Okay.

**Syl:** What was one of the ideas you wanted to talk to GrowthX about?

**Syl:** Yeah, did you have something?

**Syl:** Was it the trend monitoring?

**Syl:** No, I'm done.

**Syl:** Yeah, mean, there's a bunch of other things we can definitely, project that we can give you, I think some of the stuff you were talking to right now, they can probably also work on.

**Syl:** Okay.

**Syl:** So maybe we can share that document.

**Syl:** So there's a bunch of things, mean, I don't have to bounce it for me, so I don't want to open another conversation here.

**Syl:** But we can send you some of the simple kind of like automation.

**Syl:** Okay.

**Syl:** We can send you some automation ideas that we're thinking about, especially on the community and social side of the house.

**Syl:** And so I think that would be, I mean, it's a new wheelhouse in terms of what needs to be built.

**Syl:** So just understanding if you guys can do it.

**Syl:** If not, then we can, you know.

**Jason Gong:** Yeah, that sounds good.

**Jason Gong:** Just keep us posted.

**Jason Gong:** I think the one to keep us posted is the library of templates, only because that one, I would probably assume at least a two-week lead time between design and depth, you know, of minding it on your site.

**Jason Gong:** So just keep us posted so that we can make sure we're allocating on our site as well.

**Syl:** Yeah, again, like it's probably going to be a next week thing since Chris is out and Nathan is busy with a kind of a project right now for this week.

**Jason Gong:** And I saw the video went out.

**Jason Gong:** I saw it in a bunch of different places.

**Syl:** So it looked really good, the launch video.

**Syl:** Yeah, no, it looks good.

**Syl:** I think that's like another thing.

**Syl:** Again, it might be out this week.

**Syl:** So that's kind of a big thing.

**Syl:** Basically, actually, did you re-roll the document?

**Syl:** I'm just about to meet.

**Syl:** I think maybe we can share that with you, but basically we've been revamping a lot of, rethinking of how we're going to do community.

**Syl:** There's going to be a three-tier community, different programs for different people.

**Syl:** And one of them, basically, the thing that you guys could be pretty good at, or at least help with, is the middle community, which is kind of like what we were talking about, Marcel, the care plans of the world.

**Syl:** Like, we're basically working with a sales team and our user base to be like, hey, these are like, you know, software engineer, like normal companies at work days, at like, what is the other guy I work at?

**Syl:** I mean, a bunch of places, right?

**Syl:** I mean, they use AI in kind of very interesting ways as developers, and so we want to basically generate content out of them, right?

**Syl:** And so content is like big C content.

**Syl:** Some of them are NSF, and we would love to record them video style, like go in-depth with them.

**Syl:** Some of them might just be like, cool, 45 minutes interview on a Zoom call, you know, cool, this is great.

**Syl:** Like, Marcel, you're there to do this.

**Syl:** Great, great, great.

**Syl:** Can you share the prompt?

**Syl:** And, you know, it's a package of, like, a blog post plus, like, a templated prompt or whatever we want to call it, right?

**Syl:** And it's just, like, farming this level of people, right, from, like, content.

**Syl:** And, of course, on the exchange for them, they get part of, like, a club or whatever special thing we're going to give them, right?

**Syl:** And so that's why you guys can come in and be, like, basically, you know, like, I mean, one of the questions we had was, like, you know, can you guys just basically be the production house of this for us?

**Syl:** You know, we'd just be, like, hey, hey, Josh, this is Lisa.

**Syl:** She works at Chime, you know, she used AI well.

**Jason Gong:** Go nuts, you know, like.

**Jason Gong:** Yeah, we can also feature that in the newsletter, too, which is a similar audience.

**Jason Gong:** Feature any of that work or test it in the newsletter, too.

**Jason Gong:** So, exciting.

**Syl:** So, I think that's, like, something we can talk about next time.

**Syl:** But, like, that's, like, I mean, we've hired someone.

**Syl:** She starts in, like, three weeks, think, two weeks.

**Syl:** Three weeks, two weeks.

**Syl:** I can't remember.

**Syl:** And so...

**Syl:** Like, you know, we hired a bunch of people to kind of like really push hard on this kind of like full leadership content, content from the brain of our users or community at large, right?

**Syl:** So, you know, it's like, and so one of the most questions was like, can we just use growthx to kind of like shoot the premium stuff?

**Syl:** And then the only question that Emma had was like, you know, if we want to do like a guy recording, basically we want to invest a lot of guy to be like the face of the company, invest in media training and getting him to like be very comfortable.

**Syl:** So that's another thing.

**Syl:** Again, Emma is not here, so I don't have the full flesh out concept yet, but like that's another thing.

**Jason Gong:** She was like, oh, can growthx do that?

**Jason Gong:** I was like, I don't know.

**Jason Gong:** We can talk to them about it and see what happens.

**Syl:** There's no show.

**Jason Gong:** We got a few ideas too.

**Jason Gong:** We'll keep shaping some ideas for next time as well that we think are going to be high impact.

**Jason Gong:** We got a wrap up, but the only ask on your end is if there's anything at all that we can see as far as UTM trying.

**Jason Gong:** For the newsletters, that would be really, really helpful in any kind of tracking from guides as well on signups.

**Syl:** You should have that in Google Analytics.

**Syl:** mean, Google Analytics, we do send a signup off-line conversion event.

**Jason Gong:** Yeah, I don't know if I'm looking at the wrong report, but the event for signups, like, you go by language, it doesn't seem to be triggering.

**Syl:** Okay, send me, I mean, we don't really use Google Analytics that much.

**Syl:** I mean, like, it's mostly something that we use for, like, contractors and things like that, so maybe something is broken.

**Syl:** I'm, you know, I'm not saying it's not, you know, like, it's not something you look at today.

**Jason Gong:** like, Amplitude, like, oh, maybe you use something else.

**Jason Gong:** Okay.

**Jason Gong:** We'll follow up with that if we don't see any...

**Syl:** The last thing I would like to say is, like, I saw you guys shot backlink, so, Jason, I know we talked about it last week.

**Syl:** If we were going to invest a lot more in editorial, like...

**Jason Gong:** I think that's the one, the one asked for me.

**Jason Gong:** I don't know if we're doing it this week.

**Jason Gong:** I don't know if we have time next week.

**Jason Gong:** It's like...

**Jason Gong:** We have all these bets in Experimental Backlinks is one that you were asking about.

**Jason Gong:** think there's a really tactical way we can use it.

**Jason Gong:** Buying newsletter subs is almost comparable to ads in a way, but a little bit more interesting.

**Jason Gong:** Like the earned citation authorization.

**Jason Gong:** I think we need to chat with all these and then decide together which one's the most important.

**Syl:** So we push on that.

**Syl:** I would just say if we invest a lot in editorial content the next few weeks, is like let's make sure we are writing editorial content that can be beachhead content for us and that we can like put Backlink behind.

**Syl:** Like, you know, like if that's the focus.

**Syl:** let's make sure like, you know, let's have the goal that we can spend money on Backlinks in two weeks on like high-level content basically, right?

**Syl:** Anyway, we all have to go to another meeting. George, we'd love to have you join more of these. Take care.

**Jason Gong:** Thanks for the conversation. We'll continue discussing this in Slack.
