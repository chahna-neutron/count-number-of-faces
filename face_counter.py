import cv2

# Load YuNet face detector
face_detector = cv2.FaceDetectorYN.create(
    "face_detection_yunet_2023mar.onnx",
    "",
    (320, 320),
    0.8,
    0.3,
    5000
)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access the camera.")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Get frame size
    height, width = frame.shape[:2]

    # Tell YuNet the current image size
    face_detector.setInputSize((width, height))

    # Detect faces
    _, faces = face_detector.detect(frame)

    # Count faces
    face_count = 0 if faces is None else len(faces)

    # Draw boxes and face numbers
    if faces is not None:
        for i, face in enumerate(faces, start=1):

            x, y, w, h = face[:4].astype(int)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Face {i}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Display total number of faces
    cv2.putText(
        frame,
        f"Total Faces: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show camera
    cv2.imshow("Count Number of Faces", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()