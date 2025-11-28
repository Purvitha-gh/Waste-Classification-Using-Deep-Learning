import tensorflow as tf

model_path = "model/model_80%_binary.h5"

print(f"🔍 Checking: {model_path}\n")

try:
    model = tf.keras.models.load_model(model_path)
    print("✅ Model loaded successfully — it's a full model (architecture + weights).")
    model.summary()
except Exception as e:
    print("⚠️ Could not load model directly — probably weights only.")
    print(e)
