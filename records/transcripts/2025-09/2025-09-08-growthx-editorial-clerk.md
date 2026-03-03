# GrowthX Editorial | Clerk

<metadata>
date: 2025-09-08
time: 19:00 UTC
duration: 34 minutes
organizer: andi@growthx.ai
participants: Andi Bailey, Alex Rapp
fathom_recording_id: 85732601
fathom_url: https://fathom.video/calls/402669725
share_url: https://fathom.video/share/mXyC7S83x6xDL45sRTsTRAVzKAZ9yjBe
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX and Clerk aligned on revising their AEO content workflow after the SSO article draft surfaced misaligned expectations around quality, technical accuracy, and content positioning. Clerk's engineering leadership (Jeff) wants upper-funnel, non-branded content to fill a gap in their existing blog, but has concerns about technical accuracy and relevance to Clerk's product vision. GrowthX proposed a product deep-dive with Jeff or Brian to understand Clerk's positioning better, commit to involving technical reviewers in content creation, and adjust the review workflow: Brian (Clerk's content engineer) will review articles first, Alex will audit approved topics in Airtable to ensure they're non-Clerk-specific, and the SSO article revision should be ready by mid-week.

---

## Context

Clerk is an authentication and user management platform working with GrowthX on AEO content strategy. This is a Phase One engagement focused on generating AI-optimized upper-funnel content to improve Clerk's visibility in LLM responses. The relationship is in early stages with some internal friction: Clerk's engineering leadership (particularly Jeff, head of engineering) had bad experiences with SEO agencies in the past and carries skepticism about both AI-generated content and GrowthX's approach specifically. GrowthX had not yet conducted a product deep-dive before creating the first draft (SSO article), which led to technical accuracy concerns and misalignment about the content's purpose—engineering wanted branded, Clerk-centric content similar to their blog, while GrowthX was deliberately creating generic upper-funnel content designed for LLM citation, not blog-quality articles.

---

## Relevance

**To GrowthX Delivery:**
- Product deep-dives must happen early in Phase One engagements before any content generation—Clerk case shows this is critical for alignment on positioning and technical accuracy expectations.
- AEO content requires explicit stakeholder education: upper-funnel, non-branded content for LLM visibility is fundamentally different from blog content; this difference must be explained and re-explained.
- Technical reviewer involvement in content creation is now a standard requirement—Clerk raised valid accuracy and nuance concerns that could have been caught earlier with SME involvement.
- Review workflows need clear ownership and sequencing (Clerk's Brian reviews first, then topic validation against approved list, not the reverse).

**To CheckThat:**
- Clerk case validates the need for domain-specific fact-checking workflows—Clerk specifically mentioned new "agentic workflows" with persona-specific fact checkers that could help prevent technical accuracy issues in future content.
- Positioning matter: Clerk explicitly flagged that an article advocating against third-party tools undercuts their product even when branded content promotes Clerk elsewhere. This is a content coherence issue CheckThat could surface.

**To GrowthX Business Development:**
- Account health: Clerk's leadership skepticism and slow approval cycle (iterative revisions needed) suggests lower trust. Gonto (external advisor) helped reset expectations by sharing he needed 5 rounds of revisions for his first articles—critical social proof for this account.
- Expansion risk: Clerk's internal bandwidth is severely constrained (one content person on their side, Jeff doing manual competitor analyses). This limits how much content they can review and absorb, even if quality improves.
- Next steps require delivery speed: Alex needs SSO revision by Wednesday, and product deep-dive this week before his Iceland offsite—timeline pressure is high.

---

## Overview

- Clerk aims to focus on upper-funnel, non-branded content to fill a gap in their current content strategy
- Technical accuracy and alignment with Clerk's product vision are key concerns for the engineering team
- GrowthX will conduct a product deep-dive with Clerk's engineering team to better understand the product and target audience
- The SSO article will be revised, and two new articles will be reviewed by Clerk's content engineer

---

## Key Topics

### Content Strategy Alignment

  - Clerk wants to focus on upper-funnel, non-branded content to complement their existing blog
  - GrowthX will avoid Clerk-specific topics for now and concentrate on generic, high-level content
  - Brian (content engineer) will continue to focus on Clerk-related content
  - Alex will review approved topics in Airtable to ensure they align with the upper-funnel strategy

### Technical Accuracy Concerns

  - Inaccuracies and technical nuances in the SSO draft were major concerns for Clerk's leadership
  - Clerk's head of engineering (Jeff) will parallel-path some topics to compare with GrowthX's output
  - GrowthX will involve technical reviewers in the content creation process to improve accuracy

### Product Deep-Dive

  - GrowthX missed conducting a deep-dive on Clerk's product, features, and pain points
  - A 30-minute call with Jeff (head of engineering) or Brian (content engineer) will be scheduled
  - The call will cover product details, roadmap, engineering perspective on personas, and customer base

### Content Review Process

  - Brian will review the next two articles (starting with "Top Authentication Vulnerabilities")
  - The "Scaling Authentication" article will be rerun with updated keywords and focus on Next.js
  - SSO article revision expected by mid-week (Wednesday at the latest)

### AI-Generated Content Expectations

  - Clerk's leadership initially expected highly polished content on the first pass
  - Alex reset expectations, emphasizing the iterative nature of the process
  - Content is primarily aimed at increasing visibility among LLMs, not matching blog quality

---

## Action Items

**Alex Rapp (Clerk)**
- Drop note to Ada re rescheduling next week's call due to Iceland offsite
- Check Airtable to ensure approved topics are not Clerk-specific; flag any that are
- Ask Jeff for 30-minute availability this week for product deep-dive with Andi or George; if unavailable, ask Brian
- Have Brian review "Top Authentication Vulnerabilities" article first, then the next article

**Andi Bailey (GrowthX)**
- Rerun "Building Scalable Authentication Systems" article with Alex's 5 Airtable comments incorporated
- Remove calibration blog from shared Google Doc folder; prep for comparison once new version is ready
- Schedule 30-minute product deep-dive call with Jeff (or Brian if unavailable) this week; conduct with either Andi or George

---

## Transcript
**Andi Bailey:** This meeting is being recorded.

**Andi Bailey:** Hey, Alex.

**Alex Rapp:** Sorry, I didn't realize I was on mute.

**Alex Rapp:** How are you doing?

**Andi Bailey:** Good, how are you?

**Alex Rapp:** Oh, yeah.

**Alex Rapp:** I got a lot going on over here.

**Alex Rapp:** I shouldn't say I made the mistake, but I already had a lot on my plate, and I decided it would be a great idea to also coach both of my kids' softball and t-ball teams on Sundays.

**Alex Rapp:** So I didn't know what I was getting myself into.

**Alex Rapp:** I'm happy I did, but it was a lot to plan for for the first week, and then I just spent the last half an hour writing individual emails to each of the teams to get them ready for next week since I'm going to be traveling.

**Alex Rapp:** You know, all of next week and we'll miss the game.

**Alex Rapp:** And so, yeah, just lots of spinning plates over here.

**Andi Bailey:** Yeah, I feel like the planning and coordination, you never realize for those sorts of things.

**Andi Bailey:** How much you have to, like, it's, you're managing parents, essentially.

**Alex Rapp:** And luckily, you know, I haven't had any issues with, you parents and my wife, you know, she coaches my daughter's soccer team, and she hasn't had any issues with parents either.

**Alex Rapp:** But I've heard really bad horror stories from, you know, other parents, you know, just about, you know, people getting a little too into it and whatnot.

**Andi Bailey:** Well, fingers crossed for you.

**Alex Rapp:** And fingers crossed that the organization piece doesn't take over your life.

**Alex Rapp:** Thank you.

**Alex Rapp:** And I don't know if I did mention it to you or to Ada.

**Alex Rapp:** I'm heading to an offsite all of next week. I mentioned this to Ada already, but I'll drop her a note after this call to figure out timing for next week's regular call once I'm on site.

**Andi Bailey:** So you're going to be in Iceland?

**Alex Rapp:** Yeah, I'm looking forward to it. It's yet another plate I'm spinning with all the coordinating and planning, but it should be fun.

**Andi Bailey:** Well, the goal here for today is to try and get the coordination of the article feedback to be a little bit less stressful.

**Andi Bailey:** Yeah.

**Andi Bailey:** So took.

**Andi Bailey:** I a look at the article and kind of looked back at the process that the team has taken so far.

**Andi Bailey:** I have some thoughts on things that we definitely missed just in our standard process that we want go back and do.

**Andi Bailey:** But I want to start by just like hearing kind of like my understanding is you guys have had like bad experience with SEO agencies.

**Andi Bailey:** You lost a lot of trust.

**Andi Bailey:** And so there's a lot of like scrutiny that's coming in.

**Alex Rapp:** But yeah, I can lay it all out on the table for you.

**Alex Rapp:** It's funny because Marcel reached out to me this morning, too.

**Alex Rapp:** And I'm like, you know, TLDR, I basically said the same thing I said to you is.

**Alex Rapp:** You know, I never expected this to be a home run, you know, right from right out of the gate.

**Alex Rapp:** I think leadership's expectations were that they were going to get this, you know, very polished, deep and detailed article, you know, on the first pass.

**Alex Rapp:** And I spent a lot of time towards the end of last week kind of bringing people back down to earth.

**Alex Rapp:** And also, I spent a lot of time with our head of engineering because he doesn't understand why we're contracting this out as opposed to using internal resources, which I'll circle back to if it makes sense.

**Alex Rapp:** But NetNet, I still feel good about the direction, and I appreciate you taking time out to kind of come up with a good game plan.

**Alex Rapp:** But so we, as you know, we have one person on this team that's writing content right now, and there's really no solution to improve that headcount in the near term.

**Alex Rapp:** We're obviously going to try to hire for that, to build out the team in the future for human-written content.

**Alex Rapp:** But we know from talking with some of our advisors and also talking with other growth leads that if we want to win at the AAO game, we need to start putting out much more content and content that is specifically tailored for the LLMs.

**Alex Rapp:** I think that was another point of misalignment between our team and the rest of the leadership as well is that they're expecting, I think, a quality bar that is very much at the same level as what we put out on our blog.

**Alex Rapp:** And I had to reset expectations there that that is not the case.

**Alex Rapp:** We are writing for, you know, to increase our visibility and presence among LLMs and it doesn't need to be this, you know, something that you're going to hang up in the loop, right?

**Alex Rapp:** It just needs to be detailed and deep enough to be able to, you know, rise to the top in terms of, you know, probability of citation, right?

**Alex Rapp:** So we ran this experiment at the beginning of this year where we onboarded, I think, man, I can't remember, it was somewhere between five and 10 external writers.

**Alex Rapp:** And the purpose of that was for blog content.

**Alex Rapp:** It wasn't for, you know, AEO at the time.

**Alex Rapp:** And the quality that we were getting there and the amount of time that we're spending to, you know, try to bring the quality up.

**Alex Rapp:** So the quality was poor.

**Alex Rapp:** And the amount of time that we're spending to bring the quality up was just, you know, it was, you know, we were in the red with that approach, you know, from the get go.

**Alex Rapp:** And our CEO is very opinionated in terms of, you know, external facing, you know, content, you know, whether it's our Twitter feed, whether it's, you know, our blog, or, you know, anything else that we put out there, you know, he has this vision that we need to be at the same level as the most respected.

**Alex Rapp:** Companies out in our community, know, namely Vercel and Stripe, you know, both of which are, you know, very well respected.

**Alex Rapp:** They have a very, you know, static, you know, approach to creating content.

**Alex Rapp:** It's very technical.

**Alex Rapp:** It's very deep.

**Alex Rapp:** And it's, you know, just very polished and professional.

**Alex Rapp:** And that is why he stepped in and basically advocated to cancel the external writer program, which we haven't revisited.

**Alex Rapp:** You know, we've had a bunch of people reach out, but we, you know, we've had to basically reject them.

**Alex Rapp:** Enter automated workflows.

**Alex Rapp:** We tested Aerofs.

**Alex Rapp:** We've tested N8N.

**Alex Rapp:** The quality that I captured out of Aerofs specifically was subpar compared to, you know, me writing this very long prompt with instructions and guidance and providing, you know, to some degree artifacts as well.

**Alex Rapp:** So, right.

**Alex Rapp:** As inputs into just, you know, ChatGPT deep research, you know, the version that came out of that process versus, you know, trying to use these automated workflow tools was far better than what we saw coming out of Aerobs.

**Alex Rapp:** We pivoted in general to N8N just, you for cost reasons and then also for, you know, what we see to be as, you just a higher quality bar and also N8N is very much in tune with, you know, I think it's more so, you know, anchored towards the type of persona that we're going after.

**Alex Rapp:** You know, it's really, you know, it can be seen more as a technical, I wouldn't call it a developer tool, but, you know, it's, it has integrations with developer tools, whereas Aerobs has some, but not many.

**Alex Rapp:** Anyways, that's, that's besides the point.

**Alex Rapp:** And so come last week when I shared the, the draft for the SSO article out to.

**Alex Rapp:** Our leadership team, you I preface it by saying this content is going to live on a different slug from our blog.

**Alex Rapp:** It's going to be unlisted for the time being until we get to a good place.

**Alex Rapp:** This is the first pass, you know, be critical, provide very transparent feedback.

**Alex Rapp:** And, you know, it just took a lot of time for me to kind of bring our head of engineering, Jeff, back around and get him to really understand what we're doing here.

**Alex Rapp:** And then also we had a call on Friday with Gonto, who is one of our advisors.

**Alex Rapp:** And I know that he's also worked with you all over at GrowthX before with, you know, not only his own company, but also some of his clients that he's advising.

**Alex Rapp:** And, you he did a great job of painting, you know, a much more vivid picture, I think.

**Alex Rapp:** And obviously it was nice to just have a third party, you know, kind of speak to the whole process in general.

**Alex Rapp:** You know, he obviously echoed my sentiment that, you know.

**Alex Rapp:** This is the first pass.

**Alex Rapp:** I think he gave it a 6 out of 10, which, you know, I think surprised our, you know, Jeff, our head of engineering.

**Alex Rapp:** And, you know, he also mentioned that he went through, I think, you know, for the first couple articles, I think he went through five different rounds of revisions before he felt really good with the output.

**Alex Rapp:** And he also mentioned, you know, he's worked with companies that, you know, went through the entire process of phase one with you all, and also ones that, you know, decided to cancel early.

**Alex Rapp:** And, you know, both are succeeding in certain areas, but both have different ranges of resources to be able to either pursue this individually or externally.

**Alex Rapp:** So, what we decided on is that we're going to wait for the revisions to come through on the SSO article.

**Alex Rapp:** We are going to parallel path the two other articles that you dropped last week with...

**Alex Rapp:** Our content engineer on our immediate team, and in parallel, this is kind of funny, our head of engineering, Jeff, he is going to take some of the topics that your team is writing and create them on his own, and we're going to run side-by-side tests, because I think this is more of an ego thing for him.

**Alex Rapp:** You know, he kept saying to me, you know, I could easily take some of these articles and, you know, go through a list of five, at least five in a day.

**Andi Bailey:** said, then why aren't you?

**Alex Rapp:** You know, we have so, and Colin, you know, luckily our CEO, he backed me up.

**Alex Rapp:** He said, marketing isn't equipped to do this right now.

**Alex Rapp:** They have so much going on and on their plates that they can't be the ones that are just focused on creating content.

**Alex Rapp:** Which, you know, which was a nice voice and vote of confidence for us.

**Alex Rapp:** And, you know, also emphasize why we are outsourcing this at this time.

**Alex Rapp:** And so, you know, I think as it stands right now, the biggest concerns that, you know, that were shared by, I would say, myself and the rest of the leadership team that did spend time going through the content or the SSL draft was, you know, some inaccuracies.

**Alex Rapp:** Just, you know, best practices and suggestions, you know, technical nuances, you know, I think that's, that's, that's probably going to be what I see as the biggest hurdle to overcome, just, just because I know you mentioned, or I think you mentioned that you don't have an in-house, you know, sort of technical writer to, you know, be the SME on, on this content.

**Andi Bailey:** Yeah, go ahead.

**Andi Bailey:** No, was going to say, I think, like, we have some people that we can lean on in this.

**Andi Bailey:** some people that we I see.

**Andi Bailey:** We have a couple of people we can lean on for this. They just weren't scoped into this part of the process, but I think that's really easy for us to add going forward.

**Alex Rapp:** Okay.

**Alex Rapp:** The other, the other one, you know, that was sort of the elephant in the room was, you know, the eighth best practice, which was, you know, advocating essentially to not use, you know, not get locked in with third party, you know, tooling, or, you third party services, which, you know, in leadership's eyes, and, know, I agree as well, you know, that's something that we obviously would not want to.

**Alex Rapp:** include because, you know, it's a directly, it's, it's directly or indirectly, basically telling the audience not to use Clerk, even though, you know, in various points of the article, we are saying to, you know, use Clerk for this specific use case, so.

**Andi Bailey:** Yeah, yeah.

**Andi Bailey:** Okay, that's, that's super helpful.

**Andi Bailey:** Marcel mentioned, I he and Jeff worked together at one point.

**Alex Rapp:** So I don't know if that's where some of the ego comes from, too.

**Alex Rapp:** Probably.

**Alex Rapp:** I don't know if, I don't know, because when we, when I first started talking to Marcel, it was, gosh, I don't remember, maybe September or October of last year.

**Alex Rapp:** And, um, somehow it came back around to, you know, they used to work together, maybe didn't have the best relationship.

**Alex Rapp:** And, but I don't know if he connected those dots this time around, because he didn't mention it at all.

**Alex Rapp:** Um, but, you know, I, I would kind of push that aside.

**Alex Rapp:** I, you know, I wouldn't worry about that too much.

**Alex Rapp:** You know, this is, you know, it's not as though Marcel's the one, you know, creating the content.

**Alex Rapp:** And it's not as though he's the one that's, um, you know, in, in, in the conversation loops, you know, within the channel.

**Alex Rapp:** And, you know, I, I really hope that that just doesn't even come up, you know, and like to just bury that as much as possible.

**Alex Rapp:** But, um, but yeah, it's less.

**Alex Rapp:** So that and much more just about technical accuracy, you know, I think there are going to be the other big hurdle that I'm, you know, had to spend a lot of time explaining was our blog does a great job of speaking to branded content, right?

**Alex Rapp:** It does a great job of, you painting pictures and delivering content as it relates directly to Clerk.

**Alex Rapp:** Our biggest gap is upper funnel, non-branded content, more generic, more high level.

**Alex Rapp:** And, you know, as Jeff was going through the draft, you know, he was basically calling out, this is not how we do this, you know, things of that nature.

**Alex Rapp:** And, you know, that's where I kind of had to recenter him and say, this is not meant to be from the lens of Clerk.

**Alex Rapp:** This is meant to be from the lens of somebody that maybe doesn't know that much about SSO.

**Alex Rapp:** They want to start learning.

**Alex Rapp:** And then this is the path.

**Alex Rapp:** way to moving them along closer to our conversion funnel.

**Alex Rapp:** So it's a building block.

**Alex Rapp:** It is not meant to be a catch-all or a, you know, a direct conversion driver for Clerk.

**Alex Rapp:** It's meant to capture the audience, get them aware of Clerk, get them interested.

**Andi Bailey:** Yeah.

**Andi Bailey:** And actually, that was a question that I had for you.

**Andi Bailey:** And that's just, this is just me missing a little bit of context from all of the conversations.

**Andi Bailey:** But I know this was like really, it is like top of funnel content.

**Andi Bailey:** It's very high level.

**Andi Bailey:** And in some of the other conversations, I know you guys had sent over like Discord topics, like some more specifics on, you had like a backlog of blog content.

**Andi Bailey:** That seems like it's more like specific, clerk, like expertise content and pieces where it's like high intent.

**Andi Bailey:** People already know what they're looking for.

**Andi Bailey:** They're like partway down the.

**Andi Bailey:** And they're looking, they want help from Clerk.

**Andi Bailey:** So it like, which one are we aiming for here?

**Andi Bailey:** And I want to like, talk a little bit about like, the articles, the topics themselves, and kind of that target piece too.

**Alex Rapp:** Yeah, that's a great question, you know, because I really hadn't, hadn't thought about it at that, at that angle.

**Alex Rapp:** I think for now, I would love to focus on upper funnel.

**Alex Rapp:** I think as we, you know, as we gain some momentum and, and trust among the team, then we can start to explore, you know, content areas that are, you know, much more direct.

**Alex Rapp:** directly related to what we're doing over here at Clerk, you know, the sort of, the division of church and state here is that, you know, Brian, our content engineer, who I know you met, he's going to continue to focus on related content.

**Alex Rapp:** And we are going to use your team to fill the void that we have for non-branded content, upper funnel content, whatever you want to call it.

**Alex Rapp:** There is a mass volume of opportunity in both areas.

**Alex Rapp:** So that's why I'm saying, let's get the upper funnel content nailed, and then we can start to move deeper into Clerk-specific territory.

**Andi Bailey:** Yeah, yeah.

**Andi Bailey:** Okay, that makes a lot of sense.

**Andi Bailey:** And then I do want to just a couple.

**Andi Bailey:** So there are a bunch of articles that are approved to start.

**Andi Bailey:** And so we want to keep on the path of what's been approved to start in terms of topics.

**Andi Bailey:** Like that's, we don't want to read.

**Alex Rapp:** Yeah, let me, I can go back and take a look after this call in Airtable and just make sure that none of those topics that I approved are, are, you know, calling it fall into that bucket of more Clerk-specific.

**Andi Bailey:** Yeah.

**Alex Rapp:** Yeah.

**Alex Rapp:** Um, but from what I can recall, I think they were all pretty, um, you know, more generic than, than brand specific.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** That makes sense.

**Andi Bailey:** And then the, um, one of the pieces that we missed was we usually do a deep dive, um, either with somebody from product marketing or from your product or engineering team on like kind of overarching, walk us through the product, tell us about the features, tell us about the pain points.

**Andi Bailey:** Like, you know, you have Marcel, uh, and George, I know asked some very specific questions about your goals and kind of where you are in the, like your kind of life cycle journey in the kickoff call.

**Andi Bailey:** We want to go deep on the product.

**Andi Bailey:** And even if we're, uh, targeting top of funnel content, I think for us to keep in mind kind of the product angles that your internal team thinks about on the product and engineering side, um, and...

**Andi Bailey:** Um, and...

**Andi Bailey:** You know, I saw on one of the calls you guys talk about that you've got some, like, new positioning, new features coming out.

**Andi Bailey:** Like, for us to be read in on some of that could also help just to have that context at another level.

**Andi Bailey:** So is that something that we could schedule with, like, as a product person, product marketing person that we could talk to?

**Andi Bailey:** Or even, like, I know your A's have, like, a low conversion rate right now.

**Andi Bailey:** Like, do you have, could one of them talk us through, like, a really successful sales call where it was, like, one and done, you know?

**Alex Rapp:** So we could think about So we actually don't have a sales team.

**Andi Bailey:** Oh, okay.

**Alex Rapp:** We, actually, sorry, let me grab, I have a, we have a plumbing issue and a plumber just showed up.

**Andi Bailey:** So give me one second, please.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** OK.

**Alex Rapp:** So originally we were going to have Brian do that. When I spoke with Ada about the Clerk documentation, she felt that was good enough to get started. I can ask Jeff if he has time to hop on with you. I'd recommend avoiding having Marcel on that call—Jeff is skeptical of AI-generated content, and I'd rather not introduce any history into that conversation.

**Andi Bailey:** I think 30 minutes should be fine. We don't need to take up too much of his time. We want to understand product today, roadmap, and how the engineering side of the org thinks about the product and their customer base—personas on the marketing side versus personas from the product side can sometimes differ a little bit in terminology.

**Andi Bailey:** It's a spectrum.

**Andi Bailey:** Yeah, just understanding kind of what that looks like on both sides.

**Andi Bailey:** So we can have a really comprehensive picture of, especially if Jeff is going to be reviewing more content.

**Andi Bailey:** That we make sure that we're writing for the right person, for Jeff, essentially, too, and who he has in mind.

**Alex Rapp:** Okay.

**Alex Rapp:** If he's not available, then Brian already said that he would, but not to pit them against one another, but Jeff is obviously, I think, has a higher expertise across the board than Brian does.

**Alex Rapp:** But Brian will be a good fallback in this case if we can't get him.

**Alex Rapp:** And who would you have Jeff meeting with?

**Andi Bailey:** Either myself or George. George used to work at Techstars and has done a lot of ICP work, helping pre-seed companies develop their personas. He brings a structured framework and is really good at deep dives.

**Alex Rapp:** Got it. Let me circle around with Jeff after this call and see if he's available.

**Alex Rapp:** I gave him access to the Notion workspace and told him to feel free to improve the artifacts. Gonto suggested they shouldn't be set in stone—we should constantly be improving them. I'll try to spend some time on that this week before I head out, so I can see if Jeff has time this week rather than pushing it out next week.

**Alex Rapp:** Is there anything else you wanted to cover?

**Andi Bailey:** Those are the main things. Do you guys want to look at that article before we move on?

**Alex Rapp:** We're going to have Brian review the next two articles first. He probably won't get to it until tomorrow, but that's fine. I did drop some comments in Airtable asking if we could rerun the scaling authentication article. The original keywords aren't how our audience speaks—developers wouldn't search for "scaling authentication mechanisms," they'd search for something specific like "scaling authentication for Next.js."

**Alex Rapp:** Since Next.js is our most popular framework and also the broader developer community's most popular framework, I made it specific to Next.js. Even though it's specific, it's still broad enough to have a very wide audience. So if we could rerun that one, that would be great. The other one on authentication vulnerabilities is fine—we'll start with reviewing that one.

**Andi Bailey:** I'll pull the authentication article from the review folder so people aren't looking at it. Hopefully we'll get time with Jeff. I'm going to have a couple of people review the calibration blog and this other content going forward. We're also launching some new agentic workflows, including the ability to add a really specific fact-checker for specific personas that we build. We'll experiment with that as we go.

**Andi Bailey:** But hopefully, you know, we don't want anything else to look like the calibration blog.

**Alex Rapp:** From my standpoint, I understood this would be an iterative workflow to start—like training any model, it requires modification and fine-tuning before you can feel confident hitting submit. Let me see if Jeff already ran the authentication vulnerabilities one. His is framework agnostic but calls out React and Next.js specifically. It looks like you both took a very similar approach.

**Alex Rapp:** I'll pass this one over to Brian. If you can have the team rerun the building scalable authentication systems article with the changes I made—I left about five comments in Airtable—that would be great. And when do you think we'll get the next pass on the SSO article?

**Andi Bailey:** I think we can have something by midweek, like Wednesday at the latest. I'm going to try to have something for you by end of day tomorrow.

**Alex Rapp:** If you need more time, don't rush. I'd rather see significant improvement than a thousand small fixes.

**Andi Bailey:** I'm going to pull the calibration blog out of the shared folder so people aren't looking at it and getting frustrated. We'll take another try at it.

**Alex Rapp:** I'm the only one looking at Airtable right now anyway, so you don't have to worry about it from our side.

**Andi Bailey:** I meant from the Google Doc. We can do a comparison once it's ready.

**Alex Rapp:** Perfect. Anything else from your side?

**Andi Bailey:** No, thanks for taking the time and giving me all that context. I really appreciate your patience and understanding of what success looks like.

**Alex Rapp:** I want to win with this, and that's why I'm putting as much effort as I can into it. I'm on your team, but I also need to make sure we appeal to the leadership.

**Andi Bailey:** Exactly.

**Alex Rapp:** All right, thanks so much. Feel free to reach out if you need anything else. I'll let you know what Jeff's availability is this week.
