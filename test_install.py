from ultralytics import YOLO
import torch
import cv2

print("=" * 50)
print("Pipeline Inspection Robot")
print("=" * 50)

print("PyTorch Version:", torch.__version__)
print("OpenCV Version:", cv2.__version__)
print("CUDA Available:", torch.cuda.is_available())

model = YOLO("yolov8n.pt")

print("\nYOLOv8 Loaded Successfully!")