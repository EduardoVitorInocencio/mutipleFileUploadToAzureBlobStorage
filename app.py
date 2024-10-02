import streamlit as st
import os

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io

@st.cache_data
def load_image(imagefile):
    img = Image.open(imagefile)
    return img

# Função para fazer upload para o Azure Blob Storage
def upload_to_azure_blob(file):
    connection_string = st.secrets["azure"]["connection_string"]
    container_name = "teste" # Nome do container fixo
    blob_name = file.name # Nome do blob fixo

    # Conectar ao Azure Blob Storage usando a connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    #  Converter a imagem para bytes
    imagem_bytes = io.BytesIO(file.read())
    imagem_bytes.seek(0)

    try:
        blob_client.upload_blob(imagem_bytes, overwrite = True)
        return True
    except Exception as e:
        st.error(f"Erro ao fazer upload: {e}")
        return False
    

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
        
        # Botão de confirmação de upload
        confirm_upload  = st.button("Confirmar Upload")

        if confirm_upload:
            # Simulando a janela de confirmação (modal)
            for file in uploaded_files:
                upload_to_azure_blob(file)
            # st.success("Todas as imagens foram carregadas com sucesso!")


else:
    st.subheader("About App")
    st.write("Este é um aplicativo simples para upload de múltiplos arquivos de imagem e salvá-los no Azure Blob Storage.")