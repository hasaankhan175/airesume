"""
ATS Prompt Builder

Builds a professional prompt for resume analysis.
"""


class ATSPromptBuilder:
    """Creates prompts for the Resume Analyzer."""

    @staticmethod
    def build_prompt(
        resume_text: str,
        job_description: str,
        retrieved_context: str,
        ats_result: dict,
    ) -> str:

        prompt = f"""
You are an expert ATS recruiter, HR manager, career coach, and resume reviewer.

Your task is to compare the candidate's resume against the job description.

You are also given similar resume examples retrieved from a resume knowledge base.
Use these examples only as reference. Do NOT copy their content.

==============================
JOB DESCRIPTION
==============================

{job_description}

==============================
CANDIDATE RESUME
==============================

{resume_text}

==============================
REFERENCE RESUME CONTEXT
==============================

{retrieved_context}

==============================
YOUR TASK
==============================

Perform a complete ATS analysis.

Return your answer using the following structure exactly.

==============================
CALCULATED ATS RESULT
==============================

Overall Score:
{ats_result['overall_score']}/100

Detailed Scores:

Skills:
{ats_result['scores']['skills']}

Keywords:
{ats_result['scores']['keywords']}

Experience:
{ats_result['scores']['experience']}

Education:
{ats_result['scores']['education']}

Projects:
{ats_result['scores']['projects']}

Certifications:
{ats_result['scores']['certifications']}

Matched Skills:
{', '.join(ats_result['matched_skills'])}

Missing Skills:
{', '.join(ats_result['missing_skills'])}

Strengths:
{', '.join(ats_result['strengths'])}

Weaknesses:
{', '.join(ats_result['weaknesses'])}


# ATS SCORE

Use ONLY the ATS score provided above.

DO NOT calculate another score.

Explain WHY the candidate received this score.

# SUMMARY

A concise overview of how well the resume fits the job.

# STRENGTHS

- Strength 1
- Strength 2
- Strength 3

# WEAKNESSES

- Weakness 1
- Weakness 2
- Weakness 3

# MISSING KEYWORDS

List the important keywords that are present in the job description but missing from the resume.

# MISSING SKILLS

List missing technical and soft skills.

# EXPERIENCE ANALYSIS

Evaluate whether the candidate's experience matches the job requirements.

# EDUCATION ANALYSIS

Evaluate whether the education is suitable.

# PROJECT ANALYSIS

Evaluate projects if available.

# IMPROVEMENT SUGGESTIONS

Provide detailed suggestions for improving the resume.

# FINAL DECISION

Choose exactly one:

- Excellent Match
- Good Match
- Average Match
- Weak Match



Keep your answer professional, objective, and actionable.
"""
        return prompt.strip()