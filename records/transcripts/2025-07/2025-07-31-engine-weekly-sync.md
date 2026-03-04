# Engine Weekly Sync

<metadata>
date: 2025-07-31
time: 18:30 UTC
duration: 19 minutes
organizer: Jo Kaminska (GrowthX)
participants: Darrell Etherington (GrowthX), Jo Kaminska (GrowthX), Carrie Chowske (GrowthX), Feyisayo Odedeyi (GrowthX), Joel Murphy (Hotel Engine), James Winter (Hotel Engine)
fathom_recording_id: 77790522
fathom_url: https://fathom.video/calls/366556349
share_url: https://fathom.video/share/MErYNkJVinAFxYHoZBG8nE5PCoqLd8xa
source: fathom
enriched_on: 2026-03-03 12:00 UTC
</metadata>

---

## Summary

GrowthX's new Hotel Engine team (Darrell, Carrie, Fey taking over from Jo) reviewed content production progress: 10 articles publishing this week with a focus on a new wedding/events vertical, though the CMS currently nests wedding content in the business travel guides category—Joel will create a separate Webflow collection. The team confirmed Webflow API access, discussed shifting analytics focus from impressions/clicks to conversions using Amplitude, and reviewed SEO tooling: Scrunch is showing strong early indicators for Hotel Engine, Peak access is pending confirmation, and GrowthX is exploring lms.text implementation for answer engine optimization alongside continued prompt testing (currently 135 prompts).

---

## Context

Hotel Engine is a B2B travel and hospitality platform operating in the accommodation, events, and wedding planning space. GrowthX handles their content marketing and SEO strategy, currently producing high-volume content across multiple verticals to improve organic visibility and drive qualified traffic. This was the final meeting with Jo Kaminska as the primary GrowthX point of contact; starting next week, Darrell Etherington will lead account strategy with Carrie Chowske and Feyisayo Odedeyi handling day-to-day delivery. The transition was prompted by GrowthX's account allocation, not by any account health issues—Jo emphasized the team is in good hands and collaboration has been smooth.

---

## Relevance

**To GrowthX Delivery:**
- Content production cadence on track: 10 articles per week targeting multiple verticals (business travel, wedding/events)
- Webflow CMS architecture issue: wedding content currently nested incorrectly in business travel guides; Joel handling new collection setup
- Recent Webflow outage caused formatting issues (missing H3 tags); Carrie flagged one article needing manual fix
- Webflow API key now in hand; programmatic SEO pages indexing successfully with no significant crawl budget concerns

**To CheckThat (AI Visibility):**
- Scrunch tool showing strong performance for Hotel Engine with 135+ prompts across categories; Darrell to cross-reference Peak tool results once access confirmed
- lms.text implementation being explored for answer engine optimization; Webflow now supports this natively
- Peak access pending security team discussion with Cloudflare LLM block; team awaiting ETA on removal for marketing site
- GrowthX working with Webflow as design partner; testing insights are anonymized but leveraged across client base

**To GrowthX Business Development:**
- Smooth account transition: three delivery team members taking over suggests this is a stable, ongoing engagement
- Analytics showing steady traffic and engagement growth; Carrie monitoring for conversion signals now that Amplitude access is available
- No red flags or risks identified in this meeting; account appears healthy and on track for continued expansion

---

## Overview

- Content production on track: 10 articles to be published this week
- Analytics show steady growth in site traffic and content engagement
- Webflow CMS structure needs adjustment for wedding content category
- Cloudflare LLM access for marketing site pending security team decision
- Team transition: Darrell, Carrie, and Fey taking over account management

---

## Key Topics

### Content Production and Publishing

  - 10 articles planned for publication this week
  - Fey working on uploading content this afternoon
  - Some formatting issues noted (e.g., missing H3 tags) possibly due to recent Webflow outage
  - Wedding content currently misplaced in business travel guide section

### Analytics and Reporting

  - Quick analytics report prepared with impressions and clicks
  - Shift in focus towards conversions with access to Amplitude
  - Overall traffic and engagement metrics showing steady growth

### SEO Tools and Strategies

  - Scrunch tool showing promising early indicators for Hotel Engine
  - Peak access granted to GrowthX team account
  - Exploring lms.text implementation for better answer engine optimization
  - Cloudflare LLM access for marketing site under discussion by security team

### Technical Updates

  - Webflow API key received
  - Programmatic SEO pages still being indexed successfully
  - Potential removal of old content to free up crawl budget (Joel to provide list)

### Team Changes

  - Jo transitioning off the account
  - Darrell, Carrie, and Fey taking over account management

---

## Action Items

**Joel Murphy (Hotel Engine)**
- Set up new Webflow collection for wedding content, separate from business travel guides
- Slack Carrie list of needed tasks
- Provide list of posts marked for deletion by previous agency

**Carrie Chowske (GrowthX)**
- Tag Joel in Notion re: wedding content Webflow collection issue

**Feyisayo Odedeyi (GrowthX)**
- Add H3 formatting to article missing it while publishing today's content

**Darrell Etherington (GrowthX)**
- Access & review Peak account data; compare with Scrunch prompts

---

## Transcript

**Darrell Etherington:** I never know what the meeting thing is that it's going to open. I just click join meeting and then I'm surprised every time. Is it Zoom? Is it Google Meets? Who knows? It's a fun surprise.

**Jo Kaminska:** They were like double all the meetings.

**Darrell Etherington:** That's because Matthew actually messed up and deleted everybody's meetings and then restored all the meetings and then sometimes doubled up.

**Joel Murphy:** How's it going?

**Carrie Chowske:** Between you and Darrell, Joel, you guys look like you could have some sort of like talk show together or something.

**Joel Murphy:** We could have like a podcast. That's way cooler than anything I could ever come up with.

**Darrell Etherington:** I should grab my guitar that I could put in the background, but I don't know how to play it. I have a Spark amp from my tech journalist days—they sent one for me to review. I also have a ukulele with a pickup, but I never went anywhere with teaching myself.

**Joel Murphy:** I recognize—I have one in my bedroom so I can tinker around when I'm in there. I try to play all the time. You use it or lose it.

**Darrell Etherington:** Yeah, the software modeling and stuff that it does is pretty cool. You can also use it as an impromptu karaoke machine if you want.

**Joel Murphy:** So James has got an interview currently, so we can go ahead and get started. Kali's here as well.

**Carrie Chowske:** We're good. But we just wanted to make sure that Feyisayo got a chance to kind of hear straight from you and your team what it is that we're working on and why. She's been watching our calls and recordings, keeping up to speed on everything. Fey, I'm not going to put you on the spot to introduce yourself unless you want to.

**Feyisayo Odedeyi:** Hi, everyone. My name is Fey. I'm just going to be here taking notes and watching everybody speak, basically.

**Carrie Chowske:** Nice meeting you. Anyway, I'll just keep it short and sweet. In terms of content, I wanted to make sure that we're constantly checking in on what we're delivering. James doesn't want to approve the refreshes, which speeds us up a lot. We might ask for a spot check here and there. Our plan is to publish 10 articles this week. Fey was going to work on that this afternoon, so we should have a few of those up today.

One thing I noticed the other day on the site was the way that the new wedding content is going in the business travel guide. This is one of the new verticals we're working in, one of the new content clusters. It's getting tossed in with business travel guides, but it's more consumer level than B2B.

**Joel Murphy:** Yeah, I agree. That's weird. Is that just because the CMS you guys post into has that URL structure? I think we probably don't have a wedding collection set up, so we would need to have one.

**Carrie Chowske:** My experience with Webflow is when you create a new collection, you have to create a new template and schema. You can copy them over, but you have to do those two things separately. Depending on the permissions we have, we may not have access to do that. So I might need this to come from your end.

**Joel Murphy:** Okay, yeah, we can do that. Do you mind noting it in Notion for me?

**Carrie Chowske:** Tag me. And Fey, while I'm in here, this one looks like maybe it didn't get the H3, like that other one we had an issue with. While you're publishing, if you could fix that, that'd be cool.

**Joel Murphy:** By the way, I'm assuming you guys saw about the massive outage that Webflow had this week. There was an issue where even if you went into a post and hit H3 and saved, it didn't save.

**Carrie Chowske:** It could have been. We had some issues when we were copying things over. Sometimes Webflow decides it doesn't want to keep your formatting regardless of what you've done.

**Darrell Etherington:** Webflow can be... I'll say fun.

**Carrie Chowske:** That's a good way of putting it. I think my saying is always, technology is great until it isn't. The one time it goes wrong is when you really need it to work.

**Carrie Chowske:** I did work up a quick analytics report, but it is just the, you know, impressions and clicks.

**Carrie Chowske:** I know we talked about wanting to shift that, but we do have it.

**Carrie Chowske:** If y'all want it, I don't need to go over it unless you guys want to see it.

**Carrie Chowske:** But it's there if you'd like to reference it.

**Carrie Chowske:** I just kind of summed up some stuff from Search Console just really quickly for you.

**Carrie Chowske:** Cool.

**Carrie Chowske:** And then with that, we'll show

**Carrie Chowske:** It's kind of our focus to conversions with access to Amplitude, which we talked about already on Slack, Joel.

**Carrie Chowske:** So I think we're probably good there.

**Carrie Chowske:** It can go to this team at GrowthX.

**Carrie Chowske:** I'll just, I'll tell you what I'll do instead of putting this in Notion too.

**Joel Murphy:** I'll just leave you a message in Slack with all the things that I need from you.

**Joel Murphy:** Does that work?

**Carrie Chowske:** That works.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** And then I think Darrell was working with, to get, so we can cross-reference peak with scrunch, with our scrunch prompts, correct?

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** So right now I just have that scrunch set up and we'll look at the, we can diff the list, but like, yeah, the scrunch is actually working pretty well.

**Darrell Etherington:** Yours is one of the ones that is populating well and actually showing some promising early indicators.

**Darrell Etherington:** I'm going to share the screen so that I can talk to it.

**Joel Murphy:** Darrell, did you get access to Peak?

**Joel Murphy:** I talked to James the other day.

**Joel Murphy:** said that you should have it and your, the GrowthX team account had it, but I just want to confirm.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Here go.

**Darrell Etherington:** If the team account has it, then I have it.

**Darrell Etherington:** I got to check and dip in so that I can see that.

**Darrell Etherington:** All right.

**Darrell Etherington:** But I haven't had a chance to look at it yet.

**Darrell Etherington:** But if the team account has it, then I'll have it.

**Darrell Etherington:** Cool.

**Darrell Etherington:** Let's see.

**Joel Murphy:** Can you see this now?

**Darrell Etherington:** Yep.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Great.

**Darrell Etherington:** So this is your dashboard for in Scrunch, and we have the prompts in here organized by category.

**Darrell Etherington:** And then showing your competitor's presence.

**Darrell Etherington:** Like, this is actually really strong.

**Darrell Etherington:** I think, given the relative maturity of the different players in here, and given the overall market share, I think this is pretty good.

**Darrell Etherington:** But, you know, the Scrunch thing generally is just a directional indicator.

**Darrell Etherington:** Like, it's not super authoritative.

**Darrell Etherington:** Right.

**Darrell Etherington:** Because it's kind of like a Nielsen rating type system, right?

**Darrell Etherington:** Like, it's just kind of like just suggesting a bunch of things to test, to spot test, like how you guys will rank in those queries, where those queries to be done.

**Darrell Etherington:** By other human beings, but it's not like in the same way that like GSC would provide you actual results of searches hitting the thing.

**Darrell Etherington:** It's like a sampling, right?

**Darrell Etherington:** But I think directionally it's pretty useful.

**Darrell Etherington:** And the thing to do once we get the peak things checked against this is like reference.

**Darrell Etherington:** And we're really interested.

**Darrell Etherington:** I think Marcel's talking to peak as well, like CEO to CEO, just to see how their tool compares.

**Darrell Etherington:** Because we're kind of like, we're not like pot committed to any tool at the moment.

**Joel Murphy:** It's too early in the mix to do that.

**Darrell Etherington:** So we're really seeing what's best in class.

**Darrell Etherington:** But we work really close with them in almost like a design partner relationship to keep on top of stuff as it's emerging and best practices and stuff as it's emerging.

**Darrell Etherington:** I mean, we just had a discussion about lms.text—it's a way to serve your entire site to the answer engines so the bots that crawl them can produce better results. We're experimenting with clients on this, and we're happy to loop you in. It's not an upcharge; it's just something we're doing.

**Joel Murphy:** Webflow just started supporting it, actually.

**Darrell Etherington:** So Webflow is also, I mean, it is unfortunate they had that big outage, but they're also a client, and we work pretty closely with them, too, right?

**Darrell Etherington:** So, yeah, we get the advantage of scale there.

**Darrell Etherington:** Like, we get to test across a number of clients and then kind of get the results.

**Darrell Etherington:** Obviously, anonymized, there's no, like, sharing of data or anything, but there is sharing of, like, insights, right?

**Darrell Etherington:** But, yeah, I think probably makes more sense to dive into this more once I've had the chance to test it or look at it more closely against peak.

**Darrell Etherington:** But it's something we're keeping an eye on, and if we have any specific areas where we want to test prompts, just let us know, and we can do a whole new batch against that.

**Darrell Etherington:** Right now we have 135 total, but we can definitely build that list out or build it in concert with your priorities.

**Joel Murphy:** Cool.

**Joel Murphy:** Sounds good.

**Joel Murphy:** I did have an update I mentioned last week that the Cloudflare thing blocking LLM.

**Joel Murphy:** So security team told me that they're actively discussing with Cloudflare how to optimally set this up, how we want to set it up.

**Joel Murphy:** I shared my opinion that we want them to access anything on the marketing site.

**Joel Murphy:** Yep.

**Joel Murphy:** They don't have an ETA, but hoping for some answers soon.

**Joel Murphy:** I'm hoping it's just like, yeah, turn it on and not some big undertaking post whatever decision they have to make, but that's the latest.

**Joel Murphy:** So hopefully it doesn't take long.

**Darrell Etherington:** Okay, cool.

**Darrell Etherington:** I don't know much about how it works under the hood despite paying attention to the announcement—they did a great job on the PR. For us, the only concern is that we can still index, serve, and have crawled the pages we're producing.

**Joel Murphy:** Yeah, exactly.

**Carrie Chowske:** Was there anything else? Actually, I don't think so. We were getting access to the Octave API playbook. When we can, I looked at scheduled refreshes—there's a roundup of the best cards for travel and stuff, so that would be a good time to refresh that. We got the Webflow API key today. We talked about Amplitude. I'll send you that Slack message with what I need. The beginning phase is business as usual for a few weeks. Everything's steadily climbing, which is good. Even if we focus on conversions, you need eyeballs on the site. People are going to your site and the content we're creating, and that's growing. All signals are good.

**Darrell Etherington:** One thing—the easy fix for the wedding content might be using your events category. It might work temporarily and look fine when you land on a page with events and a wedding thing as an event. Otherwise you'd be thinking about building a whole consumer vertical, but I'm not sure if it's early in testing to do a massive web architecture change.

**Joel Murphy:** No, I mean more like a quick fix—let's put this in a place that makes sense on the site. The events thing might work.

**Carrie Chowske:** These are our Hotel Engine events that we're creating for socializing. I couldn't get into Webflow yesterday during the outage to check the CMS categories. But I think you bought a site related to wedding planning, so we probably want it in its own bucket for tracking purposes.

**Darrell Etherington:** There were four articles in there—one was more internal events, and three were more wedding-focused. But I'd rather have one redirect than a dozen.

**Carrie Chowske:** I'll look and figure out what I can and loop you in. Is there anything else you need us to address this week? Are we good with business as usual?

**Joel Murphy:** As far as I know. Did I owe you something from last week? We brought up programmatic SEO and how to get indexing. I don't remember if I owe you a list.

**Darrell Etherington:** I think you gave it to us during the meeting. We're watching to make sure the stuff is getting picked up and indexed as we publish. That was our main takeaway, and it looks like it is based on Carrie's analysis. There's no significant flag that it's eating up crawl budget.

**Joel Murphy:** Right. We talked about potentially removing things to free crawl budget. Don't I owe you a list of posts the previous agency marked for deletion?

**Jo Kaminska:** Yeah, that would be good to send out.

**Joel Murphy:** I'll make a note and give you that.

**Jo Kaminska:** Anything else, team? I just wanted to say thank you, Joel and Kali, for the collaboration so far. Starting next week, Darrell, Carrie, and Fey will be handling the account. Thanks for the collaboration—you're in good hands.

**Joel Murphy:** Thank you so much. Lovely to work with you.

**Darrell Etherington:** Jo's not going anywhere, so maybe I'll see her again sometimes.

**Jo Kaminska:** I have to do this with all the Sprint customers, so I'm used to it already.

**Carrie Chowske:** Well, if that's all, that's great. We'll get a few minutes back in our day. I'll send you a message on Slack, Joel, and we'll get everything sorted.

**Joel Murphy:** Sounds good.

**Carrie Chowske:** Thanks a lot. Bye.
