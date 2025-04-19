import asyncio
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        """
        Detect people in a given frame using YOLOv8.
        Only 'person' class (class 0 in COCO) is detected.
        
        Args:
            frame (np.array): The input image frame.

        Returns:
            List of bounding boxes [(x1, y1, x2, y2), ...]
        """

        try:
            # Check if an event loop is already running
            loop = asyncio.get_running_loop()
            if loop.is_running():
                # If Streamlit already has a running loop, use async version
                results = asyncio.run(self.model.predict_async(
                    source=frame,
                    imgsz=640,
                    conf=0.5,
                    classes=[0],  # Only detect 'person'
                    verbose=False
                ))
            else:
                # Otherwise, normal sync prediction
                results = self.model.predict(
                    source=frame,
                    imgsz=640,
                    conf=0.5,
                    classes=[0],
                    verbose=False
                )
        except RuntimeError:
            # If no running event loop
            results = self.model.predict(
                source=frame,
                imgsz=640,
                conf=0.5,
                classes=[0],
                verbose=False
            )

        boxes = []
        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box[:4])
                boxes.append((x1, y1, x2, y2))
        return boxes
