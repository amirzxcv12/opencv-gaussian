
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera frame")
        break


    gauss = cv2.GaussianBlur(frame, (9, 9), 0)


    cv2.imshow("Original Camera", frame)
    cv2.imshow("Gaussian Blur", gauss)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.imwrite("gaussian_image.jpg", gauss)
        print("image saved successfully!")
        break


cap.release()
cv2.destroyAllWindows()
