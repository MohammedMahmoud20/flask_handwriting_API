from tensorflow.python.keras.models import load_model

model_path = 'model/autism_binary_handwritin_modelv.h5'

try:
    model = load_model(model_path)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
