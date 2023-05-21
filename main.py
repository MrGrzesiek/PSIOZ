
import cv2
import argparse

# --image : Source image
# --mask : Binary mask indicating pixels to be inpainted
# --method : Inpainting algorithm to be used Telea/NS
# --radius : Radius of neighborhood pixels to be considered for interpolation purpose

a = argparse.ArgumentParser()
a.add_argument("-i", "--image", type=str, required=False, default="a.jpg", help="path of image to be used")
a.add_argument("-m", "--mask", type=str, required=False, default="maska.png", help="path of masked image")
a.add_argument("-a", "--method", type=str, default="telea", choices=["telea", "ns"], help="inpainting algorithm")
a.add_argument("-r", "--radius", type=int, default=3, help="inpainting radius")
args = vars(a.parse_args())

paint_method = cv2.INPAINT_TELEA

if args["method"] == "ns":
    paint_method = cv2.INPAINT_NS

image = cv2.imread(args["image"])
mask = cv2.imread(args["mask"])
# convert to gray scale - one channel image
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
# calling the inpaint function 
output = cv2.inpaint(image, mask, args["radius"], flags=paint_method)

cv2.imshow('Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Output', output)
cv2.imwrite('output.jpg', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
#view rawimage_inpainting.py# hosted with ❤ by GitHub