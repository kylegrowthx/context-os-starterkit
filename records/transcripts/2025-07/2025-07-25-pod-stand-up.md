# Pod stand-up

<metadata>
date: 2025-07-25
time: 13:16 UTC
duration: 24 minutes
organizer: Saskia Wartnaby
participants: Darrell Etherington, Carrie Chowske, Ehtisham Hussain, Joe Sovar, Feyisayo Odedeyi, Saskia Wartnaby
fathom_recording_id: 76488147
fathom_url: https://fathom.video/calls/361797493
share_url: https://fathom.video/share/4gPUmqD92bNxJZXi5R8xaqTUyEMZqk2x
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX's delivery pod ended its engagement with Aftershoots (poor client fit) while pivoting to use Claude AI for more effective article generation and editing alongside Atlas. The team discussed workflow improvements across multiple clients, including new clients coming on board (Sunbit) and publishing automation challenges with Yurco's Prismic system. Key focus is on building internal capabilities with Claude, Gemini, and O3 for faster iterations while Atlas improves its core product offerings.

---

## Context

The pod stand-up is GrowthX's weekly team synchronization for the delivery organization. This July 25 meeting included six core contributors managing client deliverables across multiple accounts. Darrell Etherington leads the delivery pod, recently returned from San Francisco where he met with the engineering team about publication automation and other product initiatives. The meeting covers client transitions (Aftershoots exit, Sunbit onboarding), workflow optimization for article generation, and publishing challenges blocking team efficiency.

---

## Relevance

**To GrowthX Delivery:**
- Aftershoots exit demonstrates ability to end poor-fit partnerships cleanly (40-article reduced scope through August close)
- Claude AI driving significant quality and speed improvements in article generation compared to Atlas alone; team successfully using Claude for writing guideline adherence and content refinement
- Gemini showing value for technical content (Aimbid project) and Google Docs integration for quick edits
- O3 proving effective for complex multi-step reasoning tasks (studio head using it for video analysis with 80% accuracy on B-roll identification and timestamps)
- Atlas agentic workflow (used by Town) much better than default; internal linking needs vector database to compete with external tools

**To GrowthX Business Development:**
- Sunbit coming on board with two-week temporary takeover then permanent shift to GrowthX (Ehtisham managing portfolio)
- Aftershoots client fit issues highlight need for clearer ICP screening upfront; reduced engagement shows GrowthX prioritizing partnership health over revenue
- Team expanding AI prompting expertise and knowledge-sharing culture reduces bottlenecks and improves team retention

**To Publishing & Automation:**
- Yurco/Prismic automation blocked: GrowthX user lacks publishing authority, and Prismic doesn't support API-based publishing even with proper permissions; manual review still required despite automation desire
- Engine publishing automation in Linear (ticket queued for Suleiman to gradually take on)
- Prophecy articles require manual scheduling until automation pipeline complete (Saskia priority)
- Pipeline-based publishing (JSON format instead of copy-paste from Google Docs) may fix Yurco's broken link preview issue

---

## Overview

- Aftershoots engagement ending due to poor fit; team to deliver reduced scope of 40 articles by end of August
- Team encouraged to use Claude AI in parallel with Atlas for better article generation and editing
- New clients (e.g., Sunbit) coming soon; Ehtisham to manage Sunbit portfolio
- Publishing automation and workflow improvements in progress, including potential API integration for Yurco

---

## Key Topics

### Client Updates

  - Aftershoots engagement ending:
      - GrowthX's decision due to poor client fit
      - Reduced scope: 40 articles by end of August
      - Demonstrates GrowthX's ability to end non-beneficial partnerships
  - New client Sunbit coming on board:
      - Two-week temporary takeover, then permanent shift to GrowthX
      - Ehtisham to manage Sunbit portfolio

### Workflow Improvements

  - Team encouraged to use Claude AI alongside Atlas:
      - Claude more effective at applying writing guidelines and making specific changes
      - Gemini useful for technical content (e.g., Aimbid project)
      - Google Docs integration with Gemini for quick edits
  - Atlas improvements in progress:
      - Agentic workflow showing promise (used by Town)
      - Need for final proofreading/quality checking step
      - Potential vector database implementation for better internal linking

### Publishing and Automation

  - Suleiman to gradually take on publishing tasks across clients
  - Prophecy articles: Saskia to schedule manually for now
  - Engine publishing automation in pipeline (ticket created)
  - Yurco/Prismic publishing:
      - API integration impossible due to lack of publishing authority
      - Manual review still necessary
      - Potential for improved link checking through pipeline integration

### Team Collaboration and Learning

  - Encouragement to share prompting techniques and learn from each other
  - Emphasis on asking questions and sharing knowledge across different skill areas (e.g., analytics, reporting)
  - Exploration of AI tools for analytics reporting (e.g., using Claude with GA4 and GSC data)

---

## Action Items

**Carrie Chowske (GrowthX)**
- Share Claude prompting thread for Yourco articles with team

- Get Prismic API key from Jessica for Yurco publishing automation

- Inform Jessica that manual review will still be done for Yurco articles despite automation


**Darrell Etherington (GrowthX)**
- Create Linear ticket for Suleiman to start adding publishing tasks to his queue


**Saskia Wartnaby (GrowthX)**
- Schedule Prophecy articles during the week

---

## Transcript
**Darrell Etherington:** Probably not that much in the way of updates for me.

**Darrell Etherington:** I think the main, the big thing will be the aftershoots change for us.

**Darrell Etherington:** We're ending our engagement with them, which was our decision, not their decision.

**Darrell Etherington:** So that's nice for a change.

**Darrell Etherington:** They were just consistently a really terrible client and not really worth the money they were paying us.

**Darrell Etherington:** So I had a talk with Marcel.

**Darrell Etherington:** I was in San Francisco this week about it, and he agreed.

**Darrell Etherington:** We should end that.

**Darrell Etherington:** We're just not a fit for what they're looking for.

**Darrell Etherington:** I think they had expectations more along the lines of like a full service agency of record, which is not what we are.

**Darrell Etherington:** So we're rounding out our engagement by delivering them a reduced scope kind of like final package of 40 articles total.

**Darrell Etherington:** And then that'll close by end of August.

**Darrell Etherington:** So I think very good news, honestly, because it's...

**Darrell Etherington:** It's nice to know that if a client isn't a good fit, we can potentially end that on our side, although we won't make a habit of it, obviously, only in extreme circumstances.

**Darrell Etherington:** But yeah, I was just out there hanging with the engineering team last week, and that was good, too, just to meet those folks.

**Darrell Etherington:** We have a lot of new people in that side, so that should be good for product.

**Darrell Etherington:** There's a bunch of them are – there's now, like, a full design team, which is interesting.

**Darrell Etherington:** There's, like, a three-person design engineering team.

**Darrell Etherington:** And also, Matt, we have a head of studio now, maybe some of you might have seen on LinkedIn, but he's out there doing a lot of video projects for us and for clients, which is also an interesting addition to our offering.

**Darrell Etherington:** He uses a lot of AI. It's fascinating. Yeah, it looks good.

**Darrell Etherington:** They were really like heads down on their offsite.

**Darrell Etherington:** So last week, I think things were moving more slowly than usual from an engineering perspective.

**Darrell Etherington:** But now after this coming out of it, I think they'll be re-energized and moving really quickly.

**Darrell Etherington:** So hopefully some of the stuff that we've been waiting for, like the publication automation, will start to come really quickly.

**Darrell Etherington:** And we're working on other fixes for that, as you may have seen in some of the chats.

**Darrell Etherington:** But the main one is that Webflow issue, which they had talked about previously, but obviously then just lost track of and didn't solve.

**Darrell Etherington:** So hopefully we'll reopen that and solve it.

**Darrell Etherington:** Because it doesn't make any sense for people to be getting booted out of installations just because of how many seats we have or whatever.

**Darrell Etherington:** Yeah, those are the big updates for me.

**Darrell Etherington:** I think also continue to give me feedback about the workflows and the generation.

**Darrell Etherington:** I've talked to Saskia about this a little bit because I did a lot of it last week.

**Darrell Etherington:** You can put it back to engineering, but like, if you need to run the two processes in parallel right now to get good effects, do that, because they haven't made any substantive changes to the pipelines, so it doesn't make sense to just continue banging your head against the wall until they make changes, and then we can provide more feedback for that.

**Darrell Etherington:** But you also run every assignment in Atlas, even if you are doing it in exterior tools, too, because that way they'll be able to collect that data and use it to inform future generations of the product.

**Darrell Etherington:** But stay tuned on that, because there are a couple of the experimental workflows.

**Darrell Etherington:** Town has one, and it's agentic, and it is much better, and so hopefully they populate that to a lot of the other clients and companies as well.

**Darrell Etherington:** So, yeah, I think that's it for me for now.

**Darrell Etherington:** Oh, one thing to be aware of, like, we'll get more clients coming soon.

**Darrell Etherington:** The first one I know of is Sunbit, so that's coming.

**Darrell Etherington:** over to us.

**Darrell Etherington:** We're going to do a two-week sort of temporary takeover, but then the plan is to shift that to us permanently, and Ehtisham will help that in his portfolio.

**Darrell Etherington:** And that's the major updates for me. Anybody else have anything they wanted to bring up or talk about?

**Carrie Chowske:** I am just in line with what you were saying, Darrell, about the, like, running things in parallel.

**Carrie Chowske:** If I noticed, because I mentioned this to Fahey and to Joe earlier this week, but if you're not, like, if you're not regularly using Claude, like, we have projects set up for all the clients in there, so you can add the artifacts and basically do the exact same thing that we're doing in Atlas, but, like, it's a little more interactive.

**Carrie Chowske:** So, like, especially if you're really frustrated with, you're not, you can't get it to do what you want it to do.

**Carrie Chowske:** I've had really good success with it. For example, one I did for an Engine article refresh mentioned a bunch of direct competitors as the best tool for this.

**Carrie Chowske:** And it was like, we were refreshing an article that had been done for Engine when it was Hotel Engine.

**Carrie Chowske:** So it only mentioned them as a hotel solution.

**Carrie Chowske:** And so I was like, oh, we need to make sure that we're not positioning it.

**Carrie Chowske:** And I was like, hey, these are competitors.

**Carrie Chowske:** What are we doing?

**Carrie Chowske:** And Claude goes, oh, yeah, that's stupid from a business perspective.

**Carrie Chowske:** Why would I do that?

**Carrie Chowske:** Yeah, yeah.

**Carrie Chowske:** It's very funny how it like immediately does that.

**Darrell Etherington:** Also, that was a funny one because I did, because they asked for two of those things.

**Darrell Etherington:** And then one of them, I did have it work around that.

**Darrell Etherington:** And then the other one, I didn't.

**Darrell Etherington:** But they were also too similar.

**Darrell Etherington:** I was going to ask them about that because I was like, these seem cannibalistic of each other.

**Darrell Etherington:** One was a refresh.

**Darrell Etherington:** One was a net new article.

**Darrell Etherington:** But in the other one, I was like, okay, give me the best list.

**Darrell Etherington:** But like, just make them complimentary services and not duplicative of Engine.

**Darrell Etherington:** And in that one, I had not done that.

**Darrell Etherington:** All right.

**Darrell Etherington:** But yes.

**Darrell Etherington:** It just became more marketing heavy is really what it did.

**Carrie Chowske:** But it was really cool.

**Carrie Chowske:** It was like, here's some alternatives.

**Carrie Chowske:** And here's why they're not as good.

**Carrie Chowske:** Yeah, yeah, yeah.

**Carrie Chowske:** It's, I mean, it is.

**Carrie Chowske:** It's really good at that kind of stuff.

**Darrell Etherington:** And then the other thing that I would recommend with those projects is, like, if you have one that's come out of Atlas and you're, like, pretty happy with it, but it's not all the way there, throw it in there and do it.

**Darrell Etherington:** Especially if you do want to do, like, hey, make sure this adheres to the client's writing guidelines.

**Darrell Etherington:** It's very good at that.

**Darrell Etherington:** good at that.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Very good at that.

**Carrie Chowske:** If anybody's interested, too, like, how I prompt it, I've got, like, a thread of me, like, the original prompt and then, like, all the extra stuff I asked it to do.

**Carrie Chowske:** I'm happy to share that, but you can go into, I think those were for your co.

**Carrie Chowske:** It's, like, if you go in to look at the ones I did for your co, those are the ones that I, like, you know.

**Carrie Chowske:** There have been a couple where Joe and I were struggling to get it where we wanted it to be, and Claude just kind of reflowed it.

**Carrie Chowske:** It fixed the voice throughout, and I just grabbed it and ported it over.

**Carrie Chowske:** Like, I didn't have to do a whole lot after that.

**Carrie Chowske:** So, anyway, just a, just a tip for us so we're not all spinning our wheels.

**Carrie Chowske:** I'm a lot of you are frustrated.

**Darrell Etherington:** Yeah, it is a significant difference, though, because I think Jess was asking me about the after-shoot volume.

**Darrell Etherington:** Like, the after-shoot volume, if using those, is not a challenge at all, because, like, and the question will be their quality bar.

**Darrell Etherington:** Like, that's been consistently the problem with them.

**Darrell Etherington:** But I can do 20 articles for after-shoots ICP that actually is of quality that I would publish on a photo blog that I was writing and publishing myself happily in, you know, half a day.

**Darrell Etherington:** Like, it's absurd, the speed, right?

**Darrell Etherington:** So, yeah, I'm not too worried about volume as long as we are able to do this in parallel with helping the team learn and improve on Atlas, which is what is going on now, right?

**Darrell Etherington:** So, on that note, like, how did you generate the articles for town and after-shoots?

**Ehtisham Hussain:** So all of them, the ones that we delivered to client were all done in cloud.

**Darrell Etherington:** I did them in Atlas, and then I looked at the output, and I was like, this ain't it.

**Darrell Etherington:** And then I did them in cloud, and I was like, this is basically done.

**Darrell Etherington:** So I used those ones.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Because, again, those, like, if I get that kind of output, like, my life would be so much easier.

**Ehtisham Hussain:** Exactly.

**Ehtisham Hussain:** And, like, they now understand that, like, yeah.

**Darrell Etherington:** Yeah, the product that we build has to compete on merit with the real product, right?

**Ehtisham Hussain:** So they understand.

**Carrie Chowske:** From an editing perspective, too, Ehtisham, like, the first thing that I've been doing with this stuff, because we have, one of the things I've noticed is that, like, Daryl was saying with the writing guidelines, like, I feel like that's where Atlas is struggling almost the most, is, like, to apply that.

**Carrie Chowske:** And doing it in cloud, I ask it to give me, like, a report, and basically, like, hey, what would you change?

**Carrie Chowske:** What needs changing to align?

**Carrie Chowske:** But these writing guidelines, it tells you, and then you can be like, okay, do this, but don't do

**Carrie Chowske:** That, this, but don't change that, or just, hey, yeah, go for it, change the whole thing, and it'll keep everything else the same, which I wish, I wish Atlas did that, like, I just want to be able to tell it, like, keep everything else the same, just change these things, you know, and so, anyway, I've had really good luck with that.

**Ehtisham Hussain:** With Aimbid, like, with Aimbid, what I'm doing is I'm using Gemini, and I, like, I gave it instructions, like, go familiarize yourself with Aimbid.io, and then make sure you look up the latest technical information in this sector, blah, blah, blah, then I gave it competitors, and then I started tweeting it the previously done articles that we have to revise, and then Gemini is kind of correcting them for me, the code and the technical stuff.

**Ehtisham Hussain:** But it's still, like, an AI-generated output, I still don't know how accurate it is.

**Ehtisham Hussain:** we'll have to see what they think about it, but both Cloud and Gemini are supposed to be highly technical.

**Ehtisham Hussain:** So hopefully that helps.

**Darrell Etherington:** Yeah.

**Carrie Chowske:** find that too, like Gemini is really good if you're already in Google Docs, if you want it to do something and you're like, hey, this section doesn't sound like the rest of the article, align it with it or something.

**Carrie Chowske:** And it's really good at giving you a passage that sounds more like the rest of it.

**Carrie Chowske:** Like that can be really fast too to not have to switch back and forth.

**Carrie Chowske:** And Gemini didn't know about the big beautiful X thing.

**Ehtisham Hussain:** So it was marking everything as inaccurate.

**Ehtisham Hussain:** Then I fended one of the PDFs on the IRS website.

**Ehtisham Hussain:** And then it was like, oh, okay, this is correct.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Yeah.

**Darrell Etherington:** It used that on town for the, because it was fed the documents.

**Darrell Etherington:** They provided us documents too.

**Darrell Etherington:** And it used those a lot.

**Darrell Etherington:** I could see, because it tells you.

**Darrell Etherington:** It's like, hey, I'm going to check this thing.

**Darrell Etherington:** And yeah, it does it.

**Carrie Chowske:** Joe, did you have something?

**Joe Sovar:** In addition to what Carrie said about Atlas, we could really use a final polishing step.

**Joe Sovar:** We use like one step after article generation to polish that article with the instructions and writing guidelines we have in Atlas because we have a lot of it there, but Claude really does a better job with that.

**Joe Sovar:** It listens to everything, but Atlas not for some reason.

**Joe Sovar:** Yeah, I did.

**Joe Sovar:** I provided that exact feedback to Daniel directly.

**Darrell Etherington:** Right, we need a final polishing step that's just a proofreader or quality checker that uses those writing guidelines.

**Darrell Etherington:** So that's her, because he does now, in the agentic one, the part where it does the generation, it basically just throws to Claude and then references the artifacts in the same way that the projects do.

**Darrell Etherington:** So that's why it's a lot better.

**Darrell Etherington:** But there's still some gaps there.

**Darrell Etherington:** So like they're working on that.

**Darrell Etherington:** But then, yes, absolutely, we need the like fact checker polishing step after the fact.

**Darrell Etherington:** And they're working on more natural language interfaces.

**Darrell Etherington:** So that you can, like, actually have a dialogue with the thing, too.

**Darrell Etherington:** And Saskia mentioned the thing.

**Darrell Etherington:** Yeah, I was going to say that same thing, Carrie.

**Darrell Etherington:** Like, if you go to any of the COD projects that I've set up for the customers, and the ones that I've been working in mostly are Engine, Town, and Aftershoot, they will have all the history stats of where I set up the articles, and you can see all the prompts of when I went through and did it.

**Darrell Etherington:** I've been refining to try to get closer to one-shotting it out of the gate, but it does still do some unusual behavior, like, because I try to include in that do internal linking and do external linking, and it will, like, selectively just ignore one of those two things from the initial prompt, but then it's fine because you can just do it in a subsequent step, right?

**Darrell Etherington:** It's not as sophisticated at the internal linking as ours is when it's working on a good day, but, like, ours is inconsistent as well, right?

**Darrell Etherington:** Although I just thought Kirkland was working on— Kirkland has some really good ideas.

**Darrell Etherington:** Ideas about how to fix that, including using a vector database, which we don't have now, which should be a big, big improvement if you can get that implemented.

**Darrell Etherington:** So those are places where we still have the ability to really outdo the off-the-shelf tools, and I think that's what they're focusing on from a technical perspective.

**Carrie Chowske:** I don't like going back and forth between tools, but I've done things where I run the whole Atlas workflow so all steps are there, then run just that one step.

**Carrie Chowske:** As long as you know where it's pulling the input from and can copy what you've done and port it over, it works pretty well.

**Carrie Chowske:** One thing Claude is good at is preserving your links.

**Carrie Chowske:** It preserves links when it rewrites and can contextually reframe them. If you're mostly happy with something, Claude is good at rewriting sentences while keeping everything else intact.

**Carrie Chowske:** If you want your structure the same but a paragraph sounds off-brand, Claude is great at that. And if you click where it says "document," it shows you the full text of what it changed.

**Carrie Chowske:** If you do it within the thread, it shows you the changes there too.

**Saskia Wartnaby:** Thank you, Carrie.

**Saskia Wartnaby:** And thank you, Daryl.

**Carrie Chowske:** My one rule for looking at other people's prompting is you can't judge it, but you can say, "I would try this because it might work better."

**Carrie Chowske:** Or "Here's how I did the same thing differently" — that's how we all learn.

**Carrie Chowske:** I like to think I'm the laziest prompter, but then I see someone else's and they prompt the same way. I try to give it enough context without overkill.

**Carrie Chowske:** I mean, it's getting to the.

**Darrell Etherington:** where I think you treat it like a competent, like professional, it's better, right?

**Darrell Etherington:** There are some fun ones in there where I was looking for DNS record information — that was a personal project. You can see my process there, nothing too exciting.

**Darrell Etherington:** Hey, we're all learning something, right?

**Carrie Chowske:** We're all really good at different things. I was humbled by Joe on the Engine handoff work. My biggest weakness is performance reporting — I'm not great at it. In my last agency, we did demand generation, so we focused on demos booked, not reporting metrics. I don't have that background.

**Carrie Chowske:** Joe talks about GA4 and I never bothered to learn it because I was focused on demand gen. I have no idea how to work with it.

**Carrie Chowske:** No, she's very good at it.

**Carrie Chowske:** I'm learning a lot from her, too.

**Darrell Etherington:** I'm finding some of it is sticking, so I'm happy about that.

**Carrie Chowske:** Yeah, so I'm not just, I would say, like, my thing is, too, I'm trying to not be afraid to ask questions when I feel stupid, because someone else has had them, so.

**Darrell Etherington:** Actually, I mean, like, the tools are very good at analytics, so I'm curious, and I want to do some experiments about that, like taking raw output from GA4 and GSC, and then giving it to O3 or something, and being like, hey, can you give me, like, a comprehensive analytics report about this and recommendations?

**Darrell Etherington:** I think that might unblock, too, because we're kind of, like, at Dave at the moment for a lot of that stuff.

**Carrie Chowske:** That's how I did that six-month one for your co.

**Carrie Chowske:** I did that.

**Carrie Chowske:** Oh, great.

**Carrie Chowske:** I just, I gave it, I gave it the raw output from.

**Carrie Chowske:** From, I mean, I filtered it, so I had what I needed, but I was like, give me some insights from here, you know, tell me, tell me what the trends are, like, it does pretty good at that.

**Darrell Etherington:** I'd recommend trying O3 for complex tasks because it's sophisticated at multi-step reasoning. Will, the new head of studio, showed me how he one-shotted a complex task.

**Darrell Etherington:** When a designer asked for a very specific task — take a video Will created, identify every B-roll moment, screenshot it, and put it in a table with timestamps — it was very complex, and O3 did it nearly perfect.

**Darrell Etherington:** Not perfect — it was a bit over-ambitious and misidentified some non-B-roll footage — but the sophistication of understanding B-roll versus A-shots and screenshotting into a table was very good. It saved Will days of work.

**Darrell Etherington:** Yeah, that's a lot.

**Darrell Etherington:** Do we have a team login for that?

**Carrie Chowske:** We have a team login for ChatGPT Pro where you can select O3 as a model. We also have PodB accounts.

**Darrell Etherington:** We set up PodB accounts because everyone using one OpenAI account hit usage limits.

**Carrie Chowske:** Fey, were you able to get into Claude yesterday?

**Feyisayo Odedeyi:** Yes, I was. Finally.

**Feyisayo Odedeyi:** It was a pain in the butt, but it's set up now.

**Carrie Chowske:** You can see how often we're using it. Everyone will get the login link and see how much Claude is being used. After this call, it'll probably be even more.

**Darrell Etherington:** Anyone else have blockers to raise? The publishing situation is still something we're untangling.

**Darrell Etherington:** I need to create the right Linear ticket for Suleiman to start taking on all these publishing tasks. He will eventually take on everything and spearhead automation, but it'll be gradual as he gets up to speed.

**Saskia Wartnaby:** Daryl, just in the meantime, I've got quite a few articles to schedule for Prophecy.

**Saskia Wartnaby:** Should I just make space to do that during the week for now?

**Saskia Wartnaby:** How quickly do you think that will be implemented?

**Darrell Etherington:** Yes, make space for that. I'll put you first on the list once I find the right Linear template. Prophecy articles are top priority because they're complicated.

**Saskia Wartnaby:** Thanks.

**Carrie Chowske:** If we get Engine working in the pipeline, that would free up a lot of work. We probably wouldn't need help there — just pushing them live.

**Darrell Etherington:** That's the goal. Joe created a ticket for it. And then there's the Prismic/Yurco automation, but you do so many quality checks there that we might not want to hand it off anyway.

**Carrie Chowske:** For what they're paying us, the manual time isn't huge. We'd still want to do a quick review anyway.

**Darrell Etherington:** Right. Ideally we automate the slice creation but keep manual review. The automation would help but we'd still want quality control.

**Darrell Etherington:** The Yurco ticket from a couple weeks ago — did we submit it?

**Carrie Chowske:** I never submit tickets. Every time I'm about to, someone offers to do it. I've never actually submitted one.

**Joe Sovar:** You posted one for automated publishing a few weeks ago. I saw it in Linear for Yurco.

**Carrie Chowske:** Oh, right! I did submit that one.

**Darrell Etherington:** Right, the blocker is we still need the Prismic API key to move forward. Do we have that?

**Carrie Chowske:** I'll get the API key from Jessica. But I need to let her know we can't actually publish via API — we don't have the authority and Prismic doesn't support it anyway. We'll still do manual review, just skip the copy-paste.

**Darrell Etherington:** Right, our user doesn't have publishing authority, but even if they did, Prismic doesn't support API publishing.

**Carrie Chowske:** Exactly. And on top of that, I can't even preview the pages in Prismic, which makes quality checking impossible.

**Carrie Chowske:** Links work fine in Google Docs, but once they're in Prismic, I can't check them. Clicking on them does nothing, and I can't preview the page. So I can only validate links in Google Docs before hand-off. After that, I'm blind to broken links.

**Darrell Etherington:** The pipeline approach might fix this. Instead of copy-paste from Google Docs, it would send the content as JSON or another format, which could preserve and validate links properly.

**Darrell Etherington:** Alright, everybody can get back to their day. We'll sync again next week. Thanks, all. Bye.
