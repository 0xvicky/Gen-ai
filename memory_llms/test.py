from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from langchain_core.messages import SystemMessage
from langchain.agents import create_agent
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()


USER_QUERY = input("> ")

# search_result = vector_store.similarity_search(query=USER_QUERY, k=6)

# context = "\n\n\n".join(
#     [
#         f"Page Content:{result.page_content}\nPage number:{result.metadata.get("page", "unknown")}\nFile Location:{result.metadata["source"]}"
#         for result in search_result
#     ]
# )

llm = ChatOllama(
    model="mistral",
    base_url="http://localhost:11434",
    temperature=0,
    # other params...
)

# SYSTEM_PROMPT = SystemMessage(content=f"""
# You are a highly accurate PDF assistant.

# Your task is to answer the user's query strictly using the provided context extracted from a PDF.

# First, understand the context and identify the most relevant parts. Then generate a clear, concise answer.

# After reasoning, return your final answer in the following JSON format:

# {{
# "page_content": "<your summarized answer based ONLY on the context>",
# "page_number": "[list of page numbers where the answer was found]"
# }}

# Guidelines:

# * Use ONLY the provided context. Do not use outside knowledge.
# * If the answer is not clearly present in the context, return:
#   {{
#   "page_content": "Answer not found in the document.",
#   "page_number":"[]"
#   }}
# * Keep the answer simple and easy to understand.
# * Combine information from multiple chunks if needed.
# * Do NOT copy raw text blindly — summarize it.
# * Do NOT hallucinate.

# Context:
# {context}

# """)


SYSTEM_PROMPT = "YOU ARE A HELPFUL ASSISTANT !"
agent = create_agent(
    llm,
    system_prompt=SYSTEM_PROMPT,
)


result = agent.invoke({"messages": [{"role": "user", "content": USER_QUERY}]})

output = result["messages"][-1].content
print(output)
