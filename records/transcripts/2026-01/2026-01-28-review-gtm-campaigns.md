# Review GTM Campaigns

<metadata>
date: 2026-01-28
time: 00:05 UTC
duration: 34 minutes
organizer: jason@growthx.ai
participants:
  - name: Imran Patel
    email: imran@syftdata.com
    company: SIFT
    role: GTM Engineer / Founder
  - name: Jason Gong
    email: jason@growthx.ai
    company: GrowthX
    role: Founder
fathom_recording_id: 117654318
fathom_url: https://fathom.video/calls/545142666
share_url: https://fathom.video/share/ju9pj3UizXxqf5dnRa8b8cSaVQg1sxqA
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

Imran (SIFT) demoed a Clay-based LinkedIn engagement campaign that automatically captures and enriches post engagers, assigns personas and intent, and generates personalized outreach. Jason will take the POC in-house with HubSpot filtering and Instantly email expansion, while planning a separate website de-anonymization campaign.

---

## Context

This meeting was a hands-on walkthrough of an always-on LinkedIn engagement system built by Imran (SIFT) for Jason (GrowthX). The system uses SIFT webhooks to detect LinkedIn post engagement, auto-enriches ~90% of contacts, then routes them through Clay for persona and intent tagging before triggering personalized outreach. Imran presented both a LinkedIn-direct workflow (immediate) and a website de-anonymization email workflow (lower LinkedIn risk). Jason is preparing to run the LinkedIn campaign in-house and wants to expand coverage by monitoring team posts, competitor posts, and keyword triggers via Trigify.

---

## Relevance

**Product & Operations**
- Testing a new always-on LinkedIn engagement workflow that feeds post engagers into Clay for automated categorization and outreach
- Expanding lead source monitoring beyond Jason's posts to team posts, competitor posts, and keyword topics
- Building systems to support DIY execution at lower cost than agencies

**GTM & Demand Gen**
- Implementing SIFT webhooks + Clay automation to scale personalized outreach without manual work
- Adding email channel to reduce LinkedIn account risk (200-250 connection request/month limits)
- Integrating HubSpot filters to prevent redundant messaging to existing contacts
- Testing general copy strategy to enable scale across multiple lead sources

**Pricing & Vendor Strategy**
- SIFT pricing model: 1 credit per person per month (flat, regardless of activity volume or distribution channels)
- Services alternative: SIFT offers GTM engineering support (enrichment, Clay setup, HubSpot plumbing) as a lower-cost alternative to agencies
- Referral to Kamil (42 Agency) for broader HubSpot strategy beyond SIFT's scope (tracking, attribution)

---

## Overview

- **POC Handover:** Imran will transfer the Clay POC table for the LinkedIn engagement campaign to Jason, enabling immediate use.
- **DIY Execution:** Jason will manage the campaign internally, integrating HubSpot filters to prevent messaging existing contacts and adding email outreach via Instantly.
- **Website De-anonymization:** This will be a separate email-only campaign to avoid risking LinkedIn account limits (200-250 requests/month).
- **SIFT Pricing:** The model is 1 credit per person per month, regardless of activity volume or webhook destinations.

---

## Key Topics

### LinkedIn Engagement Campaign POC

  - Imran demoed a POC automating outreach to LinkedIn post engagers, built in Clay.
  - **Workflow:**
    1.  **Trigger:** SIFT webhook fires on a user's post engagement.
    2.  **Enrichment:** SIFT auto-enriches \~90% of contacts; Clay fills the rest.
    3.  **Categorization:** Clay assigns persona (e.g., "Director+ Marketing") and intent (e.g., "AU SEO").
    4.  **Action:** Clay generates a personalized LinkedIn DM with a relevant offer.
  - **Flexibility:** The workflow can route leads to external tools like HeyReach or Instantly based on intent.

### Campaign Execution & Refinements

  - Jason will take over the POC for internal execution.
  - **HubSpot Integration:** Jason will add a Clay step to filter out existing contacts before outreach.
  - **Email Outreach:** The campaign will be expanded to include email, leveraging growthx.ai's Instantly setup.
  - **Lead Source Expansion:** The goal is to monitor more sources (team posts, competitors, topics via Trigify) to scale the "always-on" campaign.
  - **Copy Strategy:** Keep copy general to accommodate multiple lead sources (e.g., personal vs. competitor posts) and enable scale.

### Website De-anonymization Strategy

  - **Recommendation:** Use a separate, email-only campaign for de-anonymized website visitors.
  - **Rationale:** Avoids risking LinkedIn account limits (200-250 connection requests/month).
  - **Workflow:**
    1.  SIFT sends identified *companies* (higher coverage) to Clay.
    2.  SIFT finds 3 top-persona contacts at that company.
    3.  Clay sends a general email offer to those contacts.
  - **Multi-threading:** The workflow can target multiple personas (e.g., Growth, Marketing, Founder) at the same company.

### SIFT Pricing & Services

  - **Credit Model:** 1 credit per person per month.
      - **Rationale:** Ensures cost predictability, as a contact is charged only once monthly regardless of activity volume or webhook destinations.
  - **Services:** Imran offered GTM engineering services (enrichment, Clay, HubSpot plumbing) as a more affordable alternative to agencies.
  - **Referral:** Imran referred Jason to Kamil at 42 Agency for broader HubSpot strategy (tracking, attribution), as it's outside SIFT's core focus.

---

## Action Items

**Imran Patel (SIFT)**
- Transfer LinkedIn engagement Clay table to Jason's workspace; ping on completion
- (Optional) Sketch out email workflow within the table if Jason needs support

**Jason Gong (GrowthX)**
- Draft email outreach copy for Clay table; share with Imran for feedback
- Upgrade SIFT plan with credit card (trial expires in 3 days; 20% discount available for annual contract)
- Add HubSpot filter step to Clay workflow to prevent messaging existing contacts
- Update Notion: define de-anonymization campaign scope (email vs LinkedIn, company vs people targeting, personas)
- Integrate Instantly email campaign once Clay table is ready

---

## Transcript

**Imran Patel:** I took a swing at the LinkedIn campaign first because that seemed like the more immediate thing we could activate right away. So you can see these are all the people who engage with you on LinkedIn—all the webhooks SIFT sent. They're all enriched, and then this is the persona match. Paula is head of CS and matches the seniority persona. Anybody doing anything marketing-related—founders, growth people—we put them in their buckets. Then based on the posts they engage with, we categorize into different intent buckets. Based on that, it generates a LinkedIn DM with the right offer.

**Imran Patel:** It will generate a DM based on that context. So for example, this is AU SEO: "Hey Paula, I do [relevant context]. I think you might find this useful." And then it gives her that offer.

**Jason Gong:** So we have a qualifying step, then a categorization step for intent. And then based on that, you're creating the DM. But we could also route to a different Instantly campaign or HeyReach campaign based on intent?

**Imran Patel:** Exactly. If you have different HeyReach campaigns depending on intent, it can route to different places. I just did this as a quick POC, but it's definitely possible.

**Imran Patel:** You have smartly done HeyReach, right?

**Imran Patel:** This You're welcome.

**Imran Patel:** do

**Jason Gong:** Yeah, so, yeah, I don't know why this is so laggy.

**Imran Patel:** on, why is my computer so laggy?

**Imran Patel:** It's probably me.

**Imran Patel:** Let me see if I stop sharing.

**Imran Patel:** helps.

**Imran Patel:** I think it's us.

**Imran Patel:** It's like wherever I am, they just restarted the network here, so.

**Imran Patel:** In the afternoon, could be me.

**Imran Patel:** All right.

**Imran Patel:** Yeah, so that's kind of the POC.

**Imran Patel:** I just sketched it out.

**Imran Patel:** I also kind of, you know, I know that you were looking, we talked about GTM engineering.

**Imran Patel:** So we do do like, you know, for some people, we do do services on the side.

**Imran Patel:** It's not our main thing.

**Imran Patel:** So if you want to kind of do a services engagement with us, but it's sort of like, I don't want to promise everything under the sun.

**Imran Patel:** It would be very much like enrichment.

**Imran Patel:** Enrichment.

**Imran Patel:** Enrichment.

**Imran Patel:** Some of this, like, you know, clay stuff, some, some HubSpot automation.

**Imran Patel:** So we can kind of engage with you on the services side if you want, if you want, like, and it's fairly reasonable, like, it's not even like, you know, it's much less than what an agency ends up charging you.

**Imran Patel:** So we can kind of, and then if you want to, like you mentioned Trigify and keyword monitoring, so we'd be able to kind of set that up, although like syftdata doesn't do it, obviously right now, but we'd kind of, you know, help you set that up as well.

**Imran Patel:** So it's up to you, like, you know, I'm happy to kind of pull together a proposal if you're interested, but this one we can, the LinkedIn one, happy to kind of put that in motion for you.

**Imran Patel:** If you look, if it looks good, I can share the table with you as well.

**Imran Patel:** Yeah, if you share the table, that'd be great.

**Jason Gong:** I think we could even, yeah, I mean, like, I think I can try to take it from here, like some of the things that are missing, it's like, I'm sure it's a way to like pull in.

**Jason Gong:** And HubSpot to make sure I don't message the wrong person, you know, and filter based on that a little bit.

**Jason Gong:** But otherwise, yeah, I guess that's it.

**Jason Gong:** And then, like, so how you're filling it is, like, so these are people that are engaging with me.

**Jason Gong:** I guess in SIFT, you can set, like, also engaging with other people.

**Imran Patel:** Correct.

**Jason Gong:** Let's see, and you can also set, like, arbitrary posts.

**Jason Gong:** Like, I guess I would have to do that in LinkedIn.

**Jason Gong:** I would, like, click posts on certain topics if I want to monitor that.

**Jason Gong:** Because I'm assuming Trickify, I don't know, I'm actually interested in trying it.

**Jason Gong:** But, like, I assume it doesn't return the post for me to, like, base my message on the post.

**Jason Gong:** But if it does, that would be really helpful.

**Jason Gong:** Like, it's like if I want to monitor SEO and it returns the post that triggered the intent, like, that would.

**Jason Gong:** Yeah, I think.

**Imran Patel:** think, so Trigify, the way Trigify works is that it can give you keyword monitoring, and then I think it should be able to trigger like webhooks on those.

**Imran Patel:** I think it would be a different table though, like, you know, the way you would set it up.

**Imran Patel:** I think that a lot of this is like when we work with other customers, ends up becoming context management, right?

**Imran Patel:** Because the quality of what you end up sending depends on what you feed the system.

**Imran Patel:** And then you have like all these, you know, D and C lists, like, okay, well, if they're in HubSpot, then like, you know, don't talk to them, all of that stuff.

**Imran Patel:** So you kind of feel like to kind of set that all up if you want to kind of take it forward.

**Imran Patel:** I just wanted to kind of show you like what's the sort of, just wanted to sketch it out for you.

**Imran Patel:** So if you want to kind of DIY, then I think it's a good base from which you can kind of go forward and do that.

**Imran Patel:** But if you want to kind of just like, you know, if you want us to do.

**Jason Gong:** Yeah, I mean, I think we're probably good on that because we're just about to get a, like, because we need more help on HubSpot in general, which I know you guys don't want to, don't want to do.

**Imran Patel:** I mean, it depends on what the HubSpot help is, right?

**Imran Patel:** So, like, if it's, like, you know, if it's, like, what is the HubSpot?

**Imran Patel:** Is it, like, more like plumbing?

**Imran Patel:** It's going to go beyond, like, just enabling this.

**Jason Gong:** It's going to be, like, set up the whole, like, top of funnel, like, tracking and attribution and, like, you know, make sure we do an event that's, like, piped into HubSpot.

**Jason Gong:** So, like, yeah, we're trying to find somebody to do, like, all of that.

**Jason Gong:** So, I think, like, that person.

**Imran Patel:** Yeah, I mean, let me, let me, let me, I think that's fair.

**Imran Patel:** I think what I can do is I can, let me put you in touch with Kamil.

**Imran Patel:** He runs 42 Agency.

**Imran Patel:** He's pretty, pretty good at HubSpot.

**Imran Patel:** If you want somebody, like, very dedicated with top of the funnel, like, tracking and all that stuff, his agency is very good at that stuff.

**Imran Patel:** So, I'll kind of put you in touch with him.

**Imran Patel:** And.

**Imran Patel:** See if that, I think you wanted a referral, so I think he's one, and I have one more in mind, and I can kind of put you in touch with them.

**Imran Patel:** But first talk to Kamil, he's pretty solid.

**Imran Patel:** He works with a lot of B2B SaaS companies, and like in general, like.

**Jason Gong:** Okay, I mean, I think we're about to like sign this other person, so it's probably not wrong.

**Jason Gong:** are, okay, then that's fine.

**Imran Patel:** Okay.

**Imran Patel:** And then if you want any help on the, more on the GTM engineering tactical side, then like, you know, we are there as well.

**Imran Patel:** I think what we can do is, what I'll do is, I'll get this table in a good enough shape so that, because it will keep on firing from sift.

**Imran Patel:** I think what I can do is, if you give me access to your clay, then I can just transfer this over to you, and I'll make some like improvements as well.

**Imran Patel:** Yeah, let's just do that right now.

**Imran Patel:** And then I can, I guess, I didn't do email because I wasn't sure what was the, like, how many did you want to send?

**Imran Patel:** And out in the notion.

**Jason Gong:** Yeah, I mean, I feel like there's other steps here that we'll add, and I can just take it from here, but I think email, I feel like I just want to monitor more and more, because if this works, then it's just feeding more signals to it, or some form of this table.

**Jason Gong:** So it's like, instead of just monitoring me, monitor our whole team, monitor like our competitors, monitor just like arbitrary topics, maybe you can even throw in like visitors to our website, I mean, that might just go always to like one campaign, you know, but like, this feels like a nice, like always on thing.

**Imran Patel:** Yeah, think, I think, I think what I would do is I would, I would, like the, I think the challenge is that like, if you take the LinkedIn, like going from LinkedIn to email generally is.

**Imran Patel:** Difficult, right, because the medium changes and it's just kind of, there's just a lot of, then deliverability comes into play and so on.

**Imran Patel:** So I'd have to kind of, I wasn't, how good is your Smartly setup?

**Jason Gong:** I think it's instantly and the industry guys manage it and we have like a million mailboxes.

**Jason Gong:** So I think it's pretty good.

**Imran Patel:** It's pretty good.

**Imran Patel:** Okay, so I think what we can do then in that world is that, yeah, so I think if you have a, if you have a Instantly campaign, I can just set it up so that we can hook it up to that Instantly campaign.

**Imran Patel:** So definitely doable.

**Imran Patel:** So how about this?

**Imran Patel:** Yeah, so did you invite me to your thing?

**Jason Gong:** Yep, I invited you to Clay.

**Jason Gong:** I mean, the Instantly campaigns aren't set up yet, but I think honestly, like what you built here is good.

**Jason Gong:** I can do one pass at it.

**Jason Gong:** think the, the part.

**Jason Gong:** So honestly, I would love more help on is just like the filling list part because I feel like I still don't fully know how to fully use SIFT.

**Jason Gong:** So like I can monitor profiles, I can monitor, I can't monitor individual posts on certain topics, but I can do that in the UI.

**Jason Gong:** So I might just like get somebody to like once a week, like just check for all the things that went viral the week before or whatever and just like click all the SIFT buttons in it even.

**Jason Gong:** But you mean like not by you, but somebody else?

**Jason Gong:** Yeah, like not by me, but by like, you know, like people who post them.

**Imran Patel:** can, like with SIFT, what you can do is we do allow, so if you like, for example, it all, we allow you to track profiles.

**Imran Patel:** So if you, if you want to track, like, let's say, what are those guys?

**Imran Patel:** Profound or something.

**Jason Gong:** Yeah, you want to track the profound people.

**Imran Patel:** Then what you can do is you can like go and let me go into your account.

**Jason Gong:** I think what would be helpful actually is the feature is like, so like the credits in your system are based on enrichment, but like my ability to like filter what I want to enrich is like not there.

**Jason Gong:** And then it's also not like I would have to do it in clay, I guess, where it's like, even if you monitor my posts, like sometimes I'll just, you know, hey, just hired this person and it's like that's like an irrelevant post and I would have loved to filter that like as far ahead as possible, I guess.

**Jason Gong:** But I guess I could filter it in clay.

**Imran Patel:** I see, I see, I see.

**Jason Gong:** Yeah, that would be a cool feature because then I could just monitor profiles, but then just filter their posts somewhere near the beginning so I don't consume all my enrichment credits.

**Jason Gong:** In 7.

**Jason Gong:** API calls.

**Jason Gong:** Yeah, or I mean, I could do it in clay as well, but I know your system kind of like auto enriches people.

**Jason Gong:** Yeah, like.

**Imran Patel:** I mean, so in this case, what happened was that the SIF system auto-enriched most people that were sent to you, that were sent in clay, which you will kind of see that, I actually hit those columns here, which I'll unhide, but like we got like about 85, 90% of enrichments, and then the rest I just filled in with like another waterfall in clay, but there is 100% enrichment at this point.

**Imran Patel:** And so, why is clay's UX, so, okay, yeah.

**Imran Patel:** And then, so the SIF already enriched 90% of those people, so you don't have to use clay enrichments for those.

**Imran Patel:** The post-craping stuff, I had you to use credits for it.

**Imran Patel:** The intent categorization happened in clay as well.

**Imran Patel:** The persona stuff happened in clay, but you can do it in SIFT as well if you give us, true.

**Imran Patel:** You have line, So, people think...

**Imran Patel:** hope really think am,

**Imran Patel:** I know your persona at this point, so I can just kind of put that, we can define it in SIFT right now.

**Imran Patel:** So there are a bunch of things that you just don't need to worry about in terms of enriching, but I think, yeah, I think the main thing would be, the main thing is usually just context engineering, right?

**Imran Patel:** Like in, in terms of like, this is, this is one action, essentially.

**Imran Patel:** And, and then if you want to kind of use everything that goes, oh, sorry, I was like, I was just presenting the wrong tab all this time, but I was like, I was showing you the clay table all this time.

**Imran Patel:** But like, yeah, I was, what I was showing you is like this, this, like, you know, like what, what came from SIFT, so full name, person, title, person, company came from SIFT, this director plus marketing thing, I just did it in clay, although you could do it in SIFT, post URL came from SIFT, intent categorization happened in

**Imran Patel:** Clay, action came from Sift, post description, I scraped it in Clay, LinkedIn DM, I generated off.

**Jason Gong:** it's interesting because like you have the post that looks like in your LinkedIn activity as well.

**Imran Patel:** Yeah, it's actually, we are going to make the change like where we can put it in the webhook itself.

**Imran Patel:** So we have the content on our site.

**Imran Patel:** It's just that not everybody wants that stuff.

**Imran Patel:** So we kind of don't usually send it.

**Imran Patel:** But we can send it out.

**Imran Patel:** And so what, in a way, there is a lot of information available to you.

**Imran Patel:** I think what we need to do is, yeah, and then get the Trigify coverage.

**Imran Patel:** Here, I think you have a few more.

**Imran Patel:** How many connected users do you have?

**Imran Patel:** Like, so you have you, is this?

**Imran Patel:** We have two.

**Imran Patel:** One of them might have.

**Imran Patel:** And Tyler is in that.

**Imran Patel:** Yeah.

**Imran Patel:** Yeah.

**Imran Patel:** And others is in that.

**Imran Patel:** Yeah, so you get two per profile, so you can add just a few more if you want to auto track, but then you can just like, you can do the manual tracking from the button thing, and that should take care of some of that, and then we can do the Trigify thing if you are interested.

**Imran Patel:** I can show you how to hook that up as well.

**Imran Patel:** It should be pretty straightforward, I think.

**Imran Patel:** It's like a bunch of people use Trigify in this fashion.

**Imran Patel:** But the idea would be that, I think the difference is that if you scrape it from, if you reach out to someone that engages with Marcel's post, it's a very different game than reaching out to someone that engages with Profound's post.

**Jason Gong:** I mean, that, I agree with that.

**Jason Gong:** feel like there is a way in the copy, like I think in the copy, I will just...

**Jason Gong:** Just, like, make it general enough that it's not like a, like, hey, you like my post on this, let me help you.

**Jason Gong:** It's like, I think I'm just going to keep it more general just to get the scale from it.

**Jason Gong:** Yeah, yeah, makes sense.

**Imran Patel:** All right.

**Imran Patel:** So, yeah, I think the copy generation is, like, the copy generation is, like, usually the last part of this thing.

**Imran Patel:** As far as you've to just corral everything together.

**Imran Patel:** and I'm happy.

**Imran Patel:** I mean, like, honestly, like, building this is awesome.

**Jason Gong:** Like, if you just throw it over to me and I'll try to.

**Imran Patel:** Did you send the clay thing to me?

**Imran Patel:** Yep.

**Imran Patel:** Sent it to your SIFData email.

**Jason Gong:** Come on, I haven't gotten it.

**Imran Patel:** Hang on.

**Imran Patel:** Imran at siftdata.com.

**Imran Patel:** No, no, no.

**Imran Patel:** I just got it.

**Imran Patel:** Okay, let's do it.

**Imran Patel:** Okay, cool.

**Imran Patel:** Join it.

**Imran Patel:** All right, perfect.

**Imran Patel:** So I'll port the table over.

**Imran Patel:** You will add, I guess, the email stuff.

**Imran Patel:** I can, I can, I can sketch out the email as

**Imran Patel:** It's not a big deal.

**Imran Patel:** And then I will, have you used, you have used Klee before, right?

**Jason Gong:** Yeah, a little bit.

**Jason Gong:** A little bit, okay.

**Jason Gong:** I mean, I'm fully, yeah, I can set up the rest of it.

**Jason Gong:** I've been meaning to spend more time here too.

**Jason Gong:** Okay, so I'll do that.

**Imran Patel:** And then whenever you kind of think you need help, just let, me and happy to help with that.

**Imran Patel:** And in terms of, yeah, I think your SIFT trial is up.

**Imran Patel:** That's it.

**Imran Patel:** just make sure that you don't lose access this time.

**Jason Gong:** Yeah, I mean, feel free to just turn it on.

**Jason Gong:** I'm sure this will work.

**Jason Gong:** Yeah, it's on.

**Imran Patel:** You have three days remaining just FI.

**Imran Patel:** Okay, cool.

**Jason Gong:** I'll put in my credit card.

**Jason Gong:** Is my credit card in there or no?

**Imran Patel:** No, it's not.

**Imran Patel:** No, you don't.

**Imran Patel:** Yeah, here's the, here's the, the, the page.

**Imran Patel:** So just, just upgrade with the, there's an upgrade.

**Imran Patel:** Credit plan button, so if you click on.

**Jason Gong:** Credits is based on like per person, or how does that work?

**Imran Patel:** Credits work on per person per month.

**Imran Patel:** So if you have some person that you send to Webhook for that month, then we will charge you credit for that.

**Imran Patel:** So you have to kind of figure out how you want to set up the Webhook.

**Imran Patel:** If you want to set up the Webhook that it only fires once per person, then I think it should be fairly straightforward.

**Imran Patel:** If you have a Webhook that fires on every activity, then a person gets charged only once per month.

**Imran Patel:** So even if they do 50 likes on your post in that month, it doesn't matter.

**Jason Gong:** Got it.

**Jason Gong:** So that's one credit.

**Jason Gong:** And then is there any credits for like the API stuff of like piping into clay?

**Jason Gong:** No, that's one credit.

**Imran Patel:** It doesn't matter how many places you send it.

**Imran Patel:** It's a one.

**Imran Patel:** One.

**Imran Patel:** One.

**Imran Patel:** One.

**Imran Patel:** One credit per person per month.

**Imran Patel:** Okay.

**Imran Patel:** Got it.

**Jason Gong:** And then is there, like the website de-anonymization stuff, I guess, do you think that should be a different table or we should also put that in this table?

**Jason Gong:** Yeah.

**Imran Patel:** I I think it might be a good idea for you to sketch out on the Notion doc that we have, like what you want there in terms of like, like what is the, like, I think if you do website de-anonymization, my suggestion generally is that that works well with email rather than anything else.

**Imran Patel:** I wouldn't, because LinkedIn has like, you have gaps, right?

**Imran Patel:** Like you can't send more than 200, 250 connection requests.

**Imran Patel:** And so blowing them up on like de-anonymized data is like a little bit risky in my opinion.

**Imran Patel:** Right.

**Imran Patel:** And so I would just, if you were to do a campaign from the website de-anonym, then I would do a separate table and I would only.

**Imran Patel:** Do email in that world, and I can, I can help you set that up as well, where you can, what SIFT can do is you can send either companies or people from website de-anonymization to Clay.

**Imran Patel:** If you send companies, you will have way more coverage because there is more companies get identified than people do.

**Imran Patel:** And then in SIFT, you can say, if there is a company, then you can say, find me the three top people at that company that match my persona.

**Imran Patel:** And then we can just give you those leads.

**Imran Patel:** So, so that's how a lot of people will do it.

**Imran Patel:** It's like, it doesn't matter who was on the website from that company, but like you just, if it's high intent, then just send it to somebody, keep it relatively vague, right?

**Imran Patel:** Like just kind of say like, hey, if you're interested, send them some offer or something and see how far you get with that.

**Imran Patel:** So that's kind of, that's, that's how you get high coverage in this way.

**Imran Patel:** And you can also multi-thread, you can send it to like growth person in a marketing.

**Imran Patel:** Person and the founder and see what happens.

**Imran Patel:** So we can kind of help you set that up as well.

**Imran Patel:** It's one motion.

**Jason Gong:** Sounds good.

**Jason Gong:** Yeah, if you throw the table in there, like when we do a pass edit, I feel like it's almost like I wanna just start using it without, it doesn't have to be perfect.

**Jason Gong:** Yeah, yeah, let's say, yeah.

**Imran Patel:** Yeah, let the perfect not be the enemy of good in GTM generally.

**Imran Patel:** So, which I remind myself, and I'm very picky about what I get, what I send out as well.

**Imran Patel:** So, all right, cool.

**Imran Patel:** So, yeah, I got your play and I'll send it, I'll ping you once it's set up.

**Imran Patel:** And then let me know if you, when you, when you do the, it should be fairly straight or forward to do the payment on the, on the thing.

**Imran Patel:** We'll give you like a big 20% discount if you do an annual contract, but if you wanna do a monthly, then just a monthly.

**Imran Patel:** Okay, sounds good.

**Jason Gong:** All right.

**Jason Gong:** Thanks Amaranh.

**Jason Gong:** All right.

**Imran Patel:** All right, man.

**Jason Gong:** I'll talk to you later.

**Jason Gong:** Bye.

**Jason Gong:** Bye.
