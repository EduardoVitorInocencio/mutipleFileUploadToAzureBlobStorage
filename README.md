
# Streamlit Multiple File Upload with Azure Blob Storage

This project is a simple web application built using **Streamlit** for uploading multiple image files and saving them directly to **Azure Blob Storage**. The application allows users to select multiple images, preview them, and upload the images to the cloud with a single click.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Azure Blob Storage Configuration](#azure-blob-storage-configuration)
- [License](#license)

## Features

- Upload multiple images simultaneously (.png, .jpg, .jpeg).
- Preview images before uploading.
- Store uploaded images directly in Azure Blob Storage.
- Simple and user-friendly interface with Streamlit.

## Technologies Used

- **Streamlit**: A Python library for building web applications quickly and easily.
- **Azure Blob Storage**: Cloud storage service for saving the uploaded images.
- **Pillow (PIL)**: Image processing library used to handle and display images.

## Setup Instructions

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- Azure account (to set up Blob Storage)

### Installation

1. Clone the repository:

\`\`\`bash
git clone <repository-url>
cd <repository-folder>
\`\`\`

2. Install the required dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Add your Azure Blob Storage connection string to **Streamlit secrets**:

- Open the `.streamlit/secrets.toml` file and add your Azure connection string under the following format:

\`\`\`toml
[azure]
connection_string = "your-azure-connection-string"
\`\`\`

## Usage

1. Run the Streamlit app:

\`\`\`bash
streamlit run app.py
\`\`\`

2. Upload multiple images through the interface. The images will be displayed for preview and uploaded to Azure Blob Storage after confirmation.

## Azure Blob Storage Configuration

Make sure you have an Azure Blob Storage account and a container created:

1. Log into [Azure Portal](https://portal.azure.com/).
2. Create a new Storage Account.
3. Inside the Storage Account, create a Blob Container (you can use the container name `teste` as mentioned in the code).

Ensure that your **connection string** is correctly configured in your Streamlit secrets to allow access to Azure.

## License

This project is licensed under the MIT License.
