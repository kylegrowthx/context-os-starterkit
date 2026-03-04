# Handover Meeting with Kyle

<metadata>
date: 2026-01-09
time: 02:02 UTC
duration: 106 minutes
organizer: jesus@growthx.ai
participants: Kyle Doherty (external), Jason Gong, Gloria Willis, Jesus Yepez
fathom_recording_id: 112959747
fathom_url: https://fathom.video/calls/524388582
share_url: https://fathom.video/share/h1hYZzxZfqjxKsNNB7VR-CMM5AWmkW4k
source: fathom
enriched_on: 2026-02-28T18:45:00Z
purpose: Handover of new automated enrichment and event attribution systems from Kyle (departing) to GrowthX team
</metadata>

---

## Summary

Kyle Doherty handed over a new always-on enrichment workflow (via Clay) that automatically populates HubSpot with company and contact data, plus a new event-to-AIG-membership attribution system. The team reviewed the Clay enrichment pipeline (progressive company filtering, revenue waterfalls, AI-driven industry classification, contact location/GTM/seniority tagging), the canonical HubSpot segmentation framework for building target lists, and critical next steps including historical Luma event upload, Circle→HubSpot sync, and AIG member attribution workflow implementation.

---

## Context

Kyle Doherty was transitioning out of his role at GrowthX and conducted this handover meeting to document and explain the systems he had built. The meeting occurred just after the 2026 New Year and focused on transferring operational knowledge of the enrichment and attribution pipelines that had been built to support GrowthX's B2B content marketing and AIG membership growth strategies. Jesus Yepez organized and recorded the meeting. The team discussed both the technical implementation details and the operational workflows required to maintain and extend these systems going forward.

Gloria Willis and Jesus Yepez are responsible for executing these systems at GrowthX, while Ed (external developer, not present) will implement critical workflows. Jason Gong attended but played a limited speaking role. The systems discussed—Clay enrichment, HubSpot segmentation, and event attribution—are core to GrowthX's ability to identify, segment, and target high-value B2B prospects.

---

## Relevance

- **Core Operational Systems:** These enrichment and attribution workflows are critical infrastructure for GrowthX's B2B marketing engine, enabling precise targeting and ROI measurement.
- **Team Knowledge Transfer:** Documents how to operate Clay, HubSpot segmentation, and the event attribution pipeline now that Kyle has departed.
- **AIG Membership Growth:** Provides the attribution framework for measuring event impact on AIG (AI-led Growth) membership conversions, a key product metric.
- **Prospect Segmentation:** Establishes canonical segments and enrichment data (seniority, GTM role, geography, company revenue/funding) for sophisticated list building.
- **Email Marketing Execution:** Clarifies HubSpot email sending protocols (domain warming, batch scheduling) and UTM tracking workflows via PostHog.
- **Integration Dependencies:** Maps out required upstream integrations (Circle→HubSpot sync, Beehive→HubSpot sync, historical Luma data import) needed for complete operation.
- **Process Documentation:** Clay workflow, HubSpot segmentation framework, and AIG attribution logic need to be formalized in runbooks for ongoing execution and troubleshooting.

---

## Overview

- **New Enrichment System:** A new, always-on Clay enrichment workflow now populates HubSpot with company data (revenue, funding, industry) and contact data (location, GTM role, seniority tier), enabling precise segmentation.
- **Event Attribution:** A new workflow tracks event influence on AI-led Growth (AIG) membership. It credits an event if a contact becomes an AIG member within 30 days of attending.
- **HubSpot Segmentation:** A new framework uses canonical segments (e.g., `Contact | Seniority Tier | Executive`) as building blocks to create complex, dynamic target lists.
- **Email Marketing:** HubSpot marketing emails are now active. For cold lists, warm the domain by sending in batches (e.g., 100 → 200 → 300) to protect sender reputation.

---

## Key Topics

### Always-On Enrichment Workflow (Clay)

  - The new workflow uses progressive enrichment to save credits by filtering out unqualified companies early.
  - **Company Enrichment (`company-based enrichment`):**
    1.  **Foundational Data:** Pulls all companies from HubSpot.
    2.  **Domain Validation:** Checks domain validity (e.g., not a parked page).
    3.  **Initial Enrichment:** Fills in missing company data (LinkedIn, website).
    4.  **Qualification:** Filters companies based on a simplified fit score (Revenue \> $1M OR Funding \> $2M) to capture high-potential startups.
    5.  **Deep Enrichment:**
          - **Revenue:** Uses a waterfall (HG Insights → Clearbit → SmartE) to get a revenue *range*. This avoids a Clay quirk where requesting an *exact* estimate runs all providers and burns credits.
          - **Industry:** An AI agent classifies companies into standardized sectors using a reference guide.
  - **Contact Enrichment (`base enrichment for people`):**
      - Pulls contacts from "good fit" companies (\~18k contacts).
      - **Data Points Pushed to HubSpot:**
          - `Location` (e.g., "San Francisco Bay Area")
          - `Is GTM Role` (True/False)
          - `Employment Seniority Tier` (Leader, Executive, Manager/IC)
      - **Credit Management:** The workflow is paused at 1k contacts to conserve credits before the monthly reset. The plan is to enrich the full list incrementally.

### HubSpot Segmentation Framework

  - The framework uses canonical segments as building blocks to create complex, dynamic lists.
  - **Process:**
    1.  **Create Canonical Segments:** Build base lists for key dimensions (e.g., `Contact | Seniority Tier | Executive`).
    2.  **Compose New Segments:** Combine canonical segments using `AND` logic to create precise target lists (e.g., `Executive AND Bay Area`).
  - **Benefit:** This method is more efficient and less error-prone than building complex filters from scratch.

### Event & Membership Attribution

  - **Goal:** Track event influence on AI-led Growth (AIG) membership.
  - **Logic:** Credit an event if a contact becomes an AIG member within 30 days of attending.
  - **Implementation:** A new workflow will compare the AIG membership date against event attendance dates.
  - **Reference:** The existing deal attribution workflow in the `EventHapply` folder serves as a template.

### Email Marketing & Tracking

  - **Sending from HubSpot:** The domain is warmed by lead magnet sends, but for cold lists, use a batch schedule (e.g., 100 → 200 → 300) to protect sender reputation.
  - **UTM Tracking:** HubSpot's campaign tracking tool is for *generating* UTM links, not for analytics.
      - **Action:** Add a `utm_content` tag to each link to identify the specific resource.
      - **Analysis:** View UTM data in PostHog, the recommended analytics tool.

---

## Action Items

**Kyle Doherty** (external)
- Send industry classification reference PDF to Jesus via Slack
- Send both call recordings to Jesus
- Create Loom tutorial on uploading historical event data to HubSpot

**Gloria Willis** (GrowthX)
- Share recording with Ed; confirm Circle→HubSpot sync; request AIG member date property + 30-day attribution workflow
- Create canonical HubSpot segments for Employment Seniority Tier (Leader, Executive, Manager-IC)
- Plan email campaign sends for cold lists using batch-warming schedule (100→200→300)
- Request Ed to build AIG membership attribution workflow

**Jesus Yepez** (GrowthX)
- Add utm_content tag to Bolt campaign tracking links; monitor UTM data in PostHog
- Rename Luma registrants segment to "Contact | Registered for Luma event"
- Confirm Beehive→HubSpot sync use case with Ed; implement if needed
- Incrementally enrich remaining ~17k contacts in Clay after monthly credit reset

---

## Transcript
**Gloria Willis:** This meeting is being recorded.

**Gloria Willis:** And trying to get as organized as possible.

**Kyle Doherty:** Yeah.

**Jesus Yepez:** Hey, Jesus.

**Jesus Yepez:** Kyle.

**Jesus Yepez:** Happy New Year.

**Kyle Doherty:** Yeah, you too.

**Kyle Doherty:** Gloria, you able to, I haven't been able to look at Slack.

**Kyle Doherty:** Were you able to check with Ed about integrating Circle with HubSpot?

**Gloria Willis:** No.

**Gloria Willis:** No, I didn't.

**Gloria Willis:** I didn't even register that.

**Gloria Willis:** I responded to you, but I didn't even register the ask there.

**Gloria Willis:** So, no, I did not.

**Gloria Willis:** So that would be the only way to get, to start enriching.

**Kyle Doherty:** To enrich those people.

**Kyle Doherty:** No.

**Kyle Doherty:** Or you could give me, if you have a CSV, we could do it that way.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Like if you're, actually, yeah, if all you're asking for is enriching them, but I guess then are you putting them in HubSpot and then like sending marketing emails to them?

**Gloria Willis:** Possibly, yeah.

**Gloria Willis:** Yeah.

**Gloria Willis:** So there should be some kind of tag on them.

**Kyle Doherty:** Yeah, that would be.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** That's totally a valid way to do it, so I bet Jesus could help you with this, but basically, like, you download a CSV of all the users that you want to enrich, you'd have their email, and they, in theory, should already exist in HubSpot, because I think we're pushing them to HubSpot, potentially, like, from HubSpot to, I'm not sure.

**Kyle Doherty:** Like, I don't know what Ed has done, to be honest, but my point is, like, if they're in HubSpot, like, the email would match to the user, or the contact, and so what you could do is you could enrich them first in Clay, and then you could push that data to HubSpot.

**Gloria Willis:** Okay, I think it's the enriching in Clay is where it goes all cloudy for me, because I'm not good at it.

**Jesus Yepez:** I can help there.

**Kyle Doherty:** Yeah, Jesus can help there.

**Gloria Willis:** Wonderful.

**Gloria Willis:** I'm glad you know how to use it, because I down here threw my computer out the window trying to, trying to.

**Kyle Doherty:** Enrich a very small list once.

**Kyle Doherty:** Yeah, it's not like the most intuitive tool for a lot of people for sure.

**Kyle Doherty:** No, no, it was not.

**Kyle Doherty:** That's actually what I'm going to go over today.

**Kyle Doherty:** I know I said a handoff doc, but like it's just been hard to like get everything done with the job.

**Kyle Doherty:** So, but I still want to go over stuff and it's relevant to you, Gloria, because it is stuff that we did before for you that were one-offs, but then now it'll be like always on.

**Kyle Doherty:** So I think it'll still be valuable for you.

**Kyle Doherty:** And I think it'll also be valuable if you're both going to work on that enrichment together, because like you'll both, you'll see what it takes.

**Kyle Doherty:** So I think that'll be helpful.

**Kyle Doherty:** Should we wait for Jason or should I just kind of get started?

**Kyle Doherty:** Okay.

**Kyle Doherty:** So, Gloria, the only other thing for you, there's two things that I'm missing just before we jump into like the details that I need to get for you and then put in that whole handoff doc.

**Kyle Doherty:** As I

**Kyle Doherty:** I in my first loom to you that gives now companies are associated with the event.

**Kyle Doherty:** When a deal is created, it associates correctly for that 30-day window.

**Kyle Doherty:** And then if a deal is closed one, it associates for that 30-day window.

**Kyle Doherty:** If you recall in that loom, I did show how you can upload, like you download the CSV and then upload to HubSpot until Ed updates the current ZAP to like handle that automatically.

**Kyle Doherty:** But what I was going to do is I was going to create a dedicated one just for that.

**Gloria Willis:** Okay.

**Kyle Doherty:** That would walk you through, okay, this is because there's, you have the virtual events, right?

**Kyle Doherty:** Where all you care about for the upload part is registrants because then Zoom is going to push the participants.

**Kyle Doherty:** Yes.

**Kyle Doherty:** So I wanted to just show, okay, here's how you do it in that case.

**Kyle Doherty:** It'll be the same.

**Kyle Doherty:** So I just wanted to make it super easy where it's like, all right, I'm doing this.

**Kyle Doherty:** Here's like the part in the loom.

**Kyle Doherty:** I can just go straight to it and just make it dead simple.

**Kyle Doherty:** And then the last part is I wanted to get the historical data in there for you because then that also be helpful because then you can like start making reports and see what it looks like and stuff.

**Gloria Willis:** Okay.

**Gloria Willis:** And then I'll have one question.

**Gloria Willis:** then I know this was your meeting, Jesus.

**Gloria Willis:** So I will shush after this.

**Gloria Willis:** Another element that we're wanting to track, and it would be nice if I could do it through it happily, but I probably wouldn't have to do it manually, is we consider it success if we had someone who went to a workshop or to a breakfast and then turned into a member of AI-led growth.

**Gloria Willis:** So is there a way to connect that in the same way it's connecting companies?

**Gloria Willis:** So it would reference a new tag of...

**Kyle Doherty:** Yeah, so once we get the sync from Circle to HubSpot so that we can say, and like all I mean by that is like we'd have a property on the contact that says like AI-led growth member or something or whatever the acronym is that you guys say, member, true.

**Kyle Doherty:** Or probably the better thing would be like the date they became a member and then you probably have another one that says are they paid or not or like what plan are they on so you'd have two but really for this purpose all you care about is the date they became one and then and then I think you'd already have the contact associated with the event so then we were then we

**Kyle Doherty:** I want to, I think, I'm not, sorry, I'm just thinking about it right now.

**Kyle Doherty:** Because you don't need to go through all the rigmarole of like associating it and all that.

**Kyle Doherty:** You really just want to be able to see, okay, of the people who signed up, which ones are attributed to, or like which ones went to an event within a window.

**Kyle Doherty:** So it'd be like, same thing, 30 day window.

**Kyle Doherty:** Okay, then I think we'd have a, you'd have a third property on the contact for AIG, AI led growth member, like AI led growth member attended event or something like that.

**Kyle Doherty:** Like whatever, whatever you want to call it to denote, hey, they became a member and we're giving credit to an event.

**Gloria Willis:** Like it was like them becoming a member was influenced by an event.

**Kyle Doherty:** Then you'd have a workflow that just checks, hey, they became a member.

**Kyle Doherty:** Did they go to an event within 30 days of that?

**Kyle Doherty:** And then if they did, you'd mark that true.

**Kyle Doherty:** So it'd be like.

**Kyle Doherty:** And I'm, it's late in the day, it's been a full day, so I'm not coming up with a good name for that property to be like, hey, they get, we're giving credit to the event, but it would be, you know, something simple, and then you just mark it true.

**Kyle Doherty:** Okay.

**Gloria Willis:** All right.

**Gloria Willis:** So I could just take this whole section of the recording and give it to Ed and be like, help me.

**Gloria Willis:** Yeah.

**Gloria Willis:** I don't know.

**Kyle Doherty:** Yeah, no, you can.

**Gloria Willis:** Great.

**Kyle Doherty:** Yeah, because you're basically just comparing the dates and he can look in the, the, he can look at the workflow that we did for deal attribution on events, which in, and actually I'll just show you right now where those are, so then he can go back in this recording and like, go find it.

**Kyle Doherty:** Um, so let me, so in.

**Kyle Doherty:** Automation workflows, there is a tab just for EventHapply, if you haven't already added this tab here, you won't see it, so it'll be in here, but you just go click it, and then you'll have it, and then these are all the workflows associated with events.

**Kyle Doherty:** The ones that are for, like, if an event influences a deal is here, and we, like, associate the event with the deal in this one, and that's where it checks the date, so you can just, like, pop into that and look at the, like, how I'm doing it, and then you can just use that same pattern to associate, to give the person joining the community credit, like, the event credit for influencing them.

**Kyle Doherty:** Wait, so, what I wanted to go over today, so, like, the other, so, like, the big things, and I'm looking over here, because I'm looking at my whiteboard with to-dos.

**Kyle Doherty:** So it was like all your stuff, Gloria, which you're like pretty much done except, like I said, cleaning up, creating that Luma for you, and then the cleanup, like getting the old HubSpot or the old Luma event data into HubSpot as events and event happily with the registrants and the attendees.

**Kyle Doherty:** The other big piece was the always on enrichment.

**Kyle Doherty:** I had done like a quick and dirty version, and then there was like this snafu with basically the growthx OpenAI API key and stuff that Understory was doing.

**Kyle Doherty:** It was like, oh man, are they like burning a bunch of credits?

**Kyle Doherty:** So I went in and looked at mine, and I was like, I'm just going to turn this off for now just because I didn't have time to look at it, and I knew we needed to redo it anyways.

**Kyle Doherty:** So anyways, what I'm doing, what I did now is I redid that.

**Kyle Doherty:** So Gloria, I apologize, it's probably going to be maybe a little boring for you, but it might also be like.

**Kyle Doherty:** Good, like educational in a way.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So, Asus, you know, you've seen some of this already, but let me make sure I'm in the right account.

**Kyle Doherty:** Yes.

**Kyle Doherty:** So where is, oh, I'm in one-off, so I don't want be in one-off.

**Kyle Doherty:** So process.

**Kyle Doherty:** And then we went over these two, which are for Tyler.

**Kyle Doherty:** But I'm just calling that out.

**Kyle Doherty:** So these are called template right now.

**Kyle Doherty:** I did that because, A, they're built from templates that I created in my account, but also because I wanted to make it clear that, like, you guys should update these and make them the way, exactly the way you want them.

**Kyle Doherty:** they're meant to be updated.

**Kyle Doherty:** Like, this is just the starting point that I'm getting you.

**Kyle Doherty:** So we have two.

**Kyle Doherty:** have one for company and we have one for people.

**Kyle Doherty:** And so it's titled company-based enrichment, again, because it's like the bare minimum you want.

**Kyle Doherty:** So I'm

**Kyle Doherty:** And so that's why I called it that.

**Kyle Doherty:** So there's three tables.

**Kyle Doherty:** And the reason we have that is because we want to progressively enrich the data.

**Kyle Doherty:** That way we're not burning credits for people that we shouldn't be trying to enrich.

**Kyle Doherty:** So what we do first, foundational data, I think you know this, Jesus, already.

**Kyle Doherty:** But Clay and really any enrichment tool, there's like, well, Clay talks about getting the corner pieces.

**Kyle Doherty:** So like if you think about doing a puzzle, you start with the corner pieces.

**Kyle Doherty:** And then from there, can build a puzzle.

**Kyle Doherty:** And like that's the same idea here.

**Kyle Doherty:** So you need specific data to be able to really enrich well.

**Kyle Doherty:** And if you don't have that data, it's kind of not worth it.

**Kyle Doherty:** So the first thing we do is we come in here and we make sure that we have those corner pieces.

**Kyle Doherty:** So what we're doing is we're pulling in basically all the companies.

**Kyle Doherty:** So we have like 14,000 companies.

**Kyle Doherty:** And then we have a lot of data already.

**Kyle Doherty:** And HubSpot is doing some enrichment already on companies and contacts.

**Kyle Doherty:** So that's another thing.

**Kyle Doherty:** Sometimes we have this data already from HubSpot.

**Kyle Doherty:** So you can see, for instance, we already have industry.

**Kyle Doherty:** We already have LinkedIn for a bunch of them.

**Kyle Doherty:** We have employee size, annual revenue.

**Kyle Doherty:** We're missing it for some, but some we have company description, so on and so forth.

**Kyle Doherty:** And some of these, we have this data because we've done one-off enrichments before.

**Kyle Doherty:** So it's one or the other.

**Kyle Doherty:** Pace2 says, I noted in the other one that we went over, I color code the columns orange for the columns that are coming from HubSpot, just so it's easy to keep track of that.

**Kyle Doherty:** Then what we do, the next thing we do is because domain is one of those corner pieces, if the domain doesn't work, like, don't bother enriching after that, right?

**Kyle Doherty:** So that's one of the first things we do.

**Kyle Doherty:** So this is just a collegiate.

**Kyle Doherty:** So this

**Kyle Doherty:** And we're using 4.0 mini, so it's pretty cheap.

**Kyle Doherty:** It's using our API key, and you can read through it here.

**Kyle Doherty:** But basically, it's just going through and making sure it's not a 4.0.4, so you can access the page.

**Kyle Doherty:** It's not like a parked page, so it's not like one of those GoDaddy pages.

**Kyle Doherty:** It's like a legit business website, because if not, then we shouldn't enrich it, right?

**Kyle Doherty:** So that's what it's doing, and then it's spitting out invalid, if it's not legit.

**Kyle Doherty:** Valid if it is, and then the ones that haven't run is because we have data on them already, like LinkedIn data.

**Kyle Doherty:** So we're assuming it's good, right?

**Kyle Doherty:** And then I think there might be, no, later on, there's some more validation we do, and I'll show you that in a second.

**Kyle Doherty:** So again, this is what I was talking about, where it's progressive.

**Kyle Doherty:** So again, it's to save credits, and just money, which means money.

**Kyle Doherty:** second.

**Kyle Doherty:** So then enrich the company.

**Kyle Doherty:** So we just do basic enrichment using Clay's enrichment.

**Kyle Doherty:** Again, these aren't met, but then some of them, like we didn't have data, so that's sort of filling in that data that we're missing.

**Kyle Doherty:** So we get things like the website, LinkedIn, et cetera, et cetera.

**Kyle Doherty:** So we get that data.

**Kyle Doherty:** Now we have to, because we have the data from two places, we have to merge it.

**Kyle Doherty:** So we check, and this is, you technically don't need to do this because I wasn't running this, if we already had that data right.

**Kyle Doherty:** But I do it anyways, because A, I wanted to show you the pattern, and B, for some of these, what will happen, like I chose not to run this one, if we had the LinkedIn URL.

**Kyle Doherty:** But it could be that we had some of the other.

**Kyle Doherty:** Another data, like company name, company domain from HubSpot.

**Kyle Doherty:** So I'm just merging them, basically saying, if I have it from HubSpot, use that.

**Kyle Doherty:** If I have it from the enrichment we just did, or sorry, if I don't have it from HubSpot, but I have it from the enrichment we just did, use that value.

**Kyle Doherty:** So it just takes, it basically just like puts it, it merges it so that we have the data, whether we have HubSpot or the enrichment.

**Kyle Doherty:** But like I said, you don't really need this because I'm not running the enrichment if we already have the data, but I mostly wanted to share the pattern.

**Kyle Doherty:** Because what will happen is sometimes you're enriching from multiple providers and they won't give you a waterfall when you're enriching for an entire company because it can't waterfall it because it's giving you so much different data.

**Kyle Doherty:** So then you have to do something like this.

**Kyle Doherty:** Yeah, so number of employees, final industry, final description, final.

**Kyle Doherty:** Et cetera, et cetera, right.

**Kyle Doherty:** And then this final thing is this domain validation status.

**Kyle Doherty:** So here's just a formula.

**Kyle Doherty:** And basically what it's doing, so you can see that it's, I won't show us the formula, be easier to look at it.

**Kyle Doherty:** So if it's valid, it's obviously saying, okay, this is valid.

**Kyle Doherty:** If it's blank, it's because we didn't need to validate the domain.

**Kyle Doherty:** So it's valid.

**Kyle Doherty:** So blank or valid is valid.

**Kyle Doherty:** I guess to make it clearer, I could have added that to this formula.

**Kyle Doherty:** that's like an upgrade you could make if you want to.

**Kyle Doherty:** Needs review.

**Kyle Doherty:** So the other check that I put in here.

**Kyle Doherty:** So besides just checking if the previous check we did was invalid, it checks to see if the domain that we got from the enrichment here matches the domain we have in HubSpot.

**Kyle Doherty:** So if they're different, it says, hey, there's a domain.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Mismatch, you should review this.

**Kyle Doherty:** So what I have done is we have another view.

**Kyle Doherty:** So we have all companies.

**Kyle Doherty:** That's what we're looking at right now.

**Kyle Doherty:** have needs review.

**Kyle Doherty:** And then you can come in here and manually review them and be like, okay, we enriched this one.

**Kyle Doherty:** Let me find one.

**Kyle Doherty:** Okay.

**Kyle Doherty:** So domains mismatch.

**Kyle Doherty:** Or if we have no domain, then like that's an issue.

**Kyle Doherty:** And what I mean by that is, let me start with that one because that one's simple.

**Kyle Doherty:** If we did the enrichment, but we couldn't find data on them, we're not going to continue doing like, we're not going to send them to do the qualification and stuff like that.

**Kyle Doherty:** Because like what's going on there.

**Kyle Doherty:** So it's like, hey, you can review that.

**Kyle Doherty:** Maybe it's not a big deal.

**Kyle Doherty:** Maybe it's legit.

**Kyle Doherty:** Maybe it's but probably something's wrong.

**Kyle Doherty:** The other one.

**Kyle Doherty:** Maybe

**Kyle Doherty:** Where did I go?

**Kyle Doherty:** Oh, the other one.

**Kyle Doherty:** Where is it?

**Kyle Doherty:** Okay.

**Kyle Doherty:** The other one is domain mismatch.

**Kyle Doherty:** So a lot of times, as you both know, you'll have like getcompact.io and getcompact.com, and that's why they're mismatched.

**Kyle Doherty:** But it also could be totally wrong.

**Kyle Doherty:** And we have so many companies and leads.

**Kyle Doherty:** I think to me, it's better to just come in and review these.

**Kyle Doherty:** And if they're fine, then just mark them as valid and then let it run.

**Kyle Doherty:** But if there's a mismatch, like go in and check it, see why, and then don't continue if it is actually wrong.

**Kyle Doherty:** So that's why I'm doing that.

**Kyle Doherty:** If you don't agree and you want to just say, you know what, we don't care, that mistake's fine.

**Kyle Doherty:** Like you can just take that out of the function that does that check.

**Kyle Doherty:** Okay, so that's that.

**Kyle Doherty:** Let's go back.

**Kyle Doherty:** So if they're blank or valid, we send them to the next table and then the next table is doing an initial qualification.

**Kyle Doherty:** So that initial qualification is it's getting, we already have annual revenue and funding from some people and employee count, but it's going getting more of that.

**Kyle Doherty:** So it's getting revenue data if it's missing and it's getting funding data if it's missing.

**Kyle Doherty:** This is actually fairly important to call out.

**Kyle Doherty:** So when I get the revenue data, what we're doing is this is a waterfall enrichment.

**Kyle Doherty:** So let me move some of this stuff around.

**Kyle Doherty:** So you have, you click on full configuration and you can see how it's waterfall and it's doing HG Insights, Clearbit, and SmartE and it progressively gets more expensive.

**Kyle Doherty:** There's more you could add if you want to.

**Kyle Doherty:** Generally, it's like most of it's going to be covered by HG Insights, but then yeah, Clearbit and SmartE like Yeah.

**Kyle Doherty:** What I want to call out, though, is we return a revenue range, we don't return the actual estimated revenue.

**Kyle Doherty:** The reason for that is when you have clay, because you can, I'll show you what I mean by this.

**Kyle Doherty:** So if I do.

**Kyle Doherty:** I think this is the, I think this is the one I did, but you can, there's a, there's one that'll, that'll return, or maybe they got rid of it, but there, there used to be one where instead of getting the revenue range, you can have it give you the estimated revenue.

**Kyle Doherty:** The problem is when you do that, what it does is it returns like a bunch of data, it just enriches the whole company.

**Kyle Doherty:** So it tries to give you all the data for the company, and then it, and then if it doesn't.

**Kyle Doherty:** So back estimated revenue, then it moves to the next provider, and then it tries to enrich that one.

**Kyle Doherty:** So what that would look like is it would do HG Insights, it would return JSON with all this data about this company, right?

**Kyle Doherty:** But if estimated revenue wasn't there, then it would go to the next one.

**Kyle Doherty:** So the problem with that is it would charge you for that data it got, and then it would try to run Clearbit and do the same thing.

**Kyle Doherty:** Clearbit didn't get there, then it would run whatever this one's name is called, I forget now, Smart E.

**Kyle Doherty:** And now, like, you basically just lost the whole benefit of waterfall enrichment, and you're paying, like, a ton of, you're just blowing credits and potentially getting no data back.

**Kyle Doherty:** So I actually burnt, like, 10,000 credits one day and got, like, totally  data and had to, like, hit up Clay and be like, hey, what the  just happened?

**Kyle Doherty:** They're like, oh, yeah, sorry, that's a quirk.

**Kyle Doherty:** So I just want you not to do that.

**Kyle Doherty:** At end of the day, like 10 to 1,000 credits sounds like a lot.

**Kyle Doherty:** It's like a few hundred bucks.

**Kyle Doherty:** Like, not good, but it's like, it's not the end of the world, but it'll just save you some headache.

**Kyle Doherty:** But that also means that it's super annoying because, of course, the different data providers don't standardize how they return the company revenue range, right?

**Kyle Doherty:** So it looks different for each of them.

**Kyle Doherty:** So you have to add the right formulas to standardize it.

**Kyle Doherty:** So then we pull out the min and the max, and then we standardize it over here so it's all the same.

**Kyle Doherty:** And it's like a full number instead of like 5 mil, 50 mil.

**Kyle Doherty:** It's like an actual number.

**Kyle Doherty:** And then what I do is I take the max revenue and just say that's the revenue final, and that's what we're saying is like the estimated revenue.

**Kyle Doherty:** Because at the end of the day, all this is just estimated revenue.

**Kyle Doherty:** So we just go with the max.

**Kyle Doherty:** If you wanted to change that and go with the min, you could do that.

**Kyle Doherty:** If you wanted to, I don't know, get the median.

**Kyle Doherty:** You probably could use a formula to get the median between the min and the max.

**Kyle Doherty:** So you can do whatever you want.

**Kyle Doherty:** But that's what I'm doing now.

**Kyle Doherty:** Total funding is nice and straightforward, luckily.

**Kyle Doherty:** So you just get total funding.

**Jesus Yepez:** then...

**Jesus Yepez:** if can just interrupt you for a minute, if you could go back to the last column that you were explaining, the revenue, that one.

**Jesus Yepez:** So you said you use a formula, but use the formula in one of the fields that you wanted to give you?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So first what it does is this is the waterfall enrichment, right?

**Kyle Doherty:** So it gets it from one of these providers.

**Kyle Doherty:** Then it gives you two columns.

**Kyle Doherty:** It gives you which provider to get it from and what it gives you the revenue range.

**Kyle Doherty:** But then here, the revenue range, you can see this one came from HG Insights and it...

**Kyle Doherty:** Gives it to you where it says from 1 million totally spelled out to whatever the max is.

**Kyle Doherty:** But if it's from Clearbit, it's 10 million written this way.

**Kyle Doherty:** And if it's from Smarty, it's almost the same, but it's a little different.

**Kyle Doherty:** There's like a space between these.

**Kyle Doherty:** Which like, that doesn't really matter, but it does when you then have to get the min and the max.

**Kyle Doherty:** Because you're splitting on these things.

**Jesus Yepez:** So, the way that you avoided Clay charging a lot of credits was by using the formula on that column.

**Kyle Doherty:** No.

**Kyle Doherty:** So, the way that I, good question.

**Kyle Doherty:** And the way that I avoided that is when you're doing this enrichment.

**Kyle Doherty:** Let me see if it'll make it clear.

**Kyle Doherty:** So.

**Kyle Doherty:** Maybe here it'll show.

**Kyle Doherty:** So, it doesn't really make it clear.

**Kyle Doherty:** So when you're setting it up, you can say, do you want range or do you want exact?

**Kyle Doherty:** And so it's already set to range, so you don't have to worry about it.

**Kyle Doherty:** But I just wanted to explain this to you because in the future for anything else, you'll be like, oh, this range is really annoying to work with.

**Kyle Doherty:** I don't want to do that.

**Kyle Doherty:** And you'll be like, let me get the exact revenue.

**Kyle Doherty:** But when you do that, the way that they return exact revenue is they return a big blob of JSON with all data.

**Kyle Doherty:** But if it doesn't include estimated revenue, then it goes to the next provider and gets that data.

**Kyle Doherty:** And then if it doesn't include...

**Kyle Doherty:** Estimated revenue goes to the next one, but the problem is it charges you each time because it is actually returning data, whereas when you're asking for one piece of data, which technically you are in this case and why it's confusing and I would consider a bug, it's charging you.

**Kyle Doherty:** Even if at the end of it you didn't get estimated revenue, you still would have gotten charged for all three of those data providers returning data.

**Jesus Yepez:** Perfect.

**Kyle Doherty:** Got it, got it.

**Kyle Doherty:** Yeah, yeah.

**Kyle Doherty:** So, no, good question.

**Kyle Doherty:** Yeah, because if that doesn't make sense, then you, yeah, you potentially would make that mistake in the future, which is what I'm trying to avoid.

**Kyle Doherty:** So, thank you for asking.

**Kyle Doherty:** Total funding, this way you don't have to worry about that.

**Kyle Doherty:** All it does is return the funding, like the total funding.

**Kyle Doherty:** And so, yeah, pretty straightforward.

**Kyle Doherty:** If you want it in the future, you can get a bunch of other data about funding, but it needs to be worth it to you.

**Kyle Doherty:** So things that you could get, for example, is you might want to know what's the most recent funding they got.

**Kyle Doherty:** So what's the most recent round?

**Kyle Doherty:** How much did they get for that round?

**Kyle Doherty:** And when did they get that round?

**Kyle Doherty:** However, because you're getting multiple pieces of data, you then have to basically, you won't be, it'll be much harder.

**Kyle Doherty:** You won't be able to actually waterfall it.

**Kyle Doherty:** So it's just, it'll cost a lot more and it's harder.

**Kyle Doherty:** So if you want to do that, just make sure you have a really good use case for it.

**Kyle Doherty:** Otherwise, like for us, just trying to determine like, hey, would this company be a good fit in terms of someone we're going to sell to?

**Kyle Doherty:** Just go with total funding.

**Kyle Doherty:** So that's what we did.

**Kyle Doherty:** Then I do this check where we say, is it a fit?

**Kyle Doherty:** So we're basically doing a very simplified fit score.

**Kyle Doherty:** And all we're doing is we're saying, do they have a million in revenue or do they have over?

**Kyle Doherty:** Or $2 million in funding.

**Kyle Doherty:** And you can change this to be whatever you want.

**Kyle Doherty:** So if you don't want to enrich as many companies, you could increase this and just not enrich as many.

**Kyle Doherty:** The reason I left it fairly low is because even though a lot of times we, like Tyler, wouldn't prioritize them from a marketing standpoint for like what you're doing, Gloria, you potentially want to market to them.

**Kyle Doherty:** So like it would be bad if like, in my opinion, it would be bad if like a hot new startup from Y Combinator or from like a few years ago that has a series A or like a pretty good seed round, but they didn't fit Tyler's criteria.

**Kyle Doherty:** So we weren't enriching them and therefore you weren't marketing to them for your events.

**Kyle Doherty:** So that's why I did that.

**Kyle Doherty:** So then if they are a fit and you can see like not a fit, then we don't send them to the next table.

**Kyle Doherty:** You can see here, have like 12,253 in this table, and then this table will be less.

**Kyle Doherty:** There's only 8,000.

**Kyle Doherty:** So now we're only enriching 8,357 companies with the other enrichment that we're doing.

**Kyle Doherty:** So in here, we are getting a bunch of stuff.

**Kyle Doherty:** What's it exactly?

**Kyle Doherty:** Oh, this was, I don't know what this is.

**Kyle Doherty:** So just so you guys have context.

**Kyle Doherty:** So what I did here is like Danny actually did a great job of standardizing like what are the sectors we care about.

**Kyle Doherty:** And so that's really good because you saw like the industry column in that table that the data providers give you.

**Kyle Doherty:** It's like total garbage.

**Kyle Doherty:** Like you can't do anything with it.

**Kyle Doherty:** It's like super high level stuff that like big consulting firms.

**Kyle Doherty:** So.

**Kyle Doherty:** Thank

**Kyle Doherty:** And you'd be like, I don't know what that means.

**Kyle Doherty:** So it's not useful.

**Kyle Doherty:** What I did, though, is I then wrote an AI prompt to have an agent classify them as one of these.

**Kyle Doherty:** So actually, this is not like crazy advanced, but it's a bit more advanced features, Jesus.

**Kyle Doherty:** I'll try to walk you through this.

**Kyle Doherty:** I know we're going over, so do you have time?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Okay.

**Kyle Doherty:** So let's see.

**Kyle Doherty:** So let me just, I'm trying to jog my number of what I did here.

**Kyle Doherty:** Oh, I know.

**Kyle Doherty:** Okay.

**Kyle Doherty:** So I said, did I see?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** For like industry category.

**Kyle Doherty:** So I see one.

**Kyle Doherty:** So we have three different agents here that are doing stuff.

**Kyle Doherty:** So this first one is saying it's checking the description we have for the company already.

**Kyle Doherty:** So it's checking if we have a description.

**Kyle Doherty:** If we do, it's saying, hey, is this description good enough for us to determine what industry this is?

**Kyle Doherty:** To make that call on that category.

**Kyle Doherty:** And then it's just returning like, yep, it's good or no.

**Kyle Doherty:** Or actually rather, it's giving a quality score.

**Kyle Doherty:** So if it's good, if it's above seven, then we're saying that's great.

**Kyle Doherty:** We're going to use that description.

**Kyle Doherty:** If it's not, then we're going and we're creating a description.

**Kyle Doherty:** So what this one is doing is it's going to their website.

**Kyle Doherty:** It's going, say the company name, company description.

**Kyle Doherty:** Although, because it could have some description.

**Kyle Doherty:** So we're including it if it, even if we don't, even if we said it's not good enough, but that's why this is toggled off as not required, because we might not have it at all.

**Kyle Doherty:** Then it has the domain and it has the enriched industry.

**Kyle Doherty:** So that industry that I said isn't useful for us.

**Kyle Doherty:** It's still useful for this because it at least puts some guardrails on it, right?

**Kyle Doherty:** Like if it says like, I don't know, like finance, it knows, okay, like it's not e-commerce, right?

**Kyle Doherty:** So it narrows it a bit.

**Kyle Doherty:** And then this just goes to the website and like tries to figure out what industry they're in, or sorry, tries to write a good description that we then can evaluate to figure out what industry they're in.

**Kyle Doherty:** So then it gives us the final company description.

**Kyle Doherty:** And this is one of those merge fields.

**Kyle Doherty:** So it's, you know, if we have one over here, take that one.

**Kyle Doherty:** If we have this one, take that one.

**Kyle Doherty:** And then now we have one column with all of them.

**Kyle Doherty:** And then you have this third one, and this is where it actually does that classification.

**Kyle Doherty:** And this is a little hard because you have to explain, you have to have the prompt for the agent, but then you also need to give it examples of what does each industry classification mean.

**Kyle Doherty:** And that ends up being just like this massive prompt that's like too much for the context window.

**Kyle Doherty:** But what you can do with agents, as long as they're, you can't do this with clay agents, but you can do that with agents that are just creating and modifying content.

**Kyle Doherty:** What you can do is in addition to the prompt, you can also give it a document to reference.

**Jesus Yepez:** So you can give it additional content.

**Kyle Doherty:** What's that?

**Jesus Yepez:** No, I just say it.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay, cool.

**Kyle Doherty:** So in here, we have this document, this PDF, that's industry classification reference guide.

**Kyle Doherty:** I don't think I can download it.

**Kyle Doherty:** I have it on my computer that I'll send it to you in Slack just so you have it.

**Kyle Doherty:** But basically, maybe I have it on my desktop.

**Kyle Doherty:** So what it does, it just breaks down each category and gives it a definition, key signals, examples, and so it can reference that, and then it just follows the prompt that it's given, and then does its thing.

**Kyle Doherty:** So that's what that's doing.

**Kyle Doherty:** And again, this is a 4.0 Mini, so it's pretty cheap.

**Kyle Doherty:** So you can see here, like it's 0.00045 cents to run that one.

**Kyle Doherty:** So not a lot.

**Kyle Doherty:** And then it gives us this industry classification.

**Kyle Doherty:** So now we have industry final, revenue final, total funding final, and now we can update the company.

**Kyle Doherty:** Why you care, Gloria, about all this is because then we, what we can do is we save that data to.

**Kyle Doherty:** To HubSpot, this you probably don't care about, but that's mostly for Danny, but this we use plus number of employees to then create this segment, are they a good fit company or are they not?

**Kyle Doherty:** So this one I'm using, right now, the fit score, the way we're scoring them, is I'm scoring them based off of, like this fit score is for the one that we're using for Tyler, so I'll show an example, so it's actually pretty strict.

**Kyle Doherty:** But what we could do is you could follow the same pattern for like a lower fit, like a less strict fit score.

**Kyle Doherty:** So we go in here, oh, no, I'm setting this with, sorry, let me go back, I'm setting this with the workflow.

**Kyle Doherty:** So what we're doing is if they have funding of 20 million or more or revenue of 10 million or more, then we're saying they're a good fit because originally that's what we're doing for Tyler, if we want to make that less strict, you could come in and change this or you could make another fit score property that's just for, that's more for like marketing instead of sales and make it less strict.

**Kyle Doherty:** But yeah, so you can do whatever you want there, but tie this back right now.

**Kyle Doherty:** Why this matters is that.

**Kyle Doherty:** So even with it being pretty strict, there's 6,200 companies that are a good fit.

**Kyle Doherty:** And then we do a segment of contacts that are associated with those companies, and there's 18,000 of them.

**Kyle Doherty:** So it's still a lot, even being that strict.

**Kyle Doherty:** So that's what's going on there.

**Kyle Doherty:** So then we have these contacts that are at good fit companies, and now we can come into Clay and enrich those people.

**Kyle Doherty:** So let me go to that one now.

**Kyle Doherty:** So now you have the base enrichment for people.

**Kyle Doherty:** So this is pulling in all those people.

**Kyle Doherty:** So we have 18,000.

**Kyle Doherty:** Right now, I have this filter down, so we're only looking at 1,000, Jesus.

**Kyle Doherty:** So I did that because we need to wait until the 13th to get another 50,000 credits because it'll be the next month with 50,000 credits, and now you can do more.

**Kyle Doherty:** So what this does, same pattern as before pulling in the data from HubSpot, then we're doing the enrichment on the people for people where we are missing data, right?

**Kyle Doherty:** And oftentimes if we're already missing data, if HubSpot didn't get us anything back, we're not going to get anything from this next enrichment.

**Kyle Doherty:** But for some people, you can see that we do.

**Kyle Doherty:** Then again, we like combine the data.

**Kyle Doherty:** So we have first name, last name, final.

**Kyle Doherty:** And then we also combine them to have full name.

**Kyle Doherty:** The reason we do that, again, is those corner pieces.

**Kyle Doherty:** Most enrichments, when you're enriching a person, you have full name.

**Kyle Doherty:** HubSpot doesn't have a full name.

**Kyle Doherty:** It's a in the , so you do it here.

**Kyle Doherty:** So now you have that.

**Kyle Doherty:** Also try to fill in LinkedIn data that we're missing.

**Kyle Doherty:** So you can see here, like this person, we didn't have a LinkedIn profile, so we get it for them.

**Kyle Doherty:** And then we have a LinkedIn URL final.

**Kyle Doherty:** Again, we're merging them.

**Kyle Doherty:** Into one column so we can reference that instead of having to write like a really nasty conditional job title, same thing.

**Kyle Doherty:** And then once we get that data, we're sending it to initial enrichment.

**Kyle Doherty:** So this table is, this workbook, it's less about the whole progressive enrichment and more about this first table is just getting the corner pieces and then the next table is the initial enrichment.

**Kyle Doherty:** Um, so this is just getting like the enrichment we need.

**Kyle Doherty:** If you had, um, let's say, let's say we started doing a bunch of ads and we wanted to target people specifically, but we needed extra data about them to figure, uh, to like do the ads.

**Kyle Doherty:** This is not a very good example, but just bear with me.

**Kyle Doherty:** Uh, and you did, and you didn't need that all the time, you would, um, you would probably like check for something in this table, the initial enrichment.

**Kyle Doherty:** Enrichment that tells you you should do that third enrichment just for the ads and then send them to that table and do that enrichment.

**Kyle Doherty:** That way it would cut down this number to only the people you truly want to spend money on that additional enrichment.

**Kyle Doherty:** So hopefully that makes sense.

**Kyle Doherty:** Basically, you don't need to add that third table like we have in the company unless you're doing a bunch of extra enrichment that you only want to do sometimes.

**Kyle Doherty:** So anyways, so here what we're doing is now we're doing the stuff that you need, Gloria and Danny, where we need two things.

**Kyle Doherty:** We want to know, I'll go to the end first just so you can see what we're doing.

**Kyle Doherty:** We want, where is it?

**Kyle Doherty:** We want location.

**Kyle Doherty:** So we try to get location for as many people as we can.

**Kyle Doherty:** And we then save that on like, there's like a location property.

**Kyle Doherty:** Let's find it right now.

**Kyle Doherty:** So it's on in the video.

**Kyle Doherty:** Yeah, so location, and it'll say something like greater Boston, San Francisco Bay Area, San Francisco, California, says all sorts of stuff, but we use that.

**Kyle Doherty:** That's easier to use because then we have in the segments that we built Gloria, we can just check like, if it includes all these cities in the Bay Area in the name, then we throw it in that, and that's what it does.

**Kyle Doherty:** So that's the first thing it's doing is we're getting that.

**Kyle Doherty:** But then the other thing we want is we want, are they GTM, the GTM role?

**Kyle Doherty:** And then we also want, are they senior?

**Kyle Doherty:** Or are they senior?

**Kyle Doherty:** And for Dani specifically, she has this, um,

**Kyle Doherty:** Like, seniority classification that she's doing.

**Kyle Doherty:** So we're saying, are they leader, executive, or manager slash IC?

**Kyle Doherty:** So what I ended up doing is I created an additional property on the HubSpot contact.

**Kyle Doherty:** HubSpot already gives you, just so you guys know that it exists.

**Kyle Doherty:** Sorry.

**Kyle Doherty:** It gives you this, employment, seniority, but it's a bunch of different things, like IC, director, leader, executive, et cetera, et cetera, et cetera.

**Kyle Doherty:** So what we do, what I do then is I take that plus their title, and then I have AI tell me which one of these buckets does it fall into.

**Kyle Doherty:** And then we set that.

**Kyle Doherty:** And, yeah, and then that's what I set.

**Kyle Doherty:** And

**Kyle Doherty:** And HubSpot on a property called Employee Seniority Tier.

**Gloria Willis:** So when I create a segment, I can use, well, that's going to be a video I need you to make.

**Gloria Willis:** When I create these segments, it would be obviously location.

**Gloria Willis:** And then I would probably just go straight to that, like, leader, executive, manager I see.

**Gloria Willis:** I wouldn't even look at the titles at that point.

**Gloria Willis:** I would just be like, maybe.

**Kyle Doherty:** Exactly.

**Kyle Doherty:** And that's why I created the other property, because that way you have, like, this simplified one that groups them for you.

**Kyle Doherty:** So that's just, it's better.

**Kyle Doherty:** Great.

**Kyle Doherty:** So that's what that does.

**Kyle Doherty:** And then one little caveat that you should be aware of, Jesus, is it also, it gives us the seniority confidence.

**Kyle Doherty:** So what that's saying is, like, am I confident in the tier that I just gave you?

**Kyle Doherty:** So, like, here you can be, like, you can see that it's not really confident that it's not leadership.

**Kyle Doherty:** There's no real other good, oh yeah, there's not really any good examples for this one, but basically we say like, hey, if it's not confident, we're just going to return blank.

**Kyle Doherty:** Because it could be saying, hey, this is an executive, but give you a five, and then we don't want to say that's executive, we'll just say, we don't know.

**Kyle Doherty:** Don't put it in the, don't put that one in the segment that we have.

**Kyle Doherty:** And then we do that, the same thing for GTM role.

**Kyle Doherty:** So it's saying, is it, is this person in a GTM role or not?

**Kyle Doherty:** And this is just a classification agent that's just like, it's just taking in job title and employment seniority.

**Kyle Doherty:** And then it's saying like, is this person in GTM or not?

**Kyle Doherty:** And it's checking for a bunch of different keywords.

**Kyle Doherty:** And then it's saying, okay, am I confident in this or not?

**Kyle Doherty:** Generally speaking, it's not returning true if it's not confident, but it could.

**Kyle Doherty:** So I just

**Kyle Doherty:** But check, so for instance, if we change this one to three, it now will go, it'll turn off.

**Kyle Doherty:** So we'll try to put that back to nine.

**Kyle Doherty:** And then that way, like, again, same thing.

**Kyle Doherty:** We're not saying, hey, this person's in a GTM role when, like, really, the agent has no  clue, right?

**Kyle Doherty:** So, so that's that.

**Kyle Doherty:** Yeah, so the kicker for this one, Jesus, is, like I said, I only have this turned on for a thousand.

**Kyle Doherty:** I could do a few more to eke out, to, like, use these credits up, but I don't think it's worth it because these will actually roll over to the next month.

**Kyle Doherty:** So you'll have 64,360.

**Kyle Doherty:** So then what you would do with this, my recommendation on how to do it, is, well, first what we can do.

**Kyle Doherty:** So what we can do is we can see.

**Kyle Doherty:** What's the credit usage for this table?

**Kyle Doherty:** So we can see this table out of 1,000, it costs 600.

**Kyle Doherty:** So we know probably what I would do is I would then run like another 1,000.

**Kyle Doherty:** I'd probably run two more 1,000.

**Kyle Doherty:** So what you would do is you'd just bump this up to 2,000, run it, see how many credits it burned, do it again, see how many credits it burned.

**Kyle Doherty:** Once you do three, you can be like, okay, it's probably like, you know, for every 1,000, we're burning 600 credits.

**Kyle Doherty:** And now you could just do the math and be like, yeah, we can do all 18,000 with how many we have credit, how many we have this month, like we're good.

**Kyle Doherty:** And this table, let's see, I don't, this table we don't do enrichments that burn credits.

**Kyle Doherty:** We do, we use agents.

**Kyle Doherty:** Oh, no, no, actually, I take it back.

**Kyle Doherty:** We do, we have this one.

**Kyle Doherty:** So this one's like, I think it's two credits per person.

**Kyle Doherty:** So

**Kyle Doherty:** And this one's pretty aggressive with running.

**Kyle Doherty:** So you'll want to think about if you actually want to do it or not.

**Kyle Doherty:** So what I mean by aggressive is if you look here, it's checking if we are missing title or we're missing location, we run it.

**Kyle Doherty:** So if we're missing either or because we need both those pieces of data.

**Kyle Doherty:** But that means it's pretty much running for every single one.

**Kyle Doherty:** So it means for the most part, you're probably going to get like, you're going to burn two credits for every person basically.

**Kyle Doherty:** So this would cost, this should, if we look at the, I would estimate this is probably going to tell us it costs almost 2,000 in credits.

**Kyle Doherty:** Yeah, almost.

**Kyle Doherty:** Which at the end of the day is like, again, it sounds like a lot.

**Kyle Doherty:** It's like not a lot.

**Kyle Doherty:** But when you have 18,000 people, like you can burn through credits really fast.

**Kyle Doherty:** So it's just something to think about.

**Kyle Doherty:** I think.

**Kyle Doherty:** At the end of the day, like you have the 50,000 monthly credits, so like they're meant to be spent.

**Kyle Doherty:** But I just call this out because what can happen is you would like run this table and like burn all your credits and then you get to the next table and it can't finish.

**Kyle Doherty:** So then that's like kind of a pickle.

**Kyle Doherty:** So it's better to, in my opinion, it's better to just go incrementally and get all the ones ran that can run fully, save the HubSpot, and then just wait to the next month until you get.

**Kyle Doherty:** The credits.

**Kyle Doherty:** At that point, once you've done that, like let's say next month, like next week, you're able to get through all 18,000.

**Kyle Doherty:** You won't run into this problem anymore because this will just automatically update when new contacts get added to the list in HubSpot.

**Kyle Doherty:** And it'll only run for those new contacts.

**Kyle Doherty:** So you'll be burning a fraction of the credits.

**Kyle Doherty:** So it's kind of like a one-time like startup fee kind of, so to speak.

**Kyle Doherty:** So that's that, yeah, and then let's do one thing.

**Jesus Yepez:** The foundation data table, it already has all the fields populated, right?

**Jesus Yepez:** You just have to enrich it by thousands.

**Kyle Doherty:** Yeah, so it has, everything's there, if we, like, actually, can show you, because we can do it for a few, maybe, like, 1500, hit save, this table might be off, so, because I was testing and I to have it on, so we might have to manually run it, but, here, let me see.

**Kyle Doherty:** Okay, here, so now we're past the thousand, and you can see it hasn't run, because over here, I have the table turned off, I don't have it auto update, because if I'm doing something, when you're

**Kyle Doherty:** Testing tables, you should always have it off because what can happen is like if you do anything that over on the left side changes data, now all the stuff to the right will just start running.

**Kyle Doherty:** So if I was showing you guys this and I like fat fingered this and put like 10,000 and hit save, it would run for 10, like, you know, like it would auto run.

**Kyle Doherty:** Whereas if I fat finger right now and hit save, nothing's going to happen because I have it turned off.

**Kyle Doherty:** So what you can do when you're testing, Jesus, you come up here and you go to run column and you can say run.

**Kyle Doherty:** It seems scary because it says 1.4,000 rows, but it's 1.4,000 rows that haven't run or have errors.

**Kyle Doherty:** So it's only going to run the ones that haven't run or have errors.

**Kyle Doherty:** And so we can run all these that haven't run.

**Kyle Doherty:** Yeah, so now it's warning us like, hey, you've almost used up your monthly credits, which we're fine with.

**Kyle Doherty:** So you hit...

**Kyle Doherty:** Run, and now it's going to enrich these.

**Kyle Doherty:** So it'll do its thing, and then it's going to go over here, this, you would have to run manually too, I think, actually, let's check, it looks like it's running.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Interesting.

**Kyle Doherty:** And when we enrich both of that, so that's something where you have to be careful.

**Kyle Doherty:** So I had turned the table off, and then I was testing this column specifically, so I turned it back on.

**Kyle Doherty:** And so, like, now you can see, like, the table's off, but, like, this one's actually on, which is fine, I wanted this to all run, but, again, you could get yourself into trouble.

**Kyle Doherty:** So, just wanted to call that out.

**Kyle Doherty:** Yep.

**Kyle Doherty:** Uh.

**Kyle Doherty:** So, yeah, so here you can, credit should have gone down, Fathom's in the way, yeah, we're at, we're over 15,000 now, we're over 15,000, so, so sorry, what was your question?

**Jesus Yepez:** Just saying, if, if we enrich all 18,000 rows, then HubSpot will populate automatically the, the other companies?

**Kyle Doherty:** What do mean, sorry, I don't understand the question.

**Jesus Yepez:** So, there are 1,500 of 18,000 rows, right?

**Kyle Doherty:** Yeah, so right now, we, in this view, we can see 1,500, but in the table, as a whole, there's 18,000.

**Kyle Doherty:** So, you can start to enrich more and more, until you've enriched all 18,000.

**Kyle Doherty:** And then, And

**Kyle Doherty:** Once you've done all 18,000, then you're going to want to turn on this source.

**Kyle Doherty:** Actually, it's already turned on, which is fine, because you're not going to get another 10,000.

**Kyle Doherty:** You're going to get a few hundred at most every day.

**Kyle Doherty:** And so what this is doing is this is pulling from that list that I showed you in HubSpot.

**Kyle Doherty:** It's pulling, it's adding to this table.

**Kyle Doherty:** And so there's a new contact that we haven't enriched.

**Kyle Doherty:** It comes in here.

**Kyle Doherty:** It adds it as a new row.

**Kyle Doherty:** Perfect.

**Kyle Doherty:** And then it'll do its thing.

**Gloria Willis:** And it's also going the other way, as in once it's enriched here, it's being pushed into HubSpot?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So for this table, I actually had to finish that part.

**Kyle Doherty:** That was like something I was doing right before we were on the call.

**Kyle Doherty:** But it's going to push to HubSpot.

**Kyle Doherty:** So it's going to push.

**Kyle Doherty:** push.

**Kyle Doherty:** The seniority tier, location, and whether or not it's GTM.

**Kyle Doherty:** The company one is already doing that.

**Kyle Doherty:** So I'll show you.

**Kyle Doherty:** So we go to score and enrichment, and we go all the way over, it's doing, so you can see it's updating the object in HubSpot.

**Kyle Doherty:** So you can come in here and edit it, and you can see what it's doing.

**Kyle Doherty:** So let me ignore blank values.

**Kyle Doherty:** Oh, come on.

**Kyle Doherty:** Okay, well, it's not doing that.

**Kyle Doherty:** But it's supposed to just give it all these blank ones, so it's easier to see.

**Kyle Doherty:** you can see we're giving it the description, we're giving it total funding, like all that data that we got.

**Kyle Doherty:** And that's going to HubSpot.

**Kyle Doherty:** Now, one thing we do want to make sure.

**Kyle Doherty:** Yeah, so this table's on.

**Kyle Doherty:** We want that now.

**Kyle Doherty:** And I don't think I ever turned any of these off.

**Kyle Doherty:** But you.

**Kyle Doherty:** We want to double check, yeah, that those are on, so these are all on, this table's on and on, and so this one, same thing, this one is updating every day, so we can see every day, it's checking, it's like pulling from that list, and if there's new companies, it adds it to here and it runs that.

**Kyle Doherty:** The one other thing to call out, Jesus, is, we can delete this now if you want, but, because you potentially don't want it, I added, so we have this enrichment here, we're getting, this is a data provider, the tagma, and this is what, it's returning like all this people data, right, so it's giving us like, all this stuff, but we really only care about like, the location,

**Kyle Doherty:** And it's giving us a bunch of other data, so if you need another data, you can get it from here.

**Kyle Doherty:** But my point is, when you get those types of enrichments, we're getting all this data, it won't let you waterfall it, like what we were looking at earlier.

**Kyle Doherty:** So if you want to get data from additional data providers to fill in the gaps, you have to do that farther down in the, like to the right in the table.

**Kyle Doherty:** So I have this here as an example.

**Kyle Doherty:** This is turned off.

**Kyle Doherty:** So it won't run.

**Kyle Doherty:** But this is another data provider called Data People Labs, or People Data Labs.

**Kyle Doherty:** They're more expensive.

**Kyle Doherty:** So they're like five.

**Kyle Doherty:** I think this one's two credits per enrichment.

**Kyle Doherty:** This one's five credits per enrichment.

**Kyle Doherty:** But what you can do is you can give them the data, like plug in the work email, the LinkedIn, full name, company name.

**Kyle Doherty:** And then you can, then you'd do this check, like, only run this if jobs.

**Kyle Doherty:** Title merged and location merged don't exist.

**Kyle Doherty:** Run this.

**Kyle Doherty:** But you'd only want to do that if you feel like you're not getting enough data because it does cost more credits.

**Kyle Doherty:** So I think what's best is I'll delete this now.

**Kyle Doherty:** I just wanted to have it in here so I could show you on this call.

**Kyle Doherty:** And you have this recording, so if you want to add it back in, you can.

**Jesus Yepez:** Great.

**Kyle Doherty:** Cool.

**Kyle Doherty:** So I'm going to delete it and I'm going to delete these are both would have come from that.

**Kyle Doherty:** That's why it says PDL, people data labs.

**Kyle Doherty:** I'm deleting these as well just to keep it clean.

**Jesus Yepez:** Before I forget, Kyle, do you receive the recording of the last call we had?

**Kyle Doherty:** Do I have it?

**Kyle Doherty:** Yeah, because I didn't receive it.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Yeah, I can get that for you.

**Kyle Doherty:** I can follow up.

**Kyle Doherty:** After this call with this one and the last one.

**Jesus Yepez:** Oh, perfect.

**Kyle Doherty:** So that's pretty much it.

**Kyle Doherty:** Any questions related to this?

**Gloria Willis:** Yes.

**Gloria Willis:** Don't worry, I'm not going to ask you to explain any more of the deeper details, but I do need to share my screen real quick.

**Gloria Willis:** When we were meeting earlier, what you were swapping through, is that covering this?

**Gloria Willis:** Or is it going to lead to being able to get that covered?

**Gloria Willis:** So system syncs with all emails obtained and enriched?

**Kyle Doherty:** Are you talking about the AI-led growth stuff?

**Gloria Willis:** Well, we want to make sure that we're getting everything enriched.

**Gloria Willis:** So whether it's coming from Luma, Beehive, or Resource Vault, a.k.a.

**Gloria Willis:** library, or Circle?

**Gloria Willis:** Yeah.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So when they get added, if they have a company, if they're associated with a company, then the company will automatically get pulled into that table.

**Kyle Doherty:** And then it'll try to enrich that company.

**Kyle Doherty:** And then remember, like, we progressively enrich.

**Kyle Doherty:** So if they don't have that, if they don't fit that criteria, a set of $1 million in revenue or $2 million in funding, it won't continue to enrich them.

**Kyle Doherty:** So it'll enrich the company, then it'll save it to HubSpot.

**Kyle Doherty:** Then we do that check, like, is the company a fit?

**Kyle Doherty:** And that's where it's pretty strict, right?

**Kyle Doherty:** So then it wouldn't enrich those contacts if they don't fit that criteria.

**Kyle Doherty:** What we could do is we could, because Tyler's not really using that anymore, that fit criteria.

**Kyle Doherty:** So you could lax that fit criteria by a lot.

**Kyle Doherty:** You could even put it to, like, $1 if you wanted to.

**Kyle Doherty:** Mm-hmm.

**Kyle Doherty:** Now, the kicker is going to be that a lot of people are going to have personal emails, so they're not going to enrich.

**Kyle Doherty:** And if you want to do that, that's like a whole other animal.

**Kyle Doherty:** I could help with that, but it would be like a whole thing.

**Gloria Willis:** I don't think so, but to do that, to even get to the enriching, these systems do have to be synced with HubSpot first.

**Kyle Doherty:** Correct?

**Kyle Doherty:** Yes, Circle and Beehive would need to be.

**Kyle Doherty:** But I would double check with Ed and Jason because I feel like, because they had been doing that, and I feel like they had gotten those people in HubSpot, but maybe I'm wrong.

**Kyle Doherty:** If you're in HubSpot, Clay doesn't care and HubSpot doesn't care.

**Kyle Doherty:** It's just checking the filters.

**Gloria Willis:** Okay.

**Gloria Willis:** I'll just share this recording because I don't understand what's happening.

**Gloria Willis:** I just want to make sure that these systems are connected and that we're somehow making sure that all of these things are enriched because that's personally, for me, where I'm going to be pulling for in-person events as well as being able to build lists, whether we're sending in-house or whatnot, for these workshops and events is having good, clean data here.

**Gloria Willis:** Next thing is self-serve for building lists.

**Kyle Doherty:** if you can just create a, I think you may have already done that.

**Kyle Doherty:** I did create a big dock on that.

**Kyle Doherty:** Let me see if I can find it real quick.

**Gloria Willis:** Yeah, so if it's, whether it's a loom or whatnot, just so that I can go in, mostly what I've been doing is just going and like making slight edits to the segments we already have.

**Gloria Willis:** And those are all dynamic, right?

**Kyle Doherty:** So they're being, they're live and being updated as new names being put in, if it fits that criteria, it's being pushed into that segment.

**Kyle Doherty:** Mm-hmm.

**Kyle Doherty:** Yeah, um, let me find the docs.

**Kyle Doherty:** I was supposed to say that?

**Kyle Doherty:** Nope.

**Gloria Willis:** Because I think, Hazel, if we, if both of us are getting really good at being able to build segment lists, it's going to be really, really good for both of us to be able to get in there.

**Gloria Willis:** don't know.

**Gloria Willis:** Do you already know how to build segments in HubSpot?

**Gloria Willis:** Nope.

**Gloria Willis:** Let's both learn.

**Gloria Willis:** I have a very basic understanding, but there is some parts where I get stuck.

**Gloria Willis:** But while you're looking for that, Kyle, the only other thing is I don't know how far or if we were ever able to do anything with being able to, like, build out sending emails from HubSpot marketing because we have our – the list that we created for our last event, which are all contacts that are local to the Bay Area.

**Gloria Willis:** They're in our HubSpot.

**Gloria Willis:** Ideally, would be nice if I can just build an email within HubSpot to send an invite to that because they're not in Luma rather than having to upload or download that list and then send it over to understory and then they have to send it.

**Gloria Willis:** But I know Jason was saying something along the lines of having to, like, warm up our – I don't know.

**Kyle Doherty:** Yeah, one of the email domain.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So, yeah, you guys can send.

**Kyle Doherty:** Like, it's set up.

**Kyle Doherty:** You have to make the email.

**Kyle Doherty:** But it's already sending for people that are downloading.

**Kyle Doherty:** Downloading those lead magnets.

**Kyle Doherty:** So that is actually starting to warm it up.

**Kyle Doherty:** I don't think it's a ton of volume, though, so it's not going to warm it up a ton.

**Kyle Doherty:** But also domains get sort of warmer as they age, too, so it's helping just from being older.

**Kyle Doherty:** The thing that you can do is people, a lot of the people that are, like, in there aren't actually, like, marketing contacts.

**Kyle Doherty:** Are you trying to send to people about events from people that are from Luma?

**Gloria Willis:** No, I'll send those people invites in Luma.

**Kyle Doherty:** So if they're in Luma, they'll get an invite from Luma.

**Gloria Willis:** If they're not in Luma, but they fit the criteria of who I want to invite, there's still that.

**Gloria Willis:** This is like 600 people, but like if they're not marked as a marketing contact, then.

**Kyle Doherty:** So, well, actually, like who are they?

**Gloria Willis:** I don't know, people who fit the ICP of who I want to invite.

**Kyle Doherty:** Okay, but they're just like in the CRM.

**Gloria Willis:** Yeah, they're just in HubSpot.

**Gloria Willis:** They aren't necessarily customers.

**Gloria Willis:** There aren't people who are in Py.

**Kyle Doherty:** They're just contacts.

**Kyle Doherty:** They're in HubSpot somehow.

**Kyle Doherty:** Like I wouldn't recommend doing that because A, you have a lot of people from Europe and like that's going to be like a huge no.

**Kyle Doherty:** If they're AIG people, you probably could get away from it, but I think you would just mess it up from AIG, right?

**Gloria Willis:** Yeah, yeah, I would just do it then.

**Gloria Willis:** So basically we're saying, and this will just be just for the invites for the breakfast.

**Gloria Willis:** Okay.

**Gloria Willis:** So just...

**Gloria Willis:** It's Bay Area locals.

**Gloria Willis:** wouldn't be everybody.

**Gloria Willis:** So basically, it's not.

**Kyle Doherty:** If they've come to an event, they're in Loma, so.

**Gloria Willis:** Right, yeah.

**Gloria Willis:** So these are completely cold-ish, but they're in our database.

**Gloria Willis:** So we have at least their contact information, but I don't know.

**Gloria Willis:** Could be any which.

**Kyle Doherty:** Oh, yeah.

**Kyle Doherty:** If they're Bay Area, you could do it.

**Kyle Doherty:** You'll be able to do it.

**Kyle Doherty:** You're not going to be violating GDPR.

**Kyle Doherty:** You can even make an argument that, like, your email is relevant.

**Kyle Doherty:** Like, you could do it.

**Kyle Doherty:** If we're in, like, France, I would say no, but we're not, so.

**Gloria Willis:** And how would I see, last question, and then I swear we can be done.

**Gloria Willis:** How would I see if they're considered a marketing contact?

**Gloria Willis:** So is there, is that a field?

**Gloria Willis:** Is that a checkmark?

**Gloria Willis:** Can I just get them from that list?

**Kyle Doherty:** Yeah, it is.

**Kyle Doherty:** So it's actually like a subscription type.

**Kyle Doherty:** I've been...

**Kyle Doherty:** I can, I created a video that went through how the lead magnets are working and it covers like that part of it.

**Kyle Doherty:** Like when you set up an email, you have to set the marketing, sorry, you have to set the list, a subscription list that they're a part of.

**Kyle Doherty:** And that specifically is the marketing one for the emails you're talking about.

**Kyle Doherty:** And so that would be on there.

**Kyle Doherty:** So what you would have to do for these people is you would have to like, you'd have, you'd create that segment, right?

**Kyle Doherty:** And then you'd have to go either in the segment or in a view.

**Kyle Doherty:** Actually, wouldn't, yeah.

**Kyle Doherty:** Anyways, in a view and you could just like mark them as subscribed.

**Kyle Doherty:** Or if it's a huge number of people, you could ask Jesus to help you create a workflow that automatically subscribes them.

**Kyle Doherty:** And the reason you have to do that is because Hotspot won't let you send it because it's like, hey, like.

**Kyle Doherty:** body's Thedro The

**Kyle Doherty:** So you're on our shared IPs, like you're going to screw up the IPs.

**Kyle Doherty:** Okay.

**Kyle Doherty:** So yeah, so it'll work.

**Kyle Doherty:** And if you're sending to like what, you'll be sending a few hundred people?

**Gloria Willis:** Like 600 people.

**Kyle Doherty:** 600.

**Kyle Doherty:** So what you can do is you can, if you just plan it far enough advance, like you don't have to do multiple emails or anything.

**Kyle Doherty:** You'd have one email template.

**Kyle Doherty:** And what you do is you'd split your list of the 600 people into probably like three lists.

**Kyle Doherty:** Like I would do 100 first, then the next day do 200, and then the third day do 300.

**Kyle Doherty:** Okay.

**Kyle Doherty:** And so you just send the first list the first day, that'll be 100 people.

**Kyle Doherty:** The next day, 200.

**Kyle Doherty:** The third day, 300.

**Kyle Doherty:** And then at that point, like the domains sent to 300 at one time.

**Kyle Doherty:** Like you can do 400, you can even.

**Kyle Doherty:** You can do like 500 the next time, 800, 1,000.

**Kyle Doherty:** It's pretty straightforward.

**Kyle Doherty:** And if you are unsure, you can just ask ChatGVT like, hey, I have a new domain, a new marketing domain.

**Kyle Doherty:** I need to warm it up.

**Kyle Doherty:** We've already just tell it like we've already sent 50 emails.

**Kyle Doherty:** Give me a warming schedule and it'll just tell you what I just said.

**Kyle Doherty:** It'll say like 700, then 200, then 300.

**Kyle Doherty:** And then you just go from there.

**Kyle Doherty:** At that point, you're going to be good unless you try to rip off like 10,000.

**Kyle Doherty:** But if you go from 300 to like 500, 600, you're going to be fine.

**Gloria Willis:** Cool.

**Jesus Yepez:** Is that the video that you talked about is on Slack?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** I sent it to Ed and Jason in the GTF channel.

**Jesus Yepez:** Oh, okay.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** And then how to actually send, like use the tool to send emails.

**Kyle Doherty:** Huzzle has a ton of good content on that in there.

**Kyle Doherty:** Uh, in their university, um, on just how to use it.

**Kyle Doherty:** Um, but if you ever use like email marketing tool, which I know, well, I don't think you have, but Jesus, if you have, and like, since you're kind of taking over this stuff, Jesus is probably a good thing to do, uh, watch.

**Kyle Doherty:** And they even have like a certification on like doing inbound.

**Kyle Doherty:** And one of the big components of that is like doing email marketing.

**Kyle Doherty:** Um, it sounds confusing, but like once you understand the components, it's pretty simple.

**Kyle Doherty:** So you just always remember that if you're sending an email blast, you just have like the components that you have is you have a list, right?

**Kyle Doherty:** And then you create an email and like, then you tell it to send a manual send.

**Kyle Doherty:** Um, and so it's just like a one-off blast.

**Kyle Doherty:** If you want to do like a drip one, you can, uh, then it's a bit trickier, but all it is, is the same thing.

**Kyle Doherty:** You have a list of who you're sending to.

**Kyle Doherty:** You either are triggering the send manually, or you're triggering it using like an event.

**Kyle Doherty:** That's kind of it.

**Kyle Doherty:** It's like event or manual.

**Kyle Doherty:** So it's like list, list, trigger.

**Kyle Doherty:** And then if you're doing a drip, then you do this in a workflow.

**Kyle Doherty:** And so you would just set that up in a workflow and you'd create your email templates for email one, two, three, and then you just put them in the workflow.

**Gloria Willis:** Okay.

**Gloria Willis:** Yeah.

**Gloria Willis:** Cause that, that's essentially what I know Jason wants us to do as well.

**Gloria Willis:** So registered for an event, attended an event, attended the event is the trigger that then starts the three email sequence.

**Kyle Doherty:** Yep.

**Kyle Doherty:** And that one is like very similar.

**Kyle Doherty:** It's the same concept as this, when you're doing email sequences where it's one-to-one.

**Kyle Doherty:** So it's like the same idea.

**Kyle Doherty:** mean, all these tools do, they all work the same way.

**Kyle Doherty:** It's like, who are we sending to?

**Kyle Doherty:** What's the trigger to send?

**Kyle Doherty:** And the trigger is either an event or you're just pushing a button that says send.

**Jesus Yepez:** Got it.

**Kyle Doherty:** Yeah, so I just sent you this link, Gloria, about segments.

**Kyle Doherty:** I think it'd be good to just go over that real quick.

**Kyle Doherty:** So let me share my screen.

**Gloria Willis:** You sent it in.

**Kyle Doherty:** Sorry, in Zoom.

**Kyle Doherty:** Okay.

**Kyle Doherty:** So if you guys save that.

**Kyle Doherty:** So, yeah, so this is the HubSpot segment guide.

**Kyle Doherty:** It explains, like, the problem that we were having.

**Kyle Doherty:** Like, there was obviously all these segments that were in there, and they're confusing.

**Kyle Doherty:** Um, so Yeah.

**Kyle Doherty:** What I did is I built out a framework that you can read through this, but basically it's like, it comes down to, you have funnel stages and you have other dimensions of how you want to slice them.

**Kyle Doherty:** So funnel stages are things like, are they a customer?

**Kyle Doherty:** Are they not a customer?

**Kyle Doherty:** Are they in a deal?

**Kyle Doherty:** Are they not in a deal?

**Kyle Doherty:** Right?

**Kyle Doherty:** Like our funnel, like growthx is funnels, like super simple.

**Kyle Doherty:** It's just really nice.

**Kyle Doherty:** Right.

**Kyle Doherty:** It's just like, but they're not in a deal.

**Kyle Doherty:** They're just like a lead or they're in a deal or they're a customer.

**Kyle Doherty:** It's kind of it.

**Gloria Willis:** So is that one through four?

**Gloria Willis:** So one is a lead, two is...

**Gloria Willis:** Oh, this is just an example.

**Kyle Doherty:** Oh, okay.

**Kyle Doherty:** That's two, that's three, that's four.

**Kyle Doherty:** So this is totally just an example.

**Kyle Doherty:** And then it's saying, and then you can slice that up more if you want.

**Kyle Doherty:** You have dimensions.

**Kyle Doherty:** So you also could just be like, I don't want to look at funnel stages, right?

**Kyle Doherty:** I just want to send to everyone there is.

**Kyle Doherty:** So in that case, you might want to just slice by dimensions and dimensions could be anything.

**Kyle Doherty:** So it could be things like...

**Kyle Doherty:** What location are they in?

**Kyle Doherty:** It could be like, what's their title?

**Kyle Doherty:** Are they senior?

**Kyle Doherty:** Are they not senior?

**Kyle Doherty:** So that's what I mean by dimensions.

**Kyle Doherty:** At the end of the day, the funnel stages are dimensions too.

**Kyle Doherty:** It's all dimensions and you're just slicing them up.

**Kyle Doherty:** But it's easier to talk about if we, yeah, kind of group them into buckets.

**Kyle Doherty:** So you have what stage they're in and you have dimensions.

**Kyle Doherty:** When you combine those, you have a segment.

**Kyle Doherty:** And you could just remove the stage or the dimension.

**Kyle Doherty:** You still have a segment.

**Kyle Doherty:** But again, it's just easier to think about this way.

**Kyle Doherty:** So then I noted what are some of the standard dimensions that we care about?

**Kyle Doherty:** So like I said, the stage or the status within a stage can be a dimension.

**Kyle Doherty:** So an example would be you're in a deal.

**Kyle Doherty:** Like you've been in a deal.

**Kyle Doherty:** What status or what stage of the deal are you?

**Kyle Doherty:** Or sorry, what status are you for that?

**Kyle Doherty:** Or are customers better?

**Kyle Doherty:** better?

**Kyle Doherty:** For if you're a customer, are you a current customer or like an active customer or a past customer?

**Kyle Doherty:** If you're, if you've reached the deal stage, are you an open deal or are you a closed deal?

**Kyle Doherty:** Then you have sub stages too.

**Kyle Doherty:** So deals are a good example.

**Kyle Doherty:** Deals have stages within, within deal.

**Kyle Doherty:** So if you're in the stage deal, there's sub stages of that deal.

**Kyle Doherty:** There's also engagement stages.

**Kyle Doherty:** So you can be like, are they engaged?

**Kyle Doherty:** they not engaged?

**Kyle Doherty:** So that could be like, have, have they received an email recently or like sent an email recently or not?

**Kyle Doherty:** Have they had a meeting booked recently or not?

**Kyle Doherty:** Those are like types of engagements.

**Kyle Doherty:** So here I put together the funnel, like a very simple one.

**Kyle Doherty:** You guys should change this.

**Kyle Doherty:** I tried to get this standardized, but it's not.

**Kyle Doherty:** So it's like captured is just S1.

**Kyle Doherty:** Um.

**Kyle Doherty:** Um.

**Kyle Doherty:** Um.

**Kyle Doherty:** So that's like, they exist, right?

**Kyle Doherty:** We have them in the CRM.

**Kyle Doherty:** ICP fit is that fit score that we did.

**Kyle Doherty:** So, but that, just remember that that's on the company, but contacts inherit that from the company.

**Kyle Doherty:** Because the contacts, I mean, it's only a fit if their company is a fit, right?

**Kyle Doherty:** Then opportunity is opportunity and customer is customer.

**Kyle Doherty:** So those are the stages.

**Kyle Doherty:** And again, this is very simplified.

**Kyle Doherty:** People get more advanced.

**Kyle Doherty:** You could add like post-acquisition stages.

**Kyle Doherty:** I don't want to get into that, so I didn't.

**Kyle Doherty:** So this just maps it out more so you can visualize it.

**Kyle Doherty:** So this is just a visualization of what I just showed you.

**Kyle Doherty:** Yeah, and then this starts to document the segments that I created.

**Kyle Doherty:** So what I did was I created canonical segments for all these standard dimensions that we talked about.

**Kyle Doherty:** So status, sub-stages, engagement, location, do not contact.

**Kyle Doherty:** The reason I did that is we have these, they exist.

**Kyle Doherty:** And you.

**Kyle Doherty:** then can use these as building blocks to compose new segments.

**Kyle Doherty:** So an example would be, there's a segment of active customers or active deals.

**Kyle Doherty:** I want a segment of contacts whose companies have active deals who also are in the Bay Area.

**Kyle Doherty:** So then you would go, you would combine that segment, the active deals and the Bay Area one.

**Kyle Doherty:** You combine those two segments and it gives you the segment active deal in the Bay Area.

**Kyle Doherty:** And that way you don't like be trying to create these all the time.

**Kyle Doherty:** just compose what you need from these segments.

**Gloria Willis:** And then do we need to add one more dimension would be that new category of leader, executive, market.

**Gloria Willis:** I see, that be under there?

**Kyle Doherty:** Yeah, probably.

**Kyle Doherty:** That might be in there already, but let's see.

**Kyle Doherty:** So, yeah, this would be helpful because it will show where they are.

**Kyle Doherty:** Oh, no, that's not what I want.

**Kyle Doherty:** So you come down here for segments.

**Gloria Willis:** They used to call them lists, so that's why I said segment lists.

**Kyle Doherty:** And then, let me see what they have.

**Kyle Doherty:** No, I don't.

**Kyle Doherty:** So you search by this.

**Kyle Doherty:** This is going to, like, contact pipe is going to give you all the ones that I created for contacts that are, like, the standard that I did.

**Kyle Doherty:** Well, it'll include some other ones, too, probably, but it'll get you to some of them.

**Kyle Doherty:** So you can can see.

**Kyle Doherty:** Yeah, so actually I created it, so you have contact marketing leaders, and you can see that it's, but it's using employment, so this was using like the old way, but now that we have that new one, you could create a, you could create, you could copy this pattern and do, use the new one.

**Kyle Doherty:** So that's employee, employment seniority tier, and that's those tiers that Danny came up with, so these ones.

**Kyle Doherty:** So you could be like, I only want leaders, I only want execs.

**Kyle Doherty:** So what I would do, if I were you, is I would create canonical versions of all three of these, and then you can use those to compose whatever you want.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Because if, if then, if then you need, oh, I need one that's leaders and execs, or leaders and managers, then you would just combine them to make that.

**Gloria Willis:** Mm-hmm.

**Gloria Willis:** Okay.

**Gloria Willis:** Okay.

**Gloria Willis:** Okay.

**Kyle Doherty:** Yeah, that's how that works.

**Kyle Doherty:** This goes into like more detail.

**Kyle Doherty:** So it's like customer stage segments, et cetera, et cetera, location.

**Kyle Doherty:** So this like maps out how I did it and how works.

**Gloria Willis:** I was more so concerned with how to actually build those segments in HubSpot.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Yeah, here I can show you that.

**Kyle Doherty:** So you go to segments and then you go to create segment and then you choose what object you care about.

**Kyle Doherty:** So the case that we're talking about, we would want.

**Kyle Doherty:** And for this one, let's say that we want that one that I said, so deal, like, so if you want to create a brand new segment, then you're going to use properties.

**Kyle Doherty:** So it'd be like, whatever you want, like, what's like a good example?

**Kyle Doherty:** So you could do, like, date of last meeting is, you could probably do, like, I don't know, a few, like, someone had a meeting less than, like, 90 days ago.

**Kyle Doherty:** So could do that.

**Kyle Doherty:** So that would include everyone that had a meeting less than 90 days ago.

**Kyle Doherty:** So that's, like, how you...

**Kyle Doherty:** And then you can add more things like and they something else.

**Kyle Doherty:** An example, could do like company fit score is good.

**Kyle Doherty:** So they had a meeting in last 90 days and they had a fit score of good.

**Kyle Doherty:** You're almost always going to want to use ands or you're generally not going to want to use.

**Kyle Doherty:** Obviously, that's just going to include both instead of filtering down people that only have booked a meeting in 90 days and have a fit score of good.

**Kyle Doherty:** So that's how you make a brand new one.

**Kyle Doherty:** When you want to make the ones that I was talking about where you're composing them.

**Kyle Doherty:** That's where instead of using properties, you're going to use memberships.

**Kyle Doherty:** So here we're going to be like, are they a member of one of those canonical lists that we talked about?

**Kyle Doherty:** So if we said like deal active So let's putter on.

**Kyle Doherty:** So we have contact whose company has an open deal, so that means like they're in this segment and so it's already put us because we're doing the end here, it's already checking segment membership.

**Kyle Doherty:** You also can add other ands for like specific properties if you want, just want to call it out.

**Kyle Doherty:** But like so then let's say the Bay Area one and the contacts in the Bay Area.

**Kyle Doherty:** So now it's like only people have an open deal and are in the Bay Area.

**Gloria Willis:** Okay.

**Kyle Doherty:** And what you're going to want to do though is you're going to want to always check first.

**Kyle Doherty:** So if you know you're looking for open deal, Bay Area.

**Kyle Doherty:** Bay Area, first thing you're going want to do is check OpenDeal, because it probably exists, so you can see here, company has OpenDeal, and it's specifically new business deals, so, like, not renewals, Bay Area.

**Kyle Doherty:** So, and the doc explains the naming, but it basically starts with, what's the object?

**Kyle Doherty:** The reason is just so you don't have, it's, like, very easy to see from the title.

**Kyle Doherty:** You technically can go over here and be like, oh, it's for the contact, but it's just nice to be able to just see it here.

**Kyle Doherty:** And also, if you're looking at it somewhere else, you won't know really easily, because you won't have that column there that says, it's a contact object, then the net, then it has a pipe, and then it's, it just, then it goes by what.

**Kyle Doherty:** What's the next filter?

**Kyle Doherty:** So company has an open deal is the next one.

**Kyle Doherty:** Oh, this is a bad example.

**Kyle Doherty:** Here's a better example.

**Kyle Doherty:** So contact, company has an open deal, then it's pipe, then it's new business.

**Kyle Doherty:** So it's like the pipeline is new business.

**Kyle Doherty:** So it's not renewals, it's not expansions.

**Kyle Doherty:** And then it's Bay Area is the last thing.

**Kyle Doherty:** So it's like progressively filtering down.

**Kyle Doherty:** That's how the naming goes.

**Kyle Doherty:** So that's like pretty easy to follow.

**Kyle Doherty:** You can't read it like a sentence, but kind of, right?

**Gloria Willis:** OK.

**Gloria Willis:** So for a list for Bay Area, if I want to just use the canonical lists, I would start with the Bay Area list.

**Gloria Willis:** And then I would say Bay Area and is this title.

**Kyle Doherty:** Yeah.

**Gloria Willis:** And then I would have to do an or Bay Area and is this title.

**Gloria Willis:** couldn't say, and is this title.

**Gloria Willis:** And this title, and this title, and this title, title, because then that would try to find only ones that have all of those titles, correct?

**Kyle Doherty:** Yeah, but what you could do is you could create a segment for those titles you're looking for first.

**Kyle Doherty:** So you could do contact, add filter, properties, title, job title.

**Kyle Doherty:** Well, I thinking, like, the tiers, the title, the tiers.

**Kyle Doherty:** so I don't have that in here yet, but, like, this will just show, this will be, like, a good example.

**Kyle Doherty:** So it can be, like, contains any of, I don't know, revops, right?

**Kyle Doherty:** Or, I don't know, events, right?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So this one's going to do, it's, like, job Job contains revops or events.

**Kyle Doherty:** For that one, it's going to be the same thing, but it's going to be picking either.

**Kyle Doherty:** All those are two of those, so you'd create that segment, and then you'd now have that canonical one.

**Kyle Doherty:** Then you would go create a new segment that uses both those segments, Bay Area plus that one where you're checking for all of them.

**Gloria Willis:** I guess I'll just have to play around with it, because I'm trying to see.

**Gloria Willis:** I don't want to compute.

**Gloria Willis:** I'll just play around with it.

**Gloria Willis:** I think I can, I'll get it.

**Kyle Doherty:** Yeah, the easiest way, though, is to use, like, is to combine segments, because then you don't have to do what you're saying, where you're like, or this and this.

**Kyle Doherty:** You don't have to do, like, all those presentations.

**Kyle Doherty:** You're saying, like, hey, you're one of these titles, and you're in the Bay Area.

**Kyle Doherty:** Right.

**Kyle Doherty:** The way I know that is because I'm saying you have to be in both these segments.

**Gloria Willis:** Yes.

**Gloria Willis:** So I have the, the, those major canonical.

**Gloria Willis:** I have to be built first, and they're not built yet, because that property is not in HubSpot yet, or it is in HubSpot.

**Kyle Doherty:** We can just do it real quick.

**Gloria Willis:** I have no clue what time it is where you're at.

**Jesus Yepez:** No, no worries.

**Kyle Doherty:** I also have a question.

**Kyle Doherty:** Let me do seniority.

**Jesus Yepez:** And I'm learning too, so.

**Kyle Doherty:** So what we're going to do, growthx, contact household ID.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Okay, so what we're going do is we're just going to, luckily like when you do this, it doesn't charge anything, so you run this like over and over again, doesn't matter.

**Kyle Doherty:** So I'll come back and add the other data we need, but right now I just want this.

**Kyle Doherty:** So now it's updating all these people, so here I'll get an exec.

**Kyle Doherty:** So we'll come in here.

**Kyle Doherty:** So we'll create a new one for contacts, Gloria.

**Kyle Doherty:** So we'll come in here, contacts, and we'll make it for execs.

**Kyle Doherty:** So it'll be like, contact, what is this probably called?

**Kyle Doherty:** Okay.

**Kyle Doherty:** So

**Kyle Doherty:** So, contact, this tier equals executive, and like, that's it, right?

**Kyle Doherty:** Because that's like all the filters we have.

**Kyle Doherty:** And then, so what we do is we come in here, say, employment seniority tier is equal to any of, and then we pick, oops, not that one, executive.

**Kyle Doherty:** And then, so, yeah, so you could, that would be the one for executive.

**Kyle Doherty:** Yeah.

**Gloria Willis:** You're going to want them for all three of those.

**Kyle Doherty:** So then when you want them for multiple, so you could be like employment seniority equals executive or whatever they like, they're like leader.

**Kyle Doherty:** You kind of have two options.

**Kyle Doherty:** You can combine the two segments, but it's like so simple.

**Kyle Doherty:** So, like, in this case, you don't really need to combine two segments to make it for executive and leader.

**Kyle Doherty:** If you want it for all three, then you just add the third one.

**Kyle Doherty:** And now you have, but I'll go back to this, because I think this is, let's actually do a few, well, let's leave it.

**Kyle Doherty:** But, like, there's definitely going to be one, well, the one that you're probably going to use the most, sorry, I'm going back and forth, but, like, it's probably going to be this one, right?

**Kyle Doherty:** So, let's make that one.

**Kyle Doherty:** Then you just save this.

**Kyle Doherty:** It says 451.

**Kyle Doherty:** Obviously, that's going to go up as that runs, that table, but we don't have that many right now.

**Kyle Doherty:** But after we enrich 18th.

**Kyle Doherty:** 1000, there's going be a lot.

**Kyle Doherty:** And I didn't add in the GTM, right?

**Kyle Doherty:** So actually, that's like a really good example where I set to add that property where it's like, is GTM role?

**Kyle Doherty:** And then that's where you would combine both of them.

**Kyle Doherty:** Because there could be instances where you just want execs and leaders and you're kind of like, I don't care what they are.

**Kyle Doherty:** But then there's going to be times you're like, nope, I only want them to be GTM.

**Kyle Doherty:** So then you're going to take both segments.

**Kyle Doherty:** These people are a GTM role.

**Kyle Doherty:** These people are this, are execs or leaders.

**Kyle Doherty:** When you combine them, they have to be in both.

**Kyle Doherty:** So it's only going to give you people that are execs or leaders and in a GTM role.

**Gloria Willis:** Perfect.

**Gloria Willis:** Now I'm done.

**Gloria Willis:** Sorry, go for your question.

**Jesus Yepez:** No, no worries.

**Jesus Yepez:** I'm sure it was very worth it.

**Jesus Yepez:** Well, my question is just a recommendation, quick recommendation, because we created

**Jesus Yepez:** We links for tracking links for the ALG workshops.

**Jesus Yepez:** We just want to know the traffic coming from YouTube videos.

**Jesus Yepez:** And we're not sure if HubSpot is showing the stats like very friendly to follow.

**Jesus Yepez:** And I think if you go to marketing and campaigns, you'll be able to see the links.

**Kyle Doherty:** Oh, you created links in the campaigns?

**Jesus Yepez:** Yeah.

**Jesus Yepez:** And the campaign is called that one, Bolt.

**Kyle Doherty:** Sorry, too many pop-ups.

**Kyle Doherty:** Okay, sorry.

**Kyle Doherty:** What did you create?

**Jesus Yepez:** If you go to assets, so we created tracking links for all those five links just to, the track, if the track.

**Jesus Yepez:** I think it's coming from YouTube.

**Kyle Doherty:** Okay.

**Jesus Yepez:** But we just want to see the stats, and we don't know which ones are coming from YouTube, which ones are coming from other sources.

**Jesus Yepez:** So I'm not sure if HubSpot is the right spot to track that.

**Kyle Doherty:** Okay, let me go back to the URLs.

**Kyle Doherty:** So you're using...

**Jesus Yepez:** It's just that when we want to see the stats for traffic, we don't know which link is which.

**Kyle Doherty:** Wait, but these have the same tags.

**Jesus Yepez:** So what are the different links?

**Jesus Yepez:** So if you go down...

**Kyle Doherty:** Like if I edit columns, let's see.

**Kyle Doherty:** So you came in here and plugged in the URL, right?

**Kyle Doherty:** Exactly.

**Kyle Doherty:** So I get that, but like normal, like what, like just explain to me what the different URLs are.

**Jesus Yepez:** So in the campaign, in marketing campaign, you'll be able to see the, well, there you go.

**Jesus Yepez:** So all of them are different, but HubSpot just named them like the same thing.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Like I wouldn't use their tool for this.

**Kyle Doherty:** It's not super good.

**Kyle Doherty:** Okay.

**Kyle Doherty:** I guess so you're sending them to different resources.

**Jesus Yepez:** Yep.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So, well, the other thing is like normally you'd also add this UTM content.

**Kyle Doherty:** I mean, you don't really need it though, but like, I think that's what they're expecting you to do.

**Kyle Doherty:** Uh.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Which is, yeah, some of their tools just aren't the best in class for what they do, right?

**Kyle Doherty:** Because they're just giving you for free, unfortunately.

**Kyle Doherty:** So they'd make you, like, click into details, which is super annoying.

**Kyle Doherty:** Because normally you'd, like, title this, but another way you can do it is, so, let get into this.

**Kyle Doherty:** So what is this?

**Kyle Doherty:** This is a specific resource.

**Kyle Doherty:** Yeah, that's the workshop for Is Your Website Optimized?

**Kyle Doherty:** Okay.

**Kyle Doherty:** So a lot of times what you'd do is you'd come in and you'd create a UTM content tag that would be, like, Is Your Website Optimized?

**Kyle Doherty:** And, like, then you would know it's for that one.

**Kyle Doherty:** Because you need to know, like, which one you're Right.

**Jesus Yepez:** And then do you think it will show up in the stats or in the deck?

**Kyle Doherty:** Yes, then you can click on it, and you can go to the stats for that.

**Kyle Doherty:** And so this one's for that link, though, so you can just, like, see.

**Kyle Doherty:** This one doesn't look like it has anything.

**Kyle Doherty:** But yeah, I wouldn't, I don't know that I would use this one for it, per se.

**Kyle Doherty:** Like, you could use, like, bit.ly, or, like, any of the other ones would be better.

**Kyle Doherty:** Because all, like, this one is actually, this one's actually not, this one's not helping you.

**Kyle Doherty:** This one is tracking UTM parameters that have come hit the, like, hit a website that has HubSpot tracking.

**Kyle Doherty:** And, like, the website doesn't have that.

**Kyle Doherty:** Oh, okay.

**Kyle Doherty:** But you also, you guys have Google Analytics.

**Kyle Doherty:** And I think you might have PostHog.

**Kyle Doherty:** Do you know if you have PostHog?

**Kyle Doherty:** Yeah, you do.

**Kyle Doherty:** So on PostHog, you'll be able to see this.

**Kyle Doherty:** So, like, that's where, like, you should, like, I recommend using the analytics tools.

**Kyle Doherty:** I like PostHog way better than Google Analytics.

**Kyle Doherty:** So if I were you, I'd use PostHog.

**Kyle Doherty:** way, way better, in my opinion.

**Kyle Doherty:** So in PostHog, you can see what pages are being visited, and you'll be able to see those UTM templates.

**Kyle Doherty:** But that's why you will want to use the, let go back.

**Kyle Doherty:** You will want to use the UTM content because if you want to look at, like, you'll be able to see, okay, like, how many people landed here who came from the source YouTube.

**Kyle Doherty:** You'll be able to do that.

**Kyle Doherty:** You'll able to do, how many came from social.

**Kyle Doherty:** Um...

**Kyle Doherty:** And then, but you won't be able to see like what specific content did they come from because you don't have the UTM content tag.

**Kyle Doherty:** So you want to add the UTM content tag so you know which resource was it for.

**Kyle Doherty:** And that's how you'll get it.

**Jesus Yepez:** Got it.

**Jesus Yepez:** Got it.

**Jesus Yepez:** Excellent.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So, I mean, so this can work if you do it that way.

**Jesus Yepez:** If not, we can just use PostHog.

**Kyle Doherty:** Well, no.

**Kyle Doherty:** So what I mean is like this will work for like creating the URLs that you need with that are tagged because that's ultimately that's all this is doing.

**Jesus Yepez:** Okay.

**Kyle Doherty:** Because this is this isn't meant for like tracking anything.

**Kyle Doherty:** It's creating the tracking that's going to show up in PostHog.

**Jesus Yepez:** Oh, okay.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So that's why.

**Kyle Doherty:** why.

**Kyle Doherty:** And then, but you won't be able to see like what specific content did they come from because you don't have the UTM content tag.

**Kyle Doherty:** So you want to add the UTM content tag so you know which resource was it for.

**Kyle Doherty:** And that's how you'll get it.

**Kyle Doherty:** Got it.

**Kyle Doherty:** Got it.

**Kyle Doherty:** Excellent.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So, I mean, so this can work if you do it that way.

**Kyle Doherty:** If not, we can just use PostHog.

**Kyle Doherty:** Well, no.

**Kyle Doherty:** So what I mean is like this will work for like creating the URLs that you need with that are tagged because that's ultimately that's all this is doing.

**Kyle Doherty:** Okay.

**Gloria Willis:** Because this is this isn't meant for like tracking anything.

**Jesus Yepez:** It's creating the tracking that's going to show up in PostHog.

**Kyle Doherty:** Oh, okay.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So that's why.

**Kyle Doherty:** why.

**Kyle Doherty:** Thanks, Kyle.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Thank you so much.

**Kyle Doherty:** And if, because you have, because we do have HubSpot marketing now, you could add the HubSpot tag to the website.

**Kyle Doherty:** I, personally, I wouldn't do that because you already have PostDog.

**Kyle Doherty:** It's just going to be one other tool to like look at the analytics.

**Kyle Doherty:** The analytics are like sort of okay.

**Kyle Doherty:** They're not great.

**Kyle Doherty:** So I would just use PostDog.

**Kyle Doherty:** Just have like one source of truth.

**Kyle Doherty:** Just have it be PostDog for your digital analytics because that's what it's good at, right?

**Kyle Doherty:** Perfect.

**Kyle Doherty:** That's my recommendation.

**Kyle Doherty:** Cool.

**Kyle Doherty:** Any other questions?

**Kyle Doherty:** Nope.

**Kyle Doherty:** Super helpful.

**Kyle Doherty:** Super, super helpful.

**Kyle Doherty:** Nice.

**Kyle Doherty:** So yeah, Gloria, the stuff I was talking about, I'll be honest, like that probably won't be done until Monday.

**Kyle Doherty:** So that's like getting in all that old data.

**Kyle Doherty:** data.

**Kyle Doherty:** Let's

**Kyle Doherty:** Um, and, oh, they'll do them about, like, how to do the uploads.

**Kyle Doherty:** It's fun.

**Kyle Doherty:** Cool.

**Kyle Doherty:** And then, then you have Britton's email, if you have any EventHapply stuff.

**Kyle Doherty:** Um, but everything's, like, pretty much set up now.

**Kyle Doherty:** Um, you will need to eventually create the reports.

**Kyle Doherty:** Um, but I think, like, Jesus or someone can help you with that.

**Kyle Doherty:** Um, you'll also, though, just have, like, if you go into the event, so, like, that test one I did, um, like, at the end of the day, like, the reality is, like, you probably won't have that many deals that are associated, right?

**Kyle Doherty:** So, you can just look here, but, like, five, right?

**Kyle Doherty:** Yeah.

**Kyle Doherty:** And it'll say, you can be like, how many say event influence creation or event closed one, event influence closed one.

**Kyle Doherty:** So, but you can also create a report for that too.

**Jesus Yepez:** Yeah.

**Kyle Doherty:** Jesus, just because Jason asked about this.

**Kyle Doherty:** So, for Luma, all the people that are in Luma, this segment right here is all the people that I've registered for a Luma event.

**Kyle Doherty:** need to change how this is in, because it's not following my pattern.

**Kyle Doherty:** So, it's all the contacts registered for a Luma event, and honestly, you don't need that last part.

**Kyle Doherty:** It's just detail that no one cares about.

**Gloria Willis:** So, it's just like, we know they had a most recent Luma event.

**Kyle Doherty:** Um, because like, there's a zap that this guy, Joe, who was here before me, set up that just like, if you're in, if you're in Luma, we sync you to HubSpot.

**Kyle Doherty:** So you have 5,500 in here.

**Kyle Doherty:** So, yeah.

**Kyle Doherty:** Great.

**Kyle Doherty:** Got it.

**Kyle Doherty:** Got it.

**Kyle Doherty:** Got it.

**Kyle Doherty:** Um, there's the other ones that he wanted where it's like, okay, who are the people that are in Circle?

**Kyle Doherty:** So AIG and who are the people that are in Beehive?

**Kyle Doherty:** But I don't think Ed has set up, he might have, but I don't think he's set up zaps that like, he did, I know he pushed people to Beehive.

**Gloria Willis:** Um, from, from HubSpot, I think, but I don't think he, I don't think it's gone the other way.

**Gloria Willis:** But I don't know what the use case is for that.

**Gloria Willis:** So I would confirm there is a use case before like doing anything.

**Gloria Willis:** Obviously, Gloria, you have a use case for who's in Circle.

**Gloria Willis:** Yeah, I'm not sure that the,

**Gloria Willis:** The newsletter, because basically everybody's on the newsletter is the Luma list.

**Gloria Willis:** So yeah, that's true.

**Kyle Doherty:** That's what it was.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** So it's the same thing.

**Gloria Willis:** Well, I guess it's like, and some other people, but I mean, I don't know what you do with those people.

**Gloria Willis:** Like all the, all the stuff they're getting is coming from Beehive and they're not subscribed to any marketing stuff.

**Gloria Willis:** So the only, the only way it could be handy is if there's people that are in subscribed to the newsletter that we potentially would want to hit with one-to-one emails, like have understory go after them.
