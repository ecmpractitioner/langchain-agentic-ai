import os
from shared.utils.load_env import load_and_return_api_key
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage
from langchain_core import tools
from langchain.agents import create_agent
from shared.utils.llm_utils import AgentResponse


class JokeAgent:
    def __init__(self):
        self.openai_key = load_and_return_api_key("OPENAI_API_KEY")
        self.prompt_path = os.path.join(
            os.path.dirname(__file__), "prompts", "system_prompt.txt"
        )
        self.system_prompt = self.load_prompt()

    def load_prompt(self):
        with open(self.prompt_path, "r") as f:
            return f.read().strip()

    def run(self, topic: str) -> str:
        """
        A simple agent that tells jokes on the topic chosen by the user.
        Args:
            topic - the topic chosen/selected by the user
        Returns
            The joke based on the topic
        """
        llm = ChatOpenAI()
        tools = [TavilySearch()]
        agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
        result = agent.invoke({"messages": HumanMessage(content=topic)})
        return result
