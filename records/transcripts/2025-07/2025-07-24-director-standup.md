# Director Standup

<metadata>
date: 2025-07-24
time: 18:59 UTC
duration: 48 minutes
organizer: Jason Gong
participants: Jason Gong, Dave Capone, Andi Bailey, Megan Dickey, Jakub Rudnik, Mara Leighton
fathom_recording_id: 76343292
fathom_url: https://fathom.video/calls/360915444
share_url: https://fathom.video/share/hxr9YkZq4ERx18C2yxZzizzAvfzSYnjW
source: fathom
enriched_on: 2026-03-03 17:45 UTC
</metadata>

---

## Summary

GrowthX leadership reviewed Jason Gong's comprehensive AI/LLM optimization resource — a prompt generator, Q&A guide, and methodology framework designed to help both internal teams and clients operationalize LLM optimization. The team debated the best way to measure LLM optimization impact, with consensus that referral traffic is misleading and that visibility metrics (what percentage of LLM responses include your content) plus attribution surveys and server logs provide a more accurate picture. Key next steps: develop client-facing one-pagers on GEO (on-site/off-site optimization), draft comprehensive GEO strategy overviews for QBRs, and work with Dave Capone to integrate Scrunch data into Looker dashboards (pending API capability for topics).

---

## Context

This is GrowthX's internal director standup focused on AI/LLM optimization and client strategy. The team — including leadership from content delivery (Jason Gong), analytics/dashboarding (Dave Capone), operations (Andi Bailey), and research (Megan Dickey) — gathered to align on how GrowthX is positioning its AI optimization expertise to clients and how to measure impact. Mara Leighton from GrowthX Labs joined externally to contribute perspective on prompt engineering. The meeting reflects GrowthX's ongoing strategic pivot toward AI as a core differentiator for its content clients, with particular focus on moving beyond vanity metrics (referral traffic) to more sophisticated attribution and measurement approaches.

---

## Relevance

**To GrowthX Delivery:**
- Artifact-based prompt generation is now a documented, repeatable methodology for content teams. Tool created by Jason Gong can generate prompts from client deliverables; tested across several client accounts with results matching production prompts.
- Client adoption friction is real — teams that tried AI workflows early and got poor results are now giving up and reverting to fully manual processes. Matthew Panzarino working to rebuild team confidence on artifact workflows at internal client.
- Core positioning challenge: clients gravitate toward referral traffic as the success metric, but that's misleading for AI/LLM optimization. Transparent communication about attribution (or lack thereof) is critical to managing expectations.

**To CheckThat:**
- Prompt quality and consistency directly correlates with LLM response quality. Systematic tracking and testing of prompts (using Claude vs ChatGPT) shows Claude produces more generalizable, less over-specified results in some cases.
- Server log analysis (potential feature for CheckThat): understanding which LLM crawler accessed content when can provide attribution data that clickthrough-based metrics cannot capture. Limitation: most clients don't have server log access or know how to extract this data.
- Topics/categories in Scrunch API currently not available via API call — potential integration blocker if GrowthX wants to surface Scrunch topic-level data in client dashboards.

**To GrowthX Business Development:**
- One-pagers on GEO (on-site/off-site optimization) and comprehensive GEO strategy overview for QBRs are now in development. These are key client-facing differentiation materials for explaining why GrowthX's LLM optimization approach is distinct.
- Measurement and attribution methodology is becoming a key sales conversation — clients are asking "how will I know it's working?" GrowthX's answer (visibility metrics + attribution surveys + server logs) is more sophisticated than competitors' referral-traffic-only models, but requires better documentation and support.

---

## Overview

- GrowthX is actively developing strategies for AI/LLM optimization, including tracking prompts and analyzing content performance
- There's a need to create client-facing resources (e.g., one-pagers) to explain GrowthX's AI/LLM approach and its value
- Integrating AI/LLM insights into content strategy is ongoing, with a focus on listicles, comparisons, and FAQs
- Measuring the impact of AI/LLM optimization remains challenging, requiring a multi-faceted approach beyond just referral traffic

---

## Key Topics

### AI/LLM Optimization Strategies

  - Developed a prompt generator to help create effective prompts based on client artifacts
  - Organized Q\&A into a more digestible format for team reference
  - Focusing on long-tail queries and content freshness to align with AI/LLM tendencies
  - Considering adoption of LLMs.TXT file for crawler education on products

### Client Communication and Resources

  - Need for proactive communication about GrowthX's AI/LLM efforts to clients
  - Planning to create one-pagers on topics like site audits and on-page recommendations
  - Upcoming webinar will include a section on practical AI/LLM optimization strategies
  - Suggestion to use QBRs as an opportunity to present comprehensive AI/LLM strategies

### Content Strategy Integration

  - Pushing for more comparison pieces, listicles, and adding FAQs across client content
  - Refreshing existing content with AI/LLM optimization in mind
  - Analyzing competitor presence in AI responses to identify content gaps

### Measurement and Analysis Challenges

  - Referral traffic alone is not sufficient to measure AI/LLM impact
  - Exploring ways to correlate prompt tracking with visit increases
  - Considering hiring a data scientist to develop more sophisticated analysis methods
  - Investigating the possibility of simulating AI/LLM retrieval to understand selection criteria

---

## Action Items

**Jason Gong (GrowthX)**
- Create doc clarifying SEO vs GEO differences, incl. examples from Scrunch call. Share w/ team.
- Develop one-pagers for on-site/off-site GEO recommendations. Inc. visual elements. For client sharing.
- Draft comprehensive GrowthX GEO efforts overview for QBRs. Inc. proactive approach, expertise highlights.

**Dave Capone (GrowthX)**
- Investigate methods to make Scrunch dashboards more actionable. Focus on translating intel to workflow impacts.

---

## Transcript
**Dave Capone:** Good.

**Dave Capone:** You in the office today?

**Jason Gong:** Yes.

**Jason Gong:** Been here quite a lot lately just because of all the, like, filming and stuff.

**Jason Gong:** Do you have new guests or are you filming, like?

**Jason Gong:** Not really into lineup the next day better, but since the first episode we've gotten the hypergrowth guy, so, like, that one's being edited.

**Jason Gong:** Otherwise, it's just been a bunch of, like, internal stuff.

**Jason Gong:** They just did one today on live coding just, like, because all the engineers were here.

**Dave Capone:** That's cool.

**Dave Capone:** How did it go?

**Jason Gong:** I was on a call, so I didn't actually hear it, but hopefully it won't.

**Megan:** Hey, guys.

**Jason Gong:** It went well.

**Jason Gong:** I'm laughing.

**Jason Gong:** Hey, Megan.

**Megan:** Oh, y'all doing?

**Jason Gong:** Good.

**Dave Capone:** Yeah.

**Dave Capone:** I would like to get an engineer's take on vibe coding, because it has to be fun, right?

**Megan:** Because, you know, they've spent so much time learning this discipline and how to code and all this stuff.

**Dave Capone:** And then, you know, to have someone just come up with a prompt that kind of does a lot of stuff that they do, like, it'd be interesting to hear their take on it.

**Jason Gong:** Yeah.

**Megan:** Yeah, I think I, like, I kind of hate the terminology.

**Megan:** Like, there's something about vibe coding that's just, like, oh, my God, like, what are we, what are we doing here?

**Megan:** But, but I, but I've, I've also done it, but I can't, I just feel weird saying, like, oh, yeah, it was, like, vibe coding, you know?

**Jason Gong:** Wow.

**Megan:** That's, like, what, like, Lovable is, though, and, like, Replit, like, that's essentially, like, what those are for.

**Jason Gong:** I mean, think Replit, a little bit more full, like, life cycle, where, like, I think.

**Jason Gong:** And lovable, as soon as you're done vibe coding, you kind of have to, like, leave.

**Jason Gong:** And then replet feels a little bit more serious, so, like, you can probably stay on it.

**Megan:** Yeah, beyond the vibe, yeah.

**Jason Gong:** Hi, guys.

**Megan:** Hey, Andy.

**Dave Capone:** Hey, I think we have everyone.

**Andi Bailey:** I just left Panzer in a room with Rachel and Jessica, Jessalyn, telling them about artifacts and having them retrust.

**Andi Bailey:** I think some of the problem that we're seeing is that if it didn't work the first time or the first five times, people give up.

**Andi Bailey:** And, like, they have gotten better.

**Andi Bailey:** And so, like, their article briefs are one line because they were like, we tried everything and it didn't work, so we just do it.

**Andi Bailey:** But one line and then edit everything at the end.

**Andi Bailey:** So Panzer is trying to get them to trust the workflows again.

**Andi Bailey:** And hopefully that will save them some time.

**Andi Bailey:** But it seems like some of their inputs, like, they just had really bad luck at the beginning and gave up.

**Andi Bailey:** Which, understandable when you just have to get stuff out.

**Andi Bailey:** But hopefully, Jakub, that will make their lives a little bit better.

**Andi Bailey:** And then we still have to find Jessalyn coverage for two weeks from now.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Thank you for identifying that.

**Jakub Rudnik:** I think we'd, like, unblocked a couple things, but not gone to that level.

**Jakub Rudnik:** And there's more to do.

**Jakub Rudnik:** So, yeah.

**Jakub Rudnik:** Appreciate it.

**Andi Bailey:** Of course.

**Andi Bailey:** Okay.

**Andi Bailey:** And now this is the Jason show of Geo.

**Jason Gong:** Oh, we were just talking about Geo.

**Jason Gong:** I thought we were going to do other.

**Andi Bailey:** I don't know.

**Andi Bailey:** You were like, let's do it.

**Jason Gong:** I feel like there's going to be a lot of questions.

**Jason Gong:** Yeah.

**Jason Gong:** Like, yeah.

**Jason Gong:** Though I didn't want to flag, because I wasn't sure if we're going to go account by account, but I feel like I'm kind of worried about Sydney a little bit.

**Jason Gong:** Like, she tends to, like, fill in for other people at the sake of her own, like, sanity and schedule and sleep.

**Jason Gong:** So, like, one of things she said was, like, I think for a metronome, she's kind of doing most of the content, because NEM, I think, is really bogged on, like, another client.

**Andi Bailey:** Hair bite, yeah.

**Jason Gong:** Okay.

**Jason Gong:** and she's kind of just, like, taking that instead of, like, surfacing it, you know, so just flagging that.

**Andi Bailey:** Yeah.

**Andi Bailey:** Sydney is, like, very selfless, it seems like.

**Andi Bailey:** She messaged me the other day, and she's like, I have food poisoning I'm about to throw up, but if you need me to stay on this call, I can.

**Jason Gong:** I was like, please leave this call.

**Jason Gong:** I'm kind of worried, because I guess I don't see all the strategy sprint stuff, but I just see more and more layered on.

**Jason Gong:** And then for web flows.

**Jason Gong:** Yeah.

**Jason Gong:** She's kind of like, I mean, she hasn't had time to do much of it, so I fill in.

**Jason Gong:** Yeah, so just like that.

**Jason Gong:** Cool, okay, so for Geo, I mean, maybe, like, if everyone's had a chance to look at it, maybe we could just make this more of a discussion.

**Jason Gong:** I mean, like, high level, what I tried to do was just clean up what I had before.

**Jason Gong:** I think it took a couple days of not looking at it to read it again and be like, this is kind of hard to consume.

**Jason Gong:** I think that the two biggest changes for me was, one, really, like, a lot of focus on this, like, how do you come up with the prompts section.

**Jason Gong:** And thanks, Mara, for having that call, because I took some, like, interesting things from that call as well.

**Jason Gong:** But maybe the most, like, actionable thing is, like, I made a prompt that kind of works off of your artifacts and can give you, like, at least something to start coming up with the prompts.

**Jason Gong:** And I tested it for some of the clients that I used to work on, and the prompts all looked, like, relatively close to the one.

**Jason Gong:** I ended up shipping for them, so hopefully that's useful, and then the other part was just trying to organize all the Q&A into something a little bit easier to digest, and my hope for this is like eventually we can kind of like iterate on these and then add, you know, stuff into a queue that needs an answer and then kind of collaborate, especially on the ones that I know we get asked about a ton.

**Jason Gong:** Like I talked to Kyle in the office today and he gets asked a bunch of these and he found it useful, so hopefully this is like the right direction.

**Jason Gong:** Let's see, and then I have kind of a to-do for things that I want to do that like anyone can fill if you think this resource is missing something.

**Jason Gong:** So I guess I'll just stop there, like what does everyone think, like is this useful, is there anything missing, do you just have general questions?

**Megan:** It was useful, yeah.

**Megan:** I started, yeah, I used the prompt for exec.

**Megan:** And so I actually ran it both in ChatGPT using O3, but then also in Claude.

**Megan:** And like, I actually, I think I liked the ones, the prompts from Claude a little bit better.

**Megan:** Like, almost felt like in ChatGPT, they were almost like too specific.

**Megan:** And they ended up missing just like, like best tool with like presentation sharing during roleplay, like almost like more like general, like it almost felt like Claude did a better job of like having it be a little bit more general versus like hyper specific, like, so like one example was like best AI roleplay platform integrating seamlessly with Gong and data and like maybe, like maybe that would be search, but like, it just kind of felt like, oh, that's maybe too, too specific.

**Megan:** So basically what I'm doing now is kind of going through all of them and just like, kind of doing like a mix of them.

**Megan:** But I do think I liked Claude's response better.

**Megan:** So that's more so just like something I saw this morning as I was looking through it.

**Megan:** But also question, what's the best way to integrate, like once this is all into story, scrunch, like, what's the best way to like actually integrate this into the Looker dashboard?

**Megan:** Because like, I know right now in like some of the client tabs, it has like the LLM tracking.

**Megan:** But like, I guess I'm wondering like, one, like, where is that currently pulling from?

**Megan:** And if it's not scrunch, how can we make it so it's pulling from scrunch?

**Jason Gong:** Yeah, think Dave would be the best person to answer that.

**Megan:** For sure.

**Jason Gong:** I think on the dashboard is, I mean, we did like.

**Jason Gong:** A V1, and since then we haven't had time to go back to it.

**Jason Gong:** Like the high level purpose of the dashboard is like I would like it to be the place that is like shared in these meetings, like with the right level of abstraction.

**Jason Gong:** But right now, I don't know if it's fully there.

**Jason Gong:** I'm trying to think of one that this one maybe.

**Jason Gong:** Yeah, like this one.

**Jason Gong:** It's kind of like.

**Jason Gong:** Yeah, I don't know.

**Jason Gong:** I mean, Dave, maybe you can talk about like how it's actually hooked up, but like right now it kind of just shows all the prompts and then, you know, your exposure over time or like how much you show up in over time.

**Dave Capone:** Yeah, so the first way an LLM is just if you click on your own queries for that one.

**Dave Capone:** I'm sure that's the one that has all the other stuff in it.

**Dave Capone:** So this one just gives you traffic over time by refer, and it just uses like a, you know, regex.

**Dave Capone:** Query to pull in, you know, like a match on like perplexity or chat, or et cetera.

**Dave Capone:** And then you'll get like sessions by landing page.

**Dave Capone:** So like how many sessions did you get from an LLM to that specific landing page or the, or here it's like the engine plus, or the, as keep saying engine, the LLM or the landing page plus the sessions there.

**Dave Capone:** So it's, it's pretty just small breakout of the traffic.

**Dave Capone:** Um, I am still looking into the API for scrunch.

**Dave Capone:** Um, I haven't been able to build anything out yet.

**Dave Capone:** have a couple of major deliverables, uh, the finish today, and then hopefully tomorrow I can get to it.

**Dave Capone:** Um, even that, like, I know we talked about, um, the visualization of what we wanted that to look like and the API might be able to do that.

**Dave Capone:** Um, there are some, I guess, limitations to the API currently.

**Dave Capone:** Um.

**Dave Capone:** So, I just got to get through it and figure out, you know, the easiest way to do it.

**Dave Capone:** Like this view here, where Jason's sharing is what we originally wanted to kind of bring into there.

**Dave Capone:** But from what I'm seeing, topics isn't something that I can pull in through the API.

**Dave Capone:** So, if that's the case, then I'll have a conversation with Scrunch and our Slack channel and see if they can add it, which will make things a little bit easier.

**Dave Capone:** But for now, like, this is kind of the view that we want to replicate using the API.

**Jason Gong:** Yeah, I mean, I think I personally like this view.

**Jason Gong:** Just like, I don't know if you guys have read some of these, like, FAQs.

**Jason Gong:** I think it's good to spend, like, a few minutes here.

**Jason Gong:** Like, I'm sure all the clients ask, you know, like, just how do you measure and what is the impact?

**Jason Gong:** And I think I've seen a lot of people kind of gravitate towards this referral traffic.

**Jason Gong:** And I think it's, like, probably the wrong metric to look at.

**Jason Gong:** Like,

**Jason Gong:** Directionally, can be one of the metrics, but basically, like, referral traffic comes from when ChatGPT, like, sites you, and you click the link.

**Jason Gong:** So, like, an example, let's see, could do it here.

**Jason Gong:** Yeah, like, if you look at, let's see, like, this one here, right?

**Jason Gong:** Like, the prompts people care about are these product mentions.

**Jason Gong:** And I want to say, in most cases, like, there's no actual way to go from the AI app to a website and have that be attributed.

**Jason Gong:** So, like, if you think about, like, this journey here, right?

**Jason Gong:** Like, I'm in ChatGPT, I ask, like, what's the best CMS?

**Jason Gong:** Shows me all this.

**Jason Gong:** Like, none of these links would allow the app to attribute that, like, I came from ChatGPT, right?

**Jason Gong:** So, for the most part, I would assume, you know, most people, I would, like, click one of these or just go type in Sanity in Google and visit the link.

**Jason Gong:** So, I think, like, if you only do referral traffic, it kind of, it might just, like, throw the client off and they might just attack.

**Jason Gong:** And then our ability to move that is not really tied to the things we're actually trying to do.

**Jason Gong:** Does that make sense?

**Megan:** Yeah, that makes sense.

**Jason Gong:** Yeah, for sure.

**Jason Gong:** So that's why in terms of like, I think that this does need like another pass.

**Jason Gong:** I don't know if you have a spec for like what you're thinking about doing.

**Jason Gong:** If not, maybe I can make one because I think whatever we do here is going to like set their expectation.

**Jason Gong:** Right.

**Jason Gong:** For like, what we're kind of working on and how they're going to measure us.

**Jason Gong:** And I think like this scrunch is probably a lot better than the referral traffic.

**Megan:** Yeah, because let me.

**Megan:** Because something one of my Emmys has been doing, like he's actually, if you just want to, I kind of share my screen or.

**Megan:** Okay.

**Megan:** Yeah, because I'm also, yeah, just trying to make sense out of.

**Jason Gong:** If you look at the URLs here, I mean, I see, like, one of them is a listicle, which is good.

**Jason Gong:** But, yeah, I don't know.

**Jason Gong:** I mean, it's probably worth, like, some research, but I would guess, like, most referral traffic a lot of times is coming from, like, just, like, direct, like, brand type stuff.

**Jason Gong:** Like, somebody researching a product directly or, like, you know, maybe, like, an informational post where, again, it's, like, not directly related to a lot of the prompts we're even tracking.

**Jason Gong:** Yeah.

**Jason Gong:** So, I mean, I think this should be part of the data we share, but I still think the main thing to anchor them on is, like, the prompt categories and your attention ratio over time.

**Dave Capone:** Yeah, I agree.

**Dave Capone:** Like, I think it's two things that we want to actually report.

**Dave Capone:** One is, like, visibility internally in the LLM, right?

**Dave Capone:** So, like, what percentage of this topic is the LLM?

**Dave Capone:** I'm choosing to show or, you know, elevate my site or my client's site.

**Dave Capone:** And then two, it's kind of the, what is the traffic that we're getting from the LLM that, you know, if we've improved our visibility and increased our visibility, then we should see a correlation to like, okay, that should mean improved visits or some signal that we're seeing from there.

**Dave Capone:** So I think it's kind of like one, we should, we should nail one of these first and be like, okay, this is the view that we want to give to our clients.

**Dave Capone:** And then we can start working on the second view, which would be like, how does this, how do we take this and then translate it to visits so that it makes sense to them?

**Jason Gong:** Yeah, translating to visits, like hard.

**Jason Gong:** I don't know if you've seen anything interesting there.

**Jason Gong:** Like, think referrals is obviously the one, but like, if they're just seeing you in ChatGPT and then Googling you, you know, like, it's a little bit more challenging.

**Jason Gong:** Like, I've seen people do like attribution surveys, you know, like, how did you hear about us?

**Jason Gong:** If they do that.

**Jason Gong:** Like, you know, definitely encourage them to add, like, ChatGPT.

**Jason Gong:** So I think immediately they'll see that where it's like, oh, yeah, this guy says it came from Google, but he's saying ChatGPT.

**Jason Gong:** And that'll probably click for them immediately.

**Jason Gong:** And then once we have that, we can show other clients and it'll be easy to make that point that referral traffic isn't the end all.

**Dave Capone:** Yeah, the hardest thing right now is that attribution part.

**Dave Capone:** But what I've seen a lot of folks do now is look in the server logs so they can attribute it from that session.

**Dave Capone:** And then they can get, like, all the details from that.

**Dave Capone:** That could be something we could ask our clients for if they're, you know, really interested in it.

**Jason Gong:** How about, just like unpack that, because I think the server log thing is interesting.

**Jason Gong:** I have been looking into how we can actually do that.

**Jason Gong:** Like, I think a lot of it just requires a little bit more access than we have for customers.

**Jason Gong:** Like, I don't even know if a lot of the customers know even how to, like, get their server logs and they would have to talk to engineering and stuff.

**Jason Gong:** But, like, how would that work?

**Jason Gong:** Like, why would a server log show at?

**Jason Gong:** Contribution, like the server log would show the agent crawler, but like how would you tie that back to like a person that visited your website?

**Dave Capone:** That's a good, I'd have to dig in look.

**Jason Gong:** Yeah, because I don't know, like I've asked the scrunch guys too, I don't think there's like a super strong way.

**Jason Gong:** Yeah, okay.

**Jason Gong:** Any other, I mean, I think that one's important.

**Jason Gong:** I imagine like all the clients are kind of looking for a way to like see what we're doing and then see the progress of it.

**Jason Gong:** And right now there's not a great solution.

**Jason Gong:** Like honestly, I would recommend, and I was doing this for some of my calls, like just kind of like screenshot this and like throw it into, you know, your Notion doc.

**Jason Gong:** And then during the call, think you can like selectively like walk through this platform.

**Jason Gong:** I think the one problem of giving the clients access is one, I guess the scrunch guys were hesitant to do that.

**Jason Gong:** guess our contract, it wasn't really like something that would allow us to kind of like pass this through to our clients.

**Jason Gong:** And get like a ton of accounts.

**Jason Gong:** And then the other one is, I think for us, it's just, there's just so many places in here that would, I don't know, like confuse the client, you know?

**Jason Gong:** So I don't want to give them access to this.

**Jakub Rudnik:** I think that's a risk to, to go back to like the referral versus citation.

**Jakub Rudnik:** Like obviously they are different.

**Jakub Rudnik:** I'll say that Webstacks is like showing them the referral, which is, it's helpful because it's really good, but they've seen that come through like their other, the other ways that they attribute themselves and it's, the traffic has been successful so far.

**Jakub Rudnik:** So like they, it's showing them that and them being aware of like, even if they can't connect exactly what we do to this, like they know that there has to be some amount of correlation and that's a very good thing.

**Jakub Rudnik:** And we can still see like, you know, the homepage, like when someone's getting a product mentioned, it's typically not linked, but they are getting a hundred like homepage visits a month directly from LLM.

**Jakub Rudnik:** So somewhere that is, like, and that would speak to me on, like, those type of queries.

**Jakub Rudnik:** So I don't think it's none.

**Jakub Rudnik:** I think it's smaller than some other things.

**Jakub Rudnik:** And then they've added, you can see on, like, maybe this has been brought up before, but on their pages, like, a quick chat that says AI or ChatGPT bring you to this page.

**Jakub Rudnik:** And so they're trying to do that as, like, you know, it's never going to give them full data, but they can at least learn something there.

**Jakub Rudnik:** Certainly, like, you know, like, Jason, you said, if a team does it in their, like, onboarding survey or whatever, when someone signs up for a trial, like, where did you hear from us?

**Jakub Rudnik:** Like, adding that is probably the best way to do it at scale.

**Jakub Rudnik:** But I do think there's benefits to the referral.

**Jakub Rudnik:** I think it tells, Megan, to your point, the more macro view is, like, this going, and you know that not all the traffic coming from LLMs is referral.

**Jakub Rudnik:** Like, probably a good chunk of it isn't.

**Jakub Rudnik:** People are going and Googling after using LLMs to, like, simplify the flow.

**Jakub Rudnik:** But to see this as, like, you know there's other clicks.

**Jakub Rudnik:** You know there's other benefits.

**Jakub Rudnik:** But seeing that...

**Jakub Rudnik:** Fathom, especially, Megan, in yours, it's like, there are a lot of referral traffic, that's good.

**Jakub Rudnik:** So we can at show the signals, and then you're like, patching together.

**Jakub Rudnik:** Andy and I were on the Homebase call earlier, and it's like, here's a puzzle, and like, 75% of it's going to be dark, but we can try to fill in as much as we can.

**Jakub Rudnik:** And like, the specific queries, I think, are really useful.

**Jakub Rudnik:** The macro view of the referrals is useful.

**Jakub Rudnik:** Some are selling a call just like, live, go into a couple of LMs and do some queries and show that they were cited.

**Jakub Rudnik:** It's like, okay, there's at least anecdotal evidence that they're being cited in LMs.

**Jakub Rudnik:** Like, all these things help to tell the story.

**Jakub Rudnik:** The story is just not going to be complete, but I would use like, all of these things.

**Jason Gong:** that's the right way to frame it.

**Jason Gong:** It's just like, the referral traffic is like, part of the picture, but you're actually getting a lot more from, you know, ChatGPT.

**Jason Gong:** Like, just like the example here.

**Jason Gong:** Sorry, any track.

**Jason Gong:** Like, not that one.

**Jason Gong:** Yeah.

**Jason Gong:** Where's my attribution one?

**Jason Gong:** Yeah, just this one.

**Jason Gong:** It's

**Jason Gong:** Like, you know, sometimes you'll get this, where, like, none of the links are attributed, but sometimes you'll get this, where, like, every link is attributed.

**Jason Gong:** And it's, like, you know, as a percentage, I don't know what it is, but I think what it's showing is just, like, okay, the referral traffic you're seeing is, like, a fraction.

**Jason Gong:** So, like, you know, like, think about the impact of, like, moving that.

**Jason Gong:** So maybe, I don't know, if you guys, like, can answer that's helpful, like, we should definitely share that along the team, and then I can make that, like, an FAQ here.

**Jason Gong:** So everyone is armed with some things.

**Jason Gong:** think, like, showing these screenshots could even be helpful, you know.

**Jason Gong:** Any other kind of questions that you guys always get, or things that would be helpful, like, as far as, like, resources on our side?

**Jakub Rudnik:** I've found in the doc you shared, the geo audit.

**Jakub Rudnik:** That was, like, one of my questions coming

**Jakub Rudnik:** And thanks for documenting that.

**Jakub Rudnik:** And it's also, right now, what I'm trying to get a better grasp so can speak to is a lot of the recommendations.

**Jakub Rudnik:** I'm like, that looks like a technical SEO audit.

**Jakub Rudnik:** There's so much overlap and best practices for Geo and SEO are the same.

**Jakub Rudnik:** And so now maybe it's just like a positioning.

**Jakub Rudnik:** Like, we're doing this for LLMs, but we're also doing it for Google, too.

**Jakub Rudnik:** Just wherever there's differentiation between the two, calling that out, I think that's a gap for me.

**Jakub Rudnik:** I feel like I'm just saying, like, we're doing what I've always done for SEO, and it's roughly working for LLMs.

**Jakub Rudnik:** And that's, like, doesn't feel like a great answer.

**Jakub Rudnik:** So it's just like a call of, like, when things are different.

**Jason Gong:** Yeah.

**Jason Gong:** Maybe, like, mapping that out more clearly would help.

**Jason Gong:** Because I thought the, if you guys haven't watched it, the call Mara had, like, the guy from Scrunch showed some, like, really great examples that, like, hit it home of, like, it's kind of like SEO, but it's a little bit different.

**Jason Gong:** So, like, you know, one, should keep investing in SEO, and I think there's, like, good case you should invest more.

**Jason Gong:** think there's more, and then...

**Jason Gong:** You know, also do a few things differently.

**Jason Gong:** So I think, like, we can, like, compile something that makes that super clear.

**Jason Gong:** So I think that's another question, right?

**Jason Gong:** It's just, like, people probably questioning, like, whether SEO is even worth it to do, and it's dead.

**Jason Gong:** Just, like, you know, like, one concrete example.

**Jason Gong:** I think I tried to share some here.

**Jason Gong:** But, like, in Scrunch, and I made a comment for them to, like, surface this better, of, like, like, for every prompt, they actually store, kind of, the search query that it runs in the background.

**Jason Gong:** And if you look at all the search queries, they're almost all a little bit more long-tail and a little bit more, kind of, biased for recency.

**Jason Gong:** So I think what that means is, like, you know, like, there's, like, a ton more long-tail queries.

**Jason Gong:** Like, that means you need more long-tail content, more content.

**Jason Gong:** And then if things need to be recent, you need to be refreshing more.

**Jason Gong:** And I think both of those things is, like, uniquely things that GrowthX can do better, right?

**Jason Gong:** Because we're doing, like, quality content at scale.

**Jason Gong:** So maybe I'll make a doc that tries to make that more clear.

**Jason Gong:** And then as far as the audit stuff goes, yeah, I mean, think, again, Dave has this larger doc on this.

**Jason Gong:** think a lot of it, like, on the website structure side overlaps, minus some, like, RobotTXT, LMTXT stuff.

**Jason Gong:** And then I think, like, how your content is structured is, like, where there's the most kind of divergence a little bit.

**Jason Gong:** And I think, yeah, I mean, I think the answer is having a doc so you can talk about it.

**Jason Gong:** And then the other answer is, like, none of our workflows do this right now.

**Jason Gong:** And, like, that needs to be baked in at some level.

**Jason Gong:** So you don't have to, like, manually do all this.

**Dave Capone:** You mentioned LLMs.TXT.

**Dave Capone:** We should probably start adopting that.

**Dave Capone:** I've started to see that unofficially.

**Dave Capone:** Like, a lot of the...

**Dave Capone:** Um, Perplexity is using it, ChatGPT is using it unofficially, so folks are posting that they are consuming the file regularly now, and they're checking it quite a bit, so I think that's something we should look into or add to our plan.

**Jason Gong:** Yeah, I mean, I've seen a few formatted, and like, the way they're formatted is also interesting, like, it's like, you're trying to educate, like, the crawler on your product, and it's like, we can do a pretty good job of, like, kind of generating that, you know, and then keeping it constantly updated.

**Jason Gong:** Um, yeah, so I guess next steps there, I mean, to have a clear doc on, like, what we're trying to do, so that at least you can communicate it, and then, yeah, mean, we just need, there's so many things to kind of try to, like, start building on our side.

**Dave Capone:** So, I think we need, like, a roadmap of, like, what we want to build.

**Dave Capone:** And then, you know, plan that out.

**Dave Capone:** I think you have something.

**Jason Gong:** Yeah, yeah, no, mean, that was that meeting earlier, too, so I think it's good that we're doing that, because I think that needs to go in here, basically.

**Jason Gong:** Like, what we're doing for editorial, what we're doing for geo.

**Jason Gong:** know, that's what's up.

**Jason Gong:** I think one of things that Colin asked me for is, like, he finds it very helpful to have, like, resources he can just, like, send to the client, so, like, instead of him having to, like, do all this work to communicate something, just having a reference.

**Jason Gong:** Like, have you guys found a desire to be like, man, I wish we just had, like, a little one-pager on this, and it would make my life much easier.

**Mara Leighton:** That's, um, that was actually my note that I just wrote down from listening.

**Mara Leighton:** Um, it could be helpful to have one-pagers, even on, like, on-site recommendations or off-site recommendations.

**Mara Leighton:** recommendations, just something that we can pass along.

**Mara Leighton:** So like, after the conversation, they can refer back, because I think I find, I know if other people are finding this, that like the live discussions, you reach like a consensus.

**Mara Leighton:** But I think sometimes for people to, like, if this is something that's not really there, bread and butter for it to like fully sink in, I've always found it useful to have like some type of resource to share with them.

**Mara Leighton:** So even if you cover it live, they can refer back to it in their own time, and like continually refer back to it.

**Mara Leighton:** So I personally would find like one pagers, pretty helpful, not that we won't be having the conversations, but just as like a kind of a learning tool.

**Jason Gong:** Yeah, that would be good.

**Jason Gong:** And then is there any one pager that like, is particularly useful?

**Jason Gong:** You said site audit?

**Mara Leighton:** I just, I, site audit is what came to mind just as something that they could pass off to their developer team, you know, if it was like, and also relatively visual.

**Mara Leighton:** And I feel like we have a good amount to go.

**Mara Leighton:** a mask.

**Mara Leighton:** In you Yeah.

**Mara Leighton:** of like

**Mara Leighton:** formatting.

**Mara Leighton:** So that's the first thing that came to mind.

**Mara Leighton:** But yeah, like on-page recommendations would be useful.

**Jason Gong:** think, I mean, I think a good forcing function here for everyone is like, I mean, we need to be proactive with this.

**Jason Gong:** I think we can't have the client come to us and ask us about Geo.

**Jason Gong:** We need to like, essentially like document and almost like run like a little, you know, session where we talk, talk about what we're doing for them, kind of our approach and like, almost like do a bit of selling.

**Jason Gong:** So like, there's no question in their mind, one, that we're doing it.

**Jason Gong:** also like, we're the right kind of partner for them to like, be, you know, bleeding edge on doing this.

**Jason Gong:** Like, I'm trying to think what the best way to do that is, because like for abnormal, I think it's the one client where I probably spent the most effort.

**Jason Gong:** Because like, he, you know, like asked a few times, or he just showed he was interested.

**Jason Gong:** don't know.

**Jason Gong:** And this is like the one pager that I think went around their team a lot.

**Jason Gong:** And I wouldn't share something exactly like this now because I know so much more than I did when I put this together.

**Jason Gong:** But basically like, yeah, I mean, I'm just repeating myself, but like they need to like feel we're being proactive on this and they can't be like, once they ask us, then we tell them.

**Andi Bailey:** So far I've been hearing as I've been dropping in on calls, like we are bringing it up.

**Andi Bailey:** And if anything feels like even tangential to it, like sharing more knowledge than what they're asking.

**Andi Bailey:** So and I know we've got we're starting to schedule like QBRs right now.

**Andi Bailey:** So I think like that's a good opportunity to bring it up and have that strategic conversation.

**Andi Bailey:** That's what we did with Homebase today.

**Andi Bailey:** I think probably like there's a Galileo call in a couple of weeks and I'm a bit.

**Andi Bailey:** Talking about numbers.

**Andi Bailey:** So I think that the, like, looking for an opportunity where the client asks a question and then we can bring up our expertise here and then use it as a jumping off point.

**Andi Bailey:** I mean, certainly also like an agenda item on weekly calls, but we should have a suggestion if we're going to bring up like our knowledge about Geo.

**Andi Bailey:** So I don't want it to come up like apropos of nothing.

**Jason Gong:** Yeah, do you think, I guess, the QBR is like a good place to do like a, like it doesn't have to be big, but it's just, like, I don't know if any of the clients have ever had like a pretty comprehensive view of like, here's what GrowthX is doing.

**Jason Gong:** You know, we're like.

**Andi Bailey:** Yeah, I mean, we should be doing that.

**Andi Bailey:** Yeah, and I mean, like, one of the things that came up a lot in the feedback calls was thoughts about how, like, us showing what we're seeing, like.

**Andi Bailey:** Trends in the market, trends in the industry.

**Andi Bailey:** So this is a good example of something that we can start to bring up more often of just like maybe it starts to be an agenda item of like little things we're seeing or like common questions we're getting right now or like focus areas.

**Andi Bailey:** But, you know, all of this varies by clients and how they want to talk to us and how like what how we structure our calls.

**Andi Bailey:** So there's no I don't think there's any specific answer, but I do think like we've been talking about this every Wednesday for the last three weeks.

**Andi Bailey:** So I think we're we're like starting to get a little bit more versed in it.

**Andi Bailey:** And certainly I haven't seen anybody like feel uncomfortable talking about it in calls yet.

**Andi Bailey:** So hopefully that's good.

**Mara Leighton:** A couple of ways that we could maybe naturally open that conversation is a sharing the webinar with anyone.

**Mara Leighton:** Maybe we haven't shared it with already.

**Mara Leighton:** And that's kind of a natural conversation starter.

**Mara Leighton:** And.

**Mara Leighton:** And then also, what was the other thing I was thinking?

**Mara Leighton:** Oh, refreshes, I think, are a really natural place to mention what we're doing here, because pretty much everyone knows what a refresh is and is interested in doing it.

**Mara Leighton:** might already be part of their strategy.

**Mara Leighton:** And that's just a more natural way for us to start talking about geo.

**Mara Leighton:** And that's kind of our Trojan horse.

**Jason Gong:** Yeah, I mean, the webinar probably would be good.

**Jason Gong:** So, webinar next week, like, I know Marcel's, like, we haven't really fully planned it out, but, like, Marcel's section is kind of a little bit on AI, but more on the kind of, I mean, his take has always been kind of, like, the fundamentals don't change, and he's going to kind of focus on that.

**Jason Gong:** And then I'm going to do a section within that that's, like, just specifically on this stuff, like, more practical, like, what are you actually trying to do here?

**Jason Gong:** So, maybe as I think about doing that, I'll make it so that whatever my 20-minute, 30-minute...

**Jason Gong:** It's really easy to just cut, and then if the client's not directly in the workshop, you can send that to them, and it'll be coherent, and it'll try to make all the points that I think we should make of, like, I mean, again, I think it's important people need to feel like, I mean, whatever we're doing for them is as much geo as SEO, it's all kind of the same thing, like, we're trying to create content that brings them, you know, an audience that drives their business, essentially.

**Jason Gong:** Cool.

**Jason Gong:** Let's see.

**Jason Gong:** Anything, anything else?

**Jason Gong:** mean, like, has anyone actually started to use the insights from here to, like, create content?

**Mara Leighton:** I would say, like, just from...

**Mara Leighton:** I from...

**Mara Leighton:** Our personal experience, like the refresh has been helpful for getting like strappy on board with like prioritizing refreshes.

**Mara Leighton:** But that's the only like immediate thing beyond the prompts for Galileo.

**Jason Gong:** Okay, because I think that, I mean, the first step is just getting everyone tracking.

**Jason Gong:** I think, I don't know what the state of that is, but hopefully this makes it easier to get everybody, like at least starting to monitor.

**Jason Gong:** And then the second part is, you know, we need to run some for audit.

**Jason Gong:** And then like this actually needs to start shaping the content we produce.

**Jason Gong:** Because it's like, I mean, it's kind of in line with what we produce already, but not as much, or not totally.

**Jason Gong:** I think what it looks like is a lot more kind of like listicles, comparisons, and kind of, you know, things that surface and essentially all these like product evaluation prompts.

**Jason Gong:** And I know our workflow is not very good at it at the moment.

**Mara Leighton:** So, yeah, related to that, we are doing, for everyone, makes sense, starting to push more of like comparison pieces, and then also a recommendation of adding in FAQs kind of across the board.

**Mara Leighton:** And then, yeah, we'll focus more on listicles and just like general formatting.

**Mara Leighton:** So, I guess we are implementing those currently.

**Megan:** Yeah, and it's definitely something that, because we're in the process of sort of like doing a bit of a strategy refresh for School AI and Superhuman.

**Megan:** So, I'm definitely starting to integrate this into the strategy, but we haven't yet actually started producing that content based on that strategy.

**Megan:** But, but it's definitely, yeah.

**Megan:** Coming in from the pipeline, for sure.

**Jason Gong:** Okay, cool.

**Dave Capone:** When I get a minute, I'd like to look at how to make these scrunch dashboards actionable, right?

**Dave Capone:** Because I think that's the question you were asking, was like, how do we take this intelligence that we're getting from, you know, scrunch, and then how do we act on this to impact our workflows or impact our, you know, articles that we're writing?

**Dave Capone:** There has to be, like, I'm just kind of looking at it now, kind of digging into it, but I'll see if I can figure something out.

**Megan:** Yeah, because I guess I'm wondering, like, there is, like, just in, like, the insights tab, and there's, like, competitive presence.

**Megan:** So, like, I'm looking at, like, okay, like, ChatGBT responses mentioning competitors, but not your brand.

**Megan:** Like, essentially see that as, like, keyword gap analysis.

**Megan:** So, like, theoretically, like...

**Megan:** We should then maybe target these prompts where competitors are showing up, but not the brand.

**Megan:** This is sort of how I'm looking at it right now.

**Jason Gong:** Yeah, I think that's the right way to look at it.

**Jason Gong:** There's a show, don't know if everyone's familiar with Scrunch yet, but that would be here.

**Jason Gong:** So, yeah, I mean, it's not very easy to do this at the moment.

**Jason Gong:** Like, what I would like is something, hopefully automated, that you get articles that are being cited for the prompts you care about, and also searches that are happening for prompts you care about.

**Jason Gong:** And then that kind of just brings it right back to SEO as far as, like, the topics to cover.

**Jason Gong:** Because it'll show you kind of, like, okay, here's all the content, and do I have a version of this content?

**Jason Gong:** And I'm like...

**Jason Gong:** Kind of present in this search to begin with to even get a chance of being cited.

**Jason Gong:** And then the on-page stuff is the stuff that's like a little bit more unclear to me.

**Jason Gong:** Like, I don't know if that's just a workflow improvement or that's like a style guide that we try to follow.

**Jason Gong:** Because it is like slightly, you know, tweaks to like how we write now.

**Jason Gong:** It's like, I don't know for all clients if we have a little kind of like key takeaways at the top, you know.

**Jason Gong:** Like, don't know if we're doing a good job of like having good chunks like within the doc that are easy to cite.

**Jason Gong:** That one probably needs a little bit more work.

**Jason Gong:** And then there's the, like, you might get this question of like, I mean, like to shape what LLMs say, it's like not totally enough to just for you to publish content, right?

**Jason Gong:** Like, it has to come from essentially what the internet says about you and the other places that get cited and like trained in.

**Jason Gong:** That one, I don't know if we have a really good.

**Jason Gong:** Answer for, like, we can give them advice, right?

**Jason Gong:** Like, you should probably be, I mean, especially if you're a developer tool, like, be active and, like, Reddit, Quora, and Hacker News, and all these places that get cited, you should probably try to get mentioned in, like, a lot of these syndicated, like, publications.

**Jason Gong:** Yeah, but we don't, we don't have, like, a work stream there, and we don't, honestly, our recommendation isn't super clear either.

**Jason Gong:** So if you get questions there, I'm think what the answer is.

**Jason Gong:** mean, it is something we need to, like, work on, basically.

**Jason Gong:** So I'm just flagging.

**Jason Gong:** Okay, anything else?

**Jason Gong:** I mean, I guess I'll communicate what the roadmap here is, but I think the current goal

**Jason Gong:** For everyone should be like get everybody tracking at least with the with with a good set of prompts and then try to find an opportunity to kind of like at least give a more cohesive like rundown of what we were even doing to make sure the clients like thinking about it the right way.

**Jason Gong:** And at least it's giving us credit that we're like doing this for them.

**Jason Gong:** And maybe you've done that already.

**Jason Gong:** So but like I think it's important to do that like at least once.

**Megan:** Cool.

**Megan:** Sounds good.

**Dave Capone:** My brain's already like going crazy on this Jason.

**Dave Capone:** So like I look, I'm on that.

**Jason Gong:** Can I share real quick?

**Jason Gong:** Sorry.

**Dave Capone:** Yeah.

**Dave Capone:** Y'all don't have to hang on if you don't want to.

**Dave Capone:** Like I'm just kind of.

**Dave Capone:** All right.

**Dave Capone:** So this is the example used before, right?

**Dave Capone:** So basically there was a search performed.

**Dave Capone:** So it did not have this trained knowledge, right?

**Dave Capone:** So did a search.

**Dave Capone:** It pulled these 10, out of these 10, it considered these four, right?

**Dave Capone:** So it knows that these four have the best answer for that.

**Dave Capone:** So I think there needs to be something where we, if we do have an existing piece of content for this particular topic, like CMS for React, for example, then we need to do a version, like what are the gaps that we have that these fill the need for, fill the demand for, for that particular to win on this one, and then that should help us identify, like, what is weak.

**Dave Capone:** So maybe there's a way we can, I don't know, do a version match or do some sort of, like, load these four into an LLM and then have it tell us the difference between our content and theirs.

**Jason Gong:** I think that's, like, a huge question.

**Jason Gong:** So I have this, I'll share it with you, Dave, but I have this list of questions that are just, like, open questions I don't think anyone's answered.

**Jason Gong:** And I think this is one of, like, okay, hey, it's doing a search and there's, like.

**Jason Gong:** 20 results, but it's being kind of opinionated on the picks.

**Jason Gong:** And then at the same time, like, even if it's being cited, it's being opinionated about what it's citing.

**Jason Gong:** Like, I've seen so many cases where it's, like, top sales tools and then HubSpot gets cited, but, like, to recommend another product.

**Jason Gong:** And it's like, what does that mean, right?

**Jason Gong:** Like, how do I shape my article so that it recommends HubSpot?

**Jason Gong:** Is ChatGPT just saying, like, we're not going to let the domain itself shill its own product?

**Jason Gong:** Like, if that's the case, like, that's, like, very important to know across, like, a few thousand prompts, right?

**Jason Gong:** I think, I don't know what the right way to answer that is.

**Jason Gong:** I'm still trying to get one of these tools to just be like, hey, we'll do that analysis for you.

**Jason Gong:** But honestly, at this point, I think I might just go and hire a data scientist, like, on contract and we can work with them.

**Jason Gong:** Because I don't think any of us have time to, like, run the Python scripts to, like, do this, you know?

**Dave Capone:** So, yeah, it seems like we need, when it does, like, a rag, like, a fan-out query and it, you know, looks for...

**Dave Capone:** The knowledge that it needs to answer the question or whatever, we need to be able to simulate that in a way where, yeah, we need to be able to simulate our own ragout fanquery so that we can understand the criteria that it's taking to retrieve this information, and then we can tailor our pages to best be suited to be retrieved for that.

**Jason Gong:** So Alan seems really tough to, like, reverse engineer, but I think at the very least we can try to, like, find patterns.

**Jason Gong:** I know Scrunch is working on it, but, like, I don't know what that even means.

**Dave Capone:** Ideally, like, I don't know how to do it, but you can run some of these offline.

**Dave Capone:** So there's ways to run some of these engines, like, you know, LLMs offline to where you can create your own silo version of the LLM.

**Dave Capone:** That could give us insight on, like, you know, if we feed it a bunch of things and we know everything about these pieces of content that we're feeding it.

**Dave Capone:** we feed it.

**Dave Capone:** It can kind of give us insight into how to manipulate it a little bit.

**Jason Gong:** Yeah, that would be interesting.

**Jason Gong:** Maybe the open source ones.

**Jason Gong:** And another question that I really want to answer, of, like, essentially what we're trying to do is just, like, approximating what people prompt, right?

**Jason Gong:** Because we have no idea what they actually prompt.

**Jason Gong:** And it's like, you have this, like, intent bucket, and in that bucket you have maybe, like, hundreds of thousands of possible prompts that are reasonable, right?

**Jason Gong:** Like, it's not totally infinite.

**Jason Gong:** And then it's like, okay, out of that 100,000, like, how many variants do you have to track before you're kind of, like, generally getting a pretty complete understanding of what's being recommended, regardless of, like, what the other prompts are, right?

**Dave Capone:** Is it 10 or is it, like, 1,000?

**Jason Gong:** Or is it, like, all 100,000 are just, like, their own special snowflake?

**Jason Gong:** And I think if we had a view there, that would help a lot.

**Jason Gong:** Because I think that's the elephant in the room.

**Jason Gong:** It's like, yeah, we're tracking prompts, but, like, is anyone typing these?

**Jason Gong:** Like, everyone's got their own context.

**Jason Gong:** And, like, is their answer different than your answer?

**Jason Gong:** I think we have no good answer to that.

**Dave Capone:** Yeah, I would almost want to correlate the number of prompts to visit increases, right?

**Dave Capone:** So, like, if you're seeing a, we track 10, and then, you know, we improve all 10.

**Jason Gong:** Oh, man, that one's, like, that one's where I think, like, only SEMrush can do it.

**Jason Gong:** Like, I don't even think Scrunch could do it.

**Jason Gong:** Like, you just don't have enough data to, like, isolate that from all the other random things that drive your traffic.

**Jason Gong:** It's, like, so hard.

**Dave Capone:** Yeah, so I think if we did, like, 10 prompts, and then we tracked and said, okay, we're going to, you know, maximize our ability to have visibility on these 10 prompts, it was worth X amount in visits, but then we go to 100, then we go to 1,000, and then we really try and think and scale it out to where then we can say, okay, best practice, diminishing returns after 1,000.

**Dave Capone:** So that's, you know, where we need to focus on for that.

**Dave Capone:** There might be a quicker way to get to that, but I don't know.

**Jason Gong:** Yeah, that one's tough.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Yeah, because you can't do that, like for one company, like you just statistically like it'd be impossible for you to like isolate that, but I don't know.

**Dave Capone:** I mean, we can isolate a thousand landing pages.

**Dave Capone:** That's not a problem.

**Dave Capone:** And we can run that in like an A-B test.

**Jason Gong:** You're not isolating for referral traffic.

**Jason Gong:** You're trying to isolate for like people learning about your brand being mentioned and then go to Google and they type you in like separating that out is going to be really hard.

**Dave Capone:** Yeah.

**Dave Capone:** We would need someone who gets like 100,000 visits plus or more a month.

**Dave Capone:** Maybe.

**Jason Gong:** Yeah.

**Dave Capone:** All right.

**Jason Gong:** All right.

**Jason Gong:** Cool.

**Jason Gong:** Thank you, everyone.

**Jason Gong:** Everyone's left already.

**Jason Gong:** Bye.

**Jason Gong:** See ya.

**Jason Gong:** Bye.
