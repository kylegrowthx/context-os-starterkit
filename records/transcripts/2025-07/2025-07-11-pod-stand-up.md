# Pod stand-up

<metadata>
date: 2025-07-11
time: 13:59 UTC
duration: 42 minutes
organizer: Saskia Wartnaby (GrowthX)
participants: Jürgen Linde (GrowthX), Matthew Alves-Hill (GrowthX), Carrie Chowske (GrowthX), Jenny Macrohon Dabon (GrowthX), Darrell Etherington (GrowthX), Feyisayo Odedeyi (GrowthX), Jessica Nicole Manificiar Gayo (GrowthX), Josip Sovar (GrowthX), Ehtisham Hussain (GrowthX), Saskia Wartnaby (GrowthX)
fathom_recording_id: 73613471
fathom_url: https://fathom.video/calls/348761276
share_url: https://fathom.video/share/itsRoNw3sR2CzzzqUxasu5Qb3viEvxrS
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

GrowthX's delivery pod welcomed three new clients—Engine (travel booking for corporate groups), Aimbit (identity and access management for non-human entities), and Town (tax services for SMBs)—increasing active clients from 4 to 7. The team discussed critical infrastructure needs: standardizing Airtable bases with locked-down fields and client-facing views, automating Google Doc creation and organization, and setting up Claude Projects and Perplexity spaces as shared knowledge bases for each client. Additionally, Jürgen Linde departed the team after contributing significantly to content strategy and team development.

---

## Context

This is a weekly standup for GrowthX's delivery pod—the team managing ongoing client engagements. The pod is scaling from 4 active clients to 7 after three new accounts (Engine, Aimbit, Town) transitioned from the sprint onboarding process. Feyisayo Odedeyi, who joined GrowthX in May after four years of freelance content writing, moved into direct support and is now working on Engine and Aimbit. Notably, this meeting marks Jürgen Linde's last day; he served as an editorial and strategic contributor to the team and is departing on good terms. The meeting focused on operational scaling challenges: how to standardize tooling (Airtable, client-facing interfaces, knowledge bases) and processes to handle the growing client load efficiently while maintaining quality.

---

## Relevance

**To GrowthX Delivery:**
- Standardizing Airtable infrastructure: Darrell to create list of locked-down fields/statuses and set up sanitized, access-controlled views for clients. Current approach of sharing full bases with editor access is too permissive and creates friction.
- Knowledge base tooling: Team moving toward Claude Projects and Perplexity spaces for client-specific context. Jenny's Perplexity space for GoodCall (with documentation + transcripts) and Matthew's Claude project experiments show the pattern working; rollout to all clients planned.
- Google Doc automation: Discussed need to automate creation and folder organization per schema (internal/external hierarchy). Flagged as highly repetitive, manual, and candidate for future Atlas integration.

**To CheckThat:**
- Identity and access management (IAM/Aimbit): Ehtisham and Darrell discussed how non-human identity management (APIs, automated processes) becomes increasingly relevant as AI agents proliferate. Aimbit's technical depth offers potential learning and reference value.

**To GrowthX Business Development:**
- Client expansion signal: Pod scaled from 4 to 7 active clients in one week (Engine, Aimbit, Town), with more potentially in flight. GoodCall temporarily paused, creating resource flexibility.
- Operational maturity: Documented processes for client transitions (sprint → pod handoff) and templates (Content OS structure from SEMrush keyword gaps) are now replicable across new accounts, reducing friction in scaling.
- Reference potential: Engine (travel/corporate off-sites) and Town (SMB tax) have ICP overlap with existing customers (e.g., GoodCall); potential for cross-selling and customer insights.

---

## Overview

- New clients (Engine, Aimbit, Town) joining the pod, increasing from 4 to 7 active clients
- Discussed standardization needs for Airtable bases and potential automations
- Explored use of Perplexity and Claude AI for creating client-specific knowledge bases

---

## Key Topics

### New Team Member Introduction

  - Feyisayo Odedeyi joined the team, working on Airbytes and Sunbit
  - Moving to direct support, will be working on Engine (new client) and Aimbit

### New Clients Overview

  - Engine: Travel booking for groups, focused on employers doing off-sites/team trips
  - Aimbit: Account access management for non-human entities (APIs, automated processes)
  - Town: Tax services for small businesses (SMB)

### Airtable Standardization and Improvements

  - Discussed need for standardized elements across client bases (e.g., statuses, clusters)
  - Carrie highlighted issues with Yurko's cluster/subcluster setup
  - Explored potential for automating Google Doc creation and folder organization
  - Joe suggested adding meta title, URL slug, and meta description fields to Yurko's Airtable

### AI Tools for Knowledge Management

  - Jenny created a Perplexity space for GoodCall, incorporating documentation and transcripts
  - Matthew mentioned similar capabilities in Claude AI for writing projects
  - Team discussed setting up shared spaces/projects for all clients to improve collaboration

### Atlas Updates and Issues

  - Reported bugs in Zapped, including external links problem
  - Carrie and Darrell to follow up with Kirkland on Duplo PSEO fixes and artifact collection

### GoodCall Project Status

  - Potential pause in work, may affect team capacity and resource allocation

---

## Action Items

**Darrell Etherington (GrowthX)**
- Create list of standardized Airtable fields/statuses that can't be changed; share with team (timestamp: 00:18:15)
- Investigate setting up sanitized, access-controlled Airtable views for clients (timestamp: 00:30:02)
- Set up Claude projects and Perplexity spaces for all pod clients; add existing context/docs (timestamp: 00:35:23)
- File ticket and Slack Kirkland re: Duplo PSEO fixes—specifically code snippet incorporation and artifact reuse (existing logos, no re-run); coordinate on how to avoid regenerating 2,200+ artifacts given credit constraints (timestamp: 00:37:04)

---

## Transcript
**Feyisayo Odedeyi:** Hi, Jess.

**Feyisayo Odedeyi:** everyone.

**Feyisayo Odedeyi:** I don't think we've, like, chatted, like, directly.

**Feyisayo Odedeyi:** Well, it's nice to meet you.

**Feyisayo Odedeyi:** Thank you.

**Feyisayo Odedeyi:** Hi, everybody.

**Saskia Wartnaby:** Hi, everyone.

**Saskia Wartnaby:** Hello.

**Carrie Chowske:** I get the feeling that we're all just very glad it's Friday.

**Saskia Wartnaby:** Every week.

**Saskia Wartnaby:** Thank you.

**Ehtisham Hussain:** So are you guys planning anything for this weekend or?

**Ehtisham Hussain:** I just have a bunch of chores lined up, a bunch of things that need to be fixed, that's it.

**Saskia Wartnaby:** Yeah, I feel like at least one day of the weekend has to be like chores, chore day, shopping and cleaning.

**Saskia Wartnaby:** But I'm going to go visit family for one of the days as well, so looking forward to that.

**Saskia Wartnaby:** We really need to, like, restain our deck, if it, like, leaves it badly.

**Carrie Chowske:** But it's been so hot, like, I just don't want to.

**Carrie Chowske:** Yeah, no, that doesn't sound like a fun activity.

**Saskia Wartnaby:** Nice thing is in the afternoon, it's in the shade, so, like, if I wait late enough in the day, like, it's not so bad.

**Carrie Chowske:** Unfortunately, motivation, like, declines later in the day.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** Well, I hope you can find a good time to get it done.

**Carrie Chowske:** Is any of us, like, in a colder area?

**Ehtisham Hussain:** Like, is it hot everywhere in the world right now?

**Saskia Wartnaby:** What's happening?

**Saskia Wartnaby:** I'm watching Nigeria at the moment, so.

**Feyisayo Odedeyi:** Town is a bit chilly, but not crazy.

**Saskia Wartnaby:** It's, like, 10 degrees Celsius.

**Darrell Etherington:** Oh, that's nice.

**Saskia Wartnaby:** Yeah, so it's it's cold, but not, like, freezing.

**Carrie Chowske:** Oh, hi, Daryl.

**Saskia Wartnaby:** We've been just chatting.

**Darrell Etherington:** I had my mic off, and I was like...

**Saskia Wartnaby:** we get 10 degrees, like, we get that for, like, two days a year or something.

**Saskia Wartnaby:** Oh, my gosh, Ehtisham, that is horrific.

**Darrell Etherington:** Not me being the only, I think, American on the call over here trying to convert Selfiest to Fahrenheit.

**Carrie Chowske:** Oh, it's so nice.

**Darrell Etherington:** I'm when it's, like, in the 20s and 30s, because I'm like, okay, that's really, that's pretty warm.

**Carrie Chowske:** Like, because I remember that from, like, I would constantly, when they do, like, a heat wave in, like, England, and I'd be like, how hot is that really?

**Carrie Chowske:** Now, keeping in mind, of course, that I know a lot of people in, like, England don't have air conditioning, so lower temperatures are a bigger thing.

**Carrie Chowske:** But I'm, like, looking at it compared to what the temperature currently was when I was living in Florida, and I was like, ah, y'all are, y'all are whips.

**Carrie Chowske:** Yeah, basically.

**Ehtisham Hussain:** So, read yesterday somewhere that Fahrenheit is asking humans how hot it is, as Celsius is, like, asking water how hot it is.

**Ehtisham Hussain:** And Kelvin is, like, asking atoms.

**Matthew Alves-Hill:** How hard it is.

**Ehtisham Hussain:** I've never heard the Kelvin one before.

**Darrell Etherington:** The Kelvin is like, it's crazy.

**Ehtisham Hussain:** It's the only scale that has absolute zero, but it's not used anywhere in the world.

**Ehtisham Hussain:** It's just used by scientists.

**Carrie Chowske:** Very interesting.

**Carrie Chowske:** Yes, 298 Kelvins here today.

**Darrell Etherington:** that was terrible.

**Darrell Etherington:** Thanks for that.

**Darrell Etherington:** That was super helpful.

**Carrie Chowske:** The only metric conversion I can do easily is pounds and kilograms, because, well, she's actually sitting here watching the meeting, by the way.

**Carrie Chowske:** She likes when I'm on a call, she likes seeing you guys.

**Carrie Chowske:** But weighing kittens, I weigh them in grams when they're little, because they gain about 100 grams a week when they're, like, from newborn to, like, about...

**Carrie Chowske:** Actually, it still keeps going, but then it becomes, once they're in months, it's, like, in pounds, right?

**Carrie Chowske:** But, like, because I know that 907 grams is two pounds, like, I go, oh, it's just double kilograms.

**Carrie Chowske:** That's roughly how much the weight is.

**Carrie Chowske:** I was about to say, so sure you just, like, divide it.

**Carrie Chowske:** Yeah, it's pretty close.

**Carrie Chowske:** Yeah, it's pretty close.

**Carrie Chowske:** So it's one of those things where I'm like, because I've been weighing kittens for so long, I'm like, you know.

**Carrie Chowske:** Do you rescue a lot, Carrie?

**Saskia Wartnaby:** Is that why you're weighing kittens?

**Saskia Wartnaby:** we don't as much as we used to.

**Carrie Chowske:** Yeah, before we moved to Georgia, Carolina, though, I was doing really high volume and I was working really closely with the rest of the people, doing a lot of their medical.

**Carrie Chowske:** That's tough.

**Carrie Chowske:** That's really tough.

**Carrie Chowske:** It was a bit of a strain, so, but I say that and we've already rescued like 25 cats since we moved here a year ago, so.

**Carrie Chowske:** Amazing.

**Carrie Chowske:** Now we've gone on a kitten tangent, but I mean, look, look.

**Carrie Chowske:** Yeah, they are very durable.

**Carrie Chowske:** It's true, it's hard not to.

**Darrell Etherington:** Let's do get into it, though.

**Darrell Etherington:** Let's first, Fey, is that right?

**Darrell Etherington:** Do you want to introduce yourself just to the pod now that you're joining the team and make sure that I have your name pronunciation?

**Darrell Etherington:** My name is Feiy.

**Feyisayo Odedeyi:** Feiy.

**Feyisayo Odedeyi:** Feiy.

**Feyisayo Odedeyi:** Nice.

**Feyisayo Odedeyi:** Yeah, that's correct.

**Feyisayo Odedeyi:** Okay.

**Feyisayo Odedeyi:** So I've been in content writing for about four years now.

**Feyisayo Odedeyi:** GoTex is actually my first company that I'm working with, working with.

**Feyisayo Odedeyi:** I used to be like a freelancer, just all over the place, like writing for agencies on and off.

**Feyisayo Odedeyi:** But this is my first time being in a company like GoTex, so it's pretty exciting.

**Feyisayo Odedeyi:** I've been learning a lot.

**Feyisayo Odedeyi:** I have been writing.

**Feyisayo Odedeyi:** This is a joke GoTex in May.

**Feyisayo Odedeyi:** I recently just joined with Saskia and Jess.

**Feyisayo Odedeyi:** So I've been writing for Airbytes, and I did a bit for Sunbit.

**Feyisayo Odedeyi:** And I got an education from the company saying that I'm now in direct support.

**Feyisayo Odedeyi:** So I guess I'm excited to see what that's about.

**Feyisayo Odedeyi:** Yeah, great.

**Feyisayo Odedeyi:** Yeah, think you're working with us on Engine, which will be a new customer, and then Aimbit.

**Darrell Etherington:** Which is also new to our pod, not a new customer, but moving over from Jacob's pod, right?

**Darrell Etherington:** So we're starting right away, like that one, and then the engine will have a little bit of time to ramp because they're coming off of the sprint process, the new sprint onboarding process.

**Darrell Etherington:** But yeah, it should be good.

**Darrell Etherington:** I think AIMBIT is like a very kind of like dense technical topic.

**Darrell Etherington:** It's like account access management for non-human entities and identities.

**Darrell Etherington:** So if like APIs or automated processes are hitting your service or business, they need to be permissioned just like a human user would, right?

**Darrell Etherington:** Like we all have different levels of permissions for using the various tools in our companies and our partners' companies.

**Darrell Etherington:** And same too for things that are just like integration points like APIs or SDKs.

**Darrell Etherington:** So those all need to have permission levels, and that's what AIMBIT does.

**Darrell Etherington:** But kind of dense, but a little bit fun, like once I started learning about it, because I was...

**Darrell Etherington:** Helping David a bit with some of the calibration before, and I was like, oh, this is neat, I didn't really know about this, and it becomes a lot more relevant when you start having AI agents doing it all the time and trying to go and do stuff on your behalf, although that's an area they're just now moving into, so they haven't really done any of that yet, but it is something that they're going to be working on.

**Darrell Etherington:** And then just, the other client engine is like, oh, there you go, Ehtisham, you know a lot about IAM, IAM?

**Ehtisham Hussain:** So with identity access management, like I used to joke around, like Carrie has heard me tell this joke that, like, I become an expert on these topics, and then I forget all about them.

**Ehtisham Hussain:** Yeah, right.

**Darrell Etherington:** It's just in RAM, and then it's pushed out.

**Darrell Etherington:** Yeah, exactly.

**Darrell Etherington:** I've learned a lot of my technical knowledge just from, I worked with Ehtisham at another agency, two other agencies actually, this is our third one together now, damn.

**Carrie Chowske:** So

**Carrie Chowske:** But he used to do a lot of really technical content, and my editing was a lot of questions like, is the reader going to know what this means?

**Carrie Chowske:** And he'd be like, yeah, and he'd explain it to me, and I'm like, thank you.

**Carrie Chowske:** So no, I've learned a lot of my technical stuff from asking Edisham really dumb questions.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** Well, it's good.

**Darrell Etherington:** mean, everybody should feel free to do that of all of us, because I feel like it's good that we all learn together, right?

**Darrell Etherington:** And we can all try to find the answers.

**Darrell Etherington:** I think that's like the best thing that I ever gained from any of my past jobs was like a random collection of knowledge across a very wide body of topics.

**Darrell Etherington:** And it's shallow.

**Darrell Etherington:** So like, you know, people challenge me on a lot of them.

**Darrell Etherington:** I'm like, well, that's the extent of my energy.

**Darrell Etherington:** But it's very broad, which is useful, right?

**Darrell Etherington:** Yeah.

**Darrell Etherington:** And then just the note on the engine.

**Darrell Etherington:** So they do like travel booking for groups and mostly focused at employers doing stuff for off-sites, on-sites, team trips, that kind of thing.

**Darrell Etherington:** So, interesting company.

**Darrell Etherington:** They've been around a long time.

**Darrell Etherington:** They've gone through some branding changes and kind of pivots over the years, but I'm familiar with them even from my TechCrunch days covering them on the news side.

**Darrell Etherington:** So that should be fun.

**Darrell Etherington:** And then we also have Town, which is coming on board, which is tax for small business, for SMB.

**Darrell Etherington:** So traditional businesses are kind of like a customer overlap with a lot of our other customers, which is helpful.

**Darrell Etherington:** Like their ICP is sort of similar ICP to like a good color Yorko, but they deal specifically in tax.

**Darrell Etherington:** So that'll be coming online also after.

**Darrell Etherington:** Like that one is also coming off the sprint.

**Darrell Etherington:** So we'll have a staged handoff, right?

**Darrell Etherington:** I think we have a couple of those meetings today.

**Darrell Etherington:** So we have the first one.

**Darrell Etherington:** So the engine sprint team and the talent sprint team today, and they can walk us through some of the docks and stuff, and then we'll be able to get everybody up to speed.

**Darrell Etherington:** But they should be fairly smooth in terms of, like, they have established the cadence and pace and expectations around deliverables, and then we can take them and recreate them, just like some of the other transitions for existing customers that we've had.

**Darrell Etherington:** So hopefully nothing too complicated there, but we'll see when we get to it.

**Darrell Etherington:** Always surprises with any of these things.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Those are the big updates for me.

**Darrell Etherington:** Is there anything anybody wanted to talk about or bring up or discuss?

**Carrie Chowske:** I have, like, a really, like, a silly question, and I'm only asking it now because maybe Matt knows because he's been working with the sprint team.

**Carrie Chowske:** But, like, do we know what, I'm going to, can I share my screen really quick?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So, so, like, the template for the, like...

**Carrie Chowske:** Content OS for the sprints, and then I noticed Engine has it too.

**Carrie Chowske:** This URL, are these ones that we're trying to compete with?

**Carrie Chowske:** Is that what this list of URLs is?

**Carrie Chowske:** Does anyone know?

**Carrie Chowske:** It looks like that's what it is.

**Carrie Chowske:** Yeah, it's an output from SEMrush keyword gap.

**Matthew Alves-Hill:** Okay, okay, good.

**Matthew Alves-Hill:** And then it's rolled up.

**Matthew Alves-Hill:** So if you go in the keywords tab, that's the raw output from SEMrush, and then the URL tab is basically a roll up.

**Matthew Alves-Hill:** It's a roll up from all those keywords, yeah.

**Matthew Alves-Hill:** Yeah, because I saw that it was linked.

**Carrie Chowske:** Yeah, I saw that it was linked to these.

**Carrie Chowske:** So I think it's just like, yeah, okay.

**Matthew Alves-Hill:** There are some differences compared to like before Straspyrin, but like the new setup does actually make a lot more sense once you're familiar with it.

**Matthew Alves-Hill:** lot more easily.

**Matthew Alves-Hill:** I had done something kind of similar for when I had set up the one for discern.

**Carrie Chowske:** Because I noticed that they weren't interlinking all these things.

**Carrie Chowske:** I'm like, why wouldn't you do that?

**Carrie Chowske:** And so I had kind of done that anyway.

**Carrie Chowske:** But that's why I was trying to figure out what this was linked to.

**Carrie Chowske:** And I couldn't figure out because like the example that was in the template had both branded and then like a competitor.

**Carrie Chowske:** So I was like, I think it might be that's what it is.

**Carrie Chowske:** Yeah, there should be a tab.

**Carrie Chowske:** There's like there's a field for like internal and external.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** So that's probably what you're seeing.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay, cool.

**Carrie Chowske:** That's that's a that's a great answer.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** Sure.

**Carrie Chowske:** Cool.

**Carrie Chowske:** Yeah, that looks like a handy model that we can maybe apply to some of the other customers.

**Darrell Etherington:** Like, I'm thinking specifically about like the new established direction for after shoot, because having the external competitor things right there might be nice for them for visibility, because it will be a lot of like, let's try to compete directly with the BP reviews.

**Darrell Etherington:** So it's Yeah.

**Darrell Etherington:** and

**Darrell Etherington:** We can just, because that's already in SEMrush, I remember finding that too, right, where it would have the competing blog posts that are performing in your opportunity space for the keyword gaps, so maybe we can set up something like that for them too, yeah.

**Darrell Etherington:** They're also supposed to share keywords with me, so I'm just going to follow up with them.

**Ehtisham Hussain:** Yeah, they are, but they're very bad about doing that.

**Darrell Etherington:** They're not great with the follow-up action items on their side, despite, in the meeting, very clearly, does it matter what Sweeney is, like, I need you to do this, Mona Lisa, and then she doesn't do it.

**Darrell Etherington:** Yeah.

**Matthew Alves-Hill:** There's another thing, Carrie, just while I'm thinking of that, that we did for, I think it was Airbyte last night, but basically like for refreshes, we did, we like exported, we did, we used a similar approach to setting up that.

**Matthew Alves-Hill:** That content OS table, but like, basically you can, you can roll up like an export out of SEMrush for like, if you're doing content, if you're doing article refresh, and then it will like, by following that formula, it will show you like the pages with the highest potential volume.

**Matthew Alves-Hill:** And then it's like, okay, these are the ones like you start with, with the refresh.

**Matthew Alves-Hill:** So in terms of like, building a strategy around how you, how you would order a refresh, you have this data in front of you that says, okay, this page is like, has the highest potential volume, and like the most keywords or whatever.

**Matthew Alves-Hill:** So we're doing it for, for Airbyte, it's because like, most of their content is AI generated.

**Matthew Alves-Hill:** So it's like a whole website, you know, it's just like, pick an article and it will be improved.

**Matthew Alves-Hill:** But it was, it was quite a nice, like, easy way to see it all and be like, okay, this page versus like, let's not spend time on this one until the end.

**Matthew Alves-Hill:** I can shoot you a link to that Airtable, actually, if you want to have a look.

**Carrie Chowske:** Yeah, that'd be great.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Did you guys talk about it in a stand-up or something, or did you just kind of...

**Carrie Chowske:** I actually recorded a video, because I built it from NAMM yesterday for AirBytes, so I'll send you the recording.

**Matthew Alves-Hill:** I'm going to share it in the D-general for everyone.

**Matthew Alves-Hill:** I'm waiting for it.

**Matthew Alves-Hill:** I'm basically waiting for Marcel to tell me I did it 100% correctly.

**Carrie Chowske:** Didn't make that mistake.

**Carrie Chowske:** And then I'll share it.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I'm pretty good-ish with Airtable, but some of them were complex.

**Carrie Chowske:** Things, too.

**Carrie Chowske:** I'm kind of like...

**Carrie Chowske:** I don't know.

**Carrie Chowske:** I don't do great with roll-ups, but that's fine.

**Carrie Chowske:** I just have to how to do it.

**Carrie Chowske:** I know how to connect things and how everything's structured, but it's a pain in the butt.

**Carrie Chowske:** And I know from experience that your Airtable can get out of hand really easily, and then you have a bunch of garbage you don't need, or it's just in your way.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I had four versions.

**Carrie Chowske:** I think I also learned about data governance from Edison.

**Matthew Alves-Hill:** I had four versions of that.

**Matthew Alves-Hill:** API's content OS, so they're still in there.

**Matthew Alves-Hill:** Don't look at the first three.

**Matthew Alves-Hill:** It's a disgrace.

**Matthew Alves-Hill:** Yeah, cool.

**Darrell Etherington:** Yeah, that's another thing that we were talking about standardization in one of the director meetings, and you can't really, unfortunately.

**Darrell Etherington:** You could start with a standard, and then they all spiral because the client demands it.

**Carrie Chowske:** What I think would be helpful, Darrell, is like, because I almost asked this several times, but it's kind of like having this hierarchy of, or I don't even know if they can, that they can change, like, the settings for what you have access to, but, like, certain things that cannot change.

**Carrie Chowske:** Like, these weeks, that's how we're doing our reporting.

**Carrie Chowske:** But, like, I don't know, for instance, if, like, like, Yurko has, like, clusters and subclusters, and they're not set up very well.

**Carrie Chowske:** To be honest, they're not, like, there's, like, the cluster and the subcluster are called the same thing.

**Carrie Chowske:** Like, what's the point of that?

**Carrie Chowske:** But in theory, you could have, like, cluster about, like, communication, you know, techniques and tips or whatever.

**Carrie Chowske:** And

**Carrie Chowske:** And then have, like, translations and texting, and you can have all these, like, subclusters in there.

**Carrie Chowske:** And, like, that's really great for, like, looking at the kind of depth, like, Jessica's been asking us for in reporting.

**Carrie Chowske:** So that's kind of what I ended up doing, but I had to go back in and change it.

**Carrie Chowske:** But, like, you can't change the topic cluster one, right?

**Carrie Chowske:** Because every looker is, like, built off of those for cohorts, but you can have other cohorts.

**Carrie Chowske:** Like, you don't have to just have that one, and then you can build reporting off of those things.

**Carrie Chowske:** So it's kind of, like, if they can just give us literally a list of, do not ever change these.

**Carrie Chowske:** These, if you change them, aren't going to break anything, but keep them standard.

**Carrie Chowske:** If you're adding things, like, you know, you want to add things, make sure that you have a schema before you, like, start doing that.

**Carrie Chowske:** Like, that would be kind of cool, because I think a lot of people just make something work for them and don't think about, like, if you have to hand it off, if you're coming into it and trying to decipher it, like, and it's not standardized, then we're all, like, that was a big problem we had, right?

**Carrie Chowske:** We did all these client handoffs.

**Carrie Chowske:** They weren't standardized, which it's fine if there's notes for whether or not they're indexed and when they've last been, we've requested them or whatever.

**Carrie Chowske:** That makes sense to have.

**Carrie Chowske:** Not every account is going to want that or need that.

**Carrie Chowske:** I don't need it for anything else.

**Carrie Chowske:** It's fine if I add that.

**Carrie Chowske:** It's not in anybody's way.

**Carrie Chowske:** But if I'm changing what the statuses are to something, like we said, it took us way too long to figure out why there were things that the status was metadata.

**Carrie Chowske:** Oh, yeah, yeah.

**Carrie Chowske:** What hell?

**Darrell Etherington:** It just meant that they were like...

**Darrell Etherington:** Yeah, those statuses should be standardized.

**Darrell Etherington:** There's no reason not to do that, right?

**Carrie Chowske:** If they would get, maybe next time you guys talk about that or something, or if you want me to post it, I can.

**Carrie Chowske:** There's also a fixed, there are a fixed number of things that they need for the looker, specifically.

**Darrell Etherington:** And one of them, which is interesting, because I'm looking...

**Darrell Etherington:** at Yorco right now that I need to get clarity on is a plain text version of the cluster because apparently it can't pull the cluster tag if it's the drop-down variable, which I was like, isn't it doing that in Yorco's Looker already?

**Darrell Etherington:** But Dave said very specifically it can't if it's one of the color-coded drop-down variables that cannot be read or interpreted by Looker.

**Darrell Etherington:** You probably could set up an automation that whenever you select one of those that it creates a plain text version in another column.

**Carrie Chowske:** Yeah, so it's something we can easily just go in and add to the different bases because otherwise that's a lot of, again, the copy and the pasting.

**Carrie Chowske:** I did it for Aftershoot.

**Carrie Chowske:** Luckily we had only published eight articles for them, but I just manually did it all, right?

**Darrell Etherington:** We have like 500 for good call and I don't want to be doing that.

**Darrell Etherington:** And the last updated, that was another place we ran into trouble.

**Darrell Etherington:** We don't always have both the published data and the last updated recorded somewhere.

**Darrell Etherington:** Like last updated, meaning last time we like refreshed it or last updated last time?

**Carrie Chowske:** The original and the last time it was changed, whether our side or, you know, their side.

**Darrell Etherington:** like it's ideally it's always our side with the customers, but maybe in some instances they're doing refreshes independent of us.

**Darrell Etherington:** But we should still know that for the purposes of the Looker dashboard.

**Darrell Etherington:** Yeah, I don't think we've been.

**Darrell Etherington:** That was the other thing, too, is like I didn't want to.

**Carrie Chowske:** There was never like really a standardization on the on how we were categorizing refreshes.

**Carrie Chowske:** And like, I think I told you this, but like the reporting for Yurko was a mess because it was categorized as a refresh like three different ways.

**Carrie Chowske:** So the cluster was refreshed, the subcluster was refreshed, the type, the content type was refreshed.

**Carrie Chowske:** And I'm like, yeah, I mean, the other things unless they're reflected.

**Darrell Etherington:** And the site architecture shouldn't matter, the cluster and the subcluster, right?

**Darrell Etherington:** Well, in terms of if I want to break it down for reporting, yeah.

**Carrie Chowske:** So at some point, it just looks like what happened with Yurko was they had clusters and they were like, we don't like the way those are named.

**Carrie Chowske:** We're going to name them different things.

**Carrie Chowske:** They changed some of them and they called them subclusters.

**Carrie Chowske:** They're not actually subclusters.

**Carrie Chowske:** They're just the new name.

**Carrie Chowske:** Right.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** But I went back in and kind of tried to make them more cluster, subcluster so that we can break that reporting down if we want to say, well, these are all topics about communication, you know, about like communication.

**Darrell Etherington:** that doesn't matter for an updated metric because that's an external thing.

**Darrell Etherington:** No, no, no.

**Darrell Etherington:** But, but it, well, it does because that's what it's pulling from, right?

**Carrie Chowske:** So like it hasn't, I think the data is like blended between the daily down, like the down, download from AirCable and search console.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** But the, but the updated number is the number we input or is.

**Darrell Etherington:** Reflected on, like, actually, ideally pulled directly from the timestamp in their CMS, as opposed to something that reflects anything we did internally.

**Darrell Etherington:** Right, okay.

**Darrell Etherington:** Yeah, just, the last updated, very specifically, just means the last time the external property was touched, not the last time we touched it.

**Darrell Etherington:** Okay, so we don't have to do anything with that, then, is what you're saying.

**Darrell Etherington:** No, no, no, we need it.

**Darrell Etherington:** It's, it's, the last time we push changes to their live website is, is the last updated thing.

**Darrell Etherington:** Okay.

**Darrell Etherington:** You know what mean?

**Darrell Etherington:** So if it's a blog post, and it gets an update that, like, oh, new content for March 2025, and that date happened on, you know, March 28th, 2025, at whatever time, like, that timestamp should be reflected in the last updated.

**Darrell Etherington:** But, but, any changes we make internally don't need to be reflected in the last updated.

**Darrell Etherington:** Yeah, that makes sense.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Yeah.

**Carrie Chowske:** That's why I was asking you for something, because you said it was...

**Carrie Chowske:** Based on when it was updated on their CMS, but you're saying, like, we're just manually updating that.

**Carrie Chowske:** It's not pulling that from...

**Carrie Chowske:** Well, it should.

**Carrie Chowske:** We shouldn't have to manually have to.

**Carrie Chowske:** That's terrible.

**Carrie Chowske:** Like, we should be able to somehow get...

**Darrell Etherington:** Sorry.

**Darrell Etherington:** No, I didn't mean, like, manually, manually.

**Darrell Etherington:** meant, like, we have to keep track.

**Carrie Chowske:** It has to be kept track of an error table, whether we automate that or make it manual.

**Carrie Chowske:** Yeah, yeah, yeah.

**Carrie Chowske:** Right now, publish date is there, but we don't have, most of them, this, which was, like, news to me.

**Darrell Etherington:** Like, when Dave told me that, I was like, oh, okay.

**Darrell Etherington:** Well, we don't have that.

**Darrell Etherington:** There's one in your code, but it's not set up correctly.

**Darrell Etherington:** was looking at it yesterday, the way that it was only to, like, I don't know.

**Darrell Etherington:** Anyway, so, we've got to figure out, like, what...

**Carrie Chowske:** Because it's really, it's determined based on, like, when certain field changes, and I'm like, well, that doesn't really help, so we've got to come up with some other way to do it.

**Carrie Chowske:** So, anyway.

**Carrie Chowske:** It might be through a scrape.

**Darrell Etherington:** It might be through a scrape of their site, like, like a page diffing scrape of some kind, right, that then feeds back in for the, for the specific URLs, if we can figure out a tracking for that, but maybe something to talk to...

**Carrie Chowske:** Yeah, think there's another thing, too, that I was going to, like, do we, is there, is anybody, I haven't looked yet, I don't know if anybody knows, is there anything in the works, like, for them to, when you create, like, a new assignment or something, like, or some sort of, actually, it would be better if it was an atlas, like, where you, it would also add, like, a Google Doc and just put it in the right folder and put the stuff in it and all that stuff.

**Darrell Etherington:** Yes, I mean, that is something, that, that's, they should be able to do that, because it was possible in AirOps, so, like, it's, there's no technical barrier to it, but, we should.

**Darrell Etherington:** I just don't know if there was already, like, a request in for it, because I just feel like that would be.

**Darrell Etherington:** I'm not sure if there is.

**Carrie Chowske:** Like, with GoodCall, we don't necessarily, we don't really need to make, put things in Google Docs, because it's, it's, you know, programmatic, so usually we're just editing right in atlas, but for, like, your co, and probably for engine, it probably, it needs more editing.

**Carrie Chowske:** Yeah, I'll do some searching around and, oh, there's an integrate with Google Workspace ticket.

**Darrell Etherington:** I wonder if that's it.

**Darrell Etherington:** But no, that's not it.

**Darrell Etherington:** I'll look around at the existing tickets and see if there is one because that would be helpful for the majority of our clients.

**Darrell Etherington:** So it must be a common need.

**Carrie Chowske:** Especially since we have like a schema and a hierarchy for like how we're doing internal and external, like it would automatically just do that.

**Carrie Chowske:** And then there's no like, did you put it in the right folder?

**Carrie Chowske:** Are you sharing it with everybody?

**Carrie Chowske:** Yeah, yeah.

**Darrell Etherington:** That is all manual and highly repetitive, which is what they keep saying, flag those things for us and then we can automate them, right?

**Darrell Etherington:** So the perfect candidate.

**Darrell Etherington:** And also, it's part of the plan for the future state of Atlas is to have that integrated natively, right?

**Darrell Etherington:** Like the document organization and the document editor for collaboration.

**Darrell Etherington:** So worthwhile.

**Darrell Etherington:** Sorry.

**Darrell Etherington:** No, no, no.

**Darrell Etherington:** Excuse me.

**Darrell Etherington:** Cool.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Oh, I also wanted to call out before I forget.

**Joe Sovar:** Oh, yeah, Joe, go ahead.

**Joe Sovar:** Can I just say about their table in your call, Carrie, would it be useful for you to have a meta title, your URL slug, and the meta description category?

**Joe Sovar:** Yeah.

**Joe Sovar:** then I can, from Atlas, directly copy-paste it there, so you don't have to go in Atlas while publishing the articles.

**Joe Sovar:** That would be much faster.

**Joe Sovar:** For all the clients I worked for, well, before, there was always that category, but in your call, you don't have that.

**Joe Sovar:** So, if that would be helpful.

**Joe Sovar:** They're in there.

**Joe Sovar:** They're just hidden.

**Joe Sovar:** So, like, if you open up the record, yeah.

**Carrie Chowske:** Yeah, they're in there.

**Carrie Chowske:** I'm looking at them.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** It just depends on what view you're looking at or if you open up the individual record.

**Darrell Etherington:** Because in two to three weeks, I'm working on them.

**Joe Sovar:** I haven't seen them.

**Joe Sovar:** That's why I'm asking.

**Joe Sovar:** Yeah, no, I apologize.

**Joe Sovar:** Yeah, we can.

**Joe Sovar:** Yeah, we

**Carrie Chowske:** But what I do for Airtable, I don't know if anybody else is doing this, but I set up my own views for the way that I like to look at things for the stuff that I need, because there's so many fields there, and they get in your way, and you don't need them all.

**Carrie Chowske:** So if anybody needs help setting up a view for themselves, I can show you how to do that.

**Carrie Chowske:** It's pretty straightforward.

**Carrie Chowske:** Okay, then I will, from now on, I will copy-paste it there.

**Joe Sovar:** Meta titles, meta descriptions, and URL slugs.

**Joe Sovar:** It will be faster than going to go to for everything.

**Darrell Etherington:** Yeah, Joe, on the left, if you look at the, I mean, the one that most specifically has this is the meta titles and descriptions view under the editor view collection.

**Darrell Etherington:** I don't think it does, because I think that one's set to filter out some stuff.

**Carrie Chowske:** Like, it's set, I think that was done for when Cedira was, like, that stuff.

**Carrie Chowske:** Oh, okay.

**Carrie Chowske:** I think, yeah, I think that I'm looking at it, but it has them, but it looks like it has a limited number of assignments.

**Carrie Chowske:** Yeah, the monthly schedule one's probably, yeah, the monthly schedule one's probably the best view, because that's

**Carrie Chowske:** It's the one that the client's looking at, too, to see.

**Carrie Chowske:** Oh, yeah, that's a good one.

**Carrie Chowske:** And it shows the status of what we're working on.

**Carrie Chowske:** Yeah, and that's got those fields visible.

**Carrie Chowske:** Okay.

**Carrie Chowske:** But, yeah, Joe, make yourself, like, your own personal view, too.

**Carrie Chowske:** Like, then you're the only one that can see it.

**Carrie Chowske:** So you can do whatever you want with it and make it, you know, only what you want to look at.

**Carrie Chowske:** You know, it's all still there, but you're just seeing the things that matter for what you're doing.

**Carrie Chowske:** Because some of this stuff's just background, and some of it's stuff that I need, some of it's stuff the client wanted, like, you know.

**Carrie Chowske:** Yeah, this is the thing we really need to improve product, because it doesn't make any sense like this.

**Darrell Etherington:** It's not designed for this usage, like Airtable, right?

**Darrell Etherington:** It's not designed as a dual, like, consumer-facing, client-facing, plus actual utility.

**Darrell Etherington:** Well, it is, like, but you have to set up, like, interfaces for that.

**Darrell Etherington:** Yeah, yeah, we haven't done the external interface part of it.

**Darrell Etherington:** That we've done, like, only the back-end expose.

**Darrell Etherington:** Yeah, yeah, it can be.

**Darrell Etherington:** I mean, you can set it up that way.

**Darrell Etherington:** I don't hate Airtable.

**Carrie Chowske:** Airtable is just.

**Carrie Chowske:** Oh, I love Airtable.

**Darrell Etherington:** It's very flexible, but it's too flexible, probably, for broad users all collaborating all at once, internal and external, without sanitized, access-controlled views, right?

**Darrell Etherington:** Yeah, yeah.

**Darrell Etherington:** And because we've, in the past, just shared the entire base with the clients, like...

**Carrie Chowske:** With editor permissions.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** It's like, could we just maybe give them access to just what they need, and then, you know, yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Oh, yeah.

**Carrie Chowske:** I know.

**Carrie Chowske:** Ehtisham knows.

**Carrie Chowske:** I hate...

**Carrie Chowske:** We had the messiest Airtable at one of the agencies we were at, and it was like...

**Carrie Chowske:** It was crazy.

**Carrie Chowske:** It had, like, duplicate fields, and fields that didn't work, and fields that did work, and things that were automated, and automations would break if you didn't use it right, and then it wouldn't calculate things correctly.

**Carrie Chowske:** It was a mess.

**Carrie Chowske:** So, like, I'm a big fan of get your data freaking...

**Carrie Chowske:** I mean, can...

**Carrie Chowske:** Especially because we're automating so much stuff, like, if you don't have good...

**Carrie Chowske:** ...data management practices, like, you're screwed.

**Carrie Chowske:** Yep.

**Carrie Chowske:** Yep.

**Darrell Etherington:** Yeah, the other thing that I was going to bring up just for my housekeeping, I moved the weekly one hour earlier just for that will consistently be better on my schedule side and hopefully better for everybody because it's earlier and most people are in earlier time zones.

**Darrell Etherington:** But yeah, except for Carrie.

**Darrell Etherington:** No, I'm just not a morning person.

**Darrell Etherington:** It's 9-15 for me.

**Carrie Chowske:** It's not that early, but I'll be fine.

**Darrell Etherington:** I'll live.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Anything else anybody wanted to talk about that, you know, is group share worthy or you want people to be able to learn from your learnings, perhaps?

**Carrie Chowske:** Jenny set up a perplexity space for, like, our good call stuff.

**Carrie Chowske:** I think that's a good, like, idea for sometimes keeping track of some of the more nuanced stuff as opposed to, because we can't keep it all in that client content.

**Carrie Chowske:** The text and the artifacts, like it's too much.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So it's a good way to kind of keep track of some of the other stuff.

**Darrell Etherington:** I don't know, Jenny, if you want to share it with everybody so they can see kind of what you did, that would be cool.

**Darrell Etherington:** I think that would be helpful.

**Carrie Chowske:** Yeah.

**Jenny Macrohon Dabon:** So before I was using the notebook LM, and I think I mentioned that before as well, but now I found that we can also do something similar on perplexity.

**Jenny Macrohon Dabon:** So you create a space and then you put in all the resources that you have.

**Jenny Macrohon Dabon:** So I put in the documentation that we have and then transcripts as well.

**Jenny Macrohon Dabon:** So just turn that into like a document or PDF and then you can put, add it as a resource.

**Jenny Macrohon Dabon:** Let see if I can share it briefly.

**Jenny Macrohon Dabon:** Yeah, I found it.

**Darrell Etherington:** If you can, if you log in with the team growthx thing to the perplexity pro account, it's in one of those spaces on the left-hand side in good call.

**Darrell Etherington:** Is that what you're?

**Darrell Etherington:** Yeah, I just used my personal one for this.

**Jenny Macrohon Dabon:** Oh, I was not looking to do that.

**Jenny Macrohon Dabon:** To the perplexity.

**Jenny Macrohon Dabon:** Because we have one in the Teams one, too.

**Jenny Macrohon Dabon:** I don't know what's in there, then.

**Darrell Etherington:** Oh, I don't know.

**Darrell Etherington:** I can see that one.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** But yeah, I like that.

**Carrie Chowske:** One of the things I like about perplexity is it lets you use just specific sources.

**Carrie Chowske:** I've always liked that, and I think that's a really handy thing, too, if you're trying to just reference certain documents or certain pages or something.

**Carrie Chowske:** It's really helpful.

**Jenny Macrohon Dabon:** And I also wonder if you can, like, edit list as a fact-checking step, just to have that in there.

**Jenny Macrohon Dabon:** You probably could, but it would probably have to be public, or it would have to.

**Carrie Chowske:** I don't know how that would work with how they're using the API, but, like, I would imagine if a public space, it's, like, accessible if you have the link, that you probably could put that as the fact-checking link, yeah.

**Carrie Chowske:** I don't know.

**Carrie Chowske:** I don't know.

**Carrie Chowske:** I haven't looked in the settings on the spaces that deep, but I know you can make them public or...

**Carrie Chowske:** Yeah.

**Carrie Chowske:** don't Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** You can actually, you can use, you can use access management.

**Carrie Chowske:** Yes, maybe we should set up this team as one then so that everybody can get easy access to it.

**Darrell Etherington:** Unless everyone can access yours, Jenny, but the, one of the teams one has all the pro advantages or whatever, right?

**Darrell Etherington:** But we can just mirror it with the existing.

**Darrell Etherington:** I'm trying to see what the, I can't see what repositories it already has in it.

**Darrell Etherington:** I don't think it has any at the moment, actually.

**Darrell Etherington:** Yeah, it has no sources currently, so it's just been set up as a skeleton, I think.

**Darrell Etherington:** You can do it, you can do a similar, similar thing in Claude as well.

**Matthew Alves-Hill:** So, yeah, like, for writing specifically, which is quite handy.

**Matthew Alves-Hill:** Like, I think, like, what Jenny's done in Perplexity and then, like, plus Claude, then you have, like, the context on both sides, like research and then writing in both spaces.

**Matthew Alves-Hill:** Pretty cool.

**Matthew Alves-Hill:** Yeah, Claude, you set that up as a project, is that

**Darrell Etherington:** Right, Matt?

**Darrell Etherington:** Exactly.

**Darrell Etherington:** A project, and you can put in, like, a ton.

**Matthew Alves-Hill:** I tried doing it what Jenny did on Perplexity.

**Matthew Alves-Hill:** For some reason, I think I was, like, running into, like, the amount of context I could upload.

**Matthew Alves-Hill:** But maybe they've changed it or something in a recent update.

**Darrell Etherington:** But Claude's crazy.

**Matthew Alves-Hill:** I mean, like, we've dumped in, you know, everything that we've collected from a client in the first four weeks, so it's, like, 5% context fault or something.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Yeah, we should set up those for everyone.

**Darrell Etherington:** Maybe I'll just spend some time getting that in the pod thing for all of our clients, and then we can all contribute and collaborate to that.

**Darrell Etherington:** But everyone should have a project, because then it makes it a lot easier when you want to query a specific thing or revise the artifacts and stuff.

**Darrell Etherington:** And then, yeah, I'll try it with spaces, too.

**Darrell Etherington:** But maybe, to Matt's point, we're hitting the account limits on, like, uploadable context, because there's a bunch of other...

**Darrell Etherington:** Clients are already in there, so, I don't know, see.

**Darrell Etherington:** It might be good, though, for the, like, we were saying for, like, the fact-checking and stuff that might be good.

**Carrie Chowske:** Because I like, I like that, I don't know, I haven't, I haven't done this with Claude, because I usually use Claude through perplexity, but they're, like, you can limit where it's searching from, which is nice, so that, like, because one of the things that keeps happening is, like, we're getting, we're getting, like, linked to pages that are talking about, like, good call, right, and they're saying not great things, you know, so, like, I mean, it's not negative, but it's not, it's not good calls content, it's not the same way, so it's, like, it might point out things that maybe you're not wanting to highlight, so, like, you can tell, like I said, you can tell perplexity, be like, hey, just ignore that stuff and focus over here.

**Carrie Chowske:** Right.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Okay.

**Darrell Etherington:** Okay, that's helpful, and that's a good go-forward project to start building these knowledge bases in the external.

**Darrell Etherington:** Tools.

**Darrell Etherington:** Anything else with Atlas?

**Darrell Etherington:** I know it's like there's been a bunch of bugs reported in Zapped.

**Darrell Etherington:** Hopefully they got the external links one fixed.

**Darrell Etherington:** Kirkland was working on that, and that was a big problem for a lot of folks.

**Darrell Etherington:** Um, Carrie, we can sidebar, but we might need to go to Kirkland for some fixes on the, that Duplo PSEO to incorporate, like, to give it specific instructions to incorporate code snippets in the one thing.

**Darrell Etherington:** And the one thing that I need to figure out for him also is I do not want to rerun all the, like, artifact collection for the logos and stuff because basically we're out of credits, but we have them all, so we shouldn't need to do that.

**Darrell Etherington:** It should be able to just repurpose the ones that already took, but I need his help on this one.

**Darrell Etherington:** I'm going to have to, like, file a ticket and also just Slack message because those two things are both, like, big and annoying and also small and stupid, and so it's like, let's get this done.

**Darrell Etherington:** We can give them the thing, wash our hands of it, each go our merry way, and be happy.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** And I'm glad that he was fine with looking at just this part of it, because I'm like, that would have really sucked to get all, like, 2,200 of the run.

**Carrie Chowske:** mean, yeah, he's not going to, he will, it's not possible for human review anyway, right?

**Darrell Etherington:** So, yeah.

**Darrell Etherington:** Yeah, that one is very frustrating, just because it's a little bit of, like, you don't know what you want.

**Darrell Etherington:** And so, therefore, you have no idea what good looks like, and it's going to be annoying back and forth, where you're like, here's a bunch of bad stuff.

**Darrell Etherington:** Can you build me a great product on the basis of this bad stuff that I give you?

**Darrell Etherington:** Right.

**Darrell Etherington:** No, we can't.

**Darrell Etherington:** But also, you don't know what it looks like, so hopefully that resolves it, and you can just go away.

**Darrell Etherington:** I'm also glad he can just deliver that CSV to him instead of having to, like, parse all the JSON out of it, because that's annoying.

**Darrell Etherington:** No, they can do that on their side.

**Darrell Etherington:** But, yeah.

**Darrell Etherington:** So expect more from that specifically, Carrie, later, should I?

**Darrell Etherington:** All right.

**Darrell Etherington:** If you do talk to Kirkland before I do, like, there's a whole bunch of them in there.

**Carrie Chowske:** Like, and if he has to redo it so that, you know, when it wipes out all whatever's in there, he can wipe those.

**Carrie Chowske:** They're fine.

**Carrie Chowske:** I'm not, we're done with them.

**Carrie Chowske:** Like, that's the ones I ran and gave to Adrian already, so we don't need them.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Even though there's ones that haven't been run yet.

**Carrie Chowske:** Good to know.

**Carrie Chowske:** All right.

**Carrie Chowske:** Uh, yeah.

**Darrell Etherington:** I'm going to call it here unless somebody else has anything that they wanted to share, but otherwise, let's go get them.

**Darrell Etherington:** We got new clients coming on.

**Darrell Etherington:** It's exciting.

**Darrell Etherington:** We're going to be, like, more of a full capacity after next week.

**Darrell Etherington:** There'll be seven clients on books instead of four where we're at.

**Darrell Etherington:** Another thing, too, depending on how long our pause with Good Call goes.

**Carrie Chowske:** Oh, that's true.

**Carrie Chowske:** Okay.

**Carrie Chowske:** So we're actually at, like, six active.

**Carrie Chowske:** You know, pulled in on some other stuff, if needed, probably.

**Carrie Chowske:** Like, if he pays it right away, and we go right back to work, then no.

**Darrell Etherington:** I don't suspect that will happen, but we'll see.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Is Jürgen on?

**Jürgen Linde:** Yeah, I'm here.

**Darrell Etherington:** Farewell.

**Darrell Etherington:** Thanks, Matt.

**Darrell Etherington:** Thanks for everything you did.

**Darrell Etherington:** was great working with you, and really appreciate all your contributions, but, yeah.

**Darrell Etherington:** Yeah, thank you, Jürgen.

**Saskia Wartnaby:** It was really great working for you, even though it was a short little while when you were my managing editor, but it was really great.

**Darrell Etherington:** Yeah, it's always emotional for me when I leave a company.

**Jürgen Linde:** I have to say goodbye to so many great people.

**Jürgen Linde:** And Saskia, Matt, like, I've worked very close with you, and both of you are doing amazing.

**Jürgen Linde:** And, Daryl, thank you for.

**Jürgen Linde:** Thank everything, and the rest of you, I wish I got a chance to work with you, but that's how life goes, but I'm definitely going to miss you all, so thank you.

**Jürgen Linde:** We'll miss you too, Jürgen, and thanks for everything, and maybe you'll work with the rest of the folks in some future iteration.

**Darrell Etherington:** Definitely.

**Darrell Etherington:** All right, take care, everyone.

**Darrell Etherington:** Hi, everybody.
