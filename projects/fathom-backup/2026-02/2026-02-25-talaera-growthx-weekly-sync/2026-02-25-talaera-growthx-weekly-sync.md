# Talaera <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-25
time: 17:00 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants:
  - Anita Anthonj (Talaera, external)
  - Paola Pascual (Talaera, external)
  - Mel MacMahon (Talaera, external)
  - Aida Knezevic (GrowthX)
  - William Leborgne (GrowthX)
  - Kathy Lam (GrowthX)
fathom_recording_id: 125296151
fathom_url: https://fathom.video/calls/578565738
share_url: https://fathom.video/share/k8BX1s3eAvxj_MVevjez7xgydaKq-uM4
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Talaera's content strategy is delivering exceptional SEO results: a high-difficulty commercial keyword jumped from position 26 to page one with AI Overview placement. A Cookiebot configuration issue was resolved by geo-targeting to EU only, which should restore GA4 traffic visibility. Next steps include automating content publishing via WordPress API integration and identifying additional B2B traffic opportunities.

---

## Context

Talaera and GrowthX conducted their weekly progress sync to review SEO performance, website optimization plans, and content workflow improvements. The Talaera team recently conducted a successful webinar on business English communication, which generated positive feedback and demonstrates strong product-market fit. GrowthX has published 19 targeted blog articles and is now seeing measurable organic traffic, with over 400 visitors from Google Search in recent weeks—significantly higher than typical early-stage content campaigns (usually ~200 visitors).

The meeting also surfaced a critical technical issue: a Cookiebot implementation was inadvertently blocking Google Analytics tags from firing on non-EU regions, causing a major discrepancy between GA4 (which showed low traffic) and Google Search Console (which accurately reported 400+ organic visitors). Paola Pascual resolved this by configuring Cookiebot to fire only in the EU. Additionally, the team discussed automating the content staging process through WordPress API integration to reduce manual copy-paste work and explored opportunities for B2B-focused landing pages to complement the B2C traction they're already seeing.

---

## Relevance

- **SEO & SEM**: Keyword ranking breakthroughs, AI Overview placement, content strategy impact on organic visibility
- **Website Optimization**: Pricing page feature grid, new "Talaera Professional" tier page, one-on-one coaching positioning
- **Analytics & Data Quality**: Cookiebot compliance issue resolution, GA4 vs. GSC discrepancy diagnosis, tracking accuracy
- **Content Operations**: WordPress API automation, workflow efficiency improvements, content publishing cadence
- **Product & GTM**: Webinar success, "Business English for Engineers" positioning for individual learners, tier value propositions
- **B2B Growth**: Opportunity to drive more B2B traffic alongside existing B2C momentum

---

## Overview

- **SEO is delivering exceptional results:** A key commercial keyword ("best corporate language training platforms...") jumped from \#26 to page one, now appearing in AI Overviews. This is a significant win, as the keyword has a high difficulty score of 50.
- **A cookie bot issue is skewing GA4 data:** The bot is blocking analytics tags from firing before consent, causing a major discrepancy between GA4 (low traffic) and Google Search Console (GSC), which shows \>400 organic visitors.
- **Website updates are planned to improve conversion:** The pricing page will get a feature grid, and a new "Talaera Professional" page will be created to clearly define the tier's value proposition.
- **Content publishing will be automated:** GrowthX will use a WordPress API key to stage content, saving manual effort.

---

## Key Topics

### SEO Performance & Strategy

  - **Keyword Wins:**
      - **"best corporate language training platforms..."** → Jumped from \#26 to page one, now in AI Overviews.
          - **Significance:** This is a high-difficulty (score 50) commercial keyword, making the rank jump a major success.
          - **Driver:** The homepage is ranking, supported by the site's overall authority on corporate training.
      - **"Business English for Engineers"** → Also appearing in AI Overviews.
          - **Actionable Idea:** Add a self-spend CTA to this page to capture individual learning budgets.
  - **Traffic Discrepancy:**
      - **GA4:** Shows artificially low traffic due to a cookie bot blocking tags before consent.
      - **GSC:** Shows \>400 organic visitors, a high volume for a new content push (typically \~200).
          - **Significance:** GSC is a reliable source, as it's a direct report from Google and unaffected by on-site tracking issues.
      - **Resolution:** Paola has configured the cookie bot to fire only in the EU. GrowthX will monitor for an immediate traffic recovery.

### Website Optimization

  - **Pricing Page:** A feature grid will be added below the tiers to show exact inclusions (e.g., AI credits, Tally minutes).
  - **"Talaera Professional" Page:** A new page will be created to define this tier's value proposition and recommended usage (e.g., "3x/week, 5 mins/day with Tally").
  - **1-on-1 Coaching:** Will be positioned as an add-on or on a separate page.

### Content Workflow Automation

  - **Problem:** Manually copying content from Google Docs to WordPress is inefficient.
  - **Solution:** GrowthX will use a WordPress API key to automate content staging.
      - **Process:** An editor pastes final content into a workflow → clicks a button → content is staged in WordPress.
      - **Security:** The API key will be limited to content staging, not admin access. GrowthX will research if access can be further restricted to only the blog section.

---

## Action Items

**Talaera Team**
- Add recent webinar to Notion webinar doc

**Anita Anthonj (Talaera)**
- Message Kayla, Anne, Tiffany regarding webinar opportunities

**Aida Knezevic (GrowthX)**
- Send SERP screenshots of AI Overviews for "Business English for Engineers" and "corporate language training" to Talaera team
- Email Kyle (GrowthX director) re: GTM/GA4 tracking configuration; review tags if Cookiebot fix insufficient
- Notify GrowthX team re: Cookiebot geo-targeting configuration change (EU-only)
- Email Paola WordPress API key implementation write-up; confirm blog-only scope and set up content staging automation
- Identify and propose B2B traffic opportunities to Talaera (in addition to current B2C momentum)
- Send Slack follow-up to Talaera regarding meeting outcomes and next steps

---

## Transcript

**Anita Anthonj:** This meeting is being recorded.

**Paola Pascual:** Hi, Anita.

**Paola Pascual:** How are you?

**Anita Anthonj:** Oh, I got the nicest message from my dad.

**Paola Pascual:** I translated it and sent it to you.

**Paola Pascual:** It's so sweet.

**Anita Anthonj:** So sweet, right?

**Paola Pascual:** That's what I thought.

**Paola Pascual:** I saw his name.

**Anita Anthonj:** I saw his name like an hour before the webinar and then it was so sweet.

**Paola Pascual:** How did it go?

**Paola Pascual:** I think it went great.

**Paola Pascual:** Yeah, they loved it.

**Paola Pascual:** I did the Tally demo as well and everyone was like, "Oh, that's good."

**Paola Pascual:** People had questions like, "Do I need a paid account to get in?" and I'll send the follow-up email very soon.

**Anita Anthonj:** I think it went well.

**Anita Anthonj:** That's awesome.

**Anita Anthonj:** It's such a great topic.

**Anita Anthonj:** I think it's nice when I, you know, in demos, I usually show the webinars we have.

**Paola Pascual:** It's a really great topic, and I'm so happy it went so well.

**Paola Pascual:** Great.

**Paola Pascual:** Yeah, I'm thinking about recycling it.

**Paola Pascual:** You know how we've been recycling the other ones?

**Anita Anthonj:** Maybe we can set it up for like in three months or something like that.

**Anita Anthonj:** Yeah, yeah.

**Anita Anthonj:** I think if you have three or four that work, let's just keep going through them.

**Anita Anthonj:** Hey Mel, we just had a webinar.

**Anita Anthonj:** Paola just killed it on the webinar.

**Mel MacMahon:** As always, very nice.

**Anita Anthonj:** My dad sent a note and he said, "I wish I'd had this in 1982."

**Mel MacMahon:** Wow.

**Anita Anthonj:** Yeah.

**Mel MacMahon:** That's very cool.

**Anita Anthonj:** Yeah.

**Paola Pascual:** He's very sweet.

**Anita Anthonj:** Yeah, yeah.

**Anita Anthonj:** No, it's awesome.

**Anita Anthonj:** It's great.

**Anita Anthonj:** It's such a good topic.

**Anita Anthonj:** I feel like we're really honing in on good topics all around.

**Paola Pascual:** Yeah, I think it touches a lot.

**Paola Pascual:** But like, we had this person, she said—because I kept saying I'm trying to be more mindful that this is for non-native English speakers—like, we help with business English, you know.

**Paola Pascual:** And this person said, "Well, I'm a native speaker. I'm from the United States."

**Paola Pascual:** But I feel like some of these things help me too.

**Paola Pascual:** Like, I'm not very confident and I don't know how to jump in.

**Anita Anthonj:** And that's even better then, right?

**Anita Anthonj:** I feel like if native speakers can resonate with it, awesome.

**Paola Pascual:** Yeah.

**Paola Pascual:** That's cool.

**Paola Pascual:** So I should add it to the Notion doc, right?

**Anita Anthonj:** To the webinar Notion doc?

**Anita Anthonj:** Yeah, of course.

**Anita Anthonj:** Yeah.

**Anita Anthonj:** Yeah, great.

**Anita Anthonj:** But yeah, that one just occurred to me.

**Anita Anthonj:** As you said, regarding webinars, I need to message Kayla, Anne, and Tiffany.

**Paola Pascual:** Well, I was just going to quickly ask Mel about the pricing thing. Is that what you were asking about?

**Mel MacMahon:** Yeah, I remember we had a conversation last week about having the feature grid below the tiers, so you know exactly what you get in there.

**Mel MacMahon:** And then that's where we would call out that you only get X number of AI credits or enough for X number of minutes with Tally or whatever.

**Mel MacMahon:** And then having a separate page that talks about a "Talaera Professional" page.

**Mel MacMahon:** I think I was talking to Anita about this.

**Mel MacMahon:** So instead of us sending over all the links to the different components, there should be a page like "here's the Talaera Professional tier" and "here's exactly how it's used" or how we best recommend it.

**Mel MacMahon:** That's where it would say like three times a week, five minutes a day with Tally plus once or twice a week conversation club.

**Mel MacMahon:** And then either the one-on-one coaching as an add-on to that page or a separate page that's basically a duplicate plus, but leans more into the one-on-one coaching side.

**Paola Pascual:** Yeah, I like that.

**Paola Pascual:** We have the grid on the pricing page.

**Paola Pascual:** I don't have those pages just yet, but I hope to have them.

**Mel MacMahon:** Oh, the grid is there.

**Mel MacMahon:** That's awesome.

**Mel MacMahon:** Maybe I just didn't refresh.

**Paola Pascual:** Yes, the grid's there.

**Aida Knezevic:** Hey, everyone.

**Aida Knezevic:** I'm sorry to keep you waiting.

**Anita Anthonj:** How are you?

**Paola Pascual:** How are you?

**Aida Knezevic:** I am good, good.

**Aida Knezevic:** Friggin' system updates.

**Aida Knezevic:** I don't get why they make us do them, but can we please schedule them when I'm not working?

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, thank you for waiting.

**Aida Knezevic:** I have some updates on performance and keyword rankings that are really exciting.

**Aida Knezevic:** But I wanted to get started by asking you for your feedback on how you think we've done so far.

**Aida Knezevic:** Anything that you would like us to do moving forward or any feedback at all?

**Aida Knezevic:** Mel, I know you were in CheckThat today.

**Aida Knezevic:** If anything comes up over there, I'm open to any feedback.

**Anita Anthonj:** Mel, do you want to share?

**Mel MacMahon:** I haven't had a chance to really drill in on it yet.

**Mel MacMahon:** I did get access and it looks like it's working.

**Mel MacMahon:** It looks like a pretty cool tool.

**Mel MacMahon:** I've been slowly catching up on it.

**Mel MacMahon:** So I'll let you know as I see things.

**Anita Anthonj:** Cool.

**Anita Anthonj:** I think the content so far has been great.

**Anita Anthonj:** Really, really good.

**Anita Anthonj:** Paola, nothing from you, right?

**Paola Pascual:** No, it's been really, really great.

**Paola Pascual:** All the content has been really, really great.

**Paola Pascual:** And other than the initial comments we had, everything after that has been implemented super quickly and super effectively.

**Paola Pascual:** Everything has been quick, delivered on time, and the feedback has been super fast to implement.

**Anita Anthonj:** And with the suggestions from Hassan on how to improve the UX and UI, it's really great.

**Aida Knezevic:** Great, great.

**Aida Knezevic:** We're happy to hear that.

**Aida Knezevic:** Sometimes we get feedback from clients like, "Why do you do it like this?" or "Why do you have a separate sprint team and a separate long-term team?"

**Aida Knezevic:** It's because we've become very good at the first couple of weeks—getting you up to speed and setting you up in our system.

**Aida Knezevic:** A few weeks ago, I set up a position tracking report in SEMrush that monitors your rankings for the target keywords we're targeting with our content.

**Aida Knezevic:** I checked it out today to see how we're progressing.

**Aida Knezevic:** And I was really excited to see that we have page one rankings for a lot of really important commercial keywords.

**Aida Knezevic:** This one I was really excited about: "best corporate language training platforms for global teams."

**Aida Knezevic:** You're appearing in the AI Overviews.

**Anita Anthonj:** And last week you were in position 26.

**Anita Anthonj:** That's page three.

**Anita Anthonj:** Do you see this?

**Mel MacMahon:** Wow.

**Mel MacMahon:** Aida, do you have any thoughts on what drives that?

**Mel MacMahon:** It seems like a rather large shift.

**Mel MacMahon:** Is that really just due to 19 blog articles?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** These are the keywords we're targeting and all the content we've published so far.

**Aida Knezevic:** Each of these keywords has a corresponding article optimized for that specific keyword.

**Aida Knezevic:** When we write content, we do in-depth research that takes into account all the information your audience would need for that topic.

**Aida Knezevic:** And then we incorporate it into the article.

**Aida Knezevic:** The content is comprehensive and optimized for a specific keyword.

**Aida Knezevic:** It's also optimized for AI chunking, which supports AI Overviews.

**Aida Knezevic:** The one thing to know is that as time goes on, content gets old.

**Aida Knezevic:** So in three to six months, we'll need to check the performance and see if there's anything that needs updating.

**Mel MacMahon:** Okay.

**Paola Pascual:** Interesting.

**Aida Knezevic:** Okay.

**Paola Pascual:** For example, with the first one—it's incredible.

**Anita Anthonj:** That jump is amazing.

**Paola Pascual:** I'm very curious: is the competition high for that one?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** The keyword difficulty is 50.

**Anita Anthonj:** That's really actually pretty difficult.

**Anita Anthonj:** That's crazy.

**Paola Pascual:** Oh, wow.

**Paola Pascual:** Yeah, that's insane.

**Aida Knezevic:** That's good.

**Aida Knezevic:** But you can rank for it because your entire website talks about this.

**Aida Knezevic:** Your homepage, everything about you as a company—you talk to corporate organizations, a corporate audience.

**Aida Knezevic:** The search algorithm associates you with those topics.

**Anita Anthonj:** Amazing.

**Paola Pascual:** Amazing.

**Paola Pascual:** Awesome.

**Mel MacMahon:** So the keyword is associated with the domain?

**Mel MacMahon:** Not just particular pages or blogs?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Let me actually share this with you.

**Aida Knezevic:** It's targeted by a specific page.

**Aida Knezevic:** For example, for this keyword, we have a corresponding blog post.

**Aida Knezevic:** Let me go to your content calendar.

**Aida Knezevic:** Actually, I think your homepage is ranking for this keyword.

**Anita Anthonj:** Oh, wow.

**Aida Knezevic:** Yeah.

**Anita Anthonj:** That's awesome.

**Aida Knezevic:** The majority of these keywords that you're ranking for—we have content about them.

**Aida Knezevic:** Does that make sense?

**Mel MacMahon:** It does, yeah.

**Mel MacMahon:** I'm trying to figure out what drives the rank.

**Mel MacMahon:** It sounds like you said our homepage is ranking for that keyword, which means the blogs that incorporate that keyword are also helping to drive the homepage, but the homepage incorporates that keyword more.

**Mel MacMahon:** Is that kind of it?

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** To your question about what drives rankings—that's a whole industry.

**Aida Knezevic:** There's a lot we know from Google, because Google was recently subpoenaed to provide information about what drives their rankings.

**Aida Knezevic:** There are two main things: you have to be an authority on the topic, and the content has to be popular—meaning people stick around, read the content, and engage.

**Aida Knezevic:** That also impacts rankings.

**Aida Knezevic:** Typically when we create content, these are the keywords we rank for.

**Aida Knezevic:** For example, we have an article about Preply alternatives that's been published on your blog.

**Aida Knezevic:** That's the one ranking for this keyword.

**Mel MacMahon:** Okay, cool.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then we also have another one that I thought was really interesting.

**Aida Knezevic:** "Business English for Engineers."

**Aida Knezevic:** That one's also showing up in AI Overviews.

**Anita Anthonj:** That's amazing.

**Aida Knezevic:** Yeah, that was.

**Paola Pascual:** Oh, sorry.

**Anita Anthonj:** Go ahead, Paola.

**Paola Pascual:** I was just curious if that was the blog or the landing page.

**Aida Knezevic:** Let me check the SERP later and take a screenshot because it looks different depending on where you are.

**Aida Knezevic:** But either way, the fact that we have a blog post and a landing page is really helpful for SEO.

**Anita Anthonj:** Super quick side note, Paola and Mel. Mel, I wonder if that "English for Engineers" page would be a really good place for that self-spend CTA you mentioned.

**Anita Anthonj:** A lot of these companies give learning budgets.

**Mel MacMahon:** You mean add the CTA directly into the blog?

**Anita Anthonj:** Yeah, yeah. That self-signup page you built for advertising?

**Mel MacMahon:** Yeah, like Paola, you could probably do that right now if you wanted to.

**Anita Anthonj:** I think that would be awesome because so many of these companies do that anyway.

**Mel MacMahon:** Yeah.

**Anita Anthonj:** Sorry, Aida, side note.

**Aida Knezevic:** No, don't worry about it.

**Aida Knezevic:** Great.

**Aida Knezevic:** So those are all the metrics I have.

**Aida Knezevic:** Overall, in Google Search Console, the traffic we measured two days ago was over 400 visitors from Google Search.

**Aida Knezevic:** That's really great.

**Aida Knezevic:** I can't remember the last time I saw such traffic growth from content we've published.

**Aida Knezevic:** For other clients, it's usually around 200.

**Aida Knezevic:** Part of it comes down to your industry—you have a wide variety of keywords to target.

**Aida Knezevic:** Some of the content we've published targets high-volume searches like "English for emails" or "how to talk in a meeting."

**Aida Knezevic:** Those are high-volume keywords.

**Aida Knezevic:** It's really positive traffic growth.

**Aida Knezevic:** And because we have access to your GTM now, I'm going to reach out to Kyle, our director, to see what we can do there.

**Aida Knezevic:** If we verify the precise issue and can fix it in Google Tag Manager, that would be good.

**Aida Knezevic:** In any case, you can also check your Cookiebot setup to make sure it's not firing everywhere.

**Paola Pascual:** That would also be really helpful.

**Paola Pascual:** Yeah, I changed that too.

**Paola Pascual:** So it's only for the EU now.

**Aida Knezevic:** Okay, great, great.

**Aida Knezevic:** If that's changed, we should see a difference pretty immediately.

**Aida Knezevic:** When did you do that?

**Paola Pascual:** Earlier today.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** In that case, I'll let the team know.

**Aida Knezevic:** Yeah, the results should be pretty immediate.

**Aida Knezevic:** I have a personal website and I remember implementing a cookie plugin and my traffic tanked.

**Aida Knezevic:** I don't have anything in my Google Analytics now—it's practically useless.

**Aida Knezevic:** So yeah, I think that should help.

**Aida Knezevic:** But if not, we can check the tag setup.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** All right.

**Aida Knezevic:** Another thing we can do is automate publishing with an API key.

**Aida Knezevic:** Instead of manually copying and pasting content, we would connect to WordPress using an API key.

**Aida Knezevic:** After you're done reviewing content, the editor copies the final version from Google Docs, pastes it into a workflow, clicks a button, and it's staged in WordPress.

**Aida Knezevic:** It's not published automatically, but it saves time—and it adds up if you're publishing five pieces.

**Aida Knezevic:** So if you're open to that, we would just need your WordPress API key and we can set up the automation.

**Paola Pascual:** Is there anything we need to know in terms of that?

**Paola Pascual:** Like, any downside to it?

**Aida Knezevic:** Yeah, I can send you a write-up from our IT team.

**Aida Knezevic:** Essentially, we don't have admin access to your WordPress.

**Aida Knezevic:** We'd just be pushing content into the blog.

**Aida Knezevic:** And I think it might be possible to limit access to just the blog section.

**Aida Knezevic:** I'll ask the team if that's something that can be done for WordPress.

**Mel MacMahon:** That's good.

**Paola Pascual:** What's that?

**Mel MacMahon:** Sorry, Paola.

**Mel MacMahon:** How are you doing this right now?

**Mel MacMahon:** Are you doing it manually?

**Aida Knezevic:** With the GrowthX team, yeah.

**Mel MacMahon:** So you have access to put stuff into our blog via WordPress?

**Mel MacMahon:** You just don't have admin access, is that right?

**Aida Knezevic:** We don't have admin access, but we have regular access to your WordPress.

**Aida Knezevic:** In this case, we'd just be setting up an automation.

**Mel MacMahon:** And that would automate all the formatting, insertion of CTAs, images, things like that?

**Aida Knezevic:** Okay.

**Aida Knezevic:** The only issues that can come up—but I don't think WordPress has this issue—are with tables.

**Aida Knezevic:** WordPress allows you to copy and paste tables as they are.

**Aida Knezevic:** With CMS platforms like Webflow and Sanity, tables are an issue and we have to do manual workarounds.

**Aida Knezevic:** But WordPress should be totally fine.

**Paola Pascual:** Awesome.

**Paola Pascual:** Great.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** Anything else?

**Aida Knezevic:** I think those are all my updates.

**Anita Anthonj:** Paola, anything from you guys?

**Paola Pascual:** No.

**Paola Pascual:** Do we have more blog posts for this week?

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** Hassan is going to send them over tomorrow or Friday.

**Paola Pascual:** It's been very exciting to see the blog grow.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** It's really, really, really good.

**Aida Knezevic:** It's really exciting, yeah.

**Mel MacMahon:** You mentioned pretty impressive click counts or something like that—like 400 as opposed to 200.

**Mel MacMahon:** What's the relationship between that and the stuff impacted by our Cookiebot?

**Aida Knezevic:** Great question.

**Aida Knezevic:** The Cookiebot traffic comes from GA4, Google Analytics—that's the traffic impacted by the Cookiebot.

**Aida Knezevic:** Google Search Console is a Google service that measures visitors who click on your website from Google Search.

**Aida Knezevic:** It's just Google Search users and it's not measured through a tag on your website.

**Aida Knezevic:** It's data from Google that they share with you as the webmaster.

**Aida Knezevic:** It's from a different data source.

**Aida Knezevic:** You don't need a tag on your website to track visits using Google Search Console because it's data Google shares with you as a website owner.

**Mel MacMahon:** Okay, so it's measuring something before the user even lands on the website and has to accept or decline the cookie box?

**Aida Knezevic:** Exactly.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** They can see when someone clicked on your website, but they can't see engagement rates.

**Aida Knezevic:** They can't see what the user did after that.

**Aida Knezevic:** You need Google Analytics for that.

**Aida Knezevic:** GSC is helpful to understand where you rank on average, what keywords you rank for in Google, average click-through rates, and how many clicks you get from Google.

**Mel MacMahon:** Okay.

**Mel MacMahon:** So, Paola, in that case, it's possible that Amplify is also impacted by this Cookiebot?

**Paola Pascual:** Okay.

**Paola Pascual:** Yeah, I pinged Victor about this.

**Paola Pascual:** I got a report from Cookiebot saying we're not compliant in some way because there's stuff firing or getting data before the cookie consent.

**Paola Pascual:** If there's any other area where you feel like there's a big opportunity and it doesn't have to be just for B2C—we've been getting a lot more B2C traffic.

**Paola Pascual:** I haven't seen that much from the B2B side.

**Paola Pascual:** If you feel like there's something that would support more B2B traffic or support a specific keyword, let us know.

**Paola Pascual:** That's something we can get done fairly quickly.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I'll think about it and let you know.

**Paola Pascual:** Awesome.

**Paola Pascual:** Thank you.

**Aida Knezevic:** All right.

**Aida Knezevic:** Thank you all.

**Aida Knezevic:** I'll send a follow-up in Slack in a little while.

**Aida Knezevic:** Thank you.

**Mel MacMahon:** Great.

**Paola Pascual:** Thanks.

**Aida Knezevic:** Bye.
