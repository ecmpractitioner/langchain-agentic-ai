import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from shared.utils.load_env import load_and_return_api_key
from agents.hello_world_agent.agent import hello_agent


if __name__ == "__main__":
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    print(f"Hello World Agent loaded API key: {api_key is not None}")
    hello_agent(api_key)

