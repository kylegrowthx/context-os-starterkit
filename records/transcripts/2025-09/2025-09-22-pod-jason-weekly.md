# pod Jason weekly

<metadata>
date: 2025-09-22
time: 16:30 UTC
duration: 36 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Nathalie Schrans (GrowthX), Marisol Smith (GrowthX), Edin Abazi (GrowthX)
speaker_note: Sydney Go was listed as an invitee but was on a flight to Manila and did not participate in the meeting.
fathom_recording_id: 88890912
fathom_url: https://fathom.video/calls/416327527
share_url: https://fathom.video/share/TfCH13u9VqTyGo8YMrWH7eTvx_Xyk7AJ
source: fathom
enriched_on: 2025-03-03 14:35 UTC
</metadata>

---

## Summary

Jason Gong led a weekly sync for his content operations pod covering three main projects: the Surge website launch (now 90% complete with minor Safari fixes needed), Augment's content strategy revamp (shifting from 30 articles/week with minimal editing to prioritized, higher-quality output), and structural workflow improvements to reduce manual editing and steering content generation more effectively. The team also outlined two new initiatives — a public GrowthX engineers blog for showcasing internal technical work and an automation reporting dashboard in Looker Studio.

---

## Context

This is Jason Gong's weekly sync for his content operations pod at GrowthX. The pod manages two main projects: Surge (a client website build/redesign handled by design engineer Edin Abazi) and Augment (GrowthX's automated content platform generating 30 articles per week). The meeting happened early in the Augment relationship (2-3 weeks into content strategy development) and reflects a strategic pivot toward content quality and intentional prioritization rather than volume-at-all-costs. The team is also running a separate content strategy sprint engagement with another client. Notably, Sydney Go (a team member) was traveling to Manila and missed the call.

---

## Relevance

**To GrowthX Delivery:**
- Augment project is scaling quickly (30 articles/week) but hitting quality and workflow friction; prioritizing content strategy over editing as the most effective way to steer quality upstream rather than fixing downstream.
- Surge website nearly ready for launch; final checklist and SEO basics (meta descriptions, titles, tags, sitemap, OG images) in place but need some optimization for search visibility.
- Workflow improvements are critical — Jason is forming a dedicated task force to iterate rapidly (hours to days, not weeks) rather than waiting for sprint cycles.
- Edin Abazi is the design engineer leading Surge build; he's requesting access to Augment repo to work on the Auggie CLI page in Sanity.

**To GrowthX Business Development:**
- Augment has 2-3 week relationship maturity; contract is live and team is publishing actively, good signal for account stability.
- Team is exploring ways to demonstrate the value of quality refreshes vs. volume; hasn't yet shown clear ROI on refresh work vs. new content, which may impact client willingness to shift content strategy.
- GrowthX engineers blog is a new internal initiative — potential positioning opportunity to showcase internal AI/engineering work and build thought leadership.

**To Content/SEO Operations:**
- Major content strategy decision: focusing on keyword clusters, prioritized topics, and quality editing on 2-10 articles/week instead of light editing on all 30/week.
- Title and URL slug optimization is a known gap — many Augment articles lack "in 2025" in titles or have dates/numbers in URLs (which impact SEO and content updates); needs a process to check before publishing.
- Article refresh workflows are not yet mature; current automated refresh tool "bulldozes" articles instead of preserving ranking sections — needs manual editorial review for refreshes.

---

## Overview

- Surge website 90% complete (9/10 requested changes done); minor Safari jitteriness on visual effects; SEO basics in place, sitemap and checklist to be created
- Augment pivoting strategy: shift from 30 articles/week with light editing to prioritized content clusters with 2-10 in-depth edits/week; content strategy roadmap due Wednesday for client call
- Workflow friction is now the critical blocker; Jason forming a dedicated task force to iterate on processes in hours/days instead of waiting for 2-week sprints
- Edin needs repo access to Augment codebase to begin Auggie CLI page development in Sanity; title/slug optimization process needs refinement before publishing
- New bets: GrowthX engineers blog (public-facing developer publication, very minimal scope) and Looker Studio automation reporting dashboard (Suleiman in progress)

---

## Key Topics

### Surge Website Progress

  - Website nearly complete; 9/10 requested changes implemented
  - Some Safari-specific issues remain (jitteriness); may remove effects for Safari
  - SEO basics in place (meta descriptions, titles, tags); sitemap to be added
  - Checklist of completed items to be created for transparency

### Augment Content Strategy

  - Content strategy process started 2-3 weeks ago; needs prioritization
  - Jacob provided topic clusters and keyword suggestions
  - Goal: Create prioritized list of topics grouped by clusters
  - Focus on steering content generation rather than extensive editing

### Content Quality and Workflow

  - Current volume (30 articles/week) challenging for thorough editing
  - Suggestion: Prioritize 2-10 articles/week for in-depth editing
  - Need to demonstrate value of refreshes and quality improvements
  - Workflow improvements needed; task force to be formed for rapid changes

### New Initiatives

  - GrowthX engineers blog: Simple, public-facing developer blog to be created
  - Augment CLI integration: To be added to existing Sanity installation
  - Automation reporting: Suleiman working on Looker Studio dashboard

### SEO Optimization

  - Need to incorporate target prompts into article titles (e.g., "in 2025")
  - URL slugs should avoid numbers and dates; redirects may be needed for updates
  - Process for checking and optimizing titles and slugs to be refined

---

## Action Items

**Edin Abazi (GrowthX)**
- Create sitemap + checklist of SEO tasks done for Surge website
- Begin Auggie CLI page dev in Sanity once repo access granted; use existing design

**Marisol Smith (GrowthX)**
- Refine title optimization process in article workflow; check SERP simulators before sending to publish
- Map out articles that need URL slug and title updates; coordinate with Nathalie on bulk corrections

**Nathalie Schrans (GrowthX)**
- Create content strategy & roadmap for Augment; prioritize over editing — due Wednesday for client call
- Share current progress on content strategy w/ Jason, even if incomplete — WIP acceptable
- Follow up w/ Suleiman re: automation reporting (Looker Studio dashboard) progress in Slack thread
- Prep meeting agenda for tomorrow's Augment call; focus on progress/plans, not metrics

**Jason Gong (GrowthX)**
- Continue pushing to get Edin added to Augment repo for dev access
- Form dedicated task force for workflow improvements — separate from 2-week sprints, decisions in hours/days
- Build Airtable metrics dashboard for client reporting by Wednesday call (optional, fallback to manual agenda)

---

## Transcript

**Edin Abazi:** Hello.

**Marisol Smith:** Hi, how are you?

**Edin Abazi:** Good, good. Finishing up for today.

**Marisol Smith:** Oh, nice. Where are you located?

**Edin Abazi:** I'm in Europe, in Central East, in Macedonia. Yeah, it's 6:30 p.m.

**Marisol Smith:** Even though I do have another call at like 11 p.m.

**Edin Abazi:** It's only once a week.

**Marisol Smith:** I am in Santiago, Chile, South America. Now it's 1:30 p.m.

**Edin Abazi:** Oh, nice. Quite close time to California time.

**Marisol Smith:** What do you do in GrowthX? What's your role?

**Edin Abazi:** Design engineer. Right now, mostly development, but like with a background in design as well.

**Marisol Smith:** I'm a content manager.

**Edin Abazi:** As I've always wanted to ask somebody in content this question: what's your favorite CMS to work on? Like editing, if you were to go into a CMS and edit the content directly.

**Marisol Smith:** I really like HubSpot. Once you get the hang of it, it's good.

**Edin Abazi:** Hi, Jason.

**Jason Gong:** Hello. How's it going?

**Edin Abazi:** Good.

**Jason Gong:** Good. Busy week ahead. I think Sydney is on a plane. Yeah, she's flying to Manila.

**Jason Gong:** Let's start a doc for this meeting. If not, I'll make it right now.

**Marisol Smith:** I have one.

**Nathalie Schrans:** I have one. I'm off camera because I need to make light.

**Jason Gong:** Yeah, what is it called?

**Nathalie Schrans:** It's podjasonweeklycheckin, but I'm dropping it in the Zoom chat also.

**Jason Gong:** Okay, so we can just talk about Surge and Augment. We can just talk about Surge first because I think it'll be quick because we're not doing a ton, at least for content, but I know Edin is knee-deep into getting their website up. Anything there I can help with?

**Edin Abazi:** No blockers, really. There was another list of 10 different things over the weekend. And we got like, I think all of them except for one. Probably like later today, I'll send a message saying it's ready. There are some issues in Safari — some weird jitteriness — which isn't quite straightforward. So one option is to just get rid of the effects completely on Safari. We'll play around with that and see what we can come up with.

**Jason Gong:** Okay. Yeah, we haven't heard anything yet about the urgency of getting it out, but we're talking to them every Wednesday and it'd be nice to get it out by then. Do you know if there's anything — once we want to get it live — what the steps even are?

**Edin Abazi:** I haven't spoken to anyone about what the process there would be like.

**Jason Gong:** Okay. And do you think that everything SEO-wise is set up? Like every page has meta descriptions, titles are right. Do we need someone from our team to look at that?

**Edin Abazi:** We have the basic meta descriptions and meta titles and meta tags in general, which do get replaced based on the page itself. I haven't really had too much time to go into the optimization side of things because of the amount of stuff we've had to do. But we can do the LD JSON schema thing for blog posts, even though the content itself doesn't have FAQs, authors, or anything right now. We can definitely add them in once they decide to add authors.

**Jason Gong:** Yeah, absolutely. If they want to do FAQs, which I doubt they will. But if we can make a list, that'd be nice because then at least we know it's just not done yet. For me, the main test is when somebody shares the link in Slack, it doesn't pull up something random. Like every page should have its own share card.

**Edin Abazi:** Those are already taken care of. Like the title, the description. OG image is pretty much the same on every page.

**Jason Gong:** Yeah, yeah. And it was made by Gene as well. So I'm guessing they'll be fine with it. And then also, if you just search it, it ends up popping up on Google. Like there's no random no-index things.

**Edin Abazi:** Yeah, well, a sitemap. I'll add one in — it's easy. After the call, I'll just create a basic one.

**Jason Gong:** Okay. Checklists of things that have been done.

**Edin Abazi:** Yeah, I'll just make a list after that.

**Jason Gong:** And then for Surge, they're taking socials in-house, so we don't have to do that anymore. I think Surge just does this a lot — they kind of change ideas and try different things. So I don't know if it's solely on us, though. It'll probably move a little bit faster. We have events. That's in a different thread. And I'm still trying to get a grasp on their content so we can do something for them. So that's Surge. For Augment, the main thing for me is just — I know we started this content strategy process probably like two, three weeks ago, and I just haven't really seen anything there. What exactly is the status of that?

**Nathalie Schrans:** So Jacob basically found topic clusters for us, along with keyword suggestions. I just honestly haven't had time to do all that with all the editing, but I'm going to do it today and tomorrow. I don't think it's going to be possible for me to edit all 30 pieces every week.

**Jason Gong:** For the most part, we've been publishing without editing, which I know is not great, but the way we get around that is by having this content strategy and aligning them to it. So I would prioritize that over editing.

**Nathalie Schrans:** Yeah, definitely. So I'm going to work on the keyword research and the content roadmap — basically a prioritized list of topics grouped by similar clusters — today and tomorrow so that you can look over it and we can present this to them on Wednesday.

**Jason Gong:** Okay. I mean, I think it's okay if you just share whatever you have, like if it's a work in progress. I just want to see the structure of it and if it's on the right track because I just haven't actually seen anything yet.

**Nathalie Schrans:** Yeah, I'll work on that today. I have another strategy sprint client that I'm working on. Our sync with them is tomorrow. But I'll work on it today and anything that's left will be tomorrow for the content roadmap.

**Jason Gong:** Okay, cool. So that's content. And our strategy there is: once we do this mapping, I think we just want to pick a super easy cluster and then I'll try to bring that number down every week and focus more on refreshes. I think one concern for me is I haven't really shown the value of refreshes at all. I have this article we built with almost $10,000 of backlinks to, and it's not really doing that much better. And then I look at it, and it's like we don't even have meta descriptions. I think we need to find some way of showing that quality matters, which I know everyone believes deep inside. But unless we show that, you're just going to be like, all right, let's just do that and publish 30 more. So I'm trying to figure out how to show that. Do you guys have any other ideas for articles where we have done quality and it's shown some results, so I can point them to it to get them on board with switching gears a bit?

**Nathalie Schrans:** Wasn't that the eight top AI coding assistants article? Hasn't it gotten the most clicks in Google Search Console?

**Jason Gong:** It's definitely not the most clicks. I mean, there were some good signals with getting picked up in Perplexity, but I think the last run of Perplexity didn't get picked up. When I read that one, I don't know if it's even SEO optimized. I just added "in 2025" to the title. I didn't change the URL or anything, but for the prompts we're targeting, almost all of them have "in 2025" in it. The first three or four sections in that article are very long-winded before it gets into the tools. One of the H2 titles was like 10 or 11 words long. I think we need to show them something that's working, and I'm just not sure if we can.

**Nathalie Schrans:** Yeah, I mean, if they're fine with more new content that isn't the best quality, we could just do that, and I would just not edit them as much. One of my suggestions was: as Marisol is generating these articles, if there are certain ones that she thinks could use editing, she could flag those so I can prioritize editing them. Because I can edit like 10 a week. And if those are the ones that Marisol thinks are the most worthwhile topic or could use more editing, then I can prioritize those. I've seen that some of the editing is more just structural editing, and that's faster. And that can make a big difference without requiring much time.

**Jason Gong:** I think especially since editing is not a blocker for publishing — whether you edit it this week or a few weeks from now when there's some signal — I think that's totally up to us. The reason for the content strategy is the most effective use of time is before something gets generated — just steering that. I think steering there is much more effective than editing the thing that comes out.

**Nathalie Schrans:** Yeah, I agree.

**Jason Gong:** Yeah, so prioritize the content strategy. Don't feel the pressure to edit every article. And then we can apply those improvements into the workflow.

**Nathalie Schrans:** Yeah. I've just been taking notes as I'm editing on things that I think would be more like workflow issues, not editing issues.

**Jason Gong:** For the workflow stuff, I'm totally aware we've been talking about it a lot and trying to figure it out. At least from my side, I think we need to change gears a ton. My suggestion was: we need a little task force that's totally detached from these two-week sprints where we can make changes in like a couple hours or a day tops instead of waiting weeks. And then we just need to hunker down and figure out how to make our workflows better. I'm working on that, but in the interim, I think we still need to keep this thing going.

**Marisol Smith:** We also need to set up the refresher pipeline so it can act as a post editor. We can publish and then select the top pages and refresh them.

**Jason Gong:** Do you think that one's helpful? Have you used the refresh workflow?

**Marisol Smith:** I haven't used that.

**Jason Gong:** Okay. I'll say it's not good. So I don't even know if it's worth it. I'd rather Nathalie just change some H2s. It basically completely rewrites the article. It doesn't do this thing where it's like, oh, yeah, it's ranking well for this keyword — let's keep those parts and shape the rest of it. It just kind of bulldozes the whole thing and rewrites it.

**Jason Gong:** Okay, so content strategy, try to figure out some way of, like, showing value of refreshes, which I, like, deeply believe in, you know, like, we just have to, like, be a little tactical and just show them it's working.

**Jason Gong:** And then, yeah, and then there's this, like, side project of, like, trying to make everything better, which I'll loop you guys into as soon as that gets kicked off, hopefully this week.

**Jason Gong:** And, yeah, and I'll try to share more there.

**Jason Gong:** then I think another thing I noticed is just, like, I think there's probably some just, like, basic things we can do to the page, like add a meta description.

**Jason Gong:** Like, I can't believe we don't have one.

**Jason Gong:** So I think that would help on the dev side.

**Jason Gong:** So I'm trying to get, um, Ed, and, uh, and your colleague, I just noticed, get him handled.

**Jason Gong:** And Okai added and me added as well.

**Jason Gong:** then once we're in there, I think we can spend a bit of time just like iterating.

**Jason Gong:** I mean, the main thing is building the Auggie CLI thing, but I think for the blog, there's just like a ton of low-hanging things to do there.

**Edin Abazi:** So I just had a quick question about that.

**Edin Abazi:** Like, are we basically just going to their code base and just adding the template library thing as like a separate page?

**Edin Abazi:** And it's going to be connected to their Sanity, already existing Sanity, right?

**Jason Gong:** I think that's the idea.

**Jason Gong:** mean, I was thinking, let's see if I can pull it up.

**Jason Gong:** So as a V1, it just kind of needs to be thrown up in any format.

**Jason Gong:** I think, I mean, you tell me if like the design you guys did works well with Sanity.

**Jason Gong:** I think the V1 could be.

**Edin Abazi:** mean, Sanity is just like the data layer.

**Edin Abazi:** doesn't really look like it's not connected.

**Edin Abazi:** Well, guess my question would be, are we putting it in a separate Sanity installation or the one they are already using?

**Jason Gong:** I think keeping it together would be fine.

**Jason Gong:** There is a thread around having some community way of contributing to it that I guess we should think about.

**Jason Gong:** I feel like it's probably best if that can live in like an open source repo and then somehow that gets synced to Sanity maybe.

**Jason Gong:** Like I think that is worth the thought of how you would do that.

**Jason Gong:** Like they do want an approval flow.

**Jason Gong:** They don't want to open it completely up to everyone.

**Jason Gong:** Yeah.

**Edin Abazi:** We can, like depending on the timeline and how quickly we want to move with this.

**Jason Gong:** We can definitely set up some.

**Jason Gong:** Yeah, think that could be a V2, like, for example, just V1, all this.

**Jason Gong:** Insanity.

**Jason Gong:** mean, for the most part, these pages are quite simple.

**Edin Abazi:** Yeah.

**Edin Abazi:** Just a lot of, like, little fields, but, like, in general, it's quite straightforward.

**Jason Gong:** Yeah.

**Jason Gong:** And then we need kind of a little workflow to do this, so I gotta get started on that.

**Jason Gong:** And then, yeah, again, I think, like, a checklist would be nice just to show them we're thinking about it, but, like, a V2, I think, could be the kind of submission part of this, which is not, like, super critical.

**Edin Abazi:** Okay.

**Edin Abazi:** That reminds me, I wanted to ask about the GrowthX engineers thing that you mentioned for Sanity.

**Edin Abazi:** How, like, what exactly were you imagining?

**Jason Gong:** Wait, sorry, what is that?

**Jason Gong:** GrowthX engineers.

**Jason Gong:** Oh, right, because we want to say.

**Jason Gong:** It's not going to be, like, public-facing...

**Jason Gong:** Yeah, I think we do want it to be public-facing.

**Jason Gong:** I think just, like, the most bare-bones, like...

**Jason Gong:** Like, developer-looking thing you want to spin up.

**Edin Abazi:** Yeah.

**Edin Abazi:** Like, publication, basically, right?

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** Just, like, very simple.

**Jason Gong:** There's a collection page, and there's a blog page, and that's it.

**Jason Gong:** Like, you don't even have to do any of the, you don't have to do related posts, you don't have to do, like, author pages, just, like, as very well.

**Edin Abazi:** We do want it to look good, though, right?

**Jason Gong:** Honestly, it doesn't even have to look amazing.

**Jason Gong:** I think that engineers just wanted a place to, like, play with our workflows, and then they'll kind of make it a little meta, and, like, talk about what they're doing.

**Jason Gong:** So.

**Edin Abazi:** I mean, still, like, I'll have Mergium or somebody else and just, like, design a basic branded view.

**Edin Abazi:** Okay.

**Jason Gong:** That sounds good.

**Jason Gong:** I was thinking, yeah, if you wanted to reuse the search stuff, it kind of works, but you have to totally feel free to do whatever.

**Edin Abazi:** Okay.

**Edin Abazi:** I was just trying not to make it take too long.

**Edin Abazi:** Yeah.

**Jason Gong:** Okay, yeah.

**Jason Gong:** So this will be our kind of, like, other bet.

**Jason Gong:** And then the newsletter, I think you're still doing, Marisol, is that right?

**Marisol Smith:** Yeah, yeah.

**Jason Gong:** And then lastly, I think Suleiman's still looking into some sort of, like, automation reporting.

**Jason Gong:** Did you say anything, Natalie?

**Jason Gong:** Any progress there?

**Nathalie Schrans:** Um, I haven't seen any progress.

**Nathalie Schrans:** Let me see the last thing.

**Nathalie Schrans:** Let's see.

**Nathalie Schrans:** There's just a lot to scroll through.

**Nathalie Schrans:** Um, but I, like, gave him the instructions and the video recording, but I don't think I've seen anything.

**Nathalie Schrans:** I will follow up in the thread.

**Nathalie Schrans:** just need to find.

**Nathalie Schrans:** Okay.

**Jason Gong:** Um, but, um...

**Jason Gong:** Um...

**Jason Gong:** Um...

**Jason Gong:** Um...

**Jason Gong:** Um...

**Jason Gong:** Um...

**Jason Gong:** Yeah, I think it's just, I think especially with Augment, there's so many random threads that are outside of the regular content.

**Jason Gong:** It's just up to us to kind of keep those going.

**Marisol Smith:** Suleiman shared a Looker Studio dashboard that he was working on.

**Marisol Smith:** Let me find it.

**Nathalie Schrans:** Like a while ago?

**Marisol Smith:** Last week, I think.

**Nathalie Schrans:** Okay.

**Marisol Smith:** Um, let me see.

**Marisol Smith:** Oh, he responded today.

**Jason Gong:** It's not finished.

**Nathalie Schrans:** Oh, where did he respond, Jason?

**Nathalie Schrans:** About the dashboard?

**Jason Gong:** Yeah, in the thread on Wednesday, he responded an hour ago and said he was working on it.

**Jason Gong:** Um.

**Jason Gong:** Oh, wait, sorry.

**Jason Gong:** Was this something else?

**Jason Gong:** Oh, no, my bad.

**Jason Gong:** That was a...

**Jason Gong:** bad.

**Jason Gong:** Oh, bad.

**Jason Gong:** Different thread.

**Marisol Smith:** I left a link in the chat.

**Jason Gong:** Let's see what that shows.

**Jason Gong:** Sorry, which chat?

**Marisol Smith:** Ah, here in, in Zoom, let, I can share it in the channel.

**Jason Gong:** Let's see what that shows.

**Jason Gong:** Let's see

**Jason Gong:** Okay, I guess I don't want to think.

**Jason Gong:** Yeah, I mean, I guess essentially what we're doing for Augment is like, we're still moving super fast, which is difficult in itself, but we're trying to kind of steer this to a more structured, stable place where it doesn't feel like we're kind of scrambling to like find 30 things to publish every week and it not totally making sense.

**Jason Gong:** Which I know feels really weird.

**Jason Gong:** think the way we do that is, like, kind of the content strategy, carve the lanes there.

**Jason Gong:** I think we need to start, like, breaking up guides into, like, different sections, or maybe just having tags.

**Jason Gong:** So, like, at least it doesn't feel like just a huge soup of, like, content.

**Jason Gong:** So even for us, like, mentally, it's, like, a little bit easier to manage.

**Jason Gong:** We need to fix this quality thing, which I think is mostly around, like, picking easier content to publish for a few weeks so we can get ahead of the quality and figure out what our process is for that.

**Jason Gong:** And then, yeah, just kind of, like, fix the pages up a little bit and bring some polish to that.

**Jason Gong:** Like, do you feel like the titles and stuff like that could benefit a little bit?

**Jason Gong:** Like, a lot of the titles are very specific.

**Jason Gong:** Which is fine, but I think once we loop in what prompts we're targeting, it's pretty clear a lot of times what content they're going for.

**Jason Gong:** Like the AI coding prompt, for example, it's basically only citing things that follow this in 2025 structure.

**Jason Gong:** So it's, I think we need to like somehow loop that into how we think about creating the articles.

**Jason Gong:** I mean, it seems like super surface level, but I mean, if that's what gets cited, then it is what it is.

**Jason Gong:** Like this one, for example, I was looking at, basically everything ChatGPT cites is basically like top AI coding tools in 2025.

**Jason Gong:** Like, you know, 2025, 2025, 2025, like we should just...

**Jason Gong:** Like, already added it to the title, but just, like, think about that a little bit in publishing.

**Jason Gong:** This one dropped out, at least yesterday.

**Nathalie Schrans:** I think I'm just looking through, I did a search of, like, all our best tool articles, and a lot of them do say for 2025, but a lot of them don't.

**Nathalie Schrans:** And another thing that we need to be mindful of, and I think this is what happens, it's just, like, publishing such a large volume, and I think the URL slugs are auto-generated.

**Nathalie Schrans:** But not having numbers and dates, or numbers and years in the URL, which we can go back and fix that once we know these are articles that are performing well, and it's worth doing that, because we just set up a free direct.

**Nathalie Schrans:** And it should be a huge issue.

**Nathalie Schrans:** Sometimes it may affect SEO a little bit, but you don't have to worry about that yet.

**Nathalie Schrans:** It's not something you're doing right now.

**Nathalie Schrans:** But that's just something I'll look at.

**Nathalie Schrans:** well, mean, Marisol, I understand the processes.

**Nathalie Schrans:** SULAMAN stages them in Sanity.

**Nathalie Schrans:** And then in the past, you have just been going through and making sure that they look good before we actually hit publish.

**Nathalie Schrans:** Is that something that you, that we should just split up moving forward or that you would continue doing?

**Nathalie Schrans:** Because I think that's just where we would need to check the slug to make sure it doesn't have that and that makes sure that the title has a year.

**Nathalie Schrans:** Or, you know, for, you so that makes sense.

**Marisol Smith:** Yeah, I, I've been doing the, this workflow with Suleiman over the last two weeks.

**Marisol Smith:** So it's very recent and, yeah, and I didn't.

**Marisol Smith:** I'm really explaining the ticket how to do the URL slug, because I run the title to these SEO SERP simulators, but probably I should do that before sending the articles.

**Nathalie Schrans:** Okay, so you run the title after it's already been staged and before you hit publish.

**Nathalie Schrans:** Okay, I see.

**Nathalie Schrans:** Yeah, mean, if that's something that you can do in your workflow, I think that would be good.

**Nathalie Schrans:** But I mean, I was, I can look through what we have in Sanity.

**Nathalie Schrans:** Can you map the articles that need to be updated?

**Marisol Smith:** And you just send me the list and I do it.

**Marisol Smith:** Because we can update them in Sanity.

**Marisol Smith:** And then we just ask to index it again.

**Marisol Smith:** Okay.

**Nathalie Schrans:** Even if we not need to, we changed the URL slug, would we not need to set up a redirect?

**Marisol Smith:** I mean, I don't know.

**Marisol Smith:** Honestly, I don't know how that could work in Sanity because we just have the editor there.

**Jason Gong:** I mean, think once it gets added, like all this stuff we can do.

**Jason Gong:** I would say for redirects, I guess.

**Nathalie Schrans:** Yeah, let's not worry about that now.

**Jason Gong:** Look here.

**Jason Gong:** I mean, don't like kill an article that's like doing well, but if it's like got no impressions anyway, like I would not care that much about a redirect.

**Jason Gong:** But if you're doing like a listicle that's already, like if you're doing this one, would definitely do a redirect, you know, to remove the eight out of the URL.

**Nathalie Schrans:** Yeah.

**Nathalie Schrans:** know what to do.

**Jason Gong:** Um.

**Jason Gong:** you.

**Jason Gong:** Cool.

**Jason Gong:** Okay.

**Jason Gong:** Let's see.

**Jason Gong:** Yeah.

**Jason Gong:** mean, I repeated a couple times, but like the strategy and then I know content quality from a workflow is really bad, and that's definitely on top of my mind.

**Jason Gong:** But I don't think we even get to a spot where we can fix that until we get them to buy into strategy and content quality.

**Jason Gong:** So I guess pick our battles and the articles you think deserve like that time.

**Jason Gong:** Like it could literally just be like two articles a week.

**Jason Gong:** It doesn't have to be 30, you know, where we spend the time to edit and make them better so that they at least have a chance of ranking.

**Jason Gong:** Yeah.

**Jason Gong:** And then we go from there.

**Jason Gong:** And please let me know if you feel anything's painful, especially around the workflows, because I'm trying to spend some time on that this week.

**Nathalie Schrans:** Yeah, I think that's probably where we should spend our time.

**Nathalie Schrans:** don't think editing was helpful for me because I could see kind of what things needed to be improved in the workflows.

**Nathalie Schrans:** So I can spend more of my time, I mean, after building up the content roadmap, I can spend more time helping me with that.

**Nathalie Schrans:** I'll be out of the office this Friday and Monday.

**Nathalie Schrans:** I just, I have a wedding and then I'll be traveling home.

**Nathalie Schrans:** so after that, I can, or I mean, before that and then after that, depending on where we end up progress-wise.

**Jason Gong:** Okay.

**Jason Gong:** Um, he, cool.

**Jason Gong:** Sounds good.

**Jason Gong:** Let's just, uh, yeah, well, we can sync, um, maybe tomorrow.

**Jason Gong:** I think, before the call on Wednesday, Natalie, whatever you're doing already with the, Yeah.

**Jason Gong:** definitely.

**Jason Gong:** Um.

**Jason Gong:** Well,

**Jason Gong:** Summaries and agendas, those were great, so please keep doing those.

**Jason Gong:** And then, yeah, as soon as Ed's added to the repo, can start making some of these changes.

**Jason Gong:** So I'll keep bugging him for that.

**Nathalie Schrans:** Yeah, and I'll prep the meeting agenda for the call tomorrow.

**Jason Gong:** Okay.

**Nathalie Schrans:** Because I mean, moving forward for August, sorry, I realize I'm just coming late for just an internal single, are we, because right now we've been having that data in like previous meeting agendas, are we just not doing that moving forward because we're, the idea is that we're going to have this dashboard.

**Jason Gong:** Yeah, so let's assume I can do it.

**Jason Gong:** guess by tomorrow, if we don't have it, I guess maybe we create it.

**Jason Gong:** My vision for that was like, it's all in Airtable because it's a lot easier to work with, kind of pulling it out with little automations and stuff.

**Jason Gong:** And then, yeah, there's just kind of a row for each of those metrics that I highlighted.

**Jason Gong:** So yeah, yeah, don't worry.

**Jason Gong:** Okay.

**Nathalie Schrans:** then I'll just talk about progress and what we're doing this week and what's coming up.

**Jason Gong:** Like a normal agenda.

**Nathalie Schrans:** Okay.

**Nathalie Schrans:** Sounds good.

**Jason Gong:** All right.

**Nathalie Schrans:** Thanks, everyone.

**Edin Abazi:** I jotted down five action items.

**Marisol Smith:** Okay.

**Jason Gong:** All right.

**Jason Gong:** Could you share with Alie?

**Jason Gong:** Yeah, I think keeping the notes.

**Nathalie Schrans:** Yeah, at the bottom of the document.

**Marisol Smith:** I see them.

**Nathalie Schrans:** I'll share in our channel, too.

**Nathalie Schrans:** you.

**Nathalie Schrans:** I'll start doing that also moving forward.

**Jason Gong:** Cool.

**Jason Gong:** All right.

**Jason Gong:** I'll talk to you all later.

**Nathalie Schrans:** Okay.

**Nathalie Schrans:** Thanks, everyone.

**Nathalie Schrans:** See you.

**Jason Gong:** Bye.

**Edin Abazi:** Bye.
