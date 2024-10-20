import streamlit as st
from langchain_groq import ChatGroq
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv

load_dotenv() 

# Initialize the LLM with the ChatGroq model
llm = ChatGroq(
    model="llama3-groq-70b-8192-tool-use-preview",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("get_llama")
)

# Styling for the background color
background_color = '''
<style>
    .stApp {
        background-color: palegreen;
    }
</style>
'''
st.markdown(background_color, unsafe_allow_html=True)

# Application Title
st.title("AI Resume Creator 💌")

# -----------------------------------------
# Section 1: Profile Details
st.header("Profile Details")

Full_Name = st.text_input("Full Name",placeholder="Enter your full name")
professional_title = st.text_input("Professional Title",placeholder="e.g., Software Engineer")
phone_Number = st.text_input("Phone Number", placeholder="Enter your phone number")
Email_Address = st.text_input("Email Address",placeholder="Enter your email address")
Linked_in = st.text_input("LinkedIn URL",placeholder="Enter your LinkedIn profile URL")
github = st.text_input("GitHub/Portfolio URL", placeholder="Enter your GitHub profile URL")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 2: Professional Summary
st.header("Professional Summary")
professional_summary = st.text_area("Write your professional summary", placeholder="A brief summary about yourself")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 3: Skills
st.header("Skills")
technical_skills = st.text_area("Technical Skills (e.g., Python, TensorFlow)",placeholder="Enter skills separated by commas, e.g., Python, AI, Machine Learning")
soft_skills = st.text_area("Soft Skills (Optional)")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 4: Education
st.header("Education")
degree = st.text_input("Degree",placeholder="e.g., Bachelor of Science")
major = st.text_input("Major",placeholder="e.g., Computer Science")
institution = st.text_input("Institution",placeholder="e.g., Stanford University")
graduation_year = st.text_input("Graduation Year or Expected Date",placeholder="e.g., 2023")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 5: Work Experience
st.header("Work Experience")
work_experience = st.text_area("List your work experience (Company, Title, Dates, Responsibilities)",placeholder="Describe your work experience")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 6: Projects
st.header("Projects")
projects = st.text_area("Describe your projects (Name, Description, Technologies, Achievements)",placeholder="Describe your projects with details")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 7: Certifications and Training
st.header("Certifications and Training")
courses = st.text_input("Course Name", placeholder="Enter relevant courses")
issuing_organization = st.text_input("Issuing Organization", placeholder="e.g., Coursera")
completion_date = st.text_input("Completion Date", placeholder="e.g., July 2024")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Section 8: Awards and Achievements
st.header("Awards and Achievements")
awards = st.text_area("List your awards and achievements", placeholder="List your awards and achievements")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# -----------------------------------------
# Function to Prepare Prompt Template
def prepare_prompt(data):
    template = """
    Create an ATS-friendly professional resume based on the following user inputs:

    Full Name: {Full_Name}
    Professional Title: {professional_title}
    Phone Number: {phone_Number}
    Email Address: {Email_Address}
    LinkedIn: {Linked_in}
    GitHub/Portfolio: {github}

    Professional Summary:
    {professional_summary}

    Technical Skills:
    {technical_skills}

    Soft Skills:
    {soft_skills}

    Education:
    - Degree: {degree}
    - Major: {major}
    - Institution: {institution}
    - Graduation Year: {graduation_year}

    Work Experience:
    {work_experience}

    Projects:
    {projects}

    Certifications and Training:
    - Course: {courses}
    - Organization: {issuing_organization}
    - Completion Date: {completion_date}

    Awards and Achievements:
    {awards}
    """
    return PromptTemplate(template=template).format(**data)

# -----------------------------------------
# Handling Resume Generation
if st.button("Generate Resume"):
    # Collect inputs into a dictionary
    data = {
        "Full_Name": Full_Name,
        "professional_title": professional_title,
        "phone_Number": phone_Number,
        "Email_Address": Email_Address,
        "Linked_in": Linked_in,
        "github": github,
        "professional_summary": professional_summary,
        "technical_skills": technical_skills,
        "soft_skills": soft_skills,
        "degree": degree,
        "major": major,
        "institution": institution,
        "graduation_year": graduation_year,
        "work_experience": work_experience,
        "projects": projects,
        "courses": courses,
        "issuing_organization": issuing_organization,
        "completion_date": completion_date,
        "awards": awards
    }

    # Prepare the prompt using the template
    prompt = prepare_prompt(data)

    # Create the LLMChain and generate a response
    chain = LLMChain(llm=llm, prompt=PromptTemplate(template=prompt))
    response = chain.run({})

    # Handle the response and save as a text file
    if response:
        resume_text = response
        st.text_area("Generated Resume", resume_text, height=400)
        
        st.success("Resume Generated Successfully✅")
        # Download option for the generated resume
        st.download_button(
            label="Download Resume as Text File",
            data=resume_text,
            file_name=f"{Full_Name}_resume.txt",
            mime="text/plain"
        )
    else:
        st.error("Failed to generate the resume. Please try again.")
