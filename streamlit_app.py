import streamlit as st
import pandas as pd
import csv
import os

st.set_page_config(page_title="TCL Parts Finder", layout="wide")

# Define the file path
DATA_PATH = "https://tclo365-my.sharepoint.com/:x:/g/personal/mario_campanile_tcl_com/EYNxpiHWKAhFvB0tW5GiWxIB-g-OQZ4Hf1YwxaJ7EVdDxA"  # Update this path

try:
    if os.path.exists(DATA_PATH):
        parts_df = pd.read_csv(DATA_PATH, 
                          sep=',',
                          encoding='utf-8',
                          on_bad_lines='skip',
                          quoting=csv.QUOTE_MINIMAL)
        
        # Rest of your code remains the same
        parts_df.columns = parts_df.columns.str.strip()
        
        model_input = st.text_input("Enter Model Number:")
        
        if model_input:
            filtered_df = parts_df[parts_df['Model'].str.contains(model_input, case=False, na=False)]
            
            if filtered_df.empty:
                st.warning("No parts found for this model.")
            else:
                part_description = st.selectbox(
                    "Select Part Description",
                    filtered_df['Part Description (TCLNA)'].unique()
                )
                
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
    else:
        st.error(f"File not found at: {DATA_PATH}")

except Exception as e:
    st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("TCL Parts Finder App")
