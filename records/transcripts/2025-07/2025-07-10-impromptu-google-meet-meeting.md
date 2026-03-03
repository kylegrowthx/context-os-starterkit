# Impromptu Google Meet Meeting

<metadata>
date: 2025-07-10
time: 18:00 UTC
duration: 22 minutes
organizer: nemanja@growthxlabs.com
participants: Matthew Alves-Hill, Nemanja Simic
fathom_recording_id: 73445281
fathom_url: https://fathom.video/calls/349643094
share_url: https://fathom.video/share/bK4swS86NBskqFy7FU4Jybhx4pRhan9E
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

Matthew walked Nemanja through GrowthX's keyword research workflow for Airbyte, demonstrating how to build a keyword database using SEMrush exports and Airtable's linked records and rollup functions. The team identified 728 unique URLs from 18,500+ keywords across Airbyte's blog and data engineering documentation, then created metrics (keyword count, average difficulty, total search volume) to prioritize pages for SEO optimization. The discussion surfaced a key tension: whether to refresh already-ranking pages or focus on lower-hanging fruit, with Nemanja planning to run the refresh analysis on Airbyte's data and send results to Marcel for direction.

---

## Context

Matthew Alves-Hill (GrowthX SEO/content specialist) was conducting a screen-share training session with Nemanja Simic (GrowthX team member) on building keyword research databases for client work. The context is Airbyte, an open-source data integration platform that's a GrowthX client. Nemanja had previously attempted similar analysis work and wanted a clearer walkthrough of the specific Airtable techniques—particularly how to structure linked records and rollup fields to surface actionable SEO targets. This is core GrowthX delivery methodology: converting raw SEMrush data into prioritized lists of pages to optimize, which informs content refresh work and SEO strategy.

---

## Relevance

**To GrowthX Delivery:**
- Documented the step-by-step Airtable workflow for building keyword databases from SEMrush exports—a repeatable template for other clients
- Introduced the tension between refreshing high-ranking pages (for incremental gains) vs. focusing on low-difficulty targets (for quick wins)—important for managing client expectations on where to focus effort
- Highlighted that linked records + rollup fields create a scalable way to surface metrics (728 unique URLs from 18,500+ keywords) that help writers prioritize work

**To GrowthX Business Development:**
- Airbyte engagement shows GrowthX's strength in working with large, complex docs/content sprawl (2,000+ pages total)
- Potential for expansion: team discussed adding "Top ETL Tools" category pages and potentially optimizing docs pages (not just blog), suggesting deeper engagement opportunity
- Nemanja planning to validate approach with Marcel and then hand off detailed priority list—sign of structured, repeatable engagement model

**To Content & SEO Thinking:**
- Matthew raised valuable point about docs optimization: user experience and developer retention matter as much as SEO rankings, drawing parallel to prior Bafi (developer tool) work where docs quality directly impacts word-of-mouth
- Identified that refresh decisions need to combine ranking data with traffic trend analysis (Google Analytics + Search Console) to understand whether pages are gaining or losing visibility over time

---

## Overview

- Created an Airtable base with 18,500+ keywords from Airbyte's blog and data engineering resources
- Demonstrated how to link keywords to URLs, resulting in 728 unique pages for potential optimization
- Explained the use of rollup fields to calculate key metrics: keyword count, avg. difficulty, and total volume
- Discussed the importance of balancing SEO optimization with user experience, especially for documentation pages

---

## Key Topics

### SEMrush Data Export and Airtable Import

  - Exported CSVs from SEMrush for specific subfolders (blog, data engineering resources)
  - Imported CSVs into Airtable, mapping essential fields: keyword, URL, search volume, keyword difficulty
  - Tip: When importing multiple CSVs, add an extra field to work around Airtable's URL mapping issue

### Creating Linked Records for URL Analysis

  - Used "Link to another record" feature to create a new table with unique URLs (728 total)
  - New table automatically maps all keywords to their respective URLs
  - Provides a consolidated view of all keywords associated with each URL

### Calculating Key Metrics with Rollup Fields

  - Added three crucial rollup fields for analysis:
    1.  Keyword Count: Counts total keywords per URL (e.g., some pages have 400+ keywords)
    2.  Average Keyword Difficulty: Calculates mean difficulty for all keywords on a page
    3.  Total Volume: Sums up search volume for all keywords on a page
  - These metrics allow for prioritization of pages with high potential impact

### Prioritization and Refresh Strategy

  - Sorted pages by total volume to identify high-potential targets
  - Discussed the challenge of determining whether to refresh already well-performing pages
  - Suggested checking individual page performance and rankings to make informed decisions
  - Considered adding sorts by difficulty and volume for more nuanced prioritization

### SEO vs. User Experience Optimization

  - Discussed the importance of optimizing documentation pages for user experience, not just SEO
  - Highlighted how good documentation can impact customer retention and word-of-mouth referrals
  - Suggested potentially focusing on both SEO and UX optimization for comprehensive improvement

---

## Action Items

**Nemanja Simic (GrowthX)**
- Run Airbyte keyword data through refresh process; analyze results
- Send Airbyte keyword Airtable to Marcel for review/feedback
- Share meeting recording link from Fathom with George in Slack

**Matthew Alves-Hill (GrowthX)**
- Add Airbyte keyword Airtable to shared folder in team space

---

## Transcript

**Matthew Alves-Hill:** Cool, okay, so obviously it's a little bit different to the keyword gap because we're just looking at Airbyte specifically, but you basically start with like the subfolders, right? So data engineering resources was one, and then I'll just load the blog in just so you can see. Like, this would come up. You can see there's like a thousand keywords, right? So this is just searching from the blog folder, and then it's straightforward, like a simple export, and you just export them all, right? So this one had a thousand, actually the data resources one had like... this is being slow. But basically all this does is mean we're only scraping from that specific subfolder.

**Matthew Alves-Hill:** So you export both these files as CSVs, save them, and then look, I've already built this Airtable, but I'm going to just talk you through step-by-step how you do it.

**Matthew Alves-Hill:** Okay, so you obviously start with a blank. I've set up a new Airtable base. If it was, like, if you were starting out with keyword research, it would be in the client's content OS. But the process is the same. I've obviously already built this. You can see down here it's 18,500. So these are our 17-and-a-half-plus thousand. I've already imported them.

**Matthew Alves-Hill:** And the way you would do that—again, you probably know. You just like map the fields. So what's important is before the import, there's going to be a load of fields from SEMrush—like traffic and whatever, a load of other stuff. You only really need this. Marcel had "Intense," but because we're only looking at the URLs, it wouldn't map to that table anyway. So I basically just cut down the things that we really care about: search volume, keyword difficulty, and then obviously the keyword itself and the URL.

**Nemanja Simic:** Right.

**Matthew Alves-Hill:** So once you've imported like one CSV file and mapped the fields, there's something about Airtable that when you then try to import further keywords, the URL field won't map to the URL column for some reason. So I just work that around by adding an extra field. You can map the URLs to the extra field, and then you just have to basically select them all and copy and paste them. Okay, a little hack.

**Nemanja Simic:** Okay. So you imported both CSVs there then?

**Matthew Alves-Hill:** Yeah, exactly. So I've imported both CSVs. When you import the first one, you set the fields, and then the second one will, like, map on. And you just want to make sure that sometimes the table's funky and it maps the wrong columns. But you just want to make sure these are the ones you care about.

**Nemanja Simic:** Yeah.

**Matthew Alves-Hill:** And primarily because what we're trying to do here is identify Airbyte pages that have the highest potential for search volume and the most amount of keywords. Like, this is why search volume is important. And we also want the keyword difficulty because it's going to average it in the next step.

**Nemanja Simic:** Yeah, cool.

**Matthew Alves-Hill:** So then once that's loaded in, you basically go to the URL column and edit the field. You basically link to another record. When you press that, it's going to create a new table. So I'm just going to cancel out, but basically you'd say "link to another record" and it's going to generate this. What's happening is you now have all of these URLs pushed over. And what's important is now you have all the keywords from those URLs. So linking to another record is going to create a new table. And when you open this table, it just works automatically.

**Nemanja Simic:** That's all you get?

**Matthew Alves-Hill:** Yeah, exactly. So once you link to another record from the URL column, it's going to create this new URLs view—I guess table. And this is what you're going to get. So now you have like each page and all the keywords that are related to it.

**Nemanja Simic:** Some of the URLs repeat. Loads repeating, right?

**Matthew Alves-Hill:** So while we have 18,000 records—keywords... Yeah, we don't have that many URLs. So what this view is doing is basically map all those keywords to the URLs.

**Nemanja Simic:** And we got what, like 700 or so here?

**Matthew Alves-Hill:** 728, yeah.

**Nemanja Simic:** And does that sound right? I don't know if you've done a site map for Airbyte yet or anything like that. I think they have like 2,000 something pages in total.

**Nemanja Simic:** But it makes sense for the data engineering directory and blog, you know, because I'm not going to update their docs—they have like docs pages and stuff, you know, glossary pages. I'm not going to refresh those. If they want to, we can, but I might as well start with something like 700 of them, where I know they do the blog. We could have probably added "Top ETL Tools" in there as well.

**Matthew Alves-Hill:** Yeah, so that's kind of interesting. This is kind of a side note, but we have the same with Bafi. They had a docs repository that was really popular with their user base, because obviously that's where they're spending a lot of time. And when we did a site audit on SEMrush for Bafi, a load of the issues were related to the docs pages—like 404s and broken links and all that. And I said the same thing at the time: is this stuff worth fixing? And Panzer made a really good point. He was like, a lot of customer retention and recommendation—like word-of-mouth stuff to other people in the field, like in Bafi's case, other developers. It's like, if the docs experience should be good. So I agree, like for SEO and the core of the service we're doing, yes, focus on the blog. But it is an interesting topic for a lot of these clients that have the docs repos—something we should think about more, spending time in those and not just optimizing for SEO, but optimizing the experience.

**Nemanja Simic:** I don't disagree with you. I just know in terms of us at GrowthX, we're trying to get results for Marcel to see that these refreshes work, and SEO is the lowest hanging fruit there. But I completely agree with you. The way I did my refresh analysis was through Google Analytics and Google Search Console—basically finding what pages have decreased in traffic, what has more traffic, not necessarily keyword-based. You know, for our workflows, going through by keyword makes more sense, and just finding the actual page itself. I also have like, I'd say, another six, seven hundred or so. So it's around that ballpark.

**Matthew Alves-Hill:** Yeah, okay. Well then, I mean, it's all kind of a mix of different tools. I was doing research earlier for Monograph, and I'm looking at their top ranking pages in Google's Search Console as opposed to just putting like "architecture" into SEMrush. It's like, it's good to source from multiple sites. Okay, cool. So basically once you do that link-to-another-record thing, you're going to get this page. This says "imported table" but it should say "keywords." It's just because I didn't map the name correctly.

**Nemanja Simic:** So that's fine. I would say like "keywords."

**Matthew Alves-Hill:** Okay. So then we have like all of the URLs that we're working with. And what are those three other columns you added on?

**Nemanja Simic:** I'll show you.

**Matthew Alves-Hill:** So first, now we have a database of potential pages. But now we need to figure out: which ones do we want to prioritize? And like Marcel was saying, we want to go for the ones that have the highest volume—essentially, like easy wins. So the first thing you do is you want to know how many keywords are on each page. I've obviously already created this, but basically this is how you would do it. So you would go in here, add a field, and select rollup. Rollup is like this little wheel thing. And we're rolling up this imported table. We're rolling up keyword difficulty, and here we want to find an average. So it's looking at the previous view and it's saying: this is the average difficulty for this page. Right. And again, you can start to see: okay, something up here might be difficult to rank for, but then when you start to see lower ones, you get where I'm going.

**Matthew Alves-Hill:** And then the final one is total volume. And what this is doing is mapping—it's another rollup mapping from search volume in the previous table. So we can see here the volume. It's taking it for each keyword, and basically in here it's taking 473 keywords, and it's basically giving us the volume for each one, adding it up, and there we get the total volume.

**Nemanja Simic:** And the thing is, if I'm ranking first, you know, this has 473 keywords, and I'm ranking first for most of them, why would we refresh it, you know what I mean?

**Matthew Alves-Hill:** Yeah, so the positioning wasn't in the initial gap. It's a good point. I guess, because Marcel said they all should be refreshed. But refreshing content that's already ranking well, I really don't know how to give you answers on that. I don't know what the best practice is. I get your point: why would you refresh it if it's already performing well? And I don't know if there's a more efficient way to do this other than checking page by page. But it's probably worth now taking the pages we have ranked here. What we've done is rank this by the total potential volume for this page, right? If we were top for all of these keywords, this is the potential volume. So I guess you'd probably just want to check these pages—the quality of them—and see, okay, well try and figure out if it's ranking well, how can it be improved? It might be worth asking Panzer about refreshes of pages that are already performing very well from an SEO standpoint.

**Matthew Alves-Hill:** So I think in the keyword gap, this would have been competitive pages, right? We would have been taking a load of competitors to Airbyte and we'd have this view. And then we'd be able to start creating assignments based on these competitive URLs, saying: okay, this one has super high potential. And you'd start building the gap analysis from that. But yeah, this is now, I think, the database that Marcel was talking about on the call. Here is your list of the big guys. And then you can, obviously, add a sort. You could sort by difficulty and then by volume or something like that to go after it however you want. But I think the right thing should be just going from the top 100 or 150.

**Nemanja Simic:** I'm just trying to figure out if I'm looking at some of these pages where they would show up. Now look at this. Keywords like "skewed data set." Airbyte is first for that, you know.

**Matthew Alves-Hill:** So this is the top page by that.

**Nemanja Simic:** And I'm looking at my refresh tool. For example, if you go to the keywords, the first one is "skewed data set," right? Position is number one. And when I Google it, it's number one when I actually check on Google. But when I was working on my refreshes, I could see this page—"skewed data set"—number one, had a decrease of 42%.

**Matthew Alves-Hill:** Yeah, so it's just like a non-competitive keyword, perhaps?

**Nemanja Simic:** Yeah. But it decreased, I'd say, by 42% in terms of in a year. I'll run this through and we'll see what happens.

**Matthew Alves-Hill:** Yeah, I mean, look, I think this is what he was talking about. Like, this is the way that he would approach it. But if it's all AI content, kind of garbage, we can elevate. So if it's already doing well, we can add internal links, strengthen the site, add a CTA, add a FAQ section. There's ways to beef it up.

**Nemanja Simic:** Yeah, okay, cool. I'll send him this Airtable as well and see what he thinks. Just to get his opinion and see if I'm on the right track. Because there's a lot of pages here, and some of them 100% should be refreshed. Like, I wish I could see the change in the actual traffic of the page over a period of time—like a year. I think that would make it a lot more clear in terms of which one we could touch up, you know?

**Matthew Alves-Hill:** Yeah, I mean, the rankings are also so variable. Like when I look for "skewed data" on SEMrush, I see everybody ranking. So that might be my location—there's various different things. But yeah, based on what he was explaining, the delta and all that kind of stuff, that's what this is, yeah?

**Nemanja Simic:** Yeah. All right, man, I won't keep you any longer. Have your night back. I really, really appreciate you showing me this. It's a much clearer explanation than I've heard. It's in HD for a change.

**Matthew Alves-Hill:** It's in HD for sure.

**Nemanja Simic:** But watching it makes perfect sense. And I know exactly where I was getting lost last time. You explained the reasoning really well as well.

**Matthew Alves-Hill:** And in future, if you want, I would say some other people might watch this recording. It's actually easiest to just go and look at the fields. I'll put this in the shared folder in the team space—the Airbyte refresh or wherever you end up putting it. It's really easy to just look at the fields and work out: okay, how are these generated? If you have access to an Airtable that's done this, basically any content OS that's done the keyword gap, the methods are just in the fields. You just go in and see: okay, this column was generated like this, and this is the formula here. So yeah.

**Matthew Alves-Hill:** All right, man.

**Nemanja Simic:** Really appreciate it. Good night. Do you want me to share this with George?

**Matthew Alves-Hill:** Yeah, you can drop in that meeting, please, in the Slack.

**Nemanja Simic:** We'll get the link in Fathom, yeah?

**Matthew Alves-Hill:** Yeah, I hope so. All right.

**Nemanja Simic:** Bye.

**Matthew Alves-Hill:** Bye.
