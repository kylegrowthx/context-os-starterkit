# Checkthat Overview

<metadata>
date: 2025-11-26
time: 19:00 UTC
duration: 37 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Talal Syed
fireflies_id: 01KAWE62M41R6PPXWZSY9VX2D5
transcript_url: https://app.fireflies.ai/view/01KAWE62M41R6PPXWZSY9VX2D5
</metadata>

---

## Summary

Marcel and Talal discussed the strategic vision for CheckThat, a B2B software platform designed to separate AI behavior change from analytics visibility tools. The platform focuses on creating comprehensive brand summaries and comparison pages for B2B products through standardized category frameworks and prompt methodologies. Key challenges include high data collection costs ($200K monthly at scale), urgent prompt uploading for critical clients like Augment Code and Lovable, and SEO indexing issues that must be resolved. Talal will lead prompt uploads and develop unified generation methodologies to avoid duplication and ensure quality, with emphasis on evaluation and comparison funnel stages over awareness and post-purchase.

---

## Action Items

**Marcel Santilli**
- Re-add Talal Syed to CheckThat Notion doc and adjust access permissions after recent export incidents
- Confirm bug fixes and setup for prompt uploading and execution workflow within CheckThat; establish process for reporting issues through Linear
- Assist Talal with creation and management of tagging and view features to better organize prompts and workspaces
- Advise on SEO strategy and technical setup to ensure pages are indexed and appropriately optimized
- Facilitate ongoing internal coordination and respond to CheckThat channel queries related to platform

**Talal Syed**
- Review and upload all prompts related to high-profile clients such as Augment Code and Lovable into CheckThat workspaces immediately to start data collection
- Coordinate with Jason and Andy to identify key clients for prompt uploads and tracking prioritization
- Implement AI-driven persona methodologies to generate company-specific prompts aligned with categories, avoiding duplicated efforts
- Document and refine prompt-making methodology to ensure consistency and optimize prompt generation across clients and categories

**Unassigned**
- Continue hiring and consulting with data scientists like Katya to advance predictive modeling and correlation studies for AI answer quality
- Develop scheduling heuristics for probe frequency and cost optimization

---

## Transcript

**Marcel Santilli:** Hello, my friend. How's it going?

**Talal Syed:** Hey. It's going well. How about you? So glad to finally meet you.

**Marcel Santilli:** Yeah, yeah, you too. I'm hearing great things about you. Said you're here and helping us, and part of this. Man. How has it been so far for you?

**Talal Syed:** It's been great. Super interesting to see things in person. Like, I have been an admirer of GrowthX from a distance for a while, so it was really good to see we work together. So pretty excited.

**Marcel Santilli:** That's really cool. How did you first run into us out of curiosity?

**Talal Syed:** LinkedIn. I think you were pretty prolific on LinkedIn, just like sharing progress, building in public. Then you guys started doing a lot of workshops and I knew Jason just from LinkedIn as well, so I had lots of little touchpoints for you guys.

**Marcel Santilli:** That's really cool. Yeah, it's so funny because on the downside of building publicly, I see some of our competitors fundraising and then literally copying how we talk about things like Air Ops and others. They didn't even used to use the word context and now they're using the word context for everything. But on the flip side, there's so many people now like, man, I really want to work with you all in some capacity. And it's really, really cool. We just gotta keep moving fast, you know, because if you're building public, you better be moving fast because everybody knows everything you're doing all the time.

**Talal Syed:** I feel like it's built a lot of trust in the market for GrowthX, so I would see it as like a net positive, at least from my lens.

**Marcel Santilli:** That's awesome. And that's good to hear. Cool. Well, we'd love to spend some time and just take you through how we're thinking on CheckThat and the work we've done so far, and find ways to get you as involved as possible. Maybe we can start with the big picture. Have you had a chance to read the overview doc for CheckThat?

**Talal Syed:** If it's the one you shared in Notion a few days ago, then I did go through that.

**Marcel Santilli:** Okay, cool. I just dropped the link, but I think my access got removed again recently. So let me re-add you. We had some incidents where folks from the delivery team, after leaving, exported our entire Notion and shared with competitors. So I've been restricting access to strategic docs. Most editors don't need that information anyway.

**Talal Syed:** Okay, that makes sense.

**Marcel Santilli:** So at a high level, the main issue with how AEO is happening right now is that there are like 163, 164 vendors, and they're conflating the behavior change happening due to AI as a fundamental technological shift with just an analytics tool—essentially a visibility tool. And Profound was smart to create that narrative. But they're very different things. What we're trying to do is separate the two. One is human behavior driven by technology like ChatGPT. That's real and true. But many of these visibility tools are just BS—like expecting everyone to run their own research from scratch to figure out who's winning. It's like asking every city to run their own election research instead of using standardized polling. So what we're doing is standardizing that a little bit more. We know it's not perfect science, but it's way better than the alternative.

**Talal Syed:** That makes complete sense.

**Marcel Santilli:** So when you think about the different stages of the funnel, there's awareness and advice, then evaluation, then comparison, then decision, and post-purchase. We decided to focus on B2B software first—that's most of our companies. Then we defined buying categories. G2 has like 1,200-1,500 categories. We did a whole exercise to come up with meaningful ones. And we're creating the best questions that represent each category at each funnel stage. We're also studying the correlation between substance and citation likelihood to build a predictive model. Katya, a data scientist, is consulting with us on that. We're actively hiring more data scientists too.

**Talal Syed:** That's cool.

**Marcel Santilli:** So most brands coming in have to figure out questions from scratch, which is silly. The second problem is they're starting data collection from zero. So what we're doing instead is saying, look, we're already collecting data. For example, we've done 128 probes on this category. If you sign up, you should be able to just add a shared library to your tracker and get all this data already.

**Talal Syed:** Right.

**Marcel Santilli:** But here's the challenge. This is expensive. It's about $0.06 per probe across all our services. If you're doing 1,200 categories, 100 prompts per category, probing daily across five or six services, you're looking at about $200K monthly. That's significant. So the key is making sure these questions are the best questions for each category. We prioritize the categories people actually buy from. Over time, we'll put some on different schedules—maybe every other day instead of daily, some weekly. We'll weight certain probes higher than others.

**Talal Syed:** That makes sense.

**Marcel Santilli:** For brands, the cool thing is our context generator is really, really good. If you look at LangChain, our workflow generates this context and creates a summary that's way better than what you'd get from Scrunch or others. And we're trying to create an SEO play. Semrush figured out the data moat but never did the SEO play. Crunchbase did. G2 did. We can't afford to buy clicks for B2B SaaS tools now that they're costing $20 a click. But because we're making this data available, if we can have the surface area of brands and categories, then we create a massive moat. So we could rank for things like "LangChain pricing," "LangChain alternatives," etc. We become the best answer source and eventually become a judge of which AI service is giving the best answer. End users can see, "Cloud versus Gemini versus ChatGPT versus OpenAI, which has the better answer for MLOps platforms, and which ones are missing things?"

**Talal Syed:** I think this also provides a pretty big moat if you turn this into research and studies. Not many companies are going to run large-scale experiments costing $100K+. So if you want to target companies in dev rel space, we could create a report using six months of data and do targeted outreach. Just makes sense.

**Marcel Santilli:** That's a great idea. Yeah, you can come up with key insights and things like that. But here's the challenge—we effed up some stuff and none of the pages got indexed. I don't even know if they're indexing yet. So that's a big thing for us to solve. On one end, we need to set this up for success so it's truly an SEO play. What are the technical things we should do? Is our strategy correct? Right now, the H1 is "What are the best MLOps platforms?" Is that right? Or should it be categories or brand pages? There's a lot of that.

**Talal Syed:** Right.

**Marcel Santilli:** On the other end, we need a strong opinion and thought process on how we create the right questions. I saw the doc you started writing on that. Then we form a strong public opinion and dogfood the crap out of our own tools. The idea is we have different funnel stages, and we're trying to make this internal experience seamless. It's mostly working—just need to improve so we can add prompts, run probes, catch issues, and validate. The goal is to validate with a couple of customers first and work through rough edges. Once we feel good, we can give customers access. Then after a week or so, we can tell the whole world. Because the second we start promoting this heavily, it's going to hurt our relationship with Scrunch and others, and they might kick us off their platform. If our customers don't have all their data here and it's not collecting, then we lose what we're delivering.

**Talal Syed:** So we work really closely on finding a place to upload prompts, document thinking, load workspaces, starting with critical customers like Augment Code and Lovable, because they want to promote CheckThat?

**Marcel Santilli:** Exactly. Then we build workflows and iterate on them. We need to auto-generate a lot of these questions too. The admin panel is way more feature-rich than the public interface.

**Talal Syed:** Just a random question. Eventually, do we want to set up all clients within CheckThat? I know we had requirements for Augment Code where we needed prompts right away and duplicated work. So that merger is happening sometime soon?

**Marcel Santilli:** The way I see it, every day we don't put prompts for our customers in here is a day we're not collecting that data. It's less about what you're showing them, it's more about if you came up with a thousand prompts—hopefully less—we should just put them all in here and make sure it's working. How we tag it, visualize it, show it can evolve easily. But if we're not collecting data, you can't go back in time. We won't be able to export data from other places like Scrunch. It's going to be really messy. So this is urgent. For instance, we've done high-profile client work for Augment Code and Lovable. We should upload all those prompts now. Start collecting data now.

**Talal Syed:** One other question. I looked at the documentation on how prompts are being populated. They're being populated at a subcategory level. My question is how do we do it for a particular company? There are prompts relevant to their category, but some are only relevant to them as a company. So there are definitely some that are going to be relevant to that particular product category, but there are going to be some that are only relevant to them as a company. So we also want to populate those. I don't know if we have a way of generating those right now, and that seems like the biggest blocker to uploading prompts.

**Marcel Santilli:** Yeah. So let's take Ramp as an example. You should be able to come in here and add custom prompts and select the funnel stage. I noticed the ones I uploaded yesterday haven't run, so I need to double check why. We'll be able to create tags too. But just getting all the prompts in here will be a huge help. Come up with prompts, you can overdo it if needed, and it should be fairly easy. Copy and paste them per line, organize by funnel stage, create prompts, and it should work. We're going to find bugs though. There's one with line breaks that's creating issues. I flagged it. We can give feedback to the team through Linear later.

**Talal Syed:** Question about methodology. The main problem is that if you take 10 different people, they'll come up with 10 different prompt sets. We really need an informed opinion on how to design custom prompts. Every board is doing it a different way. Some use Scrunch, some use ChatGPT or Claude. What have you already thought through? What's the best practice flow for creating prompts for subcategories? How can we apply that to individual companies so we don't duplicate work?

**Marcel Santilli:** Yeah. So fundamentally, I think the way to think about it is understanding the audience. We had to focus on category first because it was really hard to do audience-based questions. But audience-based questions make a lot of sense as a way to seed the right questions. So like, jobs to be done, questions about skills, backgrounds. Different work products they need. When you get into awareness and advice, there's a lot of that. That's the internal side—KPIs, metrics they care about. That's going to drive content strategy. Then external things—terminology, definitions, tools, templates, how-tos. That's the big picture on how to come up with questions. For each funnel stage, come up with a set of questions, but focus on higher intent and work backwards. If you start too broad, what value are you getting? So for instance, I did this for Ramp for the CFO club project. A finance manager at a fast-growing B2B startup. Based on that, write a job description. Think through their fears. What gets them fired or promoted? Who do they work with? Within that context, what are all their questions around their job? Questions like: how can I automate financial reporting? How do I prepare a 409A evaluation? Who should I benchmark? How should I model sales capacity planning? What's the standard SaaS metrics dashboard? How do I calculate working capital requirements? What should my month-end close checklist be? These are really good, high-quality questions. Then you can go into Perplexity and type this in. But I don't know if there's value tracking this. There aren't many brands mentioned. So that's more like just surfacing opportunities. Whereas further down the funnel, evaluation prompts, you can see accuracy. Like, do we have good post-sales answers? But teams we work with don't care much about post-sales. So evaluation is really important. Maybe we create comparison ones. I don't know how much value awareness and advice tracking have if there's no brands mentioned.

**Talal Syed:** Yeah. For awareness, I think it's a one-off thing. The only thing we need to track is if a brand shows up as a cited source. If they see us mentioned when looking for solutions they might need a year down the line, it builds some trust. But the ROI isn't there.

**Marcel Santilli:** Right. And it's driving traffic, but won't be mentioned much. Sometimes it does, but it's very minor.

**Talal Syed:** Similarly for post-purchase, I don't think it makes sense either. Evaluation and comparison is where the money lies. And I've been doing it like, taking context artifacts, feeding them into Claude, creating a digital twin of the persona, then asking questions across specific features. If you were this persona and wanted this feature, what's the impetus to search for this? What language would you use? The results have been good.

**Marcel Santilli:** Yes. So we can take that and create different workflows that could generate those questions. Yeah, so I think the most important thing is to load up all the questions, even if you're unsure about usefulness. Get them into workspaces and make sure customers have access. Start with Augment and others. Get it loaded up and working. We can figure out tagging and views as we go. We'll work through bugs in the process. The time-sensitive thing is just get all the prompts loaded. It's okay if we archive them later or run differently. I'd rather spend a couple grand on wasted probes but have the optionality to have that data in the next 30 days than not have it and be like, oh, we wish we had that question sooner.

**Talal Syed:** Yeah, that makes sense. So Augment Code is one I can check with Jason and Andy. What are the high-profile clients we have that I want to set up immediately?

**Marcel Santilli:** Yes. And set up those workspaces, create prompts, load them up so we start tracking them.

**Talal Syed:** Cool. Awesome. Sounds good. I gotta run. But let me know if you think of anything else. Feel free to drop questions in the CheckThat channel and tag me. I'm fairly involved with this one, but I'm really excited to have your help.

**Talal Syed:** Thank you so much and have a great rest of your day.

**Marcel Santilli:** Yeah, yeah, you too. And let's find time for you to come out to SF. I don't know.

**Talal Syed:** Yeah, definitely. I'm actually going to Pakistan for my sister's wedding tomorrow, so I'll be back early January.

**Marcel Santilli:** Well, enjoy that. That would be a very happy time. One of those that takes several days to celebrate. Intense celebration.

**Talal Syed:** But when I'm back, I'm definitely going to fly and meet the team in person as well.

**Marcel Santilli:** Yeah, I love that, man. All right, well, enjoy your time, brother.

**Talal Syed:** Take care.

**Marcel Santilli:** Bye.

---

## Key Themes

- **Market Differentiation:** Separating AI behavioral change from visibility/analytics tools; positioning as standardized category-based research platform
- **Data as Moat:** Using large-scale experiments ($100K+ monthly probe costs) to build unique research insights unavailable to competitors
- **SEO and Content Play:** Creating brand summaries and category comparison pages to rank for high-intent B2B software queries and become the authoritative answer source
- **Cost Optimization:** Probes cost $0.06 each, potentially reducible to $0.03; prioritizing categories and scheduling to manage $200K/month burn at scale
- **Urgent Data Collection:** Emphasizing immediate prompt uploads for critical clients (Augment Code, Lovable) to capture data; cannot backfill historical data
- **Unified Prompt Methodology:** Need standardized process using persona-based framework (role, jobs, fears, KPIs) applied across subcategories and company-specific contexts
- **Workflow Validation:** Testing with pilot customers before full market promotion to avoid damaging Scrunch partnership and ensuring platform stability
- **Funnel Focus:** Evaluation and comparison stages highest ROI; awareness and post-purchase lower priority due to minimal brand mentions
