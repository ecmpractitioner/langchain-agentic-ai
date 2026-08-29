from shared.utils.llm_calls import call_openai_llm
from shared.utils.load_env import load_and_return_api_key
from agents.search_agent_v3.agent import search_agent

if __name__ == "__main__":
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    tavily_key = load_and_return_api_key("TAVILY_API_KEY")
    print(search_agent(api_key, tavily_key, "List top three AI roles from Linkedin"))
