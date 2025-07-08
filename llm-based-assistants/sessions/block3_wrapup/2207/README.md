# 22.07. _Pitch_: LLM-based Research Assistant

In the final pitch, the _contractors_ will present their solution to automated research hypothesis generation and validation. The solution will have to introduce a multi-agent environment to conduct collaborative research tasks with built-in verification and conflict resolution mechanisms. The solution will read and analyze research literature, generate hypotheses, and validate findings through agent collaboration. The research domain is linguistics so we can evaluate the quality of the generations better.

The initial idea to the architecture of this multi-agent system is the following:
* There are 3 agents:
    * The _literature reviewer_ processes and summarizes research papers, extracts key claims, methodologies, and findings, and identifies citation networks and paper relationships
    * The _hypothesis generator_ generates research hypotheses based on literature gaps using cross-domain analogy generation techniques, proposes multiple competing hypotheses with reasoning, and ranks them by novelty and feasibility
    * The _validator_ evaluates hypotheses for logical consistency, challenges assumptions and identifies missing evidence, and provides constructive feedback for hypothesis refinement
* Once a new research question comes, the _literature reviewer_ is triggered; it processes relevant papers and forms a structured analysis for the _hypothesis generator_
* Once the _hypothesis generator_ receives the analysis, it generates multiple hypotheses and sends them with reasoning to the _validator_; the _hypothesis generator_ has an access to a ool to query a linguistic knowledge graph (KG) for entities and relations
* _Validator_ has the KG tool as well; if the hypotheses contradict the graph or is just not reliable, it sends feedback back to the _hypothesis generator_ for refinement, otherwise approves it
* Once hypotheses are approved by the _validator_, they are returned to the user

![System Architecture](./architecture.jpg)

Now once again, we will not add any actual integrations but rather simulate them, which the agent will not be aware of. All they will know is that these tools are provided and which scheme they conform to.

Obviously, in a real product, such research process would run with actual research databases. However, this functionality is not relevant for us, so we will once again simulate it with a synthetic literature collection. Also, the knowledge graph is usually not static and is updated as the system evolves, which will not be the case for this project.

As always, you don't have to strictly follow this scheme, it is just a quick start suggestion for you, you may change it as you want.

## Task

The project folder has the following structure:
1. The [`resources` folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/resources) contains sample research abstracts and domain knowledge about linguistics generated with Claude. You will use it to simulate the literature base for the agents.
2. The [`multi_agent` folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/multi_agent) folder will store the implementation of your system.
    * [`tools.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/multi_agent/tools.py) will contain the tools for your agents. It now contains a single tool for querying KG but you may want to add a RAG tool for literature in case you want it more custom than the standard LangChain implementation or if you choose another framework.
    * [`prompts.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/multi_agent/prompts.py) will contain the prompts for your system.
    * [`agents.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/multi_agent/agents.py) will implement the multi-agent system.
3. [`demo.ipynb`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/demo.ipynb) will showcase the capabilities and the limitations of the resulting system. It will take the initialized multi-agent system from `multi_agent/agents.py` and run it with different research questions.

Your task is to fill in the code in the provided boilerplates following the instructions [below](#steps).
* You may use any LLM and any orchestration framework you like.
* You are free in your implementation as long as it follows the architectural constrains (implements a suggested or your version of a multi-agent system). 
* You don't have to strictly follow the boilerplate, it is just a quick start suggestion; if you think it fits your solution better, feel free to remove/edit the suggested functions as well as add your. The only limitation you have here is that the solution should be written as Python scripts (not a notebook!), and it should be called from `demo.ipynb`.

You don't have to find a perfect solution, imagine you are building an initial baseline; this activity is more about detecting the limitations and vulnerabilities of your own work and suggesting the ways to improve. Most importantly, you have to be able to explain your design choices and justify them for this particular use case.

## Steps

### Setup

1. Download the [project folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207).
2. Go through the [usual setup routine](https://maxschmaltz.github.io/Course-LLM-based-Assistants/infos/llm_inference_guide/README.html) to setup your environment for the project. Put the resulting `requirements.txt` file with the dependencies in the project folder.

### Knowledge Graph Tools in `multi_agent/tools.py`

1. **Knowledge Graph Query Tool (`knowledge_graph_query()`)**
* Write a tool to query the knowledge graph for fact-checking and validation.
* Should support queries for entity relationships, confidence scores, and contradictions.
* Return relevant graph information for validation purposes.

2. (Optional) **RAG Tool**
* If you want it more custom RAG tool the standard LangChain implementation or if you choose another framework for orchestration, put your RAG tool here.
* It should extract relevant literature fragments from the literature base in [`litbase.md`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/resources/litbase.md).

### Prompts in `multi_agent/prompts.py`

Here, you will be adding the prompts you will find required for your implementation.

### Multi-agent System in `multi_agent/agents.py`

Complete the `ResearchLaMA` class as follows:

1. **Initialization (`__init__()`)**
* Initialize your LLM.
* Initialize the four agents (literature reviewer, hypothesis generator, validator).
* Initialize the knowledge graph and orchestration system.
* Replace the placeholder for the keyword arguments (`**kwargs`) with specific parameters that you need to initialize the agent (or none, if none is needed).

2. **Invoke the _Literature Reviewer_ (`literature_reviewer_node()`)**  
* Extract the most relevant papers from the literature base in [`litbase.md`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/sessions/block3_wrapup/2207/resources/litbase.md).
* Generate a summary with key information, findings, theories etc.

3. **Invoke the _Hypothesis Generator_ (`hypothesis_generator_node()`)**  
* Generate multiple research hypotheses based on retrieved literature.
* Generate confidence to the hypotheses.

5. **Invoke the _Validator_ Agent (`validator_node()`)**  
* Fact-check hypotheses against knowledge graph.
* (Re)assign confidence scores to generated content.
* Generate feedback if the hypotheses should be regenerated.

6. **Refine Hypotheses (`refine_hypotheses()`)**  
* Have the _hypothesis generator_ refine the hypotheses based on the feedback from the _validator_.

7. **Agent Run (`run()`)**
* Route the input through the steps.
* Ensure the transparent output: current steps, reasoning, validation result etc.

Additional notes:
* If you will be using `LangGraph` as the orchestration framework, create a state scheme and replace the individual parameters in the functions with the `state` parameter.
* Build the routing logic in a separate function according to your framework (e.g. specify edges and nodes for `LangGraph`).
* Once again, you may add/edit anything you want as long as it creates a multi-agent system.

### Demonstration in `demo.ipynb`

Define the parameter values you need for instantiating the `ResearchLaMA` class from `multi_agent/agents.py` and initialize it. Run the agent with different research questions -- it should demonstrate the complete pipeline from literature analysis through hypothesis generation, criticism, and validation.

## Deliverables & Logistics

1. Prepare slides that would present your solution to the "company board" (your fellow students). The slides should highlight the design decisions step by step (agent initialization, multi-agent pipeline, knowledge graph integration, etc.), explain the choices of the LLMs, orchestration framework, and conflict resolution mechanisms, so basically justify why you implemented the system the way you did. It should then inspect the outputs of the system in detail and provide a qualitative analysis of the research hypotheses generated, their novelty, feasibility, and validation quality. Finally, it should discuss the current limitations and possible workarounds.
2. With these slides, you will hold a presentation (30-40 min). After that, you have to be ready to answer the questions from the board.
3. Put the complete code and the slides to a GitHub repository. It may be private if you want, then you will have to send an invitation for the username `maxschmaltz`. The submission succeeds via email, and the deadline is July 22, 12pm. Note: if you will put the files to the repo manually, don't forget to exclude environment variables, dependencies etc.