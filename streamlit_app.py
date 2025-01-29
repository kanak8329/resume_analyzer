# import streamlit as st
# import requests
#
# st.title("AI-Powered Resume Analyzer")
#
# # Upload resume
# resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
#
# # Input job description
# job_description = st.text_area("Paste the job description here:")
#
# if st.button("Analyze"):
#     if resume_file and job_description:
#         # Send data to Flask backend
#         response = requests.post(
#             "http://127.0.0.1:5000/analyze",
#             files={"resume": resume_file},
#             data={"job_description": job_description}
#         ).json()
#
#         # Display results
#         st.write(f"ATS Score: {response['ats_score']}%")
#         st.write(f"Missing Keywords: {', '.join(response['missing_keywords'])}")
#         st.write(f"Suggestions: {response['suggestions']}")
#     else:
#         st.error("Please upload a resume and paste the job description.")

import streamlit as st
import requests

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #4f8bf9;
        text-align: center;
    }
    .stButton button {
        background-color: #4f8bf9;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #3a6bb7;
    }
    .stFileUploader {
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        border-radius: 5px;
        padding: 10px;
    }
    .result {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1>AI-Powered Resume Analyzer</h1>", unsafe_allow_html=True)

# Sidebar for additional information
st.sidebar.title("About")
st.sidebar.info(
    """
    This app helps job seekers optimize their resumes for Applicant Tracking Systems (ATS).
    Upload your resume and paste the job description to get an ATS score and improvement suggestions.
    """
)

# File Uploader for Resume
st.markdown("### Upload Your Resume (PDF)")
resume_file = st.file_uploader("", type="pdf", key="resume_uploader")

# Text Area for Job Description
st.markdown("### Paste the Job Description")
job_description = st.text_area("", placeholder="Paste the job description here...", height=200)

# Analyze Button
if st.button("Analyze Resume"):
    if resume_file and job_description:
        # Send data to Flask backend
        with st.spinner("Analyzing your resume..."):
            response = requests.post(
                "http://127.0.0.1:5000/analyze",
                files={"resume": resume_file},
                data={"job_description": job_description},
            ).json()

        # Display results in a visually appealing way
        st.markdown("<div class='result'>", unsafe_allow_html=True)
        st.markdown("### Analysis Results")
        st.markdown(f"<p>ATS Score: <strong>{response['ats_score']}%</strong></p>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h4>Missing Keywords:</h4>", unsafe_allow_html=True)
        st.markdown("<ul>" + "".join([f"<li>{keyword}</li>" for keyword in response["missing_keywords"]]) + "</ul>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h4>Suggestions:</h4>", unsafe_allow_html=True)
        st.markdown("<ul>" + "".join([f"<li>{suggestion}</li>" for suggestion in response["suggestions"]]) + "</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please upload a resume and paste the job description.")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; color: #777;">
        Built with ❤️ by kanak chouksey
    </div>
    """,
    unsafe_allow_html=True,
)

# Smooth scroll functionality
import streamlit.components.v1 as components

smooth_scroll_script = """
<script>
function smoothScroll() {
    document.querySelectorAll('.stButton button')[0].scrollIntoView({ behavior: 'smooth' });
}
smoothScroll();
</script>
"""

components.html(smooth_scroll_script)
