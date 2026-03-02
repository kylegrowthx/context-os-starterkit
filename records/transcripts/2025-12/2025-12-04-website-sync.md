# Website Sync

<metadata>
date: 2025-12-04
time: 14:45 UTC
duration: 17 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar, Kaitlin Quimby, Franco Caputo
fathom_recording_id: 106277789
fathom_url: https://fathom.video/calls/496644921
share_url: https://fathom.video/share/8Wmmubx2Xkq8RsTNLzfrNdg5FJbPWX16
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Datagrid's website development partner WonderUp identified two critical SEO issues on the newly migrated Datagrid website: duplicate pages with URL suffixes (`-1`, `-ef` etc.) causing non-indexable content, and a GA4 tagging failure preventing session tracking despite normal traffic in Google Search Console. Franco (WonderUp) has already implemented canonical tags, removed noindex tags, and added JSON schema to blog posts; he will now color-code the audit doc to show WonderUp's capacity limits and delete duplicate pages, while Vivek will investigate the GA4 issue with Kyle and request a follow-up audit from Mika once fixes are complete. The team also aligned on early-next-week newsletter distribution targeting mid-month send, and confirmed Vivek now has access to the shared event calendar for the upcoming "agent-a-thon."

---

## Context

This is a technical sync between GrowthX (represented by Vivek Shankar from content/SEO team) and Datagrid, one of GrowthX's clients, working through WonderUp (a Webflow design and development firm based in Buenos Aires). The meeting was called urgently after Vivek detected a spike in non-indexed pages on Datagrid's newly migrated website during a routine technical SEO audit. Thiago da Costa from Datagrid attended to represent the client, while Franco Caputo from WonderUp joined to discuss implementation capacity. This is part of GrowthX's delivery engagement with Datagrid, which involves SEO strategy and website optimization.

---

## Relevance

**To GrowthX Delivery:**
- Technical SEO audit identified critical issues (duplicate content, GA4 misconfig) that require cross-team investigation — Vivek must work with Kyle on GA4 setup, then request follow-up audit from Mika to validate fixes
- Client capacity assessment: WonderUp can handle duplicate deletion and canonical/noindex fixes but cannot resolve GA4 tagging (requires GrowthX technical partner involvement)
- Established clear ownership model for Datagrid site fixes with color-coded action doc

**To GrowthX Business Development:**
- Datagrid account health: site migration created technical debt but team is aligned on remediation; Vivek has direct relationship with multiple stakeholders (Thiago at Datagrid, Kaitlin at Toric, Franco at WonderUp)
- Newsletter campaign is proceeding on schedule with early-next-week draft due, mid-month send — supports content marketing narrative and event promotion for upcoming "agent-a-thon"

**To GrowthX Operations:**
- Calendar access issue flagged: Vivek did not receive calendar invite for Datagrid event calendar (expected from Rai at Datagrid); Kaitlin to resend
- Established baseline for technical SEO audit cycle: after WonderUp fixes are live, expect Mika to run follow-up audit within 1-2 weeks

---

## Overview

- **Critical SEO Issues:** The new site has two major problems: duplicate pages with URL suffixes (e.g., `-1`, `-ef`) causing non-indexable content, and a GA4 tagging failure that prevents session tracking.
- **Immediate Fixes:** Franco (WonderUp) has already implemented several fixes, including adding missing canonical tags, removing old `noindex` tags, and adding JSON schema to blog posts.
- **Clear Ownership:** Franco will use Vivek's audit doc to highlight which tasks WonderUp can and cannot handle. Vivek will then investigate the GA4 tagging failure and coordinate a follow-up audit.
- **Newsletter Plan:** The next newsletter draft is due early next week for a mid-month send, covering recent updates and upcoming events like the next "agent-a-thon."

---

## Key Topics

### Website SEO Audit Findings

  - Vivek (growthx.ai) presented findings from a technical SEO audit, prompted by a spike in non-indexed pages.
  - **Problem 1: Duplicate Pages**
      - The new site has many duplicate blog posts with URL suffixes (e.g., `-1`, `-ef`).
      - Some of these suffix pages exist without an original, causing confusion.
  - **Problem 2: GA4 Tagging Failure**
      - GA4 is not recording sessions for many new pages.
      - Google Search Console (GSC), which is tag-independent, shows normal traffic, confirming the issue is with GA4 implementation, not traffic.

### SEO Fix Plan & Ownership

  - Franco (WonderUp) outlined the fixes already implemented:
      - Added missing canonical tags.
      - Removed old `noindex` tags.
      - Unpublished the previous project and removed its GTAG/GSC traces.
      - Added JSON schema to blog posts (pending for webinars/events).
  - **Action Plan:**
      - **Franco (WonderUp):**
          - Use Vivek's audit doc to highlight tasks WonderUp can/cannot handle.
          - Delete duplicate blog posts with URL suffixes.
      - **Vivek (growthx.ai):**
          - Investigate the GA4 tagging failure with Kyle.
          - Request a follow-up audit from Mika after WonderUp's fixes are complete.

### Newsletter & Event Sync

  - **Newsletter:**
      - Goal: Mid-month send covering recent updates and upcoming events.
      - Vivek will send a draft early next week.
  - **Events:**
      - Kaitlin will add the next "agent-a-thon" (next month) to the event calendar.
      - Kaitlin is sourcing a video reel from the last "agent-a-thon" for the newsletter.
  - **Calendar Access:**
      - Vivek confirmed he now has access to the shared calendar.

---

## Action Items

**Vivek Shankar (GrowthX)**
- Send newsletter draft to Kaitlin next week
- Check GA4 tagging w/ Kyle; propose next steps

**Kaitlin Quimby (Toric/Datagrid)**
- Add next month's Agent-a-thon to event calendar
- Check GrowthX access to Datagrid event calendar; resend invite if needed

**Franco Caputo (WonderUp)**
- Update audit doc w/ color-coded actions; send to Vivek; then Vivek ask Mika rerun audit
- Delete duplicate blog posts w/ numeric suffixes; send updated list to Vivek

---

## Transcript

**Vivek Shankar:** Hey, Kaitlin.

**Kaitlin Quimby:** Hi. How are you?

**Vivek Shankar:** Good.

**Kaitlin Quimby:** Good.

**Vivek Shankar:** This was a bit impromptu, wasn't it?

**Kaitlin Quimby:** Yeah. Well, we definitely want to get those things fixed. It's just we noticed a bunch of them, so I think it's just easier to hop on a call, you know?

**Vivek Shankar:** Yeah, yeah. So, yeah, a bit of churn on our end. You know, Mara was originally supposed to take over, then she left GrowthX, so basically I'm back, so for better or worse.

**Kaitlin Quimby:** It was preemptive... Okay, Franco just messaged me. He'll be on in a second.

**Vivek Shankar:** Is he from T86?

**Kaitlin Quimby:** Yeah, he works at WonderUp.

**Vivek Shankar:** While we're waiting, I tagged Miles and I forgot the other person's name. Dov? No, Xander.

**Kaitlin Quimby:** Oh, yeah, Xander.

**Vivek Shankar:** The arrow had flagged Xander for the product updates. What we're trying to basically do is — I think I remember you saying that the newsletter would go out the middle of the month, if I'm correct?

**Kaitlin Quimby:** I mean, I think that would be ideal. You know, do a little like what's coming up and what's happened in the last 30 days.

**Vivek Shankar:** Yeah. So we were thinking of sending you a draft early next week with the aim to send it out mid-month.

**Kaitlin Quimby:** We did our agent-a-thon last month and we're going to be doing another one next month as well, which I need to put those on the event calendar. And I'm hoping I have the video reel from the one last month so that we can add it to that as well. So there's just kind of a few things I'm trying to get for you guys as well.

**Vivek Shankar:** Speaking of the calendar, did you add a team at GrowthX, and does it just show up in Google Calendar?

**Kaitlin Quimby:** Yeah, so there should have been an email and then you add it, but we added team at GrowthX. I mean, I can add individual ones, but we did add a team. Usually there's an email and it's like, "You've been shared this calendar, do you want to add?"

**Vivek Shankar:** Yeah, I didn't see it yesterday. Will it come from you or another Datagrid address?

**Kaitlin Quimby:** I think Rai was the one who sent it, but I'll take a look.

**Vivek Shankar:** Here we go.

**Kaitlin Quimby:** Hi. Wow, it's so sunny there.

**Franco Caputo:** Yeah. Sunny, hot, and humid. Summer in Buenos Aires for you.

**Kaitlin Quimby:** Nice to meet you, Vivek, by the way.

**Vivek Shankar:** Nice to meet you as well, Franco. Yeah, I kind of messaged Thiago and Thiago was like, okay, it's best to get on a call and deal with all this. I had sent a document over. I don't know if you had a chance to look at it.

**Franco Caputo:** I did. Yeah.

**Vivek Shankar:** So there's, we saw those issues on a technical audit. Not all of them are super critical. Some of them are recommendations. But what prompted it was basically we saw a spike in non-indexed pages, and during the migration, the new website seems to have a lot of URLs with a weird suffix, and they seem to be clones of existing Datagrid pages. And some of those suffix pages don't have original pages, so I don't know what's happening there. But yeah, so I just wanted to flag that for you. And also, a second issue was there seems to be a tagging problem with the new pages, because in GA4, we're not seeing any sessions being recorded for quite a lot of the pages that we've created, whereas GSC, which doesn't depend on the tag, is showing regular numbers. So I just wanted to bring that up and flag it to you.

**Franco Caputo:** Yeah, so I already kind of tried to improve and solve a lot of those issues. Like a couple of days ago when Kaitlin sent me the doc, I went over all of the pages, added the missing canonical tags, removed a couple of noindex tags. And then I also went ahead and unpublished the previous project and removed any traces of GTAG and the search console. And then also the canonical tags, just in case. Mean, unpublishing would have been enough, but I kind of deleted all traces of that. And then I also added the JSON schema to the blog posts, not yet to the webinars and events. I mean, there are a lot of pages that existed in the previous project that don't exist in the new one yet because we're working on those new designs. But beyond that, I'm not sure what else I can do or my team can do on a technical SEO level inside of Webflow to mitigate this. It seems like also some of it might be coming from the Google Analytics panel configuration, which we have limited knowledge of. Since mainly we're more of a dev and design firm, but yeah, I mean, obviously happy to support anything that we can and know about. I don't know if what we worked on is sufficient enough to start seeing some improvements and how long those changes take to be indexed.

**Vivek Shankar:** So in that talk, could you then — I'm just trying to get an idea of what WonderUp can and can't handle so that there's a section there that says "Summary of actions we recommend taking." Could you just put a simple highlight color saying, "we can do this" or "we can't do this" or whatever. I'll leave it up to you. Because the thing is, from our end, we can't do this because we're not a design agency. I just want to get an idea and then we can recommend.

**Franco Caputo:** Yeah, so this I already did. I mean, I already did this, too. Also, I guess some of the keywords probably do. I just kind of copied what was in the previous pages. But you know, since we don't own Datagrid or anything, probably Kaitlin or Thiago are best to recommend the actual descriptions and keywords. But yeah, we already did this one. I'm just going to mark the ones that we either didn't do or can't do. This one, I'm just going to mark orange. The reason being is we can do it, but the reason I haven't done this one is because those blog posts existed before. I'm not sure which ones are supposed to be the ones that need to be up. The duplicates were already up at the previous project. We could actually show... Yeah, they need to choose, but if I search, yeah, so these are probably the ones that are duplicated. They're the ones with the little suffix at the end, the weird suffix. So exactly, this one doesn't have it, whereas this one does. It seems that the content is the same. Yeah, that's what we saw, so if it's the same, I could just delete all of them. I think you can delete everything with the suffix with that weird suffix. If you guys allow it, I'm just going to make sure that I'm looking at it the right way. But yeah, all of these have a suffix. So I'm going to go ahead. I mean, first of all...

**Vivek Shankar:** Some of them have like a one as well, like one, two, EF, whatever. In case there's a number in the first URL, like we have some blogs about Primavera P6 and stuff.

**Franco Caputo:** Yeah, but you can see that I added the slot here, and I can double check. Like all of them have that one, and the reason that it's doing that is because I'm adding the suffix, the end dash. So I'm just going to take these two. Yeah, so this is TBD. I just wanted to check that. So this I already did. The only template that we have online is the blog.

**Kaitlin Quimby:** And we highlight the ones that are done in green and then ones that aren't in yellow, just so then we know. If you want to tag me, or is that you, Vivek?

**Franco Caputo:** I mean, yeah, so this one is done-ish because you have to check the title, the description.

**Kaitlin Quimby:** Added the canonicals and checked the H1s, but this is...

**Vivek Shankar:** Oh, I can... If it was copied from the old URLs, it should be fine. I don't think we had any issues with that. We can certainly check a few samples. Let me just make sure everything's fine.

**Franco Caputo:** This is, so we need to change the categories on this one. The reason I haven't done this one is because those blog posts existed before. You just need to go in and make sure that you have the right SEO title tag and meta description, and that's it. You go to page settings. But we don't have category pages on this new project. Because we're not using SEO categories, we're real-time search. This shouldn't be happening. Let me double check that.

**Vivek Shankar:** Sorry, I do have to hop on another call. So Kaitlin, just so you know, we can always rerun the audit to make sure that the action items are done. So for example, checking the metadata, et cetera, we can do that once WonderUp finishes everything. And then we can follow up on this. And meanwhile, Franco, if you have any issues or whatever, just feel free to tag me. I'm not in the Slack channel with you guys, but I'm sure.

**Franco Caputo:** Yeah, I mean, I already think I already did all of these pretty much, except these two that are more like for the Datagrid team. So I'll let you know if I've run into anything I haven't done yet.

**Vivek Shankar:** Okay. Once I get this list, I'll ask Mika to run the audit again, just to verify. And I will check internally regarding the GA4 tagging, because that's not in our wheelhouse either. I'll just check with Kyle and see what we can do about that and take next steps.

**Kaitlin Quimby:** Okay.

**Vivek Shankar:** All right. Cool. Well, Kaitlin, I'll talk to you later during our sync. Cheers, Franco.

**Franco Caputo:** Yep.

**Kaitlin Quimby:** Thank you. I'll talk to you later. Take care. Bye, guys. Bye.
