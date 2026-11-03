import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL")
)

response = model.invoke("Hello! Explain LangChain in one line.")

print(response.content)