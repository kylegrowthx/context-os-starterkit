# Brex <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-19
time: 20:30 UTC
duration: 62 minutes
organizer: team@growthxlabs.com
participants: Jon Kowieski (Brex), George Haikal (GrowthX), Marcel Santilli (GrowthX), Aida Knezevic (GrowthX)
fathom_recording_id: 123871693
fathom_url: https://fathom.video/calls/571614029
share_url: https://fathom.video/share/WsS6CWrYd_Bh7FNGXfnsWcTQvTLQ2poE
source: fathom
enriched_on: 2026-02-27T14:30:00Z
</metadata>

---

## Summary

Jon (Brex) and George (GrowthX) reviewed design feedback on the Resources hub from Bongo (Brex CDO), scoped a migration of Pry.co to Sanity for high-velocity content publishing, and aligned on three blocking items: justification document for design approval, Pry.co admin access, and Kirkland's laptop shipment.

---

## Context

Brex and GrowthX are executing a strategic engagement around content marketing and AI visibility. The Resources hub is a key content surface for Brex; Bongo (CDO) is the final approval authority on design changes. Separately, Brex acquired Discover (giving them access to Brex + Capital One + Discover credit card positions), creating new competitive positioning opportunities that Jon wants to explore through rapid content publishing on Pry.co. A team member (Kirkland) is awaiting laptop access, which is blocking contributor onboarding. GrowthX's scope includes design approval advocacy, prototype iteration, and evaluating the Pry.co migration as either a scope trade or a separate engagement.

---

## Relevance

- **Design & UX:** Resources hub redesign approval strategy; use of competitor examples (Ramp, Nike, Apple) to justify functional improvements.
- **Content Strategy:** Plan to migrate Pry.co to Sanity for rapid publishing; positioning around Brex's expanded credit card portfolio post-Discover acquisition.
- **Product & Tools:** Scope clarification on tool page CTAs and SEO URL structure; persona-specific directories (CFO directory) as high-value content play.
- **Engagement Operations:** Blocking items resolved (Kirkland's access, Pry.co admin access, design justification); scope decision on Pry.co (trade vs. separate project).
- **AI Visibility:** Free workspace access for Jon (Brex) to explore AI visibility tool; potential integration with Brex's competitive differentiation strategy.

---

## Overview

- **Design Approval Strategy:** The Chief Design Officer (Bongo) approved the redesign's functional SEO/UX improvements (tagging, CTAs) but rejected visual changes, preferring the current layout. The strategy is to create a detailed doc justifying the changes with data and competitor examples (Ramp, Nike, Apple) to secure approval.
- **Pry.co Migration:** Jon wants to migrate Pry.co to Sanity to create a high-velocity content hub, enabling rapid publishing (est. 50 articles in 2–3 weeks). GrowthX will scope the migration as both a scope-swap and a separate project.
- **Access Unblocked:** Kirkland's access is unblocked. Jon will ship a laptop today or tomorrow, resolving a major bottleneck that has stalled progress.

---

## Key Topics

### Resources Hub Redesign Feedback

  - **Feedback:** Bongo approved functional changes but rejected visual ones, preferring the current layout.
      - **Approved:** Tagging, new CTAs, new content blocks (author, date, read time).
      - **Rejected:** New visual design, image sizes, and font styles.
  - **Rationale:** The design was built in Render to enable rapid iteration and feedback before a costly Sanity build.
  - **Specific Edits Required:**
      - **Global Nav:** Make the sub-nav sticky on scroll.
      - **Article Page:** Reduce large font sizes and increase header visibility.
      - **Author Bio:** Add an option to hide the author bio, as Jon is the primary author for "Spend Trends."
      - **Article Topics:** Redesign the post-article topic section for a cleaner look.
      - **Search:** Add a search bar to the hub.
  - **Content Strategy:**
      - **"Latest" Section:** Replace "Spend Trends" content with general Brex articles to align with internal preferences.
      - **"Index" Feature:** Bongo approved the concept of persona-specific directories (e.g., a "CFO directory") as a high-value content play.
      - **URL Structure:** Move all content under `/resources/` (e.g., `/resources/tools/`) to strengthen the hub's SEO authority.

### Pry.co Migration to Sanity

  - **Goal:** Create a high-velocity content hub for rapid publishing.
  - **Blocker:** Jon needs admin access to Pry.co to provide GrowthX with the necessary context for scoping.
  - **Scoping Options:**
    1.  **Scope Swap:** Replace current tool-building work with the migration.
    2.  **Separate Project:** Run the migration as a distinct engagement.

### Admin & Access

  - **Kirkland's Access:** Unblocked. Jon will ship a laptop today or tomorrow.
  - **AI Visibility Tool:** George will add Jon to the Brex workspace for free access.

---

## Action Items

**Jon Kowieski (Brex)**
- Check Sanity location of Resources Index; confirm w/ George
- Schedule review mtg w/ Bongo; include Alex if available
- Send Kirkland shipping address to George; coordinate laptop shipment
- Draft Pry.co project doc (scope, goals, constraints) for George
- Obtain admin access to Pry.co for George and GrowthX

**George Haikal (GrowthX)**
- Fix render font scaling; update Resources render per feedback; share w/ Jon
- Create and share talking-points doc (changes, rationale, examples) w/ Jon
- Add Jon to AI Visibility workspace
- Scope Pry.co migration/hub in 2 ways; share w/ Jon

---

## Transcript
**George Haikal:** This meeting is being recorded.

**George Haikal:** Jon, how's it going?

**Jon Kowieski:** Good, how are you?

**George Haikal:** Good, man.

**George Haikal:** I feel like it's been a while since we've seen each other, no?

**Jon Kowieski:** Yeah.

**Jon Kowieski:** I mean, being out, well, company ride about last week.

**Jon Kowieski:** That's where...

**George Haikal:** How'd that go?

**Jon Kowieski:** It was fun.

**Jon Kowieski:** It's been a while since I've seen everyone at the company in person.

**Jon Kowieski:** We just don't do events like that anymore here.

**Jon Kowieski:** So got to meet some of the Capital One team, too, so that was cool.

**Jon Kowieski:** But yeah, it was definitely fun.

**Jon Kowieski:** I haven't been to Vegas since the last one, so...

**George Haikal:** Oh, it in Vegas?

**Jon Kowieski:** Yeah, I don't even know how they did it.

**Jon Kowieski:** They planned it in three weeks, so...

**George Haikal:** Wow.

**Jon Kowieski:** They just did it crazy fast.

**George Haikal:** So the catalyst was the acquisition, it sounds like.

**George Haikal:** Yeah.

**Jon Kowieski:** There was no plan before that.

**Jon Kowieski:** So I think Capital One was like, yeah, we'd love to get everyone in a room kind of thing and present like why we're better together kind of thing.

**George Haikal:** So we will definitely be having a lot more compliance.

**George Haikal:** Yeah.

**Jon Kowieski:** Yeah, they said that.

**Jon Kowieski:** So, which was like.

**George Haikal:** To be expected.

**Jon Kowieski:** Yeah, we're actually changing things up today even.

**Jon Kowieski:** Like we can't talk about banking in a certain way anymore here.

**George Haikal:** Really?

**Jon Kowieski:** So, yeah, that's essentially it has to follow FINRA guidelines now.

**Jon Kowieski:** So that is something even, yeah, today we're changing.

**George Haikal:** Interesting.

**George Haikal:** What other immediate big changes are coming?

**George Haikal:** Or is it kind of business as usual until they get more integrated?

**Jon Kowieski:** I mean, the acquisition is not final, so no one can answer that question.

**Jon Kowieski:** And if they say they know the answer, they don't know the answer.

**George Haikal:** Do they have a final date or no?

**George Haikal:** Like a target date?

**Jon Kowieski:** No.

**Jon Kowieski:** Most of the company was guessing like 90 days after the announcement.

**Jon Kowieski:** But to be honest, in this administration, I don't think a single acquisition is not gone through.

**Jon Kowieski:** So we'll see.

**Jon Kowieski:** I almost think it could be sooner, but they probably need to do their checks and balances too.

**Jon Kowieski:** But I don't think, I think that will all be fine.

**George Haikal:** Got it.

**George Haikal:** Got it.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** It just might be.

**Jon Kowieski:** But yeah, I spoke to that team, so they're excited.

**George Haikal:** Are you excited?

**Jon Kowieski:** Yeah, I don't know.

**George Haikal:** I'm one of the remotes.

**Jon Kowieski:** I'm remote.

**Jon Kowieski:** And yesterday we were talking through, so I'll bring that up right away.

**Jon Kowieski:** He doesn't want to change the UX or the design.

**Jon Kowieski:** I kind of thought that would happen.

**Jon Kowieski:** But what I mean by that is like the image sizes and things like that.

**Jon Kowieski:** What I did explain to him is how like a lot of these features would be better for SEO.

**Jon Kowieski:** So like the tagging on there, he's like, yeah, that works.

**Jon Kowieski:** The new CTAs, yeah, that works.

**Jon Kowieski:** Adding new blocks and new sections, it works.

**Jon Kowieski:** So author, date, and time to read, yes.

**Jon Kowieski:** So he just did not want to change the, let me see.

**Jon Kowieski:** He didn't want to change the look, I guess, more than anything.

**George Haikal:** But like your download.

**George Haikal:** Can you show me what you mean, sorry?

**George Haikal:** Or if there's a call recording as

**George Haikal:** Well, that'd be helpful, but I just want to make sure we get everything right before we create a new version.

**Jon Kowieski:** Let me share my screen.

**George Haikal:** He wants to keep this style.

**George Haikal:** Oh, no.

**George Haikal:** Really?

**Jon Kowieski:** You got to pick what you can get here.

**Jon Kowieski:** But what he wants, I at least got him to add this.

**George Haikal:** Because this has real value, the tagging, the trends, the categorization.

**Jon Kowieski:** Yeah, like add this, add these new topics, except it has to be in this style.

**Jon Kowieski:** What do you mean it has to be in this style?

**Jon Kowieski:** Image style, I guess, and the text.

**Jon Kowieski:** That's what I mean by it.

**Jon Kowieski:** But, I mean, what you changed on here was like, this is a square.

**Jon Kowieski:** This is somewhat of a rectangle.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So he wanted to keep...

**Jon Kowieski:** He but he liked these, this, there wasn't a lot of change here, I didn't think, but they will probably say keep the fonts as is because it's brand, but he was definitely for adding like the new categories, we don't have an index, I know what you mean there, tools, trending, so adding all these, was like, yeah, that's completely fine.

**Jon Kowieski:** And adding the seal there, I was like, yeah, that makes more sense.

**Jon Kowieski:** So he was fine with that.

**George Haikal:** So most of the changes, I would say, are like compliance-related.

**George Haikal:** What about the global nav?

**Jon Kowieski:** I did bring that up as well.

**George Haikal:** And then, and then these, these breakout of the pages as well, the articles, the books, the case studies, like adding that as the sub nav.

**Jon Kowieski:** Um, so, he didn't go into that, but I can ask him super quick.

**Jon Kowieski:** I don't think he liked it.

**Jon Kowieski:** Um.

**Jon Kowieski:** Let me see the comments super quick.

**Jon Kowieski:** I feel like he made this page, by the way, this original page.

**George Haikal:** Yeah, it sounds like it, yeah.

**Jon Kowieski:** My preference would be to keep the existing layout system and structure kind of thing.

**Jon Kowieski:** And then we add the new data into that.

**Jon Kowieski:** Because I even had to tell him, like, there's stuff from, like, 2024 and 2000, like, early 25 that are on, like, the current page that do not make sense to even have, because we don't do it anymore.

**Jon Kowieski:** So I might have to have a meeting with him, like, just one-on-one.

**George Haikal:** Yeah, we're happy to, yeah, I mean, you have your one-on-one too, but we're also happy to meet if needed, like, if it'd be helpful.

**Jon Kowieski:** Yeah, I just know what to expect, because yet again, you saw what we actually got approved by the last CMO and, like, three...

**Jon Kowieski:** People before it got even sent to him.

**Jon Kowieski:** So then basically none of the changes were implemented yet.

**Jon Kowieski:** So I don't want this.

**Jon Kowieski:** I'm trying to like take what I can get.

**Jon Kowieski:** And like, I understand everything.

**Jon Kowieski:** I understand the value of that navigation as well.

**Jon Kowieski:** And this just makes it a lot easier.

**Jon Kowieski:** For some reason, he did want to see it in Sanity.

**Jon Kowieski:** And I was like, that would take them an extreme amount of time if we don't know if it's like final.

**Jon Kowieski:** Yeah, yeah.

**Jon Kowieski:** So I let him know that too.

**George Haikal:** Appreciate that.

**Jon Kowieski:** So honestly, I didn't see like tremendous changes, but I understood from the navigation point.

**Jon Kowieski:** I think what he didn't like is the fact the main navigation disappeared.

**Jon Kowieski:** And what then happened was this navigation.

**George Haikal:** What do you mean when you scroll?

**Jon Kowieski:** Yeah.

**George Haikal:** Yeah, that should all be sticky.

**George Haikal:** I mean, it's just on Render for now.

**George Haikal:** So it's just not rendering through.

**George Haikal:** But like, you can see it.

**George Haikal:** The intention.

**George Haikal:** The key thing is for it to stay sticky on scroll.

**Jon Kowieski:** And if that's the case, I can speak through that.

**Jon Kowieski:** So, but yeah.

**Jon Kowieski:** And even what's below here, no one's clicking that.

**Jon Kowieski:** I understand UX very well.

**Jon Kowieski:** This font size is too small.

**Jon Kowieski:** Like this actually, no one's listening to it.

**Jon Kowieski:** But I do think there is someone else that might be improving it.

**Jon Kowieski:** And they might be right there.

**Jon Kowieski:** They meet like bi-weekly, I think.

**Jon Kowieski:** So got a feeling that might be the case as well.

**Jon Kowieski:** So, but I'm going to speak to him again.

**Jon Kowieski:** And like, this is just awful for, I don't know, visibility in my opinion.

**Jon Kowieski:** Like, this is way too small.

**Jon Kowieski:** And like what you guys did, I agree with.

**George Haikal:** Like.

**George Haikal:** I agree with this.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Like, I want to see it, and I want to, like, be, I want to easily read it.

**Jon Kowieski:** So, I don't know why that, he didn't like that.

**George Haikal:** And then when you hover, so when you're on the global nav, when you hover over resources, on both, right?

**George Haikal:** So on this one, if you scroll up all the way, and then hover over resources.

**George Haikal:** Yeah, without clicking, sorry.

**George Haikal:** Yeah, just without clicking.

**George Haikal:** You can see this was reorganized as well.

**George Haikal:** And so I'm going look at this compared to, so we pulled in, we basically organized all the different topics, right, that we laid out on this page.

**George Haikal:** On the left side, I'm going to discover, articles, case studies, reports, the index, and then tools, and topics as well.

**George Haikal:** It's much cleaner.

**George Haikal:** And then there's the customer hub still as well.

**George Haikal:** And we can pull in case studies up into the customer hub.

**George Haikal:** And then the right panel is, sorry, we already have case studies on discover.

**George Haikal:** But then the right panel is latest as well, surfacing the latest content.

**George Haikal:** Nuclearlicht, And

**George Haikal:** So if you look at this compared to the existing experience when you hover.

**Jon Kowieski:** Yeah, this is terrible.

**George Haikal:** Yeah.

**Jon Kowieski:** Yeah, I've been waiting to pick this battle because I just needed proof.

**Jon Kowieski:** I needed proof like this is why this should be here.

**Jon Kowieski:** AKA these pages should be linked in the top nav.

**Jon Kowieski:** I like this, so I can definitely, I didn't know this, but I'll try to fight for this for sure, because there's actually a tremendous amount of value for technical reasons.

**Jon Kowieski:** So, but that makes sense.

**Jon Kowieski:** This stuff, I'll see what they say.

**Jon Kowieski:** Sometimes I'll just tell you, spend friends, they don't fight.

**Jon Kowieski:** Like, that's what brings in an enormous amount of traffic.

**Jon Kowieski:** Good traffic.

**Jon Kowieski:** So.

**George Haikal:** Yeah.

**George Haikal:** And, and.

**George Haikal:** Did you have time to go into the actual article experience as well?

**George Haikal:** So can you click into one of the articles?

**Jon Kowieski:** I did not know that was...

**George Haikal:** We did a lot, Jon.

**George Haikal:** I told you, we did a lot.

**Jon Kowieski:** Anything in Spend Trends, we should not need approval, by the way.

**Jon Kowieski:** Oh, that's right.

**Jon Kowieski:** This is pretty big.

**Jon Kowieski:** Header size is the famous font size.

**Jon Kowieski:** Oh, yeah, they might eat this.

**Jon Kowieski:** We might not be happy to see this, just because I don't.

**Jon Kowieski:** I'll just say the font size might be a little too big.

**George Haikal:** Got it.

**Jon Kowieski:** Headers, though, I can't even see.

**Jon Kowieski:** But you can't tell what's a header and what's not a header, so that would be a direct issue.

**George Haikal:** Yeah.

**George Haikal:** And then if you click articles, so heard you on that.

**George Haikal:** If you click articles, articles, you articles,

**Jon Kowieski:** Ugh.

**Jon Kowieski:** I like it.

**Jon Kowieski:** I like it a lot.

**Jon Kowieski:** I don't think I should have an issue with this, but I'll have to check.

**Jon Kowieski:** They're just going to ask how much work is this all going to take to create?

**Jon Kowieski:** I already know that.

**Jon Kowieski:** It's like one of his questions because what was the first thing he said?

**Jon Kowieski:** Why would we redesign the whole system?

**Jon Kowieski:** Why just not like make changes to existing pages?

**Jon Kowieski:** So that was one of his questions to me.

**George Haikal:** We can help with answers as well.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** I mean, even on the render platform, one of his questions, why is this being built outside the core system?

**Jon Kowieski:** And I was like, well, it's easier to build it and render instead of like building an insanity.

**Jon Kowieski:** So before we even do the build, we need to make sure it's approved by you.

**George Haikal:** Yeah.

**George Haikal:** It's uncomparable.

**George Haikal:** Easier to make edits and adjust and render like it's just to be nimble and so we can get all the right feedback and then we can pull in all the work.

**Jon Kowieski:** Yeah, he's very much just trying to understand why this is being built as a completely separate thing versus just making those additions in the current system and build that build off of what we have.

**Jon Kowieski:** That's what he said.

**George Haikal:** Where does he feel like it's a complete rip and replace besides the resources hero section?

**George Haikal:** Because basically what we're doing is enriching and improving the overall experience within the constraints of what you already have.

**George Haikal:** Like the global nav is still resources.

**George Haikal:** We're just adding and servicing the right content and organizing it better.

**George Haikal:** Same with articles by role and by topic.

**George Haikal:** They're better organized.

**George Haikal:** I'm pulling in case studies.

**George Haikal:** He's, um...

**George Haikal:** Below on the resources, I'm just curious, is there anything that's particularly standing out as like, well, this is completely off?

**Jon Kowieski:** I don't think he knew that this was up here and in a different way.

**George Haikal:** I think he was just looking at that specific resource pages.

**Jon Kowieski:** Granted, this, I don't think we should have a problem with getting through at all because it's a nightmare.

**Jon Kowieski:** The index, this one actually confused me.

**Jon Kowieski:** Like, what is this?

**George Haikal:** Yeah, so we're going to build, as a player, we're going to build indexes as well, which think of them as like interactive tools, but directories, enriched directories and databases that are tailored to your personas.

**George Haikal:** So like a CFO directory is an example.

**George Haikal:** We're still fleshing it out, but it's essentially, we're all the CFOs, the companies they work for, what the companies do.

**George Haikal:** So like, it's still a content play, but it's more of a differentiated interactive experience.

**George Haikal:** Like those, I think, can be huge.

**Jon Kowieski:** I agree with that.

**Jon Kowieski:** If you're a CFO and you want to see all the other CFOs, that's actually a super valuable page.

**George Haikal:** Yeah, but even if you look up any company, right, then this could come up with their CFO tag as well.

**George Haikal:** And then we'll get in Richard with like all the relevant topics or answers to the questions that we're already trying to target here.

**Jon Kowieski:** So this page should be completely fine.

**Jon Kowieski:** I think this is actually Insanity.

**Jon Kowieski:** Like the ability, I believe it's under Resources, but we will have to check.

**Jon Kowieski:** If it's not, like that's something we need to, I'll have to check after this meeting and see exactly where it is.

**George Haikal:** Because then the idea here is, right, then you have all these tags.

**George Haikal:** And if you see, even for tools, right, they all have a persona tag as well.

**George Haikal:** And so there's going to be a place where any, the persona tag, you can go to finance manager.

**George Haikal:** And agnostic of the actual content type, everything related to a finance manager, you'll be able to see whether it's case studies you're surfacing that are related, whether it's tools, whether it's articles.

**George Haikal:** So it's another way to connect everything.

**Jon Kowieski:** So, yeah, how we built it out already, and I guess since we only did it with this, is slash tools, technically resources is not in it.

**George Haikal:** But I don't know how that would, I'm trying to think, like.

**George Haikal:** We can move everything over very quickly.

**George Haikal:** I think because Kirkland's already plugged into everything.

**George Haikal:** I don't think that's much of an issue.

**George Haikal:** Yeah.

**George Haikal:** And I think it makes sense for everything to come off slash resources, right?

**George Haikal:** Unless there's an issue in your mind with having slash resources slash tools versus just slash tools.

**Jon Kowieski:** I guess the only issue that could actually pop up is, like, page like this, actually.

**Jon Kowieski:** The URL.

**Jon Kowieski:** URL.

**Jon Kowieski:** The URL.

**Jon Kowieski:** And that will actually come up with some other stuff that you're working on.

**Jon Kowieski:** The URL string is just going to be huge, but that's not the case for everything.

**Jon Kowieski:** It's just like this one and the per diem one that we have you working on, but this stuff technically won't have that issue.

**Jon Kowieski:** So that's the only thing I'm thinking through.

**Jon Kowieski:** I mean, but technically you could do like tools, resource, gosh, I mean, you even have the topic.

**George Haikal:** Yeah, yeah, yeah.

**Jon Kowieski:** Technically it could be like, it doesn't have to be resources, but tools slash topic slash whatever, which could be helpful.

**Jon Kowieski:** And the reason why that would be helpful is if I'm looking for an interactive calculator or something, but nevermind.

**Jon Kowieski:** I'm like thinking through this way too fast.

**George Haikal:** That works for us.

**George Haikal:** I don't know.

**George Haikal:** It's helpful, though.

**George Haikal:** It's helpful to think through all the experience.

**Jon Kowieski:** That would help for templates, I guess.

**Jon Kowieski:** But this is actually one area, the template section itself, that I was thinking would be built out almost in a separate area, where it's like templates slash topic slash.

**Jon Kowieski:** Yeah, that is one.

**Jon Kowieski:** I'm fine with this page, though.

**Jon Kowieski:** I'm fine with all of these.

**Jon Kowieski:** He didn't realize this.

**Jon Kowieski:** He's just going to question.

**Jon Kowieski:** Is this following our brand fonts?

**Jon Kowieski:** Is that the only thing?

**Jon Kowieski:** I'll get a meeting with him and try to talk him through it, I think.

**Jon Kowieski:** Because I think his concern is we're just going to spend too much time on this stuff.

**Jon Kowieski:** Granted, I would like to.

**George Haikal:** It's completely worth it for the foundation that we want to build there, in my opinion.

**Jon Kowieski:** I just need to understand.

**Jon Kowieski:** Because I was going to offer you a render too.

**Jon Kowieski:** But then he's going to be like, why am I even seeing this?

**Jon Kowieski:** So keep that in mind.

**Jon Kowieski:** If it's possible to get this render and make this navigation stick, that would be very helpful.

**Jon Kowieski:** He's basically someone where he expects to see what is final, almost, when it gets to him.

**George Haikal:** So I'm just not trying to have the other directors under him see this, because then we'll add three to four other layers.

**Jon Kowieski:** But the resources, I've just been waiting to fight for this.

**Jon Kowieski:** And I'll have to fight for this and get Alex into that too.

**Jon Kowieski:** And say this is for internal linking and SEO and technical SEO.

**Jon Kowieski:** That should be a good enough explanation.

**Jon Kowieski:** The only thing they may not like is this.

**George Haikal:** Which is fun.

**George Haikal:** I'm like, yeah, it's also so easy to remove or edit anything that you see right now.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** The one thing is they might want this.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Showing from, like, the blog, like, whatever is here.

**Jon Kowieski:** So that is probably the one thing I think off the top of my head that they would want.

**Jon Kowieski:** I think everything else was, like...

**George Haikal:** That they would want removed, or...?

**Jon Kowieski:** I think adding the blog articles here would work.

**George Haikal:** Oh, adding the blog articles, okay.

**Jon Kowieski:** Yeah, like, if you look at the latest now, it's selected.

**Jon Kowieski:** So they might actually just want this.

**Jon Kowieski:** I know we want to highlight this one clearly like crazy.

**Jon Kowieski:** Mm For good reason, but they don't like to highlight Spendtron.

**George Haikal:** Mm-hmm.

**Jon Kowieski:** So...

**George Haikal:** We can add the Brex article there under the latest.

**Jon Kowieski:** Yeah, it's probably what he's going to prefer.

**Jon Kowieski:** So...

**Jon Kowieski:** Though I would absolutely love if it was Spendtron.

**Jon Kowieski:** Um...

**Jon Kowieski:** It's all good.

**Jon Kowieski:** Um, but too many people on that team will not be available.

**Jon Kowieski:** And this might be the other thing.

**Jon Kowieski:** Like you can see, he wants certain sections probably highlighted.

**Jon Kowieski:** And that's crazy.

**Jon Kowieski:** I'll talk to Alex about this too.

**Jon Kowieski:** But I don't think he wants any spend trends actually in that main net.

**George Haikal:** So we can, I mean, we can keep it to say articles, we can keep it to say the original three.

**Jon Kowieski:** Yeah.

**George Haikal:** Articles, Brex, Brex, benchmarks, and e-books.

**Jon Kowieski:** I think if I was Insanity, I think these are selected manually.

**Jon Kowieski:** I think.

**Jon Kowieski:** So they have to be.

**Jon Kowieski:** E-book wise, like, I don't even know who's going to write e-books here anymore.

**Jon Kowieski:** The person that was is no longer here.

**Jon Kowieski:** And he's gone in December.

**Jon Kowieski:** So.

**Jon Kowieski:** Like, I'm gonna have to have a conversation even about that.

**Jon Kowieski:** Like, there's just a lot of stuff that one person did.

**Jon Kowieski:** He's no longer here.

**Jon Kowieski:** So, a lot of this stuff is just old.

**Jon Kowieski:** Like, this just kills me.

**George Haikal:** Yeah, yeah.

**George Haikal:** So, why are we highlighting stuff like this?

**Jon Kowieski:** And I know this is probably from 2024 as well.

**George Haikal:** Yeah.

**Jon Kowieski:** So, but this is kind of actually what happened the last time we tried this.

**Jon Kowieski:** So, and, yeah, that's just the personal preference.

**Jon Kowieski:** So, just keep that in mind.

**George Haikal:** Got it.

**George Haikal:** So, I'll make those edits and then articles.

**George Haikal:** We'll reduce the font size and we'll make the headers more visible.

**George Haikal:** Obviously, like, when they're actually saying it, like, it would, that would not be a mistake we're gonna make.

**George Haikal:** This is just a render instance.

**George Haikal:** Yeah.

**George Haikal:** Yeah.

**George Haikal:** Yeah.

**George Haikal:** Outside of that and what we just talked about, any other glaring edits before you want to show?

**George Haikal:** And again, happy to bring in, happy to all meet as well because I know we just want to make sure that you're set up for success, right?

**George Haikal:** And this, I think, is a good point.

**George Haikal:** We'll make these edits, but I think there's very good rationale behind every one of these moves.

**Jon Kowieski:** Yeah, so it's not possible to meet with him this week.

**Jon Kowieski:** He's fully booked.

**Jon Kowieski:** Gosh, let me see if next week.

**George Haikal:** Because we can even pull in Marcel and Alex, too, if it's worth it.

**Jon Kowieski:** Alex thinks.

**Jon Kowieski:** I'll tell you, he's the chief design officer, and he basically determines what is on the website and where it is.

**George Haikal:** So if I had the ability to do certain things, they would have already been done, like much of what you mentioned.

**Jon Kowieski:** I've been thinking about over a year and a half, but it probably helps when someone from the outside comes in.

**George Haikal:** I was going to say, yeah, it definitely helps if it's someone external, right?

**George Haikal:** Because then there's no, nothing ever negatively impacts you, right?

**George Haikal:** But external recommendations and advice could always help.

**Jon Kowieski:** Oh man, I hope he's not.

**Jon Kowieski:** Maybe on Tuesday, Alex will not be able to join because Alex will be in LA now.

**Jon Kowieski:** He should be at our, our SKO is now Monday through Wednesday in LA.

**Jon Kowieski:** So there's no way he's gonna, I'm pretty sure he's in LA, but he should be.

**George Haikal:** Maybe, yeah, maybe we can ping Alex to like, also.

**George Haikal:** So, um...

**George Haikal:** Thanks for letting me know.

**George Haikal:** Backchannel Bongo if needed.

**George Haikal:** I just think the more effort, the better here.

**George Haikal:** If it's not going to negatively impact anything.

**George Haikal:** at the very least, meeting them Tuesday would be amazing.

**Jon Kowieski:** I'm going to Slack Bongo and see what we can do.

**Jon Kowieski:** So right now, it seems as though his calendar isn't too crazy for next week after Tuesday.

**Jon Kowieski:** At the same time, he should not be at SKO, but that would really suck.

**Jon Kowieski:** That could actually be something.

**Jon Kowieski:** So I guess outside of this, the one thing too is Kirkland.

**Jon Kowieski:** We can definitely send him a laptop and he can get shipped today or at the latest tomorrow morning.

**Jon Kowieski:** Which I think would give him basically full access.

**Jon Kowieski:** So yeah, I just think there's a dress and then that's...

**Jon Kowieski:** he doesn't snowboard.

**Jon Kowieski:** But yeah, so when that happens, if they're both out, what can we do?

**Jon Kowieski:** Nothing.

**Jon Kowieski:** So I don't want to run into that.

**Jon Kowieski:** So, or something else happens and they both like can't do anything.

**George Haikal:** So yeah, if you give me his address, I'll send that over to my team.

**Jon Kowieski:** But is there anything else that you wanted to go over?

**George Haikal:** I think this was the most important, right?

**George Haikal:** Because we just want to unblock the design here.

**George Haikal:** So it was actually really good getting your feedback from Bongo.

**George Haikal:** I keep calling him Bongo.

**George Haikal:** Sorry, Bongo.

**Jon Kowieski:** Don't say that to him.

**Jon Kowieski:** Nothing will get approved.

**George Haikal:** Immediately ends the call.

**Jon Kowieski:** Is that going say Bongo?

**Jon Kowieski:** He would.

**George Haikal:** That was very helpful.

**George Haikal:** I think if we can meet next week, that'd be great.

**George Haikal:** And in the interim, we'll make the edits on our end to this render instance to make it look really possible.

**George Haikal:** I appreciate that.

**George Haikal:** That's helpful.

**Jon Kowieski:** Give me that, and maybe that's a shared document, and I can share it with him, and then he will actually probably give his feedback within the document itself.

**George Haikal:** Nice.

**Jon Kowieski:** Then we can kind of go back and forth there.

**Jon Kowieski:** And I at least can fight for, like, I mean, I like everything.

**Jon Kowieski:** Then what you think he cares about most?

**George Haikal:** So, like, in terms of talking points, I can speak to the importance, we can speak to the importance of, like, the entirety of the experience from GlobalNav, why we're servicing what we're servicing, down to the resources hub?

**Jon Kowieski:** Yeah, that's a good question.

**Jon Kowieski:** With him, because he's the chief design officer.

**George Haikal:** Yes.

**Jon Kowieski:** I think it has a lot to do with, like, the look and UX.

**Jon Kowieski:** He essentially likes it as is, and doesn't want to change it that much.

**Jon Kowieski:** The crazy thing, though, is sometimes at this company, if you really want to get something across the finish line, you kind of do a compare and contrast of what Ramp is doing.

**Jon Kowieski:** I would not suggest you guys do that, but that might be something I have to think through.

**Jon Kowieski:** Like, hey, look at what Ramp is doing.

**Jon Kowieski:** It's clearly working for blah, blah, blah.

**Jon Kowieski:** Sometimes that actually helps me get things across the line, as bad as it is, and I hate doing that, but that's one thing that maybe, and maybe he thinks it looks a little bit like Ramp.

**Jon Kowieski:** I would not doubt that he actually made a comparison.

**Jon Kowieski:** Granted, it doesn't really look like Ramp.

**George Haikal:** No, I mean, we made sure to make it differentiated, but I mean, there's like standard best practice stuff, like the hero section.

**George Haikal:** Having the articles like big and read.

**Jon Kowieski:** He might be actually comparing it to this.

**Jon Kowieski:** I didn't think about that.

**Jon Kowieski:** So this would actually be, I do love the look of this, but he would never approve it.

**Jon Kowieski:** Like, I like that a lot, actually.

**Jon Kowieski:** So that would never go through.

**Jon Kowieski:** But in terms of, like, God, I wonder if this looks great.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Load more, perfect.

**Jon Kowieski:** Page one, page two.

**Jon Kowieski:** And this is all organized.

**George Haikal:** Yeah.

**George Haikal:** And will be, like, when we actually go to the finish line on it, too.

**George Haikal:** And start building.

**George Haikal:** All of this will be organized, tagged by topic, by role.

**George Haikal:** And then you see on the right in the sub-nab, there will also be drop-downs for role and for topics.

**George Haikal:** So you'll be able to view all content.

**George Haikal:** next time.

**George Haikal:** I'll

**Jon Kowieski:** On my side, sorry.

**Jon Kowieski:** But that should be good.

**Jon Kowieski:** This I actually got to really think through.

**Jon Kowieski:** So you want to do resources slash tools slash.

**Jon Kowieski:** Yeah, that should be fine.

**Jon Kowieski:** We just have the instances.

**Jon Kowieski:** will be two instances where the URL is like very, very long, but no one's going to.

**George Haikal:** I think that tradeoff is worth it, though.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** It'll make the resources page incredibly strong by doing that, I guess.

**George Haikal:** Mm-hmm.

**Jon Kowieski:** So technically it would make this page strong.

**Jon Kowieski:** But this title could actually.

**Jon Kowieski:** Yeah, I got to think through it.

**Jon Kowieski:** The title itself, if it was something else, could actually have the power to rank.

**Jon Kowieski:** So tools for the fastest growing companies.

**Jon Kowieski:** Yeah, yeah, yeah.

**Jon Kowieski:** Finance tools.

**Jon Kowieski:** Well, if they're all finance-related, yeah, technically that would actually work.

**Jon Kowieski:** So let's say someone searches finance tools.

**Jon Kowieski:** If all these pages were powerful enough and I put all my work into them outside of what you guys are doing, yeah, that could actually work.

**Jon Kowieski:** Yeah, that's fine.

**Jon Kowieski:** But yeah, that's kind of everything on my end for this, for the index.

**Jon Kowieski:** It would be cool just to, I guess these are good examples.

**Jon Kowieski:** The best finance tools, I don't know, because that could be an article, but if you showed, there's no way you have, okay, maybe.

**George Haikal:** No, no, yeah, these tools aren't built out yet.

**Jon Kowieski:** And then, yeah, the font size, the header size.

**George Haikal:** Yep, that'll be changed.

**Jon Kowieski:** Because it's so big, it's actually extremely hard to read, I would say.

**Jon Kowieski:** Our articles, I think I've pulled you the pattern.

**Jon Kowieski:** What size screen are you on, by the way?

**Jon Kowieski:** much again.

**Jon Kowieski:** Thank

**Jon Kowieski:** Oh, I'm on a 32.

**George Haikal:** Yeah.

**Jon Kowieski:** But, okay, maybe that is a little different.

**Jon Kowieski:** So, and then if it got moved into, okay, I guess that does look different.

**George Haikal:** It's just when you're on a larger screen for some reason.

**George Haikal:** 32 inch.

**Jon Kowieski:** Well, no, now it's actually, the font is different.

**Jon Kowieski:** So that's actually weird.

**Jon Kowieski:** It's just when it's loading on my screen.

**Jon Kowieski:** So now it actually looks way different, even though we're on the same page.

**Jon Kowieski:** So maybe that has something to do with the render itself.

**Jon Kowieski:** See what I mean?

**George Haikal:** I do see what you mean.

**Jon Kowieski:** So if you went like this, and then you went like this.

**George Haikal:** So this is mobile view.

**George Haikal:** So the first view you just showed me is mobile view, correct?

**Jon Kowieski:** This is mobile.

**Jon Kowieski:** How it should look.

**George Haikal:** That looks good.

**Jon Kowieski:** That

**Jon Kowieski:** Yeah, it makes sense.

**Jon Kowieski:** I think it's the rendering program is what's going on.

**Jon Kowieski:** Yeah.

**George Haikal:** But this looks good, no?

**Jon Kowieski:** And this is what it should look like, for sure.

**George Haikal:** Yes, yeah, yeah, yeah.

**Jon Kowieski:** So there's something going on, I think, just with the rendering software, most likely, I think, is what it is.

**Jon Kowieski:** And then if you make it too big, all of sudden this font changes to this font.

**George Haikal:** Yeah.

**Jon Kowieski:** That's what's going on.

**Jon Kowieski:** Which we wouldn't want happening, even if someone...

**George Haikal:** Yeah, I mean, it would never happen outside of this render instance, right?

**George Haikal:** Because this is like a test environment to display things.

**George Haikal:** But I can try to fix that as well.

**Jon Kowieski:** Let's just do this, and I'll beg for forgiveness.

**Jon Kowieski:** Screw it.

**Jon Kowieski:** So I don't think there should be a problem there.

**Jon Kowieski:** This is a new section of the website I want.

**Jon Kowieski:** So, and if that's what these pages will look like...

**Jon Kowieski:** ahead.

**Jon Kowieski:** Uh, we're not building anything new.

**Jon Kowieski:** I don't know.

**Jon Kowieski:** New for other sections of the website.

**Jon Kowieski:** I was already doing this anyway with you guys, so I can say, hey, it's just adding a better user experience.

**Jon Kowieski:** So, yeah, that should work.

**Jon Kowieski:** I think this should be perfectly fine.

**Jon Kowieski:** Um, it'd be great if I had the option for the author, if they, if we had the option for them not to have a bio.

**Jon Kowieski:** Like, I can tell you right now, the author of basically almost all spend trends is me.

**Jon Kowieski:** Um, so I was thinking through that.

**Jon Kowieski:** Uh, in the future.

**George Haikal:** Sorry, you broke up a bit.

**George Haikal:** I heard, um, it'd be great if we have the option for, and then you broke up.

**Jon Kowieski:** Not to have a bio for the author.

**George Haikal:** For it to be.

**George Haikal:** a bio.

**Jon Kowieski:** Do you have an author?

**Jon Kowieski:** Like, if you just clicked on and off or something like that.

**Jon Kowieski:** Otherwise, this team is going to have capacity.

**Jon Kowieski:** Problems, I think, in the future.

**Jon Kowieski:** Granted, probably one of the only authors here will probably have like two authors.

**Jon Kowieski:** You and someone else, right?

**Jon Kowieski:** Yeah, that's the crazy part.

**George Haikal:** You and Brex, Team.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** So we asked, like, I got LT together at one point.

**Jon Kowieski:** was like, what articles would you be fine with?

**Jon Kowieski:** And honestly, like, most of them didn't want to be authors.

**Jon Kowieski:** And I'm like, that's fine with me.

**Jon Kowieski:** Like, I generally don't care.

**Jon Kowieski:** So, but yeah, that will be the instance.

**Jon Kowieski:** So this, we'll just have to say, is the rendering software.

**Jon Kowieski:** But it actually looks good when it looks normal.

**Jon Kowieski:** So I can tell this is a little bigger.

**Jon Kowieski:** I'll have to look into the other font sizes.

**Jon Kowieski:** I'm going to have two directors of design try to make comments, most likely.

**George Haikal:** Mm-hmm.

**Jon Kowieski:** Because Because of

**George Haikal:** Yeah, it's more so like so when they're done reading an article, they're interested in that article type and the topic of anything within that article like got them thinking about something else that they want to explore, then they'd have that option to go into that topic category right after before they're in the actual recommended specific piece of content.

**George Haikal:** Not married to it, though, but that was the thought process behind it.

**Jon Kowieski:** I'm going to go to...

**George Haikal:** Not married to it.

**Jon Kowieski:** Yeah, just looks kind of goofy with the rest of the page.

**Jon Kowieski:** If you like look at everything else, I'd say I just kind of wonder like, what's this doing here?

**Jon Kowieski:** If that makes sense.

**Jon Kowieski:** Granted, I wonder.

**George Haikal:** I even think we could do it under, we can make it look cleaner.

**George Haikal:** Yeah, it's either under related or cleaner where it's topics and the topic serves in a line right to the right of it.

**George Haikal:** And it takes up much less space.

**George Haikal:** It only takes up one line, basically.

**Jon Kowieski:** I would like to see that, actually.

**Jon Kowieski:** I think that would be super helpful.

**Jon Kowieski:** This, like, I want immediately, so.

**Jon Kowieski:** But, yeah, I like it.

**Jon Kowieski:** I'm clearly not that picky.

**Jon Kowieski:** So.

**Jon Kowieski:** Oh, shoot.

**Jon Kowieski:** I just.

**Jon Kowieski:** But, yeah, so everything here is good.

**Jon Kowieski:** And this is basically the same format across all of these.

**Jon Kowieski:** Google-wise, organization.

**Jon Kowieski:** Everything is super helpful.

**Jon Kowieski:** And then search, would have, because it doesn't exist, I guess that was one thing.

**George Haikal:** Like, how is that going to work with all these?

**George Haikal:** Yeah, we can add search.

**George Haikal:** And, yeah, totally easy.

**Jon Kowieski:** Yeah, that was, like, my.

**Jon Kowieski:** The one thing I was super curious about was actually that ability.

**Jon Kowieski:** Because, technically, you strip that ability away, I think.

**Jon Kowieski:** Yeah, this.

**Jon Kowieski:** So click that.

**George Haikal:** How does this work?

**George Haikal:** I think I've used it before.

**Jon Kowieski:** Yeah, yeah.

**Jon Kowieski:** Just general.

**Jon Kowieski:** The only thing is that I don't think this works very well.

**Jon Kowieski:** I'm just searching for an article.

**Jon Kowieski:** Yeah, none of this has to do with spend management.

**George Haikal:** No.

**Jon Kowieski:** No, no.

**Jon Kowieski:** So it's not really working as is.

**Jon Kowieski:** So the amount of tagging that we would need done is like actually pretty extreme.

**Jon Kowieski:** So keep in mind these, I guess, as well, the current topics.

**Jon Kowieski:** Granted, I think business banking was the only one.

**Jon Kowieski:** I don't know about AI.

**Jon Kowieski:** I don't know what is going to fall into AI, but if that's in here, someone put it in here.

**Jon Kowieski:** So that might be something that we just keep in mind.

**Jon Kowieski:** But So.

**Jon Kowieski:** Yeah.

**Jon Kowieski:** Um, yeah, everything looks good to me.

**Jon Kowieski:** If you could just give me the talking points, give me a whole document on what you did and why you did it.

**Jon Kowieski:** I actually think that will be the possibly the most helpful thing.

**Jon Kowieski:** Even more helpful than just having a meeting with him.

**Jon Kowieski:** So he is just has time to absorb everything.

**George Haikal:** So if you want to even take screenshots and like this is, yeah, we'll make a grant.

**Jon Kowieski:** And I will say, like I said, the compare and contrast, like some reason it works here.

**Jon Kowieski:** And if you know of like a very solid, like company doing some of this stuff, maybe like give some links to those examples or something.

**Jon Kowieski:** I think that helps.

**Jon Kowieski:** So I like to have everything original, but that is one of the things I've learned here that actually helps.

**George Haikal:** And is a ramp.

**George Haikal:** Are Ramp comparisons a no-no, based on what you just said?

**George Haikal:** No.

**George Haikal:** Fine.

**George Haikal:** Sorry, no meaning it's fine, too?

**Jon Kowieski:** Yeah, no, it's fine.

**Jon Kowieski:** At times, I've actually had to compare and contrast Ramp a lot.

**Jon Kowieski:** And I severely, like, hate it.

**Jon Kowieski:** But if it helps me get something across the finish line that will help us, it's like, all right, I gotta do this.

**Jon Kowieski:** Like, so, yeah.

**Jon Kowieski:** And so that, I think, will help quite a bit.

**Jon Kowieski:** But even if you had someone other than Ramp, that might be helpful, too.

**George Haikal:** Yep, yep, yep.

**Jon Kowieski:** I can tell you Nike and Apple are admired quite a bit.

**George Haikal:** Okay.

**Jon Kowieski:** So maybe Capital One will be admired soon.

**Jon Kowieski:** So that would actually be wild if you found some of the same features on their website.

**Jon Kowieski:** Because...

**Jon Kowieski:** Because...

**Jon Kowieski:** ...

**Jon Kowieski:** That is a huge talking point.

**George Haikal:** I like that.

**George Haikal:** I like that.

**Jon Kowieski:** But yeah, I'm very okay with everything you have.

**Jon Kowieski:** And I can actually explain it quite well for technical and a lot of technical, actually.

**Jon Kowieski:** And I've hated this resources page for since the day I started.

**George Haikal:** Well, either way, it sounds like, you know, great progress overall.

**George Haikal:** And we'll make sure to make this talking point stock great.

**George Haikal:** So it's super clear the value that we're, like what we're trying to do, what the value is with examples that we know resonate already with them.

**Jon Kowieski:** That sounds great.

**Jon Kowieski:** And then it might not get out until I see if I can have a delivery.

**Jon Kowieski:** So Kirkland should receive that computer by maybe Saturday or Monday at the latest.

**George Haikal:** Okay.

**Jon Kowieski:** Okay.

**Jon Kowieski:** I think.

**George Haikal:** I appreciate that.

**Jon Kowieski:** It's helpful.

**Jon Kowieski:** will probably get an email about when that's coming.

**Jon Kowieski:** And then.

**Jon Kowieski:** But yeah, that's everything on our end.

**Jon Kowieski:** And if you have any other questions, let me know if there's any more hiccups.

**Jon Kowieski:** The access thing is like my biggest nightmare here.

**George Haikal:** But I think I, I truly think we're on the other side of that now.

**Jon Kowieski:** I think so.

**George Haikal:** Which is great, but was, was big.

**Jon Kowieski:** The person I'm talking to is a contractor for us that like figures this all out for everyone.

**George Haikal:** Really?

**George Haikal:** That's so ironic.

**George Haikal:** Yeah, that's hilarious.

**Jon Kowieski:** Yeah, that is not normal.

**Jon Kowieski:** So, yeah, I'll have to figure that out.

**Jon Kowieski:** But yeah, just ping me.

**George Haikal:** yeah.

**George Haikal:** And...

**George Haikal:** And it's end of the day.

**George Haikal:** get it, man.

**George Haikal:** get it.

**George Haikal:** End of the day, towards the end of the week.

**George Haikal:** Don't worry about it.

**George Haikal:** Totally.

**George Haikal:** Yeah, we'll share learnings as they come.

**George Haikal:** I'm seeing a lot on the AI visibility side as well, which we can talk through next week or just ping me if you have any questions.

**George Haikal:** A lot of really good learnings from experiments that we're running and with us publicly launching, check that as well.

**Jon Kowieski:** Do we have access to your AI visibility?

**Jon Kowieski:** That's right.

**George Haikal:** You will by the end of the week if you don't already.

**George Haikal:** I think we were managing your workspace for you, but we'll add a seat for you and get you set up ASAP.

**Jon Kowieski:** I'll just continue with Google.

**Jon Kowieski:** Check that.

**Jon Kowieski:** If I'm on the wrong website, this will release.

**George Haikal:** No, check that .ai.

**Jon Kowieski:** Yeah, thank God.

**Jon Kowieski:** I was like, if I actually went to a .com and signed up for some random product, this would be a nightmare.

**Jon Kowieski:** Oh, we're not actually signed up.

**Jon Kowieski:** Okay.

**Jon Kowieski:** It's like a free signup, though?

**George Haikal:** Yeah, let me, before you do anything, we'll sign you up on our end because we already have your workspace set up.

**George Haikal:** So let me just add you before you do anything.

**George Haikal:** yeah, it's all included in free for you.

**Jon Kowieski:** Yeah, we're definitely comparing and contrasting still.

**Jon Kowieski:** So granted, I think I said we're turning off of Profound.

**Jon Kowieski:** So Profound is very, very expensive.

**Jon Kowieski:** And we're thinking through some other things right now.

**Jon Kowieski:** I'll say for AI visibility and just trying to figure that out.

**Jon Kowieski:** So, oh, for Pry.co, I guess with all the tools we're working on, what is realistically, when could your team actually get to that?

**George Haikal:** Get to Pry.co?

**Jon Kowieski:** Just stripping that down and like helping us get it into sanity.

**George Haikal:** Yeah, is there any more, is there like a project doc or any more context you have there?

**George Haikal:** I'm here.

**George Haikal:** There

**George Haikal:** On what you want, Don?

**Jon Kowieski:** We can create that if that is what you want.

**George Haikal:** That'd be helpful.

**George Haikal:** Yeah, because then we can scope it out.

**George Haikal:** I'm stripping it down.

**Jon Kowieski:** What I mean is, what is that, CFO desk or whatever the hell that is?

**Jon Kowieski:** The CFO club.

**Jon Kowieski:** Essentially making it somewhat similar to this.

**Jon Kowieski:** I can share my screen.

**Jon Kowieski:** And I generally do not care how it looks.

**Jon Kowieski:** That is not what it's for.

**Jon Kowieski:** But just something like, even what you guys did with this, I was like, yeah.

**Jon Kowieski:** I understand everything you did here.

**Jon Kowieski:** So even this, like in a different way, would be all we want.

**Jon Kowieski:** We're just trying to get a content hub.

**George Haikal:** That's all it is.

**George Haikal:** Yeah, how do we get access to Pride.co right now?

**George Haikal:** Whoa.

**Jon Kowieski:** All

**Jon Kowieski:** Oh, God, I got to figure that out.

**Jon Kowieski:** I don't even know who gave me access.

**Jon Kowieski:** And they didn't give me admin access either.

**Jon Kowieski:** That's the first step, I guess.

**George Haikal:** I feel like the most used word between us in the last month has been access.

**George Haikal:** Like, if you go through a transcript of all our conversations, the most frequently used word.

**Jon Kowieski:** Well, that's where when I first got here, I'm like, who can give me access?

**Jon Kowieski:** No one knew.

**Jon Kowieski:** What the  happened?

**George Haikal:** Yeah.

**Jon Kowieski:** It was Google Tag Manager access.

**Jon Kowieski:** No one knows.

**Jon Kowieski:** That person left?

**Jon Kowieski:** How?

**Jon Kowieski:** Yeah, okay.

**Jon Kowieski:** I'll see what I can do there.

**Jon Kowieski:** I think there's, like, someone from the acquisition that can help, because no one uses the website.

**Jon Kowieski:** Like, so, that is something that's, like, very, very much on my mind, outside of, like, everything else.

**Jon Kowieski:** Okay.

**Jon Kowieski:** That's...

**Jon Kowieski:** Probably one of the number one things.

**Jon Kowieski:** I'm like, did just publish articles now?

**Jon Kowieski:** Like, I could.

**Jon Kowieski:** I hate the CMS, but I just want to move the website over.

**Jon Kowieski:** So Greg was aware of that, but that is a lot of work in itself.

**Jon Kowieski:** And that's kind of what I need to know is, like, in terms of priority, like, how much work would that be compared to the tools?

**George Haikal:** What can we do in one month kind of thing?

**George Haikal:** Yeah.

**Jon Kowieski:** So that is what I'm trying to figure out.

**Jon Kowieski:** So if you could help me figure that out, like, do we have to give up tools for the month or something like that?

**Jon Kowieski:** Then that will help a lot.

**George Haikal:** Basically to trade off the work within the same scope.

**Jon Kowieski:** That's what I'm trying to figure out.

**George Haikal:** Because there's two different worlds.

**George Haikal:** There's, like, phasing it where, again, we're just, like, mixing and matching the scope and the work we're doing within the same scope.

**George Haikal:** Or there's adding pry.co as its own lane.

**George Haikal:** And then running and managing that as its own thing.

**George Haikal:** And then if you're, I think we talked about like a little more control over the content, less layers of review.

**George Haikal:** Like if that's what the play with Pride.co is, given that it already has like pretty good authority and the foundation.

**George Haikal:** While I'm going through this exercise of scoping out effort and time, I'm happy to scope it out in both ways, existing and as a separate engagement.

**Jon Kowieski:** The one thing we really want is just to get it moved over and get it stripped.

**Jon Kowieski:** Like creating content at light speed.

**Jon Kowieski:** I would be able to create probably 50 pieces of content in two to three weeks for that one.

**Jon Kowieski:** Particularly because we'd probably go after some of the same keywords in just different ways.

**Jon Kowieski:** So that one we could do very, very quickly, but we're just doing a lot of AI visibility kind of things But then that's two to three weeks of your time, right?

**George Haikal:** That you're trading off.

**George Haikal:** idea.

**George Haikal:** And you're kind of valuable, man.

**Jon Kowieski:** Well, there's certain keywords that we're trying to think through.

**Jon Kowieski:** I would say the highest priority keywords, we have the ability to influence.

**Jon Kowieski:** And I have the ability to influence quite quickly.

**Jon Kowieski:** So we're trying to think through some other things right now.

**Jon Kowieski:** We just got acquired by Capital One.

**Jon Kowieski:** Technically, we no longer have just one credit card.

**Jon Kowieski:** We now have all Capital One's credit cards.

**Jon Kowieski:** We now have all Discover's credit cards because they acquired Discover.

**Jon Kowieski:** So technically, we have the ability to do something that almost no one else in our space does.

**Jon Kowieski:** So that is one thing that's been on my mind since the acquisition.

**Jon Kowieski:** So that is also something we're thinking through.

**Jon Kowieski:** What if we have three credit cards showing?

**Jon Kowieski:** Ramp does not have the ability to do that.

**Jon Kowieski:** So...

**Jon Kowieski:** But they also have the ability to drastically influence us.

**Jon Kowieski:** And I would say Capital One is not doing well when you actually break down things.

**Jon Kowieski:** So I do need to hop.

**Jon Kowieski:** I need to get a few things done.

**Jon Kowieski:** But we talked through quite a bit.

**George Haikal:** Yeah, feel free to pay me.

**George Haikal:** great progress.

**George Haikal:** Great progress.

**Jon Kowieski:** Especially for priorities and things like that.

**George Haikal:** The tool section, we really, really want built out.

**Jon Kowieski:** But along the way, the other thing we will need help with, is adding these new CTAs that go to the tool pages from certain sections.

**Jon Kowieski:** So if we had the ability to add these CTAs, and I hate to say Ramp, but they have some CTAs where I'm like, I've wanted it.

**Jon Kowieski:** I want that.

**George Haikal:** So at the same time, they don't actually send anything to their tool pages from related content.

**George Haikal:** Yeah.

**Jon Kowieski:** So that's it.

**Jon Kowieski:** So that's it.
