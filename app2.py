import streamlit as st
from PIL import Image
import pytesseract

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"D:\Luminar\Study\Deep learning\DL Project\OCR\Tesseract-OCR\tesseract.exe"

# Page Configuration
st.set_page_config(
    page_title="Resume Filter",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Minimalist Professional CSS
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background: #ffffff;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Typography */
    .main-title {
        font-size: 2rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        color: #6b7280;
        font-size: 0.95rem;
        font-weight: 400;
        margin-bottom: 3rem;
    }
    
    /* Cards with subtle borders */
    # .card {
    #     background: #ffffff;
    #     border: 1px solid #e5e7eb;
    #     border-radius: 8px;
    #     padding: 2rem;
    #     margin-bottom: 1.5rem;
    # }
    
    /* Section titles */
    .section-title {
        font-size: 0.875rem;
        font-weight: 600;
        color: #1a1a1a;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1.5rem;
    }
    
    /* Score display */
    .score-box {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .score-value {
        font-size: 3rem;
        font-weight: 600;
        color: #1a1a1a;
        margin: 0;
        line-height: 1;
    }
    
    .score-label {
        font-size: 0.875rem;
        color: #6b7280;
        margin-top: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .score-detail {
        font-size: 0.875rem;
        color: #9ca3af;
        margin-top: 0.75rem;
    }
    
    /* Skills section */
    .skills-header {
        font-size: 0.875rem;
        font-weight: 600;
        color: #1a1a1a;
        margin: 2rem 0 1rem 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .skills-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    
    .skill-tag {
        background: #f9fafb;
        color: #1a1a1a;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        font-size: 0.875rem;
        font-weight: 500;
        border: 1px solid #e5e7eb;
    }
    
    .skill-tag.missing {
        background: #fef2f2;
        border-color: #fecaca;
        color: #991b1b;
    }
    
    /* Button */
    .stButton > button {
        background: #1a1a1a;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 2rem;
        font-size: 0.875rem;
        font-weight: 500;
        width: 100%;
        margin-top: 1.5rem;
        letter-spacing: 0.3px;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background: #374151;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 6px;
        border: 1px solid #e5e7eb;
        padding: 0.75rem;
        font-size: 0.875rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1a1a1a;
        box-shadow: 0 0 0 1px #1a1a1a;
    }
    
    .stTextInput > label {
        font-size: 0.875rem;
        font-weight: 500;
        color: #1a1a1a;
    }
    
    /* File uploader */
    .stFileUploader {
        border: 1px dashed #d1d5db;
        border-radius: 6px;
        padding: 1.5rem;
        background: #fafafa;
    }
    
    .stFileUploader > label {
        font-size: 0.875rem;
        font-weight: 500;
        color: #1a1a1a;
    }
    
    .stFileUploader [data-testid="stFileUploaderDropzone"] {
        min-height: 120px;
    }
    
    .stFileUploader [data-testid="stFileUploaderDropzoneInput"] {
        display: none;
    }
    
    .stFileUploader section {
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
    }
    
    .stFileUploader button {
        background: #1a1a1a;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
    }
    
    /* Image container */
    .image-box {
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        overflow: hidden;
        margin-top: 1rem;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 6px;
        border: 1px solid #e5e7eb;
    }
    
    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">Resume Filter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze resume skills with OCR technology</div>', unsafe_allow_html=True)

# Initialize session state
if "image" not in st.session_state:
    st.session_state.image = None
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""
if "skills" not in st.session_state:
    st.session_state.skills = ""

# Two column layout
col1, col2 = st.columns([1, 1], gap="large")

# LEFT COLUMN - Upload & Preview
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Upload Resume</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose image file",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    
    if uploaded_file:
        st.session_state.image = Image.open(uploaded_file)
        extracted = pytesseract.image_to_string(st.session_state.image)
        st.session_state.extracted_text = extracted.replace("\n", " ").lower().strip()
    
    if st.session_state.image:
        st.markdown('<div class="image-box">', unsafe_allow_html=True)
        fixed_img = st.session_state.image.resize((400, 500))
        st.image(fixed_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT COLUMN - Skills Input & Results
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Required Skills</div>', unsafe_allow_html=True)
    
    st.session_state.skills = st.text_input(
        "Enter skills (comma separated)",
        value=st.session_state.skills,
        placeholder="python, machine learning, docker"
    )
    
    def clean_text(text):
        text = text.lower().strip()
        while "  " in text:
            text = text.replace("  ", " ")
        return text
    
    if st.button("Analyze Resume"):
        if st.session_state.extracted_text == "":
            st.warning("Please upload a resume image first")
        elif st.session_state.skills.strip() == "":
            st.warning("Please enter at least one skill")
        else:
            cleaned = clean_text(st.session_state.skills)
            skills_list = [s.strip() for s in cleaned.split(",") if s.strip()]
            
            score = 0
            found = []
            
            for skill in skills_list:
                if skill.lower() in st.session_state.extracted_text.lower():
                    score += 1
                    found.append(skill)
            
            percentage = (score / len(skills_list)) * 100 if skills_list else 0
            
            # Score Display
            st.markdown(f"""
            <div class="score-box">
                <div class="score-value">{round(percentage)}%</div>
                <div class="score-label">Match Score</div>
                <div class="score-detail">{score} of {len(skills_list)} skills found</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Matched Skills
            if found:
                st.markdown('<div class="skills-header">Matched Skills</div>', unsafe_allow_html=True)
                skills_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in found])
                st.markdown(f'<div class="skills-grid">{skills_html}</div>', unsafe_allow_html=True)
            
            # Missing Skills
            missing = [s for s in skills_list if s not in found]
            if missing:
                st.markdown('<div class="skills-header">Missing Skills</div>', unsafe_allow_html=True)
                missing_html = ''.join([f'<span class="skill-tag missing">{skill}</span>' for skill in missing])
                st.markdown(f'<div class="skills-grid">{missing_html}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)