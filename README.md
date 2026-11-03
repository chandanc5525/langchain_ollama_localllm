# LangChain + Ollama: Local LLM Applications

**Building Generative AI and Agentic AI applications using LangChain, Ollama, and Python.**

This repository is a hands-on implementation of LangChain integrated with Ollama to explore Large Language Models (LLMs), prompt engineering, conversational applications, tool calling, AI agents, and Retrieval-Augmented Generation (RAG).

The primary objective is to understand how to develop LLM-powered applications using locally hosted models without depending on paid cloud-based LLM APIs.

---

## Project Overview

LangChain is a framework for developing applications powered by Large Language Models, while Ollama provides the infrastructure to run open-source LLMs locally.

This project brings both technologies together to create a practical learning environment for Generative AI and Agentic AI development.

### Project Objectives

- Understand LangChain architecture and its core components.
- Integrate locally hosted LLMs using Ollama.
- Implement prompt engineering and prompt templates.
- Understand model invocation and response handling.
- Explore LangChain Expression Language (LCEL).
- Implement structured output using Pydantic.
- Develop tool-calling workflows and AI agents.
- Build Retrieval-Augmented Generation (RAG) applications.
- Explore agent orchestration using LangGraph.
- Prepare applications for deployment using FastAPI and Docker.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM application development |
| Ollama | Local LLM runtime |
| Qwen 3 (4B) | Open-source language model |
| uv | Python project and dependency management |
| python-dotenv | Environment variable management |
| Black | Python code formatting |
| isort | Import organization |
| FastAPI | API development (planned) |
| Docker | Application containerization (planned) |

## Repository Structure

```text
langchain_ollama_localllm/
│
├── main.py
├── .env
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
│
└── .venv/
```

**Note:** The virtual environment (`.venv/`) and environment configuration (`.env`) should not be committed to GitHub.

## Prerequisites

Before getting started, install the following:

1. Python 3.12 or higher
2. [uv – Python Package Manager](https://docs.astral.sh/uv/)
3. [Ollama](https://ollama.com/)
4. Git

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/chandanc5525/langchain_ollama_localllm.git
```

Navigate to the project directory:

```bash
cd langchain_ollama_localllm
```

### Step 2: Install Dependencies

This project uses `uv` for dependency management.

Install the dependencies defined in `pyproject.toml`:

```bash
uv sync
```

### Step 3: Download the Ollama Model

Download Qwen 3 (4B):

```bash
ollama pull qwen3:4b
```

Verify the installed model:

```bash
ollama list
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory.

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:4b
```

**Important:** Local Ollama execution does not require a paid API key. The local Ollama server provides access through its localhost endpoint.

### Step 5: Run the Application

Execute the Python application using `uv`:

```bash
uv run python main.py
```

---

## Project Implementation

### 01. LangChain + Ollama: Hello World

The initial implementation demonstrates how to connect LangChain with a locally hosted Ollama model.

#### Implementation (`main.py`)

```python
import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

# Load environment variables
load_dotenv()

# Initialize the local language model
model = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL")
)

# Send a prompt to the language model
response = model.invoke(
    "Hello! Explain LangChain in one sentence."
)

# Display the generated response
print(response.content)
```

#### Execution

```bash
uv run python main.py
```

#### Implementation Workflow

```text
User Prompt
     |
     v
LangChain Application
     |
     v
ChatOllama
     |
     v
Ollama Local Server
     |
     v
Qwen 3 (4B)
     |
     v
Generated Response
```

#### Key Concepts

| Component | Explanation |
|---|---|
| `load_dotenv()` | Loads environment variables from `.env`. |
| `ChatOllama()` | Initializes the Ollama chat model. |
| `model.invoke()` | Sends a prompt to the language model. |
| `response.content` | Extracts the generated text. |

---

## Learning Roadmap

The repository will progressively cover the following concepts through practical Python implementations.

| Phase | Topic | Concepts |
|---|---|---|
| 01 | LangChain Fundamentals | Chat models, model invocation |
| 02 | Prompt Engineering | PromptTemplate, ChatPromptTemplate |
| 03 | LCEL | Runnable components and pipelines |
| 04 | Structured Output | JSON, Pydantic |
| 05 | Conversational AI | Message history and context |
| 06 | Tool Calling | Tools and external integrations |
| 07 | AI Agents | Agent execution and reasoning workflows |
| 08 | RAG | Document loaders, chunking, embeddings, vector databases |
| 09 | LangGraph | Stateful and multi-step agent workflows |
| 10 | Deployment | FastAPI, Docker |

## Why Local LLMs?

This project emphasizes local LLM development using Ollama.

| Feature | Local LLM (Ollama) | Cloud LLM API |
|---|---|---|
| Execution | Local machine | Cloud infrastructure |
| API key | Not required for local access | Generally required |
| Internet | Not required after model download | Required |
| Cost | Hardware and electricity | Provider-dependent usage charges |
| Data processing | Locally processed | Sent to external provider |

Local execution provides greater control over model deployment and data handling, subject to the security of the local environment.

## Future Enhancements

- Reusable prompt engineering workflows.
- Conversational AI applications.
- Structured output and data extraction.
- Tool calling with local LLMs.
- Autonomous AI agents.
- Document-based RAG applications.
- Vector database integration.
- Multi-agent orchestration using LangGraph.
- REST API development using FastAPI.
- Production deployment using Docker.

## Author

**Chandan Chaudhari**

- GitHub: [@chandanc5525](https://github.com/chandanc5525)
- Repository: [langchain_ollama_localllm](https://github.com/chandanc5525/langchain_ollama_localllm)

---

*This repository is part of a practical learning journey focused on Generative AI, Local LLMs, LangChain, and Agentic AI application development.*