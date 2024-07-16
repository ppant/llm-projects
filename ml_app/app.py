from flask import Flask, request, jsonify
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from PIL import Image
import numpy as np

app = Flask(__name__)
model = MobileNetV2(weights='imagenet')

def prepare_image(image_path):
    img = Image.open(image_path).resize(224,224)
    img_array = np.extend_dims(np.array(img),axis=0)
    return preprocess_input(img_array)

@app.route('/predict', methods=['POST'])

def predict():
    data = {'success': False}

    if request.files.get('image'):
        image = prepare_image(request.files(['image']))
        preds = model.predict(image)
        results = decode_predictions(preds)
        data['predictions'] = [f"{label}: {round(prob*100, 2)}%" for (_, label, prob) in results[0]]
        data['success'] = True
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='192.168.1.54')



