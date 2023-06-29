# pandas help read csv content
import streamlit as st
import pandas
from streamlit_timeline import timeline

# Set the page configuration
st.set_page_config(page_title="devi karuppiah's portfolio", layout="wide", page_icon='👧🏽✨')


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Devi Karuppiah")
    content = """
    Hi, I am Devi! ✨
    
    Passionate about effective communication from a young age, on my completing my undergrad, I joined a multinational IT firm's program management group, improving technical documents across the SDLC, as a technical writer. Seeking growth, I pursued a Master's in IT Management in the US. With experience in market research at Research Now, project portfolio management at Deloitte, and cross-functional leadership at Microsoft, I thrive in diverse domains.

    Both at life and work, I always strive to see the big picture and embrace challenges as opportunities. As a strategic problem-solver, I possess core skill of project management, emotional intelligence and being comfortable with conflict. I bring enthusiasm, purpose, and a 'roll-up-your-sleeves' attitude to every task and project I've delivered . Being purpose driven, I'm always on the lookout to make a positive difference in people's lives.





    """
    st.info(content)

content2 = """
Scroll down to read more about me. Feel free to contact me at https://www.linkedin.com/in/devipriyakaruppiah/!
"""
st.write(content2)


st.title('Career Snapshot')

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


# Display heading
    st.title('Education 📚')
def main():
    # Define table data
    table_data = [
        ['Qualification', 'Major', 'Graduation Year', 'Institute', 'Score'],
        ['Bachelor\'s Degree', 'Btech', '2012', 'SASTRA University', '8.1 (Honors)'],
        ['Master\'s Degree', 'Information Technology Management', '2016', 'UT Dallas', '3.6'],
        ['Certification', 'AI Product Management Specialization', '2023', 'Duke University via Coursera', 'NA'],
        ['Certification', 'Mastering OpenAI Python APIs', '2023', 'Udemy', 'NA']
    ]

    # Display the table
    st.table(table_data)

if __name__ == '__main__':
    main()












