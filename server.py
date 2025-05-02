
from flask import Flask, request, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        print("🟢 Bir istek geldi!")
        if 'image' not in request.files:
            return jsonify({'error': 'No image part in the request'}), 400

        image_file = request.files['image']
        img = Image.open(image_file.stream)

        # Örnek bir işlem: sadece boyutları al
        width, height = img.size
        return jsonify({
            'message': 'Image received successfully',
            'width': width,
            'height': height
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

