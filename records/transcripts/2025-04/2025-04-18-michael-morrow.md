# Michael Morrow

<metadata>
date: 2025-04-18
time: 21:33 UTC
duration: 26 minutes
organizer: Jason Gong (GrowthX)
participants: Michael Morrow (external), Jason Gong (GrowthX)
fathom_recording_id: 58135247
fathom_url: https://fathom.video/calls/279907892
share_url: https://fathom.video/share/cnqgwMiskiKsMD7ASsRaaYnSz4ojguys
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

Jason Gong explored Michael Morrow's background in customer operations across growth-stage and large enterprise environments to assess his fit for building GrowthX's post-sale customer success infrastructure. Michael discussed eight years of experience at Avanti Markets, Ignite, and F5, including health scoring models, CSM automation, and customer journey optimization, while Jason contextualized GrowthX's need to scale from delivering outcomes-as-a-service rather than standalone AI tools. Both parties expressed mutual interest, with Michael energized by GrowthX's growth-stage environment and Jason impressed by Michael's technical aptitude and philosophy on building systems from first principles.

---

## Context

Michael Morrow is a potential hire being evaluated for a customer operations role at GrowthX. Jason Gong, who leads GoToMarket at GrowthX (managing client relationships with Webflow and Abnormal Security while also driving growth initiatives), conducted this exploratory conversation through Bridget's referral. GrowthX is currently operating without dedicated post-sale CRM infrastructure—they use Attio for sales but lack tooling to monitor remote team performance and track customer health signals in real-time. The company is building an "agency for the age of AI" that delivers outcomes-as-a-service rather than shipping AI tools directly to customers, which mitigates hallucination and oversight risks that plague self-serve AI products. This meeting was an opportunity to find someone who could help define GrowthX's customer operations needs and implement an appropriate system from the ground up.

---

## Relevance

- **To GrowthX Delivery:** Michael's expertise in building multidimensional health scoring models (10 models at Ignite), customer journey mapping, and CSM automation (especially QBR automation via Matic) aligns with GrowthX's need to scale delivery without proportionally scaling headcount. His technical depth (Gainsight implementation, data pipeline work, integrations) and preference for first-principles thinking match GrowthX's approach to building systems. Michael's experience working with 90-person global CSM teams at F5 is directly applicable to managing GrowthX's expanding remote teams.

- **To GrowthX Business Development:** Candidate demonstrates strong cultural and capability fit for a growth-stage environment—explicitly prefers smaller companies (15-35 people at Avanti, 800-1000 at Ignite) over enterprise bureaucracy (disliked F5's lack of strategic input). Michael is energized by AI-native companies doing outcome-driven work, and his entrepreneurship background (master's degree, taught entrepreneurship, advisor roles) suggests potential for expansion work beyond ops.

- **To Hiring:** Michael's story shows deliberate progression (startup operations → data/tooling focus → enterprise scaling) and clarity on what motivates him (autonomy, collaborative problem-solving, growth stage). His skepticism of AI-only tools (cited hallucination risks, airline chatbot discount example) aligns with GrowthX's philosophy. Next step: define specific customer ops role scope and responsibilities, then technical deep-dive on Attio + Gainsight architecture.

---

## Overview

- Michael has diverse experience in customer operations, from startups (Avanti Markets) to large corporations (F5), with a strong preference for growth-stage environments
- GrowthX is seeking someone to help set up and optimize their post-sale customer operations, including selecting and implementing appropriate tools
- Michael's technical aptitude and experience with CRM/CS tools (e.g., Gainsight) align well with GrowthX's needs
- Both parties expressed mutual interest, with Michael energized by GrowthX's growth stage and AI-focused approach

---

## Key Topics

### Michael's Professional Background

  - Master's in entrepreneurship, ran small ventures during studies
  - First role at Avanti Markets (15 to 35 employees):
      - Built new product line (hardware + SaaS)
      - Touched all aspects of the business
  - Ignite (800 to 1000 employees):
      - Focused on data, integrations, and CS tech stack
  - F5 Networks:
      - Program manager role, less strategic than anticipated
      - Built customer journey for SaaS product (DDoS protection)
      - Worked with 90-person global CSM team

### GrowthX's Current Situation

  - No dedicated post-sale CRM, using Attio for sales
  - Challenges in monitoring remote teams' performance
  - Seeking help to understand needs and set up appropriate systems
  - Delivering outcomes as a service, not just AI tools

### Customer Success Tools and Strategies

  - Gainsight described as the "Ferrari of CRMs" for CS
  - Michael's experience with health scoring models:
      - Built 10 multidimensional health models at Ignite
      - Limited input on health scoring at F5
  - Automation within CS tools:
      - Building call-to-actions, tasks based on specific parameters
      - QBR optimization using AI tool Matic

### AI in Customer Operations

  - GrowthX focusing on delivering outcomes, not just AI tools
  - Challenges of AI hallucinations in customer-facing scenarios
  - Importance of human oversight in AI-driven processes

---

## Action Items

- Michael to follow up with any additional questions
- Potential further discussions on specific role and responsibilities at GrowthX
- GrowthX to evaluate Michael's fit for their customer operations needs

---

## Transcript
**Michael Morrow:** I've got friends that live in Oakland.

**Jason Gong:** It's honestly so nice. I'm Canadian originally, and I moved here like seven years ago, and I would almost never come to Oakland. Then when we're looking for a longer-term place to stay, we came here and were like, holy crap.

**Michael Morrow:** It's a cool spot. I like how close it is to SF, but it's not in SF, and you're not dealing with SF things.

**Jason Gong:** It's a nice blend between here and LA in my head. Well, it's really nice to meet you. You know, Bridget shared some context. Maybe I could just give a quick intro, but we'd love to hear more about you.

**Michael Morrow:** Sounds good.

**Jason Gong:** So I lead GoToMarket at GrowthX, which is essentially two parts. One part, I have kind of a book of clients—some of the bigger ones you might have heard of, like Webflow and Abnormal Security—and I have a few smaller startups. And then the other half is to grow GrowthX itself, both from top of funnel, which is more on the marketing and sales side. The main reason I have some clients is to figure out how to make that more efficient. And a big part of that is at GrowthX, we're really trying to build like almost a kind of agency for the age of AI. The ways agencies are run today doesn't really make sense now with AI. Part of why we wanted to talk to you is—what's exactly breaking when you have three people handle 10 clients instead of five? And how do you make that scalable with automation? Sometimes it's not even AI.

**Jason Gong:** My background is go-to-market growth, leading that for tech companies. I've been at startups like Kite and Bardeen, and led growth at Firm (you'll see them at Peloton checkout). I also had my own startup, a YC-backed dev tool startup that folded. I joined GrowthX after meeting Marcel at an event—I was their number one power user of an AI tool called Aerofs at the time. It seemed like a no-brainer.

**Michael Morrow:** Thanks for that background. Sounds like you've got a lot of different flavors throughout your career.

**Jason Gong:** Yeah, that's why it helps to be here. There's a lot of figuring things out from first principles, which really excites me about this role.

**Michael Morrow:** I've worked with big companies for the past few years, but I wanted to get back to my entrepreneurial roots. I moved to Washington for my master's in entrepreneurship, studied how to start companies and build from the ground up. I ran a dog services company out of my apartment while studying to get my feet wet with documentation and taxes. After graduation, an adjunct professor from the program joined a local company and brought me on as his right-hand man to build a new product line. This was about eight years ago, at Avanti Markets.

**Michael Morrow:** At that point, customer success was a very new concept. We dove into the deep end, building a completely new product line—a hardware and SaaS mix. I had to learn networking, cabling for the hardware, and support a SaaS backend, introducing it to a team that had only worked with on-premise solutions. I touched every angle of the business: marketing, product, engineering. After three years, they got acquired by 365 Retail Markets (they sold unattended retail kiosks). My boss was deemed redundant, so I looked for something new.

**Michael Morrow:** I wanted to dive deeper into data and what supports good customer operations. Integrations, data pipelines, different warehouses, dashboard builders like Tableau, Gainsight, Tatango. That gave me exposure to the foundational tech stack work. It all culminated in my last role—a program manager role at F5. I thought it would be more strategic, but there were a lot of leaders at the table. I didn't really have a voice and wasn't being utilized to my best value. It was too administrative for what I was looking for.

**Jason Gong:** When you were at Ignite, how big was that company?

**Michael Morrow:** Ignite went from 800 when I started to 1000 while I was there. Pretty good growth. Avanti was much smaller—15 people when I started, 35 when they got acquired.

**Michael Morrow:** For me, the preference comes in with team size and growth stage of the company, not the product. I'm really good with creative and critical thinking and collaborating. Any place where I can sit at a table with smart people and strategize and build solutions from the ground up, that's where I'll thrive. At F5, all the tools were already decided and I couldn't influence the workflows. I had no leverage to say, "Maybe there's a better way for us at this scale and size."

**Jason Gong:** I was also part of a company that got acquired and said, nope, this is not what I'm interested in.

**Michael Morrow:** I want to get back to my entrepreneurial roots.

**Jason Gong:** For sure, GrowthX is that. We're spinning up new work streams that could be companies in themselves. We do that literally every week.

**Michael Morrow:** That's exciting.

**Jason Gong:** Is there any customer ops project you've done recently that relates to what we're struggling with?

**Michael Morrow:** Hard to tell without being in the business, but at F5, one of my larger programs was building out the customer journey from pre-sales through renewals, upsell, and expansion. Working within their contract cycles (one or three years), understanding optimal deployment time and metrics for successful onboarding.

**Michael Morrow:** At F5, I did this for their SaaS product—DDoS protection. They introduced a SaaS suite about three years before I left. The past year I was there was a huge growth year. They wanted to shift 80% of customers to SaaS and move them off the on-premise solution they'd started with.

**Michael Morrow:** The SaaS product was predominantly DDoS protection, very similar to Cloudflare. It also had an anonymizer in the token chain. The big thing was having an online platform—a web app dashboard where customers could view stats, configure changes, and see attack patterns by country. The older on-prem solution required customers to work with an engineer internally for those numbers.

**Michael Morrow:** At F5, it was taking stock, auditing what currently exists, figuring out what's noise, what can we replicate. It was about automating as much as we could for the CSM team throughout the customer journey. Whether automating QBR decks using Matic (an AI tool—it's in my top five CS tools now), or reporting performance of CSMs across the globe. I worked with a 90-person global CSM team.

**Michael Morrow:** It was as granular as working with engineers in India to build data designer features in Gainsight so data flowed properly into metrics, reports, and dashboards. And as high-level as communicating how the program aligns with leadership expectations. I worked hand-in-hand with CSMs, their managers, our tooling team, and communicated upward to leadership. This was basically my only focus for about six months.

**Jason Gong:** What's Gainsight?

**Michael Morrow:** Gainsight's like the Ferrari of CRMs. It's a CS tool through and through. Everywhere I've gone that has a CRM has a Salesforce instance too, and they're connected. Deal and opportunity information comes into the CS tool so CSMs have more context when there's a handoff. And you build automation within Gainsight—call-to-actions, tasks that alert CSMs based on specific parameters like churn indicators or health score changes.

**Michael Morrow:** At F5 I didn't have as much input on health scoring as I wanted. That plays into my complaint about not having a seat at the table. But at Ignite, absolutely. We built 10 different multidimensional health models using their CRM, Tatango. The team strategized around what markers of good health we used, how to weight them, then they'd flow through a waterfall system—if a customer hit churn criteria at the top of the funnel, that was the priority and they couldn't even get a health score for other things. Very involved with strategy and tooling.

**Jason Gong:** That's the stuff we struggle with. We don't even have a CRM for post-sale. We just have one for when we're trying to sell. We're trying to use Attio for post-sale, but I don't know if it's the right tool.

**Michael Morrow:** I haven't heard of Attio. I'll have to look that up.

**Jason Gong:** A lot of our challenges are that we have remote teams doing something that normally any agency or company doesn't do. They're using a weird suite of tools, working in weird ways. To catch underdelivery on customer A before the customer starts flagging it is challenging because bringing those signals together and making an assessment is hard.

**Michael Morrow:** You'd have to do A-B testing so you don't get false flags and red herrings.

**Jason Gong:** Yeah, it's a pretty ambiguous space. We're kind of just looking for somebody who can come in to help us understand what we need and then set it up.

**Michael Morrow:** That sounds like an exciting opportunity. I did a lot of this kind of stuff around my entrepreneurship program—business plan competitions, pitch competitions. I was a coach and judge for multiple years with Seattle U and University of Washington, working with students on early-stage ideas. How would you scale this if you got funding? How would you pitch to investors? I took on some advisor roles and was very involved in the young professional community here in Seattle. I worked on their board, did operations, hosted networking events and meetups. There was a lot more energy before COVID around tech startups.

**Jason Gong:** That community is super important. Your network makes you.

**Michael Morrow:** Definitely.

**Jason Gong:** Did you have any questions for me? I'm an open book, happy to share anything. How do you like it at GrowthX?

**Michael Morrow:** How do you feel about the company?

**Jason Gong:** I definitely like it. Before GrowthX and my own startup, I built a lot of tools that weren't necessarily for me—coding tools, dev tools, security tools. At GrowthX, finally, what I've been doing for myself throughout my career—building tools, automating things, using the technical side of my brain alongside the business side—is being used. It's a place where I can be myself and everything's getting used. We're part of GrowthX's brand, which feels great.

**Jason Gong:** As a company, I think they've gotten so many things right. With AI, I was at an AI company before, back in 2018. When you build tools for people to use, you're often giving them something they can shoot themselves in the foot with. It's a lot of work to use something well. What GrowthX gets right is the product isn't that tool. It's irrelevant what tool we use. We're delivering an outcome in the form of a service. Because we've made that decision, it makes go-to-market so much easier. We don't have to juggle making AI do something it's not ready for.

**Michael Morrow:** On that note, I read a headline today about Cursor AI—a support agent AI—that served a hallucinated policy to someone trying to get support. He produced something for his company based on a fake policy, and now there's a lawsuit. It's shooting yourself in the foot.

**Jason Gong:** I've heard in Canada that one of the airlines used AI in their support chat and hallucinated a discount that didn't exist, and they had to honor it.

**Michael Morrow:** Yeah, exactly. It's good to hear that GrowthX is really a team of people behind it rather than some developer making an AI do too much.

**Michael Morrow:** It definitely sounds like it's more about the client relationship and optimizing internal workloads that support that relationship.

**Jason Gong:** I think there's a version of the world where instead of self-serve SaaS, you're kind of hiring a person. Whether that person is a real person or some mishmash of AI and people, it doesn't matter to you. You hired them for a job and how well they do it is what you're paying for.

**Michael Morrow:** And right now, if people aren't keeping up with AI and the progress, they're falling behind. It's so exponential. I use OpenAI every single day—for shopping lists, workout plans, D&D theorycrafting for my Dungeons & Dragons group. It's really capable where it's supposed to be capable.

**Michael Morrow:** It sounds like a really cool environment. I'm energized by early stage and growth stage companies.

**Jason Gong:** Yeah, I really enjoyed speaking with you. Your comments about being a more technical person resonates too. I'm way more technical than most CS ops people I work with. There's a lot of people-skill folks in CS, but then they get on a computer and don't know how to copy and paste properly. It's pretty crazy how technically adept people should be and aren't.

**Jason Gong:** If somebody tried to make an AI-enabled CS tool, great, but then you give it to people not accustomed to thinking in systems. That's where problems arise. There's a training and accessibility component.

**Michael Morrow:** I had a colleague who was the digital campaign guy and he right-clicked everything, used context menus for everything, no keyboard shortcuts, no efficiencies. He had 60 tabs open at any given moment. You're our digital guy, the guy designing the digital experience for our customers, and something's going to break there.

**Jason Gong:** The externality of all this AI stuff is that when you figure out how to automate things, people can't adapt the way the people building can.

**Michael Morrow:** Yeah, exactly. That's why I try to stay on top of everything.

**Michael Morrow:** Thanks for your time, Jason.

**Jason Gong:** And if you have any questions, feel free to ping me.

**Michael Morrow:** Sounds good.

**Jason Gong:** Appreciate it. Have a good weekend.

**Michael Morrow:** Likewise. See ya.
