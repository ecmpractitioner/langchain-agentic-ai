from agents.react_search_agent.agent import search_agent
from shared.utils.load_env import load_and_return_api_key


def test():
    print("Tested")


def run_agent():
    pass


if __name__ == "__main__":
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    print(search_agent(api_key))
