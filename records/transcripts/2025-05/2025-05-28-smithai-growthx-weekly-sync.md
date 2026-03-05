# SmithAI <> GrowthX Weekly Sync

<metadata>
date: 2025-05-28
time: 17:34 UTC
duration: 25 minutes
organizer: elvis@growthxlabs.com
participants: Elvis Goren, Maddy Martin, Mara Leighton, Volodymyr Popovych
fathom_recording_id: 65177810
fathom_url: https://fathom.video/calls/310969939
share_url: https://fathom.video/share/KsKVWy1ysAQ1bgVWj69thGJx1J5x1Gvm
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

GrowthX and Smith.ai discussed the MVP strategy for interactive invoice and incident report templates on Smith.ai's website, with a focus on printable 8.5x11" PDF formatting and email delivery. The team aligned that the MVP should prioritize design polish (consistent spacing and alignment) and a working "send to email" flow for blank templates, rather than attempting to capture and format filled-in forms. Elvis will create the PDF templates and draft the MVP proposal, while Volodymyr will research Webflow-compatible plugins for PDF generation and email functionality.

---

## Context

Smith.ai is a client of GrowthX working on home services industry templates. They're building out reusable invoice and incident report templates as interactive web tools on their site, initially targeting HVAC, General Contracting, and Legal verticals. This meeting was a working session to align on the technical implementation approach with Smith.ai's product lead (Maddy Martin), GrowthX's design and implementation leads (Elvis Goren and Mara Leighton), and a technical partner (Volodymyr Popovych) to evaluate feasibility and constraints around PDF generation, email delivery, and printability within the Webflow platform.

---

## Relevance

- **To GrowthX Delivery:** Smith.ai engagement demonstrates template-based product expansion across multiple verticals (HVAC, General Contracting, Legal). Technical constraints around Webflow's server-side limitations (PDF generation, email sending) require external tools like Zapier, informing future implementation strategies for similar clients.
- **To GrowthX Business Development:** Smith.ai is expanding template offerings beyond the initial invoice and incident report, indicating strong product-market fit and potential for future scope expansions. The collaborative approach with Elvis, Mara, and technical partners shows healthy client relationship and room for additional service work.
- **To Smith.ai Account Health:** Project is in active development phase with clear MVP definition and role clarity. Design polish and printability are key quality drivers; design QC (especially spacing/alignment on incident details) must complete before functionality is wired up.

---

## Overview

- MVP approach: Separate dedicated page (smith.ai/templates/home-services/invoice) with printable 8.5x11" PDF templates. Users can interact with templates and email blank/fillable PDFs to themselves via popup modal. Data capture and server-side processing handled via Zapier integration.
- Design polish required: Fix spacing/alignment inconsistencies in incident report (white space gaps between fields, uneven column widths). Template must preview exactly as it will print.
- User experience: Playable templates with clear disclaimer explaining they're experimental. Options for export as PDF, email link, or bookmark. Future phases could support saving customized versions.

---

## Key Topics

### PDF Template Design and Printability

Maddy emphasized that the PDF must be perfectly printable at 8.5x11" standard paper size, with the web preview matching the printed output exactly. The current incident report has spacing inconsistencies (uneven gaps between field labels, misaligned columns for "Missed," "Incorrect," "Other") that must be fixed before implementation. Text input fields need constraints to prevent overflow when printed. The container's aspect ratio should match 8.5x11" dimensions so users see exactly what will print.

### Design Polish as MVP Blocker

The team identified design QC as the highest priority: consistent spacing throughout the incident report, aligned columns, professional formatting, and clear visual hierarchy. Maddy flagged specific issues with sales tax formatting and multi-line descriptions (project description should be limited to one line to ensure clean printing, like a watch repair ticket).

### Interactive vs. Fixed Template Strategy

Maddy proposed a two-tier approach: an interactive playground version where users can experiment (with a disclaimer), plus a fixed template version optimized for printing. This avoids confusion from users filling it out, submitting, and receiving a blank PDF instead. Future phases could allow customization and saving.

### Implementation via Webflow + Zapier

Volodymyr identified that Webflow cannot natively handle PDF generation or email sending (no access to external libraries). Zapier is the simplest solution to handle these server-side processes. The team needs to identify Webflow-compatible plugins for the PDF generation, email, and print functions before finalizing the implementation approach.

### MVP Scope Definition

The MVP is scoped to: separate dedicated page (smith.ai/templates/home-services/invoice), fillable invoice and incident report templates at 8.5x11", ability to "send to email" via button (could be pop-up modal for email capture), and automatic delivery of pre-created blank template PDF. The interactive playground with customization and dynamic PDF generation is post-MVP.

---

## Action Items

**Elvis Goren (GrowthX)**
- Conduct design QC check. Fix alignment/spacing issues in incident report (white space gaps between fields, column width inconsistencies). Ensure professional polish before implementation.
- Create 8.5x11" printable PDFs for invoice and incident report templates. Verify design quality and print output. Target: next week.
- Draft MVP proposal with Volodymyr. Define what users can do, how output is formatted, and delivery method. Clarify "send to email" vs. "save" vs. "print" functionality. Collaborate async on tech implementation.

**Volodymyr Popovych**
- Research Webflow-compatible plugins for PDF generation, email functionality, and print. Recommend options that work within Webflow's constraints. Collaborate async with Elvis on implementation approach.

---

## Transcript
**Volodymyr Popovych:** After doing my research, I think the simplest way would be to have some kind of a Zapier integration set up that will handle all those steps.

**Volodymyr Popovych:** There are other ways, probably we could create like a whole custom application, but I'm just not really sure if that's something that is really required for this project.

**Volodymyr Popovych:** But I guess I'm curious, how, like, where do you want this form to live?

**Volodymyr Popovych:** Like how many blog posts do you think it will be posted on?

**Volodymyr Popovych:** Or is it something that will appear frequently on the website or is it just one blog post?

**Elvis Goren:** Yeah, the idea was for it to appear frequently.

**Elvis Goren:** So we would, this is like basically the trial run and like we have the invoice, an incident report, and then we're expanding to other topics and to other kind of businesses.

**Elvis Goren:** So like for HVAC companies or for legal or for whoever, whichever.

**Elvis Goren:** Yeah, so I see your issue with the server side.

**Elvis Goren:** Is there not a way like the SMTP set up to enable that?

**Elvis Goren:** Is the problem the email delivery or is the problem the conversion to PDF, just so I can understand?

**Volodymyr Popovych:** Yeah, kind of both, kind of both, because like there is no way for me to connect to any sort of outside library to handle those processes in Webflow.

**Volodymyr Popovych:** So we have to do that outside of Webflow in some other way.

**Volodymyr Popovych:** And I just figured that Zapier would be the easiest solution here.

**Volodymyr Popovych:** Another thing I was curious about is the PDF template, basically.

**Volodymyr Popovych:** Like, how do you want that PDF to look?

**Volodymyr Popovych:** And I saw in the Notion doc, I saw there was this one HTML file with four...

**Volodymyr Popovych:** It's kind of has some styling issues, minor styling issues still, and also I saw the forms that you guys embedded in Webflow, so they look like a basic, basic forms to me, and I just, I was just curious, what's the final result you want to achieve?

**Elvis Goren:** So, for the invoice, so, okay, there's three there, the invoice, maybe it'd be easier to put up while I'm talking, for the invoice, essentially, people can fill it out on that page, and then we want to be able to obviously PDF that in a letter format, so that it's like, it's printable, right?

**Elvis Goren:** Like, that's another question that I had — we want to be able to send it to them, not just a huge PDF that doesn't meet the sizing requirement.

**Elvis Goren:** It has to be able to be printable, and basically it also acts as an email capture, right?

**Elvis Goren:** So does that kind of answer the question?

**Volodymyr Popovych:** Is there a specific template that you want to follow for the PDF files?

**Elvis Goren:** What do you mean by...

**Volodymyr Popovych:** Like just how do you want all the form submission data to be displayed?

**Volodymyr Popovych:** How do you want it to be formatted?

**Volodymyr Popovych:** A PDF.

**Elvis Goren:** The invoice should be...

**Elvis Goren:** I'm not sure I understand the question, but the invoice should just look like a PDF invoice, right?

**Volodymyr Popovych:** Okay, just like the basic invoice, nothing extra fancy.

**Volodymyr Popovych:** I'm just curious about what steps I will need to take to generate the PDF, you know, and if it's just like the simplest way to display the...


**Volodymyr Popovych:** The data in, like, the simple invoice style document, then it's okay.

**Volodymyr Popovych:** I was just curious — maybe it was supposed to be some other PDF styling.

**Elvis Goren:** I don't know how the styling would change after PDF conversion. Essentially, if you want it to look like the current version, it could have fillable fields, but that's an extra step.

**Elvis Goren:** I think the idea is for them to fill it out on the page.

**Maddy Martin:** I mean, the goal is that there's a template that they can use and they can send it to themselves via email, so it would have to be a formatted email.

**Maddy Martin:** That says, you know, here's the Smith.ai, you know, here's the whatever home contractor invoice that you requested from Smith.ai, or check out this invoice from Smith.ai, right?

**Maddy Martin:** And, and there's plenty of sort of like bootstrapped or, you know, regular templates for that, that I see all over websites, you know, all the time.

**Maddy Martin:** For example, I booked flights today, and a really good example of like, when you book a flight, you can PDF or email your receipt or your itinerary or any of that stuff, right?

**Maddy Martin:** So like, that's a familiar format.

**Maddy Martin:** But I'm, I like the idea of doing it as an editable one.

**Maddy Martin:** I think the shortest MVP is that you can have your results PDFs emailed to you in some sort of acceptable format. The next step could be getting this into a blank template or an editable template that can be sent to you.

**Maddy Martin:** But, yeah, I think it's very helpful to be able to play with it and send it to yourself.

**Maddy Martin:** What people actually want is to save the PDF template in a few different ways. For example, I could set rows and fields the way I want them and export it. Or set a price per unit and export it with write-in fields for quantities and customer names. Or save it as a bookmark to return to. Or export as a customized PDF. Or fully edit it. There are three variants I see, but we don't have to launch with all three at the same time.

**Maddy Martin:** It just depends on how easy it is to update once we've launched v1 of it.

**Maddy Martin:** Can we go back and do v2 across the board?

**Elvis Goren:** Yeah, I guess one of the options that were kind of in what you said was like, just have them save because then that eliminates the SMTP call, like the actual email call, but then we don't get the email, right?

**Elvis Goren:** Right.

**Elvis Goren:** So, so I think ideally it's like save it in the same formatting, same design.

**Maddy Martin:** I think we have to solve it, but I'm not saying that it has to be like the number one thing that we solve before we actually launch it.

**Maddy Martin:** Like what is the MVP is the real question.

**Maddy Martin:** And to me, it's being able to share either download or email the thing that I played with.

**Maddy Martin:** Right.

**Maddy Martin:** And, and then there's some sort of like data capture, I don't know how hard that is.

**Maddy Martin:** So I sort of, you know.

**Maddy Martin:** I look to you three to tell me how hard is it, what's possible, and we might not be able to solve it on this call, but maybe async with a little bit of digging and work, you know, we can figure it out.

**Elvis Goren:** I think another potential option could be, okay, so they can play around with it, maybe they don't fill it out fully, and if they hit the submit, we just have an auto email that we've already created the PDF, like we've turned the HTML into a PDF on our end, and if somebody submits through this specific form, we'll just send them an empty fillable PDF, and that could be like the MVP, and then the next step, of that is, they'll actually fill it out, and they'll receive, do you know what I mean, does that make sense, what I'm saying?

**Maddy Martin:** Yeah, yeah, I mean, so basically what you're saying is, I get to play with it, but not save anything, inside of the, and we can talk about whether or not it's really going to live on the blog, because.

**Maddy Martin:** I feel like it should be vol, like, smith.ai slash templates slash home services slash invoice or something, right?

**Maddy Martin:** Like, you know, like, home services invoice template, right?

**Maddy Martin:** Like, it sort of needs its own section because on the blog, like, there's such a big right rail that the experience sort of is, like, all shifted to the left.

**Maddy Martin:** Like, sort of want it to be the main thing that I see, and we probably are going to want, like, a lead capture form on there at some point, and there's just no room.

**Maddy Martin:** So I would rather, you know, that we reconsider that possibility.

**Maddy Martin:** The other thing is there's too narrow of a space on the left side of the blog to do an 8.5 by 11 page paper.

**Maddy Martin:** Like, those dimensions don't fit on the blog.

**Maddy Martin:** So, like, that's...

**Maddy Martin:** Not going to be an eight and a half by 11.

**Maddy Martin:** So we have to think about someone actually printing this off.

**Maddy Martin:** Like if we're going to email them the blank PDF, the first thing I'm going to want to do is to print it and bring it to my job later this afternoon.

**Maddy Martin:** Right.

**Maddy Martin:** So.

**Maddy Martin:** I don't want to take this too far.

**Maddy Martin:** Like we don't even know if people are going to use it, but I want it to be plausible and like it's not plausible.

**Maddy Martin:** If it's too long and too narrow and like someone with a regular printer, which we know everyone's got an office with invoices.

**Maddy Martin:** So they definitely have a printer.

**Maddy Martin:** Like, how are they going to print that off?

**Maddy Martin:** So I would I would make sure that the page breaks nicely, that it prints perfectly at like eight and a half by 11.

**Maddy Martin:** And we might need to make some little adjustments there.

**Maddy Martin:** But no matter what we do, it's always going to be something that we want printer friendly.

**Maddy Martin:** Right.

**Maddy Martin:** And printer friendly means it has to fit in eight and a half by 11.

**Maddy Martin:** And the easiest thing for us to do is to have the frame look exactly like it's going to print.

**Maddy Martin:** So if it's eight and a half by 11, like the proportions of the sort of container that it's in on the web page should be those dimensions too, right?

**Maddy Martin:** So whatever aspect ratio eight and a half by 11 is, like that's sort of the frame that I expect to be on the site.

**Maddy Martin:** And then obviously, you know, on mobile, you know, you're zoomed in or whatever.

**Maddy Martin:** But I really think that that's important.

**Elvis Goren:** Yeah, I guess the MVP that I proposed is, I don't know if it's going to cause frustration.

**Elvis Goren:** Like, are they going to get confused that they're going to fill this thing out and when we send it to them, it's not actually the thing they filled out, right?

**Elvis Goren:** Like, I'm trying to...

**Maddy Martin:** I think that we just have a disclaimer at the top that says, like, this is all for you to experiment with.

**Maddy Martin:** Um, and you can, you can play with it.

**Maddy Martin:** I mean, we, and then you can send it to yourself as a...

**Maddy Martin:** template to use fully, right?

**Maddy Martin:** Like, this is just a play space, and that's, you you guys can copyright for that, but when we're ready, we can say, okay, you can save, you know, your actual results, but if people are going to want to customize it, or they're going to want to, you know, scratch certain things out, or, you know, also we need to make sure that, like, if there's going to be actually placeholder text on some of these things, like, does that get printed or not?

**Maddy Martin:** Like, we have to make all those decisions.

**Maddy Martin:** So, I think a lot of this actually can be hashed out, like, async, but I would say, like, what I see on my screen is what I want to see printed, and I don't want, like, lines wrapped differently on a printer.

**Maddy Martin:** It should be, like, if I'm previewing a PDF, that's how it's going to print.

**Maddy Martin:** It should sort of be that way, like, on my screen.

**Maddy Martin:** Yeah.

**Elvis Goren:** Well, guess the logical next step would be just...

**Elvis Goren:** Convert these into a printable PDF and then implement on page and then people can go and test it out and then set up a submit button for the specific page.

**Elvis Goren:** So we know that and potentially have an automated email that we include that PDF.

**Elvis Goren:** Yeah, I don't know what submit means.

**Maddy Martin:** I mean, it's not really submit because they're not submitting anything to us.

**Maddy Martin:** Right.

**Maddy Martin:** But so I think we need to, like, get that right because it's not really submit.

**Maddy Martin:** It's almost like we need those.

**Maddy Martin:** We need this space on the right side instead of all the navigation items.

**Maddy Martin:** It needs to say, like, and this, you know, to my email or, you know, print PDF or whatever, you know.

**Maddy Martin:** So I think that if you guys can come up with what that looks like, just a few basic things and maybe it follows you as you go down the page.

**Maddy Martin:** I don't know.

**Maddy Martin:** But that plus, like, the aspect ratio fixing, there's a few things that we need to work on.

**Maddy Martin:** And I think we could use the width.

**Maddy Martin:** I mean, you can see here, like, there's still things that are misaligned, right?

**Maddy Martin:** Like, if we go to incident details, like, there's, like, two, and then there's three, and then there's other.

**Maddy Martin:** And you can see that the width difference between missed and incorrect is different than incorrect and other.

**Maddy Martin:** Like, those gaps are not the same.

**Maddy Martin:** And other could definitely fit on the right if scheduling error was moved up.

**Maddy Martin:** Like, it's just, like, not really cleaned yet still.

**Maddy Martin:** So that needs to be solved.

**Maddy Martin:** Like, there's a little bit of work here that needs to be done still.

**Maddy Martin:** And that level of polish is something I've given you guys feedback about before.

**Maddy Martin:** So, like, that spacing, like, your designer needs to get all of that right.

**Maddy Martin:** Even if you look at the box above incident description and the words incident description, the gap differs. If you look at "client expectation" and "actual outcome," the white space above those lines of text differs as I go down.

**Maddy Martin:** Like it can't be like that.

**Maddy Martin:** It has to be really consistent.

**Maddy Martin:** You see what I'm saying? The white space gaps above "actual," "client," and "incident" are inconsistent — wider and narrower variably.

**Maddy Martin:** That's not clean work.

**Maddy Martin:** So the designer needs to get all this stuff clean, and then we can talk about printing it.

**Maddy Martin:** But let's assume they're going to do that.

**Maddy Martin:** Everything's really tight.

**Maddy Martin:** And then bold, question is, what is a plugin that Webflow will accept, knowing that GrowthX is going to figure this out, and

**Maddy Martin:** And it's going to be in like a frame or something.

**Maddy Martin:** The way that I just buy, you know, a plane ticket and it allows me to print my receipt, like, you know, it's sort of that sort of frame.

**Maddy Martin:** Okay.

**Volodymyr Popovych:** Well, the question I have is probably right now what we have here, these couple form blocks, this doesn't look like a regular invoice would look, you know.

**Volodymyr Popovych:** This is an incident report, but yeah, exactly.

**Maddy Martin:** So this is a different thing, right?

**Maddy Martin:** On a Smith.ai page, you know, it's, and maybe it's not interactive, you know, with the blank template, but we have an interactive one as well.

**Maddy Martin:** The interactive version with big boxes where you can write a million words will break your PDF. We need to run through the whole scenario with Elvis: I'm a user, I go in, I want to print, I write 500 words in a box — what does it look like when I print it?

**Maddy Martin:** Like, these are the things that I think that you guys can be testing in between our calls.

**Elvis Goren:** Yeah, that's the only one, the very extensive one with the multi-step.

**Elvis Goren:** That's the only one that I don't have 100% good implementation thoughts on.

**Elvis Goren:** The other ones are fairly straightforward. If this lives on a new page, we can make it 8.5x11.

**Maddy Martin:** If we go to the invoice, you could add items. If you add a bunch of items, you still need to print it. The question is, does the footer still show up on page two? These are things we need to consider. Maybe you can't add too many items until we figure it out. Last week I flagged the sales tax formatting — it still looks wrong. The spacing around sales tax and comma separator needs work.

**Elvis Goren:** I just pulled this one from the library — I apologize for showing that version.

**Maddy Martin:** You've got project description here. I would limit that to one line. If you want a simple thing to print, think of a watch repair ticket — limited lines, abbreviations as needed. There's a separate playground version if you want to experiment. But the fixed template is the one that prints nicely, and you can email yourself the link. If you want a PDF, you have the more fixed template.

**Maddy Martin:** We need to think about what's good. If someone prints something ugly and says it's from Smith.ai, it looks bad. We're not going to be happy.

**Mara Leighton:** Our takeaways are: Priority 1, ensure seamless user experience on the site with everything aligned nicely. Share with our designer for final QC to ensure everything is tight. Priority 2, make sure it looks nice in printed form or PDF. Those are the top two priorities. Any lingering implementation questions, Vol? We're at your disposal. We're always available now that we have a sense of what this should look like.

**Mara Leighton:** We can keep you in the loop, Maddy, as much as you want, but we can also work with you, Vol, on a continual basis like async if there are some collaboration needs to happen beyond the conversation today.

**Volodymyr Popovych:** Okay, now, I guess I just want to understand what the MVP here would be.

**Volodymyr Popovych:** And as I took it, it's probably we have a separate page with a fillable invoice that people can fill out.

**Volodymyr Popovych:** They can control P it and print it to their printer.

**Volodymyr Popovych:** And if they will also have a possibility to send an empty template to their email.

**Maddy Martin:** I think we need to define that. What I was just saying — you can't rely on control P (browser print).

**Maddy Martin:** That frame needs to be printable and emailable. The email is probably just a link to that page. We need to define what will print nicely. The PDF might be emailed or printed. The template needs to save as a PDF nicely based on what we allow users to change. Once you have a PDF, users can email it themselves. These are business owners, not people borrowing computers at a library.

**Maddy Martin:** I think we need to zoom out. Elvis, let's have a clear plan of attack. What will we allow users to do and why? How do we get the right format? How do we get it to them? Don't worry about email capture right now — we can tackle that later.

**Maddy Martin:** But do we need, like, a form functionality, Like, you know, is there a plug-in that is going to be an, you know, email print, you know, the little buttons that we can plug into this page?

**Maddy Martin:** Like, that's really what I would like you to figure out, Vol.

**Maddy Martin:** Like, what can we recommend to GrowthX that is compatible with our site?

**Maddy Martin:** Like, and then GrowthX, like, you know, your job is to figure out, you know, what does Ready look like and what are we asking Vol to work on?

**Maddy Martin:** With those buttons that he's going to find that are compatible with our site.

**Maddy Martin:** Like, what are we asking him to wire up for those buttons?

**Elvis Goren:** The clear action is: first, create those PDFs and ensure the design is good — 8.5x11" for invoice and incident report. We need to provide PDFs by next week. Then the only step after that is creating a unique form button (not submit, but "send to yourself") on the page. When they click it, it automatically sends the blank PDF we've already created. That's the MVP.

**Maddy Martin:** It could be a pop-up modal or any number of things. You two can work out those details offline and come up with a proposal for what the MVP looks like.

**Elvis Goren:** Yeah, I agree. Sounds good to me. Thanks for your time, guys. Pleasure to meet you. We'll be in touch.
