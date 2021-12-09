import numpy as np
import cv2
import math

hand_cascade = cv2.CascadeClassifier('Hand_haar_cascade.xml')

#Video cap
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    blur = cv2.GaussianBlur(img, (5,5), 0)
    
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    retval2, thresh1 = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    hand = hand_cascade.detectMultiScale(thresh1, 1.3, 5)
    mask = np.zeros(thresh1.shape, dtype = "uint8")

    for (x, y, w, h) in hand:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
        cv2.rectangle(mask, (x,y), (x+w, y+h), 255, -1)

    img2 = cv2.bitwise_and(thresh1, mask)
    final = cv2.GaussianBlur(img2, (7,7), 0)
    contours, hierarchy = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(img, contours, 0, (255,255,0), 3)
    cv2.drawContours(final, contours, 0, (255,255,0), 3)

    if len(contours) > 0:
        cnt = contours[0]
        hull = cv2.convexHull(cnt, returnPoints = False)
        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0

        #apply cosine rules to find angle for all effect
        if defects!= None:
            for i in range(defects.shape[0]):
                p,q,r,s = defects[i,0]
                figure1 = tuple(cnt[p][0])
                figure2 = tuple(cnt[q][0])
                dip = tuple(cnt[r][0])

                #find length of all side of triangle
                a = math.sqrt((figure2[0] - figure1[0])**2 +(figure2[1] - figure1[1])**2)
                b = math.sqrt((dip[0] - figure1[0])**2 + (dip[1] - figure1[1])**2)
                c = math.sqrt((figure2[0] - dip[0])**2 + (figure2[1] - dip[1])**2)

                #apply cosine rules
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c))*57.29
                if angle <= 90:
                    count_defects += 1

        if count_defects == 1:
            cv2.putText(img, "This is 1", (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            cv2.putText(img, "This is 2", (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 3:
            cv2.putText(img, "This is 3", (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 4:
            cv2.putText(img, "This is 4", (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 5:
            cv2.putText(img, "This is 5", (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, 2)

    cv2.imshow('img',thresh1)
    cv2.imshow('img1',img)
    cv2.imshow('img2',img2)
    
    if cv2.waitKey(30) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
