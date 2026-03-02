# Manuel Alejandro Valderrama Florez -Hiring Manager Screen | AI Engineer (Software Engineer, AI and Agent)

<metadata>
date: 2025-11-20
time: 19:01 UTC
duration: 63 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Manuel Alejandro Valderrama
fathom_recording_id: 103268384
fathom_url: https://fathom.video/calls/480689206
share_url: https://fathom.video/share/vNkKy1awx77wWVGCSMzhCggocJVngE_h
source: fathom
enriched_on: 2026-03-02 19:45 UTC
</metadata>

---

## Summary

Daniel Lopes conducted a hiring screen with Manuel Alejandro Valderrama, an ML/MLOps engineer from Colombia, for an AI Engineer role at growthx.ai. Manuel's background spans machine learning infrastructure (Rappi's predictions team, Graphite's content AI tools) and vector database optimization, with demonstrated expertise in cost-effective inference scaling that aligns closely with growthx.ai's agent-based content pipeline. Both discussed how growthx.ai's output-based culture and flexible remote work environment address Manuel's values around balancing engineering challenges with family responsibilities.

---

## Context

Manuel Alejandro Valderrama is a systems-minded ML engineer based in Colombia. He brings 5+ years of production ML experience, starting with industrial IoT at Omnicon, moving to agricultural ML at CIAT, and scaling to production systems at Rappi (Mercado Libre's logistics platform, ~80-person team). Most recently, he spent three years at Graphite (2022–2025), an SEO content SaaS startup, where he built internal ML tools for writers. He was part of a nine-person team laid off when Graphite shut down its SaaS vertical to focus on its premium human-written content service—a decision Manuel disagrees with, believing AI-assisted content is the market's future. This conversation is a hiring screen for growthx.ai's AI Engineer role.

---

## Relevance

**To GrowthX Hiring & Team Building:**
- Manuel's production MLOps background (feature/vector stores, inference scaling, observability tools at Rappi) directly addresses growthx.ai's infrastructure needs for deploying agents at scale.
- His vector database work (Pinecone → PgVector migration, PCA-based dimensionality reduction, half-precision quantization for 50% cost reduction) is immediately applicable to growthx.ai's content embedding and retrieval pipeline.
- Cultural fit around output-based work and remote flexibility resonates with his values (managing family, needing flexibility for unexpected events). Company has 60%+ of engineers with 0–2 year-old children due to COVID-era hiring.

**To GrowthX Product & Agent Strategy:**
- Manuel's agentic writer POC at Graphite (shelved due to Graphite's philosophy of human-only writing) proves he understands and values automated content generation—the core of growthx.ai's product direction.
- He's built multi-LLM routing (Gemini, Perplexity comparison) and LLM-as-judge scoring systems, both relevant to content quality evaluation and model selection at scale.
- His brief automation tool (scraped competitor content for SEO briefs) shows knowledge of competitive content analysis, a key input to growthx.ai's content pipeline.

**To GrowthX Business Development:**
- Manuel's experience productionizing ML at Rappi (80-person logistics company) and Graphite (SEO SaaS) provides perspective on ML cost-benefit tradeoffs in B2B services, valuable for positioning growthx.ai's agent-assisted model to cost-conscious clients.
- His view that SaaS-only products won't work long-term (Graphite's failure mode) and that services + software hybrid models are the path forward aligns with growthx.ai's service-first strategy.

---

## Overview

- **Strong MLOps Background:** Manuel has deep experience productionizing ML models (Rappi), building feature/vector stores, and optimizing inference.
- **Vector DB Optimization:** At Graphite, he replaced Pinecone with PgVector for its multi-query efficiency, then cut AWS disk costs by reducing vector size (PCA) and precision (half-precision).
- **Strategic Alignment:** Manuel's vision for AI-driven content (automating drafts for human editors) aligns with growthx.ai's agent-based pipeline, contrasting with Graphite's "human-only" writing philosophy.
- **Flexible Culture Fit:** Manuel confirmed growthx.ai's output-based culture, which offers the flexibility he values for managing personal commitments like family.

---

## Key Topics

### growthx.ai: Context & Vision

  - **Company:** \~80 people; 15-person engineering team.
  - **Origin:** Grew from a marketing agency using AI tools to an internal product team building its own SaaS.
  - **Product Vision:** An agent-based content pipeline that automates first drafts, enabling human editors to focus on strategy and refinement.
  - **Market View:** AI search (Gemini) will increase demand for high-volume, constantly updated content, making websites "content production machines."

### Candidate Background: Manuel Valderrama

  - **Education:** Electronic Engineering (B.S.), Computer Science (M.S.).
  - **Experience:**
      - **Omnicon:** PLC programming, industrial IoT (ML for machine failure prediction).
      - **CIAT:** Research on image-based crop yield prediction (drones, satellites).
      - **Rappi:** MLOps engineer for the "predictions team."
          - **Role:** Productionize ML models, build microservices, create observability tools.
          - **Projects:** Built a vector/feature store (Snowflake) to predict delivery times.
      - **Graphite:** ML Engineer (2022–2025).
          - **Focus:** Building internal SaaS tools for content writers.
          - **Layoff:** Part of a team of 9 laid off when Graphite killed its SaaS vertical.

### Key Project: Vector Database Optimization at Graphite

  - **Goal:** Group Google topics (keywords) by intent using SERP titles.
  - **Initial Challenge (Pinecone):** Inefficient for multi-query requests needed to find a topic and its neighbors simultaneously.
  - **Solution 1 (PgVector):** Replaced Pinecone for its multi-query efficiency.
  - **Solution 2 (Cost Reduction):** Addressed high AWS disk costs from large embeddings.
      - **PCA:** Reduced vector dimensionality.
      - **Half-Precision:** Migrated to 16-bit vectors, cutting index size by 50%.
      - **Binary Embeddings:** POC showed good results but required a full database rebuild.
  - **Unsuccessful Attempt:** An HNSW index failed to build due to complex hyperparameter tuning.

### Other Graphite Projects

  - **Brief Automation Tool:** Scraped competitor content to generate SEO briefs, questions, and answers for writers.
  - **Multi-LLM Routing:** Used multiple models (Gemini, Perplexity) to provide writers with diverse perspectives for comparison.
  - **LLM-as-a-Judge:** Used an LLM to classify topic quality (binary score), helping filter bad keywords and correct misspellings.
  - **Agentic Writer POC:** A proof-of-concept for automated long-form content was shelved due to Graphite's "premium human content" philosophy.

---

## Action Items

- **Daniel Lopes (GrowthX):** Discuss Manuel's candidacy with Tucker (likely Tucker Lumpkin, hiring lead).
- **Tucker:** Follow up with Manuel Alejandro Valderrama regarding next steps in the hiring process.

---

## Transcript
**Daniel Lopes:** This meeting is being recorded.

**Daniel Lopes:** Can you hear me?

**Manuel Alejandro Valderrama:** Do you go by?

**Daniel Lopes:** Can you hear me?

**Manuel Alejandro Valderrama:** Yeah, yeah, I can hear you.

**Daniel Lopes:** Nice.

**Daniel Lopes:** Sorry, I'm a couple of minutes late.

**Daniel Lopes:** I'm setting up my space here.

**Manuel Alejandro Valderrama:** No worries.

**Daniel Lopes:** Do you go by Alejandro or Manuel?

**Manuel Alejandro Valderrama:** I don't have a preference.

**Manuel Alejandro Valderrama:** Whatever you'd like to do.

**Manuel Alejandro Valderrama:** Manuel is okay.

**Daniel Lopes:** Sounds good.

**Daniel Lopes:** Where are you based?

**Manuel Alejandro Valderrama:** I'm in Colombia.

**Daniel Lopes:** Oh, nice.

**Daniel Lopes:** I'm from Brazil.

**Daniel Lopes:** So we're American.

**Manuel Alejandro Valderrama:** Nice.

**Daniel Lopes:** Super.

**Daniel Lopes:** Thanks for taking the time.

**Daniel Lopes:** Thanks for applying.

**Daniel Lopes:** Super excited to chat with you.

**Daniel Lopes:** I was just reviewing the resume right before the call.

**Daniel Lopes:** I didn't have a chance.

**Daniel Lopes:** chance.

**Daniel Lopes:** I

**Daniel Lopes:** We to chat with Tucker, but I think we have a lot of interesting things in common, I think, that we worked on similar problems.

**Daniel Lopes:** So it would be cool to get your background and see how you could help us.

**Daniel Lopes:** But today, maybe we could just, I can give you a bit of my background and a little bit of growthx first, and then maybe you could do the same.

**Daniel Lopes:** And then we spend 10, 15 minutes going briefly through your past experience.

**Daniel Lopes:** And then I have a bunch of general questions about the kind of stuff that we're building that I think you might have overlapped with some of those two.

**Daniel Lopes:** So it would be nice to get your experience in that.

**Daniel Lopes:** I know we want to have like 45 minutes, but probably we can cover it a lot.

**Daniel Lopes:** But if that makes sense.

**Daniel Lopes:** Yeah, so my...

**Daniel Lopes:** Just like, yeah, so I can't start with my background.

**Daniel Lopes:** So my background, like I've been a programmer for 25 years. Started when I was 15.

**Daniel Lopes:** I don't know if you guys in Colombia have the same technical high school or like vocational schools in parallel with normal schools.

**Daniel Lopes:** That's super popular in Brazil.

**Daniel Lopes:** So I did computer science in high school and then did it again in college.

**Daniel Lopes:** So high school started working at 15 because you have to get your internship done and ended up getting a job full-time at the same time.

**Daniel Lopes:** So then started doing desktop apps and then switching to web in 2005-ish.

**Daniel Lopes:** Did a lot of Rails stuff for like a long time.

**Daniel Lopes:** still do a big chunk of our background, back end is still Rails.

**Daniel Lopes:** But I was pretty active in the Rails community in Brazil, helped teach a bunch of people, ended up moving to Chicago.

**Daniel Lopes:** We worked for one of the companies under the folks that created Rails.

**Daniel Lopes:** And then after that, moved to the Bay Area, joined as a product engineer in a company called IFT, like if this, then that, like a Zapier precursor.

**Daniel Lopes:** And then I switched to lead the product team there.

**Daniel Lopes:** So I was head of product there for a bit.

**Daniel Lopes:** And then I took over one product from Basecamp that was spinning off and ran that first last seven.

**Daniel Lopes:** And then last year, I was taking a sabbatical to study as much as possible about prompt engineering, accuracy on like things, using things like regs and AI agents.

**Daniel Lopes:** Before we could call them agents, it was mostly chaining and looping things and seeing if something good comes out of it.

**Daniel Lopes:** And before tool calling was even a thing.

**Daniel Lopes:** And that was actually part of my last feature that I built under my previous company as well, was building our chatbot like three years ago.

**Daniel Lopes:** And then I took a sub-article, spent a ton of time reading a ton of papers about prompt engineering, context engineering, that kind of stuff.

**Daniel Lopes:** And at that same time, I met Marcel.

**Daniel Lopes:** Marcel was my co-founder.

**Daniel Lopes:** He was CMO at HashiCorp, and the last one was DeepGram.

**Daniel Lopes:** And DeepGram is like a text-to-speech, speech-to-text API.

**Daniel Lopes:** And he was doing very similar stuff that I was doing.

**Daniel Lopes:** He was essentially just interested in, like, how can I use AI as much as possible in content marketing?

**Daniel Lopes:** Or in marketing, general, to make DeepGram more effective.

**Daniel Lopes:** And he was trying to, he was pretty effective at doing that at DeepGram, and he started, like, talking about it.

**Daniel Lopes:** And that kind of took off.

**Daniel Lopes:** Oh, sorry.

**Daniel Lopes:** But that kind of took off on LinkedIn.

**Daniel Lopes:** So he started trying to teach people with workshops, but, like, all the companies, everybody was joining.

**Daniel Lopes:** There's two companies.

**Daniel Lopes:** can't do it.

**Daniel Lopes:** Can you do that for us?

**Daniel Lopes:** But I essentially started doing, he started doing that as a service on top of it.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Existing tools.

**Daniel Lopes:** There was a bunch of things like Airtable, NAN, and Air Ops, and some other things.

**Daniel Lopes:** And as the company grew, I joined him when we had 10 clients in September last year.

**Daniel Lopes:** And we ended up, the volume was pretty high already.

**Daniel Lopes:** So I ended up moving a bunch of stuff out of the existing tools and started building some of our in-house tools.

**Daniel Lopes:** And a lot of the stuff that we have today is essentially products that we expect to launch next year.

**Daniel Lopes:** But it's been powering the internal team.

**Daniel Lopes:** And that's kind of the backstory.

**Daniel Lopes:** We're about, we're engineering teams, 15 people?

**Daniel Lopes:** 15?

**Daniel Lopes:** Yeah, 15.

**Daniel Lopes:** All right.

**Daniel Lopes:** And content team is, the whole company is about 80 people, but the product team, it's 15 people.

**Daniel Lopes:** So that's kind of the background.

**Daniel Lopes:** I'd love to hear your backstory and how you ended up here.

**Manuel Alejandro Valderrama:** That's a good story.

**Manuel Alejandro Valderrama:** Well, before you read this on my resume, but I'm an electronic engineer, probably not too much related to software, but yeah, I was doing some software.

**Manuel Alejandro Valderrama:** I think back in the university.

**Manuel Alejandro Valderrama:** Then I take a master's degree in computer sciences.

**Manuel Alejandro Valderrama:** That's basically my education.

**Manuel Alejandro Valderrama:** But well, right after that, I joined the industry, but not the software industry.

**Manuel Alejandro Valderrama:** I started programming PLCs.

**Manuel Alejandro Valderrama:** Yeah.

**Manuel Alejandro Valderrama:** That was...

**Manuel Alejandro Valderrama:** That's kind of weird.

**Manuel Alejandro Valderrama:** It's kind of different to program Python or something.

**Manuel Alejandro Valderrama:** Probably you read about how the PLCs work.

**Manuel Alejandro Valderrama:** But yeah, that was interesting.

**Manuel Alejandro Valderrama:** Then I joined the IoT team in that company.

**Manuel Alejandro Valderrama:** So I started doing some industrial Internet of Things programming.

**Manuel Alejandro Valderrama:** Basically to estimate production in the machines, vibrations, stuff like that.

**Manuel Alejandro Valderrama:** Try to do some basic machine learning for that time to determine some specific variables or predict them, failures and stuff like that.

**Manuel Alejandro Valderrama:** Then I moved to the research industry.

**Daniel Lopes:** was an Omnicon?

**Manuel Alejandro Valderrama:** Oh, the Omnicon.

**Manuel Alejandro Valderrama:** That's a company here in Colombia.

**Manuel Alejandro Valderrama:** Then I joined the research industry.

**Manuel Alejandro Valderrama:** That's CIIT.

**Manuel Alejandro Valderrama:** That's part of CGRID.

**Manuel Alejandro Valderrama:** That's a big research conglomerate that covers a lot of research centers around the world.

**Manuel Alejandro Valderrama:** Here in Colombia, basically, I was doing some research.

**Manuel Alejandro Valderrama:** We used camera drones, multispectral images, satellite images.

**Manuel Alejandro Valderrama:** That was a good time, actually.

**Manuel Alejandro Valderrama:** Absolutely.

**Manuel Alejandro Valderrama:** And we ended up using all that information to predict yields from some, for cassava, I forgot the name of that.

**Manuel Alejandro Valderrama:** Well,

**Manuel Alejandro Valderrama:** From these farmers, you know, the idea was to predict the yield.

**Daniel Lopes:** So it's farming, so it's like image-based satellite data for farming prediction.

**Manuel Alejandro Valderrama:** Yeah, yeah, yeah.

**Manuel Alejandro Valderrama:** We used machine learning to predict that with the multispectral drones that was equipped with these special cameras.

**Manuel Alejandro Valderrama:** We calculated these different vegetation indexes with the field information.

**Manuel Alejandro Valderrama:** We tried to predict that and predict illnesses and stuff like that.

**Manuel Alejandro Valderrama:** I actually have a paper about that.

**Manuel Alejandro Valderrama:** Yeah, we tried to predict cassava production with different species of cassava using these images.

**Manuel Alejandro Valderrama:** That was nice.

**Manuel Alejandro Valderrama:** Then we moved to Rappi, where we usually heard about them.

**Manuel Alejandro Valderrama:** Okay.

**Daniel Lopes:** So was that connected to the university?

**Daniel Lopes:** How did you go from, because, like, in your resume, you have, like, some time at, like, as machine learning engineer, and it's all in the same city, right?

**Daniel Lopes:** So it's, like, machine learning engineer for the university, Avediana College?

**Manuel Alejandro Valderrama:** Oh, yeah, yeah, yeah, yeah, yeah, yeah.

**Manuel Alejandro Valderrama:** Well, actually, while I was doing my master's degree, I was doing, yeah, I was working with them.

**Manuel Alejandro Valderrama:** Yeah, I was doing some machine learning with Internet of Things.

**Manuel Alejandro Valderrama:** We actually built a really simple model to predict flooding in some rivers.

**Manuel Alejandro Valderrama:** We used the sensors in field just to predict that.

**Manuel Alejandro Valderrama:** That was actually my master's degrees.

**Manuel Alejandro Valderrama:** But the interesting thing that I was using FPGA to build their neural network data.

**Manuel Alejandro Valderrama:** Predicted the footing.

**Manuel Alejandro Valderrama:** That was interesting.

**Manuel Alejandro Valderrama:** But yeah, that was like 10 years ago.

**Manuel Alejandro Valderrama:** Oh yeah, 2016.

**Daniel Lopes:** 2016 feels not so long ago.

**Manuel Alejandro Valderrama:** Yeah, compared with the experience, it's not that a lot.

**Manuel Alejandro Valderrama:** Well, then I joined Rappi here in Colombia.

**Manuel Alejandro Valderrama:** I was working for the team, for the predictions team.

**Manuel Alejandro Valderrama:** Basically, I was in charge of predictionizing their machine learning models.

**Manuel Alejandro Valderrama:** I was not the one that created the models.

**Manuel Alejandro Valderrama:** I was the one that productionized and built the microservices, optimized the code.

**Manuel Alejandro Valderrama:** I was in charge of monitoring, built the tools, the observability tools.

**Manuel Alejandro Valderrama:** Also, I was in charge to create a vector and feature store.

**Manuel Alejandro Valderrama:** For them, that was a really nice time.

**Manuel Alejandro Valderrama:** I spent there like two years or so.

**Manuel Alejandro Valderrama:** And then I joined Graphite.

**Daniel Lopes:** Walk me through the transition here, because you have such an interesting background.

**Daniel Lopes:** Because at CIT, you were doing both some of the research stuff, but you're also working on product.

**Manuel Alejandro Valderrama:** that right?

**Manuel Alejandro Valderrama:** you have like your pass application.

**Manuel Alejandro Valderrama:** Yeah, yeah.

**Manuel Alejandro Valderrama:** Well, the idea of the main researcher was to create a platform, a self-service platform that the researchers uploads their satellite or drone imagery.

**Manuel Alejandro Valderrama:** And then we analyzed then we we analyzed it for them.

**Manuel Alejandro Valderrama:** And give them the analysis, probably something like a report or stuff like that.

**Manuel Alejandro Valderrama:** We ended up building a first version before COVID, in which we upload the Orthomosaic images.

**Manuel Alejandro Valderrama:** Basically, the Orthomosaic is a combination of multiple single photos, and you can create a single big image.

**Manuel Alejandro Valderrama:** Even you can calculate the 3D height of the terrain and stuff like that.

**Manuel Alejandro Valderrama:** It's a pretty interesting thing.

**Manuel Alejandro Valderrama:** Yeah, we created this service for the researchers.

**Manuel Alejandro Valderrama:** I productionized that there.

**Manuel Alejandro Valderrama:** Then I moved to Rappi.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Got it.

**Daniel Lopes:** So that, you were like, what's the tech stack that you're using for?

**Daniel Lopes:** So you're like, Python?

**Manuel Alejandro Valderrama:** Oh, yeah, Python, Python, yeah.

**Daniel Lopes:** Mostly Python, yeah.

**Daniel Lopes:** What did you guys use for, like, the front-end and, like, the web, as as, like, Django, or, like, React, or, like, what was the, or FastAPI, or whatever?

**Manuel Alejandro Valderrama:** Or for the C80s server was React, back then.

**Manuel Alejandro Valderrama:** Yeah.

**Daniel Lopes:** Makes sense.

**Manuel Alejandro Valderrama:** Yeah, for the back-end, for the back-end was Flask.

**Daniel Lopes:** Flask.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** And then, and then, then you joined Rappi.

**Manuel Alejandro Valderrama:** What did they do?

**Daniel Lopes:** Can you give me the context?

**Manuel Alejandro Valderrama:** Yeah, I was, I was telling you that, it was the one that productionized the models and, and optimized that.

**Manuel Alejandro Valderrama:** And we, we, we use Python there, also.

**Manuel Alejandro Valderrama:** The, I, I don't know, I don't know what else to say.

**Manuel Alejandro Valderrama:** I I, they, they say, but, but.

**Manuel Alejandro Valderrama:** Yeah, it was there for like two years.

**Daniel Lopes:** That's another thing that we were thinking about, like feature stores and optimization of inference.

**Daniel Lopes:** Like some of stuff that you have listed here are some of the things that we're probably going to hit soon.

**Daniel Lopes:** But here is just like what was the experience there?

**Daniel Lopes:** What was your, like you were in charge of like the whole machine learning, engineering, and executing while another person was building the model.

**Manuel Alejandro Valderrama:** So like you're interacting pretty, probably pretty close with the person figuring out the features.

**Manuel Alejandro Valderrama:** Yeah, another person was in charge to build the model, to test the model, to, before going to production.

**Manuel Alejandro Valderrama:** I was the one that in charge of production, had the greatest service itself, the maintain the, the, the, the dependencies, the observability.

**Manuel Alejandro Valderrama:** And all this stuff related.

**Manuel Alejandro Valderrama:** As I said, it was the one that was in charge of creating the feature store.

**Manuel Alejandro Valderrama:** Basically, we had Snowflake back then in Rappi.

**Manuel Alejandro Valderrama:** The idea was to extract these features that our data scientists in our team, because they had multiple small teams.

**Manuel Alejandro Valderrama:** Rappi is pretty big, and each squad had its own interests.

**Manuel Alejandro Valderrama:** And the team that I was working on, basically, our objective was to predict when the product was ordered in the app, when it will be.

**Manuel Alejandro Valderrama:** In the door of the customer.

**Manuel Alejandro Valderrama:** So we were the predictions team, if I remember correctly.

**Manuel Alejandro Valderrama:** Yeah, we extracted these features that the data scientists really need.

**Manuel Alejandro Valderrama:** We filtered them and we made them available to be consumed for them, as well for the model store, which we versioned the models that they were building over the time.

**Manuel Alejandro Valderrama:** I was in charge of all of that.

**Manuel Alejandro Valderrama:** Of course, in the monitoring of all that, if something was down, we were the first to be in the front line just to be taken to in charge of repair.

**Daniel Lopes:** Got it.

**Daniel Lopes:** What was the team structure?

**Daniel Lopes:** Was it you as a machine learning engineer on this squad?

**Manuel Alejandro Valderrama:** And then a data scientist?

**Manuel Alejandro Valderrama:** Yeah.

**Manuel Alejandro Valderrama:** That's it?

**Manuel Alejandro Valderrama:** I was a machine learning engineer.

**Manuel Alejandro Valderrama:** We had two data scientists.

**Manuel Alejandro Valderrama:** There were operational analysts, I think, that was, I don't remember correctly, it was, that was in charge of, of analyzing the operation and try to, to optimize the, the, the best paths.

**Manuel Alejandro Valderrama:** And they, they were, they were more like industrial engineers.

**Manuel Alejandro Valderrama:** Yeah.

**Manuel Alejandro Valderrama:** That makes sense.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And then, and then, so that was like four-ish years ago, and then you joined Graphite, right?

**Manuel Alejandro Valderrama:** So Graphite.

**Daniel Lopes:** Uh-huh.

**Manuel Alejandro Valderrama:** Graphite.

**Daniel Lopes:** Give me a little bit of, like, I'm, I'm, I've heard of them and like, I've, I listened to a one interview from, I think it's evening, That's kind fun.

**Daniel Lopes:** Yeah.

**Manuel Alejandro Valderrama:** Ethan Smith.

**Manuel Alejandro Valderrama:** Ethan Smith.

**Daniel Lopes:** Yeah.

**Manuel Alejandro Valderrama:** Ethan Smith.

**Manuel Alejandro Valderrama:** Ethan Smith's podcast.

**Daniel Lopes:** Yeah, right, right, right.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So that's the one that I watch.

**Daniel Lopes:** That's as much context as I have about what you guys are doing there.

**Daniel Lopes:** And I was just checking the website right before the call.

**Daniel Lopes:** So you guys, so you joined four years ago as a machine learning engineer already?

**Manuel Alejandro Valderrama:** Yeah.

**Manuel Alejandro Valderrama:** Yeah, was a machine learning engineer.

**Daniel Lopes:** So that's, like, that's right when, like, that GPT was, that's, like, that's 2021, is that right?

**Daniel Lopes:** 2022.

**Manuel Alejandro Valderrama:** Okay.

**Manuel Alejandro Valderrama:** Two, two.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** What did you have here?

**Daniel Lopes:** Yeah, go ahead.

**Manuel Alejandro Valderrama:** Sorry.

**Manuel Alejandro Valderrama:** I started, I started with them.

**Manuel Alejandro Valderrama:** GPT was not the thing back then.

**Daniel Lopes:** Mm-hmm.

**Manuel Alejandro Valderrama:** Uh, we, we were working with, uh, classical machine learning techniques.

**Daniel Lopes:** Thanks.

**Daniel Lopes:** Hey.

**Manuel Alejandro Valderrama:** NLP stuff, just to predict the text and stuff like that.

**Manuel Alejandro Valderrama:** For example, we had a pretty good model that predicts the website type based on the URL and the content and basically tell us, oh, okay, this website is a product page or an article page, and that was one of the models that we used for that.

**Manuel Alejandro Valderrama:** There were other models.

**Daniel Lopes:** Like a categorization based on the content type of the page or an entire website?

**Manuel Alejandro Valderrama:** Based on the content type.

**Manuel Alejandro Valderrama:** I was actually working on a new version of that a few months ago.

**Manuel Alejandro Valderrama:** I was trying to use BERT just to try to classify better.

**Manuel Alejandro Valderrama:** Because we started to notice the model was drifting a little bit, the model was trained a long time ago, and this stuff changed a lot, and then we noticed that.

**Manuel Alejandro Valderrama:** But that not worked for some reason, and we started noticing the model that we used back then was out of support.

**Manuel Alejandro Valderrama:** We were using an older framework, so we tried to migrate that to newer technology. We ended up using PyTorch. I wasn't in charge of the migration to PyTorch—I was trying to do something different—but we ended up using PyTorch, basically the same logic as before, but with PyTorch to get rid of all the old dependencies.

**Manuel Alejandro Valderrama:** And then the new thing working, and then try to, in the future, modernize the thing and then try to train a new model and reduce the drift.

**Manuel Alejandro Valderrama:** But sadly, that didn't happen.

**Manuel Alejandro Valderrama:** Sadly.

**Manuel Alejandro Valderrama:** Well, most recently, we started, we noticed we needed a vector database just to group our topics, Google topics, using the titles.

**Manuel Alejandro Valderrama:** But the challenge was, try to get the whole topics database into the current infrastructure, right?

**Manuel Alejandro Valderrama:** We didn't watch.

**Manuel Alejandro Valderrama:** And to pay an external provider like PineCon, we actually tried PineCon, but for our needs, that wasn't super efficient.

**Manuel Alejandro Valderrama:** We actually had the...

**Manuel Alejandro Valderrama:** Why not?

**Daniel Lopes:** Are you guys focused more on the cost or on the...

**Daniel Lopes:** No, Was not returning the right results?

**Manuel Alejandro Valderrama:** No, it actually worked very well.

**Manuel Alejandro Valderrama:** But the thing was, we were doing multiple queries for multiple topics at the same time.

**Manuel Alejandro Valderrama:** Back then, the PineCon query wasn't working like that.

**Manuel Alejandro Valderrama:** We were able to make concurrent calls to the API, but not call multiple queries at the same time, with the same call.

**Daniel Lopes:** I've dealt with this kind of problem multiple times in the past, both at my previous job and here as well.

**Daniel Lopes:** What kind of content are you guys storing and what was the decision around how did you do your embeddings, how did you do the chunking, that kind of stuff?

**Manuel Alejandro Valderrama:** I was interested in the different approaches everybody takes.

**Manuel Alejandro Valderrama:** Our approach was really simple.

**Manuel Alejandro Valderrama:** We had the topic, the Google topic, and we had the titles for each, the first 10 titles, 20 titles, whatever you want.

**Daniel Lopes:** And we ended up...

**Daniel Lopes:** When you say topic, that would be like the keywords that...

**Manuel Alejandro Valderrama:** Oh, yeah, yeah, yeah, We had...

**Manuel Alejandro Valderrama:** I'm sorry, I'm sorry.

**Manuel Alejandro Valderrama:** That's the graphite thing.

**Manuel Alejandro Valderrama:** We call the keyword, the Google keyword, topic, because you are looking for this topic.

**Manuel Alejandro Valderrama:** Then, yeah, we had this keyword, and then the titles of each, the result, the result page, the title, right?

**Manuel Alejandro Valderrama:** And the idea was to embed the titles.

**Daniel Lopes:** The titles, okay.

**Daniel Lopes:** So they're very short.

**Daniel Lopes:** There's no one that can need to, okay.

**Manuel Alejandro Valderrama:** The idea was to embed the titles, then get the average of the titles.

**Manuel Alejandro Valderrama:** So were you embedding the title and the description, or just the title?

**Manuel Alejandro Valderrama:** I'm assuming there would be a SERP, and then you get the results.

**Manuel Alejandro Valderrama:** Just the title, just the title.

**Daniel Lopes:** Okay.

**Manuel Alejandro Valderrama:** Just the title.

**Manuel Alejandro Valderrama:** That's it.

**Manuel Alejandro Valderrama:** So the idea behind that was to, the titles will, or should, will give you a pretty good idea what the intention of that keyword is.

**Daniel Lopes:** It's my mistake, intent.

**Daniel Lopes:** Okay, that's it.

**Daniel Lopes:** So the challenge of Pinecon is that you guys had, like, one keyword that would generate, like, 200 titles on the SERP result, and then you have to, like, call all of those in parallel?

**Manuel Alejandro Valderrama:** No, no, no, no, no, no.

**Manuel Alejandro Valderrama:** Because we had these embeddings.

**Manuel Alejandro Valderrama:** We uploaded them to Pinecon.

**Manuel Alejandro Valderrama:** But, for example, if you were looking for a specific topic, you tried to find a similarity, which are the related topics to this.

**Manuel Alejandro Valderrama:** So this will give you a myriad of results.

**Manuel Alejandro Valderrama:** But probably you don't need only one.

**Manuel Alejandro Valderrama:** Probably you need the vicinity of this main topic and try to get the holograph, right?

**Manuel Alejandro Valderrama:** The problem was...

**Manuel Alejandro Valderrama:** You can't call the main topic or the central topic and their vicinity at the same time, but you need to do and request to the Pinecone API.

**Manuel Alejandro Valderrama:** That was costly and inefficient in our opinion.

**Manuel Alejandro Valderrama:** So that's why we didn't get into Pinecone back then.

**Daniel Lopes:** What do you guys end up using with VectorDatabase now?

**Manuel Alejandro Valderrama:** PgVector.

**Daniel Lopes:** PgVector, okay.

**Manuel Alejandro Valderrama:** That was super efficient in my opinion, but there was another challenge that came with using PgVector.

**Manuel Alejandro Valderrama:** PgVector was really nice because you can, with a single query, you can get multiple neighbors of these topics at the same time, group by whatever you want, et cetera. It's more efficient than Pinecone, but there was another challenge that came with using PgVector.

**Manuel Alejandro Valderrama:** The thing was the size, the disk size, you know, because these embeddings are pretty large, so we noticed that it was costing a lot.

**Manuel Alejandro Valderrama:** And so my job, or no, that's not the word, my task was to reduce that.

**Daniel Lopes:** And how did you go about that?

**Daniel Lopes:** Do you guys just like AWS, or is it something else for the posters?

**Manuel Alejandro Valderrama:** Yeah, using AWS, yeah.

**Manuel Alejandro Valderrama:** Yeah, that was really costly because of the disk size, and we had two environments, the staging and production, and we also had...

**Manuel Alejandro Valderrama:** Dev environments to test the features, so that was getting really, really costly for the company.

**Manuel Alejandro Valderrama:** So we decided to shrink that.

**Manuel Alejandro Valderrama:** That's why we decided to do a reduction in the vectors, just to save some disk size.

**Manuel Alejandro Valderrama:** With a PCM, you know, this was a really good solution.

**Manuel Alejandro Valderrama:** We did these figures that just tried to find the right balance between the vector size and the accuracy of each of the queries based on the index, because that was another variable to take into account, the index that we were using.

**Manuel Alejandro Valderrama:** Integer embeddings, binary embeddings, 16-bit half-precision embeddings, and stuff like that.

**Manuel Alejandro Valderrama:** The first version, basically, we did this PCN reduction that was not enough because the index was huge in size.

**Manuel Alejandro Valderrama:** So, we migrated to the second version of that was to our half-precision vectors, the index was cut in half, that was pretty nice.

**Manuel Alejandro Valderrama:** I was trying to, I think that was the last version, reducing the embeddings and also the index.

**Manuel Alejandro Valderrama:** I tried to implement different indexes, like HNSW index, which in paper was more efficient, more better.

**Manuel Alejandro Valderrama:** We curious in something that was in paper, but in practice, that didn't work.

**Manuel Alejandro Valderrama:** I don't know why.

**Manuel Alejandro Valderrama:** I think the index was huge.

**Manuel Alejandro Valderrama:** It required a lot of hyperparameter tuning just to work well and the index would never finish building.

**Manuel Alejandro Valderrama:** So that was a problem.

**Manuel Alejandro Valderrama:** So that's why I even offered binary embeddings.

**Manuel Alejandro Valderrama:** I added a proof of concept with a small version of the database and transformed these embeddings to binary and got pretty good results, actually.

**Daniel Lopes:** But the thing was we need to rebuild the entire...

**Daniel Lopes:** Index.

**Manuel Alejandro Valderrama:** Index.

**Manuel Alejandro Valderrama:** No.

**Manuel Alejandro Valderrama:** We need to calculate, again, the full database of embeddings, because the thing was, do you need higher, a larger vector dimension just to get similar accuracy compared with that.

**Daniel Lopes:** makes sense.

**Daniel Lopes:** So that was the part that you, like on your resume, that you have the point about the RAG platform.

**Manuel Alejandro Valderrama:** So that was the work that you were doing on the RAG platform?

**Manuel Alejandro Valderrama:** Yeah, that was, that's, that's recent.

**Manuel Alejandro Valderrama:** Yeah, we were, we were doing new, new, new features for the, for the customers, you know, Graphite, Graphite, but basically is, or was, agency part, the software service part, I was working, of course, for the software service.

**Manuel Alejandro Valderrama:** service, and we were building these tools for the, for

**Manuel Alejandro Valderrama:** The writers in the agency, and basically, we were using, we were building this brief automation tool, which basically took the competitors, you put your topic, right?

**Manuel Alejandro Valderrama:** So, it will scrape the web and will show you, okay, these people are writing similar stuff about this topic, and also, the idea was to take this whole thing and create questions about this topic, generate answer engine, generate content, extract the terms from the comparison.

**Manuel Alejandro Valderrama:** And the answer engine content, and that's the whole thing.

**Manuel Alejandro Valderrama:** And then show all that to the writer, just to write better articles.

**Daniel Lopes:** Yeah, we have a similar system.

**Daniel Lopes:** like, you guys, that's the brief, and then what is the RAG part of this?

**Daniel Lopes:** Like, as you do the research, you put in the RAG, and, like, are you guys, like, using Pinecone for that as well?

**Daniel Lopes:** Well, Alex, are you using PG vector for that as well?

**Manuel Alejandro Valderrama:** No, that was basically based on the content itself, just to, we give the topic and the content and generate the questions and the answers for that.

**Manuel Alejandro Valderrama:** But we did this for different or multiple providers.

**Daniel Lopes:** What leads to the team structure you have there?

**Daniel Lopes:** So, like, so they have an agency, like, because I'm not, I'm actually not super familiar.

**Daniel Lopes:** So, they have.

**Daniel Lopes:** Have an agency and they have an internal service software team and the software team service the agency or do you guys serve outside clients on the same platform or do you work directly with the agency only?

**Manuel Alejandro Valderrama:** No, I'm not super familiar with this, but what we were doing was we built these tools for bot, for external clients and our internal clients.

**Manuel Alejandro Valderrama:** Basically, the main tool, we call this platform tool, was this software that was written in Django, the front end, I don't remember, I was not working in the front, sorry.

**Manuel Alejandro Valderrama:** But, but basically, basically...

**Manuel Alejandro Valderrama:** The platform allows the external client that paid for the tool just to get access to these tools and just to get the competitor information, how they are ranking compared with the others and stuff like that.

**Manuel Alejandro Valderrama:** And we'll give you a writing assistant in which the customer, SEO especially, will write the articles based on this.

**Manuel Alejandro Valderrama:** But on the other side were the internal agency tools that basically were the same or lighter version of these tools for the customers or simplified versions in which the internal client will look at.

**Manuel Alejandro Valderrama:** Okay, need this brief, and then they copy the information, and then start writing their own stuff.

**Manuel Alejandro Valderrama:** Yeah.

**Daniel Lopes:** Got it, got it.

**Daniel Lopes:** And then, so, and then you are, what's the structure of your ML AI team?

**Daniel Lopes:** So, like, you are a machine engineer, do you guys, and you just kind of serve these two product teams, sort of, right?

**Daniel Lopes:** So, they will come to you with, like, hey, we need to build, like, a brief generator, or we need to figure out, like, how is your role?

**Daniel Lopes:** And, or, like, are you embedded in the product teams, and, like, doing whatever necessary?

**Daniel Lopes:** My role.

**Daniel Lopes:** Yeah.

**Manuel Alejandro Valderrama:** My, oh, well, well, basically, we had the EA Chief, Greg Druck, probably, did you look at the, he was in, he was in charge of getting the, the...

**Manuel Alejandro Valderrama:** This still version in most cases of the product needs from Ethan and Marcos and the other product team, and they basically give us the task that we needed.

**Manuel Alejandro Valderrama:** So in most cases, I had assigned these necessities requirements, and then they give me the liberty to offer my own solution for that.

**Manuel Alejandro Valderrama:** And for example, the Pinecone to PgVector migration stuff, that was all my work.

**Manuel Alejandro Valderrama:** And yeah, the other part is this product team that probably they will face, oh, I have this problem.

**Manuel Alejandro Valderrama:** If I can.

**Manuel Alejandro Valderrama:** If and I can do something about it, I will take the task and do the stuff, the fix or patch, whatever it needed.

**Manuel Alejandro Valderrama:** If it was required, it was related to something that I was working on, probably I could do something faster, but in some cases, no, but whatever, that was part of the day-to-day.

**Daniel Lopes:** Got it.

**Daniel Lopes:** So like, you also mentioned that you guys did like multi-LLM routing.

**Daniel Lopes:** Can you walk me a little bit like through what was the goal there?

**Manuel Alejandro Valderrama:** Well, that's not...

**Manuel Alejandro Valderrama:** I think that that's about quality, because they said they needed multiple point of views.

**Manuel Alejandro Valderrama:** Regarding the...

**Manuel Alejandro Valderrama:** The answer engine content.

**Manuel Alejandro Valderrama:** So that's something I didn't work too much, but I was using it.

**Manuel Alejandro Valderrama:** I provided some patches on this, but the idea basically was to, okay, you generated this content.

**Manuel Alejandro Valderrama:** How this content compares with Gemini or with Perplexity or Cloud and stuff like that.

**Manuel Alejandro Valderrama:** And then show the writer, okay, these are these terms, for example, generated from Perplexity or Gemini.

**Manuel Alejandro Valderrama:** So in most cases, these terms overlaps.

**Manuel Alejandro Valderrama:** That was one of the use cases.

**Manuel Alejandro Valderrama:** And the other case.

**Manuel Alejandro Valderrama:** This is where, like, the questions, probably the questions about the topic or the keyword were not the same that we use, sorry, that's not what, the question that one provider generates is not the same that the other generates.

**Manuel Alejandro Valderrama:** So we ended up using multiple questions, multiple answers, and stuff like that, and we ended up showing this to the content writer as a, in the screen, just to, basically the writer just had the ability to check which questions were better or not.

**Daniel Lopes:** Got it, and, okay.

**Daniel Lopes:** Like, would, I'm just trying to, so that, so you have.

**Daniel Lopes:** It sounds like those are different needs, but like you have this brief generator that will like come up with the questions and then you also have the assistant for like coming up with better questions.

**Daniel Lopes:** Do you guys, did you ever work on something that would be like drafting a full piece or writing and generating like long form content or that's something that you guys.

**Manuel Alejandro Valderrama:** You mean, you mean, you mean automated content using, using answer engines?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Cause like for like, we have like quite a lot of our stuff is mix of agents that do different things and they are assembled together as like a content pipeline.

**Daniel Lopes:** Yeah.

**Manuel Alejandro Valderrama:** I was working, I was working on something that was a, this was a simple proof of concept, but I think he didn't.

**Manuel Alejandro Valderrama:** But we were working on something that an agentic writer that took the intentional idea of this stuff and writes its own content.

**Manuel Alejandro Valderrama:** But actually the content was not that bad.

**Manuel Alejandro Valderrama:** Probably with more love and time will get better.

**Manuel Alejandro Valderrama:** But the philosophy of Ethan was to give premium content, human content, stuff like that.

**Daniel Lopes:** So that was completely discard.

**Daniel Lopes:** So you guys are more focused on figuring out the topics, figuring out the questions, providing things for the writers to write better.

**Daniel Lopes:** But it's mostly manual, the writing.

**Manuel Alejandro Valderrama:** Yeah, yeah, yeah, yeah, it was, as I was telling you, the idea, or my idea, that was to take all that and automate the thinking.

**Manuel Alejandro Valderrama:** But probably they didn't like it because the writers love their jobs.

**Manuel Alejandro Valderrama:** The thing they sell is premium human content.

**Manuel Alejandro Valderrama:** I think the premium is they think is the word.

**Manuel Alejandro Valderrama:** So they say this is filtered by experts and blah, blah, blah, blah, blah.

**Manuel Alejandro Valderrama:** So no machine in the middle, just in the writing part, no.

**Manuel Alejandro Valderrama:** But probably the tools, the whole content was automatically generated.

**Daniel Lopes:** Got it.

**Daniel Lopes:** So just to make sure you have them, can we go over for like, I have enough, I can have 10 minutes more.

**Daniel Lopes:** like, and I didn't give you enough time to ask any questions or anything.

**Daniel Lopes:** I'm going to make sure you have more time.

**Daniel Lopes:** And I want to, I have a couple of more questions that I want to.

**Manuel Alejandro Valderrama:** Oh, well, well, I found you on the internet.

**Manuel Alejandro Valderrama:** You know, a proper talker told this to you it was laid off.

**Manuel Alejandro Valderrama:** They basically...

**Daniel Lopes:** Oh, I didn't know that.

**Daniel Lopes:** Tucker didn't mention that.

**Daniel Lopes:** So I thought you were still there.

**Manuel Alejandro Valderrama:** No, no, no, no, it was laid off.

**Manuel Alejandro Valderrama:** Oh, well, this is another good story.

**Manuel Alejandro Valderrama:** They killed the SaaS vertical.

**Daniel Lopes:** Oh, wow.

**Daniel Lopes:** I didn't know that.

**Daniel Lopes:** Because I was clicking on the website, I felt it was...

**Daniel Lopes:** Yeah, I couldn't get it clear in a second.

**Manuel Alejandro Valderrama:** Yeah, they did that.

**Manuel Alejandro Valderrama:** They still have a couple of engineers just to maintain probably the few contracts, the running contracts, just to maintain the tool and stuff like that.

**Manuel Alejandro Valderrama:** Yeah, basically, it was laid off because of that with other eight...







**Manuel Alejandro Valderrama:** People, if you have another position, probably can recommend you a good data scientist that I know from there.

**Manuel Alejandro Valderrama:** Well, so I think Ethan believes, or that is what I believe, the software service is not the path to go.

**Manuel Alejandro Valderrama:** What did you think?

**Daniel Lopes:** Yeah, no, like, I think that's, I think we're in an interesting inflection point where, like, to be, like, completely transparent, like, a lot of our stuff is agents interacting with people.

**Daniel Lopes:** So we have a large content writing team, too, but we have a pretty large software service as well, and a lot of what we have is the info to write different agents.

**Daniel Lopes:** So, and it will create custom agents for every client.

**Daniel Lopes:** and it will

**Daniel Lopes:** That will take context documents, will take access to different regs and stuff like this.

**Daniel Lopes:** And it's the writer interacting with the agent that creates the content.

**Daniel Lopes:** So the first draft will be fully automated.

**Daniel Lopes:** The person comes in and removes stuff and stuff like that.

**Manuel Alejandro Valderrama:** That was my b-shirt.

**Daniel Lopes:** Yeah, sounds like it.

**Daniel Lopes:** But in the meantime, it's pretty complex.

**Daniel Lopes:** You're putting together all the things.

**Daniel Lopes:** LLMs are changing all the time.

**Daniel Lopes:** The models are changing all the time.

**Daniel Lopes:** There's quality problems that you have to trace.

**Daniel Lopes:** There's evaluation challenges, like how do you track?

**Daniel Lopes:** What's the definition of good content versus not so good content?

**Daniel Lopes:** How do you measure that?

**Daniel Lopes:** So there's all these challenges that you have to figure out.

**Daniel Lopes:** But I think we're getting to the point where I think that you will require people in a loop.

**Daniel Lopes:** But over time, it be less and less and less.

**Daniel Lopes:** And we'll be more at the strategic level.

**Daniel Lopes:** And they will be choosing the different topics.

**Daniel Lopes:** They will be analyzing the competitors and that kind of stuff.

**Daniel Lopes:** Like gaps that they want to cover for that content creation, maybe the drafting will be like automated and people will like improve it.

**Manuel Alejandro Valderrama:** Like almost like the same way that, I don't know if you use stuff like Cloud Code or if you use something like Cursor or things like that.

**Daniel Lopes:** Yeah, like you still need programmers, but we're not typing everything, you know?

**Manuel Alejandro Valderrama:** Yeah, yeah.

**Daniel Lopes:** But that's how I think like, I think like software as a service might change, but I think it's like, it's very, there will be more services than just software subscription.

**Daniel Lopes:** At least in this period while like AI is like stabilizing, like for example, we have, we changed models like almost every month, you know?

**Daniel Lopes:** Like there's like a new version, okay, like let's try it out.

**Daniel Lopes:** And they all have different flavors, like they all put things better in different areas and worse in different areas.

**Daniel Lopes:** And some stuff, it's faster, some stuff is lower.

**Daniel Lopes:** Sometimes some stuff has actual, actual taste of alterites.

**Daniel Lopes:** Some stuff is actually better at like being more.

**Daniel Lopes:** Spectral and like obeying orders, like they all have different stuff, but the moment that you, I don't know, like they stabilize a little bit and you can use different models for different tasks and you have that surface covered, then I think you can start bringing users more in the traditional SaaS mode.

**Daniel Lopes:** And the meantime, it's changing so fast that even like training our internal team is a challenge, you know?

**Daniel Lopes:** So that's why we have the agency on top so we can eat the complexity and figure out how to do that for the users.

**Daniel Lopes:** And then my expectation is like the next six months to a year, things will be a lot easier to interact with.

**Daniel Lopes:** Like the same way, like last year, if you wanted to program using something like an LLM, you had to like create a bunch of stuff.

**Daniel Lopes:** You had to create like either like a Jupyter notebook for yourself or create a custom GPT, fitted knowledge.

**Daniel Lopes:** Now you have like cloud code and it's pretty close, pretty useful already.

**Daniel Lopes:** At least, like, to me, it's, like, insanely productive product work.

**Daniel Lopes:** And I think that's going to happen in many industries.

**Daniel Lopes:** And content creation, I think it's going to be very similar.

**Daniel Lopes:** But the tooling is not there yet.

**Daniel Lopes:** So we need to build it.

**Manuel Alejandro Valderrama:** That's how I think.

**Manuel Alejandro Valderrama:** Yeah.

**Daniel Lopes:** But maybe I'm wrong, because, like, I'm coming from the product perspective.

**Daniel Lopes:** I've spent my whole life building a product.

**Daniel Lopes:** Maybe Ethan is right.

**Manuel Alejandro Valderrama:** We'll see.

**Manuel Alejandro Valderrama:** But how did you see the growthx with these changes?

**Manuel Alejandro Valderrama:** in AI.

**Manuel Alejandro Valderrama:** I mean, in SEO particularly, I think that's getting pretty complicated.

**Manuel Alejandro Valderrama:** This Gemini is showing you the result in the first page of Google.

**Manuel Alejandro Valderrama:** How do you think this is affecting the market for the products?

**Daniel Lopes:** Like, I think, like, top-of-funnel content?

**Daniel Lopes:** I think.

**Daniel Lopes:** welcome.

**Daniel Lopes:** You're You're

**Daniel Lopes:** Gemini will ingest everything and answer for you.

**Daniel Lopes:** It still needs data to answer it properly because the questions are getting very specific.

**Daniel Lopes:** don't ask just a keyword anymore.

**Daniel Lopes:** They ask a full-blown paragraph or they will have a back and forth.

**Daniel Lopes:** And that has to come from somewhere.

**Daniel Lopes:** And then the other parts, the bottom of the funnel, becomes even more important.

**Daniel Lopes:** So I think the need for a large volume of content just grows.

**Daniel Lopes:** Because you need to like, LLMs are also going further away from using their own knowledge to tap into external sources more and more.

**Daniel Lopes:** Like you see like they all now support this.

**Daniel Lopes:** Like six months ago it was only perplexity.

**Daniel Lopes:** Now you see like ChatGPT, by default, web search is turned on and you get like a hundred sources, you know.

**Daniel Lopes:** And so you have to be constantly creating content and updating them on the regular to be relevant.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So I think it turns websites into like content production machines, basically, instead of just write once and maybe apply.

**Daniel Lopes:** You have to be constantly changing it to rank well on an LLM search or on an AI search.

**Manuel Alejandro Valderrama:** So to me, the internet content will be AI content in what?

**Manuel Alejandro Valderrama:** One year?

**Daniel Lopes:** Two years?

**Daniel Lopes:** I think we're essentially changing.

**Daniel Lopes:** I'm not even sure if websites would be the normal way of people interacting with things anymore.

**Daniel Lopes:** But content, for sure, I think will be.

**Manuel Alejandro Valderrama:** like, somebody has to be producing content.

**Manuel Alejandro Valderrama:** ChatGPT has this thing that you can't even play music from the ChatGPT website.

**Manuel Alejandro Valderrama:** That's weird, at least for me.

**Manuel Alejandro Valderrama:** I didn't like that.

**Manuel Alejandro Valderrama:** I prefer the open, like, Spotify app or whatever.

**Manuel Alejandro Valderrama:** I think they're overdoing it a little bit.

**Manuel Alejandro Valderrama:** They're going too far.

**Daniel Lopes:** But quick question.

**Daniel Lopes:** One of the things that we're trying to figure out is evaluations.

**Daniel Lopes:** don't know if you worked with that graphite, but evals, because you did traditional machine learning evals, monitoring model drift and all that.

**Daniel Lopes:** And for us, we want to generate drafts and briefs and stuff like that and have them be as good as possible.

**Daniel Lopes:** And there's always that, what is the definition of a good content?

**Daniel Lopes:** So we were trying to figure out the breakdown of this, like how do you score that and how do you monitor the output of those things?

**Daniel Lopes:** I have no, no, like, this is not like a whiteboard or anything kind of question.

**Daniel Lopes:** It's just more like, how do you think about that and how would you, if you were in charge of figuring out our evals for content quality?

**Manuel Alejandro Valderrama:** Well, I was not in charge of content quality, but I was in charge of...



**Manuel Alejandro Valderrama:** It evaluated the topics quality, right?

**Manuel Alejandro Valderrama:** So, you know, there probably be good topics and bad topics.

**Manuel Alejandro Valderrama:** And we ended up using LLMs just to classify the good topics, intentions, or not, you know, all this.

**Daniel Lopes:** So that helped us to...

**Daniel Lopes:** So you had an LLM as a judge for topic quality?

**Daniel Lopes:** Yeah, an LLM as a judge?

**Manuel Alejandro Valderrama:** Yeah, exactly.

**Daniel Lopes:** How did you do the judging?

**Daniel Lopes:** like, how did you do the, your score, like binary scoring, or it was like 0 to 5 score, like Likert scoring, like what was the...

**Manuel Alejandro Valderrama:** Because that's how we also have done that a bit, and then I'm always curious what's the approach here.

**Manuel Alejandro Valderrama:** Well, we thought that the best way was binary score.

**Manuel Alejandro Valderrama:** Yeah, yeah.

**Manuel Alejandro Valderrama:** Probably will not be the better, it was the fastest one just to just to...

**Manuel Alejandro Valderrama:** get Yeah.

**Manuel Alejandro Valderrama:** There were pretty, we got pretty good results on that and we helped us to reduce the disk size, just dumping some bad keywords and even to fix some unintended topics that we had or were bad spelled and stuff like that.

**Daniel Lopes:** What was the definition of bad?

**Daniel Lopes:** Was it based on spelling or is it based on context of the client?

**Daniel Lopes:** Or like, how did you guys set up the prompt for that?

**Manuel Alejandro Valderrama:** We ended up using a mix of our own database and we built this graph with the content.

**Manuel Alejandro Valderrama:** You know, if you, if you have this topic, probably it would be related to some, a certain topic.

**Manuel Alejandro Valderrama:** So, uh, we have seen...

**Manuel Alejandro Valderrama:** I that was the intention of that, for example, a pretty good topic was the Vikings, you know?

**Manuel Alejandro Valderrama:** So if you search for Vikings, probably you will get the people, right?

**Manuel Alejandro Valderrama:** Or the football team.

**Manuel Alejandro Valderrama:** So we used that, we built our vector database just to get the main topic, try to get the neighbors, and try to establish what was the intention.

**Manuel Alejandro Valderrama:** probably if a keyword were in the wrong part of the graph, probably was bad.

**Daniel Lopes:** Got it.

**Daniel Lopes:** So what do you guys use for the graph?

**Manuel Alejandro Valderrama:** Like, did you do just like regular, like, similarities for, or did you use a graph database?

**Manuel Alejandro Valderrama:** Yeah, regular database.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So you didn't have like anything like Neo4j or anything?

**Manuel Alejandro Valderrama:** No, we tried that, but it was slow.

**Manuel Alejandro Valderrama:** So it was faster, dude.

**Manuel Alejandro Valderrama:** Do get the PgVector.

**Daniel Lopes:** Got it.

**Manuel Alejandro Valderrama:** That makes sense.

**Manuel Alejandro Valderrama:** That's something that I tried, yeah.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Okay, like, I don't want to use your whole day, but, like, any other questions for me?

**Daniel Lopes:** What can I answer?

**Manuel Alejandro Valderrama:** No, no.

**Manuel Alejandro Valderrama:** Well, what is your...

**Manuel Alejandro Valderrama:** I mean, I have a kid, you know?

**Manuel Alejandro Valderrama:** I have a two-year-old kid, three-year-old kid, sorry.

**Manuel Alejandro Valderrama:** Kids get sick.

**Manuel Alejandro Valderrama:** So, something that I had at graph, I thought, I'm sorry, my kid is sick, so I need to get to the doctor, stuff like that.

**Manuel Alejandro Valderrama:** How do you handle that?

**Daniel Lopes:** Yeah, life happens, you know?

**Daniel Lopes:** So, to me, like, that's one thing that I always liked about some of my previous jobs, was just, like, flexible.

**Daniel Lopes:** flexible.

**Daniel Lopes:** Yeah, so

**Daniel Lopes:** They're all remote, at least in the last eight years, and not monitoring people hours or like not monitoring days off or anything, guarantee a minimum time off.

**Daniel Lopes:** like a minimum 15 days of time off, but flexible.

**Daniel Lopes:** And like, I'm not monitoring people's day to day, what they, how many hours they are in on Slack.

**Daniel Lopes:** I'm just monitoring like their geek bots, like what they're stand up, what they're working on.

**Daniel Lopes:** And then by the end of the week, I would usually use an MCP bot to like take the digest of what everybody did.

**Daniel Lopes:** And I would do like every other week, do like, I would do a one-on-one with everybody.

**Daniel Lopes:** And we talked about whatever they did, but, and I would keep an eye on linear, but we have folks everywhere.

**Daniel Lopes:** have folks in, in Italy, for example, that I don't overlap much.

**Daniel Lopes:** I have folks in the Bay Area, that's much easier for me to have meetings with them more often.

**Daniel Lopes:** But we have, we don't track, uh, uh, time off when we don't track.

**Daniel Lopes:** Okay.

**Daniel Lopes:** It's just based on output.

**Manuel Alejandro Valderrama:** Oh, that's nice.

**Manuel Alejandro Valderrama:** That's nice.

**Manuel Alejandro Valderrama:** Yeah, I don't...

**Manuel Alejandro Valderrama:** Okay, my kid is not getting A lot of people have kids here as well.

**Daniel Lopes:** So, like, a lot of people have kids.

**Daniel Lopes:** I think, like, probably, like, 60% or, like, even more, the company has two years old.

**Daniel Lopes:** Everybody's in that range.

**Daniel Lopes:** Either zero, like, we have two guys on pet leave now for six weeks.

**Daniel Lopes:** And then all the way to, like, two years old, that is the range.

**Daniel Lopes:** Marcel has a two years old.

**Daniel Lopes:** So, everybody in the engineering, you guys are two years old somehow.

**Daniel Lopes:** I don't know why, but there's the...

**Manuel Alejandro Valderrama:** COVID, COVID, COVID, yeah.

**Daniel Lopes:** COVID, yeah.

**Manuel Alejandro Valderrama:** Yeah, that's the reason.

**Daniel Lopes:** Yeah, that's a good causation for relation there.

**Manuel Alejandro Valderrama:** Yeah, well, what I was trying to say, yeah, my kid is not getting sick, but probably these things happen.

**Manuel Alejandro Valderrama:** So, I really get to know that it's not a problem.

**Manuel Alejandro Valderrama:** Or in case of something happened, you need to go out.

**Manuel Alejandro Valderrama:** And some people don't tolerate that, I guess.

**Manuel Alejandro Valderrama:** So that's what it was.

**Daniel Lopes:** Yeah, no, that's, that's a really, like, we're constantly trying to get better at, like, measuring, not measuring, but, like, communication of context.

**Daniel Lopes:** Like, I think work, and, like, seeing, like, if you tell me, like, oh, today I couldn't work because something happened, and then, but your project is in a good state, like, it doesn't matter, you know, like, it can, like, I got my programmer, like, I don't, I can't produce eight hours straight, I know that.

**Daniel Lopes:** So, like, some days I'm gonna have off days, some days I will work better in the evening, some days I'll work better in the weekend, so, like, sometimes, sometimes I want to take two days off because I can't figure out the solution for this thing, I just want to go do something else.

**Daniel Lopes:** So, like, know,

**Daniel Lopes:** I understand that creative work doesn't happen in like on the schedule, so.

**Manuel Alejandro Valderrama:** Okay, that's good to know.

**Daniel Lopes:** Cool, man.

**Daniel Lopes:** Thanks for your time.

**Daniel Lopes:** I think I covered, I had like always, I always have like a buzz in the questions to ask.

**Daniel Lopes:** I think I could keep going for another two hours, but I don't want to use your entire day.

**Daniel Lopes:** I appreciate your time and I'll follow up with Tucker and he'll follow up with you.

**Manuel Alejandro Valderrama:** Thanks, Daniel.

**Manuel Alejandro Valderrama:** I really appreciate the opportunity to get an interview with you guys.

**Manuel Alejandro Valderrama:** I hope you, we will get in touch soon.

**Manuel Alejandro Valderrama:** You know, you will decide based on our conversation if we're getting, we're moving forward or not.

**Daniel Lopes:** But yeah, thanks.

**Daniel Lopes:** All right.

**Daniel Lopes:** Thank you.

**Manuel Alejandro Valderrama:** Have a good day.

**Manuel Alejandro Valderrama:** See ya.
