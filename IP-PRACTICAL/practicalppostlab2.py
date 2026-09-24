# import cv2

# # Read image directly in grayscale mode
# img = cv2.imread('time.jfif', cv2.IMREAD_GRAYSCALE)

 

# # Check if the image was loaded properly
# if img is None:
#     print("Error: Image not found or unable to load.")
# else:
#     # Show the grayscale image
#     cv2.imshow('Grayscale Image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#code2
# import cv2

# # Read the image
# image = cv2.imread('space.jpg')

# # Check if image is loaded properly
# if image is None:
#     print("Error: Image not found or unable to load.")
# else:
#     # Split the image into B, G, R channels
#     B, G, R = cv2.split(image)

#     # Show the original image and wait for a key press
#     cv2.imshow("CS24106 Original", image)
#     cv2.waitKey(0)

#     # Show blue channel
#     cv2.imshow("Blue", B)
#     cv2.waitKey(0)

#     # Show green channel
#     cv2.imshow("Green", G)
#     cv2.waitKey(0)

#     # Show red channel
#     cv2.imshow("Red", R)
#     cv2.waitKey(0)

#     cv2.destroyAllWindows()


#code3
# # Python program to read image
# # as YCrCb color space
# # Import cv2 module
# import cv2
# # Reads the image
# img = cv2.imread('shapes.jfif')
# # Convert to YCrCb color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# # Shows the image
# cv2.imshow('CS24106 image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code4
# # Python program to read image
# # as HSV color space

# # Importing cv2 module
# import cv2

# # Reads the image
# img = cv2.imread('shapes.jfif')

# # Converts to HSV color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # Shows the image
# cv2.imshow('CS24106 image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #code5
import cv2
# Read the image
image = cv2.imread('shapes.jfif')
# Check if image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load.")
    exit()
# Convert the image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# Display the LAB image
cv2.imshow('CS24106 LAB Image', lab_image)
# Wait for a key press and close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
