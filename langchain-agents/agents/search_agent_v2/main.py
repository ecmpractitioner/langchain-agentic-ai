from agents.react_search_agent_v2.agent import search_agent
from shared.utils.load_env import load_and_return_api_key

if __name__ == "__main__":
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    tavily_key = load_and_return_api_key("TAVILY_API_KEY")
    print(search_agent(api_key, tavily_key, "What is the weather in Bangalore"))
