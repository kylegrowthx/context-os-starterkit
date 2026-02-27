# Weekly Prospecting Block

<metadata>
date: 2026-02-25
time: 22:30 UTC
duration: 96 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Gloria Willis, Jason Gong
fireflies_id: 01KHSJ8WRHXRRMWX072Q6MSH5Q
transcript_url: https://app.fireflies.ai/view/01KHSJ8WRHXRRMWX072Q6MSH5Q
</metadata>

---

## Summary

The team discussed creating a personal CRM system that captures detailed relationship contexts, aiming to integrate it with tools like HubSpot for efficient outreach. They outlined a tiered contact engagement model to prioritize interactions and manage workload effectively, with plans for automated pre- and post-event messaging to enhance lead nurturing. Additionally, workshops were planned to share insights and build community, alongside strategies to expand into new markets like Salt Lake City.

---

## Action Items

**Marcel Santilli**
- Follow up with Rachel on co-hosting the March 26th dinner event and confirm location agreement
- Provide clarity and final approval of the personal contact dossier before uploading to HubSpot
- Invite Kristen or confirm alternate arrangements for Growth Cafe March 26th session with Cece
- Monitor and push registration for Salt Lake City dinner event targeting 12–15 attendees, with follow-up on venue capacity
- Continue developing personal CRM system including contact dossier updates and tier segmentation to improve network management
- Coordinate with Stevie and Daniel on addressing content-related engineering tickets for the 'check that' platform

**Jason Gong**
- Assist Gloria Willis with Luma connection troubleshooting and API key integration
- Create scaffolding for contact engagement tiers and automate linking of transcripts and dossiers to HubSpot
- Prepare and send Salt Lake City event invitations with Dig, including reviewing and expanding invitee lists
- Establish weekly relationship/top-of-funnel review meetings separate from pipeline reviews to track interactions and nurture leads
- Develop outreach tools and messaging platforms integrated with contact dossiers for scalable yet personalized communication
- Follow up with Gloria and Marcel on managing content workflow improvements and refining 'check that' functionalities

**Gloria Willis**
- Book venues and ensure March and April event logistics are finalized, including the Angler venue for 26th March dinner and April 7th HubSpot event
- Manage RSVPs and help keep registrations to targeted percentages, understanding that most come late
- Coordinate speaker arrangements for Growth Cafe event and confirm Cece's participation
- Assist in messaging workflows and expand attendee outreach for Salt Lake City event

---

## Transcript

**Marcel Santilli:** This meeting is being recorded.

**Gloria Willis:** Hello.

**Gloria Willis:** Did you find out how the messages got moved?

**Jason Gong:** What's that?

**Jason Gong:** No, I'm just moving back, Like, so confused how this meeting got here.

**Jason Gong:** I feel like Dig might have misunderstood what I was asking.

**Gloria Willis:** I think we're gonna need to get my cursor connected to Luma, because I tried to do something, and then it asked me all kinds of technical questions that I couldn't answer. And then I got afraid and I stopped and I gave up.

**Jason Gong:** We can. We can do that. I guess we could do that now.

**Jason Gong:** Before Marcel joins, could you share what you're seeing? Because that repo has changed, like, a lot since last week.

**Gloria Willis:** Well, this is what I was trying to do. How do I make it come over here?

**Jason Gong:** What are you looking for?

**Gloria Willis:** I was trying to pull up what my original ask was of. I just want to have it build a list of all the March events for me so that I can then do a Slack post. So I just wanted go into Luma, look at the calendar, and pull all the names. And then it was trying to do API stuff.

**Jason Gong:** Oh, I see. Yeah. Can you show me the message where it, like, got stuck?

**Gloria Willis:** Oh, I accidentally archived it.

**Jason Gong:** You scroll up a bit. API returns events. Your calendar key is set up for the lg, the URL you gave first. Calendar. If that's the same calendar, confirm. Yes. And go ahead. Okay.

**Gloria Willis:** Okay, so we have this confirm your calendar API key is set up to pull from Luma dashboard under integrations and API keys under account settings. So this is where I'm at.

**Jason Gong:** Okay, let me see your screen.

**Jason Gong:** Let me see if we can find it.

**Jason Gong:** Yeah, let me see your screen. Let me use GitHub desktop. Let me just click on this. Okay, cool. So you want to go to settings, right? Let me click on this icon.

**Gloria Willis:** These are my things from home.

**Jason Gong:** Let me just find, like, you have to click on the actual account, not on the user account settings, but the account settings, like, like the gear. I'm not sure if you have permission to see it.

**Gloria Willis:** I think we might need to have someone who has administrative access to the Luma account help us out here.

**Jason Gong:** Okay, so what we can do is we can have, like, Dig or whoever has that access can help you out.

**Jason Gong:** But once you have that API key, just put it in the dot env file and then come back to us.

**Gloria Willis:** What's a dot env file?

**Jason Gong:** It's an environment file.

**Jason Gong:** It's where we store our API keys so that they're not exposed on GitHub.

**Gloria Willis:** Okay, and where do I find that?

**Jason Gong:** It's in the root of the repository where the app is, the app code is.

**Gloria Willis:** Okay, so it's in the root of the repository. Okay, got it.

**Jason Gong:** Okay.

**Marcel Santilli:** Hey, everyone.

**Marcel Santilli:** So Gloria, how are we doing with the Luma setup?

**Gloria Willis:** I think we're gonna need to escalate this to someone who has permission to access the admin settings in the Luma account.

**Marcel Santilli:** Okay.

**Marcel Santilli:** I think we should have Dig handle that since he set everything up.

**Gloria Willis:** Good call.

**Marcel Santilli:** So let's, let's jump into the main agenda items. I know we've got a lot on the list today.

**Marcel Santilli:** First, let's talk about the personal CRM and contact dossier.

**Jason Gong:** Yeah, so we've been thinking about how to structure contact information for better relationship management.

**Jason Gong:** The idea is to create detailed markdown files for each contact that capture personal context, family details, past interactions, and any relevant business information.

**Jason Gong:** This goes beyond what traditional CRMs can do.

**Marcel Santilli:** Right, and the key thing for me is that we capture the human side of the relationship.

**Marcel Santilli:** Not just deals or interactions, but the personal touches that make relationships last.

**Marcel Santilli:** We want to link these dossiers to HubSpot records, but keep the sensitive stuff locally.

**Jason Gong:** Exactly. We can use HubSpot's note-pinning feature to store markdown references or summaries, while keeping the full dossiers in a private file system.

**Jason Gong:** This way, we maintain privacy while still integrating business data.

**Marcel Santilli:** I like that approach. So Jason, what's next on building this out?

**Jason Gong:** I'm going to create scaffolding for our contact tiers.

**Jason Gong:** We'll have tier one contacts who need direct Marcel involvement, tier two for moderate engagement, and tier three for broader network contacts.

**Jason Gong:** This helps us prioritize who needs attention and when.

**Marcel Santilli:** That makes sense. This tiering will help me focus on the relationships that matter most.

**Marcel Santilli:** And it'll help the team know who can be delegated to.

**Marcel Santilli:** Now, one thing I want to make sure we're clear on: we need to get these dossiers approved and finalized soon so we can start syncing them to HubSpot.

**Jason Gong:** Agreed. I'll have a draft set ready for your review by end of week.

**Gloria Willis:** And I can help with the event-related contact information once we have the dossier structure locked in.

**Marcel Santilli:** Great. Now let's move to event planning. Gloria, where are we on the Salt Lake City event?

**Gloria Willis:** We're targeting 12 to 15 attendees for the Salt Lake City dinner.

**Gloria Willis:** The challenge is we don't have a huge network there yet, so we're thinking of expanding invites to include founders and marketing directors beyond just our typical marketing leader contacts.

**Marcel Santilli:** Good thinking. That gives us flexibility. What about venue logistics?

**Gloria Willis:** I'm working on venue options and will have recommendations by next week.

**Gloria Willis:** I'm also setting a goal of 80% RSVP six weeks out for events, which means we need to start outreach early.

**Marcel Santilli:** That's smart planning. What about the March 26th dinner?

**Gloria Willis:** The Angler venue is booked for March 26th, and we're planning to co-host with Rachel.

**Gloria Willis:** I need confirmation from you on the location agreement so we can finalize details.

**Marcel Santilli:** I'll follow up with Rachel this week and get that locked down.

**Marcel Santilli:** What about the Growth Cafe session with Cece?

**Gloria Willis:** We're coordinating that for March 26th as well.

**Gloria Willis:** Kristen was supposed to help, but I want to confirm alternative arrangements if she's not available.

**Marcel Santilli:** I'll reach out to Kristen and confirm or sort out alternatives.

**Jason Gong:** One more thing on events: I want to set up an automated messaging system.

**Jason Gong:** We'll create a queue where Marcel approves invite lists and message copy, then team members like Dig or Jesus send them out.

**Jason Gong:** All interactions get logged to HubSpot so we don't lose context.

**Marcel Santilli:** I like that. It keeps me in the loop without creating a bottleneck.

**Marcel Santilli:** Let's make sure the messaging is personalized but scalable.

**Gloria Willis:** That makes sense. I can help coordinate the messaging workflows.

**Marcel Santilli:** Now let's talk about our workshop strategy.

**Marcel Santilli:** We've got the CEO OS workshop on March 20, and there's strong interest.

**Marcel Santilli:** I want to be selective about who we invite to protect our R&D and intellectual property.

**Jason Gong:** So we're using the workshop as a hook for community membership and brand building?

**Marcel Santilli:** Exactly. The replays are gated to members only, which maintains exclusivity.

**Marcel Santilli:** We're also planning Growth Cafe events in person where we can go deeper with participants.

**Gloria Willis:** This builds brand authority while protecting our secret sauce.

**Marcel Santilli:** Right. And this ties into the broader strategy of building a personal brand around AI-native marketing.

**Jason Gong:** Speaking of which, I wanted to bring up the Check That project.

**Jason Gong:** Stavone is working on the visibility audit, analyzing millions of AI responses to understand reputation and presence metrics.

**Marcel Santilli:** Yes, and this is critical for our market positioning.

**Marcel Santilli:** We're creating a data-driven framework to quantify how companies are perceived by AI systems.

**Marcel Santilli:** This will become a key part of our sales process.

**Jason Gong:** The deal room concept you mentioned is part of this, right?

**Marcel Santilli:** Exactly. We're building a prospect hub where we can track leads stuck between awareness and closing.

**Marcel Santilli:** This addresses the gap where deals stall due to bandwidth issues.

**Jason Gong:** I've noticed Tyler's capacity is stretched thin, so this system becomes even more important.

**Marcel Santilli:** True. We need a system that tracks these relationships independently of the traditional pipeline.

**Marcel Santilli:** Let me outline the structure: we have a visibility audit that shows market presence, then a deal room that tracks engagement and next steps.

**Marcel Santilli:** Stevie and Daniel are the engineering leads for Check That, and we need to clarify priorities with them.

**Jason Gong:** I'll coordinate with them on content improvements and bulk generation features.

**Jason Gong:** Moving to Clickhouse should help with performance.

**Gloria Willis:** So is there anything else we should cover today?

**Marcel Santilli:** One more thing: I want to set up weekly relationship and top-of-funnel review meetings separate from our regular pipeline reviews.

**Marcel Santilli:** These will focus specifically on tier one and tier two contacts and what engagement actions we need to take.

**Jason Gong:** That's a good idea. It keeps relationship management front and center.

**Jason Gong:** I'll set that up.

**Marcel Santilli:** Great. I also want to explore creating a WhatsApp group for quick voice note brain dumps.

**Marcel Santilli:** We can transcribe these and pull insights into contact notes and action items.

**Jason Gong:** That's efficient. Just need to be mindful of privacy.

**Marcel Santilli:** Absolutely. Only essential people in the group.

**Gloria Willis:** I think this covers the main agenda. Any final thoughts?

**Jason Gong:** I think we've got a solid roadmap.

**Jason Gong:** I'll start on the tier scaffolding and dossier templates this week.

**Marcel Santilli:** Perfect. Let's reconvene next week and review progress.

**Marcel Santilli:** Everyone clear on their action items?

**Gloria Willis:** Yes. I'll focus on venue logistics and event planning.

**Jason Gong:** And I'll work on the technical infrastructure for dossiers and messaging.

**Marcel Santilli:** Great. Let's ship it.
