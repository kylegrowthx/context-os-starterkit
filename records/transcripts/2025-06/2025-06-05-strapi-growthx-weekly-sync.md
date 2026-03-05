# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-06-05
time: 16:32 UTC
duration: 29 minutes
organizer: Sydney Go
participants: Sydney Go, Jason Gong, Usman Ghani, Paul Bratslavsky, Theodore Onyejiaku, Victor Coisne, Golzar Yaghoubpour
fathom_recording_id: 66747243
fathom_url: https://fathom.video/calls/318590728
share_url: https://fathom.video/share/MQajiEzBe6qU9EBkkVeNCWncaXD4Jy34
source: fathom
enriched_on: 2026-03-03 15:45 UTC
</metadata>

---

## Summary

Strapi and GrowthX discussed strong content performance — articles gaining impressions, CTR up — with a production plan of 10 blog articles and 10 integration pages weekly, plus a focus on use case articles and SEO-optimized content. The team committed to a strategy pause the following week to audit keywords, investigate integration page traffic decline, and implement LLM tracking for ChatGPT and Perplexity to identify how Strapi is cited in AI responses. GrowthX outlined three content distribution priorities: automated social media drafts for LinkedIn and Twitter, Medium publishing automation via API (highest priority to save Theodore time), and video-to-blog conversion workflows.

---

## Context

Strapi is a headless CMS platform and a GrowthX content marketing client. This weekly sync is part of an ongoing engagement focused on content strategy, SEO performance, and content distribution. Sydney Go (GrowthX) leads content operations with Jason Gong (GrowthX strategy) and Usman Ghani (GrowthX) supporting. On the Strapi side, Paul Bratslavsky (likely product or marketing lead) drives priorities, Theodore Onyejiaku (content) handles execution, Victor Coisne (analytics/strategy) tracks performance metrics, and Golzar Yaghoubpour manages CTAs and funnel reporting. The team has been publishing heavily (10 articles + 10 integration pages per week) and seeing early wins with new content ranking well within days of publication.

---

## Relevance

**To GrowthX Delivery:**
- Volume production (20 items per week) plus strategy pause shows disciplined agile delivery — test, analyze, then optimize. Applicable to other content clients.
- GA4 funnel tracking tied to CTA text is a measurement pattern worth replicating; Golzar's approach to tracking personalized CTAs through common text is clever standardization.
- Integration page performance decline requires investigation: distinguish between re-crawl lag and actual ranking loss. Victor's hypothesis about Google re-indexing is testable with Search Console data.
- Meta description and title tag optimization workflows (pixel-based limits vs. character counts) — Strapi uses pixel limits (550px titles, 680px descriptions), audits recommend character limits (65 chars for title, 160 for description). Worth documenting as a QA template.

**To CheckThat:**
- LLM tracking implementation for ChatGPT and Perplexity citations — up to 100 prompts across 2 LLMs. This is direct CheckThat / AI visibility use case; product-market fit validation on a tier-1 B2B SaaS client.
- Strapi content regularly cited in LLM responses (Jason observed old Strapi forum posts driving answers). LLM tracking will quantify this and flag stale content to refresh.

**To GrowthX Business Development:**
- Strapi shows strong engagement: weekly syncs, strategic pauses for optimization, investing in automation (Medium API plugin). Signal of account health and expansion potential.
- Requested three new initiatives (social drafts, Medium automation, video-to-blog) with clear time-saving ROI (Theodore spends 20-30 min per Medium publish). Can be upsell or retention lever.

---

## Overview

- Content performance is strong: articles gaining impressions, CTR up, new articles ranking well; listicles and AI-related content performing best
- Production plan: 10 blog articles and 10 integration pages per week, prioritizing use case articles, SEO-focused content, and developer-focused articles
- Research sprint planned for strategy optimization, including LLM tracking (ChatGPT and Perplexity citations), keyword cannibalization analysis, integration page traffic investigation, and workflow upgrades for images and FAQs
- Content redistribution initiatives discussed: automated social media post drafts for LinkedIn and Twitter, Medium publishing automation via API (highest priority), and video-to-blog conversion workflow

---

### Content Performance and Production

Sydney reported strong week: articles gaining significant impressions and CTR increases. Investigation showed listicles (top 10 websites, best AI security tools) and trends articles driving performance. Articles published in January-March are now ranking for target keywords. Two use case articles already published and performing well. Current production: 10 blog articles and 10 integration pages per week. Next week: pause production to conduct strategy review. Future focus: use case articles, SEO-focused how-tos (e.g., "How to Build Tools for E-Commerce"), and developer-focused content.

### Content Strategy and Optimization

Planned two-week strategy sprint: pause production, implement LLM tracking for ChatGPT and Perplexity, conduct keyword cannibalization analysis, and investigate integration page traffic decline (Victor noted month-over-month decline despite new updates). Jason will roll out LLM tracking around June 16 with up to 100 prompts across two platforms. Workflow upgrades for images and FAQs approved and ready for implementation. Integration pages being updated gradually by Theodore; Paul confirmed others tasks take priority.

### CTA Strategy and Analytics

Discussion on use case article CTAs: decision to keep "Try a live demo" rather than test signup CTAs. Victor noted CTAs don't perform well generally, so sticking with demo CTA. Sydney personalizing CTAs per article while maintaining the "demo" text for GA4 funnel tracking consistency (tracked by button text). Golzar will update funnel report with common text from personalized CTAs.

### Technical SEO

Theodore flagged title tags and meta descriptions need tightening per audit recommendations: titles should not exceed 65 characters (for SEO friendliness), meta descriptions max 160 characters. Sydney currently uses pixel-based limits (550px for titles, 680px for meta descriptions, using Mangles tool) to prevent mobile truncation. Agreed to adjust going forward.

### Content Distribution and Repurposing

Three priorities identified:
1. **Social media automation:** Auto-generate LinkedIn and Twitter post drafts for each blog article to reduce manual work
2. **Medium publishing automation (highest priority):** Theodore created a Strapi V5 plugin to publish articles to Medium via API; GrowthX to build workflow in AirOps. Currently takes 20-30 minutes per article to manually handle Medium's formatting issues. API approach will save significant time.
3. **Video-to-blog conversion:** Convert video content (community talks, smaller Strapi Conf talks) to draft blog posts for repurposing or expansion

Paul noted they republish on Medium, Dev.to, and Daily.dev for reach (get 1,000-2,000 reads per month). Canonical URLs point back to Strapi blog. Jason raised concern about canonicals not preventing cannibalization edge cases but agreed the reach benefit outweighs the risk if managed carefully.

---

## Action Items

**Sydney Go (GrowthX)**
- Track performance of integration pages; connect with Theodore for list of updated pages, add to library studio
- Add relevant images to use case articles after research phase

**Golzar Yaghoubpour (Strapi)**
- Update GA4 funnel report flow with common text from personalized CTAs

**Victor Coisne (Strapi)**
- Review and edit LLM tracking prompts list, add evaluation phase questions if needed

**Theodore Onyejiaku (Strapi)**
- Send Medium API details and plugin information to Jason/GrowthX team via Slack

---

## Transcript
**Paul Bratslavsky:** Fathom, you're like 10 minutes away from me.

**Paul Bratslavsky:** We should get a coffee sometime.

**Golzar Yaghoubpour:** How long are you here for?

**Sydney Go:** I'm here till September, but I'll be back in December.

**Sydney Go:** Okay, yeah, we should definitely get a coffee.

**Sydney Go:** Yes, we should.

**Sydney Go:** I'll message you privately.

**Sydney Go:** That'll be fun.

**Sydney Go:** Awesome.

**Sydney Go:** I didn't know you were in Vancouver.

**Sydney Go:** That's really cool.

**Sydney Go:** So how's everything going?

**Sydney Go:** Good.

**Sydney Go:** Thanks for sending the free read.

**Sydney Go:** I was happy to read that.

**Sydney Go:** Sorry, was trying to send it a little bit earlier, but if someone gets away from me.

**Sydney Go:** Okay, so we actually have really good results this week.

**Sydney Go:** Our articles have started really gaining impressions.

**Sydney Go:** Our CTR is up.

**Sydney Go:** Everything is doing really well.

**Sydney Go:** I dug into a little bit deeper, like what produced that increase in impressions and the increase in CTR. I'm looking at our top performing content. And contributing to a lot of listicles, so top 10 websites, and I think the trends article is also somewhere up there, so top 10 websites, best AI security tools, so we're going to definitely add those to our next round of ideation, seeing if we can, if there are more listicle opportunities that we can do, and especially with AI, because I think that's really where the space is at at the moment.

**Sydney Go:** And then the articles that we published last week are already ranking for some good results.

**Sydney Go:** If it says not found, that means that we don't have, it doesn't have a keyword yet, but that was also published a couple of days ago, so it's not a surprising result.

**Sydney Go:** We also, yeah, so everything's doing well, and the articles that we published in January to March are already starting to really, really ramp up and get all those top keywords that we want, so, so far, everything is looking great.

**Sydney Go:** And yeah, we really appreciate the big push on publishing last week, I think that really contributed to this as well.

**Sydney Go:** For our production this week, plan to get you 10 blog articles and 10 integration pages, as always.

**Sydney Go:** And then next week, we're going to do the same before we pause production for a little bit to really dig into our strategy and then double down on what's working as well.

**Sydney Go:** Currently, we are working on the use case articles that you sent over last week.

**Sydney Go:** We published two.

**Sydney Go:** They're performing well, so I think it is a good opportunity to flesh out that pillar as well.

**Sydney Go:** And then we're also working on some more SEO-focused and developer-focused articles.

**Sydney Go:** So how to build tools for e-commerce platforms, website personalization.

**Sydney Go:** So a little bit of marketing and developer.

**Sydney Go:** And then I saw that Paul also looked through the new ideas that we had last week and approved some of them.

**Sydney Go:** So I'm adding those to our pipeline for development as well.

**Sydney Go:** Do we have any questions on the performance and production side?

**Sydney Go:** That looks pretty good.

**Victor Coisne:** Yeah, I know.

**Victor Coisne:** I'm very happy with everything.

**Sydney Go:** And then, so looking forward for next week, I remember that integration pages were mentioned last week.

**Sydney Go:** I have not seen them in our content OS, so I just wanted to see if it's anywhere else that I've missed.

**Sydney Go:** I think I was talking to Theo, or Golzar Theo, last week about this.

**Golzar Yaghoubpour:** I think the last thing was that we had a backlog to work through, so I don't know, Paul, if you have an update.

**Paul Bratslavsky:** Yeah, so basically the updated integration pages, we're slowly adding them, well, at least the updates to Strapi.

**Paul Bratslavsky:** We just have other things that we're prioritizing for this week and next week, so we're just doing a few at a time, but our goal is to work through the best.

**Paul Bratslavsky:** Okay.

**Paul Bratslavsky:** all the updated ones.

**Paul Bratslavsky:** Okay.

**Sydney Go:** Yeah.

**Theodore Onyejiaku:** And remember, you shared a link.

**Theodore Onyejiaku:** So I'm working with the link to the Notion document you shared with me.

**Theodore Onyejiaku:** Okay.

**Sydney Go:** And the Notion document works fine.

**Sydney Go:** There's nothing you can do to help you guys in a part?

**Sydney Go:** No, no, no.

**Paul Bratslavsky:** Like, I'm okay with it now.

**Theodore Onyejiaku:** Like, I've started, like, updating the previous integration pages so that we could have the new updates.

**Theodore Onyejiaku:** Okay.

**Sydney Go:** Awesome.

**Sydney Go:** Okay.

**Sydney Go:** And then there are no new integration pages that you want us to go through because I went through our OS.

**Sydney Go:** And it looks like there are some in draft that were never...

**Sydney Go:** Um, fleshed out.

**Sydney Go:** I think this was, um, still from, um, I actually don't know when this is edited, I'm not going to lie.

**Sydney Go:** Um, so let me know if you want us to work on these, um, or do you prioritize them?

**Sydney Go:** I think because they're all, like, low priority, they're, like, three, tier three, uh, like, maybe just pausing, uh, on them.

**Paul Bratslavsky:** like, a couple of things I wanted to kind of, like, mention, like, I know we have a lot of content and we wanted to kind of figure out, uh, some strategies for redistribution, something that could make it easier for you and I, and then that's something to talk about, uh, and I could save that for a little bit later, uh, because I'm not sure if you have any other topics that you want to mention, first.

**Paul Bratslavsky:** Okay.

**Sydney Go:** Uh, okay, so, uh, so, uh, as I mentioned earlier, we're, oh, not sharing, right screen is what we're doing, sorry.

**Sydney Go:** All right, back to the, um, so we're, we're going to start working on the use case articles.

**Sydney Go:** So, thank you, Golzar, for sending those.

**Sydney Go:** We're going to start on that this week and hopefully get PDDs by Friday.

**Sydney Go:** We already have the LMS one, the Learning Management System one.

**Sydney Go:** I think that's been published.

**Sydney Go:** And I think I did target the keyword online learning system there as well as a secondary keyword.

**Sydney Go:** But if it doesn't rank, then we can add that in.

**Sydney Go:** Victor, sorry, I saw your hand out.

**Victor Coisne:** I have a question around integrations, but maybe finish and I'll talk about integrations.

**Victor Coisne:** Okay.

**Sydney Go:** So we put the data from the how to build a blog and then how to build an LMS.

**Sydney Go:** And it looks good.

**Sydney Go:** So we are going to get more granular.

**Sydney Go:** Like this might have a little bit of overlap with the how to build a blog article, but getting more granular should help with not duplicating content and competing with the same keywords.

**Sydney Go:** Yeah.

**Sydney Go:** So I think that's it.

**Victor Coisne:** So for my question on integration, I want to get a sense of how that's performing from a search standpoint, like seriously what we do for the blog and kind of keywords ranking, trying to get a sense of how that works for the integration page.

**Victor Coisne:** If we do like a month over month analysis, I just did the number, but if I look at Google Analytics, the blog, the number of users actually went up, but page view went down.

**Victor Coisne:** On the blog, it's still kind of growing the number of users that's kind of like a good trend.

**Victor Coisne:** Overall, the integration, though, is actually decreasing.

**Victor Coisne:** So I'm wondering if it's because we're kind of changing a lot and changing a lot of the content, and therefore we need some time for Google to kind of re-crawl and re-index that content before we see it ranking. I think it would be good to kind of track performance on the integration pages specifically.

**Victor Coisne:** Yep.

**Sydney Go:** So I think we just started, correct me if I'm wrong, but I think we just started uploading those this week.

**Sydney Go:** Is that correct?

**Sydney Go:** You mean the integration pages, right?

**Theodore Onyejiaku:** Yes.

**Sydney Go:** No, this week, this week.

**Sydney Go:** This week.

**Sydney Go:** Okay.

**Sydney Go:** So I'll connect with you to see which integration pages have been updated.

**Sydney Go:** And then I'll get that going in our library studio as well.

**Usman Ghani:** Okay.

**Usman Ghani:** Thanks.

**Usman Ghani:** That's all right.

**Sydney Go:** Okay.

**Sydney Go:** Thank you.

**Sydney Go:** I have a question about the how-to articles, the use case ones.

**Golzar Yaghoubpour:** And I may have just forgotten.

**Golzar Yaghoubpour:** What is the CTA that you're adding for these articles?

**Golzar Yaghoubpour:** I think we've been using the demo one.

**Sydney Go:** The demo?

**Sydney Go:** Okay.

**Golzar Yaghoubpour:** Victor, what do you think about pushing people to sign up instead of the demo for this, or at least for the ones that the sales team had requested?

**Golzar Yaghoubpour:** Or we can A-B test it.

**Golzar Yaghoubpour:** Shall we say that one more time?

**Golzar Yaghoubpour:** So, Sydney said that CTA for the use case articles is the Launchpad demo.

**Golzar Yaghoubpour:** And I was thinking maybe we should change it to sign up for CE on some of them, or we can A-B test it.

**Golzar Yaghoubpour:** Like, Sydney can keep the demo, and we can A-B test it on the pages that the sales team had requested first.

**Golzar Yaghoubpour:** I honestly don't think it's worth doing an A-B test.

**Victor Coisne:** I think we have other A-B tests that should take priority over this. What we saw is those CTAs don't perform really well anyway. So yeah, trying a live demo is fine with me.

**Victor Coisne:** Okay.

**Sydney Go:** Okay.

**Sydney Go:** I did look at the, how to build an online, a learning platform.

**Sydney Go:** Oh, wait, this is the wrong one.

**Sydney Go:** Yeah, and I think that we can start getting images into these as well.

**Sydney Go:** If, after the research that we plan to do, and I know Jason, I think I saw you add an image to some of the other articles, so I'm going to add those in after. I have been trying to customize the CTA, so instead of just having "Try a live demo," I've changed it to something more specific to the article. Through the how-to articles, I think I did "How to Build Your Blog," just trying to keep the common CTA text so it doesn't break the tracking.

**Sydney Go:** So, yeah.

**Sydney Go:** Thank you.

**Golzar Yaghoubpour:** So, thank you for sharing that because the way that the funnel report is pulled in GA4 right now is based on the text of the button.

**Golzar Yaghoubpour:** So, but I think the most, are you still using the demo in the CTAs?

**Golzar Yaghoubpour:** Or if you're personalizing it fully, we'll do a different way with the funnel report.

**Golzar Yaghoubpour:** I've been keeping this part, the exact same because I don't know.

**Sydney Go:** perfect.

**Golzar Yaghoubpour:** I'll just update the flow then with like the similar text or text that they all have in common.

**Theodore Onyejiaku:** Okay, just a comment.

**Theodore Onyejiaku:** The titles, they often don't have "Strapi" in them. Is there a reason for that? Like, the heading for this CTA, this one has Strapi mentioned, but some don't — like "Try the live demo" doesn't have the Strapi keyword attached to it. Is there a reason for that?

**Golzar Yaghoubpour:** That was, I think that was the text given to us, though, don't know that, I pulled it from a document, but, um, yeah, that was, That's what was provided, um, that's what was provided to the GrowthX team when we originally made the CTA document in Q1.

**Golzar Yaghoubpour:** And, and to your question about the reasoning, I don't, there wasn't, like, a specific reasoning, we were trying to just keep the, the CTA language as, um, short as possible, but that didn't perform very well, so this may perform better.

**Golzar Yaghoubpour:** Yeah, so this is, um, I did test it to see if it, if it works.

**Sydney Go:** right.

**Sydney Go:** That's

**Sydney Go:** With the preview thing.

**Sydney Go:** Yeah, should see if it does work.

**Sydney Go:** So it did.

**Sydney Go:** If you want me to change this back, I have been personalizing them a little bit.

**Sydney Go:** No, keep doing what you're doing.

**Golzar Yaghoubpour:** And we can keep the demo CTA for now, for all the how-tos.

**Golzar Yaghoubpour:** Yeah.

**Golzar Yaghoubpour:** Okay.

**Sydney Go:** And then I know, Theodore, you wanted to talk about meta descriptions a little bit. So I'll just show you. What we do is we run the titles and the descriptions through this Mangles tool to make sure we're keeping the title tag within 550px so our articles don't get truncated on mobile, and our meta description at less than 680px so it doesn't get truncated on mobile either.

**Sydney Go:** Yeah, I get your point.

**Theodore Onyejiaku:** It's just that based on the audits so far, absolutely.

**Theodore Onyejiaku:** Like the one Golzar shared with me, it's recommended we keep it to the character length of 65 for the title, then for the meta descriptions, 160 characters.

**Theodore Onyejiaku:** So like most articles, I try as much as possible to make it at least not exceed the 65 character lengths for SEO friendliness.

**Theodore Onyejiaku:** So I was like, I've been seeing more with character lengths that are very, very long.

**Theodore Onyejiaku:** So I brought it to your attention.

**Theodore Onyejiaku:** Okay, awesome.

**Sydney Go:** I'll double check on new articles coming through to make sure they meet the standards.

**Sydney Go:** Okay, and then I think that's it from me and Jason. I know you have some thoughts on the research sprint. Jason, can you walk through that really quick?

**Jason Gong:** Yeah, basically Sydney is doing an incredible job on all the content.

**Jason Gong:** I've been thinking more just on the strategy side.

**Jason Gong:** So basically, the week after next, we want to focus on these four things, like less on production of content and just kind of one, rolling out the LM tracking.

**Jason Gong:** So with this, I did a first pass.

**Jason Gong:** We'll look for you guys to take a look.

**Jason Gong:** Essentially, these are just going to be the prompts that we track to see, one, if you're being mentioned, and then two, for the response, the LM is reporting.

**Jason Gong:** And we're mainly just going to track ChatGPT and Perplexity, like what are the citations that are driving the answer.

**Jason Gong:** And then we'll use that to prioritize content. So take a look at this.

**Jason Gong:** Basically, almost everything is kind of product evaluation awareness, like kind of in the layer of the funnel where people haven't really decided to use any platform yet, and they're just trying to find the best one.

**Jason Gong:** And then, wait, I just heard a sound.

**Jason Gong:** I wasn't sure if somebody raised their hand, but feel free to just cut me off if you have a question.

**Jason Gong:** But, yeah, so this is probably where we're focused, because that's where most of our content targets.

**Jason Gong:** But I think it is worth for you just to chat through, I guess, I'm not sure who on your team thinks through product marketing, but more at the, like, evaluation phase.

**Jason Gong:** Like, maybe somebody's asking, like, can Strapi do this?

**Jason Gong:** Or, like, how much does Strapi cost?

**Jason Gong:** Or, you know, like, questions like that that we don't really produce content for, but you guys probably think more about.

**Jason Gong:** Because we can add those prompts in here as well.

**Jason Gong:** And those are actually really useful to track.

**Jason Gong:** For example, with other customers, we've seen old forum posts from years ago driving answers about the product. It'll help you clean things like that up. How many prompts can we track? I can already think of a few I want to add.

**Victor Coisne:** Yeah, let's limit to a hundred for now.

**Jason Gong:** I don't have a great answer for the exact limit, but let's do a hundred for now.

**Jason Gong:** If you have like way more than that, let me know and let me see what we can do.

**Jason Gong:** Basically, we're, I mean, the cost to us is number of projects, number of prompts, and number of platforms to track.

**Jason Gong:** So I think we're trying to keep that within reason.

**Jason Gong:** Generally, we're doing a hundred in total for now.

**Jason Gong:** So that's across Perplexity and ChatGPT. Review that and let me know. The 16th is when I'm going to try rolling all this stuff out. So the main thing is LLM tracking.

**Jason Gong:** We're going to upgrade our workflows to push some of the stuff we've been testing into production, like images and FAQs.

**Jason Gong:** We're already, I think, approved all the templates we showed a week or two ago.

**Jason Gong:** So we have everything we need from you guys.

**Jason Gong:** This is probably another huge bucket of work for Sydney to drive just on keywords, seeing what's cannibalizing, surfacing kind of like what the more important pages are, like what you brought up around integrations.

**Jason Gong:** I'm going to assume what's happening because I remember the last time I looked at it, you have like five pages that I think drive about almost all the traffic to that part of your website.

**Jason Gong:** And probably just some of the bigger ones are declining in traffic.

**Jason Gong:** So just looking into why — is it a ranking thing or are fewer people searching for those topics? Maybe search volume is shifting to LLMs, figuring out stuff like that.

**Jason Gong:** And then some of the insights we get from tracking the prompts, it'll show us basically, here's the type of content that steers a lot of the answers to the prompts.

**Jason Gong:** And for questions like, do we have that content?

**Jason Gong:** If yes, is it ranking?

**Jason Gong:** If no, what can we do to make that better?

**Jason Gong:** And then the last thing — we haven't forgotten — is you guys asked if we can add a step to our workflow to have pre-created social posts for some articles. That's something I'm going to look into as well.

**Jason Gong:** We still have some time on this call.

**Jason Gong:** Maybe just, like, we could spend five minutes chatting about that.

**Jason Gong:** It's, like, which accounts, what the main goals are for you guys, you know, on socials, essentially.

**Paul Bratslavsky:** Yeah, I could start with that.

**Paul Bratslavsky:** So our goal is to create better quality content with a broader focus.

**Paul Bratslavsky:** Create better quality content, and then instead of producing more content, focus on redistribution.

**Paul Bratslavsky:** So try to figure out how to make existing content that we have, and repurpose it to different platforms.

**Paul Bratslavsky:** The three areas that we kind of want to spend some time in, I'll start with the socials, is for every blog post that we write or produce internally, it would be nice to have automated drafts of social posts created for LinkedIn and Twitter.

**Paul Bratslavsky:** Those would be like the first two I would start with, that will make it easier.

**Paul Bratslavsky:** Second is we do republish content, like for instance, if Theo has an article that he writes, he also repurposes to Medium, and that is very tedious to do manually.

**Paul Bratslavsky:** And so what we wanted to do is create a workflow through AirOps where after we publish an article, there's an automated flow that publishes it to Medium via API. That's easier than manually copying and pasting and figuring out the formatting.

**Paul Bratslavsky:** That would be like the second kind of option because right now it takes a decent amount of physical time to do that.

**Paul Bratslavsky:** And that's very monotonous and time wasteful.

**Paul Bratslavsky:** And that way Theodore could spend that time doing something more valuable.

**Paul Bratslavsky:** And then the third item I would add to that is something that we mentioned before as an action item is to have a workflow that takes video content and converts it to the first draft of a blog post that then we could either finish ourselves or republish.

**Paul Bratslavsky:** Because we have, for instance, from Strapi Conf, we had a lot of smaller community talks.

**Paul Bratslavsky:** And it would be nice if we could just pass that video and have it create, like, a summary blog post of what was talked about that we could repurpose either to write a full blog or, like, whatever.

**Paul Bratslavsky:** So those would be, like, the three things that come to immediate things that would be helpful for us.

**Paul Bratslavsky:** Okay, that makes sense.

**Jason Gong:** This Medium one, so what exactly are you doing there?

**Jason Gong:** Are you just publishing the exact same article?

**Jason Gong:** And then does Medium have this way of like pointing back to the one on your website and saying like, that's the canonical version?

**Jason Gong:** Yes, exactly.

**Paul Bratslavsky:** You should share the canonical URL and I'll let you see or actually talk about it because that's the one that experiences the pain at the moment.

**Paul Bratslavsky:** Okay, I think you probably shared the details.

**Theodore Onyejiaku:** Basically, when we publish an article, we would want to share it on Medium, Dev.to, Daily.dev, and the rest.

**Theodore Onyejiaku:** So Medium in particular, it doesn't support Markdown.

**Theodore Onyejiaku:** And when you do, it's supportable.

**Theodore Onyejiaku:** When you import the Markdown file, it kind of gets disarranged.

**Theodore Onyejiaku:** You have to, you know, take more time to make sure everything is okay.

**Theodore Onyejiaku:** And when you copy and paste the published post to Medium, you also get the same issue, unlike Dev.to, which requires that you just paste.

**Theodore Onyejiaku:** The markdown from Strapi, and make sure everything is looking good, and then you publish.

**Theodore Onyejiaku:** So when we publish to these platforms, we also add the canonical URL pointing back to Strapi, the original Strapi blog post.

**Paul Bratslavsky:** So the issue is right now it's so time-consuming. There's a Strapi V5 plugin someone created that makes sharing to Medium much easier by repackaging the Strapi markdown article into an API call to Medium directly.

**Paul Bratslavsky:** That will all do it in one shot.

**Paul Bratslavsky:** In AirOps, we could have a workflow where we share a link of a Strapi article and click a button that automatically publishes it. That will save a lot of time for Theodore because it currently takes 20 to 30 minutes of manual work per article. That's such a wasteful place to spend time.

**Jason Gong:** So the reason you post on Medium and Dev.to — is it just for reach? Are you getting organic traffic from their recommendation feed?

**Theodore Onyejiaku:** Yeah, it's for reach.

**Theodore Onyejiaku:** And for most of our audience, we use Medium and Dev.to. Monthly, we get thousands of reads — maybe 1,000 to 2,000 reads. So they're performing well, and we want to keep that going.

**Jason Gong:** I ask because I've seen another customer do this with Dev.to and it was somehow cannibalizing their blog.

**Jason Gong:** I know they have a canonical tag, but canonical tags don't guarantee that the main version ranks. You always find edge cases.

**Jason Gong:** But I guess for getting organic traffic, it might be worth the cannibalization risk. We can set it up so Medium publishes as a draft first, and you click a button to publish. That should be straightforward as long as the API allows it. I'll chat with our team about adding that.

**Jason Gong:** Let's see.

**Jason Gong:** Video content.

**Jason Gong:** This one, let me get back to you on.

**Jason Gong:** I know we have something, but I don't know if it's like something we're maintaining at the moment, but we should have something for that.

**Jason Gong:** And then Twitter and LinkedIn.

**Jason Gong:** Let's see.

**Jason Gong:** Is this for your company account, Paul, or how do you think about who should post?

**Paul Bratslavsky:** So basically when an article is ready to share, we create social posts for the Strapi company account.

**Paul Bratslavsky:** So it'd be nice if we have just a bunch of drafts that are generated, you know, based on the resources that we provide it.

**Paul Bratslavsky:** That makes it easier so we're not starting from scratch.

**Jason Gong:** Got it. I'll follow up with you in Slack about what accounts and voice you want for those posts. We can get that in a good place.

**Jason Gong:** Okay, well, I think all these are doable.

**Jason Gong:** I think let's try to see if I can cram it into that week.

**Jason Gong:** But the main focus for me is rolling out LLM tracking and some of the lower-hanging fruit like images and FAQs that we know will improve content production. I think I'm pretty clear on everything we have to do.

**Jason Gong:** Any other questions?

**Paul Bratslavsky:** I'm just going to say as a note, if you have to pick one thing to prioritize, I think Medium Automatic Publishing would be the best because it physically takes time to do that could be spent somewhere else, you know?

**Paul Bratslavsky:** So to me, I think if he could get back some of his time as a star, that would be amazing.

**Paul Bratslavsky:** Okay, that's probably the easiest one to do, honestly.

**Jason Gong:** How does it work for Medium in Dev2?

**Jason Gong:** Can you just give us an API key or add us as a manager on the account?

**Jason Gong:** I'm not super familiar.

**Jason Gong:** Yeah.

**Paul Bratslavsky:** So Theo created a plugin, and I guess he could just send you all the details in Slack.

**Paul Bratslavsky:** I know we are at the time, but it's basically you have to communicate with the API, and you have a key.

**Paul Bratslavsky:** Theodore can send you all the details about the plugin since he created it.

**Jason Gong:** Great. Anything else before we wrap up? Okay, I'll wait for you guys to review and edit the prompts, then I'll try to get everything set up for next week so we can see what the LLM tracking is showing.

**Victor Coisne:** Cool. Sounds good. Thanks, everyone. Bye.

**Paul Bratslavsky:** Thanks, everyone. Bye.

**Sydney Go:** Bye.
