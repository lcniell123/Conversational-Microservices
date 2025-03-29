from fastapi import FastAPI
from agent import converse_with_service_b

app = FastAPI()

@app.get("/converse")
def start_conversation(query: str):
    return converse_with_service_b(query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
