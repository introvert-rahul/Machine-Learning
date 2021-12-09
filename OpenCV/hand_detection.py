import cv2

hand_cascade = cv2.CascadeClassifier('Hand_haar_cascade.xml')
#hand_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in hand:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'hand', (50,50), font, 0.5, (0,0,0), 1, cv2.LINE_AA)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()