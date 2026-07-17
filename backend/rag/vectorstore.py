from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.loader import load_documents
from rag.embeddings import get_embeddings

BASE_DIR = Path(__file__).resolve().parent.parent
VECTORSTORE_DIR = BASE_DIR / "vectorstore"


def build_vectorstore():
    print("=" * 60)
    print("Building FAISS Vector Database")
    print("=" * 60)

    print("\nLoading PDF documents...")
    documents = load_documents()

    print(f"Loaded {len(documents)} pages.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("\nLoading embedding model...")
    embeddings = get_embeddings()

    print("Generating embeddings and building FAISS index...")

    db = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    VECTORSTORE_DIR.mkdir(exist_ok=True)

    db.save_local(str(VECTORSTORE_DIR))

    print("\n✅ FAISS Vector Database Created Successfully")
    print(f"Saved to: {VECTORSTORE_DIR}")