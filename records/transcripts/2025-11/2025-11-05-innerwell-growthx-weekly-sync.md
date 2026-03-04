# Innerwell <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-05
time: 16:31 UTC
duration: 27 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill, Jakub Rudnik, Akina Tran, Noa Cornberg, Andrew Berman
speaker_note: All speakers correctly identified from transcript and matched to calendar invitees. Andrew Berman was cc'd but did not speak during the call. Andi Bailey was invited but did not participate.
fathom_recording_id: 99405506
fathom_url: https://fathom.video/calls/462971486
share_url: https://fathom.video/share/Xf5SA_cZ935wtHmg68vSvo7RAyJCMp22
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Innerwell's technical team has successfully unblocked the redirect implementation process, eliminating the need for GrowthX to access GitHub. Matthew and Jakub confirmed that Innerwell's in-house process works and GrowthX will follow Ilya's Loom tutorials to complete remaining city page and `/availability` redirects. The team also aligned on a two-track content roadmap: immediately scale ketamine blog content to capitalize on proven traction, and test comparison content (e.g., "Innerwell vs. Spravato", "ketamine therapy vs. SSRIs") using a proven SaaS playbook (informational → alternatives → competitor comparison) to capture high-intent medical search traffic.

---

## Context

This is a weekly operational sync between GrowthX and Innerwell on their content marketing engagement. GrowthX provides B2B content marketing services ($200k+/year engagements), and Innerwell is a telehealth platform focused on ketamine therapy. The relationship is multi-month and highly technical, spanning SEO infrastructure, content publishing, and analytics. This meeting occurred at the midpoint of a large technical SEO cleanup project — migrating blog URLs from the old `/reflections/` structure to condition-specific structures like `/ketamine/`, along with setting up comprehensive 301 redirects and improving site architecture. The team is executing on a content roadmap that includes both immediate tactical wins (scaling ketamine content) and strategic initiatives (testing comparison content to capture high-intent medical search traffic).

---

## Relevance

- **To GrowthX Delivery:** Innerwell's technical team has successfully built a working redirect process in-house, eliminating the need for GrowthX to gain GitHub access. This is a good example of client capability — when GrowthX provides guidance (via Loom tutorials), internal teams can execute. The comparison content strategy test (ketamine vs. SSRIs, Innerwell vs. Spravato) represents a potential replicable playbook for medical/pharma verticals using the proven SaaS content model (informational → alternatives → direct comparison).

- **To GrowthX Business Development:** Innerwell is expanding the engagement scope. Beyond technical cleanup, they're investing in new initiatives (comparison content, city page expansion for EMDR and other services) and process improvement (preventing future URL structure errors). This signals product-market fit and account growth.

- **To CheckThat:** Innerwell's content roadmap focuses heavily on SEO visibility for ketamine therapy and competitive treatment comparisons. This is a high-volume, high-intent medical search category where AI visibility and search result quality will be critical differentiators.

---

## Overview

- **Redirects Unblocked:** Innerwell's team has a working redirect process, making GrowthX's GitHub access unnecessary. GrowthX will now use Innerwell's Loom tutorials to implement the remaining redirects.
- **New Blog URL Process:** New blogs will now use the new `/ketamine/` URL structure. GrowthX will fix recent posts and create a process to prevent future errors.
- **Content Roadmap Defined:** The roadmap has two tracks: 1) immediately scale ketamine blog content, and 2) test comparison content (e.g., "Innerwell vs. Spravato") to capture high-intent search traffic.
- **Technical Audit Planned:** GrowthX will run a full technical SEO audit (using Screaming Frog) after all redirects are live to find and fix any new errors.

---

## Key Topics

### Technical SEO & Redirects

  - **Redirect Process:** Innerwell's team has a working redirect process, making GrowthX's GitHub access unnecessary.
      - **Action:** GrowthX will use Innerwell's Loom tutorials to implement the remaining redirects (city pages, old `/availability` pages).
  - **Index Page Request:** A Prismic-based index page is needed to organize content.
      - **Action:** Innerwell will scope the design and assign development.
  - **Mental Health Services Page:** This high-level landing page is a prerequisite for all related content redirects.
      - **Action:** Innerwell will develop this page after the technical cleanup is complete.
  - **Looker Dashboard:** The dashboard will be updated with new regex expressions to reflect the new URL slugs, but only after all redirects are live.

### Blog URL Structure

  - **Problem:** New blogs are using the old `/reflections/` URL structure instead of the new `/ketamine/` structure.
  - **Cause:** A communication error on GrowthX's side.
  - **Solution:**
      - **Fix:** GrowthX will move the recent posts to the correct URL structure. If they have no traffic, a simple URL change is sufficient; otherwise, a 301 redirect is required.
      - **Prevention:** GrowthX will create a process to ensure all future blogs use the correct URL structure.

### Content Roadmap & New Initiatives

  - **Ketamine Content Scaling:** GrowthX will immediately increase the cadence of ketamine-related blog posts, building on a proven content strategy.
  - **Comparison Content Strategy:**
      - **Goal:** Capture high-intent search traffic by comparing Innerwell's services to competitors and other treatments.
      - **Test Cases:**
          - Innerwell's ketamine therapy vs. SSRIs (e.g., Lexapro)
          - Innerwell's oral tablets vs. Spravato (a key competitor)
      - **Playbook:** Use a proven SaaS content model:
          - High-level informational page (e.g., "What is Spravato?")
          - Alternatives page (e.g., "Spravato Alternatives")
          - Direct comparison page (e.g., "Innerwell vs. Spravato")
      - **Action:** GrowthX will research keyword volume and draft a test template for Innerwell's medical team to review.
  - **Programmatic City Pages:** Expanding programmatic city pages for other services (e.g., EMDR) is a future possibility, pending data analysis.

---

## Action Items

**Akina Tran (Innerwell)**
- Send Ilya's Loom tutorial (redirects/breadcrumbs/clinician block) to Jakub & Matt; then Isra test/implement, city and `/availability` redirects, Looker update, and Screaming Frog
- Draft Prismic index page design; then start Mental Health Services landing page
- Review 4 pending articles; then notify Matt

**Jakub Rudnik (GrowthX)**
- Confirm Isra's Prismic/index-page design capability; then request that Akina send design request to Ilya
- Restore 'Mental Health Services' landing page bullet point in the tech SEO documentation

**Matthew Alves-Hill (GrowthX)**
- Fix new blog URLs: set ketamine tag/subfolder for recent posts; move indexed posts with 301 redirects; notify Shonali
- Research med-comparison topics and keyword volume; draft 1-2 test templates (ketamine vs. SSRIs, Innerwell vs. Spravato); send to Akina for medical team review
- Set up Airtable automation: automatically add published articles to the end of the content board

---

## Transcript
**noacornberg:** She's not here?

**Jakub Rudnik:** No, yeah, no.

**noacornberg:** One minute, I'll ping her.

**noacornberg:** Oh, no, man, no.

**Matthew Alves-Hill:** Where are you actually based, Noah?

**noacornberg:** I don't I'm I'm in Tel Aviv.

**noacornberg:** I'm

**Matthew Alves-Hill:** Okay, yeah, and you got it.

**noacornberg:** Oh, glasses, new glasses.

**Matthew Alves-Hill:** I have to, getting old.

**noacornberg:** Yeah, yeah, yeah, I got mine today.

**noacornberg:** I purchased one, so I'm waiting for them.

**noacornberg:** Yeah, I wear contact every day, so my eyes are killing me because I'm on the screen every day for like 12 hours.

**noacornberg:** So I'm like, okay, I will get glasses.

**noacornberg:** So I went to do it today.

**Matthew Alves-Hill:** And yeah, it's a sign of getting old.

**Matthew Alves-Hill:** Yeah, I think it's going to when I put them on, I feel serious.

**noacornberg:** Hi, Akina.

**noacornberg:** Hi, Akina.

**noacornberg:** So I'm the only one without eyeglasses, so for the next one, I will bring mine.

**noacornberg:** I'm with contact right now.

**Akina Tran:** Yeah, I like to wear my blue light glasses, even with my contacts on.

**noacornberg:** Ah, you are with contact and blue light?

**Akina Tran:** Mm-hmm.

**Jakub Rudnik:** Okay.

**Akina Tran:** I think my contacts actually have some blue light.

**noacornberg:** Yeah, there's blue light.

**Akina Tran:** Yeah, but the only problem is double protection.

**Jakub Rudnik:** Yeah, yeah, yeah, I get dry with contact lenses, so in the winter even more so.

**Matthew Alves-Hill:** Okay, we get the subject, we can move forward.

**noacornberg:** A bit to know about each other.

**Matthew Alves-Hill:** Yeah, cool, let me pull up our agenda.

**Matthew Alves-Hill:** Cool, I think the first thing, oh, my laptop's going to die here.

**Matthew Alves-Hill:** I think the first thing would be, would be cool to get a bit of an update from your side, Akina, on the redirects.

**Matthew Alves-Hill:** looks like there was, like, some progress made when we were having a look since last week.

**Akina Tran:** Yes, so we finished the redirects on this date.

**Akina Tran:** I think you guys still need access, right, on the GitHub to complete...

**Matthew Alves-Hill:** Yeah, exactly.

**Jakub Rudnik:** So I think that's right, just to jump in, sorry, the top, those are all done correctly, and we can talk about the, because there's a little bit of a delay, like traffic's moving around, I could talk about that in a minute if that's necessary, but from like an execution of additional redirects, I don't know how you all did those, but if it's like something that we can just do now, because they were set up correctly, what we had needed GitHub for was like, if your team hadn't figured out that, the proper redirects, like we had some support, but since they're being done on your set, I don't know, I just don't know if that's necessary, so I want to know how you're doing that, and if we can jump in at this point, or how that works.

**Akina Tran:** Yeah, can definitely, perfect timing, Ilya just sent over a loom for how to migrate the rest of them, or how to add the links to the cities, and then the other stuff, so.

**Akina Tran:** I think we should, I'll send that over and I think we should be good there.

**Jakub Rudnik:** Okay, so then we'll take a look, we'll confirm that, let's do that, Matt, quickly, so we can just confirm with Isra, if that's not necessarily great, and so let's confirm that that's all works, that the redirects are set up properly, and then we can move forward with actually doing the city pages, as well as the old ketamine state pages, the slash ability pages, availability versions, we also want to do redirects with those, once, once we know the process is working, but we just need to confirm that, that would, if that all works, based on that loom, and we have access, then GitHub, and all that stuff, we can just forget, and set off to the side, because y'all have, knocked that out.

**Akina Tran:** Okay, and then, aside from the redirects, you guys are working on the injection?

**Akina Tran:** Repository, right?

**Jakub Rudnik:** So we, in my understanding, that was over with your team with a, like, a ticket person on your team to design.

**Akina Tran:** I've outlined how it would work and created, so if that's not correct, let me Oh, I thought you guys, I thought that was one of the tests that the Prismic expert on your side was going to test out.

**Akina Tran:** Or was he only doing the redirects?

**Jakub Rudnik:** And we're talking about the, let me, I'll just share my screen so we have it.

**Jakub Rudnik:** Like, the index type of pages here.

**Jakub Rudnik:** Matt, have you worked with Isra on anything like this that was not on my radar?

**Matthew Alves-Hill:** No, just the, just the redirect process for Isra that he's been briefed on.

**Akina Tran:** Okay, so he only did the redirect, okay.

**Akina Tran:** But, yeah, let me follow up with Isra.

**Akina Tran:** Ilya, to start on that index page request.

**Akina Tran:** Okay.

**Jakub Rudnik:** I don't know Isra on our side's skills as well, but this is something we can show on this today and see what he says there.

**Jakub Rudnik:** I just, yeah, that wasn't, so just some misalignment, but yeah, we'll follow up there, but, and then we'll get back to you, and then you can send it over to Ilya if that's not his skill set.

**Jakub Rudnik:** He's been more on the publishing and technical side, but potentially can design this as well, just unsure at this point.

**Akina Tran:** Okay, I think in addition to the redirect recording, they, Ilya also recorded how to add the breadcrumbs, and then the clinician block too.

**Akina Tran:** So if you guys are able to help with that, that would just help us speed up the process on transitioning the technical.

**Jakub Rudnik:** Okay, yeah, we'll test those, let's make sure we can do it, and then hand over to Isra, assuming everything's good there.

**Jakub Rudnik:** Just so we all have awareness, I've kind of cleaned it up and then added a couple small details to the technical SEO recommendations, like at the top of this page.

**Jakub Rudnik:** It's getting messy with like some things checked off in between, so just organize between ketamine and mental health pages, and then any additional like, many projects we can add here, but these should be in chronological order.

**Jakub Rudnik:** A lot of this is in flight already, so we'll just continue to check off.

**Jakub Rudnik:** I wanted to give clarification on the additional, like what's outstanding at this stage.

**Akina Tran:** Okay, now that's helpful to have.

**Jakub Rudnik:** Yeah, so it's just getting a little messy after like a month of some things getting completed, some having additional steps and whatnot.

**Matthew Alves-Hill:** and will, once you you

**Matthew Alves-Hill:** Once the redirects are completed, then we can go in and clean up the looker as well.

**Matthew Alves-Hill:** We'll have to change the looker to reflect the new slug parts.

**Matthew Alves-Hill:** So once that's done, then the looker will be tidied.

**Matthew Alves-Hill:** We did make the changes, Akina, that you asked for, but because the way that the regex expressions are in there, they're going to only to update them once the redirects are done.

**Matthew Alves-Hill:** So I'll hang you in.

**Matthew Alves-Hill:** We could share more on that once they're set up.

**Akina Tran:** Okay.

**Jakub Rudnik:** Okay, sounds good.

**Jakub Rudnik:** There's one more on, I think that was outstanding.

**Jakub Rudnik:** I think it was with your development team, but like a mental health services, high-level landing page.

**Jakub Rudnik:** And that was to here.

**Jakub Rudnik:** And then now there's outline like the, oh, I didn't mean.

**Jakub Rudnik:** Um, yeah,

**Jakub Rudnik:** Sorry, I'll make sure this is what it was, and I think I just deleted the bullet point here, and I moved around, but the mental health services, like how we have an academy page, and an EDMR, and so on.

**Jakub Rudnik:** Is this with your team, and if so, is there any progress on this one?

**Akina Tran:** This one will come after all the technical stuff, I believe.

**Jakub Rudnik:** Okay, so anything, basically anything under that will fall, fall behind, because we don't want to redirect anything to a URL path that doesn't exist, and that it won't exist until we have this page, so just for everyone's awareness, and keeping on top of order of operations, and then I'll just restore this page, is that it?

**Akina Tran:** Okay, the other thing on redirect, I just commented on that thread with Shanali, so for the blog pages, I thought for new blogs, we're going to use the new URL structure.

**Akina Tran:** The, that we had for the 301 redirects that don't use reflection.

**Akina Tran:** I'm not sure that's something that, that the publisher would set up and then Shinnelli updates, or that you would, we'd have to publish it and then change the redirect.

**Matthew Alves-Hill:** Um, I think that's, Jakub, I think that's more a question for you on the vacations.

**Matthew Alves-Hill:** We could redirect.

**Matthew Alves-Hill:** I'll have to, can you say that one more time?

**Akina Tran:** Sorry.

**Akina Tran:** Yeah.

**Akina Tran:** So for the blog pages, we had the 301 redirect project to change it from reflections to the different conditions and whatnot.

**Akina Tran:** So for new blog pages, like the ones that Shinnelli just published today, they're still showing under the old URL schema.

**Akina Tran:** How do you want to, how all the changes there?

**Akina Tran:** So they matched all the old ones we updated.

**Jakub Rudnik:** So they should now be under, like, ketamine, like, under that sub, like, conditions type of folder, is that right?

**Akina Tran:** Yeah, let me share my screen.

**Akina Tran:** So we migrated all the old reflections blogs to these so that they're more crawlable for all the conditions they filter.

**Akina Tran:** But then for the new ones that she published, they all fall under this old URL structure still.

**Jakub Rudnik:** Yeah, do we?

**Jakub Rudnik:** And I'm less on top of the topics that we did this week, but are they ketamine-specific topics from that new strategy?

**Matthew Alves-Hill:** Yeah, that was lost in translation for me.

**Matthew Alves-Hill:** That's on me.

**Matthew Alves-Hill:** We can change that going forward.

**Jakub Rudnik:** Yeah, so those should just be moved to the ketamine tag, and then they should have the ketamine subfolder.

**Jakub Rudnik:** And then as long as we just do that.

**Jakub Rudnik:** And if they're brand new, basically, I would just see if they've actually been indexed and if there was any impressions or anything yet.

**Jakub Rudnik:** And if not, just change the URL and it doesn't matter if there was already some traction, set an actual redirect.

**Matthew Alves-Hill:** Yeah, I'll have a look because it's been, we've been in, this would be like the third or fourth week.

**Matthew Alves-Hill:** So it should be fine to just change them.

**Matthew Alves-Hill:** Like, you know, I'll have a look and then I'll, I'll let you know what we're going to do, but that's just, that's just a miss on my end.

**Matthew Alves-Hill:** But there's no reason why I'll, I'll make sure that's changed going forward.

**Matthew Alves-Hill:** And then we're obviously like working through the ketamine cluster now.

**Matthew Alves-Hill:** So they'll all just live in that, in that sub folder.

**Akina Tran:** Okay.

**Akina Tran:** Sounds good.

**Akina Tran:** The, oh, so.

**Akina Tran:** I don't know.

**Akina Tran:** Well, so Ilya commented on.

**Akina Tran:** And the stuff you guys sent on the redirect and the access to the Git repository.

**Akina Tran:** And he says he doesn't think this will work with our next 14 with pages router as redirects are not supported.

**Akina Tran:** We would need to migrate to newer next JS and app routers.

**Jakub Rudnik:** I think that's all unnecessary.

**Jakub Rudnik:** Anyway, if the new, if your redirect, however it's set up by your team, if that works, then all of that, we can just put a pin in and move to like an archive or whatever you want.

**Jakub Rudnik:** I think about it, but shouldn't be necessary, assuming we can redirect in the same way your team is doing it right now.

**Akina Tran:** Okay.

**Akina Tran:** Do you still need access to the Git repository then?

**Jakub Rudnik:** We should not.

**Akina Tran:** Okay.

**Matthew Alves-Hill:** With the looms that, with the looms that you guys send us, we can just pass that on to Israel and you should be able to do the same thing.

**Matthew Alves-Hill:** you.

**Akina Tran:** Okay, sounds good.

**Akina Tran:** And then, so once the technical stuff is finished and we have the mental health page out, what are like next steps here just for end of year and roadmap stuff?

**Jakub Rudnik:** Yeah, I think there's two different options and sorry Matt if I jumped in, but there's like expanding the Ketamine blog content is like one of those priorities on the editorial front and I think we'll be doing some of that anyway.

**Jakub Rudnik:** Matt, you can speak to that cadence.

**Matthew Alves-Hill:** Yeah, yeah, well, we can up the cadence now once this is sorted out, like some more of the, if you remember how this structured kind of like the general SEO stuff and then like the more programmatic Ketamine therapy for specific.

**Matthew Alves-Hill:** Conditions or population types, et cetera.

**Matthew Alves-Hill:** So we can, like, I would say we would up the cadence to a mix of those, like semi-programmatic and then the building out the cluster as well.

**Matthew Alves-Hill:** And then I would say the ketamine roadmap is pretty well populated now for the remainder of the year.

**Matthew Alves-Hill:** And then we can decide to move on to the mental health in the same approach.

**Matthew Alves-Hill:** That's how I would, that would be my plan.

**Matthew Alves-Hill:** don't know, what do you think, Jakub, if you add anything to that?

**Jakub Rudnik:** Yeah, that's what I had from an editorial strategy.

**Jakub Rudnik:** We felt all pretty aligned on that a month or so ago and Matt presented it.

**Jakub Rudnik:** And then the other piece that we had generally on the roadmap and we'll have to see how these respond.

**Jakub Rudnik:** And there's some data to look into, but filling out additional city pages for, like ketamine has, would have some gaps.

**Jakub Rudnik:** Like, there's just additional programmatic on the location-based pages.

**Jakub Rudnik:** We can also do...

**Jakub Rudnik:** You know, we could do cities for EMDR.

**Jakub Rudnik:** can do cities for other services they all offer.

**Jakub Rudnik:** It's just a matter of like, do we have any traction and reason to do those, right?

**Jakub Rudnik:** It's like, is there?

**Akina Tran:** Yeah.

**Jakub Rudnik:** So I haven't mapped those pieces out.

**Jakub Rudnik:** There's still work to be done on it.

**Jakub Rudnik:** Like if that's, we know the Ketamine blogs work.

**Jakub Rudnik:** We know the Ketamine location pages work.

**Jakub Rudnik:** When we get beyond that, that is still kind of a black box maybe because we've been focused on cleaning those up so far.

**Jakub Rudnik:** So that's like the rough other idea that we could go into.

**Jakub Rudnik:** It's like your appetite plus what we find in the data to date.

**Akina Tran:** Got it.

**Akina Tran:** Okay.

**Akina Tran:** What about...

**Akina Tran:** Actually, no, we can pin that for next week.

**Akina Tran:** I think let's wrap up the technical stuff.

**Akina Tran:** I'll have them flesh out the index page and start work on the mental health page.

**Akina Tran:** And then I'll share the loom with you guys and let me know if you have any questions there for the updates on the breadcrumbs and the rest of the city redirects.

**Akina Tran:** And then we can revisit the city stuff in parallel with expanding the ketamine content.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** And the ketamine stuff is the easiest.

**Jakub Rudnik:** Like, I think that's the one that we just, we expand right away and can work through that as we do the deeper research and map out the other programmatic areas.

**Jakub Rudnik:** Like that will take more time, but where is the, kind of means it's simpler just being editorial in general.

**Jakub Rudnik:** And also we've already done that work and we know that the ketamine blogs like have traction.

**Jakub Rudnik:** So that's just like the, that's the layup and it should be pretty seamless to go from where we are now to just expanding that and the others we can do in tandem.

**Jakub Rudnik:** And I can spend my time mapping that while Matt's expanding the editorial.

**Jakub Rudnik:** So should be able to do both.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** And if there's anything else, you know, we've like aligned on those pieces general.

**Jakub Rudnik:** And then if there's any other areas to expand on or that you're interested and happy to, you know, scope those out or think on how that would fit into all the work we're doing already.

**Jakub Rudnik:** So we're open for sure.

**Jakub Rudnik:** Just that's where my brain was.

**Akina Tran:** Okay.

**Akina Tran:** I did have a question for the content topics.

**Akina Tran:** So where do we land with like medication, like talking about like specific medications, like ketamine therapy and SSRIs or like Innerwell's ketamine therapy versus like spervato and things like that?

**Matthew Alves-Hill:** It hasn't.

**Matthew Alves-Hill:** I don't think we've touched on that since I joined.

**Matthew Alves-Hill:** It is something that I've noticed.

**Matthew Alves-Hill:** There's definitely like I've seen in the keyword research, there's definitely like potential for like comparison style articles.

**Matthew Alves-Hill:** There's definitely search volume there.

**Matthew Alves-Hill:** It's definitely something I would say is worth doing.

**Matthew Alves-Hill:** I just don't, like, I don't know.

**Matthew Alves-Hill:** It would be interesting to know a bit more about, like, how delicate, I guess, that could be.

**Matthew Alves-Hill:** Is that a worry if we're comparing, like, straight up other medications?

**Matthew Alves-Hill:** I guess I could map it out and we could, like, run through, like, okay, this is a good topic based on your knowledge.

**Akina Tran:** Yeah, I would say, let's see, like, what the volume is there.

**Akina Tran:** Like, what are we missing out on that we're not getting from the other stuff?

**Akina Tran:** And let's, like, do, like, one test template and we'll send it to our medical team to review and see if there's concerns there.

**Akina Tran:** But I think for the most part, we should be okay.

**Akina Tran:** I think there's definitely appetite since a majority of the people that come in for ketamine therapy have probably tried some version of SSRIs, whether it's, like, Lexapro or, you know, one

**Akina Tran:** So if we just take one that's like one of the bigger medications and test that, let's see how that does.

**Akina Tran:** And then if it works well, we can expand on that topic.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** That's cool.

**Matthew Alves-Hill:** I'll add that to the next week and then we can chat about it.

**Matthew Alves-Hill:** But yeah, there's definitely, like I've definitely seen, it's definitely worthwhile doing.

**Matthew Alves-Hill:** There's definitely volume there and it would help us build out, like, it would be good for our domain authority as well to be talking about some other stuff.

**Matthew Alves-Hill:** It's good for internal linking.

**Matthew Alves-Hill:** So yeah, cool.

**Jakub Rudnik:** I would imagine those are good on the conversion front as well.

**Jakub Rudnik:** Just thinking about like the hierarchy of all the topics.

**Jakub Rudnik:** So I could see those working well, assuming that again, the volume's there.

**Akina Tran:** Yeah.

**Akina Tran:** So there's like two kind of things.

**Akina Tran:** There's like one, like ketamine therapy versus the psychiatric medications.

**Akina Tran:** Anxiety and depression, but then there's also the bigger one would be like ketamine there, Innerwells, oral tablets, and then like Spravato.

**Akina Tran:** We don't prescribe Spravato.

**Akina Tran:** Spravato is like kind of a competitor, but that's like the most well-known ketamine pill, if you will.

**Akina Tran:** And that's like a big competitor in our search.

**Akina Tran:** So I'd be curious if we could test one that's medication and maybe one that's with Spravato versus like how we do it.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Yeah, that's, that's, um, got it.

**Jakub Rudnik:** When, so this type of field is different than where I might like pass with SEO, but just doing some quick checks, like when we do SaaS content to backup half a step, I do like software lists, like best CRM.

**Jakub Rudnik:** And then you do like, you pick a CRM, like HubSpot and you do HubSpot alternatives, and then you do HubSpot for Salesforce.

**Akina Tran:** And it looks like same kind of thing will work here.

**Jakub Rudnik:** Like,

**Jakub Rudnik:** Because Bravado alternatives does have organic traffic, like there is a page, it's, you know, drugs.com has this and a few others.

**Jakub Rudnik:** And so it looks like we can both, again, Matt will can like scale, see how far this scales, but the like high level drug type of informational page, then the alternatives to that specific drug, and then that drug versus Innerwell, all those would be different pages.

**Jakub Rudnik:** And it looks to me very, very quick glance, but that type of playbook, Matt, that we do in SAS would work over here as well, potentially.

**Jakub Rudnik:** So just to call that up before I lose track of that little detail I found.

**Akina Tran:** No, that's good to know.

**Jakub Rudnik:** So, you know, okay, I put that, it's probably not the perfect place for it, but I just put it below the technical recommendations as a checklist.

**Jakub Rudnik:** So we keep tabs on kind of this, like that is another project is the, by the way, Jacob, I see you have a couch.

**noacornberg:** Now, so, and your dog is sleeping, so, yeah, I see progress.

**noacornberg:** It's another progress.

**Jakub Rudnik:** Yeah, I moved the camera so we can, like, watch her just snore behind me.

**Jakub Rudnik:** It's good.

**noacornberg:** If you need a dog sitter, Akina is very good at it, by the way.

**Jakub Rudnik:** She barks at the mailman, but otherwise, very sweet dog.

**Jakub Rudnik:** She'd sit on your lap all week long.

**noacornberg:** My dog, my dog only sleeps, so it doesn't do anything, only sleeps.

**noacornberg:** And eats.

**Jakub Rudnik:** You, Matt and Noah, you are the two that call me out in the office each week.

**Jakub Rudnik:** Noah's complimented me on the progress.

**Jakub Rudnik:** Matt's telling me, like, that picture went from unwrapped to wrapped.

**Jakub Rudnik:** So I'm glad people are keeping tabs.

**Jakub Rudnik:** need to, like, give me a line.

**noacornberg:** It's, yeah, it's a part of the progress.

**noacornberg:** It's a part of the progress.

**Jakub Rudnik:** So.

**Matthew Alves-Hill:** I was just going to add, Noah, Shonali is into the air table.

**Matthew Alves-Hill:** We've arranged it so that she's clear on what's been staged on our end.

**noacornberg:** Yeah, it's published.

**noacornberg:** It's published.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** Yeah, I'm going to set up an automation so that we know to add those to the end once it's published.

**noacornberg:** Yep.

**noacornberg:** Don't like, I told you that also last week, I'm trying to put some moderation into our, in our development so we can, you know, Q&A and everything will be better.

**noacornberg:** So all good.

**Matthew Alves-Hill:** Okay, rad.

**Matthew Alves-Hill:** I think that is everything.

**Matthew Alves-Hill:** Akina, there's two articles, I think, just waiting for your review from last week.

**Matthew Alves-Hill:** So, and then two more this week, but then next week, we'll, I'll scope out and do a little bit of research into these alternatives ideas.

**Matthew Alves-Hill:** And then we will, we'll ramp up the content as well from next week.

**Matthew Alves-Hill:** So, yeah.

**Akina Tran:** Okay, sounds good.

**Akina Tran:** And I just said.

**Akina Tran:** Okay.

**Akina Tran:** So let me know if there's anything missing there.

**Akina Tran:** And then, yeah, keep me posted on the blog publishing stuff for the URL that needs to be done on Chanel even.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** That sounds good.

**Jakub Rudnik:** We'll follow up with those this week, I think, so we can make sure those keep moving and we can get those redirects.

**Jakub Rudnik:** One thing I wanted to add was just technical errors.

**Jakub Rudnik:** We fixed a lot of stuff, but after all these redirects are set and everything, just for next steps, I'll want our side to run a screaming frog analysis and use our SEO tools to look for other additional errors.

**Jakub Rudnik:** Things just have popped up and always want to do this after a lot of technical changes.

**Jakub Rudnik:** So I don't know what will come out of that, Akina, but from next steps, technically, I think we can consider all these redirects and the mapping and the cannibalization in a phase one, but assume that there will be some other things to fix coming out of that.

**Jakub Rudnik:** Hopefully we can.

**Jakub Rudnik:** handle a lot of that, too, but just want to call that out that I'll want to confirm that things are working properly and things after the next week or two.

**Jakub Rudnik:** So I put that into the roadmap as well.

**Akina Tran:** Cool.

**Jakub Rudnik:** Okay.

**Akina Tran:** Sounds good.

**Jakub Rudnik:** Thank you both.

**noacornberg:** Thank you.

**Akina Tran:** Thank you.

**noacornberg:** Bye.

**noacornberg:** Bye.
