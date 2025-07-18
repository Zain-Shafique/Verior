from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    """Analyze text sentiment and return polarity + category"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Categorize sentiment based on polarity
    if polarity > 0.5:
        sentiment = "Strongly Positive"
    elif polarity > 0:
        sentiment = "Positive"
    elif polarity == 0:
        sentiment = "Neutral"
    elif polarity >= -0.5:  # Note: -0.5 <= polarity < 0
        sentiment = "Negative"
    else:
        sentiment = "Strongly Negative"
    
    return polarity, sentiment

@app.route('/')
def home():
    """Simple root route to avoid 404 errors"""
    return jsonify({
        "message": "Welcome to Sentiment Analysis API",
        "endpoint": "POST /analyze",
        "parameters": {"texts": "Array of strings to analyze"}
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint for analyzing multiple text inputs"""
    data = request.get_json()
    
    # Validate request format
    if not data or 'texts' not in data:
        return jsonify({"error": "Missing 'texts' field in request body"}), 400
    
    if not isinstance(data['texts'], list):
        return jsonify({"error": "'texts' must be an array"}), 400
    
    results = []
    for text in data['texts']:
        # Validate individual input
        if not isinstance(text, str):
            results.append({
                "input": text,
                "error": "Invalid input. Please enter a valid string."
            })
            continue
            
        if len(text.strip()) == 0:
            results.append({
                "input": text,
                "error": "Invalid input. Please enter a non-empty string."
            })
            continue
        
        # Process valid input
        polarity, sentiment = analyze_sentiment(text)
        results.append({
            "input": text,
            "polarity": polarity,
            "sentiment": sentiment
        })
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)