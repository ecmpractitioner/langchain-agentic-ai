# Search Agent V3

This agent uses an LLM together with Tavily search to answer questions using live internet results.

## What it does

- Reads the OpenAI API key and Tavily API key from the environment
- Sends the query to a LangChain agent
- Uses Tavily as the search tool
- Returns the answer from the agent

## Setup

Add the following keys to your `.env` file:

```env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

## Run

From the project root (`langchain-agents`), run:

```powershell
python -m agents.search_agent_v3.main
```

You can also change the query in `main.py` to test different searches.
