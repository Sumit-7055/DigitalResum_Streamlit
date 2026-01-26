from pathlib import Path
import streamlit as st
from  PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"resources"/"SumitKumar_Resume.pdf"
profile_pic = current_dir/"resources"/"Image.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sumit Kumar"
PAGE_ICON = ":wave:"
NAME = "Sumit Kumar"
DESCRIPTION = """
System Engineer @TCS | Backend developer| Microservices | Springboot | Java
"""
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sumit007kumar/",
    "GitHub": "https://github.com/Sumit-7055",
    "EMAIL" : "sumit5507kr@gmail.com",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/pdf",
    )

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- About ---
st.write('\n')
with st.expander("👤 About Me", expanded=False):
    st.markdown("""
    I’m a **Java Backend Developer** with 2 years of hands-on experience, currently working with **Citibank (via TCS)** in the BFSI domain, where I build robust, scalable APIs across the full Software Development Lifecycle (SDLC) — from requirement analysis and development to testing and release.

    I’ve worked on multiple APIs end to end, taking them from initial development all the way to production deployment, with a strong focus on performance, stability, and maintainability.

    **Collaboration** is a key part of my role — I work closely with data insertion teams, Kafka teams, QA/testing teams, and product owners to deliver high-quality backend solutions aligned with business requirements.

    ### 🔧 What I Actively Work On:
    • Java & Spring Boot backend API development  
    • REST and SOAP APIs  
    • Exposure to load balancer concepts and distributed systems  
    • Writing comprehensive JUnit test cases  
    • Experience building APIs using Flask (Python) based on team requirements  

    ### 🛠️ Tools & Platforms I’ve Worked With:
    Bitbucket, GitHub, OpenShift, Harness, Kafka, SonarQube, Snyk, Diffblue, and internal AI-based engineering tools used at Citibank.

    I strongly believe in writing clean, well-documented, and maintainable code. I particularly enjoy exception handling and error management, with a preference for structured approaches like global exception handlers to build resilient applications.

    I’m continuously improving my skills and am actively open to **Java Backend / Spring Boot roles** where I can contribute from Day 1.  
    _Let’s connect._
    """)

# --- SKILLS ---
st.write('\n')
with st.expander("🛠️ Technical Skills", expanded=False):
    st.markdown("""
    **Programming & Frameworks:**  
    Java, Spring Boot, REST APIs, SOAP APIs, Microservices, Flask (Python)

    **Testing & Code Quality:**  
    JUnit, Unit Testing, SonarQube, Diffblue

    **DevOps & Platforms:**  
    Git, GitHub, Bitbucket, OpenShift, Harness, CI/CD Pipelines

    **Security & Quality Tools:**  
    Snyk, Internal AI tools

    **Concepts:**  
    SDLC, Load Balancer Concepts, Distributed Systems, Exception Handling, Global Exception Handling
    """)


#workExperience
with st.expander("💼 Work Experience", expanded=False):
    st.markdown("""
    **Tata Consultancy Services (TCS)**  
    *System Engineer – Java Backend Developer | Citibank | BFSI Domain*  
    📍 Kolkata, India 🗓️ Aug 2024 – Present

    ### 🔧 Roles & Responsibilities:
    - Designed, developed, and maintained scalable backend APIs using Java and Spring Boot for enterprise BFSI applications.
    - Took end-to-end ownership of multiple APIs, handling requirement analysis, development, testing, deployment, and production support.
    - Successfully delivered 3 production-ready APIs, ensuring high performance, reliability, and security.
    - Implemented RESTful and SOAP APIs aligned with enterprise architecture and compliance standards.
    - Wrote comprehensive JUnit test cases, improving test coverage and ensuring long-term maintainability.
    - Collaborated with Kafka teams, data ingestion teams, QA, and product owners to ensure seamless integration and timely delivery.
    - Worked extensively with CI/CD pipelines using GitHub, Bitbucket, Harness, and OpenShift.
    - Improved code quality and security using SonarQube, Snyk, and Diffblue.
    - Developed backend services using Flask (Python) based on evolving project needs.
    - Implemented global exception handling and structured error management for resilient services.
    """)

#Certifications
with st.expander("🎓 Certifications", expanded=False):
    st.markdown("""
    - **Oracle Certified Associate (OCA), Java SE 8 Programmer**  
    - **Oracle Cloud Infrastructure Certified Foundation Associate**  
    - **Oracle Cloud Infrastructure Certified AI Foundation Associate**
    """)

with st.expander("📚 Education", expanded=False):
    st.markdown("""
    **Anna University**  
    *B.Tech in Electronics Engineering*  
    🗓️ July 2020 – June 2024

    **Sainik School Kazhakootam**
    """)

