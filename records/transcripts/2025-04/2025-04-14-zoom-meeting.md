# Zoom Meeting

<metadata>
date: 2025-04-14
time: 14:56 UTC
duration: 31 minutes
organizer: Marcel Santilli (santilli@fwd.digital)
participants: Marcel Santilli, Ericksson Abad
fathom_recording_id: 57105552
fathom_url: https://fathom.video/calls/276662742
share_url: https://fathom.video/share/izFGTKGCTFkDyVkvErwpoPuFxhjkEAxA
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Marcel Santilli and his accountant Ericksson Abad reconciled significant discrepancies between tax preparation (QuickBooks and prior accounting), and Marcel's actual transaction records (Airtable and bank account exports). The core issue: prior tax calculations used accrual-basis revenue ($1.4M) rather than cash basis ($1.141M), inflating taxable income by approximately $300k. They agreed to adjust the revenue downward, reinstate home office deductions ($30k), and apply Section 179 accelerated depreciation for a vehicle purchase ($110k), arriving at an estimated taxable income of roughly $200k for 2024 after adjustments and pending verification of expense categorizations with their tax preparer.

---

## Context

Marcel Santilli is building a consulting business through an LLC structure and recently incorporated a C-Corp to separate business entities. He has been using Airtable as a "gut check" to verify transaction categorization and completeness against QuickBooks. Ericksson Abad is Marcel's bookkeeper/accountant who maintains both the QuickBooks records and reconciles them with actual transactions from business checking and credit card accounts (primarily Chase 5042 credit card and a business checking account). The prior tax preparation (via API Accounting, with involvement from Anderson Tax and Riot as final preparer) created a significant mismatch: their calculations removed ~$500k in expenses and added ~$300k in income that Marcel believes doesn't reflect actual cash basis transactions, resulting in an unexpectedly high tax liability. This meeting focused on understanding the discrepancies and adjusting the tax calculations to align with real transactions.

---

## Relevance

- **Tax Planning & Accuracy:** Revenue adjustment from $1.4M (accrual) to $1.141M (cash basis) will significantly reduce 2024 taxable income; decision to recognize post-asset-transfer revenue to the C-Corp rather than the LLC further reduces LLC's burden. Section 179 depreciation on $110k vehicle purchase and reinstatement of $30k home office deduction are critical deductions to maximize legitimate tax-reduction strategies.

- **Accounting Operations:** Recurring gaps found in QuickBooks vs. actual transactions (e.g., only handful of gas expenses coded vs. 50 actual transactions in Airtable, Nadia's credit card transactions missing entirely) indicate process breakdowns in transaction import or manual coding. Need to audit and standardize categorization methodology to prevent future discrepancies.

- **Financial Forecasting & LLC/C-Corp Split:** The decision to split revenue recognition at the asset-transfer date (January 2025) between LLC and C-Corp requires clear retroactive adjustments to 2024 numbers; future operations will be C-Corp, so LLC's 2024 tax burden is a one-time event that should be minimized through legitimate deductions.

---

## Overview

- Revenue recognition needs adjustment from $1.4M to $1.141M (cash basis)
- Significant expenses were removed (\~$500k) and additional income added (\~$300k), explaining the unexpected tax increase
- Estimated taxable income around $200k after adjustments, subject to verification
- Home office and vehicle depreciation need to be properly accounted for

---

## Key Topics

### Revenue Recognition and Cash vs. Accrual Basis

  - Current QuickBooks setup: Revenue on cash basis, expenses on accrual basis
  - Agreed to use $1.141M as revenue figure (cash basis) instead of $1.4M
  - Some invoices created in December for January kickoffs were incorrectly recognized in 2024
  - Decision to recognize revenue after asset transfer date to C-Corp, reducing LLC's taxable income

### Expense Categorization and Deductions

  - Home office deduction: Previously $30k, needs to be reinstated (17% of square footage)
  - Vehicle purchase ($110k) to be considered for Section 179 accelerated depreciation
  - Gas expenses potentially miscategorized (only handful in QuickBooks vs. 50 transactions in Airtable)
  - Food/entertainment expenses to be adjusted to 50% deductible

### Tax Liability Estimation

  - Rough calculation: $276k profit (from Airtable) - $110k (car) - $10k (home office) ≈ $200k taxable income
  - W-2 income expected to be net positive or neutral due to overpayment
  - Ericksson to compare Chase 5042 credit card transactions in Airtable vs. QuickBooks for accuracy

### QuickBooks vs. Airtable Reconciliation

  - Airtable serving as a "gut check" for transaction categorization and completeness
  - Discrepancies found in gas transactions and potentially other categories
  - Ericksson to export and compare Chase 5042 data between systems

---

## Action Items

**Ericksson Abad (Accountant)**
- Add back home office expenses to tax calculations. Research/apply appropriate limitations ($30k estimated deduction, 17% of square footage for separate office floor).
- Adjust revenue in tax calculations from $1.4M to $1.141M (cash basis, per actual checking account deposits). Communicate change to Anderson Tax and Riot (final preparer).
- Include Section 179 accelerated depreciation for vehicle purchase (~$110k) in tax calculations.
- Compare Airtable model entries (1,918 transactions total) with QuickBooks Chase 5042 transactions. Identify missing or miscoded entries. Adjust QuickBooks as needed for accuracy.
- Review/adjust QuickBooks categorizations, prioritizing gas expenses (50 Airtable transactions vs. only handful in QB; some may be miscategorized as meals/entertainment). Compare with Chase 5042 statement and Airtable model.

---

## Transcript

**Marcel Santilli:** How's it going?

**Ericksson Abad:** I'm trying to imagine how you feel. I just want you to know I'm really trying to get it down for you, too.

**Marcel Santilli:** No, I know. It's not your fault or anything. It's just like I hate this situation.

**Ericksson Abad:** Yeah, it's a lot. I was shocked too. I was like, damn, how do we get it this low?

**Marcel Santilli:** So I pulled up my Airtable model where I exported every credit card and bank transaction. That's my simplified view. I'm trying to match categories and see if there's anything wrong. The first thing I looked at was gas expenses. Why is it so off? I don't know if I'm looking at the wrong thing, but when I check the auto expenses category, I'm assuming all gas should be there. And then comparing to last year, clearly there's a bunch of transactions missing. Could it be that the connection broke some months, or did we accidentally remove transactions?

**Ericksson Abad:** Yeah, exactly as you mentioned. When we reconciled 2024 activity, we only included what should have been included. With the Chase 5042 account, it won't reconcile entirely because that card also included Nadia's card that was ending. We only included your card. So some might be miscoded. And Nadia's card isn't in QuickBooks—it didn't get uploaded.

**Marcel Santilli:** Okay, but Nadia's stuff is related to the LLC. We gave her the card to make it easier for her physical card instead of using mine for everything. It should all be business.

**Ericksson Abad:** Right, it's a business credit card.

**Marcel Santilli:** But even if we exclude stuff, I'm seeing $4,200 just for gas for example. There's definitely transactions either missing or somewhere else.

**Ericksson Abad:** They're probably in a different account.

**Marcel Santilli:** We can figure this out. The easiest path would be to estimate based on credit card transactions. I'm okay being aggressive here—trying to minimize the 2024 burden, even if the C-Corp pays more taxes down the line. For instance, the prior accountants removed the home office deduction. But that was a $30,000 write-off last year. It's 17% of the house square footage and a completely separate floor. Why would they just remove that?

**Ericksson Abad:** Yeah, with the house, I think they totally misinterpreted it. It looks like they excluded the entire $217k spent, which is a big chunk. We need to add that back.

**Marcel Santilli:** Wait, they excluded everything?

**Ericksson Abad:** But I want to make sure about IRS guidelines. It's not always dollar-for-dollar. There are limitations to how much we can deduct. Still, even if limited, they shouldn't have removed it entirely.

**Marcel Santilli:** That makes sense. Some of it is furniture, like cabinets. But yeah, there's also a lot of Upwork expenses. What's the best approach for today?

**Ericksson Abad:** I included Upwork as consulting expenses. Everything from Remotes.com, Upwork, and other consultant-type names are already included as expenses. There's also software and subscriptions. The biggest gap we didn't anticipate was the additional income. When you were talking to API Accounting, they added W-2, miscellaneous income, and $1.4M in revenue—about $300K more than you estimated.

**Marcel Santilli:** So the W-2, I actually overpaid on taxes. The second I put it in, it showed I get a $10,000 tax return. They owe me $10,000. So the W-2 should actually be net positive, not negative.

**Ericksson Abad:** Okay.

**Marcel Santilli:** My wife had no income, and I exceeded the Social Security limit.

**Ericksson Abad:** So you withheld too much.

**Marcel Santilli:** Exactly. From looking at the checking account, I'm getting $1.141M in revenue. Where's the other $250K-plus? Is that just how we're recognizing it?

**Ericksson Abad:** So in QuickBooks, we set it as cash-based. We didn't split it out. Usually for quarterly contracts we'd spread revenue across three months, but I kept it cash-based because the prior accountant said that was more favorable.

**Marcel Santilli:** But cash basis means only money in the checking account, right? On cash basis, if it's not in checking, there's no other way we got paid.

**Ericksson Abad:** Yeah, but in QuickBooks whenever we invoice a customer, we recognize revenue. So the $1.4M includes invoices issued in the year but not yet paid.

**Marcel Santilli:** That's the problem. Alice was creating invoices in December for January kickoffs—90 days early—but the revenue shouldn't be recognized because the engagement hadn't started. That explains the $300K mismatch. We removed ~$500K in expenses and added ~$300K in income that isn't real cash.

**Ericksson Abad:** Yeah, we can tell them. I actually mentioned this to them. In the C-Corp right now, I'm using accrual basis properly—every invoice goes to deferred revenue and we recognize it only for the month we deliver services. For the LLC, I followed the prior advice that cash basis was more favorable, so I didn't change it because of time constraints.

**Marcel Santilli:** But if we're using cash basis, shouldn't we use the actual cash numbers—what's actually in the bank?

**Ericksson Abad:** Yes. I would say we should adjust to use $1.141M instead of $1.4M.

**Marcel Santilli:** I'll suggest that to Anderson Tax.

**Ericksson Abad:** That's definitely something we can change. One more thing though—we're pushing some revenue to 2025, but it won't necessarily be the C-Corp's expense.

**Marcel Santilli:** Right, the asset transfer was January 23rd. So for a kickoff on January 13th where we invoice for three months—technically the LLC should only report the income before asset transfer. But if we want to be simple, everything invoiced by the LLC is the LLC's responsibility, right?

**Ericksson Abad:** Yeah. I'm doing the first option because it lowers LLC income. Only recognizing revenue through the asset transfer date, then moving everything after to the C-Corp.

**Marcel Santilli:** Okay, so it's less of an issue deferring to next year.

**Ericksson Abad:** Yeah, plus if we're doing cash basis, that's what we're supposed to do anyway.

**Marcel Santilli:** Okay, so roughy speaking... (checking numbers) ...the gut check here is $276K. Obviously we can't deduct 100% of everything. Food is maybe 50%, so ballpark $300K profit.

**Ericksson Abad:** From the Chase accounts?

**Marcel Santilli:** This is for the business checking and Chase 5042 credit card—including Nadia's card. But this doesn't include the vehicle purchase.

**Ericksson Abad:** Right.

**Marcel Santilli:** Ideally we do Section 179 accelerated depreciation on the car. That's about $110K right there.

**Ericksson Abad:** Is this just from the Chase?

**Marcel Santilli:** Chase checking, 5042, and Nadia's card—it's all part of the business accounts. Just those three. So the delta is about $276K. And the only things missing would be the vehicle and anything we can't recognize 100%. For assets—computers, furniture—I'm not sure what the rules are. We use Hathi for equipment, which might be expensable.

**Ericksson Abad:** Yeah, I moved all that. Let me see what we have. Did the Amex get included?

**Marcel Santilli:** This is about 1,918 transactions. Excluding revenue, that's 1,800 transactions. Yeah, there's still some miscategorized stuff, but at least ballpark it's correct. Like domain renewals—where should that go? Right now it's under professional services, but it should be subscriptions.

**Ericksson Abad:** In QuickBooks they're lumped together in subscriptions/licenses.

**Marcel Santilli:** And there's some fixed assets like a desk—about $20. We could reclass that to the balance sheet. But the main thing not included is home office expenses—mortgage and other costs. Last year I think it was $20K or so.

**Ericksson Abad:** I didn't see any mortgage expenses in QuickBooks. Did you pay that from personal?

**Marcel Santilli:** No, I just take it for taxes—17% of square footage. (After looking through numbers) So if we assume home office is $10K and the car is $110K, I don't see why we wouldn't do accelerated depreciation on the car.

**Ericksson Abad:** Okay, let me make a list of what we definitely need to fix.

**Marcel Santilli:** What is this Airtable model you're using? Do you want to use it as official finance records?

**Ericksson Abad:** That's why we use QuickBooks—we need official financials. But Airtable is a nice gut check to make sure there aren't big buckets miscategorized or missing.

**Marcel Santilli:** Right, like the gas one. There are 50 gas transactions in Airtable but only a handful in QB.

**Ericksson Abad:** Yeah, some are probably miscoded. Me and Susanna went through and flagged any we recognized as gas stations. But some might be coded as meals and entertainment if we didn't recognize them.

**Marcel Santilli:** We could check what's in the meals account to see if they're higher.

**Ericksson Abad:** Yeah, I exported a Chase 5042 spreadsheet. I'll compare it with the Airtable categories and fix QB so they match.

**Marcel Santilli:** Sounds good.

**Ericksson Abad:** And the revenue adjustments and house expenses will make a significant impact too.

**Marcel Santilli:** Yeah, so if we assume the W-2 is net positive, or even neutral, and assume revenue of $1.141M, and we add back the car depreciation and R&D stuff we talked about, my assumption is we'd be close to conservatively $200K taxable income.

**Ericksson Abad:** In net profit?

**Marcel Santilli:** Actually taxable liability.

**Ericksson Abad:** Got it. But could be off depending on what other expense categories need adjustment.

**Marcel Santilli:** Right, like if some entertainment or meals are only 50% deductible. But this is just the basic gut check. The net is $276K, and if food is only 50%, that's another $20K, so $300K. Minus $110K for the car, minus $10K for home office—that brings us to $200K pretty conservatively.

**Ericksson Abad:** Okay.

**Marcel Santilli:** But again, if there are things that really can't be fully written off, let me know. Riot would be the best one to answer that since they're the final preparers. We just need to give them the adjusted numbers.

**Ericksson Abad:** Yeah, it's a lot.

**Ericksson Abad:** I was shocked, too.

**Ericksson Abad:** I was like, damn, how do we get it this low?

**Ericksson Abad:** Like, how do we get it even low at all?

**Marcel Santilli:** So, yeah, like, so the way, like, I know, like, what I was kind of trying to do, hold on, let me try to pull up what I was looking at here.

**Marcel Santilli:** Okay, so what I had done at one point was just export every credit card transaction, you know, and every bank transaction into this.

**Marcel Santilli:** That's right.

**Marcel Santilli:** So that's my dumb view, if you will.

**Marcel Santilli:** That's a little bit more simplified, right?

**Marcel Santilli:** And so essentially, what I was looking at as I'm kind of going through this is just like trying to match at least some of these categories and see if there's anything wrong.

**Marcel Santilli:** So the first one that I was doing was to guess, right?

**Marcel Santilli:** Which was the one that I was like, okay, why is it so off?

**Marcel Santilli:** And so like, but I don't know if I'm looking at the wrong thing.

**Marcel Santilli:** And then I was trying to find like the different kind of categories or understand why like when you go to expenses, like if you go to the category that I could find, which is I think auto, right?

**Marcel Santilli:** I'm assuming all gas should be in that, right?

**Marcel Santilli:** Auto expenses.

**Ericksson Abad:** Yeah.

**Marcel Santilli:** And then if we go to last year, I was just trying to like pattern match to see if we're off by something, you know, and I was like, okay, clearly there's a bunch of transactions missing here.

**Marcel Santilli:** So I was like, okay, like, why is that?

**Marcel Santilli:** Like, you know, so then I was like, could it be that like some months, like the connection broke and then we missed some of the transactions?

**Marcel Santilli:** Or could it be that we just like remove those transactions accidentally or because that could be making up a good chunk of the expenses, you know?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** So it is exactly as you mentioned.

**Ericksson Abad:** So when we reconciled the activity in 2024, we only reconciled what you mentioned was what we should have included.

**Ericksson Abad:** So for example, with the Chase 5042 account, it's not going to reconcile entirely to the amount that you're seeing because that also included another card that was ending.

**Ericksson Abad:** Which was, to our understanding, was Nadia's card.

**Ericksson Abad:** And we only included your card.

**Ericksson Abad:** So it's possible that some are miscoded into different buckets.

**Ericksson Abad:** And there's also, for sure, Nadia's card is not included in QuickBooks.

**Ericksson Abad:** So they did not get uploaded.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So it should be included.

**Marcel Santilli:** It's just that Nadia's stuff is also related to the LLC.

**Marcel Santilli:** It's just the personal stuff, the $65.97.

**Marcel Santilli:** The only reason I gave her her own card was just to make it easier for her to have her physical card instead of just using mine for everything.

**Ericksson Abad:** Okay.

**Ericksson Abad:** But they're all business, essentially, because it's a business credit card.

**Ericksson Abad:** Yeah.

**Marcel Santilli:** it should be all there.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** But then, like, what I was trying to figure out is, like, even if you look here, even if you exclude, like, hold on, let me add.

**Ericksson Abad:** Just filter for your 5042, maybe.

**Marcel Santilli:** Like, even if we do this, like, it's still 4200, right, for gas, for example.

**Marcel Santilli:** And so I think there might be, like, definitely there's got to be transactions either missing or somewhere else, right?

**Ericksson Abad:** Yeah, they're probably in a different account.

**Ericksson Abad:** So the majority of...

**Marcel Santilli:** We can figure this out.

**Marcel Santilli:** It's just, like, what I was thinking was mostly, like, the easiest path here would be, like, to try to estimate some stuff based on, like, just the credit card transactions.

**Marcel Santilli:** And I'm okay, like, being essentially, like, super, like...

**Marcel Santilli:** ...

**Marcel Santilli:** ...

**Marcel Santilli:** What's the right word here?

**Marcel Santilli:** Like, aggressive, I guess, is maybe the right word on, like, for...

**Marcel Santilli:** What we report?

**Marcel Santilli:** Yeah, essentially, like, and then, and I don't know if, like, they understood that.

**Marcel Santilli:** It's like, hey, we're okay.

**Marcel Santilli:** Like, I'm personally okay taking, let's call it, a little bit of risk, and also, like, being aggressive and doing, trying to minimize the, like, the 2024 burden, even if it's the expense of the C-Corp paying a bit more taxes down the line.

**Marcel Santilli:** Like, for instance, like, the R&D stuff, like, you caught it already, but, right, like, it's like, that's why I didn't understand, like, how much they were, like, how they were approaching it, you know?

**Marcel Santilli:** Like, for instance, like, hey, the home office, like, let's just remove that.

**Marcel Santilli:** It's like, okay, like, I don't, because there's another office, you know, like, but then, like, last year, that was, like, a $30,000 write-off, right?

**Ericksson Abad:** Like,

**Marcel Santilli:** Because, like, the mortgages lost all the expenses.

**Marcel Santilli:** Like, essentially, it's, like, 17% of the square footage of the house, and it's a completely separate floor.

**Marcel Santilli:** Like, things like that that I was like, okay, like, maybe they're just, like, being super, super, like, blank, like, F this, remove, remove, remove, you know?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** Yeah, with the house, I think they totally just misinterpreted that because it looks like they excluded the entire amount that was spent for the whole minimum.

**Ericksson Abad:** Which was a 217k, and that is a big one already there.

**Ericksson Abad:** they wiped out that amount, then that explains a big chunk of it.

**Marcel Santilli:** Okay.

**Ericksson Abad:** So we need to have them added back.

**Ericksson Abad:** But, again, like, I just want to make sure, too, like, because I'm looking into some of this stuff in, like, the IRS, like, guidelines, and usually it's not always, like, dollar for dollar, right?

**Ericksson Abad:** So there's also, like, limitations to some of how much we can deduct.

**Ericksson Abad:** And so, still, given the fact.

**Ericksson Abad:** That they removed the entire thing entirely, but it could still be, like, limited.

**Ericksson Abad:** Got it.

**Marcel Santilli:** Okay.

**Marcel Santilli:** That makes sense.

**Marcel Santilli:** Yeah, because I think, like, for instance, not, like, some of this is, like, for instance, like, cabinets, right?

**Marcel Santilli:** Or from what I understand, it's considered, like, furniture, essentially, right?

**Marcel Santilli:** And then, yeah, these were, like, just the transactions, but I don't know how, like, some of them, like, for instance, like, there's Upwork, too, which is, like, a ton.

**Marcel Santilli:** I don't know if we, what is the best approach here, you think, for today, for me to, like, focus on?

**Ericksson Abad:** Yeah, I included the Upwork stuff as the consulting expenses, too.

**Ericksson Abad:** So those were...

**Ericksson Abad:** So basically everything, Remotes.com, Upwork, and any other names that I recognized that are related to Inc.

**Ericksson Abad:** I just basically assumed everyone was a consultant, which would also be included as an expense.

**Ericksson Abad:** And so those are already included.

**Ericksson Abad:** I wouldn't click into that one as much.

**Ericksson Abad:** But there's other categories, like the software and subscriptions, those were all also included.

**Ericksson Abad:** So we went through the list to see which ones were the highest amount that were re-spent.

**Ericksson Abad:** And the biggest chunk really is just the biggest gaps that we really didn't anticipate from the time when you were talking to API accounting was the additional income, which was including their W-2, all miscellaneous incomes, and the 1.4, right?

**Ericksson Abad:** Because it was like 300K more than what you had estimated.

**Ericksson Abad:** didn't think a when in, you didn't more We So Thank

**Ericksson Abad:** At the time, you were talking to API accounting.

**Marcel Santilli:** So the W2, though, like, essentially, I overpay on, like, taxes on the W2.

**Marcel Santilli:** So, like, the second I put the W2 in here, it already said, like, I already have a $10,000, like, tax return.

**Marcel Santilli:** Like, essentially, like, they owe me $10,000.

**Ericksson Abad:** Okay.

**Marcel Santilli:** So the W2 should actually be a net positive, not a net negative, essentially.

**Ericksson Abad:** Okay.

**Ericksson Abad:** Okay.

**Marcel Santilli:** Because, like, with the, like, my wife didn't have income.

**Marcel Santilli:** And so it's like, and I kind of overpaid on the, like, on the, and I exceeded the limit on the Social Security.

**Ericksson Abad:** I see.

**Ericksson Abad:** So you withheld too much.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then, and then what I was trying to figure out was, like, the, from just looking at the checking, right?

**Marcel Santilli:** Like, essentially, I get 1.141 in revenue.

**Marcel Santilli:** Mm

**Marcel Santilli:** Where is the other 250 or so, 5,000?

**Marcel Santilli:** Or is this just how we're recognizing this?

**Ericksson Abad:** Yeah, so the way we actually have it in QuickBooks, I haven't adjusted it to be, well, it's entirely incorrect, but the way we recognized it in LLC was just cache-based, right?

**Ericksson Abad:** We didn't even split it out, because usually if we wanted to split it out, depending on when we actually delivered the services, so let's say some of the contracts were quarterly, right?

**Ericksson Abad:** So we would normally spread that out to three months.

**Ericksson Abad:** I just left it as cache-based, because that's what the API accountant said.

**Ericksson Abad:** It was more, I think, favorable to leave it as cache-based instead of accrual-based, and it's more in line with everything else that we did.

**Ericksson Abad:** And so I left it at that.

**Ericksson Abad:** But the other 300 that I'm seeing is like, so there was also revenue that you got from, and I'm not sure if this is related to the business, but there was like Stripe transaction.

**Ericksson Abad:** That we counted in there.

**Ericksson Abad:** There was some, like, Stripe revenue that was coming in, and I wasn't sure what that was for.

**Marcel Santilli:** Yeah, like, the Stripe was just, like, the courses and stuff that would go throughout the year.

**Marcel Santilli:** Oh, okay.

**Marcel Santilli:** Essentially, like, there's no way to get paid unless it hits the checking account, right?

**Marcel Santilli:** Like, so, like, on cash basis, like, if it's not in the checking, the business checking, like, we, like, there's no other way we would have gotten paid as a business.

**Ericksson Abad:** Yeah, but, like, think about, like, so when it was booked in QuickBooks, basically, whenever we invoiced the customer, even without payment, you're already recognizing that in revenue.

**Ericksson Abad:** So these are all, like, invoices that were issued in the year, the 1.4, but you still haven't gotten paid.

**Marcel Santilli:** But here's the thing, like, there was, oh, , okay.

**Marcel Santilli:** So there was a lot there that was, like...

**Marcel Santilli:** Alice just going in and creating the invoice because we knew we were going to have a kickoff like in January, for example, right?

**Marcel Santilli:** But that revenue like shouldn't be recognized because it didn't start.

**Marcel Santilli:** Even though the invoice was created 90 days before the engagement started, was just like the second people sign, like Alice would create an invoice.

**Marcel Santilli:** But then she wouldn't actually send it.

**Marcel Santilli:** But it looks like it was created, you know, like probably in December, you know?

**Marcel Santilli:** But then if we're paying taxes for that in 2024, then it's like, that's why like, because we weren't doing the estimate, like I estimated this.

**Marcel Santilli:** So if there's like, obviously like 500k worth of like expenses that were removed, and then another 300 that were added, then that kind of explains the extra 300k.

**Marcel Santilli:** Because my hope was to essentially like, oh, very little, like maybe an extra 50 or something just to be super.

**Marcel Santilli:** Conservative, you know, and then the rest be the estimated payment for Q1, essentially.

**Ericksson Abad:** Yeah, we can tell them, well, we can tell them, because I did mention that to them, and that was, because that exercise will just take us.

**Ericksson Abad:** I tried to, I'm doing that, for example, in corp right now, we're recognizing exactly like on a cruel basis.

**Ericksson Abad:** So every invoice that we issue out, it goes to deferred revenue, and we're only recognizing revenue for the month that we deliver services.

**Ericksson Abad:** So it's actually spread out in the LLC, because I had, would have to do this, like, for the entire year.

**Ericksson Abad:** And I took your prior accountant's advice about, like, how the IRS would treat it as more favorable if there was a cash basis.

**Ericksson Abad:** So I didn't touch that, because we're, like, constricted with time.

**Marcel Santilli:** But considering this, we could tell them.

**Marcel Santilli:** Because this is when, know, she paid.

**Ericksson Abad:** Yes, this is the cash basis piece.

**Marcel Santilli:** This is the actual, like, amount of money.

**Marcel Santilli:** Or, as far as taxes are concerned, should be 1.1.

**Ericksson Abad:** If it was all cash-based, yeah, but we did, it's like a bit of, basically it's both right now, right?

**Ericksson Abad:** Your expenses are accrual-based and your revenue in QuickBooks is all, it's all cash-based, but there's still stuff that you haven't received in, that they didn't include it in 2024.

**Ericksson Abad:** Does that make sense?

**Ericksson Abad:** Because it's like, it's all, the method is all cash-based.

**Marcel Santilli:** So for tax purposes, forget QuickBooks or whatever, like just from an IRS perspective, like we're doing cash basis or accrual, and then even for accrual, well, let's start there.

**Marcel Santilli:** Like, is it cash basis?

**Ericksson Abad:** It is cash basis, yes.

**Marcel Santilli:** Okay, so then for a tax perspective and for estimating the taxes, would it be fair to, like, assume this is correct, since this is actual transactions in the bank account?

**Marcel Santilli:** Or this is ballpark, at least?

**Ericksson Abad:** Yes.

**Ericksson Abad:** I would say we should adjust, you should use this number instead of the 1.4 number.

**Marcel Santilli:** Okay.

**Marcel Santilli:** I would suggest that to Anderson.

**Ericksson Abad:** So that's one thing where we could change.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So then that helps.

**Ericksson Abad:** Yeah.

**Marcel Santilli:** Because that's what I was saying.

**Marcel Santilli:** It's like, even if the, I guess the payments are all here too, the credit card.

**Ericksson Abad:** But I think, I'm like thinking about this more.

**Ericksson Abad:** I think what's happening though, it's just like, we're just kind of pushing it into 2025.

**Ericksson Abad:** And even though we push it to 2025, it doesn't necessarily mean that it's going to be the C Corp's expense still, right?

**Ericksson Abad:** Because that didn't happen until like two or like 123 was the asset transfer.

**Ericksson Abad:** So this is still, it's either we take it into 2024 or we recognize it in 2025, which is the.

**Ericksson Abad:** Got it.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** But then I guess it just depends how we're going to do it, right?

**Marcel Santilli:** Like on what's C-Corp versus what's LLC.

**Marcel Santilli:** So for instance, like a kickoff that happened January 13th, right?

**Marcel Santilli:** You invoice for three months.

**Ericksson Abad:** Mm-hmm.

**Marcel Santilli:** And then if the C-Corp incorporated at this date and the asset transfers were that date, then technically like the LLC should report income of like only that amount.

**Marcel Santilli:** But then if we're doing, so that's one approach, right?

**Marcel Santilli:** Like the other approach is just, hey, it invoices until the C-Corp invoices it, it's all LLC and LLC is going to have to cover everything, right?

**Marcel Santilli:** On tax-wise, right?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** I'm doing the first option because that lowers the risk or that lowers the income on LLC.

**Ericksson Abad:** First one.

**Ericksson Abad:** Only recognizing a portion, basically everything after the asset transfer date, I'm moving to Inc.

**Ericksson Abad:** so that it's lesser on the LLC.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So then it's like less of an issue, right, that we're deferring into next year, right?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** Or not deferring.

**Marcel Santilli:** I mean, if we're doing cash cases, like that's what we're supposed to do anyways.

**Ericksson Abad:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So then like roughly, I guess, let me just filter out.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So then that puts us at about, like, obviously this could be off, right?

**Marcel Santilli:** But like...

**Marcel Santilli:** Like...

**Marcel Santilli:** then like...

**Marcel Santilli:** you.

**Marcel Santilli:** Oh, this has massive expenses.

**Marcel Santilli:** Oh, I see.

**Ericksson Abad:** Account transfers.

**Ericksson Abad:** Yeah, we have everything for 8111 voted, like reconciled to the penny in the bank statement for that account.

**Marcel Santilli:** Okay, so...

**Marcel Santilli:** Okay, so then, this is, again, this is just a gut check, right?

**Marcel Santilli:** Like, so the gut check here is 276.

**Marcel Santilli:** If this was, like, obviously, there's things we can't recognize 100%, like food can most likely all be mostly, like, 50%, right?

**Marcel Santilli:** For most of this, like, so it's like ballpark, give or take.

**Marcel Santilli:** $300 profit.

**Ericksson Abad:** This includes?

**Marcel Santilli:** But this doesn't include the vehicle purchase, essentially.

**Ericksson Abad:** Okay.

**Marcel Santilli:** Ideally, would do Section 179 accelerated depreciation, and that's like $110 right there.

**Ericksson Abad:** And is this just for the Chase?

**Ericksson Abad:** It's 8111, 5042 credit card, Nadia's credit card, but it's all 504, or like part of the business credit card account.

**Marcel Santilli:** Correct.

**Ericksson Abad:** And just those two accounts.

**Marcel Santilli:** Correct.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So as you can see here, the accounts are these three.

**Ericksson Abad:** Okay.

**Ericksson Abad:** So it's like- transaction on those three accounts, and it's excluded.

**Marcel Santilli:** There might be a couple missing here and there that are just empty that I've just filtered out, right?

**Marcel Santilli:** That I just need to go through, but, you know, being conservative here, it would be-

**Marcel Santilli:** Essentially, like this, like, which is, comes out to about, you know, the delta between those two is like 276.

**Marcel Santilli:** And then the only things missing from here would be the vehicle and anything that it can't be recognized 100%.

**Marcel Santilli:** Or, and then outside of that, it would be assets, essentially, right?

**Marcel Santilli:** Like, how we recognize assets and, like, do we do depreciation?

**Marcel Santilli:** Do we do, like, you know, like, for instance, like a computer?

**Marcel Santilli:** Like, what are the rules to have to recognize computers, right?

**Marcel Santilli:** Like, but it uses, like, because we use Hathi, like, we could technically say it's an expense, you know, as well, if it was more favorable, too, I think, but I don't know.

**Ericksson Abad:** Yeah, I mean, I moved all that.

**Ericksson Abad:** I think it's, let me see, I'm just trying to look at what we have.

**Ericksson Abad:** I'm trying to think of what else could be in QuickBooks that's not, because everything we did recognize.

**Ericksson Abad:** Oh, what about your, did the Amex, is your Amex included in here, or was that a, it was like this year.

**Ericksson Abad:** Okay.

**Ericksson Abad:** So this is just going to be on, I'm looking at the balance sheet, the balance sheet.

**Marcel Santilli:** So this is about 1918 transactions.

**Marcel Santilli:** And then if you exclude the revenue from it, that's 1800 transactions, essentially.

**Marcel Santilli:** Like, you overtake.

**Marcel Santilli:** Um, yeah, because we have, there's things still that are miscategorized, but at least like ballpark should be correct.

**Marcel Santilli:** Like this hover thing is like domain renewals, like where do we want to put it, right?

**Marcel Santilli:** Like right now it's miscategorized as like professional services, right?

**Marcel Santilli:** Like, but, um, yeah.

**Ericksson Abad:** Well, for us, we, in QuickBooks, they are the same.

**Ericksson Abad:** They're, they're probably lumped.

**Ericksson Abad:** I remember coding these and they're in subscriptions, like licenses subscriptions right now.

**Ericksson Abad:** So you could either put it in the balance sheet or you can write.

**Marcel Santilli:** So really, the main things here, I think, are like, like, coffee, you know, is this asset, mostly.

**Marcel Santilli:** So that's about 20.

**Ericksson Abad:** Yeah.

**Ericksson Abad:** Yeah, so we could reclass that to balance sheet and capitalize it.

**Marcel Santilli:** And then outside of that, I think, like, yeah, like, this is like.

**Ericksson Abad:** I put all that stuff in there.

**Ericksson Abad:** Yeah, Mission Rock.

**Ericksson Abad:** And then there's, like, another name that I see for the Tony.

**Ericksson Abad:** Is that the address at the 365?

**Marcel Santilli:** Yeah, yeah.

**Ericksson Abad:** Yeah, so those are all.

**Ericksson Abad:** And to rent expense.

**Marcel Santilli:** And then the only thing that doesn't include is, like, the home expenses, like, for home office, right?

**Marcel Santilli:** Which is, like, mortgage and, like, other expenses.

**Marcel Santilli:** Last year, I think it ended up being, like...

**Ericksson Abad:** I didn't actually see any mortgage expenses in QuickBooks.

**Ericksson Abad:** Did you pay that out of your business?

**Marcel Santilli:** No, so mortgage expenses, like...

**Marcel Santilli:** The way I do it is just, like, considering just the expense in the...

**Marcel Santilli:** Just for filing taxes.

**Ericksson Abad:** Oh, okay.

**Marcel Santilli:** Like me, like...

**Marcel Santilli:** Because you're only taking, like, the 17%, right?

**Marcel Santilli:** Like, of the...

**Marcel Santilli:** I think that's...

**Marcel Santilli:** It's whatever the square footage was.

**Ericksson Abad:** Let's see.

**Marcel Santilli:** Let's Let's see.

**Marcel Santilli:** We...

**Marcel Santilli:** We...

**Ericksson Abad:** Is...

**Ericksson Abad:** Thank you.

**Marcel Santilli:** Just see everything.

**Marcel Santilli:** What the business one stuff is.

**Marcel Santilli:** But, I don't know, I got to find it.

**Marcel Santilli:** But essentially last year, I think it was like 20K, right?

**Marcel Santilli:** last Here's we're

**Marcel Santilli:** For the home office, since we're doing assets only, I think we can assume, like, if we assume the home office is like 10 and the car is 110, I don't see why we wouldn't be able to do accelerated depreciation on the car.

**Ericksson Abad:** Mm-hmm.

**Ericksson Abad:** Okay, so let me make a list.

**Ericksson Abad:** I think we have a few here that should definitely be found.

**Ericksson Abad:** So we have the revenue.

**Marcel Santilli:** We should use the...

**Ericksson Abad:** So, okay, another question for you.

**Ericksson Abad:** What is this Airtable model that you're using?

**Ericksson Abad:** Like, do you want to use that as your finance?

**Ericksson Abad:** Okay.

**Ericksson Abad:** So the part of the reason why we're using QuickBooks is because, like, if we wanted to use that as financials with, like, conjunction with, like, I mean, I would say that is correct.

**Ericksson Abad:** QuickBooks is correct.

**Ericksson Abad:** Like, all transactions are in there.

**Ericksson Abad:** Minus Nadia's transactions.

**Marcel Santilli:** But, like, maybe if we're going there, like, okay, let's take just the gas one, right?

**Marcel Santilli:** Like, there's 50 gas transactions and then 5042.

**Marcel Santilli:** Is that just coded differently in the, because there's only, like, a handful in QuickBooks?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** So some of them because of how, okay, so, like, the methodology that me and Susanna did was basically, like, if we could recognize that it's a gas station, then, yeah, we should definitely put it into gas.

**Ericksson Abad:** But I'm already seeing some under, like, communals and entertainment.

**Ericksson Abad:** So I think, I don't know if she assumed everything.

**Ericksson Abad:** Like, if someone, if something was, like, at a gas station she's not aware of, if it's not, like, 76, she would have put it into, like, communals and entertainment.

**Ericksson Abad:** So, like, another check that we could do is, like, to see what the balance is in the meals or other accounts to see if they're higher.

**Ericksson Abad:** And then we could, like, just fix it or shift it around.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah, like, I think the...

**Marcel Santilli:** But Airtable is just, like, a nice gut check just to make sure, like, there's not big buckets, like, either miscategorized or missing, you know?

**Ericksson Abad:** Yeah.

**Ericksson Abad:** Yeah.

**Ericksson Abad:** So I exported a spreadsheet of what you did with the Chase 5042.

**Ericksson Abad:** I'll go through it again, compare it with the buckets, and then I'll fix it so that they're in line with what we have in the Chase credit card account.

**Ericksson Abad:** And then we'll see if it makes a big difference.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** sounds good.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** think, like...

**Ericksson Abad:** And revenue and then the house expenses, I think, will make a significant impact, too.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So essentially, like, if we assume, like, W2 is net positive, but even if we assume it's, like, neutral, right?

**Marcel Santilli:** And then we assume the revenue is 1141.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then we add the car and add back up some of the stuff we talked about, like, for instance, like the R&D and stuff like that.

**Marcel Santilli:** Then my assumption would be, like, we would be pretty close to, like, conservatively 200K, like.

**Ericksson Abad:** In net profit?

**Marcel Santilli:** In net profit.

**Marcel Santilli:** But it could be, not net profit, but, like, in taxable, like.

**Ericksson Abad:** Oh, your taxable liability.

**Marcel Santilli:** Yeah, yeah.

**Ericksson Abad:** Okay.

**Ericksson Abad:** But I could be off, right?

**Marcel Santilli:** Because, like, this is just, like, the gut check.

**Marcel Santilli:** Like, if there's major categories of expenses that are, like, okay, this is, like, this is entertainment, or this part is only, like, 50%.

**Ericksson Abad:** Okay, so that's different.

**Marcel Santilli:** But...

**Marcel Santilli:** This is just, you know, just the basic, that's how we estimate it essentially, right?

**Marcel Santilli:** Like, and then, which is mostly just looking at all of these as expenses, right?

**Marcel Santilli:** And I already excluded the car payments from here, so there shouldn't be anything.

**Marcel Santilli:** Um, and, okay, there's this, but we'll exclude a few things, but, um, which then, like, the net is 276 here, and then if we assume the food is only 50%, that's another, like, 20, right?

**Marcel Santilli:** So that's, like, 300, and then you subtract 110 for the car, and at, and another 10 for, for, like, home expenses, that should bring us to 200 pretty conservatively.

**Ericksson Abad:** Okay.

**Marcel Santilli:** But, again, like, if there's pockets here that you're like, no, no, no, this is not how it works, like, this, this can't be entirely written off.

**Ericksson Abad:** Yeah, I mean, that's something that Riot would be able to best answer, right, because they're the ones that are—I think we have to just give them the adjusted numbers that we have.
