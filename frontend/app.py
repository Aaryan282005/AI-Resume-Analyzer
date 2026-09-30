import os
import streamlit as st
import requests


# ============================================================
# 1. CONFIGURATION
# ============================================================

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000/analyze-resume"
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# 2. APPLICATION HEADER
# ============================================================

st.title("📄 AI Resume Analyzer")

st.write(
    "AI-powered resume analysis, ATS scoring and job matching system."
)

st.divider()


# ============================================================
# 3. INPUT SECTION
# ============================================================

st.header("📋 Resume & Job Information")

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# 3.1 Resume Upload
# ------------------------------------------------------------

with col1:

    st.subheader("📄 Resume")

    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Upload your resume in PDF format."
    )

    if uploaded_resume is not None:

        st.success(
            "Resume uploaded successfully."
        )

        st.write(
            f"**Filename:** {uploaded_resume.name}"
        )

        st.write(
            f"**File size:** "
            f"{uploaded_resume.size / 1024:.2f} KB"
        )


# ------------------------------------------------------------
# 3.2 Job Description
# ------------------------------------------------------------

with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=250,
        placeholder="Paste the complete job description here..."
    )

    if job_description.strip():

        st.success(
            "Job description added successfully."
        )

        st.write(
            f"**Characters:** {len(job_description)}"
        )


st.divider()


# ============================================================
# 4. ANALYZE RESUME BUTTON
# ============================================================

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True
):

    # --------------------------------------------------------
    # Validation
    # --------------------------------------------------------

    if uploaded_resume is None:

        st.warning(
            "Please upload a resume PDF."
        )

    elif not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

    else:

        # ----------------------------------------------------
        # Prepare resume file
        # ----------------------------------------------------

        files = {
            "file": (
                uploaded_resume.name,
                uploaded_resume.getvalue(),
                "application/pdf"
            )
        }

        # ----------------------------------------------------
        # Prepare job description
        # ----------------------------------------------------

        data = {
            "job_description": job_description
        }

        # ----------------------------------------------------
        # Send request to FastAPI
        # ----------------------------------------------------

        try:

            with st.spinner(
                "Analyzing resume with ATS and Gemini AI..."
            ):

                response = requests.post(
                    BACKEND_URL,
                    files=files,
                    data=data,
                    timeout=120
                )

            # ------------------------------------------------
            # Successful response
            # ------------------------------------------------

            if response.status_code == 200:

                st.success(
                    "Resume analyzed successfully!"
                )

                result = response.json()

                st.session_state[
                    "analysis_result"
                ] = result

            # ------------------------------------------------
            # Backend returned an error
            # ------------------------------------------------

            else:

                st.error(
                    f"Backend error: "
                    f"{response.status_code}"
                )

                st.write(
                    response.text
                )

        # ----------------------------------------------------
        # FastAPI server not running
        # ----------------------------------------------------

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure the backend server is running."
            )

        # ----------------------------------------------------
        # Request took too long
        # ----------------------------------------------------

        except requests.exceptions.Timeout:

            st.error(
                "The analysis took too long. "
                "Please try again."
            )

        # ----------------------------------------------------
        # Other request errors
        # ----------------------------------------------------

        except requests.exceptions.RequestException as e:

            st.error(
                f"Request failed: {str(e)}"
            )


# ============================================================
# 5. DISPLAY RESULTS
# ============================================================

if "analysis_result" in st.session_state:

    result = st.session_state[
        "analysis_result"
    ]


    # ========================================================
    # 5.1 EXTRACT RESUME DATA
    # ========================================================

    resume_data = result.get(
        "resume",
        {}
    )

    filename = resume_data.get(
        "filename",
        "Unknown"
    )

    resume_analysis = resume_data.get(
        "analysis",
        {}
    )

    resume_profile = resume_analysis.get(
        "resume_profile",
        {}
    )

    skills = resume_profile.get(
        "skills",
        []
    )


    # ========================================================
    # 5.2 EXTRACT ATS DATA
    # ========================================================

    ats_result = result.get(
        "ats_analysis",
        {}
    )


    # --------------------------------------------------------
    # Final ATS score
    # --------------------------------------------------------

    final_score_data = ats_result.get(
        "final_ats_score",
        {}
    )

    ats_score = final_score_data.get(
        "final_ats_score",
        0
    )

    exact_skill_score = final_score_data.get(
        "exact_skill_score",
        0
    )

    semantic_skill_score = final_score_data.get(
        "semantic_skill_score",
        0
    )

    keyword_score = final_score_data.get(
        "keyword_score",
        0
    )

    resume_quality_score = final_score_data.get(
        "resume_quality_score",
        0
    )


    # --------------------------------------------------------
    # Component coverage
    # --------------------------------------------------------

    exact_skill_analysis = ats_result.get(
        "exact_skill_analysis",
        {}
    )

    exact_skill_percentage = exact_skill_analysis.get(
        "match_percentage",
        0
    )


    semantic_skill_analysis = ats_result.get(
        "semantic_skill_analysis",
        {}
    )

    semantic_skill_percentage = semantic_skill_analysis.get(
        "semantic_match_percentage",
        0
    )


    keyword_analysis = ats_result.get(
        "keyword_analysis",
        {}
    )

    keyword_percentage = keyword_analysis.get(
        "coverage_percentage",
        0
    )


    resume_quality_analysis = ats_result.get(
        "resume_quality_analysis",
        {}
    )

    resume_quality_percentage = resume_quality_analysis.get(
        "quality_percentage",
        0
    )


    # ========================================================
    # 5.3 SKILL DATA
    # ========================================================

    skill_gap_analysis = ats_result.get(
        "skill_gap_analysis",
        {}
    )

    matched_skills = skill_gap_analysis.get(
        "matched_skills",
        []
    )

    missing_skills = skill_gap_analysis.get(
        "missing_skills",
        []
    )


    # IMPORTANT:
    # prioritized_skill_gaps is directly inside ats_result
    # according to your current backend response.

    prioritized_skill_gaps = ats_result.get(
        "prioritized_skill_gaps",
        []
    )


    # ========================================================
    # 5.4 GEMINI DATA
    # ========================================================

    ai_analysis = result.get(
        "ai_analysis",
        {}
    )

    resume_ai_analysis = ai_analysis.get(
        "resume_analysis",
        {}
    )

    job_recommendations = ai_analysis.get(
        "job_recommendations",
        {}
    )


    # --------------------------------------------------------
    # Resume AI analysis
    # --------------------------------------------------------

    overall_assessment = resume_ai_analysis.get(
        "overall_assessment",
        "No assessment available."
    )

    strengths = resume_ai_analysis.get(
        "strengths",
        []
    )

    weaknesses = resume_ai_analysis.get(
        "weaknesses",
        []
    )

    technical_skills = resume_ai_analysis.get(
        "technical_skills",
        []
    )

    experience = resume_ai_analysis.get(
        "experience",
        []
    )

    projects = resume_ai_analysis.get(
        "projects",
        []
    )

    improvement_areas = resume_ai_analysis.get(
        "improvement_areas",
        []
    )


    # --------------------------------------------------------
    # Job recommendations
    # --------------------------------------------------------

    job_alignment_summary = job_recommendations.get(
        "job_alignment_summary",
        "No job alignment information available."
    )

    matching_strengths = job_recommendations.get(
        "matching_strengths",
        []
    )

    job_skill_gaps = job_recommendations.get(
        "skill_gaps",
        []
    )

    priority_improvements = job_recommendations.get(
        "priority_improvements",
        []
    )

    resume_customization_tips = job_recommendations.get(
        "resume_customization_tips",
        []
    )


    # ========================================================
    # 6. RESULTS HEADER
    # ========================================================

    st.divider()

    st.header(
        "📊 Resume Analysis Dashboard"
    )

    st.caption(
        "AI-powered ATS scoring, skill matching and resume analysis"
    )


    # ========================================================
    # 7. TABS
    # ========================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Resume",
            "📊 ATS Analysis",
            "🎯 Skills",
            "🤖 Gemini AI"
        ]
    )


    # ========================================================
    # TAB 1 — RESUME
    # ========================================================

    with tab1:

        st.subheader(
            "📄 Resume Information"
        )

        st.write(
            f"**Filename:** {filename}"
        )


        st.subheader(
            "👤 Resume Profile"
        )

        st.write(
            f"**Name:** "
            f"{resume_profile.get(
                'name',
                'Not available'
            )}"
        )

        st.write(
            f"**Email:** "
            f"{resume_profile.get(
                'email',
                'Not available'
            )}"
        )


        st.subheader(
            "🛠️ Resume Skills"
        )

        if skills:

            st.write(
                ", ".join(skills)
            )

        else:

            st.info(
                "No skills detected."
            )


    # ========================================================
    # TAB 2 — ATS ANALYSIS
    # ========================================================

    with tab2:

        st.subheader(
            "📊 ATS Analysis"
        )


        # ----------------------------------------------------
        # Overall score
        # ----------------------------------------------------

        score_col1, score_col2 = st.columns(
            [1, 2]
        )


        with score_col1:

            st.metric(
                label="Overall ATS Score",
                value=f"{ats_score:.2f}/100"
            )


        with score_col2:

            st.write(
                "Score Progress"
            )

            st.progress(
                min(
                    max(
                        ats_score / 100,
                        0.0
                    ),
                    1.0
                )
            )


        st.divider()


        # ----------------------------------------------------
        # Score breakdown
        # ----------------------------------------------------

        st.subheader(
            "Score Breakdown"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Exact Skill",
                f"{exact_skill_score:.2f}/30"
            )


        with col2:

            st.metric(
                "Semantic Skill",
                f"{semantic_skill_score:.2f}/30"
            )


        with col3:

            st.metric(
                "Keywords",
                f"{keyword_score:.2f}/20"
            )


        with col4:

            st.metric(
                "Resume Quality",
                f"{resume_quality_score:.2f}/20"
            )


        st.divider()


        # ----------------------------------------------------
        # Component coverage
        # ----------------------------------------------------

        st.subheader(
            "Component Coverage"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Exact Match",
                f"{exact_skill_percentage:.2f}%"
            )


        with col2:

            st.metric(
                "Semantic Match",
                f"{semantic_skill_percentage:.2f}%"
            )


        with col3:

            st.metric(
                "Keyword Coverage",
                f"{keyword_percentage:.2f}%"
            )


        with col4:

            st.metric(
                "Resume Quality",
                f"{resume_quality_percentage:.2f}%"
            )


    # ========================================================
    # TAB 3 — SKILLS
    # ========================================================

    with tab3:

        st.subheader(
            "🎯 Skill Analysis"
        )


        # ----------------------------------------------------
        # Matched skills
        # ----------------------------------------------------

        st.write(
            "### ✅ Matched Skills"
        )


        if matched_skills:

            columns = st.columns(3)


            for index, skill in enumerate(
                matched_skills
            ):

                with columns[
                    index % 3
                ]:

                    st.success(
                        skill
                    )

        else:

            st.info(
                "No matched skills found."
            )


        st.divider()


        # ----------------------------------------------------
        # Skill gaps
        # ----------------------------------------------------

        st.write(
            "### 🚨 Skill Gaps"
        )


        if missing_skills:

            columns = st.columns(3)


            for index, skill in enumerate(
                missing_skills
            ):

                with columns[
                    index % 3
                ]:

                    st.warning(
                        skill
                    )

        else:

            st.success(
                "No major skill gaps detected."
            )


        st.divider()


        # ----------------------------------------------------
        # Skill priorities
        # ----------------------------------------------------

        st.write(
            "### 🎯 Skill Priorities"
        )


        if prioritized_skill_gaps:

            for gap in prioritized_skill_gaps:

                skill = gap.get(
                    "skill",
                    "Unknown skill"
                )

                priority = gap.get(
                    "priority",
                    "UNKNOWN"
                ).upper()


                if priority == "HIGH":

                    st.error(
                        f"🔴 **HIGH PRIORITY** — {skill}"
                    )


                elif priority == "MEDIUM":

                    st.warning(
                        f"🟠 **MEDIUM PRIORITY** — {skill}"
                    )


                elif priority == "LOW":

                    st.info(
                        f"🔵 **LOW PRIORITY** — {skill}"
                    )


                else:

                    st.write(
                        f"**{priority}** — {skill}"
                    )

        else:

            st.success(
                "No skill priorities identified."
            )


    # ========================================================
    # TAB 4 — GEMINI AI
    # ========================================================

    with tab4:

        st.subheader(
            "🤖 Gemini AI Analysis"
        )


        # ----------------------------------------------------
        # Overall assessment
        # ----------------------------------------------------

        with st.expander(
            "📋 Overall Assessment",
            expanded=True
        ):

            st.write(
                overall_assessment
            )


        # ----------------------------------------------------
        # Strengths
        # ----------------------------------------------------

        with st.expander(
            "💪 Strengths"
        ):

            if strengths:

                for strength in strengths:

                    st.success(
                        strength
                    )

            else:

                st.info(
                    "No strengths identified."
                )


        # ----------------------------------------------------
        # Weaknesses
        # ----------------------------------------------------

        with st.expander(
            "⚠️ Weaknesses"
        ):

            if weaknesses:

                for weakness in weaknesses:

                    st.warning(
                        weakness
                    )

            else:

                st.info(
                    "No weaknesses identified."
                )


        # ----------------------------------------------------
        # Technical skills
        # ----------------------------------------------------

        with st.expander(
            "🛠️ Technical Skills"
        ):

            if technical_skills:

                st.write(
                    ", ".join(
                        technical_skills
                    )
                )

            else:

                st.info(
                    "No technical skills identified."
                )


        # ----------------------------------------------------
        # Experience
        # ----------------------------------------------------

        with st.expander(
            "💼 Experience"
        ):

            if experience:

                for item in experience:

                    st.write(
                        f"• {item}"
                    )

            else:

                st.info(
                    "No experience information identified."
                )


        # ----------------------------------------------------
        # Projects
        # ----------------------------------------------------

        with st.expander(
            "🚀 Projects"
        ):

            if projects:

                for project in projects:

                    st.write(
                        f"• {project}"
                    )

            else:

                st.info(
                    "No project information identified."
                )


        # ----------------------------------------------------
        # Improvement areas
        # ----------------------------------------------------

        with st.expander(
            "📈 Improvement Areas"
        ):

            if improvement_areas:

                for improvement in improvement_areas:

                    st.warning(
                        improvement
                    )

            else:

                st.info(
                    "No improvement areas identified."
                )


        # ====================================================
        # AI JOB ALIGNMENT
        # ====================================================

        st.divider()

        st.subheader(
            "🎯 AI Job Alignment"
        )


        # ----------------------------------------------------
        # Job alignment summary
        # ----------------------------------------------------

        with st.expander(
            "📊 Job Alignment Summary",
            expanded=True
        ):

            st.write(
                job_alignment_summary
            )


        # ----------------------------------------------------
        # Matching strengths
        # ----------------------------------------------------

        with st.expander(
            "✅ Matching Strengths"
        ):

            if matching_strengths:

                for strength in matching_strengths:

                    st.success(
                        strength
                    )

            else:

                st.info(
                    "No matching strengths identified."
                )


        # ----------------------------------------------------
        # AI skill gaps
        # ----------------------------------------------------

        with st.expander(
            "🚨 AI Skill Gaps"
        ):

            if job_skill_gaps:

                for gap in job_skill_gaps:

                    st.warning(
                        gap
                    )

            else:

                st.info(
                    "No AI skill gaps identified."
                )


        # ----------------------------------------------------
        # Priority improvements
        # ----------------------------------------------------

        with st.expander(
            "🎯 Priority Improvements"
        ):

            if priority_improvements:

                for improvement in priority_improvements:

                    st.warning(
                        improvement
                    )

            else:

                st.info(
                    "No priority improvements identified."
                )


        # ----------------------------------------------------
        # Resume customization tips
        # ----------------------------------------------------

        with st.expander(
            "📝 Resume Customization Tips"
        ):

            if resume_customization_tips:

                for tip in resume_customization_tips:

                    st.info(
                        tip
                    )

            else:

                st.info(
                    "No customization tips identified."
                )


# ============================================================
# 8. NO RESULTS YET
# ============================================================

else:

    st.info(
        "Upload a resume and run the analysis "
        "to view your results."
    )