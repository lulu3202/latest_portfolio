import streamlit as st

def main():
    st.title("Skills & Tools ⚒️")
    st.markdown("Skills and tools I possess:")

    # List of skills and tools
    skills = [
        "Python",
        "JavaScript",
        "HTML/CSS",
        "Machine Learning",
        "Data Analysis",
        "SQL",
        "Git",
        "Stakeholder Management"
    ]

    # Display skills
    st.header("Skills")
    st.markdown("\n".join(skills))

    # Display tools
    st.header("Tools")
    st.markdown("- Streamlit\n- Jupyter Notebook\n- JIRA\n- PyCharm\n- Azure DevOps\n- GitHub")


if __name__ == '__main__':
    main()
