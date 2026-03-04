# Rapyd CMS Sync

<metadata>
date: 2025-04-10
time: 16:00 UTC
duration: 11 minutes
organizer: kirkland@growthx.ai
participants: Kirkland Gee, Mark Stiltner
fathom_recording_id: 56636735
fathom_url: https://fathom.video/calls/273449954
share_url: https://fathom.video/share/J-EfFZ2WDuJLRK-yseq4yi2v6t3U4szx
source: fathom
enriched_on: 2026-03-04 16:30 UTC
</metadata>

---

## Summary

Kirkland Gee and Mark Stiltner explored secure content upload solutions for Rapyd's WordPress site, which requires VPN and custom browser access configured by their Tel Aviv IT team. After evaluating a manual single-user browser setup, they pivoted to a preferred API-based solution where GrowthX can bulk upload articles via CSV or JSON format through an intermediary Rapyd API endpoint, enabling full automation with AirOps. Mark will investigate WordPress REST API, bulk import plugins, and Pantheon hosting capabilities to determine the best format for content transfer, with custom browser access remaining as a backup plan if API integration proves unfeasible.

---

## Context

Rapyd is a payments platform that uses a proprietary security setup for WordPress access, requiring VPN authentication and custom-configured browsers locked to specific machines. Kirkland Gee from GrowthX is working with Mark Stiltner to find a sustainable way to upload content to Rapyd's WordPress site without creating operational bottlenecks. GrowthX currently plans to handle content creation and delivery for Rapyd, and they need a scalable process that doesn't depend on a single team member having direct browser access. This conversation reflects Rapyd's enterprise-grade security posture and GrowthX's focus on automation-first delivery workflows.

---

## Relevance

**To GrowthX Delivery:**
- API-driven content delivery is a preferred approach over manual user access for client security and scalability
- Enterprise clients may have strict IT security requirements (VPN, custom browsers, Tel Aviv-based IT) that force creative technical solutions
- Automation via AirOps can significantly improve delivery efficiency for bulk content uploads across clients

**To GrowthX Business Development:**
- Rapyd represents a high-security, enterprise-class prospect with elevated operational requirements
- Expanding to other payments and fintech firms will likely encounter similar security constraints, creating a replicable pattern for future engagements
- GrowthX's ability to work within Rapyd's security constraints demonstrates consulting sophistication and increases account stability

**To CheckThat:**
- Not directly relevant to this call

---

## Overview

- Rapyd's WordPress site requires special security measures for access, initially proposing a custom browser setup
- An API-based solution for bulk content uploads emerged as a preferred alternative to individual access
- Both parties agreed to explore automated content transfer options to streamline the process and maintain security

---

## Key Topics

### Rapyd's Current CMS Access Protocol

  - Rapyd uses a proprietary browser system with VPN for WordPress access
  - IT team in Tel Aviv configures custom browsers on specific machines
  - Access is locked to the configured machine, not user accounts
  - Initial proposal: Set up growthx.ai team member (Ada) with this custom access

### Exploring Alternative Content Transfer Methods

  - Kirkland suggested using WordPress API or plugins for bulk uploads
  - Potential formats: JSON or CSV files containing article content and metadata
  - Mark to investigate WordPress REST API, plugins, or hosting provider (Pantheon) options
  - Goal: Create a streamlined process where growthx.ai can "click a button and send everything over"

### Technical Considerations for API Integration

  - Need to determine exact format and fields required for content transfer
  - Possibility of setting up a Rapyd-hosted API endpoint for growthx.ai to send content to
  - growthx.ai can potentially use AirOps to automate content sending to the API endpoint
  - Content would be imported as drafts for Rapyd team review

### Security and Access Management

  - Custom browser setup remains as a "Plan B" if API integration isn't feasible
  - API solution preferred to avoid adding new users to Rapyd's approved list
  - Reduces dependency on individual team member availability for content uploads

---

## Action Items

**Kirkland Gee (GrowthX)**
- Check with Yousa (GrowthX IT) regarding potential security implications of the proposed WordPress API access solution before implementation.

**Mark Stiltner (Rapyd)**
- Investigate WordPress API (REST API), bulk import plugins, and Pantheon hosting options for streamlined content upload capabilities.
- Provide GrowthX with a sample export of 5 blog posts containing all fields and metadata structure (including SEO fields and Yoast plugin data if applicable) to establish the required format for bulk uploads.

---

## Transcript

**Mark Stiltner:** There we are. Thanks for jumping on a day.

**Kirkland Gee:** Yeah, of course.

**Kirkland Gee:** Sorry.

**Mark Stiltner:** It took a week and a half to get a date sorted. I'm a little slow on Slack, but I talked to my IT team and what we'd have to do to get somebody set up is: we've got everything locked down, so they would set up their computer with a custom browser. I forget the name of it — it's not like Chrome or something. It's a proprietary browser system. They'd have that configured to access our WordPress site. So one person within the company's computer would basically have that access, though it could be more than one. But everybody who was going to access it would have to have their computer set up, and it's locked to the machine, not like an account.

**Kirkland Gee:** Right, so they set it up and put that browser on the machine and then that machine can access the website through that browser. I'm just trying to think through who that needs to be and the best way to go about that. So it's just on WordPress, but they have some sort of custom authentication that requires this.

**Mark Stiltner:** Exactly. So on our system, we use a custom VPN. For me to access WordPress through my system, I have to be logged in through that VPN. When they do it on a third party, they set it up with that VPN. You download a browser, and they have full control of that browser — they can turn it off, uninstall it, do whatever they want within it. Then they put the VPN access there, so you can log into the VPN and access the website via that browser.

**Kirkland Gee:** That's not too crazy. We just have to make sure we get the right people. I'm not going to be the person that needs that access.

**Mark Stiltner:** Yeah, it'll be Ada. I'm thinking it would be Ada. I'm not sure what her time zone is, but the whole IT team is in Tel Aviv. I'm mountain time, and I usually meet with them around 8 in the morning, which works well because that's 5 their time. Not sure if Ada is East Coast or West Coast — if she's East Coast, it'd be easier because they're later.

**Kirkland Gee:** I think she's actually in Bosnia.

**Mark Stiltner:** Oh, that's going to be really sweet.

**Kirkland Gee:** That's even closer than any of us are. So it should be not too crazy for her. Basically, she'll just need to get on a call with the IT team, sort this out, and then she can access it that way.

**Mark Stiltner:** Yeah, I've already put in a request. If it's going to be Ada, it'll be me, Ada, and the IT team. You might need to be on that call too — I'm not sure how your systems are configured.

**Kirkland Gee:** We're early on, so we don't have any security built into our machines — no Vanta, no remote management, none of that. But I want to check with Yousa, our IT guy who handles security, just to make sure there's nothing I'm missing. And yeah, I can hop on that call to be an extra set of eyes.

**Mark Stiltner:** Probably not a bad thing for you to get under your belt either.

**Kirkland Gee:** If you start onboarding other enterprise firms like payments companies with elevated security needs, you'll probably run into this pattern. I can't imagine that if there's all that level of security, there wouldn't be a way to do something through an API. Here's what I'm thinking out loud: what if we put the articles in a JSON format that's parsable? Could your team bulk upload through the API on the back end so we wouldn't have to manually do anything?

**Mark Stiltner:** That's a possibility. It might take a little more time. I'm a bit underwater right now, but I've got some freelance developers who might be able to do that.

**Kirkland Gee:** I'm just processing this out loud. If we're going to scale volume and keep things going consistently, we don't want to lock this down to one person on our team. If she goes out of office for a week, we have no way of uploading. So here's what I'm thinking: you tell us the format you need the content in — whether it's a CSV file, JSON file, whatever fields you need. Somebody on your side can connect to the WordPress API. I used to do this all the time on different CMSs. We just specify: we need the title, the body of the article, and whatever metadata. We prepare a file in that format, and you can run a script and upload everything super quickly. That's another route to explore.

**Mark Stiltner:** I can run that by my developers. That might work. So you're suggesting using the WordPress API — like the REST API?

**Kirkland Gee:** I don't know how authentication will work in that respect or if there are any blocks to using it. But there are also WordPress plugins that do bulk export and import. The key thing is: in as many cases as possible with a client, I want us to be able to click a button and send everything over. That's the goal.

**Mark Stiltner:** Yeah, this is definitely a better approach than trying to get one person set up with access.

**Mark Stiltner:** I can look for a plugin or check the REST API. Our hosting provider might have something too. We're hosted with Pantheon.

**Kirkland Gee:** Yeah, I used to work with Kinsta at ClickUp. You could directly work on the database in SQL, but it was a bit unreliable. There are plugins where you upload a CSV, map your columns to the blog post elements, and it just uploads them all. If we do the hard work of getting everything organized and set up a workflow, all we have to do is pass you the file. And it also means you don't have to add another person to your approved users list — that's management overhead you don't need.

**Mark Stiltner:** Yeah, that would make it easier. I'm going to talk to my team about this. We'd need to figure out whether it's a CSV or JSON file and what format.

**Kirkland Gee:** I haven't seen your WordPress, so I don't know what plugins you use or what metadata you need. Are there SEO title fields? That varies if you're using Yoast or not. The best approach is: whatever format you can export in — whether through the API or a plugin — just give us a copy of that export for maybe five blog posts. That way we know exactly what fields we need to fill in to send you the data.

**Mark Stiltner:** Yeah, I'll go back to my team on that. Ideally, what would be nice is if we could set it up so you export a JSON file and we give you a connector to an API we set up, so it runs in there as a draft for us to review.

**Kirkland Gee:** Exactly. We can send that to a Rapyd-hosted API that's connected to your WordPress on the back end. We can literally set up a workflow in AirOps to prepare articles and hit a button to send it to that endpoint. I don't think we could go directly to WordPress with their security model, but we can put something in place in between.

**Mark Stiltner:** Right.

**Mark Stiltner:** I like that approach. I'm going to go back to my team and see if we can set that up. It's definitely a better way to go. I'll let you know, and we'll keep the custom browser option as a plan B if this doesn't work out.

**Kirkland Gee:** It just seems like a potentially easier way for everybody if we get that initial setup done. Very cool. I'll keep you posted once I run this by Yousa.

**Mark Stiltner:** Sounds good.

**Kirkland Gee:** Reach out and ping me in that channel if you need any other questions.

**Mark Stiltner:** All right, thanks, Mark.

**Kirkland Gee:** Have a good one.
