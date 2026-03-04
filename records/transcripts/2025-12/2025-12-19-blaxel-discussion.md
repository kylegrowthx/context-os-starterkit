# Blaxel discussion

<metadata>
date: 2025-12-19
time: 17:52 UTC
duration: 15 minutes
organizer: william@growthx.ai
participants: Aida Knezevic, Kathy Lam, William Leborgne
fathom_recording_id: 110127103
fathom_url: https://fathom.video/calls/513216485
share_url: https://fathom.video/share/VkjX2-juUzBj5v5h7mTyf2cLz56g-TAF
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Aida presented a new AI-assisted workflow for creating content topic clusters for Blaxel, demonstrating how Claude can be used for data analysis while maintaining human control over strategic decisions and keyword validation. The GrowthX team reviewed the refined cluster strategy (which Blaxel's client Paul had approved) and identified critical AI guardrails: avoiding AI-generated strategic insights, removing overly technical content, and using a final validation step against client goals that successfully surfaced missing topics like "use cases" and "security/compliance." Kathy committed to documenting this workflow in Notion for team reuse.

---

## Context

Blaxel is a GrowthX client (contact: Paul, French founder) who had recently approved revised content topic clusters for their strategy. This meeting was an internal GrowthX sync between Aida (who conducted the cluster work), Kathy (who helped present to the client), and William (organizer) to review the process Aida used and capture best practices. The meeting occurred three days after Aida and Kathy had presented the final clusters to Paul, who provided positive feedback on the strategy itself. The conversation surfaced a technical blocker on the client side: Blaxel uses PostHog analytics rather than GA4, and HIPAA compliance constraints prevent standard GA4 integration without additional tools.

---

## Relevance

**To GrowthX Delivery:**
- New reusable AI workflow for topic cluster generation established, with clear guardrails for human review and validation (documented in Notion for team access)
- Key best practice: Manual keyword validation using SEMrush before finalizing clusters; AI hallucinations are common and require spot-checking
- Process refinement identified: Remove AI-generated strategic insights and limit content suggestions to avoid out-of-scope deliverables (e.g., coding tutorials)
- Final validation prompt methodology (cross-reference against client goals) successfully identified missing cluster categories ("use cases," "security/compliance") that would have reduced content effectiveness

**To GrowthX Business Development:**
- Client blocker on analytics setup (PostHog + HIPAA compliance preventing GA4 integration) requires solutions engineering; Fresh Paint tool identified as potential workaround with BAA option
- Client satisfaction signal: Paul approved cluster strategy at first review, indicating strong alignment and strategic clarity in presentation
- Expansion opportunity: If analytics issue is resolved, team may have data for optimizing content performance and identifying additional topics

---

## Overview

- **Blaxel's analytics blocker:** The client uses PostHog, not GA4. A HIPAA compliance issue prevents a simple GA4 setup, requiring a potential workaround like Fresh Paint to sanitize data.
- **New AI workflow:** Aida demoed a new process for creating topic clusters, using Claude for data analysis but manual review for strategic decisions and keyword validation.
- **Key AI guardrails:** The process avoids AI-generated strategic insights (which are often unfounded) and technical content (e.g., coding tutorials) to ensure quality and manage scope.
- **Validation step:** A final prompt asks the AI to review the strategy against client goals, uncovering missed topics like "use cases" and "security/compliance" that were then integrated.

---

## Key Topics

### Blaxel Client Update

  - The client, Paul, approved the revised topic clusters.
  - **Blocker:** The client uses PostHog, not GA4.
  - **Challenge:** A simple GA4 setup is not possible due to HIPAA compliance requirements.
  - **Potential Solution:** Use Fresh Paint, a tool that sanitizes PHI from data streams, making marketing tools like GA4 compliant via a Business Associates Agreement (BAA).

### New AI-Assisted Strategy Workflow

  - Aida demonstrated the new process for creating topic clusters, designed to improve clarity and accuracy.
  - **Goal:** Ensure each cluster's purpose, target audience, and rationale are explicit.
  - **Process Steps:**
    1.  **Context Upload:** Upload all project documents (transcripts, personas, competitor URLs) to Claude to provide a complete, isolated dataset.
    2.  **Competitor Analysis:**
          - Prompt Claude to analyze competitor URLs and keywords from the provided CSV.
          - **Refinement:** Filter analysis to direct competitors only.
          - **Guardrail:** Remove AI-generated "strategic insights" → Claude lacks full context and can make unfounded assumptions.
    3.  **Cluster Generation & Manual Validation:**
          - Prompt Claude to generate 4–5 clusters with descriptions, rationale, audience, and keywords.
          - **Manual Validation:** Spot-check and replace inaccurate keywords, using SEMrush to verify search volume.
          - **Strategic Refinement:**
              - Isolate commercial keywords into a dedicated "Comparison & Alternatives" cluster.
              - Remove overly technical topics (e.g., "Python for AI") → Avoids content requiring coding examples, which is out of scope.
              - Remove AI-suggested content types → GrowthX Labs owns this strategic decision.
    4.  **Final Validation:**
          - Prompt Claude to identify any missing topics by cross-referencing the strategy against client goals.
          - **Result:** This step identified "use cases" and "security/compliance."
          - **Action:** Create new clusters for these topics and merge "production readiness" into an existing one.

---

## Action Items

**Kathy Lam**
- Create Notion doc summarizing Aida's cluster workflow for team reuse

---

## Transcript
**Aida Knezevic:** Paul is a very nice European man.

**Aida Knezevic:** He's French.

**William Leborgne:** Yeah, I know.

**William Leborgne:** I was speaking in French with them when we first connected.

**Aida Knezevic:** Oh, very nice.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** How'd it go?

**Aida Knezevic:** It went well.

**Aida Knezevic:** He liked the clusters.

**Aida Knezevic:** He thought everything made sense.

**Aida Knezevic:** And yeah, I think we're in a really good spot with them.

**Aida Knezevic:** The only blocker is that they're using PostHog instead of Google Analytics, so we might need to tell them to set up GA4 for us.

**Aida Knezevic:** But that might not be possible considering that they are, like, they have to be HIPAA compliant and Google Analytics is not HIPAA compliant.

**William Leborgne:** Really?

**William Leborgne:** I did not know that.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** I mentioned that on the call.

**Aida Knezevic:** used to write content for a company called Fresh Paint.

**Aida Knezevic:** That's a lot of money.

**Aida Knezevic:** Have this software that can make any marketing tool HIPAA compliant.

**Aida Knezevic:** They sit in the middle and they like capture PHI, they like remove it, and then they send it downstream.

**Aida Knezevic:** And you can sign like a business associates agreement with FreshBank, so you're totally compliant.

**Aida Knezevic:** So, yeah.

**Aida Knezevic:** How do you think it went, Kathy?

**Aida Knezevic:** Was it okay?

**Kathy Lam:** Yeah, yeah, I think so.

**Kathy Lam:** He's like really helpful.

**Kathy Lam:** So, yeah, it was really great to like present to him like this was our first meeting.

**Kathy Lam:** And so, yeah, I'm glad to get that over and done with.

**Kathy Lam:** Thank you so much for rejiggering all the clusters.

**Aida Knezevic:** No worries.

**Aida Knezevic:** Yeah, I think what like, I think like when I was looking at the clusters earlier this morning, I was like this all like from a high level makes sense, but the information that's presented under the clusters isn't as straightforward as it could be.

**Aida Knezevic:** And it really...

**Aida Knezevic:** Really, like, just from the experience of working with all of these clients, like, they need to understand, like, what each cluster is supposed to do, who it's going to speak to, and why we're recommending it.

**Aida Knezevic:** And I think just having clarity in those sections is really important. Then we have to double-check all the example keywords in SEMrush to ensure the search volume is correct — because Claude loves to lie. You just can't trust Claude.

**Aida Knezevic:** If it doesn't have access to the right information, it's going to start hallucinating. Let me show you what I did today.


**Kathy Lam:** And then, William, I pushed out our meeting with Tyler, so I think we should have time.

**William Leborgne:** Oh, cool.

**William Leborgne:** Okay.

**William Leborgne:** Yeah, I saw that that happened out there.

**Aida Knezevic:** Oh, cool.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So the first thing I did for the Blaxel project — I uploaded the meeting transcript, the product deep dive transcript, the product feature matrix, which is so important, the competitors URL, the company context, and the audience personas.

**Aida Knezevic:** This way, I ensure nothing else seeps in — no external context that might affect the analysis.

**Kathy Lam:** And then I'm just gonna walk you through what I did. After this, I'm gonna take what you did and create a quick Notion doc so it's available for the team.

**Aida Knezevic:** Yeah, that's a great idea.

**Aida Knezevic:** So, I told it to read the kickoff meeting transcripts, summarize their goals, and explain why they're partnering with GrowthX right now. I titled that section "Why GrowthX Right Now."

**Aida Knezevic:** This is good. If I'd had more time, I would have added an intro sentence saying "GrowthX is here to help," but that's fine — what matters is that it captures their goals and what they're trying to achieve.

**Aida Knezevic:** It summarizes their goals, why they're here, and what their definition of success is. That's what matters.

**Aida Knezevic:** Then the next step was to analyze the competitors CSV file in the project documentation.

**Aida Knezevic:** It contains a list of blog URLs and keywords they rank for.

**Aida Knezevic:** For each competitor, provide the breakdown of what kind of topic clusters they cover, and how much is their average monthly search volume.

**Aida Knezevic:** Also provide a breakdown of the top topic clusters that all competitors cover at the top.

**Aida Knezevic:** So I meant, like, before the competitors, we just need to understand what are the clusters at a high level.

**Aida Knezevic:** example.


**Aida Knezevic:** It started analyzing the CSV file.

**Aida Knezevic:** At this point, I realized that this file had organic competitors as well as direct competitors.

**Aida Knezevic:** So I was like, okay, this analysis is valuable, but I'm going to narrow it.

**Aida Knezevic:** When it generated this response, I used a prompt saying there are some organic competitors in that file as well.

**Aida Knezevic:** Only include the following domains in your analysis.

**Aida Knezevic:** If one of those competitors doesn't appear in the CSV file, tell me.

**Aida Knezevic:** So I can go back and add them.

**Aida Knezevic:** It found those specific competitors.

**Aida Knezevic:** It identified that all five are present.

**Aida Knezevic:** And then it compiled everything into a comprehensive analysis.

**Aida Knezevic:** At that point, it was fine, but then it started giving me a strategic overview of what each domain is doing.

**Aida Knezevic:** For example, it highlighted top performing content, which is helpful but not what I wanted in the competitor analysis.

**Aida Knezevic:** Focusing on the clusters is most important, so I didn't want that much detail in the competitor analysis. Sometimes it can be helpful, Yes, I think it can be helpful.

**Aida Knezevic:** But I think I decided, like, to cut this to avoid making the document too long.

**Aida Knezevic:** And then, let's see what I actually said, because I know I wasn't happy with this.

**Aida Knezevic:** Oh, yeah, I said, remove strategic insights.

**Aida Knezevic:** You don't know anything about these companies' content strategies, which is true.

**Aida Knezevic:** It's making assumptions about what they're doing.

**Aida Knezevic:** I told it, "Your only job is to analyze the data and tell me what the topic clusters are based on the URLs and keywords they rank for." But it started making strategic takeaways, and we don't really know what we're looking at. We're analyzing just their blogs — they might be doing webinars, white papers on their site that we're unaware of.

**Aida Knezevic:** So we have just a small snapshot of their overall content strategy. This type of work is very strategic — AI should not be doing it.

**Aida Knezevic:** So I cut everything except the data analysis part, which was great. We did it as pure data analysis. I asked it to provide a paragraph summary for each competitor instead of just tables, and I told it to remove top performing URLs or high volume keyword suggestions — those might be helpful for the content calendar later, but they're not needed in the strategy document.

**Aida Knezevic:** It would confuse the customer asking why we included that in the example keywords, and it just opens a can of worms.

**Aida Knezevic:** Then I copied and pasted it into Notion and said, "Look at the analysis of the entire CSV file — which topic clusters can we create for the Blaxel blog content strategy, like four to five clusters? These should be aligned with their audience and help them grow authority, visibility, and leads. Each cluster should be broad enough to support months of content production. For each topic cluster, provide a brief description, why we recommend it, the target audience, and five example keywords all taken from the CSV file."

**Aida Knezevic:** Then it analyzed and the first output was pretty good. The example keywords were more of a miss than a hit, so I did manual spot checking. If I wasn't happy with a keyword, I looked at the description to see if it made sense, like "agent architecture" — and I'd replace it with something I knew had higher search volume, like "AI agent frameworks."

**Aida Knezevic:** It's just about making sure these are good keywords. I copied and pasted everything into Notion, then edited all the example keywords.

**Aida Knezevic:** Then I provided feedback on each cluster. Number one was good, but all commercial keywords should go into a separate cluster — it had bulked them together. I isolated them into their own cluster. Number two was good but needed commercial keywords removed. Number three had content type suggestions I wanted removed.

**Aida Knezevic:** When it comes to suggesting content types, that should come down to us — we should decide what type of content to create.

**Aida Knezevic:** The AI would suggest practical implementation guides, but we can't do those. We can talk about how to implement something at a high level, but we can't do tutorials. So we have to be careful about what we promise.

**Aida Knezevic:** Same with number four. Then I removed number five and replaced it with the commercial keywords cluster. Number five was "Python for AI development," which is too technical — I don't want to do coding languages. If code examples start showing up in content, that's a bad sign. We should stay away from anything that needs coding examples.

**Aida Knezevic:** Then it regenerated the clusters. I created a new "Comparison & Alternatives" cluster. I didn't use any of the AI-suggested examples — I manually found them, like "E2B versus Modal" and "Modal alternatives." I'm not sure about "AI development alternatives," but that might be usable.

**Aida Knezevic:** Sorry, my vet is calling me.

**William Leborgne:** Just a second.

**Kathy Lam:** Yeah, go for it.

**Aida Knezevic:** My vet is coming over to vaccinate my cat in a couple minutes.

**William Leborgne:** Got it.

**Kathy Lam:** No worries, we'll finish quickly.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, yeah.

**Aida Knezevic:** Then I generated a brief description about the clusters explaining how we arrived at them. Then came the key part — I asked Claude: "Is there anything important missing from this topic cluster strategy based on the project documentation and client goals?" It went through the kickoff call and identified missing use case content, security and compliance case studies, and production readiness/reliability. I folded production readiness into an existing cluster.

**Aida Knezevic:** So I told Claude to create a use case cluster and a security/compliance cluster. I merged production readiness under the first one. Now we have "AI Agents" with a sub-cluster for use cases, and a separate security cluster. That allows us to verify we didn't miss anything. This is all accessible in Blaxel's project files if you want to dive deeper.

**Kathy Lam:** This is awesome.

**William Leborgne:** Thank you, Aida.

**Aida Knezevic:** No problem. I'll see you next week.
