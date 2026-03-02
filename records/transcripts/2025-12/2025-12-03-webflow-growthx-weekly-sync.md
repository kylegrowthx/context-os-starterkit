# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-03
time: 19:01 UTC
duration: 28 minutes
organizer: jason@growthx.ai
participants: Colin Lateano, Lake Tahoe
fathom_recording_id: 106063613
fathom_url: https://fathom.video/calls/493295180
share_url: https://fathom.video/share/8DvWSTqi7zo8o4awDtjyiy4SHTtb8poU
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: "Lake Tahoe is a GrowthX employee (internal speaker); only two active speakers in this recorded segment. Many attendees listed on the calendar invite but did not participate in this particular recording."
</metadata>

---

## Summary

GrowthX and Webflow synced on the integration hub strategy, focusing on a V2 roadmap that enhances content with rich media and FAQ expansion powered by Reddit/forum questions. Colin shared Amplitude data showing the Upload Care integration page drove app install spikes, validating that the hub supplements (not cannibalizes) the marketplace. The team identified three key gaps: formal processes for partner change requests, a triage system for new integration hub submissions, and a category structure overhaul to replace the current imbalanced system (some categories with 1 app, others with 40).

---

## Context

This is a weekly sync between GrowthX's content/integration team (represented by Lake Tahoe) and Webflow's partnerships and developer experience teams (Colin Lateano as primary contact). GrowthX has been building Webflow's integration hub—a collection of 400+ implementation guides for Webflow + third-party app integrations. The hub drives SEO value (articles ranking well in search), feeds into Webflow's AI-powered product recommendations, and has become a key asset for Webflow's tech partnerships team as they acquire and onboard new partners. Colin's team manages the hub's operational health and responds to partnership team requests for changes, additions, and improvements.

---

## Relevance

**To GrowthX Delivery:**
- V2 strategy requires FAQ expansion sourced from Reddit/forum searches for each integration—likely 15–20 hours per article type to research and integrate authentically
- Screenshot and rich media additions require either scaled tooling or manual creation per article—scope impact on delivery timeline
- Category structure overhaul via Webflow API may require GrowthX dev resources to script and test

**To GrowthX Business Development:**
- Partnership leverage is a new revenue angle: Colin indicated 180–200 apps could benefit from dedicated guides, suggesting a potential co-creation/co-marketing vector with Webflow partners
- Webflow testimonial from Rachel Wolan is in progress (planned for week of 12/10)—position for case study or reference
- Colin's team is defining a formal triage process for partner requests; GrowthX should clarify SLA and ownership (is this ad-hoc or a retainer scope?)

**To CheckThat:**
- Integration hub content is feeding AI tool recommendations at scale; mentions of "AI vibe-coding" and long-tail search queries suggest strong AEO/AI discoverability value
- Webflow's AI-driven product suggestions likely pull from the hub as canonical sources, validating SEO + AEO strategy alignment

---

## Overview

- **V2 Strategy:** The V2 strategy will enhance articles with rich media (screenshots) and integrate Reddit/forum questions into FAQs to provide canonical answers to user pain points.
- **Partnership Leverage:** The hub is a powerful tool for the tech partnerships team, driving app installs (e.g., Upload Care saw a spike) and providing data to advocate for partner app improvements.
- **Category Overhaul:** A new category structure will be implemented to fix partner complaints about inconsistent categories (e.g., some with 1 app, others with 40), improving user experience and SEO.
- **Process Gaps:** Two key processes are missing: a formal way for partners to request article changes and a triage system for new integration hub requests.

---

## Key Topics

### V2 Strategy for Article Enhancement

  - With over 400 articles published, the team is planning a V2 strategy to improve content quality and utility.
  - **Primary Enhancements:**
      - **Rich Media:** Add screenshots and other media to articles.
      - **FAQ Expansion:** Integrate common questions from Reddit and forums into FAQs.
          - **Rationale:** Provide canonical answers to user pain points, replacing scattered forum threads.
          - **Example:** For "Webflow WooCommerce," address the product limit question directly.
              - **Answer:** The Advanced plan supports high volume, but the process is tedious.
              - **Significance:** This honest answer builds trust and clarifies platform capabilities.

### Hub Performance & Partnership Leverage

  - The integration hub is a key asset for the tech partnerships team, who are now requesting changes and additions.
  - **Performance:**
      - Articles are ranking well in search.
      - Amplitude data shows a clear spike in installs for apps featured in the hub (e.g., Upload Care).
      - **Conclusion:** The hub supplements the marketplace by driving discovery, not cannibalizing it.
  - **Strategic Value:**
      - **Partner Advocacy:** Provides data (e.g., page visits) to advocate for partner app improvements in QBRs.
      - **New App Justification:** Proves user demand for integrations that don't yet have an app.
      - **Growth Potential:** An estimated 180–200 unique apps could benefit from dedicated guides.

### Category Structure Overhaul

  - The current category structure is inconsistent, with some categories having only 1 app and others having 40.
  - **Impact:** This inconsistency causes friction for the tech partnerships team, who manage partner relationships.
  - **Solution:** Implement a new, more logical category structure.
      - **Implementation:** GrowthX will use the Webflow API to update categories in the CMS.
      - **SEO:** A 301 redirect strategy is needed for old category pages.
      - **Decision:** Prioritize a simpler structure over the complex, multi-nested proposal to ensure feasibility.

---

## Action Items

**Lake Tahoe (GrowthX)**
- Draft V2 plan: FAQ-led content, screenshots/media, linking, Reddit questions; share with Colin

**Colin Lateano (Webflow)**
- Define triage/intake process for partner-requested updates; share with Lake Tahoe
- Send Amplitude install-spike chart to Rachel Wolan for testimonial
- Share category recategorization proposal with Partnerships team; collect feedback

---

## Transcript
**Lake Tahoe:** This meeting is being recorded. I think it's probably hot in here because it's hot in one of the other rooms.

**Colin Lateano:** New office.

**Lake Tahoe:** Yeah, it's a lot of the team here this week. How was your Thanksgiving?

**Colin Lateano:** Busy. Traveling and family, and a lot of snow where I am.

**Lake Tahoe:** My family's visiting from Toronto. I almost forget snow exists until they remind me.

**Colin Lateano:** That's a luxury. I bought a snowblower—I'm dealing with a lot of snow here.

**Lake Tahoe:** It's been good. All right, so this week's mostly a quick update, but we've published over 400 articles now.

**Lake Tahoe:** I wanted to think about what a V2 looks like and what we want to improve. We need better linking, screenshots, and rich media at scale. And when I look at searches for something like Webflow WooCommerce, I see Reddit threads with real questions people are asking. We should make that more explicit in our content—essentially mining those threads for FAQ answers.

**Lake Tahoe:** So when you read some of these, it's like, you know, it would be good to have a canonical answer to like some of these questions that is controlled by you instead of whatever this thread is.

**Colin Lateano:** How would we do that at a scale like this?

**Lake Tahoe:** I think it depends on the question.

**Lake Tahoe:** I looked at if a lot of these required, like, it's like super opinionated or just something that is answerable very quickly by, like, just like by the fact we have your help center ingested in your, like, API ingested.

**Lake Tahoe:** Kind of like, let's see what this one is.

**Lake Tahoe:** I don't know if you can access website.

**Lake Tahoe:** Okay, so something you cared about, like, kind of this cap on products.

**Colin Lateano:** Maybe I mean more, if, if, if I'm thinking you're suggesting the V2 of this would be potentially finding.

**Colin Lateano:** Because there already is an FAQ on every implementation guide.

**Colin Lateano:** Are you thinking of adding more questions in the FAQs that would be better answered?

**Colin Lateano:** And so then we could be doing querying of common questions regarding implementation, maybe through Reddit or other major forums, and then generating a larger FAQ on every page?

**Lake Tahoe:** Yeah, that could be one form.

**Lake Tahoe:** I guess the high-level thing that I'm trying to hear is like, you want to be helpful, I think when you kind of like look at the couple of keywords that revolve around these topics, you end up seeing some of the other content out there, and I'm noticing a pattern around just like people with questions that you end up doing with Reddit.

**Lake Tahoe:** It's like, how do we kind of layer that into the content?

**Lake Tahoe:** That's like a FAQ, you know?

**Colin Lateano:** I think it's an excellent approach, and that is the thesis of this integrations hub is trying to solve long-tail questions.

**Colin Lateano:** So people feel confident in their implementation of Webflow.

**Colin Lateano:** So if the V2 of this is finding what common questions are regarding the interop of topic X and Webflow and enhancing the docs to include, enhancing the integration docs to include those answers of questions, I think it's wonderful.

**Colin Lateano:** I think it's a good idea.

**Lake Tahoe:** Yeah, I guess to answer your question, I actually don't know how we would cover this, but that would be the work to figure it out.

**Lake Tahoe:** This one's interesting, where it's like a best practice a little bit, and you see people arguing about maybe it would be better on WordPress or something.

**Lake Tahoe:** So, under, no, no, no.

**Lake Tahoe:** I guess just directionally, I guess, you know, it seems like you're interested in this too, so.

**Colin Lateano:** I think the directional idea is right.

**Colin Lateano:** Yeah.

**Colin Lateano:** I don't know if this question explicitly.

**Colin Lateano:** We'll be able to get a good answer because the good answer of that is we're really not built for this.

**Lake Tahoe:** Oh, okay.

**Colin Lateano:** But if you really wanted to use Webflow to be a product page for every single product you have, our CMS at enterprise level could support this amount of volume.

**Colin Lateano:** It's just fairly tedious, but sure, you could do it.

**Colin Lateano:** Yeah.

**Lake Tahoe:** See, the advanced plan can support it, but it's...

**Lake Tahoe:** It's like, yeah, it's cool, it's ready.

**Lake Tahoe:** I mean, maybe that is the answer.

**Lake Tahoe:** like it, you know, not every answer has to be the goals to be helpful.

**Lake Tahoe:** I guess there's a product marketing kind of thought of whether you want to almost acknowledge things like that.

**Colin Lateano:** I, as long as, as long as, I think it's a fairly honest answer I'm seeing right now.

**Colin Lateano:** So.

**Colin Lateano:** So.

**Colin Lateano:** Thank

**Colin Lateano:** I think we could generate an answer as long as it's not hallucinating anything, but this is a great idea.

**Colin Lateano:** This is a great way to enhance the pages.

**Colin Lateano:** I'm totally down with that one.

**Colin Lateano:** I will also say on our side, these pages are ranking.

**Colin Lateano:** And so what we're getting is more and more partners, developers, whoever we want to be, that actually own the integration surface are reaching out to us asking, can they make changes to the pages?

**Colin Lateano:** Or some are asking, can we get in this hub?

**Colin Lateano:** Because, I mean, we have at this point now, 380 apps.

**Colin Lateano:** Some apps are not included in the hub yet.

**Colin Lateano:** Can we, they're asking, can they get included in the hub?

**Colin Lateano:** So there is a world of also, I've been telling the partnership team to...

**Colin Lateano:** We could create some sort of triage method to actually get asks forwarded to you, but like, I don't know if, I don't know if, it makes sense to me that we're slowing down on how many integrations to surface, because we might be running out of integrations, but I think we will have a trickle continually.

**Colin Lateano:** Probably one for every major app, probably one for new partners.

**Colin Lateano:** I think this will be a vector of, I think this will be a vector actually, even as like a, a small partnership marketing suggestion.

**Colin Lateano:** I did a, I did a random pulse of one partner that was asking, can they help write their article?

**Colin Lateano:** And the, the partnership team were asking me, well, how does this, does this compete with our marketing, our marketplace pages?

**Colin Lateano:** My answer is, my really, I don't think it does.

**Colin Lateano:** Let me check if I can pull that data now.

**Colin Lateano:** But I was looking at after we launched the integration page, did we see a spike of installs?

**Colin Lateano:** And the answer was a slight yes.

**Colin Lateano:** So I think there's even an influence of installs based on ones that are promoting integrations with the app.

**Colin Lateano:** Let's see if I can regenerate that right now.

**Lake Tahoe:** Yeah, I mean, it seems like this is, like, becoming leverage for your, I guess, you guys have a separate team for partnerships.

**Colin Lateano:** We do.

**Lake Tahoe:** Yeah.

**Lake Tahoe:** I wonder, I don't know, like, they could use this.

**Lake Tahoe:** It's like, okay, if you have some partner leaning in, they want to, like, collaborate, like, what is the best way to get the most out of that?

**Lake Tahoe:** Kind of interesting.

**Lake Tahoe:** Because this page is, I mean, honestly, it's like a small part of it.

**Lake Tahoe:** But I feel like, yeah, we could...

**Lake Tahoe:** Making this concrete, like, create a process where they can update these, or at least have suggestions.

**Colin Lateano:** Well, I mean, if there was some way to just even have a triage where some sort of request can land in some inbox, that would be very helpful.

**Lake Tahoe:** I mean, Vic had one, I think, that we did, but that was the last.

**Colin Lateano:** I don't think we have a good process on our side, so I don't, that makes complete sense to me.

**Colin Lateano:** But let me just, I'm just regenerating this, this little graph on Amplitude.

**Colin Lateano:** Let me, I'm sharing for a second.

**Colin Lateano:** Hello, let me switch at a, at a right axis, there we go.

**Colin Lateano:** So, there is a trailing indicator here, this was Upload Care, Upload Care Reaching.

**Colin Lateano:** They out to us about their listing, and there was then questions about, is this listing competing with the marketplace?

**Colin Lateano:** And what I'm really seeing on this is even looking on a weekly basis, there is a notable spike and a lower high of installs post-upload care page being available.

**Colin Lateano:** Even if Upload Care's integration page is getting only, on average, 300 a week, there is some relationship of the apps being installed based on that.

**Colin Lateano:** And so there is something here of actually adding another trailing value that is not cannibalizing the marketplace, it's actually enhancing the marketplace.

**Colin Lateano:** And so I'm pushing our partnerships team to understand that, and so I would expect we'll have a larger influx of people asking, can they co-author, can they make suggestions, can they possibly enhance our integration pages?

**Colin Lateano:** And I would expect also, this will probably be...

**Colin Lateano:** That a default mechanism for most feature partnerships.

**Lake Tahoe:** Yeah, because, I mean, like, Stripe won't feel it, but, like, some of your smaller partners will.

**Lake Tahoe:** absolutely.

**Lake Tahoe:** All right, well, there's something to do there.

**Lake Tahoe:** Let's see.

**Lake Tahoe:** Oh, and also I saw, like, I mean, I guess I understand, like, this is, you know, like, now this is being, kind of fed into all these things.

**Lake Tahoe:** I imagine any time you ask, like, something about Webflow and Wombomers, this will, this page will likely show up as well.

**Colin Lateano:** Likely so.

**Colin Lateano:** And that's exactly my assumption about the, about the, the visits being very, very agent influenced.

**Colin Lateano:** I have a very strong feeling that because of the, because of how long tail these searches are.

**Colin Lateano:** Yeah.

**Colin Lateano:** And this is showing up in a lot of implementation questions.

**Colin Lateano:** And.

**Colin Lateano:** Yeah.

**Colin Lateano:** I fully believe that the technically dangerous person trying to figure out an implementation between their tech stack is absolutely trying to vibe code something and learn from AI.

**Colin Lateano:** So it makes complete sense to me that we've seen a spike, although unprovable, about the volume being very much not a spam attack of crawlers, but actually a programmatic question set of like, how do I do X, Y, Z?

**Lake Tahoe:** I kind of just assumed Rachel will mention it to you, but she's doing like a, it's like a little testimonial for us next week.

**Lake Tahoe:** If there's anything else you're seeing that we haven't shared yet, it would help arm Rachel for the testimonial. We're planning a little video at your office.

**Colin Lateano:** I don't have more analytics to show, but the data I showed—with the spike up and to the right—proves this isn't just bot traffic.

**Lake Tahoe:** That's all you need.

**Lake Tahoe:** We're working on design suggestions for the developer hub and hoping to get those to you soon. We have a bunch of use case guides pretty much done. We got some comments from Raymond that we've addressed. Anything else?

**Colin Lateano:** I have access to everything I need on our side. Sounds good.

**Colin Lateano:** Do you have the capability on your side to implement the category changes?

**Colin Lateano:** Or do you need us to actually manually change the templates of what categories exist?

**Colin Lateano:** I think it's possible from your editor controls.

**Lake Tahoe:** Yeah, I think categories is purely a CMS item change, right?

**Lake Tahoe:** Like we get real small ones and make sure that reference field is updated.

**Colin Lateano:** Yep.

**Lake Tahoe:** I believe we can do that.

**Lake Tahoe:** Are we...

**Lake Tahoe:** He's in the API now, if you remember, are we still doing, I think we have the API, so it should be, I mean, we need our engineering, just like write a little script or something, but, yeah, so I guess to answer your question, we can do that on our end.

**Colin Lateano:** And, I, I think that would be valuable to do, I think it will hit SEO, slightly, because those category pages are not totally, are not totally done, maybe we can think about a good strategy to 301, the integration types, but, I, I, we, we do get complaints from partnership team on the categories not being very descriptive or not making sense in some domains, so.

**Lake Tahoe:** Did you share these suggestions at all?

**Lake Tahoe:** Do you think they're more on board with these ones?

**Colin Lateano:** I didn't.

**Colin Lateano:** So the partnership team right now is at, I've been doing some end-of-year conferences.

**Colin Lateano:** I didn't share this with them.

**Colin Lateano:** I'm happy to share it with them.

**Colin Lateano:** I don't know if we will get a response back because it's a multi-nested structure in the first, in the better proposal.

**Colin Lateano:** I just don't know if they're going to read all of it and say, yeah, okay, these 70 categories are rational.

**Colin Lateano:** I appreciate that.

**Lake Tahoe:** Yeah.

**Lake Tahoe:** I mean, anecdotally, was there any particular integration where they weren't happy with the category?

**Colin Lateano:** No.

**Colin Lateano:** The feedback was some categories only have one or two in them, and why do some categories have 40?

**Colin Lateano:** It was fair to evaluate our categories.

**Lake Tahoe:** What does your partnership team do exactly?

**Colin Lateano:** So the partnership team is divided into two sections.

**Colin Lateano:** One is partners that are like resellers and agencies that implement Webflow, and the other is tech partnerships.

**Colin Lateano:** And the tech partnerships team is the one I'm talking about.

**Colin Lateano:** They reach out to major brands or emerging brands and work with them to get an integration app on Webflow.

**Colin Lateano:** So many of our apps that you'll see, like our Adobe Express or our Getty Images or our Shutterstock apps, those are directly related from partnerships team going out and seeking those companies and saying, Webflow is an emerging brand.

**Colin Lateano:** You really should get involved in it.

**Colin Lateano:** We have a large customer base that will use the app, which helps partners see immediate value and commit to building on Webflow.

**Colin Lateano:** Our app marketplace didn't grow purely organically.

**Colin Lateano:** It was a lot of influence and having these partnership members reach out and try to get those apps on the system.

**Lake Tahoe:** And then there...

**Lake Tahoe:** I guess their goal is like how many installs and like kind of touches these apps get with your user base, I imagine.

**Colin Lateano:** Yes, yes.

**Colin Lateano:** That is their dream goal.

**Colin Lateano:** They don't have direct influence on that.

**Colin Lateano:** So they don't measure that as like the metric they want to track.

**Colin Lateano:** But yes, the partnership is only successful if there's actually use of that because a company investing in time to build an app on Webflow without having any reach is going to say, well, was a waste and walk away from ever being another partner again with us.

**Colin Lateano:** So they absolutely want to see installs.

**Colin Lateano:** absolutely want to see value add in some dimension.

**Colin Lateano:** And they act as account managers of that partnership.

**Colin Lateano:** So that's why I'm saying that I get reached out to about why is my partner's app showing up in this integration hub in a weird category that doesn't fit?

**Colin Lateano:** Or my partner's asking about, well, the integration guide isn't totally correct.

**Colin Lateano:** Can they make some changes to it?

**Colin Lateano:** Like that's the, they're trying, they are relationship managers at the core.

**Colin Lateano:** And so this integration hub has become an extension of promotion for their partners.

**Lake Tahoe:** Yeah.

**Lake Tahoe:** Okay.

**Lake Tahoe:** I think, yeah, I don't know exactly when, but I think the update we can do.

**Lake Tahoe:** I personally have probably go with this suggestion just because I don't know if we have the dev to do this kind of nested structure.

**Lake Tahoe:** I don't know either.

**Lake Tahoe:** I'd rather just keep it a little simple, simpler.

**Lake Tahoe:** Yeah.

**Lake Tahoe:** we can look at that.

**Colin Lateano:** Is the Notion doc shareable, or should I copy it to a Google Doc?

**Lake Tahoe:** By default we don't make it shareable, but I can. It's not as good as Google Docs for sharing, but they can access it.

**Colin Lateano:** Just which meeting did we have the category layouts?

**Colin Lateano:** It's its own section, right?

**Colin Lateano:** So if I go to Webflow and GrowthX, there is a.

**Lake Tahoe:** Yeah, where is the spot?

**Colin Lateano:** I don't think I have access to this section.

**Lake Tahoe:** We've nested it a lot, okay.

**Lake Tahoe:** Let me just move.

**Lake Tahoe:** Okay, we'll move it out to somewhere accessible.

**Colin Lateano:** I found it.

**Lake Tahoe:** I found it.

**Lake Tahoe:** I can share it.

**Lake Tahoe:** Right.

**Lake Tahoe:** Sure.

**Lake Tahoe:** right.

**Lake Tahoe:** you.

**Lake Tahoe:** Yeah, I'm still thinking about this integration thing, because one thing that jumped at me at the beginning when we're doing that Stripe doc was interesting, the capabilities of that Stripe app, and there's a whole lot of things that it could do, but it seemed to only do a certain set of things, and I was curious, do you want to just build that integration out, or do you want to write a guide that almost circumvents, not circumvents, but gives you another option?

**Colin Lateano:** Say it again, I'm sorry.

**Lake Tahoe:** Nah, never mind.

**Lake Tahoe:** I think I was just thinking, now I kind of understand who owns the apps side, and who builds it, and who facilitates the creation of those, and then...

**Lake Tahoe:** Cause like...

**Lake Tahoe:** like...

**Lake Tahoe:** It feels like where we could be valuable with these integration guides is, like, I mean, you're trying to make Webflow more accessible and feature-rich and stuff like that.

**Lake Tahoe:** trying to think, like, is there a way to help your partnership team, you know, do what they do?

**Lake Tahoe:** Because at the end of the day, I mean, if Stripe builds another app that, like, does some of the things we say the APIs can do, like, that's probably the best solution.

**Lake Tahoe:** Yeah, it absolutely is.

**Lake Tahoe:** Yeah.

**Colin Lateano:** So you're saying other enhancements of the integration guides are when there's an app, although I kind of think you're already doing it, but you're saying you would, you want to make deeper content for utilizing each of the apps?

**Lake Tahoe:** No, well, I mean, yeah, like, that will do, I guess I was thinking, like, okay, with, like, how do we arm your company, I guess?

**Lake Tahoe:** I know it's a different team, but, like, arm Webflow to go to Stripe and be like, hey, guys, your app is kind of, like, like, a little bit, you know, build a belt.

**Colin Lateano:** I think that's a much harder conversation.

**Colin Lateano:** Yeah, fair enough.

**Colin Lateano:** I think this as a supplement to partnerships is really great.

**Colin Lateano:** I don't know if this can be a leading conversation to say, this integration page is getting visited a lot.

**Colin Lateano:** Well, I mean, it probably is, but I don't know how much more we can do with it at this moment.

**Colin Lateano:** But I do think with enough momentum showing, this integration page gets visited a lot.

**Colin Lateano:** And we are seeing these mutations happen.

**Colin Lateano:** You Need to Enhance Your App is absolutely a fair conversation.

**Colin Lateano:** But I think it comes up in a QBR.

**Colin Lateano:** I think a lot of what we can offer is we can do deeper guides on how to use the apps.

**Colin Lateano:** But also, it's really important to note that we probably have 180 to 200 apps that are very, very unique and could use additional help in getting marketing guides.

**Colin Lateano:** And I think it would be a great value add.

**Colin Lateano:** But we also are having integration guides for things that don't have apps yet.

**Colin Lateano:** And we can use...

**Colin Lateano:** use...

**Colin Lateano:** The indication of people are searching for this, finding it, showing we need an app.

**Colin Lateano:** I think that's a really useful value prop.

**Colin Lateano:** But I think that is coming out naturally.

**Lake Tahoe:** Yeah.

**Colin Lateano:** Which is also why I think, I don't know, 400.

**Colin Lateano:** I think the number is probably closer to 700, if I'm being honest about.

**Colin Lateano:** All of the novel apps that we have to solve problems, plus all of the major platforms that we'd want to have integrations with, I'm going to guess is probably closer to a number like 700.

**Colin Lateano:** But I think it's slowing down makes sense to me.

**Colin Lateano:** I think we are scraping the barrel right now.

**Lake Tahoe:** No.

**Lake Tahoe:** Well, I haven't checked that table and wall.

**Lake Tahoe:** I think we do have something close to 700.

**Lake Tahoe:** But even, you 700 is like, you know, two months away or whatever that is.

**Lake Tahoe:** Sure.

**Lake Tahoe:** Like our, yeah, it could have a little bit cool.

**Lake Tahoe:** I think that's it on our end.

**Lake Tahoe:** So, there's a little green.

**Lake Tahoe:** I don't about.

**Lake Tahoe:** We owe you these two suggestions here, and that's it at the moment.

**Colin Lateano:** Right on.

**Colin Lateano:** I'd love to think about what a process can be also so partnerships can asynchronously make requests for changes to any of the listings, but I think that'd be a great next step of it.

**Colin Lateano:** I'm going to share with a partnership team right now this recategorization strategy and ask their opinion of it.

**Colin Lateano:** I'm not imagining a very big amount of feedback from it, but it's fair to give them a chance to give a round of feedback.

**Lake Tahoe:** Cool.

**Lake Tahoe:** Sounds good.

**Lake Tahoe:** All right.

**Lake Tahoe:** Colin and Zach.

**Lake Tahoe:** Ciao.

**Lake Tahoe:** See you later.

**Lake Tahoe:** Talk to you soon.

**Lake Tahoe:** Appreciate it.

**Lake Tahoe:** See you.
