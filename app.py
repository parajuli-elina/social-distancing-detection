import streamlit as st
import cv2
import tempfile
import os
from detection.detector import YOLODetector
from detection.birdseye import BirdEyeTransformer
from detection.distance import calculate_social_distancing
from detection.utils import draw_social_distancing

st.title("Social Distancing Detection")
uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()

    if success:
        st.write("### Mark 4 points for ROI (Perspective Transform)")
        points = []

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
                points.append((x, y))

        temp_frame = frame.copy()
        cv2.namedWindow("Select ROI Points", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("Select ROI Points", click_event)

        while True:
            for pt in points:
                cv2.circle(temp_frame, pt, 5, (0, 255, 0), -1)
            cv2.imshow("Select ROI Points", temp_frame)
            if cv2.waitKey(1) & 0xFF == 27 or len(points) == 4:
                break

        cv2.destroyAllWindows()

        # Initialize Detector and Bird Eye View
        detector = YOLODetector()
        transformer = BirdEyeTransformer(points)

        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            persons = detector.detect(frame)
            centers = [((x1+x2)//2, (y1+y2)//2) for (x1, y1, x2, y2) in persons]

            bird_points = transformer.transform_points(centers)

            risky_pairs, statuses = calculate_social_distancing(bird_points)

            output_frame = draw_social_distancing(frame, persons, statuses, risky_pairs)

            stframe.image(output_frame, channels="BGR")

        cap.release()
        os.unlink(tfile.name)
