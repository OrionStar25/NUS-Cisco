import sys
sys.path.append('../')

from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from utils.utils import *


def main():
    # Load documents
    print("Loading documents")
    loader = DirectoryLoader('../task_2/products/access_point_modules', glob="**/*.txt", show_progress=True)
    documents = loader.load()

    # Split documents
    print("Splitting documents")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    print("Creating embeddings")
    embeddings = HuggingFaceEmbeddings()

    # Create index 
    print("Creating index") 
    db = FAISS.from_documents(docs, embeddings)

    # Save the index
    print("Saving index")
    pkl = db.serialize_to_bytes()  # serializes the faiss
    write_text_to_file('faiss_index.pkl', pkl)


if __name__=='__main__':
    main()
