# Waste-Classification-Using-Deep-Learning

A Convolutional Neural Network (CNN)–based system to classify waste into Organic and Recyclable categories.
This project includes model training, evaluation, and a Tkinter GUI application for real-time waste image prediction.

📌 Project Overview

Waste management is one of the critical challenges in modern society. Proper segregation helps in recycling, composting, and reducing environmental pollution. This project uses a deep learning CNN model built using TensorFlow/Keras to automatically classify waste images.

A desktop application (built with Tkinter) allows users to upload an image and receive instant prediction results.

🚀 Features

✔️ Deep learning model using CNNs
✔️ Binary classification – Organic vs Recyclable
✔️ Image preprocessing (resizing, normalization, augmentation)
✔️ GUI application built with Python Tkinter
✔️ Real-time waste image prediction
✔️ Graphs for training vs validation accuracy & loss
✔️ Dataset organized into train/test folders
Model Architecture

The CNN model consists of:

3× Convolutional layers

MaxPooling layers

Flatten layer

Dense (fully connected) layers

Sigmoid output neuron for binary classification

The model was trained for 10 epochs with data augmentation.

📊 Model Performance
Training vs Validation Accuracy

Training Accuracy: ~99%

Validation Accuracy: ~90%

Training vs Validation Loss

Training Loss: Near 0

Validation Loss: Stable with slight fluctuations

Graphs Used

✔️ Accuracy curve

✔️ Loss curve

🧪 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the GUI
python app/gui.py

3️⃣ Train the Model (Optional)

If you want to retrain:

python train_model.py

📌 Dataset

The dataset contains two folders:

dataset/
├── Organic/
└── Recyclable/


Each folder contains images of waste items like:

Organic: fruits, vegetables, food waste

Recyclable: plastic bottles, cans, paper, metal, etc.

🖥️ GUI Preview

The GUI allows users to:

🟢 Upload an image
🟢 View the uploaded image
🟢 Click “Predict”
🟢 Get real-time classification result

The interface includes a background image, stylized buttons, and prediction display.

🛠️ Technologies Used

Python (3.x)

TensorFlow / Keras

Pillow (PIL)

Tkinter

NumPy

Matplotlib

💡 Future Enhancements

Some improvements planned:

Multi-class classification (Glass, Metal, Plastic, Organic, etc.)

Mobile app version (Kivy / Flutter + TensorFlow Lite)

Web dashboard for waste analytics

Better real-time classification

Integration with IoT-based smart dustbins
