# Pod stand-up

<metadata>
date: 2025-08-01
time: 13:16 UTC
duration: 27 minutes
organizer: Saskia Wartnaby
participants: Darrell Etherington, Carrie Chowske, Ehtisham Hussain, Saskia Wartnaby, Joe Sovar, Feyisayo, Matthew Alves-Hill, Jenny Macrohon Dabon, Jürgen Linde, Jessica Nicole Manificiar Gayo
fathom_recording_id: 77933482
fathom_url: https://fathom.video/calls/367828797
share_url: https://fathom.video/share/Dm4zSfk2sJMDSvb-VMYgb4w-c1Mrs8TJ
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX's content pod onboarded two new clients—Airbyte (100 refreshes/week, in Expansion phase) and Sunbit (25 articles/week, already self-publishing, strong product fit)—while aligning on a major product shift: the assignment direction redesign will consolidate brief and outline into one interface and de-prioritize SEO keywords as a primary generation input, reflecting a broader philosophical move toward human-centric, usability-focused content over SERP optimization. The team is experimenting with Claude and Atlas hybrid workflows, with Claude consistently outperforming Atlas on tone and readability, and Darrell introduced the concept of a "content help desk"—guided prompting via query chains—to lower friction for less experienced users while maintaining output quality.

---

## Context

This is GrowthX's weekly pod stand-up, an internal team sync led by Darrell Etherington. The meeting brings together the content creation and product teams to align on client onboarding, operational updates, and feedback on product development. The pod operates as a delivery-focused group managing high-volume content generation for clients like Airbyte and Sunbit, while also providing input into product improvements being designed by the engineering team (including new assignment direction workflow and SEO integration strategy).

---

## Relevance

**To GrowthX Delivery:**
- Sunbit onboarded as a high-volume fit (25 articles/week) with independent publishing—validates GrowthX's ability to service enterprise-scale content production
- Airbyte entering Expansion phase with 100 weekly refreshes—requires operational scaling of refresher pipeline
- Team experimenting with hybrid Atlas/Claude workflows to improve content quality—early data shows Claude outperforms Atlas on tone and readability
- Modified refresher pipeline at Airbyte (batching strategy) now optimized for single-run bulk processing—useful pattern for other clients

**To GrowthX Business Development:**
- Sunbit demonstrates strong product-market fit: they self-publish our output, have high satisfaction, and are actively expanding scope to multiple verticals (dental, automotive, home services)
- Both new clients came from Sprint program expansion (Airbyte) and warm referrals (Sunbit via Hashem)—indicates program model working as client acquisition engine

**To Product/Engineering:**
- Assignment direction redesign: consolidating assignment brief and outline; de-prioritizing SEO keywords as input while maintaining them as secondary output for client-facing documentation
- Philosophical shift in content strategy away from SERP-optimization-first toward human-centric, usability-focused content—aligns with LLM-first world
- Team feedback: Atlas struggles with tone and writing guidelines vs. Claude; agentic pipelines showing promise for Airbyte refreshes
- Proposed "content help desk" workflow (guided prompting via query chains) to lower barrier for less experienced users—could be product differentiator

---

## Overview

- New clients Airbyte (100 refreshes/week from Expansion phase) and Sunbit (25 articles/week, self-publishing, excellent product fit)
- Assignment direction redesign: consolidating assignment brief and outline, de-prioritizing SEO keywords as primary input
- Team experimenting with hybrid Claude/Atlas workflows; Claude outperforms on tone and readability
- Philosophical shift toward human-centric, usability-focused content vs. pure SERP optimization
- Proposed "content help desk" for guided, scaffolded content creation to improve accessibility for less experienced users

---

## Key Topics

### Calendar and Publishing Updates

  - Calendar incident: Matthew accidentally deleted and restored team events
  - New pod-specific calendar invites sent out
  - Automated publishing workflows being developed by dev team
  - CMs/MEs to include walkthroughs in ticket links for client publishing

### New Client Updates

  - Airbyte: New client from Sprint to Expansion program
      - Currently doing 100 refreshes per week
      - Using modified refresher pipeline for efficient updates
  - Sunbit: New non-Sprint client
      - Requesting 25 articles per week
      - Publishing content independently
      - Good fit for GrowthX's high-volume capabilities

### Content Generation Strategies

  - Team experimenting with combining Atlas pipeline and Claude for better results
  - Carrie developed a workaround using refresher pipeline and Claude
  - Saskia finding better results with Claude compared to Atlas for content generation
  - Discussions on improving Atlas's writing style and tone

### Product Improvements

  - Assignment direction being redesigned:
      - Combining assignment brief and outline
      - Reducing emphasis on SEO keywords in initial content generation
      - Considering a "content help desk" approach for guided content creation
  - Team providing feedback on product issues and suggestions for improvement

### SEO and Content Strategy

  - Philosophical debate on the role of SEO in content creation
  - Trend towards more human-centric, usability-focused content over strict SERP optimization
  - Discussion on balancing SEO considerations with readability and user experience

### AI Tools and Workflow Optimization

  - Exploration of using AI agents for tasks like Webflow site building
  - Potential for using AI to streamline Airtable workflows and interface creation
  - Team encouraged to experiment with AI tools for process improvement

---

## Action Items

**Darrell Etherington (GrowthX)**
- Share HubSpot CMO interview video in Slack for team visibility — discusses alignment with product philosophy on human-centric content

- Experiment with OpenAI agent to build client-facing Airtable interface for workflow automation

**Ehtisham Hussain (GrowthX)**
- Generate Airbyte outlines using both Atlas and Claude pipelines, compare results, and submit best version by Friday; message client with framing of new approach as latest improvement

---

## Transcript
**Darrell Etherington:** Hey, everyone.

**Darrell Etherington:** How's it going?

**Darrell Etherington:** We had a fun calendar-related incident this week where Matthew Alves-Hill deleted everybody's calendar events and then restored them all, but it was fine.

**Darrell Etherington:** It happened overnight.

**Darrell Etherington:** Nobody noticed.

**Darrell Etherington:** Seamless.

**Darrell Etherington:** I wondered what those emails were about.

**Saskia Wartnaby:** I just felt like, this meeting has changed.

**Darrell Etherington:** Yeah, he just mistakenly, he thought he was logged in with his account, but he was logged in with the team account, which I've done many times as well.

**Darrell Etherington:** So definitely not best practices to just have the team account out there, but we're young.

**Darrell Etherington:** We'll learn eventually.

**Darrell Etherington:** On that subject, hopefully, let me know if anybody still needs to get the specific pod thing invited.

**Darrell Etherington:** I think I sent out all the invites that were requested, and I don't know that we have all of them back yet from the client side, but hopefully those will continue to come.

**Darrell Etherington:** And then the other update on that front is just the tickets thing, because they do want the walkthrough.

**Darrell Etherington:** So I figured the CMs or the MEs who are doing the publishing should do that, because they can include the walkthrough in the ticket link.

**Darrell Etherington:** And then, so that one will solve.

**Darrell Etherington:** I mean, Suleiman will use the different logins for different publishing platforms to avoid even, he can do multiple at the same time, right?

**Darrell Etherington:** But he'll be doing that, and then we've also got API keys to a bunch of the people, to the dev team.

**Darrell Etherington:** So those automated publishing workflows they're working on, both this week, they've done a bunch, and then next week, that's the focus of this two-week dedicated sprint.

**Darrell Etherington:** So hopefully a bunch of those will be done, too, which will be interesting, because, I mean, then we'll have to put the output back in the flow to do the publication, if we're taking it out to do corrections and modifications, and sometimes net new generation on the cloud page, but minor inconvenience.

**Darrell Etherington:** Versus trying to set the stuff up yourself, right?

**Darrell Etherington:** Okay.

**Darrell Etherington:** Those are the big updates I had.

**Darrell Etherington:** Well, we have a lot of client stuff, so I'll just provide some updates there because we have a new client, Airbyte, that was just added.

**Darrell Etherington:** They were in Sprint and then Sprint to Expansion, I think they did.

**Darrell Etherington:** So that's coming on to our docket.

**Darrell Etherington:** We just had a handover meeting, which Carrie can talk more about because I wasn't able to make it because I had a conflict, but we'll have another one.

**Darrell Etherington:** And more and more new clients to come as they come off of Sprint.

**Darrell Etherington:** But we also added Sunbit, which was not a Sprint client, just a good shape handoff client.

**Darrell Etherington:** They're very happy with us at Hashem.

**Darrell Etherington:** You can say more if you want, but I feel like that's a good steady state relationship at the moment.

**Darrell Etherington:** Yeah, you go first.

**Ehtisham Hussain:** They're like a classical example of a good fit client for us because they want 25 articles per week and that kind of high volume I don't think anyone else is going to give them. Plus, they're happy with the output. They're publishing on their own, which I didn't know yesterday. She moved a bunch of articles to ready to publish during the meeting, and I thought I was handling it, but apparently we are not publishing for them.

**Ehtisham Hussain:** But other than that, they're a perfect example of the kind of customer that's a good fit for GrowthX, and GrowthX is a good fit for them.

**Darrell Etherington:** I think they're because their expectations are aligned to like the type and quality of output we can do.

**Darrell Etherington:** They help it helps that they're not a very technical product at all.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** And essentially, what is it called?

**Darrell Etherington:** Payment splitting for services for expensive big ticket things like dental work.

**Darrell Etherington:** Dental work is, I think, one of their number one.

**Darrell Etherington:** And then automotive is another one, too.

**Darrell Etherington:** Right.

**Darrell Etherington:** But there's tons of categories for that.

**Darrell Etherington:** They can, as we've seen in the news, they can go further down market.

**Darrell Etherington:** Like, did anyone see the Instacart thing?

**Darrell Etherington:** That was a big story maybe like a month ago, two ago.

**Darrell Etherington:** Instacart made a deal with one of them where they were splitting, like, pay over time for food delivery, which was like a recession indicator, probably.

**Darrell Etherington:** But yeah, they have a lot of room to run.

**Darrell Etherington:** So hopefully, we'll be a good client for a long time to come.

**Darrell Etherington:** And just a pleasure to work with, too, both the primary stakeholders on that one.

**Darrell Etherington:** Airbyte, Carrie, you want to give some background on that?

**Carrie Chowske:** The video was lagging, so I turned it off.

**Carrie Chowske:** I'm not sure what's going on.

**Carrie Chowske:** Anyway, I don't have any more information on Airbyte yet.

**Carrie Chowske:** They're doing 100 refreshes a week.

**Carrie Chowske:** Wow, okay.

**Carrie Chowske:** Made both me and Joe laugh.

**Carrie Chowske:** Andy tagged Joe in on that as CM.

**Carrie Chowske:** I just didn't know if Jenny has been reassigned fully to something or if she's going to float long term.

**Carrie Chowske:** No, that's probably just an Andy visibility issue.

**Darrell Etherington:** I can stick with her on our current distribution and then figure out how we should right-size that.

**Carrie Chowske:** I moused over the pod B list in my email the other day. Is Jenny on it? I noticed she wasn't showing up.

**Darrell Etherington:** She's not. Let me add her now.

**Carrie Chowske:** Thanks, I just remembered when you mentioned her.

**Carrie Chowske:** Airbyte's situation was pretty unclear. I talked with Jacob about it. He had done a long-term strategy plan for them before they went back to Sprint, and they were happy with it. But then they decided to do the strategy Sprint, which is when they shifted to 100 weekly refreshes. They're just about done with those refreshes—we probably have just two or three more weeks of them. After that, it's unclear whether they'll return to the original strategy Jacob outlined or do something different. We'll need to figure that out once the refreshes wind down.

**Darrell Etherington:** We'll need to come up with a plan for what's next. I also had a chat with Ada yesterday about Airbyte.

**Joe Sovar:** She told me that the Airbyte team didn't spend much time on those 100 refreshes. They use the same prompt for every article in the article direction and just run it. They've modified their refresher pipeline, and apparently it works well.

**Carrie Chowske:** That might be something for the rest of us to look at too.

**Carrie Chowske:** I'm I, I, I kind of.

**Carrie Chowske:** created like a workaround.

**Carrie Chowske:** was playing with, I think I shared this with you, Daryl, and I know I shared it with Feyi.

**Carrie Chowske:** might have, did I share it with you, Joe?

**Carrie Chowske:** Basically what I did was I used the refresher pipeline, and then I also asked Claude to do the same stuff, and then kind of said, okay, now what's different?

**Carrie Chowske:** Okay, well, now take the best of both and do that, and it worked pretty well.

**Joe Sovar:** You sent me an example of what you did, I think, with Towner Engine, so I can try on your code, but I didn't try it yet.

**Joe Sovar:** Yeah, yeah.

**Joe Sovar:** It's in the engine project on Claude, if anybody wants to see it.

**Carrie Chowske:** I can dig it up, but it's, it was, I basically kind of, and I used some of the same direction in the instructions for our refresher pipeline too, because again, it doesn't go to, it doesn't use the writing guidelines, so I gave it the writing guidelines.

**Darrell Etherington:** was like, use these, you know?

**Darrell Etherington:** Wait, our pipeline, you did that, or you did that in class?

**Darrell Etherington:** I did.

**Darrell Etherington:** That in Atlas and in our pipeline.

**Carrie Chowske:** So I just put it in the instructions, like the refresh instructions.

**Darrell Etherington:** I'm not sure how well it worked.

**Carrie Chowske:** I mean, it kind of, I don't know, I feel like our pipeline still struggles a little bit with the writing with our writing guidelines.

**Carrie Chowske:** More so than Claude, I think Claude gets the tone of voice better than than using Atlas does still, but yeah.

**Carrie Chowske:** But in general, like there wasn't a lot of difference.

**Carrie Chowske:** It was all tone of voice stuff.

**Carrie Chowske:** So giving it more information at that beginning stage or just giving it the link and telling it what you're trying to do, like telling it, here's what I want to change.

**Carrie Chowske:** Here's what I don't want to change.

**Carrie Chowske:** It does.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Like it's not awful.

**Carrie Chowske:** So it is workable.

**Carrie Chowske:** And then kind of the same strategy we're using with all of our other articles with, you know, telling Claude, like, hey, make this better.

**Carrie Chowske:** Right.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** I'm looking at the pipeline for the ones for Airbyte to try to determine what's different.

**Darrell Etherington:** And they also

**Darrell Etherington:** Divide them by batches, which is interesting.

**Darrell Etherington:** Well, they were doing that initially, I think, because they were, there's, I saw somewhere where they talked about it.

**Carrie Chowske:** was either because, I can't remember, but it was either because they were still making changes as they were going.

**Carrie Chowske:** So they were doing new pipelines for them each time because they had to keep making, they didn't want to, like, overload it.

**Carrie Chowske:** But they said now it should be good to do them all in one.

**Carrie Chowske:** Oh, okay, okay.

**Carrie Chowske:** So it's not actually.

**Carrie Chowske:** Yeah, it's in one of the videos that they gave us access to.

**Darrell Etherington:** I don't know.

**Darrell Etherington:** But that's all good feedback, Carrie.

**Darrell Etherington:** I'm about that, like, process for Eng team because they, I know that they want to do the refresher, but they just haven't gotten into it yet.

**Darrell Etherington:** And so I will provide them that.

**Darrell Etherington:** Maybe I'll just call them this call or whatever, but so that they can incorporate that.

**Darrell Etherington:** We had a good chat this week about assignment direction with the new product manager. Kirkland is taking on a project to redo that. He's going to consolidate the assignment brief and outline into one thing.

**Darrell Etherington:** And they will, you will be able to have much more influence on it.

**Darrell Etherington:** And the other thing I think that we all aligned and agreed to was that it will not take as input.

**Darrell Etherington:** It will still produce the SEO information as an output, like as part of the step, it'll say, oh, here's the keyword stuff here, the targets, whatever, so that we can use that to populate the client-facing documents if they want, if they're curious about, like, why we're targeting this keyword or what the volume is or whatever.

**Darrell Etherington:** But it won't take that into strong consideration in the generation of the article thing.

**Darrell Etherington:** Previously, the pipelines used keyword SEO analysis as their primary guiding factor. Now it will consider SEO only secondarily or not at all, so it won't just be trying to produce a 4,000-word SERP-winning thing. We had a philosophical debate about whether that's actually what we want to do.

**Darrell Etherington:** And like, it was the, we've had a discussion with clients a bit too.

**Darrell Etherington:** Like, you can aim to win SERP, but do you want that or do you want to aim to win usability and readability?

**Darrell Etherington:** Or like, you know, what is your preference?

**Darrell Etherington:** Especially in a world where LLM stuff is more important and in theory that tracks closer to like human readability.

**Darrell Etherington:** In theory, why are we doing all this keyword research only to ignore it once we throw it into the pipeline?

**Carrie Chowske:** Before, it was highly prioritizing keywords. We'd choose a keyword and run it through the pipeline, but the pipeline would want to use a different keyword. We'd have to argue with it, and even when we changed it, it seemed to create more work for us than it helped.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Well, I mean, it ended up being a, it's a fun call.


**Darrell Etherington:** There's a big philosophical debate between me and Jason about what is the value of SEO and where should it lead. I'm of the opinion that SEO should follow. If you try to start with SEO as a guiding factor, you won't get anywhere except behind. Carrie and I were talking yesterday about how marketing is going more old school, almost like focus groups—thinking about how someone would actually search, thinking about the human element instead of just keywords. Going forward, you definitely can't just rely on the SEO part.

**Darrell Etherington:** And it should be a differentiator for us versus other content marketing products and AI tools. I did an interview with the HubSpot CMO that talks a lot about this stuff—I'll share it in Slack if people are curious. It indicates where the product is heading.

**Darrell Etherington:** The key ingredient we need to unlock is getting the product working well, and then everything else will fall into place. Does anyone have problems, trouble, or big things to flag? Like Carrie was pointing out with the pipelines, if you've noticed anything about the product, even if it's small, this is a good time to share it.

**Saskia Wartnaby:** I've been using the artifacts you gave me in the Claude project, and it's producing really great results with minimal input. I can adapt it a lot quicker than in Atlas. The way Atlas writes is awful to me—very cocky and straightforward, different from what I want and what Claude does. I'm relying on Claude mostly, but I'm still running Atlas pipelines and comparing. Sometimes the Atlas outlines are good, but the writing isn't great, so I take the outline and give it to Claude.

**Darrell Etherington:** Are you running any of the agentic pipelines? Only Town has an agentic pipeline right now.

**Saskia Wartnaby:** I'm just using whatever's there—I think the article new one, the normal one.

**Saskia Wartnaby:** Matthew is expanding the changes they're making, and I'm excited to see those in action. I want to argue with Atlas the way I argue with Claude—I can produce something better a lot quicker with Claude because of how it works.

**Darrell Etherington:** It's the Socratic method—I suggested that for the assignment redesign. Some people aren't good at prompting, so we don't want open-ended prompting. But instead of bounding it, we could use a guided flow—a waterfall where the machine asks "What do you want to do?", you answer, and then it asks "I need this information from you." It's a chain of queries that elicits what you need. Like a content help desk.

**Saskia Wartnaby:** Exactly.

**Saskia Wartnaby:** It's like a CX decision tree. I just named the product "content help desk."

**Carrie Chowske:** That's a great name.

**Ehtisham Hussain:** Don't get too good at things because then you end up doing everything.

**Carrie Chowske:** Jen said I'm the queen of Airtable, but really I'm the queen of the workaround—Airtable is just the tool I was using that day.

**Darrell Etherington:** This is an interesting thing I'd like to try. On a client call, a stakeholder mentioned he uses an OpenAI agent to build Webflow sites. It reads the docs, figures out the WYSIWYG editor, and builds the website.

**Darrell Etherington:** Airtable has built-in AI. Is it good?

**Carrie Chowske:** It's pretty good. I've used it for automations, and it's really good at cross-referencing tables—"if this, then that" kind of logic. It's decent, but it wouldn't handle how complex things can get.

**Darrell Etherington:** You could try having an agent build a client-facing Airtable interface by describing exactly what you did in detail. You'd need to give it your auth, but those credentials expire, so it should be okay. It logs into Airtable as you and can manipulate at the same level you can. It's an interesting experiment to try.

**Carrie Chowske:** I see all the branches and know it can be done, but organizing them is hard for my brain. AI is really helpful because I've always known: if you have the data, you can do this. It can be done. Why hasn't anybody done it? So I just do it myself.

**Darrell Etherington:** Agents are very good at organizing your thoughts and creating an architecture for execution that reflects what you want, even if you can't clearly articulate it. Happy Friday. Ehtisham, do you have more?

**Ehtisham Hussain:** What's our next move for Airbyte?

**Darrell Etherington:** I set up the Claude project as comprehensively as I can right now. We'll use it as a final correction polishing step. You can experiment with generating outlines first. Let's do that given our timeline. Use the Claude project or Atlas to generate outlines, bake off to see which is better, and submit by Friday for their consideration next week. Run the articles with both, then do final fact-checking in the Claude project using the knowledge base they provided. I also have Claude do code review—check all code snippets are correct. That's the plan for Airbyte.

**Ehtisham Hussain:** Should it go out with a custom message from me explaining this is new?

**Darrell Etherington:** Yeah, frame it as new and our latest and greatest. That might have a psychological effect. On their side, Apurva is the key person to convince—Dan will follow whatever Apurva thinks. Apurva had qualitative feedback, not quantitative. So the perception that we're doing something new and very different might influence them. Just articulate that we're doing this new approach.

**Carrie Chowske:** Joe, did we hear back from Jessica on that last article for this week?

**Joe Sovar:** It's the one with the survey template, and I'm waiting for her to comment on whether it's ready to go or needs revision, so I know whether to move it to ready to stage or revise.

**Carrie Chowske:** Let's buzz her.

**Darrell Etherington:** Great. Enjoy your Friday and weekend. I'll be back Tuesday—Monday is a Civic Holiday in Canada.

**Saskia Wartnaby:** That's nice. We had a public holiday this month but it falls on a Saturday, so no Monday off for us.
