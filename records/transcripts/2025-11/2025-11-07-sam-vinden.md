# Sam Vinden

<metadata>
date: 2025-11-07
time: 15:01 UTC
duration: 27 minutes
organizer: George Haikal
participants: George Haikal, Marcel Santilli, Sam Vinden
fathom_recording_id: 100034379
fathom_url: https://fathom.video/calls/466652418
share_url: https://fathom.video/share/nyE37zX2s3zJJwCahR4dxzoejECyEZHc
source: fathom
enriched_on: 2026-03-02 00:15 UTC
</metadata>

---

## Summary

George Haikal and Marcel Santilli onboarded Sam Vinden (Lovable's new Head of Growth) on GrowthX's organic growth strategy for Lovable. The strategy has two main pillars: a "Guides" blog with 5 articles/week and a "Templates" gallery starting with website templates at 5/week, targeting a TAM of 7-10M monthly US searches. Key risks identified include domain spoofing (users creating fake bank sites on Lovable subdomains) and 2,000 low-quality how-to pages that drive branded traffic but create poor user experience. Sam's immediate priority is reviewing GrowthX's Notion documentation before starting in December; longer term, the team explored leveraging Lovable's community for template and tutorial contributions.

---

## Context

Sam Vinden is joining Lovable as Head of Growth in December, having spent three years at Clio (fintech) scaling the growth marketing team from 5 to 30 people. This call was his first deep-dive into GrowthX's eight-week engagement with Lovable, which began in early September. George Haikal, a CMO with experience at IBM, HashiCorp, DeepGram, and Scale.ai, brought GrowthX's content marketing expertise into a full engagement after GrowthX grew from $0 to $13M in the past year. Marcel Santilli, GrowthX's founder, joined the call midway to add context on strategy and scaling challenges. The meeting took place on a Friday morning (7am San Francisco time, 3pm London time) as part of onboarding Sam before his December start.

---

## Relevance

**To GrowthX Delivery:**
- Lovable's community has tens of thousands of engaged users available as potential template/tutorial contributors — opens door to community-powered scaling beyond GrowthX's current 1 AI engineer + 1 design engineer capacity bottleneck on templates
- Domain spoofing risk is a critical site health issue requiring content moderation; redirecting poor-quality how-to pages may improve user experience but requires alignment with Lovable leadership on branded traffic trade-offs
- Dual-track execution (5 guides + 5 templates/week) is sustainable now; scaling to 50 guides/week (like Augment Code) is possible but requires trade-off with other client work

**To GrowthX Business Development:**
- Sam Vinden represents a strong hire signal for Lovable and suggests the client is taking organic growth seriously internally
- Account health: leadership alignment already achieved with Rachel and Cece on how-to page redirects; pending full strategy/execution alignment in December when Joanna (CEO) and Sam are both settled
- Expansion potential: Sam mentioned interest in tutorials and community programs; GrowthX's contributor network experience (1000+ contributors at HP) positions us well to help design and scale

**To CheckThat:**
- Marcel mentioned AI search visibility testing (Lovable base vs. Base 44, guides showing up on first page) — early positive signal for CheckThat value in monitoring AEO performance

---

## Overview

- **Dual-Track Strategy:** GrowthX is executing a dual-track strategy to drive organic traffic: a new "Guides" blog and a "Templates" gallery.
- **High-Impact Focus:** The strategy targets a Total Addressable Market (TAM) of 7–10M monthly US desktop searches, starting with high-volume website templates.
- **Critical Site Health Issue:** A site audit revealed users are creating spoofing sites (e.g., for banks), risking a domain-wide flag that would severely impact revenue.
- **Community-Powered Scaling:** Sam proposed leveraging Lovable's community for scaling, with Marcel suggesting templates and tutorials as the best starting points.

---

## Key Topics

### The Problem: Low Organic Traffic & Site Health Risks

  - **Poor-Quality "How-To" Content:**
      - An existing library of \~2,000 low-quality "how-to" pages creates a poor user experience.
      - These pages capture branded search traffic (e.g., "lovable support") but fail to provide useful answers.
      - **Decision:** Redirect pages for critical queries (like support) to the correct destinations to improve user experience.
  - **Domain Spoofing Risk:**
      - A technical SEO audit identified users creating spoofing sites (e.g., for banks) on Lovable subdomains.
      - **Risk:** If unaddressed, this could cause the entire `lovable.com` domain to be flagged as "suspicious," severely disrupting revenue.

### The Solution: Dual-Track Organic Growth Engine

  - **"Guides" Blog:**
      - A new blog built by GrowthX's design engineering team.
      - Content production is 5 articles/week, using AI-ready artifacts (e.g., a detailed feature matrix) to ensure accuracy and scale.
  - **"Templates" Gallery:**
      - **Strategy:** Start with website templates (7 published, 5/week) to target the highest-volume, lowest-complexity search opportunities.
      - **Vision:** Build a large library to enable Product Listing Pages (PLPs) for long-tail keywords (e.g., "construction website templates for general contractors"), mirroring the successful Wix model.

### Execution & Scaling

  - **Current Pace:** 5 guides and 5 templates per week.
  - **Scaling Bottleneck:** Template production is complex, requiring a full-time AI engineer and design engineer.
  - **GrowthX Capacity:** Can scale guide production to 50/week (based on experience with client Augment Code), but this requires a trade-off with other initiatives.
  - **Community Contributor Program:**
      - **Proposal (Sam):** Leverage Lovable's community for content creation.
      - **Potential Use Cases (Marcel):**
          - **Templates:** Low-effort way for the community to contribute.
          - **Tutorials:** A good fit for community-driven content.
          - **Guides:** Less suitable due to the high fact-checking and research effort required.

---

## Action Items

**Sam Vinden (Lovable)**
- Review GrowthX Notion re: Lovable guides/templates/audits/TAM/workflows before starting in December

**George Haikal (GrowthX)**
- Try Arc browser for 2 weeks

---

## Transcript

**George Haikal:** Can you hear me? Let's see, how about now?

**Sam Vinden:** Can you hear me now?

**George Haikal:** Yeah, yeah, yeah. Sometimes I have one monitor here where the voice comes through, and the display and audio from my laptop.

**Sam Vinden:** How are you doing?

**George Haikal:** Good, man, I'm good, it's good to meet you, how are you?

**Sam Vinden:** Yeah, good, thank you. It's a weird time because I haven't actually started Lovable yet, but I'm getting stuck in and finding my way around.

**George Haikal:** Yeah, yeah, it's good to be prepared.

**George Haikal:** I met with Joanna, who just joined earlier this week, and it was straight into the fire, as you would expect and probably want, right?

**George Haikal:** But smart to get ahead of it, for sure.

**Sam Vinden:** Yeah, definitely, definitely.

**Sam Vinden:** Nice, and how long has GrowthX been working with Lovable?

**George Haikal:** Week 8.

**Sam Vinden:** Okay, I was reading your Notion update earlier. What I'd love to hear is what the brief was, what the ask was, the work you've done so far, and what's coming up at a high level. And thanks for sharing the Notion — over the next few weeks before I join, I'll try to get stuck into as much of that as possible.

**George Haikal:** 100%, yeah.

**George Haikal:** And Marcel will join in a few minutes as well.

**George Haikal:** We can add some context, but I think what would be super helpful is maybe, could you give like 15, 20 second intro, just like maybe how you got here and then what you plan to like oversee and help with.

**George Haikal:** And there's just so many moving parts at Lovable, so I love hearing it from that.

**Sam Vinden:** Yeah, yeah. It's funny because from my perspective, we're still figuring that out as well.

**George Haikal:** Right.

**Sam Vinden:** Should I wait till Marcel joins to go through that?

**George Haikal:** Yeah, yeah. Honestly, you'll save yourself some time. I can get into the actual work and strategy and what's been done. And where are you based?

**George Haikal:** I'm based in San Francisco.

**Sam Vinden:** Ah, okay. Yeah, right there on the West coast.

**George Haikal:** Nice, yeah. What time is it here? It's 7am, so we're morning people. But it's always good to connect early in the morning when most people aren't up yet. And where are you?

**Sam Vinden:** I'm in London. I used to live in Vancouver, so I'm familiar with the West coast, albeit the colder part. I'll be traveling over to Stockholm fairly regularly, but I'm based in London.

**George Haikal:** How did you get connected to Lovable, or what made you interested in working there?

**Sam Vinden:** I had a conversation with Eleanor as a starting place, and that led from there.

**Sam Vinden:** Yeah, I'm currently finishing up my existing job at Clio, which is a fintech. It's interesting because all our users are based in the US — most people in the UK haven't heard of Clio, but people in the US know it. I spent the last three years there growing the growth marketing team from five people to around 30.

**George Haikal:** That's amazing, man.

**George Haikal:** Super exciting.

**George Haikal:** Well, I can get into, you know, kind of the what and I can actually, this will be cool because it took some work to get here.

**George Haikal:** So I'll start by showing you a few things as well.

**George Haikal:** Essentially, CC and Rachel and Marcel all knew each other prior, I think, in prior roles, but also the community out here in San Francisco is small, especially the CMO community.

**George Haikal:** So I was a prior CMO at IBM, HashiCorp, DeepGram, and then Scale.ai most recently.

**George Haikal:** And while at Scale.ai, GrowthX was a side business where I was teaching people through workshops how to build marketing workflows and streamline content creation.

**George Haikal:** And then that gained a ton of traction and he doubled down.

**George Haikal:** Long story short, 0 to 13 mil this year, which is super exciting.

**George Haikal:** Ton of work.

**George Haikal:** Obviously, so much learning.

**George Haikal:** And I joined, let's see, three months ago now.


**George Haikal:** It's been amazing.

**George Haikal:** It's been amazing.

**George Haikal:** I joined three months ago because I knew our CTO, Daniel, who was super impressive, managed product, had a product at IFTTT, which is basically like Zapier before Zapier.

**George Haikal:** And then, yeah, it's been a while.

**George Haikal:** I think I joined when we were at $4 million, and then in the last six or seven months, we grew to $13 million, and then plans to double and beyond.

**George Haikal:** Next year, and then keep going.

**George Haikal:** it's super exciting.

**George Haikal:** But that's how we got to Lovable.

**George Haikal:** And the idea for the engagement was our bread and butter is editorial content on web to drive organic traffic.

**George Haikal:** But our workflows are super powerful.

**George Haikal:** We can go into the hood and show you that we chose kind of a custom engagement here.

**George Haikal:** So the eight-week process is our strategy sprint where we understand the gaps, where we want to win, and where we can add the most value. Through that process, we identified two lanes that I'll pull up and show you. The first is editorial.

**George Haikal:** The first call in the morning, all my tabs from the late night prior are always open, it's hilarious.

**Sam Vinden:** Yeah.

**George Haikal:** Okay, here we go.

**Sam Vinden:** Have you tried Arc yet? The browser?

**George Haikal:** Arc? No, no, no.

**Sam Vinden:** I used to be the same with Tabzilla, but I switched to Arc about six months ago and it saved me.

**George Haikal:** Highly recommend?

**Sam Vinden:** I'd recommend trying it. If you do, you've got to stick with it for about two weeks and then you'll start to see the real value.

**George Haikal:** I love that, I love trying new things, I'll definitely take you up on it.

**George Haikal:** The first lane we chose was guides. It took us a while to get here for a few reasons, but essentially we duplicated the blog on Lovable's site.

**George Haikal:** We pulled in our design engineering team and then another engineer to kind of help and do all the work here.

**George Haikal:** So what you're seeing is the final product of a messy bunch of weeks.

**George Haikal:** And here is where we're posting blogs at scale.

**George Haikal:** All of these go through not only a massive, well-oiled content creation engine, but we also did two weeks of really intense strategy, identifying the opportunities and where we wanted to win.

**George Haikal:** And all of that was approved initially by CeCe and Rachel. Then on a weekly rolling basis, our new articles get re-approved as well with comments back and forth.

**George Haikal:** So at the beginning of this process, what we did is I met with five different teams over at Lovable.

**George Haikal:** Sebastian, who was running templates, CeCe and Rachel, Nadd and Felix at Design, Growth Hacker is the incumbent SEO agency, and then the paid as well.

**George Haikal:** Just to understand what everyone's working on and where we can actually add value. Through that we gained expertise on every piece of the business that we turned into AI workflow-ready artifacts.

**George Haikal:** For example, a product-specific artifact where we have a super-detailed feature matrix on Lovable that we can use in our comparison content. It's only when you get that level of specificity and expertise that you can create this type of content at scale.

**George Haikal:** And so that's the guides portion.

**George Haikal:** And the second piece, I see Marcel joining too.

**George Haikal:** So let me slow down.

**Marcel Santilli:** Hey, what's going on?

**George Haikal:** Hey, hey, how's it going?

**Marcel Santilli:** Sam, sorry. I'll turn on my camera in a minute. I'm driving and sorry to be late — it's early on a Friday so my schedule's thrown off.

**Sam Vinden:** No worries. Lovely to meet you, Marcel. We'll chat more soon.

**Marcel Santilli:** All right. Don't know if you can see me. There we go.

**George Haikal:** Amazing.

**George Haikal:** Amazing.

**George Haikal:** I'm just catching him up, Marcel, on the work that we've done so far, guides, and then moving over to templates.

**George Haikal:** So the second piece, Sam, are this template gallery.

**George Haikal:** Same process, two to three weeks of intense research on competitive analysis, where are the opportunities, what is the highest impact, lowest complexity.

**George Haikal:** Space that we can target, focused on what people are building with Lovable.

**George Haikal:** And so, you know, it goes, spans everything from websites, internal tools, SaaS, what we found through our research, and I can run you through the air tables and all the supporting research, was that websites have, and website templates have the highest amount of proven search traffic already, and the lowest complexity place to start.

**George Haikal:** So instead of starting with a gallery of dashboards and tools that have lower intent, lower search ball, or maybe higher intent, lower search ball.

**George Haikal:** We wanted to start with websites, and we were building out, and we already have seven published, five more weekly moving forward.

**George Haikal:** These really high-quality templates that are also optimized for search with explanations of the how and the what behind each one.

**George Haikal:** So not only can you go and get a head start on creating whatever you want to create where you came to Lovable for, and you can remix it in the app, but you also have a little education explanation and some SEO optimization on each template as well.

**George Haikal:** And so the idea here is we're adding a categories section up here, it'll be flat tagging system navigable across everything, starting with websites and different categories of websites, similar to how – I really like how Wix does theirs.

**George Haikal:** So portfolios, going to be one section, and then obviously it goes down to each individual one.

**George Haikal:** Starting with websites and then eventually moving towards the other higher intent categories once we get more user intent info from the team.

**Marcel Santilli:** Yeah, that makes sense.

**Sam Vinden:** Go on, Marcel.

**Marcel Santilli:** From our research, the PLPs — the listing pages — get the majority of traffic for Wix and others. It's not individual templates that get most traffic, but we need to start somewhere and build enough to add categories, tagging, and PLPs where most traffic can flow. We're very early, but it's huge — if you search "construction website templates" and then "construction website templates for general contractors," it's essentially infinite. We're starting with a couple, but once we have enough templates, it's easier to customize colors, images, messaging, app names, and so on. It won't be five per week forever — we're early and don't want to lose momentum. We're also building workflows under the hood that make working with Lovable's API easier, so design engineers reviewing this have to do very little to ship an app.

**Sam Vinden:** Yeah, it makes complete sense.

**Sam Vinden:** And I know you use Wix as an example there, but I'm very familiar with this from the Shopify side as well.

**Sam Vinden:** So, yeah, makes sense.

**George Haikal:** Those are the two main lanes. There's other work we've done — some site audits we're in the middle of.

**Marcel Santilli:** That might be worth bringing up. The main urgent finding was that some people are setting up spoofing sites on Lovable subdomains — like fake bank sites and things like that. There are a lot of those. If you don't address some level of content moderation, you could get the entire domain flagged as suspicious, which could disrupt revenue. UGC has its downsides. We need to be very careful with this. There are a few other things, but this was the most important one for you to be aware of.

**Sam Vinden:** That's helpful, thank you. So you're also looking at the technical SEO side of things?

**Marcel Santilli:** Yeah. The way to think about it is we have a capacity. We're trying to help you grow organically, increase visibility, improve AI search visibility, and drive traffic and signups.

**Marcel Santilli:** And we see like the health of your site and the user experience as one aspect of it.

**Marcel Santilli:** But we're not going to be like your website agency, but we will do the audits.

**Marcel Santilli:** If we find things, we're happy to fix it as long as it's within our, you know, our expertise.

**Marcel Santilli:** And so we just like to be an extension of the team as much as possible.

**Sam Vinden:** Brilliant.

**Sam Vinden:** Cool.

**Marcel Santilli:** Oh, and sorry, one more is there's this other agency.

**Marcel Santilli:** I don't know if HRCC told you about, but they did a bunch of the how-to stuff.

**Marcel Santilli:** So we haven't touched that.

**Marcel Santilli:** And one thing that I did recommend to the team.

**Marcel Santilli:** It's that like these how-to guys, like the content is really bad because it's just not good at all.

**Marcel Santilli:** And some of them, it's generating clicks, but it's generating branded clicks.

**Marcel Santilli:** So it's like lovable support.

**Marcel Santilli:** And then you get a how-to page that has like nothing to do with how to get help if you're getting stuck on something, you know.

**Marcel Santilli:** So it created bad user experience for lovable users.

**Marcel Santilli:** I don't think it's worth investing time completely redoing 2,000 pages one by one when that takes us away from guides and templates, which is where we recommend focusing. But we definitely need to address this. I don't think we have full alignment yet on whether to kill it and redirect because it's a bad experience but getting clicks. A lot of those clicks are branded — if someone's searching "lovable something," they'll find Lovable 100%. So it's really about trading off where they land, not net new traffic. But there are some non-branded ones. What I recommend is taking some like "customer support" and redirecting them to the right place as a middle ground.

**Sam Vinden:** Okay, cool. That decision's not made yet but it's something you've pushed for?

**George Haikal:** We're on the same page. I talked to Rachel and Cece this past Wednesday and they're on board. I also spoke with Vic at Growth Hackers about the redirect.

**Sam Vinden:** Have you set goals for what you want to achieve from the work Growth Hackers are doing?

**George Haikal:** The first eight weeks was a sprint where we figured out what works and how to set up structure, processes, and workflows to get the engine going. Production is five articles per week and five templates per week. We're doing that so we don't go too niche too quickly and can respond to early signals to double down on what's working.

**Marcel Santilli:** Let me paint the vision. The way we approach this is you got to get to quality activity first — getting things published. Then: is this getting indexed? Getting impressions? Getting clicks? Showing up in AI search? Yes — if you search "Lovable base" vs "Base 44," the guides show up on the first page. We're getting quality signals. But then we look at: are people staying on the page? Is content quality justified by this audience? Or is click-through rate or time on page completely different from the rest of the site? It's early to tell yet. Then it's about where to double down on volume. We go through cycles of enriching versus net new — it's a trade-off between upfront human review versus refresh and enrichment later. If you're doing a listicle with 17 apps, you can do 17 screenshots and add customer quotes, but that's more work. It's a trade-off between incremental quality and getting the page out, indexed, and getting clicks. Once it gets clicks, you optimize and constantly improve your page inventory. Right now we're ramping up.

**Marcel Santilli:** Yeah, like, so the way we kind of approach it, but open to ideas here or different thoughts is, like, you got to get to quality activity first, right, a.k.a.

**Marcel Santilli:** getting things out and publishing.

**Marcel Santilli:** And then the next thing is, like, is this getting indexed?

**Marcel Santilli:** Is it getting impressions?

**Marcel Santilli:** Is it getting clicks?

**Marcel Santilli:** Is this showing up in AI search, right?

**Marcel Santilli:** And it is, like, if you search for lovable base versus base 44, now the guides is cited.

**Marcel Santilli:** It's showing up in the first page.

**Marcel Santilli:** Obviously, there's a lot more work that goes into it.

**Marcel Santilli:** So we're getting quality signals.

**Marcel Santilli:** But then the next thing we look at is, okay, of those quality signals, are people actually staying on the page?

**Marcel Santilli:** Is the content quality there justified by this audience?

**Marcel Santilli:** Or is the click-through rate or time on page completely different from the rest of the site?

**Marcel Santilli:** Right now, it's a little earlier to tell that.

**Marcel Santilli:** And then it becomes just a matter of where do we want to double down on volume initially?

**Marcel Santilli:** And then we tend to go through these cycles on enriching versus net new, right?

**Marcel Santilli:** And the net new is ultimately about how much human review we want to put on that first shot versus how much do we want to do it on the refresh and enrichment phase, right?

**Marcel Santilli:** And so the way to kind of think about it is like, hey, if you're doing a listicle and there's 17 apps mentioned, and you try to do 17 screenshots and things like that, and you try to like add, you

**Marcel Santilli:** You lovable, like quotes from customers or something like that, then it's going to add a little bit more, right?

**Marcel Santilli:** And the more layers of reviews and things like that, it's kind of like a tradeoff between, you know, that incremental quality versus like getting the page out, getting it indexed, getting it to start getting clicks.

**Marcel Santilli:** And then once it starts to get clicks, you're like, okay, now let's go optimize and make it even better and constantly be optimizing like our inventory of pages, right?

**Marcel Santilli:** Like, so right now we're kind of in the ramp up phase.

**Marcel Santilli:** We did a TAM analysis — we can show you the work in Airtable where we aggregate it for guides and templates. It's about 7 to 10 million monthly searches in the US alone for desktop. That's the TAM of all the opportunities we identified — thousands of them across templates and guides. As we go through and get more reps in, we can double down and make projections for two or three months out. The tricky part is brands like Lovable that have done little content but have amazing brand and intent — hard to predict because there are branded variants on the long tail that mix in, which isn't bad. Early signals are very encouraging that pretty much anything we put out will do well. Now it's really a volume game — how do we crank volume and monitor.

**Sam Vinden:** Well, this is something I was going to ask is if we're seeing really good traction from this, can GrowthX scale like the amount that we're doing?

**Marcel Santilli:** The main bottleneck is we have one AI engineer and one full-time design engineer on templates — it's very complex. You're building five websites a week, and although we have automation, it's not five minutes. Editorial is different. With our scope, it's $25,000 a month. You're not our biggest customer, but it's significant. It's hard to add more capacity to guides because we took two extremely expensive US-based AI and design engineers from the product team to really crank this — it's a valuable engagement for us. Now we're figuring out how to scale templates to free up capacity.

**Marcel Santilli:** With customers like Augment Code, we've scaled to 50 guides a week, but there's diminishing return at a certain point. Then we flip to enrichment and find additional opportunities. With Lovable it's different — almost every topic is fair game, so the TAM of opportunities is massive. We're open to scaling. Rachel mentioned tutorials too.

**George Haikal:** It's a trade-off. If we open too many lanes, it's hard to focus.

**Marcel Santilli:** It's going to be hard to really triple down on one lane if we spread too thin. But we have capacity — we're 90 people, 50 dedicated to clients and the rest on infrastructure. We can scale.

**Sam Vinden:** Okay, that sounds great. I'm really interested in how we can utilize the Lovable community — tens of thousands of incredibly engaged people.

**Marcel Santilli:** I didn't get a chance to introduce my background, but at HP I built a contributor network site in DevOps and security that got to 1,000 contributors and about a million visitors a month organically. I'm super passionate about building community — we just launched ai-led-growth.com community for ourselves too. There are definitely a lot of things we could do to create a contributor program and reward people with credits or something like that.

**Marcel Santilli:** There's a trade-off with community — we've got to figure out where they add best value. With guides, we do a lot of fact-checking and deep research with competitive mentions, so editing community content could be as much effort as creating it. But there are places they can help — templates are obvious, or tutorials, or if they make a YouTube video about Lovable, they can submit and be featured.

**Sam Vinden:** Things like that could be cool to think about. Thank you so much for running me through everything. I'm going to dive into your Notion over the next couple weeks to get up to speed before I start in December. Any questions for me?

**Marcel Santilli:** Not on my end. I'm super excited. You're in London?

**Sam Vinden:** I'm going to be based in London but over in Stockholm every six weeks or so.

**Marcel Santilli:** I'll be over there whenever Cece and Rachel are. That's awesome. Excited to work together and dig into the Notion. It's only eight weeks of work so far, but hopefully you see how much progress we made. When new stakeholders come in, we're always trying to build a relationship. I was a CMO for 10 years and worked with many bad agencies, so we try to show early that we're different and collaborative.

**Sam Vinden:** I appreciate that. I was telling George before you joined — Joanna just joined, plus Cece and Rachel are in the account. I want to make sure there aren't too many cooks in the kitchen. In December we'll figure out who's taking responsibility for what forward. Conversations then.

**Marcel Santilli:** Sounds awesome. Thank you, I appreciate it. Thanks for coming on early, guys. Speak soon. Bye.
