"""
Build FAISS Index

Processes all resume PDFs and creates a FAISS vector database.
Run this file only when building or rebuilding the index.
"""

from pathlib import Path
import time

from config import settings

from services.pdf_loader import PDFLoader
from services.text_cleaner import TextCleaner
from services.chunker import TextChunker
from services.vector_store import VectorStore


def build_index():

    print("=" * 70)
    print("AI Resume Analyzer - Building FAISS Index")
    print("=" * 70)

    start_time = time.time()

    chunker = TextChunker()
    vector_store = VectorStore()

    all_documents = []

    total_pdfs = 0
    failed_pdfs = 0

    # Iterate through every category folder
    for category_dir in sorted(settings.RESUME_DATA_DIR.iterdir()):

        if not category_dir.is_dir():
            continue

        category = category_dir.name

        print(f"\nProcessing Category: {category}")

        pdf_files = list(category_dir.glob("*.pdf"))

        for pdf_path in pdf_files:

            total_pdfs += 1

            try:

                # Extract PDF text
                text = PDFLoader.extract_text(pdf_path)

                if not text.strip():
                    continue

                # Clean text
                clean_text = TextCleaner.clean(text)

                # Convert to LangChain Documents
                documents = chunker.split(
                    text=clean_text,
                    source=pdf_path,
                    category=category
                )

                all_documents.extend(documents)

            except Exception as e:

                failed_pdfs += 1

                print(f"Failed: {pdf_path.name}")
                print(e)

    print("\nCreating FAISS Index...")

    vector_store.create(all_documents)

    print("Saving Index...")

    vector_store.save()

    elapsed = time.time() - start_time

    print("\n" + "=" * 70)

    print("Index Successfully Created!")

    print(f"PDFs Processed : {total_pdfs}")
    print(f"Failed PDFs    : {failed_pdfs}")
    print(f"Total Chunks   : {len(all_documents)}")
    print(f"Time Taken     : {elapsed:.2f} seconds")

    print("=" * 70)


if __name__ == "__main__":
    build_index()