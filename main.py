import cv2

# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("test.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (1,1), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# OPTIONAL to filter out small/large dots using contour area filtering
# Adjust the area to only keep larger dots
'''
DOT_AREA = 10
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < DOT_AREA:
        cv2.drawContours(thresh, [c], -1, 0, -1)
'''

# Bitwise_and to extract dots
result = cv2.bitwise_and(image, image, mask=thresh)
result[thresh==0] = 255

cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
cv2.imshow("result", result)
cv2.waitKey()