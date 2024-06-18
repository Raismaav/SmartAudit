import cv2
import pytesseract

image = cv2.imread('test_image.png')
cv2.imshow('Image', image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(image)
print(text)

