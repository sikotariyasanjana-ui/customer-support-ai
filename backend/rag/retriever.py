"""
retriever.py
Loads the FAISS vector database and retrieves relevant documents.
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embeddings

BASE_DIR = Path(__file__).resolve().parent.parent
VECTORSTORE_PATH = BASE_DIR / "vectorstore"


def load_retriever():

    print("=" * 60)
    print("Loading FAISS Vector Database")
    print("=" * 60)

    embeddings = get_embeddings()

    db = FAISS.load_local(
        folder_path=str(VECTORSTORE_PATH),
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

    print("✅ Vector Database Loaded Successfully")

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        }
    )

    print("✅ Retriever Ready\n")

    return retriever