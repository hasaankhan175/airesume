"""
Vector Store Service

Handles creating, saving, loading, and searching the FAISS vector database.
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import settings

from huggingface_hub import login

login(token=settings.HF_API_TOKEN)
class VectorStore:
    """Manage the FAISS vector database."""

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        )

        self.db = None

    def create(self, documents: List[Document]):
        """
        Create a FAISS index from documents.
        """

        self.db = FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

    def save(self):
        """
        Save the FAISS index to disk.
        """

        if self.db is None:
            raise ValueError("Vector database has not been created.")

        self.db.save_local(
            folder_path=str(settings.VECTOR_STORE_DIR)
        )

    def load(self):
        """
        Load an existing FAISS index.
        """

        self.db = FAISS.load_local(
            folder_path=str(settings.VECTOR_STORE_DIR),
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

    def similarity_search(
        self,
        query: str,
        k: int = settings.TOP_K_RESULTS
    ):
        """
        Retrieve the most relevant documents.
        """

        if self.db is None:
            raise ValueError("Vector database not loaded.")

        return self.db.similarity_search(
            query=query,
            k=k
        )