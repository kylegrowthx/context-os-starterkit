# Ed <> Jason Weekly

<metadata>
date: 2025-08-11
time: 15:42 UTC
duration: 27 minutes
organizer: Jason Gong
participants: Edin Abazi, Jason Gong
fathom_recording_id: 79712746
fathom_url: https://fathom.video/calls/377663103
share_url: https://fathom.video/share/11c5v1Vd3xd6B-BxNiSgqKDXCiJC1KjT
source: fathom
enriched_on: 2026-03-03 15:42 UTC
</metadata>

---

## Summary

Jason and Edin from GrowthX aligned on final design refinements for their blog redesign before deploying the new responsive layout. Key focus areas include fixing responsive table and tab styling on mobile, redesigning the table of contents placement, and improving the citations styling. They reviewed design inspiration from OpenAI and Anthropic, and agreed on next priorities: finishing the blog deployment and expanding the Lead Growth Community offering (which has already attracted 6 paying members at $50/year).

---

## Context

Jason Gong and Edin Abazi are GrowthX team members working on a major redesign of GrowthX's blog and technical content platform. They're moving off Webflow to build a custom solution with better component support (tabs, tables, callouts, author sections) inspired by high-quality research blogs like Anthropic's. Edin handles the frontend engineering while Jason oversees the strategic direction and product decisions. This meeting occurred mid-sprint with the redesign nearly ready for deployment, pending final styling touches and review from Nick (likely their design/product lead).

---

## Relevance

**To GrowthX Delivery:**
- Blog redesign is a key product offering and will shape how GrowthX presents technical content to prospects and partners
- Custom components (MDX-based, styled callouts, interactive tables, author sections) align with GrowthX's positioning on design-forward research and technical depth
- Responsive design on mobile is critical — tables and tabs must work across devices without breaking layout
- Inspiration from Anthropic's research site suggests potential for deeper, longer-form technical content (10k+ word articles with custom layouts)

**To GrowthX Business Development:**
- Lead Growth Community already has 6 paying members ($50/year = ~$300 ARR) with minimal marketing — strong product-market signal
- Community offering is currently underdeveloped (members only get the workshop-as-course); expansion of features is top priority post-blog-deployment
- Website and blog redesign must reflect actual community offerings to avoid confusing new prospects

**To CheckThat:**
- Blog redesign will showcase CheckThat as part of GrowthX's technical content strategy
- Custom components and MDX support enable richer content about AI visibility and prompt engineering

---

## Overview

- Blog redesign nearly complete; focus on responsive tables, tab styling, and table of contents placement
- Responsive design challenges: tables need to scroll horizontally on mobile and desktop, tab components need better visual prominence
- New design elements inspired by OpenAI and Anthropic blogs: floating table of contents (hidden by default), author sections, styled components
- Citations should be simple small text, not gray boxes
- 6 members already paying for Lead Growth Community ($50/year) despite limited current offerings
- Post-deployment priorities: expand Lead Growth Community features and update website to match actual offerings

---

## Key Topics

### Blog Redesign Progress

- Responsive design challenges with tables and tab components on mobile vs. desktop
- Table styling: needs to scroll horizontally on mobile due to space constraints; Jason wants tables to bleed outside container on desktop for better visibility
- Tab component styling needs refinement — currently too subtle/hidden, need better visual prominence
- Considering author section at top (inspired by OpenAI's layout) to credit main author and contributors
- Table of contents placement: explored top-of-post, collapsible sidebar, and floating options; leaning toward floating TOC hidden by default, reveals on hover/click
- Font size considerations: slightly smaller for academic feel (like Anthropic's research blog), but larger than that for readability
- Inspiration from Anthropic's research site: custom components, different layouts per article, clean design without sacrificing depth

### UX Improvements

- New "prompt wrapper" component with fixed height and scrolling — Edin wants to reduce container size on mobile because it takes up half the screen and interferes with page scroll
- Citations styled as basic small text rather than in gray boxes (Edin tried 10 different approaches, simpler is better)
- Floating table of contents: hidden by default with small icon peeking from side, reveals on hover/click to avoid clutter on long articles
- Reusable components for consistent styling (callouts, author sections, prompt wrappers, MDX-compatible components)

### Technical Considerations

- Investigating CMS options supporting MDX for rich content creation (e.g., Pages CMS)
- Implementing programmatic table of contents generation to avoid manual updates
- Script placement: reviewing whether to use tag manager or separate scripts (taking cues from Anthropic's approach)

### Lead Growth Community

  - 6 people paid $200/year (discounted to $50) without full feature set
  - Current offering limited to workshop content broken into a course
  - Need to expand community features and align website with actual offerings

---

## Action Items

**Edin Abazi (GrowthX)**
- Reduce prompt wrapper container size on mobile; fix scrolling issues
- Increase table width on mobile; ensure horizontal scrolling
- Adjust tab styling to increase visibility/obviousness (make less subtle)
- Create Markdown-based component for table of contents with styled background
- Prototype floating table of contents; hidden by default, reveals on hover/click

**Jason Gong (GrowthX)**
- Fix footer layout and styling

---

## Transcript
**Jason Gong:** Hey, how's it going?

**Edin Abazi:** How's it going?

**Jason Gong:** Pretty good.

**Jason Gong:** did, um, dropped my kid off at a new daycare today, so it was a little sad.

**Jason Gong:** Yeah, or it's a preschool now, so I guess we, like, kind of graduated the family daycare we were at before.

**Edin Abazi:** Was he sad or?

**Edin Abazi:** He's crying a little bit.

**Edin Abazi:** Is it, like, things I'm getting used to?

**Jason Gong:** Probably, but, I don't know, at least he said that he liked the new daycare, so we'll see.

**Jason Gong:** Hopefully he adjusts fast.

**Jason Gong:** Yeah, I don't know, it'll be fine.

**Edin Abazi:** Yeah.

**Edin Abazi:** How about you?

**Jason Gong:** How's, how are you doing?

**Edin Abazi:** Good, good.

**Edin Abazi:** Just, uh, trying to understand the cries, whether it's, like, a sleep cry or...

**Jason Gong:** Oh, very good.

**Jason Gong:** ...hungry cry, yeah.

**Edin Abazi:** Yeah.

**Edin Abazi:** Trying to understand all the, the whole world.

**Jason Gong:** Got it, cool, I see you already made some changes.

**Jason Gong:** Looks great, honestly.

**Jason Gong:** I think the final one is still deploying.

**Jason Gong:** I still added another one.

**Edin Abazi:** What was it about?

**Edin Abazi:** I forgot.

**Jason Gong:** Like another change request?

**Edin Abazi:** I think you had one about... what was it called?

**Jason Gong:** I don't know about the table maybe being a little wider, but looking at it now, otherwise it looks pretty good.

**Edin Abazi:** Yeah, I think it just deployed.

**Edin Abazi:** So basically I had to make a wide version of the tab group for the section with the columns.

**Edin Abazi:** I made it, let me just double check on my phone. I was having some trouble making it responsive.

**Jason Gong:** Oh, yeah, true.

**Edin Abazi:** Yeah, I think it's fine now on mobile. When was that design made? The one that, like, a person from their team did it?

**Jason Gong:** I think you just sent it this morning.

**Jason Gong:** And basically, like, we've always wanted to, like, move off of Webflow, and that guy's, like, a Webflow dev.

**Jason Gong:** So I just kind of, like, in parallel, just at least get him to help.

**Edin Abazi:** Yeah.

**Jason Gong:** obviously, haven't told him that we're going to move it off of Webflow, but I think he kind of knows.

**Edin Abazi:** So one thing I want to do, I noticed that you want to, I noticed that you did the, you made the prompt wrapper a fixed height and, like, scrollable.

**Jason Gong:** Yeah, that might break something.

**Jason Gong:** But I guess I was trying to just try to make it more parallel, like, the OpenAI guys do it as well.

**Jason Gong:** Well, just so it doesn't get too tall, I guess, was the thing I was trying to solve for.

**Edin Abazi:** Yeah, I just want to make the container a little smaller on mobile because it takes up, like, half the screen.

**Edin Abazi:** And then as the user is scrolling down, they end up scrolling within the prompt box instead of, like, the whole page.

**Jason Gong:** That makes sense.

**Jason Gong:** That's one thing I want to do.

**Edin Abazi:** And I think you made another change where you put one of the lists in a gray background.

**Jason Gong:** Oh, I created a separate thing because I wanted a separate, like, prompt wrapper just because I think, like, semantically it'll confuse them from, like, just like a callout.

**Edin Abazi:** Yeah, the reason why I left it is just because so we don't have duplicate code, but it's, like, the same gray background.

**Jason Gong:** But I want to go back to it because I think it broke the responsiveness.

**Edin Abazi:** Like, it's a little, it goes outside the viewport right now.

**Jason Gong:** Oh, I see.

**Jason Gong:** Oh, wait.

**Edin Abazi:** For the citations at the end, I tried 10 different things.

**Edin Abazi:** It didn't look good. I think we should just leave it as basic small text, like I did at the end.

**Edin Abazi:** Especially in the latest post with the quote at the end, just adding another gray box underneath it just didn't make sense.


**Jason Gong:** I'm going to fix the footer as well.

**Edin Abazi:** The most annoying thing about this has been, like, the responsiveness with the tables and everything.

**Jason Gong:** Yeah, I can see that.

**Edin Abazi:** On mobile, I made them scroll horizontally because there's no other way to showcase tables on mobile.

**Jason Gong:** That seems right.


**Edin Abazi:** I've seen on the output website we did cards instead of a table, but in this case, it wouldn't make sense.

**Jason Gong:** Yeah, I think it should be a table.

**Jason Gong:** Let's see, I'm trying to find one from OpenAI.

**Jason Gong:** Yeah, they also have scrolling tables. I'll put an example in the main channel — shows what OpenAI does.

**Jason Gong:** They don't shy away from making tables wider on desktop.

**Edin Abazi:** The table?

**Jason Gong:** Yeah, basically forcing people to scroll horizontally if needed.

**Jason Gong:** Maybe we could tweak that a bit because right now it looks vertically squished on mobile.

**Edin Abazi:** Yeah, it's basically just a number. Can make it wider on mobile.

**Jason Gong:** Yeah, and then on desktop, I think we should have it bleed outside of the container a little bit.



**Edin Abazi:** Let me just write these down so I don't forget. Yeah, I mean, that tab component, they use a ton.

**Jason Gong:** Yeah, cool. I think we'd probably make the tab versus a pill or something, but I think the tab looks pretty good.

**Edin Abazi:** Yeah, I think it conveys the idea without making the article way too long.

**Jason Gong:** I think it works fine.

**Edin Abazi:** I'll play around with styling a little more. So what's the plan? Like when is this going live?

**Jason Gong:** I'm waiting for that thread.

**Jason Gong:** But I think the forcing function here was like, they wanted to do a post on GPT-5.

**Edin Abazi:** So.

**Jason Gong:** I'm waiting for Nick to, one, like review this, I think it's good he hasn't because I didn't really catch the thing on the tabs, but now that I look at them, like, okay, that makes sense that these should have been tabs.

**Jason Gong:** So as soon as he reviews this, I think we can probably deploy it.

**Jason Gong:** But until then, we can just keep polishing, I think.

**Jason Gong:** I'm trying to think if the tabs are maybe a little too, like, hidden, like you don't realize they're there.

**Edin Abazi:** Yeah, that's why I want to, like, play around with the styling a little more to make it more obvious.

**Jason Gong:** Yeah, other than that, I think it's good. The font size is right — it was just spacing and styling issues.

**Edin Abazi:** Similar to OpenAI, but when you look at the details like the sidebar, it's quite similar.

**Jason Gong:** Yeah, I think it's mainly the sidebar. I mean, it's not a bad thing because I don't know if anyone else is invested in making their blogs this nice.


**Edin Abazi:** I was going to ask, well, I wanted to discuss the table of contents, because...

**Jason Gong:** Personally, I think we could put it at the top so it's just there without cluttering the page as you scroll.

**Jason Gong:** I also really like the authors section at the top. Wonder if we could do something similar.

**Edin Abazi:** Will we have this many authors?

**Jason Gong:** I don't know.

**Jason Gong:** I think if, like, basically, from what I understand, their whole team works on these posts.

**Jason Gong:** I think, like, if we gave them a way to, like, very nicely kind of, you know, say who the main author was and then who the contributors were, I think they would go for that.

**Jason Gong:** And it makes it just feel more researchy.

**Edin Abazi:** Yeah.

**Edin Abazi:** Yeah, we can definitely play around with that.

**Edin Abazi:** I was thinking of, you know how we have the sidebar navigation on left?

**Jason Gong:** Yeah.

**Edin Abazi:** I was thinking of when the user clicks on a post, basically collapsing the menu, the navigation, and showing the table of contents within the left sidebar.

**Edin Abazi:** There's not enough space in the sidebar, and the UX is a bit questionable.

**Edin Abazi:** I'll play around with it a little more.

**Jason Gong:** I think we should make that the last thing. This Anthropic research site is a good reference — they have a clean table of contents at the top that doesn't scroll.

**Edin Abazi:** Just at the top?

**Jason Gong:** Yeah, ideally as a component so we don't have to manually update it. I was thinking Markdown, but...

**Edin Abazi:** I think I can do it programmatically.

**Jason Gong:** I like the design at the bottom of Anthropic's page. We could do a component with a styled background, small paragraph text, and bigger headers.

**Edin Abazi:** Yeah, I can create a component that takes Markdown and applies the styling.

**Jason Gong:** With that, we're pretty good. I really like Anthropic's site. For the scripts, they do a few separately, but most is probably just in the tag manager.

**Edin Abazi:** Yeah, I feel like everything should have been in the tag manager.

**Jason Gong:** We can ask them about that. We could make callouts slightly different color-wise.

**Edin Abazi:** Every article looks different on this Anthropic blog.

**Jason Gong:** Yeah, they're amazing. I'm reading one now — 10,000 words with tons of custom components. This is a nice lane of work that feels high-value. We can bring some of this design thinking to our content.

**Jason Gong:** Are there CMSs that let you write in MDX?

**Edin Abazi:** I really like MDX.

**Edin Abazi:** There's a CMS called Pages CMS that taps into your repo and gives you a file list to edit. I'm not sure about MDX support though, and React components in a CMS editor would be complicated.

**Jason Gong:** There's probably something. The main challenge is letting users visually add components without making the UI too complicated.

**Edin Abazi:** If the CMS had access to the codebase, it could read TypeScript types and know what components exist and their props. Interesting project to think about.

**Jason Gong:** I saw what Mergum did earlier — the tab component looks really good.

**Jason Gong:** Okay, let me just update the thread so he knows what we're working on.

**Edin Abazi:** I made a small list on the Linear task with things to do.

**Edin Abazi:** I'm tempted to make the font size slightly smaller on the blog post, but the slightly larger size gives a better reading experience.

**Jason Gong:** Wait, say that again?


**Jason Gong:** Yeah, they're all maybe one or two points smaller.

**Edin Abazi:** The highly academic ones always have smaller font.

**Jason Gong:** Yeah, I think that's the feeling they want — more academic.

**Jason Gong:** For long articles like Anthropic's, a floating table of contents would be helpful — hidden by default but peeks in from the side and shows on hover.

**Edin Abazi:** That's a good idea. Maybe a little icon that reveals on hover or click.

**Jason Gong:** Exactly.

**Edin Abazi:** I'll play around with that idea.

**Edin Abazi:** I think that's it.

**Edin Abazi:** What should we prioritize after this? There's a bunch on Linear.

**Jason Gong:** Maybe we can sync tomorrow — I have a call in a few hours and this will probably take the rest of the day.

**Jason Gong:** My priorities: not totally clear on the client stuff yet, but the main thing is the Lead Growth Community. Six people have already paid — crazy, because we haven't even publicized it. But after they pay, they don't get much right now, which feels bad.

**Jason Gong:** We did add payment options — just one checkout flow, but I could show you.

**Jason Gong:** It needs better styling, but six people paid $200/year (discounted to $50) for basically nothing yet.

**Jason Gong:** Right now they only get the workshop as a course, which is nice but it's the only offering. We need to expand the community. Plus the website has a PR I need to review — it needs to catch up to what the community actually offers now. That's my top priority.

**Jason Gong:** We can chat more after the search stuff.

**Edin Abazi:** Just keep me updated.

**Jason Gong:** I'll see if Nick replies. Just the four things I noted in the thread.

**Edin Abazi:** Cool. Chat later.

**Jason Gong:** Bye.
