from pydantic import BaseModel
from langchain_tavily import TavilySearch
from langchain_core import tools
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from shared.utils.llm_utils import AgentResponse


def search_agent(api_key: str, tavily_api_key: str, query: str) -> str:
    """
    The agent returns the search result based on the query from internet
    Args:
        api_key = OpenAI or other LLM key
        tavily_api_key = Tavily search api key to search internet
        query = the query to search
    Returns
        Agent response in a pydantic format
    """
    llm = ChatOpenAI()
    tools = [TavilySearch()]
    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
    result = agent.invoke({"messages": HumanMessage(content=query)})
    return result
