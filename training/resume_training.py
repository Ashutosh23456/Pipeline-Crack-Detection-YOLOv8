from ultralytics import YOLO


def main():

    model = YOLO(
        "runs/detect/models/PipelineDefectDetector-3/weights/last.pt"
    )

    model.train(resume=True)


if __name__ == "__main__":
    main()