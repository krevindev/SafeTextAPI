# app.py
from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import os

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'bin', 'tesseract')

# The rest of your Flask app code


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
