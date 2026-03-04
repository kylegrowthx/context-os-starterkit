# Website SEO Sync 

<metadata>
date: 2025-07-14
time: 16:02 UTC
duration: 11 minutes
organizer: Jenn Peters (GrowthX)
participants: Cameron Brown (Firework), Jenn Peters (GrowthX), Samrawit Stifanos Berhe (Firework), Megan Dickey (GrowthX), Dave Capone (GrowthX)
fathom_recording_id: 73948969
fathom_url: https://fathom.video/calls/350561632
share_url: https://fathom.video/share/sz1H8eCKJH1A6ieJN_8n2zragqikZFp4
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

Cameron Brown (Firework) updated GrowthX and internal stakeholders on the website migration: infrastructure team implemented non-www to www redirects (results visible in weeks), the first industry page launched today with the rest rolling out this week, and WordPress will be turned off once all pages migrate to Webflow. To unblock cross-team dependencies, Cameron committed to delivering a spreadsheet before Thursday's call outlining action items for GrowthX, Firework's infrastructure team, and Webflow. Sam approved new blog posts, content continues on schedule, and Dave will verify the redirect implementation by crawling the site.

---

## Context

Firework is migrating its website from WordPress to Webflow. Cameron Brown is the lead on this migration, serving as the bridge between GrowthX (which is handling SEO and content strategy), Firework's infrastructure team (managing server configuration and redirects), and Webflow (implementing the new site structure). This is a critical infrastructure project with cascading dependencies: redirects must be properly configured before indexing, all content must be migrated before WordPress can be shut down, and partners page requirements may necessitate keeping some legacy NGINX infrastructure. The team faces time pressure due to key people being out of office (Abhishek, Ritesh) and Cameron's vacation at the end of the month, making coordination and clear ownership of action items essential.

---

## Relevance

- **To GrowthX Delivery:** Firework's website migration is a full-funnel SEO project involving content strategy, technical implementation, and timeline management. SEO performance metrics won't be visible for weeks after redirects deploy. Content cadence must maintain momentum through migration to keep pages flowing into the new site.

- **To GrowthX Business Development:** Firework remains actively engaged through migration and sees GrowthX as essential to the SEO outcome. Account shows strong alignment with clear ownership and weekly coordination calls. Risk: if migration slips due to dependencies, could impact SEO results and timeline expectations.

- **To CheckThat:** Firework's Webflow migration offers opportunity to demonstrate CheckThat value — visibility into on-page SEO implementation and content optimization during the rebuild phase. No explicit mention in call, but technical refresh is ideal moment for AI visibility tooling pitch.

---

## Overview

- Redirect from non-www to www domains implemented, but results won't be visible for weeks
- First industry page launching today; remainder to roll out this week
- Content creation continuing as planned; Sam approved new blog posts
- Cameron to create a spreadsheet detailing action items for all parties involved

---

## Key Topics

### Infrastructure Updates

  - Redirect from non-www to www domains allegedly implemented
      - Dave to crawl site and check for issues once confirmed
      - Results won't be visible in crawling/indexing for several weeks
  - Debate ongoing about necessity of NGINX server infrastructure
      - May need to keep for partners page maintained by third-party company
  - Cameron aiming to complete tasks before month-end vacation

### Content Creation Progress

  - GrowthX team maintaining planned content cadence
  - Sam approved new blog posts for the content manager to work on this week
  - Performance metrics discussion reserved for Thursday meetings

### Project Timeline and Coordination

  - Cameron working to complete tasks before end of month (pre-vacation)
  - Challenges due to key team members being away (Abhishek, Ritesh)
  - Cameron to create spreadsheet detailing action items for GrowthX, infrastructure team, and Webflow
      - Will help manage dependencies and keep all parties aligned

### Technical Considerations

  - Partners page (firework.com/partners or /partnerships) may require existing infrastructure
  - Cameron launching first industry page today, others to follow this week
  - Plans to turn off WordPress once all pages are migrated

---

## Action Items

**Cameron Brown (Firework)**
- Create spreadsheet with action items for Firework, GrowthX, infrastructure team, and Webflow. Include task sequencing and dependencies. Share with all parties before Thursday call.

**Dave Capone (GrowthX)**
- Crawl Firework site to verify non-www to www redirects are properly implemented. Check for consistency issues. Report findings to Cameron.

**Samrawit Stifanos Berhe (Firework)**
- Blog post approvals. Approved new blog posts for GrowthX content manager to work on this week (completed in call).

---

## Transcript

**Jenn Peters:** I'm in Vancouver.

**Jenn Peters:** Oh, Vancouver, that's nice.

**Jenn Peters:** Yeah, but my sister-in-law lived in Edmonton for a long time, so I spent, like, I don't know, like, we'd visit it, like, we'd go there fairly frequently, but, yeah, I need to go there in the summer, because every time I go there, it's winter.

**Jenn Peters:** Yeah, it gets super cold here.

**Samrawit Stifanos Berhe:** Honestly, there's no reason to visit, unless you have family here.

**Samrawit Stifanos Berhe:** Exactly.

**Jenn Peters:** Not much happens.

**Jenn Peters:** But in the summer, I heard it's really nice, because there's, like, a river valley and stuff like that, and, yeah, I just have to check it out, like.

**Jenn Peters:** In better seasons, when I'm not, like, battling windshear.

**Jenn Peters:** Yeah, yeah.

**Jenn Peters:** No, it actually does get pretty nice here in the summer.

**Jenn Peters:** It's a little bit rainy, actually, this summer in particular.

**Samrawit Stifanos Berhe:** But, yeah, usually there's quite a bit, like, of festivals and stuff like that happening in the summer.

**Jenn Peters:** Oh, I love to hear that.

**Jenn Peters:** And it's, like, a cool downtown vibe, I heard, yeah.

**Jenn Peters:** Mm-hmm.

**Jenn Peters:** Yeah.

**Jenn Peters:** Hi.

**Jenn Peters:** Hey, Cameron.

**Jenn Peters:** Hey, everybody.

**Samrawit Stifanos Berhe:** Yeah, I'm like, so agile, the test is out, so as a little reminder, sorry, I just cut somebody off, but I thought I was just admiring Cameron's chair, chair agility.

**Jenn Peters:** Oh, yeah, why stand up?

**Jenn Peters:** Yeah, right?

**Cameron Brown:** Okay, yeah, I'm sure, I don't know if you guys have a bit of an agenda, but just to sort of, I guess, kick things off, get right into it.

**Cameron Brown:** For Dave, our infrastructure team has allegedly implemented the redirect from non-www to www domains, although, like you said, we probably won't see that reflected in our sort of like crawling and indexing results for several weeks.

**Cameron Brown:** I just wanted to sort of hopefully start off on a positive note there.

**Cameron Brown:** Yeah, I'm dealing with this other one problem in the background.

**Cameron Brown:** The only other issue is I'm debating with our infrastructure team as to whether or not we still need this whole NGINX server infrastructure.

**Cameron Brown:** The only reason why we think we might need to keep it around is because currently our partners page is developed and maintained by a third-party website or a third-party company.

**Cameron Brown:** I believe they're actually called partner page.

**Cameron Brown:** So we may need to keep around some of our existing infrastructure simply to sort of maintain the current status quo where firework.com slash partners or partnerships, I believe, still looks as if it exists as part of our site.

**Cameron Brown:** So that's one of the other nuances that I'm dealing with.

**Cameron Brown:** But otherwise, I think we're still tracking well.

**Cameron Brown:** I launched one of, or I'm going to sort of officially launch the first industry page today, and then hopefully roll out the remainder of them over the course of this week.

**Cameron Brown:** And then from my perspective, that's all that I need to have covered in order to sort of like actually start the dominoes falling in terms of like turning off WordPress and doing all of the things that go along with that.

**Cameron Brown:** So it's sort of like a turbulent week because Abhishek, CMO, has been off in the past couple days and weeks for various reasons.

**Cameron Brown:** Ritesh, my manager, is off this week, hence why he's not on this call.

**Cameron Brown:** But I'm also trying to get all this done prior to the very end of the month where I go on vacation for a week.

**Cameron Brown:** So that's kind of like my ideal goal timeline.

**Cameron Brown:** I think it's very doable, however, you know, sometimes working is part of it.

**Cameron Brown:** Organization tends to delay things a little bit.

**Cameron Brown:** So I'm trying to stay optimistic, but that is sort of my update for you all.

**Cameron Brown:** But, yeah, I don't know if this, I know this is sort of just like our sync call, and usually Ritesh has like a couple of action items for you guys in terms of, I guess I'll do my best to sort of like speak on his behalf, is I don't know if you guys have a list of action items that he's given you.

**Cameron Brown:** Do you have sort of like updates on that in terms of how the last week of content writing went on your side?

**Jenn Peters:** No, like performance wise, we probably better like reserved that for the Thursday meetings, like in terms of what we covered last week while Megan was away, like, you know, the message I got from him was just like, let's keep up the cadence that we've been working on.

**Jenn Peters:** As planned just for that, you know, when everything is ironed out that we'll still have stuff in the pipeline kind of rolling out and that's what we're doing on our end.

**Jenn Peters:** I think my impression of this call is just for you and Dave to align and, you know, just to kind of catch up there.

**Jenn Peters:** But Megan, did you have anything to add to that?

**Megan Dickey:** Yeah, I guess, yeah, the only other thing for me, so yeah, typically we have, we'll ask Ritesh to sort of approve the blog post for our content manager to work on for this week.

**Megan Dickey:** So since he's out, like, is there someone else who's able to?

**Jenn Peters:** Sam's already approved them, actually. It just happened just before the call, so you're not going to be far behind or anything. Sam's on it.

**Jenn Peters:** Cool. Awesome. Thanks, Sam.

**Megan Dickey:** Well,

**Megan Dickey:** And Cameron, sounds like you have everything you need from Dave, at least for the time being.

**Megan Dickey:** Yeah, definitely.

**Cameron Brown:** I may over, like, when we sort of really get into crunch time, I may message you guys in the Firework GrowthX Slack channel, just if I have any questions.

**Cameron Brown:** But yeah, I appreciate you joining a call and sort of standing by, but I am still sort of like under the impression that I am kind of the bottleneck here, because a couple of like, I'm obviously sort of like the bridge between the folks on this call and the infrastructure team.

**Cameron Brown:** I'm also sort of talking to Webflow about some of these issues as well.

**Cameron Brown:** I'm just kind of going over my notes to make sure I'm not missing anything.

**Cameron Brown:** But yeah, no, I at least, I, and I thank you guys, because you have played a part in sort of over the last week or so, I have a much clearer.

**Cameron Brown:** A picture of exactly what needs to be done.

**Cameron Brown:** One of the things that I am going to try and work on, maybe have ready before our Thursday call, I'm imagining some sort of like spreadsheet that I'll put together where we have like myself, growthx, our infrastructure team, and Webflow in terms of like a list of action items that have to occur over time.

**Cameron Brown:** And as long as we sort of stick to those, I'll share that document with you guys and all of those parties that I just mentioned.

**Cameron Brown:** Because I sort of anticipate one of the challenges over the next days and weeks is in order to sort of get infrastructure moving, I've had to pull in my manager to sort of like flex that authority a little bit.

**Cameron Brown:** So as long as everyone's sort of on the same page in terms of what they're responsible for and what needs to happen when, because, you know, some things will need to wait for other tasks.

**Cameron Brown:** Then I think, you know, as long as we have our ducks in a row, we're looking good because I'm still obviously chugging along here to try and get the site totally ready to switch over.

**Cameron Brown:** But, yeah, I don't have a whole lot for you guys other than that.

**Megan Dickey:** Well, then, yeah, we'll get moving on the new blog post and we'll just stay in touch and then we'll meet up again on Thursday. Appreciate you guys taking the time.

**Cameron Brown:** Sounds good. Yeah, of course.

**Dave Capone:** Hey, wait, Dave, before we go.

**Dave Capone:** If the engineers have put the redirects in place for the www or non-www, I'll go through and crawl the site and make sure there's no issues there. I'll let you know what I find.

**Cameron Brown:** I will sort of let you, oh, actually, where did that conversation go?

**Cameron Brown:** Just to give you some context here, this is what I mean. I'm sure he doesn't mind. We were talking here a little bit about the redirect.

**Cameron Brown:** He raises some concerns about the sitemap kind of changing the subject, and I've asked and explicitly sort of confirmed that the redirect has been implemented because he says it's doable, but he doesn't confirm for me that it's done.

**Cameron Brown:** The issue and the reason why I'm raising this here is because this person from our infrastructure team, I think, is based in Hong Kong.

**Cameron Brown:** So they're probably asleep right now, and I'm not going to get confirmation probably until this evening, if not tomorrow morning.

**Cameron Brown:** So it sounds like, based on just the conversation that we're having, that he may have already done it, but I'm not entirely sure.

**Cameron Brown:** I maybe could look through some Git commits and sort of interpret on my own, but yeah, I just don't want you to sort of like waste your time.

**Cameron Brown:** And then seeing that nothing's changed because it's possible that he hasn't quite done it yet or hasn't committed it to the main branch or anything.

**Cameron Brown:** Okay.

**Cameron Brown:** Yeah, I appreciate that.

**Dave Capone:** I'll run my crawler on it to make sure that the rules look good. We can double check to make sure that there's consistency there. And if I see anything, I'll point it out.

**Cameron Brown:** No problem. Thanks, everyone.

**Samrawit Stifanos Berhe:** Thank you.
