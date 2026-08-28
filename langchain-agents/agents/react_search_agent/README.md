# React Search Agent

This agent uses LangChain to answer questions with a simple search tool. This agent will have a static tool instead of searching from outside ex: internet

## Setup

Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your-api-key
```

## Run

From the `langchain-agents` folder, run:

```powershell
python -m agents.react_search_agent.main
```
