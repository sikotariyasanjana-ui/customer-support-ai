"""
loader.py
Loads all PDF files from the knowledge_base folder.
"""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# backend folder
BASE_DIR = Path(__file__).resolve().parent.parent

# backend/knowledge_base
KNOWLEDGE_BASE = BASE_DIR / "knowledge_base"


def load_documents():
    """
    Load all PDF files from the knowledge_base folder.
    Returns a list of LangChain Document objects.
    """

    if not KNOWLEDGE_BASE.exists():
        raise FileNotFoundError(
            f"Knowledge base folder not found:\n{KNOWLEDGE_BASE}"
        )

    pdf_files = sorted(KNOWLEDGE_BASE.glob("*.pdf"))

    if not pdf_files:
        raise ValueError(
            f"No PDF files found inside:\n{KNOWLEDGE_BASE}"
        )

    documents = []

    print("=" * 60)
    print("Loading PDF documents...")
    print("=" * 60)

    for pdf in pdf_files:

        print(f"Loading: {pdf.name}")

        try:
            loader = PyPDFLoader(str(pdf))
            docs = loader.load()

            print(f"✓ Loaded {len(docs)} page(s)")

            documents.extend(docs)

        except Exception as e:
            print(f"✗ Failed to load {pdf.name}")
            print(f"Reason: {e}")

    if len(documents) == 0:
        raise ValueError("No valid PDF documents were loaded.")

    print("=" * 60)
    print(f"Total PDF files : {len(pdf_files)}")
    print(f"Total pages     : {len(documents)}")
    print("=" * 60)

    return documents