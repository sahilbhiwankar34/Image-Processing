# import numpy as np
# import cv2 as cv

# img = cv.imread("cone.jpg", 0)

# rows, cols = img.shape

# M = np.float32([[1, 0, 100], [0, 1, 50]])

# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow("Sahil Bhiwankar(CS24106)", dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


# code2
# import numpy as np
# import cv2 as cv

# # Read the image in grayscale
# img = cv.imread("cone.jpg", 0)

# # Check if the image is loaded
# if img is None:
#     print("Error: Image not found. Make sure 'cone.jpg' is in the same folder as this Python file.")
#     exit()

# # Get image dimensions
# rows, cols = img.shape

# # Reflection matrix (vertical flip)
# M = np.float32([
#     [1, 0, 0],
#     [0, -1, rows],
#     [0, 0, 1]
# ])

# # Apply reflection
# reflected_img = cv.warpPerspective(img, M, (cols, rows))

# # Display the reflected image
# cv.imshow("Reflected Image", reflected_img)

# # Save the reflected image
# cv.imwrite("reflection_out.jpg", reflected_img)

# # Wait for a key press and close the window
# cv.waitKey(0)
# cv.destroyAllWindows()


# code3
# import numpy as np
# import cv2 as cv

# # Read image
# img = cv.imread("shapes.jfif", 0)

# # Check if image exists
# if img is None:
#     print("Error: girlImage.jpg not found.")
#     exit()

# # Get image dimensions
# rows, cols = img.shape

# # Rotate the image by 30 degrees with scale 0.6
# rotation_matrix = cv.getRotationMatrix2D((cols/2, rows/2), 30, 0.6)
# img_rotation = cv.warpAffine(img, rotation_matrix, (cols, rows))

# # Display image
# cv.imshow("Sahil Bhiwankar(CS24106)", img_rotation)

# # Save image
# cv.imwrite("rotation_out.jpg", img_rotation)

# cv.waitKey(0)
# cv.destroyAllWindows()

# code4
# import cv2 as cv
# import numpy as np

# # Read image in grayscale
# img = cv.imread("cone.jpg", 0)

# # Check if image is loaded
# if img is None:
#     print("Error: girlImage.jpg not found.")
#     exit()

# # Shrink the image
# img_shrinked = cv.resize(
#     img,
#     (250, 200),
#     interpolation=cv.INTER_AREA
# )

# # Display shrunk image
# cv.imshow("Sahil Bhiwankar(CS24106) Shrunk Image", img_shrinked)

# # Enlarge the shrunk image
# img_enlarged = cv.resize(
#     img_shrinked,
#     None,
#     fx=1.5,
#     fy=1.5,
#     interpolation=cv.INTER_CUBIC
# )

# # Display enlarged image
# cv.imshow("Sahil Bhiwankar(CS24106)Enlarged Image", img_enlarged)

# cv.waitKey(0)
# cv.destroyAllWindows()

# code5
# import cv2 as cv
# import numpy as np

# # Read image in grayscale
# img = cv.imread("cone.jpg", 0)
# # Or use: img = cv.imread("cone.jpg", 0)

# # Check if image is loaded
# if img is None:
#     print("Error: Image not found.")
#     exit()

# # Crop the image
# cropped_img = img[100:300, 100:300]

# # Display the cropped image
# cv.imshow("Cropped Image", cropped_img)

# # Save the cropped image
# cv.imwrite("cropped_out.jpg", cropped_img)

# # Wait for a key press and close windows
# cv.waitKey(0)
# cv.destroyAllWindows()

# code 6
# import numpy as np
# import cv2 as cv

# # Read the image in grayscale
# img = cv.imread("cone.jpg", 0)

# # Check if the image is loaded
# if img is None:
#     print("Error: girlImage.jpg not found.")
#     exit()

# # Get image dimensions
# rows, cols = img.shape

# # Shearing transformation matrix
# M = np.float32([
#     [1, 0.5, 0],
#     [0, 1, 0],
#     [0, 0, 1]
# ])

# # Apply shearing transformation
# sheared_img = cv.warpPerspective(
#     img,
#     M,
#     (int(cols * 1.5), int(rows * 1.5))
# )

# # Display the sheared image
# cv.imshow("Sahil(CS24106)Sheared Image", sheared_img)

# # Save the output image (optional)
# cv.imwrite("sheared_out.jpg", sheared_img)

# # Wait for a key press and close all windows
# cv.waitKey(0)
# cv.destroyAllWindows()

# code7
# import numpy as np
# import cv2 as cv

# # Read the image in grayscale
# img = cv.imread("cone.jpg", 0)

# # Check if the image is loaded
# if img is None:
#     print("Error: girlImage.jpg not found.")
#     exit()

# # Get image dimensions
# rows, cols = img.shape

# # Y-axis shearing transformation matrix
# M = np.float32([
#     [1, 0, 0],
#     [0.5, 1, 0],
#     [0, 0, 1]
# ])

# # Apply shearing transformation
# sheared_img = cv.warpPerspective(
#     img,
#     M,
#     (int(cols * 1.5), int(rows * 1.5))
# )

# # Display the sheared image
# cv.imshow("SAhil Y-Axis Sheared Image", sheared_img)

# # Save the output image
# cv.imwrite("sheared_y-axis_out.jpg", sheared_img)

# # Wait for a key press and close all windows
# cv.waitKey(0)
# cv.destroyAllWindows()