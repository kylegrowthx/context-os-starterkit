# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-04-23
time: 18:01 UTC
duration: 33 minutes
organizer: sydney@growthx.ai
participants: Sydney Go, Jason Gong, Usman Ghani (GrowthX); Golzar Yaghoubpour, Victor Coisne, Paul Bratslavsky, Theodore ONYEJIAKU (Strapi)
fathom_recording_id: 58814999
fathom_url: https://fathom.video/calls/282969848
share_url: https://fathom.video/share/kj8Ze5gUWCeB1Bce-Yy34n1YRCEFDq3T
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

GrowthX and Strapi aligned on a major content and UX push, bringing on Usman Ghani as a dedicated content manager to boost quality and accuracy. The team launched an image generation workflow to enrich blog posts and discussed a social media strategy focused on developer audiences via Twitter (deep technical content) and LinkedIn (founder-led thought leadership). Integration page restructuring is underway to improve CTAs and scannability, with the top 10 pages getting immediate attention.

---

## Context

Strapi is a headless CMS platform serving developers and enterprise teams. This is an ongoing engagement where GrowthX handles content marketing and SEO strategy for Strapi's public website. The weekly sync focuses on content delivery, product integration coverage, and how GrowthX can help Strapi reach and engage its developer community. Usman's onboarding as a dedicated content manager signals a scaling in delivery volume and quality expectations.

---

## Relevance

**To GrowthX Delivery:**
- Scaling content production requires dedicated staff augmentation; Usman's arrival (7 years tech content strategy) indicates potential for expanded output and client focus on accuracy
- Image generation workflow represents a new service offering for enriching blog posts and content refreshes
- Integration page restructuring is a systematic, repeatable template-based approach that could become a reusable methodology for similar clients

**To CheckThat:**
- Strapi's integration pages are SEO-critical; CheckThat audits could reveal AI visibility gaps for Strapi vs. competitor headless CMSs
- Developer-focused content strategy on Twitter/GitHub could be tracked for AI mentions and community engagement signals

**To GrowthX Business Development:**
- Strapi is expanding content team capacity (new hire + production tracking), signaling account growth and renewal confidence
- Partnership potential: Strapi references GrowthX CMS recommendations to prospects; discussion of co-marketing via Strapi's partner program
- Integration page performance data suggests opportunities to quantify ROI on content restructuring (CTR improvements)

---

## Overview

- New content manager (Usman) joined GrowthX team to improve content quality and accuracy for Strapi
- GrowthX introducing image generation workflow and social media offerings to enhance Strapi's content
- Integration page performance analysis reveals opportunities for format unification and content restructuring
- CTA placement and design to be optimized for better conversion (minimal, inline CTAs preferred)

---

## Key Topics

### Content Team Update

  - New content manager (Usman) added to GrowthX team
      - 7 years experience in content strategy for tech companies
      - Focus on improving quality and accuracy of Strapi's content
      - Expertise in technical concepts and developer-focused writing

### Image Generation and Social Media Strategy

  - New image generation workflow in development
      - Uses intermediate configuration to assemble images (similar to Figma)
      - Will be integrated into content refreshes, especially for blog posts
  - Social media strategy recommendations:
      - Twitter: Focus on deep, technical content for developer audience
      - LinkedIn: Potentially leverage founder accounts for developer-focused content
      - Suggestion to create ghost-writing service for founders/leaders

### Integration Page Performance and Improvements

  - Current performance metrics:
      - React CMS and Next.js pages driving most traffic
      - Other integration pages have low click-through rates
  - Proposed improvements:
      - Unify format across all integration pages
      - Restructure content to prioritize key information (e.g., why use Strapi with specific integration)
      - Add contextual CTAs and social proof
      - Consider using toggles for detailed information to improve scannability

### CTA Optimization

  - Move inline CTA higher up on integration pages
  - Use minimal, text-based CTAs instead of purple background versions
  - Explore possibility of contextual, automated CTA text generation

### Content Production Tracking

  - Team to provide regular updates on:
      - Number of articles delivered per week
      - Remaining backlog
      - Potential bottlenecks in content production

---

## Action Items

**Jason Gong (GrowthX)**
- Create X (Twitter) social media strategy for Strapi founders, focusing on deep technical content for developer audience and community engagement
- Touch base with Daniel (Strapi design) to gather brand guidelines and finalize image generation workflow integration

**Sydney Go (GrowthX)**
- Update top 10 integration pages with new format: one-liner value prop, brief intro, "why use Strapi with [integration]", CTA, social proof, how-to integrate section
- Send list of content produced this week and remaining backlog to Victor by end of call
- Send new batch of topic ideas for Strapi approval later today or tomorrow
- Share Looker reports access in Slack channel
- Refine content workflow to ensure CTAs are included in all new content
- Request access to Figma design files for CTA components

**Golzar Yaghoubpour (Strapi)**
- Update CTA component in Strapi to allow inline placement higher on integration pages (Notum web agency has completed technical work; Golzar to implement)
- Change all existing CTAs to minimal version in content (text-based, no purple background)
- Share CTA component Figma file and implementation instructions with Jason and Sydney

---

## Transcript

**Sydney Go:** Sorry, give me five seconds.

**Sydney Go:** Jason's going to be here in a little bit and I'm just pulling up your meeting notes.

**Sydney Go:** I know the first part of your meeting notes, Jason was the one who filled out.

**Sydney Go:** Actually, sorry, before anything, we have a new content manager on your team so that we can start actually creating content for you quickly and more accurately because it's when it's got a really developer background and what we really wanted to double down on is if it was on quality of your content and accuracy, if your content to make sure that content that ranks gives you a good reputation online.

**Sydney Go:** So Usman, do you want to introduce yourself before we get started?

**Usman Ghani:** Hi, everyone. So I'm pretty good with technical stuff.

**Usman Ghani:** I have seven years of experience in content strategy and writing for companies like Atlassian, Stream, Pipeline, Zendesk, etc.

**Usman Ghani:** So I think I can help with your technical concepts and yeah I can work with you.

**Sydney Go:** Okay, so when Jason hops in a little bit, he's currently in San Francisco.

**Sydney Go:** Yes, all right.

**Sydney Go:** I was just going to say that when you hop on, walk everyone through our new image generation workflow and some of the social offerings that we have.

**Jason Gong:** When we start with that, and then I think you probably went through it already. But what I'm kind of getting at is how we want to start enriching and bringing quality to some of the integration pages.

**Jason Gong:** But I'll start with the image generation piece since I don't know if you've been thinking in that realm.

**Jason Gong:** Yeah, this is a need from a lot of our customers. One of the best ways to get content ranking is to have rich multimedia. A lot of your content could use that, and it'll help it rank.

**Jason Gong:** The problem with just trying to generate images in ChatGPT is it's not there yet. It's in this weird uncanny valley — it gets really simple things wrong, and you have to manually catch and fix them. We don't want that.

**Jason Gong:** So what we've built is to show a peek under the hood. What we're doing is not generating the image directly, but we generate the intermediate configuration to assemble the image. So there are tools out there — we use Playwright and similar ones — where you use code to tell it what you want to assemble, and then it assembles it for you almost like in Figma. Then we screenshot it and deliver the final image.

**Jason Gong:** So images are images and text is text. We hook this up in your content management where you give it an article or a paragraph, think about what the graphic should be, and then generate it. This isn't trained on your brand guidelines yet, which is something I'll ask you about after this call — whether you have a Figma file or other specs. But basically, what we'll have soon is something that can generate branded graphics like this for all your articles.

**Jason Gong:** So what we'll do after that is layer this into our refreshes — especially for the blog, we'll start including these branded graphics.

**Jason Gong:** That's coming down the line. We're piloting it with a few folks right now. When we refresh an article, we want this to be part of it. For now it's included in everything we do.

**Jason Gong:** That's image generation. Any questions on that?

**Jason Gong:** Let's move on to socials. This is general advice based on what's been working. We have a work stream around ghost writing for mostly leaders and founders of companies.

**Jason Gong:** People follow personalities. Someone on the last call asked what company accounts should be doing. The thing is, for there to be engagement, you have to create a personality for your company account. It doesn't have to be provocative or pointed in any way, but that's what people want to follow.

**Jason Gong:** On Twitter, a tactical example: you guys have highlights of Strapi plugins. What you can do is go deeper. Your audience on X is developers. They want to see what's under the hood. They want to hear from somebody with authority on the technical space.

**Jason Gong:** Instead of surface-level posts, go deeper — how does this plugin work? How do you integrate it? What can you do with it after that? It's more work, and we can help generate it. Vercel does this really well. They have a bigger following, but when they talk about an update, they create a whole thread going deep. They talk about technical details that a marketer wouldn't even understand.

**Jason Gong:** So that's the audience on X. For LinkedIn, it's more about non-technical audiences that you guys also target. If I were to automate anybody's account or get them to post more, it would be the founders like you, Victor. The way to think about what to say there is be transparent about your journey, your customers' journey, and just share. We basically figure out what that looks like for each person — we'd create a brand voice for Victor as a CMO talking about Strapi. What would that look like? What would you say? What's your cadence?

**Jason Gong:** Yeah, yeah, it's me raising my hand.

**Victor Coisne:** That makes perfect sense. Paul isn't on the call, but this is something we've discussed already. We've shared feedback with our social media person about what we could do better.

**Victor Coisne:** Yeah, very aligned on Twitter and the principles you've highlighted. For LinkedIn though, we're still primarily going after developers. So as much as I'm on board with building my personal brand, it would make sense to have the founders who are developers — myself and Aurelian — build following there, since developers are still our primary champion audience.

**Victor Coisne:** The marketers and content managers are secondary personas for us. I'm on board with doing that. If we can add it as a work stream, it's super relevant. It makes more sense to start with the founders.

**Jason Gong:** Yeah, we can share more there. I get that developers are developing it. If your primary audience is developers, we wouldn't use LinkedIn for that. But I know you guys are getting more into cloud, and you have a demo form. I assume it's not developers filling that out. So maybe that's a space for later, but I wanted to highlight it. If anyone should be on LinkedIn, it's the founders like Victor.

**Jason Gong:** Beyond working with clients like you, we also spin up new work streams. One I'm spending the most time on right now is a ghost writing service where we take founders and leaders and write content for their LinkedIn accounts. The metrics we think about are awareness on X and leads on LinkedIn.

**Jason Gong:** Once you build a good LinkedIn following, the best thing to do is start scraping, enriching, and retargeting those people. If a post gets a hundred likes, you go through and figure out which personas you want to target, then start emailing and connecting with them on LinkedIn. There are tool suites for that.

**Jason Gong:** So for developers specifically on X, my initial thought is you guys already have a really good community. Look at your GitHub repo — the number of PRs, the things your community's doing. That's the heartbeat. Take that and talk about it in a genuine way to create engagement.

**Jason Gong:** So on my side, for image generation, I'll talk to Daniel later today. Maybe next week or the week after we can start bringing that into your old blog posts to start enriching them.

**Victor Coisne:** That sounds good.

**Victor Coisne:** I tagged you on Slack in the thread where we shared brand guidelines. We added Daniel to a Figma file with a template. That's awesome.

**Jason Gong:** Oh, I also wanted to mention — we're helping some of our customers pick CMSs, and whenever we can, we recommend Strapi. So we'll loop you into those conversations.

**Victor Coisne:** We have a partner program where you get referral commissions.

**Jason Gong:** If this is starting to become a habit, we should definitely talk about that.

**Victor Coisne:** Yeah, that sounds good.

**Jason Gong:** On my side, it seems like they want technical guidance — "Why should I use Strapi? How do I integrate this?" So I'll loop you in, and you can figure out who from Strapi should get involved.

**Victor Coisne:** That sounds good.

**Jason Gong:** Cool. Sydney, take it away.

**Sydney Go:** Sorry, I realized I was muted when I started sharing my screen. My Google Meet isn't cooperating. So basically, I'm diving through your integration pages to see how they're performing. Here's the non-branded integration page performance — you're getting good impressions, good clicks, good average CTR. But all these metrics are mostly driven by your top two pages: React CMS and Next.js. Those are pulling most of the data.

**Sydney Go:** I'm looking at monthly data to see the bigger picture. Apart from those two pages, everything else is doing okay but has very low click-through rates. So what we're thinking is to really unify the format. Both React and Next.js have the same format and they're performing well.

**Sydney Go:** I think you've been using the newer integration pages we've been sending. Here's what that looks like. You have a Strapi highlight section that's always the same, and setup is also consistent. That's working for React and Next.js, but not the other pages.

**Sydney Go:** What we'd like to do is change the format. Instead of starting with "What is React.js?", let me pull up the Gatsby page to show the old format.

**Sydney Go:** Here's what we want to do instead: start with a one-liner that tells people what Gatsby is for Strapi — basically why they'd use it together. Then a very brief "what is it?" section. This is for top-of-funnel searchers. If someone's searching "Gatsby headless CMS," they already know what Gatsby is.

**Sydney Go:** Link to the documentation. Then go into "Why use Gatsby with Strapi?" Some of your older pages do this, but the newer ones have two sections of generic "what is Strapi" or "why Gatsby" content. To give value quickly, bring back the "why together?" section and add a CTA. Include social proof to strengthen it.

**Sydney Go:** Then go lower in the funnel with "how to integrate," keeping the project example repo and Strapi office hours. I've done this for three of your pages, including AWS.

**Sydney Go:** The AWS page has a lot of h3 and h2 headers with lots of links. It's hard to parse at first glance. Someone searching for options hits this page and won't know how to navigate it. So we're fixing up the format to focus on the different intents your pages are bringing in.

**Victor Coisne:** I love the idea of reworking the structure. It's very needed. We should prioritize which pages to tackle first. Gatsby is a dying framework — nobody's really using it, so we shouldn't put much effort there.

**Victor Coisne:** Just to give context on pages like AWS: we actually migrated that from our docs. Someone took a big block of docs and pasted it as an integration page. We get a lot of traffic from the docs. Looking at GA, a lot of that traffic is coming from the docs as a referral source. That's the history.

**Victor Coisne:** I'm really excited about refactoring the structure. For some categories, like deployment, we have integration pages that are sorting categories. We were talking to Golzar about this yesterday. We want to call out cloud at the beginning — you should really be deploying to cloud first.

**Victor Coisne:** But if you really have like, you know, if you really have to deploy to the US, here is how you go about it.

**Victor Coisne:** They're all like category specific CTAs that we should, and when I say CT, I don't think we should do a banner because I think those all they tend to convert not super well, but like a text-based CTA component.

**Victor Coisne:** That should be done in Sprapi.

**Victor Coisne:** It's a component that we can add to the content structure.

**Victor Coisne:** I think like, you know, I want us to think about that.

**Victor Coisne:** It's like, when is something in the body of the text versus when when some of the content is actually in a different component in Sprapi?

**Victor Coisne:** Does that make sense?

**Victor Coisne:** Yeah.

**Sydney Go:** Yeah, it definitely makes sense.

**Golzar Yaghoubpour:** I'd also add on the CTA topic: right now we have buttons that say "Get in touch" or "Learn more about this integration," and they're all the way at the bottom. Most people don't scroll that far. What I want to do is move the CTA up.

**Golzar Yaghoubpour:** Notum, our web agency, has already built the technical work to add an inline CTA. It's just a matter of moving it higher on the page. With the new structure you're proposing, after the "why integrate" section makes sense for the form, rather than having people scroll another 30-40 seconds.

**Golzar Yaghoubpour:** That's the only thing I'd add, but I really like the new layout you're proposing.

**Sydney Go:** Thanks for that feedback.

**Jason Gong:** You mentioned migrating AWS from docs. Is it important to keep that content in docs, or should we repurpose it for integration pages? I don't want to mess with the docs too much.

**Victor Coisne:** They wanted to move it out because the expectations are much higher for docs — everything has to be perfectly maintained and work 100%. For integration pages, the expectations are lower.

**Jason Gong:** The theme for what we're doing is: when people search for "AWS with headless CMS," they're not looking for an in-depth guide initially. They want to know what they can use and how it works. That's the content we'll cover. For pages that already go very deep, maybe we just tag them at the top as "not the official integration guide" and link to the docs.

**Sydney Go:** Yeah, I don't think we go into the docs.

**Sydney Go:** There's a tag on our integration pages that say something along the lines of this isn't the official integration guides and artificial documentation.

**Sydney Go:** So I think what Victor was saying is that I was before did open and then as an integration page that we can now change.

**Victor Coisne:** We can push some deployment or hosting solutions into the how-to section using toggles to hide lengthy content. That way people can scan quickly and see there are multiple options — Azure, AWS, different container services. It'll be long, but we can be creative about hiding it under toggles.

**Jason Gong:** That sounds good.

**Jason Gong:** For CTAs, what we've done for other clients is make them more contextual. If you can pull the header and description text into the CMS, we can dynamically generate the CTA. For example, on the AWS page, instead of just saying "deploy this on Strapi," it could say "If you want to integrate AWS for this reason and benefit, use Strapi." That would help conversion.

**Golzar Yaghoubpour:** Is there a way to automate that in a workflow? It's going to get convoluted quickly if we're doing it all manually.

**Jason Gong:** As long as the header and description text are in fields in your CMS, we can automate this through a workflow.

**Golzar Yaghoubpour:** Perfect. Paul and I talked about this in early March or end of February. It's great that it can be automated. For the top 10 pages, we should definitely do what you said and see how it performs by traffic volume. Then before expanding it, I'll grab the code.

**Sydney Go:** I did have one question. Your integration pages cover a lot of different types of partners. AWS is definitely not the same as Java or Ruby. Is there a way you determine who gets an integration page?

**Victor Coisne:** It's more by category. There are different types of integration — front-end integrations through APIs, and basically any technology you can use to extend or customize Strapi. The breadth is very wide. We want to be loose with who gets listed, so it's kind of a free-for-all right now.

**Sydney Go:** What I was thinking is if we can categorize them in certain ways for our purposes — not necessarily on your backend.

**Victor Coisne:** Just focus on the SEO-friendly ones.

**Sydney Go:** Perfect. I'll get the first batch of those this week, and then we can start testing and iterating.

**Sydney Go:** That's all I had on my end. We're almost out of time. Any questions or anything else to discuss?

**Victor Coisne:** Yeah.

**Victor Coisne:** It's great we're zooming out from the details and talking strategy. I appreciate that. But it would be good to get a summary — not details on every article, but how many articles were delivered this week? What's left in the backlog? That way we can quickly see if we need to provide more topics or identify bottlenecks.

**Sydney Go:** I'll send that over. I should have one ready by the end of this call. We'll send more topic ideas later today or tomorrow so you can start approving them. Your next batch of articles should be with you by tomorrow, and I'll send you the list.

**Victor Coisne:** Excellent.

**Victor Coisne:** Thank you.

**Golzar Yaghoubpour:** Sydney, are we able to access the Looker reports you showed?

**Sydney Go:** Yes, you should be able to. I'll share them in chat now.

**Golzar Yaghoubpour:** Can you send them to the shared Slack channel?

**Sydney Go:** Perfect, I'll do that.

**Golzar Yaghoubpour:** Great, I'll pin it.

**Golzar Yaghoubpour:** I left you a message about CTAs. The recent batch hasn't been including them.

**Theodore ONYEJIAKU:** I shared links to previous messages from Golzar and Victor so you can see what the CTA examples look like.

**Sydney Go:** Thank you for that. We're going to add those back in and refine the workflow to make sure they're included going forward.

**Golzar Yaghoubpour:** Perfect.

**Golzar Yaghoubpour:** Thank you for posting that video. I appreciate you being proactive.

**Golzar Yaghoubpour:** When I created the blog CTA component, we only had the colorful versions with purple backgrounds. Since then we've added lighter options and a minimal version that looks very inline.

**Golzar Yaghoubpour:** I think the minimal versions will perform better. Any thoughts?

**Theodore ONYEJIAKU:** The CTA is just a script you can add at the top, bottom, or wherever it makes sense in the content. You can preview it before inserting.

**Golzar Yaghoubpour:** I think there's value in changing all CTAs to the minimal version instead of the purple background. Should we use the minimal one going forward?

**Sydney Go:** Yes, I think so. From my experience, the more minimal the CTA, the better it performs — even text-only CTAs.

**Victor Coisne:** I agree. The minimal version is the most developer-friendly. It doesn't break up the text like the purple version does.

**Golzar Yaghoubpour:** Perfect. Let's change everything to the minimal version across the board.

**Sydney Go:** I'll request access to the Figma CTA files now.

**Jason Gong:** I've updated the instructions as well.

**Golzar Yaghoubpour:** I'll share the CTA design files with you both. You can reach me at golzar.yaghoubpour@strapi.io, and Jason's email is jason@growthx.ai.

**Sydney Go:** Thank you for sharing the Google Analytics explorations. Those are very helpful.

**Golzar Yaghoubpour:** Thanks everyone. Great call.

**Jason Gong:** Thank you. Bye.
