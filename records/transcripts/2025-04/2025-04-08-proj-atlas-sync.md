# Proj: Atlas Sync

<metadata>
date: 2025-04-08
time: 20:01 UTC
duration: 49 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Felipe Lima
fathom_recording_id: 56214482
fathom_url: https://fathom.video/calls/272398325
share_url: https://fathom.video/share/knXE7sapHhpSkY3qWaHfMM1RxfRSbHT5
source: fathom
enriched_on: 2026-03-04 18:42 UTC
</metadata>

---

## Summary

Daniel and Felipe reviewed Atlas Sync's core product roadmap, covering pipeline execution UI (table-based with collapsible workflows, step-level execution control, and YAML configuration), input/output handling ($steps.step_id syntax and multi-type components), performance optimization (pagination and archiving), and pipeline versioning strategy. Daniel confirmed offers out for Dana and incoming offer for Stephanie, plus plans to hire 3-4 people for client ops roles — marking a team expansion phase aimed at accelerating both product development and delivery capacity. Next sync scheduled for Thursday.

---

## Context

This is an internal product development sync between Daniel Lopes (GrowthXLabs founder and CEO) and Felipe Lima (external engineer), focused on Atlas Sync, a new pipeline management and execution platform. Atlas Sync is being built as a core product to serve GrowthX's internal needs and potentially as a standalone offering — it's designed as a simpler, more performant alternative to tools like AirOps. The meeting is part of the regular development cadence, with Daniel checking in on progress, discussing technical architecture decisions, and planning team expansion needed to accelerate the project.

---

## Relevance

- **To GrowthX Delivery:** Atlas Sync will become a key internal tool for managing pipeline-based workflows and client execution. The UI design decisions (collapsible workflows, step-level execution control, YAML configuration) directly impact how GrowthX operations teams will manage complex projects. Team expansion will also affect delivery capacity — hiring for client ops (3-4 people) and product-level engineers (Dana, Stephanie) will enable faster delivery of client work.

- **To CheckThat:** The product-level thinking about input/output handling, data type components (text, dates, numbers, images), and pipeline versioning relates to how CheckThat might integrate similar patterns in AI visibility workflows and prompt management.

- **To GrowthX Business Development:** Strong product momentum with a focused, small team shipping quickly. Felipe's satisfaction with focused development time and Daniel's confidence about hiring at high levels suggests this is a strategic hire/team-building moment. Pipeline versioning and performance optimization suggest maturity thinking about product scalability, which is important for enterprise adoption stories.

---

## Overview

- The team is developing a pipeline management system similar to AirOps, with a focus on simplifying UI and improving performance
- Key features include pipeline execution table, step management, and input/output handling
- The project scope is substantial, but there's optimism about releasing a usable version quickly by prioritizing core functionalities
- The team is actively recruiting, with offers out to Dana and potentially Stephanie, to support various aspects of the project

---

## Key Topics

### Pipeline Management and Execution UI

  - Developing a table-based UI for pipeline execution management
  - Features include:
      - Collapsible completed workflows to reduce clutter
      - Ability to run single cells, multiple selected cells, or entire rows
      - Checkbox and play button for execution control
      - Retry functionality for completed steps
  - Planning to use YAML for initial pipeline configuration, with potential for a more sophisticated editor later

### Input/Output Handling

  - Discussing syntax for referencing outputs of previous steps (e.g., `$steps.step_id`)
  - Considering UI components for different data types (text, dates, numbers, images)
  - Initially focusing on text/markdown input, with plans to expand to more complex types later

### Performance Considerations

  - Addressing concerns about UI slowdown with large datasets
  - Implementing pagination and archiving for older executions
  - Potential for downloading completed executions to improve performance

### Pipeline Versioning

  - Recognizing the need to version pipelines to handle changes without breaking existing executions
  - Considering cloning views when pipeline structure changes

### Team Expansion and Roles

  - Offers being prepared for Dana and potentially Stephanie
  - Planning to hire 3-4 people for client ops roles
  - Discussing potential roles for new hires:
      - Dana: Working on product-level features
      - Stephanie: Potentially working on SDK development
      - Clint: Focusing on scalability and infrastructure

### Current Development Progress

  - Felipe is making good progress and enjoying the focused development time
  - The team is optimistic about delivering a usable version quickly by prioritizing core functionalities

---

## Action Items

- Continue development of core pipeline management and execution features
- Finalize and extend offers to Dana and Stephanie
- Proceed with hiring for client ops and additional engineering roles
- Schedule follow-up meeting on Thursday to discuss further ideas and progress
- Prioritize simplifying UI elements to accelerate development and release timeline

---

## Transcript

**Felipe Lima:** Yeah.

**Felipe Lima:** We're going to talk about the pipeline and execution UI. We have different questions that I think we're ready to tackle.

**Daniel Lopes:** Yeah, it's very real and was very difficult to teach. I think workspace management is what I'd call it.

**Daniel Lopes:** Thank you.

**Felipe Lima:** Thank you very much.

**Daniel Lopes:** It's the UI that we're calling the Atlas project.

**Felipe Lima:** OK.

**Daniel Lopes:** Yeah.

**Felipe Lima:** I think that the workspace table that I can see is where the data goes.

**Daniel Lopes:** Okay, so I'm going to start creating the workspace structure. We need to create a bunch of milestones based on the broader areas.

**Daniel Lopes:** We have workspace management and account management. The hierarchy is: account, then workspace, then project, and pipeline.

**Daniel Lopes:** This table view is going to be important.

**Felipe Lima:** Actually, I mean, this table here that is great.

**Felipe Lima:** Yeah, so this is already done. Each row corresponds to a pipeline execution and each column corresponds to a step in the pipeline.

**Felipe Lima:** I just don't have any data today, but it should populate correctly. It's just not usable yet — you can't play or run the pipeline yet.

**Felipe Lima:** That would be the next step. We could make clicking the play button a good milestone for the end of this week — just triggering your workflows.

**Felipe Lima:** What do you think about having that as a deliverable next week? Being able to click the play button here would send the workflow to our temporal worker and run the thing.

**Felipe Lima:** It might be a little too optimistic, but that would be the core use case for this UI — click the play button and it runs the workflow in the pipeline.

**Felipe Lima:** Yeah, yeah.

**Daniel Lopes:** Let me open the app and share my screen so we can go through this together.

**Daniel Lopes:** So we have a pipeline execution and the experience of dealing with the phases of the pipeline. When you click on it, it's a big thing on itself.

**Felipe Lima:** You mean managing this sidebar here, the side panel with input and output starters?

**Daniel Lopes:** Yeah, just the steps and the output. It's a good starting point but it's a project by itself.

**Felipe Lima:** I'd say it's a milestone by itself.

**Daniel Lopes:** How do we call this? Pipeline management?

**Felipe Lima:** I'm calling this pipeline step management. There's a pipeline step, which is each workflow in the pipeline. Each step references a workflow type.

**Daniel Lopes:** Right.

**Felipe Lima:** I'm calling this the step type. So we need the spec for the server — what is the workflow, what are the input schema, what are the output schema. That's the three things you need.

**Felipe Lima:** There's this distinction we need to make when talking about steps. Does that make sense?

**Daniel Lopes:** Yeah, it does.

**Felipe Lima:** So when you say "step," it means the actual step in the pipeline. And "step type" is the kind of schema. This is the pipeline schema.

**Daniel Lopes:** Yeah, I was thinking that the makes sense.

**Daniel Lopes:** I think the first large area is defining the pipeline — finding the types of steps, this schema and all that. That would be under the pipeline management area.

**Daniel Lopes:** Then we have running it, and then working with the output.

**Felipe Lima:** Yeah, I think it's like execution management. In the run management, there's the studio where what happens to each step — that's what we're talking about.

**Daniel Lopes:** Yeah, a pipeline execution working with that output. Basically listing these steps with their inputs, outputs, and triggers.

**Daniel Lopes:** And do we have support for different types of step components? Where is that?

**Felipe Lima:** Let me speak about that first. A step type has a schema. Right now we have props like properties — you could have a date, a string, a number. It can be a complex type or an array, but we don't specify what the display is. What do you want for the display type?

**Daniel Lopes:** Yeah, so if you see here, in the output we have the UI. That's how it's actually happening today — by default, we have text. And then we can create custom special components.

**Felipe Lima:** Oh, I see. So that's how we can handle this. OK.

**Daniel Lopes:** They have a few of these already. I think the minimum we need for sure is text, dates, numbers, and images — single image, multi-image, and arrays for selecting one or many things.

**Felipe Lima:** I think that covers most of what we need. It makes sense. I'll just use what they did as reference since it's fresh in my head.

**Daniel Lopes:** Yeah, so I was thinking that if there was no UI, we'd fall back to a text area.

**Felipe Lima:** Right.

**Felipe Lima:** Yeah, yeah.

**Felipe Lima:** So the photoshoot just texts basically.

**Daniel Lopes:** that would be basically the MVP, but like ideally we would have like image, or a single image, and then the future maybe have, but the RTE would have like the chat already, or maybe they all have the chat, like that's a lot of people have to decide.

**Daniel Lopes:** I think the chat is version future stuff. The minimum here is just a text area with markdown inside, which is fine. Later we can add a chat after.

**Felipe Lima:** Yeah, I was thinking about how they allow you to have a reference field that references other data. They're using building blocks. For us, since we have control over the code and can do things in React, I think a composite field composed of title or body would work.

**Daniel Lopes:** Yeah, exactly. It's composing things together. I mean, even AirOps uses Claude and Claude runs out — they hit the limit. If we had this as one step pipeline, they'd use us instead of Claude.

**Felipe Lima:** So we talked about execution, input, and pipeline. I have a question — how do you reference the output of a step into the input of another one? Do you have specific syntax for that?

**Daniel Lopes:** That's what I was thinking. Every step would have inputs coming in. Let's say we have a React component with props like the name of the step. So for steps, if assignment_generation is the ID, you could choose whatever ID you want.

**Felipe Lima:** So it would be like something like `$steps.assignment_generation` or whatever you want?

**Daniel Lopes:** Yeah, it could be a link as well. This is just brain-dumping here. I was just thinking about what's possible.

**Felipe Lima:** Yeah, that makes sense. This is very similar to how N8N and others do it.

**Daniel Lopes:** Right. The experience matters. You can see they have separate teams — the marketing side and the product side are clearly split. They're using liquid templates for things like this.

**Daniel Lopes:** It's kind of cool because you can see walls of the value.

**Daniel Lopes:** So AirOps has outputs, and I was wondering if we even need that. AirOps does outputs and you get the result object from the step. It's essentially the same as AirOps.

**Felipe Lima:** So I was assuming you always use the output of a previous step. Why would you want to use something else?

**Daniel Lopes:** Sometimes you reference different steps further down. In some areas you want to use outputs from previous steps or from different points.

**Felipe Lima:** Right, but you always want the output of the previous step. Maybe we don't need it if it's always the same.

**Daniel Lopes:** Well, the reason why tools like AirOps do it — they have outputs in their schema. Let's look at how they do it. In their nomenclature, steps are called nodes. So `node.error_trigger` is the node name. And they use syntax like `json_workflow.name` to reference it.

**Felipe Lima:** So it's the name, the step name?

**Daniel Lopes:** Yeah, that's what we'd use as the ID. The output is a JSON array of objects. That's the standard structure. So when a workflow fails, you can pass it as a workflow that will handle the error. They send it as part of the webhook. That's how they structure their schema.

**Daniel Lopes:** So they have, they call workflow.

**Daniel Lopes:** the schema, the schema of this step, it's called workflow and the execution schema is this, basically, for that one.

**Daniel Lopes:** So, and I think you're right, I think they don't do the, like it's gonna look, they do, yeah, they don't do, they don't do so, yeah, the whole stuff.

**Felipe Lima:** It was basically implicit that you grab the outputs, right?

**Felipe Lima:** Which was, yeah, it makes sense.

**Felipe Lima:** Yeah, it makes sense, no, makes sense.

**Felipe Lima:** Yeah, okay.

**Felipe Lima:** That's really a little implementation detail, doesn't really matter that much, but that makes sense, really.

**Felipe Lima:** Cool.

**Felipe Lima:** I think I've had any other questions for you.

**Daniel Lopes:** What have the little details about it here?

**Daniel Lopes:** There's the literature in the board.

**Daniel Lopes:** Oh yeah, I'll let you add rows manually, so you can, let me add that to the, like if you tap there, you would add a row.

**Daniel Lopes:** Another thing that would, like, there's like the little details of the table will be, like, if you ran,

**Daniel Lopes:** thing.

**Daniel Lopes:** Like, ideally, if any completed, it should just collapse and go away, you know, some of our clients today is just like, you scroll like a thousand things to get to where they're actually going to work.

**Daniel Lopes:** It should be at least, I don't know, like, there's some, some UX here that we're going to have to figure out.

**Daniel Lopes:** But do you have the core stuff working?

**Daniel Lopes:** This is easier to do.

**Felipe Lima:** So, basically what a hide, old, completed, workflow, runs, right?

**Felipe Lima:** Yeah, like.

**Felipe Lima:** So they don't, they don't clutter the UI?

**Daniel Lopes:** Yeah, that's what I was thinking.

**Felipe Lima:** It makes sense to me.

**Felipe Lima:** Yeah, you kind of, you want to have them hidden in case you need them.

**Daniel Lopes:** Yeah, you can collapse components based one point.

**Daniel Lopes:** Next year, our team, all right.

**Daniel Lopes:** image gallery and very much future stuff.

**Daniel Lopes:** I think we can go back here and we were talking about some of the little stuff.

**Daniel Lopes:** So we have pipeline management, pipeline execution, that's called this maybe, executions table or executions index table.

**Daniel Lopes:** And we can have the little details there like collapse.

**Felipe Lima:** Yeah, one thing that's worrying me is that I remember you were always complaining about performance of the air up to I how to get super slow so we want to make sure we don't run to the same.

**Daniel Lopes:** Yeah, so I think like we can just like whatever is fully executed we can just like download it.

**Felipe Lima:** Yeah.

**Felipe Lima:** So people don't usually interact with them once it's fully done.

**Felipe Lima:** Yeah.

**Felipe Lima:** Cuteed.

**Daniel Lopes:** Archive.

**Daniel Lopes:** We can even call it archive.

**Daniel Lopes:** Let's call it archive.

**Felipe Lima:** Honestly, I think it's just like some form of pagination.

**Felipe Lima:** Yeah.

**Felipe Lima:** you just have the most recent in the top, maybe.

**Felipe Lima:** Yeah.

**Felipe Lima:** you don't want to be scrolling down every time.

**Felipe Lima:** So just most recent that it's happening in the old stuff.

**Felipe Lima:** To be older.

**Felipe Lima:** Yeah.

**Daniel Lopes:** it's basically a queue of things.

**Daniel Lopes:** And then ability to run single row.

**Daniel Lopes:** or many rows.

**Felipe Lima:** You also have the import feature.

**Felipe Lima:** have button that's import.

**Felipe Lima:** We need to wait.

**Felipe Lima:** We need to wait.

**Felipe Lima:** about the UI to create a pipeline.

**Felipe Lima:** How do you actually create pipeline?

**Felipe Lima:** Do you just use an LLM?

**Felipe Lima:** a chat UI or do you actually?

**Felipe Lima:** Visually or is this code?

**Daniel Lopes:** I say, yeah, the way we have there is fine for now and then we do it.

**Daniel Lopes:** And then later on we do it like a DSL or a template.

**Felipe Lima:** Actually, I should decorate the SL.

**Felipe Lima:** Like Ruby DSL just for like testing and need it, right?

**Felipe Lima:** create the pipeline.

**Felipe Lima:** But yeah, we could just have a, yeah, what's important is that we can just use that for now.

**Daniel Lopes:** What's the, what else we had?

**Daniel Lopes:** What's something I was thinking about in place?

**Daniel Lopes:** In place.

**Daniel Lopes:** In Having.

**Daniel Lopes:** For the.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Accuience of the row, right?

**Daniel Lopes:** So you can change the text like a spreadsheet style.

**Daniel Lopes:** And what else?

**Daniel Lopes:** Oh, there's the ability to run an pyrow at once or pull or step-by-step, you know?

**Felipe Lima:** Isn't that same as the third bullet pointer?

**Daniel Lopes:** Fine though, yeah.

**Daniel Lopes:** What I was thinking is the ability to do.

**Felipe Lima:** I think you're trying to say like an entire row or, yeah, I see a point, you just see it in your cell or the entire row.

**Daniel Lopes:** Yeah, like ideally there would be like, I don't know how the UI would look like.

**Daniel Lopes:** Maybe it's missing like a kind of button.

**Daniel Lopes:** But you know, AirOps, you have, AirOps section doesn't have that.

**Daniel Lopes:** But ideally you would have, like maybe there's a column before here.

**Daniel Lopes:** Or maybe there is a mode that you toggle that...

**Daniel Lopes:** would be, I don't know about you actually have to figure out, but it would be like, press, press, press, press, press, there's like a big air offs behavior of today, and idea that would be another behavior to just press one button and go execute all, you know, without human intervention.

**Felipe Lima:** I see a point.

**Felipe Lima:** Yeah.

**Felipe Lima:** So maybe you should try or try to say, you know, you can click, click, click, click, sell multiple miles and then run them all.

**Felipe Lima:** Is that what you have in mind?

**Daniel Lopes:** No, I was thinking that, like, today, air offs, like, let's say we want to generate an article.

**Daniel Lopes:** It's like the use case would be programmatic as well.

**Daniel Lopes:** You have the pipeline defined, and you don't want people to, if we're going to output like 100 pages, that's 100 pages times 10 steps that you have to click.

**Daniel Lopes:** You press once and let it go all the way to the end, have that option, know.

**Felipe Lima:** So you mean for the entire world, right?

**Felipe Lima:** we'll click once and run the entire world.

**Felipe Lima:** Cool.

**Felipe Lima:** got that.

**Felipe Lima:** But then you also want.

**Felipe Lima:** You run a single cell, so click a cell and run.

**Felipe Lima:** Because there's like a play button in the cell, right?

**Felipe Lima:** So you click the play button in the cell and it runs.

**Felipe Lima:** But you also want to find a stack record, but I don't know if you did not run it here.

**Felipe Lima:** You're also saying that you want to select a cell, multiple cells, and then run specific cells in batch.

**Felipe Lima:** Is that what you're trying to say?

**Felipe Lima:** Yeah.

**Daniel Lopes:** I think, you know, like, the way this could depend.

**Daniel Lopes:** Like, let me take a screenshot of it and open the street floor.

**Daniel Lopes:** If this could be like a, we don't have draw on the, it could be like an additional column here, but it's just like a, like a button, like a play button.

**Daniel Lopes:** Okay.

**Daniel Lopes:** you press, it executes everything.

**Felipe Lima:** But isn't that the-

**Felipe Lima:** As the first column there on the left to the hashtag call, we update using the same thing.

**Felipe Lima:** The hashtag would be to.

**Daniel Lopes:** Yeah, I think just the hash the checkbox and the play button here.

**Daniel Lopes:** We'll do the job.

**Daniel Lopes:** Yeah, we can we can.

**Felipe Lima:** I think that works.

**Daniel Lopes:** no, you're right.

**Daniel Lopes:** think like if the if nothing is selected, and if it's one is collected, this button could switch to X execute one.

**Felipe Lima:** Yeah.

**Felipe Lima:** And then if you have the same button, like you just run whatever is selected.

**Felipe Lima:** Right, cool.

**Daniel Lopes:** makes sense.

**Daniel Lopes:** And if you want to do a step by step, you just click, click, click, click.

**Felipe Lima:** Yeah.

**Daniel Lopes:** yeah.

**Daniel Lopes:** OK, a question for you on.

**Felipe Lima:** If it's a step already ran and finished like this, this is going check marks.

**Felipe Lima:** Can you.

**Felipe Lima:** And then again, I think we need a way to refresh it.

**Daniel Lopes:** that's going to be a kind of like, we have a way to open the step.

**Daniel Lopes:** Maybe if they are ready, you never run them from that.

**Daniel Lopes:** You could have the retry here, you know?

**Daniel Lopes:** They could have the retry button.

**Felipe Lima:** I like that.

**Felipe Lima:** I like that.

**Felipe Lima:** like a little play button that shows when you hover, so.

**Felipe Lima:** Air ops, right?

**Felipe Lima:** right.

**Felipe Lima:** Which is kind of nice.

**Felipe Lima:** So I guess we'll end up copying lot of stuff to do this.

**Daniel Lopes:** Like the main thing that Air Ops does, like, we kind of don't need.

**Daniel Lopes:** It's not because having the text in the field, know, right?

**Daniel Lopes:** So what we actually want is like UX that we have to edit in full the steps.

**Daniel Lopes:** But that's it.

**Daniel Lopes:** But if we have this, and you can have a button to replay, yeah, it would be fine, you know.

**Felipe Lima:** Okay.

**Felipe Lima:** I mean, right.

**Felipe Lima:** basically, we try ability to try an already finished success for that step in the sliding panel.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Felipe Lima:** mean, it has a lot to do.

**Felipe Lima:** I don't need to have actions.

**Felipe Lima:** Like, it's just really a mix of both.

**Felipe Lima:** You know, actions.

**Felipe Lima:** I'm a little bit.

**Felipe Lima:** You need to take on that.

**Daniel Lopes:** This is the same.

**Daniel Lopes:** That's what we were talking about.

**Daniel Lopes:** do it.

**Daniel Lopes:** You're on the screen.

**Daniel Lopes:** Go.

**Felipe Lima:** On the menu.

**Felipe Lima:** On the menu.

**Felipe Lima:** Yeah.

**Daniel Lopes:** The button in checkboxes.

**Daniel Lopes:** The one thing that's kind of tricky in this whole system is like if you change the pipeline, it happens to the data, you know?

**Daniel Lopes:** Yeah.

**Felipe Lima:** So I added a versioning to the step ID, to step type, that's what I'm calling.

**Felipe Lima:** So if you change the spec protocol, then you would be a new version.

**Felipe Lima:** So it's just like you have actions.

**Felipe Lima:** used to refer to the algorithm, you want to go to new, have to explicitly upgrade.

**Felipe Lima:** That way we can prevent like changes from breaking existing stuff.

**Felipe Lima:** But...

**Felipe Lima:** Yeah.

**Daniel Lopes:** We can let it break for now, because it's going to be just us defining the pipelines.

**Felipe Lima:** Yeah.

**Felipe Lima:** It's just something to think about.

**Felipe Lima:** It will cause trouble in the future, for sure, if we allow anything.

**Daniel Lopes:** And just to think about the architecture, to be able to handle that in the future.

**Daniel Lopes:** But we don't have to code that now.

**Felipe Lima:** Yeah.

**Daniel Lopes:** Anything else?

**Daniel Lopes:** Let's...

**Daniel Lopes:** Oh, wait.

**Felipe Lima:** deliver.

**Felipe Lima:** That's right.

**Daniel Lopes:** Well, we might also have to able to sort.

**Felipe Lima:** You need to, like, I suppose you could just use, like, red cross, right?

**Felipe Lima:** we need to, like, mock up the failed run.

**Felipe Lima:** We don't have any in this demo.

**Felipe Lima:** I guess we'll just get a red self with a cross.

**Felipe Lima:** That should be enough, right?

**Daniel Lopes:** Yeah, I think so.

**Daniel Lopes:** Well, what else?

**Daniel Lopes:** I think Peritur can, yeah, the UI, so that.

**Felipe Lima:** So, for creating the pipeline, you said we use a YAML.

**Felipe Lima:** So, would you, like, just upload the YAML file?

**Felipe Lima:** you have, like, import the YAML?

**Felipe Lima:** YAML is just in point.

**Daniel Lopes:** We type it in here, you know, and then we work in the YAML here.

**Felipe Lima:** Oh, and configure in the settings.

**Felipe Lima:** Okay.

**Felipe Lima:** Yeah.

**Daniel Lopes:** And then later, we can just add, like, one of the stacks editors that has, like, YAML syntax, I think.

**Daniel Lopes:** What do we have in flow in this year?

**Felipe Lima:** Yeah, I see your point about here about we need to version the pipeline itself as well or we might get you right because.

**Felipe Lima:** Yeah, what happens if you change the steps super what happens previous executions.

**Felipe Lima:** I guess we can just.

**Felipe Lima:** I'm kind of tempted to just add a version to pipeline and then if you change it, we kind of like clone the view.

**Felipe Lima:** You know, keep the old version and separate view, right, like pipeline if you want.

**Felipe Lima:** And then we choose a new view and then like a fresh, you know, like a bread.

**Felipe Lima:** I don't know.

**Felipe Lima:** Yeah.

**Daniel Lopes:** think we have a.

**Daniel Lopes:** Claude is just.

**Daniel Lopes:** Thank you.

**Felipe Lima:** Yeah.

**Felipe Lima:** Yeah.

**Daniel Lopes:** Two stuff.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Okay.

**Daniel Lopes:** I'll see that.

**Daniel Lopes:** I think it's all of the rate limiting from my idea of like shoving the whole thing into the context.

**Daniel Lopes:** It's not.

**Felipe Lima:** Show me what?

**Felipe Lima:** Because I changed the

**Daniel Lopes:** research instead of using the vector database and pulling just a vector, like the small VBA thing to do the whole research every step of the way.

**Daniel Lopes:** And that's what's causing entropic.

**Daniel Lopes:** Oh, that's right.

**Felipe Lima:** Shumen took us around the rate limit per minute per minute.

**Daniel Lopes:** I'm talking a minute to have this crazy thing that opening it doesn't.

**Daniel Lopes:** Anyway, I'll figure that out, but what else?

**Daniel Lopes:** I think that's it.

**Daniel Lopes:** It's really, it's not a small scope for sure.

**Felipe Lima:** Yeah, no, is, yeah, it's a plan and work here for months.

**Felipe Lima:** Yeah.

**Felipe Lima:** Well, it kind of depends.

**Felipe Lima:** mean, I think we have, we have, I think we can probably release something usable quickly.

**Felipe Lima:** I'm optimistic.

**Felipe Lima:** they kind of really become more complex.

**Felipe Lima:** For example, like the system display types, like if we just say it's just taxi area for now, right?

**Felipe Lima:** right.

**Felipe Lima:** Yeah, and maybe like limit some functionality little bit, I think more about what's complex here.

**Daniel Lopes:** At the end of the day, everything just stacks is fine, like Mark now, like we're just dealing with Mark now essentially.

**Daniel Lopes:** Everybody knows HTML in the company, like I pretty much have everybody, you know.

**Felipe Lima:** Yeah, I think that you honestly be why it's complex, it is the biggest thing here.

**Felipe Lima:** The backend is not sure, not terrible, it's just the UI will be work.

**Felipe Lima:** So we have just whatever we can simplify in the UI if you go have help us shoot faster.

**Felipe Lima:** Yeah, okay.

**Daniel Lopes:** Yeah, I agree.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like maybe if we have like this pipeline working with that area, just like that's a great start and then we can do the chat after, like anything that people are struggling with, like for example, I was just checking right now right before a call on this message that I have just to give you an idea of how this would be impact.

**Daniel Lopes:** But we have this question from days where he's asking for ability to, because right now our pipeline only takes one keyword and tries to use that keyword to roll the article, but he wanted to be able to give more keywords.

**Daniel Lopes:** what he did was to use the feedback action to like add more keywords.

**Daniel Lopes:** But let's say if we had the pipeline the way we're thinking, and we would be able to just do the, to come here like let's say like during the draft phase, and say, select, select the intern and say, add this list of keywords, you know.

**Daniel Lopes:** Right.

**Felipe Lima:** then we run it.

**Daniel Lopes:** That would be super cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** would be super That would be super cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And imagine if we have the MCP as well, you can say actually what are the good Yeah.

**Felipe Lima:** Yeah.

**Felipe Lima:** There's some research find out which keyword you should use.

**Felipe Lima:** Yeah.

**Felipe Lima:** That would be wild.

**Felipe Lima:** Yeah.

**Felipe Lima:** That would be really cool.

**Felipe Lima:** Yeah.

**Felipe Lima:** We'll get there.

**Felipe Lima:** I mean, that's

**Felipe Lima:** it's not a huge lift.

**Felipe Lima:** Cool, my pre-excitable this is I'll keep cranking, but yeah, how are you feeling about things in general?

**Daniel Lopes:** we've been there.

**Daniel Lopes:** We've had a single one all over.

**Felipe Lima:** Honestly, I'm pretty pumped.

**Felipe Lima:** I'm having fun building this, to be honest.

**Felipe Lima:** I really like that there's very little perfume meetings.

**Felipe Lima:** There's very few interruptions.

**Felipe Lima:** I can just get my head down and get  down.

**Felipe Lima:** You know, that feels great.

**Felipe Lima:** really like that.

**Felipe Lima:** I know it won't be always like this and it seems going to grow, which is also cool, having more good help.

**Daniel Lopes:** But I think that's what I'm hoping we don't have to, I can keep getting people at our level.

**Daniel Lopes:** In this case, if I had a design engineering working with you on this project together, don't need to be in other, don't need to manage bunch of dreamers.

**Daniel Lopes:** like, I think the only exception we've made.

**Daniel Lopes:** and we shouldn't make more exceptions to that and like we can run pretty in the same format we have probably for a long year.

**Felipe Lima:** Yeah, I agree.

**Felipe Lima:** No, I agree with you.

**Felipe Lima:** But I'm thinking more like you need more synchronization.

**Felipe Lima:** You need to like onboard an engineer and then you need to synchronize.

**Felipe Lima:** Okay, what are you working on?

**Felipe Lima:** What am I working on?

**Felipe Lima:** What are the next steps?

**Felipe Lima:** kind of have to do that kind of syncing.

**Felipe Lima:** But in terms of like, yeah, you can just keep them working.

**Felipe Lima:** They just run a bit, right?

**Felipe Lima:** You just can trust that they will get so that that's awesome.

**Felipe Lima:** So yeah, you're to.

**Daniel Lopes:** I do one thing that I want to take off of your plate that you're doing so much is like as soon as we have a couple of one or more two engineers wrapped up, it's just help with the recruiting that you don't have to be this solo person running on.

**Felipe Lima:** It's not bad actually.

**Felipe Lima:** I mean, this week ahead of the interview yesterday and that's it.

**Felipe Lima:** I don't have any more interviews this week yet, but it's not terrible.

**Felipe Lima:** It's manageable.

**Daniel Lopes:** Yeah, I think we can figure out once we have more people can figure out the schedule.

**Daniel Lopes:** only do like a couple of a week at most.

**Felipe Lima:** Yeah, I think true to tree is a good is a good soft limits.

**Felipe Lima:** Yeah, I'm interviewing.

**Felipe Lima:** By the way, how are we doing on offers like we have one for Dana and yeah, we have one for Dana.

**Daniel Lopes:** We're gonna make one for Stephanie.

**Daniel Lopes:** Like, I think he's definitely strong.

**Daniel Lopes:** Like he's strong.

**Daniel Lopes:** But I think like he's not at the same level as as some of us.

**Daniel Lopes:** And like I experienced like a business wise and started up that he's been at the same time.

**Daniel Lopes:** I think it's the same title, you know, like with the same title, but like the expectations would be slightly different.

**Daniel Lopes:** Yeah, that's fine.

**Felipe Lima:** I mean, Dana's definitely different level is higher level.

**Daniel Lopes:** think that he's excited about the working at the the product level.

**Daniel Lopes:** So I hope we can close him.

**Daniel Lopes:** So he would be like somebody that would be great for doing the other areas of this project.

**Daniel Lopes:** Like another thing that like I was just talking to Kaya, that means you figure out is the air air table experience.

**Daniel Lopes:** Like I said, yesterday, somebody deleted one of the air.

**Daniel Lopes:** Like he thought so much.

**Daniel Lopes:** And there's a lot of stuff like this that we can't build there, so like we make it proper for our workflows.

**Daniel Lopes:** So, like, Dana could be one person taking that while you take this.

**Daniel Lopes:** And, like, on the SDK work, right, make it a promise.

**Daniel Lopes:** think that's something that Stephanie could be great at, you know?

**Felipe Lima:** Yeah, you're right.

**Daniel Lopes:** And Clint could be great at, like, figuring out how to run them and, like, at scale.

**Daniel Lopes:** mean, so that's how I'm thinking about them.

**Felipe Lima:** Yeah, Kubernetes, maybe, like, having something that's all just scalable.

**Felipe Lima:** Yeah, give us our render.

**Felipe Lima:** Maybe you can the price everything to our format.

**Felipe Lima:** Yeah, hopefully we can do that.

**Daniel Lopes:** So, like, I'm thinking of having both of them at that layer.

**Daniel Lopes:** And you can go either way, because, like, you have to scale on both layers.

**Daniel Lopes:** And I think Dana is more on the product side of things.

**Daniel Lopes:** And I just...

**Daniel Lopes:** Of course, a design engineer role that is like, start closing people that market will switch to full-time.

**Daniel Lopes:** Mark will be on the client ops role, and...

**Daniel Lopes:** Yeah, we need more support.

**Felipe Lima:** feel like just part-time is we're barely making sure answer.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** So like, I think we're gonna, I'll try to hire like three to four people for the client ops.

**Daniel Lopes:** It's sad because there's so much to be done on the program, and I got CEO stuff.

**Daniel Lopes:** I can adjust them from the places.

**Daniel Lopes:** But the offer out is in the staff end of today.

**Daniel Lopes:** And we also close somebody that was like part, basically a PM with me.

**Daniel Lopes:** So he can like, give me all the meetings, help clean up the stuff, like help the other teams manage their projects and all that.

**Daniel Lopes:** And he's also, job should be done expert.

**Daniel Lopes:** So he would be like doing research on our clients as well, them as a product, like one of the things myself.

**Felipe Lima:** Very cool.

**Felipe Lima:** Awesome.

**Felipe Lima:** really excited again, pretty happy about it.

**Felipe Lima:** Even though we didn't have one on...

**Felipe Lima:** So don't worry about it, it's not really not.

**Felipe Lima:** Actually, we have one schedule for later this week for Thursday, so we can talk more about it then.

**Felipe Lima:** Sounds good.

**Felipe Lima:** Yeah, you have a bunch of ideas.

**Daniel Lopes:** want to make sure I include you on all these things about who do we hire next, make sure your process, to hire your level stuff as well, it's not just on it.

**Felipe Lima:** Yeah, happy to have one wherever, yeah, don't feel like you have to include me or anything like that.

**Felipe Lima:** But thank you.

**Felipe Lima:** Sounds good.

**Daniel Lopes:** Yeah, just want to make sure you are excited and you're here.

**Daniel Lopes:** I'm very excited.

**Felipe Lima:** Yeah, don't worry about that.

**Felipe Lima:** Awesome, not good.

**Daniel Lopes:** That sounds good.

**Daniel Lopes:** All right, I'll give you a few minutes back.

**Daniel Lopes:** one.

**Felipe Lima:** I will go and shoot, bye.

**Daniel Lopes:** Bye.
