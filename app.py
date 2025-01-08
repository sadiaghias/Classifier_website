from flask import Flask, request, jsonify, render_template
from PIL import Image
import torch
import torchvision.transforms as transforms
import urllib.request
import os
from io import BytesIO

app = Flask(__name__)

# Load ImageNet labels
url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
imagenet_labels = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

# Function to download image from URL and predict
def load_and_predict(image_data):
    # Open the image from the downloaded data
    image = Image.open(BytesIO(image_data))

    # Preprocess the image (resize, convert to tensor, normalize)
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    image = preprocess(image).unsqueeze(0)

    # Load pre-trained model
    model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet50', pretrained=True)
    model.eval()

    # Run the model
    with torch.no_grad():
        outputs = model(image)

    # Get the predicted class index
    predicted_class_idx = torch.argmax(outputs, dim=1).item()

    # Get the class name from ImageNet labels
    class_name = imagenet_labels[predicted_class_idx]

    return class_name

# Route to handle file upload and prediction
@app.route('/upload-file', methods=['POST'])
def upload_image_file():
    if 'images' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['images']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to a temporary location
    image_path = os.path.join("uploads", file.filename)
    file.save(image_path)

    # Read the image and run prediction
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Run the prediction on the image file
    class_name = load_and_predict(image_data)

    # Clean up the saved file
    os.remove(image_path)

    return jsonify({"result": class_name})

# Route to handle image URL and prediction
@app.route('/upload-url', methods=['POST'])
def upload_image_url():
    image_url = request.form['image_url']

    try:
        # Download the image from the URL
        image_data = urllib.request.urlopen(image_url).read()

        # Run the prediction on the image URL
        class_name = load_and_predict(image_data)

        return jsonify({"result": class_name})

    except Exception as e:
        return jsonify({"error": f"Error processing the image URL: {str(e)}"}), 400

# Route for the home page (HTML form)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Make sure the uploads directory exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
