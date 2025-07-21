# task1.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": "Summary coming soon"}

@app.get("/")
def root():
    return {
        "message": "Send POST requests to /summarize endpoint",
        "example": {
            "method": "POST",
            "url": "/summarize",
            "body": {"text": "Your paragraph here"}
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)# task1.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": "Summary coming soon"}

@app.get("/")
def root():
    return {
        "message": "Send POST requests to /summarize endpoint",
        "example": {
            "method": "POST",
            "url": "/summarize",
            "body": {"text": "Your paragraph here"}
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Install dependencies:
# pip install fastapi uvicorn pydantic

# Start server:
# python -m uvicorn task1:app --reload