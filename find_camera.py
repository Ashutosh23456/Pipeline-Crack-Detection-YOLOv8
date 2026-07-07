import cv2

for i in range(5):
    print(f"\nTesting Camera {i}")

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Better for Windows

    if not cap.isOpened():
        print("Not Available")
        continue

    ret, frame = cap.read()

    if ret:
        print("Working")
        cv2.imshow(f"Camera {i}", frame)
        cv2.waitKey(3000)
    else:
        print("Opened but no frame")

    cap.release()

cv2.destroyAllWindows()