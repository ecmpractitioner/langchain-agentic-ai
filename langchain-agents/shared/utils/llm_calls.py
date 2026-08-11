"""Utilities for making calls to diverse LLMs in one place."""

from openai import OpenAI, OpenAIError


def call_openai_llm(
    model_id: str, user_prompt: str, system_prompt: str, assistant_prompt: str, **kwargs
) -> str:
    """Call an OpenAI chat model with a simple message payload."""
    try:
        openai_client = OpenAI()
        llm_model = model_id or "gpt-4o-mini"
        llm_params = {"model": llm_model, **kwargs}

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        if assistant_prompt:
            messages.append({"role": "assistant", "content": assistant_prompt})

        response = openai_client.chat.completions.create(
            messages=messages, **llm_params
        )
        return response.choices[0].message.content or ""
    except OpenAIError as e:
        return f"OpenAI Error: {e}"
