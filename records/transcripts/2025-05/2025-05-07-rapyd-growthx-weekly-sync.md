# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-05-07
time: 17:31 UTC
duration: 34 minutes
organizer: Aida Knežević (aida@growthxlabs.com)
participants: Aida Knežević, Jakub Rudnik, Rachel Pasche, Mark Stiltner, Nicolette Mychajluk, Kristin Reischel, Francine Harris
fathom_recording_id: 61312653
fathom_url: https://fathom.video/calls/293568218
share_url: https://fathom.video/share/SJJJ_ax-KUjGzPDyXkGqiiCSqzHmE3Yo
source: fathom
enriched_on: 2026-03-03 12:00 UTC
speaker_note: Kristin Reischel and Francine Harris were on the invite but did not participate in the meeting. Only Aida, Jakub, Rachel, Mark, and Nicolette actively spoke.
</metadata>

---

## Summary

GrowthX and Rapyd aligned on content strategy refinements to improve blog performance and AI visibility. The teams pivoted focus from local payment methods to local card acquiring, implemented a new XML generation workflow in Aeroops to include Rapyd's point of view, and committed to optimizing CTAs across articles through a six-cluster mapping system. Key priorities are resolving GA4 reporting issues, creating a targeted landing page for the high-performing Swift Alternatives blog, and exploring broader strategies to get Rapyd mentioned across external platforms where AI models train on content.

---

## Context

Rapyd is a global fintech platform enabling online businesses to accept and process payments. GrowthX has been producing content for Rapyd as part of a larger content marketing engagement, publishing to Rapyd's blog to drive traffic, establish thought leadership, and improve SEO/AI visibility. This is the weekly operational sync between the two teams to review article performance, align on messaging and strategy, and track workflow improvements. To date, 9 articles have been published, generating 14 clicks per week as of Week 17, with the Swift Alternatives blog performing particularly well at 2% CTR. The team is working to optimize the content creation workflow in Aeroops and ensure content is positioned effectively both for search engines and AI model training.

---

## Relevance

**To GrowthX Delivery:**
- Aeroops content generation workflow now includes Rapyd-specific point-of-view layer in polishing instructions, enabling more client-centric content at scale
- Established systematic CTA optimization process: 6-topic cluster mapping with short/medium/long variations, moving from ad-hoc CTA placement to programmatic insertion
- GA4 reporting issues identified as blocking traffic attribution; Aida tasked with reconnecting property to ensure accurate performance data for future strategy
- Airtable workflow improved with new "Reviewed" status between "Ready to Review" and "Staging" to reduce friction for multi-reviewer processes

**To CheckThat / AI Visibility:**
- Rapyd explicitly interested in AI/LLM optimization beyond traditional SEO—team discussed "surround sound" strategy of getting Rapyd mentioned across external platforms (reviews, listicles, Reddit, industry forums) where LLMs train
- Emphasis on transparency and specificity in product messaging to help LLMs better understand Rapyd's value proposition; concern raised that opaque SaaS websites confuse AI models
- Long-tail, nuanced keyword targeting approach aligns with AEO best practices: appearing in diverse search contexts rather than competing on generic keywords
- Opportunity to audit existing Rapyd website and landing pages for clarity and AI-friendliness

**To GrowthX Business Development:**
- Swift Alternatives blog demonstrates strong pull (2% CTR, continued traffic interest), indicating viable expansion into comparative/alternative-product content as a differentiator
- Rapyd engagement shows client willingness to invest in workflow improvements and systematic optimization—signals account health and expansion potential
- Account demonstrates need for ongoing SEO/AEO strategy consulting; positioned for retainer or expanded scope if blog continues to drive qualified traffic

---

## Overview

- XML generation workflow in Aeroops now includes Rapyd's point of view for articles
- Need to shift focus from local payment methods to local card acquiring in content
- CTAs on blog posts to be optimized and programmatically inserted based on topic clusters
- Swift Alternatives blog performing well; opportunity to create targeted landing page
- Exploring strategies to optimize content for AI/LLM consumption and visibility

---

## Key Topics

### Content Generation Workflow

  - XML generation step added in Aeroops after image creation
  - Polishing instructions now include Rapyd's point of view for articles
  - Weekly batch of XML files to be provided for Rapyd's ingestion

### Content Focus Adjustment

  - Pivot from local payment methods to local card acquiring, especially for Europe/UK markets
  - Reduce mentions of markets Rapyd no longer serves (e.g., India, China)
  - Emphasize benefits of local card acquiring: lower fraud rates, higher approval rates

### Blog Performance

  - 9 articles published so far, with 14 clicks per week (Week 17)
  - Swift Alternative blog performing well with 2% click-through rate
  - GA4 reporting issues persisting; Mark to investigate and potentially reconnect property

### CTA Optimization

  - Plan to add more product-focused CTAs within blog text
  - Programmatically insert 2-3 CTAs per blog based on topic clusters
  - Consider creating specific landing pages for high-performing articles (e.g., Swift Alternatives)
  - Nicolette to map existing CTAs to topic clusters and create short/medium/long versions

### AI/LLM Optimization

  - Focus on getting Rapyd mentioned in various contexts across the web
  - Target long-tail, nuanced searches in content creation
  - Ensure clear, transparent product messaging on website and landing pages
  - Maintain foundational SEO practices while expanding presence on external platforms

---

## Action Items

**Aida Knežević (GrowthX)**
- Investigate GA4 reporting issue. Disconnect/reconnect property if needed. Ensure blog traffic data is flowing correctly.
- Add "Reviewed" status to workflow in Airtable. Place between "Ready to Review" and "Staging".

**Rachel Pasche (GrowthX)**
- Add CTA suggestions to blog posts. Leave comments in Airtable for product-focused CTAs. Coordinate w/ Nicolette's CTA mapping.

**Mark Stiltner (Rapyd)**
- Review Swift blog. Identify conversion improvement opportunities. Consider landing page w/ comparisons (SWIFT, RTP, instant card payouts). Plan CTAs.

**Nicolette Mychajluk (Rapyd)**
- Create landing page for Swift alternatives. Compare SWIFT, RTP, instant card payouts. Include tables, form. Draft CTAs for blog insertion.
- Map existing CTAs to 6 topic clusters. Identify gaps. Create short/medium/long versions for each cluster. Send to Mark for review.

---

## Transcript
**Mark Stiltner:** I think Kristen is out.

**Mark Stiltner:** Francine is out.

**Mark Stiltner:** Kristen is out.

**Mark Stiltner:** Mark will probably join.

**Mark Stiltner:** But he's in Hawaii right now, so he might be a few minutes late.

**Mark Stiltner:** So we can just go ahead and get started.

**Mark Stiltner:** Okay, great.

**Aida Knežević:** So I already sent the agenda in our Slack channel, but so let me just share my screen really quickly.

**Aida Knežević:** Oh, there's Nicolette.

**Aida Knežević:** Hey, Nicolette.

**Aida Knežević:** So, yeah, this is the article generation workflow in Aeroops.

**Aida Knežević:** I think I showed it to you once.

**Aida Knežević:** So right after an image, right after we generate an image, there's an XML gen step.

**Aida Knežević:** We just click to run, and then it generates this.

**Aida Knežević:** So we will...

**Mark Stiltner:** That looks like XML to me in my layman's eyes.

**Mark Stiltner:** Yeah.

**Aida Knežević:** I think, yeah, so we just copy-paste this into, remind me, into a CSV file?

**Mark Stiltner:** No, we can just ingest this as like, as a Word doc, Google doc, CSV file, whatever.

**Mark Stiltner:** Once it's in XML, it's good to go.

**Mark Stiltner:** and you can actually put as many, like, we can handle one or multiple files at a time.

**Mark Stiltner:** And here, as long as there's like a title tag, which there usually is in a XML document, like, we'll be able to figure out where an article stops and where another one starts.

**Mark Stiltner:** So, this is it.

**Mark Stiltner:** I just basically need this in whatever format you want to download it in.

**Mark Stiltner:** Okay, great.

**Mark Stiltner:** So, yeah, we have a title tag here.

**Aida Knežević:** So, think the best way to go about it is every week after.

**Aida Knežević:** Like, Rachel, when you're done with, where is this, where is this getting information from, just a second, topics, I just need to check where is this workflow getting the article data from.

**Aida Knežević:** So if it's getting it from the article doc, then Rachel can just, like, generate this when she's done, like, reviewing your comments and implementing feedback, and then she can, like, put all of them in one doc.

**Aida Knežević:** That would be great.

**Aida Knežević:** Yeah, yeah, but I'll ask Kirkland just to confirm, because I just realized that.

**Mark Stiltner:** Yeah, if we just did, like, a once a week batch in one file, then we'll just upload once a week and be good to go.

**Aida Knežević:** Okay, okay, sounds good, sounds good.

**Aida Knežević:** so we're in air ops, I just wanted to show you.

**Aida Knežević:** Really quickly.

**Aida Knežević:** So your polishing instructions now include your, hold on, so they now include your point of view for articles that you shared.

**Aida Knežević:** Hey, great.

**Aida Knežević:** Yeah.

**Aida Knežević:** So this is just basically like the same doc that you shared.

**Aida Knežević:** The polishing instructions are pretty flexible, so we could like add a lot of different things to it.

**Aida Knežević:** Rachel said that this week's batch is really good in terms of product mentions.

**Aida Knežević:** So we're going to wait for your feedback to see what you think.

**Mark Stiltner:** I just finished reading one right now that I thought was getting really close.

**Mark Stiltner:** I'm seeing one issue continuing to crop up that I wanted to address, but I did notice a significant improvement.

**Mark Stiltner:** Hey, that's great.

**Aida Knežević:** So it's working because there is kind of an internal debate going on on whether polishing instructions should be like short and to the point or whether they could be like super elaborate.

**Aida Knežević:** So I'm in like the other camp.

**Aida Knežević:** So I'm glad to see that.

**Mark Stiltner:** You like short and sweet is your camp or you're the long and elaborate?

**Mark Stiltner:** I'm the longer one.

**Aida Knežević:** Yeah, because it just works.

**Aida Knežević:** Like I say it works for my clients.

**Aida Knežević:** But what is the piece of feedback that like what's coming up for you again?

**Mark Stiltner:** So the thing I'm continually seeing across blog posts is a over focus on local payment methods.

**Mark Stiltner:** And the reason this exists is because it is pervasive throughout our content.

**Mark Stiltner:** So that's that's on us.

**Mark Stiltner:** But we've had a pretty big pivot in the last year.

**Mark Stiltner:** And what's happened is we found that our best market is Europe and the UK.

**Mark Stiltner:** And in Europe and the UK, we don't really offer very many local payment methods.

**Mark Stiltner:** We offer credit cards.

**Mark Stiltner:** So whereas like in all these other markets in Asia, we went nuts.

**Mark Stiltner:** And like integrated all these payment methods.

**Mark Stiltner:** And we don't do that much business in Asia.

**Mark Stiltner:** In LATAM right now, we're not doing that much.

**Mark Stiltner:** In Europe, where we are doing a lot of business, we don't really offer local payment methods.

**Mark Stiltner:** So we've really shifted our focus from, hey, you've got to localize your payment methods to, hey, Europe, you need to work with a direct card acquirer.

**Mark Stiltner:** And that's coming through a lot of the copy.

**Mark Stiltner:** And some of the things that are like focuses that we've completely abandoned are in there.

**Mark Stiltner:** So I see India and China come up a lot as examples, both of which are great examples of places where local payment methods are important.

**Mark Stiltner:** But we pulled out of both of those markets.

**Mark Stiltner:** We don't work there at all.

**Mark Stiltner:** So, you know, seeing examples on like use UPI for payments in India, it's just not relevant to us because we don't support UPI anymore.

**Mark Stiltner:** We don't support India anymore.

**Mark Stiltner:** Same thing with China.

**Mark Stiltner:** So I think we need to.

**Mark Stiltner:** Dial down the focus on local payment methods and payment localization, and where we're talking about that in articles, replace it with talking about local card acquiring.

**Mark Stiltner:** And local card acquiring means that your card acquiring process, or the one who's processing your transactions, is in the same market as the customer who's making the purchase.

**Mark Stiltner:** And the processor processing of those transactions, the acquirer, is in the same market.

**Mark Stiltner:** You get lower fraud rates because they understand that market and their fraud trends better.

**Mark Stiltner:** You get lower or higher approval rates because, again, you understand that market better.

**Mark Stiltner:** You're able to approve more transactions.

**Mark Stiltner:** It's just a big benefit for everybody.

**Mark Stiltner:** There's no middleman that you're going through.

**Mark Stiltner:** So that's the message that we need to get in here.

**Mark Stiltner:** can give you some specifics about that.

**Mark Stiltner:** I'm not sure what the best way to write that up would be, but that's the issue to us.

**Aida Knežević:** Okay.

**Aida Knežević:** Yeah, that's, I mean, even I can just take this transcript as well.

**Aida Knežević:** But if you have, like, additional details on how local.

**Aida Knežević:** I mean, I could just add a paragraph to the polishing instructions to say, you know, when talking about, like, instead of talking about local payment methods, talk about local card acquiring, like, when it comes up, depending on the topic.

**Aida Knežević:** So that would work.

**Mark Stiltner:** The tricky thing is, sometimes it's still kind of relevant.

**Mark Stiltner:** It's not bad to have a mention of, like, oh, by the way, you can improve your conversion rates by offering local payment methods.

**Mark Stiltner:** But it doesn't need to come up all the time and you don't need to go into depth into it.

**Mark Stiltner:** Okay.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** So that's going to be, like, a mix of just human intervention and just our own workflows.

**Aida Knežević:** So, yeah, that's definitely doable.

**Jakub Rudnik:** Can I ask, just for maybe on how it, is this still pervasive on the site?

**Jakub Rudnik:** I know if you're making that kind of product company change, is it something that's just across the site?

**Jakub Rudnik:** Or is this, like, you know, the LMS are picking up old information and just like that?

**Jakub Rudnik:** I would just be curious for, like, how we're thinking about that, how to.

**Mark Stiltner:** We've dialed it in on our main site messaging, but it's still pervasive in our old blog posts.

**Mark Stiltner:** And so I think the blog cleanup process will help.

**Mark Stiltner:** And I'm guessing that that's where the LLMs are pulling a lot of it from.

**Mark Stiltner:** Yep, that makes a lot of sense.

**Jakub Rudnik:** I was trying to do quick searches here.

**Jakub Rudnik:** I didn't see like a ton on other sites.

**Jakub Rudnik:** There's probably other things, you know, like if there's an old press release or if someone's put you into a listicle and there's some information.

**Jakub Rudnik:** There could be other sources, too, that would be much harder to clean up.

**Jakub Rudnik:** But yeah, anything on the own site.

**Jakub Rudnik:** But yeah, the blog cleanup, it's nice that that's like a double tip if there's messaging changes, too.

**Jakub Rudnik:** So agreed.

**Jakub Rudnik:** It's really mostly on curiosity for me and then how like this kind of product change or company change impacts, you know, how we have to think of that.

**Jakub Rudnik:** So that's just a really good note.

**Jakub Rudnik:** I appreciate the insight.

**Jakub Rudnik:** Cool.

**Mark Stiltner:** I still owe you the blog review.

**Mark Stiltner:** I've got to get back into that.

**Mark Stiltner:** No problem.

**Jakub Rudnik:** Not like the most fun.

**Jakub Rudnik:** You know, it's a little tedious.

**Jakub Rudnik:** But yeah, just ping me, tag me in the.

**Jakub Rudnik:** The doc or in Slack when you've, you know, gotten another batch done and I'll take care of those.

**Jakub Rudnik:** Okay.

**Mark Stiltner:** Yeah, other than that, I'm just checking through these articles right now.

**Mark Stiltner:** What else is on our agenda?

**Aida Knežević:** Okay, so I wanted also to dive into the performance report.

**Aida Knežević:** So we have nine articles published so far.

**Aida Knežević:** And let me show my screen.

**Aida Knežević:** So week 17, that was last week.

**Aida Knežević:** So we're up to 14 clicks per week.

**Aida Knežević:** Which is nice to see.

**Aida Knežević:** Yeah.

**Aida Knežević:** More than one per article.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** So this is actually, hold on, let me just change the date range right here.

**Aida Knežević:** So made of four.

**Aida Knežević:** So we do like Monday through Sunday.

**Aida Knežević:** So yeah, the Swift Alternative one got a bunch of clicks.

**Aida Knežević:** It has a click-through rate of...

**Aida Knežević:** 2%, which is great to see.

**Aida Knežević:** But yeah, I think as we publish more content, it's just going to grow more.

**Aida Knežević:** What I do want to talk about pretty early, but let's get into it actually in a minute.

**Aida Knežević:** Let me go to the second page.

**Aida Knežević:** So I am still having issues with the GA4 report.

**Aida Knežević:** It's just not getting any data.

**Aida Knežević:** So I'm going to go into your group GA4 again to see if these blogs are showing traffic in GA4.

**Aida Knežević:** Take a look.

**Mark Stiltner:** We did fix that traffic problem that was coming through before.

**Mark Stiltner:** If there's another issue, let me know.

**Aida Knežević:** Yeah, because I was playing around with the dates and everything, and it's just not doing anything.

**Aida Knežević:** DSC is fine.

**Aida Knežević:** But yeah, this is strange.

**Aida Knežević:** So I'll have to look into it.

**Aida Knežević:** And also the LLM referral traffic.

**Aida Knežević:** Rapyd is still, like, flat.

**Aida Knežević:** We're still not seeing, like, percent.

**Mark Stiltner:** That wouldn't be out of, or that is out of GA4.

**Mark Stiltner:** Yeah, yeah.

**Aida Knežević:** Okay, let me see what I'm seeing.

**Mark Stiltner:** So if I go to my, this is all slash blog, right?

**Aida Knežević:** Yeah.

**Mark Stiltner:** Let me just see what I'm seeing from, say, May 1st.

**Mark Stiltner:** Now, if I'm seeing your traffic, I normally, no, I'm getting traffic through.

**Mark Stiltner:** Okay.

**Mark Stiltner:** Hmm.

**Mark Stiltner:** Okay, maybe I need to, like, disconnect and reconnect the property.

**Aida Knežević:** might need to.

**Aida Knežević:** We might have screwed something up.

**Mark Stiltner:** Let me show you my screen.

**Mark Stiltner:** Make sure that I'm looking at the right thing.

**Mark Stiltner:** Okay.

**Mark Stiltner:** So, like, here, I just did, I just filtered to May, May 1st to May 7th, slash blog, and I'm definitely seeing traffic coming through on everything.

**Mark Stiltner:** So it looks like I'm seeing somewhat normal reporting there.

**Mark Stiltner:** Okay.

**Aida Knežević:** How do I look at just referral traffic from, like, ChatGPT?

**Mark Stiltner:** Where's where's that?

**Aida Knežević:** I can record a video for you.

**Aida Knežević:** I sort of know conceptually where it is, but I don't...

**Aida Knežević:** can't just get right to it.

**Aida Knežević:** Okay.

**Mark Stiltner:** I was going to go look at that if you could direct me there, but if you actually do the video, that'd be great.

**Mark Stiltner:** I'll set a report for it here.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** I'll take a look and report the video for you.

**Mark Stiltner:** Okay.

**Aida Knežević:** Yeah.

**Mark Stiltner:** You might need to reconnect, though, because something was definitely broken on our end and we fixed it, but you might have to reset your report.

**Mark Stiltner:** Mm-hmm.

**Aida Knežević:** Okay.

**Aida Knežević:** That's good.

**Aida Knežević:** That's fine.

**Aida Knežević:** Super easy.

**Aida Knežević:** Okay.

**Aida Knežević:** So what I did want to discuss was CTAs on your website.

**Aida Knežević:** So on your blogs, I mean.

**Aida Knežević:** So, for example, let's go to the Swift Alternatives blog, since it's getting, like, the most clicks right now.

**Aida Knežević:** Okay.

**Aida Knežević:** So when we were on the webpage...

**Aida Knežević:** So I see like a newsletter CTA and then we have a webinar and then we have like this is a contact us CTA.

**Aida Knežević:** I was wondering if there's a way we could like add more like more CTA similar to this, but maybe like more product focused.

**Aida Knežević:** And like find a way to insert them in text.

**Aida Knežević:** I can.

**Mark Stiltner:** I can add any kind of CTA that we want and I can do it one off or programmatically across different types of blogs.

**Mark Stiltner:** You tell me what you want, I can get it in there.

**Mark Stiltner:** Okay, that's that's perfect.

**Aida Knežević:** Rachel, I know you've been adding like the CTAs that Nicolette put together in the blogs.

**Aida Knežević:** So maybe you could just like leave a comment and say like, you know.

**Aida Knežević:** Add CTA for X product here.

**Aida Knežević:** Ideally, we might include, well, depending on if it's a super top of the funnel one, we can just have one CTA.

**Aida Knežević:** But if it's something that's further down the funnel, I would add even two to three throughout the text.

**Aida Knežević:** Can they be the same or could they all be different?

**Aida Knežević:** They can be the same.

**Aida Knežević:** We just want to get people's attention.

**Aida Knežević:** Okay.

**Mark Stiltner:** Maybe what I should do is select a CTA for each of our categories.

**Mark Stiltner:** Okay.

**Mark Stiltner:** So if we look at our categories here, we have, I'm looking at backlog and considering what I really need to look at are buckets.

**Mark Stiltner:** Let's see how I look at our buckets.

**Mark Stiltner:** What's the best way to just see the buckets?

**Mark Stiltner:** An air table?

**Aida Knežević:** Mm-hmm.

**Aida Knežević:** Just a second.

**Aida Knežević:** So you just go.

**Aida Knežević:** Topkit Clusters.

**Aida Knežević:** Those are like the six.

**Mark Stiltner:** I could probably just select a CTA from that document for each cluster, and then we just programmatically enter like two or three on the blogs for each one.

**Mark Stiltner:** And maybe one at the bottom, one in the middle, change up the one on the side to be, although there's nobody ever clicks on the ones on the side, like maybe three, like one towards the top or something.

**Mark Stiltner:** What's best practice?

**Jakub Rudnik:** That's roughly right.

**Jakub Rudnik:** I mean, it depends on what you have, too.

**Jakub Rudnik:** Like, nobody clicks on the right side thing because you just, it's like nobody sees an ad anymore.

**Jakub Rudnik:** But if you could do some things that make it stand up more, and there, even if it's like nobody does, it's still, you know, a quarter of a percentage point can matter when you have the right thing at the right time.

**Jakub Rudnik:** So I think just generally what you outlined.

**Jakub Rudnik:** So doing it scalably, picking the cluster and adding programmatically, I do think I would look at the right side too.

**Jakub Rudnik:** Again, if you're just putting a bunch of these, you are covering more ground and getting more shots on goal essentially and a little bit more accurate.

**Jakub Rudnik:** Then I would, especially if it's top of funnel, I think the programmatic general for the cluster CTAs makes sense to me.

**Jakub Rudnik:** I think the articles that you're further down the funnel are really specific.

**Jakub Rudnik:** That's where I would then start to like, there'd be less mileage on those.

**Jakub Rudnik:** So I'd get that first thing kind of done.

**Jakub Rudnik:** But something like this, you know, Swift alternatives article, that's good.

**Jakub Rudnik:** Like if you do that, right, that's a, that's a conversion magnet.

**Jakub Rudnik:** That thing can be converting three, five, 10% of traffic when I've done alternatives articles in the past.

**Jakub Rudnik:** And so that one, like I'm looking really quickly.

**Jakub Rudnik:** It's like we should have a Swift verse, you know, rapid type of landing page that really got two paragraphs.

**Mark Stiltner:** Cool.

**Jakub Rudnik:** We got an idea about like, we can extend that potentially, but then send them to a landing page.

**Jakub Rudnik:** It totally compares and shows the differences and why.

**Jakub Rudnik:** That's way more effort, right?

**Jakub Rudnik:** So you have to have traffic to justify, but on a page like that, that very specific CTA with the landing page behind it could be a real revenue differentiator, where other articles, probably not as much.

**Jakub Rudnik:** Gotcha.

**Mark Stiltner:** Yeah, I mean, there would be nuances there, but we could build a landing page.

**Mark Stiltner:** It wouldn't be Swift versus Rapyd.

**Mark Stiltner:** would be like, because Swift is like supported by Rapyd.

**Mark Stiltner:** It's more like, I don't know, Swift versus other payment methods that we offer or something like that.

**Mark Stiltner:** And like, my rap, it's great.

**Mark Stiltner:** But I get what you're saying, like, get a landing page together, maybe, that's really dialed in.

**Mark Stiltner:** So if it's a really good blog, dial it in more.

**Jakub Rudnik:** Alternatives or any sort of listicle, generally speaking, are like ones you want to look at right away.

**Jakub Rudnik:** Those are, depends how close they are in your industry and so on.

**Jakub Rudnik:** But generally, like I've seen three, five, 10, 15% on a list of.

**Jakub Rudnik:** Those are like with easier conversion things like a premium tool.

**Jakub Rudnik:** take those numbers all down for what you're looking at, but they're going to be three to five X what you'll see conversion wise from another article, generally speaking, if it's like on the nose.

**Jakub Rudnik:** Yeah, when I've done SaaS, it's like software.

**Jakub Rudnik:** So we have to apply it over to your world a little bit.

**Jakub Rudnik:** Just bear with me, but like pick a soft.

**Jakub Rudnik:** So CRM, you do best CRM software and best like free CRM software.

**Jakub Rudnik:** And like those goals do pretty well, five to 10%.

**Jakub Rudnik:** Alternatives a little bit higher.

**Jakub Rudnik:** So alternatives to Salesforce that does really well, a little bit higher than the listicle, but the traffic is lower because it's a single product versus the larger category.

**Jakub Rudnik:** And then even lower in the traffic world, again, that's where I come up with the alternatives is one product versus one.

**Jakub Rudnik:** So Salesforce versus HubSpot.

**Jakub Rudnik:** So this one is a little bit different because it's more like in your ecosystem where you have different choices, but someone found that.

**Jakub Rudnik:** And then you're kind of like trying to expand their mind of like there's actually more like you thought this was your problem, but it's actually kind.

**Jakub Rudnik:** A bigger problem or it could be solved differently.

**Jakub Rudnik:** So yeah, it's not a versus.

**Jakub Rudnik:** I don't know.

**Jakub Rudnik:** I would have to think about what the creative way to do that or if someone's done something like that.

**Jakub Rudnik:** But those are the three pillars of my low funnel SaaS content plays.

**Jakub Rudnik:** I think they largely apply.

**Jakub Rudnik:** You just have to shift them slightly with how your world, with this fintech and the product that you have.

**Jakub Rudnik:** It's just a little bit different, but there's a lot you can pull.

**Jakub Rudnik:** Those general search ideas still apply, and they all really work conversion-wise.

**Mark Stiltner:** So we've done some blogs in the past on things that really tie in to what you're saying, like Rapyd versus a competitor called Nuve, or Rapyd versus a competitor called Checkout.com.

**Mark Stiltner:** We could do, and for those, we build out some of that infrastructure too because we tested it in a few ways.

**Mark Stiltner:** So I've got a landing page.

**Mark Stiltner:** It's like Rapyd versus Checkout.com landing page, rapidversuscheckout.com blog with like feature comparison tables and stuff.

**Mark Stiltner:** So if we were.

**Mark Stiltner:** And to do something like alternatives to Checkout.com, alternatives to Nuvei, alternatives to Airwallex, we've already got all that stuff in place for that.

**Mark Stiltner:** So maybe those are some things we should consider.

**Mark Stiltner:** Yeah, I think so.

**Jakub Rudnik:** I think that it makes it really easy to test.

**Jakub Rudnik:** And like, of course, you can be a little bit more specific or change things as you go.

**Jakub Rudnik:** But as far as like a V1, will this work?

**Jakub Rudnik:** Yeah, that's like a great way.

**Jakub Rudnik:** Let's not rebuild the wheel.

**Jakub Rudnik:** Let's just do this and put that content, know, create that content, put it in there and then test from there.

**Jakub Rudnik:** But I think that's really obvious, like reuse your infrastructure.

**Jakub Rudnik:** And then same thing as you're saying that it's like, do we do we have a Checkout.com alternatives page?

**Jakub Rudnik:** You know, if you have the versus, you should also build up the funnel slightly, right?

**Jakub Rudnik:** Get the alternatives and then you can lead them to that versus page that you already have created.

**Jakub Rudnik:** And then are there lists that we should be creating that are more of like that umbrella that could lead people down?

**Jakub Rudnik:** So.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah, there's a few things in there for sure, but repurposing those landing pages makes a ton of sense.

**Jakub Rudnik:** Like the format, and then we can find how the content fits within for this variant.

**Jakub Rudnik:** Okay.

**Mark Stiltner:** I like that a lot.

**Mark Stiltner:** So I should look at the Swift blog now and look into maybe seeing if there's some ways that we can get some other pages on there, a landing page and things like that that can help with conversion and get some specific ads under that one.

**Mark Stiltner:** And that's the only one I should look at that for right now, though.

**Jakub Rudnik:** That's the one I think Aida said as well, but especially with the traffic there, there's tons of impressions like you're – that's the right intent.

**Jakub Rudnik:** That one was the one that stood out to me as well.

**Jakub Rudnik:** Yeah, I think we just watched the clicks, and if something's really growing, if it's lower in the funnel, that's where we could consider.

**Jakub Rudnik:** But that would be the first one.

**Jakub Rudnik:** It's a good test.

**Jakub Rudnik:** You already have some traffic there.

**Jakub Rudnik:** That's where I'd start for sure.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** I'll look into that one.

**Mark Stiltner:** This is an area where payments gets complex.

**Mark Stiltner:** So I'll have to do some analysis of the traffic.

**Mark Stiltner:** give you an example with Swift, Swift is basically it's a system for banks to transfer money.

**Mark Stiltner:** There are other ways to do it.

**Mark Stiltner:** For us, it's not like Rapyd versus Swift.

**Mark Stiltner:** It's kind of like us doing an article on Visa versus MasterCard.

**Mark Stiltner:** I don't care if you use Visa and MasterCard.

**Mark Stiltner:** You're going to run them both through Rapyd, but you might care which one you choose.

**Mark Stiltner:** It's sort of at that level.

**Mark Stiltner:** then the other level of complexity is Russia recently got thrown off a banking network.

**Mark Stiltner:** So there could be a whole bunch of Russian eligarchs trying to figure out a way to launder money, in which case we can't work with them anyway.

**Mark Stiltner:** So there's just all these little complexities that get in there.

**Mark Stiltner:** Yeah, yeah.

**Mark Stiltner:** So we have to make some assumptions.

**Jakub Rudnik:** I mean, if you know what the ICP of that blog would be, great.

**Jakub Rudnik:** If it's like, it could be two or three things.

**Jakub Rudnik:** And yeah, you do have to kind of like imagine what the CTA would be and is there options.

**Jakub Rudnik:** And then if we have enough traffic.

**Jakub Rudnik:** Like maybe it is a matter of trying a few different CTAs, you know, or like even placing them throughout the article, like here at Targeting.

**Jakub Rudnik:** So there's different ways to approach that.

**Jakub Rudnik:** So, yeah, take a crack at what that would look like if you want.

**Jakub Rudnik:** Like we should be bouncing those ideas off and continuing that conversation, especially with your nuanced knowledge of the space.

**Jakub Rudnik:** But really, yeah, why would someone be looking for that?

**Jakub Rudnik:** And then what can we show them on the next page that would say Rapids, like the best option for what you're trying to solve?

**Mark Stiltner:** So, Nicolette, actually, this is some stuff I could use your help with.

**Mark Stiltner:** For this Swift blog, are you there?

**Mark Stiltner:** Yeah, I'm here.

**Mark Stiltner:** Hey, hey, for the Swift blog, remember the RTP versus bank transfers blog that we did a while ago that has some comparison tables in it?

**Mark Stiltner:** Yes.

**Mark Stiltner:** Take a look at the Swift blog.

**Mark Stiltner:** Take a look at that and see if maybe we can write a...

**Mark Stiltner:** Landing page that maybe talks about like, or a deeper piece of content, maybe not even a landing page.

**Mark Stiltner:** talks about like the benefits between SWIFT bank transfers, real-time payment networks, and instant card payouts.

**Mark Stiltner:** And then the conclusion is like, you know, Rapyd does all of it.

**Mark Stiltner:** You just need to figure out what the best one is for you and talk to Rapyd for all your global payout needs.

**Mark Stiltner:** If what I think we could do is build that out into like a bit of a landing page, we kind of look at the tables that we've already built and that kind of thing, pull them together, and have it be like a very crisp, concise landing page with a form on it.

**Mark Stiltner:** And then we would need some CTAs to insert into the blog as well.

**Mark Stiltner:** Could you take a look at that?

**Mark Stiltner:** Yes.

**Mark Stiltner:** And then the other thing I'd like you to take a look at, I've got, this is why I'm sharing my screen.

**Mark Stiltner:** Um, we have the six topic clusters here.

**Mark Stiltner:** Mm-hmm.

**Nicolette Mychajluk:** Will you take that CTA list that you created?

**Mark Stiltner:** Mm

**Mark Stiltner:** And make a determination on which CTA is most relevant to each cluster, and then send that to me, we'll review, and then we can work with Tom and our internal team to automatically insert multiple CTAs in those.

**Mark Stiltner:** Okay.

**Mark Stiltner:** But do you recommend to create any new ones, any new CTAs, if it doesn't seem...

**Mark Stiltner:** We might need them, but take a look at what we've got.

**Mark Stiltner:** Let's map it out.

**Mark Stiltner:** And then we will need some new ones just in the sense that, okay, we're going to have one, like, in the middle of the text.

**Mark Stiltner:** That one's probably a little bit short and sweet.

**Mark Stiltner:** We're going to have one at the bottom.

**Mark Stiltner:** That one's probably a little bit longer.

**Mark Stiltner:** We're going to have one over on the side.

**Mark Stiltner:** It probably needs to be similar messaging to the one that's in the middle of the text.

**Mark Stiltner:** But maybe we don't want it to be exactly the same.

**Mark Stiltner:** So we may need, like, multiple versions of the same CTA.

**Mark Stiltner:** Like a short, middle, and long version, we'd call it.

**Mark Stiltner:** Does that sound good?

**Mark Stiltner:** Mm-hmm.

**Mark Stiltner:** Sounds great.

**Mark Stiltner:** Cool.

**Aida Knežević:** All right.

**Aida Knežević:** Great.

**Aida Knežević:** So that's about it that I wanted to...

**Aida Knežević:** cover for today.

**Aida Knežević:** Do you guys have any other questions?

**Aida Knežević:** I had two action items I wanted to run by you.

**Mark Stiltner:** I am running into just a little bit of confusion with my review process and remembering the blogs that I have reviewed.

**Mark Stiltner:** And sometimes I'll go and click on one and be like, oh, did I edit this one yet?

**Mark Stiltner:** Or did another member of my team edit this one now that we've kind of added some more team members for review?

**Mark Stiltner:** And I was wondering if it's possible to add a step or if this screws up your workflow, if instead of like ready to review going right to staging, there was like another one that said like reviewed.

**Mark Stiltner:** And that way, like when we're done reviewing it, we can just say reviewed and we know not to go back and look at it again.

**Mark Stiltner:** Yeah, yeah, I can just add that super easy.

**Rachel Pasche:** Another thing that some other clients of ours do is in the Airtable, they leave a comment like reviewed or whatever, and then it'll, you know, that'll notify me and then it differentiates that from the other ones, like having a comment on that.

**Rachel Pasche:** Blog or on that.

**Rachel Pasche:** Sorry, not making sense.

**Mark Stiltner:** Where would I add that comment in Airtable?

**Aida Knežević:** You just expand it and you just leave a comment right here.

**Aida Knežević:** You can also tag people so they see it.

**Aida Knežević:** Oh, I see.

**Aida Knežević:** Yeah, then I still got to look at it.

**Mark Stiltner:** I don't mind tagging it at this, but it was just right there in that little status bar I saw reviewed and I can just like cruise right down to the next one that hasn't been reviewed yet.

**Mark Stiltner:** Okay.

**Mark Stiltner:** on it.

**Mark Stiltner:** Because like right now, you know, I know we have reviewed several of these ready to review for rapid post and put in there like a, you know, comment to you guys, but I don't remember which one.

**Mark Stiltner:** So then when I go to review, I got to click on each blog and see which ones have comments.

**Aida Knežević:** Yeah, they make sense.

**Aida Knežević:** Okay.

**Aida Knežević:** So yeah, I added one.

**Aida Knežević:** It's reviewed.

**Aida Knežević:** It's in purple.

**Aida Knežević:** Cool.

**Aida Knežević:** Thank you.

**Mark Stiltner:** My other comment, because we are seeing more traffic coming in from AI.

**Mark Stiltner:** We're starting to think about like, how do we optimize for AI?

**Mark Stiltner:** And it's definitely a different way of thinking about things.

**Mark Stiltner:** mean, one is like some AI searches the web, so search engine optimization still works.

**Mark Stiltner:** But, you know, this stuff is getting like training data.

**Mark Stiltner:** It's getting trained on the web, and I'm assuming that there's ways to optimize for that, too.

**Mark Stiltner:** I was just wondering if you guys had done any exploration into how to optimize for large language model, you know, AI optimization, and if there are any techniques or best practices that you've learned that could share.

**Mark Stiltner:** The short of it is one, it's in everybody's mind.

**Jakub Rudnik:** We're talking all the time.

**Jakub Rudnik:** There's a big thread on that in one of our channels in Slack this week.

**Jakub Rudnik:** So, in general, always on the mind.

**Jakub Rudnik:** Second is like a lot of that is probably searching Google is built into the way we're doing content.

**Jakub Rudnik:** It's not that different from SEO, you know, but it's built in into the way we're structuring using keywords, things like that, but it's not just like your own properties.

**Jakub Rudnik:** I think that's...

**Jakub Rudnik:** The additional piece that I've at least seen, so feel free to chime in, other folks, but the, like, we used to call it, like, surround sound SEO, but now that is, like, applying really well to all alums is, like, different sources, you know, on, like, brand mentions, linked or unlinked, things that you're not just owning, but on, like, larger content ecosystems on the web.

**Jakub Rudnik:** So having presence on review sites and have original reviews and lots of data there.

**Jakub Rudnik:** I mentioned those listicles earlier, like, in the SaaS world, we all write listicles, so getting into other people's listicles, like, you need more shots in goal, not just your own, like, spreading wider.

**Jakub Rudnik:** I think there is more, it seems like there's more on social media, but, like, that's more of organic mentions than just, like, building your own profile.

**Jakub Rudnik:** So it's really thinking of, like, how do you get to other places, how do you get the Rapyd name mentioned in other spots?

**Jakub Rudnik:** know, there's lots of different ways to approach that, but that's the, that's the number one thing I've seen that, like, most people agree on and seems to...

**Jakub Rudnik:** Track from things that I have done.

**Jakub Rudnik:** The other one is like some long tail just on the content you're writing is like targeting more long tail nuanced searches rather than like the same keywords.

**Jakub Rudnik:** Everyone's searching, but that's it's harder to figure out where to go.

**Jakub Rudnik:** And anyway, but that's the like other one that we're not doing like we aren't doing is like the off your own website.

**Jakub Rudnik:** How do you.

**Mark Stiltner:** Get rapid seeing elsewhere.

**Jakub Rudnik:** I mean, that kind of tracks us what I was thinking.

**Mark Stiltner:** If essentially these models are training themselves on whatever data that they're hoovering up and building responses based on probability, then you just want to show up in the right context in as many possible places as you can.

**Jakub Rudnik:** You need to like when someone's talking about the issue that you care about on Reddit, like the thing that people think about, like for lack of like that, just in a very specific way, like then extrapolate that across lots of platforms.

**Jakub Rudnik:** Or people are talking.

**Jakub Rudnik:** That's the much harder stuff.

**Jakub Rudnik:** There's definitely ways to spur more of that.

**Jakub Rudnik:** So,

**Jakub Rudnik:** If you then go and do a Reddit growth strategy, that can work if done properly and feeling natural.

**Jakub Rudnik:** so there's lots of ways to approach it.

**Jakub Rudnik:** It's nuanced between your industry or vertical or whatever, where do people talk about you?

**Jakub Rudnik:** What research do they do in that space?

**Jakub Rudnik:** All those things, that's where you need to think.

**Jakub Rudnik:** And then it's like, we're doing this for the direct traffic or the organic value or whatever, but then knowing that there's some unmeasurable or hard-to-measure value to the other things too.

**Jakub Rudnik:** So it's just like kind of making a lot blurrier on the value to some strategies.

**Jakub Rudnik:** Okay.

**Aida Knežević:** Like all of your, especially like bottom of the funnel content, like I know you already have a bunch of content on your site, but like updating, I know you're probably going to do some of that anyway, but like updating the product messaging just to make sure it's like referring to the most like.

**Aida Knežević:** And also just like your landing pages and your product pages, like the way that they talk about your product, like it's important to be really clear about what the product does.

**Aida Knežević:** You know, having, you know, in some, some SaaS websites, they think you, you avoid that trap, but some SaaS websites, they get very opaque about what their product is about.

**Aida Knežević:** And the LLM also struggles to understand it.

**Aida Knežević:** So wherever you can be like crystal clear about what you're doing, that's going to be very, very helpful.

**Aida Knežević:** But yeah, I think like, yeah, you really need foundational SEO.

**Aida Knežević:** And then, you know, what Jacob said about like, appearing in the right places.

**Jakub Rudnik:** Transparency and specificity, like two words, if you're just thinking that, then wide coverage, you know, in your site, be those two words, especially, and then extend those things wherever.

**Jakub Rudnik:** Or whatever properties you can be on to really simplify that overall.

**Jakub Rudnik:** But I think also we'll surface, you know, other insights in that.

**Jakub Rudnik:** Should be a continued conversation, so I know this is just a short overview, but we'll keep chatting and then forwarding anything else we see, whether it's on LinkedIn or internal sharing or something.

**Jakub Rudnik:** Okay, that's all I got.

**Mark Stiltner:** Nicolette, anything?

**Mark Stiltner:** Nicolette, you were reviewing some blog posts this week.

**Mark Stiltner:** Did you have any questions for the team on anything about that?

**Mark Stiltner:** No, not.

**Mark Stiltner:** It's been a moment.

**Mark Stiltner:** All right, cool.

**Mark Stiltner:** Then I think we're good.

**Mark Stiltner:** All right.

**Mark Stiltner:** Thank you, guys.

**Aida Knežević:** See you next week.

**Aida Knežević:** Bye.

**Aida Knežević:** Bye.
