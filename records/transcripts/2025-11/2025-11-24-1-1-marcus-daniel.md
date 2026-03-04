# 1:1 Marcus + Daniel

<metadata>
date: 2025-11-24
time: 17:31 UTC
duration: 33 minutes
organizer: Daniel Lopes (GrowthX)
participants: Marcus Derencius, Daniel Lopes
fathom_recording_id: 103913221
fathom_url: https://fathom.video/calls/484082652
share_url: https://fathom.video/share/Am9z9tfzh1unsvKZuQ2Ev2GyTMzUPvhy
source: fathom
enriched_on: 2026-03-02 00:45 UTC
</metadata>

---

## Summary

Daniel outlined a major engineering team restructure designed to scale delivery: assigning junior engineers to Engagement Managers to handle client accounts while Marcus and Nico focus on architectural decisions, code review, and complex projects like Zapier and Lovell integrations. Kirkland would transition to Team Lead role coordinating the junior engineers and supporting recruiting, accommodating his personal commitments. The hiring strategy hinges on open-sourcing the `output.space.dev` framework and using take-home assignments as the primary filter for candidates with strong automation and content skills, with Marcus joining the technical interview panel.

---

## Context

This is an internal 1:1 between Daniel Lopes (GrowthX CEO/Founder) and Marcus Derencius (Senior Engineer), discussing the near-term engineering team structure as GrowthX scales client delivery. The conversation addresses current bottlenecks: client feedback delays stalling task completion, senior engineers stretched thin on multiple accounts, and a need to hire and onboard new engineers quickly. Daniel is seeking Marcus's feedback and buy-in before announcing the restructure to the broader team. The meeting also covers Marcus's highly efficient development workflow (using CloudCode for planning, CodeX for execution) and the `FlowCli Debug` tool—powerful internal capabilities that will shape how junior engineers are trained.

---

## Relevance

**To GrowthX Delivery:**
- New team structure (junior engineers paired with Engagement Managers, seniors focused on architecture/review) directly addresses slow client feedback loops and task completion delays that currently stall delivery.
- Hiring junior engineers with SEO/content background and basic coding skills (not full-stack engineers) represents a shift in hiring profile—focus on automation + content skills over deep code expertise.
- Open-sourcing `output.space.dev` framework and using take-home assignments as hiring filter will both accelerate onboarding and improve quality of new hires on the framework from day one.
- Marcus's CloudCode-CodeX workflow and parallel task management pattern will become training template for new junior engineers; `FlowCli Debug` tool will be integrated into the public framework for visibility into agent behavior and costs.

**To GrowthX Business Development:**
- Kirkland's transition to Team Lead role (away from pure engineering) reflects his high client-facing value; repositioning him to support recruiting, sales prep, and planning mitigates risk of key relationships depending on his availability while accommodating his personal commitments.
- New structure supports expansion from ~7 accounts per EM to handling higher client count by decoupling relationship ownership (EMs) from technical execution (junior engineers).

**Organizational Notes:**
- Léo Stefan hired as Chief of Staff Engineer (QA + Full Stack background from ThoughtWorks) to support Kirkland with recruiting and meeting load—builds organizational capacity for scaling.
- Marcus flagged concern about Kirkland's occasional disappearance in meetings and slower code review cycles; Daniel aware of personal/family treatment issues affecting Kirkland's capacity.

---

## Overview

- **Proposed Restructure:** A new model assigns junior engineers to Engagement Managers (EMs) for client accounts. Senior engineers (Marcus, Nico) will provide high-level support, code review, and lead complex projects.
- **New Kirkland Role:** Kirkland is proposed as Team Lead for the junior engineers. This leverages his client-facing skills and frees him from deep coding while accommodating personal commitments.
- **Hiring Strategy:** The new `output.space.dev` framework will be open-sourced. Take-home assignments using it will serve as a key filter for hiring junior engineers with strong automation and content skills.
- **Workflow Efficiency:** Marcus's workflow (using CloudCode for planning, CodeX for execution) is highly efficient. The `FlowCli Debug` tool is also a powerful asset for analyzing agent activity and HTTP requests.

---

## Key Topics

### Current Challenges

  - **Client Feedback Delays:** Slow feedback stalls tasks and risks clients abandoning the platform for manual workarounds.
  - **Task Management:** The current system is effective for organizing meetings but less so for driving asynchronous task completion.
  - **Senior Engineer Availability:**
      - **Kirkland:** High client-facing value but often unavailable for deep coding due to personal matters.
      - **Nico:** Strong technically but focused on large projects, leading to minor bugs in daily work.

### Proposed Team Restructure

  - **Goal:** Create a scalable engineering team by leveraging diverse skill sets.
  - **New Roles & Structure:**
      - **Engagement Managers (EMs):** Client-facing relationship owners (7–8 accounts each).
      - **Junior Engineers:** Assigned to EMs; focus on automation and content.
          - **Profile:** Strong content/SEO background, some coding experience (e.g., Next.js, Vercel).
      - **Senior Engineers (Marcus, Nico):**
          - High-level technical support and architectural decisions.
          - Code review for junior engineers.
          - Lead complex projects (e.g., Zapier, Lovell API agent) for 1–2 months, then hand off to a junior engineer.
      - **Kirkland (Proposed Team Lead):**
          - Coordinate junior engineers and manage their onboarding.
          - Act as a technical liaison for sales and client planning.
      - **Léo Stefan (Chief of Staff Engineer):**
          - Full-stack engineer with a QA background.
          - Can support Kirkland with recruiting and meeting attendance.

### Hiring & Onboarding

  - **Hiring Funnel:**
      - The new `output.space.dev` framework will be open-sourced.
      - Take-home assignments using the framework will be the primary technical filter.
  - **Interview Process:**
      - Marcus will join the technical interview panel to review take-home assignments.
      - **Candidate Profile:** A current candidate (technical SEO PM at UOL) fits the ideal profile, having built an AI automation agency with Zapier and Make.

### Developer Workflow & Tools

  - **Marcus's Workflow:**
      - Uses CloudCode for initial planning, then CodeX to refine the plan and execute the task.
      - Manages multiple parallel tasks by instructing the AI to avoid files used in other sessions.
  - **`FlowCli Debug` Tool:**
      - A powerful internal tool for analyzing agent activity, HTTP requests, and costs.
      - Daniel proposes integrating it into the public `output.space.dev` framework.

---

## Action Items

- **Daniel (GrowthX):** Announce Kirkland's new Team Lead role to the team.
- **Daniel (GrowthX):** Add Marcus to the technical interview panel for take-home assignment reviews (especially for new candidate from UOL with SEO/AI automation background).
- **Marcus (GrowthX):** Provide feedback on the `output.space.dev` framework's user experience, including Docker setup issues and complexity for end users.
- **Marcus (GrowthX):** DM Daniel privately about any issues with Clint (regarding code contributions and collaborative approach).

---

## Transcript
**Marcus Derencius:** Thank you.

**Daniel Lopes:** E aí, cara, beleza?

**Marcus Derencius:** E aí, tudo bem?

**Daniel Lopes:** Bom, deixa eu fechar a porta.

**Daniel Lopes:** Olha, a câmera, quando eu levanto, ela sai.

**Daniel Lopes:** Pede o foco.

**Daniel Lopes:** Pede o foco automático.

**Marcus Derencius:** É que nem consegui seguir.

**Daniel Lopes:** Agora funciona.

**Daniel Lopes:** Massa.

**Marcus Derencius:** Dá aflição isso, nossa.

**Daniel Lopes:** E aí, cara, como é que estão as coisas?

**Daniel Lopes:** Beleza?

**Marcus Derencius:** Tá bom, bem, tá bem, eu sei.

**Daniel Lopes:** Tá.

**Daniel Lopes:** Tranquilo, tentando...

**Daniel Lopes:** Como é que é?

**Marcus Derencius:** Tá gorda aí, porra?

**Daniel Lopes:** Pois é.

**Daniel Lopes:** Tá foda.

**Daniel Lopes:** Comecei a fazer o Zwift de novo todo dia e agora...

**Daniel Lopes:** Sem Zwift é foda, porque mesmo como eu moro num lugar legal, tipo, o tempo fica assim, né?

**Daniel Lopes:** Deixa eu tirar o blur.

**Marcus Derencius:** Ah, acabou.

**Daniel Lopes:** A gente pega fogo aqui constante, tipo, três dias da semana, mas sobre aqueles sete dias, uns três, assim, quatro dias, nublado de manhã.

**Daniel Lopes:** Fogo, frio para caramba. E o Zwift resolve a desculpa.

**Daniel Lopes:** Não tem desculpa.

**Marcus Derencius:** Um brother que tava aqui fazendo...

**Daniel Lopes:** De lá de fora, né?

**Marcus Derencius:** Não, eu ia falar que um brother que tava aqui fazendo o kite comigo no fim de semana.

**Marcus Derencius:** Ele tem uma loja de bike da Trek em Campinas, assim.

**Marcus Derencius:** Ele é representante da Trek e faz todos os rolés de bike pela...

**Daniel Lopes:** Ah, mas pelo Brasil.

**Marcus Derencius:** Ele falou que vai agora lá, onde você foi lá na Espanha?

**Daniel Lopes:** Ah, em Girona?

**Marcus Derencius:** É.

**Daniel Lopes:** Em Girona, legal.

**Daniel Lopes:** A gente estava tentando decidir para onde é que a gente vai agora, porque chegou a tirar do dia 20 ao dia 28, que a Kátia tem férias também.

**Daniel Lopes:** E a estava tentando decidir onde é que a gente ia, eu estava querendo ir para a Europa, mas a gente acabou decidindo ir para a Bahia.

**Daniel Lopes:** Mas eu estava aqui em Girona, a Espanha.

**Daniel Lopes:** Agora é dezembro?

**Daniel Lopes:** É, mas está frio, né?

**Daniel Lopes:** Você está em Portugal?

**Marcus Derencius:** Não, ainda estou aqui no Ceará, no Brasil, mas vou para Portugal em duas semanas.

**Marcus Derencius:** É, mas está frio lá, e dá para pedalar, né?

**Daniel Lopes:** Mas é o mesmo tempinho daí, assim.

**Daniel Lopes:** É, mas não dá para entrar na água, né?

**Daniel Lopes:** A gente vai...

**Marcus Derencius:** É a mesma temperatura, é frio, né?

**Marcus Derencius:** Aqui, onde tem borracha.

**Daniel Lopes:** Já vai.

**Daniel Lopes:** A gente vai pro Big Island, tentar fazer o desculpa-drive em Cosmanta Reis lá.

**Marcus Derencius:** Então, acho que é melhor do que engolir um frio na Europa, né?

**Marcus Derencius:** É, eu tô frio essa época lá, porque teve chuva forte e tudo.

**Marcus Derencius:** Ah, mas tem que ir lá, onde eu tô lá, tem muita bicicleta lá.

**Daniel Lopes:** Como é que é nome do lugar que tá vendo?

**Marcus Derencius:** Eu sempre esqueço.

**Marcus Derencius:** Perto de Porto, chama Viana do Castelo.

**Daniel Lopes:** Viana do Castelo.

**Marcus Derencius:** Aí eu aluguei uma P de dois quartos lá.

**Marcus Derencius:** Tem um hotel de bike lá, chama Fio Viana.

**Daniel Lopes:** Acho que você me mandou, é aquele que você me mandou o link, né?

**Marcus Derencius:** É, é.

**Marcus Derencius:** Tem vários.

**Marcus Derencius:** Os caras que fazem o tour de Portugal, vai lá no café, quando eu tomo café, os caras vão lá tomar café.

**Marcus Derencius:** Os caras com a roupa de bike, sabe?

**Daniel Lopes:** Aí trabalhando e os caras treinando.

**Marcus Derencius:** Treinando.

**Daniel Lopes:** Sobre café direto?

**Marcus Derencius:** Ah, não, vou pela manhã, aí eu tomo café, fico até o almoço, aí a tarde volto pra cá.

**Marcus Derencius:** Porque as cadeiras são ruins, então não tô podendo trabalhar num lugar que tem cadeira ruim, que a bomba fica do seu lado.

**Daniel Lopes:** Como é que tá o serviço?

**Daniel Lopes:** Como é que você tá o workload aí?

**Marcus Derencius:** É, eu tô empolgado, então eu tô trabalhando pra caramba, mas...

**Daniel Lopes:** Tá interessante as coisas que você tá fazendo e tal, ou tá...

**Marcus Derencius:** Tá, não, eu gosto, assim. É chato quando tem que fazer muita reunião com os clientes, que é a parte mais difícil. O resto vai bem. Tudo que é de código da Fathomax já tá ótimo, mas às vezes reunião com o cliente tem que discutir. O Kirkland faz isso melhor. Coisas de conteúdo sem ser via código. Obrigado.

**Marcus Derencius:** Eu fico usando CloudCode, CodeX para tudo. Qualquer coisa que eu não tenho que usar, aí fica mais lento.

**Daniel Lopes:** É, foda, né, cara?

**Daniel Lopes:** Como é que é o seu workflow?

**Daniel Lopes:** Você está usando o VCLI only e aí você deixa ele codar as tasks ou você usa o planning mode e tal?

**Marcus Derencius:** É, então, algumas eu já sei quando ele faz bem, aí eu mando ele fazer, eu vou acompanhando e me intervenho no meio do caminho. Aí outras vezes, eu mando ele, porque o CodeX é melhor para planning. Então eu mando o CloudCode escrever o plan e o CodeX para revisar e refinar o plan. E aí eu falo para o CodeX executar depois. Eu mando salvar no arquivo o texto, né?

**Daniel Lopes:** Ah, não tentei isso ainda. Eu faço o mesmo fluxo de criar o plan file primeiro, mas eu nunca tentei usar o CodeX para revisar. Eu estou fazendo tudo dentro do VS Code Extension com o Code.

**Marcus Derencius:** Eu nem abro o Cursor só, eu faço o review no Pool Request só. Então eu fico com três sessões abertas às vezes. Você está fazendo uma coisa, vejo que tem algum bug, já vou colocando na outra aba.

**Daniel Lopes:** Encontro esse bug na outra aba do terminal.

**Marcus Derencius:** É, é.

**Daniel Lopes:** Como é que você faz vários branches no mesmo computador? Não tem como, né?

**Marcus Derencius:** É, então eu falo para ele, tem outra alteração em processo, não faz commit. Escreve aí, analisa. Mas eu ia fazer os Git Worktrees para usar com Flow, né? Fazer um kill separado para configurar o temporal, mas ainda não fiz.

**Daniel Lopes:** Ah, gostaria, fácil, é.

**Marcus Derencius:** Obrigado.

**Daniel Lopes:** Acho que duas tarefas no mesmo projeto é meio difícil, mas se for coisa pequena, dá para fazer e separar o commit depois.

**Marcus Derencius:** É, é o que eu tenho mais feito, principalmente quando é bem separado, porque às vezes vou lá ver porque alguma coisa falhou num workflow que demora meia hora para rodar. Aí eu falo, deixa separado, aviso outra sessão, não mexe nesses arquivos, aí ele consegue trabalhar em separado, não ficar bagunçando. E se o Research deu pau em alguma coisa, eu mando rodar de novo, e faz em paralelo, mas faço coisa bem separada.

**Daniel Lopes:** Como é que tá de quantidade de trampo?

**Daniel Lopes:** Você tá com um monte de testes?

**Marcus Derencius:** Tem bastante trabalho. Não, eu fiquei esperando o feedback do pessoal e o pessoal não dá o feedback, ou demora três dias para dar, aí acabo dispersando e esquecendo que tinha a tarefa ali. Então essa parte que eu estou fazendo um esquema para fazer um follow-up no pessoal, para eles revisar. Tenho uma preocupação que se alguma coisa não está boa, não fica bom em uma tentativa, os editores desistem de usar e vão tudo para o CloudCode direto. Eles me dão feedback, falam que está ok, a tarefa fica lá parada. Tem bastante trabalho, algumas coisas é rápido de arrumar, outras que o cara escreve uma linha só, mas é um negócio gigante de coisa.

**Daniel Lopes:** Como é que tem sido trabalhar com o estilo?

**Marcus Derencius:** É, assim, ela é correta, faz bem, tem média interação durante os ciclos. Nas reuniões é boa quando tem aquela reunião de terça-feira, que aí discute as coisas e tudo mais. Esse follow-up das tarefas, que às vezes a Andy faz, dá bronca no pessoal. Ela ajuda a organizar, ajuda a discutir, às vezes tem que conversar com o pessoal antes da reunião, então vem bem. Ela organiza bem as tarefas e prioriza tudo durante as reuniões, mas fora do ciclo, está tudo independente.

**Daniel Lopes:** O que eu estou pensando em fazer, é tipo, o motivo que eu estou querendo conversar com você é para pegar o feedback seu, porque a gente está pensando em fazer, ter aquela, acho a gente tocou de leve na, ah, você não está no Rio, mas a gente está, teve o All Hands semana passada, e no All Hands a gente está falando, a ideia é ter tipo, engagement managers, vão ser responsáveis pela interação com o cliente, saca?

**Daniel Lopes:** E é aquele, pessoa é fixa com o cliente constante, então a gente está mudando, pegando quem tem afinidade para conversar com o cliente, manter relacionamento, essas coisas, e mudar o role, ao invés de ser relacionado a conteúdo e tal, ser um role.

**Daniel Lopes:** de Engagement Manager, e cada Engagement Manager teria mais ou menos umas 7 a 8 contas, e aí o que a está pensando é ter um engineer para cada Engagement Manager, quase que, não precisa ser 100% alocado, mas maior parte do tempo alocado dentro daquelas contas, saca?

**Daniel Lopes:** Então, mesmo se não tiver nada para fazer, tipo, eu vou ficar tentando achar as coisas para melhorar e tal, e aí o que a gente estava tentando, o que eu estava pensando em fazer é ter essa leva de como vai ser muita gente, te imagina que seja 7, para tocar 60 contas, então, tipo, mais ou menos 7 pessoas, tem que ter 7 grupos, e aí o que eu estava pensando em fazer é ter essa layer de gente que é mais junior, saca?

**Daniel Lopes:** e com um profile mais de automation, está aprendendo a fazer, está aprendendo a codar agora, tipo, estilo do Kirkland, assim, mas o Kirkland já está nisso há mais tempo, né, então ele já sabe

**Daniel Lopes:** Eu acordar mais, já sabia, já entendi as coisas bem mais do que o pessoal que a tá achando, mas a gente fez uma offer pra um programador, por exemplo, que ele é copywriter e editor, com um skill bem legal, assim, de conseguir fazer as coisas bonitinhas, UI design e tal, e fez um monte de produto ele mesmo, assim, tipo o solopreneur, e tem background em SEO e content marketing, sabe?

**Daniel Lopes:** E fazendo os produtos tudo em XJS, vibecoded, mas ele entende o código, sabe?

**Daniel Lopes:** Ele pede pra ele fazer o walkthrough do código e tal, ele sabe o que tá acontecendo, ele tá aprendendo já tem três anos, e o modelo que eu tô pensando seria ter, tipo, você e o Nico como special projects e review, code review dessa galera, sabe?

**Daniel Lopes:** Só pra eu não...

**Daniel Lopes:** As decisões mais técnicas, os projetos mais difíceis, assim, ter opinião sua, mesmo que vocês não cobrem...

**Daniel Lopes:** Um projeto inteiro, meio que support, imagina que vai ter o Zapier, Zapier é super complicado do ponto de vista de SEO, talvez vai ter que fazer um site para eles, ou no caso do Lovell, por exemplo, que o Nico teve que codar um agent que conversa com o back and forth com API dele, sabe?

**Daniel Lopes:** Tipo, o ideal seria alocar vocês nesses projetos assim por um tempo, sei lá, um ou dois meses, e aí fazer o handoff junto com um dos juniors para os caras entenderem o vocês estão fazendo, e aí vocês voltam para o high level e eles continuam com aquela conta, saca?

**Daniel Lopes:** E não sei se faz sentido, e aí outra coisa que eu estava pensando em colocar o Kirkland, que o Kirkland ainda precisa do review sales, saca?

**Daniel Lopes:** A ideal seria vocês terem a oportunidade de revisar o código deles, the architecture decision, essas coisas, das coisas maiores, mas ele tem bastante habilidade de treinar essa galera, de criar o onboard.

**Daniel Lopes:** De entrevistar eles e tal.

**Daniel Lopes:** E tem a ideia toda de SEO.

**Daniel Lopes:** Ele meio que tem o horizontal T-shape ali.

**Daniel Lopes:** Mesmo que o T-shape dele é mais raso, o horizontal SKUs dele é bem bom.

**Marcus Derencius:** Então eu estava pensando em fazer de...

**Marcus Derencius:** é de conteúdo, né?

**Daniel Lopes:** Pois é.

**Daniel Lopes:** E eu estava pensando em fazer de team lead, saca?

**Daniel Lopes:** De team lead.

**Daniel Lopes:** Não seria senior engineer acima de vocês, mas coordenar essa galera toda, saca?

**Daniel Lopes:** E tem vocês dois de proper technical support, technical engineering, architectural decisions, essas coisas.

**Daniel Lopes:** Não sei se faz sentido.

**Marcus Derencius:** Faz.

**Marcus Derencius:** até algo que eu...

**Marcus Derencius:** O cliente tem um elogio dele, então ele encaixa bem, ele conversa bem com os clientes, de elaborar a ideia de alguma solução mais nova, que ele consegue fazer essa parte bem.

**Marcus Derencius:** Não duro só.

**Marcus Derencius:** É que às vezes ele parece que ele fica muito ocupado, preso com algum cliente, que às vezes tem semana que ele um pouco...

**Daniel Lopes:** Desaparece.

**Marcus Derencius:** Desaparece.

**Marcus Derencius:** até, só isso que eu ia até dizer para...

**Marcus Derencius:** Assim, eu falo, nossa, tem semana que eu...

**Marcus Derencius:** Assim que ele só pede um código review, sei lá, cada duas semanas, ele pede para quase todos, né?

**Marcus Derencius:** Então, não sei se alguma coisa está travando ele, né?

**Marcus Derencius:** Então, mas...

**Marcus Derencius:** Mas é isso, eu acho que ele faz bem isso, ele conversa bem com os clientes, de planejar os workflows ou pipeline, o que mudar.

**Marcus Derencius:** Então, eu acho isso bem...

**Marcus Derencius:** Muito bom dele, ele...

**Marcus Derencius:** Principalmente dos agentes pipelines, ele que está fazendo bastante das revisões.

**Marcus Derencius:** ele...

**Marcus Derencius:** Como está funcionando...

**Marcus Derencius:** Até por isso que eu acho legal essa ideia de ter um pessoal mais júnior, ajuda bem, porque os workflows vão ficar bem sólidos, assim você mais ajusta do que fica mexendo no código. A gente faz pouca coisa, fica lá só testando o workflow que funciona sem ter que mexer no código fonte dele. Essa parte é onde o Camilo está fazendo muito bem, de ficar lá testando os workflows manualmente. Se tiver mais gente que tenha bastante desse conteúdo, entender de conteúdo mais do que tecnicamente. Porque está ficando mais fácil as coisas da parte de coisas avançadas. Vai fazer integração com o CMS, essas coisas. Depois que está pronto, vai fácil, o próprio Cloud Code consegue ajustar, arrumar um monte de bug técnico. Mas essa parte do conteúdo que eu fico lá tentando automatizar, para tentar melhorar os inputs.

**Daniel Lopes:** Mas essa parte é difícil.

**Marcus Derencius:** É, faz sentido.

**Daniel Lopes:** Aí, à medida que a gente for lançar o... Eu não sei se você acompanhou o código do output.space no GitHub de migration, que eles estão migrando os workflows para o output.

**Marcus Derencius:** Até foi tentar usar o output, rodar, mas não conseguiu. Não, não foi fácil, não.

**Daniel Lopes:** Quando que você tentou fazer?

**Marcus Derencius:** Foi na semana passada, acho.

**Daniel Lopes:** Ah, na semana passada?

**Daniel Lopes:** Ok.

**Daniel Lopes:** Eu vou conversar com os caras daqui a pouco.

**Daniel Lopes:** Mas a ideia seria fazer ele ficar bem simples, que aí você roda output.space.dev, roda local, e a gente faria open source. E a gente consegue começar a mandar os take-homes no codebase do output, e pedir o pessoal para quem conseguir escrever os workflows legal no framework, a gente contrata. Ano que vem, janeiro, a gente tem um time. Estou entrevistando uma menina hoje do Brasil, uma PM de SEO technical para a UOL, que abriu uma agência de AI automation usando Zapier e Make. Ela escreveu um código bem legal. Vou te adicionar nas entrevistas para a parte técnica. Eu estava fazendo a parte técnica até então, o Kirkland fazendo a parte de SEO, e Steve fazendo a parte de Culture Fit e PM, mas se a gente for acelerar esse plano, seria legal ter você no processo. Fazer o technical interview, revisar o assessment e take-home deles. Ficam esses três lá.

**Marcus Derencius:** É, até para ver, eu quero usar todo o output novo, pensando como o usuário final vai usar. Se alguma coisa ficar muito difícil, instalei o Docker aqui, rodando, já deu os paus. Já tinha um tempdir antigo, que deu conflito, ele ficou travando. Então tem que colocar mais comando para resetar as coisas.

**Daniel Lopes:** Dá o feedback para os caras lá no canal.

**Marcus Derencius:** É, então eu vou começar a testar e começar a colocar esses feedbacks.

**Daniel Lopes:** Eu não tentei usar ainda, vou tentar usar essa semana. Eu estou tentando sair do CheckThat, estou meio que agarrado nele, mas vou tentar sair dele essa semana, e semana que vem eu mudo para o output. E para o ContentOS, para o Atlas, para a versão nova do Atlas, que vai ter um monte de coisa.

**Daniel Lopes:** Mas, então, você acha que é tranquilo eu fazer o announcement do Kirkland para o time? Não tem nenhuma oposição?

**Marcus Derencius:** Não, não, eu acho que é muito bom. Ele realmente faz muito bem esse papel.

**Daniel Lopes:** É uma coisa só que ele está ocupado. Esse é um dos motivos que eu estou querendo fazer ele ficar num job mais horizontal, mais associado a recrutamento, sales, planning ahead, fazer o technical prepping para os clientes que é possível, fazer o pitch do que não é possível. Porque eu acho que ele está lidando com um monte de coisa pessoal, familiar, que está complicando a vida dele. Ele me deu o toque, pediu para eu não comentar com ninguém.

**Marcus Derencius:** Entendo, a família dele está começando esse tratamento.

**Marcus Derencius:** Eu gosto muito dele, gosto de trabalhar, só não tem quem está para frente.

**Daniel Lopes:** Ele falou alguma coisa ou você percebeu só de observar?

**Daniel Lopes:** É isso que eu queria conversar com você.

**Marcus Derencius:** Sim, nas últimas duas reuniões ele falava meio ausente, mais desconectado. Eu gosto muito dele, é só para isso, só para cuidar bem.

**Daniel Lopes:** Eu estava falando com ele, a gente pode fazer isso como um test run. Se não tiver dama, se tiver muito workload, a gente volta ele para o role normal. Eu contratei o Léo Stefan, que era da ThoughtWorks, de Porto Alegre, amigo do Neto, como Chief of Staff Engineer. Ele tem background de QA também, mas é Full Stack Engineer, mudou de QA para Full Stack nos últimos 10 anos. Aí eu posso pedir ele para ajudar com acompanhar meetings, recruiting process, dividir o load com Kirkland. Ele está lidando com coisas pessoais, mas preocupado que não está conseguindo focar em tarefa de coding mais hardcore. Mas ao mesmo tempo ele tem esse valor de qualquer meeting que entra com o cliente, ele consegue explicar para o time o que fazer. O board dessa galera também, sabe? Pessoal que foi do role dele para a programadora.

**Marcus Derencius:** É, foi a mesma coisa do Sentinel One. Eu entrei depois, que já tinha o Nico, aí eu entrei mais tímido, tentando entender as coisas antes de falar. Depois que eu entendi, tudo bem. No começo estava meio perdido. Mas depois, ok, foi bem, né? Faz sentido.

**Daniel Lopes:** O que você acha do Nico?

**Marcus Derencius:** Tecnicamente é bom. Mas ele faz umas coisas bastante avançadas. No dia a dia, tirando dos projetos que ele está full time, vejo pouco. Ele está muito ocupado com as coisas de logo. Tem muito bugzinho do dia a dia que eu vou lá e arrumo rápido, porque às vezes ele não está disponível. Ele é muito bom tecnicamente.

**Daniel Lopes:** Essa é uma das coisas que eu quero pedir para Léo para olhar mais também, acompanhar o progresso da galera no dia a dia. O Marcus é meio óbvio, tipo, 50 PRs, merges por semana, o resto do time.

**Marcus Derencius:** Se você olha lá no GitHub Insights, está 20 vezes mais.

**Daniel Lopes:** É um bom. Então tá, cara, eu queria só pegar a sua opinião, o seu feedback.

**Marcus Derencius:** Cloud Code é muito bom, fico aqui fazendo as coisas.

**Daniel Lopes:** A gente tem que fazer um curso desse negócio, sabe? O que estava querendo fazer é pedir o Léo fazer um curso público de como usar essas coisas. Você vê a galera usando, mas o pessoal não usa no mesmo nível. Não fazem o plano, revisar o plano, pedir para executar, acompanhar. O pessoal está só ali ainda no task. Porque estão usando como Hub Co-Pilot style.

**Marcus Derencius:** É. Um amigo também que é programador falou, "Como é que você usa? Você não acha horrível?". Falei, "Porra, estou aqui usando, não faço mais nada". Só fico mandando aqui o CloudCode.

**Daniel Lopes:** Energy all day.

**Marcus Derencius:** Tem o FlowCli Debug agora. Faz um debug dos seus negócios ali. Pega cada activity que ele fez, analisa entre um e outro.

**Daniel Lopes:** A gente tem que migrar isso para depois que terminar essa versão do output. O único motivo de não investir muito naquilo é que se tiver um monte de gente fazendo, seria problema. Mas quando a gente terminar o framework, a gente pode começar a fazer a parte pública. Ter o debugger ali dentro, como se fosse um command line tipo "output space debug". Que a gente vai ter o trace na final. A gente tem cenários de trace. Cada vez que ele roda, ele salva o trace inteiro, não só com as activities, mas também os HTTP requests. Então você consegue ver onde é que falhou, o custo das coisas, se a ex-API voltou errado, etc. Vai conseguir divulgar bem.

**Daniel Lopes:** Vou lá porque tem outra reunião agora, mas valeu pelo feedback. Eu vou tentar agendar mais 1-on-1s com a galera breve.

**Marcus Derencius:** Está tranquilo, eu sei que você está ocupado. Eu estou aqui, fico me segurando para não ficar mexendo no código dos caras tudo aqui.

**Daniel Lopes:** Então, beleza. Mudando esse profile, mudando essa estrutura do time, tendo esse monte de gente, é exatamente isso que você vai ter que fazer, sabe? Você vai ser o indivíduo mais experiente que vai estar fazendo essas interfaces com os dois lados.

**Marcus Derencius:** É, vou ver se o Clint não vai ficar mexendo no saco.

**Daniel Lopes:** Ele é bem conservador, né?

**Marcus Derencius:** Tudo tá grande. Uma má vontade de estabelecer.

**Daniel Lopes:** Me manda essa conversa quando você vê que está ensinando algo. Me manda DM em privado, só para eu acompanhar.

**Marcus Derencius:** Deixa tudo público agora, todas as coisas eu coloco, ele vai lá, puxa de mão em público.

**Daniel Lopes:** Coloca público, mas me manda via DM só para eu acompanhar, porque ele tem esse profile. Para open source project é uma coisa, mas para entrar no project é foda.

**Marcus Derencius:** Tá bom, mano. Então tá. Falou, tchau.
