from flask import Flask, render_template, request
from utils.helpers import reverse_string
from utils.text_tools import analyze_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Task 1: Display reversed string
    reversed_str = reverse_string("Hello World")
    
    # Task 2: Text analysis
    analysis = None
    error = None
    
    if request.method == 'POST':
        text = request.form['text'].strip()
        if not text:
            error = "Please enter some text!"
        else:
            analysis = analyze_text(text)
    
    return render_template(
        'index.html',
        reversed_str=reversed_str,
        analysis=analysis,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)