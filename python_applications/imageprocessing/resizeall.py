import cv2
import glob

#idk how to work this with mac
images=glob.glob("/Users/andrewyip/Desktop/udemy_python/intro_stuff/imageprocessing/resizepractice/*.jpg")


for image in images:
    img=cv2.imread(image,0) #image read in grey scale
    re=cv2.resize(img,(100,100)) #resizing the image
    cv2.imshow("Hey",re) #renaming random name and re is the name we named the variable
    cv2.waitKey(500) #wait
    cv2.destroyAllWindows() #destroys all
    cv2.imwrite("resized_"+image,re) 