# app.py
import streamlit as st
from PIL import Image
import torch
from torchvision.models import mobilenet_v2
from utils import load_model, get_transform, predict

# Load class names
with open("classes.txt", "r") as f:
    class_names = [line.strip() for line in f]

st.title("🌍 Disaster Image Classifier")
st.markdown("Upload a disaster image to predict the category: **Flood**, **Fire**, or **Earthquake**.")

# Load model
model = load_model("student_model.pth", mobilenet_v2, num_classes=len(class_names))

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Classify"):
        transform = get_transform()
        label = predict(image, model, transform, class_names)
        st.success(f"🔥 Predicted Disaster Type: **{label.upper()}**")
