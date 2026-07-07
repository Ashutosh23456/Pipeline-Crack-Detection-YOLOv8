from ultralytics import YOLO
import torch


def main():

    print("=" * 60)
    print("PIPELINE RUPTURE DETECTOR TRAINING")
    print("=" * 60)

    print("PyTorch :", torch.__version__)
    print("CUDA :", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU :", torch.cuda.get_device_name(0))

    # Load your previously trained model
    model = YOLO("yolov8n.pt")
    

    model.train(
    data="prototype_yolo/data.yaml",
    epochs=50,
    imgsz=640,
    batch=2,
    device=0,
    workers=0,
    patience=10,
    cache=True,
    project="prototype_models",
    name="RuptureDetector",
    pretrained=True,
    optimizer="AdamW",
    lr0=0.0005,
    plots=True,
    save=True,
)


if __name__ == "__main__":
    main()