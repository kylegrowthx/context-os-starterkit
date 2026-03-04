# GrowthX Bi-Weekly All Hands

<metadata>
date: 2025-04-15
time: 15:59 UTC
duration: 31 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, Bridget McGillivray, Sucheta Biswas, Nicolas Fernandez, Alexandra Vaughan, Matt Panzarino, Branko Kral, Carrie Chowske, Clint Shryock, Usman Ghani, Daniel Lopes, Kirkland Gee, Bruno Santilli, Mariana Montezzana
fathom_recording_id: 57390439
fathom_url: https://fathom.video/calls/276299580
share_url: https://fathom.video/share/PqoYcVGyLy1s1KFKd5yupk1kF3x5yRV8
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

GrowthX held its bi-weekly all-hands meeting to celebrate significant company growth (7 new hires bringing headcount to 50), update the pipeline strategy focusing on higher-quality deals including Webflow, SentinelOne, and StackBlitz ($330k contract), and demonstrate new AI-powered workflows for content creation and style guide generation. The team emphasized stricter qualification criteria, higher average deal sizes ($12k-15k+), and new tools like Linear and Geekbot for improved project tracking and team communication.

---

## Context

This is GrowthX's internal bi-weekly all-hands meeting held on April 15, 2025. The company is experiencing rapid growth, having scaled from 10 employees in January to 50 by mid-April. Marcel Santilli (CEO) and Bridget McGillivray (VP of Operations) led the meeting, celebrating seven new hires with diverse backgrounds and skillsets, then diving into business updates from the sales and delivery teams. The meeting showcased two major strategic shifts: a more selective sales approach focusing on high-quality enterprise deals and higher domain authority, and new AI-powered internal tools designed to improve content delivery and team workflows for their B2B SaaS content marketing services and CheckThat AI visibility platform.

---

## Relevance

**To GrowthX Delivery:**
- New workflow for extracting company names and key topics from articles, plus automated image search integration, will reduce research friction for content teams
- Style guide generator (accepting up to 10 example articles) creates customized tone/voice guides that teams must refine manually — critical for matching client brand voice
- Linear project management now integrates with Slack for task tracking; separate projects for client work vs. internal requests (small: <1 week, large: >1 week)
- Article analysis and image integration workflows moving from testing to production, requiring team feedback on outputs

**To CheckThat:**
- Voice agent work with VAPI AI ($27k/month engagement) showcases AI visibility strategy for niche use cases; opportunities to audit CheckThat prompts for voice agent products
- StackBlitz Bolt.new content strategy (building fully functioning app examples) aligns with CheckThat's positioning for developer tools and product categories

**To GrowthX Business Development:**
- Deal quality improving significantly: Webflow (kickoff), SentinelOne (late procurement), Normal Security (closed), StackBlitz (closed, $330k contract), Vappy AI ($27k/month)
- Average deal size increasing to $12k-15k+, up from smaller engagements; less than 2 months to close on major deals
- Series A funding announcement expected the following week; anticipated spike in inbound pipeline
- Strong logos across compliance-heavy and technical industries (CERN, Imobit) indicate market expansion beyond core vertical
- Stricter ICP qualification criteria filtering out low-domain-authority prospects, focusing on high-quality relationships

---

## Overview

- Company growth: 7 new hires, now at 50 employees (up from 10 in January)
- Pipeline focus: Stricter qualification criteria leading to higher-quality deals (e.g., Webflow, SentinelOne)
- New workflows: Style guide generator and article analysis tool introduced to enhance content creation
- Linear & Geekbot usage: Emphasized for improved task tracking and team communication

---

## Key Topics

### New Hire Introductions

  - 7 new employees introduced, bringing total headcount to 50
  - Diverse backgrounds: UK, Colombia, Slovakia, North Carolina, Missouri, India, Pakistan
  - Varied interests: horse riding, mountain biking, cat rescue, CrossFit, yoga, football

### Pipeline & Deal Updates

  - More selective qualification process: focusing on higher domain authority and ICP fit
  - Notable deals:
      - Webflow: Kickoff last week
      - SentinelOne: Late procurement stage
      - Vappy AI: $27k/month for voice agent technology
      - StackBlitz: $27k/month, \~$330k contract for Bolt.new product
      - CERN and Imobit: Targeting compliance-heavy and technical industries
  - Average deal size increasing to $12k-15k+

### New Workflows Demonstration

  - Article analysis tool: Extracts company names, key topics, and performs image searches from input text
  - Style guide generator:
      - Creates customized style guides based on example articles (up to 10)
      - Outputs sections on tone, voice, with good/bad examples
      - Designed to be further refined manually for client-specific needs

### Linear & Geekbot Usage

  - Geekbot: Used for daily stand-ups and team communication
  - Linear:
      - Project management tool with separate projects for each client
      - Small requests (\<1 week) vs. larger projects (\>1 week)
      - Integration with Slack for easy task creation

---

## Action Items

**Bridget McGillivray (GrowthX)**
- Update sales alert channel with recent deals (Webflow, SentinelOne, Normal Security, StackBlitz)

**Daniel Lopes (GrowthX)**
- Build workflows to summarize and send digests of Geekbot updates

**Kirkland Gee (GrowthX)**
- Continue development on image integration and generation workflows

**Team (GrowthX)**
- Use Linear for tracking work; create tasks from Slack requests
- Test new style guide workflow in Aerofs; provide feedback on outputs vs. client style guides
- Customize generated style guides manually for client-specific tone and examples

---

## Transcript

**Sucheta Biswas:** Sorry, I couldn't hear you.

**Bridget McGillivray:** I'm going to play some music.

**Sucheta Biswas:** Okay.

**Bridget McGillivray:** My computer is frozen now.

**Sucheta Biswas:** I can see a presentation screen.

**Bridget McGillivray:** Very pretty.

**Nicolas Fernandez:** Hello, everyone.

**Bridget McGillivray:** Everyone can see my screen?

**Bridget McGillivray:** Hopefully. Thumbs up. Perfect. Okay, cool.

**Bridget McGillivray:** So, agenda for today:

**Bridget McGillivray:** Oh, there we go.

**Bridget McGillivray:** New hires, we'll do some intros, so I hope you're all here, and I'll have you introduce yourself.

**Bridget McGillivray:** And then we'll do a little update on the pipeline, talk about some of the new customers we've signed since last time, and then Daniel's going to take over and do a little linear.

**Bridget McGillivray:** This meeting is being recorded.

**Bridget McGillivray:** As well as show some new workflows.

**Bridget McGillivray:** So, it should be good.

**Bridget McGillivray:** Let's start with new hires. We had seven people start since the last all-hands meeting. We're now at 50 people in the company, which is crazy. So, if you each want to introduce yourselves, I'll call your name, and you can come off mute and just tell us your name, where you're from, and then something you like doing outside of work.

**Alexandra Vaughan:** My name is Alexandra Vaughan. I am from Bogota, Colombia. And something that I like to do other than work is probably horse riding.

**Bridget McGillivray:** Nice, awesome.

**Bridget McGillivray:** Cool.

**Bridget McGillivray:** Matthew, do you want to go next?

**Matthew Panzarino:** Yeah, hey, I'm Matt. I'm from the UK, but living in Cape Town. And I'm a big mountain biker, much to the detriment of my financial situation. I spend a lot of money on it.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Nice.

**Bridget McGillivray:** You and Daniel can bond over that.

**Bridget McGillivray:** How many bikes you each have.

**Bridget McGillivray:** All right, Usman, you want to go next?

**Bridget McGillivray:** We'll right back.

**Bridget McGillivray:** You

**Bridget McGillivray:** Roseman, are you there?

**Bridget McGillivray:** Okay, we'll skip.

**Bridget McGillivray:** Branko, do you want to go?

**Branko Kral:** Sure, thanks. I'm big into mountain biking. I used to be very broke and very happy because of it during college, and it stuck with me. I'm also into backcountry snowboarding, strength training, and doing goofy stuff with my kid and my partner. I'm in Slovakia. I used to live in California for about eight years in Mammoth, and I would come down to the cities for business and conferences. I'm stoked to be here and feeling very good about the team and where this is all headed.

**Bridget McGillivray:** Awesome.

**Bridget McGillivray:** Excited to have you.

**Bridget McGillivray:** Carrie, want to go next?

**Bridget McGillivray:** I have a feeling I know what your hobby will be.

**Carrie Chowske:** Anyone who knows me is going to know what this answer is going to be. I'm in North Carolina. We've lived here for just about a year. Before that, I was in Florida. Outside of work, I do a lot of different things, but we've primarily been focused on cat rescue for quite a while. At one point, I think we had something like 30 to 40 cats and kittens in our house, but we only have 10 currently. One of them is technically a foster, but I don't think he's going to find a home, and I'm annoyed about it because he's really goofy.

**Bridget McGillivray:** I'm still mind blown by that, by the way, 30 to 40 cats in the house.

**Carrie Chowske:** That's not even a lot, that's what's so funny, is in Rescue Man, it's like, yeah, the keyword is only Mara listen.

**Carrie Chowske:** I, I, yeah, we, yeah, we've cut back, since we moved to North Carolina, we cut back and then immediately found three mother cats that were co-parenting 20 kittens that we have found homes for, so.

**Bridget McGillivray:** Wow, so you're very busy, but we're excited to have you on the team.

**Bridget McGillivray:** Clint, do you want to go next?

**Clint Shryock:** Hey, everyone. I'm Clint. I'm in Missouri. As far as things I like to do, I like playing sports. My wife and I do CrossFit. My kids are in a lot of sports, so we're doing a lot of that. All five of us enjoy skiing, so we try to go to Colorado twice a year. We just went for spring break, where all five of us picked up snowboarding for the first time. I have two small dogs that you'll probably see if you ever have conference calls with me, because they follow me everywhere.

**Bridget McGillivray:** Awesome.

**Bridget McGillivray:** Thank you, Clint.

**Bridget McGillivray:** Sucheta, you want to go next?

**Sucheta Biswas:** Yeah. Hey, hi, everyone. I'm Sucheta from India. I live in the Silicon Valley of India, also called Bangalore. Outside of work, I do a lot of things, but I primarily like to do yoga. I'm also into gardening. I have one cat, he's a ginger, and he's a very clingy cat, so you will see him around.

**Bridget McGillivray:** Nice, thank you, and I think Usman, I see you're here.

**Usman Ghani:** Yes, sorry, my audio was off, I didn't notice it earlier.

**Bridget McGillivray:** No worries.

**Usman Ghani:** I'm from Karachi, Pakistan. I've joined as a content manager. The fun fact about me is that I'm a football fan. I support Barcelona Football Club.

**Bridget McGillivray:** Nice.

**Bridget McGillivray:** Cool, thank you all.

**Bridget McGillivray:** Thanks for the intros, and we're all excited to work with you.

**Bridget McGillivray:** I will jump forward now, and Marcel, are you here now?

**Marcel Santilli:** Yeah, what's going on, everyone? I was just meeting with a customer in person, so I got to hear everybody's intro. I got to see some familiar faces as well. A fun fact: Clint was very early on at HashiCorp, and I was there for two years. I'm super excited to see all of you, and I feel personally really humbled that Clint is here as well, joining us in this journey. HashiCorp is a company that had amazing culture and obviously went public. Clint stayed all the way to them going public. Terraform is a huge inspiration for how we're thinking about the product. I just wanted to give a special shout-out. We're super excited for you to join in. It's just insane that we have 50 people — we were literally 10 in January. This is awesome. There's a lot of work ahead, but it's pretty exciting as well. Let me mention a little bit here on the pipeline. I'll talk about some of the things that Bruno and the team and I have been working on.

**Marcel Santilli:** One of the things we're starting to notice is that we need to be more strict about our qualification criteria. We're starting to essentially turn down more meetings with companies that have no domain authority and very little ICP fit. Because of that, we're being a lot more strict. But the benefit is that the deals we're closing are higher quality deals. We did a kickoff last week with Webflow, we're in late procurement with SentinelOne, we closed Normal Security, and we just closed StackBlitz yesterday. These are really amazing logos. A lot of really awesome companies that every company would kill to have. Most of our pipeline is made out of those, which is pretty exciting. Also, with our Series A announcement coming up most likely next week, we should see a huge spike in inbound. If you're ever curious on deals, we also have a sales alert channel where you can keep track of things.

**Marcel Santilli:** But with that, we'll go into a couple of the logos we closed.

**Marcel Santilli:** Before I touch on that, there's one I wanted to touch on a bit more that's related to StackBlitz as well. That's VAPI AI. What's really cool is that we won VAPI AI at $27,000 a month, and StackBlitz is also $27,000. The main reason we won VAPI is also because we talked about what we were going to do for StackBlitz, and they were super excited as well. The use case is pretty unique. With VAPI, they're voice agents. You can think of it like a custom GPT where you can prompt a voice agent. You can pick your transcriber like DeepGram or others. You can pick your voice provider like text-to-speech options like Google, Elevenlabs, or DeepGram. You plug in a phone number and you essentially have a fully functioning voice agent that you can use. It's a great platform, and they're doing really well. The whole idea of what we're doing with them is essentially pre-building some of these voice agents, pre-prompting them, and templatizing them. We're also creating landing pages that describe what those things are. So if you're creating a voice agent for a dentist's receptionist, or a voice agent that's an expert in something, we're trying to do that programmatically. With StackBlitz, it's kind of similar, and we closed that, which is really exciting.

**Marcel Santilli:** Most companies closing a $330,000 contract is a huge deal. For us, that's like $9,000 to $30,000 a month, which is pretty exciting. Even StackBlitz, which was a slower deal, closed in less than two months. StackBlitz built a product called Bolt.new. Their biggest competitor is Lovable. What we want to do for them is something like G2.com category pages, but with fully functioning apps. The idea is having an engineer in the loop to pre-build and scaffold some of these apps, then embed them in pages that are fully enriched. If you're searching for, let's say, a CRM for dentists, what's a better experience than landing on an actually fully functioning app? Or how to build a Product Hunt clone — what's better than having an actually fully functioning Product Hunt experience that you can port? The idea is to do that and eventually plug in user-generated content to feature on the catalog as well. It's pretty cool.

**Marcel Santilli:** We've got two other ones, CERN and Imobit. What's really exciting with companies that are in spaces that are either compliance-heavy or more technical is that they're so underserved. Think about process optimization for chemical plants — just the amount of terminology and knowledge that's really hard to find because a lot of it is hidden away in PDFs or random places. Research agents and our workflows that help research and find that knowledge do really well there. It's a huge opportunity where there are a lot of people searching for it, and I think we can have a meaningful impact on these companies. These are more technical industries, but they're also underserved. So it's pretty exciting, and our average deal size now has been in the $12k-15k+ range, which is pretty exciting.

**Bridget McGillivray:** Perfect.

**Bridget McGillivray:** Thanks, Marcel.

**Bridget McGillivray:** All right, I'm going to jump forward, so Daniel, want to take over, and we have 15 minutes, so I think you'll be able to get through.

**Bridget McGillivray:** Both of those.

**Daniel Lopes:** Yeah, I'll go real quick, because I'm going to pass it off to Kirkland right after.

**Daniel Lopes:** But Kirkland has been the one building most of the new workflows, so it's great to have him demo everything himself.

**Daniel Lopes:** One thing I was going to show is a quick refresher on Linear and how we use Geekbot as well. First thing: always make sure to answer your Geekbot. It's super helpful to all of us. I see everything that's happening. I'm going to log in to show you our views and how people have managed their accounts in Geekbot. We can see everything that's happening, and I'm planning to build workflows on top of this so we can summarize and send digests of what's happening.

**Daniel Lopes:** In my case, for example, I'm constantly monitoring a handful of pods or groups. For example, the Delivery Pod (EPD) is super important for me, so I can see every day what's happening with everybody. I check Slack most of the time, but I also check Geekbot once a week or so to see what's going on and what everybody's talking about. I have a timeline to see everything, and everyone else has their timeline as well. I'm not sure if all of you can log into Geekbot and see the same way we do, but the directors have their own, and each pod has their own. It's pretty easy for us to go back and see what happened to that pod. The plan is to build more integrations on top of this and make it easier to parse things out and share the information across the board.

**Daniel Lopes:** One other thing: by now, every account should have a project in Linear. I'm going to open my Linear here and show you how to find where your requests are and what's the current state of the things that you shared in Slack with the engineering team. Over time, my hope is that the rest of our organization can develop the same habit of creating things and sharing tasks and handing off work to each other.

**Daniel Lopes:** For the EPD team, if you're going to projects, we now have six teams, and the teams all have projects inside. The main thing we'll see here is the Onboarding team, so we're using this for new folks that are joining. For example, with Clint, I can see exactly what he's up to this week. We have a few milestones for him. The first couple of days is learning how we work, then learning about the business, learning about LLMs and AI in general, learning our internal tech, and then starting to work with us on real tasks. We tend to have the same approach with all the other areas as well. That's on the engineering side. On the Delivery side, you all have projects. Some of you are already using it pretty actively, and some of you are still starting. I would recommend looking at your daily stand-ups in your pod and seeing what can be passed off, what should be tracked on a multi-day period. That's a good approach to what can be shared and put in a tool like Linear. In my case, we're always receiving a ton of requests.

**Daniel Lopes:** One of the requests was from Mariana asking to add localization to a refresher grid. The first thing I would do is create a task from Slack. I tag the issue to the small requests project. We have separate projects for different types of work. We have a project for small requests — things that might take a couple of days but everything less than a week. Pretty much everything you ask in our EPD request and feedback channel goes into this project. We also have a roadmap that I'm still porting from Basecamp. Then we have major projects. Projects are everything that takes more than a week. We have three projects in progress now. Felipe is working on the pipeline, which will replace some of the work we're doing. Things are moving pretty fast, and it's looking good. We have an Ashby migration — we're moving out of Workable to Ashby, and Marcus is leading that. Marcus is part-time but does a lot in just four hours. We're super happy that next month he's joining full-time. This next week is mostly focused on the Ashby migration, so Kirkland will be handling most Slack responses until Marcus is done. Kirkland is also leading an effort to think about how we can handle programmatic workflows — landing pages with different components. Because of this view, I can have a good idea of how the projects are going. Think of Linear as a place to share the work and never forget the work that's there. Your projects are synced, and you have a project for each one of your clients in Linear. We have filters predefined for the board, and you can create your own filters. If anybody's not in a project, that's where I can come in and pick something meaningful to work on. We have different labels, so client requests are things specific to certain clients. Because we're creating things from Slack, it will be synced with Slack as well, and they'll be notified. The same approach can work on all of your projects.

**Daniel Lopes:** Now, one cool workflow we haven't released yet — Kirkland built this. Imagine you have an article. In this case, I grabbed an article from G2 about customer review statistics. I'm just passing the whole article, and then we break it down: we read the article and extract company names and brands, and key topics. Then we perform image searches on this, and at the end we can have a bunch of images you can use to find things you want to reference in your article. You don't have to search for things on the internet multiple times. For example, if you're going to write about Power Reviews, you could reference logos from these companies. We're also doing some other things for image integration and image generation that Kirkland is working on. I'll pass to him now.

**Kirkland Gee:** Yeah, that workflow he just demoed is live in AEO Grid. It probably needs some bug fixing and testing, but it's coming along. I wanted to show one other thing. We got some requests about style guides and people having issues with workflows not understanding tone, voice, or specific grammar and formatting. I made a separate workflow where you can create a style guide that you can put into your polishing instructions or wherever in your workflow. This is an example I did for GrowthX. It kind of works, but since we don't have a lot of blog content, it has some weird things like suggesting a lot of hashtags because our landing page has many headings. Let me show a different example. With StackBlitz, all you have to do is give a couple of example articles. You can provide up to 10, comma-separated. I cut it off at 10 because you usually get the general gist with 10 examples. Just throw this in, run the workflow. It takes a minute to run because it scrapes all those pages. It creates a style guide based on each blog post and synthesizes all those into one final output. While that's running, I'll show an example from the past. Here's one for VAPI. It gives you sections for tone and voice, and for each section, it shows: here's what you should do, here's a bad example, here's a good example — all based on the content you feed into the workflow. The biggest thing is to go use this and see how it works. We've done some initial tests, but there's always room for improvement. Go run it, see what you get compared to a client style guide. See if it's getting close or if there are things missing or specific elements you want to use. This is a standalone workflow in Aerofs, not attached to any grids. Get the output and put it in your polishing instructions or feedback in the grids.

**Daniel Lopes:** Yeah, I'd also add that a good place to put this would be either in the polish instructions in the grid or in the feedback section. You can split the feedback and put at the top something like "maintain this tone." That's one way to use it. What will be generated is just an initial draft. You should edit that a ton manually. It's just there to help you start. But it's worth spending even a day just customizing it, coming up with the right examples, asking the client what their favorite articles are, reading the articles yourself. The main thing is the format. Having sections on tone and voice that matters and why it matters, with good and bad examples. Handcrafting that will get you super close to the right tone.

**Marcel Santilli:** Let me double-click on this because it's super critical. A client we're working with is a great example. The CEO cares deeply about their brand and voice. For us to win their trust, even before we close the deal, we have to show we're capable of delivering really unique, well-positioned style and tone content that's actually useful. That's super critical. Part of my process last night was finding writings that would work well with that brand. They have no blog content — just product announcements. So I did a hybrid approach. I picked the manifesto from Bryce Daniel's Indie VC, took some writing from Jason Fried at 37 Signals, combined it with the About page from First Round's publication, and came up with a really awesome kind of vibe. Then I could feed some of that into this workflow. But this doesn't replace critical thinking, creative skills, connecting the dots, and having taste. That's where you all come in. It's super critical: if you see really good writing or unique tones, save it. We're going to create a repository of that. Most of our clients have no great examples of what they actually want either.

**Bridget McGillivray:** It's super exciting. All right, I think that's it for today. Thank you, Kirkland. And also, if anybody wants to do presentations or demos of something exciting you're working on, please let me know. I'd love to have more guest speakers in the all-hands showing us what you're working on.

**Marcel Santilli:** This is ridiculous. We're always finishing the all-hands on time.

**Bridget McGillivray:** How is this possible?

**Marcel Santilli:** This has never happened before, and you keep doing it.

**Bridget McGillivray:** Well, knock on wood, but let's hope we keep doing it. Thanks, everyone. Have a good day and week.

**Bruno Santilli:** See you next time. Thank you.

**Mariana Montezzana:** Take care.

**Branko Kral:** Have a great day.
