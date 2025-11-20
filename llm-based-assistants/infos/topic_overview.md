---
title: Topics Overview
---

:::{hide_references}
:::

:::{renderpdf} https://raw.githubusercontent.com/maxschmaltz/Course-LLM-based-Assistants/main/llm-based-assistants/sessions/block1_intro/2310/2310.pdf
:viewer: mozilla
:::


# Topics Overview


* October: INTRO
    * Week 1
        * [22.10. Intro](#2210)
        * [23.10. Lecture: Ontological Status of LLMs](#2310)
    * Week 2
        * [29.10. Lecture: LLM & Agent Basics](#2910)
        * [30.10. Lab: Intro to LangChain](#3010)

* November–December: CORE
    * Week 3
        * [05.11. Lecture: Virtual Assistants](#0511)
        * [06.11. Lab: LLM-based Chatbot](#0611)
    * Week 4
        * [12.11 & 13.11. Labs: RAG](#1211)
    * Week 5
        * [19.11. Lecture: Multi-agent Environment](#1911)
        * [20.11. Lab: Multi-agent Environment](#2011)
    * Week 6
        * [26.11 & 27.11. Labs: LLM-powered Website](#2611)
    * Week 7
        * [03.12 & 04.12. Labs: LLM-powered Research Assistant](#0312)
    * Week 8
        * [10.12. Lecture: Role of AI in Recent Years](#1012)
        * [11.12. Wrap-up](#1112)
    * Week 9
        * [17.12. Debate: Role of AI in Recent Years](#1712)
        * [18.12. Project Proposals](#1812)

* January–February: PROJECTS
    * Weeks 10-13
        * [Project work](#project_weeks)
    * Week 14
        * [04.02 & 05.02. Project Presentations](#0402)


_____________________________________________________________________________



See detailed descriptions if the sessions below.

<div style="font-size:9pt">
    <div class="notes">
        <p><em>Notes</em>:</p>
        <ul>
            <li>This schedule may be changed, should the need arise.</li>
            <li>You are <strong>not</strong> required to read anything. However, you are strongly encouraged to read sources marked by pin emojis 📌: those are comprehensive overviews on the topics or important works that are beneficial for a better understanding of the key concepts.</li>
            <li>Sources marked with a popcorn emoji 🍿 is misc material you might want to take a look at: blog posts, GitHub repos, leaderboards etc.</li>
            <li>For the <em>labs</em>, you are provided with practical tutorials that the respective lab tasks will mostly derive from. The core tutorials are marked with a writing emoji ✍️; you are asked to inspect them in advance (better yet: try them out).</li>
        </ul>
    </div>

_Disclaimer_: the reading entries are no proper citations; detailed infos about the authors, publication date, venue etc. can be found under the entry links.
</div>


_____________________________________________________________________________



## October: INTRO



### Week 1



<a name="2210"></a>
#### 22.10. Intro

That is an introductory meeting, in which I we will cover the contents and the schedule of the course, the class formats and the formalia, and where all your questions, suggestions etc. will be discussed.

**Key points**:
* Course introduction
* Q&A



<a name="2310"></a>
#### 23.10. _Lecture_: Ontological Status of LLMs

This lecture will suggest a warm-up discussion about different perspectives on LLM nature. We will focus on two prominent outlooks: LLM as as a complex statistical machine vs LLM as a form of intelligence. We'll discuss differences of LLM and human intelligence and the degree to which LLMs exhibit (self-)awareness.

**Key points**:
* Different perspectives on the nature of LLMs 
* Similarities and differences between human and artificial intelligence
* LLMs' (self-)awareness

**Sources**:
* 📌 [The Debate Over Understanding in AI's Large Language Models](https://arxiv.org/abs/2210.13966) (pages 1-7), `Santa Fe Institute`
* [Meaning without reference in large language models](https://arxiv.org/abs/2208.02957), `UC Berkeley & DeepMind`
* [Dissociating language and thought in large language models](https://arxiv.org/abs/2301.06627), `The University of Texas at Austin et al.`
* [Do Large Language Models Understand Us?](https://direct.mit.edu/daed/article/151/2/183/110604/Do-Large-Language-Models-Understand-Us), `Google Research`
* [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (chapters 1-8 & 10), `Microsoft Research`
* [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜](https://dl.acm.org/doi/abs/10.1145/3442188.3445922), `University of Washington et al.`
* [Large Language Models: The Need for Nuance in Current Debates and a Pragmatic Perspective on Understanding](https://arxiv.org/abs/2310.19671), `Leiden Institute of Advanced Computer Science & Leiden University Medical Centre`



### Week 2



<a name="2910"></a>
#### 29.10. _Lecture_: _Lecture_: LLM & Agent Basics

In this lecture, we'll recap the basics of LLMs and LLM-based agents to make sure we're on the same page. 

**Key points**:
* What makes an LLM
* Instruction fine-tuning & alignment
* LLM-based agents
* Structured output
* Tool calling
* Piping & Planning

**Sources**:
* [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223), `Renmin University of China et al.`
* [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682), `Google Research, Stanford, UNC Chapel Hill, DeepMind`
* [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783), `Meta AI`
* [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560), `University of Washington et al.`
* [Agent Instructs Large Language Models to be General Zero-Shot Reasoners](https://arxiv.org/abs/2310.03710), `Washington University & UC Berkeley`
* [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), `OpenAI`
* 📌 [Aligning Large Language Models with Human: A Survey](https://arxiv.org/abs/2307.12966) (pages 1-14), `Huawei Noah’s Ark Lab`
* [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), `OpenAI`
* [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862), `Anthropic`
* ["We Need Structured Output": Towards User-centered Constraints on Large Language Model Output](https://arxiv.org/abs/2404.07362), `Google Research & Google`
* 🍿 [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/), `OpenAI`
* [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935), `Renmin University of China et al.`
* [ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920), `Huawei Noah’s Ark Lab et al.`
* [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761), `Meta AI`
* [Granite-Function Calling Model: Introducing Function Calling Abilities via Multi-task Learning of Granular Tasks](https://arxiv.org/abs/2407.00121), `IBM Research`
* 🍿 [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html), `UC Berkeley` (leaderboard)
* [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629), `Princeton University & Google Research`
* [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549), `University of Science and Technology of China & Tencent YouTu Lab`
* [Evaluating Large Language Models. A Comprehensive Survey](https://arxiv.org/abs/2310.19736), `Tianjin University`



<a name="3010"></a>
#### 30.10. _Lab_: Intro to LangChain

This is the first lab which will guide you through the basic concepts of LangChain for the further practical sessions.

**Sources**:
* ✍️ [Models](https://docs.langchain.com/oss/python/langchain/models), `LangChain`
* [Messages](https://docs.langchain.com/oss/python/langchain/messages), `LangChain`



## November-December: CORE



### Week 3



<a name="0511"></a>
#### 05.11. _Lecture_: Virtual Assistants

The first core topic addresses single-LLM virtual assistants such as chatbots and RAG systems. We'll discuss how these systems are built and how you can tune them for your use case.

**Key points**:
* Recap: Prompting
* Memory
* RAG workflow & techniques
* RAG vs long-context LLMs

**Sources**:
* [A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications](https://arxiv.org/abs/2402.07927), `Indian Institute of Technology Patna, Stanford & Amazon AI`
* 📌 [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) (pages 1-9), `Google Research`
* [Automatic Prompt Selection for Large Language Models](https://arxiv.org/abs/2404.02717), `Cinnamon AI, Hung Yen University of Technology and Education & Deakin University`
* [PromptGen: Automatically Generate Prompts using Generative Models](https://aclanthology.org/2022.findings-naacl.3/), `Baidu Research`
* [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501), `Renmin University of China & Huawei Noah’s Ark Lab`
* [Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174), `UC Santa Barbara & Microsoft Research`
* [From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models](https://arxiv.org/abs/2401.02777), `Beike Inc.`
* 📌 [Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach](https://arxiv.org/abs/2407.16833) (pages 1-7), `Google DeepMind & University of Michigan`
* [A Survey on Retrieval-Augmented Text Generation for Large Language Models](https://arxiv.org/abs/2404.10981), `York University`
* [Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks](https://arxiv.org/abs/2412.15605), `National Chengchi University & Academia Sinica`
* [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511), `University of Washington, Allen Institute for AI & IBM Research AI`
* [Auto-RAG: Autonomous Retrieval-Augmented Generation for Large Language Models](https://arxiv.org/abs/2411.19443), `Chinese Academy of Sciences`
* [Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity](https://arxiv.org/abs/2403.14403), `Korea Advanced Institute of Science and Technology`
* [Querying Databases with Function Calling](https://arxiv.org/abs/2502.00032), `Weaviate, Contextual AI & Morningstar`



<a name="0611"></a>
#### 06.11. _Lab_: LLM-based Chatbot

> On material of [_Lecture_: Virtual Assistants](#0511)

In this lab, we'll build a chatbot and try different prompts and settings to see how it affects the output.

**Sources**:
* ✍️ [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api), `LangGraph`
* [Use the graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api), `LangGraph`



### Week 4



<a name="1211"></a>
#### 12.11 & 13.11. _Labs_: RAG

> On material of [_Lecture_: Virtual Assistants](#0511)

In this lab, we'll start expanding the functionality of the chatbot built at the last lab to connect it to our user-specific information. On the first day, we'll preprocess our custom data for further retrieval. The following day we'll complete move from data preprocessing to implementing the RAG workflow.

**Sources**:
* ✍️ [Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval), `LangChain`
* ✍️ [Build a custom RAG agent](https://docs.langchain.com/oss/python/langgraph/agentic-rag), `LangChain`
* [Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders), `LangChain`
* [Text splitters](https://docs.langchain.com/oss/python/integrations/splitters), `LangChain`
* [Embedding models](https://docs.langchain.com/oss/python/integrations/text_embedding), `LangChain`
* [Vector stores](https://docs.langchain.com/oss/python/integrations/vectorstores), `LangChain`
* [Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers), `LangChain`
* ✍️ [Build a RAG agent with LangChain](https://docs.langchain.com/oss/python/langchain/rag#build-a-rag-agent-with-langchain), `LangGraph`
* [Adaptive RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/) (deprecated), `LangGraph`



### Week 5



<a name="1911"></a>
#### 19.11. _Lecture_: Multi-agent Environment

This lectures directs its attention to automating everyday / business operations in a multi-agent environment. We'll look at how agents communicate with each other, how their communication can be guided (both with and without involvement of a human), and how this is used in real applications.

**Key points**:
* Multi-agent environment
* Agents communication
* Examples of pipelines for business operations

**Sources**:
* 📌 [LLM-based Multi-Agent Systems: Techniques and Business Perspectives](https://arxiv.org/abs/2411.14033) (pages 1-8), `Shanghai Jiao Tong University & OPPO Research Institute`
* [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442), `Stanford, Google Research & DeepMind`
* [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325), `MIT & Google Brain`
* [Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View](https://arxiv.org/abs/2310.02124), `Zhejiang University, National University of Singapore & DeepMind`
* [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155), `Microsoft Research et al.`
* 🍿 [How real-world businesses are transforming with AI — with more than 140 new stories](https://blogs.microsoft.com/blog/2025/03/10/https-blogs-microsoft-com-blog-2024-11-12-how-real-world-businesses-are-transforming-with-ai/), `Microsoft` (blog post)
* 🍿 [Built with LangGraph](https://www.langchain.com/built-with-langgraph), `LangGraph` (website page)
* 🍿 [Your AI Companion](https://blogs.microsoft.com/blog/2025/04/04/your-ai-companion/), `Microsoft` (blog post)
* [Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant](https://arxiv.org/abs/2502.01390), `Delft University of Technology & The University of Queensland`



<a name="2011"></a>
#### 20.11. _Lab_: Multi-agent Environment

> On material of [_Lecture_: Multi-agent Environment](#1911)

This lab will introduce a short walkthrough to creation of a multi-agent environment for automated meeting scheduling and preparation. We will see how the coordinator agent will communicate with two auxiliary agents to check time availability and prepare an agenda for the meeting.

**Sources**:
* ✍️ [Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent#multi-agent), `LangGraph`
* [Human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop), `LangGraph`
* [Plan-and-Execute](https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/) (deprecated), `LangGraph`
* [Reflection](https://langchain-ai.github.io/langgraph/tutorials/reflexion/reflexion/) (deprecated), `LangGraph`
* [Multi-agent supervisor](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) (deprecated), `LangGraph`



### Week 6



<a name="2611"></a>
#### 26.11 & 27.11. _Labs_: LLM-powered Website

This lab open a mini-cycle of labs, where you will individually build a couple of smaller multi-agent systems. These labs are needed for you to practice the technical implementation of such systems, identify and work on your weak spots, as well as discuss all the doubts and difficulties you encounter. Consider it preparation for the final project. During the first two labs, you will create a workflow to generate websites with LLMs. The LLMs will generate both the contents and the code required for rendering, styling and navigation.

**Sources**:
* see [_Lab_: Multi-agent Environment](#2011)
* ✍️ [HTML: Creating the content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content), `MDN`
* ✍️ [Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started), `MDN`



### Week 7



<a name="0312"></a>
#### 03.12 & 04.12. _Labs_: LLM-powered Research Assistant

The second system you will build individually will be a multi-agent research assistant. It will facilitate in planning the research, generating and evaluating hypotheses, and finding the literature for a given scientific problem.

**Sources**: see [_Lab_: Multi-agent Environment](#2011)



### Week 8



<a name="1012"></a>
#### 10.12. _Lecture_: Role of AI in Recent Years

The last _lecture_ of the course will turn to societal considerations regarding LLMs and AI in general and will investigate its role and influence on the humanity nowadays.

**Key points**:
* Studies on influence of AI in the recent years
* Studies on AI integration rate
* Ethical, legal & environmental aspects

**Sources**:
* 📌 [Protecting Human Cognition in the Age of AI](https://arxiv.org/abs/2502.12447) (pages 1-5), The University of Texas at Austin et al.
* 📌 [Artificial intelligence governance: Ethical considerations and implications for social responsibility](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4515121) (pages 1-12), `University of Malta`
* [Augmenting Minds or Automating Skills: The Differential Role of Human Capital in Generative AI's Impact on Creative Tasks](https://arxiv.org/abs/2412.03963), `Tsinghua University & Wuhan University of Technology`
* [Human Creativity in the Age of LLMs: Randomized Experiments on Divergent and Convergent Thinking](https://arxiv.org/abs/2410.03703), `University of Toronto`
* [Empirical evidence of Large Language Model's influence on human spoken communication](https://arxiv.org/abs/2409.01754v1), `Max-Planck Institute for Human Development`
* 🍿 [The 2025 AI Index Report: Top Takeaways](https://hai.stanford.edu/ai-index/2025-ai-index-report), `Stanford`
* [Growing Up: Navigating Generative AI’s Early Years – AI Adoption Report: Executive Summary](https://ai.wharton.upenn.edu/focus-areas/human-technology-interaction/2024-ai-adoption-report/), `AI at Wharton`
* [Ethical Implications of AI in Data Collection: Balancing Innovation with Privacy](https://arxiv.org/abs/2503.14539), `AI Data Chronicles`
* [Legal and ethical implications of AI-based crowd analysis: the AI Act and beyond](https://pubmed.ncbi.nlm.nih.gov/40421374/), `Vrije Universiteit`
* [A Survey of Sustainability in Large Language Models: Applications, Economics, and Challenges](https://arxiv.org/abs/2412.04782v1), `Cleveland State University et al.`



<a name="1112"></a>
#### 11.12. Wrap-up

This informal meeting will give a small summary with key takeaways from the course. We will also discuss the next steps such as project requirements, proposal procedure etc. 

**Key points**:
* Summary
* Project discussion
* Q&A



### Week 9



<a name="1712"></a>
#### 17.12. _Debate_: Role of AI in Recent Years

> On material of [_Lecture_: Role of AI in Recent Years](#1012)

The core block of the course will be concluded by the final debates about the role of AI in recent years. Debate topics well be announced on 10.12.

**Sources**: see [_Lecture_: Role of AI in Recent Years](#1012)



<a name="1812"></a>
#### 18.12. Project Proposals

In this meeting, you will introduce your project proposals. The goal of this session is to receive feedback on your idea from your peer students and me in order to adjust the idea if necessary. Additionally, the intermediate consultations for the project groups will be scheduled.

**Key points**:
* Project proposals
* Consultation scheduling



## January-February: PROJECTS



<a name="project_weeks"></a>
### Weeks 10-13

This time is given to you to implement the projects as well as to prepare a short presentation for the final week. During this time, there will be a few consultations for the project groups, where we will be inspecting the intermediate progress and addressing the issues.



### Week 14

<a name="0402"></a>
#### 04.02 & 05.02. Project Presentations

Finally, the last two sessions of the course will be dedicated to your project presentations.