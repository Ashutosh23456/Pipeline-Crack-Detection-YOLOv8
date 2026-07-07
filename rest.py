from ultralytics import YOLO

model = YOLO("models/rupture_detector.pt")

results = model.predict(
    source="prototype_dataset/rupture/rupture_001.jpeg",
    conf=0.15,
    show=True,
    save=True
)