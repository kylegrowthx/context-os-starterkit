# Lovable Templates Check-In

<metadata>
date: 2025-10-20
time: 17:30 UTC
duration: 27 minutes
organizer: Georgemaine Lourens
participants: George Haikal, Nicolas Castellanos, Georgemaine Lourens
fathom_recording_id: 95381467
fathom_url: https://fathom.video/calls/444847296
share_url: https://fathom.video/share/jJ1sh2tCPzvox3yXb76iCB9XvBk96xoL
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

GrowthX's Lovable Templates project team aligned on a data-driven template strategy backed by 5,000+ competitor URLs and keyword research, deciding to prioritize portfolio websites as the highest-value starting point. Georgemaine confirmed she can reliably use Claude AI to extract designs from screenshots at scale, and the team agreed on a progressive launch approach targeting ~5 templates ready by Wednesday's client meeting rather than a big-bang release. Key blockers identified: Nico needs to resolve a guide section deployment issue, George must flesh out the template strategy with Lovable-specific mini-app categories, and Georgemaine will define per-category feature lists by referencing best practices from Webflow templates.

---

## Context

GrowthX is building a library of production-ready templates for Lovable, an AI-powered web builder. This is a core deliverable for a strategic partnership — the templates will ship on Lovable's platform and drive SEO value through targeted, high-intent keywords. The meeting brought together the core delivery team (Georgemaine on design systems and template blocks, Nicolas on pipeline and technical implementation) with George Haikal, who's leading the template strategy and client relationships. This check-in happened mid-sprint to lock in prioritization and de-risk the Wednesday client presentation.

---

## Relevance

**To GrowthX Delivery:**
- Georgemaine validated Claude AI can reliably extract and nail template designs from screenshots — a key scalability lever for production volume.
- Team confirmed progressive launch (5+ templates by Wed) is more pragmatic than waiting for a full 50-template library, reducing deployment risk.
- Workflow clarity: Georgemaine owns design system/blocks, Nicolas owns pipeline and gallery production, George owns strategy and client alignment.

**To GrowthX Business Development:**
- George's data-driven strategy (5,000+ competitor URLs, keyword research, search difficulty scoring) positions GrowthX as methodical and serious — strong reference value and upsell signal.
- Portfolio website category identified as highest-priority based on real search volume — direct evidence we're optimizing for client success, not guessing.
- Progressive launch approach may accelerate time-to-revenue and improve Lovable's perception of GrowthX's execution speed.

**To CheckThat / AEO:**
- The Airtable template strategy with keyword volume and difficulty data is directly applicable to AEO research and competitor benchmarking work.
- Lovable templates represent a live case study in keyword-driven content strategy and SEO-first product design.

---

## Overview

- Template strategy: Portfolio websites identified as highest-priority starting point; George to break down into specific types (photography, artist, agency, etc.) and refine with Lovable-specific mini-app categories before Wednesday client meeting.
- Launch approach: Team confirmed progressive launch strategy over big launch; aiming for ~5 portfolio templates ready by Wednesday, then expand into other categories based on client feedback.
- Design validation: Georgemaine successfully used Claude AI to extract designs from screenshots consistently; exploring bulk image input for rapid scaling followed by human review.
- Workflow: Georgemaine owns template blocks and design system, Nicolas owns pipeline/gallery production and technical implementation, George owns strategy and Lovable client relationship.
- SEO foundation: George provided data-driven Airtable with 5,000+ competitor URLs, keyword research, search volume, and difficulty scores across template categories.
- Technical blockers: Nico resolving guide section deployment issue; assessing Remix feature and prompt-box implementation needs; evaluating static MD files vs. database for SEO strategy.

---

## Key Topics

### Template Strategy and Prioritization

  - George shared Airtable with 5,000+ competitor URLs, keywords, search volume, and difficulty
  - Portfolio websites identified as high-priority due to search volume
  - Team to break down broad categories (e.g., portfolio) into specific types (photography, artist, etc.)
  - George to provide more detailed list of template categories to target next

### Template Development Workflow

  - Georgemaine focusing on getting template blocks right
  - Successfully used Claude AI to generate design from screenshots consistently
  - Exploring methods to scale template creation:
    1.  Feeding URLs of live pages (limited by URL availability)
    2.  Bulk image input for rapid template generation, followed by human review

### Launch Strategy and Minimum Viable Product

  - Aiming for progressive launch rather than big launch
  - Discussed minimum template library for launch (\~50 templates suggested)
  - Need to define features required for each template category (e.g., author page, blog post page for blogs)
  - Plan to emulate best examples from competitors like Webflow

### Technical Considerations

  - Nico working on resolving deployment issues for guide section
  - Exploring Remix feature implementation; may need Lovable team's input
  - Considering adding a prompt box for direct template remixing
  - Evaluating need for database vs. static MD files for SEO strategy

### Design and Content

  - All designs cleared NAD's comments
  - "About This Template" section content still to be determined; not blocking progress

### SEO and Sitemap

  - George shared sitemap for Lovable with Nico
  - Nico to sync with Kirkland and potentially Forkhan on sitemap updates

---

## Action Items

**Nicolas Castellanos (GrowthX)**
- Resolve guide preview deploy issue w/ Forkhan; then send article batch to George Haikal
- Sync w/ Kirkland & Forkhan re: sitemap updates
- Test Remix on preview; then assess prompt-box need and report to George Haikal

**George Haikal (GrowthX)**
- Flesh out Airtable template strategy w/ Lovable mini-apps; then share w/ Georgemaine & Nico
- Define bare-minimum template library launch experience; then share w/ Nico & Georgemaine
- Confirm progressive launch approach w/ Lovable; then update Nico

**Georgemaine Lourens (GrowthX)**
- Compile per-category feature lists + Webflow examples; then share w/ Nico & George Haikal

---

## Transcript
**Georgemaine Lourens:** Hello?

**Nicolas Castellanos:** Hey, I'm here.

**Georgemaine Lourens:** Okay, cool. Maybe we can ping George. All right, let's give him another minute. He's probably still in his last meeting. Yeah, he's booked as hell.

**Nicolas Castellanos:** Yep.

**Georgemaine Lourens:** Are you feeling better or still?

**Nicolas Castellanos:** No, I'm on painkillers, so yeah, I'm fine.

**Georgemaine Lourens:** Painkillers? Drugged up. Yeah.

**George Haikal:** Hey, guys.

**Nicolas Castellanos:** Sorry about that.

**Georgemaine Lourens:** Hey.

**George Haikal:** No worries. How's it going?

**Georgemaine Lourens:** Good.

**George Haikal:** Good, man. Doing well. Busy morning.

**Georgemaine Lourens:** I can imagine. Do you want to jump right into it?

**George Haikal:** Yeah, let's do it.

**George Haikal:** There's Slack right now.

**Georgemaine Lourens:** Okay. Maybe I can start. So I have two things. My main focus for this week is going to be the templates workflow.

**Georgemaine Lourens:** I'm going to focus on getting the blocks right first, unless you already kind of figured out the template strategy, and then maybe we can focus on the ones that we want to attack first.

**Georgemaine Lourens:** But I'm fine with sticking to blocks.

**Georgemaine Lourens:** And this morning, I spent a lot of time trying to get Claude to get the design from a screenshot and nail that and lovable.

**Georgemaine Lourens:** After a couple of tries, I got it to do that really consistently.

**Georgemaine Lourens:** But the challenge with that is that I kind of fed it like individual screenshots of UI elements that belong to the design system.

**Georgemaine Lourens:** And while that works really well, we kind of need to figure out a way to...

**Georgemaine Lourens:** But Nico had a couple of ideas.

**Georgemaine Lourens:** So one was kind of like feeding it a URL of a live page.

**Georgemaine Lourens:** But the downside of that, obviously, is that you need URLs, and you might not always have that.

**Georgemaine Lourens:** And the other way was just testing how we could just kind of like feed it a bunch of images, and then it just rapid fires a lot of templates.

**Georgemaine Lourens:** And then a human just kind of has to review a bunch of like 100 or something and kind of like figure out the right ones.

**Georgemaine Lourens:** So that is my focus for the next coming days.

**Georgemaine Lourens:** And another note, I need to help out on the SentinelOne database site, but that should only take like a morning.

**Georgemaine Lourens:** But I have tomorrow morning blocked for that.

**Georgemaine Lourens:** And that is it on my end.

**George Haikal:** Great. Wi-Fi cut out for a bit of that, but basically it's working on the template workflows so that we're able to do them at scale.

**Georgemaine Lourens:** Yeah, exactly.

**Nicolas Castellanos:** On my end, basically supporting that, planning to have Pipeline doing that by Friday.

**Nicolas Castellanos:** We can probably get that sooner.

**Nicolas Castellanos:** And then have some questions for you, whether it makes sense or not to get the gallery production ready now, or if it makes more sense to have, like, to work on templates.

**George Haikal:** Got it.

**George Haikal:** Okay.

**George Haikal:** So, a few things.

**George Haikal:** The first of, like, we're sticking to the goals, right?

**George Haikal:** Let me check.

**George Haikal:** Is there anything published on their guide section right now?

**Nicolas Castellanos:** Not yet.

**Nicolas Castellanos:** I'm working.

**Nicolas Castellanos:** I'm sure that I just got an answer from Forkank, he sent some logs trying to figure out why it's not deploying on the preview app.

**Nicolas Castellanos:** It was before.

**Nicolas Castellanos:** I don't know what's causing it not to right now.

**George Haikal:** Okay, so there's like a tiny issue with the deploy and so like before the meeting.

**Nicolas Castellanos:** Yeah, once that's up, they should be able to see it.

**Nicolas Castellanos:** It was working on like Thursday.

**Nicolas Castellanos:** I don't know what's going on now, but yeah, I'll actually be able to resolve this faster now I got the logs.

**George Haikal:** No problem.

**George Haikal:** That's perfect.

**George Haikal:** And then we'll just keep sending or we'll send you like a batch of articles like when they're next already, just so it's easier for you.

**George Haikal:** you don't have to get back and forth.

**George Haikal:** Okay, on the templates, let's see here.

**George Haikal:** Let me show you guys what we did quickly. It will help add some clarity to everything.

**George Haikal:** So, can you guys see the Airtable?

**Nicolas Castellanos:** Yes.

**George Haikal:** Cool.

**George Haikal:** So this is for templates specifically.

**George Haikal:** Basically, what we did here was take a ton of good inspiration from, you can see there's like 5,000 different competitor URLs from people doing it well, Wix, Webflow, etc.

**George Haikal:** Got all the keywords, did some research, enriched it, and basically boiled down all of the keywords, the potential search volume, the actual difficulty, where the URLs were from, and then the intent, and then came up with general tags, right?

**George Haikal:** Which are essentially categories, template categories.

**George Haikal:** Yeah.

**George Haikal:** So that's organized by total volume.

**George Haikal:** I was hoping this makes it a little clearer for you, Georgemaine, of like, where we should be prioritizing next, like the next set up.

**George Haikal:** Of template categories based on like real information.

**George Haikal:** And so I'm going to keep adding to the list, but this is why we started with Portfolio websites in the beginning, right?

**George Haikal:** websites in general, because there's just a ton of low-hanging fruit on the search volume front.

**George Haikal:** And then I'm going to break this down a little more specifically into like, because right now there's really not many mini-apps or things that are more related to lovable.

**George Haikal:** So I'm going to finish fleshing that out, but it's a good starting point for like us to talk through with the client on Wednesday.

**George Haikal:** And then us to root all the work we're doing into something real, like real numbers.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** So it kind of seems like Portfolio is the first place to start, but it's also, it's very broad, right?

**Georgemaine Lourens:** So how do we, how

**Georgemaine Lourens:** How we kind of like fill that in?

**Georgemaine Lourens:** we just kind of like, like my first instinct would be either we combine it with some of the, some of the keywords that we already have, or we just kind of look at the examples that you shared and just kind of try to go for those that are on their listing.

**George Haikal:** Yeah, I think the next step of this is break, is like exactly what you're saying, breaking this up into like, all right, like what types of different portfolio websites.

**Georgemaine Lourens:** are in there, like this is already showing like, you know, an agency website template.

**Georgemaine Lourens:** Oh, there's more, oh, nice.

**George Haikal:** Yeah, well, it's all a roll-up of all the different URLs, like this, this category is just a summary of all of these.

**George Haikal:** Photography portfolio, you know, artist, so.

**Nicolas Castellanos:** Let's meet up.

**George Haikal:** Yeah, I know, right, what?

**George Haikal:** Got to see where this one is.

**Nicolas Castellanos:** Oh, cool.

**Nicolas Castellanos:** Great.

**Georgemaine Lourens:** Yeah, don't worry about it.

**Nicolas Castellanos:** Oh, AWS is down.

**George Haikal:** Cool.

**George Haikal:** Okay, so, like, a more helpful starting point in, like, next list of templates to target is what I'm hearing, right?

**Georgemaine Lourens:** Yeah, I think if you're going to review this with Lovable on Wednesday, then I think the best way forward for us is to just focus on the template pipeline using the templates we're focusing on right now.

**Georgemaine Lourens:** And then as soon as you and the client agree on the ones that you want to attack, we can switch to that and go from there.

**Georgemaine Lourens:** But another question that me and Nico had was, like, what is the bare minimum template library launch experience?

**Georgemaine Lourens:** Because I can imagine that you would want, like, at least a certain amount of templates on there or a certain amount of categories, but it might be worth to think about that in advance.

**Georgemaine Lourens:** And like in the past, I've launched galleries with, like, around 50-ish templates, but that's not a lot of categories, but it's decent.

**Georgemaine Lourens:** But I'm not sure what the agreement here is.

**Georgemaine Lourens:** Because when you get some time to think about it, let me know.

**George Haikal:** That's good.

**George Haikal:** I'm that down right now.

**George Haikal:** Okay, that makes sense.

**George Haikal:** So right now, yeah, go ahead, Nico.

**Nicolas Castellanos:** Yeah, and then the other thing we need is to figure out that, like, what a template of each of those categories look like in terms of, like, the features in them.

**Nicolas Castellanos:** Like, for blogs, you need, like, I don't know, an author page, the blog post page, the index page.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Registration, but how does it look for, like, portfolios, agency sites?

**Nicolas Castellanos:** Like, if we can get, like, a list of features that are a must for those kind of categories, that will be great to just give, like, specific directions to the pipeline to build them.

**Georgemaine Lourens:** Yeah, I can do that. I can look at examples of what great looks like.

**George Haikal:** Exactly. And then emulating it, right?

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Yeah, now you showed that, all that, that was our table.

**Nicolas Castellanos:** I'm thinking if it makes sense, just trying to replicate, like, those best results you find right now in Webflow for those search intents, and basically replicate what they have in there in terms of features.

**Nicolas Castellanos:** There's, like, the best 10 Webflow templates for those search.

**Georgemaine Lourens:** Yeah.

**George Haikal:** Yeah, yeah, I don't think we have to reinvent the wheel.

**George Haikal:** It's more, yeah, like, whatever looks good, and you guys are comfortable with, and you think, like, it looks great, and it's easy to reproduce.

**George Haikal:** Then we're happy with, for sure.

**Georgemaine Lourens:** Cool.

**George Haikal:** Cool.

**George Haikal:** Just saying something.

**George Haikal:** Okay.

**George Haikal:** Okay.

**Georgemaine Lourens:** And what is your plan for Wednesday?

**Georgemaine Lourens:** Like, what would you ideally want to share?

**George Haikal:** Yeah, so the fleshed out template strategy, having some, like, five or so blogs already published.

**George Haikal:** Oh, the other thing, Nico, is I sent a Slack to you in Kirkland on the sitemap for Lovable.

**Nicolas Castellanos:** I saw it. Yeah, still need to sync with him.

**George Haikal:** Yeah.

**Nicolas Castellanos:** I'll sync with him and with Forkhan, who might know how to update the sitemap.

**Nicolas Castellanos:** Because I don't know if this will update it.

**Nicolas Castellanos:** I don't think so.

**George Haikal:** Okay.

**George Haikal:** Yeah, yeah, so that would be awesome to get ahead of it.

**George Haikal:** And then, is there anything we're missing with, like, that you all need?

**George Haikal:** Maybe, so say we have five templates ready.

**George Haikal:** Okay.

**George Haikal:** There's things on, like, the Remix feature.

**George Haikal:** Like, is there anything that isn't going to work that's on the template now that you need their team for?

**Nicolas Castellanos:** Yeah, for that, we will need them.

**Nicolas Castellanos:** Ideally, I can take a look at how the Remix feature is working, like, on production on their site.

**Nicolas Castellanos:** Build it and test it on the preview link.

**Nicolas Castellanos:** That might work.

**Nicolas Castellanos:** Then we have, this can be for the future, but we have an idea of having, like, a prompt box.

**Nicolas Castellanos:** So you can just directly, like, Remix it in the template page.

**Nicolas Castellanos:** For that, we will need them.

**Nicolas Castellanos:** Again, I can probably try to take a look at how that is being done and replicated.

**Nicolas Castellanos:** Apart from that, depending on the SEO strategy, I might find that we need to build something out database-wise.

**Nicolas Castellanos:** I don't think so, because right now, the plan is to build everything.

**Nicolas Castellanos:** on MD files, and all that data can be static on the pages, but yeah, I'll take a look at that.

**George Haikal:** Okay, so what do you need from them to help?

**Nicolas Castellanos:** If we need a database, then a database, somewhere where we can record stuff and make queries to.

**Nicolas Castellanos:** If not, then just the prompt thing, which I'll test today and make sure if we need anything from them.

**George Haikal:** Okay, so okay, nothing from them now.

**Nicolas Castellanos:** Yeah, no, right now I need to check both things.

**George Haikal:** Okay.

**George Haikal:** Cool, I'm checking one more area quick, which is the motion.

**George Haikal:** And I'm doing more work on them this afternoon, so we'll be in a good spot, but all the designs.

**George Haikal:** Stuff was good, cleared all NAD's comments, right?

**Georgemaine Lourens:** Yep.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think the only design piece that's still open is what we put in the About This Template section.

**Georgemaine Lourens:** I think that might be part of the SEO strategy, but I'm not sure what that's supposed to be.

**Georgemaine Lourens:** I just marked it up with random data.

**Georgemaine Lourens:** I think it's fine for now, but I don't know what we want to do there.

**Georgemaine Lourens:** Like, should it be Getting Started section?

**Georgemaine Lourens:** Should it be About This Template?

**Georgemaine Lourens:** I think we, I'm not sure what the process here is.

**Georgemaine Lourens:** I can work together with Ada if that is the best way forward.

**Georgemaine Lourens:** Or maybe Marcel wants to think about it himself first.

**Georgemaine Lourens:** I don't know.

**Georgemaine Lourens:** Or it's something that you might want to tackle during the SEO strategy.

**George Haikal:** Yeah.

**George Haikal:** Let me think about it.

**George Haikal:** Well, right now it's not like the most, like it's not.

**George Haikal:** Blocking anything.

**George Haikal:** it's fine.

**George Haikal:** But yeah, we definitely will want to make it better.

**George Haikal:** we'll loop Ada in once there's a little more structure.

**George Haikal:** And like we have a list that she can like, go down and execute on.

**George Haikal:** it's easy for her to work off of.

**George Haikal:** But that's makes sense to stay on top of.

**George Haikal:** Okay, cool.

**George Haikal:** Blogs seems unblocked.

**George Haikal:** Templates, we're in a good spot.

**George Haikal:** So Georgemaine by Wednesday, by the meeting, like, do you think we'll be in a spot where we can say, hey, we have these X number of templates ready to go?

**Georgemaine Lourens:** Yeah, you mentioned five, right?

**George Haikal:** Yeah, whatever number you're most comfortable with.

**George Haikal:** And then the other thing there is like getting the slash templates page live as well, right?

**Georgemaine Lourens:** Yeah, Nico is gonna take care of that because I fixed most of the bugs. It just needs to be production-ready. And yeah, I think five templates or more by Wednesday should be good. You'll know by tomorrow end of day what I have ready.

**George Haikal:** So you have the more accurate number.

**George Haikal:** Yeah, no, that's perfect.

**George Haikal:** Yeah, I mean, I don't want to press you too hard on it, like whatever number you're fine with, because we're going to expand into different categories as well.

**George Haikal:** So it's not like we need 50 of the newsletter publication blog style ones, like the ones you already have are great.

**George Haikal:** So if they're ready and cleared of bugs, like it's a good starting point, because then we need to work towards like what we need for launch, which is good.

**Nicolas Castellanos:** So what I'm hearing is we're thinking this as a progressive launch, not a big launch. I'll confirm that with them. I think it would take too long to make it a big launch.

**George Haikal:** Yeah, that's my thought. I'll confirm with them. They want to solve for speed too.

**Nicolas Castellanos:** Great.

**George Haikal:** Cool, I'm pretty clear on everything.

**George Haikal:** Is there anything that's still unclear or in the way?

**Nicolas Castellanos:** No, pretty clear.

**George Haikal:** Thanks, guys. We'll talk soon. Let me know if anything comes up in the meantime.

**Georgemaine Lourens:** Will do. See you guys later.

**George Haikal:** Have a great start of your week.

**Nicolas Castellanos:** Bye.
