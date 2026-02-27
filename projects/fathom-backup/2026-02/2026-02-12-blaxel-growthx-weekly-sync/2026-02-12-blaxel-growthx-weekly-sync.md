# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-12
time: 19:59 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants:
  - Paul Sinaï (Blaxel, CEO)
  - Aida Knezevic (GrowthX, Content Lead)
  - Nicolas Lecomte (Blaxel, VP Growth & Product)
  - Carly Piekos (GrowthX, AI Search Lead)
  - William Leborgne (GrowthX)
  - Kathy Lam (GrowthX)
fathom_recording_id: 122090601
fathom_url: https://fathom.video/calls/564313439
share_url: https://fathom.video/share/M2DPsgpXwjjT6b7yBCX3XuDgLXxnzCj9
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX delivered V3 of its agentic article generation pipeline with improved quality controls and product alignment, addressing factual errors in previous content. Blaxel's AI search visibility (1.5%) remains flat; the team will analyze tracked prompts to remove noise and focus on emerging keywords like "persistent sandboxes" and "agent context persistence" ahead of the Agent Drive feature launch. All active action items assigned with clear deliverables.

---

## Context

GrowthX and Blaxel are in an intensive content partnership focused on AI search visibility. After discovering quality issues in the first generation of Blaxel articles (factual errors about GPU capabilities and product scope), GrowthX invested in a completely new pipeline architecture that fact-checks all claims against Blaxel's product matrix and filters out banned phrases and corporate language.

Blaxel's primary growth lever is not traditional SEO but dominance in AI search (ChatGPT, Claude, Cursor). Paul and Nicolas emphasized that users are asking these tools directly for "persistent sandboxes" and "agent context persistence"—emerging keywords driven by recent AI papers—and Blaxel is positioned to own this space with its upcoming Agent Drive feature. The team is balancing bottom-of-funnel content (comparisons, product listicles) with educational posts, while monitoring visibility metrics (currently 1.5%, vs. competitor E2B at 7.1%).

---

## Relevance

- **Content Ops**: GrowthX pipeline V3 with EXA research, product matrix integration, and quality gates; 5 new drafts queued, 3 under revision.
- **AI Search Strategy**: Blaxel pursuing AI visibility over SEO; targeting "persistent sandboxes," "stateful sandboxes," "agent context persistence"; currently rank #1–3 for "persistent sandboxes" on Google.
- **Performance & Metrics**: "Code Sandbox alternative" article performing well; Google Search Console and PostHog analytics confirm traffic growth week-over-week.
- **Feature Alignment**: Agent Drive (Google Drive for AI agents) launching soon; enables positioning on storage/persistence/context keywords.
- **Prompt Optimization**: CheckThat tracking ~7% broader prompts; plan to audit and remove low-value keywords to improve visibility metric signal-to-noise ratio.
- **Cross-Org Collaboration**: Blaxel providing public docs (Mintlify/GitHub) and support KB (support.blaxel.ai, Pylon) for integration into GrowthX pipeline.

---

## Overview

- **New Content Pipeline:** GrowthX launched V3 of its article pipeline to fix quality issues (e.g., inaccurate product info), ensuring content is now fact-checked against a product feature matrix.
- **AI Search Is Top Priority:** Blaxel's primary goal is to dominate AI search (via ChatGPT, Claude, etc.), not traditional SEO. The immediate focus is on keywords like "persistent sandboxes" and "agent context persistence."
- **Check That Performance:** Blaxel's 1.5% visibility is flat. The next step is to analyze the tracked prompts to remove irrelevant ones that dilute the data and skew the performance metric.
- **New Content Focus:** The strategy will shift to bottom-of-funnel content (product listicles, comparisons) and educational posts on key persistence concepts, leveraging Blaxel's upcoming "Agent Drive" feature.

---

## Key Topics

### Content Pipeline & Quality Control

  - **Problem:** Previous articles required full rewrites due to factual errors (e.g., incorrect GPU capabilities), indicating a flawed content pipeline.
  - **Solution:** GrowthX launched V3 of its agentic article generation pipeline to improve quality and accuracy.
      - **Researcher:** Now uses EXA (vs. baseline Tavilli) for better research on technical topics.
      - **Fact-Checking:** Incorporates Blaxel's product feature matrix during research to ensure content aligns with product capabilities.
      - **Quality Gates:** Articles are graded against a rule set to prevent errors like unsourced claims or patronizing links.
  - **New Content Sources:** Blaxel will provide its documentation and knowledge base to enrich the AI research process.
      - **Documentation:** Public GitHub repo via Mintlify.
      - **Knowledge Base:** `support.blaxel.ai` (built on Pylon).

### AI Search Performance & Strategy

  - **Context:** Blaxel's target audience uses AI tools (ChatGPT, Claude, Cursor) to find solutions, making AI search visibility the top priority.
  - **Check That Performance:** Blaxel's visibility is 1.5% (vs. competitor E2B's 7.1%) and has been flat.
      - **Hypothesis:** The performance metric is skewed by tracking too many broad, irrelevant prompts.
      - **Action:** GrowthX will export and analyze the prompt list to identify and remove low-value queries.
  - **Keyword Focus:** The strategy will target keywords reflecting high-intent user needs, even if they lack traditional search volume.
      - **Keywords:** "persistent sandboxes," "stateful sandboxes," "agent context persistence," "storage."
      - **Rationale:** These terms are emerging in user conversations and social posts, driven by papers like the recent one from Anthropic on LLMs and tools.
      - **Blaxel's Advantage:** The upcoming "Agent Drive" feature (a Google Drive for AI agents) directly addresses these persistence needs.

### Content Delivery & Performance

  - **Delivery Pace:** The pace of new articles slowed while GrowthX built the new pipeline.
      - **Catch-up:** 5 new drafts are in the editing queue for delivery today/tomorrow.
      - **Revisions:** 3 articles are finalizing revisions; Natalie will request final sign-off.
  - **Article Performance:**
      - The "Code Sandbox alternative" article is performing well, driving clicks and ranking high in Google Search Console.
      - Blaxel's own analytics (Posthog) confirm this article is getting the most traffic.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Integrate Blaxel docs (GitHub) and KB (support.blaxel.ai) into article pipeline
- Consult Kyle & Talal re: AI search visibility targets; prep for next sync w/ Paul & Nico

**Nicolas Lecomte (Blaxel)**
- Convert Content Ideas doc to table (idea, URL, date)
- Build MVP CTA banner w/ PostHog tracking; notify Aida when live

**Carly Piekos (GrowthX)**
- Export and review CheckThat prompts; remove irrelevant; identify gaps

---

## Transcript

**Aida Knezevic:** All right, well, I wanted to get us started with some pipeline updates because the last round of articles that we delivered had a couple that had to be completely rewritten. That's always a red flag for us because it means the pipeline isn't doing what it's supposed to be doing. So we spent some time developing a brand new pipeline and adding additional steps to the workflow to prevent specific issues from happening again. For example, the new pipeline should no longer suggest that Blaxel can do GPU compute or model training. Moving forward, it should also reference all Blaxel products relevant to the specific topic, not just sandboxes. We revised the article generation pipeline to incorporate the product feature matrix during the research step, which allows the researcher to find information relevant to Blaxel's benefits, not just general information on the topic.

**Aida Knezevic:** So to show you what that looks like in practice, this is V3 of the agentic article generation pipeline. We're using EXA as a researcher. EXA is the most advanced researcher we use for technical topics. Typically, we use Tavilli as the baseline and switch to EXA when needed.

**Paul Sinaï:** Are you connected with our documentation and knowledge base?

**Paul Sinaï:** We have both. Our documentation uses Mintlify, which is plugged into our public GitHub repository, so you can access the entire documentation in Markdown format, which works well with agents. For support, we're using Pylon with a website at support.blaxel.ai that contains workarounds and guides not in the main documentation but still relevant to how customers use and leverage the product.

**Aida Knezevic:** I think we can definitely incorporate the documentation and knowledge base as a separate step. This rule list is mapped to feedback from your review team—Vikram, Nicolas, or yourself—covering issues like unsited statistics, inaccurate product info, unsourced competitor claims, and patronizing concept explainer links. We break it into multiple steps because there's a context limit to how much information the AI can take in at one time.

**Aida Knezevic:** Because we had to regenerate articles, we're now also working on new articles at the same time. You'll get five new drafts either today or tomorrow—they're in the editing queue. We're also finalizing revisions on three articles, and Natalie will follow up in the external channel to get your final sign-off.

**Nicolas Lecomte:** I was going to ask because it seemed the pace of delivery slowed down. I assumed you were waiting to fix the workflow first.

**Aida Knezevic:** Yes, Natalie got really sick on Monday and Tuesday, which slowed us down. We have a couple of people involved in building the new pipeline. We'll make it up, though. You'll still get the articles you're due, but we'd rather fix everything and do it right than waste your time reviewing subpar content.

**Paul Sinaï:** Makes sense.

**Aida Knezevic:** For content ideas, we have four new topics, but we're also doing additional keyword research this week for bottom-of-funnel topics. When I spoke with Paul last week, he mentioned the space is getting crowded, so we need to get into product listicles and comparisons.

**Aida Knezevic:** I think we can turn the Content Ideas doc into a table with idea, URL, and date columns to make it easier to track.

**Nicolas Lecomte:** Of course, yes.

**Aida Knezevic:** For those terms you mentioned—persistent sandboxes and stateful sandboxes—these don't have search volume in SEMrush, but we can incorporate these keywords into existing content so they're mentioned throughout. If somebody Googles them, an article could still show up.

**Nicolas Lecomte:** Could it be because it's so recent? From my perspective, I keep hearing it more and more. People directly tell us they're looking for persistent sandboxes or stateful sandboxes when asking about Blaxel.

**Paul Sinaï:** That's what I was about to say. More people are asking about running agents inside sandboxes or separately. There are several social posts about this. It's a very hot topic right now, and people are looking to persist context in different ways—not vector databases or graph databases, but just keeping a file system directly attached to the sandbox. So persistence, storage, and context storage are the keywords we really want to push right now because they're one of our strengths. In the coming days, we're going to release a new feature called Agent Drive—it's like Google Drive but optimized for AI agents.

**Paul Sinaï:** Storage, persistence, and agent context persistence are definitely the keywords where we see increasing demand from our customers and prospects.

**Aida Knezevic:** In that case, we definitely want to brainstorm some topic ideas. I'd keep the angle fairly simple. We could write an educational blog post and then something more technical if you want, and link them together.

**Carly Piekos:** I just looked up "Persistent Sandboxes" and Blaxel popped up as number one first, then number three on a second search, so you're in the top three.

**Paul Sinaï:** That's good. I really want to be number one.

**Carly Piekos:** If you search in incognito mode on your end, you might see different results since you're logged in with your Blaxel domain.

**Paul Sinaï:** What are your thoughts on CheckThat performance? It's getting better, but it's still quite flat. I'm wondering how we can improve.

**Aida Knezevic:** CheckThat performance depends on the prompts we're tracking, and we're tracking a lot of them. The key is understanding where you're not showing up at all and whether those prompts are important for you. If broader prompts show you not at all, that's less of a red flag as long as you're showing up for very important prompts. I think we can export the prompts and analyze them to see if any are less relevant and could be skewing the dataset. What I'm seeing is that E2B has the highest visibility at 7.1%, which is also not super high. I think we have a lot of broader prompts. We should look at prompts where you're not showing up or showing up inconsistently and see how we can improve there. The more we publish, especially product listicles, the faster they show up in AI search. So as we publish more of that type of content, your visibility will grow. But we want to review the prompts we're tracking to make sure we're not diluting the data.

**Paul Sinaï:** Makes sense.

**Aida Knezevic:** I sent over the CTAs. Whenever you have time to set up the MVP banner, let us know.

**Nicolas Lecomte:** I'll work on it as soon as I can. I'm planning some website updates, so I'll include it.

**Aida Knezevic:** Perfect. There are ways to track clicks in PostHog and how they progress to other parts of the site.

**Nicolas Lecomte:** Yes, that would be good as well.

**Aida Knezevic:** I think those are all the updates we had. Anything else we can help you with?

**Paul Sinaï:** No, I think we covered most things. My biggest concern right now is how we can improve our presence in AI search, especially since our audience uses CloudCode, Cursor, ChatGPT, or Gemini to find tools like us. What I'd like is a plan to see what we can target reasonably. Right now our visibility is 1.5% over the last 30 days. What's a realistic objective for the next three to six months? I'd like to discuss this at our next meeting so we can set a target and figure out what it will take from everyone to achieve it.

**Aida Knezevic:** The first step would be looking at the prompts we're tracking and seeing what's missing. But I think, Carly, we should also take this to Kyle and Talal since they've been working on forecasting plans. This could be right up their alley.

**Carly Piekos:** Sounds good.

**Paul Sinaï:** Thank you so much.

**Aida Knezevic:** Thank you.

**Paul Sinaï:** Thank you. Really nice to meet you, Carly. Good to see you again, Aida. See you next week.

**Nicolas Lecomte:** Bye.

**Aida Knezevic:** But now back here, I'm like, I could get out of bed.

**Nicolas Lecomte:** How often do you go to SF?

**Aida Knezevic:** This was actually my first time.

**Nicolas Lecomte:** Okay.

**Aida Knezevic:** So I think I might go back in a couple of months.

**Aida Knezevic:** We're preparing, like we're working on like platforms.

**Aida Knezevic:** We don't just have Atlas and check that.

**Aida Knezevic:** We're like our dev team is building on other, like a more elaborate platform.

**Aida Knezevic:** And I think once that's ready to launch, I might go back.

**Nicolas Lecomte:** But we'll see whenever they need me.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** So yeah, it's more exceptional ad hoc kind of thing.

**Aida Knezevic:** Not like regular.

**Aida Knezevic:** Yeah, yeah, exactly.

**Aida Knezevic:** Do you go to San Francisco a lot?

**Nicolas Lecomte:** Often.

**Nicolas Lecomte:** Yeah, yeah.

**Nicolas Lecomte:** I was there at the beginning of the week.

**Nicolas Lecomte:** Go there once a month, about once a month.

**Aida Knezevic:** Cool.

**Nicolas Lecomte:** The whole team is there.

**Nicolas Lecomte:** I think you saw the whole team.

**Nicolas Lecomte:** So yeah, it makes yeah, it makes more sense as well to go.

**Carly Piekos:** Tick, Sporting Goods, Dow Jones, et cetera.

**Carly Piekos:** So, yeah, I'm really, really happy to join the team and I can't wait to build out your strategy.

**Nicolas Lecomte:** Awesome.

**Nicolas Lecomte:** Nice to meet you.

**paul:** Nice to meet you too.

**Aida Knezevic:** Great.

**Nicolas Lecomte:** Maybe we can do a quick intro.

**Nicolas Lecomte:** I don't know on our end.

**Aida Knezevic:** Yeah, yeah, totally.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** If that makes sense.

**Nicolas Lecomte:** But yeah, we're Nico and Paul.

**Nicolas Lecomte:** We're two of the co-founders of Blaxel.

**Nicolas Lecomte:** Paul is the CEO and I'm running growth and product.

**Nicolas Lecomte:** So, yeah, it's mostly us working with you guys on the content.

**Nicolas Lecomte:** Plus, and then we have somebody in-house.

**Nicolas Lecomte:** His name is Vikram and he does our technical content as well.

**Nicolas Lecomte:** So that means documentation, entering blog posts, that kind of stuff.

**Carly Piekos:** Okay.

**Carly Piekos:** Awesome.

**Carly Piekos:** And Paul?

**paul:** Yeah, I'm Paul.

**paul:** So I'm the CEO of Blaxel.

**paul:** I'm mostly technical and in charge of sort of the business.

**paul:** Everything's self-related.

**paul:** Yeah, it's mostly my background is an entrepreneur.

**paul:** Blaxel is my third startup.

**paul:** I sold the previous one to the largest European thought provider.

**paul:** Yeah, it's many what I do.

**paul:** I live in San Francisco.

**Carly Piekos:** Oh, yeah.

**Carly Piekos:** Are you both in San Francisco?

**paul:** No, Nico is based in New York, but he's doing back and forth between New York and SF.

**paul:** But the HQ, like, the team is mainly in SF, and it's where we are hiring all our future growth team and engineering team.

**Carly Piekos:** Okay.

**Carly Piekos:** Yeah, I'm East Coast, too.

**paul:** I'm, like, an hour from New York.

**Nicolas Lecomte:** Okay, cool.

**Nicolas Lecomte:** Nice.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, I wanted to get us started with some pipeline updates because the last round of articles that we delivered, there were a couple of in there that had to be.

**Aida Knezevic:** We've written completely, and that's always like a red flag for us because we're like, okay, the pipeline isn't doing what it's supposed to be doing.

**Aida Knezevic:** So we spent some time just developing like a brand new pipeline and adding additional steps to the workflow to prevent specific issues from happening again, specifically the new pipeline.

**Aida Knezevic:** For example, should no longer suggest that Blaxel can do GPU compute or like model training.

**Aida Knezevic:** Moving forward, it should also reference all Blaxel products that are relevant to the specific topic that it's covering, not just sandboxes.

**Aida Knezevic:** And we also revised the article generation pipeline to incorporate the product feature matrix during the research step.

**Aida Knezevic:** That allows the researcher to find information that's relevant to Blaxel's benefits, not just in general, like for that specific topic.

**Aida Knezevic:** what?

**Aida Knezevic:** search becauseAAAAA

**Aida Knezevic:** So the researcher just isn't like taking the topic that we've given it, but it's also looking at like your company context to research like additional information so that we can provide, like we can incorporate Blaxel in a more organic way.

**Aida Knezevic:** Okay, to show you actually like what that looks like in practice.

**Aida Knezevic:** So this is the V3 of the agentic article generation pipeline.

**Aida Knezevic:** We're using EXA as a researcher.

**Aida Knezevic:** EXA is the most advanced researcher that we use.

**Aida Knezevic:** We use it whenever we're dealing with technical topics.

**Aida Knezevic:** Typically, we use Tavilli.

**paul:** We are integrated.

**paul:** We know that because we have integration with them in our platform.

**Aida Knezevic:** So it's a reason why.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, we use, we alternate between EXA and Tavilli.

**Aida Knezevic:** And I know that Tavilli is the baseline that we start with.

**paul:** And then if we notice like, oh, this is not working, let me try to.

**Aida Knezevic:** 25 milliseconds resumed from standby.

**Aida Knezevic:** So this is like a complete list.

**Aida Knezevic:** And this is based on the feedback that you've given us.

**Aida Knezevic:** So like these rules, they have to be like, the article is basically graded against these rules.

**Aida Knezevic:** It has like a list of banned AI phrases as well.

**paul:** Also has banned corporate language.

**paul:** And do you connect, are you connected with our documentation as well and our knowledge base?

**paul:** We have both.

**paul:** We have our documentation.

**paul:** We are using Mintlyfy.

**paul:** So we can, and Mintlyfy, Mintlyfy is plugged on our GitHub public repository.

**paul:** So you can use it if you want to directly access the entire documentation in Markdown format, which usually works pretty well with agents.

**paul:** So it's one thing that...

**paul:** You could do.

**paul:** We are doing this for the support with Pylon.

**paul:** And the second thing is the knowledge base.

**paul:** We are using Pylon.

**paul:** And there is a website called, I think it's support.blackcell.ai, where there is specific posts about, you know, some workaround or, you know, guides that are not promoted inside the documentation, but can still be relevant as the overall knowledge that the company has been.

**paul:** built around how to use our product or leverage some part of the product or some limitation even can be mentioned into that.

**paul:** So maybe, I don't know if you are already doing this, but could be super interesting maybe to leverage our documentation and the knowledge base.

**Aida Knezevic:** Yeah, yeah, I think the documentation and the knowledge base, I don't think there's a reason why we couldn't incorporate it as maybe a separate step, but I'll add.

**Aida Knezevic:** And this is mapped to feedback from your review team, so from Vikram, from Nicolas, or from yourself.

**Aida Knezevic:** So, for example, unsighted statistics, inaccurate product info, unsourced competitor claims, like, or patronizing concept explainer links.

**Aida Knezevic:** Like, for example, like, just adding links that, like, the readers would be like, why are you showing me this link?

**Aida Knezevic:** So, things like that.

**Aida Knezevic:** And then we can obviously expand this with anything else that comes up in the future.

**Aida Knezevic:** But it's just important because you have, like, a context limit to how much information the AI can take in at a time.

**Aida Knezevic:** We like to break it up into multiple steps.

**paul:** It makes sense.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** And then we, because we had to regenerate the articles, and then we also started working on new articles at the same time, you will get five new drafts, I think, either today or tomorrow.

**Aida Knezevic:** I know it's in the editing queue, so they're working on it right now.

**Aida Knezevic:** And we're also...

**Aida Knezevic:** also...

**Aida Knezevic:** Like finalizing revisions on three articles.

**Aida Knezevic:** So Natalie will follow up with that in the external channel as well, just to get your final sign off.

**Nicolas Lecomte:** Okay, because I was going to ask, because it seemed that the pace of delivery of new articles had slowed down.

**Nicolas Lecomte:** So I was wondering, I assume that you guys were waiting first to fix the workflow before.

**Aida Knezevic:** Yeah, yeah, that was a big, like Natalie that got sick, really sick on Monday and Tuesday.

**Aida Knezevic:** So we were like trying to, we were trying to like fix the pipeline.

**Aida Knezevic:** And Jen, like we have a couple of people that were involved in like building the new pipeline.

**Aida Knezevic:** So that just slowed us down a little bit, but we're going to like make it up.

**Aida Knezevic:** So it's not, you're still going to get like the articles that you're due, but we would just rather fix everything and do it right.

**Aida Knezevic:** Rather than just have to like waste your time basically with just like reviewing content that isn't on par.

**paul:** Makes sense.

**Nicolas Lecomte:** That makes sense.

**paul:** Makes sense.

**Nicolas Lecomte:** Oh, good.

**Nicolas Lecomte:** And I hope she feels better soon.

**paul:** Yeah.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** I think she.

**Aida Knezevic:** He's doing better.

**paul:** There's a flu going around California that's just...

**paul:** Yeah, which is pretty bad.

**paul:** I can testify for it.

**paul:** I'm vaccinated against flu, but my kid was sick like a week ago.

**paul:** So it's pretty bad.

**paul:** And he's sick again this week.

**Aida Knezevic:** So it's pretty bad.

**Aida Knezevic:** Yeah, it was going around in our office as well.

**paul:** I managed, knock on wood, I managed to escape it.

**paul:** You left California before.

**Aida Knezevic:** Yes, but also I have...

**Aida Knezevic:** I don't know if you had this because you're European, but I got this vaccine when I was little.

**Aida Knezevic:** And I have like this mark, like I have two marks on my arm.

**Aida Knezevic:** And I feel like in the US, they don't give those vaccines anymore.

**paul:** maybe...

**paul:** I have like some antibodies that are...

**paul:** Antibodies.

**paul:** Yeah, it's the long term.

**paul:** I never had it, but it's...

**paul:** Yes, probably you are addicted.

**paul:** You have a bubble around you.

**paul:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** So, yeah, we were working on getting new content this week.

**Aida Knezevic:** And then these are the four that have been published since our sync last week.

**Aida Knezevic:** These have all been indexed, and some of them are already even getting traffic.

**Aida Knezevic:** So I was just looking at the Looker report, and this is just Google Search Console data.

**Aida Knezevic:** Let me just filter this out.

**Aida Knezevic:** So you can kind of see, like, how we're in this week right now, but you can see kind of, like, how week over week the traffic is growing pretty steadily as we're publishing.

**Aida Knezevic:** And then, for example, the article Code Sandbox alternative is doing quite well, both in terms of, like, clicks so far and the average position.

**Aida Knezevic:** And yeah, and then it's soon as, and I was also looking at your post hoc, because we also have, like, we don't.

**Aida Knezevic:** don't use Google Analytics, obviously.

**Aida Knezevic:** So I was also looking at the post-hog analytics as well.

**Aida Knezevic:** And the code sandbox alternatives here seems to be getting the most traffic.

**Aida Knezevic:** But again, we need to filter this by session source to understand where the traffic is coming from.

**paul:** Yeah.

**paul:** Yeah, we are fixing some trackers in our implementation for the website.

**paul:** I don't know if it affects the blog, Nico.

**paul:** I know Tomai is working on this because we launched small campaigns, ads, paid ads.

**paul:** We started with LinkedIn and Google.

**paul:** And we launched today, we are launching X and Reddit.

**paul:** And we can see like everything around competitor is definitely getting much more conversions than the rest.

**paul:** But it's, it's, it's, it's also a trend.

**paul:** And one thing I'm.

**paul:** Probably we should write a paper related to what Entropic wrote at the end of last year around tools.

**paul:** Entropic published a paper saying the LLMs are getting so good that now we may be, in the future, maybe we won't need any more tools and just give a computer and the LLM will be able to use just simple commands and file system access.

**paul:** So people are just crazy about soundboxes right now, since this paper.

**paul:** So it's really good for us, like the outgrowth is pretty good right now.

**paul:** So we're super excited, but we probably, we want to go even faster.

**paul:** So maybe doing some research or related posts with this Entropic paper would be interesting.

**Nicolas Lecomte:** Yeah, and I did, by the way, that's one of the, I think.

**Nicolas Lecomte:** The content ideas, that was one of the ideas that I listed.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** I think we have, if you go to the topics in considering, so we have, there are four here that are new, but then we also need to go, we're also doing additional keyword research this week, just for bottom of the funnel topics.

**Aida Knezevic:** When I talked to Paul last week, he told me that the space is getting a little bit crowded, so we do need to, like, get into those product listicles and comparisons.

**paul:** Yeah.

**Aida Knezevic:** But let me just double check and go to the docs.

**Aida Knezevic:** Content ideas.

**Aida Knezevic:** Oh, yeah, yeah, I see this.

**Aida Knezevic:** All right.

**Aida Knezevic:** It's pretty cool.

**Aida Knezevic:** I think we can actually, like, turn this into a table, and then you can just, like, add, like, the idea, the URL, if you have, like, a URL.

**Aida Knezevic:** And then you can also add the date when you added it.

**Aida Knezevic:** So that makes it easier to track.

**Nicolas Lecomte:** Of course, yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Let's go back.

**Aida Knezevic:** Let's see what else I wanted to show you.

**Aida Knezevic:** Cool.

**Aida Knezevic:** For these, you brought up these terms, persistent sandboxes and stateful sandboxes.

**paul:** Yep.

**Aida Knezevic:** These two don't have search volume in SEMrush, but we can incorporate these keywords into the existing content so that they start kind of at least are being mentioned throughout.

**Aida Knezevic:** And then if somebody Googles it, then like an article could still show up because it's mentioning these concepts.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** Could it be because it's so recent?

**Nicolas Lecomte:** Because, I mean, you know, on my perspective, I keep hearing it more and more.

**Nicolas Lecomte:** We're not.

**Nicolas Lecomte:** We're

**Nicolas Lecomte:** Like, a lot of people tell us, yeah, you know, or, you know, when I ask them, yeah, you want me to to test Blaxel?

**Nicolas Lecomte:** And they were like, oh, because I was looking for persistent sandboxes, flat out told me that I'm looking for persistent sandboxes or stateful sandboxes.

**Nicolas Lecomte:** So, but maybe that's a very new concept as well.

**paul:** Yeah, it's what I was about to say, and it's going to ramp up, like, more and more people are asking for, for instance, running agents inside a sandbox or separately.

**paul:** There is, like, several social posts about this.

**paul:** So our recommendation is to separate it, but we also want to publish, like, maybe there is some way to do it, but not in the usual way.

**paul:** So I think it's an opportunity to publish about this.

**paul:** It's very hot threads now, and people are looking to persist the context in different ways, like, not vector database, not even graph database, but start to just want to.

**paul:** Keep a file system directly attached to the sandbox.

**paul:** So the persistence and the storage, context storage, these kind of things, are the keywords that we really want to push right now.

**paul:** Because I think it's, I believe it's one of our strengths.

**paul:** And in the coming days, we are going to release a new feature, which we call Agent Drive.

**paul:** It's like a Google Drive, but optimized for AI agents.

**Aida Knezevic:** So in terms of speed, in terms of how you interact with it, how you can connect.

**paul:** So it's, so yes, storage, persistence, agent context, persistence is definitely the keywords that we see, where we see an increasing demand from our customers and prospects.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Yeah, okay.

**Aida Knezevic:** In that case, we definitely want to brainstorm some topic ideas.

**Aida Knezevic:** I would still keep it, the angle, like fairly simple.

**paul:** The GEO, most of our users are using mostly AI anytime they ask something.

**paul:** So I'm discounting a bit the SEO effect, and I'm more concerned about people asking about those questions directly to ChatGBT or Cloud, Cloud Code or whatever behind, and us not being mentioned.

**paul:** We really want to be in the first one popping up when you ask AI, okay, I need to persist the context within my sandbox.

**Aida Knezevic:** This is typically where we should be the first one.

**Aida Knezevic:** Okay, okay.

**Aida Knezevic:** That is super clear.

**Aida Knezevic:** Yeah, in that case, I think we can brainstorm a couple of topics here and then see how it goes.

**Aida Knezevic:** I'm sure that we could at least write a very kind of educational blog post, and then if you want to do something more technical, that would also be great, and we could link to it.

**Carly Piekos:** I just looked at Persistent Sandboxes up, and you popped up as number one first, and then I re-googled it, and you popped up as number three, so you're in the top three for that.

**paul:** Okay, okay, that's good, that's good.

**paul:** I really want to be on the number one.

**Carly Piekos:** Yeah, yeah, so like if you, I just, I don't know, I didn't do it in incognito mode, but I just, you know, looked it up, so if you look it up on your end.

**Nicolas Lecomte:** Because I can't find it, I just, you looked up Persistent Sandbox on Google?

**Carly Piekos:** Yeah.

**Nicolas Lecomte:** Because I don't see it.

**Nicolas Lecomte:** Okay.

**paul:** But probably you need to sort of do it in incognito, Nico, because on Google, you are logged in with your Google account from blackset.ai with the domain.

**Nicolas Lecomte:** So you, would be, probably the search engine is avoiding the workspace with the same domain.

**Nicolas Lecomte:** Okay.

**paul:** Also, I had a question about the...

**paul:** The check that performance for the, so it's getting better, but still we are still a bit flat.

**paul:** Just wonder what are your texts on these performances and how we can improve our performances for uncheck that, you know?

**Aida Knezevic:** Yeah, so let me, I just logged in, so the check that performance is dependent, like it's very, it's obviously depends on the prompts that we're tracking, and we are tracking a lot of prompts here.

**Aida Knezevic:** I think where we want to, what we want to understand is where do you not show up at all?

**paul:** Yeah.

**Aida Knezevic:** And then understand are these prompts like important for you?

**Aida Knezevic:** Because if we have like slightly broader prompts.

**Aida Knezevic:** Where you're not showing up at all, that wouldn't be that big of a red flag as long as you're showing up for the prompts that are very, very important to you.

**Aida Knezevic:** So I think what we can do, and Carly, mean, I think we can export the prompts and then we can kind of take a look at the data set and see if the prompts that we're tracking here, like if there are any that are kind of less relevant because they could skew the data set.

**Aida Knezevic:** Because what I'm seeing, like just in the workspace, like overview, your competitors are like E2B has the highest visibility at 7.1%.

**Aida Knezevic:** So they're also not like super high because I think we have a lot of prompts that are more broader, but also in terms of, so that's the first point of order.

**Aida Knezevic:** And then we also want to take a look at the prompts that are relevant for you that we're tracking where you're not showing.

**Aida Knezevic:** You're or you're showing up inconsistently and then seeing how we can show up more.

**Aida Knezevic:** Again, the more we publish, especially the listicles, the product listicles, those start showing up very quickly in AI search.

**Aida Knezevic:** So the more we publish that type of content, your visibility is going to grow.

**Aida Knezevic:** But we do want to take a look at the prompts that we're tracking to make sure that we're not diluting the data with anything that we actually don't want to be tracking.

**paul:** Makes sense.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** And I did send over the CTAs.

**paul:** I don't know.

**Aida Knezevic:** I mean, when you have the time to set up the MVP for the banner, just let us know.

**Nicolas Lecomte:** Yeah, I'll work on it as soon as I can.

**Aida Knezevic:** Don't worry about it.

**Nicolas Lecomte:** No, but I'm planning.

**Nicolas Lecomte:** I'm working progress on the website, so I plan to do some updates.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** No, I think that that would be good for us.

**Aida Knezevic:** And then I think I'm sure that there

**Aida Knezevic:** There are ways to track, like in post-hoc, just the clicks and how they're progressing to other parts of the site.

**Nicolas Lecomte:** So that would be good as well.

**Nicolas Lecomte:** Yes, totally.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I think those are all the updates that we had.

**Aida Knezevic:** Anything else that we can help you with?

**paul:** I think, no, we covered most of the things.

**paul:** To be honest, my biggest concern right now is just to how we can improve our presence on Geo, especially since our audience, like when we ask, we try to ask what people are using to choose or find tools like us, and are using a lot, like by far, just CloudCode or Cursor, or sometimes just Chachibe or Gemini.

**paul:** So, yeah, what I would like just is probably having maybe a plan to see what.

**paul:** We can target like reasonably right now on seven days, if I take like 30 days, right now we are visibility at 1.5.

**paul:** What is our objective for the next three months or six months?

**paul:** I don't know what is reasonable to, but I just would like to discuss this next at our next meeting to see, okay, in three months, this is where we would like to be.

**paul:** This is our objective and what it would take from everyone like you and us to achieve this objective.

**Aida Knezevic:** Totally.

**Aida Knezevic:** I think, yeah, that the first step would be looking at the prompts that we're tracking and then, you know, seeing what's missing as well.

**Aida Knezevic:** But I think, Carly, I would also take this to Kyle and Talal.

**Aida Knezevic:** know that they've been working on a lot of these, like, forecasting plans.

**Aida Knezevic:** So I think this is something that could be right up their alley.

**Carly Piekos:** Sounds good.

**paul:** Sounds good.

**paul:** good.

**paul:** Thank you so much.

**Aida Knezevic:** All right.

**Aida Knezevic:** Thank you.

**paul:** Thank you.

**Aida Knezevic:** a good rest of your day.

**paul:** Really nice to meet you, Carly.

**paul:** was good to see you again, Aida.

**paul:** Thank you.

**paul:** See you next week.

**paul:** Bye-bye.

**Nicolas Lecomte:** Bye-bye.
