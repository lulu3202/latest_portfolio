import streamlit as st
from streamlit_timeline import timeline

# Set the page configuration
st.set_page_config(page_title="devikaruppiah's portfolio", layout="wide", page_icon='👧🏽✨')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:

    content = """
    Hi, I am Devi! ✨

    I've always been an editor at heart. It was this love for communication that made me start out as a technical writer for a multinational IT firm. I wanted more out of life and work. I got my wish granted on Xmas of 2014, when I stepped into US for the first time to pursue my Master's in IT Management at UT Dallas. It has been an eventful 8+ years.
    
    Be it life or work, I always see the big picture and embrace challenges as opportunities. I shine at creating clarity, generating excitment and getting things done. I bring enthusiasm and a 'roll-up-your-sleeves' attitude to every task. Being purpose driven, I'm wired to look for opportunities to make a positive difference in people's lives.
    """
    st.info(content)

content2 = """
Scroll down to read more about me. Feel free to contact me at [LinkedIn](https://www.linkedin.com/in/devipriyakaruppiah/)!
"""
st.markdown(content2)

st.title('Career Snapshot')

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# Display heading
st.title('Education📚')

# Define table data
table_data = [
    ['Qualification', 'Major', 'Graduation Year', 'Institute', 'Score'],
    ["Bachelor's Degree", 'Btech', '2012', 'SASTRA University', '8.1 (Honors)'],
    ["Master's Degree", 'Information Technology Management', '2016', 'UT Dallas', '3.6'],
    ['Certification', 'AI Product Management Specialization', '2023', 'Duke University via Coursera', 'NA'],
    ['Certification', 'Mastering OpenAI Python APIs', '2023', 'Udemy', 'NA'],
    ['Certification', 'Learn Python By Building 15 Projects & ChatGPT', '2023', 'Udemy', 'NA']
]

# Display the table
st.table(table_data)

# Display heading
st.title('Achievements🥇')

# Define achievements bullet points
achievements = [
    "Cohort’19, VolunteerNow Young Leader Council: YLC trains young professionals to serve on non-profit boards",
    "Completed Harvard’s Sustainable Business Strategy, a program that develops purpose-driven leaders, Dec 2019",
    "Served as a board member on Deloitte's Step-up DFW chapter - an organization that offered pro bono consulting to NGOs",
    "Commencement Speaker addressing the class of Fall 2016 at The University of Texas at Dallas",
    "Dean’s Advisory Council, UT Dallas; Leader of school-wide social media project impacting 8200+ students",
    "Recipient of Dean’s Impact Scholarship for displaying extraordinary impact to Jindal school of Management",
    "Awarded JSOM Perspectives Top Grad Contributor 2016 for contributing the most to the school’s official blog",
    "Editor-in-chief of BioSpace Newsletter, SASTRA University; led a team of 4 to launch a successful department-wide monthly newsletter to an academic community of 500+ members",
    "Recipient of two awards ('On the Spot', 'CLP Faculty') from Learning and Development department at Tata Consultancy Services, for outstanding contribution to the presentation sessions conducted for Associates"
]

# Render the achievements as bullet points using st.markdown()
st.markdown("<ul>" + "".join(f"<li>{achievement}</li>" for achievement in achievements) + "</ul>", unsafe_allow_html=True)
