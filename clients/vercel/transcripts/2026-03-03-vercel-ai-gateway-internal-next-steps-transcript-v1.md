# Vercel AI Gateway — Internal Next Steps
**Date:** March 3, 2026
**Duration:** 47 minutes
**Participants:** George Haikal (GrowthX), Kirkland Gee (GrowthX), Tamyres Ogasawara (GrowthX), Hassan Rashid (GrowthX)
**Source:** Fireflies

---

## Summary

Internal GrowthX team sync on the Vercel AI Gateway SEO workstream. The team defined an MVP approach: ship SEO fundamentals (titles, headings, descriptions, FAQs) without waiting on Vercel's backend data, then layer in dynamic data and UI components as a second phase. Hassan presented his keyword research and competitive audit. The group debated how much impact copy-only changes would have, with Tamy and Kirkland expressing skepticism but agreeing it builds momentum and captures low-hanging wins against weak competitor content. Kirkland proposed a workflow: Hassan finishes keyword research and produces 1-2 example optimized pages, Tamy builds a JSON generation workflow to scale changes across all ~170 pages, and Kirkland vibe codes a UI mock-up inspired by Open Router's tab structure. Kirkland also identified two technical SEO issues: comparison pages lack canonical URLs (swapping model order creates duplicates) and pages depend on JavaScript rendering (not server-side rendered), hurting crawlability. The team aligned on getting content format and data model answers from Vercel before Thursday's call.

## Action Items

**Hassan Rashid:**
- Complete detailed keyword research, filling in competitor data from Semrush and categorizing by page clusters to identify priority SEO opportunities
- Produce 1-2 example pages with optimized content edits (titles, headings, descriptions, FAQ sections) to guide the scalable content workflow

**Tamyres Ogasawara:**
- Build a workflow for generating JSON documents containing content enhancements (titles, headings, FAQ sections) for all AI Gateway pages, based on Hassan's examples
- Align with Kirkland on finalizing best format for content delivery to Vercel and adapt JSON output if needed

**Kirkland Gee:**
- Investigate Vercel's preferred content delivery format and data model structure to facilitate easy implementation
- Draft a rapid UI mock-up inspired by Open Router's tab structure (performance, providers, pricing, apps) for the AI Gateway model pages
- Support Tamy in building the JSON content workflow by leveraging AI tools (Claude, Opus) to accelerate content change drafts

**George Haikal:**
- Coordinate with Vercel team to confirm frontend access and data model sharing to clarify technical scope
- Facilitate approval and early delivery of content and UI changes as baseline SEO enhancements prior to deep data integration

---

## Key Discussion Points

### MVP SEO Strategy
- Team agreed on phased approach: SEO fundamentals first (copy, headings, FAQs, metadata), data integration second
- Skepticism that copy-only changes will move rankings significantly, but consensus that it builds momentum, shows progress, and captures low-hanging wins
- Competitor content (Artificial Analysis, Open Router) is driving more traffic than Vercel despite lower quality content, suggesting opportunity for quick gains
- Vercel is open to any SEO changes the team recommends, no constraints on approach

### Content Workflow
- Hassan finalizes keyword research and produces 1-2 example optimized pages as templates
- Tamy uses examples to build a scalable workflow generating JSON documents with content enhancements for all ~170 pages
- JSON is the ideal output format. If Vercel needs something else, add a conversion step at the end
- Phase 1 scope is text and media only. Tables, charts, and dynamic data are phase 2

### Technical Issues Identified
- Comparison pages have no canonical URLs. Swapping model order (Qwen/Gemini vs Gemini/Qwen) creates duplicate pages with different URLs
- Comparison pages are client-side rendered only. Disabling JavaScript shows no content. Need server-side rendering for SEO and LLM crawlability
- Kirkland suggested generating markdown versions of pages for LLM training data accessibility
- Pages are programmatically generated via Next.js with data stored in a console backend, not a traditional CMS

### Access and Format Questions for Vercel
- What format does Vercel want content updates in for 170 pages? JSON ideal, but need confirmation
- Can they share the data model so the team can match their structure?
- Frontend (Next.js) access status: not a blocker for phase 1 (JSON handoff), but needed for phase 2 UI work

### UI Mock-ups
- Kirkland to vibe code a mock-up adding tabs (performance, providers, pricing, apps) to the model page, inspired by Open Router
- George Main may be looped in for polished visuals after initial prototype
- Comparisons page is highest priority for mock-up due to URL multiplication potential
- Vercel is already building their own comparison tool, which excited the team

---

## Transcript

George Haikal: Hey, hey,

Kirkland Gee: hey, what's up?

George Haikal: Hello.

George Haikal: Hello.

George Haikal: Hey, Tammy.

George Haikal: Hey, Hassan.

Tamyres Ogasawara: This meeting is being recorded.

George Haikal: You still sick, Kirkland?

Kirkland Gee: Mostly, no.

Kirkland Gee: My allergies are bothering me now, but otherwise I'm much better.

Kirkland Gee: Finally.

George Haikal: Nice.

George Haikal: I'm assuming everyone's met, right?

George Haikal: Hassan, you've met Kirkland and Tammy.

Kirkland Gee: I actually don't know if we'd like properly met, but I've been in a meeting with you before.

Hassan Rashid: I'm sure we've been in meetings.

Tamyres Ogasawara: Yeah, yeah, Me and Hassan, we know each other off pipeline feedbacks.

George Haikal: The fun stuff.

George Haikal: The fun stuff for sure.

George Haikal: Hasan is helping a ton with or is and will continue to be helping a ton with Vercel.

George Haikal: And he did a lot of, like, the keyword research and understanding what could drive the most impact for the AI gateway portion of the site.

George Haikal: And so I wanted to kind of like brainstorm and figure out next steps during this call on, like, how can we get to a point where we can tell the client these are the changes we want to make to the existing page and why, and so we can figure out on our side the priority and what's going to drive the most impact in terms of search and what's already out there.

George Haikal: But I wanted to get with you all on, like, what's actually possible, because we don't want to have to wait on their data.

George Haikal: Like, we can at least get to a baseline of SEO fundamentals to have them start competing, and then we can layer in as a V2 after this first sprint all their data that they're going to give us access to.

George Haikal: So that's the way I was thinking about it.

George Haikal: But there's a lot in between what I just said and, like, actually putting it into practice.

George Haikal: And so, Kurt, kind of see your brain cooking on something.

Kirkland Gee: Yeah, listen, I'm just trying to think.

George Haikal: I think what can help is if I show you all this and I'll send the link in here as well.

George Haikal: Put the link in here.

George Haikal: This is what Hassan built out.

George Haikal: And it's essentially like a keyword research and audit of, like, all the competitors that we found for their AI gateway.

George Haikal: And we'll pull in how they're actually doing in terms of search volume.

George Haikal: But I think the most important piece here to help us focus is like, the priority summary and, like, where we can start competing immediately with the competitors that are driving the most traffic.

George Haikal: And, like, tactically, it's like, what are the changes we can make on the page to help give them a shot at each one of these?

George Haikal: Like, I think to them, that's what they care about.

George Haikal: And that's like, the clearest way we can communicate it is how can we make an impact in these areas?

George Haikal: We try to get edit access as well.

George Haikal: So could you give edit access to this, please?

George Haikal: Yeah, just requested it.

George Haikal: Thank you, sir.

George Haikal: Here are all the page types broken down.

Hassan Rashid: Yeah.

Hassan Rashid: Try now.

Hassan Rashid: Yeah.

Hassan Rashid: I think the starting with the page templates or, you know, taking a look at those might be helpful, just because something like a calculator might be a bigger lift than just a comparison or a leaderboard or a ranking.

Hassan Rashid: So maybe we can get some insight there.

George Haikal: And ultimately they're down for whatever.

George Haikal: We met with them on Friday, met with them on Friday, and they're open to whatever changes we want to make.

George Haikal: And in the interim, we can just send them whatever we have for them to publish it until we plug in.

George Haikal: So we don't have to wait to plug to plug into anything.

Kirkland Gee: What are they going to be able to.

Kirkland Gee: Are they going to build out these pages, you're saying, or what?

Kirkland Gee: Like, we can send stuff to them.

Kirkland Gee: What.

Kirkland Gee: What can they do right now before we have access to stuff?

George Haikal: I mean, whatever we want, basically back that up.

Kirkland Gee: What are they gonna do?

Kirkland Gee: What are they gonna have the time and resources to actually build out for us?

George Haikal: I think, like, structurally here, probably nothing.

George Haikal: But adding any sections on these pages, I don't think would be a massive lift for them.

George Haikal: Changing anything that's already on here.

George Haikal: Adding like.

George Haikal: Yeah, anything outside of, like, changing the entire structure.

George Haikal: Like, that's more of a.

George Haikal: Let's get with George Manning, figure out what the best approach is.

George Haikal: But I think enriching they're open to doing.

Kirkland Gee: In the interim, can we add or change the.

Hassan Rashid: How the tables or how the data is presented and displayed like a table in.

Hassan Rashid: Or like a graph instead of a table?

Hassan Rashid: Can they do that stuff?

George Haikal: Yes.

Hassan Rashid: Okay.

George Haikal: Looks like they have changes, too.

Kirkland Gee: Okay.

Kirkland Gee: So, Hasan, you've done a bunch of research and kind of thought this through, right?

Kirkland Gee: I mean, you're much farther along than I am on, like, thinking about what we should do.

Kirkland Gee: I've mostly been thinking about how we can do it right.

Kirkland Gee: Or what we need access to to be able to do it.

Kirkland Gee: So

Hassan Rashid: it was.

Hassan Rashid: It was all Claude, but, you know,

Kirkland Gee: it always is at this point.

Kirkland Gee: No one's doing any real.

Hassan Rashid: Yeah, I mean, I'm now going into, you know, like, if you go into the.

Hassan Rashid: The keywords tab, I'm now going into each, like, specific competitor and getting the actual data from Semrush and filling in that volume of the kd Columns and a few others.

Hassan Rashid: And we ideally want to categorize this by like the cluster so or like I guess the template or the cluster so what type of page template we're looking at and for each competitor, what keywords they're ranking for that Vercel is not ranking for and what the priority should be.

Hassan Rashid: So that's really what I'm thinking in terms of like the overall structure right now.

Hassan Rashid: But I don't, I'm not sure how that data should be presented.

Hassan Rashid: There's definitely going to be stuff that Vercel already has and we can enrich that or update that, that table or graph or whatever they already have.

Hassan Rashid: So that's great.

Hassan Rashid: But outside of that I'm not sure any, you know, like data that they don't currently have on the website, how we can best present that and what their capabilities are for, you know, showing or presenting that.

Tamyres Ogasawara: Question.

Tamyres Ogasawara: Did you notice any particular components and, or type of section in the competitors that all of them have or like at least the most relevant of them have versus like how the way the Vercel page is structured right now?

Hassan Rashid: George, do you want to show the Open Router and the Ollama examples?

Hassan Rashid: I think those are some good ones and we might have some.

Hassan Rashid: Vercel might not have some.

Hassan Rashid: Some of those.

Hassan Rashid: Like

George Haikal: can you see my screen?

George Haikal: So it's like Open Router does a really good job of organizing by pulling in their like usage data as well.

George Haikal: And so different providers, different performance.

George Haikal: Like we will have access to this stuff from Vercel a little bit.

George Haikal: Some of it will be different.

George Haikal: Like we're not going to be able to get the tokens but we'll be able to get like the percentage of usage is what they said.

George Haikal: Because compared to Open Router for example, they're like way less in terms of number of tokens.

George Haikal: So they just want to show percentage.

George Haikal: But apps activity uptime, like this is all stuff that we can do and it's all in the document that I sent as well.

George Haikal: But I mean something that even like little things like.

George Haikal: Hold on, they did a really good job at like filtering and adding some tags as well.

George Haikal: Let me go find the actual sheet that it was.

George Haikal: It might have been Olama as well.

Hassan Rashid: So Tammy, you can, you can kind of notice the, in that activity tab for Open Router they have like a, the bar that fills in.

Hassan Rashid: So stuff like that I don't think I've seen on the Vercel website yet.

Tamyres Ogasawara: Yeah, like more question to Kirkland in this case, if the main value is actually coming from this type of data, then where we will extract this consolidated data.

Tamyres Ogasawara: Like do they have already kind of like a database that we can extract this information from?

Tamyres Ogasawara: This is the main thing that I'm thinking about because then it's not exactly something that for example, we can have a pipeline or a simple programmatic SEO initiative.

Tamyres Ogasawara: It's more like a tool in a way.

Kirkland Gee: Yeah, I think you're thinking about this the right way.

Kirkland Gee: I think generally there's not really anything that we're trying to do here that we're going to get from like say web research or from much AI of anything.

Kirkland Gee: Like.

Kirkland Gee: Yeah, which is mostly front end design and building UI to surface data.

Kirkland Gee: They already have.

Kirkland Gee: Like that is really most of what we're trying to do, at least initially.

Hassan Rashid: Yeah, totally.

Kirkland Gee: And so George, I saw some notes in here about like they're willing to give us front end access, but also you're saying they're willing to do some of the work or build some of this.

Kirkland Gee: So like, what, what is the goal of this meeting?

Kirkland Gee: Are we trying to come out of this meeting with like a clear prioritized list of do this, then that, then that, then that?

Kirkland Gee: Like, is that what you're trying to get at to start?

George Haikal: Yes.

Kirkland Gee: Okay.

Kirkland Gee: Yeah.

George Haikal: And it's like, what's the MVP to get them to like SEO Fundamental Chef's Kiss without having to incorporate their data?

George Haikal: Because we still need this week to figure that out.

George Haikal: And so like what's the low hanging fruit we can already attack for them?

Kirkland Gee: Where do these pages.

Kirkland Gee: Do these pages live in a cms?

Kirkland Gee: Did we talk about that?

Kirkland Gee: I don't, I don't recall.

Kirkland Gee: Like, are they just in the repo or they.

Tamyres Ogasawara: I don't think, Yeah, I don't think we talked about CMS specific stuff.

George Haikal: No, they're currently generated programmatically.

George Haikal: The console holds the underlying data run as Next js.

Kirkland Gee: Yeah, cms.

Kirkland Gee: Okay, yeah, yeah.

George Haikal: And like this is what I'm saying.

George Haikal: Like if we want better copy, if we want to add things to any of them, they can just.

George Haikal: Her team can update it.

Kirkland Gee: Okay, so something we could do.

Kirkland Gee: All right, so.

Tamyres Ogasawara: So I mean, one thing.

Kirkland Gee: Yeah, no, I was gonna say like, okay, good, just rewrite some of the copy.

Kirkland Gee: Like use AI to write a better title and a better description and a better whatever.

Kirkland Gee: But like how useful is that?

Tamyres Ogasawara: Like, yeah, this is exactly where I was getting.

Tamyres Ogasawara: Because I was going to say like, of course we can add, for example FAQs and get better headings and get better intros and this type of stuff is fairly like, similar to what we do on a daily basis.

Tamyres Ogasawara: But how much is this actually going to impact rankings is something that I'm thinking about because for me seems like very heavily reliant on actually, like having a dynamic component so we can increase like, engagement with the page and time in the page and this type of stuff.

Tamyres Ogasawara: At least that's my impression.

Tamyres Ogasawara: I don't know if Hassan has a different, like, perspective of maybe there are some copywriting in terms of like, textual or even like media stuff that we can add in the meantime, while we wait to have higher clarity of where this data is coming from and how we will actually work in partnership with them with like enhancing the UI or like the two in general.

Kirkland Gee: Yeah.

Kirkland Gee: Huh.

Kirkland Gee: Excuse me.

Kirkland Gee: Yeah, that's kind of what I'm thinking is like, what do we actually like, if we do want to have a phase one, that's before we have access to data.

Kirkland Gee: Like, what is that?

Kirkland Gee: I'm not sure it makes sense to just rewrite the paragraph at the top and change the title.

Kirkland Gee: Like, I mean, I don't think that's going to make a meaningful difference because

Tamyres Ogasawara: like, one question that I have for if we compare Vercel with the other players, how they are looking, like, in terms of like, authority and number of ranks and keywords and this type of stuff just for me to understand in a benchmarking perspective how well they are positioned or if they are even like weak on these points, because if they are weaker in these points, which might be the case, and then we just like redo a paragraph and headings.

Tamyres Ogasawara: I don't know how much results this will get us.

Tamyres Ogasawara: Like we can do it.

Tamyres Ogasawara: But I'm just trying to think in terms of leverage, what could be what we pull here in this case.

George Haikal: Yeah, I'm pulling them up right now to show you.

George Haikal: But the short is there's Vercel's not showing up in the top for pretty much anything related to the AI Gateway stuff.

George Haikal: And there's a ton of room to grow and we'll have this done like today so we can share on, like actually show.

George Haikal: But yeah, let me pull up.

George Haikal: This is Ollama.

George Haikal: This is Open Router.

George Haikal: We'll do Vercells as well.

George Haikal: You can see what they're coming out.

George Haikal: That's their main competitors.

Kirkland Gee: probably because most of the keywords are branded in some way, shape or form.

Tamyres Ogasawara: Yeah.

George Haikal: Vercel, AI Gateway and then Jacob, AI Gateway, Vercel.

Tamyres Ogasawara: Can you please go back on Open Router so I can see the Metrics, I mean, like the smrc.

Tamyres Ogasawara: Yeah, Correct.

Tamyres Ogasawara: I mean, Versailles not looking bad on the models though, compared to them.

Tamyres Ogasawara: Maybe we can get like some edge, like editing headlines and adding maybe like FAQs and this type of stuff, at least on long tails.

Tamyres Ogasawara: What do you think?

Tamyres Ogasawara: Work with.

Kirkland Gee: Yeah, I mean, so actually backing this up.

Kirkland Gee: Okay.

Kirkland Gee: Me and Tammy are not necessarily convinced it's going to make a huge difference, but George is there.

Kirkland Gee: I'm thinking just relationship wise, we know this is only one piece of the puzzle.

Kirkland Gee: Right.

Kirkland Gee: But is doing that piece very quickly a valuable thing to do?

Kirkland Gee: Knowing that we have a second piece coming after?

Kirkland Gee: Right.

Kirkland Gee: Like, we're not saying, hey, these improvements are going to give you the rankings you deserve, but, you know, this is a piece of the puzzle.

Kirkland Gee: Let's do it first while we're waiting.

Kirkland Gee: Like, I think maybe that's the way we should be thinking about this.

George Haikal: That's the way I'm thinking about it.

Kirkland Gee: Yeah, we just need to.

Kirkland Gee: We just need to like spin some wheels and like do something quickly.

Kirkland Gee: And this is the one place where maybe we're not blocked at all.

Kirkland Gee: And yeah, Tammy, we might learn something from it, right?

Kirkland Gee: Or we might get some information.

Kirkland Gee: So.

George Haikal: Correct.

George Haikal: And like.

George Haikal: Yeah, I completely agree.

George Haikal: And like, like what kind of kills me is look like this page is doing better than Vercel's deep seek on their AI gateway, right?

George Haikal: Like this ArtificialAnalysis AI right there.

George Haikal: Their models leaderboard, which is right here.

George Haikal: And then their comparisons, right?

George Haikal: These are both driving more traffic than anything Vercel is doing on their AI gateway.

George Haikal: And the content is shitty.

George Haikal: And so like, we can beat this for sure.

George Haikal: And so I'm trying to capture some of that.

George Haikal: I understand we can't do it in one.

George Haikal: That's why I'm talking.

George Haikal: It's like, I don't know either.

George Haikal: It's more.

George Haikal: So like, what are.

George Haikal: What can we phase out to show progress and early wins?

George Haikal: Like you were just saying, Kirkland.

George Haikal: Yeah, to get to like a baseline.

George Haikal: Because right now I don't want to wait like two weeks to like plug into their data and then.

Kirkland Gee: Yeah, yeah.

George Haikal: And there's going to be a back and forth for sure with their team.

George Haikal: And so.

George Haikal: Yeah.

Kirkland Gee: Okay, so what I'm thinking then can you go back to the Vercel page?

Kirkland Gee: So do we have any idea what the data model for this page looks.

Kirkland Gee: Looks like at all?

Kirkland Gee: Like what is just text versus what's coming from some database somewhere?

Kirkland Gee: I don't know if they talked about that at all.

Kirkland Gee: So front is a next JS App would not be able to touch underlying data.

George Haikal: We can look at the front.

Kirkland Gee: I'm just trying to think about like if we're going to give them content we want to change, like what, what format do they need that in?

Kirkland Gee: You know what I mean, to make that easy.

George Haikal: Yeah, I know.

Kirkland Gee: Tammy, what are you thinking about?

Tamyres Ogasawara: I was going to ask you and Hassan who did the research.

Tamyres Ogasawara: How do you feel about maybe targeting one specific cluster and trying to go for long tails and try to go for like adding FAQs with long tails.

Tamyres Ogasawara: This is one thing that I can see as maybe getting a smaller win without having to rely so much on their database.

Tamyres Ogasawara: Because what I want to avoid is us spinning the content with things that are available on the web and maybe they won't provide like something very valuable to rank for like higher volume terms.

Tamyres Ogasawara: But maybe if we go for long tails in a specific like FAQ way we can get maybe also AI citations since Vercel is a relevant player.

Tamyres Ogasawara: So I was kind of thinking that this could have like, give us some wins.

Tamyres Ogasawara: And in terms of like difficulty of doing that technically it's very like, it's very much closer to the quote unquote easier, technically speaking.

Tamyres Ogasawara: So I don't know what you think.

Hassan Rashid: Yeah, I was, I was thinking of FAQs as well, kind of as a long term or you know, like long run keyword play.

Hassan Rashid: But George, I'm also curious.

Hassan Rashid: Did they specifically request any like, did they just say, oh, like if you guys see any copy improvements or H2H1 improvements, feel free to let us know?

Hassan Rashid: Or did they, did they actually have like specifics they could see?

Hassan Rashid: Oh, like we kind of notice like these pages aren't ranking well just because they're the headings or whatever aren't optimized.

Hassan Rashid: Did they have any specific like ideas around that or was it just whatever you guys see isn't working and let's just fix those?

George Haikal: Yeah, it was, it was more the latter.

George Haikal: Like we're very open minded about what we can do in SEO and Gateway.

George Haikal: Like they know it's not perfect and like they're open to any approach that we recommend that would help.

George Haikal: Don't have an impact.

Kirkland Gee: Okay, so I have a few thoughts that I'm just gonna throw out there.

Kirkland Gee: So if I had my, my perfect world, here's how I think this might go is step one, Hassan, you finish up kind of the research that you're doing and just kind of firm up our opinion.

Kirkland Gee: But I think we have a general idea of like what we want to do is step one, and then step one is.

Kirkland Gee: Tammy, we can work.

Kirkland Gee: I say we probably you, but I can also help if you need it.

Kirkland Gee: But I'm confident you can handle it.

Kirkland Gee: Just basically do like a simple workflow to build essentially a long list of JSON documents of whatever enrichments we want to make to the pages.

Kirkland Gee: So if that's, you know, we get a new title, a new heading, a new description, a new whatever other paragraph and then an FAQ section.

Kirkland Gee: And maybe there's one other thing we want to add based on Hasan's research that we're like confident just adding copy in this way will make an improvement.

Kirkland Gee: We can just do a pass on that and send them a document.

Kirkland Gee: No engineering, no code access, none of that.

Kirkland Gee: We can do that all super easily.

Kirkland Gee: We give them back, then we figure out how to get front end access.

Kirkland Gee: While we're waiting on that, we could have George Main or one of us mock up a new UI for the pages.

Kirkland Gee: Just if we did add some of these more dev components like a pricing table, or we built a comparison page.

Kirkland Gee: Like we could work on mock ups first as sort of like what I did for Brex George, where we just like do it on render and just show it to them.

Kirkland Gee: And then either we can pass that off to them and they can implement it, or they can give it to us however they want to handle that.

Kirkland Gee: That's kind of how I'm thinking about this.

Kirkland Gee: But I don't know,

Tamyres Ogasawara: I think, yeah, I think the research that Hassan did is already like very helpful because it shows like the main clusters and keywords and etc.

Tamyres Ogasawara: So this is very helpful for me to have ideas.

Tamyres Ogasawara: But one thing that could be complementary is that maybe Hassan can optimize one page or two pages as an example of how he would do it.

Tamyres Ogasawara: And then I can kind of get the idea of how he's structuring the optimization and then structure like a JSON that I can essentially apply like variables and a higher like abstraction logic for that.

Tamyres Ogasawara: But at least I have like one or two examples to ground myself and say, okay, according to Hassan, this is the most like a optimized way to do that.

Tamyres Ogasawara: I can optimize ABC with just like content, like changes.

Tamyres Ogasawara: And then I proceed to create a quote unquote tool that I can essentially work into applying that for all the existing pages.

Kirkland Gee: Yeah, that's exactly what I was thinking.

Kirkland Gee: It's like.

Kirkland Gee: And that's like, that's a good suggestion.

Kirkland Gee: Yeah.

Kirkland Gee: Step one is let's get an example of what we would change about this page and then we can scale that example and give them the content just as a document of some kind and then we can start prioritizing.

Kirkland Gee: Okay, then do we make new pages or do we add components to these pages?

Kirkland Gee: Like what's the next best thing?

Kirkland Gee: I guess that needs to be led a bit by the research of like do we do comparisons next?

Kirkland Gee: Do we do pricing?

Kirkland Gee: Do we just improve the model pages?

Kirkland Gee: Like what's the next best thing to do?

Kirkland Gee: And then we can either mock that up or depending on timing for them getting us access, we can just do it.

Kirkland Gee: Like I don't know how particular they're going to be, right.

Kirkland Gee: Because they said they're like kind of okay with it.

Kirkland Gee: But you know how that goes George.

Kirkland Gee: Like yeah, Brex.

Kirkland Gee: I'm just, I'm traumatized by Brex.

Kirkland Gee: But that's a.

George Haikal: Don't even get me started, dude.

George Haikal: So much has happened too.

George Haikal: I won't even worry on this call.

Kirkland Gee: I got my Brex laptop here.

Kirkland Gee: I'm on this laptop.

Kirkland Gee: I got my personal laptop over here just in case.

George Haikal: We just, we just lost our point of contact at Brax.

Kirkland Gee: Really?

George Haikal: Yeah.

George Haikal: And so.

Hassan Rashid: Oh yeah, yeah.

George Haikal: It'll be a fun week.

George Haikal: It's been a fun week.

George Haikal: Yeah, we're figuring it all out, but it's not easy.

Kirkland Gee: Didn't they pay up front though?

Kirkland Gee: Wasn't.

Kirkland Gee: Didn't they do something crazy like that?

George Haikal: Yeah, but they're gonna get hit with the actual invoice in 10 days, eight days.

George Haikal: And so I want them to see it and it be a no brainer.

George Haikal: But when you layer in the acquisition and capital one, adding a bunch of compliance steps for our content now like we'll see.

Kirkland Gee: Yeah, that's tough.

George Haikal: We'll see.

Kirkland Gee: But hey, I'm gonna get the charge finder I think finally live probably tomorrow.

Kirkland Gee: So at least that'll be there for them to like have as value as like.

Kirkland Gee: Whoa.

Kirkland Gee: They did this.

George Haikal: So, so nice.

George Haikal: Is there anything blocking you there?

Kirkland Gee: Just, just finishing it.

Kirkland Gee: I finally got unblocked access wise today and then my Sanity access expired and so I had to redo that and they had to make me a new Slack account to be able to request the access to Sanity.

Kirkland Gee: And then my vercel access was wrong because it was on two different accounts and one of them had the wrong access that was linked to the wrong GitHub account.

Kirkland Gee: So they had to fix that.

Kirkland Gee: So right now I just have to fill out the data in the charge finder.

Kirkland Gee: Like actually get the data into Sanity from our workflow flows, but that's mostly fine.

Kirkland Gee: So.

George Haikal: Yeah, sounds like a nightmare.

Hassan Rashid: That could be.

Hassan Rashid: That could be good for.

Hassan Rashid: As a backup for ramp as well once charge finder is done.

Hassan Rashid: Just in case,

George Haikal: as a.

George Haikal: Well, how do you mean?

Hassan Rashid: You know, when you said like as well as a backup or as an upsell, in case they're not like going with us for whatever.

Hassan Rashid: However many results we've gotten in the AI visibility space, if we want to do like a programmatic upsell for them or.

George Haikal: Yeah, just show them.

George Haikal: Yeah, yeah, it's.

George Haikal: What we're trying to do is leverage the BREX work for them.

George Haikal: I mean, the thing is we're, we're building these tools because ramp has them existing and they're driving traffic already.

George Haikal: But what we're doing looks way better and should perform better than ramps is our bet.

George Haikal: And so at least looks way better right now is what we can control.

George Haikal: And so it still would look good.

George Haikal: But.

George Haikal: Yeah.

George Haikal: So for this it sounds like finalize the keyword research and then an example of great one great page.

George Haikal: What the changes we should make on that page, what they should look like.

George Haikal: And then from there we'll figure out what to do next.

George Haikal: But that's basically prioritizing all the work that we can send to the AI Gateway team this week or whenever it's done that they can go and publish on their own in terms of access or.

George Haikal: Did I miss anything?

Kirkland Gee: Can you just.

Kirkland Gee: Can you find out from the Vercel team what format they'd like that content in?

Kirkland Gee: Like, if we have suggestions on if we want to give them content for 170 pages?

Kirkland Gee: Like, what's going to make it easy for them to implement that?

Kirkland Gee: Like, is it a JSON document?

Kirkland Gee: Is it.

Kirkland Gee: Can they give us the data model so we can like match it?

Kirkland Gee: Like, you know, what do they want that would be good as Tammy builds a workflow to just know what the output of that workflow should look like.

Kirkland Gee: Yeah, exactly.

Kirkland Gee: JSON is ideal, but I mean, do they need something else?

Kirkland Gee: I don't know.

Kirkland Gee: And truthfully, Tammy, you can do it in JSON anyways and then whatever.

Kirkland Gee: Like if they need it in some other format, just add a step at the end to like translate it into whatever they need.

Kirkland Gee: But for sure.

Hassan Rashid: And then do we also.

Hassan Rashid: Oh, sorry, go ahead.

Tamyres Ogasawara: I was just agreeing with, with Kirkland.

Tamyres Ogasawara: We are good.

Hassan Rashid: Do we also want to capture what, what is like just text on the page and what is data flowing in?

Hassan Rashid: Do we.

Hassan Rashid: Do we want to know that as well

George Haikal: on the existing AI Gateway page?

Hassan Rashid: Yeah, so like stuff that we can change that's just like copy or UI stuff as opposed to, I mean, I guess that's pretty apparent now.

Kirkland Gee: I think we can assume all the text that looks like that is changeable and all the stuff the tables is not changeable would be.

George Haikal: Yeah, okay.

Tamyres Ogasawara: Yeah, I was going to say that since we don't have access right now to the database and additional data, if you want to send just the tweaks that you would do in terms of like tags or like adding elements on the page or adding an FAQ or something like that, and then for the tool you can just put a placeholder of like two, then that's, that's great for me.

Kirkland Gee: And I think ideally we can, we can assume we can add new sections, right?

Kirkland Gee: A new heading, whatever we want below it.

Kirkland Gee: We should assume we can do whatever we want with new sections.

Kirkland Gee: Especially if new sections are just content related.

Kirkland Gee: Like if they don't involve organizing a bunch of data that's like this phase one and phase two would assume we can incorporate their data into whatever UI we want.

Kirkland Gee: That's like how I'm thinking about it.

George Haikal: Yeah, no, I think that's right.

George Haikal: This makes sense.

George Haikal: I mean, hasan, this might take a little bit after this, but like, is anything jumping out here?

George Haikal: We can come up with like a full example of.

George Haikal: Great.

George Haikal: Outside of this call as well, but

Hassan Rashid: I have to take a look.

George Haikal: Yeah.

Hassan Rashid: What the competitors are doing, just you know, what the best practices are.

George Haikal: There's one example that had a really good filter as well.

George Haikal: Let me go find it for you.

George Haikal: Cool.

George Haikal: And then anything else in terms of access that we need answers to or that we need to make progress on what format we'd like the content in the pages.

George Haikal: Give us access to the data model if you can.

George Haikal: I know, it's so ugly.

George Haikal: Yeah, I mean it's insane.

George Haikal: And it's like showing it's driving traffic, which is nuts.

George Haikal: And then front end, we still need to answer on front end access.

Kirkland Gee: Yeah, correct.

Tamyres Ogasawara: Front end access wouldn't be a blocker.

Tamyres Ogasawara: If they say that the JSON is fine.

Tamyres Ogasawara: If they say like, oh, you can send us the JSON and then we can publish ourselves, then front end won't be a blocker.

Tamyres Ogasawara: But like in the long run, if we want to create UI edits on the components and this type of stuff, then it will become a blocker.

Tamyres Ogasawara: So I would say like, it is a should have, not like must have blocker.

Tamyres Ogasawara: Everything will crash if you don't have it right.

Tamyres Ogasawara: Now for this first phase.

George Haikal: And in the meantime, because the call with them is Thursday, so we have time but like being able to show them, I think being able to show them the great page at the very least, if not have already sent them the updates and got their approval.

George Haikal: But then like what we're thinking for the different tabs on the pages that we want to add, I think that could be good as well.

George Haikal: Looking through and making sure we have all the questions answered.

George Haikal: Yeah.

George Haikal: I mean, as a V1, that's fine.

George Haikal: It's like, let's get to a baseline of fundamentals and then painting the picture of like, what this can look like next week, in two weeks when we pull in their data, I think would be compelling as well.

George Haikal: Even if it's just like a render.

Tamyres Ogasawara: Yeah.

Tamyres Ogasawara: I think first step would be getting this like, great version and editing everything that is possible with text and media.

Tamyres Ogasawara: Then another next step would be potentially doing like a mock up of what we think.

Tamyres Ogasawara: That would be like a better option with the components and stuff.

Tamyres Ogasawara: And then.

Tamyres Ogasawara: And then starting to build from there.

George Haikal: Cool.

George Haikal: That makes sense.

George Haikal: I know we're out of time.

George Haikal: I gotta jump, but is anyone unclear on next steps?

George Haikal: It's basically tying up the keyword research.

George Haikal: An example of.

George Haikal: Great.

George Haikal: And then from this, Tammy will build out this out for each page, which is basically going to be a workflow.

George Haikal: And then we'll send the output and

Tamyres Ogasawara: then it would be good for.

Tamyres Ogasawara: For them to confirm if JSON works or if they want a specific format for this, like 170ish pages.

George Haikal: Kirkland, what were your thinking on Vibe coding what this could look like for them?

George Haikal: Is that.

George Haikal: Does that even make sense right now before we get these questions answered?

Kirkland Gee: I mean, we could like.

Kirkland Gee: It's not going to be like a.

Kirkland Gee: It could.

Kirkland Gee: Yeah, if you want to do it, we can.

Kirkland Gee: I.

Kirkland Gee: Because like, basically I just try to copy their page and then just add some new components to it in some other app.

Kirkland Gee: I mean, it's one of those things of like, it's like the new Figma, it feels like.

Kirkland Gee: Or instead of designing it, we just actually code it so they can see it.

George Haikal: Yeah,

Kirkland Gee: yeah.

Kirkland Gee: I don't know if you want, like us to do that or if you want to loop in the, like George Wayne or a designer.

Kirkland Gee: I don't know what their bandwidth looks like because, I mean, you know, I'm no designer.

Kirkland Gee: Right.

Kirkland Gee: Like, yeah, I can mock something up.

Kirkland Gee: I can throw some new components on a page.

Kirkland Gee: But George may have a better opinion given Vercel and how Important that is, I think that's up to you where that to go, but I think it's probably worth doing at least just maybe adding something to this page or rethinking the UI here and then, you know, maybe doing one of the other templates.

Kirkland Gee: Whichever one we think is most important, like comparisons or whatever comparisons is probably the one to do.

Kirkland Gee: Because it's like the most.

Kirkland Gee: You get the most unique URLs from comparison pages.

Kirkland Gee: Right, because you just start cross comparing everything.

George Haikal: Yeah.

George Haikal: So they're building out a comparison tool on their end.

George Haikal: Versalas.

George Haikal: Well, you'll be able to pull similar to open routers comparison and I show that to them live and they love the comparison.

Kirkland Gee: So they're going to do this.

George Haikal: Yeah, something similar.

Kirkland Gee: Okay,

George Haikal: Interesting.

Kirkland Gee: Can you try something for me really quick?

Kirkland Gee: Can you just change Quinn to Gemini and then change Gemini to Quinn?

Kirkland Gee: I just want to see if this.

George Haikal: This is so funny to me.

George Haikal: Yeah.

Kirkland Gee: Okay.

Kirkland Gee: And can you right click and inspect this page?

Kirkland Gee: Just go to the dev tools and look at the canonical URL for this page.

Kirkland Gee: Just command F for canonical.

George Haikal: Doesn't have one.

Kirkland Gee: Yeah.

Kirkland Gee: Okay, so what's funny here is like they're making a unique URL based on the different models that you put in, right?

Kirkland Gee: But they're just building the URL left to right with no canonical URL.

Kirkland Gee: So if you swap the order, they're now duplicating the page.

Kirkland Gee: And I don't know if these pages are getting rendered.

Kirkland Gee: Like basically we need to talk to Vercel about how they build this because they need to build it a very specific way where every time you put any combination of models, that adds a new page to the database essentially that gets server side rendered.

Kirkland Gee: And so you don't have to make all the pages up front, but anytime someone does a new combination of models, it should make that static URL.

Kirkland Gee: And then no matter which order, every combination of models has its own page, regardless of the order that you put put them in.

Kirkland Gee: And they'll all be on the same URL.

Kirkland Gee: So whether it's Quen Gemini, seed or seed Quen Gemini, those should be the same URL.

Kirkland Gee: Does that make sense?

George Haikal: Yeah, that makes sense.

Kirkland Gee: Because this case, like you can just keep swapping them back and forth.

Kirkland Gee: Tammy, I've been doing this for way too long.

Kirkland Gee: I also like, funny enough, I built a website for Magic the Gathering rules and I had to solve this problem because like you can put in any number of cards and it generates a page with like an explanation of how the rules work.

Kirkland Gee: And so I had to think through, like, well, what if someone comes and looks at the same set of cards in a different order?

Kirkland Gee: Like, how do I want to handle that?

Kirkland Gee: It's a different thing.

Kirkland Gee: It's the same SEO problem.

Tamyres Ogasawara: It's fresh in your mind.

Kirkland Gee: It's fresh, literally.

Tamyres Ogasawara: But it was crazy for you to think like on the go about this without analyzing the page.

Kirkland Gee: I just was immediately, well, because it's like, developers don't think about that shit.

Kirkland Gee: They're just like, does the UI work?

Kirkland Gee: Cool, I'll just load a hundred different URLs and make it work.

Tamyres Ogasawara: This could actually be a competitive advantage for us.

Tamyres Ogasawara: A relevant one.

Kirkland Gee: A thousand percent.

Kirkland Gee: It's actually like super relevant.

Kirkland Gee: And I don't also, can you do one more thing for me just to check.

Kirkland Gee: And this is something you could actually mention to Vercel.

Kirkland Gee: Go back to the comparison, just whichever one you had, like with all the models loaded.

Kirkland Gee: And then Command Shift P on your keyboard and disable JavaScript and then hard refresh the page.

Kirkland Gee: So Command Shift R. I want to see if this is a rendered page.

Kirkland Gee: Yeah, it's not.

Kirkland Gee: So like, these pages are not going to super easily show up in search.

Kirkland Gee: Like when you make that page, it should now be able to load without JavaScript.

Kirkland Gee: Maybe not the first time.

Kirkland Gee: Like, maybe if no one's ever done it before, then it's not already server side rendered, but it should, should be essentially built at build time and not dynamically rendered so that this can show up in Google as just an HTML page if someone looks for that URL.

Kirkland Gee: So this is like a little, it seems like a little thing, but it does matter.

George Haikal: No, I mean, so that's like amazing.

George Haikal: Yeah, that's amazing.

Hassan Rashid: Does this mean LLMs will also have a hard time?

Kirkland Gee: In theory, yes.

Kirkland Gee: LLMs shouldn't really be able to, like, depending on what crawling engine they're using, which, like, so, so many crawlers are so much better at dealing with JavaScript these days than they were five years ago that, like, it's less of a concern.

Kirkland Gee: But, like, you still want to build it to make it as optimized and easy as possible.

Kirkland Gee: Because if it has to render JavaScript, that takes twice as long to crawl that page.

Kirkland Gee: And like, some crawling engines are not going to get it or they're not going to go as deep or whatever,

Hassan Rashid: you know, this is great ammo.

Hassan Rashid: This is great.

Kirkland Gee: So you can literally show them like, hey, look, we can build this in a way where that doesn't happen.

Kirkland Gee: And yes, Tammy, you're correct.

Kirkland Gee: Alabs do less of this because they're much often just trying to crawl like markdown for it.

Kirkland Gee: Because, like, the other thing is, like, what we could do is for all of these pages, we probably should just have like

Hassan Rashid: some.

Kirkland Gee: We should think about some way of building a markdown version of them for LLMs.

Kirkland Gee: I don't know what that really needs to look like because, like, llabs are probably not going to be getting their model data from Vercel.

Kirkland Gee: Like, like, I don't think we need like a copy page content as markdown button.

Kirkland Gee: Right?

Kirkland Gee: People aren't going to be in their terminal copying the model information to go build something.

Kirkland Gee: Like, it's not like docs, but maybe like, I don't know, we could think about having like a MD file of all the pages stored somewhere.

Kirkland Gee: I don't know.

Kirkland Gee: I don't know if that makes any sense.

Kirkland Gee: I might be.

Kirkland Gee: I may be going a little too crazy right now, but.

George Haikal: No, no, no, I mean, this is all great, man.

George Haikal: This is all super helpful, I think, just for like the sake of time.

George Haikal: Kirkland, do you think you could throw together just what Open Router has done here?

George Haikal: Don't.

George Haikal: We don't need all of it, but basically like some of these tabs.

George Haikal: Performance provider.

George Haikal: Just a few.

George Haikal: And then I can get George Main to make it look like gorgeous after.

George Haikal: But just having a version that we can show would be super helpful to them.

George Haikal: They want to keep the playground, unfortunately.

George Haikal: I asked about usage and stuff and they want to keep it.

George Haikal: It doesn't need to be like the first thing that people see, but any place you can get it, he can take it like the rest.

Kirkland Gee: I could do it tomorrow because I need to wrap up this Brex stuff today, if that's all right.

George Haikal: Yeah, yeah, yeah, that's totally fine.

George Haikal: That's totally fine.

Kirkland Gee: Actually, I can probably just have Claude do it and.

Kirkland Gee: Yeah, never mind.

Kirkland Gee: I. I'm just gonna have Claude do it while I do the brick stuff.

Kirkland Gee: It'll be fine, Tammy.

Kirkland Gee: I will give it a shot first and then I might pass it off to you.

Kirkland Gee: But I really think I can just like yell at Claude for a few minutes or give it the transcript of this meeting and it'll just go and do it.

Kirkland Gee: Probably.

Kirkland Gee: It's crazy what OPUS can do when you just let it think for a while.

George Haikal: You put on a specific mode or.

Kirkland Gee: No, I mean, I'll just do like.

Kirkland Gee: Generally what I will probably do is just take the transcript of this meeting from Fireflies, give it to Opus in plan mode, give it the URL of the open router page and just, like, turn my voice to text on and just talk at it for a minute about the different tabs and stuff.

Kirkland Gee: Give it the vercel page and say, hey, mock up this vercel page with this tab structure.

Kirkland Gee: Mock up all the UI and, like, just let it go.

George Haikal: Jesus.

Kirkland Gee: It'll probably be fine.

Kirkland Gee: Probably is a keyword there, but.

Kirkland Gee: Okay, I'm gonna actually do that.

Kirkland Gee: If you.

Kirkland Gee: If we're good here, I'm gonna jump off and do that while I'm thinking about it, like, while my brain is fresh, and just get that started and then go do this Brex stuff.

Kirkland Gee: Is there anything else we need?

George Haikal: No, I mean, I think that's a good initial step.

George Haikal: I mean, that's, like, fantastic progress for any other client.

George Haikal: We're treating them special because they're custom, so.

Kirkland Gee: Yeah.

Kirkland Gee: All right, cool.

Kirkland Gee: I'm gonna go get that shot real quick.

George Haikal: Cool.

George Haikal: Thanks, everybody.

Tamyres Ogasawara: Thank you.

Hassan Rashid: Awesome.

George Haikal: Later.

Hassan Rashid: Thanks, guys.
