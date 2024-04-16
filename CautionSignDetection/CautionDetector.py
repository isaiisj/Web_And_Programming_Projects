import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract'

image = cv2.imread('images.png')

b,g,r = cv2.split(image)
#cv2.imshow('Blue',r)
#cv2.waitKey(0)

g = cv2.blur(g,(3,3))
#cv2.imshow('Blurred',g)
#cv2.waitKey(0)
canny = cv2.Canny(r,150,200)
canny = cv2.dilate(canny,None,iterations=1)

text = pytesseract.image_to_string(canny).strip()
print('texto:',text)

if text == 'CAUTION':
    print("Right Sign")
else:
    print("It´s wrong")


cv2.imshow('Image', image)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()