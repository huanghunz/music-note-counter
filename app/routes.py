from flask import render_template, request, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # 示例返回数据
    result = {
        'C': 10,
        'D': 8,
        'E': 12,
        'F': 6,
        'G': 15,
        'A': 9,
        'B': 7
    }

    return jsonify(result)