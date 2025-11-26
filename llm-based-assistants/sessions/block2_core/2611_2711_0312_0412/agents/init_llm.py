from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.rate_limiters import InMemoryRateLimiter


# this rate limiter will ensure we do not exceed the rate limit
# of 40 RPM given by NVIDIA
_rate_limiter = InMemoryRateLimiter(
    requests_per_second=5 / 12,  # 25 requests per minute to be sure
    check_every_n_seconds=3,  # wake up every 5 seconds to check whether allowed to make a request,
    max_bucket_size=2  # controls the maximum burst size
)


def init_llm(model_name: str, **kwargs) -> ChatNVIDIA:
    
    """
    Initialize and return a ChatNVIDIA language model with rate limiting.

    Args:
        model_name (str): The name of the NVIDIA model to use, see https://build.nvidia.com/models for available models.
        **kwargs: Additional keyword arguments to pass to the ChatNVIDIA constructor.

    Returns:
        ChatNVIDIA: An instance of the ChatNVIDIA language model with rate limiting.
    """


    return ChatNVIDIA(
        model=model_name,
        # api_key=os.getenv("NVIDIA_API_KEY"),
        rate_limiter=_rate_limiter,  # bind the same rate limiter as we have shared requests
        **kwargs
    )