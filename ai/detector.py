from ultralytics import YOLO
import config


class RuptureDetector:

    def __init__(self):

        print("Loading AI model...")

        self.model = YOLO(config.MODEL_PATH)

        print("Model loaded successfully.")

    def detect(self, frame):

        results = self.model.predict(
            source=frame,
            imgsz=config.IMAGE_SIZE,
            conf=config.CONFIDENCE_THRESHOLD,
            verbose=False
        )

        return results