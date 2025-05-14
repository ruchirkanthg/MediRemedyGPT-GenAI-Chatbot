# MediRemedy Chatbot - Generative AI

The End-to-End Medical Chatbot Generative AI Project involved building a sophisticated conversational agent capable of delivering medical information and guidance using a combination of cutting-edge technologies. At its core, the chatbot utilized Google Gemini LLM (Large Language Model), integrated through Langchain, to enable advanced natural language understanding and generation capabilities. The project implemented a Retrieval-Augmented Generation (RAG) architecture, combining generative AI with a retrieval system to provide accurate, contextually relevant answers. Pinecone.ai served as the vector database, facilitating fast and precise retrieval of relevant medical documents through semantic search. The front-end was built using HTML and CSS, offering a clean, intuitive user interface, while the back-end was developed using Flask, which acted as a bridge between the user interface, LLM, and database. The Flask server also handled API requests, user authentication, and session management, ensuring a smooth and secure user experience.

The deployment pipeline utilized Docker for containerization, enabling consistent application performance across different environments. The project leveraged AWS EC2 instances for hosting the chatbot, providing scalability and reliability. The AWS IAM (Identity and Access Management) service was used to securely manage access to AWS resources, ensuring security best practices. The Docker images were stored and managed in AWS ECR (Elastic Container Registry), facilitating seamless integration with CI/CD pipelines managed through GitHub Actions. The CI/CD pipeline automated processes including testing, building, pushing Docker images to ECR, and deploying the application on EC2, promoting a continuous deployment strategy. Langchain’s framework was instrumental in managing prompt chaining, maintaining contextual conversations, and supporting complex dialogue flows. The RAG approach combined with Pinecone’s vector search ensured that responses were not only generated but also rooted in reliable medical sources. The holistic use of cloud services, automation tools, and AI technologies led to the development of a robust, scalable, and secure medical chatbot capable of enhancing patient engagement and supporting healthcare professionals.


Here’s a comprehensive README file for the MediRemedyGPT-GenAI-Chatbot project, providing clear, step-by-step instructions to set up and use the application.

⸻

MediRemedyGPT-GenAI-Chatbot

Summary 
MediRemedyGPT is an end-to-end medical chatbot powered by generative AI. It leverages Google Gemini LLM integrated via Langchain and employs a Retrieval-Augmented Generation (RAG) architecture to deliver accurate and context-aware medical information. This project is designed to assist users in obtaining reliable medical guidance through natural language conversations.

Features
	•	Conversational AI: Engage in natural language dialogues to receive medical information.
	•	Google Gemini LLM Integration: Utilizes advanced language models for understanding and generating responses.
	•	Langchain Framework: Manages the flow of conversations and integrates various components seamlessly.
	•	Retrieval-Augmented Generation (RAG): Combines generative AI with a retrieval system to enhance response accuracy.
	•	Web Interface: User-friendly interface built with Flask for easy interaction.

Prerequisites

Before setting up the application, ensure you have the following installed:
	•	Python 3.8 or higher: Download Python
	•	Git: Download Git
	•	Docker (optional, for containerized deployment): Install Docker

Installation

Follow these steps to set up the MediRemedyGPT-GenAI-Chatbot:

1. Clone the Repository

Open your terminal or command prompt and run:

git clone https://github.com/ruchirkanthg/MediRemedyGPT-GenAI-Chatbot.git
cd MediRemedyGPT-GenAI-Chatbot

2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to manage dependencies:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies

Install the required Python packages using pip:

pip install -r requirements.txt

4. Configure Environment Variables

I used the Pinecone vector database to store my knowledge base which is present in the data folder of this repo. Please set up your own Pinecone account and paste the API keys into their respective variables. 

Also, create your Google Gemini API key to access the respective Gemini model that has been used in this project. 

Create a .env file in the root directory to store your environment variables. At a minimum, you should define your API keys and any other necessary configurations.

5. Run the Application

Start the Flask application:

python app.py

By default, the application will be accessible at http://127.0.0.1:8080/.

Usage

Once the application is running:
	1.	Open your web browser and navigate to http://127.0.0.1:8080.
	2.	You will see the MediRemedyGPT chatbot interface.
	3.	Type your medical-related questions into the chat input box.
	4.	The chatbot will respond with information generated using the integrated AI models.

Project Structure

The repository is organized as follows:

MediRemedyGPT-GenAI-Chatbot/
├── .github/             # GitHub workflows and configurations
├── Data/                # Dataset files used for training or retrieval
├── code/                # Additional code modules
├── src/                 # Source code for the application
├── templates/           # HTML templates for the Flask web interface
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration for containerization
├── README.md            # Project documentation
└── .env                 # Environment variables (not included in the repository)

Docker Deployment (Optional)
Refer to the Dockerfile to containerize the application. 


⸻

For more information and updates, visit the GitHub repository.

⸻

