import cv2
import numpy as np

# Step 1: Read the damaged image
damaged_img = cv2.imread("feather_damaged.png")

if damaged_img is None:
    raise FileNotFoundError("feather_damaged.png not found!")

# Step 2: Get height and width
height, width = damaged_img.shape[:2]

# Step 3: Create a black mask
mask = np.zeros((height, width), dtype=np.uint8)

# Find black pixels
black_pixels = np.all(damaged_img == [0, 0, 0], axis=2)

# Convert black pixels to white in the mask
mask[black_pixels] = 255

# Step 4: Save mask
cv2.imwrite("feather_mask.png", mask)

# Display
cv2.imshow("Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()