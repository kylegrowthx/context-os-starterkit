# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-22
time: 15:00 UTC
duration: 31 minutes
organizer: stevie@growthx.ai
enriched_on: 2026-02-28 14:32 UTC
participants:
  - name: Marcel Santilli
    email: marcel@growthxlabs.com
    affiliation: GrowthX (CEO/Founder)
    role: Founder & CEO
  - name: Daniel Lopes
    email: daniel@growthxlabs.com
    affiliation: GrowthX
    role: Product Lead
  - name: Jose Farias
    email: jose@growthx.ai
    affiliation: GrowthX
    role: Engineering Lead
  - name: Estevão Mascarenhas
    email: estevao@growthx.ai
    affiliation: GrowthX
    role: Full-stack Engineer
  - name: Stevie Kim
    email: stevie@growthx.ai
    affiliation: GrowthX
    role: Product Manager
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: GrowthX
    role: QA & Testing
  - name: Jason Gong
    email: jason@growthx.ai
    affiliation: GrowthX
    role: Team Member
  - name: Pedro Steimbruch
    email: pedro@growthx.ai
    affiliation: GrowthX
    role: Team Member
fathom_recording_id: 116321127
fathom_url: https://fathom.video/calls/540859770
share_url: https://fathom.video/share/iFx8-mczzzHBQx5V6rux3bhErkz51sFD
source: fathom
speakers_confirmed: true
</metadata>

---

## Summary

The CheckThat team reviewed and approved the billing RFC with key implementation decisions: inline webhook processing with delegation to a PORO, and updating pricing plans in the webhook handler post-payment. The team identified three critical launch blockers—incorrect BrandFetch logos eroding customer trust, silent Temporal workflow failures preventing onboarding and admin features, and the final pre-launch architecture tasks of fixing subcategory charts and de-duplicating brands.

---

## Context

CheckThat is approaching launch with the team in final sprint mode. The billing system integration with Stripe is now being finalized—Estevão proposed an RFC that sparked discussion around inline vs. queued webhook processing. Jose advocated for inline processing with proper delegation to avoid race conditions, while noting that future optimizations using concurrency keys or timestamp sorting could be addressed post-launch.

Beyond billing, the team is tackling launch-critical issues: BrandFetch's logo fetching for redirecting domains like cloud.com → cloud.ai is broken and undermining customer demos, Temporal workflow failures are silently failing without graceful UI fallbacks, and two major architecture tasks remain—fixing subcategory chart filtering and de-duplicating brands. Stevie and the product team need these resolved before going live to ensure trustworthiness and feature completeness.

---

## Relevance

**For Billing & Payment Processing:**
- Stripe webhook architecture design decisions and trade-offs between inline and async processing
- Pricing plan synchronization strategy to enforce feature limits after successful payment
- Pay gem evaluation for potential faster implementation with manageable trade-offs

**For Product & QA:**
- BrandFetch logo quality issues as a trust and demo blocker for key customer accounts
- Temporal workflow failure modes and the need for graceful error handling in user-facing interfaces
- Feature data filtering (subcategory charts by workspace prompts) requiring significant architecture work

**For Launch Readiness:**
- Identification of three critical blockers that must be resolved before public release
- Progress tracking on final pre-launch architecture tasks (subcategory charts, brand de-duplication)
- Cross-functional action items with clear ownership and dependencies

---

## Overview

- **Billing RFC Approved:** The billing RFC is approved with two key changes: process webhooks inline to preserve event order and update the `workspace.pricing_plan` in the webhook handler to apply new feature limits post-payment.
- **Logo Override is a Blocker:** Incorrect BrandFetch logos for key customers (e.g., Cloud) are a launch blocker, as they erode trust and prevent demos. A manual override feature is the agreed-upon fix.
- **Silent Workflow Failures:** The "Basic Research" Temporal workflow is failing silently, causing an empty onboarding description for `meta.com` and an infinite loading spinner in the admin panel. This is a critical bug requiring immediate investigation.
- **Final Architecture Tasks:** Jose will complete the final two pre-launch architecture tasks: fixing subcategory charts and de-duplicating brands.

---

## Key Topics

### Billing RFC Review

  - **Webhook Processing:**
      - **Problem:** The RFC's proposed inline webhook processing could cause race conditions if multiple events are processed in parallel.
      - **Solution:** Proceed with inline processing. Stripe's retry mechanism provides a safety net, and a future, more robust solution (e.g., sorting by timestamp, using SolidIQ concurrency keys) is out of scope for now.
      - **Refinement:** Delegate processing logic to a PORO to keep the controller clean.
  - **Pricing Plan Updates:**
      - **Problem:** The RFC's `handle_checkout_completed` webhook handler does not update the `workspace.pricing_plan` in our database.
      - **Solution:** Update the plan in the webhook handler to apply new feature limits immediately after payment succeeds.
      - **Implementation:** Use `PricingPlan.publicly_available.find_by(stripe_price_id: ...)` to find the correct plan.
      - **Environment Handling:** Use conditional logic in the `stripe_price_id` method to manage different IDs for production vs. sandbox environments.
  - **Gem vs. Custom Implementation:**
      - Estevão will evaluate the `pay` gem as a faster alternative.
      - **Risk:** A gem may lack the flexibility for future "fancy" subscription features, potentially requiring a fork.
      - **Guidance:** If using the gem, implement a `workspace.owner` method to abstract the concept of an owner, making future changes easier.

### Launch Readiness & Bug Review

  - **Logo Fetching Issues (BrandFetch):**
      - **Problem:** BrandFetch returns incorrect or missing logos for key brands (e.g., a random person for "Ask Cody," no logo for "Cloud").
      - **Root Cause:** BrandFetch struggles with domains that redirect (e.g., `cloud.com` → `cloud.ai`).
      - **Impact:** This is a launch blocker. It erodes user trust and prevents demos, as customers fixate on the incorrect logo.
      - **Solution:** Implement a manual override in the admin panel to upload correct logos to S3.
  - **Silent Workflow Failures:**
      - **Problem:** The "Basic Research" Temporal workflow is failing silently.
      - **Symptoms:**
          - Onboarding for `meta.com` yields an empty description.
          - The admin panel's brand research feature gets stuck in an infinite loading state.
      - **Cause:** The UI does not handle Temporal workflow failures gracefully.
      - **Urgency:** Investigate immediately. Temporal logs have a short lookback period (a few days).
  - **Jose's Progress:**
      - Completed the "competitor changes backfill" ticket.
      - Created two non-blocking "Stabilize Week" tickets:
          - "Switching workspaces requires a refresh."
          - "Prompt count meaning is not clear."
      - Currently fixing subcategory overview charts to filter data by a workspace's specific prompt subset.
      - Next: De-duplicate brands, the final pre-launch architecture task.
  - **Estevão's Progress:**
      - Completed minor onboarding fixes.
      - Focused on the billing RFC.
      - Will address remaining onboarding/competitor tasks before starting billing implementation.

---

## Action Items

**Estevão Mascarenhas (GrowthX, Full-stack Engineer)**
- Evaluate Pay gem for billing; decide use vs custom
- Implement Stripe webhook plan-swap on success; use PricingPlan.publicly_available
- Define workspace.owner method for Pay gem
- Create Linear task: admin logo override; set as blocker
- Reproduce onboarding w/ meta.com; investigate empty description

**Stevie Kim (GrowthX, Product Manager)**
- Verify suggested competitors PR shows all brands; report to Estevão
- Confirm logo override as blocker w/ Daniel + Marcel
- Send Temporal logs link to Jose + Estevão; then investigate basic research failures

**Jose Farias (GrowthX, Engineering Lead)**
- Complete subcategory overview charts fix to filter by workspace prompt subset
- Begin brand de-duplication task (final pre-launch architecture work)

---

## Transcript
**Jose Farias:** Hey Estevão, I was looking at your billing RFC, we might as well talk about it while people are joining, if that sounds good.

**Estevão Mascarenhas:** Yeah, sure, let's do it.

**Jose Farias:** I don't think, I don't see anything that is particularly like jumps out, this looks good.

**Jose Farias:** But very minor things, like we have a webhooks pattern that we currently do, that we persist the payload and then process it afterwards.

**Jose Farias:** In your code snippets, I believe you're processing it in line, which probably is fine.

**Estevão Mascarenhas:** Yeah, that's a good point.

**Estevão Mascarenhas:** I was thinking about it yesterday. The issue with enqueuing those to be processed later is that we could lose the linearity of those events.

**Estevão Mascarenhas:** We can have events being processed in parallel, right?

**Estevão Mascarenhas:** Like if multiple workers start getting those.

**Estevão Mascarenhas:** That's why I left in line, but if you have any ideas.

**Estevão Mascarenhas:** The good thing is that Stripe usually retries the event if it fails on our site for some reason.

**Estevão Mascarenhas:** But yeah, perhaps you could keep track of those that fails.

**Jose Farias:** So I do have ideas, but nothing that we need to implement right now.

**Jose Farias:** Stripe sends a timestamp with the event. We can persist that and then sort webhooks by timestamp.

**Jose Farias:** Psychic doesn't support this on the free tier, but SolidIQ has concurrency keys.

**Jose Farias:** So you can limit the concurrency to like, oh, if it's a Stripe thing, then process it like one at a time and in order.

**Estevão Mascarenhas:** Yeah, that would work.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** But let's not, let's not complicate it.

**Estevão Mascarenhas:** Hey, Stevie.

**Jose Farias:** Hey.

**Jose Farias:** We're just talking about the...

**Jose Farias:** The billing, RFC.

**Jose Farias:** So on, just to wrap that up, I think we can do inline.

**Jose Farias:** That's fine.

**Jose Farias:** Maybe just like delegate it to a Poro or something, just like a different class, just so that the controller is not like mixing things like with different processors for different webhook sources.

**Jose Farias:** And then...

**Estevão Mascarenhas:** Honestly, yeah, go ahead.

**Estevão Mascarenhas:** I'll try the pay gem you mentioned. If it works for what we need, most of this RFC work won't matter. I wanted to write the RFC to think through the full flow—trials, upgrades, everything.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** But I will try it.

**Estevão Mascarenhas:** Hopefully that will work.

**Jose Farias:** Yeah, I think worth taking a look.

**Jose Farias:** I'm not set on using the gem. It may be less flexible if we want fancy subscription features.

**Jose Farias:** The upside is Stripe implementation could be done in 10 minutes. The downside is if we need custom features, we'd have to fork it.

**Jose Farias:** So there's a trade-off to weigh.

**Jose Farias:** One thing I didn't see: in your code snippets, we're only setting the pricing plan to free. Where do we update it in the webhook handler?

**Jose Farias:** In `handle_checkout_completed`, I'd expect to see a lookup by Stripe price ID and updating the workspace plan.

**Estevão Mascarenhas:** Let me check the webhooks.

**Jose Farias:** We need to update the workspace to a different plan after checkout succeeds.

**Estevão Mascarenhas:** I wrote a detailed plan with controller logic to create Stripe sessions and handle redirects, but it was too long to include here. When we create the checkout session, we set up the workspace plan. I'll check if that's sufficient.

**Jose Farias:** But we need to update the plan in the database after payment succeeds, right? That way the new limits apply immediately.

**Estevão Mascarenhas:** Yeah, that makes sense.

**Jose Farias:** So just because it's going to be like slightly unusual, I'll say what I'm thinking there.

**Jose Farias:** We have obviously a pricing plan model and that has a method called publicly available.

**Jose Farias:** `PricingPlan.publicly_available` returns an array of publicly available plans.

**Jose Farias:** You should be able to call `.find_by` on that array to match the Stripe price ID.

**Jose Farias:** Once you find the matching plan, get its ID and persist that to the database.

**Jose Farias:** That's how you swap the plans.

**Jose Farias:** That's what I'm thinking.

**Jose Farias:** We'd use different price IDs for different environments.

**Jose Farias:** I think we could make the pricing plan instances respond differently depending on `Rails.env`.

**Jose Farias:** It would be a conditional inside the `stripe_price_id` method: if it's production, use this ID; otherwise, use that ID.

**Jose Farias:** And that's how we can test in sandbox environments with the same plans.

**Jose Farias:** It's just they have different IDs for production and anything else.

**Estevão Mascarenhas:** Yeah, on my plan, I was thinking on using the Rails credentials because we already have those for all the environments, but it's not a credential like we could do.

**Jose Farias:** Inline should work. You want to debug quickly if something breaks, and the price IDs aren't confidential.

**Jose Farias:** Yeah, I think that's it.

**Jose Farias:** Everything else, honestly, looks good.

**Estevão Mascarenhas:** So I wouldn't oppose implementing this.

**Jose Farias:** I also wouldn't oppose using the gem if you think that would be a worthwhile investment or not investment because it would probably be quicker to implement but more difficult to maintain.

**Estevão Mascarenhas:** The pay gem expects an email attached to a model. We'd need to delegate workspace to return the owner's email. I'll test whether it requires much customization.

**Jose Farias:** I'd be surprised if it does. The author knows what he's doing and builds modular things. Likely just needs a `pay_customer` macro and an email method.

**Jose Farias:** I'd advise creating a `workspace.owner` method abstraction now—return the first user for now. That way, if we change ownership logic later, we just update that one method instead of refactoring everything.

**Jose Farias:** Cool.

**Jose Farias:** I don't think I have anything else on the RFC, so good to go there.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Yeah, no, no problem.

**Estevão Mascarenhas:** I think it's just us.

**Jose Farias:** I do think it's just us.

**Stevie Kim:** I don't know why they tortured me by putting this so early.

**Stevie Kim:** I think changed the time to an hour earlier, and I'm like, what?

**Stevie Kim:** Didn't Daniel just complain about it being too early yesterday?

**Stevie Kim:** And now I realize why, because, yeah, he declined all the meetings.

**Jose Farias:** Well, there you go.

**Jose Farias:** Yeah, apologies.

**Stevie Kim:** I'm not awake.

**Jose Farias:** Yeah, no worries.

**Jose Farias:** No worries at all.

**Jose Farias:** Do we want to just quickly go through the linear, like, the changes since yesterday on linear?

**Jose Farias:** Yeah, I think that'd be helpful.

**Stevie Kim:** Stuff's happening pretty fast, so it's good.

**Jose Farias:** Yeah.

**Jose Farias:** I can start, if that sounds good.

**Jose Farias:** Sounds good.

**Stevie Kim:** So, I...

**Jose Farias:** Completed that ticket that was sort of all-encompassing.

**Jose Farias:** I commented on it.

**Stevie Kim:** I just commented on it saying, like, okay, we talked about a bunch of things here.

**Jose Farias:** Let's treat this ticket as the competitor changes backfill.

**Jose Farias:** And that's finished.

**Jose Farias:** So I completed the ticket, and then I created other tickets for the rest of the issues.

**Jose Farias:** I do think...

**Jose Farias:** Oh, no.

**Jose Farias:** I was going to say one of them was a blocker, but no, I changed my mind on that.

**Jose Farias:** created two tickets that aren't completed.

**Jose Farias:** The rest were completed.

**Jose Farias:** I just created tickets to track the work.

**Jose Farias:** And they're both in the Stabilize Week label.

**Jose Farias:** One is switching workspaces requires a refresh.

**Jose Farias:** That's definitely weird and something we should address, but not something that impacts outside customers yet.

**Jose Farias:** So that's why I did...

**Jose Farias:** Um...

**Jose Farias:** And, what was the other one?

**Stevie Kim:** I would totally know that if my brain was online.

**Jose Farias:** Oh, here it is.

**Jose Farias:** No worries.

**Jose Farias:** The prompt count meaning is not clear.

**Jose Farias:** It represents the amount of prompting probed out of the total when it seems like it's just So, it's just something to do there.

**Jose Farias:** do think just like a slash and a number might be enough.

**Jose Farias:** But, anyway, nothing blocking.

**Jose Farias:** So, I created those two.

**Jose Farias:** And then, to wrap it up, what I was working on last night and planning on wrapping up this morning is this.

**Jose Farias:** Again, a stabilized weak ticket, not a blocker, which is odd.

**Jose Farias:** But,

**Jose Farias:** does require significant architecture, so that's why I tackled that.

**Jose Farias:** And it's, I talked about it yesterday, so I won't go into too much detail, but it's fixing the subcategory overview charts so that they obey the subset of prompts chosen by the workspace.

**Jose Farias:** So to be clear, this would be, okay, this is this workspace.

**Jose Farias:** It has some tracked competitors.

**Jose Farias:** How are those competitors performing on the subset of prompts that belong to the main subcategory?

**Jose Farias:** It's weird.

**Jose Farias:** Like, it's a lot to process, but I think that's what we want because the alternative is doing, how are the competitors doing on all the prompts chosen by this workspace?

**Jose Farias:** And that's just the main competitors tab.

**Jose Farias:** That's what it is.

**Stevie Kim:** Right, right, right.

**Jose Farias:** So this would be, same thing, how are the chosen competitors doing on the prompts chosen by this workspace that are, that belong

**Jose Farias:** Long to the subcategory.

**Stevie Kim:** I think that makes sense.

**Stevie Kim:** Yeah.

**Jose Farias:** I think so too.

**Jose Farias:** But I just, data is hard.

**Jose Farias:** Like sometimes Daniel or Marcel will come in and be like, no, that doesn't make sense.

**Stevie Kim:** I mean, as, yeah.

**Stevie Kim:** I mean, I think as a user, that's what they're going to want to see because like a brand could have so many different product lines and they want to be able to see how their, you know, content's performing for those specific product lines.

**Stevie Kim:** And they belong to different subcategories.

**Stevie Kim:** So against like their competitors in those subcategories.

**Jose Farias:** So I think that makes sense.

**Jose Farias:** Yeah.

**Jose Farias:** Cool.

**Stevie Kim:** Like I'm pretty confident, I'll say.

**Jose Farias:** Sounds good.

**Jose Farias:** Yeah, me too.

**Jose Farias:** And then the last thing I'll say is wrapping, after wrapping up that work this morning, I'll again, tackle a non-blocking ticket, but that requires re-architecture, which would be not duplicating brands anymore.

**Jose Farias:** And once we have that, I do believe that is the last like big architecture change that I see us having to make before launch.

**Jose Farias:** So that after that, I can move on to like all of the other things that I consider, quote unquote, less splashy, which is all the other tickets.

**Jose Farias:** That's it for me.

**Estevão Mascarenhas:** Awesome.

**Estevão Mascarenhas:** I can go next.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** So yesterday, in the morning, was tackling a bit of small tasks and bugs and fixes and improvements to the onboarding.

**Estevão Mascarenhas:** And in the afternoon, I was focused on the RFC for the billing.

**Estevão Mascarenhas:** I started with a large plan and what I shared in the RFC is like mostly the overview of the architecture of it.

**Estevão Mascarenhas:** So I planned this afternoon to be focused on it.

**Estevão Mascarenhas:** I still have some minor things that I want to work regarding to onboarding and competitors, because once I start...

**Estevão Mascarenhas:** With the billing, I would like to be more focused on it and not be like back and forth.

**Estevão Mascarenhas:** So, yeah.

**Estevão Mascarenhas:** So, Stevie, I left a comment for you on Liner about, for example, the suggested competitors.

**Estevão Mascarenhas:** That's the PR, Jose, that we were just discussing on the channel.

**Estevão Mascarenhas:** So we should now be showing all the brands, even if we don't have a public profile for that brand.

**Stevie Kim:** So, yeah, let me know if that's working properly.

**Estevão Mascarenhas:** Like I tested, but just let me know if this is what would be needed.

**Estevão Mascarenhas:** Perfect.

**Stevie Kim:** There's just one update.

**Estevão Mascarenhas:** One issue with BrandFetch: for some domains, they return bad results. For example, Ask Cody's logo is a random person from a review section.

**Estevão Mascarenhas:** I contacted BrandFetch about it. They say it's a technical issue they can't solve.

**Estevão Mascarenhas:** A stopgap solution would be adding a manual override in the admin panel. We upload logos to S3 for key brands like Cloud, and use those instead of BrandFetch.

**Estevão Mascarenhas:** The issue is that BrandFetch struggles with redirect domains. For example, cloud.com redirects to cloud.ai, and all logo fetchers struggle with this. Switching providers won't solve it.

**Estevão Mascarenhas:** The manual override is more precise and reliable than chasing better APIs.

**Jose Farias:** Yeah.

**Jose Farias:** Yeah.

**Jose Farias:** Oh, sorry.

**Stevie Kim:** This would help with current customers. An executive manager declined a demo for one of our customer logos (hyper-exponential) because they knew the customer would fixate on the wrong logo instead of listening to anything else. It degrades trust immediately.

**Stevie Kim:** If we add a manual override, we'll need to audit key logos proactively instead of being reactive.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Yeah, I agree.

**Jose Farias:** That sounds good.

**Jose Farias:** Following redirects is similar to what we do for citation URLs. I'm disappointed that logo APIs don't handle it—though I don't know if there's enough revenue in the API business to justify that work. Anyway, a manual override makes sense. It'll solve the problem regardless.

**Jose Farias:** Cool.

**Jose Farias:** Yeah.

**Estevão Mascarenhas:** Is this a launch blocker? Missing logos in the competitor list might be okay, but wrong logos for customer accounts is bad.

**Stevie Kim:** Showing the wrong customer logo is a problem. It erodes trust immediately, even though those accounts aren't paying Q1 revenue yet. Eventually we'll monetize them, but for launch it's a credibility issue. I'd call it a blocker.

**Estevão Mascarenhas:** This should be about an hour of work. We already have ActiveStorage and S3 set up, so it's just UI and conditional logic. I'll create a blocker task for it. If someone else has time, great—otherwise I'll do it.

**Stevie Kim:** I'll confirm with Daniel and Marcel that this is a blocker.

**Estevão Mascarenhas:** Cool.

**Estevão Mascarenhas:** Nice.

**Estevão Mascarenhas:** Okay.

**Jose Farias:** I tested onboarding with meta.com yesterday. The description came back empty. I wasn't sure if the workflow failed.

**Estevão Mascarenhas:** Meta.com is Facebook's domain?

**Jose Farias:** Yeah. The onboarding flow went: CTA > enter domain > investigate > fetch logo (correct) > confirm domain > fetch profile (blank). The description field was empty where there should be a company blurb.

**Estevão Mascarenhas:** Okay, thanks.

**Estevão Mascarenhas:** I will check it out for meta.

**Estevão Mascarenhas:** Okay.

**Stevie Kim:** I ran into an issue in the admin panel doing brand research. There's a bug in the basic research workflow. I started investigating, but had to leave for dinner.

**Stevie Kim:** I can check Render logs but can't debug the CheckThat side anymore. There are a lot of failed jobs in basic research, and the UI pings indefinitely. I'm not sure what's happening. Can anyone check this, or I'll dig in later today?

**Estevão Mascarenhas:** You mean the Temporal jobs for workflows?

**Stevie Kim:** Yeah, for the workflows.

**Jose Farias:** That might be the same issue as meta.com. If a Temporal workflow fails, the UI doesn't handle it gracefully—not in the admin, not in onboarding.

**Jose Farias:** I'm surprised workflows are failing. Maybe it's fetching the website and hitting bot detection or similar?

**Estevão Mascarenhas:** I was testing basic research yesterday and it was working fine. I didn't touch the workflow.

**Estevão Mascarenhas:** The only change I made was to the brand lookup endpoint. It was returning brands without data (empty description, no profile). I made it more restrictive—now we only return brands we have data for.

**Estevão Mascarenhas:** That's the only change. This is weird. Can you send a link to the failed jobs?

**Jose Farias:** This isn't new. Marcel mentioned research workflows hanging—appearing to run for days. We told him they were definitely failing, just silently. So the workflow fails without the UI knowing.

**Jose Farias:** This needs investigation. The answer is probably in the Temporal logs, but we need to check soon—they only keep a few days of history.

**Stevie Kim:** The Temporal logs should be in CheckThat, but I'm not sure about the new organization.

**Jose Farias:** We recently deployed a CheckThat output thing on Render, but I'm not sure we're using it yet. There are two places to check—it'll be in one of those.

**Jose Farias:** Also, I just deployed a massive dependency update. Let me know if anything's broken.

**Jose Farias:** Does anyone have anything else?

**Stevie Kim:** I'm testing the onboarding flow and some workspace features. Leonardo is setting up automated testing while I do manual testing.

**Jose Farias:** Great. See you all tomorrow.

**Stevie Kim:** Bye.

**Jose Farias:** Bye-bye.

**Estevão Mascarenhas:** Thank you.
