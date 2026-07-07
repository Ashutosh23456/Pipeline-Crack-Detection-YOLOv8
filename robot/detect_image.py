from ultralytics import YOLO
from pathlib import Path

# Load trained model
model = YOLO("runs/detect/models/PipelineDefectDetector-3/weights/best.pt")

INPUT_FOLDER = "inference/images"

print("=" * 60)
print("PIPELINE RUPTURE DETECTION")
print("=" * 60)

results = model.predict(
    source=INPUT_FOLDER,
    conf=0.25,
    imgsz=640,
    save=True,
    project="inference",
    name="outputs",
    exist_ok=True
)

print("\nDetection Complete!")
print("Results saved to:")
print(Path("inference/outputs"))