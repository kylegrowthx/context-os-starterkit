# Brex Resources Hub: Design Feedback from CDO Review

<metadata>
purpose: Actionable design feedback document for the design engineer implementing Resources Hub changes
audience: GrowthX design engineer (internal)
summary: Collated feedback from Bango (Brex CDO) on the Resources Hub redesign, relayed by Jon Kowieski on Feb 26, 2026. Organized by component with clear approved/rejected/ambiguous status for each item.
domain: client-delivery
confidence: high
context_tier: 2
last_updated: 2026-03-02
</metadata>

**Source:** Feb 26, 2026 Brex weekly sync. Bango reviewed the prototype at `brex-hub.onrender.com/resources` side-by-side with the current `brex.com/resources`. Jon relayed all feedback.

**Reference doc:** [Proposed Enhancements (Talking Points)](brex-resources-page-talking-points-v1.md)

**Live prototype:** [brex-hub.onrender.com/resources](https://brex-hub.onrender.com/resources)

**Production:** [brex.com/resources](https://www.brex.com/resources)

---

## How to Read This Document

Each section covers a specific component or page of the Resources Hub. Within each section:

- **KEEP** = Do not change from what's currently on brex.com
- **CHANGE** = Modify from the prototype to match this feedback
- **ADD** = New element approved for inclusion
- **REMOVE** = Element should be taken out
- **BUILD** = Proceed with building, but expect possible revisions in next round

Every item includes the specific instruction and, where relevant, why Bango cares about it.

---

## 1. Global Design Rules

These apply to every page in the Resources Hub. Bango called typography his "number one thing across all these new pages."

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Typography (font sizes, weights) | Match production exactly. Do not increase or decrease any font sizes from what is currently live on brex.com. This was Bango's top priority. |
| 2 | KEEP | Image proportions and sizes | Match production. Do not change image aspect ratios or dimensions from what currently exists on the live site. |
| 3 | KEEP | Spacing | Match production. Card spacing, section spacing, padding must all match the current design system. |
| 4 | CHANGE | Tag placement | Move all tags (e.g., "Spend Trends", "CFO", topic tags) to appear directly above the "Read More" button on every card, across every page. Currently in prototype they appear elsewhere. |
| 5 | CHANGE | Build environment for next review | Next version must be shown in Sanity, not on Render. Bango specifically requested this. He did not want to review in Render. |

**Why this matters:** Bango views deviations from the existing design system as a non-starter. The prototype had larger fonts, different image sizes, and adjusted spacing. All of that must revert to match production. The new features we're adding (tags, CTAs, sections, metadata) are approved, but they must live within the existing visual framework.

---

## 2. Global Navigation (Resources Dropdown)

This is the highest-impact change with the fewest objections. Jon: "The main nav will actually be more powerful than the rest of this."

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | ADD | Blog | Add "Blog" as a navigation item in the Resources dropdown. Bango's first question was "Where's the blog in this?" This was his biggest concern. |
| 2 | ADD | Brex Benchmark | Add "Brex Benchmark" as a navigation item. Bango is actively pushing Brex Benchmark as a brand property. Consider renaming what was "Reports" to "Brex Benchmark." |
| 3 | ADD | Topics index | Approved. Jon convinced Bango that the topics index adds value. Keep it in the nav. |
| 4 | REMOVE | Careers | We removed Careers from the nav in the prototype. Bango did not notice or object. Jon agrees it no longer fits. Note: Bango may notice and question this in a future round, so be prepared to justify. |
| 5 | CHANGE | Featured article (right panel) | The "Latest" panel on the right side of the dropdown should be static/manually controlled, not dynamically pulling the most recent article. Set it to the Capital One acquisition announcement for now. Bango wants to control what's featured here. |
| 6 | KEEP | Everything else in the nav | All other proposed additions (content type links, topic links) were accepted. The rest of the restructured dropdown was approved as designed. |

**What to build:** A three-column Resources dropdown with Blog, Brex Benchmark, Topics, and all content type links in "Discover." Right panel shows the Capital One acquisition article as a static featured piece. No Careers link.

---

## 3. Sub-Navigation and Breadcrumbs

This is the most structurally different change from the prototype. Bango was firm on this despite Jon pushing back.

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Breadcrumb bar | Keep the breadcrumb (e.g., "Resources / Articles") styled exactly as it appears on the current production site. Upper left, same font, same style. Bango explicitly likes this style. |
| 2 | CHANGE | Secondary nav position | Move the secondary nav (Articles, Books, Case Studies, Reports, Index, Tools) from the upper-right position in the prototype to below the breadcrumb bar. Stack it: breadcrumb on top, secondary nav underneath. |
| 3 | REMOVE | "Resources" heading text | Bango crossed out the "Resources" heading text in the upper left of the main page. Remove it. The breadcrumb handles orientation. |

**Bango's exact words (via Jon):** "Leverage a breadcrumb bar and add the secondary nav below it."

**Layout structure:**
```
[Breadcrumb: Resources / Articles]
[Secondary Nav: Articles | Books | Case Studies | Reports | Index | Tools]
[Page content below]
```

**Note from Jon:** "I'm not sure how that's going to look. Be honest. But I was like, okay. I tried to explain why we should keep it as well. And I tried very hard. But that was one thing that was really important to him." This is non-negotiable for now. Build it, show it, and we may revisit in a future round if it looks off.

---

## 4. Resources Hub Main Page (/resources)

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Card layout and image styles | Use the existing card layout from production. Same image sizes, same card proportions. Do not use the resized cards from the prototype. |
| 2 | KEEP | Content card style (featured section) | The large featured content card on the left stays in its current production proportions. Do not resize. |
| 3 | CHANGE | Tags on cards | Move tags to directly above "Read More" on every card. |
| 4 | ADD | "By Brex" + date | Bango approved adding publisher attribution and date to cards. E.g., "By Brex, January 2026." Jon explained the SEO value and Bango agreed. |
| 5 | KEEP | CTA section | The CTA banner/section stays. Jon spent 5-10 minutes convincing Bango not to remove it. It's approved. |
| 6 | CHANGE | CTA copy | Replace "Join the waitlist" with clearer copy. The current copy confused Bango ("So this is a newsletter?"). Jon's suggestion: "Keep up with Brex benchmark and Brex product updates." Finalize copy with Brex team, but the direction is clear: describe what users get, not a waitlist. |
| 7 | ADD | New content sections | Case Studies, E-books & Guides, The Index, Tools, Trending, Spend Trends, and topic-specific sections were all approved. Build them out. |
| 8 | ADD | "See All" links | Approved on every section. These create the indexable hub pages we need for SEO. |
| 9 | REMOVE | "Resources" heading text | See Section 3 above. Remove the heading. |

---

## 5. Articles Page (/resources/articles)

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Typography and layout | Match production. Same font sizes, same card sizes, same spacing. |
| 2 | CHANGE | Tags on cards | Move tags above "Read More." Same as global rule. |
| 3 | KEEP | Everything else | Jon: "I think he was fine with most of this." All other proposed changes (topic filtering, organization) are approved. Most content on this page is Spend Trends. |

---

## 6. Ebooks Page (/resources/ebooks)

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | BUILD | Ebook organization/filtering | The current ebook filter on production is broken. Jon demonstrated this live to Bango by trying to filter for AI ebooks and showing it takes multiple clicks with no clear path. Our redesigned version lets users browse by category in one click. Bango did not give explicit approval but leaned positive. Jon: "I'd say do it. But he didn't say for sure, yes or no. I think he's thinking through it still." |
| 2 | KEEP | Typography | Match production. Same font sizes, weights, and spacing. |
| 3 | BUILD | Category-based browsing | Build it as designed in the prototype. If a user wants only AI ebooks, they should find them in one click. This is a significant UX improvement over the broken filter. |

**Risk:** This may face back-and-forth in the next review round. Build it following all other design system rules (typography, image sizes) to minimize objections.

**Cover:** Jon explicitly said to attribute this decision to him if Bango questions it: "You can just say I said that." Since Jon is leaving March 10, use this runway to get the ebooks page built and in front of Bango before his departure.

---

## 7. Case Studies Page (/resources/case-studies)

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | CHANGE | Image shape | Use rectangular images, not square. Bango explicitly rejected squares: "He does not like the square. He's like, rectangle. I want to keep our current design system." |
| 2 | CHANGE | Grid layout | Three case studies per row, not four. With rectangular images at the correct proportions, four per row would make cards too small to read. Three per row maintains readability. |
| 3 | CHANGE | Tags on cards | Move tags above "Read More." Same as global rule. |
| 4 | KEEP | "See All" link | Approved. Placement as designed. |
| 5 | KEEP | Rest of layout | Jon: "The rest of this he was fine with adding as long as you continue doing the same thing, like tags below." All new sections, organization, and structure are approved. |
| 6 | KEEP | CTA section | Same as main page. Keep the CTA, change the copy. |

---

## 8. Article Template (Individual Article Page)

This was "not a fun part of the review." Bango did not like the typography changes on article pages. Revert typography and keep the approved additions.

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Typography | Revert to production typography. Bango "did not enjoy the typography" on the article template. Match font sizes, heading styles, body text exactly to production. |
| 2 | ADD | Author, date, time to read | Add author name, publish date, and estimated read time at the top of the article. Approved. |
| 3 | ADD | Topic tag above title | Add the topic tag (e.g., "Expense Management") above the article title. Approved. |
| 4 | ADD | Header image (Spend Trends only) | Header images can be added to all Spend Trends articles. Jon: "He doesn't need to approve that." This is already within scope for Spend Trends, which are the majority of articles on the site. |
| 5 | CHANGE | Table of contents | Use dropdown style instead of sticky sidebar. Bango: "Why not just keep what we have on the page where it's like a drop down." Match the existing ToC pattern on production. |
| 6 | ADD | Social share buttons | LinkedIn and Twitter only. No Facebook. Bango agreed Facebook doesn't make sense for Brex. George confirmed the final scope: "We'll just make it just LinkedIn and Twitter." |
| 7 | KEEP | Topic tags at bottom of article | Tags at the bottom of the article are approved for Spend Trends articles. Jon: "The topics at the very bottom. The tags. Yeah, you can do that is fine for Spend Trends." Since Spend Trends is the majority of articles on the site, apply this to all articles but note it was only explicitly confirmed for Spend Trends. |
| 8 | KEEP | FAQ section styling | Keep FAQ in the design system. Typography matches production. Styling approach from the prototype is fine. |
| 9 | KEEP | Related articles section | Approved, as long as card images and typography match the design system. The additions (author, date, time to read, tag, "Read More") on related article cards are all fine. |

---

## 9. CTA Component (All Pages)

The CTA appears on multiple pages. This feedback applies everywhere it shows up.

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | CTA section exists | Jon convinced Bango to keep it. It stays on all pages. |
| 2 | CHANGE | Copy: headline | Replace "Join the waitlist" and any newsletter-sounding language. Bango asked "So this is a newsletter?" and was confused. |
| 3 | CHANGE | Copy: description | Make the purpose clear. Jon's direction: something like "Keep up with Brex benchmark and Brex product updates." Position it as a content/product update signup, not a generic newsletter. |
| 4 | CHANGE | Copy: button text | Replace "Join the waitlist" button text with something that matches the new messaging. E.g., "Subscribe" or "Get updates." |

**Copy is not finalized.** Jon said he needs to think through the exact wording. George also suggested pulling the existing CTA copy from the current brex.com as a safe starting point. For now, build the component with placeholder copy that follows this direction and flag it for final copy approval.

---

## 10. Tools and Index Pages

| # | Action | What | Detail |
|---|--------|------|--------|
| 1 | KEEP | Tools index layout | Approved. Jon: "Tools, it's very much like Spend Trends, have full control. It's just the design system. Good to go." |
| 2 | KEEP | The Index layout | Approved. Jon: "The index was fine. We went through that." |
| 3 | KEEP | Design system rules | Same typography, image sizes, and spacing rules apply. |
| 4 | BUILD | Topics in main nav | Bango asked to see what topics look like in the main nav. Jon: "He just wanted to see what it looked like and if it looks like this, it's like completely fine. I'll say just create it. It'll be better for the overall website at the end of the day." Build it. |

---

## 11. Approval Status Summary

### Explicitly Approved

| Item | Notes |
|------|-------|
| Blog in global nav | Bango's biggest ask |
| Brex Benchmark in global nav | Bango pushing this as a brand property |
| Topics index in nav | Jon convinced him |
| Static featured article (Capital One acquisition) | Bango wants manual control |
| Tags above "Read More" (all pages) | Approved across the board |
| CTA section (kept, with copy change) | Jon fought for it successfully |
| New content sections on /resources | Case Studies, E-books, Index, Tools, Trending, etc. |
| "See All" links on every section | Approved |
| "By Brex" + date on cards | SEO rationale accepted |
| Article metadata (author, date, read time, topic tag) | Approved |
| Header images for Spend Trends articles | Doesn't need further approval |
| Social share: LinkedIn + Twitter only | Facebook dropped |
| Topic tags at bottom of articles | Approved |
| Related articles section | With design system compliance |
| FAQ section styling | With design system compliance |
| Tools index page | Full control, design system |
| The Index page | Approved |

### Explicitly Rejected

| Item | Reason |
|------|--------|
| Changed typography (larger fonts, different weights) | Must match production design system |
| Changed image sizes/proportions | Must match production design system |
| Changed spacing | Must match production design system |
| Square case study images | Must be rectangular |
| Four case studies per row | Must be three per row |
| "Join the waitlist" CTA copy | Confused Bango, needs rewrite |
| "Resources" heading text on main page | Bango crossed it out |
| Showing next version on Render | Must be in Sanity |
| Facebook social share | Not relevant for Brex |
| Sticky sidebar table of contents | Use dropdown style instead |

### Ambiguous / Needs Discussion in Next Round

| Item | Status | Our Approach |
|------|--------|--------------|
| Ebooks page organization/filtering | Jon argued for it, Bango leaned positive but no explicit yes | Build it. Follow design system. Expect possible feedback. |
| Careers removed from nav | Bango didn't notice. Jon agrees it should go. | Leave it out. Justify if asked. |
| Topics in main nav | Bango wanted to see it, not explicit yes | Build it. Jon says "just create it." |
| CTA final copy | Direction set, exact wording TBD | Use placeholder. Flag for approval. |
| Sub-nav/breadcrumb layout | Approved by Bango but Jon is skeptical it'll look right | Build it as specified. May revisit after seeing it live. |

---

## 12. Process Notes

**Revision rounds are normal.** Bango's banking page went through 12 rounds. Jon: "We've never had one, two rounds, three rounds, four rounds, multiple rounds. But I feel like most of these, maybe we do get to two rounds."

**Next review should include Alex Rudyak.** Jon: "If we get Alex next round to go through it with him and show your changes, it will be very helpful. So he heard from me UX, technical SEO, user journeys and why it would benefit."

**The written doc was valued.** Bango was very positive about the talking points document. Jon: "He was like, yes, I'm very glad they did that. I'll take a look. I'm very busy. I normally don't have time to think through all this stuff very thoroughly." Continue preparing detailed written docs for future reviews.

**Compliance context.** FINRA compliance reviews now apply to content mentioning Brex products, banking, or yield. This likely won't affect Resources Hub structure or tools, but any article copy or product marketing language may need legal review. Not a blocker for the design work.

**Team transition.** Jon Kowieski's last day is March 10. Yolanda La is taking over as primary Brex contact. All future design feedback will flow through Yolanda and Alex.

**Technical access.** Kurt needs Vercel access to submit PRs. This is the last blocker for implementing changes in the production codebase. Jon is coordinating with admins.

---

## Implementation Priority

Based on impact and approval clarity:

1. **Global Navigation (Resources Dropdown)** - Highest impact, cleanest approval. Add Blog, Brex Benchmark, Topics. Set static featured article. Remove Careers.
2. **Global design system compliance** - Revert all typography, image sizes, and spacing to match production across every page.
3. **Tag repositioning** - Move tags above "Read More" on all card types, all pages.
4. **Sub-navigation/breadcrumb restructure** - Breadcrumb above, secondary nav below. Remove "Resources" heading.
5. **Resources Hub main page sections** - Build out all approved content type sections with "See All" links.
6. **Article template updates** - Add metadata (author, date, read time, topic tag), header images for Spend Trends, dropdown ToC, LinkedIn + Twitter share.
7. **CTA copy update** - Replace across all pages. Use placeholder if final copy isn't confirmed.
8. **Case studies page** - Rectangular images, three per row.
9. **Ebooks page** - Build category-based browsing. Follow design system.
10. **Tools and Index pages** - Build out following design system rules.

---

*Source: Feb 26, 2026 Brex weekly sync. Feedback from Bango (CDO) relayed by Jon Kowieski.*
*Prepared by GrowthX | March 2, 2026*
