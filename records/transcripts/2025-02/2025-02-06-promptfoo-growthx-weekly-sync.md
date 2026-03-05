# Promptfoo <> GrowthX Weekly Sync

<metadata>
date: 2025-02-06
time: 18:31 UTC
duration: 12 minutes
organizer: Vivek Shankar (GrowthX)
participants: Vivek Shankar, Kyle Gaudreau, Vanessa Sauter
fathom_recording_id: 46012522
fathom_url: https://fathom.video/calls/226856041
share_url: https://fathom.video/share/QXxBDfyxsxy4Qt6nz9ydXx9YsRZUqWrb
source: fathom
enriched_on: 2026-03-05 14:32 UTC
</metadata>

---

## Summary

GrowthX and promptfoo synced on LLM security content delivery, with GrowthX explaining quality challenges caused by SEO-driven research pulling in irrelevant competitor content. The teams agreed to continue refining the research process and implementing manual LLM checks alongside fact-checking flows to maintain scalability while improving accuracy. Vanessa is reviewing updated articles on application layer vulnerabilities and system prompt leakage, with Vivek to deliver the excessive agency article by the next day.

---

## Context

promptfoo is a vendor of an LLM testing and evaluation tool. GrowthX provides content marketing services and is creating a series of LLM security articles for promptfoo, covering topics like system prompt leakage, application layer vulnerabilities, improper output handling, excessive agency, and unbounded consumption. This weekly sync is a regular check-in to track article progress, address quality issues, and align on next steps. The challenge is that GrowthX's content generation process relies on SEO-driven research that sometimes pulls in irrelevant competitor content, creating inconsistencies that require manual editing.

---

## Relevance

**To GrowthX Delivery:**
- Content generation at scale for specialized technical audiences (LLM security) requires hybrid automated + manual review workflows to avoid reputational risk
- SEO-focused research algorithms can work against domain-specific content quality—need refinement to persona and topic boundaries
- Implementing LLM-as-judge for persona fit and fact-checking within the generation pipeline is preventing full manual authorship but adds process complexity

**To CheckThat:**
- This engagement demonstrates real-world use of LLM evaluation tools in production content workflows
- Potential reference case if promptfoo wants to showcase GrowthX's use of their platform

**To GrowthX Business Development:**
- promptfoo relationship is active with regular syncs and article delivery cadence; expansion potential to other technical audiences or product categories
- GrowthX team expansion (engineers being added) is timed to increase delivery speed and workflow flexibility for this and future clients

---

## Overview

- Content quality challenges stem from SEO-driven research pulling in irrelevant competitor content
- GrowthX is refining their research process to better focus on LLM security topics and persona
- Manual LLM checks and fact-checking are being implemented to ensure content accuracy
- promptfoo to review updated articles on application layer vulnerabilities and system prompt leakage

---

## Key Topics

### COVID-19 Experiences

  - Kyle (GrowthX) currently has COVID-19, his first time getting it in 5 years
  - Vivek (GrowthX) caught the first strain in Southeast Asia before it was widely known
  - Vanessa (promptfoo) had COVID 1.5 years ago while traveling internationally, sick for 10 days

### Content Quality Challenges

  - GrowthX facing issues with automated content generation for LLM security topics
  - SEO-driven research pulls in irrelevant competitor content, creating "content gaps"
  - Manual edits required, leading to some inconsistencies slipping through
  - GrowthX working on refining the research process to focus on specific topics and personas

### Quality Assurance Measures

  - Manually using LLMs to check content suitability and accuracy
  - Implemented fact-checking flow within article generation process
  - Aiming to avoid fully manual writing to maintain scalability

### Article Status Updates

  - Application layer vulnerabilities: Edits incorporated, awaiting Vanessa's review
  - System prompt leakage: In client review stage, Vanessa to review
  - Improper output handling: Access granted to promptfoo's CTO, awaiting confirmation
  - Excessive agency: To be delivered by GrowthX within next day
  - Unbounded consumption: Moved to "published" status (previously delivered)

### GrowthX Team Expansion

  - Close to adding several engineers to the team
  - Aim to improve workflow adaptability and value delivery speed

---

## Action Items

**Vanessa Sauter (promptfoo)**
- Review application layer vulnerabilities article (recently edited)
- Review system prompt leakage article (in client review)
- Ping Michael (promptfoo CTO) regarding improper output handling article review status
- Review excessive agency article once delivered

**Vivek Shankar (GrowthX)**
- Deliver excessive agency article by tomorrow (February 7)

---

## Transcript

**Vanessa Sauter:** I think he should be joining—he would double check.

**Vivek Shankar:** All right, I'm not sure if Kyle's gonna join because he has COVID.

**Vivek Shankar:** Kyle is unfortunately stuck in 2020.

**Vivek Shankar:** He was telling me this is the first time he's got COVID. So I was a bit surprised.

**Vivek Shankar:** That's kind of an accomplishment.

**Vanessa Sauter:** You know, five years later, you get it.

**Vivek Shankar:** Well, it's definitely no fun, no matter when you get it.

**Vanessa Sauter:** I know.

**Vivek Shankar:** I think it's still taking like 14 days or something to recover.

**Vanessa Sauter:** Yeah, it takes a long time. It's pretty brutal.

**Vivek Shankar:** Did you ever catch any of the strains?

**Vanessa Sauter:** Yeah, I did. I was traveling internationally, and it's giving like a year and a half ago. I got COVID when it came back. I was pretty sick for like 10 days. Even after the vaccines, it's so hard.

**Vivek Shankar:** Yeah, I actually caught the first ever strain because I was in Southeast Asia. I got COVID before anybody even knew it was COVID.

**Vanessa Sauter:** Oh my god, that's how early you were.

**Vivek Shankar:** Yeah, I was in Asia right during Chinese New Year.

**Kyle Gaudreau:** I'm going through my first bout of it. It's about two and a half weeks ago.

**Vanessa Sauter:** I'm so sorry about that. Did you get the prescription that helps with COVID symptoms?

**Kyle Gaudreau:** I think if my fever had run long enough, I would have been more apt to go to the doctor and do it. But I had a fever for like a day and a half, and then it was just all the other stuff. So I was like, we'll just see where this goes.

**Vanessa Sauter:** You've got a dog in the background.

**Kyle Gaudreau:** Oh yeah, my dog loves to jump up in the window like that.

**Vanessa Sauter:** What kind of dog do you have? He's a Russell Terrier?

**Kyle Gaudreau:** He's about 25 pounds, very cute. Any Terrier can be a handful.

**Vanessa Sauter:** We got ours as a puppy from Tijuana. He's like really big—completely dark coat, mostly German Shepherd. My wife was adamant on breaking gender norms, so she insisted we name him Baby, and he has a pink collar and a pink tag. It's funny because he looks very scary but is a total sweetheart.

**Vanessa Sauter:** Let me just double check on Slack to see if Kyle will make it. No worries.

**Vivek Shankar:** I can share my screen and run over the agenda while we wait.

**Vivek Shankar:** By the way, my internet might be a bit dodgy, so if you can't hear me, please let me know.

**Vivek Shankar:** So we wanted to check in regarding improper output handling. I noticed the request from your CTO last week. I granted him access and just wanted to know if we're good to go ahead.

**Vivek Shankar:** The application layer vulnerabilities—we addressed your edits just before the call. The article is ready for you to review. The system prompt leakage is in client review, which is basically the first time you review it. The other two articles are in post-edits.

**Vivek Shankar:** Following on from my message yesterday, we've been trying to avoid having to manually write these articles because that doesn't help you and it doesn't help us scale. We've been refining the researcher part of our flow. The issue we're having right now is that it's looking at SEO performance and competitor content, no matter what the quality is. It's seeing that if competitors address subjects x, y, z—which may or may not have anything to do with LLM security—then if we don't address that, it becomes a content gap and won't perform as well. So it's pulling in all these additional things. Because competitor content is non-existent or completely off-point, there's a lot of edits we're doing manually. A few things are slipping through, which is why we can't automate that part. We're working on refining it to zoom in on particular topics and refine it for the persona.

**Vivek Shankar:** The other thing, regarding the LLM as judge, we are doing that manually because we don't have it as part of our flow yet. For the system prompt leakage, we ran it through an LLM to check: is this suitable for the persona? Is this information accurate? We also have a fact-checking flow within our article generation process to make sure we're not saying anything weird or out there. We could go ahead and manually write all of these things, but that's not going to serve the purpose we're looking for.

**Vanessa Sauter:** Thank you for laying that out. I know it's hard. It's a new challenge. We're all trying to solve it right now. I appreciate you explaining that. I haven't had a chance to look at the system prompt leakage yet. I'm giving the application layer a cursory look, but let me do a more thorough review. Probably won't be until later today or tomorrow. I appreciate you guys reworking this. It looks like you did incorporate the edits, which is great.

**Vanessa Sauter:** So I've got to look at this one. I need to look at the system prompt leakage one. Was there another one I needed to review?

**Vivek Shankar:** The improper output handling one. You didn't mention that your CTO would look at it and then give final sign-off.

**Vanessa Sauter:** So I'll ping Michael, your CTO, and see where he's at. I'll take a look at the application layer vulnerabilities and the system prompt leakage. And you guys are going to deliver the excessive agency one?

**Vivek Shankar:** Yes. Ian had moved unbounded consumption to published because that was actually already delivered—it was the first one we delivered.

**Vanessa Sauter:** Yeah, I thought we'd already done that one. So we'll take a look at it. Let me know when the excessive agency one is done.

**Vivek Shankar:** Excessive agency should be in by this time tomorrow, or maybe even earlier.

**Vanessa Sauter:** So I've got homework on my end, and I've got good follow-ups.

**Vivek Shankar:** If there are any other quality issues, please let me know. We'll keep working to make sure we get it there.

**Kyle Gaudreau:** In the background, we're trying to get more support to address the things Vivek mentioned about speed and workflow adaptation. We're quite close to adding quite a few engineers soon. It's early stages, but we have good progress. Hopefully that means we can bring more value quickly.

**Vanessa Sauter:** I appreciate that update. It's a challenge right now. Thanks for being transparent about it.

**Vivek Shankar:** All right, we'll take care. If anything comes up, let me know.

**Vanessa Sauter:** Hope you recover from COVID. It's pretty nasty. Hope you guys have a great rest of your day.

**Kyle Gaudreau:** Thanks, Vanessa.
