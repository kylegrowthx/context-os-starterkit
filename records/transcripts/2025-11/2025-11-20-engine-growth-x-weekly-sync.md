# Engine <> Growth X - Weekly Sync

<metadata>
date: 2025-11-20
time: 19:30 UTC
duration: 30 minutes
organizer: carrie@growthx.ai
participants: Carrie Chowske, Kyle Gaudreau, Joel Murphy, Cole Parker, Kali Wootton, Rory Conroy, George Haikal, Feyisayo, James Winter, Barry Goodnight, Colm Shalvey, Luke Tubinis
fathom_recording_id: 103277864
fathom_url: https://fathom.video/calls/480689561
share_url: https://fathom.video/share/Um33UPgVVsu7QjepNa1zssMcNc2sJbK3
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Engine's content marketing partnership reviewed strong performance gains in experimental content clusters: the Expense & Financial Management cluster grew 23% over two months, with Policy Enforcement showing particularly strong traction, while industry-specific content (Energy & Utilities, Construction & Infrastructure) showed clear uplift following the experiment launch. Joel requested a new measurement approach beyond session counts to prove ROI to stakeholders—the team will implement content-to-conversion correlation tracking in Amplitude, likely using a data-layer tagging solution in the CMS. Key upcoming initiatives include launching the NGINX waitlist (today), rolling out a revised rewards program in January 2026 with higher rates and statement credits for Direct Bill/NGINX users, and completing holiday content to ensure smooth coverage through year-end.

---

## Context

GrowthX is providing content marketing services to Engine (Hotel Engine), a B2B travel and hospitality operations platform. This weekly sync between Carrie Chowske (GrowthX Content Lead) and Joel Murphy (Engine Content/Product), with supporting input from Kyle Gaudreau (GrowthX Analytics), reviews content performance, discusses strategy iterations, and aligns on upcoming product launches and content initiatives. The partnership is structured around experimental content bets: testing new topic clusters (Expense & Financial Management, Industry-Specific verticals) and monitoring performance through session volume, engagement metrics, and (increasingly) conversion correlation analysis.

---

## Relevance

**To GrowthX Delivery:**
- Experimental content approach is delivering measurable results (23% growth in Expense & Financial Management cluster, clear session jumps in industry-specific verticals)—validates testing-based content strategy and shows potential for scaling to other accounts
- Request for conversion-correlation tracking reveals need for more sophisticated measurement tooling (data-layer tagging in CMS, Amplitude event setup) that GrowthX should consider building as a repeatable service offering
- Glossary content system (Webflow template/collection) is now production-ready; this could become a reusable component for other clients with complex topic structures

**To GrowthX Business Development:**
- Engine account is engaged, collaborative, and actively seeking deeper analytics—strong signal for account health and expansion (e.g., additional analysts, larger content scope)
- NGINX waitlist launch and rewards program update (Jan 2026) indicate Engine is actively shipping new products; GrowthX may have opportunities to create launch-supporting content or expand into paid/product-led growth content

**To CheckThat:**
- LLM performance monitoring continues to be critical to Engine's strategy: ChatGPT volatility (5.1 model updates reducing citations), Claude's rapid growth across the portfolio, brand confusion between Hotel Engine and Engine in LLM outputs
- Content discoverability via LLMs remains a key metric Engine tracks; checkThat's AI visibility index would be directly valuable for ongoing optimization

---

## Overview

- **Performance:** The Expense & Financial Management cluster grew 23% in 2 months, with Policy Enforcement content showing strong traction.
- **New Metric:** Joel requested a conversion metric (beyond sessions) to prove content ROI to stakeholders. The team will explore a scalable solution, likely a data layer tag for Amplitude.
- **Product Updates:** The NGINX waitlist launches today, enabling content promotion. A new rewards program (Jan 2026) will offer higher rates and statement credits for Direct Bill/NGINX users.
- **Holiday Prep:** Content for the next two weeks is nearly complete to ensure a smooth holiday period.

---

## Key Topics

### Content Performance & Reporting

  - **New Looker Dashboard:** A new dashboard now cohorts experiment content by subcategory (e.g., Policy Enforcement, Receipt Chaos) to track performance.
  - **Expense & Financial Management Cluster:**
      - Grew 23% over the last two months.
      - **Policy Enforcement:** Strongest growth, with session volume comparable to older, established content.
      - **Direct Bill:** Performing well.
      - **Receipt Chaos:** High growth rate is misleading due to a low session count (81).
  - **Industry-Specific Cluster:**
      - Shows a clear jump in sessions since the experiment began.
      - **Energy & Utilities:** Rapid growth.
      - **Construction & Infrastructure:** Steady growth; more content is being published this week.
  - **LLM Performance:**
      - **ChatGPT:** Still the top source for sessions. Recent volatility in citations/position may be due to model updates (e.g., GPT-5.1).
      - **Claude:** Growing rapidly.
  - **New Reporting Metric:**
      - **Goal:** Move beyond sessions to show content's impact on conversions.
      - **Method:** Analyze the correlation between viewing experiment content and converting.
      - **Rationale:** Provide a more robust ROI narrative for stakeholders.
  - **Implementation Strategy:**
      - **Short-Term:** Carrie will provide a Google Sheet mapping content to subcategories for Joel's analysis.
      - **Long-Term:** Explore a scalable solution, likely a data layer tag in the CMS to pass content categories directly to Amplitude.

### Upcoming Initiatives

  - **NGINX Waitlist:**
      - Launches today.
      - Joel will confirm when content promotion can begin.
      - **Rationale:** Gauge organic interest in the product.
  - **Rewards Program Update (Jan 2026):**
      - **Key Changes:** Higher reward rates and statement credits for Direct Bill/NGINX users.
      - **Content Strategy:** Joel is clarifying if statement credits are exclusive to Direct Bill/NGINX to determine the primary benefit to highlight.
  - **Glossary:**
      - A Webflow template and collection exist.
      - Joel will review the setup today to unblock content creation.

### Logistics & Holiday Planning

  - **Content Pipeline:**
      - This week's content is published.
      - Next week's content is due today.
      - Post-Thanksgiving content will be delivered by Monday to get ahead.
  - **Holiday Schedule:**
      - No meeting next week.
      - Joel is out Nov 26–29.

---

## Action Items

**Joel Murphy (Engine)**
- Review Webflow glossary collection/template; confirm go-ahead to Carrie
- Define Amplitude event/field for content tags; coordinate CMS/data-layer tagging w/ Kyle
- Confirm NGINX waitlist live; notify Carrie to add CTAs/mentions
- Confirm rewards statement-credit eligibility; notify Carrie to update content

**Carrie Chowske (GrowthX)**
- Send Joel Google Sheet mapping content to experiment buckets
- Add NGINX waitlist CTA comments in articles for Joel; implement on approval

---

## Transcript

**Carrie Chowske:** I almost forgot to do this agenda for today. I usually do them in the afternoon, the day before, and I didn't because I was working on hand-off stuff and did it this morning. My head's spinning.

**Carrie Chowske:** It's Joel.

**Joel Murphy:** Hey, guys. How are you?

**Kyle Gaudreau:** Good. About yourself?

**Joel Murphy:** Oh, extremely hectic day.

**Carrie Chowske:** Relatable.

**Kyle Gaudreau:** Hopefully, you know, this baseline for you is not moving each week. I feel like you've been under a lot of that.

**Joel Murphy:** You've had a lot of those recently. So hopefully it's not just normalizing and compounding to even be a crazier week each week for you. I think it might be.

**Kyle Gaudreau:** Just an observation.

**Joel Murphy:** Yeah, I think it might be, man, unfortunately. But whatever, you know, comes with the territory. I just got surprised with, hey, we're launching today on a thing that's the NGINX waitlist. So surprise, today's the day.

**Kyle Gaudreau:** I do recall many times it felt like this time of year being in-house tended to be the craziest time. Have the holidays coming, have yearly planning that almost always is later than it should be. Doing all these other things and trying to get ahead before the holidays. It's always a fun balance.

**Joel Murphy:** Yeah, it's extremely fun. But I'll say this, it's better than it was when I was at Deal because at least everybody at Engine is also going to celebrate Thanksgiving and most of the same holidays, whereas Deal was just like, you know, all over the place.

**Kyle Gaudreau:** Yeah, that's an interesting one.

**Carrie Chowske:** I like doing it in retail because of Black Friday and everything—you were doing Christmas stuff in August, sometimes July, probably even earlier now. But it was nice because by the time Christmas came around, everything was really dead because nobody does a whole bunch of marketing in January or February in retail. So you're not doing anything in December. We won the office decorating contest every year because we had plenty of time to decorate.

**Joel Murphy:** Interesting. I'm jealous.

**Carrie Chowske:** I'm not, I didn't like that job very much, but I liked the group of people I worked with. I worked for a national retail chain.

**Joel Murphy:** Well, maybe I'll pivot to that in my next.

**Carrie Chowske:** Oh, I don't know if I could do it anymore. The constant feedback on small details—oh, this is the wrong shade of pink or something. That kind of stuff was like, ah.

**Joel Murphy:** Yeah, I can imagine.

**Carrie Chowske:** I don't have a ton of anything groundbreaking to go over today, but just a few things I wanted to make sure we touched base on before we're not meeting in person next week. Content for this week's already been published and I should have everything for next week to you today. I'm almost done with it, actually. My hope is to try to get you the content either tomorrow or at the very latest Monday so that you've got it ahead of time. And we're not playing catch up when we come back.

**Joel Murphy:** Okay, I will. I still have my Friday time blocked out, but I have nine meetings tomorrow. So if I don't make it, I'll do it Monday for sure.

**Carrie Chowske:** Not a problem. I just want to make sure you have it so that when you do have the time, it's there waiting for you. So you're not waiting on me.

**Joel Murphy:** That's all I'm trying to get done.

**Carrie Chowske:** And then the other thing was for the glossary—I saw there's a collection and a template in Webflow. Is that the correct one I was looking at?

**Joel Murphy:** Yes, it should be. I haven't had time to put my eyes on it to make sure it's buttoned up, but yeah, you are looking at the right thing.

**Carrie Chowske:** Okay. Yeah, I mean, just let us know. We can start adding those in when that's ready to go. I just didn't know. I saw it in there and was like, I need to ask about this. I know we left it kind of with you having somebody build that out. So as long as we're moving forward on it, the answer is totally fine with me.

**Joel Murphy:** Cool. All right, yep. Sounds good. I'll take a look at that probably today. Just, like I said, running around like a chicken with its head cut off.

**Carrie Chowske:** It's okay. I only found it because I was digging around looking for product screenshots. The problem is, I can pull things from anywhere on the site, but within the CMS, you can't pull anything from just the regular assets for the site without actually just finding them and uploading them. It's so dumb.

**Joel Murphy:** It's so dumb. Yes, I hate that. God, I have run into so many things with Webflow this week that just really pissed me off, and that was one of them.

**Carrie Chowske:** Yeah. It's really great in terms of building individual pages, but the content management side of it is not my favorite. I'll say that.

**Carrie Chowske:** But yeah, using it to build pages, I had to fix something on the fly the other day because I didn't want to spend another day waiting to send it back and get another answer. I went in and fixed it myself. And I was like, actually, this is pretty easy once you figure out how it works.

**Joel Murphy:** Like, it's really easy to use. But yeah, I'm going to figure out the weird, stupid quirks that exist. I could go on, but I'll stop.

**Carrie Chowske:** I hear you. Okay, let's just look at some performance stuff really quick. I set up a second cohorting group in Looker for our bets and experiment. I hate the way this scrolls—when you get your mouse over one of the charts, it won't scroll. You got to get outside it. There's a second one down here by subcategory. This is just the ones from the experiment: Expense and Financial Management and Industry-Specific clusters. There's a non-experiment category that we can filter out. It would create weirdness if I broke this out any further. But the ones that are industries are in here, and you can look at just those. We can also look at just the expense management ones—the policy enforcement. This one is Direct Bill and NGINX, right now it's just Direct Bill and then Receipt Chaos. So you can see the individual ones too and how they're doing. The expense and financial management cluster grew by about 23% over the last two months. Policy Enforcement had the most growth, which makes sense since we did the most content there, but it's doing really well. It's pretty equivalent to the number of sessions we're seeing for some older, established content. So it caught traction fairly quickly. The Direct Bill stuff is doing pretty well also. Receipt Chaos has huge growth because it was brand new, but it's still only 81 sessions.

**Joel Murphy:** So I didn't want to give you the false inflation there.

**Carrie Chowske:** Yeah, I appreciate that. That's just for the Expense & Financial Management cluster, not the entire cluster. This is just that topic cluster for these subcategories.

**Joel Murphy:** That's, so it's, anyway, we're able to exclude those as well.

**Joel Murphy:** So we can look at just the experiments.

**Joel Murphy:** Can you help me out with a list of the content that goes with each one of these buckets? I want to see if I can surface any conversions that have come from any of this stuff. I need a way to group it together so we can say more than just sessions.

**Carrie Chowske:** Do you just want a Google Sheet or Airtable interface?

**Joel Murphy:** Just do a Sheet. I think I can make that work. I'm thinking—what's the easiest way for us to group this stuff so Amplitude can use it? I know we talked about that before.

**Carrie Chowske:** Yeah, we just never got anywhere with it. Leave that with me. I'll figure that stuff out. You can always go back into that interface. I know they're grouped by those categories, but I can set up any view you want so you can see it in real time as opposed to just a static spreadsheet.

**Joel Murphy:** Well, what I need is a way in Amplitude to look and see—I'm not necessarily expecting a direct one-to-one, but I want to see: did they view any of the stuff that we're seeing grow with sessions, and did they convert? Like, a correlation between viewing the two?

**Carrie Chowske:** I'm hoping we'll see some of that. The engagement on this is pretty high. Those engaged sessions on GA4 are about the time spent on the page, correct, Kyle?

**Kyle Gaudreau:** Yeah, basically, it's helping you understand things like bounce rate, factoring in whether they actually engaged in a meaningful period of time.

**Carrie Chowske:** And the rates on these are really, really strong.

**Joel Murphy:** So hopefully, that might be the one thing GA4 does better than Amplitude—it already has a setting for engaged sessions, whereas I have to put in parameters in Amplitude. I don't expect to see direct causality, but I was looking into this last week for our customer stories and did see correlation between viewing those and converting. I saw maybe a trend for causality, but it wasn't a big enough sample size to confirm. It would probably be the same with this.

**Carrie Chowske:** That reminds me, I did start adding in references to those customer stories in content. I appreciate you noting that. Hopefully that'll help too because it's strong, and we're trying to work it in naturally instead of just dumping it somewhere.

**Joel Murphy:** That's where I'm at now, but I think we're getting there. It's really interesting data to come across and realize how long these things were just in PDFs that you couldn't find. We've been shooting ourselves in the foot repeatedly. But yeah, cool. I'll work on that.

**Kyle Gaudreau:** Yeah, I think the challenge is making it repeatable. We can do a static analysis where we give you a spreadsheet you can filter with regex, but as we publish more content, we need to think about how to handle this systematically. The spreadsheet is probably a good stopgap.

**Kyle Gaudreau:** One of the ways I've done this in the past is tagging things in the data layer as it comes through, and then Amplitude can read that. So the question is: is there a process we can set up so that as something is published by us, it's tagged and then passed through the data layer that Amplitude can pick up?

**Joel Murphy:** Yeah, that's exactly what I was thinking of. I just have to figure out what that thing is.

**Kyle Gaudreau:** I can create any setting in the CMS. You just have to figure out what Amplitude can pick up. Then there's backfilling it, which is another bit of a challenge.

**Joel Murphy:** That'll suck, but we'll do that.

**Carrie Chowske:** I'm wondering if there's a way to connect Airtable and Amplitude, maybe through Zapier or something, since we do a lot of tagging in Airtable. Let me check what their integration looks like.

**Joel Murphy:** I wish I could rewind time and just categorize all this stuff in different subdirectories. That would have been easy, but no one thought of that when Webflow was set up.

**Kyle Gaudreau:** I think the other thing we should weigh as we go through this is whether we're seeing a lift in other places—branded search traffic, direct traffic. There's noise around those segments, but if you see growth curves following similar patterns, we can make arguments about attribution. It's easier for clients where we're the only ones producing content. With many people involved, it gets complicated. What you mentioned is good logic—it probably undercredits the bigger picture, but it is what it is.

**Joel Murphy:** We can figure out what's there and whether there's a story to be told. I'm not looking for something to post in announcements. It's more about being able to say: if I report that sessions went up, people will ask what that means. I want to answer: here's the correlation with conversions, here's why it's fuzzy, don't take this as absolute truth.

**Kyle Gaudreau:** That makes sense. I think this is a good time to do it. Generally, in our engagements, we see upticks around month three and month six. We're at that point now where we're starting to understand traffic segments better and what's working. The engagement points that are actually turning into conversions are important to understand. We should look at whether anything is disproportionately better than we realized. Sessions alone doesn't surface that.

**Joel Murphy:** Cool. All right.

**Carrie Chowske:** Sounds good. If we wanted to connect Airtable and Amplitude, we'd probably use Zapier. It looks like it's possible—you can connect it to an event in Amplitude. We just have to decide which field to use.

**Joel Murphy:** Yeah, I've never gotten a straight answer about Zapier. Nobody officially owns Amplitude. So I'll just take the approach of creating a field and bubbling it up to Amplitude directly. Less people to talk to.

**Carrie Chowske:** Understood. That's the shortest path, the least resistance.

**Carrie Chowske:** And then the second part of those bets was the industry-specific content. You can see a pretty clear jump when we started doing that. There are a few that are categorized there that weren't necessarily part of the original work, so there's some artificial inflation. But if you look at that within the experiment, we're seeing pretty strong growth with Energy & Utilities specifically, and then steady growth with Construction & Infrastructure. This week has a couple construction-specific articles coming. Claude is still growing pretty rapidly for you. ChatGPT is still the strongest number of sessions, but search data is a little volatile at the moment. We're seeing increases in citations and position again.

**Kyle Gaudreau:** Some of what I've been hearing in the past week is that ChatGPT 5.1 and recent changes have led to less citations happening. Data shows they're broadly seeing fewer citations referenced in outputs. Now it's upticking again, so maybe they're adjusting. Because they're so dominant, anything that happens creates wild ups and downs.

**Joel Murphy:** If citations go down, have you seen any effect on referrals directly from ChatGPT?

**Kyle Gaudreau:** If there are fewer links being shown, referral traffic would be going down. But the data is mixed. I'm finding Claude is increasing quite a bit across our accounts, so it's not just a massive drop-off for brands seeing fewer citations. It's hard to gauge at the moment, but it seems to be going up again. Maybe they're refining things.

**Joel Murphy:** I haven't seen significant changes in our form submissions at Engine, but I saw one from a friend's business with a ChatGPT UTM source. Hard coding that value. I wonder if that person found them in a general inquiry with a citation as a suggested solution, or if they searched specifically for that company.

**Kyle Gaudreau:** That's the challenge—how to think about brand on brand in the LLM world. There are cases where it can go either direction. We should keep optimizing for non-brand intent, but also seed how LLMs talk about your brand in different ways. Conventionally, we'd avoid product mentions in top-of-funnel content, but is that rule still valid? We're seeing our phrases parroted by LLMs, which gives us surface area to ensure they're thinking about you correctly. The example you're facing—LLMs confusing Hotel Engine with Engine—is clear, though hopefully improving.

**Joel Murphy:** Yeah, I could see that. Engine is a tough word to search for. It encompasses so many things. But Hotel Engine—there's only one Hotel Engine. It used to be us. Always the fun branding exercise.

**Kyle Gaudreau:** I'm working on building this with my team—dedicated support around analysis and insights, both internally and externally, to understand what we're learning across brands. We're developing wider experimentation around AEO that we can stand up in various places and share learnings.

**Joel Murphy:** Cool. Luke had some AEO notes he's going to send me. It's week two for him, but he said he's verified it works.

**Kyle Gaudreau:** Looking forward to it.

**Carrie Chowske:** I think that's all I've got. Anything else you need from us, Joel, before we don't see you for a couple weeks?

**Joel Murphy:** Yeah, a couple things. The NGINX waitlist goes up today. I'm thinking we can start working with the NGINX stuff you planned, soon. I'll verify, but the idea with starting now rather than in two or three weeks is just to gauge organic interest. We're running a banner on the homepage, so I'm thinking why not put up content about it or that mentions it—mentions and other things in the existing content. I'll let you know. The other thing is our rewards program is changing in January for new and existing customers. The reward rate is higher, and for Direct Bill and NGINX customers, they'll be able to use those rewards to pay their Engine balance—statement credits, which is new and valuable. Some people don't have enough booking volume to reuse points for bookings, so statement credits are a key benefit.

**Carrie Chowske:** I'm assuming that's only with Direct Bill, right? You have to have Direct Bill set up first to be able to do that.

**Joel Murphy:** I asked that yesterday and haven't gotten an answer yet. They're like, hooray, statement credits. And I'm like, well, what if I don't use Direct Bill or NGINX? I just use my Engine card. There's no Engine balance for me to apply points to. So are we going to still lead with statement credits as our main benefit or should it be the rewards rate? But hey, also, you can do this if you're a customer that pays us monthly. I haven't gotten an answer yet.

**Carrie Chowske:** Yeah, we can. I can add CTAs on anything relevant that we've got. But for the waitlist—hold off on that. Let me confirm that the NGINX waitlist is officially live now.

**Joel Murphy:** Hold off. Let me confirm that, yes, this is out of the gate officially now.

**Carrie Chowske:** I'll tell you what I can do. I'll leave some comments for you in the articles that you've got in production, and you can say yay or nay when you're handing them back. You might know more at that point, and then it's a quick reminder that, oh yeah, we can go ahead and talk about it. You don't have to keep that in your brain.

**Joel Murphy:** Yeah, thank you.

**Carrie Chowske:** Yeah, not a problem. We'll start working on adding that in as soon as we know it's a go.

**Joel Murphy:** Cool. Just a heads up, we're off Thursday and Friday, and I'm taking Wednesday, so I'm sure you guys are doing something similar. I'll try to enjoy it. We'll see if I get to enjoy it. I hope so.

**Kyle Gaudreau:** Yeah, yeah, yeah.

**Joel Murphy:** Good luck. All right.

**Carrie Chowske:** Talk to you after the holiday. See you guys. Thanks. Bye.
