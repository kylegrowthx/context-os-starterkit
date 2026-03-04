# [Landbase] GrowthX <> Firework - Weekly Sync

<metadata>
date: 2025-07-03
time: 18:31 UTC
duration: 39 minutes
organizer: Megan Dickey (GrowthX)
participants: Cameron Brown (Firework), Jenn Peters (GrowthX), Megan Dickey (GrowthX), Ritesh Kewlani (Firework), Steve Takizawa (Firework), Vincent Yang (Firework), Can Ozdoruk (Firework), Jorge Leon (Firework), Winnie Ng (Firework), Samrawit (Firework), Camille Nepomuceno (Firework), Abhishek Anjanappa (Firework), Yi Jin (Firework/YAAS Partners)
fathom_recording_id: 72175087
fathom_url: https://fathom.video/calls/342251824
share_url: https://fathom.video/share/EWj2xYgpgPWXytGgLewq8bLunPfkrz3x
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

GrowthX and Firework identified critical technical SEO blockers causing poor blog indexation and inconsistent lead generation from content. The WordPress-to-Webflow migration has created a sitemap gap—the WordPress sitemap hasn't been updated since October 2024, excluding hundreds of new Webflow blog posts from search indexes. While some older blog posts still perform well (80k+ impressions), newer content is being indexed sporadically due to canonical tag issues and missing sitemap entries. The team agreed to test a targeted fix on March blog posts by manually updating the sitemap and reviewing canonical tags on landing pages, while escalating for technical SEO expertise from GrowthX's Dave Capone.

---

## Context

Firework is a D2C e-commerce platform that GrowthX is supporting through SEO-driven content marketing. The engagement centers on driving qualified leads through strategic blog content, but the account has been plagued by a structural problem: a migration from WordPress to Webflow that began in October 2024 created a misalignment between where content is published (Webflow) and where the indexable sitemap lives (WordPress). Firework publishes new blog posts weekly, but the WordPress Yoast plugin—which automatically manages the sitemap—has no visibility into Webflow changes, leaving hundreds of posts invisible to search engines. This is a serious revenue blocker for the account: blog content is a core lead-generation mechanism, but weak indexation makes measuring content ROI nearly impossible.

---

## Relevance

### To GrowthX Delivery
- Identified critical technical barrier to content success: WordPress/Webflow architecture mismatch is blocking blog indexation independent of content quality or strategy
- Requires coordination with infrastructure teams both at GrowthX and Firework to resolve (infrastructure personnel turnover at Firework is complicating resolution)
- Two parallel fixes needed: (1) manual sitemap management for immediate relief, (2) long-term Nginx rewrite to make Webflow primary and WordPress secondary
- Need to escalate Dave Capone (GrowthX SEO expert) to guide technical SEO decisions

### To GrowthX Business Development
- Account shows strong renewal signals: Firework is investing engineering time (Cameron Brown's focus) and leadership alignment (Ritesh pushing for solutions) on fixing underlying infrastructure
- Content strategy is solid (beauty, luxury, D2C verticals performing well), but technical blockers are masking true performance
- Lead gen metrics concerning but partially artificial: of 11 blogs published/refreshed April–June, only 11 leads generated (~1 lead per blog), but indexation issues may be suppressing demand-gen potential
- Risk: if technical SEO issues persist, content strategy improvements won't compound—need visible quick wins (March blog posts sitemap fix) to maintain confidence

### To CheckThat
- Relevant as real-world example of AI visibility challenge: even well-structured content (Firework's blog program) is invisible to search without proper technical foundations
- Canonical tag audit on landing pages reveals broader opportunity for CheckThat prompt/indexation validation tools in complex migrations

---

## Overview

- WordPress sitemap frozen since October 2024; new Webflow blogs not being added to search index
- Sitemap issue compounds canonical tag problems on landing pages, creating a dual technical SEO crisis
- Blog performance data shows extreme variance: March had posts with 80k+ impressions and posts with zero impressions, partly due to indexation randomness
- Lead generation from recent blog posts is low (0.06–1 lead per blog) compared to older WordPress content, which still drives majority of leads
- Team will pilot sitemap fix on March blog posts as proof of concept before full rollout
- Cameron to fix canonical tags on landing pages in separate call with Jenn; Megan to recruit Dave Capone for technical SEO guidance
- Long-term solution requires reversing site infrastructure hierarchy (Webflow primary, WordPress fallback) with Nginx rewrite, but infrastructure ownership unclear at Firework

---

## Key Topics

### Indexing and Sitemap Crisis

The core blocker: WordPress sitemap hasn't been updated since October 24, 2024, when the Webflow migration began. The Yoast plugin on WordPress automatically manages the sitemap but has no visibility into Webflow posts, leaving new blog URLs invisible to Google. Cameron discovered this by examining the sitemap XML directly—the most recent entry was dated October 24. While Google can still index pages not on the sitemap, inclusion significantly improves odds. Jenn confirmed via Google Search Console that many Webflow blog posts are missing from the search index. The team will test a manual fix: Cameron will unpublish old WordPress blogs, clear the outdated sitemap, manually export all current Webflow blog URLs, and write a new `blog-sitemap.xml` subsection. This is labor-intensive but will show quick results if it works.

### Canonical Tag Issues on Landing Pages

Secondary but critical: many landing pages have incorrect or missing canonical tags from the WordPress-to-Webflow migration. These pages rank important keywords for lead gen but are being penalized or de-indexed by Google due to canonical confusion. Cameron proposed a separate focused call with Jenn to audit and fix canonical tags on high-impact landing pages. This could be a quicker win than the full sitemap rebuild.

### Blog Performance Data: High Variance

Megan and Jenn analyzed blog traffic and lead generation from March through June. Performance is wildly inconsistent:
- **March:** Varied from 0 to 80k+ impressions per post
- **April:** 7 new blogs → 8 leads (1.1 leads per blog)
- **May:** 2 new blogs → 3 leads (1.5 leads per blog)
- **June:** 2 refreshed blogs → 8 leads; 0 new blog posts drove leads

Older WordPress content still dominates lead generation. The team suspects variance is partly due to indexation (older posts are indexed, newer posts aren't), but Ritesh raised a valid point: some March posts perform excellently despite not being on the sitemap, suggesting Google may be valuing other signals (author authority, topic freshness, backlinks) over sitemap inclusion.

### Content Strategy and Targeting

Current focus: high-performing categories are card podcasts, industry verticals (beauty, luxury), and D2C growth strategies. CTA testing is underway (pre-trial vs. book-a-demo). June's tariff-focused content performed poorly despite high topical relevance at the time, suggesting the audience cares more about evergreen, vertical-specific strategies than timely trend-jacking.

### Infrastructure Limitations

The long-term solution requires Firework to reverse the site hierarchy: make Webflow primary and WordPress a fallback for the few remaining WordPress-only pages, managed via Nginx rewrite rules. Cameron is willing to do this but needs infrastructure support. Key blocker: the infrastructure engineers who previously helped are no longer with Firework, and finding a new owner is proving difficult. Megan and GrowthX are watching this as a sign of potential resource constraints at Firework.

---

## Action Items

**Jenn Peters (GrowthX)**
- Schedule one-on-one call with Cameron to audit and fix canonical tags on high-impact landing pages (target: half-hour session, real-time fixes)
- Analyze blog performance & lead generation for posts published October 2024–February 2025; compare to recent data and identify patterns

**Cameron Brown (Firework)**
- Manually add March blog posts to new `blog-sitemap.xml` subsection in WordPress; track indexing improvements and lead generation impact
- Work with Jenn on canonical tag audit and remediation for landing pages

**Megan Dickey (GrowthX)**
- Contact Dave Capone (GrowthX SEO expert); recruit him for next week's Firework call to provide technical SEO guidance on sitemap and indexation strategy
- Share meeting context and technical findings with Dave before the call

---

## Transcript

**Jenn Peters:** Sweet.

**Jenn Peters:** My cat would not have, like, laps during a meeting, but she does like to, you may see, like, a tail, like, walk across at some point.

**Jenn Peters:** Hey, Cameron.

**Cameron Brown:** Hey, Cameron.

**Cameron Brown:** How are you?

**Cameron Brown:** Good.

**Jenn Peters:** I'm just admiring Megan's dog, which is trying to steal the show here on her.

**Cameron Brown:** Oh, that's awesome.

**Cameron Brown:** My wife is at work today, and I, that's only relevant because when she's home, my dog is attached to her hip.

**Cameron Brown:** But I am, I mean, because she's away, that means I am blessed to have this little guy with me.

**Cameron Brown:** Cute.

**Jenn Peters:** I saw, I saw them in your profile photo, I think, and I was like, oh my god, that is so sweet.

**Jenn Peters:** Are they a cockaboo?

**Jenn Peters:** Whoa, see, I mean, he's mistaken for a cockaboo.

**Cameron Brown:** constantly, he's a petite golden doodle.

**Cameron Brown:** Oh, dude.

**Cameron Brown:** He's so petite.

**Jenn Peters:** He is so sweet, oh my gosh.

**Jenn Peters:** He's just an old guy.

**Jenn Peters:** Hey, Megan.

**Jenn Peters:** Hey, You look like you're in a beautiful, like, sunshine, heavenly.

**Ritesh Kewlani:** there is, yeah, there seems to be a bug with my, you know, video call because it was fine in the previous meeting and somehow I don't know the camera is all wrongly, so let me try to turn it off.

**Ritesh Kewlani:** No, I don't mind.

**Jenn Peters:** Yeah, that's not a problem.

**Jenn Peters:** Yeah, it's not a problem for me.

**Jenn Peters:** It's just, if it bothers you, I think it looks great.

**Megan Dickey:** It's very ethereal.

**Jenn Peters:** Angelic.

**Jenn Peters:** Yes, exactly.

**Jenn Peters:** You look very angelic.

**Jenn Peters:** Yeah, so, Megan, if you want to, I'm just going to share from my screen.

**Jenn Peters:** Yeah, yeah, thank you.

**Megan Dickey:** Yeah.

**Megan Dickey:** Yeah, we're, were you all able to take a look at the, at the performance?

**Megan Dickey:** Or otherwise Okay.

**Megan Dickey:** As we can just kind of jump right in.

**Megan Dickey:** We can quickly browse through it.

**Ritesh Kewlani:** Like, I honestly wasn't able to review it, but yeah.

**Ritesh Kewlani:** Okay, yeah, yeah, yeah, no worries, no worries at all.

**Megan Dickey:** Okay, well, yeah, guess.

**Megan Dickey:** Yeah, yeah, can do it, Jen.

**Megan Dickey:** Cool.

**Megan Dickey:** Yeah, I guess we can start with the blog performance from March, April, May, and a little bit of June in terms of clicks and impressions.

**Megan Dickey:** And then I'll talk a little bit about leads based on blog posts published or refreshed in April, in March, April, May, and June.

**Megan Dickey:** So, yeah.

**Megan Dickey:** But yeah, like, months.

**Megan Dickey:** Okay.

**Megan Dickey:** All right, Jen, I'll let you go from there.

**Jenn Peters:** Yeah, for sure.

**Jenn Peters:** Yeah, so basically, I just compiled this little report.

**Jenn Peters:** I decided to go back as far as March.

**Jenn Peters:** I think we had originally talked about, like, April, May, June, but, you know, June being a little bit, like.

**Jenn Peters:** Quite recent to track really any performance.

**Jenn Peters:** I mean, even really March can be just in regards to like how long it can take to pieces start to see like some sort of results.

**Jenn Peters:** But what you can see here is clicks as well as like zero click pieces.

**Jenn Peters:** And then like each section has like some key insights at the bottom.

**Jenn Peters:** So like one thing to note is that like for March and like part of April, just kind of as time allowed for me, I just kind of like took a look at some of those like zero clicks, zero impression ones to see like what's going on there.

**Jenn Peters:** And yeah, there's like definitely some issues with like indexing.

**Jenn Peters:** I mean, some of these across the board could be like some newer pieces as well, which is something to keep in mind is that they might just not have had enough time to like really gain any traction.

**Jenn Peters:** But we do see that those kind of like indexing issues across some of the pages, which definitely could be affecting clicks as across the board.

**Ritesh Kewlani:** Jen, Jen. Quick question. Like, why is this indexing issue affecting some of the blogs and not the others? Like, what is happening here? Were you able to deep dive and figure out what is the root cause of this?

**Jenn Peters:** Yeah, I mean, Cameron might be able to give a bit more insight into that just because you guys have a lot more kind of view into migration and that kind of thing.

**Jenn Peters:** But what I'm assuming is that some of these are, like, you know, some of the ones that are kind of, like, higher impressions doing better are some of those older posts that we were talking about before that are from WordPress.

**Jenn Peters:** And then there's been some, like, messiness with the migration as this stuff moves over to Webflow with, like, indexing and site mapping issues that are kind of causing some of these places.

**Jenn Peters:** Like, even the blog, like, landing page, I think, is one of the ones that is a little bit, well, hidden at the moment.

**Jenn Peters:** So, yeah, Cameron, I don't know if you want to add to that or have something else?

**Ritesh Kewlani:** So, Jen, Jen, my understanding is, like, we started migrating to Webflow back in October.

**Ritesh Kewlani:** And since then all the blogs have been published on Webflow, so I don't particularly see that reason, like, for some of the blogs not getting indexed, because all of them are published in Webflow.

**Ritesh Kewlani:** There's definitely something else happening here which we don't know about, and my biggest concern is this has been happening for quite a long time, and if we don't understand what is the reason behind it, I think it's just going to keep impacting the blog performance going forward.

**Cameron Brown:** Yeah, so I do actually, I don't want to, like, I could probably spend the whole meeting talking about this issue, because it is so important.

**Cameron Brown:** I've been focusing on it for the last couple days.

**Cameron Brown:** So one thing that I kind of want to do, perhaps with you, Jen, on a separate call, is really dig into that canonical issue specifically, because I think perhaps we can fix some of the issues with our most important landing pages from that canonical tag perspective fairly quickly and sort of at least make some progress, get back on track in terms of like the SEO quality that we want to be at.

**Cameron Brown:** I will quickly share my screen to sort of like illustrate a point that we've been sort of hypothesizing for a while.

**Cameron Brown:** First of all, it took me a while even just to find the sitemap.

**Cameron Brown:** I kind of had to go digging through some old WordPress code because typically it's very common for things to just exist under sitemap.xml and it was kind of hard to find this URL.

**Cameron Brown:** But anyways, here is our post sitemap, which essentially, I mean, for the people who don't understand sitemaps very deeply, this is all a single sitemap.

**Cameron Brown:** It's just sort of convenient.

**Cameron Brown:** There's a Yoast plugin installed on our WordPress site that is organizing the sitemap into sort of like sections.

**Cameron Brown:** I don't want to appear contradictory because I've said in the past that you can only have one sitemap.

**Cameron Brown:** So that is still technically true despite it sort of appearing to have multiple here.

**Cameron Brown:** But anyways, the post sitemap is our blogs.

**Cameron Brown:** If you look at blog, if you search for the word blog, it's in every single one of these URLs.

**Cameron Brown:** So just the way that we're structuring our posts from the WordPress site, clearly posts are exclusively blog posts.

**Cameron Brown:** People who come from a WordPress background might understand why that distinction is important.

**Cameron Brown:** However, the important insight here is if we scroll all the way to the bottom to see the most recently modified blog in the sitemap, it was modified on October 24th, 2024.

**Cameron Brown:** So that is the most recent addition to the sitemap, and that all but confirms my theory that Webflow blogs have not been added to the sitemap since October 24th, 2024.

**Cameron Brown:** The reason why these blogs still perform well is because they exist on the new Webflow site under the exact same URL.

**Cameron Brown:** That's why they're still indexed.

**Ritesh Kewlani:** But how is that possible, Cameron?

**Ritesh Kewlani:** Growthx has been publishing new blogs every week with new URLs.

**Cameron Brown:** So the reason why is because the Yoast plugin on WordPress does a lot of the heavy lifting in terms of building the sitemap and structuring your SEO.

**Cameron Brown:** And every time you create a new blog post, Yoast automatically picks up the Slack, gives it a basic meta description, adds it to the sitemap, does all of the things that you probably would want a plugin to sort of handle.

**Cameron Brown:** And the plugin is installed on the WordPress site.

**Cameron Brown:** So every time we publish a blog on Webflow, Yoast has no idea anything changed, right?

**Ritesh Kewlani:** But these blogs are still getting indexed.

**Ritesh Kewlani:** We saw 80 to 90% of the blogs in the month of March getting indexed, having views.

**Ritesh Kewlani:** We are seeing current blog posts that are being published being indexed.

**Cameron Brown:** So there's a strong correlation between pages that exist on the sitemap and them having a likelihood of being indexed, but I don't necessarily think it's a requirement.

**Cameron Brown:** I think Google can index pages even if they don't exist on a sitemap.

**Cameron Brown:** Just really increases the odds.

**Jenn Peters:** Yeah, and just to add to that, like just because of the document that I said, like it's giving the impression that all the other ones in that column are indexed.

**Jenn Peters:** That's not the case necessarily.

**Jenn Peters:** I didn't go through every single post and check that they were all indexed.

**Jenn Peters:** I just checked the ones from March there that were zero because I wanted to check if that was the reason why.

**Jenn Peters:** So that's not to indicate that all the rest in that column are indexed.

**Jenn Peters:** If you went through a bunch of them, I can guarantee you.

**Jenn Peters:** And if you go through Google Search Console, you can see how many of your pages aren't indexed.

**Jenn Peters:** And, of course, a lot of those, like, you don't, if it's, if there's a valid reason, like, it's a redirect and you, you've de-indexed intentionally from those previous pages, that's, of course, you want to ignore those.

**Jenn Peters:** But just to mention that, like, yeah, there would be some across those that would not be indexed as well.

**Jenn Peters:** Yeah, Cameron, great insight.

**Cameron Brown:** Thanks.

**Cameron Brown:** Yeah, so for the team, I've already looked into what we could do in response to this.

**Cameron Brown:** I'm sort of starting from the point of assuming we can't just get rid of WordPress on any sort of short-term basis.

**Cameron Brown:** What can I do in the interim to improve our position?

**Cameron Brown:** I have done sort of a deep dive and I can manually structure the site map.

**Cameron Brown:** What I can do is go to WordPress, unpublish every single one of our blogs from a WordPress on the WordPress side.

**Cameron Brown:** Obviously, they'll still exist on Webflow.

**Cameron Brown:** I'm not gonna be undoing anything important.

**Cameron Brown:** What importantly that will do is Yoast will recognize, okay, Cameron just unpublished all of the site, all of the blogs.

**Cameron Brown:** We now no longer have a use for this post sitemap.xml file.

**Cameron Brown:** It will completely empty out.

**Cameron Brown:** Then what I will do, go to Webflow, export all of the URLs that our current blogs currently exist under and manually write all of the XML data and then upload it to the WordPress site.

**Cameron Brown:** But the problem with this is that's a lot of work.

**Cameron Brown:** And every time we publish new blogs, I have to manually update this XML document and then push it to the WordPress site.

**Cameron Brown:** So I'm willing to do that because I want to see improvement in this area.

**Cameron Brown:** I want to also show GrowthX that we're willing to sort of like work with you and do what it takes on our side of things.

**Cameron Brown:** And again, just want to reemphasize the best strategy here is to get off WordPress as soon as possible, and I can't stop stressing that enough.

**Megan Dickey:** And just to be clear, I think I'm not clear on why we, yeah, like, why can't we just move from WordPress to Webflow entirely?

**Megan Dickey:** Like, guess, like, what's stopping that?

**Cameron Brown:** A couple things. Internally, we've had discussions. I am trying to get our infrastructure team to help us move, because I think one, plan A is just lose the pages that aren't currently in Webflow.

**Cameron Brown:** Like, there's still a couple pages that need to be rebuilt.

**Cameron Brown:** I personally, I think this is still a larger conversation.

**Cameron Brown:** I'm okay with letting those free and just sort of, like, retroactively developing them as we have time.

**Cameron Brown:** The other solution is essentially reverse the hierarchy of how our site infrastructure is set up.

**Cameron Brown:** Right now, the WordPress site is kind of like the king or the parent, whatever analogy you want to use, and it's diverting traffic that it can't handle to the Webflow site.

**Cameron Brown:** And that's why the sitemap exists on WordPress.

**Cameron Brown:** We've kind of all been over this.

**Cameron Brown:** What I am proposing is rewrite all of our router rules on our Nginx server, make the Webflow site the primary domain, and instead have rules that point to the WordPress site for the few pages that are still existing.

**Cameron Brown:** The problem internally for you, GrowthX, is the people on infrastructure that I know well and have helped me in the past with this Nginx server no longer are with us.

**Cameron Brown:** So, I am trying to figure out a team owner of this project from the infrastructure side, but it sounds like that's going to be a challenge.

**Cameron Brown:** But anyways, I'm sorry I've delayed the conversation.

**Cameron Brown:** We've gone a little bit off track.

**Ritesh Kewlani:** No, so important and so interesting to me.

**Cameron Brown:** Yeah, this is kind of my number one priority.

**Cameron Brown:** I'm obviously still working on, like, landing pages because, again, that helps with the migration process, but I've really, in the past two days or so, been trying to see if we can do anything here, and essentially manually rebuilding our sitemap is what I've come up with.

**Cameron Brown:** It's possible.

**Cameron Brown:** It's just a lot of work, and every time we publish new posts, that's manual work on my end.

**Cameron Brown:** So there's a lot of trade-offs.

**Megan Dickey:** Yeah, I definitely think this needs to be a top priority, because then I think, then we'll have a better, a better idea of how content is actually performing once everything in the back end is actually operating properly.

**Megan Dickey:** Because, like, otherwise, it's like, yeah, like, we have, we have some data, we have some insights, but the insights that we pull from that data might, yeah, it could be wrong if, like, if we're not actually, like, letting the blogs, like, live up to their full potential.

**Megan Dickey:** So, essentially.

**Ritesh Kewlani:** So, Cameron, I have a suggestion. Before we undertake such a big project, I know it's a lot of manual effort to move the entire sitemap. Can we at least test out this theory?

**Ritesh Kewlani:** Because personally, I'm not feeling like 100% confident that this is the reason for a lot of these blogs not getting indexed. If what you're saying is true, can we start with, let's say, blogs for the month of March and quickly see if that is helping yield any results before we, like, my...

**Cameron Brown:** I can try something like that. One thing, I think GrowthX will probably back me up on it. We come from different perspectives here, and we have different motivations, but on this matter, I definitely trust the expertise on the GrowthX side.

**Cameron Brown:** You're right to say that it's not, like, if we do this, this will help. It's automatically fix everything, yeah. It's not helping, right?

**Cameron Brown:** One thing and I think we're all sure of is missing blogs that are not on the sitemap is surely not helping them be indexed.

**Jenn Peters:** Yeah, for sure.

**Jenn Peters:** I mean, like, of course, there's like so many different things that go into making a piece of content succeed, right?

**Jenn Peters:** But at the bare bones basic level, it had like the sitemap of a site and like canonical tags and like all of those types of things have to be, you know, correct.

**Jenn Peters:** And if I can go into any page that's not indexed and look at the source and see the canonical is not correct, then I mean, I think, yeah, I think like what you're saying, Cameron's right.

**Jenn Peters:** Like we all have different perspectives and we all, you know, it's not just going to be like a one fits all solution for every single piece.

**Jenn Peters:** But I think there's some pretty clear indicators we have here just from basic GSC, like scanning.

**Jenn Peters:** That's like, this is, I mean, and just look at the date that it has that, you know, that you have as a marker.

**Jenn Peters:** It's a pretty clear indication as this being like a big blocker, in my opinion.

**Cameron Brown:** Yeah, so I think we kind of are getting at two issues here, and I think for some pages, both issues might be the case, but that's why I think at least maybe you and I, Jen, should have a one-on-one, and just, if there's canonical issues on our landing pages, obviously the blog is important because it brings in so much new traffic to the site, but our landing pages are so important from a marketing perspective.

**Cameron Brown:** If there's something we can quickly do in terms of, like, let's spend half an hour looking into the canonical tag, see if I can do anything quickly, let's make progress in that area, and then I will work on, because I can do this independently, I won't need your help.

**Cameron Brown:** I essentially want to go through the list of unindexed landing pages with you, look at the canonical tag issues, see if I can fix them in real time, and then the second issue being the sitemap, I will do what you, Ritesh, Fathom suggested, and I'll create another essentially subsection of our sitemap, I'll call it like blog sitemap.xml, and then I'll add all the March published articles, or whatever month we choose, it doesn't matter, to that sitemap, and then we'll see if we see a bunch of them start to get better SEO scores, get indexed and GSC and things like that.

**Ritesh Kewlani:** Yeah, that sounds good.

**Ritesh Kewlani:** The only thing, Cameron, that doesn't give me confidence in this solution is when I look at the month of March, there are blogs that have done extremely well, like 80k impressions, 50k impressions, and so there is a lot of variation in terms of some blogs performing really well versus some blogs not performing at all, and I just want to make sure we are able to root cause this problem, because this is like, as Megan was saying, a lot the this is like absolutely critical situation for us.

**Ritesh Kewlani:** We need to figure out a solution to this problem. And if we all feel this is the right way to go about it, Cameron, you need to quickly test it out and let us know if it works. I would also recommend like Megan and Jenn, if you have somebody on the team who's an expert in technical SEO, we need somebody who can really help us out here because Cameron is not an SEO expert. He's a web developer. We don't have that resource on our team to be able to guide us.

**Ritesh Kewlani:** So at this point in time, we need somebody who can really look into this and help us understand, okay, this is what the next step should be. Do you have anybody on the team that you can probably bring on a call next week?

**Megan Dickey:** Yeah, yeah, we have. Yeah, you've maybe met Dave because he was actually the director on this account. But I don't know if then he kind of took over. So it was a little chaotic in that way. But he is like our SEO expert, I'll have to ask him if he's an expert on the technical side of things, but he would be, I think, our best bet in terms of, like, getting his insights.

**Megan Dickey:** And, like, and just to be clear, I mean, like, we're not saying that, like, we can't do a better job of having the right strategy, like, writing better content. Like, that is definitely, like, also a part of this.

**Megan Dickey:** And, like, even just, like, based on, like, the lead analysis that I did, it's, like, there are definitely some patterns in terms of, like, the content that, like, did drive leads versus did not drive leads.

**Megan Dickey:** And, like, and I think we're also just still not, based on that, like, content strategy that I laid out a couple weeks ago, like, we're still in the early phases of that.

**Megan Dickey:** And I do think that, based on the analysis that I've done, that it will ultimately help to drive more leads.

**Megan Dickey:** But, like, Ritesh, I know you had a concern that, like, yeah, like, some of that newer content wasn't really driving as many leads and like part of that could be could be around like the indexing issue but then the other part I think is also around the type of content that we're doing like there was a bunch of content in June that were like about tariffs and like even though that was like a really hot topic like it just it wasn't resonating with people like it didn't none of those posts actually drove leads so there was still also like a content element to this of course.

**Megan Dickey:** but like but then it's like once we really get that strategic content on the site then we also just need to make sure that we're like supporting it and setting it up for the best possible success.

**Megan Dickey:** it's definitely like they're a two a two part strategy I think is like kind of what we need to focus on moving forward.

**Megan Dickey:** The technical side and then the content side of course.

**Cameron Brown:** I have a question to Ritesh's point. I think at this point, it's just like a general curiosity. I think we can sort of leverage the insights later. But if it is the case that we have published some articles in March and they are doing well, we now know with confirmation I just showed you guys, they're doing well in spite of not existing on the sitemap.

**Cameron Brown:** So I would only assume, you know, I think it would be somewhat unexpected if we add those articles to the sitemap and they do worse. I think that's probably something we can almost guarantee.

**Cameron Brown:** But it does make me ask the question, what is Google valuing? Because they're evidently subpar from the SEO positioning perspective.

**Cameron Brown:** What is making that content, those posts do well in spite of that, that might be a valuable insight going forward in terms of, you know, let's fix the site map, of course, but if it's doing well in spite of this, like, subpar positioning that we're facing right now, then let's do more of that, right?

**Cameron Brown:** What is the, what is that cause?

**Cameron Brown:** That's kind of, I'm just curious.

**Jenn Peters:** Yeah, for sure.

**Jenn Peters:** I think we'd have to spend a bit more time digging into these top performing and kind of looking at, you know, a little bit more, like, if there was traffic peaks, you know, during that time and, and kind of, like, see if we can collate any kind of trends around those topics and see if, if there's particular things we can, can glean from those.

**Jenn Peters:** But yeah, I, I agree with you.

**Ritesh Kewlani:** And I think one, one more thing we need to look at is also understand how many of these blogs actually led to form fills. We're just looking at clicks and impressions.

**Megan Dickey:** Yeah, we actually do have that actually from, Jen, if you wanna just pull up, it's in the Notion doc.

**Jenn Peters:** There it is. Leads Analysis, yeah?

**Jenn Peters:** Yeah.

**Megan Dickey:** Okay, let me know. Can you all see this?

**Jenn Peters:** Yep, yes.

**Cameron Brown:** Cool.

**Megan Dickey:** Yeah, so, okay, I'm just supposed to pull it up on my screen. Yeah, so, so basically, I looked at, of all the posts that we published in April, May, and June, including posts that we refreshed, so like, in April, seven newly published blogs resulted in eight leads, and May, two newly published blogs resulted in three leads, June, two refreshed blogs led to eight leads, but no, none of those newly published blogs in June led to leads.

**Megan Dickey:** And like, and as I said, like, there was, there was a lot of content around tariffs, and like, that just didn't do well.
