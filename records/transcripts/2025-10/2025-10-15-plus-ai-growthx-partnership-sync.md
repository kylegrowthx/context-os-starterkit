# Plus AI <> GrowthX - Partnership Sync

<metadata>
date: 2025-10-15
time: 19:33 UTC
duration: 28 minutes
organizer: Tyler Pavlas (GrowthX)
participants: Marcel Santilli (GrowthX), Dan Li (Plus AI), Tyler Pavlas (GrowthX)
fathom_recording_id: 94465546
fathom_url: https://fathom.video/calls/441458620
share_url: https://fathom.video/share/9ii9pP8Lo2ZjvrxKfnQMYhXxHSsxfk1p
source: fathom
enriched_on: 2026-03-02 00:32 UTC
</metadata>

---

## Summary

GrowthX and Plus AI scoped a potential partnership around programmatic template pages and editorial content strategy. Plus AI needs help with keyword research, content generation, and SEO optimization for thousands of presentation template pages—a workflow-heavy project that fits GrowthX's capabilities. The team agreed to focus on a hybrid approach: launching 20+ new templates with programmatic page generation, refreshing existing content, and researching editorial expansion opportunities. Next steps: Marcel will provide a detailed proposal outlining GrowthX vs. Plus AI responsibilities and timelines.

---

## Context

Plus AI is an AI presentation generation platform that allows users to create presentations via API or UI. They've built a library of presentation templates and have ambitions to scale from hundreds to thousands of indexable pages across categories like "construction templates," "startup pitch decks," and "how-to" content. Tyler (Plus AI's head of growth) and Dan (engineering) connected with Marcel (GrowthX CEO) and Tyler (GrowthX) to explore how GrowthX's content workflow and SEO expertise could help them achieve that scale.

This meeting was a scoping call to assess fit and define responsibilities. Dan emphasized that Plus AI has capacity on the engineering and programmatic side but wants outside expertise on SEO strategy, keyword research, and content-to-page mapping. Marcel was transparent about GrowthX's current resource constraints due to other client commitments and platform launches, signaling that the engagement should focus on strategy and workflow building rather than custom design or engineering.

---

## Relevance

**To GrowthX Delivery:**
- High-quality workflow opportunity aligned with GrowthX's core strength: building scalable content systems. Can reference this as a case study for how to map workflows to thousands of pages.
- Template-based approach (not full design) fits GrowthX's constraint to avoid custom engineering. Plus AI's Webflow CMS is manageable within standard workflow patterns.
- Potential to establish playbook for programmatic page generation + editorial refresh that could be reused across future clients (Magic Slides, Zapier-style models).
- Plus AI's API-based architecture means content feeds directly into workflows—clean integration pattern.

**To CheckThat:**
- Plus AI presentation templates could benefit from AI visibility strategy: understanding how presentation-adjacent content ranks in AI search results and how to optimize for AI model training.
- Discussion of embedding PowerPoint vs. text extraction touches on AEO concerns: whether embedded media is indexable and how to make slide content discoverable to AI models.

**To GrowthX Business Development:**
- Partnership value: $30k deal already exists (strategy sprint starting 10/1/25). Scope and delivery success here could justify expansion into ongoing managed services.
- Account expansion signal: Dan mentioned tools as secondary opportunity ("Word to PPTX" is popular). Could become a content + distribution play if templates succeed.
- Reference potential: If Plus AI ships 1000+ SEO-optimized pages and gains traction, this becomes a strong case study for programmatic content at scale.

---

## Overview

- Plus AI operates a presentation generation platform with existing template pages but needs to scale from hundreds to thousands of SEO-optimized pages across categories like "construction templates" and "startup pitch decks."
- GrowthX excels at workflow building and content generation but is capacity-constrained due to platform launches and other custom client projects (Lovable, Webflow, Brex, Ramp, etc.), so the engagement must focus on strategy, workflow building, and quality review—not custom design or engineering.
- Both parties agreed to a hybrid approach: Plus AI leads programmatic page generation and technical implementation; GrowthX leads SEO strategy, keyword research, category mapping, and editorial content (both new and refresh).
- The MVP scope includes launching 20+ new templates, refreshing existing content, and researching additional editorial opportunities (e.g., "how-to" articles, comparison content, tool integrations).
- Plus AI will provide permanent URLs for API-generated presentations and confirm API parity with UI-based generation; GrowthX will deliver a proposal detailing responsibilities, timelines, and next steps within 24 hours.

---

### Plus AI's Current Setup and Needs

- Using Webflow CMS for template pages; currently manages this manually, but faces scalability challenges beyond a few hundred pages.
- API now available to generate presentations programmatically (.pptx format); previously manual creation was the only option.
- Current content strategy includes best-of listicles, versus/comparison content, alternatives-to content, and how-to articles—estimated ~355 blog articles for their category.
- Seeking help with keyword research (what terms should they target?), category/listing page strategy (how to organize thousands of pages), content generation workflows, and SEO optimization.
- Open to editorial expansion but feels they've covered obvious low-hanging fruit; wants outside perspective on what's next.
- Top pages manually updated ~monthly (e.g., "Best AI Presentation Makers"), while how-to articles are largely set-and-forget.

### GrowthX's Capabilities and Constraints

- Confident and experienced in building scalable content workflows that can crank out high-quality pages programmatically.
- Has playbook for this type of work (referenced Zapier/Bardeen AI model with human-in-the-loop quality review).
- Extremely capacity-constrained: already managing custom projects for Lovable, Webflow, Brex, Ramp, Xen Appier, Surge, and others; launching platform to customers in ~1 month.
- Cannot commit to custom design/engineering work, templating, or pull requests into client repos—these are non-standard, time-intensive activities.
- Can focus on strategy, workflow building, quality review, and content generation.

### Programmatic Page Generation and API Discussion

- Plus AI API generates .pptx files delivered as CloudFront URLs; currently files expire after X hours/days (needs permanent URLs).
- API also supports Google Slides; both formats can be embedded (PowerPoint via Microsoft viewer iframe, Google Slides natively).
- Key concern: embedded presentations don't have readable text for SEO or AI models; alternative is to extract text, generate PNG screenshots, or create a transcript of slide content.
- Plus AI can handle one or all of these options; GrowthX and Plus AI need to determine the best approach for SEO and AI visibility.
- Dan showed that API has full feature parity with UI (custom prompts, template selection, outline control).

### SEO Strategy: Category Pages and Programmatic Expansion

- Discussion centered on why category/listing pages are critical for SEO: TripAdvisor, Wix, ThemeForest all rank category pages higher than individual items.
- Plus AI needs to create hundreds of category pages (not just the main "templates" page) with filters like professional/consulting/dark mode, plus use-case-based categories like "construction templates," "startup pitch decks," etc.
- Key insight: each filter option should be a unique, indexable page (e.g., "construction templates" is a separate page from "professional templates"). Users see a seamless app-like experience, but search engines see distinct pages.
- Scope: 5-50 presentations per category minimum, across dozens of categories. If targeting thousands of pages, Webflow's headless CMS may become a bottleneck; Plus AI's own database solution (pending) would be better.
- MVP: launch 20+ new templates, set up category page structure, refresh 2-3 top existing pages to test quality and workflow.

### Editorial Expansion Opportunities

- Plus AI has mostly relied on direct tutorials and comparisons; lacks depth in long-form editorial or emerging topics.
- Magic Slides publishes ~100 articles per day (low quality), but still ranks 2-3 per query; Plus AI's human-in-the-loop approach could significantly outrank them with far fewer, higher-quality articles.
- Editorial serves dual purpose: (1) topical authority and internal linking for programmatic pages, (2) insurance policy if programmatic pages stall.
- Marcel suggested exploring tools/utilities (e.g., "Word to PPTX," "PNG to SVG") as micro-content opportunities; Plus AI has popular converters but hasn't productized them.
- Content refresh strategy: programmatic workflows can automatically keep editorial content fresh (e.g., monthly updates to comparison content, re-ranking of tools, etc.).

### Proposed Hybrid Scope

- **GrowthX responsibilities:** SEO strategy, keyword research, category mapping, workflow building, quality review, editorial recommendations and creation (refreshes + new pieces).
- **Plus AI responsibilities:** Programmatic page generation, API permanent URLs, category page templating in Webflow, presentation library sourcing.
- **Shared responsibility:** Technical integration (how to pipe Plus AI data into GrowthX workflows, how to display presentations on pages for SEO).
- No custom design or site redesign; work within Plus AI's existing Webflow template.
- First milestone: proposal due tomorrow, kickoff within 2 weeks.

---

## Action Items

**Dan Li (Plus AI)**
- Ensure Plus AI API provides permanent URLs for generated presentations (currently deleted after X hours/days)

**Marcel Santilli (GrowthX)**
- Research editorial opportunities for Plus AI; provide recommendations
- Reconnect with Tyler Pavlas re Plus AI project scope; draft proposal including 20+ new templates and content refresh strategy
- Prepare readout for Dan Li detailing GrowthX vs Plus AI responsibilities in potential partnership

---

## Transcript

**Tyler Pavlas:** This meeting is being recorded.

**Tyler Pavlas:** Hey, you're on mute. Can you hear me, though?

**Marcel Santilli:** Yeah. How's it going?

**Tyler Pavlas:** It's going great. I'll set the stage for you because there's some important context to put out there up front, but the whole goal here is just to properly scope things out.

**Marcel Santilli:** I read your note and talked to Dan in person at the CEO conference.

**Tyler Pavlas:** Oh, perfect. Do you even want me to set the stage?

**Marcel Santilli:** Only if there's anything above and beyond those two things. Is there any context that wasn't in the calendar?

**Tyler Pavlas:** No, no. You've got everything you need.

**Tyler Pavlas:** Hey, Dan.

**Dan Li:** Good to see you again.

**Tyler Pavlas:** Thanks for your patience, by the way. I know it took a while to connect with Marcel and look into the use case in more detail. So glad we're finally circling back.

**Dan Li:** Yeah, no worries.

**Marcel Santilli:** I love that. The picture in the back—is that your family?

**Dan Li:** Yeah. Normally I don't work out here at the kitchen table, so I don't even care.

**Marcel Santilli:** It looks like one kid, maybe more?

**Dan Li:** Two kids. One son, one daughter.

**Marcel Santilli:** That's awesome, man. Boy and girl—what ages?

**Dan Li:** Four-year-old son, two-year-old daughter.

**Marcel Santilli:** Oh, man, my daughter's two and a half. That's awesome. There's a lot of founders that end up starting companies right around when they have kids.

**Dan Li:** It's probably a good idea, but...

**Marcel Santilli:** What does your partner think?

**Dan Li:** She's always had a more stable job, so it worked out.

**Marcel Santilli:** From a minimization framework perspective, if you're going to do this thing, you have to do it. That's awesome, man.

**Marcel Santilli:** But super quick—Tyler did an amazing job summarizing things in our conversation. I totally agree with you. I used to be a heavy user of SlideShare. I used to consume knowledge mostly through SlideShare back in the day, which is insane to me that LinkedIn bought it and messed it up, I think?

**Dan Li:** Yeah, LinkedIn bought it and messed it up.

**Marcel Santilli:** Your insight on that front is spot on. You've already built these template pages, and we're really confident in our ability to build workflows that enable us to crank things out in a very high quality way. I think the two areas that would be super helpful to understand: one, what's an ideal case scenario where we could plug in? And two, what are the areas outside of workflow building that you'd want us to own?

**Marcel Santilli:** And the main reason I'm being fully transparent is we have an insane amount of demand, and we're about a month away from launching our platform more broadly to first customers. Because of that, we're more constrained on what we'd consider custom projects. It's not custom because of the workflows—it's custom because of all the other potential things we're doing. Between Lovable, Webflow, Brex, Ramp, and Xen Appier, Surge, and a few others, that's already too many custom ones. We're just trying to be super transparent about the process given our relationship.

**Dan Li:** For sure. Yeah, I think from our perspective, these programmatic pages would be the main thing we're interested in. On the editorial side, I don't know, Tyler, if you checked in on that—do we have good ideas there?

**Dan Li:** We're open to doing stuff. We just haven't had as many good ideas on the SEO side. On the programmatic side, we're happy to take stuff on. We've deployed some programmatic stuff through Vercel in the past, routed through CloudFlare proxy for certain subdomains or URL paths. If there's a version of the workflows where you can carve out what you've done for other folks...

**Dan Li:** The areas where we're looking for help is the workflow: how do we go from keyword research on what terms we're targeting to generating the page with nice content? I don't know how these pages have been set up in the past. Maybe low code or AI code gen using Vercel or other CMS. We have Webflow, but I don't know how well Webflow CMS would handle this. If there's a lightweight way for you to help us do what you've already built for other people, we can roll with that. But I don't really know what that looks like.

**Marcel Santilli:** When you're getting into thousands and thousands of pages, that over time might have more product-central integrations. For example, they give us access to their repo, and we do pull requests building directly into their templates library. There's a lot of features that already exist around remixing and things like that. We work within their stack. But the more we have to do design, templating, and pull requests, the less we can take on because that's not a standard thing. Everybody's repo is completely different. But you already have the page design, so ideally it's just the content itself—the words, the images. Where does that live? In a database somewhere?

**Dan Li:** Just in our CMS right now.

**Marcel Santilli:** Okay, so it's in a CMS. We can keep doing that in the meantime, knowing that over time, if you're getting to thousands and thousands of pages, that's going to have some limitations. For instance, if you have 5,000 pages, even though Webflow claims to be headless, they don't have super open API documentation on their CMS's headless capabilities. They've recently acquired or partnered with a massive database, so they'll have a Webflow Cloud thing comparable to Supabase. The experience is like Canva: when you're not logged in, you see items and assets; when you're logged in, you see the same but can use and remix things. You wouldn't be able to do that as easily down the line. But if part of the scope is us plugging into a Webflow collection that already has all this, mapping to the fields and creating workflows, then it's a matter of having experts in the loop doing calibration on what great looks like. That's what we do with strategy: figuring out all the categories, all the possible templates, and then creating the content. The only part I'd love to understand better is how you're doing the specific slides. Is there an API or way for us to programmatically generate that template within your platform? What's the process today going from input to output on a presentation template?

**Dan Li:** Today the process is manual inside our app, which is why we haven't scaled it. Now we have an API, so you can generate via the API. We spit out a .pptx file that's a link. We'd need to think about how to show those previews. We can use a Microsoft PowerPoint viewer—an embedded iframe—so people can flip through the deck. Obviously, that's not a great SEO experience because there's no content on the page about the actual slide content. But maybe that's okay given all the other stuff you'd write. We've also done manually taking PNG screenshots of every slide and putting them on the page in a lightbox. But I don't know if ideally we'd want the transcript of the entire slide deck on the page somehow. That would probably require some additional thinking. But the versions where we upload PNGs or a PowerPoint file both exist.

**Marcel Santilli:** I'll show you some of the stuff we've done and can do. This is all auto-generated with our workflows. We can auto-generate wording, cover images, screenshots. We have customers with image libraries we can pull from. Under the hood, it generates multiple image ideas, selects the best, generates a bunch of different images, uses a vision model to look at each one and select the best ones, and outputs only the best. So there are things we can do like that. Can you do a quick two-three minute demo now or later just so we understand a bit more? And we can assume the API allows you to do close to almost everything a user can do logged in. That would be super helpful.

**Dan Li:** Yeah, sure.

**Dan Li:** Thank you.

**Tyler Pavlas:** And Marcel, if you see any opportunity on the editorial side for Plus—like Dan mentioned, he's open-minded but didn't think there was much more juice to squeeze. He gave me the Magic Slides example: how are they gaining traction publishing 100 articles a day?

**Dan Li:** Just 100 articles of garbage content. The craziest thing is, on some search terms, you'll see two or three of those articles in the top 10. It's definitely not something we should replicate.

**Marcel Santilli:** Yeah, we'll get into that. The only reason I'm not focusing much on that is I'm extremely confident there are opportunities—things you should do even if you decide not to do it right now or not work with us. Editorial is not only an insurance policy for programmatic, but it also helps you build topical authority and relevance and allows you to go after longer-tail things. In AI search, AI visibility is becoming more important.

**Dan Li:** We've done a lot of low-hanging fruit on the editorial side: best-of listicles, versus content, alternatives-to content, and a million how-to articles about PowerPoint, Google Slides, presentations. We'd love to have you guys take a look at what could be next for us.

**Dan Li:** So basically, the tool works like this: you can say, "Create a pitch deck for a self-driving food truck that serves tacos," and it'll make the presentation for you. When you do this via the API, it automatically chooses a relevant template—for the food truck, something a little more futuristic-looking. In this view, you also see the outline before the entire presentation gets generated. But in the API, you can just have the entire thing.

**Marcel Santilli:** That's awesome. Through the API, can we shape the outline or modify it?

**Dan Li:** You can shape the outline just by changing the prompt. You can give a very detailed prompt, and it'll use that for the content. What comes out here is the actual PowerPoint file when you do it via the API. It's like a CloudFront link to the .pptx. This is using our default template—no special colors or backgrounds. We could turn this into 15 different images or just an image of the title page.

**Marcel Santilli:** Are you planning on supporting Google Slides too?

**Dan Li:** Yeah, it also supports Google Slides. It's the same experience in both.

**Marcel Santilli:** Because with Google Slides, we can embed it right away.

**Dan Li:** We can embed PowerPoint too.

**Dan Li:** This is an embedded PowerPoint.

**Dan Li:** I just don't know if this is good for SEO.

**Marcel Santilli:** It's okay as long as we have access. I think the easiest part would most likely be a PDF. But we need to research models' ability to take a PPTX file and understand every slide. As long as frontier models can handle it well, we can take that information and shape it so our workflows output it. There would be multiple workflows. We're not just outputting a prompt that says "create a beautiful website"—it's more detailed, down to brand elements.

**Dan Li:** Yeah, so we can definitely do this. This is probably the easiest thing to do right off the bat. We'd make it embeddable as a PowerPoint without needing any work to host or transform it. Then I think the things we'd need help with are writing the content on the page to describe the presentation and make it searchable.

**Marcel Santilli:** That seems pretty simple. How would the API work? It would essentially host the file and return a URL?

**Dan Li:** Yes.

**Marcel Santilli:** And that URL is hosted in your CDN or S3 bucket?

**Dan Li:** I think we might have to change things to make sure it's a permanent URL. Right now, it gets deleted after X hours or days. But we could do that, whatever needs to be done.

**Dan Li:** There are a couple different versions of this too. There's what I was telling Tyler: if this is less doable, the other version I'd be interested in is more like a SlideShare style site. We're happy to make that a separate page altogether, not in the Webflow CMS. We can do something else. I just want to give you all the context on what I think is easiest. But we're open to other ideas too.

**Marcel Santilli:** I'm searching something really quickly. For what you have right now, one thing that would make a big impact is this: if you search for "construction website templates," you notice listing pages rank highest. ThemeForest and Wix are both PLPs—you don't land on a specific item unless searching for that item specifically. TripAdvisor is a great example. Most of their traffic goes to listing pages, not individual hotel pages. What you're missing is the majority of potential in filtered views of your templates.

**Dan Li:** And that's where I'd want your SEO thinking. We have templates, which are different from example final output presentations—they're more generic. We do have it set up so you can pull the "professional" tag and everything comes up. We haven't made 500 different category pages, but we can add that. It's already part of the system.

**Marcel Santilli:** Yeah, that's perfect. Each filter option should be an indexable page itself. So "construction templates" is a different page that's also indexed. The experience for the user is seamless—looks like an app—but every single thing you click is an indexed page. That's the thing a lot of people mess up. It's like dealership plus modern tags. It would have to be more like the categories of things people are searching for. That's part of what we'd figure out during the sprint: do they search for "pitch decks" or "startup presentation templates" or the use case? That's definitely the core part we want help with. You're not creating one presentation per category—it's more like 5 to 50 per category, at least. For Webflow right now, they have "Made in Webflow," and they also have their new builder agent thing where they want to build starter kit apps. It's the same: the Webflow templates experience is a hybrid of those two things.

**Marcel Santilli:** So I'll do more digging on the editorial front. And apologies for not having done more of this, but how are you keeping that content fresh? You've done a ton of content, but how are you constantly refreshing, updating, improving it?

**Dan Li:** For top pages like "Best AI Presentation Makers," I go in manually and update it probably once a month or so. For how-to articles, we just let it sit—I don't think those ever get updated. For versus content, we update that every so often.

**Marcel Santilli:** Got it. I think the reason for the editorial is, you've done a lot, but 355 blogs for your category isn't crazy. Magic has 3,000 pages. The good news is the quality we can put out with the human in the loop is going to be way better than what they're already ranking for. Jason was at Bardeen AI and did this exact Zapier playbook. And then another area we could explore down the line is tools. Magic does a lot with tools—like PNG to SVG, SVG to PNG, JPEG to PNG. Sometimes the tools aren't super high-value, but they work.

**Dan Li:** One of our popular ones is Word to PPTX. And that converts pretty well.

**Marcel Santilli:** Or it's like grabbing a popular repo library and putting a UI on top of it.

**Dan Li:** Yeah, yeah. So definitely if there are ideas on those, we'd want to do as many as possible immediately. And even if you guys have the research, we're happy to do the work.

**Marcel Santilli:** I really want to do this. As long as you're okay with the fact that some engineering or design might be split a bit more—we might be constrained on putting a full-time design engineer on this. That way, our resources go toward strategy, which we can do really well, building workflows, and humans in the loop reviewing to make sure things are good. The only thing we can do is publish templates for you. The ceiling is higher with templates, but the time to get signals takes a lot longer. But editorial has low-hanging fruit we can go after left and right. And we can programmatically keep that content fresh. So even if the editorial scope is mostly refreshing existing content, as part of the strategy sprint, the MVP can be launching at least 20 new templates and getting that whole process down. Then refresh a set of pages you already have so you get a sense of quality. The biggest lift is coming up with examples. But as the library gets richer, we can take screenshots and use it in the content. You can link between the two.

**Dan Li:** That sounds great. Yeah, I like it.

**Marcel Santilli:** Cool. Let me reconnect with Tyler, and we'll get back to you super, super fast. Then we can pencil in a kickoff. Full transparency: our main concern is how much design engineering we need, because we're already under six different custom ones that are super intense on engineering and design resources. The more this can be standard—us not needing to redesign your entire site—that really helps.

**Dan Li:** Makes sense. We'd love to just get the next readout from you guys on what you would and wouldn't need to do. Because I just don't have a good sense of what's hard versus easy for you.

**Marcel Santilli:** Cool. That gave us all the context we needed. We'll get back to you by tomorrow.

**Dan Li:** Okay. Sounds great.

**Marcel Santilli:** Thanks, Dan. Talk soon, man.

**Dan Li:** Bye.
