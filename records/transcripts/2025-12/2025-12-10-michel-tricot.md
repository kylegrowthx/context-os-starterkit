# Michel Tricot

<metadata>
date: 2025-12-10
time: 18:46 UTC
duration: 44 minutes
organizer: erik@growthx.ai
participants: Michel Tricot, Erik O'Brien, Dignory Carmona, Kushal Chatterjee
speaker_note: "6 - Grand Canyon" device name matched to Michel Tricot through transcript context (Airbyte team introducing platform features, primary speaker explaining agentic data architecture)
fathom_recording_id: 107804672
fathom_url: https://fathom.video/calls/500945006
share_url: https://fathom.video/share/KxtkuDWnMDcsFqP_yrNqL4m2GZzTT_2t
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

To map Airbyte's agentic data platform and its value for AI engineers.

---

## Context

Michel Tricot is the founder/product lead at Airbyte, the open-source data integration platform. GrowthX is exploring Airbyte's new agentic data platform—a strategic product for AI agents that need autonomous access to internal company data. This call was a deep-dive intro to understand how Airbyte is positioning itself in the emerging agentic AI market, specifically around data infrastructure for autonomous agents rather than just API integration (like Merge). Erik O'Brien (GrowthX CEO/marketing lead) wanted to map the product, understand its near-term roadmap, and identify content angles for GrowthX's AEO/AI focus.

---

## Relevance

**To GrowthX Content Strategy & AEO:**
- Airbyte's agentic data platform is a new market narrative (autonomous discovery vs. manual agent prompting) that aligns with GrowthX's AI infrastructure focus
- The Entity Cache concept (cross-silo discovery) vs. Merge's direct-fetch-only model is a compelling differentiator story for B2B SaaS audiences
- Content opportunity: "Why autonomous agents need discovery, not just integration" — educational positioning

**To CheckThat (AI visibility):**
- Airbyte is building an AI-native data layer; understanding their ontology vision and Entity Cache indexing strategy could inform CheckThat's research into how AI systems consume/prioritize data

**To GrowthX Business Development:**
- Airbyte's February 2026 private beta launch (Entity Cache + cloud product) signals momentum; expansion opportunity for case studies or thought leadership content
- Kushal Chatterjee (Airbyte team member on call) — potential future contact for ongoing updates or collaborative content

---

## Overview

- Airbyte’s platform enables autonomous agents by automating the `Discover → Fetch → Act` data loop, replacing manual data pipeline builds and maintenance.
- The platform uses two connector types: `Replication Connectors` build a cross-silo `Entity Cache` for discovery, while `Direct Connectors` provide real-time data access and writes.
- The `Entity Cache` is the platform's core differentiator, enabling agents to autonomously discover data across systems (e.g., finding "Invesco" in Zendesk, Jira, and Salesforce). Competitors like Merge offer only direct fetch.
- `Direct Connectors` are the source of truth; the `Entity Cache` provides a stale data fallback, ensuring agents can operate even if a source API is down.

---

## Key Topics

### The Agentic Data Loop

  - Airbyte's platform automates the `Discover → Fetch → Act` loop, the core process for agents to access and use internal company data.
  - **Discover:** Find relevant data across all connected systems.
  - **Fetch:** Retrieve the most up-to-date, permissioned data from the source.
  - **Act:** Perform actions like updating records or triggering workflows.

### Platform Components & Workflow

  - **Entity Cache (Discovery Layer):**
      - Built by `Replication Connectors` mirroring data from all sources (e.g., Zendesk, Salesforce).
      - Enables agents to autonomously discover data across silos without needing specific IDs.
      - Example: An agent can find all data related to "Invesco" across all systems, not just a pre-defined Zendesk ticket ID.
  - **Direct Connectors (Fetch & Act Layer):**
      - Embeddable tools for agents to perform real-time `Read` and `Write` operations.
      - `Read` access is available now; `Write` functionality is planned for January.
      - Serve as the source of truth; if a source API is down, the agent can fall back to the `Entity Cache` for stale data.
  - **Auth Module:**
      - Enforces fine-grained, user-level data access policies.
      - Example: A payroll agent can only see compensation data for its user's team.

### Competitive Advantage

  - **Problem:** Building agents without Airbyte requires massive, ongoing effort for:
      - Connector development and maintenance (API changes, rate limits).
      - Auth and permission management.
      - Data replication and indexing for discovery.
  - **Solution:** Airbyte provides a single API key that handles all data infrastructure, freeing teams to focus on agent logic.
  - **Differentiator:** The `Entity Cache` enables true agent autonomy. Competitors like Merge offer only direct fetch, requiring agents to be manually prompted with specific IDs.

### Future Vision

  - **Ontology:** The `Entity Cache` is the first step toward a full ontology, which will provide a unified, cross-system definition of core business entities like "Customer."
  - **Deployment:**
      - `Direct Connectors` are available now for rapid agent prototyping.
      - The full cloud product with the `Entity Cache` will enter private beta in February.

---

## Action Items

**Kushal Chatterjee (Airbyte)**
- Share Airbyte's internal agentic data platform document with Erik O'Brien via Slack

**Erik O'Brien (GrowthX)**
- Review the shared document and follow up with questions via Slack or directly with Kushal

---

## Transcript
**Michel Tricot:** Eric, I cannot, you're muted.

**Michel Tricot:** Wow, you have two note takers.

**Erik O'Brien:** Yeah, I think Dig has a couple that she's testing out, so it was just me hanging out with the note takers for a bit there.

**Michel Tricot:** Feels like a crowd.

**Michel Tricot:** Yeah, I like the Fathom notes actually, so I might try using that one too.

**Erik O'Brien:** Yeah, Fathom has been the one that most of us use.

**Erik O'Brien:** Fireflies, some people are testing, and then Reve AI is a new one I haven't seen before.

**Erik O'Brien:** They're a client, but I haven't seen anybody using it.

**Erik O'Brien:** All right, well, let's jump into it.

**Erik O'Brien:** So, yeah, today we're really trying to just kind of get a map of the platform, kind of where it sits today, what are we looking at near-term, and kind of what the longer-term vision is, so kind of with a really focus on, like, what does this really unlock for AI engineers building agents?

**Erik O'Brien:** So, if there's anything you have to show, I think that would be super helpful for visuals.

**Erik O'Brien:** Otherwise, I've got some questions we can just run through.

**Michel Tricot:** Yeah, let me share something, actually.

**Michel Tricot:** So, this is a very high-level view of what Airbuy does with the agency data platform, which is, on one end, you have agents that need to execute.

**Michel Tricot:** Okay.

**Michel Tricot:** And to get to and finalize a specific task, to get access to this task, and to solve them, they need to have access to external context, and that context can be stored in the database, this context can be stored in any kind of SaaS application that you might have, and the way the loop for an agent to actually perform that task is always the same thing.

**Michel Tricot:** is, one, you need to discover what is available to you, and you can see, you can make a parallel with CloudCode, you're asking CloudCode to do something, the first thing he's going to do is going to discover what the code base looks like, for an agent that is operating, not for code, but for like a different type of task, they also need to discover what data is available to them, so that might be, okay, where can I find information about Erik across all these different data silos, all these different services?

**Michel Tricot:** And that's what I call the discovery and search phase, and that's a place where actually the existing product of AirVide is very, very strong, which is we know how to pull every single piece of data from the system, and we know how to create what we call entity caches.

**Michel Tricot:** And then the second one is more about, like, when we think about the loop of an agent, it's just discover, then it's actually getting the data itself, like the relevant data.

**Michel Tricot:** So the discovery allows you to just narrow down what type of data you need to have access to, then you can fetch it.

**Michel Tricot:** It's like the fetch is everything that we have to do is looking at permissioning, looking at the most up-to-date information from the system of Rekop.

**Michel Tricot:** And the last one is really the ability to do and to perform actions.

**Michel Tricot:** So if somehow the task leads to, well, I need to update some information about...

**Michel Tricot:** Erik on this particular system.

**Michel Tricot:** How do you enable the agents to do it?

**Michel Tricot:** And that's really the loop that we see when it comes to accessing data.

**Michel Tricot:** It's like discovering, fetching, and acting.

**Michel Tricot:** And that's what the new platform is all about.

**Michel Tricot:** So the top part is really discovery and search.

**Michel Tricot:** And the bottom part is really about taking actions and reading the most up-to-date data.

**Michel Tricot:** Does that make sense?

**Erik O'Brien:** Erik Yep, I'm following.

**Michel Tricot:** And that's really the loop that we've identified with our customers.

**Michel Tricot:** And for one task, you might have multiple iterations of that loop because that's what the agent does.

**Michel Tricot:** It just discovers the world, understands the data, take actions, and that's all.

**Michel Tricot:** Erik And we want to be like the enabler for that.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** And so, I guess, looking at kind of the stack of the day of like, where does this fit within the, how we've defined kind of the agentic data infrastructure stack?

**Michel Tricot:** It really fits in the context piece.

**Michel Tricot:** Is that what you're asking for?

**Michel Tricot:** It's all about the context.

**Michel Tricot:** It's just the agent needs to have access to as much context and as much relevant context as possible.

**Michel Tricot:** And the ability to update that particular context.

**Michel Tricot:** And here, we're very much focused on your internal data, your company data, and that's the part of the context that we want to serve.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** you.

**Erik O'Brien:** Thank

**Erik O'Brien:** And if we were kind of looking at, you know, from a team that's building AI agents, like, what exact problems do you remove for those teams?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** What would they say, like, you know, imagining in the future, what is Airbyte and Gentic data, like, uniquely good at?

**Michel Tricot:** Yeah.

**Michel Tricot:** So, two things.

**Michel Tricot:** If you look at a world before Airbyte, every single company that is building an agent has to do many things.

**Michel Tricot:** The first one is they need to be able to integrate with the systems.

**Michel Tricot:** They need to be managing the authorization and authentication to the systems.

**Michel Tricot:** They need to be building the actual data pipelines because you need to have this ability to discover.

**Michel Tricot:** And most systems don't allow you to discover the data within their systems.

**Michel Tricot:** And, well, they need, basically, to build this whole block of how do you make this context available to

**Michel Tricot:** When you are in the world with Airbytes and the agentic data platform, all of this information is available through very simple agentic tooling, where you've just enabled and provided some credentials, and Airbytes will take care of how do you connect to the service, how do you manage authentication, how do you manage permissioning of the data, how do you manage the indexing of And how do you make it efficient and fast for users, plus all the maintenance of like, how do you make these connectors better over time, when APIs are changing, when rate limiting are changing, like all the things that people hate doing is something that we're exposed to very, very simple endpoints, and they never have to worry about that complexity.

**Michel Tricot:** Maybe I should send you the document.

**Michel Tricot:** next time.

**Erik O'Brien:** It would definitely be helpful for additional context.

**Erik O'Brien:** So can you describe, I think, you know, we talked about last time, like AI-ready connectors.

**Erik O'Brien:** Can you just describe that in kind of plain terms, like what that qualifies and what it doesn't?

**Michel Tricot:** Yeah, so AI connectors is the piece that is at the bottom here, which is the ability to do the action and the actual fetch of information.

**Michel Tricot:** So very simple, embeddable connectors that you can directly connect your agent to.

**Michel Tricot:** And they are really meant to be included into your code, to be added into all the code that you're writing for your agents.

**Michel Tricot:** So, because they operate...

**Michel Tricot:** So, operate...

**Michel Tricot:** So...

**Michel Tricot:** So...

**Michel Tricot:** So...

**Michel Tricot:** So much infrastructure, those are the ones that are very simple to open source for us because you can just install them into your project and with a one line, you just have access to all the data that you want to connect to.

**Michel Tricot:** The piece that is not really, I don't know if like, I don't call them like AI already, but they serve AI use cases is all our existing connectors that are like the replication connectors, like the ability to actually do an inventory of all the data that is available across your systems and build that particular cache.

**Michel Tricot:** But yeah, the one that we call AI connectors that we're releasing are the one that get people started very, very fast in exploring, exploring, like doing basic exploration, but very, very solid, like read and write into this operation.

**Erik O'Brien:** And if a team that was using the new platform kind of only turned on, you know, one feature to play with or kind of start testing around with, would that be the one?

**Michel Tricot:** Yeah, yeah.

**Michel Tricot:** The reason why direct connectors are so important is that that's generally how most teams that are building agents are starting.

**Michel Tricot:** Where, one, they want to test how good their agents can do with a very limited set of information and very controlled context.

**Michel Tricot:** Where, you know, can say, okay, like, you can tune the agent to say, Erik on Stripe is this particular ID.

**Michel Tricot:** And then you can see what the agent is going to be able to

**Michel Tricot:** To perform knowing that using the direct connector to fetch information about Erik using that particular ID, the moment when it breaks is that when you don't know who the user is going to be, when you don't know what is actually available across the whole inventory of beta, and that's when you need the top part.

**Michel Tricot:** And that generally comes as a second step in like any kind of agentic project, like you start with something that is very controlled, and then you have to go for something that is much broader where you don't know what kind of request you're going to receive, and that's where direct connector actually start failing, and where you need to have an ability to do that exploration, like an easy way to do that exploration.

**Michel Tricot:** I have a question.

**Michel Tricot:** How are the, how are we going to integrate the direct connectors with the replication connectors?

**Michel Tricot:** Yeah, uh, they are basically like to separate that of connector, but they are linked.

**Michel Tricot:** Okay.

**Michel Tricot:** We know that if you've connected Gong, for example,

**Michel Tricot:** For you will have two connectors running, one for replication, one for direct connection, and one is going to do the mirroring, and the other one will be able to just interact directly with, but it's going to be, it's using the same credential, the same permissioning model.

**Michel Tricot:** So you say, you kind of, it's the same sync or the same connection, but there's two connectors running and conducting two different types of tasks.

**Michel Tricot:** One is really about replication, which is the ability to build a full understanding of all the inventory of data.

**Michel Tricot:** The other one is really to operate at the record level.

**Michel Tricot:** And how does the replication connector, like, be it, like, can you explain the entity cache?

**Michel Tricot:** Like, how does it, like, kind of build the entity cache?

**Michel Tricot:** Yeah.

**Michel Tricot:** So the first version of the entity cache is going to be very similar to what you would have in a warehouse when you're replicating data.

**Michel Tricot:** So, dedicated, like...

**Michel Tricot:** Entity tables where you can search through.

**Michel Tricot:** So, if I want to say, hey, give me all the information about Invesco, give me all the support you get for Invesco, that's why the entity cache will be extremely important, is that it will first allow you to understand, okay, who is Invesco?

**Michel Tricot:** It will allow you to understand how is this account represented within Zendesk, for example, and then it will give you access to a list of all the most recent tickets that are available, and then what your agent can do once it has access to that information is just to use these IDs, these entities, to actually fetch the data directly from Zendesk and look at, okay, what are the attachments that are available, did they submit any reports, what is the latest, what the conversation, what was the last time I had the

**Michel Tricot:** The answer to a ticket.

**Michel Tricot:** And that's when the direct fetch becomes critical.

**Michel Tricot:** But to start, like the discovery and the search is very important as the starting point for doing any kind of task.

**Michel Tricot:** A good example would be, you know, recently someone was saying, okay, we just enrich all the data with Manus.

**Michel Tricot:** Right.

**Michel Tricot:** Okay.

**Michel Tricot:** Well, you didn't tell Manus, go, go figure it out.

**Michel Tricot:** You just gave Manus a list of users and then from that list of user.

**Michel Tricot:** So that was basically you replacing the search and the discovery.

**Michel Tricot:** You've done the discovery manually.

**Michel Tricot:** And then the agent, what it did is for every single one of these entities that you were prompting, it would go open LinkedIn, search for the person, get the information and return it and enrich it.

**Michel Tricot:** So that was, that's more, that's a search and fetch part.

**Michel Tricot:** Yeah.

**Michel Tricot:** Okay.

**Michel Tricot:** Okay.

**Michel Tricot:** Okay.

**Michel Tricot:** Okay.

**Michel Tricot:** Okay.

**Michel Tricot:** And that's what happens in most projects.

**Michel Tricot:** The discovery and the search is generally done in a very controlled way, where you provide what is the starting point, when you want to have the ability to have any kind of starting point, and have the entity cacher just prompt you, this is how you start if you want to get any information about Invesco.

**Michel Tricot:** And by the way, I also have data about Invesco on Salesforce, and I also have data about Invesco on the product database, and I also have information about Invesco in these other silos, and the agents can decide, okay, I want to know if I have information about Invesco on Zendesk, maybe I also care about like their consumption, so maybe let's look at what data is available on Orb, or like your metering system, or let's look at what is available also on Salesforce.

**Michel Tricot:** And then you start, the agents start grouping all this information, and give you like a full report of, this is what the state of Invesco is, and and what the

**Michel Tricot:** At some point, you might decide, yeah, maybe this customer is right, because they are very upset about one particular ticket, and boom, it starts running into your support or customer success system, you need to go into a call with Invesco right now.

**Michel Tricot:** And that's when the write actually comes to play.

**Michel Tricot:** Right, and these connectors, I mean, right now they don't do write, but the idea is that the connectors will eventually go to write back records and update things.

**Michel Tricot:** Yeah, and that's something I want to have in January, an initial version of write.

**Michel Tricot:** Okay, very cool.

**Michel Tricot:** Okay, makes sense.

**Michel Tricot:** But yeah, the entity cache today, it's a very simple search, but what I want to get to is actually the ability to link across multiple systems.

**Michel Tricot:** So here it might just ask, like, give me information you have on Salesforce.

**Michel Tricot:** What I wanted to be able to say is, like, here is the information on Salesforce, but you can also find information on X, Y, and Z.

**Michel Tricot:** visit not switch.

**Michel Tricot:** Thank

**Michel Tricot:** Got it.

**Michel Tricot:** Yeah, and I think, like, so actually, like, today in our meeting with Erik, we gave him the content calendar for the next, like, the post we're doing, and, like, one of them is also, one of them is on ontology as well, so maybe we, if we could go over that as well, so that they had no other contents to write about that.

**Michel Tricot:** Yeah, so, ontology, I would say, is still a little bit far in the future, in terms of how we're thinking about it.

**Michel Tricot:** In a way, the entity cache is the first version of what ontology is, because has the entity mapping on the first level.

**Michel Tricot:** Correct.

**Michel Tricot:** So it's really this ability to just have a representation of, within an organization, this is what, this is what a customer is.

**Michel Tricot:** This is all the places where you can find data about that particular, that particular.

**Michel Tricot:** Like, super entity that we call customer.

**Michel Tricot:** But yes, here, I would say that.

**Michel Tricot:** That's a place where we need to continue to do a lot more discovery, but the cache is the first version of Any questions, Erik?

**Erik O'Brien:** Sorry, was taking some notes.

**Michel Tricot:** I'm always taking silence as I was not there enough.

**Erik O'Brien:** No, no, no.

**Erik O'Brien:** I'm more just introspective and taking notes most of the time.

**Erik O'Brien:** Yeah, no, I'm following so far.

**Erik O'Brien:** So, how can customers deploy today, like, if they're using, is it, like, single tenant, hybrid?

**Michel Tricot:** So, we're building the cloud product.

**Michel Tricot:** Like, right now...

**Michel Tricot:** If they want to deploy, they only have access to the direct connectors, which is how do you get started as fast as possible, building your V1 of your agent.

**Michel Tricot:** Everything that has to do with the discovery is something where you have to go and start using our cloud product, and that's something that we will be releasing in private beta sometime in February.

**Michel Tricot:** But yeah, we basically, we have that piece here, because that's the existing, like, AirBite business, and we're actually building that piece here at the moment.

**Michel Tricot:** Thank you.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** you.

**Erik O'Brien:** All right, so I think we've got an idea of kind of the loop, the direct connections, the existing kind of business entity cache.

**Erik O'Brien:** I guess if we were to like paint the, we kind of walked through the before and after, but if we were like before and after of support co-pilot built with you or without, built with you versus without you kind of, can you just kind of paint like the story of like what a non-technical reader can picture?

**Michel Tricot:** Yeah.

**Michel Tricot:** So if you're building a support agent before, you would say, okay, what is the primary data source I need to look

**Michel Tricot:** Or what features have we added or what fixes have we done that might impact this particular customer.

**Michel Tricot:** So very quickly you end up with, yes, the dominant players for market shares in terms of the GitHub, the Zendesk, etc.

**Michel Tricot:** But not everyone uses those.

**Michel Tricot:** Or maybe they're using a version of it that is not the same that you've built.

**Michel Tricot:** So you end up having to build very quickly 10 connectors.

**Michel Tricot:** And then you realize, okay, now my problem is that with Zendesk, my only way to know what is attached to Invesco is what my customers are doing is they go on Zendesk, they look at the customer ID, and they say, instead of saying, oh, give me information about Invesco, they're going to say, oh, give me information about Invesco.

**Michel Tricot:** And by the way, this is...

**Michel Tricot:** On Zendesk, ID 12345.

**Michel Tricot:** That's a  experience because people are going in and out of my system.

**Michel Tricot:** And so what you're going to have to do is say, okay, well, it's pretty easy.

**Michel Tricot:** I just need to go look at all my Zendesk tickets and start identifying who is Invesco in Zendesk.

**Michel Tricot:** And I need to be able to make that mapping information available to my agents.

**Michel Tricot:** So suddenly, I need to go through all the customers that are listed within Zendesk.

**Michel Tricot:** I need to replicate them to create that mapping.

**Michel Tricot:** That's the replication piece.

**Michel Tricot:** And I need to make it available to my agents.

**Michel Tricot:** Oh, so now it means that every time I add a new customer, I need to make sure that I'm updating that mapping.

**Michel Tricot:** I'm updating this information because I need to be able to search and convert Invesco to an ID that then my agent can query somewhere.

**Michel Tricot:** Oh, and by the way...

**Michel Tricot:** I need to make sure that within Jira, I'm able to search all the tickets where Invesco is mentioned, but here I don't have a definition of the Invesco as a customer, I just know the name, someone put the word Invesco into my tickets.

**Michel Tricot:** So I need to build and replicate and create an index for all my tickets within Jira.

**Michel Tricot:** And you end up having to, yeah, I want to make sure also that all my tickets are probably replicated because what matters to me is probably the most recent ticket that was written.

**Michel Tricot:** And so you end up building that whole replication pipeline that has to connect to Zendesk, that has to connect to Jira, and that has to be able to replicate the data as a cadence, potentially like every minute to make sure that you have this information available in the cache in case someone or an agent is actually operating on Invesco.

**Michel Tricot:** And you end up just building this.

**Michel Tricot:** You end up building this.

**Michel Tricot:** And

**Michel Tricot:** You building this, you end up building all these interfaces, and you need to make sure that all of that is always up-to-date because someone is going to tell you, oh, wow, the data is not coming fast enough, or, oh, actually, you know what, the product is broken because suddenly Gong went from, not Gong, but Zendesk is going from, like, the V1 to the V2 in the API, I need to change that.

**Michel Tricot:** Oh, and by the way, they also changed what the data looked like and how you query the API.

**Michel Tricot:** And so you end up, so your only work now as someone who is building an agentic product is to build this, and it's to build this, and it's to build this.

**Michel Tricot:** And now you're also stuck.

**Michel Tricot:** You have to maintain that, and you need to maintain that.

**Michel Tricot:** And that's going to take the whole team to actually make them, to actually make them good.

**Michel Tricot:** And with Airbyte, you just have a simple API key.

**Michel Tricot:** few tools that you can plug into your agent, and boom, everything is handled for you.

**Michel Tricot:** And your agent...

**Michel Tricot:** Go ahead.

**Erik O'Brien:** What kind of tools would those be?

**Michel Tricot:** Like agentic tools.

**Michel Tricot:** like the ability for an agent to actually stop the flow of just generating text and actually ask an external service, like give me additional information.

**Michel Tricot:** I mean, when I'm talking about, does it make sense when I say tool that I'm talking about like agentic tools?

**Erik O'Brien:** Yeah, yeah.

**Michel Tricot:** Gotcha.

**Michel Tricot:** So that's basically it.

**Erik O'Brien:** Okay.

**Erik O'Brien:** What's the decision logic that kind of picks replication versus direct access for a given request?

**Erik O'Brien:** Like, is that a policy that, you know, you guys establish or is it customer or agent dependent?

**Michel Tricot:** Yeah, I think it's, it's more about what phase are you in?

**Michel Tricot:** So if you don't...

**Michel Tricot:** So if the agent doesn't know what to do, it should always start with the entity cache, because it needs to discover who is Invesco, where can I find data about Invesco, so that's when the entity cache is necessary, it's like the what's starting the whole processing, if you take a parallel with CloudCode, it's when CloudCode is going to go over your code base and it's going to start reading the code to understand what files should I be touching, what files exist, what library is imported, cetera, et cetera.

**Michel Tricot:** So it's more about gathering context.

**Michel Tricot:** And the moment you go for direct connection is when you actually need to get the real data, the most up-to-date data, to say, okay, now I know how to find Invesco onto Zendesk.

**Michel Tricot:** Now I know what tickets in Jira are mentioning Invesco.

**Michel Tricot:** Now I know what, like, tickets.

**Michel Tricot:** Tickets on GitHub are actually touching the feature that Invesco is complaining about, and that's when you start doing more of the fetch, and then when you need to actually write something, so maybe it's like writing an internal ticket onto Zendesk and say, well, this is everything that I found, or this is a response I want to provide to Invesco, that's when you also use the Direct Connect topic, because this one is about writing information back into Invesco.

**Michel Tricot:** the operational system.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** So is it safe to say, like, if we were to remove the entity cache from this diagram, all this would kind of collapse?

**Michel Tricot:** It would.

**Michel Tricot:** Yeah, but that's generally how product, like agentic product starts.

**Michel Tricot:** They only start without the cache, because you start by just making sure, can I interact, can my agent interact with this it's part.

**Michel Tricot:** Can it read?

**Michel Tricot:** Can it write?

**Michel Tricot:** But it's always very targeted.

**Michel Tricot:** Like the discovery is very intentional.

**Michel Tricot:** Like you say, I want to read information about Invesco and Gong.

**Michel Tricot:** And by the way, this is the call I'm interested in.

**Michel Tricot:** Or this is the customer idea of Invesco within Gong.

**Michel Tricot:** But getting ideas, knowing you have information on Invesco on Gong, like is something right now that is prompted by the user or by the agent.

**Michel Tricot:** But that's normally not how it works when you want to be at scale in production and having autonomous agent.

**Michel Tricot:** Like the autonomous agent is just figure out what we need to do next for Invesco.

**Michel Tricot:** And it needs to understand where is Invesco, where is Invesco, where do I have data about Invesco, pull all that information, and then come up with a list of tasks or a list of actions.

**Michel Tricot:** So how do you keep the cache coherent across replication and direct access paths?

**Michel Tricot:** Yeah.

**Michel Tricot:** The replication is basically leveraging the existing product and the data is most of the time up-to-date.

**Michel Tricot:** Maybe it was like one or two or five minutes delay, but the cache is always being populated and then direct connector becomes the source of truth.

**Michel Tricot:** If there is a mismatch between what the entity cache is returning and what the direct connector is returning, then the direct connector actually wins because it's actually getting the data directly from the system of record.

**Michel Tricot:** So this is also a question that I've been getting from the team a lot, like on the marketing side and everything.

**Michel Tricot:** You know, obviously...

**Michel Tricot:** ...

**Michel Tricot:** Merge has like a lot of momentum, like Merge and other tools, I guess like, I think, is there a competitive difference just to replication connectors or is there more to it, I guess?

**Michel Tricot:** Yeah.

**Michel Tricot:** I mean, if you don't have replication, you cannot do discovery and search.

**Michel Tricot:** So you're not, you cannot be an autonomous agent.

**Michel Tricot:** I see.

**Michel Tricot:** So they can basically, they can do fetch based.

**Michel Tricot:** They're basically just doing fetch by doing API integration.

**Michel Tricot:** Correct.

**Michel Tricot:** And then we're doing the discovery and search aspect.

**Michel Tricot:** Yeah.

**Michel Tricot:** Okay.

**Michel Tricot:** And we have, we have a headstart there because we already have the replication.

**Michel Tricot:** Okay.

**Michel Tricot:** That makes it, that makes it a lot clearer.

**Michel Tricot:** Yeah.

**Michel Tricot:** But that's really, that's really what matters, Zach.

**Michel Tricot:** If you want something that runs autonomously, you have to assume that the discovery has to be done autonomously.

**Michel Tricot:** If you, if it's just a copilot, yes, you can get by by saying, oh, agent, look at this, this document, and I'm giving you the URL of the document.

**Michel Tricot:** Okay.

**Michel Tricot:** That works really well with direct connection, but that's not how it is.

**Michel Tricot:** That's not what autonomy actually is.

**Michel Tricot:** If you want something that is autonomous, you need to come up with a specific target or goal or outcome that you want to get to, and the agent is going to figure out, what do I need to do that, where do I find information, pull the information, look at the system of record, and write back to the system of record.

**Erik O'Brien:** Anything to call out with the off module?

**Michel Tricot:** Yes.

**Michel Tricot:** This one is just about making sure that whatever data the agent is looking to get is allowed to have access to it.

**Michel Tricot:** at arehur Let's tells Are I

**Michel Tricot:** And whether the agent is an autonomous agent or whether the agent is controlled by a human through a chat or copilot experience, you want to make sure, imagine the case where you're looking to make a people, let's say a recruiting helper agent.

**Michel Tricot:** And you don't want anyone who has access to that copilot to be able to say, oh, what was the feedback that everyone gave Erik during his interview process when Erik is already hired?

**Michel Tricot:** This is something that maybe only your people team or your recruiting team should have access to, or maybe the hiring manager.

**Michel Tricot:** Or it can be, well, I want to create a payroll agent.

**Michel Tricot:** Well, then you need to be even...

**Michel Tricot:** even...

**Michel Tricot:** Okay.

**Michel Tricot:** to be even more careful about who has access to that co-pilot, and you need to make sure that maybe Kushal is leading a team, can only see the compensation for his own team, not for like Charles' team or another team, and that's where the authentication modules comes into play, it's like making sure that agents only accesses the data that it is allowed to have access to.

**Erik O'Brien:** Yeah, so we can basically have policies bind data access to the purpose of the task.

**Michel Tricot:** Right, and to the person, the, yeah, exactly.

**Erik O'Brien:** To the individual user as well, yeah.

**Erik O'Brien:** Is there any auth patterns to call out that are native, like OAuth paths or?

**Michel Tricot:** Yeah, I mean, this is really to access the integration points.

**Michel Tricot:** Like, the OAuth module is also very important at the edge.

**Michel Tricot:** side case.

**Michel Tricot:** I want Thank

**Michel Tricot:** Which is right here, which is what data is being written by the Airbyt tools.

**Michel Tricot:** But yes, otherwise, yes, it contains all the information about how do you connect to the end system, which user has configured their credentials, et cetera, et cetera.

**Michel Tricot:** Sorry, I'm doing some live editing I don't like.

**Erik O'Brien:** Any kind of call out for, like, the contract between agents and the platform?

**Erik O'Brien:** Like, I guess, is there, what is the precise contract between agents and your platform?

**Michel Tricot:** In what sense?

**Erik O'Brien:** Yes.

**Erik O'Brien:** Like, input schema.

**Michel Tricot:** The tool interface, I mean, those are pretty standard.

**Michel Tricot:** In terms of the schema itself, I think it's less and less important because agents are able to figure out like schema drift, schema differences, as long as the data is properly labeled and properly documented.

**Michel Tricot:** So in terms of the contract, while we're returning JSON objects and schemas and descriptions and things like that, so that the agent actually understands what each field is about, but we're not too prescriptive in what the data, how the data changes, because the agents in general can figure it out.

**Erik O'Brien:** And then how do the platform kind of expose provenance or like confidence back to the agent or to the user?

**Erik O'Brien:** Is it like citations or freshness labels or policy badges or something like that?

**Michel Tricot:** Good question.

**Michel Tricot:** I've not thought about it.

**Michel Tricot:** Okay.

**Michel Tricot:** I mean, the thing is like the tools is actually pretty, it's pretty clear about what data, where data is coming from.

**Michel Tricot:** Now it's more like how does the, the builder of the agent want to surface that information?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So more of a UI decision by that agent builder.

**Michel Tricot:** Yeah.

**Michel Tricot:** Like all the, all the metadata is available and is attached.

**Michel Tricot:** Like, you know, it's coming from Salesforce, you know, when it was last replicated, you know, what, like the freshness of the cache, you know, that it was a call from Salesforce that it's, that returned that data.

**Michel Tricot:** So.

**Michel Tricot:** so.

**Michel Tricot:** All this information is real and is available to the agents.

**Michel Tricot:** Now it's up to the builder to actually figure out how they want to surface it.

**Erik O'Brien:** Any failure modes that you've already kind of tested against?

**Michel Tricot:** What you call a failure mode?

**Erik O'Brien:** I don't know, and the direct connectors potentially not working or...

**Michel Tricot:** Yeah, in that case...

**Michel Tricot:** Yeah, that's actually...

**Michel Tricot:** So the good thing with having both the cache and the direct connector is the direct connector guarantees you freshness.

**Michel Tricot:** But also the danger with the direct connector is that if there is anything wrong, then your operation stops.

**Michel Tricot:** week's Thank you.

**Michel Tricot:** If, for example, an API is down, well, you cannot have access to that data and your agent is stuck.

**Michel Tricot:** You can always fall back to the cache.

**Michel Tricot:** So you might have more stale data, not the most up-to-date data, but you still have some data available to you.

**Michel Tricot:** In terms of what if the entity cache fails, well, this is not good because it means that the discovery cannot happen.

**Michel Tricot:** So you can still leverage the direct connector, but at that point, you cannot have the autonomy you want from your agents.

**Michel Tricot:** Because they won't be able to know where is the, where do I have data about growth .

**Michel Tricot:** But at that point, becomes our, I mean, that's our job to make sure it's, it doesn't fail.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Michel Tricot:** Yeah.

**Michel Tricot:** But yes, the entity cache and the replication makes it so that the direct connector, if anything wrong happens with it, if anything wrong is broken about the source system, you can still operate because the data is available.

**Erik O'Brien:** So what about this kind of overall platform or system becomes more defensible with scale, like connector hardening, data maps?

**Erik O'Brien:** I guess what's the compounding advantage or kind of the mode story you guys are trying to build with agentic data?

**Michel Tricot:** Yeah, I think the same one we've done in the data space, which is, it's very hard to operate and build and maintain all these connectors.

**Michel Tricot:** And today we have a very efficient...

**Michel Tricot:** So of doing so.

**Michel Tricot:** The other part is the value you can provide once you have the entity cache is really this ability to discover across multiple silos.

**Michel Tricot:** So it's not a network effect because the data is just for one customer, but it makes it so that we can create connections between different systems and we can do it automatically.

**Michel Tricot:** So you get more value the more system you connect to the system as a customer.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** With the last couple of minutes, anything I haven't asked that you want to touch on or anything else in the doc we haven't covered yet?

**Michel Tricot:** Uh, no, I might just share.

**Michel Tricot:** The document with you, so you have access to the whole context.

**Michel Tricot:** Yeah, and that'll be helpful.

**Michel Tricot:** And then, yeah, it'll obviously help with writing all of our articles, too.

**Michel Tricot:** Yeah, I know.

**Michel Tricot:** I'm investing in our article writing context.

**Michel Tricot:** Yeah, it's going into the growthx.ai mind.

**Erik O'Brien:** All right.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** This is obviously super helpful to kind of get a little bit closer to the product, the platform.

**Erik O'Brien:** Better understand kind of what we're looking at and what we can start to talk about.

**Erik O'Brien:** Some of the key points.

**Erik O'Brien:** So really appreciate the time.

**Michel Tricot:** Of course.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Well, I'll look out for an invite to this doc.

**Erik O'Brien:** And then if any other kind of follow-up questions come up, once I get a chance to look through it, I'll either reach out through Khrushal or in Slack.

**Michel Tricot:** No, good.

**Michel Tricot:** Khrushal, can you share it?

**Michel Tricot:** Yeah, I'll share it with you.

**Erik O'Brien:** Yeah, it's in our Slack.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Khrushal.

**Michel Tricot:** Khrushal.

**Erik O'Brien:** Great, thank Erik, thanks.

**Erik O'Brien:** Thank you, talk later, bye.

**Michel Tricot:** Okay, about the document on your site?

**Michel Tricot:** Yeah, look, this was pretty, really helpful.

**Michel Tricot:** Yeah, think like, just need to be more, just need to make your address of the product for writing everything, yeah, but thank you.
