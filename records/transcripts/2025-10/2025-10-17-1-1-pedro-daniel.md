# 1:1 Pedro + Daniel

<metadata>
date: 2025-10-17
time: 16:31 UTC
duration: 30 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes (GrowthX), Pedro Steimbruch
fathom_recording_id: 95025773
fathom_url: https://fathom.video/calls/443942481
share_url: https://fathom.video/share/sHoxb86wcohuibbHs-yy-3Tc-cixi96U
source: fathom
enriched_on: 2025-03-02 19:45 UTC
</metadata>

---

## Summary

Daniel and Pedro discussed Pedro's database optimization work on the IGP project (handling 5M+ records), with a focus on Postgres performance tuning and exploring TimescaleDB and DuckDB alternatives to load 3 months of data in 4-5 seconds. They reviewed the strategic landscape — two existential threats (AI Visibility companies moving into content creation and WearOps executing GrowthX's roadmap) — and aligned on Content Inventory and CheckThat as critical projects to scale services and defend market position. Pedro expressed strong motivation to grow professionally within GrowthX and flagged some process gaps around project pitches; Daniel confirmed Pedro's performance is strong with positive feedback from the team and noted the company will establish clearer role definitions once operations stabilize in November.

---

## Context

Pedro joined GrowthX in late June/early July as a Product Engineer, working on the IGP (internal client) project. This is his second project at the company; he's been in the role for approximately 4 months and has built strong working relationships across the team, with Daniel noting positive feedback from colleagues including George, Rosé, and the GP team. The 1:1 occurred as Daniel was managing a heavy workload during a period of significant strategic pressure — the company was fielding investor interest, had recently faced a funding process that was unexpectedly time-consuming, and was grappling with two simultaneous competitive threats. Pedro's role focuses on backend and performance optimization work; his immediate focus is on database performance optimization for the analytics platform, which is critical infrastructure for GrowthX's product roadmap.

---

## Relevance

**To GrowthX Delivery:**
- Database performance optimization (Postgres, TimescaleDB, DuckDB) is a blocker for shipping analytics features; Pedro's work directly unblocks the IGP and analytics product development.
- The analytics data aggregation capability (full-year historical data, not just 18 months like Google Analytics) is positioned as a competitive differentiator that justifies paid product pricing.
- Daniel highlighted the importance of owning projects through uncertainty, being proactive, and communicating — qualities needed as the team scales and pitches become more detailed.

**To GrowthX Business Development:**
- Content Inventory project is essential to unblock service team scaling — the team has high client demand but insufficient delivery capacity to create content at required volume and quality.
- Competitive context: Profound, AIOps, WearOps, and Surfer SEO are moving aggressively into content creation and analytics; GrowthX's closed-loop offering (opportunities → content creation → analytics → automation) is differentiated but needs to ship before competitors capture market share.
- Pedro is positioned as a potential contributor to CheckThat or Content Inventory in the coming weeks, providing capacity for critical roadmap items.

**To GrowthX Organization:**
- Daniel plans to establish clearer role definitions and levels in November once operational chaos stabilizes; Pedro's interest in growth and current positive performance suggests he's likely candidate for expanded responsibilities.
- The 1:1 revealed process gaps around project pitching (Daniel acknowledged pitches can be underspecified) and communication cadence — Daniel is working on improving systems once workload allows.

---

## Overview

- Pedro is working on optimizing database performance for the IGP project, handling \~5M records/table
- GrowthX faces competitive pressure from AI Visibility companies and WearOps in the content creation space
- Content Inventory and Check That projects are critical for scaling services and defending market position
- Pedro is motivated and seeking opportunities to grow professionally within the company

---

## Key Topics

### Project Updates

  - Pedro's working on 2nd IGP project; relationship is fluid and collaborative
  - Optimizing database (Postgres) for faster dashboard loading (5M+ records/table)
  - Exploring TimescaleDB plugin and potentially DuckDB for performance gains
  - Goal: Load 3 months of data in 4-5 seconds, full year in 10 seconds or less

### Company Strategy and Challenges

  - Two "existential threats" identified:
    1.  AI Visibility companies (e.g., Profound, AIOps) moving into content creation
    2.  WearOps following a similar roadmap to GrowthX
  - Content Inventory project crucial for scaling service team and meeting client demand
  - Check That project needed to compete with AI Visibility companies
  - Balancing rapid development with maintaining product cycles and organization

### Professional Growth and Feedback

  - Pedro expressed desire to grow professionally and become more relevant within GrowthX
  - Daniel noted importance of proactivity, dealing with uncertainty, and ownership in Product Engineering
  - Company considering clearer role definitions and levels in the future
  - Pedro's performance viewed positively; no immediate critical feedback

### Future Projects and Ideas

  - Potential involvement in Content Inventory or Check That projects
  - Pedro's ideas for Assistant feature to edit documents (company artifacts and assignment outputs)
  - Suggestion to survey top Cloud Project users for feature ideas

---

## Action Items

- Pedro to optimize Postgres performance by Monday
- Test TimescaleDB and DuckDB alternatives Tuesday-Thursday
- Daniel to take a week off for management tasks and focus on Content Inventory
- Pedro to write a Notion doc with rough notes on Assistant feature ideas
- Consider sending a questionnaire to top Cloud Project users for feature suggestions
- Daniel to share the pitch for GP's upcoming project with Pedro next week

---

## Transcript
**Pedro Steimbruch:** This meeting is being recorded.

**Pedro Steimbruch:** Today I'm working in a different place.

**Daniel Lopes:** Let me adjust the background here — it's like a blur.

**Pedro Steimbruch:** I'm on the beach. I have a house outside.

**Daniel Lopes:** Onde que é?

**Pedro Steimbruch:** Fica uns 10 minutos da cidade.

**Daniel Lopes:** Qual que é a sua cidade mesmo?

**Pedro Steimbruch:** É Jaguarão — uma cidade pequena, é a fronteira com o Uruguai, bem no sul.

**Daniel Lopes:** Você não tá longe do Nicolas, né?

**Pedro Steimbruch:** Não, pertinho — umas quatro horas.

**Daniel Lopes:** E no mais, como é que tem umas coisas com o teu trampo?

**Pedro Steimbruch:** Cara, eu tô no segundo projeto com o IGP, né?

**Pedro Steimbruch:** Eu curto muito trabalhar com o IGP.

**Pedro Steimbruch:** É muito fluido, a gente se acerta bem e colabora rápido. Ele não me bloqueou em nada, está bem da hora. Óbvio que eu não bloqueei ele em nada também.

**Pedro Steimbruch:** Estou curtindo para caramba, eu consegui dar um gás legal no início do projeto.

**Pedro Steimbruch:** Estou relativamente contente com o resultado do Analytics ali.

**Pedro Steimbruch:** E agora estou trabalhando com dados de produção. Foi um pouco assustador a quantidade de dados vindo — temos uns 5 milhões de registros em cada tabela já.


**Pedro Steimbruch:** Daí hoje eu comecei a fazer um trampo de otimizar o banco e otimizar o nosso padrão de leitura para deixar mais rápido, conseguir montar o dashboard mais rápido.

**Pedro Steimbruch:** Mas tem bastante coisa ainda para fazer. Trabalhei para otimizar a parte de tráfego, agora estou otimizando a parte de Google Search.

**Pedro Steimbruch:** Semana que vem vou testar TimescaleDB, um plugin para Postgres que o Zé compartilhou, para ver como performa. Se eu não conseguir carregar os últimos três meses do Analytics em menos de 4-5 segundos, vou experimentar o DuckDB. Mas estou confiante que otimizando o Postgres e fazendo leituras assíncronas (tudo é síncrono hoje) conseguirei rodar queries pesadas de forma assíncrona e trabalhar com o ano inteiro em 10 segundos ou menos.

**Pedro Steimbruch:** Pretendo terminar a otimização do Postgres na segunda, e terça, quarta e quinta, testar TimescaleDB e DuckDB.

**Daniel Lopes:** Performance sempre dá trabalho. Mas quando você adiciona dados reais é que você vê o que você vai precisar.

**Pedro Steimbruch:** Tô com a conexão um pouco ruim hoje, está travando.

**Daniel Lopes:** Se quiser desligar o vídeo, cara.

**Pedro Steimbruch:** Vou desligar o vídeo, se melhora.

**Daniel Lopes:** Na verdade, a interface com o GP tá ficando bem legal — vai substituir o Luca, é tipo um pivô para o projeto inteiro. O que o Brad tá fazendo, a gente vai usar toda a parte de Analytics no sistema inteiro. Vai fechar o loop usando Analytics — vamos saber quais são as oportunidades. Performance é importante porque é onde sempre dá gargalo, e é uma das coisas que ninguém provê. Google Analytics mesmo não tem data pra mais de 18 meses. O diferencial nosso é que estamos acumulando esses dados — não só Analytics, mas dados das páginas como o Brad fez. Isso sozinho já é valor suficiente para ser um paid product.

**Pedro Steimbruch:** Com certeza a performance vai ser um desafio mantendo os dados por tanto tempo. Mas à medida que avançarmos, vamos investigando e melhorando.

**Daniel Lopes:** Como é que você está? Você está aqui há três meses?

**Pedro Steimbruch:** Talvez mais — entrei no final de junho, início de julho. Então fazendo uns 4 meses.

**Pedro Steimbruch:** Tô bem empolgado com o trabalho. Desde que entrei, venho numa crescente de motivação. Tô bem desafiado, contente com os desafios. Quero crescer profissionalmente e quero crescer aqui dentro — essa é minha intenção. Estou 100% engajado com a empresa.

**Daniel Lopes:** A gente tá super satisfeito que você tá trabalhando aqui. Perguntei ao pessoal e todo mundo gosta de trabalhar com você — Rosé, GP, pessoal do lab. Não sei se tem algum feedback, algo que compartilhar, algo que a gente pode melhorar.

**Pedro Steimbruch:** Posso pensar mais. Sei que você é extremamente ocupado, sempre na correria. Vejo a quantidade de coisa que faz e fico impressionado. Mas o projeto — o pitch principalmente — vem um pouco... eu acho que poderia ser mais elaborado. Não é criticar, óbvio que não.

**Daniel Lopes:** Eu entendo.

**Pedro Steimbruch:** Senti vontade de pegar e propor a questão de websites e connectors para resolver a multiplicidade de APIs de terceiro. Talvez se perdesse mais tempo naquilo, seria uma experiência ruim pra mim. À medida que a gente se adapta com Shape Up e o GP ajuda mais (já que você tá cheio de trabalho), os pitches vão vindo com as pontas mais fechadas.

**Daniel Lopes:** Isso é uma coisa que quero resolver e melhorar — está sendo difícil por questão de workload, mas tendo o roadmap mais planejado e dividindo os times fica mais fácil. O Marcel também está ajudando com product management e UI, essencialmente de CheckThat, então me aliviou. Tem mais alguma coisa que você quer falar?

**Pedro Steimbruch:** Na reunião com o Marcel, percebi que ele esperava uma UI mais opinionated do que a gente quer mostrar pro manager de conteúdo e pro cliente. Pensei: será que o Marcel não deveria ter se envolvido mais no pitch para gerar o valor que gerou no CheckThat? De qualquer forma, é o primeiro ciclo do analytics, então acho que ainda vamos ter tempo para incorporar mais ideias.

**Daniel Lopes:** Sim, esse seria o ideal. É o que estou planejando fazer. Eu e o Marcel fazemos o shaping das coisas praticamente em HTML, e agora que ele está aprendendo Cloud Code, montei um workflow para ele criar coisas táticas dentro do Rails direto, na rota de mockups. O problema com Marcel é que sua visão é 10 steps ahead — a gente tem que trabalhar backwards para caber no escopo viável. E agora, do ponto de vista de competitors, a gente tem dois existential threats acontecendo ao mesmo tempo.

**Daniel Lopes:** A gente não tá em risco, temos renda suficiente, esse mês estamos em break-even. Mas durante o processo de funding tivemos inbound interest de investors — não estávamos procurando e acabou distraindo muito, perdemos quase um mês inteiro fazendo todos os cycles de funding.

**Daniel Lopes:** Várias empresas de AI Visibility estão tendo demanda enorme e começaram a nos olhar como alternativa. Quando estávamos no funding, o Profound e o AIOps pivotaram — o AIOps agora faz AI Visibility Content Creation. Ambos estão tentando fazer full cycle content creation com analytics, todas as ideias que temos. A gente tem que chipar essa parte rápido e tentar bagunçar o mercado — reduzir preço, fazer do jeito mais barato possível, potencialmente a custo mesmo, para deixar a vida deles mais difícil de crescer no nosso espaço.

**Daniel Lopes:** WearOps está executando exatamente nosso roadmap. Temos mais acesso ao que eles estão fazendo — estão totalmente inspirados no que viram a gente fazer, na forma que Marcel apresenta conteúdo nos workshops, nas coisas internas que viram na parceria conosco. O jeito que construímos agents, o domain model, até os nomes e palavras são iguais — no roadmap temos opportunities, assignments. Eles estão executando no mesmo roadmap que a gente. Então temos essas duas coisas acontecendo ao mesmo tempo — a gente tem que agir nisso rápido.

**Daniel Lopes:** Content Inventory é o projeto que vai resolver o problema de scalability da empresa. Temos demanda gigante de clientes mas não conseguimos servir porque o pessoal não consegue criar conteúdo no volume e qualidade necessários. A gente tem que terminar o Content Inventory antes de novembro para os CheckedApp, e independente disso, a gente precisa do Content Inventory para escalar o time de serviço. O time está super agarregado.

**Daniel Lopes:** Estamos sofrendo pra implementar — tem tanta complexidade, domain model, systems thinking direto do jeito que Marcel faz que é praticamente impossível outra pessoa conseguir fazer. Brad, George e Ren não conseguiriam — não têm o acesso direto que tive lidando com esse espaço junto com o Marcel. É um momento bagunçado, mas imagino que novembro pra frente conseguimos começar a ter um product cycle melhor. Novembro também vai ser bagunçado — vamos lançar CheckDepth, mudar várias coisas no Atlas, migrar todos os workflows pro framework novo. Vamos lançar o framework em dezembro. Vai ter muita coisa, mas acho que dá pra manter um product cycle relativamente organizado.

**Pedro Steimbruch:** Faz total sentido. Você me perguntou e isso me instigou — achava que alguns pontos podiam ter sido melhores. Mais uma pegada de retro, assim. Mas entendo completamente. Me sinto à vontade tocando o projeto com as incertezas. Vou assumindo uma grande parte das coisas. O que fico na dúvida, compartilho, mas não tenho problema em tocar incerteza e assumir.

**Daniel Lopes:** Acho que é bem de boa. A qualquer momento que tiver dúvida ou falta de clareza, pode mandar DM. Se me marcar no channel e eu não ver, pode mandar DM — estou sem capacidade de ser proativo por enquanto, tenho que melhorar meus sistemas, mas consigo ser reativo. Então, qualquer coisa dá o grito.

**Pedro Steimbruch:** Quero agregar da melhor forma possível aqui dentro, quero crescer profissionalmente e me tornar mais relevante na empresa. Se tiver feedback para trilhar esse caminho, pra mim tá ótimo.

**Daniel Lopes:** Pra mim não tenho nada. Assim que as coisas estabilizarem em novembro, vou gastar mais tempo com organização dos projetos, organização dos teams e dos roles, começar a adicionar levels mais claros. No geral, o que é bem claro pra mim é a divisão do tipo de trabalho — temos o tipo de trabalho que Kirkland, Marcos e Nico fazem versus Product Engineering, que é o trabalho que vocês estão fazendo (você, GP, Stevon, Rosé, Brad), e a parte do framework é outro tipo.

**Daniel Lopes:** Essas áreas têm necessidades um pouco diferentes. Está ficando mais fácil definir coisas que são importantes. Pro Product Engineering, o que é importante é exatamente o que você e JP estão fazendo — proatividade, lidar com incerteza, cobrir o que não estava claro, comunicar proativamente, ownership. Não tem nada que pula de imediato com feedback crítico por enquanto.

**Pedro Steimbruch:** Tô empolgado pra entregar esse projeto. Sei que semana que vem tem esse trabalho crucial de otimização antes de fazer o roll-out. Aguardo pra ver se vou pro Content Inventory ou ajudar no CheckThat — tô assim, amarrado aí de trabalhar com o José, o cara é muito foda, vai ser da hora colaborar com ele.

**Daniel Lopes:** Mandei uma oferta pra outro cara de BaseC Camp com commits no Reyes — é um cara bom também. Mas de imediato não sei ainda. Próxima semana vou tirar a semana inteira de folga, dando meu role de management e movendo meus one-on-ones pra frente pra avançar mais no Content Inventory. Mas ainda é meio unclear se seria mais vantagem pular no CheckThat ou Content Inventory. O Inventory é bem grande e talvez faça sentido começar por lá, mas se o Marcel aumentou o escopo do CheckThat, talvez faça sentido atacar por lá também. Daqui a semana vou ter uma visão melhor. Ambos são existential risks — se não chipar o Content Inventory, não conseguimos escalar o time de serviços. Se não chipar o CheckThat, os Profound developers vão obter nossa região.

**Pedro Steimbruch:** Estou sentindo a pressão ali. O Brad ontem mostrou o Analytics pra ele. Mostrou um que é praticamente um Atlas — parece bem maduro.

**Daniel Lopes:** Surfer SEO.

**Pedro Steimbruch:** Surfer SEO, acho que é. E aí senti a pressing need de a gente shipar de uma vez.

**Daniel Lopes:** Pra gente, o Inventory é mais... todos esses têm coisas interessantes, mas faltam a possibilidade de não se preocupar com custo. Surfer SEO é bom em otimização — se você coloca uma página, faz scraping e tem oportunidade, mas pra criar oportunidade nova é fraco. Pra otimizar as páginas que você tem, são bem bons. Eles têm scoring, você aperta o botãozinho e ele ajusta. Mas não escaneiam o site inteiro e não têm Google Analytics, só Google Search Console. Nenhum dos players fecha o loop inteiro. Profound adicionou Content Creation com UX legal, mas o gerador do Brief e conteúdo é fraco — só gera Listicles. Acham oportunidade só baseado em LLM prompts, não fecham o ciclo e não têm Analytics.

**Daniel Lopes:** Adicionando Google Analytics também. Todo mundo está faltando fechar o loop — a gente está bem perto. Fez a parte mais difícil primeiro, criar qualquer tipo de conteúdo independente da complexidade. Agora estamos adicionando os Analytics, e a próxima parte é adicionar automatização na estratégia inteira, tanto pra conteúdo novo quanto otimizado. Tenho o plano todo na cabeça, dá pra bater de frente com Surfer SEO e Profound. Está chegando lá. Em uma semana, acho que temos o design todo pronto do sistema inteiro. Ajudo o Brad a terminar a parte de pages e depois fazemos oportunidades e reassign — tracking de quem está mexendo em cada conteúdo. Isso é outra coisa que ninguém pensa — nunca vai ter criação de conteúdo sem expert review. Pra conteúdo técnico precisa de marketplace de gente para revisar com comentários que façam parte da pipeline de melhoria. Não pode ser só mudar context artifacts manualmente, tem que ser automated self-improvement. Vamos começar a pensar nisso em dezembro, quando adicionar mais gente na parte de qualidade.

**Pedro Steimbruch:** Bastante coisa mesmo. Acho que temos que entregar rápido.

**Daniel Lopes:** Esse é o desafio. Mas o progresso do projeto está excelente, cara. Agradeço e vocês lidando bem com falta de clareza. Só pra dar contexto, o GP projeto vai fazer o shaping de um agent pra disparar workflows via MCP, mais parecido com Cloud Code. Quando a gente tiver o pitch mais ou menos organizado semana que vem, te adiciono pra você ver — você tava pensando na Assistant e tem um overlap grande.

**Pedro Steimbruch:** Tenho uma ideia legal pro Assistant — conseguir editar documento. Documento é qualquer artefato (company artifact ou saída do Assignment). A gente poderia ter abstração de documento como qualquer artefato e saída do Assignment, e o Assistant vai saber editar esses documentos, manter o histórico. Tava bem afim de trabalhar uma parada dessas.

**Daniel Lopes:** Se você escrever um Notion Doc com rough notes — não precisa ser detalhado — pra eu e JP dar uma olhada. A gente está pensando mais ou menos parecido. Está super early, nem começamos nada. Tenho umas ideias, JP tem outras. Se colocar as suas, acho que dá pra...

**Pedro Steimbruch:** Vou colocar. Outra ideia que tive é que vi uns caras bons na parte de conteúdo — Hassan é um cara muito esperto, tem um outro rapaz que fez tutorial de como faz Cloud Project. Queria mandar um questionário: o que mais gostam no Cloud Code, o que poderia ter no Cloud Project que não tem, que seria da hora? Pra fazer o nosso Assistant com algumas pegadas que facilitem o trabalho deles.

**Daniel Lopes:** Faz total sentido. Tá certo, cara. Tem mais alguma coisa?

**Pedro Steimbruch:** Não, é isso aí.

**Daniel Lopes:** Valeu, cara. Tchau.
