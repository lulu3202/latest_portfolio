import streamlit as st
import pandas

st.header("Portfolio")


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"])
        st.write(row["description"])

        st.image("images/" + row["image"])
        st.write(f"[View Post]({row['url']})")

