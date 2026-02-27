# Lovable <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-19
time: 21:00 UTC
duration: 31 minutes
organizer: marcel@growthxlabs.com
participants: Rachel Hepworth, Megan Dickey, George Haikal (GrowthX), and Lovable team
fireflies_id: 01K9X5SEE5WSG97R68P7DMYC7B
transcript_url: https://app.fireflies.ai/view/01K9X5SEE5WSG97R68P7DMYC7B
</metadata>

---

## Summary

GrowthX and Lovable reviewed competitive positioning, template generation workflow progress, and reporting dashboard improvements. Lovable is second in organic search volume behind Replit with a clear SEO opportunity ahead. The team demonstrated a 21-workflow automated template generation system achieving high quality output. A new Looker dashboard tracks guides and template performance; GA4 integration pending to track user behavior beyond clicks. The team discussed scaling to 10 guides and 10 templates weekly and reviewed a new homepage template strategy.

---

## Action Items

**George Haikal (GrowthX)**
- Send list of non-branded competitive keywords with rank and volume
- Break down organic keywords and summarize competitor SEO strategy focused on templates and blogs
- Follow up with Sebastian on prioritizing high-intent website templates for the main landing page
- Scope resource and engineering needs to double guides and templates production to 10 per week
- Resend Looker dashboard access and recap in Slack to all participants
- Check with security lead on approval for GrowthX to merge PRs with weekly security reviews
- Retroactively retrieve signup data for redirected how-to pages for analysis

**Megan Dickey (GrowthX)**
- Ensure GA4 integration and update Looker dashboards before next update

**Rachel Hepworth (Lovable)**
- Confirm GA4 access with Igor and Elena, and request adding George Haikal to GA4 access
- Coordinate GA4 access confirmation and confirm meeting cancellation due to Thanksgiving week

---

## Transcript

**Rachel Hepworth:** This meeting is being recorded.

**Megan Dickey:** I just saw that most people declined.

**Rachel Hepworth:** This, like cc.

**Megan Dickey:** Anton Infernal declined.

**George Haikal:** They always do. CC does it this week. It's usually just Rachel and CC on these calls.

**Megan Dickey:** Okay.

**George Haikal:** For sure. Cool. Yeah, no worries.

**Megan Dickey:** How you doing? How's your day?

**George Haikal:** Good, good. Got a lot done. Which is awesome. How was yours?

**Rachel Hepworth:** Good. Just busy. Yeah. Still good. All good.

**George Haikal:** Surviving.

**Rachel Hepworth:** Yeah. Survival.

**Megan Dickey:** Yeah. And like, my AirPod stopped working, so hopefully I don't sound too, like, echoey.

**George Haikal:** But that's cool. When they stop working that stuff.

**Megan Dickey:** Yeah. It's like they'll connect to my phone but not my laptop. Like. Yeah. I think I might just get, like, the next generation of AirPods, like, just for fun and see if they're any better. But. Yeah. Hey, Rachel, how you doing?

**George Haikal:** You're muted.

**Rachel Hepworth:** I said I'm good. How are you guys?

**Rachel Hepworth:** Good, good.

**George Haikal:** Well, doing well. Are you also over at the HQ? Is that just CC this week?

**Rachel Hepworth:** No, it's just CC. No, I refuse to travel to Europe and I would definitely not be on this call if I was in Stockholm. So I think it's going to be just us today probably.

**George Haikal:** Yeah, no problem. We can get into it. How's everything with you before we jump in?

**Rachel Hepworth:** Good. Yeah. Just getting ready for Thanksgiving break next week. I'm going to be on the East Coast, so it'll be a good change.

**George Haikal:** Where at?

**Rachel Hepworth:** New Jersey.

**George Haikal:** Nice. Nice. I grew up in Boston, so not for Thanksgiving, but for Christmas I'll be back home. It's been a while, but I love the East Coast, especially when it's. I guess it's starting to get wintry, but when it's fall turning to winter, it's pretty cool.

**Rachel Hepworth:** Yeah. Yeah. I think it's getting pretty cold right now.

**Megan Dickey:** Yeah. I'll be in the Midwest, so a little older and less interesting, some might say.

**George Haikal:** All right, let's do it. Share my screen. Cool. So a ton to go through. I'll speed through the more routine reporting stuff because I want to show you some insane progress Rachel that we made. I was on the line late last night with our engineers kind of running through end to end the template workflow and where we've gotten it. It's super impressive. So I'll show you that today. But before. Is there anything related here that's top of mind for you?

**Rachel Hepworth:** I think the main thing I want to understand is how to look at the metrics and maybe that'll be a next week thing. But reporting is the main question for me.

**George Haikal:** Fantastic. So what we'll do, we did another site audit. We'll go through what we found there. That was more competitive market. Where are we at compared to Base 44, Replit, V0 and then specifically in terms of if they're doing anything on blogs or templates. Yeah, focused on the work that we're doing. I know you asked about that last week. We'll go through that, run through the templates process and demo. We'll go through the guides and we put together some reporting. But next week we'll have it very, very, very dialed in. But right now we see all the numbers week to week, the change, and it's a nice clean dashboard view and it's organized by templates and guides. So we'll run through that. We'll talk through the GitHub integration that I shot over to you as well to clear that out. And then template. Excuse me. Sebastian had a template project for the main landing page and I kind of collated all the details, information and our thoughts and I'm gonna run through that with you at the end to see if we should drive, what your take is, etc.

**Rachel Hepworth:** Okay, great. Cool.

**George Haikal:** So first we'll do this quickly, but essentially we did a content audit. It's linked here, shared with you. I'll jump into the link in a second. What we looked at was all the competitors, search volume, specifically organic search volume in the categories that we care about, which right now are blogs and templates. The three main things that I pulled out and then we can dive into the report itself is Base 44 is really the only competitor that has a blog. It's brand new. Right now there's less than 30 monthly visitors. I can show you right here. But they are publishing pretty quickly. So it's just something that we're always monitoring and staying on top of. They kind of just stood up a blog and so we'll stay on top of it. But we're definitely doing well in comparison. V0 similar thing, not too many total monthly visitors. They only have a template library and their strategy is basically pulling projects that the community pulled or that their team members made in pretty disorganized links. So they're not. They're not thinking it through like a program or portfolio. They're more so getting these templates out and it's not driving again, a ton of traffic. But we're monitoring and we feel like the structure of our template library is already in a great place. And then in terms of overall organic search volume, right now, Lovable is second you can see right here only to Replit. And 80% of this organic traffic from Replit is all branded and the other 20% is for really, really, really niche keywords like Python Compile or things that we don't really want to compete against. Anyway, so the short story here is in terms of our goals, which are guides, templates and scaling those organic growth engines, it's a pretty blue ocean and we already have the foundation set and so super excited to now start tracking the actual metrics, optimizing and driving real results because no one else in the space is doing a good job at it.

**Rachel Hepworth:** The keywords we think would have value. And this is kind of the flip wave looking at it. Who are the people ranking for those keywords? If we have a list of like, hey, we would really. If we could be in the top three of these 20 non-brand search terms, it would be amazing. Do. Is it useful to understand that at all?

**George Haikal:** List of non-branded search terms, who is ranked? Yes, yes. And we have that. And I can send it to you.

**Rachel Hepworth:** Yeah, I'd just be curious. And then for Replit, it's like they have such a huge number of keywords and Bubble IO as well. I mean they've obviously been at it for a lot longer. What is driving that for Replit? Like if you look at their. Is it just that they have like a lot of templates or a lot of content? I'm curious what's happening there. I recognize that they've been around for like, I don't know, seven, eight years. So they're in some ways a very different stage of company. But I'm curious about that.

**George Haikal:** Yeah, I mean the majority of their traffic is going straight to their homepage.

**Rachel Hepworth:** So when we look at. Yeah, but. Okay, but that would be the same as Lovable. I mean the organic traffic column you have is that visits. Like they have 1.8 million visits a month or like what is that number?

**George Haikal:** Yeah, visits.

**Rachel Hepworth:** But okay, because I don't. It's hard to believe that Lovable's brand name is driving way more visits than. Or that Replit's brand name is driving way more visits than Lovable. I have to think that a lot of that's being driven by their huge long tail of keywords.

**George Haikal:** 11,000.

**Rachel Hepworth:** Yeah. Which implies that they're doing something in SEO that works again, that could have started years ago. I'm just curious what it is. I recognize that a lot of those terms are probably very technical and we don't care about them, but it's more like, oh, what, what is generating all of that, regardless of what the term is?

**George Haikal:** So what I'll do is I'll break out all of these organic keywords, right, that competitors are ranking for and essentially stack rank them based on volume. And what we actually want to compete with as Lovable.

**Rachel Hepworth:** Yeah, it's actually less about the individual words and more about like, is this through. They have a huge template gallery or they have extensive blog or they did a glossary or like, you know, what is the. It feels like this. They probably have a strategy around it and not they just published a lot of random pages. So that's what I'm curious about. If you had to sum up, like, what are they doing generally to capture all these keywords? That would be interesting.

**George Haikal:** Sure, totally makes sense. And then. Cool. So let's come back to this for a second. So for the templates, I want to summarize at a high level. Basically what we set out to do was we don't want to just race to 15 templates and stitch everything together and then it not be a scalable engine that we can get to a thousand very easily. Right. Hit the long tail, hit the variations, get as much search volume as possible. So what we did, we had our AI engineer and our design engineer not only setting the quality bar with your team, but also building out the workflow that actually creates the templates.

And so what I want to show you quickly is a little bit under the hood on the how. So this is your workspace here. There's templates and there's two pipelines. There's the template generation, which actually builds the structure of the template in lovable itself, and the ID page content pipeline, which takes that template, that project in lovable, and creates the SEO optimized content that you see as the final product on lovable.dev templates.

What the team's done is they built up 21 different workflows, which you can just think of as steps within the pipeline. Everything from a project creator itself to a brief generator that basically the input is, you know, what do you want to build, the type of website it ties to the Personas that we agreed on for lovable, and you can pull in images as well. The main thing I want to show you is what we've done is we pull in the brief, the custom brief of what we want to build, create a project in lovable with it. And then what we do is we actually generate that template within Lovable.

And so what that looks like is. And then I'll show you the actual lovable chat. It basically is our design engineer plus our AI engineer operating as if they were talking back and forth. Lovable in an agentic workflow. And so what it does is it clones an existing project in Lovable. It then tells Lovable, hey, this is the project I want to create. Here's the plan. It goes back and forth on the criteria for the plan and building out steps. It analyzes the project to make sure it hits the quality that we need based on the spec that we create. It verifies that spec within Lovable as well and make sure the output that Lovable has generated up until this point meets that spec. It then executes again. It optimizes for page structure. Thereafter it validates. Are there any bugs in this project? Are all the pages working? A bunch of nuance to how a website actually runs and works. And then at the end we have this content curator that goes in as lovable of the media that's put in of the pictures and videos and whatever you've added to this template. Is there any room for improvement based on the Personas and the quality of the images? So we go ping Unsplash and Pexels to essentially improve the quality of the images. And then we do a final polish, right, and what that looks like. And again, this took weeks of setting up, but now what it looks like is an hour back and forth autonomously of essentially our agent going back and forth and literally building with Lovable to an insanely high quality bar.

You can see here, it's sharing the detailed spec. It's going back and forth. Great. It's answering now that it's saved in code because it can always refer back to it. Now go do these things actually implement the plan? It's an insanely long chat. I won't run through everything, but the final output is, you know, a one shot that just takes a little bit of polish from a high level design engineer. And we're there, which is pretty, pretty impressive. And so this is all the work that's gone on up until now under the hood. Again, pretty insane stuff. But I wanted to show you a little bit of the how because it's it looks relatively simple when you hit the landing page and you see beautiful templates, but a ton, a ton, a ton of crazy context engineering prompt engineering workflows being built was done.

**Rachel Hepworth:** Cool.

**George Haikal:** Let's jump to. We'll leave Sebastian's Project for the end. And we'll go through the reporting here. We set up your Looker dashboard. Megan helped set this up. Megan, do you want to run through this?

**Megan Dickey:** Yeah for sure. Yeah. So these.

**Rachel Hepworth:** Let's see.

**Megan Dickey:** So this is the one for guides. Yeah. So I set up two new views, one for the guides and then one for templates. And so for the guides, we're looking at clicks and impressions. And then if you kind of like scroll down over, you can actually like view each individual landing page and see the overall performance for that specific page. And then if you want to just look at it by week, then that's just right below you see guides performance by week. Compare the impressions, URL, clicks, CTR and then average position. And then we did the same thing for the templates. So basically it's obviously like early days for both of these things. And so there's not a ton of data that we're working with right now, but I think it'll be helpful as this engagement progresses, we'll be able to get a really good idea of what's working and how we can improve upon that.

**Rachel Hepworth:** And what are clicks? Like any click or is it a click on something specific?

**Megan Dickey:** Yeah so it's like it's a click to. So like if this shows up in like Google search, like it's. It's someone clicking on the page.

**Rachel Hepworth:** Oh, I see. Just visiting the page. Okay.

**Megan Dickey:** Yeah, exactly. Yeah.

**Rachel Hepworth:** Are you guys able to track anything beyond that or does that have to then come from our side?

**Megan Dickey:** Yeah it. So yeah, what we. So yeah, my limitation because like ideally we would love to be able to track like okay like sure there's a click but like then what is someone actually doing once they get to that page. And like that's where we're going to need a better integration with GA4. And yeah apologies. I'm still kind of getting up to speed on the account, but my understanding is that we don't currently have access to GA4, and I think that would. Having that set up on your end and then giving us access to that would be sort of the next step.

**Rachel Hepworth:** We've given you guys access or some people. I feel like we keep getting requests for more and more access and so I don't know but I'm pretty sure we only have I think the free version of GA4. We all have a paid version but I thought I had given access.

**Megan Dickey:** So.

**Rachel Hepworth:** I can look at that but I feel like somebody on the team has access to it.

**Megan Dickey:** Okay. Yeah. George, are you. Maybe you have some more context there.

**George Haikal:** Yeah let me confirm. Last I checked we didn't but let me go in and confirm. Do you know who I should reach out to? Rachel on your end it's almost always.

**Rachel Hepworth:** Igor because he handles security.

**George Haikal:** Fantastic.

**Rachel Hepworth:** But I think Elena might have also done it in the past. Just going to do a quick search. Yeah Elena said she added Megan. Yeah she said Elena said she added you.

**Megan Dickey:** Yeah. Okay well then yeah we'll get that pulled in. Yeah sorry I must have. Must have missed that.

**George Haikal:** No problem. Rachel you're on a thread with Elena now. Could you tell her to add my email as well?

**Rachel Hepworth:** Yeah she's on vacation so it's gonna take a while.

**Megan Dickey:** Okay great. Yeah I will then get that pulled in shortly.

**George Haikal:** Great then. So by next week we'll be able to tie all of that after the visit to here what's happening after and so we'll be able to paint the entire picture again. It's early days but it'll ask you a starting point for weekly reporting. Is there anything else that you'd want to see?

**Rachel Hepworth:** Rachel do we have the. Link to this dashboard?

**Megan Dickey:** Yeah like I see you guys linking to the image but the direct dashboard would be good.

**Rachel Hepworth:** Yeah like I see you guys linking to the image but the direct dashboard would be good. Oh looks like we do. Okay but I can reshare it. No worries.

**George Haikal:** Okay but I can reshare it. No worries.

**Rachel Hepworth:** Yeah that'd be great. I think ultimately what I, what I really want is to get the like actual sign up data as well. So this is a good start but we'll need we'll need to add that kind of additional data piece in here.

**George Haikal:** Definitely in the chat. Again thanks. No problem. And I can resend it in a recap in the Slack too so everybody has it.

**Rachel Hepworth:** Okay.

**George Haikal:** Amazing. Okay this all looks healthy. Unless there's anything else on the reporting side Rachel or what you want to see. I feel like we have our marching orders there. I want to talk through Sebastian's template idea and get your thoughts.

**Rachel Hepworth:** Okay sounds good.

**George Haikal:** Essentially and let me pull up the Slack here. I don't need the web version. Let me pull it on my screen from here. What Sebastian's asking for is on the main page similar to what V0 has including our templates right now as they are website templates but also moving forward apps tools etc. Into like Start building here section right under the actual prompt box on the main page similar to how V0 does it now. I went back and forth with him where does the prompt box and then you can literally start here but with a more organized streamlined template. Streamlined Template that's higher intent. So our focus as you know is websites and search volume. Lowest complexity lowest difficulty highest impact. Here this is now getting into if we're going to be right under the prompt box on the main page higher intent. And so we're happy to put the team towards building more specified templates but what I'm going to reach out to Sebastian about is we just need to know what the highest intent or priority of websites people are building with Lovable are. And then next tools internal tools SaaS dashboards whatever it is because that's what is going to make the highest impact going under the prompt box here. So that's the short of his ask where definitely the team's capable. I can scope it out and I can drive this with him. I just want it to run all of that by you and get your thoughts.

**Rachel Hepworth:** I mean what's the implication if you work on this with him? Like is the other stuff going to be slowed down?

**George Haikal:** No, no. The five guides per week and the five templates per week would not be slowed down. We could we would even just incorporate the templates we're building for the. Your main page into the ones that we publish.

**Rachel Hepworth:** Yeah yeah. I mean the ask makes sense. Megan Dickey So I don't. Rachel Hepworth CC and I are not concerned with the ask. If it doesn't derail you know the original purpose of what you guys are working on then there's no problem. I thought the issue is that making the apps was kind of hard for you guys.

**George Haikal:** It is. So what I'm going to talk to him about is starting with websites for now and then what the highest. What the basically the most built website list is for actual users in Lovable.

**Rachel Hepworth:** Or what is his ask just about what goes on the homepage? Or is there something. I thought he was asking you guys to like make the apps.

**George Haikal:** Eventually it will be the apps as well. But he's fine starting with the website that we've already built.

**Rachel Hepworth:** Can we fill a start from a template section?

**George Haikal:** Fine. To start with the website that we've already built. Right.

**Rachel Hepworth:** Oh yeah yeah yeah yeah. I think that's fine.

**George Haikal:** Now I'll connect with him on the community app showcase but essentially this will grow into apps and the other tools.

**Rachel Hepworth:** But yeah I mean we want them all to come from the same place and then they can be merchandised in specific areas because I assume with the templates gallery at some point you know we'll want to have a top templates or the best of the best is another organizing principle. We just don't really have enough time. That makes sense but. So those could eventually feed directly into the homepage. But for now we can just select some to put on the homepage. It's totally fine.

**George Haikal:** Amazing. So I'll keep you updated there and I'll drive that.

**Rachel Hepworth:** Okay.

**George Haikal:** Lastly Growth Hackers submitted that PR and now the how to page is finally redirect. Yeah good.

**Rachel Hepworth:** Is like are you guys in that channel? The Growth Hackers channel?

**George Haikal:** I'm in one separate from you all. Is it. Was it a lot of back and forth in the.

**Rachel Hepworth:** No I just like I'm not supposed to be. They were not an agency I was working with. Other people were. So I finally just had to go into the channel and say do this what's the issue? And then they did it. But like for some reason nobody was willing to like actually make that call. So we just did it. But like Anton did flag again that those how to pages were getting enormously more traffic than the pages that were doing. You know I've pointed out again that most of it was brand name traffic or like so you know traffic is not traffic. But that's part of why I want like the you know like sign up metrics because otherwise it's hard to you know you don't have any data arguing against that that the stuff we're doing is any better. But yes it's redirected now so should.

**George Haikal:** Be it also be interesting if I can retro the sign of data for the how to pages too?

**Rachel Hepworth:** Yeah I mean that'd be interesting. I'm sure. It's low. Like I can't imagine it being anything other than very very low.

**George Haikal:** And the final thing is streamlining the publishing for guides and templates. I shot a lot of integration to you. You said you passed to the CISO who approved it. Does that still sit with Ferkin? Is there any way I can I can push on that?

**Rachel Hepworth:** Yeah it should. Didn't I didn't I ping him in channel to get you?

**George Haikal:** I don't know. I don't know if he back channeled you or.

**Rachel Hepworth:** No no no. CC and I had a discussion with Firkin and Igor the security the CISO and he said let's do it. We're in a critical stage of growth. There's more to Ms. Blah blah blah. We could have a weekly security review of all PRs merged by GrowthX just to make sure it's legit which it would be with 99.9999% chance. So he. We have a whole Slack convo where he was like yes and Firkin is in that convo. So the path should be clear for you. And if it's not just let us know. But there shouldn't be an issue.

**George Haikal:** Okay. Amazing. I will let you know. Otherwise again a ton of work. Now we're finally in a spot with the templates but it's taking a lot less manual time. And it's relatively.

**Rachel Hepworth:** What would it take if we were to do 10 guides and 10 templates a week? Like how do we. How do we move faster? Like we removed the PR thing. Now.

**George Haikal:** Guides because we have our experts editors reviewing. They're both doable. Let me. Let me start with that. They're both doable. I would need to go in and scope out the time for another person on the guides.

**Rachel Hepworth:** Yeah.

**George Haikal:** And then the templates. When I get with my engineering team today to. There was one piece of this workflow that they were finalizing. I would know more but they're both very doable. Do you want me to get a scope on increasing?

**Rachel Hepworth:** Yeah let's. Let's figure out what it would mean to double it.

**George Haikal:** Okay fantastic. Do that. The answer is yes to both. And the foundations are super solid. The workflows for both are super solid and they'll work really great. Yeah I'll get you the numbers on that though. Required.

**Rachel Hepworth:** Amazing. Anything else Rachel at top of mind.

**George Haikal:** That's it for me.

**Rachel Hepworth:** Amazing. Rachel are we meeting next week or are you guys taking Thanksgiving off?

**George Haikal:** Let's see.

**Rachel Hepworth:** Yeah.

**Megan Dickey:** So yeah I am actually out of town next week but I'll still make sure that the. The Looker dashboard is updated with the GA4 integration before then.

**Rachel Hepworth:** Great.

**George Haikal:** What about you Rachel? Are you out or.

**Rachel Hepworth:** I mean I'm just in New Jersey with the in laws but I. I don't think it's a big deal if we cancel the meeting. I mean it's the day before Thanksgiving for most people so I assume many people are taking it off.

**George Haikal:** We'll skip this one and I can send over an update async.

**Rachel Hepworth:** That sounds good.

**George Haikal:** Works.

**Rachel Hepworth:** Yep.

**George Haikal:** Amazing.

**Rachel Hepworth:** Thanks guys.

**George Haikal:** Thanks Rick.

**Rachel Hepworth:** Thank you.

**Rachel Hepworth:** Bye.

**Megan Dickey:** By.
