# Topics Overview

The schedule is preliminary and subject to changes!

The reading for each _lecture_ is given as references to the sources the respective lectures base on. You are **not** obliged to read anything. However, you are strongly **encouraged** to read references marked by pin emojis 📌: those are comprehensive overviews on the topics or important works that are beneficial for a better understanding of the key concepts. For the pinned papers, I also specify the pages span for you to focus on the most important fragments. Some of the sources are also marked with a popcorn emoji 🍿: that is misc material you might want to take a look at: blog posts, GitHub repos, leaderboards etc. (also a couple of LLM-based games). For each of the sources, I also leave my **subjective** estimation of how important this work is for **this specific** topic: from yellow 🟡 _'partially useful'_ though orange 🟠 _'useful'_ to red 🔴 '_crucial findings / thoughts_'. These estimations will be continuously updated as I revise the materials.

For the _labs_, you are provided with practical tutorials that respective lab tasks will mostly derive from. The core tutorials are marked with a writing emoji ✍️; you are **asked** to inspect them **in advance** (better yet: try them out). On lab sessions, we will only **briefly recap** them so it is up to you to prepare in advance to keep up with the lab.

_Disclaimer_: the reading entries are no proper citations; the bibtex references as well as detailed infos about the authors, publish date etc. can be found under the entry links.

_____________________________________________________________________________

## Block 1: Intro


### Week 1

<a name="2204"></a>
#### 22.04. _Lecture_: LLMs as a Form of Intelligence vs LLMs as Statistical Machines

That is an introductory lecture, in which I will briefly introduce the course and we'll have a warming up discussion about different perspectives on LLMs' nature. We will focus on two prominent outlooks: LLM is a form of intelligence and LLM is a complex statistical machine. We'll discuss differences of LLMs with human intelligence and the degree to which LLMs exhibit (self-)awareness.

**Key points**:
* Course introduction
* Different perspectives on the nature of LLMs 
* Similarities and differences between human and artificial intelligence
* LLMs' (self-)awareness

**Core Reading**:
* 📌 [The Debate Over Understanding in AI's Large Language Models](https://arxiv.org/abs/2210.13966) (pages 1-7), `Santa Fe Institute` 🟠
* [Meaning without reference in large language models](https://arxiv.org/abs/2208.02957), `UC Berkeley & DeepMind` 🔴
* [Dissociating language and thought in large language models](https://arxiv.org/abs/2301.06627) (intro [right after the abstract, see more on the sectioning in this paper at the bottom of page 2], sections 1, 2.3 [_LLMs are predictive ..._], 3-5), `The University of Texas at Austin et al.` 🔴

**Additional Reading**:
* [Do Large Language Models Understand Us?](https://direct.mit.edu/daed/article/151/2/183/110604/Do-Large-Language-Models-Understand-Us), `Google Research` 🟠
* [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (chapters 1-8 & 10), `Microsoft Research` 🟡
* [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜](https://dl.acm.org/doi/abs/10.1145/3442188.3445922) (paragraphs 1, 5, 6.1), `University of Washington et al.` 🟡
* [Large Language Models: The Need for Nuance in Current Debates and a Pragmatic Perspective on Understanding](https://arxiv.org/abs/2310.19671), `Leiden Institute of Advanced Computer Science & Leiden University Medical Centre` 🟡

<a name="2404"></a>
#### 24.04. _Lecture_: LLM & Agent Basics

In this lecture, we'll recap some basics about LLMs and LLM-based agents to make sure we're on the same page. 

**Key points**:
* LLM recap
* Prompting
* Structured output
* Tool calling
* Piping & Planning

**Core Reading**:
* [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223), (sections 1, 2.1, 4.1, 4.2.1, 4.2.3-4.2.4, 4.3, 5.1.1-5.1.3, 5.2.1-5.2.4, 5.3.1, 6) `Renmin University of China et al.` 🔴
* [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682), `Google Research, Stanford, UNC Chapel Hill, DeepMind`
* ["We Need Structured Output": Towards User-centered Constraints on Large Language Model Output](https://arxiv.org/abs/2404.07362), `Google Research & Google`
* 📌 [Agent Instructs Large Language Models to be General Zero-Shot Reasoners](https://arxiv.org/abs/2310.03710) (pages 1-9), `Washington University & UC Berkeley`

**Additional Reading**:
* [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), `OpenAI`
* [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903), `Google Research`
* [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783), `Meta AI`
* [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/), `OpenAI`
* [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935), `Renmin University of China et al.`
* [ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920), `Huawei Noah’s Ark Lab et al.`
* [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761), `Meta AI`
* [Granite-Function Calling Model: Introducing Function Calling Abilities via Multi-task Learning of Granular Tasks](https://arxiv.org/abs/2407.00121), `IBM Research`
* 🍿 [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html), `UC Berkeley` (leaderboard)
* [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549), `University of Science and Technology of China & Tencent YouTu Lab`

_____________________________________


### Week 2

<a name="2904"></a>
#### 29.04. _Lab_: Intro to LangChain

The final introductory session will guide you through the most basic concepts of LangChain for the further practical sessions.

**Reading**:
* [Runnable interface](https://python.langchain.com/docs/concepts/runnables/), `LangChain`
* [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/#should-i-use-lcel), `LangChain`
* [Messages](https://python.langchain.com/docs/concepts/messages/), `LangChain`
* [Chat models](https://python.langchain.com/docs/concepts/chat_models/), `LangChain`
* [Structured outputs](https://python.langchain.com/docs/concepts/structured_outputs/), `LangChain`
* [Tools](https://python.langchain.com/docs/concepts/tools/), `LangChain`
* [Tool calling](https://python.langchain.com/docs/concepts/tool_calling/), `LangChain`

#### 01.05.
_Ausfalltermin_

_____________________________________________________________________________

## Block 2: Core Topics


## Part 1: Business Applications


### Week 3

<a name="0605"></a>
#### 06.05. _Lecture_: Virtual Assistants Pt. 1: Chatbots

The first core topic concerns chatbots. We'll discuss how chatbots are built, how they (should) handle harmful requests and you can tune it for your use case.

**Key points**:
* LLMs alignment
* Memory
* Prompting & automated prompt generation
* Evaluation

**Core Reading**:
* 📌 [Aligning Large Language Models with Human: A Survey](https://arxiv.org/abs/2307.12966) (pages 1-14), `Huawei Noah’s Ark Lab`
* [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560), `University of Washington et al.`
* [A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications](https://arxiv.org/abs/2402.07927), `Indian Institute of Technology Patna, Stanford & Amazon AI`

**Additional Reading**:
* [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), `OpenAI`
* [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862), `Anthropic`
* [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501), `Renmin University of China & Huawei Noah’s Ark Lab`
* [Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174), `UC Santa Barbara & Microsoft Research`
* [From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models](https://arxiv.org/abs/2401.02777), `Beike Inc.`
* [Automatic Prompt Selection for Large Language Models](https://arxiv.org/abs/2404.02717), `Cinnamon AI, Hung Yen University of Technology and Education & Deakin University`
* [PromptGen: Automatically Generate Prompts using Generative Models](https://aclanthology.org/2022.findings-naacl.3/), `Baidu Research`
* [Evaluating Large Language Models. A Comprehensive Survey](https://arxiv.org/abs/2310.19736), `Tianjin University`

<a name="0805"></a>
#### 08.05. _Lab_: Basic LLM-based Chatbot
> On material of [session 06.05](#0605)

In this lab, we'll build a chatbot and try different prompts and settings to see how it affects the output.

**Reading**:
* ✍️ [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/), `LangChain`
* ✍️ [LangGraph Quickstart: Build a Basic Chatbot](https://langchain-ai.github.io/langgraph/tutorials/introduction/) (parts 1, 3), `LangGraph`
* ✍️ [How to add summary of the conversation history](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/), `LangGraph`
* [Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/), `LangChain`
* [Few-shot prompting](https://python.langchain.com/docs/concepts/few_shot_prompting/), `LangChain`

_____________________________________


### Week 4

<a name="1305"></a>
#### 13.05. _Lecture_: Virtual Assistants Pt. 2: RAG

Continuing the first part, the second part will expand scope of chatbot functionality and will teach it to refer to custom knowledge base to retrieve and use user-specific information. Finally, the most widely used deployment methods will be briefly introduced. 

**Key points**:
* General knowledge vs context
* Knowledge indexing, retrieval & ranking
* Retrieval tools
* Agentic RAG

**Core Reading**:
* 📌 [Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach](https://arxiv.org/abs/2407.16833) (pages 1-7), `Google DeepMind & University of Michigan`
* [A Survey on Retrieval-Augmented Text Generation for Large Language Models](https://arxiv.org/abs/2404.10981) (pages 1-19), `York University`

**Additional Reading**:
* [Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks](https://arxiv.org/abs/2412.15605), `National Chengchi University & Academia Sinica`
* [Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity](https://arxiv.org/abs/2403.14403), `Korea Advanced Institute of Science and Technology`
* [Querying Databases with Function Calling](https://arxiv.org/abs/2502.00032), `Weaviate, Contextual AI & Morningstar`
* [Auto-RAG: Autonomous Retrieval-Augmented Generation for Large Language Models](https://arxiv.org/abs/2411.19443), `Chinese Academy of Sciences`

<a name="1505"></a>
#### 15.05. _Lab_: RAG Chatbot
> On material of [session 13.05](#1305)

In this lab, we'll expand the functionality of the chatbot built at the last lab to connect it to user-specific information.

**Reading**:
* [How to load PDFs](https://python.langchain.com/docs/how_to/document_loader_pdf/), `LangChain`
* [Text splitters](https://python.langchain.com/docs/concepts/text_splitters/), `LangChain`
* [Embedding models](https://python.langchain.com/docs/concepts/embedding_models/), `LangChain`
* [Vector stores](https://python.langchain.com/docs/concepts/vectorstores/), `LangChain`
* [Retrievers](https://python.langchain.com/docs/concepts/retrievers/), `LangChain`
* ✍️ [Retrieval augmented generation (RAG)](https://python.langchain.com/docs/concepts/rag/), `LangChain`
* ✍️ [LangGraph Quickstart: Build a Basic Chatbot](https://langchain-ai.github.io/langgraph/tutorials/introduction/) (part 2), `LangGraph`
* ✍️ [Agentic RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/), `LangGraph`
* [Adaptive RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/), `LangGraph`
* [Multimodality](https://python.langchain.com/docs/concepts/multimodality/), `LangChain`
_____________________________________


### Week 5

<a name="2005"></a>
#### 20.05. _Lecture_: Virtual Assistants Pt. 3: Multi-agent Environment

This lectures concludes the Virtual Assistants cycle and directs its attention to automating everyday / business operations in a multi-agent environment. We'll look at how agents communicate with each other, how their communication can be guided (both with and without involvement of a human), and this all is used in real applications.

**Key points**:
* Multi-agent environment
* Human in the loop
* LLMs as evaluators
* Examples of pipelines for business operations

**Core Reading**:
* 📌 [LLM-based Multi-Agent Systems: Techniques and Business Perspectives](https://arxiv.org/abs/2411.14033) (pages 1-8), `Shanghai Jiao Tong University & OPPO Research Institute`
* [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442), `Stanford, Google Research & DeepMind`

**Additional Reading**:
* [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325), `MIT & Google Brain`
* [Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View](https://arxiv.org/abs/2310.02124), `Zhejiang University, National University of Singapore & DeepMind`
* [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155), `Microsoft Research et al.`
* 🍿 [How real-world businesses are transforming with AI — with more than 140 new stories](https://blogs.microsoft.com/blog/2025/03/10/https-blogs-microsoft-com-blog-2024-11-12-how-real-world-businesses-are-transforming-with-ai/), `Microsoft` (blog post)
* 🍿 [Built with LangGraph](https://www.langchain.com/built-with-langgraph), `LangGraph` (website page)
* [Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant](https://arxiv.org/abs/2502.01390), `Delft University of Technology & The University of Queensland`

<a name="2205"></a>
#### 22.05. _Lab_: Multi-agent Environment
> On material of [session 20.05](#2005)

This lab will introduce a short walkthrough to creation of a multi-agent environment for automated meeting scheduling and preparation. We will see how the coordinator agent will communicate with two auxiliary agents to check time availability and prepare an agenda for the meeting.

**Reading**:
* ✍️ [Multi-agent network](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/), `LangGraph`
* ✍️ [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/), `LangGraph`
* [Plan-and-Execute](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/), `LangGraph`
* [Reflection](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion/), `LangGraph`
* ✍️ [Multi-agent supervisor](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/), `LangGraph`
* [Quick Start](https://microsoft.github.io/autogen/stable//user-guide/core-user-guide/quickstart.html), `AutoGen`

_____________________________________


### Week 6

<a name="2705"></a>
#### 27.05. _Lecture_: Software Development Pt. 1: Code Generation, Evaluation & Testing

This lectures opens a new lecture mini-cycle dedicated to software development. The first lecture overviews how LLMs are used to generate reliable code and how generated code is tested and improved to deal with the errors.

**Key points**:
* Code generation & refining
* Automated testing
* Generated code evaluation

**Core Reading**:
* [Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977), `Fudan University, Nanyang Technological University & University of Illinois at Urbana-Champaign`
* 📌 [CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning](https://arxiv.org/abs/2207.01780) (pages 1-20), `Salesforce Research`
* [The ART of LLM Refinement: Ask, Refine, and Trust](https://arxiv.org/abs/2311.07961), `ETH Zurich & Meta AI`

**Additional Reading**:
* [Planning with Large Language Models for Code Generation](https://arxiv.org/abs/2303.05510), `MIT-IBM Watson AI Lab et al.`
* [Code Repair with LLMs gives an Exploration-Exploitation Tradeoff](https://arxiv.org/abs/2405.17503), `Cornell, Shanghai Jiao Tong University & University of Toronto`
* [ChatUniTest: A Framework for LLM-Based Test Generation](https://arxiv.org/abs/2305.04764), `Zhejiang University & Hangzhou City University`
* [TestART: Improving LLM-based Unit Testing via Co-evolution of Automated Generation and Repair Iteration](https://arxiv.org/abs/2408.03095), `Nanjing University & Huawei Cloud Computing Technologies`
* [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374), `OpenAI
* 🍿 [Code Generation on HumanEval](https://paperswithcode.com/sota/code-generation-on-humaneval), `OpenAI` (leaderboard)
* [CodeJudge: Evaluating Code Generation with Large Language Models](https://arxiv.org/abs/2410.02184), `Huazhong University of Science and Technology & Purdue University`

#### 29.05.
_Ausfalltermin_

_____________________________________


### Week 7

<a name="0306"></a>
#### 03.06. _Lecture_: Software Development Pt. 2: Copilots, LLM-powered Websites

The second and the last lecture of the software development cycle focuses on practical application of LLM code generation, in particular, on widely-used copilots (real-time code generation assistants) and LLM-supported web development.

**Key points**:
* Copilots & real-time hints
* LLM-powered websites
* LLM-supported deployment
* Further considerations: reliability, sustainability etc.

**Core Reading**:
* 📌 [LLMs in Web Development: Evaluating LLM-Generated PHP Code Unveiling Vulnerabilities and Limitations](https://arxiv.org/abs/2404.14459) (pages 1-11), `University of Oslo`
* [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856), `Google DeepMind & The University of Tokyo`
* [Can ChatGPT replace StackOverflow? A Study on Robustness and Reliability of Large Language Model Code Generation](https://arxiv.org/abs/2308.10335), `UC San Diego`

**Additional Reading**:
* [Design and evaluation of AI copilots -- case studies of retail copilot templates](https://arxiv.org/abs/2407.09512), `Microsoft`
* 🍿 [Your AI Companion](https://blogs.microsoft.com/blog/2025/04/04/your-ai-companion/), `Microsoft` (blog post)
* [GitHub Copilot](https://github.com/features/copilot), `GitHub` (product page)
* 🍿 [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/), `GitHub` (blog post)
* 🍿 [Cursor: The AI Code Editor](https://www.cursor.com), `Cursor` (product page)
* [Automated Unit Test Improvement using Large Language Models at Meta](https://arxiv.org/abs/2402.09171), `Meta`
* [Human-In-the-Loop Software Development Agents](https://arxiv.org/abs/2411.12924), `Monash University, The University of Melbourne & Atlassian`
* [An LLM-based Agent for Reliable Docker Environment Configuration](https://arxiv.org/abs/2502.13681), `Harbin Institute of Technology & ByteDance`
* [Learn to Code Sustainably: An Empirical Study on LLM-based Green Code Generation](https://arxiv.org/abs/2403.03344), `TWT GmbH Science & Innovation et al.`
* [Enhancing Large Language Models for Secure Code Generation: A Dataset-driven Study on Vulnerability Mitigation](https://arxiv.org/abs/2310.16263), `South China University of Technology & University of Innsbruck`

<a name="0506"></a>
#### 05.06 _Lab_: LLM-powered Website
> On material of [session 03.06](#0306)

In this lab, we'll have the LLM make a website for us: it will both generate the contents of the website and generate all the code required for rendering, styling and navigation.

**Reading**:
* see [session 22.05](#2205)
* ✍️ [HTML: Creating the content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content), ``MDN``
* ✍️ [Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started), ``MDN``

_____________________________________


### Week 8: Having Some Rest

#### 10.06.
_Ausfalltermin_

#### 12.06.
_Ausfalltermin_

_____________________________________


### Week 9

<a name="1706"></a>
#### 17.06. _Pitch_: RAG Chatbot
> On material of [session 06.05](#0605) and [session 13.05](#1305)

The first pitch will be dedicated to a custom RAG chatbot that the _contractors_ (the presenting students, see the [infos about Pitches](./Formats/Pitches.md)) will have prepared to present. The RAG chatbot will have to be able to retrieve specific information from the given documents (not from the general knowledge!) and use it in its responses. Specific requirements will be released on 22.05.

**Reading**: see [session 06.05](#0605), [session 08.05](#0805), [session 13.05](#1305), and [session 15.05](#1505)

#### 19.06.
_Ausfalltermin_

_____________________________________


### Week 10

<a name="2406"></a>
#### 24.06. _Pitch_: Handling Customer Requests in a Multi-agent Environment
> On material of [session 20.05](#2005)

In the second pitch, the _contractors_ will present their solution to automated handling of customer requests. The solution will have to introduce a multi-agent environment to take off working load from an imagined support team. The solution will have to read and categorize tickets, generate replies and (in case of need) notify the human that their interference is required. Specific requirements will be released on 27.05.

**Reading**: see [session 20.05](#2005) and [session 22.05](#2205)

<a name="2606"></a>
#### 26.06. _Lecture_: Other Business Applications: Game Design, Financial Analysis etc.

This lecture will serve a small break and will briefly go over other business scenarios that the LLMs are used in. 

**Key points**:
* Game design & narrative games
* Financial applications
* Content creation

**Additional Reading**:
* [Player-Driven Emergence in LLM-Driven Game Narrative](https://arxiv.org/abs/2404.17027), `Microsoft Research`
* [Generating Converging Narratives for Games with Large Language Models](https://aclanthology.org/2024.games-1.6/), `U.S. Army Research Laboratory`
* [Game Agent Driven by Free-Form Text Command: Using LLM-based Code Generation and Behavior Branch](https://arxiv.org/abs/2402.07442), `University of Tokyo`
* 🍿 [AI Dungeon Games](https://play.aidungeon.com), `AI Dungeon` (game catalogue)
* 🍿 [AI Town](https://www.convex.dev/ai-town), `Andreessen Horowitz & Convex` (game)
* [Introducing NPC-Playground, a 3D playground to interact with LLM-powered NPCs](https://huggingface.co/blog/npc-gigax-cubzh?utm_source=chatgpt.com), `HuggingFace` (blog post)
* [Blip](https://github.com/bliporg/blip), `bliporg` (GitHub repo)
* [gigax](https://github.com/GigaxGames/gigax), `GigaxGames` (GitHub repo)
* [Large Language Models in Finance: A Survey](https://arxiv.org/abs/2311.10723), `Columbia & New York University`
* [FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications](https://arxiv.org/abs/2403.12285), `Imperial College London & MIT`
* [Equipping Language Models with Tool Use Capability for Tabular Data Analysis in Finance](https://arxiv.org/abs/2401.15328), `Monash University`
* [LLM4EDA: Emerging Progress in Large Language Models for Electronic Design Automation](https://arxiv.org/abs/2401.12224), `Shanghai Jiao Tong University et al.`
* [Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207), `Stanford`
* [Large Language Models Can Solve Real-World Planning Rigorously with Formal Verification Tools](https://arxiv.org/abs/2404.11891), `MIT, Harvard University & MIT-IBM Watson AI Lab`

_____________________________________________________________________________

## Part 2: Applications in Science


### Week 11

<a name="0107"></a>
#### 01.07. _Lecture_: LLMs in Research: Experiment Planning & Hypothesis Generation

The first lecture dedicated to scientific applications shows how LLMs are used to plan experiments and generate hypothesis to accelerate research.

**Key points**:
* Experiment planning
* Hypothesis generation
* Predicting possible results

**Core Reading**:
* 📌 [Hypothesis Generation with Large Language Models](https://arxiv.org/abs/2404.04326) (pages 1-9), `University of Chicago & Toyota Technological Institute at Chicago`
* 📌 [LLMs for Science: Usage for Code Generation and Data Analysis](https://arxiv.org/abs/2311.16733) (pages 1-6), `TUM`
* [Emergent autonomous scientific research capabilities of large language models](https://arxiv.org/abs/2304.05332), `Carnegie Mellon University`

**Additional Reading**:
* [Improving Scientific Hypothesis Generation with Knowledge Grounded Large Language Models](https://arxiv.org/abs/2411.02382), `University of Virginia`
* [Paper Copilot: A Self-Evolving and Efficient LLM System for Personalized Academic Assistance](https://arxiv.org/abs/2409.04593), `University of Illinois at Urbana-Champaign, Carnegie Mellon University & Carleton College`
* [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://arxiv.org/abs/2408.15545), `University of Science and Technology of China & DP Technology`
* [Mapping the Increasing Use of LLMs in Scientific Papers](https://arxiv.org/abs/2404.01268), `Stanford`

<a name="0307"></a>
#### 03.07: _Lab_: Experiment Planning & Hypothesis Generation
> On material of [session 01.07](#0107)

In this lab, we'll practice in facilitating researcher's work with LLMs on the example of a toy scientific research.

**Reading**: see [session 22.05](#2205)

_____________________________________


### Week 12

<a name="0807"></a>
#### 08.07: _Pitch_: Agent for Code Generation
> On material of [session 27.05](#2705)

This pitch will revolve around the _contractors'_ implementation of a self-improving code generator. The code generator will have to generate both scripts and test cases for a problem given in the input prompt, run the tests and refine the code if needed. Specific requirements will be released on 17.06.

**Reading**: see [session 27.05](#2705) and [session 05.06](#0506)

<a name="1007"></a>
#### 10.07. _Lecture_: Other Applications in Science: Drug Discovery, Math etc. & Scientific Reliability

The final core topic will mention other scientific applications of LLMs that were not covered in the previous lectures and address the question of reliability of the results obtained with LLMs.

**Key points**:
* Drug discovery, math & other applications
* Scientific confidence & reliability

**Core Reading**:
* 📌 [Can LLMs replace Neil deGrasse Tyson? Evaluating the Reliability of LLMs as Science Communicators](https://arxiv.org/abs/2409.14037) (pages 1-9), `Indian Institute of Technology`

**Additional Reading**:
* [A Comprehensive Survey of Scientific Large Language Models and Their Applications in Scientific Discovery](https://arxiv.org/abs/2406.10833), `University of Illinois at Urbana-Champaign et al.`
* [Large Language Models in Drug Discovery and Development: From Disease Mechanisms to Clinical Trials](https://arxiv.org/abs/2409.04481), `Department of Data Science and AI, Monash University et al.`
* [LLM-SR: Scientific Equation Discovery via Programming with Large Language Models](https://arxiv.org/abs/2404.18400), `Virginia Tech et al.`
* 🍿 [Awesome Scientific Language Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models), `yuzhimanhua` (GitHub repo)
* [CURIE: Evaluating LLMs On Multitask Scientific Long Context Understanding and Reasoning](https://arxiv.org/abs/2503.13517), `Google et al.`
* [Multiple Choice Questions: Reasoning Makes Large Language Models (LLMs) More Self-Confident Even When They Are Wrong](https://arxiv.org/abs/2501.09775), `Nanjing University of Aeronautics and Astronautics et al.`

_____________________________________________________________________________

## Block 3: Wrap-up


### Week 13

<a name="1507"></a>
#### 15.07. _Pitch_: Agent for Web Development
> On material of [session 03.06](#0306)

The _contractors_ will present their agent that will have to generate full (minimalistic) websites by a prompt. For each website, the agent will have to generate its own style and a simple menu with working navigation as well as the contents. Specific requirements will be released on 24.06.

**Reading**: see [session 03.06](#0306) and [session 05.06](#0506)

<a name="1707"></a>
#### 17.07. _Lecture_: Role of AI in Recent Years

The last lecture of the course will turn to societal considerations regarding LLMs and AI in general and will investigate its role and influence on the humanity nowadays.

**Key points**:
* Studies on influence of AI in the recent years
* Studies on AI integration rate
* Ethical, legal & environmental aspects

**Core Reading**:
* 📌 [Protecting Human Cognition in the Age of AI](https://arxiv.org/abs/2502.12447) (pages 1-5), The University of Texas at Austin et al.
* 📌 [Artificial intelligence governance: Ethical considerations and implications for social responsibility](https://onlinelibrary.wiley.com/doi/full/10.1111/exsy.13406) (pages 1-12), `University of Malta`

**Additional Reading**:
* [Augmenting Minds or Automating Skills: The Differential Role of Human Capital in Generative AI's Impact on Creative Tasks](https://arxiv.org/abs/2412.03963), `Tsinghua University & Wuhan University of Technology`
* [Human Creativity in the Age of LLMs: Randomized Experiments on Divergent and Convergent Thinking](https://arxiv.org/abs/2410.03703), `University of Toronto`
* [Empirical evidence of Large Language Model's influence on human spoken communication](https://arxiv.org/abs/2409.01754v1), `Max-Planck Institute for Human Development`
* 🍿 [The 2025 AI Index Report: Top Takeaways](https://hai.stanford.edu/ai-index/2025-ai-index-report), `Stanford`
* [Growing Up: Navigating Generative AI’s Early Years – AI Adoption Report: Executive Summary](https://ai.wharton.upenn.edu/focus-areas/human-technology-interaction/2024-ai-adoption-report/), `AI at Wharton`
* [Ethical Implications of AI in Data Collection: Balancing Innovation with Privacy](https://arxiv.org/abs/2503.14539), `AI Data Chronicles`
* [Legal and ethical implications of AI-based crowd analysis: the AI Act and beyond](https://link.springer.com/article/10.1007/s43681-024-00644-x), `Vrije Universiteit`
* [A Survey of Sustainability in Large Language Models: Applications, Economics, and Challenges](https://arxiv.org/abs/2412.04782v1), `Cleveland State University et al.`

_____________________________________


### Week 14

<a name="2207"></a>
#### 22.07. _Pitch_: LLM-based Research Assistant
> On material of [session 01.07](#0107)

The last pitch will introduce an agent that will have to plan the research, generate hypotheses, find the literature etc. for a given scientific problem. It will then have to introduce its results in form of a TODO or a guide for the researcher to start off of. Specific requirements will be released on 01.07.

**Reading**: see [session 01.07](#0107) and [session 03.07](#0307)

<a name="2407"></a>
#### 24.07. _Debate_: Role of AI in Recent Years + Wrap-up
> On material of [session 17.07](#1707)

The course will be concluded by the final debates, after which a short Q&A session will be held.

Debate topics:
* LLM Behavior: Evidence of Awareness or Illusion of Understanding?
* Should We Limit the Usage of AI?

**Reading**: see [session 17.07](#1707)