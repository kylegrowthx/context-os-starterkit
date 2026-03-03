# Webstacks<>GrowthX Weekly Sync

<metadata>
date: 2025-09-11
time: 16:31 UTC
duration: 39 minutes
organizer: jessalynn@growthx.ai
participants: Jessalynn Jones (GrowthX), Jakub Rudnik (GrowthX), Jesse Schor (Webstacks)
fathom_recording_id: 86645289
fathom_url: https://fathom.video/calls/407132494
share_url: https://fathom.video/share/hx2qCmdMGdTZrP2z9EPGygscypJ5hfhT
source: fathom
enriched_on: 2026-03-03 20:15 UTC
</metadata>

---

## Summary

Webstacks and GrowthX finalized a HubSpot workflow to export blog lead data including first page seen, lifecycle stage, and lead score to Google Sheets — enabling the team to measure direct ROI from pillar content and understand which blogs drive qualified leads. As pillar and sub-pillar content pieces near completion (end of this week or early next), the team agreed to first assess performance before deciding whether to pursue spoke content, refresh existing blogs, or experiment with TLDR/FAQ-style content additions to improve user experience and AI overview optimization. Jesse committed to testing the workflow with a private browser flow, Jessalynn to coordinate data layering with the reporting team, and Jakub to review early results and design TLDR/FAQ experiments.

---

## Context

Webstacks is a GrowthX content marketing client working on SEO and organic lead generation for their blog. GrowthX has been executing a pillar-and-spoke content strategy with Webstacks, producing deep-dive content on major topics alongside sub-pillar pieces. This meeting is part of their weekly check-in cadence where the teams align on campaign progress, technical implementation, and strategic priorities. Jessalynn Jones leads GrowthX's content strategy work with the client, while Jakub Rudnik directs content performance analysis and experimentation. Jesse Schor is Webstacks' lead stakeholder managing HubSpot workflows and data infrastructure.

---

## Relevance

**To GrowthX Delivery:**
- Established data pipeline showing direct lead attribution from blog content, enabling better ROI measurement for content-driven engagements
- TLDR/FAQ experiment represents scalable content optimization pattern that can be applied across multiple client accounts
- Structured data for blog content becoming core technical deliverable alongside editorial work
- Webstacks client maturity demonstrated: already measuring pipeline impact and lifecycle stage progression

**To CheckThat (AI Visibility):**
- TLDR and FAQ sections designed to improve AI overview citations and featured snippet positioning — direct application of CheckThat insights
- Content experimentation focus on how LLM chunking and direct answers affect organic visibility metrics
- Client explicitly considering AI discoverability in content strategy decisions (using TLDR as pseudo table of contents for LLM consumption)

**To GrowthX Business Development:**
- Webstacks is a high-maturity, well-organized client tracking multi-touch attribution across blog touches and deal progression
- Account expansion opportunity: HubSpot data infrastructure work and CMS module development indicate scope expansion potential
- Client requesting recommendations on structured data implementation — signals openness to advisory services beyond content execution

---

## Overview

- HubSpot workflow set up to export lead data, including first page seen, lifecycle stage, and lead score
- Content team wrapping up pillar and sub-pillar pieces; discussing next steps (spokes vs. refreshes)
- Exploring TLDR/FAQ-style content additions to improve user experience and SEO performance
- Planning to implement structured data for better content organization and search visibility

---

## Key Topics

### HubSpot Automation for Lead Export

  - Created workflow to export lead data to Google Sheets
  - Included fields: contact ID, company ID, create date, first page seen, lifecycle stage, lead score
  - Broadened criteria to capture all blog visits (not just GrowthX blogs) for comprehensive analysis
  - Added "date added" field to differentiate between contact creation and conversion dates
  - Jesse to test the workflow and ensure data exports correctly

### Content Strategy Progress and Next Steps

  - Pillar and sub-pillar pieces nearly complete (finishing this week or early next)
  - Considering options for next content focus:
    1.  Develop spoke content based on pillar performance
    2.  Refresh existing blog content
    3.  Implement TLDR/FAQ-style additions to improve user experience and SEO

### TLDR/FAQ Content Experiment

  - Proposed adding summary sections at the top of longer blog posts
  - Benefits: Improves user experience, potentially boosts SEO performance
  - Jakub to design experiment testing TLDR and FAQ formats on select pages
  - Team to research examples and best practices for implementation

### Reporting and Analytics

  - New HubSpot export will provide more comprehensive data on blog performance
  - Team to analyze early results from published pillar content
  - Reporting team to set up filtering for various metrics (e.g., first page seen vs. page visited, GrowthX-specific vs. all blog conversions)

---

## Action Items

**Jesse Schor (Webstacks)**
- Test HubSpot workflow export to Google Sheet (run private browser test, check data accuracy)

**Jessalynn Jones (GrowthX)**
- Contact reporting team re: filtering blog conversion data (first page seen vs page visited, GrowthX-specific, data layering)
- Research/share recommendations on structured data for TLDR sections
- Prepare early learnings report from published pillar content for next week's meeting

**Jakub Rudnik (GrowthX)**
- Review pillar content early results, share in team channel
- Design TLDR/FAQ experiments for pillar content, select test pages
- Prepare early learnings report from published pillar content for next week's meeting

---

## Transcript
**Jessalynn Jones:** Good morning to you.

**Jakub Rudnik:** Good morning to you.

**Jessalynn Jones:** What's up, guys?

**Jesse Schor:** Good morning.

**Jessalynn Jones:** It's just going to be us today.

**Jessalynn Jones:** Rachel's out for a little bit this morning.

**Jessalynn Jones:** I just saw your message about testing the HubSpot automation for the export.

**Jessalynn Jones:** Thanks for setting that up.

**Jessalynn Jones:** I'm trying to log into our instance of HubSpot really quick right now.

**Jessalynn Jones:** How's the week going?

**Jesse Schor:** Pretty crazy to be honest.

**Jessalynn Jones:** But good.

**Jesse Schor:** We're seeing some trends, I guess you could say.

**Jesse Schor:** Just like everyone's in budget planning mode or trying to get something launched last minute to exhaust budget, which like we typically kind of tend to see around like Q4, but it's been good.

**Jessalynn Jones:** It's a good hectic, at least.

**Jesse Schor:** Just, I wouldn't say we're the most like buttoned up when it comes to our CRM cleanliness.

**Jesse Schor:** So it's a lot of like jumping into things and then it's like, where are we at with these guys?

**Jessalynn Jones:** Yeah, I feel like that's always, always a challenge.

**Jessalynn Jones:** Like every organization that I've been a part of, I feel like there's always CRM issues.

**Jessalynn Jones:** With it just not being maintained, and then it doesn't become a priority until it's a problem, and then you're trying to hectically get things together.

**Jesse Schor:** Yeah, it's just not feasible. I mean, unless you have someone dedicated to all that, but even then, it only makes sense when you have enough people using it to really have process.

**Jessalynn Jones:** Yeah, that makes sense.

**Jessalynn Jones:** For the HubSpot workflow, do you want to walk through it, or do you want me to pull it up on my screen?

**Jesse Schor:** I can walk through it if you want. It's pretty straightforward. The only thing I'm curious about is, one, I want to make sure I have the list membership correct, or if there's another list. And then the date field is the only other thing that I'm not totally sure about, because I believe that HubSpot brings it over in kind of the universal time, and then we'll need to convert it on the sheet.

**Jesse Schor:** Now, it doesn't look like there's any formula you guys are using, so I assume that there's some transformation that your team has set up to put the proper date in. So I don't want to edit the formula or edit the sheet without talking to you guys, but we can add a formula to auto-convert.

**Jessalynn Jones:** Yeah, so when I was talking to our reporting team, they made it sound like basically if we can just export raw data, they'll transform it in how they need to for the reporting.

**Jessalynn Jones:** So however it comes out of HubSpot is fine. And then we can either set up formulas in the sheet to transform it into a format that they want, or they can do that when they actually hook it up to our Looker dashboard.

**Jesse Schor:** Okay, so should we create a new tab in the sheet then that like I can just dump all of the data into? Because right now I kind of just have it lined up to like the lead sheet.

**Jesse Schor:** I can add a new one and then we can also include like additional data if that's helpful. So if we want to include like lifecycle stage or even like lead fit, those might be good things to track, because right now we're kind of just getting it from that initial conversion, which is good, but then you guys don't see like, okay, does that then become anything to impact our pipeline? So like if it becomes an opportunity, we can always adjust that.

**Jessalynn Jones:** Yeah, that would be really helpful just seeing like not only what's resonating, but what's resonating with the right people. Okay, so let's say I can edit this.

**Jesse Schor:** Oh, perfect. I see the tab. And I don't have permissions to view this.

**Jessalynn Jones:** I just tried opening it up and it said that I don't have permission. So I don't necessarily need permissions for it if you're going to set it up for us, but I wasn't able to view it.

**Jesse Schor:** Is there anything other than lifecycle stage that we would want?

**Jessalynn Jones:** Great — date, first page seen, lifecycle stage.

**Jessalynn Jones:** You said that you guys have, like, what's the word I'm looking for? Not lead ranking, but like lead scoring. You have that set up? I think lead score would be helpful.

**Jesse Schor:** Is there anything else, Jakub, that you think that we should include?

**Jakub Rudnik:** I think the lead score especially is a good addition that I didn't have initially penciled in, but if that's easy. The first page, for sure, that's important to me.

**Jakub Rudnik:** That gives us more — it takes the report much further than we have already. We can see macro level data, and then we can see the pages in a table, kind of like what we've done manually so far.

**Jessalynn Jones:** Yeah, the only other thought that I had is, and I don't know how built out you guys already have this in HubSpot or how easy it is to do, but just trying to see it all the way through the pipeline — if we have any conversion value on leads too, so then we can see like direct ROI on any of the blog conversions.

**Jesse Schor:** We would need to get deal info for that. Like anything the contacts associated with — it's not at the contact level.

**Jessalynn Jones:** So if that's not easy, I don't think it's a big deal, but it's just like taking it the next step to kind of see it go all the way through the pipeline.

**Jesse Schor:** Lifecycle stage can be a good gauge for that because then we'll see when someone becomes an opportunity, and that can be a flag for how much that deal is. I think what we can probably do is put in a request with your team — they probably have more expertise on how to join and bring together the data. But what we could maybe do is have a separate sheet for the deals that are coming in and relate it to any of the contacts that have met the criteria for this workflow, and then they can join that data up.

**Jessalynn Jones:** I think if we're going to do that, then we'll probably need a little bit more contact data in the import so they can filter deals by that or match them based on that. Contact ID and company data — I don't think we necessarily need the contact information, but I think the company data we would need so they can tie that to deals that are tied to the company.

**Jesse Schor:** Yeah, I think we can do contact ID and company ID. I guess we could do deal ID, but either way, you guys will need a separate sheet and I can send that data to it with the deal ID. We can just start with contact ID and company ID and go from there.

**Jessalynn Jones:** I wonder if we can even just add another tab here with a deal import.

**Jesse Schor:** I'm just not sure how to best join that up. Anyone that goes through this workflow is a contact at the contact level, but all the deal stage data that would help us see if this turned into pipeline and if that pipeline converted comes from the deal object. When a contact goes through this, it only reads if there are deals associated to the contact. So I think we'll probably need a separate workflow that sends to the same sheet, but with deal info. I'll have to figure out in HubSpot how to best segment that — it'll just be like if they have an associated contact that went through that workflow.

**Jessalynn Jones:** I'm trying to remember from setting up workflows in HubSpot — if you can filter the export based on first page seen or something like that. Is that almost similar to how you're doing the lead import, but just from the deal record instead?

**Jesse Schor:** No, we can filter deals through here as well, but it's going to be at the deal level — the deal name. And then any activity associated with that contact is on the contact record. First page seen doesn't exist as a property on a deal. If we have contact info with contact ID and company ID on a deal tab, then basically if they're part of this list, they're someone that's seen a GrowthX blog. And then based off the deals we have flowing in, we can match any contacts that have a contact ID associated with that deal. That's what we'll need your team's help with — dumping raw data and they'll clean it up, and they can join based on the match on contact ID between deals and contacts.

**Jessalynn Jones:** That makes sense.

**Jessalynn Jones:** When we're doing the lead export, I'm just wondering if it's valuable to include — we can segment it based on GrowthX-produced blogs and Webstacks-produced blogs, or just all blogs together. I wonder if there's value there, because then we can see blog health collectively, but also individually how the blogs we're producing are contributing. More holistically, how they're supporting general SEO efforts and organic traffic. We're interlinking to other blogs, and all the blogs we're producing contribute to domain authority. While it's helpful to look at individual blogs and which ones produce the most leads, looking at it holistically is also helpful. Could we do both GX blogs and just how the blog traffic is doing overall, with leads produced from all blogs holistically, and then filter down from there?

**Jesse Schor:** Yeah, I think we can probably do that if we change the criteria in the workflow.

**Jesse Schor:** To just be like — visited any blog page and converted by filling out a form. That'll give you everything.

**Jessalynn Jones:** Or even, we can do a first page seen if you want to look at it just through the scope of direct blog attribution, not even visited the blog. I don't know which one is more valuable for you to see.

**Jakub Rudnik:** I think the first touch is more relevant to whether the blog is a growth channel as an acquisition source — that's where I typically look.

**Jakub Rudnik:** There is value if they've touched a blog at all and which blogs are generating that. So there's value to both. I primarily go with first touch as the starting point, but the secondary is important too — especially with the efforts we were doing when Ada was on the account, with different landing pages and pushing people around the site. Did they touch any blog and what's their journey versus Jessalynn's point — are we winning SEO with blogs that are turning into customers? Different meaning for each.

**Jessalynn Jones:** First page seen versus page visited is the filter factor there.

**Jesse Schor:** Yeah, the only thing is we're omitting people. To Jakub's point, it does change what we're viewing. First page seen would be any net new contacts created from their first visit ever being a GrowthX blog — that's helpful from a discoverability and SEO standpoint. Page visit is helpful for anyone that exists and then sees one of our blogs and converts.

**Jesse Schor:** For example, if someone sees one of our ads and clicks on a landing page, their first page seen — even if they don't convert — is that landing page. If they search in Google, see our name, click on it, that won't show as their first page seen anymore. So if they convert after that, there's no credit to the blog. Maybe what we do is combine this into page visited and first page seen. Actually, we could just do page visited and include first page seen in the sheet, so we can match if first page seen is a GrowthX blog and create that segment. If the page visit was a GrowthX blog, we can also segment on that, even if first page seen is something else.

**Jessalynn Jones:** Just do the broader import and then filter down from there, basically.

**Jesse Schor:** I'd rather give you guys everything and then we can chop it up, as opposed to only partial data.

**Jakub Rudnik:** And to that point, Jesse, I would want all blogs — both from first page seen and from any touch of any blog — and then be able to filter for GrowthX blogs specifically. If we see what other pages are converting, there's value in knowing things we didn't create, why that might be working, and if we should send traffic to those blogs more specifically. There's a lot we can do with learning outside of what we've done, both on first touch and any touch. So I'd want any blog and then filter down to GrowthX specifically.

**Jesse Schor:** Okay, cool. Yeah, so this will basically give them visited the page and I'm going to add criteria. We can try this and see how the data looks. So basically, anyone that visits a blog and completes a form will go to the sheet. If they don't, it filters them out.

**Jessalynn Jones:** Sounds good.

**Jesse Schor:** I'll update this sheet to be the leads with first page seen and lifecycle stage. I'll run this starting today so we don't get flooded with everyone in our database. We can look back at this probably tomorrow and run tests ourselves — go in a private browser, view a blog page, fill out a form, and see how it comes through. If it's coming through as expected, we'll let this run and you can hand this off to your team.

**Jesse Schor:** Thanks so much for your help with this.

**Jessalynn Jones:** I'm excited to get a more holistic view of conversion value on things. I think it'll help with strategy too.

**Jakub Rudnik:** At this stage, I'm fully behind that. You're the furthest client we have stage-wise and we should definitely be looking at these pieces. We're well past early intent signals and just traffic growth. This is key to continuing to iterate and learn what works traffic-wise. Let's make sure we're getting more ROI out of everything we do.

**Jesse Schor:** It looks like I'm going to put email domain instead of company name, since that's kind of like a company record.

**Jessalynn Jones:** My only slight concern is that I know sometimes deal contacts have different domains than their primary domain. People sometimes put in alternative email addresses that don't match their company domain, so I'd worry that stuff would fall through the cracks. Can you export based on company ID like you do for the lead import? Can you do that for the deal import too?

**Jesse Schor:** It's not giving me that option.

**Jesse Schor:** HubSpot automatically associates based on email domain with a company — that's how they use it as the unique identifier. If someone's not matched, it's usually because they use a personal email, which is very rare. For us, we don't really have scenarios where someone completes a form with a personal email and converts to pipeline. It's usually they're signing up for the newsletter or just consuming our content.

**Jessalynn Jones:** Yeah.

**Jesse Schor:** I think this might suffice, but I could duplicate this for deals and see if I can get company ID from there as well. If not, we can just create another sheet for companies and do the same thing for deals, and then that's how we join all the data together.

**Jessalynn Jones:** For next steps, if you can double-check that it's coming through as intended, that would be great. Then I'll ping our reporting team to have them look at this and talk about filtering by the different values we discussed — first page seen versus page visited, holistic blog conversions, and GrowthX-specific conversions. I'll have them see what they can do in terms of data layering.

**Jesse Schor:** One other thing I just thought of for this, do we, on the sheet, you guys have create date.

**Jesse Schor:** Is that the contact's create date or is that the create date in this sheet?

**Jesse Schor:** That's the create date for the contact.

**Jessalynn Jones:** Okay.

**Jessalynn Jones:** Just because we are looking at like lead growth month over month for some of our reporting.

**Jessalynn Jones:** And so we're using that create date to figure that out.

**Jessalynn Jones:** Okay, cool.

**Jesse Schor:** We might want to include something like date at it to like make that the date of like today in those instances that I mentioned where like a contact exists and then converts.

**Jesse Schor:** And like I bring this up too because I just saw this the other day where like we had a contact that was created from one of our ads like a year ago, year and a half ago.

**Jesse Schor:** And we had...

**Jesse Schor:** Like outbound at them and, you know, they've been a part of other ad campaigns and email campaigns.

**Jesse Schor:** And then they like came back to our site from just like search and converted on our sales form.

**Jesse Schor:** So in like those instances, we, the create date might be like outdated, but the date that like they get added to the sheet would be, uh, in line with when they, they convert it.

**Jesse Schor:** Yeah.

**Jesse Schor:** It makes sense.

**Jessalynn Jones:** So like lead growth month over month, do you think it would be more accurate to look at that based on date added versus create date then?

**Jessalynn Jones:** Is that kind of what you're getting at?

**Jessalynn Jones:** Potentially.

**Jesse Schor:** We'll have to see how the data comes out.

**Jesse Schor:** I think like when we're looking at like net new contacts, probably, uh, when we're looking at things more holistically, we might be able to look at it just.

**Jesse Schor:** By create date, but that basically assumes that they were created from this action.

**Jesse Schor:** And so like, that's just something like we, we would just need to be cognizant about in any of the reporting.

**Jessalynn Jones:** Sure.

**Jessalynn Jones:** Makes sense.

**Jessalynn Jones:** That's a really good call.

**Jessalynn Jones:** Yeah.

**Jessalynn Jones:** All right.

**Jesse Schor:** So I'll save this and then I'll publish.

**Jessalynn Jones:** So I know we're kind of right up against time.

**Jessalynn Jones:** Just one last thing that wanted to run by you is so we are just about wrapping up with the pillar pieces and the sub pillar pieces.

**Jessalynn Jones:** We should be done with that.

**Jessalynn Jones:** think end of next week or end of this week or early next week, I think we'll have exhausted all the pillars and sub pillars.

**Jessalynn Jones:** So we wanted to touch base with you on like what direction you want to go next.

**Jessalynn Jones:** Do you want us to start digging into those spokes?

**Jessalynn Jones:** Do you want us to look at refresh opportunities on the blog?

**Jessalynn Jones:** Do you have thoughts about what you would like us to tackle next for content?

**Jesse Schor:** I think maybe it would be good for us to look at, I know it's super early, but if there are any takeaways we can see about the pillars that are being published, we could decide on the spokes to build out further. Let's see how the pillars are performing at least so far. I would anticipate the first one we published about three weeks ago is going to have more traffic than what we published this week, but that's to be expected. The other thing I thought about — Jakub brought up last time the FAQ-style data to add into blogs. I actually saw on Yahoo a really interesting way they're doing it. They basically had takeaways at the top that were bullet points — like TLDRs, you know those recipe blogs where the whole life story is there, and everyone wants to get to the recipe? So there was a TLDR section. For pillar posts especially, that could be an interesting way to satisfy AI overview content — direct bullet points of what you're about to read, almost like a pseudo table of contents. It's a briefing of each section, and then the full article begins. If you want to read the full article, it's there. If you just want the SparkNotes, that's at the very top.

**Jakub Rudnik:** We've seen it a few times. I think we have a couple of clients who have done it, though I'd have to double-check who and how. It's on my experiment board too — both FAQs and TLDRs because they serve similar purposes, but I'm not sure which is more effective. As for choosing the topics, I'll look at the pillars and early results tomorrow and send that over to the channel we all have. But for FAQs and TLDRs, I've been looking to implement a couple of these experiments across a few clients so we can get better data and feel good about it. Since you have interest, I think I can design what that would look like, pick some pages to run the experiment on, and put those in. I can take that on for both TLDR and FAQ, run those separately, and see how that impacts citations or impressions on a couple of cohorts of pages. This could be a good time to do it.

**Jesse Schor:** I'll try to find the example I saw on my phone, but yeah, I kind of thought about that right away. It doesn't have to be everywhere, but especially on beefier pillar-style blogs where there's a ton of content, it could be beneficial to have that TLDR.

**Jakub Rudnik:** It makes sense with the chunking that everyone believes in with LLMs and citations — it's similar to what you used to do for featured snippet optimization. It's just more direct and further up. And to your point, it's good for LLMs, but also good for the reader on a huge piece like that. I totally follow the logic. I'll find a couple of examples as well. If you have one, shoot one over. And Jessalynn, we can talk about how to actually implement that.

**Jessalynn Jones:** Can you just, as we're thinking about this, do you guys already have a module in your CMS to add a wrap-up at the top? Or is that something we should be generating?

**Jesse Schor:** We don't. It would just be a part of the rich text. That being said, if there's a better way to set this up using structured content or structured data like we talked about last time, let me know and we can do that. Do you guys have another pillar for next week?

**Jessalynn Jones:** Yes. I believe we're doing chapter six next week, and this week we're wrapping up chapter five.

**Jesse Schor:** So if between now and next week you guys can let me know if you find anything on that — articles or things that point to how we can best use structured data to set it up — I can work with the team to get that implemented. This time next week, we're trying to hit the ground running, and either way, that's going to be a good thing to have.

**Jessalynn Jones:** Kind of along the same lines, has your dev team been able to add that module for comparison charts in the CMS yet?

**Jesse Schor:** No, it'll probably be a minute to get designs and stuff. I thought that would be a lot easier than it has been.

**Jessalynn Jones:** Sounds good. Anything else you need from us?

**Jesse Schor:** No, I think we're good. I'll look out for those other pieces. If you guys can share some recommendations early next week, or if there are reports based off your dashboards with early learnings from what we publish, then I can come next week prepared to think through if we need to pivot into something different or we're ready to dive into the spokes.

**Jessalynn Jones:** Sounds good. All right, have a good rest of your day. Thanks.

**Jakub Rudnik:** You too. Bye.
