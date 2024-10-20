import streamlit as st

# Styling for the Streamlit app background
background_color = '''
<style>
    .stApp {
        background-color: #1b1b1b;  /* Professional dark background */
        color: white;  /* Ensure all text is readable */
    }
</style>
'''

st.markdown(background_color, unsafe_allow_html=True)
st.title("AI Resume Creator 💌")

# ---------------------------------------------------------------
# Section 1: Profile Details
st.header("Profile Details")
full_name = st.text_input("Full Name", placeholder="Enter your full name", key="full_name")
professional_title = st.text_input("Professional Title", placeholder="e.g., Software Engineer", key="title")
phone_number = st.text_input("Phone Number", placeholder="Enter your phone number", key="phone")
email_address = st.text_input("Email", placeholder="Enter your email address", key="email")
linkedin = st.text_input("LinkedIn URL", placeholder="Enter your LinkedIn profile URL", key="linkedin")
github = st.text_input("GitHub URL", placeholder="Enter your GitHub profile URL", key="github")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 2: Professional Summary
st.header("Professional Summary")
professional_summary = st.text_area("Professional Summary", placeholder="A brief summary about yourself")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 3: Skills
st.header("Skills")
skills_input = st.text_area("Skills", placeholder="Enter skills separated by commas, e.g., Python, AI, Machine Learning")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 4: Education
st.header("Education")
degree = st.text_input("Degree", placeholder="e.g., Bachelor of Science")
major = st.text_input("Major", placeholder="e.g., Computer Science")
institution = st.text_input("Institution", placeholder="e.g., Stanford University")
graduation_year = st.text_input("Graduation Year", placeholder="e.g., 2023")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 5: Work Experience
st.header("Work Experience (Optional)")
work_experience = st.text_area("Work Experience", placeholder="Describe your work experience")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 6: Projects
st.header("Projects")
projects_input = st.text_area("Projects", placeholder="Describe your projects with details")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 7: Certifications and Training
st.header("Certifications and Training")
courses = st.text_input("Courses", placeholder="Enter relevant courses")
issuing_organization = st.text_input("Issuing Organization", placeholder="e.g., Coursera")
completion_date = st.text_input("Completion Date", placeholder="e.g., July 2024")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Section 8: Awards and Achievements
st.header("Awards and Achievements (Optional)")
awards = st.text_area("Awards", placeholder="List your awards and achievements")

st.markdown("<hr style='height:2px; background-color: white;'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Generate Resume in Text Format
if st.button("Generate Text Resume"):
    # Basic Validation
    # if not all([full_name, professional_title, phone_number, email_address, professional_summary, 
    #             skills_input, degree, major, institution, graduation_year, projects_input, 
    #             courses, issuing_organization, completion_date]):
    #     st.error("Please fill in all required fields.")
        # Creating the resume text
        resume_text = f"""
        {full_name}
        {professional_title}
        Phone: {phone_number}
        Email: {email_address}
        LinkedIn: {linkedin}
        GitHub: {github}

        Professional Summary:
        {professional_summary}

        Skills:
        {skills_input}

        Education:
        Degree: {degree}
        Major: {major}
        Institution: {institution}
        Graduation Year: {graduation_year}

        Work Experience:
        {work_experience or 'N/A'}

        Projects:
        {projects_input}

        Certifications and Training:
        Courses: {courses}
        Issuing Organization: {issuing_organization}
        Completion Date: {completion_date}

        Awards and Achievements:
        {awards or 'N/A'}
        """

        # Display the generated resume
        st.text_area("Generated Resume", value=resume_text, height=600)

        # Option to download the text as a file
        st.download_button("Download Resume as Text File", data=resume_text, file_name='resume.txt', mime='text/plain')
