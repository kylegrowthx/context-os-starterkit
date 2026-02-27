# CheckThat Weekly Check In

<metadata>
date: 2026-01-05
time: 18:00 UTC
duration: 39 minutes
organizer: marcel@growthxlabs.com
participants: Stevie Kim, Daniel Lopes, Leo Steffen, Pedro, Jose Farias, Jason Gong
fireflies_id: 01KDNY91VPQ4JYWYXF55DCZ4Z8
transcript_url: https://app.fireflies.ai/view/01KDNY91VPQ4JYWYXF55DCZ4Z8
</metadata>

---

## Summary

The CheckThat team reviewed CMS and editorial workflow improvements aimed at boosting SEO content creation and internal linking. They discussed cost optimization strategies including a proposed probe frequency reduction to every other day and evaluation of data vendor partnerships. The team addressed workflow reliability issues, implemented bug fixes for brand research, and discussed migration of editors to a new AI-driven page generation system with better fact-checking support and reduced manual controls.

---

## Action Items

**Stevie Kim**
- Create a ticket for probing schedule adjustment for free tier to every other day
- Create new ticket for library prompts to be set on every other day schedule
- Coordinate with data vendors (Ahrefs follow-up) on probing data partnerships

**Daniel Lopes**
- Review and consider new note-taking tools; ensure meeting host manages recordings
- Confirm with Marcel regarding resumption of brand research activities
- Create ticket to fix lack of failure catch/response in workflows that cause process hangs
- Write ticket to add internal linking workflow step for new profile brand pages to ensure correct source linking
- Support Jason Gong with migrating editors from Atlas to new generative AI page creation platform and gather feedback tickets
- Set up Sentry NCP as recommended by Jose for improved error monitoring

**Jose Farias**
- Add comments and improvements offline to prompt scheduling ticket including custom and library prompts

**Pedro**
- Implement iScope for cited domains and URLs per prompt after dependencies are merged

**Jason Gong**
- Migrate editors from Atlas workspace to new page generation system
- Collect structured feedback from editors in the form of tickets for continuous improvement

**Team - Lala & Daniel**
- Help Daniel monitor vendor costs weekly, coordinate with Alice on spreadsheet cost tracking

---

## Transcript

**Stevie Kim:** This meeting is being recorded.

**Daniel Lopes:** It.

**leo steffen:** Morning.

**Stevie Kim:** Morning.

**leo steffen:** How's it going?

**Daniel Lopes:** Morning.

**leo steffen:** Hey. Happy Monday, y'all.

**pedro:** It's Happy Monday. Happy New Year. Finally.

**Stevie Kim:** Yeah.

**leo steffen:** Yeah, that's right. Happy New Year. I'm still with all the kids at home, so it's. It's just crazy days. I just asked them to go downstairs to go to the pool because it's kind of warm today. They're just running like crazy around the house.

**pedro:** How many do you have?

**leo steffen:** Three. One is two and a half. And my wife is trying to put him to sleep. He should be taking a nap now, but he's starting not to want to take a nap anymore. And then the other ones are 6 and 9 and 9 again.

**pedro:** It's a full house.

**leo steffen:** It is, yeah.

**pedro:** Yeah.

**leo steffen:** This is joined.

**Daniel Lopes:** Here.

**Stevie Kim:** I threw the notion doc in the. Chat as well, so if you haven't had a chance to look at it.

**leo steffen:** Yeah, I haven't. Okay, let me take a look. You put it on the Slack chat?

**Stevie Kim:** No, on the Zoom. Yeah, I shared it in Slack yesterday. Yeah, I shared it in Slack yesterday. But I just shared it here.

**Daniel Lopes:** I don't see Here.

**Stevie Kim:** Yeah, with all the note takers or. Messages are taking over. I'll add it again. It should be on everyone. Do you see it now?

**Daniel Lopes:** I'll just.

**Stevie Kim:** Okay.

**leo steffen:** Thank you.

**Stevie Kim:** Yeah.

**leo steffen:** So I have fireflies here or what is it the other one? Phantom.

**Stevie Kim:** Yeah, we've been evaluating a few different note takers.

**leo steffen:** So, Yeah, I don't know what to do, so. But I should expect that the host of the meeting would be recording. Right. Or not. So if you're the host, then you'll be. You'll have it running or whatever it is.

**Stevie Kim:** I. Yeah, I think Daniel's the host now.

**Daniel Lopes:** Okay.

**leo steffen:** So I don't have to add it to any meeting. I go. Right. Someone else is going to be.

**Stevie Kim:** Yeah.

**leo steffen:** Okay, good.

**Daniel Lopes:** Let me take a look at your document.

**Stevie Kim:** I'm not sure if Marcel's gonna join today.

**Stevie Kim:** Daniel, do you know if Marcel's gonna join today?

**Daniel Lopes:** Daniel?

**Daniel Lopes:** There.

**leo steffen:** Oh, there he is.

**leo steffen:** Okay. Hey.

**Daniel Lopes:** I think he had a. I. Think Marcel had the call. The friend. You guys here before maybe join?

**Daniel Lopes:** No, it was his schedule. I just messaged him. I think we can start the problem.

**Stevie Kim:** Cool.

**Stevie Kim:** Yeah, we can. We can start.

**Stevie Kim:** Whoops.

**Stevie Kim:** Okay.

**Stevie Kim:** Yeah, Monday. Let's go.

**leo steffen:** Rev it up. The engines.

**Stevie Kim:** All right. So. So, yeah, I mean, I already did. A recap of like all the. You know, that was done last Friday. But yeah, just want to do real quick one here just to kind of show how we're improving and you know, getting a little bit more focused on that launch rate readiness especially. So yeah, just the CMS work, editorial work that, that Daniel did last week, we're in a lot better shape now to get editors enabled to create the content that we need, to, to increase the our SEO standing. So and then the cost, you know, mitigation, there's the, you know, the Gene fx but we're also looking into data vendors to partner with to see if we can, you know, decrease our spending. On probing and oh yeah, I didn't.

**Daniel Lopes:** I remember that you sent me a message to check a doc but I. Never checked if you could send me the doc again. Stevie, I can take a look.

**Stevie Kim:** Yeah, yeah, I met with similar web on Friday but he said that to talk about their probing data we need to sign an NDA. And so he emailed me that and so yeah, and then so he couldn't tell me a whole lot but I got like a high level overview. But we'd have to meet again with, with another you know, probably se on their side after we sign the NDA. And then I think I'm talking to. Ahref tomorrow, maybe I'll send it your way.

**Stevie Kim:** Cool. So there's a few blockers that we need to tackle in order to feel confident and comfortable getting it into our design partners hands. So the I think like the Google overview AI bow that's pretty clear about what the expectation there is. I think the one that the probe frequency. Peter, I did add some notes on that ticket before this meeting and really I just, I'll. Is it this one?

**Stevie Kim:** Yeah. So basically like you said, it does need to like we need to take the pricing into consideration. And so I was thinking about, you know, the free tier I think is more obvious because we have it set to weekly so it'd be we probe every day for seven days. Then the back off would be weekly pro tier. There's a range that's in that pricing doc. So I think we need to like be more clear about how often we want to probe in the pricing doc before we you know, tackle this ticket. And same with the business tier. Daniel, do you have any thoughts on, on this one?

**Daniel Lopes:** Yeah, I think like I know this came from our selling came from the, from the monetization document but even just in the short term, just adding in the crop, just adding if today is just every other day, if we do nothing and we do a 20 minutes change today to just probe every other. Day, I think that would already cut our cost in half and Then that would be a temporary thing that we can do until we figure out this whole process, I think, because I think. If I remember correctly, because I was thinking about taking a pass, she'll just do a design architecture. Sort of talk here with how we could structure this because it's going to be a little tricky every time I start adding pricing tiers and then the pricing tier changes. What you do with the best code starts to get a bunch of if. Else stuff around pricing. And where do we put the tiers? Like would be the plans that we pull from Stripe. Like would that be defined as features in Stripe? The stripe supports features. There's all this like downstream things that can be a little bit more complicated. But until we figure that out, just. Like adding like every other day I think would be enough.

**Stevie Kim:** Okay. Yeah, if that makes sense. Yeah, no, that sounds good to me. So we can't. What we can do then is create a new ticket for that.

**Daniel Lopes:** Yeah.

**Stevie Kim:** And then. Yeah, and put this one on the back burner for now.

**leo steffen:** Stripe has an auto discount or something feature that we could do for the free. Free tier. You can leave.

**Daniel Lopes:** We can.

**leo steffen:** Don't need any. Anything in particular for the free tier.

**Daniel Lopes:** So you just need to know which plan the. The custom prompt belongs to it when you're running it. And then I think the backend is also more complicated because you need to know who does the account, who this prompt belongs to when you run it. So you need to know if it's somebody that's under a different tier and then if they change tier then they need to update that. So there's like all the relationship of. The prompt with the plan and the account here. We haven't coded the plans yet, so. It's a little harder.

**Jose Farias:** Sorry, quick question. Only custom prompts will have a custom schedule, correct?

**Daniel Lopes:** Yeah. Right. Yeah.

**Jose Farias:** So in that case that can just be a first party field on the, on the prompts table.

**Daniel Lopes:** I think. Yes, you're right.

**Jose Farias:** Okay, we can, let's. We can take it offline and I can add some comments to the ticket. I think there might be a judo there that we could.

**Daniel Lopes:** Yeah, you're right. Yeah, I agree. Yeah.

**pedro:** From our last, from our last sync, I remember Marcel saying something like the library prompts should be. Should have frequency too. That was mainly my question.

**Daniel Lopes:** Yeah, I think there's two, two layers of frequency here. There's like the custom ones that will be tied to the pricing and then. You have the library ones that will run more frequently and. But with the definition of more frequent on the Library ones to me could. Be like every other day for now, you know, just to. Because I don't think it's going to impact the data how you guys display. If there was anything that's on a daily basis, then you would see like. That it would be like this funny chart like this because we're not going to run it. But I don't know if that's going to impact.

**Jose Farias:** We'll have to make some changes, but they're not difficult.

**Daniel Lopes:** Okay.

**Jason Gong:** For what it's worth, I think Scrunch has always been on every three days and their charts are all weekly. So like it almost never occurs to you that it's daily. So I think there's like wasted. Almost like design around that too.

**Daniel Lopes:** How you're showing it. That's a good call out. And then on the flip side on the data collection for this study, I know that Isaac is making progress there. That one we're going to run every. Day and with no limits on search tools today we have limits on search tools. That's another thing that we might in the future want to add as like a pricing tier. So if you're an enterprise then we increase search tools. But that's a little bit unrelated because we split. It's not going to impact. Because we split the. So when you guys are changing. Oh yeah. That actually impacts. So like on the current job today I think we have both combined. Jose. So it's so. And then the. The data collection for the study, we. Want to have a special frequency. We want to have data that makes sense. Cool. Sorry to derail the.

**Stevie Kim:** Totally fine. That's so yeah, as I said, I'll make the ticket for that for the library prompts to be daily or sorry every other day schedule. And then that other ticket will just be for custom prompts and that way. We can kind of separate the.

**Daniel Lopes:** The link one. I'm not sure I like. I think I understand. So like, is it that cloud AI. Was a broken link? Like right. Right under the.

**Stevie Kim:** Yeah.

**Stevie Kim:** So.

**Daniel Lopes:** This is broken links or that. We are linking to the outside sources.

**Stevie Kim:** Oh, this isn't linked to a ticket. I'm thinking maybe I got this from Slack. I should have linked to the Slack.

**Daniel Lopes:** Because if it's broken links then then we need to figure out. But if it's the correct source.

**Stevie Kim:** No, I think it was. Yeah, it says it was linking to cloud instead of internal pages, but I don't know.

**Daniel Lopes:** Yeah, it would like. It will like that's the way it's set up. Now so it will.

**Stevie Kim:** Okay.

**Daniel Lopes:** Because just going to use the right sources for everything. The problem there it was because we. Didn't have an internal linking workflow and I added this week. But that only works on the pages and the profile page, it doesn't run. Through the pages so system to the page pipeline. So we would have to add a. Step to the researcher. So when we research a new brand. Would add a step to the researcher to use the same internal linking workflow from the pages. So they will like look for dimensions. Of different brands and then link internally. And that will solve it. But then we have to decide if there will be. There are cases where like linking to. This external one is correct. So it will say things like the source for this is this external link that is correct to be external or points to the G2. So pointing to external is not a problem. We just want to make sure we. Link to our internal ones. The new workflow does that. And we would want to decide if we want to do forward only or backwards. Backward. You'd have to write a script that. Executes 6,000 internal linking profiles. But I'm not even sure the profiles are good enough to do that effort. I think like forward. Think fixing forward would be ideal. And then we fix with the ones we want to have it. Super. Right. You know, maybe add a button or. Something so there's like some. I can write more. I can write the ticket for this.

**Stevie Kim:** That'd be great. And you know, I. So the only problem with only, you know, fixing them going forward, I mean, it's. Well, I mean. Okay, so I think maybe three. A few of us have. Have gone through the design partner workspaces. Right. So those really need to be great and you know, and have the. The internal linking. But that's. I mean this is more for SEO anyway. Right. So I don't think that. Yeah, I think you're right. Probably like fixing the. The current ones probably isn't a priority because we don't have that much. Right. We don't have that many. We haven't created that many.

**Daniel Lopes:** Yeah, we have 6,000 and they are. Kind of linking well between each other on the pages. So that's more than I. Yeah, I. Guess that's more than I. Yeah. So we have 6,000 profiles and you. Pretty much find any brand, like almost any brand. So like when I run the internal. Linking on alternatives, for example, all the. Profiles are linked correctly. So.

**Stevie Kim:** Okay, see, I thought this was just. For the new pages that we were.

**Daniel Lopes:** Yeah, the new pages is fixed. The new pages that's going to be fixed already. Yeah. The only place that's not going to do that is the profile. So the profile.

**Stevie Kim:** All right. So, yeah, I'm assuming. I'm assuming.

**Daniel Lopes:** Yeah, I can talk to myself about this. But for SEO reasons, I don't think it matters anymore because the pages will have all the links, and the profile. Links to the pages, and it links. To the page at the tab, and it links to the pages at the section. So, like, the sections of the profile would be like alternatives or pricing or user sentiment. Each one of those sections now linked to the page, and that page has. Links to all the profiles of the companies mentioned. So I think the trailing map of the internal link is there. It's just more if we don't. If you want to fix the profile page too, but.

**Stevie Kim:** Okay.

**Daniel Lopes:** I don't think it's a blocker. I think it was a major blocker if we're talking about pages. And that was the thing that I fixed this weekend.

**Stevie Kim:** Got it.

**Daniel Lopes:** I was finishing the thing.

**Stevie Kim:** Got it. Okay, cool. Thanks. And I think that. Oh, there was one other that I wanted to. Not that one, this one. And I do think we need Marcel for this. Pedro had some questions, and I reread it again, and I was actually not quite sure exactly how Marcel wanted the ui. So.

**pedro:** I will basically move on with the approach I proposed there. And we can see, because these are just white changes. The one that so should should be in this one. I mean, I still need to implement. And this. I can have your input, Jose. We need to implement iScope for cited domains and URLs for a prompt scope. But I think that's after your pr. Right, Right. So I can catch up from there and calculate the cited URLs and domains for each. For each prompt as a scope, and then we are ready to display this data here.

**Stevie Kim:** Now, that sounds good to me. If it's not a lot of work. To change things, then if you need.

**pedro:** To change later, it's just UI changes.

**Jose Farias:** Cool.

**Stevie Kim:** Those were the only ones I wanted to talk about. So if anybody has any updates they want to share. All right, now's a good time.

**Daniel Lopes:** I hit some little stuff on the admin and then I can create a bunch of tickets like the screenshot one I created already, but deleting a brand I created as well. So that was problem. There was an issue with the researcher. There is one bug that affects all the workflows, actually. And, like, if the workflow fails, we. Don't send back a modification to the app. So you see that sometimes you get research. If we do like a brand research and it hangs for forever, it's probably. Because the workflow failed. Same thing would happen if the page generation. So if the workflow fails like there is no catch of failure in our flows that will send the webhook back to cancel that execution. So that is one that might be. I can create the ticket for that. But that, that one I think is worth fixing because we want to do a lot of brand researches. That's one thing that we kind of stopped and we should start doing again. Just like going to the brand candidates, looking at the known companies and triggering the research.

**Stevie Kim:** So I think Marcel wanted us to pause on that. That's why I stopped doing that because we already had enough and he wanted us to focus on yeah making the ones that we have really excellent. Instead of continually adding new ones, I mean we've added new ones. For instance, if you know a competitor is know to like one of our customers or workspaces doesn't exist. We've done that more ad hoc. But yeah, I haven't gone through the list like I was doing just because. Of him wanting pause on that. But it, it might be, it might be good timing to, to start in again maybe.

**Daniel Lopes:** Yeah, I, I'll ask him in the chat because I think there's no. It doesn't hurt to add more pages. We just wanted to validate. If you're having like 6,000 pages that were not indexed would be a problem like off the, like of the, the. Start and I don't think it is. Because we're getting like all the impressions and everything. And now that we, we would have. To fix anything that's like specific to the profile. But I'm not seeing any problems with the profile. You know, the profiles that are usually accurate and all that. There was one bug that I also fixed this weekend that the research of. Brands sometimes would find the wrong branch brand. So we have things like Delta. It's, it's probably not Delta Airlines that we wanted. It's probably another Delta. So I started passing the context. I think that works but I didn't QA that a lot. So if you, if you guys start. To see brands that should be another brand, then there might be a plug on what I did. But now essentially whenever you trigger a brand research, it will pass the, the probes that they show up like the. Top three probes and that would be part of the Google query to try. To find the domain for the brand and then we scrape that domain so that should take care of that. For example, peak and profound. I think they got stuck because the domains were not found. Yes. So that's another thing that I did this.

**Jose Farias:** And.

**Daniel Lopes:** Probably a good idea to read the readme that I shared or like right before the call the readme and the loom just to see how the page generation works.

**Jason Gong:** Oh actually a question on that to managing like the editors that are creating the pages is the idea like the stuff they're doing in Atlas will eventually just move straight into check that out.

**Daniel Lopes:** Let me actually share that and then. Like maybe if you have any questions since you're here, Jason, like you'd probably need it better so to lose your 5 minutes of your time period to. See how that works. But we added there was a bunch. Of workflows under the hood. They all use the same researchers and agents that we use on contentos and Atlas. But if you go to slash admin. Go to slash Admin and Pages, you. Have page types here, there's four fixed types and then you select one of these, you type the brand you want to create and then you have probably we should never use this. And then if you click Generative AI it will create the brief. This takes about 30 seconds. What we'll do is take all the. Profile data we have and do a Gemini search. Do like a Google enabled Gemini search to see what are the things we. Should cover considering that profile or what. The Personas and that kind of stuff and then it will return a search. Intent, a Persona and.

**Jason Gong:** To like take the places.

**Jason Gong:** So like right now like all of this is in Atlas, right? Like they've hand carved artifacts, they're like hand editing them.

**Daniel Lopes:** Yeah, artifacts. Yeah. We should sunset the checked at workspace. In Atlas and ask them to just create through here and this will generate the outline to generate the direction. So it's the same fields that we. Would usually have in Atlas but with everything hand carved here and under the hood. Everything like with the artifacts and the writing guidelines, everything is fixed under the hood and we can change them. But I would rather have folks change. That once they try to use it and tell us what to change. Because that's where things are going south on contentos. Just folks start changing the writing guidelines of the proofreader and it's completely like we get the agent stuck without control. So ideally just they go through here, create a few pages and then if they say like oh, actually for alternatives or for pricing, I don't want the. Section am I having to edit the section all the time. The info to change that is under. The hood and it's like super easy to change. So would the rather better to have. Them tell us what to improve than let them try to improve. If that makes sense.

**Jason Gong:** Okay.

**Daniel Lopes:** And then just to walk you through the whole thing. So like they will generate an outline. With this format, like H2 and whatever is in square brackets. Here is whatever they can guide. They can also change the outline however they want. If there are a specific format that we want to follow for every single page with the exact same titles for each H2, we can do that too. We just wrap it with strict, but we can also add that to the template. So this is coming from a template that informs the general direction of the outline. That template is not specified to be strict. We can make the template be strict. And then whenever you define this, you will have under the research questions. Research questions are hidden and they are read only, so you can't change that. But whenever you change this, the next. Step will update the research questions to match the new outline. So that should create an accurate research data set for the generation. And then once you generate, you will see a page very similar to Atlas. That will be like just like waiting. I think this one already finished.

**pedro:** I guess.

**Jason Gong:** So it sounds like the reason we're doing this is because, you know, taking a little bit more control out of their hands is better. I just know like the editors we have on check that, like Harry and Kabishka, like they're for example, they're making custom artifacts for each pipeline. All that stuff they're doing. What is the best way to now migrate that?

**Daniel Lopes:** Yeah, I saw the artifacts. I don't think the word for X would work. So I took the artifacts and created. One for each of the content types. So yeah, I checked what they had. And I don't think that was going to be a good idea. And this is the system that we're. Going to have in contentos in the future. So we're going to completely remove folks control out of artifacts and we're going to have like a personalized or personalized. Writing guideline, calibrate the writing guideline and then you choose things instead of free form writing because the free form writing is essentially prompting and some of the. Things that they have, for example, the proofreader checklist would throw the. It would make things hallucinate because they're. Asking for information that was not in the, in the context anymore. So same thing that would make things. Get stuck in the loop because it. Was Actually not proofreading, it's more like research question. So there were things that were in. Different places where they should be and that I think contentos is designed wrong in my mind where we exposed the controls to the wrong users. That was meant for be like the Karten's team to do it and we have non technical users doing it. So it gets stuck in problems. But under the hood here we have the content type and the content type. Can have the artifacts. So if they have specific things that they want to do with like pricing pages or answer pages, we can do that for them. They just use the feedback.

**Jason Gong:** Yeah, so I guess I'm trying to think of. So is this. Should I ask them to switch over to this new method now or give you some different time?

**Daniel Lopes:** Okay, exactly.

**Jason Gong:** And then if they have any feedback to kind of create that in the form of tickets now like here's what it spat out, here's what I would like. Kind of perfect document.

**Daniel Lopes:** Yeah, exactly, yeah. Get them to use this right away. And we can close check that there for now and it's all synced. So like everything you're going to do here will publish automatically because that's another problem we have if we were trying. To use content OS that there was no way to publish back already. So but now it's publishing here. So if they just go through like. For example I created this one for client right before the status in draft. It has the COVID images stuff the. COVID image you might want to sync. Up with Ren to improve. But it's just an HTML, it's easy. To change and it's easy to regenerate. So once we have we can regenerate in bulk or one by one. There is also like since we are doing the profile research ongoing instead of. Having all the brands there, let's say Andropic wasn't here. So as you can see it's all linked into internal profiles. All right, so but let's say there's a brand that wasn't here and we. Add the profile, then you have to. Come back here and refresh the internal links. So it will update the article and add it. When I do this, it also adds. Additional related articles here at the bottom. This will be automatically but you can also do manually. So if you click manually here, it's just markdown syntax and you can put any kind of link you want that's in our website here. And once you press this, it will not delete the past ones or just append if there is new ones and people can Remove. So that is the internal linking part. So you can trigger from here cover images as well. And when you generate the page, it. Will generate everything will generate with internal. Links already will generate the meta descriptions. And it will generate the COVID image. And I think that should make their life faster.

**Jason Gong:** Yeah, I think it'll definitely make the 0 to 1 part of creating a page faster. And then the editing experience like I guess they can figure out. And then we'll just give feedback and tickets, but I'll, I'll get them to migrate to this. They did tell me, I was talking to them earlier that like the fact checking was what was taking them time. I think to them fact checking just meant like you know, hey, is it reflecting the right price for pricing pages, et cetera. But I think I'll again just ask them to give you that feedback in the form of tickets.

**Daniel Lopes:** Yeah, so for the fact checking if it helps. So let's say like this one, if they're editing like the view that they. Would see right after pressing that generate article button would be this form. And in this form here, let's say. They're not sure if the $200 is correct. There is at the bottom here there's a research summary that you can look for the pricing, you know, so the. Information that was used will come from. The research summary and we can structure the. So this is where it came from and put in the sources. So it's in the same article. It's just the same page. It's just collapsed on that bottom layer. So that might be a good tip for that. And then you can see where it came from. And then they're talking about legacy prices and that kind of stuff will be tricky to find on just Googling, but you can't find that on Google or Perplexity or Cloud like folks do. So that's why I'm keeping the research data there as well, if that makes sense. Okay, sounds good.

**Stevie Kim:** Does anybody else have any updates or. Questions or things that are blocking them?

**Stevie Kim:** Cool.

**leo steffen:** Yeah, six second rule. No, I don't have any.

**Daniel Lopes:** I merged those change on Friday, on Saturday that does the genus split. So if anybody. I think that change that we made last week was already enough to reduce the cost. I'll double check today. But yeah, essentially we should be good. It was my mistake. Essentially we're scraping HTML using HTML as. Tokens and I think that should put. Us in a good spot for.

**Stevie Kim:** We're not gonna, we're not gonna do any other changes for now on from like the audit.

**Daniel Lopes:** I don't think so. And Lala, he'll be working with me to like put all the costs, all the vendors in a spreadsheet and maybe have Alice help us pull like on a weekly basis so we keep an eye on the cost and they can split the cost from like Atlas, check that and the rest of the company so we can see where the cost is going. To increase cost. Like adding AI overview will increase cost. And one of the concerns that I. Have there is that Google has a different rate limiting. So when we are adding that, that might be a problem because if we run 6,000 calls to Google, I don't know if Google can handle it at our current price, our current plan. But I don't think Google is going to cost a lot. The real cost comes from anthropic OpenAI and debug from Jina. But keep an eye.

**Stevie Kim:** Boom. Sounds good.

**Jose Farias:** Just a quick one for Sentry. If you not using Sentry ncp, you should start using it because it was game changer for me. Like I just copy pasted like a slow query issue and in 15 minutes was fixed, committed, pushed and it worked well too. So you should definitely give it a try.

**Daniel Lopes:** I'll set it up.

**Daniel Lopes:** Cool, Cool. All right everyone, thank you.

**Stevie Kim:** All right, thanks. See you guys later.

**Jose Farias:** Thank you.

**Daniel Lopes:** One, two.
