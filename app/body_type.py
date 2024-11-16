import cv2
import mediapipe as mp

def detect_body_type(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Image at path {image_path} could not be loaded. Check the file path.")
    
    # Use MediaPipe to detect body landmarks (pose detection)
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    
    if results.pose_landmarks:
        # Process body type (simple logic here, can be improved based on body landmarks)
        return "Athletic"  # Example, update logic as required.
    else:
        return "Unknown"
