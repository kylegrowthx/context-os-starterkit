# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-05
time: 20:00 UTC
duration: 47 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Sam Pfluger, Brock Walters, John Jeremiah, Irena Reedy, Aida Knezevic
fathom_recording_id: 99506450
fathom_url: https://fathom.video/calls/463458800
share_url: https://fathom.video/share/tfLNiv8TQKLtAkynxys8ytdFufe-Vxng
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

GrowthX and Fleet aligned on a major content strategy to correct inaccurate AI search results about Fleet (e.g., "Fleet is not an MDM") through fresh, authoritative content. The team reviewed the first calibration blog post, approved AI-generated feature images, and discussed an SEO-focused approach to reprioritize blog topics with keyword intent alignment. Fleet approved 10+ topics for immediate production, with GrowthX to draft 3 posts next week, while Phase 2 will launch a programmatic SEO project covering all 335 Fleet osquery data tables.

---

## Context

Fleet (fleetdm.com) is a modern device management platform. GrowthX is providing content marketing services ($200k+ engagement) to correct inaccurate AI search results that mischaracterize Fleet's capabilities. The project began after GrowthX and Fleet identified that AI models are returning outdated or false information in comparisons (e.g., claiming Fleet is not an MDM when it actually offers MDM capabilities and can run alongside other MDMs). This is a weekly sync to align on content strategy, review AI-generated calibration posts, approve blog topics, and measure performance through SEO and LLM referral metrics. John recently joined Fleet as a content/SEO specialist from Blink Ops and was brought into the call to learn the strategic context and measurement approach.

---

## Relevance

- **To GrowthX Delivery:** Fleet approved 10+ blog topics from the initial 79-topic Airtable list for immediate content production. GrowthX will draft 3 articles next week and iterate on SEO title alignment. Phase 2 will tackle 335 osquery data tables with programmatic SEO templates. John's SEO expertise brings new perspective on LLM referral measurement and AI overview optimization vs. traditional keyword rankings.

- **To CheckThat:** This project demonstrates AEO (AI Engine Optimization) in practice. Discussion revealed that AI models pull from fresh content selectively (50% keyword coverage over 7 months), comparison content gets cited by LLMs more readily than definitional content, and prompt anticipation (12-word conversational queries) differs from keyword SEO. John noted that March 2025 Google AI summaries caused clicks to drop even as impressions rose — a key metric to track via Looker dashboard.

- **To GrowthX Business Development:** Fleet has hired a head of marketing (Ashish) with John reporting to him, suggesting expansion of content efforts. This is a high-complexity, long-term account requiring deep product knowledge (Fleet's nuanced MDM positioning, osquery uniqueness) and sophisticated measurement (LLM referral tracking via Looker). Potential for reference case study if LLM referral strategy succeeds. Account health appears strong with clear strategic alignment.

---

## Overview

- **Primary Goal:** Correct AI search results (e.g., "Fleet is not an MDM") by publishing fresh, authoritative content.
- **Content Strategy:** Pivot from product-centric topics to SEO-driven keywords to improve search visibility.
- **Phase 2:** Launch a programmatic SEO project for 335 osquery data tables to create a massive, differentiated content library.
- **Action:** Sam will grant GrowthX and John Google Search Console access to enable performance tracking.

---

## Key Topics

### The Problem: Inaccurate AI Search Results

  - The project's primary objective is to correct outdated and inaccurate information in AI search results.
  - **Example:** A prospect's AI comparison of Jamf vs. Fleet falsely stated, "Fleet is not an MDM."
  - **Root Cause:** AI models misinterpret Fleet's nuanced capabilities, such as its ability to be used *alongside* another MDM.
  - **Solution:** Publish fresh, authoritative content to update AI models with accurate information.

### Content Strategy & Prioritization

  - **Airtable Topics:** Brock has reviewed \~20 of 79 topics, approving \>10.
      - **Rationale for Rejection:** Avoiding competition with official docs and reproducing generic content (e.g., "resetting a device to factory default").
  - **SEO Alignment:** The initial list of topics is too product-centric for high SEO ranking.
      - **Solution:** Repurpose topics with SEO-friendly titles (e.g., "Manage Android devices") and include product details in H2s or body text.
  - **Phase 2: Programmatic SEO for osquery Data Tables**
      - **Opportunity:** Create a blog post for each of Fleet's 335 osquery data tables.
      - **Benefit:** This project would create a massive, differentiated content library that highlights a unique product feature.
      - **Execution:** A programmatic SEO approach will be used, generating pages from a template.

### Calibration Blog Review

  - **Purpose:** Align on writing voice and style.
  - **Feedback:** The draft is authoritative and deep, which is critical for AI visibility.
      - **John:** Superficial posts fail with AI; deep content is essential.
      - **Brock:** Content must be factually accurate to build trust.
  - **Feature Image:** The AI-generated image successfully captures the Fleet brand aesthetic.
      - **Next Step:** Irena will get final approval from Mike T.

### Performance Measurement

  - **Tool:** A Looker dashboard will track performance.
  - **Key Metric:** LLM referral traffic, showing which AI models are driving users to the site.
  - **Context:** John noted a trend at his previous company where AI summaries increased impressions but decreased clicks.
      - **Goal:** Use the dashboard to analyze this trend for Fleet.
  - **Access:** Google Search Console access is required to build the dashboard.

---

## Action Items

**Erik O’Brien (GrowthX)**
- Collect calibration blog feedback from Brock, Sam, John, Irena; then incorporate and tag GrowthX
- Review Brock’s Airtable list; return prioritized SEO-aligned topics to Brock
- Track programmatic SEO for osquery data tables; plan Phase 2 w/ Sam

**Brock Walters (Fleet)**
- Approve 10–25 Airtable topics for Erik; then GrowthX draft 3 posts next week
- Add GitHub emoji to Search Console thread to add to Sam’s board

**Sam Pfluger (Fleet)**
- Grant GrowthX and John Search Console access; then GrowthX build 7-tab Looker dashboard

**John Jeremiah (Fleet)**
- Request Search Console access from Sam

---

## Transcript
**Erik O'Brien:** Hey, John, Erik, how are you?

**Erik O'Brien:** Doing well.

**Erik O'Brien:** How's your week going?

**John Jeremiah: That's good.

**John Jeremiah: New week, new job, started on Monday, so yeah.

**Erik O'Brien:** All right.

**Erik O'Brien:** Welcome to the club.

**John Jeremiah: Yeah.

**John Jeremiah: How about you?

**John Jeremiah: How's your week going?

**Erik O'Brien:** It's good.

**Erik O'Brien:** Today's been a long been Busy, but that's typical for Wednesdays for me.

**Erik O'Brien:** No complaints.

**John Jeremiah: Yeah, I don't complain.

**John Jeremiah: I have nothing to complain about.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Where are you joining fleet from?

**Erik O'Brien:** Where are you at before?

**John Jeremiah: Uh, is that Blink Ops?

**Erik O'Brien:** Blink Ops.

**Erik O'Brien:** I'm aware of them.

**John Jeremiah: A little Israeli startup doing,

**John Jeremiah: Uh, they're competing with tines and torque, um, so, security automation, gotcha, hey folks, hey Sam, how's it going, not too bad about yourself, not bad, I'm the same.

**Sam Pfluger: You

**Sam Pfluger: I love that file that somebody shared with me.

**Sam Pfluger: Ooh, fancy.

**Sam Pfluger: I like it.

**Erik O'Brien:** Yeah, included a header image, and I know, I think the existing blogs don't have any, but I thought we'd throw one in there just in case.

**Sam Pfluger: Yeah, I think they do.

**Sam Pfluger: Well, some, some of them do, it kind of depends.

**Sam Pfluger: More, yeah, I mean, most of the things, our file structure is a little, not strange, but the way the website kind of renders it.

**Sam Pfluger: It can make it look a little stranger than it actually is, but most of the guides, actually, you're right, don't have images, but we can always add something in there.

**Sam Pfluger: And we have like news, we have stuff sprinkled in there with uh, some of them have videos, it of doesn't matter.

**Erik O'Brien:** I assume Brock or Irina are going to join today too?

**Sam Pfluger: Yeah, I'm kind of hoping Brock can show up and give us a little bit more here but like, kind of depends on, I have questions, although I don't want to, I'm going to wait.

**John Jeremiah: Do you get done with what you're doing, Erik?

**Erik O'Brien:** Oh, I was just checking to see if I had gotten a note from Brock, but it didn't look like it.

**John Jeremiah: Okay.

**John Jeremiah: So, I mean, I'm brand new.

**John Jeremiah: Started on Monday.

**John Jeremiah: And I want to learn more about how you guys are doing what you're doing and kind of the bigger picture.

**John Jeremiah: So if you have time on this call, we could do that, or we could do it separately.

**John Jeremiah: We can do it separately, but I'd really like to learn more about the background of how GrowthX is doing.

**John Jeremiah: What you guys are doing and how you're, more importantly, how you're, how we're going to measure the impact.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Absolutely.

**Brock Walters: Hey, everybody.

**Brock Walters: Sorry for joining me.

**Brock Walters: Hey, John.

**Brock Walters: Nice to see you.

**John Jeremiah: Hey, Brock.

**John Jeremiah: Good to see you, too.

**Brock Walters: Okay, cool.

**Brock Walters: So I'm assuming you guys got a chance to introduce yourselves a little bit.

**Brock Walters: And, Erik, we're hiring a whole, a small army of marketing people here.

**Brock Walters: So, John is, I invited him to this.

**Brock Walters: next time.

**Brock Walters: We're hiring a head of marketing, Ashish.

**Brock Walters: John's going to be reporting to him.

**Brock Walters: Irena, hello.

**Brock Walters: I'm assuming Irena's going to be working on that team as well.

**Brock Walters: So I don't know where that will leave me in the mix, but I'm happy to still be working on this stuff.

**Brock Walters: And as I've said all along, my, the way I see my function here is not to necessarily be guiding what the marketing message is, but just to be here to ensure that whatever the marketing message has in it is true.

**Brock Walters: Maybe, maybe John will want to start lying right out of the gate.

**Sam Pfluger: I, but I, I doubt so.

**Brock Walters: So, so, uh, uh, what, what, what, where does that leave us with our, uh, with our regular update here?

**Brock Walters: do you guys, do you have anything you want to talk about?

**Erik O'Brien:** I've got an agenda for us.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** So you should have seen Ada shared the calibration blog, both in the Slack, and then you should have got an email from Google Drive as well.

**Brock Walters: Yep, I saw that.

**Erik O'Brien:** So, yep, the goal here is really just to align on voice and kind of writing style to make sure that we're artifacts are appropriately being pulled into the generation process and the output looks up to par for you guys.

**Erik O'Brien:** Cool.

**Erik O'Brien:** So, knowing that you just got it today, we'll give you a couple days to kind of review and leave any feedback.

**Erik O'Brien:** You can just leave it directly in that Google Doc.

**Erik O'Brien:** And then once everybody's had a chance to review, you can just tag us to say, hey, review's done.

**Erik O'Brien:** Incorporate this feedback.

**Brock Walters: Cool.

**Brock Walters: And, John, just for your benefit, we have a pretty detailed thing in the company handbook, which I'm assuming you at least know about or maybe you've looked at it.

**Brock Walters: It's part of the stuff you're probably going to be going through during onboarding.

**Brock Walters: And that's the

**Brock Walters: You know, Mike is pretty particular about how we write things and how we even even the formatting of certain things.

**Brock Walters: And so I feel pretty confident that we're going to get the style and kind of if you describe the style as the voice, maybe they're two different things.

**Brock Walters: But I feel pretty confident that we're going to get the style right just because we have so much detail about what the fleet writing style should be in the public handbook and the growthx people basically just took a lot of that to kind of define this.

**Brock Walters: So I think I have high confidence in at least that part of it, that it's going to be very close, but I'm happy to review it when I get a chance.

**Erik O'Brien:** Wonderful.

**Sam Pfluger: And there's the calibration blog, or no, I see it.

**Sam Pfluger: Never mind.

**Sam Pfluger: It says it right there.

**Sam Pfluger: It's the first name of the file.

**Sam Pfluger: Just the same thing I'm looking at.

**Erik O'Brien:** Got it.

**Erik O'Brien:** Yep, you've got it.

**Sam Pfluger: Cool.

**Brock Walters: And, you know, obviously, everybody's opinion on that here is welcome.

**Brock Walters: If, Sam, if you don't think it's the right, if it doesn't sound like you enough, right, then.

**Sam Pfluger: I don't know about me.

**Brock Walters: Cool.

**Brock Walters: So, yeah, I will, I have not looked at it yet because I've been neck deep in other stuff, but I intend to look at it today.

**Erik O'Brien:** Right.

**Brock Walters: Sounds great.

**Erik O'Brien:** And then, I know you had a chance to go through all the assignments in Airtable, or at least some of them.

**Brock Walters: went through, I think there's 79 of them, and I think I went through 20 of them.

**Brock Walters: I kind of rejected a couple of them out of hand.

**Brock Walters: I was trying to put a meaningful comment in each one as to why.

**Brock Walters: Some of them were kind of like, maybe we should come back to that later.

**Brock Walters: Some of them were just like, topics that I don't know that we...

**Brock Walters: What I don't want is for whatever official documentation we have to somehow be in competition with these blog posts that are being auto-generated, right?

**Brock Walters: That's my fear I have.

**Brock Walters: So I just need to kind of, and then when I opened, expanded the list and saw, oh, there's only, you know, there's only 60 more to do.

**Brock Walters: I will, but I will get through it, I promise.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Yeah, I think, because you don't need to go through all of them, I think if we can get just like 10 for us to work on over the next few weeks.

**Brock Walters: Oh, cool.

**Brock Walters: Well, I think I already gave the thumbs up to more than 10 of them, but I just kind of axed maybe three or four.

**Brock Walters: But I will make sure that there's plenty to start with, you know, like 25 or something, because most of the topics look good.

**Brock Walters: And some of them I won't, at the risk of, you know, putting everybody to sleep and boring everyone to death, I would give you.

**Brock Walters: I'll my justification for why the ones that were chosen weren't good.

**Brock Walters: And just to give you an example, I'm absolutely certain that Jamf has an article on resetting a device to factory default.

**Brock Walters: The problem is there's a little bit of controversy around whether or not the lock and wipe and features in Fleet should be used for doing that.

**Brock Walters: And so then, okay, what are we talking about?

**Brock Walters: Are we talking about Apple's documentation for setting a device to factory default or Windows documentation?

**Brock Walters: If so, why are we reproducing documentation that already exists that probably isn't going to be as good as the companies that make the stuff?

**Brock Walters: So those are the kind of decisions that I'm making, and maybe I'm being too slicey-dicey about it.

**Brock Walters: But when we're starting here, I do want to be careful with this project because, as I've told you probably 500 times, two years from now, I want all the information out on...

**Brock Walters: ...

**Brock Walters: The world about Fleet to be true and right.

**Brock Walters: So, okay.

**Erik O'Brien:** Yeah, I would say if they're, like, quickly scanned, if there's ones that are just like a sure yes.

**Brock Walters: Okay, I will do that.

**Erik O'Brien:** I can go faster through there.

**Erik O'Brien:** Take time.

**Brock Walters: Awesome.

**Erik O'Brien:** Then Ada, unfortunately, got sick today, so she wasn't able to join, but she did have some thoughts on your stream assignments list.

**Erik O'Brien:** Mainly that they're very product-oriented, so they don't really mesh well with the SEO kind of keyword intent that we're looking to go after.

**Erik O'Brien:** Yep.

**Erik O'Brien:** So, wouldn't rank very high and be difficult to kind of rank for in the search results, but we can extract some keywords from some of the topics.

**Erik O'Brien:** And so, I think it's not like none of these are worth our time.

**Erik O'Brien:** It's more of like some of them will be.

**Erik O'Brien:** And others will have to kind of rethink how do we kind of align to a different keyword where the topic makes sense.

**Brock Walters: Yeah, and I think that totally, that's totally legitimate.

**Brock Walters: Like, I don't know, again, that list has nothing to do with what's popular in the world, right?

**Brock Walters: That list has only everything to do with what Brock thinks is important about talking about the features.

**Brock Walters: Now, I suppose there's some alignment there, because I'm definitely interested in promoting features of Fleet that are new, and that, obviously, we wouldn't be building these features if, A, people were, you know, people are asking us for them, and B, we think other customers will benefit from those same features, right?

**Brock Walters: Right.

**Brock Walters: So, I think that there's some alignment there.

**Brock Walters: In other words, the things that...

**Brock Walters: That people are looking for in terms of a device management platform, surely some of those blog topics would be relevant to them.

**Brock Walters: But there are other things that are, I agree with that assessment that they're product based and it's, but I think I said this on the last call about that kind of analysis, which is why I wanted to give you the list.

**Brock Walters: It's like, okay, if you're looking at Jamf's blog posts to determine what is popular, well, what's being left out of that analysis is features that Fleet might have that are perfectly parallel with what Jamf has, but they call it a different thing.

**Brock Walters: Or, what we're leaving out of the mix completely is features that Fleet has that are differentiating that Jamf doesn't have.

**Brock Walters: So, I understand that the mission is this SEO.

**Brock Walters: But I just feel like maybe what's missing from that is differentiation of features, but maybe I'm just not understanding the mission.

**Erik O'Brien:** No, I think that definitely makes sense.

**Erik O'Brien:** Like we definitely want to incorporate as many kind of references to fleet and the product and features that you guys have.

**Erik O'Brien:** It's just how do we do that aligned with keyword and kind of, so some of the titles, that's where like she's saying, you know, we can do a post with like manage Android devices.

**Erik O'Brien:** And that'd be the main title and then manage Android devices with fleet as like an H2 title.

**Erik O'Brien:** So we get to have push a little bit more of those feature sets within the piece itself.

**Brock Walters: Cool.

**Brock Walters: And if she's willing to like, you know, have a discussion about that, I'm sure we could go through the list and kind of arrive at or, or we can let you guys do whatever analysis that you would.

**Brock Walters: Do on that list and see, okay, like, hey, if we do an article on this topic, the thing that would make it, put it in front of the most eyeballs would be saying it this way.

**Brock Walters: Yep.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So I think that's kind of what our, we'll probably take a pass on that and come back with more feedback of like, here's the ones we could prioritize from your list.

**Erik O'Brien:** Okay.

**Brock Walters: Because we have.

**Brock Walters: there's, there's one other, sorry to cut you off.

**Brock Walters: There's one other thing that I guess I, I didn't make it very clear.

**Brock Walters: I, I was kind of, uh, I wasn't meaning to be unclear about it, but I realized after I sent it that it was kind of an inside baseball thing.

**Brock Walters: So, uh, Mike, this isn't, certainly isn't Mike's first foray into trying to make, you know, fleet content popular in the world, right?

**Brock Walters: So, uh, one thing he had me doing and one thing he does and has been doing is.

**Brock Walters: So, uh,

**Brock Walters: Assuming that there's a way of putting the fleet website content out into the world where people are going to see it more, right?

**Brock Walters: Because, and I think the thinking is, the content already exists.

**Brock Walters: So it's just kind of like, okay, make it more visible in more places.

**Brock Walters: And one of the projects he had me do was going through what we are currently calling data tables.

**Brock Walters: Now, this gets very technical and nerdy pretty quick, but Fleet uses osquery.

**Brock Walters: OSquery is a way of getting data from operating systems that data is expressed as a SQL table.

**Brock Walters: So we have documentation for every one of those SQL tables that can express data from enrolled devices.

**Brock Walters: What he had me do last year was go through the 335 tables that we have for osquery and start making a post about each one.

**Brock Walters: Now, there were two aspects to that project.

**Brock Walters: One of them was to make the example queries better, because some of the tables that we have in this documentation don't even have an example.

**Brock Walters: So that was one part of the project.

**Brock Walters: The other part of the project, though, was just to say like, hey, what does this table do?

**Brock Walters: Does this table have some meaningful value for our customers or for people out in the world that aren't our customers that might go, hey, that's a really cool thing and I might want to use that.

**Brock Walters: And talk about the tables in that way.

**Brock Walters: So what I put in the message to Aida was, okay, not only these 24 topics, because I couldn't think of 50, but we probably should have a blog post on every single one of the tables.

**Brock Walters: And some of them are quite obscure, but I mean, like, I don't know.

**Brock Walters: That content exists.

**Brock Walters: That project should be something that we should do.

**Brock Walters: We would be driving people towards the website, driving people towards...

**Brock Walters: Towards understanding why the product is differentiated, and maybe I'm focusing on that too much, but we do have this built-in set of features that we can talk about, and we could literally have a blog post for every single one of those.

**Brock Walters: So in addition to whatever 79 you've come up with and the 25 that I came up with, there's 330 more.

**Brock Walters: That's all I was trying to say.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** Yeah, think that would be something we would look to kind of do as, like, a programmatic SEO play, and so it would basically come up with, like, here's what the page format and layout would look like for an example one.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And then be able to kind of programmatically just launch those pages.

**Brock Walters: Yeah, that would be super cool.

**Brock Walters: And that would be brilliant, I think, as well, because if the...

**Brock Walters: The way we were doing it was just on LinkedIn, right?

**Brock Walters: And LinkedIn doesn't give you a lot of formatting options for things like code blocks, right?

**Brock Walters: So, like, it was just kind of, you can put some nerd stuff in there, but it doesn't look great.

**Brock Walters: And the whole point of the LinkedIn post was to point people back to the data table page.

**Brock Walters: But if we came up with some blog post format that was, like, super awesome that had, like, you know, formatted code blocks and looked really nice, and then we just started cranking those out, one for each one, that could be super cool.

**Brock Walters: But maybe that's phase two, I don't know.

**Erik O'Brien:** Yeah, I think that would be phase two once we get through kind of calibration and make sure we're all aligned off, like, how the non-programmatic stuff would play.

**Erik O'Brien:** But it'd also probably be a larger conversation on how we would do that, probably with Sam, assuming we could kind of get in there and create them all.

**Erik O'Brien:** Like how many different pull requests that would take.

**Erik O'Brien:** So we'll definitely keep that on the list of ideas and I'll start tracking that so that once we do shift to phase two, we can have that as kind of like a long-term, hey, this is a priority that we want to get out content for these pieces.

**Brock Walters: Awesome.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So in the calibration blog, let me switch screens here.

**Erik O'Brien:** Got too many windows open.

**Brock Walters: Me too.

**Sam Pfluger: No such thing.

**Brock Walters: So your computer starts to slow down and crash like mine does every day.

**Brock Walters: You need a new computer, that's it.

**Erik O'Brien:** So you'll see in the calibration blog, we included a feature image.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And so these are generated as part of the pipeline, like based off the topic at hand.

**Brock Walters: Here's mentioned.

**Brock Walters: I get

**Brock Walters: And there's like a robot, there's like a robot brain that created that little picture, is that what you're saying?

**Erik O'Brien:** We have a designer that creates the prompts, the robot brain takes those prompts, and looks at the content of the article, and then creates these featured images.

**Brock Walters: Okay, do you ever get anything weird in there, like a, like a sunflower or an elephant?

**Erik O'Brien:** You know what mean?

**Erik O'Brien:** Not, not, not unintentionally.

**Erik O'Brien:** Um, we, we did have one customer that has very like floral abstract, uh, featured images, and so there definitely was a sunflower.

**Brock Walters: Amazing.

**Erik O'Brien:** Um, but yeah, I think this is essentialized color of Apple devices.

**Erik O'Brien:** So this is one we picked for the article and put in there, but, um, overall, what are your thoughts on just look and feel?

**Brock Walters: I'm not the right person.

**Sam Pfluger: The, I mean, the look and feel, I can tell that it grabbed, I know at least, uh, the flower pot.

**Sam Pfluger: A little, it's a cube of butter, I don't care what anybody says, but the far bottom little cube of butter.

**Sam Pfluger: That does look like butter.

**Sam Pfluger: It's directly from the website, so I mean, it did a good job on...

**Brock Walters: Oh yeah, I mean, that does look, I mean, that drawing looks fleetish, yeah, I would say that.

**Sam Pfluger: Yeah, I mean, if you go between that, it's like, the test is, if I go between that and the, uh, and the...

**Sam Pfluger: Yeah, Erik, like, go put another tab and go to the, go to fleetdm.com.

**Brock Walters: Is it jarring?

**Brock Walters: I mean, it's, it's, that, that artwork is in everything, and it's one particular artist, and, like, without having copped that guy's work, yeah, that little drawing kind of looked like a drawing that you So if you scroll down a bit, I can show you, keep going, maybe...

**Brock Walters: Oh, there it Oh, yeah.

**Brock Walters: So...

**Brock Walters: Why is that butter there?

**Sam Pfluger: I don't know.

**Brock Walters: I forgot what they told me it is.

**Sam Pfluger: It's butter.

**Brock Walters: It's floating butter.

**Brock Walters: It's floating butter.

**Brock Walters: Okay.

**Sam Pfluger: I mean, everybody likes butter unless you're It's the good stuff.

**Sam Pfluger: It's yellow, not white.

**Brock Walters: So, you know.

**Sam Pfluger: That's right.

**Brock Walters: can stay true to that.

**Brock Walters: Okay, cool.

**Brock Walters: I mean, for me, thumbs up on that.

**Brock Walters: But I don't know if I'm the definitive.

**Sam Pfluger: Are we talking about just the picture?

**Sam Pfluger: Yeah.

**Brock Walters: Yeah.

**Brock Walters: I mean, you have an E?

**Sam Pfluger: I mean, Mike T is the ultimate.

**Sam Pfluger: The ultimate.

**Sam Pfluger: you know, John, I'd be interested to hear what you think.

**John Jeremiah: I wear polka dot and stripes.

**Brock Walters: I'm not the designer.

**Brock Walters: Fair enough.

**John Jeremiah: I mean, I think, look, I think it's fine.

**John Jeremiah: It connects back with our brand.

**John Jeremiah: It uses imagery from our brand.

**John Jeremiah: I think it's okay.

**John Jeremiah: I don't think people are going to, from an SEO perspective, I mean, for me, at least, the challenge with these kind of blogs, this kind of an exercise is understanding what's our objective.

**Brock Walters: Well, I can tell.

**Brock Walters: tell you that, John.

**Brock Walters: And it's a very good question and the right one to be asking.

**Brock Walters: I think I can make it simple.

**Brock Walters: The purpose of this is not necessarily for SEO on the website, but it's to ensure that AI searches for Fleet topics have the right information.

**Brock Walters: And what we've already proven is that they don't.

**Brock Walters: So part of this is because Fleet has developed MDM features so quickly, but I literally just sent these guys two weeks ago, an AI search that someone at a prospect did on they basically typed into some AI comparison between Jamf and Fleet.

**Brock Walters: And the reason it got sent to me is because I happen to be friendly with the guy who works there.

**Brock Walters: And so the result of this was in multiple places in that output, it said Fleet is not an MDM.

**Brock Walters: Jamf is an MDM, Fleet is

**Brock Walters: It's not.

**Brock Walters: And so everybody at that company, except for the guy who actually knows what an MDM is, you know, came away from this exercise with the idea that, like, well, gee, Dan, why are you even bringing us this product for, you know, to evaluate because they're not even the same thing.

**Brock Walters: So what these guys do, hopefully, what they're going to do by putting this content out in the world is change those results.

**John Jeremiah: Yeah, no, no.

**John Jeremiah: And, and, and I, have, I have history with GrowthX going way, way, way, way, way back when Marcel and I both launched TechBeacon at HP Software.

**John Jeremiah: So I, I, I know, I know Marcel and we worked side by side.

**John Jeremiah: I was the first guy to post on TechBeacon when we launched that together.

**John Jeremiah: But the, the point I was getting at those is that blogs and posts like this, whether it's SEO or EIE, I mean, AIO or EIEIO, I don't know what the right acronym is for, at the end of the day, you're writing for a machine.

**John Jeremiah: At some level, you want to make sure the content, the machine's going to read it.

**John Jeremiah: And the thing I like about this post is it's authoritative and it's deep.

**Brock Walters: It's not a superficial post.

**John Jeremiah: Yeah.

**John Jeremiah: The superficial definition level posts don't work anymore because the AI tools all ignore them.

**John Jeremiah: So this feels to me like the right kind of thing that will help to solve that problem.

**John Jeremiah: But my point is, is I think the picture, the graphics, the AI, that's not really going to drive it at a great level.

**John Jeremiah: So I think if it's good enough, I'm of the opinion to ship it, right?

**John Jeremiah: It doesn't have to be perfect.

**John Jeremiah: Yeah.

**John Jeremiah: But yeah, this is good stuff.

**John Jeremiah: And I think it's the more of these we do and the more we can do these faster, the better.

**Irena Reedy: Agree.

**Irena Reedy: I would like to just run past the graphics by my TV just to double shape because it's, and just get the final.

**Irena Reedy: So.

**Brock Walters: Mike is the style counselor.

**Sam Pfluger: So here's how I think we do that.

**Sam Pfluger: Best way to do that is with a PR.

**Sam Pfluger: There's one that allows us to, if we just get the, you know, the rubber stamp on it, then we ship it.

**Sam Pfluger: And there's no more conversation.

**Irena Reedy: It's done and on to the next one.

**Sam Pfluger: So, I think the next thing we need, and it might be in your, in your agenda, Erik, is, and I saw a little bit of it in the Slack thread as well, is me to kind of help you guys get spun up on, cool, if we were going to ship this tomorrow, how do we make a pull request?

**Brock Walters: Because that's the real, that's the real and Sam, that's why I had Erik invite you, because we had talked originally on the first call, I think, about what Erik asked about access to the website.

**Brock Walters: You know, I don't even really know what we're talking about, or how you're, how you guys, how you and Mike envision this tour.

**Brock Walters: Right.

**Sam Pfluger: So, here's the problem is I'm going to jump in one minute.

**Erik O'Brien:** I know you shared the recording, so we can definitely reference that and get as far as we can, and if we run into any issues, we can kind of circle back with you, but I think we have enough just off the video you sent to at least get in there and submit the pull request.

**Sam Pfluger: Did I send a video?

**Erik O'Brien:** Yeah.

**Sam Pfluger: Cool.

**Sam Pfluger: Look at me go.

**Sam Pfluger: I'm proud of my former self.

**Erik O'Brien:** The one thing we don't have yet is access to Google Search Console, and so that's the one thing we need access to.

**Sam Pfluger: Yeah.

**Sam Pfluger: I'll dig into that.

**Sam Pfluger: I've got to get with Mike and figure that out.

**Sam Pfluger: I'm pretty sure I have access to that.

**Sam Pfluger: Yeah.

**Brock Walters: I just assumed you did.

**Sam Pfluger: If you don't, we'll figure it out.

**Sam Pfluger: I probably do, but I might not know that

**Sam Pfluger: I do, I'll get with Eric, he'll probably be the other one that knows all the nooks and crannies.

**Sam Pfluger: Okay, well I think Sam, this is just like, do you need an action item on your board for this?

**Sam Pfluger: No, I'll go, yeah, actually, yeah Brock, if you have that thread handy, you can just slap the github emoji on that thing.

**Sam Pfluger: Okay, I hope that's what I'll do.

**Sam Pfluger: You know, make sure it ends up on our board.

**Sam Pfluger: Okay.

**Sam Pfluger: Because that has the email that I need to add to it anyway.

**Sam Pfluger: So that way, whenever I do figure out how to weasel my way in there, I can just add that email.

**Sam Pfluger: And then I'll, I'll hit you guys back up in the channel and let you know it's done.

**Brock Walters: Sounds good.

**Sam Pfluger: Cool.

**Sam Pfluger: All right, I'm gonna jump to the next one.

**John Jeremiah: All right.

**Erik O'Brien:** See you, Sam.

**Brock Walters: Thanks everyone.

**Erik O'Brien:** For next week, we'll, have, so after we get your guys feedback on this original calibration article, we'll have.

**Erik O'Brien:** have.

**Erik O'Brien:** of tips.

**Erik O'Brien:** Three new articles, based off what you've approved in Airtable, and so we'll keep things moving on our end.

**Erik O'Brien:** And then I know, John, you had questions more specific about how we're doing this.

**John Jeremiah: Yeah, I'd like to get a better sense as to how we're, I mean, from a, you know, I can look at Ahrefs or SEMrush and other tools to get a good handle, at least to get a guess as to, in Google Search Console, I can get a handle as to where we're at in general from an SEO perspective.

**John Jeremiah: So, LLMs and prompts are another animal entirely, and last gig, was, we were looking at how do we measure the traffic coming from them from looking at website traffic in the logs on the backend, how are you guys doing that?

**Erik O'Brien:** Yep, so, once we get access to Search Console, we'll put together a Looker dashboard, and it'll have seven different tabs on it, but one of them is LLM referral traffic.

**Erik O'Brien:** And so, we can see which LLM is referring to the site.

**Brock Walters: And which pages they're landing on.

**Brock Walters: And Looker is kind of like Google, like Tableau kind of visualization thing.

**John Jeremiah: Yeah, I know Looker.

**John Jeremiah: I mean, I'm familiar with, I'm familiar enough, I'm familiar with Looker and Search Console.

**John Jeremiah: So it'll be interesting.

**John Jeremiah: I'll be really interested in seeing how that data is flowing through and how we're seeing the net impact of it.

**John Jeremiah: So, you know, I'm going to ping Sam up too and say, tell him I need access to Search Console as well.

**John Jeremiah: It's one of those, those things that, well, one, want to see if you guys had the same drop off I had at Blink, which is in March of this year, when the AI results started to become popular in Google search, all of a sudden impressions went up, but clicks went down.

**Erik O'Brien:** Yeah.

**Brock Walters: I mean, that's definitely a story I've been reading about, you know, I don't have any data that shows that, but it's certainly something people see, they've been talking about.

**Brock Walters: I have screenshots of it.

**John Jeremiah: Yeah.

**John Jeremiah: have

**John Jeremiah: Screenshots of it, and I've talked to other people who've seen the same thing happen in other places.

**Brock Walters: Totally.

**Brock Walters: And just anecdotally, I hear people saying things like, I never use Google anymore.

**Brock Walters: And I'm just like, what?

**Brock Walters: I don't know if that's what's driving it, but that does seem to be a thing.

**John Jeremiah: Well, mean, when you use Google, you're using an AI now.

**John Jeremiah: Oh, totally.

**John Jeremiah: Yeah.

**John Jeremiah: And what happened was in March, they rolled out AI summaries.

**John Jeremiah: And all of a sudden, AI summaries started to summarize the results.

**John Jeremiah: And that meant that all of the old SEO tactics of writing a simple glossary, this or what is this or what is that, that was simple and short, those tactics all failed because that was all encapsulated in the AI summary.

**John Jeremiah: Yeah.

**John Jeremiah: And so people would get the answer to the AI summary and never go to the website.

**John Jeremiah: You'd show up in the search result, but your clicks all went away.

**Brock Walters: Yeah, that makes sense.

**John Jeremiah: So that started to happen.

**John Jeremiah: But yeah, I'm really interested in following along because this is something.

**John Jeremiah: I was working on looking at how to solve at my last place, and so you guys are approaching it here, which will be interesting.

**John Jeremiah: But yeah, it's fun that Marcel and I get to cross paths again.

**Erik O'Brien:** Yeah, absolutely.

**John Jeremiah: I'll have to tell him.

**Erik O'Brien:** Yeah, do.

**John Jeremiah: Tell him hi from tech beacon days long ago.

**John Jeremiah: But he and I both had less gray hair.

**Erik O'Brien:** Yeah, I think from the AI overviews perspective, we just did an analysis for another client, and it's, they're still really experimental, like 50% of keywords tracked over seven months, only showed up in one month, and then the next month, you look for the same exact query, and it didn't show up or didn't show an AI overview.

**Erik O'Brien:** And so it's a bit of a art and science to try to figure out kind of what's going to get pulled in, and is it freshness of content, is it style?

**Erik O'Brien:** Structure of content.

**John Jeremiah: I think that's the understatement of this call.

**John Jeremiah: I think there's a lot of art that looks like science, but it's a lot of art trying to figure this out right now.

**Erik O'Brien:** And I think we're all in the same boat, but yeah, I'm with you.

**Erik O'Brien:** Yeah, I mean, we published an article for Lovable just a couple weeks ago, and it's already getting cited by ChatGPT.

**Erik O'Brien:** So we're like, okay, freshness comparison articles seem to be things that they like.

**Erik O'Brien:** Want to go towards, and it's more like the middle and bottom funnel kind of consideration stuff.

**Erik O'Brien:** Definitional, like you're probably not going to get cited, you might get pulled into the answer somewhere.

**Erik O'Brien:** But that's stuff that we track on a platform called Scrunch, that we just fill with a bunch of prompts that are related to your company and your audiences, and then try to track like, are we showing up?

**Erik O'Brien:** If so, like which LLMs are citing us, or at least showing us in the answer.

**Erik O'Brien:** And so we can at least use that to guide.

**Erik O'Brien:** lot thought.

**Erik O'Brien:** really see We mean, I've

**Erik O'Brien:** What different topics we want to kind of boost content in versus which ones are we showing up pretty well.

**John Jeremiah: That gets into the prompt anticipation, just like from a keyword perspective, anticipating the keywords people are going to search for.

**Erik O'Brien:** You have to start to anticipate the prompts that you want to show up for.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Instead of the two to three word keyword, it's like a 12 word.

**John Jeremiah: Yeah.

**John Jeremiah: Have we done that yet here as far as an exercise saying, what do we think the target prompts or the prompts we want to be competing for?

**Brock Walters: We've just started looking at the material that's been provided and just kind of all the things that we talked about today, reviewing the actual potential titles for blog posts and talked about some of the seed data for kind of getting the voice and the style of the company, right?

**John Jeremiah: Cool.

**John Jeremiah: This is cool.

**John Jeremiah: I'm glad we're doing this.

**John Jeremiah: This is going to be a, it's a good, good, I'm glad this has started.

**Brock Walters: Yeah.

**Brock Walters: I feel the same way.

**John Jeremiah: And I knew that you'd be interested or at least that.

**John Jeremiah: Yeah.

**John Jeremiah: No.

**John Jeremiah: Well, and I think the other thing we've got to do, and we've got to really always think about is, and this is where the challenge I think comes in, and I know we're all way over on time, but I don't have anything to tell the employee call, but I think the challenge is ultimately is writing for the reader about helping them answer the problem or solve the problem that they're facing.

**John Jeremiah: Um, and, and that all almost always means that we, it's less about us.

**Brock Walters: It's more about them.

**Brock Walters: I totally agree with that.

**Brock Walters: And that's why I'm so concerned about these articles being true.

**Brock Walters: You know what I mean?

**Brock Walters: I mean, it's like, we have to be saying things that are actually true things about the product and not just like transformational IT, you know, that's just nonsense.

**John Jeremiah: We need, yeah, no, no, I mean, content has to be valuable for the reader and they have to educate the reader and it has to help the reader solve the problem that the reader.

**John Jeremiah: And, and for me, that's, that's the North Star of it all.

**John Jeremiah: Yeah.

**John Jeremiah: And, you know, the, the, the buzzwords, the promotion, hype is not where it isn't going to help grow the product.

**John Jeremiah: What's going to grow the product is people get it becoming, finding, finding, finding that the content is trustworthy and reliable.

**John Jeremiah: Yeah.

**Brock Walters: But I think that you're, I think you're kind of onto something there because like, I think that that's almost the function that people expect the AIs to perform now.

**Brock Walters: And, and so it's like, in other words, please, please, you know, disregard all the marketing jazz and find me the articles that actually show me something like a real comparison between these two products that I'm interested in.

**Brock Walters: And, and, the problem is that the results in that comparison have been somehow given validity by the fact that everybody won't shut up about AI.

**Brock Walters: And the results are actually .

**John Jeremiah: They may be, they may be, well, and to be quite honest, there's so many variables that it depends on, you know, it depends on the model, depends on how much context has been used in the model.

**John Jeremiah: I mean, I have been doing a lot of work with AI, and I find that the longer I work with a model in a chat prompt where there's a large context window, then eventually the quality starts to drop.

**John Jeremiah: And I have to kill that, and I have to kill that chat and start again with, with, when freshly seeded again with whatever I want to talk about.

**John Jeremiah: And I have multiple examples of where I've had long running conversations on a specific topic, usually as code.

**John Jeremiah: But at some point, all of a sudden it starts just flaking out and, and loses and becomes incoherent.

**John Jeremiah: Incoherent is probably an overstatement, but it, it's, it becomes dumb.

**John Jeremiah: yeah.

**John Jeremiah: Yeah.

**John Jeremiah: And the only way to, to make it better is to reset.

**Brock Walters: I had found one other strategy, which is that if you always start with the same, like, text file, and you basically say, like, this is the context for the conversation we're going to have.

**John Jeremiah: That's right.

**John Jeremiah: No, that's absolutely right.

**John Jeremiah: And in my scenario, a lot of what I've been doing is coding.

**Brock Walters: I've been coding an app.

**Brock Walters: Ever been late for a meeting?

**Brock Walters: Every meeting?

**John Jeremiah: This meeting?

**John Jeremiah: So I have an app in the App Store that I wrote last couple of months.

**John Jeremiah: I'm in beta testing.

**John Jeremiah: It's called Beyond Time.

**John Jeremiah: And basically, it's a notification app that bugs you.

**John Jeremiah: It's as if you had an executive assistant to alert you and say, show up for the meeting.

**John Jeremiah: So it's a simple app, simple concept.

**John Jeremiah: But in Vibe Coding and working with either Gemini or Claude, in both cases, as I would be iterating with it, if I let the prompt go too long, as far as too many sessions, eventually, it would start giving me really, really crappy answers.

**Brock Walters: You know, I have a very conspiratorial...

**Brock Walters: I theory about this, and I know we're over, here's the, Claude just introduced, I didn't get this theory until I saw that Claude announced this.

**Brock Walters: Claude announced a feature called Memories.

**Brock Walters: And what the Memories feature promises is that it will do better with your context of everything you've ever told it.

**Brock Walters: And I'm like, oh, well, maybe that's why they've been making the context so crap, so that they could sell another feature to keep it.

**Brock Walters: Of course, that's why they've been doing it that way.

**John Jeremiah: Yeah, perhaps.

**John Jeremiah: I've been using, I don't buy Claude, I buy Poe.

**John Jeremiah: So I use Poe to manage all the different tools, that plus Gemini.

**John Jeremiah: But it is interesting.

**John Jeremiah: But I know exactly, I understand the problem that we're dealing with.

**John Jeremiah: And especially if somebody doesn't know any better, and they ask ChatGPT a question.

**John Jeremiah: And I think ChatGPT is the most, is one of the harder ones to pin down, because I think it's more artistic as far as coming back with responses.

**Brock Walters: Meaning it makes  up more often than not.

**John Jeremiah: Yeah.

**Brock Walters: That was a very diplomatic way of saying that.

**John Jeremiah: That's why I don't use it.

**Brock Walters: I use Gemini and Claude.

**John Jeremiah: But if you're not an informed user and know enough to double-click, you will take the answer as being authoritative.

**Brock Walters: And to me, I know that obviously in your role, you're interested in the marketing performance.

**Brock Walters: I am more interested in correcting that because if you – people are relying on this information and the information is three years old.

**Brock Walters: It was true three years ago that Fleet was not an MDM.

**Brock Walters: But the fact that these things are still surfacing that as a fact is the thing that we're fighting.

**John Jeremiah: Yeah, but do we have the – does our content still say that out there?

**John Jeremiah: If I were to do a deep search on our website, am I going to find stuff that says that?

**John Jeremiah: You might.

**Brock Walters: And here's why.

**Brock Walters: It's because Fleet is so unique as a product.

**Brock Walters: It's because there are plenty of places where we probably say in our own promotional material or in blogs about Fleet that you can use Fleet alongside another MDM.

**Brock Walters: Well, why would you do that if Fleet was an MDM?

**Brock Walters: But the fact is both of those things are true.

**Brock Walters: So we're not only dealing with like two or three-year-old information about like Fleet didn't used to have these features, but now it does.

**Brock Walters: But we're also dealing with the reality that there is a use case for Fleet where you have an MDM, and you're also using Fleet.

**Brock Walters: And I just don't believe that these tools will have the subtlety necessary to tell that story accurately.

**Brock Walters: And obviously, because I just got someone two weeks ago who sent me a thing that showed me that that's true.

**Brock Walters: And that goes back, Eric, I'm not trying to push my agenda, but that goes back to why I want to have some of these more deeply technical topics is because I feel like we have to not just talk.

**Brock Walters: We're the places where we're directly competing with products like Jamf, but we have to somehow factor into this story eventually how we differentiate.

**Brock Walters: Because I really believe that that's the key to getting the results right.

**Brock Walters: If it's true that these LLMs are searching for fresh content, then we have to be able to tell the story in the way that's current now and get rid of the version of the story from two or three years ago.

**Brock Walters: And maybe that's an oversimplification of how it works, but the product is complex.

**Brock Walters: You know, how do we talk about it?

**John Jeremiah: Yeah, think if there, you know, the thing I'm thinking about Brock is if there are things that we think are absolutely false that we have said in the past or that have changed over time.

**John Jeremiah: I think if we can figure out where that is and scrub it, that would be helpful.

**Brock Walters: Yeah, I mean, I don't think there's anything currently on Fleet's website or documentation that says Fleet is not an MDM, but there's definitely stuff that says you can use Fleet alongside another MDM, and I can easily see where a model would misinterpret that information because MDMs tend to be exclusive.

**Brock Walters: Well, like you would never use two if you didn't have to, unless you were having one for each platform, which is another thing that we're trying to sell, you know, as a positive attribute of the product.

**Brock Walters: It's like, hey, you can consolidate on Fleet.

**Brock Walters: So, I see it as two problems.

**Brock Walters: One, the product is complex, where I can see where models would not understand the subtleties of what it can do.

**Brock Walters: And two, there's old information before Fleet had its current features.

**Brock Walters: So, we can talk about this endlessly.

**John Jeremiah: Yeah, can go on.

**John Jeremiah: Eric, we're taking over Eric's time.

**Brock Walters: Eric, thanks for running along with us.

**Brock Walters: Yeah.

**Brock Walters: Well, I think Eric is interested in this stuff, or at least I've gotten the impression that he was.

**Brock Walters: So, hopefully I know.

**Erik O'Brien:** It's, I mean, more context for me.

**Erik O'Brien:** I have a somewhat limited context window, but I think the more I get from you guys, the more I can kind of dial in for the content that we need to go after.

**Brock Walters: Yeah, and you've been very helpful so far, and I promise we will go over that stuff that's in there, and I'll make sure that I have at least 10 more articles that are ready to go.

**Brock Walters: Wonderful.

**John Jeremiah: All right.

**Brock Walters: Thank you, guys.

**Erik O'Brien:** Thank you.

**John Jeremiah: Thank you.

**John Jeremiah: Take care, everybody.

**John Jeremiah: Bye.

**John Jeremiah: Bye.
