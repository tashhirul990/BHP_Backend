from flask import Flask, request, jsonify
import os
import utils

app = Flask(__name__)




@app.route("/")
def index():
    return "Welcome to the Home Price Prediction API!"

@app.route("/get_locations")
def get_locations():
    response = jsonify({
        'locations': utils.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods=['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']
    response = jsonify({
        'estimated_price': utils.get_estimated_price(location, sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utils.load_artifacts()
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
