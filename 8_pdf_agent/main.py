from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "golang.pdf"

# load the pdf
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

print(docs[43])
