# 17.07. _Pitch_: Agent for Web Resumes

In the third pitch, the _contractors_ will present their solution to generating HTML resumes. The agent will receive an initial prompt with a (partial) description of some character, will then creatively fulfill the gaps in their biography and generate and validate an HTML one-page resume for them.

The suggested idea to the workflow is the following:
* The agent receives the initial prompt (e.g. "Make a resume for John. John is a 40-years old farmer and he wants to start working for OpenAI.")
* The agent creatively fill in the gaps in (makes up) the character's biography: all that is usually needed for a resume: education, relevant experience etc. The agent should consider the job that the character wants to find (if provided) and make up relevant education and experience.
* The agent creates an HTML resume.
* The agent validates it statically.
    * If the page is valid, the system saves the file(s) and exits;
    * Otherwise, the page is regenerated until valid or until the max number if generations is reached.  

As before, you don't have to strictly follow this scheme, it is just a quick start suggestion for you, you may change it as you want. For example, you might want to have a two-agent system with a creative agent and more deterministic web coding agent.


## Task

The project folder has the following structure:
1. The [`webagent` folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/1707/webagent) folder will store the implementation of your system.
    * [`prompts.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/1707/webagent/prompts.py) will contain the prompts for your system.
    * [`agents.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/1707/webagent/agents.py) will implement the agent (or the multi-agent system, if you want to).
2. [`demo.ipynb`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/1707/demo.ipynb) will showcase the capabilities and the limitations of the resulting system. It will take the initialized pipeline from `webagent/agents.py` and run it a few times.

Your task is to fill in the code in the provided boilerplates following the instructions [below](#steps).
* You may use any LLM and any orchestration framework you like.
* You are free in your implementation as long as it follows the architectural constrains (implements a suggested or your version of a system for creative HTML resume generation). 
* You don't have to strictly follow the boilerplate, it is just a quick start suggestion; if you think it fits your solution better, feel free to remove/edit the suggested functions as well as add your. The only limitation you have here is that the solution should be written as Python scripts (not a notebook!), and it should be called from `demo.ipynb`.

You don't have to find a perfect solution, imagine you are building an initial baseline; this activity is more about detecting the limitations and vulnerabilities of your own work and suggesting the ways to improve. Most importantly, you have to be able to explain your design choices and justify them for this particular use case. 


## Steps

### Setup

1. Download the [project folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/1707).
2. Go through the [usual setup routine](https://maxschmaltz.github.io/Course-LLM-based-Assistants/infos/llm_inference_guide/README.html) to setup your environment for the project. Put the resulting `requirements.txt` file with the dependencies in the project folder.

### Prompts in `webagent/prompts.py`

Here, you will be adding the prompts you will find required for your implementation. There are now 4 prompt placeholders as a suggestion, feel free to add/remove anything as you need for your implementation.

### Resume Generation in `webagent/agents.py`

Complete the `ResumeGenerator` class as follows:

1. **Initialization (`__init__()`)**
* Initialize your LLM. You might want to increase the temperature this time as the task is more creative.
* Initialize the agent(s).
* Replace the placeholder for the keyword arguments (`**kwargs`) with specific parameters that you need to initialize the agent (or none, if none is needed).

2. **Complete the Initial Biography (`complete_biography()`)**  
* Make up everything missing for the resume: education, experience, skills etc.
* Make sure that the resulting biography is consistent with the past **and** the plans of the character from the initial prompt (if applicable): for example, given the example from above "Make a resume for John. John is a 40 years old farmer and he wants to start working for OpenAI.", the biography should both mention something agricultural (he is a farmer) and AI-related (he wants to apply for OpenAI).

3. **Generate HTML (and CSS) Code for the Resume (`generate_resume()`)**
* Generate the resume one-pager.
* It is up to you if you want to generate a single code or two code per script.
* The resume is static so no JS is needed.

4. **Validate the Code(s) (`validate_resume()`)**  
* Statically check if the code(s) is/are valid.
* The return type and related navigation style is up to you: it can be a `bool` value, an `AIMessage` that you will parse separately, a structured output with a verdict and a comment etc.

5. **Refine the Code(s) (`refine_resume_code()`)**  
* If there are errors detected in `validate_resume`, fix them here.
* The errors can be related both to the programming and the contexts.

6. **Save the Resume (`save_resume()`)**  
* Save the code(s) into a file (files).
* If you have an agent with a file system tool (e.g. a validator), you don't need this function.
* The filename can be generated here or provided from another action (in which case you should adjust the parameters correspondingly).

7. **Agent Run (`run()`)**
* Route the input through the steps.
* Ensure the transparent output: current steps, reasoning, validation result etc.

Additional notes:
* If you will be using `LangGraph` as the orchestration framework, create a state scheme and replace the `query` etc. parameters in the function to the `state` parameter.
* Build the routing logic in a separate function according to your framework (e.g. specify edges and nodes for `LangGraph`).
* Once again, you may add/edit anything you want as long as it creates a multi-agent system.

### Demonstration in `demo.ipynb`

Define the parameter values you need for instantiating the `ResumeGenerator` class from `webagent/agents.py` and initialize it. Run the agent a few times with different initial prompts. Experiment with how full the initial description is.


## Deliverables & Logistics

1. Prepare slides that would present your solution to the "company board" (your fellow students). The slides should highlight the design decisions step by step (agent initialization, the pipeline etc.), explain the choices of the LLMs etc., so basically justify why you implemented the system the way you did. It should then inspect the outputs of the system in detail and provide a qualitative analysis of those. Finally, it should discuss the current limitations and possible workarounds.
2. With these slides, you will hold a presentation (30-40 min). After that, you have to be ready to answer the questions from the board.
3. Put the complete code and the slides to a GitHub repository. It may be private if you want, then you will have to send an invitation for the username `maxschmaltz`. The submission succeeds via email, and the deadline is July 17, 12pm. Note: if you will put the files to the repo manually, don't forget to exclude environment variables, dependencies etc.