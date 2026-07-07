from ultralytics import YOLO
import torch


def main():

    print("=" * 60)
    print("PIPELINE DEFECT DETECTOR TRAINING")
    print("=" * 60)

    print("\nPyTorch Version :", torch.__version__)
    print("CUDA Available  :", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU :", torch.cuda.get_device_name(0))

    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset/config.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device=0,
        workers=0,      # <-- IMPORTANT: change from 4 to 0
        patience=20,
        cache=True,
        project="models",
        name="PipelineDefectDetector",
        pretrained=True,
        optimizer="auto",
        plots=True,
        save=True,
    )


if __name__ == "__main__":
    main()