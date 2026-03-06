# Carta Follow Up Call <> GrowthX AI, Inc.

<metadata>
date: 2025-03-06
time: 22:33 UTC
duration: 39 minutes
organizer: bridget@growthxlabs.com
participants: Bridget McGillivray, John Ferreira
fathom_recording_id: 50668804
fathom_url: https://fathom.video/calls/246819004
share_url: https://fathom.video/share/so4CNwWMiGLLBoyGYsZpNEN6o3yq4Qy3
source: fathom
enriched_on: 2026-03-04 15:45 UTC
</metadata>

---

## Summary

John Ferreira from Carta walked Bridget McGillivray through the complete workflow for setting up equity plans and option grants after GrowthX AI's Series A close, including demonstrating the Carta platform's board approval workflows and preferred stock class creation. The team is waiting for the official 409A valuation (expected in about two weeks) before finalizing everything in production, but Bridget will practice in the sandbox environment first. GrowthX AI plans to close its remaining five angel investments this week and will then populate all equity information in Carta once the 409A report arrives.

---

## Context

GrowthX AI, Inc. recently closed Series A funding and is now setting up its post-investment cap table and equity grant infrastructure. This call was between Bridget McGillivray (GrowthX CFO/Operations) and John Ferreira, a Carta implementation specialist, to walk through the end-to-end process for managing equity in Carta — from creating the equity plan and board consents to issuing individual option grants and handling preferred stock for new investors. The relationship is transactional: Carta is the equity management platform provider, and John was providing customer onboarding and guidance. The meeting happened late in the evening for John (Brazil-based, returning from Carnival break) but was essential for getting GrowthX ready to manage equity at scale.

---

## Relevance

- **To GrowthX Delivery:** Post-Series A operational infrastructure. Option grants, board workflows, and equity administration are core post-raise activities that directly impact team retention and cap table hygiene. The Carta workflow includes automated board consents and templates, reducing legal friction.

- **To GrowthX Business Development:** Updated cap table and equity setup unlock investor communications and future fundraising. The 409A valuation (expected March 2025) will be critical for setting fair market value for option pricing. Angel round closing this week alongside Series A means complex equity for multiple investor classes.

- **To GrowthX Finance:** 409A valuation required for compliance. Carta setup will require Certificate of Incorporation amendment to reflect new Series A Preferred share class. Post-close, all equity accounting flows through this system.

---

## Overview

- Carta can be used to create and manage equity plans, option grants, and board approvals efficiently
- GrowthX AI needs to wait for their official 409A valuation before proceeding with full setup
- The process involves creating the equity plan, getting board approval, and then issuing individual grants
- Carta provides templates and streamlined workflows for board consents and approvals

---

## Key Topics

### Carta Setup and Valuation

  - GrowthX AI recently closed Series A funding but hasn't issued option grants yet
  - A 409A valuation is in progress, expected in about two weeks
  - John demonstrated how to add a non-Carta valuation in the system:
      - Used $5.81 as the fair market value per share
      - Set an effective date of February 26, 2025 (placeholder)

### Equity Plan Creation

  - John showed how to create an equity plan in Carta:
      - Upload existing plan or create new one
      - Set plan details like reserve pool size, vesting windows, and plan duration
      - Carta generates necessary documentation, including board resolutions

### Option Grants Process

  - Demonstrated how to create individual option grants:
      - Can be done one-by-one or via bulk upload spreadsheet
      - Includes details like grant size, vesting schedule, and expiration date
  - Explained difference between ISO (for US-based employees) and NSO grants

### Board Approval Workflow

  - Carta facilitates board approvals for equity plans and option grants:
      - Creates board consent documents
      - Notifies board members for electronic approval
      - Automates grant issuance upon full approval

### Preferred Stock Setup

  - For investors, new share classes (e.g., Series A Preferred) need to be created
  - Requires updated Certificate of Incorporation from Delaware
  - John demonstrated how to add new share classes and issue preferred shares in Carta

---

## Action Items

**Bridget McGillivray**
- Practice creating equity plan & grants in Carta sandbox env. Use replace_app_with_sandbox hack.
- Remove business legal partners' access from Carta production environment
- Obtain 409A valuation report from valuation provider
- After receiving 409A report, upload equity plan, board approvals, and option grants to Carta

---

## Transcript

**John Ferreira:** Camino.

**Bridget McGillivray:** Wow, late.

**Bridget McGillivray:** Do you normally work this late?

**John Ferreira:** Yeah, it's usually I'm leaving around this time, but you know, we just got back from an out-of-office period — Monday, Tuesday, Wednesday — returning today.

**Bridget McGillivray:** Over Carnival?

**John Ferreira:** Yes, exactly.

**Bridget McGillivray:** The day after Carnival, everybody's at work.

**Bridget McGillivray:** I've been to Rio, but I've never been during Carnival.

**John Ferreira:** I went in the summer.

**Bridget McGillivray:** It's on my bucket list.

**Bridget McGillivray:** So we got our Series A funding in the bank, which is great, but we have not yet done the option grants. So I was wondering if it makes sense for us to even chat today or wait till I have everybody's option grants and we can load everybody in.

**John Ferreira:** We can use Carta for this. So you don't have to make everybody sign, and then accept everything again electronically when we do Carta. Let me share my screen with you real quick because there's a couple of things I want to show you. So you guys have the 409A and then some numbers from a different source, right? How's that coming along?

**Bridget McGillivray:** Yes, the report itself is not ready. We should have it in like two weeks.

**John Ferreira:** They gave us numbers so we could do the cap table and things like that, but not the full report. We'll need a report from them. The reason is the FBE within the platform uses that price for the option grants. If you have that price, we can put a placeholder temporarily in Carta and update it later.

**Bridget McGillivray:** So which price do you need?

**John Ferreira:** Whatever they gave you as a fair market value per share.

**Bridget McGillivray:** I have a post-money enterprise value and a post-money equity value. I'm not sure if I'm using the right terminology.

**John Ferreira:** It's the equity one. Give me a second.

**Bridget McGillivray:** I'm just going to copy-paste it in the Zoom chat.

**John Ferreira:** Okay.

**Bridget McGillivray:** The post-money enterprise value is $5.81 per share.

**John Ferreira:** That's the stock price. Do you have a different one?

**Bridget McGillivray:** No, that's the per-share value.

**John Ferreira:** Fair market value is $5.81. Let me show you what I'm doing. So usually in Carta, you go under Finance and Evaluation, then Manage Valuations. I'll add a non-Carta valuation.

**Bridget McGillivray:** Is the valuation provider on your list?

**John Ferreira:** I don't see it. Is it a niche firm?

**Bridget McGillivray:** Yes, I don't think it'll be on your list.

**John Ferreira:** That's okay, I'll just go with "Other." And then I'll enter the price: $5.81. I need an effective date.

**Bridget McGillivray:** Can we change this later if I get it wrong?

**John Ferreira:** Yes.

**Bridget McGillivray:** Can you use February 26th for now? I think that's right, but I can change it later.

**John Ferreira:** Sure. As a placeholder, down here in the future, when you need to change it, just click the three dots and do the modifications.

**John Ferreira:** Now, let's talk about option grants. We start with the umbrella — the equity plan itself. We'll upload your existing plan, associate it to the share class, create a reserve pool with the number of shares, effective dates, and some windows for people who get terminated. Then we create equity awards and draft options. The plan is one thing, and another thing is the forms — form of option agreement and form of activities agreement. If you weren't using Carta and needed to grant someone options, you would fill out these forms and the employee would accept by counter-signing. Every time they vested and wanted to purchase shares, they'd fill out the exercise forms, send you payment, and you'd send back a share certificate. With Carta, we just use the templated forms and attach them to the awards electronically. There's no need to do this manually.

**Bridget McGillivray:** Can we just use the Carta templates?

**John Ferreira:** Yes, we can use Carta's templates. And I'll show you equity plans. This is a copy of a plan.

**John Ferreira:** What is the size of the option pool?

**Bridget McGillivray:** Number of shares or percentage?

**John Ferreira:** Number of shares. For the example, we don't need the number yet, but I'll put one share here.

**John Ferreira:** These are windows for when people leave, depending on the termination type. They have these windows to make a decision after they leave. And these are plan duration settings. Each award will have its own duration as well. The repurchase period is zero and can't be modified. The logic is if you leave today and have vested shares, the company has the right to repurchase them on the termination date. You don't have to wait.

**Bridget McGillivray:** So those things we cannot edit?

**John Ferreira:** No, these core parts you cannot edit. It seems standard.

**John Ferreira:** Carta will generate necessary documentation, including the plan document. Plus you can compensate people with restricted stock. These are the options. Carta will push you to do a board consent to approve the plan which is in draft and associate it with your cap table. So my goal here is that you can do this by yourself eventually. Essentially, Marcel and I come up with the terms of the plan, we talk to counsel, we enter all the info for our plan which generates a board resolution, the board signs it, and then the next step is individual grants. Let me show you how it looks in demo.

**John Ferreira:** Let's check the plan first. We have the reserve here — this is the size of the pool and the availability of how many shares we can compensate people with. And then we go to Equity Award Option Status. The dashboard shows all the option grants. You click on the label and it pops up the employee name, outstanding deposit status (meaning valid), total quantity granted, how many shares they've purchased so far, exercise price, and information from the equity plan — name of company, name of plan, and when it was printed and approved.

**Bridget McGillivray:** Can you do a bulk upload, like if we have a board meeting and approve 20 people at once?

**John Ferreira:** Yes, you can download a spreadsheet, fill it in, and upload it. The main thing is, you go to Draft Options. If this is a new thing and you want a board consent, we can help with that. You just go New Option and it will ask if you need to create a board consent.

**Bridget McGillivray:** So first we decide on what we want the option plan to be — expiry, things like that. Then we have the board approve the plan itself. Once the plan is approved, we issue all the grants and the board approves all the individual grants as well?

**John Ferreira:** You can do it in one board session if you want to approve both the plan and the grants together.

**Bridget McGillivray:** Yeah, I saw templates for that. Then in one board session, we could approve the plan and the grants. And then you produce the legal documentation in Carta and we download those documents, bring them to the board, sign them, and put them back in Carta?

**John Ferreira:** Exactly. Let me check where your company is incorporated. It's Delaware, so it should allow me to do this. Let me show you the whole workflow. Add plan, create new plan.

**John Ferreira:** I'll create a draft and draft board consents.

**Bridget McGillivray:** Everything is in here?

**John Ferreira:** Yes. These are the board members already invited through the platform. You can give it an expiration date and customize the notification they will receive. Then you can publish and people will approve. The board members will go one by one.

**Bridget McGillivray:** So they get a notification in Carta and it's done in there?

**John Ferreira:** Yes, exactly. It's going to be on tasks. They just approve and that should work. You can do offline approval too. Once everybody approves, all the documentation is here. Now we're good to go with equity awards. Draft options, new option. If I need a board consent, I create a draft. Once the board consent is approved, it creates the individual grants automatically. So I'll use the spreadsheet to bulk upload. You can fill it in and upload it.

**Bridget McGillivray:** Can the grants be backdated?

**John Ferreira:** Yes, you can backdate them. The expiration date should come from the board approval. Let me show you: is this an ISO (Incentive Stock Option) or NSO (Non-Qualified Stock Option)?

**Bridget McGillivray:** So we could also grant angel investors here and they would just be called investors?

**John Ferreira:** Yes, but ISO type can only be issued for people who live in the US and have an employment relationship with the company. If anything different from that, it should be NSO.

**John Ferreira:** I'm showing you this, but I don't expect you to remember everything. Once I complete the draft, I get a summary showing the plan information and a table. Then it triggers notification to the board and they click Yes in Carta. Once the board approves and everything is fully approved, it gets sent out automatically. So to recap: we post the valuation, we create the plan, we draft it, drag everything through the board approval if we want to use Carta for it. Every time we need approval, we create the board consent and return to the workflow. Once everything is in place and the board members approve, everything powers forward as you create things within the platform.

**John Ferreira:** My hack for you: it's always "replace app with sandbox." You have access to it. It resets every day by midnight PST. You can play around with real data without it shooting messages to anyone. The only people who can see it have the same access level as you.

**Bridget McGillivray:** And I can practice and try it myself. Do companies often give their lawyers access to Carta?

**John Ferreira:** Yes, they do. But if you have a specific person or firm, you can go to Company and add them with full access or editor access if they just need to review.

**John Ferreira:** Congratulations on your Series A, by the way. I know it's hard. When it comes to investors, you probably have people who bought shares from your preferred class. In order to reflect that in Carta, we'll need your Certificate of Incorporation from Delaware, which will need to be amended because you only have one class right now and now you have preferred. You'll get a new version from the Delaware Secretary of State, and I can upload it to Carta. I'll go to Manage Your Classes, Update Class, New Finding, and upload the document. Carta will read the documentation and create a table similar to this one, but now you'll have a Preferred class like Series A. Then you can set the conversion ratio (usually 1 to 1), dividends, and other rights. Once the new class is set up, you'll go to Draft Shares. Carta will pop up an interface where you enter the investor name, email, relationship, entity type, preferred class, quantity, price per share, currency, dates, and any legends. Law firms tend to put legends all over the place in preferred stock docs, so I just search for the word "legend" and grab every piece, then build one legend for all the preferred investors and put everything here. Once we're done, you log off and Carta will tell you what's missing. Let me know if you have availability and we can do another hour. Once everything is in the right place, we can move faster, but let's take our time to review everything.

**Bridget McGillivray:** No, I'm going to watch this again. I'm not sure if I'll be comfortable uploading everything until we have the actual 409A, which I'll hopefully get next week and then I'll be ready.

**Bridget McGillivray:** And we're closing all of our angels this week. The VC came in, but we're doing the angels this week, then I can do everybody after that.

**John Ferreira:** Did you do anything via crowdfunding?

**Bridget McGillivray:** No.

**John Ferreira:** And it's just one VC firm?

**Bridget McGillivray:** Five angels. It'll be easy.

**John Ferreira:** Yes, it will be. I do it all the time. It's straightforward. For me, it's just a matter of coffee and moving through the platform.

**Bridget McGillivray:** Thank you very much. I will definitely watch this again and try it myself. But I'll let you know if I need help. Thanks for taking the call.

**John Ferreira:** No problem. I apologize because I saw your note asking about yesterday. Something went wrong on our end, but I'm sorry.

**Bridget McGillivray:** Don't worry. It's all good.

**John Ferreira:** Awesome. Okay, see you soon.

**Bridget McGillivray:** Yeah, when you can jump into a quick call again, I appreciate it. Bye.

**John Ferreira:** No problem.
