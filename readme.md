# Social Distancing Detection 

This app detects people in a video and calculates social distancing between them in a bird's-eye view perspective. It uses YOLO for object detection and calculates the Euclidean distance between people to assess if they are maintaining proper social distancing.

### Features:
- Upload pre-recorded videos (mp4, avi, mov).
- Select Region of Interest (ROI) for perspective transformation.
- Detect people using YOLO and display bounding boxes.
- Calculate social distancing based on the bird’s-eye view transformation.
- Visualize social distancing in real-time with color-coded bounding boxes:
  - **Red**: High Risk (Too Close)
  - **Yellow**: Medium Risk (Threshold Distance)
  - **Green**: No Risk (Safe Distance)

### How it Works:
1. **Upload a video** via the Streamlit interface.
2. **Select ROI (Region of Interest)** by clicking on 4 points in the first frame to define the perspective transform.
3. **YOLO detection** is applied to each frame to identify people.
4. **Bird’s-eye view** transformation is applied using the ROI.
5. **Distance calculation** is performed in the bird's-eye view, and risky pairs are identified.
6. **Bounding boxes** are drawn in real-time, with color-coded labels indicating social distancing status.

---

## Requirements

The app uses several Python libraries and tools, which need to be installed in your virtual environment. Use the `requirements.txt` to install all dependencies:

```txt
streamlit
opencv-python
numpy
torch
ultralytics
