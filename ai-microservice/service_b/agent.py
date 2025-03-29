import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

# Load OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize AI Model
llm = OpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

# Define the prompt for AI B's response
prompt = PromptTemplate.from_template("You are an AI agent replying to another AI. Continue this conversation: {query}")
response_chain = LLMChain(llm=llm, prompt=prompt)

def generate_response(query):
    """ Generates AI response and handles empty responses """
    try:
        response = response_chain.run(query).strip()
        if not response:  # Check if response is empty
            response = "I'm not sure how to respond to that. Can you clarify?"
        return {"reply": response}
    except Exception as e:
        return {"reply": f"Error generating response: {str(e)}"}  # Handle AI errors
