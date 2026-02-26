# CheckThat Weekly Check In

<metadata>
date: 2025-12-15
time: 18:00 UTC
duration: 41 minutes
organizer: marcel@growthxlabs.com
participants: Gianpiero, Estevão Mascarenhas, Jacopo, Marcel Santilli, Pedro, Daniel, Jason, Stevie Kim, Jose Farias, Leonardo
fireflies_id: 01KC4VVPYN3XDS95D9G6560AV6
transcript_url: https://app.fireflies.ai/view/01KC4VVPYN3XDS95D9G6560AV6
</metadata>

---

## Summary

The CheckThat team focused on organic growth validation, SEO strategy, onboarding improvements, and bug management processes. Marcel outlined a two-step milestone: validating organic traffic growth through public area performance and ensuring existing customers can use checked-out accounts effectively. The team discussed plans to validate organic growth quickly before a full product launch splash, with emphasis on CMS improvements, editorial workflows, and addressing infrastructure challenges like API caching for brand data.

---

## Action Items

**Stevie Kim**
- Add summary and detailed descriptions to milestone documents
- Create necessary tickets for onboarding flow and SEO-related work

**Jose Farias**
- Arrange a 1-hour meeting with Marcel and Stevie to review and shape onboarding flow and CMS improvements
- Put up a PR for major backend refactor concerning portrayals and prompt rankings

**Leo Steffen**
- Join onboarding and CMS shaping session
- Coordinate with team to verify Brandfetch API key usage and integration

**Joe Beschi**
- Configure JavaScript error logging in Sentry
- Optimize admin area performance aiming for requests under 5 seconds

**Estevão Mascarenhas**
- Investigate Brandfetch API key usage
- Assist in onboarding experience shaping

**Marcel Santilli**
- Share shaping doc with team
- Prepare for leadership presentation and dedicate time for onboarding/CMS shaping

---

## Transcript

**Estevão Mascarenhas:** This meeting is being recorded.

**Marcel Santilli:** What up? Happy Monday. I need to get more coffee. Be right back. Okay.

**Leo Steffen:** Morning.

**Stevie Kim:** Morning.

**Jose Farias:** Good morning. It's great to see your face, man. It's been a while.

**Jbeschi:** Hey yeah likewise. Good to see you all.

**Leo Steffen:** Good to see you all. This is my first weekly check in with you. I joined last Monday.

**Jbeschi:** Yeah I saw your face in the record.

**Leo Steffen:** Yeah that's me Leo. Nice to meet you all. And please add me as a reviewer to your pull requests. If you submit any I would like to just follow up whatever is going on.

**Jose Farias:** Will do.

**Marcel Santilli:** All right I think we have everybody. Stevie do you want to kick us off?

**Stevie Kim:** Sure. So I was out Friday so before Friday though I created after talking to Marcel like we created these lanes of focus areas that we wanted to keep everybody aligned on. I had put some tickets already in those lanes and I just want to thank everybody who picked up you know tickets that were prioritized around organic growth and especially. And so I just wanted to give a shout out to everybody who just took the initiative there to grab things that were in those buckets and looks like there's you know about three at least that are in progress. All right I'm just gonna share my screen real quick.

**Marcel Santilli:** Yeah. In a quick context that we're trying to move towards this make sure we keep in mind kind of the milestones and outcomes we're trying to optimize for. Right. And some of these check ins like keeping the focus on that essentially like at the end of the day the main things keeping us from trying to make a massive splash on this thing is one validating that the public area can grow organically. Right. So keep posting updates. But and there's like a major set of kind of changes if you will of the kinds of pages publicly and a whole organic strategy. So Jose I'll set up time with you and Stevie later this afternoon just to kind of get your thoughts on the. I guess you can call it PRD or just the shaping docket pull together before we share with everybody else.

And so there it's mostly like we don't want to go out to the market and say hey everybody look at this thing. And then tip our hand on this kind of like share library plus SEO play strategy that we have. Right. Milestone number one. It's like go as fast as possible and validating that input to output being traffic organic traffic. And if we get that validated then we're good. Right. We're getting impressions not quite clicks yet but the signals I think are pretty positive. And then the second one is validating that our existing customers can be successful using our their checked out accounts essentially validating that through our teams first. Right. And so end to end we have feature parity or at least an end to end experience for tracking their AI visibility. Once those two things are validated then we can say we are launch ready. From being launch ready then we can add let's say a week or two to actually make a big splash. Right.

So we can think about this phase as sprinting as hard as possible towards that. And then there's a couple of big buckets that we haven't focused on that are also going to be we're going to need to tackle which are mostly around the onboarding flow signup flow that some of the missing things. Right. And so this week I'm hoping to we can all shape that a little bit more and and start to prioritize as well. So that's the big picture I guess.

**Stevie Kim:** Yeah no that's perfect. That way I don't have to go through this doc but this is the overview page and I did put some descriptions in the milestones and Marcel if you want to excuse me. Take a look at this and you know change anything that you know you think needs to be updated and then I'll add up at the top in the short summary that the two like highlighted areas of focus that Marcel just covered.

**Marcel Santilli:** Cool. Yeah. Any any thoughts from folks on. On kind of. And also what how to make the most out of these check ins.

**Stevie Kim:** Crickets.

**Leo Steffen:** Crickets.

**Stevie Kim:** All right well so as I mentioned I did you know add some of the some tickets from Triage and and other ones that I noticed that were SEO related into these buckets like the organic growth strategy. If you know of any other ones that fall into these focus areas definitely you know add them to the milestone. I haven't gone through every single ticket in here and then some of them just are titles and I don't have all the context yet. And so if you know more of what those tickets are about know that they're related go ahead and add them to the milestone. So so yeah just there's you know a couple of ways that people like to work. One is to pick up tickets that they're kind of interested in doing and and working on and that that was my ways preferred as an engineer. But also some people like you know to be assigned tickets. So they just want you know like at the beginning of the week they just want to know what they're working on. So feel free to you know tell me like your preferred way of working and I can accommodate that.

But right now I'm just letting people pick things up that are prioritized into these milestones around the organic growth getting ready for that. And then yeah as once Marcel gets that shaping doc in in a place where we can start creating tickets we'll want to prioritize that because we want to enable editors to be able to execute on our plan. Our growth strategy around creating all these different pages for SEO.

**Marcel Santilli:** I think we can jump into. Yeah sorry go ahead Leo.

**Leo Steffen:** I would like to ask how you guys manage or jump into issues such as Sentry alerts or any CI CD failures. How do you do that? Is that. Or bugs for. For instance do you add it to the board or just wait for an alert to common Sentry and. And assign it to a person? How does that work?

**Jose Farias:** I think because Sentry is already sort of like a board in and of itself. Duplicating it in linear might be repetitive but I think let's all just agree to keep an eye on Sentry. If anything high priority comes in we should all be capable of identifying it as a high priority issue and just like jump on it and fix it. Usually they're quick. If it's not quick we can create the ticket ourselves. That sounds good.

**Leo Steffen:** Sounds good. So it is an agreement that we're all going to assign or whoever wants to look at any of the issues just assigned to them on Sentry and we work from there.

**Jose Farias:** That's good.

**Marcel Santilli:** And Jose right now would you say there are any division of areas when you see a bug? Like meaning like if you see something come up in Sentry is the goal for anyone to be able to tackle any bug or that there are certain types of bugs or issues that might be better tackled by someone that worked more.

**Leo Steffen:** I mean there are two levels right? First you get an alert you take a look at it you assign it to yourself and you triage it. You just look into it and see if there's. If this. That's something you can fix. If not then you just go if it belongs to a person or is from another team or it is more likely to be successful.

**Marcel Santilli:** Somebody like I'm asking more for I guess for Jose like today or for anyone else that's been on the team a little longer like have them. Had there been cases where something comes up and it's like well it's actually probably best handled by someone else. You know I saw it.

**Jose Farias:** But yeah. So I think let's just handle it on a case by case basis and be like definitely. If it come if you see it take a look. I think everyone can have the the criteria to be like oh yeah this is. This is Jose bug. Like I'm just going to tag him and essentially what Leo said. So we could take it one at a time I think for now.

**Marcel Santilli:** Okay.

**Jbeschi:** Yeah. Let me add that we have already Atlantic alerting for sentry errors on Slack. So you don't need to like proactively check Sentry every day or every hour or something. If there is any a new issue unassigned you get the alert on Sentry on Slack. And also we have alerting for Ioccurring issues. So if you have like an issue that is occurring too often you have an alert no matter if it's assigned to someone or not. So you don't need to check Sentry. Like just check Slack and it's enough.

**Jose Farias:** Sorry. One other thing to add. I think let's not worry about stepping on toes right now. It's just like if you see the solution submit a pr. If it's a one liner like maybe even merge it and CC the person that has the most context and then they can take a look in their own time. If whichever engineer is like oof I don't know about this solution like this fixes it but I don't know if it's good. Then you can just wait to merge and wait for a review.

**Marcel Santilli:** Perfect.

**Jose Farias:** And I think that's enough process. So that sounds good.

**Marcel Santilli:** Yeah that sounds great. Yeah definitely leaning towards speed given we have no external audiences using anything right now in private areas. So definitely moving towards speed. Makes sense I guess. On the. I'm just curious for the one that we had last week around I think it was the BREX workspace where one of the screens was blank. Was that actually a bug was there just like a. Because the user didn't do this thing first. This thing was a known screen. I'm just trying to understand those types of issues or friction points. Like a blank screen for example.

**Estevão Mascarenhas:** Thank you. So Brax I think that workspace that got created by the admin panel that feature that I did. So when you create created there what happens is it doesn't start with any prompts so the workspace starts blanks. What we can do is if we want to keep doing that change it. So when you create A new workspace. It starts with already the subcategory prompts so it doesn't start blank. I can change that. It's real simple. So what I did to fix that is just added all the subcategory for Brax all the prompts there and then the data starts picking up. So that's what happened. I think this is part of the onboarding flow as well. Like what we want to do. Maybe we want to give a choice to the user like if he wants to import everything from the secretary or start just with custom prompts or something like that.

**Marcel Santilli:** Yeah I think like on the onboarding flow what I was hoping is I want to spend a lot of time with Jose and Stevie on shaping a lot of the what I call like the CMS changes because they're pretty pretty significant and you know Daniel reviewed it and was pretty good with it you know so I don't want to over shape essentially. I think it's at a place now where we need engineering input. But then on the onboarding flow if. I don't know if like maybe Leo or Style like one of you wanted to shape it a little bit as well that would actually probably like help quite a bit. And working closely with Stevie on that just because I think we already have a pretty good idea of the kind of. At least from a technical perspective which like the company context the Personas like all of that works really well. It's just mostly the experience of signing up. We don't want it to be like why force someone to go in the panel and click like contacts right? Like we want to require a domain to be given as a primary domain. You want to associate a brand with it whatever you know so.

So I think that that could be a good. Because I'm. I don't want to be the bottleneck I can be the reviewer there. But it seems like a lot of the issues are going to happen on an experience perspective from us not the defining what the minimum requirements of inputs are to create a workspace all the way to what a good experience should look like you know.

**Estevão Mascarenhas:** Yeah I discussed a couple weeks ago with Daniel and yeah he told me to wait for when Jose was back because he did like he started working already with the onboarding flow. Like the first version that we worked in he had put something together but. But I can help. I don't know. Jose is pretty busy with other parts but if we can split work that's that's fine. I can sync with him as well.

**Marcel Santilli:** So let's maybe hold off for today and then Jose like we can tackle. I was going to book an hour for us this afternoon. I have a presentation today with the entire leadership team of HubSpot at 12:30 but then after that I'm pretty pretty flexible. It's going to throw an hour for you me and Stevie to to just go through the doc that I pulled together as well and then we can tackle plan out how we want to shape the onboarding experience as well. If that works.

**Jose Farias:** That works.

**Leo Steffen:** Include me in this column or so.

**Marcel Santilli:** Perfect. Yeah. See if you do you mind throwing it on our calendar? I put a block on my calendar but it's from during our 101 essentially for an hour two to three. And then you can include Jose and Leo as well. And I'll share the doc with everyone as well. I just don't want anyone to be like distracted until it's properly shaped.

**Stevie Kim:** Sounds good.

**Marcel Santilli:** Cool.

**Jbeschi:** There's one thing I'd like to ask about bugs. It could help because right now we are only catching Rails bugs Ruby bugs in Sentry. So that means that we're not going to catch every possible issue right? What we could do is also start collecting the JavaScript errors and reporting them. But it's going to be noisy. So that means that we are going to have some error that are not so important and some that might be important. So we need to value correctly the signal noise ratio on that. And also even if we do so we're not going to catch our bug with Sentry because Sentry is going to catch only the errors. But we can have bugs that are not actually you know runtime errors in Ruby or JavaScript. So as next step what I can do to maybe help with catching bug is set up the JavaScript sentry setup configure it and we can see how it feels. But it's going to be noisy. So maybe I can set up some on alerting and we see how it feels. Maybe it's gonna help. But I just wanted to clarify that we're not gonna catch every issue with Sentry and no matter how we configure it right we need to do some QA and visualize stuff because otherwise it's not possible to catch everything.

**Marcel Santilli:** Yeah that makes sense. And I think like a couple of things that for me are are I think important. Turning it on I think is good or tracking more I think helps because we can always filter the alerts right? Like to exclude those but at least like capturing so that we can. And then what I was thinking is mostly like extremely slow load times. Right. Like if a screen or something is just taking like really long time to load but also including the admin area in that ideally as well as we start to like. Because I noticed like I think that that's one of the areas where it feels like three to four times slower than everywhere else which is understandable. And then if there's a way at all to know if like there were blank screens or things that just from a user experience were like friction then that would be really great too because as we go down the next several weeks or so knowing that like the number of screens that were just either blank or just took a long time to load or reduced overall that's already like a good outcome to at least try to like see if we're making progress towards you know.

**Stevie Kim:** Yeah I noticed the same thing. It was on. Yeah on Thursday I was going to create some tickets around that around the admin area where it was. The slow load times will affect editors being able to you know work on the. The pages and then trying to get that data quality like if you have to go in every day to brands or you know prompts and stuff and it takes you know you're just waiting for the page to load for a while. Yeah it's. It's going to be an issue just with their productivity.

**Jbeschi:** I haven't optimized the pub. The admin pages sorry because I thought was not necessary but I will do some work on that and we do have alerting already for slow request so we are notified if we have like if the app is behaving badly generally we are notified and then we have punctual like filter that we can use to check for every endpoint. I've done some optimization on the public mainly. Mainly public area. Sorry but I will take a look at the admin. I know there is some like for example I can see that we have like 23 second requests sometimes on admin prone controller index right now. So I will just make sure that Everything is last 5 seconds in admin and below 1 second in public era. I will work on that.

**Marcel Santilli:** That'll be great in the context here just. And it will make sense once I share the docket finish shaping it. But we should assume that there's going to be anywhere from 100 to 200,000 public pages on the site in the next three or four months. So that's a good assumption to have between because we're already at 23,000 brand pages and each brand page is going to have potentially one to 10 variants for pricing or reviews or other things and and then you have both category lists and you know and all the other areas that I put in the organic strategy doc as well that hopefully if if anyone hasn't read definitely read that one for sure. The the organic strategy one.

**Stevie Kim:** So I did have a question around this this ticket I made last week around the each prompt should be associated with more than one subcategory and I wanted to see if there were any questions on this ticket or.

**Marcel Santilli:** The extra context here too just for everyone. I talked to Daniel quite a bit on Friday like we should and look at the thread as well. I posted a comment of a mental model in the thread but the idea is that things evolve over time. I don't know if you captured that part.

**Stevie Kim:** No I'll put it. Yeah I'll put the thread in.

**Marcel Santilli:** But the way to think about it is like legal AI wasn't a category until like six months ago right? But there might be prompts over time that we know for a fact we want to add it to the shared library right? We might not want to have that associated with the category necessarily or maybe multiple categories that prompt might belong to because those categories might be evolving right? And so we should think of categories as really just like a holding group or a group of prompts that might be evolving. And you might want to be testing different categories right? For instance CRM and sales might be a category but you know AI for sales might be an emerging one right? And some of the prompts in one should be in that other one. That doesn't mean this one's going to get deleted necessarily. You know it just might might be different.

And so the concept of categories as a holding group for subcategories is going to really corner ourselves into like a really rigid structure where at the end of the day we want this to be more and more closer to how brands and buyers think of these categories if you will as really like hey when I'm buying like for instance like when I'm buying a piece of software for our company right? Like I think about it in a certain way right? And the way I think about it changes and evolves right? I wasn't thinking about like coding agents you know like a year ago necessarily as a buying group right? Or category. And so we want to try to keep it as flat as possible and also just have the ability to manage a shared library of prompts. The best mental model is that what we're building is a shared library of prompts. And and then we're tagging those prompts if you will in different ways that make sense you know for our audiences or our customers with. That makes sense.

**Stevie Kim:** Yeah. And I'll add that some of them don't make sense right now and it'd be an easier way to edit them by adding them to the subcategory that they actually should belong to. We're also changing or you know adding subcategories like Marcel said. So that added flexibility will be really really helpful for people that are going in all the time and having to review all the prompts that are in subcategories that we have.

**Jose Farias:** I think this should be relatively straightforward barring any surprises. So we can just prioritize this as up next and any any one of us can tackle it.

**Marcel Santilli:** Perfect.

**Stevie Kim:** I think that's the only one that I wanted to to get some focus on just. And clarity. I think most of the other ones are pretty straightforward and a little bit smaller. But if anybody else has questions on tickets that they want clarity on feel free to. To ask now.

**Marcel Santilli:** Yeah I think the one in my mind is just making sure the. Especially the the charts. I think we have a ticket on just like the overview charts and things like that. Like some of these things are like first impression things you know and we.

**Stevie Kim:** Have a lot of tickets on those. So yeah Kyle I think made a lot of tickets. So I was actually going to take a little bit of time with you during our. Our call but to. To kind of figure out what we wanted to do there. Marcel. But we can. I can do like a. Create maybe one ticket instead of just having all those piecemeal ones to talk about to shape the experience a little bit and then have you review it. If you'd rather do that.

**Marcel Santilli:** No I think we're. It should be pretty straightforward like the ticket I submitted with examples you know and explaining like what. Like just the experience. It's just like. I think it's fairly like common sense of like hey if you see a chart that has like 50 lines on it and it's hard to read and you're not really sure where you're looking at or which line and which color to associate with which brand like that's just like an overwhelming experience. And then I just gave examples of what profound as well what peak does well and kind of like in the screenshots and the tickets. So I think like anyone can tackle that just because we're going to have that chart like visualization everywhere in the app. And so just making that a common Component that we feel really good about is going to make a big difference everywhere.

**Stevie Kim:** Yeah yeah I just meant more of like the. The smaller tickets that have been created more recently. Some of them are you know just to be able to filter on like model prompts. Like there's a lot of scrunch parody that we're missing. And so those are kind of more of the. The tickets. I wasn't sure if you guys wanted them in one ticket or if it's fine them being separate for them.

**Estevão Mascarenhas:** I.

**Jose Farias:** For what it's worth I think generally I personally do prefer separate tickets for separate issues. The one thing that does jump up to me is there's like a fidelity concern here in linear where there are milestones and there are tickets in those milestones and then these smaller ones like if we put them there like it's a lot of noise so maybe we just add a bugs milestone or like.

**Marcel Santilli:** A lot of these are going to be under the experience one I think which I think is fair. You know like.

**Jose Farias:** Yeah that works.

**Marcel Santilli:** Yeah.

**Jose Farias:** If they're all grouped together then that works just to differentiate them between like oh this actually like is a big one and needs shaping and engineering input versus another one that's like a quick one layer.

**Marcel Santilli:** Okay that sounds. That sounds good. And the the only other one that I haven't posted yet but I'm just curious. Like one thing I notice is right now the way we're working on the broader like CMS and how we manage pages and slash profiles for brands and kind of like public pages. Because today there's not a lot of controls over almost most of the aspects of those pages like the meta description or the meta title and things like that. So I might suggest some small tweaks to those while we're working on the bigger one. For instance like the fact that our H1 and meta title for all the brands is just the name of the brand and then a dash check that AI is not great. And so even little tweaks like that to have overview pricing and blah blah blah in that makes a huge difference potentially on it getting ranked. And so might be a couple of those kind of in between things. The. That will. That will help. Any. Do we want to go around really quickly or anything that folks are either unclear or want to share. As far as like just to share context on any work from last week.

**Jose Farias:** I'm about to. Sorry sorry. I'll just say real quick I'm about to merge or put a PR up for a significant refactor. It has to do with all the data stuff essentially like the portrayals and the prompt rankings and whatnot. So just a heads up in case anyone is touching that code. Back end or front end? Probably best to pygmy just so we can coordinate because it's a. It's going to be a big one in terms of conflicts or surface area for git conflicts. That's it.

**Leo Steffen:** And workflows. Repo or check? Just check that.

**Jose Farias:** Oh check that. Just check that.

**Marcel Santilli:** Cool.

**Estevão Mascarenhas:** I have a quick question. I was checking which account we are using for brand fetch and the key that we're using I couldn't find. It's not the account that we have on our password. Do you know if you created an account just for. Just for check that. Because my idea there was to use brand fetch to get the color of the brand so we can put in the chart. Brand fetch already gives us that. So it would be nice. But yeah just confirming which color.

**Marcel Santilli:** No but Leo this would be a good one for you to help.

**Leo Steffen:** We have separate keys for.

**Marcel Santilli:** Yeah. And anything we can do to just try to cache as much as possible. So we're not pinging brand factors API because the cost will go. Oh like we'll go up quite a bit. Right. Like if you have you know I I don't know how. Like essentially like if you have a logo you know like we do one API call grab everything cash and store everything and then maybe set a trigger to to like repaint the API if it's you know outdated. Otherwise it's going to get into the tens of thousands of dollars probably pretty quickly. But yeah.

And brands don't tend to change like the the their logos that frequently you know so I think that would be good.

**Leo Steffen:** Yeah I'm gonna ping you later still.

**Estevão Mascarenhas:** All right.

**Marcel Santilli:** And. And they have two different APIs. I don't know if you're familiar with it but but essentially like there's the. What is it the search API versus the the logo API or something. So the the search API you know I think it's easier to use for the search experiences versus the ones where we're filling out logos. You know people. Data labs already. Data labs. You have the firm graphics. Yeah. And this is. Sorry I'm just make. Change the speaker here. The. Just to make sure. Sorry one second. Okay. You guys hear me? Okay?

**Jose Farias:** Yep.

**Marcel Santilli:** Got a special guest over here. Yeah. And Stamil for what you're saying is mostly to fill out the logos right? Not for grabbing data or is it for grabbing additional data?

**Estevão Mascarenhas:** No no for additional data. We discussed. I created a task but I'm prioritizing other tasks that Stevie discussed with us on the milestones.

**Marcel Santilli:** I was on the wrong speaker. Can you say that again?

**Estevão Mascarenhas:** Yeah no no worries. No it's not for it's not for data reachment for that what we discussed. I created a task but I I I'm prioritizing the charts the SEO bugs and other stuff. So.

**Marcel Santilli:** Yeah. Estevão Mascarenhas: Do you remember if you have. Yeah. Do you remember if you have account. You created account for brand patch just for check that. Because we are using a key there that I think I might.

**Marcel Santilli:** Yeah I think I might. Estevão Mascarenhas: If you can yeah if you can share later that would be nice.

**Marcel Santilli:** Yeah yeah because that we're going to use quite a quite a bit but.

**Marcel Santilli:** Cool. That sounds I think we're on the free so it's definitely the free one that lets you do a bunch of calls but so I can create another one if I don't. But I think I did. So the way so just to understand like yeah it's under tools. So it's tools.

**Estevão Mascarenhas:** I think I tried to sign you with that but the key that we're using this client side it's different.

**Marcel Santilli:** Yeah yeah I think we can swap it. Leo you can you can work with both Yousef as well as like Ericsson or Bridget if just to see if anything else is hitting our ramp. Cards. There's no credit card. Okay. Yeah. So their logo API is very high high throughput free. So we can just swap to whatever. Well and just to understand. So so right now if we are monitoring prompts right like or somebody sets up a workspace and now we find you know we identify new brands then if the way I understand it is those brands get put into a queue to go do deep research on. Right. What when and how are logos fetched from brand fetch in that process? Just so I understand for my own.

**Jbeschi:** They are just fetched for the CDN every time you hit Endpoint. We use their own cdn. We can even maybe use our own CDN and cache their CDN if that's going to work. So we don't do. We do zero work. I'm not sure if it's going to work. I need to check but maybe if we just set up something on Cloudflare maybe we can just cache it or maybe we can just store the logo when we process the brand. That's going to work too but then we need to update them like daily or something. Yeah yeah we have those two options mostly.

**Marcel Santilli:** Yeah like the More. I think we just like decide when those triggers happen so that like as it adds up. Right. And as we expand knowing like the more we're pre processing those things that come up in the experience the less likely people are going to run into users. You know run into things where it's just like a blank logo because we haven't fetched or we're waiting for brand fetch or brand fetch with hot reload. It's essentially we just link to their logo. So. And their logo CDN is open so we can you pass the API key just. Just because they asked. But you don't even have to. But we could have a fallback on the server and just use the same. So. Yeah yeah yeah. Okay. That sounds good. Yeah. The. The more we. I guess we can rely on our own stuff in case like Brent like what would happen today if like let's say their API was down? Let's just put like would every logo on our site be down?

**Leo Steffen:** No it's a cdn so it would. Be locally unlikely to go everything down. Okay. Distribute. Because it's like yeah yeah it can't happen. The Cloudflare. Yeah. Everybody goes down.

**Leo Steffen:** Yeah.

**Marcel Santilli:** Nothing to do or like lovable. Took down all of GitHub at one point. I don't know if y' all remember. Yeah they were talking about it in the webinar. Yeah Cool. Awesome. That. That sounds good. I'll. I'll. I'll share the. The doc and then we'll. We'll do the session a little bit later. But did you guys cover the cms? No no I'm doing an hour session later. That's. That one though. That'd be good. Awesome. All right thanks everyone. Talk soon. Cheers. The recording has stopped.
