# Webflow <> GrowthX Weekly Sync

<metadata>
date: 2025-08-27
time: 17:31 UTC
duration: 28 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Sydney Go (GrowthX), Luke Stahl (Webflow), Colin Lateano (Webflow), Michael Huard (Webflow), Kelly We (Webflow), Meg Murray (Webflow), Kirat Chhina (Webflow), Vivian Hoang (Webflow), Anushri Gupta (Webflow), Darin LaFramboise (Webflow), Rachel Wolan (Webflow)
fathom_recording_id: 83340525
fathom_url: https://fathom.video/calls/391735273
share_url: https://fathom.video/share/hRYETYqEEpE15UQ55vmt5zygePgy2p-M
source: fathom
enriched_on: 2025-03-03 17:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow synced on integration management, editorial content strategy, and content accuracy concerns. Webflow is handling ~400 integrations with 20-30 added weekly and is exploring community-submission workflows, while GrowthX is developing supporting code examples and documentation. The team discussed how to balance content velocity with competitive accuracy when AI-generated listicles reference other CMS platforms, with Luke pushing to align on Webflow's competitive posture before publishing and to delay listicles until after Webflow Conf when new AI features launch.

---

## Context

This is an ongoing weekly sync between Webflow and GrowthX as part of their content marketing engagement. Webflow is a no-code platform for building websites and applications, and GrowthX handles their B2B content strategy and SEO deliverables. The relationship includes multiple work streams: managing integrations, creating editorial content, building example applications for new product launches, and ensuring content accuracy and brand positioning. Luke Stahl represents Webflow's product marketing team and is deeply involved in positioning strategy, particularly around upcoming AI announcements at Webflow Conf (scheduled for ~3 weeks out). Jason Gong runs content operations at GrowthX and oversees the day-to-day execution and tooling for generating and publishing content.

---

## Relevance

**To GrowthX Delivery:**
- AI accuracy in listicles is a core concern when referencing competitors — need to establish research constraints (official docs only vs. third-party sites like G2/Reddit) to avoid publishing inaccurate information
- Integration guides require stricter sourcing rules to prevent "Zapier slop" — GrowthX has implemented code-level citation validation to ensure only trusted sources are used
- Example applications for new product launches require product expertise, clean code, and ongoing maintenance — client capability assessment needed to determine if GrowthX can deliver at scale
- Webflow's AI product announcements at Webflow Conf (3 weeks out) will reshape positioning — listicles and CMS content should be delayed until GrowthX can incorporate new AI messaging

**To GrowthX Business Development:**
- Webflow is expanding integrations from ~400 to scale with 20-30 per week, with potential community submissions requiring review process (expansion signal)
- Editorial content pipeline is steady (composable commerce article in design), but velocity depends on design bandwidth and competitive positioning alignment
- Account shows healthy engagement: multiple stakeholders (Luke on PMM side, Colin on product/dev, Michael on editorial), regular weekly syncs, collaborative problem-solving on content strategy

---

## Overview

- Webflow maintains ~400 integrations with 20-30 added weekly; exploring community submission workflows with review processes
- GrowthX is evaluating capacity to create clonable example repos for new product launches (code components) — requires product expertise, clean code, and maintenance commitment
- Composable commerce article is in design phase; editorial team is capacity-constrained during Webflow Conf prep cycle
- Listicle content accuracy concerns center on sourcing method (official docs only vs. third-party review sites); Luke flagging that competitive comparisons require alignment on Webflow's vetting standards
- Webflow Conf (3 weeks out) will feature major AI announcements (AI site builder exiting beta, code generation capabilities) — team agreed listicles should incorporate AI messaging and potentially delay publication until post-conference when full positioning is clear

---

## Key Topics

### Integration Progress and Community Involvement

  - Approximately 400 total integrations, with 20-30 new ones added weekly
  - Potential for community-submitted integrations, requiring a review process
  - Discussion on who should review community submissions (Vic, Colin, or Alan's team)

### New Product Documentation and Examples

  - Need for clonable repo examples for new products like code components
  - Challenges: requires product understanding, clean code, and ongoing maintenance
  - Consideration of GrowthX's potential involvement in creating these examples

### Editorial Content and AI Positioning

  - First article (on composable commerce) is with Design for finalization
  - Suggestion to incorporate AI mentions in listicles, especially after Webflow Conf announcements
  - Upcoming AI releases: AI site builder coming out of beta, code gen capabilities

### Content Accuracy and Competitive Information

  - Concerns raised about the accuracy of information in listicles, especially regarding competitors
  - Discussion on AI's information sourcing and potential limitations
  - Proposal to restrict research to official company websites and developer documentation
  - Consideration of simplifying content to focus on verified information

### API and Integration Guides

  - Mention of an API key issue that needs resolution with Colin
  - Integration guides progressing well, with strict sourcing to ensure accuracy

---

## Action Items

**Luke Stahl (Webflow)**
- Review API-first article for positioning and accuracy

- Get headless CMS source of truth document from Joe, share with Jason Gong (GrowthX)

- Discuss competitive content concerns with Colin Lateano (Webflow) and manager in 1:1 meetings

- Re-review listicles, highlight which ones are challenging from a competitive standpoint

**Jason Gong (GrowthX)**
- Investigate listicle creation process and research constraints to restrict sources to official docs only

- Determine GrowthX capacity to create clonable code component examples and provide feedback to Colin

---

## Transcript

**Jason Gong:** Cool, and then Colin said he was at a conference, so I guess we can just get started and then whenever he joins, does that work?

**Luke Stahl:** Yeah, yeah, yeah, that sounds good.

**Jason Gong:** Let's see, so I'll say not a lot to update on the integration stuff, that's just going now.

**Jason Gong:** Our process there is basically like we make it and then we just publish it for the most part.

**Jason Gong:** But if you check the Airtable, there's a spot that highlights all the ones that you guys haven't looked at if you do want to go back and look at them.

**Jason Gong:** But we heavily review them internally.

**Jason Gong:** And then there's constantly new ones being worked on and added.

**Jason Gong:** But I can't remember, Sydney, how many there are in total.

**Jason Gong:** I think there's still maybe 400 in total.

**Jason Gong:** So we're basically going through them like 20-ish, 20 to 30, or maybe like 20-ish a week.

**Jason Gong:** So that'll just be kind of constantly ongoing.

**Jason Gong:** Another thread there was Vic had like one case where it seemed like an app maker wanted to create one themselves.

**Jason Gong:** we created like a little template for them.

**Jason Gong:** And then it seems like a cool like community thing.

**Jason Gong:** So maybe at some point that turns into like a community submission thing perhaps.

**Luke Stahl:** Do you know, did Vic, did they talk about, I just missed it, but was there a conversation around like who reviews those?

**Luke Stahl:** Community submissions, just because it's like, we want to make sure that they're not posting links that are, you know, 404s or just, you know, they can't post whatever and it just get there.

**Luke Stahl:** So I'm assuming there's some sort of like, there'll be an approval process or something in place to make sure whatever they submit is reviewed.

**Luke Stahl:** I don't, I don't know if that was meant to be something Vic was going to review or Colin before it gets to the integration pages, but I think those ones specifically need additional eyes on it if they're coming from community.

**Luke Stahl:** It's great if we have community doing it, but we can't just like publish without review.

**Jason Gong:** I think for that one, we'll just start a thread once we get the draft back.

**Jason Gong:** I think that one, I mean, we can definitely review, but I guess, yeah, it'd be good to understand from Vic too, like what, like, it sounds like this one's a relatively small app maker.

**Jason Gong:** So I feel like we could probably do what we want, but maybe, maybe one day Stripe things us, you know, they want to like make some edits.

**Jason Gong:** Their page and that one probably requires like someone from your side to like, it's more like a relationship or something.

**Jason Gong:** Yeah.

**Jason Gong:** Cool.

**Jason Gong:** Yeah.

**Jason Gong:** I mean, well, I guess the plan there is like when that draft comes in, can just look at it together.

**Jason Gong:** I mean, there's definitely things we can just flag for sure.

**Luke Stahl:** That might also be part of Alan's idea around it too — someone on his team, like with the integration pages, should be giving them a look over before they get published. We would think we need to follow that similar process for the community ones too.

**Jason Gong:** That sounds right.

**Jason Gong:** So yeah, that's integrations.

**Jason Gong:** And then the integration docs, we're still waiting for Colin to review kind of our initial one.

**Jason Gong:** That one is blocking kind of us messing a bunch of time to like make the workflow that creates those at scale.

**Jason Gong:** So I'll just flag it again for him.

**Jason Gong:** And then Colin brought up.

**Jason Gong:** What kind of, guess, new products you guys are launching slash prioritizing?

**Luke Stahl:** Yeah, this stems from, because I'm working on the code component launch as well, this stems from wanting to be able to create more use case examples.

**Luke Stahl:** So, you know, obviously our DevRel team is smaller, engineering is backlogged on a number of different things.

**Luke Stahl:** So it's like, how could we create like a clonable repo that someone can get into and, you know, clone and then test out our code components or anything along those lines?

**Luke Stahl:** So I know Vic is working on some of them, but it's also like a capacity thing.

**Luke Stahl:** So it's like, does your team have the ability to maybe support?

**Luke Stahl:** I think that's where Colin was going with that, because we're going to have additional releases once Webflow Comp comes out.

**Luke Stahl:** And the idea is to have more example apps or, you know, not.

**Luke Stahl:** That's massive in scale, but just more example apps for our developer audience to be able to go in and test out.

**Luke Stahl:** They wouldn't require the same level of format as a blog post. I think what Colin was saying was more in line with how you're doing the integrations — something repeatable. These are the steps, but then having someone with that kind of expertise to do it and then review it on our end to make sure it actually works.

**Luke Stahl:** So like, most likely it'll live here under an examples.

**Luke Stahl:** And also actually there's, there's a tab above, like right now you're in the guides tab.

**Luke Stahl:** There's an example right there.

**Luke Stahl:** I think it would live within here and it would be tag code components.

**Jason Gong:** I think that context is helpful. This is pretty different from stuff we've done. It would be good for us to help if you think this is something you'll always keep doing. But if it's just getting us to do 10, that's probably not the best use of our time to learn all of this. We would almost just write them manually because it's not worth spending the engineering time to build something repeatable.

**Luke Stahl:** I think it's something to kind of think about and get back to Colin on because those example apps are not as easy either because it does require a level of understanding of our product.

**Luke Stahl:** It does require creating clean code and, and having stuff that, you know, can be maintained as well, you know, and it's, that's, that's the other thing.

**Luke Stahl:** Once it's there, who maintains it when changes need be and all that other stuff.

**Luke Stahl:** And so I think there's more to it that needs to be kind of fleshed out here.

**Luke Stahl:** So, yeah, but I think Colin brought it up as a let's think about it type ordeal.

**Luke Stahl:** Okay.

**Jason Gong:** Yeah, well, I mean, I pinged with some questions in the thread, but I'll add some more context from this call.

**Jason Gong:** We can keep chatting there.

**Jason Gong:** Cool.

**Jason Gong:** And then let's see, for editorial stuff, I think Michael is reviewing that first article.

**Jason Gong:** Yeah, that one, he's already submitted over to Design.

**Luke Stahl:** So the composable one, I got back to him on like the diagrams versus like the inspirational image asset.

**Luke Stahl:** So I think that's just with Design to kind of figure out how to create the additional mermaid diagrams.

**Luke Stahl:** And they're just, again, really backed up.

**Luke Stahl:** It's Webflow Conf time.

**Luke Stahl:** So when they can get to it, they'll get to it.

**Luke Stahl:** I haven't reviewed the API-first article yet — just as a heads up, I'll get into that. But the top CMS one, Sydney, this was the call-out I put in there today. I think you've got the right players in there now. What I'm thinking about now is especially with Webflow Conf coming out — we're going to be dropping a lot of things around AI, and AI being such a hot topic.

**Luke Stahl:** That should almost be like its own little line item within those, like how these companies are using AI and then how we are using AI.

**Luke Stahl:** And so it's like, I think some of these listicles would be better prioritized to launch after Webflow comp when you have all of our releases and can start linking to things like Project Orion, our, you know, our co-gen app that we're building and all those other things that are going to be in play.

**Luke Stahl:** So I think it's on the right track.

**Luke Stahl:** It's just, it would change.

**Luke Stahl:** Like if we published it tomorrow, it would be drastically out of date and need to be revised.

**Luke Stahl:** And we would have people knock on our door.

**Luke Stahl:** This doesn't paint us in the right light or anything of the sort because we're not talking about X, Y, and Z things.

**Luke Stahl:** So that's what I just wanted to make note of that I started thinking about today.

**Luke Stahl:** So there's just kind of a narrative shift about Webflow right now, and it's moving into that AI-driven kind of space.

**Luke Stahl:** I think we need to reflect that when we're talking about us in these listicles, too.

**Jason Gong:** So most of the stuff we're publishing are listicles.

**Jason Gong:** So would you say that applies for, I guess, most things where we're going to talk about Webflow's product, like to maybe wait a little bit on those?

**Luke Stahl:** I mean, it depends on like what products you're talking about, but I mean, our AI is hitting a lot of them.

**Luke Stahl:** So even if you talk about personalization or localization, our AI is going to be a part of that.

**Luke Stahl:** You know, like our AI is moving from beta capabilities to no longer being in beta.

**Luke Stahl:** We have releases coming that will hit the AI situation — not only our AI site builder, but how we do code gen capabilities and other things.

**Luke Stahl:** So there's just a lot that's going to be in the mix in like three weeks.

**Luke Stahl:** And so that would obviously change some of the take on what we say about us.

**Luke Stahl:** As someone who worked at Builder, when I read their comparison, Builder looks fantastic. Their cons are just that they innovate a lot, which isn't that big of a con. They're all about AI and doing these things. We're not talking about AI ourselves, so we kind of didn't do ourselves a good service with that part.

**Jason Gong:** The ones that are closer to AI, we should definitely wait. Can you still review this one? If it falls in the same category or we could publish it, that would help us decide whether to pause or prioritize.

**Jason Gong:** Yeah, I mean, this one definitely has a different take because you're focusing more on APIs, right?

**Luke Stahl:** So, I mean, that's a bit different versus the other one you're talking holistically as a platform, right?

**Luke Stahl:** You're saying like these platforms, these CMS platforms, these are the top, blah, blah, blah.

**Luke Stahl:** And then we don't speak to our AI offerings.

**Luke Stahl:** And it's just, I don't know if that hurts us, but I'll give the API first one a re-review.

**Luke Stahl:** That's kind of the downside to listicles — you're going to have a lot of eyeballs on them, and if you're not using the messaging correctly about us as a platform, that's where we get into trouble. I almost wonder if I need to pull Michael in for some of these listicles too, to get his thoughts not just from the technical standpoint, but on how we represent ourselves.

**Jason Gong:** That would help. I think it goes back to the product marketing doc you shared — things like that help us make sure we talk about Webflow properly.

**Luke Stahl:** I can give over the headless CMS source of truth document now — it was finalized last week. Let me ping Joe and get that to you so you can understand how we speak about ourselves around the headless CMS nature.

**Jason Gong:** But it sounds like that one's going to publishing, so that's good.

**Jason Gong:** So we could probably do a few more there in the interim. The composable one — that's more informational, SEO-type stuff.

**Luke Stahl:** When it's more competitive in nature, like the top CMS platforms piece, I wonder how your AI is pulling all of that data. Are you doing deep research into their websites or using third-party websites? How do you know these statements are factual across all these different providers? We added StoryBlock and Contentful into the mix. I was at Contentful, so I'm wondering how your AI pulled this stuff and how it's vetted. Is it pulling from third-party sites or only looking at their platform product pages and developer documentation? I'm just trying to see how we could avoid it pulling incorrect information.

**Jason Gong:** It's a good question.

**Jason Gong:** I think for Listicles, we definitely like prioritize the company's website itself.

**Jason Gong:** It pulls from G2, Trustpilot, and Reddit threads.

**Luke Stahl:** The problem with G2 and those third parties is people post them and never update them. I used to manage software review sites, and I'd have to keep them up to date. But you know months will go by without updates even as new features roll out. That's the hard thing about competitive pieces. When it's a "top platforms" piece, I think of that as competitive — breaking down pros and cons. You show us in the mix without saying one is best, just that these are the top and what they offer. That's where the accuracy question comes in.

**Jason Gong:** You guys scrutinize this more than our other customers. Maybe we could only cite the official website. If that means we say a little less for some tools, that is what it is. We're often trying to say a lot about each one.

**Jason Gong:** To say some cons, maybe we're looking at a Reddit thread where someone was complaining. But there's no way to really verify what they're saying. One thing we could do is make the research part more restrictive. The outcome is it'll probably be more up to date and accurate. But we might not be able to say many cons, so maybe we make the section smaller and just comment on the product in general. We can come back and revise it later or get a real developer to do it.

**Luke Stahl:** That's something to think about. I'm working with the solutions team to build out a competitive GPT. I initially erred on the side of always searching the web, but that created issues. I had to redefine it to only look at competitor platform pages, product pages, and developer documentation. It took confining my web search capability to get it right. I gave it all our competitor context and customer quotes to make it work well. Even then, it operates about 80% — 20% still requires human review. It's made me wonder how your AI is pulling information and where it's sourcing from.

**Jason Gong:** For listicles, honestly, most of our customers don't care as much about how completely verifiable and accurate everything is. Right now it's probably pulling from the usual places. But what you're describing was a huge issue with our integration guides — if you start trusting Google, it pulls in all this Zapier slop. We have so much stuff, and it's hard to keep it out unless you're really strict. We actually have a code step that checks every individual citation because all the LLMs don't do it reliably. If you say "only trust official docs," it doesn't do that consistently. Perplexity lets you restrict on domain but not subdomain and path. ChatGPT does site searches like "paypal.com/whatever" but doesn't do it consistently either. Our solution was to have a code step that validated every citation.

**Luke Stahl:** I'll make that a point for my one-on-one with Colin tomorrow. I don't know if I'm muddying the waters by showing concern for these things. I'm still new — I don't know what our stance is on publishing a blog that talks about competitors. If we post it and someone's knocking on the door saying "Luke, did you vet every single one of these?" I'd say the AI went through and did its thing and I gave feedback, but I don't know it to be 100% accurate. That's what I'm cautious about.

**Luke Stahl:** It comes down to what we want to produce and publish and how many eyeballs will be on it. I think it's worth talking to my manager one-on-one since he's our person for competitive intel from a PMM standpoint. He'll have thoughts on a piece like that.

**Jason Gong:** That would be good to align on. Our customers have different bars for what they're willing to say. Surge AI, for example, is the Scale AI competitor in data labeling — they're barely willing to say anything unless a researcher has groomed it with a fine-tooth comb. Then we have billion-dollar companies who just say "do whatever you want, publish, and we'll revise later." If you can tell me where you want to stand, we can adjust accordingly.

**Luke Stahl:** I don't want to be a roadblock. I'm just providing feedback on who might be involved and what vetting we do so I can speak to it. At this point, if we publish non-integration blog content, they'll ask "Luke, what did you do to vet this?" That's where I want to be prepared. One solution is to say less but still publish, then revise once we see it's driving traffic. Prismic does a lot of this — their blog is never meaty, and that's what I'd imagine would work. Maybe when we get into pros and cons, we were getting too deep in the weeds.

**Luke Stahl:** Maybe it needs to be simplified more. We have to watch how we speak about ourselves — the terminology around "API first" and "headless" needs to be cautious. We're gearing up to change how we speak about ourselves in this AI positioning going forward. Once we have that, Michael can share it with you, and it's just a matter of revising. I don't think this should absolutely stop publishing, but the AI aspect is cool to weigh in on. What are we doing with AI? People vet products on that now. You do a CMS — CMS has been around forever. What are you doing with AI? That's what people want to know.

**Jason Gong:** Next steps — I'm going to look into how we're creating these and pull that out to see what we can do. If you have more guidance on what you can or can't say, we can converge those things.

**Luke Stahl:** I'll get you the headless source of truth document — that will point us in the right direction for how we speak about ourselves as a headless platform. You'll have that going forward. AI stuff is still in the works, but it's coming together for Webflow Conf.

**Jason Gong:** Sounds good.

**Jason Gong:** Um, let's see.

**Jason Gong:** Anything else? One thing — Colin gave us an API key and our engineer had trouble with it. It's probably just a permission issue. That's the only thing we're waiting on from you guys. We have integrations, and guides are probably the next repeatable thing — we can do four or five a week. Informational SEO content is in a good spot. Listicles we covered this whole meeting. We have our lanes where we're already publishing — that's the main focus. Then we'll try to get some of the other ones running.

**Luke Stahl:** One thing to think about — I'm writing a blog for Joe and the team about "developers love headless until they don't." It's not an attack on Contentful or competitors — just talking about headless in general. I think if we do listicles focused on topics like that — headless, features — you could speak to it and tie in what we do toward the end. I'll re-review some of the listicles and highlight which ones are challenging from a competitive perspective. Topic-based, informational pieces like the composable one work really well from an SEO perspective and are easier to push out.

**Jason Gong:** I'm trying to find, and maybe Sydney, or if you have a link to it already, that's great, but I'm trying to find that list.

**Jason Gong:** Yeah.

**Jason Gong:** If you want to, when you send over the notes, you just want to resend the list for the listicles.

**Luke Stahl:** I'll go through them again — there might be ones that get into competitive weeds where we rethink it and focus on others instead.

**Jason Gong:** I want to do the same for informational stuff. Sydney, what state is that in? Do we have approved ones or do we just have the composable commerce one? We don't have a backlog or roadmap of other articles yet.

**Sydney Go:** We have the one for now, and I can send you the rest in a bit. I just have to transfer it to the sheet we have.

**Jason Gong:** That would be good too — get Luke to see which ones look good. I think Luke has context for what would run into "we're not ready to talk about that yet" territory.

**Luke Stahl:** Yeah, I'm thinking about what I would put out as SEO articles versus what a PMM would put out around competitive stuff. That's where I'm trying to push you toward pieces that will be faster to publish.

**Jason Gong:** Sounds good. All right, appreciate your time, Luke.

**Luke Stahl:** Catch you later.
