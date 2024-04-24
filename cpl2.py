import streamlit as st
import os

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Define the folder from which you want to display files
folder_path = "./cns"  # Update with your folder name

# Get list of valid file extensions
valid_extensions = ('txt', 'py', 'cpp', 'java', 'json', 'js', 'html', 'css', 'bat', 'c', 'kt')

# List files in the specified folder with valid extensions
files = [''] + [file for file in os.listdir(folder_path)]

selected_file = st.selectbox('Select file', files)

if selected_file:
    if selected_file != '':
        file_path = os.path.join(folder_path, selected_file)
        st.text(f"{selected_file}")
        content = read_file_content(file_path)
        st.code(content, language='python')
    else:
        st.info("Select a file from the dropdown to view its content.")
else:
    st.text("Please select a file from the dropdown.")
