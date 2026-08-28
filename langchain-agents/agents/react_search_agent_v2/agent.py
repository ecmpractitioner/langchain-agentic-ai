from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient


tavily = TavilyClient()


@tool
def search(query: str):
    """
    A simple tool that searches internet for the weather
    Args:
        query: query to search
    Returns:
        The search result
    """
    print(f"Searching with query {query}")
    return tavily.search(query=query)


def search_agent(api_key: str, tavily_key: str, weather_query: str) -> str:
    """
    A simple search agent to search internet for the queries

    """
    llm = ChatOpenAI(api_key=api_key)
    tools = [search]
    agent = create_agent(model=llm, tools=tools)
    # result = agent.invoke({"messages": HumanMessage(content=weather_query)})
    result = agent.invoke({"messages": HumanMessage(content=weather_query)})
    return result
