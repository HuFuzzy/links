import cv2
import sys
import numpy as np



boob = cv2.CascadeClassifier('xml_cascade/boobs')


img = cv2.imread('08719.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
boobs = boob.detectMultiScale(gray, 1.3, 5)

if (len(boobs)>0):
    print("asdasd")


for (x, y, w, h) in boobs:
   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
   roi_gray = gray[y:y + h, x:x + w]
   roi_color = img[y:y + h, x:x + w]
   font = cv2.FONT_HERSHEY_COMPLEX
   cv2.putText(img, "BOOB", (x, y), font, 0.5, (200, 255, 255), 2, cv2.LINE_AA)


cv2.imshow('Sasha Grey', img)
k = cv2.waitKey(0)

if k == 27:
    img.release()
    cv2.destroyAllWindows()
    img.release()
    cv2.destroyAllWindows()