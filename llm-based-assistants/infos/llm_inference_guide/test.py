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