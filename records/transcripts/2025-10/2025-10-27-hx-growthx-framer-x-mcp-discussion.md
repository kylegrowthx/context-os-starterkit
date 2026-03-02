# hx <> GrowthX | Framer x MCP Discussion

<metadata>
date: 2025-10-27
time: 17:00 UTC
duration: 20 minutes
organizer: Erik O'Brien
participants: Kirkland Gee, Mark Boyes-Smith, Bailey Seybolt, Erik O'Brien
fathom_recording_id: 97027445
fathom_url: https://fathom.video/calls/452952368
share_url: https://fathom.video/share/qh3ZkMtAeexyer-Rhxbr7h_XG_gqN6mD
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and HX aligned on automating article publishing from Storyblock to Framer using the MCP (My Content Plugin), with GrowthX owning the final CMS schema design and HX providing backend support. The team confirmed that Framer's decommissioned API requires the MCP approach, which mandates a manual review step before publishing due to the plugin's requirement for an active logged-in user. HX will grant Framer access with plugin-config role to enable GrowthX to build the integration, and will provide visual examples and geometric/gradient design guidance to shift AI-generated article images from generic stock-photo styling toward abstract, brand-aligned artwork.

---

## Context

HX (Hyperexponential) is a client in the financial services/AI space launching a major rebrand within the next month. They're rebuilding their marketing website on Framer and producing AI-generated articles as a core piece of their go-to-market strategy, working closely with GrowthX on content generation and publication automation. Mark Boyes-Smith, HX's design lead for both product and brand, is overseeing the website redesign and visual strategy. This meeting brought together HX's technical and design leadership with GrowthX's engineering team (Kirkland Gee) to solve the publishing workflow and establish design direction for article imagery.

---

## Relevance

**To GrowthX Delivery:**
- GrowthX owns the CMS schema design for Framer publishing — this is a key deliverable that determines how articles flow from Storyblock through the pipeline. Schema design should prioritize simplicity for reliable MCP execution.
- The manual review step before publishing (required by MCP architecture) is now a permanent part of the workflow. GrowthX should plan for a human-in-the-loop publishing process with clear delegation.
- Kirkland Gee's Framer access will need plugin-config role permissions to build and test the MCP integration — HX will provide this through Frankie Chaffin-Edwards.

**To CheckThat:**
- HX's AI-generated article strategy directly reflects demand for strong content generation capabilities. GrowthX's success here demonstrates real client value around tuning AI engines for GTM content, which is a CheckThat conversation.
- David (AI/content lead on HX side) is guiding the content strategy and will provide design references for imagery — establishing clear feedback loops with client AI stakeholders strengthens the engagement.

**To GrowthX Business Development:**
- HX's rebrand and 1-month launch timeline indicate high velocity and trust in the GrowthX partnership. This is an account health signal showing strong alignment and scope expansion (publishing automation + design support).
- Mark Boyes-Smith's emphasis on brand ownability and avoiding generic "iStockphoto AI" positioning suggests HX sees GrowthX as a strategic partner, not just a vendor. Reference potential for brand-aligned content services.
- The engagement spans product engineering (Kirkland), content strategy (Bailey), and external partner coordination (Erik) — strong internal support and cross-functional delivery.

---

## Overview

- **Framer Publishing:** The workflow will use Framer's MCP (My Content Plugin) to publish AI-generated articles via the CMS. This method is required because Framer's API is decommissioned.
- **MCP Constraint:** The MCP requires a user to be logged into Framer with the plugin open, which necessitates a manual review step before publishing.
- **AI Image Strategy:** The current AI-generated images are too generic. The new direction is abstract, geometric art using HX's brand gradients to create a unique, ownable visual style.
- **Next Steps:** HX will grant GrowthX Framer access to build the MCP schema. HX will also provide visual examples to guide the new AI image generation.

---

## Key Topics

### Framer Publishing Workflow

  - **Goal:** Automate publishing of AI-generated articles from Storyblock to Framer.
  - **Constraint:** Framer's API is decommissioned, requiring the use of the MCP (My Content Plugin).
  - **Solution:** Publish via Framer's CMS, not by filling content blocks in a template.
      - **Rationale:** This method proved more reliable in testing, avoiding issues like incorrect content placement.
      - **Process:** Use the MCP to populate a simple CMS metadata schema.
  - **MCP Constraint:** The plugin requires a user to be logged into Framer with the MCP receiver open.
      - **Impact:** This necessitates a manual review step in the workflow before publishing.
  - **Schema Ownership:** GrowthX will design the final CMS schema.
      - **Rationale:** HX has no strong preferences and trusts GrowthX to build the most functional schema for the content pipeline.

### AI Image Generation Strategy

  - **Problem:** Current AI-generated images are too generic and don't align with the new HX brand.
  - **New Direction:** Create abstract, geometric art that evokes the brand without directly illustrating article content.
      - **Rationale:** This approach is more suitable for abstract topics and avoids a generic "AI iStockphoto" feel, ensuring brand ownability.
  - **Creative Elements:**
      - Geometric shapes and mathematical concepts
      - Rich brand gradients
      - Layering
  - **AI Limitations & Workarounds:**
      - **Color Inconsistency:** AI struggles with exact hex codes.
          - **Workaround:** Use black & white illustrations or design a set of brand-compliant backgrounds for AI to generate on top of.
      - **Complexity:** Highly complex scenes require significant refinement.
          - **Decision:** Start with a simpler style to get to market quickly.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Email Frankie GrowthX pod email for Framer access; request plugin-config role

**Mark Boyes-Smith (HX)**
- Email Bailey/Erik AI image refs (gradients/geometric); cc Frankie

---

## Transcript
**Erik O'Brien:** Hey, Bailey.

**Bailey Seybolt:** Hey, everyone.

**Bailey Seybolt:** How's it going?

**Erik O'Brien:** Good, good.

**Erik O'Brien:** Kirkland, have you met Bailey yet?

**Kirkland Gee:** I don't.

**Kirkland Gee:** I think we've talked in Slack.

**Bailey Seybolt:** Yeah, I've got a thing.

**Bailey Seybolt:** Or maybe notion comments in the margins.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Nice to meet you properly.

**Bailey Seybolt:** This meeting is being recorded.

**Mark Boyes-Smith:** Hey, team.

**Mark Boyes-Smith:** How's it going?

**Erik O'Brien:** Good.

**Erik O'Brien:** How are you doing, Mark?

**Mark Boyes-Smith:** Good.

**Mark Boyes-Smith:** Nice to meet you all.

**Mark Boyes-Smith:** I'm sorry I've been so difficult to get hold of over the past few weeks.

**Erik O'Brien:** It's been insane.

**Erik O'Brien:** been insane.

**Erik O'Brien:** No worries.

**Erik O'Brien:** know Frankie mentioned you guys are doing a bunch of work on the back end, so I totally get it.

**Mark Boyes-Smith:** It seems, I don't know what's going on, but where most businesses tend to slow down into the back half of the year, this business seems to get worse.

**Mark Boyes-Smith:** It's crazy.

**Mark Boyes-Smith:** We've got, and this week we have product leadership off-sites from Wednesday onwards.

**Mark Boyes-Smith:** Next week we've got exec off-sites for the entire week, and then we have the big HX birthday at the end.

**Mark Boyes-Smith:** So it's chaotic from day one.

**Mark Boyes-Smith:** Anyway, it's lovely to meet you all.

**Mark Boyes-Smith:** I think we should have Frankie joining us as well, but she is on vacation today, so maybe she'll catch the recording.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So just quick intros.

**Erik O'Brien:** Kirkland, and I'll let him do his own intro, but he's our engineer that will be helping with the setup.

**Erik O'Brien:** Bailey is managing editor working on HX.

**Erik O'Brien:** So she's, all the content pieces you see, and I believe she sent an email over about image generation as well.

**Erik O'Brien:** This is kind of more broadly the team working with HX on the back end.

**Mark Boyes-Smith:** Nice.

**Mark Boyes-Smith:** Nice to meet you both.

**Bailey Seybolt:** Nice to meet Yeah, same to All right.

**Erik O'Brien:** So I know Kirkland knows a lot more about the Framer and MCP setup than I do. Mark, is there anywhere you'd like to start, or anything you've learned from the Framer side about requirements they've passed along?

**Mark Boyes-Smith:** Not from my side. Is it worth me starting with a bit of context? I'm coming in totally fresh to this conversation, so I can maybe go from the beginning with what I know, and then we can join the dots.

**Mark Boyes-Smith:** Okay, cool.

**Mark Boyes-Smith:** So I oversee design at HX on the product side, but then also on the brand side as well. And we've been obviously thinking about how to elevate our brand experience. We're launching a new brand over the next month or so. And as part of that, we're rethinking about the website.

**Mark Boyes-Smith:** We've moved over to Framer, as Eric mentioned.

**Mark Boyes-Smith:** We're building that internally, leveraging a lot of AI capabilities in order to produce the right component tree.

**Mark Boyes-Smith:** Obviously, you've worked with David, who's working really, really closely with some AI engineers to develop the content for the website.

**Mark Boyes-Smith:** And as part of this, we're thinking critically about how do we create really great go-to-market content, articles, blog posts.

**Mark Boyes-Smith:** And I think that's where this engagement comes from, right?

**Mark Boyes-Smith:** Like, how do we actually tune the right AI engines in order to do that?

**Mark Boyes-Smith:** So that's probably where my knowledge ends.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So we are working with David, who's guiding the AI pipelines that are generating content. He's working very closely with Bailey and the team on what type of content we want to go for. How do we get that to go from zero to one?

**Erik O'Brien:** So that's what we've been working on over the past eight weeks or so.

**Erik O'Brien:** And then, so going forward, you know, we've been doing publishing fairly manually to Storyblock.

**Erik O'Brien:** And so going forward, we want to figure out how do we do kind of this automated publishing once we have the articles ready to go.

**Erik O'Brien:** And so I think that's where we come in with how do we get that automated publishing pipeline to work with Framer, given the kind of requirements they've, I think, shared with you of not using the API, but using the MCP plugin.

**Mark Boyes-Smith:** Right.

**Mark Boyes-Smith:** Okay.

**Mark Boyes-Smith:** That makes a lot of sense.

**Mark Boyes-Smith:** When we started to produce this website, I immediately went down the route of the API plugin, and then realized that they've decommissioned it and it's all MCP now. So a lot of the work that I've been doing is figuring out how to work with the product engine we have internally built with cloud code. I had mixed success with it, if I'm honest.

**Mark Boyes-Smith:** It's great for the one-off.

**Mark Boyes-Smith:** The bulk transactions are impossible.

**Mark Boyes-Smith:** I realized it was quicker for me to either script it in Python or do it myself, rather than trying to get Claude to actually run through any bulk kind of stuff.

**Mark Boyes-Smith:** So yeah, I think I know as much as you do on that one.

**Mark Boyes-Smith:** We have it working.

**Mark Boyes-Smith:** We understand how to do it from a credential perspective.

**Mark Boyes-Smith:** The biggest challenge that I've noticed with it is you have to be logged into Framer and have their MCP receiver open.

**Kirkland Gee:** You guys know that as well, right?

**Kirkland Gee:** Correct.

**Kirkland Gee:** Yeah.

**Mark Boyes-Smith:** It's annoying, you know, but I didn't want to say it the least.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I sort of did just to improve the concept, like set up our own Framer instance, just to make sure I understood how this works.

**Kirkland Gee:** And very, very similar experience.

**Mark Boyes-Smith:** I think it will probably mostly work.

**Kirkland Gee:** I mean, essentially, one thing is like what we're trying to accomplish isn't like...

**Kirkland Gee:** Like, rebuilding pages or, you know, creating new components or anything like that.

**Kirkland Gee:** We're just filling in boxes, essentially, like, for this field, put this content there.

**Kirkland Gee:** So I think it'll probably be fairly reliable, I would hope.

**Mark Boyes-Smith:** I think we've got a good chance of this as well.

**Mark Boyes-Smith:** Let me share my screen and show you the way we've got this set up.

**Mark Boyes-Smith:** And please tell me if this is not helpful.

**Mark Boyes-Smith:** There we go.

**Mark Boyes-Smith:** Okay.

**Mark Boyes-Smith:** So we tried a few different routes on this one.

**Kirkland Gee:** Can you see my screen by the way?

**Mark Boyes-Smith:** Cool.

**Mark Boyes-Smith:** So we tried a few different routes with this one.

**Mark Boyes-Smith:** The first one was to create a template for an article and then fill in.

**Mark Boyes-Smith:** I mean, this is the homepage, but, like, then fill in the content blocks using the MCP.

**Kirkland Gee:** So it identifies the ID and inserts the content.

**Kirkland Gee:** Yeah.

**Mark Boyes-Smith:** Mixed levels of success with that erring towards unsuccessful.

**Kirkland Gee:** I don't know if you had any different experience.

**Kirkland Gee:** No, same thing. Especially placements sometimes.

**Mark Boyes-Smith:** It would get a little weird or it might pick the wrong box.

**Kirkland Gee:** Yeah, the CMS route worked a little bit better for me in my testing.

**Kirkland Gee:** Yes, exactly.

**Mark Boyes-Smith:** And so that's where we got to as well.

**Mark Boyes-Smith:** So we have, right now, we have a super, super basic article setup.

**Mark Boyes-Smith:** And we could go away and create different templates for the different types of articles you might want, whether it's thought leadership or a quick thought or a note or something like that.

**Mark Boyes-Smith:** And then as Kirkland said, we came into the CMS and we built out a very, very simple metadata schema for this.

**Mark Boyes-Smith:** And then obviously mapped all of the story IDs from Storyblock, so we didn't lose all of that.

**Mark Boyes-Smith:** That seems to have worked particularly well.

**Mark Boyes-Smith:** No challenges there.

**Mark Boyes-Smith:** As I say, you're seeing some, like, missing information there where it just hasn't figured things out.

**Mark Boyes-Smith:** Doing this in bulk was a nightmare.

**Mark Boyes-Smith:** But what we've done is lifted and shifted everything from maybe a couple of weeks ago and put it in.

**Mark Boyes-Smith:** So it gave us, like, a really, really clean.

**Kirkland Gee:** Where does the actual, maybe it's just farther to the right, but the actual content of the article, yeah, it's just wasn't in the view.

**Kirkland Gee:** And that's all marked down, right?

**Mark Boyes-Smith:** So that's good.

**Mark Boyes-Smith:** Yeah, nice and easy.

**Mark Boyes-Smith:** And actually, I can, I mean, I can show you maybe an example of one that's filled out.

**Kirkland Gee:** All of this seems super straightforward.

**Kirkland Gee:** That content's over on the left, is that just pulling, like, from the headings in the content?

**Mark Boyes-Smith:** It is, yeah.

**Mark Boyes-Smith:** We have a component that does this already.

**Kirkland Gee:** It's a bit, I mean, it's obviously still a work in progress, but we like the idea of having the jump links there.

**Mark Boyes-Smith:** Yep, of course.

**Mark Boyes-Smith:** The other thing as well, David's been looking at bringing in a standard FAQ block for the bottom of key pages.

**Mark Boyes-Smith:** I don't know if, I'm curious if that's something that you would advise people bring on to things like article pages as well, just to get that flow through the website and from, I assume, from an SEO perspective.

**Kirkland Gee:** And if you build the component, there's no reason not to put it there.

**Kirkland Gee:** I might suggest if we can make it, like, toggleable so it's either there or there.

**Kirkland Gee:** That way, if there's an article where that's not relevant, you don't, like, you don't get it showing up empty or anything weird like that.

**Kirkland Gee:** But it's nice to have.

**Kirkland Gee:** And again, just, like, question, answer, question, answer, and set it up that way.

**Mark Boyes-Smith:** Yeah, yeah.

**Kirkland Gee:** Works well.

**Mark Boyes-Smith:** Cool.

**Mark Boyes-Smith:** So, I mean, from a frame of setup perspective, it's fairly straightforward.

**Kirkland Gee:** Cool.

**Mark Boyes-Smith:** Yeah.

**Mark Boyes-Smith:** Nothing more on that one.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** The only thing we have to sort of work out is, like, ideally, we can, when we run the workflow to create the content, we put a human review step at the end, take a look, click a button, and publish.

**Kirkland Gee:** Just making sure that, like, our workflows can connect properly and someone's going to have to have the MCP plugin open and, like, all that stuff.

**Kirkland Gee:** It's going to be a little bit fiddly, but I don't think it's anything too complicated.

**Mark Boyes-Smith:** Just tedious.

**Mark Boyes-Smith:** Yeah.

**Mark Boyes-Smith:** I wonder if they've got anything on their roadmap about just having a permanent MCP.

**Kirkland Gee:** There's something weird about that. I didn't know if it was like a third-party plugin for a while.

**Kirkland Gee:** Yeah, I thought so too.

**Kirkland Gee:** I was trying to figure that out too because it kind of feels like one, but maybe they're just trying to keep it sort of like opt-in for the more technical folks until it's a little bit, you know, ironed out.

**Mark Boyes-Smith:** Yeah.

**Mark Boyes-Smith:** So it's probably worth saying like we don't have any strong preference over the way that that metadata is structured, what goes in and what doesn't go in.

**Mark Boyes-Smith:** So I think what might even be ideal is if we get you keys to the system and allow you to just figure out what the right kind of schema is there that you need.

**Kirkland Gee:** Yeah, I think that would be great.

**Kirkland Gee:** Erik, I just need to think about like what, basically who needs access?

**Kirkland Gee:** Maybe one of the pod emails.

**Kirkland Gee:** I don't know if we have something with a Framer account already.

**Kirkland Gee:** I just don't want like just me to have access in case a different engineer or somebody else needs to take a look at something.

**Erik O'Brien:** Yeah, we can take that back. We are transitioning from pod zero to another pod, and I know those emails are also changing.

**Kirkland Gee:** We have a bunch of access emails, and trying to coordinate all that stuff gets unreal, but I think just one of those, the most relevant one, getting access to Framer, making sure that we can, like, I forget all the role levels, but whenever we need to be able to configure plugins so that we can actually turn that on and mess with that, should be fine.

**Mark Boyes-Smith:** Fab, yep, we can give that a go.

**Mark Boyes-Smith:** I think maybe just work with Frankie on that one.

**Kirkland Gee:** She can give you all the access. She has everything in it that you need.

**Kirkland Gee:** Excellent.

**Kirkland Gee:** Then, yeah, I think this, yeah, it looks like you guys have already done most of the work, and it'll just be a little bit of fiddling on our side, and we should be in good shape.

**Kirkland Gee:** So, unless you guys have other questions.

**Erik O'Brien:** Nothing on my mind.

**Erik O'Brien:** I think if you're clear, I'm clear.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** I didn't have any other questions on this, but I was wondering, as long as we have you here, if you wanted to take a quick look at the images that our pipeline is generating.

**Mark Boyes-Smith:** So, so weind.

**Mark Boyes-Smith:** We capture some feedback for our designer.

**Mark Boyes-Smith:** I'd love that.

**Bailey Seybolt:** That would be fantastic.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I'm just going to share my screen.

**Bailey Seybolt:** You don't need to see my meetings, but here we go.

**Bailey Seybolt:** Okay, cool.

**Mark Boyes-Smith:** Can you see those?

**Bailey Seybolt:** So I think the, I wasn't part of the initial conversation, but my understanding was we wanted to sort of go in a more graphic direction that aligned with your kind of updated branding.

**Bailey Seybolt:** My sense is that this maybe based on Frankie's comments went a little too far in the graphic direction, but I think any sort of feedback you have that we can pass along would be really helpful.

**Bailey Seybolt:** So we can kind of take another crack at this.

**Mark Boyes-Smith:** Absolutely.

**Mark Boyes-Smith:** So yeah, when we saw the first version of it, what was really interesting is the graphic sat firmly between where we were and where we're going, um, in a slightly uncomfortable spot.

**Mark Boyes-Smith:** And we recognized that we wanted our imagery to feel.

**Mark Boyes-Smith:** Like it evoked the brand, but not necessarily always to tie back to the core content of the article, knowing that some of the content was going to be fairly abstract in general, like trying to tie an image to it felt like probably a non-starter in some situations.

**Mark Boyes-Smith:** They can start to feel a little bit abstract in general, right?

**Mark Boyes-Smith:** And so we really want to play with the idea of geometric shapes, mathematical concepts.

**Mark Boyes-Smith:** We've got these like wonderful rich gradients that we're using now and layering over some of our geometric shapes.

**Mark Boyes-Smith:** All of these are things that we think we could play with as part of the AI generated art.

**Mark Boyes-Smith:** I know David has shared some like really interesting examples of actual scenes that can be depicted.

**Mark Boyes-Smith:** So it's almost like you pick a graphical style and then you kind of evoke lots and lots of different scenes in that graphical style.

**Bailey Seybolt:** I'm going to have to share something via email.

**Mark Boyes-Smith:** I don't have one to hand, but if we kind of turn up the level of complexity, it's going to require a bit more refinement and review from us.

**Mark Boyes-Smith:** And actually, we just need something that's really simple to get us out the gate so that whenever you see an article from us, it's just framed beautifully in our brand language.

**Bailey Seybolt:** Yeah, okay.

**Bailey Seybolt:** And Erik, are those examples something that you had?

**Bailey Seybolt:** Something that we have somewhere?

**Erik O'Brien:** I don't recall seeing one, so we might just have Mark send us.

**Bailey Seybolt:** Okay, yeah, Mark, if you want to send us anything you think would be helpful to give us, give our designer kind of more context around what you're thinking, that would be great.

**Mark Boyes-Smith:** Absolutely, yeah, can definitely do that.

**Mark Boyes-Smith:** I'm curious just to get your advice on, I mean, this is new territory for me, and I'm curious what the, like, the limitations are of AI gen artwork.

**Mark Boyes-Smith:** What would we consider a good bar to hit?

**Kirkland Gee:** I don't know, that's a really big, tough question. But let me give some perspective on some different things we've done.

**Kirkland Gee:** Because it's interesting, to say the least, of what it can and can't do.

**Kirkland Gee:** And there are things that I can be like, oh, yeah, I think it can do that and actually can't, and vice versa, just depending on what you're trying to do.

**Kirkland Gee:** It's like very specific colors are pretty much impossible.

**Kirkland Gee:** Like, if you're trying to get it to hit a very specific hex code, it'll generate four times, and it's going to be four very slightly different shades of that exact hex code, right?

**Kirkland Gee:** It's be really close.

**Kirkland Gee:** Like, you can even see, like, the red-orange color here.

**Kirkland Gee:** Like, they're the same, but they're not, right?

**Kirkland Gee:** And that's just, like, super consistent across everything.

**Kirkland Gee:** So some things that we've done is, like, whether that's kind of making colors less important in the images, like, where you're not trying to hit specific brand colors can be helpful.

**Kirkland Gee:** Or we've done, like, black and white illustrations to get around that in the past.

**Kirkland Gee:** Or we've done things where maybe we design a set of four or five different backgrounds that are in our brand color.

**Kirkland Gee:** And then we can sort of do an AI generated illustration on top of this background and then generate some text on top of that background to make like a hero image that has some predefined stuff that we know is good.

**Kirkland Gee:** And then sort of piecing in some little things here and there. That's helped get around some issues. It makes it a little less variable, right?

**Kirkland Gee:** Everything's not completely unique, but you're also sticking to some guidelines, fonts, colors, that kind of stuff, because that's where it really falls apart.

**Mark Boyes-Smith:** Got it.

**Mark Boyes-Smith:** Okay.

**Mark Boyes-Smith:** That's really helpful.

**Mark Boyes-Smith:** What we can do is I can regroup with my brand designer, pull together a couple of examples of things that we really love, and just see if we can send something over and put that to the test. That would be great. Cool.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** And I know in speaking with Frankie, we're also happy to just use kind of like a rotating header.

**Erik O'Brien:** Featured image that you guys have already that's like in your library as a placeholder until we get something that's more appropriate for each article.

**Erik O'Brien:** So happy to go in a few different directions depending on kind of the output and the fidelity we can get to.

**Mark Boyes-Smith:** I'm kind of hoping that we don't have to do that.

**Mark Boyes-Smith:** Like I had suggested it as a fallback, but I'm hoping that we can achieve something that feels like predictable enough and evocative enough to use.

**Mark Boyes-Smith:** The one thing that I wanted to avoid, I think you'll get this, is like I don't want us to be the equivalent of iStockphoto for AI.

**Mark Boyes-Smith:** If I can avoid that, because we've put so much attention into making the brand feel ownable and unique in the marketplace.

**Mark Boyes-Smith:** The last thing I want to do is kind of put in artwork that feels overly generic just because we haven't put the investment and attention into working with you and the team to get it right.

**Mark Boyes-Smith:** So that's the only thing that I'm trying to avoid, but we can do a little bit more work on our side too.

**Erik O'Brien:** Bailey will share this with our designer to give them some better feedback. Wonderful.

**Mark Boyes-Smith:** Fab.

**Mark Boyes-Smith:** Well, it was really lovely to meet you all.

**Mark Boyes-Smith:** Is there anything else I can help with?

**Kirkland Gee:** No, I don't think so, at least from my side.

**Bailey Seybolt:** Yep.

**Erik O'Brien:** So we will work with Frankie, get her the right kind of team email access for the API keys, and then, or not the API keys, but for Framer access.

**Erik O'Brien:** Yes.

**Erik O'Brien:** And then we will get to work on kind of seeing what we can come up with.

**Mark Boyes-Smith:** Nice.

**Mark Boyes-Smith:** Are you on our Teams instance so that we can just have a back and forth as you need things?

**Erik O'Brien:** Unfortunately not.

**Erik O'Brien:** We have Slack.

**Erik O'Brien:** So email's been the way that, yeah, email's been, unfortunately, the way that we've been communicating back and forth with Frankie outside of our Notion space.

**Erik O'Brien:** So I think that'll work, at least for the time being.

**Mark Boyes-Smith:** That's fine.

**Mark Boyes-Smith:** Not a problem at all.

**Mark Boyes-Smith:** If there's anything you need, drop me an email, ccfranky, because she'll prompt me if I miss it.

**Mark Boyes-Smith:** And we can build out any components that you need as well to make those articles look amazing.

**Kirkland Gee:** So I'm really looking forward to working with you all.

**Erik O'Brien:** Awesome.

**Bailey Seybolt:** Thanks so much.

**Mark Boyes-Smith:** Thanks very much.

**Mark Boyes-Smith:** Great to meet you.

**Mark Boyes-Smith:** See you later.

**Kirkland Gee:** Have a great day.

**Kirkland Gee:** Bye.

**Erik O'Brien:** you.

**Erik O'Brien:** Bye.
