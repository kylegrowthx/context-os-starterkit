# Attio <> GrowthX

<metadata>
date: 2025-03-28
time: 22:02 UTC
duration: 32 minutes
organizer: Jason Gong
participants: Jason Gong (GrowthX), Matthew Fischer (Attio)
fathom_recording_id: 54486334
fathom_url: https://fathom.video/calls/264591034
share_url: https://fathom.video/share/N3aqKGsadFVJhJsWiHYJTeMPBCf39zSF
source: fathom
enriched_on: 2026-03-04 23:27 UTC
</metadata>

---

## Summary

Jason Gong (newly hired Head of GoToMarket at GrowthX) and Matthew Fischer (Attio) discussed solving GrowthX's lead qualification bottleneck by implementing Default for lead routing with a webhook integration to Attio, rather than using Chili Piper or RevenueHero. Matthew demonstrated how Attio's workspace object can power customer success management through lists, sequences, and automations—showing GrowthX how to track customer health, manage renewals, and run onboarding pipelines, with GrowthX planning to add around 10 additional "lite" users at a discounted rate when expanding beyond their core team.

---

## Context

GrowthX is a B2B content marketing agency that recently hired Jason Gong as Head of GoToMarket. GrowthX has been using Attio for their CRM but Jason is new to both the company and the platform. The core problem driving this meeting: GrowthX's sales process (currently handled primarily by the founder, with occasional help from Kyle) is bottlenecked by unqualified leads reaching the team. Jason wanted to explore lead qualification and routing solutions (Chili Piper, RevenueHero, Default) and understand how to optimize Attio for customer success management as they scale.

Attio is a next-gen CRM platform, and Matthew Fischer is their customer success representative. The conversation showed that Attio can integrate with various lead qualification tools via webhooks, and that its workspace object (which represents customer accounts) enables sophisticated post-sale operations through lists, automated workflows, and data enrichment from sources like Segment and Polytomic.

---

## Relevance

- **To GrowthX Business Development:** Lead qualification via Default is in beta at Attio but can be integrated via webhook immediately. GrowthX identified ~10 additional "lite" users needed for their delivery pods (8-9 pods total). Matthew offered to structure a discounted rate as a workaround until Attio launches formal lite user tiers in Q2 2025.

- **To GrowthX Delivery:** Attio's workspace object can track customer accounts with billing data, product usage, and acquisition metrics. GrowthX can build lists for onboarding pipelines, renewal management, and account health monitoring. Custom objects can represent projects with Kanban views. Sequences tool integrates with workflows for email campaigns and Slack alerts.

- **To GrowthX Business Model:** Jason flagged the need for a CDP (exploring HighTouch) to sync product usage data into Attio. Matthew demonstrated Attio's use of Segment + Polytomic for automated data syncs and workflows that trigger sales escalations (e.g., "added 10 users in last month" → enterprise sales outreach).

---

## Overview

- GrowthX will implement Default for lead qualification and routing (currently in beta at Attio), integrating via webhook since native integration isn't yet available
- Attio's workspace object represents customer accounts and can store billing info, product usage data, and acquisition metrics for customer success workflows
- Attio enables custom lists for onboarding pipelines, renewal management, and account health monitoring; sequences tool for email campaigns; and custom objects (e.g., for projects) with Kanban views
- Matthew offered a discounted rate structure for ~10 additional limited-access "lite" users to support GrowthX's 8-9 delivery pods; formal lite user tiers are planned for Q2 2025

---

## Key Topics

### Lead Qualification and Routing Solution

GrowthX's core problem: the founder and Kyle (sales team) are bottlenecked by unqualified inbound leads. Jason evaluated three solutions—Chili Piper, RevenueHero, and Default—based on their ability to do conditional form branching, call external APIs (e.g., SEO tools to check website traffic/backlinks), and embed a calendar. Default emerged as the clear preference: it has built-in enrichment from Apollo and Clearbit, supports complex conditional logic and progressive forms without needing web devs, and can integrate with Attio via webhook even though the native integration is still in beta. Matthew confirmed that lack of a native integration is not a blocker—any form tool with a webhook capability can pipe data into Attio.

### Attio for Customer Success Management

Matthew demonstrated Attio's architecture for post-sale: the workspace object represents a customer account and stores billing info, product usage data (from Segment syncs), and acquisition metrics. Users are distinct from contacts—users have product accounts while contacts are just people. Lists are used to organize workspaces by status (onboarding pipeline, renewals, account health with filters for good/okay/bad health). Sequences tool provides email campaigns integrated with workflows. Activity feeds track product usage updates and list membership changes sourced from Segment and Polytomic syncs, though the feed doesn't pull in company emails and meetings—those live in the associated company record but can be used for filtering/reporting.

### Attio Customization and Flexibility

Custom objects can be created for domain-specific use cases (e.g., projects). Lists can be configured with Kanban views to visualize workflow stages. Tasks can be assigned to either workspaces (post-sale) or companies (sales), though Matthew acknowledged Attio could have better internal standards around this. Workflows trigger automations like rounding leads to team members by geography during onboarding or firing sales alerts when product usage milestones are hit (e.g., "added 10 users in the last month").

### Lite User Access and Pricing

Attio does not currently offer lite/viewer user tiers—all seats are full-price. However, Matthew offered GrowthX a workaround: structuring a discount into their subscription if they add 10 additional users for their delivery pods (8-9 pods, approximately 1 lite user per pod plus some overlap). Formal lite user tiers with billing restructuring are planned for Q2 2025; no rush on either side.

---

## Action Items

- **Jason Gong (GrowthX):** Implement Default for lead qualification and routing; set up webhook integration to Attio (Matthew available to help wire this up)
- **Jason Gong (GrowthX):** Activate Attio's workspace object and build lists for customer success: onboarding pipeline, renewal management, account health monitoring
- **Jason Gong (GrowthX):** Explore Segment or HighTouch integration to sync product usage data into Attio for automated workflows and alerts
- **Jason Gong (GrowthX):** Follow up with Matthew when ready to add 10 additional lite users; Matthew will structure a discounted rate until formal lite tiers launch in Q2 2025

---

## Transcript
**Matthew Fischer:** Hey, Jason, how are you?

**Jason Gong:** Hey, doing good.

**Jason Gong:** Thanks for jumping on on such short notice.

**Matthew Fischer:** No, of course.

**Matthew Fischer:** I appreciate you reaching out and kind of flagging what you guys are looking for and how you need to be supported.

**Jason Gong:** So, excited to chat.

**Jason Gong:** For sure.

**Jason Gong:** I mean, for context, I basically just joined this week.

**Jason Gong:** I guess my official title is Head of GoToMarket.

**Jason Gong:** So all this RevOps stuff is falling on me a little bit.

**Jason Gong:** Never used Attio.

**Jason Gong:** Almost exclusively just used HubSpot.

**Jason Gong:** I haven't even used Salesforce, honestly, like very much anyway.

**Jason Gong:** Yeah, but I mean, it seems really, really cool.

**Jason Gong:** It's also very early.

**Jason Gong:** I do have a few questions maybe we can leave to the end.

**Jason Gong:** But the one thing we wanted to do is, like, right now, we...

**Jason Gong:** We have a kind of lead funnel that's just, I mean, we have like one page and then it's just like an account lead form that fills Attio.

**Jason Gong:** And one gap is like we don't really qualify too much.

**Jason Gong:** We have a, we're currently bottlenecked by our ability to take on new clients and because we don't qualify kind of enough at the beginning and do enough discovery, like I feel like we're letting in customers that aren't a great fit and we waste a lot of time on them that could have went to somebody that was a better fit.

**Jason Gong:** So yeah, just trying to kind of start that qualification as early as possible, basically.

**Jason Gong:** I mean, hopefully that's helpful enough context.

**Matthew Fischer:** No, no, it is.

**Matthew Fischer:** And it's something that we face ourselves in terms of we were, I mean, at this point, we're still only doing inbound and we have to do a lot of qualification up front to ensure that you're working with the highest value leads and you're not overwhelming your sales team with leads that are less qualified.

**Jason Gong:** And our sales team is one person.

**Jason Gong:** It's our founder.

**Matthew Fischer:** So, I mean, at this point, I might take some calls soon.

**Jason Gong:** There's somebody named Kyle who you may or may not know who might take some calls.

**Jason Gong:** But that's also part of the problem why we need to qualify more because it's very costly to make him take an unqualified call.

**Matthew Fischer:** Yeah, of course.

**Matthew Fischer:** So in terms of this lead flow, I mean, you sent over a really helpful overview of one path you're thinking about.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** I guess the, as an example, what we do is we have, I mean, we will send leads to Attio based on signups, but also we have a talk to sales form, which will then send a lead to Attio.

**Matthew Fischer:** And then we have a workflow automation set up within the system that will basically qualify the lead based on the enrichment that Attio does automatically, but then also based on additional enrichment that we can do via our AI attributes, and then decides whether or not it passes a qualification test.

**Matthew Fischer:** And if it does, automatically enroll the person into an email sequence that comes from an account executive.

**Jason Gong:** So that's one path you can set up. Yeah, that part, I'm interested in that.

**Matthew Fischer:** No, I was just going to say that's like, that's one flavor, but there are different ways you can hook this up.

**Matthew Fischer:** So if you wanted to set something up to, like based on the information someone provides in the form, like, you know, conditionally display a calendar link, there can be solutions there with a form provider.

**Jason Gong:** Yeah, I think that's the part I'm interested in.

**Jason Gong:** And I'm pretty, you know, like familiar with it.

**Jason Gong:** It seems like with Attio, very full-featured, and I feel like I can do everything I need if I'm okay with them submitting the form and then seeing a, all right, we'll reach out to you later.

**Jason Gong:** It seems like the qualification I can do there is pretty much that can be done.

**Jason Gong:** I guess the version where I have a form, there's kind of conditional branching, and then there's optionally a calendar at the end of that seems a little bit less so.

**Jason Gong:** Like at least with Attio on its own.

**Jason Gong:** So I've looked at Chili Piper, which does not support Attio, and also RevenueHero, which does not support Attio.

**Jason Gong:** I'm kind of looking at default right now, which seems to do everything I need, but I just wanted to make sure I'm considering everything.

**Jason Gong:** And it looks like the one option you guys floated was Typeform integrated into Attio.

**Jason Gong:** I mean, does Typeform have the capabilities I need?

**Jason Gong:** How it works, guess maybe try to think of the requirements there, because I've used Typeform extensively, and just like, it doesn't feel like it's great for this sort of stuff.

**Jason Gong:** Maybe I haven't used the right tier.

**Jason Gong:** The things I want to do: can Typeform toggle things in Attio as someone's rolling through different branches? Can it call arbitrary APIs, like our SEO tools? For example, if someone gives us a website, we want to check if they're already doing SEO—check their traffic and backlinks.

**Jason Gong:** So we look at if your website has a lot of traffic and backlinks and stuff, like, can it call arbitrary APIs to like, get info back and then logic based on that?

**Jason Gong:** Does it have kind of enrichment sources out of the box that are like, decent?

**Jason Gong:** That's the stuff I kind of care about.

**Jason Gong:** Does it have decent built-in enrichment sources? And at the end, if it shows a calendar, do I still have to use Calendly on top of Typeform, or is there another option?

**Matthew Fischer:** Yeah, no, no, super helpful.

**Matthew Fischer:** I think, I mean, based on everything that you're saying, I appreciate the further context, especially around having, like, making calls to other solutions.

**Matthew Fischer:** I'm not sure if type form would be the best fit there.

**Matthew Fischer:** If you have a form provider in mind and they support webhooks, I can help you wire that up to Attio. Two things happen: first, we send the form data to Attio. Second, if your team members' mailboxes are synced to Attio, calendar events trickle through and automatically create contacts and companies.

**Matthew Fischer:** So really, it's just about having a webhook for the form submission hit Attio.

**Jason Gong:** Okay, that makes sense. Are you aware of tooling your customers use for routing with conditional logic that ends in a calendar, before it hits Attio?

**Matthew Fischer:** Yeah, Chili Piper is actually pretty popular for that.

**Jason Gong:** Wait, so can you use Chili Piper with audio or no?

**Jason Gong:** Because when I filled out their demo form, they were like, sorry, we don't support your CRM.

**Matthew Fischer:** So they don't have a native integration, which is why you just have to set up a webhook, a simple webhook to fire to us.

**Matthew Fischer:** Oh, see.

**Matthew Fischer:** Right.

**Matthew Fischer:** But nothing else, like there won't be any other issues with using Chili Piper plus Attio.

**Matthew Fischer:** Because again, as long as, you know, the scheduling component through Chili Piper, that will go to your team member's calendar, which will then sync through the mailbox, sync into Attio.

**Matthew Fischer:** The webhook will handle sending the data to Attio.

**Matthew Fischer:** And another reason why, I mean, there are some teams who, you know, want to use something like Calendly or Cal.com and then use another form tool.

**Matthew Fischer:** But if you're looking for something that...

**Matthew Fischer:** It has like routing and then also scheduling all in one place.

**Jason Gong:** Chili Piper is quite popular.

**Jason Gong:** That's pretty good.

**Jason Gong:** Okay.

**Jason Gong:** And then this revenue hero.

**Jason Gong:** So I guess, I mean, how do I even use this though?

**Jason Gong:** Like when I do get a demo, okay, am I just supposed to say, because I guess I just lie on the, on the form, but like it just feels like they don't want to talk to you unless you're using Salesforce or HubSpot.

**Jason Gong:** Which is clunky.

**Jason Gong:** Okay.

**Jason Gong:** Do you, have you heard much about default at all?

**Matthew Fischer:** Yeah, they might be a customer of ours. From a partnership perspective, we've been in conversation with them and a few of our customers use them as well. I think that could definitely be an option. In terms of native integration, I would think we'd have one with Default before we have one with ChiliPiper.

**Jason Gong:** Yeah, I mean, they said, I was talking to them earlier today, they said it's in beta, but it's not released yet.

**Jason Gong:** So what you're saying is it doesn't matter if there's no native integration—we can just use a webhook or API call at the end to pipe the data in.

**Matthew Fischer:** Yep, exactly.

**Jason Gong:** Which is totally cool, because it seems like I would have to do that with default anyway until they build that integration.

**Jason Gong:** And I mean, I guess, what does building an integration even do other than like piping that form data in at the end?

**Jason Gong:** Like, is there anything else that I'm missing?

**Jason Gong:** What does the native integration really mean?

**Matthew Fischer:** You know, for things like forms in this particular flow, it's really just sending the form data.

**Matthew Fischer:** One thing I'll flag for Default is that you might be able to get away without setting up a webhook because they have a Zapier integration.

**Matthew Fischer:** But if you'd prefer not to use Zapier, we can definitely work on setting this up together so that it just hooks up directly to Attio.

**Jason Gong:** So Typeform plus other tools isn't a great solution. Chili Piper is more expensive. RevenueHero seems cheaper, but if I fill out their demo form and say "other" for CRM, they disqualify me.

**Matthew Fischer:** I have to say, Salesforce might be the keyword for them to get a card.

**Jason Gong:** Yeah, I guess so.

**Jason Gong:** I don't understand why it's not self-serve. It's less than $100 a month—I don't know how they can afford to talk to everyone.

**Matthew Fischer:** And did you say you chatted with default earlier today?

**Jason Gong:** Yeah.

**Jason Gong:** Yeah, I talked to them already.

**Jason Gong:** How did their solution look for this?

**Jason Gong:** I mean, honestly, it looks pretty good.

**Jason Gong:** Apart from the fact that I have to, I guess, write an API call to connect it to default or to Addio.

**Jason Gong:** Everything looks great.

**Jason Gong:** It has.

**Jason Gong:** It

**Jason Gong:** Apollo and Clearbit just kind of, like, bundled in so I don't need an account or anything.

**Jason Gong:** I can use that.

**Jason Gong:** I mean, I guess I don't know if there's anything special that Chili Pepper can't do.

**Jason Gong:** But, I mean, another nice thing is, like, it has, like, this kind of progressive form and web page that's kind of, like, built into it as well.

**Jason Gong:** So I don't have to get my web devs involved.

**Jason Gong:** I can build, like, a very kind of complicated pathing, like, you know, if it's, like, JSON.

**Jason Gong:** Jason at bigtech.com.

**Jason Gong:** It just goes straight to Calendar.

**Jason Gong:** And then if it's something in the middle, you can ask more questions.

**Jason Gong:** If it's, like, something that looks unqualified, you can route to, like, an email.

**Jason Gong:** I guess I would use Attio for that, so it's not special to them.

**Jason Gong:** Yeah, so it looked nice.

**Jason Gong:** I feel like the only other thing I'm kind of considering is Revenue Hero.

**Jason Gong:** If they're disqualifying me, it'll take them a couple days to get back to me unless I say I'm using Salesforce. I appreciate the help—I'll probably just go with Default to keep things moving.

**Jason Gong:** You still there? I do have some questions.

**Matthew Fischer:** No worries. My internet was having trouble so I disabled my video.

**Jason Gong:** I guess the other thought was, OK, so I've used HubSpot before.

**Jason Gong:** I think HubSpot is pretty decent as a post-sales upsell and even just monitoring customers type of tool.

**Matthew Fischer:** Yeah.

**Jason Gong:** For Attio, do you guys recommend doing stuff like that for customer success?

**Matthew Fischer:** I can show you what we have set up.

**Jason Gong:** Yeah, that would be amazing.

**Matthew Fischer:** Yeah, we use Attio for customer success. I can show you how to set up a workspace record for your team and how that powers different flows. Let me pull up a demo workspace record.

**Jason Gong:** Do you have a viewer-type account? For example, we have customers and pods that work with them. Within each pod, there are people who don't need full access but would benefit from seeing the customer page, activity feeds, and triggers. Is there just one level of account?

**Matthew Fischer:** Yeah.

**Matthew Fischer:** That's something we're working on—different user tiers over the next quarter or two—but we need to restructure billing first.

**Matthew Fischer:** But in the meantime, if you have, how many team members would this be that you'd be adding on?

**Jason Gong:** How many lite-type people would we add? At least five, I'd say.

**Jason Gong:** I mean, we have pods.

**Jason Gong:** I actually don't know how many pods we have.

**Jason Gong:** I think.

**Jason Gong:** think.

**Jason Gong:** We have eight or nine pods, so at least one per pod. Let's say 10 more people total.

**Matthew Fischer:** Okay.

**Matthew Fischer:** Yeah, so what I can do is I could, as a workaround, basically just structure a discount that I add into your subscription, so that if you add in those 10 seats, then they'll be at a discounted rate.

**Jason Gong:** That's interesting. Let's do that after we move our customer success data in here. I'd like to see how you set up the GrowthX workspace. For example, if we added two new users recently, what would you track to understand how that impacts our pipeline?

**Matthew Fischer:** Yeah, definitely.

**Matthew Fischer:** Let me share my screen. Can you see it?

**Jason Gong:** Yep, I see it.

**Matthew Fischer:** Okay, perfect.

**Jason Gong:** Okay, so you guys need to segment.

**Matthew Fischer:** Yep.

**Matthew Fischer:** And we have, so there's an object you can use out of the box called workspaces.

**Matthew Fischer:** And what it can ultimately represent is a customer account.

**Matthew Fischer:** So for each workspace record, we'll create a, or sort of each account, we'll create a workspace record.

**Matthew Fischer:** And then this is where we pipe all the information with regards to, like, basic information about the customer account.

**Jason Gong:** Where do I find that, actually?

**Jason Gong:** I'm looking at my account right now.

**Jason Gong:** I see, I see records, I see lists, and then I have, like, the tab on the left, like, notifications, tasks, notes, emails.

**Matthew Fischer:** Click your workspace name (growthx.ai) in the top left corner. Then go to Workspace Settings and navigate to Objects under the Data section.

**Jason Gong:** Sorry, could you do that one more time?

**Matthew Fischer:** Let me flip into my demo account to show you since I have admin permissions there.

**Matthew Fischer:** Then you'll see users and workspaces, which are two objects you could activate.

**Jason Gong:** Is this included in my plan?

**Matthew Fischer:** Yes, it's included.

**Matthew Fischer:** So a workspace represents a customer account, and this is where we pipe in billing information for the account, product usage data, acquisition data, if we have it at the time of conversion, and then a user represents a user within a given customer account.

**Matthew Fischer:** And we associate a company with a workspace, and then we'll associate users with their corresponding person record.

**Jason Gong:** So a user is different than a contact because a user has usage tied to it and account info?

**Matthew Fischer:** Yeah, you can think of companies and people as just people in the world that you've interacted with, companies or companies in the world you've interacted with, and then a user is someone who actually has a user account with your product, and then a workspace is a customer account.

**Jason Gong:** This is great.

**Jason Gong:** Okay, yeah.

**Jason Gong:** Then, can I just take a look at what ours looks like just on your screen?

**Jason Gong:** want to see what you guys typically, how you structure things.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** So we have a, oh, go ahead.

**Jason Gong:** No, I'm just thinking.

**Jason Gong:** So I guess here is where things are updated, and then I guess you have workflows.

**Jason Gong:** know, it's like added 10 users in the last month, and then you get your enterprise sales guy to reach out to us.

**Matthew Fischer:** That's where stuff like that happens.

**Matthew Fischer:** Yeah, exactly.

**Matthew Fischer:** And then we also have a, so alerts based off of automation.

**Matthew Fischer:** And based off the changes that happened with the product usage or something like that, we'll trigger alerts for the sales team.

**Matthew Fischer:** But then we also have an onboarding pipeline that we, how we manage our onboarding process.

**Matthew Fischer:** So this is a list and workspaces get added to it at the time of conversion.

**Matthew Fischer:** So when someone converts to paid, we will, in the workflow, qualify that account to see if they meet our onboarding threshold.

**Matthew Fischer:** And if they do, then they get added to the list, round-robin to the right team member based on geo.

**Jason Gong:** So a list is like, I guess, how do people use lists?

**Jason Gong:** So like, for example, if we have like churn likely, like that would be a list that's kind of like a category of like behavior almost.

**Jason Gong:** Or I guess in this case, it looks like an action needed type of list onboarding pipeline.

**Matthew Fischer:** Yeah, we have a list for onboardings. We also have a separate list for renewals and another for monitoring top accounts.


**Matthew Fischer:** We have different filters on that list, so we can check to see customers who are in good health, customers that are in okay health, and then bad health.

**Jason Gong:** Right.

**Jason Gong:** So managing renewals, let's say it's like, whatever, three months to renewal date, you'll put people on that list, and then maybe some campaigns that try to talk to us or something, you know?

**Matthew Fischer:** Yeah, exactly.

**Matthew Fischer:** And then we also have within the product, I don't know if you've seen it, but we have a sequences tool.

**Matthew Fischer:** So what's nice about this is that it can plug right into workflows.

**Matthew Fischer:** So if you have an automation for, say, inbound leads or for renewals, where when a renewal date's coming up, they automatically get added to the renewal list, so then you have a place where you can manage that.

**Jason Gong:** Can a sequence send Slack messages?

**Matthew Fischer:** It can't send a Slack message.

**Matthew Fischer:** We have an integration with Slack that is through a workflow where you can send a Slack message to a channel.


**Jason Gong:** Yeah, because I guess we talk to our customers mostly through Slack, but I guess an email is fine too.

**Jason Gong:** Okay, but I guess for all intents and purposes, like a sequence is kind of just a workflow, but with emails only.

**Matthew Fischer:** Yeah, exactly.

**Matthew Fischer:** Yes, exactly—a traditional email sequence.


**Jason Gong:** Okay, so I see lists.

**Jason Gong:** I see like, I guess all these properties.

**Jason Gong:** This activity feed kind of makes sense.

**Jason Gong:** Could you just like scroll around in this activity feed on the left there?

**Matthew Fischer:** Yeah, absolutely.

**Matthew Fischer:** The activity feed shows updates from Segment.

**Matthew Fischer:** We also use Polytomic to sync with our data warehouse.

**Matthew Fischer:** Also updates like when we move records within the onboarding pipeline or add them to lists.

**Matthew Fischer:** In terms of monitoring things like meetings and emails, that's where you'll go through to the connected company.

**Jason Gong:** Okay, so that's in the company.

**Jason Gong:** Okay, so those kind of activities don't really get pulled into the workspace object?

**Matthew Fischer:** Correct.

**Matthew Fischer:** They don't get pulled into the record page, but when these things are associated, you can use that information for filtering purposes, for reporting purposes.

**Matthew Fischer:** Let's say, for example, I was looking at a list of top customers, and I wanted to filter them for customers I haven't spoken with in, say, a month.

**Matthew Fischer:** Because the company and the workspace are associated, I can drill down into the company and pull that filter.

**Jason Gong:** This is interesting.

**Jason Gong:** We weren't sure what to use for customer success. There are standalone tools, but we're also about to get a CDP.

**Jason Gong:** We're just about to get a CDP of some kind.

**Jason Gong:** Not sure if you have any recommendations.

**Jason Gong:** Looks like you guys' segment.

**Jason Gong:** We're looking at High Touch.

**Jason Gong:** Yeah, but basically doing all the stuff you're showing.

**Jason Gong:** So this is very helpful.

**Matthew Fischer:** Perfect.

**Jason Gong:** Yeah.

**Jason Gong:** Okay, great.

**Jason Gong:** I think you've shown most of the interesting parts. Could you go back to the workspace record for a second?

**Jason Gong:** Okay, so I see there's a task tab here.

**Jason Gong:** When would a task be here associated with a workspace versus, because I saw your company had a bunch of tasks in it.

**Jason Gong:** Why would you put it in company versus workspace?

**Matthew Fischer:** Yeah, to be honest, I think this is something that we could have internally, we could have better process around.

**Matthew Fischer:** The workspace is the source of truth for post-sale folks.

**Matthew Fischer:** And then obviously, for some things, you'll need to jump into the company record to catch up on looking at specific emails or meetings.

**Matthew Fischer:** But really, in terms of data and where you live, I also work in post-sale, and I live primarily off of workspace records.

**Matthew Fischer:** So I think from a process perspective, if someone in sales was creating tasks, they should have that associated with the deal.

**Matthew Fischer:** And then for post-sale, have those tasks created and associated with the workspace.

**Jason Gong:** For you guys, tasks are about upselling and retention. But we're an agency with a lot of delivery work, so I need to think through what goes in Attio versus where projects live. That's something I'll figure out.

**Matthew Fischer:** One other thing to mention with lists: you can create custom objects, like for projects, and use Kanban views to visualize them.

**Matthew Fischer:** Teams use Kanban views to track project stages and information—you could apply the same framework to customer success workflows.

**Jason Gong:** I think I have a rough idea of what I'd use this for.

**Jason Gong:** I can imagine lists for upselling new service lines or churn prevention. This is very helpful. I'll go with Default for lead routing and implement the workspace thing as soon as I can. For the additional users, I'll follow up once I get workspaces figured out.

**Matthew Fischer:** Yeah, that sounds great.

**Matthew Fischer:** No rush on the user seats. We're happy to work with you to bring folks in with limited access at a discounted rate. Just reach out when it makes sense.

**Jason Gong:** Thanks for your help, Matthew.

**Matthew Fischer:** Thanks for the time, Jason.

**Jason Gong:** Bye.
