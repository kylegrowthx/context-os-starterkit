# CheckThat Weekly Check In

<metadata>
date: 2026-02-23
time: 18:30 UTC
duration: 36 minutes
organizer: marcel@growthxlabs.com
participants: Estevão Mascarenhas, Marcel Santilli, Stevie Kim, Pedro, Daniel Lopes, Jason, Leonardo, Nigel, Jose
fireflies_id: 01KHPN5Q6KJ6PZQR1B4BAPDM4Q
transcript_url: https://app.fireflies.ai/view/01KHPN5Q6KJ6PZQR1B4BAPDM4Q
</metadata>

---

## Summary

Marcel shared progress on CheckThat V2 prototyping, having spent 200 hours on the product over the past month with 100 hours focused on UI coding. The team discussed creating a front-end prototype to validate design before full development, focusing on three outputs: improving public-facing pages, creating a detailed single-brand audit view, and redesigning the dashboard. Estevão agreed to collaborate on transforming the manual prototype into automated workflows while maintaining a research-driven approach for scaling across categories.

---

## Action Items

**Marcel Santilli**
- Validate acceleration support for CheckThat V2 prototype with Daniel
- Continue refining audit methodology and prototype structure, integrating feedback from team
- Sync with Daniel and update Estevão and Stevie on next steps
- Lead creation of manual prototype approach to automate workflows and presentations for end-to-end functioning prototype

**Estevão Mascarenhas**
- Support collaboration with Marcel on shaping the UI/UX prototype and automating workflows
- Prepare for iterative sketching and rapid mock-up sessions for prototype development

**Stevie Kim**
- Participate in knowledge sharing during prototyping sessions to absorb insights

---

## Transcript

**Estevão Mascarenhas:** It.

**Marcel Santilli:** Hey, Stevie.

**Stevie Kim:** Hey. How's it going?

**Marcel Santilli:** Oh, well, being much better than last week.

**Stevie Kim:** Oh, I'm pretty good. Hanging in there. My dog is recovered from her surgeries, and it's been a long time since she was completely healthy, and I forgot what a little devil she is, so trying to get back to training and all that good stuff.

**Marcel Santilli:** Yeah. Nice. That's good. She's feeling better.

**Stevie Kim:** Yeah. Yeah.

**Marcel Santilli:** Hey, Pedro, Good to have you back. Yeah. Good to be back. It felt like a month, so.

**Marcel Santilli:** Everyone, I think Daniel might not be able to join today. So I don't know if you're waiting on anyone else.

**Stevie Kim:** No. You created this meeting. Did you have... I did, yeah.

**Marcel Santilli:** Oh, that's... These were deleted because we moved to one engineering a week and then the strategy meeting.

**Stevie Kim:** Okay, well, I didn't move anything, so it was either Dig or somebody else on my.

**Stevie Kim:** Oh, it popped back up like, okay, okay. And then there's another one this week, so.

**Stevie Kim:** Yeah.

**Marcel Santilli:** Okay. So just so I understand, what is the cadence today or...

**Stevie Kim:** Yeah, like, when do you all check in? Yeah, so we do it on Mondays, like an hour. Basically an hour ago, we have our engineering check in. And that's where I kind of try to bring everybody up to speed on what was discussed between you, Daniel, and me on Fridays. So, like, kind of the overall, like, strategy, like, if we need to change our priorities or anything like that.

**Marcel Santilli:** Okay, cool. All right. And I think we can drop. But Stavon, if you wanted to stay on, I. So see, we just kind of catch up. So I. I chatted a little bit with Jose just like 30 minutes or 40 minutes ago. I'm still. Dana's still heads down. So I'm still like, just want to triple check with Daniel. But what I'm hoping to do is, like, try to pull Stavon to help me with accelerating my prototyping.

**Marcel Santilli:** And a lot of kind of, like, taking essentially, like, where I am and kind of translating into like, this is what it could look like before we go. And, like, essentially, like, I'm almost calling this, like, a CheckThat V2. Like, you know, to probably the better way to kind of, like, think about it, you know, And I think it's getting closer and closer. But what I told Jose earlier is in the last, like, call it like, 30 days, I probably spent 200 hours on CheckThat related things. AO related things. And of those 200 hours, probably only about, like, 50 or 60 of those hours were actually, like, connecting the dots, reading, researching and things like that. And probably a hundred of those hours were like, like VI coding.

**Marcel Santilli:** So I'm decent at it, but nah. Um, like, I'll give you like a quick example. Like, earlier today, it was like, I. I think I spent like 20 minutes just getting this grid, like to look the way I wanted to, you know, and it's like, gosh, like, I don't know. That was the best 30 minutes of my time. It looks nice now, but it was like, you would laugh at my prompts, like, back and forth, just like, nope, nope, nope. And so I'm sure it was like, it would have been like a five minute thing otherwise, you know, like.

**Marcel Santilli:** But, but, but I think we're. I'm. I'm getting closer and, and I think it would be really, really helpful. So I want to validate with Daniel, but either way I think it'll be helpful Stavon and others if others want to stay on. But I just don't want to distract because I feel like it's so like unbaked, you know, I was just trying to get help on. Think of it as like creating a, like a V2 that's like front end prototype only.

**Marcel Santilli:** And then we will use one brand. I'm thinking either webflow or one where we have a lot of data is a customer and they're in a mature category that's like a category that's like well established. And then we can use that to just like validate everything you're doing, doing, and then get like end to end working, you know, or. Or at least like looking the way we want to look. And then we can reverse engineer and go like, okay, cool. Like, what do we need to do in order to make that like, be true, you know?

**Marcel Santilli:** Okay, cool. Nigel, Pedro. Jose. Like, feel free to drop Jose. I'm just gonna stick through ND if you want to stay on something.

**Stevie Kim:** Yeah, I think it'd be good for me to get as much cool info as possible.

**Marcel Santilli:** Okay, cool. Take care.

**Marcel Santilli:** But. Okay, so let me take you through you all through a little bit. Kind of like where. Where I am right now. Okay. So how I got here is effectively there's a couple of different paths of that I'm taking. So one path was the. Let's call it like the handbook path, which was like me trying to write out my thoughts, which is kind of like part where we are, part where we're going, part where how I'm thinking. And so it's kind of like there's some divergence there. But. But I think this is getting like better and better every day, you know. And then as I'm flagging things, I'm like, okay, cool. Like today I made some big changes to presence score, for example, right. And I'm trying to update everything.

**Marcel Santilli:** I haven't done the fine comb through everything. Like it's like directionally good and accurate and there I haven't gone through. There might be still a few inconsistencies as I'm updating things. You know, there might be other references to this that might still be outdated. But like overall links is getting really close, right? The, the challenge with this is like as I'm doing this, I'm a very much a visual person. So it get to a point where I'm like, gosh, like I just want to freaking see something otherwise my brain stops working, right?

**Marcel Santilli:** So, so then one of the better ways to do that was we had these strategy sessions. One of them was with this company called Eon. And I'm like, well let me just like go to town and spend a couple of hours just like doing an audit for them, right. Like end to end and see like what I would present to them, right. What's cool about this one example is that they're like in the data recovery backup kind of categories, but they're like a new player, but they raise an F ton of money and they're doing really well. And so you know, it's like they're worth over a billion dollars backed by Sequoia and raised over a hundred million and they're like non existent in AI visibility, but they're like a Gartner cool vendor or whatever, you know, so, so they like to, they seem like more, more legit.

**Marcel Santilli:** So then I started to do that, right. So, so I went in, I think I might have shown, but I, let's see, records customers and I created like a bunch of different things, like a prompt guide, like what prompts I would track. I did research on them. I looked at like how analysts cover them, you know, and so you can kind of see like it did like a whole analysis of their whole space. I did an SEO analysis of Sam Rush's like CP server. I looked at sources that are cited and checked at like to classify their sources, right. So I was looking at like every single source and check that and then trying to compare and understand like which ones of those are vendors, which ones are analysts influencing their space boats, right. And, and, and then I analyze their blog, I analyze all their competitors blogs as well. Like I, I did a ton of work here Right.

**Marcel Santilli:** And, and this is probably like, let's call it like $50 worth of like personal credit. Slash, like, you know, API credits, things like that. Like maybe last. But. But like this is still not crazy, right? Like this, this is very wasteful. But it's not like, you know, this was like a thou. It wasn't a thousand dollars worth of compute, right? Like, and this can all be done using the context of check that and everything else, right. Like so, but then it's like overwhelming amount, right?

**Marcel Santilli:** So then as I was sharing with them last week, it's like, gosh, like I need to send them something. So then I took kind of like two approaches. One approach was like, look at our entire methodology, update it and forget check that exists. Or like knowing that check that exists. Like, let's create a whole new experience based on the docs only, you know. And then another one was kind of like. And for me it's helpful to do these one shot things because it like even if it's off almost always, there's at least one or two things that are like, oh, that's cool. Like I kind of like that. Right?

**Marcel Santilli:** Like so whereas like the getting the thing right, once it gets to a place, it's like, oh, how do I present this? It's really hard. If you go like component by component, module by module. It's almost like a. I can just like one shot it and then you just like tweak and play around with it and then you try a couple of different ways, you know. So, so did that and it was like pretty decent overall, right? Like it's already like way more digestible than, than like what it is today, you know, because it's like, it just gives you like very specific things, you know, like the benchmarks or whatever and like trends.

**Marcel Santilli:** And then there's a lot more deep dives. But even within the prompts, it's like it tries to hide away. Like the prompts are like the behind the scenes. Don't worry about it a lot more, you know, and, and then the other approach I took was like doing a. Here's like these seven MD files with a ton of stuff in it. And like how would you present it to this binder, you know, and this is this, right? Which is like broken down more based on the audit I did, right? Which is like competitive intel. This has like an entire like competitive landscape. All the players and our analysis of the set of where they are.

**Marcel Santilli:** And then for each of the players, like perception scoring of like the analysts, you know, like the like it feels way more like, whoa, this is like good qualitative information. This is like SEO performance audit. You know, some of these are like, still need to tweak a little bit, you know, and then there's like competitive, which I did like content efficiency. So I looked at all of their competitors and we looked at authority score, number of keywords they rank for organic traffic, and then value of the traffic, backlinks, and then how much content pages, how many content pages the competitors have, AKA like blogs, guides, AKA work or THX to create for them and then where they are at and then traffic per content page.

**Marcel Santilli:** And it's like you can see they get like no traffic. And then you can see their competitors, right? Like, like it's. It's pretty clear. It's like not just a volume game. It's like traffic per page is also important. And. And then it kind of gives them some analysis of like them versus the medium. You know, it just feels more like, holy shit. Okay, this is like very concrete, you know, like, this is like how I would do it, you know, content efficiency, you know, you can see where you are. And this is where like I started to realize this is a good example because it's kind of like a player that has money and is legit, that also is at zero.

**Marcel Santilli:** But it might be even helpful to find one like middle round customer, well established, has some area like some, some version of that, right? Like we could do augment code, we could do webflow. Like it depends and then like it suggests some winning strategies. But then this stays at the level that it's not super like specific, right? Visibility and category mapping. This is more of kind of as you can see here, like this took like a lot less of like, this is the framing fit only information to this framing. And this is more like the full audit, right? Like, so, so this is, this is a lot. But this is literally all of this is. Let's call it like four workflow outputs at most, right? Like, even though this seems like a lot, this is mostly like a deep researcher, right? This is literally like one really long prompt, some context files on the brand and then going go to town and figure this out, right? Like it's. It was truly like, like insane. Like just to give an idea, like one of them was even through perplexity. And it was like, it was like truly like one shot. I gave it some context files and then it was just like this. And this is what I came up with, right? Which was like, so a lot of this data is based on like Legit one deep research. So obviously we can do better than that. Right? Like so.

**Marcel Santilli:** So that's the good thing about this is, like, you can give it the methodology and then you can just ping all these models and then aggregate the findings of all these models. So unlike the visibility where we need to actually probe a ton all these other areas, I think we can do more as like a qualitative deep research as opposed to like truly having to probe. So think of these other areas as like, you know, this is a little bit less than recommendation. So anyways. All right, so this is where I am now. And. And now I'm kind of like trying to go like one by one and. And let me try to find this really quickly. Overview 1. I just did, And I think it might be in scratch pad. Give me a sec. Gotta find where it is.

**Marcel Santilli:** But. But now I want to kind of like go through the find of use. You know, in the product. There's a file here. I got to find where it is. But it was essentially like a plan for like the overview of section. Like tap, for example. Right. And then let me find where it is. I think it's this. I gotta find it. But it was the overview tab where it's like, I'm essentially like aggregating everything. Right. So anyways, I'll pause here, but the ideal scenario for me would be like, I shape and get it to a point, you know, and then like Stavon, like, you take that and like, we create kind of like the structure overall, you know, and I have like, a lot of ideas, so we can have like, kind of like sketching sessions and then you can quickly, like, mock it up, you know, and. And kind of like take it from there. And, and. And then like, kind of like we were working like pretty intensively, like together on this, you know. What do you think?

**Estevão Mascarenhas:** Yeah, that's awesome, by the way. I think. Yeah, like, I'm trying to visualize the workflow, but I think what you have already, like, already gave me some ideas how to add to the app. But just so. Just so I understand better, your idea is to protect something entirely new from the UI perspective using check. That's like look and feel. Or should we think about how do we fit it in the current app, like, experience? What's your thoughts on that?

**Marcel Santilli:** So there's two separate things. One, the way I was approaching this initially was to. A lot of these things are going to be. Take a step back, trying to organize my thoughts. There is potentially three outputs, right? One output is changes to the public area. And so which is. We want things to feel like a bit more like this, right? Like, we're just like, oh, okay, cool. Like there's like adoption over time and like, there's charts or whatever, right? Like for, for our public areas.

**Marcel Santilli:** And a lot of these, like, composite scores and trends are become like, more actionable than just the visibility one. We already made like, some awesome improvements to how it is the public pages are today so that it's like, already better, but even today it's still like, visibility only only tells you one part of the story, right? Whereas, like, if we incorporate how AI perceives the brand, how AI their overall reputation in the market, as well as like the presence and visibility score, then it starts to become, like, way more concrete as well as, like, we start to, like we talked about last week, like, make the category pages, like, really, like, more contextualized.

**Marcel Santilli:** But that's an output. That's not the first output because first we need to nail like a good view for one brand for one audit, essentially. Right? And so for me, I'm trying to nail a bit like, snapshot. Like, this is the. You have a customer coming in and they're like, help me with this, tell me what the hell is going on, right? And, and then what we're trying to do, which is what I started, is like our version of this, which is like the AO grader slash. This, which is like amplitudes AI visibility, which, by the way, it's like they don't even update. Like, look, this was last updated November 3rd, likes it. So it's just like super one off. Like, clearly they don't care about this and they're not creating public pages on this. But I do think it's like, simple enough that makes it like, oh, cool, this is awesome, right? And it's kind of like the hook, if you will,

**Marcel Santilli:** and then the third output, and then we can decide which order we kind of tackle is the version of the how do we evolve our current experience? Which today we validated that from an SEO perspective, like, people want this information, right? It's like week over week. But from a like, usage perspective, no one is getting any value out of the dashboard. And the reason for that is because, like, even I struggle with like, coming through analysis. And then I'm like, can you just give me the data? Because I'm just going to run like an agent on this because this is insane. Like, there's no way I can come up with, like, any insights, you know, so unless we can kind of like get to that point with an audit, almost like the dashboard just becomes like a double data that then is going to be less powerful than just like an agent with an mcp, essentially. Right. Like, which might eventually become the only way we can do this. It's just like, honestly, it's just like power people with more of that kind of view, or let people sign up and have access to the data and then they can pull, you know, through either Connect or MCP or something else. Right. So.

**Marcel Santilli:** So I. I don't see today a way that this is like a slight tweak of, like, what we're doing is a slight tweak of this. The probing the data, the visualization, the components, I think are going to be evolved and used. Like, you know, we're not going to throw away this, but. But, like, I just don't. Like, there's no way you can look at this and go, what am I supposed to do with this information? And in what context is this in? Like, what is this for? Like, what. Like, there's nothing here that drives that. Or if you go in here, like, there I. There's no way to make sense of this. Like, there's nothing you can possibly do with this information. Right. Like, it's the right foundation of data, but then, like, there's layers of data processing and data pipelines that to. To then get to like, oh, okay, like, this is what it means. You went from this to this. Or. Or even if you look at something like this adoption year over year, you're like, oh, I see. This makes sense. Like, HubSpot is getting fucked and Salesforce is okay, and that's kind of it. Like, you know, it's like, cool, like, right? Like, there's no way to, like, be able to come to these conclusions any other way, you know, and that's why visualization is so important, is because, like, it's part data, part processing that and then. And then figuring out, like, this, like, when you lay out this, it becomes like, whoa, this is like, this is it. Like, this is the weight, right? Like, this makes a ton more sense. You know,

**Estevão Mascarenhas:** the analytics makes a lot of sense. Like, if we get like, one freaking awesome report, like, if we can nail that, like, just uncovering what we add to the public page or what we wired behind the upgrade plan or something, I think it's going to become like, just a matter of monetization and how to present that. Yeah, I agree. I think you're right. Like, let's start with just one report and make it awesome, because all the Data is going to be there and then we just figure out how to present that and how you can shape the product around that.

**Marcel Santilli:** Yeah. And like, and then what I was thinking is like, this can pull data from a bunch of different places over time. The report itself, and it could be packaged as Growth X, not just check that if needed. Right. Like, and so, and it's what we have to do at the beginning of an engagement, no matter what. And so like at the beginning of every Sprint kickoff, we have to do an audit, we have to analyze the brand, we have to understand their competitive landscape. Like that's just work we're doing. Except everyone is just like prompting perplexity and whatnot. And no one is like really doing this or they're going into Semrush and doing a, you know, a one off look. Right. But it's so much easier to do it and this more programmatic way. And then there's can just some of these components we don't have to tackle right now. It can just be like ways to visualize an output of something we're doing, you know, and this could be like a huge lead gen for us on both sides essentially, you know.

**Stevie Kim:** So is your expectation that it would be like the similar onboarding experience where we would do the research, kick off the workflows through the onboarding experience, or would we do this already for like. Well, we couldn't do it for all brands we have in the public place. But anyway, what, what's your, your thought on like, how this all how these reports are getting kicked off and is this for free users or is this for paid? Like, where is the cutoff there?

**Marcel Santilli:** Yeah, like, so once we have a full report, we can figure out like, okay, this is where. But what I'm hoping is something like this will become the golden standard for all the categories and something that people start to share publicly because people are starting to like the CEO of Atio, share a screenshot of this page and a link to this page. Right. Like, so say that that would be my hope is that people are growing. They're like, whoa, this is, look at us. Amazing, right? And, and, and then like these public pages become way more shareable and then the audit itself becomes way richer with like, but, but in a way that's easier for people to kind of understand. Right. Like, so these scores, hopefully we can surface them publicly. And, and then the audits are like kind of like the deep dives where, you know, we grab all of it and then we make sense out of it. Right? Like like we might not have this like full detail here and you know, but that's, that's kind of like. Okay, and like me being publicly, we might not have this level. Right. Or we might only limit to like the, the leaders publicly. And then the audit, we might show like only you in the top 15, you know, and, and then like hide the rest. Right. Like, so if you go to like crunch base, like they do a really good job with this which is like you can see certain trends. Right. And it's like there's locks everywhere, right?

**Stevie Kim:** Yeah.

**Stevie Kim:** So lightweight version of the scores and some of the audit for the public version and then for after sign up and I'm assuming they'd have to pay for the full audit.

**Marcel Santilli:** So. Yeah, yeah, like you can have these essential modules where you show just a little bit and it's just like explore and it's just like unlock this, unlock that. Right. Like so we're unlocking like modules in depth of data, but you're still showing like this, like this level hopefully.

**Estevão Mascarenhas:** So yeah, just confirm my understanding. So we're all online. So the idea is for us, Marcel, should. So basically you have a prototype that was manually made and it's like in shape. The idea is for us to basically automate it, like to create basic workflows, the presentation for it, not the final thing, but like an end to end working prototype. And then after we settle on that, okay, this is what we want, then it becomes like the backlog for the team.

**Marcel Santilli:** And then we all like, yes, except along the way, let's say we're trying to do part of the deep research is like go look at analysts and blah, blah, blah, and figure out how analysts do this, this, this and this. A lot of the stuff I did, it was like five deep researcher processes and then taking those five and then coming up with this. And so for us, kind of similarly like, hey, if we're going to do this, we might as well figure out, let's pick this category. And this category has like 50 players. Okay, let's go make sure those 50 profiles are created and then let's make sure we're tracking all 50 of those. Okay, cool. And then we do it once and then we say, okay, can we go enrich the public profile so that we're pulling mostly from our public pages over time. Right. Like so, so we're using the process of creating one off to figure out like, okay, this is a no brainer to have publicly so that the deep research can go fetch information externally. But mostly it's like, if you think of, like, okay, you have 200 categories. 200 categories each have, let's call it, like, 50 shortlist players, right? It's a lot of data, but, like, 250, okay, that's 10,000 pages. It's not that far off from where we are, kind of. Right. So if you do, like. And you don't need to update it daily, right? You only need to update it, like, monthly or even less often. Some things may be weekly, but most things are, like, company description doesn't need to change more than, like, once a month, maybe, you know, and you can. And so that's kind of the idea is that, like, the deep researcher is the aggregator of the information. And as much as possible, we're pulling from there, but we're trying to validate end to end and. And then kind of go from there. But let me run to this meeting, but I'll ping you later if you're. If you're around. But I'll also sync with. With Daniel, and then I'll. I'll let you both know.

**Estevão Mascarenhas:** Awesome.

**Marcel Santilli:** All right, talk soon. See y'. All. Bye.

**Estevão Mascarenhas:** Thank you. See you. Bye. Bye.
