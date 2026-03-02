# Okta <> Growth X - Weekly Sync

<metadata>
date: 2025-10-22
time: 17:00 UTC
duration: 51 minutes
organizer: kyle@growthxlabs.com
participants: Sydney Arin Go, Rachael Tiow, Kyle Gaudreau
fathom_recording_id: 96029803
fathom_url: https://fathom.video/calls/448726959
share_url: https://fathom.video/share/vncJiAfjSQbSVF5PzL_5hyju52bgQBxc
source: fathom
enriched_on: 2026-03-02 19:40 UTC
</metadata>

---

## Summary

GrowthX and Okta aligned on a major architecture shift for their AI-powered SDR tools — moving from a resource-intensive 1-Gem-per-account model to a scalable "baseline" vertical Gem approach that supports tiered ABM campaigns (1-to-1, 1-to-few, 1-to-many). Rachael is developing a clear product POV to differentiate Okta (for traditional banking/healthcare) from Auth0 (for SaaS/fintech), and Emily, her new hire, will lead testing and SDR enablement starting next week. The team will test Clay-enriched account briefs and competitive insights (Ping, ForgeRock, Gigya) to validate the value of additional data before scaling.

---

## Context

Okta is a major enterprise identity and access management (IAM) vendor, and this is a weekly working session between Okta's growth and product teams and GrowthX's content and strategy team. Sydney Arin Go and Kyle Gaudreau represent GrowthX; Rachael Tiow is driving go-to-market strategy and product positioning at Okta. The relationship is focused on building AI-powered sales development tools that help Okta SDRs prospect more effectively by providing contextual account and vertical-specific intelligence. This is part of a broader strategic initiative at Okta to shift from program-centric to account-centric ABM, powered by generative AI and data enrichment (including Clay for technographic data).

The meeting happened because the team needed to align on a major architecture pivot — the current tool design was proving inefficient due to platform constraints (Gemini's 10-file limit, NotebookLM's uncertain fit) and SDR adoption friction. The conversation also touched on product strategy: Okta's growing complexity across Customer Identity (Okta and Auth0 being confusing to the market) and the need to develop distinct positioning by vertical and use case.

---

## Relevance

### To GrowthX Delivery

- **Tiered ABM methodology**: The "baseline vertical Gem + manual account brief upload" pattern is a scalable approach for handling platform constraints while maintaining SDR adoption. GrowthX should document this model as a reusable pattern for clients building AI-powered sales tools.
- **Data enrichment validation**: The planned Clay pre/post-test is critical to GrowthX's AEO and content strategy work — proving ROI of enrichment will inform how the team recommends third-party data integration to other clients.
- **Vertical-specific briefs**: GrowthX is building and will test artifacts for Retail, Hospitality, and B2B SaaS. Results will feed back into GrowthX's content library and vertical expertise.

### To CheckThat

- **Competitive insights integration**: Okta plans to surface competitive intelligence (Ping, ForgeRock, Gigya positioning) within the Gems without explicit competitor bashing. This is a practical demonstration of how CheckThat's AI visibility insights could be surfaced in B2B outreach without appearing aggressive.
- **Prompt guardrails**: Sydney's briefs already include explicit "do/don't" instructions (e.g., "don't bash competitors"). Okta is expanding these guardrails. This validates the importance of careful prompt design in outbound AI tools.

### To GrowthX Business Development

- **Account health signal**: Rachael's frustration with tool constraints, her drive to define a product POV, and her hiring of Emily all signal a healthy, growing account. Okta is investing in this motion and expanding team capacity.
- **Expansion play**: Emily's arrival and focus on prompt refinement and SDR enablement suggests Okta may expand the scope of work with GrowthX beyond initial artifacts to include ongoing optimization and training.
- **Reference potential**: Once the baseline Gem + brief architecture is live and validated with real SDR activity, Okta could become a strong reference for B2B SaaS companies building similar tiered ABM motions.

---

## Overview

- **New Architecture:** Shift from 1-Gem-per-account to a "baseline" vertical Gem. SDRs will manually upload specific account briefs to the Gem to provide hyper-relevant context.
- **ABM Integration:** The new architecture supports a tiered ABM strategy (1-to-1, 1-to-few, 1-to-many), with the baseline Gem handling 1-to-many outreach and detailed briefs reserved for high-value accounts.
- **Okta/Auth0 POV:** Rachael is defining a clear product POV to eliminate internal competition: Okta for traditional banking/healthcare, Auth0 for SaaS/fintech/digital banking.
- **New Team Member:** Rachael's new hire, Emily, starts next week and will lead testing, prompt refinement, and SDR enablement for the new tool.

---

## Key Topics

### Problem: Current Tool Architecture is Inefficient

  - The current 1-Gem-per-account model creates significant friction for SDRs, hindering adoption.
  - **Constraints:**
      - **Gemini:** 10-file limit per Gem.
      - **NotebookLM:** Larger context window, but its suitability for this workflow is unproven.

### Solution: New "Baseline" Gem Architecture

  - A single, "baseline" Gem will be created for each vertical (e.g., Retail, Hospitality).
  - **Process:**
    1.  The Gem is pre-trained on general industry artifacts.
    2.  An SDR uploads a specific account brief to the Gem at the start of a new thread.
    3.  The SDR prompts the Gem, which now has both general industry and specific account context.
  - **Rationale:** This structure avoids context-blending issues while simplifying the SDR workflow.

### ABM Strategy & Tool Integration

  - Rachael is now guiding Okta's ABM strategy to shift from program-centric to account-centric.
  - **New Tiered Model:**
      - **1-to-1 & 1-to-few:** Use detailed account briefs (like the ones GrowthX created) to build hyper-relevant campaigns.
      - **1-to-many:** Use the "baseline" vertical Gem for broad outreach.
  - **Common Room:** Will be used for 1-to-many plays, leveraging data from Clay.

### Competitive & Clay Data Integration

  - Rachael will provide competitive insights (Ping, ForgeRock, Gigya) to enrich the baseline Gems.
  - **Strategy:** Use competitive data for positioning (e.g., "We address common gaps in your current setup") rather than direct competitor bashing, which is explicitly forbidden by existing guardrails.
  - **Clay Data Test:** Compare outputs from a Gem with and without Clay data to validate its value and optimize credit usage.

### Okta vs. Auth0 Product POV

  - Rachael is defining a clear product POV to eliminate internal competition.
  - **Proposed Division:**
      - **Okta:** Traditional banking and healthcare.
      - **Auth0:** SaaS, health tech, fintech, and digital banking.
  - **Validation:** Rachael has requested data on win rates by segment (e.g., Okta wins 40% in banking vs. Auth0's 10%) to confirm this strategy.

---

## Action Items

**Rachael Tiow (Okta)**
- Add Emily to next weekly sync invite
- Share ABM strategist instructions w/ Kyle
- Send Sydney hospitality net-new logo list + B2B SaaS docs/case studies; then Sydney test artifacts
- Share Clay-enriched briefs w/ Sydney; then Sydney run pre/post-Clay tests
- Add Emily to GrowthX Slack channel

**Kyle Gaudreau (GrowthX)**
- Share retail outbound email examples w/ Sydney

---

## Transcript
**Sydney Arin Go:** Hi.

**Kyle Gaudreau:** Hello.

**Kyle Gaudreau:** You almost fooled me.

**Kyle Gaudreau:** Your old background.

**Sydney Arin Go:** No, my background is uglier than this.

**Kyle Gaudreau:** How are you doing?

**Sydney Arin Go:** I'm good.

**Sydney Arin Go:** It's busy.

**Sydney Arin Go:** I'm out of office next week, so I'm trying to scramble everything together and make sure everything is lined up out of office.

**Sydney Arin Go:** Nice.

**Kyle Gaudreau:** What you doing?

**Sydney Arin Go:** Sorry?

**Kyle Gaudreau:** Go ahead.

**Sydney Arin Go:** I don't think we'll need coverage on Auth0 or Okta, because I am going to try to do everything myself in advance this week.

**Kyle Gaudreau:** And if I need to be on support next week, I'll be always online, so.

**Kyle Gaudreau:** You very much deserve it.

**Kyle Gaudreau:** Are you traveling?

**Kyle Gaudreau:** traveling?

**Kyle Gaudreau:** Are you traveling?

**Sydney Arin Go:** Going back to Vancouver?

**Sydney Arin Go:** No, not yet.

**Sydney Arin Go:** So my grandmother's birthday is at the end of October, and she really wanted to go do a Mount Fuji trip.

**Sydney Arin Go:** So we're going to Japan.

**Kyle Gaudreau:** Whoa, that sounds fun.

**Sydney Arin Go:** Yeah, I hope it'll be.

**Kyle Gaudreau:** It's a lot.

**Kyle Gaudreau:** Have you ever been excited?

**Sydney Arin Go:** I am excited.

**Sydney Arin Go:** It's just, you know, I'm excited for all of the things that come with being in Japan.

**Sydney Arin Go:** But have you ever been around a massive Filipino fam?

**Kyle Gaudreau:** No, okay, yeah, yeah.

**Kyle Gaudreau:** But generally, I get, yeah, the traveling with family is a different angle.

**Sydney Arin Go:** So, yeah, I get that.

**Sydney Arin Go:** Hi.

**Rachael Tiow:** Hello.

**Kyle Gaudreau:** Sydney was just telling me she's going to Mount Fuji next week.

**Rachael Tiow:** Oh, nice.

**Sydney Arin Go:** I've never been there.

**Rachael Tiow:** But Japan is fun.

**Sydney Arin Go:** Yeah, it'll be our first time, too.

**Sydney Arin Go:** I've tried to see Mount Fuji multiple times.

**Sydney Arin Go:** Never showed up for me.

**Sydney Arin Go:** Fingers crossed this is the time.

**Rachael Tiow:** What do you mean?

**Rachael Tiow:** Like you showed up and the weather sucked or?

**Sydney Arin Go:** Yep.

**Sydney Arin Go:** I think like three times now.

**Sydney Arin Go:** Different years, three times.

**Kyle Gaudreau:** Oh, great.

**Sydney Arin Go:** Sometimes it may not be your time.

**Sydney Arin Go:** Yep.

**Sydney Arin Go:** Nope.

**Sydney Arin Go:** I'll let you all know if this is it.

**Rachael Tiow:** Send us pictures.

**Rachael Tiow:** Hiking is out in, I'm not speaking from personal experience, but my very good friend's mom, she is 80.

**Rachael Tiow:** I swear she's 80.

**Rachael Tiow:** But she sends us all these pictures about her hiking with her friends.

**Rachael Tiow:** And I'm thinking, wow, the 80, most 80 year olds in the United States have dementia, diabetes, and have had like two hip replacements.

**Rachael Tiow:** And here this woman is like hiking up all these crazy trails.

**Kyle Gaudreau:** As I'm getting older, I can see me not being able to do that.

**Kyle Gaudreau:** So I need to get ahead of it.

**Kyle Gaudreau:** I'm just, I've been feeling so old.

**Rachael Tiow:** Kyle, it's a mindset, and it's also movement is medicine.

**Rachael Tiow:** I think we all live in an age, okay, we don't need to be like Brian Johnson, right?

**Rachael Tiow:** Spending $2 million a year looking like a vampire, but.

**Kyle Gaudreau:** Is that the guy who gets like his son's blood infused?

**Rachael Tiow:** Okay, dude, he does not, okay, he's, he, I've watched some of his videos on YouTube, that dude is a trip, he wakes up and he's like, time to live forever.

**Rachael Tiow:** I was like, it's only people like you.

**Rachael Tiow:** Like you, you're  weirdos.

**Kyle Gaudreau:** Seriously.

**Kyle Gaudreau:** No, that's messed up.

**Rachael Tiow:** No, he doesn't look like a human at all.

**Kyle Gaudreau:** Must be a different guy.

**Kyle Gaudreau:** There's some dude, I can't remember his could be, I'm not surprised.

**Kyle Gaudreau:** I've seen him, uh, pop up in random articles here and there, and.

**Rachael Tiow:** Let's see if it's the same guy, let me pull him up.

**Kyle Gaudreau:** He's been getting his son's blood infused into him for a long time, to like, it's theoretical.

**Kyle Gaudreau:** Because his son's younger, it's like, helps to keep him young, I don't know, it sounds like  to sounds exactly like him.

**Rachael Tiow:** This dude here, hold on, let me see.

**Rachael Tiow:** Yeah, I think you're right.

**Rachael Tiow:** Oh my god, you are right.

**Kyle Gaudreau:** Oh my Oh, it's a guy?

**Kyle Gaudreau:** Yeah, oh man.

**Rachael Tiow:** Nothing about him looks healthy, sorry, let me pull him out.

**Kyle Gaudreau:** Let's talk.

**Kyle Gaudreau:** Oh yeah, yeah, no, it's definitely a guy.

**Kyle Gaudreau:** Yeah, no, it's freaky.

**Kyle Gaudreau:** It's, uh, yeah, it's really freaky looking.

**Kyle Gaudreau:** Yeah, that's the song, you know.

**Kyle Gaudreau:** Man.

**Rachael Tiow:** This is, this is the issue when people have so much money, they don't know what to do with their time, and decide to go for these crazy moonshot ideas.

**Rachael Tiow:** I would love to see him when he dies, because I'll be like, what...

**Rachael Tiow:** What you have to say on your deathbed, Mr.

**Sydney Arin Go:** Johnson?

**Rachael Tiow:** I sound like the grim reaper.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** I feel like this is just a sneak peek into how stressed and your mood has been lately that you're feeling.

**Rachael Tiow:** Did I tell you guys last week how I was just in this mode where if I were told that I had cancer and it's stage four and I have like a month left to live, the person who's just like the people that are just in my way and it's driving me crazy, I'll clobber them to death with this lighter.

**Kyle Gaudreau:** Oh my God.

**Kyle Gaudreau:** What's going on?

**Sydney Arin Go:** Are you okay?

**Sydney Arin Go:** Repressed anger.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** No, no.

**Rachael Tiow:** By the way, it's just my sense of humor.

**Rachael Tiow:** Like if people don't know me, they think like I'm super violent.

**Rachael Tiow:** But I'm like everyone...

**Rachael Tiow:** I have a very good friend, whenever I pick him up before we go riding, he'll get in the car and I'll say to him, Andy, guess what happened?

**Rachael Tiow:** He's like, what?

**Kyle Gaudreau:** Do I need to bring my guitars?

**Rachael Tiow:** Have you watched that Antonio Banderas movie?

**Kyle Gaudreau:** Yeah, yeah, yeah.

**Kyle Gaudreau:** What?

**Kyle Gaudreau:** Oh, boy.

**Rachael Tiow:** In the event of something crazy happening, never submit this call to the courts.

**Kyle Gaudreau:** We'll burn it.

**Sydney Arin Go:** burn it.

**Rachael Tiow:** We raise it from the ether.

**Rachael Tiow:** But anyway, the reason why I sounded like a grim reaper is because I was actually having a conversation with a friend yesterday, no, a couple days ago, and we were talking about death.

**Rachael Tiow:** And I said to him, you know, for a very long time, I never understood why people would be so terrified of death.

**Rachael Tiow:** But then I had this crazy visceral experience where I was standing in my kitchen.

**Rachael Tiow:** It's the weirdest thing.

**Rachael Tiow:** I'm standing in my kitchen.

**Rachael Tiow:** kitchen.

**Rachael Tiow:** kitchen.

**Rachael Tiow:** kitchen.

**Rachael Tiow:** in I'm I'm I'm

**Rachael Tiow:** My backup against the fridge, and I had this moment where I felt, oh my gosh, death feels so scary because all these things I worked so hard for, this pathetic human acquiring all these material items, I'll lose everything.

**Rachael Tiow:** And these things that I so acquire has been giving me so much purpose to work harder as a busy rat on a wheel, only to realize I'm losing it all.

**Rachael Tiow:** Like, it's actually quite scary, and I realized, oh my gosh, yeah, now I know why people are afraid of death.

**Sydney Arin Go:** I feel like this is a heavy chat for 1 a.m.

**Rachael Tiow:** Let's talk about ice cream.

**Sydney Arin Go:** is going to haunt my dreams tonight.

**Kyle Gaudreau:** No, is the I'll let you know what my state of mind is tomorrow.

**Kyle Gaudreau:** This is the fuel you need.

**Kyle Gaudreau:** You need to watch this recording in those late nights where you're trying to stay up and figure out how you're going to keep working.

**Rachael Tiow:** Oh, my word.

**Rachael Tiow:** Okay, we'll talk about happier things.

**Kyle Gaudreau:** I love to eat ice cream.

**Kyle Gaudreau:** What's your dessert of truth?

**Kyle Gaudreau:** I'm a cheesecake guy.

**Kyle Gaudreau:** Although I'm very blessed to, my wife Claire is a really, really good cook and baker.

**Kyle Gaudreau:** And so we do this thing now, we've been doing it for years, but we're in the middle of the season of it, where we love Great British Bake Off.

**Kyle Gaudreau:** And so with two of our good friends, it comes out on Fridays, they come over on Fridays, they come over, she bakes us something new and interesting.

**Kyle Gaudreau:** We didn't eat it, we eat it, we didn't it, and it's just an excuse for us to eat her amazing cooking.

**Rachael Tiow:** Oh, that sounds so fun.

**Rachael Tiow:** Yeah, it's definitely, yeah, that sounds really fun.

**Kyle Gaudreau:** Yeah, and we do, we'll also do like a fantasy league version of this, so we pick who's going to win.

**Kyle Gaudreau:** My team, I've won twice, but now I have no, my team, I'm out, all my people got kicked off already, so I'm the loser this year.

**Rachael Tiow:** So does the loser bake or what?

**Kyle Gaudreau:** But no.

**Kyle Gaudreau:** No, no one wants that.

**Kyle Gaudreau:** We'll go out for dinner.

**Rachael Tiow:** Yeah, exactly.

**Kyle Gaudreau:** Get an order and take out.

**Rachael Tiow:** What about you, Sydney?

**Sydney Arin Go:** I like ice cream, too.

**Sydney Arin Go:** Vegan ice cream, because I found out a couple years ago that I'm lactose intolerant.

**Rachael Tiow:** Oh, I'm so sad.

**Rachael Tiow:** I know.

**Sydney Arin Go:** Me, too.

**Sydney Arin Go:** Developing lactose intolerance after 23 years of knowing the wonders of dairy.

**Kyle Gaudreau:** Yeah, it's almost better to always be that way, so you don't know what it's like.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Like, oh, yeah.

**Rachael Tiow:** You know, we have really fun flavors in Asian countries, Kyle.

**Rachael Tiow:** Like, we have corn.

**Kyle Gaudreau:** Corn ice cream.

**Kyle Gaudreau:** Okay.

**Rachael Tiow:** I would try.

**Sydney Arin Go:** I'm not favorite.

**Rachael Tiow:** And then, of course, the classic mangoes.

**Kyle Gaudreau:** But then we have, like, is it Ube, Sydney?

**Rachael Tiow:** The one in the brand that has purple color, but it's so good.

**Rachael Tiow:** one.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Yeah.

**Kyle Gaudreau:** If only they do like ube soft serve with matcha, you know, like a swirl.

**Kyle Gaudreau:** What is ube again?

**Kyle Gaudreau:** Is it just purple sweet potato?

**Rachael Tiow:** Is that what ube is?

**Rachael Tiow:** No, ube is its own.

**Sydney Arin Go:** purple yam.

**Sydney Arin Go:** Yeah, yeah.

**Kyle Gaudreau:** purple yam.

**Sydney Arin Go:** But it's native, I think, to the Philippines, so I don't know that for sure.

**Rachael Tiow:** Yeah.

**Sydney Arin Go:** We do do, not soft serve, but in the mountains, because there's a lot of them up there, we do this jam that if you put it in the fridge, tastes like soft serve ice cream.

**Sydney Arin Go:** What?

**Sydney Arin Go:** And we just eat it by itself.

**Kyle Gaudreau:** What?

**Sydney Arin Go:** And apparently you're not allowed to bring it, like, in carry-on.

**Sydney Arin Go:** You can do it export, but you're not allowed to bring it in your carry-on or you're in check-in, otherwise they'll confiscate it.

**Sydney Arin Go:** Interesting.

**Sydney Arin Go:** it's, Philippines is hoarding it.

**Rachael Tiow:** Okay.

**Rachael Tiow:** I feel like it's a pancake waffle kind of morning.

**Kyle Gaudreau:** Oh yeah, it's still early for you, eh?

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Oh my gosh, I've been up since 3.30, because I had a call at 4.30.

**Kyle Gaudreau:** What the hell?

**Rachael Tiow:** And I have a rule about I gotta be up at least an hour before my meeting.

**Rachael Tiow:** Like, my warm-up time, I'm like this old Ford model, unlike an Elon Musk Tesla, right?

**Rachael Tiow:** Like, I can't do that.

**Kyle Gaudreau:** Yeah, I'm the same.

**Kyle Gaudreau:** I'm the same.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Okay.

**Kyle Gaudreau:** Let's jump into it.

**Kyle Gaudreau:** I feel like I could always just keep these meetings that way, but that's not what you're paying us for.

**Rachael Tiow:** Real quick, real quick, I have very, very good news.

**Rachael Tiow:** Okay.

**Rachael Tiow:** I'm not dominating the world.

**Kyle Gaudreau:** That's not the good news.

**Kyle Gaudreau:** the good news is, your Kyle's like, that's good news for us.

**Rachael Tiow:** The good news is I got someone starting on my team next week.

**Rachael Tiow:** Amazing.

**Rachael Tiow:** And I am so incredibly excited for her to join the team.

**Rachael Tiow:** I think you'll very quickly tell when she joins the call how polar opposite we are.

**Rachael Tiow:** She's actually very much like Sydney, very calm, very collected.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Not like the...

**Rachael Tiow:** Actually, you two are the same, Kyle.

**Rachael Tiow:** So anyway, you guys will jive really well, and I'm like that crazy fireball in the air, just like ping-ponging around.

**Rachael Tiow:** Very organized, very process-oriented, very thoughtful.

**Rachael Tiow:** So she will...

**Rachael Tiow:** I will get her onboarding with us, and then she will start to do a lot of, like, review of stuff, testing of stuff, because one of the critical things that I want her to look into is with all these artifacts that you've built, which I've reviewed, I thought of creating, like, a baseline in light of ice cream, whether it is lactose-free or not.

**Rachael Tiow:** We need, like, a base, so the hospitality vertical one will be, like, a base, and then we can add accounts to it, which then enriches the gem even more, but if we just kick it off...

**Rachael Tiow:** Because I've been testing the retail artifacts that you guys initially pulled, and also the hospitality, and I just tested...

**Rachael Tiow:** As a base, it's good enough for somebody who has no idea what the hell is going on to at least prompt it to understand, how do I break into retail?

**Rachael Tiow:** It was one of the questions I asked it.

**Rachael Tiow:** So I'm going to have to start working on that.

**Rachael Tiow:** But anyway, I just want to share that.

**Kyle Gaudreau:** super excited.

**Kyle Gaudreau:** Yeah, that's awesome.

**Kyle Gaudreau:** That's awesome.

**Rachael Tiow:** Congrats.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** Yeah, let us know what we can do to help get them up to speed.

**Kyle Gaudreau:** But that's good.

**Kyle Gaudreau:** Yeah, would love that feedback.

**Kyle Gaudreau:** I know you had mentioned some things in the channel.

**Rachael Tiow:** What was that yesterday?

**Rachael Tiow:** Oh, like the email was so funny.

**Kyle Gaudreau:** was.

**Kyle Gaudreau:** Oh, yeah.

**Rachael Tiow:** Beer, Katrina.

**Kyle Gaudreau:** was like, wait, why?

**Kyle Gaudreau:** That's weird because it doesn't say that in the template.

**Rachael Tiow:** I don't know where that.

**Rachael Tiow:** I know.

**Rachael Tiow:** Then I reviewed your instruction and I thought maybe we need to be explicit.

**Rachael Tiow:** Do not start with deer.

**Kyle Gaudreau:** I don't know what its problem was.

**Rachael Tiow:** It's a Gemini problem.

**Rachael Tiow:** I call, I say Gemini like the grandmother trying to use iPhone.

**Kyle Gaudreau:** So.

**Kyle Gaudreau:** The nice thing about Gemini, though, is it does have larger context windows, if we are going to, you know, give them some credit.

**Kyle Gaudreau:** So they are one of the better, like, general LLMs out there when it comes to, like, feeding a lot of context.

**Kyle Gaudreau:** And so that's, like, one of the, they do very well on, like, some, like, the testing scores and things of that nature.

**Kyle Gaudreau:** Sometimes I don't know how much to trust those scores, though, to be honest.

**Kyle Gaudreau:** But that is one of the big values of Gemini right now, is just your context window.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** But, what was I going to say?

**Kyle Gaudreau:** Yeah, like, on the, you know, how it's writing those emails, like, I would say, like, that was the part we probably made the least amount of tweaks to.

**Kyle Gaudreau:** And so very much, like, I think we should continue to come back to those instructions and, you know, modify them over time.

**Kyle Gaudreau:** And be thoughtful about the relative architecture of what, you know, similar to what you were just mentioning of, like, how are

**Kyle Gaudreau:** All these artifacts you use, how to plan the instruction, power it, it was mostly as like a V1 to validate like, does this get us better than we were before, cool, like this seems like a step in the right direction, but like, how do we continue to build off of that, with the mindset being, how do you, for lack of a better way of framing this, like dummy proof this, so you need less enablement from each individual and need them to read these docs and copy and paste these prompts and things of that nature, like, we can always experiment with that kind of stuff, I'm just working under the assumption that those are points of friction that's gonna lead to less adoption and usefulness, and so how can we think of the right architecture and instructions that avoids that, essentially, and so yeah, we can, we should be continuing to evolve this, it sounds like you were even thinking, trying to think back to your note, what you were mentioning, but you.

**Kyle Gaudreau:** You were mentioning something about, like, consolidating more within Notebook, LLM.

**Kyle Gaudreau:** Well, the marketing people, because...

**Rachael Tiow:** Oh, that was just marketing.

**Rachael Tiow:** Yeah, but I have also tested, I have been, this is another thing that I want Emily to, like, really stress test, because so far, what we've talked about has been, hey, if we, ideal is to create that gem per account.

**Rachael Tiow:** But that means...

**Kyle Gaudreau:** I wouldn't call it ideal, to be clear.

**Kyle Gaudreau:** It is the ideal within the, what we know today.

**Kyle Gaudreau:** I think we should continually try to think if there's a better...

**Rachael Tiow:** Yeah, yeah, so the current state is, the idea behind it, the reason behind it is so that it does not blend research context from one account to the next.

**Rachael Tiow:** But what I've also been playing around when it's on the Notebook, LLM, is when I...

**Rachael Tiow:** If the SDR instruction as one of the instructions, as one of the documents in Notebook LM, it seems to do just fine.

**Rachael Tiow:** So, I haven't tested, you know, of course, I gotta ask questions and then review the actual account brief to see if it's smoking crack or not.

**Kyle Gaudreau:** But, like, how many braces did you add to it?

**Kyle Gaudreau:** Like, help me understand a little bit.

**Rachael Tiow:** Yeah, so my thinking right now is, I would prefer, in an ideal world, assuming that the context in LLMs for the Gemini does not hallucinate too much, is that, say that we're all SDRs here and we have 40 target accounts for retail, that we're gonna create our own retail, I call it growth engine.

**Rachael Tiow:** Versus creating one gem per account.

**Rachael Tiow:** Because they have to replicate that process of creating it all the time.

**Rachael Tiow:** The other thing is it's now becoming, it's catching attention.

**Rachael Tiow:** And now I'm getting asked, hey Rach, I want my AEs to use this growth engine.

**Rachael Tiow:** And I'm just thinking, okay, I got to think of a better way.

**Rachael Tiow:** Because I don't trust that they, you'd think it's very simple.

**Rachael Tiow:** But trust me, they lose a lot of things in the, the recipes get lost in the middle.

**Rachael Tiow:** So all of this is say, I got to find a different way.

**Rachael Tiow:** And maybe it's notebook element.

**Rachael Tiow:** Maybe it's agent space.

**Rachael Tiow:** So I've been looking into agent space and see if I could use it.

**Rachael Tiow:** But agent space is quite limited too.

**Rachael Tiow:** Like it's, I, maybe I'm, I'm sure there's something that I'm missing.

**Kyle Gaudreau:** But it's a little bit of walking.

**Kyle Gaudreau:** Not as familiar with because, you know, we don't, yeah.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Oh, in addition to that, if I may add, I'm now, I don't even know what I'm doing anymore.

**Rachael Tiow:** I'm now kind of somewhat pseudo leading ABM again.

**Rachael Tiow:** Oh, that's a game.

**Rachael Tiow:** Congrats.

**Rachael Tiow:** No, I mean, I love it, right?

**Rachael Tiow:** Anything that's hunting, I'm all game.

**Rachael Tiow:** So I'm trying to guide the team through how do you think strategically, by strategically not this nebulous, because you're hired by Deloitte to write some paper around it, but how do you see themes and trends across accounts?

**Rachael Tiow:** And how do you want to cluster accounts?

**Rachael Tiow:** Because I was spending quite a great deal of time yesterday brainstorming with my boss.

**Rachael Tiow:** I said, two things can be true at the same time, right?

**Rachael Tiow:** An account does not need to be in a high intent, but because it's an account we want to do business with, we can tier it as tier one.

**Rachael Tiow:** Because we eventually got to drive awareness to move it down the buying journey.

**Rachael Tiow:** So then the question becomes, well, how do we want to pick our one-on-one accounts, like the whale accounts?

**Rachael Tiow:** How do we want to pick a one-to-few accounts and how do want to pick a one-to-many?

**Rachael Tiow:** So that really got me thinking about, okay, this is really helpful because I used Claude to create an instruction for the gem to be an ABM strategist.

**Rachael Tiow:** Its goal is to identify clusters of themes and trends.

**Rachael Tiow:** And I'm sure at this point, if you all have read at least two account briefs, you'll see there's a consistent pattern in all these companies, right?

**Rachael Tiow:** So I want the ABM or marketing person to use the notebook LM to understand, hey, what are the top three clusters of challenges?

**Rachael Tiow:** I want to prepare content for it.

**Rachael Tiow:** I want to adjust my webinar to speak to these problems, so on and so forth, because that's not what they're doing right now.

**Rachael Tiow:** Right now, they're just picking programs and sending it out to accounts just because...

**Rachael Tiow:** They think that's what they care about, and it's relevant to them, but it's not.

**Kyle Gaudreau:** Shoot me over those instructions.

**Kyle Gaudreau:** I'm happy to, like, see.

**Rachael Tiow:** Yes, I can share them with you.

**Kyle Gaudreau:** Don't judge them too hard, though.

**Rachael Tiow:** Oh, no, no, no, no.

**Kyle Gaudreau:** The intention is to be helpful here, not to be judgmental.

**Kyle Gaudreau:** I just want to help, so it's all good.

**Rachael Tiow:** By the way, as soon as I said that, you froze.

**Kyle Gaudreau:** Oh, I did?

**Kyle Gaudreau:** Oh, I was just saying that the intention is not to judge, it's just the hope.

**Kyle Gaudreau:** So, you know, all good.

**Kyle Gaudreau:** Just curious what you came up with, because that was one thing you had mentioned I was going to start jamming on, but if you've already started, I can see if I have useful thoughts to add to what you've already done there.

**Rachael Tiow:** Kyle, I was totally joking.

**Kyle Gaudreau:** You can totally...

**Kyle Gaudreau:** Oh, no, I know, know, I I did take it seriously.

**Rachael Tiow:** Yes, yes, yes.

**Rachael Tiow:** I mean, I tell people all the time, my ego will get hurt, but it's all necessary.

**Rachael Tiow:** It's all part of the process to become better.

**Rachael Tiow:** So, feel free to give me your honest opinion.

**Kyle Gaudreau:** Oh, yeah, sure.

**Kyle Gaudreau:** The reason I pulled this up real quick, by the way, you were, now I know you were just talking about notebook.lm in that context, but as we take it back to gems, the thing that we need to be mindful of, and let me know if this looks different in your instance, because I'm, no, I guess I do have a, I don't know how I have a pro account.

**Kyle Gaudreau:** I guess maybe growthx bought me one that I'm not aware, I don't know what's happening.

**Kyle Gaudreau:** Anyways, we can only add up to 10 files per gem.

**Kyle Gaudreau:** Yeah, so you're maybe already on your radar or whatever, but it's just something we have to be mindful of with like the structure.

**Rachael Tiow:** By the way, would you know, does Agent Space, Notebook.lm, and Gemini all use the same LLM engine that they have built themselves?

**Kyle Gaudreau:** This just literally would use Gemini, Agent Space, I don't know.

**Rachael Tiow:** Okay.

**Rachael Tiow:** Because the thing is, if, to your point, they are actually pretty good with context management.

**Rachael Tiow:** Actually, I've tried using your same instruction in the Notebook LM.

**Rachael Tiow:** It worked.

**Rachael Tiow:** I can demo it for you right now, if you like.

**Kyle Gaudreau:** Oh, yeah.

**Kyle Gaudreau:** I'm not surprised about that.

**Kyle Gaudreau:** mean, they should be relatively, like, adaptable.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** You know, a ChatGPT, a Claude, whatever.

**Kyle Gaudreau:** It was less like, how does a Gemini specifically work, and more, what are the outputs we want to...

**Rachael Tiow:** Ah, I see what you mean.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Okay.

**Kyle Gaudreau:** So, if we need to jump into another system at one point, whatever, like, I think a lot of what we're talking about here can be transferred.

**Kyle Gaudreau:** I don't know.

**Kyle Gaudreau:** Part of this makes me now start to think, I'm not pushing for this now, but, like, how...

**Kyle Gaudreau:** How much should we be doing account-specific briefs versus industry-specific, and what's the value of that, and the structure, and et cetera?

**Rachael Tiow:** Ok, so yesterday, I read, I'm halfway through, I read Sephora, Adidas, I've already read Tesco and Sainsbury's account briefs.

**Rachael Tiow:** So all this hard work that you guys are doing, I am really reading them.

**Kyle Gaudreau:** That's good to know.

**Rachael Tiow:** Yes, yes, it's my insomniac reading material.

**Rachael Tiow:** No, just kidding, it's so interesting to me, like when I read it, and I'm studying the accounts, and I'm just thinking, holy .

**Rachael Tiow:** Ok, so as I was going through it, it kind of got me thinking, am I over, ok, am I overthinking this by trying to pull context at an account?

**Rachael Tiow:** I'm sure there is value in that.

**Rachael Tiow:** I guess what I'm trying to lead to is, there's value in an overall vertical-specific artifacts.

**Rachael Tiow:** Let's Let's Let's get started.

**Rachael Tiow:** get get Thank you.

**Rachael Tiow:** And I think if we can feed it enough from what we're pulling from, hey, here are common challenges that we see large enterprise retailers are going through, and we add Adidas and all the stuff in there.

**Rachael Tiow:** They're not our customers, but they're just to build more context.

**Rachael Tiow:** I think it can work as well, like as if I'm prospecting Nike.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Like it's relevant enough to be dangerous, you know?

**Kyle Gaudreau:** There's also a way, again, like every idea I feel like that we're going to have is going to have some pros and cons, and we just have to be like full of like which ones are we most comfortable with from a con standpoint.

**Kyle Gaudreau:** There's another way we could think about like the structure of the gem where, yeah, it's very much built with the industry-specific briefs.

**Kyle Gaudreau:** I'll call them like industry-specific gems.

**Kyle Gaudreau:** We train that in a whole variety of different ways.

**Kyle Gaudreau:** We just dial it in.

**Kyle Gaudreau:** And we feel good about its relative like repeatability of what it's doing.

**Kyle Gaudreau:** We still do a con.

**Kyle Gaudreau:** But the account briefs are, let me just actually share again, just to make sure it's clear.

**Rachael Tiow:** The account briefs are so good.

**Rachael Tiow:** I ran it, as you're pulling this out, I'm as a company, we need to move faster, because Adidas has completely called out this $1 billion investment with SAP, and SAP has Gigia.

**Rachael Tiow:** They're apparently deprecating Gigia.

**Rachael Tiow:** I'm like, guys.

**Kyle Gaudreau:** didn't even know Gigia was all around.

**Kyle Gaudreau:** I haven't heard that name in years.

**Rachael Tiow:** I know, but Gigia was like everything in retail.

**Rachael Tiow:** They were a very tough competitor for us, in Europe especially.

**Kyle Gaudreau:** Anyway, I digress.

**Kyle Gaudreau:** So, good to hear.

**Kyle Gaudreau:** And that's why I'm also hesitant to just say we don't do the account briefs.

**Kyle Gaudreau:** And so, a potential solution here would be, okay, let's call, like, obviously, what I'm showing is more of a Cole Haan-focused solution.

**Kyle Gaudreau:** Test gem, let's call it a retail-focused gem, the resources we feed in, the instructions, all very much industry-centric, the kind of outputs we want.

**Kyle Gaudreau:** We still have the account briefs, we figure out the proper place and methodology of where to store that for accessibility for your SDRs.

**Kyle Gaudreau:** And as they come to this, they can just do the briefs and start the thread by feeding in that context and asking those questions.

**Kyle Gaudreau:** And so it has the benefit of not producing a  ton of gems and having, like, you know, gems.

**Kyle Gaudreau:** It has the downside of just folks finding that brief, uploading it, kicking off the prompt in the right way.

**Kyle Gaudreau:** But honestly, like, that part's, like, pretty dang simple.

**Kyle Gaudreau:** Like, it relatively, like, usually a best practice here is, like, when you're going to feed.

**Kyle Gaudreau:** And as much context as a brief like that, and you have this project, like, you just want to kind of, like, warm the LLM a little bit with the context, and that's super easy to do, and then they can build off of that in the thread and start to ask, like, further questions and play around with everything we've instructed the gem to do.

**Kyle Gaudreau:** Yep.

**Kyle Gaudreau:** There's different versions we can play around with, but that is a potential, not the most ideal solution that's out there, perhaps, but maybe an enhancement of what we're doing now, I don't know.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Where they go and find that, though, you know, and do they do that consistently?

**Rachael Tiow:** Which is, yeah, so if they do it that way, and they can, that one, I don't even know, that one is, I'm also solving a bigger issue at hand right now.

**Rachael Tiow:** I think I've mentioned this to you guys before, looking into common room.

**Kyle Gaudreau:** Oh, yeah, yeah, what's going on with that?

**Rachael Tiow:** You know, I had a call this morning, and it's straight

**Rachael Tiow:** Me out all week of last week.

**Rachael Tiow:** I was actually really upset last week because I was like, why am I spending five hours, six hours, putting all these slides and trying to tell them what the problems are when it is so obvious?

**Rachael Tiow:** And of course, my executive sponsor said, Rachel, you see the problem.

**Rachael Tiow:** A lot of us don't.

**Rachael Tiow:** So you need to paint that picture for us.

**Rachael Tiow:** Yeah, you need to align us on the true norm.

**Rachael Tiow:** So it went really, really well, actually.

**Rachael Tiow:** In my, in my, in my, I had to put on my sales hat.

**Rachael Tiow:** So I met with all the key stakeholders that were going to be on the call to socialize it with them, see where they're at, suss out their appetite.

**Rachael Tiow:** So I kind of go in knowing, I'm like, this is going to be a very solid call because they have been exposed and because they were exposed and I did a lot of handholding and making sure they read the pre-read.

**Rachael Tiow:** on side of

**Rachael Tiow:** It was a very engaging call.

**Rachael Tiow:** I think we left the call understanding that the true north that we're all looking towards is not just exterior productivity, but really what we're calling for is pipeline productivity and conversion.

**Rachael Tiow:** And very, very importantly, for net new logos, because right now a lot of us are spending time on customers.

**Rachael Tiow:** Why?

**Rachael Tiow:** That's an account manager's job, right?

**Rachael Tiow:** So that was a very, I'm glad they came to that conclusion, even without me being explicit about it.

**Rachael Tiow:** And I think I kind of had that moment of, wow, this is how an effective making goes, because they're all talking amongst themselves, but they're getting to the point that I want them to get to.

**Kyle Gaudreau:** So I'm like, okay, thank accepted them.

**Rachael Tiow:** Like a dream.

**Rachael Tiow:** It went really well.

**Rachael Tiow:** And then one of the things that came.

**Rachael Tiow:** So yesterday when I spent an hour talking to Janice, she says, Rachel, how are all this account briefs that y'all are working on going to work?

**Rachael Tiow:** I said, the thing with Common Room is it's not going to be as rich in context as it would be as what you guys are pulling.

**Rachael Tiow:** So we'll still need it, but where we'll need it is much more for one-on-one, one-to-few ABM plays.

**Rachael Tiow:** And then Common Room, we can still feed because like the clay stuff that I pull, we can pump it in there and that's for one-to-many.

**Rachael Tiow:** So that's why I came to this kind of situation where I'm thinking about exactly what we're all coming towards is a baseline artifacts gem or engine where you learn and you know everything can help you break into 60% of all the retail accounts.

**Rachael Tiow:** Whereas when we're doing one-on-ones like the Adidas of the world and maybe like some clusters of accounts, we want to do one-to-few, that will require.

**Rachael Tiow:** A lot of these kind of briefs, and I think it will be much more manageable to them in the event where they want to create their own gem, and I really recommend it too, right?

**Rachael Tiow:** I think they are missing a big part of the picture if they don't even read the briefs, and it doesn't even take that long.

**Rachael Tiow:** Guys, it took me 10, 15 minutes to scan through Adidas, and then the ones I'm like, oh, this caught my attention, I just double-click in it.

**Rachael Tiow:** And then the other way to really get familiar with the account briefs was I asked, while I was reading the brief, I just asked the notebook LM.

**Kyle Gaudreau:** What's the issue here with SAP?

**Rachael Tiow:** So I guess all of this is I'm figuring out how to drive adoption, because that's one thing that Emily will be focused on, is driving adoption and enablement for using these briefs.

**Rachael Tiow:** And I think it will be very, very helpful, because we're going to be using this to drive ABM and ABX strategy, or I guess the same thing.

**Rachael Tiow:** But between us all, he and my manager...

**Rachael Tiow:** ...

**Rachael Tiow:** ...

**Rachael Tiow:** She me earlier this week, she's like, Rachel, I am so frustrated.

**Rachael Tiow:** I'm like, what's going on?

**Rachael Tiow:** She's like, I got two ABM teams.

**Rachael Tiow:** And none of them have a  clue on their ABM strategy.

**Rachael Tiow:** So now I've stepped in to help build that thing out.

**Kyle Gaudreau:** Meaning you have an Auth0 and an Okta, or are you meaning...

**Rachael Tiow:** We have an ABM team for both.

**Kyle Gaudreau:** They're merged as one.

**Rachael Tiow:** But one in Amer and one in Amiya.

**Kyle Gaudreau:** And yeah.

**Rachael Tiow:** So I'm going to be building it out.

**Rachael Tiow:** I'm going to help guide them on the strategy, which has always been my plan.

**Rachael Tiow:** Because when I first got in, I could tell that they don't know what the heck they're doing.

**Rachael Tiow:** They're a very program-centric team, but they're not really thinking about it as, why are we choosing Coca-Cola over Pepsi?

**Rachael Tiow:** That kind of a thing.

**Kyle Gaudreau:** That makes sense.

**Rachael Tiow:** Okay, anyway, I didn't mean to digress.

**Rachael Tiow:** I know we're past time.

**Rachael Tiow:** I'm going to add all these other artifacts, and I've been reading the artifacts too, and I thought, wow, this is pretty darn good in context-laying, and I really like the one where you guys are painting the A Day in the Life of whoever.

**Rachael Tiow:** Yeah, yeah, yeah.

**Rachael Tiow:** I'm going to task Emily to start building out those engines as a baseline and work closely as a team, all of us, where she'll definitely have more bandwidth to test up prompts.

**Rachael Tiow:** And I'm sure you'll enjoy working with her a lot more than me, guarantee.

**Kyle Gaudreau:** I don't know about that.

**Kyle Gaudreau:** Different flavors of good.

**Rachael Tiow:** Real quick, I got to make a trip to SF, Sydney, when you're back, and then maybe we'll do, hey, can you do dim sum?

**Rachael Tiow:** Are you gluten, allergic to gluten or no?

**Sydney Arin Go:** No, but I'm also a Vancouver, not in San Francisco.

**Rachael Tiow:** Oh my gosh, yes!

**Kyle Gaudreau:** No, we can fly you out for that, you know.

**Rachael Tiow:** Well, but then the other thing is this.

**Rachael Tiow:** out for I'm a

**Kyle Gaudreau:** Vancouver has much better dim sum than SF.

**Sydney Arin Go:** Oh, yeah.

**Kyle Gaudreau:** true.

**Rachael Tiow:** I would probably.

**Rachael Tiow:** So, Kyle, maybe.

**Kyle Gaudreau:** Hey, I've always wanted to go back.

**Rachael Tiow:** I've only been once and I loved it.

**Rachael Tiow:** I'm literally like a stone throw away.

**Rachael Tiow:** can just drive up from Seattle.

**Rachael Tiow:** Yeah, no, everything looks to be doing well.

**Rachael Tiow:** By the way, too, the reason why also as I'm thinking about this like sort of base, I don't call it generic because it's not generic.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** It's because of Okta.

**Rachael Tiow:** Okta has been a little bit of a conundrum for me.

**Rachael Tiow:** Workforce is super easy.

**Rachael Tiow:** It's so easy to understand.

**Rachael Tiow:** It's internal users.

**Rachael Tiow:** It's a very strict B2B use case.

**Rachael Tiow:** But when it comes to Okta's customer identity versus Auth0, that one, I'm still, yeah, I told my boss, I said, I am taking a very strong stance and I'm going to develop a POV.

**Rachael Tiow:** I could be completely wrong.

**Rachael Tiow:** I But I.

**Rachael Tiow:** I.

**Rachael Tiow:** I'm also half right, I told her.

**Kyle Gaudreau:** I thought it was very interesting that the latest email that I shared, how Auth0 and Okta were both framed, the average person has no idea about that.

**Rachael Tiow:** It's really bad.

**Kyle Gaudreau:** It's really bad.

**Rachael Tiow:** That's why when you send me all these things, I'm like, so embarrassing.

**Rachael Tiow:** We're going to change this.

**Rachael Tiow:** I don't feel embarrassed because it's not my team, but you're right.

**Rachael Tiow:** By the way, Kyle, besides the everyday human that's not in this space, do not know the distinction between the two.

**Rachael Tiow:** The fact that we don't know makes it really...

**Kyle Gaudreau:** Oh, yeah, yeah, absolutely.

**Rachael Tiow:** It's like we don't know why there's Fuji apples and Honeycrisp apples and how they're different.

**Rachael Tiow:** They're just apples.

**Rachael Tiow:** No, they're different.

**Rachael Tiow:** I just bought some apples yesterday, that's why.

**Kyle Gaudreau:** It is almost apple season.

**Kyle Gaudreau:** guess, well, maybe it is.

**Rachael Tiow:** I don't know.

**Rachael Tiow:** Fun fact, though, apples that we buy in the store were harvested at least a year ago.

**Kyle Gaudreau:** Yeah, well, we're big farmer's market people nowadays.

**Kyle Gaudreau:** Okay, that's good.

**Kyle Gaudreau:** So we try to find a good, take our son, go to the playground, go to the farmer's market.

**Rachael Tiow:** That's so fun.

**Rachael Tiow:** Yeah, yeah, yeah.

**Rachael Tiow:** And you can go to UPIC Farms.

**Rachael Tiow:** I was just feeling kind of sad yesterday.

**Kyle Gaudreau:** I wanted to buy an apple because I want to make tuna salad and not use grapes.

**Rachael Tiow:** And I looked at those apples and I felt so sad.

**Rachael Tiow:** I'm like, I know you were harvested at least a year ago.

**Rachael Tiow:** And have you ever been radiated?

**Rachael Tiow:** Not the same.

**Rachael Tiow:** Not the same.

**Kyle Gaudreau:** Not the same.

**Rachael Tiow:** Okay, anything I can do to help you guys?

**Kyle Gaudreau:** Yeah, Sydney, is there anything we need right now, like in terms of clarity of accounts or anything?

**Sydney Arin Go:** I'm trying to work on.

**Sydney Arin Go:** Yeah, the only thing that we can do moving forward currently is we can pick two verticals to prioritize and then give me...

**Sydney Arin Go:** Some accounts to test the artifacts on, and then I can send you those.

**Rachael Tiow:** You really want to test, Sydney?

**Rachael Tiow:** Okay, I don't have all these fancy things that Brad, whoever, all the other people have shared with you, but on the B2B SaaS is what I really want to.

**Rachael Tiow:** And there's definitely nuances.

**Rachael Tiow:** When we built B2B SaaS, we had to build one for enterprise and one for commercial.

**Rachael Tiow:** I have documents on it.

**Rachael Tiow:** I can share them with you.

**Rachael Tiow:** One of the key distinctions for the SaaS part for enterprise and commercial is typically when you're a company that's about 200 to 300 large, you're slowly moving up market.

**Rachael Tiow:** That means if you're going to start to close deals with companies like Zapier, Salesforce, they will require enterprise layer, enterprise federation, we call it, but that's literally the enterprise layer for SSO.

**Rachael Tiow:** Now, without without it...

**Rachael Tiow:** Manually got to code it or they got to depend on Salesforce.

**Rachael Tiow:** And chances are companies are going say, well, because of that, we're not going to do business with you.

**Rachael Tiow:** So that's a very different reason than why a company like Salesforce would buy Auth0.

**Rachael Tiow:** Salesforce would buy Auth0 because they have acquired so many tools.

**Rachael Tiow:** Trying to keep up with all of them is just way, way too challenging.

**Rachael Tiow:** So that key distinction is super important.

**Rachael Tiow:** It's most people overlook that, but that is actually a very critical component between these two.

**Rachael Tiow:** But I have documents.

**Rachael Tiow:** I can share them with you.

**Rachael Tiow:** I can find customer case studies and share them with you.

**Rachael Tiow:** I want to ask you guys on competitive insights.

**Rachael Tiow:** So this is such a cumbersome thing.

**Rachael Tiow:** So thank God I have Emily because maybe I should get an intern to do these kind of things.

**Rachael Tiow:** We have tons of competitive insights against Ping, ForgeRock, SAP.

**Rachael Tiow:** Gigia, but they don't want to share them like a Google Drive, like the PMM team has done a lot of research, like they share with you guys.

**Rachael Tiow:** So I've got to manually export it.

**Rachael Tiow:** But that's something that I thought, hey, maybe that could help.

**Rachael Tiow:** Like if we know that a company uses Gigia or Ping, then that artifact can be helped, can be built into your context, right, is what I'm thinking.

**Sydney Arin Go:** Or maybe I'm adding too many things in here.

**Sydney Arin Go:** No, I think we can add that in.

**Sydney Arin Go:** Um, okay.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Yeah.

**Kyle Gaudreau:** I think the key is like, how confident you are in the accuracy of that.

**Kyle Gaudreau:** Uh, because I am always skeptical of those insights, just in what I've seen in the past.

**Rachael Tiow:** Competitive insights?

**Kyle Gaudreau:** In terms of like, that they, like this brand uses that, those sorts of like technographic, like they use this product.

**Kyle Gaudreau:** Like, it's not that I've never...

**Kyle Gaudreau:** never...

**Kyle Gaudreau:** It's

**Kyle Gaudreau:** Seeing value from it or whatever.

**Kyle Gaudreau:** It's just like so many players have come and gone in that space.

**Rachael Tiow:** We're buying HG Insights.

**Kyle Gaudreau:** Yeah, I haven't, so I can't speak a ton to, like, at least to my recollection, I don't remember really experimenting with their data much.

**Kyle Gaudreau:** And, you know, I'm just naturally skeptic of a lot of, like, intent, signal, whatever data.

**Kyle Gaudreau:** It's not like that there isn't value, it's just like, how accurate is it?

**Kyle Gaudreau:** And so, I'll operate under the assumption that, you know, you all have already validated it and you trust it and so it's all good.

**Kyle Gaudreau:** But it's just the thing to be careful of because, like, I do feel like if it becomes too heavy a part of your motion and mix and then you don't have it, I sometimes see these things and the outreach to me and of these signals and I'm just like, your signal was wrong and you just immediately lost my attention.

**Rachael Tiow:** Well, this is how I'm hoping when we, I don't know how, okay.

**Rachael Tiow:** What I always recommend that people do is you don't go tell a company, hey, we know you use GigGit, right?

**Rachael Tiow:** Oh, yeah, for sure.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** And of course, if they do that, for sure, I'm like, you've just pissed people off.

**Rachael Tiow:** I'm hoping that we can scrape the context, say, if we kind of somewhat, I don't expect the insights on technographics are 100%, but let's just go in with the baseline.

**Rachael Tiow:** 60% is accurate.

**Rachael Tiow:** So it's a hit and miss, right?

**Rachael Tiow:** You can strike gold or you could just completely miss.

**Rachael Tiow:** But where are the gaps in any of our competitors?

**Rachael Tiow:** We talk about it in a very overall way without taunting our competitors.

**Kyle Gaudreau:** Because if you do that, to me, I'm like, that is such a low-class act.

**Kyle Gaudreau:** I'm like, come on.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** And that reduces the stakes of accuracy because it's less obvious and you're more focused on positioning.

**Rachael Tiow:** And that positioning can still be relevant regardless.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Because the philosophy here is...

**Rachael Tiow:** I'm not reaching out to tell you that your existing setup sucks.

**Rachael Tiow:** That's rude.

**Rachael Tiow:** And that's just going piss people off.

**Rachael Tiow:** My position is, hey, there are gaps.

**Rachael Tiow:** And I'm aware, chances are you have these kind of challenges.

**Rachael Tiow:** And here's how it can be addressed.

**Rachael Tiow:** Potentially, we don't know.

**Rachael Tiow:** We'll have a thought exercise and see how that goes.

**Rachael Tiow:** So it's not a hard pitch, a hard sell in any way.

**Rachael Tiow:** I hope at least that's how SDRs are really going to adopt this practice.

**Rachael Tiow:** But soon, soon, with all these artifacts that we've got, right?

**Rachael Tiow:** Real quick to just side note, I've been testing the retail one to just write outbound emails.

**Rachael Tiow:** Even without an account associated to it, comes up pretty darn good.

**Kyle Gaudreau:** I'll share them with you.

**Rachael Tiow:** That's cool.

**Rachael Tiow:** So that's enough for us to go in and talk to prospects, yeah?

**Rachael Tiow:** So that's at least my thought.

**Kyle Gaudreau:** I think there's something to build off there for sure.

**Kyle Gaudreau:** It's just a matter of what context do we feed in?

**Kyle Gaudreau:** You know, aligning on that, making sure, yeah, it's not skewing the direction of, like, competitor bashing, where that would bleed through maybe unintentionally into the gems, and that could, you know, start to make it into messaging more than we would intend.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So, like, that kind of stuff of, like, do they use it, but also as well as, like, what is Acero or Okta's, like, perspective on your relative strengths versus their needs.

**Kyle Gaudreau:** So, so, yep.

**Rachael Tiow:** Back in bold.

**Rachael Tiow:** Okay, sorry, go ahead, Sydney.

**Sydney Arin Go:** I do think our account briefs currently have that actually very, very explicitly at the very end.

**Sydney Arin Go:** It says, do say this, don't, and then a couple of the don'ts are don't bash your competitors.

**Sydney Arin Go:** It's very, very clear on that.

**Kyle Gaudreau:** Yeah.

**Sydney Arin Go:** Because I did notice, like, originally it started doing that, I'm like, uh, let's not.

**Sydney Arin Go:** So, it is quite explicitly in there.

**Sydney Arin Go:** Um, but we can add more guardrails.

**Sydney Arin Go:** Um.

**Rachael Tiow:** Okay, the other one.

**Rachael Tiow:** Okay, so I'll get you a couple accounts to test them.

**Rachael Tiow:** Hospitality is a very good one to start.

**Rachael Tiow:** I just got to find a solid list of net new logos.

**Rachael Tiow:** I'll get that to you by tomorrow.

**Rachael Tiow:** Okay, earliest by end of day.

**Rachael Tiow:** then the other one, I'll send you the SaaS stuff.

**Rachael Tiow:** And I'm very keen to see as you guys start working on Okta.

**Rachael Tiow:** This is my strong stance.

**Rachael Tiow:** I'll send you guys on a document.

**Rachael Tiow:** My strong POV is Okta goes after traditional banking and healthcare, and Azure does all things SaaS, like health tech, fintech, digital banking.

**Rachael Tiow:** I will have a report by end of week from the data team, because I sent...

**Rachael Tiow:** A ticket for them to analyze, to provide some analysis around where have we been close winning as a business for Okta in FinServ and OddsZero.

**Rachael Tiow:** And I want the distinction between banking and fintech.

**Rachael Tiow:** If OddsZero is winning 10% and Okta is winning 40%, just move the whole lot over to Okta.

**Kyle Gaudreau:** Makes sense.

**Rachael Tiow:** The pie is really big, guys.

**Rachael Tiow:** Like, stop trying to kill each other along the way.

**Rachael Tiow:** So, yeah, anyway, so that's that.

**Rachael Tiow:** And then one thing I'm keen on exploring right now is the breeze that you pulled recently, Sydney, has no clay context.

**Rachael Tiow:** And it's really interesting.

**Rachael Tiow:** I had the managed services pull clay data on those accounts.

**Rachael Tiow:** I'll share them with you guys, too.

**Rachael Tiow:** I wonder if.

**Rachael Tiow:** We run it through your engine, how that will differ free and post-clay.

**Rachael Tiow:** Now I'm kind of anxious because we're negotiating for more clay credits.

**Rachael Tiow:** We can look at that like a version with or without just to see.

**Rachael Tiow:** because the reason why is I see clay being very useful, but where?

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** And what additional context that you'll need that they can provide versus us just pulling, I don't know.

**Rachael Tiow:** So we'll find out, we'll find out.

**Rachael Tiow:** Because what this does then is I may not need to spend so many credits pulling things from clay.

**Rachael Tiow:** I just got to pull like the pertinent ones to help add more context to your engine as you're building it out.

**Rachael Tiow:** So those are a few things I'm thinking about.

**Rachael Tiow:** I'm like, where can I conserve credits and so on and so forth?

**Rachael Tiow:** Because right now what I have managed, this is.

**Rachael Tiow:** Do on the clay side is to build like a table to scrape for retail, hospitality, fintech, health tech, and sass.

**Rachael Tiow:** I know it feels like it's a little bit much, but we'll find out.

**Rachael Tiow:** And I have the budget to spend.

**Rachael Tiow:** If I don't spend it, then it's just going to go to digital ads.

**Kyle Gaudreau:** What a  waste.

**Kyle Gaudreau:** Yeah, we can definitely experiment with that.

**Kyle Gaudreau:** I think there could theoretically be, though, still some value of just its ability to plug into some of the systems that are just designed and just been refined to provide more consistent signal around things.

**Kyle Gaudreau:** And, you know, it's not that we can't replicate that in some ways, but in the publicly available data we have, sometimes it might not be as reliable.

**Rachael Tiow:** Yeah, because what I'm thinking is if you guys are more on the call.

**Rachael Tiow:** Context side, clay can be more of the, what I call, like, the filmographic side.

**Rachael Tiow:** Right.

**Rachael Tiow:** And then the nice thing is you guys can validate, too, because clay is not, like, the Bible of truth on everything, right?

**Rachael Tiow:** So, yeah.

**Kyle Gaudreau:** Cool.

**Rachael Tiow:** Cool.

**Rachael Tiow:** All right.

**Rachael Tiow:** Very good catching up.

**Rachael Tiow:** Hopefully your dreams won't be as scary now, Sydney.

**Kyle Gaudreau:** Oh, no.

**Kyle Gaudreau:** Might not.

**Rachael Tiow:** She'd like, I'm dreaming of ice cream.

**Kyle Gaudreau:** Yeah, yeah, yeah.

**Rachael Tiow:** Cool.

**Rachael Tiow:** All right.

**Rachael Tiow:** I appreciate you guys.

**Rachael Tiow:** And next week, I'm going to add Emily to the call.

**Rachael Tiow:** Cool.

**Rachael Tiow:** I'll add her to the channel come Monday.

**Rachael Tiow:** I want her to just focus on her work and not worry about this crazy team of one at the moment.

**Kyle Gaudreau:** Sydney will be in Japan.

**Kyle Gaudreau:** So, I'll hold it down for us.

**Rachael Tiow:** Okay.

**Kyle Gaudreau:** So.

**Kyle Gaudreau:** Eat some good food for her.

**Kyle Gaudreau:** She was teasing the idea of jumping on.

**Kyle Gaudreau:** I was like, no.

**Rachael Tiow:** No.

**Rachael Tiow:** Oh, gosh.

**Rachael Tiow:** Sydney.

**Kyle Gaudreau:** Seriously?

**Kyle Gaudreau:** No.

**Kyle Gaudreau:** Go do your Mount Fuji thing.

**Sydney Arin Go:** Go Go

**Sydney Arin Go:** I will say you were online when you were offline as well.

**Sydney Arin Go:** Yeah, Rachel said about it.

**Sydney Arin Go:** I it runs in the industry.

**Rachael Tiow:** Well, but then also because I'm in Hawaiian time.

**Kyle Gaudreau:** Yeah, yeah.

**Rachael Tiow:** Like, it's kind of weird.

**Rachael Tiow:** Like, Kyle, you're almost 1 p.m., yeah?

**Kyle Gaudreau:** Oh, no, no, no, 11 a.m.

**Kyle Gaudreau:** Oh, 11 a.m.?

**Kyle Gaudreau:** Almost 11, yeah.

**Rachael Tiow:** Okay.

**Rachael Tiow:** It's almost 8 a.m.

**Kyle Gaudreau:** here, but I feel like I'm ready for lunch.

**Kyle Gaudreau:** That's kind of, you know, bad if you just end up starting early and working super late your time, but, hey, if you get to end a bit early, enjoy that amazing weather, get some outdoor time.

**Rachael Tiow:** Yes, I'll send you guys some pictures.

**Kyle Gaudreau:** Please, I'd love to see it.

**Rachael Tiow:** Yeah, cool.

**Rachael Tiow:** All right, guys, thank you so much.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** All right, talk soon.

**Rachael Tiow:** Bye.
