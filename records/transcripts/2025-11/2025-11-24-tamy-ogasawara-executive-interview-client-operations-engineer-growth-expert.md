# Tamy Ogasawara -Executive Interview | Client Operations Engineer (Growth Expert)

<metadata>
date: 2025-11-24
time: 19:31 UTC
duration: 75 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Tamyres Ogasawara
fathom_recording_id: 103975278
fathom_url: https://fathom.video/calls/483635870
share_url: https://fathom.video/share/Dx6a5KiZu5srFi6Fp9Gy_szr-_FJdoXR
source: fathom
enriched_on: 2026-03-02 02:45 UTC
</metadata>

---

## Summary

Daniel Lopes conducted an executive interview with Tamyres Ogasawara for the Client Operations Engineer (Growth Expert) role at growthx.ai, a company building an AI workflow engine and Content OS platform. Tamy presented her take-home project—a keyword extraction API with separate markdown prompts for summarization, categorization, keyword extraction, and sentiment analysis—demonstrating strong architectural thinking, prompt engineering discipline, and alignment with growthx.ai's code-first, framework-driven approach. Daniel was highly impressed by Tamy's background (10 years in web/SEO/PM, self-taught AI automation, bootstrapped a BI SaaS), her structured development process using AI tools, and how her project mirrored growthx.ai's internal workflows, and committed to extending an offer after team calibration.

---

## Context

Tamyres Ogasawara is a Brazilian-based engineer and product leader being evaluated for a "forward deploy" role at growthx.ai, the AI infrastructure and content automation startup co-founded by Daniel Lopes (ex-IFTTT/Basecamp CTO, 25 years programming) and Marcel (ex-CMO at HashiCorp, Scale AI, DeepGram). The interview serves as the final stage of their hiring process, following a team interview. Tamy is a strong cultural fit: she shares Brazilian heritage with much of the team (15+ Brazilians across GrowthX), speaks Portuguese, and works in a timezone that aligns with the team's global presence.

This interview focuses on Tamy's take-home project—a demonstration of how she approaches system design, AI tooling, and prompt engineering under time constraints—combined with deep-dive discussion of her career trajectory and technical philosophy. The interview is intentionally structured to evaluate whether her thinking patterns, problem-solving approach, and experience building AI-driven automation align with growthx.ai's vision: productizing an agency's AI workflows into a code-first, open-source Content OS that partners can integrate via CMSs like Webflow and Strapi.

---

## Relevance

**To GrowthX Hiring & Team Building:**
- Strong culture fit: Brazilian heritage, Portuguese speaker, aligned with team's global composition (15+ Brazilians on staff). Immediate rapport with Daniel on Brazil/local context.
- Technical + Product hybrid: 10 years web (SEO/CRO) → 4 years PM (Scali, Passei Direto/Wall) → 2 years AI/automation consultant. Unique "forward deploy" perspective combining technical depth with product intuition.
- Self-taught AI automation and prompt engineering expertise: no formal ML background, but disciplined approach to learning and systems design mirrors growthx.ai's philosophy.
- Ready to extend offer: Daniel was "highly impressed" and committed to proposing role by EOD Nov 24 or AM Nov 25 pending team calibration.

**To GrowthX AI/Product Strategy:**
- Take-home architecture validates internal framework: Tamy's code-first, markdown-based prompt structure with JSON schemas, role/goal definitions, chained tasks, and evaluation loops directly mirrors growthx.ai's internal Content OS architecture.
- Prompt engineering best practices: Temperature tuning for determinism (lower for summary/keywords, higher for creativity), explicit schemas, examples-over-rules approach, guardrails for edge cases, and service-specific scoring/retry logic all demonstrate sophisticated AI systems thinking.
- Forward-looking optimization: Tamy identified improvement areas (service-specific retries vs. global score, cost optimization) before shipping—the exact mindset growthx.ai needs for productizing its agency workflows.

**To GrowthX Delivery & Content Operations:**
- Entrepreneurial track record: Bootstrapped a BI SaaS for e-commerce marketing ops (10x ROI before sunset), demonstrating ability to execute end-to-end from architecture to launch.
- Structured development process: Uses ChatGPT for validation, Codex for prototyping, Copilot for refinement—reflects systematic approach to AI-augmented development vs. ad-hoc AI use.
- SEO/linguistics background: 4 years SEO/CRO with linguistics degree, deep knowledge of content intent and search. Directly applicable to CheckThat (AI visibility index) and Content OS SEO capabilities.

---

## Overview

- **Ideal Candidate:** Tamy's background as a PM who self-taught AI automation for SEO is a perfect fit for the "forward deploy" team's hybrid role.
- **Take-Home Alignment:** The take-home project's architecture (code-first, markdown prompts, JSON schemas, evaluation loops) mirrors growthx.ai's internal framework, validating a strong technical and cultural match.
- **Vision & Strategy:** growthx.ai is productizing its agency's workflows into a Content OS, built on an open-source, code-first AI engine. The goal is to partner with CMSs (e.g., Webflow, Strapi) to provide deep SEO capabilities they lack.
- **Decision:** Daniel was highly impressed and will extend an offer after calibrating with the team.

---

## Key Topics

### growthx.ai: Context & Vision

  - **Founding:** Daniel (25 yrs programming, ex-IFTTT/Basecamp CTO) and Marcel (ex-CMO at HashiCorp, Scale AI, DeepGram) co-founded growthx.ai in 2023.
  - **Origin:** Built an agency (60+ clients) to prove the model, then productized the underlying AI infrastructure.
  - **Product Strategy:**
      - **1. AI Workflow Engine:** An open-source, code-first framework for building complex AI workflows.
          - **Rationale:** Code offers superior scalability and flexibility over visual builders (e.g., AirOps) for complex, high-volume tasks.
          - **Features:** End-to-end tracing, agent-driven optimization, and a future marketplace for monetizing workflows.
      - **2. Content OS:** A SaaS platform productizing the agency's workflows.
          - **Goal:** Enable internal marketing teams to replicate Marcel's success at DeepGram (25x growth in 3 months) without hiring an agency.
          - **Features:** Normalized analytics, a page catalog with semantic analysis, and a task management system.
      - **3. Marketplace:** A platform connecting clients with expert freelancers for tasks like technical reviews, with all context and communication managed within the Content OS.
      - **4. AI Visibility Tool:** A data product tracking AI prompt performance, positioned as a Semrush/Profound competitor.

### Tamy Ogasawara: Background & Experience

  - **Career Path:** 10 years in web, starting in SEO/CRO → Product Manager (Scali, Passei Direto/Wall) → AI/SEO Automation Consultant.
  - **Key Experience:**
      - **SEO/CRO:** 4 years, leveraging a linguistics degree for deep content and search intent analysis.
      - **Product Management:** 4 years, building products across checkout, catalog, growth, and SRE.
      - **Entrepreneurship:** Bootstrapped a BI SaaS for e-com marketing ops (built with Bubble.io), achieving a 10x ROI before the project was sunset.
      - **AI/Automation:** Last 2 years focused on making SEO a product via micro-apps and prompt engineering.

### Take-Home Project: Keyword Extraction API

  - **Challenge:** Build an API to extract summary, category, keywords, and sentiment from text.
  - **Architecture:**
      - **Structure:** Separate markdown files for each task (summarization, keywords, etc.).
          - **Rationale:** Enables parallel execution, independent maintenance, and easier debugging.
          - **Trade-off:** Slightly higher token usage and API calls.
      - **Prompt Design:** A consistent template for each task.
          - **Components:** Role/Goal, Context, Chained Tasks, Examples, Guardrails, and a JSON Schema for output.
      - **Evaluation & Retries:**
          - **Current:** A global 0-20 score; retries all services if the total score is \<15.
          - **Future Improvement:** Implement service-specific retries (e.g., retry only summarization if it fails) to reduce costs and improve efficiency.

### Development Process & AI Tooling

  - **Workflow:** A structured process for using AI.
      - **1. Analysis:** Review past, similar projects to leverage existing knowledge.
      - **2. Architecture:** Diagram the system and make high-level tech decisions (e.g., TypeScript/Node.js).
      - **3. Prompting:** Use ChatGPT to validate ideas and find counter-arguments.
      - **4. Prototyping:** Use Codex to generate a high-level code skeleton.
      - **5. Refinement:** Use Copilot for debugging, refactoring, and adding detail.

---

## Action Items

- **Daniel Lopes (GrowthX):** Discuss Tamyres Ogasawara's candidacy with Tucker and the team for calibration.
- **Daniel Lopes (GrowthX):** Extend an offer to Tamyres Ogasawara by EOD Nov 24 or AM Nov 25 pending team approval.

---

## Transcript

**Daniel Lopes:** This meeting is being recorded.

**Tamyres Ogasawara:** Can you hear me well?

**Daniel Lopes:** Yeah, now I can.

**Tamyres Ogasawara:** Oh, awesome, awesome, awesome. I don't know what was happening, but it's good.

**Daniel Lopes:** I think it was on my side. Are you from Brazil?

**Tamyres Ogasawara:** Yeah.

**Daniel Lopes:** Yes, yes, I'm from Brazil.

**Daniel Lopes:** Sim, sim, sou do Brasil.

**Daniel Lopes:** Beleza.

**Daniel Lopes:** Eu sou de Belo Horizonte, meu sócio, Marcel, é de São Paulo, mas cresceu aqui.

**Daniel Lopes:** A gente tem um monte de brasileiro no time.

**Daniel Lopes:** Não sei se você sabia.

**Tamyres Ogasawara:** Perfeito.

**Tamyres Ogasawara:** Pior que eu não sabia, todo mundo que eu falei até agora, nenhum era brasileiro, então eu não estava sempre sabendo dessa informação.

**Daniel Lopes:** A gente tem eu, Marcel, tem Mateus, tem Pedro, Estevam, cinco brasileiros, tem Stefan também.

**Daniel Lopes:** E aí, tem os brasileiros.

**Tamyres Ogasawara:** Tá em peso, tá em peso.

**Daniel Lopes:** Quase todo mundo no time de...

**Daniel Lopes:** Acho que tem mais gente no time editorial também.

**Daniel Lopes:** Acho que tem Mariana, acho que tem mais quatro pessoas.

**Daniel Lopes:** A gente deve ter umas 15 pessoas no Brasil.

**Daniel Lopes:** No time técnico a gente tem uns 6.

**Daniel Lopes:** Mas não é por cultura, a gente posta o job post em qualquer lugar e sempre tem bastante brasileiro aplicando.

**Daniel Lopes:** E acho que por causa da nossa qualidade de ensino no Brasil, a gente acaba pegando bastante brasileiro.

**Daniel Lopes:** A gente pode mudar para inglês, que aí eu posso gravar a entrevista.

**Tamyres Ogasawara:** For sure, for sure.

**Daniel Lopes:** Ok, cool.

**Daniel Lopes:** I hope you don't mind, but we record all of our interviews.

**Tamyres Ogasawara:** Yeah, for sure.

**Daniel Lopes:** Just for everybody to calibrate.

**Daniel Lopes:** But, yeah, for today, I was thinking that maybe I can just give you my background for like five minutes, explain how we got here. And then if you could walk me through your take-home, explain how you do things and how you're working.

**Daniel Lopes:** I didn't have time, and I usually don't do that on purpose, but I didn't have time to check the assignment that you completed for us.

**Daniel Lopes:** Then maybe after that, just walk me through your resume, your projects, what you've been doing, or your life story.

**Daniel Lopes:** That would be really helpful.

**Daniel Lopes:** And I can start with mine.

**Daniel Lopes:** But yeah, so my name is Daniel. I'm a co-founder of GrowthX. We started the company last year.

**Daniel Lopes:** Before that, I've been a programmer for like 25 years.

**Daniel Lopes:** I've been in like 2000, I have like a course technical, computer science, and also like a bachelor's degree in computer science.

**Daniel Lopes:** And then got super excited about a framework, web development framework.

**Daniel Lopes:** We were called Ruby on Rails in 2005 when it got launched.

**Daniel Lopes:** And then that's when I switched from desktop development to web development, because I was more focused on desktop apps first.

**Daniel Lopes:** And then started working for a bunch of American companies when I got involved with Rails and got involved with the community, helped organize a bunch of events.

**Daniel Lopes:** Eventually, like I got tired from the Brazilian market.

**Daniel Lopes:** It was like 2012, 2011.

**Daniel Lopes:** The Brazilian startup ecosystem wasn't as mature for like creating great products.

**Daniel Lopes:** And I was trying to figure out like what are the companies that I would like to work for.

**Daniel Lopes:** And then I got the opportunity to work for a company that was invested by the creators of the Ruby on Rails framework in Chicago. So I did that for three years.

**Daniel Lopes:** And then I got a lot of my friends from the Brazilian Rails community who had ended up here in the Bay Area. And then I wanted to come over here and see what was happening in the tech community and the job market, and got a job here.

**Daniel Lopes:** Ended up joining a company called IFTTT, if this, then that, like a precursor of Zapier. I don't know if you've heard of them.

**Daniel Lopes:** Yeah, so it was like Zapier, consumer-focused Zapier, basically, pre-Zapier.

**Daniel Lopes:** And, yeah, it was an interesting project, 10 million users, joined as a programmer on the product team, and then I switched to lead their entire product after, from the technical side, and then as head of product.

**Daniel Lopes:** Started coding less, and actually just managing all the different projects, did that for a couple of years.

**Daniel Lopes:** And then the Basecamp folks were spinning off a bunch of their projects, and they wanted to just focus on Basecamp.

**Daniel Lopes:** Like, Rails came out of Basecamp, and Basecamp was their core product, company called 37 Signals, and they had, like, a bunch of other products.

**Daniel Lopes:** So they were spinning off a bunch of different companies. I took one of their companies as a CTO, and I ran that for the last seven years before joining Marcel.

**Daniel Lopes:** And that was right at the inflection point, like my end of my seven years there was like right at the inflection point where like COVID layoffs were starting.

**Daniel Lopes:** So the whole market was kind of like frozen.

**Daniel Lopes:** And we also had a very clear path for AI to become like something that would enable a bunch of different applications that you couldn't do before.

**Daniel Lopes:** So I was, my last project with Canopy at the company was actually a chatbot.

**Daniel Lopes:** Before chatbots were easy to do.

**Daniel Lopes:** So we spent a lot of time figuring out the regulations, figuring out the accuracy and like how to respect the context, like not let things like harassment get through or prompt injection attacks, all that stuff.

**Daniel Lopes:** So I spent a lot of time on that.

**Daniel Lopes:** And then I wanted to study a lot.

**Daniel Lopes:** So it took like an eight-month sabbatical, just reading a bunch of AI papers and prompt engineering and context engineering and all that. And that's when I met Marcel, was at the end of the sabbatical.

**Daniel Lopes:** And he was doing the same, but he was coming from the marketing angle.

**Daniel Lopes:** Like he wanted to figure out like how to do, how to reinvent entire marketing teams using AI.

**Daniel Lopes:** And he was, Marcel has an interesting background.

**Daniel Lopes:** He was a CMO at HashiCorp, the company behind Terraform.

**Daniel Lopes:** And also Scale AI, a big one for data labeling.

**Daniel Lopes:** And then DeepGram, which is a speech-to-text processing platform, like a competitor of 11 Labs.

**Daniel Lopes:** And when he was in DeepGram, he was trying to figure out how to do what he did at HashiCorp with a much smaller budget.

**Daniel Lopes:** And so he was trying to figure out, okay, how can I leverage AI to do entire content teams, but still have the same quality and like plant as many seeds as possible and then improve the ones that actually work.

**Daniel Lopes:** By pushing a bunch of different pieces.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So when I joined him, he was starting this, trying to teach people how to do that. He was still at DeepGram, and he had gotten great success doing that at DeepGram, achieving like a 25X in just three months.

**Daniel Lopes:** And because of his background in AI, he could understand the whole systems really well.

**Daniel Lopes:** So he knew what was possible, what wasn't possible, and et cetera.

**Daniel Lopes:** So he was building like super complex chaining systems that you could call, like LLMs calling each other, calling APIs, like the usual stuff that everybody's doing now.

**Daniel Lopes:** Marcel was doing that like two years ago, and he was hitting all sorts of scalability problems. He got to the point where he was teaching people how to do it, and people wanted to do it, but they didn't have the staffing for it. So he ended up starting an agency on the side while still running DeepGram. And then it got to the point where he decided it made more sense to just run the agency. That's when I joined him.

**Daniel Lopes:** So like we already had like 10-ish clients.

**Daniel Lopes:** They're all really big clients like Ramp, Reddit, Superhuman.

**Daniel Lopes:** And they all needed like thousands of runs a day.

**Daniel Lopes:** And none of those tools could handle that easily.

**Daniel Lopes:** And the ones that could, like in a day, you'd have to like fork and hit self-host.

**Daniel Lopes:** And now you have self-hosting like 10 different instances and all that.

**Daniel Lopes:** So we ended up building the infrastructure to handle that as code.

**Daniel Lopes:** So like we have like a way to create workflows in code and that kind of stuff.

**Daniel Lopes:** So that was the first product.

**Daniel Lopes:** And that's how it started.

**Daniel Lopes:** But yeah, so that's a little bit of my last 20 years compressed in five minutes.

**Tamyres Ogasawara:** Awesome.

**Daniel Lopes:** I hope that makes sense.

**Tamyres Ogasawara:** Yes, it does.

**Tamyres Ogasawara:** It does.

**Tamyres Ogasawara:** It got a good feeling of your background.

**Daniel Lopes:** Sure.

**Daniel Lopes:** And then at the end, I can answer any questions, anything.

**Daniel Lopes:** I don't have a hard problem.

**Daniel Lopes:** Just a little bit.

**Daniel Lopes:** Sure.

**Daniel Lopes:** Sure.

**Daniel Lopes:** Yeah, I don't have a hard stop, but if we go over, Fathom is fine.

**Daniel Lopes:** Yeah, if you could walk me through your code base for the take-home, that would be great, because that project is actually representative of some of the things we do.

**Tamyres Ogasawara:** For sure, for sure.

**Tamyres Ogasawara:** Can you see my screen?

**Daniel Lopes:** Mm-hmm.

**Tamyres Ogasawara:** Awesome.

**Tamyres Ogasawara:** Perfect.

**Tamyres Ogasawara:** So, this is the take-home.

**Tamyres Ogasawara:** Do you know fully about the challenge that was given to me, or is, like, totally no context, and you'd like me to explain a bit of the challenge?

**Daniel Lopes:** can you just scroll down, just to make sure I'm looking at the right one, or usually do it.

**Daniel Lopes:** Okay, yeah, so this is the

**Daniel Lopes:** New one that Kirkland came up with.

**Tamyres Ogasawara:** it's keywords, extract keywords from the text, right?

**Tamyres Ogasawara:** If I remember correctly.

**Daniel Lopes:** Yeah, correct.

**Tamyres Ogasawara:** Correct.

**Tamyres Ogasawara:** So essentially, it is an API that I will post like a text or like a short paragraph or something.

**Tamyres Ogasawara:** And what I need to do is that I need to extract summary, especially if it's like a longer text.

**Tamyres Ogasawara:** I need to categorize it.

**Tamyres Ogasawara:** I need to bring the primary and secondary keywords.

**Tamyres Ogasawara:** And then a high-level sentiment analysis.

**Tamyres Ogasawara:** So there are three options, either positive, neutral, or negative.

**Tamyres Ogasawara:** So this is kind of like the challenge that they gave me.

**Tamyres Ogasawara:** So I had to explain, of course, the prompt strategy.

**Tamyres Ogasawara:** The prompt strategy is essentially composed of different files for each one of those.

**Tamyres Ogasawara:** So I have a markdown for each one of those for the summarization, categorization, keywords, and sentiment analysis.

**Tamyres Ogasawara:** And then I did a little bit of explanation over here on some of my strategies.

**Tamyres Ogasawara:** I think the one that is more...

**Tamyres Ogasawara:** More interesting are the structure and the key principles.

**Tamyres Ogasawara:** So the structure across all prompts is that I start off by giving a row slash a goal.

**Tamyres Ogasawara:** So defining like what is the scope and what is the main objective, then giving it a little bit of context, dividing into tasks, more like a chain of thoughts, like step-by-step type of situation.

**Tamyres Ogasawara:** The next sample in order to have kind of like a golden sample, essentially of what I expected to return to me.

**Tamyres Ogasawara:** Some rules like slash and also like guardrails of like hard constraints in terms of length, format, style, and also some high-level like, I would say, treatments for edge cases in terms of like if something fails, what happens.

**Tamyres Ogasawara:** And then last but not least, the output, which is a JSON schema because it's supposed to be emulating slash being an API.

**Tamyres Ogasawara:** Some of the principles that I essentially thought about is, first of all, emphasizing the...

**Tamyres Ogasawara:** Title of the text, because usually the title already comes a bit with the intent, so it's interesting to give it a little bit more weight than like the full content.

**Tamyres Ogasawara:** Then also explicit schemas, so JSON structure, example over rules as well, I like to give it very clear examples of other ones, and then of course like using natural language.

**Tamyres Ogasawara:** Trade-offs, so trade-offs here, since I divided the problems each one into like its own folder and file, then pros is like more clear, easier to debug, I think it's likely one of the main ones.

**Tamyres Ogasawara:** It's a parallel execution as well, and independent maintenance, so I can like change like each one of the files like as I want, if I feel like the contextualization is not good, or if I feel like the summarization is not good, I can like focus on essentially giving maintenance slash testing like then more.

**Tamyres Ogasawara:** Then separately, which is more intuitive, calls, slightly higher token usage, more API calls, and slightly higher calls due to higher token usage, and also more API calls.

**Tamyres Ogasawara:** So I like to give you a high-level thought of what are the pros and phones, although the take-home already told me to do them separately.

**Tamyres Ogasawara:** I like to emphasize what is the pros and cons of doing that.

**Tamyres Ogasawara:** So another layer of the case is like determinism versus creativity.

**Tamyres Ogasawara:** I decided to use a lower temperature because most of the tasks like summary, category, keywords, independent sentiment, I don't need like a high creativity.

**Tamyres Ogasawara:** It's like a higher risk that I didn't see a good like upside on assuming this risk.

**Tamyres Ogasawara:** And then what I decided essentially for summary, category, keyword, and sentiment is that for summary, two to four sentences, I give it like a context?

**Tamyres Ogasawara:** Length, Limit, I will show you on the code in a bit.

**Tamyres Ogasawara:** Categories one to three, at least one of them needs to be specific, aka a bit more long tail, like a subcategory.

**Tamyres Ogasawara:** So if I have technology and then machine learning, the third one, I defined that it needed to be something a bit more specific as like a prompt engineering, for example.

**Tamyres Ogasawara:** Then keywords, essentially also I did some length type of like rules that I will show you a little bit the thought process, and also count.

**Tamyres Ogasawara:** So it has to have at least one primary keyword, and if I'm not mistaken, four secondary keywords.

**Tamyres Ogasawara:** Sentiment analysis, the main constraint, very, very high like constraints that needs to be either a positive, neutral, or negative.

**Tamyres Ogasawara:** So here I give more like details, but I think we can jump to like, what are the things that I would do if I had more time, and then we can go to the code.

**Tamyres Ogasawara:** So what I would do if I had more time, essentially right now, I use a score system to approve essentially the output.

**Tamyres Ogasawara:** This score system is a global one, aka, although I have scores for each one of the, I would say, services, the end score is just one.

**Tamyres Ogasawara:** So it has like a zero to 20 points that it could have.

**Tamyres Ogasawara:** And if it is lower than 15, it's considered like a failure.

**Tamyres Ogasawara:** If it is higher than 15, it's considered like a good balanced output.

**Tamyres Ogasawara:** So the main constraint with this model is that since it is global, if one area got like a low, like low end point, for example, if the summary one through five, it got like a two, it still like goes as a success.

**Tamyres Ogasawara:** So if I had more time, I would essentially work on separating each one.

**Tamyres Ogasawara:** into their own type of verification, like at least 2.5 out of like five, for example.

**Tamyres Ogasawara:** And another thing that I would do is essentially I would also do a system of essentially making sure that they regenerate just the service that went with the bad outputs.

**Tamyres Ogasawara:** Because right now, if I had 15, 14 out of 20, and the main issue was like the summarization, right now it is regenerating summarization, categorization, sentiment, etc.

**Tamyres Ogasawara:** So if I had more time, I would likely do the retry based on the specific service and not like the retry of all the four services.

**Tamyres Ogasawara:** So since Tucker told me to take max two hours, there were some choices that I had to do in terms of like prioritization of what I would like and what I would

**Daniel Lopes:** Walk me through your development process, because this really is pretty well-structured, pretty elaborate.

**Daniel Lopes:** What was your tool of choice?

**Daniel Lopes:** You probably used AI for this.

**Daniel Lopes:** How did you tackle figuring out, so you got this assignment, what is the first thing that you did after that?

**Daniel Lopes:** Just to be clear, it's kind of the opposite environment of most places where people will be like, oh, don't use AI, or I want you to do things.

**Daniel Lopes:** We're kind of trying to do the exact opposite of that, where we had, because today, there's very few people, for our product engineering and for the runtime and infrastructure engineering roles we have, sometimes we will give like an assignment that's essentially impossible to do if you don't do it with AI.

**Daniel Lopes:** All right.

**Daniel Lopes:** And then we had a couple of people that actually did it, moved on.

**Daniel Lopes:** And it was like a pairing for a session, and I'm sitting next to them, and I'm seeing them code.

**Daniel Lopes:** It's like, gosh, this guy is way better than me.

**Daniel Lopes:** And they move a lot faster than they expect.

**Daniel Lopes:** So we made exceptions to that.

**Daniel Lopes:** But most of our team is just using AI all day long.

**Daniel Lopes:** So there's nothing wrong with quite the opposite.

**Daniel Lopes:** So walk me through your process of how you've managed to do it.

**Daniel Lopes:** If you actually did it in two hours, and if you did, what was the process?

**Daniel Lopes:** Nothing.

**Daniel Lopes:** If you took longer, that's totally fine, too.

**Daniel Lopes:** And I've done take-home assignments myself that would be like, just do it for two hours.

**Daniel Lopes:** I I spent two days on it.

**Daniel Lopes:** And that is fine, too.

**Daniel Lopes:** But walk me through the whole background here, if you could.

**Tamyres Ogasawara:** Yeah.

**Tamyres Ogasawara:** So essentially, I did take more than two hours.

**Tamyres Ogasawara:** I think it took about four to five, to be very honest, to do that side.

**Daniel Lopes:** Yeah, I did want to cover on a deeper level, especially because it didn't have anything mentioning like retry and like evaluation, etc.

**Tamyres Ogasawara:** So it wasn't mentioning these, but I think this is so important for you to understand my level of like knowledge, like because I could do like in one hour if I wanted to just like output directly just a summary and not have like not make sure that actually I'm doing at least a base level evaluation or retry system.

**Tamyres Ogasawara:** So for sure, took me more than like two hours because I wanted to make sure that I was covering at least, I would say the main cases that I could see failing.

**Tamyres Ogasawara:** So in terms of my thought process, essentially, I work nowadays as a consultant slash contractor for AI, specifically for SEO.

**Tamyres Ogasawara:** So I've been working with that for the past two years.

**Tamyres Ogasawara:** So to be very honest, one of the reasons.

**Tamyres Ogasawara:** And why I had such a clear idea of what I wanted is because I already built systems very similar to these take-home.

**Tamyres Ogasawara:** So systems of like making briefs, systems of like making Reddit type of content, systems of summarizing content, trying to find keywords out of already existing content and etc.

**Tamyres Ogasawara:** So the first thing that I do, being like very honest, this might be unusual, I don't know.

**Tamyres Ogasawara:** But the first thing that I did is that I studied all the systems that I already created in the past that were similar to this challenge.

**Tamyres Ogasawara:** So I was taking a look of everything that I did and all the kind of like hiccups that I did on the way of trying to get like a good output of content and also trying to work in a way that I can make sure that the content that I produce would be good.

**Tamyres Ogasawara:** So this was the first step.

**Tamyres Ogasawara:** Then when I found that I could like essentially take at least 50 to 60% of what I already learned in the past, then

**Tamyres Ogasawara:** The first thing that I did is also I went through doing the architecture of the system.

**Tamyres Ogasawara:** So essentially doing like a simple type of like flowchart slash diagram of how I thought this would work for each one of the services.

**Tamyres Ogasawara:** So first going through what I would do for like summarization and then going through what I would do for each one of them.

**Tamyres Ogasawara:** And then when I have a clear idea of like the sequence of what I want to happen, I have a clear idea of what are essentially the base level stuff that I wanted to use.

**Tamyres Ogasawara:** For example, one of the decisions that I took before even starting to code is that I would do it on TypeScript and also Node.

**Tamyres Ogasawara:** So when I had those like more like architecture level decisions and I knew that I already built something similar in the past that worked, then I went through like doing my, I would say quote unquote vibe coding type of exercise of going through like chat DPT and talking to it of like, I have ABC ideas.

**Tamyres Ogasawara:** I think in this case, it would make sense for me to do.

**Tamyres Ogasawara:** X, Z, please give me counter examples of why this wouldn't work.

**Tamyres Ogasawara:** So usually what I do is that I have a predefined idea and then I tell the AI actually to tell me why it sucks.

**Tamyres Ogasawara:** That's kind of how I vibe with it.

**Tamyres Ogasawara:** Then after doing this exercise, I got a clear idea of like what would be points that I could do like differently or in a more complete way.

**Tamyres Ogasawara:** And then I started to code.

**Tamyres Ogasawara:** And then I went through like coding together, like, of course, with Copilot.

**Tamyres Ogasawara:** It's one that I use a lot on my day-to-day.

**Tamyres Ogasawara:** GPT Codex as well is one that I use a lot on my day-to-day.

**Tamyres Ogasawara:** And then I started to code one by one, starting off with the prompt.

**Tamyres Ogasawara:** I always like to start off with the prompt.

**Tamyres Ogasawara:** So I went through like, I think only with the prompt, it took me like honestly one hour and a half to do the prompts.

**Tamyres Ogasawara:** Yeah, that makes sense.

**Daniel Lopes:** I was thinking so hard about like, what was the structure that I wanted to, the prompt to have?

**Daniel Lopes:** the markdown files, right?

**Tamyres Ogasawara:** The...

**Tamyres Ogasawara:** Yeah, yeah, yeah.

**Tamyres Ogasawara:** markdown files.

**Tamyres Ogasawara:** Correct.

**Tamyres Ogasawara:** Correct.

**Tamyres Ogasawara:** So then already took me like one hour and a half.

**Tamyres Ogasawara:** But to be frank, when I have like a very like predefined prompt that already has some rules on it and guardrails and like what to avoid and output and etc.

**Tamyres Ogasawara:** Then it's actually easier for me to code.

**Tamyres Ogasawara:** At least like with my background, I started off like two years and a half ago doing more like prompts instead of like coding on TypeScript nodes or like Python and etc.

**Tamyres Ogasawara:** So for me, always start off with the prompts because I can already think of on the written down way what I want to do before putting it into code.

**Tamyres Ogasawara:** And then I translate it into like, okay, now that I have the prompts and that I have a clear idea of what would be the output of like each one of those prompts.

**Tamyres Ogasawara:** Then I can start to go like for TypeScript nodes and like Fatspy, which is like the API framework that I utilize over here.

**Tamyres Ogasawara:** So then I can essentially essentially

**Tamyres Ogasawara:** So I would say like, in a nutshell, that's kind of like how my thoughts, thought process worked.

**Daniel Lopes:** Got it.

**Daniel Lopes:** This is great.

**Daniel Lopes:** Walk me through the, okay, so you have, this is kind of funny because like the way you structure the folders, that was not part of the assignment.

**Daniel Lopes:** So the assignment was just like, did it specify a TypeScript to node or does it just be a practice?

**Tamyres Ogasawara:** It didn't, I think it didn't specify TypeScripts and nodes, you know, I think it specify like any type like front end that I wanted.

**Tamyres Ogasawara:** I don't know.

**Tamyres Ogasawara:** I think you mentioned maybe Python TypeScripts as kind of like suggestions, but not like as requirements if I'm not mistaken.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Yeah, because like the way you organize things is very similar to, like we were working on the, like we have our internal framework for writing workflows in code.

**Daniel Lopes:** And we're going to open.

**Daniel Lopes:** And it's very, very similar to the way you organized.

**Daniel Lopes:** So we have markdown, essentially mark, there are YAML files, but you write the markdown for the prompts.

**Daniel Lopes:** And you can set the temperature and the parameters on top as like a YAML front matter, that kind of stuff.

**Tamyres Ogasawara:** Yeah, one thing that they did mention is that they wanted to have one folder of prompts.

**Tamyres Ogasawara:** That's one thing that was specified on the take-home, but this choice of like using like TypeScript and kind of like the choice of how it's structured, this was open.

**Daniel Lopes:** Yeah, and then you have guardrails.

**Daniel Lopes:** So we are also like shipping part of the framework.

**Daniel Lopes:** It's another one as a judge system.

**Daniel Lopes:** So it works very similar to how you did.

**Daniel Lopes:** And yeah, so like you kind of took a lot of the stuff that we are codifying.

**Daniel Lopes:** So you would like understand the workflows right away if you jumped in.

**Daniel Lopes:** So walk me through the source, what you have in this.

**Tamyres Ogasawara:** So I have the validation, the server of course, the types specified.

**Tamyres Ogasawara:** Then I have the services.

**Tamyres Ogasawara:** Here is a one like this core system that I told you about that I did to essentially help evaluating.

**Tamyres Ogasawara:** Then I have the LLM also like TypeScript type of like treatment on top of the on top of the prompts.

**Tamyres Ogasawara:** Then I have the API to essentially make the call, like the people can call the API with a JSON essentially.

**Tamyres Ogasawara:** I have like the final validation of like the global score of everything together over here on this one to make sure that they like all the four services are on an acceptable end.

**Tamyres Ogasawara:** And then quality and then a little too.

**Daniel Lopes:** So what's your process?

**Daniel Lopes:** I haven't used GitHub Copying, I know they have a chat, and you also mentioned codecs.

**Daniel Lopes:** have a chat.

**Daniel Lopes:** So how do you use both?

**Tamyres Ogasawara:** So usually what I like to do is that I like to go through codecs to think on like the app on a global level, like what I want to do with everything.

**Tamyres Ogasawara:** So usually I fit it with like what is the architecture that I thought about or with some suggestions in terms of like rules and what I think that would be the output and services and et cetera.

**Tamyres Ogasawara:** And I tell you to essentially break down those into what structures you think that it would be interesting and also give me like some critics slash feedback in terms of like, am I forgetting something on the architecture that I did?

**Tamyres Ogasawara:** I forgetting something on the like rules that I did?

**Daniel Lopes:** So that's also why I like to start.

**Tamyres Ogasawara:** And the prompts, because then it's easy to fit into it and say, like, this is what I'm expecting.

**Tamyres Ogasawara:** This is the behavior that I'm expecting.

**Tamyres Ogasawara:** And then when I have this broken down, then I start to create the folder, the files and stuff.

**Tamyres Ogasawara:** And then through creating everything, of course, I won't get, like, a full app speech, like, with codecs, unfortunately.

**Tamyres Ogasawara:** And then through, like, doing the files, then I go through copilot, and I get help of copilot in terms of, like, like, okay, I have this structure, like, tell me what is an efficient way to, I don't know, structure, like, the types.

**Tamyres Ogasawara:** Tell me if the types are actually including all the cases.

**Tamyres Ogasawara:** And also, like, debugging in terms of, usually codecs fit something that isn't fully functional.

**Tamyres Ogasawara:** So I do a lot of debugging with copilots as well.

**Tamyres Ogasawara:** And last but not least, what I usually do with copilots is also getting a little bit of help in terms of, okay, how can I do that in a way that is cleaner, for example?

**Tamyres Ogasawara:** How can I do that?

**Tamyres Ogasawara:** in a way that is simpler.

**Tamyres Ogasawara:** These are typical questions that I do.

**Tamyres Ogasawara:** And sometimes if I am unclear about what a specific part is doing, or how it has like relationship in terms with like relationship with other parts like routes and cars and et cetera, then I tell it's like, okay, what is the relationship between X and Z?

**Tamyres Ogasawara:** And then it helps me a lot with that.

**Tamyres Ogasawara:** So I would say start off with codex.

**Tamyres Ogasawara:** Actually, start off with doing the prompts, the architecture, fitting to codex to tell it to speed me like a high level structure of the services that I want to have, slash the micro lab.

**Tamyres Ogasawara:** Then when I have this done, create the files, create the folders, create the high level, like broad code structure on essentially like code.

**Tamyres Ogasawara:** And then with copilots, I'm like, okay, now let's debug.

**Tamyres Ogasawara:** Let's make sure that all the relationships make sense.

**Tamyres Ogasawara:** Let's let's make sure that the schema makes sense.

**Tamyres Ogasawara:** If it is like, if it has like a database and.

**Tamyres Ogasawara:** Let's make sure that everything is like following a consistent like structure because one of the points that I think Codex is not too good is that sometimes it's quite inconsistent, especially when you are talking a lot with it.

**Tamyres Ogasawara:** So Copilot is a bit more good in like looking at all the files and then spitting back to me what is going on.

**Tamyres Ogasawara:** Just like Cursor as well, think Cursor is also good at looking at the whole context of the app and not like the specific service slash specific file that I'm creating.

**Daniel Lopes:** Yeah, they all kind of work in different ways where...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, we go, we like the one, the framework that we're doing is like it's instrumented for a cloud code.

**Daniel Lopes:** So it will use cloud code, some agents and stuff like that.

**Daniel Lopes:** But, and I just, mostly what I use all the time is cloud code, but Cursor and Copilot, they do graph your entire code base and they understand all the files and everything.

**Daniel Lopes:** But...

**Daniel Lopes:** Cool.

**Daniel Lopes:** So you also mentioned ChatGPT.

**Daniel Lopes:** you start with ChatGPT and then you go into Codex.

**Daniel Lopes:** You take a dump of what you did in ChatGPT and then iterate in Codex and then you refine with Copilot.

**Tamyres Ogasawara:** Yes, correct.

**Tamyres Ogasawara:** That's kind of a high-level way that I do it because ChatGPT is good for me to have conversations about if it makes sense.

**Tamyres Ogasawara:** And then when everything is making sense, then it's like, okay, one would be like a base-level skeleton of these.

**Tamyres Ogasawara:** And then I have a base-level skeleton that would be like Codex.

**Tamyres Ogasawara:** And then I create the files.

**Tamyres Ogasawara:** And then when I create the files and I do the whole structure, then the fine-tuning, let's say like that.

**Tamyres Ogasawara:** I know that not literally fine-tuning, but literally like refinement of the app I do with Copilot.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Yeah, it's super helpful to see how you think and how you use it.

**Daniel Lopes:** Because to me, that is something that makes somebody be able to learn super fast and continue to iterate on things.

**Daniel Lopes:** Like my first 10 years of my career, spent teaching people how to code.

**Daniel Lopes:** And that's actually how I moved to Chicago, was to be both a product engineer and an instructor for one of the first coding boot camps.

**Daniel Lopes:** So it's pretty cool to see like how people can use and how different people use things in different ways.

**Daniel Lopes:** And I think that there is a set of common patterns of the people that get better with the tools that they follow.

**Daniel Lopes:** And you see like, and you definitely have that profile that you can leverage in different ways.

**Daniel Lopes:** And that's why was very curious to see how you came up to the conclusion of this way or architecture in your project.

**Daniel Lopes:** I skimmed through a project before, and it was really well-organized.

**Daniel Lopes:** So I can tell that you spent time thinking about the architecture and you paired with, like, a good, somebody, like, you had a pair programming session with an effective way to land on everything, right?

**Daniel Lopes:** Cool.

**Daniel Lopes:** Walk me through your background.

**Daniel Lopes:** Like, you can start from whatever section you want, but you have a pretty interesting, like, the way we organize the team today is that we have, we're actually changing the structure of the team now, and we have a product team that has a bunch of different kinds of programmers, and then we have this forward deploy team where you have Stevie, Kirkland, you've met both of them, and then we have Marcus and Nico.

**Daniel Lopes:** They're both, like, Marcus has, like, 20 plus years of experience, and Nico is also a very experienced engineer, but they're traditional they're traditional engineers.

**Daniel Lopes:** They're just super good, but they don't come from the background of SEO or content or marketing.

**Daniel Lopes:** And then Kirkland is the opposite.

**Daniel Lopes:** He spent most of his life in that area, and then he led the SEO and the marketing function at ClickUp.

**Daniel Lopes:** And that's where he started being allowed to code and learning, figuring out how to automate things and all that.

**Daniel Lopes:** And he did an amazing job there.

**Daniel Lopes:** So that's the structure of team we have, and you would be on this team.

**Daniel Lopes:** And so we're noticing that pairing people like Markers with Kirkland, even if they're not working the same stuff, but having them be able to talk to each other and calibrate what is possible, what's not possible, think about the hiccups that we might have of rolling out large functions or coming up with new websites for different clients and stuff like that.

**Daniel Lopes:** It's like, for example, Nico just...

**Daniel Lopes:** Build an agent that generates templates for Lovable in their template library, and it goes back and forth and creates a final version of the template.

**Daniel Lopes:** So Nico can do that, but if he doesn't have somebody like Crickman say, this is how we structure the template library and how it will do well versus like, it is a heavy lift project as well.

**Daniel Lopes:** It's going to take us probably a month or two to get it right.

**Daniel Lopes:** Is it worth doing versus doing just like a cluster of categories or whatever, like more traditional things?

**Daniel Lopes:** So that's kind of the structure of the team.

**Daniel Lopes:** And it would be really cool to get your background because I see that you do both, but you have a PM background and you've been doing a lot of SEO and growth consulting and you're doing some automation as well.

**Daniel Lopes:** And I also can see that you're coding these things and you understand the code.

**Tamyres Ogasawara:** That's why I was asking, like open the code and like walk me

**Daniel Lopes:** So, and you can like think about the architecture and all that.

**Daniel Lopes:** And I saw that you were a PM for an SIE function of the wall, right?

**Daniel Lopes:** So, like walk me through your background.

**Tamyres Ogasawara:** Yeah, my background is honestly a bit of a lot of stuff.

**Tamyres Ogasawara:** It's kind of crazy, but in short, I've been working with digital slash web for the past 10 years.

**Tamyres Ogasawara:** I started off with SEO.

**Tamyres Ogasawara:** So, my bachelor degree was actually in literature and linguistics.

**Tamyres Ogasawara:** So, for me, it made a lot of sense for me to work with SEO because it would be like a lot of content writing, thinking about like keywords and the structure and like what people like engage with when they are like reading.

**Tamyres Ogasawara:** A bit of semantics as well, like understanding what is the intent of the search.

**Tamyres Ogasawara:** So, all of these for me made a lot of sense coming from linguistics.

**Tamyres Ogasawara:** So, background, so I worked with SEO for about four years of my career.

**Tamyres Ogasawara:** I got into like a management.

**Tamyres Ogasawara:** So of CRO and SEO, so conversion rate optimization, and also search engine optimization.

**Tamyres Ogasawara:** But then I felt a bit like the curiosity of, okay, I really want to be more engaged into actually building something.

**Tamyres Ogasawara:** Just for like a funny background, my father comes from software engineering.

**Tamyres Ogasawara:** He's an enterprise architect.

**Tamyres Ogasawara:** So I was curious to know a bit more about like tech and a bit more about like building apps and this kind of stuff.

**Tamyres Ogasawara:** So that's when I did a jump to work as a product manager.

**Tamyres Ogasawara:** And then I worked as a product manager for about like four years as well.

**Tamyres Ogasawara:** And I am a very curious person.

**Tamyres Ogasawara:** Like I am very, very curious into understanding a lot about how things work and the structure of things.

**Tamyres Ogasawara:** And I'm a very hands-on person as well.

**Tamyres Ogasawara:** So one thing that frustrated me a bit with like just knowing one or two products is that I didn't feel like I had a global vision of how a business works.

**Tamyres Ogasawara:** So I went through like...

**Tamyres Ogasawara:** like...

**Tamyres Ogasawara:** Working with a checkout, working with a catalog, to working with growth as a product manager, and also working all the way to security with SRE team.

**Tamyres Ogasawara:** So it was also kind of like follow on my curiosity, to be very honest.

**Tamyres Ogasawara:** And I really loved actually to work with all of these different functions, because I do have like the ambition of like five, ten years, have my own company to be an entrepreneur.

**Tamyres Ogasawara:** So I kind of do that, like being a contractor and having, I already had an agency as well.

**Tamyres Ogasawara:** So I kind of did that in the past, but I feel like you need to be ready in terms of like having a lot of knowledge, and not like vague, superficial knowledge, like deep knowledge into stuff.

**Tamyres Ogasawara:** So that's why I also became a product manager of like multiple products, so I could understand that kind of like the full idea of a business.

**Tamyres Ogasawara:** What was the company that, so like...

**Daniel Lopes:** You joined as an SEO person and you switched to product manager at the same company?

**Tamyres Ogasawara:** Yes, yes.

**Tamyres Ogasawara:** I worked at a company called Scali, which was a company essentially for kind of like a system of acquisition, but for other companies.

**Tamyres Ogasawara:** It's kind of like affiliate is a very loose term, but I would say like affiliate company where they had their own strategy of how to acquire customers and leads and et cetera.

**Tamyres Ogasawara:** And then they started to develop their own technology behind this as well.

**Tamyres Ogasawara:** So their own checkout, for example, because they wanted to experiment with higher conversion and a catalog.

**Tamyres Ogasawara:** So they could organize a bit all the telecommunications, because in Brazil, I think you might know that that's very messy.

**Tamyres Ogasawara:** So they have their own like technology in order to be more efficient.

**Tamyres Ogasawara:** Generating leads for a lower cost so they can have like bigger deals with companies such as like Vivo, Ching, UI, etc.

**Tamyres Ogasawara:** So I first started off with like having a website that was already working and then optimizing it for SEO and CRO.

**Tamyres Ogasawara:** But then since I got more curious about technology, there was an opportunity to actually build the checkouts instead of like being the person that would optimize the website for SEO.

**Tamyres Ogasawara:** And then that's where I do like a product management transition.

**Tamyres Ogasawara:** So I did like a formal like interview process.

**Tamyres Ogasawara:** think I had like two, three interviews and one case study to do.

**Daniel Lopes:** Like it was like an actually formal migration.

**Daniel Lopes:** What was the team structure?

**Daniel Lopes:** How big is the company and like what's the setup there?

**Tamyres Ogasawara:** It was fairly big, think they had around 200 employees back then, 200, 250.

**Tamyres Ogasawara:** So So Thank

**Tamyres Ogasawara:** The team that I started to work as a product manager essentially had one designer, I think it was four developers, one being like the tech lead, and then a product manager.

**Tamyres Ogasawara:** And then we kind of had a relationship with another team because it was two checkout teams.

**Tamyres Ogasawara:** So one was for what we call core, which was like backend.

**Tamyres Ogasawara:** So essentially going to like MongoDB, understanding like what were the main failures and card processing and yada, yada.

**Tamyres Ogasawara:** And one for the front end, which was more like component, how can we make this like better user experience so people will actually feel the form and how we can like check the information.

**Tamyres Ogasawara:** So it was kind of like loosely saying like back end and front end of the checkout.

**Tamyres Ogasawara:** So I started off working with the back end, but then the front end guy went away and then I did like the whole checkout.

**Tamyres Ogasawara:** So the back-end checkout team structure was this one, like three developers, one tech lead, one part-time designer, because this was back-end, they were like, it's not very necessary to have a designer, and then me as a product manager, APM, actually, back then.

**Daniel Lopes:** Got it.

**Tamyres Ogasawara:** So this was my first role.

**Daniel Lopes:** As a PM.

**Tamyres Ogasawara:** And then you switched it to Wall after, right?

**Tamyres Ogasawara:** Yes, yes.

**Tamyres Ogasawara:** Actually, went to Passei Direto, which is a company for helping students in Brazil to essentially go through their exams in universities.

**Tamyres Ogasawara:** And over there, after, I think, two months that I was on the team, they were actually acquired, at least publicly acquired by Wall Editech, which is the education side of Wall.

**Tamyres Ogasawara:** So, technically, it was Passei Direto, because this was the only...

**Tamyres Ogasawara:** The that I was working on, wasn't working for other products slash other verticals of law, but this was part of law edtech, I would say, kind of like environment, yes.

**Daniel Lopes:** Got it, got it.

**Daniel Lopes:** That's very interesting.

**Daniel Lopes:** So in two months you made the, you probably joined thinking the company would be one, and now you're working for like a giant company.

**Daniel Lopes:** Yeah.

**Tamyres Ogasawara:** Oh yeah, like it started off as a startup, because Passing Direct was a very small startup.

**Tamyres Ogasawara:** I think they had like 60, 70 people.

**Tamyres Ogasawara:** So like compared to wall, they were pretty small.

**Tamyres Ogasawara:** And then we had like a more flexible type of like tool usage.

**Tamyres Ogasawara:** We used to use Slack and like Google Cloud and all the Google kind of suite.

**Tamyres Ogasawara:** And then with the wall migration, then it changed for like teams and things started to be more like strict in terms of like how we would.

**Tamyres Ogasawara:** Corporate.

**Tamyres Ogasawara:** Yeah, corporate, yeah.

**Daniel Lopes:** It was an interesting transition for sure.

**Daniel Lopes:** How's it been?

**Daniel Lopes:** So you've done, so you were at Wall for a couple of years, and then you did a few other things, right?

**Daniel Lopes:** So you're like walking through the rest of it.

**Tamyres Ogasawara:** Yeah, essentially I took the risk of like trying to be an entrepreneur, like full time, so to speak.

**Tamyres Ogasawara:** So I worked as a consultant for some companies, and at the same time, I did work on trying to build the first version of a product, actually.

**Tamyres Ogasawara:** It was a BI SaaS, specifically made for e-commerces, more focused on actually like the marketing ops side of things.

**Tamyres Ogasawara:** So every metric related to like ads and organic and stuff.

**Tamyres Ogasawara:** So I worked there for about eight months to build like the first version of these products.

**Tamyres Ogasawara:** We literally had nothing when I joined then as a part-time contributor.

**Tamyres Ogasawara:** So I helped them to have the first version and also to do the go-to-market.

**Tamyres Ogasawara:** And we were able to launch this product and actually, in a bootstrapped way, we were able actually to get the money back that we invested on the product because we didn't invest much.

**Tamyres Ogasawara:** were very lenient.

**Tamyres Ogasawara:** Like, I built, oh my God, it was crazy.

**Tamyres Ogasawara:** I built the product kind of like with Bubble.

**Daniel Lopes:** That's kind of like the structure, you know, Bubble.io.

**Daniel Lopes:** Yeah.

**Tamyres Ogasawara:** It was my first experience with actually having to develop something with kind of like a database.

**Tamyres Ogasawara:** And I didn't have a lot of coding background when I started to build this.

**Tamyres Ogasawara:** And then I paired together with a data analyst so he can help me a bit with treating the data and like ETL and this type of stuff and making it compatible with like Bubble and then connect to Bubble.

**Tamyres Ogasawara:** We had a first version.

**Tamyres Ogasawara:** So we had a lot of things like trial and error, but the thing is that we got to like, I think back then it was like 60 to 70k US dollars, but we spent like, we spent 5k to like 7k US dollars.

**Tamyres Ogasawara:** was, I'm overestimating it, honestly.

**Tamyres Ogasawara:** So we had like 10x type of result.

**Tamyres Ogasawara:** So this was one of my experiences as well.

**Tamyres Ogasawara:** Unfortunately, they decided to sunset the product because they had also like a consulting side of the company and the consulting side was kind of like the cash cow.

**Tamyres Ogasawara:** And for them, although we had a 10x, they were expecting like a, I don't know, 100, 200x.

**Tamyres Ogasawara:** So they sunset the products and then I started to do, yeah, they started to do like.

**Tamyres Ogasawara:** That's a good run.

**Daniel Lopes:** It's so fast.

**Tamyres Ogasawara:** Yeah.

**Tamyres Ogasawara:** Yeah, I thought so as well, but like they were bootstrapped.

**Tamyres Ogasawara:** So Yeah.

**Tamyres Ogasawara:** So

**Tamyres Ogasawara:** They had different priorities.

**Tamyres Ogasawara:** And then since like after this like eight months, I worked as a contractor for like American companies in general.

**Tamyres Ogasawara:** So I think the major project that I did as a contractor was actually working as a SEO product manager at Enrollment Resources, which is a Canadian company.

**Tamyres Ogasawara:** Also into like education technology, but they are more on the like web development side of things.

**Tamyres Ogasawara:** They develop like websites and lead collection systems.

**Tamyres Ogasawara:** And also, of course, like in the process of that, they also needed to make the product SEO friendly because the product was kind of like the web structure.

**Tamyres Ogasawara:** So I worked with them for almost two years. I think it was one year and nine or ten months to help structure actual SEO products, which is when I got deeper into web coding and prompt engineering and thinking.

**Daniel Lopes:** That's great.

**Tamyres Ogasawara:** And now, yeah, now that's it.

**Tamyres Ogasawara:** I'm working still as a contractor, but more into automation.

**Tamyres Ogasawara:** So the last two years of my career, we're very focused on automating stuff, building micro-apps, and actually making a CEO a product rather than a service, in a way.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Yeah, this is such a – you have such a perfect background for what you're trying to do.

**Daniel Lopes:** So it's, like, super helpful to hear all the details of everything you shared.

**Daniel Lopes:** I want to make sure you have time to ask questions as well.

**Daniel Lopes:** Is there anything that I can – happy to answer anything, happy to show you anything, or, like, talk about how we see things, how things might evolve as a company, and that kind of stuff?

**Tamyres Ogasawara:** I think the question that I have the most is, like, what is your vision of success?

**Tamyres Ogasawara:** Yes.

**Tamyres Ogasawara:** And I I

**Tamyres Ogasawara:** I know that this is a very broad question, so I will make it like, in the next three years, what's your vision of like, we accomplished what we are trying to accomplish, like, how do you see that, like, unfolding?

**Daniel Lopes:** Yeah, that's a great question.

**Daniel Lopes:** Let's see, what was the best way to show you that?

**Daniel Lopes:** I can actually share you, share my feedback, so give me a sec.

**Daniel Lopes:** Don't mind me, my screen here, this is actually what I had also, and then I ended up not asking you, none of the questions that I had, because it was, I usually go off script quite a bit, but, yeah, so the way we're thinking is, let me show you the pitch deck from Marcel as well, from our funding.

**Daniel Lopes:** So, So, So, So, So, So, So, So, So, So,

**Daniel Lopes:** Yeah, so, like, we basically, like, when I joined Marcel, like, I helped build IFTTT.

**Daniel Lopes:** IFTTT is the precursor of Zapier, so I'm really familiar with all the way folks can automate things, and that's been something that I've been thinking about for many years, even after I left IFTTT, like, almost eight years ago.

**Daniel Lopes:** So I was always kind of bummed out that we didn't become, like, the source for connecting everything, like, the way I thought it was possible, and we always had this two different visions, like, me and the CTO, like, the CEO, sorry, I also had the product, and he was also, like, had the own product, and his take was, like, he wanted to be consumer-focused, and I wanted, like, we didn't collapse, like, we worked really well together, and I love him.

**Daniel Lopes:** But we decided to not focus on the B2B side of things, and that's where Zapier grew.

**Daniel Lopes:** And then when I joined Marcel, it kind of felt like getting a do-over on this, on like, Marcel is stitching together this thing on the top is AirOps.

**Daniel Lopes:** So that's one of our workflows that we had for one of the clients.

**Daniel Lopes:** So we had like a bunch of core workflows that are reusable.

**Daniel Lopes:** So we would like to trigger them as like child workflows.

**Daniel Lopes:** And they were different, essentially like pretty complex chain workflows and all that.

**Daniel Lopes:** But even that wasn't sophisticated enough.

**Daniel Lopes:** So we ended up, okay, like this is a temporary thing.

**Daniel Lopes:** The really great way to do things is being code.

**Daniel Lopes:** And we're going to the trajectory where like generating code is becoming better and better and better.

**Daniel Lopes:** Why are we stitching together things with the user interface while code is becoming a natural language interface?

**Daniel Lopes:** So it was like, can we create a programming environment where you can create workflows in code in natural language?

**Daniel Lopes:** And can I move?

**Daniel Lopes:** And when I joined, was just...

**Daniel Lopes:** So I was going be the one that was going to maintain a shift of workflows like this.

**Daniel Lopes:** We had no plans of fundraising or anything.

**Daniel Lopes:** I was just interested in working with Marcelo because he was a pretty aggressive, fast-growing, right-minded CEO, CMO that could turn into the kind of CEO that should run VC-backed companies because you have both different profiles.

**Daniel Lopes:** Like you have bootstrap, people have one type of mindset, and then you have venture-backed companies.

**Daniel Lopes:** And sometimes they can be the same, but usually they're not.

**Daniel Lopes:** And Marcelo is definitely more of like a VC-backed startup mindset.

**Daniel Lopes:** And that's why when I was like, okay, like, do I go bootstrap or do I go this?

**Daniel Lopes:** And then I met Marcelo, we go this.

**Daniel Lopes:** And the idea there was just like, can I figure out a way to automate everything that Marcelo can think of as fast as he can think of?

**Daniel Lopes:** And so that was the original idea.

**Daniel Lopes:** The like, can I...

**Daniel Lopes:** Rebuild IFTTT, but now with everything that's possible today and in actual language and be able to create systems that are as complex as this or even more, like an agent is way more complex than this.

**Daniel Lopes:** So that was the beginning, but always with the goal of like this bottom layer, it's more like, I'll show you the final thing here.

**Daniel Lopes:** The bottom layer, this is too complex to jump into immediately, but for me, the bottom layer is essentially an infrastructure layer.

**Daniel Lopes:** So you have, this is not the best representation, this one is better.

**Daniel Lopes:** So the way we think about it is that we have a three-part system where the bottom layer is our infrastructure.

**Daniel Lopes:** So there's essentially our AI workflow engine, where you can think of it like LinkChain or Maester is another one that's actually closer to what we've built that we're going to ship next month.

**Daniel Lopes:** And where you can...

**Daniel Lopes:** can create workflows, you can run them, and ideally, also have a place to deploy them, but it's all open source, and the benefit that you have is that you also get a lot of traces, so you can see end-to-end all the API executions, and you can let lose an agent to figure out how to improve things based on the output.

**Daniel Lopes:** They want to reduce costs, so you can look at all the trace and reduce costs there, and you're going to need all the different tooling for that, and we also have the idea of having a marketplace where you can deploy some of your workflows, and you can have people pay for them through API calls.

**Daniel Lopes:** We have, like, or seven core agents that do different things, so they could all be part of the marketplace, for example, and that's the color of thinking about the AI infrastructure layer, so to think of it, like, almost like an NN competitor, or, like, an Ops competitor, but it's code first, so you might have a GUI, but

**Daniel Lopes:** The UI is more to help you inspect what you wrote in code, but even if you don't write the code, you're starting with natural language, but under the hood, it's just writing code.

**Daniel Lopes:** So you can go as complex as you want, and all the code is also legit code, so you can have a programmer take over, improve, and add different packages, or improve the tracing and all that, and give it back to the marketer.

**Daniel Lopes:** Markers today, they're technical.

**Daniel Lopes:** They're not programmers, but they're all pretty advanced, so you can have people like Marcel and some of the other folks we have on the team, they can vibe code stuff, no problem.

**Daniel Lopes:** And if you make the environment a little easier for them to vibe code, then for sure they can be super effective, and you can pair them with Markers, kind of programmer, or me, and then we can take it to the other level.

**Daniel Lopes:** So that's how we think about this layer, and this layer, it's not only for Markers, it can be for anything.

**Daniel Lopes:** So we have clients like Office Zero, for example, Okta, where...

**Daniel Lopes:** We do like sales enablement for them.

**Daniel Lopes:** It's all our focus, but we can do it.

**Daniel Lopes:** So like the whole layer is pretty robust.

**Daniel Lopes:** So the plan, like the vision for this part is to like open source this month, see how well it does, if we can build a community around.

**Daniel Lopes:** And like all of our automations, all of our plants today are already using it.

**Daniel Lopes:** So it's almost like if we're getting paid to build this tool that we can now gift to the community and see if we can have it grow beyond what we do and continue to hire folks to improve it and have a forward deploy or like almost like a consulting arm for doing this kind of automation on top of our infrastructure.

**Daniel Lopes:** So that bottom layer, that's how we see it.

**Daniel Lopes:** It's kind of a long shot.

**Daniel Lopes:** It's not our first priority.

**Daniel Lopes:** Our first priority, that's more like a long-term goal.

**Daniel Lopes:** Our first priority is look at the agency.

**Daniel Lopes:** That we build and have them be our first client for a platform where somebody like Marcel can do what he did at DeepGram consistently.

**Daniel Lopes:** So you don't have to hire SEO agencies or outside agencies to be able to actually tap into the power of using some of those tools that we can do.

**Daniel Lopes:** Like you spent probably like hundreds of hours figuring out how to stitch together all this stuff in the last four or five years.

**Daniel Lopes:** Not a lot of people are doing that and it will take a while for all of them to do it.

**Daniel Lopes:** Can we get like a subset of those things that are common and productize and have folks use it?

**Daniel Lopes:** So things like, for example, like we're running the agency with like 60 something clients.

**Daniel Lopes:** are the things that they're all struggling with?

**Daniel Lopes:** Like we have all the workflows that we wrote and that the team that you join will continue to write custom workflows for certain things.

**Daniel Lopes:** They're parametrizing the agents we have and that kind of stuff.

**Daniel Lopes:** But there's also things on top of that that are repetitive.

**Daniel Lopes:** For example, setting up a Google Search Console or a Looker dashboard or a GA, that kind of stuff.

**Daniel Lopes:** Every client would be different if you don't normalize it.

**Daniel Lopes:** So we have a product that you have all the analytics integrated into one place.

**Daniel Lopes:** The visualization is the same.

**Daniel Lopes:** We just plug in your GA or your Fathom if you're using – if you're a company in Europe or something like this.

**Daniel Lopes:** We normalize the reporting.

**Daniel Lopes:** And then same thing with all your pages.

**Daniel Lopes:** So, like, we scrape all your pages and we create a catalog of all your pages so we can know, like, okay, this page here is, like, the content is too thin for the persona or the CTA is not really aligned with, like, the products that you sell.

**Daniel Lopes:** So we do, like, cement – we can do, like, semantic analysis on the pages plus all the usual.

**Daniel Lopes:** Mm-hmm.

**Daniel Lopes:** Core vitals or the kind of stuff that you do for SEO.

**Daniel Lopes:** And then we also have an entire place for like creating the contextual documents about the clients, like things like their personas, things about like the writing guidelines, that kind of stuff.

**Daniel Lopes:** How can we make those things be generated as close to usable as possible and then have humans do the final pass?

**Daniel Lopes:** So, but those are like all the things that we are like, as we run a content marketing team, they're all hitting different problems because we are like serving the 65 clients, like each pod performs in a different way, like then you normalize.

**Daniel Lopes:** So the goal like for us is to like have, we have the product today.

**Daniel Lopes:** So this is our internal product and then you can have here, for example, you have pages, for example, it's where we scrape all your pages and then you can see some of the issues and the matter.

**Daniel Lopes:** You can see...

**Daniel Lopes:** You can the content of the page.

**Daniel Lopes:** You can see some different things.

**Daniel Lopes:** We're going to add some things that are still missing here, but you can see the traffic of the page as well.

**Daniel Lopes:** You can see the Google Search Console.

**Daniel Lopes:** one is not set up.

**Daniel Lopes:** And you can see, and opportunities will be the insights or things that you can do with this page to perform better.

**Daniel Lopes:** Opportunities, we're still building, and assignments is essentially the work that the team is performing, almost like a chair or linear inside of the platform itself.

**Daniel Lopes:** So our goal is to have this platform here available for clients to use by first week of Federer.

**Daniel Lopes:** We're using it ourselves.

**Daniel Lopes:** The clients don't log in, so we just talk with it, essentially.

**Daniel Lopes:** But that's how we run all of our content work.

**Daniel Lopes:** So the goal is to have this platform here, be a standalone product that –

**Daniel Lopes:** Our content team operates, and then over time, give clients operation ability as well.

**Daniel Lopes:** And we are also working on a marketplace for, instead of you having to onboard writers and editors into every client, they receive the tasks with all the context that they need to know how to review or improve that article, or to fact check and all that, or to leave comments.

**Daniel Lopes:** If they're like, let's say you're writing for Office Zero, or Okta, or like a clerk, those are all clients that are like super technical.

**Daniel Lopes:** So essentially, you need like a security expert to review their articles.

**Daniel Lopes:** So like, how do you interact with these people?

**Daniel Lopes:** You can't just give them like Google Docs and have them like write the comments.

**Daniel Lopes:** And then like, now I lost the comment because it's a separate system where you can't improve the workflows and all that.

**Daniel Lopes:** And there's all the logistics of managing it as well.

**Daniel Lopes:** Like, hey, we have these comments, did you finish?

**Daniel Lopes:** And like, there's all these things that we're struggling with for that trying to operate the company.

**Daniel Lopes:** So it goes to close the loop.

**Daniel Lopes:** So you go from the content OS or the content creation platform for content marketing teams, starting with the external as us running it for the client and helping them become an internal content platform and having the marketplace for integrating with freelancers or experts and then having also the AI workflow automation.

**Daniel Lopes:** So like long-term vision, ideally, is that we close this loop and we have three, almost three independent products, plus all the forward deploy possibility that we can have on top of our own AI framework.

**Daniel Lopes:** So essentially four products that we see.

**Daniel Lopes:** I hope that makes sense.

**Tamyres Ogasawara:** Yes, does make sense.

**Tamyres Ogasawara:** actually have one question that is a bit more specific.

**Tamyres Ogasawara:** How do you see that, like,

**Tamyres Ogasawara:** A potential relationship with, like, Webflow, Framer, those type of, like, no code, no code, like, CMS.

**Tamyres Ogasawara:** Because I know that, like, for example, Webflow is launching a system for, like, AI, SEO optimization, and they did launch, like, a system of trying to prompt your page.

**Tamyres Ogasawara:** And I know that, for example, their content is not as good, like, likely not as good as, like, what we are able to do with a lot of what you are saying, because it's way, like, seems like a way deeper level.

**Tamyres Ogasawara:** But I got curious, kind of, like, how do you see the whole environment for this?

**Daniel Lopes:** Yeah, it's a fast-moving environment.

**Daniel Lopes:** Webflow is one of our top clients.

**Daniel Lopes:** They're also an investor on a smaller term, on the more of, like, a seed-level investment.

**Daniel Lopes:** And their CPO is also, like, a close.

**Daniel Lopes:** So we think we need to be, I don't know the long term.

**Daniel Lopes:** The long term, it's really hard to predict.

**Daniel Lopes:** The space is just moving so fast.

**Daniel Lopes:** But we're also building another product that we're talking, that they might use.

**Daniel Lopes:** So we're working on this AI visibility tool that it's more like an index of AI visibility, almost like a G2 crowd or like a SendRush for AI visibility.

**Tamyres Ogasawara:** Like a Profound?

**Daniel Lopes:** Yeah, a competitor of Profound.

**Tamyres Ogasawara:** The Profound is a normal SaaS.

**Tamyres Ogasawara:** have to sign up and create your own prompts.

**Daniel Lopes:** Ours is like SendRush, where we track all the prompts for you already.

**Daniel Lopes:** So when you sign up, you just see the data from the existing prompts, and you can add your custom prompts.

**Daniel Lopes:** But all the other prompts are essentially free for the subscription.

**Daniel Lopes:** So it's a public data set of prompts for your different categories.

**Daniel Lopes:** And

**Daniel Lopes:** And so, like, I can see us integrating with Webflow and others and providing them the data for prompt or amplitude and stuff like that.

**Daniel Lopes:** But for the content creation part itself, that second product that I showed you, the content OS, it will sit on top of CMSs.

**Daniel Lopes:** So, like, Strap is another client.

**Daniel Lopes:** Standity might become a client as well.

**Daniel Lopes:** So I think we want to integrate with all of them and feed them back the opportunities.

**Daniel Lopes:** So you could turn on self-publishing, and then you can operate and publish through their API.

**Daniel Lopes:** Or you can receive, if they end up creating, like, a really good place to receive, like, ideas, and then they would just generate the page, great.

**Daniel Lopes:** Then we don't have to do that workflow for every client because that part is painful.

**Daniel Lopes:** So the more integrated we can be with those CMSs, the better.

**Daniel Lopes:** And, like, we probably would integrate first.

**Daniel Lopes:** with integrated CMSs, CMSs, the the

**Daniel Lopes:** So well with Webflow, Strapi is also really close to us.

**Daniel Lopes:** They've been a client for more than a year.

**Daniel Lopes:** So probably Strapi and Webflow would be like direct integration, but I think they will struggle, like to be honest, like they're big companies, but they will struggle to get it right for like the level of the depth that some of this stuff would have to do.

**Daniel Lopes:** And we're probably better off integrating with us and we partner with them.

**Daniel Lopes:** And because this is not, this is not general purpose.

**Daniel Lopes:** Like if you have like a photographer or a small business owner trying to create a website and you get like a  ton of like geo optimization and SEO stuff in the mix and say, oh , like what is this?

**Daniel Lopes:** It's hard to make it easy to use, you know?

**Daniel Lopes:** But if you're like a sophisticated internal content marketing team, then you can do it.

**Daniel Lopes:** But I don't know if they will.

**Daniel Lopes:** navigate that part really well.

**Tamyres Ogasawara:** Yeah, so far, I think they have a lot of opportunities to address because I use myself, some of them, to kind of try and check it out.

**Tamyres Ogasawara:** That's why I'm with the question.

**Daniel Lopes:** Could it be familiar with that?

**Daniel Lopes:** Because we get a lot of clients that use, like we have a couple of folks from Frameware on the team as well.

**Daniel Lopes:** Yeah, so we're, we have a bunch of CMS overlap for sure there.

**Tamyres Ogasawara:** Yeah, for sure. It would be interesting to see how I'm also evaluating it.

**Tamyres Ogasawara:** Because I saw this, like, a kind of opportunity for integration.

**Tamyres Ogasawara:** Because a lot of tools that try to do what you are doing aren't good. They don't have the depth and maturity that you're showing.

**Tamyres Ogasawara:** For example, Search Atlas is one. I don't know, I haven't liked it too much.

**Tamyres Ogasawara:** I haven't liked too much, like, my experience with testing it as well.

**Tamyres Ogasawara:** So I think out of the ones that you mentioned, AirOps is likely the one that I liked the most, but still there are some limitations there.

**Tamyres Ogasawara:** So I was kind of crazy.

**Daniel Lopes:** Nico, the engineer on the cloud ops team, he was first engineer at AirOps.

**Daniel Lopes:** And we had a strong partnership with them for a while.

**Daniel Lopes:** Yeah, see them as one of our biggest competitors, though.

**Daniel Lopes:** kind of, they're taking a different approach because they have the graphic visual interface workflows.

**Tamyres Ogasawara:** Yeah, for sure.

**Daniel Lopes:** I personally hate that, if you can code, because, like, it's fun to prototype stuff super quick, but I ended up, I ended up being, like, a lot faster for much more complex stuff.

**Tamyres Ogasawara:** didn't call it code, you know, so like, why am I doing this?

**Daniel Lopes:** I see your point.

**Tamyres Ogasawara:** I can't agree.

**Tamyres Ogasawara:** I can't agree now.

**Tamyres Ogasawara:** Like when I started off, of course, it's very helpful to have something like visual, but now that like on the last like six months-ish, when I started to be a bit deeper into coding, then I started to like also be a bit more biased of like some things are way more flexible in coding than having to do a lot of like nodes.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That would be one thing that I hope that we can do well.

**Daniel Lopes:** It's just like, especially building up this team, now the client ops team, would be to have you all help us make that environment as easy as possible for like, let's imagine like you like six months ago or like one year ago before you started like vibe coding things.

**Daniel Lopes:** What do we have to do to like, is it documentation?

**Daniel Lopes:** Is it like the better user interface?

**Daniel Lopes:** Is the better commands?

**Daniel Lopes:** To run things properly, like maybe it's terminal first, but then like, do you have like a web version after?

**Daniel Lopes:** Like, that is the part that I'm like, that I want us to like close the loop.

**Daniel Lopes:** And that I think will happen for sure.

**Daniel Lopes:** And it hasn't happened yet.

**Daniel Lopes:** And you see things like Vercel just launched a workflow framework that is closer to how we were thinking, but they're thinking more engineers.

**Daniel Lopes:** And I want us to make it more like general purpose, knowledge worker, accessible, you know?

**Daniel Lopes:** So, yeah, but there's definitely competitors everywhere.

**Tamyres Ogasawara:** So that's the stuff that keeps me awake at night.

**Tamyres Ogasawara:** Competitors and also potential partners because like overlap could be competitive, but could be like compulsory.

**Tamyres Ogasawara:** So, yeah.

**Daniel Lopes:** I see like Webflow, Strapi, all the CMSs as partners.

**Daniel Lopes:** And I see our ops as a potential competitor.

**Tamyres Ogasawara:** Yeah, for sure.

**Tamyres Ogasawara:** When you mentioned it, I think.

**Tamyres Ogasawara:** Yeah, I think this was my main question, honestly.

**Tamyres Ogasawara:** I love to talk with you.

**Tamyres Ogasawara:** I think your vision is pretty cool.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** Yeah, cool.

**Daniel Lopes:** I'll chat with Tucker and the rest of the team today and follow up with you probably today or tomorrow morning or something like that.

**Daniel Lopes:** But I really appreciate it.

**Daniel Lopes:** Where did you learn English?

**Daniel Lopes:** Because your English is so good.

**Daniel Lopes:** I had to move out here to get better.

**Daniel Lopes:** Have you lived abroad?

**Tamyres Ogasawara:** I learned by myself.

**Tamyres Ogasawara:** No, I learned by myself.

**Tamyres Ogasawara:** Studying and I had some friends that were from Canada when I was younger.

**Tamyres Ogasawara:** So I also talked a lot to them while I was learning by myself.

**Daniel Lopes:** But it was 90% self-learning, I would say, for sure.

**Daniel Lopes:** Nice.

**Tamyres Ogasawara:** Congrats.

**Tamyres Ogasawara:** That sounds great.

**Tamyres Ogasawara:** you.

**Tamyres Ogasawara:** I appreciate it.

**Tamyres Ogasawara:** I really appreciate it.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** Thanks for your time.

**Daniel Lopes:** And we'll

**Daniel Lopes:** Well, for sure, we'll definitely make an offer.

**Daniel Lopes:** I just need to calibrate everything with the rest of the team.

**Daniel Lopes:** But yeah, like super impressed by your background, super impressed by how you've executed on the tasks.

**Daniel Lopes:** And I'm excited to have you potentially joining us.

**Tamyres Ogasawara:** All right.

**Tamyres Ogasawara:** Yeah, I appreciate it.

**Tamyres Ogasawara:** Thank you so much, Daniel.

**Daniel Lopes:** Cheers.

**Daniel Lopes:** Bye.
