from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('pdfs')

    if not files:
        return jsonify({'error': 'No files provided'}), 400

    filenames = []
    for file in files:
        if file and file.content_type == 'application/pdf':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
        else:
            return jsonify({'error': f'Invalid file format for {file.filename}'}), 400

    return jsonify({'message': f'Files {", ".join(filenames)} uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
