from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "eee"
print(os.getenv("OPENAI_API_KEY"))