import cv2
import numpy as np
import os
import string
# Create the directory structure
if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data"):
    os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data")
if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/datadata/train"):
    os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/train")
if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test"):
    os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test")
for i in range(10):
    if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data/train/" + str(i)):
        os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/train/"+str(i))
    if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test/" + str(i)):
        os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test/"+str(i))

#for i in string.ascii_uppercase:
 #   if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data/train/" + i):
  #      os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/train/"+i)
   # if not os.path.exists("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test/" + i):
   #     os.makedirs("C:/Users/Abhishek/Sign-Language-to-Text-master/data/test/"+i)
    


# Train or test 
mode = 'train'
directory = 'C:/Users/Abhishek/Sign-Language-to-Text-master/data/'+mode+'/'
minValue = 70

cap = cv2.VideoCapture(0)
interrupt = -1  

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {
             'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'six': len(os.listdir(directory+"/6")),
             'seven':len(os.listdir(directory+"/7")),
             'eight':len(os.listdir(directory+"/8")),
             'nine':len(os.listdir(directory+"/9"))
             }
    
    # Printing the count in each set to the screen
    # cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "IMAGE COUNT", (10, ), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "SEVEN : "+str(count['seven']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "EIGHT : "+str(count['eight']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    cv2.putText(frame, "NINE : "+str(count['nine']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (220-1, 9), (620+1, 419), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[10:410, 220:520]
#    roi = cv2.resize(roi, (64, 64))
    
    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray,(5,5),2)
    # #blur = cv2.bilateralFilter(roi,9,75,75)
    
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #time.sleep(5)
    #cv2.imwrite("/home/rc/Downloads/soe/im1.jpg", roi)
    #test_image = func("/home/rc/Downloads/soe/im1.jpg")


    
    test_image = cv2.resize(test_image, (300,300))
    roi = test_image
    cv2.imshow("test", test_image)
        
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)       
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', roi)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', roi)
        
        
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
