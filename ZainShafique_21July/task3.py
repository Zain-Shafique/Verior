# task3.py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

nltk.download('punkt')

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(
    request: TextRequest,
    num_sentences: int = Query(2, gt=0, description="Number of sentences in summary")
):
    text = request.text.strip()
    
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    
    # Try Sumy for longer texts
    sentences = nltk.sent_tokenize(text)
    if len(sentences) > 2:
        try:
            parser = PlaintextParser.from_string(text, Tokenizer("english"))
            summarizer = LexRankSummarizer()
            summary_sentences = summarizer(parser.document, num_sentences)
            return {"summary": " ".join(str(s) for s in summary_sentences)}
        except Exception as e:
            print(f"Sumy error: {e}")
    
    # Fallback for short texts
    return {"summary": " ".join(sentences[:min(num_sentences, len(sentences))])}

@app.get("/")
def root():
    return {
        "message": "Sumy-based summarization API",
        "instructions": "POST JSON with 'text' field to /summarize",
        "parameters": {
            "num_sentences": "Optional number of sentences (default=2)"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Install dependencies:
# pip install fastapi uvicorn nltk sumy

# Start server:
# python -m uvicorn task3:app --reload

# Standard request
# curl -X POST "http://localhost:8000/summarize?num_sentences=3" \
# -H "Content-Type: application/json" \
# -d '{"text": "Natural language processing enables computers to understand human language. It involves tasks like translation, sentiment analysis, and summarization. Modern NLP uses deep learning models. These models require large datasets for training. Applications include chatbots and virtual assistants."}'

# Custom length
# curl -X POST "http://localhost:8000/summarize?num_sentences=1" \
# -H "Content-Type: application/json" \
# -d '{"text": "Short text. Only two sentences."}'

# Short text
# curl -X POST "http://localhost:8000/summarize" \
# -H "Content-Type: application/json" \
# -d '{"text": "Single sentence input."}'