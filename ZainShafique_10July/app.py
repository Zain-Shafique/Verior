from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/word_count', methods=['POST'])
def word_count():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input: JSON must contain "text" field'}), 400
    text = data['text']
    words = text.split()
    count = len(words)
    return jsonify({'word_count': count})

@app.route('/character_frequency', methods=['POST'])
def character_frequency():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input: JSON must contain "text" field'}), 400
    text = data['text']
    text_no_spaces = text.replace(" ", "")
    freq = {}
    for char in text_no_spaces:
        freq[char] = freq.get(char, 0) + 1
    return jsonify({'frequencies': freq})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
