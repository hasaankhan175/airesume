"""
Retriever Service

Loads the FAISS vector database and retrieves the most
relevant resume chunks.
"""

from typing import List

from langchain_core.documents import Document

from config import settings
from services.vector_store import VectorStore


class Retriever:
    """Retrieve relevant documents from the FAISS vector database."""

    def __init__(self):

        self.vector_store = VectorStore()
        self.vector_store.load()

    def similarity_search(
        self,
        query: str,
        k: int = settings.TOP_K_RESULTS
    ) -> List[Document]:
        """
        Perform similarity search.

        Parameters
        ----------
        query : str

        k : int

        Returns
        -------
        List[Document]
        """

        return self.vector_store.db.similarity_search(
            query=query,
            k=k
        )

    def mmr_search(
        self,
        query: str,
        k: int = settings.TOP_K_RESULTS,
        fetch_k: int = 20
    ) -> List[Document]:
        """
        Perform Max Marginal Relevance search.
        """

        return self.vector_store.db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=fetch_k
        )