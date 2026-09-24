# import cv2
# import numpy as np

# # Read the input image
# img = cv2.imread("tree.jpeg")

# # Check if image was loaded successfully
# if img is None:
#     print("Error: Image not found or path is incorrect.")
#     exit()

# # Apply averaging (blur) filter
# im1 = cv2.blur(img, (5, 5))

# # Apply box filter (with normalization)
# im2 = cv2.boxFilter(img, -1, (2, 2), normalize=True)

# # Display both filtered images side by side
# combined = np.hstack((im1, im2))
# cv2.imshow("CS24106 Blurred (5x5) vs Box Filter (2x2)", combined)

# # Wait for key press and close window
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# code2
# import cv2
# import numpy as np

# # Read the input image
# img = cv2.imread("tree.jpeg")

# # Check if the image was loaded successfully
# if img is None:
#     print("Error: Image not found or path is incorrect.")
#     exit()

# # Apply Gaussian Blur
# dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

# # Display original and blurred images side by side
# cv2.imshow("CS24106 Original vs Gaussian Blur", np.hstack((img, dst)))

# # Wait for a key press and close all windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code3
# import cv2
# import numpy as np

# # Read the input image
# img = cv2.imread("blurred.jpeg")

# # Check if the image was loaded successfully
# if img is None:
#     print("Error: Image not found or path is incorrect.")
#     exit()

# # Apply Median Blur
# dst = cv2.medianBlur(img, 5)

# # Display original and blurred images side by side
# cv2.imshow("CS24106 Original vs Median Blur", np.hstack((img, dst)))

# # Wait for a key press and close all windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code4
import cv2
import numpy as np

# Load the image
img = cv2.imread("gill.jpeg")

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Apply Bilateral Filter
# d = 15, sigmaColor = 100, sigmaSpace = 100
dst = cv2.bilateralFilter(img, 15, 100, 100)

# Display original and filtered image side by side
cv2.imshow("CS24086 Original vs Bilateral Filter", np.hstack((img, dst)))

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()