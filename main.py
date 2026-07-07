import cv2
import time
import os
from datetime import datetime

import config
from ai.detector import RuptureDetector

# -----------------------------------------
# Initialize
# -----------------------------------------

detector = RuptureDetector()

os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)

cap = cv2.VideoCapture(config.CAMERA_INDEX)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Camera Started")

prev_time = time.time()

# Prevent saving the same rupture repeatedly
image_saved = False

# -----------------------------------------
# Main Loop
# -----------------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # AI Detection
    # -----------------------------

    results = detector.detect(frame)

    annotated = results[0].plot()

    detected = False
    confidence = 0.0

    # -----------------------------
    # Check Detection
    # -----------------------------

    if len(results[0].boxes) > 0:

        detected = True

        confidence = float(results[0].boxes.conf[0])

        # Save image only once
        if (
            config.SAVE_DETECTIONS
            and confidence >= config.SAVE_CONFIDENCE
            and not image_saved
        ):

            filename = datetime.now().strftime(
                "rupture_%Y%m%d_%H%M%S.jpg"
            )

            path = os.path.join(
                config.OUTPUT_FOLDER,
                filename
            )

            cv2.imwrite(path, annotated)

            print(f"\nSaved : {path}")

            image_saved = True

    else:

        # Ready to save next rupture
        image_saved = False

    # -----------------------------
    # FPS
    # -----------------------------

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # -----------------------------
    # Dashboard
    # -----------------------------

    cv2.rectangle(
        annotated,
        (0, 0),
        (640, 120),
        (40, 40, 40),
        -1
    )

    cv2.putText(
        annotated,
        "PIPELINE INSPECTION ROBOT",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2,
    )

    if detected:

        status = "RUPTURE DETECTED"

        status_color = (0, 0, 255)

    else:

        status = "NORMAL"

        status_color = (0, 255, 0)

    cv2.putText(
        annotated,
        f"Status : {status}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        status_color,
        2,
    )

    cv2.putText(
        annotated,
        f"Confidence : {confidence:.2f}",
        (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        annotated,
        f"FPS : {fps:.1f}",
        (470, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 0),
        2,
    )

    cv2.imshow(config.WINDOW_NAME, annotated)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# -----------------------------------------
# Cleanup
# -----------------------------------------

cap.release()

cv2.destroyAllWindows()