import streamlit as st
import pandas as pd
import csv

st.set_page_config(page_title="TCL Parts Finder", layout="wide")

st.title("TCL Parts Finder")

# File upload
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file:
   try:
       parts_df = pd.read_csv(uploaded_file, 
                             sep=',',
                             encoding='utf-8',
                             on_bad_lines='skip',
                             quoting=csv.QUOTE_MINIMAL)
       
       # Clean column names
       parts_df.columns = parts_df.columns.str.strip()
       
       # Debug column names
       st.write("Available columns:", parts_df.columns.tolist())
       
       # User input for Model Number
       model_input = st.text_input("Enter Model Number:")
       
       if model_input:
           try:
               filtered_df = parts_df[parts_df['Model'].str.contains(model_input, case=False, na=False)]
               
               if filtered_df.empty:
                   st.warning("No parts found for this model.")
               else:
                   # Display filtered results
                   st.write(f"Found {len(filtered_df)} matching parts")
                   
                   # Part selection
                   part_description = st.selectbox(
                       "Select Part Description",
                       filtered_df['Part Description (TCLNA)'].unique()
                   )
                   
                   # Display part details
                   selected_part = filtered_df[filtered_df['Part Description (TCLNA)'] == part_description]
                   
                   if not selected_part.empty:
                       col1, col2 = st.columns(2)
                       
                       with col1:
                           st.write("### Part Details")
                           st.write(f"**Part Number:** {selected_part['Part No.'].iloc[0]}")
                           st.write(f"**Year Sold:** {selected_part['Year Sold'].iloc[0]}")
                           st.write(f"**Type:** {selected_part['Type'].iloc[0]}")
                       
                       with col2:
                           if st.checkbox("Show Price"):
                               st.write(f"**Price:** ${selected_part['Price'].iloc[0]:.2f}")
                   
           except AttributeError as e:
               st.error(f"Error filtering data: {str(e)}")
               st.write("Please check if 'Model' column exists in your CSV")
               
   except Exception as e:
       st.error(f"Error reading file: {str(e)}")
       st.write("Please ensure your CSV file is properly formatted")

else:
   st.info("Please upload a CSV file to begin")

# Add footer
st.markdown("---")
st.markdown("TCL Parts Finder App")
