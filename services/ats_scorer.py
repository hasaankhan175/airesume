"""
ATS Scorer

Calculates a deterministic ATS score by comparing
a resume against a job description.
"""

import re
from typing import Dict


class ATSScorer:
    """
    Production-ready ATS scoring engine.
    """

    def __init__(self):

        self.weights = {
            "skills": 35,
            "keywords": 20,
            "experience": 20,
            "education": 10,
            "projects": 10,
            "certifications": 5,
        }

        self.stopwords = {
            "the", "a", "an", "and", "or", "to", "of",
            "for", "in", "on", "with", "is", "are",
            "be", "as", "by", "at", "from", "into",
            "using", "use", "will", "should", "must",
            "required", "preferred", "looking", "candidate",
            "experience", "work", "job", "role"
        }

        self.education_keywords = [
            "bachelor",
            "master",
            "phd",
            "bs",
            "bsc",
            "ms",
            "msc",
            "mba",
            "degree"
        ]

        self.project_keywords = [
            "project",
            "projects",
            "developed",
            "built",
            "implemented",
            "designed",
            "created"
        ]

        self.certification_keywords = [
            "certified",
            "certificate",
            "aws",
            "azure",
            "google cloud",
            "tensorflow",
            "oracle",
            "cisco",
            "microsoft"
        ]

    # -------------------------------------------------------

    def tokenize(self, text: str):

        words = re.findall(
            r"[A-Za-z][A-Za-z0-9+#.-]*",
            text.lower()
        )

        return {
            word
            for word in words
            if len(word) > 2 and word not in self.stopwords
        }

    # -------------------------------------------------------

    def extract_years(self, text: str):

        years = re.findall(
            r"(\d+)\+?\s*years?",
            text.lower()
        )

        if years:
            return max(map(int, years))

        return 0

    # -------------------------------------------------------

    def contains_any(
        self,
        text: str,
        keywords: list
    ):

        text = text.lower()

        return any(
            keyword.lower() in text
            for keyword in keywords
        )

    # -------------------------------------------------------

    def score(
        self,
        resume_text: str,
        job_description: str,
    ) -> Dict:

        resume_words = self.tokenize(resume_text)

        jd_words = self.tokenize(job_description)

        matched_keywords = sorted(
            resume_words.intersection(jd_words)
        )

        missing_keywords = sorted(
            jd_words - resume_words
        )

        # ------------------------------------
        # Keyword Score
        # ------------------------------------

        keyword_ratio = (
            len(matched_keywords) / len(jd_words)
            if jd_words else 0
        )

        keyword_score = round(
            keyword_ratio *
            self.weights["keywords"],
            2
        )

        # ------------------------------------
        # Skill Score
        # (same keywords but weighted higher)
        # ------------------------------------

        skill_score = round(
            keyword_ratio *
            self.weights["skills"],
            2
        )

        # ------------------------------------
        # Experience Score
        # ------------------------------------

        resume_years = self.extract_years(
            resume_text
        )

        jd_years = self.extract_years(
            job_description
        )

        if jd_years == 0:

            experience_score = self.weights["experience"]

        else:

            ratio = min(
                resume_years / jd_years,
                1
            )

            experience_score = round(
                ratio *
                self.weights["experience"],
                2
            )

        # ------------------------------------
        # Education Score
        # ------------------------------------

        resume_has_education = self.contains_any(
            resume_text,
            self.education_keywords
        )

        jd_requires_education = self.contains_any(
            job_description,
            self.education_keywords
        )

        if jd_requires_education:

            education_score = (
                self.weights["education"]
                if resume_has_education
                else 0
            )

        else:

            education_score = self.weights["education"]

        # ------------------------------------
        # Project Score
        # ------------------------------------

        project_score = (
            self.weights["projects"]
            if self.contains_any(
                resume_text,
                self.project_keywords
            )
            else 0
        )

        # ------------------------------------
        # Certification Score
        # ------------------------------------

        certification_score = (
            self.weights["certifications"]
            if self.contains_any(
                resume_text,
                self.certification_keywords
            )
            else 0
        )

        # ------------------------------------
        # Final Score
        # ------------------------------------

        total_score = round(

            keyword_score +

            skill_score +

            experience_score +

            education_score +

            project_score +

            certification_score,

            2

        )

        total_score = min(
            total_score,
            100
        )

        # ------------------------------------
        # Strengths
        # ------------------------------------

        strengths = []

        weaknesses = []

        if skill_score >= 25:
            strengths.append(
                "Strong technical skill match."
            )
        else:
            weaknesses.append(
                "Technical skills do not sufficiently match the job description."
            )

        if experience_score >= 15:
            strengths.append(
                "Relevant work experience."
            )
        else:
            weaknesses.append(
                "Relevant experience is limited."
            )

        if education_score == self.weights["education"]:
            strengths.append(
                "Education matches job requirements."
            )
        else:
            weaknesses.append(
                "Education requirements are not fully met."
            )

        if project_score:
            strengths.append(
                "Relevant projects detected."
            )
        else:
            weaknesses.append(
                "No significant projects found."
            )

        if certification_score:
            strengths.append(
                "Relevant certifications found."
            )

        return {

            "overall_score": total_score,

            "scores": {

                "skills": skill_score,

                "keywords": keyword_score,

                "experience": experience_score,

                "education": education_score,

                "projects": project_score,

                "certifications": certification_score,

            },

            "matched_keywords": matched_keywords,

            "missing_keywords": missing_keywords,

            "matched_skills": matched_keywords,

            "missing_skills": missing_keywords,

            "resume_years": resume_years,

            "required_years": jd_years,

            "strengths": strengths,

            "weaknesses": weaknesses,

        }