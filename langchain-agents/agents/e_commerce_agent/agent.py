from pathlib import Path

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from agents.e_commerce_agent.tools.agent_tools import get_product_price, apply_discount

# from tools.agent_tools import get_product_price, apply_discount
from langsmith import traceable


class EcommerceAgent:
    def __init__(
        self,
        model_name: str,
        temperature: float,
        model_provider: str,
        max_iterations: int,
    ):
        self.model = model_name
        self.tools = [get_product_price, apply_discount]
        self.tools_dict = self._create_tool_dict()
        self.temperature = temperature
        self.model_provider = model_provider
        self.llm = self._create_llm()
        self.agent = self._create_agent()
        self.max_iterations = max_iterations

    def _create_tool_dict(self):
        return {t.name: t for t in self.tools}

    def _create_llm(self):
        # llm = init_chat_model(self.model, self.temperature)
        llm = init_chat_model(
            model=self.model,
            model_provider=self.model_provider,
            temperature=self.temperature,
            tools=self.tools,
        )
        return llm.bind_tools(self.tools)

    def _create_agent(self):
        pass

    def _get_prompt(self, path: str) -> str:
        with open(path, "r") as file:
            return file.read()

    @traceable(name="Langchain Agent Loop")
    def run(self, message: str):
        # self.llm = self.llm.bind_tools(self.tools)
        # create the messages for the llm
        messages = [
            SystemMessage(
                content=self._get_prompt(
                    str(
                        Path(__file__).resolve().parent
                        / "prompts"
                        / "system_prompt.txt"
                    )
                )
            ),
            HumanMessage(content=message),
        ]

        """we have almost everything now. We begin the agent loop and the agent loop, we will check if the 
        response from LLM requires a tool calling. If yes, we will call the tool and then iterate again until LLM 
        decides there are no more tool calling required. Finally, we return the response from LLM"""
        # for this example, we will iterate ten times
        for iteration in range(1, self.max_iterations + 1):
            print(f"\n --- iteration {iteration}")
            # the response from LLM for chat completion is in AIMessage format. Let's check if the AI message has tool calls
            ai_message = self.llm.invoke(messages)
            if not ai_message.tool_calls:
                # this means, this is the final answer, so return it
                return ai_message.content
            else:
                # LLMs can return more than one tool call and in such case, we have to iterate and execute the calls
                # for this example, we will access only the first tool call because we know based on our question, we will have only one tool call
                tool_call = ai_message.tool_calls[0]
                tool_name = tool_call.get("name")
                tool_args = tool_call.get("args", {})
                tool_id = tool_call.get("id")
                print(
                    f"\n Tool selected {tool_name} with args {tool_args} and tool_id {tool_id}"
                )
                # print(self.tools_dict)
                # now let's get the tool to use from the dict
                tool_to_use = self.tools_dict.get(tool_name)

                # tool_to_use will be python based langchain tool and has invoke method to invoke it.
                # before that, check to see if tool_to_call is blank or not
                if tool_to_use is None:
                    raise ValueError(f"Tool '{tool_name}' not found")
                else:
                    observation = tool_to_use.invoke(tool_args)
                    """When there are more than one tool call or more than one interaction with the LLM,
                    we need to preserve the history and share it with the LLM"""
                    messages.append(ai_message)
                    messages.append(
                        ToolMessage(content=str(observation), tool_call_id=tool_id)
                    )
                    # Sprint(f"observation is {observation}")
        print("ERROR: Max iterations reached without a valid answer")
        return None
