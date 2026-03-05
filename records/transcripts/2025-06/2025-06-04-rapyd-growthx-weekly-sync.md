# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-06-04
time: 17:30 UTC
duration: 35 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Jakub Rudnik, Rachel Pasche, Darrell Etherington, Kristin Reischel, Mark Stiltner, Francine Harris
fathom_recording_id: 66494575
fathom_url: https://fathom.video/calls/316800260
share_url: https://fathom.video/share/_f4PFqPKHyQFyV8CFMkxh4dAKpysX7i8
source: fathom
enriched_on: 2026-03-03 15:42 UTC
</metadata>

---

## Summary

Rapyd and GrowthX aligned on internal staffing changes, refined XML import workflows, and reviewed early content performance metrics. Aida is transitioning to GrowthX's onboarding team, with Jesselyn taking over as Rapyd's managing editor, while Rachel continues supporting the account. The teams discussed blog post workflow improvements, Airtable access permissions, and launched Looker reporting for content performance tracking—confirming 18 published blog posts with measurable SERP rankings and LLM visibility gains, plus planning for data filtering and A/B testing on blog length and format.

---

## Context

Rapyd is a GrowthX B2B content marketing engagement focused on international payment solutions and financial services. This was a weekly operational sync between Rapyd's content team (led by Mark Stiltner on delivery) and GrowthX's team (Aida managing the account, Jakub overseeing, Rachel on editorial execution). The call covered routine updates—staffing transitions within GrowthX, workflow improvements for the XML-to-publish pipeline—alongside substantive discussions about content performance and analytics infrastructure. The relationship is maturing past initial launch: the blog is now generating measurable organic search visibility and LLM referral traffic, prompting both teams to invest in better data visibility and experimentation frameworks.

---

## Relevance

### To GrowthX Delivery

- **Account transition risk mitigated**: Aida's move to onboarding was positioned as a positive (bringing her 6-week-old ME promotion expertise to new client onboarding), with structured handoff to Jesselyn starting next week. Rachel's continuity on execution reduces disruption risk.
- **Blog workflow optimized**: Agreed on weekly XML batch upload process via shared drive, eliminating manual per-post coordination. Mark to notify when developers finish XML integration setup.
- **Airtable cost/access constraint identified**: Adding editors incurs per-license costs; team exploring read-only viewer access + comment tagging workaround to allow Rapyd reviewers into Airtable without license escalation.
- **Content review loop clarified**: Mark will follow up with Kristin on best practices for assigning and tracking blog reviews across teams, using Airtable directly or Monday.com as backup.

### To CheckThat / AEO

- **LLM traffic visibility confirmed**: Rapyd blog now driving measurable LLM referral traffic; Looker report shows LLM Referral Traffic Summary page tracking by source. Currently 54 clicks/week from LLMs (still smaller than organic, but impressions higher in LLMs per Jakub).
- **Content-to-LLM correlation being studied**: Swift Alternative blog post now has featured snippet in UK Google search; Telegraphic Transfer vs Wire Transfer article appearing in AI Overviews. Team recognizing pattern: as organic visibility increases, LLM mentions follow, but with different dynamics than organic clicks.
- **Blog isolation for metrics**: Aida will create separate Looker tables with data filters to isolate /blog traffic from whole-site LLM metrics, plus individual URL tracking—three-view funnel (whole site, blog, individual posts) to understand content impact.

### To GrowthX Business Development

- **Account health positive**: 18 blog posts published in ~3 weeks, on track for ~18/week. Early SERP rankings and featured snippets confirm content quality. Kristin's team capacity (3 reviewers) now bottleneck; Mark is managing scannability/length feedback to avoid mid-cycle pivots.
- **Data-driven optimization planning**: Team deferring format/length changes until 6+ weeks of baseline data. Mark planning A/B tests on CTA placement, button wording, post length once sufficient traffic established. Engagement rate in GA4 being tracked as proxy metric.
- **Visual content gap identified**: Aida highlighted SEMrush finding that top-ranking content includes images throughout body copy. Rapyd team considering adding visual breaks (screenshots, images) to high-performing posts in enrichment phase.

---

## Overview

- **Team transition**: Aida moving to client onboarding; Jesselyn (former colleague with journalism background) taking over as managing editor; Rachel staying for continuity
- **XML workflow**: Weekly batch upload process agreed—.xml files with post tags placed in shared drive after each call, then imported and moved to published folder
- **Performance wins**: Swift Alternative post now has UK Google featured snippet; Telegraph Transfer vs Wire Transfer in AI Overviews; overall keyword visibility up 0.66%
- **Analytics infrastructure**: Looker report now available with Google Search Console, GA4, and LLM Referral Traffic data; planning to add blog-specific filters and individual URL views
- **Content optimization deferred**: Team gathering 6+ weeks baseline data before testing shorter posts, more bullet points, or different CTAs; engagement rate in GA4 is proxy metric
- **Airtable access**: Exploring read-only viewer permissions for Rapyd reviewers (tagging Aida/Rachel to mark "reviewed") to avoid Airtable editor license costs

---

## Key Topics

### Team Changes and Workflow Updates

- Aida transitioning to onboarding team role; Jesselyn (former colleague from content agency with journalism background) taking over as managing editor
- Rachel remaining on the account for continuity and document tagging
- Airtable access discussion: Rapyd team wants read-only viewer access to pick posts for review directly; Aida to check with Kyle on permissions; considering workaround where reviewers tag Rachel in comments to mark "ready for review," Rachel then marks as "reviewed"
- XML file process being refined:
  - Weekly batch uploads of .xml files to shared drive (after weekly call, then imported by Rapyd developers)
  - Posts to be separated with `<post>` and `</post>` tags for clear delineation
  - Manual publishing to continue until XML setup is complete

### Content Performance and Metrics

  - 18 blog posts published to date
  - Seeing progress in views and SERP rankings
  - Swift Alternative blog post now has featured snippet in UK Google search
  - Telegraphic transfer vs wire transfer article appearing in AI overviews
  - Overall visibility for tracked keywords increased by 0.66%
  - Team has access to Looker report for performance tracking
  - Discussing potential for isolating blog traffic data in reports

### Content Strategy and Improvements

  - Team considering ways to improve blog post scannability
  - Discussing potential for shorter posts and more bullet points
  - Planning to gather more data before making significant format changes
  - Considering A/B testing for CTAs, post length, and format once baseline data is established
  - Engagement rate in GA4 being used as a metric for content performance
  - Importance of visual breaks and images in content highlighted

### CTA Implementation

  - Team agreed on Option 1 for CTAs
  - Implementation pending development support
  - Current process of integrating CTAs to continue until new system is ready

---

## Action Items

**Aida Knežević (GrowthX)**
- Check with Kyle regarding Airtable permissions for Rapyd team (read-only viewer access, not editor license)
- Create new Looker table for blog-specific data with data control filters to isolate blog traffic; include three views: whole site, /blog section, and individual GrowthX blog post URLs
- Post XML file format specs in team Slack channel (the post-tag syntax for batch uploads)

**Mark Stiltner (Rapyd)**
- Follow up with Kristin regarding best practices for blog content project management and team capacity planning

---

## Transcript
**Darrell Etherington:** I have another one, but it's with Matthew and Megan.

**Darrell Etherington:** It's just workflow improvement stuff we're trying to do.

**Darrell Etherington:** Yeah, it's good, fun.

**Aida Knežević:** Yeah, I know that there was a workflow update last week, but I was out on vacation.

**Aida Knežević:** So it really get up to speed with the changes, but I guess I updated it again today.

**Aida Knežević:** Yes, he did, which is funny.

**Darrell Etherington:** This is separate from that.

**Darrell Etherington:** This is more about leaving aside the engineering pieces.

**Darrell Etherington:** Can we change the best practices on just the stuff that we have control over on the content creation side?

**Darrell Etherington:** But, yeah, we're thinking a lot about working with Kirkland, too, pretty closely.

**Darrell Etherington:** That's cool.

**Aida Knežević:** Yeah.

**Jakub Rudnik:** Rachel, is your wilderness adventure?

**Jakub Rudnik:** Great word, honey.

**Jakub Rudnik:** it.

**Jakub Rudnik:** Thanks.

**Jakub Rudnik:** Alright.

**Jakub Rudnik:** Cool, actually.

**Rachel Pasche:** They had one section that was just like juvenile bears—I'll send a video afterwards. It was a bunch of bears fighting because they were all so young and playful. There was like a big water thing and they were all just having a melee in there.

**Rachel Pasche:** It was so cool.

**Jakub Rudnik:** Rachel, what did you go to this week? Will you explain it, just for context?

**Rachel Pasche:** Yeah, there's like a wildlife park near where I live in Arizona with free-ranging wolves, bears, and bison, and there were jaguars too. You drive through the park and they're free-range. We had one section with juvenile bears just fighting all around, and you have to stop your car because of the bear fights. It was crazy.

**Rachel Pasche:** It's like the next Yellowstone or something.

**Jakub Rudnik:** That's really cool.

**Kristin Reischel:** Nice.

**Aida Knežević:** Okay.

**Aida Knežević:** So, yeah, before we jump into, like, our regular meeting stuff, I just wanted to update you really quickly on some internal changes that we have going on.

**Aida Knežević:** So, in the next couple of weeks, I'm going to be transitioning to kind of a different role with the onboarding team for new clients.

**Aida Knežević:** And that means that...

**Mark Stiltner:** Thanks for that.

**Mark Stiltner:** yeah.

**Aida Knežević:** Someone else, a new managing editor is going to come like step in my role.

**Mark Stiltner:** Her name is Jesselyn.

**Aida Knežević:** She is actually, me and her, we used to work together at a different content agency.

**Aida Knežević:** We're there for over a year.

**Aida Knežević:** So we're kind of cut from the same cloth.

**Aida Knežević:** Like we, but she has also a background in journalism.

**Aida Knežević:** So I know she's going to be a great fit for the account and you're going to be in good hands with her.

**Aida Knežević:** It's not going to be an abrupt handoff.

**Aida Knežević:** So she's probably going to join the meeting next week.

**Aida Knežević:** And then like, I'll continue like working with her to make sure that she has like all the contacts that she needs on the account.

**Aida Knežević:** But most importantly, Rachel is still going to be here.

**Mark Stiltner:** So she's the one generating her account.

**Aida Knežević:** So that part isn't going to change.

**Mark Stiltner:** Could I just tag Rachel when things are ready for review or edits moving forward then?

**Mark Stiltner:** Good luck on your new role.

**Jakub Rudnik:** Aida was promoted to senior ME about six weeks ago and has done an awesome job. We're adapting how we do client onboarding—we've had great experience with Rapyd, but we want to be more focused. The leadership team decided to pull Aida and other folks in to form a SWAT team to nail client onboarding. It's a loss for this account, but we feel good about the team here and think we can keep moving forward well.

**Mark Stiltner:** Cool. Good luck on your new role.

**Aida Knežević:** Did you have anything else you want to cover today?

**Mark Stiltner:** I just wanted to give an update on what we're doing with the XML.

**Mark Stiltner:** Okay.

**Mark Stiltner:** For now, we're still working on importing that first set of four blog posts.

**Mark Stiltner:** So I've gone into the Airtable and just kept those labels as XML and changed all the other ones to publish back to my Web Manager to publish manually.

**Mark Stiltner:** We're going to keep publishing manually while we get the XML set up.

**Mark Stiltner:** From your end, I think the files look right, like what we're getting from you is correct.

**Mark Stiltner:** But I wanted to talk through the process of how we receive it.

**Mark Stiltner:** So I was talking to the team today, and what they were hoping that we could do is just set up, like, a Google Drive or some kind of shared drive.

**Mark Stiltner:** doesn't matter with what.

**Mark Stiltner:** And then maybe at the end of every week or on a set day, maybe after this call, a .xml file, so not a Word doc or a Google doc, but like a .xml file with all the blog posts in that batch.

**Mark Stiltner:** We just drop in there as one file.

**Mark Stiltner:** They'll grab it, import from there, move it into like a published folder in that drive, and we'll just do that.

**Mark Stiltner:** We'll just have a drive that we put everything in.

**Mark Stiltner:** That'll be a good way to keep track of it.

**Mark Stiltner:** And then they ask that we do like, you know, all the posts, like Fathom, all the posts we're going to do in one .xml file, and to separate things with post tags, just so that we know where one post in and one post begins.

**Mark Stiltner:** That'll make sense to whoever's outporting the .xml.

**Mark Stiltner:** I just put a note in the chat what that means.

**Mark Stiltner:** It basically just means you like tag it with post at the top of the post, and then tag it with slash post at the bottom of the post, and yeah, super cool.

**Mark Stiltner:** Jerry, you're shaking your head like, you know what I'm talking about.

**Mark Stiltner:** I'm just paring with the developers.

**Darrell Etherington:** It makes a lot of sense.

**Darrell Etherington:** It should be far more efficient, but yeah, great.

**Aida Knežević:** Face it in the channel, just so we don't forget.

**Mark Stiltner:** Yeah, I threw it there, and then I will basically, we'll just keep cranking on like regular posting until we have everything sorted, and then I'll just tell you, okay, start giving it to me as the XML files.

**Mark Stiltner:** Okay.

**Mark Stiltner:** Okay.

**Mark Stiltner:** So that was that.

**Mark Stiltner:** Yeah, Kristin, while I've got you on here for your team, the posts from Sujata were super helpful.

**Mark Stiltner:** I moved those into reviewed so that they can move on to the next phase.

**Mark Stiltner:** I just wanted to make sure, and maybe I wanted to make sure that your team would have access to Airtable, because ideally, if your team is reviewing, you know, X number of posts a week or whatever, I don't think we need to just like manually assign them posting.

**Mark Stiltner:** I don't need do

**Mark Stiltner:** Send them to it.

**Mark Stiltner:** think we could just say everybody who's reviewing posts could go into the Airtable, pick a post, you know, put a little note in there saying that they're reviewing it, and just review it and mark it as reviewed once it's done.

**Mark Stiltner:** So I think it'd be easy if we could get everybody into Airtable.

**Mark Stiltner:** I wanted to make sure you were okay with that.

**Aida Knežević:** Jacob, I know that there was discussion with Kyle about editors for Airtable.

**Aida Knežević:** So I think we'll look into, so when we add someone as an editor, it incurs, like, additional costs.

**Aida Knežević:** And if we have too many editors, then, like, those costs add up very, very quickly, just to be fully transparent with you.

**Aida Knežević:** So I think if we add them, like, with permissions that aren't as extensive, then we can, like, avoid that.

**Aida Knežević:** But I have to check with Kyle first.

**Kristin Reischel:** I think we set up our own process in Monday, so we can use that. You just have to assign articles to us.

**Mark Stiltner:** The problem with that is we have to go in here, pick an article, assign it, put it into Monday, have them do it there, put it back here. I was hoping we could just get everybody to go into Airtable, look at blogs ready for review, grab one, review it, mark it as reviewed.

**Mark Stiltner:** Aida, they don't actually need to be an editor in Airtable. They just need to be able to click a link and open the doc.

**Aida Knežević:** That's the permission they need. I'm sure we can make that work. I just want to double check with Kyle first.

**Mark Stiltner:** If you're not able to do that, then we can use Monday instead. Kristin, you and I can circle back.

**Jakub Rudnik:** If you add them as read-only, they would need to tag whoever is reviewing—Aida or Rachel—to mark it as reviewed.

**Mark Stiltner:** Yes, that's the workaround. They'd tag Rachel, she marks it reviewed.

**Mark Stiltner:** Ideally, everybody gets signed up to review a few blogs per week. They can grab one, review it, mark it as reviewed. If they can't make changes, it could get confusing. I could add a comment saying "Mark's reviewing this," but that incurs cost.

**Jakub Rudnik:** Adding editors means issuing new Airtable licenses. We've found people use them once and forget. But the easiest workaround is just using comments in the doc—people tag Rachel when done, and she marks it reviewed.

**Mark Stiltner:** That's what I'll do with my team. Each member reviews three blogs a week. They can grab one, pick another, go. Kristin, you and I can circle back on this.

**Aida Knežević:** Like in rankings and in clicks, one thing, I believe that all of you are editors of this Looker report.

**Aida Knežević:** So in case you want to, for example, see month over month growth and traffic changes, yeah, you can do that.

**Aida Knežević:** So you can just click edit and you'll be able to do that on your own.

**Aida Knežević:** If you are unfamiliar with Looker, I can show you how.

**Jakub Rudnik:** Same. We have a member on our team who built these reports. The report works pretty well and doesn't require changing data sources.

**Aida Knežević:** You can bookmark this. The chart doesn't update automatically—you have to adjust the date each time you log in. Everything else is automatic. How many blogs are published now?

**Mark Stiltner:** That's 18 blogs. We're seeing progress in views and SERP rankings. We need more traffic data, but at this pace—if Kristin has Sujata and Corral, and I have Nicolette and Vanessa, that's three reviewers each at 18 blogs a week total—we could accomplish in a week what we've done so far.

**Kristin Reischel:** Okay, yeah, yeah, we can talk about that, Mark, for sure.

**Kristin Reischel:** Yeah, this is great.

**Aida Knežević:** This first page pulls Google Search Console data. The second page has GA4 data and Search Console queries. The last page is LLM Referral Traffic Summary showing which LLMs drive traffic—currently showing whole site. I can create a data control filter to isolate blog traffic if needed.

**Mark Stiltner:** Yes, I want to see it historically overall to see if our efforts are helping.

**Kristin Reischel:** I think it'd be worth isolating the blogs to see that impact.

**Aida Knežević:** We want to gauge blog post impact, which are optimized for Google search. We can see whether those strategies translate to LLMs and establish a link between organic search visibility and appearing in LLMs.

**Jakub Rudnik:** We've been tracking this—as we publish content, LLM traffic increases. With months three to six, we see enough LLM traffic that it's meaningful. Currently at 54 clicks per week from LLMs, though there are more impressions in LLMs than clicks. When we expand content footprint for topics, the homepage and educational content together drive LLM visibility. Tracking both whole site and blog-specific views is useful—LLM dynamics are different from organic.

**Mark Stiltner:** Can you set it up as a filter we can toggle between?

**Aida Knežević:** I can set up a new table with data control filters to add published blog posts. Easiest approach.

**Mark Stiltner:** Will it filter by URL or just /blog section?

**Jakub Rudnik:** I'd want three views: whole site, /blog, and individual URLs. That gives us the full funnel of ROI impact. All three have validity.

**Jakub Rudnik:** The blog should lift overall site performance. Creating the /blog filter is easy—one addition. The individual URLs require maintenance each time we publish, but all three views make sense. Not a huge lift.

**Aida Knežević:** I wanted to give you an update on the position tracking report in Semrush. We saw keyword improvements—the Swift Alternative blog post has a featured snippet in UK Google search (commercial intent), and the Telegraphic Transfer vs Wire Transfer article is now in AI Overviews. Some articles lost rankings too. SERP tracking is volatile week-to-week but helps month-over-month. Overall keyword visibility is up 0.66%, which is good considering we've only published 18 articles and aren't targeting most of these keywords yet.

**Aida Knežević:** On the content side, I know you have multiple people doing reviews. If there's anything repetitive that you keep correcting, I'd love to hear it so we can tailor polishing instructions. When you get many comments in a row, it's easy to miss patterns, so it helps to hear directly from you what needs to change.

**Mark Stiltner:** These calls are a great forum. I review everyone's edits and bring patterns to these calls. One issue I'm seeing: old language saying "accept in one country or 100." We actually cover 190+ countries, so we changed the CTA doc to say "one country or worldwide."

**Rachel Pasche:** That language was in the CTA template, and with LLM instructions not to alter wording, it kept appearing in every article. I updated it yesterday, so going forward it shouldn't show up.

**Mark Stiltner:** Your team mentioned wanting to improve scannability and blog length. Some do read long and redundant. My approach: get a baseline of data on what works, then test shorter posts, bullets, different formats. But I want to understand what we can measure.

**Kristin Reischel:** Can we isolate performance differences by length? The Looker report shows title, but we probably have more data to analyze what's actually working.

**Mark Stiltner:** I have A/B testing tools to track form clicks per blog and test short vs. long format. Baseline data first, then A/B testing on format, CTA placement, button wording. I need baseline on my end.

**Jakub Rudnik:** CTAs and language work well for A/B testing. Word count and success is tougher—it depends on intent. A 350-word definition post beat longer posts; ultimate guides need length. There's nuance: word count plus content type plus funnel stage plus competitor length. Pattern matching with LLM support works better than pure scientific testing. We publish to understand what succeeds.

**Aida Knežević:** We look at GA4 engagement rate after months to see what gains attention. For top performers, clients often add images or screenshots to enrich them. SEMrush data shows top-ranking content includes images throughout body copy. Visual breaks on every screen really influence engagement.

**Mark Stiltner:** One more thing—we're going with CTA option one. Development support needed for XML integration. Continue integrating CTAs manually for now; I'll update you when it's ready.

**Aida Knežević:** Great, looking forward to integrating those. See you next week.
