# Sunbit <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-25
time: 16:00 UTC
duration: 32 minutes
organizer: Kyle Gaudreau
participants: Jason Beltran (Sunbit), Angel Kemper (Sunbit), Ehtisham Hussain (GrowthX), Kyle Gaudreau (GrowthX)
fathom_recording_id: 89852668
fathom_url: https://fathom.video/calls/420798549
share_url: https://fathom.video/share/16sGwVity7rjb1u-ycnh7yMjpbkeFot2
source: fathom
enriched_on: 2026-03-03 16:45 UTC
</metadata>

---

## Summary

GrowthX and Sunbit reviewed progress on content automation and webhook integration requirements. Ehtisham presented four new topic clusters targeting auto and dental verticals across B2B (merchant/practice adoption) and B2C (financing/reviews) segments, with 10 high-volume keywords per cluster ready for review. Jason outlined critical webhook payload changes needed for full automation: separating summary and key points as distinct fields, including cluster categories, adding focus keywords, converting markup to HTML, and ideally including featured images. The team confirmed they can ingest approximately 250 pre-published articles into draft status once the webhook refinements are complete, with manual scheduling to follow.

---

## Context

Sunbit is a fintech company in the consumer finance space offering financing solutions for auto repair, dental care, and similar service industries. GrowthX is delivering content marketing and SEO services for Sunbit's blog, with the goal of driving merchant adoption and shop direct reviews. This meeting focused on the final automation phase for Sunbit's content publishing pipeline—moving from manual article creation to fully automated ingestion via Trey (their automation platform) and webhook delivery to WordPress. The team has been working together for several months, with recent work establishing the topic clusters and content templates. Jason (Sunbit's Head of Content) needs the technical specifications locked down so he can configure WordPress to properly receive and publish articles without manual intervention.

---

## Relevance

**To GrowthX Delivery:**
- Content production at scale: The 250-article ingest represents a major milestone in moving Sunbit from manual to automated publishing. Once webhook fields are fixed, this becomes a repeatable process for similar high-volume clients.
- Vertical expansion opportunity: The B2B/B2C cluster structure (auto merchant adoption, dental practice adoption, auto financing, dental care financing) demonstrates how to target both supply-side (merchants) and demand-side (consumers) audiences in the same vertical—a pattern applicable to other fintech and service clients.
- SEO keyword strategy: Targeting keywords with 4,400+ monthly search volume in competitive categories shows confidence in Sunbit's domain authority and market position. GrowthX can reference this case for similar high-volume, competitive niches.

**To CheckThat:**
- AI-generated metadata: Jason mentioned using Claude to generate focus keywords and categories as a workaround. Sunbit could use CheckThat's AI visibility tools to validate keyword optimization and SEO metadata quality at scale.
- Training content extraction: The team discussed converting Sunbit's video case studies and training materials into blog articles. CheckThat could help evaluate how well AI-generated content aligns with Sunbit's brand voice and messaging guidelines.

**To GrowthX Business Development:**
- Account expansion signal: Sunbit is moving from content creation to automation—this signals confidence in the content strategy and readiness to scale. Strong renewal likelihood and potential for upselling related services (keyword research, competitive analysis, content optimization).
- Product differentiation: The ability to handle regulated industries (Sunbit operates in consumer finance with compliance restrictions) is a selling point for GrowthX's services. Mention of restrictions on AI note-takers shows Sunbit values compliance-aware partners.
- Traffic anomaly investigation: Minor traffic dips on four pages and GA tracking inconsistencies flagged during the call. GrowthX can proactively offer diagnostic services, positioning as a trusted partner beyond content creation.

---

## Overview

- Four new B2B and B2C topic clusters introduced targeting auto and dental verticals for merchant adoption and shop direct reviews
- 40 high-volume keywords identified (up to 4,400/month search volume) across clusters ready for initial topic selection and review
- Webhook payload refinements required to enable full automation: separate summary/key points, include categories and focus keywords, convert to HTML format, add image support
- Team confirmed ability to ingest ~250 articles into draft status once webhook is finalized; manual scheduling to follow for controlled rollout
- Traffic analysis detected slight dip with four pages losing traffic; team investigating potential GA tracking issues and search result parameter changes
- Trey platform updates bring improved project organization, better workspace navigation, data tables, and vector tables for AI workflows

---

## Key Topics

### Content Strategy Expansion

  - Introduced 4 new topic clusters:
      - B2B auto merchant adoption
      - B2B dental practice adoption
      - B2C auto repair financing
      - B2C dental care financing
  - 10 topics per cluster, including case studies and training-related content
  - Targeting high-volume keywords (up to 4,400 searches/month)
  - Team to review and select 5-10 initial topics for production

### Automation Progress and Requirements

  - Webhook payload structure needs refinement:
      - Separate keys for summary and key points (currently in content)
      - Focus keywords to be included in metadata
      - Categories (clusters) to be added for proper blog categorization
      - HTML format preferred over markup for content
      - Image inclusion desired for blog tiles
  - Jason implementing temporary fixes (e.g., AI-generated focus keywords)
  - Plan to ingest \~250 articles into draft status, then manually schedule publishing

### Traffic Analysis and Monitoring

  - Slight dip in sessions and active users observed
  - Four pages lost traffic; team to monitor for trends
  - Potential GA tracking issues reported by other managing editors
  - Recent changes to search result parameters may affect impression data in tools like SEMrush

### Trey Platform Updates

  - New project format organizes workflows within products
  - Improved navigation between workspaces
  - Addition of data tables and vector tables for AI
  - More intuitive interface, though still potentially intimidating for new users

---

## Action Items

**Ehtisham Hussain (GrowthX)**
- Modify webhook payload structure: separate summary and key points as distinct fields (not embedded in content), add cluster name as categories field, include focus keywords in metadata, consider adding featured image field. Test modified payload and send to Jason for WordPress integration validation.

---

## Transcript
**Angel Kemper:** Hello, good morning.

**Kyle Gaudreau:** Hey, how's it going?

**Angel Kemper:** Good, how are y'all?

**Kyle Gaudreau:** Are you my note takers?

**Kyle Gaudreau:** Yeah, we've gotten to the point where we're communicating to them as humans.

**Angel Kemper:** How are you, note taker?

**Angel Kemper:** Please don't enslave me and my family.

**Angel Kemper:** You will eventually take over.

**Kyle Gaudreau:** Yeah, too many of these note takers, that's for sure.

**Kyle Gaudreau:** Do you all tend to use that internally at all?

**Angel Kemper:** No, we've used it a couple times just for like one-off like sessions and meetings and stuff like where we know like not everyone can attend, but rarely have I like taken action with it.

**Angel Kemper:** You know what I mean?

**Angel Kemper:** Like it's nice, it's a nice to have and I haven't found a need to have for it yet.

**Angel Kemper:** So So don't know.

**Angel Kemper:** But other partners and people that we work with definitely use it, which I can understand.

**Kyle Gaudreau:** It's gotten to the point, legit, that if a meeting isn't recorded, I'm like, oh my god, I can't believe this isn't recorded.

**Kyle Gaudreau:** I use transcripts so much.

**Kyle Gaudreau:** It's super helpful.

**Angel Kemper:** Well, I will say, you guys' recaps that have been provided in the past, they're always so accurate and thorough.

**Angel Kemper:** And obviously, it's the note takers.

**Angel Kemper:** And we have, like I said, a couple of other partners we work with that do the same.

**Angel Kemper:** So it is really helpful.

**Angel Kemper:** So maybe I just need to step up my game and figure out a way to utilize it.

**Kyle Gaudreau:** I recommend it.

**Kyle Gaudreau:** So many meetings were, even internal, we're having conversations about this and that.

**Kyle Gaudreau:** It's just helpful to have something to not lose some of the key detail and then just build off of those thoughts in different ways.

**Angel Kemper:** It saves me tons of time.

**Jason Beltran:** Yeah, absolutely.

**Jason Beltran:** We have some restrictions on that.

**Jason Beltran:** Yes, because we work in such a sensitive environment, consumer finance, so we can't really take advantage of the note takers.

**Kyle Gaudreau:** That's a good point.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Good point.

**Jason Beltran:** Yeah.

**Jason Beltran:** So, yeah, it's kind of, it's one of the aspects of working in a highly regulated space is you can't do everything.

**Jason Beltran:** Like when I used to just work in SaaS, like there, it's like the world was open.

**Jason Beltran:** Like going to check with legal was, you know, for contracts and maybe some, like if it had to do with like investor messaging, that was like forward looking statements.

**Jason Beltran:** Yeah.

**Jason Beltran:** Other than that, it's free reign.

**Kyle Gaudreau:** One of benefits of startup life.

**Jason Beltran:** Yeah.

**Kyle Gaudreau:** I mean, even in the SaaS space, bigger public companies, you know, some of the companies we work with, I'm like, this would be really cool to do with you all, but there's no way your security team would ever go for it.

**Jason Beltran:** Exactly.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** It's it goes.

**Kyle Gaudreau:** Yeah.

**Jason Beltran:** Good stuff.

**Jason Beltran:** All right.

**Jason Beltran:** Yeah.

**Kyle Gaudreau:** Let's jump into it, Ashok.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** I'm going to start sharing.

**Ehtisham Hussain:** I think you guys can all see my screen now.

**Ehtisham Hussain:** So the next batch is in, the 25 articles.

**Ehtisham Hussain:** I see we're accumulating quite a big to be published and to be reviewed backlog, but the good thing is I think the automation is like pretty much done.

**Ehtisham Hussain:** So Jason, what else, do you need something else from our side?

**Jason Beltran:** Yeah.

**Jason Beltran:** So we're, we're pretty close and I'm doing some stuff on my end to kind of get us as close to automation as possible, but I did have some requests for the, for the payload that's kind of posting to the, to the webhook.

**Jason Beltran:** So we can talk about.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** So we'll talk about it in this meeting.

**Ehtisham Hussain:** I'll take notes and it's being recorded.

**Ehtisham Hussain:** So, yeah, I'll deliver it to the dev team.

**Ehtisham Hussain:** We discussed experimenting with some new types of topics to drive auto dealership adoption and dental practice adoption.

**Ehtisham Hussain:** So much.

**Ehtisham Hussain:** So I went with some B2B topics and some B2C topics.

**Ehtisham Hussain:** The B2C topics are to drive shop direct reviews and the B2B topics are to drive merchant signups.

**Ehtisham Hussain:** And it's not like, so we have these in the OS, as you can see.

**Ehtisham Hussain:** So I've created four new clusters.

**Ehtisham Hussain:** B2B auto merchant adoption, B2B dental practice adoption, B2C auto finance repair, auto repair financing, and B2C dental care financing.

**Ehtisham Hussain:** And then we have topics, like 10 topics against them.

**Ehtisham Hussain:** We're all, they're all in.

**Ehtisham Hussain:** Considering they're not in production or anything yet, some of the, like a lot of them have keywords related to them, but some of them are direct, like they're like case studies for which I'll need your help.

**Ehtisham Hussain:** And then we can do general case studies.

**Ehtisham Hussain:** don't really have to mention anyone, but if we can mention anyone, that, you know, someone that would be great, but we can do general as well.

**Ehtisham Hussain:** Um, and we have some topics on how to train, uh, your service advisors to offer Sunbit, uh, to customers and how to.

**Jason Beltran:** Yep.

**Kyle Gaudreau:** Wow.

**Angel Kemper:** That was abrupt.

**Kyle Gaudreau:** Maybe he got a forced update.

**Kyle Gaudreau:** And he's back.

**Ehtisham Hussain:** I think I'm back. Yeah, this has been happening for three days straight.

**Kyle Gaudreau:** Oh, I have two internet connections.

**Ehtisham Hussain:** I got two different internet connections.

**Kyle Gaudreau:** So the other one kicks in.

**Jason Beltran:** I have the same thing—like a backup at work, yeah, same thing happens to me.

**Ehtisham Hussain:** Right, so all these topics are up there if you guys want to review them. These are kind of middle and bottom of the funnel topics. We're going up against some seriously high volume and high keyword difficulty keywords, but we've got traffic, we've got traction. I think we're in a position to do this. We're going for keywords as high as 4,400 per month now. I'll continue with the general topics we do on B2C for dentistry, dentistry costs, those topics will be in there. I've put these 40 new topics in there, so we can do maybe five to ten, and if you guys go through them.

**Jason Beltran:** Yeah, I was going to ask how to give you feedback.

**Jason Beltran:** Because we do, we have so much information, like training, on how to offer Sunbit, how to confidently offer Sunbit.

**Jason Beltran:** And I was just curious, how can we provide you with that content to help kind of, because we, of course, one, we don't want the article to contradict the stuff that we say in training.

**Jason Beltran:** We want it to be aligned.

**Jason Beltran:** So, yeah, like, what's the best way of kind of aligning?

**Ehtisham Hussain:** If you have, like, if you have PDF documents, or if it's published somewhere online, whatever source material you have on it.

**Ehtisham Hussain:** What videos?

**Ehtisham Hussain:** Yeah, you can just share them on Slack.

**Jason Beltran:** Okay, sounds good.

**Jason Beltran:** And we also have video case studies and a bunch of stuff as well.

**Ehtisham Hussain:** Oh, perfect, perfect.

**Ehtisham Hussain:** Because, like, what we can do is we can use the transcript from the video case studies, and we can turn it into a article, and then we

**Ehtisham Hussain:** You can embed the video in there as well.

**Jason Beltran:** Perfect.

**Ehtisham Hussain:** So that would be a pretty solid case study with text and video element and everything.

**Ehtisham Hussain:** Yeah, that sounds good.

**Ehtisham Hussain:** So anything you have, just share it.

**Jason Beltran:** For example, like if you're going to.

**Jason Beltran:** I was going to say like, and then like certain verbiage, like I hear the case study says how a local garage, what, you know, it's normally referred to as a service drive instead of a garage.

**Jason Beltran:** So like little things, tweets like that.

**Jason Beltran:** Yeah.

**Jason Beltran:** We'll just kind of continue.

**Jason Beltran:** I guess we'll just like in the documents provide you with feedback.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** And you can also like leave comments over here on Slack.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** So, so we've got this thing going for us now.

**Ehtisham Hussain:** So I did some traffic analysis.

**Ehtisham Hussain:** This is the first time usually like with Sunbit, go in, everything's going up.

**Ehtisham Hussain:** I have some pretty nice graphs to make.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** But this week, like.

**Ehtisham Hussain:** I saw that the sessions and active users went down, so I did a little digging on what happened, and I saw that these pages, and I mentioned them, like we discussed it on Slack as well, so these pages lost traffic.

**Ehtisham Hussain:** These four, they're still live, so I'm just going to keep an eye on them, I'll see if this week was an anomaly, because there are some issues going on with GA, with Google Analytics, and some other managing editors were also discussing it in their channels that traffic reports have been a bit bad for some customers.

**Kyle Gaudreau:** That shouldn't affect GA as much, at least to my knowledge, I admittedly do need to spend a little bit more time looking at what's been happening, but essentially the TLDR of it is a lot of tools like a Google Search Console, or a SEMrush, or, you know, varying tools that are trying to interpret the search results pages, they would use a parameter,

**Kyle Gaudreau:** That would allow them to take snapshots of 100 results at a time, and now that's not working, and now it's like 20 at a time or something.

**Kyle Gaudreau:** There's still a few details I'm trying to sort out.

**Kyle Gaudreau:** The net effect of that is that pretty much all our accounts are seeing a drop in impressions, but it's an artificial drop.

**Jason Beltran:** It's just a tracking issue drop.

**Ehtisham Hussain:** And so that shouldn't affect GA.

**Ehtisham Hussain:** Yeah, I was thinking the same thing, but like a couple of the Emmys were, they reported that their GA numbers were also.

**Ehtisham Hussain:** Yeah, I'll dig into that as well.

**Kyle Gaudreau:** Luckily, I have a good chunk of time later today.

**Ehtisham Hussain:** And we can also just keep an eye on it for this week, next week, and we can see if this is a trend that continues and we continue to lose traffic or something, we can dig deeper and see what happens.

**Ehtisham Hussain:** On the surface, what I'm seeing is that this page, like this URL, it used to bring us a lot of traffic month, sorry, week after week, and

**Ehtisham Hussain:** This does not exist anymore, so I think Angel has implemented a redirect.

**Angel Kemper:** and we fixed that one.

**Jason Beltran:** So we fixed that one.

**Jason Beltran:** It does exist again.

**Ehtisham Hussain:** And so we're good to go on that.

**Ehtisham Hussain:** Yeah, and then I found from the homepage, there was one page as well.

**Ehtisham Hussain:** So I'll keep an eye on these things.

**Ehtisham Hussain:** And I'll keep an eye on these trends.

**Ehtisham Hussain:** Hopefully, it's just like nothing to be concerned about.

**Ehtisham Hussain:** But if it continues to go, then we can take deeper and we can see if we are losing rankings or something.

**Ehtisham Hussain:** So, yeah, so that's pretty much it.

**Ehtisham Hussain:** Like, if I discuss automation, like, what should we do in terms of automation?

**Ehtisham Hussain:** Because Kyle and I were discussing this thing and we were like, this is such a massive opportunity.

**Jason Beltran:** There's like a, if we can get to automated publishing, we can immediately publish like 200.

**Jason Beltran:** And I think we're extremely close.

**Jason Beltran:** And I'll...

**Jason Beltran:** I'll show you what I've done so far, and then I kind of, I'll show you like some of the things that I am fixing on my own, but it would be nice if we just had it kind of like, it'd be clean if we had it from the jump.

**Kyle Gaudreau:** One quick thing before we jump in this, I just don't know who's going to thread on, Ehtisham, let's be careful of how much we publish initially, like.

**Ehtisham Hussain:** Oh yeah, we will trickle.

**Kyle Gaudreau:** Okay, okay, okay, I just want to make sure.

**Jason Beltran:** Because they're all going into draft, and then we're going to go in and like manually post them to make sure that they're posting on like a good schedule, but if we cannot ingest 250 articles at once, that'll be a beautiful thing.

**Kyle Gaudreau:** All right, we're all on the same page, I just wanted to make sure we weren't just like mass posting and potential red flags get, yeah, okay, cool.

**Jason Beltran:** All right, so let me show you what we got going on. I'm back.

**Ehtisham Hussain:** I'm back. Sorry about that. The devs are going to do the bulk of the work here anyway.

**Jason Beltran:** So this is what's being posted to the endpoint that I provided in Trey.

**Jason Beltran:** So we're getting the title.

**Jason Beltran:** We're getting the content.

**Jason Beltran:** The content's all in markup.

**Jason Beltran:** So I'll show you what I do.

**Jason Beltran:** I'm converting the markup into HTML, which is pretty easy to do.

**Jason Beltran:** I wrote a script that makes that happen.

**Jason Beltran:** wrote

**Jason Beltran:** So that's all the blog content, and then we have the excerpt, which is the summary, and then we have the slug, the draft, the SEO title, and SEO description.

**Jason Beltran:** What I'm missing here is the focus keywords.

**Jason Beltran:** So, and I can, so I'll show you what I'm doing in the meantime, but it would be nice to have in the metadata here, like the Yoast focus keywords.

**Jason Beltran:** And then what I noticed is in the content, this is where including the summary and the key points, they're right here and right here.

**Jason Beltran:** We should actually, those shouldn't be part of the content.

**Jason Beltran:** Those should be separate keys.

**Jason Beltran:** So there should be a key that says like summary, and then has the summary, and then key points, and has the key points.

**Jason Beltran:** And then the content should only be the blog content itself.

**Jason Beltran:** So in this instance, it would start at after the key points, which is that gun-wrenching moment.

**Jason Beltran:** That's where it starts.

**Jason Beltran:** So what I'm doing in order to account for that as of today and the way that the current payload is coming through is I've put in a place, and I'm still working on it, as you can see, I have some failures here.

**Jason Beltran:** But what I'm doing is getting the information from the webhook, and then this is where I'm cleaning up and rewriting the script or the markup to HTML.

**Jason Beltran:** And then what I've also done within the script, and this is where I'm getting some failures, but I'm still working on it, is I'm trying to extract the summary and key points from the content and then have them output separately under separate keys.

**Jason Beltran:** And then another thing that I would like in the web book, which we need in order to post it properly, just automate some things, is the categories of the blog.

**Jason Beltran:** Like, what kind of blog is it?

**Jason Beltran:** So even if you sent over, like, the name of the cluster, like, let's just say B2B Dental, that would be good enough where I could kind of remap it to Dental Tips or whatever categories you want.

**Jason Beltran:** Right now, I'm using AI to categorize the content. It reads the content and then categorizes it for me. But it would be nice if we just had that clean since we already have it in the clusters. And then I'm having Claude generate the focus keywords as well. So it would be nice if, rather than having Claude generate some focused keywords, we actually have them come from GrowthX. Claude's making stuff up for me right now, like here's some potential SEO meta keywords. But it would be nice if they came from GrowthX since we already have that metadata in the document.

**Jason Beltran:** Yeah, exactly.

**Jason Beltran:** As long as all of that is being posted to the webhook, we'll be good.

**Jason Beltran:** And then here, I kind of just basically take everything from the webhook, the content, all of these outputs, and then I put it into a JSON format that is compatible with our WordPress instance.

**Jason Beltran:** And then I post the raw JSON over to WordPress.

**Jason Beltran:** All of that's working really well. The only thing right now that I'll fix this morning is the JavaScript that's extracting the key points and summary. Once I have that completed, I can remove these two AI steps and have it all just coming from GrowthX in the payload, and I'll be in a really good place.

**Jason Beltran:** So, just to kind of sum up, it would be nice to have the content, strip the summary and the key points from the content, and have them as separate keys.

**Jason Beltran:** It would be great if the content was not in markup language, but in HTML, but whatever, I think the script I wrote works really well, so that's not a must.

**Jason Beltran:** And then I need the categories, which would be your clusters, and then the focus keywords.

**Jason Beltran:** And other than that, I think we're good to go.

**Jason Beltran:** And once we have all of that, I think we'll be, like, we can shoot off the 250.

**Jason Beltran:** But what I'm doing today should work as well, because we, you know, I have some of these fixes in place.

**Jason Beltran:** So it really just depends on if your developers can get that, those extra data fields posts, you know, in the, in what they're posting to the webhook, that would be excellent.

**Jason Beltran:** It just depends on the speed on that.

**Jason Beltran:** If not, if it's going to take them weeks or whatever, like a next sprint, then we can always just use the fixes I put in place and just send them all through that way.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So, like, on the surface, it kind of sounds like an easy-to-do task because all I have to do is just go in the document and just separate the summary and key takeaways.

**Ehtisham Hussain:** Right now, what we do is we post the title, then we have a summary, key takeaways, then we do the intro.

**Ehtisham Hussain:** I can just move it up and assign it its own headings.

**Ehtisham Hussain:** We can put the cluster manually in there.

**Ehtisham Hussain:** can put the focus keyword in there.

**Ehtisham Hussain:** So, and then I will go to the devs and say, hey, look, is this going to work?

**Ehtisham Hussain:** So I think, yeah, we can, we should be able to do this.

**Jason Beltran:** Yeah, if you could do that and then test it, send me another, you know, test.

**Jason Beltran:** We should be, we should be really good.

**Jason Beltran:** Like, we're very close.

**Jason Beltran:** All right. One other thing in the payload—there isn't an image. I didn't know if we were intending to have an image with the blog or not, but we actually do need the images because the blog tiles have images.

**Angel Kemper:** I have a question too. Are we still having to manually input the related articles?

**Jason Beltran:** So the blog will automatically put in the related articles.

**Angel Kemper:** Cool.

**Kyle Gaudreau:** Generally, I would say we should plan for images to at least have the option. We've had a couple customers who just go without that, but you all weren't set up for that, so we're not pushing for it either.

**Jason Beltran:** Yeah, if we could have an image, that would be great.

**Jason Beltran:** If not, I think we can manually go and build the image.

**Jason Beltran:** Like that's much easier than what we're doing today.

**Jason Beltran:** So either way, I think we'll be good.

**Ehtisham Hussain:** All right.

**Jason Beltran:** It's fun to see it go through and post to the website and it's like, oh, that's great.

**Kyle Gaudreau:** It's such a really...

**Kyle Gaudreau:** Yeah, this will be a huge unlock for sure once we get that in the right rhythm, everything's working well.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Faster signal should mean faster growth.

**Jason Beltran:** Oh, yeah.

**Ehtisham Hussain:** What kind of images are you guys using right now?

**Ehtisham Hussain:** Are these generated to AI or are you sourcing them from stock images websites?

**Jason Beltran:** Stock sites.

**Jason Beltran:** So what we're doing is in Canva, we'll get an image and Angel will go in and manipulate it a little bit to make sure the colors are all very similar. But if we're just getting stock imagery, that works as well.

**Ehtisham Hussain:** All right. I'll look into the image thing as well. I've taken notes for all these requirements. So we'll do another test soon and see how it comes through.

**Jason Beltran:** That's good. I'm excited. This is going to be a game changer.

**Ehtisham Hussain:** So this is all there is from my side.

**Jason Beltran:** Cool. Kyle, did you like looking at Trey again?

**Kyle Gaudreau:** You know, some things look different, some of it doesn't, but you know.

**Jason Beltran:** Yeah, they've changed up quite a bit. So now they have this project format where each of your workflows are within the product.

**Kyle Gaudreau:** Oh, that's huge that you can organize like that now.

**Jason Beltran:** Yeah. And then you can go in and navigate between workspaces. So here's what Angel does on a day-to-day basis building out workflows for monday.com. What's nice is we can go here and then navigate from one to the next, which we never had before. You also have data tables and vector tables for AI.

**Kyle Gaudreau:** Oh, it's so much more intuitive to navigate in that way.

**Jason Beltran:** Yeah, yeah.

**Jason Beltran:** It's really cool what they've done with it, and it's still, I think, intimidating to a lot of folks, but...

**Kyle Gaudreau:** For sure, yeah.

**Kyle Gaudreau:** I think some of the, yeah, just there's a lot of concepts for people to wrap their head around, you know, related to something like Atrey, but it's fun once you can see all those different things and branching and loops and whatever, and you're like, oh, wow, I built this engine, and, you know.

**Jason Beltran:** Yeah, and it's so funny, like, we're actually working on getting, upgrading to enterprise, and we're looking at, like, Workato and a few others just to, like, do comparisons, because we want more people to use Trey, and even our developers, because our developers...

**Jason Beltran:** They've been like anti-iPads.

**Jason Beltran:** It's like makes them so much more efficient, but they feel it's like a threat, I guess.

**Kyle Gaudreau:** I mean, man, the ones that lean into it, it's crazy what they can build.

**Kyle Gaudreau:** Yeah, I think I get it, especially with them leaning into the AI side more and more. There are wild differences in how developers think about that nowadays. We're the types who hire people who are mandatory to be savvy in leveraging AI. But as a result, it's absolutely insane how fast this team can build things. Our platform itself did not exist two or three months ago. It's crazy what they've built and what's coming.

**Jason Beltran:** Yeah, it's pretty cool.

**Kyle Gaudreau:** Yeah, I'm curious—another time to pick your brain about how you interpret and think about things with Workato. They were always like one of the biggest focus areas. They took a very different marketing strategy than we did at the time. We were beating them for a while and then they got ahead of us. I never knew how much in reality—you hear internally about which platform is better, but the reality of it.

**Jason Beltran:** So I'll give you a quick perspective on that. I think all of the automation platforms are at parity in terms of capabilities, even when it comes to AI agents. They all do the exact same thing. There are layers of customization that you can do.

**Kyle Gaudreau:** So Zapier is very much like you can't really do much.

**Jason Beltran:** It's just easy and dummy proof. It's like the iPhone of automation platforms. Then you have N8N, which is more for small business, but it doesn't have those enterprise features. Then you go up to Trey and Workato, and both have customization capabilities and AI agents that are very similar. The UI of Trey is far superior. Workato looks kind of like a child's software—they didn't really put time into the UI. That's a differentiator. And then it comes down to how they price. Trey's pricing structure is much different than N8N and Zapier—they're all varied. For us, it's about looking at their cost structure and what's most appealing to us, and then switching costs. So much is running through Trey.

**Kyle Gaudreau:** I understand why platforms have to think about credits or tasks, but it's hard for someone still in the weeds. I don't know what to expect for how much I'll need. What if I blow through it all? But I want to experiment. It's a tough barrier to entry.

**Jason Beltran:** Yeah, I'd assume that's why everyone has gone to the consumption model, but the consumption model works for cloud because there's greater understanding and teams that focus on it. Same with AI tokens. For something like this, I think the gym membership subscription model is the best. You have three or four tiers, and depending on use, you go from one to the next. You know 20% will use it all, and 80% won't use much—they offset each other. It's just easier to price and everyone digests it.

**Kyle Gaudreau:** Yeah, I would agree with that.

**Kyle Gaudreau:** I got to hop to my next one.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Appreciate the time, as always.

**Jason Beltran:** Looking forward to getting some more automation going soon.

**Jason Beltran:** Sounds good.

**Kyle Gaudreau:** All right, see you, Bye.

**Jason Beltran:** Bye.
