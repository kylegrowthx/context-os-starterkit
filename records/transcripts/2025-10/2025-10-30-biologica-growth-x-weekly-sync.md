# Biologica <> Growth X - Weekly Sync

<metadata>
date: 2025-10-30
time: 20:01 UTC
duration: 25 minutes
organizer: team@growthxlabs.com
participants: Matthew Panzarino (GrowthX), Brian Magida (Biologica), Elizabeth Zwillinger (Biologica)
fathom_recording_id: 98169772
fathom_url: https://fathom.video/calls/458181511
share_url: https://fathom.video/share/cJza9SBjBj1PDV57fsGJoYzKyyQq2Hz7
source: fathom
enriched_on: 2025-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX and Biologica aligned on fixes for content quality and the medical review process. A researcher regression causing broken links was fixed by Daniel; the team agreed to review articles from the past few weeks and spot-check the next batch. MD tagging will shift from over-conservative to clinical-focused—reserving tags for medical claims rather than simple data points like "maintain bedroom temps between 60-68°F." GrowthX will provide bibliographies alongside articles to help Biologica's medical reviewer (Maggie) identify unreliable sources and apply a blacklist. On images, the team finalized a workflow: GrowthX delivers lead images (less face-focused) and interstitial images as links in Google Docs, and Biologica places them in a CMS image block to maintain consistent formatting. Matthew is finalizing content expansion options (symptom explainers and ingredient education) to present by Friday for scalable, lower-review-burden content.

---

## Context

Biologica is a women's health content and product company focused on menopause-related symptoms and wellness. GrowthX is delivering content at scale for Biologica's website—articles with medical claims that require clinical review. This is a mid-engagement sync addressing operational pain points: content quality (link validation), medical review efficiency (tagging), and visual consistency (image strategy). Brian Magida leads Biologica's editorial and regulatory side; Elizabeth Zwillinger manages day-to-day coordination with Maggie, their medical reviewer. Matthew Panzarino leads GrowthX's delivery on this account. The relationship is mature enough that both teams are now planning phase two: scalable content with less manual review overhead.

---

## Relevance

**To GrowthX Delivery:**
- Researcher regression identified and fixed; next batch articles will be validated for broken/unreliable links. Review past 2 weeks' content as due diligence.
- MD tagging instruction set needs refinement: shift from conservative over-tagging to clinical framework alignment. Focus tags on medical claims, not data points with authoritative sources.
- Bibliography workflow implemented: deliver plain-text list with links for each article to help medical reviewer identify unreliable sources and manage blocklist.
- Image strategy finalized: lead images (tire crops, full face shots) delivered as links, placed by client via CMS image block to avoid formatting issues.
- Fact-checker logic enhancement: implement disease-modifying study filter to prevent studies on disease-affected populations from supporting claims about baseline health status.

**To GrowthX Business Development:**
- Client expanding into phase two scalable content (symptom explainers, ingredient education). Matthew presenting options Friday for feedback—indicates growth potential and account expansion.
- Strong delivery momentum: Brian reviewed 15-20 articles and sees quality improvement. Pain point is regulatory/review, not content quality.
- Renewal/expansion signal: focus shifting from content creation to optimization and scaling, suggesting maturity and trust in GrowthX output.

---

## Overview

- **Link Quality Fix:** A researcher regression causing bad links is fixed. The next article batch will be correct, and GrowthX will review the last few weeks' content.
- **MD Tagging Refined:** MD tags will now be reserved for medical claims, not simple facts. This reduces review load and improves focus.
- **Image Strategy Updated:** New lead images will be less person-focused (tire crops, full face shots). GrowthX will deliver images as links for Biologica to place.
- **Content Expansion:** GrowthX is developing a strategy for scalable content (e.g., symptom explainers) that avoids cannibalizing existing keyword authority.

---

## Key Topics

### Link Quality & Fact-Checking

  - **Problem:** Recent articles contained broken or unreliable third-party links.
  - **Cause:** A researcher regression. The new researcher finds sources (e.g., paywalled papers) that the fact-checker cannot access, preventing it from validating claims.
  - **Solution:** Daniel pushed a fix. The next article batch will reflect this.
  - **Action:** GrowthX will review articles from the last few weeks to correct any lingering link issues.

### MD Tagging Process

  - **Problem:** The current process is overly conservative, tagging simple facts (e.g., "75% of women experience hot flashes") and creating an unnecessary review burden for Maggie.
  - **Solution:** GrowthX will update its instruction set to reserve MD tags for medical claims requiring expert review.
  - **Example:** A fact like "maintain bedroom temps between 60-68°F" is a data point, not a medical claim, and does not require an MD tag if the source is authoritative.

### Medical Review Enhancements

  - **Bibliography:** GrowthX will provide a plain-text bibliography with links for each article.
      - **Rationale:** This gives Maggie an easy way to check all sources at once, improving efficiency and helping to identify unreliable sources (e.g., the Sleep Foundation, which is funded by mattress companies).
  - **Source Filtering:** GrowthX will investigate logic to filter out irrelevant sources.
      - **Example:** A study on women with HIV should not be used to support a general claim about women's health.

### Image Strategy

  - **Updates:**
      - **Lead Images:** Less person-focused (tire crops, full face shots) to shift focus from "who is this person" to "it is a person."
      - **Interstitial Images:** GrowthX will prioritize generating images that match Biologica's previously approved aesthetic.
  - **Workflow:**
      - GrowthX will deliver two images per article (lead + interstitial) as links in the Google Doc.
      - Biologica will handle image placement to ensure consistent formatting across the site.
      - **Recommendation:** Use a CMS image block to allow GrowthX to call the image programmatically, preventing layout issues.
  - **Backfill:** After approval of the new style, GrowthX will generate images for all existing articles to replace outdated ones (e.g., those with text overlays).

### Content Expansion Strategy

  - **Goal:** Develop a scalable content strategy with a lighter review burden for Biologica.
  - **Challenge:** Avoid cannibalizing keywords from existing product-focused content while finding topics with enough depth for dozens of articles.
  - **Potential Pillars:**
      - Symptom explainers
      - Ingredient education
  - **Status:** Matthew will present concrete options for feedback by Friday or early next week.

### CMS Tagging

  - **Goal:** Automate CMS tagging to match Airtable's topic clusters (e.g., perimenopause, postmenopause).
  - **Plan:** GrowthX will map Airtable clusters to CMS tags and include them in the article metadata.
  - **Future:** This setup enables automated publishing and tagging via API (e.g., Shopify) for large content batches.

---

## Action Items

**Brian Magida**
- Review 1–2 articles from next batch; send feedback to Matthew
- Send Google Meet link to Liz; then hold quick follow-up

**Matthew Panzarino**
- Review MD-tagging instructions; tweak to reduce over-tagging
- Implement fact-checker logic to exclude disease-modifying studies
- Deliver next batch to Brian/Liz: articles + 2 images/article (Airtable/Drive links)
- Send Brian/Liz examples of consumer sites using image blocks
- Send Brian 2–3 content expansion options for feedback
- Align w/ Brian/Liz on Airtable→CMS tag mapping; then update Airtable + publishing

**Elizabeth Zwillinger**
- Email Maggie re: bibliography/sidecar; then inform Matthew

---

## Transcript
**Brian Magida:** This meeting is being recorded.

**Brian Magida:** whatever reason, the most recent pipeline didn't get copied and pasted, so she made changes to the one prior, but it sounds like you guys can take her feedback and just apply it, whether it's proactively or reactively to whatever comes out of the pipeline, so that feels good.

**Brian Magida:** think the biggest, and Liz, I don't know if you have any other thoughts that you want to go over.

**Brian Magida:** For me, like, I think the biggest hurdle we need to get over is, and it sounds like perhaps you've addressed this in the past week, but it's making sure that, like, the links themselves are all, like, good.

**Brian Magida:** Like, the links to the third-party articles, because, candidly, like, when I'm reading through this stuff, I'm checking some of them, but there are just so many links, I can't, like, possibly check every single link.

**Matthew Panzarino:** No, no, no, no, no, that's our job, right?

**Matthew Panzarino:** Like, we should be doing that, and I think what happened is we had a regression in the researcher.

**Matthew Panzarino:** And Daniel pushed an update yesterday.

**Matthew Panzarino:** And so the next batch, I would love for you to evaluate those.

**Matthew Panzarino:** Don't do all of them.

**Matthew Panzarino:** Do one.

**Matthew Panzarino:** Because I'm pretty confident that this will be rectified.

**Matthew Panzarino:** But yeah, I think you got hit with a regression.

**Matthew Panzarino:** And we're using a new researcher, not to get it too into the weeds, but it just finds stuff that is like behind paywalls and like research papers that may be buried or whatever.

**Matthew Panzarino:** And basically what happens is the fact checker is unable to find those same references.

**Matthew Panzarino:** And so it's unable to flag incorrect stuff.

**Matthew Panzarino:** So it's okay.

**Matthew Panzarino:** I think we got it.

**Matthew Panzarino:** But I feel you on that.

**Matthew Panzarino:** And we don't want her to have to like feel like every link is unreliable.

**Matthew Panzarino:** That's not, you know, that's not a baseline good for us.

**Matthew Panzarino:** So this next should be rectified.

**Matthew Panzarino:** And then we shouldn't have that problem too much going forward.

**Brian Magida:** And once like, I guess we'll go through one or two articles.

**Brian Magida:** Let's just assume we give you the thumbs up on it.

**Brian Magida:** Will you then be able to like, will you run every article like through that? Do we have any that like maybe slipped through the cracks?

**Matthew Panzarino:** so the researcher is part of every article creation process.

**Matthew Panzarino:** So we're talking about like base stuff we're adjusting.

**Matthew Panzarino:** So anything that we create goes through it.

**Matthew Panzarino:** That's why it was like we trusted it and then we had a regression.

**Matthew Panzarino:** So it's our fault for that catch again, but we've caught it now.

**Matthew Panzarino:** So yeah, anything in the future that you see should not have like a bunch of wrong links and stuff.

**Brian Magida:** Yeah, I understood the future.

**Brian Magida:** I'm more just thinking like as general peace of mind.

**Brian Magida:** once that we've reviewed, like can we put them back through that?

**Brian Magida:** We can take a look.

**Matthew Panzarino:** Yeah, we'll take a look through them.

**Matthew Panzarino:** Basically, it would be like reviewed and approved.

**Matthew Panzarino:** We'll go take a look through all those and then make sure that we're okay.

**Matthew Panzarino:** I don't think that it's a long-running issue.

**Brian Magida:** So at the most, we'll probably have to check in the last couple of weeks.

**Brian Magida:** Okay.

**Brian Magida:** Okay, cool.

**Brian Magida:** And then Liz was just catching me up on Nancy.

**Brian Magida:** It's going to take a look.

**Brian Magida:** She's got a bunch of articles.

**Brian Magida:** And so I'm hoping in the next like day or two, there's additional set of articles that I'll be able to hand back over to Maggie to give like one review on the regulatory side.

**Brian Magida:** One thing that did come up, and I know like Liz has flagged this actually before, I forget if I communicated this, but Maggie just flagged it again, is just around the quantity of like MD tags, where I think we should just align on essentially like what constitutes an MD tag, because I think there might be too many, like we just might be too conservative in terms of flagging things that are tagged.

**Brian Magida:** And I'm sure this is like very hard to get dialed in correctly, but I think we just need to look at that specific process, because ideally there's just less like tags that as we're doing like control app to go through.

**Brian Magida:** It's like, I think she's reviewing a lot of stuff that she just doesn't have to necessarily.

**Brian Magida:** And then there might even be things that are not being captured by the MD tag.

**Elizabeth Zwillinger:** That should be, so.

**Elizabeth Zwillinger:** I think that's very, very, very rare.

**Brian Magida:** Okay.

**Elizabeth Zwillinger:** The other way around.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It's 100%, we just probably are overly conservative there in our instruction set because we're just like, is this, just check, just make sure, you know.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I'll look at our instruction set there and see if we can tweak it to compensate for that.

**Matthew Panzarino:** This may actually be related to, we just ran some tests on the framework that you gave us, just the clinical framework.

**Brian Magida:** Okay.

**Matthew Panzarino:** You know, do these adhere or whatever?

**Matthew Panzarino:** The good news is, there's not a big difference between what we've been delivering and what the framework says.

**Matthew Panzarino:** There's a couple of things here and there that are probably things that would have gotten caught in MD review, you know.

**Matthew Panzarino:** But if we can prevent them from even having to be caught, so much the better.

**Elizabeth Zwillinger:** One of them is like data.

**Elizabeth Zwillinger:** It's almost, it's not even MD review, it's data.

**Elizabeth Zwillinger:** It's a data review.

**Elizabeth Zwillinger:** So I'll give you a perfect example.

**Elizabeth Zwillinger:** Um, I'm in the perimenopausal vassal motor.

**Elizabeth Zwillinger:** in motor.

**Elizabeth Zwillinger:** Symptoms, causes, and relief.

**Elizabeth Zwillinger:** don't even know which, but it says, evidence-based cooling strategies include maintaining bedroom temperatures between 60 and 68 degrees, and that's MD tagged.

**Elizabeth Zwillinger:** That's like, if there's a, if we're, if that evidence is pointing, there's a link, a hyperlink to sleepfoundation.org, which that's actually, I'm pretty sure that's a paid, um, it's not a good source, because it's like paid for by mattress companies.

**Matthew Panzarino:** Oh, I see.

**Elizabeth Zwillinger:** That's all those reviews, but regardless, okay, so that's not a great source, but let's put that aside for a second.

**Elizabeth Zwillinger:** Assuming that that's like a link to a actually published article about sleep temperatures, that's not really an MD that needs to review that, and that's like a fact checker that's like, does this data, is that data pulled from that link?

**Matthew Panzarino:** Right.

**Matthew Panzarino:** Yeah, let's say it's an, it's an authoritative source, and we're comfortable with it.

**Matthew Panzarino:** They pull it from PubMed, if you actually look at their source of 60 to 68 degrees.

**Matthew Panzarino:** it's to be jump scale.

**Matthew Panzarino:** We can probably just change that link.

**Matthew Panzarino:** But yeah, we'll keep coming up with that source.

**Elizabeth Zwillinger:** Yeah, but in the same article.

**Matthew Panzarino:** It's just, if the link, if the data is proven out, and it's a factual claim, and the link is secure, we don't need to MD tag it.

**Matthew Panzarino:** We were a little misdemeanor about this today, because we were talking about linking, and we were thinking, like, do we, we probably don't need to flag this for her, because it's like, is it correct?

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Then, hey, it's true.

**Elizabeth Zwillinger:** So, yeah.

**Elizabeth Zwillinger:** Yeah, there's another one on the same article, about 75% of women experience hot flashes, and it's links to a good, good resource.

**Matthew Panzarino:** Okay.

**Elizabeth Zwillinger:** So.

**Matthew Panzarino:** Okay, yeah, that's good.

**Matthew Panzarino:** That was great, and it literally, we were just talking about it today, Nana brought it up, and I was like, yeah, it's a really good point, because it's like, the number of MD tags has been proliferating a bit, and I think it's just getting really antsy about, like, are you sure?

**Matthew Panzarino:** You know, so we'll, we'll assume that if we, if we get our fact checking correct, and if the links, like a PubMed link, has authoritative sourcing, which our fact checkers should catch.

**Matthew Panzarino:** Then we're not going to MD-tag those.

**Matthew Panzarino:** And we'll MD-tag stuff that's pre-floating statements about, you know, or medical claims that should probably have eyes on.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Untune that.

**Elizabeth Zwillinger:** I think that would make a huge difference in workflow.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Does that feel okay to you, Brian?

**Elizabeth Zwillinger:** Okay.

**Matthew Panzarino:** Yeah.

**Brian Magida:** No, I was just giving a thumbs up.

**Brian Magida:** That feels good to me.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, it's just human nature.

**Matthew Panzarino:** If we flood the zone for her, too, it just becomes more difficult for her to catch stuff that is important.

**Matthew Panzarino:** So, yeah.

**Brian Magida:** And then, yeah, and from, like, the, I'll let Liz opine on this, because she'll have a better perspective.

**Brian Magida:** But from my perspective, I've read, like, at least 15 to 20 articles, like, recently through the new pipeline.

**Brian Magida:** And, like, broadly speaking, they feel very good.

**Brian Magida:** Like, I think, like, the pain that we're going through right now is really just more on this.

**Brian Magida:** It's, like, more medical review side. So if we can make some of these tweaks, I think it'll just put everything in a really good spot.

**Elizabeth Zwillinger:** Okay, cool.

**Matthew Panzarino:** Yeah, and if there are things that would make her life easier from like a data perspective or anything like that, we can also provide those as sidecar files or things like that.

**Matthew Panzarino:** Like, as an example, if she wanted a bibliography or, you know, bibliography of sources alongside it or anything like that, let us know how to make her life easier too, you know?

**Matthew Panzarino:** Like, we will find ways to make it easy.

**Matthew Panzarino:** We have the data, so it's not like we can't slice it in ways that make it easier.

**Matthew Panzarino:** I'm not saying you have to, but as she enters this and she's talking about it or you're talking about it with her, don't hesitate.

**Elizabeth Zwillinger:** Okay, I will follow up with her immediately after this call and let you know right away, because I think as you're saying it, a bibliography actually could be quite useful.

**Elizabeth Zwillinger:** Yeah.

**Matthew Panzarino:** She's kind of finding her own sources.

**Matthew Panzarino:** Mm-hmm, yeah.

**Matthew Panzarino:** Yeah, and like the, as an example, the mattress company paid for survey, like that kind of thing.

**Matthew Panzarino:** She's kind of she's know,

**Matthew Panzarino:** It's easy for her to flag and be like, hey, can we add this to our block list?

**Matthew Panzarino:** And we're like, sure, yeah, no problem.

**Matthew Panzarino:** We'll put it on the list of things not to reference, right?

**Matthew Panzarino:** Because we have a reference, the way that we build it out, we have a framework of things we like it to go look at.

**Matthew Panzarino:** Like, hey, here's a bunch of sources that are authoritative.

**Matthew Panzarino:** Here's what we want you to look at as a researcher, but we can't block, we can't list all the things we don't ever want it to do on the web.

**Matthew Panzarino:** It doesn't work that way, right?

**Matthew Panzarino:** It would be thousands of sites long.

**Matthew Panzarino:** But if there are ones that crop up that are outliers, we can add them to a block list.

**Matthew Panzarino:** But it's so much easier to see that, obviously, if there's a bibliography.

**Matthew Panzarino:** So let me look at a way to format that in a clean way with links.

**Matthew Panzarino:** So it'll be a plain text bibliography with links, obviously, so she can click if she chooses to.

**Matthew Panzarino:** But, like, right now, I can look up, like, the, this isn't the visual motion, this is a different one.

**Matthew Panzarino:** But we have a complete source bibliography for every article that we do.

**Matthew Panzarino:** And so, like, this one that I'm looking at is...

**Matthew Panzarino:** NCCIH, PubMed, another PubMed, NIH, JAMA, Nature Scientific, Frontiers, which are peer-reviewed journals, Science Direct, et cetera.

**Matthew Panzarino:** So like this listing of things would say, and after that step in the pipeline where it does that research, it no longer uses the web.

**Matthew Panzarino:** And we do this so that we can gate what information we're seeing.

**Matthew Panzarino:** And it's not suddenly like later on you say, oh, hey, could you copy edit this for me?

**Matthew Panzarino:** And it's like, cool, I'm going to go like pull a thing from the web.

**Matthew Panzarino:** And all of a sudden you've got this pollution in the article.

**Matthew Panzarino:** So it should be a pretty comprehensive list of any resource that was used.

**Matthew Panzarino:** It will be long in some cases.

**Matthew Panzarino:** So it's not like she has to check all of them.

**Matthew Panzarino:** It's just a resource for her to look at if she needs the sourcing of anything.

**Brian Magida:** Yeah, I think like I recall one example that I flagged to you all, which was it was research that was done.

**Brian Magida:** And...

**Brian Magida:** I'm women who experience HIV as like the example.

**Brian Magida:** And so I think that that's like the next step, which is ensuring there's almost like a governor in place, which says, okay, like at a high level, these are women as part of a study that we care about, but they're experiencing some disease state that doesn't actually apply to like what we're talking about.

**Brian Magida:** And so it should actually not use that as a source.

**Brian Magida:** Yeah.

**Matthew Panzarino:** Maybe that's like a separate conditional thing I have to give the fact checker.

**Matthew Panzarino:** I'll think about the logic on that.

**Matthew Panzarino:** We'll have to write some logic for it basically to say like, hey, if a disease is modifying the baseline, you know, health status of a woman and you are saying this only applies in these scenarios, let's not use that example.

**Matthew Panzarino:** Please look for another example from the baseline health status.

**Matthew Panzarino:** We'll see how that works.

**Matthew Panzarino:** I can't promise 100%.

**Matthew Panzarino:** That's tricky.

**Matthew Panzarino:** But we'll see how it works and we'll try and get as close as we can.

**Brian Magida:** Yeah. Cool.

**Brian Magida:** think we want to talk about some of the photography stuff and like just like images if possible.

**Brian Magida:** I think in the agenda you might have mentioned that there, I could have also misread this, that there's like some updates that you guys made.

**Matthew Panzarino:** don't know if there's anything to review right now.

**Matthew Panzarino:** Not yet, but hopefully tomorrow.

**Matthew Panzarino:** I hope tomorrow.

**Matthew Panzarino:** We should have a new batch of stuff for you to look at, a new batch of articles, and those articles will have the new imagery.

**Matthew Panzarino:** So take a look at it.

**Matthew Panzarino:** It'll be attached.

**Matthew Panzarino:** It'll be in context.

**Matthew Panzarino:** So you can see in the context it was generated.

**Matthew Panzarino:** And the two major updates, of course, is I took all of your feedback about what kinds of the photography we had created were most appealing.

**Matthew Panzarino:** And we're going to try and find those in our batches of generation per article to present to you.

**Matthew Panzarino:** And then the other was on the lead images, tire crops, less head shots, full face shots to make it less focused on who is this person and more focused on it is a person.

**Matthew Panzarino:** Those two things should be in effect for your next batch.

**Brian Magida:** Okay.

**Elizabeth Zwillinger:** And then just...

**Elizabeth Zwillinger:** What you just going send them to us?

**Elizabeth Zwillinger:** What format?

**Elizabeth Zwillinger:** Because I would like...

**Elizabeth Zwillinger:** This is actually something I want to share with somebody else on our team.

**Elizabeth Zwillinger:** So is it going to be a Google link again?

**Elizabeth Zwillinger:** And the images are going to be in...

**Elizabeth Zwillinger:** What format is it going to come in?

**Matthew Panzarino:** I think we upload them directly to Airtable now, but that's not absolutely necessary.

**Matthew Panzarino:** We can give them to you however you want, really.

**Elizabeth Zwillinger:** I don't want to interfere with your process.

**Elizabeth Zwillinger:** You've already been doing.

**Elizabeth Zwillinger:** if you're doing Airtable, then maybe, Brian, could download them and send them.

**Elizabeth Zwillinger:** I just want to get nervous eyes on them.

**Matthew Panzarino:** Yeah, or we can make it like here.

**Matthew Panzarino:** And like anything that we choose for publishing, we'll put in Airtable because it keeps our life organized for our publisher.

**Matthew Panzarino:** But then I can also just deliver them to you with the batch of articles.

**Matthew Panzarino:** Say, hey, here's the articles and here's a Google Drive with the images.

**Matthew Panzarino:** I don't know what you'd have to do.

**Elizabeth Zwillinger:** No, sorry.

**Elizabeth Zwillinger:** I wanted to see the whole thing in...

**Matthew Panzarino:** Like, see the article.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, that's on your site.

**Brian Magida:** You'd have to stage it. I think for this, when you deliver the Google Doc, if you could just have like a hyperlink to the image in Airtable, if that's possible, or just a hyperlink to the image stored on Google Drive, I think that would be sufficient.

**Brian Magida:** Liz, is that kind of what you're relating to?

**Brian Magida:** Yeah, I think that would just be sufficient for right now.

**Brian Magida:** And then we'll obviously see it like in situation when it goes to publishing.

**Brian Magida:** But yeah, it's for that one image, right?

**Elizabeth Zwillinger:** Per article.

**Elizabeth Zwillinger:** It's going to be the head, the main image, and then the images within the article, right?

**Matthew Panzarino:** Or no?

**Matthew Panzarino:** Yes, we're going to deliver you two images per article.

**Matthew Panzarino:** So one that's an interstitial image that can go anywhere you want.

**Matthew Panzarino:** And then the other one is there.

**Matthew Panzarino:** I personally do not want us to place the images in the articles. I think you should decide where you want them and put them in. That way they appear at the same place in every article. I don't want us to just throw them in from a formatting perspective, because they could flow differently on your site.

**Brian Magida:** So I would have a fixed place in which they appear.

**Brian Magida:** Yeah, that's totally fine.

**Brian Magida:** We're still, I was going to flag, like, there's still some kinks that we're working through just on, like, the tech side.

**Brian Magida:** Yeah, it just FYI, like, still working through getting Bradford in there.

**Brian Magida:** But, but yeah, to your point, like, we can, we can take the onus of placing that image and then certainly, like, work back with manufacturer or dev shop to say, like, hey, can we just, like, code in, like, spot within the template where an image could go or something, so.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** Normally, if you, so there's a couple of ways to do it, and obviously you'll let your dev team take the lead on what the right way to do it is.

**Matthew Panzarino:** But if you put an image block in, and then just basically say, hey, here's the block, we can call the block.

**Matthew Panzarino:** So, like, we can put the text to call the image in.

**Matthew Panzarino:** That way you don't have to worry about, okay, does it come before this H2 or after or whatever?

**Matthew Panzarino:** I'm to do that.

**Matthew Panzarino:** I just don't want like, paste the images into your CMS.

**Brian Magida:** That's like a recipe.

**Matthew Panzarino:** It just doesn't it's responsive.

**Brian Magida:** It never works right, you know, all of that.

**Brian Magida:** Okay.

**Brian Magida:** Is there a consumer-facing brand that you're already working with that's doing that that I can take a look at, like, how they use images in there?

**Matthew Panzarino:** We do so many SaaS products at the moment.

**Matthew Panzarino:** It's only a handful of – yeah, consumer-facing.

**Matthew Panzarino:** Let me think about it.

**Matthew Panzarino:** I'll let you know.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Well, it's just trying to think off – if I think off hand of anybody I think is doing a good job, too, I'll send that over.

**Elizabeth Zwillinger:** So I'm like, hey, this is cool.

**Elizabeth Zwillinger:** Whether it's our client or not, you know.

**Elizabeth Zwillinger:** Sure.

**Matthew Panzarino:** That'd be great.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Sounds good.

**Brian Magida:** Or he does a pretty good job with it, but it's, like, highly custom.

**Brian Magida:** So, like, every image is actually, like, designed.

**Brian Magida:** It's not going to work for us.

**Matthew Panzarino:** Yeah.

**Brian Magida:** All right.

**Brian Magida:** Switching gears, I think you mentioned you're still working through that additional content expansion opportunity that Marcel was mentioning.

**Brian Magida:** I just don't know if there's anything worth talking about.

**Brian Magida:** just want to get, again, we're starting to get to this point where, hey, we're feeling pretty good about the content that you're producing.

**Brian Magida:** We still need to work through some of the regulatory stuff.

**Brian Magida:** But, like, phase two, we want to be able to sort of look at what are some additional content opportunities that perhaps have more scale, less onus on us from a review perspective.

**Brian Magida:** We'd just love to talk about that, whether you're ready to talk about it today or next week.

**Matthew Panzarino:** Yeah, I'm close.

**Matthew Panzarino:** I'm just trying to, like, I'm trying to walk a line here between, like, I don't want to, you've got to think about the future.

**Matthew Panzarino:** You don't want to, like, cannibalize the keywords you're establishing with authority that drive towards a product.

**Matthew Panzarino:** So you want to, you've got to walk a parallel path.

**Matthew Panzarino:** And then you also, I'm trying to, I'm trying to just balance the need.

**Matthew Panzarino:** We need to like attack broadly interesting topics with, okay, but if we're going that deep, shouldn't we talk about the way that our product interacts with this?

**Matthew Panzarino:** So I'm just dancing on a little bit.

**Matthew Panzarino:** I've basically come up to three primary pillars, which is like symptom explainers, which we already do some of where it's like, hey, here's a thing and here's, it's related to this.

**Matthew Panzarino:** And I'm still trying to see if there's enough meat on the bone there that is different from, oh, you have this symptom.

**Matthew Panzarino:** So, hey, here's the ways you could tackle it.

**Matthew Panzarino:** And guess what?

**Matthew Panzarino:** Biologica does a great job at that.

**Matthew Panzarino:** We don't want it to be that.

**Matthew Panzarino:** We're already doing that, right?

**Matthew Panzarino:** Then there's also like ingredient education, which we're already doing some of.

**Matthew Panzarino:** I'm just trying to find like a patch to land on that is really broadly applicable, that does not run it over because you don't want to cannibalize your own keyword work that you're doing there.

**Matthew Panzarino:** And you're already serving some of those needs, but I'm close. I'll get you something probably tomorrow. Rather than going down the rabbit hole, let me provide you with a few options and you can give me some succinct brief input of like, yeah, further down this path or not.

**Brian Magida:** I think that's the best case.

**Matthew Panzarino:** And I'm kind of walking myself in circles a little bit on this, just being honest, because I think it's, I'm trying, I'm walking down this path and I'm like, hey, if we're doing like symptom explainers, like, you know, why is my period suddenly irregular?

**Matthew Panzarino:** What's the difference between anxiety and hormonal anxiety?

**Matthew Panzarino:** Or, you know, what's happening to my brain during menopause?

**Matthew Panzarino:** I'm like, man, I feel like we've walked these paths a lot.

**Matthew Panzarino:** And like finding new ways to ask those questions and walk those paths is interesting.

**Matthew Panzarino:** And then if you go too far afield, it's like, okay, now we're talking about hobbies and really tangential topics.

**Matthew Panzarino:** So I just don't want to do the wrong thing here as we're establishing your brain presence and your web presence.

**Matthew Panzarino:** We're going to set a good foundation.

**Matthew Panzarino:** So I'm trying to do the right thing and make sure that you have the right strategy and one that has legs.

**Matthew Panzarino:** We want to publish, like, dozens and dozens of pieces in this world, not just a handful of establishing pieces.

**Matthew Panzarino:** So I want to find something that has enough depth there.

**Brian Magida:** Yeah, would love to be able to, whether it's Friday or even, like, next week is fine.

**Brian Magida:** Just I want to make sure we're keeping kind of some momentum going in that direction.

**Matthew Panzarino:** Yeah, let's chop it up.

**Matthew Panzarino:** I think I need to walk myself out of this morass with a little bit more feedback from you, but I'll give you some concrete stuff that I've worked on, and then you can tell me whether or not we're sniffing up the right tree, and then we'll get it done.

**Matthew Panzarino:** Once we've kind of established the strategy overall, or the broad strategy, doing the keyword research and starting to produce the articles is, like, a week and a half, you know?

**Matthew Panzarino:** Like, so we'll be able to move on it pretty quick.

**Brian Magida:** Okay.

**Brian Magida:** Was there anything else that we needed to talk through right now?

**Matthew Panzarino:** Oh, clinical framework that you gave me, the next batch of articles, that you will...

**Matthew Panzarino:** We'll have that stuff apply, as well as the link improvements or fixes, so to speak.

**Matthew Panzarino:** So you'll see that reflected or should see it reflected.

**Matthew Panzarino:** So include that in your feedback, like, hey, we gave them this rubric.

**Matthew Panzarino:** Make sure that we're kind of in the ballpark on that.

**Matthew Panzarino:** I understand that's like a regulatory thing, a lot of it.

**Matthew Panzarino:** So we're trying to make sure that it's paying attention to it.

**Matthew Panzarino:** The good news, as I mentioned before, it's not radically different from the examples that I've walked through.

**Matthew Panzarino:** I need to finish editing these pieces to get them over to you this week.

**Matthew Panzarino:** But we've got a new batch coming your way that should have that already applied.

**Brian Magida:** Okay.

**Brian Magida:** And then I guess this is like cart before the horse a little bit, but you'll send over with this next batch the updated images.

**Brian Magida:** Let's just assume the images are great.

**Brian Magida:** They're approved.

**Brian Magida:** Will you then be able to just go through and update the publishing of the existing articles that are already published with the updated images?

**Brian Magida:** Is that kind of like the next step there?

**Matthew Panzarino:** Yeah, we can. If we want to generate new images for those to make them all adherent or get the interstitial images for the previous ones, we'll just go through and do a batch of those, and then the publisher will do them all in one batch probably next week.

**Brian Magida:** Yeah, we'll have to do that.

**Brian Magida:** Just at the very bare minimum, there's images that have text overlays that, like, shouldn't have text overlays.

**Matthew Panzarino:** Absolutely.

**Matthew Panzarino:** But, yeah, we'll get the approval so that you are happy with what we're delivering, and then we'll generate them.

**Matthew Panzarino:** I'm trying to think.

**Matthew Panzarino:** Maybe, Brian, best case is we generate them, and then send you the folder, and you can just go through and make sure you're cool with all of them.

**Matthew Panzarino:** Then we will put them on the articles.

**Brian Magida:** Yeah, that works.

**Brian Magida:** And then we haven't talked about this, but I like the new, like, topic clustering that you put together.

**Brian Magida:** And so as a result, we have these tags that we use within the CMS.

**Brian Magida:** We should talk about how to migrate the topic cluster convention that you have within Airtable to consumer-facing tags. We can handle this over Slack.

**Brian Magida:** It's probably honestly as simple as reproductive years, perimenopause, postmenopause, or something like that.

**Brian Magida:** But in your publishing process, being able to apply the correct tag or series of tags to the article, that way I don't have to do it after the fact.

**Brian Magida:** But we can talk about that through Slack.

**Matthew Panzarino:** Yeah, it's actually pretty straightforward.

**Matthew Panzarino:** We do this with almost every client.

**Matthew Panzarino:** We just haven't really set up your workspace for it because we've been pre-launched, right?

**Matthew Panzarino:** But the vast majority of folks will get a generated breadcrumb with the appropriate metadata in it.

**Matthew Panzarino:** So you'll have, like, the proper keywords.

**Matthew Panzarino:** And then the keyword cluster that is going out.

**Matthew Panzarino:** After, like, key, various keywords, and we can map those, so we'll make sure that they are, they are mapped to the same ones as in the Airtable, and we'll just put them in Airtable fields, so our publisher will be able to see them, and then he'll be able to use them and assign them to the proper tags, it's probably the easiest way to go about it, and then long term, if we ended up using, like, the Shopify API, let's say we end up generating, like, a dozen pieces or more, and you're like, you know, hey, these are really great, we reviewed these, and, like, cool, we can then ship them to the Shopify API, to publish them, stage them, and you can release them, whatever your preference, when you do that, it'll pull from those fields, and tag them automatically, so, it should work well.

**Brian Magida:** Okay.

**Brian Magida:** Liz, was there anything else that you wanted to talk about?

**Elizabeth Zwillinger:** No.

**Brian Magida:** Cool.

**Brian Magida:** Liz, do you want to, I just want to chat a couple quick things with you, so I'll just shoot you a Google Meet link, we can jump on that.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Thanks.

**Matthew Panzarino:** Thanks.
