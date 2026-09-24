# import cv2
# img = cv2.imread("shapes.jfif")
# t_lower = 50  
# t_upper = 150 
# edge = cv2.Canny(img, t_lower, t_upper)
# cv2.imshow('CS24106 original', img)
# cv2.imshow('CS24106 edge', edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #code2
# import cv2
# img = cv2.imread("shapes.jfif") 
# t_lower = 100  
# t_upper = 200  
# aperture_size = 5 
# edge = cv2.Canny(img, t_lower, t_upper, 
#                  apertureSize=aperture_size)
# cv2.imshow('CS24106 original', img)
# cv2.imshow('edge', edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code3
# import cv2
# img = cv2.imread("shapes.jfif") 
# t_lower = 100
# t_upper = 200 
# aperture_size = 5
# L2Gradient = True 
# edge = cv2.Canny(img, t_lower, t_upper, L2gradient = L2Gradient )
# cv2.imshow('CS24106 original', img)
# cv2.imshow('CS24106edge', edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #code4
# import cv2 
# img = cv2.imread("shapes.jfif") 
# t_lower = 100
# t_upper = 200 
# aperture_size = 5 
# L2Gradient = True
# edge = cv2.Canny(img, t_lower, t_upper,
#                  apertureSize = aperture_size, 
#                  L2gradient = L2Gradient ) 
# cv2.imshow('CS24106 original', img)
# cv2.imshow('CS24106 edge', edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #code5
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# # --- Load grayscale image ---
# img = cv2.imread('shapes.jfif', cv2.IMREAD_GRAYSCALE)

# if img is None:
#     raise ValueError("Image not found. Please check the path and filename.")

# # --- Sobel Edge Detection ---
# # Sobel in X and Y directions
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# # Compute magnitude
# sobel_edges = cv2.magnitude(sobelx, sobely)
# sobel_edges = np.uint8(sobel_edges)

# # --- Display Results ---
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('CS24106 Original Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(sobel_edges, cmap='gray')
# plt.title('CS24106Sobel Edges')
# plt.axis('off')

# plt.tight_layout()
# plt.show()

# # --- Save Result (optional) ---
# cv2.imwrite('sobel_edges.jpg', sobel_edges)

#code6
import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- Load grayscale image ---
img = cv2.imread('gill.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Please check the path and filename.")

# --- Prewitt Edge Detection ---
# Prewitt kernels
kernelx = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]], dtype=np.float32)
kernely = np.array([[-1, -1, -1],
                    [0,  0,  0],
                    [1,  1,  1]], dtype=np.float32)

prewittx = cv2.filter2D(img, cv2.CV_64F, kernelx)
prewitty = cv2.filter2D(img, cv2.CV_64F, kernely)

# Compute magnitude
prewitt_edges = cv2.magnitude(prewittx, prewitty)
prewitt_edges = np.uint8(prewitt_edges)

# --- Display Results ---
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('CS24086 Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(prewitt_edges, cmap='gray')
plt.title('CS24086 Prewitt Edges')
plt.axis('off')

plt.tight_layout()
plt.show()

# --- Save Result (optional) ---
cv2.imwrite('prewitt_edges.jpg', prewitt_edges)
