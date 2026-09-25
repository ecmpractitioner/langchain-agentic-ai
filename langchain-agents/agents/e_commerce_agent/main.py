from agents.e_commerce_agent.agent import EcommerceAgent
from agents.e_commerce_agent import constants
from shared.utils.load_env import load_and_return_api_key

if __name__ == "__main__":
    print("Running the agent...")
    api_key = load_and_return_api_key("OPENAI_API_KEY")
    agent = EcommerceAgent(
        constants.DEFAULT_MODEL,
        constants.TEMPERATURE,
        constants.MODEL_PROVIDER,
        constants.MAX_ITERATIONS,
    )
    print(agent.run("For the product laptop, apply silver tier discount"))
