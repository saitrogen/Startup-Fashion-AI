import streamlit as st
from color_extraction import extract_dominant_color
from body_type import detect_body_type
from recommendations import get_recommendations
import os

# Folder to store uploaded images
UPLOAD_FOLDER = "app/static/input_images"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Streamlit UI
st.title("Fashion AI - Personalized Outfit Recommendations")

# Occasion selection
occasion = st.selectbox(
    "Choose an occasion:",
    ["Casual", "Formal", "Party", "Wedding", "Sports"]
)

# File upload
uploaded_file = st.file_uploader("Upload an image of yourself:", type=["jpg", "png"])

if uploaded_file:
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    # Step 1: Extract dominant color
    dominant_color = extract_dominant_color(file_path)
    st.write(f"Dominant color detected: {dominant_color}")

    # Step 2: Detect body type
    body_type = detect_body_type(file_path)
    st.write(f"Detected body type: {body_type}")

    # Step 3: Generate recommendations
    recommendations = get_recommendations(occasion, dominant_color, body_type)
    st.write("Recommendations for you:")
    for recommendation in recommendations:
        st.write(f"- {recommendation}")

else:
    st.write("Please upload an image to get started!")
