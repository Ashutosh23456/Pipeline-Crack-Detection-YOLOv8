from pathlib import Path
from collections import defaultdict
import random
import shutil
import re

# ==========================================================
# DATASET PREPARATION CONFIGURATION
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_IMAGES = PROJECT_ROOT / "dataset" / "images" / "train"
SOURCE_LABELS = PROJECT_ROOT / "dataset" / "labels" / "train"

DESTINATION = PROJECT_ROOT / "dataset" / "prepared"

TRAIN_RATIO = 0.70
VAL_RATIO = 0.20
TEST_RATIO = 0.10

RANDOM_SEED = 42

random.seed(RANDOM_SEED)

# ==========================================================
# GROUP AUGMENTED IMAGES
# ==========================================================

def get_group_name(image_path):
    """
    Example:

    005590.jpg
    005590_0.jpg
    005590_1.jpg

    ---> 005590
    """
    return re.sub(r'_\d+$', '', image_path.stem)


groups = defaultdict(list)

for image in SOURCE_IMAGES.glob("*.jpg"):
    groups[get_group_name(image)].append(image)

print("=" * 60)
print("DATASET PREPARATION")
print("=" * 60)

print(f"\nTotal Groups : {len(groups)}")
print(f"Total Images : {sum(len(v) for v in groups.values())}")
# ==========================================================
# SPLIT GROUPS
# ==========================================================

group_keys = list(groups.keys())
random.shuffle(group_keys)

total_groups = len(group_keys)

train_end = int(total_groups * TRAIN_RATIO)
val_end = train_end + int(total_groups * VAL_RATIO)

train_groups = group_keys[:train_end]
val_groups = group_keys[train_end:val_end]
test_groups = group_keys[val_end:]

print("\nDataset Split")
print("-" * 30)
print(f"Train Groups : {len(train_groups)}")
print(f"Validation   : {len(val_groups)}")
print(f"Test         : {len(test_groups)}")

# ==========================================================
# CREATE OUTPUT FOLDERS
# ==========================================================

for split in ["train", "val", "test"]:

    (DESTINATION / "images" / split).mkdir(parents=True, exist_ok=True)
    (DESTINATION / "labels" / split).mkdir(parents=True, exist_ok=True)

print("\nOutput folders created successfully.")
# ==========================================================
# COPY DATASET
# ==========================================================

def copy_split(group_list, split_name):

    image_count = 0

    print(f"\nCopying {split_name} dataset...")

    for group in group_list:

        for image in groups[group]:

            label = SOURCE_LABELS / f"{image.stem}.txt"

            destination_image = DESTINATION / "images" / split_name / image.name
            destination_label = DESTINATION / "labels" / split_name / label.name

            shutil.copy2(image, destination_image)

            if label.exists():
                shutil.copy2(label, destination_label)

            image_count += 1

    print(f"{split_name.capitalize()} Images Copied : {image_count}")
    # ==========================================================
# START COPYING
# ==========================================================

copy_split(train_groups, "train")
copy_split(val_groups, "val")
copy_split(test_groups, "test")

print("\n" + "=" * 60)
print("DATASET PREPARATION COMPLETED SUCCESSFULLY!")
print("=" * 60)