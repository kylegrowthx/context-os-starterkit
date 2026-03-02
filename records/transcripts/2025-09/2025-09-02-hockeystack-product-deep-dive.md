# HockeyStack Product Deep Dive

<metadata>
date: 2025-09-02
time: 16:32 UTC
duration: 29 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien (GrowthX), Jackson Stevens (HockeyStack)
fathom_recording_id: 84383257
fathom_url: https://fathom.video/calls/398415709
share_url: https://fathom.video/share/5Wzr37T2z1pbAykUuiHk1sHoa-Fbdeqk
source: fathom
enriched_on: 2026-03-02 01:42 UTC
</metadata>

---

## Summary

Jackson Stevens from HockeyStack walked Erik O'Brien through the platform's two core products: Marketing Intelligence (attribution, custom reporting, Odin AI analyst) and Account Intelligence (sales enablement, scoring, Nova AI). The platform ingests data from CRMs, marketing automation tools, paid channels, and website pixels — then uses fingerprinting technology to track both known and anonymous users across the entire buyer journey. Implementation takes 3-4 days for initial dashboards and full deployment within 5 weeks, with dedicated CSM support.

---

## Context

Jackson Stevens is a product expert at HockeyStack, a go-to-market intelligence platform. Erik O'Brien is from GrowthX and was meeting with Jackson to develop a deep understanding of HockeyStack's platform capabilities and use cases that will inform content GrowthX creates for HockeyStack's marketing and sales leaders. GrowthX uses these product deep dives as input into their content creation workflows to create targeted assets and messaging that resonates with HockeyStack's ideal customer profiles (marketing teams, sales leaders, CMOs). The meeting was conversational by design, allowing Jackson to walk through feature sets while leaving room for Erik's questions about implementation, feature maturity, and customer adoption patterns.

---

## Relevance

**To GrowthX Delivery:**
- HockeyStack's core value prop (unified data ingestion + AI-powered insights for attribution) is directly relevant to content for marketing leaders and CMOs struggling with multi-touch attribution and channel ROI justification
- Odin (marketing AI analyst) and Nova (sales AI agent) are recent product launches (Odin rolled out November last year) — good timing for content around AI-powered decision support in go-to-market
- Implementation velocity (3-4 days to first dashboard, 5 weeks to full deployment) is a strong proof point for productized, self-serve motion — relevant to buyer pain around long implementation cycles
- HockeyStack's emphasis on lifting the black box of scoring (showing the "why" behind account scores) addresses a fundamental sales adoption blocker — content opportunity around transparency and trust in data

**To CheckThat:**
- HockeyStack's fingerprinting approach to anonymous user tracking (vs. cookies) could be relevant to AEO research — shows how pixel-based and account-level data is being used to segment B2B buyer journeys
- The platform ingests third-party signals (hiring, funding, news) and connects to call recording software for unstructured data extraction — relevant to how AI visibility tools are expanding beyond web data

**To GrowthX Business Development:**
- Marketing teams are HockeyStack's primary ICP; sales product is secondary — suggests that account expansion plays into the Account Intelligence product, but require marketing buy-in first
- HockeyStack co-founders are Amelia and Amir — establishing potential for referral or partnership conversations around content or visibility into fast-growing B2B SaaS stacks

---

## Overview

- HockeyStack solves the complexity of multi-touch attribution by unifying data ingestion from CRMs, marketing automation, paid channels, and website pixels to map the full B2B buyer journey
- Two core products sold separately or bundled: Marketing Intelligence (custom attribution modeling, Odin AI analyst for natural language questions, lift/incrementality reporting) and Account Intelligence (sales enablement, account scoring with transparency, intent signals, Nova AI for sales planning)
- Key technical differentiator is fingerprinting technology for anonymous user tracking (vs. cookies), enabling attribution credit to be given to top-of-funnel awareness touchpoints that traditional last-touch attribution misses
- AI analysts (Odin for marketing, Nova for sales) are recent (Odin launched Nov 2024) and designed to eliminate manual dashboard creation and data analysis; Odin answers business questions at a glance, Nova recommends next steps to break into accounts based on past deal patterns
- Implementation is fast: templated attribution dashboard live in 3-4 days; fully operational with custom dashboards and CSM support within 5 weeks
- Primary ICP is marketing teams (heavily skewed toward marketing leaders, CMOs, demand gen); sales product is secondary but powerful when accounts already have marketing intelligence in place

---

## Key Topics

### The B2B Attribution Problem

- Traditional last-touch and even basic multi-touch attribution misses credit for top-of-funnel awareness activities (brand ads, content, events) that influence deals
- Standard reporting shows ~80% of deals come from "direct" or "organic" because they only count the final touchpoint, ignoring the dozens of impressions and earlier touchpoints that set the stage
- B2B buyer journeys are complex: 4-5 people from one company research different pages/content, but only one converts as a form fill; HockeyStack captures all the anonymous activity from the other researchers

### Platform Data Ingestion & Architecture

- Connects to Salesforce/HubSpot (CRM), marketing automation (Pardot, Marketo, HubSpot), all major paid channels (LinkedIn, Google, Meta, Reddit, TikTok) via APIs, and website pixel tracking
- Tracks both known users (those in CRM) and anonymous users across the entire journey from first impression to deal close
- Uses fingerprinting (not cookies) to identify anonymous users by analyzing ~hundreds of device/location attributes and reverse IP lookup to match back to account level
- Builds AI-powered account context as the foundation for both Marketing Intelligence and Account Intelligence products
- Can ingest third-party signals (hiring, funding, news) and unstructured data from call recording software to enrich scoring

### Marketing Intelligence Product

- Templated attribution dashboard ships out-of-the-box within first week; customers just connect systems and define goals
- Custom report builder UI allows full data slicing by channel, campaign, creative, geography, segment, industry, time period
- Multiple attribution models available: last-touch, first-touch, linear, and predictive (uses incrementality testing to weight touchpoints based on actual impact)
- Lift/incrementality reporting shows true conversion impact per touchpoint — e.g., "customers who see Campaign X are 7.7x more likely to convert to deal created" — preventing wasted spend on high-frequency but low-impact campaigns
- Odin AI analyst (launched Nov 2024) answers natural language business questions: "Which channels deliver highest-quality leads?" or "Will LinkedIn retargeting improve conversion rates on paid search leads?" — eliminates manual dashboard creation and analysis
- Visualization options include bar charts, funnels, Sankey diagrams showing most common paths to conversion and average time between stages

### Account Intelligence Product

- Sales reps view account detail pages (natively in Salesforce iframe or HockeyStack interface) showing buyer journey, account score (0-100), scoring factors, and contact/stakeholder activity
- Account scores use LLMs and are fully transparent (shows "this account is hot because of: recent hiring + 5+ contact engagements + pricing page visit") — builds trust vs. competitor black boxes
- Account plans surface best next steps and sales touchpoints by analyzing past deals to identify what actually moved the needle (gift sending, specific email messaging)
- AI-generated personalized outreach suggestions and email/LinkedIn messaging to save reps research time
- Stakeholder mapping and enrichment (phone, email, job changes, promotions, hiring signals)
- Workflow automation backend: any signal triggers actions (new hire in ICP, pricing page visit, intent threshold reached) that can spawn contact discovery, qualification questions, outreach sequences, Salesforce routing, or LinkedIn audience syncing

### Implementation & Go-to-Market

- Fast time-to-value: templated attribution dashboard in 3-4 days (just system connections + goal definitions); full deployment with custom dashboards within 5 weeks
- Dedicated CSM guides setup and creates first custom dashboards
- Products sold separately (marketing + sales can buy independently) or bundled for discount
- Primary ICP: marketing teams and CMOs seeking attribution and proof of marketing ROI
- Sales side is secondary product, but powerful when marketing already uses the platform — unique angle because account scoring is based on marketing intelligence, not just intent data

---

## Action Items

**Jackson Stevens (HockeyStack)**
- Send custom deal room with resources and reference materials to Erik

---

## Transcript

**Jackson Stevens:** Yeah, so before I get started, I'm also curious: is the idea to develop an understanding of the platform's value and use cases for your other clients, or is it more to help drive content ideas for HockeyStack?

**Erik O'Brien:** Yeah, so we use it as input into our workflows to create content. This product deep dive helps us inform different artifacts that we create, which then flow into how we create content for you guys that targets your ICPs.

**Jackson Stevens:** Cool, okay. Yeah, that works for me. So in that case, I can definitely give you the high level and some of the most common use cases. But like you mentioned, let's keep it conversational. If any specific questions come up, I'm always happy to take a quick pause and dive into anything.

**Erik O'Brien:** Yeah, absolutely.

**Jackson Stevens:** Awesome. I'll share my screen here. So the biggest challenge we see in go-to-market today comes from the sheer volume of data ingestion over time. We're working with a lot of scale-ups and enterprise companies that are collecting tons of data from different sources. It gets increasingly hard to extract insights from that data. That's why teams need not only a way to collect the data, but also normalize it, categorize it, and map it onto a single buyer journey so you can understand what touchpoints are influencing down-funnel metrics like pipeline and revenue.

Because the B2B buyer journey is so complex, data ingestion becomes really prevalent when you're trying to make decisions about channels, campaigns, and strategies to focus on. We actually ran a report that shows it takes hundreds of impressions and dozens of touchpoints for a deal to close. With standard CRM reporting or traditional attribution modeling, teams see about 80% of deals coming from direct or organic. But that's only because they have a last-touch model that only accounts for the final touchpoint — it's not accounting for the other touchpoints, especially top-of-funnel brand awareness that impacted deal creation.

That's what HockeyStack enables: tracking every single touchpoint from the very first anonymous impression all the way through to closed-one. Other tools can show you what's working at a high level, but the problem is they can be inefficient. Every platform tracks data differently, so unless you get everything into one buyer journey timeline and line everything up, you won't extract insights because those touchpoints don't line up — especially with CRM modeling that requires contact-to-opportunity assignment. That's why we have Odin, our AI analyst, where you can ask any real-world business question: "We have $10,000 of marketing budget remaining this quarter. What should we focus on?" or "Which marketing channels are generating the highest-quality leads consistently?"

Odin eliminates the process of manually creating dashboards, defining KPIs, setting up attribution models, and analyzing data. Our philosophy is less about proving past ROI and more about using data to make decisions for future strategies to create future value.

**Erik O'Brien:** That makes sense.

**Jackson Stevens:** The way this works is we connect to any platform that tells the story of buyer journeys. Typically our customers use Salesforce or HubSpot for CRM, then Pardot, Marketo, or HubSpot for marketing automation. We connect natively with all major paid channels — LinkedIn, Google, Meta, Reddit, TikTok — through APIs. And we put a tracking pixel on their website. This lets us understand activity not only from converted users in their CRM but also from all anonymous users.

Typically when a company evaluates a software platform, 4 or 5 people from that company look at different content and web pages, but only one person fills out a form and converts. The rest avoid form fills like the plague to avoid email lists. That's where HockeyStack adds value — bringing in data points from that anonymous activity.

We also bring in third-party signals. We have AI agents that find hiring signals, funding rounds, news articles, job changes — all customizable. That feeds into our account intelligence side. What we do is create an AI account context on every account, which becomes the backbone for both products. On the marketing intelligence side, we have attribution with templated approaches and custom reports through our report builder UI. We also have lift and incrementality reporting as part of custom reporting, and Odin, our AI analyst, where you ask real-world business questions.

On the account intelligence side, we surface that same dataset to sales as intent signals and account scores so they can build priority lists. We can automate workflows to capitalize on that signal data at scale. We have another AI agent on that side called Nova, where leadership can ask questions like "How are my best reps performing? What are they doing differently than the rest of the team?" or specific questions about segments, regions, or accounts. That's about how we take data and craft a plan to break into a specific account.

**Erik O'Brien:** So would you say the account context is split between sales and marketing? You have both sides of the coin there for go-to-market?

**Jackson Stevens:** Yeah, absolutely. That comes down to both our products. Let me show you how we're ingesting data first, then how we use it for both sides. We're bringing everything at the account level — deal stage changes. We have a partnership API with LinkedIn, so we can bring in impression-level data, whether someone sees an ad or watches a video. We're tracking everything at the contact level too. So Dave at Lacuna Inc. is a converted user because we have his email and the time he submitted the form. We can see all his touchpoints leading up to that form and every touchpoint after — website visits, marketing automation, email, sales touches.

Then we're bringing in all anonymous activities. For every anonymous user, we assign a unique string of numbers and letters to distinguish them from the next user. But we're not relying on cookies for this anonymous tracking. We have a newer technology called fingerprinting where we look at hundreds of different attributes about a person — their device, location — then match that to a dataset for reverse IP lookup and match back to the account level. We can see all the website activity, where they came from, what page they looked at, how long they were there, what links they clicked.

With typical attribution, you only give credit to Google Paid, or maybe with multi-touch, a webinar. But it only looks at activity from Dave because he converted. It doesn't account for the website visit, the LinkedIn campaign that influenced that visit, or the Twitter ad. With our multi-touch modeling, we look at all those touchpoints and give credit where credit is due, then use that to decide what to focus on.

**Erik O'Brien:** Any questions on this view?

**Jackson Stevens:** I know a couple other technologies have a similar timeline view, but nothing quite as granular from my experience. Makes sense. Okay, so typically our customers don't spend too much time in this view — it's the building blocks for our reporting and attribution tool. The way customers action on this data at the aggregate level is through Odin, among other ways. With Odin, you can ask any real-world question and eliminate the time it takes to manually analyze reports and dashboards. This pulls data not only from reports and dashboards in your HockeyStack environment but every single touchpoint from every buyer journey across every account to give you the data you need.

In this example: "Which marketing channels deliver the highest-quality leads consistently?" Odin defines what it sees as a high-quality lead and breaks it out for you — sales qualified leads by channel, closed-one revenue by channel, bringing in CRM data, spend by channel directly from the channels themselves through API connections with LinkedIn. It shows ROI, averages, insights, and strategic actions. So in this example: "Shift 12% incremental budget to LinkedIn in Q3 to safeguard pipeline."

This is where most customers spend their time looking at data to make real-world business decisions. You can get super granular. A real scenario might be "Do paid search leads who don't convert become more likely to convert or close faster if I retarget them on LinkedIn?" Typically getting this answer is a huge process of creating cohorts, doing calculations, understanding performance differences. Odin answers that in seconds. It creates cohorts: paid search leads with LinkedIn retargeting and paid search leads without. Shows conversion rates, average days to close, and provides strategic insights. In this scenario, yes, LinkedIn retargeting improved outcomes — conversion rate nearly doubled and shorter sales cycle.

**Erik O'Brien:** Any questions on any of the AI stuff? Anything Odin-related? How long has Odin been a feature or product you've had around?

**Jackson Stevens:** Yeah, it's newer — less than a year. It rolled out officially in November.

**Erik O'Brien:** Is Odin more a decision support tool for the marketing side?

**Jackson Stevens:** Yes, absolutely. Odin is designed for marketing only — those marketing questions. But on the account intelligence side, we have another AI agent called Nova, where sales decisions get made.

**Erik O'Brien:** Who typically has access to this? Is it more leadership or broad-based? Is that up to the team?

**Jackson Stevens:** It's up to the team, but typically everyone in the marketing org. You can create custom dashboards broken out by strategy, so maybe someone focused on content marketing or just paid can have their own dashboard and make decisions from there.

**Jackson Stevens:** We also have a templated approach. Let me jump into custom reports in a second, but first I'll show you the attribution template dashboard. This is essentially out-of-the-box. During implementation, customers just connect their systems and define goals and properties, and you get all this data within the first week. We're breaking everything into channels and showing metrics around how those channels perform. All columns are based on what they define to track — deals created might be stage-one opportunities or whatever they call it internally.

We're looking at everything through a linear model right now, but we can change the attribution model. We have last-touch, first-touch, various multi-touch models. Customers like the predictive model, which does incrementality testing in the backend to assign different weighting to touchpoints based on past impact. If you drill into a specific channel like LinkedIn ads, it breaks out by campaign. These three campaigns roll up into LinkedIn ads. You can get more granular and see ad level within each campaign. You can look at deals too — for a campaign, see how many deals were created. Click into record details and it shows all deals created with that campaign as one touchpoint along the buyer journey. You can drill into every deal, see all touchpoints and different campaigns that impacted it, and all attribution credit given to each.

**Erik O'Brien:** For the predictive model, are you able to slice by company size or industry verticals? Can you get that granular?

**Jackson Stevens:** Yeah, absolutely. That would work in our custom reporting. Here you can change filters, look at specific regions or segments, break out the data and put the predictive model on that. You can change columns, even change the lookback period. The idea is to slice and dice data to answer any question. And this is unique to HockeyStack — the lookback period. Marketers want to understand campaign performance month-over-month, quarter-over-quarter. No other tool can do that. If you want a day-to-day source of truth on how segments or regions perform, that comes with custom reporting.

You can get answers on the attribution dashboard, then create a custom dashboard. In this example, it's our CMO overview. Everything here is fully editable and customizable. You can add columns within the product because we have a report builder UI. You can break it out however you want — in this example, high-level marketing channels and associated metrics. You can also add customer acquisition costs, how much inbound pipeline this quarter. We have all types of visualization: bar charts, reports, funnel views, Sankey views. Define your goal and see the most common paths to reach it, average time between stages, conversion rates, dropoff.

An important piece is incrementality or lift reporting. Attribution shows what touchpoints appear frequently, but doesn't calculate the impact those touchpoints have on conversion. This is cohort analysis. In this example, if an account interacts with this campaign at any point in their buyer journey, they're 7.7 times more likely to convert to deal-created. This other campaign has no lift. This helps avoid doubling down on a campaign because it shows up in attribution a lot but actually has no lift on conversion.

**Erik O'Brien:** Any questions on the custom reporting?

**Jackson Stevens:** No, pretty straightforward, just very detailed. Yeah. You can get granular — these are ad networks, but we also bring in campaign-level data: campaign groups, campaigns, and creatives or ad level. In this example, LinkedIn creatives, but could be Google AdWords. That brings me into account intelligence. I want to be conscious of time, so I'll move quickly. Essentially, this view is for reps. Reps can log into HockeyStack or this is an iframe in Salesforce so they get data wherever they're living.

For Abbott Laboratories, if they wanted to drill into that account, they'd get all this information about the account. They have that same buyer journey view that's the data foundation for marketing. But they also have an overview where we summarize the buyer journey through AI so they don't do manual analysis. They'll see what contacts are interacting with web pages, what ads, third-party signals. We give every account a score. Abbott Laboratories has a 77, based on first-party engagement and third-party signals.

What's nice about HockeyStack is we provide full transparency into these scores. We show scoring factors. We use LLMs for scoring to detect nuances like repeated downloads. The idea is that other tools are a black box on scoring, leading to lack of adoption by reps. Because reps have peace of mind — "this account is hot because they're doing this, this, and this" — they trust the data and action on it.

Then there's a recent hire in finance leadership. We get that from third-party signals or connecting with call recording software. We ingest unstructured data. If somebody mentions "We just hired somebody in finance, they haven't updated LinkedIn yet," we ingest that and use it to score the account.

From there, we identify ICP contacts, enrich with phone and email, and you can add them to CRM. Then we have the account plan. This is where reps spend a lot of time. With a target account list, they can understand the best way to break into an account. We do similar incrementality testing — look at past deals, understand what sales touchpoints impacted conversion, then recommend best next steps. Maybe a wine gift in a past deal moved the needle forward, so we recommend it here. We can craft email or LinkedIn messaging so reps can use it as-is or edit and send themselves. It's a good starting place.

We have a stakeholder map breaking out departments, bringing in data about who recently joined or left. This person left this company to HockeyStack in August 2025. Job changes, promotions, hiring signals. This is the drilled-in level where reps spend time on high-priority accounts.

We also have backend workflows to capitalize on signal data at scale. Anything can trigger a workflow — a pricing page visit, an intent threshold, hiring new ICP people. We can push accounts through contact discovery to identify titles fitting your ICP and enrich them, add them to CRM. We have AI nodes to bring in signal and qualification data. "Do they have a decision maker in my target department? Do they have typical funding for my ICP?" Then branch off. If it qualifies, put it in outreach sequence, route to a rep in Salesforce, or sync the audience to LinkedIn for retargeting. Possibilities are limitless. We want to orchestrate the backend to make sure reps have the right data at the right place and time. Rather than prospecting accounts not showing much intent, they can personalize outreach at scale. We create content within sales emails through workflows so reps send personalized messaging without all that research and focus on higher-priority accounts.

**Erik O'Brien:** Any questions on the account intelligence side?

**Jackson Stevens:** No, I don't think so. Okay. Was this helpful?

**Erik O'Brien:** Yeah, super helpful. I do have one question: how long does it take for a customer after signing to get from nothing to time-to-value? How long to integrate and set up for their first metrics view?

**Jackson Stevens:** The templated attribution dashboard should be available in the first 3-4 days. All you need is to connect systems and define goals, properties, and definitions. You'll have a dedicated CSM to help through that process. We'll create the first few custom dashboards. That comes within the next couple of weeks. The idea is they should be fully up and running without anything left within 5 weeks.

**Erik O'Brien:** And on the customer side, you guys have quite a few across marketing, sales, CRO, all go-to-market titles. Have you seen trends? Is it more marketing teams looking for attribution plus account or marketing intelligence suite? Or more sales leaders looking to round out with account intelligence? Or mix?

**Jackson Stevens:** Heavily skewed towards marketing. Marketing is definitely our biggest ICP. We're known as an attribution product. We do more than that, but most inbound is marketing trying to get visibility into what's working and not, then using that to make decisions. Sales is more a secondary product.

**Erik O'Brien:** I know Amelia and Amir wanted to get away from being known for attribution only.

**Jackson Stevens:** It seems like the bread and butter at least has been. It's helpful to understand marketing is always looking for ways to prove their value. Yeah, definitely. It's interesting because on the sales side, there are so many other tools doing similar things. Our unique position is because we have attribution and data foundation, know what works and doesn't, we use that to score accounts more accurately based on clients' specific marketing functions.

**Erik O'Brien:** Yeah, absolutely. My first job was in inside sales. I wish we had anything close to this.

**Jackson Stevens:** Yeah. I was an SDR for a couple years too and could have benefited from this for sure. So I know we're getting close to time.

**Erik O'Brien:** One last question: if marketing is the big ICP, are there stoppers if a sales organization doesn't want to adopt? Or if marketing wants to run with it, they foot the bill?

**Jackson Stevens:** The two products are sold separately. Marketing intelligence is sold separately from account intelligence.

**Erik O'Brien:** That's helpful.

**Jackson Stevens:** Or you can bundle them for a bit of a discount on both.

**Erik O'Brien:** Okay, anything else I should know before we hang up? I think there's a very detailed walkthrough, so we got pretty much everything.

**Jackson Stevens:** Yeah, we definitely got through the big pieces. There's a couple other nuances, but high level we covered the important ones. I can send over a custom deal room with resources you can refer to between conversations. If other questions come up, I'm always happy to help via email, Slack, or whatever.

**Erik O'Brien:** Yeah, wonderful. Thanks man.

**Jackson Stevens:** Sounds great. Well, I appreciate your time, Erik. I'll follow up with that information.

**Erik O'Brien:** Yeah, looking forward to staying connected.

**Jackson Stevens:** Absolutely. Appreciate it, Jackson.

**Erik O'Brien:** Have a good one.

**Jackson Stevens:** You too. Bye.
