import os
import time
import requests
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Load OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize AI Model
llm = OpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

# Conversation prompt for AI
prompt = PromptTemplate.from_template("You are an AI agent. Continue this conversation: {query}")
conversation_chain = LLMChain(llm=llm, prompt=prompt)

# URL of Service B (Ensure it's correct)
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://127.0.0.1:5001/respond")  # ✅ Ensure "/respond" is included

def converse_with_service_b(initial_query):
    """ Manages the conversation between AI agents with a 5-second limit """
    conversation_history = [f"User: {initial_query}"]
    start_time = time.time()

    while time.time() - start_time < 5:  # Limit conversation to 5 seconds
        last_message = conversation_history[-1]

        try:
            # Send the last message to Service B
            response = requests.get(SERVICE_B_URL, params={"query": last_message}, timeout=3)

            if response.status_code == 200:
                service_b_reply = response.json().get("reply", "...")
            else:
                service_b_reply = f"Error: Service B returned status {response.status_code}"

        except requests.exceptions.RequestException as e:
            service_b_reply = f"Error: Could not connect to Service B ({str(e)})"

        conversation_history.append(f"AI B: {service_b_reply}")

        # Generate the next response from AI A
        service_a_reply = conversation_chain.run(service_b_reply)
        conversation_history.append(f"AI A: {service_a_reply}")

    return {"conversation": conversation_history}
