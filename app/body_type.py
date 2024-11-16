import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

def detect_body_type(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        return "Unknown"  # Fallback if image cannot be read
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize Mediapipe Pose model
    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return "Unknown"

    # Use landmarks to infer body type
    landmarks = results.pose_landmarks.landmark
    shoulder_width = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x - landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x
    hip_width = landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x - landmarks[mp_pose.PoseLandmark.LEFT_HIP].x

    if shoulder_width > hip_width:
        return "Inverted Triangle"
    elif shoulder_width < hip_width:
        return "Pear"
    else:
        return "Rectangle"
