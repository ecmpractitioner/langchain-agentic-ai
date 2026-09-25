# E-commerce Agent

This agent uses an Ollama chat model and LangChain tools to look up product
prices and apply membership discounts.

## How It Works

The agent follows a manual tool-calling loop:

1. The model receives the user request and the shopping-assistant system prompt.
2. The model calls `get_product_price` to retrieve the catalog price.
3. The agent sends the tool result back to the model.
4. The model calls `apply_discount` when a discount tier was provided.
5. The agent sends the discounted price back to the model and returns the final response.

The loop stops when the model returns a response without tool calls or when the
configured maximum number of iterations is reached.

## Requirements

- Python 3.11 or later
- Ollama installed and running
- The configured Ollama model available locally

Pull the default model before running the agent:

```powershell
ollama pull qwen3.5:4b
```

The model and provider are configured in `constants.py`:

```python
DEFAULT_MODEL = "qwen3.5:4b"
MODEL_PROVIDER = "OLLAMA"
```

## Run

From the `langchain-agents` directory, activate the virtual environment and
run the module:

```powershell
.\.venv\Scripts\Activate.ps1
.\.venv\Scripts\python.exe -m agents.e_commerce_agent.main
```

The sample request in `main.py` is:

```text
For the product laptop, apply silver tier discount
```

The laptop costs `$1,200.00` and the silver tier discount is 10%, so the
discounted price is `$1,080.00`.

## Available Tools

### `get_product_price`

Looks up a product in the catalog.

Supported products:

- `laptop`: `$1,200.00`
- `mouse`: `$25.00`
- `keyboard`: `$30.00`

### `apply_discount`

Applies a membership discount to a price.

Supported tiers:

- `silver`: 10%
- `gold`: 15%
- `platinum`: 20%

The system prompt requires the agent to retrieve the price before applying a
discount and prevents it from calculating the discount itself.

## LangSmith Tracing

The `run` method is decorated with `@traceable(name="Langchain Agent Loop")`.
To enable tracing, add these variables to the `.env` file in the
`langchain-agents` directory:

```env
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=your_project_name
```

`main.py` loads the environment through `load_and_return_api_key` before the
agent is run. Do not commit `.env` or expose API keys in source control.

## Using the Agent in Python

```python
from agents.e_commerce_agent.agent import EcommerceAgent
from agents.e_commerce_agent import constants

agent = EcommerceAgent(
	constants.DEFAULT_MODEL,
	constants.TEMPERATURE,
	constants.MODEL_PROVIDER,
	constants.MAX_ITERATIONS,
)

answer = agent.run("For the product laptop, apply silver tier discount")
print(answer)
```

## Configuration

Change these values in `constants.py`:

- `DEFAULT_MODEL`: Ollama model name
- `TEMPERATURE`: model response randomness
- `MAX_ITERATIONS`: maximum model/tool exchanges per request
