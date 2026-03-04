# Glenn Lawyer -Technical Discussion Interview | Data Scientist

<metadata>
date: 2025-12-09
time: 21:58 UTC
duration: 66 minutes
organizer: katja@growthx.ai
participants: Katja Wittfoth, Glenn Lawyer
fathom_recording_id: 107527391
fathom_url: https://fathom.video/calls/500371810
share_url: https://fathom.video/share/8UTmkwyNmGjcfnhPu8QSSPRaECUstz5r
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Technical interview with Glenn Lawyer, Staff Data Scientist at Invoca, exploring his background in neuroscience and machine learning, current work on attribution models, and his LLM-based labeling project that reduced client onboarding from two weeks to two days. Katja and Glenn discussed GrowthX's challenge of measuring brand visibility in LLM search and explored a framework for testing LLM behavior against top search queries weighted by Google popularity, with focus on understanding how user search behavior translates from Google to LLM interfaces.

---

## Context

This is a technical interview between Katja Wittfoth (GrowthX AI advisor) and Glenn Lawyer (Staff Data Scientist at Invoca) conducted as part of GrowthX's AI and data science hiring exploration. The meeting was structured to cover Glenn's background, deep dive into one of his recent projects, and discuss GrowthX case studies. Glenn brought 15 years of experience spanning academia (neuroscience, evolutionary dynamics), startup founding (CyberHedge acquisition), and technical roles at scale (Stripe, Invoca), making him valuable context for GrowthX's product strategy around AI visibility and LLM search. The second half pivoted to a strategic discussion about how to measure and optimize brand visibility in LLM responses, where data and measurement approaches are far less transparent than traditional search engine optimization.

---

## Relevance

**To GrowthX Delivery:**
- LLM labeling framework demonstrates major operational win: reduced Invoca's model onboarding from two weeks to two days while maintaining 80-90% accuracy. Directly applicable to GrowthX client data labeling workflows and onboarding efficiency.
- Validation methodology (holding out human-labeled data to test LLM performance across multiple verticals) provides replicable approach for assessing LLM-based automation on GrowthX deliverables.
- Practical insight on bag-of-words vs embedding models for noisy conversational data is relevant for GrowthX's work on phone-based and conversational signals.

**To CheckThat / AI Visibility:**
- Core challenge: measuring LLM visibility is fundamentally different from Google SEO. LLMs train on documents (not query-log-driven), making traditional keyword-weighted metrics fragile. Suggests need for multi-channel approach (Google keywords as proxy, social mention mining, digital twin focus groups).
- Hypothesis that user behavior in LLMs mirrors Google behavior (question-asking vs keyword search) is testable and foundational to CheckThat's positioning. High entropy in keyword queries vs low entropy in natural-language questions could indicate reinforcement learning optimization.
- Risk flag: LLM paid placement (Sam Altman has announced plans) will corrupt organic visibility metrics, requiring transparent communication with clients about long-term vs short-term stability.

**To GrowthX Business Development:**
- Glenn's skepticism about sustained LLM visibility measurement (fragile due to opaque data, lack of query access, potential paid placement) should inform how GrowthX frames its AI visibility value prop—as a long-term strategic play (weeks, months, years), not a quick-win channel.
- Glenn's emphasis on metric improvement over controlled experiments suggests GrowthX should set expectations around measurement approaches and timelines, differentiating from Google SEO's faster feedback loops.
- Reference potential: Glenn's multi-year experience with AI adoption friction (institutional inertia, skepticism to buy-in) mirrors challenges GrowthX will face scaling AI visibility with enterprise clients.

---

## Overview

- **Background:** Glenn Lawyer has 15 years in academia (neuroscience, evolutionary dynamics) and experience at startups (CyberHedge, acquired) and large tech (Stripe).
- **Current Role:** As Staff Data Scientist at Invoca, he manages the core marketing attribution model—a complex, multi-channel Bayesian Pitman-Yor model—and leads the company's AI pivot.
- **Key Project:** Developed an LLM-based labeling tool that cuts client onboarding from two weeks to two days. The project was CEO-endorsed but shelved for \~6 months due to institutional inertia before being greenlit for production.
- **Growthx Case Study:** Proposed measuring LLM brand visibility by querying top LLMs with weighted Google search phrases. This approach is a scrappy, short-term solution, as the future of LLM search is uncertain (e.g., paid placement, lack of query data).

---

## Key Topics

### Background & Experience

  - **Academic:** PhD in neuroscience (structural MRI), postdoc in evolutionary dynamics (viral spread).
  - **Startups:** Co-founder of CyberHedge (acquired). Built the tech stack and team as the first technical hire.
  - **Stripe (1.5 yrs):**
      - **Project:** Investigated misbilling issues for enterprise clients.
      - **Finding:** The core problem wasn't pricing anomalies but client frustration over unpredictable invoices from variable card mixes.
      - **Solution:** Built a simple AR(2) time-series model to flag these unpredictable bills, enabling proactive CSM outreach.
  - **Invoca (Current):** Staff Data Scientist.
      - **Company:** 350-person firm providing marketing attribution for inbound phone calls.
      - **Role:** Manages the core attribution model and leads the AI pivot.

### Invoca: Core Model & AI Pivot

  - **Core Model:** A multi-channel Bayesian Pitman-Yor model with six layers of priors.
      - **Rationale:** A bag-of-words approach is superior to embeddings for spoken language, which is noisy and contains sparse, high-signal words (e.g., "new patient").
  - **AI Pivot:** Invoca is pivoting to an "AI-first" strategy.
      - **LLM Labeling:** Using LLMs for bulk data labeling, reserving humans for edge cases.
      - **Embedding Models:** Exploring for simpler, out-of-the-box signals.
      - **AI Agents:** Building agents trained on human agent call data to replicate their conversational style.

### Invoca: LLM Labeling Project

  - **Problem:** Custom model onboarding took two weeks due to slow human labeling.
  - **Solution:** Developed an LLM-based tool to automate labeling.
      - **Process:** LLM labels calls → Trains model → Evaluates on new LLM-labeled data.
      - **Result:** Reduced onboarding to two days with minimal performance loss.
      - **Validation:** LLM was correct 80–90% of the time; manual review showed the LLM was often right even when it disagreed with human labels.
  - **Production:** The project, initially shelved for \~6 months, was greenlit after the company's AI pivot gained traction.

### Growthx Case Study: Measuring LLM Brand Visibility

  - **Challenge:** Measuring brand visibility in LLM search, where data is opaque and the future is uncertain.
  - **Proposed Solution (Short-Term):**
    1.  **Define Queries:** Use top Google search phrases, weighted by their popularity, as a proxy for LLM queries.
    2.  **Query LLMs:** Run these phrases against major LLMs (e.g., OpenAI, Gemini).
    3.  **Measure:** Track brand mentions and rank in responses to create a weighted visibility score.
  - **Hypothesis:** User behavior will be stable, with users asking questions in LLMs as they do in Google.
  - **Verification:** Test the hypothesis by comparing response variability between natural-language questions (low entropy) and keyword-based queries (high entropy).
  - **Long-Term Challenge:** The model is fragile due to opaque LLM data, potential paid placement, and evolving user behavior.
  - **Measuring Impact:** Use metric improvement over time, as controlled experiments are not feasible without holdout groups.

---

## Action Items

- **GrowthX:** Test hypothesis on user behavior in LLMs vs Google by comparing response entropy between natural-language questions and keyword-based queries across OpenAI and Gemini.
- **GrowthX:** Design focus group or digital twin study to validate search phrase similarity between Google and LLM user behavior.
- **GrowthX:** Plan for long-term LLM visibility measurement strategy; communicate to clients that optimization is a weeks-to-months-to-years investment, not a rapid-feedback channel like Google SEO.

---

## Transcript
**Glenn Lawyer:** How are you?

**Glenn Lawyer:** Doing great.

**Glenn Lawyer:** How about you?

**Katja Wittfoth:** Very good.

**Glenn Lawyer:** Where are you located?

**Glenn Lawyer:** I'm in beautiful Carmel, Indiana.

**Katja Wittfoth:** That sounds fun.

**Katja Wittfoth:** Is there...

**Glenn Lawyer:** Actually, today was warm.

**Glenn Lawyer:** We got up into the high 40s, so the snow is melting.

**Katja Wittfoth:** Well, yeah, we have roughly 50s, I guess.

**Katja Wittfoth:** High 40s, too, in the area.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah, well, your weather is generally going to be better than mine, unless you're in the city itself enjoying the fog.

**Katja Wittfoth:** I guess, I guess.

**Katja Wittfoth:** But, yeah, very nice to meet you, and thanks for taking the time to chat with us.

**Katja Wittfoth:** My name is Katja, and I'm helping growthx in AI and data science as an advisor, and helping them hiring data science team, as well as here and there, especially in research and running some AI visibility studies as well.

**Katja Wittfoth:** So today, roughly the plan is as follows.

**Katja Wittfoth:** I would love to learn more about you, your recent work.

**Katja Wittfoth:** We'll deep dive in one of your projects.

**Katja Wittfoth:** And then I have a couple of case studies focused on growthx.

**Katja Wittfoth:** I would love to chat through with you.

**Katja Wittfoth:** Does that sound good to you?

**Glenn Lawyer:** Yeah, it sounds really good.

**Katja Wittfoth:** It sounds good.

**Glenn Lawyer:** The point of procedure, though, you had to hear about one of my projects and to do a couple of case studies.

**Katja Wittfoth:** So I'm going to need you to track the time on this, because I don't know how much time you want for each of these.

**Katja Wittfoth:** And just tell me when we're getting close.

**Katja Wittfoth:** Oh, well, sounds good.

**Katja Wittfoth:** Okay.

**Katja Wittfoth:** And I'll also elaborate if I want like a short, high-level details or maybe some more deep dive.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** So maybe I'll start with you.

**Katja Wittfoth:** If you can tell me a little bit about yourself, that would be.

**Glenn Lawyer:** Yeah, so I've always liked building things, and I've got sort of a mathematical bent of mind.

**Glenn Lawyer:** So that, of course, meant building mathematical models of the way the world works, and that's what got me into data science.

**Glenn Lawyer:** Lucky enough, in my PhD, I could apply this to actually understanding how the human brain works.

**Glenn Lawyer:** I was in a neuroscience lab, so playing with the structural MRI, and then decided as long as I'm on big questions, I got to spend my postdoc figuring out how life itself works.

**Glenn Lawyer:** That's grandiose, but I was looking at evolutionary dynamics and how things, you know, look at viruses, which are real-time, and I could see also how they spread through time and space.

**Glenn Lawyer:** So some really nice stuff there, looking at evolutionary patterns and adoption.

**Glenn Lawyer:** Fifteen years in academia from the master's all the way through the end of the postdoc was enough for me to realize I should make some life changes.

**Glenn Lawyer:** So I decided to start my own companies.

**Katja Wittfoth:** Companies?

**Glenn Lawyer:** Yeah, yeah, the first two didn't work out so well.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** But by then, I'd kind of figured out a little bit more about what needed to be done.

**Glenn Lawyer:** So the second two actually did work pretty well.

**Glenn Lawyer:** Actually, one of them just got acquired about three months ago.

**Glenn Lawyer:** So that felt nice.

**Glenn Lawyer:** And one of those that worked the best, CyberHedge, I was running that for four years, co-founder.

**Glenn Lawyer:** There's the founder, and I was the first hire.

**Glenn Lawyer:** So I didn't actually found it, but it was him and me for a while, and I did all the technical stuff.

**Glenn Lawyer:** He's non-technical.

**Glenn Lawyer:** Brilliant operator, just non-technical.

**Glenn Lawyer:** After four years, I'd solved the hard problems.

**Glenn Lawyer:** I'd built a solid tech stack that could deliver our solution and the team, more importantly, the team that could actually build and extend that tech stack.

**Glenn Lawyer:** Stripe called me up, and I thought it might be interesting to make a shift, so I did.

**Glenn Lawyer:** Spent a year and a third, year and a half, something like that.

**Glenn Lawyer:** Stripe, but there's a little bit of friction because I'm not used to large organizations and no shade on Stripe, but when you're running a 7,000, 8,000 person company that's in a highly regulated space, you know, I prefer being able to move a little faster and having a little bit more accountability and ownership of my own projects.

**Glenn Lawyer:** So I ended up at Invoca where I am working on mapping out the differences between LLMs and other types of embedding models, which are trained on written word, how, what actually happens when you take these and apply them to spoken word, because we're looking at telephone transcripts and things don't always match up.

**Glenn Lawyer:** So having some fun looking at that intersection right now.

**Katja Wittfoth:** What do they do in Invoca exactly?

**Glenn Lawyer:** I'm staff data scientist on the data team.

**Katja Wittfoth:** No, I mean the, the company.

**Glenn Lawyer:** Oh, company.

**Glenn Lawyer:** Yeah, sorry.

**Glenn Lawyer:** Two things.

**Glenn Lawyer:** The company started by making...

**Glenn Lawyer:** In the link between online advertising and inbound sales calls, let's say you run a dentist office, are you selling some other high-touch product?

**Glenn Lawyer:** You put out your ad on Google, call us to get your children's teeth cleaned, it's the start of your special.

**Glenn Lawyer:** Now your phone starts ringing.

**Glenn Lawyer:** You don't know if it's coming from that Google ad or something else.

**Glenn Lawyer:** We help bridge that gap by rotating phone numbers, so when the person calls, it's one of our numbers, and now we've got the inbound phone calls.

**Glenn Lawyer:** The next question is, okay, so your phone is ringing, but are they calling in response to the ad?

**Glenn Lawyer:** And that's what my team does, is we look at those transcripts and says, what happened on the transcript?

**Glenn Lawyer:** Was it a new patient or was it an existing patient calling to schedule for their kids?

**Katja Wittfoth:** So that's sort of like marketing attribution?

**Glenn Lawyer:** It's exactly marketing attribution, yes.

**Glenn Lawyer:** And it's solving some core issues in marketing attribution.

**Glenn Lawyer:** Okay, so it's basically a provider of marketing attribution models, right?

**Glenn Lawyer:** Yes, yeah, to specializing on things.

**Glenn Lawyer:** Yeah, that's, your summary is good.

**Katja Wittfoth:** And they basically provide that service to any of the company who wants to know their attribution?

**Glenn Lawyer:** Yeah.

**Katja Wittfoth:** In offline, right?

**Katja Wittfoth:** You're saying it's offline?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Obviously, you're not going to buy from us if it doesn't make sense for your company.

**Glenn Lawyer:** But there are a lot of businesses, especially in the U.S., that have rely on inbound telephone calls to close the deal.

**Katja Wittfoth:** Would you say it's more like a small businesses, like in your example?

**Glenn Lawyer:** No.

**Glenn Lawyer:** I gave you the example of a dentist office, but it's not going to be a single dentist running an office.

**Katja Wittfoth:** It's going to be a nationwide chain.

**Katja Wittfoth:** Okay.

**Katja Wittfoth:** So they need to know what works.

**Glenn Lawyer:** I can tell you one of our marquee customers is AutoNation.

**Katja Wittfoth:** I don't know.

**Glenn Lawyer:** What is this?

**Glenn Lawyer:** On AutoNation, they sell cars.

**Glenn Lawyer:** Cars online.

**Katja Wittfoth:** Okay.

**Glenn Lawyer:** So, but, you know, people also call them to sell a car or to buy a car or, you know, buying a car is a kind of a high-tech thing.

**Glenn Lawyer:** And, you know, they want to know if people are calling them.

**Glenn Lawyer:** Are they calling for it to buy the car?

**Glenn Lawyer:** they calling for service?

**Glenn Lawyer:** Are they, you know, why is this person calling us?

**Glenn Lawyer:** And to be able to analyze that at scale.

**Katja Wittfoth:** So they, you basically, it sounds like the company is focusing more on calls rather than.

**Glenn Lawyer:** Yeah.

**Katja Wittfoth:** And everything else.

**Katja Wittfoth:** Because, like, given the company has a billboard, that's not part of UICP, right?

**Glenn Lawyer:** Correct.

**Katja Wittfoth:** Correct.

**Glenn Lawyer:** Yeah, we're focusing on the.

**Katja Wittfoth:** Inbound calls.

**Glenn Lawyer:** Yeah, it's the inbound calls is really our secret sauce.

**Glenn Lawyer:** And that's what we promise.

**Glenn Lawyer:** So if you don't have people calling you, what would be, we'll take your money, but we're not sure what we'll give you in return.

**Glenn Lawyer:** So it's, you know, it's an awkward fit.

**Glenn Lawyer:** So if you do have those inbound calls, we can do a lot.

**Glenn Lawyer:** And of course, we're looking to grow and, you know, what can we do that expands this and supporting call centers and things.

**Katja Wittfoth:** you know, every company.

**Katja Wittfoth:** big is the company?

**Glenn Lawyer:** 350 people.

**Katja Wittfoth:** Oh, and how big is the data team?

**Glenn Lawyer:** Data team is actually really small.

**Glenn Lawyer:** I have two other data scientists on my team.

**Glenn Lawyer:** Then we have two guys who are running the actual platform.

**Glenn Lawyer:** But I have to be a little careful here.

**Glenn Lawyer:** The company's been around for 20, 25 years or so.

**Glenn Lawyer:** So there's also other teams that have built a lot of infrastructure.

**Glenn Lawyer:** We have this massive pipeline.

**Glenn Lawyer:** You know, we have the raw telephone call, basically an MP3 file.

**Glenn Lawyer:** So we're managing the ring switches.

**Glenn Lawyer:** We actually, when you call in, it's going through one of our switches on the telecom network.

**Glenn Lawyer:** That's how we get the transcript.

**Glenn Lawyer:** And so there's the people building that and there's taking the raw audio files and turning those into text, that's obviously a data science project, but I don't touch that.

**Glenn Lawyer:** That's not the data science team.

**Glenn Lawyer:** So when I say it's only a few people in the data science, I'm ignoring a lot of people doing a lot of really hard technical data science-y kind of work, but that's, it's, you know, it just helps.

**Katja Wittfoth:** So it's you and another two data scientists?

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** Manager is technically really, really competent as well.

**Glenn Lawyer:** So he's not just a good manager, but he's a hands-on data scientist.

**Glenn Lawyer:** That's helpful.

**Katja Wittfoth:** And you guys are like full, full, full stack team doing from analytics to ML.

**Glenn Lawyer:** Interesting definition.

**Katja Wittfoth:** Or is there a separate, separate analytics ML team?

**Glenn Lawyer:** We recently brought in an ML team to help with some of our ML modeling.

**Glenn Lawyer:** So, uh, they're doing, I, these buzzwords get really confusing, Katja.

**Glenn Lawyer:** Uh, ML used to mean one thing and that's...

**Glenn Lawyer:** It's of what I'm doing, but ML now means training an embedding model, and that's what this other team is doing.

**Glenn Lawyer:** So if ML means are you running XGBoost to make predictions, that's one thing.

**Glenn Lawyer:** If you mean setting up a training pipeline to maintain an embedding model in production, that's another thing.

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** So, yeah, we have a team that we brought in to actually manage some of the AI infrastructure in production that we're moving towards.

**Katja Wittfoth:** Our core product is actually a bespoke in-house ML product.

**Glenn Lawyer:** I don't know how deep your knowledge goes.

**Glenn Lawyer:** Obviously, you know what a bag of words model is.

**Katja Wittfoth:** Yeah, yeah.

**Glenn Lawyer:** And you probably heard of latent Dirichlet allocation?

**Katja Wittfoth:** Yes.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Okay, so that's the typical way people do a bag of words.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** The Dirichlet prior is interesting, but it doesn't handle fat-tail distributions well.

**Glenn Lawyer:** The better model is a Pitman-Yor, which is a variation on the Dirichlet.

**Glenn Lawyer:** And what we have...

**Glenn Lawyer:** is a multi-channel Pitman-Yor model that has like six layers of Bayesian priors on it.

**Glenn Lawyer:** It's a really advanced statistical model, which does make a difference, and that's the model I'm responsible for.

**Glenn Lawyer:** So, yeah, it's basically a backwards-latent Dirichlet allocation, except the stats are much deeper and much more.

**Katja Wittfoth:** Interesting.

**Katja Wittfoth:** Interesting that your core model is Bayesian and core, right?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Well, again, some of this comes down to the difference between spoken and written word.

**Glenn Lawyer:** If you're going to do matching based on similarity, the definition that the embedding model uses for similarity has to match the way people talk.

**Glenn Lawyer:** And if you'll excuse me, the plan, so I was calling about the plan that I was talking about, that's what I want to do, is talk about the plan.

**Glenn Lawyer:** That's how people talk on calls.

**Katja Wittfoth:** Yeah, yeah.

**Glenn Lawyer:** I was cartooning it a little bit, but that is so far from the written word that all the uhs, all the fillers, the fact that they say the plan...

**Glenn Lawyer:** Three times because they're trying to put their thoughts together when they're calling about their insurance plan.

**Glenn Lawyer:** I filed the claim and I'm calling about the claim that I filed.

**Glenn Lawyer:** You know, this is what really happens.

**Glenn Lawyer:** That's not the embedding models miss that.

**Glenn Lawyer:** You have these large gaps between words.

**Glenn Lawyer:** So actually a bag of words model does a better job of filtering out the noise and anything else.

**Glenn Lawyer:** And the other thing is, let's say we want to know if a person is a new patient or an existing patient.

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** That's signal we're looking for on the call.

**Glenn Lawyer:** The call goes for 15 minutes.

**Glenn Lawyer:** There's eight words that distinguish a new from an existing patient on this 15 minutes.

**Glenn Lawyer:** The rest is noise.

**Glenn Lawyer:** So an embedding model is going to try to figure out mostly noise.

**Glenn Lawyer:** A bag of words can actually say, hey, these are the 10 words that matter.

**Glenn Lawyer:** And it doesn't matter how close they are.

**Glenn Lawyer:** There's a lot of room there, you know.

**Glenn Lawyer:** My job right now is experimenting with the better ways of moving this forward, using more embeddings and everything.

**Glenn Lawyer:** It's not a clear win.

**Katja Wittfoth:** How much LLM and GNI do you actually use versus statistical models?

**Katja Wittfoth:** And where do you find it more useful and less useful?

**Katja Wittfoth:** Like one of the examples you gave of a bag of words you find actually a patient's status, very helpful.

**Katja Wittfoth:** But if you can talk more.

**Glenn Lawyer:** also a lot cheaper to run, which also matters.

**Glenn Lawyer:** You know, maybe let's say that the LLM is more accurate, but if it costs you 100x to run it, can you actually affordably run the LLM and everything for a 3% performance gain?

**Glenn Lawyer:** You know, so that comes in.

**Glenn Lawyer:** So to answer your question, some of this, remember, I joined the company a year ago, so I can't be totally responsible for the product stack.

**Glenn Lawyer:** Let's

**Glenn Lawyer:** The company itself had this model.

**Glenn Lawyer:** The team that it created it had just quit.

**Glenn Lawyer:** So they had been a toxic manager that they'd replaced, but not before the damage was done.

**Glenn Lawyer:** And all of this before I joined.

**Glenn Lawyer:** So this is stuff I found out after I joined the company.

**Glenn Lawyer:** My current manager is amazing.

**Glenn Lawyer:** So I really liked the company, did the right thing there.

**Glenn Lawyer:** But basically, they brought me in as the guy who could actually understand this model and make it work.

**Glenn Lawyer:** So that was my first responsibility.

**Glenn Lawyer:** And now the company itself is really making a massive pivot into AI.

**Katja Wittfoth:** That is one of our core things.

**Glenn Lawyer:** Because again, you know, also where the market is going.

**Glenn Lawyer:** So I've been participating in that.

**Glenn Lawyer:** We are looking very strongly at using more AI powered models for doing some of this same analysis.

**Glenn Lawyer:** But it's not quite as straightforward as you initially think, because the spoken is different from the written and the models are trained on the written or the example.

**Glenn Lawyer:** Yes, I can take a telephone transcript, jump into an LLM, and get pretty accurate signal out whether or not they're a new or existing patient.

**Glenn Lawyer:** I know this.

**Glenn Lawyer:** I've tested it.

**Glenn Lawyer:** It obviously works.

**Glenn Lawyer:** It's just too expensive.

**Glenn Lawyer:** Now, could I train a smaller embedding model?

**Glenn Lawyer:** Is it possible to a distilled model that could do the same thing?

**Glenn Lawyer:** Well, before I say yes or no on that, let's pretend that it's a yes to make things easy, and that's such an obvious win.

**Glenn Lawyer:** Great.

**Glenn Lawyer:** Now I've got to convince the company that that's the tech stack that we should build and build this new product, which, again, is doable.

**Glenn Lawyer:** And I can't tell you if that's happening or not because it's proprietary, but you see that's not something that it's like, hey, this is the solution, and it's there in two weeks.

**Glenn Lawyer:** There's time to build that and all the infrastructure around that model.

**Glenn Lawyer:** So even if I do do that and show that it works and show the cost savings or the advantages, I can't say that we have that in production yet.

**Katja Wittfoth:** But, you know, what are some of the ideas?

**Katja Wittfoth:** Like, that's totally understandable, especially if the company was around, you said, 20 years.

**Katja Wittfoth:** It's likely they're moving a little slower, but what are the, you see as a huge potential for a new tech stack as LLM to this problem?

**Glenn Lawyer:** Yeah, so some stuff that does make a huge difference, a lot of our models do use human labeling.

**Glenn Lawyer:** I think that never totally goes away, partly because there's some inertia in our company to keep them, and partly because the LLMs are really good, except on the edge cases, and we actually do need to handle the edge cases.

**Glenn Lawyer:** But we can still leverage LLMs to do the bulk of labeling.

**Glenn Lawyer:** That's one very clear huge win in my own group.

**Glenn Lawyer:** There's a lot of other AI wins across the whole company that I don't want to go, I'll give you a quick example of this.

**Glenn Lawyer:** We're, we'll make an industry report, and we'll specialize this for 10 different industries.

**Glenn Lawyer:** One of our CSMs is really happy that they can use AI to make this process.

**Glenn Lawyer:** So there's stuff like that that happens across the company.

**Glenn Lawyer:** I don't think you're asking about that because I don't touch that.

**Glenn Lawyer:** The CSM is doing that themselves.

**Glenn Lawyer:** But within our own tech stack, certainly the labeling is a clear win.

**Glenn Lawyer:** Some of our other cheaper signals were, you know, I mentioned the gold package, which is you can really customize for basically whatever signal you want to find on the model.

**Glenn Lawyer:** Some of our more out-of-the-box signals, we are moving towards using embedding models in different forms, and that's something I'm deeply involved in.

**Glenn Lawyer:** Of course, everybody wants to build agents.

**Glenn Lawyer:** So if I tell you that we're building agents, that shouldn't be a surprise.

**Glenn Lawyer:** I can't give you details because, again, it's proprietary and public announcements we've made.

**Glenn Lawyer:** But there's some things that an intelligent observer from the outside could see.

**Glenn Lawyer:** What would we offer as our discrimination factor on the agents we'd offer?

**Glenn Lawyer:** Well, we have all the telephone calls, so we know how your human agents handle calls.

**Glenn Lawyer:** And that would allow us to make an AI agent that has the same understanding that your human agents do.

**Glenn Lawyer:** So that's something that the company is exploring quite heavily.

**Glenn Lawyer:** And that, of course, means we'd need to then extract some of this data from these telephone calls to be able to pull it off.

**Glenn Lawyer:** And again, an intelligent outside observer could conclude this fairly easy.

**Glenn Lawyer:** So I'm not telling you anything confidential, but that's some of the projects we're working on that I promise.

**Katja Wittfoth:** Sounds great.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** And as I mentioned, I think those are the main things.

**Glenn Lawyer:** If we stick to the current product, what's happening on the phone call, labeling for the basing model when that's appropriate, embedding models for when that's less appropriate, extending new products, as I mentioned, to understand what happens on the calls and turning that into agents.

**Katja Wittfoth:** Is that like a custom for every client is different, what they're trying to do?

**Katja Wittfoth:** up not?

**Katja Wittfoth:** Achieve, or is it like a common across different clients?

**Katja Wittfoth:** What are you trying to get?

**Glenn Lawyer:** Well, let me give you an example.

**Glenn Lawyer:** I already mentioned we work with dentist offices.

**Glenn Lawyer:** So, of course, I can't tell you the national chains we work with, but it doesn't matter because it's a dentist office, right?

**Glenn Lawyer:** We also work with some national chains for insurance companies.

**Glenn Lawyer:** And both of these clients would want to know if the person is a new client or an existing client.

**Katja Wittfoth:** Okay.

**Glenn Lawyer:** So, in a sense, yeah, there are things that are common across all clients.

**Glenn Lawyer:** But the question is, is the model going to be the same?

**Glenn Lawyer:** Because existing a new client is different with a dentist office than it is with an insurance company.

**Glenn Lawyer:** So you would build a different model then for… Yeah.

**Glenn Lawyer:** Well, I mean, again, that's one of the open questions.

**Glenn Lawyer:** On certain signals, we can have out of the box.

**Glenn Lawyer:** We might want to have industry-specific ones.

**Glenn Lawyer:** And that actually is, you know, these are…

**Glenn Lawyer:** Lower tier products are the industry-specific model.

**Glenn Lawyer:** So yeah, you're an insurance company.

**Glenn Lawyer:** We have one that's worked for a lot of insurance companies.

**Glenn Lawyer:** It's set up.

**Glenn Lawyer:** You press go and it goes.

**Glenn Lawyer:** And of course, we can fine-tune one specifically for your data if you pay us a little bit more money and get the gold package instead of the silver package.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** What made you join the company?

**Katja Wittfoth:** And you mentioned that the Stripe was a big company and that you were looking for the switch.

**Glenn Lawyer:** Is that the reason?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** And I liked Invoca because, again, it was a unique chance to actually look at the core problem or a core problem with AI is the difference between conversational and written.

**Glenn Lawyer:** I don't know.

**Glenn Lawyer:** I'm not saying that's the biggest business problem out there.

**Glenn Lawyer:** That might not drive the most business value, but scientifically or technically, it's extremely interesting.

**Glenn Lawyer:** And I think that might be – it's a route towards –

**Glenn Lawyer:** What could be a fundamental breakthrough in AI as we move forward?

**Katja Wittfoth:** For Stripe, actually, was it in person in the area or remote?

**Glenn Lawyer:** No, no, it was remote.

**Glenn Lawyer:** Oh, remote, okay.

**Katja Wittfoth:** At Stripe, what are some of the projects you worked on?

**Glenn Lawyer:** Yeah, I had a couple that I was doing.

**Glenn Lawyer:** So the main one was I was embedded in the Miss Billing platform team.

**Glenn Lawyer:** Context on this, let's say you're running your company and you do all your online purchases through Stripe.

**Glenn Lawyer:** You get an invoice from Stripe, you think it's wrong.

**Glenn Lawyer:** You're going to call the Miss Billing team at Stripe to figure out why your invoice isn't what you expect.

**Glenn Lawyer:** So, I mean, it's a level of the B2B level of Miss Billing.

**Glenn Lawyer:** And the initial mandate was based on the assumption...

**Glenn Lawyer:** That if there's a misbilling, it's probably because there's an anomaly in our pricing structure.

**Glenn Lawyer:** So I was looking for anomalies in the pricing structure and assuming that was driving misbilling.

**Glenn Lawyer:** Turns out that there actually aren't that many anomalies.

**Glenn Lawyer:** Stripe is really good.

**Glenn Lawyer:** There had been historically in their grow fast era, they had been a little less rigorous on their pricing, but they tended to catch these things in time before they became catastrophic and fix them.

**Glenn Lawyer:** So that conception turned out to not be totally accurate on what the problem was.

**Glenn Lawyer:** Stripe didn't know this partly because we didn't have good data over what was actually causing the misbilling.

**Glenn Lawyer:** So at first I was looking at detecting anomalies and I developed and delivered some algorithms for that.

**Glenn Lawyer:** And then I started organizing the data on the misbilling board to understand what were actually the different root causes and the financial impact of each one.

**Glenn Lawyer:** From that work, I realized that one of the biggest drivers of customer pain was actually things that were fairly invisible.

**Glenn Lawyer:** It was our larger clients, enterprise-level clients, who could not predict what their Stripe invoice was because it depended on, for example, changes in the card mix.

**Glenn Lawyer:** And this was very frustrating to clients.

**Glenn Lawyer:** They didn't understand why the same amount of revenue passed through Stripe would have a different invoice each month, invoice amount.

**Glenn Lawyer:** These complaints were also invisible because, again, Stripe is pretty good.

**Glenn Lawyer:** So, I mean, the invoice might be off by $100 here or there.

**Glenn Lawyer:** These are really complex billing sites.

**Glenn Lawyer:** So, you know, being off by $100 is actually amazingly accurate.

**Glenn Lawyer:** But it would take hours or days of time for the poor analyst to figure this out.

**Glenn Lawyer:** And the customer is still upset because the bill was wrong.

**Glenn Lawyer:** You know, and they didn't care if it was $1 million too much or $100,000 too much or $100,000 too little.

**Glenn Lawyer:** It's not the direction.

**Glenn Lawyer:** It's the fact that now they...

**Glenn Lawyer:** Like their accounting is off and they can't predict their costs.

**Glenn Lawyer:** It's just really bad.

**Glenn Lawyer:** So I switched to building an anomaly detector that would see if these bills.

**Katja Wittfoth:** What type of model was it?

**Glenn Lawyer:** It's super simple, super simple, lightweight.

**Glenn Lawyer:** Basically, I was using an autoregressive model, two lags on it.

**Glenn Lawyer:** We're looking at the percentage of revenue.

**Glenn Lawyer:** How much, how many dollars are you passing through Stripe in terms of, you the total card transaction amount and how much we need for that?

**Katja Wittfoth:** Autoregressive time series model?

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** Super simple.

**Glenn Lawyer:** It was good enough.

**Glenn Lawyer:** It was identifying enough of these big ticket ones that the guy who was dealing with them was happy with it and also pointed in the right direction.

**Glenn Lawyer:** And it was also predictive because one of the other interesting things is it's not so much that these enterprise clients are half stable.

**Glenn Lawyer:** There was clients that suddenly ramped up into enterprise.

**Glenn Lawyer:** And this is a really interesting signal to throw up.

**Glenn Lawyer:** These guys are really wrapping up.

**Glenn Lawyer:** But maybe we wanted to have a heads up that you might get a call from them that their bill isn't quite what they expect.

**Glenn Lawyer:** So that was also – and if you get a phase change in the way the growth trajectory is going with an AR2 model, it's going to be an outlier.

**Glenn Lawyer:** I was flagging some of those as well.

**Glenn Lawyer:** But when we looked at those, those were actually clients that was worth making the CSM aware of because it was going to lead to opportunity.

**Glenn Lawyer:** Yeah.

**Katja Wittfoth:** Strength is generally very, very much known for – as far as I heard, it's a strong team that does a lot of controlled experiments and sophisticated measurement in statistics of their analytics.

**Katja Wittfoth:** Was there anything like that you were working on during this time?

**Glenn Lawyer:** I know exactly what you're talking about.

**Glenn Lawyer:** I forget the name of the staff data scientist who built the experiments platform.

**Glenn Lawyer:** It's called Kepler.

**Glenn Lawyer:** That's the internal Stripe name for it.

**Glenn Lawyer:** I think you work with Paige Bassini.

**Glenn Lawyer:** You can ask her about it so she can give you some details.

**Glenn Lawyer:** I believe she's also at Mercury.

**Katja Wittfoth:** She used to be.

**Katja Wittfoth:** Used to be.

**Glenn Lawyer:** Yeah, okay.

**Glenn Lawyer:** Yeah, that's right.

**Glenn Lawyer:** She did move on, didn't she?

**Glenn Lawyer:** That experiments platform is heavily tied to A-B testing.

**Glenn Lawyer:** And one of the things that Stripe does really, really well is make sure that that checkout service that you're going to embed in your website is smooth.

**Glenn Lawyer:** It's super smooth because of all the A-B testing.

**Glenn Lawyer:** So that's where a lot of the experimentation is focused.

**Glenn Lawyer:** They're also really strong on the fraud detection.

**Glenn Lawyer:** I was able to actually give some advice to one of the fraud guys we brought in because handling extreme distributions was challenging for him.

**Glenn Lawyer:** And I've got some background in extreme distribution theory.

**Glenn Lawyer:** So, yeah, Stripe does have some very sophisticated models.

**Glenn Lawyer:** But simple wins.

**Glenn Lawyer:** I'll go sophisticated if we need to.

**Glenn Lawyer:** And I gave you the example of that in Invoca when we have the Pitman-Yor model.

**Glenn Lawyer:** And I didn't go too much into detail, but it's not a Pitman-Yor prior.

**Glenn Lawyer:** We have six levels of these Pitman-Yor priors, one for the agent track, one for the caller.

**Glenn Lawyer:** And I actually understand and can visualize this in my head.

**Glenn Lawyer:** So, yeah, I can do that.

**Glenn Lawyer:** And, yes, in that case, it's sufficient.

**Katja Wittfoth:** But why do that if you don't need to?

**Katja Wittfoth:** Well, we will talk more about experimentation in metrics during the case study discussion.

**Katja Wittfoth:** But maybe last question to your background.

**Katja Wittfoth:** Maybe let's go a little deeper in one of the projects.

**Katja Wittfoth:** If you can share one of the recent projects you're extremely proud of and just talk me through that.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Well, let's go with one of the ones with the LLM.

**Glenn Lawyer:** And for the labeling, because that's actually.

**Glenn Lawyer:** Topical and hit some of this.

**Glenn Lawyer:** So I said we have this Pitt manure model, which of course is going to, it's semi-supervised.

**Glenn Lawyer:** So we label, let's call it 100 calls, 100 true, 100 false, or 50 true, 50 false, just toy, toy numbers.

**Glenn Lawyer:** This was all done with human labeling.

**Glenn Lawyer:** And we would actually do it in rounds of, they'd label 40 calls, we'd train the model, they'd label another 40 to evaluate it, we'd train the model.

**Katja Wittfoth:** I inherited this, by the way, not saying I designed it that way.

**Glenn Lawyer:** But there's also the initial round zero.

**Glenn Lawyer:** So it took basically about two weeks for a customer to spin up a custom model.

**Glenn Lawyer:** And this is quite annoying to the customers, as you can imagine.

**Glenn Lawyer:** So I took a passion time, we have quarterly passion times.

**Glenn Lawyer:** I forked the production code.

**Katja Wittfoth:** What is passion time?

**Glenn Lawyer:** Oh, it's, you have three days where you can basically, I mean, there's a theme, you're supposed to, this one was built.

**Katja Wittfoth:** Well,

**Glenn Lawyer:** So I forked the production code.

**Glenn Lawyer:** I put an LLM classifier in front of this that would randomly select, randomly start pulling calls and labeling the calls until it had a balanced data set of 100 calls, would train the model, get the model results back, label another 100 calls to evaluate the fit, and then see how that worked.

**Glenn Lawyer:** Then turn it over to human to evaluate it.

**Glenn Lawyer:** So that's an interesting...

**Glenn Lawyer:** Framework, I tested that framework on existing models where we actually had a few hundred labeled human calls.

**Glenn Lawyer:** So I was not using the LLM to evaluate how well it predicted the LLM.

**Glenn Lawyer:** I could hold out the human labeled calls, train the LLM and see how well it predicted on human labeled calls, and then measure model performance, which I was did over, I don't think I got as far as 10, but I was testing over six or seven different clients from very different industry verticals.

**Glenn Lawyer:** And I was able to show that doing this, we should be able to onboard a client in two days instead of two weeks.

**Glenn Lawyer:** And that the LLM, again, I told you earlier that it's struggles with edge cases, but it actually does pretty good for 80 to 90% of the calls.

**Glenn Lawyer:** That's why I know those numbers.

**Glenn Lawyer:** I looked at those calls.

**Katja Wittfoth:** I looked at every single one where the LLM disagreed with the human.

**Glenn Lawyer:** 90% of the time the LLM was right, but there were edge cases and there were times where the LLM was just stupid.

**Glenn Lawyer:** And so I was able to show that we could actually use LLMs to measure.

**Katja Wittfoth:** Do you guys deploy the approach?

**Glenn Lawyer:** Well, there's a fun story behind that one.

**Glenn Lawyer:** The short answer is yes, but it took a little bit to get there.

**Glenn Lawyer:** Among other things, are 85 people who did passion time projects, which you want know with 150 or so engineers in the company is roughly what you'd expect.

**Glenn Lawyer:** The CEO, not the CTO, the CEO called out my project.

**Glenn Lawyer:** It was one of only two that we used to demo afterwards at the Nextall Company All Hands.

**Glenn Lawyer:** He said, is the kind of stuff we love.

**Glenn Lawyer:** So definitely got the top-level buy-in from that.

**Glenn Lawyer:** I also told you that the company is pivoting to be AI first.

**Glenn Lawyer:** When I joined, they weren't.

**Glenn Lawyer:** There's a lot of skepticism around AI, and I know you've seen the debate in public, so you know all the arguments.

**Glenn Lawyer:** The C-suite has been working really hard to pivot our company to be an AI first company because they recognize we need to make this change, and there was some institutional inertia.

**Glenn Lawyer:** I think they've done that now.

**Glenn Lawyer:** now.

**Glenn Lawyer:** Watching the Slack channels, I can see now how, I told you about this customer, whoever it was, maybe it was an account executive, but the person generating the report and how they could massively speed their time.

**Glenn Lawyer:** So we've now have the cross-company buy-in that LLMs really are useful and helpful.

**Glenn Lawyer:** And what I didn't tell you is I did this project, they all thought it was great and it got set on the shelf.

**Glenn Lawyer:** And I was thinking, why?

**Glenn Lawyer:** You know, this turns onboarding time from two weeks to two days and removes major point of customer annoyance.

**Katja Wittfoth:** Why aren't we just, and it's off production code.

**Glenn Lawyer:** So it's not hard to slot it into production.

**Glenn Lawyer:** You know, I didn't build this as a toy toy.

**Glenn Lawyer:** It's a fork of the production pipeline.

**Glenn Lawyer:** But they wanted to make sure we had institutional buy-in and now we've got it.

**Glenn Lawyer:** And the project has got greenlit about three weeks ago, two weeks ago.

**Glenn Lawyer:** And the team that manages our customer-facing interfaces is working on building it out.

**Katja Wittfoth:** It took a couple of months, right?

**Katja Wittfoth:** Yeah, it took six months.

**Glenn Lawyer:** Five, six months, four months.

**Katja Wittfoth:** Do you generally actually work together with product managers and execs, or is it far away from your team?

**Glenn Lawyer:** Invoca structure has the data science team is doing more prototyping, stock work, and then we hand over to the other teams to make the production implementation.

**Glenn Lawyer:** I do work really closely with the PM on that prod team because I need to know what his concerns are and his thoughts are to make sure that what we're prototyping matches with where he's taking things.

**Glenn Lawyer:** So, yes, I work very closely with him, and a lot of that is actually just listening to him.

**Glenn Lawyer:** If he has a tech problem, I'm answering it for him, making little tools for him to make his life easier.

**Glenn Lawyer:** So, yes, we work closely with him, but the way that

**Glenn Lawyer:** company is structured, that's actually, it's another team's job to build this out.

**Glenn Lawyer:** And again, would I set up my company that way if I was doing things?

**Glenn Lawyer:** Well, that's really not a question I can ask because I didn't set this company up.

**Katja Wittfoth:** It's how it is.

**Glenn Lawyer:** Yeah.

**Katja Wittfoth:** A lot of times also what I see in my career is like even if you build something super cool that is reducing some time on bringing efficiency or bringing more revenue, it is another part that's bringing it to the crowds and convenience.

**Glenn Lawyer:** How would you like generally go about that and then try to promote and try to execute on the project?

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** And you're right.

**Glenn Lawyer:** It's not just me who has this thing.

**Glenn Lawyer:** It's common in the tech world.

**Glenn Lawyer:** So, first of all, you want to make sure that people in the company know you care.

**Glenn Lawyer:** So, when

**Glenn Lawyer:** I told you I work closely with the PM.

**Glenn Lawyer:** He knows that I'm trying to solve his problems.

**Glenn Lawyer:** I monitor the chat for the people who are actually selling and delivering this Pitman-Yor model I talked about.

**Glenn Lawyer:** So I see what they're struggling with.

**Glenn Lawyer:** I don't always jump in to help them because it's not always appropriate, but I've got an eye on it.

**Glenn Lawyer:** I have jumped in and helped enough that I've, oh, I've gotten one or two awards from the company from this.

**Glenn Lawyer:** It's not major shout outs like I was the level two instead.

**Glenn Lawyer:** I wasn't the top performer for engagement, but I was the number two for supporting last quarter, got 200 bucks for it.

**Glenn Lawyer:** And then, you know, the winner gets a thousand.

**Glenn Lawyer:** But I have enough engagement that people know that I actually care and care about their concerns.

**Glenn Lawyer:** That's the first thing.

**Glenn Lawyer:** And secondly, that I'm delivering quality.

**Glenn Lawyer:** So when I'm presenting this, it's like, OK, here's what I found.

**Glenn Lawyer:** Here's the data that backs it up that shows these gains.

**Glenn Lawyer:** It's there's actually some measurements behind it.

**Glenn Lawyer:** And here's my estimate of what it would.

**Glenn Lawyer:** to turn this into a production system.

**Glenn Lawyer:** So they have hard numbers from a person who they know cares and who is otherwise appears credible.

**Glenn Lawyer:** That's basically all you can do.

**Glenn Lawyer:** Honestly, Katja, this is one of the areas where I'm really growing.

**Glenn Lawyer:** If you look at my CV or from what I told you, when I was in academia, that was never a problem because I always got to decide my own projects.

**Glenn Lawyer:** That's not always common in academia, but even in the PhD, said, okay, this is the next paper I'm going to write.

**Glenn Lawyer:** Nobody was telling me what papers to write.

**Glenn Lawyer:** I was doing my own thing all the way through.

**Glenn Lawyer:** In startups, if I'm running the company or if I was the first employee, it's like, if I say this goes into production, it goes into production.

**Glenn Lawyer:** So that was kind of, it's a heavy responsibility and you have to be really careful with it, but it was never, I was the guy you had to convince.

**Glenn Lawyer:** It wasn't me trying to convince other people.

**Glenn Lawyer:** I was the decider on that.

**Glenn Lawyer:** And it was only when I got to Stripe that I suddenly realized that, whoa, wait a second, even if this thing is a real innovation that really does make a difference, that's not always the answer.

**Glenn Lawyer:** So I learned some things from Stripe on how to do that.

**Glenn Lawyer:** I'm learning more at Invoca, and it's a growth area for me.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Well, let's switch over to your case study and talk more about growthx.

**Katja Wittfoth:** Yes.

**Katja Wittfoth:** So first thing I would love to discuss with you is, so growthx helps generally a marketing team and growth team for their clients.

**Katja Wittfoth:** But one part of that we are trying to figure out is with a new LLM search, right?

**Katja Wittfoth:** Like before it was just Google, and now we have plenty of LLM searches.

**Katja Wittfoth:** How would you think about...

**Katja Wittfoth:** Um...

**Katja Wittfoth:** Um...

**Katja Wittfoth:** Um...

**Katja Wittfoth:** And how would you define and measure it?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah, that's actually, I'm going to give you a quick answer now, but this is one of the core questions.

**Glenn Lawyer:** And the challenge with core questions is the quick answer is usually incomplete.

**Glenn Lawyer:** You have to actually put it into the second or third.

**Glenn Lawyer:** So I'm putting that caveat out there because I'll give you an answer that sounds credible, but I also know that there's going to be gaps in it, and I don't know where those are yet.

**Katja Wittfoth:** It's just brainstorming.

**Glenn Lawyer:** Yeah, yeah, I know, I know, I know, I know.

**Glenn Lawyer:** But I've been around this circle too many times.

**Glenn Lawyer:** So basically what the high-level view is, there are certain phrases that people are going to use which should surface your brand.

**Glenn Lawyer:** So we'd maintain a list of those.

**Glenn Lawyer:** So we would run those against, and again, I'm not thinking yet of budget, how much this is going to cost, but we have a list of the major AI providers.

**Glenn Lawyer:** I think that's a short enough list.

**Glenn Lawyer:** We can keep that at 10.

**Glenn Lawyer:** I made up the 10 bit.

**Glenn Lawyer:** I'm thinking, you know, we have Google, OpenAI, we have Grok, and then Gemini, which is Google again, Microsoft.

**Glenn Lawyer:** So that's four or five, and let's make it 10 just to get out of numbers.

**Glenn Lawyer:** So we have 15 or 20 credible search terms.

**Glenn Lawyer:** You can't necessarily say that per company, but we can say it per brand, because a company can run multiple brands, right?

**Glenn Lawyer:** But per brand or per product line, however the company slices it.

**Glenn Lawyer:** We take these 15 search term phrases, run them down the 10 different AIs, and measure how often their company is mentioned in the output.

**Glenn Lawyer:** So, for example, example, example,

**Glenn Lawyer:** I know you mentioned first for each one of these, and that tells you the other things you need to also monitor are the phrases you're using, matching with what people actually do.

**Glenn Lawyer:** And that's one of the key weaknesses to this model.

**Glenn Lawyer:** But basically, run search phrases measure how often your company gets the top hit for these phrases.

**Katja Wittfoth:** And how would you develop a metric for measurement of the brand visibility?

**Katja Wittfoth:** Would you just, like, how many count divided by the total searches?

**Katja Wittfoth:** Is that what you're saying?

**Glenn Lawyer:** That's not going to be a fair comparison because, like I said, we have 15 search phrases.

**Glenn Lawyer:** The first ones are going to be much more popular than the last one.

**Glenn Lawyer:** And if you're number one with the last one, but it's the one that nobody uses, you're not really all that popular.

**Glenn Lawyer:** So there would need to be some kind of a weighting on this.

**Glenn Lawyer:** I don't know how to get a measure on how popular those are.

**Glenn Lawyer:** Again, because it's an AI-based search, so I don't even know if you could get that from Google.

**Glenn Lawyer:** I don't have a super deep background on what sort of analytics are available from Google.

**Glenn Lawyer:** Although, no, actually, you should have a lot.

**Glenn Lawyer:** If you've got, you should know what searches are suffering, hitting your keywords from Google Analytics.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah, I'm guessing.

**Glenn Lawyer:** I don't know, but yeah, so you should have some idea from that.

**Glenn Lawyer:** And actually, would say, that's what I would use.

**Glenn Lawyer:** The reason I'd use that is because people are lazy.

**Glenn Lawyer:** The way they've been searching on Google, that's how they're going to search in OpenAI.

**Glenn Lawyer:** It's going to be very similar.

**Katja Wittfoth:** You think that people search similar, same as we use Google?

**Glenn Lawyer:** That's a lot of what I see.

**Glenn Lawyer:** I would want to verify that hypothesis.

**Glenn Lawyer:** But do people open...

**Katja Wittfoth:** Let's talk about this.

**Glenn Lawyer:** I love that.

**Glenn Lawyer:** How would we verify?

**Katja Wittfoth:** So, you're saying something like "pizza near me". This is how I would search.

**Glenn Lawyer:** I want to buy a car.

**Glenn Lawyer:** What brand of car is the best?

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** Then it's a question, right?

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** But usually in Google, we would do the keywords, right?

**Katja Wittfoth:** Mm-hmm.

**Katja Wittfoth:** Do you think that people's behavior is still the same using LLMs?

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** So I'm going to lay out a couple of hypotheses or axioms as to why I think this.

**Glenn Lawyer:** Human nature does tend to be fairly stable.

**Glenn Lawyer:** The other way of saying that is people are generally lazy.

**Glenn Lawyer:** If you look at what happened with Google, originally they were, in a very technical sense, a search engine.

**Glenn Lawyer:** And you'd put in specific words, it would find the specific websites that actually could answer.

**Katja Wittfoth:** That had those words more often than others, PageRank, for example.

**Glenn Lawyer:** Google realized that people were actually wanted to answer questions, that yes, some people were looking for a specific web page, but a lot of users were actually just wanted to get an answer to a question, and people were typing questions into the address bar.

**Glenn Lawyer:** So then Google changed their core algorithm, and they're now expecting people to type questions into the search bar and get an answer back.

**Glenn Lawyer:** Google was doing that before AI hit the scene.

**Glenn Lawyer:** I can't put a date on it, but let's say 2017, 2018, maybe something like that.

**Glenn Lawyer:** So if Google realized that the mass population comes to these oracles and says, tell me what car should I buy, that's probably what people are doing.

**Glenn Lawyer:** And I don't think people are going to massively change that way using AI.

**Glenn Lawyer:** If they're looking to AI to answer their questions, they're probably going to ask AI a question.

**Glenn Lawyer:** It's kind of what people do.

**Glenn Lawyer:** There is going to be a difference.

**Glenn Lawyer:** There might be a long chat.

**Glenn Lawyer:** Hey, OpenAI.

**Glenn Lawyer:** Hey, Claude, tell me what kind of car I should buy.

**Glenn Lawyer:** Well, what's important to you in a car?

**Glenn Lawyer:** Well, gee, I really care about mileage and I've got, you my family I've got to take care of.

**Glenn Lawyer:** Okay, well, based on that, you know, so that's going be a different search.

**Glenn Lawyer:** And Google, they might go in and say, what's a car with high mileage or something.

**Glenn Lawyer:** So there are differences.

**Glenn Lawyer:** But I still think that there's, looking at human nature and human laziness being what it is, that there basically is, at least, AI will change things, but not in the first couple of years.

**Katja Wittfoth:** So what I'm doing today might not work five years from now, but people don't change that quickly.

**Katja Wittfoth:** Let's think how we can verify this.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** That's where it gets hard because I don't know how to get the data out of OpenAI.

**Katja Wittfoth:** I mean, if I could look at OpenAI's chat logs, that would be great.

**Katja Wittfoth:** Yeah, and we don't have this data, so.

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** You know, even if I worked at Google, I'm not sure I could get that because I might have to work at the right department to get.

**Glenn Lawyer:** access to it.

**Glenn Lawyer:** So I hope that's how it is at Google.

**Glenn Lawyer:** I hope they have some privacy controls.

**Glenn Lawyer:** So from the outside, how do we do this?

**Glenn Lawyer:** I would focus on the models that are optimizing for engagement, which is OpenAI, Gemini.

**Glenn Lawyer:** It's less so Claude.

**Glenn Lawyer:** I really don't know what happens with Grok.

**Glenn Lawyer:** I'm not on Twitter, and I don't know how popular Grok is.

**Glenn Lawyer:** off of Twitter, so I can't say anything on that.

**Katja Wittfoth:** Yeah, just focus on one.

**Glenn Lawyer:** Yeah, we'll just focus on one.

**Glenn Lawyer:** doesn't matter.

**Glenn Lawyer:** If Grok does focus on engagement, it's on the list.

**Glenn Lawyer:** If it doesn't, it's off.

**Glenn Lawyer:** So we have one that's focused on engagement.

**Glenn Lawyer:** We could test different types of prompts and see what response we get back.

**Glenn Lawyer:** The idea isn't totally clear for me, but if they've used reinforcement learning to optimize it for a certain kind of...

**Glenn Lawyer:** If you're a certain kind of behavior from people, that behavior is going to lead to a more stable response than a different behavior.

**Glenn Lawyer:** If you can get some of the top-level model weights out, you might be able to get the entropy over the top K words, for example.

**Glenn Lawyer:** Or if not, you can just run the prompts multiple times and see if you get the similar responses back each time.

**Glenn Lawyer:** So there would be a way to measure the entropy.

**Katja Wittfoth:** But that doesn't really give us the...

**Katja Wittfoth:** It might be.

**Glenn Lawyer:** are you coming to?

**Glenn Lawyer:** Yeah, I'm setting up for it.

**Glenn Lawyer:** So that's our output measure.

**Glenn Lawyer:** And we can run what I think humans do, which is, hey, who makes the best car?

**Glenn Lawyer:** Or what's the best pizza maker near me?

**Glenn Lawyer:** Or whatever the question is.

**Glenn Lawyer:** I'll just phrase it as a question how I think people will ask it.

**Glenn Lawyer:** What sort of response does that get back?

**Glenn Lawyer:** Does the model seem to optimize?

**Glenn Lawyer:** If it does, then the answer should be fairly consistent because I'm within the reinforcement learning.

**Glenn Lawyer:** And then I'd have to try different ways of phrasing that sentiment that they're off my hypothesis.

**Glenn Lawyer:** If, in which case, again, assume my hypothesis is right, then they have reinforcement learning train the model to respond very specifically to these kind of responses.

**Glenn Lawyer:** So then we'd get a common response to a common question.

**Glenn Lawyer:** And an off one is outside the reinforcement learning, so you'd get much more variability in responses.

**Glenn Lawyer:** That's my core hypothesis.

**Glenn Lawyer:** That would be the best idea I have.

**Katja Wittfoth:** So to summarize what you're suggesting is we would run a human-like questions, and we would see probably similar responses versus if it's over and over again.

**Katja Wittfoth:** And if we run a Google-type keyword question, we'll have more variability in response.

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** The high-level intuition is I'm trying to reverse engineer the reinforcement learning they've put on it under the assumption that they are going to use reinforcement learning to tune it towards what most people do.

**Glenn Lawyer:** So that's the intuition.

**Glenn Lawyer:** And I gave you my first question, first pass of how we'd actually measure that, which on the first pass it seems reasonable, might not on the second pass.

**Katja Wittfoth:** Okay.

**Katja Wittfoth:** What are your thoughts on focus group study?

**Katja Wittfoth:** Recruit 100 people, make them ask the way they would ask?

**Katja Wittfoth:** Would that work?

**Glenn Lawyer:** Where my mind is actually going to this is I read some interesting pages.

**Glenn Lawyer:** Papers on digital twin studies, where companies claim, and I also have a scientific paper showing that there's some evidence that this actually works, that they have, these companies claim they've actually trained LLMs based on distinct individual personalities, and by fine-tuning on distinct individual personalities, the LLMs do respond this way, so you can actually do, use LLMs to simulate focus groups.

**Glenn Lawyer:** So, yeah, focus group might be a way of doing that, and that does have a lot of advantages.

**Glenn Lawyer:** I don't believe the LLMs are that good at mimicking, but I'm seeing scientific research that they might be good enough that we could do this much cheaper and do it at scale using a digital twin service.

**Katja Wittfoth:** Yeah, maybe.

**Glenn Lawyer:** So, yeah, you've got a good idea, and there's a couple ways we could implement it.

**Katja Wittfoth:** Well, going back to our original question, I have probably two.

**Katja Wittfoth:** Your questions to you about the brain visibility.

**Katja Wittfoth:** So we define those questions and phrases we want to ask.

**Katja Wittfoth:** How would you go about defining, so if we don't work for one specific pizza shop, how would we define what should be in the list?

**Katja Wittfoth:** What should AI give us as a response?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** The startup scrappy answer for that is, what are you seeing that's coming from your Google keywords?

**Glenn Lawyer:** You know, what search for people using Google keywords?

**Glenn Lawyer:** So I would just take that straight over, or take the top 10 most popular by Google keywords.

**Glenn Lawyer:** And also, if I have it from Google keywords, I can wait.

**Glenn Lawyer:** I've got the top 10, and that allows me to wait, and which allows me to wait the score for the response.

**Glenn Lawyer:** So, again, that works, but it's not going to work five years from now.

**Glenn Lawyer:** So that's our problem.

**Glenn Lawyer:** And how do we then solve that little bugbear, knowing which phrases are actually the ones to use when we actually don't have access to it?

**Glenn Lawyer:** But this is one of those puzzles that actually I've got a lot of backburner questions about LLMs, like how is this actually going to work going forward?

**Glenn Lawyer:** Also, and one of the questions I had for the growth AI team, which they had a good answer to, but, you know, as soon as people start paying for being mentioned, which is, I mean, Sam Altman has already announced the plans for this, and it's been in the works for a while.

**Glenn Lawyer:** Then they're showing up, you know, the top three words that show up or the top brands that show up are because somebody bought it, not because of anything you've done to optimize that.

**Glenn Lawyer:** So how can you even control or test that?

**Glenn Lawyer:** So there are those concerns that come up as well.

**Glenn Lawyer:** Their answer, of course, was, well, part of what we do is help with the LLM optimization, but the other part is it's just a channel.

**Glenn Lawyer:** So let's say the LLM does recommend you to the website, you still need to provide what they were looking for, and that's actually their real value proposition.

**Glenn Lawyer:** To get back to your question, how do we keep the search phrases up to date when we don't have context in what they are and we don't have insight?

**Glenn Lawyer:** If you get observability, that's really hard to answer.

**Glenn Lawyer:** It might have to be focus groups.

**Glenn Lawyer:** You might have to hope that enough people are still using Google search, that there's meaningful signal there, and hope that Google search still exists.

**Glenn Lawyer:** You could mine other data sets, let's say.

**Glenn Lawyer:** For example, you can search for every time your pizza shop is mentioned on Facebook, or Twitter, or whatever public channel you can get information from, and look for the phrases people are using around that.

**Glenn Lawyer:** That's going to get you another couple years into this, after the Google keyword starts to fade off.

**Glenn Lawyer:** And you could actually start that right away, so I could start to measure the correlations now, when the Google is still good data, and I hope that that carries forward.

**Glenn Lawyer:** But no, I don't know how to do that five years from now.

**Katja Wittfoth:** Well, I'll probably learn more in five years.

**Glenn Lawyer:** Yeah, I mean, I want to tell you, oh, the digital twins will solve all of it, because it's been proven, and that's the best answer I've got.

**Katja Wittfoth:** it's a lot of faith, you know.

**Katja Wittfoth:** My last question to you, and that's also very open-ended.

**Katja Wittfoth:** So, let's say we work with a client.

**Katja Wittfoth:** And...

**Katja Wittfoth:** And we want to measure that the actions we made for them, right?

**Katja Wittfoth:** We maybe generated new content for them, that those actions were actually successful in terms of their LLM visibility.

**Katja Wittfoth:** How would you go about measuring that?

**Katja Wittfoth:** In any way is interesting, right?

**Glenn Lawyer:** It's like either evaluating, is there experimentation we can do, what actually works?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Okay, so again, I'm going on guesswork here because I haven't actually tested this.

**Glenn Lawyer:** I know that with search engine optimization, there were things you could actually test, and Google would update its index frequently enough that you might get feedback fairly quickly.

**Glenn Lawyer:** I don't know how often OpenAI updates their model such that if you had made this change, that suddenly there were a lot more documents.

**Glenn Lawyer:** And that coming up first is also less clear than it is on Google search.

**Glenn Lawyer:** So it is a very hard problem.

**Glenn Lawyer:** I know our clients aren't going to like that answer.

**Katja Wittfoth:** We need to promise them something else.

**Katja Wittfoth:** So there's two different things, right?

**Katja Wittfoth:** When they update the model, then it will be whatever they scrape as part of the model.

**Katja Wittfoth:** But in LLM search, this is something that triggers the actual search inside LLM.

**Katja Wittfoth:** That's what we are talking about, right?

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** But let's say we have one of our client companies and they've got a current web page and we can accurately measure how well they do an AI search that actually have your key phrases, your competitors get mentioned before you and seven out of 10 of these.

**Glenn Lawyer:** Oh, that's no good.

**Glenn Lawyer:** We've got to do something.

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** You need to pump out a lot more content that hits these areas in these things.

**Glenn Lawyer:** And because when you look at your content.

**Glenn Lawyer:** It's actually outdated and incoherent.

**Glenn Lawyer:** They say, okay, and they pump out all that new content.

**Glenn Lawyer:** I don't know the delay between when they pump out that content, when AI scrapes that content, which I assume is pretty quickly, within hours, and when AI then uses that newly scrapped content to update their model weight so it's going to show up in their model.

**Glenn Lawyer:** Do they deploy weekly, monthly, daily updates on this?

**Glenn Lawyer:** So I don't know the time delay from when the company makes the changes to when it would show up in OpenAI.

**Katja Wittfoth:** What do we see is likely one to two days.

**Glenn Lawyer:** One to two days, it is that fast?

**Glenn Lawyer:** Okay, yeah, good.

**Katja Wittfoth:** Not the model retrain, but like the search that triggers.

**Katja Wittfoth:** That basically an AI bot scrapes the websites.

**Glenn Lawyer:** One to two days?

**Katja Wittfoth:** Okay.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** We have to be really transparent.

**Glenn Lawyer:** With customers that this is an effort that it's a long-term investment.

**Glenn Lawyer:** So we're looking at a week, months, years, not hours, minutes, days.

**Glenn Lawyer:** So that's painful.

**Glenn Lawyer:** The nice thing about a long-term investment is the payoff is also long-term.

**Glenn Lawyer:** So once you're at the top, you're going to stay there longer.

**Katja Wittfoth:** So would you go about measurement as per metrics or any way of anything towards the controlled experiment?

**Glenn Lawyer:** Wait, one more time?

**Katja Wittfoth:** Because you mentioned the word control in there.

**Katja Wittfoth:** So the measurement of those actions that we take for the clients, if they're successful or not, would you go the route of measuring them by metrics or rather designing and the controlled experiment?

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** Metrics.

**Glenn Lawyer:** I don't know how to do a holdout set on this one.

**Glenn Lawyer:** So I don't know how to set up a controlled experiment.

**Glenn Lawyer:** Again, with Google, it's a little easier, I'm hoping, in the sense that I could buy keywords only in a certain geographical area.

**Glenn Lawyer:** So I could segment by geography or Facebook.

**Glenn Lawyer:** It's really easy to segment by multiple factors.

**Glenn Lawyer:** So I can do a controlled experiment with search engine optimization.

**Glenn Lawyer:** I don't know if that's going to work with an LLM because of just how the model is structured.

**Glenn Lawyer:** So I don't think you can do A-B testing in the same way.

**Glenn Lawyer:** I think it would have to be metric improvement.

**Katja Wittfoth:** Makes sense.

**Katja Wittfoth:** And we're at time, but I'm open for a little, a couple of minutes for your question to me.

**Glenn Lawyer:** Sure.

**Katja Wittfoth:** If you have time.

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** I can stay for a minute or two here.

**Glenn Lawyer:** So I guess the big one is I know that you're somewhat external to the company and that gives you an interesting perspective on things.

**Glenn Lawyer:** I'm really impressed with them.

**Glenn Lawyer:** These guys are just scrappy and they've been building for so long and they've actually, they're solving customer problems in direct conversation with the customer so they know what they need and they're building fast, which is what I've seen is the way things work.

**Glenn Lawyer:** And that's how you win.

**Glenn Lawyer:** And even going back to when I was studying evolution at the Max Planck and how things spread and move, that's how life wins as well.

**Glenn Lawyer:** So it's not just the rule for startups.

**Glenn Lawyer:** It's how you work, rapid iteration with feedback from the real world.

**Glenn Lawyer:** That's how it happens.

**Glenn Lawyer:** So that's my impression of the team and the guys.

**Glenn Lawyer:** What's yours?

**Katja Wittfoth:** That's pretty good.

**Katja Wittfoth:** I think same, what I see is, and what I admire the company and what Daniel and Marcel is doing, they bring expertise first, right?

**Katja Wittfoth:** Marcel brings the marketing and growth expertise, and Daniel, his experience from engineering side, and they really apply and think through what the latest technology we can apply to improve our product and improve, actually, growth and marketing strategy for our clients.

**Katja Wittfoth:** And I think this is really inspiring that they are looking for latest innovation to bake into their product.

**Glenn Lawyer:** Very cool.

**Glenn Lawyer:** Anything else, or does that answer your question?

**Glenn Lawyer:** No, that's...

**Glenn Lawyer:** That does help with some insights.

**Glenn Lawyer:** I guess sort of as a follow-up, can you be a little bit more clear on what your role is in the company and more the trajectory of that role?

**Glenn Lawyer:** As in, are you advising, but you're thinking of joining full-time when the time is right?

**Katja Wittfoth:** Or you're advising and planning to stay on the advisory side?

**Katja Wittfoth:** I'm currently helping, so it's temporary, helping with AI data science.

**Katja Wittfoth:** Yes, until we have a team at Growthx, and then I will discontinue.

**Glenn Lawyer:** Okay.

**Katja Wittfoth:** Okay, that's...

**Katja Wittfoth:** No trajectory plan.

**Glenn Lawyer:** Yeah, yeah.

**Glenn Lawyer:** No, and that makes sense.

**Glenn Lawyer:** I mean, you've got a full-time job.

**Glenn Lawyer:** Exactly.

**Glenn Lawyer:** And Mercury is also a really interesting company.

**Glenn Lawyer:** Yeah.

**Glenn Lawyer:** I'm not going to push this any farther than right now, but I think I'd be pretty happy with the job there.

**Glenn Lawyer:** So no, I did not ask you to recommend my name or put me in anything.

**Glenn Lawyer:** I'm done with this for now.

**Glenn Lawyer:** But let me just...

**Glenn Lawyer:** say that it looks like a really interesting and fun place to work.

**Glenn Lawyer:** so I wish you that.

**Glenn Lawyer:** is.

**Glenn Lawyer:** It is.

**Glenn Lawyer:** Yeah.

**Katja Wittfoth:** Well, thank you so much, Glenn.

**Katja Wittfoth:** It was nice to meet you.

**Katja Wittfoth:** And thanks for your time.

**Katja Wittfoth:** And I think Fathom will be in touch.

**Glenn Lawyer:** Okay.

**Glenn Lawyer:** Very good.

**Glenn Lawyer:** Sounds good.

**Glenn Lawyer:** Thank you, Glenn.

**Glenn Lawyer:** Bye-bye.
