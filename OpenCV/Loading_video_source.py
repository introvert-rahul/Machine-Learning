
'''
import cv2
import numpy as np
import requests
import imutils 


url = 'http://192.168.9.71:8080/shot.jpg'


while True:
    img-res = requests.get(url)
    img-arr = np.array(bytearray(img-res.content), dtype = np.uint8)
    img = cv2.imdecode(img-arr, -1)
    img = imutils.resize(img, width = 1000, height = 1800)
    cv2.imshow("Android_cam", img)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
'''
import urllib
import cv2
import numpy as np
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://192.168.9.71:8080/shot.jpg'

while True:
    imgResp = urllib3.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('temp',cv2.resize(img,(600,400)))
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;

cv2.destroyAllWindows()