from shared.utils.load_env import load_and_return_api_key
from agents.hello_world_agent.agent import hello_agent


if __name__ == "__main__":
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    print(f"Hello World Agent loaded API key: {api_key is not None}")
    hello_agent(api_key)
