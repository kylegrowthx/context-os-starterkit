# Zoom: GrowthX + a16z

<metadata>
date: 2025-09-04
time: 22:29 UTC
duration: 29 minutes
organizer: Marcel Santilli (GrowthX)
participants: Marcel Santilli (GrowthX), Seema Amble (a16z), Zach Cohen (a16z)
fathom_recording_id: 85161917
fathom_url: https://fathom.video/calls/401321112
share_url: https://fathom.video/share/nVPJVyz67seDbK9Ji5xprhXXsu_6CWe6
source: fathom
enriched_on: 2025-03-02 12:00 UTC
</metadata>

---

## Summary

Marcel Santilli gave a16z partners Seema Amble and Zach Cohen an accelerated demo of GrowthX's internal AI-powered content platform, demonstrating how the company has built infrastructure to scale service delivery starting with content marketing. GrowthX has achieved $11M ARR with only $230K monthly burn and a 40% win rate on ~$200K ACV deals—all without dedicated sales or marketing—and is raising $40-60M to expand engineering from 15 to 25+ people, invest in ML/AI, and pursue adjacent service verticals like e-commerce. Seema and Zach committed to discussing the opportunity with a16z's growth team and signaling back on check size and round dynamics.

---

## Context

GrowthX is a B2B content marketing services company that recently completed a Series A and is now pursuing Series B funding from select tier-one investors. Marcel Santilli founded GrowthX to solve a fundamental gap in marketing: most companies either lack a content catalog or struggle to maintain one, while AI answers (like ChatGPT-powered search results) are collapsing content half-life. Seema Amble and Zach Cohen are a16z partners who have been tracking GrowthX's progress since the Series A—they last met approximately a week after that close—and wanted to see the product that the team had built in the intervening months. This call served as both a product update and a soft open for Series B discussions, with GrowthX emphasizing a thoughtful, selective fundraising approach.

---

## Relevance

**To GrowthX Business Development:**
- A16z's validation is notable: Seema reported that GrowthX is the only marketing tool a portfolio company "really likes" and outperforms 50-75 other marketing companies a16z has met
- 40% win rate on $200K ACV is exceptionally high for B2B services; Seema noted "real ROI" with customers and mentioned they're "the real deal"
- Strong product-market fit signals: $2M MRR added in August while burning only $230K (17:1 ratio), with 70%+ margins trending upward
- Seema's action: discuss with a16z growth team on check size/round dynamics and provide signal same-day; indicates serious interest conditional on a16z's appetite for the quantum

**To CheckThat / AI Visibility Strategy:**
- Marcel framed the entire company thesis around AI answers shortening content half-life and making fresh, credible, comprehensive content the new sales call—this is core to CheckThat's visibility mission
- Platform includes SearchGPT-like ranking visibility tracking across queries with confidence scores; Augment Code case study shows 7+ citations in different AI answer contexts after content work
- Fact-checking workflow demonstrates sophisticated multi-source evidence validation—a capability that mirrors CheckThat's approach to answer accuracy

**To GrowthX Product Development:**
- Internal platform roadmap includes knowledge vault (with confidence scoring and reg attached) and content roadmap feature launching "this week"—these may become SaaS products or marketplace components
- Encoding agent architecture (workflows-as-code) allows scalable execution; agentic loops with evals are improving efficiency while maintaining quality
- Marketplace of experts for production tasks (analogous to data labeling) is being piloted but deliberately not launched yet—team prioritizing quality over headcount efficiency
- Planned expansion from 15 to 25+ engineers suggests significant infrastructure and product build-out ahead

---

## Overview

- GrowthX has developed an AI-powered content creation platform, combining advanced workflows with human expertise
- The company has reached $11M run rate with high capital efficiency (only $230K burn in August)
- GrowthX is raising $40-60M to scale operations, expand product development, and capture market opportunity
- A16z partners expressed interest, noting GrowthX's strong performance compared to other marketing companies they've evaluated

---

## Key Topics

### GrowthX Platform Overview

  - AI-powered content creation platform with context-aware assistants and AI editors
  - Workflow encoding agent writes workflows as code for scalable execution
  - Features include deep research, drafting, fact-checking, and image generation
  - Platform currently used internally by GrowthX team, with plans to expose features to clients incrementally

### Traction and Financial Performance

  - Reached $11M run rate without dedicated sales or marketing efforts
  - 40% win rate on ~$200K ACV deals
  - August metrics: $230K burn, added almost $2M in run rate
  - 70%+ margins, trending upward

### Product Roadmap and Vision

  - Building infrastructure to scale services, starting with content marketing
  - Developing knowledge vault and content roadmap features
  - Exploring adjacent services (e.g., e-commerce catalog management)
  - Potential to offer platform to other agencies in the future

### Fundraising and Growth Plans

  - Raising $40-60M to capitalize on market opportunity
  - Aims to expand engineering team from 15 to 25+ people
  - Plans to invest in ML/AI team for model improvements and efficiency gains
  - Focused on thoughtful, targeted fundraising process with select investors

---

## Action Items

**Seema Amble (a16z)**
- Discuss GrowthX Series B opportunity with a16z growth team regarding check size and round dynamics
- Follow up with GrowthX team today post internal discussion

**Zach Cohen (a16z)**
- Discuss GrowthX Series B opportunity with Seema and a16z growth team regarding check size and round dynamics

**Marcel Santilli (GrowthX)**
- Share data room with a16z upon receiving positive signal on continuing conversation

---

## Transcript

**Seema Amble:** Hey.

**Marcel Santilli:** Hey, how are you?

**Seema Amble:** Good.

**Seema Amble:** I'm going to put a zoom back on.

**Seema Amble:** My computer died, so now I'm on my phone in my home office.

**Marcel Santilli:** Oh, good.

**Marcel Santilli:** How have been?

**Marcel Santilli:** I feel like it's been a minute since the dinner, I think it was last time.

**Seema Amble:** It's been good.

**Seema Amble:** Yeah, I had a baby in the meantime.

**Marcel Santilli:** Oh, my God.

**Seema Amble:** Yeah, a second baby.

**Seema Amble:** Are you talking to us?

**Seema Amble:** Just kidding.

**Marcel Santilli:** I know.

**Seema Amble:** and yeah, anyways, I am on mat leave.

**Seema Amble:** And sorry, that's why I was a little bit slow on the email response.

**Seema Amble:** But no, look, I really like you, wanted to get the update, and I heard you were raising, Zach and I didn't want to miss out.

**Marcel Santilli:** Oh, my God.

**Marcel Santilli:** I am so sorry to take you away from your baby.

**Seema Amble:** That is so much more important than this conversation.

**Seema Amble:** No, no, no, no.

**Marcel Santilli:** going to ask, boy or girl?

**Seema Amble:** A girl.

**Seema Amble:** So I have a boy.

**Seema Amble:** I have a boy and a girl.

**Seema Amble:** So, you...

**Seema Amble:** Thank

**Seema Amble:** You have two kids?

**Marcel Santilli:** One, which is our miracle baby.

**Marcel Santilli:** It's just two years, four months now.

**Seema Amble:** Oh, nice.

**Seema Amble:** Okay.

**Seema Amble:** Yeah.

**Seema Amble:** My son has just turned two.

**Marcel Santilli:** Oh, my God.

**Marcel Santilli:** That is intense.

**Marcel Santilli:** You're a badass.

**Marcel Santilli:** You're a legit badass.

**Marcel Santilli:** That's amazing.

**Marcel Santilli:** Congrats.

**Marcel Santilli:** So happy for you.

**Zach Cohen:** He's underselling how big of a badass he was.

**Marcel Santilli:** I mean, there's no doubt before, but having a two-year-old and a newborn is next level crazy out of those little badass, you know, and hard as hell.

**Seema Amble:** Yeah, it's hard, but yeah, it's a fun age.

**Seema Amble:** Look, guys, we keep hearing good things about you in the market.

**Seema Amble:** It was funny, Marcel, at that dinner, everyone was, I mean, I know a lot of people were your fans there in the audience, but they had great things to say.

**Seema Amble:** So, and actually, it's funny, one of my other partners.

**Seema Amble:** I was like, have you talked to GrowthX?

**Seema Amble:** One of the agencies I work with loves them.

**Seema Amble:** That's the only marketing tool they really like.

**Seema Amble:** So I'm excited to, yeah, wanted to catch up and hear the latest.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** And remind me, have you guys seen the platform?

**Marcel Santilli:** I can't remember last time we actually met, Matt, like how long ago it was, like, because I feel like we built so much.

**Zach Cohen:** So quickly that after your Series A closed, like literally a week after, and I don't think we saw the product.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So maybe, I know we only have 30 minutes, but maybe I can do a super accelerated version of just like walking guys through some stuff, if that makes sense.

**Seema Amble:** That'd be great.

**Marcel Santilli:** Great.

**Marcel Santilli:** Cool, cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So I'll share my screen.

**Marcel Santilli:** I'm going to like fly through a little bit.

**Marcel Santilli:** So bear, bear with me a little bit, but I'll skip intros and things.

**Marcel Santilli:** I think that the main thing like that we're seeing is that I think AI answers just accelerating.

**Marcel Santilli:** The crap out of everything.

**Marcel Santilli:** Essentially, like the first sales call, the way we think about it, happens inside of AI Answer.

**Marcel Santilli:** Now people are spending 15 to 20 minutes.

**Marcel Santilli:** And to be part of that answer, you have to have the most credible, comprehensive, fresh content.

**Marcel Santilli:** And so it just so happened that a lot of what we're building now, this is just accelerating that category of spend, you know.

**Marcel Santilli:** And so kind of fast forward, I think a little bit.

**Marcel Santilli:** I'm sure you guys are seeing a lot of this already in the market.

**Marcel Santilli:** So I can kind of skip through both.

**Marcel Santilli:** One of the things that I think is important to highlight for a show of the platform is just like how hard getting content right it is.

**Marcel Santilli:** And I know like you all have investments in like legal AI, for example.

**Marcel Santilli:** So it's a great analogy of like you wouldn't do a demand letter or a contract or an M&A doc through chat to BT and just trust whatever comes back, right?

**Marcel Santilli:** Like you wouldn't just dump all your due diligence docs from a deal you're working on into chat to BT and then like that's it, right?

**Marcel Santilli:** And so I think the same mentality.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's not always applied to marketing and content and expert-led content that builds trust with your audiences, right?

**Marcel Santilli:** But it's, you know, I would argue just as important because it's part of the growth of the business, you know, and right now distribution is more of a mode than anything else before, right?

**Marcel Santilli:** And so with the AI models, just a lot of it is generic and accurate.

**Marcel Santilli:** Disability tools just point out, you know, where the gaps are, and then workflow platforms are hard to maintain, and agencies, like, every single...

**Marcel Santilli:** Portfolio company you guys have.

**Marcel Santilli:** can go talk to every single marketer and every single one of them, and I almost guarantee you they all hate the agencies they work with.

**Marcel Santilli:** And they all probably feel those are all way too expensive for what they're getting, right?

**Marcel Santilli:** So the way we think about it is content is the atomic unit of marketing.

**Marcel Santilli:** Every part of marketing is content, and a lot of what companies do.

**Marcel Santilli:** Content happens to compound, which is amazing, and like ads and outbound, but it also decays, and AI answers is just causing the half-life to be even shorter, right?

**Marcel Santilli:** So it's decaying even faster.

**Marcel Santilli:** So you have this massive catalog now of these companies do content or no catalog at all.

**Marcel Santilli:** And they either need to build up a catalog that builds their distribution or keep maintaining their catalog.

**Marcel Santilli:** And now it comes more of the unit of value.

**Marcel Santilli:** Nobody wants to buy more tools.

**Marcel Santilli:** And so we're going after this opportunity.

**Marcel Santilli:** Service just happens to be 50 times bigger.

**Marcel Santilli:** And that's why we're tackling services right on within this category.

**Marcel Santilli:** It's just so much bigger than any tool.

**Marcel Santilli:** So, like, that's why none of our deals, we compete with anybody almost.

**Marcel Santilli:** Like, we've not lost deals pretty much, right?

**Marcel Santilli:** We lose deals to inaction and inertia rather than a competitive tool, right?

**Marcel Santilli:** And so I have to kind of show you, like, I think part of what we built under the hood.

**Marcel Santilli:** And so, like, this is our internal platform.

**Marcel Santilli:** And a lot of what we've done is kind of, like, part of the onboarding process.

**Marcel Santilli:** As we go through this eight-week strategy.

**Marcel Santilli:** Since we started doing that about three months ago, knock on wood, we've had 100% conversion.

**Marcel Santilli:** And so a lot of what we do is talk to customers, understand their business, ingest all the artifacts that they have, all the docs, do research on the space, and find their audience better and create these artifacts.

**Marcel Santilli:** This is essentially context engineering, right?

**Marcel Santilli:** Where this is the big picture that you need to feed these workflows.

**Marcel Santilli:** And the way to kind of think about it is, like, everywhere along this, you have a context-aware assistant and an AI editor that's almost like a notion of AI-like editor, right, with shortcuts and things.

**Marcel Santilli:** But also we're tracking every contract with this, like, just like they would with some kind of, like, assistant.

**Marcel Santilli:** But that assistant is context-aware, similar to, like, a cursor-like experience, right?

**Marcel Santilli:** And they can kind of accept or, you know, or reject changes and things like that, right?

**Marcel Santilli:** And then there's a lot more here that I won't

**Marcel Santilli:** Going into like the knowledge base that ingests a bunch of information that we're retrieving as part of our research as we're creating content for them, analytics on all the signals and an inventory of like different assignments and opportunities that we're flagging based on like their site map and all the content and all the AI activity and visibility that we're tracking, right?

**Marcel Santilli:** Every single activity is measured here and tracked here so that we can start to correlate that with the outputs and the outcomes and see what's working and doubling down on that.

**Marcel Santilli:** And then on the editorial side or on the workflow execution side, what we built under the hood is an encoding agent that writes workflows as code that allows us to execute these, if you will, agentic workflows and deterministic workflows in a much more scalable way.

**Marcel Santilli:** So every step of the way here under the hood, there is some kind of workflow and this workflow is all right.

**Marcel Santilli:** So in code and that allows us to just use the coding agent framework that we built that we write every workload in code and run it, right?

**Marcel Santilli:** But the thing that's important here and why we think this is going to win, and this is the right primitive, is that code is now way more maintainable and scalable because of coding agents and because of AI.

**Marcel Santilli:** And so we're leveraging that.

**Marcel Santilli:** So as plot code and others get better and better, like our platform and framework gets better as well and our ability to build more and more powerful, agents and workflows gets better, easier, and faster, right?

**Marcel Santilli:** And so this is an example of a deep researcher one that uses a ton of different APIs and tool calling like EXA, Parallel, Tablet, Perplexity, Deep Research, GPT, Deep Research, and it's doing a bunch of tool calling, defining the success criteria, self-evaluating, running through a bunch of loops, and returning a really deep research year brief, right?

**Marcel Santilli:** And you can see it's

**Marcel Santilli:** It thought for like 11 minutes, and it only uses certain types of sources, and it has even a confidence score for each one of the sections, right?

**Marcel Santilli:** So it's just the beginning of our process, and for every customer, it's different.

**Marcel Santilli:** Same thing with the drafter.

**Marcel Santilli:** There's things like, for example, validating, internal linking, even fact-checking.

**Marcel Santilli:** With fact-checking, think it's one of the best examples here of what's possible.

**Marcel Santilli:** This splits the content into chunks, extracts different passages from each chunk, and comes up with reasoning as well as questions to answer in order to fact-check.

**Marcel Santilli:** And then it researches each one of those and then verifies using evidence, right?

**Marcel Santilli:** And so based on this evidence, it might be something very, very particular in nuance, right?

**Marcel Santilli:** Like lang graph and open hands offer blah, blah, blah, and then this is the evidence and then the suggestive rewrite.

**Marcel Santilli:** It's usually something very, very nuanced that's maybe misattributed or whatnot.

**Marcel Santilli:** That allows us to kind of scale the quality, everything from image to N.

**Marcel Santilli:** Everything else.

**Marcel Santilli:** then the final product of all this is like, Augment Code is a great example.

**Marcel Santilli:** They've been a customer now for, I think, 13, 14 weeks.

**Marcel Santilli:** They've now, this section of the side slash guys is 100% generated by us, the images, everything else.

**Zach Cohen:** And you can see like, this is, you know, user in this system, is it on the company side or is it with GrowthX is?

**Marcel Santilli:** Yeah, GrowthX side, and that's a great question.

**Marcel Santilli:** Like, so we have over the point experts that are managing editors and strategists that this is all delivered as a service today.

**Marcel Santilli:** And we're exposing the platform incrementally over time.

**Marcel Santilli:** And so for now, like, it's 100% internal.

**Marcel Santilli:** But think of it as like, over time, we're leaving behind a Palantir-like platform.

**Marcel Santilli:** You know, it's a good thing.

**Marcel Santilli:** We're essentially choosing to expose just the stuff that we know people will able to digest.

**Marcel Santilli:** Like, let's say, like, weekly we have, like, a report of your SEO or GEO, so that's going to be, like, a...

**Marcel Santilli:** Or maybe we have like an internal version of all the knowledge base that we incorporate, so you can have like a perplexed life experience with your internal stuff, but the team is creating, sticking together the workflows and perform the creation.

**Zach Cohen:** And then how do you think about scaling the internal team, especially like the deployed team, like number of humans per account, I'm assuming that's like what a lot of these tools are going to go after, but the team does seem still pretty large today.

**Marcel Santilli:** So I'm curious, like, you know, your revenue going up with number of humans, like, I mean, Palantir talks about this stuff all the time.

**Marcel Santilli:** Yeah, so there's a couple of different angles there, right?

**Marcel Santilli:** Like, so the forward deploy, there's a point where you can't defy gravity, or at least we believe, right?

**Marcel Santilli:** Like, where we need to understand the companies, like Sentinel One, we have to talk to multiple stakeholders, get a line in, like, in order for you to be successful, there's a reason Palantir has forward deploy people as well, right?

**Marcel Santilli:** Like, there's a point of that.

**Marcel Santilli:** But then on the production side, part of our roadmap is...

**Marcel Santilli:** Building a marketplace of experts for some of the production.

**Marcel Santilli:** So we can think of it as very analogous to like a data labeling pipeline where, you know, or a human feedback pipeline where the part of the production can be delegated or fact-checking or, or not fact-checking, or production or quality checking, you know, can be delegated to a marketplace.

**Marcel Santilli:** And, and you can eval that and, and essentially like have like places where though there's multiple workflows trying multiple different things and you're returning multiple results to then a human that can select who one's the best, you know, there's a lot of different pieces of that that are way more scalable from that perspective.

**Marcel Santilli:** But then what we're finding like, for instance, like here, where this is already like our third or fourth evolution of this for this customer, where now we're like collapsing some of these workflows into agentic loops with evals now that we have a lot more data and, and know what quality it looks like, right?

**Marcel Santilli:** And so, so that.

**Marcel Santilli:** That's why it's getting way more efficient and effective.

**Marcel Santilli:** But I think part of this is also knowing that, hey, if you solve for efficiency early, you don't solve for how to get to grade and how to deliver value to customers.

**Marcel Santilli:** And that's where I think people are going to make a mistake if they try to solve for the headcount efficiency.

**Marcel Santilli:** For us, the reason this could all be a marketplace and it could look like we have only 30 headcount in the company.

**Marcel Santilli:** We didn't do that because you don't want the person hitting publish for abnormal security to be a random freelancer in a random country that's going to steal data or something, right?

**Marcel Santilli:** Like, so for now, like, we wanted to really optimize for quality over, like, headcount.

**Marcel Santilli:** But with 70% plus margin trending up, we'll feel pretty confident in the ability to create even more leverage.

**Marcel Santilli:** And then, like, one quick example and then, like, we can kind of dig in is, like, with augment code, like, we publish all these guides.

**Marcel Santilli:** But I think a lot of what we're seeing the results is, you know, that this is an example of searching for AI coding tools.

**Marcel Santilli:** Enterprise's augment code now is mentioned and they weren't before, but now they're not only cited once, twice, three, four, five, six, seven times, you know, and they're showing up in a bunch of different places and a bunch of different queries as well in AI answers.

**Marcel Santilli:** And so a lot of it is like, if you're not part of the answer, you're kind of non-existent in a lot of ways, right?

**Marcel Santilli:** And they've also just hit like an all-time high already on traffic, the content of creator for them at this point.

**Marcel Santilli:** And so we're seeing a lot of really, really positive momentum there.

**Marcel Santilli:** And so that's a little bit of the TLDR.

**Marcel Santilli:** can dig in a little bit more on the platform and kind of what we're building.

**Marcel Santilli:** And then really quickly on the traction, you guys probably read it in the memo.

**Marcel Santilli:** I think we're really, really efficient.

**Marcel Santilli:** We got to 11 million run rate.

**Marcel Santilli:** We just hired first salesperson, so pretty much without sales, without a lot of marketing.

**Marcel Santilli:** And mostly word of mouth, and we're really capital efficient.

**Marcel Santilli:** In August, we only burned $230K and added almost $2 million in run rate.

**Marcel Santilli:** And so we're feeling really, really positive, a lot of really great signals from customers, a lot of upsells in the work right now that were unsolicited, of customers coming to us asking for more.

**Marcel Santilli:** And yeah, and then we're raising 40 to 60, and a ton of other things we can walk through, and we're happy to share a data room if there isn't.

**Seema Amble:** Maybe one other thing to touch on is where you guys are heading in terms of, like, roadmap, and, like, what do you want this to be in five years?

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** I think, like, the way to think about what we're building in a lot of ways is, like, we're building the things we need in order to scale service, and we're tackling service starting with content because content is the atomic unit for marketing.

**Marcel Santilli:** But this applies just so much more.

**Marcel Santilli:** And so in

**Marcel Santilli:** A lot of ways, you have the platform, and then the infra, the marketplace, and then software, kind of almost like plays, right?

**Marcel Santilli:** Yeah, the way we're thinking is that, first thing, we've been doing things in phases, as in like, okay, what is your initial question, what's the head count?

**Marcel Santilli:** So we started with one account, we started with like, three or four people in the beginning, see how they work, figure out what they're doing that could be automated, could be like, more efficient, and then what are the features that will power that, and then see if we can reduce and maintain the quality or increase quality.

**Marcel Santilli:** And like, for, and internally, that's why we have this internal tool just for ourselves, because we can move a lot faster by training our own people.

**Marcel Santilli:** Like, when we roll all the new version, I can just like, literally get 40 people in the room, say, that's how it's going to be now, but the whole user base is trained.

**Marcel Santilli:** So we can shift super fast.

**Marcel Santilli:** So in turn, our internal roadmap...

**Marcel Santilli:** App is essentially all the features that we see that will reduce the amount of people but increases quality at the same time.

**Marcel Santilli:** So, so far has been the workflows run time, the ability to inspect the workflows, the ability to see the tracing data of what happened, and then stitching together the workflows was the thing that we worked in the last couple of months, and now we're working on finishing the knowledge vault and finishing the content roadmap.

**Marcel Santilli:** So, those are two things that people who struggle today, how do I create content out of internal data or data that was fact-checked by our team that we know is fully accurate.

**Marcel Santilli:** So, like we have a knowledge graph with a reg attached to that that we're already shooting this week, and then we have a content roadmap feature that essentially you see the opportunities extracted from your website, and then you can see the work getting moved along, and when it's finished and it's ready to read there you

**Marcel Santilli:** You have the whole timeline of the work getting done.

**Marcel Santilli:** So those are two things that we saw, like, okay, we're hitting all the time with these things.

**Marcel Santilli:** And I tried first with, like, off-the-shelf tools like AirTable or using some other knowledge base, and then eventually we see how much capacity we can add.

**Marcel Santilli:** So the internal side, we have the six things that Marcel has on the screen on the left side, what we call GrowthX internal platform.

**Marcel Santilli:** We don't expect to make this whole thing accessible to customers or to sell that.

**Marcel Santilli:** Maybe over time, maybe, like, a couple of years from now, I think next year, we have deteriorated so much on it that onboarding a new pod is so quick that we can start selling this to other agencies or a new version of this can be sold to other agencies.

**Marcel Santilli:** But as we do that, there's a bunch of things that we know we use all the time with every client.

**Marcel Santilli:** So those we already expect.

**Marcel Santilli:** So we're extracting, like, a recording tool for GEO and invisibility, example.

**Marcel Santilli:** We're extracting a few other things.

**Marcel Santilli:** So things are repeating.

**Marcel Santilli:** And those are what we can expect as regular SaaS, or even free, so a small listing will be free.

**Marcel Santilli:** And then we have the marketplace, which is a separate platform, and we have the infrastructure for us to create workflows as well, that we can use with anything, like ProOcto we use for sales, enabling.

**Marcel Santilli:** So we have a few experiments that we're running with some clients, to see how well our infrastructure will do with different domains.

**Marcel Santilli:** Yeah, and then like, just to touch on kind of like, from overall, I kind of go to market as well, it's not only the service, there's a lot of adjacent services that our customers are in.

**Marcel Santilli:** We know there's hundreds of billions in spend that we're going after.

**Marcel Santilli:** And then there's adjacent services, there's additional services, there's new verticals and kind of use cases.

**Marcel Santilli:** So for instance, catalog for e-commerce, like PLPs, PDPs, you know, like there's the RealReal, and a few others, like have been reaching out to us and asking.

**Marcel Santilli:** Okay.

**Marcel Santilli:** And then on the apps and software, kind of these standalone plays that are a huge kind of place as well for us.

**Marcel Santilli:** And so that's kind of a high level.

**Marcel Santilli:** don't know if that answers the question.

**Zach Cohen:** Sorry.

**Seema Amble:** Yes, I think this was very helpful.

**Zach Cohen:** Sorry.

**Seema Amble:** I was on mute.

**Zach Cohen:** And then I guess, like, you know, a little bit, like, why raise 40 to 60?

**Zach Cohen:** seems like you guys are growing really fast.

**Zach Cohen:** You know, your burn multiple is pretty low.

**Zach Cohen:** You know, why is now the right time to raise?

**Marcel Santilli:** Why that quantum of capital?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, I think, like, right now, the way we kind of think about it is we're very capital efficient, but we also have a massive surface area to go execute against, right?

**Marcel Santilli:** And we think this is a once in a lifetime opportunity.

**Marcel Santilli:** To go win the service space for marketing and sales services, that is a massive category that people are underestimating how much work it's going to be to go win that category, but also how much pain and willingness to pay and move people have.

**Marcel Santilli:** And that's why we have like almost a 40% win rate on a 200K almost ACV with zero marketing and sales spend, right?

**Marcel Santilli:** Like, and it's like, I've never seen it before in my whole career and I've been in a lot of fast growing companies, you know, that done very, very well, you know, and so for us, it's like, it's a once in a lifetime opportunity to go really, really build out and the surface area that we're building is like pretty, pretty substantial as well.

**Marcel Santilli:** And so three things is like the, continue to build the infra, it's the platform and some of these self-serve plays that we have in the marketplace.

**Marcel Santilli:** But it's also investing and go to market more, more aggressively, you know, and for us, like raising 20, 30,

**Marcel Santilli:** It wouldn't make that much of a difference because we are capital efficient.

**Marcel Santilli:** We really want to double down on all these things.

**Marcel Santilli:** So we have over seven built lanes here and about 14 or so principal engineers that are staff in these lanes.

**Marcel Santilli:** We should have a really more significant footprint here.

**Marcel Santilli:** And everything you see here, it's been around 12 months, but really the engineering team has been mostly staffed in the last three or four months.

**Marcel Santilli:** So hopefully it's kind of the slope of change that you see as well.

**Marcel Santilli:** Yeah, well, essentially, each one of these blocks here could be almost like a company itself.

**Marcel Santilli:** And we don't want to understaff that.

**Marcel Santilli:** It can't be just one person in front of the blocks.

**Marcel Santilli:** It has to be like at least two and then get the best people we can and don't have to like undertake somebody or get somebody super cheap but try to squeeze them out with a bunch of PMs.

**Marcel Santilli:** So we're kind of staffing the team a lot of former founders or former managers that got excited about the app.

**Marcel Santilli:** I didn't want to be building in this space.

**Marcel Santilli:** So we have 15 people today.

**Marcel Santilli:** think I could easily use 25 just on the product team.

**Marcel Santilli:** And we also need to start staffing our ML and AI team to start helping with prompt improvements, find 20 models, all the little stuff that could be micro models that would be added to that efficiency.

**Marcel Santilli:** And over time, just be also an infrastructure itself as well.

**Zach Cohen:** Awesome.

**Zach Cohen:** Do you have any questions for us?

**Zach Cohen:** know we're coming up on the hour, so I want to make sure that we don't just pepper you.

**Seema Amble:** Yeah, I feel like we have a good sense of what you're doing, especially since I think we just chatted.

**Seema Amble:** It feels like just a few months ago.

**Seema Amble:** And by the way, I did ask all the people at my table at the dinner what they thought of you guys.

**Seema Amble:** So I have a good sense of how the product's working now.

**Marcel Santilli:** Yeah, that's perfect.

**Marcel Santilli:** I think for us, the main thing is we're keeping this process.

**Marcel Santilli:** Thank Thank

**Marcel Santilli:** This fairly, like, small and thoughtful, I think, of just, like, we're not trying to involve every single company out there.

**Marcel Santilli:** Like, we filter out anyone that we thought had, like, a lot of investments and, you know, that didn't follow kind of, or people that already believe in services software and kind of get us and have been building the relationship since Series A.

**Marcel Santilli:** And so it's, like, I think we're in a good place.

**Marcel Santilli:** We're mostly in, like, fourth, fifth meetings or partnership meetings this week.

**Marcel Santilli:** And so we're hoping to kind of get back to building as quickly as possible, but obviously also be thoughtful and appreciate and have empathy for the process, you know, because this is a partnership.

**Marcel Santilli:** And there's a lot of layers to our business.

**Marcel Santilli:** So obviously, like, super, super flexible, but also just don't want to waste time on either end.

**Marcel Santilli:** And so it's mostly, like, you know, understanding, like, we're not for everyone.

**Marcel Santilli:** I think we're extremely confident we're going to win this space, and it's a massive space.

**Marcel Santilli:** And it's

**Marcel Santilli:** also not a winner-take-all, but we do think there's not any or almost any player approaching the space the way we are.

**Marcel Santilli:** And by space, I mean marketing services overall.

**Marcel Santilli:** And so we want to be aggressive and seize the opportunity.

**Seema Amble:** Yeah, so why don't – Zach and I will chat, but I think given this quantum of check size that you're looking to around size that you're raising, we should chat with our growth folks and just get their two cents as well.

**Seema Amble:** That's what we often do with like series BCCs.

**Seema Amble:** I – yeah, look, we've looked at – I don't know, Zach, we've probably met 50 to 75 companies in marketing, and most of them are not doing even a fraction of how well you are.

**Seema Amble:** And so clearly I think you've seized the demand and like obviously offered a product that people want.

**Seema Amble:** And like I said, I've chatted with enough people who use you and they're like, yeah, this is the real deal.

**Seema Amble:** And like it's dollars actually.

**Seema Amble:** Yeah.

**Seema Amble:** Where there's real ROI in spending here.

**Seema Amble:** I know your process is moving quickly.

**Seema Amble:** So why don't we sync up on our side and then channel with our growth team?

**Seema Amble:** then if you – the data room would be very helpful because I think that just helps us get through, get feedback faster if it's easy to share.

**Marcel Santilli:** Yeah, yeah, it's definitely easy.

**Marcel Santilli:** I think for us, like, the main thing is just, like, we're just being very thoughtful of, like, when we're sharing.

**Marcel Santilli:** I think perhaps just, like, give us just a quick signal of, like, yes, let's continue the conversation before we kind of, like, open up every single thing.

**Marcel Santilli:** But we've already shared the data room with 10 investors.

**Marcel Santilli:** And so it's not, like, a matter of, like, we don't want to share.

**Marcel Santilli:** It's just making sure that it's, like, we're sharing in the process of continuing the conversation as well.

**Marcel Santilli:** But as long as give us a thumbs up, like, even a text message real quick or anything, like, we'll share you immediately, you know, just to say, like, yes, absolutely, we definitely want to continue the conversation, yeah.

**Seema Amble:** Yeah, I –

**Seema Amble:** Look, I think for us, the conversation is really around, like, check size and, like, that round dynamic more so than if that wasn't the pace, think I'd absolutely, I would just tell you right now, yes.

**Seema Amble:** So let Zach and I just chat and then with our growth folks and then come back to you today.

**Marcel Santilli:** Sounds good.

**Marcel Santilli:** Well, we're super excited.

**Seema Amble:** And, again, sorry to take you away from the family.

**Seema Amble:** No, no, Sorry, I have to hop in the car because we're running to a doctor's appointment.

**Seema Amble:** But, yeah, no, great to catch up.

**Marcel Santilli:** And I'm not surprised at all that the business has continued to rip.

**Marcel Santilli:** So that's awesome.

**Marcel Santilli:** Yeah, likewise.

**Seema Amble:** We'll talk soon then.

**Seema Amble:** Okay.

**Zach Cohen:** All right.

**Seema Amble:** Good to see you guys.

**Marcel Santilli:** See you guys later.

**Marcel Santilli:** See you guys next time.

**Marcel Santilli:** Bye.

**Marcel Santilli:** Bye.
