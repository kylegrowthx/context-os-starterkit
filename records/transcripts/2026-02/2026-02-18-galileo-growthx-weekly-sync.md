# Galileo <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-18
time: 18:30 UTC
duration: 12 minutes
organizer: team@growthxlabs.com
participants: Jackson Wells (Galileo), Carrie Chowske (GrowthX)
fathom_recording_id: 123441902
fathom_url: https://fathom.video/calls/570059798
share_url: https://fathom.video/share/_hDzjyxNmPzUt2eYw2uRd9U9NZi_sBxb
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Review AEO performance and strategize on closing the visibility gap.

---

## Context

Galileo is an AI platform for debugging and evaluating LLM applications. Jackson Wells leads product at Galileo and regularly syncs with Carrie Chowske, senior strategist at GrowthX, on AEO (AI Engine Optimization) strategy. Carrie was late to this meeting due to a client call with a new executive who inherited the Galileo partnership, underscoring the importance of clear visibility into results. This weekly sync focuses on closing Galileo's critical AEO visibility gap (currently 3.4%) and addressing stakeholder skepticism from Galileo's CMO Jason, who has not yet been convinced of the platform's value or had a direct review of the CheckThat visibility tool. The goal is to build a data-driven case that shows why current visibility metrics are lower than competitors, what the realistic targets should be (8–15%), and how targeted content will drive measurable progress.

---

## Relevance

**To CheckThat:**
- Core prompts on Galileo are showing 20% visibility (strong baseline), validating the targeted strategy vs. volume approach.
- Visibility metric is being incorporated into AEO score formula; sentiment metric is being deprecated as it doesn't differentiate B2B products.
- Feature request: platform-level visibility segmentation (ChatGPT vs. Google AI Overview vs. Perplexity) to identify which platforms drive the most citations and mentions.
- Content artifacts are living documents updated quarterly and are now the critical bottleneck for scaling content and reducing the 14-article review backlog.

**To GrowthX Delivery:**
- Content artifact accuracy will directly impact Jackson's review time and publication speed; Carrie to ensure quarterly updates and conflict resolution in artifacts.
- Competitor content footprint breakdowns and visibility plan framework are being drafted for Jackson to present to CMO Jason, showing realistic targets (8–15%) and competitive positioning against direct competitors (Langfuse) vs. broader platforms (Langsmith, Datadog).
- SEO performance tracking continues as a leading indicator for AEO success; both metrics show positive week-over-week trends on core prompts.

**To GrowthX Business Development:**
- Galileo's CMO Jason is skeptical of AEO platform value; strong data presentation is critical to stakeholder buy-in and continued engagement.

---

## Overview

- **AEO visibility is a critical gap (3.4%),** creating stakeholder risk with CMO Jason. The strategy is to target high-intent queries, not compete on volume.
- **The AEO score formula will be revised** to replace the sentiment metric with visibility. Rationale: Sentiment is often net-positive for B2B products and thus not a strong differentiator.
- **Content artifacts are the key to scaling.** Jackson will review them with the product team to ensure accuracy, which will reduce the current 14-article review backlog.
- **Initial data on core prompts is positive,** showing 20% visibility. This validates the targeted strategy and serves as a strong baseline for future growth.

---

## Key Topics

### AEO Performance & Stakeholder Risk

  - AEO visibility is the primary performance gap, currently at 3.4%.
      - **Goal:** Reach 8–15% visibility to be considered solid progress for this stage.
  - This gap creates stakeholder risk, as CMO Jason is skeptical of AEO and has not yet seen the platform.
  - **Strategy:** Frame the data by comparing Galileo to direct competitors (e.g., Langfuse), not large platforms with broad offerings (e.g., Langsmith, Datadog), to show a more accurate relative position.

### AEO Score Formula Revision

  - The current AEO score formula will be revised to better reflect B2B performance.
  - **Change:** Replace the sentiment metric with visibility.
      - **Rationale:** Sentiment is often net-positive for B2B products and thus not a strong differentiator.
  - The revised formula will focus on three metrics:
      - Position
      - Visibility
      - Citation Share

### Content Strategy & Artifacts

  - The content strategy will focus on targeting high-intent queries to differentiate Galileo, rather than competing on volume.
  - **Content Artifacts:**
      - Jackson will review the source material with the product team to ensure accuracy and prioritize future content.
      - **Rationale:** Accurate artifacts are the key to scaling content creation and reducing the current 14-article review backlog.
      - **Note:** Artifacts are living documents updated quarterly; minor inaccuracies are expected and corrected over time.

### Platform & Data Insights

  - **Platform Weighting:** All AI platforms (ChatGPT, AI Overview, AI Node) are currently weighted equally in the aggregate score.
  - **Feature Request:** Jackson requested the ability to segment data by individual AI platform.
      - **Rationale:** This would provide a clearer signal, as platform performance varies significantly (e.g., Perplexity yields more citations, ChatGPT yields fewer).
  - **SEO as a Leading Indicator:** SEO performance is a strong signal for future AEO success, as AEO best practices are rooted in SEO.

---

## Action Items

**Jackson Wells**
- Add secondary offerings to article queue; publish ready articles
- Schedule product team review re: source materials + content prioritization
- Add relevant new library prompts to core AEO prompts

**Carrie Chowske**
- DM Jackson Slack: visibility plan framework + competitor content footprint breakdowns
- Confirm visibility metric scope (all prompts/platforms); share w/ Jackson
- Retool AEO scoring formula (visibility, position, citation share; outliers)
- Submit product feature request: platform-level visibility segmentation

---

## Transcript

**Jackson Wells:** Hello.

**Jackson Wells:** How are we doing?

**Carrie Chowske:** Sorry. I was on a call with another client and spent the last hour getting grilled by their CEO about whether or not GrowthX knows what they're doing. It was fun. It was an interesting call.

**Jackson Wells:** He inherited the partnership from his predecessor.

**Carrie Chowske:** So he's like, you know, never really signed the contract with us. So it's been a lot of convincing him that we do know what we're doing. And it was the first time that we had met. So I couldn't get out of it. I have to do this. I'm so sorry I meant to message you a few minutes before, but I was literally fighting for my life.

**Jackson Wells:** Oh, good. I'm sorry to hear that.

**Carrie Chowske:** It was actually kind of fun. I do agency-style work, even though GrowthX is not technically an agency. We operate like one and it's why I like it. You don't get the brunt of that every day like our point of contact does.

**Jackson Wells:** You know, I only have to deal with it once in a blue moon. I am trying to avoid that exact same outcome on my end. So it's definitely getting increased pressure specifically around AEO, which I think we're pretty aligned on how we think about it. But it doesn't come without having to back that up and come up with plans and be able to address concerns.

**Carrie Chowske:** The things that you brought up in Slack, I went ahead and pulled some very preliminary findings based on that. We can dig into it deeper, but at least we have something to start from and we can decide what to do next with it.

**Jackson Wells:** Yeah. I need to keep having conversations with Jason, who's our CMO. Ultimately, it would be good for us to bring him in and give him a look at CheckThat at some point. He seems quite skeptical, despite not having seen the tool. I'm working on that right now, but I think it may be good to hear directly from you guys about it. And we're evaluating whether to use that GEO score or weight it differently. I do think we need to factor in visibility. I've been digging into the platform more. I do think visibility is probably something we need to take into consideration, but I just need a little more time to think through it. It's a sales kickoff right now, so I don't have a ton of bandwidth this week. But I'm going to focus on it a little more to start to assuage concerns.

**Carrie Chowske:** Yeah. I feel like we made some slight inroads with Jason, just giving him the breakdown of it. So that's a note to self to make sure I'm showing my work.

**Jackson Wells:** Totally. I mean, you do a great job at that. You've got to look for it to know that it exists.

**Carrie Chowske:** Right. I think you're right. There's a couple of things I like about the formula we're using and a couple that I'm not sure about. I do like that we're de-emphasizing citation share. Getting cited at all is good, honestly, even a 3% citation share is really high. And I like that it's weighting it less because it's not having as big of an impact on the score. But I think sentiment is weighted a little too heavily. I see a lot of negative sentiment. I think one of the competitors had the lowest sentiment score I've seen, like in the 50s. And that immediately drops the score down, but it doesn't take away from how much visibility they have. Position is a good metric. But instead of sentiment, we ought to be looking at position, visibility, and citation share.

**Jackson Wells:** Agreed. I think sentiment was relevant with B2C products because you're going to have a lot more user-based reviews and data to pull from. But with B2B products, sentiment seems net positive almost everywhere.

**Carrie Chowske:** People really have to hate something to be out there on the internet talking about it negatively in a business sense, you know? It takes work to do that.

**Jackson Wells:** Yep.

**Carrie Chowske:** Okay. Replace with visibility. Okay, I think everybody types while talking.

**Jackson Wells:** For sure.

**Carrie Chowske:** So here's three things I identified looking at that visibility gap. It's not really a one-and-done problem, right? It's several issues. One reason we should revisit the formula is visibility without citations. What's happening right now is Galileo is appearing at a fairly consistently high rate. Anything in the 40 and above is really strong. 20 and above is good. But we're not seeing links. So it suggests that content exists and they're recognizing that you qualify. They're not just getting mentioned by competitors, but they're getting mentioned by third party. If AI is going to follow the model of SEO, it's going to have more weight in terms of how often they get mentioned. But even though we can't maybe win on volume, we can if we really target those high-intent queries and think about where Galileo is directly competing and focus on differentiating in that lane as opposed to trying to beat them all overall. That's not going to happen, or it's less likely. It's a problem that a lot of SaaS products have. The more niche you get, the harder it is to say, these are my direct competitors. Ideally, you're revolutionizing something or doing a niche that someone hasn't completely filled yet. So that makes sense that that's hard to nail down.

**Jackson Wells:** Got it. What were you saying about secondary offerings?

**Carrie Chowske:** Yeah, any of the ones that are going to be our secondary, we definitely want to make sure we get those.

**Jackson Wells:** Yeah, those are definitely the ones I want to put into the article queue. I think getting the stuff that's ready for publishing out the door and then taking a second to calibrate on exactly what needs to be done next would be great. I think any suggestions as far as what is most important for us closing the AEO gap against our competitors would be great. We are pretty behind right now as far as visibility is concerned. Position is pretty good, sentiment obviously is fine, and we're starting to close the gap with citation share, which is great. But it's really the visibility where we're kind of very behind where I'd like to be.

**Carrie Chowske:** Yeah, I agree with that.

**Jackson Wells:** And I'm a little nervous to show Jason the platform for that exact reason. Because the first thing you see is visibility and it looks really bad.

**Carrie Chowske:** It does. I mean, I'm confident I can frame it. It's always the risk that they think, well, of course you think it looks good. You want me to think you're doing a good job. But I really work hard not to be a bullshitter about that sort of thing. I'm realistic. When you look at it holistically, it's not a great picture. But when you think about what we're comparing here, you have to consider that you're not just looking at where you directly compete with these brands, but everything else that they do and how big their footprint is. One thing that might help: I could pull other accounts we have that have a very similar concern where we've had some successes. I know of one that's very niche and because we really nailed the volume of what we're doing, they followed on some of our suggestions. And looking at that compared to what you're doing, when you're also competing with both very niche, very direct competitors and big names as well.

**Jackson Wells:** Yeah, that would be helpful. I think also any potential content footprint breakdowns we can get for the competitors that we are lagging against would be great. I do agree when it comes to competitors like Langsmith and Datadog because they have wider offerings across a broader collection of use cases and they've got a bigger net.

**Carrie Chowske:** It's going to be at the bottom of that list. Clearly, if we're looking at it here, it is underneath all of those, but it's not as far from them as if we're also including these other additional competitors. Langsmith is really far out ahead. But to be honest, 3.4% isn't awful. I wouldn't say it's bordering on good. Like, it's getting there. For the size of where you're at in this stage of content, what I would expect to really see and call solid progress would be closer to 10%. Like, in the 8 to 15 range, roughly, would be where I would expect to see it at this stage. And that is clearly not where we are. But I think given that we've got a lot yet to publish that's targeted at AI visibility, I think we have the potential to get it there pretty quick.

**Jackson Wells:** Yeah, so let's get that stuff over the line, then let's assess and go from there. I think going through your guys' source material, there's definitely a lot that needs to be discussed internally. I've started to pick apart some of the different pieces. There's a lot there. And I do want to schedule some time with our product team to kind of go over it and future-proof it a bit and then prioritize it differently.

**Carrie Chowske:** We don't have to worry too much. Yes, future-proofing is good, but don't worry too much because it is a living document. We update that at a minimum quarterly. So it was good timing for us to have you review them anyway.

**Jackson Wells:** Okay.

**Carrie Chowske:** Any information you give us that is going to influence what we're creating for content, we add that in as we go. And the reason we evaluate them is because sometimes you'll get artifacts that are conflicting with each other. So you're telling it one thing and this one says something else. So you've got to evaluate them. And then also make sure it's accurate with the current breakdown of product and messaging.

**Jackson Wells:** So I need to go through all of that a little more thoroughly and then bring in other people because I think that will help us figure out where we want to put our energy into content moving forward.

**Carrie Chowske:** Yeah, makes sense. So I think we covered a lot of this. I did pull the overall GEO score based on our current formula and we've seen an increase week over week. It's gone up. And I think that's related to us honing in on some different prompts specifically. It sounds shady when I talk about it, you know? To say, well, we've got to track the right prompts. But it's not so much about tracking the ones you know you're going to be good at. It's more about tracking the ones you want to be known for. The idea is getting in front of that search and being like, if somebody is looking up this use case, we want Galileo to show up there. If they're looking up this use case in this industry for this persona, we want to be there. And so we know what we can do with those prompts to find out when people ask, are we getting those mentions? It sounds because you're kind of going around it from the back end like you're doing new-age math to manipulate the data. But it's really more about clear differentiation.

**Jackson Wells:** It's like very pure old-school marketing in a lot of ways. Yeah, it is. It's definitely not rigging it. It's more just preemptively thinking about what is going to make sense for your brand, for your product. I did have a question: for the overview, that visibility is off all of the prompts that are in our library, correct?

**Carrie Chowske:** I believe it is. And then I believe it also, I will confirm this again, but these numbers here are telling you how much it is. And then this is kind of compared against how often your competitors are being mentioned. I do think it is in those prompts, but I think it's also heavily. And like with ChatGPT, their training data is still from August of last year. So while they do some live search, the training data is trailing. So they may see what you've posted, but view you as irrelevant if what you had on your site in August of 2025 is not relevant. But yeah, I think looking at the prompt level and looking at the competitors are the two biggest signals. So if we're looking at direct competitors, I've got a lot of work to do there. And then on specific prompts, we're a little better when we get drilled down into these deeper topics. One of the things I was looking at was really interesting. When I was calculating those scores, I had to go through the prompts one by one. So to see how position and what's appearing, the average position for Galileo is nine. But this is one where I think it's weighting this too strongly because if BrainTrust is in the top three all week long, they get 100 in that score. Whereas Galileo gets a zero. That doesn't make any sense because you still were mentioned.

**Jackson Wells:** Yeah. We do need to retool it with that in mind and think about the potential outliers to get a more true measure.

**Carrie Chowske:** But when you look at individual prompts, we're looking at that overall score and visibility is 3.8%, right? But on this one, we're at 25. And 25 would win the top spot on the main chart. But on this specific prompt, it's still fairly low on the list. So it's just a lot of different factors. And that's why I'm really encouraging people to do what you've done: focus on these core prompts. Like, what are the ones we care the most about? I think it's great to say, here's two library prompts, so these are broader. All my competitors could see these prompts too. But the ones I really care about, you've got two of them right here in the top five, which I think is a really solid measure of where we're going.

**Jackson Wells:** This makes sense. I feel like there's a couple of the new library prompts that are now considered in the library that I'll probably add to the core prompts as well, just because they are really applicable to our platform.

**Carrie Chowske:** Yeah, definitely do that. Because those would be from when we changed the classification and then there were some new prompts.

**Jackson Wells:** So if there's ones in there you want to add, let's do it. Yeah, I will go through there and look at it. Also, one more question. So how are these all weighted? Like each platform is weighted equally? ChatGPT, AI Overview, AI Node are all weighted equally?

**Carrie Chowske:** I believe they are, yes. I wish there was a way you could see for just the individual platforms. I think that's something they're looking into doing. Like you could see that overall visibility by platform. But I do think this is a pretty good indication. I tend to see a pretty close correlation between both of Google's AI options. I tend to see the most citations from Perplexity. And then the least mentions from ChatGPT, unless you've got a really established content platform. But that's not hard and fast, but that is kind of where I expect it to be.

**Jackson Wells:** For sure. Is there plans on the roadmap to segment by AI platform for pulling the data specifically?

**Carrie Chowske:** I hope so. I want to say yes, but if there isn't, I'm going to put one in because that's what I want. That to me is one thing that's lacking from a lot of the other tools as well. The more you can drill down and use the data you have, the more useful it is. Especially when you've got a platform like ChatGPT that is so far ahead of the others, that it's like having SEO show up and giving you an aggregate of Google and Bing and whatever, like Ask Jeeves from 1995. It's not as useful.

**Jackson Wells:** Totally. Sweet.

**Carrie Chowske:** I think that's pretty much everything. Just kind of nice to see that on those core prompts, in the first week of data, we're able to say we're starting to show up for these prompts that we're really focusing on. We've got 20% visibility, which is a good baseline. And then we should see it continue to grow if we continue creating content around those topics. Not just specifically targeting that prompt, but that overall credibility and relevance that is also a hallmark of SEO.

**Jackson Wells:** Yep. Totally.

**Carrie Chowske:** We're still seeing growth trajectory with SEO too, which is again something we don't want to forget about, even though it feels less important these days. But SEO is still how the vast majority of people are finding products online, both in B2C and B2B.

**Jackson Wells:** Yep.

**Carrie Chowske:** And seeing that is a good signal of what you're going to see reflected in AI visibility. It's the canary in the coal mine, in a sense.

**Jackson Wells:** For sure. And there's best practices that get carried between the two. SEO best practices directly funnel into AEO best practices. I think new and shiny is definitely taking precedence over the thing that drives it, which is still SEO rankings and SEO best practices.

**Carrie Chowske:** So we're throwing fancy new letters in front of more or less the same thing and trying to measure it now. We're at the keyword-stuffing phase, you know? Like, that's where we are with it. And people are doing all these best-of lists. I think it's good to have those plays. But at the end of the day, you've got to write content for humans too. People that are actually making the decision. While they may use an AI tool to evaluate or narrow down their search, at the end of the day, they've got to believe what you're saying and see proof of that differentiation. We have to make sure that content's there as well.

**Jackson Wells:** Totally. Yeah. It's a weird inflection point. And I guarantee you in three months, all the best-of listicles are going to get smashed in some sort of algorithm change.

**Carrie Chowske:** So everybody's doing them. I don't think it's going to go away just because it's an easy way to answer a very direct prompt. But I think what we saw with Google and how it weights things with its EEAT, I think we're going to see something along those lines. And quite honestly, I feel like Google's already doing it. They're really funneling traditional search into AI. They're saying, here's the overview. And if you want to know more, you should search in AI. Don't listen to all this stuff down here. And more and more people are going to start picking up on that because they trust Google more than they trust OpenAI. They know Google.

**Jackson Wells:** Yeah, 100%. Oh, 100%. Sweet. Well, I've been trying to clear out some of the review queue. I just finished another four today, but that still leaves 14.

**Carrie Chowske:** Yeah, my hope is that if we get the artifacts right and we can start consistently getting accurate content, that should help us cut down on your review time and we should be able to push things through faster. That's another reason I really want to make sure that we're staying up to date on those artifacts and that you're seeing the changes you're asking for. That's what's going to allow us to keep running at scale.

**Jackson Wells:** Yeah, some of the newer ones I reviewed today were much better as far as internal linking is concerned. And the copy was closer from the product-messaging perspective. So it was a step in the right direction. I'm feeling good about that for sure. Fingers crossed when we get all these out of the publishing and editing queue, we'll start to see a good lift there.

**Carrie Chowske:** Yeah, me too. We just got to keep it going. And when I say you're not the only account that's having those issues, everybody's having that problem. It's definitely just getting the quantity that we do is hard to manage with a small team.

**Jackson Wells:** Oh, God, yes. I don't know what I was doing at the last role. It was exhausting doing the whole thing end to end. It's crazy. Well, yeah, I think we're in a good spot. Preemptively, it could be good to draft up something around our plan to increase visibility and why visibility is as it is right now. Just because I do foresee that becoming a question in the next probably week. I'm going to try to stave it off for about a week. But then I assume I can't stave it off any longer.

**Carrie Chowske:** I can draft something for you and then we can tweak it together. I'll just get you a framework to go with.

**Jackson Wells:** And we can adjust based on what Jason's looking for. That would be very solid. If you want to just DM it to me in Slack versus the normal channel, that would be great. It would be good to have that in the back pocket for informed discussions moving forward.

**Carrie Chowske:** Yeah, for sure.

**Jackson Wells:** Thank you, Carrie.

**Carrie Chowske:** I appreciate it. I'm so sorry, again, about being late, but it worked out. We had plenty of time.

**Jackson Wells:** We did, indeed.

**Carrie Chowske:** I'm hoping I don't have to fight for my life again next week. I'm hoping once we get on a good cadence and if we're seeing results, we can switch to a biweekly meeting. Then I can spread them out and not have those back-to-back issues.

**Jackson Wells:** That would help if we run long.

**Carrie Chowske:** That's my plan.

**Jackson Wells:** Cool.

**Carrie Chowske:** All right. I will talk to you next week, but I will see you on Slack in the meantime.

**Jackson Wells:** Sounds good. Have a good rest of your day. Bye.

**Carrie Chowske:** Bye.
