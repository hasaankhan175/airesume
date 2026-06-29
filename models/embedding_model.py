"""
Embedding Model

Loads the SentenceTransformer embedding model and provides methods
for generating embeddings.
"""

from sentence_transformers import SentenceTransformer
from typing import List

from config import settings


class EmbeddingModel:
    """Wrapper around SentenceTransformer."""

    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed_text(self, text: str) -> List[float]:
        """
        Generate an embedding for a single piece of text.

        Args:
            text: Input text.

        Returns:
            List[float]: Embedding vector.
        """
        return self.model.encode(
            text,
            convert_to_numpy=True
        ).tolist()

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple text chunks.

        Args:
            documents: List of text chunks.

        Returns:
            List[List[float]]
        """
        return self.model.encode(
            documents,
            convert_to_numpy=True
        ).tolist()

    def get_model(self):
        """
        Return the underlying SentenceTransformer model.
        """
        return self.model