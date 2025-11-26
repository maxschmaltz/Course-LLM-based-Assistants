# 26.11 & 27.11 & 03.12 & 04.12. LLM-powered Website

## Project Overview

In this assignment, you will build an LLM-based **multi-agent system** using LangChain and LangGraph for the collaborative creation of simple websites. The agents work in a decentralized manner and distribute the responsibilities based on their skills. The twist: agents do not know their roles directly! Instead, each receives a noisy profile and must deduce roles and workflow through debate and planning.


### Agents and Roles

There are 3 agents:
* **Amily:** Has strengths in writing, research, and some hobbies.
* **John:** Interested in visual arts, can find images, loves UI and design.
* **Riya:** Knows code and static analysis, but also likes chess and outdoor sports.

Each agent only has access to some tools — web search, image search, file manager, or code checker.


## System Workflow

1. **Stage 1: Debating Roles & Planning**: Sequential
* All agents receive a website topic, the task, and the *profiles* (not explicit roles) of all agents.
* Each agent proposes a plan: who does what, in what order, and why (based just on the provided profiles/tools).
* Votes and criticism: 
   * Each agent reviews others' plans, critiques them, and assigns grades (1-10).
   * Each agent self-reflects on their plan based on the critiques.
* Revision: All agents can revise their plan after seeing feedback.
* Repeat voting until one plan reaches at least 17 points (combined from 2 other agents).

The goal of the first stage is for the agents to understand their specialization and build and agree on a plan based on it.

2. **Stage 2: Website Creation**: Decentralized
* Agents build the website step by step, following (but not blindly!) the agreed plan.
* On every turn, an agent receives the artifacts so far and the plan, then decides what to do and who should go next.
* Agents can reject prior work and send it back for fixes, or skip steps if needed (decentralized, flexible).

3. **Stage 3: Approval** (optional): Sequential
* Optionally, a final round of vote can be added to confirm successful completion of the website. 


## Assignment Tasks

Your starter code contains ready fragments for the basic ReACT agent and all tools. The rest is up to you! You must fill in the missing logic: prompts, structured outputs, graph orchestration etc.

* Implement each system's stages (planning, critiquing, plan execution steps, approval).
* Make use of provided code to initialized agents and bind them with tools.
* Handle the debate and voting loop (consensus via grades).
* Allow decentralized execution: any agent may determine who acts next, and can send things “back” if needed.
* Agents must confirm when the project is done before the system ends.

**Important**: The key is to show how roles, workflows, and cooperation can emerge, not to hard-code assignments.