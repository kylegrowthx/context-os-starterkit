# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-29
time: 18:00 UTC
duration: 35 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong, Sydney Go, Liz Kushnereit, Edin Abazi, Colin Lateano, Vic Plummer, Zach Plata
fathom_recording_id: 97768135
fathom_url: https://fathom.video/calls/455829244
share_url: https://fathom.video/share/4xV3MWAfcBUKaE1E-FNX9yN12pMLdt4j
source: fathom
enriched_on: 2026-03-02 09:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on the deliverables for Webflow Code Components: a React component file plus a critical `.webflow.tsx` definition file that exposes designer-controlled props to non-technical users. Colin pressed for a proposal by EOD Oct 30 outlining expanded scope for Q4/Q1 budget, covering both Code Components and a new "Remixable Web Apps" program (functional apps for Webflow Cloud that users can customize or remix). Jason committed to drafting the capacity proposal by end of day, splitting engineering and content workstreams.

---

## Context

Webflow is GrowthX's largest strategic client and engineering partner. Webflow is building out a Code Components system that lets developers create reusable React components for the Webflow designer, exposing a curated set of props to non-technical users. GrowthX has been tasked with developing a library of components (starting with ShadCN equivalencies) that work within Webflow's Shadow DOM security constraints. This is part of a broader strategic push: Webflow also plans to launch a "Remixable Web Apps" program on December 1st—one new app per day to showcase what's possible on Webflow Cloud—and is asking GrowthX to support that effort starting in January. The meeting focused on clarifying scope before budget decisions were finalized for Q4 and Q1 (Webflow's fiscal quarters start one month late, so Q1 begins in February).

---

## Relevance

- **To GrowthX Delivery:** Code components require specific workarounds for Webflow's Shadow DOM security model — CSS is isolated, context is not shared across components, and libraries like ShadCN don't port one-to-one. GrowthX needs to become fluent in Webpack overrides, Webflow-specific build constraints, and the `.webflow.tsx` definition file pattern. A reusable sample-page template can be created once and deployed across all components, reducing per-component overhead.

- **To GrowthX Engineering Capacity:** Webflow is requesting an expanded engineering scope for Q4/Q1, distinct from typical content-driven delivery. Jason flagged that Webflow's work is "more engineering and product" than editorial, requiring dedicated full-stack engineers. A formal capacity proposal with engineering and content workstreams is due EOD Oct 30 so Colin can secure Q4/Q1 budget.

- **To GrowthX Business Development:** Webflow's "Remixable Web Apps" program (launching Dec 1 with one app per day) is an evergreen expansion opportunity similar to CheckThat. If GrowthX can prove it can generate components at scale, Webflow may expand scope further. Colin emphasized the need to prove the core capability (building components that work in Webflow) before tackling merchandising or distribution logistics.

- **To Strategic Positioning:** Figma Make and Replit were cited as inspiration for app-library models. This positions GrowthX as not just a content vendor but a product services partner capable of executing engineering-heavy initiatives at Webflow's scale.

---

## Overview

- **Deliverable Defined:** A complete code component is a React file plus a `.webflow.tsx` definition file. The definition file is critical, as it exposes specific props to the Webflow designer, enabling non-technical users to customize the component.
- **Key Constraint:** Webflow's security model renders components in a Shadow DOM, isolating their CSS and preventing them from sharing context with the main page. This requires workarounds for common patterns and makes direct porting of libraries like ShadCN non-trivial.
- **Distribution Strategy:** Components will be hosted in a public GitHub repo for CLI installation. A WYSIWYG marketplace is not feasible due to security risks (live code execution on the canvas), making developer-focused tools like `npm` commands the only option.
- **Scope Expansion:** Webflow needs a proposal from GrowthX by EOD Oct 30 for an expanded engineering scope, covering Code Components and a new "Remixable Web Apps" program, to secure Q4/Q1 budget.

---

## Key Topics

### Defining a "Complete" Code Component

  - The core deliverable is a React component that renders correctly in the Webflow designer.
  - A complete component requires two main files:
    1.  **React Component File:** Standard React/TypeScript code.
    2.  **`.webflow.tsx` Definition File:** This is the critical piece that exposes specific props to the Webflow designer.
          - It imports the React component and Webflow-specific types (`DeclaredComponent`, `WebflowProps`).
          - It uses `declareComponent` to define the component's name, description, and the subset of props a designer can control.
  - **Development Tools:** Storybook is a useful but optional local dev tool for testing component states.

### Webflow Code Component Constraints

  - Webflow's security model has key constraints that prevent direct porting of standard React libraries:
      - **Shadow DOM:** Components render in an isolated Shadow DOM, preventing CSS conflicts but also isolating their styles and context from the main page.
      - **No Shared Context:** Components cannot communicate with each other or the main page. Webflow provides workarounds (e.g., for a chart and input component to interact).
      - **Webpack-based:** The build process uses Webpack, which may require custom overrides for some libraries.
  - **Resources:** Webflow provided docs on `Component Architecture`, `Installation`, and `Frameworks & Libraries` to explain these constraints and their solutions.

### Distribution & Developer Experience (DX)

  - **Distribution Model:** Components will be hosted in a public GitHub repo. Users will install them via the Webflow CLI using `npm` commands.
  - **No WYSIWYG Marketplace:** A drag-and-drop interface is not feasible due to security risks. Components execute live on the Webflow canvas, making direct imports a potential exfiltration risk.
  - **Future DX:** A more advanced CLI experience (e.g., an `init` command, component selection menu) is a long-term goal.

### Scope Expansion & Budgeting

  - **Request:** Webflow needs a proposal by EOD Oct 30 for an expanded engineering scope to secure Q4/Q1 budget.
  - **New Program: "Remixable Web Apps"**
      - **Goal:** Build a library of functional web apps (not just UI components) to help users solve problems and get started with Webflow Cloud.
      - **Model:** Inspired by Figma Make and Replit.
      - **Timeline:** An aggressive marketing push starts Dec 1 (one app/day), which GrowthX may support starting in January.
  - **Proposal Structure:** The proposal should outline capacity for both the Code Component and Web App programs, potentially splitting into "engineering" and "content" workstreams.

---

## Action Items

**Vic Plummer (Webflow)**
- Send GrowthX docs links: Component Architecture, Installation, Webpack overrides
- Send GrowthX docs JSON schema for examples page

**Jason Gong (GrowthX)**
- Schedule follow-up w/ Colin re: CLI install/DX; invite Edin
- Draft Q4/Q1 engineering/content capacity proposal for Colin; send to FP&A

**Colin Lateano (Webflow)**
- Research app-library examples (e.g., Replit); share w/ Jason

---

## Transcript
**Jason Gong:** This meeting is being recorded.

**Colin Lateano:** It asks for permissions to modify your system settings, and I have no idea why a camera would ever need that.

**Colin Lateano:** So I have to keep denying it.

**Colin Lateano:** But it gives me cool features like this.

**Jason Gong:** I think we have something like this in the office that's from maybe Dell or Logitech that looks the same.

**Jason Gong:** This is really cool.

**Jason Gong:** Is it a quality thing or is it supposed to just like quality?

**Colin Lateano:** It's a quality thing, and I was trying to do hand gestures.

**Colin Lateano:** Now I look like a loser.

**Colin Lateano:** There are hand gestures you're able to do to make it do things, like follow you and zoom in.

**Colin Lateano:** But I guess I'm not doing that today.

**Jason Gong:** I know you have a hidden Twitch account we just haven't found yet.

**Colin Lateano:** I'll be honest with you. I have wanted to be on camera a lot. I just can't make the time. That's the biggest problem.

**Colin Lateano:** I would love to be a streamer.

**Jason Gong:** Cool.

**Jason Gong:** Today, just want to talk about code components.

**Jason Gong:** Sydney is out this week.

**Jason Gong:** So I know a lot of that work is still happening.

**Jason Gong:** can do a little update there.

**Jason Gong:** But yeah, I mean, the integration stuff is mostly stable and not thinking there.

**Jason Gong:** And then we're really trying to get that pipeline for the integration use case guides out this week. We're targeting three to five a week at the moment. On components, we have a resident full stack web dev expert on the team. We have some questions, mainly around what is the success criteria for delivery and what is in scope?

**Jason Gong:** I think we both went through the getting started guide. I chose the Astro site, though Edin was telling me maybe I should choose the Next.js site instead. But I did that and I created a component that seems to be working. The scope, at least to get this on the page, is styling, design, functionality, and HTML structure—that seems to be the bare minimum. And I know for stuff like this, you need the .webflow file. I think Edin flagged a few things as well. So I guess, is that something you could talk more about?

**Colin Lateano:** What exactly is a complete component? A complete component can be ambiguous. Also, Vivian, this will be mainly on code components, so if you want to balance, feel free. But the main focus of code components is getting started with our code component system. I see your notes—there's a range of questions around why use Astro for React snippets. So we want to create a variety of useful components that our customers may want to add to their sites.

**Colin Lateano:** From that point of view, some will be just front-end systems, some will have server involvement. But the main output is React code that can be placed in Webflow's code component element on a Webflow site. That code can render in the designer, allowing a user to insert this custom code as a component. The novelty here is that we have some limitations of code components. I think Zach shared a little bit of this—our code components are not exactly pure, perfect React. Otherwise, we would just use ShadCN as the answer for all the components we wanted to offer. Because of these nuances, the ask is to take the limitations of Webflow's code component system and make sure we can generate a component library like ShadCN where all of them can run in Webflow's code component system. Eventually, this project would evolve to have web app-related React components that tie in with what you're hosting on cloud. But the first few we're hoping to prove out are going to be like ShadCN equivalencies.

**Colin Lateano:** Are we all familiar with shadcn or other major libraries for components?

**Edin Abazi:** Yep.

**Colin Lateano:** Okay.

**Colin Lateano:** So, the best

**Colin Lateano:** The big deliverable execution is, can this actually play on Webflow code component?

**Colin Lateano:** So, if you have a Webflow account, please don't do this on the brand account that we're sharing for integrations.

**Jason Gong:** Yeah, no, we did that.

**Jason Gong:** We have our separate account.

**Colin Lateano:** So if you can open the code component part of this and insert the code you generated, that's an accomplishment. That's the win. And part of this is documenting any nuances—if the code becomes complex, if there's a novel approach to styling or class handling.

**Vic Plummer:** Open the book, the book icon. Yeah, there.

**Jason Gong:** I think these are just our regular components, not sure there's any cloud component. I didn't get that far because I think the piece that I'm missing to bring it there is the Webflow TypeScript file.

**Vic Plummer:** Sorry, I thought you were driving and trying to explain it.

**Jason Gong:** Oh no, this is my screen. But we don't need to make that link work with this. Edin, you should clarify, because I think I just need to poke around more to fully understand what we need to deliver. Are you able to show what a complete code component looks like—what files are there?

**Colin Lateano:** Vic, do you have an active site with a coconut right now?

**Vic Plummer:** Yeah, totally.

**Vic Plummer:** I can share that.

**Vic Plummer:** My audio went out for a second, so I was driving blind.

**Vic Plummer:** Let me jump into...

**Vic Plummer:** Okay.

**Vic Plummer:** Where are we at?

**Vic Plummer:** So, in Webflow, we have some components, like code components, that come in as with props.

**Vic Plummer:** Let's see.

**Vic Plummer:** I might not be on the show.

**Vic Plummer:** Oh.

**Zach Plata:** We've got our site ready.

**Zach Plata:** Vic, if you...

**Vic Plummer:** Thank you.

**Vic Plummer:** They come in over here. If you want to share with them, Doc—because I just have pretty nasty ones—but we're just trying different things out. The main thing is they are loaded in a shadow DOM. So when you look at the page or the preview, you'll see a shadow DOM, but what users can do is we define different properties. Right now, that's just a pretty basic one with no styling. Zach, if you have one with styling already up, that would be better to show.

**Vic Plummer:** Let me look at our examples. So let's say we have ShadCN components. These are different projects within one repo, but consider this a root repo. You have a components folder, and each folder has a definition file for Webflow. You've got the component as it normally would be, and then you have this `alert.webflow.tsx` file. This is the definition file. You import styles here, you import the components as well as these data types. You import the props for Webflow—Webflow has specific props—as well as the `declareComponent` method. Down here you declare your component `Webflow alert`, give it a name and a description, and that is what shows up in Webflow. Then you define the props that would be shown in Webflow for somebody to manage themselves. Not all props that are defined in the component need to be here, but the ones you'd want someone to manage in Webflow, you'd define here.

**Colin Lateano:** I saw that component you just showed had just two.

**Jason Gong:** That Webflow file is the part where you define what the levers are—how users interact with it.

**Vic Plummer:** And in this repo, there's a bunch of different components that are defined.

**Vic Plummer:** Yeah.

**Vic Plummer:** And then some of them were a little bit more advanced.

**Jason Gong:** What was that story file?

**Vic Plummer:** Storybook. So we were using Storybook to run these locally. It's just a way to look at your components and mess with the props. It gives you a better environment to mess with your components instead of just running it on your React app. You can see different states, control the different states. So you can choose the variant versus having to specifically write that on your app. It's just a developer utility. Storybook is nice, but it's not necessary at all. If it causes more headache than it's worth, it's not necessary.

**Jason Gong:** I think I understand what a component is.

**Jason Gong:** I think I remember reading something in the docs about, like, what it takes to actually, like, deploy it and have it show up in the Webflow designer.

**Vic Plummer:** I think the most important part that Colin was saying about, like, why they're not one-to-one is, okay, here.

**Vic Plummer:** So the component architecture, I think, is the most important part to read to understand, like, how these things render in Webflow.

**Vic Plummer:** So I'll throw that in the chat.

**Vic Plummer:** But so it's encapsulated in the shadow DOM, and that's where the CSS that you import, the component itself, all lives.

**Vic Plummer:** And also, it doesn't hold context, so we can't talk to other things on the page.

**Vic Plummer:** And so some libraries that people might use don't work as well.

**Vic Plummer:** And I know Zach had some experience with this, but so we offer some alternatives to communicate or to do things, like, if you had...

**Vic Plummer:** A chart component and then maybe an input component and they weren't all together, how to make them talk to each other so that they could react like you would expect them to or work like you would expect them to.

**Vic Plummer:** And then in this installation section here, there's a frameworks and library section.

**Vic Plummer:** We've created some specific plugins specifically for things we know people are going to use.

**Vic Plummer:** So Tailwind, Emotion, as well as Material and ShadCN. We have some things for path aliases as well as some preprocessors that you can use.

**Vic Plummer:** So I think these two together will give you an understanding of limitations and then the workarounds that you might need to do.

**Vic Plummer:** Everything's built in Webpack, so that's also something to note. You might have to do some Webpack overrides. I'll send that over. But you can't just build a static component and convert it one-to-one into Webflow. These are some of the things you need to consider. So I'd say these three docs are the most important ones.

**Jason Gong:** to Then pieces they've we've

**Jason Gong:** I think that makes sense.

**Jason Gong:** So I think I understand, like, the creation of the component, importing it, some of these dependencies.

**Jason Gong:** As far as, like, okay, let's say we make, like, 10 of them, what the next step would be after that?

**Jason Gong:** Like, where would they live?

**Vic Plummer:** So I think at this current time, we have this little examples page here where we're hosting all of our examples.

**Vic Plummer:** So we have, like, a little GIF, and then we have a live example page.

**Vic Plummer:** So it's a web page that shows on Webflow.

**Vic Plummer:** And I think just so people can see, hey, we really mean that React is on Webflow versus people being like, oh, well, that could just be anywhere.

**Vic Plummer:** And then we also have a link to the repo with some information here.

**Vic Plummer:** So this is all managed in our docs through, like, a JSON, like, schema.

**Vic Plummer:** And I'm happy to send that over.

**Vic Plummer:** So if you wanted to do this, but if you wanted to take a step further and make more of a marketplace.

**Vic Plummer:** Something like that.

**Vic Plummer:** I think that would be a different conversation where it lives.

**Colin Lateano:** This is just where it is right now.

**Colin Lateano:** For now, that's the right conversation to have, though.

**Colin Lateano:** Our current schema for our dev docs wouldn't work at the scale we're asking GrowthX to create components. We'd be going pages deep. So we definitely want a folder or project within Webflow examples of all the code components available for external users. We'd create a visual library in our docs or marketplace—not sure where yet—but that's not ready. However, that shouldn't stop velocity on examples. If we have a ton of examples, we'd use our existing example set or create a new way to visualize and interact with each component before viewing code.

**Jason Gong:** How it shows up probably matters quite a bit. The component itself is kind of like these two files, maybe with dependencies. But the way you're showing it now, you almost need a whole site where the component lives. So we're generating quite a lot more. If we do 100 components, would each one have its own overhead and its own little site to render it live and show it? How would you imagine that looks?

**Colin Lateano:** Some of that sounds duplicative. There are two questions. One: programmatically, how do you enact this seamlessly with no humans in the middle? We'd need APIs available to run imports on a site so we can sample and display every component. But the expectation was just the component files needed for someone to import via CLI. If they're not familiar, they'd do an import of the file name and it would come in. We don't need all the example folders because they're end-to-end full sample pages. But making a sample page is non-unique—if you make it once, it's a skill you can deploy every time because the page itself won't significantly differ between components.

**Jason Gong:** Right. I think that makes sense. Any questions for me?

**Edin Abazi:** A couple questions. In terms of how we'd display these, I feel like a documentation site that displays components makes the most sense—a website where you click on each component and see a preview. And it would make sense for it to be made in Webflow as well. But what kind of components are we making? Atomic UI components like fields and buttons, or more CTAs and huge sections?

**Colin Lateano:** The answer is both—not only both, but also comprehensive components that would interface with custom web apps that you'd create eventually. The goal is to create an expansive library so users see a huge repo of what they can do with Webflow. Much like our integrations hub, we should start with the simplest but expand pretty quickly to other things. If there's a question about how to display them, I'd love to figure that out with you. Right now, there's no API to import these effectively, so it's complicated to do this programmatically. But I think we can work together. The first question is: can GrowthX produce these at scale? I want to do ShadCN as the general example set, then also think of really interesting variants that would be great for users to see, letting creativity drive more advanced components.

**Jason Gong:** As long as we have really great categorization and labeling.

**Edin Abazi:** How will they install one component, all components, or multiple at the same time? Can they put them in shared libraries without modifying?

**Colin Lateano:** That's not possible. We're limited by the command line import for a very long time. The security constraint is that once you import a code component, it's live rendered on canvas—the editor for Webflow. Any code can be executed at that point, when you open your Webflow instance, not even the site. So we're not going to have drag-and-drop WYSIWYG importing for security reasons for a very long time. This library should live in the repo we have. Packages should be available in our examples GitHub, and users can import from there using npm commands on the command line. This is going to be developer enablement, not WYSIWYG.

**Edin Abazi:** I didn't mean specifically WYSIWYG, but the whole experience. I think the most sensible thing would be a project init command that sets up the project to be specific to Webflow. Then they can run individual commands, where they press space bar to select which components they want to install.

**Jason Gong:** I think we have more work to figure out on our side. Maybe we can have a separate meeting to talk about this. I feel like it's definitely possible. We can answer what the scope is.

**Colin Lateano:** I'd love to decompose this into a couple of question sets.

**Colin Lateano:** One: can we make components that can be imported into Webflow and render and work? There are limitations in our code component functionality that restrict some React features. Two: how do we merchandise this and display it? Three: where's the store so users can actually use them on their sites? Two and three are tightly coupled but can be independent. If GrowthX wants to own the example page, that's wonderful. Or we can tap our web team to build it. But here's what I really need: can we build the right method on GrowthX to generate a huge library of valuable, distinct components that people would want to import? I want to start from that question before merchandising. If that's in scope and we can prove it works, I can push what we do on our side and expand scope for GrowthX.

**Jason Gong:** Yeah, that makes sense. There are two separate threads. Let's explore: can we do it? I think yes, but we need to figure out what that really means—how much work is it and what we can automate. That's one thread. The other thread is that Webflow is testing our limits. The work is a lot more engineering and product than it is typical. For example, most of our engagements are a lot more editorial in nature.

**Jason Gong:** We need to increase scope so we can dedicate more engineers—people like Edin, people with ML expertise. That's something I need to figure out with Marcel and bring to you with something more structured than the DM thread we have going on.

**Colin Lateano:** That totally makes sense. Just for the record, since this is our weekly sync, I'm making proposals for Q4 and Q1 budget. We're one month late on quarters—our Q1 actually starts in February. So the big thing is expanding engineering scope at GrowthX. I'm making a pitch this week and next week for different contractor and agency scopes. If we expand engineering and split into content and engineering workstreams, I'd love to get what you can present to FP&A in terms of additional GrowthX scope and the outputs. Can you throw that together in a day and a half?

**Jason Gong:** Yes, we'll give you something. If it needs more detail in some areas, let me know.

**Jason Gong:** I'll chat with the team and Marcel in a few hours. We'll get it to you.

**Colin Lateano:** In that proposal, can you outline what fits in each program? If we split between engineering and content, what opens up in content? How do we tie the programs together and fund them?

**Jason Gong:** Yeah, that makes sense. An easier way to frame things is to do it by capacity. For example, the product team talked about the marketplace, but it's hard for me to tell if that's a three-month project or something longer.

**Colin Lateano:** Let me de-scope that. The work is making web apps—not building pages, not managing parts of Webflow, but building web apps that solve user problems. That's an evergreen problem set, not at the same velocity as code components. It ties into code components. The issue is that the marketplace team is moving in go-to-market motions, not holistic product solutions. We're trying to build web apps that solve user problems and can be initiated in Webflow Cloud. Marketplace is not the right word—we'd have a library of interesting apps that solve problems so developers can import them to Webflow Cloud. Eventually, all these bridge together: here's a bunch of components you can import into Webflow to get started, so you know how to style and build your way.

**Jason Gong:** Got it. So it's less about styling and more about finding all the use cases and functional apps that could be helpful. As long as you cover functionality, we don't need a different one for every different look.

**Colin Lateano:** The primary goal is getting started. Some people will use them out of the box, some will configure them in novel ways. Some will take the file and use our remix tool like Lovable—take the file from our examples, plug it into an AI tool, and customize it. We're looking to give a bunch of shells. The marketplace team is framing this wrong. Their heart's in the right place, but it's the wrong frame. We're making a giant example library that developers at different skill levels can use to solve problems for their business marketing sites. Starting December 1st, we're doing a new app every day that you can remix—that's the marketing go-to-market plan. Is there a way GrowthX could supplement that? I've pushed back saying you can't get the team to figure out a bunch of apps in a month. But if it fits, that's amazing.

**Jason Gong:** Yeah, that timeline is terrible. It doesn't work. But at some point, we could pick that up—maybe early next year, January.

**Colin Lateano:** Sure.

**Colin Lateano:** The hope is it's evergreen—an incredible amount of apps for different use cases that you could install on your site. Evergreen work like Code Components and Integration Guides.

**Jason Gong:** I don't see terminal stops on these. Is there any product that does this as a reference? Most other SaaS companies either do it well or don't at all.

**Colin Lateano:** Yeah, Figma Make does it. And probably Replit does it. I can look into a few of the emerging ones. I do have to go, but that's the whole scope of what that is. I'll talk more about the actual scope of work.

**Jason Gong:** All right, sounds good. See you later.

**Colin Lateano:** Thank you.
