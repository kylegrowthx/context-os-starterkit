# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-04-30
time: 16:31 UTC
duration: 45 minutes
organizer: Sydney Go (GrowthX)
participants: Victor Coisne (Strapi), Paul Bratslavsky (Strapi), Theodore Onyejiaku (Strapi), Golzar Yaghoubpour (Strapi), Sydney Go (GrowthX), Jason Gong (GrowthX), Usman Ghani (GrowthX)
fathom_recording_id: 60061286
fathom_url: https://fathom.video/calls/289329889
share_url: https://fathom.video/share/k_MdUJay7PksQppEwGEGoEivQRHVjipe
source: fathom
enriched_on: 2026-03-04 19:53 UTC
</metadata>

---

## Summary

GrowthX and Strapi aligned on three core content initiatives: improving Strapi's fact-checker to catch technical nuances (beyond Strapi-specific features), rolling out a new comparison page template optimized for SEO with consistent Strapi inclusion and architectural-level features, and building out long-tail use-case content targeting keywords like "LMS," "e-commerce," and niche verticals to showcase Strapi's versatility. The teams agreed on workflow standards (Markdown drafts via Notion/Hack.md for existing content, direct CMS entry for new content) and discussed a curated content approach where GrowthX pulls multiple existing resources to create higher-volume, trend-aware articles.

---

## Context

Strapi is an open-source headless CMS that competes with platforms like Contentful, Directus, and Sanity. This is an ongoing weekly sync between Strapi's product and marketing leadership (Victor Coisne, Paul Bratslavsky, Theodore Onyejiaku, Golzar Yaghoubpour) and GrowthX's content strategy team (Sydney Go, Jason Gong, Usman Ghani) to execute Strapi's content marketing roadmap. GrowthX handles all content creation, SEO optimization, and delivery while Strapi provides product expertise and strategic direction. The engagement includes content production (blog articles, integration guides, comparison pages), SEO ranking optimization across Strapi's target audiences (developers, DevOps, content teams), and workflow improvements. StrapiConf, Strapi's annual conference, is happening in two weeks and will announce a new "Strapi AI Architecture" feature that generates content models from prompts—which opens new opportunities for use-case templates and demonstrations.

---

## Relevance

**To GrowthX Delivery:**
- Strapi's new AI Architecture (launching at StrapiConf in 2 weeks) creates a scalable path for generating use-case templates and demonstrations—potentially a repeatable content model for future clients in the headless CMS space
- Workflow standardization (Markdown via Notion/Hack.md for drafts, direct CMS entry for new content) improves collaboration efficiency and reduces revision cycles
- Curated content approach (pulling 3-5 existing resources to create single synthesized articles) is a new delivery method that increases output volume while maintaining quality—applicable to other clients

**To CheckThat / AI Visibility:**
- Strapi fact-checker is working but limited to Strapi-specific features; opportunity to explore how CheckThat's capabilities could catch nuanced technical issues (legacy code patterns, performance implications) that LLMs miss
- Comparison pages are a major ranking opportunity and CheckThat could help verify competitive claims remain accurate as competitor features evolve

**To GrowthX Business Development:**
- Account health signals are positive: multi-month engagement, expansion beyond initial scope (new comparison template, long-tail use cases, curated content workflows), and strategic alignment on upcoming product launch
- Strapi is investing in infrastructure (Airtable consolidation, discussion of automatic data updates) suggesting commitment and budget for long-term partnership
- Potential to showcase Strapi as reference case study—particular strength in long-tail vertical SEO (LMS, e-commerce, internal tools, niche builders) demonstrates differentiation vs. competitors
- Paul Bratslavsky's emphasis on workflow standardization and content oversight suggests strong operational discipline on Strapi's side

---

## Overview

- Strapi fact-checker working well for Strapi-specific content; exploring solutions for web developer knowledge gaps
- New comparison page template proposed; discussing implementation and maintenance strategies
- Focus on long-tail use cases for Strapi to showcase versatility and improve SEO rankings
- Exploring curated content approach for blog posts to increase volume and quality of published articles

---

## Key Topics

### Strapi Fact Checker and Content Accuracy

  - Fact checker effectively catches Strapi-specific content errors
  - Exploring solutions for highly technical web developer knowledge gaps
  - Currently using human reviewers to catch nuanced technical issues
  - Theodore's technical expertise valuable for content review

### Content Production and Workflow

  - Some articles published, others in progress
  - Discussing draft creation process in Strapi CMS
  - Agreed to use Markdown format for content drafts (e.g., Notion, Hack MD)
  - Exploring options for maintaining comparison page data (spreadsheet vs. Airtable)

### Comparison Page Template and Performance

  - New template proposed with structured sections (overview, CMS comparison, feature breakdown)
  - Discussing inclusion of Strapi in all comparisons for consistent referencing
  - Aiming for balance between maintainability and SEO optimization
  - Considering architectural-level differences rather than feature-level changes for evergreen content

### Long-tail Use Cases for Strapi

  - Opportunity to showcase Strapi's versatility through specific use cases (e.g., LMS, e-commerce, internal tools)
  - Discussing approach: individual templates vs. collections of use cases
  - Short-term focus on identifying and prioritizing high-volume use case keywords
  - Leveraging new Strapi AI Architecture (announcing at StrapiConf in 2 weeks) to generate use-case content models and examples

### Curated Content Approach

  - Proposal to create articles by synthesizing 3-5 existing resources from multiple sources
  - Aim to increase content volume and quality while maintaining relevance
  - Discussing workflow for suggesting and approving curated content ideas
  - Adding "inspiration articles" column in Content OS to provide curated resource recommendations

### Content Approval Process

  - Clarified workflow for approving topic ideas in Airtable
  - Options to mark topics as "approved" or change status to "ready to start"
  - Theodore responsible for reviewing and approving new content drafts in Notion

---

## Action Items

**Theodore Onyejiaku (Strapi)**
- Review new content drafts in Notion

**Sydney Go (GrowthX)**
- Send integration page drafts via Notion/Hack.md moving forward
- Resend Airtable link for content ideas to Strapi team
- Send keyword research and ideas for LMS and other top use cases next week

**Paul Bratslavsky (Strapi)**
- Start thread in group Slack channel, loop in Maxim (Strapi dev) re comparison page structure, data maintenance, and potential Airtable integration vs. spreadsheet approach

---

## Transcript

**Theodore Onyejiaku:** Good.

**Sydney Go:** Is it just us today?

**Usman Ghani:** I think Victor should jump on.

**Paul Bratslavsky:** Let me see.

**Jason Gong:** Yeah.

**Paul Bratslavsky:** He should jump on.

**Paul Bratslavsky:** Maybe he's running a little bit late, but we could probably start.

**Sydney Go:** Okay. So I have a couple of updates for you guys. I'm really sorry, I didn't finish that, but I'll add that in later. So quick content updates for this week. Our Strapi fact checker is working, but I know Theodore, you brought up a couple of limitations or errors that we had in our articles.

**Sydney Go:** Our Strapi checker, basically my understanding is correct, goes through the articles and checks for Strapi-specific content. So if there's anything wrong with what we talked about with Strapi's offerings or Strapi's features, then it will catch those details. But we're still looking for a solution for how to catch very specific web developer knowledge gaps. So I think you called out code for React JS, is that correct?

**Victor Coisne:** That's correct.

**Jason Gong:** Like, I think it's actually the one you caught was really interesting, and I spent a bunch of time with our engineering team figuring that out. It's like a bit legacy code—it still works, it's not necessarily wrong, but it's not something you would try to promote, right? Because it's supported but legacy, and for stuff like that, we're currently solving it by having a developer review to try to catch stuff like that. Then I think we're trying to figure out a version of the fact checker that can pick up stuff like that, because we ran it with the current one and it doesn't pick up things like that, you know, because it's really nuanced.

**Theodore Onyejiaku:** Yeah, and I think it's not just for React, okay. Like for most technical content, I think we could also extend the fact checker to give us codes that are like up to date or current, although like you said, we probably aren't promoting them. So yeah, but I would love it if it's more accurate.

**Jason Gong:** And how did you catch that one in particular? Like, are you a frontend developer, Theodore? It feels very, very technical.

**Paul Bratslavsky:** You might not know it, but he built some projects before with frontend and Strapi. He tried to have developers on our marketing team to help with that stuff.

**Jason Gong:** Well, yeah, I mean, just want to let you know we're working on it. That one is honestly pretty tricky that we're trying to figure out. Right now we're just using humans to try to catch it.

**Sydney Go:** Okay, and that's the update for the fact checker. So for content production this week, we sent over a couple of articles, and I know a couple of them are published. We only have three that aren't published so far.

**Sydney Go:** I did want to ask, is there a way for me to create drafts in the CMS? So if the integration page is published, can I rewrite the data and say that it is a draft?

**Paul Bratslavsky:** After it's published, currently, you're not able to do that. If you make changes and you click Save, it will auto-publish the new changes.

**Sydney Go:** Okay, so can I then send the integration pages to you, like through Google Docs as we've been doing, and then you can check it for me, and then I can upload it? Or how do you guys want to do that?

**Paul Bratslavsky:** Yeah, what would work best? I feel like if we are able to have you expecting the review first.

**Theodore Onyejiaku:** Yeah, I think we just have it in one place, which is Strapi, so that when you're done I could review them. This is for existing content.

**Paul Bratslavsky:** So that's like a new integration. Do you prefer using the draft in Google Docs or do you prefer a spreadsheet feel?

**Theodore Onyejiaku:** I prefer it to be in Markdown. If Google Docs supports it or preferably Hack.md.

**Sydney Go:** Okay. I can send them over via Hack.md then moving forward. That's good to know.

**Sydney Go:** Okay, and then the next thing I wanted to show you guys is about the comparison page template proposal. Before we do that, I wanted to show you the performance of your comparison pages. These are three avenues that we want to go for: new content optimized, integration pages optimized, and finally optimized comparison pages.

**Sydney Go:** So here is your dashboard. This is your comparison page performance over the last month. You are getting clicks and traction. Your average positions aren't bad for your comparison pages. But the thing that's holding your comparison pages back is that there's not a lot of content there. So if people click to see a table, they go. Which isn't a good signal to Google. So I worked on your comparison page template this week.

**Sydney Go:** Just a quick overview of who the two CMSs are. In this case, I decided on two non-Strapi CMSs so you could see how we plan to integrate Strapi in. The headline can change any other way, and then the subtitle is right there up front. This should ideally have a very specific plus point for either Strapi or the CMS on page.

**Sydney Go:** This is where your CMS comparison will come in. Before everything, all of this content will be keyword optimized. It's going to be very short as well. And then for the structure, you have "What should you choose between the two?" and then right at the bottom, "Why Strapi is still the ideal alternative," so if people get this far, you might as well plug in Strapi.

**Sydney Go:** There are some sections that we're not 100% sure on. For example, "How they perform in action" will probably be Strapi only. So if it's Strapi versus Contentful, then you'll have this section. But if it's Contentful versus another CMS, we won't have the same because it doesn't make sense and just adds noise.

**Sydney Go:** For the feature breakdown, we could have a table and also content in text. So the question I have for you is: can you have a table on the page, or would it just be better if we gave it to you as text instead? Both work fine SEO-wise.

**Paul Bratslavsky:** So I do have to double check with my team because I believe the data gets pulled from the Excel spreadsheet that I shared with you for the comparison. I'll have to check to be sure, and I don't think there's a way of doing things. We would have to kind of talk to Maxim or another developer who's helping us with the website to see how quickly they could update this to be able to have this as Markdown.

**Victor Coisne:** Hey Paul, let's start a thread on the group channel and loop in Maxim so that you can just chime in right away. Yeah, I think Maxim was the one who implemented it. The reason we did it with a spreadsheet is for ease of maintainability. Like if we move away from that spreadsheet, it becomes a bit harder to update. And another piece of feedback is that I think in the table we should always have Strapi as a column. That way people are always referencing Strapi regardless.

**Sydney Go:** Awesome. Yeah that makes sense. We want to stop Strapi from being excluded from the get-go, because the quick comparison right at the top is what I assume is what you're pulling from the spreadsheet. So if there is a way for us to create content around that spreadsheet, that would be the ideal way to do this. You have basically your time to value. This is your most valuable thing, right up top, and it's always going to be updated. And then everything else, we try to make it as evergreen as possible. So the feature breakdown probably won't change.

**Victor Coisne:** The features change quite a bit, that's the thing that changes.

**Sydney Go:** Yeah, but we can try to make it as general as possible. We don't want a feature breakdown if we don't need to have that part either. So you can just have, very quickly, "Which should you choose?" and then some best use cases, what we're going to go for. That way, you don't need to change much.

**Victor Coisne:** I think where you had that, we can make it so that it's not really in the weeds of the feature, but more like the architecture level. There's some fundamental differences that are not going to change.

**Jason Gong:** I mean, I think one thing is, once we understand how this all works with the info getting pulled in, is think about how we could even help keep that updated, like with browser agents and scraping and workflows. I think how up-to-date the information is will probably factor into how these rank. I think there is some complexity to getting that to work, so we can make that a V2.

**Victor Coisne:** I even see some stuff where our features are not up to date. So I want to make sure we have this internally. It should be owned by Nicholas, who's a product marketer. That's kind of a product marketing topic for competitive battle cards. We use the Google Doc right now.

**Paul Bratslavsky:** Is that still the best mechanism to use or would something like Airtable make it a little bit easier, especially if you're thinking of doing something where you auto-scrape and update the information?

**Victor Coisne:** We could. If you guys tell us, it would be a lot easier to maintain if we move the table to Airtable. We can do that, that's no big deal. Let's start that thread, let's see how you guys are doing it now, and then we can figure it out.

**Jason Gong:** Airtable definitely would work better, but I know we use Airtable and we pay so much money to them, we almost don't want to recommend it. So we can figure it out.

**Sydney Go:** Okay, the last thing that I wanted to share with you guys is for next week. Currently we're working on all the articles that Theodore sent into the chat. We did some keyword research on those as well to make sure that we're really targeting the right keywords and intents with our articles. These are the current ideas that are in Airtable. I'll send you the OS again, and you can definitely see them and just tell me or highlight which ones you think will work best.

**Sydney Go:** For the integration pages, I appreciate if you tell me which ones you want me to work on first this week. If all of them are good, then we'll start working on all of them this week. If not, then we'll pick the next 10 that look good to work on. I remember you saying last week that Gatsby wasn't the best example to present, so it'd be nice if you can tell us which ones work best.

**Sydney Go:** For comparison pages, we can start generating the articles before we have the infrastructure set in place so that we can just plug it all in as soon as it gets going. Or we can also put that on hold depending on what you guys want to do. But basically these 10 comparison pages that I pulled out, I got them from your Looker Studio report—the ones that are currently getting a lot of impressions, the top 10, so that we can start working on those and hopefully get more impressions to those as well.

**Usman Ghani:** Yep, that makes sense.

**Victor Coisne:** I think we'll get a better idea of the page structure once we have that thread going. You could start generating the content, the high level stuff that's not feature related. I think we can get started with that. One thing that came to mind for me and Paul is for the content, the new articles. I think we have an opportunity to play with a long tail of use cases for Strapi. It's one of the big benefits of Strapi is how versatile it is compared to other systems that are a lot more opinionated, and so that makes it a good fit for things like quizzes, LMS, or all kinds of internal tools. So I think there is an opportunity there to try to rank for some of the use cases. Because we don't really do use cases justice on our website. We have high level ones, it's just like talking as if all websites are created equal. But it's not the case. People actually look for software that are more bespoke to a specific case.

**Victor Coisne:** I shared earlier, and I can share it again with Paul. I shared in Slack. We have it for the record. This is actually from our competitor, Directus. And they have this pretty cool blog post that lists about 100 different use cases categorized within different app categories. So I think just to start, but I feel like it would be good to lean in on that because the intent that we would capture—folks that have software for LMS, I'd love to Strapi to rank for those keywords.

**Jason Gong:** I've seen there's like an awesome Strapi repo, and I see you have a showcase on your website now. Like for you, where does this fit in that kind of structure?

**Victor Coisne:** So we have a showcase—actually websites I've built using Strapi. It's kind of like a portfolio. We don't think many people use it and that's a different thread we should make sure it's easier. Right now people have to submit a pull request, it's a little bit not super intuitive. Okay, the awesome repo has been used to, that's how we started like five years ago, but we don't really use it anymore because a lot of those things on that awesome repo actually have been moved to the site. So in there you have a lot of plugins. Now we have a plugin marketplace. So yeah, that one's deprecated. The other one is not deprecated, but not very accurate.

**Jason Gong:** I'm trying to think about this. The showcase is like complete websites, but like personally, one of the use cases could be like as simple as a logo carousel, where the logos sit in like some CMS collection within Strapi and then you're giving somebody an example of how they would do that.

**Paul Bratslavsky:** I think the goal is, let's say I'm a user and I'm building something and I want to build a product e-commerce store. And you kind of have like the long tail, like search for—you know, Strapi, well, maybe not Strapi, but e-commerce. Or someone's like, I'm building a yoga studio app or something that's more specific to a niche product they're building. To showcase that could be used for it. So sometimes people might search like web builder or hotel website template. Like the idea is to have it more specific to hit long tail words where someone who's thinking of building something might search whatever that need is, and then we want to be able to rank for that stuff.

**Paul Bratslavsky:** So the goal is, let's say someone's searching for how to build an e-commerce store, and you kind of describe how they could use Strapi as the backend for that. That would be very useful. And ultimately, yeah.

**Jason Gong:** Oh, I was gonna ask like, for these pages, what would you imagine the experience is for the user? Would there be a path for them to kind of spin that up with Strapi? Or is it more just informational, like, hey, you're building an e-commerce site, here's how you do it using Strapi? Because like to me, I don't think you could have a frontend without having a backend, and Strapi is a backend. So it's like when someone's building an LMS, yoga studio app, a map, whatever app that tracks dog walkers. It's like the idea is that you could talk about that use case and all of that could be powered with Strapi. And I think that's what's cool about Strapi—it's so versatile. Like you could use it in so many different use cases that some people might not even be aware of.

**Paul Bratslavsky:** So like the idea is think of any app idea, like Strapi could be the backend for it.

**Jason Gong:** I think I want to untangle the intent because like we have Bolt as our customer. And for them, what we're doing is like, you want to have this template marketplace, right? It's full of a bunch of stuff. And then I think usually how those are set up is like you just have a crazy long tail. There's a lot of duplicate stuff like that. But then the stuff that ranks in a lot of cases is like the collection. So like, oh, here's a collection of portfolio websites, right? And then under that will be literally like a hundred portfolio websites that individually would not rank. Same as how Webflow does it. Like none of their templates rank, it's like a collection. So you're kind of almost setting up this like template marketplace thing. That's one way of like going after this kind of template, and then yeah, but I guess, you know, you guys don't necessarily have that yet, and I don't know if it makes sense to do that. So let us think about how to do that.

**Victor Coisne:** The way I think about it in the short term is like maybe we can do a crawl, walk, run kind of approach. What we discussed here, I think it's a longer term work stream where we need to sort out like whether we want to invest in this because there are a lot of other pieces to it. I think it's more of a longer term goal. In the short term, what I would suggest is treat it at an tactical level. Let's identify okay, what are like some of the top use cases, keywords that already rank? For instance, LMS is starting to become a bigger, bigger use case for us. We're starting to sign customers that have LMS driving their interest. LMS systems like traditional ones are ripe for disruption. So I think there's opportunity. Let's identify where those use cases are in volume, and then prioritize a couple of articles that try to rank for those keywords. I think it's a quick win in the short term until we build the bigger.

**Sydney Go:** OK, we'll send over some keyword ideas so we can get that started next week.

**Sydney Go:** Awesome. OK, and we're at time, almost three minutes. Usman, did you have a quick question?

**Usman Ghani:** I did have a quick question.

**Paul Bratslavsky:** So I just want to make sure that everybody in terms of work deliverables is on the same place. So it makes it easier for everyone to manage stuff. If it's content that already exists, you guys just going to create the draft in Notion and share it with Theodore. But if it's new content, I think the easiest thing to do is actually add directly in Strapi, where Theodore could work on it right from there. It just makes it much easier. So I just wanted to reiterate that.

**Paul Bratslavsky:** And then another thing—a while ago, we kind of talked about creating curated content. So having three or four different types of resources, like a YouTube transcript or two blog posts, and kind of using that to generate articles. Is that something that we're able to start doing now?

**Jason Gong:** So for that one, you would provide the kind of seed material—here's a YouTube video we made, or here's a webinar. It could be like any content.

**Paul Bratslavsky:** And this was a conversation we started before Jason joined. So maybe in the transition, it just wasn't mentioned. But the idea was, so I don't know if you're familiar with NotebookLM. It's a Google thing which allows you to point to five different resources and they'll generate an audio like podcast. So like we want something similar for like blog post writing. So that way, sometimes like we might not have like an original idea, but we'd look at four different articles that were like oh, would be kind of cool and useful for our community. And so like give you those three resources to write an article based on curated content. And it doesn't all have to be Strapi, but I think it ranks them, you know, drive them.

**Jason Gong:** Um, and then in terms of like how it's you, they're you still thinking for kind of SEO or what is it more would it be more for like something else?

**Paul Bratslavsky:** I believe it's still for blog writing. It's just basically instead of coming up with an idea where you have like a main idea you pass it to like the AI and the AI writes the article based on whatever the key concept of this idea is. We want to have a curated approach where we could point to five, four, three different resources and it creates a whole new article based on that. And again, it could be something that could bring added value. So that way, it's not just original articles written by AI based on one theme, but it's curated content that may be trending. Like for instance, maybe there's four different articles in four different places, but it all makes sense to be like a cool like one blog post.

**Jason Gong:** Right. Interesting. Yeah, I mean, we can explore that. Conceptually, anything could be an input creating a piece of content. Like for other customers, like we ingest like white papers and podcast transcripts and YouTube transcripts. Right. But I guess if you have like a specific idea, maybe to share that and then we can go from there. Because I guess typically how we do the SEO part is like we have an intent. You know what your product does and we just kind of research that space to see what keywords are there and then we just write for those.

**Paul Bratslavsky:** So yeah I guess like for me like it would be like you know you make content that's about the product but you make content that may be trending or is kind of like discoverable content that may not be specific to Strapi but you know that other people are searching. And then you know so that's kind of like the idea. So you have these buckets. One is like this is about the product. Two is like this is for a current user. Three is like this is for discoverability specifically to get people to come to the website. Just think out loud but that would be like the idea. Like so sometimes when I use Twitter as an example, like sometimes I find content where it's like someone made a post but it's like curated content of some interesting things and I'm like oh that's kind of cool. Then you get interested in that person or so like do something like that for our blog and website.

**Jason Gong:** Maybe we could like do another call and we can like dig a little deeper. I mean it sounds like pieces of it is like right now we don't really have like a live feed that kind of is like time sensitive. Like for example if something goes viral on Twitter about some concept, you know like we want to have a listen. It doesn't have to be like that crazy.

**Paul Bratslavsky:** It's just like you know, we saw few cool articles that we thought would be interesting for our community and so we want to use those those datasets to create a whole new article which is curated content that could rank for, let's say we saw something interesting about Bolt versus V0 versus whatever. Instead of like, basically combine those together and create a new article that covers those topics in a curated way.

**Jason Gong:** You just want a way to drive the types of content we're publishing a little bit more. What would that look like just in the channel if you just throw on, hey, here's some cool things we read recently. Would that be your interface with us?

**Paul Bratslavsky:** From your standpoint, it's how you build the tool. For instance, I did this for my own personal project where I'm just able to point to four or five different documents and it will just auto-generate a summary of those things with key research and sourcing topics. He and I are doing stuff, but sometimes it's not just us coming up with these ideas. Sometimes it's just cool stuff is already happening, and there's already content around it, so source that content to create curated content that we could add as additional content on our website, so that we could increase the volume of how much stuff we're posting.

**Jason Gong:** Yeah, I think I'll understand it a little bit more of what exactly you mean, because there's different purposes for publishing. SEO generally tries to make sure that we're not publishing duplicate stuff for a particular topic that maps to a keyword and search intent, and then there's other purposes like topics that are just interesting and time-sensitive that might not rank like that but you want to publish as well.

**Paul Bratslavsky:** So what I've seen, I forgot what website it was, but they literally had like a resource. It's also a headless CMS company, but they just published content on, you know, if you do something similar, like server-side rendering or like something like this, like, they're trying to hit as many keywords. And so, the idea is creating content around, like, some sort of, like in this case, like you're telling us what to publish or. So when I think of curation, so sometimes, like, let's say I want to search something, and I like, I gotta go there, I gotta go here, I gotta go there, I gotta go here. And then sometimes you just have a blog post that's just like all the things that are interesting in the space that I'm interested in in one place. Like it's basically content that would be interesting for like stuff around frontend development stuff around Tailwind. But the idea is that stuff picks you know couple of different resources and writes that article about it. It's like oh yeah, yeah, okay, I think I finally know it. Instead of like kind of what we do now, like we take all this and we kind of repackage it as our own. But instead you're looking for almost like an article that's like a gateway or like a kind of like a collection of things. Like, hey, if you're interested in this, go here, here's what it's like. Not necessarily kind of like almost way label it, but point to these nice kind of existing resources.

**Jason Gong:** I think what Paul is trying to say is that let's say we are writing an article on Next.js optimization or performance, so we want to like get the best examples. Like I have a good taste in like what it means to like write well for this, like only based on you know documentation from this site. Yes this resource that resource like don't kind of go everywhere. I mean like transparently you know what we do is like we kind of take a topic, we break it down, and then you're right, we use the combination of like deep research, searching, scraping to come up with like the base, I guess building blocks to then create the article. Yeah, I think what you're looking for is the ability to like kind of for all of us to steer that a little bit more like, hey yes, you know, only use Wikipedia as Strapi documentation or whatever it is.

**Jason Gong:** Exactly yeah that's what I meant by curation. But okay, I've got it. So we're kind of carrying away this. Probably a different conversation. Yeah, exactly. Yeah, yeah. So I think we might even figure out if we don't have like, I'm trying to think of the right interface for this. I can only have our content OS and all the keywords in it in there that could be one, or like if you just dump it to Slack, we can figure it out. But one way we could do this is like, we have a key. And then we could just add a column and it's like, you know, what do you think are the best resources that cover this today, and then we can kind of like narrow what we use like in our research, you know, to come up with our version of that article. Like with that, you think with that covers what you're thinking.

**Paul Bratslavsky:** In terms of like, if it fits, you know, exactly, like picking five different resources and benefiting new content from it, yeah.

**Jason Gong:** Okay. So okay. And then we should also have one where like, it's not necessarily writing an article. You just think like, these are good and useful. And then, you know, you give us the resources and then we figure out what the output is. Because I guess like, usually for this SEO stuff, you're writing for a certain intent for a search, that's probably what steers it more than anything. But I guess like the idea would be like, you know, we talk about making sure like we have more quality. The articles and sometimes if you have certain datasets that are already automatically in the workflow and to do the best that you can, but sometimes you're like, oh, well, we're writing an article about Next.js, next year's just improved their documentation. I want you to use their improved documentation for this particular article. So that's like idea for us to be able to pick and choose a little bit more.

**Jason Gong:** Like you said, have a little bit to that. Yeah, we, these conversations are really helpful. We already try to figure out how we can only use stuff that's published in last six months and then only code based on official documentation. Yeah, and the goal is not for every article, but when it makes sense, because it's a high level, we're adding that layer in. It sounds like you guys just have good ideas and you read things for that as well. So I don't know exactly what that flow looks like. Maybe for now, like, if you see a topic that we're going to publish soon and you have opinions on like, hey, based on this, you can either throw it in Slack or just type. I think we would call them if not, we'll add it in the content OS. Then that's what we get, so we'll kind ahead. Yeah, so I think it'll be a great idea.

**Paul Bratslavsky:** It's like, to add a column in Content OS, top, like article you're working on, we could add additional resources that could kind of help you get, you know, fine-tuned a little bit.

**Jason Gong:** Yeah, and then I think on the new content idea side, I think Theodore, you know, does a really good job. Like, he's always sharing kind of ideas for new things to publish. Like feel free to do that as well. When you do, if you share a little bit more about like, where the idea came from, what you think is a good resource that covers that topic, we can also factor that in what info we use to like generate the article. You think that would work.

**Theodore Onyejiaku:** Yeah, I think so.

**Paul Bratslavsky:** We could add that extra thing in the content OS and we could start doing it right away just to kind of give you the little bit more direction with recommended resources. I added the URL in.

**Sydney Go:** It's right beside the assignment status. It says inspiration articles. And if anything is set to 03 generating article generation, that means that we're already working on it. If it's an 01 considering, that means this idea is for you guys. If you want to approve it, goes to ready to start. And if you want to add ideas at the ready to start stage, you guys are approving networks as well.

**Theodore Onyejiaku:** Sorry, I want to understand. I was trying to approve some topics today, but I wasn't so sure, although I saw the colon for approve or reject something. And like okay let me confirm yeah approve yes or no so if that's where i should go like when i go to considering i could approve the or should i go to ready for publish?

**Sydney Go:** Yeah, so I think there was a misunderstanding when this board was set up. So the view that I'm on actually has that column hidden. So I'll just unhide it for me and then I'll put it to the next stage. Thank you for doing that. Okay, it is something like this: like if you want me to approve some topics, how do I do that? Because I know I asked before. And yeah, yeah, this this works if you want to just add the topic approved it works if you want to change the assignment status to ready to start, that works as well. It's entirely up to what's more convenient for you.

**Theodore Onyejiaku:** Okay, cool, thank you. Thank you.

**Sydney Go:** Okay, so I'm so sorry for taking over 15 minutes of your time, but as really productive chat and we have a lot of ideas for next week and we're excited to get those started. Is there anything else?

**Paul Bratslavsky:** I just want to say one last thing. If you have any questions just ping me directly. I'm here to help with whatever you need to help us keep moving forward.

**Paul Bratslavsky:** Okay awesome thank you thank you so much.

**Sydney Go:** Thanks, thank you. All right, thanks for coming.

**Jason Gong:** Bye.

**Jason Gong:** Bye.
