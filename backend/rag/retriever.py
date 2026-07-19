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

    try:
        db = FAISS.load_local(
            folder_path=str(VECTORSTORE_PATH),
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
        print("✅ Vector Database Loaded Successfully")
    except Exception as e:
        print(f"⚠️ Warning: Could not load local FAISS index ({e}). Rebuilding it...")
        from rag.vectorstore import build_vectorstore
        try:
            build_vectorstore()
            db = FAISS.load_local(
                folder_path=str(VECTORSTORE_PATH),
                embeddings=embeddings,
                allow_dangerous_deserialization=True
            )
            print("✅ Vector Database Rebuilt and Loaded Successfully")
        except Exception as rebuild_error:
            print(f"❌ Error: Rebuilding FAISS index failed: {rebuild_error}")
            raise rebuild_error

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        }
    )

    print("✅ Retriever Ready\n")

    return retriever