# Matthew Fischer

<metadata>
date: 2025-04-09
time: 16:01 UTC
duration: 32 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Matthew Fischer (Attio), Andrew Lee (Attio)
fathom_recording_id: 56382344
fathom_url: https://fathom.video/calls/272123150
share_url: https://fathom.video/share/Bzhsf4SDKj4b7X7xxcFcMe6xL-8GXjst
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

Jason Gong from GrowthX worked with Matthew Fischer and Andrew Lee from Attio to set up a Default tool integration for capturing lead form submissions directly into Attio CRM via API calls. They debugged JSON formatting issues and configured a PUT request to create/assert person records using email addresses as the matching field, with Attio auto-creating company records based on email domain. Jason left with options to store form data either as person attributes, in a dedicated "Lead Form Submissions" list, or attached to deals, with guidance on Attio's early-deal-creation model for funnel tracking.

---

## Context

Jason Gong from GrowthX is integrating Default (a lead form builder/router) with Attio CRM, GrowthX's internal CRM platform. GrowthX is a B2B content marketing and AI visibility agency. Attio is a modern CRM that differs from traditional systems like HubSpot in its approach to early-stage deal creation and funnel tracking. This technical support call was a follow-up to a previous conversation where Jason initially requested help with the integration. Because Attio hadn't yet released a native Default integration, Jason needed to hand-code the API connection to route lead form submissions into Attio.

---

## Relevance

- **To GrowthX Delivery:** GrowthX is building lead capture infrastructure using Attio as the core CRM. Understanding how Attio handles person records, company auto-creation, and early-deal-stage creation will shape how the team processes inbound leads and structures data for clients. The "Lead Form Submissions" list pattern is a repeatable approach for tracking early-funnel activities.

- **To GrowthX Business Development:** This is Jason's first hands-on technical implementation with Attio, indicating GrowthX is operationalizing its CRM infrastructure post-deployment. Success here enables GrowthX to better manage its own sales pipeline and serve as an informed user when consulting clients on CRM configuration.

- **To CheckThat:** Not directly relevant to this call, though the conversation touches on data structure and attribution challenges (how to measure conversion impact of early-stage form submissions).

---

## Overview

- Debugged JSON formatting issues and successfully configured a PUT API call to assert/create person records in Attio using email as the matching field
- Attio auto-creates company records based on email domain; no separate company creation required
- Three options for storing form submission data: add to person attributes, create a person-based "Lead Form Submissions" list, or attach to deals
- Attio creates deals early in the funnel (on account creation or form submission), enabling better funnel tracking and drop-off analysis compared to HubSpot's separate Lead object
- No per-contact pricing in Attio; can safely send all form submissions without qualification concerns

---

## Key Topics

### API Integration Setup

  - Used PUT request to assert/create person records: `https://api.attio.com/v2/objects/people/records?match_on=email_addresses`
  - Email address is the matching parameter for the assert operation (determines whether to create or update an existing person)
  - Resolved JSON formatting issues in Default's interface; final working structure wraps email data in a "values" object:
    ``` json
    {
      "data": {
        "values": {
          "email_addresses": [
            {"value": "jason+test@growthx.ai"}
          ]
        }
      }
    }
    ```
  - When asserting a person, additional attributes (name, company, etc.) can be included in the same request body
  - Attio auto-creates company records based on email domain and enriches them if enrichment data is available
  - No need to use Postman or other tools if Default's JSON editor is working, though Postman was mentioned as a debugging aid

### Lead Form Data Storage Options

  - **Person attributes:** Attach submission data directly to the person record when asserting the person
  - **Person-based list:** Create a dedicated list (e.g., "Lead Form Submissions") configured as a table with custom columns/attributes to capture submission details (email, name, company, etc.). The list acts like a table where each submission is a row with associated metadata
  - **Deal-based:** Create a deal when the form is submitted or after a meeting is booked, then attach form data to the deal. This enables better funnel reporting (form submission → meeting → qualified → opportunity)

### Attio's Deal Creation Approach

  - Creates deals early in the funnel (e.g., on account creation, trial signup, or lead form submission)
  - Deal stages used for qualification and progression (e.g., "Intro/Meeting" → "Qualified" → "Not Qualified")
  - Matthew Fischer's company uses this approach: when someone creates a workspace/trial or submits their "Talk to Sales" form, a deal is automatically created in the first pipeline stage
  - Benefits:
      - Centralized data storage (all submission info attached to one deal record)
      - Improved funnel reporting (track drop-off between form submission, actual meeting, qualification, and close)
      - No need for a separate "Lead" object; deals serve that purpose from the start

### Comparison to HubSpot Model

  - **HubSpot:** Separate objects for Lead (pre-qualification) and Deal (post-qualification). Leads become deals only after qualification via a discovery call
  - **Attio:** Deal object serves both purposes. Deals are created immediately on form submission or account creation, then moved through stages (Intro/Meeting → Qualified → Not Qualified) based on progression
  - **Key difference:** Attio enables earlier funnel visibility and drop-off tracking; HubSpot requires qualification before deal creation, which can miss early-stage insights
  - **Potential challenge:** Assigning meaningful deal values to early-stage form submissions. Solution: Use a minimum contract value for all submissions (as GrowthX does) or use deal stages and filters to report only on "real" opportunities (e.g., exclude Intro stage from revenue forecasting)

---

## Action Items

**Jason Gong (GrowthX)**
- Create "Lead Form Submissions" list in Attio as a person-based list; add table columns for form submission data (e.g., email address, name, company, submission date)

---

## Transcript
**Matthew Fischer:** Hey, Jason.

**Jason Gong:** Can you hear me okay?

**Jason Gong:** Yes.

**Jason Gong:** Hello.

**Jason Gong:** How's it going?

**Matthew Fischer:** Good, good.

**Matthew Fischer:** Great to chat again.

**Jason Gong:** Yeah, thanks for making the time.

**Matthew Fischer:** Yeah, of course.

**Jason Gong:** Cool.

**Jason Gong:** We could probably just jump in.

**Jason Gong:** I was just looking for your help setting up this tool called Default. I think I mentioned it last time, too.

**Matthew Fischer:** Oh, yeah.

**Jason Gong:** Basically, what I'm trying to do is set this up because they haven't released their native integration yet — they keep promising dates and pushing them back. I just need to get this working by calling the API directly to create records. Maybe I could show you where I was having trouble. Basically, I couldn't figure out the JSON format. At a high level, it's a form where you put in your email and it routes you to different places. There are multiple paths, but that's basically the experience.

**Jason Gong:** So for example, this is the email form and, you know, a few routes go to the scheduler and then a few routes go to that like secondary screen just on my screen where it like further tries to qualify.

**Jason Gong:** And what I'm trying to do is just, I guess, you know, at some stages here, I just want to like create.

**Jason Gong:** People and maybe a company.

**Jason Gong:** I'm not sure if companies are auto-created, but create the associated Adio objects that I should create.

**Matthew Fischer:** Yeah, yeah, definitely.

**Matthew Fischer:** And do you want to send this data to Adio only if they book a meeting?

**Matthew Fischer:** Or do you want to send it to Adio regardless, even if they're not qualified?

**Jason Gong:** Because there are a few different paths here.

**Jason Gong:** Yeah, I probably want to send it to Attio in all cases. I'm trying to think if there's a case of an extremely unqualified person. Do you know if Attio charges us per contact? Is there any reason for me not to just send everybody into Attio?

**Matthew Fischer:** No, we don't price based on records.

**Jason Gong:** Great, then I want to send everyone to Attio. What do you recommend as records to create for an inbound lead form like this? Is it people? Is it people and company? Is it other things?

**Matthew Fischer:** I would recommend creating a person and a company. I would recommend asserting them, because they might already exist — maybe they sent you an email at some point and are already in the CRM. Instead of using a POST, I would use a PUT. I'll drop the endpoint into the chat.

**Jason Gong:** Got it.

**Matthew Fischer:** Flip over to the API Explorer box on the right-hand side. If you switch to shell for the language and click the examples dropdown, then click Request Example. This shows how the data is structured, though within Default you can provide custom JSON for the body.

**Jason Gong:** Yeah, I was playing with this. I think by default they wrap it in data already. Let me try to run this and see what happens. Let's test it.

**Jason Gong:** OK, so that one didn't work.

**Jason Gong:** Let's see.

**Jason Gong:** The right.

**Jason Gong:** OK, so you have value and then.

**Jason Gong:** And then you have to choose email.

**Jason Gong:** Do you think maybe I just don't need like this thing?

**Jason Gong:** It's just like that.

**Matthew Fischer:** Yeah, so I'll share I'll drop into the chat.

**Matthew Fischer:** We have details for all the different attribute types, how you need to structure the data when writing to Attio.

**Matthew Fischer:** So the one that I just dropped in is for email address.

**Matthew Fischer:** And if you scroll down to the writing value section.

**Matthew Fischer:** it.

**Matthew Fischer:** t no There's There's

**Matthew Fischer:** You'll see that you can either use email addresses if you're providing multiple email addresses, or you can just write to an email address if you're just providing a single value.

**Matthew Fischer:** So it's in this section down here.

**Jason Gong:** Cool.

**Matthew Fischer:** You click writing to an email address.

**Matthew Fischer:** Yeah, perfect.

**Matthew Fischer:** So that's how you would need to format it.

**Jason Gong:** Okay, so that's it. Let's try again. It's wrapped in values, right?

**Matthew Fischer:** Exactly. And then there's one modification to the URL for the assert call. Within the URL itself, you need to establish a parameter for matching purposes.

**Jason Gong:** Is that in the docs? It seems like it's not mentioned.

**Matthew Fischer:** I don't think you want to put this in the header. You want to add that as a URL parameter.

**Jason Gong:** Oh, I see.

**Jason Gong:** So assert only works for single values? Like, if I wanted to include name as well, and company and all those fields, how would that look? Let me just see if this works first.

**Matthew Fischer:** For the assert, you just have to specify the attribute used for matching. But in the rest of the body, you can include as many attributes as you'd like.

**Jason Gong:** Got it.

**Jason Gong:** I wish there was a way to see what request they're making. But does this error message say anything to you?

**Matthew Fischer:** It looks like formatting within the body itself.

**Jason Gong:** Let me check the request they sent.

**Matthew Fischer:** This is a nitpicky thing, but instead of "value," you might need "values." And click edit.json to double-check. I don't think email address needs to be wrapped in curly brackets — what you have set up with values is already wrapping the whole thing.

**Jason Gong:** Actually, looking at this, it looks like it does need the brackets. Let me see what happens.

**Matthew Fischer:** Have you used something like Postman in the past?

**Jason Gong:** I have.

**Jason Gong:** I don't have a setup here.

**Jason Gong:** I've been trying to use it, but I'm not really sure how.

**Matthew Fischer:** For the matching attribute, in the query parameters below, you can just type in email address. Then in the body parameters, provide email address for the first value. Try pasting that into the JSON editor.

**Jason Gong:** In the Default JSON editor?

**Matthew Fischer:** Yeah. The issue is I'm not sure how to read the payload that Default is showing you. I usually use Postman to make sure the structure is set up correctly, so you can see what the payload actually looks like.

**Jason Gong:** It's their problem, honestly. Let me run this. I'm getting a "cannot find attribute" error.

**Matthew Fischer:** Let me check the documentation.

**Matthew Fischer:** You should be able to double-check the documentation for writing email address values. If you go to your object settings, go to workspace settings, then to objects, then to people, then attributes. Navigate to the right-hand side of the email address attribute and click the three dots to open the menu. Try copying the slug. That's odd — you should be able to write to email address instead of email addresses. Let me structure it properly and drop it into the chat.

**Matthew Fischer:** Format it like this. So this might actually be in the matching app. If you edit the URL, that might have been our issue. You could sort by created date. You might need to remove the filter and type in created date — it'll be the first option. Perfect. And then if you click into your filter.

**Jason Gong:** What am I doing here? No filter.

**Matthew Fischer:** Maybe try doing a hard refresh for the page.

**Matthew Fischer:** And then add back in the sort.

**Matthew Fischer:** And then remove that filter.

**Matthew Fischer:** If you click Clear All Filters at the bottom.

**Jason Gong:** OK, great.

**Jason Gong:** Well, I guess this is a better problem.

**Jason Gong:** I guess I just need to figure out how work with this.

**Jason Gong:** Let's see if we just do that.

**Jason Gong:** It didn't look like the error was the same one that I was getting here.

**Jason Gong:** So I feel like that isn't the issue.


**Matthew Fischer:** And then I think you'll need to modify that, yeah, all right.

**Jason Gong:** I feel like they're literally not just looking at this part, they're not even wrapping the data in like brackets or something, you know, like, yeah, is there a way for, if you go back to the editor, is there a way for you to, if we hop into the, okay, so you have to provide values.

**Jason Gong:** Yeah, I mean, I should talk to them.

**Jason Gong:** mean, clearly it's working in the other thing.

**Andrew Lee:** Maybe just a thought — maybe their body block needs wrapping in data, and then you put values as the nested object in the edit.json. Because in curl, we did data, right? So this one should be values instead of data.

**Jason Gong:** I just thought it auto-wrapped, but I guess I'm wrong.

**Andrew Lee:** That's right.

**Matthew Fischer:** Nice.

**Jason Gong:** Okay.

**Jason Gong:** Wow, that was amazing.

**Jason Gong:** Thank you so much.

**Jason Gong:** No problem.

**Jason Gong:** Okay, cool.

**Andrew Lee:** We just don't know how to use it.

**Jason Gong:** Yeah, I know.

**Jason Gong:** Okay, so we create the people.

**Jason Gong:** So when you do that, does it auto-create the org based on the email domain or anything, or do I just need to do that?

**Matthew Fischer:** Yes, it will auto-create the org based off of the domain of the person.

**Matthew Fischer:** So if you go into Attio and then you go to that test record that you recently created, you might also just be able to search for that record.

**Matthew Fischer:** If you hit forward slash on the keyboard.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** So You

**Matthew Fischer:** You can just do a quick search.

**Matthew Fischer:** I think it was Jason Plus.

**Matthew Fischer:** Yeah.

**Matthew Fischer:** Cool.

**Matthew Fischer:** And you can see if you click to the company tab or that.

**Matthew Fischer:** Yeah, perfect.

**Matthew Fischer:** You see the company is automatically created.

**Matthew Fischer:** In this case, the company was created in the past, but if you just assert a person and they're net new, then based off the domain and email address, money will be automatically created and then enriched if we're able to provide enrichment data.

**Matthew Fischer:** I think the other consideration here is for the responses that you're gathering, I think there's just a decision that you'll want to make with regards to where you want that data to be stored.

**Matthew Fischer:** If you always want that information to be at the person level or if you prefer to add it to the deal that gets created.

**Matthew Fischer:** And I guess there's also a question, like, would you want a deal to be auto-created when that initial meeting gets booked, or would you prefer to just create the deal manually if that first call goes well?

**Jason Gong:** Right.

**Jason Gong:** Right, okay, so this is, I guess, the event.

**Jason Gong:** What's the pattern for, I guess it's an activity.

**Jason Gong:** Is activity like the record, or is it an interaction?

**Jason Gong:** Or no, okay, I guess I'm trying to think, like, when something happens, in this case, like, lead submitted lead form, like, how is that supposed to be tracked?

**Matthew Fischer:** Yeah, so, so what folks will do for a lead like this is they'll set up either a list or an object that they will add.

**Matthew Fischer:** So, we'll create the person.

**Matthew Fischer:** Let's run with the list example.

**Matthew Fischer:** They'll have a list that will be...

**Matthew Fischer:** be...

**Matthew Fischer:** It's Lead Form Submissions.

**Matthew Fischer:** It's a person-based list.

**Matthew Fischer:** And when somebody submits your form, you'll assert the person and then add that person to the Lead Form Submission list.

**Matthew Fischer:** And in that list, you'll have attributes where the information that they've submitted is logged.

**Jason Gong:** Is that a list?

**Jason Gong:** Okay.

**Jason Gong:** I haven't played with lists too much.

**Jason Gong:** I just assumed.

**Jason Gong:** Like, what does it mean to log information in a list, other than the name of the list?

**Jason Gong:** I guess you can see we don't use it at all.

**Jason Gong:** Yeah, so it's...

**Jason Gong:** Lists have, like, additional information.

**Jason Gong:** It's almost like a table, I guess.

**Matthew Fischer:** Yeah, so you can create attributes.

**Matthew Fischer:** You can set up a list and create attributes within the list that you could use to capture information from the Lead Form Submission.

**Matthew Fischer:** And for your case, I would probably just start from scratch, which is at the bottom right, and then make this a person-based list, and call this lead form, yeah, or something like that.

**Matthew Fischer:** Cool.

**Matthew Fischer:** And then you select table, and then call this, like, all submissions.

**Matthew Fischer:** And then you can add columns and create attributes for different pieces of information you're gathering as part of the submission.

**Matthew Fischer:** Okay, this is where it is.

**Jason Gong:** I'll stick here.

**Matthew Fischer:** Yeah, the short explanation is that this is where your submission data lives.

**Jason Gong:** Okay. In my head, I was thinking I could have a submitted lead form event on the person record. But I guess that doesn't really matter. Okay, I do have to hop.

**Jason Gong:** My last question — typically after a discovery call, you create a deal if there's qualification, right? But I notice you create a deal for everything, which seems a little weird to me. Why are intro and meeting deal stages instead of creating deals after some discovery over a call?

**Matthew Fischer:** We follow a similar approach — deals are created as early as possible. Whenever someone creates a workspace/trial account or submits our "Talk to Sales" form, a deal is created and added to one of the first pipeline stages. Then if it's qualified, we move it to a qualification stage. If unqualified, we move it to a not-qualified stage. Instead of a separate lead form list, you could attach form information directly to the deal. From a reporting perspective, this helps you see the drop-off between form submission, actual meeting, and qualification.

**Jason Gong:** In HubSpot, they have a lead object for early-stage prospects before you assign a number. We have a minimum contract amount, so we label even demo requests with a number, which makes our funnel reporting a little weird. Maybe we just need a filter — don't count certain stages unless they reach proposal.

**Matthew Fischer:** Yeah, that's what we do. You have three options: attach the form submission information directly to the person when creating them, send the data to that lead list we created, or attach form data to a deal. I'd recommend either the list or attaching to the deal. All of that can be done through our API.

**Jason Gong:** Okay, got it.

**Jason Gong:** All right, well, thank you so much for the help.

**Matthew Fischer:** Yeah, absolutely.

**Matthew Fischer:** And feel free to reach out if you have anything else comes up with this flow.

**Jason Gong:** That sounds good.

**Jason Gong:** I think a RevOps consultant guy is starting this week.

**Jason Gong:** So I'll probably see him at some point, but thank you so much.

**Matthew Fischer:** Nice.

**Matthew Fischer:** Yeah, absolutely.

**Matthew Fischer:** Cheers, Jason.
