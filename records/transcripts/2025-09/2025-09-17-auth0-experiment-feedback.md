# Auth0 Experiment Feedback

<metadata>
date: 2025-09-17
time: 18:32 UTC
duration: 32 minutes
organizer: Kyle Gaudreau
participants: Kyle Gaudreau, Sydney Go, Nick Winkler, Rachael Tiow
fathom_recording_id: 87988687
fathom_url: https://fathom.video/calls/412152349
share_url: https://fathom.video/share/aAo-JZ-xncc9kDzSxsz2z5-VJaRAyy2X
source: fathom
enriched_on: 2026-03-03 01:20 UTC
</metadata>

---

## Summary

GrowthX and Okta reviewed the Auth0 experiment, where Gemini AI is being used to accelerate SDR account research and outreach. Nick Winkler reported massive time savings — reducing account research from 1-2 hours to roughly 10 minutes per account — and described Gemini's ability to enable far more targeted, personalized messaging compared to previous broad-brush approaches. The team identified technical issues (Gemini file permissions, occasional inaccuracies like claiming companies are non-operational), challenges with validation and consistency, and process improvements needed for scaling to other SDRs. Next steps include building better templates and prompts, fixing the permissions issue, and evaluating workflow restructuring around account-specific gems.

---

## Context

Okta's Nick Winkler is an SDR running a pilot with GrowthX where they're testing Gemini AI to accelerate account research and personalized prospecting. Kyle Gaudreau (GrowthX Labs) and Sydney Go (GrowthX) are supporting the experiment. Rachael Tiow from Okta is also involved in the initiative. The hypothesis is simple: can AI-powered research and message generation make SDRs dramatically more efficient while maintaining or improving outreach quality? The experiment has been running for a couple of weeks, and this feedback session is gathering Nick's observations on what's working, what's not, and what needs to be refined before rolling out to other SDRs.

---

## Relevance

- **To GrowthX Services:** Demonstrates the potential for AI-augmented account research and outreach workflows in B2B sales motions. Time savings from 1-2 hours to 10 minutes per account could be a significant selling point for future GTM services around AI-assisted prospecting. Shows need for better prompt templates, validation frameworks, and SDR enablement processes.

- **To CheckThat / AI Visibility:** Real-world example of Gemini's limitations when it lacks internet access — it confidently provides outdated information (e.g., false bankruptcy status, outdated promotions) that could hurt outreach. Highlights importance of validation and fact-checking in AI-generated content. This is a key use case for improving AEO and AI content reliability.

- **To Okta Relationship:** Strong account health signal. Nick is enthusiastic despite friction points, and the rollout to other SDRs is imminent — indicates Okta's commitment to the experiment. Need to resolve technical issues (Gemini permissions, file access) before broader adoption. Potential to expand if this becomes a standard part of their sales workflow, creating recurring engagement around template optimization and AI quality.

---

## Overview

- The AI tool is significantly accelerating workflow, reducing account research time from 1-2 hours to about 10 minutes per account
- Gemini enables much more specific and targeted messaging compared to previous broad-brush approaches (20 accounts with a single message vs. personalized, account-specific messaging)
- Some technical issues with file permissions and Gemini's occasional inaccuracies (incorrectly flagging active companies as non-operational) need addressing
- File permission issues may be resolved by moving files to personal folder rather than shared folders created by others
- Gemini's folder vs. individual file limitation (10 documents per gem) and ability to add entire folders are areas for optimization
- Subject line and congratulatory message duplication/outdated references across multiple emails to same account is a deliverability concern
- The experiment shows promise in making SDRs more efficient, but refinements are needed for wider adoption across the team

---

## Key Topics

### Sentiment and Time Savings

  - Nick reported overall positive sentiment, describing the tool as "definitely helpful" and a "huge value add"
  - Time savings: 1-2 hours reduced to approximately 10 minutes per account for research, qualification, and prospect list building
  - Enables much more specific messaging than previous approaches (previously: 20 retail accounts with a single message; now: tailored, account-specific messages)
  - Workflow transformation: enables account research depth that would have been unfeasible without AI assistance

### Gemini Usage and Workflow

  - Standard prompt: "Help me break into [X account]"
  - Gemini analyzes provided research documents and returns: account qualification assessment, key buying signals (data breaches, digital transformation initiatives, lack of modern identity solutions), specific personas to target (VP IT Infrastructure, CTO, COO), and email cadence recommendations
  - Nick uses a 15-step email sequence built into Outreach platform, with Rachael providing sample prompts that Nick either uses verbatim or customizes per persona
  - Nick goes back to Gemini with "help me write an email to [person] using this prompt" to generate personalized email copy
  - Gemini is faster at email generation than account research/analysis

### Technical Challenges

  - File permission issues when accessing shared folders in Google Drive (downloading turned off for files shared via folder created by Rachel; may be resolvable by moving files to personal folder)
  - Gemini was down at least once during pilot, causing frustration
  - Limited to 10 documents per "gem" (AI workspace), requiring manual addition/removal of documents for each new account
  - Uncertainty about folder vs. individual file usage in gems — testing whether entire folders can be added to gems and whether documents remain accessible when removed from gem knowledge base
  - Document access behavior: when gem contains a folder but not individual documents, Gemini will acknowledge it lacks the info and ask clarifying questions rather than hallucinate

### AI Output Quality

  - Generally good output, but occasional inaccuracies stemming from Gemini's lack of internet access (e.g., incorrectly flagged New York & Company as bankrupt/non-operational when they're fully operational, just transitioned from brick-and-mortar to online)
  - Produces sometimes-identical subject lines across multiple emails to same company, which impacts email deliverability (open rates drop when same subject is used across multiple emails to same organization)
  - References outdated information without validation (e.g., congratulating someone on a promotion they received a year ago, rather than recent)
  - Nick is skeptical of AI-provided information and wants ability to validate claims via Google/LinkedIn before sending
  - Kyle noted that Kyle has personally received "congrats on joining GrowthX" emails after being there nearly a year
  - Tone is "corny" — frequently starts emails with "All right team" which feels forced

### Improvement Suggestions

  - Provide justification/reasoning for accounts rejected from the program (e.g., why Steve Madden was excluded), so SDRs can learn patterns for future account selection
  - Implement better prompt templates and instructions to improve consistency and reduce corny tone
  - Consider restructuring to one gem per account with broader instructions/templates within the gem, and individual chats for specific accounts/personas (reduces manual add/remove friction, though could risk lost document context)
  - Avoid congratulatory messaging in AI-generated emails; instead, focus on non-time-sensitive, value-based messaging
  - Empower users to request multiple email variants, allowing them to branch into new themes (e.g., "give me a few variants, then build 3 more within that theme")
  - Add ability to validate AI-provided information before sending (though this may be beyond Gemini's capabilities)

### Scaling Considerations

  - SDRs not as thoughtful as Nick may hit friction points that he navigates smoothly — Kyle wants to minimize those friction points during rollout
  - Some users may resist Gemini's processing time (takes a second or two to synthesize research), though Kyle notes that fast responses usually indicate shallow analysis
  - Important to educate users that processing time enables better synthesis (e.g., "instant noodles still take 3 minutes")
  - Nick is excited about rollout and expects many questions/feedback once other SDRs get access
  - Balance: making the process easy and repeatable for one SDR vs. easy and repeatable for many SDRs with different skill levels

---

## Action Items

**Sydney Go (GrowthX)**
- Investigate Gemini docs permissions issue; test if moving files to personal folder resolves problem

**Kyle Gaudreau (GrowthX Labs)**
- Create prompt templates for Gemini; design easier setup process for SDRs

- Develop improved template prompts and instructions for Gemini to streamline SDR workflow

- Evaluate and propose new approach to avoid using potentially inaccurate congratulatory messages in AI-generated emails

---

## Transcript

**Kyle Gaudreau:** All our client meetings, so we'll have, like, you know, we have a big team, so there'll be multiple meetings that are overlapping, and it's like, oh, someone else is in a meeting right now. Like, that's not how this is supposed to work. I think Rachael is going to be on this, yeah?

**Nick Winkler:** Yeah, we'll give her a minute then.

**Kyle Gaudreau:** Where are you at now, Sydney?

**Sydney Go:** So, short story, we're on Victoria Island because I have to get government papers for the cat. She's here, and we did a four-hour ferry to get here yesterday, coming back today for another four hours. I must really love her.

**Kyle Gaudreau:** Well, I can set the stage a little bit while we wait for Rachael and Nick.

**Kyle Gaudreau:** I've got a few things on my mind that would be helpful. First, I'd love to get your top-level sentiment — is this a value add or not? This is an experiment, and experiments can fail, and that's okay. Our intention is to learn how to build something effective. Second, I'd love you to walk us through how you've been using Gemini in a gem, any patterns you've noticed, screenshots, that kind of thing. I know that's a lot for 30 minutes. You seem quite thoughtful about this, but I can't assume everyone else will put that time and effort in. So I want to understand where you're hitting friction points, because those will probably be even more acute for other folks. And then we can think about how to adjust our enablement and scaling approach. Does that sound good?

**Nick Winkler:** Where should we start?

**Kyle Gaudreau:** Let's start from the top. What's your general sentiment? Is this crap? Is it helpful?

**Nick Winkler:** Yeah, definitely helpful.

**Nick Winkler:** It's accelerating my workflow dramatically, especially on the account research side. The key thing is it's reducing account research from an hour or two hours to no more than 10 minutes per account. It's a huge value add. Without a tool like this, we probably wouldn't have done a project like this or at least not in this depth. Previously, what we'd do is take 20 retail accounts that all have loyalty, send them one message that fits the bill. Now being able to get so much more specific within those messages is miles better than what we previously would have done.

**Kyle Gaudreau:** Amazing.

**Kyle Gaudreau:** So when you talk about that time savings, is that time to get a first touch out?

**Nick Winkler:** Yeah. When I think of the research piece, I start with qualifying the account — What volume are they getting? Are they a tech-forward company? Do they have things in place that would justify an investment in customer identity? Then I figure out if they have the right people to talk to, who I need to talk to, who we've talked to before. Then I build out my prospect list and figure out my messaging. All of those things have been cut down from one to two hours to probably 10 minutes.

**Kyle Gaudreau:** What about some things that are not going super well?

**Nick Winkler:** There's a couple things, but by far the biggest is Gemini. I'm running into an issue where all of a sudden downloading is turned off for one or more of these files, and it won't allow me to insert them. This just happened right before this call.

**Kyle Gaudreau:** That's interesting. Can you try it from a different folder?

**Nick Winkler:** The files are all in this folder. The weird thing is, if I go into the drive directly, I have no problem accessing or downloading those files. So I'm not really sure what changed in the last day.

**Sydney Go:** Rachael was the one who created that folder. It might be a user permission problem. I have the same issue — when I'm downloading something personally, I can do it. But when I try to upload something using an automated file, I can't do it because of the permission levels. If I were to move files to my own folder, that might give me a better shot of having everything work. Those permission issues from the folder creator are usually a security layer.

**Nick Winkler:** Yeah, I'm pretty sure you're spot on. If I moved them into my own folder, that would probably solve it.

**Nick Winkler:** I guess outside of Gemini issues, I've got a couple notes. One thing is about account selection. We got our accounts earlier today, and a colleague came up asking why Steve Madden was excluded. I verified — they have login, they have loyalty. So for accounts that don't make the cut, if there was justification or reasoning we could either challenge or learn from, that would be helpful. Not just so we're not wondering why, but so in the future as we scale and add more accounts, we can think better about which accounts are worth the investment vs. which ones check the boxes or avoid issues we've had with others.

**Kyle Gaudreau:** Makes sense. One other thing I want to dig into.

**Nick Winkler:** There's one account, New York & Company. I went in knowing it's not a particularly strong account — they've had a lot of financial trouble. When I prompted Gemini with it, it told me it wouldn't work as an account because it was bankrupt. But they're still fully operational; they've just moved from brick-and-mortar entirely online. I liked that it gave a financial justification — saying even if the account was around, given what they've been through financially, it's not your best account to go after. It did a really good job with that. But I was concerned it flagged that the company no longer exists, which surprised me.

**Kyle Gaudreau:** You can dig into that one as well.

**Kyle Gaudreau:** Hey, Rachael. We were just starting with sentiment. I wanted to get a flavor — is this crap? Is this helpful?

**Rachael Tiow:** Crap.

**Kyle Gaudreau:** Well, this is an experiment, and experiments can fail. It's okay. We really want raw feedback as much as possible. It's encouraging to hear that Nick is saving about one to two hours per account. That's huge. Now I want to get into specifics. Nick, can you walk us through how you've been leveraging Gemini? I'm curious about different prompts, use cases, what's been useful and not useful. I'm trying to see patterns in how you're using this.

**Nick Winkler:** Totally. So my standard prompt is always "Help me break into [X account]." It's pretty corny — every time Gemini starts with "All right team." But it right away tells me: "Is this a good account for you to get into?" which is good. Then it goes into the signals and how they fit into the account — data breach, no modern identity solution, moving to a digital-forward model, no social login. It checks every box for every signal. Then it says who to go after.

That's where I start drifting. It recommends personas like VP of IT Infrastructure and CTO. I might branch out and find a more targeted person. For example, the CTO also acts as COO.

From there, Rachael and the team made a 15-step email sequence in Outreach. Rachael put together sample prompts we can use verbatim or customize per persona. I've been staying pretty true to them, and it's produced really good stuff. Then I go back to Gemini and say "Help me write an email to [name] using this prompt" and throw in the template. It understands and works faster on message generation.

One thing I've noticed: if I'm doing multiple people in the same account, Gemini gives me the same subject line, which impacts deliverability. Open rates drop when you use the same subject across multiple emails to the same company. It does change them enough most of the time, but maybe once or twice they were identical.

**Kyle Gaudreau:** There are definitely a few things we can help with — better prompts and templates. One thing I've found success with is asking for a few variants. Even if you keep it broad — "give me a few" — you'll find an interesting thread to double-click into and branch from.

**Nick Winkler:** It has naturally done that a couple of times.

**Kyle Gaudreau:** We can tweak template prompts and instructions to make this easier for you and other SDRs as we bring them in.

**Kyle Gaudreau:** Is there anything you found to be stubborn — like you're trying to tease out information and it's just not getting you there?

**Nick Winkler:** One thing is Gemini can't access the internet. It will tell me a company is non-operational when they're actually operational. But there are other situations where it references information in emails — like "congrats on your recent promotion" — and I need more proof. I had one example where someone had been in that role for over a year, but Gemini congratulated them like it was recent. I want to validate that information. I'm a skeptic about AI information, so it's another manual step for me to check Google or LinkedIn.

**Kyle Gaudreau:** I've been on the receiving end of those emails. "Oh, congrats on joining GrowthX" — I've been here almost a year. I'm leaning towards we should be careful and just not try to play that game with congratulatory messages.

**Nick Winkler:** We have email best practices in the gem, so it knows not to be overly nice. As long as it doesn't start with "All right, listen up," we're good.

**Kyle Gaudreau:** Any other big unlocks or challenges?

**Nick Winkler:** Gemini was down one day, which was frustrating. One interesting thing: you can add folders to gems, not just individual documents. We've been limited to 10 documents per gem, so we've had to swap documents for each new account. But if folders work, that could be helpful. I'm hesitant to put more than one account at a time because I don't want Gemini to dig through everything.

**Rachael Tiow:** The best practice is one gem per account.

**Nick Winkler:** Rather than removing and adding accounts back in?

**Rachael Tiow:** Yeah, because of that add-and-remove issue.

**Kyle Gaudreau:** You could do one gem per account. We could think about structure differently — the gem has instructions, templates, broader things to make it perform repeatably. Individual chats could be where you do the specific accounts, starting with the brief and attaching documents within the chat rather than the gem knowledge base.

**Nick Winkler:** So documents within the chat, not the gem itself?

**Kyle Gaudreau:** Yeah. Then you don't have to add or remove from the project folder. With Claude, adding and removing things occasionally causes it to miss changes. Not saying that's the only reason, but there could be benefits — less gems, more focus, more structured instructions and templates.

**Nick Winkler:** If I start a new chat five days later for the same account, would the chat still hold the document if I removed it from the gem?

**Kyle Gaudreau:** They probably won't hold it. It might act like it does, but that's the danger. How do we make this easy and repeatable for you and also for multiple SDRs? More room for failure means more failures.

**Nick Winkler:** Gemini did something good though: when I put a folder in the gem but the specific documents weren't there, instead of guessing, it gave me the questions I needed to ask myself. It was aware it didn't have the information and didn't falsify anything.

**Kyle Gaudreau:** Well, I have to hop to another meeting. This was very helpful. If things come up — frustrations, cool unlocks, whatever — share them in Slack. I know you have a lot of accounts to focus on.

**Rachael Tiow:** We're here to help Nick get promoted to AE.

**Nick Winkler:** Now that it's being rolled out to the SDRs, there will be a lot of questions and comments coming your way.

**Kyle Gaudreau:** Thank you, Nick. Love to hear this is saving you time. We're just scratching the surface here.

**Nick Winkler:** Yeah, think the ideal state here is, you know, I've become obsolete, so hopefully this helps me get voted first, like Rachel said.

**Nick Winkler:** I'm kidding, but no, it's really cool.

**Nick Winkler:** think there's a lot of, you know, potential to, I mean, I think Rachel said it really well when we first started working together was that we can, you know, we make the C players into A players.

**Nick Winkler:** So I think this could, you know, do a lot of really cool stuff.

**Kyle Gaudreau:** Well, what we're trying to do is take an A player and make them into even more of a superstar, so.

**Nick Winkler:** Right.

**Nick Winkler:** Cool.

**Nick Winkler:** Well, thanks, Nick.

**Nick Winkler:** Awesome.

**Nick Winkler:** Thank you.

**Rachael Tiow:** All right, see ya.

**Rachael Tiow:** you.
