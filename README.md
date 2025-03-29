# microservice-conversation

2 microservice containers have a conversation

AI Conversation System

Overview

This project runs two AI agents that communicate with each other for up to 5 seconds. The system consists of two services:

Service A: Initiates the conversation and calls Service B.

Service B: Responds to messages received from Service A.

Backend: Built using FastAPI and LangChain.

How to Run

1. Clone the Repository

git clone https://github.com/your-repo/ai-conversation.git
cd ai-conversation

2. Set Up a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in both service_a and service_b directories.

service_a/.env

OPENAI_API_KEY=your-openai-api-key
SERVICE_B_URL=http://127.0.0.1:5001/respond

service_b/.env

OPENAI_API_KEY=your-openai-api-key

Running the AI Services

Start Service B

cd service_b
python app.py

Runs at: http://127.0.0.1:5001

Start Service A

cd service_a
python app.py

Runs at: http://127.0.0.1:5000

Testing the Conversation

1. Test Service B Directly

curl "http://127.0.0.1:5001/respond?query=Hello"

Expected Response:

{"reply": "Hello! How can I assist you today?"}

2. Test AI-to-AI Conversation

curl "http://127.0.0.1:5000/converse?query=Hello"

Expected Response:

{
"conversation": [
"User: Hello",
"AI B: Hello! How can I assist you today?",
"AI A: I'm here to help! What would you like to discuss?",
"AI B: Let's talk about AI's impact on the world!",
"AI A: AI is transforming industries worldwide..."
]
}

Stopping the Services

To stop both services, press CTRL + C in each terminal.

If using a virtual environment, deactivate it:

deactivate

Next Steps

Build a UI to display conversations

Containerize services with Docker

Deploy on Kubernetes
