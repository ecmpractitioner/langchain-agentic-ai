from pathlib import Path
from shared.utils.load_env import load_and_return_api_key
from agents.e_commerce_agent import constants
from agents.e_commerce_react_agent.agent import ECommerceReACTAgent

if __name__ == "__main__":
    print("Running the agent...")
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    agent = ECommerceReACTAgent(
        constants.DEFAULT_MODEL,
        constants.TEMPERATURE,
        constants.MODEL_PROVIDER,
        constants.MAX_ITERATIONS,
    )
    path = str(Path(__file__).resolve().parent / "prompts" / "ReAct_prompt.txt")
    print(agent.run("For the product laptop, apply silver tier discount", path))
