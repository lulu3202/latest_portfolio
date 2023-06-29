import streamlit as st
from streamlit_timeline import timeline

# Set the page configuration
st.set_page_config(page_title="devikaruppiah's portfolio", layout="wide", page_icon='👧🏽✨')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Devi Karuppiah")
    content = """
    Hi, I am Devi! ✨

    Passionate about effective communication from a young age, on my completing my undergrad, I joined a multinational IT firm's program management group, improving technical documents across the SDLC, as a technical writer. Seeking growth, I pursued a Master's in IT Management in the US. With experience in market research at Research Now, project portfolio management at Deloitte, and cross-functional leadership at Microsoft, I thrive in diverse domains.

    Both at life and work, I always strive to see the big picture and embrace challenges as opportunities. As a strategic problem-solver, I possess core skill of project management, emotional intelligence and being comfortable with conflict. I bring enthusiasm, purpose, and a 'roll-up-your-sleeves' attitude to every task and project I've delivered. Being purpose driven, I'm always on the lookout to make a positive difference in people's lives.
    """
    st.info(content)

content2 = """
Scrolldown to read more about me. Feel free to contact me at [LinkedIn](https://www.linkedin.com/in/devipriyakaruppiah/)!
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
    ['Certification', 'Mastering OpenAI Python APIs', '2023', 'Udemy', 'NA']
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
