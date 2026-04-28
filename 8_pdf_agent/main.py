from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()
pdf_path = Path(__file__).parent / "golang.pdf"


# ================INDEXER================================#
# load the pdf
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

# print(docs[43])

# implemeting chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = text_splitter.split_documents(documents=docs)

# print(chunks[0])

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en")
# vector = embeddings.embed_query("hello, world!")
# print(vector)
vector_store = QdrantVectorStore.from_documents(
    embedding=embeddings,
    documents=chunks,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

print("Indexing of doc is done.👍🏿")
