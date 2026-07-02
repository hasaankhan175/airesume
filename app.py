import os
import tempfile

import streamlit as st

from services.analyzer import ResumeAnalyzer

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Hide Streamlit Branding */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */

.stApp{
    background:#0f172a;
}

/* Main Container */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* Hero Card */

.hero{

    background:linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    );

    padding:35px;

    border-radius:20px;

    border:1px solid rgba(255,255,255,.08);

    box-shadow:0px 10px 30px rgba(0,0,0,.35);

}

/* Cards */

.card{

    background:#111827;

    padding:25px;

    border-radius:18px;

    border:1px solid rgba(255,255,255,.08);

    margin-bottom:20px;

}

/* Titles */

.big-title{

    font-size:42px;

    font-weight:700;

    color:white;

}

.subtitle{

    font-size:18px;

    color:#b8c2cc;

}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#111827;

}

/* Buttons */

.stButton button{

    width:100%;

    background:#2563eb;

    color:white;

    font-weight:600;

    border-radius:10px;

    height:55px;

    border:none;

}

.stButton button:hover{

    background:#1d4ed8;

}

/* Text Area */

textarea{

    border-radius:12px !important;

}

/* Upload */

[data-testid="stFileUploader"]{

    border-radius:15px;

}

.metric-card{

    background:#1f2937;

    padding:20px;

    border-radius:15px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# INITIALIZE
# ==========================================================

analyzer = ResumeAnalyzer()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.success("Backend Status")

    st.write("✅ RAG")

    st.write("✅ FAISS")

    st.write("✅ Hugging Face")

    st.write("✅ ATS Engine")

    st.write("✅ Resume Analyzer")

    st.markdown("---")

    st.info("""
**Tech Stack**

• Streamlit

• LangChain

• FAISS

• Sentence Transformers

• HuggingFace

• PyMuPDF
""")

    st.markdown("---")

    st.caption("Made by Hasan 🚀")

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<div class="big-title">

🤖 AI Resume Analyzer

</div>

<div class="subtitle">

Production Ready Resume Screening using

RAG • FAISS • HuggingFace • ATS Scoring

</div>

</div>

""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# INPUT SECTION
# ==========================================================

left,right=st.columns(2)

with left:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.subheader("📄 Upload Resume")

    uploaded_file=st.file_uploader(

        "",

        type=["pdf"]

    )

    st.markdown("</div>",unsafe_allow_html=True)

with right:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.subheader("💼 Job Description")

    job_description=st.text_area(

        "",

        height=280,

        placeholder="Paste the complete Job Description..."

    )

    st.markdown("</div>",unsafe_allow_html=True)

# ==========================================================
# ANALYZE BUTTON
# ==========================================================

analyze=st.button(

    "🚀 Analyze Resume"

)

# ==========================================================
# PROCESS
# ==========================================================

if analyze:

    if uploaded_file is None:

        st.error("Upload a Resume PDF.")

        st.stop()

    if job_description.strip()=="":

        st.error("Paste a Job Description.")

        st.stop()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.getbuffer())

        temp_path=tmp.name

    with st.spinner("Analyzing Resume..."):

        result=analyzer.analyze(

            resume_path=temp_path,

            job_description=job_description

        )

    os.remove(temp_path)
    st.session_state["result"]=result

# ==========================================================
# RESULT PLACEHOLDER
# ==========================================================

if "result" in st.session_state:

    result = st.session_state["result"]
    ats = result["ats_result"]
    report = result["report"]

    st.success("Analysis Completed Successfully!")

    # ===============================
    # Metrics
    # ===============================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🎯 ATS Score",
        f"{ats['overall_score']:.1f}%"
    )

    c2.metric(
        "✅ Matched Skills",
        len(ats["matched_skills"])
    )

    c3.metric(
        "❌ Missing Skills",
        len(ats["missing_skills"])
    )

    c4.metric(
        "📄 Resume Experience",
        f"{ats['resume_years']} Years"
    )

    st.divider()

    st.subheader("📊 Score Breakdown")

    scores = ats["scores"]

    st.progress(scores["skills"] / 35)
    st.write(f"Skills: {scores['skills']:.1f}/35")

    st.progress(scores["keywords"] / 20)
    st.write(f"Keywords: {scores['keywords']:.1f}/20")

    st.progress(scores["experience"] / 20)
    st.write(f"Experience: {scores['experience']:.1f}/20")

    st.progress(scores["education"] / 10)
    st.write(f"Education: {scores['education']:.1f}/10")

    st.progress(scores["projects"] / 10)
    st.write(f"Projects: {scores['projects']:.1f}/10")

    st.progress(scores["certifications"] / 5)
    st.write(f"Certifications: {scores['certifications']:.1f}/5")

    st.divider()

    left, right = st.columns(2)

    # with left:

    #     st.subheader("✅ Matched Skills")

    #     for skill in ats["matched_skills"]:
    #         st.success(skill)

    # with right:

    #     st.subheader("❌ Missing Skills")

    #     for skill in ats["missing_skills"]:
    #         st.error(skill)

    # st.divider()

    tab1, tab2, tab3 = st.tabs(
        [
            "🤖 AI Analysis",
            "💪 Strengths",
            "⚠ Weaknesses"
        ]
    )

    with tab1:

        st.markdown(report)

    with tab2:

        for item in ats["strengths"]:
            st.success(item)

    with tab3:

        for item in ats["weaknesses"]:
            st.warning(item)

    st.download_button(
        "📥 Download Report",
        report,
        file_name="resume_analysis.txt"
    )
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "© 2026 AI Resume Analyzer | Built with Streamlit"
)