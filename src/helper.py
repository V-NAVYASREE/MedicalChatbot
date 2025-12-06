from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter     
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

def load_pdf_file(data):
    loader = DirectoryLoader(data, glob="**/*.pdf", loader_cls=PyMuPDFLoader)

    documents=loader.load()
    return documents

def filter_to_minimal_docs(docs:List[Document])->List[Document]:
   minimal_docs=[]
   for doc in docs:
       src=doc.metadata.get("source")
       minimal_docs.append(
            Document(

                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
   return minimal_docs
   
   """ given a list of documents, return a list of documents with only page_content and source metadata
   """
    
#split the doc into smller chunks
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    texts=text_splitter.split_documents(minimal_docs)
    return texts
def download_hugging_face_embeddings():
    """ download the embeddings model from huggingface and return the embeddings object"""
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    embeddings=HuggingFaceEmbeddings(model_name=model_name,
                                    
                                   )
    
    return embeddings
embedding=download_hugging_face_embeddings()
embedding