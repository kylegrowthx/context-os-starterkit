# Lovable <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-15
time: 20:00 UTC
duration: 31 minutes
organizer: George Haikal (GrowthX)
participants: Marcel Santilli (GrowthX), George Haikal (GrowthX), Aida Knezevic (GrowthX), Cecilia Stallsmith (Lovable), Rachel Hepworth (Lovable), Anton Osika (Lovable), Carilu Dietrich (Lovable), Fern (Lovable)
fathom_recording_id: 94476185
fathom_url: https://fathom.video/calls/441107109
share_url: https://fathom.video/share/VqymdoRE3QNkDsUbAsUFVw8sef9SBsZS
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

GrowthX presented an MVP template gallery with high-quality designs and a guides section ready for publication, with Lovable approving the direction. Marcel outlined platform limitations in Lovable's API capabilities (inability to iterate on repos programmatically), noting this will require engineering collaboration to solve as Lovable scales enterprise. GrowthX is ready to publish templates and guides within 2 days pending Lovable's final sign-off, along with 5 new comparison articles under review in Airtable.

---

## Context

GrowthX is delivering content marketing and templates for Lovable, a no-code platform for building web applications. Lovable recently launched a templates feature and is expanding content offerings including guides and comparison articles. This weekly sync is part of ongoing collaboration to develop high-quality, scalable content systems for Lovable's user base. Cecilia (cc) leads product marketing on the Lovable side and had recently been traveling for meetings at OpenAI and other SF-based companies. The team is focused on getting templates and guides published quickly to start generating search index signals and gathering analytics data, with a short publication timeline (2 days) chosen over perfecting design before launch.

---

## Relevance

**To GrowthX Delivery:**
- MVP template gallery with 10-30 initial templates launching within 2 days — demonstrates ability to ship faster than perfecting design quality first
- Guides section live as separate content pillar from blog, with 5 new articles (comparison articles lead focus), ready for publication pending Lovable's 1-2 day review window
- Technical approach using flat URL structure (/templates/[name]) instead of nested categories for flexibility and SEO scalability
- GrowthX is building proprietary backend tools for research, fact-checking with confidence scoring, bibliography generation, and knowledge base for semantic content retrieval

**To CheckThat:**
- Knowledge base system being built for Lovable content will store research artifacts, enabling semantic retrieval and reuse across multiple content types
- Site crawler and daily snapshot system correlating content changes to analytics signals—directly applicable to CheckThat's AI visibility index concept

**To GrowthX Business Development:**
- Lovable platform limitation flagged as escalation point: cannot ping API for iterative improvements on repos, only import repos after creation — may block enterprise expansion
- Action item: Marcel to provide detailed technical feedback on Lovable platform limitations to product team for potential roadmap impact
- Lovable launching Shopify templates next week — validates market demand for templates and suggests content expansion opportunity
- Editorial quality bar discussion: Lovable team is not pushing perfectionism; pub-first-iterate approach aligns with GrowthX's lean methodology

---

## Overview

- Templates and guides are nearly ready for publication, pending final approval
- GrowthX has developed an MVP gallery experience for templates with high-quality designs
- Guides section is being built as a separate content area from the blog, with initial articles ready
- GrowthX is developing sophisticated backend tools for content creation, research, and site optimization

---

## Key Topics

### Template Gallery and Design

  - GrowthX presented an MVP gallery experience for templates
  - Categories and layout structure are in place, with ability to hide empty categories
  - Template designs shown are high quality, surpassing current UGC content
  - GrowthX aims to start with 10-30 templates, gradually expanding to fill category pages

### Guides Section Development

  - New "Guides" section being created separate from the blog
  - Initial UI is similar to blog but will be improved over time
  - 5 new articles are ready for Lovable team review
  - Content will be published unless Lovable team intervenes within 1-2 days

### Technical Approach and Infrastructure

  - [GrowthX is using a flat URL structure for flexibility (e.g., /templates/\[name\] instead of nested categories)](https://fathom.video/share/VqymdoRE3QNkDsUbAsUFVw8sef9SBsZS?tab=summary&timestamp=902.0)
  - Backend tools include:
      - Research planning and evaluation system
      - Fact-checking with confidence scoring
      - Knowledge base for storing content artifacts
      - Site crawler for tracking daily changes and correlating with analytics

### Content Creation Process

  - GrowthX is building sophisticated tools for content research and creation
  - Includes bibliography generation and fact-checking with confidence scores
  - Knowledge base being developed to store and retrieve information semantically

### Product Limitations and Potential Improvements

  - Current Lovable platform limitations prevent multi-step API interactions for complex app building
  - Marcel to provide detailed feedback on platform limitations and potential improvements
  - Discussion needed with Lovable product team on addressing these limitations

---

## Action Items

**Marcel Santilli (GrowthX)**
- Provide detailed feedback on Lovable platform limitations to product team; schedule session with product team to discuss API iteration constraints and GitHub integration workarounds

**Rachel Hepworth (Lovable)**
- Get NAD (Sebastian, presumably) to review gallery homepage experience for templates and confirm design direction

**George Haikal (GrowthX)**
- Publish guides and templates within 2 days unless Lovable team intervenes with feedback

**Cecilia Stallsmith (Lovable)**
- Review 5 new articles in Airtable (link coming via Slack); tag Fern for comparison articles review

---

## Transcript
**Cecilia Stallsmith:** Oh my gosh, I'm sorry.

**George Haikal:** No worries at all.

**George Haikal:** I think last time we talked, Cece, you were like pulling a pita bread out from the pantry to eat it.

**Cecilia Stallsmith:** Yeah, I'm sorry.

**Cecilia Stallsmith:** I have a block on my calendar for eating and it doesn't get respected very well, so I'm going to have to work on that.

**George Haikal:** You've done better than me.

**George Haikal:** I don't think I even have a block.

**Cecilia Stallsmith:** Kind of just get it where it fits in.

**George Haikal:** Good to be good for you.

**Aida Knezevic:** Yep.

**George Haikal:** Beautiful.

**George Haikal:** Okay, just move some things around.

**George Haikal:** Let's see who's in here.

**George Haikal:** Cool.

**George Haikal:** Marcel will be joining in two minutes.

**George Haikal:** He's wrapping up another call.

**George Haikal:** Cece, I'm assuming Rachel's still going to join or?

**Cecilia Stallsmith:** Yes, she should be.

**George Haikal:** She will be, I think.

**George Haikal:** Amazing.

**Cecilia Stallsmith:** Yeah, sorry for the minute.

**Marcel Santilli:** It's so good to see you.

**Cecilia Stallsmith:** How are you?

**Cecilia Stallsmith:** Good see you, too.

**Cecilia Stallsmith:** Guys, sorry for having not been able to join our last couple of conversations.

**Cecilia Stallsmith:** I know.

**Cecilia Stallsmith:** I was like being whisked around the city to open AI and like seeing Sam Altman walk by to meet with Anton and craziness.

**Marcel Santilli:** You know, it's tough being a celebrity these days, you know?

**Cecilia Stallsmith:** Pretty funny watching and like it was pretty, it was one of those moments where I was like, I feel like I'm in an episode of Silicon Valley because we really kept like hopping in an escalator, like go to masters of scale, like go to open AI and like all these things were just very bougie feeling.

**Cecilia Stallsmith:** I was like, what's happening?

**Marcel Santilli:** One of the most surreal moments I've had, funny enough, I went to Alex's house, which is like literally over there, like in our office, and the CEO guy used to be the CEO of Scale.

**Marcel Santilli:** You know, and we're setting up upstairs for recording and then I go downstairs to grab water or something.

**Marcel Santilli:** And then Sam Altman walks out of his room because he was living with Alex, with his hair all messed up.

**Marcel Santilli:** Like he just woke up at 10 o'clock and I was like, hi.

**Marcel Santilli:** It was like this most awkward, like hi kind of thing.

**Marcel Santilli:** It's just like go about my business.

**Cecilia Stallsmith:** Like I'm just going to pretend you didn't see me.

**Cecilia Stallsmith:** It's funny because he very much is just a CEO, but I feel like the world stage, you know, like the platform, you know, it's just insane.

**Cecilia Stallsmith:** Guys, their company, they're really doing everything.

**Cecilia Stallsmith:** This is a different topic, but excited to dive in on all your things.

**Cecilia Stallsmith:** I have not gotten to review the stuff that you guys sent to, that you flagged me in, but it's on my list today.

**Cecilia Stallsmith:** What else?

**Marcel Santilli:** Let's jump in.

**Marcel Santilli:** We're going to go fast forward mode, you know, like terrible mode here and then stop us.

**Marcel Santilli:** But the three things we want to get through today is guides.

**Marcel Santilli:** We're not blocked, but it's mostly final sign off.

**Marcel Santilli:** I think we've done most of the work here on both like calibration, building the section.

**Marcel Santilli:** And then, like, a quick check on both the MVP experience, make sure we're good, and then the quality bar, which Sebastian has a review and gave positive feedback so far.

**Marcel Santilli:** So those are, like, the three main things.

**Marcel Santilli:** We can go in that order, or we can go in reverse order.

**Marcel Santilli:** Like, so does that sound good?

**Marcel Santilli:** Is there anything else that you want to talk about besides this?

**Marcel Santilli:** All right, going once, twice.

**Cecilia Stallsmith:** Thank you.

**Cecilia Stallsmith:** I think I'm good.

**Cecilia Stallsmith:** Rachel, anything else you'd want to cover?

**Rachel Hepworth:** Nope, that's it.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Want to start with templates or guides?

**Marcel Santilli:** Let's do templates first, just because this is a functional complexity.

**Marcel Santilli:** All right, perfect.

**Marcel Santilli:** So we, George, want to drive some of these, and I can kind of edit commentary on all of them, or as you kind of click through.

**Marcel Santilli:** You're only sharing Notion, by the way, so I don't know if you want to share.

**George Haikal:** Yeah, we can click through each experience as well when we speak through it.

**George Haikal:** But basically, from last week, the three goals were to create an MVP experience of how the templates would actually look on the website, and then send three or four examples of what a great template looks like in terms of quality. I know there were some concerns about what that bar really is for Sebastian, and for us—can we hit it programmatically? Can we do enough variation in the design? All that was sent over last night. We can start either with the overall template gallery experience, which is the MVP, or with each individual template.

**Marcel Santilli:** Yeah, let's start with the gallery overall. By the way, I should have the password already, but I don't know if the link is in one password. I can send you the link again as well.

**Marcel Santilli:** Cool.

**George Haikal:** It takes a bit to load.

**George Haikal:** Cool, I have it up here.

**George Haikal:** So this is the gallery experience that we designed, again, the MVP.

**George Haikal:** These categories are more than placeholders now, because we thought through all the categories Sebastian had, and then based on our research, what we thought was most important to start with. But this is the overall experience.

**George Haikal:** You can click into each one here, and we took inspiration from what Sebastian was already doing, because we didn't want him to make too many structural changes to his templates, and then kind of expanded on that.

**George Haikal:** So there's a place to actually view the thing you're building.

**George Haikal:** In this case, it's a dark mode blog template.

**George Haikal:** There's the key highlight section.

**George Haikal:** There's the remix function, which we will plug in to get to work.

**George Haikal:** There's a breakdown of features and capabilities, and then there's an about this template, which breaks down pretty much everything you need to know about the template, how to use it, and this we can change and edit as needed as well.

**George Haikal:** What was looking more so for layout, structure, and feedback on both of those.


**Cecilia Stallsmith:** Look and feel is really cool.

**Cecilia Stallsmith:** Rachel, where do you feel like Sebastian's feedback feels that this is, like, not making the mark?

**Rachel Hepworth:** I feel like one of the things he had been saying was, like, there's this, like, one-shot prompt concept.

**Cecilia Stallsmith:** It looks great to me.

**Rachel Hepworth:** I don't know if you saw his latest comment, but basically he just claims there was confusion.

**Rachel Hepworth:** So his concern is he wants to show off apps that are, like, really robust and complex, and you need multiple prompts to build it that way, which is not how growthx can do it programmatically.

**Rachel Hepworth:** And that's probably true.

**Rachel Hepworth:** Like, can't build a super, super robust app with one prompt.

**Rachel Hepworth:** And that's fine.

**Rachel Hepworth:** So we can share those versions, which, like, Sebastian and Tim would have to make on the homepage and things.

**Rachel Hepworth:** But he doesn't have any problem with this as a long tail and in a template gallery.

**Rachel Hepworth:** So he was basically like what you and I said, Cecilia.

**Rachel Hepworth:** He was like, oh, I'm fine with that.

**Rachel Hepworth:** I don't know where there was confusion.

**Rachel Hepworth:** It's just the difference between the app you can build with multiple prompts, which, of course, is always going to be more robust than an app than something you can build with one.

**Rachel Hepworth:** But one is how you get scale.

**Marcel Santilli:** And so I think...

**Marcel Santilli:** I think we're all in agreement now and should just move forward.

**Marcel Santilli:** Rachel, could I?

**Marcel Santilli:** Marcel, have you guys talked?

**Rachel Hepworth:** finish your thought.

**Rachel Hepworth:** I'm curious how you, like, what the idea is in terms of how your work, basically, I all of this should come together in one place.

**Rachel Hepworth:** And is there clarity with you guys on how that's happening?

**Marcel Santilli:** So there's a couple of things.

**Marcel Santilli:** So just so, excuse me, for your context, think I mentioned with Rachel on that last week.

**Marcel Santilli:** But one of the main limitations is you can't ping an API for Lovable with one really good prompt and then look at an entire repo of what it actually built and then send another API request to iterate on that.

**Marcel Santilli:** And so the reason we can't do programmatically is not because we're, like, not capable of our tech limitation on our end.

**Marcel Santilli:** We don't have an API.

**Marcel Santilli:** It's a platform limitation on that.

**Marcel Santilli:** And then so then when we spent some time exploring, was like, well, we can build an entire repo.

**Marcel Santilli:** And that's literally what Webflow wants us to do and other people wants to do is like.

**Marcel Santilli:** And then you can just import a repo, right?

**Marcel Santilli:** When we did this for Bolt, it actually worked beautifully.

**Marcel Santilli:** Unfortunately, when we try that out with Bolt, I mean, with Lovable, even using the stack that we know Lovable likes, which is like Byte and like Tailwind, you know, like using the stack.

**Marcel Santilli:** When you do that and then you import it, it fails often.

**Marcel Santilli:** And when it doesn't fail, if you try to give it a prompt to iterate it, everything breaks and it goes wild.

**Marcel Santilli:** And so we kind of abandoned that or put that aside for now.

**Marcel Santilli:** And so the next step that we did was like we tried a bunch of different things between like using picking designs and porting and whatnot.

**Marcel Santilli:** And what we arrived at is like this combination of like inspiration plus really detailed prompt in our workflow plus about, you know, one to two hours of design intervention that we are confident we can cut that down to less and less and less intervention, essentially, you know.

**Marcel Santilli:** And that's what you're seeing here is an example of that.

**Marcel Santilli:** And so we can scale this and we're very confident.

**Marcel Santilli:** Often that over time, the scalability will get even better while maintaining or improving quality as well.

**Marcel Santilli:** I know that was a lot, but I wanted to explain the context. Essentially, one prompt doesn't get you quite there.

**Marcel Santilli:** And unfortunately, there's not an easy way we found so far using the platform itself outside of prompting to create that loop. Most of that is because of the way the integration works with GitHub. With Bolt and others, you can connect the project directly.

**Cecilia Stallsmith:** And with Lovable, you can import after you create it into GitHub. So it's kind of a little nuance to capture and give to the product team.

**Rachel Hepworth:** So I was going to say, is this like a discussion you're having with Sebastian?

**Marcel Santilli:** Is there any interest in changing that?

**Marcel Santilli:** It's not in full transparency because we just want to make sure we deliver on the sprint, right? So if we spend time there, it would distract away from us actually driving the numbers that you all care about. And so for us, if those two things launch, then it's like, okay, breathe, and now go iterate on it.

**Cecilia Stallsmith:** Rachel, this is like a product team decision. This is beyond Sebastian.

**Rachel Hepworth:** And it's not about him doing, it's about him thinking through about whether it makes, like, who's driving this on the lovable side?

**Marcel Santilli:** Is this actually important in terms of something that at some point we want to build out? Or is it not? I'm an insanely heavy user of Figma, Make, Lovable, Bolt, and now Claude Code and Copilot, and I've used all of them. I've never written a single line of code in my life other than HTML back in the day. So from tens of hours of vibe coding into all these platforms, I just know where the platforms fall short. And so I can give very clear feedback, if you all want, to the Lovable team.

**Rachel Hepworth:** I think it would be useful and to understand based on that feedback, what you think it would unlock to fix it.

**Marcel Santilli:** And then internally, we can decide when and how.

**Marcel Santilli:** And where we might want to change it. That would be super useful, I think.

**Rachel Hepworth:** Yeah, I feel like that's a blocker that we're going to run into increasingly as we go enterprise, so I'd actually love to hang in a session with you and some people. But I don't want to take up too much of your time—even a recording of some of that would be useful. I have a set of people we should get.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** We'll take it as an action on our end, and then if you can just tell us who and when, I'll prioritize it for sure.

**Marcel Santilli:** This is super important.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And the reason I said I didn't want to spend the time now is not because of my time, it's more so the rest of the team can continue to execute and not add scope or change direction.

**Rachel Hepworth:** I agree.

**Marcel Santilli:** So can you show some of examples, George, really quickly?

**Marcel Santilli:** I feel pretty good, and I used to be a designer back in the day, so it's like on how these things look, and I would have my personal blog on this, for example.

**Rachel Hepworth:** I thought these look nice.

**Rachel Hepworth:** I think my question is really that we need to get NAD to look at them. Does it look nice? I think it looks nice. And then, does it conform with the Lovable design? Is this for the guides and the Lovable posts?

**Marcel Santilli:** That's what I wasn't totally clear about. These are templates that go into the library.

**Rachel Hepworth:** Templates.

**Marcel Santilli:** Okay, so disregard that. They're substantially better than the UGC stuff on your homepage.

**Rachel Hepworth:** I mean, Marcel, that's too low of a bar, but yes, I agree.

**Cecilia Stallsmith:** Yes, absolutely.

**Marcel Santilli:** Um, let me put it this way, like, the bar is great.

**Marcel Santilli:** These look beautiful.

**Marcel Santilli:** Yeah, it's like, we have a designer in the loop.

**Marcel Santilli:** And we're coming up with a lot of different ways of building additional features, which is like how you create the images, the icons, the logos, the copy.

**Rachel Hepworth:** So those are all things.

**Marcel Santilli:** It won't get better and more scalable from here, so.

**Rachel Hepworth:** Okay.

**Rachel Hepworth:** On the templates like the homepage and the gallery experience, you have a lot of categories there. Are you thinking you're going to have things for every category before you launch?

**Rachel Hepworth:** How are you thinking about making it not look empty?

**Marcel Santilli:** We can hide categories. The main thing is most of the traffic out in the world goes to list pages, right? So if you search for most templates, you land on a filter view of a gallery. Because of that, to rank for construction website templates, it's not just one template—it's more like 50 different templates. We're trying to have enough within a filter view to fill that. Our goal is to not let publishing a thousand be the enemy of getting 10 out, then 20, then 30, and getting it indexed. The main thing we need to validate is getting one sheet indexed, getting impressions, and seeing where we can get clicks while continuing to crank.

**Marcel Santilli:** It's just a process, but that's why I'm being a broken record and trying to push as much as I can.

**Marcel Santilli:** And I hope that's okay.

**Rachel Hepworth:** Yeah, that's great.

**Rachel Hepworth:** Awesome.

**Rachel Hepworth:** What do you need to like get close to being able to...

**Rachel Hepworth:** Start publishing this stuff.

**Rachel Hepworth:** What are the next steps for you guys?

**Marcel Santilli:** George, is there anything that we're blocked on deploying what we have other than continue to crank on templates?

**George Haikal:** No.

**George Haikal:** Outside of getting this layout and structure approved, if you want NAD.

**Rachel Hepworth:** Okay, now we can scrap NAD, taking a look at the templates.

**Rachel Hepworth:** So the templates seem unblocked.

**Rachel Hepworth:** I think it's more just the gallery homepage experience, right?

**Marcel Santilli:** Making sure that he feels okay with that.

**George Haikal:** We can get with NAD there.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then just merge into slash templates.

**Marcel Santilli:** think that's where, and then we're good.

**Marcel Santilli:** We're in your repo.

**Marcel Santilli:** This is a branch in your repo already.

**Marcel Santilli:** So it's like, it's not like this has to be rebuilt somewhere else, you know?

**Marcel Santilli:** So it's like, this is, I think post-publishing before we link to it or anything like that, I'm sure we're going to want to do some performance testing and just make sure like things are good, you know, overall in some QA.

**Rachel Hepworth:** Well, I don't know how much QA level does.

**Marcel Santilli:** We'll have to figure that out.

**Rachel Hepworth:** Yeah.

**Rachel Hepworth:** It may be very little.

**Marcel Santilli:** Us clicking around just to make sure.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's like, it's good.

**Marcel Santilli:** Cool.

**Marcel Santilli:** I want to make sure we, we can come back to this later on too, but it's, if we're good, like the main thing we're doing here is just like continue to refine the categories, the subsections within these categories, different filters we're going to have, but we're taking very much like, our recommendation is to try to take a flat approach.

**Marcel Santilli:** So let me explain.

**Marcel Santilli:** So one of the mistakes people make when they're doing programmatic is they set into a ontology or taxonomy, right?

**Marcel Santilli:** So slash internal apps or slash SASS slash something else, right?

**Marcel Santilli:** The challenge with that or an individual page is that that ties a URL slug to a tag and that tag over time can change names and can change intent and a bunch of different things.

**Marcel Santilli:** And so like the way that I prefer to do this is like, you have index pages and you have individual pages, right?

**Marcel Santilli:** So an individual page is just like slash template slash.

**Marcel Santilli:** Something, for example, right?

**Marcel Santilli:** And I'll write this down more.

**Marcel Santilli:** Whereas, like, the index pages are just, like, individual URLs of themselves.

**Marcel Santilli:** In other words, individual pages are not subpages of the index collections.

**Marcel Santilli:** So, like, let me just, like, explain in a different way to hopefully make sense.

**Marcel Santilli:** When I was at DeepGram, we launched SlashLearn.

**Marcel Santilli:** If go to SlashLearn, there's, like, multiple grids on every single piece of content.

**Marcel Santilli:** If you go to individual article, it's SlashLearn, SlashArticle, and then there's just the URL, right?

**Marcel Santilli:** But then if you go SlashLearn, SlashTopic, Slash a bunch of other things, it's a filter view of the index page.

**Marcel Santilli:** But even if the article is part of a how-to, it's not under a sub-URL slug, right?

**Marcel Santilli:** And so the idea here is, like, trying to keep things as flat and flexible as possible.

**Marcel Santilli:** Is kind of what we're going with.

**Marcel Santilli:** So that...

**Marcel Santilli:** Over time, if you want to have a thousand tags or a thousand filters, you can have a thousand filters and you don't have to migrate thousands of pages from one filter to the other.

**Marcel Santilli:** And you can have a many to many relationships between categories and filters and individual pages.

**Marcel Santilli:** So you can reorganize it very quickly without having to do, because like what you end up with is like a bunch of having to move things around or end up with URL slugs that make no sense.

**Marcel Santilli:** And then you're constantly migrating pages around because you decided to change your taxonomy on your filters, essentially.

**Rachel Hepworth:** Makes sense.

**Rachel Hepworth:** Sorry, that was very confusing.

**Rachel Hepworth:** I mean, is there any reason we wouldn't want to do it?

**Rachel Hepworth:** Is there any drawback that we should be aware of?

**Marcel Santilli:** No, it's just like the main thing is you can pull via API a lot of the stuff.

**Marcel Santilli:** And over time, you're going to serve the individual pages.

**Marcel Santilli:** Think of individual pages like as the page plus a card that shows it.

**Marcel Santilli:** Like there's so many different ways you can show it.

**Marcel Santilli:** And you can show it in multiple different places on your app and your site anyways.

**Marcel Santilli:** And so there's really no drawbacks to do.

**Marcel Santilli:** It's just, like, a more flexible way, you know, versus, like, setting ourselves in stone.

**Rachel Hepworth:** Cool.

**Marcel Santilli:** Let's go to Guides really quickly here.

**Marcel Santilli:** I'm really excited for Guides.

**Marcel Santilli:** And so there's a lot of UI UX improvements we'll make, but we're just going to MVP the hell out of this thing. This is a preview URL, so that's why it's super slow.

**George Haikal:** It won't be this slow on the actual site.

**Marcel Santilli:** This is very similar to the blog. This is not what it will look like a month from now—it will look much better. But this gets us the ability to publish. This has three pieces of content that Aida and the team have produced already, and we'll fill that in more and more. The Guides experience will have different categories or filters.

**Rachel Hepworth:** Is this going to be separate from the blog, right?

**Marcel Santilli:** Correct.

**Rachel Hepworth:** This is the other thing that I think NAD just needs to confirm, yeah looks good or no.

**Cecilia Stallsmith:** Honestly, our blog is so bad that part of me is like, can we just, are you guys rebuilding our blog?

**Cecilia Stallsmith:** Our blog is so horrible.

**Marcel Santilli:** I mean, it is really bad. What we're doing is essentially duplicating your blog and cleaning up a couple of things. We're trying to get published things out, get things indexed, and then over time improve this. If you like the improvements we make here, you can apply that to the blog or copy the style. The main thing is that this is the reason we're able to drive the kind of results we did for Augment Code and others—it's things like this that you're not linking to from almost anywhere. The faster we can hit publish so we can start indexing and getting signals, the better. But it's okay if we want to wait another week or so. We're ready to push this out and start shipping content.

**Cecilia Stallsmith:** I'm not, I've, Rachel and I have worked a lot of places where the CEO is like extremely intense about quality bar.

**Cecilia Stallsmith:** I would say that we are not that way.

**Cecilia Stallsmith:** I almost feel like I have to bring that to the company. I know Sebastian flagged it, but honestly, we're not that strong on quality bar.

**Cecilia Stallsmith:** So let's define a quality bar, but don't feel blocked.

**Rachel Hepworth:** I think we should flag it to you and then publish unless you hear otherwise.

**Rachel Hepworth:** So it's like onto us to, you know, like give this a day or two.

**Rachel Hepworth:** And if you don't hear anything, just move forward.

**Cecilia Stallsmith:** So the burden will be on us to intervene if we want to.

**Marcel Santilli:** Yeah, that, that is, that is perfect.

**Marcel Santilli:** Ada, is there anything on your end that you are blocked by or want feedback from the team here on the editorial side?

**Aida Knezevic:** Yeah, so we have five new articles that are ready for your review.

**Aida Knezevic:** I will follow up in Slack later with a link to the Airtable where you can find the documents.

**Cecilia Stallsmith:** But yeah, I'll tag Fern.

**Cecilia Stallsmith:** I think she took a look at the Lovable versus Bold article.

**Cecilia Stallsmith:** So she can also take a look at other comparisons that we're working on.

**Cecilia Stallsmith:** Great.

**Cecilia Stallsmith:** Thank you.

**Cecilia Stallsmith:** I think one of my biggest concerns is that from the stuff that she built for comparisons, there aren't a ton of differentiators.

**Cecilia Stallsmith:** And what's hard is a lot of our differentiators are a little bit intangibles.

**Cecilia Stallsmith:** So we're like, it just works on Lovable.

**Cecilia Stallsmith:** And people don't like that it doesn't just work on Bold.

**Cecilia Stallsmith:** So that's an existential product marketing problem I'm going to have to solve.

**Marcel Santilli:** There is like review stuff that we've been able to come up with where it's like Lovable has better reviews.

**George Haikal:** So that just works as reflected on some of those things.

**Marcel Santilli:** And then we can use like reviews and comments by people that are customers and users of Lovable and how they describe the product.

**Cecilia Stallsmith:** And that is the best product marketing is how people describe the product.

**Cecilia Stallsmith:** If they like the product, it's what they do, so, yeah.

**Cecilia Stallsmith:** Yeah, that's very, very helpful, because I do feel like when it comes to, like, a pure feature matrix, it gets a little underwhelmed.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Can I show the under the hood for a couple minutes? There's a lot of stuff we're building for the guides.

**Cecilia Stallsmith:** It's not a meeting unless I geek out a little bit—it's the only way I get energized. Also, I love seeing how you're building all of this.

**Marcel Santilli:** So you Vibe-coded a lot of this together, or do you have developers building this?

**Cecilia Stallsmith:** We have a team of about 20 plus people, but I Vibe-code a lot of things. I don't Vibe-code the whole app though—I Vibe-code just the frontend and UI only, using fake data, in a separate folder within the app. That way engineers can take it and implement however they want.

**Marcel Santilli:** This one is cool—it's a comparison tool generating a research plan, evaluating it in the loop, and storing everything in a knowledge base. You see the bibliography at the bottom. It's been a long time since I've heard the word bibliography—that's hilarious.

**Rachel Hepworth:** Take me back to school days.

**Aida Knezevic:** Exactly.

**Marcel Santilli:** In my school days in Brazil, I used to go to the library, and my dad bought this massive encyclopedia—cost like five grand to get all the editions. I had to transcribe word for word, and if you messed up even one word, you couldn't use whiteout. You had to throw away the entire paper.

**Cecilia Stallsmith:** Oh my gosh.

**Marcel Santilli:** Our kids will never know what it's like to white out something or have to start from scratch. Everything will just always be saved.

**Cecilia Stallsmith:** You won't even know what it's like to have your hard drive break.

**Marcel Santilli:** It researches passages for fact-checking and assigns confidence scores to each one. For example, "99.9% uptime, 500+ integrations, SOC-compliant"—it has nuanced corrections. Like, for credit-based pricing, it might say "credits based on complexity, not output size" if that's more accurate. This is our Atlas platform where we're building all the different content types. Each type has custom instructions and workflows. We'll be able to track ROI, AI visibility, and all this gets stored in the knowledge base so over time it can be retrieved semantically.

**Cecilia Stallsmith:** Will we eventually be able to use this tool?

**Marcel Santilli:** Yeah, that's the goal. We're about a month away from that.

**Marcel Santilli:** We also built a scraper and crawler that takes your site map and crawls every page, taking daily snapshots. It ingests all the content and markdown, allowing you to correlate results, workflows, human interventions, and output over time. In your CMS, there's no history—you don't see screenshots or know what changed about site vitals. With this, if you look at an analytics chart over 90 days, you can see how much was from content changes versus code changes versus vitals changes. We'll open this very soon, but I wanted you to see all the infrastructure behind the content we're sending.

**Cecilia Stallsmith:** And this enables you to do this at a bigger scale for us.

**Rachel Hepworth:** Does that also let you keep things like the competitor pages automatically updated?

**Marcel Santilli:** Not yet.

**Marcel Santilli:** Not yet.

**Marcel Santilli:** Mostly because that's not where we see the value. With agents, you're not going to let them do a pull request and merge on autopilot—that's a recipe for disaster. Plugging in your site and saying "publish anything you want anytime you want" is way too dangerous. For now, if it could alert you that a page might have issues, that would be useful. That's the opportunities tab we're still building—it takes website vitals and other signals to suggest ways to optimize your pages.

**Marcel Santilli:** Yeah, we're very, very close—maybe a week away from hitting publish and getting some of this stuff out. Then we'll start to get signals.

**Rachel Hepworth:** Yeah, we've made progress.

**Cecilia Stallsmith:** For a minute I was thinking, why are we doing all this dropshipping stuff? But we're launching with Shopify next week, so it'll become relevant.

**Marcel Santilli:** There you go. More dropshipping articles, guys.

**Cecilia Stallsmith:** You're leading us to the future that we didn't know we needed. You could also create a predictions engine for product-market fit.

**Marcel Santilli:** I have my little birds that fly around and listen to everything.

**Cecilia Stallsmith:** Yeah.

**Marcel Santilli:** Thank you both. I appreciate it. Thanks, bye.
