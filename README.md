# Pipeline Crack Detection using YOLOv8

## Overview

This project is an AI-powered pipeline inspection system that detects cracks and ruptures on pipeline surfaces using the YOLOv8 object detection model. It is designed as part of a mechanical engineering final-year project combining computer vision, robotics, and machine learning.

The system can process images from a camera, identify damaged regions, and support automated pipeline inspection with minimal human intervention.

---

## Features

* Crack and rupture detection using YOLOv8
* Image inference for pipeline inspection
* Dataset preparation utilities
* Model training and retraining scripts
* Robot integration modules
* Camera interface for real-time inspection
* Modular Python project structure

---

## Project Structure

```text
PipelineInspectionRobot/
│
├── ai/
├── inference/
├── robot/
├── training/
├── utils/
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* YOLOv8
* OpenCV
* Ultralytics
* NumPy
* Robotics Integration

---

## Installation

Clone the repository:

```bash
git clone git@github.com:Ashutosh23456/Pipeline-Crack-Detection-YOLOv8.git
cd Pipeline-Crack-Detection-YOLOv8
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main application:

```bash
python main.py
```

For model training:

```bash
python training/train.py
```

For inference:

```bash
python robot/detect_image.py
```

---

## Dataset

The project uses a custom pipeline crack detection dataset prepared for YOLO format.

Large datasets and trained model weights are intentionally excluded from this repository to keep it lightweight. Replace the dataset paths with your own copies before training.

---

## Future Improvements

* Live video pipeline inspection
* Raspberry Pi deployment
* Edge AI optimization
* Automatic crack severity estimation
* Cloud-based monitoring dashboard
* Mobile application integration

---

## Author

**Ashutosh Shembade**

Mechanical Engineering Student
Aspiring Data Scientist | Machine Learning Enthusiast | Computer Vision Developer

---

## License

This project is intended for educational and research purposes.
