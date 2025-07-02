from flask import Flask, jsonify, request, render_template
from model import predict
from image import import_image

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_route():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    image = import_image(image_file)
    age, gender, ethnicity = predict(image)

    return jsonify({
        "Age": age,
        "Gender": gender,
        "Ethnicity": ethnicity
    })

if __name__ == "__main__":
    app.run(debug=True)
