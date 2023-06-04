from dotenv import load_dotenv
import os
import streamlit as st
import requests
from typing import List
import json
import socket
from urllib3.connection import HTTPConnection

API_BASE_URL = "http://74.14.93.6:8000"

load_dotenv()



embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

from constants import CHROMA_SETTINGS
import chromadb

def list_of_collections():
    client = chromadb.Client(CHROMA_SETTINGS)
    return (client.list_collections())

def main():
    # Custom CSS
    st.markdown("""
        <style>
            .title {
                font-family: "Arial", sans-serif;
                color: #2E86C1;
                font-size: 48px;
            }
            .header {
                font-family: "Arial", sans-serif;
                color: #34495E;
                font-weight: bold;
            }
            .subheader {
                font-family: "Arial", sans-serif;
                color: #5D6D7E;
                font-weight: bold;
            }
            .text {
                font-family: "Arial", sans-serif;
                color: #5D6D7E;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .title {
                text-align: center;
                color: #4a4a4a;
            }
            .subtitle {
                text-align: center;
                font-size: 18px;
                color: #8a8a8a;
            }
        </style>
        <h1 class='title'>Fiber Mind</h1>
        <p class='subtitle'>You want to know what you don't know</p>
    """, unsafe_allow_html=True)
    
    

    # Document upload section
    #st.markdown("<h2 class='header'>Document Upload</h2>", unsafe_allow_html=True)
    #files = st.file_uploader("Upload document", accept_multiple_files=True)
    # collection_name = st.text_input("Collection Name") not working for some reason
    #if st.button("Embed"):
    #    embed_documents(files, "collection_name")

    # Query section
    st.markdown("<h2 class='header'>DataBase</h2>", unsafe_allow_html=True)
    collection_names = get_collection_names()
    selected_collection = st.selectbox("Database", collection_names)
    if selected_collection:
        query = st.text_input("What do you want to know?")
        if st.button("Bring me the knowledge"):
            retrieve_documents(query, selected_collection)

def embed_documents(files:List[st.runtime.uploaded_file_manager.UploadedFile], collection_name:str):
    endpoint = f"{API_BASE_URL}/embed"
    files_data = [("files", file) for file in files]
    data = {"collection_name": collection_name}

    response = requests.post(endpoint, files=files_data, data=data)
    if response.status_code == 200:
        st.success("Documents embedded successfully!")
    else:
        st.error("Document embedding failed.")
        st.write(response.text)

def get_collection_names():

    collections = list_of_collections()
    return [collection.name for collection in collections]

def retrieve_documents(query: str, collection_name: str):
    endpoint = f"{API_BASE_URL}/retrieve"
    data = {"query": query, "collection_name": collection_name}

    # Modify socket options for the HTTPConnection class
    HTTPConnection.default_socket_options = (
        HTTPConnection.default_socket_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            (socket.SOL_TCP, socket.TCP_KEEPIDLE, 45),
            (socket.SOL_TCP, socket.TCP_KEEPINTVL, 10),
            (socket.SOL_TCP, socket.TCP_KEEPCNT, 6)
        ]
    )

    response = requests.post(endpoint, params=data)
    if response.status_code == 200:
        result = response.json()
        st.markdown("<h3 class='subheader'>Results</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='text'>{result['results']}</p>", unsafe_allow_html=True)

        st.markdown("<h3 class='subheader'>Documents</h3>", unsafe_allow_html=True)
        for doc in result["docs"]:
            st.markdown(f"<p class='text'>{doc}</p>", unsafe_allow_html=True)
    else:
        st.error("Failed to retrieve documents.")
        st.write(response.text)

if __name__ == "__main__":
    main()
