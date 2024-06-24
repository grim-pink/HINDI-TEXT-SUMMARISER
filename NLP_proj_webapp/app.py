from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from summarizer import summary_text
from ocr_code import ocr
from ner import entities_found
import os
import traceback
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/process-input', methods=['POST'])
def process_input():
    try:
        summary_length = request.form['summary_length']  # Corrected to get 'summary_length' key from form

        # Initialize text variable
        text = ""

        # Checking if a valid file is uploaded
        file = request.files.get('file', None)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            text = ocr(file_path)  # Assuming ocr function returns text
        elif 'textarea' in request.form:
            text = request.form['textarea']

        # print(text)

        # Process the summary based on the summary length chosen
        if summary_length == 'short':
            summary = summary_text(text, summary_length='short')
        elif summary_length == 'long':
            summary = summary_text(text, summary_length='long')
        else:
            summary = 'Invalid summary length specified'

        entity = entities_found(text)

        summary_ = summary[0]['summary_text']

        # print(summary_)
        # print(entity)
        if len(entity) == 0:
            entity = None

        return render_template('page1.html', summary= summary_, entities=entity, requested=True)

    except Exception as e:
        traceback.print_exc()
        return render_template('page1.html', error='An error occurred while processing the input.')


if __name__ == '__main__':
    app.run(debug=True)
