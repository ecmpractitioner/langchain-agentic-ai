# React Search Agent V2

This agent uses LangChain to answer questions with a simple search tool. This agent will use Tavily client to connect to internet and search.

## Setup

Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your-api-key
```

## Run

From the `langchain-agents` folder, run:

```powershell
python -m agents.react_search_agent_v2.main
```
