from flask import Flask, render_template, request, jsonify
from src.helper import hugging_face_embedding_model_download
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

embeddings = hugging_face_embedding_model_download()

INDEX_NAME = "mediremedy"

# Ensure vector_store is correctly initialized
vector_store = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

# Ensure retriever is correctly set
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 7})

llm = GoogleGenerativeAI(model="gemini-2.0-flash-thinking-exp-01-21", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
])

document_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, document_chain)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["POST"])
def get_bot_response():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"response": "Please provide a valid input."})

        print(f"User Input: {user_message}")
        print("Retriever Type:", type(retriever))
        print("Vector Store Type:", type(vector_store))

        response = rag_chain.invoke({"input": user_message})
        print("Full Response:", response)

        bot_reply = response.get("answer", "I'm not sure how to respond.")

        return jsonify({"response": bot_reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"response": "An error occurred. Please try again."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)