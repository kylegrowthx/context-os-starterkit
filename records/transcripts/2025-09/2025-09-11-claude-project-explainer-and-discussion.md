# Claude Project Explainer and Discussion

<metadata>
date: 2025-09-11
time: 15:06 UTC
duration: 36 minutes
organizer: tiandra@growthx.ai
participants: Sucheta Biswas (GrowthX), Tiandra Burns (GrowthX)
fathom_recording_id: 86608941
fathom_url: https://fathom.video/calls/402212496
share_url: https://fathom.video/share/6WpGLBbeCA1pEGUX6Rqepr7w3kKZspLp
source: fathom
enriched_on: 2026-03-03 03:45 UTC
</metadata>

---

## Summary

Sucheta walked Tiandra through GrowthX's Claude AI setup and project workflows, demonstrating how to use custom instructions, file uploads, and specialized projects for content creation and post-processing tasks. They discussed how Claude's artifacts and training capabilities address common workflow challenges, particularly for clients like Abnormal Security (which requires heavy internal linking and fresh statistics) versus simpler clients like Immubit and Tag. Tiandra committed to resolving her Claude access issues with Yusuf and creating a Claude project for Immubit's post-processing workflow.

---

## Context

This is an internal GrowthX meeting between two content delivery team members. Tiandra was experiencing technical difficulties accessing Claude via the pod-a@growthx.ai account and needed guidance on the platform setup. Sucheta, who has already built Claude projects for Abnormal Security (GrowthX's most complex client), walked Tiandra through the login process, demonstrated how to set up custom projects with instructions and file uploads, and shared best practices for leveraging Claude's capabilities in content creation workflows. The discussion reflected GrowthX's broader initiative to adopt Claude as a post-processing and content generation tool to improve efficiency and quality across multiple client accounts.

---

## Relevance

**To GrowthX Delivery:**
- Claude projects with custom instructions and file uploads can significantly reduce post-processing time, particularly for internal linking challenges on clients like Abnormal Security
- Sucheta's approach of uploading case studies, glossary pages, and blog examples as training materials enables Claude to make more accurate decisions without hallucinating
- Pod accounts have limitations (no Google Drive integration), but personal accounts unlock additional features; this should inform how team members structure their Claude workflows
- Different clients require different strategies: Abnormal needs heavy internal linking and fresh statistics on each article, while Immubit and Tag are more straightforward and can reach optimized workflows in ~1.5 months

**To GrowthX Business Development:**
- Claude adoption and workflow optimization could position GrowthX as having proprietary AI-assisted content methods, relevant to AI visibility strategy and CheckThat positioning
- Tiandra's experience optimizing Immubit and Tag content demonstrates scalability potential for efficient, high-volume client work
- Internal knowledge sharing on Claude best practices (visible in Sucheta's detailed instruction-building approach) creates team leverage and client delivery efficiency

---

## Overview

- Claude AI offers advanced capabilities for content creation, editing, and research beyond standard ChatGPT
- Custom instructions and file uploads allow for tailored AI assistance on specific projects/clients
- Proper setup and access to Claude (via pod accounts) is crucial for leveraging its full potential
- Experimentation and sharing best practices between team members can optimize workflows

---

## Key Topics

### Claude AI Setup and Access

- Tiandra experienced difficulties logging into Claude using the pod-a@growthx.ai account
- Sucheta demonstrated the login process, which requires being added to the correct pod by Yusuf
- Personal accounts allow for more features like Google Drive integration, while pod accounts have limitations

### Claude AI Capabilities and Usage

- Custom instructions can be added to create specialized AI assistants for different tasks/clients
- Files (articles, guidelines, etc.) can be uploaded to provide context and training data
- Claude can generate content, perform research, add internal links, and follow specific formatting guidelines
- The system learns and improves over time with continued use and feedback

### Content Creation Workflow Improvements

- Sucheta uses Claude for post-processing tasks, especially for challenging aspects like internal linking
- Tiandra has streamlined her process by carefully editing briefs and outlines to reduce AI hallucinations
- Both discussed strategies for efficient research and maintaining fresh statistics/examples in content

### Client-Specific Considerations

- Abnormal Security requires frequent updates and diverse examples due to the evolving cybersecurity field
- Immubit and Tag have more straightforward content needs, allowing for a more efficient process
- Different clients may require varying levels of customization and ongoing research

---

## Action Items

**Tiandra Burns (GrowthX)**
- Contact Yusuf to resolve Claude pod access issues. Need to be added to pod-a@growthx.ai in order to log in.
- Create Claude project for Immubit post-processing. Upload artifacts (writing guidelines, internal links reference, glossary), add custom instructions for post-processing workflow.

---

## Transcript

**Sucheta Biswas:** So I didn't need Google, okay, it's the same thing.

**Tiandra Burns:** Let's just see if it's loading properly. This is Google, right?

**Sucheta Biswas:** It takes a while, and then you realize it's not you, it's the browser.

**Tiandra Burns:** I'm going to use another account. I don't have my 1Password here.

**Sucheta Biswas:** Oh, you don't actually need 1Password. You will only need your Gmail. Your Gmail account should be open somewhere.

**Tiandra Burns:** Okay, it's pod-a@growthx.ai. It says "Couldn't find your account."

**Sucheta Biswas:** Try pod dash A in small letters.

**Tiandra Burns:** I'm so sorry. I didn't get a chance to log on before this meeting.

**Sucheta Biswas:** It's good that we're here because the other things will take less time. I knew that you were taking some time to log in to Claude, so let's just get this sorted.

**Tiandra Burns:** Yeah, it's telling me that this email can't be found. Let me sign in and try again.

**Tiandra Burns:** Okay, there we go. Now you can see what I'm doing.

**Sucheta Biswas:** Okay, signed into Anthropic. Why don't you check Claude to sign in with email?

**Tiandra Burns:** How do I log in to Claude? What is happening?

**Sucheta Biswas:** Let me log off the account where I'm not using it much on Firefox and I'll show you.

**Tiandra Burns:** Yeah, it's still loading on Chrome.

**Sucheta Biswas:** That's so crazy. Okay, I will just share my link with you now.

**Tiandra Burns:** Okay, yes, that would be great.

**Sucheta Biswas:** Okay, so here you just paste like pod-E, and then you just continue with email. Then click the link sent to your email.

**Sucheta Biswas:** So if you're part of a pod—for example, pod-E is Jakub's pod and I was not added to it. So you need to tell Yusuf that you need to get added to this pod first. So pod-E@growthx.ai. If you're added to that pod, you can easily sign in. If you're not, then you can't sign in. You will not get the email.

**Sucheta Biswas:** You need to be on pod-A. So if you're on pod-A, which you are, you will get a similar email here, and then you can just click on it.

**Sucheta Biswas:** Okay, so this one is more simple. Let me show you this one. Basically, we go to projects over here, right?

**Sucheta Biswas:** Have you seen how custom GPTs work? Let me show you that first. I'll go to my ChatGPT.

**Sucheta Biswas:** My session has expired. Everything is broken.

**Tiandra Burns:** Clearly not today.

**Sucheta Biswas:** So basically what happens in a project or custom GPT is you feed it custom instructions. And you create these micro editors or GPTs. For example, with Abnormal, what we've done is created a post-processing kind of GPT. What I'm doing is taking all the instructions I've fed into the Atlas artifact and copying them here as files.

**Sucheta Biswas:** For example, I have an internal links file, then I have the blogs, some of the best sample blogs, glossary templates, other blogs. And all the instructions, you can paste in the LLM format over here. So you see all this markdown and different stuff which you already put on Atlas. You just have to copy paste the artifact over here.

**Sucheta Biswas:** You can do some copy pasting here. Or you can paste or upload some artifacts, say the writing guidelines. We have the target personas on the files. And the best part about Claude is it allows you to attach more files and add more instructions.

**Sucheta Biswas:** I started using this one first. You can always stop me and ask questions or let me know if I'm going too fast. For this, what I basically started doing is I started training this. First I upload the instructions for whichever prompts for LLM and some of my best articles for that account. And then what I started doing is I started teaching it.

**Tiandra Burns:** Are you just putting the URLs there?

**Sucheta Biswas:** No. I'm just copy pasting. So, for example, if I have this document open, I just copy and I paste it in. What happens on Claude is it turns it automatically into kind of a document.

**Sucheta Biswas:** So, for example, I'll just show you this magic. This is one article and this is a different article. Now I'm pasting it over here and asking, "Can you help me find just random words out of both these articles?"

**Tiandra Burns:** So it will basically take whatever you upload.

**Sucheta Biswas:** And the best part is you can always attach a drive to it or link your drive. But because we're using the group pod, you cannot do that because this is a different email idea altogether. But if you're using a personal one on another browser, you can maybe attach your URLs or do something like that.

**Sucheta Biswas:** It will show you this has analyzed article one with this word count, and article two with this much word count. And then this is the copy function. So you can basically copy this.

**Sucheta Biswas:** And the best part is that if it contains all the links and stuff like that, when you copy it, it's going to copy everything. If we just paste it here, you're getting well formatted. Your formatting is taken care of with H2s and H3s. These are some of the advantages over ChatGPT. This is how basically the thing functions.

**Sucheta Biswas:** Now what I discovered today is that you can make spelling mistakes also, so it's okay. It misunderstands. Basically you just make Claude do all the work for you. So you convert them into this type, whatever we have on Atlas backend. And then you can copy paste individual ones. So if you want only the bullet formatting or only the interlinking prompt, you can copy them. Or you can copy the entire thing.

**Sucheta Biswas:** So basically what I did today when I was editing this one is it kind of automatically got saved into this files format instead of me going there and adding it. There is one feature where you can kind of directly convert it into an artifact. It did it automatically and just saved it in the file section on its own.

**Sucheta Biswas:** So these are all the case studies that I kind of made from the Abnormal side. And then I just saved it here. So basically what you can do is you can create different projects for different functions as well. Okay, so Abnormal has these industry pages where it's the same template, but you change the name of the industry—construction industry, manufacturing, things like that. So these will be like very hyper specific projects, which you feed into Claude. So the instructions will vary from whatever I do in the post-processing one.

**Tiandra Burns:** Basically, just go as hyperspecific as you can.

**Sucheta Biswas:** Now, what I've had most difficulty in Abnormal is in the internal links. So for that, Panzer suggested that I create a document for internal links, which I already had. And then here somewhere I've instructed it to fetch the internal links from the document. So initially, it might give you false results or kind of hallucinate. So then you kind of keep on training it and then it improves over time.

**Sucheta Biswas:** This will be important for you. Remove all the company names. I've kind of mentioned it.

**Tiandra Burns:** And some of this also comes from the Atlas artifacts.

**Sucheta Biswas:** So you just feel free to find and paste all the artifacts over here or just upload them as files. And also when you have uploaded things on files, for example, we have glossary pages which are definition pages and then blog pages. So we can always in the instructions or in the chat we can say, "You can just name it and just give a vague example, okay?" So it kind of pulls data from here. Whatever data you will upload, it will kind of pull it from here.

**Sucheta Biswas:** Like we were talking about adding the meeting notes and stuff. So you can upload those meeting files over there, meeting recordings, and then we can generate that, fetch the meeting notes or what is the sentiment analysis of the client from those notes. Things like that.

**Tiandra Burns:** And we can put the link or the URL to the file or to the video here, is that correct?

**Sucheta Biswas:** Again, you can put some URLs. So some URLs are fine, where you ask it to comb certain URLs and stuff like that. But the only URLs that won't work are like the doc URLs, like these ones.

**Tiandra Burns:** That's good to know.

**Sucheta Biswas:** It will only work if you have a personal account, if you have an account where the Gmail ID is connected. So here, the Gmail ID is the pod account, right? So we don't have access to that. So it can't fetch. Otherwise, you could have just uploaded it from Google Drive. So you have to upload from device, or you can just add text content, stuff like that.

**Sucheta Biswas:** Okay, so this is mine, but I'm still like learning. But I'll just show you what a Claude F account looks like. You're using Claude a lot.

**Tiandra Burns:** That for Abnormal, yeah?

**Sucheta Biswas:** Yeah, especially post-processing because the internal linking is very, very difficult. Also, we have 404 errors. So when it combs those links and gives me the article with the internal links, actually, I'll just show you how it kind of gave me the result. This is what I generated. And earlier, like we use a lot of internal links in Abnormal. You can see the link. But so many times it's just wrong. This is really fine. See, this is the wrong link. So I have like remove it manually. So when I click on this and this has come up with a lot of training and post-processing and things like that. Yeah, there are a lot of 404 errors. So I make all this, but I just need to clean this up. So I just go clean it here and add my own links. And also I need to record this.

**Tiandra Burns:** So like, you can do multiple things in here that way, yeah. Because, yeah, because Atlas' internal link is completely broken for me, it doesn't work as much as it should. Yeah, sorry. After the writing guidelines are put in, once it generates, I forget what it generates before then, the brief. I go in the brief and comb through and get rid of all the stats that I think will hallucinate. And I go in and put in parentheses like specifically hyper source, blah blah blah. And then when it generates the outline, I'm able to go in and do more cleaning. So now when it comes to post-processing, I've been able to shave a lot of time now because I'm not allowing the AI to even have a chance to generate anything that's going to make my life complicated.

**Sucheta Biswas:** The internal links are good.

**Tiandra Burns:** Um, internal links are pretty good for me. The only thing is because some of our links are newer, right? And it hasn't caught up because I know what I wrote last week. I go in and manually still add those links. But in general, it does really good linking internally. And it doesn't do such a bad job anymore externally with the statistics. But I do go in, and I think manual linking in some regard, at least for now, has to happen just to maximize the SEO potential. You know what I mean? So it's like, I know the content I'm writing and I know I can grab this link from here. So, but ultimately, I don't have as many links in mine as you have to have in yours. I have a lot less.

**Sucheta Biswas:** Correct, because for Jakub's pod, I'm doing a one-one project. So it kind of has like five, six internal links, and they're all generated by Atlas. So it's completely fine. It's only for Abnormal where we have to insert a lot of different links and kind of re-writing. Then, as you said, I have to manually check which were the earlier published articles this week. So I kind of like to bring in those freshness as well. So, yeah, but because I have uploaded that document there in Atlas, my task is now only to edit the links and not like keep on adding. So it kind of saves some time there. So it's good.

**Sucheta Biswas:** Like for example, some link is there on some keyword. So I just go there and I'm like, okay, I know here I have to put the link. So I don't have like comb the keyword also. So that is where I've like saved my time.

**Tiandra Burns:** That's helpful. So I'll probably, I don't know, I guess I need to figure out why I can't get into Claude or what the heck's going on here. So I can actually like add some things in here.

**Sucheta Biswas:** And you can always like ask fans or Nana Marines for a Claude F account. This is Claude F, right? So you can see how like their prompts are very, very detailed. That's what he said. And see, this is very short. This one is short. This is for one of them. But article editor, but they have the instructions over here.

**Sucheta Biswas:** So I was telling you, right, that you can give very brief ones over here, but you can add the detail. And I'm sure this has been added. I forgot where the addition happens, but you can basically kind of collect everything. And there's one button which you click, and then it kind of converts into this text format, which you can add to the files.

**Sucheta Biswas:** Instructions. Like, basically, you ask Claude to generate all the instructions that you have added in the past, because you're even training it, right? And those instructions, you kind of save it over here in files format. So you can have a writing guidelines, you can have a company context, you can have so many different things. And from here only, I got the idea of how you can use it for different stuff.

**Sucheta Biswas:** So let's see, they have created one for comments collector. They have some keyword research stuff also going on. And then they have an article editor, artifact operator. So it's so many different things you can just go on and experiment with and this one I really, really liked.

**Sucheta Biswas:** So what I did is I just took this one up and asked Claude to generate the same one for Abnormal. So it was like kind of detailed and it has stuff like empathetic listening and editorial standards, accuracy first, right? So objectivity, integrity, all of this. So you got to like learn so many different things. Whenever you're doing your research also, you just need to put minimal stuff over here and then Claude to return it.

**Sucheta Biswas:** And we had something similar for Abnormal's research also, which I kind of fetched from ChatGPT. And I want to fetch like we didn't do Claude because for all this industry articles and stuff, I need like fresh stats every time. And I feel that going into Perplexity and keeping on asking it to generate different statistics or different examples, very tiring and cumbersome. So I just want Claude to like do the task for me. So let's see how it's all in the experiments.

**Sucheta Biswas:** Because sometimes I do spend a lot of time in research, like really thorough research so that one good example comes in for one article.

**Tiandra Burns:** I was having that same thing. And what I do is as I find like, if the stat isn't already in our Notion, because we have a Notion I think you guys have a Notion too of all the stats you use and where they're from. So any new stat I get, I add it to the Notion doc. That way, but then it's still kind of, you have to type in the word, find stat, you know, so, but luckily it's a lot easier. I've simplified my process a little bit. So I'm super happy about that. But thank you so much for showing me what you've done in Claude.

**Tiandra Burns:** And I guess, I don't know who I need to get a hold of, but I need to get a hold of someone so I can figure out how I can get into Claude because I don't know what's going on.

**Sucheta Biswas:** Yusuf is your man. Yusuf, that's right. Yeah. Cool. And thanks for the research thing in motion.

**Sucheta Biswas:** So what we have in Abnormal is we have all these different reports. So this IBM report is FBI reports. And we have a couple of them which I have memorized. And it's, again, it's also part of the internal linking and things. But more than statistics, what we really need are those examples. But it's a very good idea to kind of save some of it in a document and then upload it. I use that idea.

**Sucheta Biswas:** The thing with Abnormal is sometimes I feel, you know, it's so varied, I feel that we need kind of different statistics every time or every couple of articles. You can't keep on saying that data breaches happen with 2.2 million or whatever. So if it's 10 articles and 10 articles have the same statistics, it kind of gets monotonous. So I need figure something out.

**Sucheta Biswas:** And the research generator on custom GPT, it kind of also is to fetch those particular codes and stuff from customer stories or different white papers and case studies and stuff. So I don't know if that's the same case with that because every again, everything is very different.

**Sucheta Biswas:** Are you also working on Immubit? You have Immubit?

**Tiandra Burns:** Yes, I'm with Immubit and mostly the post-processing for me in this Claude project would really have to deal with Immubit. It's that's the one mostly. Tag, like, it's very, we don't really do like with Tag and Immubit, we don't really do like customer quotes or things like that, or case studies right now. So it's mostly about with Immubit, it's mostly about the statistics, at least having one or two statistics and having good examples. And then with Tag, it's honestly just about promoting their tours. So they already, you know, we already have their documentation and all of that there. So after learning it, it's more straightforward. I feel like I'm not, I don't have to do a lot of external things, luckily with them, and I don't have to include so many links.

**Tiandra Burns:** So now that I've been working, what, like a month and a half, maybe, like it's really dialed in. And sometimes it just depends on how Atlas wants to behave that day or not. But as long as I'm being more focused and it's coming a lot better and faster for me. So I'm very lucky. I think some clients might be further away from being able to be at that quick pace. Getting it quick, but hopefully, hopefully, all of us can get there. I just, I guess I got lucky with Immubit and Tag that they're more straightforward. And again, Mariana is just awesome with being like, "Let's add this to the doc, get this to the doc."

**Sucheta Biswas:** I agree. I was going to experiment with the artifact where you have the CTAs. So it's more, for Abnormal, it's more of like, you know, "Book a demo" or "Get a personalized demo." What about you? Do you have customer CTAs in artifacts or how is it?

**Tiandra Burns:** Yeah, we do have, I think we have a list of them in there somewhere in the writing instructions and the artifacts. And for maybe for Tag and for Immubit, yeah, I think we have them. And so far, it does really great with doing the call to actions. I don't have to tweak it or nothing. I just might make sure that the link is properly added. Sometimes it might skip that. But so far, Atlas does really good in doing good call to actions. And even if I have to revise it and I say, like, "Reframe this to not mention this or this," it does really great in reframing it. So great on the call to actions. And it's just the getting it to link better, which I think at time it's getting better at linking. For me, it's again, having to make sure that what it generates at the beginning, I just have to kind of go out and delete some things and just don't even let it try to generate certain things in the beginning.

**Tiandra Burns:** So yeah, I've gotten lucky to be able to figure those things out.

**Sucheta Biswas:** That's really, we should talk more of things. You know, I got some ideas from you, got some ideas from me. So.

**Tiandra Burns:** And you're working, like, you're always like in experimental phase and I'm not, I'm not there yet in everything. So like certain things here.

**Sucheta Biswas:** Yeah, and I have this habit of, you know, like, putting all my fingers in the project. So whenever I read something on it, this is the reason why I do a lot of research. Because if I'm doing something, I want to just get deep into it. And then I kind of get something else. And I give those ideas to Mariana that, hey, you know, this is what's happening in the industry, why don't we write about this and stuff. So we can't endlessly write of the same thing all over, especially with cybersecurity, which is kind of an always evolving domain. So that and tech, like, you can't be complacent, you can't just rely on again, one stat and stuff.

**Tiandra Burns:** And that's really interesting from client to client, because Abnormal is going to be like always updating, always current, whereas, you know, Tag, they're not going to be so, there's not going to be so much to update there, you know, or so much going on. So it's really interesting who's going to need more updating and refreshes and more research than others.

**Sucheta Biswas:** I think that's interesting. But yeah, I'm just going to also experiment more on Atlas and see because this should ideally take 15 minutes, the post-processing. It should not take more than that. So the aim is to like scale, get better, write more quality also give more output. So yes, yeah. But to get into Claude, do get into our account, do it into Panzer's account also and see what kind of prompts there was. You know, there are some certain things which will not like strike us at all. Like thinking logically we are so used to always editing, editing. We're just thinking that editors are more, that you wanted to make this better we will not ask you to think logically or think like a CEO or stuff like that. So yeah, okay, will do. Thank you for your time. We didn't even have to use the whole hour and yeah I appreciate it. All good and you can always feel free to reach out to me anytime you want to have a discussion. We can always ask.

**Sucheta Biswas:** If one is busy, otherwise he will have joined or, you know, we can all three have a chat or something.

**Sucheta Biswas:** Sounds like a plan. Let me know how it goes. And if you need any other help for logging in where I can come in, just let me know. If you want to sit and, you know, do those prompts with me together, all in.

**Tiandra Burns:** Thank you. Have a good day.

**Sucheta Biswas:** Bye, Tiandra.

**Tiandra Burns:** Bye.

**Sucheta Biswas:** Bye.
