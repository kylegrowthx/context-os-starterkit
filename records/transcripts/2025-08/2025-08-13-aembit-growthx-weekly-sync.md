# Aembit <> GrowthX Weekly Sync

<metadata>
date: 2025-08-13
time: 16:32 UTC
duration: 30 minutes
organizer: ehtisham@growthx.ai
participants: Ehtisham Hussain (GrowthX), Darrell Etherington (GrowthX), Apurva Davé (Aembit), Ashur Kanoon (Aembit)
fathom_recording_id: 80345866
fathom_url: https://fathom.video/calls/380298524
share_url: https://fathom.video/share/-6wVWMZ3vcb4d42dwc1bk9uEeQpTzBDz
source: fathom
enriched_on: 2026-03-03 19:45 UTC
</metadata>

---

## Summary

GrowthX presented blog performance metrics to Aembit showing strong improvements in search ranking (average position dropped from 37.9 to under 20) and impressions (up to 88,000), but clicks plateaued around 400/month due to AI overviews and zero-click searches. The team discussed a strategic shift toward thought leadership and opinion-driven articles to differentiate from current how-to content and drive engagement. Aembit committed to reworking several articles and collaborating with Darrell to create a new schema format that enforces strong opinions for thought leadership pieces.

---

## Context

Aembit is a cloud security company that GrowthX provides content marketing services for. This is part of an ongoing engagement where GrowthX manages blog content strategy and production using a mix of AI-assisted and human-edited workflows. The weekly sync is part of GrowthX's content delivery cadence, where GrowthX's content strategist (Ehtisham) and editor (Darrell, from GrowthX's partner TechCrunch background) review performance data and article quality with Aembit's product and strategy team. The conversation reflects tension between using AI to create volume at scale versus maintaining editorial quality and authentic thought leadership — a core challenge in the content marketing model GrowthX operates.

---

## Relevance

### To GrowthX Delivery:
- Clear evidence of AI-generated content quality gaps: thought leadership pieces lack authentic opinions and differentiation, requiring stronger schema/prompt direction.
- Client feedback confirms need for deeper editorial intervention beyond mechanical conversion (schema redesign with Darrell underway).
- Blog performance shows AI volume strategy is generating impressions but not clicks — baseline metrics validate need to experiment with new article types.

### To GrowthX Business Development:
- Aembit account is engaged and growth-minded despite content quality challenges — they're investing in schema redesign and willing to iterate.
- Risk signal: Apurva's skepticism about machine-generated thought leadership suggests client may consider alternate vendors if quality doesn't improve.
- Opportunity: Aembit's large Snowflake customer reference and future case studies create expansion potential beyond blog content.

### To CheckThat / AEO:
- Client experiencing firsthand the impact of AI overviews and zero-click searches on organic traffic — validates AEO/CheckThat relevance in differentiating content.
- Discussion of "capturing surface area" and building authority corpus over months/years maps to CheckThat's positioning around AI visibility and search behavior shifts.

---

## Overview

- Blog average position improved significantly (37.9 → under 20), impressions up 3x (28k → 88k), but clicks plateaued at ~400/month due to AI overviews and zero-click searches.
- Aembit's current AI-assisted content process fails to produce authentic thought leadership — articles lack strong opinions and differentiation from standard positioning.
- Team will experiment with thought leadership articles using a new schema format with explicit opinion directives, while continuing to produce technical how-to content that drives baseline traffic.

---

## Key Topics

### Blog Performance Analysis

  - Average blog position improved from 37.9 in January to under 20 in August
  - Impressions increased significantly from \~28,000 to 88,000
  - Clicks plateaued around 400 per month
  - Click-through rate declining, attributed to AI overviews and zero-click searches

### Content Strategy Shift

  - Moving towards thought leadership and top-of-funnel content
  - Aiming to differentiate from current technical how-to articles
  - Challenges in producing high-quality thought leadership pieces with current AI-driven process
  - Team discussing need for new schema format to improve thought leadership article creation

### Article Review and Quality Issues

  - "Cloud Posture Tools" article reads as a Prisma product pitch; needs repositioning to cover CSPM tool class broadly (Prisma, Wiz, Orca, Lacework, Sysdig) and reframe Aembit's role as "inoculation" rather than "catching risks."
  - AI Agents article falsely claims new risk surfaces specific to AI, then lists only standard risks — lacks original thinking and appears to be "fancy title on standard positioning."
  - DevOps article conflates workload and DevOps concepts, needs clarity refinement.
  - Root cause: Current AI creation method produces vanilla, undifferentiated content without real opinions or evidence-based insights.

### Newsletter and Case Studies

  - Aembit to share their company newsletter for potential improvement suggestions
  - Limited customer base restricts case study options in the near term

---

## Action Items

**Apurva Davé (Aembit)**
- Send company newsletter to Ehtisham for review and click-through improvement suggestions.
- Review DevOps article today post-Faso's comments. Check for clarity on workload vs DevOps distinction.

**Ehtisham Hussain (GrowthX)**
- Rework "Cloud Posture Tools" article. Focus on CSPM tool class (Prisma, Wiz, Orca, Lacework, Sysdig), not specific vendors. Adjust Aembit positioning from "catching risks" to "inoculation."
- Create new schema for thought leadership articles with Darrell. Include strong opinion directive to enforce authentic viewpoints.

---

## Transcript
**Darrell Etherington:** Exchange, but written out, so you don't actually have to see the media file.

**Darrell Etherington:** Hey, Hey, Apurva.

**Apurva Davé:** How's it going?

**Apurva Davé:** Good.

**Darrell Etherington:** Hi, Ashur.

**Apurva Davé:** I'm just walking back to my house, so I'll be on probably in about 10 minutes.

**Apurva Davé:** Okay, no worries.

**Darrell Etherington:** And I don't, I think Dan Kaplan might still be out.

**Apurva Davé:** I don't know if he's still out.

**Darrell Etherington:** I think he said last week that he was going to be out this week, so that seems correct.

**Apurva Davé:** All right.

**Apurva Davé:** So we're good.

**Apurva Davé:** I think it's just us two on our side.

**Apurva Davé:** Okay, cool.

**Darrell Etherington:** You want to get us started then, Ehtisham?

**Darrell Etherington:** Yeah, let me share my screen.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** My screen is really busy right now.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So last week, one of the bigger action items from Dan was to start discussing some numbers and start looking at some traffic data, Looker Studio, and stuff like that.

**Ehtisham Hussain:** So I have a report for you.

**Ehtisham Hussain:** And then we can talk about the articles and outlines and everything.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So, so we have the data from January up until now.

**Ehtisham Hussain:** Your top performing blogs have been pretty consistent throughout the months.

**Ehtisham Hussain:** It's all always this authentication to Microsoft Graph API and MCP OAuth blog that's bringing in the most traffic.

**Ehtisham Hussain:** I looked at other trends in this, this was kind of interesting.

**Ehtisham Hussain:** So, so I took this data, and I turned it into these charts, so we can actually see how things have been progressing.

**Ehtisham Hussain:** some Мар years.

**Ehtisham Hussain:** to Have

**Ehtisham Hussain:** The average position for blogs, and this is only blog specific, it has been improving since January.

**Ehtisham Hussain:** In January, like we started at the average position of 37.9.

**Ehtisham Hussain:** It went into the late 20s and mid 20s.

**Ehtisham Hussain:** And then most recently, like in August, it has finally, for the first time, the average position has come to less than 20.

**Ehtisham Hussain:** So it's overall, it's a slow progression towards betterment.

**Ehtisham Hussain:** And what we want to do is get it to less than 10 or something.

**Ehtisham Hussain:** And that would be ideal because then that would mean that a lot of blogs are now in the top two or three or four spots.

**Ehtisham Hussain:** So that's a positive trend.

**Ehtisham Hussain:** The average position has been improving.

**Ehtisham Hussain:** The average impressions have been going up significantly in the last few weeks have been really good.

**Ehtisham Hussain:** And there's like almost like a hockey stick going up.

**Ehtisham Hussain:** The impressions have gone from in January, like 20 or February.

**Ehtisham Hussain:** Let's say 28,000, 27,000, now they're at 88,000, so impressions are up, average position is up, the number of clicks, they are, as you can see, they are a plateau, they are around the 400 mark, in some months they have been around 350, 370, 380, last week it was 406.

**Apurva Davé:** Can you just clarify, does this mean, someone's on a blog, and they click on something, taking us, taking them to somewhere else on our website, is that what this means?

**Apurva Davé:** no, no, no, this is like someone finding a blog on a search engine, and then clicking.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So coming to your website.

**Ehtisham Hussain:** Got it.

**Ehtisham Hussain:** Through a blog.

**Ehtisham Hussain:** So, this is kind of plateaued, and this has been just consistent, like it hasn't dropped significantly, it hasn't increased significantly, and the biggest reason behind that is the click-through rate, the click-through rate has been going down, and the click-through rate is, even though your impressions are up.

**Ehtisham Hussain:** And the click-through rate is down.

**Ehtisham Hussain:** That's pretty consistent across different industries, and it's pretty consistent with the trend that we are seeing.

**Ehtisham Hussain:** That's mostly, we are attributing it to AI overviews and zero-click searches.

**Ehtisham Hussain:** A lot of the people are getting information that they would ideally get by visiting your website.

**Ehtisham Hussain:** They're getting it on the search page now because of AI overviews.

**Ehtisham Hussain:** So they are seeing your website, the impression, it counts as an impression, but they're not clicking through because they're already getting the information they need on the search page.

**Ehtisham Hussain:** So the click-through rate is down.

**Ehtisham Hussain:** So that's something, so that was what I found.

**Ehtisham Hussain:** And I think the immediate ideas that I would like to flow to kind of counter that and increase the click-through rate, increase, get some more traffic on the website is two things.

**Ehtisham Hussain:** Number one, it's something that we have already started.

**Ehtisham Hussain:** We've already started some more, like, easier topics to say.

**Ehtisham Hussain:** Even though all topics are technical, as we discussed last week and the week before, but they're kind of like top of the funnel topics and more thought leadership content.

**Ehtisham Hussain:** And that's something we have already started.

**Ehtisham Hussain:** I would also like to propose some case studies, like if you can get some of your higher, like most engaged customers, interview them and turn those interviews into case studies.

**Ehtisham Hussain:** And then you can find a way to distribute them even outside of organic, like we can start distributing them on social and through email.

**Ehtisham Hussain:** If you have a, like, let's say over 10,000 people email list or a highly engaged, let's say 5,000 people email list, we can start other methods of distribution as well to get more traffic onto the website.

**Ehtisham Hussain:** That's one way to counter it.

**Ehtisham Hussain:** Impressions going up means that what you're posting is actually working because people are searching for it and people are seeing it on the page.

**Ehtisham Hussain:** But click-throughs not increasing consistently.

**Ehtisham Hussain:** With the impression that's consistent across industries right now, that's because of AI overviews in most cases, and that's not something that we can control, but we can counter it by these methods, by trying other methods of distribution, and by experimenting with the kind of articles that we're doing.

**Ehtisham Hussain:** Because most of the stuff that you guys have on the website right now that's bringing in a lot of traffic, that's how-to guides, and they are super technical articles, so there's that as well.

**Ehtisham Hussain:** So that's what I had graphic-wise.

**Ehtisham Hussain:** There were two outlines with you on the new topics, which are more like thought leadership and more opinion thesis kind of topics.

**Ehtisham Hussain:** So do let us know if these are good to go, and then we can start creating drafts on them.

**Ehtisham Hussain:** The securing AI agents and LLM workflows without secrets, plus the cloud posture tools don't catch this risk, but IAM will, but attackers will.

**Ehtisham Hussain:** So there's topic as well, and then there's two more outlines that I've planned that are coming your way this week.

**Ehtisham Hussain:** The real risk behind service accounts and service management versus secrets, secrets management versus secrets elimination.

**Ehtisham Hussain:** Plus there's a few that are ready to review.

**Ehtisham Hussain:** I've noticed that Ashur left a few comments over there, Dan left a few comments.

**Ehtisham Hussain:** So do let us know if we should revert to editing or if we should proceed with just finalizing and publishing those articles.

**Apurva Davé:** So just to clarify, on the data, this is all blog-only data.

**Apurva Davé:** It's not...

**Ehtisham Hussain:** Yeah, exactly.

**Ehtisham Hussain:** It's exclusive to blog.

**Ehtisham Hussain:** Okay, that's helpful.

**Apurva Davé:** Okay, and then we do...

**Apurva Davé:** We already do a monthly company newsletter.

**Apurva Davé:** So, you know, per your suggestions regarding like how we can improve the click rate, we...

**Apurva Davé:** I think it would probably be valuable to send you that newsletter, and perhaps you might suggest how we can improve the newsletter for a click-through.

**Apurva Davé:** We get minimal click-through on our newsletter in general.

**Apurva Davé:** Like, it's not a click generator.

**Apurva Davé:** And so, you know, we build our list in very traditional ways, like either people subscribe or these are names we're getting at trade shows.

**Apurva Davé:** And the like.

**Apurva Davé:** So we're, you know, we're doing that stuff, but it's not producing engagement.

**Apurva Davé:** So we'll make a point to send that to you, and maybe you've got ideas on how we can improve that.

**Apurva Davé:** Yeah, that sounds great.

**Apurva Davé:** Okay, yeah.

**Darrell Etherington:** I mean, we had that same problem at TechCrunch, and it was like a, basically it was the, is it a property or is it a driver, right?

**Darrell Etherington:** And you have to key them very specifically for one or the other.

**Darrell Etherington:** So, yeah.

**Darrell Etherington:** I'm curious to take a look, but yeah, happy to do that.

**Darrell Etherington:** Okay, that's great.

**Darrell Etherington:** And then customers, like we're just at a disadvantage here.

**Apurva Davé:** I think we've talked about before, we don't have a lot of customers, which means the pool we have to draw from is very little.

**Apurva Davé:** We have beaten Snowflake to death as a customer reference.

**Apurva Davé:** We're not going to get a lot more out of them.

**Apurva Davé:** Our other big customer is not the kind of company that will do that stuff.

**Apurva Davé:** So we're stuck there for a bit.

**Apurva Davé:** So we have to find other ways to improve the click-through rate, unfortunately.

**Ehtisham Hussain:** All right, all right.

**Ehtisham Hussain:** So case studies are, let's say they're not a practical solution right now.

**Ehtisham Hussain:** Yeah, I don't think of them.

**Apurva Davé:** I mean, we'll get them.

**Apurva Davé:** They'll come, but there's nothing coming in the next eight weeks.

**Apurva Davé:** You know what I mean?

**Apurva Davé:** Like when they come, there'll be few and far between.

**Apurva Davé:** And then, man, when we get one, we can go to town on it.

**Apurva Davé:** But we can't build a strategy around them.

**Ehtisham Hussain:** Yeah, I think of some other ideas.

**Ehtisham Hussain:** As well.

**Ehtisham Hussain:** And until then, we can do thought leadership and top of the funnel.

**Ehtisham Hussain:** These are recently the most recent batch of titles that you approved.

**Ehtisham Hussain:** You must have noticed that there is kind of like a difference.

**Ehtisham Hussain:** The kind of topics that we're going for now, there are more opinion pieces and more thought leadership.

**Ehtisham Hussain:** So that should help too, because that would kind of differentiate from what we have been doing so far.

**Ehtisham Hussain:** Yeah, for sure.

**Apurva Davé:** Although I do think if I recall, I didn't look at all of them.

**Apurva Davé:** was away last week.

**Apurva Davé:** But like, for some of them, I think like the one that Ashur reviewed on the CSPM tools, it sounded like Ashur red flagged that, I think, if I recall.

**Apurva Davé:** And so one of the concerns, I have two concerns on this front.

**Apurva Davé:** One, I think even on this more thought leadership position, we're running into the same kind of content quality problems we were running into on the.

**Apurva Davé:** Deeper ones.

**Apurva Davé:** Maybe I'll, let's do this one first, and then I'll do this, my second observation on that.

**Apurva Davé:** But, Ashur, correct me if I'm wrong.

**Apurva Davé:** I think when I looked at your comments, your reaction was like, I'm not sure I want to even edit this.

**Apurva Davé:** It feels so far off.

**Ashur Kanoon:** Yeah, so I started putting like my general thought on the title.

**Ashur Kanoon:** And that one, that one was, I mean, it looked more like a product pitch for Prisma than anything that was helpful to us, honestly.

**Ashur Kanoon:** Like, that's the conclusion I kind of came up with.

**Ashur Kanoon:** I just don't know how this thing is going to help us in any way.

**Ehtisham Hussain:** I'm just switching over to my...

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Yeah, yeah.

**Ehtisham Hussain:** So it's the Cloud Posture Tools one, right?

**Ehtisham Hussain:** Yep.

**Ashur Kanoon:** All right.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So I'll go through the whole thing, and I'll see what tweaks we can make here.

**Ehtisham Hussain:** But the whole idea was that Aembit can catch these IAM risks.

**Ehtisham Hussain:** We wanted to position Aembit as the thing that would catch the risks that we mentioned in this article.

**Ehtisham Hussain:** And we wanted to say that Cloud Foster tools were not really built for catching those risks.

**Ehtisham Hussain:** Yeah, we're not either, so that's kind of a disconnect.

**Ashur Kanoon:** Oh.

**Apurva Davé:** We stop the risk.

**Apurva Davé:** But we actually don't catch the risk, which is kind of funny.

**Ehtisham Hussain:** Interesting.

**Darrell Etherington:** Catching it implies like a data tool, right?

**Apurva Davé:** Like, I see it, I found this, you should do something about this. It's like, "Hey, your cholesterol is high. You need to deal with that." Or, to continue the analogy, we're the statin — the drug you take that makes the problem go away, but we can't tell you that you have the problem in the first place. We inoculate against it.

**Ehtisham Hussain:** Is that more accurate?

**Darrell Etherington:** Like, even if, even if you're not identifying it, but you're providing an inoculation, or you're providing a curative?

**Darrell Etherington:** Which one is, which is a better?

**Darrell Etherington:** Oh, yeah, we're providing an inoculation.

**Apurva Davé:** Oh, gotcha.

**Apurva Davé:** Okay.

**Apurva Davé:** Yeah, thanks.

**Darrell Etherington:** Thank you.

**Apurva Davé:** I'm clarifying my poorly constructed analogy in medical areas where I have no business being.

**Apurva Davé:** No, I was like, this is a very useful metaphor, but I want to make sure I have the right.

**Ehtisham Hussain:** Yeah, we can rework it to this angle.

**Ehtisham Hussain:** We can rework the article.

**Ehtisham Hussain:** Yeah.

**Apurva Davé:** And then I think Asher's comment was like, like, it sounded like too much of a focus on one, one CSPM.

**Apurva Davé:** It's what I'm reading, Asher, correct me if I'm wrong, I came across as like, cortex this, cortex this, this.

**Apurva Davé:** It's that.

**Apurva Davé:** And this is a class of tools, right?

**Apurva Davé:** Tons of people have them.

**Apurva Davé:** Wiz has it.

**Apurva Davé:** Orca has it.

**Apurva Davé:** Lacework, Sysdig.

**Apurva Davé:** It's a class.

**Apurva Davé:** And so either we refer to just the class of tools and what they do, or we use at least three of these companies, so that we don't feel like we're focused on one of them.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Yeah, this is helpful.

**Ehtisham Hussain:** We can definitely just rework the article with this feedback.

**Apurva Davé:** OK.

**Apurva Davé:** OK.

**Apurva Davé:** And, you know, I flag it mostly because, like, I want to get to a point where things don't come to us in the shape where we just have to outright reject, right?

**Apurva Davé:** That's too much work for us.

**Apurva Davé:** It means we had to do a lot of thinking.

**Apurva Davé:** .

**Apurva Davé:** And I don't like making Ashur think, generally doesn't work out well.

**Apurva Davé:** I don't like making myself think.

**Ashur Kanoon:** Yeah, I know, I know.


**Apurva Davé:** The AI Agents one, which I reviewed, it was okay.

**Apurva Davé:** You know, like, it would have, like, a big mental break in the middle, from my point, from an app point, which I think you corrected, right?

**Apurva Davé:** But then again, like, it felt, it didn't feel actually well thought out.

**Apurva Davé:** Like, it said, like, oh, AI Agents have this new risk surface.

**Apurva Davé:** And then it goes on to list everything which was a standard risk.

**Apurva Davé:** Like, it didn't actually, it felt like the engine didn't put any thinking into what's actually new here.

**Apurva Davé:** What's the old stuff, right?

**Apurva Davé:** So, it seemed to me like there was some, like, it was, like, a fancy title against, like, just the standard positioning.

**Apurva Davé:** And got it.

**Apurva Davé:** And that, that to me, like I was, you know, again, it's like, what, what is the thinking behind the article that gets us to, you know, a good place?

**Apurva Davé:** The, your, your workflows are supposed to get you there.

**Apurva Davé:** And to me, it seemed like this was like, take Ambit's positioning, stick it against a new headline, and you're good.

**Ehtisham Hussain:** All right. Yeah, I'm noting this down. So this is something that is going to need a deeper fix from our side.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** I continue to come back to the point, like, look, if we're writing thoughts.

**Apurva Davé:** Leadership articles here, like you need an opinion and then you need, you know, you need current context to establish, you know, some break from the norm, typically.

**Apurva Davé:** Right. And I don't think the AI Agents article had it.

**Apurva Davé:** And I also don't think that it really tried to think about what's different about AI environments.

**Apurva Davé:** And so, look, we're going to need to improve that if we really want to do thought leadership articles through this method.

**Darrell Etherington:** Yeah, we probably need to introduce a new schema format directive for thought leadership rather than trusting it to do it on its own recognizance.

**Darrell Etherington:** Just a note for our side, Ehtisham.


**Apurva Davé:** Yeah, there was the DevOps one too, but if I recall, I also felt like there was a core problem with the DevOps one.


**Apurva Davé:** I haven't re-reviewed this after Faso's comments. I'll have to take a look at it.

**Apurva Davé:** But there was this miss where it felt like it was throwing everything at DevOps, and that made it unclear. It conflates DevOps and workloads, and there's no reason for that.

**Apurva Davé:** I will review it today.

**Apurva Davé:** My other comment, if I could come back to your top-level point: you mentioned we're moving towards thought leadership articles.

**Apurva Davé:** You also said our most productive articles are technical how-to's.

**Apurva Davé:** Yeah, they're super technical how-to articles.

**Ehtisham Hussain:** you probably know where I'm going with this.

**Darrell Etherington:** Yeah.

**Apurva Davé:** Okay, so great.

**Apurva Davé:** Are we picking up scraps with the thought leadership articles?

**Apurva Davé:** Or do we actually believe they're going to be able to drive a multiple of traffic that the how-to's do?

**Ehtisham Hussain:** Yeah, so the how-to articles have been bringing in the bulk of your traffic.

**Ehtisham Hussain:** But looking at the traffic trends, it's mostly a plateau. Let me share my screen.

**Ehtisham Hussain:** So I had your data here.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** I pulled data for every month — January through April — for all the blogs.

**Ehtisham Hussain:** It's pretty much a plateau. We haven't seen any major dips, but we haven't seen any major highs either, just isolating the blog.

**Ehtisham Hussain:** I didn't look at the whole website — you may have done other campaigns that made a difference elsewhere. But if you just look at the blog, it's pretty much flat.

**Ehtisham Hussain:** So at this point, if you want to break the plateau and do something different, that's what we're proposing. We experiment with thought leadership, top-of-funnel content, and other approaches.

**Ehtisham Hussain:** Your technical how-to blogs will keep bringing that baseline traffic. On top of that, we can add thought leadership and top-of-funnel articles.

**Ehtisham Hussain:** That's an experiment. The other direction is to keep publishing highly technical articles, but you've been doing that for six months without a massive surge in traffic.

**Ehtisham Hussain:** I would agree that it hasn't resulted in a massive surge in traffic.

**Apurva Davé:** And then the question is: will thought leadership articles do that?

**Ehtisham Hussain:** Yeah, that's an experiment.

**Apurva Davé:** I don't have a lot of faith in thought leadership articles driving a massive surge. I'm okay to try the experiment.

**Apurva Davé:** It's probably an SEO question — are we capturing something SEO-wise that thought leadership articles are better positioned to do? I think thought leadership articles don't have a long shelf life, but they have a better chance of being picked up by publications.

**Ehtisham Hussain:** They have a better chance of people engaging with them. If you post them on LinkedIn, you can start a discussion and position yourself as the one who initiated it.

**Ehtisham Hussain:** Yeah, I agree.

**Apurva Davé:** But then back to my other point, this methodology that we're using will not create those articles.

**Apurva Davé:** Based on what I've seen, nothing is friction-based enough, has strong enough opinions, or has the real content backing it up to drive a conversation. It's still very vanilla.

**Apurva Davé:** We're hoping for the wrong thing from the creation method we're using.

**Apurva Davé:** I can't say there's anything we've created that I'd look at and think, "If I post this on LinkedIn, I'll drive a ton of conversation." It's not happening.

**Darrell Etherington:** Like, anecdotally, we have had exactly that feedback from other clients.

**Darrell Etherington:** We posted something and it got picked up and republished by other people. So I don't think it's impossible.

**Darrell Etherington:** Looking at the traffic, the things that drive it are those deeply technical how-tos, which are beyond the capability of any machine.

**Darrell Etherington:** That's a highly expensive, highly manual process.

**Darrell Etherington:** What we're supposed to provide is the volume play — far less per article, but hopefully additive because we can produce volume.

**Darrell Etherington:** That's the alignment we need. Some of it is content, but some is breadcrumb content that establishes authority gradually over time.

**Darrell Etherington:** If I think about it as an editorial publication model — what we used to do at TechCrunch — we covered everything. We were the destination and could self-refer constantly.

**Darrell Etherington:** You build that corpus over months and years. Then it provides huge gains, because you're authoritative, everyone's locked in, and your domain rating goes way up.

**Darrell Etherington:** That's the overall approach and where we fit. Thought leadership, I think, is within reach.

**Darrell Etherington:** We just need to add direction and pipeline specifically for it. You can get the machine to produce contrarian or interesting ideas.

**Darrell Etherington:** What the machine probably can't produce at this point is deeply technical, highly useful how-tos.

**Apurva Davé:** Yeah, I got that. And I don't think what we're doing will get us to deeply technical how-tos.

**Apurva Davé:** But I worry that we're expecting thought leadership articles to get picked up and spark tons of conversation. I haven't seen us get to that point either.

**Apurva Davé:** There's a third thing: surface area. Cover a lot of surface area, create self-reference, and over time that builds a strong basis for traffic.

**Apurva Davé:** That one I fully believe is in the space of what we're doing. I would love to get to thought leadership that really could spark conversation.

**Apurva Davé:** That would be amazing. I'm skeptical, based on what I've seen, that this engine is capable of that. It doesn't seem to have real opinions about anything.

**Apurva Davé:** We haven't developed a method to give it opinions — friction-based, evidence-based, anything-based. That worries me. Surface area, yes, 100%.

**Apurva Davé:** But that's one pillar out of three. That doesn't make a strategy. I'm willing to go forward.

**Apurva Davé:** I'm totally willing to go with the thought leadership approach, but we need changes to make it compelling.

**Apurva Davé:** Maybe the problem is I still write articles for human readers. There's not a lot of human readers, way more machine readers. I might just be misaligned with what the market requires today.

**Ehtisham Hussain:** No, human readership is always going to be there. If we can crack that, the rest should come easy.

**Ehtisham Hussain:** Yeah, I've taken the note. We'll mix thought leadership with top-of-funnel articles. I'm going to work with Darrell to create a new schema with strong opinion directives.

**Apurva Davé:** Last thing: I don't care which kind of article it is. We review them all the same way. Is it interesting? Is it factually correct? Does it have an opinion we can get behind? The review is the same. I don't do anything differently. I don't think our viewpoint should change based on article type.

**Ehtisham Hussain:** So this...

**Ehtisham Hussain:** Today was about reviewing the data and planning next steps on topics to create for your approval.

**Darrell Etherington:** Actually, Ehtisham, we have a hard stop — we have another client call. We can continue async.

**Darrell Etherington:** All right, sounds good.

**Apurva Davé:** Thank you so much.

**Ehtisham Hussain:** Thanks. Goodbye.
