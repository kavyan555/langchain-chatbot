Project Title

AI Chatbot using LangChain and Groq
________________________________________
Description

This project is a web-based AI chatbot application that allows users to interact with a Large Language Model in real time. It uses LangChain to structure prompts and manage the interaction pipeline, while Groq’s LLaMA 3.3 model provides fast and accurate responses.
The application is built with Streamlit and supports multiple chat sessions within a single interface.
________________________________________
Features

•	Real-time chatbot interaction

•	Multi-session chat support

•	Prompt-based response generation using LangChain

•	Clean and interactive UI built with Streamlit

•	Secure API key management
________________________________________
Tech Stack

•	Python

•	Streamlit

•	LangChain

•	Groq API
________________________________________
Project Structure

LANGCHAIN_CHATBOT/

│── app.py

│── requirements.txt

│── .env

│── .gitignore

│── venv/
________________________________________
Prerequisites

•	Python 3.8 or above

•	Groq API Key
________________________________________
Installation

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Configure environment variables

Create a .env file in the root directory and add:

GROQ_API_KEY=your_api_key_here
________________________________________
Running the Application

streamlit run app.py

Open the browser and navigate to:

http://localhost:8501
________________________________________
Usage

•	Enter a message in the input box

•	The chatbot generates a response using the LLM

•	Start a new chat using the sidebar button

•	Switch between previous chats from the sidebar
