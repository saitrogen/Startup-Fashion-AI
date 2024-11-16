import streamlit as st
import cv2
import numpy as np
from PIL import Image
from color_extraction import extract_dominant_color
from body_type import detect_body_type
from recommendations import get_recommendations

# Streamlit user interface for inputs
st.title("Fashion AI - Image Upload & Recommendations")

# User Input
st.header("Please fill in the following details:")

occasion = st.selectbox("Choose the occasion:", ["Casual", "Formal", "Party", "Work", "Date"])
color_preference = st.color_picker("Pick your favorite color for clothes", "#000000")

# Upload Image
uploaded_file = st.file_uploader("Upload an image of yourself", type=["jpg", "png"])

if uploaded_file is not None:
    # Convert the uploaded image to a format OpenCV can work with
    pil_image = Image.open(uploaded_file)
    image = np.array(pil_image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Save the image for further processing
    image_path = "static/input_images/user_image.jpg"
    cv2.imwrite(image_path, image)

    # 1. Color Extraction
    dominant_color = extract_dominant_color(image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # 2. Body Type Detection
    try:
        body_type = detect_body_type(image_path)
        st.write(f"Detected Body Type: {body_type}")
    except Exception as e:
        st.write(f"Error detecting body type: {str(e)}")

    # 3. Get Recommendations
    recommendations = get_recommendations(occasion, color_preference, body_type, dominant_color)
    st.write(f"Recommended Clothes for You: {recommendations}")

else:
    st.write("Please upload an image of yourself to proceed.")
