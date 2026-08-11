# langchain-agentic-ai
# project learning to build LangGraph based AI Agents

Langchain-agents

# Environment Bootstrapping & Project Setup

This guide covers the initial process of bootstrapping a Python development environment, setting up project dependency management, configuring environment variables for Large Language Models (LLMs), and preparing the workspace for LangChain development.

---

## 1. Repository Initialization & Branching Strategy

To keep the project clean and isolated from existing boilerplate, initialize the repository using an orphan branch (a branch with no commit history).

1. **Clone the repository:**
```bash
git clone <repository_url>
cd link-chain-course

```


2. **Create a fresh orphan branch:**
An orphan branch starts with a completely clean slate, containing no files or historical commits.
```bash
git checkout --orphan project/hello-world

```


3. **Wipe existing files:**
Remove all tracked and untracked files from the working directory to ensure a completely empty workspace.
```bash
rm -rf .

```



---

## 2. Setting Up Python Dependency Management with UV

**UV** is an extremely fast Python package manager built on Rust. It handles dependency resolution, environment isolation, and package installation with high efficiency.

### Verifying Installation

Verify that `uv` is installed globally on your system:

```bash
uv --help

```

*(Note: If `uv` is not installed, it can be installed via pip using `pip3 install uv`)*

### Initializing the Project

Run the initialization command to generate the project skeleton, including the `pyproject.toml` configuration file and a default `main.py` entry point:

```bash
uv init

```

This creates:

* **`pyproject.toml`**: Tracks project metadata and installed dependencies.
* **`.venv/`**: An isolated virtual environment directory.
* **`main.py`**: A default boilerplate script.

---

## 3. Installing Core Project Dependencies

Install the necessary libraries for interacting with LangChain, managing provider-specific integrations, and handling environment variables and code formatting.

1. **Install core LangChain:**
```bash
uv add langchain

```


2. **Install provider-specific integration packages:**
LangChain decouples third-party providers into independent packages. This modular design ensures that you only download the dependencies required for the specific LLM providers you utilize (e.g., OpenAI, Anthropic, Google).
```bash
uv add langchain-openai

```


3. **Install utility packages:**
* **`python-dotenv`**: Loads environment variables securely from a local `.env` file.
* **`black` & `isort**`: Code formatting and import sorting utilities.


```bash
uv add python-dotenv black isort

```



---

## 4. Configuration and Security Best Practices

### Creating a `.gitignore` File

To prevent sensitive files, virtual environments, and local build artifacts from being tracked or accidentally committed to version control, create a `.gitignore` file with standard Python exclusions:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual Environments
.venv/
env/
venv/

# Environment Variables & Secrets
.env

```

### Managing API Keys Securely

Create a `.env` file in the root directory to store your API keys.

> [!WARNING]
> Never commit API keys or secret tokens to public version control repositories. Automated scrapers constantly scan public repositories for leaked keys, which can result in unexpected financial charges. Always restrict API budgets and set up usage limits on your provider dashboard.

Add your provider keys to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

```

---

## 5. Verifying the Environment in Code

To ensure that the environment variables load successfully and that the runtime has access to the installed packages, configure `main.py` to load and print the environment configuration.

```python
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Verify access to the OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")
print(f"API Key Loaded: {'Yes' if api_key else 'No'}")

```

Run the script within the active virtual environment using `uv run`:

```bash
uv run main.py

```

---

## 6. Version Control Checkpoint

Once the environment is verified and configured, stage and commit the setup files to your working branch:

```bash
git add .
git commit -m "environment setup"
git push origin project/hello-world

```