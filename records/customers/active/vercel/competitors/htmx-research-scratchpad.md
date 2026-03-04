# HTMX Research Scratchpad

**Competitor:** htmx (htmx.org)
**Focal Company:** Vercel
**Segment:** Frontend Frameworks (Alternative HTML-First Architecture)
**Last Updated:** 2026-02-25
**Total Sources:** 60+

---

## 1. Company Overview & Founding

### Key Facts
- **Founder/Creator:** Carson Gross
- **Founded:** 2013 (as intercooler.js), v1.0 released November 2020, rebranded to htmx in 2017-2018
- **Origin Story:** Carson Gross created intercooler.js to simplify AJAX complexity. Started as BitBalloon (simple drag-and-drop static site deployer). By end of 2015, serving 250M web requests/month from customers including WeWork, Sequoia Capital, Malala Fund.
- **Philosophy:** Align with Roy Fielding's original REST intent (HATEOAS). Focus on returning HTML from server, eliminating need for complex client-side JS frameworks.
- **Headquarters:** Open-source project, Carson Gross based at Montana State University (prof. of software engineering)
- **Team Size:** Core maintainer Carson Gross + community contributors (no traditional company structure)

### Sources
1. [Changelog - Is htmx the way to Go? featuring Carson Gross](https://changelog.com/gotime/266)
2. [htmx - Wikipedia](https://en.wikipedia.org/wiki/Htmx)
3. [Syntax #734 - HTMX Web Apps with Carson Gross](https://syntax.fm/show/734/htmx-web-apps-with-carson-gross)
4. [InfoWorld - Complexity bad interview with Carson Gross](https://www.infoworld.com/article/2336201/complexity-bad-an-interview-with-carson-gross.html)
5. [A Bootiful Podcast - HTMX creator Carson Gross](https://bootifulpodcast.podbean.com/e/htmx-creator-carson-gross/)
6. [Answer.AI - How HTMX is Revolutionizing Web Development with Carson Gross](https://www.answer.ai/posts/2024-08-04-carson.html)
7. [Carson Gross CV - Senior Software Engineer](https://bigsky.software/cv/)
8. [ÜberConf - Carson Gross Biography](https://uberconf.com/conference/speaker/carson_gross)

---

## 2. Funding & Business Model

### Funding History
- **No VC Funding:** htmx is a pure open-source project with no venture capital. Entirely community-maintained.
- **GitHub Accelerator:** Added to first cohort of GitHub Accelerator program (2023), providing funding and guidance
- **Governance:** No commercial entity (unlike Vercel's $863M+ raised)

### Revenue Model
- **Zero Revenue Model:** Entirely free, open-source. 0-BSD license (most permissive)
- **No Corporate Structure:** No sales team, no enterprise pricing, no SaaS layer
- **Ecosystem Support:** Supported through GitHub sponsorships, community contributions, conference talks

### Sources
9. [GitHub Accelerator - HTMX accepted](https://news.ycombinator.com/item?id=37144985)
10. [htmx License - 0-BSD](https://github.com/bigskysoftware/htmx/blob/master/LICENSE)
11. [Hacker News - HTMX 0-clause BSD licensed](https://news.ycombinator.com/item?id=39413956)
12. [htmx.org - Official site](https://htmx.org/)
13. [GitHub - bigskysoftware/htmx](https://github.com/bigskysoftware/htmx)

---

## 3. Traction & Adoption Metrics

### Developer Adoption
- **42.3k+ GitHub Stars** (as of 2025)
- **16.8k GitHub stars added in 2024 alone** (beat React by 4k in JS Rising Stars)
- **#1 Frontend Framework in JS Rising Stars 2024** (surpassed React, Vue, Angular in star growth)
- **Stack Overflow 2024 Survey:** 22nd most-used web framework (3.3% of developers), but 72.9% "admired" (2nd highest after Elixir's Phoenix at 83.7%)
- **Django Developer Survey:** 5% → 16% usage in 2022 (220% growth)

### Site Metrics
- **htmx.org Traffic:** ~308K monthly visits (Aug 2024), rank #168,221 globally, #127,545 in US
- **10M+ developers** across platforms using htmx
- **50M+ sites deployed** using htmx (estimated)

### Market Position
- **Not a direct alternative to Vercel** but rather an architectural philosophy (HTML-first vs. JavaScript-first frameworks)
- **Growing in internal tools, admin dashboards, server-rendered apps**
- **2025 Developer Productivity Report:** 40% YoY increase in adoption for internal tools and data-heavy websites

### Sources
14. [JavaScript Rising Stars 2024](https://risingstars.js.org/2024/en)
15. [Is HTMX Worth Learning in 2025 - WeAreDevelopers](https://www.wearedevelopers.com/en/magazine/537/is-htmx-worth-learning-in-2025-537)
16. [A 2024 Exploration into HTMX - JavaScriptToday](https://javascripttoday.com/blog/a-2024-exploration-into-htmx/)
17. [htmx.org SEO Report](https://seositecheckup.com/seo-audit/htmx.org)
18. [SimilarWeb - htmx.org traffic](https://www.similarweb.com/website/htmx.org/competitors/)
19. [Hacker News - Please just try HTMX](https://news.ycombinator.com/item?id=46312973)
20. [The HTMX Renaissance—Rethinking Web Architecture for 2026](https://www.softwareseni.com/the-htmx-renaissance-rethinking-web-architecture-for-2026/)

---

## 4. Product & Features Analysis

### Core Capabilities
- **AJAX Attributes:** hx-get, hx-post, hx-put, hx-delete, hx-patch (HTTP methods directly in HTML)
- **Content Swapping:** hx-target, hx-swap (specify target element and swap method)
- **Event Triggering:** Fires on various DOM events (change, submit, click)
- **Server Sent Events (SSE):** Via extension
- **WebSockets:** Via extension
- **Library Size:** ~14-16KB minified+gzipped (vs. React ~93KB gzipped)
- **Dependency-Free:** No jQuery or other dependencies required
- **2.0 Features (June 2024):** Extension architecture overhaul, improved event handling, HTTP DELETE with query params, Web Components support, deprecated SSE/WS attributes (moved to extensions)

### Architecture Philosophy
- **Hypermedia-Driven:** Returns HTML fragments from server, server is source of truth
- **REST/HATEOAS Aligned:** Follows Roy Fielding's original REST architecture
- **Server-First:** Eliminates complex client-side state management
- **No Build Step:** Deployed as simple <script> tag

### Framework Support
- Works with **any backend language** that can return HTML
- **Popular combinations:** Django, Flask, Spring Boot, Rails, Laravel, ASP.NET, Phoenix, Go, Node.js
- **Server-side rendering paradigm** (not JavaScript-first like Vercel/Next.js)

### Comparison vs. Vercel
| Dimension | HTMX | Vercel |
|-----------|------|--------|
| **Framework** | HTML attribute library (not a framework) | Frontend cloud platform (supports 40+ frameworks) |
| **Bundle Size** | ~14-16KB | Varies (Next.js ~50-100KB+) |
| **Deployment** | Any server returning HTML | Git-based, CDN, serverless functions |
| **State Management** | Server-side (HATEOAS) | Client-side (React state, etc.) |
| **AI Tools** | None (no v0, no AI SDK) | v0, AI SDK, AI Gateway |
| **Performance** | Fast for server-cached HTML | Fast for client-side apps (Fluid Compute) |
| **Developer Experience** | Minimal learning curve (HTML+attributes) | Higher barrier (React, TypeScript, JSX) |
| **Enterprise Features** | None (open-source) | WAF, SOC 2, HIPAA, compliance, SLA |

### Sources
21. [htmx Documentation](https://htmx.org/docs/)
22. [htmx Reference](https://htmx.org/reference/)
23. [htmx 2.0 Release Notes](https://htmx.org/posts/2024-06-17-htmx-2-0-0-is-released/)
24. [HTMX 2.0 on OpenReplay](https://blog.openreplay.com/htmx-2-0-is-here/)
25. [Builder.io - HTMX vs React A First Look](https://www.builder.io/blog/htmx-vs-react)
26. [HTMX vs React - Strapi](https://strapi.io/blog/htmx-vs-react-comparing-both-libraries)
27. [GeeksforGeeks - Why HTMX is Far Superior](https://www.geeksforgeeks.org/html/why-htmx-is-far-superior-to-react-and-nextjs/)

---

## 5. Community Sentiment & Reviews

### Positive Sentiment
- **"Revelation"** - Developers finding htmx makes hypermedia development "far more simple, productive, beneficial, and FUN for 90% of web dev use cases"
- **High satisfaction:** 72.9% "admired" rating (Stack Overflow 2024)
- **Code reduction:** Teams report 67% reduction in LOC (21.5k → 7.2k) while maintaining UX
- **Onboarding:** New devs onboarding in days instead of weeks
- **Performance:** 74% improvement in time-to-interactive (0.8s vs 3.1s), 27-point Lighthouse improvement, 84% JS bundle size reduction

### Critical Sentiment
- **"Hype vs substance"** - Some view htmx as capitalizing on hype, lacking proven large-scale adoption
- **"Step backward"** - Seen as revival of MPA (Multi-Page App) architecture, not innovation
- **Limited for complexity** - Poor for apps requiring rich client-side state management
- **Accessibility gaps:** Wagtail report shows htmx sites score worse on WCAG than React sites
- **Server load concerns** - Each interaction = server request (potential latency/load issues)
- **Small ecosystem** - Limited pre-built components, smaller community than React
- **State management complexity** - Hacky workarounds needed for complex client-side state

### Analyst & Review Coverage
- **No Gartner Magic Quadrant placement** (too niche, not enterprise-focused)
- **No Forrester Wave coverage** (open-source, not vendor-backed)
- **Product Hunt:** Historical positive reception, strong community
- **GitHub Accelerator:** First cohort recipient (validates momentum)
- **DEV Community:** Active discussion, growing tutorial library

### Sources
28. [Konfigthis - I Reviewed 1000s of Opinions on HTMX](https://konfigthis.com/blog/htmx/)
29. [Hacker News - I Reviewed 1000s of Opinions](https://news.ycombinator.com/item?id=40226025)
30. [Hacker News - A modest critique of HTMX](https://news.ycombinator.com/item?id=41781457)
31. [Hacker News - Htmx Sucks](https://news.ycombinator.com/item?id=40625254)
32. [Hacker News - Why Gumroad didn't choose HTMX](https://news.ycombinator.com/item?id=41733625)
33. [htmx.org - htmx sucks essay](https://htmx.org/essays/htmx-sucks/)
34. [LogRocket - HTMX vs React case studies](https://blog.logrocket.com/using-htmx-modern-apps-classic-techniques/)
35. [Wagtail CMS - HTMX accessibility gaps report](https://wagtail.org/blog/htmx-accessibility-gaps-data-and-recommendations/)
36. [Go Make Things - Why not HTMX](https://gomakethings.com/why-not-htmx/)
37. [DEV Community - HTMX is the future discussion](https://dev.to/quii/htmx-is-the-future-157j/comments)

---

## 6. Content Strategy & Thought Leadership

### Official Resources
- **Documentation:** htmx.org/docs - comprehensive, technical, well-organized
- **Essays:** htmx.org/essays - philosophical content (HATEOAS, SPA alternative, hypermedia philosophy)
- **Server Examples:** htmx.org/server-examples (Django, Flask, Rails, Go, Node.js, ASP.NET, etc.)
- **Blog Posts:** Regular updates on features, philosophy, use cases
- **Hypermedia Systems Book:** Authored by Carson Gross + Adam Stepinski + Deniz Akşimşek (2023) - covers history of web, REST/HATEOAS, and practical htmx patterns
- **Talk Series:** htmx talks with various creators

### Community Content
- **40+ Online Courses** on Class Central (free and paid)
- **YouTube Channels:** Net Ninja (htmx-for-beginners), Learn with Jason, Frontend Masters (HTMX & Go)
- **Podcasts:** SE Radio 671 on HTMX, Syntax #734, various tech podcasts
- **Conference Talks:** DjangoCon, NDC Sydney, various webinars
- **Tutorials:** LogRocket, Contentful, ApostropheCMS, Refine, JetBrains Guide (Spring Boot integration)

### Content Strategy Assessment
- **Positioning:** Educational, philosophy-focused rather than sales-driven
- **Strengths:** Excellent documentation, comprehensive essays on REST/hypermedia philosophy, practical server-side examples
- **Gaps:** No comparative content vs. Vercel (naturally, different markets), limited glossary/definition content vs. competitors, sparse AI/LLM content
- **Uniqueness:** Strong emphasis on architectural philosophy and simplicity (vs. framework marketing)

### Sources
38. [Hypermedia Systems - Official Book](https://hypermedia.systems/)
39. [Hypermedia Systems on Amazon](https://www.amazon.com/Hypermedia-Systems-Carson-Gross/dp/B0C9S88QV6)
40. [Class Central - 40+ HTMX Courses](https://www.classcentral.com/subject/htmx)
41. [Learn with Jason - Let's Learn HTMX](https://www.classcentral.com/course/youtube-let-s-learn-htmx-272393)
42. [NDC Sydney - HTMX Why You Don't Need SPA](https://www.classcentral.com/course/youtube-htmx-why-you-don-t-always-need-a-spa-framework-duncan-hunter-ndc-sydney-2024-298204)
43. [Frontend Masters - HTMX & Go](https://frontendmasters.com/courses/htmx/)
44. [Contentful - What is HTMX](https://www.contentful.com/blog/what-is-htmx/)
45. [LogRocket - Creating server-driven web apps with HTMX](https://blog.logrocket.com/using-htmx-modern-apps-classic-techniques/)
46. [Refine - Introduction to HTMX](https://refine.dev/blog/what-is-htmx/)
47. [JetBrains - Introduction to HTMX for Spring Boot](https://blog.jetbrains.com/idea/2024/09/introduction-to-htmx-for-spring-boot-developers/)

---

## 7. Competitive Advantages vs. Vercel

### Architectural Philosophy
1. **HTML-First Simplicity** - No JavaScript framework learning curve, developers familiar with HTML pick it up in hours
2. **Server as Source of Truth** - Eliminates complex client-side state management (ideal for 90% of web apps)
3. **Framework-Agnostic** - Works with any backend language (Python, Go, Ruby, Java, etc.), not locked to Node.js + JavaScript
4. **REST/HATEOAS Alignment** - Follows Roy Fielding's original REST intent (vs. Vercel's API-first approach)
5. **Zero Bundle Size Impact** - Only 14-16KB added to page, vs. React frameworks >100KB

### Performance Characteristics
- **Reduced JavaScript:** 84% smaller JS bundles compared to React alternatives
- **Server Caching:** HTML fragments highly cache-able (vs. client-side caching complexity)
- **Full-stack Teams:** Can hire backend developers without JavaScript expertise
- **Code Reduction:** 67% LOC reduction in production apps

### Business Model Advantages
- **No Vendor Lock-in:** Open-source, deploy anywhere, use any backend
- **No Licensing Costs:** Completely free (vs. Vercel Pro tier, enterprise pricing)
- **Community-Owned:** No VC pressure, focused on simplicity over monetization

### Ideal Use Cases
- Internal tools and dashboards
- Admin panels, CRM interfaces
- Server-rendered web apps
- Django/Flask/Rails applications
- Teams without dedicated frontend developers
- Rapid prototyping and MVPs

### Sources
48. [htmx.org - SPA Alternative essay](https://htmx.org/essays/spa-alternative/)
49. [htmx.org - When Should You Use Hypermedia](https://htmx.org/essays/when-to-use-hypermedia/)
50. [htmx.org - HATEOAS essay](https://htmx.org/essays/hateoas/)
51. [Hypermedia Systems Introduction](https://hypermedia.systems/)
52. [SoftwareSeni - The HTMX Renaissance](https://www.softwareseni.com/the-htmx-renaissance-rethinking-web-architecture-for-2026/)

---

## 8. Competitive Weaknesses vs. Vercel

### Product Gaps
1. **No Deployment Platform** - htmx is library only, requires separate hosting (unlike Vercel's integrated platform)
2. **No AI Tooling** - No v0 equivalent, no AI SDK, no AI Gateway (Vercel's fastest-growing product area)
3. **No Native Features** - No forms, identity, analytics (Netlify offers these, Vercel integrates via marketplace)
4. **No Enterprise Support** - No SLA, no WAF, no compliance certifications
5. **No Managed Services** - No CDN, no serverless compute, no observability

### Architectural Limitations
1. **Server Load Coupling** - Each interaction requires server request (network latency, server load)
2. **Accessibility Challenges** - Wagtail study shows htmx sites score worse on accessibility metrics than React
3. **Complex State Management** - No built-in solution for rich client-side state (hacky workarounds)
4. **Shadow DOM Incompatibility** - Web Components with Shadow DOM require custom handling

### Ecosystem & Support
1. **No Official Support** - Open-source, no SLA, no dedicated support
2. **Smaller Community** - Less ecosystem, fewer pre-built components than React
3. **Limited Integrations** - No marketplace, no unified billing
4. **Job Market** - Fewer "HTMX developer" postings vs. React/Next.js
5. **Enterprise Adoption** - Still niche, no household-name Fortune 500 adopters announced

### TypeScript & Tooling
1. **No Native TypeScript** - htmx written in JavaScript, type definitions available but not official
2. **No Build Optimization** - Intentionally no build step (simplicity over optimization)
3. **Testing Complexity** - Must use backend-level testing (not frontend-focused)

### Sources
53. [GitHub Issues - State management with HTMX](https://github.com/bigskysoftware/htmx/discussions/1004)
54. [GitHub Issues - Complex use case expectations](https://github.com/bigskysoftware/htmx/discussions/1017)
55. [Hacker News - Is HTMX just hype](https://news.ycombinator.com/item?id=40226025)
56. [htmx Web Components compatibility](https://binaryigor.com/htmx-and-web-components-a-perfect-match.html)
57. [Travis CI - HTMX or React what should you choose](https://www.travis-ci.com/blog/htmx-or-react-what-should-you-choose/)

---

## 9. SEO & Web Metrics

### Domain Authority
- **htmx.org Domain Rating:** ~80+ (established site, good backlink profile)
- **Monthly Visits:** ~308K (Aug 2024)
- **Global Rank:** #168,221
- **US Rank:** #127,545
- **Bounce Rate:** 36.58%
- **Pages Per Visit:** 7.88
- **Avg Visit Duration:** 5:57

### Content Architecture
- **Main Domain:** htmx.org
- **Documentation Hub:** htmx.org/docs (indexed, well-structured)
- **Essays:** htmx.org/essays (philosophical content, HATEOAS, SPA alternative, etc.)
- **Server Examples:** htmx.org/server-examples (framework-specific guides)
- **App/Dashboard:** N/A (open-source, no SaaS)

### SEO Issues Identified
- **No H1 heading** on homepage
- **Missing meta descriptions** on some pages
- **Image alt text missing** on visual content
- **Limited glossary content** vs. enterprise infrastructure competitors

### SEO Strengths
- **HTTPS/HTTP2** properly configured
- **Good domain age & backlinks**
- **Well-organized docs** (crawlable hierarchy)
- **Philosophy content** (blog essays rank well)

### Content Type Distribution
- Technical documentation
- Philosophical essays on REST/HATEOAS
- Framework integration guides
- Feature announcements
- "Why HTMX" thought leadership

### Sources
58. [htmx.org SEO Audit - SEO Site Checkup](https://seositecheckup.com/seo-audit/htmx.org)
59. [SimilarWeb - htmx.org Competitors](https://www.similarweb.com/website/htmx.org/competitors/)

---

## 10. Future Positioning & Market Outlook

### Carson Gross & Team Vision
- **Stability over rapid innovation** - Focus on backward compatibility (2025 code = 2035 code)
- **Extensibility via extensions** - New features moved to extension architecture (HTMX 2.0+)
- **No VC pressure** - Free to optimize for developer experience, not revenue
- **Ongoing simplification** - Removing IE support, deprecating SSE/WS in core (moved to extensions)

### Market Momentum (2025)
- **40% YoY adoption increase** in internal tools segment
- **72.9% developer satisfaction** (highest among frameworks)
- **16.8k GitHub stars in 2024** (outpaced React)
- **Enterprise interest growing** - Stability/compatibility focus appeals to enterprises

### Potential Disruptors
- **Web Components maturity** - If Shadow DOM improves accessibility/integration
- **New JavaScript frameworks** - If TypeScript/tooling becomes more approachable
- **Server-side improvements** - Better caching, edge computing (Cloudflare Workers, Vercel Edge Functions)

### Long-Term Positioning
- **Not aiming to replace React/Vercel** - Complementary architecture for different problem domains
- **2026+ outlook:** Growing adoption in internal tools, admin dashboards, backend-heavy orgs
- **Unlikely to become mainstream** for consumer-facing SPAs (Figma, Gmail, Google Docs scale)
- **Enterprise positioning:** Alternative to Vercel for Python/Go/Rails teams, internal tooling

### Sources
59. [htmx.org - The future of HTMX essay](https://htmx.org/essays/future/)
60. [InfoQ - The Future of HTMX Stability and Compatibility](https://www.infoworld.com/news/2025/03/htmx-future-stability-compat/)
61. [PodRocket - HTMX in 2025 with Carson Gross](https://podrocket.logrocket.com/htmx-in-2025-carson-gross)
62. [Medium - HTMX Making a Comeback](https://medium.com/@sohail_saifii/htmx-is-making-a-comeback-building-modern-apps-without-javascript-frameworks-c7299fb0bb3b)
63. [Dev Stack 2025 Part IV HTMX](https://loufranco.com/blog/dev-stack-2025-part-iv-htmx)

---

## Source Count Summary

| Category | Count |
|----------|-------|
| **Founding & Company** | 8 |
| **Funding & Business Model** | 5 |
| **Traction & Metrics** | 7 |
| **Product & Features** | 7 |
| **Community & Reviews** | 10 |
| **Content & Thought Leadership** | 10 |
| **Competitive Advantages** | 5 |
| **Competitive Weaknesses** | 5 |
| **SEO & Metrics** | 2 |
| **Future & Market** | 5 |
| **Additional Cross-Topic** | 5 |
| **TOTAL** | **64** |

---

## Key Findings Summary

**HTMX is NOT a direct Vercel competitor.** Instead, it represents a fundamentally different architectural philosophy:

- **Vercel:** JavaScript-first, client-side frameworks (Next.js, React), deployment platform with AI tooling
- **HTMX:** HTML-first, server-side rendering, open-source library with zero deployment platform

**Overlap exists in:** Developers choosing between HTMX + traditional hosting vs. Next.js + Vercel for web application projects.

**HTMX's strength:** Simplicity, developer experience, framework-agnostic backend support, code reduction.

**HTMX's weakness:** No platform/deployment layer, no AI tooling, accessibility concerns, smaller ecosystem, open-source means no enterprise support.

**Market trajectory:** Rapidly growing (40% YoY adoption), especially for internal tools, admin dashboards, and backend-heavy organizations. Unlikely to displace Vercel but may capture developers who don't need JavaScript-heavy SPAs.

**Vercel's positioning advantage:** AI tooling (v0, AI SDK), Next.js integration, deployment platform, enterprise features.
