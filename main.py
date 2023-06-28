import streamlit as st
import pandas

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
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

















