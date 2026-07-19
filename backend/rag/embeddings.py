"""
embeddings.py
Creates the embedding model used by the RAG pipeline.
"""

import os
import requests
from typing import List
from langchain_core.embeddings import Embeddings

class GeminiHTTPEmbeddings(Embeddings):
    def __init__(self, model: str = "models/text-embedding-004", api_key: str = None):
        self.model = model
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    def _get_headers_and_url(self, action: str) -> tuple:
        # Strip models/ from model name to avoid double models/ in URL path
        model_name = self.model
        if model_name.startswith("models/"):
            model_name = model_name[len("models/"):]

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key
        }
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:{action}"
        return headers, url

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        if not self.api_key:
            raise ValueError("No Gemini API key found for embeddings.")
        headers, url = self._get_headers_and_url("batchEmbedContents")
        reqs = []
        for text in texts:
            reqs.append({
                "model": self.model if self.model.startswith("models/") else f"models/{self.model}",
                "content": {
                    "parts": [{"text": text}]
                }
            })
        
        response = requests.post(url, json={"requests": reqs}, headers=headers)
        if response.status_code != 200:
            raise Exception(f"HTTP Embedding Error {response.status_code}: {response.text}")
        
        data = response.json()
        return [item["values"] for item in data["embeddings"]]

    def embed_query(self, text: str) -> List[float]:
        if not self.api_key:
            raise ValueError("No Gemini API key found for embeddings.")
        headers, url = self._get_headers_and_url("embedContent")
        body = {
            "model": self.model if self.model.startswith("models/") else f"models/{self.model}",
            "content": {
                "parts": [{"text": text}]
            }
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"HTTP Embedding Error {response.status_code}: {response.text}")
        
        data = response.json()
        return data["embedding"]["values"]


def get_embeddings():
    """
    Load and return the Google Gemini embedding model.
    """

    print("=" * 60)
    print("Loading Google Gemini Embedding Model...")
    print("=" * 60)

    embeddings = GeminiHTTPEmbeddings()

    print("✅ Google Gemini Embedding Model Loaded Successfully\n")

    return embeddings