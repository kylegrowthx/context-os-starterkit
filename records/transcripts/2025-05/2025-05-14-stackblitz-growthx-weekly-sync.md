# Stackblitz <> GrowthX Weekly Sync

<metadata>
date: 2025-05-14
time: 17:31 UTC
duration: 49 minutes
organizer: daniel@growthxlabs.com
participants: Matthew Panzarino, Dave Capone, Mariana Montezzana, George Haikal, Daniel Lopes, Mitchell Wright, Monika Rozanska, KJ Krause
fathom_recording_id: 62635191
fathom_url: https://fathom.video/calls/299138443
share_url: https://fathom.video/share/oHTHxRHhcwkTCerzc7j58LyEtUuA2vq1
source: fathom
enriched_on: 2026-03-04 00:35 UTC
</metadata>

---

## Summary

GrowthX demonstrated significant progress on two key content projects for StackBlitz: ~30 one-shot templates for websites, apps, and micro-apps with companion articles, and a feature matrix comparing StackBlitz to competitors (Lovable, V0, Cursor) with persona-specific comparison content. The team aligned on a May 30th deadline for the templates page ahead of the hackathon, with action items including 5 competitor comparison articles and 5-10 template examples with supporting articles due by Friday. Key decisions included moving forward with the Webflow CMS integration, establishing a community template curation system, and determining the timeline for StackBlitz's website redesign.

---

## Context

StackBlitz is a cloud-based development environment and IDE used by millions of developers. The company (now ~30 people) is undertaking a website redesign and considering a move to Webflow CMS for better content management and flexibility. This weekly sync is part of GrowthX's ongoing $200k+ engagement to deliver content marketing, template documentation, and competitive analysis for StackBlitz.

The meeting followed a previous call the day before where GrowthX collected raw user session data from KJ at StackBlitz to understand what developers actually build with the platform. This analysis informed both the template project (identifying high-value use cases) and the competitor comparison strategy (understanding how users differentiate StackBlitz from alternatives).

---

## Relevance

### To GrowthX Delivery

- New workflow pattern: analyzing raw user session data at scale (1,000+ sessions) to identify high-ROI content topics and templates
- Companion article strategy integrating SEO-focused intros, prompt engineering tips, and customization guidance — expanding beyond basic templates
- Balancing content accuracy with maintainability in competitor comparisons; established principle of focusing on direct competitors and avoiding overreaching claims

### To CheckThat

- Direct application of AI visibility and prompt engineering research: validating one-shot prompt reliability at scale across website, app, and micro-app templates
- Opportunity to measure how StackBlitz's AI-generated templates impact discoverability and search behavior

### To GrowthX Business Development

- Expanding engagement scope: CMS integration work (Webflow setup) signals potential additional revenue opportunity
- Community template submission/curation system is a new technical requirement that may require additional scope or integration work
- May 30th hackathon deadline is a hard constraint; Friday deliverables (5 comparison articles + 5-10 templates) are critical milestones

---

## Overview

- GrowthX has made significant progress on template generation and competitor comparison workflows
- StackBlitz is undergoing a website redesign, potentially moving to Webflow CMS
- Priority is to create a templates page for the upcoming hackathon (May 30th)
- Need to balance accuracy and maintainability for competitor comparison content

---

## Key Topics

### Template Generation Progress

  - Created \~30 one-shot prompts for websites, apps, and micro-apps
  - Developed custom workflows for generating briefs and companion articles
  - Companion articles include SEO-focused intros, prompt engineering tips, and customization guidance
  - Considering both usefulness and search volume for template topics

### Competitor Comparison Approach

  - Developed feature matrix comparing StackBlitz to competitors across various categories
  - Created custom workflow for generating comparison articles with persona-specific content
  - Balancing need for accuracy with maintainability of competitor information
  - Focusing on direct competitors initially, being cautious with claims about competitors

### Website Integration and CMS

  - StackBlitz considering move to Webflow for marketing site and CMS
  - GrowthX can set up staging Webflow account to start populating content
  - Possibility of creating static pages as interim solution before full CMS integration

### Templates Page and Community Engagement

  - Priority to create a templates page for the upcoming hackathon (May 30th)
  - Plan to allow user-generated content submissions in the future
  - Considering features like commenting and creator profiles to foster community engagement

### User Research and Personas

  - GrowthX has created initial personas (e.g., internal tool builder, web designer)
  - KJ to provide additional data on user frustrations from prompt analysis
  - User interviews may be deprioritized to focus on template creation for hackathon

---

## Action Items

- **Dave Capone (GrowthX)**: Send list of potential comparison article topics for review
- **Dave Capone (GrowthX)**: Send voice guidelines & sample articles for review
- **Dave Capone (GrowthX)**: Send refined feature matrix doc for StackBlitz vs competitors
- **KJ Krause (StackBlitz)**: Add summary charts on user frustrations from prompting to shared doc
- **Mitchell Wright (StackBlitz)**: Determine timeline for website redesign & CMS integration
- **Mitchell Wright (StackBlitz)**: Have designers review Figma templates for brand alignment
- **Dave Capone (GrowthX)**: Set up staging Webflow account for CMS integration
- **Monika Rozanska (StackBlitz)**: Define requirements for community template submission/curation system
- **Dave Capone (GrowthX)**: Create & send 5 competitor comparison articles (e.g. Lovable, V0, Cursor) by Fri
- **Dave Capone (GrowthX)**: Send 5-10 template examples w/ supporting articles by Fri

---

## Transcript

**Mitchell Wright:** then Sunday, we drove to Tahoe and the whole company's out here now.

**Mitchell Wright:** That's awesome.

**Mitchell Wright:** That's awesome.

**Daniel Lopes:** How many people is the company now?

**Mitchell Wright:** About 30.

**Daniel Lopes:** Okay, nice.

**Daniel Lopes:** Oh, that's a decent size.

**Daniel Lopes:** That's hard to organize and everything.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Just too big to kind of wing it all.

**Mitchell Wright:** You have to still be planned.

**Mitchell Wright:** But yeah.

**Daniel Lopes:** Cool.

**Daniel Lopes:** I'll be quick here.

**Daniel Lopes:** We have quite a lot of things to cover.

**Daniel Lopes:** I think today, what I was thinking today would be like, just go through the agenda we have super quick.

**Daniel Lopes:** But if you have a different plan, if you want to talk about different things, you can also do that.

**Daniel Lopes:** But I wanted to show you everything that we did so far.

**Daniel Lopes:** This is actually just my camera here.

**Daniel Lopes:** Get rid of this.

**Daniel Lopes:** And I wanted to show you everything we did so far and where the things that we need next to start shipping the pages and putting stuff live.

**Daniel Lopes:** And...

**Daniel Lopes:** Some other ideas and some other things we found when we were doing the research.

**Daniel Lopes:** So does that work?

**Daniel Lopes:** Sure.

**Daniel Lopes:** Cool.

**Mitchell Wright:** So just a quick refresher.

**Daniel Lopes:** we have, look, today I was thinking about we covered a quick demo of the two projects we have going, and then we talk about things like we have to decide direction on both projects, and we also have to decide how we handle the CMS integration, and how we work with your team, or do we do the pages on our side?

**Daniel Lopes:** And then we hand it off to them, and all that.

**Daniel Lopes:** But we can talk about that in the end.

**Daniel Lopes:** Essentially, we got the data from KJ last week, and we did some analysis on it.

**Daniel Lopes:** But what we ended up doing was just do a summarization of the sessions.

**Daniel Lopes:** And so we created the custom workflow that summarized the sessions, just for us to get an idea.

**Daniel Lopes:** It's not super precise the way you would have from the analysis that KJ was doing.

**Daniel Lopes:** But we just wanted to see what people are trying to do in volume, so we got all 1,000.

**Daniel Lopes:** how doing.

**Daniel Lopes:** And then, think

**Daniel Lopes:** So that he sent to us, and we summarized everything here on the right, and you can see the difference between, like, sometimes people would start with, like, designing, trying to build an app, and then they would get stuck with, like, some backhand integration, and they would come back, like, 10 days later and do, like, a landing page, and then pop by, you know, so there's, like, a bunch of, like, mixed use, which is kind of tricky to categorize.

**Daniel Lopes:** We just, like, dumped a bunch of, like, some of the categories that you guys had and asked to generate subcategories just for us to see what kind of things we were trying to do in general, but it's not super precise to get a direction, and then after that, we started thinking about the templates project and the comparison projects off of the things that we saw from both KJ analysis and also the activity sessions that we were doing.

**Daniel Lopes:** And what we ended up doing was, like, trying to figure out if there was a way to come up with one-shot prompts that would...

**Daniel Lopes:** Be impressive, but also something that you could change yourself.

**Daniel Lopes:** So a lot of things were like landing page that people are trying to do.

**Daniel Lopes:** Could you have a prompt that almost always generate a really good landing page or a website, but you still have control of removing sections or changing the color, changing the logo before you hit play?

**Daniel Lopes:** And so that would be a bunch of template pages that's kind of similar to what we tooled us.

**Daniel Lopes:** And we saw some other players that are in the no-code or low-code space.

**Daniel Lopes:** They had a bunch of templates, catalogs that were doing well.

**Daniel Lopes:** Verso has some as well, but Verso is less broad than something that Retool does, for example.

**Daniel Lopes:** So what we ended up testing, so we tested about 30 prompts that we got some decent results.

**Daniel Lopes:** So things like for websites, we had something like this, for example, there, I'm going to go to left and Slack.

**Daniel Lopes:** This was one-shot generation, and works pretty well most of the time, pretty much always.

**Daniel Lopes:** And then you have control over the colors and everything.

**Daniel Lopes:** So we can do that for websites, and we can do multi-pages and stuff like that.

**Daniel Lopes:** It's just the prompt gets longer if we do multi-pages.

**Daniel Lopes:** Same thing with a bunch of different websites.

**Daniel Lopes:** We did a lot of web design stuff.

**Daniel Lopes:** So we're going over some of the categories and trying to recreate things that would be interesting.

**Daniel Lopes:** And then we did the same thing with the entrepreneur category.

**Daniel Lopes:** Like, can we create a bunch of different apps, like personal apps, and apps that would be internal use stuff as well.

**Daniel Lopes:** So this one is interesting.

**Daniel Lopes:** Let's open.

**Daniel Lopes:** This one is similar to things, like inspired by Things 3.

**Daniel Lopes:** And you can close everything, and all the pages work.

**Daniel Lopes:** And the prompt is pretty cool.

**Daniel Lopes:** And it's not hard to change.

**Daniel Lopes:** So it would be like for a programmer, like, or in a

**Daniel Lopes:** You have the mock data, you have the task view that you can delete if you don't want.

**Daniel Lopes:** You can customize everything.

**Daniel Lopes:** There's no code here.

**Daniel Lopes:** So it's pretty easy to parse.

**Daniel Lopes:** And then we have a design system at the end.

**Daniel Lopes:** So we landed on this format where you have all the facts above and you have the mock data in between, help you understand what the screens do.

**Daniel Lopes:** And then you have a design system that we're using tailwind for most of it.

**Daniel Lopes:** And you can customize here.

**Daniel Lopes:** There's not a lot of full stack integration, because that's where some of the deploys were getting harder to have super, super fast.

**Daniel Lopes:** So if you're doing a super base integration or something like that, I think we could do it.

**Daniel Lopes:** But it's where we were having the deploy of Netlify.

**Daniel Lopes:** We had to go through the chat to fix the issues more.

**Daniel Lopes:** So we ended up just coming up with a bunch of stuff that was one shot and have good results.

**Daniel Lopes:** So this one's pretty, pretty long.

**Daniel Lopes:** Some other stuff was much more.

**Daniel Lopes:** We also saw a lot of people talking about micro-apps.

**Daniel Lopes:** Go ahead.

**Daniel Lopes:** Yeah, KJ.

**KJ Krause:** Yeah, so, yeah, just a question about, like, the integrations.

**KJ Krause:** I think for the simplicity of the initial prompting, it makes a lot of sense to use, like, mock data and not necessarily have, like, the base auth implemented in the first prompt.

**KJ Krause:** And something that might be helpful, though, is to think about how, with the first prompt, you can set up the user and their subsequent prompts for when they eventually do want to connect those integrations.

**KJ Krause:** Because they're still prompting cues you can make.

**KJ Krause:** So, like, if you tell the AI, just go ahead and use, like, mock data and memory, don't provision a database, but still, like, plan for the future and make sure that later on we can bring in that database.

**KJ Krause:** And then even, like, I imagine in the templates, there could be, like, a next steps sort of section, like, where do I go from here?

**KJ Krause:** Otherwise, we run the risk of, like, engaging users with this really cool-looking prompt, and then they're like, oh, , I can't.

**KJ Krause:** Like it won't develop because it was set up wrong.

**KJ Krause:** So like, even if we want to wow them with simplicity on the first prompt, we really do need to think about making sure that we're not going to stymie them accidentally.

**Daniel Lopes:** Yeah, I agree.

**Daniel Lopes:** Like, and I think there's two ways to do that.

**Daniel Lopes:** One is like the way you were saying.

**Daniel Lopes:** Another thing we could do is like, let me go back to the meeting.

**Daniel Lopes:** Another thing we're thinking is that alongside the prompt, we would need to have like a companion article.

**Daniel Lopes:** And then a companion article would explain how to change the prompt.

**Daniel Lopes:** We could also have like next steps and things to do.

**Daniel Lopes:** And then, so today the way we're doing the companion article is like this.

**Daniel Lopes:** So, open.

**Daniel Lopes:** Yeah, go ahead, Mitchell, while he's pulling this up.

**Mitchell Wright:** I think the other thing to think about here is, I mean, I obviously I want these prompts and what is.

**Mitchell Wright:** Yeah, that's precisely what I was going to ask next.

**Daniel Lopes:** But essentially what we came up with was two...

**Daniel Lopes:** Custom Workflows that we start with the persona and the category in the catalog.

**Daniel Lopes:** And then we also choose the tag stack and we have the request.

**Daniel Lopes:** So the request is just broad level things.

**Daniel Lopes:** Let's say it's like Things 3.

**Daniel Lopes:** It's a well-known thing.

**Daniel Lopes:** We will know how to try to replicate that.

**Daniel Lopes:** But if you want to create a design for a website, so we have something that's more detailed, like something like this, for example.

**Daniel Lopes:** Then that will create the brief, the prompt that I showed you.

**Daniel Lopes:** gamers?

**Daniel Lopes:** In that format, that has the mock data, has the sections, and has the design system at the end.

**Daniel Lopes:** So like this, first workflow that we created, we'll generate something like this.

**Daniel Lopes:** We'll generate the prompts, essentially.

**Daniel Lopes:** So we can customize the prompt here.

**Daniel Lopes:** We can do as much work as necessary in the beginning, or we can go for volume and then deploy and see what gets used.

**Daniel Lopes:** But the final thing we have is a companion article.

**Daniel Lopes:** So the companion article looks like this.

**Daniel Lopes:** In real life, let me show you the Figma file real quick, but we're thinking that the companion article would be something that would be, like the Figma file is just like a prototype for ourselves to see how we could build this, like how it could look like.

**Daniel Lopes:** But essentially, we have the embedded result.

**Daniel Lopes:** We could have the prompt on the right side.

**Daniel Lopes:** Maybe the prompt has to be much longer, the field.

**Daniel Lopes:** But the companion article would be on the left side explaining how you could customize this if you wanted to.

**Daniel Lopes:** Or it could have the next steps as well involved, or we could have the next steps as part of the program.

**Daniel Lopes:** We could do both.

**Daniel Lopes:** And the way we're doing today to increase our velocity here, that we have two workloads.

**Daniel Lopes:** The one that generates the brief and the one that generates the companion article based on the brief.

**Daniel Lopes:** And this is the output of the companion article.

**Daniel Lopes:** We maximize this one.

**Daniel Lopes:** I can send you all the articles after for you to take a look.

**Daniel Lopes:** But it will be based on We check the persona.

**Daniel Lopes:** We created a bunch of calibration material behind the scenes that has the personas, has the style guide, has some other material there.

**Daniel Lopes:** And it will create that intro.

**Daniel Lopes:** And the parts of the intro will try to be SEO focused.

**Daniel Lopes:** So we have a keyword of choice here.

**Daniel Lopes:** So if you were trying to optimize for SEO, you could have different keyword choices here.

**Daniel Lopes:** And it would try to introduce that in the intro and then maybe some of the heading.

**Daniel Lopes:** And it goes into essentially prompt engineering tips and showing things on the forehead.

**Daniel Lopes:** And is

**Daniel Lopes:** Yep.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And how are you picking those SEO keywords?

**Mitchell Wright:** What was the research methodology that you went through on that?

**Daniel Lopes:** Yeah, that's the thing that we have to check with you because I think we need to decide if we can optimize for usefulness and what people are trying to do or volume or we could do both.

**Daniel Lopes:** You know, we could do a bit of both and see what lands.

**Daniel Lopes:** So we are checking like what people are trying to do based on the on the the set we got as websites.

**Daniel Lopes:** And then we came up with like a short list of categories and subcategories, commercial websites, personal websites, e-commerce, directory, waitlist.

**Daniel Lopes:** And then we did a check on websites like people that are like selling things like this.

**Daniel Lopes:** You have like theme for us, have like agency websites and stuff like that, like Tailwind templates and then directors like this.

**Daniel Lopes:** And then we have like a bunch of those categories.

**Daniel Lopes:** And then we also did some search on what is the traffic?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Thank

**Daniel Lopes:** That companies like Retoo are getting for templates and others.

**Daniel Lopes:** So there's a bunch of templates that are...

**Daniel Lopes:** But there are templates for things like internal apps.

**Daniel Lopes:** me see.

**Daniel Lopes:** So Retoo, for example, is a good example that has a bunch of templates.

**Daniel Lopes:** The templates get a decent traffic.

**Daniel Lopes:** Let's see.

**Daniel Lopes:** Sometimes it would be a mix of full projects or sections of apps and stuff that Retoo has.

**Daniel Lopes:** So this would be slightly different than templates for web design agencies, but we can make both work.

**Daniel Lopes:** So I think we could make a choice of, like, maybe we do 10 things that we want people to know that's possible to do with both, and we get 10 things that is volume-based and we put both up and see which one gets more.

**Daniel Lopes:** Yeah, I think having, like, a varied approach to start would be interesting so we can see.

**Mitchell Wright:** How that plays out across the initial set of pages.

**Mitchell Wright:** Yeah, that's the thing.

**Daniel Lopes:** That's how we were thinking.

**Daniel Lopes:** That's the thing that I had here that we had to decide.

**Daniel Lopes:** But next steps, we can just come up with the list and the ideas, and then shoot that over to you, and you can just give us a thumbs up.

**Daniel Lopes:** And another thing that we would need to get the review from you, like it would be the review of the voice guidelines.

**Daniel Lopes:** So everything that we're doing on the article generation, and even in the brief, uses a bunch of AI context that we created ourselves.

**Daniel Lopes:** So just getting you guys to review that and see if it's aligned.

**Daniel Lopes:** But I will show you the output of the comparison article.

**Daniel Lopes:** That one, you can see the tone better.

**Daniel Lopes:** So I can send that to you today, like the guideline, the voice guideline, and the sample articles that we're getting generated through that.

**Daniel Lopes:** But if you don't have time, that's fine.

**Daniel Lopes:** We can just move it forward, and we can always calibrate that later.

**Daniel Lopes:** And then...

**Daniel Lopes:** The other project that we're doing is the comparison stuff.

**Daniel Lopes:** So the comparison, what we're started with, is this stuff that Lovable has.

**Daniel Lopes:** It's pretty useless.

**Daniel Lopes:** As somebody that uses all the different things I've used Lovable before, I'm always like, this doesn't answer anything for me.

**Daniel Lopes:** And it's like, this design sucks.

**Daniel Lopes:** It's missing the color there, even on their own logo.

**Daniel Lopes:** So the other thing is, can we create something that's better for the ICP?

**Daniel Lopes:** And so we started with a custom research workflow and see what kind of data we can get from the competitors.

**Daniel Lopes:** Or would it have to be the people, ourselves, like researching long tail competitors?

**Daniel Lopes:** Or should we focus on 10 people and research them a ton and come up with the right matrix of features that we do better than they do?

**Daniel Lopes:** So what we ended up doing is just come up with the matrix.

**Daniel Lopes:** I used that initial feature set that you gave us.

**Daniel Lopes:** And added to that, a lot of .

**Daniel Lopes:** Search on what people were saying about both on Reddit and on YouTube and some other places, and come up with a feature matrix broken down into a bunch of different sections.

**Daniel Lopes:** So AI and Prompt Workflow, you guys have the ability to enhance prompt before, you have the discussion mode, the pricing is different, and a lot of stuff on the GitHub projects, Context Aware.

**Daniel Lopes:** So because you guys have the GitHub project, I don't know how that fits into your strategy.

**Daniel Lopes:** If everything's in GitHub, is it true to the real product that's in production, or do you guys have a different version?

**Daniel Lopes:** Because a lot of the research that we did ended up landing on the open source side of things.

**Daniel Lopes:** So the feature set here that I have is something that if you guys could help us narrow down to the precise things, it would really help with the comparison.

**Daniel Lopes:** But essentially we came up with like this section.

**Daniel Lopes:** it's AI Prompt Workflow, Framework, and Language.

**Daniel Lopes:** Port, so you guys have a bunch of stuff the other folks don't have, like Expo and some full-stack stuff, Vercell doesn't have any of this, and then you have Vizira, and then you have design and prototyping stuff.

**Daniel Lopes:** Now that you guys just had the GitHub one, that was something that everybody was complaining about, and we can make sure that's obvious on all these pages.

**Daniel Lopes:** And then you have integrations, like some of the integrations, like Netlify is way better than stuff that some of the other players are doing.

**Daniel Lopes:** It really works.

**Daniel Lopes:** And then there's some stuff with like development environment, like multi-file editing, like some of the players don't have to edit the files and stuff like that.

**Daniel Lopes:** And then same thing with deploy and hostment, hosting, deployment and hosting, and then collaboration and versioning, mobile development, non-issues.

**Daniel Lopes:** Because this is just for us to know what we should avoid in the articles, and then experimental features, the stuff that you guys are building.

**Daniel Lopes:** And then we also got a bunch of community nodes off of Reddit, YouTube, and stuff like that.

**Daniel Lopes:** And I left.

**Daniel Lopes:** left.

**Daniel Lopes:** The bunch of the citations.

**Daniel Lopes:** So this is done with a ton of the deep research of perplexity, and then reviewing mentally and going through some of this stuff.

**Daniel Lopes:** But ideally, we'll get you guys to just give us, is this in the right direction?

**Daniel Lopes:** Are we missing some certain areas here?

**Daniel Lopes:** This is a very long document.

**Daniel Lopes:** don't have to review the whole thing.

**Daniel Lopes:** Just give us, I'll send you it after.

**Daniel Lopes:** But this is the foundation for the comparison.

**Daniel Lopes:** So the comparison process we have today works like this.

**Daniel Lopes:** So this is the initial data set for ourselves, for both.

**Daniel Lopes:** And then we have an article drafting that works like this.

**Daniel Lopes:** So this has the embedded comparison that I just showed you, and it has a questions bank for each one of those sections inside of our custom workflow.

**Daniel Lopes:** So we have a custom workflow that I'll do.

**Daniel Lopes:** Let me show you.

**Daniel Lopes:** So we have a data button, which is like this smaller player that I...

**Daniel Lopes:** I...

**Daniel Lopes:** I...

**Daniel Lopes:** I...

**Daniel Lopes:** I...

**Daniel Lopes:** I wasn't really familiar with it, so I used this as a testing, and then Lovable, pretty familiar with what they do, Cursor I know upside down, so I was just testing, and Retool was like, is it really a competitor?

**Daniel Lopes:** But now that you see people doing integrations, internal integrations, it really is, but they're kind of indirect competitor.

**Daniel Lopes:** So I wanted to compare all four and what we got out of it.

**Daniel Lopes:** And the research here that's happening under the hood, let me show you all that.

**Daniel Lopes:** We use Aerox, Aerox can't handle the volume of this.

**Daniel Lopes:** So we start with something like this, just the URL, the name of the competitor, and a description, like a rough description that we write ourselves.

**Daniel Lopes:** And then we'll generate, and we use a questions bank that we have under the hood.

**Daniel Lopes:** Let me show that real quick.

**Daniel Lopes:** So, comparison, StackBlitz.

**Daniel Lopes:** We have a question bank.

**Daniel Lopes:** So we have a research and a comparison article generation.

**Daniel Lopes:** I'll show you the prompt real quick.

**Daniel Lopes:** But we have a question bank.

**Daniel Lopes:** I think that will have specific things for each area.

**Daniel Lopes:** So all the questions that we want to look for those competitors, and each one of these questions will trigger a deep research with perplexity, and then we calibrate manually.

**Daniel Lopes:** So the output of this is a document like this for Cursor, for example.

**Daniel Lopes:** We have an executive summary, their key strengths, the key limitations, and then for each one of the sections that we had defined, will create a table, seeing if they can do that or not, and how, and what's the limitations, and then at the end, a lot of things that people are talking about.

**Daniel Lopes:** So essentially the same stuff that we did for both, we do for the competitors, and then we try to merge both as a second step, and the second step looks like this.

**Daniel Lopes:** So the search result, we paste it here, we're using our pipeline thing, and we will refine this for each player if you want to, and then both data is here as well as an input data for us, so if we calibrate everything on that node.

**Daniel Lopes:** Fathom will update here.

**Daniel Lopes:** And then we have the personas.

**Daniel Lopes:** So the personas, this is where the style guide and calibrating the voice really helps because we have internal tool builder and the web designer, for example, and the things that they care about, their primary objectives and all that.

**Daniel Lopes:** So we have all this in Notion and I can send it to you and you guys, if you guys help us calibrate, it would make a difference.

**Daniel Lopes:** And then we have also two, so I've grouped the two personas together, the web designer and the internal tool builder, because these are people that know how to program.

**Daniel Lopes:** And then we have entrepreneur and a PM and operations lead.

**Daniel Lopes:** Those are people that are less technical.

**Daniel Lopes:** And when we trigger the article generation, the article generation will look like this.

**Daniel Lopes:** So we have in the case of both versus cursor, which in my mind was the one that would be like more interesting to see what happens.

**Daniel Lopes:** Because and then the intro is like it knows we're dealing with programmers here because it's cursor.

**Daniel Lopes:** And we'll be like using the like get something live.

**Daniel Lopes:** We'll

**Daniel Lopes:** Without yak shaving, can away, they approach the things in a different angle and will say things like, with both, can ship an MVP fast, but we recommend you start your project both, and later you can move on to Cursor.

**Daniel Lopes:** So it knows the weak spots of Cursor, and we're over-indexing and making sure both looks good.

**Daniel Lopes:** So it will always suggest that the both plays an important role here, and we'll have something like a fixed amount of sections.

**Daniel Lopes:** So we have an outline that we always follow.

**Daniel Lopes:** There's an article template here, and this is the article template.

**Daniel Lopes:** And we can create as many templates as we want.

**Daniel Lopes:** If we want to do one-to-one comparison of direct competitors, it could be one template.

**Daniel Lopes:** If we're going to do supporting players, it could be a different template.

**Daniel Lopes:** And if we're going to use case-based, it could be a different template, too.

**Daniel Lopes:** And the output of that, let me show you real quick, the final version of the Cursor one.

**Daniel Lopes:** Like I said, it would be like a table explaining the things that both does well, the things that other players...

**Daniel Lopes:** Do well in the things that they don't do well, or differences in cost and things like that.

**Daniel Lopes:** And this would be the kind of stuff that we'll have to do editorial work to review, and we have to decide, like, how much do we care about reviewing the results of the competitor?

**Daniel Lopes:** But we need to make sure at least what we have for both is 100% right always.

**Daniel Lopes:** So that's a decision we're going to have to make on the competitor side.

**Daniel Lopes:** But the UI of this would look like this, the way we're thinking.

**Daniel Lopes:** It's more like a prototype, so we can calibrate as much as needed.

**Daniel Lopes:** But it would be both versus lovable.

**Daniel Lopes:** We would have a TLDR.

**Daniel Lopes:** Actually, let show you another one.

**Daniel Lopes:** This one is an older one.

**Daniel Lopes:** So it would be...

**Daniel Lopes:** So it's both versus lovable on an intro, a TLDR, and then we can have the specific features.

**Daniel Lopes:** That we care about.

**Daniel Lopes:** This is just simple stuff.

**Daniel Lopes:** And then we can have this section.

**Daniel Lopes:** Like I showed you, so it could be like how both compares to lovable.

**Daniel Lopes:** And then we have the main areas.

**Daniel Lopes:** And then we break down each area based on what we do well versus them and why it matters.

**Daniel Lopes:** And then at the end, we can have a list of things that people are talking about that we can shuffle and have in different order.

**Daniel Lopes:** And then you can have an FAQ at the end as well.

**Daniel Lopes:** So the FAQ, we're getting pretty good results off of the research that we're doing.

**Daniel Lopes:** It's like, for example, we'll have the FAQ is here.

**Daniel Lopes:** So they're going like in very detail because of the amount of data we have on the other players.

**Daniel Lopes:** So we'll see like the context window, we'll talk about token cost, we'll talk about what people are complaining on Reddit about lovable or cursor and things like that.

**Daniel Lopes:** So we can extend the FAQ to have a big list and then we can shrink it down to whatever we want to ship.

**Daniel Lopes:** So let's

**Daniel Lopes:** The general direction that we went with the comparison, and we're almost done.

**Daniel Lopes:** Yeah, so what we're going to have to decide with the comparison one is essentially, do we want to go super broad and have like both versus Webflow, like for example, if we're using Webflow to create landing pages, do we want to do that?

**Daniel Lopes:** Or do we want to go broad even more in like the use case, like both versus Webflow or versus Retool for certain kinds of apps or use case level, you know, where like both versus level for web design, like both is like creating landing pages much better than the zero, for example, or like should we have an article for that or should we have very specific?

**Daniel Lopes:** And so that's another decision you're going to have to make.

**Daniel Lopes:** And yes, Monika, do you have, do you have any thoughts on, you know, the different approaches here if we...

**Mitchell Wright:** We kind of just try and get a lot of pages out and not do thorough fact checking on stuff or go slower.

**Mitchell Wright:** What are your thoughts there?

**Monika Rozanska:** Yeah, I mean, we want it to be accurate because the last thing we want is for that to be picked up and, you know, used against us as, know, accurate and correct information, but I'm also mindful of how we would keep that up to date with things that are changing so fast.

**Monika Rozanska:** And that kind of, like, makes me lean towards being a little bit more high level, granular, because if we start looking at every individual feature for every individual product, you know, keeping up to date can become a bit of a full time job.

**Monika Rozanska:** And in general,

**Monika Rozanska:** We can have a date on the website, on the page, saying up to this date, that's the report we have, you know.

**Monika Rozanska:** Yeah, no, I get that, but, you know, if this becomes out of date, even though we've said this is valid as of that date, that's still an outdated information on our website, which ideally we would want to keep as accurate as possible, because in six months time this could be become, you know, this could become something that we don't really lean on unless we're super on it, updating that content as each feature develops.

**Monika Rozanska:** But that's not to say that this is not helpful, it's just I'm trying to think of a way how this could serve its purpose without us having to live in that doc constantly.

**Daniel Lopes:** Is your concern on the on boats, like on the features on both sides to be accurate?

**Daniel Lopes:** Or the.

**Daniel Lopes:** Features on the competitor's side.

**Daniel Lopes:** It's both really.

**Monika Rozanska:** Well, from both perspectives, even more reasons for us to keep that up to date, because if we ship something and we don't add to that dog, we're missing that opportunity.

**Monika Rozanska:** So we'll definitely want to keep that up to date.

**Monika Rozanska:** And from the competitor's point of view, I think it's more of a question of us wanting to be very kind of accurate and making sure we're not providing incorrect information on competitors, because that could make us look, you know, a little bit shady if we are misleading our users on our competitors.

**Monika Rozanska:** So I would want us to be very, very cautious in terms of how we are positioning that.

**Monika Rozanska:** So it's not like us versus them, and we're actually not even being accurate in information we are providing.

**Monika Rozanska:** This is the kind of trust built.

**Monika Rozanska:** I agree.

**Mitchell Wright:** So I think just starting with what we kind of consider our most direct competitors and then being a little bit more particular about making sure that the claims there are accurate is probably the right move.

**Mitchell Wright:** Yeah, that makes sense.

**Daniel Lopes:** Yeah, we can definitely put somebody to do the review on everything and making sure claims are correct on both sides.

**Daniel Lopes:** And on our side, it's pretty easy to do.

**Daniel Lopes:** We can keep that Notion document up to date.

**Daniel Lopes:** And whatever you change, we can always recreate the articles based on that.

**Daniel Lopes:** And then we can figure out the system to not change the competitors or something like that.

**Daniel Lopes:** And if it's like 20 pages, it's fine.

**Daniel Lopes:** Like we can always do it hand.

**Daniel Lopes:** If it's 200 pages, we have to figure out how to automate some of this.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** hiçbir

**Daniel Lopes:** But I don't think you guys are thinking about going 200 pages for competitors.

**Daniel Lopes:** Does that make sense?

**Daniel Lopes:** We can figure out the volume on this for sure and figure out the process for fact-checking and review.

**Daniel Lopes:** So fact-checking here will be essentially to check a lot of this and we can figure it out.

**Daniel Lopes:** No, understand about it.

**Daniel Lopes:** No, he's heading out.

**Daniel Lopes:** Oh, OK.

**Daniel Lopes:** Yeah, that makes sense.

**Daniel Lopes:** We can calibrate on that after this meeting.

**Daniel Lopes:** And we can send to you the list of people.

**Daniel Lopes:** can start thinking about the articles.

**Daniel Lopes:** We can calibrate on the feature set as well.

**Daniel Lopes:** And then we can rerun the research based off those things.

**Daniel Lopes:** And then we can work on the articles.

**Daniel Lopes:** And then another stuff that we're doing is the stuff that you're doing, George, with Monika.

**Daniel Lopes:** And yeah, I think the short thing here is we've met with KJ and Monika.

**Daniel Lopes:** I'll next time.

**Daniel Lopes:** We have a good understanding of who the users are and what buckets they fall into, but we want to go two, three, or four levels deeper and really understand the language they're using, their specific pain points within those buckets.

**Daniel Lopes:** And that level of granularity is going to inform the language and stone and style we use in all of our materials and all of the projects.

**Daniel Lopes:** so talk to Monica about it, but we're happy to just add what we do on our customer discovery side.

**Daniel Lopes:** And work alongside her to do those user interviews and get that level of granularity that we think will benefit both of these projects.

**Daniel Lopes:** Yeah, like remaining for us in this case, it's like this.

**Daniel Lopes:** KJ?

**Daniel Lopes:** Yeah, KJ.

**Daniel Lopes:** Yeah, just want to jump in.

**KJ Krause:** Yeah, I didn't realize you were doing friction and pain point stuff.

**KJ Krause:** I have a couple more summary charts on users' specific frustrations that they mentioned in their prompting that I can add to that.

**KJ Krause:** Doc that I shared with you.

**KJ Krause:** That'd be fantastic.

**Daniel Lopes:** Thanks, KJ.

**Daniel Lopes:** Cool.

**Daniel Lopes:** So essentially, for us, this is super helpful on aligning on things like this.

**Daniel Lopes:** This is the kind of stuff we use in our prompts to generate the articles as the first best.

**Daniel Lopes:** And getting the interviews and getting how people talk about things helps us come up with this.

**Daniel Lopes:** But also, having your eyes on this document will help as well.

**Daniel Lopes:** So that's a refined version of the ones you had seen in the beginning.

**Daniel Lopes:** But I can send that over afterwards as well.

**Daniel Lopes:** Yeah, I think we covered everything.

**Daniel Lopes:** And when we were also going through this, we saw a few things that could be potential future ideas.

**Daniel Lopes:** For example, V2 has a ton of traffic on microapps.

**Daniel Lopes:** So they have stuff like RGB color picker.

**Daniel Lopes:** And you can essentially one-shot an RGB color picker that works really well.

**Daniel Lopes:** And we could have like a bunch of showcase microapps filled with...

**Daniel Lopes:** .

**Daniel Lopes:** .

**Daniel Lopes:** Both, and their traffic here is pretty, pretty good.

**Daniel Lopes:** This is what Retool has, for example, Company Logo Finder, CSV to JSON, RGB color beaker, Base64 encoder, and a bunch of little stuff.

**Daniel Lopes:** We tried some of these, and we get super close to almost production ready with both.

**Daniel Lopes:** So we could have a place in the future that's a catalog of microapps.

**Daniel Lopes:** So that's one of the ideas we saw based on traffic.

**Daniel Lopes:** Another thing that we saw that some of the other players doing quite a bit when they're checking their traffic was case studies on their blog.

**Daniel Lopes:** Like, for example, this one is from Lovable, because we were going to be doing interviews.

**Daniel Lopes:** We could extend the interviews to be about case studies and general articles about that, and we have the pipeline for creating the drafts.

**Daniel Lopes:** And then we could do editorial work to polish the interview result into an article format, and some of the other players are already done.

**Daniel Lopes:** Doing that, and we also saw that some of the stuff for jobs to be done that George can do, who could extend in the future because we know you guys are thinking about an academy and some other stuff.

**Daniel Lopes:** We could do interviews on user behavior and intent and help that calibrate the templates we build or the micro-attribute or whatever.

**Daniel Lopes:** And same thing with interviews for churn, so we could have the templates that would help you build full stack things.

**Daniel Lopes:** Maybe if people are churning because of back-end integration, could have the kind of stuff that KJ was talking about, have the next steps cover some of those things.

**Daniel Lopes:** And yeah, so that's just a few things that we saw when we were going through the research in the last two weeks.

**Daniel Lopes:** But that's the general state of everything.

**Daniel Lopes:** We are now in this week three and week four deliverables that we want to have.

**Daniel Lopes:** Now it's like we have to start creating, like thinking about the CMS, thinking about creating the pages, thinking about the data structure for the CMS.

**Daniel Lopes:** That…

**Daniel Lopes:** And where these things would go.

**Daniel Lopes:** So ideally, we would start talking about how we do the collaboration there.

**Daniel Lopes:** We could have a separate meeting if you want, but does that, like, in general, is that the direction of this or?

**Mitchell Wright:** Yeah.

**Mitchell Wright:** So we still have time, so I don't see a reason to push off talking about some of this stuff right now.

**Mitchell Wright:** So first thing I would say is this is great.

**Mitchell Wright:** I think, you know, a lot of good information here.

**Mitchell Wright:** One thing that we're thinking about is what the timeline looks like as far as, like, specific deliverables.

**Mitchell Wright:** And I understand that some of that stuff is dependent upon us.

**Mitchell Wright:** Like, internally, we're going through a bit of a website redesign.

**Mitchell Wright:** And as part of that, we might actually use Webflow for some of our marketing side stuff.

**Mitchell Wright:** So in that case, we would potentially use the Webflow CMS for this instead of what we had talked about previously, like Strappy or something.

**Mitchell Wright:** So that's one thing to consider.

**Mitchell Wright:** But at the same time, that website redesign could be something that takes a little while.

**Mitchell Wright:** So it may be a case where we kind of land on sort of the content and maybe we get like a high-level design and we can start generating things.

**Mitchell Wright:** But it may actually take like some weeks to go live until we get website redesign stuff done.

**Mitchell Wright:** You know what I mean?

**Daniel Lopes:** What if we come up, like I don't know what's the stack of your website today.

**Daniel Lopes:** Like we could do something without the CMS at all and we could generate static pages for your website first in whatever.

**Daniel Lopes:** Format that you guys have, and we have our grid, create the HTML, maybe you guys are using Tailwind or whatever, might be using the HTML and then the JavaScript code and whatever we need, and have one of our programmers send the full request into your marketing site or something like that.

**Daniel Lopes:** And then we have, it's going to be like low volume, and we're going to have to scrap these pages afterwards once you guys switch to workflow.

**Daniel Lopes:** And then we do the integration in CMS, but we'll at least have something up.

**Daniel Lopes:** We can have like maybe 10 pages up in this format for the comparisons, or maybe five, and we could have pretty fast the story kits as well.

**Daniel Lopes:** So, but then we'll have to switch up, you know what I mean?

**Daniel Lopes:** I don't know if that solves the problem, but just trying to figure out if can put something up in like a week or two, and then it's going to be like a...

**Mitchell Wright:** Sure, sure, sure.

**Mitchell Wright:** Yeah, so I mean, currently it's a Remix app, so that's totally possible for us to do something like that.

**Mitchell Wright:** I just wonder.

**Mitchell Wright:** If we're redoing a lot of work and if that's worth it.

**Mitchell Wright:** So we need to figure out on our side what the timeline would look like for that anyway.

**Mitchell Wright:** And then I think for some of these templates for the pages, I think the figmas that you guys have done are a good starting point.

**Mitchell Wright:** But we'd also probably want to run those past our designers to get their take on it so that it's just aligned with all of the brand and design styles that we're going to have there.

**Mitchell Wright:** So, yeah.

**Mitchell Wright:** So on our side, you know, I still need to go back and get some timelines and figure that piece out.

**Mitchell Wright:** But on your side, I'm more just curious what it looks like for having some initial set of pages for us that if we had everything set up on our side, we could pull into a CMS or build out as a static page or whatever.

**Daniel Lopes:** Yeah, like for us, like setting up the, getting the integration, we could even set up like an integration Webflow on like a staging account and start putting the data there.

**Daniel Lopes:** Like we have a few clients that use Webflow, we have integration with Webflow and we can create the collections and everything there.

**Daniel Lopes:** So we could have all the data put in the CMS and you guys, like later we can just export from the staging Webflow we might be using, you guys import into yours.

**Daniel Lopes:** And, and, and then we can, we can have like, we don't have a lot of web design in house.

**Daniel Lopes:** We have a couple of people that can do it pretty well and they're allocated to another, but they will be available in one week.

**Daniel Lopes:** And we also have agencies we work with and we could allocate them to your project.

**Daniel Lopes:** If you guys don't have the time to do the pages, but if you just, we could start just putting stuff in Webflow, a staging account that we can mess with it.

**Daniel Lopes:** And then you guys, we can like help you transition to the final one production.

**Daniel Lopes:** Is that?

**Daniel Lopes:** Yeah.

**Mitchell Wright:** That could work, yeah.

**Daniel Lopes:** Yeah, because the CMS stuff for us, like, so much time goes into, like, getting the page right and, like, having the client design team work with whatever we're putting in the page.

**Daniel Lopes:** And then, like, that takes away from actually, like, iterating on the workflows and making the language right and publishing volume.

**Daniel Lopes:** So, like, if we can just, like, do the CMS stuff now, that would be, like, especially guys who go on Webflow and we have full experience, that's easy for us.

**Daniel Lopes:** Cool.

**Mitchell Wright:** Cool.

**Mitchell Wright:** Okay, that works.

**Mitchell Wright:** And then, Monika, what else did we talk about this morning?

**Monika Rozanska:** So, for me, probably the key priority is to have a page with templates.

**Monika Rozanska:** Let's...

**Monika Rozanska:** Let's...

**Monika Rozanska:** Also, slash, we would want to start our users submitting their own projects into that page, and it feels like the templates that you guys created would be a good starting point for that page.

**Monika Rozanska:** So we've got some content there, and then we could set up a system where users can submit their own stuff, and we can curate it and select what else we want to add.

**Monika Rozanska:** So that would be a way of combining those two quite nicely, and I'm still not sure whether we'll have that as one kind of big project where we've got templates and that's where they live, or whether that would be in addition to those kind of more marketing-focused pages that maybe, like, Mitchell wants to use more from the, like, SSO point of view.

**Monika Rozanska:** So I don't really know how that would, like, look from, like, our web and design point of view.

**Daniel Lopes:** So that's kind of how...

**Mitchell Wright:** EZero does it.

**Mitchell Wright:** They have like, you know, all these community things, but a majority of those are actually made just by employees.

**Mitchell Wright:** There's only a handful that are actually external.

**Mitchell Wright:** But I think, you know, this sort of bootstraps that process or whatever, and then having a way for them to, for community members to submit their own stuff that we could look at and curate.

**Mitchell Wright:** And it sort of creates this flywheel of, now we have this UGC that is also bringing in additional templates and pages for us that we're not having to generate ourselves.

**Mitchell Wright:** One thing that EZero doesn't do is that they don't enrich the content at all.

**Daniel Lopes:** So even their own stuff, you see like ShedCN folks doing like their internal for sale people doing stuff, and there's like no data on that page.

**Daniel Lopes:** So we could get, do the curation that we're talking about, do the UGC stuff, and then we can enrich those pages with SEO in mind.

**Daniel Lopes:** Yes, exactly.

**Mitchell Wright:** think, I think that's great, because right, they can give us, you know, the template, maybe like some.

**Mitchell Wright:** Small description, but then we can really expand on that via some of these workflows you all have already built.

**Mitchell Wright:** Right, exactly.

**Mitchell Wright:** Yeah.

**Daniel Lopes:** Cool.

**Monika Rozanska:** I'll also see it, which I think would be really good for our community, is having a way of people actually, you know, interact with the creator.

**Monika Rozanska:** So like commenting section, you know, it would be good if we could have that as a place where people also get some work from, get hired.

**Monika Rozanska:** So if somebody likes some of those pages, they can actually contact the creator and they can make some money through this exercise.

**Monika Rozanska:** So it not only drives traffic to their pages, but also it incentivizes submitting good quality content.

**Daniel Lopes:** Like that's funny.

**Daniel Lopes:** One of our recruiter just went to finding a bunch of people that is really good at coding and stuff because we wanted to hire a few.

**Daniel Lopes:** And like having, like having in there that doesn't exist.

**Daniel Lopes:** So like we're.

**Daniel Lopes:** Trying to find people in a lovable community and be zero, and trying to find who is doing this kind of stuff, and doing that as a feature on a website would be amazing.

**Daniel Lopes:** We would have hired people from that.

**Daniel Lopes:** Yeah, exactly.

**Monika Rozanska:** We've got a partnership with Contra, where we do exactly that.

**Monika Rozanska:** We've got our bold experts.

**Monika Rozanska:** So those are the people we would send our customers if they need help building something, whether it's from scratch or whether figuring out certain integrations that go beyond the scope of our support.

**Monika Rozanska:** So it's probably, it will be a good place, in addition to what we've got in Contra, for those creators to showcase what they've already done, and for people to not be able to use it as an inspiration, but also interact with those creators.

**Monika Rozanska:** So it's just another place for the community to come together.

**Monika Rozanska:** Be good to think about it as we are laying down the foundation and setting things up to make sure that where we've got in place would support this kind of, you know, level of interaction.

**Monika Rozanska:** Yeah, that makes sense.

**Daniel Lopes:** Yeah, that's something we were thinking about in the beginning, but I didn't know where that would fit in your roadmap.

**Daniel Lopes:** So it's very cool that you're thinking about that.

**Daniel Lopes:** Let me see if there's anything else we have in the agenda that we need to talk about.

**Daniel Lopes:** Like, after this meeting, like, we talked about so many different things.

**Daniel Lopes:** I'll send you, like, a bunch of requests and, like, our plan on our end.

**Daniel Lopes:** And I don't think we're blocked on anything.

**Daniel Lopes:** It's more like whatever you can help will just make things better.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Is there anything else that you guys want to cover?

**Mitchell Wright:** Yeah, mean, think, like I said, the main thing is just trying to get some kind of timeline on when we would actually have, like, first versions of things for us to look at and give.

**Mitchell Wright:** Feedback on as far as templates or comparison page content that we can get other people internally on our side to look at things and give their feedback and start that process.

**Mitchell Wright:** And then, you know, I'll go back and figure out what the hosting page building situation is going to be.

**Mitchell Wright:** Sounds good.

**Mitchell Wright:** Yeah.

**Mitchell Wright:** like, how about this?

**Daniel Lopes:** Like, this week, we can pick a handful of competitors ourselves.

**Daniel Lopes:** Like, there's the obvious ones like Lovable and V0.

**Daniel Lopes:** There's Cursor.

**Daniel Lopes:** Like, there's a supporting one versus the direct competitor.

**Daniel Lopes:** We can pick, like, five.

**Daniel Lopes:** And then we create the articles.

**Daniel Lopes:** We have our editorial team, like Mariana and everyone else, help review that.

**Daniel Lopes:** And then we can send that to you probably tomorrow or Friday, like, five articles.

**Daniel Lopes:** And same thing for the templates.

**Daniel Lopes:** I can send you, like, a few templates and some of the...

**Daniel Lopes:** It's particular

**Daniel Lopes:** I can send, like, maybe five or ten templates and supporting articles.

**Daniel Lopes:** You can send that in, like, a Notion format or something like that.

**Daniel Lopes:** And then in the meantime, we'll figure out the Webflow setup, and maybe next week we can have the integration from our workflows to making API calls to Webflow and adding stuff to a staging Webflow account that we create ourselves.

**Daniel Lopes:** Yeah, and on our side, you know, no rush on there.

**Mitchell Wright:** I don't think we'd be able to look at anything until Monday, even at the earliest, because we're still at our offsite and stuff planned.

**Mitchell Wright:** People are traveling Friday.

**Mitchell Wright:** so, yeah, so no rush on that.

**Mitchell Wright:** But yeah, by Monday would be fantastic.

**Mitchell Wright:** Sounds great.

**Mitchell Wright:** Right.

**Mitchell Wright:** Worth it.

**Monika Rozanska:** And just to maybe kind of make sure that we're aligned on the priorities, we've got our hackathon starting end of this month.

**Monika Rozanska:** So in case this changes anything for you guys, so I know you will be doing some user research.

**Monika Rozanska:** So that's good data for us to have as we're digging into that kind of more narrower ICP.

**Monika Rozanska:** Probably not critical right now for that hackathon piece.

**Monika Rozanska:** It would be good to have those templates at the door for that.

**Daniel Lopes:** What's the date again for the hackathon?

**Monika Rozanska:** May 30th?

**Mitchell Wright:** Yeah, it starts May 30th and it goes for a whole month.

**Monika Rozanska:** It feels like it will be a good resource for users to tap on.

**Monika Rozanska:** So if we double down on that and maybe deprioritize user interviews, if that would allow us to move quicker, that would probably be our preference.

**Daniel Lopes:** Yeah, because maybe we could put something up just for the hackathon, for the people that will be doing the hackathon, like looking at the templates and things like that.

**Daniel Lopes:** It doesn't have to be the final form, you know.

**Daniel Lopes:** Just have a starting point for those.

**Monika Rozanska:** Exactly, starting point, know, inspiration, kind of idea generation plays, prompting good practices and stuff like that, wherever we could get out.

**Monika Rozanska:** The door for people to be able to just go there and, you know, get the ideas flowing or if they're stuck on anything, that's a good place to start, especially for the beginners.

**Monika Rozanska:** That would probably help us immensely.

**Monika Rozanska:** Yeah, we can totally do that.

**Daniel Lopes:** That's cool.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Anything else?

**Daniel Lopes:** I think that sounds great and that, yeah, that works for us.

**Mitchell Wright:** Awesome.

**Mitchell Wright:** All right.

**Daniel Lopes:** Thanks, everybody.

**Daniel Lopes:** This has been a fun project so far, especially for me just creating all the prompts and like super cool.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Anything you have to send it over.

**Daniel Lopes:** I will send you a bunch of stuff after this call and expect the articles on Monday at latest.

**Daniel Lopes:** Okay.

**Mitchell Wright:** Sounds great.

**Mitchell Wright:** Thank you all.

**Daniel Lopes:** All right.

**Daniel Lopes:** See you.
