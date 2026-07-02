"""
Resume Analyzer

Main pipeline for Resume Analysis using RAG.
"""

from pathlib import Path
from typing import Union
from services.ats_scorer import ATSScorer

from services.pdf_loader import PDFLoader
from services.text_cleaner import TextCleaner
from services.retriever import Retriever

from prompts.ats_prompt import ATSPromptBuilder
from models.llm import LLM


class ResumeAnalyzer:
    """
    Main Resume Analyzer Pipeline.
    """

    def __init__(self):

        self.loader = PDFLoader()
        self.cleaner = TextCleaner()
        self.retriever = Retriever()
        self.llm = LLM()
        self.ats = ATSScorer()

    def analyze(
        self,
        resume_path: Union[str, Path],
        job_description: str,
        top_k: int = 5,
    ) -> str:
        """
        Analyze a resume against a job description.

        Parameters
        ----------
        resume_path : str | Path
            Path to the uploaded resume PDF.

        job_description : str
            Target job description.

        top_k : int
            Number of similar resume chunks to retrieve.

        Returns
        -------
        str
            AI-generated ATS analysis report.
        """

        # -----------------------------------------
        # Convert to Path object
        # -----------------------------------------

        resume_path = Path(resume_path)

        # -----------------------------------------
        # Step 1: Extract Resume Text
        # -----------------------------------------

        resume_text = self.loader.extract_text(resume_path)

        # -----------------------------------------
        # Step 2: Clean Resume
        # -----------------------------------------

        resume_text = self.cleaner.clean(resume_text)
        
        ats_result = self.ats.score(
            resume_text=resume_text,
            job_description=job_description,
            )
        # -----------------------------------------
        # Step 3: Retrieve Similar Resume Chunks
        # -----------------------------------------

        results = self.retriever.similarity_search(
            query=resume_text,
            k=top_k,
        )
        retrieved_context = "\n\n".join(
            f"""
        Category: {doc.metadata.get('category', '')}
        Source: {doc.metadata.get('source', '')}

        {doc.page_content}
        """
            for doc in results
        )

        # -----------------------------------------
        # Step 4: Build Prompt
        # -----------------------------------------

        prompt = ATSPromptBuilder.build_prompt(
            resume_text=resume_text,
            job_description=job_description,
            retrieved_context=retrieved_context,
            ats_result=ats_result,
        )

        # -----------------------------------------
        # Step 5: Generate AI Analysis
        # -----------------------------------------

        report = self.llm.generate(prompt)

        return {   
            "ats_result": ats_result,
            "report": report
            }