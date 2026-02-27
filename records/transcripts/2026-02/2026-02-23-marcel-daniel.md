# Marcel <> Daniel

<metadata>
date: 2026-02-23
time: 19:57 UTC
duration: 32 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Daniel Lopes
fireflies_id: 01KJ61874JJZWXMZAYGQQZ27CK
transcript_url: https://app.fireflies.ai/view/01KJ61874JJZWXMZAYGQQZ27CK
</metadata>

---

## Summary

Marcel and Daniel discussed refining CheckThat's UI and scoring methodology with Esteban's support for rapid iteration. The team plans to bring Esteban onsite for approximately a month to accelerate UI development while working with static data first, with a targeted feature freeze and launch by mid-March. They aligned on integrating CheckThat and OS workflows, automating workspace creation with pre-sales flagging, and using a reputation-based vendor shortlist from analyst reviews to guide deep research and competitive analysis.

---

## Action Items

**Marcel Santilli**
- Confirm and communicate Esteban's start date for UI collaboration upon Daniel's approval
- Continue refining presence, reputation, and influence scoring methodology with real data validation
- Update and maintain internal documentation for CheckThat and OS integration and workflows
- Coordinate data querying approach with backend team while Esteban focuses on UI design

**Daniel Lopes**
- Facilitate Esteban's onboarding ASAP to start UI development with static data
- Oversee QA onboarding and documentation creation for OS feature freeze with target launch around March 17th
- Support architecture and analytics integration between OS and CheckThat with backend team
- Implement API workflows to automate workspace creation and site audits between CheckThat and OS platforms

---

## Transcript

**Marcel Santilli:** Link, copy, invite, link.

**Daniel Lopes:** This meeting is being recorded.

**Marcel Santilli:** And then you go into Fireflies and you go capture and then paste the link here and then put like, whatever the title is and says, start capturing and then approve it to get in.

**Daniel Lopes:** Oh, nice.

**Marcel Santilli:** But it's like a bit of a pain, you know, when it's an ad hoc meeting. It doesn't have any triggers to auto join.

**Daniel Lopes:** Yeah, they don't have a local app.

**Marcel Santilli:** So what I was thinking is to get your approval and alignment to bring Esteban. He said he's down for it for like a month or whatever and just have him sitting next to me. I've spent over 200 hours on CheckThat in the last 30ish days, and at least a hundred of those are UI coding things that weren't me connecting the dots. By having Esteban here, we can do a few half days and full days of iterating quickly.

**Daniel Lopes:** Yeah, yeah.

**Marcel Santilli:** The way to think about Steven is he's a designer that can code. He's a worse designer than most designers, but he's a better programmer than most designers.

**Daniel Lopes:** Yeah, let's do that. Makes a lot of sense.

**Marcel Santilli:** So in my mind, there's three potential outputs here. One output is the public pages. Another output is what the experience for someone signed up and logged in is like. And then another output is like the equivalent of an audit or an AO grader. This one can be effectively the same for when we kick off an engagement as well as for CheckThat.

**Daniel Lopes:** Yeah, right, right.

**Marcel Santilli:** The report is the easiest to do and will help validate. Just to show you, this current version takes a minute to load. But I took the MD files from all my outputs and created a quick report to visualize it better. There's too many tabs, it doesn't fit together. But it had like competitive landscape with a bit of an audit and competitive SEO analysis. This part is really cool because it looks at all their competitors by authority, keywords ranked, traffic value, backlinks, content pages and traffic per page.

**Daniel Lopes:** Yeah, yeah, yeah. I need to look at this. This is overlap because what we're building now, literally the three areas of OS is Jakob is sprinting through revamping the analytics collection of metrics and Brad is building the Crawler in a three layer system. The first layer is just a sitemap finder collecting all URLs. The second is a very basic crawler that hits all pages and gets the meta tags to see which ones are live, 404, or redirect. And then the third is a multi tier analysis with health check using data for SEO instead of Lighthouse.

**Marcel Santilli:** Yeah, yeah. Because this is all based on pretty much just URLs and slugs. This only uses Semrush MCP servers. And the idea here on this section was just like suggesting clusters without giving them how to do it, because ideas are cheap. It's just giving value without actually giving them an assignment.

**Daniel Lopes:** And very interesting.

**Marcel Santilli:** I created a new version asking how would you reimagine this app versus taking CheckThat and going refactor CheckThat. This is more of how would you approach it with our new methodology. And I feel like it's already closer. So you have the presence score, reputation which looks at overall reputation and reviews, community authority, analyst coverage, and community signals. Then perception, which is your perception score over time where you rank in perception and by each attribute by engine. And then influence score.

**Daniel Lopes:** How did you get all this data into this app?

**Marcel Santilli:** This was like a deep researcher coming up with this and this is influenced by CheckThat data. But I set up the render MCP and Jose gave me that tip. So I can essentially query the data directly.

**Daniel Lopes:** That's so scary. Make sure there's no deletion or write back.

**Marcel Santilli:** I'm writing a guide on how I was planning on doing it first.

**Daniel Lopes:** I think the ideal set up here would be to fly out Steven, he works with you on this and get the UI as close as possible focused on static data in the app. Like not query one off if needed.

**Marcel Santilli:** Yeah, exactly. Like query one off for only one brand. And then we're like cool, this looks great. Now let's do a second brand. And by the time we do a third, we're like okay. And then as we identify areas there's like okay, this is great. Then we can try to make it so the deep researcher is querying things that should just be querying from a public page like information it needs.

**Daniel Lopes:** If he could come ASAP, and you guys finish the UI as close as possible but static, then you can bring in Jose to think about the architecture because Jacob was thinking about all the clickhousing analytics data and high volume metrics from OS. That would have overlap with the architecture for this. And then they can shape the technical side. If Stefan was here already, I could see that just being like two weeks on this, you two working together. And then second half March is turning that into reality with Jose and Pedro.

**Marcel Santilli:** Yeah, exactly. So he said he's available, I checked in with him. He's available if needed. So I can tell him to give him the green light.

**Daniel Lopes:** Make sense.

**Marcel Santilli:** I modified the presence rate today because it was too heavily weighted towards visibility quality. I made changes so now the next stage is going to be focusing on querying the data and assigning scores and seeing if it makes sense with actual real data.

**Daniel Lopes:** And that can even be like a Jupyter notebook for you to be querying this stuff and validating the formulas while he's doing the UI.

**Marcel Santilli:** Yeah. For example, I modified presence rates. Like I don't think this makes sense because as I did the UI for the audit, presence rates were too high. Eon has 0.1% visibility so a 30 score out of 100 if they have 0.1% visibility makes no sense. I came up with tweaks where you have different tiers and modifiers so it's effectively impossible to hit 100. That way for you to be 100, it's like reaching AGI. So there's always a gap to fill.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** It's getting to the same place we got to on OS, which is okay, now there's agnostic patterns we can hit. Like low presence plus low influence means AI has no material from you, establish source from scratch. High reputation plus low presence, okay cool. So those are all shortcut paths to recommend something.

**Daniel Lopes:** That makes a lot of sense.

**Marcel Santilli:** Let me update the handbook with this because there's this energy that happens when you put something on there. And when I get the grid to look good, I'm like yes, okay cool. This is awesome. This is going to work.

**Daniel Lopes:** Yeah, yeah, yeah. I know exactly what you mean. Words and fat marker stuff just makes me less anxious. Still anxious until I see all the screens.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Where we are with OS, I think we need to get to that stage. I think you progressed enough on words. If we can get to where we have all the screens, or at least all the screens for one area. If we just pick the report and do all those screens for the report. The feature that we launch is this report area.

**Marcel Santilli:** By the way, I highly recommend as you're building things to update the handbook with how your thinking is evolving. Everything is here, so at any point if you want to use it, it's all here. The latest and greatest.

**Daniel Lopes:** Yeah, I need to do that. I do something similar on the project folder. But this is a good idea. I actually put it on the agenda for today. Second half of this month once we get past feature completion. I think the timeline for OS will be this week and next, working as hard as we can to get to QA stage from ninth forward. We onboard a QA and beta, Whedon and whoever can test. During that week as well we create guides for how to use the product in the product code, here's how this screen works, here's the high level.

**Marcel Santilli:** That's why I created guides and tutorials. So if it's internal we can use this. And I create a section or a tab. That's why I created tutorials. But we can do like product tabs as well.

**Daniel Lopes:** But the value of being in the code base is that agents can read it while you're coding and vice versa, you can create pages really fast by reversing the code.

**Marcel Santilli:** Yeah, that's one of the restrictions maybe we have. For me I effectively do the same. But the trade off of having it locally is then anytime I need that context for anything else, it becomes harder. So I just run it as a workspace parallel folder.

**Daniel Lopes:** Yeah but you can't do like CI. We shouldn't launch a large feature without docs. Like we can reinforce things like that on the output, but you can tie the whole thing together.

**Marcel Santilli:** Is there a way to like effectively do a symlink or something close to that to where it's in both places, but anytime a push happens to one, it syncs to the other?

**Daniel Lopes:** You can do a git submodule. It's a bit of a hassle, but the docs become its own repo. You can send link as well.

**Marcel Santilli:** Right now it's like I had docs in context one and now that I started making docs in the handbook better, I almost never reference my docs in context zone because they're so outdated. It would effectively take a thousand dollars worth of credits to make it better.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** The handbook is the most thought through. Regardless, I think it would be really helpful for me to convert the OS things we've discussed into docs here. If we had the equivalent of what I have for CheckThat for OS or if you point me in the right direction, I can help.

**Daniel Lopes:** I think that's what I was thinking that this should be done when we make all the features. As in demo, what is feature complete, what is not a part of the scope. So what is there is actually the training for how to learn. That's like William, this part is not going to need a lot of training. But everyone else needs training so it has to be really enablement material.

**Marcel Santilli:** So it's almost like methodology more here because we have too many things to read. People don't read.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Yeah, that's true. I was just using this like quick context. Everything. So I don't have to explain like what an opportunity is. I don't have to explain. And it shortcuts like the things. But anyways it's fine. It's not a big deal. But even this helps. Having this already explained, which I took from your doc.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Like the product ecosystem just helps a lot. Understanding like, yeah, we'll figure out.

**Daniel Lopes:** I think a big part of the second half of the month once we lock in all the features. Because there's still some features to be defined as in how can we ship this in the next two weeks? Because the way I'm thinking is the next two weeks is to get your feature complete. Whatever I don't finish, because I need to be off from like 9th to 16th because of my parents here. And then during that week they will be in QA bug fixes. And then when I come back, it's William. The beta team starts and documentation. I write it. And that week will also be the week that we can launch the output. The guys are just finishing wrapping up the set of features that were not possible before until the foundation. So the cost and the like replacing Langviews and Galileo became possible just because we have all this infrastructure. So I want to have these features as part of the launch. So they're clear, oh wow, this is not possible before. So they're finishing that this week. Next week they essentially QA everything and polish. And then they have one week where I'm out to do whatever is left and then announcement on the 17th. Both products will be essentially in a good spot on the week of the 15th.

**Marcel Santilli:** Okay, I think that sounds good. How should I think about this? In my mind, it's like it's almost like a subset of CheckThat in the public pages plus a subset of the OS is what we use in both as an audit. And it will accelerate the crap out of efficiency. Because most of the inefficiency in both our sales process and the first two weeks of a sprint is go research them, go research their space, go research all the competitors.

**Daniel Lopes:** I think OS needs to do it as part of the workspace calibration. It's the setup phase. And yeah, that is because the workflow we actually have there is that for the opportunity finding.

**Marcel Santilli:** But you need to do it so there's one quick thing though. You definitely need to do it as part of the setup. But we do it no matter what in sales and like. And we need to do a version of it for CheckThat. For instance right now, Corelogix. The deal is kind of stuck and had I done a quick process of just showing their gap, it would move a little bit more.

**Daniel Lopes:** Oh, I think the audit is. We talked about that with the team last week because we have the on page health stuff that data for SEO gives that we can do for like 5 dollars for like 10,000 pages or something. And then you have site wide things that we would need anyway. But we could expose those as consumable things.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Integrate both.

**Marcel Santilli:** Exactly. Like imagine if like you send a version of this during sales. But then there's parts of this that are similar to Crunchbase where if you go to Crunchbase there's locks everywhere. Or if you go down here, it's like you know, it'll be cleaner. But the idea is like as much as possible it's public and CheckThat pages and we use that so we don't have to do deep research from scratch on every brand. Like if you've already done the whole, you already mapped the whole category, you've already done reputation analysis and overall brand context on every player. You have their AI visibility already computed. We're doing that already. And then we're just going and doing a quick audit on a few more things and then presenting mostly that information.

**Daniel Lopes:** Yeah. Like I don't see why we wouldn't be able to like if you have a sales lead, you go into CheckThat, you create a workspace. You go into OS, create a workspace and then let that trigger the site audit and the basic crawler and sitemap discovery. And you do the same on CheckThat to find all the visibility and all the things. And one calls the other as an API.

**Marcel Santilli:** Yeah, okay. Yeah. Because like these audit pages can both be checked out or GrowthX branded. It's just swapping the logo and where you host it. But it's like effectively it's the same thing.

**Daniel Lopes:** Yeah. And like if you do that, let's say CheckThat wants to generate these pages. Like let's say we want to have those audit pages as like a magic link inside CheckThat that you can send around as a salesperson. If we have like this API that requires doing something on OS to enable to render that, that is possible.

**Marcel Santilli:** So do we need to create a workspace? Because like what I'm noticing with CheckThat is like I have to create the workspace so I'm creating a bunch of workspaces. They're not really effectively workspaces. It's me like running these processes, which is fine, but it's almost like a pre stage workspace.

**Daniel Lopes:** Yeah, we can shortcut that. We can have like a pre sales workspace flag or something that doesn't show up in the grid. And it's just used for doing site audits. And that's pretty straightforward. And it could even create on the fly.

**Marcel Santilli:** Because CheckThat actually has more dependencies on having to run things a bit more. But then were you imagining that? So let's imagine we don't know there's a legit brand like Corelogix. They're legit. Or even Eon, which just raised 127 million. They're legit, they effectively need help. But we don't know if they're going to be a free user, a CheckThat user, or a GrowthX client. Do you imagine like they come in inbound and they're very warm and legit? Do you imagine automatically trigger, which one creates first a CheckThat account or OS account first?

**Daniel Lopes:** Yeah, I think the CheckThat one makes a lot of sense because CheckThat runs a bunch of research and creates articles and stuff first. And then OS essentially has a prerequisite to run this first.

**Marcel Santilli:** And then OS is all about auditing their website.

**Daniel Lopes:** Yeah, ideally, ideally every company on OS has a CheckThat profile so we don't have to do all this heavy lifting of reputation and competitor and all that.

**Marcel Santilli:** But the ideal process here is like we're computing the workspace and CheckThat has to be created to do certain things. So let's pick this category. This category has 50 players. Okay, let's make sure those 50 profiles are created and then make sure we're tracking all 50.

**Daniel Lopes:** The competitors I added on the workspace. Now workspace set up on OS is hard coded. Because I was expecting to be able to hit an API on CheckThat and pull from there. Like one of the steps in the setup should be like create a CheckThat profile.

**Marcel Santilli:** The way I was doing here that I think could be really interesting is use reputation to create a short list of 25 to 50 which are the ones that Gartner and G2 rate the highest. It's a combination of all of them essentially. Like it's effectively like you have the entire audience and then the short list that for sure triggers are the ones that have shown up and have legit reputation.

**Daniel Lopes:** Yeah, like, it's essentially like there's 50 of these, right? Where they show up as like a leader in the magic quadrant.

**Marcel Santilli:** Exactly. Like some spaces call it one thing, others call it something else. Cloud native storage versus data center backup versus enterprise backup. But they all effectively are similar. And then there's our version of how we categorize too, which is going to evolve. But our version is like data and backup or something like that.

**Daniel Lopes:** Right, right.

**Marcel Santilli:** And this essentially creates a really good short list of legit companies. And then that's the short list that those for sure should be mapped, should have deep research, should be analyzed. Because if Gartner put an analyst on a vendor and that analyst talked to over 20 customers, they have to have like over X amount of revenue, they are as legit as they get. You should know them.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** And so that was kind of my thought process. Between Gartner, Forrester, and some of these, plus peer reviews, mostly G2 and Trust Radius, Giga Ohm, you can get to the top 25 to 50 legitimately reviewed ones. And then those for sure we trigger. And we don't need a human to approve it.

**Daniel Lopes:** Yeah, it makes sense.

**Marcel Santilli:** And then for the OS setup, hopefully we can just pull from that.

**Daniel Lopes:** From that. Yeah, we can pull from. Yep.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Okay, cool. All right. I'm gonna work on some.

**Marcel Santilli:** All right, man. Sounds good. I'll let Stone know, and then I'll keep you posted.

**Daniel Lopes:** Sounds good. Yeah, whenever the sooner he can come, the better.

**Marcel Santilli:** Yeah. I told him let's go.
