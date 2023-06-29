import streamlit as st
import pandas as pd

def main():
    # Set page title and icon
    st.set_page_config(page_title='Portfolio App', page_icon='📚')

    # Display heading
    st.title('Education 📚')

    # Define table data
    table_data = [
        ['Qualification', 'Major', 'Graduation Year', 'Institute', 'Score'],
        ['Bachelor\'s Degree', 'Btech', '2012', 'SASTRA University', '8.1 (Honors)'],
        ['Master\'s Degree', 'Information Technology Management', '2016', 'UT Dallas', '3.6'],
        ['Certification', 'AI Product Management Specialization', '2023', 'Duke University via Coursera', 'NA']
    ]

    # Create a DataFrame with the table data
    df = pd.DataFrame(table_data[1:], columns=table_data[0])

    # Style the header row
    styles = [
        {'selector': 'th', 'props': [('background-color', '#E6CCFF'), ('border-radius', '0px')]}
    ]
    styled_df = df.style.set_table_styles(styles)

    # Display the styled DataFrame
    st.dataframe(styled_df, height=200)

if __name__ == '__main__':
    main()

