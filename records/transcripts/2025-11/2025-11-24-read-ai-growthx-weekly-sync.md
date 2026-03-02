# Read AI <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-24
time: 20:01 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Sarah Spagnolo, Aida Knezevic, Erik O'Brien, David Shim, Kate Reinmiller, Justin Farris
fathom_recording_id: 103984680
fathom_url: https://fathom.video/calls/482938053
share_url: https://fathom.video/share/cdFmgjTZtKZyJh7xP_ByKyab-zsefLjD
source: fathom
enriched_on: 2026-03-02 10:30 UTC
</metadata>

---

## Summary

Read.ai (Sarah Spagnolo) met with GrowthX (Aida Knezevic, Erik O'Brien) to review content strategy feedback and introduce two new performance dashboards. Aida updated the Airtable content calendar to use a hub-and-spoke model, and Sarah confirmed that GrowthX should execute the full year-long content program with only high-level feedback from Read.ai. The team also launched Scrunch (for LLM visibility tracking) and Looker (for SEO/GA4 analytics), revealing a critical insight: Read.ai's LLM citation rate is 1% versus competitors' 20%, a gap that can be closed through increased educational content publishing.

---

## Context

This is a weekly sync between Read.ai and GrowthX, a B2B content marketing agency managing Read.ai's content strategy and AEO (AI Engine Optimization) work. Read.ai is an AI meeting transcription and conversation analysis platform, and this meeting addresses content feedback calibration and performance measurement as GrowthX prepares to execute a high-volume, year-long content program. The partnership represents a strategic shift: instead of per-article approval workflows, GrowthX will operate autonomously with Sarah providing only strategic input on topic prioritization through Airtable comments.

---

## Relevance

**To GrowthX Delivery:**
- New approval workflow reduces touchpoints: Sarah will only comment on Airtable to flag back-burner topics rather than approving each article. This supports high-volume publishing (3 new blogs per week starting).
- Content calibration emphasizes product breadth (enterprise search as more than note-taking), business impact framing (must-have vs. nice-to-have), and accuracy in examples—all core to effective B2B tech writing.
- Airtable hub-and-spoke organization (parent pages + related subtopics) aligns with content cluster strategy for both SEO and LLM visibility.

**To CheckThat / AEO:**
- LLM citation gap is clear and quantifiable: 1% vs. 20% at competitors. A cybersecurity client with 1,000+ content URLs achieved 15% citation rate, proving the volume-quality correlation.
- Scrunch dashboard now tracks position, sentiment, and citations across Claude, Gemini, ChatGPT, Perplexity, and other LLMs. Erik has seeded 100+ custom prompts beyond the base 25.
- November 19 spike in citations coincided with external brand events (news coverage + YouTube influencer video), revealing that LLM visibility is amplified by off-site visibility work.

**To GrowthX Business Development:**
- Account expansion signal: Read.ai is investing in dashboards (Scrunch, Looker), custom prompt development, and year-long content planning, indicating strong confidence in the engagement.
- Renewal and reference potential: If GrowthX successfully closes the citation gap through content, this becomes a marquee case study for AEO capabilities.

---

## Overview

- **Content Strategy Shift:** The content strategy now focuses on business impact and a broad product view (beyond note-taking), not just tone. GrowthX will execute the full content plan, with Sarah providing high-level feedback in Airtable.
- **LLM Visibility Gap:** Read.ai's LLM citation rate is 1% vs. competitors' \~20%. This gap is caused by insufficient educational content; the solution is to publish more blog posts and knowledge base articles.
- **New Performance Dashboards:** Two new dashboards are live: Scrunch (for LLM visibility) and Looker (for traditional SEO/GA4). Aida will send Sarah an invite to the Looker dashboard.

---

## Key Topics

### Content Strategy & Feedback

  - **Calibration Feedback:** Sarah's feedback on the enterprise search blog post was content-focused, not tone-focused.
      - **Expand Product View:** Position the product beyond note-taking to include all inputs for enterprise search.
      - **Drive to Business Impact:** Frame the AI platform as a "must-have" for business velocity and profitability, not a "nice-to-have."
      - **Use Clear Examples:** Avoid jargon and ensure examples are accurate to prevent user distraction.
  - **Airtable Hub & Spoke Model:** Aida updated Airtable to show content clusters (hubs) and related articles (spokes) for better organization.
  - **Content Approval Process:** The process shifts from per-article approval to full execution by GrowthX.
      - **Rationale:** To support a year-long, high-volume content program.
      - **New Workflow:** Sarah will skim topics in Airtable and comment on any to de-prioritize.

### Performance Tracking Dashboards

  - **Scrunch (LLM Visibility):** Monitors Read.ai's presence in LLM responses (Claude, Gemini, etc.).
      - **Key Metrics:** Position, sentiment, and citations.
      - **Citation Gap:** Read.ai's 1% citation rate is far below competitors' \~20%.
          - **Cause:** Insufficient educational content on the website.
          - **Solution:** Increase content volume. A cybersecurity client with 1,000+ URLs has a 15% citation rate.
      - **Insight:** A recent spike in citations (Nov 19) coincided with a news event and a YouTube influencer video, showing the impact of external brand visibility.
  - **Looker (SEO & GA4):** Aggregates data from Google Search Console and GA4.
      - **Key Reports:**
          - **GA4 Overview:** Tracks sessions vs. engaged sessions (\>10s, scroll, or click).
          - **Non-Branded Search:** Monitors organic traffic from keywords without "read.ai."
          - **Conversions:** Shows GA4 events. Some event names are unclear (e.g., "meeting report"), likely capturing logged-in state events.
          - **Cohort Report:** Will track the performance of GrowthX-published content.
          - **Query Report:** Identifies new keyword opportunities from existing search traffic.

---

## Action Items

**Aida Knezevic (GrowthX) (5)**
- Fix Teams bot auth/link for next week's sync; test with Sarah
- Update enterprise search calibration per Sarah's feedback; send to Sarah for review
- Select 3 foundational topics; start drafting 3 new blogs this week
- Email Looker invite to Sarah; she'll share internally with Read.ai team
- Tag David (Read.ai) in Slack regarding GA4 custom conversion events

**Sarah Spagnolo (Read.ai) (1)**
- Skim Airtable ContentOS calendar; tag Aida on any back-burner topics to de-prioritize

**Erik O'Brien (GrowthX) (1)**
- Export and send full Scrunch prompt list to Sarah for review

---

## Transcript
**Sarah Spagnolo:** This meeting is being recorded.

**Aida Knezevic:** Hi.

**Sarah Spagnolo:** How are you both?

**Aida Knezevic:** Good.

**Sarah Spagnolo:** are you?

**Sarah Spagnolo:** Good.

**Sarah Spagnolo:** Happy Monday.

**Sarah Spagnolo:** Okay.

**Sarah Spagnolo:** Last week, the re-bot left because somebody didn't accept it.

**Aida Knezevic:** I have to log in as the Teams account.

**Aida Knezevic:** One second.

**Aida Knezevic:** have to leave the meeting.

**Erik O'Brien:** Got to figure out a way to fix that.

**Sarah Spagnolo:** Yeah, I guess so.

**Erik O'Brien:** How was the weekend?

**Sarah Spagnolo:** It was very busy, but good.

**Erik O'Brien:** What about you?

**Erik O'Brien:** Not busy, which was great.

**Erik O'Brien:** Oh, that's nice.

**Erik O'Brien:** I did.

**Erik O'Brien:** Hang up all the Christmas lights yesterday, so a bit sore from hanging off the roof.

**Sarah Spagnolo:** Oh, wow.

**Sarah Spagnolo:** In advance of Thanksgiving.

**Sarah Spagnolo:** Way to go.

**Erik O'Brien:** Yeah, I figured I'd get it done before I get tired after eating all the Thanksgiving food.

**Sarah Spagnolo:** Yeah, okay.

**Aida Knezevic:** I'm still logged in as my own account.

**Aida Knezevic:** Just one second.

**Sarah Spagnolo:** I'll be back.

**Erik O'Brien:** Yeah, it's the first year I've done any decorating before Thanksgiving, so I tried something new this year.

**Sarah Spagnolo:** It was my friend from Vienna was visiting, and they don't have Thanksgiving in Vienna, of course.

**Sarah Spagnolo:** And so we were talking a bit about how, like, it's just like, it goes from Halloween straight in.

**Erik O'Brien:** Yeah.

**Sarah Spagnolo:** Which makes sense.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** Plus, it's like, what kind of, I mean, I guess you can reuse some of your Halloween, like, pumpkins and other stuff, but, like, otherwise, I don't really have any Thanksgiving decorations.

**Sarah Spagnolo:** Right.

**Sarah Spagnolo:** Right.

**Sarah Spagnolo:** Although I did get, we're going to my aunt and uncle's house, and I got them some Halloween, not Halloween, Thanksgiving coasters.

**Erik O'Brien:** Oh, nice.

**Erik O'Brien:** Yeah.

**Sarah Spagnolo:** Oh, it's still under, Aida.

**Sarah Spagnolo:** You're muted now, Aida.

**Aida Knezevic:** I changed ownership of the event to myself, but that ended up deleting the meeting link.

**Aida Knezevic:** So, this is annoying.

**Aida Knezevic:** Hold on.

**Sarah Spagnolo:** Reed's still here now.

**Aida Knezevic:** Yeah, I, last time time I

**Aida Knezevic:** I was able to log in from the Teams account, and I did get, like, a prompt to accept it.

**Aida Knezevic:** So I was able to authorize it.

**Sarah Spagnolo:** Can you authorize it now?

**Aida Knezevic:** I'm not.

**Aida Knezevic:** It's not showing up.

**Aida Knezevic:** It was like a pop-up box.

**Sarah Spagnolo:** Okay.

**Sarah Spagnolo:** Well, you know what?

**Sarah Spagnolo:** We have a new desktop app, so I should be able to record that way.

**Sarah Spagnolo:** Let me see.

**Sarah Spagnolo:** There we go.

**Sarah Spagnolo:** Okay.

**Sarah Spagnolo:** I'm able to record it locally.

**Sarah Spagnolo:** Perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Hopefully.

**Aida Knezevic:** So from next week, we will be able to use, like, the recorder in the meeting, but now it's just a little too complicated.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So, Sarah, I did see that you provided some really helpful feedback on the calibration.

**Aida Knezevic:** Any high-level notes that you had for us?

**Aida Knezevic:** Oh, it's gone.

**Sarah Spagnolo:** Oh, yeah, there went the reading.

**Sarah Spagnolo:** I bought high-level notes.

**Sarah Spagnolo:** I thought the tone was good.

**Sarah Spagnolo:** I was a little distracted by the content of the blog post itself, which I wanted to be sure to give you a lot of guidance and insight into how we think about the component parts of our platform, as well as keywords and other angles that I feel like were really important.

**Sarah Spagnolo:** I think that where I want to make sure we have alignment is in driving, well, a few things in particular.

**Sarah Spagnolo:** One is looking more expansively at our product that beyond note-taking, and we've talked about this a fair amount, but there will be some aspects where we're going to focus purely on our note-taking capabilities, but this article in particular was on enterprise search.

**Sarah Spagnolo:** And so I want to be sure that we are clear.

**Sarah Spagnolo:** That the inputs into Enterprise Search are not just meeting notes and conversations.

**Sarah Spagnolo:** And that's not just about collating ephemeral conversations and putting it into some type of a knowledge management software, but it's combining all different inputs into one.

**Sarah Spagnolo:** And so that became a theme that I provided a bunch of feedback on.

**Sarah Spagnolo:** There was also the theme of driving all the way to business impact.

**Sarah Spagnolo:** So making sure that the outcome of working with a meeting note taker or Enterprise Search is not just the ability to find a detail, but actually drive velocity in your business as the eventual better return on investment when you work with AI platforms such as Read or any other, frankly.

**Sarah Spagnolo:** Just making sure we position the product as...

**Sarah Spagnolo:** Not a nice to have, but a must have if you want to compete in the modern world, which I didn't say that specifically, but we should all keep that in mind, that it should be a compelling software that somebody wants to use to drive profitability and all of the things that are important to a business long term versus just making it easier for people to communicate with one another.

**Sarah Spagnolo:** And so those were the two largest buckets of feedback.

**Sarah Spagnolo:** I wasn't really commenting on tone, even though you asked me specifically about tone.

**Sarah Spagnolo:** I think that these changes will help get you towards tone.

**Sarah Spagnolo:** I also think that the only thing that's not in there about tone that I would say is just really clear examples, no jargon about what makes this a value add to your business.

**Sarah Spagnolo:** So in some cases, the examples that were provided, because they were not exactly right, were distracting to me that I couldn't say like, this is the right example or this is the right

**Sarah Spagnolo:** For example, or I would describe it this way just because the descriptions itself were off base.

**Sarah Spagnolo:** So I couldn't even get to that next point.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** That makes total sense.

**Aida Knezevic:** I think, yeah, your feedback is really helpful.

**Aida Knezevic:** I know I did say to focus on the voice and the tone, but it is very helpful to understand, like, what are the types of benefits that we want to call out?

**Aida Knezevic:** And I think we do this for, like, enterprise search now, and we should be good to go.

**Aida Knezevic:** For any other, you know, for, like, the future articles where we talk about enterprise search.

**Sarah Spagnolo:** Great.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Sarah Spagnolo:** I think I did see you tag someone else to provide.

**Sarah Spagnolo:** I talked to her.

**Sarah Spagnolo:** I actually had a meeting with her, and we revised one section based on our comment.

**Sarah Spagnolo:** So that's addressed.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** In that case, we're going to go back and just fold in your feedback.

**Aida Knezevic:** We need to update the artifacts and then.

**Aida Knezevic:** And we can send it to you just to take another look.

**Sarah Spagnolo:** Okay.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** All right.

**Aida Knezevic:** We do want to work on three new blogs this week.

**Aida Knezevic:** But before we dive into that, I did want to show you sort of the updates that I made to Airtable based on our discussion last week.

**Aida Knezevic:** So last week you asked if there's a way that we could show, okay, what is like the hub, like the foundational piece of content?

**Aida Knezevic:** And then what's like the perimeter of that?

**Aida Knezevic:** Like what are, which is, it's called basically hub and spoke model in SEO, which is you have like a parent page or like a more foundational piece of content that targets a more broad concept.

**Aida Knezevic:** And then from there you have like different sub pages that talk about a specific topic within that broader concept.

**Aida Knezevic:** So when you go.

**Aida Knezevic:** Go to Assignments, and if you expand, you can see what are the hubs.

**Aida Knezevic:** So we're, I mean, obviously, as we do more keyword research, there will be more hubs here and, like, more spokes, but this is what we're starting with.

**Aida Knezevic:** So you can see what is the hub, and then you can expand to see, okay, what is, like, the hub page, and then the spokes.

**Aida Knezevic:** And I think that can kind of help you because you're likely, like, probably, like, 99% sure that you want to approve something like this.

**Aida Knezevic:** But for the spokes, it makes it easier for you to see, okay, what are, like, what are they suggesting that's also related to this topic?

**Aida Knezevic:** And then we have for, and it's basically the same for, like, all clusters.

**Aida Knezevic:** So we have, like, a hub that's, like, AI for product teams, and then under here we have, like, a hub page that would talk about AI for product managers.

**Aida Knezevic:** And then we have, like, a couple of spokes that talk about different subtopics.

**Aida Knezevic:** I think that should make it kind of more organized for you to go through.

**Sarah Spagnolo:** Okay.

**Sarah Spagnolo:** And then, so I brought this up to David a little bit earlier today, and I was saying that what Justin and I had asked for you to do is to kind of prioritize the hub and the spokes so it was easier for us to weigh in.

**Sarah Spagnolo:** Thank you for doing that.

**Sarah Spagnolo:** His point back to me was that your team should be doing all of it.

**Sarah Spagnolo:** Like, the goal is to work together on a year-long program where you're creating massive amounts of content for us.

**Sarah Spagnolo:** So to that end, like, I shouldn't really be negating any content or worrying about prioritization because there is no prioritization if you're going to do it all.

**Sarah Spagnolo:** What's your feedback on that because you had very specifically been asking me to approve or not.

**Sarah Spagnolo:** So how do we, how do I think about both of those inputs together?

**Aida Knezevic:** Yeah, I think his approach is something that I love.

**Aida Knezevic:** So it's like the approach is like, you know, create the strategy, make the content calendar, just execute on it.

**Aida Knezevic:** I think what we typically have is clients who do want to like be very involved and they do want to approve.

**Aida Knezevic:** So that's kind of what we default to, but it's certainly not expected of you to do that.

**Aida Knezevic:** But I think where it would be helpful if you just skimmed these topics and then if there's something that I think last week Justin pointed out in one of the, there was an article about how to write a project like.

**Aida Knezevic:** Like a PRD or something.

**Aida Knezevic:** Yeah, yeah, exactly.

**Aida Knezevic:** And he was like, I'm not so sure about like, this isn't something that like we do, like it's just, you know, so those types of things.

**Aida Knezevic:** I don't think it's not a valuable topic because it is like speaking to product managers and it does allow.

**Aida Knezevic:** us to show up in front of that audience.

**Aida Knezevic:** But if you're like, well, that's not the best, like, you know, because we do want to prioritize topics that are closer to your product.

**Aida Knezevic:** So anything that kind of falls out of that, you can let us know, but you don't have to, like, go through and, like, approve each one.

**Aida Knezevic:** You could just kind of skim the list and let us know, like, hey, these are the ones that are kind of, like, we want to be on the back burner.

**Sarah Spagnolo:** Where should I comment if that's the case in this?

**Aida Knezevic:** So if you look at the, sorry, something got in my eye.

**Sarah Spagnolo:** If you look at the title record and then if you expand, leave a comment here and you can tag me.

**Sarah Spagnolo:** Okay.

**Sarah Spagnolo:** And you gave me access to this.

**Sarah Spagnolo:** I actually haven't gotten in there.

**Aida Knezevic:** Yes.

**Aida Knezevic:** So you should have commenting access.

**Aida Knezevic:** I'll drop a link in the chat and let me know if you can open it.

**Aida Knezevic:** It's also in our Notion base.

**Aida Knezevic:** If you find, like, ContentOS, there should be a link in there.

**Sarah Spagnolo:** Yeah, I'm in.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** I think we are, I think we can, like, get started with three topics that we think are quite, like, foundational, and we know that, you know, they're connected to the product.

**Aida Knezevic:** So we can get, I can pick those out today.

**Aida Knezevic:** And then, yeah, I'll be on the lookout for, like, any additional feedback.

**Aida Knezevic:** Great.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then for the performance tracking part, so we did set up a Looker dashboard and a Scrunch dashboard.

**Aida Knezevic:** So the Looker dashboard is to track, like, traditional search performance, and then the Scrunch dashboard is to...

**Aida Knezevic:** Measure visibility in different LLMs based on the prompts that we provide the platform.

**Aida Knezevic:** So, excuse me.

**Aida Knezevic:** So I think we can get into Scrunch first because it's a smaller report.

**Aida Knezevic:** I'm going to just – have you ever used a tool like Scrunch before?

**Sarah Spagnolo:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So Scrunch, Profound, Meridian, they're all LLM visibility platforms.

**Aida Knezevic:** That function by sending different prompts to LLMs, then they pull the responses, they analyze them, and they kind of present them in a dashboard like this.

**Aida Knezevic:** So what we did was we provided Scrunch with a description of your company, a list of your competitors, and then we also provided descriptions of your target audience.

**Aida Knezevic:** And then Scrunch generated, I think, is it 25?

**Aida Knezevic:** So,

**Aida Knezevic:** 25 or 35 base prompts, Erik?

**Erik O'Brien:** Yeah, usually starts with 25.

**Erik O'Brien:** I went in last week and added several more.

**Aida Knezevic:** Okay, yeah.

**Aida Knezevic:** So they generate like 25 base prompts, and then we can add more.

**Aida Knezevic:** So Erik has uploaded probably like 100, 200 more.

**Aida Knezevic:** But we can also add many more prompts in here.

**Aida Knezevic:** We can also, we'll also download the list of prompts and share it with you so that you can kind of weigh in and let us know if there's anything that you would like us to track.

**Aida Knezevic:** So these prompts are sent to all of these different LLMs like Claude, Google, Gemini, Chagibiti, Perplexity.

**Aida Knezevic:** And then we kind of get an idea of where your competitive presence stands compared to like your top competitors.

**Aida Knezevic:** The position breaks down like where you appear in an LLMs response if it's like listing different products.

**Aida Knezevic:** Or platforms, and sentiment is self-explanatory, citations refer to the number of links to your website that appear in LLM responses.

**Aida Knezevic:** So at 1%, this is quite low.

**Aida Knezevic:** However, for most of our clients, they are around 3% to 4%.

**Aida Knezevic:** On the other hand, your competitors are roughly around 20%.

**Aida Knezevic:** So the way to increase citations is just to have more content on your website that we can, that LLMs can cite.

**Aida Knezevic:** We have one of our cybersecurity clients, they have a really big knowledge base on their website.

**Aida Knezevic:** They have over 1,000 URLs of content across their blog, glossary, like different subfolders.

**Aida Knezevic:** And their citation rate is around 15%.

**Aida Knezevic:** So the more educational content...

**Aida Knezevic:** The you have on your website, the higher the, you know, chance that you'll be cited by LLMs.

**Aida Knezevic:** And we also see this in their Looker Report.

**Aida Knezevic:** We break, there's a page that breaks down how much traffic your website gets from different LLMs.

**Aida Knezevic:** And we can see for that client that the vast majority of LLM referral traffic goes to their blog and to other educational content on their website.

**Aida Knezevic:** We can download this, export it, and send it to you as a PDF.

**Aida Knezevic:** We'll be going over this, like, pretty regularly, especially as we, like, start publishing content.

**Aida Knezevic:** And then in the prompt section, scrunch auto-generates these topics.

**Aida Knezevic:** And then we have, like, different, it's basically, like, grouping different prompts together.

**Aida Knezevic:** So if we look at

**Aida Knezevic:** AI-powered meeting transcription, for example, we can see all of the different seed prompts, and then when we click into a prompt, we can see all of the different responses over the last couple of days from different LLMs, and we can see who are the competitors that are showing up in different LLM responses.

**Aida Knezevic:** I think if we even like click through the individual response, we can see the exact dates and the full response.

**Aida Knezevic:** So for example, we have like, this is the latest one.

**Aida Knezevic:** So for example, let's go back to, let's go to November 19th.

**Aida Knezevic:** So like best-in-class platforms with strong transcription plus conversation analysis.

**Aida Knezevic:** We can actually see what the AI's response was.

**Sarah Spagnolo:** So what, you're just pinging it every day?

**Aida Knezevic:** Yeah, that's what Scrunch is doing.

**Aida Knezevic:** Like sometimes maybe even multiple times a day.

**Sarah Spagnolo:** So it's interesting.

**Sarah Spagnolo:** November 19th, we had a news moment.

**Sarah Spagnolo:** I wonder.

**Aida Knezevic:** Okay.

**Sarah Spagnolo:** I also saw a spike in an influencer piece of coverage.

**Sarah Spagnolo:** I wonder if that all, how that all works together.

**Aida Knezevic:** What platform was the influencer using?

**Sarah Spagnolo:** I think it was YouTube.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I think, for example, like you can see the citations and it did cite this blog post that you have around for best AI notetakers and AI co-pilots.

**Aida Knezevic:** So that blog post was pulled into the response.

**Aida Knezevic:** But, yeah, I think with LLM visibility, what we can control.

**Aida Knezevic:** and the growthx side is the content and like the publishing velocity and how we talk about read.ai and how we position read.ai against your competitors, but there's also a whole world out there where, you know, appearing on other websites and just like that brand visibility is huge boost.

**Aida Knezevic:** So, yeah, okay, so yeah, like I said, Erik can download the prompts if you're interested in taking a look, but the way we use Scrunch, like over the long term, especially once we start publishing, we want to monitor your overall presence, whether it's, you increasing, decreasing for specific topics and And then if there's something where we're noticing that your visibility is decreasing, we can try and see, you know, what, why is that happening?

**Aida Knezevic:** Like how we can kind of influence it.

**Aida Knezevic:** With the content, obviously, any competitive comparisons, like best sub, listicles, those end up having, like, those have a pretty quick impact on LLM responses.

**Aida Knezevic:** So we do try to, like, prioritize those if we're just looking at LLM visibility.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then for Looker, I will send an email invite to the Looker report, and you should be able to share it internally with anybody that needs access.

**Aida Knezevic:** So this is data.

**Aida Knezevic:** This report is created using data from your search console, which just includes organic traffic data from Google and Google Analytics 4, which aggregates all data that comes to your website.

**Aida Knezevic:** right.

**Aida Knezevic:** Are you using anything?

**Aida Knezevic:** Anything else other than GA4 to monitor web analytics and traffic?

**Sarah Spagnolo:** I don't know.

**Sarah Spagnolo:** I'm not the person who has that information.

**Aida Knezevic:** Okay.

**Aida Knezevic:** No worries.

**Aida Knezevic:** It's usually just GA4, but recently we've been having some clients say that they're also using, like, other tools to track their website traffic, so I just want to check.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So for – so this initial page, it breaks down data from your Google Analytics 4 dashboard, and it compares sessions to engage sessions.

**Aida Knezevic:** And this is, like, a month-by-month breakdown, but we can also change it to a week-by-week breakdown so you have, like, a better idea how traffic moves week over week.

**Aida Knezevic:** An engaged session in Google Analytics 4 is a session that lasts longer than 10 seconds, or it includes a page scroll, or it includes

**Aida Knezevic:** It's the user clicking on a link to go somewhere else on your website or go to a different website.

**Aida Knezevic:** So that counts as an engaged session.

**Aida Knezevic:** And typically, this is the average range of engaged sessions that we see across most of our clients, so slightly more than 50%.

**Aida Knezevic:** If you scroll down, you can see the individual landing page performance, including data around the individual engagement rate for each landing page.

**Aida Knezevic:** And you can also see a breakdown of sessions by referrers.

**Aida Knezevic:** So this includes all referral channels, like social, organic, like organic, social, and both paid social, paid search ads, email.

**Aida Knezevic:** For the non-branded page, this is data from Google Search Console, and it's measuring...

**Aida Knezevic:** traffic that comes to your website from search queries or keywords that don't include your company name.

**Aida Knezevic:** So that's why they're non-branded.

**Aida Knezevic:** And we can see like an overall like traffic growth or decrease in URL clicks and impressions, which is what those are the only two metrics that we can track in Google Search Console.

**Aida Knezevic:** Google Search Console also allows us to track the average position for each page on your website and the average click-through rate.

**Aida Knezevic:** And you can also see like the individual performance of different landing pages in Google Search Console.

**Aida Knezevic:** For the conversion events, this is data from your Google Analytics 4 account.

**Aida Knezevic:** And any conversion events that you have set up in GA4 are going to appear here.

**Aida Knezevic:** I think so.

**Aida Knezevic:** GA4 does come.

**Aida Knezevic:** With some pre-built conversion events, I think page view, session start, user engagement, first visit, scroll, those are all baked in.

**Aida Knezevic:** But for example, I think these are probably custom.

**Aida Knezevic:** So I think this is fairly like self-explanatory.

**Aida Knezevic:** think meeting report, well, actually sign up is self-explanatory, but these two, I'm not exactly sure what they're measuring.

**Aida Knezevic:** So it would be helpful for us to know, like for the future, what these are tracking.

**Sarah Spagnolo:** Okay.

**Erik O'Brien:** Yeah, I know David did share that GA4 wasn't the cleanest at this moment.

**Erik O'Brien:** So I think some of these are capturing logged in state events.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Sarah Spagnolo:** If you could tag David in Slack about this, that he would be the best.

**Aida Knezevic:** And then for the cohort report, so this is the page where we will be tracking GrowthX performance, like, of all the content that we publish on your website.

**Sarah Spagnolo:** I apologize, but Looker is sometimes pretty slow to load.

**Aida Knezevic:** But, yeah, right now this is empty, obviously, because we haven't published any content.

**Aida Knezevic:** But right now, these are all non-GrowthX URLs, which is basically the entirety of your website.

**Aida Knezevic:** But once we do start publishing, we're going to be also seeing different, like, color-coded traffic insights here.

**Aida Knezevic:** And here we will track the performance of different topic clusters. This is data from GA4 and Google Search Console, so we can see how things are performing at a glance.

**Aida Knezevic:** The landing page report is basically your Google Search Console dashboard pulled into Looker. You can see the overall performance of your website, including the average click-through rate and the average position. Typically the click-through rate is a lot smaller, which is why it doesn't show up in this color-coded chart, but you should be able to see the data as you move through. You can also see the different performance of various landing pages, including clicks, impressions, click-through rate, and average position for each URL.

**Aida Knezevic:** The query report is also data from Google Search Console, and it breaks down all the different keywords that Google Search Console has detected that are bringing users to your website.

**Aida Knezevic:** So let's just wait a minute for it to load.

**Aida Knezevic:** I heard from someone that Looker is looking to like introduce paid plans.

**Aida Knezevic:** Because right now it's free.

**Aida Knezevic:** And that was their theory behind the slow performance of their dashboards.

**Aida Knezevic:** Okay, we got it.

**Aida Knezevic:** So yeah, you can see kind of the different query distribution.

**Aida Knezevic:** Obviously, there are a lot of different branded queries here.

**Aida Knezevic:** But if you scroll up, you can see all of the different queries that you're ranking for.

**Aida Knezevic:** And then you can also kind of change it by country.

**Aida Knezevic:** And this report is pretty interesting in the sense that...

**Aida Knezevic:** We will look at this data to understand if there are any additional opportunities for keywords that we could target.

**Aida Knezevic:** Sometimes you might be ranking for a really interesting keyword that we could use for a blog post, but you actually don't even have content on that keyword, so it can also be helpful in that regard.

**Aida Knezevic:** And I realize we're at time, so I just wanted to go through quickly through the LLM referral report.

**Aida Knezevic:** So here you can see all of the LLM referrers that are bringing traffic to your site.

**Aida Knezevic:** ChatGPT is typically at the top, followed by perplexity.

**Aida Knezevic:** And in the landing page report, you can see the different landing pages that are getting traffic from different LLMs.

**Aida Knezevic:** So typically it's a homepage, then followed by other, like for most of our clients, it's blogs, but, you know, also product pages get pulled in, sometimes even careers.

**Aida Knezevic:** And this table.

**Aida Knezevic:** It's just going to show you, like, once it loads, it's going to show you, like, chart breakdown of, like, the different LLM referral traffic and how it's gone up or down over the past year.

**Sarah Spagnolo:** So it seems like these are where your team minds to see, A, what's been successful or what's working, and also potential ideas for avenues to explore.

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** So this is where we'll be spending a lot of time once we start publishing and measuring performance.

**Sarah Spagnolo:** Great.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** I'll send you an invite to lookers.

**Aida Knezevic:** You should get that in your inbox.

**Aida Knezevic:** In the meantime, yeah, we'll get to work on improving the calibration.

**Sarah Spagnolo:** And I will look at the Bayer table.

**Aida Knezevic:** Okay, thank you.

**Sarah Spagnolo:** right.

**Sarah Spagnolo:** I'll see you next Thank you, everyone.

**Erik O'Brien:** Speak to you soon.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Thanks, Sarah.

**Erik O'Brien:** Thank you.
