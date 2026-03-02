# CMS Sync - GrowthX Publishing for Elementum

<metadata>
date: 2026-01-27
time: 17:31 UTC
duration: 19 minutes
organizer: tyler@growthx.ai
participants:
  - name: Kirkland Gee
    email: kirkland@growthx.ai
    company: GrowthX
    role: Forward Deployed Engineer
  - name: Andrew Bennett
    email: abennett@elementum.com
    company: Elementum
    role: Head of Growth
  - name: Porter Hoskins
    email: phoskins@elementum.com
    company: Elementum
    role: Platform Engineer
  - name: Tyler Pavlas
    email: tyler@growthx.ai
    company: GrowthX
    role: Account Lead / VP of Growth
fathom_recording_id: 117506780
fathom_url: https://fathom.video/calls/545575123
share_url: https://fathom.video/share/se6Mw9Gzg1weRzK5_cMYZnfqFEy1tV9X
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

GrowthX and Elementum aligned on a publishing workflow using Keystatic, a lightweight CMS that creates commits to Elementum's existing Markdown-based GitHub repo, enabling direct content publishing. The team finalized contract terms including a gross non-performance termination clause, written permission for logo use, and quarterly payments, with contract signing expected by Jan 28 and project kickoff scheduled for Feb 9.

---

## Context

Elementum currently lacks a traditional CMS, managing content through Markdown files stored in a GitHub repository with automated CI/CD deployment. GrowthX, engaged to create high-intent SEO content (educational pieces, comparisons, alternatives) aimed at driving AI answer ranking, needed a frictionless way to publish directly without manual handoffs. Rather than implement a heavyweight CMS like Sanity or Strapi, the team selected Keystatic—a lightweight tool that layers a browser-based UI on top of Markdown files, allowing GrowthX team members to edit content while triggering automatic commits to the repo.

The engagement spans three to six months initially, with potential expansion to `/guides` sections, use case pages, and custom components (CTAs, tables, table of contents). This is part of a larger $216k GrowthX Growth Execution engagement focused on content-led demand generation for Elementum's platform.

---

## Relevance

**For GrowthX**
- Demonstrates how to solve publishing friction in non-traditional tech stacks (Markdown-based, no CMS)
- Keystatic as a repeatable pattern for future clients using GitHub-first workflows
- Validates strategy of publishing high-intent educational and comparative content for B2B SaaS

**For Elementum**
- Enables content velocity without hiring additional FTE
- Keystatic preserves existing tech stack and GitHub workflow
- Quarterly payments align with phased content strategy (3-6 month initial phase)

**For Contract & Operations**
- Gross non-performance termination clause protects both parties given absence of fixed deliverables
- Written logo permission requirement adds brand control
- Quarterly payments create natural checkpoint intervals for strategy review and refresh

---

## Overview

- **CMS Solved:** Elementum will implement Keystatic, a lightweight CMS that provides a UI on top of their existing Markdown files, enabling GrowthX to publish directly.
- **Contract Finalized:** The contract is approved pending three revisions: adding a "gross non-performance" termination clause, requiring written permission for logo use, and setting quarterly payments.
- **Kickoff Scheduled:** The project kicks off Feb 9 with a strategy session (Andrew, Nader) and a separate product deep dive (Kyle Westwood).

---

## Key Topics

### Content Publishing Workflow

  - **Problem:** Elementum lacks a traditional CMS, using only Markdown files in a GitHub repo, which prevents direct publishing by GrowthX.
  - **Solution:** Elementum will implement **Keystatic**.
      - **Why:** It provides a browser-based UI for editing Markdown files directly in the repo, preserving the current tech stack.
      - **Mechanism:** Edits in Keystatic create commits in the GitHub repo, triggering the existing CI/CD pipeline.
  - **Content Scope:**
      - **Initial 3–6 months:** Focus on blog posts for SEO (educational, comparisons, alternatives).
      - **Future:** Potential for `/guides` sections, use case pages, and custom components (CTAs, tables, TOCs).
      - **Goal:** Drive high-intent traffic and improve AI answer ranking.

### Contract & Logistics

  - **Contract Revisions:**
      - **Termination:** Add a clause for "gross non-performance" (e.g., inability to deliver services).
          - **Why:** The "termination for breach" clause is insufficient, as defining "breach" for an ongoing service is ambiguous.
      - **Logo Use:** Require explicit written permission.
      - **Payments:** Set to quarterly.
  - **Signers & Contacts:**
      - **Signer:** David Blonski (CFO) → `david@elementum.com`
      - **Billing:** Levi Brown → `l.brown@elementum.com`
  - **Kickoff Meeting (Feb 9):**
      - **Strategy Session:** Andrew Bennett (Elementum), Nader (Elementum CEO)
      - **Product Deep Dive:** Kyle Westwood (Elementum, best person for product demo)

---

## Action Items

**Porter Hoskins (Elementum)**
- Host Keystatic on Elementum route; configure GitHub repo; add publish automation; share access with Kirkland Gee

**Tyler Pavlas (GrowthX)**
- Update contract with termination for cause/inability to deliver; add written name/logo permission; set quarterly payments; send to Andrew
- Schedule Feb 9 kickoff with Andrew Bennett and Nader (CEO); schedule product deep dive with Kyle Westwood
- Send Andrew dinner details with confirmed attendees; Andrew to confirm attendance

**Andrew Bennett (Elementum)**
- Send Tyler CFO signer (David Blonski) and billing contact (Levi Brown)

---

## Transcript

**Tyler Pavlas:** We worked together or something.

**Andrew Bennett:** I know, exactly, exactly.

**Kirkland Gee:** This meeting is being recorded.

**Kirkland Gee:** How are you?

**Andrew Bennett:** Good, good.

**Andrew Bennett:** I'm sitting, I don't know, probably eight miles as the crow flies from Kirkland, Washington.

**Kirkland Gee:** Oh, no way.

**Andrew Bennett:** Okay.

**Kirkland Gee:** I am quite far away.

**Andrew Bennett:** I actually live in Virginia.

**Andrew Bennett:** Okay, nice.

**Kirkland Gee:** Way on the other side.

**Andrew Bennett:** Sitting under a pile of snow.

**Kirkland Gee:** Yes.

**Kirkland Gee:** It's almost up, my office is in our basement, and the snow is almost up to like the window on our house.

**Andrew Bennett:** Right, right on.

**Andrew Bennett:** Awesome.

**Andrew Bennett:** Awesome.

**Andrew Bennett:** Hey, Porter, thanks for joining on short notice.

**Porter Hoskins:** Hey, no problem.

**Andrew Bennett:** So, yeah, just super, I think this will probably be a really quick conversation.

**Andrew Bennett:** This is kind of me not quite having full understanding of our web stack.

**Andrew Bennett:** So, we're planning on going forth together on a relationship to have GrowthX create content for us at scale. They kind of said, hey, yeah, just give us a login to your CMS and we'll post stuff.

**Andrew Bennett:** And I know we don't have a CMS.

**Andrew Bennett:** I know that GrowthX's platform is super modern and sophisticated.

**Andrew Bennett:** Porter understands really well the architecture of website.

**Andrew Bennett:** So I just wanted to get you two together and just confirm that, yes, we understand how GrowthX will post content to our site without us needing any manual step on our end.

**Tyler Pavlas:** Perfect.

**Tyler Pavlas:** We got, you know, Forward Deployed Engineer from GrowthX with Forward Deployed Engineer from Elementum.

**Tyler Pavlas:** So this should be the right conversation.

**Tyler Pavlas:** And Andrew and I will just sit in the peanut gallery.

**Andrew Bennett:** Exactly.

**Kirkland Gee:** Yeah, Porter, I think this is super simple.

**Kirkland Gee:** I just kind of like, if you guys don't have a CMS, how are blogs getting on the website today?

**Kirkland Gee:** Are they just like in the repo somewhere or is there some sort of lightweight markdown something handling that?

**Porter Hoskins:** Like, how are you guys doing that today?

**Porter Hoskins:** Yeah, so we just have lightweight markdown files in the repo, but like, we can pull from a bucket, like, we can change it, whatever we need to do.

**Kirkland Gee:** Yeah, there's like, I mean, there's, you know, Tyler was asking me, there's kind of infinite ways we could do this, like, you guys could give us access and we could just like upload files to the repo if we need to do it that way.

**Kirkland Gee:** We could set up some sort of, like, I don't know, Keystatic is one of them, but there's like a dozen CMSs that essentially just look at markdown files in a GitHub repo, but give an editor like a UI to work with.

**Kirkland Gee:** But more automated is better for us.

**Kirkland Gee:** And then there's like more complex things like Sanity or Strapi or stuff like that, but we don't necessarily have to go that route.

**Kirkland Gee:** It doesn't help us, per se.

**Porter Hoskins:** Yeah, what's easiest for you guys?

**Kirkland Gee:** You know, probably something like Keystatic, if you're familiar with it.

**Kirkland Gee:** Or any alternative, it's just that one, it literally just sits on top of existing markdown files.

**Kirkland Gee:** It just like gives you the way to like, hey, there's this markdown file in the repo, and then there's some Tiptap UI that somebody else can work with in the browser, and then we can set up automations to like publish that way.

**Kirkland Gee:** I think this is probably the simplest thing to do, if that's how you're already doing it today, is you just have to set it up.

**Kirkland Gee:** But if you find an alternative solution you're happy with, we're good with that, too.

**Porter Hoskins:** So I host Keystatic, and put it on a route, and then it'll let you just...

**Porter Hoskins:** Basically, yeah.

**Porter Hoskins:** Lets you like submit for requests?

**Kirkland Gee:** Yeah, it makes commits when you make edits.

**Kirkland Gee:** So you edit an article, and it just sends a commit to the repo.

**Kirkland Gee:** Directly affecting that markdown file, but it's still all tracked through GitHub.

**Kirkland Gee:** Sweet.

**Kirkland Gee:** So it's, we've used it with a couple of clients.

**Porter Hoskins:** It seems ridiculously easy.

**Porter Hoskins:** Yeah, you literally, it's really nice.

**Porter Hoskins:** Okay, yeah, let's just do it.

**Kirkland Gee:** Cool.

**Kirkland Gee:** Yeah, we just set up something like this, and then we can, the only thing I don't know, because I don't remember if we've done this, is like fully automating publishing through Keystatic.

**Kirkland Gee:** I can't imagine it's that hard.

**Kirkland Gee:** Like, there's probably some endpoint we can hit with a workflow, but we can figure that piece out.

**Kirkland Gee:** Okay.

**Kirkland Gee:** So, I think this will work great for us.

**Porter Hoskins:** Great.

**Porter Hoskins:** Let's do it.

**Tyler Pavlas:** Andrew, are y'all thinking at all about the timeline for when you might implement a CMS?

**Andrew Bennett:** Honestly, we have bigger fish to fry with.

**Andrew Bennett:** We're trying right now.

**Andrew Bennett:** Now.

**Andrew Bennett:** We.

**Andrew Bennett:** No, I mean, I think that we're going to wind up doing a fairly short-term revision to some of the messaging that's on the site right now.

**Andrew Bennett:** We're more focused on assets for the field than we are on doing a big revision.

**Andrew Bennett:** And I mean, I don't even have a higher, I don't even have an FTE open right now for content beyond, you know, beyond the work that you guys are doing.

**Andrew Bennett:** So, I'm sure we'll get to it in a few quarters, but it's not on the short list right now.

**Tyler Pavlas:** Kirkland, any downsides to like our content performance when it comes to not publishing through CMS?

**Kirkland Gee:** Not at all.

**Kirkland Gee:** CMS has no bearing on performance.

**Kirkland Gee:** It's just like, something like Keystatic, like there are some downsides, right?

**Kirkland Gee:** Like it's, you're stuck with just markdown files.

**Kirkland Gee:** It's harder to do like custom components and those kinds of things at scale, but like there are ways to work around that, too.

**Kirkland Gee:** And I think, no, I don't think there's any hindrance to not having like a bigger, heavier weight CMS.

**Kirkland Gee:** I think this would work fine.

**Tyler Pavlas:** Okay.

**Tyler Pavlas:** Any questions, Andrew or Porter, that we can help answer?

**Porter Hoskins:** Porter, are you good?

**Porter Hoskins:** Yeah, just so you guys know, I like support the release notes, the blogs, and then like I did like a landing pages markdown and like actually have like components that you can drop in there.

**Porter Hoskins:** Nice.

**Porter Hoskins:** Through the markdown.

**Porter Hoskins:** So what other stuff do you guys want to do?

**Kirkland Gee:** I don't know in this particular case, but there are times where like CTAs are a very common example of like having some various CTAs with different images, different texts that are maybe like predefined that we can plop into different articles, things like.

**Tyler Pavlas:** I've heard, I've heard a couple of them because I've asked Ada about this before.

**Tyler Pavlas:** And it's like being able to publish a table in the content is helpful.

**Tyler Pavlas:** Being able to have like a table of contents where someone could navigate to different sections.

**Tyler Pavlas:** Those are really the only.

**Tyler Pavlas:** Yeah.

**Kirkland Gee:** And that's all doable in Markdown just fine.

**Kirkland Gee:** As long as it's like properly supported.

**Kirkland Gee:** There are some cases like Sanity is a funny example.

**Kirkland Gee:** It's a bigger CMS, but it does not like Markdown tables most of the time, unless you add some like special handling for it.

**Kirkland Gee:** I actually think Keystatic would handle that better, weirdly enough.

**Tyler Pavlas:** And if the table is too much trouble, like a member of our team has said, we can use Claude to convert a table into an HTML code block and then insert it.

**Tyler Pavlas:** If that, I mean, I'm not technical, but.

**Tyler Pavlas:** We can render tables easy peasy.

**Tyler Pavlas:** Oh, okay.

**Porter Hoskins:** I agree with that premise.

**Porter Hoskins:** I promise.

**Porter Hoskins:** But just in general, what kind of content are we doing?

**Porter Hoskins:** Just blog posts or landing pages?

**Porter Hoskins:** Or what's the plan?

**Porter Hoskins:** Am I covering everything we need?

**Porter Hoskins:** Or do I need to add something?

**Tyler Pavlas:** Yeah, I can answer the question for you.

**Tyler Pavlas:** So here's a good look at the typical content types that we focus on.

**Tyler Pavlas:** Sorry, I'm just grabbing a slide that really makes it clear.

**Tyler Pavlas:** We typically do publish to the blog.

**Tyler Pavlas:** Sometimes we will, you know, set up like a slash guides if that's better for scale and can have that in the footer as opposed to like in the top menu navigation.

**Tyler Pavlas:** We did that with Augment Code, for example.

**Tyler Pavlas:** You can see that they've got like this guide section, but it's not in their main menu.

**Porter Hoskins:** It's in the footer.

**Tyler Pavlas:** And that's where we've published hundreds of pieces of content.

**Tyler Pavlas:** And that's it's best if the content types are helpful.

**Tyler Pavlas:** Educational content, alternatives, comparisons, so more bottom of funnel.

**Tyler Pavlas:** We could even think about use case pages, which Andrew and I were talking about, but that typically comes later after we've done more of the SEO content.

**Tyler Pavlas:** And we've even created this vendor directory for Ramp that is a custom section of their site.

**Tyler Pavlas:** We use some forward deployed design engineers to actually build this.

**Tyler Pavlas:** And then we've even created like this templates library for Lovable.

**Tyler Pavlas:** So I guess, you know, quick answer to your question, for the first three to six months of the engagement, we would pretty much just be publishing to the blog.

**Tyler Pavlas:** Unless you wanted us to set up a slash guides.

**Andrew Bennett:** Yeah, so Porter.

**Andrew Bennett:** Yeah, sorry, Porter.

**Andrew Bennett:** I gave you very little context on this.

**Andrew Bennett:** Because this is all, it's really about content consumption and ranking.

**Andrew Bennett:** Ranking, not just SEO, but you know, AEO, GEO, ranking, and not about you know performance marketing form fills, you know, kind of world.

**Andrew Bennett:** It's just getting a good stream of high quality content out into the world about who we are and what we do and how we're different in different use cases.

**Porter Hoskins:** Awesome.

**Porter Hoskins:** Yeah.

**Porter Hoskins:** Cool.

**Tyler Pavlas:** Getting in the AI answers, driving higher intent traffic.

**Tyler Pavlas:** That's the goal.

**Kirkland Gee:** And just one thing that is relevant is like our team is also available to help with dev stuff.

**Kirkland Gee:** Like if we need something that you guys don't have the time or the bandwidth, like we have a pretty small dev team, but we're all over the place helping with stuff.

**Kirkland Gee:** So if it's like, hey, we want to do a landing page and we have some very specific requirements, like our team can help sketch that out and figure those things.

**Andrew Bennett:** Cool.

**Porter Hoskins:** Sounds good.

**Porter Hoskins:** Porter, Kirkland, I think we're set.

**Tyler Pavlas:** And Andrew...

**Tyler Pavlas:** And Andrew...

**Tyler Pavlas:** And.

**Tyler Pavlas:** If you have two minutes to just make sure we're aligned on contract and signature, we'll be good to go.

**Kirkland Gee:** Awesome.

**Kirkland Gee:** Awesome.

**Andrew Bennett:** Thanks, guys.

**Andrew Bennett:** Great to meet you. Appreciate it.

**Kirkland Gee:** Bye.

**Tyler Pavlas:** I need an easy button.

**Tyler Pavlas:** That was nice.

**Andrew Bennett:** I know.

**Andrew Bennett:** I figured that would be the case.

**Andrew Bennett:** But, again, if we were talking old school CMS, I would have been very capable of handling that on my own.

**Andrew Bennett:** But this world, I don't know very well.

**Tyler Pavlas:** Yeah, it's interesting.

**Tyler Pavlas:** Like, not even needing a CMS is a weird concept for me to wrap my head around.

**Andrew Bennett:** But more research to do.

**Andrew Bennett:** Yeah, exactly.

**Andrew Bennett:** So I'm getting another round on termination.

**Andrew Bennett:** Of course, termination for convenience, I know, is off the table.

**Andrew Bennett:** Do you have language that you've used that just protects against just like sort of termination for cause or just like gross non-performance, you guys go out of business, you're unable to provide content at all.

**Andrew Bennett:** So, I mean, I'm not talking like editorial review isn't going well, but just literally like complete inability to deliver the services.

**Tyler Pavlas:** I'm sure that would be easy for us to add.

**Tyler Pavlas:** I'll reach out to VP of Ops and our counsel to see what they recommend.

**Tyler Pavlas:** Okay.

**Tyler Pavlas:** Did you see that we have termination for breach in here?

**Tyler Pavlas:** I didn't know if that covered what you were talking about, but I think I can probably add language if it's not.

**Tyler Pavlas:** Not sufficient to mention, you know, if we go out of business, if we are completely unable to deliver the services, I can definitely get more language added if that would help.

**Andrew Bennett:** I think it probably would.

**Andrew Bennett:** And it's just because since there aren't fixed deliverables, my guess would be that defining breach would be a little fuzzy.

**Tyler Pavlas:** Totally understand, yeah.

**Andrew Bennett:** Right.

**Andrew Bennett:** And so just getting more explicit around, yeah, inability to deliver the services, whatever the better words are for that.

**Tyler Pavlas:** Okay, definitely, definitely.

**Tyler Pavlas:** Let me get that added.

**Tyler Pavlas:** Everything else, does everything else look okay?

**Andrew Bennett:** Yeah, I think we're fine.

**Andrew Bennett:** Yeah, we're fine on the numbers.

**Andrew Bennett:** Let's, does everything else.

**Andrew Bennett:** Let's just give things to the.

**Andrew Bennett:** You were going to add permission on the name and logo, right?

**Tyler Pavlas:** Written permission.

**Andrew Bennett:** Yes, sir.

**Andrew Bennett:** Yeah.

**Tyler Pavlas:** Yeah.

**Tyler Pavlas:** Add written permission here.

**Tyler Pavlas:** Update our termination clause to be a bit more clear and connect it to deliverables to any extent that I can.

**Andrew Bennett:** And then quarterly payments.

**Tyler Pavlas:** And then quarterly payments.

**Tyler Pavlas:** Yep.

**Tyler Pavlas:** Yep.

**Tyler Pavlas:** Yep.

**Tyler Pavlas:** Okay, cool.

**Tyler Pavlas:** Everything else look good?

**Andrew Bennett:** Yeah.

**Tyler Pavlas:** Okay, perfect.

**Tyler Pavlas:** If I can get this turned around today or tomorrow, are you pretty much able to sign that same day?

**Andrew Bennett:** Yeah, so I will send you, our CFO will sign, I'll send you the signer and the billing contact.

**Andrew Bennett:** Um.

**Andrew Bennett:** Um.

**Andrew Bennett:** Um.

**Andrew Bennett:** And, yeah, David Blonski, the CFO, will be the actual signer.

**Tyler Pavlas:** Is it just David at Elementum.ai?

**Andrew Bennett:** It is.

**Andrew Bennett:** So it's Blonski, B-L-O-N-S-K-I.

**Andrew Bennett:** And, yes, and he is David at Elementum.com.

**Andrew Bennett:** And then the billing contact is Levi Brown, L-E-V-I Brown.

**Andrew Bennett:** And he's L Brown at Elementum.com.

**Tyler Pavlas:** Perfect.

**Tyler Pavlas:** Awesome.

**Tyler Pavlas:** I think we'll have this wrapped up probably by end of day tomorrow.

**Tyler Pavlas:** And we'll lock in the ninth as the kickoff.

**Tyler Pavlas:** And you will be the only one on the kickoff.

**Tyler Pavlas:** Or will there be anybody else that will add to that meeting?

**Andrew Bennett:** And so in that kickoff, are we primarily talking like scheduling and roles for the first phase?

**Tyler Pavlas:** Overview of the strategy sprint and then pretty deep dive into your ICP and, you know, why now, what you feel like your competitors are doing well.

**Tyler Pavlas:** It's basically like the meeting where our team captures as much nuance as possible, and we typically do a product deep dive after that.

**Tyler Pavlas:** So if you wanted that first conversation to just be with you and then the product deep dive with like the best person on the team to give us a demo with the platform, that could be a good way to structure it, to use their time effectively.

**Andrew Bennett:** Probably, yeah, okay, I think we should probably invite Nader, our CEO, to the kickoff.

**Tyler Pavlas:** Nice, I like that idea, yeah.

**Tyler Pavlas:** And then product deep dive, like, person who's the best to give us a demo, who is that?

**Andrew Bennett:** Kyle, Kyle Westwood.

**Tyler Pavlas:** Thanks for you.

**Tyler Pavlas:** Yo.

**Tyler Pavlas:** Okay.

**Tyler Pavlas:** Yeah, I think you and Nader for the kickoff, and then Kyle Westwood for the product deep dive should be perfect.

**Tyler Pavlas:** And just, I think that, apparently we may have mentioned this to you, but we do have a dinner next Wednesday evening, and I know you're in Seattle, so no pressure.

**Tyler Pavlas:** And we also do a lot of dinners, so I can give you a better lead time on the next one.

**Tyler Pavlas:** Um, but any chance, once I get like a better list of the attendees, that you'd be interested?

**Andrew Bennett:** I mean, I would like to, yes, I'm interested in, and I mean, it would be great timing just to, you know.

**Tyler Pavlas:** Right before the kickoff, yeah.

**Andrew Bennett:** Yeah, you know, get some, get some best practices from you know from folks who have been working with you guys.

**Andrew Bennett:** Um, I'm not positive that I can go, I haven't checked flights yet, but I mean, if I can, if I can just go, go down and back for the afternoon, and I might, I might try to pull that off.

**Tyler Pavlas:** Okay, awesome.

**Tyler Pavlas:** I'll shoot you a link with the details and, um.

**Tyler Pavlas:** When I get some clarity on like who's all going, I'll also send that to you so you can kind of just decide if it's worth your while.

**Tyler Pavlas:** But I'm almost positive that Marcel will be there and that our VP of growth will be there.

**Tyler Pavlas:** So I'll confirm those details.

**Tyler Pavlas:** But yeah, think we're feeling good and got everything I need to lock things in with you.

**Andrew Bennett:** Okay.

**Andrew Bennett:** Awesome.

**Andrew Bennett:** Sounds great, Tyler.

**Tyler Pavlas:** Appreciate it.

**Tyler Pavlas:** All right.

**Andrew Bennett:** Thanks, Andrew.

**Andrew Bennett:** Thank you.
