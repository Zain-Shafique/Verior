from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keywords', methods=['POST'])
def extract_keywords():
    # Get JSON data from request
    data = request.get_json()
    
    # Validate required fields
    if not data or 'text' not in data:
        return jsonify({
            "status": "error",
            "message": "Missing 'text' field in request body",
            "data": None
        }), 400
    
    text = data['text'].strip()
    language = data.get('language', 'en').strip()  # Default to English
    
    # Validate text content
    if not text:
        return jsonify({
            "status": "error",
            "message": "Text cannot be empty",
            "data": None
        }), 400
    
    # Actual keyword extraction logic
    # REPLACE THIS WITH YOUR IMPLEMENTATION
    keywords = ["sample", "keywords"]
    
    return jsonify({
        "status": "success",
        "message": f"Extracted {len(keywords)} keywords from text",
        "data": {"keywords": keywords}
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Runs on http://localhost:5000
