from fastapi import FastAPI
from agent import generate_response
import logging

app = FastAPI()

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

@app.get("/")  # Root endpoint
def home():
    return {"message": "Service B Running"}

@app.get("/respond")  # ✅ Ensure this is correctly defined!
def respond_to_query(query: str):
    logging.info(f"Received query from Service A: {query}")  # Debugging log
    response = generate_response(query)
    logging.info(f"Service B response: {response}")  # Debugging log
    return response  # Ensure response is returned properly

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001)
