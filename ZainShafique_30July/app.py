from flask import Flask, request, jsonify
import cohere
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Configure logging
logging.basicConfig(
    filename='api.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route('/summarize', methods=['POST'])
def summarize():
    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'route': request.path,
        'status': 'pending',
        'input_length': 0
    }

    try:
        data = request.json
        if not data or 'text' not in data:
            raise ValueError("Missing 'text' in request body")
            
        text = data['text']
        log_entry['input_length'] = len(text)
        
        if not text.strip():
            return jsonify({"summary": "", "warning": "Empty input"}), 200
        
        # Call Cohere API
        response = co.summarize(
            text=text,
            model='command',
            length='medium',
            extractiveness='medium',
        )
        
        summary = response.summary
        log_entry['status'] = 'success'
        return jsonify({"summary": summary}), 200
        
    except Exception as e:
        log_entry['status'] = f'error: {str(e)}'
        return jsonify({"error": str(e)}), 400
        
    finally:
        logging.info(log_entry)
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)