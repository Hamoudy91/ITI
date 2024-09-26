import streamlit as st
import pandas as pd
import spacy

# Load spaCy model for NLP
nlp = spacy.load('en_core_web_sm')

# Load the updated CSV file
data_path = 'PartITIT2024 - Sheet1.csv'  # Change the path based on the file
try:
    parts_df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    st.write("File loaded successfully.")
except FileNotFoundError:
    st.error(f"File not found: {data_path}. Please ensure the file is uploaded.")
    st.stop()
except pd.errors.ParserError:
    st.error(f"Error parsing the file: {data_path}. Please check the file formatting.")
    st.stop()

# Display file structure to debug issues
st.write(parts_df.head())

# Continue the chatbot implementation or other functionalities here
