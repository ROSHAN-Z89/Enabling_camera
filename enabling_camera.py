import cv2
video_cap = cv2.VideoCapture(0)
while True :
    ret ,vid = video_cap.read()
    cv2.imshow("video_live",vid)
    if cv2.waitKey(10) == ord('a'):
        break
video_cap.release()
