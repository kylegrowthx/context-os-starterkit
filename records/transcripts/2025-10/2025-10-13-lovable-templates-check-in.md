# Lovable Templates Check-In

<metadata>
date: 2025-10-13
time: 17:30 UTC
duration: 24 minutes
organizer: Nicolas Castellanos
participants: George Haikal, Georgemaine Lourens, Nicolas Castellanos, Marcel Santilli
fathom_recording_id: 93750407
fathom_url: https://fathom.video/calls/437789958
share_url: https://fathom.video/share/xEFq3Xf8ZM2veod7zuVt3n9bjktbFuQL
source: fathom
enriched_on: 2026-03-02 17:18 UTC
</metadata>

---

## Summary

GrowthX is building a templates product for Lovable, an AI-powered website builder. In this check-in, the team showcased significant progress across three parallel tracks: Georgemaine completed the categories UI with proper hierarchy and breadcrumbs ready for handoff to Nicolas; Nicolas duplicated Lovable's entire website including blog section and is preparing to publish approved articles; and the team is creating 3-5 high-quality blog block templates to establish quality standards with Lovable before scaling. George will send an incremental update today with template links, gallery experience, and editorial progress to accelerate feedback cycles.

---

## Context

GrowthX is building web templates as a strategic product expansion with Lovable, a no-code website builder. This is an internal product execution meeting involving GrowthX's engineering core (Georgemaine on UI/design, Nicolas on backend/publishing, George on product/coordination). Marcel (founder) is also present. The team has already duplicated Lovable's website structure and has 3 approved articles ready for publication, with 7-8 more in the content pipeline. The immediate goal is to deliver a set of exemplary templates that prove quality and capability before scaling the templates business across multiple categories.

---

## Relevance

- **To GrowthX Delivery:** The templates workflow discovery (Tailwind UI components + Dribbble inspiration) may apply to other client projects. Long-term strategy includes outsourcing template creation to expert contractors, reducing time from core team. DCAP CMS access is blocking efficient template data upload.
- **To CheckThat:** Not directly mentioned in this meeting.
- **To GrowthX Business Development:** Strong execution signal—3 approved articles ready, website infrastructure complete, quality bar being established. Next update to Lovable will be concrete deliverables (template links, gallery UX, editorial progress) rather than roadmap. Potential for reference/case study if Lovable adopts templates at scale.

---

## Overview

- Significant progress on categories UI, template creation, and website duplication
- Focus on delivering 3-5 high-quality blog templates to benchmark quality with Lovable
- Immediate goals: finalize categories UI, productize gallery, and publish approved articles

---

## Key Topics

### Categories and UI Progress

  - Georgemaine implemented new categories with labels and icons
  - Hierarchy, breadcrumbs, and routing functionality working
  - UI polish to be completed today and handed off to Nicolas

### Template Creation Workflow

  - Exploring more efficient workflow using Tailwind UI components and Dribbble inspiration
  - Nicolas working on refining the AI-driven template generation process
  - Aim to create 3-5 high-quality blog templates for quality calibration

### Website Duplication and Publishing

  - Nicolas duplicated Lovable's website, including blog section
  - New /guides section to be created, mirroring blog structure
  - Three approved articles ready for publication, 7-8 more in pipeline
  - Publishing process: manually add Markdown files to repo (for now)

### Template Showcase Strategy

  - Initially, templates will be showcased in website footer, not main navigation
  - Decision on prominent placement pending Lovable's approval of template quality

### Project Management and Communication

  - Team to send incremental updates to Lovable for faster feedback
  - Upcoming update to include template examples, gallery experience, and blog/guides progress
  - Awaiting DCAP access to streamline template data uploading process

### Workload and Long-term Strategy

  - Current pace is good, focus on maintaining template quality
  - Exploring options to outsource template creation to expert contractors in the future

---

## Action Items

**Georgemaine Lourens (GrowthX)**
- Finish categories UI polish and hand off to Nicolas
- Create 3-5 high-quality blog website block templates for quality calibration with Lovable

**Nicolas Castellanos (GrowthX)**
- Duplicate blog section into /guides with same UI and backend structure
- Post Markdown files for first batch of approved blog articles to Lovable's repo

**George Haikal (GrowthX)**
- Send incremental update to Lovable today: 2 template links, gallery experience link with password, template categories overview, and editorial progress on 3 approved + 7-8 pipeline articles

---

## Transcript

**George Haikal:** What's up, Nico?

**Nicolas Castellanos:** Good.

**Nicolas Castellanos:** How's George?

**Nicolas Castellanos:** All good?

**George Haikal:** Good morning or good night, good evening.

**Nicolas Castellanos:** How are you guys doing?

**Georgemaine Lourens:** All good. Not a holiday for you guys, right? Just the working day.

**George Haikal:** Just working, just working. Me too. But it's great not having too many meetings. When everyone else has a holiday, you kind of get some time to think and actually get work done. So it's been great.

**Georgemaine Lourens:** All right, nice. Well, I hope you get to use it productively. Do you guys want to jump into it?

**George Haikal:** Yeah, let's do it. How has it been since Friday? What progress has been made? Where do you guys think you need the most help right now or other access or anything that's blocking?

**Georgemaine Lourens:** On my end, I can quickly share my screen, but this is still a work in progress. So for me, I've been working on the categories. I got all of the new ones that Ada and you worked on, and I put them in. I'm going to go with these labels plus an icon because Lovable has a lot of icons. I need to finish them all up, but I think this should be good. Each category has subcategories, so the route works, the hierarchy, and the breadcrumbs all work. I should be done with this today, and then Nicolas can come in and polish the code and make it production ready.

**Georgemaine Lourens:** I also met with Daniel today to talk about the templates to see if we can find a more efficient workflow. Right now I'm just polishing a lot in Lovable—it works, but it's also a lot of rounds. But he had this idea where we could use Tailwind UI components and just paste in the code and add an image from Dribbble as inspiration and go from there. I shared that idea with Nicolas and I think he's feeling it too.

**Georgemaine Lourens:** My goals are to wrap up the categories UI today and hand that off to Nicolas, and then I'll be full-time on templates. I feel confident I can deliver at least three to five good block templates that we can use to calibrate on quality with Lovable.

**George Haikal:** Amazing. Great stuff, man. It looks good.

**Georgemaine Lourens:** You want to go next, Nicolas?

**Nicolas Castellanos:** Yep. So, yeah, Georgemaine said we're working on the template workflow. I'm going to apply that idea Daniel shared. I'm also doing some general fixes on that workflow, trying to get it a little less strict. Right now it starts iterating a lot on the same problems—finding missing features and adding them repeatedly. I need to get it less strict so it finishes at some point and doesn't keep adding features like crazy.

**Nicolas Castellanos:** Apart from that, my plan is to focus on that today, and then either tomorrow or Wednesday, start productizing the gallery. What are your thoughts on what we should focus on—templates or the gallery itself? What are the most important things you think we should be sharing with Lovable about the gallery?

**George Haikal:** Yeah, I think what's ASAP to show them are the templates—what an example of good looks like for three to five templates. Georgemaine, you're working on that next, which is good because then we ground the conversation in what we can do, what the quality looks like for our templates, here's the categories we want to start targeting, and here's the gallery and experience we want to create. But that's all downstream from—does this template look good enough that they'll trust us to produce these at scale based on our strategy, which is the categories we're choosing and the design UI experience and layout, duplicating the /guides and making a new templates section. So I think that's all downstream of the templates, but it's good that they're all working in parallel right now.

**George Haikal:** And then the other thing is getting to publish on the website. We already have three approved articles that are ready to go and another seven or eight in the pipeline. We're going to have a weekly number of articles ready to go and published. Their team has been really good at reviewing and getting back to us quickly. So the only block there is duplicating the /blog on their website and creating the /guides section.

**Nicolas Castellanos:** We have that here. Let me share the link. They just shared us the password to the review app.

**George Haikal:** Okay.

**Nicolas Castellanos:** So let me share that to you.

**Georgemaine Lourens:** So you already duplicated their blog, Nico?

**Nicolas Castellanos:** Everything. The blog included.

**Georgemaine Lourens:** You're quick.

**George Haikal:** Go, Nico. You both are, to be fair.

**Georgemaine Lourens:** Yeah, it's amazing progress.

**Nicolas Castellanos:** I can get you the password for that link. The blog, if you do /blog, the blog should be there. But they already have a blog, so we need to create /guides instead. The way they send blogs is like MD files into the repo. Is that the same plan we have for sending ours?

**George Haikal:** The way they publish blogs right now is just markdown. It's just manual markdown. If that's the way they've been doing it, we can just do that quickly for the first couple and have it ready.

**Nicolas Castellanos:** I'll look into the channel and see what we have. I'll duplicate this into guides and maybe send a couple to show how it looks.

**George Haikal:** Amazing. Where should I be looking on this link, by the way?

**Nicolas Castellanos:** This link is the experience in general. You have templates and then you have blogs. I'll copy blogs to also be guides.

**Georgemaine Lourens:** Yeah, we should probably do another push on the templates because the stuff on there is probably old.

**Nicolas Castellanos:** Yeah, let me do that. This is what you should be seeing. You have templates and then the blog. Like this, with the same backend for this.

**George Haikal:** Sweet. Nice, this looks good. Cool. So I'm wondering what I can just ship over to them today. That's a good indicator of progress.

**Nicolas Castellanos:** Yeah, I'll do that right now.

**Georgemaine Lourens:** By the way, question, George. Should templates be in the main navigation at the top of the website? Because the way the conversation has been going, it feels like we still need to first prove that it works before we really show it to the rest of the world. So maybe it shouldn't be in the main nav, but only in the footer for now.

**George Haikal:** Yeah, great question. I've been thinking about it too. I think it all starts with if they like our templates and if they buy into what our templates can do for all these different categories. If they like them, and if they're something Sebastian can just add to what we're doing instead of making it separate, then I think it could live on the main. But if they don't like the quality of the templates and it needs to be more of a hidden separate experience, then we go that route. I think it's all just pending the templates. In the ideal world, I would like it to be on the main, and then it's just way easier for us to drive people to it and get engagement.

**Georgemaine Lourens:** So I think maybe to not upset anyone or to take the safe route, we should just move it to the footer and not have it in the main for now.

**George Haikal:** Yeah, for now, I think that's good.

**Georgemaine Lourens:** Okay, cool.

**George Haikal:** And then, Nico, what's the process for getting the blogs up? Let's say we have three blogs already ready and five coming. What's the process that would work best for you?

**Nicolas Castellanos:** Right now it's me. I can just send a PR with the MD file. I'll figure out how the process works. Maybe they have something different, like a workflow on GitHub that auto-publishes them to the repo. But right now what I can do is just post the MD file, send a PR, get merged, shipped.

**George Haikal:** Okay, and that's pretty easy. For the first batch, I think just making progress before this meeting makes the most sense. But if we can figure out if the process is more complicated than that with them, that would be good to uncover earlier too. Let me get you the ones that are ready to send.

**Nicolas Castellanos:** Should I run one of our workflows to get SEO metadata and stuff?

**George Haikal:** Yeah, maybe. You can ask Ada too. She's the expert here.

**George Haikal:** This makes sense to me. The two big goals are getting to publish on the blog—we're literally pretty much there. By the end of the day, we could have three articles at least sent over to them, and on the template side, progress tomorrow, and then before the meeting we'll have five or so examples we can show them. Are those just of different types of websites?

**Georgemaine Lourens:** I picked the blogs. So it should be five different blog websites. I think we have three now. We have the one from Marcel, the first one that I created with a bunch of animations, and I'm working on the third one right now. So it's five of the same category, and I think that should be a good benchmark. Here's what we can do with one and then move from there.

**George Haikal:** I agree. I think we can honestly ship that out today to them. If the one you already made and the one Marcel made are done, we could just package up a little update to them. I can say, hey, we'll be ready by the meeting with five or so of these, but there will be variations of this one website blog. This is an example of the quality you can expect. We'll come with a bunch of different variations and talk about where we want to go from there.

**Georgemaine Lourens:** Yeah, I think that could work, right?

**George Haikal:** How can they view them? It's an easier way to.

**Georgemaine Lourens:** Well, they're essentially Lovable projects, so we can just kind of share a link and they can just open it. So I don't see an issue there.

**George Haikal:** Cool. So if you could grab them from the team account, I can go grab them too, but I want to make sure I'm not picking the wrong one—the one you made and the one Marcel made. Let's drop a link in the chat.

**George Haikal:** Best case scenario, we get async updates from them today and tomorrow, and we can make even more progress by the meeting versus having to wait until Wednesday to show everything and then try to get feedback in 30 minutes. Then there's always follow-up after because they're pulling different people in. That's why I'm trying to push for sending stuff earlier.

**Georgemaine Lourens:** Yeah, no, I agree with that. These incremental updates are way better. Did they even look at the stuff you shared on Friday?

**George Haikal:** No, I just talked to them direct. I didn't send anything big out because it was going to be a Loom. While it was good progress, I wanted to wait for the templates. But Ada sent some editorial updates too, so we're in a good spot.

**Georgemaine Lourens:** Okay, cool.

**George Haikal:** So I guess our next update will be the first time they really see the templates and the gallery experience. Yeah, so let's aim for templates—the two versions—the gallery experience. So they'll be able to click around with the password.

**Nicolas Castellanos:** Yes.

**George Haikal:** And I want to give you enough time and not too much pressure, Nico, on the actual blogs. You said it should be easy?

**Nicolas Castellanos:** Yeah, it should be super easy to do. I'll timebox it.

**George Haikal:** If it's not, let me know, but it should be super easy. Cool. Where can they view that easiest? Is it on the same link?

**Nicolas Castellanos:** It could be either the same link or I can create another one. Probably safer to create another one because we'll be sending stuff to templates and we might break things.

**George Haikal:** That makes sense. And then, okay, so we'll plan for /blog. Basically we duplicated the blog into a guides, a /guides.

**Nicolas Castellanos:** Yeah. So same UI, same everything, just a different path? Cool.

**George Haikal:** And then here are the first three articles ready to go. The only thing they need to do there is review, approve, and then actually ship it on their end.

**Nicolas Castellanos:** Yeah.

**George Haikal:** Cool. You guys feel like you're getting enough from their engineering team on their side?

**Nicolas Castellanos:** Yeah, except DCAP.

**George Haikal:** Yeah, I've hit them up three or four times. I just did it again this morning. These extra review messages we're sending are because we don't have access to their CMS right now. Once they give us access, we don't have to be sending links with previews.

**Nicolas Castellanos:** What is DCAP going to help with?

**George Haikal:** DCAP will help with uploading the data for the templates—the details, the prompts, the images, the descriptions. That's taking a ton of time right now.

**Nicolas Castellanos:** But I don't think they figured out how to use it yet. So I'm not sure.

**George Haikal:** We'll make sure Wednesday we focus on that because that seems important to actually start getting this out and used. Okay, this is great. Guys, this was like two or three days of work and it's insane progress, which is good. How do you guys feel workload-wise?

**Nicolas Castellanos:** I think good. I mean, I wish we had been at this point a little bit earlier. But I think we're good.

**George Haikal:** Yeah. But then if we keep this pace, we're going to be in a great spot.

**Georgemaine Lourens:** Yeah, I think so too. I think the pace we have right now is awesome. What I'm focused on is the templates quality bar. If we can swing that in our favor, then I feel like the rest will be easy.

**George Haikal:** Definitely. And you're confident that the two links you're going to send over of the templates are pretty reproducible? It's not taking you too much time to go back and forth. Long term, I don't want this taking too much of your all's time.

**Georgemaine Lourens:** Likewise, I think the goal should be to hand this over to someone else who does it. I already spoke to Daniel about this and he has a guy that I believe you spoke to as well who can just do this full time for a month for us.

**George Haikal:** Yeah, they're expert-rated, verified Lovable coders essentially for these companies, right?

**Georgemaine Lourens:** Yeah, exactly. So I'm confident. I think the first ones take a little bit more time on my end, but I also feel like we're still figuring things out and that will get less over time. It just gets better, so I'm confident.

**Nicolas Castellanos:** Georgemaine, did you get access to the history chat of Marcel's template?

**Georgemaine Lourens:** No, I didn't. He shared a link with me, but he basically said what he did. He basically just had an image as inspiration and then he said things like, make it 10x better and populate the content and stuff like that. Like typical Marcel fashion.

**George Haikal:** It's hilarious. Cool. All right, so I'll hit you guys up a bit later to make sure we have everything. But basically, today, I want to send them the two links to the templates of what good looks like, the link with the password to the overall experience, and let them know it's the templates. They'll focus on the templates with that link. And then, pending Nico, we'll send the duplicate of the blog as well. And then I could batch up an explanation of the other template categories and the editorial progress we've made on other articles that are ready for their review as well.

**Nicolas Castellanos:** Yep.

**Georgemaine Lourens:** Sounds good.

**George Haikal:** Cool. Thanks, guys. Let me know if anything comes up.

**Georgemaine Lourens:** We'll talk soon. Later. Bye.
