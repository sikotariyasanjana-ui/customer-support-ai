"""
embeddings.py
Creates the embedding model used by the RAG pipeline.
"""

from langchain_community.embeddings import HuggingFaceEmbeddings


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    """
    Load and return the HuggingFace embedding model.
    """

    print("=" * 60)
    print("Loading Embedding Model...")
    print(f"Model : {MODEL_NAME}")
    print("=" * 60)

    embeddings = HuggingFaceEmbeddings(
        model_name=MODEL_NAME,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    print("✅ Embedding Model Loaded Successfully\n")

    return embeddings