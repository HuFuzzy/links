

import cv2
import requests
from bs4 import BeautifulSoup

from requests import get






face_cascade = cv2.CascadeClassifier('xml_cascade/faces_default')
eye_cascade = cv2.CascadeClassifier('xml_cascade/eye')
fullbody_cascade  = cv2.CascadeClassifier('xml_cascade/fullbody')

for i in range(0, 9):
    siteImg = "hb8o" + str(i)




    for i in range(4,9):
        site = "https://prnt.sc/"
        img = str(siteImg) + str(i)
        site = site + str(img)

        page = requests.get(str(site))
        soup = BeautifulSoup(page.content,'html.parser')
        imagem = str(soup.find_all(id="screenshot-image"))
        imagem = imagem.split()[6]
        imagem = imagem[5:63]
        print(imagem)

        with open("test"+str(i)+ '.png', 'wb') as arquivo:
            response = get(imagem)
            arquivo.write(response.content)

        printImg = cv2.imread("test"+ str(i) + '.png')
        gray = cv2.cvtColor(printImg, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        body = fullbody_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(printImg, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = printImg[y:y + h, x:x + w]
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(printImg, "Rosto", (x, y), font, 0.5, (200, 255, 255), 2, cv2.LINE_AA)





            cv2.imshow('Sasha Grey', printImg)
            k = cv2.waitKey(0)

            if k == 27:
                img.release()
                cv2.destroyAllWindows()
                img.release()
                cv2.destroyAllWindows()
        img = str(siteImg)
        site = "http://prnt.sc/"



