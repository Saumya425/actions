from flask import Flask, request, jsonify  
import joblib  
import numpy as np  
  
app = Flask(__name__)  
  
# Load the trained model  
model = joblib.load('model.pkl')  
  
@app.route('/predict', methods=['POST'])  
def predict():  
    data = request.get_json()  
    features = data['features']  
    predictions = []  
    for feature in features:  
        feature_arr = np.array(feature).reshape(1, -1)  
        prediction = model.predict(feature_arr)  
        predictions.append(prediction.tolist())  
    return jsonify({'predictions': predictions})  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  
