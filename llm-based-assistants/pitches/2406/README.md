# 24.06. _Pitch_: RAG Chatbot

In this pitch, the contractor has to present their implementation of a RAG Chatbot for internal data of an imaginary company. The pipeline will run an Adaptive-RAG architecture and will implement an LLM-based reranking of the retrieved documents. For simplicity, the chatbot won't have any memory and will answer each query independently.


## Task

The project folder has the following structure:
1. The [`resources` folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/resources) contains the files that simulate an internal database of an imaginary company. Your system will retrieve specific information from these documents. The resources are one PDF and one MD containing the description and the rules of a [currently ongoing hackathon](https://www.kaggle.com/competitions/openai-to-z-challenge/overview), respectively. The hackathon started a few weeks ago so LLMs do not have information about it.
2. The [`rag_chatbot` folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/rag_chatbot) folder will store the implementation of your system.
    * [`data_manipulation.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/rag_chatbot/data_manipulation.py) will contain the functionality related to data preprocessing and storage: loading, chunking, indexing.
    * [`agent.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/rag_chatbot/agent.py) will implement the Adaptive-RAG pipeline.
    * [`main.py`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/rag_chatbot/main.py) will assemble and initialize the whole thing together; it will construct the index from `data_manipulation.py`, give it to the agent from `agent.py`, and initialize the system to be able to be queried.
3. [`demo.ipynb`](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406/demo.ipynb) will showcase the capabilities and the limitations of the resulting system. It will take the initialized RAG chatbot from `rag_chatbot/main.py` and query it with a few examples.

Your task is to fill in the code in the provided boilerplates following the instructions [below](#steps).
* You may use any tools for data preprocessing, any LLM, any embedding model, and any orchestration framework you like.
* You are free in your implementation as long as it follows the architectural constrains (implements a version of Adaptive-RAG). 
* You don't have to strictly follow the boilerplate, it is just a quick-start suggestion; if you think it fits your solution better, feel free to remove/edit the suggested functions as well as add your. The only limitation you have here is that the solution should be written as Python scripts (not a notebook!), and it should be called from `demo.ipynb`.

You don't have to find a perfect solution, imagine you are building an initial baseline; this activity is more about detecting the limitations and vulnerabilities of your own work and suggesting the ways to improve. Most importantly, you have to be able to explain your design choices and justify them for this particular use case. 


## Steps

### Setup

1. Download the [project folder](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/pitches/2406).
2. Go through the [usual setup routine](https://maxschmaltz.github.io/Course-LLM-based-Assistants/infos/llm_inference_guide/README.html) to setup your environment for the project. Put the resulting `requirements.txt` file with the dependencies in the project folder.

### Data Preprocessing in `rag_chatbot/data_manipulation.py`

1. **Data Loading (`load_data()`)**
* Write code to load all files from the specified folder.
* Handle multiple file formats (PDF, Markdown).
* For each file, create a `Document` object with its content and relevant metadata (such as filename or file type).
* Return a list of all loaded `Document` objects.

2. **Chunking (`split_data()`)**
* Write code to split each document into smaller, manageable chunks (e.g., by paragraph, sentence, or fixed token size).
* Ensure each chunk is a `Document` object, preserving or updating metadata as needed.
* Return a list of all chunked `Document` objects.

3. **Indexing (`create_index()`)**
* Write code to create an index from the provided document chunks.
* Store the resulting index persistently in the `knowledge/` folder for later retrieval.

`init_index()` will serve as the entry point for data preprocessing and indexing in `rag_chatbot/main.py`, you don't have to change anything.

As a reminder, you may choose any data loader, text splitter, embedding model etc. as long as you can explain the choice. If you need, you may add any preprocessing steps you want.

### Adaptive-RAG in `rag_chatbot/agent.py`

Here, you have to implement an Adaptive-RAG pipeline from [this paper](https://arxiv.org/abs/2403.14403). The key idea is simple: given the query, the system first decides whether it is a straightforward, a simple, or a complex query, and then performs no RAG, one- or multi-step RAG, respectively, to answer the question. Additionally, you will have to perform an LLM-based reranking of the retrieved documents for RAG (both one- and multi-step).

Complete the `AdaptiveRAGAgent` class as follows:

1. **Initialization (`__init__()`)**
* Load the document index from the `knowledge/` folder (the assembly procedure in the main file will make sure the knowledge base has been created by that time).
* Initialize your LLM and any retriever needed for RAG.
* Replace the placeholder for the keyword arguments (`**kwargs`) with specific parameters that you need to initialize the agent (or none, if none is needed), and adjust the `init_rag_agent()` arguments accordingly.

2. **Query Classification (`classify()`)**
* Implement logic to classify the input query as "direct", "simple RAG", or "iterative RAG".
* It can be a separate lightweight LLM, or the main LLM you use in the system, it's up to you.

3. **Document Reranking (`rerank()`)**
* Use your LLM to rerank a list of retrieved `Document` objects based on their relevance to the query.
* Return the reranked list.

4. **Direct Answering (`answer_directly()`)**
* For "direct" queries, answer using only the LLM without retrieving from the index.

5. **Simple RAG (`simple_rag()`)**
* For "simple RAG" queries, retrieve relevant documents from the index, rerank them, and use the top results as context for the LLM to answer.

6. **Iterative RAG (`iterative_rag()`)**
* For "iterative RAG" queries, perform multi-step retrieval and reasoning, retrieve, rerank, and possibly refine the query or context in multiple steps.

7. **Agent Run (`run()`)**
* Route the query through the classification step and call the appropriate answering method based on the result.
* Ensure the transparent output: reasoning steps, predicted query class, retrieved documents etc.

`init_rag_agent()` will serve as the entry point for agent initialization `rag_chatbot/main.py`, you don't have to change anything.

Additional notes:
* If you will be using `LangGraph` as the orchestration framework, create a state scheme and replace the `query` parameter in the function to the `state` parameter.
* Build the routing logic in a separate function according to your framework (e.g. specify edges and nodes for `LangGraph`).
* Once again, you may add/edit anything you want (except the LLM-based reranking remains required) as long as it sticks to the general Adaptive-RAG framework.

### Initialization in `rag_chatbot/main.py`

The main function simply creates and stores the index and then initializes the RAG chatbot. All you need to do is to adjust the parameters of the function `init_pipeline()` to match the ones in the RAG chatbot initialization function (`init_rag_agent()`).  

### Demonstration in `demo.ipynb`

The `rag_chatbot/main.py` provides you the function `init_pipeline()` to easily instantiate the pipeline. Define the parameter values you need for the function and call it to assemble the whole thing. It will return a run-ready instance of the `AdaptiveRAGAgent` class. The notebook already contains 10 questions for which you will have to show the outputs during the presentation. Feel free to add yours if you think it will showcase some specific properties of your system better.


## Deliverables & Logistics

1. Prepare slides that would present your solution to the "company board" (your fellow students). The slides should highlight the design decisions step by step (data preprocessing, chatbot pipeline etc.), explain the choices of the tools, LLMs etc., so basically justify why you implemented the system the way you did. It should then inspect the outputs of the system (the 10 questions from the demo notebook as well as yours if applicable) in detail and provide a qualitative analysis of those. Finally, it should discuss the current limitations and possible workarounds.
2. With these slides, you will hold a presentation (30-40 min). After that, you have to be ready to answer the questions from the board.
3. Put the complete code and the slides to a GitHub repository. It may be private if you want, then you will have to send an invitation for the username `maxschmaltz`. The submission succeeds via email, and the deadline is June 24, 12pm. Note: if you will put the files to the repo manually, don't forget to exclude environment variables, dependencies etc.