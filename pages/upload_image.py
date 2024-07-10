import streamlit as st
import os

# Function to handle image upload
def upload_image_page():
    st.title("Upload Image")

    unit_id = st.session_state.get('selected_unit')
    if unit_id is None:
        st.error("No unit selected.")
        return

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        save_path = os.path.join("assets/images", f"{unit_id}_{uploaded_file.name}")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Image uploaded successfully and saved to {save_path}")

    if st.button("Back to Unit Details"):
        st.session_state.page = 'unit_detail'
        st.session_state.selected_unit = unit_id

