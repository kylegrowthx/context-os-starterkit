# Mohitdeep Singh - Interview | AI Engineer (Applied AI Scientist)

<metadata>
date: 2025-12-10
time: 17:58 UTC
duration: 69 minutes
organizer: katja@growthx.ai
participants: Katja Wittfoth, Mohitdeep Singh
fathom_recording_id: 107777122
fathom_url: https://fathom.video/calls/502069860
share_url: https://fathom.video/share/eKCGLi3Zm8YpS6M7mZcEjfhaBfMud84s
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Katja Wittfoth interviewed Mohitdeep Singh for GrowthX's AI Engineer (Applied AI Scientist) role. Mohit demonstrated 8+ years of deep expertise in analytics, signal processing, and recommendation systems (Radio, Pandora, Pinterest, Roku), followed by recent GenAI work at Coupang on RAG-based product recommendation (19% engagement lift) and LLM agents for fraud detection. In response to a GrowthX case study, Mohit proposed a novel multi-agent content quality system that would score GrowthX's long-form content across 5 pillars (factuality, structure, SEO, style, engagement) and use reinforcement learning with editor feedback to systematically improve content. Katja will connect him with Taka for next steps, likely involving team meetings and a take-home assignment.

---

## Context

GrowthX is actively hiring for a new AI Engineer role to advance its content quality and delivery capabilities. Katja Wittfoth, working in an advisory capacity as a data scientist, is leading the hiring process. Mohitdeep Singh is a candidate being evaluated for this role. The interview follows a structured but flexible format, with Katja conducting initial technical deep-dives before loop interviews with the broader GrowthX team. Mohit had prior exposure to GrowthX's product and team through a conversation with Daniel (likely a co-founder or leadership team member), so he came into the interview with some familiarity of the company's AI-driven approach and tooling.

---

## Relevance

### To GrowthX Hiring & Team Development
- **Strong technical fit:** Mohit's background in production recommendation systems (Pinterest cold-start, Roku targeting) and GenAI projects (Coupang RAG, LLM agents for fraud) directly maps to GrowthX's needs for content quality and AI-driven delivery.
- **State-of-the-art mindset:** Explicitly seeks remote-first, innovation-friendly environments; values experimenting with cutting-edge techniques—aligns with GrowthX culture as described by Katja.
- **Next steps:** Taka will contact within days (likely within 24-48 hours based on Katja's comment); process includes team meetings and a take-home assignment.

### To CheckThat & Content Quality Systems
- **Direct proposal relevance:** Mohit proposed an RL-based content quality system that could operationalize CheckThat's strengths—multi-agent scoring on factuality, SEO, style, engagement.
- **Reinforcement learning approach:** GrowthX is not currently using RL but sees it as the next step; Mohit's expertise in RL feedback loops (editor signals) could accelerate that roadmap.
- **Implementation ready:** Proposed framework includes concrete metrics (TER score, Flesch-Kincaid, embedding similarity, XGBoost classifiers) that CheckThat could validate or integrate.

### To GrowthX Business Development
- **Cultural signal:** Candidate explicitly praised GrowthX's UI, remote-first culture, strong writing discipline, and openness to innovation. This suggests strong cultural fit and low onboarding friction.
- **Candidate enthusiasm:** Described GrowthX work as "very exciting" and asked thoughtful questions about RL, team structure, and company direction—indicators of genuine interest and low flight risk.

---

## Overview

- **Deep Experience:** 8+ years in analytics, with a strong background in signal processing (audio classification at Radio/Pandora) and recommendation systems (Pinterest/Roku).
- **Recent GenAI Focus:** At Coupang, led a RAG-based product recommender (19% engagement lift) and used LLM agents for fraud detection feature engineering.
- **Proposed Quality System:** For GrowthX, outlined a multi-agent system to score content on 5 pillars (factuality, structure, SEO, style, engagement) and improve it with RL.
- **Cultural Fit:** Seeks an innovative, remote-first environment open to state-of-the-art approaches, aligning with GrowthX's described culture.

---

## Key Topics

### Professional Background

  - **Intel (Research Intern):** Researched CNN pipelines for Intel chips using legacy code.
  - **Radio (Data Scientist):** Built a collaborative filtering algorithm for real-time audio personalization.
      - **Method:** Classified music genres from audio signals using spectrograms.
  - **Pandora (Data Scientist):** Evolved the audio classification system.
      - **Method:** Used CNNs on spectrograms and textual analysis on lyrics for a dual-channel recommendation system.
  - **Pinterest (Data Scientist):** Improved the home feed ranking system.
      - **Challenge:** Solved cold-start problems for new users.
      - **Method:** Integrated CNN-transformer models with visual embeddings and used approximate nearest neighbor search for retrieval.
  - **Roku (Data Scientist):** Built audience segmentation and propensity models for ad targeting.
      - **Method:** Used XGBoost and Logistic Regression for daily batch predictions.
      - **Rationale:** The Logistic Regression model provided a probability score, while its regression slope helped the ad team understand the revenue trade-off for different probability thresholds.

### Recent GenAI & LLM Projects

  - **Coupang (AI Engineer):** Led the design of a distributed data engine and feature store (Delta Lake) to solve data infrastructure challenges.
  - **Product Recommender (Coupang):**
      - **Problem:** Slow, generic recommendations with cold-start issues.
      - **Solution:** A two-stage RAG system:
        1.  **Candidate Generation:** Semantic retrieval from a vector DB (using Firecrawl/Bing Search) for product summaries.
        2.  **Ranking:** A GRU model on clickstream data to sequence and rank candidates.
      - **Refinement:** Fine-tuned a distilled model (5.4B params, 8 LoRA layers) on 100M records to improve recommendation quality.
      - **Outcome:** 19% lift in new product engagement; 11-month project with a 3-person team.
  - **Fraud Detection (Coupang):**
      - **Problem:** Detect behavioral anomalies in transaction data in seconds.
      - **LLM Role:** Used LLM agents for feature engineering and flagging anomalies, rather than direct detection.
      - **Rationale:** Agents analyze patterns (e.g., tone mismatches, "hallucination facts") in system-generated text to identify fraudulent structures.

### GrowthX Case Study: Content Quality System

  - **Goal:** Design a system to score and improve GrowthX's long-form content.
  - **Proposed Framework:** A multi-agent system scoring content on 5 pillars:
    1.  **Factuality & Accuracy:**
          - **Method:** Extract entities (numbers, nouns) from the prompt and generated text.
          - **Metric:** Compare entity counts; use TER score to measure edit distance.
    2.  **Structure & Coherence:**
          - **Method:** Evaluate logical flow between entities.
          - **Metric:** Use Flesch-Kincaid score to measure readability.
    3.  **SEO & Keyword Coverage:**
          - **Method:** Check for primary/secondary keyword presence and density.
    4.  **Brand Voice & Style:**
          - **Method:** Use embedding similarity against brand examples.
          - **Refinement:** Fine-tune a small model (2.5B-3.5B params) with LoRA for paraphrasing to align with the brand's vocabulary.
    5.  **Engagement Propensity:**
          - **Method:** Train a classifier (e.g., XGBoost) on historical data (traffic, time-on-page) to predict future performance.
  - **System Improvement with Reinforcement Learning (RL):**
      - **Environment:** The content quality scores.
      - **Actions:** Rewrite, simplify, research, add citations.
      - **Rewards:** Increased readability, higher keyword scores, decreased hallucination count.
      - **Feedback:** Incorporate editor feedback as a reward signal to accelerate learning.

---

## Action Items

- **Taka (GrowthX):** Contact Mohitdeep Singh within a few days (likely within 24-48 hours) to discuss the next round of interviews.
- **Next Round:** Likely includes meeting more team members and a take-home assignment.

---

## Transcript

**Mohitdeep Singh:** Sorry, my UI was kind of stuck.

**Katja Wittfoth:** Can you see me now?

**Katja Wittfoth:** No worries.

**Katja Wittfoth:** Yes, I can see you now.

**Katja Wittfoth:** Is that Mohit?

**Mohitdeep Singh:** Yeah.

**Katja Wittfoth:** Perfect. I'm Katja, very nice to meet you.

**Mohitdeep Singh:** Sorry for pronouncing it wrong in the beginning.

**Katja Wittfoth:** No, no, you actually pronounced it correctly.

**Katja Wittfoth:** Well, very nice to meet you and thanks for taking the time to interview with us. So I'm Katja. I'm helping GrowthX with data and AI and currently also hiring data science team. I'm in an advisor role, so it's temporary. But professionally, I myself am a data scientist at a different company and also helping other companies with their data science AI projects.

**Katja Wittfoth:** So today, I have roughly the following plan. I would love to learn more about you, hear about your projects, and deep dive into one of them. I also have a couple of case studies based on GrowthX that I'd love to talk through with you. And that's pretty much it. How does that sound?

**Mohitdeep Singh:** That sounds great, actually.

**Katja Wittfoth:** Awesome.

**Katja Wittfoth:** So how about we start with you? If you can tell me a little bit more about yourself and your recent work.

**Mohitdeep Singh:** Sure. So I'm Mohit, and I have been working in the analytics domain for a little over eight plus years now.

**Mohitdeep Singh:** I'm currently working with Coupang. Previously, I have a lot of experience working with signal data. I think one of my most important projects was with Intel, where I was working as a research intern. My main purpose was to identify pipeline-based code that they could use with their chips. We didn't have a lot of resources, so I was mostly using legacy code to create CNN pipelines. My work was research-based—understanding what we could do in the deep learning world with Intel's existing hardware.

After my internship ended, I started working with Radio, which was mainly a project on audio classification and real-time personalization. This was around 2014, so we didn't have the cloud architectures and microservices we see now. We created a collaborative filtering algorithm, and my role was mostly to identify the different kinds of genres within music.

**Mohitdeep Singh:** And this was more into identifying the patterns that you see in audio files using spectrograms.

**Mohitdeep Singh:** So it was into signals.

**Katja Wittfoth:** Oh, so it's not on tags, it's like on the signal.

**Mohitdeep Singh:** Yes, it's on the signal. Yeah, it's actually very exciting to work on that. And back then we wrote the functions ourselves and we were kind of creating the embeddings from the spectrograms, you know, by a native pipeline that we had over there.

**Mohitdeep Singh:** So I was the data scientist that was working on the mode classification from those audio waveforms when I was working with radio.

**Mohitdeep Singh:** And similar kind of thing actually happened when I transitioned to Pandora. But my role slightly changed over there.

**Mohitdeep Singh:** So I was now looking at CNNs of these spectrograms, not directly interpreting the vibration data from the spectrograms and then creating embeddings from it.

**Mohitdeep Singh:** So that is, I think, one of my most formal introductions with the CNN pipelines that we see on Python today.

**Mohitdeep Singh:** And in addition to that particular pipeline, I was also doing textual analysis on the lyrics of the songs that you would hear on that platform.

**Mohitdeep Singh:** That kind of gave us two different channels that we could focus on.

**Mohitdeep Singh:** One of them was to find out the genres that you can figure out from the spectrograms.

**Mohitdeep Singh:** And the other point was people who focus a lot more on the lyrics as well. So my role over there was to design this particular CNN pipeline on the Spectrograms because I had that kind of experience when working with Radio.

**Mohitdeep Singh:** So it was actually a very exciting project for me.

**Mohitdeep Singh:** I got to learn a lot and mostly it was POCs, but I think it eventually went into the production, but I was no longer part of the production team.

**Mohitdeep Singh:** And we did some A-B testing on a few of the recommendations to find out whether they actually worked or not.

**Mohitdeep Singh:** Yeah.

**Katja Wittfoth:** That's awesome.

**Katja Wittfoth:** Yeah, I really heard good things about Pandora.

**Katja Wittfoth:** Also during my master's, I think there was some collaboration and presenters shared a lot of cool stuff from Pandora. Back in the day, Pandora was a company that took state-of-the-art pretty seriously.

**Mohitdeep Singh:** Yeah, I mean, they had a lot of hardware.

**Mohitdeep Singh:** I think they had very solid funding, given that you practically had no competition back then.

**Mohitdeep Singh:** I think there were a few platforms like GrooveShark, but they did not have the similar kind of footprint as Pandora had.

**Katja Wittfoth:** So after you joined Pinterest,

**Mohitdeep Singh:** Yeah, so I mainly joined Pinterest with a few of my friends' recommendations.

**Mohitdeep Singh:** So I had a few colleagues working over there.

**Mohitdeep Singh:** They were my friends from my bachelor's, and they kind of helped me refer to that position.

**Mohitdeep Singh:** And one of the key things that the hiring manager at Pinterest liked was my experience with the recommendation system that I had actually helped build in my tenure with Pandora.

**Mohitdeep Singh:** And he also saw that I had built a CNN based classification system for the spectrograms that you see on the audio signals, right?

**Mohitdeep Singh:** So those two experiences actually helped me for this particular role.

**Mohitdeep Singh:** Because if you look at the background of Pinterest, so it's mainly based around personalization of the home feed, right?

**Mohitdeep Singh:** I think Pinterest set the precedent for the Reels and Shorts that we kind of see now.

**Mohitdeep Singh:** But it was much more limited back then.

**Mohitdeep Singh:** We did not have so much of data.

**Mohitdeep Singh:** So we had a lot of cold starting problems with the recommendation systems.

**Mohitdeep Singh:** Because we did not have a lot of information about the users, like what they like and what you would actually recommend to the users.

**Mohitdeep Singh:** And they go into the platform.

**Mohitdeep Singh:** Then I think it created a survey where you could choose what kind of things you're interested in.

**Mohitdeep Singh:** And then we had a basic template of what 80 to 90% of the users actually like, depending on your choices.

**Mohitdeep Singh:** So my role over there was to help them improve their ranking system that uses.

**Mohitdeep Singh:** I think there were two different embedding models for the users and the pins.

**Mohitdeep Singh:** So we tried to integrate the CNN transformer models with the visual embeddings based on the images that the user is actually viewing.

**Mohitdeep Singh:** Later on, Pinterest started capturing click data and click stream data. We also captured how much time a user is spending around a particular kind of image, right? That kind of helped them with ad placement later on. I was mostly involved with the ensemble modeling of their vision transformer and ResNet models, not with the ad team.

**Mohitdeep Singh:** So, yeah, so the data was trained on millions, millions of bins, actually.

**Mohitdeep Singh:** And we were using approximate neighbor search indexing for retrieval of those particular kind of embeddings.

**Mohitdeep Singh:** And depending on the image that the person is actually liking or showing interest in it, we would place the ads.

**Mohitdeep Singh:** So that is, again, you know, two different things to optimize for, whether you want to increase the revenue or whether you want to increase the engagement on those feeds.

**Mohitdeep Singh:** Now, that's a very...

**Katja Wittfoth:** Which is the same, right, for Pinterest.

**Mohitdeep Singh:** Yes, yes, it is right now.

**Mohitdeep Singh:** But back then, they wanted to find out what actually kind of helps the users, what kind of...

**Mohitdeep Singh:** keeps them engaged, right?

**Mohitdeep Singh:** Because I think at around 2021, you're still, in Pinterest was still trying to pull itself out with the competition that Meta and other similar kind of platforms, you know, gave.

**Katja Wittfoth:** And you said the spin data, I see in your resume, it was using also GPT-A2, like by the hanging case?

**Katja Wittfoth:** Yes.

**Katja Wittfoth:** That's exciting, like very early use of the technology, right?

**Mohitdeep Singh:** Yeah, I mean, we had a lot of comments, right?

**Mohitdeep Singh:** And I think Hugging Face was everybody's friend back then.

**Mohitdeep Singh:** Like, you know, most of us engineers that we were working on different kinds of models and experimenting with different kinds of architectures, were using, you know, Hugging Face models that are readily available.

**Mohitdeep Singh:** And we did not have the large language models, right?

**Mohitdeep Singh:** So...

**Mohitdeep Singh:** So you had to use whatever was available over there.

**Mohitdeep Singh:** I think we tried using Flan T5.

**Mohitdeep Singh:** Flan was pretty good.

**Mohitdeep Singh:** And we were looking at long-former encoder models also.

**Mohitdeep Singh:** But I think those were kind of overkill for the comment section.

**Mohitdeep Singh:** Like that's all of the text data that you can actually extract.

**Mohitdeep Singh:** But most of the information actually came from the ensemble models because they have lots of images.

**Mohitdeep Singh:** And I think there were some GIFs also.

**Mohitdeep Singh:** But, you know, we did not process all of that.

**Mohitdeep Singh:** were mainly looking at still images.

**Mohitdeep Singh:** And we were creating a ResNet on top of that.

**Mohitdeep Singh:** And we were trying to train on those particular pins and find out, you know, what actually works or not.

**Mohitdeep Singh:** So very straightforward.

**Mohitdeep Singh:** And, yeah, so for this project, the main highlight was I...

**Mohitdeep Singh:** We used Google Cloud and they relied a lot on Databricks because the recommendation actually generates on the fly and you would actually need to wait some time for the, you know, you could see the skeletal framework and then it would have the new pins recommended to you, right?

**Mohitdeep Singh:** So I was part of that team and mostly it was based around image processing, what kind of loss functions we can combine with the text and any signals that we can extract from the image.

**Mohitdeep Singh:** So that's more or less what I had at Pinterest and...

**Katja Wittfoth:** Got it.

**Katja Wittfoth:** And then you joined Roku after that.

**Mohitdeep Singh:** Yes, yes.

**Mohitdeep Singh:** I joined Roku and they have...

**Katja Wittfoth:** It looks like you switched also from Pinterest ad to your...

**Katja Wittfoth:** Something that more like towards internal retention and churn, well, at least the two bullet points, right?

**Katja Wittfoth:** Maybe that was more, oh, ad ranking as well, but talk me through that.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** So to talk about ad ranking, there were mainly click-through rate models that kind of told you what kind of images the person is actually involved in.

**Mohitdeep Singh:** So we used a multi-objective optimization model for that, which was mainly focused around revenue and the engagement of it.

**Mohitdeep Singh:** So the model serving for this particular model was on Kubernetes, and we were doing a lot of feature competition using Spark.

**Mohitdeep Singh:** And we were using scan-based embedding stores for this.

**Mohitdeep Singh:** So that's, you know, my experience with the ad What is scan-based embedding stores?

**Mohitdeep Singh:** So these are embedding embedding stores that are.

**Mohitdeep Singh:** Primarily used for any kind of, you know, visual and any kind of text-based models that we have, right?

**Katja Wittfoth:** Because you need to find out the embeddings for that.

**Katja Wittfoth:** So it's basically scalable nearest neighbors, right?

**Mohitdeep Singh:** So it's built on Google and it's a vector similarity search.

**Mohitdeep Singh:** Nothing very fancy, but that's what it does.

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** Nice.

**Katja Wittfoth:** Okay.

**Mohitdeep Singh:** Yeah, so the main reason for extracting this embeddings is to find out whether the retrieval is actually working or not because you need to find out the recommendations for it.

**Mohitdeep Singh:** And that's why I have mentioned that as well.

**Mohitdeep Singh:** And depending on the images that you see, there is a database that kind of gets referred back to to find out what kind of ad themes you can push.

**Mohitdeep Singh:** And there are different categories.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** categories in that ad which have tags in them.

**Mohitdeep Singh:** Some of them are baby themed.

**Mohitdeep Singh:** Some of them are kind of construction themed, furniture themed because people come to Pinterest for ideas, right?

**Katja Wittfoth:** If they're building any kind of new things, maybe a new recipe, something little.

**Mohitdeep Singh:** So tags are very important over there and tags actually define what ads would go through it.

**Mohitdeep Singh:** So any kind of new cookware that people want to push.

**Mohitdeep Singh:** And the ad also had an internal ranking that kind of said which ads actually provide the good amount of revenue.

**Mohitdeep Singh:** And there is an engagement score with the ad as well.

**Mohitdeep Singh:** That kind of that's kind of predicted based on the similarity of such kind of ads in the past.

**Mohitdeep Singh:** So the ads team is, it's like a war room.

**Mohitdeep Singh:** You don't have a lot of space for missing on the ads.

**Mohitdeep Singh:** Right.

**Mohitdeep Singh:** They kind of generate the revenue for Pinterest.

**Mohitdeep Singh:** And coming to the ranking algorithm itself, it's very basic.

**Mohitdeep Singh:** When I was there, they were using associative filtering for it directly.

**Mohitdeep Singh:** So there were metrics of the user level interactions, and you had the users on one index, and then you run a similar vector decomposition on it.

**Mohitdeep Singh:** You find weights on it, and you kind of define the collaborative filtering inputs, depending on what kind of user behaviors you are getting.

**Mohitdeep Singh:** So very simple, but very good, because they have very good categorization of these ads.

**Mohitdeep Singh:** So that's how the ad ranking actually worked in Pinterest.

**Katja Wittfoth:** Okay, let's switch to the more recent experience.

**Katja Wittfoth:** Love to hear that.

**Mohitdeep Singh:** Yeah, so my most recent experience is with Coupang.

**Mohitdeep Singh:** And currently...

**Katja Wittfoth:** Like in between you were in Roku, but Roku seems to be like similar to Pinterest, right?

**Katja Wittfoth:** Like it's also an ad and retention, churn, et cetera.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** Maybe a couple of words there before we go to the Roku part.

**Mohitdeep Singh:** Yeah, I mean, so if I have to speak about Roku, the most interesting part of Roku is the scale of it.

**Mohitdeep Singh:** I mean, with Pinterest, I just have a image cards and maybe a few click-through data to go through it.

**Mohitdeep Singh:** But when it came to Roku, everything is through Kafka itself.

**Mohitdeep Singh:** And there is a lot of segmentation that goes into it.

**Mohitdeep Singh:** So I had actually built an audience segmentation model that kind of used K-means and DB scan.

**Mohitdeep Singh:** And there are propensity models in place as well.

**Mohitdeep Singh:** And the audience segmentation is primarily responsible for...

**Mohitdeep Singh:** Or pushing the ads that you see on the Roku platform.

**Katja Wittfoth:** And they have propensities for like their features or their products?

**Mohitdeep Singh:** they do.

**Mohitdeep Singh:** And they have a few things that are kind of determined based on your interaction with the website.

**Mohitdeep Singh:** So basically...

**Katja Wittfoth:** my guess, is it more like XGBoost or...

**Mohitdeep Singh:** It's mainly XGBoost.

**Mohitdeep Singh:** It's not CMM-based because even if...

**Mohitdeep Singh:** I'm not entirely sure like how the internal data actually gets processed.

**Mohitdeep Singh:** But the main target is to find out how the user is most likely to respond to a given thing, right?

**Mohitdeep Singh:** You have a thing or a card or an ad.

**Mohitdeep Singh:** So the main data collection point is clicks.

**Mohitdeep Singh:** Okay, clicks and conversions.

**Mohitdeep Singh:** What is the dwell time?

**Mohitdeep Singh:** What is the watch time?

**Mohitdeep Singh:** If there are any kind of search events right after that.

**Mohitdeep Singh:** And there are a few other things like what kind of device the user is on, if they're using the media box, if they're on a streaming platform.

**Mohitdeep Singh:** So if I have to talk about the propensity itself, we created a lot of user-related features.

**Mohitdeep Singh:** Some of the contextual features like what time of the day, what is the category of channel, what kind of app versions there were.

**Mohitdeep Singh:** And, you know, there were a few interaction features as well.

**Katja Wittfoth:** So would it be, what is the cadence of predictions this year?

**Katja Wittfoth:** Was it batch or real time?

**Mohitdeep Singh:** It was batched.

**Katja Wittfoth:** It's not like daily or weekly.

**Mohitdeep Singh:** It's daily.

**Mohitdeep Singh:** I wouldn't say daily.

**Mohitdeep Singh:** So it's mini batch based.

**Mohitdeep Singh:** So if I have to talk about just one particular user, so there are different categories of users and the batches actually get segmented on the basis of the time when the user is most likely to interact.

**Mohitdeep Singh:** So you have two batches per user, and that gets divided based on the most likely time of the day you would interact with the platform because they want to do a lot of ad revenue, right?

**Katja Wittfoth:** Oh, and like basically they use propensities for ad piping.

**Katja Wittfoth:** Ah, okay.

**Katja Wittfoth:** This is great.

**Katja Wittfoth:** Awesome.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** And if I...

**Mohitdeep Singh:** Sorry.

**Mohitdeep Singh:** If I have to talk about the content features as well, you have a lot of tags over here as well.

**Mohitdeep Singh:** And that kind of are dependent on what kind of...

**Mohitdeep Singh:** Streaming thumbnails the user is interested in, if there is any kind of user that is looking at the genre of the things, if they're interested in particular actors, production houses, all those kind of things.

**Mohitdeep Singh:** So it all boils down to the interaction features that kind of tell you it's a matrix of user with the content max score and historical engagement similarity, which is a query.

**Mohitdeep Singh:** And there are a few affinity features that kind of define, okay, the user might be actually interested on it.

**Mohitdeep Singh:** So the scale of the features is overwhelming, actually, because they have, the layout is very similar to the other OTT platforms, right?

**Mohitdeep Singh:** You have one row, have flashcards, and then you can actually scroll through the page as well.

**Mohitdeep Singh:** And you have other devices that kind of interact with the APIs, mean, the Roku platform, platform,

**Mohitdeep Singh:** So there are a few baseline models, like you said, XGBoost is one of them, and there is a logistic regression model as well.

**Mohitdeep Singh:** So the main purpose of having this logistic regression model is to find out what is the probability of, you know, the user interacting with this, basically the propensity of it, and how much can you gamble on top of it.

**Mohitdeep Singh:** So you have...

**Katja Wittfoth:** That's great.

**Mohitdeep Singh:** Yeah, so on one hand, you have the prediction of whether it will happen or not, and on one hand, you have a regression slope that you can actually go down, because you cannot just use logistic regression as is, right?

**Mohitdeep Singh:** You can chalk out the probabilities around it, and then you can have a linear regression model, and you can move down the slope, and you can find out how much of the probability are you losing.

**Mohitdeep Singh:** So that works very closely with the revenue and the ads team.

**Mohitdeep Singh:** So...

**Mohitdeep Singh:** So that's how I think most of the ad revenue models are kind of selected.

**Mohitdeep Singh:** And we usually have business meetings around, you know, what should be the probability for some of the new things that get launched on the platforms.

**Mohitdeep Singh:** So I don't know how things are run now.

**Mohitdeep Singh:** I mean, but it's still very fresh to me because it was very recent.

**Katja Wittfoth:** And yeah, but let's talk about the recent experience, especially I see that you're really very experienced in traditional ML.

**Katja Wittfoth:** So maybe we can focus on Gen AI, LLMs as of recent work you were doing.

**Mohitdeep Singh:** Yeah, sure.

**Mohitdeep Singh:** That sounds great, actually.

**Mohitdeep Singh:** So currently, when I had, not currently, I mean, I had joined Coupang in 2024.

**Mohitdeep Singh:** And one of the key challenges that, you know, Coupang...

**Mohitdeep Singh:** What was facing is they did not have very good feature stores.

**Mohitdeep Singh:** Okay.

**Mohitdeep Singh:** So I was the key engineer in that.

**Mohitdeep Singh:** That kind of design, what the distributed data engine would be, what their pipelines would actually look like.

**Mohitdeep Singh:** So we had to create a Delta Lake, which kind of acts as a feature store.

**Mohitdeep Singh:** I mean, it's still getting built.

**Mohitdeep Singh:** So the main purpose of this is to find out the cataloging behavior, what kind of product metadata we have.

**Katja Wittfoth:** Because it's a payment gateway, right?

**Mohitdeep Singh:** So we have a lot of scope for pushing these ads over here as well.

**Mohitdeep Singh:** And that kind of contains a lot of text embeddings as well.

**Mohitdeep Singh:** And some of them are session-based features, which are kind of anonymized.

**Mohitdeep Singh:** So what I did over here is there was a lot of text and metadata, right?

**Mohitdeep Singh:** So for the embeddings, I was actually using it.

**Mohitdeep Singh:** Stilbert for the reviews, and we were having domain-specific embedding space, and we were using an ANN index, which is in memory.

**Mohitdeep Singh:** We were using Fathom for it, actually.

**Mohitdeep Singh:** So if I have to talk about the Gen A I use in it, I was using VectorDB Ingestion, and for that, I was using a lot of Firecrawl and Bing Search.

**Mohitdeep Singh:** So this was a structured RAG approach, okay?

**Mohitdeep Singh:** This is mainly to find out semantic similarities, so basically semantic retrieval for content generation pipelines.

**Mohitdeep Singh:** So instead of relying on a collaborative filtering algorithm, going through all the hoops of cold-starting, finding out extra features that might actually work or not, we completely took a different route that kind of creates the embeddings on the text data that's available.

**Mohitdeep Singh:** And then...

**Mohitdeep Singh:** Find out what might actually work based on the outputs of the RAC.

**Mohitdeep Singh:** So there is actually two stages for this recommendation system.

**Mohitdeep Singh:** One of the stages is kind of it's detecting the candidates.

**Mohitdeep Singh:** Sorry, it's generating the candidates.

**Mohitdeep Singh:** So the main point of this is to find out the similarity of these embeddings of the candidate embeddings with whatever we have.

**Mohitdeep Singh:** And then there is a ranking model.

**Mohitdeep Singh:** Which uses GRU on clickstream data.

**Mohitdeep Singh:** That kind of finds out, you know, what kind of, you know, sequences, sequence generation we can actually think about generating.

**Mohitdeep Singh:** So if I have to create a particular pipeline, so there was a, so you research on the reviews or whatever kind of things you have.

**Mohitdeep Singh:** You create a finaliber,

**Mohitdeep Singh:** Third strategy, which I already mentioned to you, then you do a planning around it, you draft it, and then you finally see what might actually work.

**Mohitdeep Singh:** Basically, you can do A-B testing on it, and you finally go for changing it.

**Mohitdeep Singh:** So that is what happened at Copank.

**Mohitdeep Singh:** So it's candidate generation, you rank it, and then you select the final, you know, suggestions based on it.

**Mohitdeep Singh:** So that's, you know, what I've been doing with Gen.ai very recently.

**Mohitdeep Singh:** And the other equivalent is fraud detection pipeline, and that's a separate team that I'm also involved with.

**Mohitdeep Singh:** So the main idea is to find out any kind of behavioral anomalies within the transaction data itself.

**Mohitdeep Singh:** So it's mainly around what kind of transactions are kind of unexpected from a particular...

**Mohitdeep Singh:** The kind of user that includes like any kind of time, it could be amount, if there are chargebacks, if there are very frequent transactions of a particular amount that kind of happen.

**Mohitdeep Singh:** And there are a few cybersecurity flags as well that kind of gets handed over.

**Mohitdeep Singh:** So it's a very neat process, but the main challenge over here is to get it done in under a few seconds.

**Mohitdeep Singh:** You don't have a lot of time on this.

**Mohitdeep Singh:** So my role over here is to mainly make sure that the models are up to date.

**Mohitdeep Singh:** So there are autoencoders in place that kind of create the embeddings.

**Katja Wittfoth:** What type of like text would be used here?

**Katja Wittfoth:** So I can imagine that transactions mostly are tabular data.

**Katja Wittfoth:** But is there any text you were using for...

**Mohitdeep Singh:** So it's mainly based around the text that is generated by the platforms, right?

**Mohitdeep Singh:** So you can't have much of the data coming directly from the user.

**Mohitdeep Singh:** So much of the feature engineering or text-based data is generated by the platform itself.

**Mohitdeep Singh:** So it becomes very easy for us from that because, you know, systems can only generate particular type of text around it and you can have very good feature extraction pipelines from that.

**Mohitdeep Singh:** So if I have to talk about behavioral anomaly detection and mainly it tries to look for any kind of abnormal structures around any kind of outputs that are coming from the system.

**Mohitdeep Singh:** And, uh,

**Mohitdeep Singh:** So, you know, if there are any kind of points that require very less number of splits, then we can find out that it's very anomalous because a user will not have very similar kind of transactions going again and again at the same time, which kind of detects it might be particularly fraudulent behavior.

**Katja Wittfoth:** So, can you give me like an example of, so I can understand what is exactly like a LLM component use or like which type of data was inputted and what is the example of like fraudulent part on that?

**Mohitdeep Singh:** Yeah, sure.

**Mohitdeep Singh:** So, number one thing that gets captured with any kind of payment website is user behavior.

**Mohitdeep Singh:** One, and you can capture user behavior from a web.

**Mohitdeep Singh:** Using the count of clicks, if there are purchase counts, what is the time between the actions, if there are any kind of returns that might happen for that particular transaction.

**Mohitdeep Singh:** If somebody is abandoning the cart, that is also one of the features.

**Mohitdeep Singh:** And there are session level features like entropy.

**Mohitdeep Singh:** And if you particularly, it's unusual nighttime behavior.

**Mohitdeep Singh:** Not a lot of transactions happen in the late night, unless the user is particularly doing that.

**Mohitdeep Singh:** So that's user feature.

**Mohitdeep Singh:** Coming to the transaction features, you have switching between payment methods.

**Mohitdeep Singh:** That is very unlikely to happen.

**Katja Wittfoth:** But don't, like, this is all sounds to me very tabular.

**Katja Wittfoth:** Like, I don't understand where's the LLM component.

**Katja Wittfoth:** Like, why would we use anything in LLM?

**Katja Wittfoth:** Or are you saying we use LLM for feature generation?

**Mohitdeep Singh:** Feature creation?

**Mohitdeep Singh:** Yes.

**Katja Wittfoth:** Ah, feature engineering.

**Mohitdeep Singh:** Okay.

**Katja Wittfoth:** So...

**Katja Wittfoth:** So we're not like using actually LLM for like detecting, it's only the feature engineering part.

**Mohitdeep Singh:** You could say that, but mainly we were creating agents that tries to find out abnormal structure within these transactions.

**Mohitdeep Singh:** If there are any kind of tone mismatches, hallucination facts.

**Mohitdeep Singh:** And, you know, these are the kind of anomalies that we were trying to detect using LLMs itself.

**Mohitdeep Singh:** So, yeah, I mean, they were not directly interfacing the pipeline itself because you have slick stream data and it makes very little sense to use LLMs.

**Mohitdeep Singh:** But instead of you doing the feature engineering and training a different kind of model, you can actually interface few of the LLM agents based on similar kind of patterns that, you know, Coupang has already seen because we have.

**Mohitdeep Singh:** of good data on transaction and that kind of helps the LLM to find out this might be a very similar kind of case.

**Mohitdeep Singh:** So mainly it happens after the ingestion and to find out whether that particular feature has to be flagged or not on all of the features that I already mentioned to you.

**Mohitdeep Singh:** So user level, transaction level, any kind of device level, or, you know, sometimes users have multiple accounts.

**Mohitdeep Singh:** They switch between the accounts.

**Mohitdeep Singh:** That's very unlikely to happen in a very short period of time.

**Mohitdeep Singh:** So, yeah, so that's one of the things.

**Katja Wittfoth:** Yeah, that sounds good.

**Katja Wittfoth:** But maybe to your experience, if you can share with me latest project you've done that you are particularly proud of, especially if it's in LLM space, that would be amazing.

**Katja Wittfoth:** And if you can share.

**Katja Wittfoth:** Or like with me, what was the problem?

**Katja Wittfoth:** Who were the stakeholders?

**Katja Wittfoth:** How did you approach it?

**Mohitdeep Singh:** And what was the outcome?

**Mohitdeep Singh:** Yeah, so I would go back to the project that I was talking about.

**Mohitdeep Singh:** And that's mostly around the content generation side of things.

**Mohitdeep Singh:** So we already have a lot of users, right, at Coupang.

**Mohitdeep Singh:** And we have a lot of vendors that actually give us information on any kind of new products.

**Mohitdeep Singh:** That include summaries, insights, any kind of competitor comparisons, those kind of things.

**Mohitdeep Singh:** So we need to recommend these products.

**Mohitdeep Singh:** And like I said earlier, the product recommendation at Coupang did not have a very good feature store.

**Mohitdeep Singh:** And the recommendations actually did not work very well.

**Mohitdeep Singh:** Because not fast enough.

**Mohitdeep Singh:** And some of them had really bad cold starting problems.

**Mohitdeep Singh:** So if I have to talk about the architecture itself, so a lot of ingestion happened from the product information website, PDFs, URLs, etc.

**Mohitdeep Singh:** And that mainly found out any 20 to 30 chunks of every kind of product.

**Mohitdeep Singh:** And finally, we created a summary on top of the products that kind of have the theme, what is the sentiment, what is the competitive comparison, the executive summary, and all of that.

**Mohitdeep Singh:** Basically, a card about the product.

**Mohitdeep Singh:** And that is my product level information.

**Mohitdeep Singh:** And we actually store it in a separate embedding database after generating the embeddings from it.

**Mohitdeep Singh:** Now, coming to the user side of things, I have already mentioned to you about the different kind

**Mohitdeep Singh:** Kind of user click-level data that gets actually captured, right?

**Mohitdeep Singh:** And that includes interaction with the website, what kind of products they are buying, what kind of vendor site they actually go to.

**Mohitdeep Singh:** So these things can be actually leveraged for creating a matrix for the different kind of users.

**Mohitdeep Singh:** And then the matrix is actually converted to trees.

**Mohitdeep Singh:** And the graph, basically the tree of these users can be used to recommend similar kind of products to new users that kind of use the platform.

**Mohitdeep Singh:** Now that we have two different inputs, we have the information about the user and we have the information about the products as well.

**Mohitdeep Singh:** So what happens is it becomes very easy to recommend new products to the user.

**Mohitdeep Singh:** Now, one of the major challenges that we were facing is these recommendations were not very good looking.

**Mohitdeep Singh:** I mean, they are very generic.

**Mohitdeep Singh:** I'm looking, you know, they seem very AI-generated, okay?

**Mohitdeep Singh:** The product owners actually did not like that.

**Mohitdeep Singh:** So what I did is I took this information, I took this data.

**Mohitdeep Singh:** So basically I have sequences, right?

**Mohitdeep Singh:** And I actually trained one of the distilled models on top of this model.

**Mohitdeep Singh:** Basically I fine-tuned that model.

**Mohitdeep Singh:** And to do that, I used SageMaker.

**Mohitdeep Singh:** And I was doing it on AWS because we were not getting enough resources on Azure.

**Mohitdeep Singh:** And we did it for, you know, we did it for four to five epochs on the entire data itself.

**Mohitdeep Singh:** And we had around 100 million records for fine-tuning that.

**Mohitdeep Singh:** And the sequence generation or, you know, we actually tracked for publicity of the fine-tuned model.

**Mohitdeep Singh:** And I was doing a low-right adaptation of the 5.4 model for around eight layers.

**Mohitdeep Singh:** And after doing it, we got almost 19%.

**Mohitdeep Singh:** Improvement on top of what we were seeing from the generated product recommendations for the users.

**Mohitdeep Singh:** So that's, you know, my most recent project, which used LLM fine-tuning, and I was also recommending the LLM based information to the users.

**Mohitdeep Singh:** And for this entire process, I had just a three-member team.

**Mohitdeep Singh:** I was the main engineer, or you can call me as a data science researcher.

**Mohitdeep Singh:** was other?

**Mohitdeep Singh:** Other two?

**Mohitdeep Singh:** Who was other two?

**Mohitdeep Singh:** There were two data engineers that kind of worked with me, which they were mainly helping me for retrieval.

**Mohitdeep Singh:** And, you know, it was not very strictly defined, the roles.

**Mohitdeep Singh:** We kind of did everything, just till we got the API actually.

**Mohitdeep Singh:** So everything, I think, right, in today's date, every company is kind of following the same kind of structure.

**Mohitdeep Singh:** They create microservices.

**Mohitdeep Singh:** So we also did that.

**Katja Wittfoth:** How long was the project?

**Mohitdeep Singh:** So this project was almost 11 months long.

**Mohitdeep Singh:** And we got good results.

**Mohitdeep Singh:** We were getting almost, if I have to track about involvement with the new kind of products, that was boosted around 19 to 20%.

**Mohitdeep Singh:** And that was very good, considering the fact that this was only the first iteration.

**Mohitdeep Singh:** And we actually deployed into production.

**Katja Wittfoth:** So that's great.

**Katja Wittfoth:** And do you usually work with a product manager or is it more like with engineering?

**Katja Wittfoth:** Or what's, like, the day-to-day look like?

**Mohitdeep Singh:** On a day-to-day basis, I have a lot of interactions with the product manager because since AI is not very cheap, they want to track where the expenses are going and what are the kind of results.

**Mohitdeep Singh:** So I make sure that, you know, within my team, everybody has the tickets updated.

**Mohitdeep Singh:** They put everything in the comments where they're stuck.

**Mohitdeep Singh:** If they need any kind of pair-coding help, I do that.

**Mohitdeep Singh:** And, you know, the basic stuff.

**Mohitdeep Singh:** I think that's kind of expected from any kind of senior member within the team.

**Mohitdeep Singh:** I try to be as much collaborative as possible.

**Mohitdeep Singh:** And we have PowerPoint presentations almost two weeks by the end of every sprint.

**Mohitdeep Singh:** And that kind of highlights if the team has achieved anything significant or new or, you know, any kind of challenge.

**Mohitdeep Singh:** just that we might be facing so that it gives a very clear picture to the leadership of where we are actually, what we are doing.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Well, thanks for sharing.

**Katja Wittfoth:** I would love to switch gears to growthx case study, if that is okay with you.

**Katja Wittfoth:** So I'll give you a concrete growthx problem.

**Katja Wittfoth:** I would love you to walk me through how you would approach it.

**Katja Wittfoth:** So it's really, you know, conversation and brainstorming together.

**Katja Wittfoth:** So at growthx, we generate the long form content for clients, right?

**Katja Wittfoth:** And we want, of course, a reliable way to deliver and measure quality of the content.

**Katja Wittfoth:** And also a way that we can systematically improve it all the time.

**Katja Wittfoth:** So we'd love...

**Katja Wittfoth:** I'd to hear your thoughts and ideas on how would you define quality, or actually, in general, how will you design a system that scores content quality and uses the scores to improve over time?

**Mohitdeep Singh:** Okay.

**Mohitdeep Singh:** So mainly, I think the challenge is to score the content, right?

**Mohitdeep Singh:** Because that will actually drive confidence within the people who are actually consuming it.

**Mohitdeep Singh:** So, if I say that you are publishing a lot of articles or generating a lot of articles, and I'm assuming growthx is mainly based around marketing and, you know, the product domains, right?

**Mohitdeep Singh:** So it needs to speak the language of the leadership of that particular company.

**Mohitdeep Singh:** So I...

**Mohitdeep Singh:** I think that makes a very good case for using growthx as their main partner for, you know, content generation and engagement, right?

**Mohitdeep Singh:** So one of the main things that needs to be defined are the main quality pillars or, you know, what you would track.

**Mohitdeep Singh:** So you look for factuality and accuracy, you look for structure and coherence, and you look for the keyword coverage, basically SEO stuff.

**Mohitdeep Singh:** And you also do one more thing, which kind of matches the voice of the brand or, you know, the style of the writing that the brand actually has.

**Mohitdeep Singh:** And then you try to find out propensity over here as well, whether the, you know, the generated content is actually going to be interacted a lot or not.

**Mohitdeep Singh:** So a model at the end, which kind of tells you what is the likelihood of engagement going to.

**Mohitdeep Singh:** For us, I mean, if growthx had to measure their own content.

**Mohitdeep Singh:** So those are the, you know, five main pillars that I would define for any kind of, you know, content quality checking.

**Katja Wittfoth:** Now, can you repeat all of them?

**Mohitdeep Singh:** Yes.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** So number one would be to check for the facts that are actually stated.

**Mohitdeep Singh:** Yeah.

**Mohitdeep Singh:** Factuality of it.

**Mohitdeep Singh:** The second would be to check for the structure of the content that is generated.

**Mohitdeep Singh:** The third would be to check for tags, keywords, basically SEO stuff.

**Mohitdeep Singh:** And then you check for the language or the style of writing of the content generation.

**Mohitdeep Singh:** And at last, you try to find out what is the likelihood of the engagement of this content going to look like.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** What do we do after?

**Mohitdeep Singh:** What after?

**Mohitdeep Singh:** What What What

**Mohitdeep Singh:** Yeah, so coming to the scoring pipeline, you can create a multi-agent system.

**Mohitdeep Singh:** And since you are already going to leverage generative AI for most of the things, we try to find out the context, number one, that kind of tells us what the competitor content is actually looking like.

**Mohitdeep Singh:** We look through the client source documents or whatever has been provided to us.

**Mohitdeep Singh:** We retrieve what are the different kind of styles or any kind of financial language, any kind of jargon that they have given in the public statements.

**Mohitdeep Singh:** And we basically create these samples for us.

**Mohitdeep Singh:** So this will help us rate our generated content versus what we have actually seen.

**Mohitdeep Singh:** So a supervised approach, basically.

**Mohitdeep Singh:** And you need a fact check agent that kind of checks for, you know, all these different kinds.

**Katja Wittfoth:** of claims that are created in the generated content, right?

**Mohitdeep Singh:** You check for the claims using entities, if there are any kind of numbers within the prompt versus what you are actually getting in the final generated context.

**Mohitdeep Singh:** And you also check for any kind of noun-based keywords, whether that was actually mentioned correctly or not.

**Katja Wittfoth:** And you check for any...

**Katja Wittfoth:** will check it against what?

**Katja Wittfoth:** So we will extract this as entities and then...

**Mohitdeep Singh:** Yeah, so you can check it with the prompt itself.

**Mohitdeep Singh:** So I'm assuming the prompt is going to come directly with data injected from the data sources that you have created.

**Mohitdeep Singh:** And then finally, you have the generated content, right?

**Mohitdeep Singh:** And in the generated content, you can run the same entity extraction pipeline.

**Mohitdeep Singh:** You can use PC for it.

**Mohitdeep Singh:** You can use any kind of pre-trained entity extraction pipeline for it.

**Mohitdeep Singh:** Right.

**Mohitdeep Singh:** And you can extract numbers, you can extract nouns, and you can actually look for any kind of...

**Mohitdeep Singh:** We have repeated subsequences, any kind of similar kind of words or groups of words kind of happening again and again.

**Mohitdeep Singh:** So that is going to tell you whether it is hallucinating or not.

**Mohitdeep Singh:** And you can score each of the chunks that is generated versus the prompt that was actually provided based on a very simple count analysis, right?

**Mohitdeep Singh:** Whether it is actually happening or not.

**Mohitdeep Singh:** So that's very easy to check.

**Mohitdeep Singh:** And every content that gets generated, we check for these claims and facts and see whether it is actually true or not.

**Mohitdeep Singh:** One of the other things that you can actually track is use a TER score.

**Mohitdeep Singh:** So TER score will actually tell you, you know, how many items you need from the source to actually reach to the destination, right?

**Mohitdeep Singh:** Because you're kind of compressing the...

**Mohitdeep Singh:** So if it's very far, and if the score is really high, you can say that, okay, there might be something really wrong, and it might need to be flagged as well.

**Mohitdeep Singh:** You can decide the thresholds based on the different samples that you run through it.

**Mohitdeep Singh:** So that kind of needs to be checked.

**Mohitdeep Singh:** But the next agent should actually check for any kind of missing links between the entities.

**Mohitdeep Singh:** So it's kind of a little bit more complex, but it will actually evaluate what is the logical connection between the different kind of entities.

**Mohitdeep Singh:** And you can have the Flesh score around it, or I think you can have the Kinkade score for the readability of these contents that gets generated.

**Mohitdeep Singh:** And you can also detect...

**Mohitdeep Singh:** The repetition using the structure and the readability agent.

**Mohitdeep Singh:** So that is going to check for the structure of the content that is getting generated with this agent, right?

**Mohitdeep Singh:** So that will solve the structural problem.

**Mohitdeep Singh:** Now coming to the SEO.

**Katja Wittfoth:** Can you talk me through, for example, flash reading score?

**Mohitdeep Singh:** Is that something that out of the box?

**Mohitdeep Singh:** No, it's a, yeah, I mean, you can use it directly on the content that is kind of generated, right?

**Mohitdeep Singh:** So it is going to tell you, so you are looking at the article from New Yorker, right?

**Mohitdeep Singh:** Some of the articles are very difficult to read because the facts are kind of very linked and it's not very understandable.

**Mohitdeep Singh:** It's to the user unless they already know about it, right?

**Mohitdeep Singh:** So you can use this agent to find out if the content that is getting generated is easy to read or not.

**Mohitdeep Singh:** Because we want more people to interact with the content, right?

**Mohitdeep Singh:** And the Flesch-Kincade score can actually tell you whether the text is going to be easily readable.

**Katja Wittfoth:** I'm just wondering if it's like, I'm not familiar with this measurement.

**Mohitdeep Singh:** Is that something that is like statistical score or is it out of the box?

**Mohitdeep Singh:** Okay, so it's not like something we need to define it.

**Mohitdeep Singh:** So if I have to tell you, so there are three main parameters that kind of needs to check with.

**Mohitdeep Singh:** And one of them is the total number of words divided by the total number of sentences.

**Mohitdeep Singh:** How many syllables you have divided by the total number of words.

**Mohitdeep Singh:** So, yeah.

**Katja Wittfoth:** That's basically something that is used like in a grade level school system.

**Mohitdeep Singh:** Ah, got it.

**Katja Wittfoth:** Yeah, now I remember.

**Mohitdeep Singh:** So that's one of the key things that you can actually use for, you know, just to check for readability.

**Mohitdeep Singh:** Because if it can be related to the reader, the engagement is going to be really high.

**Mohitdeep Singh:** But if the reader feels a little bit overwhelmed that, okay, I'm not understanding this, then probably they're not going to interact with that content a lot.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Let's maybe skip the text SEO and go into the quickly style and then more into the engagement likelihood.

**Mohitdeep Singh:** Yeah, sure.

**Mohitdeep Singh:** So, one of the things that you can use for the brand.

**Mohitdeep Singh:** Or the tone itself is you can have embedding-based similarity model which has the brand examples with it.

**Mohitdeep Singh:** Basically how the brand is actually writing and you can match the embeddings to check for any kind of tone, the style of the writing, and you can check for vocabulary.

**Mohitdeep Singh:** I think vocabulary is going to be the main determining factor when it comes to the tonality of the voice itself, I mean the content generation itself.

**Mohitdeep Singh:** So you can have a loop around it, a final agent that is mainly going to paraphrase this particular content that is generated again and again till it reaches a specific alignment or a deviation score.

**Mohitdeep Singh:** So what I mean to say is that you can have a TER score over here as well and because it's going to be the same kind of content, it should...

**Mohitdeep Singh:** At least have 90% usage of the vocabulary that has been already used in the brand in the past, right?

**Mohitdeep Singh:** And it has to be very similar.

**Mohitdeep Singh:** So one way to ensure it is you keep paraphrasing it till you get your desired output.

**Mohitdeep Singh:** The other way is you can actually have these samples of data with yourself.

**Mohitdeep Singh:** You can have a fine-tuned model, a very small model.

**Mohitdeep Singh:** I'm talking about a 3.5 billion or a 2.5 billion parameter model because you are not going to do any kind of complex classification or sequence generation, right?

**Katja Wittfoth:** It is actually really simple.

**Mohitdeep Singh:** It's just going to paraphrase it.

**Mohitdeep Singh:** So you can train it for four to five LoRa layers and you can use that model in the end to just paraphrase the information that has come from the agent on top of them.

**Katja Wittfoth:** And that will give you the brand voice.

**Mohitdeep Singh:** Okay, this is how the brand voice actually

**Mohitdeep Singh:** Looks like.

**Mohitdeep Singh:** And, yeah, I think that will take a little bit of time and effort because you need really good examples.

**Mohitdeep Singh:** And I think they need to be human reviewed in the beginning just to make sure that it actually looks good.

**Mohitdeep Singh:** And, yeah, so that's the tonality of it.

**Mohitdeep Singh:** So I can talk about the last one, which is, you know, the engagement scoring.

**Mohitdeep Singh:** So to engagement scoring, you have all these features, right?

**Mohitdeep Singh:** And you can actually find out whether the particular user is going to use it or not.

**Mohitdeep Singh:** So if you kind of have all these features, you can track what is the traffic is for a particular content in the last 30 days.

**Katja Wittfoth:** You can check the ranking.

**Mohitdeep Singh:** For the primary and the secondary keywords, what is the time the user is kind of spending, and you can actually convert all of this into one or zero, right?

**Mohitdeep Singh:** Basically, it is performing very nicely, or it is not performing nicely, it's low performing.

**Mohitdeep Singh:** So you can have multiple features in it, like what is the content length, what is the paragraph density, if you can have the FK scores as well, like I mentioned.

**Mohitdeep Singh:** And semantic features, and all those features.

**Mohitdeep Singh:** So it's not going to be a very complex model, it's just going to have a lot of features in it.

**Katja Wittfoth:** Well, that sounds good, and this is something that you think this will be basically a quality score composite of these five elements.

**Mohitdeep Singh:** Yeah, and you can create an equation of these differences.

**Mohitdeep Singh:** That's create an that you do.

**Mohitdeep Singh:** We call it as engagement, and it can be the constants or the lambda values that you have on top of all these different kind of features, like the keywords, the structure, the readability, the tonality of it, the factuality of it.

**Mohitdeep Singh:** So you can tweak these things based on which vendor is actually coming to you.

**Mohitdeep Singh:** So some might need more factuality, not much of the tone.

**Katja Wittfoth:** So to question, maybe here to just wrap it up because we're almost at time, but I also want to leave at least like one minute for you to ask me questions.

**Katja Wittfoth:** So you mentioned how you would create all of the scores.

**Katja Wittfoth:** would love to hear your opinion on like that method versus creating an LLM as a judge and where we could use the LLM as a judge in this process.

**Katja Wittfoth:** And the second question is...

**Katja Wittfoth:** Where would you see reinforcement learning in the process, if at all, for this type of, you know, improvement of the content all the time?

**Mohitdeep Singh:** One of the key things, okay, that's a lot of questions.

**Mohitdeep Singh:** So if I have to put in reinforcement learning, you have to put policies around the scoring, right?

**Mohitdeep Singh:** Because I already defined the engagement scoring.

**Mohitdeep Singh:** So you can actually create a reinforcement learning agent that acts like a content engine for the, you know, growthx.ai.

**Mohitdeep Singh:** And what that basically does is you create the states, you create the actions.

**Mohitdeep Singh:** The state is mainly going to be the scores, right?

**Mohitdeep Singh:** Your scores are basically your nodes.

**Mohitdeep Singh:** And you can add a few things for the competition.

**Mohitdeep Singh:** And you can define the actions, whether it should rewrite it, whether it should...

**Mohitdeep Singh:** Simplify it, whether it should do research again, if it needs to add citations, and you can create a reward structure, like if the hallucination count is decreasing, the keyword score is increasing, readability score is increasing.

**Mohitdeep Singh:** So that's your environment setup, right?

**Mohitdeep Singh:** And you can have many different types of rewards, like the immediate reward, the intermediate reward, or you can have a long-term reward at the end.

**Mohitdeep Singh:** And if I have to talk about algorithm, so...

**Katja Wittfoth:** Don't worry about this.

**Katja Wittfoth:** I just wanted to know, like, high level, and maybe, like, a few words about LLM suggestion, we can wrap up.

**Katja Wittfoth:** Like, I don't need, like, deep, just a few words.

**Katja Wittfoth:** Where would you use it, if at all?

**Mohitdeep Singh:** Yeah, I think this is going to be a reinforcement learning based on online feedback, right?

**Mohitdeep Singh:** It's going to come directly from the online...

**Mohitdeep Singh:** And you can use editors or you can use somebody from the client side itself that kind of gives you the clarity or the usefulness of it.

**Mohitdeep Singh:** And you can use this because at some point you will need it, even though the RL algorithm might work at a certain time.

**Mohitdeep Singh:** But if you want it to work a little bit earlier, then the editor feedback will be very useful in this context.

**Mohitdeep Singh:** Given that you will be generating the content for them.

**Katja Wittfoth:** Awesome.

**Katja Wittfoth:** Well, thank you so much.

**Katja Wittfoth:** And unfortunately, we ran out of time, but I'm okay to stay for another one or two minutes if you have questions to me.

**Katja Wittfoth:** And if you have time.

**Mohitdeep Singh:** Yeah, sure.

**Mohitdeep Singh:** I can spare a few minutes. So Daniel actually showed me a lot of stuff that GrowthX is doing. It seemed very exciting. I don't really remember all the tools he showed, but I saw that you have a very good UI—it's very clean, and you're recommending a lot of stuff for the clients.

**Mohitdeep Singh:** I know that GrowthX is using a lot of agents, so since you mentioned one of the most challenging problems at GrowthX, so I wanted to know if you are using reinforcement learning now, or that's something you're still planning?

**Katja Wittfoth:** Yes, we are not using reinforcement learning, but I think this is really a next step to start thinking about this.

**Katja Wittfoth:** That's why I was asking you those questions.

**Mohitdeep Singh:** I think this is something that Daniel is already thinking of implementing, and something we would love to see very soon. That sounds actually very exciting. So I just had one more question—what's the team actually look like? How is work actually tracked?

**Katja Wittfoth:** I can't really speak to that directly because I'm not working directly with the team—I'm more in an external advising role. But from what I observe, the culture is open. Daniel and Marcel are running the company in a way that's open to feedback and new approaches. Daniel is looking for someone in this role who can bring creative, state-of-the-art approaches that maybe just came out and we can implement in the company. There's a lot of openness to innovation, which is a great culture. And from what I observe, they're remote-first and have a very strong writing culture as well.

**Katja Wittfoth:** So a lot of like updates and thoughts are shared via writing.

**Katja Wittfoth:** And I think this is, it makes also a lot of sense and is good for like people to like 3D put their thoughts and collaborate on more deeper level than, you know, constant ad hoc meetings, but rather like have everything written down.

**Mohitdeep Singh:** So if that is, if that answers your questions.

**Mohitdeep Singh:** No, sounds great, actually.

**Mohitdeep Singh:** And thanks for sharing that information with me.

**Mohitdeep Singh:** So you.

**Mohitdeep Singh:** Would you have any information on when would be the next round be like?

**Katja Wittfoth:** Yeah, so we don't really have like a set structure of how to interview for those roles because those roles are new.

**Katja Wittfoth:** So we are actually creating the process as we go, but you will hear from Taka next, probably within, you know, I'm not sure how fast he is, but he seems to be very fast.

**Katja Wittfoth:** So today or in a few days, and then we will go from there. Most likely you'll meet some other team members and maybe some sort of take-home assignment.

**Katja Wittfoth:** Thank you for sharing. That was a pleasure to meet you and thanks for taking the time to interview.

**Mohitdeep Singh:** Well, thank you so much. That was great. And you'll hear back from Taka soon.

**Katja Wittfoth:** Thanks, Katja.

**Mohitdeep Singh:** Bye.
