# SchoolAI <> GrowthX Weekly Sync

<metadata>
date: 2025-05-15
time: 20:00 UTC
duration: 38 minutes
organizer: jenn@growthxlabs.com
participants: Jenn Peters, Dave Capone, Nikki Muncey, Colton Taylor, Kyle Gaudreau, Daniel Lopes
fathom_recording_id: 62951346
fathom_url: https://fathom.video/calls/301135411
share_url: https://fathom.video/share/n-EUByzm6NuLwg8cgz2dKeio8skzK_u6
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

GrowthX and SchoolAI reviewed content performance and seasonal strategy, discovering a 25k-impression spike in overall traffic but needing to account for educational seasonality. The team identified the critical need to shift summer content toward administrators and purchasing influencers (key buying season runs May-September), while also developing philosophical content around ethical AI in education. Dave proposed a cleaner SEO reporting approach to track ranking movements more precisely, and the team tackled technical SEO issues with robots.txt and sitemap cleanup in Framer.

---

## Context

SchoolAI is an AI education platform serving schools and educators. GrowthX provides content marketing services for SchoolAI. This weekly sync brings together the SchoolAI marketing and operations team (Nikki, representing their strategic direction) with GrowthX's content and SEO specialists (Jenn handling content strategy and production, Dave managing SEO performance) to align on content topics, performance analysis, and technical implementation. The partnership is in active content creation mode, with multiple pieces staged in Framer weekly and a new educator contractor (Graham) now reviewing articles for pedagogical accuracy and reducing AI overclaiming.

---

## Relevance

**To GrowthX Delivery:**
- Validated the importance of educating clients on seasonality in niche verticals; SchoolAI's teacher-focused content peaks during school year, admin/purchasing content during summer buying season (May-September)
- Graham (external educator contractor) is an effective quality gate, catching AI workflow overclaiming and hyperbolic language — model for other content-heavy clients
- Framer's limitations on custom robots.txt and sitemap control requires external intervention and testing by GrowthX

**To CheckThat:**
- SchoolAI planning major push on ethical AI in education content—aligns with broader AI education trend following federal executive orders; opportunity to audit SchoolAI's AI visibility as they expand philosophy/policy coverage
- Dashboard accuracy concerns flagged; new reporting structure for SchoolAI tracks top-3, 4-10, and 11-20 ranking buckets separately to isolate real ranking movement from volume-driven noise

**To GrowthX Business Development:**
- Account health strong: 25k impressions and 954 clicks in one week; site broadly performing well despite GrowthX blog content showing variance
- SchoolAI leadership (Nikki) actively engaged on strategy and willing to invest in solving problems "right" rather than band-aid fixes (e.g., custom sitemap solutions)
- Expansion opportunity: SchoolAI has student and parent products in pipeline; currently targeting teachers and admins only

---

## Overview

- Site performance improving overall; GrowthX content metrics need investigation
- Seasonality in educational content crucial; summer focus on admin/purchasing content
- Need to address philosophical/ethical AI in education topics
- Technical issues with robots.txt and sitemap need resolution

---

## Key Topics

### Content Performance and Strategy

- Overall site impressions/clicks up 25k/954 respectively
- GrowthX blog content down, but dashboard accuracy in question
- Seasonality impacts educational content performance
  - School year cycle affects teacher-focused content
  - Summer: focus on admin/purchasing content (buying season runs May-September)
  - Teachers less engaged during summer break; admins and purchasing committees most active during buying season
- New content ideas:
  - Ethical AI in education and school safety
  - Administrator-focused AI implementation guidance
  - Summer learning with AI tools for students
  - AI literacy curriculum for educators

### SEO Metrics and Reporting

- Average position metric can be misleading; new report in development
- Clicks/impressions increasing despite position changes
- Need to account for educational seasonality in metrics
- New reporting will break rankings into top-3, 4-10, and 11-20 buckets to isolate real ranking movement from volume effects

### Technical SEO Issues

- robots.txt file needs updating to properly handle spaces pages (currently allows all spaces, need to add "disallow /spaces" at bottom after allow list)
- Sitemap requires cleanup to remove non-indexable pages; Framer-generated sitemaps include app.pages which are not managed by product team
- Framer limitations causing difficulties in implementing custom robots.txt and programmatic sitemap updates

### Content Review Process

- New educator (Graham) providing valuable feedback on AI content
- Catching hyperbolic language and AI overclaiming; AI workflows often overstate capabilities ("we can do it all automatically" when human direction still required)
- SchoolAI planning to focus on ethical AI in education content, especially given executive order trends

---

## Action Items

**Jenn Peters (GrowthX)**
- Collaborate with Dave on admin/influencer targeting strategy for summer buying season (May-September)

**Nikki Muncey (SchoolAI)**
- Send internal docs on SchoolAI's ethical AI stance to GrowthX team
- Provide Basecamp pro access to Dave Capone and Jenn Peters (contains 2+ hours of AI literacy training content)
- Add "disallow /spaces" to robots.txt file (after allowing specific space pages)

**Dave Capone (GrowthX)**
- Investigate Framer sitemap generation and custom robots.txt implementation
- Test robots.txt changes on spaces pages to verify no-index enforcement
- Explore options for optimizing crawl budget; consider external sitemap generation if Framer limitations prevent proper control

---

## Transcript

**Dave Capone:** We're going to, let me start over.

**Dave Capone:** We weren't able to meet up because I had the contractor come late.

**Jenn Peters:** So we're going to put it into this meeting. Yeah, so we'll just talk about it this morning. That should be fine. That's great because I don't have much to cover so I'm happy to hear about all that. That's awesome. Pretty much like going smoothly otherwise. So yeah, sweet.

**Jenn Peters:** So you saw an increase in performance. Yeah, like site overall, but GrowthX not. But then also I'm now suspicious of Tracker not being fully working properly.

**Jenn Peters:** So yeah. Hey Nikki.

**Dave Capone:** Hey Nikki.

**Nikki Muncey:** We're all here together.

**Jenn Peters:** I thought it was just going to be me hanging out with two note takers and then Dave popped on and I was so excited. The note takers are, they get a bit crazy when you get in meetings like 20 plus people or 50 plus people.

**Nikki Muncey:** So our CEO actually is always complaining because we use Ask Elephant as our note taker. And so we get on a company meeting and we get like 50 of them. And shouldn't you be smart enough to know that we are the same female name that's long time.

**Jenn Peters:** Yeah. Who won? Share the recording. Like we have the same. We have a couple of different tools that run. And yeah, it's always a matter of just like, okay, I'm not letting in anymore. I'm not going to do it anymore because that's enough. It's getting crazy.

**Jenn Peters:** Yeah. Separate section for note takers. Yeah. Just put them somewhere else. They definitely don't need, you know, 50 or whatever. But yeah, it's good when you're just like the only person sitting there like waiting on a meeting and then it's just like only note takers.

**Jenn Peters:** How's it going? Good. So busy.

**Jenn Peters:** Are you finding that things are a little bit easier content-wise with Graham on the team now?

**Nikki Muncey:** Yeah, has that helped a little bit?

**Jenn Peters:** That's good. Totally. Oh, amazing.

**Jenn Peters:** Just for context, Dave, I think I did mention to you, but SchoolAI brought on a contractor teacher, an actual educator that's reviewing our articles now and giving some great feedback as well. So yeah, he's been chatting with me, and he DMs me, DMs Deya, and we talk about articles and all that kind of stuff.

**Jenn Peters:** So yeah, he just has been catching things on workflows that the workflow does that's kind of just repetitive things that it likes to do, I guess a little bit hyperbolic at some times and needs to kind of be reined in a little bit with its promises of what AI can do and all that kind of stuff.

**Jenn Peters:** But yesterday, he was like, I think the workflow is confused about, like, what actually can be done. Yeah, he literally messaged me and said the same thing. He was like, I think it's confused. And it's like basically saying that like everything can be done automatically and it's like, no, you still need to tell it what to do and that kind of stuff.

**Jenn Peters:** And I was like, okay, yeah, that's valid. And then today he had like another point that was kind of similar, like something it said about just something hyperbolic, like it could just like do everything for you or like, you know, it just, it does it all. And, you know, it's just like, no, okay, we have to kind of like rein that in a little bit and it, you know, it still needs, it doesn't do that thing that it's telling it to do or it's not doing it automatically.

**Jenn Peters:** That's something that's quite common across accounts that we're seeing is just that it'll kind of over promise or over sell. It's like, it's talking about itself, you know, the workflow when it's doing, when it's making an article with AI. So it's built, it's bringing itself up.

**Jenn Peters:** Self-biased?

**Jenn Peters:** Yeah, self-biased. It's like, we can do it all, right? We do it automatically. And it's like, shut up.

**Jenn Peters:** But yeah, awesome. I'll keep my little update quick. I know that you and Dave didn't get a chance to meet before, so I'll give the floor to Dave to talk about. But, yeah, as per usual, the next batch of content is being staged in Framer, as usual by Deya. Everything's going well there. Deya's having a bit more of a smooth week so far. Yeah, with everything in her region and everything. So everything's going well there.

**Jenn Peters:** I've been reviewing all the articles and, like I said, talking to Graham as well. I've been doing, like, other things across the articles just kind of with tone of voice and things like that and just kind of seeing where we can improve, like, the H2s and overall. Like, given the kind of, like, tone we want to have with articles and the authority of the voice and everything, I still think there's ways that we can, like, tweak content, tweak headers to make them more speak to the reader and be a bit more engaging and still fun within the, like, parameters of being, like, high-level content.

**Jenn Peters:** That just means, so your average position is like where you, like down in number, because that means, yes, so up means down. Down in number is like, yes, that's what you're trying to say.

**Jenn Peters:** Yeah, I hear you. Yeah, it's like where you're appearing on the search when somebody's typing in something like where you are, where basically like SchoolAI is coming up. I don't have that one open right now, but Dave, can you see that one as like in terms of average position, like where SchoolAI is coming up?

**Dave Capone:** And I couldn't see like, so on the left axis, is that the average position?

**Jenn Peters:** And then, um, yeah, I would have to open up the original actual, um, I think it's cut it off there on the side. Um, I'm trying to see what color. Yeah, it's the light green.

**Dave Capone:** Okay. In that case, yeah, then that would mean it's falling.

**Nikki Muncey:** Um, it just looks like spiked significantly, which is that because we added so much content. So there's two reasons for that, right?

**Dave Capone:** So when you're adding content, you're going to get an increase in visibility. When you have an increase in visibility, you're not going to be ranking on the first page, so that'll knock your average position down. Typically, the way that you can clean this up to where it isn't distracting is that you can limit your view or average position view to only my top 20 or top 10 rankings, which then should get you back to where you can track your ones and threes. So I'm actually working on another report that'll do that.

**Dave Capone:** So that report will actually show us like average position of our top number of top threes that you have per day, and then we'll track that over time so that we can say, okay, we gained more top threes, we gained more four through tens, or we lost four through tens, and then you can tell where it went. So you can say, okay, we lost some four through tens, but then we got them in one through three, or we lost some four through tens, and now it goes through 11 through 20.

**Dave Capone:** And you can basically tell where your rankings are going, and then we can investigate and see what pages are impacted by that. So we'll clean this up and we'll have another report, which will be a little bit more actionable after this. Okay, great.

**Nikki Muncey:** Yeah, I'd love to see that because I think I'd just love to be able to speak internally, right? Like when I get questions, understand what I'm looking at. So yeah, just a more in-depth reporting, I think is going to be really helpful.

**Jenn Peters:** And Dave, I was just chatting about that earlier is that there could be like a few areas on the current dashboard where it's not being fully accurate at the moment in terms of like the GrowthX content. Just like, for example, and I'll this to this later in the report, but you know, like it's not necessarily updating properly or something because like looking at a piece over time and seeing like where it's. And that kind of thing, like we should be able to get more results on that pretty soon. But yeah, I saw an example of the new dashboard with another account. It looks awesome. It's got so much different things it can track on there.

**Nikki Muncey:** Inundate me in data.

**Jenn Peters:** I'd rather have more than less. Awesome. Data we have.

**Dave Capone:** So average position has gone up. So we went from, in January, were at, like, can I share real quick?

**Jenn Peters:** Yeah, please do. All right. Take over.

**Dave Capone:** There it is. Okay. Let me know when you can see the page. Yep. Yep. Okay. So in January, were around, what, 16.9, and then middle of the year so far, it's dropped to seven, then it's kind of gone up. But what you like to see is a spike here of impressions and clicks, even though our average position goes up, that's because showing up in more places, right?

**Dave Capone:** So as your impressions increase, that's going to be a sign of increased visibility. And because you're showing up in so many other places and Google was trying your content out in a lot of different places, that's going to impact your average position. So even though it's reporting like a 27, I will still say that because you have your clicks have been maintaining and your impressions have increased, that overall health is good. We'll know more once we break this down by average, like by position type. So like one to three, four to 10, et cetera. So overall healthy though. So like, yeah, this is something you want to see.

**Jenn Peters:** What I really like to see is just that like, despite that, despite that going up, that our clicks and impressions are going up. So it's like, people are still finding it. People are still seeing it. And it's like, yeah, we're just, we're like that little spike. What is that? Like April 10th, just on clicks and impressions. It's really nice to see. So yeah.

**Dave Capone:** Nikki, one thing that'll help us is if you can kind of. This is a rough, like a proximization of what your seasonal traffic looks like. So we can account for that too, right?

**Jenn Peters:** I have that in my report today actually too, to like talk about as like something we need to look at strategically. Mentioned it, Dave, the other day because, yeah, so basically we have like a huge jump in impressions and clicks over the past week on the site overall, like 25k impressions, 954 clicks, you can see on the dashboard here, it's looking pretty sweet. The GrowthX blog content is down over the previous week. However, after I started digging into it, I started thinking that maybe the dashboard is not fully marketing properly as we just talked about. So we'll look into that.

**Jenn Peters:** And yeah, so as I mentioned here, we need to start thinking about like the seasonality of certain aspects of educational content. And like in terms of like the school year and other things that might be impacting it, how do we measure that? That's something that's going to be interesting. We could try to figure out, but for example, looking at this article I've linked here and looking at the downturn in clicks this past week on it, assuming that the data that we have is correct on it, the top writing piece over the course of however long has been this AI homework, health and tools guide. It peaked around April. It did like a lot of traffic around mid April to like end of April. And then by May, it's kind of like fizzling out a little bit.

**Jenn Peters:** So like my question is like, is this related to the topic and the school year and like where we could be positioned like in the school year and teachers looking for this kind of information? I don't think it's too much. And like I say, Dave was the one that brought this up. He'd be like, I don't think it's odd for us to like look into this or like too much or, you know, because I think that it's going to affect some topics over others. But yeah, Dave, you wanted to add to that?

**Dave Capone:** I guess from a sample size of one, have to always remember that. But I will say that, like, you know, if it's a holiday and most kids aren't in school, so they're not doing the searches that they need to to go to utilize or to use your site. So I think like to visit your site. So I think that's one. And teachers aren't in school either. So thinking through the different holiday seasons, we can then formulate like a, OK, this holiday is coming up. So we're expecting a dip in traffic. That way we can account for that and say, even though a dip last year, you know, where can we find growth during those times to help keep things at a decent run rate?

**Dave Capone:** And then two is like during the summer season when, you know, educators aren't in school or I mean, yeah, when educators are in school and kids are like summer break, like how much of an impact is that on business so that we can account for that and we can start thinking through that. So it's actually pretty interesting.

**Nikki Muncey:** And just to speak to that a little bit, you're dead on. Like, okay. So from a student perspective, right now, we don't have our student product yet. Like, we don't want students to be targeting students ever. Or parents yet. Yet. From a teacher perspective, though, content that resonates really well with teachers is going to do well when school is in session, right? Because teachers are in school, thinking about school. They are going to do, we actually were talking about this with email today in terms of, like, what do you send to teachers? Are they going to be paying attention to stuff? Teachers aren't going to be looking at this type of stuff typically over the summer.

**Nikki Muncey:** That said, we do have, like, ISTE is a big conference that we're going to. That's at the end of June. Like, end of June, beginning of July. That's a big teacher thing, right? So they're going to be thinking about that. We did do, like, space camp type situation. I don't remember exactly what it was, but it was like training for teachers that was free over the summer last year. That was really big. So there are ways that we can engage teachers, but they are going to be doing less like searching for this type of stuff.

**Nikki Muncey:** At the same time, buying season for schools is like right now to September. So when they purchase it, it's during the summer. And so your admins and content that like is going to be relevant to admins is going to be something that we probably want to focus in on because that kind stuff will still resonate because this is when we do, like this will be when we do most of our revenue is this text, which is why we do it for three months.

**Jenn Peters:** Administrators, administrator focused, like what, you know, AI tools kind of the ministers use to, you know, boost classroom engage or whatever. Yeah, that's really interesting. Or like how to help your teachers use AI, you know what I mean? Like it can...

**Nikki Muncey:** It will be about using AI in the classroom, but how do we do it from that administrator lens? Because they're the ones who are thinking about school. There's so many interesting topics we can do around that, like seasonally.

**Jenn Peters:** I'm just like, you just really got me thinking, like brainstorming-wise, like how can we set up kids for over the summer break with AI tools to help them? Like once we have a student product to talk about, you know, how can we keep them occupied? You know, how to keep your students engaged and occupied so you don't forget their stuff over the summer holidays? How can we, you know, prepare for the breaks and that kind of stuff? Or like seasonal holidays and that kind of stuff. Like there's so many different things that we can do. But I think seasonality is really going to come into play for a lot of these different topics.

**Dave Capone:** Yeah, Jenn, let's think through if now is the buying season, now it's up until, you know, summer vacations. It's over like, say, September. Um... So let's think through what the ICP is, because it's to be completely different, right? So I think it's going to be someone who is looking to purchase software for their school or purchase software for their classroom. It is still maybe a teacher, but it might be someone who's looking to...

**Jenn Peters:** Administrators, like Nikki, hey, like, so, you know, those in office with the money that control...

**Nikki Muncey:** Yeah, that's a really good point, is that there are, and this is where it starts to get so friggin' messy and, like, it's just insane. It's like you have your district level and your school level superintendents and administrators and the people who are actually, like, in those positions, and that's what their whole career has been. You also have teachers who are on AI purchasing committees who are at the district level or the school level, depending, and sometimes they're also teaching in the classroom. Sometimes that's their whole job. I have a friend who that's her whole job now. She is evaluating AI for Alpine School District, which is our local school district. And so sometimes you have positions like that that we need to be targeting. You also have your instructional and tech coaches who sometimes teach at the same time and sometimes are just doing that.

**Nikki Muncey:** So there's this whole spectrum of the people with the buying power, the people with very strong influence over the people with the buying power, and then our daily users. And I would say those with instructor and influence are like, those are the people we need to be thinking about in the summer. Yeah.

**Dave Capone:** Let's, let's, Jen and I will take this one offline and we'll think through some strategy.

**Jenn Peters:** Got a lot of ideas. I think it comes down to like, thinking about the queries, like what those people are actually searching for. It's not going to be necessarily like super ICP specific. Like we can do some broader topics that cover all those bases. We just have to think about the queries that they're using to search for these tools during this season that speak to what they're looking for.

**Nikki Muncey:** The other thing that is going to be really interesting right now, and I would love for us to, like, focus in on, is having and sharing we have, we need to share an opinion about how AI should be used in schools, especially with, like, the executive order. Like, the big, like, trend of that was sort of flash in the pan, but that is still a real thing. And that has, like, accelerated school leaders looking for AI solutions in their schools. Like, this is very much a hot topic right now in terms of, like, should AI be in schools? How can we put it in schools safely? Like, I think a lot of articles, yeah, yes, a lot of, and how do we protect it, right? Like, how do we make it something that doesn't just, like, cheat for students?

**Nikki Muncey:** We have done have been more focused on like the very tactical ways that we can use AI, right? Like I'm thinking about like formative assessments. We've done it for lots of different subjects. And all of that is great. I'm not saying that it's that it's not. But I think that we can, especially as we move into the summer, especially with the trends that are happening in the US right now, I think it would be good to start incorporating content around sort of the philosophical question of like, is this okay?

**Jenn Peters:** Yeah. And if it is okay, how? And then how do we do it right?

**Nikki Muncey:** So that it is a tool that helps students grow and learn rather than something that actually hinders them. Is helpful?

**Jenn Peters:** Yeah, that's perfect.

**Dave Capone:** If you have any internal documents that go over what AI stance is on ethical usage of AI in schools, that would be helpful that we can reference when we create these articles.

**Nikki Muncey:** Yeah, let me send you this right now. And then we have a blog post that went live with the executive order that I will also send you. And then we have a ton. I will get you guys pro access to Basecamp, which is our teacher training something. We have probably two hours at least worth of content in there about like AI literacy. How do you teach AI literacy to kids? Like, what does that all look like? So I can get you access to that so that you can see everything. All of those courses are linked at the bottom of the page that I just linked to.

**Jenn Peters:** The courses are linked on the link. They're linked on the link.

**Nikki Muncey:** And you actually should be able to access them all just like signing up, just creating an account. But if you just use your GrowthX emails, I will also make sure that you have. Yeah.

**Jenn Peters:** I will pass the floor on to Dave now and just kind of, you know, the rest of the stuff that we can cover here, we can look at async, it's just like more review and catch that stuff, but I want to make sure there's enough time for you to talk about your, everything robots.txt or whatever it was that you were going over.

**Dave Capone:** Nikki, if you could, I guess, share your screen and open up Framer, maybe we can figure out. Not Webflow, Framer, but I'm happy to show you.

**Nikki Muncey:** Okay. Let me turn my screen. My computer is like getting to that point where it's fighting me. And it probably doesn't help that I have Framer open. I think it's three different tabs right now. Okay. Can you see Framer? Yep.

**Dave Capone:** Okay. Where am I going?

**Nikki Muncey:** So on the left. If you scroll down and see if there's a robots.txt file, because it says, Framer says that it creates it automatically. So it says, the robots.txt file serves as a guide for web robots, blah, blah, blah, blah, blah. Framer generates a robots.txt file automatically to view this file as slash robots to the end of your URL, blah, blah, blah. So it does it automatically. We need to edit it. So edit.

**Jenn Peters:** Like, where would that even be? These are just the pages.

**Nikki Muncey:** Yeah, it's not, like, in the pages. I can say it with confidence.

**Dave Capone:** So you need to enable custom robots.txt. So first you need to enable the option to create a custom robots.txt file. Listen. As you to override the automated generated block. Okay, how do we do that?

**Nikki Muncey:** This is every day, y'all.

**Jenn Peters:** Every day. What about in site settings at the top and the gear on the right? Is there anything on the right side? Like, is there anything that little, yeah, in there, is there anything good in there?

**Nikki Muncey:** It's the same place. Oh, it's the same.

**Jenn Peters:** I feel like Framer sometimes doesn't let you access everything. Because it's supposed to be just a plug and play, ready to go. You just, you know, we're going to do this for you automatically. Where is it? You'll never. Can you click the gear icon?

**Dave Capone:** That's what I did. That's where I am.

**Jenn Peters:** That's what we're in.

**Dave Capone:** Okay, so then it says we can create a meta robots directive. Do. Going to That's what We'll be to disallow a landing page. A what? So we can create a meta robots tag that will no-index the landing pages. So instead of... So then which pages do we want to no-index? Spaces.

**Nikki Muncey:** Spaces.

**Dave Capone:** So on the left-hand side, on page settings, do we have one for spaces?

**Nikki Muncey:** Oh, okay, hold on. You are talking about... Okay, so now...

**Dave Capone:** Yep, there's spaces. So if we're going to de-index all of those pages, then show pages and search engines is unchecked. So that should no-index them.

**Nikki Muncey:** All right, so I'm on the...

**Dave Capone:** So it's... Redirects are live. Yeah, I think we're good. Spaces. I'm just going to go to the search console and find one.

**Nikki Muncey:** I think we're going to be good.

**Dave Capone:** Okay.

**Nikki Muncey:** Do we need to also nofollow or not yet?

**Dave Capone:** I think because that's unchecked, show in search engines, I think that's already going to automatically apply the noindex on those pages. I can't find one that's open to confirm it. Give me one second because we redirected them all. Okay, this one's a 404. Spaces biology. It's spelled wrong. Yeah, see, that one's redirecting fine. I think we're going to be okay. Okay.

**Dave Capone:** So I think we, the 301s are going to handle most of the redirection. So once they're 301, they will not be indexable at that point because Google can't get to them. And then if they are still open, that show page and search engine is unchecked, which should be. Just allow them from showing up. So, okay, wait.

**Nikki Muncey:** So I actually think that the question is. Yeah, we're like in a weird spot because the. Yes, I think this will prevent them from this will prevent the www.1s from indexing. And then they put like robots.txt. This is where I'm repeating words that I've heard that I don't fully understand. But like. Yeah. On AppDot, on those pages, but the AppDot pages as part of the sitemap is like something we control on our end is what I was told. So I can't get to robots.txt on AppDot.

**Dave Capone:** So there it is. Okay. So I see allow all of the different spaces on there. So that's fine. Let me go and make sure that they're probable. This is fine. We got it. Think we got this. Wait, we're allowing all spaces?

**Nikki Muncey:** Not all of them.

**Dave Capone:** I see a list of maybe 28 or so. Or no, yeah, maybe. That's more than 28. That's 50. There's a lot of them on here.

**Nikki Muncey:** That can be indexed or that cannot? That can be indexed, yes. Okay, so there should be like 800 that can be indexed. And everything else should not be indexable. Does that match with what you're seeing?

**Dave Capone:** No. Okay. So disallow user agent all. Here, I'll share my screen so you just don't look at me trying to figure this out in real time. Okay. So this directive here, user agent star, is going to say all search engines, and then we're allowing only these specific pages to be open. Okay.

**Dave Capone:** But they're going to be open anyway because the directive is to allow everything to begin with, right? So what I would do is at the bottom of this list, I would then put a disallow, see how it's disallowed private? I would then put disallow spaces. Because the way the robots.txt file works, it'll see these first and allow those spaces to be open. And then close everything else.

**Dave Capone:** So if I were to put the disallow at the top, then it would block everything and these wouldn't get indexed. So the order really matters in how you put it in your robots.txt. So here, after this disallow private, I would put disallow spaces.

**Nikki Muncey:** And then I was trying to understand the nuance of this yesterday with ChatGPT. Is there something in addition to the robots.txt that we need to do? Like it was saying, like, robots.txt is half the thing?

**Dave Capone:** Yeah. So robots will, if it's already indexed, then you would, once Google finds the robots, disallow the robots.txt, it should get rid of it. Okay. But you can have either or. So if You have a meta robots in your code on the landing page. That's a directive also to tell it not to index, but it'll obey both of them, right? So you don't need both. It's overkill. As long as you have it here in the robots.txt file, you'll be fine.

**Nikki Muncey:** Okay, so I don't need the robots.txt and a noindex meta tag.

**Dave Capone:** Correct. Like you can, like a lot of times folks just do it anyway, but it's basically overkill at that point. Okay. So as long as you have, I added the code you would need to put in that on the bottom of the robots.txt file, and I can test this too when you put it in there in that one or have the devs put it in there, and we can go through and test a bunch of that. But as long as you put that at the bottom of it, you should be fine.

**Nikki Muncey:** And then do I get the sense that we just need to like rebuild our sitemap? So are thoughts on that?

**Dave Capone:** So is... It's like these spaces, pages won't be removed from the sitemap, right?

**Nikki Muncey:** Correct.

**Dave Capone:** So that would, the way Google would handle that is that it would impact the crawl budget, right? Because Google is going to allocate a certain number of pages that it's going to crawl per day. And if it does find one of those spaces that is no index, it'll just skip it. But that'll waste a page that Google could have indexed, a good page that Google could have indexed. Okay. So taking them out of your sitemap is probably, you know, the best thing to do.

**Nikki Muncey:** How do I do that?

**Dave Capone:** So then in Framer, I would have to switch in Framer how to do that. Okay.

**Nikki Muncey:** Well, yes. So if you can take that as an action item, like figuring out how to do it in Framer, but also this sitemap includes these app.pages, and that is also not managed by our product team. Like, I don't know who that lives with. So... So we need to figure out sitemap that encompasses www and app. And then we need to clean up the whole thing. So, yeah. Okay.

**Dave Capone:** It's a stretch, but could I be able to have access to Framer so I can do some tests?

**Jenn Peters:** We have it. We do. Well, don't we have it through our team email already? That's how I'll access it, in there. Chaos in there. Can get in. So you should have access through the team email already. Yeah. And hopefully Framer will let you see all the things you need to see because I know Framer likes to not allow.

**Nikki Muncey:** Framer is fun. Just let me know if you can't access anything that you need to access.

**Jenn Peters:** Yeah.

**Dave Capone:** I'll try and take a look tomorrow. If I can't get to it tomorrow, I'll But yeah, that should be, I'm not going to say it's simple because obviously Framer has its quirks. So I'll do what I can to try and make it work.

**Nikki Muncey:** And if we need to, I don't know how any of this works, but if we need to put something on top of Framer, like some sort of tool to build a sitemap that will work and is optimized and is whatever, like let's do it right once if we can, instead of band-aiding it with Framer right now. And then eventually when we rebuild the website, like needing to start from scratch, maybe that's something that you rebuild the website, you start from scratch anyway. But like, just, we are willing to get what we need to do the thing right. We're already building a whole new website right now, which is also happening.

**Jenn Peters:** I think for a, I could crawl.

**Dave Capone:** I create a sitemap XML file that has all the correct pages in there using the right directives to make sure that all the right pages are. However, would have to update it incrementally every time, like once I'm going to update it and run that myself. It's clear that I do. That is something that we can do, but I would typically want that to be done by the CMS because that's, you know, Google's going to, if Google looks at the sitemap and you launch four pieces of content and it's not in the sitemap, then that's pretty bad. Like, you know, Google wants to make sure that, you know, it's in the navigation, we have internal link, it's in your sitemap, and like that signifies importance. If it takes like a week for me to update the file, then that's something that's going to be counterproductive.

**Dave Capone:** So because of the frequency that we're launching content, I would recommend against that, that we just have a static, you know, sitemap file for now. So I'll investigate what's going on in Framer and then see if there's something I can do.

**Nikki Muncey:** Okay. Good luck. Thank you. And thanks for, I realize we're seven minutes over just barely. So thank you both.

**Jenn Peters:** No problem. See you. All good. Talk to you soon. Bye.
