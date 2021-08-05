import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[] #times at which object went from 0-1 or 1-0
df=pandas.DataFrame(columns=["Start","End"])#dataframe for times that items were moved

video=cv2.VideoCapture(0) #0 means video stays open

while True:
    check, frame = video.read() #current frame that is read from video camera
    status=0 #no motion in current frame 0 = no motion
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #live frame but in gray scale
    gray=cv2.GaussianBlur(gray,(21,21),0) #blurry gray scale version  #making gray image blurry

    if first_frame is None: #only first iteration
        first_frame=gray
        continue #to beginning of the loop

    #gray and gray color difference from blurred frame
    delta_frame=cv2.absdiff(first_frame,gray) #comparing the gray and the first_gray #this returns another image
    
    #black and white frame (how to show if there is objects in a frame) if have threshold limit of 30 assign 255
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #how to detect objects (white moving)
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)#how to remove black holes from white area(smoothen)

    #to find contours (list of contours)
    #example if you have two white images but distinct from each other youll get two contours
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#dont modify current threshold frame

    #only keep contours that have area bigger than 1000 pixels (adjust 1000 by size of what you want to measure)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1 #when you find a contour of pixels > 10000
        #rectangle only drawn if contour > 1000
        #Rectangles around the objects 
        (x, y, w, h)=cv2.boundingRect(contour) #assigning variables
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3) #drawing rectangle drawing to frame
    status_list.append(status) #add it to the status_list of the whole thing

    status_list=status_list[-2:]

    #checking the last two elements to see if they are changing
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #how to show the frames
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    #how to quit
    if key==ord('q'):
        if status==1:
            times.append(datetime.now()) #if status is 1 when you press key add it to the times list
        break

print(status_list)
print(times)

#displaying the times list
#throw into csv file
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True) #like a dictionary (key: value)

#converting the dataframe to a csv file
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
