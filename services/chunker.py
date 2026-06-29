"""
Text Chunking Service

Splits cleaned resume text into LangChain Document objects
with metadata for Retrieval-Augmented Generation (RAG).
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import settings


class TextChunker:
    """Split cleaned text into overlapping LangChain Documents."""

    def __init__(
        self,
        chunk_size: int = settings.CHUNK_SIZE,
        chunk_overlap: int = settings.CHUNK_OVERLAP,
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(
        self,
        text: str,
        source: Path,
        category: str
    ) -> List[Document]:
        """
        Split text into LangChain Document objects.

        Parameters
        ----------
        text : str
            Cleaned resume text.

        source : Path
            Path to the original PDF.

        category : str
            Resume category (e.g., ENGINEERING, HR).

        Returns
        -------
        List[Document]
        """

        if not text.strip():
            return []

        chunks = self.splitter.split_text(text)

        documents = []

        for chunk_id, chunk in enumerate(chunks):

            document = Document(
                page_content=chunk,
                metadata={
                    "source": source.name,
                    "filepath": str(source),
                    "category": category,
                    "chunk_id": chunk_id,
                }
            )

            documents.append(document)

        return documents