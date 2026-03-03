# Okta Weekly Syncs

<metadata>
date: 2025-09-03
time: 20:30 UTC
duration: 34 minutes
organizer: Kyle Gaudreau (GrowthX)
participants: Kyle Gaudreau (GrowthX), Sydney Arin Go (GrowthX), Erick Campos (Okta), Rachael Tiow (Okta)
fathom_recording_id: 84813158
fathom_url: https://fathom.video/calls/397830788
share_url: https://fathom.video/share/jwxGkUmR12RpxhQsn1abtrnZrbAQE15A
source: fathom
enriched_on: 2025-03-02 15:42 UTC
</metadata>

---

## Summary

GrowthX and Okta aligned on account enablement enhancements and data integration challenges during this weekly sync. Kyle and Sydney reviewed improvements to account briefs now featuring research sources and data collection logic, while Rachael outlined plans to integrate a login scraping tool and explore Common Room as a potential unified platform for insights across SDRs, AEs, and marketing teams. The team also discussed shifting GrowthX's role from building Okta's tiering system to providing consultative support, establishing baseline metrics to measure pipeline impact, and addressing a critical SLA gap where leads currently take 5.5 days to receive follow-up instead of the target 1 hour to 1 day.

---

## Context

Okta is a major enterprise software company (identity and access management), and GrowthX is providing growth strategy and demand generation support as part of a significant engagement. Rachael Tiow owns growth initiatives at Okta and serves as the primary point of contact; she's building a "growth operating engine" to support both field-driven acceleration and enterprise scalability. Kyle Gaudreau is the GrowthX lead on the account, with Sydney Arin Go supporting research and intelligence development, and Erick Campos contributing from Okta's side. This weekly sync is part of ongoing rhythm to review tactical progress on enablement, refine data integration approaches, and troubleshoot scaling challenges across Okta's large, complex go-to-market organization (with multiple regional teams, SDR groups, and marketing functions that need to coordinate).

---

## Relevance

**To GrowthX Delivery:**
- Shift from building Okta's tiering system to consultative/advisory role reduces scope creep and allows GrowthX to focus on enablement and insights delivery where they add most value
- Account brief quality improving with integrated research sources and data validation workflows — direct output of GrowthX's intelligence work
- Data structure challenges (Google Drive organization, Gem-per-account approach, Notebook LM automation scripts) indicate need for systematic platform thinking

**To CheckThat:**
- Okta exploring login scraping for authentication detection — potential synergy with CheckThat's signal-gathering capabilities for account intelligence
- Large enterprise signal aggregation problem (pipeline attribution across marketing, SDR, AE activity) is core CheckThat use case

**To GrowthX Business Development:**
- Account showing healthy expansion: moving beyond initial scope to platform/integration questions (Common Room, Upside tool evaluation, flow orchestration)
- Critical SLA issue (5.5 days vs. 1-hour target for form follow-up) signals operational pain that GrowthX could solve with automation/workflow design
- Americas SDR team underperformance vs. strong UKI team suggests room for targeted enablement or coaching
- Rachael actively building multi-team gem strategy (AEs, SDRs, marketing) — high dependency on GrowthX intelligence quality

---

## Overview

- Internal Okta team working on tiering system; GrowthX to provide consultative support
- Enablement docs now include research sources and logic for data collection
- Exploring Common Room as a potential wrapper for insights and data integration
- Focus on measuring impact: pipeline generation, event metrics, and reducing stalled opportunities

---

## Key Topics

### Enablement Documentation Updates

  - Account briefs now include summary and detailed intelligence with sources
  - Clay data incorporated and double-checked for accuracy
  - Potential integration of login scraping tool data for enhanced insights

### Tiering System Development

  - Internal Okta team working on comprehensive tiering system
  - GrowthX to shift focus to consultative role and problem-solving
  - Avoid duplicate efforts and conflicting systems for end-users

### Data Integration and Accessibility

  - Exploring Common Room as a potential wrapper for insights
  - Challenges with current data storage in Google Drive folders
  - Investigating scripts to update Notebook LM automatically
  - Considering one Gem per target account for SDRs and AEs

### Metrics and Measurement

  - Current SLA for lead follow-up (1 hour for form fills, 1 day for events) not being met (5.5 days average)
  - Focus on measuring pipeline generation, event metrics (signups, attendance, meetings booked)
  - Exploring integration with propensity to buy score to reduce stalled opportunities

### Cross-team Collaboration

  - Supporting AEs, SDRs, and marketing teams with insights and tools
  - Challenges in coordinating efforts across large organization
  - UKI team performing well, Americas SDR team facing challenges

---

## Action Items

**Rachael Tiow (Okta)**
- Connect Kyle with engineer who built login scraping tool; share doc if available
- Gather and share data on login scraping tool with Kyle; include logic used if possible
- Compile baseline metrics (opens, replies, meetings booked, pipeline from SDR output)
- Clean up account list in Clay; remove irrelevant accounts (e.g., RecSpace, adult toy retailers)

**Kyle Gaudreau (GrowthX)**
- Send info on Upside tool to Rachael; offer to connect her with Dan Amati if interested

**Sydney Arin Go (GrowthX)**
- Wait for Rachael's cleaned Clay list, then run new account briefs

---

## Transcript

**Rachael Tiow:** Okay, we're not here to talk about colors.

**Kyle Gaudreau:** Who else are we waiting for today? It's just going to be us on our end, so I think we're probably going to get started. Just shared the agenda. Let us know if there's anything outside of this on top of mind for y'all that we should cover. So I just wanted to cover some of the things we've worked on last week.

**Kyle Gaudreau:** Sydney has a variety of things we can catch up around — some of the enablement docs and spending some time thinking about the tiering system. Want to get some feedback on that. A few things to cover on the healthcare pipeline and Okta Artifact side of things. And Rachael, I want to make sure we have time to talk about your note yesterday about the flow you showed and the conversation around current state versus what we're trying to build towards in the future. Anything outside of that we should walk through?

**Rachael Tiow:** Looks good.

**Rachael Tiow:** Oh, one thing on the tiering thing, we can talk about it in a bit.

**Rachael Tiow:** There's an internal team that's looking at all these tiering, which makes me wonder, should we not do the tiering ourselves?

**Kyle Gaudreau:** I want to avoid duplicate efforts so that time can be spent elsewhere. My hunch is where we can probably be most useful is to trust your internal team's knowledge of the business.

**Kyle Gaudreau:** We can be consultative and help identify key problems you're running into as you're thinking about that work, and maybe there are areas we can step in. I don't want to create a confusing situation where there are different tiering systems for end users.

**Rachael Tiow:** My initial thought when the tiering was because I didn't know we were building something like that.

**Rachael Tiow:** The guy who's leading the project is currently out of office this week.

**Kyle Gaudreau:** So once he gets back next week, I'm going to sync with him and keep you posted. At this point, you just know there's something being worked on, but we're not yet sure of the details.

**Rachael Tiow:** Got it.

**Kyle Gaudreau:** Sydney, anything particular you want to cover on the enablement docs? Any questions or things to walk through?

**Sydney Arin Go:** Nothing major, but George and I went through them last week and found that we weren't actually sharing our research sources with you. So now all these docs have a two-part structure — the account briefs have a summary section, and the intelligence brief has the actual sources and the logic we used to pull all the data.

**Kyle Gaudreau:** I'm still not used to these tabs being here in Google Docs.

**Rachael Tiow:** I love it.

**Rachael Tiow:** Sydney, I've got a quick question: How much of the data we pull from Clay is incorporated into these briefs? I just wanted to know because I saw Azure AD noted on there.

**Sydney Arin Go:** Yeah, I incorporate all the data from Clay and then have our system double-check it to ensure we have consistent data. Sometimes there are conflicts. For example, there was one where Clay said they had a membership program.

**Sydney Arin Go:** But it turned out to be an affiliate program for a different website that happened to have the same name. I caught that manually and compared with Clay to understand where the disconnect happened. Clay had sources on there as well.

**Rachael Tiow:** I've connected with the strategic CSM on the Clay side, and we're refining a lot of the prompts to get more granular intel.

**Rachael Tiow:** Hopefully that will be more accurate than me pulling things manually. The second thing — we have an engineer who built a tool a couple of years ago to scrape login data, which tells us if they use a legacy setup or a homegrown setup. That tool has been pretty accurate, and if we can get the data, it enhances all the brief stuff we're putting together. I'll keep you posted on what I find.

**Kyle Gaudreau:** It could be interesting to understand the logic that was built into it. A scraper isn't complicated, so the key is understanding what signals they were looking for. We could take that and work it into our system. Best case is we figure out the logic and incorporate that into our work, which would be straightforward for our engineering team.

**Rachael Tiow:** So would it make more sense that I can connect you with the guy who built it?

**Kyle Gaudreau:** Yeah. Or if they have something they can pass along showing the signals they were looking for.

**Rachael Tiow:** I don't think it's complicated. You can easily update it asynchronously.

**Kyle Gaudreau:** I'm not opposed to talking live with them to save time.

**Rachael Tiow:** If there's a doc we can share, I'll get all that data and share it over.

**Rachael Tiow:** My mind is all over the place. I'm thinking about how we scrape all this data and have account briefs, but within each account folder like Estee Lauder, we also have cold calling guides and SDR resources.

**Kyle Gaudreau:** Yeah, cold outreach resources.

**Rachael Tiow:** So that's more like a prospecting resource?

**Kyle Gaudreau:** Correct. It's a combination — guidance for calling or emailing based on the context fed into the brief in different ways.

**Rachael Tiow:** Have you guys worked with Gemini much?

**Kyle Gaudreau:** Sort of. It's probably one of my least favorite LLMs. My understanding is that Gems are largely the same as Cloud Projects or ChatGPT Projects — you set instructions, feed files. Similar to custom GPT in some ways, depending on how the team uses it.

**Rachael Tiow:** We're testing different approaches to instructing Gems. One approach is making it a holistic outbound resource — I call it the SDR coach. Someone else created one purely for email, which is too limited since SDRs do more than send emails. I was thinking about copying your approach, but I can't because it's specific to Estee Lauder.

**Kyle Gaudreau:** That brings up something on my mind. We've been talking about this internally — there could be a path where we need enablement on how to use Gems and how not to use them, and what to watch out for.

**Rachael Tiow:** I'm catching up with Nick later this week.

**Kyle Gaudreau:** I want to understand how he's using it. I can see a path where it's helpful, but if you feed it all the briefs and information with certain prompting approaches, the individual briefs and insights start to lose their value.

**Rachael Tiow:** This brings up a bigger thing I've been thinking about.

**Rachael Tiow:** We've talked about having a wrapper where all this data lives — versus having it in Salesforce, which is too clunky. We're evaluating a tool called Common Room to surface all these insights, and I'm actively testing it to see if it works.

**Rachael Tiow:** I don't want to lose sight of what we initially agreed on — how do we build a growth operating engine within Okta that supports OddZero and Okta's business? Whether by industry or business segments. Right now we're doing a few things — looking long-term and tackling short-term issues. I want to make sure we don't lose sight of what angle we're chasing, because short-term tweaks may not lead where we want to be. How do we get to V1 first, then iterate? There will be gaps, but if it's 60-70% good, that's great because it supports them way better than other resources they have access to.

**Rachael Tiow:** The other thing — with all these documents you've created, I'm looking at building agents. I've suddenly become like a growth engineer, which isn't really my strength. Could I code agents since we don't use ChatGPT?

**Kyle Gaudreau:** Yeah, that would be great.

**Rachael Tiow:** I'm leveraging all the research you've put together to share with our marketing team. Our structure is: global campaign team dictates what runs for the year, global demand gen has event-in-a-box programs that are broad brushstroke, and regional/field teams address the exact pain of specific company clusters. I built a Gem for marketing to ideate based on these insights — it's been eye-opening and powerful for them. I'm supporting AEs, SDRs, and the marketing org across three teams. Everything sits in docs right now. Ideally, if we can pump everything into Common Room as a wrapper, that would be great. Common Room does a lot out-of-the-box, but many things we need are custom and bespoke to our business.

**Kyle Gaudreau:** I think as we zoom out, we should pick a set of challenges, metrics, or opportunities that we're particularly focused on. Then the experiments we run now and in the future should focus on that specifically. As you bring in other layers, it creates ambiguity. If we look at it from that lens across teams, it makes it easier to understand what we're experimenting on. For example, if our hypothesis is that the team is struggling to take the right industry-first approach across early stages of the buyer lifecycle, and that's hurting stage-two conversions — let's unpack that and run experiments to move the needle there. It's easier said than done, but the better we stick to that, the easier it is for us to not just be order takers but thought partners instead.

**Rachael Tiow:** No, I don't want you guys to be order takers. I want you to be my thought partners and business partners.

**Kyle Gaudreau:** I didn't think it was that way.

**Rachael Tiow:** Okay, so this is good.

**Rachael Tiow:** I've established baseline metrics. There are many experiments we can run, and I want to be cognizant we need proper onboarding pieces in place first. I'm measuring pre-growth engine and post-growth engine — we have inbound stats, and I'm scraping data for outbound and marketing programs. A few things we're looking to tackle: how do we leverage all these insights? During initial onboarding when we did OddZero for retail, we had OddZero artifacts and a generic OddZero retail artifacts.

**Rachael Tiow:** The signals I've shared are what I deem important, but there's more, and they differ by industry. I welcome you to challenge me because I'm learning from you too. When leads come inbound — they're hand raisers. Our SLA is: one hour for form fills and one day for event leads. For example, I met someone at Identivus, marketing enriches them, and we have one day to follow up. That's three days end-to-end. But I found our actual response time is 5.5 days — we're completely breaching our SLA. This is critical. I'm working on an automated process internally, but I also want to know: that flow you and Marcel talked about — where when leads come in, we scrape and enrich with signals and respond with personalized messages — how do we do that? Is it a tooling issue, or do I need to broaden the scope?

**Kyle Gaudreau:** Generally, we don't want to write to your CRM or marketing automation tools. Reading sometimes depends on the situation, but it introduces complexity. That's just not our world.

**Rachael Tiow:** We have experience doing these things, but that's not how GrowthX operates.

**Rachael Tiow:** No, that's fine. How do we plug in? Right now, a lot of our research and files sit in Google Drive folders, not in Salesforce.

**Kyle Gaudreau:** My thought on this — not necessarily the solve, but one idea: use your Clay table. Think about workflows around triggering events: is it a new lead, a target account, whatever the trigger is. How can we build something less dependent on asking Sydney to run accounts and create briefs, and more like a self-serve system where you run it yourselves and we help with setup and focus on other experiments?

**Kyle Gaudreau:** Set inputs in Clay — account names and relevant data — then we configure our endpoints into your Clay table. Inputs feed through and produce outputs back into Clay columns. That way, anytime you or Erick want to run accounts, you just do it without pinging Sydney each time. It's self-serve and programmatic. The remaining piece is where the briefs live. This doesn't solve that, but it at least gets data into Okta systems instead of just Google Drive folders.

**Rachael Tiow:** That's why I thought Common Room could be the wrapper. It becomes the UX where SDRs, AEs, managers, and demand gen folks can all access and stack-rank insights.

**Kyle Gaudreau:** I need to educate myself on that. Marcel is more familiar with Common Room than I am.

**Rachael Tiow:** I'd love the pros and cons of Common Room. Of all the tools I've looked at, it seems like the most effective wrapper. Outreach sucks, Salesforce is clunky, Sixth Sense doesn't work for us. We could build it ourselves, but that's not ideal. I didn't mean to derail us, but do we need to map out priorities and do a V1 even without the perfect wrapper? Let's work with what we have.

**Rachael Tiow:** I already have access to Common Room and they're setting up an instance for us to see what it looks like when we pump signals in.

**Kyle Gaudreau:** Yeah, like if we pump signals in here, what does it look like?

**Rachael Tiow:** Interestingly, our Common Room isn't plugged into Salesforce yet — it has a connector we can enable. The team that initially bought Common Room did it for the community developer org, not for revenue. I'm testing this for the revenue side.

**Kyle Gaudreau:** This is a good example of where I've been hesitant about expanding scope. Not that we can't do things in parallel, but we need to focus on this specific experiment first. There are still a few pieces — how we're measuring it, how we understand if it's working, how we're adapting. We're getting momentum but stuck on some critical pieces. It's less a capacity issue and more a focus issue. We feel better about the briefs, and there are things we can still adapt. The key question is: how do we make it more self-serve and repeatable for you?

**Rachael Tiow:** And where does that data live? I found some scripts that could help.

**Rachael Tiow:** There are scripts we can write to automatically update Notebook LM. You mentioned before that combining 10 accounts into one Gem doesn't provide accurate data. The UKI team manager suggested having each rep create one Gem per target account. That's perfect because the data sits in a folder, readable by SDRs and AEs but not writable. We write a script to update Notebook LM by industry so marketers can search and research. They can also upload those docs into their own Gems, as can SDRs. That streamlines access to the data.

**Rachael Tiow:** At our company size, there are so many people doing everything and nothing simultaneously. A critical thing I'm trying to figure out is tracking opens, replies, meetings booked, and pipeline from SDR output. Those seem straightforward.

**Kyle Gaudreau:** We can get that data.

**Rachael Tiow:** The area where I want to measure lift is when the commercial team uses this research for retail accounts and runs their own events — direct mail, executive briefings, etc. I want to see how using this data increases signups, attendance, meetings booked, and pipeline influence. The ultimate metric is pipeline. Felix is building a propensity-to-buy score for stage-four opportunities, which have about 50% close probability. If we pair that with our insights, we'll see a reduction in opportunities stalling in stage two.

**Kyle Gaudreau:** Someone we know and partner with is Dan Amati, co-founder of Upside. He's a legit operator. He walked me through a demo a month ago. It basically solves what you're describing — taking all these different signals and understanding what drove pipeline creation and what happened afterward. That's what their tool does. I'll send you info and can connect you with them. Full transparency: I haven't used it myself yet, so I can't vouch for the tech. But knowing his background, the vision and product are credible. I can't say if it's ready for your use case, but it's worth exploring.

**Rachael Tiow:** Got it. We're at time and I have a pipeline review call.

**Rachael Tiow:** So what are our next steps? I'll get the baseline metrics, and then we can start measuring as SDRs kick off. I'm syncing with the AVP of Americas SDRs — the Americas team has been challenging to manage, whereas the UKI team has been phenomenal.

**Kyle Gaudreau:** Yeah, for sure. We saw messages about additional accounts to run. We'll do that.

**Rachael Tiow:** One thing — when we went through the Clay account list today, we found accounts that shouldn't be there. RecSpace, a tech company, appeared on the retail list. Some adult toy retailers also got picked. We need to clean up the list tomorrow, then run the account briefs. I appreciate you guys very much, Kyle. If I may ask one thing: speak plainly. If you have concerns, please speak openly with me. I'm strong-willed and stubborn at times, but that shouldn't discourage honest feedback.

**Kyle Gaudreau:** No worries at all. I appreciate it. Well, good catching up. We'll chat again soon.

**Rachael Tiow:** Thank you. Bye.

**Sydney Arin Go:** Thank you.
