# Marcel <> Daniel

<metadata>
date: 2026-02-23
time: 19:57 UTC
duration: 32 minutes
source: fireflies
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    role: Founder & CEO, GrowthX
    email: marcel@growthxlabs.com
  - name: Daniel Lopes
    role: CTO, GrowthX
    email: daniel@growthxlabs.com
fireflies_id: 01KJ61874JJZWXMZAYGQQZ27CK
transcript_url: https://app.fireflies.ai/view/01KJ61874JJZWXMZAYGQQZ27CK
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Marcel and Daniel aligned on accelerating CheckThat's UI development by bringing Esteban (designer/developer) onsite for a month to iterate on static data, with target launch by March 17. They mapped integration between CheckThat and OS: automating workspace creation via API, using a reputation-based vendor shortlist (filtered through Gartner/G2/Forrester analyst reviews) to pre-populate competitor data and eliminate manual pre-sales research, and standardizing the audit report as a shared asset for both platforms.

---

## Context

Marcel has invested over 200 hours on CheckThat in the past 30 days, with 100+ hours spent on UI code that distracted from core product development. The meeting focuses on three urgent priorities: (1) UI/UX refinement for CheckThat's three key outputs (public pages, authenticated user experience, and audit report), (2) documenting OS feature scope for mid-March launch, and (3) linking CheckThat and OS workflows to eliminate redundant research in sales and delivery. Daniel is unavailable March 9–16 due to personal commitments and needs the team to reach feature completion and QA by that date.

---

## Relevance

**CheckThat (AI Visibility Software)**
- Finalizing presence, reputation, and influence scoring methodology with real data validation
- Building three primary UI outputs: public profiles, authenticated experience, and audit/grading interface
- Creating static-data UI mockups before backend integration to validate UX with live data later

**OS (Site Audit & Crawler)**
- Planning two-week feature completion sprint, QA phase during Daniel's absence (March 9–16)
- Integrating three-layer crawler: sitemap discovery → health check → multi-tier SEO analysis
- Coordinating with CheckThat via API to automate workspace setup and pre-populate competitor research

**Sales & Delivery**
- Eliminating repetitive pre-sales research bottleneck by pre-computing CheckThat profiles for competitor categories
- Using reputation-filtered vendor lists (Gartner/G2/Forrester leaders) to auto-trigger workspace creation and deep research
- Delivering audit reports as shared asset across both products and sales process

**Product Documentation & Knowledge**
- Creating in-codebase product guides and tutorials to enable AI agents to learn product behavior in parallel with development
- Updating handbook with methodology and thinking as products evolve (reducing outdated context debt)
- Planning feature-complete documentation and enablement materials by March 17 launch

---

## Decisions & Commitments

1. **Bring Esteban onsite ASAP** for one month to do rapid UI/UX iteration on CheckThat with Marcel, focusing on static data first
2. **Feature-complete timeline for OS**: Next two weeks (through March 9), then QA/bug fixes March 9–16, launch by March 17
3. **CheckThat audit report** becomes the primary launch feature—nail all screens for the report area before adding other features
4. **API integration between CheckThat and OS**: Workspace creation in OS will trigger CheckThat profile creation and crawler setup via API
5. **Pre-sales workspace flag** in CheckThat to streamline non-production research workspaces and eliminate manual setup
6. **Vendor shortlist methodology**: Use top 25–50 brands from Gartner/Forrester/G2/Trust Radius magic quadrants to auto-populate competitor lists (no human approval needed for analyst-vetted vendors)
7. **Documentation-first approach**: In-codebase product guides linked to code, updated during feature development, not after

---

## Open Questions

- How will API authentication work between CheckThat and OS for automated workspace and crawler triggering?
- Should the pre-sales workspace flag appear in the OS interface, or remain hidden from end users?
- How will CheckThat scoring handle companies with <0.1% visibility (Esteban example)—the tiered modifier approach prevents 100 score, but is it intuitive to users?
- When will Jose and Pedro (backend team) be available to design the architecture for CheckThat data querying and OS analytics integration?
- Should the audit report support both CheckThat-branded and GrowthX-branded versions, or standardize to one?

---

## Overview & Key Topics

- **UI/UX Development**: Esteban onsite for static-data UI mockups; focus on report area for March launch
- **CheckThat Scoring**: Presence, reputation, influence methodology; tiered modifiers to prevent artificial 100 score
- **OS Feature Scope**: Feature completion by March 9, QA by March 16, launch March 17; three-layer crawler system
- **CheckThat + OS Integration**: API-driven workspace creation, shared audit report, auto-triggered competitor research
- **Sales Efficiency**: Eliminate manual pre-sales research by pre-computing CheckThat profiles; use analyst-vetted vendor lists
- **Documentation Strategy**: In-codebase product guides updated during development; handbook as single source of truth
- **Product Architecture**: Jupyter notebook for data validation; render MCP for direct data querying; git submodule for docs sync

---

## Action Items

**Marcel Santilli**
- Confirm Esteban's start date and green-light his onboarding for one-month UI collaboration
- Continue refining presence, reputation, and influence scoring with real data validation using Jupyter notebook
- Update GrowthX handbook with CheckThat methodology (presence, reputation, influence, shortcut recommendation paths)
- Coordinate static-data UI development with Esteban; prepare second and third brands for sequential validation after CheckThat report UI ships
- Document data querying approach and write guide for render MCP before involving backend team

**Daniel Lopes**
- Facilitate Esteban's onboarding ASAP
- Drive OS feature completion by March 9 (coordinate with Jakob on analytics, Brad on three-layer crawler)
- Oversee QA onboarding and documentation creation for feature-complete launch scope by March 17
- Design API integration between CheckThat and OS (workspace creation, site audit, competitor list auto-population)
- Implement pre-sales workspace flag in CheckThat to streamline non-production research workspaces

---

## Transcript

**Marcel Santilli:** So what I was thinking is to get your approval and alignment to bring Esteban. He said he's down for it for like a month or whatever, and just have him sitting next to me. I've spent over 200 hours on CheckThat in the last 30 days, and at least a hundred of those are UI coding things that weren't me connecting the dots. By having Esteban here, we can do a few half days and full days of iterating quickly.

**Daniel Lopes:** Yeah, yeah.

**Marcel Santilli:** The way to think about Esteban is he's a designer that can code. He's a worse designer than most designers, but he's a better programmer than most designers.

**Daniel Lopes:** Yeah, let's do that. Makes a lot of sense.

**Marcel Santilli:** In my mind, there's three potential outputs. One is the public pages. Another is the authenticated user experience. And then another is like the equivalent of an audit or grader. This one can be effectively the same for when we kick off an engagement as well as for CheckThat.

**Daniel Lopes:** Yeah, right, right.

**Marcel Santilli:** The report is the easiest to do and will help validate. I took the MD files from all my outputs and created a quick report to visualize it better. It had competitive landscape with an audit and competitive SEO analysis. This part is really cool because it looks at all their competitors by authority, keywords ranked, traffic value, backlinks, content pages and traffic per page.

**Daniel Lopes:** Yeah, yeah, yeah. I need to look at this. This is overlap because what we're building now, literally the three areas of OS is Jakob sprinting through revamping analytics collection, and Brad is building the crawler in a three-layer system. First layer is sitemap discovery. Second is basic crawl that gets meta tags to see which are live, 404, or redirect. Third is multi-tier analysis with health check using SEO data instead of Lighthouse.

**Marcel Santilli:** This is based on URLs and slugs using Semrush MCP servers. The idea was suggesting clusters without prescribing how to do it—giving value without assigning work.

**Daniel Lopes:** Very interesting.

**Marcel Santilli:** I created a new version asking how would you reimagine this app versus refactoring CheckThat. It's how would you approach it with our new methodology. You have presence score, reputation (overall reputation, reviews, community authority, analyst coverage, community signals), then perception (score over time, ranking by attribute and engine), and influence score.

**Daniel Lopes:** How did you get all this data into this app?

**Marcel Santilli:** A deep researcher came up with this, influenced by CheckThat data. I set up the render MCP—Jose gave me that tip. So I can essentially query the data directly.

**Daniel Lopes:** That's so scary. Make sure there's no deletion or write back.

**Marcel Santilli:** I'm writing a guide on how I was planning to do it first.

**Daniel Lopes:** I think the ideal setup would be to fly out Esteban, have him work with you, and get the UI as close as possible focused on static data in the app. Not query one-off if needed.

**Marcel Santilli:** Yeah, exactly. Query one-off for only one brand. We're like, cool, this looks great. Now a second brand. By the third, we're confident. Then we can make it so the deep researcher queries things that should be from a public page.

**Daniel Lopes:** If he could come ASAP and you guys finish the UI as close as possible but static, then you can bring in Jose to think about the architecture. Jacob was thinking about ClickHouse analytics data and high-volume metrics from OS. That overlaps with the architecture here. They can shape the technical side. If Esteban was here already, I could see that being two weeks on this—you two working together. Then second half March is turning that into reality with Jose and Pedro.

**Marcel Santilli:** Yeah, exactly. He said he's available. I checked with him. He's available if needed. I can tell him to give him the green light.

**Daniel Lopes:** Make sense.

**Marcel Santilli:** I modified the presence rate today because it was too heavily weighted toward visibility quality. Now the next stage is focusing on querying data, assigning scores, and seeing if it makes sense with real data.

**Daniel Lopes:** That can even be like a Jupyter notebook for you to query this stuff and validate formulas while he's doing the UI.

**Marcel Santilli:** Yeah. I modified presence rates. I don't think this makes sense. When I did the UI for the audit, presence rates were too high. Eon has 0.1% visibility, so a 30 score out of 100 makes no sense. I came up with tweaks—different tiers and modifiers so it's effectively impossible to hit 100. To be 100, it's like reaching AGI. There's always a gap to fill.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** It's getting to the same place we got with OS. Low presence plus low influence means AI has no material from you—establish source from scratch. High reputation plus low presence—okay, cool. Those are shortcut paths to recommend something.

**Daniel Lopes:** That makes a lot of sense.

**Marcel Santilli:** Let me update the handbook with this. There's energy that happens when you put something there. When the grid looks good, I'm like, yes, okay cool. This is awesome. This is going to work.

**Daniel Lopes:** Yeah, yeah, yeah. I know exactly what you mean. Words and fat marker stuff make me less anxious. Still anxious until I see all the screens.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Where we are with OS, I think we need to get to that stage. You've progressed enough on words. If we can get all the screens, or at least all screens for one area—just pick the report and do all those screens. The feature we launch is this report area.

**Marcel Santilli:** I highly recommend updating the handbook with how your thinking evolves. Everything is here. At any point, you want to use it—it's all here. The latest and greatest.

**Daniel Lopes:** Yeah, I need to do that. I do something similar in the project folder, but this is a good idea. I put it on the agenda for today. Second half of this month once we get past feature completion. The OS timeline is this week and next, working hard to get to QA stage by the ninth. We onboard QA and beta—Whedon and whoever can test. During that week, we create guides for how to use the product in the code: here's how this screen works, high level.

**Marcel Santilli:** That's why I created guides and tutorials. If it's internal, we can use this. I create a section or tab. We can do product tabs as well.

**Daniel Lopes:** The value of being in the codebase is that agents can read it while you're coding, and vice versa—you create pages fast by reversing the code.

**Marcel Santilli:** That's one restriction we have. I effectively do the same, but the trade-off of having it locally is then any time I need that context for anything else, it becomes harder. I run it as a workspace parallel folder.

**Daniel Lopes:** But you can't do CI. We shouldn't launch a large feature without docs. We can reinforce things on the output, but you can tie the whole thing together.

**Marcel Santilli:** Is there a way to do a symlink or something close—where it's in both places, but any time a push happens to one, it syncs to the other?

**Daniel Lopes:** You can do a git submodule. It's a bit of a hassle, but the docs become their own repo. You can send link as well.

**Marcel Santilli:** Right now it's like I had docs in context one. Now that I'm making docs in the handbook better, I almost never reference my context docs because they're so outdated. It would take a thousand dollars worth of credits to make them better.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** The handbook is the most thought through. Regardless, I think it would be helpful for me to convert the OS things we've discussed into docs. If we had the equivalent of what I have for CheckThat for OS, or if you point me in the right direction, I can help.

**Daniel Lopes:** I think that should be done when we make all the features. Demo what is feature complete, what's not in scope. What's there is the training for how to learn. For someone like William, this doesn't need a lot of training. But everyone else needs training, so it has to be really enablement material.

**Marcel Santilli:** It's almost like methodology, because we have too many things to read. People don't read.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** That's true. I use this like quick context—everything. So I don't have to explain what an opportunity is. It shortcuts things. But having this already explained helps. I took it from your doc.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** The product ecosystem helps a lot. Understanding—yeah, we'll figure it out.

**Daniel Lopes:** A big part of the second half of the month is once we lock in all the features. There's still some features to define—how can we ship this in two weeks? The way I'm thinking: next two weeks get to feature complete. Whatever I don't finish—I'm off from the ninth to sixteenth because of my parents—during that week it's QA bug fixes. When I come back, it's William. Beta team starts and documentation. That week we launch the output. The guys are finishing features that weren't possible before until the foundation—replacing Langviews and Galileo became possible because of this infrastructure. I want those features in the launch. So they're clear: oh wow, this is not possible before. They're finishing this week. Next week QA and polish. Then one week where I'm out to do whatever's left, then announcement on the seventeenth. Both products will be in a good spot the week of the fifteenth.

**Marcel Santilli:** Okay, I think that sounds good. How should I think about this? In my mind, it's like a subset of CheckThat in the public pages plus a subset of OS is what we use in both as an audit. It'll accelerate efficiency. Most inefficiency in both our sales process and first two weeks of a sprint is: go research them, go research their space, go research all the competitors.

**Daniel Lopes:** OS needs to do it as part of workspace calibration. It's the setup phase. That's the workflow for opportunity finding.

**Marcel Santilli:** You definitely need to do it as part of setup. But we do it no matter what in sales. We need a version of it for CheckThat. For instance, right now, Corelogix—the deal is stuck. Had I done a quick process just showing their gap, it would move more.

**Daniel Lopes:** I think the audit is... we talked about that with the team last week. We have on-page health stuff that data for SEO gives us. We can do about five dollars for ten thousand pages. Then site-wide things we'd need anyway. We could expose those as consumable things.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Integrate both.

**Marcel Santilli:** Exactly. Imagine sending a version of this during sales. But parts are like Crunchbase—there are locks everywhere. Or cleaner. But as much as possible, it's public CheckThat pages so we don't have to do deep research from scratch on every brand. If you've already mapped the whole category, done reputation analysis, overall brand context on every player, have their AI visibility computed—we're doing that. Then we do a quick audit on a few more things and present mostly that information.

**Daniel Lopes:** Yeah. I don't see why we wouldn't be able to—if you have a sales lead, you go into CheckThat, create a workspace. Go into OS, create a workspace, then let that trigger the site audit and basic crawler and sitemap discovery. Do the same on CheckThat to find all visibility and things. One calls the other as an API.

**Marcel Santilli:** Yeah, okay. Because these audit pages can be CheckThat-branded or GrowthX-branded. It's just swapping the logo and where you host it. Effectively it's the same thing.

**Daniel Lopes:** Yeah. And if you do that—let's say CheckThat wants to generate these pages. Like, we want those audit pages as a magic link inside CheckThat that a salesperson can send around. If we have an API that requires doing something on OS to render that, that's possible.

**Marcel Santilli:** So do we need to create a workspace? What I'm noticing with CheckThat is I have to create the workspace. I'm creating a bunch of workspaces. They're not really effectively workspaces. It's me running these processes, which is fine, but it's almost like a pre-stage workspace.

**Daniel Lopes:** Yeah, we can shortcut that. We can have a pre-sales workspace flag or something that doesn't show up in the grid. It's just used for doing site audits. Pretty straightforward. Could even create on the fly.

**Marcel Santilli:** Because CheckThat has more dependencies on having to run things. But were you imagining that? So let's imagine a legit brand like Corelogix—they're legit. Or Eon, which just raised 127 million—they're legit. They need help. But we don't know if they're a free user, CheckThat user, or GrowthX client. They come in inbound, warm and legit. Do you imagine automatically trigger, which one creates first—CheckThat account or OS account?

**Daniel Lopes:** Yeah, CheckThat makes a lot of sense because CheckThat runs a bunch of research and creates articles first. OS has a prerequisite to run after.

**Marcel Santilli:** And then OS is all about auditing their website.

**Daniel Lopes:** Yeah, ideally every company on OS has a CheckThat profile so we don't have to do all this heavy lifting of reputation and competitor stuff.

**Marcel Santilli:** The ideal process is we're computing the workspace and CheckThat has to be created to do certain things. Let's pick a category. This category has fifty players. Make sure those fifty profiles are created and tracked.

**Daniel Lopes:** The competitors I added to the workspace. Now workspace setup on OS is hardcoded because I was expecting to hit an API on CheckThat and pull from there. One of the setup steps should be create a CheckThat profile.

**Marcel Santilli:** The way I was doing here is interesting—use reputation to create a short list of twenty-five to fifty, the ones Gartner and G2 rate highest. It's a combination of all of them. You have the entire audience, then the short list—ones that have shown up and have legit reputation.

**Daniel Lopes:** Yeah, like, it's essentially fifty of these, right? Where they show up as a leader in the magic quadrant.

**Marcel Santilli:** Exactly. Some spaces call it one thing, others another—cloud native storage versus data center backup versus enterprise backup. They're effectively similar. Our version of how we categorize will evolve. Our version is like data and backup or something.

**Daniel Lopes:** Right, right.

**Marcel Santilli:** This creates a really good short list of legit companies. That's the short list that for sure should be mapped, should have deep research, should be analyzed. If Gartner put an analyst on a vendor and that analyst talked to over twenty customers, they have over X amount of revenue, they're as legit as it gets. You should know them.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Between Gartner, Forrester, peer reviews—mostly G2, Trust Radius, Giga Ohm—you get to top twenty-five to fifty legitimately reviewed ones. Those for sure we trigger. No human approval needed.

**Daniel Lopes:** Yeah, it makes sense.

**Marcel Santilli:** And for OS setup, hopefully we can just pull from that.

**Daniel Lopes:** From that. Yeah, we can pull from. Yep.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Okay, cool. All right. I'm gonna work on some.

**Marcel Santilli:** All right, man. Sounds good. I'll let Esteban know, and then I'll keep you posted.

**Daniel Lopes:** Sounds good. Yeah, whenever the sooner he can come, the better.

**Marcel Santilli:** Yeah. I told him let's go.
