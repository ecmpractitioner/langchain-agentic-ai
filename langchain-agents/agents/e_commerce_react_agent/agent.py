import inspect
import re

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from agents.e_commerce_react_agent.tools.agent_tools import (
    get_product_price,
    apply_discount,
)
import ollama

# from tools.agent_tools import get_product_price, apply_discount
from langsmith import traceable

# We will ReACT prompt for this agent.


class ECommerceReACTAgent:
    def __init__(
        self,
        model_name: str,
        temperature: float,
        model_provider: str,
        max_iterations: int,
    ):
        self.model = model_name
        self.tools_dict = self._create_tools_dict()
        self.tools_description = self._create_tools_description()
        self.temperature = temperature
        self.model_provider = model_provider
        self.max_iterations = max_iterations

    def _create_tools_dict(self):
        return {
            "get_product_price": get_product_price,
            "apply_discount": apply_discount,
        }

    # since we are building ReACT agent, we need to create a list with
    # - tool name
    # - tool signature
    # - description or docstring of the tools
    def _create_tools_description(self):
        description = []
        for tool_name, tool_function in self.tools_dict.items():
            original_function = getattr(tool_function, "__wrapped__", tool_function)
            # print(f"original function is {original_function}")
            signature = inspect.signature(original_function)
            docstring = inspect.getdoc(tool_function) or ""
            description.append(f"{tool_name}{signature} - {docstring}")
        return "\n".join(description)

    def _get_prompt(self, path: str):
        with open(path, "r") as file:
            return file.read()

    def _create_llm(self, model: str, messages: list(dict[str:str]), options):

        return ollama.chat(model=model, messages=messages, options=options)

    def _Create_agent(self):
        pass

    def _get_final_prompt(self, react_prompt: str, question: str) -> str:
        return (
            react_prompt.replace("{tool_descriptions}", self.tools_description)
            .replace("[{tool_names}]", ", ".join(self.tools_dict.keys()))
            .replace("{{question}}", question)
        )

    @traceable(name="ECommereceReActAgent")
    def run(self, message: str, prompt_path: str):
        # load the prompt
        react_prompt = self._get_prompt(prompt_path)
        # replace the prompt with tools, question, and descriptions
        final_prompt = self._get_final_prompt(react_prompt, message)
        # print(final_prompt)

        # next, we need to create a scratch pad for the LLM. This is like a working pad for LLM
        # It will have the full history of the chat
        scratchpad = ""
        options = {"stop": "ss", "temp": 0}

        # Now we will iterate
        for iteration in range(1, self.max_iterations):
            print(f"------ Starting Iteration {iteration}-------")
            # now let's add the result of the previous response from LLM to the final prompt
            final_prompt += scratchpad
            # now get the response from the LLM
            response = self._create_llm(
                model=self.model,
                messages=[{"role": "user", "content": final_prompt}],
                options={"stop": ["\nObservation"], "temperature": 0},
            )
            # print(response.message)
            # Now we have the response from the LLM and this could be the last repose after all tool calling if any.
            # Now, we need to check for the "final answer" and if it contains, end the iteration and return the response.
            # If not, continue the iteration untill all toll calls if any are completed
            llm_response = response.message.content
            final_answer_match = re.search(r"Final Answer:\s*(.+)", llm_response)
            if final_answer_match:
                return final_answer_match.group(1).strip()
            else:
                # This is not the final answer and there might be tool call.
                # Parse and get the tool details with the input
                # This is Action and Action Input would look like: Action: get_product_price\nAction Input: laptop
                action_match = re.search(r"Action:\s*(.+)", llm_response)
                action_input_match = re.search(r"Action Input:\s*(.+)", llm_response)

                print(
                    f"action_match is {action_match} and action input match is {action_input_match}"
                )

                # next get the action and action input
                tool_name = action_match.group(1).strip()
                tool_input = action_input_match.group(1).strip()
                print(f"tool_name is {tool_name} and tool_input is {tool_input}")
                # Split comma-separated args; strip key= prefix if LLM outputs key=value format
                raw_args = [x.strip() for x in tool_input.split(",")]
                args = [x.split("=", 1)[-1].strip().strip("'\"") for x in raw_args]
                if tool_name not in self.tools_dict:
                    observation = f"Error: Tool '{tool_name}' not found. Available tools: {list(self.tools_dict.keys())}"
                else:
                    observation = str(self.tools_dict[tool_name](*args))

                # CHANGE 7: History is one growing string re-sent every iteration (replaces messages.append).
                scratchpad += f"{llm_response}\nObservation: {observation}\nThought:"
        print("ERROR: Max iterations reached without a final answer")
        return None
