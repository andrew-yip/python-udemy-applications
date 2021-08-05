import cv2

img = cv2.imread("/Users/andrewyip/Desktop/galaxy.jpg",1,)
print(type(img)) #type is numpy array
print(img.shape) #HOW MANY PIXELS HORIZONTAL AND VERTICAL
print('HELLO MY NAME IS JOE', img.ndim) #DIMENSIONS
print(img) #prints the numpy array


resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))#resize
cv2.imshow("Galaxy", resized_img) #to show

cv2.imwrite("Galaxy_resized.jpg", resized_img)

cv2.waitKey(0) #0 so it stays forever
cv2.destroyAllWindows() #destroys