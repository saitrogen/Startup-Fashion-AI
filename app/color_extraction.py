from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

def extract_dominant_color(image_path):
    # Open the image
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Reduce size for faster processing
    image_np = np.array(image)

    # Reshape image data to (number of pixels, 3)
    pixels = image_np.reshape(-1, 3)

    # KMeans clustering to find dominant color
    kmeans = KMeans(n_clusters=1, random_state=0).fit(pixels)
    dominant_color = kmeans.cluster_centers_[0]

    # Convert to integer RGB values
    return tuple(map(int, dominant_color))
