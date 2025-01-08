# Image Prediction Flask App

This project is a simple Flask-based web application that allows users to upload an image from their machine or provide an image URL to get predictions using a pre-trained **ResNet-50** model.

The application uses the **PyTorch** library for image processing and prediction, and it loads ImageNet labels to display the predicted class name.

## Features

- **Image Upload**: Users can upload an image file from their system for prediction.
- **Image URL**: Users can also provide an image URL for prediction.
- **Model**: The app uses a pre-trained **ResNet-50** model from **PyTorch**'s hub to classify the image into one of the ImageNet classes.

## Requirements

To run this project locally, you need the following libraries:

- Flask
- PyTorch
- Pillow
- torchvision

You can install these dependencies using `pip`:

```bash
pip install flask torch torchvision pillow

/image-prediction-flask-app
    /uploads                 # Directory to temporarily store uploaded images
    /templates
        index.html           # HTML form for uploading images or providing URLs
    app.py                   # Main Python script that runs the Flask app
    requirements.txt         # File containing all dependencies for the project
    README.md                # Project documentation (this file)


### Explanation:

- **Basic Information**: The README starts with an overview of the project, its key features, and the libraries required.
- **Installation Instructions**: It includes instructions on how to clone the repository, install dependencies, and run the app.
- **Usage**: Describes the functionality of the web app and how users can interact with it.
- **Project Structure**: Lists the file and folder structure to help new developers understand the organization of the project.
- **Sample Prediction**: Provides an example of what the user will see after uploading the image or providing an image URL.

This README should give anyone who comes across the project a good understanding of its purpose and how to run it locally.
