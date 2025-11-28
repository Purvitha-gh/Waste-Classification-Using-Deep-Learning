import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# ✅ Define the same CNN structure as your weight file
def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),

        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),

        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

# ✅ Build model and load weights
model = build_model()
model.load_weights("model/model_80%_binary.h5")

# ✅ Prediction function
def predict_waste(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x)[0][0]
    return "Recyclable Waste" if prediction > 0.5 else "Organic Waste"
