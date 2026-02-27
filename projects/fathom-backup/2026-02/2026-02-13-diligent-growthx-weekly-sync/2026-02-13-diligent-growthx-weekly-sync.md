# Diligent <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-13
time: 16:00 UTC
duration: 32 minutes
organizer: Carrie Chowske (GrowthX)
participants_external: John Habib (Diligent), Jordan Barlow (Diligent), Shathabi Ravindra (Diligent), Abi Ravindra (Diligent), Kezia Farnham (Diligent), Festus Shodipo (Diligent), Tyler Phelps (Diligent), Amanda Roesser (Diligent)
participants_internal: Carrie Chowske (GrowthX)
fathom_recording_id: 122315623
fathom_url: https://fathom.video/calls/565597924
share_url: https://fathom.video/share/grhsWWyp2LyssGx2igsuqikH7zzNQzz_
source: fathom
enriched_on: 2026-02-27T00:00:00Z
enriched_by: Claude
</metadata>

---

## Summary

Weekly sync between GrowthX and Diligent covering LLM content refreshes (3 ready to publish, 3 in review), Sanity API key approval process for automated staging, and AI visibility metrics showing 100% citation coverage on key prompts. Also discussed Optimizely publishing errors, brand alignment for AI-generated images, and migration timeline for Feb 23 with 3-day publishing freeze.

---

## Context

GrowthX is Diligent's content marketing partner, responsible for managing their LLM gap refreshes, keyword research, and AI visibility strategy. Diligent's web team is in the middle of a site migration and has expressed concerns about integrating new tools (Sanity API, Atlas) with their existing Optimizely CMS setup. Carrie Chowske leads content strategy and AI visibility tracking for the account; Kezia Farnham is the primary stakeholder on Diligent's side managing production, approvals, and web integration. The partnership includes regular reporting on organic traffic, AI citation visibility, and keyword research (DMI, Vaults, ACL keyword studies).

---

## Relevance

- **Production & Delivery:** Content review bottleneck resolution; process improvements for flagging new vs. refresh content and AI-generated images
- **Client Integration:** Sanity API key approval pending; web team concerns about CMS integration security and documentation
- **Content Strategy:** DMI keyword research methodology (topic competitors vs. business competitors); Vaults keyword prioritization for next phase
- **AI Visibility:** Breakthrough metric—100% citation coverage on key library prompts; high volatility compared to traditional SEO; platform differences (Google AI Overview vs. AI Mode)
- **Risk Management:** Site migration timeline (Feb 23); 3-day publishing freeze; internal taxonomy shift with minimal expected SEO impact

---

## Overview

- **Production:** 3 LLM gap refreshes are ready for review; 3 more are in review. The Sanity API key request for automated staging is pending a web team security review.
- **Process Improvements:** To streamline reviews, content will be flagged as "New" or "Refresh" in the production list, and AI-generated images will be commented on for approval.
- **Strategy:** The DMI keyword research used topic competitors (e.g., MetricStreams) instead of direct business competitors to find higher-volume topics. Diligent has 100% AI visibility on key prompts, but this metric is highly volatile.
- **Migration:** The site migration is firming up for the week of Feb 23, with a 3-day publishing freeze. A planned internal taxonomy shift is not expected to impact SEO.

---

## Key Topics

### Production & Process Improvements

  - **Content Status:**
      - 3 LLM gap refreshes are "Ready to Publish."
      - 3 more are "In Review."
      - 3 additional refreshes are in production, due by EOD Feb 13 or Feb 16.
  - **Sanity API Key for Automated Staging:**
      - **Request:** An API key for automated staging from GrowthX's pipeline.
      - **Rationale:** Frees up manual staging time for higher-level tasks.
      - **Blocker:** Diligent's web team requires more info on the Atlas/Sanity integration, citing past difficulties publishing from Optimizely.
  - **Review Process Enhancements:**
      - **Flagging Content Type:** Add a "New" or "Refresh" column to the production list to enable different review workflows.
      - **Flagging AI Images:** Add a comment to new AI-generated images for explicit approval.
          - **Rationale:** Ensures brand alignment and avoids re-reviewing previously approved assets.
          - **Note:** GrowthX uses text overlays to prevent AI text hallucinations.
  - **GRC Guide Publishing Issue:**
      - **Problem:** A generic "structure tool crashing" error prevents publishing the main GRC guide in Optimizely.
      - **Action:** Diligent's web team will attempt to troubleshoot and publish the guide.

### Content Strategy & Keyword Research

  - **Keyword Prioritization:**
      - **Vaults Keywords:** Diligent is reviewing the list to extract top suggestions and add comments for a follow-up discussion.
      - **DMI Keywords:** The research used topic competitors (e.g., MetricStreams) because direct business competitors lacked sufficient search volume for the subject matter.
  - **AI Visibility & Organic Performance:**
      - **Organic Traffic:** Growth is strong across most business units, especially ENT.
      - **AI Visibility (7-day):**
          - 100% visibility achieved on key library prompts, including "how to secure board document sharing and collaboration."
          - Diligent is cited in all 5 sources for that prompt.
          - **Observation:** AI visibility is highly volatile, enabling faster impact assessment than traditional SEO.
          - **Platform Discrepancy:** Google AI Overview citations are significantly higher than Google AI Mode, which is unusual compared to other clients.

### Site Migration

  - **Timeline:** Firming up for the week of Feb 23.
  - **Publishing Freeze:** A 3-day freeze is planned for Wednesday–Friday of that week.
  - **Taxonomy Shift:** An internal content topic shift is planned.
      - **SEO Impact:** Not expected to be significant, as URLs will remain unchanged.
      - **Risk:** Potential for temporary, automated breadcrumb errors.

---

## Action Items

**Kezia Farnham (Diligent)**
- Review LLM gap refreshes in Sanity; publish 3 Ready, edit 3 In Review
- Review remaining AI visibility points in Carrie's report
- Follow up with web team on Sanity/Atlas integration documentation and security concerns
- Troubleshoot GRC guide publishing error with web team and test if issue can be resolved from their end

**Carrie Chowske (GrowthX)**
- Double-check production view in Sanity; ensure all statuses are visible to Kezia
- Send Sanity API key/Atlas integration security documentation to Kezia for web team review
- Verify Tyler Phelps (Diligent) has Check access; add if missing
- Review AI image generation pipeline; ensure brand alignment with design guidelines; enforce 'AI-generated' comments for new images
- Update content workflows: use 'Existing URL' terminology for refreshes instead of 'Suggested URL'; add New/Refresh column to production review view
- Send GRC guide task list and live Optimizely link to Kezia for web team troubleshooting

---

## Transcript

**Carrie Chowske:** It's Friday, so that's good, but also it's Friday, so it means I've got a lot to get done before the end of the day, but that's all right.

**Carrie Chowske:** We were the part of North Carolina that got hit with the blizzard last week.

**Carrie Chowske:** So the snow like finally melted.

**Carrie Chowske:** I can get in the general vicinity, you know, and kind of say, and that same thing, I work with so many people around the world that, like, we're constantly, like, trying to translate that, and people will talk about the temperature, and they'll post it in both.

**Carrie Chowske:** I'm like, it's so cute.

**Carrie Chowske:** I just don't know why we don't embrace that kind of stuff more, you know, like, we're all different. Let's just deal with it.

**Kezia Farnham:** Thanks for passing on the agenda.

**Carrie Chowske:** The production update, I think, is accurate. We've been trying to, like, clear out things, and I'm much more of an accurate record keeper than most people are. I gotta know where everything is.

**Carrie Chowske:** I just heard from production this morning that they're working on some more of those LLM gap refreshes. They're trying to have them done today, but at the very latest, it'll be Monday.

**Carrie Chowske:** There should be three in there that are marked as ready to publish. And then there's three that are in review. I think two of those are, two of the ones ready to publish are new.

**Kezia Farnham:** So I'll take a look on Monday then at these. I did go in today and I had a moment where I was like, it looked like a long list and then suddenly it looked a lot shorter.

**Carrie Chowske:** So maybe I'll just double check and make sure I don't have anything that I like forgot to put on your view. So I didn't miss any of those because there could be some, you know, stragglers that I missed because of that.

**Carrie Chowske:** Our production team asked if we could maybe get an API key for Sanity to do, just automate staging. We wouldn't be publishing to it or anything.

**Kezia Farnham:** We have, and I've chased because it was a couple kind of follow-up questions, but we, I would say some things may be a little slower at the moment, just because we're still mid-migration. So that's kind of like the main focus in the web team. But I have recircled the question and just asked if there was anything further that is needed from the web team to know.

**Carrie Chowske:** I can also just send you like a quick little message too that's like, here's what we're using it for and here's what we need. And so that they're confident in like the security of it because it's only accessed by our workflows. It's just going between us and your CMS for us to be able to just auto stage from our pipeline. It kind of saves a little bit more manual time on this end. And we got one person doing a lot of staging for a lot of clients. And the more we can help automate that, the more that frees him up to do other higher level tasks.

**Carrie Chowske:** You should also have a check that invite that I sent earlier this week. I didn't know who else that, in addition to you, that you wanted me to send.

**Kezia Farnham:** I'm sure Tyler will want access if he's not already been added.

**Carrie Chowske:** I went in and double checked that all the scrunch prompts are in there and then checked all the tags and everything. There will be some differences if you're looking at the data side by side, if you do go into scrunch and look at it. Just because we track differently than they do. And we're looking at a different set of prompts because we also have those library prompts that are part of check.

**Kezia Farnham:** I know we did have some conversations previously on trying to get them, I guess, as close to our brand styling and also help to automate some of that process from us because on our end, we were doing some of this through Canva. And I think the brand team were very happy with the output. There was a few tweaks that were requested in terms of like styling and we sent on our brand kit and then also the imaging for any icons that are used.

**Kezia Farnham:** And then if your team is able to just comment when it's a new image, that would be super helpful. So I know, okay, I'm going to pay a little bit more attention. It's an AI, and I'm not checking for something that was already kind of approved and published and having to kind of do the guesswork.

**Carrie Chowske:** I'll look at how the image step is constructed in your pipeline, too, because we have a couple different ways that we do it. And usually when there's text involved, it's done as an overlay, so we don't get those weird hallucinations where there's, like, you know, like nonsense in the text. I used to be a graphic designer, so, like, I can't handle when graphics look crappy.

**Kezia Farnham:** If it's not now, we will make it that way. And just letting us know, like, this is one that's AI. I generated, please approve. And then that'll just make the review process super fast for the content team as well and for myself.

**Carrie Chowske:** I will flag that for them. I'm sure they'll have no problem with that.

**Kezia Farnham:** And I think on that, I left a comment on one of the blogs today and it was just, if something is a refresh, would it be possible to change the wording from suggested URL to existing URL? And that would, again, just make me know immediately, yep, this is a refresh and I know what I'm looking at. And it's also super helpful and clear for any kind of sort of audit trail when we go back and try and work out where things are off or refreshes.

**Carrie Chowske:** I can also make it so it's clear, too, when you're looking at the list of things that are ready for review. Like I can put a column in there, too, to say if it's new or refresh. You can also see it before you even go into it.

**Carrie Chowske:** And the only other thing that I had that was new was just kind of touching base on the prioritization of the recent like keywords, keyword research that we've done. We think that it was the last one that Vivek did for you, the ACL one that I did, and then the DMI that I just delivered. We're okay with the moment, I think, on deliverables. I think we've got other, a few more like LLM gap refreshes we can do before we're really getting critical on what we need to be doing.

**Kezia Farnham:** Let me go through, I think for the vaults keywords, there were a, there's a little bit more, I've started to make some comments in there. I think there's some really good suggestions. I think what we can do is we can start to just take out like the best of, and then there's a few kind of areas where I just want to like have like whether, you know, questions or just raise or maybe kind of adjust things slightly.

**Kezia Farnham:** And thanks for sending through the latest for the DMI for a first batch there.

**Carrie Chowske:** The only thing I wanted to bring up was I know something that Vivek flagged for me when I did the first one was just that we didn't do direct business competitors, but it had more to do with the topic concentration, and there just wasn't enough volume really around the topics. If I was looking at more broad competitors like MetricStreams, we looked at the topic competitors, like who you're fighting against for that space in the search. So it's a little more geared toward that in case, you know, you're concerned about it or Tyler or anything that that's why we went that route, just because we were looking for, you know, getting those things top of mind. But I got so much from just that once we went to with these other competitors. So I was like, let's start here and see what topics are relevant. And then we can narrow further and dig in deeper if we need to.

**Kezia Farnham:** And I'm sure, like, I think this will also help to pass back to the internal team to be like, here's where the conversations were leading us to. And if we want to have further conversations, we can to, you know, go even further.

**Carrie Chowske:** It was still really helpful. Like I said, that's really kind of what got me to the like, looking at these different types of competitors in terms of content competitors, rather than business competitors, which is, you know, when we're doing content, you kind of, got to deal with like, who's on the SERP, right? Any context is always useful at anything.

**Carrie Chowske:** I too, I was pulling this up because I wanted to talk about AI visibility a little bit more, but just a quick, I did a quick summary on where we're at with organic traffic. Since we just did the monthly review, I just pulled like 30 days just to kind of like look at the business units and like where we're at. I'm seeing pretty good growth across most of them. These, these were the top four, saw the biggest lift in ENT. And then we also had gains, pretty significant gains in these areas as well.

**Carrie Chowske:** And then I've really been digging into like the AI visibility now that we have everything kind of built out. I really loved, when I logged in yesterday, I saw that we had like 100% visibility on a couple of the top, a couple of these library prompts, which tend to be the broader prompts, which is, I think, kind of impressive, honestly, because those are the harder ones usually to get the visibility for. So it shows that what we're doing is getting noticed by the LLMs. And there's some like, you know, where, and on most of those, Diligent's getting the lion's share of citations as well.

**Carrie Chowske:** Just this one in particular, how to secure board document sharing and collaboration. This is like, out of these five citations, like Diligent's obviously one of them, but Diligent's present in all of the prompts.

**Carrie Chowske:** So there's a lot of there's a lot more volatility here than with SEO. Which honestly, I think is good. You can see right away, like what you're doing, if what you're doing is having impact, you don't have to wait as long. But what I what I kind of like to look at, too, is across like different platforms, like what is getting, you know, what's where are getting cited? Where are you getting coverage? Where are you getting positive mentions versus maybe not so positive or neutral mentions?

**Carrie Chowske:** And a thing that I've noticed, and this is interesting to me that these are so far apart, diligent, because for the most part, I'm seeing Google AI overview and AI mode kind of closer together in terms of how often you're getting mentioned or cited. Because what I've seen Google doing, and I think we'll start to see them picking up a little more steam in relation to ChatGPT, because they started really pushing AI in search. So in addition to the AI overviews, now if you read the AI overview, you expand it, especially in mobile, the button is like huge. It's like, explore this more in AI? And you're like, yeah, okay, maybe I will, you know? So I started to notice a little bit more of a trend kind of linking these together, because if someone's going to look at that AI overview, they may very well dig into Google AI mode as well. So, but it's interesting, this one's, yours is not as close as a lot of the other ones I've seen. But it's also more spread out evenly over these platforms.

**Kezia Farnham:** I will jump in and maybe take a look at the remaining points in your, that you've listed out here. That's great. Thank you for putting the report together as well. I have a couple quick things to flag before we jump.

**Kezia Farnham:** And also, I just actually got a message from our web team. In terms of the question around publishing, so what I'm hearing from them is, I think they want a little bit more information on how Atlas would integrate with Sanity, just on the system, what that would look like, they're saying the internal team have requested to be able to publish from Optimizely, but that's not been possible without a lot of work. So I think they just want to have a little bit more insight from you, and how the process works.

**Carrie Chowske:** As soon as we're done, I'll send you our standard message, and you just tell me if you need more information, and I'll get with our head of client ops on that side to get more information if you think you need it.

**Kezia Farnham:** And a quick question on that GRC guide that they were struggling to publish. So was this, this was our main GRC? Like, are you able to reshare the task list for the one that was the challenge? Because I think the web team, they will retry from their end and see if they can solve it that way.

**Carrie Chowske:** Yeah, I think it was literally just when they try to go and publish it that they're getting this, kind of a generic error, so I don't know if that's literally all that they could say, is that when they tried to, they could save it, but like when they went to publish it, they would get this error about the structure tool crashing.

**Kezia Farnham:** Oh, can you send me that? Yeah, it's just last week's agenda. That was in the agenda from last week. I will pass that on. And then is there a link to the actual Optimizely? Is that in there as well?

**Carrie Chowske:** No, is the live one.

**Kezia Farnham:** If you wouldn't mind. That would be super useful. I was going to find it, but we've done a number of updates to that piece over time. And so I want to make sure I'm getting the right one. I'll pass that over to them anyway. And they've said that they will go in and just try and troubleshoot, but also see if they can do it on their end.

**Kezia Farnham:** Quick note in terms of migration, it is looking like it's really firming up for the end of the month. So what is likely is that it won't just be one day. I did think that was fairly tight in terms of a publishing freeze. They're currently looking to be more likely the Wednesday through the Friday of, I want to say the 23rd. The week of the 23rd. So that's kind of the latest there. They did mention there is going to also be a taxonomy shift for the content internally. From my side, I'm not necessarily seeing any kind of like major SEO risks around that. Did want to raise it in case anything jumped out to you. I would say it's probably a lower priority, like a lower risk level than anything else relating to a migration. But that was a question that did come from the web team.

**Carrie Chowske:** Like in terms of like the content like topics or just the be used?

**Kezia Farnham:** It's just the content topics, how it's, I imagine this will impact the breadcrumbs there. It is going to be automated, how it's categorized. And checks will probably be like a little bit more manual over time. So there might be a period, if anything is kind of mixed match, where it's not 100% accurate.

**Carrie Chowske:** So are they changing the structure of the URLs, too?

**Kezia Farnham:** That's staying the same.

**Carrie Chowske:** Okay. Then I don't think it'll matter. It shouldn't. But I think we'll just keep an eye on it and you and I can, you know, let them know if they think it all gets messed up. I don't think it'll matter, though. I think that if it's just for your internal purposes, it shouldn't, if it's not part of the URL or the code necessarily, I don't think it's going to affect SEO.

**Kezia Farnham:** So I'm to think if there's anything of that that would be like a slight signal potentially.

**Carrie Chowske:** Maybe. If it's like in the header or the title of the page or something, but I just don't know what it would be.

**Kezia Farnham:** No worries. The, I think the education and templates aspect, I think more to come there, I have started getting back some documentation from the team that I'm now doing some mapping for. So, so no actions needed there at this point, and yeah, I think that's, I think that's pretty much what I had on my side to cover here. I think in terms of prioritization, let's take a look, let's take a look back and kind of get some more of the SEO pieces in the mix with the LLM side. So, we don't start to sort of fall short, just, you know, focusing one way, leaning one way more than the other.

**Carrie Chowske:** I do think the way that you've approached it and we're continuing to do is the right way. And I think that we're focused still on keywords quite a bit because that's going to, the keywords are still a signal of what people are using AI to search for too. And so I think the balance is really good. I just didn't do much more in depth with SEO for this week just because we had just done a big, I just did the monthly one last week.

**Carrie Chowske:** That's another thing that I wanted to mention that I was hoping we could do, well, we're doing this actually across the board, but like going to biweekly syncs too, so that when we do report that we've got, you know, a little bit more depth to give you than just every week. Which is great for the AI visibility, but in terms of the SEO isn't always, you know, isn't always there. So it gives us a little more, a little more time there. I'm going to be out of office on when we would normally be meeting, not next week, but the following. So it's the 27th. So I didn't know if you wanted to start that. We could meet next week and then, and then skip the following and then we'll, we'll do the, we'll start by week.

**Kezia Farnham:** Even if we are not covering, like, like performance of, you know, okay, it's gone up, it's gone down, like that kind of thing on, on a weekly basis. Because I think, you know, SEO is a little bit more, at least on the organic side, like a little bit more, takes time. You're going to have so many, so much, even when there's like high volatility, it's like, that's not going to necessarily be information that's necessarily worthwhile to hold on to. You have a signal, but not much more than that, but I think it could still be good to, like, have consultancy time, where we can jump in and solve for something if we need to.
