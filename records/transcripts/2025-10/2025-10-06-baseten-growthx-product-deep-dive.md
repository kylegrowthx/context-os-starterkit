# Baseten <> GrowthX | Product Deep Dive

<metadata>
date: 2025-10-06
time: 17:03 UTC
duration: 59 minutes
organizer: Erik O'Brien
participants: Rachel Rapp, Marylise Tauzia, Erik O'Brien
fathom_recording_id: 92108207
fathom_url: https://fathom.video/calls/430483022
share_url: https://fathom.video/share/ki2YTh-QKxzysyC8Uz4Q4TgmgaJAvyM7
source: fathom
enriched_on: 2026-03-02 10:32 UTC
</metadata>

---

## Summary

Erik from GrowthX conducted a deep product training session with BaseTen's Rachel Rapp and Marylise Tauzia to understand how to position the company's inference infrastructure in content. BaseTen's core pitch centers on three pillars — performance (30-70% lower latency and higher throughput than competitors), reliability (four-nines uptime powered by multi-cloud capacity management), and cost efficiency — all enabled by the BaseTen Inference Stack. Rachel walked through BaseTen's three products (Dedicated Deployments for scale, Model APIs for early-stage testing, and Training for engineers), modality-specific optimizations (LLMs, embeddings, transcription with 1000x real-time factor, image generation, and compound AI chains), and real customer wins (OpenEvidence's 78% latency reduction, Bland AI for voice agents). The team emphasized a content voice that's knowledgeable yet humble, showing rather than telling through customer examples, while avoiding "teacher" positioning.

---

## Context

GrowthX is working with BaseTen, a B2B inference infrastructure company that serves mission-critical LLM applications at scale. This was a product deep-dive training session to prepare GrowthX's content strategy for a major engagement with BaseTen. Rachel Rapp is a PM on BaseTen's core product team with deep technical expertise, and Marylise Tauzia leads product marketing at BaseTen. They provided extensive context on BaseTen's positioning, competitive advantages, customer proof points, and deployment architecture — all input for GrowthX to create content that helps BaseTen own the inference conversation in market. This is part of GrowthX's ongoing $200k+/year B2B content marketing engagements; the content strategy centers on translating technical expertise into relatable, customer-backed narratives rather than academic or didactic writing.

---

## Relevance

**To GrowthX Delivery:**
- Content positioning should emphasize BaseTen's customer wins (OpenEvidence, Zed Industries, Bland AI) over abstract technical messaging — "show, don't tell" through case studies with specific metrics (78% latency reduction, 3.6x throughput gains, 70% cost savings)
- Avoid "teacher" voice; instead position BaseTen as peer to developers with a knowledgeable yet humble tone, emphasizing transparency and control (open-source packaging, visible FDE work, customer ownership of model changes)
- BaseTen uses "compound AI systems" as a keyword but Rachel noted it hasn't gained broad adoption — recommend SEO research to validate best terminology for agent/multi-model workflows before heavy content investment
- Content should address modality-specific optimizations (embeddings, transcription, chains) separately with distinct use cases (search, medical scribes, pharma document processing, voice agents) rather than treating inference as monolithic

**To GrowthX Business Development:**
- BaseTen is likely in contract discussions with GrowthX given the training session scope; engagement appears foundational to their content roadmap overhaul (messaging doc needs refresh, competitor content strategy already exist)
- Client shows strong alignment on brand voice and is actively shaping market narrative — positioning BaseTen Inference Stack and MCM (multi-cloud capacity management) as differentiators signals they're preparing competitive messaging
- Renewal/expansion signal: Marylise explicitly asking for Erik's feedback on content strategy and requesting team reviews of search pages suggests high engagement and collaborative planning

**To CheckThat:**
- BaseTen's reliance on transparency, developer control, and open-source model support creates narrative alignment with CheckThat's visibility mission — models like Whisper, Quen, DeepSeek, Llama are core to BaseTen's positioning
- Training product launching in two weeks as "training for inference" signals emerging demand for fine-tuning + deployment workflows; potential early case study opportunity once GA'd

---

## Overview

- BaseTen offers three core products: Dedicated Deployments, Model APIs, and Training, all optimized for mission-critical inference
- Key differentiators: superior performance (latency/throughput), high reliability (4 nines uptime), cost efficiency, and transparent developer experience
- BaseTen Inference Stack combines model runtime optimizations and inference-optimized infrastructure for best-in-class performance
- Content strategy should emphasize technical expertise while maintaining a relatable, humble tone, leveraging customer examples

---

## Key Topics

### BaseTen Product Overview

  - Three main products serving the inference lifecycle:
      - Dedicated Deployments: Custom GPU deployments with full control
      - Model APIs: Pre-optimized, popular LLMs for quick testing and early-stage use
      - Training: Infrastructure-focused for engineers, enabling multi-node training

### Key Pillars and Differentiators

  - Four pillars: Forward-deployed engineers, Developer experience, Model performance, Infrastructure
  - Three main differentiators:
      - Performance: Consistently lower latency (30-70%) and higher throughput than competitors
      - Reliability: 4 nines uptime powered by multi-cloud capacity management (MCM)
      - Cost efficiency: Optimized resource usage leading to significant cost savings

### BaseTen Inference Stack

  - Combines model runtime optimizations and inference-optimized infrastructure
  - Model runtime: Includes modality-specific runtimes, custom kernels, speculation engines
  - Infrastructure: Handles routing, networking, auto-scaling, and multi-cloud management

### Modality-Specific Optimizations

  - Embeddings: 2x higher throughput, 10% lower latency, smallest memory footprint
  - Transcription: 1000x real-time factor, lowest word error rate
  - BaseTen Chains: Enables efficient compound AI workflows with independent scaling

### Deployment Options

  - BaseTen Cloud: Default option and single-tenant deployments
  - Self-hosted: Includes hybrid option for spillover to BaseTen Cloud

### Content Strategy Considerations

  - Aim for a knowledgeable yet humble tone, avoiding a "teacher" persona
  - Emphasize strong technical arguments while remaining relatable to developers
  - Focus on showing rather than telling, leveraging customer examples and case studies

---

## Action Items

**Marylise**
- Ask Mike re granting Erik Google Analytics + Search Console access

- Nudge team to review search pages for content strategy feedback


**Rachel Rapp**
- Review links in Cosex channel, provide thoughts on content strategy

---

## Transcript
**Rachel Rapp:** Hi.

**Rachel Rapp:** Okay, real quick, nice to meet you.

**Rachel Rapp:** Marylise is late.

**Rachel Rapp:** I need two more minutes.

**Rachel Rapp:** I didn't want you to think that we were super late, but give me two minutes.

**Rachel Rapp:** I'm here, but I just got to wrap something up.

**Rachel Rapp:** And then Marylise will be.

**Rachel Rapp:** So one second.

**Erik O'Brien:** Okay.

**Marylise:** Hi, everyone.

**Erik O'Brien:** Hey, Marylise.

**Marylise:** Sorry, I was.

**Rachel Rapp:** Sorry, I also just was wrapping up the marketing channel ask real quick and then.

**Rachel Rapp:** Cool.

**Rachel Rapp:** Yeah, pull up another new browser to not show you.

**Erik O'Brien:** My tabs, which is why I have so many tabs.

**Marylise:** You've got the deck up.

**Rachel Rapp:** Yeah, I'm pulling it up right now.

**Rachel Rapp:** Sorry, but I'm meeting.

**Marylise:** I opened it too.

**Rachel Rapp:** So if you want, I'm happy to do it.

**Rachel Rapp:** I got it.

**Marylise:** We're good.

**Marylise:** Okay, cool.

**Marylise:** Do you guys enjoy each other?

**Marylise:** I don't think you've met Rachel yet, Erik.

**Rachel Rapp:** I came on and I was like, give me two minutes.

**Rachel Rapp:** Anyways, hi.

**Rachel Rapp:** Nice to meet you, Erik.

**Rachel Rapp:** I'm Rachel.

**Rachel Rapp:** I'm a PM on Marylise's team.

**Erik O'Brien:** I work on our core product.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** And I'm Erik O'Brien.

**Erik O'Brien:** I am an account strategist at GrowthX.

**Erik O'Brien:** So working with Marylise and the team as we get ramped up with everything BaseTen and get started on content production.

**Rachel Rapp:** Great.

**Marylise:** So it's just you today and then you'll pass the info to everyone, basically?

**Erik O'Brien:** Yep, yep.

**Erik O'Brien:** So that's when we got our recorder going.

**Erik O'Brien:** I've got a separate note taker going as well.

**Erik O'Brien:** So it should cover all grounds.

**Erik O'Brien:** And just for kind of brief context.

**Erik O'Brien:** it's...

**Erik O'Brien:** Goals today is to kind of go deep on how you tell BaseTen's story, especially around performance, reliability, and kind of why teams choose BaseTen.

**Erik O'Brien:** So really trying to look to understand how you frame the product to different audiences, what proof points or examples you lean on, and then obviously we'll kind of turn that into kind of where content can help amplify most of that.

**Erik O'Brien:** So less of a formal interview, more like a working session, just to kind of hear how you guys position BaseTen and how we can translate that into some content that helps own the inference conversation.

**Marylise:** Cool.

**Marylise:** And I wanted to bring Rachel on because she's like the oldest on the team.

**Marylise:** She's got a lot of like product context and she's more technical, so she would be great for all that.

**Marylise:** I'll jump in.

**Rachel Rapp:** And say, Marylise, I remember there was a messaging doc that you put together a while ago.

**Rachel Rapp:** That might be, I don't know if it's still, if things have shifted much.

**Marylise:** I it needs to be updated.

**Marylise:** Okay.

**Marylise:** showed it to Dani a couple weeks ago.

**Marylise:** She wanted to see it, but I don't think she gave me any feedback.

**Rachel Rapp:** But with the whole.

**Rachel Rapp:** The whole performance thing going on, it's a great idea to refresh it.

**Rachel Rapp:** Cool.

**Rachel Rapp:** Okay.

**Rachel Rapp:** So if it's cool, Erik, we have some slides that we use also for training our sales team in a little bootcamp.

**Rachel Rapp:** So I'll just go through there and then maybe, you know, interrupt as you have questions.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Works perfect.

**Rachel Rapp:** Let me just share my screen.

**Rachel Rapp:** Again, I have too many things open.

**Rachel Rapp:** It never gets better.

**Marylise:** Until you go through your questions and you lose everything.

**Rachel Rapp:** And then I like urge a bunch of tabs, but not the ones where I'm like, oh, these might be useful.

**Rachel Rapp:** And then, yeah, it's a disaster.

**Rachel Rapp:** So let's see if it behaves, but cool.

**Rachel Rapp:** Okay.

**Rachel Rapp:** So just to give you a high level of, you know, what is BaseTen, what are our products?

**Rachel Rapp:** So I'd say at a really high level, everything that we do at BaseTen is in the service of inference and in particular mission critical inference.

**Erik O'Brien:** So that's typically, you know, inference.

**Erik O'Brien:** And do you know what inference is?

**Erik O'Brien:** Sorry.

**Rachel Rapp:** Okay, so inference that typically affects like an end user somewhere that, you know, our customers have products that their customers are interacting with.

**Rachel Rapp:** So the performance of their products is directly affecting their end users.

**Rachel Rapp:** And to serve that whole inference lifecycle, we have three main products.

**Rachel Rapp:** Sort of our bread and butter is this one in the middle, the dedicated deployments.

**Rachel Rapp:** That's how we started as a company.

**Rachel Rapp:** This means that you have GPUs that are running for you.

**Rachel Rapp:** You know, you sort of, you don't necessarily own the hardware, but you do, you know, you pay per usage.

**Rachel Rapp:** So you own it for that time.

**Rachel Rapp:** can do it on demand.

**Rachel Rapp:** So that's like your model running on the GPU that you choose.

**Rachel Rapp:** You can also choose, you the region it's located in, but it's just very customizable, you know, workload specific, dedicated, like a dedicated deployment of your model for you.

**Rachel Rapp:** You can control the auto scaling settings.

**Rachel Rapp:** can control everything around there.

**Erik O'Brien:** Does that make sense so far?

**Erik O'Brien:** Yep.

**Rachel Rapp:** Cool.

**Rachel Rapp:** So the second one is the model APIs.

**Rachel Rapp:** So in this case, you have like a pre-optimized front.

**Rachel Rapp:** Tier model, we choose like very popular models right now, all LLM specific, so large language models.

**Rachel Rapp:** These are going to be models like the DeepSeqs, the Llamas, the KimiK2s, the ChatGPT, or not ChatGPT, sorry, GPT OSS.

**Rachel Rapp:** All of those, there's like the QuenCoder, I think is another one.

**Rachel Rapp:** So those LLMs that we see a lot of usage around for use cases from, you know, everything from chat to code generation is a really big one.

**Rachel Rapp:** So those pre-optimized models, we have it running on our hardware.

**Rachel Rapp:** You get the API endpoint, you can ping that.

**Rachel Rapp:** And in that case, instead of being a usage or consumption-based model, like the dedicated deployment, where it's really your hardware, instead it's really looking at inputs and outputs.

**Rachel Rapp:** So you're going to send tokens into the model, and you're going to get tokens back out, and that's also how the billing works.

**Rachel Rapp:** And that's sort of like, I would say, you know, that's what you see a little bit more frequently in the field.

**Rachel Rapp:** There are other players that have, you know, like if you ever wanted to try out like a DeepSeq that's running somewhere and you get an API endpoint, that's sort of the high-level concept there.

**Rachel Rapp:** And there are the important things that are still, you you want

**Rachel Rapp:** To be reliable, to be fast, and all of those things, the quality to be there.

**Rachel Rapp:** The last one is training.

**Rachel Rapp:** It's sort of in the name, but our training product is very infrastructure-focused, so it gives you really the hands-on ability to really touch the code.

**Rachel Rapp:** It's not like there's other training products that are like a really big abstraction where you get a UI and it's completely UI-based.

**Rachel Rapp:** Ours, on the other hand, is like very infra-based, so you can do like multi-node training, which means that you can do like really large data sets.

**Rachel Rapp:** You have like that whole workflow that lets you take those models that you're training and then deploy them into production, so it's still in sort of this like inference loop, but at a very infrastructure level for our training product.

**Rachel Rapp:** So those are sort of our three main products that, you know, everything will tie into them, and I actually want to, if it's okay, I want to jump ahead real quick, because Yeah, to me, well, let me see, sorry, I think we, yeah, so, so, hmm.

**Marylise:** later.

**Marylise:** Bye.

**Marylise:** Bye.

**Marylise:** Yeah, the deck changed.

**Rachel Rapp:** I know I got cautious, too.

**Rachel Rapp:** Yeah, I'm just kidding.

**Rachel Rapp:** Because the way I like to think about it, way, you know, and sorry to jump around here, I just know, because it's not an actual sales, you know, things.

**Rachel Rapp:** I don't have to go right in that flow.

**Rachel Rapp:** I just, you know, when I think about BaseTen, we really have these four pillars.

**Rachel Rapp:** We have those three products, and they sit on top of these four pillars.

**Rachel Rapp:** And the first is, you know, our forward-deployed engineers, they work really closely with our customers.

**Rachel Rapp:** They optimize the workloads for them.

**Rachel Rapp:** They optimize those, you know, pull all the different levers of, like, you know, performance, quality, cost efficiency, uptime, like all of those really important parameters for our customers.

**Rachel Rapp:** They work as an extension of their teams to make sure that all of those different SLEs are met.

**Rachel Rapp:** And then, so that's a big thing that we push is our forward-deployed engineering team.

**Rachel Rapp:** They're sort of like the celebrities, the superstars of our company.

**Rachel Rapp:** They work, you know, our customers really rave about them.

**Rachel Rapp:** So we like to highlight them.

**Rachel Rapp:** The second is the DevEx, or developer experience, model management, everything that has to go with our UI.

**Rachel Rapp:** So in contrast, for competitors that often deliver things that are like a black box.

**Rachel Rapp:** So you don't...

**Rachel Rapp:** They might come to you and say, oh, this is your performance metric, this is your latency, this is your throughput, whatever, but you can't really understand how they got there.

**Rachel Rapp:** So if you do have a technical team and you want to know, oh, well, did you try this?

**Rachel Rapp:** Did you try this?

**Rachel Rapp:** You really have no idea.

**Rachel Rapp:** And if you want to make any changes there, that's, I think, a quote that I love from a prospect was like, that's a human in the loop that we don't have access to, right?

**Rachel Rapp:** So that's something that you can't actually touch and get your hands on and get involved with.

**Rachel Rapp:** So in contrast to that, we're very, very transparent.

**Rachel Rapp:** The library that we use to package models is open source.

**Rachel Rapp:** You can look at all of the code.

**Rachel Rapp:** Everything that our FDEs do is completely transparent.

**Rachel Rapp:** You own the changes that are done to your model.

**Rachel Rapp:** If you want to pack up and go somewhere else tomorrow, you can.

**Rachel Rapp:** It's always your model.

**Rachel Rapp:** It's not a black box.

**Rachel Rapp:** And all of the performance is very transparent.

**Rachel Rapp:** So on the one side, there's that.

**Rachel Rapp:** On the other hand, it's just that control that either from the UI or the CLI, you can really go and do everything yourself.

**Rachel Rapp:** And then the other is going to be the, another big one, of course, performance is our model.

**Rachel Rapp:** Performance team, just optimizations, everything around, like, we call this now, we used to have these, yeah, sort of these two different pillars, the model performance and then the actual infrastructure, so that would include, like, the hardware, the scaling, and we've packaged now both of those into this thing that we call the BaseTen inference stack, so I think that's something that we're going to hit on a lot in content, and we have a guide on that on our website, you can find, you go under resources and then guides, and it's, we only have four, so it's one of those four.

**Rachel Rapp:** It's really good, really long, very in-depth, but it basically packages a lot of the things that we do on the model performance side and on the infrastructure side to make things so fast and so reliable, so the way that I like to think of these two is the model runtime, to me, is really, like, synonymous with the work of our model performance team and a lot of the model level optimizations that we do to make things super fast.

**Rachel Rapp:** I mean, we win on speed all the time with customers, we, you know, people turn from our competitors and come to us because we can hit just a much lower, like, 30% to 70% lower latency, higher throughput than our competitors that they're

**Rachel Rapp:** We're already on.

**Rachel Rapp:** This happens regularly.

**Rachel Rapp:** And then on the infrastructure side, where that comes in, it does also play a role for performance, is the consistency of that performance.

**Rachel Rapp:** So let's say that you want to have like 400 millisecond latency on an AI phone call.

**Rachel Rapp:** Well, you want to have that latency, whether you have five users or 5,000 or 5 million.

**Rachel Rapp:** Like, let's say you go viral.

**Rachel Rapp:** You want to be able to meet that demand and keep meeting that latency SLA.

**Rachel Rapp:** And in order to do that, you need to be able to scale efficiently.

**Rachel Rapp:** You need to be able to have access to the compute.

**Rachel Rapp:** That compute needs to be located close to your customers.

**Rachel Rapp:** You need to have the networking in place, the request routing in place, the cold starts in place.

**Rachel Rapp:** And all of that is an infrastructure challenge.

**Rachel Rapp:** That's not really at the model side.

**Rachel Rapp:** That's on the infrastructure side.

**Rachel Rapp:** So the infrastructure does touch the performance from that perspective of the latency, of the consistency of the latency.

**Rachel Rapp:** And also does play with the latency a little bit because like networking and all that comes into play as well.

**Rachel Rapp:** But on the other hand, what we also think of for the infrastructure is going to be around reliability, right?

**Rachel Rapp:** So all of this at the end of the day runs on GPUs.

**Rachel Rapp:** A lot of it's packaged.

**Rachel Rapp:** Different ways, either single models, compound AI workflows, and that all needs to be very reliable and highly available.

**Rachel Rapp:** So you need to be able to, again, like, you know, if the cloud fails, you need to be able to scale elsewhere.

**Rachel Rapp:** you run out of capacity, you need to be able to scale elsewhere.

**Rachel Rapp:** And that's something we also take into account with our inference-optimized infrastructure.

**Rachel Rapp:** And go back here.

**Erik O'Brien:** Outside of latency and throughput, what are other kind of performance-related metrics you guys track for clients?

**Rachel Rapp:** I'd say there's really, those are sort of the two high-level categories.

**Rachel Rapp:** Throughput, you can think of, throughput to me is mainly just throughput.

**Rachel Rapp:** There's different ways to measure throughput.

**Rachel Rapp:** can think of, like, overall throughput.

**Rachel Rapp:** You can think of token throughput.

**Rachel Rapp:** But I think generally we just do, like, yeah.

**Rachel Rapp:** I mean, it depends on the context.

**Rachel Rapp:** If it's overall, like, request throughput or token-level throughput.

**Rachel Rapp:** So we just use throughput sort of generically.

**Rachel Rapp:** But latency, you can break down into, like, end-to-end latency.

**Rachel Rapp:** So that's the time from, like, when you send a request.

**Rachel Rapp:** And

**Rachel Rapp:** And you get the full response back.

**Rachel Rapp:** And then you're going to have another really common measure of latency is going to be time to first token, for instance, token for LLM.

**Rachel Rapp:** Or if you're doing a voice AI application, it's going to be time to first byte.

**Rachel Rapp:** So the first time that a byte of audio is turned back to you.

**Rachel Rapp:** And those are really important for the LLM and the voice AI use cases because as soon as you start hearing a response or seeing a response, the end user still has that feeling of like they're getting a response.

**Rachel Rapp:** And those are typically abbreviated as TTFT or TTFB.

**Marylise:** And what about cold starts, Rachel?

**Rachel Rapp:** Like it's also like performance related, right?

**Rachel Rapp:** It is.

**Rachel Rapp:** We do talk about cold starts.

**Rachel Rapp:** We don't put numbers on them.

**Rachel Rapp:** And the reason for that is just that it's very, we've done a lot of optimizations around cold starts.

**Rachel Rapp:** We're going to do more optimizations around cold starts.

**Rachel Rapp:** And it's just a very high variability.

**Rachel Rapp:** So, you know, some cold start, especially it depends on the model, depends on the workload.

**Rachel Rapp:** depends on if the person's doing caching or not.

**Rachel Rapp:** You know, if we can cache the weight somehow, if we, you know, have enough, if they have enough load, then we might have like a warm replica somewhere, meaning that it's already kind of prepared for them.

**Rachel Rapp:** more on the model.

**Rachel Rapp:** So it could be anywhere on the scale of like 20 seconds to three minutes, and you know, how impressive that is also depends on the model, and you know, so we've been a little bit wary of how we talk about cold starts, but yeah, Marylise, you're right, that's definitely something we should talk about in performance, just, you know, when we put a number on it, we need to be careful.

**Marylise:** Yeah.

**Marylise:** And you know, Erik, I mean, from a performance perspective, so there's the product side, but there is here a side of the story that I like to tell, because I think he also shows performance in another way, that our team is extremely fast and responsive, and our customers talk about it, and there is one like being fast and responsive to customers' requests, which I think we're really good at, but also being fast and responsive with the market.

**Marylise:** So new models get put out, like, you know, any day, and generally we get no notice, or we're like, we do, but we support them.

**Marylise:** The library within 24 hours, so they become available really quickly, and our customers love that from a team performance perspective to support them.

**Marylise:** So it's just something to have in mind as well, because I think it's part of the story.

**Erik O'Brien:** Wonderful.

**Rachel Rapp:** Cool.

**Rachel Rapp:** Anything you want to dive into now, or is it cool if I keep going?

**Erik O'Brien:** Yeah, just keep going.

**Rachel Rapp:** It's been good so far.

**Rachel Rapp:** Yeah, so some of these features that you can see here are really sort of, we call them like model runtime optimizations that are tuned to specific modalities.

**Rachel Rapp:** So there's six different, we call them model modalities.

**Rachel Rapp:** That's really five, and then compound AI that we specialize in.

**Rachel Rapp:** So this is going to be sort of your typical gen AI buckets, right?

**Rachel Rapp:** So large language models, voice synthesis, or text-to-speech, same thing.

**Rachel Rapp:** Image generation, embeddings, compound AI systems, and transcription.

**Rachel Rapp:** And I think also also, you could add, actually, video

**Rachel Rapp:** So those are these features that you see here.

**Rachel Rapp:** These are different optimized applications that our different engineering teams have done.

**Rachel Rapp:** So BaseTen embeddings inference is like the fastest package for embeddings inference on the market.

**Rachel Rapp:** It's like, I mean, don't quote me on the metrics that are on the blog.

**Rachel Rapp:** I think it's like 3.something, 3.6x higher throughput, and then 10% lower latency.

**Rachel Rapp:** Again, that's going to vary a little bit based on the hardware and the workload, but faster than every other embeddings tool out there that you can use.

**Rachel Rapp:** So we have great products for embeddings, for chains.

**Rachel Rapp:** This is built for Confed AI Systems.

**Rachel Rapp:** It lets you deploy a chain of different models and processing steps, everything on its own hardware with its own auto-scaling.

**Rachel Rapp:** And this way, you don't have like these monolithic deployments where you have certain tasks blocking the GPU.

**Rachel Rapp:** You can scale independently.

**Rachel Rapp:** So for transcription, for instance, we use this for the next feature.

**Rachel Rapp:** We have also the best transcription product out there in terms of actual speed and cost and quality.

**Rachel Rapp:** When comes to open source, and we power that with chains because you can use like, you know, you can do chunking of the audio where you cut the audio into little pieces and you can run that on like a CPU or a much cheaper GPU like an L4, and you can scale that up massively to do that really fast and parallel.

**Rachel Rapp:** And then you can hand that transcription off to the actual model that's going to be doing the speech-to-text transcription.

**Rachel Rapp:** And then you can send that back or you can like iterate over it.

**Rachel Rapp:** You can use an LLM afterwards to do like quality control on the end product, and you can do all of that like on different hardware and different auto-scaling, and that just totally speeds up the process and makes it more cost-efficient because now you have, you know, the right type of hardware running for each step in your workflow.

**Rachel Rapp:** I'm trying to think, Marylise, is there anything else that we have modality-wise that I'm missing?

**Rachel Rapp:** I think those are the big three.

**Rachel Rapp:** I know we have now also for, it's called diarization, which is basically like speaker identification, but we haven't talked about that publicly yet, but that'll be coming soon in the next few weeks, hopefully.

**Marylise:** I think the one thing I wanted to say, but it's a modality that's part of LLMs, but we have been seeing a lot of really, really strong success with coding platforms.

**Marylise:** So it's a subset of LLM, it's in the same world, but we are doing really, really well there.

**Rachel Rapp:** Yeah, good point.

**Rachel Rapp:** And we have a case study that you can look there that's with Zed Industries, and they have great metrics on latency and throughput that we've been able to achieve.

**Rachel Rapp:** Let me see if I can.

**Rachel Rapp:** I already have our homepage pulled up, go away, Zoom.

**Rachel Rapp:** Sorry, Zoom.

**Rachel Rapp:** I think my computer is punishing me now because I have too many things open.

**Rachel Rapp:** But if you look at our customers page in general, you'll notice a lot of these are very performance oriented.

**Rachel Rapp:** I know at the beginning you had some points about, you know, how do we like to communicate this?

**Rachel Rapp:** you.

**Rachel Rapp:** But

**Rachel Rapp:** Especially from like the customer angle, so you can see everything is very performance-oriented.

**Rachel Rapp:** can pull from a lot of these.

**Rachel Rapp:** And Zed Industries, yeah, 3.6X higher throughput, 45% lower P90 latency.

**Rachel Rapp:** And, you know, I love this number because it actually was already, it was on one of our competitors and they had already optimized it for very low latency.

**Rachel Rapp:** So, like the best they could do was the number they came in at and we brought it down another 45%.

**Rachel Rapp:** Yeah, so definitely a good resource here is to go to our customers page, calling it out because it's a little bit tricky to find out.

**Rachel Rapp:** We're also going to be redoing this page.

**Rachel Rapp:** But if you go to customers, then you have to scroll down, scroll down, and then here are our case studies.

**Rachel Rapp:** Cool.

**Rachel Rapp:** And the last call out, and again, this is going to change a little bit.

**Rachel Rapp:** I think the sort of the high level that you need to take away from the deployment options is just that we can do this anywhere.

**Rachel Rapp:** We can do this in any cloud.

**Rachel Rapp:** We have partnerships with nine different clouds, including the big hyperscalers that people...

**Rachel Rapp:** Typically we use like AWS and GCP.

**Rachel Rapp:** So when we talk about BaseTen cloud, which is what we typically default to, that's running across these nine different clouds that we have partnerships with, but we can also do self-hosted deployments.

**Rachel Rapp:** We can do sort of an in-between that's called single tenant, meaning that the cluster is just for you.

**Erik O'Brien:** You're not sharing the cluster with anybody else.

**Erik O'Brien:** And then under the self-hosted sort of umbrella, we can also do hybrid, which means that you self-host your workload.

**Erik O'Brien:** And if you run out of capacity, you can spill over to BaseTen cloud.

**Erik O'Brien:** What's the use cases for kind of each of those cloud deployments?

**Erik O'Brien:** Like, just so I have it on transcript here, is there specific instances or is it more a client preference?

**Rachel Rapp:** Yeah, I think you hit the nail on the head there.

**Rachel Rapp:** A lot of it with the self-hosted is going to be, you know, IP, regulated industries, healthcare, finance.

**Rachel Rapp:** If you have anything that just can't leave your VPC, maybe you have, like, you know, something in place with clients already.

**Rachel Rapp:** That they're fine being in the AWS ecosystem, but they can't leave that.

**Rachel Rapp:** So, you you kind of just want to stick on what you already have, what they have their customers that have already signed agreements for, that they're willing to be in that environment.

**Rachel Rapp:** So they want to stay in that environment.

**Rachel Rapp:** That's typically in the self-hosted case.

**Rachel Rapp:** On the, you know, on the hybrid case is that if you run out of capacity and you do have some workloads that aren't as sensitive, then you could spill over and run that capacity.

**Rachel Rapp:** And our cloud, as I don't have, you know, if you're using like a really high-end GPU, those are typically harder to get, especially on demand.

**Rachel Rapp:** So if you have a launch or something like that, then you have sort of that flex capacity.

**Rachel Rapp:** The single tenet is sort of a compromise there.

**Rachel Rapp:** So you don't have such strict security or IP requirements that it actually needs to be in your VPC, but you still want to have that assurance of like, you it's just a cluster running for you.

**Rachel Rapp:** There's no other customer or any other workload that's going to be on that cluster.

**Rachel Rapp:** And then BaseTen Cloud, I mean, of course, still very, very secure.

**Rachel Rapp:** It's typically a technicality when people need to do the self-hosted.

**Rachel Rapp:** But BaseTen Cloud, the biggest point there is just time to market, right?

**Rachel Rapp:** Like, who can...

**Rachel Rapp:** It gets started in hours.

**Rachel Rapp:** Literally, you know, we're open AI compatible, so you just change a line of code.

**Rachel Rapp:** It takes, like, no time to get up and running.

**Rachel Rapp:** So definitely fastest time to market there.

**Marylise:** But I would say in terms of customers choosing, like Rachel said, if they go self-listed, generally, they want to choose.

**Marylise:** They're like, I have reservations at AWS, I want to use it with BaseTen, so they will say, I'll go there.

**Marylise:** But, like, if they do BaseTen Cloud, it's going to be us choosing where the loads go.

**Marylise:** And that's also where they get all the benefits of what we call our MCM product, like multi-cloud capacity management, where that's when, like, you know, we send the loads where we need to.

**Marylise:** And then if one of the providers go down, then we can load balance very easily.

**Marylise:** So that's really where you get the whole benefits of BaseTen.

**Marylise:** But if you don't care about where it's hosted, then you leave it with us.

**Erik O'Brien:** Yep.

**Rachel Rapp:** Bon.

**Rachel Rapp:** Bon.

**Rachel Rapp:** Thank

**Rachel Rapp:** So I know we already went a little bit into our different products, but just to give a little bit more, shed a little bit more light on the use cases here, so we typically position model APIs around people who are just sort of testing something out, maybe there's a new model, you want to see how it performs in your workflow, see how the quality is, and maybe you're still building a POC, you're just very early in your journey and you don't have the amount of scale that would justify having like an actual dedicated deployment running for you, that's when we position our model APIs around.

**Rachel Rapp:** For the dedicated deployment side, that's when you actually have that scale, you know, can scale pretty much limitlessly.

**Rachel Rapp:** So if you have like, you know, you're launching something, you already have a big, you know, consumer base, you're a scale up in enterprise, then the actual dedicated deployment where you have that hardware running for you and you can control the auto scaling settings and everything around it, that's when that would come in.

**Rachel Rapp:** And then training, because our training product is a little bit lower level and it's a little bit closer to the actual training infrastructure, we position it for engineers, like it's not, you know, one of the...

**Rachel Rapp:** These very abstracted UIs, it's not for, you know, like, tinkerers or people who want, like, the lowest lift to try to sort of fine-tune a little model.

**Rachel Rapp:** It's really, you know, for people who are a little bit more serious and they, you know, they're comfortable writing the code, they're comfortable working at a lower level, and that's when we position our, or where we position our training product.

**Rachel Rapp:** Yeah, so again, this is, like, the inference lifecycle that I mentioned a little bit in the beginning, so you can come in and sort of test and scale new models with these model APIs, and then you can just sort of swap them out and try different models and figure out what works best for you.

**Rachel Rapp:** You can fine-tune them with training, or you can even train your own custom models, and then you can deploy those into production and run them at scale with Dedicated, and that's sort of this, this lifecycle that we see here with the three different products.

**Erik O'Brien:** And do four deployed engineers work across?

**Erik O'Brien:** This kind of customer journey, or is there a certain point in which they engage, like, step two or step three?

**Rachel Rapp:** Typically three.

**Rachel Rapp:** So FDEs are going to come in at the dedicated level most frequently.

**Rachel Rapp:** We do have machine learning engineers who work on the fine-tuning and the training.

**Rachel Rapp:** But, again, it would have to be sort of a bigger use case.

**Rachel Rapp:** Oh, sorry, my throat's a little scratchy.

**Rachel Rapp:** Yeah, so MLEs are, I mean, so we haven't actually GA'd our training product yet.

**Rachel Rapp:** So I think we don't know yet, Marylise, correct me if I'm wrong, but we don't know exactly what would be the criteria for when an MLE jumps on a deal or actually gets involved.

**Rachel Rapp:** Whereas for the FDEs, I think it's pretty much, like, if you're qualified for dedicated and you do have some skill, then our FDEs would be involved.

**Rachel Rapp:** And the model APIs are, like, completely self-serve, typically, unless you're, like, you know, there are some products where the product is built around model APIs.

**Rachel Rapp:** Like, we've worked with companies like Retool, where they have, I think it's, like, an agent builder platform.

**Rachel Rapp:** And then that's completely more.

**Rachel Rapp:** So if you are like, your product revolves around the model APIs and integrating the model APIs, then I think FTEs would get involved, but typically they're more on the dedicated side.

**Marylise:** Yeah, for training, no, go ahead.

**Erik O'Brien:** was just curious if there was, you know, new customers coming in at that kind of model API level, and they just need kind of coaching or direction on, you know, which models are best for our use case or product.

**Erik O'Brien:** But it sounds like there's some, you know, some instances where that's a possibility.

**Rachel Rapp:** Yeah, I think there is.

**Rachel Rapp:** It's something we've talked about, and I'm sorry, I missed the earlier meeting, so I don't know.

**Rachel Rapp:** I don't have, like, full, you know, context purely out of my own ignorance there about what the scope is that you guys are working on.

**Rachel Rapp:** But something we have talked about is having content around, like, when to use which model, you know, what are the use cases that we see particular models being used around and just more model-specific content.

**Rachel Rapp:** I think also our competitors.

**Rachel Rapp:** have some of that content as well, where they have like a, you know, these are the models that we recommend for different use cases.

**Marylise:** Yeah.

**Marylise:** Yeah, and there's a lot of that, like, I think it's, we start to see it with modern APIs of like, yeah, which model do you recommend?

**Marylise:** Like, think later than last week, we had this type of questions.

**Marylise:** So people want to know.

**Marylise:** But yeah, we, it's, you know, we still have a lot to do there.

**Marylise:** And I want to say, want to say for training, it's still like, you know, so we were looking actually going GA in, in two weeks.

**Marylise:** Products has really gone a very long way.

**Marylise:** But right now it's going to be positioned as like a training for inference.

**Marylise:** Not like we're trying to kind of exclude as much as we will be able to, like people coming to us just to train.

**Marylise:** You know, everything we do is in service of inference.

**Marylise:** And then that release is also saying that.

**Marylise:** So you come in, you're training your model and, you know, we make it so easy for you to deploy and do inference on base 10 in the future, we still.

**Marylise:** We to have a training for training, but like this GA version will still, you know, but we actually have two customers in beta who are doing training for training.

**Marylise:** So we know it works really well for them.

**Marylise:** We're just trying to kind of like right now, limit the ICP a little bit.

**Marylise:** But our engineering team definitely helps most of them still.

**Rachel Rapp:** And so I know we sort of jumped ahead here a little bit and hinted at this.

**Rachel Rapp:** The three things that we've been also sort of hitting on whenever we hit on any of our products or any of our offerings is these three things.

**Rachel Rapp:** Performance.

**Rachel Rapp:** Everything is super fast.

**Rachel Rapp:** Best in class performance.

**Rachel Rapp:** The lowest latency.

**Rachel Rapp:** The highest throughput.

**Rachel Rapp:** And this is something that we're really doubling down on.

**Rachel Rapp:** So this is really going to be the number one thing that we want to emphasize.

**Rachel Rapp:** And then from their reliability, we have better reliability than, I think, all of our competitors.

**Rachel Rapp:** The way we power that is through something that

**Rachel Rapp:** We call multi-cloud capacity management, which essentially abstracts all of the different clouds that we run on so we can just scale models up on any cloud.

**Rachel Rapp:** We basically treat them as sort of one global cloud as opposed to the nine different ones that lets us scale beyond capacity constraints, that lets us scale beyond hardware failures.

**Rachel Rapp:** You know, when a cloud goes down, our competitors go down for hours and we just scale models up in a different cloud.

**Rachel Rapp:** So we power really good reliability.

**Rachel Rapp:** We typically say that we power four nines reliability.

**Rachel Rapp:** And then, of course, cost efficiency.

**Rachel Rapp:** This one, to me, goes really hand in hand with the performance.

**Rachel Rapp:** What I like to stress is that even if you're going to spend a little bit more on hardware, let's say like you're using a B200 and some people might say, oh, well, it's just a more expensive GPU.

**Rachel Rapp:** You know, but if you're just like, let's say you're 1.5 X-ing the cost, but you get three times the throughput, you're actually going to be saving costs overall because things are just so efficient and you're using the hardware maximally.

**Rachel Rapp:** And a lot of our tooling, if not all of our tooling, is built around that.

**Rachel Rapp:** So it's a built around getting the most of the hardware, the highest throughput and the most bang for your buck.

**Rachel Rapp:** And this is something that we also sort of skipped ahead of, but I think to me this is really like everything sits again on these four pillars.

**Rachel Rapp:** The first, the four deployed engineers, the developer experience of you actually being able to, you know, lift up the hood and see what's going on and do things yourself and not being totally dependent on our team.

**Rachel Rapp:** We also have a lot of customers that are power users of the product and one of them is latent.

**Rachel Rapp:** We also have a case study with them that you can see on our website, the model performance team and our infrastructure team as well.

**Rachel Rapp:** And we couple those two again into this now, this product that we talk about, the BaseTen inference stack.

**Rachel Rapp:** And we say everything runs or everything is powered by the BaseTen inference stack.

**Rachel Rapp:** It powers our super high performance.

**Rachel Rapp:** It powers our super high uptime.

**Rachel Rapp:** Cool.

**Rachel Rapp:** Some customers.

**Rachel Rapp:** Oh, yeah.

**Rachel Rapp:** So, again, is this, maybe this is obvious to you.

**Rachel Rapp:** So, this is, again, this is a deck that we use for standards.

**Rachel Rapp:** So you might already know just sort of some logos to associate with each of these modalities that we focus on.

**Rachel Rapp:** I can skip over this.

**Rachel Rapp:** don't know if this is helpful for you, but, you know, like, for LLMs.

**Rachel Rapp:** Is this helpful?

**Erik O'Brien:** I'm sorry.

**Rachel Rapp:** Yeah, yeah, it is.

**Rachel Rapp:** Great.

**Rachel Rapp:** Okay, great.

**Rachel Rapp:** So, yeah, this is, you we've got the meta.

**Rachel Rapp:** They have the LLAMA models, the whales for DeepSeq.

**Rachel Rapp:** This other one is Quen.

**Rachel Rapp:** These are all really popular LLMs that we see people use.

**Rachel Rapp:** These are also model APIs that we have.

**Rachel Rapp:** Well, not LLAMA anymore.

**Rachel Rapp:** We're actually deprecating that one.

**Rachel Rapp:** But, you know, model APIs we have had.

**Rachel Rapp:** For transcription, have OpenAI actually has a great transcription model called Whisper.

**Rachel Rapp:** That's the one that we optimize, that we use in our transcription product.

**Rachel Rapp:** And Mistral as well, image generation.

**Rachel Rapp:** This is not, oh, yeah, so Flux, they do have an open source one.

**Rachel Rapp:** We do offer it.

**Rachel Rapp:** But they also have some closed source one, Stability.

**Rachel Rapp:** So those are sort of the big names there.

**Rachel Rapp:** And the image generation space is actually, we need to update this because Quen came out with a great image generation model as well.

**Marylise:** We should update LLMs too because we have GPT-OSS now.

**Rachel Rapp:** Yeah, true.

**Rachel Rapp:** Yeah, we got to update this.

**Rachel Rapp:** Text-to-speech, we have Canopy and Cam AI, Canopy is closed source, Canopy is open, Canopy is that upside-down triangle.

**Rachel Rapp:** Embeddings are a really big one.

**Rachel Rapp:** I think embeddings don't get a lot of hype, but they are actually used a ton.

**Rachel Rapp:** So Quen embedding, they have like an 8B model, so 8 billion parameters.

**Rachel Rapp:** a really popular one.

**Rachel Rapp:** And then there's other, I think, Gemma from Google.

**Rachel Rapp:** We don't have the logo here, but that's another really popular one.

**Rachel Rapp:** And then these are two sort of smaller labs, Mixed Bread, based in Germany.

**Rachel Rapp:** And then the Beijing Academy of Artificial Intelligence also has multiple models that are very beloved.

**Rachel Rapp:** And then, of course, Compound AI Systems, we have our own SDK, a Python SDK for this called Base in Chains that we talked a little bit about this before.

**Rachel Rapp:** And this just lets you sort of link all of these models together as chainlets that call each other directly and scale independently and are just really, really fast.

**Erik O'Brien:** How do you guys choose which ones you pick for?

**Erik O'Brien:** Each category, is it purely performance-related?

**Rachel Rapp:** There's actually not that many.

**Rachel Rapp:** Sorry, I hope I'm understanding your question right, I, you know, Marylise, correct me if I'm wrong, but there's not that many open-source models that are actually at the bar, the quality bar, that people are using them in production.

**Rachel Rapp:** So we actually do use pretty much all of the models that people would use, right?

**Rachel Rapp:** So there might be, like, you know, six to ten LLMs that people are really using in production.

**Rachel Rapp:** And that's, like, a manageable number, right?

**Rachel Rapp:** Like, that's something that you can actually put in a library or offer for people to use.

**Rachel Rapp:** So we don't really, you know, we choose based on quality, but I think sort of the big players all have very similar models because they all meet this quality bar.

**Rachel Rapp:** As, like, for a transcription, for instance, Whisper, there's another one, VoxTroll.

**Rachel Rapp:** And those are, like, as far as I know, those are, like, the only two.

**Rachel Rapp:** I could be forgetting maybe, like, one other one.

**Rachel Rapp:** But if so, it's like one of their ones, like two or three open source transcription models.

**Rachel Rapp:** Also, you can also call them ASR for automatic speech recognition.

**Rachel Rapp:** It's the same thing or like not exactly the same thing, but, you know, they both typically are used in service of transcription.

**Rachel Rapp:** Yeah, so it's like a very small set, right?

**Rachel Rapp:** It's just a set of three.

**Rachel Rapp:** So it's relatively easy to talk about once you break them into these different categories of the actual modality.

**Rachel Rapp:** Again, image generation, these are like the big two, big two players, except that Quinn now also has one.

**Rachel Rapp:** So then you have like three, you know, three model providers.

**Erik O'Brien:** I think the biggest set is going to be guess that's open source is the key there.

**Erik O'Brien:** They have to be open source to be used on the platform, or is it that's just the one that you guys pull in availability?

**Erik O'Brien:** And then if a customer wants something that's closed source, you guys can also facilitate that.

**Rachel Rapp:** Exactly.

**Rachel Rapp:** So we can do anything open source, fine-tuned, or custom.

**Rachel Rapp:** That being said, of course, if a new model comes out that is open source, that's something we can support out of the box.

**Rachel Rapp:** Our engineers can optimize it right away.

**Rachel Rapp:** We don't offer closed source models from like...

**Rachel Rapp:** Any of the big source closed source providers, you know, ChatGPT is closed source, Anthropic is closed source, you know, Claude, like, we don't offer any of those.

**Rachel Rapp:** Where we come in when it comes to closed source is, like, say that you're a company that has their own custom LLM.

**Rachel Rapp:** Like, you have an LLM that's been trained on your own custom financial data, and you want to run that LLM somewhere and serve it to your customers, then we can do that for you, right?

**Rachel Rapp:** We're totally agnostic to the model type.

**Rachel Rapp:** Like, you can absolutely run a custom model on Base10, but that's when we come in on the custom side.

**Rachel Rapp:** It's not that we're offering those custom models to people.

**Rachel Rapp:** We're, like, powering companies' custom models so they can offer it to people.

**Rachel Rapp:** Gotcha.

**Rachel Rapp:** Yeah, but typically, you know, our bread and butter is going to be – I don't want to say it because really our bread and butter is all of the above, but the open source models, we can, you know, let's say an amazing new open source model drops, like the next DeepSeq v4, and it's incredible.

**Rachel Rapp:** Well, our engineers can just swarm, and they can jump on that.

**Rachel Rapp:** They can, you know, put that on our platform.

**Rachel Rapp:** They can make it super fast, and they can just, you know, really –

**Rachel Rapp:** Dig in and optimize that, and then say to the world, we have the fastest, best DeepSeq V4, and you can just take it and use it in your product.

**Rachel Rapp:** So that's where the open source comes in and why we have such a relationship to open source, because just by being open source, our engineers can make, you know, they can optimize it and get their hands on it right away and then go make it available to other people.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** Thanks for clarifying.

**Rachel Rapp:** And then a couple sort of keywords that you can look for, some use cases that a lot of these get applied for, everything from like search, search is going to be really big on the embedding side, also on the LLM side, agents, of course, compound AI using different models, you can think of voice agents, you can think of any type of agent, code generation, like Marylise said, it's something that we've seen a lot of, we have multiple code gen customers, but I think only one case study right now, which is that Zed Industries one, AI phone calling, so bland AI, we have a case study, study on our customers page, chat bots with LLMs, anything with foundation models, so foundation models in this case is going to be also typically

**Rachel Rapp:** What we were just talking about with that closed source, so like people who have their own in-house model that they've trained and they want to serve to people, we do that for Writer, we do that for Cam AI, we do that for a few different companies.

**Rachel Rapp:** Document processing, recommender systems, scribes, we do a ton of different scribes in the transcription side, translation, audio generation, voice synthesis.

**Rachel Rapp:** All of these are different use cases that we serve and that we serve actively, that we have customers that are doing and that these models let people do.

**Marylise:** Yeah, and I would say from a content perspective, as you're building a content plan, I think this is where we would want to go deeper and talk about all these use cases and have content related to that with the performance and reliability in mind.

**Rachel Rapp:** Yeah, so here focusing on one use case that we do really well is voice.ai.

**Rachel Rapp:** one one really do do so that

**Rachel Rapp:** So we have this case study on our website.

**Rachel Rapp:** You can go look there for a little bit more specific wording for specific stats.

**Rachel Rapp:** But here at a high level, we use a dedicated deployment to serve Bland AI as voice agents.

**Rachel Rapp:** I'm sorry, I'm thinking.

**Rachel Rapp:** I know this really well, but we've had to rethink what we talk about here.

**Marylise:** So I'm like censoring.

**Marylise:** Yeah, but I think it's fine.

**Marylise:** But we can talk about the sensitivity.

**Marylise:** Like something happened with Bland where we were kind of like doing this really cool content about how do you build voice agents with, you know, open source and stuff.

**Marylise:** And they felt kind of like that was competing with what they do.

**Marylise:** So we try to not say we do voice AI, but we do text to speech and, you know, be a little more on the kind of use cases rather than just the general category too.

**Rachel Rapp:** Yeah, yeah.

**Rachel Rapp:** Sorry.

**Rachel Rapp:** I was like, I'm going to, yeah.

**Marylise:** Yeah.

**Marylise:** So be careful.

**Marylise:** Don't tell you like content team to write a voice AI thing because we're probably going to.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I'm working with Deepgram as well.

**Rachel Rapp:** So we'll save.

**Rachel Rapp:** So here at Open Evidence, they do medical search, question answering, become a really big, big player.

**Rachel Rapp:** They think it's like 40% of doctors in the United States use Open Evidence.

**Rachel Rapp:** They work with a doctor in every state and zip code.

**Rachel Rapp:** They help doctors filter through sort of the massive amounts of medical literature now that are coming to light every day.

**Rachel Rapp:** And with really high quality, fact-based, fast question answering for doctors at the point of care.

**Rachel Rapp:** So they do, we serve them on Undedicated.

**Rachel Rapp:** They have their own custom model that we serve for them.

**Rachel Rapp:** So in this case, you could, you know, sort of call it closed source, but it's, I don't know, closed source to me is always more like open and anthropic.

**Rachel Rapp:** It is really like custom, their own in-house model.

**Rachel Rapp:** And they serve that, you know, that high scale for, you know, different times of the day and all of that, that they control with our dedicated product.

**Rachel Rapp:** They also do model training and, um, I guess model APIs, Marlies, I don't know what the model APIs are.

**Marylise:** I think it's.

**Rachel Rapp:** Thanks to them on Moodle APIs the other day, yeah.

**Marylise:** Oh, think we were playing with it.

**Rachel Rapp:** Yeah, they do training.

**Rachel Rapp:** Oh, nice.

**Rachel Rapp:** So they're like a full stack BaseTen user.

**Rachel Rapp:** as modeling experimentation and then core product is going to be dedicated.

**Rachel Rapp:** Cool.

**Rachel Rapp:** And then some of the reasons that they chose us was really just the FTE partnership.

**Rachel Rapp:** Our FTEs have been super hands-on, helping them optimize their workloads.

**Rachel Rapp:** Really incredible performance metrics on our customers page.

**Rachel Rapp:** I just love all of these.

**Rachel Rapp:** 78% lower latency is pretty incredible from the performance side.

**Rachel Rapp:** 6x faster deployment processes.

**Rachel Rapp:** This is also leading into our DevEx.

**Rachel Rapp:** Just the fact that like their engineer there is a power user.

**Rachel Rapp:** You know, he comes to us when he wants support or he wants extra hands or he wants, you know, like a new latest and greatest technique.

**Rachel Rapp:** But at the end of the day, he can really do things himself because our DevEx is just that friendly.

**Rachel Rapp:** And because, you know, now they got rid of all of these manual processes that just speed up the actual deployments, like 8x less time spent on maintenance.

**Rachel Rapp:** And then an estimated 2 million saved.

**Rachel Rapp:** And

**Erik O'Brien:** Yeah, super powerful.

**Rachel Rapp:** Yeah, I love that.

**Rachel Rapp:** Those are some good numbers.

**Rachel Rapp:** And then reliability.

**Rachel Rapp:** So again, they're serving doctors all over.

**Rachel Rapp:** Doctors rely on them at the point of care.

**Rachel Rapp:** They rely on them to be available.

**Rachel Rapp:** They rely on them to be fast.

**Rachel Rapp:** And how do they do that?

**Rachel Rapp:** using this multi-cloud capacity management system that we talked about, which actually lets you sort of treat all of these nine different clouds as one universal cloud.

**Rachel Rapp:** So if, you know, you know, God forbid, I know.

**Rachel Rapp:** So don't lean into this as well, because GCP is a partner.

**Rachel Rapp:** But just to give you a concrete example, everybody knows that GCP went down, they were down for about a day.

**Rachel Rapp:** And then these big players like Spotify was down, you know, a lot of different products were down because they were running on GCP.

**Rachel Rapp:** When that happened, we just automatically scaled up people's workloads into different clouds, like anybody running on Base 10 cloud who was running on GCP.

**Rachel Rapp:** But before our engineers could get in the war room, like they had already been scaled over into different clouds.

**Rachel Rapp:** They had like, like, we're on the scale, if there was any downtime, it was like minutes, if anything, compared to our competitors.

**Rachel Rapp:** The others, was like ours.

**Rachel Rapp:** And that's what we also use here for open evidence.

**Rachel Rapp:** use MCM, MCM for short, to power that reliability that they need.

**Rachel Rapp:** Clay.

**Rachel Rapp:** Actually, I've never talked about Clay before.

**Marylise:** I guess, Kenzie, you made this slide.

**Marylise:** I don't know.

**Marylise:** I guess we do embedding.

**Marylise:** I don't know either.

**Rachel Rapp:** Okay, I'm just going to read you the slide then.

**Rachel Rapp:** We do embeddings.

**Rachel Rapp:** They use dedicated.

**Rachel Rapp:** They got 70% cost savings, really fast latency, very high uptime.

**Rachel Rapp:** Yeah.

**Rachel Rapp:** I mean, yeah, I can read the slide, but you know, you can, you got it.

**Rachel Rapp:** And you're probably sensing some themes, right?

**Rachel Rapp:** This is always leaning into those three pillars of like, very, very fast.

**Rachel Rapp:** So very low latency, very high throughput, very high uptime, four nines at a minimum in our messaging that we use as four nines uptime, powered by MCM, and then the cost efficiency as well that goes in hand in hand with the performance.

**Rachel Rapp:** Okay.

**Rachel Rapp:** Thank

**Rachel Rapp:** Captions.

**Rachel Rapp:** Again, this is a Kenzie slide.

**Rachel Rapp:** This is new.

**Rachel Rapp:** So, yeah, this is the same themes.

**Marylise:** Okay.

**Marylise:** think one thing I want to say about caption, and I don't know if there is in the deck, the last slide that is hidden, is it?

**Marylise:** So, basically, when caption came online, you could see all of a sudden our system, no, that's not it.

**Marylise:** Yeah, it's like, you know, you can look at graphs of our systems and the consumption of our resources, and when caption came online, it just was super bursty.

**Marylise:** There's a high peak, and you can see us, like, totally taking it and then coming down very smoothly.

**Marylise:** So, just to talk about, like, the flexibility and how we can just handle peak loads very easily, and we just saw that so big when caption came on.

**Rachel Rapp:** It was beautiful.

**Rachel Rapp:** Oh, yeah.

**Rachel Rapp:** I think that's true.

**Rachel Rapp:** I think that's, yeah, it reminded me that I think our PM actually said that without MCM, they would not have been able to serve the scale on their launch day.

**Rachel Rapp:** Like, they went so viral.

**Rachel Rapp:** viral.

**Rachel Rapp:** That they scaled like insanely.

**Rachel Rapp:** And we were able to handle that with MCM seamlessly because we have basically infinite capacity because we can just tap into all of those different clouds.

**Rachel Rapp:** You know, worst case scenario, even if we would put you in a region that's not the closest to your users, that's still such an advantage compared to just not being able to meet that demand and then being offline for those people, right?

**Rachel Rapp:** So even if you're sacrificing a teeny bit of latency, what you're getting for that is you have basically limitless scale.

**Marylise:** Yeah.

**Marylise:** And I think they actually had an update release or something a couple of weeks ago and same thing happened.

**Marylise:** All of a sudden it just burst up and we dealt with it very well.

**Marylise:** Yeah.

**Marylise:** We just never know when our customers are doing that.

**Marylise:** Our system is just able to adapt to it.

**Rachel Rapp:** Cool.

**Rachel Rapp:** So now a little bit more into the inference stack.

**Rachel Rapp:** This is everything that we couple into our inference optimized infrastructure, so reliability and our model runtime, so performance.

**Rachel Rapp:** And here you see those two layers.

**Rachel Rapp:** So at the top, we have the inference runtime.

**Rachel Rapp:** It leans on a bunch of different model performance optimizations, some of them including, you know, the specific modalities, specific runtime, so like a runtime for embeddings, a runtime for transcription, all of the different custom kernels that we use, kernel fusion, like really at the lowest level that our engineers are writing, speculation engines of different types of like speculative decoding or spec tag.

**Rachel Rapp:** We also have our own type of lookahead decoding called BaseTen lookahead.

**Rachel Rapp:** And this is also really useful for the cogeneration use cases.

**Rachel Rapp:** So there's a ton of different like anything that is sort of leading, bleeding edge performance research.

**Rachel Rapp:** Our engineers bring that into production, they battle hard in it.

**Rachel Rapp:** They actually like we work very closely with the NVIDIA team, we actually, you know, we'll take their newest tooling, battle hard in it for production, and then ship patches back to NVIDIA that they will integrate into their open source repository.

**Rachel Rapp:** And get hub.

**Rachel Rapp:** So you actually like we're even shipping improvements to NVIDIA and you're getting sort of like the

**Rachel Rapp:** The sneak peek or like the earliest, latest gen with us.

**Rachel Rapp:** And then, you know, a month later, it'll become open source on NVIDIA's repo.

**Rachel Rapp:** And again, this is all, this is taken from the guide on our site.

**Rachel Rapp:** It's super meaty.

**Rachel Rapp:** It's very long, but it is a nice resource if you want to ever like look up a specific term that you see us use here.

**Rachel Rapp:** Like custom kernels is a quick, is a little section with two paragraphs and you can read a little bit more there.

**Rachel Rapp:** So all of that inference runtime stuff that sits on top of the inference optimized infrastructure.

**Rachel Rapp:** So this is going to be everything with the hardware, with the routing, the networking.

**Rachel Rapp:** So like, you know, like the load balancing, the cold starts, the active, active reliability, the independent component auto scaling.

**Rachel Rapp:** So like the actual scaling up and down and going from zero to one and one to a hundred and a hundred to a thousand.

**Rachel Rapp:** The routing could be like geo aware.

**Rachel Rapp:** So for instance, if you have customers in Italy, well, you might want to serve them in Frankfurt or in Ireland, as opposed to, you know, the U S West coast, because that's going to have more latency.

**Rachel Rapp:** So that was sort of network.

**Rachel Rapp:** Working decisions are going to be coupled in there as well.

**Rachel Rapp:** The actual auto-scaling settings that can be SLA aware, meaning like let's say you have a particular latency that you want to meet or that you have to meet.

**Rachel Rapp:** Our FDEs will work with you to actually tune those auto-scaling settings for your workload to make sure that you're hitting that.

**Rachel Rapp:** And the multi-cloud management or multi-cloud capacity management, that's that MCM that lets you, again, just scale agnostically across any cloud.

**Rachel Rapp:** And all of that sits on top of all of our different cloud providers that we call BaseTenCloud.

**Rachel Rapp:** We call it BaseTenCloud.

**Rachel Rapp:** I probably should have said earlier, I just want to emphasize that we don't actually own hardware.

**Rachel Rapp:** Like it's very cloud partnership based.

**Rachel Rapp:** It's not like, you we're sending you to a data center somewhere that we purchase or something like that.

**Rachel Rapp:** We don't buy the compute.

**Rachel Rapp:** We just have these partnerships with so many different clouds that unlocks like limitless capacity even to the latest and greatest GPUs like B200s.

**Rachel Rapp:** Cool.

**Rachel Rapp:** And now I'm going to dive in a little bit to some of these features that we talked about that are really modality specific.

**Rachel Rapp:** So BaseTen Embedding's inference, this is that.

**Rachel Rapp:** Our old branding, so you can tell this is a little bit old.

**Rachel Rapp:** But again, so there's also, we have newer metrics as well.

**Rachel Rapp:** You can see on B200s, these were run on, I think, H200s or H100s, which is a little bit, also powerful GPUs, but not the newest.

**Rachel Rapp:** So why it's great, 2x higher throughput than all of the other open source tools out there that are really popular.

**Rachel Rapp:** think like TEI from Hugging Face is a really popular one.

**Rachel Rapp:** You've got Olama that a lot of people are using, Infinity.

**Rachel Rapp:** What's that one?

**Rachel Rapp:** And VLLM, we also like smoke VLLM in every use case ever, but that's another story.

**Rachel Rapp:** So yeah, we're looking at 2x higher throughput, 10% lower latency, and also smallest memory footprint.

**Rachel Rapp:** So why am I mentioning this?

**Rachel Rapp:** Well, I think you can always sort of game the metrics.

**Rachel Rapp:** Like we have competitors that game the metrics, and how do they game the metrics?

**Rachel Rapp:** By just throwing more B200s at it, right?

**Rachel Rapp:** And then conveniently not mentioning the cost, right?

**Rachel Rapp:** So you can just use double the GPUs and be like, oh, we're so much faster, but they won't be like telling you, yeah, you're paying for twice as many GPUs.

**Rachel Rapp:** Great.

**Rachel Rapp:** So we have actually these tools that are not just more performant, but they're all.

**Rachel Rapp:** So much more efficient.

**Rachel Rapp:** So we have by far the lowest memory footprint here, which means not only are you getting faster performance, but it's going to be at a lower, so a higher cost efficiency, so lower overall cost for that hardware.

**Rachel Rapp:** And yeah, just way more efficient overall.

**Rachel Rapp:** And what is it used for?

**Rachel Rapp:** embeddings are used typically for things like search.

**Rachel Rapp:** They can be used for recommender systems.

**Rachel Rapp:** They're frequently used in these compound AI use cases where, you know, you have an agent or something that's going to be doing embeddings for a search query and then maybe using a tool to get some information.

**Rachel Rapp:** And return it to the user.

**Rachel Rapp:** And then, course, you know, RAG is a classic one.

**Erik O'Brien:** And if you look up...

**Erik O'Brien:** Is compound AI something you guys termed internally or is that something that's used across the industry?

**Rachel Rapp:** So both.

**Rachel Rapp:** And if you find a better way or like a more popular way of calling it, then please let us know and lean into that from like the SEO side.

**Rachel Rapp:** Compound AI systems was a really popular keyword about a year ago.

**Rachel Rapp:** And it was something we saw competitors leaning into.

**Rachel Rapp:** It's...

**Rachel Rapp:** It's...

**Rachel Rapp:** Something that there's like, I think it was, I don't know if it was UC Berkeley, but some university coined the term and it was getting a lot of momentum.

**Rachel Rapp:** Since then, I personally don't have the feeling like it's taken off.

**Rachel Rapp:** Like, it's not like a coined thing that everybody is saying compound AI.

**Rachel Rapp:** You could also interchange it with agents in a lot of these cases because agents are compound AI.

**Rachel Rapp:** Also, people are leaning into agents.

**Rachel Rapp:** call things that are compound AI agents, even if they're not really agents.

**Rachel Rapp:** There's also like compound workflows, compound pipelines, multi-model, whatever.

**Rachel Rapp:** So, again, I think you can default to compound AI systems.

**Rachel Rapp:** I'm sure there's traction there, but I think it could be worth doing the homework and being like, what is the highest search volume or what's the best keyword there?

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yeah.

**Rachel Rapp:** And I think also because we do have competitors that are also leaning into that keyword and we want to rank for it against them, it's also a good one to make sure that we're hitting at least for that reason.

**Erik O'Brien:** Gotcha.

**Rachel Rapp:** So, to transcription, we've also done a lot.

**Rachel Rapp:** More here recently around diarization, which is related.

**Rachel Rapp:** So we have the fastest, most accurate, most cost-efficient whisper transcription whispers, an open-source model by OpenAI that lets you do transcription.

**Rachel Rapp:** So 1,000x real-time factors, so super, super fast, the lowest word error rate, so very high accuracy, and just the best performance overall.

**Rachel Rapp:** So here we have a lot of companies that have like scribes, medical scribes, veterinary scribes, or like compound AI.

**Rachel Rapp:** You know, you might think of an agent use case where you're speaking to the agent, and first it's going to transcribe that audio into text, and then it's going to use that text and hand it to an LLM, and the LLM is going to do search, and then it's going to come back to you with an answer, right?

**Rachel Rapp:** So those compound workflows are also very commonly used in conjunction with transcription.

**Rachel Rapp:** Another popular one is this diarization, again, which is like speaker identification, so it might be like maybe you have, I don't know if you've heard of Granola, but, you know, these note-taking apps where you have five different people.

**Rachel Rapp:** Yeah, same, same.

**Rachel Rapp:** So you have like five people using it, right, and it's going to, you know, I think Granola doesn't do diarization, but similar idea of like, let's say,

**Rachel Rapp:** Wanted to tell you who was saying what, or like Gong, right?

**Rachel Rapp:** Gong, where you have the calls recorded and it sort of shows you who's speaking that speaker matching as well.

**Rachel Rapp:** And then again, Company Eye, we have this product called BaseTenChains.

**Rachel Rapp:** We also have a product page there on our website with more information if you want to find that.

**Rachel Rapp:** It should be under the products tab.

**Rachel Rapp:** So the thing here is that, like the great thing here is really just it lets you chain models together and while also keeping them very modular.

**Rachel Rapp:** So you can chain these different models together as individual, we call them chainlets.

**Rachel Rapp:** A chainlet is one model or processing step.

**Rachel Rapp:** It's run on its own independent hardware.

**Rachel Rapp:** It scales independently.

**Rachel Rapp:** So let's say you have something that's like very CPU bound.

**Rachel Rapp:** You can deploy that on a CPU rather than having that block a very expensive, you know, by comparison, expensive GPU in the meantime.

**Rachel Rapp:** So you can separate those different parts of the workload, really put them on the hardware that's best suited for them, scale them as they need to be scaled, and then, you know, link them all together so that they're calling each other directly.

**Rachel Rapp:** So you don't have.

**Rachel Rapp:** That network overhead of like actually sending data in and out of the cloud, right?

**Rachel Rapp:** They're actually just remote services that are calling each other directly.

**Rachel Rapp:** And again, these are going to be for these use cases like, you know, AI phone calling or like any of those agent use cases or rags.

**Rachel Rapp:** literally anything that uses multiple models.

**Rachel Rapp:** So one case study, again, on our site is going to be that latent case study.

**Rachel Rapp:** They do pharmaceutical search and they do chains or they use chains to actually process.

**Rachel Rapp:** They make patient data searchable very quickly.

**Rachel Rapp:** So what does a patient look like in terms of pharmaceutical search?

**Rachel Rapp:** Well, you've got all of these different documents.

**Rachel Rapp:** You've got doctor's notes.

**Rachel Rapp:** You've got pictures of like prescriptions and all of that.

**Rachel Rapp:** And they want to make all of those different types of documents, both structured and unstructured data, searchable very, very quickly.

**Rachel Rapp:** So they use what's called optical character recognition or OCR to process those documents visually.

**Rachel Rapp:** That can be done on a CPU.

**Rachel Rapp:** It's fine.

**Rachel Rapp:** It's pretty performant on a CPU.

**Rachel Rapp:** It's also much cheaper to run it on a CPU.

**Rachel Rapp:** You can scale that massively on a CPU.

**Rachel Rapp:** They run that part of the workload on this.

**Rachel Rapp:** CPU, then we can hand that off to their embeddings that actually embed that data, and then you can do search on that as well.

**Rachel Rapp:** So they're power users of chains.

**Rachel Rapp:** And then our deployment options, I'm not sure how much you guys are going to, again, we have to update this right now, so I'm not sure how much you guys will interface with this, but at sort of a high level, we have these two buckets.

**Rachel Rapp:** The one is BaseTen Cloud, and the other one is self-hosted.

**Rachel Rapp:** Under BaseTen Cloud, have, you know, like sort of default, and then you also have single tenant, which means that you have those clusters that are just running for you.

**Rachel Rapp:** And underneath the umbrella, Is it cutting for you, too?

**Erik O'Brien:** Yes, I didn't know that was just me.

**Marylise:** Yeah, you've been cutting, Rachel?

**Marylise:** Yep.

**Marylise:** Thank Thank Thank Thank Thank you.

**Marylise:** Thank Thank You

**Marylise:** Yeah, can take one here.

**Marylise:** So she talked about BaseTen Cloud and single tenant being like part of it.

**Rachel Rapp:** Hybrid, which means that you're running self-hosted.

**Marylise:** She's gone again.

**Marylise:** Yeah, and I wanted to say self-hosted is, hybrid is going to be a sub-offering of self-hosted.

**Marylise:** It's basically like you self-host in your own VPC, but if something goes down, you can spill over to BaseTen Cloud, which is basically the hybrid option.

**Marylise:** So we are about to update the website to remove hybrid as its own thing, and then we'll roll it under self-hosted, and then we're going to add content around single tenant in BaseTen Cloud.

**Marylise:** That's coming in a couple of weeks, yeah.

**Marylise:** Rachel, yeah, you were cutting, so I covered the changes we're making.

**Rachel Rapp:** Perfect, sorry, Skip, I switched time.

**Rachel Rapp:** I think we were kind of, yeah, that was it.

**Rachel Rapp:** We only have trivia for the sales team.

**Marylise:** Yeah, sorry, Erik, unless you want to do trivia, think we're good.

**Marylise:** Yeah, we can quiz you now, though.

**Erik O'Brien:** I don't know if I would pass that.

**Erik O'Brien:** I caught quite a bit of it, but I don't know about if I could pass any trivia questions.

**Erik O'Brien:** I guess one question I had that is just more general, so nothing specific about the content, but when we're kind of educating the market and kind of top of funnel stuff, do you guys have a preference on, is it like you want to sound like a teacher or more of a peer or more of a performance lab?

**Erik O'Brien:** Any kind of thoughts on that top of funnel content?

**Marylise:** I don't think we want to be a teacher.

**Marylise:** think we want to be, we just, I think teacher.

**Marylise:** It feels a little like, you know, we are kind of, we have a voice that is like, kind of like the one I think teacher, I feel like someone who is serious and stuff.

**Marylise:** Like, so we have this kind of like fun, you know, I think the brand, want to be very knowledgeable with melody.

**Marylise:** And so what we want to show is this really like very strong technical argument, but while staying very humble.

**Marylise:** And so being very relatable from a developer perspective with melody.

**Marylise:** Does that answer your question?

**Marylise:** Yeah, so I feel like teacher is too much of like, I want to tell you all this.

**Marylise:** No, we actually want to show, not tell in a way.

**Marylise:** So that's why we lean so much on the customer example.

**Marylise:** And I think I saw that in your write-up, you know, like I think in the way you were talking about the voice and how we actually using like relieved example is really the way we want to do it.

**Erik O'Brien:** Okay, wonderful.

**Erik O'Brien:** I do.

**Erik O'Brien:** Need to jump to my next call, but a few different things, I think more for Marylise, but any other feedback on the artifacts or content strategy would be great to get in this week.

**Erik O'Brien:** And then just another touch on those Google Analytics and Search Console access.

**Marylise:** I can't give that to you.

**Marylise:** I'll talk to Mike.

**Marylise:** Unless you have access to Google Search and stuff to add users, Rachel?

**Marylise:** Are you an admin?

**Rachel Rapp:** I don't know.

**Rachel Rapp:** I would ask Mike or Andre.

**Marylise:** Yeah, okay.

**Marylise:** Yeah.

**Marylise:** Okay.

**Marylise:** I'll ask Mike.

**Marylise:** And then the additional content, I can nudge the team to see if they want to review, you know, search on pages.

**Marylise:** I am done on my end.

**Marylise:** But yeah, it will be great to have another set of ideas on them.

**Erik O'Brien:** So.

**Erik O'Brien:** Yeah.

**Marylise:** Wonderful.

**Marylise:** Are you in the channel with Cosex, Rachel?

**Marylise:** Yeah, if you want to look, put the links.

**Marylise:** If you have time, I would love to get your thoughts too.

**Rachel Rapp:** Yeah, for sure.

**Rachel Rapp:** Sorry, I wanted to give you a demo, but then I had to talk too much.

**Erik O'Brien:** But anyway.

**Erik O'Brien:** If you guys have questions, let me know.

**Marylise:** Yeah, we can do a demo another time if you need.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Well, this was very helpful, very informative.

**Erik O'Brien:** But, yeah, we'll keep you posted if we need more.

**Erik O'Brien:** Great.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Thanks, Steve.

**Erik O'Brien:** Bye.
