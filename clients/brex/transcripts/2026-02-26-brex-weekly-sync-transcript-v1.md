# Brex <> GrowthX - Weekly Sync
**Date:** February 26, 2026
**Duration:** 36 minutes
**Participants:** George Haikal (GrowthX), Jon Kowieski (Brex), Alex Rudyak (Brex), Yolanda La (Brex), Marcel (GrowthX), Aida (GrowthX)

---

## Summary

- **FINRA Compliance:** New guidelines require review of all content mentioning banking, yield claims, or Brex products. Even minor copy changes now need compliance approval. Yolanda and Abby are working with Nancy to define exact scope and push back where possible to avoid blocking SEO efforts.
- **Resources Hub Redesign Feedback:** Bango (Chief Design Officer) reviewed the redesign. Key feedback: add blog and Brex Benchmark to navigation, keep existing typography and image sizes, move tags above "Read More" buttons, adjust CTA copy, and use breadcrumb bar above secondary nav.
- **Navigation Wins:** Main navigation changes had the fewest objections. Adding blog, benchmark, and topics index were approved. This is the highest-impact change.
- **Technical Access:** Kurt has his Brex laptop and can build locally, but still needs Vercel access to submit PRs. Jon is coordinating with admins to expedite.
- **Team Transition:** Jon Kowieski's last day is March 10. Yolanda La will take over as primary Brex contact. Knowledge transfer underway.

## Action Items

**George Haikal**
Share redesigned Resources Hub incorporating blog and Brex benchmark together in navigation (11:33)
Adjust CTA copy on resources and articles pages to clarify purpose, replacing confusing language (16:34)
Assemble and circulate updated version of redesigned Resources Hub post feedback integration (30:45)
Contact Kurt regarding pending Vercel access to unblock PR submissions (32:22)
Coordinate knowledge transfer and next steps with Yolanda as John prepares to depart (34:30)

**Jon Kowieski**
Follow up with admin contacts to expedite Vercel access approval for Kurt (32:28)
Assist in final adjustments and design review rounds with Bango and other stakeholders (29:17)
Support Yolanda and George with transition and access questions until March 10 (35:26)

**Yolanda La**
Work with Abby and Nancy to clarify FINRA compliance content review processes and document necessary guidelines (05:36)
Collaborate in ongoing SEO and content compliance strategy to avoid bottlenecks while maintaining marketing effectiveness (07:37)
Assume project communications and ownership from Jon following his departure (34:30)

**Alex Rudyak**
Participate in next design review round to provide UX, SEO, and customer perspective support alongside Bango (29:21)

---

## Key Decisions & Details

### Compliance (FINRA / Capital One)
- FINRA compliance now applies to all content mentioning Brex products, banking, or yield. Not just articles, but any marketing materials.
- Tools pages are likely exempt unless they reference specific Brex rates or products.
- Even two-word changes in existing articles require compliance review going forward.
- Yolanda and Abby meeting with Nancy to define boundaries and push back on overly broad scope.
- Resources Hub and tools sprint are not blocked by compliance for now.

### Resources Hub Redesign (Bango Feedback)
- **Navigation:** Add blog and Brex Benchmark to the resources nav. Remove careers (Jon noted it no longer fits). Topics index approved.
- **Featured content:** Right-side featured article should be static, currently pulling the Capital One acquisition announcement.
- **Sub-navigation:** Bango wants breadcrumb bar to stay visible with secondary nav stacked below it. Jon expressed reservations about how this will look but confirmed the requirement.
- **Typography/Design system:** Keep existing font sizes, image proportions, and spacing. No deviations from current design system. This was Bango's top priority across all pages.
- **Tags:** Move tags (e.g., Spend Trends, CFO) above "Read More" buttons across all resource types.
- **CTA:** Keep the CTA section but change copy. Current "Join the waitlist" language confused Bango. Jon suggested something like "Keep up with Brex benchmark and product updates."
- **Case studies:** Keep rectangular images (not square). Three per row instead of four to maintain readability within the design system.
- **Ebooks:** Current filter doesn't work properly for ebooks-only browsing. Jon convinced Bango of the need for better organization but didn't get explicit approval yet. Building it out anyway.
- **Article template:** Keep existing typography. Add author, date, time to read, and topic tag above title. Header images fine for Spend Trends (improve engagement). Table of contents can be dropdown style. Social share limited to LinkedIn and Twitter only.
- **Approval process:** Bango appreciated the detailed write-up George prepared. Expects to see next version in Sanity (not Render). Multiple revision rounds are normal (Bango's banking page went through 12 rounds).

### Technical Access
- Kurt has Brex laptop and local build environment working.
- Charge finder tool is built and ready for PR submission.
- Blocked on Vercel access. Kurt requested it but hasn't received it yet.
- Greg (key engineering contact) is in Japan, back next week.
- Jon reaching out to the contractor who handles access provisioning.

### Team Transition
- Jon Kowieski leaving Brex on March 10.
- Yolanda La taking over as primary point of contact.
- Alex Rudyak continuing in his role.
- Jon available via Slack for access and technical questions until departure.

---

## Transcript

**George Haikal:** Hey Alex, how's it going?

**George Haikal:** Hey Yolanda.

**Yolanda La:** Hey everyone.

**Yolanda La:** How are you?

**George Haikal:** Doing well, doing well.

**George Haikal:** Good to see you both.

**Alex Rudyak:** Likewise.

**George Haikal:** Haven't seen you since the.

**George Haikal:** You guys had the.

**George Haikal:** The offset in Vegas.

**George Haikal:** Yeah.

**Yolanda La:** Yes.

**Yolanda La:** It's been a moment.

**George Haikal:** Yeah.

**George Haikal:** Sounds like that all went well though.

**Alex Rudyak:** Yeah.

**Alex Rudyak:** Sko so.

**Yolanda La:** Oh, you just got back?

**Alex Rudyak:** Yeah, I got back last night so I'm in full survival mode to.

**George Haikal:** Survival mode.

**George Haikal:** Yeah, I feel that, I feel that.

**George Haikal:** How is there any big takeaways from that scale?

**Alex Rudyak:** We're pretty awesome, you know.

**Yolanda La:** Is that as fun as one one Brex?

**Alex Rudyak:** No, not even close.

**Jon Kowieski:** But that's reassuring.

**Jon Kowieski:** Yeah.

**Alex Rudyak:** Jokes aside about being awesome, I mean looking at our customer base, when you think about the most valuable progressive companies in the world.

**Alex Rudyak:** OpenAI Anthropic, both customers, there's a reason that they decided to go with us versus others.

**Alex Rudyak:** It's hard to like argue with that.

**George Haikal:** You just can't argue with that.

**George Haikal:** Yeah.

**Alex Rudyak:** Because you know they do their due diligence

**George Haikal:** Is there anything top of mind for you and.

**George Haikal:** Hey John, good to see you again from the Capital One acquisition.

**George Haikal:** I know.

**George Haikal:** I think I just saw a chat come in earlier about some more compliance reviews for new things we want to do on the site.

**George Haikal:** Just curious if there's anything else that's top of mind from there before we jump in.

**Alex Rudyak:** Nothing in addition to that.

**Alex Rudyak:** I can't even say that I saw that one but let me check that out.

**Yolanda La:** That conversation came more so from my end.

**Yolanda La:** We recently had some FINRA compliance guidelines to be made updates across the website more so towards our banking articles or any mentions of like yield, industry leading yield, that type of thing.

**Yolanda La:** And then more recently it looks like they want reviews across basically all content that we are producing within spend trends but across the website as well.

**Yolanda La:** I don't think it will bleed over into like tools.

**Yolanda La:** It's more so whenever we talk about our products and us marketing our products where they legal to come through and review.

**Yolanda La:** So a lot of our long form content is I think is where it's going to be at.

**Jon Kowieski:** So the tools pages it could be in like expense management pages per state for example.

**Jon Kowieski:** So if you actually bring up racks in the product those are going to have to go through compliance now.

**Jon Kowieski:** So and if you even change two words like Yolanda and I were talking about, it's going to have to go through compliance now.

**Jon Kowieski:** So any refreshes we do have to go through compliance.

**Jon Kowieski:** So yeah, that's where this is probably moving forward.

**Jon Kowieski:** What will need to happen.

**Jon Kowieski:** Abby on our team, she pulled some magic before and we were able to not go through this process like the blog.

**Jon Kowieski:** But now Capital One definitely wants to make sure we're much more compliant.

**Jon Kowieski:** So that's why this change is happening.

**George Haikal:** Okay, that's helpful.

**George Haikal:** I mean, still needed some clarity on like what that would actually look like.

**George Haikal:** But in terms of the Resources Hub and the tools that we want to sprint on, sounds like we're not blocked by the compliance.

**George Haikal:** It's more so articles or anytime Brex is mentioned.

**George Haikal:** Is that accurate?

**George Haikal:** Is that fair?

**Jon Kowieski:** I think that's the most accurate for now.

**Jon Kowieski:** Like until we get more information.

**Yolanda La:** Yeah, I think they're still working through it.

**Yolanda La:** Abby and I might have a conversation with Nancy to go through the details of exactly, you know, what is what needs to to go through.

**Yolanda La:** We may try to push back just so that, you know, we're not hindered in terms of our SEO efforts.

**Yolanda La:** Like I said, like the two word change, like that needs to be documented, but we can't have two word changes go through review every single time.

**George Haikal:** We are on the same page there.

**George Haikal:** Okay, let me share my screen.

**George Haikal:** Unless there there's anything else top of mind for you all, but definitely have some progress that I want to make sure we run through today to get your thoughts on.

**George Haikal:** Cool, Let me get you on my screen here.

**George Haikal:** So to catch Alex and Yolanda up on some context.

**George Haikal:** Essentially what our main goal is right now is to sprint on the Resources Hub redesign.

**George Haikal:** The redesign of the.

**George Haikal:** And redesign might be a strong word, right?

**George Haikal:** The refinement of the current experience for the Resources Hub that lives on brex.com to do that, John and I went back and forth on a bunch of different versions of what our design engineer put together for what the new experience should look and feel like.

**George Haikal:** All optimized for SEO.

**George Haikal:** So flat tagging, a better hero experience, topics and relevant content being pulled first.

**George Haikal:** All with the ability to be categorized, searched for and then a sub nav that's constant.

**George Haikal:** Same thing with this new filtering topic type new experience again, we went back and forth and I know Bango has the final say here on design.

**George Haikal:** And so what I wanted to spend the bulk of this meeting with is John met with Bango earlier this week on this new redesign and it sounds like you, you got some pretty clear feedback on the next step.

**George Haikal:** John, I would love to understand even page by page what that looks like to make sure my team can sprint, get it done and we can push this through.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So let's start with the resources and the navigation.

**Jon Kowieski:** His big thing is where's the blog in this?

**Jon Kowieski:** Because it went from like we did side by side comparison.

**Jon Kowieski:** Like it before you could see like one of them was Brex benchmark in the blog, which I'm like, yeah, maybe we could make the articles one that if that's his biggest concern.

**Jon Kowieski:** The other thing in the resources that we actually got rid of was careers.

**Jon Kowieski:** He didn't notice, but I did.

**Jon Kowieski:** So that might be something he might pick apart next time.

**Jon Kowieski:** By the way, I don't think careers actually make sense in here anymore with what your new version was.

**Jon Kowieski:** But the one thing I actually loved was I convinced him to do the topics.

**Jon Kowieski:** So he was okay with that index.

**Jon Kowieski:** He was okay with.

**Jon Kowieski:** But yet again, his biggest comment was the blog and Breck's benchmark.

**Jon Kowieski:** One of his bigger things is pushing Breck's benchmark.

**Jon Kowieski:** Okay.

**Jon Kowieski:** I kind of asked actually like, hey, what if we just changed what is reports on the left?

**Jon Kowieski:** Like, what if we called that Brex benchmark and it was like, I don't know.

**Jon Kowieski:** So a little bit in between there.

**Jon Kowieski:** But potentially that first.

**Jon Kowieski:** First one could just be the blog and Brex benchmark.

**George Haikal:** Yeah, that's what I'm thinking here as well.

**George Haikal:** Yeah.

**George Haikal:** Because this is very easy for us to edit and fix.

**George Haikal:** And so what we'll do is we'll pull in the blog here, we'll pull in the blog here, and then we'll pull in the benchmark as well and we'll just replace.

**Jon Kowieski:** And then on the far right of this, I think we even had this discussion advance.

**Jon Kowieski:** George.

**Jon Kowieski:** It's so funny.

**Jon Kowieski:** But yeah, he's like, I just want to have what we have now.

**Jon Kowieski:** And I think I told you in the beginning, I'm like, yeah, I think we're going to need to cool.

**Jon Kowieski:** Be able to control what's in that.

**Jon Kowieski:** And I was like, I had a feeling like that specific article is what we want to highlight for a while there.

**Jon Kowieski:** So he definitely wanted that made it very easy fix.

**George Haikal:** Yeah, we can have it.

**George Haikal:** Pulling the acquisition announcement.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So nothing huge there, I thought.

**Jon Kowieski:** And then on to like the actual resource, the main page.

**Jon Kowieski:** Do you want to do the main resources page?

**George Haikal:** Yes.

**George Haikal:** Which we are on.

**Jon Kowieski:** No, this is the case study one.

**Jon Kowieski:** Sorry.

**George Haikal:** Oh, resources.

**George Haikal:** Sorry.

**Jon Kowieski:** So the very top, the very first thing you did was actually cross out in the upper left resources.

**Jon Kowieski:** You just crossed it out.

**Jon Kowieski:** Like, I don't want this okay.

**Jon Kowieski:** So I was like, okay.

**Jon Kowieski:** And then like that upper right navigation.

**Jon Kowieski:** This I was trying to tell you before, he wants that in a similar style is like what is on the current resource center page, which we did have a back and forth on, by the way.

**Jon Kowieski:** I was like, this is going to make it easier for UX people to discover things like that.

**Jon Kowieski:** He's like, I really like the spacing and I like how like this is.

**Jon Kowieski:** So this might be.

**George Haikal:** So just to be clear, he likes how this sub nav looks currently.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Like breadcrumb.

**Jon Kowieski:** But it could be above.

**Jon Kowieski:** And I was trying to get to that.

**Jon Kowieski:** So he does want like the breadcrumbs when you go into this other sections to look the same.

**Jon Kowieski:** Like that breadcrumb right there in the upper left.

**Jon Kowieski:** Right there.

**Jon Kowieski:** He likes that style.

**Jon Kowieski:** And I was like, okay.

**Jon Kowieski:** Like I try to talk him out of it.

**Jon Kowieski:** He wants to keep that.

**Jon Kowieski:** So I was like, okay.

**Jon Kowieski:** And then he wants the navigation you essentially made in the upper right to go under that.

**Jon Kowieski:** Which I was like, I don't know what this will look like.

**Jon Kowieski:** So I do think it.

**Jon Kowieski:** By the way, I should have probably said this.

**Jon Kowieski:** George, when we do things like this, it goes through multiple rounds of revisions.

**Jon Kowieski:** So our new banking page probably went through 12 rounds actually.

**Jon Kowieski:** Yeah, people don't know that.

**Jon Kowieski:** So.

**Jon Kowieski:** Oh, and then the one thing about that, he wants to keep the original.

**Jon Kowieski:** And I think I sent this to you.

**Jon Kowieski:** Typography sizes, depth.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Which I was like, okay, this is probably like the brand guidelines kind of stuff.

**Jon Kowieski:** But he was not for if you scroll down changing these sizes.

**Jon Kowieski:** Oh, right there.

**Jon Kowieski:** Actually go up.

**Jon Kowieski:** Making this change.

**Jon Kowieski:** He was not for if you go up like you change the left image size.

**Jon Kowieski:** I would say he's like, I just want to keep it what it is,

**George Haikal:** but keep it what it is.

**George Haikal:** Can you help me understand what you mean?

**Jon Kowieski:** Like this style.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** And I was like, okay.

**Jon Kowieski:** But if you go back to yours, like he wants to keep.

**Jon Kowieski:** Yes.

**Jon Kowieski:** This style.

**Jon Kowieski:** The one thing though is the tags, the spend trends and the cfo.

**Jon Kowieski:** He wants that.

**Jon Kowieski:** But he wants it below or he wants it above.

**Jon Kowieski:** Read more.

**Jon Kowieski:** So he just wants it moved down to be above.

**Jon Kowieski:** Read more.

**Jon Kowieski:** And that's across this page.

**Jon Kowieski:** He's okay with Buy Brex January.

**Jon Kowieski:** I was like, he's like, yeah, we can do that.

**Jon Kowieski:** Because I was explaining why for like C. SEO purposes.

**Jon Kowieski:** But he does want to keep the style.

**Jon Kowieski:** But if you go down the CTA, he even right here we actually have like five to 10 minutes.

**Jon Kowieski:** Like why I try to convince him why we need this?

**Jon Kowieski:** Um, and I think the only thing he's like, what is this?

**Jon Kowieski:** A newsletter cta?

**Jon Kowieski:** I'm like, this could be a CTA for anything.

**Jon Kowieski:** And I was trying to convince him.

**Jon Kowieski:** I'm like, when we do winter release, spring release, all that, I'm like, this is what we need for that.

**Jon Kowieski:** Or we get people when a new blog comes out, we send them the new blog.

**Jon Kowieski:** He's like, I think he just don't like the copy is what it I got from it.

**Jon Kowieski:** And when he saw Join the wait list, he's like, so this is a newsletter.

**Jon Kowieski:** He didn't make it like completely clear.

**Jon Kowieski:** So I think what just needs to happen is.

**Jon Kowieski:** Yes, we just need to change that copy.

**George Haikal:** Yeah, we can just replace this with the current CTA that you have copying with.

**Jon Kowieski:** I think that's about it.

**George Haikal:** Is there a good example that we can pull from here just while we're on the cta?

**Jon Kowieski:** I. I would say something like, keep up with Brex benchmark and Brex product updates or something along those lines.

**Jon Kowieski:** And just not that.

**George Haikal:** And then this would be.

**Jon Kowieski:** I gotta think through that.

**Jon Kowieski:** Like, okay, I at least got him not to remove it.

**Jon Kowieski:** I'm just like, he agreed to do like the copy change, though.

**Jon Kowieski:** And I was like, yeah.

**Jon Kowieski:** And like I said, like I just said, we go through multiple rounds.

**Jon Kowieski:** We've never had one, two rounds, three rounds, four rounds, multiple rounds.

**Jon Kowieski:** But I feel like most of these, maybe we do get to two rounds.

**Jon Kowieski:** So this.

**Jon Kowieski:** He was fine with adding these new ones.

**Jon Kowieski:** But what he didn't like was the sizes.

**Jon Kowieski:** He wants to keep the image sizes.

**Jon Kowieski:** So if you go on the actual page right now, he wants to keep the size like those sizes, like what's on the page.

**Jon Kowieski:** Which is weird because the case studies are actually a different size.

**Jon Kowieski:** I didn't realize that, but.

**Jon Kowieski:** So he does not like the square.

**Jon Kowieski:** He's like, rectangle.

**Jon Kowieski:** I want to keep our current design system, which would get.

**Jon Kowieski:** This would not be four, this would be three.

**Jon Kowieski:** If you look at that.

**Jon Kowieski:** Unless you like shrink them down.

**Jon Kowieski:** But then the UX would be absolutely terrible and you won't be able to read anything.

**George Haikal:** But for case studies, it would be for.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So yet again, he just wants the tags above the read more buttons.

**Jon Kowieski:** But he allowed that, which I was like, cool.

**Jon Kowieski:** We actually didn't lose that.

**Jon Kowieski:** And the see all he was fine with too, where we put it.

**Jon Kowieski:** Then the rest of this he was fine with adding as long as you continue doing the same thing, like tags below.

**Jon Kowieski:** So he was cool with adding all of this, which I was like, thank you.

**George Haikal:** Amazing.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So it's really.

**George Haikal:** And then just so I remember.

**George Haikal:** So I think the biggest question mark still here is the sub nav.

**George Haikal:** So remove resources.

**George Haikal:** The sub nav.

**George Haikal:** It sounds like he wants it to.

**George Haikal:** Is it to look exactly like this, like underlined and under resource center.

**Jon Kowieski:** I think he wanted it above.

**Jon Kowieski:** So that's where I say like he wanted.

**Jon Kowieski:** How he described it was like leverage a breadcrumb bar and add the secondary nav below it.

**Jon Kowieski:** I wrote this down because it was kind of confusing to me, but that is what he said word for word.

**Jon Kowieski:** It's the one thing I was like kind of confused about.

**Jon Kowieski:** But what I mean by that is like you.

**Jon Kowieski:** You see resources slash articles right there.

**Jon Kowieski:** It's like you make that the breadcrumb bar and then below that you have your secondary nav that you have on the right below that.

**Jon Kowieski:** It's going to look weird.

**Jon Kowieski:** I think I thought this was not my preference, but maybe it'll take him seeing that.

**George Haikal:** So it sounds like you want to stack, stack this sub nav basically under here, replacing the resources or honestly under the resources.

**George Haikal:** Because he still wants to see the breadcrumb.

**Jon Kowieski:** Yes, that's exactly what it is what you just said.

**George Haikal:** Okay, so

**Jon Kowieski:** I'm not sure how that's going to look.

**Jon Kowieski:** Be honest.

**Jon Kowieski:** But I was like, okay.

**Jon Kowieski:** I tried to explain why we should keep it as well.

**Jon Kowieski:** And I tried very hard.

**Jon Kowieski:** But that was one thing that was really important to him.

**Jon Kowieski:** I think.

**Jon Kowieski:** I. Yeah, I didn't.

**Jon Kowieski:** I'm not sure why.

**Jon Kowieski:** So then if you went into articles, I think he was fine with most of this.

**Jon Kowieski:** The one thing is most of this is like spend trends, to be honest.

**George Haikal:** Same thing here with the tags.

**Jon Kowieski:** Yeah, same thing.

**Jon Kowieski:** Just put it below and then every.

**Jon Kowieski:** That's.

**Jon Kowieski:** Those changes are all fine.

**Jon Kowieski:** So yeah, across the board.

**Jon Kowieski:** It's just moving the tags above.

**Jon Kowieski:** Read more.

**Jon Kowieski:** So ebooks, by the way, this very page, I think I got him to understand why we need it, but he actually bought me on this one.

**Jon Kowieski:** So whatever our normal ebooks pages, I gotta find it.

**Jon Kowieski:** Like there's no organization in it.

**Jon Kowieski:** You can't find.

**Jon Kowieski:** Like if I'm in accounting, I only want to see the accounting ebooks.

**Jon Kowieski:** So I would build this out personally.

**Jon Kowieski:** But in the next round there might be a little bit of back and forth.

**Jon Kowieski:** But I feel like I explained it why it's a UX experience that helps discover these.

**Jon Kowieski:** And if I only want to read about the AI ebooks, the only way I could possibly do that is coming here in one click.

**Jon Kowieski:** So we were going through the original ebooks page, by the way.

**Jon Kowieski:** It's like you have to go through the filter and this is just like a back and forth.

**Jon Kowieski:** I'll send you what it is.

**Jon Kowieski:** Like go on the normal resources ebooks page.

**Jon Kowieski:** I'll send it in the chat.

**Jon Kowieski:** The filter doesn't actually work for ebooks only.

**Jon Kowieski:** Yeah, yeah.

**Jon Kowieski:** So I explained this.

**George Haikal:** Does it even I can't even click ebooks.

**George Haikal:** It took a while but.

**Jon Kowieski:** So you go to that filter and right there just click on the AI because I was actually showing this live and why it doesn't work and why we needed what you have.

**Jon Kowieski:** I was like, I only want to see the E box.

**Jon Kowieski:** And now I just had to do that and maybe I can go to content type.

**Jon Kowieski:** But that literally just took me a couple click like and that's where I was explaining like UX wise, it took me one click.

**Jon Kowieski:** With what Grotex created, it's also much easier to discover just the ebooks themselves.

**Jon Kowieski:** So I'd say just keep it.

**Jon Kowieski:** He was not actually super clear on this.

**Jon Kowieski:** So you can just say I said that.

**Jon Kowieski:** So.

**Jon Kowieski:** But yet again the most important thing to him was the typography staying the same.

**Jon Kowieski:** That was the number one thing he said across all these new pages.

**Jon Kowieski:** So I'm just making you aware of exactly like what I did and I made this like comparison that you're looking at now and how bad it is.

**Jon Kowieski:** So we went through that.

**Jon Kowieski:** So I'd say do it.

**Jon Kowieski:** But he didn't say for sure, yes or no.

**Jon Kowieski:** I think he's thinking through it still.

**Jon Kowieski:** But here's the thing and I told you George, he wants to see it.

**Jon Kowieski:** Insanity.

**Jon Kowieski:** He didn't want to see it in on render and I explained why we had to do that.

**Jon Kowieski:** So.

**Jon Kowieski:** But yeah, build it out this way.

**Jon Kowieski:** It's better for organization and like it's better for their website.

**Jon Kowieski:** So the case study part though, yet again it's like the same layout.

**Jon Kowieski:** I'm sorry, if you go to your render now, like the resources articles like ebooks.

**Jon Kowieski:** Yeah, build it out.

**Jon Kowieski:** The case study section though is actually different.

**Jon Kowieski:** So he wants like I said, the original typography, image design.

**Jon Kowieski:** The design system is what it's called.

**Jon Kowieski:** So okay, yet again he like that cta.

**Jon Kowieski:** We just got to figure out like to call it something else.

**Jon Kowieski:** And that's how I was able to like keep it and make it so he didn't eliminate it.

**Jon Kowieski:** Like we can switch up the copy and he's like, okay, let's do that.

**Jon Kowieski:** All right, so that was fine.

**Jon Kowieski:** And then the index was fine.

**Jon Kowieski:** We went through that.

**Jon Kowieski:** I explained that tools, it's very much like Spend Trends have full control.

**Jon Kowieski:** It's just the design system.

**Jon Kowieski:** So yeah, same thing.

**Jon Kowieski:** Good to go on this.

**Jon Kowieski:** And then the article template, this was not a fun.

**Jon Kowieski:** Not a fun part of the review.

**Jon Kowieski:** So if you click on that article yet again, I want to keep the existing typography.

**Jon Kowieski:** So why I at least got him to include like the author date type, time to read and you put expense management above the title.

**Jon Kowieski:** That's fine.

**Jon Kowieski:** If you're doing this with Spend Trends, the header image is fine.

**Jon Kowieski:** We stripped out the header image to increase site speed as well as get people engaged with the page.

**Jon Kowieski:** But that can be added to all spend runs, by the way.

**Jon Kowieski:** So I think that is completely fine.

**Jon Kowieski:** He doesn't need to approve that.

**Jon Kowieski:** And one thing on the side I had to ask through like the table of contents, like he was fine with it, but he's like, why not just keep like what we have on the page where it's like a drop down.

**Jon Kowieski:** So either way that should be fine for all Spend Trends, by the way, which is majority of the articles on this website.

**Jon Kowieski:** So got it.

**Jon Kowieski:** And then the other thing I had to convince him was those new social buttons.

**Jon Kowieski:** And I think it would actually just be Twitter, LinkedIn and then the link we don't have Facebook.

**Jon Kowieski:** I don't think so.

**Jon Kowieski:** He was like, yeah, I don't.

**Jon Kowieski:** That doesn't make sense for us.

**George Haikal:** Unless you're just Twitter.

**Jon Kowieski:** Yeah, well, LinkedIn, we're super active.

**Jon Kowieski:** LinkedIn and Twitter were super active.

**George Haikal:** Okay, we'll just make it just LinkedIn and Twitter.

**Jon Kowieski:** Yeah, but he looked at the whole page and did not enjoy the typography.

**Jon Kowieski:** The topics at the very bottom, by the way.

**George Haikal:** Uhhuh.

**Jon Kowieski:** The tags.

**Jon Kowieski:** Yeah, you can do that is fine for spun friends.

**Jon Kowieski:** So we went over that too.

**Jon Kowieski:** So the typography would be the same for the faq but kind of like how you're styling it and then related articles section, as long as it's in the design system for images and typography.

**Jon Kowieski:** But the changes that you had there are fine because you added on like author date, time to read, tag, read more.

**Jon Kowieski:** So yeah, you can do all that.

**Jon Kowieski:** So I feel like that's everything.

**Jon Kowieski:** He did ask, by the way.

**Jon Kowieski:** And I had to explain this, like, yeah, I'd love to actually go through that topic in the main nav in the role.

**Jon Kowieski:** I was like, well, like we can't really create that doing this with.

**Jon Kowieski:** Yeah, he just wanted to see what it looked like and if it looks like this, it's like completely fine.

**Jon Kowieski:** That's what I'll say.

**Jon Kowieski:** I'll say just create it.

**Jon Kowieski:** It'll be better for the overall website at the end of the day.

**Jon Kowieski:** So that was basically his notes.

**Jon Kowieski:** It's kind of what I thought coming in because I've been through so many different design reviews for product patients.

**Jon Kowieski:** Probably close to like 40, so.

**Jon Kowieski:** But yeah, not a lot of crazy comments which I was glad.

**Jon Kowieski:** I'm like, I will take like whatever Bangle will give me at the end.

**George Haikal:** Yeah.

**Jon Kowieski:** But I think if we get Alex next round to go through it with him and show like your changes, it will be very helpful.

**Jon Kowieski:** So he heard from me UX technical SEO user journeys and why it would benefit.

**Jon Kowieski:** And he was also very happy by the way of your write up right away, like I told you, he was like, yes, I'm very glad they did that.

**Jon Kowieski:** I'll take a look.

**Jon Kowieski:** So he's like, I'm very busy.

**Jon Kowieski:** I normally don't have time to like think through all this stuff very thoroughly.

**George Haikal:** So I'm glad it was helpful.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So that was super helpful.

**Jon Kowieski:** But we at least got most of your changes actually into this.

**Jon Kowieski:** I would say so.

**Jon Kowieski:** The main thing, to be honest, that was on my mind for a long time was actually the main navigation, which is big.

**George Haikal:** Yeah.

**George Haikal:** That sounded like.

**George Haikal:** Had almost the least amount of comments.

**George Haikal:** Just adding the blog, adding the benchmark and then just having the static latest be the.

**George Haikal:** Or the article being pulled to the latest be the acquisition.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** And if that's all he cares about, I was like, I'll take everything else they added.

**George Haikal:** Amazing.

**Jon Kowieski:** I mean that in the main nav will actually be more powerful than the rest of this.

**George Haikal:** Definitely.

**Jon Kowieski:** So I've wanted it since like day one.

**George Haikal:** So yeah, that's huge.

**George Haikal:** Okay, this is helpful.

**George Haikal:** I guess, or I don't guess.

**George Haikal:** Our team will put together another version of this incorporating all those edits.

**George Haikal:** We'll get back to you when that's done.

**George Haikal:** But I want to get ahead of like access and like how we would actually implement these changes.

**Jon Kowieski:** Oh, does.

**Jon Kowieski:** I thought you had the right access now.

**Jon Kowieski:** Did he not.

**Jon Kowieski:** Did Kurtland not get out his laptop?

**George Haikal:** There's one.

**George Haikal:** He got his laptop and there's one thing we're waiting on, which is his Vercell access.

**George Haikal:** We already have the charge finder tool completely ready just for him to submit a pr.

**George Haikal:** He needs the Vercel access and he said he requested it yesterday.

**George Haikal:** So yes, on the laptop?

**George Haikal:** Yes.

**George Haikal:** On the access to build locally so we weren't unblocked and building the tools anymore.

**George Haikal:** He's already built that out.

**George Haikal:** But to be able to get into the code base and submit a pr.

**George Haikal:** This last piece of Vercel access that he requested yesterday is what we need, did he not?

**Jon Kowieski:** So Greg is in Japan.

**Jon Kowieski:** He'll be back next week.

**Jon Kowieski:** By the way.

**Jon Kowieski:** He's, like, skiing, I think.

**George Haikal:** Nice.

**Jon Kowieski:** So I think.

**Jon Kowieski:** I mean, Greg and Kurt, like, clearly, it's awesome that you've been talking with them because they help a ton.

**Jon Kowieski:** And then I could reach out to.

**Jon Kowieski:** It's like a contractor that is giving access to.

**Jon Kowieski:** So I've been like, talking to him every time you've had issues.

**Jon Kowieski:** So he needs first cell, but he requested it and he didn't get it.

**George Haikal:** Yeah.

**Jon Kowieski:** Can you like, actually mention this to Kurt?

**George Haikal:** Yes.

**Jon Kowieski:** Know who to reach out to if he requested it?

**Jon Kowieski:** With a BREX laptop, like that should not be an issue.

**Jon Kowieski:** He should already have access.

**Jon Kowieski:** Oh, yeah, yeah, of course.

**Jon Kowieski:** Let me see.

**Jon Kowieski:** I'll try to ping this guy who is the one that gives all the access.

**Jon Kowieski:** J.

**Jon Kowieski:** First cell.

**Jon Kowieski:** Okay.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** I will message him now.

**Jon Kowieski:** And if he can't do it for some reason, I don't know if he can.

**Jon Kowieski:** Kurt might know the admin in Vercel because Kurt probably has the right access.

**Jon Kowieski:** I know if Greg was here, he could probably do it.

**George Haikal:** Great.

**George Haikal:** I just added.

**George Haikal:** I just sent the message in the external channel to get them all.

**Jon Kowieski:** Yeah, because it's someone on the engineering side, probably with some admin.

**Jon Kowieski:** Access to it is really what it is.

**Jon Kowieski:** I don't even have that kind of power up top.

**Jon Kowieski:** So helping someone now having trouble,

**Jon Kowieski:** I mean, after this, then hopefully there's no bottlenecks.

**Jon Kowieski:** Because to be honest, this process that he went through, others have also gone through.

**Jon Kowieski:** It's like hell onboarding people.

**George Haikal:** Yeah, I can't imagine.

**George Haikal:** Hey, I do have a hard stop today, John and Yolanda, so I have to jump.

**Jon Kowieski:** Oh.

**Jon Kowieski:** Are you aware that Yolanda now will be taking over?

**Jon Kowieski:** Did Marcel talk to you?

**George Haikal:** No, no.

**George Haikal:** But we're connecting today.

**George Haikal:** We're connecting today, so.

**Jon Kowieski:** I'm sorry, I thought he did.

**Jon Kowieski:** I. I mean, I'll have one other call, but I'm actually moving on from Bru.

**Jon Kowieski:** Yolanda will be taking over for me.

**Jon Kowieski:** So you'll be communicating with Yolanda from now on.

**Jon Kowieski:** And Alex got it.

**Jon Kowieski:** So.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So everything will be kind of switching up.

**Jon Kowieski:** And I'm sure things when Capital One, the acquisition happens, we'll probably have more compliant um.

**Jon Kowieski:** So yeah, just be aware of that.

**Jon Kowieski:** You can slack me still like access wise.

**Jon Kowieski:** You at least should have all the right access and then any other questions.

**Jon Kowieski:** My last day will be March 10th.

**George Haikal:** Got it.

**Jon Kowieski:** So I will be.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Soon enough.

**Jon Kowieski:** So.

**Jon Kowieski:** But yeah, Yolanda knows a lot of the stuff I do and she can help too.

**Yolanda La:** Not enough.

**Yolanda La:** Just kidding.

**Yolanda La:** We'll get through it, George.

**Yolanda La:** George and I will work through it.

**George Haikal:** We'll get through this together.

**George Haikal:** Sorry to see you go, John, but up.

**George Haikal:** I'm happy for you.

**Jon Kowieski:** Yeah, yeah, yeah.

**Jon Kowieski:** So I should have.

**Jon Kowieski:** I thought you knew.

**Jon Kowieski:** I'm sorry but yeah, if you have any questions, just reach out in the meantime.

**Jon Kowieski:** So I'm trying to make sure everyone has like the right knowledge, access and everything before I leave just so you're prepared.

**Jon Kowieski:** So.

**George Haikal:** But appreciate that.

**Jon Kowieski:** Good, good chatting.

**Jon Kowieski:** And yeah, next week, if you have any other questions, just let me know.

**Jon Kowieski:** Super.

**George Haikal:** Likewise.

**George Haikal:** Likewise.

**George Haikal:** Appreciate it.

**George Haikal:** We'll be in touch soon.

**Jon Kowieski:** Awesome.

**Jon Kowieski:** Have a good one.

**George Haikal:** Amazing talk to you.

**Jon Kowieski:** Bye.
