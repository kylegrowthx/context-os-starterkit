# Director Standup

<metadata>
date: 2025-07-30
time: 19:00 UTC
duration: 32 minutes
organizer: Megan Dickey
participants: Jakub Rudnik, Dave Capone, Matthew Panzarino, Jason Gong, Mara Leighton, Darrell Etherington, Andi Bailey, Megan Dickey
fathom_recording_id: 77511962
fathom_url: https://fathom.video/calls/365784719
share_url: https://fathom.video/share/vXzBXJMiBqyEsGUAwdYTjBonc32iv7_K
source: fathom
enriched_on: 2026-03-03 09:15 UTC
</metadata>

---

## Summary

GrowthX's director team aligned on a major new initiative: implementing LLMs.txt, a proposed web standard that helps AI chatbots understand website context and find important content, with Dave developing the workflow over 1-2 weeks. The team debated the experimental nature of LLMs.txt and similar tools like Scrunch—acknowledging they're directional indicators rather than proven metrics—but agreed to test and potentially share findings publicly, particularly with interested clients like Galileo and Monograph. Meanwhile, Webflow account management was fixed: the team upgraded pod aliases so delivery staff can access client accounts without getting kicked out.

---

## Context

This is GrowthX's weekly director standup, held with the delivery and operations leadership. The team includes GrowthX executives and one external consultant (Mara Leighton from GrowthX Labs). The meeting focuses on operational updates, client deliverables, and new tactics being tested in the AI visibility and SEO space. Mara joins from different locations (in this case, a middle school classroom) and serves as a collaborative partner on client accounts.

---

## Relevance

**To GrowthX Delivery:**
- LLMs.txt workflow represents a new tactical offering for clients looking to increase AI visibility; Dave needs 1-2 weeks to finalize it with URL prioritization and newest-content logic
- Webflow pod aliases issue is resolved; teams should now have stable access to client accounts (Suleiman available as backup)
- Need to communicate LLMs.txt carefully to avoid overpromising—position as directional experiment, not magic fix

**To CheckThat / AI Visibility:**
- LLMs.txt is an emerging standard being adopted by Stripe, Langchain, and others; GrowthX positioning to test and publicly share results
- Scrunch and LLMs.txt sit in same category: directional measurement tools, not precise metrics; team will monitor ChatGPT server logs (via Geo tools) to see if LLMs.txt file gets used
- Debate between skepticism (Darrell: "placebo") and pragmatism (Jason/Dave: better to test and share findings than stay behind)

**To GrowthX Business Development:**
- Galileo and Monograph are receptive to new LLM tactics; opportunity for account expansion if Mara/team can offer Galileo LLMs.txt in next 2 weeks
- AirByte Reddit posting strategy working; shared with other clients as a low-cost discovery tactic
- Clients asking about experimental tools (GEO, LLMs.txt) signals market pressure on their CMOs—GrowthX can position as forward-thinking partner willing to test new approaches

---

## Overview

- New LLMs.txt file standard discussed; team to create workflow for implementation
- Webflow account issues resolved; pod aliases added to client accounts
- Debate on value and measurement of new SEO/LLM initiatives like Scrunch and LLMs.txt
- AirByte's Reddit posting strategy shared as potential tactic for other clients

---

## Key Topics

### LLMs.txt Implementation

  - New proposed standard for helping LLMs understand website context
  - Dave developing workflow to generate LLMs.txt files for clients
  - Debate on effectiveness and measurement of impact
  - Team agrees to test and potentially share results publicly

### Client Updates

  - Monograph interested in LLMs.txt implementation
  - Galileo receptive to new AI/LLM tactics, including Reddit posting strategy
  - AirByte seeing success with posting content to their Reddit user page

### SEO and LLM Measurement Tools

  - Discussion on value of tools like Scrunch for measuring LLM visibility
  - Team agrees these are directional indicators, not precise measurements
  - Importance of clear communication with clients about experimental nature

### Webflow Account Management

  - Pod Webflow aliases now added to client accounts after upgrade
  - Will help reduce team members getting kicked out of Webflow

---

## Action Items

**Andi Bailey**
- Follow up w/ Bianca for list of registrants for Marcel's Fri event; share w/ team for engagement

- Create/maintain list tracking pod Webflow aliases associated w/ specific clients


**Dave Capone**
- Generate LLMS.txt file for Galileo (Mara's client); sync w/ Mara offline re: details

- Complete workflow for generating LLMS.txt files; incl. URL prioritization, newest URLs; est. 1-2 wks

- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts


**Megan Dickey**
- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts


**Mara Leighton**
- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts


**Jason Gong**
- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts


**Darrell Etherington**
- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts


**Matthew Panzarino**
- Prioritize adding pod Webflow alias to assigned clients; esp. those w/ frequent kickouts

---

## Transcript

[Note: The first ~20 minutes of this recording captured pre-meeting small talk between Megan and Mara about pets and Mara's location (calling from a middle school classroom in Europe while traveling). The substantive meeting begins around the 20-minute mark when Andi calls the meeting to order.]

**Andi Bailey:** Alright, how's everybody doing?

**Mara Leighton:** Definitely busiest call day and I just got out of them, so I'm feeling pretty good.

**Andi Bailey:** I've had an hour free since 9am. Today is Geo Day. But two things. First, did you guys get a sense of how many of your clients are signed up for Marcel's thing on Friday? Is there anybody else that we need to bump?

**Mara Leighton:** No one has asked about it. I believe the clients that I specifically sent it to, at least one of them could attend. But I can see if there's anyone else that we haven't shared it with.

**Andi Bailey:** Maybe we can get a list from Bianca on who's registered so that we can follow up too. I will take that action item. And then the other piece, I'm going to throw it over to Dave, because we got a question last week from Monograph about Webflow's new feature where you can upload LLMs.txt. Dave, can you explain why that's important and how we get it for everybody?

**Andi Bailey:** We only know that you can do this in Webflow right now. Dave's working with Nico on a query so we can generate and upload that to Webflow. But the next step is figuring out what other CMSs we can do this for.

**Dave Capone:** Thanks. So, LLMs.txt. Basically, this is like a treasure map to LLMs for your website. We're trying to let the bot know the context of your website, your offerings, brief descriptions, and a list of the best content on the site. There's a website, llms.txt.org, that has all the requirements for this new standard. Think of it as a complement to robots.txt. For crawlers like Google, you have robots.txt for search engines. LLMs.txt is made for chatbots—Claude, ChatGPT, Perplexity—for them to gain knowledge about the site and direct them to the best things. I've been working with Nico and just finished the ticket so I can walk through the requirements and how this will be great for our clients. The problem is, if we use Claude to generate the LLMs.txt file right now, there's limitations. For each query, it's limited to 10 URLs, so it doesn't give an accurate representation of the website because it only slims itself to 10 URLs. So we need a workflow to break this into smaller tasks: get the context of the client and what's important, identify the site structure, tie in performance data, and generate the file. Those are the five core things we have to do to be successful. I've got acceptance criteria and success metrics. Here's an example for Monograph: in markdown, it gives you company context broken into topics and sections, with a page and brief description directing the LLM to certain areas. Essentially a treasure map to all the best content on your site.

**Jason Gong:** Is there a limit to it? Like, for websites with a big blog, would you want every blog entry in here too?

**Dave Capone:** I think we need to test, Jason, because I don't have a good answer. The way it's described, it's for LLMs and it's a separate file. So it works a little differently than sitemap.xml or robots.txt. I think there's going to be organic discovery from the LLM. So it'll organically find content. I think the purpose is more like, "Here's the best things on our site, so you don't have to go find it yourself." So I think it'll have what we tell it is important, and then what it finds organically, for a full range of URLs and context of your site.

**Darrell Etherington:** So this is like nothing at the moment, right? This is a proposed standard which none of the LLM makers acknowledge, accept, or participate in.

**Dave Capone:** It is a proposed standard, but it's being used. Folks are implementing it on their sites and seeing in server logs lots of usage from ChatGPT and other LLMs using this file.

**Jason Gong:** Some examples of that would be helpful. Because there's a difference between LLMs treating it as a special guide to your content versus LLMs just looking at it like everything else. But anecdotally, respected people have it. Langchain has one, structured like this. I think the part to get clear is how we communicate this to clients. We don't want to make it seem like this is something that'll change their life. It's more like there's not a ton of clarity, but it seems like it helps. Here are the data points.

**Dave Capone:** Yeah, I think the way we position this is that it would help increase the visibility of your most important pages to an LLM. I don't think the purpose is to give every page to an LLM. It's more like here's the context of our company and the most important content.

**Andi Bailey:** In terms of getting this, we already know one client asked about it. Is it something we should offer proactively? Or do we want to see if people ask about it? And then second, if we do this now, how are we measuring it? What's the metric we're looking at?

**Dave Capone:** For most CMSs we'll build this in. Webflow already has a delivery method where you can upload the text file. WordPress also has it through Yoast. If not, it's pretty simple—we can generate the file and email it to the client, and they can upload it to the root URL. Should we be doing this? I think yes. It's a hot topic for Geo and it helps increase visibility.

**Jason Gong:** I also think we should do it. I think we just need to be careful about how we measure it. I don't know if this on its own is measured. It's more like, are you being cited or mentioned more? Like the way you measure it would need server logs, right? If ChatGPT is finding this file, how often is it using it? If it's using it quite a bit, then I think that's a success metric. And is it increasing the number of sessions from ChatGPT, or is it citing it better in ChatGPT? If it's getting hit more than your home page, that says something. Still haven't had time to work on getting server logs, but I think the Geo tools are adding it soon.

**Dave Capone:** The screen we're looking at here is Stripe. This is a very similar output of what they're doing. I think it's something we should test. We have an iteration now of how it creates the content, but we don't know if that's the best way. So there's a test and learn scenario. Maybe our company context is too much and we dial that back. Maybe that allows us to add more landing pages or we go into each product and break that out. There's an opportunity to test and learn on best practices.

**Darrell Etherington:** I don't want to raise this with anyone unless it's brought up, because all of this is placebo at the moment. I get it, especially for CMOs whose CEOs are asking them how to do stuff. But we don't know anything about this. There's possible knock-on effects where if LLMs cite this markdown version instead of the real thing, people get sent to a weird version of your website. So I'm not going to raise it with anybody because I can't convincingly sell it.

**Jason Gong:** I don't think I've seen the LLMs.txt being cited. But did you guys see the Webflow thing? They're going to give you a Geo score. It's like placebo, but it's still valuable. We need to keep showing we're investing here. If you frame it as "here's a bet a lot of people are making," like Stripe, Langchain, and everyone else, let's run an experiment. That will show we're being forward thinking. We're not pretending there's a magic bullet or selling snake oil, but showing we know and are pushing the envelope on Geo.

**Andi Bailey:** Darrell, Airbyte is being annoying on all our publishing pieces. So let's give them something else we're working on. Here's another option. Because they're on WordPress.

**Darrell Etherington:** I highly doubt specifically them. I feel like they're going to be allergic to that of all the customers because they're more sophisticated.

**Andi Bailey:** I can't help but present options. It's been a real problem for me professionally.

**Jason Gong:** Tactically, I had to look at the prompt you created, Dave, but it didn't look super complicated. I think we can generate just this file for all the clients. And then individually, if you think it'll help, use it. If not, don't. As a company we're going to be talking about it. So you're going to have to deal with that. On Friday we're going to have a two-hour session where I'm going to talk about LLMs.txt—not as snake oil, but as something people are trying. Even tracking prompts is placebo to some degree.

**Darrell Etherington:** We haven't talked about that. You don't know what prompts anyone's using. That is a fully procedure.

**Mara Leighton:** I think Scrunch is full nonsense.

**Darrell Etherington:** I vibe-coded it in five seconds and it's... that is actually fine. I'm talking about this LLMs.txt thing.

**Jason Gong:** It's the exact same thing, right? But we need to do it. I think that has changed. We need to do something there. I don't want to be the old man shouting nothing's changed, the fundamentals remain the same.

**Darrell Etherington:** That's why I'm like, it's a dynamic new time. You can actually focus on quality. You don't have to worry about any of this stuff because it was a hack. You could hack SEO. It was hackable. But then they ask you how you measure it.

**Jason Gong:** How would you answer that? I think that's the main reason we're monitoring. We need at least some kind of directional marker.

**Darrell Etherington:** Yeah, but that's not measurement. That's a made-up number. I pushed Scrunch. You can look at the calls where I talk about Scrunch. I don't talk about it in a way that's negative. I talk about it in a way that's factual and clear—this is a directional indicator. It can help you think about how you might show up.

**Jason Gong:** Yeah, I mean, that's valuable in itself. I don't think we're framing it as this translates to traffic.

**Matthew Panzarino:** At least I haven't, and I don't think we should. Yeah, I talked about it with Monograph today and it turns out he knows the investors in Scrunch. But I laid it down and said, look, it's one step above tea leaves at this point, but it could provide us some directional measurements. Especially if they're looking for specific clusters of prompts. They specifically want non-software questions to see if they showed up in non-software questions. Like, what's the best software for managing my team's time as an architect? Sure, we might show up there. But what if it's like, "I have this really weird problem, I'm unprofitable, and I don't know how to fix it." And it's like, "Maybe you should try Monograph." That's what they're most interested in. We're going to go to forums, architecture forums, subreddits, scrape those for questions, and build clusters for them. But I was very straightforward with him: nobody knows exactly how this will play out. He said, "Yeah, I know the investors in Scrunch," so you don't have to believe in it. But it's something. And I think as long as we present it as "we don't want to be left behind, so we're willing to experiment," that puts the labor on us to figure out if it's valuable to you over time.

**Darrell Etherington:** Maybe they'll figure it out. And I think that is helpful. But this is like putting up a dream catcher in your house.

**Jason Gong:** No, I think it's more valuable than that. We're sampling a presumably infinite number of prompts to see the direction.

**Darrell Etherington:** Oh, I mean that is actually fine. I'm talking about this LLMs.txt thing. I don't necessarily trust Raymond Martinez, VP of SEO, about his opinion on this, because he has a biased opinion. But this Scrunch stuff, I don't think they're doing anything technically interesting. But it is interesting to think about how your customers are thinking about your product and what questions they might be asking. It is useful in that regard.

**Jason Gong:** It's in the same domain as Nielsen surveys, where people ask, "Have you heard of YouTube?" And you say yes. If you sample enough people, it gives you a rough number.

**Darrell Etherington:** I literally described it as that on the call. It's like you're a Nielsen family with random sampling, hopefully representing the population.

**Jason Gong:** I think it'll get better. But the LLMs.txt thing—I think for the clients I'm on, they would want it, even if it's just an experiment. We start looking at if it's even getting pinged. So I think it's worth the investment to create a workflow where it's available for everyone. And then whether you want to use it or not is up to you.

**Mara Leighton:** I think for Galileo, I would want to offer this. They're under temperature, interest, pressure. I offered them, with all the caveats we've mentioned, which helps solidify the context we've been providing to them over the last few weeks. But I think just being proactive and aggressive would help from a relationship standpoint to share. With all the caveats, I shared the Airbyte Reddit posting with them. Thank you, Jacob. They were very excited about that. We talked at length about how there's a shelf life loophole potentially. Test it and see how it goes. But from that, they're getting a lot of pressure, so it's just partnering with them on test projects and being very realistic—you might not glean anything, it might not work. But we're coming to you with ideas. That's a use case where this would be beneficial.

**Dave Capone:** Yeah, we can sync offline and I'll try to generate one for you.

**Mara Leighton:** That'd be great. I would appreciate it.

**Matthew Panzarino:** We're not countering any of your points. But Mara, with the Reddit thing, as far as I understand, you were suggesting they populate their subreddit with topics that could be indexed by LLMs, correct?

**Mara Leighton:** It was what Jacob showed us in yesterday's Director Sync with Airbyte. They've been publishing from their own account—not in subreddits. They've been able to see them showing up in related LLM searches, though not every single time.

**Matthew Panzarino:** Did they create their own subreddit?

**Darrell Etherington:** No, they're just posting to their own account. Like you slash whatever.

**Matthew Panzarino:** Yeah, it's their subreddit, but it's "you" instead of "all."

**Matthew Panzarino:** Yeah, okay, cool. This is great. I actually really like this approach. I didn't remember they were posting like that. This makes a lot of sense because I think most LLMs over-index on Reddit for questions.

**Mara Leighton:** We talked about community forums. So it was helpful to pick back up and our key stakeholder is feeling a little bit more supported. Anyway, they just hired a new person. So it was nice for relationship building to partner with him. It also makes him look good internally. They were very receptive.

**Matthew Panzarino:** I think it would benefit a lot of our clients. I'm going to be careful not to mention it until they get content ramped, because Monograph doesn't have anybody to do this. It would be like—careful they ramped. And I'll be like, sure, but I would have to build a pipeline for it, which we can do. I'm fully confident we're capable of generating the content. And then we'd figure out a way to automate publishing because I don't want to manually paste into Reddit. I'm pretty sure we could do something like that—have them approve batches and post one thing to Reddit a day automatically for the next month. But I also need to get their pipeline to ship 10 articles a week.

**Jakub Rudnik:** I don't know, I haven't said anything yet, but I do think that at least bringing up stuff that Dave's finding, we should throw together and use some of this time. The worst thing is an experiment where nothing happens. And we can talk about that on a Marcel workshop or LinkedIn. Probably more likely LinkedIn. That's really useful for us—testing and debunking, because there's going to be a lot of snake oil merchants on LinkedIn in this area. So we should be really skeptical, but then how do we actually prove that out as worthwhile time? We have to carve that time. I think that's very difficult right now. Personally I want to do some of those things, but where can we? If we can carve that time, it can be really impactful. The Airbyte stuff is lucky they brought it to us. I don't know how we action something like that without giving away trade secrets a client might have found. So we have to do that close to the vest. But if we can find those public things, that opens up a lot where we don't have to worry about stepping on anyone's toes or ruining their creativity. So I'm glad. Thanks Dave for surfacing it. We should just all be on the lookout for those. What could we go try since we have 40 clients and websites at our disposal to some extent?

**Andi Bailey:** So Dave, in terms of actioning those for those who want to, or when they bring them up with clients, we have the workflow now. And so this is just a manner of creating a ticket and assigning it to you, or what's the process?

**Dave Capone:** The workflow—I created a ticket in Linear to build it. There's additional requirements on our end. I want to build into it because the way the prompt works now just randomly grabs URLs. I want to add priority to the URLs it grabs. If we have the most important URLs and newest URLs, I can run that through the prompt. That's pretty easy. So I can create these. But we need about a week or two to build the workflow.

**Mara Leighton:** Follow-up question: when would we be comfortable softly sharing this with clients as a possibility? Just so I don't get ahead of myself on mentioning it to Galileo.

**Dave Capone:** Let's talk offline. I think there's a few things we can do, but it's close. Comparing this to the free one that's out there, ours is really good compared to that. So let's take a look.

**Andi Bailey:** Yeah, see if you can get this ready by end of the week. That would be great so we can start doing it next week. What's the blocker on getting it done by then?

**Dave Capone:** I'll talk to Nico about it.

**Andi Bailey:** Okay. We're at time, but just last thing: Webflow accounts. I know they didn't work the first time we tried to add them. We thought we could just add them as free users. We were wrong. We've upgraded all the seats. So your pod Webflow alias should now be added to your clients. I'm going to start a list so we can track which pod aliases are associated with which clients. If clients move around, we probably don't want to move the emails. But that's a follow-up for me. Especially if your clients are getting kicked out of Webflow, let's prioritize this for this week. That should give them a surprising amount of time back. Or they could just send it to Suleiman. So two options there should both save you time.

**Jakub Rudnik:** Yeah.

**Dave Capone:** Thanks.

**Dave Capone:** So, llms.txt.

**Dave Capone:** Basically, this is like a treasure map to llms for your website.

**Dave Capone:** Basically, we are trying to let the bot know the context of your website, our offerings, brief descriptions, and then a list of, like, the best content that we have on the site.

**Dave Capone:** So, I've developed, so there's a website, it's llms.txt.org, or wherever it is, that has all of the requirements for the standard that they're using for this new file.

**Dave Capone:** Think of it as, a complement for llms.

**Dave Capone:** So, we have, like, robots.txt for crawlers, right?

**Dave Capone:** So, for, like, Google and search engines, llms.txt, which is a lot to say out of my mouth at one time, is made for, like, chats.

**Dave Capone:** So, like, it's going to be for chatbots.

**Dave Capone:** So, for Claude, or for, like, chatbots.

**Dave Capone:** GPT or, you know, perplexity for them to gain some knowledge about the site and then direct them to like the best things.

**Dave Capone:** So I'll share kind of what we've put together.

**Dave Capone:** I've been working with Nico on this and I actually just finished the ticket so I can kind of walk through the requirements and then how this is going to be great for our clients.

**Dave Capone:** So let me share that.

**Dave Capone:** Okay, so the problem statement is like if we use just Claude right now to generate the lms.txt file, what happens is that there's a lot of limitations.

**Dave Capone:** It does a pretty good job, so it'll go through, it'll take our artifact of the company context and it'll then crawl the site and then using a combination of the two, generate a list based off of the requirements that we put in there.

**Dave Capone:** The issue is that it's limited for each query that it does, it's limited to 10 URLs per query.

**Dave Capone:** So it doesn't really give you an accurate representation of the website or the client's site because it's slimming itself to only 10 URLs.

**Dave Capone:** So that's essentially why we need a workflow so that we can break this up into smaller tasks that then we can have, one, be able to get the context of the client and what's important and who their ICP is, all the good things, any data points or et cetera for the bot.

**Dave Capone:** It's to identify the site structure and make sure that we are giving a good context of how the site is organized to the LLM and then tying in performance data and then generating the file.

**Dave Capone:** So those are kind of the five core things that we have to do to be successful with this new workflow.

**Dave Capone:** So I've got, like, acceptance criteria, you know, considerations, success metrics, but basically...

**Dave Capone:** So we want to go with this is, you know, I'm giving it all the direction it needs to do that.

**Dave Capone:** And then here's an example for Monograph.

**Dave Capone:** Basically, in Markdown, it kind of gives you, here's the company context broken out into topics or sections.

**Dave Capone:** So like core platform features, it gives you a page, a brief description of that page and directs the LLM to those certain areas.

**Dave Capone:** So essentially a treasure map to all the best content on your site.

**Jason Gong:** Is there like a limit to it?

**Jason Gong:** Like presumably like, you know, for websites with like a big blog, would you want every blog entry in here too?

**Dave Capone:** And that I think we need to test, Jason, because I don't have a good answer.

**Dave Capone:** Like the way that is described is this is for LLMs and it's a separate file.

**Dave Capone:** So it works a little bit differently than say like a sitemap.xml or, you know, robots.txt.

**Dave Capone:** But I essentially think it.

**Dave Capone:** Yeah.

**Dave Capone:** On one hand, there's going to be organic discovery from the LLM.

**Dave Capone:** So it's going to organically itself find content on our site.

**Dave Capone:** I think the purpose of this is more like, here's the best things on our site, so you don't have to go find it yourself.

**Dave Capone:** Whereas, you know, so I think it'll have what we tell it is important, and then what it finds organically to have a full, I guess, a full range of URLs and context of your site.

**Dave Capone:** So what it already is untrained on your content, whatever it discovers and trains itself on content, and then what we give it to train itself on content.

**Dave Capone:** So kind of those three things.

**Darrell Etherington:** So Jason's already used to my cranky mode, but this is like nothing at the moment, right?

**Darrell Etherington:** Like this is a proposed standard, which none of the LLM makers acknowledge, accept, participate in, whatever.

**Darrell Etherington:** Right, like.

**Dave Capone:** Well, yes, it is a proposed standard, but it's being used.

**Darrell Etherington:** So.

**Darrell Etherington:** It's being used by people, but not by the LLMs.

**Dave Capone:** Yes, by the LLMs.

**Dave Capone:** So folks are implementing this on their sites and seeing in logs, in server logs, lots of usage from, I guess, ChatGPT and other LLMs using this file.

**Dave Capone:** So they can...

**Jason Gong:** I mean, some examples of that would be helpful.

**Jason Gong:** Because I guess there's a difference between, like, the LLMs treating it as, like, a special kind of guide to your content versus LLMs just, like, looking at it like it looks like everything Yeah, they'll hit everything.

**Darrell Etherington:** You put a website on your trunk URL, they'll hit it or whatever, your home demand.

**Jason Gong:** But I mean, like, anecdotally, like, respected people kind of have it.

**Jason Gong:** So, I mean, we should have something.

**Jason Gong:** Like, I'm looking at, like, Langchain, they have one.

**Jason Gong:** It's roughly structured like this.

**Jason Gong:** Like, I think the part maybe to get clear is just, like, how we communicate this to clients.

**Jason Gong:** So, like, we don't want to, like, make it seem like this is some crazy thing that'll change their life.

**Jason Gong:** You know, like, it is kind of a...

**Jason Gong:** That in a direction where there's like not a ton of clarity, but it seems like it helps, you know, and here are the data points.

**Dave Capone:** Yeah, and I think the way that we position this would be that it would help increase the visibility of your most important pages to an LLM.

**Dave Capone:** Like, I don't think the purpose of this is to like, you know, give every page to an LLM.

**Dave Capone:** I think it's more of here's like the context of our company and the most important content that you need to know about.

**Andi Bailey:** And then in terms of getting this, like, well, we already know one client has asked about it.

**Andi Bailey:** Is it something that we should, well, something that we should offer proactively?

**Andi Bailey:** Like, do we even want to offer this proactively or do we want to see if people are asking about it?

**Andi Bailey:** Um, and then the second piece is like, okay, we do this now, how are we measuring it?

**Andi Bailey:** Or like, what is the metric that we're looking at to, if this is an experiment?

**Dave Capone:** Absolutely.

**Dave Capone:** For more to the fund.

**Dave Capone:** piece, that Thank

**Dave Capone:** Yeah, I think for most CMSs, we'll build this in.

**Dave Capone:** So like Webflow already has a delivery method for this where you can just upload the text file yourself.

**Dave Capone:** WordPress also has it through Yoast.

**Dave Capone:** So I'm pretty sure we'll see this being adopted through the rest of the CMSs.

**Dave Capone:** If not, it's pretty simple where we can generate the file and email it over to or give it to the client, and they can just have their team upload it to the root URL.

**Dave Capone:** But should we be doing this?

**Dave Capone:** I think it's probably like, I guess, yes, we should be doing this.

**Dave Capone:** It's a hot topic for like Geo and it helps increase like visibility.

**Jason Gong:** I also think we should do it.

**Jason Gong:** I think just like communicating, maybe we can think through it and then how you measure it.

**Jason Gong:** I don't know if this on its own is measured.

**Jason Gong:** It's more just like, are you being cited or mentioned more?

**Jason Gong:** It's like the way.

**Dave Capone:** Yeah, and I hope that if for us to find out if it's.

**Dave Capone:** Effective or not, would need server logs, right, because, like, basically, if, you know, ChatGPT is finding this file, and then, one, how often is it using it to reference it?

**Dave Capone:** Like, so if it's using it quite a bit, then I think that's a success metric, because then we know that it's finding it helpful and it's using it.

**Dave Capone:** And then, two, is it increasing the number of sessions that we're getting from ChatGPT, or is it citing it better in ChatGPT would be a better way of looking at that, I guess.

**Dave Capone:** So, one, definitely hard to find.

**Jason Gong:** I mean, if it's getting hit more than your home page, I think that says something.

**Dave Capone:** Yep, I agree.

**Jason Gong:** Still don't fully know how to get server logs, haven't had time to work on that.

**Jason Gong:** But I think the Geo tools are adding it soon, so maybe that's how we get it.

**Dave Capone:** The screen we're looking at in front of us here is Stripe, and this is kind of a very similar output of what they're doing.

**Dave Capone:** Yeah.

**Dave Capone:** And I think it's something we should test, right?

**Dave Capone:** Like, so we have an iteration now of how it kind of creates the content for this file, but we don't know if that's, like, the best way to do it or not.

**Dave Capone:** So I think there's just probably, you know, a test and learn scenario here where, okay, maybe our company context is too much and we can dial that back.

**Dave Capone:** And then, you know, maybe that allows us to add more landing pages or maybe we go into each individual product and break that out.

**Dave Capone:** But I think there's an opportunity to test and learn here on some best practices.

**Darrell Etherington:** I don't want to raise this with anyone unless it's brought up, frankly, because I just can't, like, it's placebo.

**Darrell Etherington:** All of this is placebo at the moment.

**Darrell Etherington:** And I get it, especially for CMOs who are freaking out because their CEOs are asking them how to do stuff.

**Darrell Etherington:** But, like, it doesn't, we don't know anything about this.

**Darrell Etherington:** It doesn't do anything in theory, right?

**Darrell Etherington:** Like, there's, I don't even think the indicators that you've cited are real indicators.

**Darrell Etherington:** Like, it's just a thing to make yourself feel good.

**Darrell Etherington:** Andy put it well, like security blanket, right?

**Darrell Etherington:** So I'm not going to raise it with anybody because I can't convincingly sell it, but there's harm in terms of site performance, in terms of like, if you, if they cite this thing instead of the other thing and the LLMs get confused and then send people in references to this weird markdown version of your website instead of the real thing, like there's all kinds of possible knock-on effects.

**Darrell Etherington:** So I don't know.

**Jason Gong:** I don't think I've seen like the LMTX being cited.

**Jason Gong:** But I mean, I, I don't know.

**Jason Gong:** I mean, it's like the, like, did guys see the Webflow thing?

**Jason Gong:** It's like, they're going to give you like a GEO score.

**Jason Gong:** It's like, it is placebo, but I mean, presumably it's still valuable, you know, like, I think we just need to keep showing we're investing here.

**Jason Gong:** I think if you frame this like this, like, if you really think it'll hurt, that's one thing, but it's like, you know, here's a bet a lot of people are making, like Stripe, like, you know, Langchain and everyone else, like, let's run an experiment here and add it.

**Jason Gong:** I think just that will show, like.

**Jason Gong:** Like.

**Jason Gong:** Kind of being forward thinking, you know, like at least on the marketing side, that's like, all we're investing in.

**Jason Gong:** It's like, we want to appear like we're forward thinking on Geo, and we're pushing the envelope there.

**Jason Gong:** Not pretending like there's like a magic bullet in selling snake oil, but like, like at least showing we're like, know, yeah.

**Andi Bailey:** Darrell, like, I would also say like, so Ambit, like, maybe it doesn't do anything, but also like, they're just being annoying on all of our publishing pieces.

**Andi Bailey:** So, like, let's give them some, like, hey, here's this other thing that we're working on as a company.

**Andi Bailey:** Like, you guys just want to see, like, how things do.

**Andi Bailey:** Here's, here's an option.

**Andi Bailey:** Because they're on WordPress, so.

**Darrell Etherington:** Yeah, I really highly doubt that.

**Darrell Etherington:** specifically them.

**Darrell Etherington:** Like, I feel like they're going to be particularly allergic to that of all the customers, because they're a little more sophisticated.

**Darrell Etherington:** But like, yeah, I just don't, I would much.

**Darrell Etherington:** I'd rather be the voice of reason when everybody is going crazy, presenting them with all these stupid things and the world's on fire.

**Andi Bailey:** I can't help but be, it's been a real problem for me, professionally.

**Jason Gong:** I mean, I think, like, at least tactically, like, I had to look at that prompt you created, Dave, but I think it would, it didn't look super complicated where I think we can generate just this file for all the clients.

**Jason Gong:** And then, I guess, individually, if you think it'll help you use it.

**Jason Gong:** If not, don't.

**Jason Gong:** I mean, as a company, we're going to be talking about it.

**Jason Gong:** So you're going to have to deal with that, unfortunately.

**Jason Gong:** Like, on Friday, we're going to a two-hour session where I'm going to talk about LN260, like, not in the way that it's snake oil and magic bullet to solve all your problems, but, like, we should be talking about all the things people are at least trying, you know?

**Jason Gong:** Like, even tracking prompts is, like, a placebo to some degree.

**Darrell Etherington:** You don't know what prompts anyone's using, but, like, here Oh, that is a fully procedure.

**Darrell Etherington:** We haven't talked about that.

**Mara Leighton:** I think Scrunch is full nonsense.

**Darrell Etherington:** I vibe-coded it in five seconds, and it's...

**Jason Gong:** It's the exact same thing, right?

**Jason Gong:** But we need to do it.

**Jason Gong:** I mean, I think that has changed.

**Jason Gong:** Like, we need to do something there.

**Jason Gong:** And I think, like, being the old man, like, shouting, like, nothing's changed.

**Jason Gong:** The fundamentals remain the same.

**Jason Gong:** Like, I don't want to be that, you know?

**Jason Gong:** I don't to be that either.

**Darrell Etherington:** That's why I'm like, it's a dynamic new time of, like, you can actually focus on quality.

**Darrell Etherington:** You don't have to worry about any of this stuff because it's, like, there was a hack.

**Jason Gong:** You could hack SEO.

**Jason Gong:** It was hackable.

**Jason Gong:** It was eminently But then they ask you, like, how you measure it.

**Jason Gong:** Like, how would you answer that?

**Jason Gong:** I think that's the main reason we're monitoring.

**Jason Gong:** Like, we need at least some kind of directional, you know, marker for, like.

**Darrell Etherington:** Yeah, but that's not measurement.

**Darrell Etherington:** That's not measurement.

**Andi Bailey:** That's a made-up number, right?

**Darrell Etherington:** Like, I push scrunch.

**Darrell Etherington:** I talked to, you can look at the calls where I talk about scrunch.

**Darrell Etherington:** I don't talk about it in a way that is negative.

**Darrell Etherington:** I talk about it in way that is factual and clear about that this is a directional indicator for you.

**Darrell Etherington:** And it can help you in that way, thinking about how you might show up in these interests.

**Jason Gong:** Yeah, I mean, that's in itself, like, valuable.

**Jason Gong:** Like, don't think we're framing it as, like, hey, this translates to traffic.

**Matthew Panzarino:** At least I haven't, and I don't think we should.

**Matthew Panzarino:** Yeah, I talked about it with Monograph today, and it turns out he knows the investors in Scrunch.

**Matthew Panzarino:** He's like, yeah, yeah, I know exactly how this is working, and I'm like, great, I'm glad.

**Matthew Panzarino:** But I just basically laid it down and said, look, it's one step above tea leaves at this point, but it could provide us some directional measurements, especially if they are looking for specific clusters of prompts because they specifically wanted non-software questions to see if they showed up in non-software questions.

**Matthew Panzarino:** In other words, like, what's the best software for managing my team's time as an architect?

**Matthew Panzarino:** Okay, sure, we might show up there, but what if it's like, hey, I have this really weird problem, I'm unprofitable, and I don't know how to fix it, you know?

**Matthew Panzarino:** And it's like, hey, maybe you should try a piece of software like Monograph, right?

**Matthew Panzarino:** Like, that's what they're most interested in looking for, and I'm like, we can, I think what we're going to do is go to some forums, architecture and

**Matthew Panzarino:** Engineer Forums and Subreddits and scrape those for questions and then build some clusters for them to at least populate Scrunch with.

**Matthew Panzarino:** But I was very straightforward with him and was like, hey, nobody knows exactly how this will play out.

**Matthew Panzarino:** And he's like, yeah, he goes, I know the investors in Scrunch and all that, so you don't have to believe in the point.

**Matthew Panzarino:** But it's something, and I think as long as we present it like we don't want to be left behind, so we're willing to do the experimentation for you.

**Matthew Panzarino:** Because we're running their Scrunch dashboards right there.

**Matthew Panzarino:** So I think it puts it as like the labors on us to figure out whether this is valuable to you over time.

**Darrell Etherington:** Maybe they'll figure it out.

**Darrell Etherington:** And that I think is like helpful, but like this is like putting up a dream catcher in your house.

**Darrell Etherington:** Like it's like, okay, what do you think this is going to do?

**Jason Gong:** No, I think it's like more valuable than that for sure.

**Jason Gong:** Like, I mean, what we're doing practically, right?

**Jason Gong:** Like we're sampling like presumably infinite number of prompts to like see the direction.

**Darrell Etherington:** Oh, no, I mean that.

**Darrell Etherington:** That is actually fine.

**Darrell Etherington:** I'm talking about this LLM's text thing.

**Darrell Etherington:** And I don't necessarily trust Raymond Martinez, vice president of SEO, about his opinion on this, because he has a biased opinion on this.

**Darrell Etherington:** But yeah, no, this crunch stuff, I find, like, I don't think they're doing anything technically interesting.

**Darrell Etherington:** I think it's interesting to think about how your customers are thinking about your product and what questions they might be asking, and it is useful in that regard, right?

**Jason Gong:** I mean, I think it's, like, in the same domain as, like, Nielsen surveys, where people ask, like, have you heard of YouTube before?

**Jason Gong:** And you say yes.

**Jason Gong:** And if you sample enough people, it gives you a, you know, a rough That's exactly how I described it.

**Darrell Etherington:** I literally described it as that on the call.

**Darrell Etherington:** It was like, it's like you're a Nielsen family, and you have random sampling, and, like, that's hopefully represented the population.

**Jason Gong:** But it's, you I mean, I think it'll get better than that, to be honest.

**Jason Gong:** Like, like, I think, like, people have figured it out, I believe.

**Jason Gong:** But the LLM's, like, TXT thing, okay, but I mean, but just, like, the, like, I think for the clients that I'm on, they would want it, you know, even if it's just an experiment.

**Jason Gong:** We start looking at, like, if it's even getting ping.

**Jason Gong:** So I think it's worth the investment to at least create a little workflow where it's available for everyone.

**Jason Gong:** And then whether you want to use it or not, you know, kind of up to you.

**Mara Leighton:** Also, I think just, like, for one use case, I think, like, in terms of, like, temperature, interest, pressure, I feel like Galileo would be one where, like, I would like to offer this to them.

**Mara Leighton:** I also offered, with all of the caveats that we've mentioned, which I think also just, like, helps solidify some of the, like, context we've been providing to them over the last few weeks.

**Mara Leighton:** But I think just in terms of being proactive and aggressive, like, I think it would help from a relationship standpoint to share.

**Mara Leighton:** But, like, with all of the caveats that we've mentioned today, I shared with them the Airbyte Reddit posting.

**Mara Leighton:** So thank you so much, Jacob.

**Mara Leighton:** They were actually pretty excited about that.

**Mara Leighton:** And we talked at length about how it's, you know, potentially, like, there's a shelf life loophole, you know, like.

**Mara Leighton:** Test it and see how it goes, but I think from that, like, I think they're getting a lot of pressure, so it's just kind of like partnering with them to come up with like test projects and then being very realistic about like, you might not glean anything from this, it might not work XYZ, but we're coming to you with ideas.

**Mara Leighton:** So that's a use case where like I could see this being beneficial.

**Dave Capone:** Yeah, we can sync offline and I'll try and generate one for you.

**Mara Leighton:** That'd be great.

**Mara Leighton:** Thank you.

**Mara Leighton:** I would appreciate it.

**Matthew Panzarino:** But like, we're not countering any of your points.

**Matthew Panzarino:** Really, really, oh, sorry, go ahead.

**Dave Capone:** So my, so my takeaway from this is I'm going to take, I'm going to be Sweden, I'm to be in the middle here.

**Dave Capone:** And I believe we need to do this, but I also believe we need to test this.

**Dave Capone:** And if it is , then I want to be able to go on LinkedIn and create a post and say, we tested, you know, all of our clients on llms.txt.

**Dave Capone:** And guess what?

**Dave Capone:** It's .

**Dave Capone:** And that's going to show us as leaders in this business.

**Dave Capone:** And show our expertise in this domain and drive us more clients.

**Dave Capone:** So that's what I'll do.

**Matthew Panzarino:** Mara, with the Reddit thing, as far as I understand what that was, was you suggesting, hey, populate your subreddit with a bunch of topics that could be indexed by LLMs, correct?

**Mara Leighton:** It was what Jacob showed us in yesterday's Director's Sync with Airbyte.

**Mara Leighton:** They've been publishing from their own account, so not publishing, and Jacob, correct me if any of this is incorrect, but not publishing in subreddits.

**Mara Leighton:** And they've been able to, it sounds like not repeated every single time, but they have seen them showing up in related LLM searches.

**Matthew Panzarino:** How are they posting, though?

**Matthew Panzarino:** Did they create their own subreddit?

**Matthew Panzarino:** Not in other people's subreddits.

**Matthew Panzarino:** I mean, did they create their own subreddit and talk about stuff in their subreddit?

**Darrell Etherington:** Or they are just posting replies?

**Darrell Etherington:** What's their...

**Darrell Etherington:** No, they're just posting...

**Darrell Etherington:** To their own account.

**Darrell Etherington:** Like, you know, you can do a you slash whatever.

**Matthew Panzarino:** it's their subreddit, but it's you instead of all.

**Matthew Panzarino:** Yeah, Yeah, that's what I mean.

**Matthew Panzarino:** Sorry, I apologize.

**Matthew Panzarino:** Yeah, they didn't create a subreddit, they just posted an user.

**Matthew Panzarino:** Yeah, okay, cool.

**Matthew Panzarino:** This is great.

**Matthew Panzarino:** I actually really like this approach, to be honest.

**Matthew Panzarino:** I was, I didn't remember that they were posting like that.

**Matthew Panzarino:** And I'm like, this makes a hell of a lot of sense, because I think most LLMs over-index on Reddit for questions.

**Mara Leighton:** So.

**Matthew Panzarino:** Yep.

**Mara Leighton:** Yeah, and we talked about, we had had like kind of an open question on like community forums.

**Mara Leighton:** And so it was helpful to kind of like pick back up and have it feel like it's, our key stakeholder is like a little bit more.

**Mara Leighton:** Anyway, they just hired a new person.

**Mara Leighton:** So it was a nice like relationship building also just to like partner with him.

**Mara Leighton:** So like it also makes him look good internally.

**Mara Leighton:** And they were very, very receptive to that.

**Matthew Panzarino:** So.

**Matthew Panzarino:** It's cool.

**Matthew Panzarino:** I think, I think it would benefit, I think a lot of our clients.

**Matthew Panzarino:** I'm going to be really careful not to mention it until they get content ramped, because like Monograph doesn't have anybody to do this.

**Matthew Panzarino:** would be like.

**Matthew Panzarino:** careful they ramped,

**Matthew Panzarino:** And I'll be like, sure, but I would have to build a pipeline for it and all of that, which we can do, fully confident we are capable of doing that, at the very least generating the content, and then we'd have to figure out a way to automate publishing, because I don't want to manually paste stuff into Reddit.

**Matthew Panzarino:** But I'm pretty sure we could do something like that for them, and just have them approve big batches of content, and then we can post one thing to Reddit a day automatically for them for the next month, and then just get some stuff seeded out there.

**Matthew Panzarino:** But I also need to get their pipelines to shape to ship 10 articles a week, so we can do that first.

**jakubrudnik:** I don't know, I haven't said anything yet, but I do think that at least bringing up that stuff that Dave's finding in anything like this, we should be throwing together and using some this time.

**jakubrudnik:** And then the worst thing we get is an experiment, and absolutely nothing happens, and we can go talk about that either on a Marcel-like workshop, or...

**jakubrudnik:** ...

**jakubrudnik:** ...

**jakubrudnik:** Probably more likely on LinkedIn, like that is really useful for us to be testing this and like debunking, because there's going to be a lot of like snake oil merchants on LinkedIn in this area.

**jakubrudnik:** So I think it's like really, we should be really skeptical, but then like, how do we actually like proving that out as a worthwhile time?

**jakubrudnik:** We have to carve that time.

**jakubrudnik:** think that is very difficult right now.

**jakubrudnik:** Personally, like I want to do some of those things, but where can we?

**jakubrudnik:** But if we can carve that time, it can be really impactful.

**jakubrudnik:** The AirBite stuff is like, luckily they brought that to us.

**jakubrudnik:** I don't know how we like action something like that without like giving away trade secrets that a client might have found.

**jakubrudnik:** So we have to like do that more like close to the vest, but if we can find those public things, that opens up a lot where we don't have to like worry about stepping on anyone's toes or ruining some of their creativity.

**jakubrudnik:** So anyway, I'm glad, thanks Dave for like surfacing it and we should just all be on the lookout for those.

**jakubrudnik:** Like what could we go try since we have 40 clients and websites like at our disposal to some extent.

**Andi Bailey:** So,

**Andi Bailey:** So Dave, in terms of actioning those for those who want to, or when they bring them up with clients, we have the workflow now.

**Andi Bailey:** And so this is just a manner of creating a ticket and assigning it to you, or what's the process?

**Dave Capone:** So the workflow, I created a ticket in Linear to build the workflow.

**Dave Capone:** There's additional requirements on our ends, like that I would want to build into it to, because essentially the way the prompt works now, just randomly grabbing URLs, and I want to actually add priority to the URLs that it grabs.

**Dave Capone:** If we do have the most important URLs and newest URLs, or et cetera, or quantify the actual URLs we want to use in this lms.txt, I can run that through the prompt.

**Dave Capone:** That's pretty easy, so I can create these, but yeah, we need about a week or two to actually build the workflow.

**Mara Leighton:** Follow-up question there, when would we be comfortable, like, softly, like, sharing this with clients as a possibility?

**Mara Leighton:** Just so that I don't get ahead of, like, get out over my skis on, like, mentioning it to Galileo, for instance.

**Dave Capone:** Yeah, let's talk offline.

**Dave Capone:** I think there's a few things we can do, but it's close.

**Dave Capone:** So I think comparing this to, like, our output to the free one that's out there, like, ours is really good compared to that.

**Dave Capone:** So I think there's, you know, let's take a look.

**Andi Bailey:** Yeah, like, talk to, see if you can get this ready for, by the end of the week.

**Andi Bailey:** Like, that would be great, so that we can start doing it next week.

**Andi Bailey:** What's the blocker on getting it done by then?

**Dave Capone:** I don't know, I'll talk to that about it.

**Dave Capone:** Yeah.

**Dave Capone:** Yep.

**Andi Bailey:** Okay.

**Andi Bailey:** We're at time, but just last thing, Webflow, those accounts, I know they didn't work the first time users tried to add them.

**Andi Bailey:** of those seats, we thought we could just add them to.

**Andi Bailey:** We thought we could just add them to our Webflow account as free users.

**Andi Bailey:** We were wrong.

**Andi Bailey:** We've upgraded all the seeds.

**Andi Bailey:** So your pod Webflow alias should now be added to your clients.

**Andi Bailey:** I'm going to start a list so that we can track which pod aliases are associated with which clients.

**Andi Bailey:** Because if clients move around, we probably don't want to move the emails around.

**Andi Bailey:** But that's like a follow-up for me.

**Andi Bailey:** But especially if your clients are getting kicked out of Webflow a lot, or your teams are getting kicked out of Webflow a lot, let's try and prioritize, again, also this for this week.

**Andi Bailey:** So that will probably give them a surprising amount of time back.

**Andi Bailey:** But also they could just send it to Suleiman.

**Andi Bailey:** So two options there should both save you time.

**Andi Bailey:** Okay.

**Andi Bailey:** Talk to you guys later.

**jakubrudnik:** Yeah.
