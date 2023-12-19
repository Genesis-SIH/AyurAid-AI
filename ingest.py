import os

from langchain.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
)
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

DB_FAISS_PATH = r"vectorstore/db_faiss"
DATA_DIR = r"data"

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Create vector database
def create_vector_database():
    """
    Creates a vector database using document loaders and embeddings.

    This function loads data from PDF, markdown and text files in the 'data/' directory,
    splits the loaded documents into chunks, transforms them into embeddings using OpenaiAPI key,
    and finally persists the embeddings into a FAISS vector database.

    """
    # Initialize loaders for different file types
    

    text_loader = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
    loaded_documents = text_loader.load()

    # Split loaded documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunked_documents = text_splitter.split_documents(loaded_documents)

    
    # Initialize OpenAI embeddings
    openai_embeddings = OpenAIEmbeddings()

    # Create a FAISS vector database from the chunked documents
    vector_database = FAISS.from_documents(
        documents=chunked_documents,
        embedding=openai_embeddings,
    )

    vector_database.save_local(DB_FAISS_PATH)


if __name__ == "__main__":
    create_vector_database()
