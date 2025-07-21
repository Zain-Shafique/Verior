# task2.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk

nltk.download('punkt')

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    text = request.text.strip()
    
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    
    sentences = nltk.sent_tokenize(text)
    summary = " ".join(sentences[:min(2, len(sentences))])
    
    return {"summary": summary}

@app.get("/")
def root():
    return {
        "message": "Rule-based summarization API",
        "instructions": "POST JSON with 'text' field to /summarize"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Install dependencies:
# pip install fastapi uvicorn nltk

# Start server:
# python -m uvicorn task2:app --reload

# 2.1 Multi-sentence text
# curl -X POST "http://localhost:8000/summarize" \
# -H "Content-Type: application/json" \
# -d '{"text": "First sentence. Second sentence. Third sentence."}'

# 2.2 Short text
# curl -X POST "http://localhost:8000/summarize" \
# -H "Content-Type: application/json" \
# -d '{"text": "Only one sentence"}'

# 2.3 Empty input
# curl -X POST "http://localhost:8000/summarize" \
# -H "Content-Type: application/json" \
# -d '{"text": ""}'
