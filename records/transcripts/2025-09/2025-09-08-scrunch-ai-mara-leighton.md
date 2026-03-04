# Scrunch AI (Mara Leighton)

<metadata>
date: 2025-09-08
time: 16:34 UTC
duration: 23 minutes
organizer: mara@growthx.ai
participants: Mara Leighton, Vivek Shankar, Mariana Montezzana, Andrew Sorensen
fathom_recording_id: 85669326
fathom_url: https://fathom.video/calls/402416280
share_url: https://fathom.video/share/EktXhCnz2et2cyrpffdNbKRYqJtzstRB
source: fathom
enriched_on: 2025-03-02 08:30 UTC
</metadata>

---

## Summary

GrowthX team (Vivek, Mariana, Mara) and Andrew Sorensen from Scrunch AI worked through technical questions on site audits, LLM query depersonalization, and client reporting. Key discussion focused on how Scrunch uses incognito mode to avoid bias in LLM responses, why JavaScript-rendered content requires HTML replication for indexing by most LLMs (Gemini is the only exception), and how to set up reporting—particularly month-over-month performance analysis using Looker Studio templates instead of in-app limitations. Andrew confirmed that custom date ranges are rolling out and flagged upcoming enhancements like state/metro-level geo-targeting and improved chart visualization.

---

## Context

Scrunch AI is the CheckThat technology partner that powers GrowthX's AI visibility offerings. Andrew Sorensen is a technical product specialist from Scrunch responsible for supporting agencies and enterprise clients. This was a follow-up meeting to address open questions from a previous call, with Vivek and Mariana implementing Scrunch for client deliveries. The team needed hands-on guidance on site audit interpretation, LLM behavior (particularly around geographic and personalization biases), and how to set up reporting infrastructure for clients who expect month-over-month performance analysis—a capability that currently requires Looker Studio integration since the in-app dashboard has limited visualization and date-range options.

---

## Relevance

**To GrowthX Delivery:**
- Site audits are single-URL tools; multi-page strategy (target high-traffic pages from AI traffic tab) essential for effective optimization
- JavaScript-rendered content requires HTML replication to be indexed by LLMs other than Gemini; client websites must address this for full AI visibility
- Incognito mode depersonalization is fundamental to Scrunch's approach; custom parameters must be embedded in prompts, not relied on via user account settings

**To CheckThat:**
- Scrunch's incognito-mode approach directly influences how LLM behavior is tracked; geographic targeting is in-app, not user-account based
- State and metropolitan area geo-targeting coming in next few weeks will improve segmentation for US market research
- LLM version variation across providers (ChatGPT has country-specific versions; Claude does not) affects visibility benchmarking strategy

**To GrowthX Business Development:**
- Looker Studio reporting is enterprise/agency tier feature; suggests premium tier positioning for clients wanting month-over-month analysis
- Data export → spreadsheet → custom Looker pipeline is current workaround; client friction here indicates product gap and upsell opportunity
- Mariana's multi-client setup (Imbibit, Vallarta Adventures) demonstrates scalability; teams@growthxlabs.com shared account approach reduces admin friction

---

## Overview

- Site audits provide insights on SEO optimization for AI visibility, including robots.txt rules and JavaScript content accessibility
- Scrunch uses "incognito mode" for LLM queries to depersonalize results, with US as the default location (customizable)
- Month-over-month reporting capabilities are limited in-app, but Looker Studio integration offers more robust options
- Team is working on adding custom date ranges and improving data visualization (e.g., line charts instead of donuts)

---

## Key Topics

### Site Audit Functionality

  - Scrunch's chatbot checks specific criteria for AI visibility optimization
  - Recommendations include ensuring robots.txt allows key AI bots
  - Non-JavaScript versions should match JavaScript versions for LLM indexing
  - Only Gemini can read JavaScript; other LLMs require HTML replication
  - Audit focuses on single URLs; multiple key pages should be tested

### LLM Query Depersonalization

  - Scrunch uses "incognito mode" to submit generic, depersonalized prompts
  - Removes geographic biases unless specified in context settings
  - Default location is US; other countries can be selected in the context tab
  - Future update will allow state and major metropolitan area selection

### Reporting Capabilities

  - Current in-app options limited for month-over-month comparisons
  - New Looker Studio templates available for agencies and enterprise customers
  - Custom date ranges being added for more flexible reporting
  - Data export to spreadsheets currently required for detailed monthly analysis
  - Team working on updating visualization from donut to line charts

### Looker Integration

  - API documentation available for custom Looker integration
  - Team will create a shared user account (<teams@growthxlabs.com>) with necessary permissions
  - Support available for setting up API key and Looker connection

### Client Access Management

  - Process explained for adding new clients to Scrunch dashboard
  - Support team can assist in creating user accounts and assigning brand access

---

## Action Items

**Mara Leighton (GrowthX)**
- Review Looker Studio integration in Scrunch Help Center for month-over-month prompt performance reporting


**Vivek Shankar (GrowthX Labs)**
- Submit Slack request to Scrunch support to create Teams@growthxlabs.com user with all brand access and API key permissions for Looker integration


**Mariana Montezzana (GrowthX Labs)**
- Log out and back into Scrunch to access newly added brands (Imbibit, Vallarta Adventures) after account provision

- Attempt reconnecting analytics in Scrunch using Teams@growthxlabs.com account (after account is created by Scrunch support)

---

## Transcript
**Mara Leighton:** But what would be most helpful for you?

**Mara Leighton:** But I figure, know, Vivek, I know you have particular questions.

**Mara Leighton:** So I want to give you a chance to lead with those.

**Mara Leighton:** And then I have one particular question that maybe we can get to after.

**Mara Leighton:** And Mariana, if there's anything that pops up for you while you're listening, maybe we can do it that way.

**Mara Leighton:** But also, Andrew, this is your bread and butter.

**Mara Leighton:** So if you're like, I actually feel like something else would be better, I defer to you.

**Mara Leighton:** Okay.

**Mara Leighton:** Yeah, no, I just didn't.

**Mara Leighton:** It didn't feel like we got through everything last week.

**Andrew Sorensen:** So I was just anticipating we'd pick up where we were at, make sure we answered all questions.

**Andrew Sorensen:** So yeah, I defer to you guys, whatever makes the, you know, the best use of this time.

**Andrew Sorensen:** Cool.

**Andrew Sorensen:** All right.

**Mara Leighton:** Well, Vivek, not to just hand it over to you, but I know you have some questions.

**Mara Leighton:** Yeah.

**Mara Leighton:** Let me share my screen because it'll be a lot easier.

**Vivek Shankar:** Just a couple of questions.

**Vivek Shankar:** So one was the site audits, right?

**Vivek Shankar:** So I'm just using Galileo as an example.

**Vivek Shankar:** I ran it for Strapi as well.

**Vivek Shankar:** That's just a question.

**Vivek Shankar:** The, um, the language here.

**Vivek Shankar:** You know, for example, says the zero robots.txt has specific rules allowing all key AI bots.

**Vivek Shankar:** Is this a recommendation or is this an error?

**Andrew Sorensen:** No, it's not an error or a recommendation. Because what our chatbot is doing is our chatbot's hitting this URL and it's trying to confirm a certain criteria that are present to optimize for visibility.

**Andrew Sorensen:** What it's saying there is it couldn't 100% confirm that your robots.txt file has these specific rules to enable all bots to do this.

**Andrew Sorensen:** It could.

**Andrew Sorensen:** It very well could.

**Andrew Sorensen:** And for some of our customers, they go in, they check, they're like, yeah, we've got everything in there.

**Andrew Sorensen:** It's just surfacing and saying, hey, we couldn't determine with 100% certainty.

**Andrew Sorensen:** So it may be something you want to check to increase visibility.

**Andrew Sorensen:** Okay.

**Vivek Shankar:** Like similar vein, this question, this seemed a little more loaded.

**Vivek Shankar:** Like is a non-JS version substantially the same as a JS version?

**Vivek Shankar:** So I'm assuming you're testing.

**Vivek Shankar:** And you found that it's not, like they're substantially different.

**Vivek Shankar:** So this would be something that we need to address.

**Vivek Shankar:** Yeah.

**Andrew Sorensen:** And part of what that's calling out is most of the LLMs can't read JavaScript.

**Andrew Sorensen:** Gemini is the only exception.

**Andrew Sorensen:** So if you do have, what it's saying is we identify that there is JavaScript on there.

**Andrew Sorensen:** And so what we're calling out for you is if you do have a bunch of JavaScript, that content is not getting picked up, indexed by the LLMs.

**Andrew Sorensen:** And so if you have that, what we recommend, and there is a Help Center article that talks about all these things as well.

**Andrew Sorensen:** But if you have a lot of JavaScript, what we recommend is then replicate the content in HTML on the web page.

**Andrew Sorensen:** Don't change anything to your human-facing version, but just on the web page.

**Andrew Sorensen:** Replicate in HTML the content that's being created and being surfaced up through JavaScript so that that content is also flowing over when your site gets indexed.

**Andrew Sorensen:** Okay.

**Vivek Shankar:** When you say page over here, is it scanning every page of the website, or is it just a homepage?

**Andrew Sorensen:** No, it's just that webpage of that URL.

**Vivek Shankar:** Oh, okay, just the homepage.

**Andrew Sorensen:** Yeah, just that, exactly.

**Andrew Sorensen:** Yeah, so this is one where you would want to run this on multiple key sites.

**Andrew Sorensen:** The strategy that I recommend is if you're using our AI traffic tab, yeah, if you're using that, because that syncs up with your Google Analytics, they're kind of in the bottom right where it says your AI landing pages.

**Andrew Sorensen:** Wherever you're getting the most traffic, I always like to go optimize for that and say, okay, I want to make sure not only if we're getting a lot of traffic, I want to make sure we are surfacing up all the content that we want.

**Andrew Sorensen:** And then if there are key URLs on your page that you don't see, then you're like, no, we should be seeing more responses.

**Andrew Sorensen:** This is a core element of our offering, of our product, of our brand, whatever.

**Andrew Sorensen:** So if we're not seeing a lot of traffic there, then let's optimize for that, then I would run that through the site audit as well, just to make sure that it's got full visibility and it's being completely crawled and indexed.

**Andrew Sorensen:** Okay, cool.

**Andrew Sorensen:** Thank you so much.

**Vivek Shankar:** One last kind of technical question, I guess.

**Vivek Shankar:** So an apologies if I don't frame this correctly, no need screen sharing for this.

**Vivek Shankar:** So the LLMs customize responses, right, based on memory or whatever.

**Vivek Shankar:** How does Scrunch account for that when you're repeatedly pinging the LLMs?

**Vivek Shankar:** How do you basically de-anonymize the persona that's pinging the LLM?

**Andrew Sorensen:** And this is really technical, so I'm going to explain it in my layman's terms because I'm not super technical.

**Andrew Sorensen:** But the way I understand it is basically we submit, we submit the prompts through an incognito mode.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** For that purpose, then it is, you know, it's depersonalizing anything from anybody.

**Andrew Sorensen:** And it also, the one thing also is it's not geographic specific at that time.

**Andrew Sorensen:** So like if you have different geographic parameters that might be biasing or influencing the response as well.

**Andrew Sorensen:** So the incognito mode is what we use to make it as generic as possible.

**Andrew Sorensen:** And that's where from a prompt creation strategy, if you have certain parameters or, you know, certain specifications that you want to do, you want to include that in the prompt itself.

**Andrew Sorensen:** Whereas if you were using ChatGPT, for example, on your own, you you've got your own ChatGPT Pro, you're using it yourself.

**Andrew Sorensen:** It's going to learn over time.

**Andrew Sorensen:** So you'd want to include that as part of a prompt.

**Andrew Sorensen:** Well, what about the flip side of it?

**Vivek Shankar:** Like the reason I'm asking this question is because, you know, I know the Galileo team's going to ask this.

**Vivek Shankar:** Like this was literally the first.

**Vivek Shankar:** This question they asked us a few weeks back.

**Vivek Shankar:** I'm trying to understand how to answer this without sounding like an idiot.

**Vivek Shankar:** So if they come back to us and say, because they've asked us for the SEO side of things, if they come back and say, well, we only care about the US, right?

**Vivek Shankar:** Is it possible to customize it just to see, say, the user is from the US, and I want to see what American people in the US are seeing?

**Vivek Shankar:** Is that possible?

**Andrew Sorensen:** Yeah, ChatGPT has different versions by country, and our default, if you, can you pull up your screen share again?

**Andrew Sorensen:** I'll walk you through this, because that's a really good question.

**Andrew Sorensen:** I just want to call that out.

**Andrew Sorensen:** If you go to the context tab and click on that, you'll see here, there is an option there for primary location to select a country.

**Andrew Sorensen:** If nothing is selected, it defaults to the US.

**Andrew Sorensen:** If you select something there, then it will go to that version.

**Andrew Sorensen:** For example, ChatGPT, I don't, and we're looking into this right now, I don't think all of the other LLMs have that level of specificity.

**Andrew Sorensen:** I don't think Claude, for example, has a Claude France or a Claude UK or anything like that.

**Andrew Sorensen:** So primarily this is very helpful for ChatGPT, but yes, unless it is specified differently there, it defaults to just US, so it's only focusing on the US.

**Andrew Sorensen:** Okay, so basically the data we're seeing for ChatGPT right now is US essentially, because nothing is selected here.

**Andrew Sorensen:** Okay, correct.

**Vivek Shankar:** Okay, cool.

**Vivek Shankar:** That was all I have.

**Vivek Shankar:** Yeah, thank you so much.

**Andrew Sorensen:** And just one quick product enhancement coming here very soon is in addition to country, you will see state and then major metropolitan area coming soon.

**Andrew Sorensen:** So if they're interested in getting more specific into certain geographic areas in the US, that's coming here in the next few weeks.

**Andrew Sorensen:** All right.

**Andrew Sorensen:** Thank you so much.

**Vivek Shankar:** Yeah, you bet.

**Mara Leighton:** And then one other question that I had, if one of our clients wants to see like month over month performance on particular prompts, do you have a recommendation for how to report that to them in a way that's like really seamless?

**Andrew Sorensen:** Yes.

**Andrew Sorensen:** And it just, and let me make sure that it's working the way that it should be.

**Andrew Sorensen:** But if you go to, and let me pull up, let me pull up Galileo real quick.

**Andrew Sorensen:** If you give me two seconds and I can screen share as well.

**Andrew Sorensen:** And this is not, this is not perfect.

**Andrew Sorensen:** I'll just, I'll be super candid about this, but we're getting better with this.

**Andrew Sorensen:** The other thing too, Mara is we, let me pull this up and see this.

**Andrew Sorensen:** We just created an updated Looker Studio report just for agencies and our largest, most enterprise-tier priced customers. Let me share my screen and we'll look at this together to keep me honest here.

**Andrew Sorensen:** Okay, great.

**Andrew Sorensen:** We're looking at the right customer.

**Andrew Sorensen:** So I think it's down here.

**Andrew Sorensen:** Yes.

**Andrew Sorensen:** Do you see this here in the help center, this Looker Studio templates?

**Andrew Sorensen:** Please take a look at that because I think that that gets us better, closer to a more effective reporting structure than what we have in the app right now.

**Andrew Sorensen:** So please look at that.

**Andrew Sorensen:** That may help to this question as well.

**Andrew Sorensen:** But what we did do, just rolling it out, and I'm just going to go to the prompts tab.

**Andrew Sorensen:** Well, let's do dashboard just because it's high level.

**Andrew Sorensen:** On the dashboard, we did last week just roll out this ability to do four days, seven days, four weeks, 12 weeks.

**Andrew Sorensen:** My understanding, and let's look in this and see if this is right or not.

**Andrew Sorensen:** This should change the timeframe on here.

**Andrew Sorensen:** And I'm waiting for the competitive presence to show up because that's what we need to see.

**Andrew Sorensen:** Okay, so that's not doing exactly what I anticipated it would.

**Andrew Sorensen:** So the thing, I guess what you would do here, what we're rolling out, and it should be either today or tomorrow, is the ability to cut by timeframes, custom timeframes.

**Andrew Sorensen:** So like you could say, if we're looking at August, August 1 to August 30th, boom, July 1 to July 30th, boom.

**Andrew Sorensen:** And again, at this point, it would still be screenshots for that if you're just looking at the dashboard type of thing.

**Andrew Sorensen:** But you should be able to cut the data by specific dates so that you can then do the month over month that way.

**Andrew Sorensen:** I do think, again, please play with that Looker Studio, because that should be more of the month over month analysis in that studio as well.

**Mara Leighton:** Okay, yeah, because I think what we would be most interested in, or what clients might ask us about, is breaking it down into individual seed prompts or which ones are performing best. They would be looking for that level of granularity if we're talking about month-over-month reporting.

**Andrew Sorensen:** And one other thing too is we are going to be updating the reports, the way these things are reported in here.

**Andrew Sorensen:** We've gotten feedback that most of our clients would prefer a line chart as opposed to a donut chart. That's coming soon as well.

**Andrew Sorensen:** But for right now, this isn't really showing month-over-month. I think it's just capturing everything that's in there.

**Mara Leighton:** So it sounds like right now we'll look at the Looker integration and see what's available through there. Vivek, feel free to jump in if you have another idea.

**Vivek Shankar:** Yeah, regarding the month-on-month, the only solution I found was to export the data, then pop that spreadsheet into Looker, and group the months together. If you say 12 weeks, it lists all the days, so you can export and group by month.

**Andrew Sorensen:** Of course.

**Vivek Shankar:** Yeah, so we just group it by the month, and then you can do a bar chart or whatever.

**Andrew Sorensen:** Okay.

**Vivek Shankar:** Regarding the Looker, I have a question.

**Vivek Shankar:** So this is more of a workflow thing on our end.

**Vivek Shankar:** So we use a common ID, like Teams or whatever, to store all the Looker reports, right?

**Vivek Shankar:** And that's what has access to GSC, GA4, et cetera.

**Vivek Shankar:** That ID, I don't think exists in Scrunch, and I don't think it has the settings permissions enabled in Scrunch.

**Vivek Shankar:** And looking through the Looker instructions, I have a question for your team. We can generate the API key, but we want to integrate it with our existing Looker.

**Vivek Shankar:** We don't want to copy your Looker template.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So is it possible to send us instructions on how to do that?

**Vivek Shankar:** I tried playing around with it because Looker is really finicky. I tried putting in an API key in Looker to pull the data that way, but it doesn't let me do it.

**Vivek Shankar:** So yeah, just those two things.

**Vivek Shankar:** One, can we have a shared email mailbox like Teams that has access to generate the API key? And two, I'll read through the API documentation you'll send.

**Andrew Sorensen:** Hopefully that will help.

**Andrew Sorensen:** Let me check how we have things set up. I thought we had a generic inbox or shared user account already set up, but I don't recall what it was called.

**Vivek Shankar:** If it's set up as a user, that's great. But the main thing is Looker doesn't allow me to enter an API key and pull in the data.

**Vivek Shankar:** So I'm just wondering how to do that, you know, because Scrunch is not showing up as a sort of pre-selected connector in Looker.

**Vivek Shankar:** So it's like a custom thing.

**Vivek Shankar:** So I'm not sure how to do that customization in Looker.

**Vivek Shankar:** I was wondering if your team would have guidance on that.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So there's two here that I see that are generic.

**Andrew Sorensen:** We have tools at growthx.ai and tools at growthxlabs.com.

**Vivek Shankar:** I think it needs to be teams at growthxlabs.com.

**Vivek Shankar:** That's where we store all our Lookers and do the...

**Vivek Shankar:** Give me two seconds.

**Andrew Sorensen:** Just want to make sure that I don't see because you got a lot of users.

**Andrew Sorensen:** It's over there.

**Andrew Sorensen:** want to make sure that it's not, I don't see.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** So I don't see teams.

**Andrew Sorensen:** So I'm trying to think what's the easiest way to do this.

**Andrew Sorensen:** Can you, do you have access to our, our Slack channel?

**Vivek Shankar:** I don't know.

**Vivek Shankar:** I don't know if Mara does.

**Vivek Shankar:** I do.

**Andrew Sorensen:** Yeah, I do.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** So what I would ask, please drop a request in the Slack channel and Vivek, we can get you access to, but drop a request in the Slack channel to have that created as a user.

**Andrew Sorensen:** We'll create it as a user.

**Andrew Sorensen:** We'll also need to know what brands we're assigning to it.

**Andrew Sorensen:** If it's all the brands or if it's only specific brands or whatever, we'll make sure that we have that taken care of.

**Andrew Sorensen:** And then Vivek, if you're the one that's going to do this, I don't see right now that you have, that you're enabled to do all the integrations to create the API key.

**Andrew Sorensen:** So I can add that right now, make sure that if you're the one that's going to do it, I can.

**Andrew Sorensen:** Make sure you have the access to do so.

**Andrew Sorensen:** You'll see on your left-hand side of like Galileo when you log in, you'll see some additional tabs show up in the left-hand menu.

**Andrew Sorensen:** I don't need it.

**Vivek Shankar:** The Teams ID needs it.

**Andrew Sorensen:** We need do it for Teams.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** So then that's what we'll do.

**Andrew Sorensen:** The game plan will be, if you'll drop that into the Slack channel, I'll have my support team go in.

**Andrew Sorensen:** They'll create that as a user.

**Andrew Sorensen:** We just need to know which brands to, it sounds like we want to do it for all the brands.

**Andrew Sorensen:** Everyone, yeah.

**Andrew Sorensen:** Just say, you know, please, here's the user.

**Andrew Sorensen:** Please add this as a user and then assign all the brands to it.

**Andrew Sorensen:** And then we can also assign it the right permissions on the back end so that whoever has access to that can then go through, create the API key.

**Andrew Sorensen:** And with the API key and the documentation, you should be able to sync that up with Looker.

**Andrew Sorensen:** I've got a bunch of customers that do exactly that.

**Andrew Sorensen:** If not, I'm happy to get you on a call with our engineer to answer any questions and to make sure that we've got that integration all set up.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Cool.

**Vivek Shankar:** I'll, I'll, I'll, I'll, I'll, I'll, I'll,

**Vivek Shankar:** And I will coordinate that, I guess.

**Vivek Shankar:** I'll play around with Looker.

**Vivek Shankar:** It might be a couple, three weeks because I'm going on vacation for the next few weeks.

**Vivek Shankar:** No worries.

**Andrew Sorensen:** So, yeah, I'll get back to you on that.

**Vivek Shankar:** But thank you.

**Vivek Shankar:** Yeah, you betcha.

**Vivek Shankar:** Hopefully some more fun.

**Andrew Sorensen:** Yeah, it is, yeah.

**Andrew Sorensen:** Awesome.

**Mara Leighton:** Mariana, do you have any questions? I want to give you a chance as well.

**Mariana Montezzana:** I do have questions. I want to know if it's possible to set up Scrunch for my other two clients.

**Mariana Montezzana:** I have this set up for one, but I didn't find any options like add new projects.

**Mariana Montezzana:** And I'm not sure if these are for clients that have any services related or is it available for all clients.

**Mariana Montezzana:** Basically, I want to know if I can set this up for Immubit and the Adventures group as well.

**Mara Leighton:** For Scrunch, they should have dashboards. Is that what you mean?

**Mariana Montezzana:** I got an invitation link to access one space, but I got another invitation for Imbibit and when I click it says no access. I'm not sure if this client doesn't have the service or what I need to do to set it up.

**Andrew Sorensen:** Mariana, what's your work email?

**Mariana Montezzana:** mariana@growthxlabs.com

**Andrew Sorensen:** Okay, I see you have access to one dashboard only.

**Andrew Sorensen:** So give me two seconds here.

**Andrew Sorensen:** I just got to update some stuff on the back end here.

**Andrew Sorensen:** And then what were the other two brands that you mentioned?

**Mariana Montezzana:** ImmoBit and the Adventures Group.

**Mariana Montezzana:** But those are three different websites.

**Mariana Montezzana:** This client has three.

**Andrew Sorensen:** I don't see the Adventures Group.

**Mara Leighton:** It might be under Vallarta Adventures.

**Mara Leighton:** Vallarta Adventures is one, and Imbibit I shared access to. Let me check if the access is working now.

**Mara Leighton:** And then, yeah, Vallarta Adventures would be the other one, Andrew.

**Andrew Sorensen:** And I'm just confused.

**Andrew Sorensen:** Isn't that IMU?

**Andrew Sorensen:** Did I misspell that for Imbibit?

**Andrew Sorensen:** Isn't it IMU?

**Andrew Sorensen:** No, V-I-U-B-I-T.

**Mara Leighton:** That's what I thought it was.

**Mara Leighton:** Okay, two seconds.

**Andrew Sorensen:** Let me add that.

**Andrew Sorensen:** I don't know why that's such a thing.

**Andrew Sorensen:** There we go.

**Andrew Sorensen:** Okay, should have access to that now.

**Andrew Sorensen:** And then you said Vallarta Adventures, correct?

**Mariana Montezzana:** Yes, Vallarta Adventures.

**Andrew Sorensen:** Got it. Okay, Mariana, you should have access now.

**Andrew Sorensen:** You'll need to log out and back in. You should have access to all three now, and going forward you can create brands as needed.

**Mariana Montezzana:** How do I connect the AI traffic tab with analytics? The system says I need to be logged in with the account we use for analytics, which is a Teams account. But I'm logged in with my personal Mariana account.

**Andrew Sorensen:** You should be fine. Just log into GA4 and Scrunch in the same browser, and there should be a dropdown to select the brand you're running data on.

**Mariana Montezzana:** Okay, I'll try that.

**Vivek Shankar:** Actually, we'll need to log in using the Teams ID when Andrew sets it up to see all accounts.

**Mariana Montezzana:** So they're all under the Teams account?

**Andrew Sorensen:** Yes, everything is under Teams. There's not a separate GA4 instance for each individual brand.

**Vivek Shankar:** That's why we connected our Lookers to it as well. Got it.

**Andrew Sorensen:** Yeah, if you'll submit that over to support, I'm going to let my support guy know that that's coming just so we can turn that around.

**Andrew Sorensen:** I'll give Jaden a heads up so we can turn this around quickly. Thanks so much everyone.

**Mara Leighton:** Really appreciate it.

**Mara Leighton:** I feel like that's probably a good amount for today.

**Mara Leighton:** Anything else you'd like to ask? Otherwise we can wrap up and give everyone time back.

**Mariana Montezzana:** Thank you.

**Mariana Montezzana:** Thank you so much.

**Andrew Sorensen:** Have a great week. Thanks so much.

**Mara Leighton:** Bye-bye.

**Andrew Sorensen:** Bye.
