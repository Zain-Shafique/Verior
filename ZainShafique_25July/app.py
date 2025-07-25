from flask import Flask, request, jsonify
from translate import Translator
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS

# Configure logging
logging.basicConfig(level=logging.INFO)

def make_response(status, message, data):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), status

# Supported languages (ISO 639-1 codes)
SUPPORTED_LANGUAGES = {
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 
    'zh', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 
    'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 
    'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 
    'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 
    'ne', 'no', 'ny', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 
    'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 
    'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 
    'xh', 'yi', 'yo', 'zu'
}

@app.route('/translate', methods=['POST'])
def translate_endpoint():
    app.logger.info("Received translation request")
    
    # Validate input format
    if not request.is_json:
        return make_response(400, "Request must be JSON", None)
    
    request_data = request.get_json()
    
    # Validate required fields
    if 'text' not in request_data:
        return make_response(400, "Missing 'text' field", None)
    
    text = request_data['text']
    target_language = request_data.get('target_language', 'en').lower()
    
    # Validate text content
    if not isinstance(text, str) or not text.strip():
        return make_response(400, "Text must be a non-empty string", None)
    
    # Validate language code
    if not isinstance(target_language, str) or target_language not in SUPPORTED_LANGUAGES:
        return make_response(400, f"Invalid language code. Supported codes: {sorted(SUPPORTED_LANGUAGES)}", None)
    
    # Perform translation
    try:
        app.logger.info(f"Translating text: '{text}' to {target_language}")
        
        # Create translator (auto-detects source language)
        translator = Translator(to_lang=target_language)
        
        # Translate text
        translated_text = translator.translate(text)
        
        # Create response
        result = {
            "original_text": text,
            "translated_text": translated_text,
            "target_language": target_language
        }
        
        app.logger.info("Translation successful")
        return make_response(200, "Translation successful", result)
    
    except Exception as e:
        app.logger.error(f"Translation failed: {str(e)}")
        return make_response(500, f"Translation failed: {str(e)}", None)

if __name__ == '__main__':
    app.run(debug=True)


# Install dependencies
# pip install flask-cors translate


# Run the application
# python app.py
