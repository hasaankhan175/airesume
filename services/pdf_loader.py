"""
PDF Loader Service

This module extracts text and metadata from PDF files using PyMuPDF.
"""

from pathlib import Path
from typing import Dict

import fitz  # PyMuPDF


class PDFLoader:
    """Extract text and metadata from PDF files."""

    @staticmethod
    def extract_text(pdf_path: Path) -> str:
        """
        Extract all text from a PDF.

        Args:
            pdf_path (Path): Path to the PDF file.

        Returns:
            str: Extracted text.

        Raises:
            FileNotFoundError: If the PDF does not exist.
            RuntimeError: If the PDF cannot be read.
        """

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        try:
            document = fitz.open(pdf_path)

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            return text.strip()

        except Exception as e:
            raise RuntimeError(f"Error reading PDF '{pdf_path.name}': {e}")

    @staticmethod
    def extract_metadata(pdf_path: Path) -> Dict:
        """
        Extract metadata from a PDF.

        Args:
            pdf_path (Path): Path to PDF.

        Returns:
            dict: PDF metadata.
        """

        try:
            document = fitz.open(pdf_path)

            metadata = {
                "filename": pdf_path.name,
                "pages": document.page_count,
                "title": document.metadata.get("title"),
                "author": document.metadata.get("author"),
                "subject": document.metadata.get("subject"),
                "creator": document.metadata.get("creator"),
            }

            document.close()

            return metadata

        except Exception as e:
            raise RuntimeError(f"Could not read metadata: {e}")