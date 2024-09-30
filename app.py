import streamlit as st
import os

from PIL import Image

@st.cache_data
def load_image(imagefile):
    img = Image.open(imagefile)
    return img

def save_uploaded_file (uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())

        return st.success("Saved {} To tempDir".format(uploaded_file.name))

st.title("Multiple file uploads App")
menu = ["Home","About"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Upload Multiple Files")

    uploaded_files = st.file_uploader("Upload Multiple images", type=["png","jpg","jpeg"], accept_multiple_files=True)
    if uploaded_files is not None:
        st.write(uploaded_files) # LIST
        for file in uploaded_files:
            st.write(file.name)
            st.image(load_image(file),width = 250)
            save_uploaded_file(file)

else:
    st.subheader("About App")