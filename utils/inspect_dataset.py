from pathlib import Path
from collections import Counter

# ==========================================================
# Pipeline Inspection Dataset Inspector
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

IMAGE_DIR = PROJECT_ROOT / "dataset" / "images" / "train"
LABEL_DIR = PROJECT_ROOT / "dataset" / "labels" / "train"

print("=" * 60)
print("      PIPELINE DEFECT DATASET INSPECTOR")
print("=" * 60)

# ----------------------------------------------------------
# Load images and labels
# ----------------------------------------------------------

images = sorted(IMAGE_DIR.glob("*.jpg"))
labels = sorted(LABEL_DIR.glob("*.txt"))

print(f"\nTotal Images : {len(images)}")
print(f"Total Labels : {len(labels)}")

# ----------------------------------------------------------
# Check Missing Labels
# ----------------------------------------------------------

missing_labels = []

for img in images:
    label = LABEL_DIR / (img.stem + ".txt")

    if not label.exists():
        missing_labels.append(img.name)

print(f"\nImages without Labels : {len(missing_labels)}")

if missing_labels:
    print("\nExample Missing Labels:")

    for file in missing_labels[:10]:
        print(file)

# ----------------------------------------------------------
# Count Classes
# ----------------------------------------------------------

class_counter = Counter()

for label_file in labels:

    with open(label_file, "r") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            class_id = int(line.split()[0])

            class_counter[class_id] += 1

# ----------------------------------------------------------
# Class Names
# ----------------------------------------------------------

CLASS_NAMES = {
    0: "Deformation",
    1: "Obstacle",
    2: "Rupture",
    3: "Disconnect",
    4: "Misalignment",
    5: "Deposition"
}

print("\n" + "=" * 60)
print("Class Distribution")
print("=" * 60)

total_objects = 0

for class_id in sorted(CLASS_NAMES.keys()):

    count = class_counter[class_id]
    total_objects += count

    print(f"{CLASS_NAMES[class_id]:15s} : {count}")

print("\nTotal Objects :", total_objects)

print("\nDataset Inspection Complete!")