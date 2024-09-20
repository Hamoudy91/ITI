import streamlit as st
import pandas as pd

# Load the CSV file from the repository (adjust the path if necessary)
data_path = 'PartITI2024.csv'
parts_df = pd.read_csv(data_path)

# Set up the Streamlit app interface
st.title("Part Finder")

# Step 1: Input box for model number
model_input = st.text_input("Enter your model number", "")

if model_input:
    # Filter the data based on the model number
    filtered_df = parts_df[parts_df['Model'] == model_input]
    
    if not filtered_df.empty:
        # Step 2: Dropdown for part description (TCLNA)
        part_description = st.selectbox("Select Part Description (TCLNA)", filtered_df['Part Description (TCLNA)'].unique())
        
        # Filter based on selected part description
        selected_part = filtered_df[filtered_df['Part Description (TCLNA)'] == part_description]
        
        if not selected_part.empty:
            # Outcome: Display Part Number, Alternate Part Number, Price, Type, and Year Sold
            st.write(f"**Part Number**: {selected_part['Part No.'].values[0]}")
            st.write(f"**Alternate Part Number**: {selected_part['Alternate Part No.'].values[0]}")
            st.write(f"**Price**: ${selected_part['Price'].values[0]}")
            st.write(f"**Type**: {selected_part['Type'].values[0]}")
            st.write(f"**Year Sold**: {selected_part['Year Sold'].values[0]}")
        else:
            st.write("No parts found for the selected description.")
    else:
        st.write("Model number not found.")
else:
    st.write("Please enter a model number to get started.")
