from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as LangchainPinecone  # ✅ Avoid Import Conflict
from langchain_pinecone import PineconeVectorStore  # ✅ Correct Import
from src.helper import pdf_loader, text_chunk_processor, hugging_face_embedding_model_download
from dotenv import load_dotenv
import os
import time

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
print(PINECONE_API_KEY)

extracted_pdf = pdf_loader("Data/")
text_chunks = text_chunk_processor(extracted_pdf)
embeddings = hugging_face_embedding_model_download()

INDEX_NAME = "mediremedy"

# Initialize Pinecone Client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if Index Already Exists
if INDEX_NAME not in pc.list_indexes().names():
    print(f"Creating index '{INDEX_NAME}'...")

    # Create the Index
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,  # 🔹 Match this with your embeddings' vector size
        metric="cosine",  # 🔹 Can be 'cosine', 'dotproduct', or 'euclidean'
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    # ✅ Wait Until Index is Ready
    while pc.describe_index(INDEX_NAME).status['state'] != "Ready":
        time.sleep(1)

    print(f"Index '{INDEX_NAME}' is successfully created and ready!")

else:
    print(f"Index '{INDEX_NAME}' already exists.")

# Print All Existing Indexes
print("Available Indexes:", pc.list_indexes().names())

# ✅ Correct way to get the index instance
index = pc.Index(INDEX_NAME)

# Use LangChain’s Pinecone Vector Store
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

# ✅ Store documents in Pinecone
vector_store.add_documents(text_chunks)

print("Documents successfully stored in Pinecone!")