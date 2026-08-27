from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from shared.utils.llm_calls import call_openai_llm


# a static tool/function to return a string
@tool  # @tool is a decorator that converts a python function into a langchain tool
def search(query: str) -> str:
    """
    This is a static tool that returns a static response when asked about weather in India
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for {query}")
    return "India weather is beautiful through out the year"


def search_agent(api_key: str | None) -> dict[str, str]:
    """
    A simple search agent to search internet for the queries

    """
    system_prompt = "You are a helpful agent"
    user_prompt = "How is the weather in India"
    llm_params = {"temperature": 0.2, "max_tokens": 100}
    llm = ChatOpenAI(api_key=api_key)
    agent = create_agent(llm, tools=[search])
    result = agent.invoke(
        {"messages": HumanMessage(content="How is the weather in India")}
    )

    return result
