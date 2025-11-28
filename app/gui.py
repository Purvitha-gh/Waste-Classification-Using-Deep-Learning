import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from predict import predict_waste  # Make sure predict.py is correct
import os

# Initialize main window
root = tk.Tk()
root.title("Waste Classification System")
root.geometry("500x600")
root.configure(bg="#F2F6F7")

# Title Label
title = tk.Label(root, text="Waste Classification System",
                 font=("Arial", 20, "bold"), bg="#F2F6F7", fg="green")
title.pack(pady=20)

# Image Display Label
img_label = tk.Label(root, bg="#F2F6F7")
img_label.pack(pady=10)

# Prediction Label
prediction_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                            bg="#F2F6F7", fg="black")
prediction_label.pack(pady=20)

uploaded_image_path = None

def upload_image():
    """Upload image and display it"""
    global uploaded_image_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        uploaded_image_path = file_path
        img = Image.open(file_path)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img
        prediction_label.config(text="")  # Clear old prediction

def predict_image():
    """Predict and display the result"""
    global uploaded_image_path
    if uploaded_image_path:
        result = predict_waste(uploaded_image_path)
        prediction_label.config(
            text=f"Prediction: {result}",
            fg="green" if "Organic" in result else "blue"
        )
    else:
        prediction_label.config(text="Please upload an image first!", fg="red")

# Buttons
upload_btn = tk.Button(root, text="Upload Waste Image", command=upload_image,
                       bg="green", fg="white", font=("Arial", 14, "bold"),
                       width=20, height=1)
upload_btn.pack(pady=10)

predict_btn = tk.Button(root, text="Predict", command=predict_image,
                        bg="orange", fg="white", font=("Arial", 14, "bold"),
                        width=15, height=1)
predict_btn.pack(pady=10)

root.mainloop()
