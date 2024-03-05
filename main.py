import cv2

capture = cv2.VideoCapture(0)

while True :
    ret, img = capture.read()

    cv2.imshow("from camera", img)

    k = cv2.waitKey(30) & 0XFF
    if k == 27:
        break

capture.release()
cv2.destroyWindow()
