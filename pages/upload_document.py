import streamlit as st
import os

# Function to handle document upload
def upload_document_page():
    st.title("Upload Document")

    unit_id = st.session_state.get('selected_unit')
    if unit_id is None:
        st.error("No unit selected.")
        return

    uploaded_file = st.file_uploader("Choose a document file", type=["pdf", "doc", "docx"])

    if uploaded_file is not None:
        save_path = os.path.join("assets/documents", f"{unit_id}_{uploaded_file.name}")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Document uploaded successfully and saved to {save_path}")

    if st.button("Back to Unit Details"):
        st.session_state.page = 'unit_detail'
        st.session_state.selected_unit = unit_id

