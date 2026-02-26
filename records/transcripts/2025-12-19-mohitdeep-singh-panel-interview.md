# Mohitdeep Singh - Panel Interview | AI Engineer (Applied AI Scientist)

<metadata>
date: 2025-12-19
time: 20:30 UTC
duration: 35 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Mohitdeep Singh
fireflies_id: 01KCS8KJHJ7SD3CC737YRKRTXX
transcript_url: https://app.fireflies.ai/view/01KCS8KJHJ7SD3CC737YRKRTXX
</metadata>

---

## Summary

Mohit's interview highlighted his strong technical background and problem-solving skills relevant to GrowthX's AI challenges. He detailed his transition from signal processing at ID Research Labs to applied machine learning at Coupang, showcasing adaptability. His experience with recommender systems and personalization ranking aligns with GrowthX's AI data labeling needs. Mohit proposed a hybrid AI solution combining fine-tuned models and reinforcement learning to enhance recommendation systems. His proactive learning approach and readiness to focus on customer empathy and pragmatic solutions reinforced his cultural fit, prompting Marcel to express strong interest in moving forward with the hiring process.

---

## Action Items

**Mohitdeep Singh** - Prepare for potential AI team leadership role and culture building as the first AI hire at GrowthX

**Marcel Santilli** - Regroup with Daniel and move forward with decision making and next steps following this interview

---

## Transcript

**Marcel Santilli:** Hey, how are you?

**Mohit:** I'm doing good, how are you?

**Marcel Santilli:** Pretty good. Happy Friday before the holiday, you know. Tell me, tell me, tell me more. In what sense?

**Mohit:** You know, I started to look out and you know, it's really difficult, the job interviews and all is what I'm trying to say. It's not kind of how it used to be.

**Marcel Santilli:** Yeah, yeah. The bar is a lot higher or... You have a lot of good experience, you know. Maybe for jumping in, obviously, like I looked your background, heard good things from the team as well from Daniel and others. Love to maybe hear from your own, in your own words, a little bit of your journey, you know, and then we kind of dig in from there.

**Mohit:** Yeah, sure. So basically I started out my career working for the ID research labs and I was mainly working on the signal side, because we did not have any kind of image processing pipelines and the kind of hardware that we have now. But signal analysis was one of my main things and that's what I had been doing with Pandora with radio. I moved on to recommendation systems. Coupang is the most recent one and over here I was working with payment systems. So a lot of recommendation over there, a lot of animal detection pipelines was something that I architected. But mostly, I was working with very small impact teams. I came from a research background to a complete applied machine learning pipeline background. So that's my story in short.

**Marcel Santilli:** Yeah, like I know you had several conversations so far and whatnot. Any initial reactions on things that might get you excited to work here as well or any of the problem domains that Daniel shared that got your brain thinking, you know?

**Mohit:** So it was very interesting with the problem that me and Katya were discussing on that and I think the case study that I was working on was on those similar lines. I had that call with Katya and Daniel and it was great to explain all of those things. I had a very well structured idea around how we could handle some of the things. Katya was also talking about the problems that they are currently facing. So you want the results to come up to the LLM in such a way, such that it sees it all the time. I think it's really important given the fact that you will be working for a lot of clients and you need to be able to hit that right spot all the time. So I think that was the most interesting aspect around it.

**Mohit:** The problem that Katya and Daniel described to me, that's something every company is trying to do. They are trying to hit the bullseye with the prompt when you send it to the LLM. That got me very excited. I had an initial solution presented and we had a small discussion. It was really productive. We got to understand what we could do, what we couldn't do. And we discussed few things about the architecture as well. I really like how Daniel approaches the problem. He brings in a lot of experience in that. So yeah, it got me really excited.

**Marcel Santilli:** Yeah, that's awesome. I think there's like the part about your background that's really interesting on a lot of the recommender systems and personalization rankings. Even though at face value, what we're doing might not immediately associate with that. I come from work that companies are doing data labeling and some post training, supervised fine tuning. And when you think about that, Serge is one of our customers, Serge AI. A lot of what's happening in those areas, it's really similar to recommender system domain problems.

**Marcel Santilli:** Serge's founder, I don't know if you've heard any of his interviews, but like he spent a lot of time. The way he approached Serge and why Serge is the only one of the data labeling players is actually profitable. It's over a billion in revenue. Because the way he approached it was like he was working on recommender systems at Meta and Facebook, Twitter and YouTube. There's like all these signals that they were trying to optimize for in order to figure out what to show people in their feeds or what videos to show when you log into YouTube or what tweets to show.

**Marcel Santilli:** What they found really early on was that the best way to do it was to have human preference data. Humans say what they prefer to see and kind of do things like that. But then there's like all these other stuff, signals if you will. Data labeling, finding experts was always the bottleneck for him. For him and the projects that he was working on is like finding. So then they would just hire these like random people off the street and then eventually they're like, we should probably hire the kind of people that we want the data from. Sourcing them and giving them the tasks and then you build the system.

**Mohit:** Yeah, that's what, you know, I understand the relevance of the recommendation system now. I mean that's really one way to look at it. But you know, you can also use a reinforcement learning approach. Like you could set up few of the policy and actions. But it's not going to be instant. It's going to take some time and we need to come up with a nice reward equation for that. Maybe we can take a look at that kind of system so we can have a fine tuned model for a few of the things. And we can also have a reinforcement learning to adjust the policies. You could improve things a lot by using a good ranker or you can use a re ranker as well. I think Daniel already showed me that you have a lot of agent frameworks around few of these things. So I just added my few cents into that. You can add a factuality check, you can add a structure check and those are a few of the things that I could think top of my mind.

**Marcel Santilli:** Maybe we can look at either your experience at Roku or even Pinterest. I think it might be even slightly more more relevant. Are there examples where you had, you know, potentially like a big target where the business is trying to optimize for, from a user perspective or behavior. Like love to maybe walk through like either a project or a lane that you were involved in to try to learn about kind of how you think through it and approach the problem.

**Mohit:** Yeah. So if you think about Pinterest. They try to, they have a generative AI, they might have, I don't know what's the situation over there now, but basically these images and you can think of them as feeding them to an encoder and create embeddings and then you try to find out what the recommendations could be. Now one of the things that I have been doing at Coupang, because we have lot of product summaries and we get it from the clients who use the platform and we try to push some of these products based on the usages. There is lot of data that is captured. I mean you think about the click level data, how much time the user is actually spending on a particular kind of thing. You can actually build a nice graph of the user so it's like a tree and you can actually compare the two users. You can see what's the overlap. Instead of going with the traditional collaborative filtering approaches or normal recommendation system, your retrieval is going to be spot on because you're looking at the trees instead of looking at some similarity search. That's what makes the solution much more robust.

**Mohit:** So one of the most recent projects if you have to talk about Roku. Basically at Roku you have a multi access recommendation system. I mean you could find it in other kind of media platforms like Netflix. And basically the main challenge that we were facing is a feature store and how the feature store would actually be used. We needed it because you need to capture a lot of things around media platforms like how much time the user is actually spending on a particular content, what's the browsing time, if you are seeing some kind of genre that the user is interested in. And you also have to check for things like most of the recommendation systems have problem with cold start. Because you don't know what to recommend to the user. That was one of the main problems that we were seeing at Roku in the beginning.

**Mohit:** Now to combat this kind of situation, what I did is basically create these feature stores across the various kind of dimensions. I made that retrieval part much more simpler. I did not use any LLMs for this because the scope is kind of different. Although there are few generative aspects to it. Like they might use SLMs for few of the description generation sort of things. But if I have to talk about the main challenge that was mainly to build the feature store. And once you have the feature store you can pretty well use any kind of hybrid CF based approach like collaborative filtering. And you can also put in any kind of encoders over there if you want to encode other stuff.

**Mohit:** The other part that's kind of difficult to speculate is, you know, what the score would actually be. What kind of metrics we should be actually looking at when we have these kind of recommendations coming in. Over the years a lot of features actually went into it and those were the main key challenges on the technical side of things. But I think most of the time we were battling through the issues. How we will get the data, what kind of GDPR or region based restrictions are there. So a lot of data governance level issues were actually there.

**Marcel Santilli:** Yeah, that's helpful. How would your manager like describe you at the end of that project?

**Mohit:** I would say that he was really happy with my work and he would see me as definitely not like a thought leader because I was more involved in the technical side of things, but definitely as a very good innovator. And a person who comes and just solves problems. I have been silently tackling these problems one by one. I was helping out my team. I had two engineers that were kind of reporting to me, so I was always very helpful to them. If I see that somebody is slacking a bit, I try to do pair coding sessions with them and find out what's actually causing them not to finish their work.

**Marcel Santilli:** And how would your peers in that project or that time period describe you?

**Mohit:** I try to maintain a very light environment around the work and I kind of make sure that everybody has high spirits. Maybe they'll describe me as someone who's very friendly.

**Marcel Santilli:** What do you think, as you think about like the work you've done and the areas where you've been able to be really effective, what is your superpower? What's the thing that like, of why you're effective and good at what you do?

**Mohit:** I think the main aspect of any kind of approaching the problem is you have the foundation very good. I try to identify the problem very clearly, like what the problem is and I try to solve it as much as possible. Over the years I have accumulated all the experience and I find it easier to break it into smaller tasks. I need to make sure that my peers, my superiors, everybody is well informed of what's actually going on. So communication is key aspect over here and I try to keep it at the maximum so that you don't have a bad surprise and you are also well connected with what your engineers are doing. On the engineering side of things, on the technical aspect side of things, I do a lot of paper reviews and I try to follow a lot of AI blogs as well. Meta's AI blog is really, really awesome.

**Marcel Santilli:** How do you like to learn? What sparks your curiosity? Where do you go to learn?

**Mohit:** Earlier it was very difficult to learn but these days I just take a paper, I go to Notebook LM, I throw it over there, I tell it to create any kind of notes for me, visuals for me, explain me the equations. And I know Notebook LM is actually a very good ranker. It's a very good search and it finds out the exact kind of things. I like the fact that it does not try to inflate the thing. It does not try to put things from the Internet like you would see when you're using any of the other LLMs.

**Mohit:** So that's one of the things I try to use a lot these days. If I find a piece of code, I follow code creators. I follow a lot of very good code content creators and AI content creators on LinkedIn. They keep pushing these posts and you just need to go through them. I follow a lot of Meta blogs. I try to do few small experiments around it just to understand the scope of what they were trying to achieve. Because most of the time what I've seen is even if you think you understood what the person is trying to say, if you kind of apply it, you get a new dimension to your thinking.

**Marcel Santilli:** Well, I know we don't have a ton of time, but happy to go over a little bit too. Happy to answer some questions as well.

**Mohit:** Yeah. I think I spoke with Daniel and Katya about the AI aspect of things and I know that this is going to be the first hire in the AI side of things because I heard from Katya that she's kind of outsourced. She's not directly from GrowthX. So I think I will be starting to build the culture and that will put the next members in the team one by one. In the first few months, what would be your expectations so that I can stand out and do good on your expectations?

**Marcel Santilli:** Yeah, like, I think for me it's really making sure there's a really good framing and an understanding of the context of the company, what we're trying to achieve ultimately from like the outcomes that matter to our customers. I think folks on the build side, the technical side, especially research and things like that, it's very easy to just lose sight of the context and build empathy for the user, the customer, who we're doing this for and why it matters to them and what matters to them. And then try to, once you frame that shape, what is the problem we're actually solving for that user or customer and what we're not solving for right now in this project or this lane.

**Marcel Santilli:** Really kind of shape that in a good way and then figure out how can we be pragmatic and what do we need to build and what do we need to learn? And not trying to boil the ocean. Instead, really think through what is the question we're trying to answer. You can solve the wrong problem, that's bad. But if you solve the right problem in the wrong way, that's bad. So you have to solve the right problem in the right way. And then if you solve the right problem in the right way at the wrong time, that's actually still wrong. So it has to be the right problem in the right way at the right time.

**Marcel Santilli:** Picking the right problem to solve is really, really important. Figuring out if that is the right problem to solve right now. Then that you're doing it in the right way, in the right order. In order to do that, it's like context is so important. Not being too quick to just jumping into a solution or assuming that we're picking the right problem.

**Mohit:** Yeah, I think that's a very important thing. You need to be right at the time of the problem and the way you solve it. I think that's going to define the next steps. You can't mess up any of those. That's great. And thank you for sharing that with me.

**Marcel Santilli:** Awesome. Well, I appreciate it, man. Great chatting. And hopefully we'll chat soon and I'll regroup with Daniel, and hopefully move things quickly as well to get back to you.

**Mohit:** Thank you so much. It was really nice talking to you. You will have a great weekend.

**Marcel Santilli:** You too.
