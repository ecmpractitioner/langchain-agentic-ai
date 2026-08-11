from shared.utils.llm_calls import call_openai_llm


def hello_agent(api_key: str | None) -> str:
    """Call the LLM with a simple hello-world prompt."""
    system_prompt = "You are a helpful agent"
    user_prompt = "Tell me a joke about AI"
    llm_params = {
        "temperature": 0.7,
        "max_tokens": 100,
    }
    response = call_openai_llm(
        "gpt-4o-mini",
        user_prompt,
        system_prompt,
        "",
        **llm_params,
    )
    print(response)
    return response

