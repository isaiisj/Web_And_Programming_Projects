import cv2
import numpy as np

image = cv2.imread("images.jpg")
copia = image

#Cambiar a escala de grises
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#desenfocar la imagen
image = cv2.GaussianBlur(image,(5,5),0)

#detecatr bordes
image = cv2.Canny(image,0,300)

#Deteccion de contornos
(contornos,jerarquia) = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#DIbujando contronos
copia = cv2.drawContours(copia,contornos,-1,(255,0,0),2)

font = cv2.FONT_HERSHEY_SIMPLEX
moneda = 1
#Detectando el centro
for i in contornos:
    momento = cv2.moments(i)
    cx=int(momento['m10']/momento['m00'])
    cy=int(momento['m01']/momento['m00'])

    cv2.circle(copia,(cx,cy),3,(0,0,255),-1)
    cv2.putText(copia, str(moneda),(cx+10,cy+10),font,0.5,(0,0,0),2)
    moneda += 1
print(f"Hay {moneda-1} monedas")
cv2.imshow("resultado", copia)
cv2.waitKey(0)
