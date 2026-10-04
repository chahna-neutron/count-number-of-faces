# Count Number of Faces

## Overview

Count Number of Faces is a real-time face detection project built using Python and OpenCV. It uses the pre-trained YuNet deep learning model to detect faces through a webcam and count the number of faces present in the frame.

## Features

- Real-time face detection using a webcam
- Detects multiple faces
- Draws a bounding box around each detected face
- Numbers each detected face
- Displays the total number of detected faces
- Simple and easy to use

## Technologies Used

- Python
- OpenCV
- YuNet
- ONNX

## How It Works

1. The webcam captures a live video frame.
2. The YuNet model processes the frame.
3. The model detects faces in the frame.
4. The Python program counts the detected faces.
5. Bounding boxes and face numbers are displayed on the screen.

## Project Structure

```text
Count Number of Faces/
├── face_counter.py
├── face_detection_yunet_2023mar.onnx
├── requirements.txt
└── README.md

Installation
1. Create a virtual environment
  python3.10 -m venv venv

2. Activate the virtual environment
  source venv/bin/activate  

3. Install the required packages
  pip install -r requirements.txt

Running the Project
  Run the following command:
  python face_counter.py
The webcam will open and start detecting faces in real time.
Each detected face will be displayed with a bounding box and face number. The total number of detected faces will also be displayed.
Press q to exit the application.

Model
This project uses the pre-trained YuNet face detection model.
Model file:
face_detection_yunet_2023mar.onnx

YuNet is used to detect faces in the webcam frames. The Python program then counts the detected faces and displays the results.
Project Type
This is a computer vision and deep learning based face detection project using a pre-trained model. 

Applications
- Real-time face detection
- People counting
- Basic computer vision applications
- Webcam-based face analysis
- Smart camera systems


## Conclusion

Count Number of Faces demonstrates how a pre-trained deep learning model can be integrated with OpenCV to perform real-time face detection and face counting using a webcam.