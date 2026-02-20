# CheckThat Weekly Check In

<metadata>
date: 2026-02-18
time: 20:30 UTC
duration: 53 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Nigel Hammett, Stevie Kim, Jose Farias
fireflies_id: 01KH4KDKBC72Z8XKM9Y6XRS7WC
meeting_link: 
transcript_url: https://app.fireflies.ai/view/01KH4KDKBC72Z8XKM9Y6XRS7WC
</metadata>

---

## Summary

The CheckThat team reviewed user engagement (only one workspace invitation since Friday), engineering constraints (database migration underway, team down to two engineers), and Marcel's evolving brand intelligence framework. Marcel introduced a new composite scoring model across four vectors — presence, reputation, perception, and influence — and outlined plans for a curated brand report deliverable by Friday to support Nigel's sales outreach.

---

## Context

This is CheckThat's weekly product and strategy sync. CheckThat is GrowthX's AEO (AI Engine Optimization) measurement product — it tracks how brands appear and perform in AI-generated responses during buyer research. This meeting is where the product roadmap, measurement methodology, and go-to-market strategy for CheckThat are developed in real time. Marcel is actively shaping the product's conceptual framework while the engineering team builds the underlying system.

---

## Relevance

**To CheckThat:**
- Only one workspace invitation since Friday — traction is very early-stage and engagement is limited
- Nigel is the sole sales driver; his calls with smaller startups are generating positive signal but surfacing terminology and roadmap questions
- Marcel introduced a four-vector measurement model: Presence, Reputation, Perception, Influence — each scored as a composite 0–10
- 3D bubble chart visualization proposed to map brands across presence × perception × reputation with trend arrows
- Data system migration to support multidimensional slicing (by Personas, tags, dimensions) — Jose estimates a few days of engineering
- Brand reports planned: single-page curated audit combining public brand data + deep research insights, partially gated (require signup for detail)
- Handbook repo shared with team to align on context and workflow — Marcel will push latest changes for workflow developers

**To GrowthX Services:**
- Brand report concept mirrors an enhanced version of existing AEO audit tooling — could be a lead generation asset for the agency
- Marcel sees CheckThat as a funnel entry point: brand report → strategy session → GrowthX services engagement

---

## Overview

- User growth concerns: only one workspace invitation since Friday; traction challenges at early stage
- Engineering capacity: database migration underway; team reduced to two engineers this week (Pedro absent)
- Strategic brand framework: new model positions AI agents as primary buyer influencers; emphasizes buying categories vs. market categories
- Measurement model: four composite vectors — Presence, Reputation, Perception, Influence — with 3D visualization
- Flexible data strategy: migration to new analytics system to support multidimensional brand performance views
- Brand reports development: single-page curated audit, partially gated, targeting lead generation and sales enablement

---

## Key Topics

### User Engagement and Early Traction

Only one user has invited another person to their workspace since Friday. Nigel's outreach calls with smaller startups are generating positive qualitative signal — users see value in filtering branded vs. non-branded contexts and agree with default Persona settings. Questions are emerging around future roadmap (what actions stem from insights?) and unfamiliarity with some terminology. This signals both genuine interest and a need for clearer onboarding and product education.

### Strategic Brand Intelligence Framework

Marcel articulated a layered mental model for brand analytics built around three audiences: buyers, AI agents, and training bots. The core insight is that AI agents are now primary influencers in buying decisions — brands need to understand how they appear and perform in AI-generated context, not just in human search results.

Two key distinctions drive the framework:
- **Buying categories**: what buyers actually search for and purchase (e.g., "sales enablement software")
- **Market categories**: the broader competitive landscape brands compete within

A continuous, auto-improving graph system would capture brands, markets, and buyer personas — enabling actionable intelligence and SEO-style compounding benefits over time.

### Composite Scoring Model

Marcel introduced a four-vector measurement system:
- **Presence**: AI visibility and stability across engines during buyer evaluation stages (composite score)
- **Reputation**: aggregated analyst reviews and community feedback, tiered like Gartner Magic Quadrants (trust, innovation, support)
- **Perception**: AI-generated narratives on brand attributes across six buyer-relevant dimensions (0–10 composite)
- **Influence**: brand's ability to shape buyer decisions through onboarding, intelligence setup, and internal configuration

Visualization: 3D bubble charts combining presence × perception × reputation, with trend arrows showing trajectory. The goal is a quick visual read on brand positioning and risks.

### Technical System Migration

Jose is optimistic about migrating to a new, more flexible analytics backend. No technical blockers. Estimated lift: a few days of focused engineering. The new system will support slicing brand data by Personas, tags, and dimensions — enabling flexible quadrant views without heavy dashboard builds. The strategy favors report-style snapshots over data-intensive real-time dashboards, reducing engineering risk and complexity.

Pedro is out this week, leaving Jose and Stevie as the two active engineers. Stevie has a database migration requiring several days of focused work. Priority: growth tickets first; brand report shaping deferred to Marcel.

### Brand Reports Development

Marcel is building a "brand report" — a single-page curated audit combining public brand data with deep research insights. The report is partially gated: some content is public, detailed insights require user signup. Nigel confirmed it's useful for outreach and early sales conversations to spark interest. Marcel aims to have a more polished version by Friday.

Current AEO grader alternatives (like HubSpot's) are inadequate — the brand report is designed to be meaningfully better: more curated, more actionable, more AI-native.

---

## Action Items

**Marcel Santilli**
- Share and walk team through new handbook repository documentation for context and workflow understanding (09:05)
- Continue shaping brand reports and public page presentation to refine lead generation and user engagement features — target Friday (46:39)
- Push latest workflow and handbook repo changes to assist developers (51:36)

**Stevie Kim**
- Focus on growth tickets to free other engineers for complex technical tasks; defer brand report shaping for now (51:18)

**Jose Farias**
- Continue discussions with Jacopo to migrate to a new flexible analytics system supporting multidimensional data visualization (34:13)
- Assess engineering lift needed for new data pipelines; prioritize based on value and effort asymmetry (40:40)

**Nigel Hammett**
- Use emerging brand report tool for outreach and initial sales conversations to demonstrate value (50:48)

---

## Transcript

**Tyler Pavlas:** Hey marcel.

**Tyler Pavlas:** Happy Friday.

**Tyler Pavlas:** Indeed.

**Tyler Pavlas:** End of a long week.

**Marcel Santilli:** That's true.

**Tyler Pavlas:** How you feeling on your end?

**Marcel Santilli:** Good.

**Marcel Santilli:** Need more heads down time.

**Marcel Santilli:** Like I need a five day straight of like no meetings to catch up.

**Marcel Santilli:** But you know.

**Tyler Pavlas:** I pretty much just added you to the Wednesday calls, so hopefully that helps.

**Tyler Pavlas:** But I know there's like no amount of time that's enough time for you to be heads down.

**Marcel Santilli:** Yeah, it's like it's just two hours here and there.

**Marcel Santilli:** Don't do it.

**Marcel Santilli:** I need like five, six hours straight, you know, like to good clarity at times.

**Marcel Santilli:** Yeah.

**Tyler Pavlas:** For sure.

**Tyler Pavlas:** Totally get it.

**Tyler Pavlas:** I'll bring in Jamie now.

**Tyler Pavlas:** Intro from Carol Lou, if you didn't remember the context there.

**Marcel Santilli:** Cool.

**Marcel Santilli:** All right.

**Jamie Roberts:** Hi there.

**Jamie Roberts:** Hello.

**Jamie Roberts:** How are you guys?

**Marcel Santilli:** Really good, how are you?

**Jamie Roberts:** I'm doing well, thank you.

**Jamie Roberts:** Sorry I'm a few minutes late.

**Jamie Roberts:** It's been one of those rare Fridays where it's been 30 minute meetings back to back all day and if one goes long, everybody else suffers, you know.

**Marcel Santilli:** So I have a three year old and so today I woke up at five to try to get some stuff done and so from five to like seven it was beautiful.

**Marcel Santilli:** I got like so much done and then since I have not been, I've been on mostly meetings and.

**Jamie Roberts:** Yeah, well that's usually.

**Jamie Roberts:** Yeah, I, I don't usually have this happen and when I went back and I looked at my calendar, I'm like really?

**Jamie Roberts:** I feel like all these conversations needed to happen today so I can't be mad about it.

**Marcel Santilli:** Yeah, it happens.

**Marcel Santilli:** Anytime you take a vacation, there's a long weekend.

**Marcel Santilli:** People just pile the F out of things, you know.

**Jamie Roberts:** Yeah, exactly.

**Jamie Roberts:** But we're here, so.

**Marcel Santilli:** Yeah.

**Jamie Roberts:** Nice to meet you guys.

**Marcel Santilli:** Nice to meet you and sorry for keeping you from your long weekend.

**Jamie Roberts:** Oh no, you're all good.

**Jamie Roberts:** You're actually my last meeting today, so.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Okay.

**Jamie Roberts:** Not to me.

**Marcel Santilli:** It's like an extra burden, you know, no pressure.

**Marcel Santilli:** Well, I, I gotta say I, I've been a huge fan of Pluralsight from my HashiCorp days and we actually hire a few folks from there back then on that helped lead our like education stuff that we did back in the day.

**Marcel Santilli:** So.

**Marcel Santilli:** So when I saw that come up in the calendar, I was like really, really excited.

**Marcel Santilli:** Jamie would love to maybe get your, your background, a little journey context and then happy to.

**Marcel Santilli:** Tom and I do the same on our end, if that's okay.

**Jamie Roberts:** Yeah, absolutely.

**Jamie Roberts:** So.

**Jamie Roberts:** So yeah, I mean if you've spent, I'm sure you've been to my LinkedIn.

**Jamie Roberts:** I.

**Jamie Roberts:** You know, really focus more on that B2B SaaS, vertical focus software.

**Jamie Roberts:** Spent a lot of my career, you know, mainly high growth companies or companies that are going through transition.

**Jamie Roberts:** Right.

**Jamie Roberts:** And in some cases it's a combination of both those things.

**Jamie Roberts:** Right.

**Jamie Roberts:** Where they're doing transformation, change.

**Jamie Roberts:** I am new at pluralsight.

**Jamie Roberts:** Like I told somebody today, in fact I was joking with Carolou yesterday, I was like, yeah, I'm like on season one, episode four, I'm four weeks in.

**Jamie Roberts:** So I'm literally four weeks in and it feels like episode four.

**Jamie Roberts:** And when I say that, I don't say that lightly.

**Jamie Roberts:** Like it's been been.

**Jamie Roberts:** I'm kind of like, wow, there is lots of opportunity here.

**Marcel Santilli:** Yeah.

**Jamie Roberts:** So it's all, you know, it's all good and it's fun.

**Jamie Roberts:** But yeah, you know, pearls plural site is in an interesting time.

**Jamie Roberts:** You know, you're familiar with the company.

**Jamie Roberts:** I probably don't have to give you too much background there, but you know, they are at a point where, you know, they're in a significant place and their, their growth where they gotta do a lot of transformation.

**Jamie Roberts:** And so, you know, if it's been in the news, I mean you can see it, you know, like anytime you Google search it, you know, or get in a chat GPT.

**Jamie Roberts:** But you know, the past year and a half hasn't been exactly easy, you know, and some of the changes that have happened, but I think that that hard change has kind of happened and so now it's kind of like, okay, like we need to reset, we need to make this pivot, you know, going from B2C focus to more B2B enterprise focus and you know, really having that growth come back, you know.

**Marcel Santilli:** Yeah.

**Jamie Roberts:** So, you know, that's, I'm excited about that.

**Jamie Roberts:** I mean, that's what made me join, you know, pluralsight, you know, because with that type of journey, I mean there, you know, there's something new every week.

**Jamie Roberts:** Like I said, I'm on episode four.

**Jamie Roberts:** So yeah, that's a little bit about me and my background.

**Marcel Santilli:** That's, that's, that's incredible.

**Marcel Santilli:** Well, happy to.

**Marcel Santilli:** Tyler, do you want to do a quick intro and then I can do a bit of intro on both me and the company as well.

**Tyler Pavlas:** Yeah, yeah, definitely.

**Tyler Pavlas:** Great to meet you, Jamie.

**Tyler Pavlas:** Fellow Texan here, based in Houston.

**Tyler Pavlas:** Hopefully we're not too big of rivals.

**Tyler Pavlas:** My dad grew up in Dallas but joined GrowthX as the founding AE, work really closely with Marcel and started in strategy consulting and have been early at startups.

**Tyler Pavlas:** So we really have this model that like Combines services at the speed of software.

**Tyler Pavlas:** And Marcel and I will tell you a lot more about what that means.

**Tyler Pavlas:** But great to meet you.

**Jamie Roberts:** Yeah, great to meet you too.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And I'll do just super quick.

**Marcel Santilli:** So I am originally from Brazil, but I actually grew up in Texas as well.

**Marcel Santilli:** I grew up in Houston and then went to school in Austin.

**Marcel Santilli:** Been out here in the Bay Area for a while.

**Marcel Santilli:** But so I started a career early on at like IBM and HP and built these essentially like content hubs when like content marketing was just starting to be a thing.

**Marcel Santilli:** And so the first one I did was called securitintelligence.com, it went on to be the highest ROI program at IBM.

**Marcel Santilli:** And 15 years later, which was last year, it got pulled back into IBM successfully.

**Marcel Santilli:** But it really kind of helped inform how they took a content first approach to IBM.

**Marcel Santilli:** So IBM went from being this crazy site that was convoluted of like 40 million pages to like down to like fewer pages and being less product led organization to like information hubs and, and that was like inform Brian.

**Marcel Santilli:** It was like my peer at the time that we built this like was the person that leads IBM.com.

**Marcel Santilli:** so it was like a really like form how I thought about things.

**Marcel Santilli:** And, and so at HP I created a contributor network funny enough.

**Marcel Santilli:** And as I've been like so like involved in this, it's like it was like hey, how can I make marketing and growth a little bit more compounding and easier over time, not harder.

**Marcel Santilli:** And all the other channels just felt like the more I do the harder it gets.

**Marcel Santilli:** Like is there anything that I can do that gets them a little bit easier over time, you know, and, and it was like hey, if I just get really good editors and we come up with like really good topics for our audience and then I go fetch like and get like the best thought leaders on these topics and I pair them with editors and we crank 20 of those a week.

**Marcel Santilli:** And, and, and we keep improving every week.

**Marcel Santilli:** I think it work and it did right.

**Marcel Santilli:** Like we got to about a million visitors a month which for like it was called tech beacon.com and so it eventually was part of Micro Focus and it was generating like it was like 50% of all the leads for that business at the time.

**Marcel Santilli:** And then fast forward, I was at joint Hashicorp and we went from like 6 to 100 million in two years.

**Marcel Santilli:** And I was in charge of all digital, all growth.

**Marcel Santilli:** And it was the same thing where we had like, but it was more on the product side and technical.

**Marcel Santilli:** So I remember like plural side was part of Inspiration how to GraphQL and a few others at the time.

**Marcel Santilli:** And really like for me it was like, hey, I have, you know, 10 million open source downloads a month, but the founders won't let me de anonymize them.

**Marcel Santilli:** So I have like, you know, I have the traffic, but I have no way to.

**Marcel Santilli:** So then I created a learn environment to essentially figure out like where people were in their learning journey of how they're using global open source and like again like so every, every throughout my career was just like that again and again.

**Marcel Santilli:** And as I became a CMO and then, and so I was a service that and hired their now CMO and had a content also that helped them go public and not be as dependent on paid, you know, and then scale AI.

**Marcel Santilli:** The CEO was roommates with Sam Altman at the time.

**Marcel Santilli:** And I just created this franchise of bringing all these thought leaders like Andrew Ng, Fei Fei Li, like Kevin Scott and all as part of this kind of conference franchise called Transform X.

**Marcel Santilli:** And then we did like over 200 sessions like that.

**Marcel Santilli:** It was just free chatgpt, you know, so I kind of got to learn from behind the scenes.

**Marcel Santilli:** But you can see the common trend here, which is like content and like, but content that drove growth, that wasn't just like content like thought leadership high in the sky over there that proves no business value.

**Marcel Santilli:** And so then when I was at Deepgram, we whisper had just came out, voice AI model and we're competing with OpenAI and I'm like, what the hell do I do here?

**Marcel Santilli:** Like, Sam Altman can send a tweet and it's my entire budget for the year equivalent, right.

**Marcel Santilli:** And so I created an AI apps catalog, a gloss AI glossary, started creating content, building these AI workflows and 24 extra traffic.

**Marcel Santilli:** We built a.

**Marcel Santilli:** A newsletter called aiminds.com grew it to 300,000 subscribers and within six months it was like they were on the map essentially, you know.

**Marcel Santilli:** And then recently they raised series C 1.3 billion valuation.

**Marcel Santilli:** And so at the time was like not looking as good, like, you know, and so much so that their main investors now are main investment too.

**Marcel Santilli:** And so Growth X really started for me doing workshops, just teaching people what I had learned in the past 15 years of doing this, but from a lens of like how to use AI as a force multiplier with the right first principles, right?

**Marcel Santilli:** And then also teaching people like, hey, this is how you find, like this is who you need to operationalize this thing despite AI or In addition to AI, it's not just a set and forget.

**Marcel Santilli:** Like you need, you know, to identify the right opportunities, you need to have the right context of the company.

**Marcel Santilli:** You need people that are output bar raisers along the way.

**Marcel Santilli:** You need last mile executions, otherwise nothing gets published or improved or refreshed.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so, so then I did these workshops and after 170 people paid 500 bucks to come to the ML CMO at Deep Gram, a lot of them started like, hey, can you just do this for me?

**Marcel Santilli:** And to end I was like, oh, that sounds like a lot of fun.

**Marcel Santilli:** This is like my dream job, you know, like only do that and not deal with crazy CEOs.

**Marcel Santilli:** That sounds like fun.

**Marcel Santilli:** And then long story short, that was about 18 months ago and we hit about like a million and a half in revenue.

**Marcel Santilli:** I was like, I should quit my job.

**Marcel Santilli:** And that's how GrowthX started.

**Marcel Santilli:** And now crazy enough, like we bootstrap until March of last year and then we raised a series A round and we're now 90 people and 60 of those are forward deployed to customers.

**Marcel Santilli:** They're like editors, forward deploy engineers, design engineers, like strategists.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then we built our own platform and agentic framework for all these workflows that I can show you.

**Marcel Santilli:** And then our whole model was like end to end.

**Marcel Santilli:** I like to think of it as like from context to content to eventually conversions.

**Tyler Pavlas:** Right.

**Marcel Santilli:** Like, and so it's ultimately with the outcome in mind of organic growth and compounding growth.

**Marcel Santilli:** But that's like the lagging indicator, right?

**Marcel Santilli:** Like, so the leading indicators that we really try to do is like manage, create and improve pages on your site so that you can impact your AI visibility and search visibility.

**Marcel Santilli:** That leads to traffic, that leads to conversion.

**Marcel Santilli:** Right?

**Marcel Santilli:** So you got to focus on the controllable inputs to drive the right outputs and then pay attention to the signals and the leading inputs are the leading outcomes that then get to the one, the ultimate one, which is conversion and revenue.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then we're kind of like an end to end publishing engine and we're an extension of your, your, your team and, and I'll shut up now because that was a lot.

**Jamie Roberts:** No, that was good.

**Jamie Roberts:** No, that was good.

**Jamie Roberts:** Thank you for the overview.

**Marcel Santilli:** Yeah, but we'd love to like just hear a little bit more.

**Marcel Santilli:** Like I, like, like I said, I'm familiar but haven't like dug super deep.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, but I can see at least from Semrush and others that this seems to be like definitely like a strong compression over the last Three, three years.

**Marcel Santilli:** Right.

**Marcel Santilli:** As far as like organic traffic.

**Marcel Santilli:** But.

**Marcel Santilli:** But like, maybe put it differently, like, if you had a magic one, you have 10,000 pages on your site.

**Marcel Santilli:** Like, what, what.

**Marcel Santilli:** What are the, the areas that, you know, if you had a magic one, you would love help or that you're feeling that extra pressure there.

**Jamie Roberts:** Yeah.

**Marcel Santilli:** So this is your years of experience already in there, you know, so you know everything.

**Jamie Roberts:** Of course, I'm an expert.

**Jamie Roberts:** No, I'm not.

**Jamie Roberts:** But so I.

**Jamie Roberts:** There's a couple of things happening.

**Jamie Roberts:** I did just have a phone call with my VP of Digital that kind of walked me through kind of like the state of the state with the website.

**Jamie Roberts:** Right.

**Jamie Roberts:** And the short of it is, is that very antiquated code.

**Jamie Roberts:** You know, there's been just multiple versions of things.

**Jamie Roberts:** And pluralsight did a rebrand, you know, that was launched, I want to say October, November, this past October, November.

**Jamie Roberts:** And so everything, I mean, there's just so many coded pages and things like that.

**Jamie Roberts:** They're in the middle of like trying to update all this.

**Jamie Roberts:** Right.

**Jamie Roberts:** And so they have a V3 coming that they're trying to line up and launch and kind of clean up the back end code and like all the things by July.

**Jamie Roberts:** So there's that.

**Jamie Roberts:** Then.

**Jamie Roberts:** The other piece of this is, is that if you go to our website today, it really speaks more to B2C and not B2B enterprise.

**Jamie Roberts:** So we went to revenue kickoff, that was my first day here four weeks ago.

**Jamie Roberts:** And we introduced these new solutions for sales to go sell to B2B Enterprise.

**Jamie Roberts:** You will not find them on our webpage or our website at all.

**Jamie Roberts:** So part of this is like, we have this antiquated website thing happening, but yet we have a business wanting to move at the speed of light.

**Jamie Roberts:** I'm like, well, like I told him today, I'm like, we can't go in there and say, sorry, we can't update any messaging or anything for the next six months until we basically rebuild the website because we don't want to throw away work.

**Jamie Roberts:** And I'm like, we're going to have to throw away some work.

**Jamie Roberts:** I'm like, so there's that piece happening.

**Jamie Roberts:** You know, I think that, you know, the biggest thing is the homepage messaging is wrong.

**Jamie Roberts:** It doesn't align to the ICPs we're going after.

**Jamie Roberts:** And the pivot from B2C to B2B.

**Jamie Roberts:** The navigation needs to be worked out.

**Jamie Roberts:** Like, we need to rethink about these user journeys and, you know, how we want them to experience our website.

**Jamie Roberts:** And so there's a lot happening there.

**Jamie Roberts:** And then I go in throughout there and I'm like, oh, and by the way, you know.

**Jamie Roberts:** Cause when the content team, you know, they.

**Jamie Roberts:** I do have some content marketers on the team, and they're generating quite a bit of content, but it's very heavy blog content.

**Jamie Roberts:** They want to hire an SEO specialist.

**Jamie Roberts:** And I'm like, time out.

**Jamie Roberts:** Like.

**Jamie Roberts:** Like, just like, let's just wait a minute.

**Jamie Roberts:** And then, you know, you come.

**Jamie Roberts:** You know, you have me come in and I'm like, so what are we doing?

**Jamie Roberts:** You know, as AI is taking over the world, like, how are we optimizing for that and showing up?

**Jamie Roberts:** And like, where is that a part of our strategy?

**Jamie Roberts:** And so.

**Jamie Roberts:** So, yeah, I just gave you a big can of worms.

**Jamie Roberts:** So that's kind of what's happening right now.

**Marcel Santilli:** This is a sweet spot.

**Jamie Roberts:** There's a lot, right?

**Jamie Roberts:** And then, you know, there's some cool things happening that aren't seeing the light of day.

**Jamie Roberts:** For example, like, you know, we have this author's fellowship program that, you know, there's a new podcast that's been spun up, you know, that it's like, how are we leveraging some of this, you know, voice of customer and, you know, bringing that onto our website, Right?

**Jamie Roberts:** So, you know, so far, the voice of customer, if you will, if you could even call it that, that you'll mainly see on the website are company logos.

**Jamie Roberts:** And I'm like, no, we need to pivot, you know, and lead with voice a customer on our website and talk about the problems we solved, you know, and the solutions we have to help them solve those problems.

**Jamie Roberts:** Like, it's just.

**Jamie Roberts:** It's a.

**Jamie Roberts:** There's a lot of pivot happening at once.

**Jamie Roberts:** And then on top of that, you have this constraint of an outdated website on the back end, you know, or very complex because, you know, I've come to find out, you know, everything is just unique and, you know, coded, you.

**Marcel Santilli:** Know, and not scale, hard coded.

**Marcel Santilli:** Are you.

**Marcel Santilli:** Are the pages mostly, like, integrated with the product?

**Marcel Santilli:** And so there's no cms, or is there like, both?

**Marcel Santilli:** Or can you help me understand it?

**Marcel Santilli:** Does that need to go into the details?

**Jamie Roberts:** Yeah, there is some product.

**Jamie Roberts:** There are some pages that are connected to the product.

**Jamie Roberts:** And so that was another thing that Dustin and I talked about today was he was like, yeah, I'm talking to product because we're taking in some of these pages and we could be optimizing some of the content on these pages, you know, so.

**Jamie Roberts:** But the product team owns that, right?

**Jamie Roberts:** So there's some of that happening as well.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay, that, that makes sense.

**Marcel Santilli:** You're giving me deja vu of Udemy.

**Marcel Santilli:** I thought you were about to start crying.

**Jamie Roberts:** You're like, oh.

**Marcel Santilli:** And then they go and get acquired by Coursera and then the CMO leaves and we're like trying to navigate it all too.

**Jamie Roberts:** Oh, so it sounds very similar.

**Marcel Santilli:** Like everything you're explaining sounds like pretty, pretty similar.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like, but like, like okay, so, so I, I'll give you the.

**Marcel Santilli:** Maybe the.

**Marcel Santilli:** Do you want the PC or the brutal truth from an outsider's perspective?

**Jamie Roberts:** No, I mean I just want you to give it to me straight.

**Jamie Roberts:** You don't have to be PC.

**Marcel Santilli:** Okay, so you have.

**Jamie Roberts:** You have an effed up.

**Marcel Santilli:** No, no, you have like 10,000 pages on your site and 4,431 of those are dead weight.

**Marcel Santilli:** So think of it as like, yeah.

**Jamie Roberts:** They need to go.

**Marcel Santilli:** You're consuming all this crawl budget, right?

**Marcel Santilli:** And, and it's like, and it's less than 2% of your traffic, you know, and, and then like about 84% based on like just me doing some quick number back at the envelope here.

**Marcel Santilli:** Obviously like if once we get into GSC and like look at your data and do more like we can understand a little bit better.

**Marcel Santilli:** It is actually like super informational and lower intent.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so I think there's like anyways all that to say there's like an insane amount of like low hanging fruit things.

**Marcel Santilli:** But, but the, the, the thing here is like that we try to get really right is like we start with, with context, right?

**Marcel Santilli:** Because, and the reason for that is like our philosophy is like your website is going to be 100 times more important because it's not only influencing buyers, it's influencing AI agents and training bots, right?

**Marcel Santilli:** And so because of that also there's the long tails way, way, way, way longer.

**Marcel Santilli:** And there's a lot of things that would happen only post sales in a lot of cases that are actually like there's things you would have never asked Google before that.

**Marcel Santilli:** Now you ask an agent, right?

**Marcel Santilli:** And the, and the amount of information that an agent has and the number of URLs it's fetching, you know, so it's a much more.

**Marcel Santilli:** The game just got like exponentially harder, right?

**Marcel Santilli:** And way more dynamic.

**Marcel Santilli:** So now it's like pages after 30 days are decaying way, way faster.

**Marcel Santilli:** And so organic still compounds, but then it's also decaying way faster.

**Marcel Santilli:** So, so it's kind of like this counter game of like how the hell do you manage 10,000 pages?

**Marcel Santilli:** So you need to build, you know, use AI as a force multiplier.

**Marcel Santilli:** The, the challenge is AI is also a shit multiplier like to say.

**Marcel Santilli:** And so garbage in, garbage out.

**Marcel Santilli:** And so then like the context is almost like so, so critical to get right because it kind of, it's an aperture by actually like multiply good things and, and like you know, apply them.

**Marcel Santilli:** But then it's not a zero or one game.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like quality is like layers of quality.

**Marcel Santilli:** Right.

**Marcel Santilli:** It's not like getting something right is not a per.

**Marcel Santilli:** Like it's subjective and so to.

**Marcel Santilli:** And it's never 100% and there's diminishing returns from go to 99 to 100%.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so it's like, it's, it's almost like a different game.

**Marcel Santilli:** And so a lot of like the way and sorry, there's like construction going on over here.

**Marcel Santilli:** So if you hear is like really starting from that.

**Marcel Santilli:** So it's like Tyler maybe can kind of like show you some, some kind of examples like Augment code, like very technical customers we have and then how we approach that a little bit.

**Marcel Santilli:** If you think it's helpful.

**Jamie Roberts:** Okay, yeah, that'd be great.

**Tyler Pavlas:** Yeah, Happy to dive deeper for you, Jamie.

**Tyler Pavlas:** To Marcel's point, you know, I think we found our sweet spot working with software companies and we definitely love when there's like a product led, but also an enterprise sales kind of focus.

**Tyler Pavlas:** And that's the Augment code story.

**Tyler Pavlas:** If you think about Augment code, when they met us, they were closer to around 20k monthly organic.

**Tyler Pavlas:** And now after about 6 months working together, we are almost 3x that number.

**Tyler Pavlas:** They were spending a lot on paid which has pretty much tapered off at this point.

**Tyler Pavlas:** And the way that we helped them get a lot of visibility was we really created content at scale but maintaining quality across their site.

**Tyler Pavlas:** And so you know, they kept their blog in the same menu nav but we created like these three sections of their site, this guide section where we're able to fine tune our engine to be more technical.

**Tyler Pavlas:** Right.

**Tyler Pavlas:** There's like code snippets in a lot of this content.

**Tyler Pavlas:** We're cross linking to the most relevant sources on their website.

**Tyler Pavlas:** But it all starts to Marcel's point with the context, right.

**Tyler Pavlas:** So we've create, we've created all these different pages.

**Tyler Pavlas:** There are these tools pages where we're comparing different tools.

**Tyler Pavlas:** There's listicles.

**Tyler Pavlas:** We have this way of like being very objective with the way we talk about different technology solutions.

**Tyler Pavlas:** We're not Bashing their competitors, so to speak.

**Tyler Pavlas:** But what's nice is if you look on the organic or the AI search side, the search that they care the most about is being the best AI coding tool built for the enterprise.

**Tyler Pavlas:** Right.

**Tyler Pavlas:** And so they want to be ahead of cursor.

**Tyler Pavlas:** That's where we're positioning them in this answer.

**Tyler Pavlas:** And you're starting to see content that we've created cited for some of their top competitors.

**Tyler Pavlas:** And so what we do up front is we start with this strategy, Sprint, where we go really deep into your icp, your company context, and then your brand voice.

**Marcel Santilli:** Right.

**Tyler Pavlas:** And so we'll, we'll shape that context up front.

**Tyler Pavlas:** And as a quick example of that, what we did for Engine in the business travel space is we identified that they really care about being industry specific.

**Tyler Pavlas:** And so for each of their target industry verticals, we're basically going in and thinking about everything that differentiates Engine in business travel, but then connecting that to these three titles in each industry with all of their fears, uncertainties, motivations, pain points.

**Tyler Pavlas:** But connected to business travel.

**Tyler Pavlas:** Right.

**Tyler Pavlas:** Not generic around, like what is frustrating the operations or the finance manager.

**Tyler Pavlas:** And so we'll evolve these over the life of the relationship.

**Tyler Pavlas:** And Marcel can definitely go into the pipelines that we use to create the content.

**Tyler Pavlas:** But the short story here is that it's a lot of context, engineering upfront, with experts in the loop, so that we really combine the best of these workflows, which it's very intimidating to start from zero trying to build AI workflows.

**Tyler Pavlas:** And if you just try to use ChatGPT or Claude, it's not enough.

**Tyler Pavlas:** And so we can sort of deconstruct how our workflows are superior.

**Tyler Pavlas:** But there's also a human in the loop at every part of the process.

**Tyler Pavlas:** Sure.

**Marcel Santilli:** And I think, like one thing just to call out super, super quick is that like right now, like your blog is actually your highest ROI per page or like higher, like driving problem is like you have two areas that are getting hammered, which is the AI content, AI ML and the cloud content, which are both like declining.

**Marcel Santilli:** The AI won by 40% and the cloud content category by 20%.

**Marcel Santilli:** Again, like, this is just like estimates.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so, and then there's like a recent thing I can send you that like blogs are now the most cited type of content in AI answers.

**Marcel Santilli:** And so it's less that it's blogs.

**Marcel Santilli:** It's just like well structured, nicely structured content, you know, like, that's well cited, fresh.

**Marcel Santilli:** It's less like blog, you know, it's more of like good docs are the same thing as a blog, right?

**Marcel Santilli:** Like it's just like written content that's well organized, you know, and well structured.

**Jamie Roberts:** Yeah, yeah, yeah.

**Jamie Roberts:** If you guys have any use cases that you can share where you've been able to take clients from not spending as much on paid media and more organic.

**Jamie Roberts:** That's another thing that I, I think is happening at this company is I'm like we.

**Jamie Roberts:** I mean I, I would like to show especially if I'm bringing in somebody like you guys, I need to be able to show efficiency gained and cost savings and paid media because we're getting it organically.

**Marcel Santilli:** Yeah, yeah, exactly.

**Marcel Santilli:** The good news here is like like we.

**Marcel Santilli:** We've seen really mature sites and do extremely well because you have 4 million backlinks.

**Marcel Santilli:** Like I, I am like so confident like in our abilities here because of that like, like with lovable that didn't even have like the same domain authority or like we're just kicking off Vercel companies that have like good authority already that have like just decaying quality on, on their portfolio pages, like that's where we can shine the most.

**Marcel Santilli:** The hardest is when they have like no authority and you're building from zero which we've done before too.

**Marcel Santilli:** But like very mature sides like Redis right now is another really mature site sentinel 1.

**Marcel Santilli:** We built our vulnerabilities database and so it's kind of like you know, and the good thing is like we do have four deploy AI engineers and designers.

**Marcel Santilli:** So you know, no promises because we haven't looked into like your setup.

**Marcel Santilli:** But we to date have not encountered a setup that we weren't able to help resolve things.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like obviously it's like if it's like a black box and we can't touch it.

**Marcel Santilli:** But normally like lovable like Ramp Rex, like all of those, they gave our engineers like access to their GitHub repo and we were able to like work with anything they had and get them to either a headless setup or something else.

**Marcel Santilli:** And so like there's a lot of like again we're not web agency of, of record here but, but like we're usually able to accelerate a zero to one because if we don't fix them some of the vitals that things then we're not going to be successful no matter what we do, you know.

**Jamie Roberts:** Yeah, yeah, absolutely.

**Jamie Roberts:** Yeah, yeah, yeah.

**Jamie Roberts:** No, I mean I know we're at time.

**Jamie Roberts:** What I'd like to do is I'd like to get you guys connected with Dustin Hawthorne so He's the VP of digital that is doing a lot well, he's responsible for web and get you guys connected and you know, go through and see what the opportunities are and have the conversation.

**Jamie Roberts:** Anything that you guys can send to me as far as, you know, cost structures, ways of working, you know, things like that for me to review, I want to go ahead and start looking at.

**Jamie Roberts:** But I think it would be great to get you connected with Dustin and you know, get a little bit deeper and see what the opportunities are and he can definitely give you more of that double click.

**Jamie Roberts:** Obviously he's been here a year and a half, so, you know, he's living this every day.

**Jamie Roberts:** He can give you the double click into like the really reels that are happening.

**Jamie Roberts:** So that way I'll give you guys a better context as to, you know, what, you know, what, what, what we'd be getting into together if we decided to partner.

**Marcel Santilli:** So that, that sounds, that sounds amazing.

**Marcel Santilli:** What one, like minor.

**Marcel Santilli:** If you have.

**Marcel Santilli:** I love that you said like, pause.

**Marcel Santilli:** Like I would say, like, the one thing is if you don't pull a trigger with an SEO agency, it's really helpful because we tend to like, I'm not needed.

**Jamie Roberts:** I'm not doing it.

**Jamie Roberts:** I don't think that count is needed.

**Jamie Roberts:** I'll be honest with you guys.

**Jamie Roberts:** I'm like, I don't think it's needed.

**Jamie Roberts:** And I, and I told Dustin that and, and Dustin did say.

**Jamie Roberts:** He was like, he's like, yeah, he's like, I want to wait and just see.

**Jamie Roberts:** And I, and I, I mean, honestly, I've already told him I was talking to you guys because I was like, I really think that we need to get with an agency.

**Jamie Roberts:** Like, I would rather take that headcount cost and put it towards, you know, a partnership that can help us stay on top of these things.

**Jamie Roberts:** Because what I worry about is hiring a headcount.

**Jamie Roberts:** It.

**Jamie Roberts:** I'm worried about it getting stale.

**Jamie Roberts:** Right.

**Jamie Roberts:** They come in with a certain skill set, they're focused in a certain area, whereas, you know, you guys are seeing things differently all day long, you know, across different businesses.

**Jamie Roberts:** And just you already said it, things are changing rapidly.

**Jamie Roberts:** So I would rather partner with somebody on this and hire a dedicated headcount for a specific, like one item thing.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The first eight weeks of our engagement, there's usually like eight different roles that touch the, you know, that kind of works it.

**Marcel Santilli:** So it's like, it'd be.

**Marcel Santilli:** But okay, that, that sounds amazing.

**Marcel Santilli:** I am keeping you from your long weekend.

**Marcel Santilli:** So I am super excited.

**Marcel Santilli:** I'm very like.

**Marcel Santilli:** Like, it would be truly an honor to get to work on pluralsight because I drew so much inspiration from.

**Marcel Santilli:** From the site back in my Hashicorp days that.

**Marcel Santilli:** Anyways, this.

**Marcel Santilli:** This one's like, we're.

**Jamie Roberts:** I. I think with you.

**Jamie Roberts:** I think with you snatching their people, you're going to have to pay it forward.

**Jamie Roberts:** I know.

**Marcel Santilli:** I.

**Jamie Roberts:** That's okay.

**Jamie Roberts:** I've done the same thing where he was only two.

**Marcel Santilli:** It was like our head of education.

**Marcel Santilli:** I'm blanking on his name now.

**Marcel Santilli:** It's been like seven years, but.

**Marcel Santilli:** And then was like one of our education engineers.

**Marcel Santilli:** So it was like, we clean house, like, kind of thing, you know, like.

**Jamie Roberts:** Yeah, I know I've just given you a hard time.

**Jamie Roberts:** I mean, I can't say I am giving you a hard time because I just hired somebody that previously worked for me at viva, and I'm kind of like, what?

**Jamie Roberts:** Like, you weren't providing the career path.

**Jamie Roberts:** It's over here.

**Jamie Roberts:** So, I mean, people have to go where, you know, their career paths are needed.

**Jamie Roberts:** And I'm.

**Jamie Roberts:** And, like, I'm supportive of that.

**Jamie Roberts:** I'm just giving you.

**Jamie Roberts:** But yeah, I'll.

**Jamie Roberts:** I'll connect you guys with Dustin via email and let you guys get something set up, and then, yes, any information you can send to me as far as, you know, partnerships and kind of what that would look like, I'll start getting, you know, some eyes on that as well.

**Jamie Roberts:** And I'm happy to join the meeting with you guys and Dustin.

**Jamie Roberts:** Just, you know, I'll.

**Jamie Roberts:** In fact, I might, you know, just as.

**Jamie Roberts:** Because I'm also ramping up in some of this.

**Jamie Roberts:** Still a lot of this, frankly.

**Jamie Roberts:** So I may just see if we can grab, you know, some time together.

**Jamie Roberts:** Is there a set amount of time that you want to meet for next time?

**Jamie Roberts:** Do you want to do a little bit longer or keep it 30 minutes?

**Marcel Santilli:** An hour would be great.

**Marcel Santilli:** So I can do a little bit more, like, audits on our end, you know, like, for instance, like, even, like, Wednesday.

**Marcel Santilli:** I have a lot of flexibility, too, and.

**Marcel Santilli:** But also, we can coordinate over email, but.

**Jamie Roberts:** Okay.

**Marcel Santilli:** But Wednesday is, like, usually a good day.

**Marcel Santilli:** I have a lot of flexibility.

**Jamie Roberts:** Okay.

**Tyler Pavlas:** And I think, you know, my job is ultimately to free up time for Marcel, so the fact that he's on this intro definitely means he cares a lot.

**Jamie Roberts:** Yeah.

**Jamie Roberts:** I'm already looking at my calendar next week, and I'm like, oh, what I'll do is, is I'll actually send.

**Marcel Santilli:** So, sorry, I got a job.

**Marcel Santilli:** Because I'm late to my next meeting, but have a great weekend.

**Marcel Santilli:** We'll talk.

**Jamie Roberts:** You too.

**Jamie Roberts:** All right, bye.

**Tyler Pavlas:** And Jamie, we can.

**Tyler Pavlas:** We can figure it out together here.

**Tyler Pavlas:** Okay, perfect.

**Jamie Roberts:** Yeah, we'll get it figured out.

**Jamie Roberts:** I will.

**Jamie Roberts:** I'll send a message to my.

**Jamie Roberts:** My account, my ae.

**Jamie Roberts:** I can.

**Jamie Roberts:** My ea.

**Jamie Roberts:** I can say it.

**Jamie Roberts:** I need a long weekend.

**Jamie Roberts:** My ea.

**Jamie Roberts:** And also.

**Tyler Pavlas:** That's me.

**Tyler Pavlas:** That's me.

**Tyler Pavlas:** I'm the ae.

**Jamie Roberts:** Yeah, that's you.

**Jamie Roberts:** So I'll send a message and let me see what I can get coordinated and I'll.

**Jamie Roberts:** I'll have you on it.

**Tyler Pavlas:** So.

**Marcel Santilli:** Perfect.

**Tyler Pavlas:** Yeah, I'll shoot.

**Tyler Pavlas:** Sometimes that Marcel and I are both open and even if he can't join, like, I definitely have gone under the hood many times and have talked through like how, you know, with us, you're basically starting with like an engine that has been pressure tested across hundreds of B2B software companies.

**Tyler Pavlas:** And the problem a lot of times to your point is like you hire someone, they have to start from zero building these workflows.

**Jamie Roberts:** Yeah, yeah.

**Tyler Pavlas:** And how long are you going to start optimizing the content on your site and creating new content?

**Tyler Pavlas:** Three to six months.

**Tyler Pavlas:** And you want to start a lot faster.

**Tyler Pavlas:** So, yeah, excited to dig a lot deeper and I'll shoot you those resources and some times and work with your EA to figure out next week what works best.

**Jamie Roberts:** Okay, that sounds great.

**Jamie Roberts:** Well, I hope you have a good weekend.

**Tyler Pavlas:** Thanks, you too.

**Tyler Pavlas:** Talk soon.

**Tyler Pavlas:** See ya.

**Marcel Santilli:** Bye.

**Marcel Santilli:** Bye.
