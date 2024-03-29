# I am importing a library 

import cv2 

# I am creating the dimensions for the image  
  
width = 800 
height = 400 

# I am reading the image then resizing it and then converting it to gray 

image = cv2.imread("Fiat.jpg") 
image = cv2.resize(image,(width,height)) 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# I am loading the number plate detector 

n_plate_detector = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml") 

# I am detecting the number plates in the Gray image 

detections = n_plate_detector.detectMultiScale(gray,scaleFactor = 1.05,minNeighbors= 7 ) 

# I am creating the loop and the boxes 

for (x,y,w,h) in detections: 

# I am drawing the rectangle around the number plate 

	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
	cv2.putText(image,"Number Plate detected",(x-20,y-10),
				cv2.FONT_HERSHEY_COMPLEX,0.5,(139,28,98),2) 
	
# I am extracting the number plate from the gray image 

	number_plate = gray[y:y+h,x:x+w] 

# I am showing the image 

cv2.imshow("Number plate", number_plate) 
cv2.imshow("Number plate detection",image)

# I am clearing the image    

cv2.waitKey(0) 
  







  

  