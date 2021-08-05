import cv2, time

video = cv2.VideoCapture(0)

a = 1

while True:
    a= a+1
    check, frame = video.read()
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #time.sleep(3)
    cv2.imshow("Capturing", gray) #shows the frame

    key = cv2.waitKey(1) #shows for however long (shows first frame of video) #waits 1millisec

    if key == ord('q'): #if you press q key it breaks
        break

print('number of frames: ', a)
video.release()
cv2.destroyAllWindows()
