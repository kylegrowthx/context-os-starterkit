# CI Demo: Georgemaine

<metadata>
date: 2025-08-11
time: 20:00 UTC
duration: 31 minutes
organizer: Daniel Lopes
participants: Daniel Lopes, Georgemaine Lourens, Stevie Kim
fathom_recording_id: 79818581
fathom_url: https://fathom.video/calls/377866774
share_url: https://fathom.video/share/F5xfxJj47CybrV136Q47eNhRMEWMZfPx
source: fathom
enriched_on: 2026-03-03 15:42 UTC
</metadata>

---

## Summary

Georgemaine presented the UI implementation for CheckThat's assignments feature, including the index view with sorting and bulk actions, and the detail view with tabbed editor/content layout. Daniel and Stevie provided feedback on nomenclature (renaming "Generated Output" to "Content" to reflect human involvement), UI hierarchy (making the Brief/Content tabs more prominent), and structural changes (moving assignments to the project level instead of inventory level). The team agreed to proceed with the Pages feature next, as it's critical for tracking metrics, with Daniel handling the data structure definition and Georgemaine starting the index view implementation.

---

## Context

This is an internal product development session for CheckThat, GrowthX's strategic software bet for B2B AI visibility. Georgemaine (engineer), Daniel (architect/product lead), and Stevie Kim (business/operations) are working on the content management platform core features. Georgemaine had skipped the demo in a previous meeting with Brad (the other engineer), so Daniel requested this follow-up to review the assignments UI and ensure alignment on the direction before moving to the next phase. The broader context: they're building an inventory-based content system with pages, opportunities, and assignments that feed into pipelines for execution—a complex product requiring close collaboration between engineering and product on both UI patterns and backend architecture.

---

## Relevance

- **To CheckThat Product:** Tab nomenclature shift from "Editor"/"Generated Output" to "Brief"/"Content" clarifies that output isn't purely AI-generated—humans work throughout. Architecture decision to move assignments to project level simplifies user workflows but adds backend complexity around pipeline switching mid-project. Pages feature is next priority and highest risk/complexity after assignments.
- **To GrowthX Delivery:** The assignments UI pattern (index with sorting/filtering + detail editor + output) becomes the template for how clients manage content workflows. Tab visibility/prominence discussion reflects real UX challenge in making core controls obvious without cognitive overload. Multi-pipeline support at project level enables flexible testing of different workflows for different client types.
- **To Team Operations:** Stevie Kim joining the product session reveals knowledge gaps—needs separate briefing on core concepts (pages, opportunities, assignments, pipelines). Indicates need for better async documentation or structured onboarding for new team members entering the product.

---

## Overview

- The assignments UI (index, detail editor, and content output views) is in good shape, with the main feedback being improved tab visibility and styling to highlight the Brief/Content toggle
- Assignments will be moved from inventory level to project level; projects can have multiple pipelines but one active pipeline tied to assignments
- Backend complexity around pipeline switching when assignments are in-progress needs to be handled at the implementation level; Daniel will send technical notes to Brad
- Tab naming finalized: "Brief" for the editor/task definition, "Content" for the output (reflecting human involvement, not just AI generation)
- Pages feature is the next development priority because it's the parent object for tracking metrics and the highest-complexity piece after assignments
- Import/export functionality for opportunities and assignments needs to be added alongside the Pages feature

---

## Key Topics

### Assignments Index View and Sorting

Georgemaine demonstrated the index view with columns for status, name, content type, date modified, and author. Multiple sorting modes are available: by name (flat list), by type (bucketed, potentially collapsible), and by person (to see who's working on what). Bulk actions allow selecting multiple assignments to change status or reassign ownership at once, though the bulk action UI still needs styling refinement.

### Assignments Detail View with Tabbed Interface

The detail view splits into two tabs: "Brief" (the task/assignment definition, including what work needs to be done and the angle/approach) and "Content" (the output, which may be text, images, metadata, or any combination depending on assignment type). The Brief tab is the editor where team members refine the task before sending it to production. The nomenclature change from "Editor/Generated Output" to "Brief/Content" better reflects the collaborative, human-involved nature of the work.

### Tab Visibility and Visual Hierarchy

Daniel flagged that the Brief/Content tabs need higher visual prominence—they are the core control users interact with, but styling currently makes them look like metadata tags rather than major navigation controls. Stevie initially confused them for tags, confirming they're not visually obvious enough. Georgemaine agreed to experiment with different styling or repositioning the tabs higher in the visual hierarchy.

### Publishing Workflows and Project-Level Settings

For clients with publishing capabilities, Daniel noted there should be a way to set up and trigger publishing workflows from the assignments UI, likely placed next to the ellipsis menu. Configuration of which pipeline is tied to project assignments should happen at the project level, not the assignment level, allowing projects to have multiple pipelines for testing but only one active pipeline for assignments.

### Project-Level Architecture: Assignments Moved from Inventory to Project

Daniel clarified that assignments should live at the project level, not the inventory level. When accepting an opportunity, the user chooses which project it belongs to, then the assignment lands in that project's assignment view. This differs from the initial structure. Projects can have multiple pipelines, but assignments for a project are tied to one active pipeline. The backend complexity lies in deciding what happens to in-progress assignments if the pipeline is switched mid-project—Daniel will send detailed notes to Brad on this.

### Pages Feature as Next Priority

Pages is the next development priority because it's the parent object for the whole system and critical for tracking metrics. The team discussed the data structure based on a Friday meeting; Georgemaine will need to search for the detailed specification. The Pages feature will likely mirror the assignments index pattern but display data similarly to what Marcel has been showing leadership. Import/export functionality for both Opportunities and Assignments must also be completed.

### Bulk Operations and Assignment Management

The UI supports assigning multiple items and changing their status in bulk. The system distinguishes between "new content" and "refresh content" assignment types. Reading time and word count metadata appear in the output view but may not apply to all assignment types (like FAQ or image generation), so the UI will adapt based on the specific workflow triggered.

---

## Action Items

- **Georgemaine Lourens (GrowthX)** — Move assignments from inventory level to project level and update the generation flow accordingly; finish styling the Brief/Content tabs to make them more prominent in the UI hierarchy
- **Daniel Lopes (GrowthX Labs)** — Send technical notes to Brad regarding pipeline integration, assignment handoff, and backend decisions about in-progress assignments when pipeline is switched
- **Georgemaine Lourens (GrowthX)** — Start development on the Pages feature, beginning with the index view and using the data structure from the Friday design session
- **Daniel Lopes (GrowthX Labs)** — Search for and share the detailed Pages data structure specification with Georgemaine for review and comment
- **Georgemaine Lourens (GrowthX)** — Schedule a separate briefing call with Stevie Kim to walk through project context, terminology (pages, opportunities, assignments, pipelines), and product definitions

---

## Transcript
**Daniel Lopes:** Good.

**Daniel Lopes:** Just eating something real quick.

**Daniel Lopes:** Yeah, we should have checked the demo next time.

**Georgemaine Lourens:** Yeah, I should have given a demo just now, but I wasn't completely forgot.

**Georgemaine Lourens:** Like, Brad was chatting for like 20 minutes, and I felt like he covered pretty much everything, and we were already going over time, so I felt like, hey, maybe I should just skip it.

**Georgemaine Lourens:** But then I realized, like, hey, I actually didn't get a chance to show it to you in like a week, because last week on Friday, our one-on-one, we replaced it with a call as well, so.

**Daniel Lopes:** Oh, yeah, yeah.

**Daniel Lopes:** Yeah, I'm still like scheduling our one-on-one.

**Daniel Lopes:** How often do you think we should meet?

**Daniel Lopes:** I was thinking like three weeks initially, but we can do that at two weeks, whatever you think is best.

**Daniel Lopes:** But we can also always do a one-off like this as well.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think...

**Georgemaine Lourens:** I think for now, this is fine.

**Georgemaine Lourens:** But I think maybe at this phase of the project, I remember the last chat we had was about the UI.

**Georgemaine Lourens:** And you had a different direction in mind.

**Georgemaine Lourens:** And I think it's in really good shape.

**Georgemaine Lourens:** So I think maybe it's good for you to also have a look at it.

**Georgemaine Lourens:** So if you want to make any changes before this goes to the branch.

**Georgemaine Lourens:** So maybe I could share my screen.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Sounds good.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** All right.

**Daniel Lopes:** Can you see everything?

**Daniel Lopes:** Yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Let's see.

**Georgemaine Lourens:** And so this is where I'm at right now. I have a section for the inventory here of the pages and the opportunities, but those two are empty. So the view is here. I loaded in all of the stuff from Airtable to test it out, and I think it works pretty well.

**Georgemaine Lourens:** Right now what I have is a status column and a little icon that represents that. You have the name, the type of content, the date modified, and the author. And if you want to switch that view, you can as well.

**Georgemaine Lourens:** So you could sort by name.

**Georgemaine Lourens:** And that's just kind of like a flat list on the name.

**Georgemaine Lourens:** You can also make buckets based on the type.

**Georgemaine Lourens:** I think it might be worth making these collapsible, but it's all in that order.

**Georgemaine Lourens:** And you can also sort by person just to see who's working on what.

**Georgemaine Lourens:** And also on type, obviously, type new content or refresh content.

**Georgemaine Lourens:** And if you want to switch status, you can just select one and hit that.

**Georgemaine Lourens:** Action menu and just pick one of these.

**Georgemaine Lourens:** And then it updates.

**Georgemaine Lourens:** And this is also where you can do the assigning, too.

**Georgemaine Lourens:** But this still needs a little bit of styling.

**Georgemaine Lourens:** And I know we don't want to do it yet.

**Georgemaine Lourens:** But I also added in the ability to do it in bulk.

**Georgemaine Lourens:** So you can just select a bunch of them and then assign the status here or assign a person.

**Georgemaine Lourens:** And if you want it, then you get this view.

**Georgemaine Lourens:** And this is kind of like the show view, right?

**Georgemaine Lourens:** You have an editor for all of the brief content.

**Georgemaine Lourens:** And if you want to turn that into actual content, then you could just click Generate, then pick a project, and then set up the task pipeline.

**Georgemaine Lourens:** And I need to work on this with Brad, which he's doing right now.

**Georgemaine Lourens:** And then as soon as it's generated, I just marked up some status.

**Georgemaine Lourens:** And then you get the generated content.

**Georgemaine Lourens:** And if you want to...

**Georgemaine Lourens:** To the state management, you can also do it from here.

**Georgemaine Lourens:** You can also do the signing status and person here.

**Georgemaine Lourens:** And you can also just go to the next one by just hitting these buttons or just using e-board navigation.

**Georgemaine Lourens:** So this is how far I got so far.

**Georgemaine Lourens:** And I think we're in a really good place UI-wise.

**Georgemaine Lourens:** I think the only thing that me and Brad talked about was that we also need to show the meta content, the meta text, and the image here in the generative content.

**Daniel Lopes:** It could be hidden like you guys have.

**Daniel Lopes:** It could be like maybe a tab or a button at the top or something like this because we actually want to detach that from what's going to be sent to the pipeline.

**Daniel Lopes:** Because essentially we just want to send the text.

**Daniel Lopes:** And we only need to be thinking about this most of the time and the keywords and whatever.

**Daniel Lopes:** Other metadata should be more about like, almost like the opportunity and why does it exist and less about like the creation itself.

**Daniel Lopes:** So like having it separate and like hidden, not on the face would be ideal.

**Georgemaine Lourens:** Yeah, maybe we can add a tab here.

**Georgemaine Lourens:** I think what Graff was thinking about was like, what if we share this view with a client and they probably want to review, the tags as well, maybe at some point images, so maybe it could be a collapsible section, but I think a tab could work as well.

**Daniel Lopes:** For images, like, oh, you're thinking, okay, so you have selected the generated content, not the assignment, right?

**Georgemaine Lourens:** Yeah.

**Daniel Lopes:** So that was the output.

**Georgemaine Lourens:** Yeah, I think I should update the names.

**Georgemaine Lourens:** I think that's a bit clearer, but the assignment would be the editor, which basically this, and then you go to...

**Georgemaine Lourens:** And then you get the generated output, and the generated output can contain data tags.

**Daniel Lopes:** Right, So in this view here, would be important to see everything.

**Daniel Lopes:** So almost like seeing the output step that we have in the pipelines, figuring out the way to present that here, you know, because it can be anything.

**Daniel Lopes:** The assignment doesn't have to be content only.

**Daniel Lopes:** So I think the name here could be like assignment instead of editor.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Or brief.

**Daniel Lopes:** And then on the other side could be result or like output.

**Georgemaine Lourens:** And then...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Or there's a better word for that.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think we can do for the editor, I think we can just do the brief.

**Georgemaine Lourens:** I think that makes the most sense.

**Georgemaine Lourens:** We've been talking about that for a long time now.

**Georgemaine Lourens:** And I think this can either be content or output.

**Daniel Lopes:** Because it's not always just generated output. Sometimes it would be just images, sometimes it would be just metadata, or sometimes it would be refreshing links, changing the sources, or adding FAQ and so on.

**Georgemaine Lourens:** Yeah, I think that's a good point.

**Georgemaine Lourens:** So, I am, yeah, I'm pretty happy with it, too.

**Georgemaine Lourens:** And I honestly want to wrap this up and kind of, like, move to the pages.

**Georgemaine Lourens:** So, I want to finish a couple of things, like the tags, and I also want to fix a few bugs that I have here.

**Georgemaine Lourens:** Are you, is there anything that you would want to see heading into a different direction, or do you feel like this is okay?

**Daniel Lopes:** A couple of things.

**Daniel Lopes:** Maybe if just show Stevie the assignments index page again.

**Georgemaine Lourens:** Yeah, all right, I didn't see this.

**Stevie Kim:** Hold on, let me close the door.

**Stevie Kim:** I do have a little bit of an opinion about what we call "Generated Output." I think "Content" makes more sense.

**Georgemaine Lourens:** Yeah, I agree. Images, no matter what it is—it's content, right?

**Stevie Kim:** I think "Output" is too obscure.

**Daniel Lopes:** Yeah, that is a good point.

**Georgemaine Lourens:** Yeah, and, you know, can think of a game for it, but...

**Daniel Lopes:** I think "Generated" is misleading because it's not always generated. There are people in the mix working on it throughout.

**Stevie Kim:** Yeah, exactly. It's collaborative work, so "Content" just makes more sense.

**Georgemaine Lourens:** No, this is super useful. Thank you.

**Daniel Lopes:** Yeah, you're right.

**Daniel Lopes:** I'm trying to think of the other, all the different assignments we take, like refreshing, meta text stuff.

**Daniel Lopes:** We add FAQs, we create new pages.

**Daniel Lopes:** It's always, essentially always content, at least in the context of this.

**Stevie Kim:** And I think what's helpful is understanding where content came from and how it got here—whether it was generated by AI, edited by people, or a mix.

**Daniel Lopes:** "Generated" has a negative connotation—it implies nobody did anything and you just sent a prompt to ChatGPT and got something back. In reality, people are editing and refining this throughout the process. It's like how you don't call code that was generated by ChatGPT "generated code" if you're actively working with it.

**Stevie Kim:** So what's the purpose of these tabs? Why have them at all?

**Daniel Lopes:** You mean these two tabs here?

**Stevie Kim:** Oh, those are tabs? I thought they were text labels. Do you want to walk through one so I understand what's going on?

**Georgemaine Lourens:** Yeah, let's walk through one. So let's say you have an assignment to write about rental car mileage tracking. You open it and you get the Brief tab. An editor would start working on this here, refining it until they feel like it's ready to send to production.

**Daniel Lopes:** Yeah, the Brief is the task. It includes what you're working on, why you're working on it, the angle you're taking, suggested keywords, and a proposed structure for the content.

**Daniel Lopes:** We're hiding some of the less-critical metadata—like keywords, competitor URLs, and other fields that clutter the view. Most people should focus on the proposed structure and the high-level reason for the article, which are the key pieces.

**Daniel Lopes:** So the visible fields are just the topic cluster, short description, potential outline, and the angle for each part. After that, people will work on it. That "Generate" button should probably be renamed—it's really "Send to Production," because it's handing off the task to the production team to execute.

**Daniel Lopes:** It just happens that we have AI working with people to generate the content, but it would be, like, send it to production, or send it directly.

**Daniel Lopes:** Execution or something like this, and then the content tab is the output of that process, and the process today happens in the pipeline, but in the future might happen somewhere else.

**Stevie Kim:** I don't know enough about how content managers think about things, but we want to be as explicit and concise as possible.

**Daniel Lopes:** Yeah, I think those two tabs should be more prominent. They're the core things you interact with—the task before and then the outcome. The fact that Stevie mistook them for tags shows they're not visually obvious enough.

**Georgemaine Lourens:** You're right. We could try different styling or move them higher in the visual hierarchy to make them stand out more.

**Daniel Lopes:** I think it's just the styling. Let me make a note on that.

**Daniel Lopes:** Another thing: some clients just work in the pipeline, while others have custom publishing workflows. We should think about where a publishing button would go here. It could live next to the ellipsis menu if needed, but that configuration—which pipeline is tied to assignments, publishing setup—should really be at the project level, not here. It's a project setting.

**Georgemaine Lourens:** So you'd define that once for all assignments in a project?

**Daniel Lopes:** Yeah, exactly. Assignments should be at the project level, not at the inventory level.

**Daniel Lopes:** For example, a client like Abnormal has one blog for glossary and another CMS for guides. At the project level, assignments might have different settings depending on the blog.

**Daniel Lopes:** That's why I originally put assignments in the sidebar under projects. Assignments completed become the staging area for the next phase, so we don't need a separate staging section.

**Daniel Lopes:** Assignments would be at the project level, and when you take an opportunity, you choose which project it goes to.

**Georgemaine Lourens:** That makes sense. So when you accept an opportunity, you choose which project it goes to, and it lands in that project's assignment view.

**Daniel Lopes:** Right. When executing assignments in the pipeline, you tie the pipeline to a type of project—it's assignment-based for client work. But you can also have free-form projects for research, sales, or recruiting, which don't follow the assignment-execution model.

**Daniel Lopes:** For client work, we have pages, opportunities, and assignments tied to a project. That's the model.

**Georgemaine Lourens:** I'm a bit fuzzy about the pipeline configuration. Is it one pipeline that intelligently adapts—like, if an assignment is for tags, it outputs tags; if it's for images, it outputs images? Or do we need special configuration for each type?

**Daniel Lopes:** You can have multiple pipelines in a project for testing different workflows, but you pick one active pipeline for assignments. That way, you can experiment without disrupting production.

**Georgemaine Lourens:** So if you set one pipeline for new articles and one for images, it handles both without additional configuration?

**Daniel Lopes:** The workflow is: create a workspace, create a project, choose if it's assignment-based or not. If it is, create a pipeline. When you go to the Assignments page, select which pipeline to use for that project. That pipeline becomes the active one for all assignments in that project.

**Daniel Lopes:** In the future, if you want to switch to a new pipeline with different settings, you go back to project settings or the Assignments Index and change it. But we need to decide: what happens to assignments that are already in progress? That's a backend decision we have to make.

**Georgemaine Lourens:** The UI side is simple—set it up once. The backend complexity is in handling the various edge cases. I'll let Brad handle that part of the implementation.

**Georgemaine Lourens:** So the to-dos for me are moving assignments to the project level and updating the generation flow.

**Daniel Lopes:** The typical assignments are article creation and refreshers. The UI should handle those well. Metadata like reading time might not apply to all types—like FAQ or image generation—but that's a minor detail we can adjust as needed.

**Georgemaine Lourens:** I'll look at the different workflows and adjust the output display if needed when we hit edge cases.

**Georgemaine Lourens:** Should we worry about the UI for pipeline configuration now, or can we defer it until after Pages?

**Daniel Lopes:** The UI risk is low. The real complexity is backend—the handoff between assignments and pipeline, what happens when you switch pipelines, etc. I think pipeline configuration belongs at the project level, but I'll send detailed notes to Brad to get his input.

**Daniel Lopes:** Let's move to Pages next. Opportunities will be simple—just a table with short descriptions.

**Georgemaine Lourens:** For now, yes. But we'll need import/export functionality for both opportunities and assignments so people can migrate from the old system. Brad has the CSV mapping, so I can reuse that.

**Daniel Lopes:** So you're thinking about starting with Pages first?

**Georgemaine Lourens:** Yes. Pages is the parent object, and from Friday's call, we decided it's crucial because we need to track metrics there.

**Daniel Lopes:** I agree. Pages is the riskier part—the bulk of the project after assignments. Assignments alone could ship as-is, even without Opportunities. But Brad might prefer shipping everything together for a more complete product launch.

**Georgemaine Lourens:** What do you think, Stevie?

**Stevie Kim:** I don't know what half this means. I know assignments, but not pages, opportunities, or pipelines.

**Georgemaine Lourens:** Would it make sense to schedule a separate call so I can walk through all this with you and we can get to know each other better?

**Stevie Kim:** Absolutely, that would be wonderful.

**Georgemaine Lourens:** I'll set that up.

**Georgemaine Lourens:** Then I think I've shown everything I wanted to show.

**Daniel Lopes:** How are you thinking about the Pages feature? Do you have mockups or wireframes?

**Georgemaine Lourens:** The data structure changed slightly after Friday's meeting. I wrote it down but need to find it. Basically, it should show the same data Marcel's been showing to leadership—metrics and all that. From Friday's sketch, the index view would be like an Airtable for URLs, and we'd add a detail/show page for each row later. I'll start with the index.

**Daniel Lopes:** I'll search for the data structure specification I created and share it with you so you can review it.

**Georgemaine Lourens:** Thanks, I'm happy with this.

**Daniel Lopes:** Great work. Thanks for the update.

**Georgemaine Lourens:** I'll hop off now. Talk soon.
