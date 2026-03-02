# Clint Irvin - Technical Discussion Interview | Data Scientist

<metadata>
date: 2026-01-15
time: 19:59 UTC
duration: 66 minutes
organizer: katja@growthx.ai
participants: Katja Wittfoth (GrowthX), Clint Irvin (Candidate)
fathom_recording_id: 114688566
fathom_url: https://fathom.video/calls/533349160
share_url: https://fathom.video/share/vJszhmf8zrQsL7BVooeEdBzx6ZyVYTL7
source: fathom
enriched_on: 2026-02-28 15:50 UTC
</metadata>

---

## Summary

Technical interview between Katja Wittfoth (GrowthX) and Clint Irvin, a data scientist and AI engineer with deep expertise in hybrid modeling, LLM automation, and AI-driven content visibility. Clint presented his background spanning government research, fintech, and AI applications, showcased two major technical case studies (bank balance forecasting and RFP automation), and proposed a comprehensive strategy for measuring and optimizing GrowthX's visibility in LLM search results. The discussion focused on his suitability for a foundational data science role starting with building an evaluation pipeline for content generation.

---

## Context

GrowthX is evaluating data science candidates for a core data infrastructure role. The position is foundational and will focus initially on building an evaluation pipeline for the company's content generation process. Katja Wittfoth, who advises GrowthX on data strategy and leads technical hiring for data roles, conducted this technical discussion to assess Clint's technical depth, problem-solving approach, and alignment with GrowthX's strategic priorities around LLM visibility and AEO (AI Engine Optimization).

---

## Relevance

Clint's background is highly relevant to GrowthX's needs. His experience spans statistical modeling (ARIMA, neural networks), LLM applications (multi-agent systems, RAG engines), and full-stack AI engineering—all directly applicable to evaluating and optimizing content for LLM discoverability. His case studies demonstrate ability to translate complex analytical challenges into measurable business impact, which aligns with GrowthX's focus on visibility metrics and content optimization. His proposed framework for measuring LLM visibility (coverage, consistency, robustness) and reverse-engineering LLM prioritization logic directly matches GrowthX's strategic priorities. His pragmatic approach to using LLMs for planning while maintaining rigorous code review suggests a mature perspective on AI tooling.

---

## Overview

- **Hybrid Modeling for Unseen Events:** At Synovus, Clint built a hybrid model (ARIMA + 1D ConvNet) to forecast bank balances, preventing $3–4M in bond-cashing penalties by distinguishing payroll dips from actual bank runs.
- **LLM-Driven Automation:** At MDLynx, Clint built a multi-agent system to automate 90% of RFP responses, freeing specialists for higher-value work.
- **LLM Search Strategy:** Proposed a three-part strategy for GrowthX: 1) Measure visibility with query variations, 2) Reverse-engineer LLM behavior with a custom RAG engine, and 3) Use an LLM to grade content features for ML analysis.
- **Role & Infrastructure:** The role is foundational, starting with an evaluation pipeline. The tech stack is open, though current pipelines use Temporal and Ruby.

---

## Key Topics

### Background & Experience

  - **Education:** PhD in Social Experimental Psychology with a doctoral minor in Statistics.
  - **Career Progression:** Data Scientist → ML Engineer → AI Engineer.
  - **Government (Homeland Security, Los Alamos, Military):**
      - Built systems for marksmanship capture and situational awareness optimization.
      - Automated statistical analyses and research methodologies.
      - ~11 years of government service before transitioning to corporate.
  - **Synovus (Bank):**
      - Built the "ariminator" system to automate DFAST regulatory models (ARIMA).
      - Reduced model refresh time from hours to ~1 hour, enabling a 2-person team to manage hundreds of models annually.
  - **Amazon (Alexa Marketing Science):**
      - Lead Data Scientist focused on personalization and cross-sell.
  - **Stealth Startup (Nomi):**
      - Built a Perplexity-style RAG search engine for real-time news.
      - Developed a sentiment analysis pipeline using fine-tuned XML-RoBERTa for better semantic understanding than dictionary-based methods.
  - **MDLynx (Current):**
      - **RFP Automation:** Multi-agent system automating 90% of RFP responses.
      - **Conference Coverage:** System to summarize medical conference abstracts.
      - **Content Recommendation:** Engine to break out of a "local minima" where content is over-optimized for a single subgroup.

### Case Study: Forecasting Bank Balances

  - **Problem:** Unpredictable payroll cycles caused large, temporary balance dips, leading the treasurer to cash in bonds at a penalty ($3–4M loss).
  - **Goal:** Forecast daily account balances 2 months out to distinguish payroll dips from actual bank runs.
  - **Solution:** A hybrid model inspired by IBM's R2N2 paper.
    1. **Pre-process:** Each account's time series was pre-whitened and differenced (ARIMA).
    2. **Model Residuals:** A 1D Convolutional Neural Network (ConvNet) was trained on the normalized residuals.
    3. **Predict & Reconstruct:** The model predicted 60 steps out; results were then rescaled and re-transformed.
    4. **Prediction Intervals:** Overlapping windows were used to generate prediction intervals, flagging significant deviations.
  - **Business Impact:**
      - **Treasury:** Eliminated the need to cash in bonds at a penalty.
      - **Private Wealth:** Identified high-value accounts with unexpected balance increases (e.g., >$750k) for targeted outreach.

### Case Study: Measuring LLM Search Visibility

  - **Goal:** Measure and optimize brand visibility in LLM search (ChatGPT, Perplexity, Claude, Google).
  - **Proposed Metrics:**
      - **Coverage:** Presence across target LLMs.
      - **Consistency:** Stability of results over time (e.g., 48-hour hourly checks).
      - **Robustness:** Presence across query variations (e.g., 50–100 reformulations).
  - **Proposed ML Approach:**
    1. **Data Collection:** Run queries, log results, and crawl source pages.
    2. **Feature Engineering:** Use an LLM to grade content features (e.g., length, tone, bullet points) against a rubric.
    3. **Modeling:** Use logistic regression to predict visibility based on content features.
    4. **Reverse Engineering:** Build a custom RAG engine to isolate and study the prioritization logic of specific LLMs.

### Role & Infrastructure

  - **First Project:** Build an evaluation pipeline for the content generation process.
  - **Tech Stack:** Open to Python. Current pipelines use Temporal and Ruby.
  - **LLM Coding:** Use LLMs for planning and rapid prototyping, but always review and refine the generated code.

---

## Action Items

- **Katja Wittfoth (GrowthX):** Follow up with Clint Irvin regarding next steps in the hiring process and timeline.

---

## Transcript

**Katja Wittfoth:** This meeting is being recorded.

**Katja Wittfoth:** Hi, Cliff?

**Clint Irvin:** Yeah, hey, how are you doing today?

**Katja Wittfoth:** Hi, good.

**Katja Wittfoth:** How are you?

**Katja Wittfoth:** Sorry for a delay.

**Clint Irvin:** No worries.

**Katja Wittfoth:** How are you doing?

**Katja Wittfoth:** How's your day going?

**Clint Irvin:** Doing pretty well.

**Clint Irvin:** Still that back-to-work-at-the-beginning-of-the-year-bluster kind of thing going on, but otherwise, good.

**Katja Wittfoth:** How about yourself?

**Katja Wittfoth:** Same, same.

**Katja Wittfoth:** It's also a lot going on in the beginning of the year.

**Katja Wittfoth:** It's just like catching up with everyone and on other projects, etc.

**Katja Wittfoth:** So, busy times.

**Katja Wittfoth:** Busy times.

**Katja Wittfoth:** I'm glad you are here.

**Katja Wittfoth:** I'm glad we are having this interview.

**Katja Wittfoth:** Sorry.

**Katja Wittfoth:** So thanks for your time.

**Katja Wittfoth:** To introduce myself, my name is Katja.

**Katja Wittfoth:** I am currently advising GrowthX on data, and Daniel asked me to interview for data roles.

**Katja Wittfoth:** So I'm helping out with that today.

**Katja Wittfoth:** I am a full-stack data scientist.

**Katja Wittfoth:** My career spans over, you know, the health tech and fintech and some AI.

**Katja Wittfoth:** Right now, my full-time position is in fintech.

**Katja Wittfoth:** So very also broad and did a bunch of stuff from, you know, analytics, data engineering to ML and AI.

**Katja Wittfoth:** So really a broad range.

**Katja Wittfoth:** Yeah, I'm happy to interview today.

**Katja Wittfoth:** So my plan was, I'd like to learn more about you if you can.

**Katja Wittfoth:** And share more about your recent work and would love to dive into one of your projects, one of your recent projects.

**Katja Wittfoth:** And then I have a growthx key study I would love to talk through with you today.

**Katja Wittfoth:** And then we'll leave a couple of some minutes for questions.

**Katja Wittfoth:** Does that sound good?

**Clint Irvin:** Okay.

**Clint Irvin:** Yeah, absolutely.

**Clint Irvin:** Just let me know how far back you want me to go and what level of detail.

**Clint Irvin:** And I'll give you whatever level of information you need to see.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Yeah, maybe you just start the high level first and then we'll go from there.

**Clint Irvin:** Okay.

**Clint Irvin:** A high level, I've got a, I'm a data scientist that's moved into almost more machine learning engineering.

**Clint Irvin:** And then in the last year or so, much more of a full stack development kind of role with AI engineering coming front and center extensively in the last probably probably.

**Clint Irvin:** Yeah.

**Clint Irvin:** 18 months working with LLM.

**Clint Irvin:** I started academically back with a PhD in social experimental psychology and a doctoral minor in stats.

**Clint Irvin:** Knew pretty quickly I didn't want to go into the academic route.

**Clint Irvin:** What the focus is of that, and I always say this as a disclaimer, most people hear psychology, they immediately think what kind of medical treatment someone walks in and sits on a couch and you talk to them.

**Clint Irvin:** But in graduate school, it immediately splits.

**Clint Irvin:** And you're either doing science, looking at the influences of information and information processing in the human brain as a scientist, not that dissimilar from a chemist or something like that, or you're doing treatment.

**Clint Irvin:** I was in the science side of it.

**Clint Irvin:** So social psych is essentially the science of how the environment and influences coming from information and other people change behavior and influence behavior and how to figure out if those changes occurred and identify what those effects are.

**Clint Irvin:** Right.

**Clint Irvin:** So that goes pretty heavily into marketing and on the government.

**Clint Irvin:** So I moved from there pretty quickly into government applications.

**Clint Irvin:** It was kind of the height of the war on terror.

**Clint Irvin:** I got picked up at Homeland Security for doctoral fellowship.

**Clint Irvin:** I worked at Los Alamos National Laboratory for about three years, both part-time and full-time on-site.

**Clint Irvin:** A couple of summers of graduate research intern, then I went to active duty military service.

**Clint Irvin:** I started right after I finished my PhD, really interested in doing tough guy stuff.

**Clint Irvin:** So I went from two straight years of training, almost 30, got first.

**Katja Wittfoth:** Sorry to interrupt you.

**Katja Wittfoth:** I hear like some, it's a little bit muffled.

**Katja Wittfoth:** So I'm not sure if it's on my side or on your side.

**Katja Wittfoth:** So it's hard to hear you.

**Clint Irvin:** Yeah.

**Clint Irvin:** Okay.

**Clint Irvin:** Let me try these.

**Clint Irvin:** These are pretty much full proof.

**Clint Irvin:** So I'll just transition really quickly.

**Katja Wittfoth:** My camera is really following me.

**Katja Wittfoth:** I'm suggesting my chair.

**Clint Irvin:** you hear better now?

**Katja Wittfoth:** Yes, much better.

**Katja Wittfoth:** Perfect.

**Katja Wittfoth:** That's perfect.

**Clint Irvin:** Okay.

**Clint Irvin:** Okay.

**Clint Irvin:** So after I moved out of government research and operational research, I immediately went into active duty military service.

**Clint Irvin:** I moved in to do what I jokingly call tough guy stuff.

**Clint Irvin:** So I was going through all the combat schools, moving into airborne ranger school, stuff like that.

**Clint Irvin:** And got hurt pretty quickly because I was almost 30.

**Clint Irvin:** And they said, back to the nerd stuff.

**Clint Irvin:** So I ended up at Aero Medical Research Laboratory.

**Clint Irvin:** So after about two years of training, then I went into two years of medical board and physical recovery.

**Clint Irvin:** It's easy to get pretty big injuries in that stuff.

**Clint Irvin:** And then started working with medical research publications.

**Clint Irvin:** And I kind of picked up there.

**Clint Irvin:** One of my favorite things had been putting together systems.

**Clint Irvin:** And my coding wasn't very good when I was in graduate school.

**Clint Irvin:** At Los Alamos National Lab, I actually got put on coding teams first exposed to it.

**Clint Irvin:** And then when I went back...

**Clint Irvin:** I realized that the statistical analyses, research methodology designs, and building tools to support those and automate those were kind of my favorite thing and where I excelled above peers.

**Clint Irvin:** After I got out, I went to do operational research and build additional systems for marksmanship capture and situational awareness optimization and looking at organizational impact across everything from like airborne schools to marksmanship schools to different training programs for all of the tough guy schools that I had just attended.

**Clint Irvin:** And then around there, hit the 10 or 11 year mark in government service and decided I wanted to migrate into corporate.

**Katja Wittfoth:** Great.

**Katja Wittfoth:** So thank you for sharing your background.

**Katja Wittfoth:** So you've mentioned, you've done, you've done government, military, and now you're moving into corporate.

**Katja Wittfoth:** Maybe let's talk a bit more about your more recent roles or projects.

**Katja Wittfoth:** What was the first company you went to?

**Clint Irvin:** So the first company I went to was Synovus, which is a bank.

**Clint Irvin:** It was a fantastic entry point because it was the right skill sets and the complexity of the domain and the rigor that's needed and the value that can be created was really high.

**Clint Irvin:** I think the thing I leaned into at Synovus was the fact that regulators require very specific models for forecasting and understanding the future risk.

**Clint Irvin:** So we had this regulatory regime called DFAST, which is the Dodd-Frank Act Stress Test.

**Clint Irvin:** And it requires banks to forecast their income statement and balance sheet for various scenarios over 9 quarters.

**Clint Irvin:** So, the complexity there is you need to build and validate hundreds of thousands of models.

**Clint Irvin:** And they need to be refreshed fairly regularly, probably quarterly, sometimes more frequently.

**Clint Irvin:** So the challenge was really in the time complexity.

**Clint Irvin:** And what we did was build the "ariminator" system.

**Clint Irvin:** So what "ariminator" does is, it's using the ARIMA framework, which is a classic time-series model, autoregressive integrated moving average.

**Clint Irvin:** But what we did was basically optimize it for Synovus's particular use case.

**Clint Irvin:** So this process used to take hours.

**Clint Irvin:** And we cut it down to about 1 hour.

**Clint Irvin:** So basically, we went from a job that would require a couple of people to babysit through the whole modeling process to a more hands-off process.

**Clint Irvin:** So we basically freed up about 2 people who could then manage hundreds of models and oversee the model validation and that kind of thing.

**Clint Irvin:** So there's huge operational efficiency gains there.

**Clint Irvin:** And then what was also interesting was the banks are concerned with the future cash flow forecasting for different financial products and services.

**Clint Irvin:** And so, treasury and other parts of the business were very interested in how to improve that forecast.

**Clint Irvin:** So, that led to a second project at Synovus where we built a hybrid model to forecast account balances.

**Clint Irvin:** And the key issue there was that the traditional time series models, if you're trying to forecast a bank account balance, you will run into a really common problem, which is the existence of payroll deposits and other recurring events that create large swings in the balance.

**Clint Irvin:** So the payroll deposits come in for about 2 or 3 days, then they seem to distribute over the next few weeks.

**Clint Irvin:** And the treasury function is trying to figure out, is this a real bank run, or is it just payroll?

**Clint Irvin:** So if they get it wrong, they have to cash in bonds as a penalty of like 3 to $4 million.

**Clint Irvin:** So the stakes are pretty high.

**Clint Irvin:** And so the approach we took was a hybrid model.

**Clint Irvin:** The idea was inspired by this paper from IBM, the R2N2 paper.

**Clint Irvin:** So the idea is, we first pre-process the time series using ARIMA.

**Clint Irvin:** So essentially, you difference the series, you remove the trend, and you're left with a whiten(ed) time series.

**Clint Irvin:** And then what you do is, you train a 1D convolutional neural network on the residuals, on the white(ened) time series.

**Clint Irvin:** And then you can make predictions and then reconstruct them back to the original scale.

**Clint Irvin:** And you can use overlapping windows to generate prediction intervals.

**Clint Irvin:** So you can flag when there's a really significant deviation from the norm.

**Clint Irvin:** And so, the approach worked really well.

**Clint Irvin:** And you could identify, whether it was a real bank run or payroll effects.

**Clint Irvin:** And so the business impact was, we eliminated the need for the treasury function to cash in bonds.

**Clint Irvin:** And then, as a side benefit, we were able to identify accounts that had really unusual balance increases and could flag those to the private wealth management team.

**Clint Irvin:** So we're talking about accounts with balances that increased by over $750k unexpectedly.

**Clint Irvin:** And so we were able to flag those to the private wealth management team.

**Clint Irvin:** And so that's an example of machine learning creating direct business value.

**Clint Irvin:** And that's what I love about fintech is you can see the direct measurable impact of your work.

**Katja Wittfoth:** Yeah, that's great.

**Katja Wittfoth:** And so I appreciate that hybrid approach.

**Katja Wittfoth:** So after Synovus, what did you do next?

**Clint Irvin:** So after Synovus, I went to Amazon.

**Clint Irvin:** I was a lead data scientist in the Alexa Marketing Science team.

**Clint Irvin:** So there, my focus was on personalization and cross-sell opportunities.

**Clint Irvin:** And we were building models to understand customer behavior and predict purchase propensities.

**Clint Irvin:** I learned a lot about scale, working with very large datasets and the engineering challenges that come with that.

**Clint Irvin:** But honestly, I was ready to get back into a more startup-like environment.

**Clint Irvin:** So I joined a stealth startup called Nomi.

**Clint Irvin:** And at Nomi, we were building a Perplexity-style RAG search engine for real-time news.

**Clint Irvin:** So the idea was, you could search for news about a topic, and the system would pull relevant articles, summarize them, and create a synthesized response.

**Clint Irvin:** And we also built a sentiment analysis pipeline using fine-tuned XML-RoBERTa for better semantic understanding than dictionary-based approaches.

**Clint Irvin:** But the startup pivoted and eventually wound down.

**Clint Irvin:** So, I'm currently at MDLynx, which is a medical information company.

**Clint Irvin:** And there, I've been building some really interesting projects.

**Clint Irvin:** So one of them is an RFP response automation system.

**Clint Irvin:** We built a multi-agent system that can automate about 90% of RFP responses.

**Clint Irvin:** So the way it works is, we have different agents specialized in different aspects of the RFP—compliance, pricing, technical fit, and so on.

**Clint Irvin:** And they coordinate to produce a comprehensive response.

**Clint Irvin:** So that frees up our RFP specialists to focus on the really high-value, custom requests.

**Clint Irvin:** We've also built a system to summarize medical conference abstracts, which is useful for staying on top of the latest research in our domain.

**Clint Irvin:** And we have a content recommendation engine that helps break out of local minima where content becomes over-optimized for a single subgroup.

**Clint Irvin:** So essentially, the system recommends new content directions based on what gaps exist in the current content library.

**Clint Irvin:** So that's where I'm at now, and I'm looking forward to exploring the GrowthX opportunity.

**Katja Wittfoth:** Great.

**Katja Wittfoth:** So, I really appreciate you walking through your career.

**Katja Wittfoth:** It sounds like you have a lot of depth, especially with the recent LLM work.

**Katja Wittfoth:** And one thing I think is really interesting and relevant for us is the approach you took at Synovus with that hybrid model.

**Katja Wittfoth:** The way you combined classical statistical approaches with deep learning is something that we think is really valuable.

**Katja Wittfoth:** So, what I'd like to do is, talk through a GrowthX case study with you.

**Katja Wittfoth:** We are heavily invested in understanding how brand visibility works across different LLM search engines.

**Katja Wittfoth:** And we want to build a system to measure and optimize that visibility.

**Katja Wittfoth:** So, how would you approach that problem?

**Clint Irvin:** That's a great question.

**Clint Irvin:** I think the first thing I'd want to do is define what we mean by visibility.

**Clint Irvin:** Because visibility can mean a lot of different things depending on the context.

**Clint Irvin:** For LLM search, I'd probably define three key metrics: coverage, consistency, and robustness.

**Clint Irvin:** Coverage is, are we present across the target LLMs?

**Clint Irvin:** Consistency is, do those results remain stable over time?

**Clint Irvin:** So, like, if we check the same query 48 hours later, every hour, do we still show up?

**Clint Irvin:** And robustness is, does our presence hold up when the query is rephrased?

**Clint Irvin:** Like, if someone searches for "GrowthX" versus "Growth X" or "content marketing for B2B", do we show up consistently?

**Clint Irvin:** So my approach would be to:

**Clint Irvin:** First, run a bunch of queries across the target LLMs and log all the results.

**Clint Irvin:** And then crawl all those source pages to extract their content features.

**Clint Irvin:** Second, I'd use an LLM to grade those content features against a rubric.

**Clint Irvin:** Like, is the content length optimal? Is the tone right? Are there good visual elements like bullet points or images?

**Clint Irvin:** Third, I'd build a logistic regression model to predict visibility based on those features.

**Clint Irvin:** And finally, I'd want to reverse-engineer the LLM's prioritization logic.

**Clint Irvin:** So I'd build a custom RAG engine that allows us to test hypotheses about what signals the LLMs are using to rank content.

**Clint Irvin:** Are they favoring recency? Authority? Comprehensiveness? Engagement metrics?

**Clint Irvin:** And then, based on those insights, we'd optimize our content.

**Katja Wittfoth:** That's a really thoughtful approach.

**Katja Wittfoth:** I think the key insight there is that you're thinking about this as a multi-layered problem.

**Katja Wittfoth:** We have the measurement layer, the feature engineering layer, the modeling layer, and the reverse engineering layer.

**Katja Wittfoth:** And that feels like a solid foundation for what we want to build.

**Katja Wittfoth:** So, the next question is, if you were to start in this role, what would be your first priority?

**Clint Irvin:** I think the first priority would be to build an evaluation pipeline.

**Clint Irvin:** Because before we can optimize anything, we need to understand what we're optimizing for.

**Clint Irvin:** We need to be able to run experiments, change a piece of content, and measure the impact on visibility.

**Clint Irvin:** So the evaluation pipeline would be the foundation for everything else.

**Clint Irvin:** It would include infrastructure for:

**Clint Irvin:** - Querying the target LLMs (ChatGPT, Perplexity, Claude, Google)
**Clint Irvin:** - Logging all results with timestamps
**Clint Irvin:** - Crawling source pages
**Clint Irvin:** - Running automated tests to detect changes in visibility
**Clint Irvin:** - Versioning the content so we can track which changes had what impact

**Clint Irvin:** And I'd want to build this in a way that's language-agnostic and can grow with the company.

**Clint Irvin:** Python is a natural choice for this kind of work.

**Clint Irvin:** But I'm open to whatever tech stack makes sense.

**Clint Irvin:** I know GrowthX currently uses Temporal and Ruby in some pipelines, so I'd want to understand how those fit into the broader architecture.

**Katja Wittfoth:** That's really thoughtful.

**Katja Wittfoth:** And yes, we do have Temporal and Ruby pipelines.

**Katja Wittfoth:** So understanding how to integrate with those would be important.

**Katja Wittfoth:** One more question for you.

**Katja Wittfoth:** You have experience at big tech, at startups, and in government.

**Katja Wittfoth:** How do you think about the trade-offs between moving fast and moving carefully in AI/ML work?

**Clint Irvin:** That's a really good question.

**Clint Irvin:** I think the key is to use LLMs for what they're good at—planning and rapid prototyping.

**Clint Irvin:** But always validate and refine the output.

**Clint Irvin:** Don't just take generated code and ship it.

**Clint Irvin:** Review it, understand it, improve it.

**Clint Irvin:** In government work, we had to move carefully because the stakes were high and the constraints were tight.

**Clint Irvin:** In startups, you have to move fast because the window is narrow.

**Clint Irvin:** The trick is finding the balance.

**Clint Irvin:** I think in the context of GrowthX, you're in a position where you can afford to be both fast and careful.

**Clint Irvin:** Fast in prototyping and experimentation, but careful in the evaluation and measurement of results.

**Clint Irvin:** So I'd emphasize building robust measurement infrastructure first, and then using that to safely iterate.

**Katja Wittfoth:** That's a really good point.

**Katja Wittfoth:** I think we're aligned on that.

**Katja Wittfoth:** So, I think that's all the questions I have for now.

**Katja Wittfoth:** Do you have any questions for me or for GrowthX?

**Clint Irvin:** Yeah, a couple.

**Clint Irvin:** First, what's the timeline for this role?

**Clint Irvin:** And what would the first 90 days look like?

**Katja Wittfoth:** Great question.

**Katja Wittfoth:** So, we're looking to fill this role within the next month or so.

**Katja Wittfoth:** And the first 90 days would focus on understanding the current content generation pipeline, identifying gaps, and scoping out the evaluation pipeline.

**Katja Wittfoth:** By the end of 90 days, we'd want to have a working prototype of the evaluation system.

**Clint Irvin:** That sounds reasonable.

**Clint Irvin:** And what about the team structure?

**Clint Irvin:** Who would I be working with?

**Katja Wittfoth:** So, you'd be working closely with our content and product teams.

**Katja Wittfoth:** And there's already some technical infrastructure in place with the Temporal and Ruby pipelines.

**Katja Wittfoth:** So you'd have some support there.

**Katja Wittfoth:** But the evaluation pipeline would be a new, foundational piece.

**Clint Irvin:** Got it.

**Clint Irvin:** I think this is a really compelling opportunity.

**Clint Irvin:** The work feels meaningful, the problem is well-defined, and I think I can make a real impact here.

**Katja Wittfoth:** Great.

**Katja Wittfoth:** Well, thank you so much for your time and for the thoughtful conversation.

**Katja Wittfoth:** We'll follow up with next steps soon.

**Clint Irvin:** Thanks, Katja.

**Clint Irvin:** I really appreciated the opportunity to discuss this with you.

**Clint Irvin:** Looking forward to hearing from you.

**Katja Wittfoth:** Take care.
