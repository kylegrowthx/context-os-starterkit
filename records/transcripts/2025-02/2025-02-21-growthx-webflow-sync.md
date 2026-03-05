# GrowthX / Webflow Sync

<metadata>
date: 2025-02-21
time: 16:00 UTC
duration: 15 minutes
organizer: Vivek Shankar (GrowthX)
participants: Vivek Shankar (GrowthX), Raveena Kapatkar (Prophecy.io), Yigit Arslan (thefunf.com)
fathom_recording_id: 48423699
fathom_url: https://fathom.video/calls/237623950
share_url: https://fathom.video/share/m7Ws4CjTUgPyTYxPnTNwATfNmCi1gNJZ
source: fathom
enriched_on: 2026-03-05 14:32 UTC
</metadata>

---

## Summary

GrowthX identified four SEO issues in Prophecy.io's Webflow blog that emerged when one blog post failed to index automatically: duplicate H1 tags hidden in the HTML markup, lorem ipsum placeholder text, unexpected H3 tags appearing before H1s in the DOM structure, and unusual internal linking patterns with query parameters. Yigit Arslan agreed to implement JavaScript-based fixes for the duplicate H1s and investigate the template issues, with the team emphasizing that Google's crawler reads raw markup rather than executed JavaScript when making indexing decisions.

---

## Context

Prophecy.io is a GrowthX client using Webflow to power their marketing site, including their blog. GrowthX's marketing engineering team (represented by Vivek Shankar and the broader VEC—the Vivek Engineering Crew) provides content and technical SEO support for the blog. The meeting was triggered when one of Prophecy.io's blog posts failed to appear in Google's search index automatically, prompting GrowthX to audit the HTML structure and surface several markup-level issues that likely contributed to indexing problems. Yigit Arslan, the lead developer at Prophecy.io, owns the technical implementation of the fixes. Raveena Kapatkar is the internal contact managing the relationship with Prophecy.io and overseeing the collaboration.

---

## Relevance

**To GrowthX Delivery:**
- SEO auditing of third-party platforms (Webflow) is a key service offering; this call demonstrates GrowthX's ability to identify non-obvious markup issues affecting indexation.
- Conditional visibility and hidden DOM elements in page builders are a recurring source of SEO problems—a teachable pattern for future audits.
- Client expectation-setting around Google's crawler behavior (raw markup vs. JavaScript execution) is essential for managing scope and solution feasibility.

**To CheckThat:**
- Duplicate structured data and hidden heading elements could affect AI model visibility and citation quality. Future CheckThat audits could flag these hidden-element patterns.
- The indexation failure highlights how technical markup issues impact both human SEO and AI crawlers.

**To GrowthX Business Development:**
- Prophecy.io's willingness to address SEO issues and implement fixes suggests strong account health and engagement. No renewal risk signals.
- Prophecy.io plans to hire a dedicated technical resource to manage their site—potential upsell opportunity for deeper technical SEO services or ongoing fractional support.

---

## Overview

- Multiple SEO issues identified: duplicate H1 tags, lorem ipsum text, unexpected H3 tags, and unusual internal linking
- Yigit (thefunf.com) will implement fixes, likely using JavaScript for H1 issue and investigating template problems for others
- Google crawler reads markup, not executed JavaScript, influencing SEO solution approach
- Some issues (e.g., internal linking) may be less problematic than initially thought due to site structure

---

## Key Topics

### Duplicate H1 Tags

  - Issue: Multiple H1 tags appearing in HTML, invisible on frontend
  - Cause: Conditional visibility for different layouts, Webflow keeps hidden elements in markup
  - Solution: Yigit to implement JavaScript fix to remove duplicates on page load
  - Concern: Effectiveness depends on whether Google's crawler executes JavaScript (it doesn't)

### Lorem Ipsum Text

  - Problem: Placeholder text found in blog pages, potentially flagged as low quality by Google
  - Action: Yigit to investigate and remove across the site, not just blog posts

### Unexpected H3 Tags

  - Issue: Four specific H3 tags appearing before H1 in blog post HTML
  - Yigit to investigate cause in blog post template

### Unusual Internal Linking

  - Problem: Search Console showing unexpected referring pages with odd parameters
  - Likely cause: Recent posts section at the end of each blog post + parameter carrying between pages
  - Less concerning than initially thought due to site structure explanation

---

## Action Items

**Yigit Arslan (Prophecy.io)**
- Fix duplicate H1 headings in blog posts HTML. Implement JavaScript solution to remove hidden H1s on page load.
- Remove lorem ipsum placeholder text from blog pages and check rest of website for any remaining instances.
- Investigate and fix unexpected H3 headings appearing before H1 in blog post HTML structure.
- Review blog post template for any other SEO-related issues and fix as needed.
- Update Raveena Kapatkar on fixes implemented for SEO issues discussed in meeting.

**Vivek Shankar (GrowthX)**
- Clarify with Yigit whether Google crawler executes JavaScript when reading H1 markup (answer: Google reads raw markup, not executed JS).

---

## Transcript
**Vivek Shankar:** for you.

**Raveena Kapatkar:** Good.

**Raveena Kapatkar:** How are you?

**Raveena Kapatkar:** How's your Friday?

**Raveena Kapatkar:** Good.

**Vivek Shankar:** It's a this meeting is being recorded.

**Raveena Kapatkar:** Yeah.

**Raveena Kapatkar:** Well, this is Yigit.

**Raveena Kapatkar:** This is the VEC.

**Raveena Kapatkar:** VEC is part of the GrowthX team.

**Raveena Kapatkar:** So they're the ones that are helping us with our blogs, blog content and everything.

**Raveena Kapatkar:** So they we wanted to have this meeting just because there was a couple of things that they found through Webflow.

**Raveena Kapatkar:** They wanted us to address.

**Raveena Kapatkar:** And so then you go through everything, then you can discuss with the E hit on exactly what we need to fix and everything.

**Vivek Shankar:** Sure.

**Vivek Shankar:** Do you guys have the Google Doc from weeks before, or do I need to send it again?

**Raveena Kapatkar:** Where did you send it?

**Vivek Shankar:** It was in the agenda. I can just paste it here.

**Raveena Kapatkar:** Oh, there we are.

**Vivek Shankar:** I used this one. It should be view-only, but yes, I see it.

**Vivek Shankar:** I can share my screen as well.

**Vivek Shankar:** So, for context, the reason we ran into this is because one of the blog posts did not get indexed automatically.

**Vivek Shankar:** We ran an audit to see if there were any issues.

**Vivek Shankar:** That's when we found all of this in the HTML.

**Vivek Shankar:** The first issue we found was duplicate H1 headings.

**Vivek Shankar:** The document explains everything. It looks fine on the CMS side and on the frontend, but in the HTML, there are two H1 tags—one is visible and another one is hidden for some reason.

**Vivek Shankar:** I'm not quite sure what's happening.

**Vivek Shankar:** We think it might be some issue with the template itself, perhaps there's some special issue.

**Yigit Arslan:** Yeah, I know why this is happening. There's probably some conditional visibility set up to show headings with different layouts. The problem is that Webflow doesn't delete them—it renders them but keeps them hidden in the markup.

**Yigit Arslan:** We can find a programmatic solution. Maybe we can remove them on page load, but I don't know if Google's crawlers run that JavaScript to read the HTML structure.

**Yigit Arslan:** Sometimes the marketing team needs multiple heading elements for customization—when the heading is too wide and there's an unwanted line break, we need to use different heading variations. Webflow renders both and hides one. If solving this with JavaScript on page load works for you, that's the simpler solution. Otherwise, I'd need to find another approach.

**Vivek Shankar:** I think that should be fine. I don't see an issue with it.

**Yigit Arslan:** Okay.

**Vivek Shankar:** From our side at GrowthX, the main issue is that you're eventually going to hire somebody. Ashleigh mentioned that somebody will come in and take charge of the website's technical side. Ultimately, it'll be your call from a communication perspective. I don't have any issues.

**Vivek Shankar:** As long as it doesn't affect performance, as long as it doesn't affect indexing, whatever solution then use as best.

**Vivek Shankar:** Well, ahead.

**Yigit Arslan:** I'm technically in charge of the website, but I'm asking you because this is an SEO issue. If Google's crawler lands on the site and just reads the markup as-is, those duplicate H1s will be in the markup. But if the crawler runs JavaScript and sees only one H1, that's a different scenario. That's a technical thing related to Google's rules.

**Yigit Arslan:** So I can find a solution based on that, or I can just change the feature so we have only one heading from the start. The JavaScript solution I mentioned is simpler.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So the question is: does it read markup or JavaScript?

**Yigit Arslan:** Yes.

**Vivek Shankar:** Yes, it reads the markup. So based on that, whatever solution you need to take.

**Vivek Shankar:** The second issue we found is lorem ipsum placeholder text. We've found it on some pages, but we only looked at the blog pages, so I'm not sure if the rest of the site has it.

**Vivek Shankar:** From an SEO perspective, the problem is that Google might flag lorem ipsum as low quality. We haven't run into issues yet, but it'd be good to clean it up.

**Vivek Shankar:** This is the confusing one. There are H3s that show up before the H1. Before the first H1, there are these exact same four H3s that appear repeatedly.

**Yigit Arslan:** I'm not sure why that's happening. Is this a blog post?

**Vivek Shankar:** This is a blog post. You can see the headers listed in the order they appear in the HTML. I checked a couple of other blog posts, and these four H3s are showing up repeatedly for some reason.

**Yigit Arslan:** Wow, alright, so yeah, this is probably because...

**Yigit Arslan:** Okay, there's a hidden...

**Yigit Arslan:** Ah, well, I think I know what is this.

**Yigit Arslan:** Okay, so you would detect these issues in the blog posts, right?

**Yigit Arslan:** So I need to go through on the blog posts to see these issues.

**Vivek Shankar:** Right, well, we're looking at the website because we are only focused on the blog posts.

**Vivek Shankar:** Like we didn't get the rest of the site, so yeah, might be good to just look at it.

**Vivek Shankar:** I'm sure if it's happening in the blog, it might be happening elsewhere.

**Vivek Shankar:** The last issue we found is unusual internal linking. We looked at Search Console and found some referring pages that look weird—one's from the main Prophecy.io blog, but another one is from an "Announcing Prophecy University" page that doesn't seem to exist, or at least that's what we thought.

**Yigit Arslan:** What do you mean by referring page?

**Vivek Shankar:** A referring page is how Google is finding and accessing this page. In this case, it's showing links from pages we didn't expect. We created "The 12 Essential Data Engineering Skills" two weeks ago and didn't link to it from anywhere, so it's confusing why "Announcing Prophecy University" is appearing as a referring page.

**Yigit Arslan:** "Announcing Prophecy University" is just another blog post. But I think I know why it's showing up. At the end of every blog post, there's a section showing recently posted blog posts. So every page links to your new posts. But I'm not sure why there are those query parameters in the URL.

**Yigit Arslan:** It's possible we're carrying parameters through the session. If someone lands on the homepage with parameters, those parameters get passed along to other pages visited in that session.

**Vivek Shankar:** Okay, so that explains it. Anyway, this doesn't look like as much of an issue then.

**Yigit Arslan:** Maybe I should review the template for any other issues like this. I think I know why those duplicate headings are showing up.

**Vivek Shankar:** That was all we had.

**Raveena Kapatkar:** Okay. Thank you. Yigit, once you have access to the document, can you review it and keep us posted on how you fix these issues?

**Vivek Shankar:** No, that was it from us.

**Raveena Kapatkar:** Awesome. Then I think we're good to go. Just keep us posted.

**Yigit Arslan:** I'll update you once it's solved.

**Vivek Shankar:** Sure. Thank you.

**Yigit Arslan:** All right.
