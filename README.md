
# Multiple File Uploads App - Streamlit

Welcome to the **Multiple File Uploads App** built using Streamlit. This application allows users to upload multiple image files and preview them directly in the app, with the option to save them locally. 

This README will guide you through the steps of cloning, running the app, and understanding how it works.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Run the Application](#how-to-run-the-application)
6. [Code Walkthrough](#code-walkthrough)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

This project demonstrates how to build a simple app using Streamlit where users can:
- Upload multiple image files (PNG, JPG, JPEG)
- Preview the uploaded images within the app
- Save uploaded images to a local directory (`tempDir`)

## Features

- **Multiple File Uploads**: Supports multiple image uploads simultaneously.
- **Image Preview**: Displays the uploaded images in real-time within the app.
- **File Storage**: Saves the uploaded files in a local directory.

## Requirements

Before running the app, make sure you have the following installed:
- Python 3.7+
- Streamlit
- PIL (Python Imaging Library) for image processing

## Installation

1. **Clone the Repository**

   To clone the repository, open your terminal and run:

   ```bash
   git clone https://github.com/your-username/multiple-file-uploads-app.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd multiple-file-uploads-app
   ```

3. **Install the Required Dependencies**

   You can install the dependencies listed in the `requirements.txt` file by running:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install the required libraries manually:

   ```bash
   pip install streamlit pillow
   ```

## How to Run the Application

After cloning the repository and installing the required packages, you can start the Streamlit app by running:

```bash
streamlit run app.py
```

Once the app is running, open your browser and go to `http://localhost:8501`.

## Code Walkthrough

### 1. **File Uploads and Image Handling**

```python
import streamlit as st
import os
from PIL import Image
```
- The necessary libraries are imported. We use **Streamlit** to build the web interface, **PIL** (Pillow) for image processing, and **os** to handle file operations.

### 2. **Cache and Load Images**

```python
@st.cache_data
def load_image(imagefile):
    img = Image.open(imagefile)
    return img
```
- The `load_image` function reads and opens the image using `PIL`. It uses the `@st.cache_data` decorator to improve performance by caching the images.

### 3. **Saving Uploaded Files Locally**

```python
def save_uploaded_file(uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success(f"Saved {uploaded_file.name} to tempDir")
```
- This function saves the uploaded files to a local directory called `tempDir`. If the directory doesn't exist, make sure to create it before running the app.

### 4. **Building the Streamlit App**

```python
st.title("Multiple file uploads App")
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Menu", menu)
```
- The app has two sections: "Home" and "About". Users can navigate using the sidebar menu.

### 5. **Main Functionality (Home Page)**

```python
if choice == "Home":
    st.subheader("Upload Multiple Files")
    uploaded_files = st.file_uploader("Upload Multiple images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    
    if uploaded_files is not None:
        st.write(uploaded_files)  # Displays list of uploaded files
        for file in uploaded_files:
            st.write(file.name)
            st.image(load_image(file), width=250)
            save_uploaded_file(file)
```
- In the "Home" section, users can upload multiple image files. The app then displays each uploaded image and saves it to the `tempDir` folder.

### 6. **About Section**

```python
else:
    st.subheader("About App")
```
- The "About" section provides information about the app.

## Contributing

Feel free to contribute to this project by submitting a pull request or reporting any issues. Make sure to follow the standard guidelines for contribution.

## License

This project is open-source and available under the [MIT License](LICENSE).
