# Building out content strategy for Turnstile and Blaxel

<metadata>
date: 2025-12-15
time: 15:16 UTC
duration: 57 minutes
organizer: William Leborgne
participants: Aida Knezevic, Kathy Lam, William Leborgne
fathom_recording_id: 108713736
fathom_url: https://fathom.video/calls/507883955
share_url: https://fathom.video/share/5rWK4HNduqsfenz25MEC5DyDuhPxe75p
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Aida walked William and Kathy through the complete workflow for building content strategies: starting with Airtable as the central data repository (kickoff transcripts and competitor keyword exports from SEMrush), then using Claude to analyze the aggregated data and identify high-priority topic clusters. During a live demo with Turnstile, the team discovered a 14MB Stripe "Guide" section dataset that exceeded Airtable's 5MB upload limit, requiring file splitting, and manually filtered out 24,000 irrelevant HubSpot keywords. William provided a SEMrush tutorial showing Domain Overview, Organic Research Positions, and Keyword Magic Tool. William and Kathy agreed to independently build a Turnstile strategy using this process and compare results in a follow-up meeting scheduled for 4 PM PT / 2 PM HT.

---

## Context

This was an internal GrowthX training session where Aida Knezevic, the lead strategist, demonstrated her proprietary content strategy workflow to William Leborgne (VP of operations) and Kathy Lam (team member). The team is in delivery mode on two clients: Turnstile (a quote-to-cash software company competing directly against Stripe) and Blaxel. The immediate context is that Turnstile's kickoff call had recently concluded, and the team needed to move into the strategy-building phase. Aida chose to run a live demo using Turnstile as the example because their data was ready and their Wednesday deliverable deadline was approaching.

---

## Relevance

**To GrowthX Delivery:**
- Airtable + Claude is the approved workflow for content strategy builds. Claude is preferred over ChatGPT because it reliably processes entire CSVs without hallucinating partial results.
- Data cleaning is critical before AI analysis — irrelevant competitor keywords (e.g., HubSpot "AI video editing" for a quote-to-cash platform) must be manually filtered, and AI output (e.g., generic thought-leadership ideas) requires strategic refinement.
- Technical blockers are emerging: SEMrush exports can exceed Airtable's 5MB upload limit. The solution is to split large CSVs into smaller chunks (e.g., 20k rows each) for sequential uploads.
- Future-proofing: William and Kathy will now have hands-on experience with the workflow, reducing Aida's solo dependency for this core process.

**To GrowthX Business Development:**
- Turnstile client health is positive: they have a clear product direction (quote-to-cash), aggressive competitive positioning (direct Stripe alternative), and are moving rapidly through sales → kickoff → strategy phases.
- Blaxel is also in motion and ready for strategy work (per William's Friday deep dive with Kathy).

**To CheckThat:**
- No direct AI visibility or AEO mentions in this session, but the workflow demonstrates how GrowthX uses Claude to synthesize competitive keyword landscapes, which aligns with CheckThat's positioning as an AI visibility tool.

---

## Overview

- **Process:** The workflow uses Airtable for data storage and Claude for analysis. Claude is preferred over ChatGPT because it reliably processes entire CSVs, avoiding the partial analysis and "hallucinations" common with other models.
- **Data Prep:** The process begins by populating the client's Airtable with kickoff transcripts and competitor keyword data from SEMrush. Irrelevant data (e.g., HubSpot keywords for a finance client) is deleted to maintain focus.
- **AI Analysis:** Claude analyzes the prepared data to identify high-priority topic clusters. The output is then manually refined to ensure strategic relevance, as the AI can sometimes generate overly generic or thought-leadership-focused ideas.
- **Practice:** William and Kathy will independently build a Turnstile strategy using this process and compare their results in a follow-up meeting.

---

## Key Topics

### Content Strategy Workflow: Airtable & Claude

  - **Airtable:** Serves as the central repository for all project data.
      - **Initial Setup:** Copy the "Strategy Sprint Template" (June version).
      - **Populate Docs Tab:** Add kickoff call transcripts and company context.
      - **Populate Organic Research Tab:** Import competitor keyword data from SEMrush.
  - **Claude:** Performs the heavy lifting of data analysis.
      - **Why Claude?** It reliably processes entire CSV files, unlike ChatGPT, which often analyzes only a portion and "lies" about it.
      - **Analysis Steps:**
        1.  **Summarize Kickoff:** Use a prompt like, "Read the kickoff call transcript and summarize the key points..."
        2.  **Analyze Competitors:** Upload the `competitor URLs` CSV and prompt, "Analyze the competitor URLs CSV file... in its entirety."
        3.  **Identify Clusters:** Prompt Claude to identify high-priority topic clusters for the client based on the analysis.

### Live Demo: Turnstile Strategy Build

  - **Initial Data Gap:** The initial competitor keyword list from Hassan was missing Stripe's "Guide" section, a major source of their SEO content.
  - **Data Correction:**
      - **Stripe Data:** A new SEMrush export of Stripe's "Guide" section yielded a 14MB CSV.
          - **Problem:** Airtable's 5MB upload limit.
          - **Solution:** Split the CSV into smaller files (e.g., 20k rows each) for sequential upload.
      - **HubSpot Data:** HubSpot keywords (e.g., "AI video editing") were irrelevant for a quote-to-cash company.
          - **Action:** Filtered and deleted 24,000 HubSpot-related records from Airtable.
  - **AI Output Refinement:**
      - Claude's first attempt to identify clusters produced generic, thought-leadership-focused ideas like "Founder first revenue operations."
      - **Rationale:** This output was rejected because it didn't map to the specific, high-volume keywords needed for a growth strategy.
      - **Action:** Aida would start a new Claude conversation to reset the context and get a more relevant analysis.

### SEMrush Tutorial for Kathy

  - William provided a quick tutorial on the essential SEMrush features for this workflow.
  - **Key Tools:**
      - **Domain Overview:** Provides a high-level SEO health check (e.g., Turnstile's Authority Score is 4/100, indicating a very new domain with low visibility).
      - **Organic Research → Positions:** The primary tool for exporting competitor keywords.
          - **Process:** Filter by `Positions 1-30` and `Exclude` brand keywords to focus on high-potential, non-branded terms.
      - **Keyword Magic Tool:** Used to find keyword variations and analyze the SERP for a specific term.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Upload split Stripe guides CSVs to Turnstile Airtable; add as artifact; prompt Claude to merge and analyze

**Kathy Lam (GrowthX)**
- Contact Alice re: pod0 Claude login credentials
- Independently build a Turnstile content strategy using the demonstrated workflow

**William Leborgne (GrowthX)**
- Build a Turnstile content strategy independently (for comparison with Kathy's work)
- Schedule and send invite to Kathy for 4 PM PT / 2 PM HT follow-up meeting to compare results

---

## Transcript
**Kathy Lam:** Oh, how are you?

**William Leborgne:** This meeting is being recorded.

**Kathy Lam:** are you?

**Kathy Lam:** Good.

**Kathy Lam:** I'm going to run down and grab something to drink.

**William Leborgne:** I'll be like right back in a sec.

**William Leborgne:** No problem.

**Kathy Lam:** Okay.

**William Leborgne:** It was good.

**William Leborgne:** It was good.

**William Leborgne:** It was relaxing.

**William Leborgne:** It was exactly kind of what I needed.

**William Leborgne:** We went to these natural hot springs that are not too far away from where we live.

**Kathy Lam:** And that was incredible.

**Kathy Lam:** I felt like my shoulders relaxed for the first time in weeks.

**Kathy Lam:** That's awesome.

**William Leborgne:** Yeah, it was very needed.

**William Leborgne:** How about yours?

**Kathy Lam:** It was good.

**Kathy Lam:** We celebrated my mom's birthday and then took her to the Christmas lights.

**Kathy Lam:** And we did some festive flower arranging.

**Kathy Lam:** So, yeah, all in all, guys.

**William Leborgne:** That's lovely.

**William Leborgne:** Like a, what are those called again?

**William Leborgne:** A wreath?

**William Leborgne:** A wreath, yes.

**Kathy Lam:** Not a wreath, but flowers are just the same.

**William Leborgne:** Okay, nice.

**William Leborgne:** That's lovely.

**William Leborgne:** You said it was your mom's birthday.

**Kathy Lam:** Yeah, yeah.

**William Leborgne:** How old, can I ask?

**Kathy Lam:** How old your mom is?

**Kathy Lam:** Yeah, She's 80.

**William Leborgne:** Hmm.

**William Leborgne:** Okay, so same range as my parents.

**William Leborgne:** My dad is just turning 80 next year.

**Kathy Lam:** Oh, cool.

**William Leborgne:** Yeah, yeah.

**William Leborgne:** Yeah, it's that time of their lives where you are really starting to think like, I got to be close to them.

**Kathy Lam:** Yeah, you need spend more time and everything.

**William Leborgne:** Yeah, yeah, exactly.

**William Leborgne:** Exactly.

**William Leborgne:** I know we talked briefly about this, but I don't think you ever told me what was the impetus for you wanting to move to Hong Kong.

**Kathy Lam:** Oh, yeah.

**Kathy Lam:** A couple things.

**Kathy Lam:** think one was my in-laws are getting older.

**Kathy Lam:** So Peter, my husband, is the only child.

**Kathy Lam:** So it's partially to do that.

**William Leborgne:** Yeah.

**Kathy Lam:** And yours was to stay closer to your dad, right?

**William Leborgne:** Yeah, mean, both of them.

**William Leborgne:** My parents were still together.

**Kathy Lam:** Oh, nice.

**William Leborgne:** Great.

**William Leborgne:** So that's part of

**William Leborgne:** It's to be close to them.

**William Leborgne:** Is that all the part just because you like Hong Kong or?

**Kathy Lam:** Well, I'm kind of like a longevity hacker.

**Kathy Lam:** Okay.

**Kathy Lam:** one of the things they say is like, it's good for you to be put in like a little bit of pressure or a little bit of like.

**William Leborgne:** Discomfort.

**Kathy Lam:** Discomfort, exactly.

**Kathy Lam:** And me having to relearn Cantonese again.

**Kathy Lam:** And then it's also extremely kind of warm there, as you know.

**William Leborgne:** And humid.

**Kathy Lam:** Yes, yes.

**Kathy Lam:** And so I was like, oh, this would be an interesting change.

**Kathy Lam:** And it's one of these things where it's not like a, you make this change.

**Kathy Lam:** And then if you don't like the change, you can't back out.

**Kathy Lam:** I feel like it's reversible because you don't die.

**Kathy Lam:** You do it.

**Kathy Lam:** And yeah, so it's kind of interesting.

**Kathy Lam:** I feel like they on average have like the longest living people.

**William Leborgne:** So I'm like.

**William Leborgne:** Oh, I should go check out what that is all about.

**William Leborgne:** I have a feeling it's the diet.

**Kathy Lam:** Like, you eat so good in Hong Kong.

**Kathy Lam:** It's very fresh, yeah.

**William Leborgne:** How about yourself?

**Kathy Lam:** Besides spending more time with your parents?

**William Leborgne:** I miss living in Europe, to be honest.

**William Leborgne:** Like, I have lived over a decade in the U.S., and I'm really glad I did.

**William Leborgne:** And it changed me in many ways, very positive ways, some less positive.

**William Leborgne:** I did become a bit of a workaholic at times, and my wife has had to, like, pull me back from that.

**William Leborgne:** But, I mean, I feel like I did really benefit from those years there.

**William Leborgne:** But I think at my core and my heart, I am more European than I am American.

**William Leborgne:** And I've always felt, no matter how long I lived there, I always felt like a foreigner.

**William Leborgne:** I still felt not connected fully and in the States.

**Kathy Lam:** Yeah.

**Kathy Lam:** Yeah, exactly.

**Kathy Lam:** It's weird because there's a bunch of different things that make it not make sense.

**William Leborgne:** Like I live in the Bay Area, but you drive all over the roads here.

**Kathy Lam:** It's like very bumpy, like a third world.

**Kathy Lam:** And you're like, this is one of the richest place.

**Kathy Lam:** And you would think that they would have roads, right?

**William Leborgne:** But they don't.

**Kathy Lam:** And then the other thing is like health care seems to be something that should be like given to everyone just because it's it's like the it's as important as an army.

**William Leborgne:** Right.

**William Leborgne:** Because these are totally right.

**Kathy Lam:** Like these things don't make sense.

**William Leborgne:** Yeah.

**William Leborgne:** Especially you like you're Canadian.

**Kathy Lam:** Right.

**Kathy Lam:** Originally.

**William Leborgne:** Yeah.

**William Leborgne:** So for you, you're the same as me.

**William Leborgne:** You're like, I know what another world looks like where where people where the government actually does take care of the health of their people.

**Kathy Lam:** Although it's hurting there, too.

**Kathy Lam:** Morning.

**Kathy Lam:** Oh, hi, Ada.

**Kathy Lam:** It's actually not working.

**Kathy Lam:** Good afternoon.

**Aida Knezevic:** Hi.

**Aida Knezevic:** Hi.

**Aida Knezevic:** Sorry I'm late.

**Aida Knezevic:** My cat made a mess in the part of my apartment where his bathroom is.

**Kathy Lam:** So I was cleaning it and I lost track of time.

**William Leborgne:** No worries.

**William Leborgne:** That's not fun.

**Kathy Lam:** I hope the cat is okay, though.

**Aida Knezevic:** No, he's fine.

**Aida Knezevic:** He's just, you know, he tries to climb things.

**Aida Knezevic:** He doesn't, like, he's blind in one eye and he has around, like, maybe 50% vision in his other eye.

**Aida Knezevic:** But that doesn't stop him from anything.

**Aida Knezevic:** So he gets into accidents.

**Aida Knezevic:** All right.

**William Leborgne:** Cool.

**William Leborgne:** Well, yeah, the purpose of this, as we kind of discussed, is just to, as best you can, in whatever form you think makes sense, to walk us through the process of working in Airtable and creating a content strategy once you're at the place to do that.

**William Leborgne:** I think we're going to do a live example.

**Aida Knezevic:** With Turnstile?

**Aida Knezevic:** Or BlackSoul?

**William Leborgne:** Yes.

**Aida Knezevic:** I think Turnstile is the one that's ready.

**Aida Knezevic:** I'm opening their air table right now.

**William Leborgne:** Yeah.

**William Leborgne:** Or BlackSoul, because BlackSoul is...

**William Leborgne:** I think BlackSoul is also ready.

**Aida Knezevic:** It could be.

**William Leborgne:** I did the Prog Deep Dive on Friday with Kathy.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** I have Turnstile open, and they're also on Wednesday, so maybe it's just better if we get started with them.

**William Leborgne:** Cool.

**William Leborgne:** Let's do it.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Let me just close all these windows.

**William Leborgne:** How was your weekend, by the way?

**Aida Knezevic:** We forgot to ask.

**Aida Knezevic:** It was good.

**Aida Knezevic:** It was good.

**Aida Knezevic:** I went and visited my boyfriend, and yeah, it wasn't like anything special.

**William Leborgne:** Are you guys doing long distance?

**Aida Knezevic:** It's remote.

**Aida Knezevic:** It's medium distance.

**Aida Knezevic:** It's like...

**Aida Knezevic:** Same distance, got it.

**Aida Knezevic:** Yeah, it's like we're three hours away by car.

**Aida Knezevic:** Gotcha, okay.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** And my previous manager, he joked, like, you have a remote job, you have a remote relationship.

**Aida Knezevic:** Everything's remote.

**Aida Knezevic:** Okay, I'm just opening stuff here.

**Kathy Lam:** Yeah, cool.

**Kathy Lam:** Well, I was going to ask, is that where you open the, what is it, Airtable from the strategy sprint doc or, like, where?

**Aida Knezevic:** I think if you go, I think if you go to Airtable and then you just look up turnstile, you should be able to find it.

**Kathy Lam:** Okay, cool.

**William Leborgne:** Yeah.

**William Leborgne:** Who creates that first instance in Airtable?

**William Leborgne:** If you want to start from zero.

**Aida Knezevic:** Okay, he does it.

**Aida Knezevic:** There's a template.

**Aida Knezevic:** You can just, I think it's, like, the June version.

**Aida Knezevic:** It's basically strategy sprint template, and I think it was made in June, and then you just copy that.

**Aida Knezevic:** I see.

**William Leborgne:** Okay.

**Aida Knezevic:** Okay, here's turnstile.

**Aida Knezevic:** What do we have here?

**Aida Knezevic:** We have nothing in the product documentation.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So, I start by just, what is this?

**Aida Knezevic:** Where's Fathom?

**William Leborgne:** Oh, yeah, you have the same problem.

**William Leborgne:** You can't do anything with Fireflies until you set up an account.

**William Leborgne:** So, you have to, like, yeah, you have to create an account with them, and they're going to ask you a bunch of questions.

**William Leborgne:** It's annoying.

**William Leborgne:** Why?

**Aida Knezevic:** Do we not have something in Fathom?

**Aida Knezevic:** I'm sure Fathom recorded it.

**Aida Knezevic:** Let me find it.

**Aida Knezevic:** Maybe if I log in with the Teams account, I can find it.

**Aida Knezevic:** Do you have the transcript, William?

**William Leborgne:** Of, um, maybe?

**William Leborgne:** Let me check.

**William Leborgne:** Because in the very beginning, my Fathom was not working, so let me just...

**Aida Knezevic:** Okay, I got it.

**Aida Knezevic:** Yeah, I'm in.

**Aida Knezevic:** Um, okay, let's see if I can copy the transcript.

**Kathy Lam:** Do you also want the sales handoff transcript or just the, uh, main one?

**Aida Knezevic:** Uh, I'll take a look.

**Aida Knezevic:** Hold on.

**Aida Knezevic:** Transcript, okay.

**Aida Knezevic:** Let's do markdown.

**Aida Knezevic:** I don't like that I have to download it.

**Aida Knezevic:** I just like to copy.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Copy and paste.

**Aida Knezevic:** I know this sounds like a super, like, spoiled, but I'm used to just copying and paste.

**William Leborgne:** I need to let my dog in.

**Aida Knezevic:** Okay, so we're in Claude.

**Kathy Lam:** Oh, okay, in Claude.

**Aida Knezevic:** Got it.

**Aida Knezevic:** See, now this is annoying.

**Aida Knezevic:** Now I have to open the markdown file.

**Aida Knezevic:** I have to, like, copy and then paste everything here.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right, so we have to kick off call transcript.

**Aida Knezevic:** Great.

**Aida Knezevic:** And we go to docs.

**Aida Knezevic:** Let's copy the company context.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Thank you.

**William Leborgne:** Oh, interesting.

**William Leborgne:** When you copy-paste it, it just automatically turns into Markdown?

**Aida Knezevic:** Yeah, you can copy as markdown. It puts in Markdown.

**Aida Knezevic:** That's cool.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** So it's actually a lot better.

**Aida Knezevic:** You don't have to upload anything.

**Aida Knezevic:** That's good to know.

**Aida Knezevic:** Okay.

**Aida Knezevic:** And then I don't add the writing guidelines because they have no, like, really, like, real bearing on the strategy most of the time.

**Aida Knezevic:** And then I will… You do or you don't?

**Aida Knezevic:** Sorry.

**Aida Knezevic:** don't.

**Aida Knezevic:** I don't because the writing guidelines are just supposed to influence, like, the content output, like, the style and the tone.

**Aida Knezevic:** So let's go to…let's see what's in the prior context from sales.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Kathy Lam:** Wow, they don't even have a CMS yet.

**Kathy Lam:** So I wonder how they're going to change our content into something on the web.

**William Leborgne:** I don't know.

**William Leborgne:** I thought they did.

**William Leborgne:** I thought they were using, what's the CMS you guys all use?

**William Leborgne:** Synergy or something?

**Aida Knezevic:** So this is interesting.

**Aida Knezevic:** So this is, like, I'm not, I wouldn't, like, add this to Claude, but this is, like, interesting.

**Aida Knezevic:** So they're going up against Stripe, need creative long-tail strategy.

**Aida Knezevic:** This is, like, good to know from the sales handoff.

**Aida Knezevic:** Docs, opinionated platform, opinionated product.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Stripe is like the elephant.

**Aida Knezevic:** All right.

**Aida Knezevic:** I know that we have Stripe in here, but it's okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Now, one thing about Stripe, yeah, this is what I was afraid of.

**Aida Knezevic:** Stripe has a lot more content on their site that Hassan was unaware of.

**Aida Knezevic:** And it's the guide section.

**Aida Knezevic:** And this is their SEO content.

**Aida Knezevic:** So, it's good that we're doing this live because you can actually see like how it's like back and forth, back and forth.

**William Leborgne:** So, now you're going to have to go and go to the Stripe and pull your own CSV, okay.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** So, let's go to organic research.

**Aida Knezevic:** And this doesn't take a long time, but it's good.

**Aida Knezevic:** So, you know how to do it.

**Aida Knezevic:** Like if Hassan misses something, you know how to add it in.

**Aida Knezevic:** So, let's go to, I think it's positions, right?

**Aida Knezevic:** It's positions, okay.

**Aida Knezevic:** So, yeah, they're ranking four.

**Aida Knezevic:** Hmm, it should be a lot more.

**William Leborgne:** Yeah, it's less than I expected.

**Aida Knezevic:** No, it's not guides.

**Aida Knezevic:** It's something else. Resources, Resources more.

**Aida Knezevic:** And then they have, like, billing.

**Aida Knezevic:** Look at this.

**Aida Knezevic:** Wow.

**William Leborgne:** Yeah, so...

**Aida Knezevic:** all articles?

**Aida Knezevic:** Yes.

**Aida Knezevic:** So, billing.

**Aida Knezevic:** And then we go to pricing experiments.

**William Leborgne:** These are all articles.

**Aida Knezevic:** Yeah, this is like an encyclopedia.

**Aida Knezevic:** All right.

**Aida Knezevic:** So we need to add guides.

**William Leborgne:** Let's do...

**William Leborgne:** Do you remove anything with Stripe first?

**Aida Knezevic:** Yeah, so let's do informational commercial first. Articles, okay.

**Aida Knezevic:** Exclude keyword containing stripe.

**Aida Knezevic:** They're a super new domain.

**Aida Knezevic:** I don't want to actually filter the keyword difficulty yet.

**Aida Knezevic:** Positions, let's look at 1 through 30.

**William Leborgne:** So this is where they appear in the search results.

**Aida Knezevic:** Okay.

**William Leborgne:** So it's about half.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So let's export the CSV.

**Aida Knezevic:** I'll call it Stripe guides.

**Aida Knezevic:** And now we have resources more.

**Aida Knezevic:** Yes, more like it.

**Aida Knezevic:** This is 60,000 keywords.

**Aida Knezevic:** Oh, wow.

**Aida Knezevic:** This is going to be way too big for Airtable.

**Aida Knezevic:** So we're going to have to break it up into because Airtable has like a five megabyte upload limit.

**Aida Knezevic:** So let's see how much is this going to be.

**Aida Knezevic:** It's like 14 megabytes.

**Aida Knezevic:** How do we want to do this?

**Aida Knezevic:** Let's do...

**Aida Knezevic:** The only option is to upload it into Google Sheets and then just, like, manually divide it.

**Aida Knezevic:** But maybe I did it already.

**Aida Knezevic:** Let me see.

**Aida Knezevic:** Because I have done...

**Aida Knezevic:** I analyzed Stripe for a different competitor.

**Aida Knezevic:** No.

**Aida Knezevic:** Okay.

**Kathy Lam:** Oh, wow.

**Kathy Lam:** Oh, this is Cloudflare Turnstile.

**Kathy Lam:** Wow, they're not at the top of my search, even when I search for their name, unless I use Cloudflare in front of it.

**Aida Knezevic:** Yeah, I think they have zero presence.

**Kathy Lam:** And it doesn't help that there's like a band name turnstile.

**William Leborgne:** Oh.

**Kathy Lam:** Yeah, that came up.

**William Leborgne:** Sorry.

**William Leborgne:** I'm really not sure about HubSpot being on here.

**Aida Knezevic:** Yeah, me neither.

**Aida Knezevic:** I really don't think.

**William Leborgne:** I don't, I'm like looking at these keywords.

**Aida Knezevic:** These are not relevant keywords.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** I mean, a lot of times that there's irrelevant keywords in here, but I just think that having HubSpot in here might muddy the waters a little bit.

**Aida Knezevic:** However, we will like filter anything out that's irrelevant in Cloud.

**Aida Knezevic:** So, I don't know.

**Aida Knezevic:** I think they mentioned HubSpot. But I'm not sure what the context was.

**William Leborgne:** He said that he was an SEO competitor, not a direct competitor, which I understand the concept, but I'm looking at the keywords, and this is a, Turnstile is a cash, you know, a quote-to-cash company.

**William Leborgne:** It's basically managing your finances, right, for your company.

**William Leborgne:** And I'm seeing, like, AI video editing, AI transparency, viral content.

**William Leborgne:** This is all HubSpot stuff.

**William Leborgne:** B2B influencer marketing, like, none of this relates to, I think we need to just remove all the HubSpot stuff.

**William Leborgne:** Like, none of these keywords make sense to me.

**William Leborgne:** Shark Tank logo.

**Aida Knezevic:** Yeah, I think we can delete it.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So did you see how I did it?

**William Leborgne:** So I just filtered by domains, entered HubSpot.

**Aida Knezevic:** Yeah, so you just go, like, apply a filter, and then you can say where domains contains HubSpot, and then we'll just delete.

**William Leborgne:** All of them.

**Aida Knezevic:** Okay.

**Aida Knezevic:** 24,000 records.

**Aida Knezevic:** Which is good because we need, we need the space, and then just check the URLs, yeah, because they're not, they're supposed to be deleted from here as well, the keywords at the very least.

**Aida Knezevic:** Yeah, so now you have to, like, delete the, um, the URLs from here as well, so let's just, okay.

**Aida Knezevic:** This is all HubSpot. So we can delete all of this and remove the filter.

**Aida Knezevic:** All right, so let's go back to the keywords.

**Kathy Lam:** TouchBee might actually be correct.

**William Leborgne:** Yeah, TouchBee is okay.

**Aida Knezevic:** Yeah, yeah, I'm just deleting the URLs that are, like, irrelevant.

**Aida Knezevic:** I just noticed that they were, like, unhelpful.

**Aida Knezevic:** Okay, so let's upload the guides.

**Aida Knezevic:** Okay, so you have to exclude the first row in import, and then we map this.

**Aida Knezevic:** So intent, map it to keyword intents, volume, search volume, keyword difficulties, keyword difficulty, cost per click.

**Aida Knezevic:** And then pages will be URL.

**Aida Knezevic:** Or just import.

**William Leborgne:** Looks like your screen froze for me.

**William Leborgne:** Maybe it's just me.

**William Leborgne:** Is it also frozen for you, Kathy?

**William Leborgne:** Oh, there we go.

**Kathy Lam:** The little wheel thing.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** In the meantime, over at the Stripe spreadsheet.

**Aida Knezevic:** So we need to, like, I need to turn this into multiple.

**Aida Knezevic:** Let's just duplicate.

**Aida Knezevic:** Because we need to chop up this spreadsheet. It's 14 megabytes, and we can't upload anything over 5 megabytes into Airtable.

**Aida Knezevic:** So we need to kind of chop it up.

**Aida Knezevic:** So let's try three and see what happens.

**Aida Knezevic:** All right.

**Aida Knezevic:** In the meantime, the Stripe stuff is uploaded here.

**Aida Knezevic:** So right now what we're going to do is we're just going to copy these URLs.

**Aida Knezevic:** Let's go back.

**Aida Knezevic:** We're just going to copy them and then paste them into the URL column, which is connected to this column.

**William Leborgne:** So these keywords are going to appear in the URL tab.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So that's how you kind of, that's how we're able to see, like, what are the keywords that a URL is ranking for?

**Aida Knezevic:** And it makes it easier to analyze it for.

**William Leborgne:** For the growth strategy.

**Aida Knezevic:** Okay.

**Aida Knezevic:** It's not responsive.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Let's go back here.

**Aida Knezevic:** So we have how many keywords?

**Aida Knezevic:** Like 40,000.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Let's try to do 20,000 for sheet.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So this is the last one.

**Aida Knezevic:** Okay.

**William Leborgne:** Our computer is struggling from so much information.

**Aida Knezevic:** I know, and it's supposed to be a MacBook, but it's like, okay, this is ready.

**Aida Knezevic:** So now you can see, like, URL tab is filled out, and then you just have to label it as external because these are all external URLs.

**William Leborgne:** What would be an internal URL?

**William Leborgne:** If you were, like, their URL.

**Aida Knezevic:** turnstile.

**Aida Knezevic:** Yeah, but honestly, I've been excluding it because it just, like, especially if we have, like, a ton of direct competitors and there's a lot of keywords in here, it's just taking up space.

**Aida Knezevic:** Okay, so where the...

**Aida Knezevic:** This is, like, okay.

**Aida Knezevic:** So what I'm gonna do is...

**Aida Knezevic:** Let's upload this later, and we'll just...

**William Leborgne:** So just to save us some time.

**Aida Knezevic:** Sure.

**Aida Knezevic:** Yeah, so I will...

**Aida Knezevic:** Well, let's just download the URL tab, and then I can upload the Stripe stuff later.

**Aida Knezevic:** So, no, not import.

**Aida Knezevic:** Okay, so in the URL tab, you go to GridView, download CSV, and we just go to type competitor URLs, and then let's just upload it here.

**Aida Knezevic:** Okay, so we can get started, and I'm just going to use, like, really basic prompts right now, but you can, you know, like, tweak them.

**Aida Knezevic:** So we can get started with, read the kickoff call transcript, and summarize the key points we need to know as we...

**Aida Knezevic:** build out their content strategy.

**Aida Knezevic:** Okay, so this is like pretty basic, but it could get us started.

**Aida Knezevic:** Claude is, like I said, Claude is a lot better at this stuff than ChatGPT.

**Aida Knezevic:** Claude is just able to consolidate information better.

**Aida Knezevic:** contextualize more information and, like, Claude will, if you give it, like, a huge CSV file, more, like, I think I've only had once or twice, like, a situation where it didn't analyze the whole file.

**Aida Knezevic:** It just looked at, like, a couple of competitors.

**Aida Knezevic:** But ChatGPT, like, its MO is it's going to, like, analyze, like, a third of the file and then, like, try to not tell you that's what it did.

**Aida Knezevic:** So, okay, so, yeah, it gives you, this is, like, the summary that I read.

**Aida Knezevic:** Hold on, let me just connect my charger.

**Aida Knezevic:** So this is, like, the summary doc that I, this is, like, the summary section that I add at the top of every content strategy.

**Aida Knezevic:** This is for us to understand what they want and also for the client to be reminded of what they told us.

**Aida Knezevic:** So, okay.

**Aida Knezevic:** So yeah, they've been unintentionally in stealth, gearing up for a public press launch, going from sales-led to marketing-led.

**Aida Knezevic:** So we already know, okay, one of the clusters has to be competitive comparisons and alternatives.

**Aida Knezevic:** That makes our job easier.

**Aida Knezevic:** It has to be like best of listicles, stripe alternatives.

**Aida Knezevic:** Like we have to like tackle all of those.

**Aida Knezevic:** So we have like the core problem.

**Aida Knezevic:** this is like their customers, clarity, triggers that drive adoption.

**Aida Knezevic:** All right.

**Aida Knezevic:** So I'm not going to read through all of this right now, but I typically do.

**Aida Knezevic:** And Claude will kind of always try to give you like actionable takeaways.

**Aida Knezevic:** And sometimes I will tell it not to give me actionable takeaways because I'm just looking for it to summarize.

**Aida Knezevic:** Like I don't want a strategy, like I'm not looking for a strategy from Claude.

**Aida Knezevic:** So, um, you just kind of, you can tell it like just summarize, don't give me action steps because it takes him longer to like.

**Aida Knezevic:** It takes it longer to process.

**Aida Knezevic:** So what I will do is now is I will tell Claude to read and summarize the competitor URLs tab.

**Aida Knezevic:** So you can use a prompt like analyze the competitor URLs CSV file in the project documentation in its entirety.

**Aida Knezevic:** Thank you so much.

**William Leborgne:** By the way, don't know if this is helpful, but they just this morning, they sent the buyer personas.

**Aida Knezevic:** I don't know if you want to add that.

**Aida Knezevic:** We should, yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** And we need to update the artifacts as well.

**William Leborgne:** Yeah, I'm going to put it in the chat here so that you can get it quickly.

**Aida Knezevic:** Okay, so using a prompt like this.

**Aida Knezevic:** And then sometimes it might, okay, found the file.

**Aida Knezevic:** Sometimes it's unable to find the file, especially if you added, uploaded the file midway through the conversation.

**William Leborgne:** So you have to start another conversation.

**Aida Knezevic:** But Claude can pull like reference previous conversations in the same project.

**Aida Knezevic:** So you shouldn't have issues with that.

**Aida Knezevic:** All right.

**Aida Knezevic:** So now it's like analyzing and it takes quite a bit to do this.

**Aida Knezevic:** And sometimes it might fail.

**Aida Knezevic:** So you have to repeat.

**Aida Knezevic:** The process, but you can kind of see like what it, what's it doing.

**William Leborgne:** Out of curiosity, why do we rely more on Claude than on ChatGPT or even on Gemini?

**Aida Knezevic:** I don't know about Gemini.

**Aida Knezevic:** Claude is just, was Marcel's preference and I've used ChatGPT for both, for this type of work.

**Aida Knezevic:** And Claude is more trustworthy.

**Aida Knezevic:** ChatGPT, like I'll give it a CSV file and it will process like a third of it.

**Aida Knezevic:** And then it's going to tell me, like, try to summarize things.

**Aida Knezevic:** And I can tell that I didn't look at the whole file and it lies.

**Aida Knezevic:** Like, so with Claude, that has happened only like once or twice, but it will typically, and it will give you, like, it will tell you, like, I've analyzed this file with this many URLs.

**Aida Knezevic:** So, you know, okay, it read the whole file.

**Aida Knezevic:** So it's a lot better.

**Aida Knezevic:** Okay.

**Aida Knezevic:** In the meantime, let's, uh, let's go here.

**Aida Knezevic:** Let's turn.

**Kathy Lam:** If I log in as myself, should I be able to see this chat, or do I need to log in as T?

**Aida Knezevic:** You need to log in as pod0.

**Kathy Lam:** Oh, pod0.

**Kathy Lam:** Okay, so I need to add pod0's Gmail thing, too.

**Aida Knezevic:** I think, so we have a login.

**Aida Knezevic:** The login details should be in 1Password for pod0.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** And then, if you've been added to pod0 by Yousef, you will get, like, a login link to your email inbox, and then you should be able to log in.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** No worries.

**William Leborgne:** Boom.

**Aida Knezevic:** Is it done?

**Aida Knezevic:** All right, so now it's creating like a comprehensive analysis document, and yeah, obviously, like for the Stripe analysis, we want to upload the, you can just upload it as a separate artifact in the project documentation, just like Stripe URLs, and then you can just tell Quad, analyze the Stripe URLs, add it to this existing competitor analysis.

**Aida Knezevic:** Okay, so we have, it's already kind of like for Stripe, we have like the primary topic clusters, positioning high-volume keyword examples.

**Aida Knezevic:** Typically in the past, I would tell it like provide keyword examples, but it seems like it has almost learned that I want keyword examples.

**Aida Knezevic:** And yeah, these clusters are like pretty high level, so you already have like a really good idea of like what is all of the content out there and like what is relevant for for turnstile based on their product and like their goals.

**Aida Knezevic:** So yeah, let's just wait a little while for the analysis to be ready.

**Aida Knezevic:** Let's see.

**Aida Knezevic:** Hmm.

**Aida Knezevic:** Why?

**Aida Knezevic:** Okay.

**Aida Knezevic:** That's great.

**Aida Knezevic:** Oh, no, wait.

**Aida Knezevic:** So sometimes it will like say that it lost the connection, but the analysis is more or less complete.

**Aida Knezevic:** So yeah, so this is ready.

**Aida Knezevic:** Super.

**Aida Knezevic:** Sure.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So it didn't, it didn't throw an error.

**Aida Knezevic:** All right.

**Aida Knezevic:** So it gives you like a breakdown of.

**Aida Knezevic:** Like, this is, like, 1,400 competitor URLs extracted from organic search data, blah, blah, blah, blah.

**Aida Knezevic:** So now you have, like, and I would, like, you can add this to the content strategy doc.

**Aida Knezevic:** Obviously, we want to remove anything that isn't helpful for the client, especially, like, you know, like, if the AI is just going into, like, too many details or, like, trying to provide strategic recommendations, I will just, or, like, even just, like, when it's, like, drawing conclusions about Stripe's content strategy, I'm very careful about, like, making these types of high-level conclusions from just using AI because it's, like, we're just giving them a small portion of their website.

**Aida Knezevic:** So it's, like, pretty hard to, like, conclude their entire content strategy.

**Aida Knezevic:** But, so now we have, like, okay, what are the, like, the primary topic clusters for each competitor?

**Aida Knezevic:** And from here, what I would do is I would prompt Claude to help me understand, okay, what are the, like, topic clusters that competitors cover?

**Aida Knezevic:** That would be important for turnstiles.

**Aida Knezevic:** So that turnstiles should cover as part of their, like, growth strategy.

**Aida Knezevic:** So let's just use something like, okay, looks like a good prompt here.

**Aida Knezevic:** Again, this is, like, pretty vague because we didn't have time to go through, like, this whole summary.

**Aida Knezevic:** But yeah, it's basically the point here is to get, is to understand like what clusters from the competitors are relevant for turnstile.

**William Leborgne:** It looks like it's rereading the entire thing though.

**William Leborgne:** Don't you want it to just read your analysis document?

**Aida Knezevic:** Yeah, it should have access.

**Aida Knezevic:** Hold on.

**Aida Knezevic:** Yeah, I guess it doesn't think it has access to this markdown file.

**Aida Knezevic:** Typically, we'll go through like the previous file.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Okay, here the topic cluster turns down needs to capture, all right.

**Aida Knezevic:** Founder first revenue operations.

**Aida Knezevic:** Yeah, I already don't like this.

**Aida Knezevic:** Because it's too, like, too thought leadershipy.

**Aida Knezevic:** So we need to understand, okay, like, is it SaaS finance operations?

**Aida Knezevic:** Is it billing and invoicing?

**Aida Knezevic:** Like, it should be mapped to the, like, the primary topic clusters in the content gap analysis.

**Aida Knezevic:** See, like, this is, like, way too, like, no, absolutely not.

**Kathy Lam:** Yeah, it's like taking direction from the actual first conversation rather than looking at the analysis.

**Kathy Lam:** It's like, stop being smart.

**Aida Knezevic:** Yeah, it's like, I didn't ask for this.

**Aida Knezevic:** Like, I am smarter than you.

**William Leborgne:** Yeah, okay. For now.

**Kathy Lam:** Yeah.

**William Leborgne:** Until AGI suddenly appears.

**Aida Knezevic:** Analysis of better content, especially topic clusters.

**Aida Knezevic:** Identify clusters that are high and medium priority for turnstile to capture for their work content strategy.

**Aida Knezevic:** Okay, let's see if this is going to be better.

**Aida Knezevic:** I only have like a couple of, like I have to jump in four minutes because I have a customer call.

**William Leborgne:** This is already really helpful.

**Aida Knezevic:** We can, you know, we'll just, I mean, I basically showed you, I showed you like what I do.

**Aida Knezevic:** And then from here, it's.

**Aida Knezevic:** It's just you, like, you kind of, like, trying to play around with it, because you already know what you're supposed to do.

**Aida Knezevic:** Like, you have, you know, like, what are the, like, you know what you're looking for.

**Aida Knezevic:** Okay, let's see.

**Aida Knezevic:** Again, like, founder first revenue operations, where does this come from?

**Aida Knezevic:** Okay.

**Aida Knezevic:** We might need to start a new conversation with Claude in order to get, like, around this.

**Aida Knezevic:** But you can also kind of, like, you already, this is, like, already super valuable.

**Aida Knezevic:** Like, you've saved a ton of time, because now you don't have to, like, these URLs manually.

**Aida Knezevic:** You know what the competitors are covering.

**Aida Knezevic:** So, yeah, you can, like, continue this conversation, or you can just start a brand new one.

**Aida Knezevic:** I will upload the Stripe stuff into Airtable after my customer call.

**Aida Knezevic:** And then you should also have access to that so you can, like, get started.

**Aida Knezevic:** But, yeah, this is basically what I do.

**Aida Knezevic:** And then for any additional competitor that you add, you can, like, provide a copy.

**Aida Knezevic:** You have this analysis and then prompt Claude and tell him, like, just analyze this additional URL file with this additional competitor data, add it to the existing competitor analysis, and then you can just kind of build on it.

**William Leborgne:** So you're, okay, so you're really not doing that much in Airtable itself?

**Aida Knezevic:** The Airtable, no.

**William Leborgne:** So we're not doing that much in Airtable, no.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** But there is, sorry, real quickly, there is another step afterwards when you're presented to them where you do actually have in Airtable a bunch of opportunities, right?

**William Leborgne:** Like, you're like, here are the keywords.

**William Leborgne:** That's a different step.

**Aida Knezevic:** Yeah, it's a different step.

**Aida Knezevic:** Right now we want to get to the strategy, so we want to identify the topic clusters, and then I can...

**William Leborgne:** And then you go on to the next step.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So once that is ready, then you can, like, drop me the content strategy, and I can show you, like, how to kind of, like, map the assignments and, like, add all of that stuff to Airtable.

**William Leborgne:** But right now we have to build a strategy.

**William Leborgne:** Okay, got it.

**Aida Knezevic:** All right.

**Aida Knezevic:** Okay, well, I hope this was helpful.

**William Leborgne:** Yeah, no, absolutely.

**William Leborgne:** Even the foibles.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** It's actually better that we had these, like, issues because they come up quite frequently, and it's better for you to, like, understand, like, like, double-checking the competitors, stuff like that.

**Aida Knezevic:** It's always helpful.

**Aida Knezevic:** Yeah.

**William Leborgne:** All right, well, I will...

**William Leborgne:** do you want to stay on for a minute?

**Kathy Lam:** Yeah, do.

**Kathy Lam:** Actually, I have a question for you, too.

**Aida Knezevic:** Okay, all right.

**Aida Knezevic:** Well, I'll see you guys later.

**William Leborgne:** Bye.

**William Leborgne:** See you shortly.

**Kathy Lam:** Howdy.

**William Leborgne:** Howdy.

**William Leborgne:** So, yeah, yeah.

**William Leborgne:** Sorry, why don't you start?

**Kathy Lam:** Where were some of your questions?

**Kathy Lam:** No, I think I was capturing all that.

**Kathy Lam:** I'm having some trouble logging into the whole PodZero thing.

**Kathy Lam:** was wondering if you might, like, have a second to help me.

**William Leborgne:** Yes, I can definitely try to help.

**William Leborgne:** I did it.

**William Leborgne:** So,

**William Leborgne:** I think.

**William Leborgne:** I don't remember how.

**Kathy Lam:** Because I was looking for the login to pod zero, and I got, like, a bill that said, oh, like, user added, and that was all I got, I think.

**William Leborgne:** But do you have the login information for pod zero?

**William Leborgne:** Okay, I think that's the first thing.

**William Leborgne:** So, hold on.

**Kathy Lam:** I got all these, like, welcome to pod zero, and I'm like, thanks.

**Kathy Lam:** I feel great.

**Kathy Lam:** But I'm like, let me in.

**William Leborgne:** Okay.

**William Leborgne:** Claude.

**William Leborgne:** Claude.

**William Leborgne:** Zero.

**William Leborgne:** Zero.

**William Leborgne:** Zero.

**William Leborgne:** Zero.

**William Leborgne:** Zero.

**William Leborgne:** Hold on.

**William Leborgne:** How am I?

**William Leborgne:** I can't remember how I did it now.

**William Leborgne:** Okay, if I just jump into Claude, how am I logged in?

**William Leborgne:** Let just check.

**William Leborgne:** Okay, I'm already logged into pod zero.

**William Leborgne:** Okay, so I feel like I just got the login information for pod zero, but I'm not seeing it in one pass.

**Kathy Lam:** Should I just ping either...

**William Leborgne:** Alice?

**William Leborgne:** Alice or Yusef?

**Kathy Lam:** Yeah.

**Kathy Lam:** Probably Alice.

**Kathy Lam:** Okay, cool.

**Kathy Lam:** I will do that.

**Kathy Lam:** All right.

**Kathy Lam:** That was most of it besides going, oh, I was overwhelmed.

**William Leborgne:** Yes.

**William Leborgne:** Also, I mean, just a lesson.

**William Leborgne:** Level set.

**William Leborgne:** And please don't take any offense because I don't know what you know when you don't know.

**Kathy Lam:** Have you used SEMrush much?

**Kathy Lam:** A little, but not as much as that.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** Okay.

**William Leborgne:** So maybe the first step is for us to just go through SEMrush together briefly.

**William Leborgne:** okay.

**Kathy Lam:** Is that okay?

**Kathy Lam:** That would be great.

**Kathy Lam:** Yeah.

**William Leborgne:** But do you have any other questions here before we jump Not a question.

**William Leborgne:** I was just going to say, I didn't know that we were going to do this, but I'm fine with it.

**William Leborgne:** It sounds like Aida wants us to actually take the lead and try and build the strategy for Turnstile, which is good practice.

**William Leborgne:** So I think we could do that.

**William Leborgne:** And I was going to say, maybe we both try to do it from scratch and then see what we get.

**William Leborgne:** And then reconvene later today and be like, hey, what did you get?

**Kathy Lam:** What did I get?

**Kathy Lam:** And then talk through it, maybe.

**William Leborgne:** Yeah.

**William Leborgne:** That's all I was going to say.

**William Leborgne:** But okay.

**William Leborgne:** So let me go ahead and because yeah, SEMrush is not super complicated, but it's like any tool, if you don't know where things are, you're just going to be spinning around because it.

**William Leborgne:** And unfortunately, they've created a UI which is very busy.

**William Leborgne:** And it's not always like hyper clear what each thing is.

**William Leborgne:** So in the beginning, it can be very overwhelming.

**William Leborgne:** So I'll just tell you right off the bat, there's like a couple of things that you're going to be using basically 90% of the time.

**William Leborgne:** The first is domain overview, which is basically like if you have a new client or whatever it is, let's say turnstile, for instance.

**William Leborgne:** This is a really good place to like get a sense of how this company is doing organically already.

**William Leborgne:** So it'll tell you right off the bat, like what is the authority score of this, or this is the same thing as the domain authority.

**William Leborgne:** And this is really important, right?

**William Leborgne:** Because this just tells you like where do they, where are they generally in the landscape of SEO, which is to say like very bad, like four out of 100 is pretty bad.

**William Leborgne:** And they have basically no organic traffic, as you can see here, it's all zero.

**William Leborgne:** So, and they're ranking for like two keywords.

**William Leborgne:** So, this is, this

**William Leborgne:** This gives you kind of a nice overview of the company.

**William Leborgne:** If you compare, for instance, to like the company I used to work at, like, you know, 51, and here you can see a lot more information about what's going on.

**William Leborgne:** So this gives you like a nice overview of kind of the company itself.

**William Leborgne:** Next, you want to look at organic research.

**William Leborgne:** Organic research is the one that she was using.

**William Leborgne:** That's the one you use probably the most.

**William Leborgne:** Like 80% of the time, I'm going straight to organic research.

**William Leborgne:** And so here you have an overview, which gives you a lot of information, which is like sort of helpful, sort of not helpful.

**William Leborgne:** What you typically go is you just jump over to positions.

**William Leborgne:** One other thing to note, this is not so relevant for what we're doing, but you will use it in the future, is you switch countries.

**William Leborgne:** Because this is not SEO for everywhere.

**William Leborgne:** It's just SEO for one country, right?

**William Leborgne:** So if you're like, okay, I want to know how they're doing in this country or in this language, then you would switch it up here.

**William Leborgne:** But so this is where it matters the most.

**William Leborgne:** You can click here, by the way, to remove this.

**William Leborgne:** These images, which makes it a little easier to view.

**William Leborgne:** So in this case, and she was using this a lot, right?

**William Leborgne:** This is like the baseline of the information that is evidence of air table.

**William Leborgne:** So organic research, you arrive on the thing, then you click on positions, and you're in this place.

**William Leborgne:** Now, because you're looking at turnstile and not, you know, stripe, for instance, you don't want to be pulling a lot of keywords that have stripe in it, because then it's really irrelevant, unless it's like competitor stuff, but that's such a small amount.

**William Leborgne:** So you're going to use this thing right here a lot, advanced filter.

**William Leborgne:** So you can do include or exclude.

**Kathy Lam:** So in this case, we'll do exclude anything that has a keyword.

**Kathy Lam:** In this case, it's like the company name is their DNA.

**William Leborgne:** Sometimes they also misspell it.

**William Leborgne:** So depending on the company, you have to just like scroll down and look, are they spelling it, you know, multiple ways.

**William Leborgne:** In this case, they do spell it wrong sometimes.

**William Leborgne:** So I have to do both of these, and you'll see.

**William Leborgne:** T, always the keyword will dip.

**William Leborgne:** So if I do this, it'll go down quite a bit.

**William Leborgne:** Oh, actually, not that much.

**William Leborgne:** A couple thousand.

**Kathy Lam:** But turnstile, you'd like change it between I or Y or whatever.

**William Leborgne:** Maybe.

**William Leborgne:** Yeah, obviously turnstile is like right now they have no visibility, so you're not going to use that much.

**William Leborgne:** But yes, that's right.

**William Leborgne:** The other thing she will often do is look at keyword difficulty and then also position.

**William Leborgne:** So she's looking at the top one to 30 is what she's typically most interested in, which makes sense, right?

**William Leborgne:** In the sense of like if it's beyond 30, I actually usually do top 20, but that's fine if here they do top 30.

**William Leborgne:** If it's beyond the 30 mark, it's going to be very – it's not going to be that potent.

**William Leborgne:** For this brand, and they're not doing that well with it, so then it's not really super, super open.

**William Leborgne:** Here you can see it dipped a lot, right?

**William Leborgne:** was at 80.

**William Leborgne:** 38,000, now we're at 40,000, so basically about half.

**William Leborgne:** So there you already have now, I've removed the name of the company, I've now, like, focused in on the keywords that are actually really potent for this company, and now I'm going to, I'm going to take these, like, 40,000 keywords.

**William Leborgne:** And so the way you do that is you go over here to export, you switch it over to CSV, and then it'll, it'll take a minute, and then it'll give you the file, the CSV file.

**Kathy Lam:** Cool?

**William Leborgne:** Yeah, that sounds great, thank you.

**Kathy Lam:** Any, any other questions on this, this part?

**Kathy Lam:** No, it seems pretty, like, self-explanatory, but thanks, like, all the different drop-downs, it's good.

**William Leborgne:** Yeah, and again, if you know some of this stuff, like, you can always tell me, like, no, I got this, and then I'll, I'll move on.

**William Leborgne:** There's just one other thing that I use a lot, which is called Keyword Magic Tool.

**William Leborgne:** You will use...

**William Leborgne:** There's probably a little less here in this work, because this is a little bit more like in the weeds, but it does get very helpful once you start to get like really specific about things.

**William Leborgne:** And so if you're like, okay, I want to know like, you know, cash, what was it again?

**Kathy Lam:** Quote to cash.

**William Leborgne:** Quote cash.

**William Leborgne:** Let's see if there's like any volume for that.

**Kathy Lam:** There you go.

**William Leborgne:** There is.

**William Leborgne:** So here, what you can do is you can look at like this exact one, but you can also look at all the different variations, which is really helpful when you're starting to think through your strategy.

**William Leborgne:** And then the other thing that is really helpful is this little button right here where you click and you can see who's already ranking at the top.

**Kathy Lam:** So this gives you like a little snapshot of your SERP, of your search engine results.

**William Leborgne:** Oh, that's good.

**William Leborgne:** Okay.

**William Leborgne:** Yeah.

**William Leborgne:** I use this a lot as well.

**William Leborgne:** And then in addition, if I click on it, it'll open a new tab and I will.

**William Leborgne:** see additional keywords that are variations of it.

**Kathy Lam:** So this is also really helpful.

**Kathy Lam:** How did you get to that list of like, who was ranking the highest for it?

**William Leborgne:** Yeah.

**Kathy Lam:** So that's this little tiny icon right here next to it.

**William Leborgne:** Yeah, exactly.

**William Leborgne:** Yeah, no, again, like I've been where you're at, like, this can be very confusing sometimes.

**William Leborgne:** And then at some point, we're not going to do this right now, but they do have this AI visibility thing, which is actually kind of helpful.

**William Leborgne:** It's not great, but it's not bad.

**William Leborgne:** And you can see, like, you know, if I do airDNA.co for information around, like, specifically AI, you know, overviews and other, like, prompts and stuff that you can find more information on.

**Kathy Lam:** I have another question.

**Kathy Lam:** Like, what if.

**Kathy Lam:** If one of their things is technical, like, oh, right now all of their content is a subdomain rather than a subfolder, do we say, hey, one of the things you should change after this eight weeks is to start thinking about making those plans?

**Kathy Lam:** Or is that something we do here?

**William Leborgne:** I see what you're saying.

**William Leborgne:** Yeah, like this is more like technical SEO stuff, right?

**William Leborgne:** Where you're saying like, yeah, your structure of your content is bad.

**William Leborgne:** I think that's actually like super early on in the sales process.

**Kathy Lam:** They're already having those conversations.

**William Leborgne:** So that's definitely not later.

**William Leborgne:** That's like very, very early.

**William Leborgne:** And that's kind of a red flag if there's any major issues there.

**William Leborgne:** BlackSoul is one of those a little bit, not like a major issue because they literally just created their CMS and their blog.

**William Leborgne:** But they were like, oh, should it be blog and then guides and then /blogs? Or should it be a separate page versus just have it all be in one place?

**William Leborgne:** My feeling is like from experience, it doesn't matter really.

**William Leborgne:** Like as long as the click depth is not super long, like it doesn't take seven clicks to get to the thing.

**William Leborgne:** It doesn't matter because 99% of people who are going to get to that blog are getting there because they Googled it, not because they went onto your blog and scrolled down or like searched in your blog.

**William Leborgne:** Like that doesn't, that almost never, ever happens.

**William Leborgne:** So having like a really clean separate structure in the UI is a nice to have.

**William Leborgne:** It's not a must have as long as it's well set up, it loads quickly, and all the other good stuff.

**William Leborgne:** Like it does all the other good stuff, but that's my personal take on it.

**Kathy Lam:** Awesome.

**Kathy Lam:** Okay, great.

**Kathy Lam:** Once I get all logged in, I'll like do one of these walkthroughs through Turnstile.

**Kathy Lam:** I guess what we can do at the end is like see what we all come up with.

**William Leborgne:** Yeah, why don't I throw in some time for us? Shall we say 4 PM my time, which is 2 PM your time, or is that too early?

**Kathy Lam:** No, I think that's good, because otherwise it goes into your evening.

**William Leborgne:** Yeah, okay, so let's do 4 p.m.

**William Leborgne:** my time, and then 2 p.m.

**William Leborgne:** your time.

**William Leborgne:** I'll send you the invite now, and then we can just, like, it doesn't matter if it's not perfectly done, like, this is us learning, right?

**William Leborgne:** So we'll just, like, share what we've been able to put together.

**Kathy Lam:** Cool, that sounds awesome.

**Kathy Lam:** Sweet.

**Kathy Lam:** Okay, great.

**Kathy Lam:** Thanks so much, have a good one.

**Kathy Lam:** Yeah, talk to you soon.

**Kathy Lam:** Okay, bye.
