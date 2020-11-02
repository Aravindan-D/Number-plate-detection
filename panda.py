import re
import pandas as pd
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'I:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('1.jpg',cv2.IMREAD_COLOR)
img = imutils.resize(img, width=500 )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
#cv2.imshow("img1",img1)...................................................................
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
screenCnt = None #will store the number plate contour
img2 = img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3) 
#cv2.imshow("img2",img2) #top 30 contours...........................................................................

count=0
idx=7
# loop over contours
for c in cnts:
  # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4: #chooses contours with 4 corners
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c) #finds co-ordinates of the plate
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite('./'+str(idx)+'.png',new_img) #stores the new image
                idx+=1
                break
            #draws the selected contour on original image        
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
#cv2.imshow("Final image with plate detected",img).........................................................

Cropped_loc='./7.png' #the filename of cropped image
cv2.imshow("cropped",cv2.imread(Cropped_loc))
pytesseract.pytesseract.tesseract_cmd=r"I:\Program Files\Tesseract-OCR\tesseract.exe" #exe file for using ocr 
text=pytesseract.image_to_string(Cropped_loc,lang='eng') #converts image characters to string
#print("NUMBER PLATE:" ,text)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#text='CG04MF2250'
n=[text]
alpha=r'[a-z A-Z]+'
number=r'[0-9]+'
for i in n:
    x=[]
    a=re.findall(alpha,i)
    b=re.findall(number,i)
    for j in range(len(a)):
        x.append(a[j].strip())
        x.append(b[j].strip())
   # print(''.join(x))
f=''.join(x)
print("NUMBER PLATE IS:",f)


#SEARCHING IN DATASET

import pandas as pd
col=['License-plate-no', 'Owner name','phone number:', 'Vehicle model:', 'License-issued-date:','FIR:']
database=pd.DataFrame(columns=col)
database['License-plate-no']=['HR26DA2330', 'CG04MF2250', 'HR26DK8337', 'TN31AP1243', 'TN01AV0001', 'KL01AQ1424', 'PY01AA0090' , 'TN01BC1010', 'TN081BE3389', 'TN87CA8790', 'KL45BC5542', 'TN91PA2341', 'HR01CD542', 'TN5AL8768', 'UP14BN4001']
database['Owner name']=['vijay kummar', 'Rnajith','Anu', 'Archana','Salmon', 'Vinai','Samson', 'Gokul', 'Vinayak', 'Dhana', 'Sekhar', 'Raj', 'Gaajapathii', 'Vimal', 'shanmugam']
database['phone number:']=['8134896473', '7612376521', '9123349879', '9841376897', '8532253819', '6382291009', '8182638101', '8898897898', '6789067543', '6876789765', '9867132561', '6273819263' ,'9762912839', '6789896504', '6787654329']
database['Vehicle model:']=['Maruthi Suzuki -shift dzire', 'Audi-Q8', 'Hyundai-ksg', 'Indica-LGI', 'Altoz', 'Indica-DLe', 'Mahindra-xuv500', 'Mahindra-scorpio', 'ford-echosport', 'Reynold-duster', 'Skoda-rapid', 'Skoda-superb', 'Skoda-activia', 'Volkswagen-polo', 'Ford-aspire',]
database['License-issued-date:']=['01-10-2002', '06-12-2001', '05-11-2009', '21-12-1990', '18-01-2020', '10-06-2006', '04-02-2019', '15-12-1998', '09-07-2005', '11-10-2004', '03-11-1989', '23-06-2002', '21-7-2003', '11-01-2005', '22-11-2008']
database['FIR:']=['NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'YES', 'NO', 'YES', 'NO' ,'YES']    
index=pd.Index([f])
k=index.get_loc(f)
lst=database.loc[k,:]
print(lst)
