import cv2
import numpy as np

# Read the damaged image
img = cv2.imread("feather_damaged.png")

if img is None:
    raise FileNotFoundError("feather_damaged.png not found!")

# Get image dimensions
height, width = img.shape[:2]

# Create a completely black mask
mask = np.zeros((height, width), dtype=np.uint8)

# ------------------------------------------------
# Mark the damaged area as WHITE
# ------------------------------------------------
# Change these coordinates according to your damage
mask[450:550, 300:400] = 255

# Save the predefined mask
cv2.imwrite("feather_mask.png", mask)

# Display the mask
cv2.imshow("Predefined Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()