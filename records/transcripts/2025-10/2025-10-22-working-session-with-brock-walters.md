# Working Session with Brock Walters

<metadata>
date: 2025-10-22
time: 20:02 UTC
duration: 60 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Brock Walters
fathom_recording_id: 96110995
fathom_url: https://fathom.video/calls/448277080
share_url: https://fathom.video/share/cGJgvz9pYgxG8YbGNxbrhqDGw4_poPob
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

Erik O'Brien conducted a deep technical walkthrough of the Fleet device management platform with Brock Walters, focusing on core differentiators and positioning. Key themes included Fleet's cross-platform "flattening" approach (unified management across Mac, Windows, and Linux via a single checkbox UI), the power of OS Query for SQL-based device data collection, GitOps configuration management, and the importance of transparent, jargon-free brand messaging for technical audiences. The session established that Fleet's open-source transparency is a critical competitive advantage—particularly for Linux users and developers who are inherently resistant to closed-source management solutions.

---

## Context

This was a knowledge-transfer session where Erik O'Brien (GrowthX) met with Brock Walters, Manager of Training & Enablement at Fleet, to deepen his understanding of Fleet's product and positioning. Brock conducted a live product walkthrough similar to what Fleet's sales team presents to new customers, using a basic left-to-right tab flow suitable for customers new to device management. Erik came prepared having watched two product videos (one from Brock and an earlier ~18-minute demo from Mike), so the session could jump past basic introductions and focus on deeper product philosophy, technical architecture, and messaging strategy. The meeting's output—a summary document that will inform GrowthX's internal artifacts and content strategy—indicates this is part of GrowthX's broader engagement to help Fleet refine and communicate its positioning.

---

## Relevance

- **To GrowthX Delivery:** Deep understanding of Fleet's product philosophy, technical differentiators (cross-platform flattening, OS Query, GitOps, webhooks), and customer personas (developer-heavy teams, Linux users, compliance-driven organizations). Erik now has foundation to consult on content strategy, messaging architecture, and positioning narratives—particularly the "open device management" story that resonates with privacy-conscious and developer audiences.

- **To Content & Brand Voice:** Clear directive from product leadership that messaging must be transparent, precise, and jargon-free. Every technical term must be explained even for a technical audience. This establishes guardrails for content creation and differentiates Fleet from competitors who use buzzwords like "POC" or "synergy" without definition—an important positioning advantage.

- **To GrowthX Business Development:** This engagement demonstrates deep, collaborative work on product positioning and customer education materials. Brock's willingness to spend an hour on a detailed walkthrough and his openness to feedback on messaging suggests strong partnership potential and room for expanded scope (product marketing, customer education, case studies).

---

## Overview

- **Core Differentiators:** Fleet's key strengths are its cross-platform "flattening" (e.g., one checkbox enables disk encryption on Mac, Windows, & Linux), powerful OS Query data collection, and GitOps for version-controlled configuration.
- **Extensibility:** The platform is designed for extensibility, using generic webhooks for automation (e.g., policy failures → Jira tickets) and allowing use alongside other MDMs for data collection.
- **"Open Device Management":** The open-source core builds trust, especially with developer-heavy teams and Linux users who are often resistant to management.
- **Content Strategy:** The brand voice must be clear and truthful, avoiding jargon and buzzwords. Every technical term must be explained to maintain credibility with a technical audience.

---

## Key Topics

### Product Philosophy & Differentiators

  - **Cross-Platform "Flattening":** A core goal is to simplify management across platforms.
      - **Example:** A single checkbox enables disk encryption on Mac, Windows, and Linux, abstracting away the underlying technical differences.
  - **Extensibility Over Prescriptive Features:** The platform uses generic tools (e.g., webhooks) to trigger workflows in other systems (e.g., Tynes, Jira), providing more power than competitors' built-in features.
  - **"Open Device Management":** The open-source core builds trust by allowing users to inspect the code.
      - **Use Case:** This is critical for managing developer-heavy teams and Linux users, who are often resistant to management.

### Core Technology: OS Query

  - **Function:** OS Query (from Facebook) expresses all device data as SQLite tables.
  - **Agent:** The `fleetd` agent includes two components:
    1.  **OS Query Agent:** Collects device data.
    2.  **Orbit:** The main Fleet agent, equivalent to the Jamf or Kanji binary.
  - **Benefit:** This architecture allows admins to query any device data using standard SQL, providing a powerful, flexible data collection engine.

### Core Workflow: Policies & Automation

  - **Policies:** Use OS Query to assess a device's state (e.g., "is the Brave browser installed?") and return a simple true/false (Boolean) result.
  - **Automation Trigger:** A policy *failure* is the trigger for all automation.
  - **Automation Types:**
      - **Auto-Remediation:** On failure, Fleet can automatically:
          - Send a generic webhook.
          - Create a ticket (Jira, Zendesk).
          - Run a script to fix the issue.
          - Install required software.
      - **Self-Remediation:** The end-user desktop app notifies the user of the failure and provides instructions to fix it themselves.

### GitOps: Configuration as Code

  - **Function:** All Fleet configurations (policies, controls, software) can be managed as YAML files in a version-controlled Git repository.
  - **Why it's powerful:**
      - **Version Control:** Enables easy rollbacks to previous, stable configurations.
      - **Peer Review:** Changes are managed via pull requests, improving stability and collaboration.
      - **Read-Only UI:** Admins can enable a "GitOps mode" that makes the UI read-only, forcing all changes through code.

### Platform Structure: Teams

  - **Purpose:** Teams are the primary organizational unit for grouping devices that require the same management controls.
  - **Cross-Platform:** A single team can contain devices from multiple OS platforms (Mac, Windows, Linux).
  - **Enrollment:**
      - **`fleetctl`:** A CLI tool for admins to build platform-specific enrollment packages (e.g., PKG for Mac, MSI for Windows).
      - **`no team` (Team ID 0):** A default staging area for devices enrolled without a specific team. Automation can then move them to the correct team.

### Content & Brand Voice

  - **Principle:** The brand voice must be clear, precise, and truthful, avoiding jargon and buzzwords.
  - **Rule:** Every technical term must be explained.
      - **Example:** "JSON" is acceptable; "POC" (Proof of Concept) is not, as it's an unexplained business buzzword.
  - **Rationale:** This approach builds credibility with a technical audience and avoids the "fluff" common in AI-generated marketing content.

---

## Action Items

**Brock Walters (Fleet)**
- Fix Dogfood instance banner

**Erik O'Brien (GrowthX)**
- Draft summary of this session and update internal Fleet artifacts
- Revise content drafts between now and Friday
- Meet with Brock on Friday to review company context and revised artifacts

---

## Transcript
**Erik O'Brien:** Hello.

**Erik O'Brien:** Hey, again.

**Brock Walters:** Your growthx note taker is AI, I'm assuming.

**Brock Walters:** It's AI everything with you guys.

**Brock Walters:** It's the best.

**Erik O'Brien:** It's everywhere.

**Brock Walters:** Everywhere.

**Erik O'Brien:** We've got it to only one per meeting now because prior to a couple weeks ago, would be like three or four of them would be in the meeting.

**Erik O'Brien:** There'd be more note takers than people.

**Brock Walters:** What's really funny, I've seen meetings like that.

**Brock Walters:** What's really funny with us is that we have AI, but there's not a thing showing in the meeting like this sometimes.

**Brock Walters:** And so there'll be an AI summary of the meeting afterwards, and it will say, Rachel sneezed.

**Brock Walters:** And then it'll be her talking about her cold.

**Brock Walters:** It's just so funny.

**Brock Walters:** There's no distinction between the casual small talk up front and the actual substance of the meeting, if there is any.

**Erik O'Brien:** All right.

**Erik O'Brien:** I figured somebody's going to get that figured out sooner or later.

**Brock Walters:** You know, maybe.

**Brock Walters:** Maybe someday.

**Brock Walters:** They'll have context, and then that's when they'll all start killing us, probably.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** For real taking our jobs.

**Erik O'Brien:** Yes.

**Erik O'Brien:** Instead of just taking notes.

**Brock Walters:** Yeah.

**Brock Walters:** All right, so what would you like to do in this session?

**Erik O'Brien:** So this session is specifically about more kind of digging deeper on the product.

**Brock Walters:** Oh, you want me to do a demo?

**Brock Walters:** If you have one that you could do, that'd be an I mean, so what I'm going to do is do something very basic, just kind of a left to right tab that I would, you know, left to right across the tabs that I would do for a customer that had never seen the product.

**Brock Walters:** I can dig in a little bit to the material that I would do in something like that we call an MDM 101 or an OS Query 101.

**Brock Walters:** We have plenty of time.

**Brock Walters:** So I think what I can do is maybe just do this very basic walkthrough and then kind of dig into maybe some of the MDM topics.

**Brock Walters:** And that's Right.

**Brock Walters:** OS Query topics.

**Erik O'Brien:** How's that sound?

**Erik O'Brien:** Sounds perfect.

**Brock Walters:** Okay, cool.

**Brock Walters:** So, and have you looked at it at all?

**Brock Walters:** Or should I just be starting at the beginning?

**Brock Walters:** And by the way, let me, before I do this, I'm going to open a new window because I have so many tabs open, it's really dumb.

**Erik O'Brien:** So I watched the video you sent over and then I watched the video that Mike had put together like almost a year ago.

**Erik O'Brien:** Oh, the pink t-shirt video?

**Brock Walters:** I think that's it, yeah.

**Erik O'Brien:** It's like spending, it's about 18 minutes of him walking through the platform.

**Brock Walters:** So I've familiarized myself, but I think we can start with as if I know nothing.

**Brock Walters:** Okay, cool.

**Brock Walters:** And, um, can you see my screen?

**Brock Walters:** Yep.

**Brock Walters:** What did you think of the three-minute video?

**Brock Walters:** Did it make sense to you?

**Brock Walters:** Did it, was there anything in there that left you scratching your head?

**Erik O'Brien:** Uh, wouldn't say head scratching.

**Erik O'Brien:** I would say it's, it's a great kind of intro to, like, what is...

**Erik O'Brien:** What Fleet?

**Erik O'Brien:** And what is MDM?

**Erik O'Brien:** How does it help?

**Erik O'Brien:** We used one of your competitors, Kanji, or now they're Uri.

**Brock Walters:** Now they're, no, it's Eru.

**Brock Walters:** Eru.

**Brock Walters:** Eru, yes.

**Erik O'Brien:** Yeah, so another really easy to say name, but at least I'm familiar kind of with the space and the purpose of it.

**Brock Walters:** So I know some people that work there.

**Brock Walters:** I used to work at Jamf, and one of the guys that I, I used to do, teach certification classes for Jamf, and one of the guys who now works at Kanji in the product org is someone that I used to have in my classes.

**Brock Walters:** And so, you know, I know him, actually, in fact, a couple people.

**Brock Walters:** So I know those guys, and I can't wait to see him next time.

**Brock Walters:** Or I just like, you went from one unpronounceable name to another, but, but apparently this is like a single thing.

**Brock Walters:** Like it's some kind of squid.

**Erik O'Brien:** I saw the little mascot they have.

**Brock Walters:** Yeah.

**Brock Walters:** Yeah.

**Brock Walters:** So maybe this has been the plan all along.

**Brock Walters:** I don't know.

**Brock Walters:** Cool.

**Brock Walters:** Okay.

**Brock Walters:** So, Fleet is organized, you know, the same way many web apps are organized.

**Brock Walters:** There's kind of top-level controls here, these tabs at the top.

**Brock Walters:** And I'm just going to run through those.

**Brock Walters:** But first, I'm going to talk about the features that we see here on this dashboard.

**Brock Walters:** So you can see that right up front, Fleet is a fully cross-platform solution.

**Brock Walters:** This is showing all the different device platforms we have in our product.

**Brock Walters:** And by the way, this is our internal instance of Fleet.

**Brock Walters:** This is not a demo instance.

**Brock Walters:** This is the instance.

**Erik O'Brien:** I figured with dogfood.

**Erik O'Brien:** Yes.

**Brock Walters:** Exactly.

**Brock Walters:** This is actually the instance that we use internally to manage devices.

**Brock Walters:** So, if you click on these.

**Brock Walters:** Oh, that's fun.

**Brock Walters:** I wonder if we're updating.

**Brock Walters:** What a bad time for that.

**Erik O'Brien:** That's another AWS outage.

**Brock Walters:** I hope that's not it.

**Brock Walters:** That's a tragic time for that, if this is the case.

**Brock Walters:** Well, what does it mean?

**Brock Walters:** I wonder if I have another instance I can get to.

**Brock Walters:** Stand by.

**Brock Walters:** Also, I'm having a problem with my password, so I don't know if that's going to work either.

**Brock Walters:** Let's see if I can, if have this bookmark somewhere.

**Brock Walters:** Okay, well, I have no idea what was going on there, and I can fix that banner later.

**Brock Walters:** The other thing that stinks about this is that this version I haven't updated yet, so this is on the old view.

**Brock Walters:** What we were seeing in Dogfood is the new view, which is very subtly different.

**Brock Walters:** They're probably updating it, which is just a very bad timing for me.

**Brock Walters:** And usually what happens is they send a message out and help engineering that they're doing that, but I'm not going to worry about it too much.

**Brock Walters:** So, dashboard, this is showing, now obviously I don't have as many devices as I have in the real instance, but this is...

**Brock Walters:** It has some phony data in it.

**Brock Walters:** And one of the things you see here on the dashboard is software.

**Brock Walters:** Now, one thing to understand about Fleet, and this is true of pretty much every MDM platform, is that all the devices that are managed report back their software inventory.

**Brock Walters:** So what we're really seeing here is all the software that's installed on all of the devices.

**Brock Walters:** But we also have a vulnerability management capability in Fleet.

**Brock Walters:** So you can see which of the software titles that have been reported back to inventory are vulnerable.

**Brock Walters:** And you can see here there's some version of Python that's vulnerable.

**Brock Walters:** There's some version of Safari that's showing it's vulnerable.

**Brock Walters:** So that's kind of cool that the vulnerability data is really very much up front in the product.

**Brock Walters:** And one thing that's interesting about Fleet in comparison to Kanji.

**Brock Walters:** It some very sophisticated vulnerability management features now, but one thing that's interesting about Fleet is that you can use it alongside another MDM if you want to, which is part of the reason for the confusion around the product, actually, that Fleet maybe isn't an MDM, because before Fleet had MDM features, like, we have lots of customers that use Jamf or lots of customers that use other MDMs, and they simply use Fleet for data collection.

**Brock Walters:** Because OS Query is so powerful.

**Brock Walters:** So, you might see an instance of Fleet that has MDM features enabled, or you might see one that doesn't.

**Brock Walters:** That's a perfectly normal thing.

**Brock Walters:** You're still going to see vulnerability data for software, because even if your devices aren't being managed by Fleet, there's still a Fleet agent that's installed that's collecting the inventory data.

**Brock Walters:** Hopefully that makes sense.

**Brock Walters:** That The other thing you see here on the dashboard is this activity feed.

**Brock Walters:** And this is actually pretty cool.

**Brock Walters:** Lots of web apps have something like this, Jira, if you've ever seen that, Confluence, lots of tools, kind of give you an up-to-the-minute status of what's happening in the platform.

**Brock Walters:** Here, this shows events like devices that have been enrolled, scripts that have been run, when a GitOps push has been done, when someone logged in.

**Brock Walters:** In the background, this is actually referred to as the audit log.

**Brock Walters:** So this is all of the events and activities that are being audited in terms of access and actions.

**Brock Walters:** And what's pretty cool about this is that this activity feed emits webhooks.

**Brock Walters:** And this is something that you see throughout the product.

**Brock Walters:** This is just one place that you see it.

**Brock Walters:** So what this means is...

**Brock Walters:** If I configure this webhook listener for, and it can be anything, it can be a generic webhook listener, it could be something like OctaWorkflows or Tynes, some sort of integration.

**Brock Walters:** If you've got something that's configured to listen for a webhook, like Tynes or like OctaWorkflows or some other no-code, low-code platform, or it could be anything, it could be a full-on different web application.

**Brock Walters:** What that means is that these webhooks can trigger events in those other systems.

**Brock Walters:** So you can get a workflow like on an enrollment, do something else in Tynes to talk to some two-factor authentication solution like Duo, or talk to the HR system, or send a message in Slack that a new computer was enrolled to the IT team.

**Brock Walters:** It's a very, very powerful system because, and it's not because other solutions don't have features like this, it's because it's generic. All it's doing is sending a webhook, and that you can use that webhook however you need to, rather than being restricted into a feature for how that action might be used.

**Brock Walters:** And a lot of other platforms are way more prescriptive about that kind of thing, and hopefully you'll see this as a theme throughout the product, that one of the things that our customers like about the product is this kind of generic extensibility.

**Brock Walters:** For the more sophisticated the client platform engineering team is, or the security team is, the more interesting these features become to them.

**Brock Walters:** For customers that aren't as sophisticated, those features might seem like barriers, but for people that know what to do with these things, it would be the difference between maybe your, and this is not meant to insult Kanji, but it's like the Duplo Legos versus the actual Legos versus the Masterworks Legos, right?

**Brock Walters:** It's a very, very apt analogy.

**Brock Walters:** Everybody knows what to do with the Duplo Legos.

**Brock Walters:** Those are for three-year-olds.

**Brock Walters:** Not everybody knows what to do with the Erector Set.

**Brock Walters:** But if you know what to do with the Erector Set, you can do some incredible stuff.

**Brock Walters:** So that's an analogy I like to use.

**Brock Walters:** Okay.

**Brock Walters:** In Fleet, we have this concept of teams.

**Brock Walters:** This is kind of the top-level organizational unit.

**Brock Walters:** You can think of a team really however you like.

**Brock Walters:** Now, I don't know that I can show you this very well here.

**Brock Walters:** Yeah.

**Brock Walters:** Okay.

**Brock Walters:** So there's two Windows computers and a Mac.

**Brock Walters:** And that's important.

**Brock Walters:** And this goes back to what I was saying on the last call with...

**Brock Walters:** Ada.

**Brock Walters:** With Ada.

**Brock Walters:** Sorry.

**Brock Walters:** Is that how you pronounce it?

**Brock Walters:** Ada?

**Brock Walters:** How you do?

**Erik O'Brien:** That's the American way to say it, yeah.

**Brock Walters:** Is it AIDA?

**Erik O'Brien:** Yep.

**Brock Walters:** Okay.

**Brock Walters:** So the idea here is that you have multiple platforms in the team.

**Brock Walters:** Well, why would you do that?

**Brock Walters:** Because we believe that if you're simplifying things, there should be kind of a flatness across all of your platforms.

**Brock Walters:** Theoretically, you should be able to manage your Windows computers the same way you manage your Macs.

**Brock Walters:** Now, this isn't always true, but that's the theory.

**Brock Walters:** So, and I'll talk more about that when I get to the control section.

**Brock Walters:** But the idea here is that your teams can have, there's no reason to segregate your Windows devices from your Macs in separate teams unless you want to do that.

**Brock Walters:** But the idea of a team is really more like, it's something that could function as a baseline.

**Brock Walters:** So, all of the devices that you want to have the same set of

**Brock Walters:** controls, you would have those in a single team.

**Brock Walters:** And that might be your accounting department, or that might be your software development department, right?

**Brock Walters:** But the thing about your accounting department is that those people all might have Windows computers.

**Brock Walters:** So you might end up, if you're breaking up your teams that way, that you would have a single platform in the team.

**Brock Walters:** It doesn't matter.

**Brock Walters:** The point is that a team should be a group of devices that you want managed to the same way.

**Brock Walters:** You can easily transfer a device from team to team.

**Brock Walters:** It's super easy to do.

**Brock Walters:** This is also where you can add hosts.

**Brock Walters:** And this is going to seem a little confusing, but because what you're getting is a giant command here, where do you run that command?

**Brock Walters:** So, a little bit, I think it's a little bit unusual for products like this.

**Brock Walters:** Fleet has a...

**Brock Walters:** So on binary for managing the console, and a lot of people are confused by this because what they see here is that, oh, this is the way you add hosts.

**Brock Walters:** This must mean I need this on every one of my hosts.

**Brock Walters:** In fact, what this is telling you to do is install a binary on your computer as the admin so that you can build packages for your hosts.

**Brock Walters:** So Fleet CTL is a command line tool that lets you do a lot of really cool things for managing the console.

**Brock Walters:** It's not something that gets enrolled on every host.

**Brock Walters:** It's something that gets enrolled only or only gets installed, sorry, on an admin's computer for doing management things.

**Brock Walters:** And one of the things you can do is build an enrollment package.

**Brock Walters:** And you can see you can build the enrollment package for Windows or Linux or Chrome or iPad or Android or what have you.

**Brock Walters:** Every team has a unique enrollment secret that in calling it a secret sounds scary.

**Brock Walters:** This is really just

**Brock Walters:** Kind of a unique identifier for the team.

**Brock Walters:** That's how the database keeps track of the separate teams in the background.

**Brock Walters:** And the output of this command when you have Fleet CTL installed on your computer is just a normal Apple PKG like any other.

**Brock Walters:** For Windows, you would be getting an MSI, which is kind of the equivalent of a PKG on Mac.

**Brock Walters:** For Linux, you can specify that you want a Debian package or an RPM package.

**Brock Walters:** So this builds the type of installer package that is typical for the platform.

**Brock Walters:** Gotcha.

**Brock Walters:** Cool.

**Brock Walters:** So if I go to controls now, what you'll see is that if I switch through these teams, the controls would be different for every team.

**Brock Walters:** And this is what I'm talking about when I'm saying that you want a team.

**Brock Walters:** The paradigm for a team is that it's a group of devices that you want to manage together. Because each team has its own set of controls, and each team has its own software, and each team has its own queries, and each team has its own policies.

**Brock Walters:** And we'll talk about what these things are, okay?

**Brock Walters:** There's one other thing to say about teams.

**Brock Walters:** We have this idea of no team.

**Brock Walters:** And this is also a little confusing.

**Brock Walters:** But no team means that you enrolled a device in Fleet and didn't specify a team for it to be in.

**Brock Walters:** In other words, if I made an enrollment package here, if I went to hosts, and I say, I want to add hosts for the best team, this command is going to create an enrollment package with this enrollment secret.

**Brock Walters:** But there is a global enrollment secret.

**Brock Walters:** So if a device gets enrolled, and there are a number of ways this can happen, like, for example, let's say you just installed, you had MDM enabled, and you just installed an enrollment profile on a device.

**Brock Walters:** After the device got enrolled in Fleet, it would then...

**Brock Walters:** And get a package to install the fleet agent.

**Brock Walters:** That package would not have a specific team associated with it.

**Brock Walters:** So it would get enrolled using the global enrollment secret into no team.

**Brock Walters:** Now, strangely, no team is actually a team.

**Brock Walters:** It's a team with team ID zero.

**Brock Walters:** All the other teams have some other ID in the database.

**Brock Walters:** No team just means it's used the global enrollment secret, and it doesn't really have a team association.

**Brock Walters:** But if I go into a device, and this is what the device record looks like.

**Brock Walters:** So it shows the device details, the software that's installed on the device, the queries for this device, and the policies that are associated to it.

**Brock Walters:** There's a number of actions that I can perform over here.

**Brock Walters:** One of them is I can transfer it to another team, which is pretty cool and super easy to do.

**Brock Walters:** You can also do that with the API.

**Brock Walters:** What a lot

**Brock Walters:** What of customers have set up is an enrollment flow where every device gets enrolled into no team, and it's kind of functioning as like a staging team.

**Brock Walters:** And then there's some automation that's performed to move it to the right team after it's been assessed.

**Brock Walters:** And that just depends on how you're doing the enrollment.

**Brock Walters:** It's flexible.

**Brock Walters:** You can also run a script and a query.

**Brock Walters:** I can't query this host because it's a VM, so it probably doesn't really even exist anymore.

**Brock Walters:** But in order to run a live query, the device has to be actually talking to Fleet.

**Brock Walters:** You can lock it or wipe it or delete it.

**Brock Walters:** Now, delete means you're deleting the record.

**Brock Walters:** But lock or wipe means you're actually wiping the device remotely or locking it.

**Brock Walters:** These are very important security features.

**Brock Walters:** One thing that's kind of cool about Fleet is that you'll see this lock and wipe regardless of what platform it is.

**Brock Walters:** So this is a very important feature for us because it's difficult to manage lock and wipe.

**Brock Walters:** For Linux, it's a little bit difficult to manage lock and wipe from Windows.

**Brock Walters:** We have these actions available regardless of what platform the device is.

**Brock Walters:** And they're all in the same place.

**Brock Walters:** They function different ways, but the UI is consistent from platform to platform.

**Brock Walters:** And that's a big theme for us.

**Brock Walters:** It's like, how do we make managing multiple platforms flatter?

**Brock Walters:** That's kind of the goal of the product, I would say, or one of the major goals of the product.

**Brock Walters:** Okay, so let's actually get on a team and talk about controls.

**Brock Walters:** So when we talk about controls, we're talking about things like OS updates.

**Brock Walters:** And we have some of this built into the product.

**Brock Walters:** So, like, you can set a minimum version for Mac OS.

**Brock Walters:** You can set a deadline for Windows and the grace period.

**Brock Walters:** You can set a minimum version for these other platforms.

**Brock Walters:** You can also turn this off and you can add your own.

**Brock Walters:** Software update controls, like Nudge, which is a very common one in the Mac management world.

**Brock Walters:** We also have OS settings.

**Brock Walters:** In OS settings, we have one OS setting built into the product, and that's disk encryption.

**Brock Walters:** And this goes back to something that I said I would talk about before, which is that if I have a team, this isn't the team I was on before, I think it was Dale's team, that has multiple platforms, Macs and Windows.

**Brock Walters:** What's kind of cool about having this disk encryption control built in is that I can set this single checkbox and turn on disk encryption for multiple platforms.

**Brock Walters:** So if I have Linux computers in here, if I have Windows computers here, I have Macs in here.

**Brock Walters:** Bye checkbox.

**Brock Walters:** Check this checkbox.

**Brock Walters:** Encryption is going to get enabled for Linux and Windows and Mac.

**Brock Walters:** Now, encryption is very, very different on all three of those platforms.

**Brock Walters:** It works differently completely on all three.

**Brock Walters:** But I only have to set one control in Fleet to enable that if the team has multiple platforms.

**Brock Walters:** So, again, this is kind of the theme, is this flattening simplification.

**Brock Walters:** Not all of our customers need that.

**Brock Walters:** Many of our customers don't need or even don't want easy buttons for things because they have sophisticated engineering teams and they want to manage this stuff on their own.

**Brock Walters:** But this is something you can do.

**Brock Walters:** Another thing you can do is have custom settings.

**Brock Walters:** So this is device profiles.

**Brock Walters:** So for Macs and iOS devices, these are referred to as configuration profiles.

**Brock Walters:** For Windows, they're referred to as device profiles.

**Brock Walters:** And these are just specifications on Windows and the Apple operating systems that allow you to.

**Brock Walters:** So it's the things like, how long is the screen lock, and what shows up on the login screen?

**Brock Walters:** Is it name and password?

**Brock Walters:** And all those kinds of controls.

**Brock Walters:** What's the password length?

**Brock Walters:** All of the things that a security organization tells a client platform engineering organization that they have to set to be a certain way so that they can be compliant.

**Brock Walters:** So this is a very important part of the product.

**Brock Walters:** This tells you that the controls have been verified on hosts.

**Brock Walters:** It tells you whether they're in a verifying state.

**Brock Walters:** This is using OS Query to do that check.

**Brock Walters:** And it's telling you if any have failed.

**Erik O'Brien:** Okay?

**Erik O'Brien:** Yep.

**Brock Walters:** We have this end user setup experience.

**Brock Walters:** And what that means is this is integrated to work with automated enrollment programs.

**Brock Walters:** So for Mac, this is referred to as automated device enrollment.

**Brock Walters:** And also for iOS devices.

**Brock Walters:** For Windows, this is referred to as Autopilot or Automated Enrollment.

**Brock Walters:** And what the end user experience is, is a thing that it's basically a fancy progress bar, right?

**Brock Walters:** And lots of, Kanji has this similar feature, it's called Passport, which you probably saw when your computer was being set up the first time.

**Brock Walters:** So there's like a screen that's showing on your computer that's kind of like telling you what's happening and what's being installed.

**Brock Walters:** And then at the end of that process, your computer is set up.

**Brock Walters:** So that's what the end user experience does.

**Brock Walters:** It lets you customize the bootstrap package.

**Brock Walters:** It lets you install software at that phase.

**Brock Walters:** It lets you run scripts to do stuff to the computer during enrollment, which is often very important for customers.

**Brock Walters:** It lets you manage the setup assistant steps, which if you just take a computer out of the box or an iOS device out of the box to set it up, there's a number of steps that you have to go through.

**Brock Walters:** This lets you skip over those if you want to.

**Brock Walters:** So that's what the end user set of experience is.

**Brock Walters:** And again, going back to this theme of the team represents a set of management concepts, if you will, for managing a certain set of devices in your org.

**Brock Walters:** You very well might want to have a different set of experience for team A versus team B.

**Brock Walters:** Now, maybe you don't have that.

**Brock Walters:** Maybe everybody in your organization needs and wants the same set of experience.

**Brock Walters:** But if you wanted them to be different, like if you wanted one of the setup assistant steps to be different for the accounting team versus the development team, you can do that.

**Brock Walters:** That's the idea here.

**Brock Walters:** You can have scripts and you have a library of scripts.

**Brock Walters:** You can see that you can upload Windows scripts, PS1, or shell scripts.

**Brock Walters:** Fleet will also accept ZSH scripts as well.

**Brock Walters:** And you can...

**Brock Walters:** can click on these and actually read them, which is kind of nice.

**Brock Walters:** You can actually see what the script is without having to download it.

**Brock Walters:** And there's a batching feature now, so you can actually run the script on multiple computers at one time.

**Brock Walters:** It tells you when they're scheduled, when they're set to be done, when the batches are complete.

**Brock Walters:** Another thing that we have here is variables.

**Brock Walters:** There aren't any, but what this is going to allow you to do is create a string in Fleet that can be used as a variable in a script or a configuration profile.

**Brock Walters:** And there's lots of technical reasons why you might want to do that.

**Brock Walters:** It's actually kind of cool that you can do this from the console.

**Brock Walters:** I don't know that any other MDM has this feature.

**Brock Walters:** But it's pretty nerdy and pretty technical.

**Brock Walters:** So this is the software section.

**Brock Walters:** And again, you...

**Brock Walters:** can install software differently for every one of your teams.

**Brock Walters:** One thing to talk about here is, this is going to be mildly confusing, but when you install the Fleet Agent, one of the things that gets installed is the Fleet Desktop app.

**Brock Walters:** And there must be something really wrong with DogFood because it says I'm not connected to it right now.

**Brock Walters:** So, I don't know what's happening with that instance, but something happened.

**Brock Walters:** I'm sure I'll find out after this meeting.

**Brock Walters:** So, where you would see self-serving...

**Brock Walters:** Oh, here we go.

**Brock Walters:** Still down.

**Brock Walters:** Maybe it's going to come back to life, come roaring back to life.

**Brock Walters:** Okay.

**Brock Walters:** Nope.

**Brock Walters:** Nope.

**Brock Walters:** Nope.

**Brock Walters:** Nope.

**Brock Walters:** Ah, cool.

**Brock Walters:** So, this is not actually the fleet server.

**Brock Walters:** This is the client side view.

**Brock Walters:** And it's a little confusing when you're looking at them one after the other.

**Brock Walters:** Like, this wouldn't be confusing at all if you'd never seen the server.

**Brock Walters:** But the reason it's confusing is because I'm showing you the server.

**Brock Walters:** The UI in the server looks very much like the UI that the end user sees.

**Brock Walters:** And again, I'm probably boring you at this point.

**Brock Walters:** But the idea is that fleet is transparent and flat.

**Brock Walters:** That means that we're also as transparent as possible to the end user.

**Brock Walters:** So, this is something that you would have to work pretty hard in Kanji or in Jamf to show the end user, hey, these are the policies that I'm running on your computer.

**Brock Walters:** This is just built into fleet out of the box.

**Brock Walters:** Another thing that you see here is self-service.

**Brock Walters:** So it's probably going to take a little while to load since it hasn't talked for a while, assuming that there isn't still a problem.

**Brock Walters:** This is my host record.

**Brock Walters:** So if I were to compare my host record in the server versus what I'm seeing here, you would see that they're pretty much identical.

**Brock Walters:** This is software.

**Brock Walters:** This is probably going to take even longer to load since there was a problem, obviously.

**Brock Walters:** And this is showing the policies that are passing on my computer, and it's showing one that's failing.

**Brock Walters:** All right.

**Erik O'Brien:** So...

**Erik O'Brien:** would fail, you just need to update one pass?

**Brock Walters:** Yeah, and I will get to that.

**Brock Walters:** Great question.

**Brock Walters:** That's exactly correct.

**Erik O'Brien:** Cool.

**Brock Walters:** You know, there's a couple more things to say about software.

**Brock Walters:** We have fleet-maintained apps, which means that those can be automatically installed from fleet.

**Brock Walters:** You can upload custom software if you need to install something that we don't have in the fleet-maintained app library.

**Brock Walters:** And that's pretty much it.

**Brock Walters:** There's kind of three levels of software.

**Brock Walters:** There's the entire catalog of things you could install.

**Brock Walters:** There's the library.

**Brock Walters:** That means that those are things that you've set to install.

**Brock Walters:** And then there's the inventory.

**Brock Walters:** That's the devices reporting back, showing what software they actually have.

**Brock Walters:** And then from those three kind of collections, there's a few different ways to install software.

**Brock Walters:** One is with a custom package.

**Brock Walters:** Two is from an app store.

**Brock Walters:** Three is with the fleet-maintained apps.

**Brock Walters:** Make sense?

**Erik O'Brien:** Yep.

**Brock Walters:** And if I add software, this is what that looks like.

**Brock Walters:** This is fleet-maintained apps.

**Brock Walters:** This is stuff from the app store.

**Brock Walters:** There probably isn't even the VPP token set up in this instance.

**Brock Walters:** And then this is uploaded custom packages with which you can have

**Brock Walters:** Custom install scripts, and you can set them for self-service, and set them for automatic install.

**Brock Walters:** All good stuff.

**Brock Walters:** Okay, so to your question, a policy in fleet is something pretty interesting, and it doesn't trigger automation, but a policy failure can, and that is the trigger for all automation in fleet.

**Brock Walters:** Now, I think I mentioned this very briefly, but before I dive completely into policies, I want to go back here and talk about queries.

**Brock Walters:** All of the fleet features, and MDM is a separate specification, but one of the interesting things about fleet as a product is that the MDM features are kind of built upon OS Query.

**Brock Walters:** What is OS Query?

**Brock Walters:** OS Query was a project that was started at Facebook in 2014.

**Brock Walters:** One of our co-founders, actually, was one of the co-creators of the OS Query product.

**Brock Walters:** Um...

**Brock Walters:** Well, OS Query is open source.

**Brock Walters:** There are lots of products that use OS Query now.

**Brock Walters:** CrowdStrike uses it.

**Brock Walters:** There are other products that have it built in.

**Brock Walters:** None of those products have one of the co-founders as the co-founder of a product like this.

**Brock Walters:** So a query just means that when you install the OS Query agent, and I guess I should back up a little bit because I've already talked about this.

**Brock Walters:** When you enroll a computer in Fleet, you install what we refer to as Fleet D.

**Brock Walters:** The Fleet D actually has two agents.

**Brock Walters:** One is the OS Query agent.

**Brock Walters:** Two is what's called Orbit, which is the Fleet agent that kind of does everything else.

**Brock Walters:** So this would be the equivalent of the Jamf binary or the Congee binary.

**Brock Walters:** Okay, OS Query is kind of a completely separate thing. And what it was built to do is find data on an operating system, and it could be anything.

**Brock Walters:** It could be the contents of a file.

**Brock Walters:** It could be the output of a shell binary.

**Brock Walters:** It could be using some deep-level API.

**Brock Walters:** Basically, any information that you can get from the computer, and it expresses that data as a SQL table, a SQLite table.

**Brock Walters:** So I don't know how much you know about databases or how much you care about databases.

**Brock Walters:** But what's really cool about that is what that means is if you can express the data from a computer in the same way from every computer, you're kind of limiting what you have to know to collect that data.

**Brock Walters:** In other words, if you can express the data on an operating system as a SQL table, that means you can write SQL queries against that SQL table to get the data back.

**Brock Walters:** And that's one of the kind of core features of Fleet.

**Brock Walters:** If I look at one of these queries, and I don't know that there are any saved in here.

**Brock Walters:** Here we go.

**Brock Walters:** This is a very, very simple query.

**Brock Walters:** This is just saying from the OS query flags table, give me everything.

**Brock Walters:** That's what select star means.

**Brock Walters:** If you look at this list of tables over here, there's 344 different tables.

**Brock Walters:** It's a long list.

**Erik O'Brien:** And there's...

**Erik O'Brien:** Yeah, think Sam, or somebody shared that list.

**Erik O'Brien:** Cool.

**Erik O'Brien:** The account policy data.

**Brock Walters:** Yeah.

**Brock Walters:** And there's, you know, there's 344 of them.

**Brock Walters:** So, like, you can get Wi-Fi status.

**Brock Walters:** You can get Windows crash log.

**Brock Walters:** You can get Windows live events.

**Brock Walters:** It's pretty incredible.

**Brock Walters:** Let me show you in a little bit easier to read way.

**Brock Walters:** Because that view of it is meant to be searchable.

**Brock Walters:** Yeah.

**Brock Walters:** So this is the Apple table, the Apple-specific tables, Linux-specific tables.

**Brock Walters:** Now, there are some tables that are cross-platform, and the ones that tend to be our cross-platform are the ones where, like, why is the ARP cache table available on Apple, Windows, and Linux?

**Brock Walters:** Well, it's because the modern network stack predates any of these operating systems, right?

**Brock Walters:** The modern network stack goes all the way back to the original Unix computers, and the network stack really hasn't changed that much.

**Brock Walters:** So the ARP cache is something that exists in the network stack of every operating system.

**Brock Walters:** That's why this table is compatible with all three.

**Brock Walters:** If that weren't the case, then Macs and Windows computers wouldn't be able to talk to each other across the network, right?

**Brock Walters:** And this is just really basic networking information, but it's available in this table.

**Brock Walters:** You can combine the tables.

**Brock Walters:** So you could pass the information from one table to another.

**Brock Walters:** So it's really the sky is the limit in terms of what kind of data you can collect as long as you can come up with a creative way for using these tables to express it and then parse it down with a query.

**Brock Walters:** And this is part of the reason why people use Fleet alongside other MDMs is because this data is so rich and so expressive that you can enhance the management capabilities of any other platform with data like this.

**Brock Walters:** Okay, now without, I'm not going to go any more into it than that.

**Brock Walters:** You can do a lot with queries.

**Brock Walters:** There's a lot of tables.

**Brock Walters:** It's really cool.

**Brock Walters:** Now, how does this work with policies?

**Brock Walters:** Well, policies also use queries, but the difference is instead of trying to collect data, what you're trying to do with a policy query is just generate a Boolean result.

**Brock Walters:** In other words, I'm assessing the state of something on the device and I'm finding out what.

**Brock Walters:** Whether or not it's true or false.

**Brock Walters:** If I can write a query in such a way that I can get a failure, like is my one password up to date, then that can act as a trigger in fleet for automation.

**Brock Walters:** So when I go back here and select automations, this is basically saying, okay, these are the automations that are available to you if a policy fails.

**Brock Walters:** One of the things I can do, which we've already talked about, I can send a generic webhook.

**Brock Walters:** Again, this is incredibly powerful.

**Brock Walters:** This means on any policy failure that I can generate, I can send a generic webhook to anything that's capable of listening to a webhook and trigger some other action in some other system.

**Brock Walters:** Or I could send an API call back to fleet directly to do something else.

**Brock Walters:** I can also send a ticket to a ticketing system like Jira or Zendesk.

**Brock Walters:** If I don't use Jira or Zendesk, my ticketing system probably can handle a generic webhook.

**Brock Walters:** So this this is...

**Brock Walters:** Super powerful.

**Brock Walters:** What else can I do?

**Brock Walters:** I can run a script on a policy failure.

**Brock Walters:** Why would I do that?

**Brock Walters:** Kanji has a feature for automatic remediation.

**Brock Walters:** Like if it runs a script and it determines that the state of that script isn't what it's supposed to be, it runs a script to fix that.

**Brock Walters:** So you could get that same behavior with this.

**Brock Walters:** Exactly the same.

**Brock Walters:** In fact, I would argue that it's better because it's not running on a clock to check that one thing.

**Brock Walters:** It's just checking the state of the device and only running it if the state of the device shows that it's failed.

**Brock Walters:** It's a very similar system.

**Brock Walters:** But the idea here is that you can customize your query to do that just with a simple SQL query.

**Brock Walters:** You can install software.

**Brock Walters:** And the classic here would be, and I don't know that this policy is set up that way, but like you could say if...

**Brock Walters:** If there's no software that shows that Brave is, if the software inventory does not show that the Brave browser has been installed, which would mean that that policy would fail, you could install the Brave browser.

**Brock Walters:** If that was a mandatory app, you could have a policy that was set up to fail if it wasn't there, and then install it.

**Brock Walters:** So hopefully you're kind of seeing the theme here.

**Brock Walters:** Yeah.

**Brock Walters:** And these policies are the same ones that show on the end user's computer, that's like, hey, you're failing this one.

**Brock Walters:** Now, the things that I'm talking about are what we refer to as auto-remediation, meaning I've set up some automation to run based on the policy failure.

**Brock Walters:** But we also have the concept of, I guess we're back to failing again.

**Brock Walters:** I don't know what's happening.

**Brock Walters:** We also have the concept of self-remediation.

**Brock Walters:** So what that means is that, like, I can show you in the, in the.

**Brock Walters:** Console.

**Brock Walters:** So if I go to one of these policies, it doesn't have a description, but you see where it says add description and resolve.

**Brock Walters:** This just means that if I had populated these, instead of there being an automated thing that runs when the policy fails, maybe all I'm doing is telling the user that the policy has failed and that they can take some steps themselves to fix it.

**Brock Walters:** So that's self-remediation versus auto-remediation.

**Brock Walters:** It's a kind of a nice feature.

**Brock Walters:** The only thing we haven't talked about is stuff in settings.

**Brock Walters:** And there's a bunch here.

**Brock Walters:** I'm not going to dig into it super hard.

**Brock Walters:** But over here in this user administrative menu is where you find things like, what do I want my instance to be called?

**Brock Walters:** And how do I set up an SMTP server?

**Brock Walters:** What's

**Brock Walters:** It's my URL, and then there's a configuration for the agent, there's usage statistics, there's a customizable URL here, so for this About Fleet menu item, you can actually set any URL you want, that might be an internal resource, that might be another web page that you manage.

**Brock Walters:** This is where you would set up Apple MDM stuff, and certificate stuff, and then there's a bunch of integrations, this is where you would set up the webhook ticket integration, this is where you set up the MDM programs, like Apple Business Manager, and Windows Autopilot, this is where you can configure GetOps mode, we didn't talk about GetOps at all, but one of the strengths of Fleet Platform is that, you have the ability to control everything that I showed you with code, and what does that, what could that possibly be?

**Brock Walters:** What mean?

**Brock Walters:** Well, if I go here, and this is the fleet public repo, the fleet entire code base is here in this repository, every single bit of fleet code is here in the public and on the internet, and that's partly what we mean by open core, open source.

**Brock Walters:** One of the repos here in the fleet organization is this fleet GitOps repo.

**Brock Walters:** We actually use this repository as the starting place for a course that we teach that shows you how to configure fleet with these YAML files.

**Brock Walters:** So for example, I have this workstations YAML.

**Brock Walters:** What this file represents is the configurations for a team.

**Brock Walters:** And if I go back to the fleet product, what that configuration file represents is everything that I've shown in terms of a team—the policies that are associated with that team, the queries that are associated with that team, the software that's associated with that team, the controls that are associated with that team.

**Brock Walters:** So if I look at this, you can see here are the policies, here are the controls, here are the team settings.

**Brock Walters:** Now, this doesn't have every one of those things, but it doesn't have to have all of them.

**Brock Walters:** But what I'm intending to show you here is that every aspect of the fleet console and every aspect of management can be controlled this way.

**Brock Walters:** Why would you want to do this crazy thing?

**Brock Walters:** Because it allows you to manage the state of the console with a version-controlled code repository that gives you the ability to roll backwards to a previous configuration if something bad happened, and it allows you to do the management work out in the open, where pull requests have to be created, and peer review of the changes are managed out in the open.

**Brock Walters:** And this is an incredibly powerful feature set.

**Brock Walters:** Of the product, probably the thing that the more sophisticated client platform engineering teams are interested in than any other feature.

**Brock Walters:** We actually have some customers that don't use the UI.

**Brock Walters:** In fact, there's a feature here in change management called GitOps mode.

**Brock Walters:** And that's how I got to where I just was because I actually was on this page.

**Brock Walters:** What this does is turns the UI into a read-only mode.

**Brock Walters:** So you can't even make changes in the UI.

**Brock Walters:** You can only make changes with code.

**Brock Walters:** And to someone that doesn't live in this world, that sounds bananas.

**Brock Walters:** But it's actually incredibly powerful.

**Brock Walters:** And what lots of organizations have tried to do with other platforms, and the reason they struggle with it, is because those platforms aren't built to do this.

**Brock Walters:** This one is built with this purpose in mind.

**Brock Walters:** Managing configuration as code is actually potentially a lot more stable, especially when something bad happens.

**Brock Walters:** Because if you're only clicking in the UI and you've clicked a bunch of stuff and it turns out that something bad happened, I have to unclick everything.

**Brock Walters:** And that's very hard to do.

**Brock Walters:** But if I have a configuration that says, hey, the state of the console is supposed to be this, all I have to do is push that up and the state has changed.

**Brock Walters:** So this is one of the most powerful aspects of Fleet.

**Brock Walters:** Everything that I've showed you can be controlled with code.

**Brock Walters:** I think that's it.

**Erik O'Brien:** How'd I do?

**Erik O'Brien:** Perfect on timing.

**Brock Walters:** Well, I've done it a few times.

**Erik O'Brien:** Yeah, and I think I've got a way better understanding of the product and kind of differentiators.

**Brock Walters:** I was trying to do that.

**Brock Walters:** In a normal demo, I might not land on that stuff.

**Brock Walters:** So much, but I feel like it's important, and I normally maybe wouldn't talk about other products that much, but I was trying to point out the places where there's an obvious scene, right?

**Brock Walters:** Jamf is a very good product.

**Brock Walters:** Kanji is a very good product.

**Brock Walters:** Sorry, I'm going to have to get used to saying whatever it's called now.

**Brock Walters:** But I firmly believe that there's room in the market for many of these products because they all do different things differently.

**Brock Walters:** And I don't know if Mike wants to hear that message necessarily, or a corporate board wants to see that your product is gobbling up every other product in the comparable segment.

**Brock Walters:** But there are definitely differences, and we have some real strengths that our customers, you know, I believe that they believe in.

**Brock Walters:** And...

**Brock Walters:** One of those differences is definitely this configuration as code thing.

**Brock Walters:** Another one of those differences is the kind of the flattening of the cross-platform world.

**Brock Walters:** The idea that hopefully what we're trying to do at the end of the day is give some people that do these jobs a little bit of their time back.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** I had a bunch of questions, but you do like rip straight through.

**Erik O'Brien:** Oh, cool.

**Brock Walters:** Well, look, I mean, go ahead and ask him anyway.

**Erik O'Brien:** Maybe there's something I missed.

**Erik O'Brien:** I'm just looking through ones that maybe aren't as obvious, but.

**Erik O'Brien:** Is there any language or phrasing you guys would avoid?

**Brock Walters:** That's a great question.

**Brock Walters:** And I was alluding to this on the call earlier, the one we had before.

**Erik O'Brien:** Yep.

**Brock Walters:** Here

**Brock Walters:** Do you mean, like, generally or, like, specific words?

**Erik O'Brien:** Generally, you know, kind of like, we want to have, like, editorial guardrails, so, like, preventing off-brand buzzwords is kind of the angle.

**Brock Walters:** Yeah.

**Brock Walters:** It's such a good question.

**Brock Walters:** And I know them when I see them.

**Brock Walters:** You know what I mean?

**Brock Walters:** Like, I'll tell you what I hate.

**Brock Walters:** And it was interesting that in one of those docs.

**Erik O'Brien:** Well, that.

**Brock Walters:** There is, what I don't think should be associated with the fleet brand is jargon that's not explained.

**Brock Walters:** And I'll try to delineate the difference.

**Brock Walters:** There is absolutely no problem with saying JSON because everybody knows what you mean when you say that, at least people that are technical.

**Brock Walters:** Right?

**Brock Walters:** But I have a huge problem with POC.

**Brock Walters:** Now, you probably know what POC means, and I know what it means.

**Brock Walters:** It means proof of concept.

**Brock Walters:** But it's just jargony, and it's not associated with an actual specification.

**Brock Walters:** And so my function in this, I think, has to be, I'm trying to be some sort of mitigator of the truth.

**Brock Walters:** And what I don't want associated with the fleet brand is anything that's jargony and unexplained.

**Brock Walters:** And I think that your documents got very close to that, at least the ones I was reviewing earlier today.

**Brock Walters:** In, it, like, the thing was saying, like, it should be clear and not jargony.

**Brock Walters:** don't remember exactly how it was phrased, but I thought it was right.

**Brock Walters:** It was like, we don't want to talk about, like, those businessy buzzwords.

**Brock Walters:** We just want to talk about the actual thing.

**Brock Walters:** And, and, and, you have to.

**Brock Walters:** Avoid being overly technical because we have to sell the product to people that are decision-makers that maybe necessarily aren't technical.

**Brock Walters:** But at the same time, the people that we're trying to attract as champions of the product are technical.

**Brock Walters:** So it's a real balancing act between saying what's true and explaining technology simply.

**Brock Walters:** I have this background as an instructor.

**Brock Walters:** That's what I did at Jamf for five years.

**Brock Walters:** And my bargain with the students was, and I probably broke it in the demo I just gave you a couple of times.

**Brock Walters:** And every time I do it, I have a problem.

**Brock Walters:** But sometimes in the middle of a demo like that, you can't stop.

**Brock Walters:** But the bargain is I'm not going to talk about something that I'm not going to explain.

**Brock Walters:** I'm not going to bring up a concept that I'm not going to explain what I mean.

**Brock Walters:** And a lot of times when you see these buzzwords in these blog articles, that's all you get.

**Brock Walters:** Fathom is AI magic that is totally unexplained.

**Brock Walters:** It's like, okay, cool, you said you're doing that, but how are you doing it?

**Brock Walters:** Or you said that this is a thing, but I have no idea what that thing means.

**Brock Walters:** So like, I don't know if I can give you specific buzzwords, but what I'm describing is what I would like to avoid.

**Brock Walters:** I want the clarity and truth of the product to come through.

**Brock Walters:** And the biggest one we have to fight right now is that apparently the AI is trained on a two-year-old conception of what fleet is.

**Brock Walters:** And the funny thing about that is like, two years for a product like this is actually not very much time.

**Brock Walters:** Like, I understand why the models still say stuff from two years ago.

**Brock Walters:** So, uh, but the fleet engineering team moves really, really fast.

**Brock Walters:** And there's actually been a lot.

**Brock Walters:** There's of stuff built in the last two years and it just so happens I've worked at Fleet for two years.

**Brock Walters:** The amount of features that have been added, mean, it's hundreds of features.

**Brock Walters:** So, I think the stuff that you called out, let me just look at it really quickly, if you don't mind.

**Brock Walters:** I know we only have a few minutes left.

**Brock Walters:** Am I making any sense?

**Erik O'Brien:** Yeah, definitely.

**Erik O'Brien:** get the general gist is, like, don't say anything that's not basically common knowledge without explaining it.

**Brock Walters:** Right.

**Brock Walters:** No, that's not where they were.

**Brock Walters:** The writing guidelines.

**Brock Walters:** And a lot of this you got from the Fleet Handbook.

**Erik O'Brien:** Yeah.

**Brock Walters:** But it's like...

**Brock Walters:** Right, it's just stuff like, this is a perfect example, the very first one.

**Brock Walters:** Certificate expiration breaks authentication, check validity dates before outages.

**Brock Walters:** Bad.

**Brock Walters:** Transform your IT infrastructure through innovative cloud-native solutions.

**Brock Walters:** Horseshit.

**Erik O'Brien:** Yeah.

**Brock Walters:** And I just don't, we can't afford any more of that.

**Brock Walters:** The only thing we can afford is to have true, clear, precise statements about what the product actually is.

**Erik O'Brien:** Yeah.

**Brock Walters:** So, I don't know if that's an answer.

**Brock Walters:** Maybe we can hone in on it more when we talk more, but.

**Erik O'Brien:** Yeah, I think, I mean, I think we, we tend to lean towards that with a lot of our clients and writing guidelines of like, we're not going to do jargon.

**Brock Walters:** We're not doing fluff.

**Erik O'Brien:** It's like, if you can't understand it, if it doesn't have a specific.

**Erik O'Brien:** Like, point in being in a sentence and just remove it or fix it.

**Brock Walters:** I think the danger is if you guys are generating five blog articles a week, how are you differentiating them?

**Brock Walters:** You know, I mean, there's a point at which you're going to run out of things to say and you want to fill it up with some nice sounding words.

**Brock Walters:** But, like, if we can do that and actually focus on real topics, like, you would know more than me.

**Brock Walters:** But if I were to dedicate all of my time to generating five blog posts a week, I think there's enough real stuff to write about.

**Brock Walters:** I genuinely do.

**Brock Walters:** The reason people put that fluffy stuff in there is because they actually don't know what they're talking about.

**Erik O'Brien:** Or have nothing else to say.

**Brock Walters:** It's just like, why don't you just fill it?

**Brock Walters:** Exactly.

**Brock Walters:** Like, I mean, just transform your IT infrastructure through Innovative Cloud.

**Brock Walters:** Native solutions.

**Brock Walters:** We got a joint value proposition.

**Brock Walters:** I'm not going to say who from whom, but it's a company that we're partnering with.

**Brock Walters:** And like, I went in and put all these like actual use cases, how our product and their product is used together.

**Brock Walters:** And she sent her version of it back.

**Brock Walters:** And it was just 100% that.

**Brock Walters:** It had been AI generated, I guarantee it.

**Brock Walters:** And none of it made any sense.

**Brock Walters:** And I like, I wasn't mad, but I'm just like, what are we doing?

**Erik O'Brien:** Like, who is this for?

**Brock Walters:** who, like, what does it actually mean?

**Brock Walters:** Well, I know what it's for.

**Brock Walters:** I mean, it's so that we get bumped up in the, when the AI searches happen.

**Brock Walters:** And I think that's a valuable thing.

**Brock Walters:** But do you, do you find that you can do this in a way and maintain the integrity of the content?

**Brock Walters:** Or is it all about the process and the gaming, the system?

**Erik O'Brien:** I mean, the headlines are typically where you're like, you have to bake the keyword in.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** But the record.

**Erik O'Brien:** The of the content, absolutely not.

**Brock Walters:** That's where you don't have to sacrifice.

**Erik O'Brien:** Okay.

**Erik O'Brien:** So yeah, there's just certain headers that have to include the keywords, but the rest of the content is we try to nail voice and tone.

**Brock Walters:** Cool, that's great.

**Erik O'Brien:** Really on brand.

**Brock Walters:** Awesome.

**Brock Walters:** Anything else in your question list?

**Erik O'Brien:** I guess one, and it's more for my curiosity and kind of just make sure I capture it, but when you say open device management, what does open deliver that these closed vendors can't?

**Brock Walters:** Great question.

**Brock Walters:** So this is the example that I always go to.

**Brock Walters:** We do Linux management, okay?

**Brock Walters:** I don't, this is a, there's a running joke in IT that like this year is going to be the year of the Linux desktop, right?

**Brock Walters:** This is going to be finally the year when it happens, and it never does.

**Brock Walters:** Okay.

**Brock Walters:** But there actually does seem to be some penetration with Linux on the desktop.

**Brock Walters:** We have one customer that has thousands of Linux desktop users.

**Brock Walters:** Okay.

**Brock Walters:** And the tendency at an organization that has a lot of users like that is that these people are reluctant to be managed.

**Brock Walters:** So why aren't Linux devices managed?

**Brock Walters:** One, there is no MDM specification for Linux.

**Brock Walters:** Two, there's dozens of Linux flavors that make management tricky.

**Brock Walters:** And three, the people that use those devices are probably using them specifically to avoid management because they know that the Windows computers and Macs in their organization are managed, but nobody can wrangle the Linux devices.

**Brock Walters:** Okay.

**Brock Walters:** The problem with, for the organization there becomes, I have to wrangle them because I have cyber insurance and I have a compliance story that I have to fulfill.

**Brock Walters:** And if I don't, we're going to lose money.

**Brock Walters:** So, how do I talk to my Linux users in a way that allows them to feel comfortable about management when they've never had to do it before?

**Brock Walters:** One way is to say, look, we're using a product where every bit of their code is published on the Internet.

**Brock Walters:** And you're probably a developer.

**Brock Walters:** Go look at their repository.

**Brock Walters:** If you want to see what they're doing or you believe that we're doing something nefarious, every single scrap of the code is on the Internet.

**Brock Walters:** This is a hugely powerful story for those people.

**Brock Walters:** Now, it's a small niche of the market, but we do have customers that have that very antagonistic user.

**Brock Walters:** And there are also just people that are reluctant to management who aren't developers.

**Brock Walters:** They've just never had it.

**Brock Walters:** We have companies who've never had device management before.

**Brock Walters:** And I think Fleet has the idea that it's open and transparent.

**Brock Walters:** They...

**Brock Walters:** They...

**Brock Walters:** We're not doing anything to hide from the end user what the admin is doing, and we're not doing anything to hide what we're doing from the admin.

**Brock Walters:** And it's not perfect, but transparency all through the system is the goal.

**Brock Walters:** So I would say that's the answer to that question.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** Well, we are a little past time, but really appreciate the walkthrough.

**Erik O'Brien:** I now know a lot more than I did coming in, so if nothing else, I got that.

**Erik O'Brien:** But we'll use this to also kind of create a summary and then feed that in to update our artifacts.

**Erik O'Brien:** So between now and Friday, we might have some revisions, but we'll also go through the company context one in pretty detailed on Friday.

**Brock Walters:** Awesome.

**Brock Walters:** If I said anything stupid, leave that out.

**Erik O'Brien:** Yeah, for sure.

**Erik O'Brien:** All right.

**Brock Walters:** Thanks, Erik.

**Erik O'Brien:** All right.

**Erik O'Brien:** Thanks.
