# Augment Code Website Run-through

<metadata>
date: 2025-06-30
time: 17:02 UTC
duration: 18 minutes
organizer: kirkland@growthx.ai
participants: Chris Kelly, Kirkland Gee, George Haikal
fathom_recording_id: 71315278
fathom_url: https://fathom.video/calls/337816566
share_url: https://fathom.video/share/gsxRfSCsyghpRCYnfzaUMQ7AxUqkDM_x
source: fathom
enriched_on: 2026-03-03 22:14 UTC
</metadata>

---

## Summary

GrowthX and Augment Code aligned on two critical website features: adding a guides section (a Sanity CMS duplicate of the existing blog structure) and integrating an MCP directory pulled from Code Library. Kirkland will prototype both the guides UI and the MCP directory with a hero section, with Augment Code's designer Meghan reviewing and refining the design afterward. The team will use a dedicated Slack channel for communication, with Chris adding Kirkland to Vercel for preview deployments and GitHub access to both the main .com repo and the CMS schema repo.

---

## Context

Augment Code is building a new website with Sanity CMS, Vercel deployment, and GitHub version control. GrowthX is partnering on the project through Kirkland, who is transitioning from marketing-focused scripting into full-time engineering. This meeting was a technical run-through to unblock the website roadmap: implementing guides and integrating the MCP directory from Code Library, Augment Code's internal tool for cataloging Model Context Protocols. Chris Kelly leads Augment Code's engineering and explained the existing architecture, while George Haikal is driving the broader Augment Code product initiative that GrowthX is supporting.

---

## Relevance

- **To GrowthX Delivery:** Demonstrates hands-on frontend prototyping and CMS architecture work (Sanity, Vercel, GitHub) that strengthens Kirkland's engineering capabilities. Real-world experience with cloud-hosted CMS and query structure reuse will inform future GrowthX client projects.
- **To GrowthX Business Development:** Deepens partnership with Augment Code through technical collaboration and design iteration. Positions GrowthX team as capable implementers on client-facing projects, not just advisors.
- **To Augment Code:** Clear deliverables defined. GrowthX handles prototyping to reduce burden on Augment Code's small team. Vercel and GitHub access unblocked. Dedicated Slack channel keeps communication clean and focused.

---

## Overview

- Two main tasks: 1) Add guides section (duplicate of blog) 2) Integrate MCP directory from Code Library
- Tech stack: Sanity CMS (cloud-hosted), Vercel for deployment, GitHub for code repos
- GrowthX team (Kirkland) to prototype designs, Augment Code team to review/refine

---

## Key Topics

### Website Structure and Tech Stack

- Two repos: .com (main site) and .com CMS (Sanity schema)
- Sanity cloud-hosted, queries defined in .com repo
- Vercel for deployment, GitHub for version control
- Existing content types: rich text, images, YouTube videos, code blocks

### Guides Section Implementation

- Duplicate blog post content model in Sanity
- Change slug for new guides section
- Reuse existing query structure from blog posts
- GrowthX team to prototype design, mirroring blog layout initially
- Augment Code team to review and refine design later

### MCP Directory Integration

- Create new schema for MCP pages in CMS repo
- Build corresponding query in .com repo
- GrowthX to prototype UI elements, pulling data from Sanity
- Consider hero section with enhanced UI for MCP pages

### Design Considerations

- Augment Code aesthetic: terminal-esque, ASCII references, technical look
- GrowthX team encouraged to take design liberties for guides section
- Augment Code designer (Meghan) to review and refine later

### Project Communication

- New dedicated Slack channel to be created for this project
- Include Chris, Kirkland, George, and Meghan (designer)

---

## Action Items

**Kirkland Gee (GrowthX)**
- Duplicate blog content model in Sanity, create new query for guides in .com repo
- Create schema for MCP pages in CMS repo, implement query on .com side
- Prototype UI for guides section, mirroring blog layout with potential enhancements
- Prototype UI for MCP pages, including hero section with GitHub stats integration

**Chris Kelly (Augment Code)**
- Add Kirkland to Vercel for preview deployments
- Send GitHub invites for .com and .com CMS repos

**George Haikal (GrowthX)**
- Create new dedicated Slack channel for website update project with Chris, Kirkland, and Meghan

---

## Transcript

**Chris Kelly:** Hey, how are you?

**Kirkland Gee:** I am doing just great. Yeah, doing good. I don't really start today, so I feel like I'm actually on top of things, you know, instead of the day coming at me.

**Chris Kelly:** I had absolute chaos this morning with my three-year-old. After I dropped him off for school, I'm like, I think I'm done for the day. It's 9 o'clock, and I've exerted as much energy and emotional stamina as I possibly can.

**Kirkland Gee:** That's the whole day?

**Chris Kelly:** Yeah, it's a lot.

**Kirkland Gee:** My son just turned one three weeks ago, so I get it. Not the same, but a lot of days it's challenging.

**Chris Kelly:** My morning is very dependent on how his night and morning go. We had a lot of fun for like 45 straight minutes of physical exertion—running around, wrestling. But then getting him to daycare is the emotional war.

**Kirkland Gee:** I don't think my son has sat still for more than three minutes since he was in the womb. He's always on the go. In one sense I'm excited because I'm sure he'll be an active, curious, adventurous kid as he grows up. But I'm also like, man, I don't know if I can keep up with him.

**Chris Kelly:** Ours is exactly the same way. Between one and one and a half to two, he wants to do stuff but can't move like he knows he should, so he gets constantly frustrated. That was a really hard six months until ours learned to walk better and we could let him go do things without destroying the house.

**Kirkland Gee:** I've seen that with friends who have kids in that age range, 18 to 24 months. They don't want it, and they can't, and it's rough.

**Chris Kelly:** Yeah, but after two, it got a lot better. That frustration eased.

**Kirkland Gee:** And then it's just new challenges, right?

**Chris Kelly:** Always just different. We're talking parenting here, George.

**George Haikal:** Love it. I can't relate, but I learned a lot.

**Kirkland Gee:** Actually, more than half of our engineering team at GrowthX have kids under four. Really cool.

**George Haikal:** Thanks for jumping on so quickly, Chris. We're trying to move really fast with Augment Code. Do you have enough context on us and what we're trying to do, or should we give you some background?

**Chris Kelly:** We can just jump into the agenda. I think I know who you are and the kinds of projects you're tackling, so we can dive in. If I'm confused about anything, I'll ask.

**George Haikal:** Amazing. I'll kick it off high level. Kirkland's the expert here on what the problems are and how to unblock them. Essentially, we want to do two things ASAP on your website. The first is adding basically a duplicate version of the blog section as a guides section, where we want to start publishing our content. I already talked to Syl about it. He loves that and wants to move fast. We want to see what's blocking you and how much we can help. The second thing is we launched Code Library, which has an MCP directory. We want to pull that and do the same on your website. Those are the two things we're going to talk through to see how hard they are, what needs to get done on both sides, and how we can best help. Because we want to take as much off your plate as possible. Maybe we can start with the guides?

**Kirkland Gee:** Yeah, this should be pretty straightforward because everything's on Sanity, right? It's CMS stuff. Blogs to guides is basically just duplicating the content model, changing the slug. There's some little cleanup things, but that's all we should need to do.

**Chris Kelly:** Yeah.

**Kirkland Gee:** For the MCP servers, that's a bit more complex. For Code Library, we're using a Supabase table. It doesn't have to be Supabase—could be a JSON file. It has fields related to the MCP: GitHub stars, forks, etc. We'd map that to UI elements in Sanity. Basically, we build UI on top of that. Should be pretty straightforward.

**Chris Kelly:** Is all that in the same codebase?

**Kirkland Gee:** There's two. I haven't moved the Sanity Studio stuff into the main repo yet, but yeah. At some point I want to migrate them all together, but for now, there's just .com and .com CMS.

**Chris Kelly:** Right, and .com CMS is literally just the schema files for Sanity Studio.

**Kirkland Gee:** Got it. And those are all getting pulled into the main .com through...are they on a different... I haven't worked with Sanity a ton, so I just want to make sure I'm clear on how that works.

**Chris Kelly:** So if you haven't worked with Sanity a ton, there's schema files, and then you also have to technically deploy the schema. We're very new on this configuration. In Sanity, you design your schema and then deploy it, which pushes it up to Sanity. We use the cloud version of Sanity rather than hosting it ourselves. So you just hit the API from that cloud version of Sanity. Then the .com repo has the Sanity client already configured, and you just define your queries in the .com repo for whatever you want to hit over there.

**Kirkland Gee:** Okay, cool. Yeah, I've done Contentful and Strappy and others. It's all kind of the same. That was my one piece—where is it hosted and how do I access it?

**Chris Kelly:** There's just a client to use that. It's already hooked up. So you would just need to create a new query in .com for the guides. You can steal the one for posts and swap a single point and call it a day.

**Kirkland Gee:** Yeah, correct. Okay. And then we'll build the schema for the MCP pages in the CMS repo and create a query for that on the .com side.

**Chris Kelly:** That's right. Yeah, and then queries and types. That's where I eventually want to move it all together. You have to do the TypeScript stuff three times in three places.

**Kirkland Gee:** So you just say, hey, do this again, but different?

**Chris Kelly:** Yeah, I'm like, here's the schema file, just make the types for it. The blog post type already has a number of different block types.

**Kirkland Gee:** Are you familiar with block types?

**Chris Kelly:** I've done it in Contentful, so I assume it's similar.

**Chris Kelly:** Yeah, it already does. It's got a rich text editor that handles rendering, and it can do images, YouTube videos, and code blocks. So if you need another one, just let me know and we can figure out who does it.

**Kirkland Gee:** I think for the most part, we try to do as much of our work in Markdown as possible because it makes everything easier. For the MCP pages, we'll probably do some sort of hero that pulls in some slightly nicer UI elements. Is that something where you have design folks who you'd want to take a crack at it first, or should we prototype something and then you clean it up after?

**Chris Kelly:** I think for speed, you guys doing it first and then getting feedback from our designer and us is probably the fastest.

**Kirkland Gee:** Yeah, because I can basically say, here's the structure, this is where everything needs to live. And then if you want to go in and change the CSS to make it look different, that's probably easier for you.

**Chris Kelly:** Yeah, totally. You'll make a bunch of decisions they don't need to make. Just make the decisions and let them refine it.

**Kirkland Gee:** Okay. I think that all makes sense for those two pieces.

**George Haikal:** Were there any other things we need to talk through? Just logistically, Chris, how do you want to run the communication? Is your designer in that external Slack we have, or should we make a separate one with everybody?

**Chris Kelly:** How much noise is in that Slack now?

**George Haikal:** It will get noisy if we're running these two things.

**Chris Kelly:** Yeah, if we want a dedicated channel just for this project, that would be easier. That way you and Syl are talking strategy, and the designer doesn't have to pay attention to that noise and doesn't need to chime in on thoughts. Just for the time being.

**Kirkland Gee:** Can we do a project channel for this?

**Chris Kelly:** Yeah, I would just do a project channel. When it's done, we can wrap that up.

**George Haikal:** So are you guys good creating that, or do you need us to?

**Chris Kelly:** No, I'll make it.

**George Haikal:** Do you have a designer on your end you want to loop in?

**Chris Kelly:** Her name is Meghan. M-E-G-H-A-N.

**George Haikal:** Cool, cool. I mean, I feel pretty clear. Kirkland, we can talk about next steps of our work and what we need to do and what you need help with after. When we're making these prototypes, Chris, is there anything we should completely avoid design-wise?

**Chris Kelly:** There's very little styling on the blog. It's just text. So if you have unique design elements you want to add to the guides to make them more readable or unique, totally feel free to take some liberties. We basically go for a terminal-esque aesthetic with ASCII references and a technical look. Feel free to take some liberties.

**Kirkland Gee:** Cool. And then are there any DevOps things I should know? I'm going to do the work and open a PR. Is there anything specific, any CI stuff I need to worry about?

**Chris Kelly:** The CI is very limited. It's just all hosted on Vercel. So I'll need to add you to Vercel as well so you can see the previews.

**Kirkland Gee:** Yeah, because if I'm not added and I try—even if you merge the PR, Vercel still gets mad because I'm not a user.

**Chris Kelly:** Yeah, it's the worst. Out of all the things they do, preview deploys for external collaborators is...

**Kirkland Gee:** It's all a money racket. They're making sure we have a Vercel user who's getting paid for.

**Chris Kelly:** So what's your email?

**Kirkland Gee:** Kirkland at growthx.ai.

**Chris Kelly:** Apparently I have to upgrade to enterprise and use the project role system. Let me try a different way. I'll add you to it.

**Kirkland Gee:** If we need a workaround, just let me know.

**Chris Kelly:** No, I'm not worried about it. I'll figure it out. So is it just you, or...

**Kirkland Gee:** For now, I actually think you can just add me. None of this is super crazy design-wise. If we need to get other folks in there, I'll give you a ping.

**Chris Kelly:** Cool. And you should also have GitHub invites for both repos if you didn't see those already.

**Kirkland Gee:** I didn't see an email, but I know why—it went to my personal one.

**Chris Kelly:** Yeah, it uses your personal GitHub account. I used to work at GitHub, so I'm very familiar with the hellscape that is users versus orgs versus different emails and notification platforms.

**Kirkland Gee:** I'm in an interesting role at GrowthX where I've been coding for four or five years but was primarily a marketing person for a long time who built custom scripts, and I just made the transition into mostly full-time engineering. So it's the little stuff like that I'm still figuring out.

**Chris Kelly:** Yeah, it's a terrible system. It causes so much complexity—are you an org or a person? You're a person with these different email addresses. The identity system is all over the place.

**Kirkland Gee:** And they don't want you to have a personal and a work GitHub account, so they make that hard.

**Chris Kelly:** Yeah. I'll add you to it. Let me double check that I added you to Sanity as well.

**Kirkland Gee:** I got that, yep.

**Chris Kelly:** Okay, so Sanity and GitHub—you're all set.

**Kirkland Gee:** Excellent. Are there any other questions from you, Chris?

**Chris Kelly:** No, I don't think so. If you have any opinions or thoughts on the website or how we should tweak it, feel free to chime in. Nothing is precious. It's a very new project repo, so a lot of stuff is not standardized and a lot of design components don't exist yet. You're going to have to manually create some repetitive stuff, but we're open to extracting and reusing things.

**Kirkland Gee:** Cool, awesome. All sounds good. Thanks, Chris. Have a great day, man.
