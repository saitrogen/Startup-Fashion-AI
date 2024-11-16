import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_color(image):
    # Convert image to RGB and resize for faster processing
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb = cv2.resize(image_rgb, (image_rgb.shape[1] // 5, image_rgb.shape[0] // 5))
    
    # Reshape the image into a 2D array of pixels
    pixels = image_rgb.reshape(-1, 3)
    
    # Use KMeans clustering to find the dominant color
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)
    
    # Get the dominant color (RGB)
    dominant_color = kmeans.cluster_centers_[0]
    
    return tuple(int(c) for c in dominant_color)
