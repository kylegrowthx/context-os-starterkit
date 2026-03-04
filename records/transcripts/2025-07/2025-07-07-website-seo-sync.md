# Website SEO Sync

<metadata>
date: 2025-07-07
time: 16:02 UTC
duration: 34 minutes
organizer: Dave Capone (GrowthX)
participants: Dave Capone (GrowthX), Jenn Peters (GrowthX), Cameron Brown (Firework), Ritesh Kewlani (Firework), Abhishek Anjanappa (Firework)
fathom_recording_id: 72526802
fathom_url: https://fathom.video/calls/344049069
share_url: https://fathom.video/share/BtL2hSTuHwYxMLWsXxEZA-pqyFD-gLUf
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Dave Capone (GrowthX SEO expert) diagnosed critical technical issues preventing Firework from ranking pages correctly, primarily caused by inconsistent www vs non-www domain handling across a hybrid WordPress/Webflow/Nginx architecture that Google sees as duplicate content. Dave recommended two paths forward: a short-term fix implementing 301 redirects to standardize on www.firework.com, and a long-term solution of migrating entirely to Webflow and deleting WordPress to eliminate the Nginx routing layer. Cameron committed to presenting these findings to Firework's Asia-based infrastructure team the next day at 9pm.

---

## Context

Firework is a GrowthX client operating in the technology sector who brought in Dave Capone for a strategic SEO audit after struggling with indexing issues and inconsistent blog performance. The client's website uses a complex hybrid architecture: WordPress as the primary domain, Webflow for newer pages, and an Nginx server that masks the true Webflow domain (webflow.firework.com) by rewriting URLs to appear as firework.com. This setup was originally designed to provide a seamless browsing experience while gradually migrating from WordPress to Webflow, but it's creating severe technical SEO problems that Google cannot properly crawl and index. Jenn Peters and Megan Dickey (GrowthX) had identified performance issues; Dave was brought in to diagnose root causes. This meeting came at a critical juncture—the Firework team needed to understand whether their infrastructure strategy could be salvaged or needed to change entirely.

---

## Relevance

- **To GrowthX Delivery:** Reinforces the importance of early SEO architecture planning in client engagements. The WordPress/Webflow/Nginx hybrid setup is a cautionary case study—technical decisions made for UX can severely impact SEO. Dave's 2-track approach (short-term 301 redirects + long-term migration) shows how to prioritize by impact and lift. This informs how GrowthX should recommend similar clients handle CMS migrations in future engagements.

- **To CheckThat:** Firework's indexing crisis is a perfect example of where AEO and AI visibility insights matter. The client has topical authority in some older content (Q2/Q3 2024 blogs rank #1) but can't get new content indexed due to technical confusion. This demonstrates the dependency between technical SEO foundations and content strategy—a core CheckThat use case.

- **To GrowthX Business Development:** Account health signal: Firework is engaged, took action to bring in outside expertise (Dave), and is willing to make infrastructure changes. This is a strong renewal/expansion signal. The 30-45 day migration timeline creates a natural checkpoint for follow-up and positioning GrowthX for follow-on content strategy work once the foundation is fixed. Document and findings deliver clear value early in the engagement.

---

## Overview

- Major SEO issues stem from inconsistent use of www vs non-www domains, causing Google indexing confusion
- Migrating entirely to Webflow ([www.firework.com](http://www.firework.com)) and eliminating WordPress/Nginx would resolve many issues
- Short-term fix: implement 301 redirects from non-www to www consistently across the site
- Blog performance discrepancies partly due to indexing issues; need to address technical foundation first

---

## Key Topics

### WWW vs Non-WWW Domain Inconsistency

  - Current setup uses both www and non-www inconsistently, confusing Google
  - Canonical tags often point to different versions than actual URLs
  - Recommendation: standardize on [www.firework.com](http://www.firework.com) for all pages
  - Implement 301 redirects from non-www to www consistently

### Split Architecture and SEO Impact

  - Current hybrid WordPress/Webflow setup causing indexing issues
  - Webflow pages actually hosted on webflow.firework.com, masked by Nginx
  - This creates duplicate content issues in Google's eyes
  - Proposed solution: migrate fully to Webflow, eliminate WordPress and Nginx routing

### International/Multilingual SEO

  - Href lang tags are incorrect, missing country codes
  - French and Spanish sites not performing as expected
  - Need to address core technical issues before optimizing international SEO

### Blog Performance Analysis

  - Stark difference in performance between older and newer blog posts
  - Many recent posts not being indexed at all
  - Likely due to technical issues preventing proper crawling/indexing
  - Need to fix foundation before diving deep into content strategy

### Content Strategy and Topical Relevance

  - Building topical authority requires consistent, clustered content
  - Current architecture issues may be fragmenting topical relevance
  - Once technical foundation is fixed, audit content clusters and internal linking

---

## Action Items

**Dave Capone**
- Create document detailing SEO findings, recommendations. Include WWW vs non-WWW issues, redirect rules, internal linking, content strategy, international expansion. Prioritize by importance & technical lift. Send within hours for Cameron's infra meeting.

- Join weekly SEO sync calls for next few weeks to provide ongoing guidance and track progress.


**Cameron Brown**
- Meet with infrastructure team 9pm tomorrow. Present Dave's recommendations. Discuss deleting Nginx server, moving to single Webflow domain (www.firework.com). Explain larger SEO vision & expansion plans.

---

## Transcript

**Jenn Peters:** Well, yeah, we kind of are chatting here, but just wanting to introduce you to Dave. As I was mentioning and Megan was mentioning in previous calls, Dave's such a great asset to our team and all things like SEO and AEO as well. I'm able to uncover a lot of the issues the site has, but he just has so much more insight into, like, okay, here's the issues, and how do we actually fix it?

**Jenn Peters:** Yeah, we can dive right in because, honestly, the site has a lot of issues in the back end and beyond. I found more after the call regarding the regional language type stuff. So, I'll just let Dave take it away and I'll just be a listener here while maybe you and Cameron kind of work it out.

**Dave Capone:** Yeah, so I spent a few hours this morning going through the site, looking at some of the concerns that y'all had, and trying to think through what the best approach is. I can share my Screaming Frog and walk through some of this. You've got a few different versions of things going on. What I've noticed, specifically with the industry pages, is everything is non-www when the site is www. There's going to be a lot of W's being thrown around in this conversation.

**Dave Capone:** The way I'll preface it: the canonical is set to non-www, but you're forcing www for the rest of the website. That causes issues because Google sees these as two separate domains, two separate sites. You'll see them as two separate pages, which causes a lot of confusion and indexing problems. Typically, sites are either on one or the other. There's been a shift recently over to www, and some pages are being set to that, but some are not, especially the canonical tags. And then with languages, the language pages are choosing non-www, which is counterintuitive to what you're telling Google.

**Dave Capone:** If you're telling Google that www is where you want all your traffic to go, but then a lot of the other pages are showing non-www, there's a lot of confusion in the index. You're in a constant state where Google's churning through this content and not getting the full understanding of where your domain is. I think the biggest thing you can change is to just pick one and say from today forward, this is what it's going to be: www. We need to make sure all the landing pages are migrating to www, including the Webflow pages and the pages in multi-language versions. So anything that's JP or FR—we can see this was 301 redirected, industry pages, and it's redirected to www, which is the right one, but then it's redirecting to probably the non-www one.

**Cameron Brown:** Right.

**Dave Capone:** So there's a lot of confusion going on, which is going to impact rankings and unfortunately not get you leads.

**Cameron Brown:** Okay, so yeah, huge insights because this whole www versus non-www was not even an issue I was as concerned about as some of the other ones. But let me back up and ask a few questions. Just so I understand, there isn't an advantage to our primary domain being just Firework.com as opposed to www.firework.com. It's just that having two is bad, right?

**Cameron Brown:** I also still think that us having multiple domains has to do with our split architecture. It's hard to collaborate with our infrastructure team because they're in Asia, but maybe we should have tried to get them on the call. The real URL of our Webflow site is webflow.firework.com. We have an Nginx server in place to essentially rewrite the URL appearance as just firework.com. The WordPress site is just firework.com as well.

**Abhishek Anjanappa:** So my concern is why is webflow.firework.com?

**Cameron Brown:** Because when we set up the Webflow site, we could not pick firework.com as its primary domain because it was already being used by the WordPress site. So when we release a page on Webflow, its real URL is webflow.firework.com. Part of what our Nginx routing server is doing is sending traffic to our Webflow site while also changing its URL appearance to just Firework.com. So when you're navigating between WordPress and Webflow pages, it always looks like you're on Firework.com. Is that an issue for us?

**Dave Capone:** It depends on how that's implemented. If that's done on a visible layer, client-side, then yes, that's an issue. If it's all done server-side with redirects done in the head where Google will see the different jumps, then that's fine.

**Abhishek Anjanappa:** Can we take that as an action item? Let us first understand what is exactly being used. The www and the non-www, where is that originating from?

**Cameron Brown:** I'm not exactly sure, but if I had to guess, my suspicion is that our original WordPress site, when we first launched Firework.com, there was no complicated architecture. We created a WordPress site with www.firework.com. I'm looking at trends to see if pages still on WordPress are all listed under www, which would confirm that theory. I'm confused now because I'm seeing www.firework.com pages that are on Webflow.

**Abhishek Anjanappa:** My question is, where does it originate? Is it the infrastructure team or is it us?

**Cameron Brown:** I have a lot of questions for the infrastructure team. I have a meeting scheduled with them tomorrow, so I don't have all the answers.

**Abhishek Anjanappa:** Let's bring this up because I'm trying to understand where this is originating from and how do we solve it.

**Cameron Brown:** This is probably the biggest concern. In my mind now, we have the www issue, the sitemap issue, and a few other things. I think they all relate to the foundational architecture.

**Abhishek Anjanappa:** On your analysis, were these the things you identified for the inconsistencies and potential lack of optimum ranking?

**Dave Capone:** Google's in a perpetual state of trying to figure out what your site is right now. Because you've made so many changes so quickly and none of it is consistent, Google's just having a hard time figuring out how to rank your site. It really goes through calculating internal links and other signals.

**Abhishek Anjanappa:** I'm just trying to understand the priority and the impact. There are certain keywords where we still rank number one. So how much of an impact is this going to give us?

**Dave Capone:** To your point, some of your pages still rank number one because you have probably had a lot of backlinks and topical authority on that page. Where this is going to impact you the most is with new stuff you publish. Any new blogs or landing pages Google hasn't seen yet will face a lot of confusion in the index.

**Abhishek Anjanappa:** One of the topics we're also looking at is the blog impressions and visits. Is that part of this discussion?

**Ritesh Kewlani:** Jenn shared this data last week. One thing we noticed is a lot of blogs are not indexing at all—they didn't even have a single impression. When Jenn dived into that, we figured out a lot of it is to do with these blogs not getting indexed.

**Abhishek Anjanappa:** And one more thing, the French and Spanish website—why is it not getting as much activity as we hoped for? Are there backlinks? Is it being recognized?

**Dave Capone:** We want to make sure that's correct because when you're pulling in international pages with all these variations of URLs, we're not 301 redirecting any of them, which is a major issue. We need to make sure we're doing 301 redirects any time these are showing up. For French and Spanish, there's a canonical version using www, but then you're telling Google not to use non-www, you're telling Google to use www, but then it's being redirected back to non-www. You're creating a redirect loop that prevents the pages from ranking.

**Dave Capone:** Because you're telling Google one thing, serving it another, and giving it a directive to go back to the page you told it not to rank. The fix is to standardize on www going forward. That is all we're going to use.

**Cameron Brown:** Thank you for that because I think I have a better understanding now. So it sounds like you could help me structure some things better, add extra canonical tags, and we could get this to a better place. However, taking a step back, the starting point for why we have this issue is because if you delete the "Webflow dot" on the front of the URL, it's going to serve the same page. Technically, Google is treating these like two different pages, one of which it's trying not to index, and pointing back to the original, causing confusion.

**Cameron Brown:** So if we just got off WordPress, deleted the Nginx server, and moved to Webflow—basically say drop Webflow dot—because now Firework.com is available as a domain again. Implement Firework.com on Webflow, get rid of the Webflow.firework.com subdomain, get rid of the Nginx. This is solving all the problems at once. It seems to me we implemented this system to make a hybrid architecture work, which works for the front-end browsing experience. Pages don't break. But from an SEO back-end perspective, it's causing a whole bunch of issues. We can have the best of both worlds by completing the migration and only having Webflow.

**Dave Capone:** I agree. I think the solution is only having Webflow, picking the URL you want to go forward with. In this instance, www.firework.com as the Webflow primary domain. That's the right move.

**Cameron Brown:** Right now, www.firework.com is associated with WordPress. I'm suggesting we delete that site, give that domain to Webflow, and we'd be on one domain, no Nginx server, no redirects, no confusion. Clean everything up.

**Dave Capone:** I agree. I think that would go a long way to help with recovery. You're still going to have migration time within Google—30 to 45 days for Google to figure everything back out. Once everything is set up 100%, you've picked the one single domain, everything is pointing to the domain, you have the right redirect rules and canonical rules. I would say 30 to 45 days for that to work itself out. Then you'd be on the right track to recovery.

**Dave Capone:** On top of that, the hreflang tags are incorrect. Typically Google picks up the language because the site is in French, but hreflang needs to use the country code on top of that. There are some x-default issues too. From a country code perspective, it hasn't passed any of the tools I've used to check it. So that's going to be an issue as well. We need to fix that.

**Abhishek Anjanappa:** Dave, it would be helpful if you can give us a document of the things you've identified with clear examples. The reason this would be helpful is we'll have a conversation with our infrastructure team. I don't think the change is going to occur over the next four weeks. We'll have to project plan because the infrastructure team works based on priorities. But these are all amazing findings. Please give us a document on your findings so that will give us a guiding principle of what to do.

**Abhishek Anjanappa:** The second aspect I really want to bring, and I know we have only eight minutes left, is understanding blog performance. Whatever the flaws were, they've been there for the last one and a half to two years, since October probably. We still see a stark difference—some blogs performing well, a whole bunch not performing well. We need to understand what's the reason for good performance versus not. Is it the content? Is it something to do with publishing? Seasonality? Based on preliminary data, we have certain blogs published in Q2 or Q3 of last year hitting it out of the park. Most recent blogs are not generating anything. There are two aspects: impressions and engagement, and leads. We want to look at both.

**Abhishek Anjanappa:** The third one in mind is why are the other language landing pages not performing well? There's a dependency on what you've identified with French, Spanish, and even Japanese. My guess is we have to sort out the foundational issues first, then start thinking about how to increase activity.

**Cameron Brown:** That's kind of what I was going to say. I think we need to really push on this because we have an imperfect testing situation. We have blogs pre-October 2024 and blogs post-October 2024. Comparing those two batches as we face current infrastructure problems is not a fair comparison—they face different back-end SEO circumstances. The positive thing I would mention is getting off WordPress is the best way to do it. I was toying with continuing the hybrid but making WordPress secondary instead of primary. If we axe WordPress entirely, that's actually much easier on the infrastructure side. Instead of adjusting our strategy and infrastructure, I'm asking them to delete things already in place. I'm optimistic that if we bring them this simpler ask, we can move fast.

**Ritesh Kewlani:** Yeah, and Abhishek, on the second point, we reviewed blog performance last week, and one thing we noticed is a lot of blogs are not indexing at all—they didn't even have a single impression. When Jenn dove into that, we figured out a lot of it is to do with these blogs not getting indexed. That's how we came up with this idea to get Dave on the call. Once we move all these pages to www, that will also help solve the blog issue we're seeing. I want to keep these as separate projects, but this is going to take probably 8-12 weeks, and we cannot wait another 12 weeks for things to get indexed.

**Abhishek Anjanappa:** Publishing is meaningless if we wait. There was indexing occurring previously. Everything was the same. My question is, why is it not occurring now? We have to work both in parallel. I'm not saying we're not doing the larger foundational piece—we have to. But we also have to look at smaller wins we can get in the short term.

**Dave Capone:** I think I'm hearing three different projects. One thing that might accelerate this is to create one single redirect rule that redirects non-www to www everywhere. You have consistency, you have the 301 redirects in place, you're forcing it to go to one web server (Webflow). Any time Google hits any of the other ones, it's immediately directed to www. The second would be doing an audit to make sure you have consistency across the board. I'm seeing issues where you're linking to trailing slashes versus non-trailing slashes, which introduces a 301 redirect and causes Google to index more pages. The name of the game is to give Google the ability to index your site and take advantage of the allocation you have for pages to crawl per day. If you keep giving it redirects, you're going to lose the amount of pages indexed and chances of new content being indexed will greatly reduce.

**Dave Capone:** If we create the correct rules and get everything in place, that'll get you closer to getting more stuff indexed. Once the 301 redirects are in place, you can take your time on the migration part because Google will already see all the stuff. The second part is making sure internal linking is pointing to the right place. You've got to make sure from a migration standpoint that any internal links do not use trailing slashes inconsistently so you have consistency across the board. Once that's done, I would have more faith that the new content you're writing will be perceived correctly and indexed by Google.

**Dave Capone:** On content strategy, to rank in a certain cluster of keywords or topics, you have to have a really great knowledge base. It's not just keywords anymore—it's about clusters. If you have a lot of knowledge in a particular topic, that helps you rank for it. There's lead time building up topical knowledge. If Google can't figure that out and clusters are spread across different variations, you'll have a hard time harnessing topical relevance in one place. Once we get the site and foundation in order, we can really look at these clusters. If they aren't performing, we can go back and ask: Is it links? Anchor text? Do we have enough articles?

**Dave Capone:** On international expansion, once the foundation is built and you've got topical relevance and structure correct, you can look at international and make sure your tags are correct, you've got the right redirects in place, and the structure looks right. You need to have a foundation and make sure you're technically accurate, then you can scale from there going forward.

**Abhishek Anjanappa:** Dave, can you please send us a document putting all of this on paper? That will give us a good conversation with our infrastructure team. Dave, I'm hoping you can send this document over the next day or so. Cameron, when have you set up your meeting with the infrastructure team?

**Cameron Brown:** They're based out of Asia, so I'm meeting with them tomorrow at 9pm. I'm interested in two things: my action items I can do immediately, but more importantly, the deadline for tomorrow is what I need to communicate to our infrastructure team. They're the ones maintaining the Nginx server and doing all the routing rules. I'm hoping to come with the ask of deleting it, but any additional context they need to know, I need to have that for them by end of day tomorrow.

**Abhishek Anjanappa:** I want our infrastructure team to understand the larger plan and vision we have in mind. It's not just deleting one thing—it's about foundation and also expansion from an infrastructure standpoint.

**Ritesh Kewlani:** I can put this together hopefully in the next couple hours.

**Dave Capone:** It's all fresh in my brain, so I can do a quick dump and put that into a document.

**Abhishek Anjanappa:** Understand that we have a little bandwidth issue. If you're doing two or three things, get to the redirect first, then delete WordPress, but do this first. I'd like to see your recommendations in that format—short-term goal versus long-term goal.

**Dave Capone:** Yeah, I'll put it by order of importance. From a technical standpoint, I'll try to do the low-hanging fruit that'll be easy and have the most impact.

**Ritesh Kewlani:** Dave, one last request. This meeting has been so helpful because we've accomplished so much. We were honestly struggling as a team to figure out how to move forward. How do we reach out to you next week? Is it possible for you to be part of these calls going forward for the next few weeks as we make progress?

**Dave Capone:** Happy to join calls. I'm also in the channel, so if there are any questions, I can immediately provide context in the channel as well. No problem going forward.

**Cameron Brown:** Thanks so much to all of you, and thanks to Dave for taking the time.

**Jenn Peters:** Yeah, we can all chat async in the channel if anything comes up, and I'm here to help with anything.

**Cameron Brown:** Awesome. Talk soon.
