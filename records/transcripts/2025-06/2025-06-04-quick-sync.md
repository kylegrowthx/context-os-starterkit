# Quick sync

<metadata>
date: 2025-06-04
time: 17:44 UTC
duration: 22 minutes
organizer: tiandra@growthx.ai
participants: Tiandra Burns (GrowthX), Feyisayo Odedeyi (GrowthX)
fathom_recording_id: 66499992
fathom_url: https://fathom.video/calls/318651860
share_url: https://fathom.video/share/skwBE_BV_cR_EB1sNN6ucW2ipJKX6xAF
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Tiandra walked Feyisayo through the Airby Article Refresher workflow in AROPS, covering URL input, keyword extraction from URLs, ChatGPT article formatting, and Surfer SEO keyword optimization targeting a minimum score of 80. When Feyisayo reported getting inconsistent Surfer scores (30, 72, 91) for identical content, Tiandra identified H2/H3 tag corruption during copy-paste operations as a likely cause and recommended using the highest score (91) to proceed. Feyisayo is now ready to practice the workflow independently.

---

## Context

Feyisayo is a GrowthX team member working on the Airbyte account doing article refreshes — updating and optimizing existing content using a systematic workflow. During the session, Feyisayo was hitting confusion around Surfer SEO's scoring inconsistencies and asked Tiandra for a walkthrough of the complete process. Tiandra is experienced with this workflow and was walking the team through it, screen-sharing to demonstrate each step of the process in AROPS, ChatGPT, and Surfer SEO.

---

## Relevance

- **To GrowthX Delivery:** The Airby Article Refresher workflow represents a documented, repeatable process for content optimization using AROPS + ChatGPT + Surfer SEO. This is operational delivery methodology for Airbyte refreshes; understanding the workflow including H2/H3 tag handling and keyword distribution is critical for consistency. Feyisayo now has a reference recording for training.
- **To CheckThat:** Surfer SEO is a key tool in the stack. The scoring inconsistencies Feyisayo encountered may warrant further investigation into how Surfer's algorithm handles identical content pasted multiple times, or whether there are API/platform quirks worth documenting.

---

## Overview

- Airby Article Refresher workflow involves using AROPS, ChatGPT, and Surfer SEO to update and optimize content
- Inconsistent Surfer SEO scores (30, 72, 91) for the same content caused confusion; using the highest score (91) is recommended
- H2/H3 tag inconsistencies when copying content between platforms can affect Surfer SEO scores
- Keywords for article optimization are sourced from the URL and Surfer SEO suggestions

---

## Key Topics

### Airby Article Refresher Workflow

  - Use AROPS to generate initial content based on URL and keyword
  - Copy output to ChatGPT for refinement and proper article formatting
  - Add keywords from Surfer SEO to ChatGPT for further optimization
  - Aim for \~2000 words (varies by client; Airbyte has in-depth articles)
  - Copy final content to Surfer SEO, aiming for a score of 80+
  - Make final adjustments (add sections, fix headers) to reach the target score
  - Transfer optimized content to Google Docs

### Surfer SEO Scoring Inconsistencies

  - Same content yielded vastly different scores: 30, 72, and 91
  - Possible causes:
      - H2/H3 tag inconsistencies when copying between platforms
      - Surfer SEO's internal algorithm fluctuations
  - Solution: Use the highest score (91) and proceed with optimization

### Keyword Selection and Usage

  - Primary keyword found at the end of the article URL
  - Additional keywords sourced from Surfer SEO suggestions
  - Copy all relevant keywords into the AROPS "refresh instructions"
  - Use ChatGPT to incorporate missing keywords naturally into the content

### Content Length Considerations

  - Airbyte articles tend to be in-depth
  - Aim for \~2000 words, but adjust based on original article length and topic depth
  - 4000+ words may be too long; compare with original article length

---

## Action Items

**Feyisayo Odedeyi (GrowthX)**
- Practice Airby Article Refresher workflow in AROPS. Use recording as reference. Focus on keyword insertion, ChatGPT prompts, Surfer score improvement.

---

## Transcript
**Tiandra Burns:** So here is the workflow.

**Tiandra Burns:** It's called Airby Article Refresher.

**Tiandra Burns:** And so here we're going to take the URL that's in our spreadsheet, add the article topic.

**Tiandra Burns:** In this case, I add the keyword.

**Tiandra Burns:** And then here, these stay the same.

**Tiandra Burns:** you kind of just like, I'm going to do an impromptu one, for instance.

**Tiandra Burns:** You just drag and drop these here.

**Tiandra Burns:** Then you will click run the workflow.

**Tiandra Burns:** This may take some time.

**Tiandra Burns:** Let's see.

**Tiandra Burns:** It may not do it now, but for instance, it'll do this.

**Tiandra Burns:** It will ask you to put the keyword in because it won't generate the keyword.

**Tiandra Burns:** So the key word for these article refreshes, have you been able to figure out where they are?

**Tiandra Burns:** Sorry, you're muted.

**Tiandra Burns:** Um, well, the key word is at the end of the, um, is at the end of the, the, um, the URL.

**Tiandra Burns:** Um, so you would put the key word here, and then you would come and run workflow.

**Tiandra Burns:** It will give you an output like this.

**Tiandra Burns:** And then I don't normally look at these because it gets, it can get confusing.

**Tiandra Burns:** Sometimes I do, sometimes I don't, um, run this, run this workflow.

**Tiandra Burns:** It will give you an output like this.

**Tiandra Burns:** So then after this, you have to add your keywords.

**Tiandra Burns:** And these are the keywords that, these are like the instructions.

**Tiandra Burns:** I lost you.

**Feyisayo Odedeyi:** Sorry, my connection went bad.

**Feyisayo Odedeyi:** So I was asking, I was saying that I asked about the keywords, there was supposed to be like a list of keywords that we would use.

**Feyisayo Odedeyi:** And I said,

**Feyisayo Odedeyi:** You I should take the primary keywords from the topic of the article, I guess, and that's what I've been doing, sort of.

**Feyisayo Odedeyi:** Is there a page for, like, document for the keywords?

**Tiandra Burns:** Yes, so I guess you missed my whole, you didn't see me do any of this then, I guess.

**Tiandra Burns:** Explain, you didn't see me explain the, explain this here, before you dropped off?

**Feyisayo Odedeyi:** And it's because I'm tripping off a few bits.

**Feyisayo Odedeyi:** Oh, okay.

**Tiandra Burns:** So I go to AROPS.

**Tiandra Burns:** I'm here on AROPS, can you see my screen?

**Tiandra Burns:** Yes, I can.

**Tiandra Burns:** Okay, so I'm in AROPS, I'm going to start again, I'm So, this is the article refresher we use for AIRBITE, I sent you the link, you're going to copy and paste whatever the article is that you want to use.

**Tiandra Burns:** The...

**Tiandra Burns:** The...

**Tiandra Burns:** The...

**Tiandra Burns:** Keyword is at the end of this link here, data imputation, right?

**Tiandra Burns:** For example, you copy and paste the company name in the about, that always stays the same.

**Tiandra Burns:** You'll run this, it'll spit out an input.

**Tiandra Burns:** Here in our case, it doesn't, so you have to put in your keyword here.

**Tiandra Burns:** Then you go here and run workflow, right?

**Tiandra Burns:** It will give you a brief.

**Tiandra Burns:** Once that's done, you run this again.

**Tiandra Burns:** It will give you research output.

**Tiandra Burns:** Now, here's where the keywords come in.

**Tiandra Burns:** It will give you this output, and you can kind of scroll and see if it's giving you similar to what you had.

**Tiandra Burns:** And you'll see up here, like, it's a lot of keywords, right?

**Tiandra Burns:** So then you'll want to come here and say, I'm going to use a different number.

**Tiandra Burns:** You might say, you want to add the keywords here, right?

**Tiandra Burns:** And I get that from here.

**Tiandra Burns:** So I copy and paste all of the keywords from Surfer.

**Tiandra Burns:** And I add them all here into the refresh instructions.

**Tiandra Burns:** I also can tell it to make it more concise or shorten it, but it hasn't.

**Tiandra Burns:** I haven't needed to give it these instructions.

**Tiandra Burns:** So for these last three that I did, I just gave it and fed it the keywords.

**Tiandra Burns:** And then you hit run workflow.

**Tiandra Burns:** After this, it should give you an output, which is like this.

**Tiandra Burns:** And it's the article you can kind of check to see up here in the right hand corner if they've given you the right amount of words.

**Tiandra Burns:** So the next step that I take.

**Tiandra Burns:** take.

**Feyisayo Odedeyi:** How do you determine the right amount of words?

**Tiandra Burns:** For instance, if it's 4,000 or 3,000, it's probably too many keywords.

**Tiandra Burns:** Okay.

**Tiandra Burns:** depending on what the subject is or how many keywords were in the last article.

**Tiandra Burns:** So if you get an output, I mean, for instance here, don't know if it tells you.

**Tiandra Burns:** Yeah.

**Tiandra Burns:** So if this was like 4,000 words, I don't know.

**Tiandra Burns:** I might have to see how much the original article was, you know?

**Feyisayo Odedeyi:** Yeah.

**Feyisayo Odedeyi:** But the average pay should be 2,000.

**Tiandra Burns:** Well, it really depends on each client.

**Tiandra Burns:** For air bites, for example.

**Feyisayo Odedeyi:** Yeah.

**Feyisayo Odedeyi:** Because it looks like there are like 2,000, slightly above 2,000, slightly below 2,000.

**Feyisayo Odedeyi:** Yeah.

**Feyisayo Odedeyi:** Yeah.

**Tiandra Burns:** They have very in-depth articles.

**Tiandra Burns:** So I copy here with this copy function.

**Tiandra Burns:** I come here and I give ChatGPT a prompt.

**Tiandra Burns:** And I say, take this text and make it to a proper article.

**Tiandra Burns:** I copy and paste the whole thing here.

**Tiandra Burns:** And then it will generate the output.

**Tiandra Burns:** And here you can kind of see, like, is it similar to what it was?

**Tiandra Burns:** So I say, after it's given me this, I say, okay, now let's go back and add in the keywords.

**Tiandra Burns:** Because if you take it directly from here, the first output, it's not going to give it, you're probably not going to get closest to the score you want.

**Tiandra Burns:** So I kind of do it double again.

**Tiandra Burns:** I add the keywords.

**Tiandra Burns:** And then it gives me the new content.

**Tiandra Burns:** And then

**Tiandra Burns:** And I copy and paste it here, I see what my score is, I see if I'm missing any keywords, if I'm missing keywords, I might highlight them, come back down to ChatGPT, where, let's see, oh, here we go.

**Tiandra Burns:** And I'd say, is there a section we can create that adds value to this article using these keywords?

**Tiandra Burns:** And they'll say, yes, but this is a great section that you can add, make sure it doesn't bulge your keywords.

**Tiandra Burns:** And then I say, great, well, where would this section be best?

**Tiandra Burns:** And then I go in and add this section to here.

**Tiandra Burns:** Then I see what I'm looking at and make sure my headers are all good here, H2, because sometimes when you copy from other...

**Tiandra Burns:** Places, it kind of switches it, and then I'm working on getting to 80 now, and from here, copy and paste to the Google Doc.

**Tiandra Burns:** Was that helpful?

**Tiandra Burns:** Do you have any questions?

**Feyisayo Odedeyi:** Sorry.

**Feyisayo Odedeyi:** I think I'm just going to have to keep training for myself.

**Feyisayo Odedeyi:** So if I was able to do one, what was just really confusing me today was the problem that I had with the same article having different scores on so far.

**Feyisayo Odedeyi:** Okay, don't worry too much about that.

**Tiandra Burns:** Just select the one I told you to select.

**Tiandra Burns:** I hadn't...

**Tiandra Burns:** No, not that one.

**Feyisayo Odedeyi:** Oh, this one, the 60, and the...

**Tiandra Burns:** Okay, so when I went Okay, so went to...

**Feyisayo Odedeyi:** Byte's website, when I went to the original content of the refresh article, and I posted it to Surfer, the first score was about 30, I posted it again, like I was trying to work on it, and I was able to get it up to 60, but obviously the score is supposed to be 80, so I was thinking like what was I doing wrong, I started to start over again, I posted it and then, I posted it from the website, and then the score was 90, so I was just confused like, why is the same article, without any edits, having two different scores?

**Tiandra Burns:** Let me stop sharing, and then let me check something.

**Feyisayo Odedeyi:** So this is the third one I even did, this is 72.

**Feyisayo Odedeyi:** The second one I did was 91, and the first one was very low, the first one was 30, and all of them have the same content throughout, this is straight from Airbyte, this is like without edits or anything, so it's the same content, but with different scores, so I'm not sure why it's asking that.

**Feyisayo Odedeyi:** Do you have...

**Feyisayo Odedeyi:** Go ahead.

**Feyisayo Odedeyi:** I have...

**Feyisayo Odedeyi:** The other...

**Tiandra Burns:** For the other one to compare.

**Tiandra Burns:** Yes, this is the first one.

**Feyisayo Odedeyi:** I mean, this is one and this is the other one.

**Feyisayo Odedeyi:** These are the last two I did.

**Feyisayo Odedeyi:** And they're literally the same thing, but see, this is 72.

**Feyisayo Odedeyi:** Can you see my screen?

**Tiandra Burns:** No, I only see the 91.

**Tiandra Burns:** It's stuck on one page.

**Feyisayo Odedeyi:** Oh, my God.

**Feyisayo Odedeyi:** Let me try it.

**Feyisayo Odedeyi:** I think that's for Google Maps.

**Feyisayo Odedeyi:** Let me stop sharing.

**Feyisayo Odedeyi:** Thank you.

**Feyisayo Odedeyi:** Okay, so this one is 17.

**Tiandra Burns:** You have all of these things between here.

**Tiandra Burns:** Yeah, keep going like that.

**Tiandra Burns:** Let's see.

**Tiandra Burns:** Two, four images.

**Tiandra Burns:** Ah, here we go.

**Tiandra Burns:** Let's see.

**Feyisayo Odedeyi:** But it's the same thing here.

**Tiandra Burns:** I need you to look at something, yeah.

**Tiandra Burns:** I need you to stop scrolling so I can see the H tags here.

**Tiandra Burns:** Okay, let's go slowly down to data warehouses.

**Tiandra Burns:** Scroll up again for me so I can see.

**Feyisayo Odedeyi:** Okay, go.

**Tiandra Burns:** Okay, make sure also these in between things, these the author, the time, make sure you delete those as well.

**Feyisayo Odedeyi:** Okay, so we go down.

**Feyisayo Odedeyi:** just saying, like, I copied, I copied this straight from the website.

**Feyisayo Odedeyi:** Yes, sometimes it.

**Feyisayo Odedeyi:** I have the same thing on, on the other page.

**Feyisayo Odedeyi:** Like, I did not take anything out and it has different scores.

**Feyisayo Odedeyi:** Oh, look, it's 91 thinking like it was supposed to take the same thing.

**Feyisayo Odedeyi:** This is 91, this is 72, but it's literally the same content.

**Feyisayo Odedeyi:** Oh, there we go.

**Feyisayo Odedeyi:** I didn't see if was anything.

**Feyisayo Odedeyi:** didn't didn't

**Tiandra Burns:** I understand, but what I'm saying is, look, look, you see how popular Data Lake Solution says H3?

**Tiandra Burns:** That should be an H2, right?

**Feyisayo Odedeyi:** yeah.

**Tiandra Burns:** So sometimes even when you copy and paste it from another place, it will mess up the order of the H2 tags.

**Tiandra Burns:** It's happened to me going from Google Docs to Surfer.

**Tiandra Burns:** It's happened to me going from the Workflows to Surfer, ChatGPT to Surfer.

**Tiandra Burns:** So sometimes even if you copy and paste it exactly, when you put it into Surfer, sometimes it will mess up the order of the H2 and H3 tags.

**Tiandra Burns:** So sometimes you'll have to go back and check.

**Tiandra Burns:** So then the 91, then I would say go with that because maybe it just...

**Tiandra Burns:** Okay, let me try to delete all of this.

**Tiandra Burns:** That's a good idea, let's see.

**Tiandra Burns:** I don't know, it keeps going from 91 to, I don't know what's happening, but it's 91 now.

**Feyisayo Odedeyi:** Yeah, it's 91, this one is 91, but this is 72, but since you said I should use the one that is 91, I think that's what I would do.

**Feyisayo Odedeyi:** So I'm just saying, like, what if I did not paste it a second and third time?

**Feyisayo Odedeyi:** was about to work from 30.

**Feyisayo Odedeyi:** I'll also fix the...

**Feyisayo Odedeyi:** I have...

**Tiandra Burns:** Yeah, I don't know.

**Tiandra Burns:** I've never had this kind of situation.

**Tiandra Burns:** Only with the headings, which may toggle the end result.

**Tiandra Burns:** Like, this is my first time doing the refreshes so far, and I...

**Tiandra Burns:** I haven't had this, I haven't, I mean, honestly, I also haven't tried to copy and paste it twice into Surfer two different times.

**Tiandra Burns:** I only do it once, so I can't say.

**Feyisayo Odedeyi:** do it once because the first time it was so low, and I was trying to start over the second time, and then I just realized that scores are a difference.

**Feyisayo Odedeyi:** And I'll work with this one, and I'll try and use AROPS to fix the article, and hopefully this will be nice.

**Feyisayo Odedeyi:** Thank you very much.

**Tiandra Burns:** You're welcome.

**Tiandra Burns:** I hope it helps.

**Tiandra Burns:** I'm going to share this recording with you, and so that way you can look back at the AROPS workflow, and if you need anything, me.

**Feyisayo Odedeyi:** All right, thank you very much, Sandra.

**Feyisayo Odedeyi:** Of course, I hope it's helpful.

**Tiandra Burns:** I'll be on, so anything you need.

**Feyisayo Odedeyi:** Thanks.

**Tiandra Burns:** You're welcome.

**Tiandra Burns:** Bye.

**Tiandra Burns:** Bye.
