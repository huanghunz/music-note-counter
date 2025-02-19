from flask import render_template, request, jsonify
from app import app
import cv2
import numpy as np
from PIL import Image
import pytesseract
import music21

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

    # 读取图像文件
    image = Image.open(file)
    # 转换为OpenCV格式
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # TODO: 实现音符识别逻辑
    # 这里需要添加音符识别的具体实现

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