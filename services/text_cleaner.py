"""
Text Cleaning Service

This module cleans extracted resume text before chunking and embedding.
"""

import re
import unicodedata


class TextCleaner:
    """Utility class for cleaning extracted resume text."""

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean extracted resume text.

        Parameters
        ----------
        text : str
            Raw extracted text.

        Returns
        -------
        str
            Cleaned text.
        """

        if not text:
            return ""

        # Normalize Unicode characters
        text = unicodedata.normalize("NFKC", text)

        # Standardize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove non-printable characters
        text = "".join(
            char for char in text
            if char.isprintable() or char == "\n"
        )

        # Replace multiple spaces with a single space
        text = re.sub(r"[ ]{2,}", " ", text)

        # Replace 3 or more blank lines with 2
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()