import cv2

# Read the original image
img = cv2.imread("feather.jpg")

if img is None:
    raise FileNotFoundError("feather.jpg not found!")

# Create a black damaged region
# Format: image[y1:y2, x1:x2]
img[450:550, 300:400] = [0, 0, 0]

# Save damaged image
cv2.imwrite("feather_damaged.png", img)

# Display
cv2.imshow("Damaged Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()