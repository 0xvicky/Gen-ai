from mem0 import Memory
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from qdrant_client.models import VectorParams, Distance
from langchain_ollama import ChatOllama
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

llm = ChatGroq(
    model="mistral",
    base_url="http://localhost:11434",
    temperature=0,
    # other params...
)
# mem0 config (CORRECT)
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {"collection_name": "mem0", "host": "localhost", "port": 6333},
        "embedding_model_dims": 768,  # Change this according to your local model's dimensions
    },
    "embedder": {  # ✅ FIXED KEY
        "provider": "huggingface",
        "config": {"model": "BAAI/bge-base-en"},
    },
    "llm": {  # 🔥 ADD THIS
        "provider": "groq",
        "config": {
            "model": "mistral",
            "ollama_base_url": "http://localhost:11434",
            "temperature": 0,
            "max_tokens": 2000,
        },
    },
}

mem_client = Memory.from_config(config)
# Add a memory
mem_client.add("I'm Vivek Cs grad", user_id="vicky")
# Retrieve memories
# memories = mem_client.get_all(filters={"user_id": "vicky"})
# print(mem_client.embedding_model)
# print(mem_client.embedding_model)
user_query = input("> ")

# # 🔍 retrieve memory
# memories = mem_client.search(query=user_query, filters={"user_id": "vicky"}, limit=3)

# # context = "\n".join([m["text"][:200] for m in memories])

# prompt = f"""
#     User memory:
#     {context}

#     Query:
#     {user_query}
#     """

# 🤖 call local LLM
result = llm.invoke([{"role": "user", "content": user_query}])

output = result.content
print(output)

# 💾 store memory
mem_client.add(
    user_id="vicky",
    messages=[
        {"role": "user", "content": user_query},
        {"role": "assistant", "content": output},
    ],
)

# mem_client.add(
#     user_id="vicky",
#     messages=[
#         {"role": "user", "content": user_query},
#         {"role": "assistant", "content": output},
#     ],
# )


print("Memory has been saved !s")
