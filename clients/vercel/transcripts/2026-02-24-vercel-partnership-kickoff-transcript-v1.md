# GrowthX <> Vercel — Partnership Kickoff
**Date:** February 24, 2026
**Duration:** 63 minutes
**Participants:** Marcel Santilli (GrowthX), George Haikal (GrowthX), Cody Henshaw (Vercel), Dan Fein (Vercel), Kristin Sauchak (Vercel), Eric Dodds (Vercel)
**Source:** Fyxer

---

## Summary

Official partnership kickoff between GrowthX and Vercel. The team aligned on growing non-branded organic traffic as the primary objective, with three immediate lanes: AI Gateway page optimization, populating the new /i content index, and models leaderboard improvements. Vercel is shifting its go-to-market toward agents and AI starting with a March preview and April launch, while front-end cloud remains the primary revenue driver. The group discussed content quality standards, pillar/cluster taxonomy for programmatic SEO, and competitive content opportunities. Access was confirmed for GSC and Amplitude. Next steps include introductions to Josh (AI Gateway) and Timothy (KB/DevX), competitive mapping from Kristin, and an AI Gateway prototype from GrowthX within two weeks.

## Key Takeaways

- **Primary Goal:** Grow non-branded organic traffic and capture broader Next.js and agent audiences. Most signups come from organic search, most revenue from self-serve pro upgrades.
- **GTM Shift:** Vercel is pivoting go-to-market messaging toward agents and AI starting March preview, April launch. Front-end cloud still drives the large majority of revenue.
- **Three Immediate Lanes:** AI Gateway page enrichment (team is eager for help), /i index pages (new content home, copy of blog structure), and models leaderboard optimization.
- **Content Quality Bar:** Vercel has an extremely high attention-to-detail standard. Dan's principle: "Ship early and often, but if you don't like it, don't ship it." Code snippets must be functional, OG images get multiple rounds, every detail matters.
- **Brand Positioning:** Vercel wants to be both "pre-cut pineapple" (accessible utility) and "Aman" (luxury hotel quality). Brand architecture will include both front-end cloud and AI/agent cloud.
- **Programmatic SEO Opportunity:** Massive untapped surface area. Pillar/cluster taxonomy, tag-based index pages, flat URL structures, and breadcrumbing for agents and crawlers. Vercel currently at 5,300 pages with potential for 40,000+.
- **Competitive Content Opening:** Historically averse to head-to-head competitive content, but Cody just published a Heroku comparison. Bottom-of-funnel competitive traffic is a gap where Vercel never shows up.
- **CMS and Access:** Contentful is the primary CMS for /i and site content. KB is managed by Timothy on DevX. AI Gateway pages live in the main "front" repo. Josh is the gateway contact. GSC and Amplitude access confirmed for both Vercel and V0.

## Action Items

**Cody:**
- Introduce GrowthX to Josh (AI Gateway contact) and add to Slack channel
- Verify GrowthX access to GSC and Amplitude for both Vercel and V0
- Track down analytics access for other Vercel properties (Next.js, AI SDK sites)

**Dan:**
- Confirm KB owner Timothy and clarify KB contribution/publishing process
- Explore CMS access for GrowthX to enable direct publishing on /i

**Kristin:**
- Share competitive mapping done with Chuck (after alignment with Cody and Dan)
- Share gold-standard content examples and load-bearing pieces used through comms channels

**Marcel / GrowthX:**
- Deliver AI Gateway/models prototype and taxonomy recommendations within two weeks
- Map pillar/cluster taxonomy strategy for /i and gateway content
- Begin competitive URL gap analysis and content opportunity mapping

---

## Transcript

### Introductions

**Cody Henshaw (00:08):** Hello. Hello.

**Marcel Santilli (00:10):** What's up, sir?

**George Haikal (00:10):** Cody, how's it going?

**Cody Henshaw (00:12):** Just crashing it. It's Tuesday. I didn't even know what day it was. Are y'all.

**Marcel Santilli (00:15):** I know,

**George Haikal (00:18):** They all blend together these days.

**Cody Henshaw (00:20):** I do

**George Haikal (00:22):** Good man. It's good to meet you. Heard great things.

**Cody Henshaw (00:24):** You too.

**George Haikal (00:29):** We got to get one of those huddle rooms, Marcel.

**Marcel Santilli (00:32):** I know. They're like six grand and they're so bulky, and I just feel like they're so expensive and they're so claustrophobic to be inside of them. I don't know. And then, like, keep. Have like a bad posture, you know, like sitting inside them. But yes, we kind of need it because it's easy to get. Get too loud in the office, but. What's going on, everyone? Hi, Kristen. Hi, Eric. How's it going?

**George Haikal (00:36):** They are so expensive. Yeah, yeah, yeah. Hey, hey.

**Eric Dodds (01:00):** Going great.

**Marcel Santilli (01:02):** Good to meet and see you all. Are we waiting on anyone else? Cody?

**Cody Henshaw (01:10):** Dan was supposed to join. Let me make sure that he still can.

**Marcel Santilli (01:14):** Cool.

**Kristin Sauchak (01:15):** Off right now on Slack,

**Cody Henshaw (01:17):** Yeah.

**Kristin Sauchak (01:18):** per usual. I was, too. If we're on.

**Cody Henshaw (01:32):** Oh he said invalid meeting. He must have tried to join my block.

**Marcel Santilli (01:37):** All good. I've been deploying an app in Vercel, and I was trying to get it the auth set up, but then I just gave up on Supabase. And remember that we use CLERK for everything else. So I'm trying to swap it out right now. I'm like, it'll be fitting for me to build and deploy an app, you know, right before this kickoff. Real quick, you know,

**Cody Henshaw (02:02):** Yeah yeah we like that.

**Eric Dodds (02:03):** I think we have a direct, we have like a direct integration with clerk though. If you go into the marketplace, you can just like wire it up.

**Marcel Santilli (02:07):** That's what I did. Yeah, it was just like, I forgot where. Not forgot. I knew we were using Clerk, but I'm like, well, that's for our actual product products. So then I was like, well, let me see. This would be a little bit easier right now.

**Eric Dodds (02:19):** Yeah, yeah. The Vercel thing is super easy.

**Marcel Santilli (02:22):** Yeah. Yeah, that's fun. Like, I've been doing some, like, proposals and. And also, like, mapping out, like, essentially like, end to end, like, here's your gap and things like that. So I. I built out this. This really cool.

**Eric Dodds (02:39):** Yeah.

**Marcel Santilli (02:41):** Well, I'll. I'll show you all later. But. But it's essentially like a mini app. Instead of buying a digital room, like a digital sales room, essentially like a custom app that I can take just like a. A full markdown and then like, turn it into a report that we can send, you know, people that are like, in the funnel, if you will. And then I just created a subdomain and cloudflare for us and then pointed Vercel there and that's it. That took like three seconds. So. So that was.

**Eric Dodds (02:51):** Vacation stuck between the hotel and the airport trying to get out. Yeah.

**Cody Henshaw (03:09):** Just have to get rid of Cloudflare.

**Marcel Santilli (03:12):** Yeah, yeah, I know. It's just that. That's just where our root domain is set up. So it's like. But I turn off the phone. Yeah,

**Cody Henshaw (03:18):** Yeah yeah yeah. I had to. I had to plug it.

**Kristin Sauchak (03:20):** Yeah, I was about to say I'm leaving.

**Cody Henshaw (03:24):** I think everybody is here. So we got, we got defined too.

**Marcel Santilli (03:27):** I know, but it'll be fun. I'm gonna prototype. We're gonna design and prototype everything in V0 for this engagement. So I'm excited. But with that, I'll kick it over to George just to do a quick intro, and then we'll kind of go around really quick if that sounds. Sounds good.

---

### Team Introductions

**George Haikal (03:45):** Yeah, sure we can go. Yeah. Good to see you, Dan. Good to see everybody. I'll go super quick but really excited to meet you all. Chief of staff here. So I try to help in all the important areas of the business, help Marcel out wherever I can. And my favorite part has been these strategy sprints. When I started, we didn't have this eight week accelerated onboarding process or just this process in general where we jump in, try to become experts on your business, make a ton of impact, add value as fast as possible. And now we put like say 40 plus clients through it. Learned from each rep along the way too. So super excited to jump in, get started and meet you all.

**Marcel Santilli (03:46):** Dan. Good to see you, man. Awesome. Well I'll go super quick and then I'll pass it over to you Cody, but CEO co founder here at Growth X. So you know I was CMO of Skill AI and so got to work with Ricky, Angie's brother for a little while. But anyways I was also fun fact, I hire my head of platform at Hashicorp, Joe Jeff and we adopted Next JS super early and I think we were a very early customer at Hashicorp of Vercel like one of the earlier, earlier customers. So we go way, way, way back. I remember hiring like writing a PRD of why we needed to re architect all our open source sites and everything to Next JS and having Mitchell and Armand the founders kind of like reviewing that and, and whatnot, you know. So so anyways been a lot of connections to, to the company so feel super honored to get to work with you all and, and, and yeah and so a quick TLDR on growth hacks if any of you don't, don't know. But started about 18 months ago. We bootstrapped at first. Now we're series A. We work with about 70 brands, you know like lovable ramp racks, large companies like Sentinel 1 and and then this team that's going to get to work with you all like essentially we also have under the hood like or behind the scenes if you will like forward deploy engineers like full stack AI engineers as well as design engineers and our strategist and just like editors as well behind the scenes every now and then they'll also interact and jump in there as needed. But just know we have almost 100 employees and 60 of those are forward deploy meaning they're folks that are would do work for you essentially. And so that's the tldr. But Cody, we can pass it over to you real quick.

**Cody Henshaw (06:20):** Yeah. So I guess I kicked off this, this project actually onboarded brought, brought Marcel over to Redis and they saw a lot of success with, with the team. So I'm stoked for them to help us grow our non branded engine and just our overall traffic engine. SEO, technical SEO and AO stuff. But yeah lead all things growth here focused on that stuff. We're going to popcorn it over to people. I popcorn it over to Kristen. She's next on my screen.

**Kristin Sauchak (06:49):** Great. Hi, I'm Kristen Salchuk. I lead comms here at Vercel, so I'll be an engaged listener mostly here. I focus a lot on driving branded search. So really excited to be focused on the other, other side of things. But please consider me a partner here if I can help you guys do your job better in any way. Here to help.

**Kristin Sauchak (07:15):** Oh, sorry. Popcorn Dodds. Next.

**Eric Dodds (07:18):** I'm Eric Dodds. Everyone calls me Dodds because my last name is shorter than my first name. So people start calling me Eric. I work on the content team here, so I really am sort of in a supporting role for all the people here and just generating content, reviewing content, et cetera. So I've been working very closely with Cody on aeo tracking a bunch of that sort of stuff and then also QA and editing a bunch of the content that we're publishing, you know, to drive top of funnel traffic. I've done a bunch of growth stuff in previous life. So you're super familiar with sort of all the, all the mechanisms, everything and so it's super fun to be contributing directly. And I'm excited to work with you to figure out how to automate some of the like brand standard voice and tone stuff as we go through cycles because that's still pretty manual right now. But I think we can go create a ton of velocity if we can sort of take some of our review cycles and just, and automate that, you know, with an agent and, and skills.

**Marcel Santilli (08:24):** That's, that's awesome.

**George Haikal (08:25):** Love that.

**Marcel Santilli (08:27):** Dan, you are famous man. In a good way. So excited.

**Dan Fein (08:31):** God, tell me more.

**Marcel Santilli (08:33):** No, no, I just heard from multiple people that you know, you, you, you, you know, you know what quality looks like and you know you've worked closely with G and others and so I'm excited to collaborate man.

**Cody Henshaw (08:35):** This is his favorite part.

**Dan Fein (08:45):** Yeah, so I'm. At times, the blocker is my role. No, we hold. What do I do? I. Right now, I just moved to, like, a new role for product narrative, so shifting from, like, pure product marketing to really focused on our storytelling. Part of that is focus on our blog, our change logs, our socials. And that's where I overlap with. With G quite a bit, is where we look at how we want to get our message out to the world. And then also with Kristen Dodson and Vibe Cody, one of the things I'm working on right now is trying to get everyone in Vercel to be like, a way better storyteller by trying to get them into an agent that can translate their words into something that's on brand, tone of voice, accurate, that kind of stuff. And so I'm really looking forward to working with you guys on that. And then the other thing is, we recently gave Vibe Cody's new little home slash I. And so we're looking forward to figuring out how we populate that

**Marcel Santilli (09:44):** I am pumped for that. I'm like going to go to town on that. Yeah,

**Dan Fein (09:46):** this whole. We need to decorate it now and we need to fill it. Yeah. So

---

### Kickoff Questions & Pressures

**Marcel Santilli (09:53):** I love it. We got a ton of examples we can go through later if we have time on like some of the stuff we've done for like augment code with that strategy which I like to call it like kind of like the you know, get people through the back doors, you know the site and then validate that the backdoors are good. And then over time, like pull that content in and other, other ways, you know. So, so super, super excited, but cool. George prepared some, some notes for us to do like a kickoff and go through some questions. But, um, I figure since speed is so important for Vercel, we're going to like move super fast, you know, and then we can kind of like double click and go a lot, a lot deeper into it. So. So I always like to think about like this first meeting as like, we don't know what we don't know. We only know what we think we know based on what's out there in the world, you know. And so this is kind of like give us the breadcrumbs and kind of point us in the right direction so we can go do the homework for you. Like, our goal is to take on as much work as possible from your plates, not add to your plates. But also like, there's times like, we just don't know things and then sometimes like we get to week six or seven and it's like, oh, we should have talked to so and so they would have told you why you shouldn't have done this or that. Right? Like, and those, those are kind of the things we're trying to figure out. But with that, George, I'll pass it over to you and we, we're just going to tag team here on, on the questions

**George Haikal (11:20):** Yeah, that sounds great, Marcel. Appreciate it. Only thing I'll there is, yeah, these questions are broad by design. Where we have some ideas from the sales process on areas we want to explore that might be fruitful. But definitely want to hear, you know, from you all your own voice, how you describe the company, the customer and like the pressures and goals that you're feeling. So that's the overall context of this conversation. With that, you know, what's, what's top of mind for you all in terms of the pressures you're feeling, what's really driving this engagement. Just help me understand a little bit more about, you know, the pressures that you're feeling here and, and, and you know, why you're excited about it.

---

### Non-Branded Traffic & GTM Shift

**Cody Henshaw (12:02):** Yeah. I mean I guess I kick off. I kind of alluded to it at the beginning. I think we're seeing especially in branded traffic we're seeing just this like hockey stick growth. If you look at non branded it's not. Not so much so people are hearing a lot about, about Vercel coming to the site signing up. People haven't. It's kind of still if you know, you know and we've got to capture all. All of the other. All of the other people out there. You know a lot of people run next. A lot of the Internet runs the next. Not all of them are on Vercell. A lot of people, building agents, a lot of them don't run on Vercel. We need to capture all of them.

**Marcel Santilli (12:38):** And, and when we say people too, like some. Sorry, I think I interrupted.

**Kristin Sauchak (12:42):** Oh, no, you're fine. Please go ahead.

**Marcel Santilli (12:45):** And when you say people, like, I always. I've used Vercel quite a bit over the years. Right. Like, so super familiar. I've also built a lot of sites in xjs and now with obviously agents and AI, like, how are we all like segmenting the population, if you will? Because now it's kind of like everybody that can't code can deploy, you know, Whereas before it was like more of like certain devs and whatnot. So we'd love to kind of hear a little bit more kind of how y' all are segmenting the buckets of potential population to go reach, you know?

**Kristin Sauchak (13:18):** Yeah, I mean, I feel like Dan probably has the best understanding of our icp, but I will give a blanket statement on top of that that I think one of the biggest pressures that we feel right now is we're really kind of turning our ship in a completely different direction in that we are well known as the front end cloud. We are the place where you can deploy a website. Front end is our game. It's still the large majority of our revenue, but we are going to market in. Talking almost exclusively now about agents and our AI and agenta capabilities. That will be even more so starting in April, really previewing in March. It's going to be all agents, all the time, but that's still a very small part of our install base and still very little of what we're known for. We've got our execs out there, like, really pounding the pavement with that story, but we still have a long way to go when it comes to, you know, the entire landscape of the Internet. So I think that's going to be just a huge focus for us over the years. I mean, over the year, hopefully not more than one year. But then, Dan, do you want to kind of walk through how we're thinking about ICPs? I don't want to.

**Dan Fein (14:34):** I hate to say that we're. We're almost not. It's just we're. We're moving so quickly that we're. I think the biggest pressure on us right now is pure. It's like, content quality while keeping quantity really high and. And then reaching everyone. But we're shipping so many things that you can't really even target any specific audience. I'm sure there's. There is a way to do it. It's just at our scale and our current sort of resource capacity, we. We kind of are struggling.

---

### Competitive Landscape & Product Surface Area

**Kristin Sauchak (15:04):** Yeah. So I'd give an example there that, like, this is kind of similar to the exercise we're going to be doing. I'm setting up tracking for our share of voice on social and earned. And it is the most taxing experience because I've got our V0 competitors, I've got our AI stack competitors. Underneath the AI stack. I've got our workflow competitors, our sandbox competitors, our gateway competitors. Then I've got Next js, then I've got kind of our traditional front end, and I want to keep an eye on all of them. But also it's. It's. It's kind of an insane and not even really useful exercise because it's so. It's such a Large group. So that's one thing to flag here because it, you know, obviously has a lot of overlap. Our competitive set as well as our ICP is like a real like, real like box of chocolates of like a real wide group of people because it's not only dev dev adjacent gen pop, but then it's also startups commercial all the way up to what we call Galactic Enterprise. So it's, we've got folks like kind of focused on all of those areas.

**Marcel Santilli (15:37):** Yeah, yeah, yeah. I think the. I always like to think about, like, how do we play to your advantages? And that's what we did with like Lovable, for example, where you, you have so much karma. And I like to call it karma versus authority because it's like, it's kind of like, you know, earn brand love links, all of the things like, let's just call it karma.

**Marcel Santilli (16:36):** You've earned infinite karma points, kind of like a few karma points and so, so it's like the. The. The. And that is directly proportional to how aggressive you can be on. On creating net new and surface areas on your site which then becomes the like to Dan's point like how do you build leverage so. So that like you maintain quality and. But you also kind of like scale like some of the things like we've been doing for instance like with Airby because they have so many connectors that are being updated all the time that's open source. We essentially set up like a cron job for a workflow agent workflow that anytime there's a change it listens for that change and then it updates their docs and then updates the landing page that are like the connectors landing page. So there's I think like lanes of that kind of stuff that hopefully like we can think through to where like those are like the clear ones versus trying to like replicate Jay's voice for his own blogs. Like, you know what I mean? Like that one is going to be like well okay, like good luck with that. Like you know that's going to. That's not going to be there. But there's like so much, so many other things that, that we can think about to where. But also like to the broader point which is like you. There's a lot of ankle biters and things that I think we can help you hopefully like suck the oxygen out of the room in all those different angles because there's no way they're going to have more authority than Vercel, like 99% of those competitors, you know.

---

### Untapped Potential & Shipping Velocity

**Dan Fein (18:03):** If you look at the untapped potential of our site, it's, like, enormous because we play in so many different areas with so many different products or what we call, like, primitives, like, things that we offer that if we just went into any single one of them that's like its own startup, its own company. Right. Like, Sandbox has, like, major companies that are like, I go to their website sometimes, like, oh, yeah. If we were able to dedicate that amount of time to this, like, to your point, on. On authority, it's like, I don't know. It just. It would be. We just push things out, and then we don't have the opportunity right now to follow them up with the drumbeat that would be required to, like, nail all the traffic that we'd want to get. So, like, today we released something called, like, Chat SDK. I would love to say that Tomorrow we had a plan and then Thursday we had a, you know, some other follow up to that plan and like there's going to be this drum beat. It's just we push and then we like move to the next thing which is a great thing because what it means is we cover tons of surface area. It's just when you have a small marketing team, like there's so much untapped potential in just taking any of those items and going long tail like is literally

**Kristin Sauchak (19:12):** My dream would be for us to choose three and like in, in a quarter it's like we're going all in on AI Gateway, we're going all in on workflows, we're going all in on Sandbox, I don't know, forever going to be the company that does that. But I kind of secretly want to do it and just see like, just like have a certain workflow where it's like we're going to do these three things. I call that out just for. Just to kind of give you a sense of our. Where we are.

**Dan Fein (19:39):** Some things naturally do that. Like next JS has its own site, its own community. AISDK has its own site, known community. It's like they have separate socials and they build their own. They have like devx and they have teams.

**Kristin Sauchak (19:42):** Yeah, yeah. I see them as like open source moons around cell planet kind of.

---

### HashiCorp Parallels & Revenue Breakdown

**Marcel Santilli (19:57):** Yeah. One thing that for whatever it's worth, like obviously Vercel has been wildly successful. So Hashicorp ended up having a great exit and then like having a worse exit later, you know, kind of thing. And so technically Vercel is better off than Hashicorp ever was. So take my here. But I remember having this conversation with Mitchell Hashimoto and being like we had 11 open source websites, you know, that had way more authority than hashimoto.com and I could not convince them to consolidate into that. And by the way, I'm not saying consolidate but one of the things I think we did tremendously well was like a shared top bar. It was like a global component. It's actually one of the reasons we moved to Next JS by the way was like these global components we implemented across all the sites and it just allowed like this kind of layer of like every single property had like really strong like I know where I am and I know how this relates to the broader ecosystem that is, let's call it Vercel ecosystem, you know. And so there's a lot of those triggers that I think will be able to like suggest that I like, essentially it's like, it's almost like cheating here. Right. Like in a lot of ways. But, but, but I would love to kind of understand a little bit more on revenue breakdown versus like, because I have a decent sense of where the puck is going, you know, like, like agents, models, like, things like that. But then we'd love to kind of understand like how to think about it like as far as like revenue breakdown because that can, can influence almost like our portfolio strategy where, where we put the bets down, you know, a little bit of like where the revenue is concentrated today, you know.

**Kristin Sauchak (21:36):** I think we probably need to get fresh data from Martin's team because I have not seen the like the line by line percentages. I just know back of envelope math. The large majority is still front end cloud workloads. Um, so mine's just anecdotal. I don't know Cody, Dan, Dodds, if you guys have seen breakdowns, but we could certainly grab it.

**Eric Dodds (22:02):** Haven't. I have not looked at the data recently. But one thing to add which this is. I'm so sorry for the, the wet blanket that's about to wrap around you, Dan, from a product narrative standpoint. But one other thing that I think because we ship so many new things, especially related to AI so quickly. There's, there's like, there's hundreds of millions of dollars out there I think for like boring stuff like WordPress sites, moving off of WordPress to next JS and Vercel and other things like that that is not like public. We don't, you know, that's not the narrative that we want to lead with. But when we think about long tail content, there's a lot of boring stuff that is, that will be extremely lucrative. And so I kind of think about those as, you know, Marcel, to your point, that's not the karma that we want to put out into the universe, but it's absolutely like an inbound funnel that we want to build.

---

### Brand Architecture — Pre-Cut Pineapple Meets Aman

**Kristin Sauchak (23:07):** Yeah. I think you're always going to. This will be I think probably like a defining foundational element of this account in that we're redoing the brand strategy right now. And one thing is that we're definitely in the brand architecture going to have front end cloud and AI or agent cloud. We had thought about moving away from front end cloud, but that was insane because of the aforementioned revenue and the agency that's working on the brand strategy. They talk to all these people about like what, what they. What you would say Vercel is, you know, if it was a thing and it came down to the two best ones were pre cut pineapple and the brand Aman, which is like the highest end hotel chain. Right. And Pre cut Pineapple was perfect. Right. Like you can buy a pineapple but we make it easier. We may get like, you know, blah, blah, Blah. So there's the utility and then there's the luxury. And G really, like, he really honed in on that. And he wants us to like, build a brand that is both aman, the most high end luxury hotel brand, but also pre cut Pineapple. And so I think from a content perspective, Dodds, you hit the nail on the head. Like, we're gonna have to do pre cut pineapple and luxury hotels at the same time, which is tough, but I know we can do it.

**Marcel Santilli (24:46):** Yeah. Like Alex Wang from Scale used to refer to it as like. Oh gosh, what's the terminology? It was essentially like luxury engineering brands. It wasn't luxury. It was, it was like something else. But essentially like how like most developers are willing to pay what they know is going to be a premium for using Stripe because it's. But it's super accessible. That doesn't mean it's like, but, but it just feels like, you know, it's kind of like an Apple Products type of type of thing. So.

**Kristin Sauchak (25:13):** Yeah. 100. Apple's really the only. The brand, the standard bearer for that. Yeah,

---

### Outcomes, Funnels & Conversion Metrics

**Marcel Santilli (25:15):** Yeah, but, but like it's accessible and, and I guess like maybe to just try to get a little bit more like specific here. Are there specific vercel.com funnels that are, you know, the bread and butter driving a lot of signups and revenue? Or how should we even like the outputs that we care about? Right, like, or the outcomes we care about. I kind of think of it as like my mental model is always like like inputs, work, outputs, outcomes. And the outcomes are ultimately like, you know, there's the lagging ones, which is revenue essentially. Right. And usage. There's like. And then there's like leading ones that are just kind of like visibility visits, signups and like, you know, sales leads, things like that. Right. That then eventually lead to revenue. And then the outputs are pretty much when, when it's related to your site and building. This is like pages and pages are made out of, you know, content, assets and code, you know, and then there's all the inputs and the work that have to happen between, you know, agents and humans to, to drive those outputs and figure out which outputs correlate to the best outcomes that matter. So all that to say like, what are there lanes today on vercel.com that are like this is working. Like we wish we could do more of this outside of I know Vercel. I go to vercel.com and I just sign up, you know, AKA branded.

**Cody Henshaw (26:48):** I mean the majority lineups come from just organic search and the majority of the revenue comes from self serve signups and on upgrades to pro. I don't have the breakdown of like what pages they come. I mean I don't think there are like almost all the signups just show that they come from the homepage.

**Marcel Santilli (27:10):** Yeah. Okay.

**Cody Henshaw (27:14):** But like in terms of like revenue breakdown like the majority of it's coming from the pro business. And to like Dodd's point, everybody's point here like the, the front end cloud is the thing that's printing the money. The AI side just not driving a ton of revenue right now.

**Marcel Santilli (27:29):** Yeah. Yeah, okay. Well, I guess I'm the exception because they keep getting us to pay a hundred dollars more, so.

**Cody Henshaw (27:37):** Are you using AI Gateway? Yeah. Yeah. And I think they're. They're

**Marcel Santilli (27:40):** No, no, I'm joking. Just for V0. I'm totally joking. I've just been using it amount this week.

**Cody Henshaw (27:44):** so. And then. But, but that's a Good point. Like V0 is kind of a different separate thing. It's Kind of a separate entity. Like we don't even track signups together with V0. So it's like probably just an important side note.

---

### Competitive Mapping & Next Steps

**Marcel Santilli (27:55):** Yeah, yeah, yeah, that makes, that makes sense. Like. Okay, so maybe what we could do as a follow up is Kristen, I think we can do most of that mapping, but if you've already done some of the mapping as far as like you mentioned, like hey, over here, it's like there's the next JS competitors, there's the V0 competitors, there's the like this Inbox competitor. Like we'll do that as well. But it'll be good to just like make sure we're not missing any, any angles. We've already done a ton of work on, on kind of like mapping everything out as far as like we scraped through all your docs, like like the entire like kind of ecosystem. But it's always good to, to kind of understand a little bit of like how you all see the, the category especially like in and deals, you know, and then we can can kind of like approach that from, from those perspectives if, if that's helpful.

**Kristin Sauchak (28:17):** yeah, yeah, yeah. Happy to. I have to jump at the half hour for another call, but Cody, Dan, I. The competitive mapping I did with Chuck, but I'll run it by you guys to make sure that you're aligned and then I'll share it. Great to meet you guys. Yeah, yeah, please.

**Marcel Santilli (28:55):** Cool. Okay. And then Kristen, super one, one quick thing. If there's anything that you see as the gold standard from your perspective as far as like content voice or whether it's Vercel or created or not would be really, really helpful to always like keep that in mind. So anything you want to send our ways of just like that we can use this reference from what you think is great, you know, be super helpful as well, you know.

**Kristin Sauchak (29:27):** Oh, definitely. Yeah. The. The guys here will. Will definitely have a strong POV there, but I can definitely share with you, like, the. The load bearing pieces of content that we use through my channels.

**Marcel Santilli (29:37):** Okay. Perfect.

**Kristin Sauchak (29:38):** Okay, cool. Thanks. Good to see you guys.

---

### ICP, Messaging & Content Quality

**Marcel Santilli (29:39):** Yeah. Yeah, absolutely. Okay. So maybe we can. I think on the icp, what it sounds like is there's some new messaging coming out next month. It sounds like. Right. Or refresh messaging or brand positioning. And then as far as like kind of the icp, it's kind of like, hey look, let's just take it sounds like let's take a little bit more of like a tactical approach of like we're just. There's so much surface area. Let's just go do the basics, you know, let's worry slightly less about the true icp. And as we dig in we might ask questions around like specific use cases. A lot of, a lot of it. I think we can, we can figure out on our own. But if there's anything there, Dan, especially from. From your angle, that, that you want to point us in the right direction there, that would be super, super helpful, you know, especially on like, what great looks like for the universe of this audience, right? Outside of what's already published on Vercel.

**Dan Fein (30:43):** totally. I think what George has added like worry less about the true ICP for now is like core to. It's like a key unlock. It'll slow us down if. Unless we like, like we'll introduce that new messaging next month whenever it is. But that'll be like 1% of the content that I'm sure you guys will end up creating. Right? It's just like you guys I feel like should let open the floodgates and feel

**Dan Fein (31:11):** like you don't even have to like map to that probably. It's just so like it probably won't even change much of what you guys are going to work on to be honest. It's much higher level, I think.

**Marcel Santilli (31:19):** Yeah. And. And I guess, like, maybe we can switch gears then and talk a little bit more about like, how, Dan, for you, you think about quality because you seem to have spent a lot of time already. And just for me to understand kind of how content is working today or anything that you've been involved, I know Eric had to drop, but anything from your end, as we start to, we'll go through a process of calibrating, but will be awesome to understand what's your gold standard or what you consider amazing so that we can start to like, reverse engineer that a little bit on our end.

**Dan Fein (32:01):** Yeah, it's a great question. I think there are a few things that like come up in my mind. Like recently in Slack, like someone said sorry for being pedantic and both my and G's response was like this is the place to be pedantic. And then the other. I'm trying to think of what it was. It was. I can't. I can't think of the example. But it's basically our attention to detail is to an extreme. That means our bar for quality before something goes out. Like on our blog, Changelogger social is like annoyingly high. It's like if you put a code snippet in a changelog and it's missing one variable import and the code is not workable. Like that's a terrible release. Um, so. So it's the attention to detail at like every like the OG image gets multiple rounds. The. The exact social copy, the actual change log, the all. All of it. Right. And so that's not in my mind a bad thing at all. I actually like that. I think that that's the coolest thing. So what I said to the team recently was, I think there are two principles that we sort of have here, and I think I mentioned earlier, one is ship early and often. Right. So quickly, keep the speed up, but if you don't like it, don't ship it. Right. And so finding that balance, that I think is actually the job. It's like, how do you do both? How do you make sure that you're getting so much out the door that you can keep up with everything that's

**Dan Fein (33:31):** created? And then how do you make sure that you're not just putting slop out into the world? And I think that's even more important now with, like, AI creating so many things. It's like, yeah, we can put out a ton, but we still want someone to land on our site, read it, and feel like, okay, this is actually, like, a interesting company, or they have, like, an interesting perspective, or they're opinionated, or they're doing it, like, at a high quality, or their first thought isn't, this is just AI slob. Right. And so it's like volume meets quality is. And then at the same time.

---

### Content Approaches & Case Studies

**Marcel Santilli (33:36):** yeah, yeah. And like, where my mind goes here is kind of like two things because I struggle with this at a Hashicorp as well. When we were doing this paper, it was like the cloud operating model paper. And I remember it took us like three, four months to.

**Marcel Santilli (34:23):** To like get the shit out life. And then I was like, okay, there's just absolutely no way I'll be able to do this. And so I switched to doing whiteboarding videos with the founders and then like transcribing that and just translating that like, very well and same thing. It's like taking content that the community already created and just like translating that in a way that was like more like almost like reporting on it and curating it. And then outside of that, like the other approaches, like. And I can. Let me share my screen really quickly here as well, just to kind of like riff a little bit is like. There are times when, for example, for Sentinel One, it was like a nightmare to get approval on some of the other content. It was really hard. And that's okay. But then we created this vulnerability database, right? And it's doing like insanely well. And I think this would probably require a couple more rounds of improvements on this, right? But this is still insane improvement on shit like this. Like, you know. You know what I mean?

**Marcel Santilli (35:30):** The quality of life improvement still. And. And then like, because like, Vercel is Vercel, if you do something like this on a site like Vercel, it's kind of like it's going to be kind of crazy up to the right, right? Like, another example of this is like with Augment code on the mcp library. So I think there's these pockets we can find, right? Like where it's like again this could be improved as well, but there's things I think that we could do where it will be a little bit better or another one that we did was like this is just a fun quick app we vibe coded a while back and we've done nothing since. Right? But the thing of this is like cursor rules, you know, and, and you know like, and, and there's a whole workflow that generates it. So like you can come here and essentially like give it like, you know, like, I don't know, like a shed CN next JS with whatever your stack is, you know, and then it triggers kind of like a, a workflow and you can have like leaderboards on things. Like. But the point is like some of these things, hopefully the bar can still be high, but it won't be like trying to pretend to be written by G, you know,

**Dan Fein (36:50):** Yeah,

**Marcel Santilli (36:52):** and, and I think there's a lot of things and, and for me like what I've seen that the biggest one is like, it's like hey, if I search for Claude Opus pricing, right? It's like anytime I see like Reddit coming up at the top or like Code Academy or these sites, I'm like, there's like we shouldn't be here, right? Like, and this is just a quick few shot prototype really quickly, right? Like, but, but it's like, hey, should we like, is there a way for us to like reposition some of the experiences you have and then enrich the, the crap out of it? You know, I, I don't know, I just wanted to kind of get our juices flowing a little bit here because it's almost like there can be like a paralysis when you have too many opportun. Too much opportunity to, you know.

---

### AI Gateway & Models Pages

**Cody Henshaw (37:41):** Yeah. And I think you'll see that with every one of our competitors. I think like, historically we've been pretty averse to competitive content. Like head to head competitive content. I just published one that was the Heroku comparison and I think like we just have to be tactful how we do that.

**Cody Henshaw (40:30):** It's not like a, you know, they suck but like this is. Yeah. Like I think this is a good piece of content. Relatively good piece of content. And it is, you know, it doesn't say we're best for. They're best for everything but for some things.

**Cody Henshaw (40:44):** And I think that goes a long way with our audiences.

**Marcel Santilli (40:49):** Yeah. So have you all done it looks like you've done in the looking. Okay. It looks there's like a KB guide here and so,

**Dan Fein (41:03):** KB is very new. It used to be resources or guides and they moved it all over to KB to kind of give more room to. Not like not everything's a guide. So like now the netlify comparison pages have a nicer little home. So KB is also kind of new for us. Yeah,

**Marcel Santilli (41:23):** And what is the process? Like?

**Cody Henshaw (41:24):** I don't know if KB is an opportunity. Yeah. What's the process for pushing stuff there?

**Marcel Santilli (41:31):** Yeah, like how does it work? Like who reviews? Yeah, because there's 322 pages there already. Right. Like so. Yeah.

**Dan Fein (41:33):** yeah, that's. That is not. Yeah, that is a different. So that's Timothy on the Dev X team. So like he. I think they own that and they contribute to that and so like I don't know the process. I don't think it's as high of a bar that to like get on there as it is to like get on the blog. So it doesn't like need to meet. Yeah, it doesn't need to meet the. Is it as educational, as informative as, I don't know, forward looking, whatever angle you go as

**Dan Fein (42:13):** something that might go on the blog. So it's. It should be easier.

**Cody Henshaw (42:16):** Yeah, I think we should definitely look at the competitive stuff, comparison stuff and publishing a lot of that pretty early. Like we know that we're losing there and if you look at some of the real bottom of funnel traffic, it's competitive and we are never the ones who show up.

**Cody Henshaw (42:30):** So I think that's important. And then on the AI gateway side, like that seems to be some. Like it's got a high bar but it also, the team is very open to making changes. Like that's not in the main cms and they also have a really good relationship with all of the model providers. So we know pretty far in advance when Kimmy was launching the latest model, like we knew way in advance and we published it into the models leaderboard or models page minutes after they made their blog post. And then we had our dynamic page. But those pages just aren't optimized. And that team is. Is really begging for help for. For optimizing that content

**Marcel Santilli (43:08):** For the KB stuff you're saying.

**Cody Henshaw (43:10):** For the AI gateway. Those pages. Yeah,

---

### Pillar/Cluster Taxonomy & Site Architecture

**Marcel Santilli (43:13):** Yeah, yeah, that one I think it's like the, the no brainer one. We love to just like get started immediately like and, and like prototype some things and, and kind of like run it by your team. Obviously. Like your, your design and dev team can implement it. They can also like give us the standards for us to, to implement it either way. But, but I think we can at least like help with the prototyping and kind of how to think about it. One of the, the things that I just want to kind of like point out that is going to be really important. So this is just our internal handbook. But I was just so like more and more like one of the things that matter a lot is kind of like almost thinking of like your website and all these pages as a knowledge graph and kind of how are you thinking about pillars and clusters and in groups, you know, and how they all correlate. And the stronger the like and more semantically relevant that web is, the better, you know, and you can keep the pages pretty flat. But you need to have like ways to like tell agents and also tell like crawlers, like how things correlate. Right. It's kind of like they're not going to ingest 100% of your site and know how page 10,051 correlates to page 327. Right. Like there's just like no way even with a little bit of cross linking. And so like when I, when I see kind of things like this, which is like super flat and there's very little breadcrumbing right. Like that happens on, on some of these where it's just like hey, where in this universe there's 322, soon there will be 3,000 of these. Like what, what group do they belong to or subgroup that they, they kind of belong to? Right. To give like an example here, this is like a non tech example but just makes it easier to understand. Like helpline, right? Like they have for example like conditions, they have wellness and then inside of those they have like treatments. So now there's like cancer care, slash treatment, right? Like so you can clearly see like and then there's like topics that are shown in these index pages that are actually like not this one is in slash health, slash cancer, this one right here. But it's still showing up in slash cancer care, slash treatment, right. So it's almost like you're setting like this universe of like pillars which is like health conditions, wellness tools and things like that as well as like clusters as holding groups, you know. And so a lot of that strategy, I think it's going to be really, really important and as well as like trying to help you all a little bit on like some of these things because like there's a lot of low hanging fruit here of just like, you know, it's pretty easy to kind of see, you know, that, that can give that boost. But maybe we focus first on the gateway and developing I and setting a strategy but then pretty quickly like hopefully giving some guidance to the rest of like hey, cross navigation, like how to organize the content, you know, some best practices as well as to make sure we're not cannibalizing each other, you know, across the site, you know.

**Dan Fein (46:20):** yeah. That makes a lot of sense. So is it is the best way to like make categories or. And just have like a set path on. Okay, we need to fill the. We have these categories and now we need to go fill them and then naturally things.

**Marcel Santilli (46:33):** Yeah, the way I kind of think about it is just like you would organize your local repo for an agent, right? You almost have your Claude MD that is 60 lines long and then you have a readme in every directory and then in every directory you kind of index and give this one liner explanation where things are and why they're there. And then you just do progressive disclosures along the way and it's kind of like you kind of have to do that with your entire website, you know. So if you think of your website as a local file with a bunch of MD files, you know, like how would you organize that and how would you then have an agent that doesn't need to crawl like 100% of every single file, every single run in order to know what's in there that has just enough breadcrumbing and you know, and you're organizing. But also like if you're human and you like open a directory in your, in your, you know, local, you know, cursor or VS code and it's like 10,000 files all in one directory all over the place with bad naming conventions and none of it makes sense and bad metadata, then it's also not going to make a lot of sense. So that's kind of how I think about it. And the more agents being a first class audience on your websites, the more that's going to be necessary to be super clean and super ocd about how you organize and correlate the content. And so once you start crossing into the thousands of pages, having these like dynamic tags almost. Right. Like so easy way to think about it is like if you look at the traffic for wix, which we study a lot for lovable, like a lot of their traffic is to index pages or even a better example here would be like a lot of the, the traffic to let's say like TripAdvisor is actually like, like best hotels for families in Paris, for example. Right. Like this page that's going to show up in whatever the organic one. These are all like index pages, right. They're not individual like a page, they're like an index. They're, they're essentially like a, a PLP essentially, you know, instead of a pdp, you know. And so it's all about like, it's just a set of variables and filters, you know, that becomes crawlable.

---

### Programmatic SEO & Scale

**Dan Fein (49:25):** I was asking, I was asking Cody like I said that I've seen a hex code site map once that was like I don't know however million 36 million links long and it's just like every combination of hex code just to see if they can, if they can to rank for like the most odd ones. And so yeah, I'd love to go like the variable route where we can just like assemble a page because we have all the content and at runtime it either like it creates and it'll be, you know, figure out how to make sure it's fast but it's not like pre computed and so we could just have like infinite side.

**Marcel Santilli (49:44):** Yeah. And we can maybe set some, like give you all some instructions for the other areas of the site. So just like some best practices, you know. But I always like to use this one as my holy grail of like what's possible. It's canva. Com. 280 million visitors a month, all organic. That's over $800 million of worth of traffic every month. They've been profitable for 10 years on a five to $10 a month subscription, you know, and, but, but so I've studied a lot of like these, the patterns there, you know, kind of like how they organize their stuff as well, you know, by use case by, by topics, by features and you know, and, and at the end of the day it's just like, it's just a way to kind of like organize it, you know.

**Cody Henshaw (50:25):** And that. That to me, Dan, correct me if I'm wrong, but that feels like the stuff that's easy for us to make. Those types of asks like the re. Architecting things based on that. Like we're not touching design, we're not touching actual content. So the team seem to be pretty open to doing that.

**Dan Fein (50:42):** What was the. What would be the actual ask you mean?

**Cody Henshaw (50:45):** Whatever. Re. Categorizing. Re.

**Dan Fein (50:47):** Oh yeah,

**Cody Henshaw (50:49):** Yeah, reconfiguring the way that domains work. As long as redirects and everything else are set up right. Like, I don't if we have a strong business case to do it, I don't think we're going to see a lot of pushback on that.

**Dan Fein (50:55):** yeah. I hope so.

**Marcel Santilli (50:59):** Yeah. And it's, it's also like just kind of having, think of it as just like one MD file that is just like spelling out what's what in the site in one liner that an agent could understand. Like, like if you want an agent to ingest every page on vercel.com for your own internal agents. Right. Like you just need to explain what's what and why it exists a little bit, you know, and then if we have that and we align internally on that and we have to also define that for Gateway for the Slasher I and everything else, then, like, it'll be really clear like, where we can go kind of go do that. And then you all already do this pretty well, but as long as you keep the landing pages themselves, like, pretty flat structure, then everything else just becomes like index pages. Right. And they can be like essentially like aggregators with the grid and a filter kind of. Right. Like, and then you can pull those pages into any other section of the site. You don't need to move the URL structure of that. And then for massive, like, sites that like what I think Vercel should become, you know, then it's like super, super manageable. Right. Like, And I think Canva's the example. Like 44,000 pages. I don't know. I think Vercel should easily be there in 10x like traffic. Right now you're 5,300 pages. I'm not saying we'll create 40,000 pages for you in one year, but I think it's the level of potential you have

**Marcel Santilli (52:26):** that could be kind of interesting. You have slush font. What the hell? Have slash everything. It's like you can go compete with every font in the planet and go create like a page for. For every freaking font. Like, there's just so much, you know, the like, surface area. And so I think, like, the more it's kind of like a trade off, the more we can like, focus on things that have that kind skill and testing it out. And the last we're like stuck in the like, like, right. Intended thought leadership piece. That sounds like G. I think the more we'll be able to kind of build leverage and build trust and show results and then like, focus on the things that are going to be like, a little bit more complex to get approval, you know, what is. I don't know, what do you all think about kind of like that approach?

**Cody Henshaw (53:20):** It sounds right to me.

---

### Defining Success — First Four Weeks

**Marcel Santilli (53:22):** All right, so sorry to kind of diverge us a little bit. I just feel like there's a lot of stuff that will organize our thoughts better this week. But how do we think about how to knock this out of the park? Like, what, you know, like the next four to six weeks. Like, how can we show. Build trust and then obviously, like, long, long term, continue to kind of earn the engagement. Like maybe Dan, starting with you, since Cody and I had talked a lot as well, but maybe love to kind of hear from your own words.

**Dan Fein (53:52):** Yeah. So I love the idea of figuring out I don't know the super, super scalable stuff because we do the opposite, right? We do the very not scalable stuff. And so I'd love to figure out a cool workflow that lets us. I don't know. When Cody gave me his initial like multiple thousand pages by the end of the year I was like oh my God. And then a week later he was like, he gave me Another version of that, which was like, double. And I was like, oh, my God again. And then I was like, oh, actually it's achievable if you just unlock. I don't know what we've been afraid to unlock, which is publishing things that don't go through 19,000 reviews. And so I would love to just figure out that workflow and then type in every keyword that we could ever think of and figure out how we make it all work.

**Dan Fein (54:49):** So, like, success to me is just getting. Probably getting to 1% of Cody's target. Right. And I know Cody's success is 100%, but for me it's like, okay, that'd be amazing.

**Marcel Santilli (55:01):** yeah, that makes. That makes sense. Cody, what what about for you? Like, how do we think about the next, especially the next four weeks, like how to like really like knock it out of the park. Like start, you know, the right way here.

**Cody Henshaw (55:16):** Yeah. I mean, I think one way is with. With content volume, but I think like everything for me is gonna come down to sessions and how those are converting into signups. Right. I think if we have. I think we have a good surface area with the models page, if we can get some wins there. Like, that is our first version of something that is fairly programmatic SEO type of like mass scale. Like, if we. We have a baseline, it gets decent traffic today. There's a great product there. If we can focus on that, you know, we've got the baseline. Let's see where we can get that traffic to. I know a month is not a long time inflection there, but at least let's. Let's see a growth from the baseline that's not fully dependent on a new model release. I think that starts to look successful and proves that this type of scalable model works. And then we just go hard in some of these other areas, like the. I mean, I want to publish a lot of pieces on the I page, obviously, because I have that available to us now. But yeah, I mean,

---

### /i Page Structure & URL Best Practices

**Marcel Santilli (55:36):** Yeah. Okay. Did you have the design done for, for that already or is that something you need help? Yeah,

**Cody Henshaw (56:18):** For the iPages, it's just a copy paste of the blog,

**Marcel Santilli (56:23):** Got it. Okay.

**Cody Henshaw (56:24):** So it's literally blog pages right now. I think they're putting the link in the footer right now and in like an index page for the index pages that also replicates what the blog looks like.

**Marcel Santilli (56:26):** Okay, cool. Okay, perfect. That by the way, if you're going on that like direction one, like very important but common mistake is like on the tags and the index pages don't use like slash, category, slash, whatever the tag is because it's just like unnecessary like complexity on, on the site. So like the more you can keep that structure flat. But, but, but we can, we can, we can help with this. So, so it's.

**Cody Henshaw (57:10):** The one that we just was the

**Marcel Santilli (57:13):** Since you're duplicating the blog, I think this, it's a mistake to do slash blog, slash category, slash community. Because category is just a dead directory. You know, it's like, yeah,

**Dan Fein (57:19):** Yeah. I was thinking I posed this this week. Like, what is the best way to categorize, like, our changelog has nothing to do with our blog, but it looks like right here it's actually a category of our blog blog.

**Dan Fein (57:34):** Like, if you click it, it's like totally different.

**Marcel Santilli (57:36):** yeah, yeah. Like, but it's a good experience because it doesn't like, look like you, you went to a different universe and you can't come back, right? Like so, so that, that's okay. But, but imagine like inside of here. Imagine if you have 3,000 articles, right? Like, this would be a bad experience. So, so then you need to think about like each one of these things is just a tag and you can compound tags essentially, right? It's a way to kind of think about it. And so it's just like TripAdvisor, right? Like, or if you go to like WIX templates, right? And it's another example here. And you go like, like industrial and service. Like you can see like it's just tags, right? And these just like filter down things further. But all of these are super indexable things. And that's for when you go like super, super scale, right? Like not. But we're not talking dozens here or even a couple hundreds. It's like really when you're going in the thousands. But that sounds good on the index. Quick things before we wrap up one, who can we work with to get our engineers some access to repo? Just that we can start to understand at least for the I and the slash gateway and also someone on the/AI gateway to start to understand like, like what we can work with as far as like information, like plug into some kind of database that has that information or just do a deep dive, you know, on the technical side.

---

### Access, CMS & Technical Setup

**Cody Henshaw (59:11):** Dan, you might be better on the CMS stuff. Yeah.

**Dan Fein (59:14):** Flash I is just our contentful. It's just our CMS

**Marcel Santilli (59:18):** Okay.

**Dan Fein (59:19):** and then. But/AI/ Gateway. I don't know how it's architected. I think it's in our main repo, which actually it's called front, and it actually has our dashboard too. So I'm sure there's a way to give you some visibility into it. I don't know to the extent that that's super possible, but I can check with. I. I think his name is. Or I think. I know. I think the person who is running that. His name is Josh. He would probably be a great person for you guys to partner up with because he's thinking a lot about AI Gateway leaderboards and model pages and all the stuff that. So I think he'd be a good contact for you. Let me see.

**Marcel Santilli (59:36):** Okay. Yeah.

**Marcel Santilli (60:00):** Okay. So we'd love to, if one of you can facilitate introduction or just add to our Slack channel, we can Take it from there and we can go do the deep dive. Normally along the way, you all might be different. It's helpful for our design engineers and engineers to just have like, at least one person have access to be able to make like, small changes on whether this like slash I or. But I also understand, like with Lovable, for example, that actually require us to have access to their main repo, you know, and so. But we're very used to that, you know, and so if there is a way, then normally that means we'll be able to move a lot faster versus but if also you tell us like, no F off, you're never going to see anything. You're just going to have to tell us what to do. That's fine. Just know that like. Well, my.

**Dan Fein (60:53):** Yeah,

**Dan Fein (60:54):** it's really up to, like, I don't mind. It's just so, like, we'll just fight it about like, Cody, I'm sure could make the argument and then figure it out. So we'll try to get you as much access as you need.

**Dan Fein (61:06):** Anything that's in our CMS is on our website. So it doesn't. Like, that seems easy.

**Marcel Santilli (61:10):** Yeah, yeah. It's just mostly like for us to figure out how to build workflows, AKA like agents that run on a cron job to push that information somewhere and that information shows up in your website will have to integrate with something. Yeah,

**Dan Fein (61:17):** Oh, no, totally. Yeah. Yeah. All I was saying was like, it's not like just confidential info and receive it. Like, I feel that's an easier one than front, our repo. So let's figure out how. What you need and then how to get you that. And if we can't get you that, then Maybe there's a workflow. You guys push somewhere and we pull and we generate a page based off of it. I don't know.

---

### Analytics Access & Wrap-Up

**Marcel Santilli (61:27):** yeah. Okay. Okay, that sounds. That sounds good. And then the last thing Cody, I can sync with you is just mostly just if we haven't already, just getting access to any and all analytics that you're already looking at and gse, but I think you already kind of started on.

**Cody Henshaw (61:55):** Yeah, I added you. I added you to anywhere that we had. And then. Yeah, yeah. So you should have amplitude GSC for both V0 and Vercel. That's basically all we use.

**Marcel Santilli (62:01):** Cool. Okay. Okay. All the other sites, do you have anything instrumented? It's okay if that. We cross that bridge later as well.

**Cody Henshaw (62:10):** Let me know if you can access any of this. We do in some cases. I don't know exactly how all of those work. I don't have access to them yet, but I will try to track those down as the next step. And then I already have a thread open with Josh about like the technical SEO stuff and improvements there. So I'll add. I'll just give him some context and add them to this channel.

**Marcel Santilli (62:21):** Okay, cool.

**Cody Henshaw (62:33):** I don't know who the right person. I don't know if it's Cjab Dan to talk about the CMS stuff, but yeah, and do that offline.

**Marcel Santilli (62:39):** Awesome. I know we're over. Apologies, George. Anything to. To wrap up, we'll send a follow up.

**George Haikal (62:45):** No, this, this was great. We'll send a follow up. Yeah, the main thing that stick out is we're going to try to get as much context as possible, figure out all the access, who the right people are to work with on these different kind of lanes and then shaping the lane. So the AI gateway, the slash I and then also just understanding where the other opportunities might be that we can explore and like place experimental bets on. And so a ton of work between now and then, but I'm super excited to get into it.

**Cody Henshaw (63:12):** Sweet.

**Dan Fein (63:13):** Great to meet you guys. Fun.

**Marcel Santilli (63:13):** Awesome. I. I'm pumped. I appreciate you both. We'll talk soon. All right, y'all, Bye.

**Cody Henshaw (63:14):** Thanks, y'all. Same talk soon.

**Dan Fein (63:17):** Sounds good. All right.

**George Haikal (63:17):** Let's go. But.
