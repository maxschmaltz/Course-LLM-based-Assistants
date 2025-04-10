# LLM Inference Guide

For this course, we will be using NVIDIA Cloud that generously hosts various open-source LLMs and provides a free API limited by 40 requests per minute (RPM). This guide shows how you set up your account and start using the LLMs.


## Contents
* [Contents](#contents)
* [Prerequisites](#prerequisites)
* [Environment Setup](#environment-setup)
* [Getting API Key](#getting-api-key)
* [Test](#test)
* [Next Steps](#next-steps)


## Prerequisites

1. Install [Python](https://www.python.org/downloads/) on your machine.
2. Install [Git](https://git-scm.com/downloads).
3. Install any IDE of your choice: [VS Code](https://code.visualstudio.com/download), [Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html) etc.
4. Create an account at [NVIDIA Developer Program](https://developer.nvidia.com/developer-program) with you **student email**: `firstname.lastname@student.uni-tuebingen.de`.


## Environment Setup

It is a good practice to have a separate isolated environment for each project. Such environment includes all of your code, resources, tests etc, as well as dependencies, (sometimes) executables and such.

1. Make a new directory where your project will be stored and open it in your IDE.
2. Open the terminal. If you are a Windows user, open GitBash (will be available after Git installation) and not the default cmd.
3. Create a Python virtual environment with [venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). The virtual environment is a directory that will contain a copy of Python and Pip as well as all the dependencies. An example for creating a virtual environment in folder _.venv_ with venv is below:

    ```bash
    python3 -m venv .venv   # create a copy of Python and so
    source .venv/bin/activate # for Unix-based (including MacOS)
    source .venv/Scripts/activate   # for Windows
    ```

4. Install requirements. Here, for the setup test purposes, we only need `langchain_nvidia_ai_endpoints` and `python-dotenv`:

    ```bash
    pip install langchain_nvidia_ai_endpoints python-dotenv
    ```

    A more robust (and really used) alternative is to create a _requirements.txt_ file like this:

    ```text
    langchain_nvidia_ai_endpoints==0.3.9
    python-dotenv==1.1.0
    ```

    and then execute

    ```bash
    pip install -r requirements.txt
    ```

5. To make this guide shorter, we do not create a git repository.


## Getting API Key

Now that you have completed all the prerequisites and prepared an environment to work in, you only need to configure an API key.

1. Create an empty _.env_ file with the following variable (leave empty for now):

    ```bash
    NVIDIA_API_KEY=""
    ```

2. Log in to [NVIDIA Cloud](https://build.nvidia.com/) with the account you created in [prerequisites](#prerequisites).
3. Go to your profile (upper right corner) > API Keys. Click Generate API Key, name it and copy.
4. Put the key value to your _.env_ under the `NVIDIA_API_KEY` variable.


## Test

Finally, you can test if the API works for you. Here's a sample code you can run in a _.py_ file in the root of your project directory:

```python
import os
import dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.rate_limiters import InMemoryRateLimiter

dotenv.load_dotenv()    # that loads the .env file variables into os.environ


# choose any model, catalogue is available under https://build.nvidia.com/models
MODEL_NAME = "meta/llama-3.3-70b-instruct"

# prompts are usually stored in a separate file
# but for the sake of simplicity, we will have it here
SYSTEM_MESSAGE = "You are a medieval French knight."


# the most simple example (synchronous implementation)
class Agent:

    def __init__(self):
        # this rate limiter will ensure we do not exceed the rate limit
        # of 40 RPM given by NVIDIA
        rate_limiter = InMemoryRateLimiter(
            requests_per_second=35 / 60,  # 35 requests per minute to be sure
            check_every_n_seconds=0.1,  # wake up every 100 ms to check whether allowed to make a request,
            max_bucket_size=7,  # controls the maximum burst size
        )
        self.llm = ChatNVIDIA(
            model=MODEL_NAME,
            api_key=os.getenv("NVIDIA_API_KEY"), 
            temperature=0,   # ensure reproducibility,
            rate_limiter=rate_limiter  # bind the rate limiter
        )

    def invoke(self, user_query):
        # prepare the messages
        messages = [
            SystemMessage(
                content=SYSTEM_MESSAGE
            ),
            HumanMessage(
                content=user_query
            )
        ]
        # inference
        response = self.llm.invoke(messages)
        return response.content


if __name__ == "__main__":
    agent = Agent()
    # ask the knight a question
    user_query = "Give me a summary of the Battle of Agincourt."
    response = agent.invoke(user_query)
    print(response)
```


## Next Steps

As for now, you're good to go! An example directory you must have gotten after going through this guide is stored [here](https://github.com/maxschmaltz/Course-LLM-based-Assistants/tree/main/llm-based-assistants/infos/llm_inference_guide) (excluding _.venv_ and _.env_).


Later, for each of the projects, you will only do the [environment setup](#environment-setup) and the steps 1 and 4 of [getting API Key](#getting-api-key); and instead of the sample code, you will have cool complex stuff, but we'll get to that yet.

Contact me in case of any questions and problems you encounter during the setup.