# # Import OpenCV
# import cv2
# # Read the image in grayscale (0) or color (1)
# img = cv2.imread('bw.jfif', 0)  # Change 0 to 1 for color
# # Create the negative image
# negative = 255 - img
# # Show original and negative side-by-side
# import numpy as np
# combined = np.hstack((img, negative))
# cv2.imshow('CS24106 Original (Left) vs Negative (Right)', combined)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#code2
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# # Load the image
# image = cv2.imread('time.jfif')
# #Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(image)
# # Adjust the brightness and contrast
# # Adjusts the brightness by adding 10 to each pixel value
# brightness = 10 
# # Adjusts the contrast by scaling the pixel values by 2.3
# contrast = 2.3  
# image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)
# #Save the image
# cv2.imwrite('modified_image.jpg', image2)
# #Plot the contrast image
# plt.subplot(1, 2, 2)
# plt.title("Brightness & contrast")
# plt.imshow(image2)
# plt.show()

#code3
# #Import the necessary libraries
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the image
# image = cv2.imread('time.jfif')

# #Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(image)

# # Adjust the brightness and contrast 
# # g(i,j)=α⋅f(i,j)+β
# # control Contrast by 1.5
# alpha = 1.5  
# # control brightness by 50
# beta = 50  
# image2 = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# #Save the image
# cv2.imwrite('Brightness & contrast.jpg', image2)
# #Plot the contrast image
# plt.subplot(1, 2, 2)
# plt.title("Brightness & contrast")
# plt.imshow(image2)
# plt.show()

#code4
# #Import the necessary libraries
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the image
# image = cv2.imread('time.jfif')

# #Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("CS24106 original")
# plt.imshow(image)

# # Create the sharpening kernel
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
 
# # Sharpen the image
# sharpened_image = cv2.filter2D(image, -1, kernel)
 
# #Save the image
# cv2.imwrite('sharpened_image.jpg', sharpened_image)

# #Plot the sharpened image
# plt.subplot(1, 2, 2)
# plt.title("CS24106 Sharpening")
# plt.imshow(sharpened_image)
# plt.show()

#code5
# #Import the necessary libraries
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the image
# image = cv2.imread('time.jfif.jpeg')

# #Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(image)

# # Sharpen the image using the Laplacian operator
# sharpened_image2 = cv2.Laplacian(image, cv2.CV_64F)

# #Save the image
# cv2.imwrite('Laplacian sharpened_image.jpg', sharpened_image2)


# #Plot the sharpened image
# plt.subplot(1, 2, 2)
# plt.title("Laplacian Sharpening")
# plt.imshow(sharpened_image2)
# plt.show()

#code6
# Import the necessary libraries
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the image
# image = cv2.imread('time.jfif.jpeg')

# #Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(image)

# # Remove noise using a median filter
# filtered_image = cv2.medianBlur(image, 11)

# #Save the image
# cv2.imwrite('Median Blur.jpg', filtered_image)

# #Plot the blured image
# plt.subplot(1, 2, 2)
# plt.title("Median Blur")
# plt.imshow(filtered_image)
# plt.show()

#code 7
# import Opencv
# import cv2

# # import Numpy
# import numpy as np

# # read a image using imread
# img = cv2.imread('time.jfif.jpeg', 0)

# # creating a Histograms Equalization
# # of a image using cv2.equalizeHist()
# equ = cv2.equalizeHist(img)

# # stacking images side-by-side
# res = np.hstack((img, equ))

# # show image input vs output
# cv2.imshow('CS24106', res)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code8
# import Opencv
# import cv2

# # import Numpy
# import numpy as np

# # import Matplotlib
# import matplotlib.pyplot as plt

# # read a image using imread
# img = cv2.imread('time.jfif.jpeg', 0)  # grayscale

# # creating a Histograms Equalization
# equ = cv2.equalizeHist(img)

# # stacking images side-by-side
# res = np.hstack((img, equ))

# # show image input vs output
# cv2.imshow('Original vs Equalized', res)

# # Plotting histograms
# plt.figure(figsize=(10, 5))

# # Original image histogram
# plt.subplot(1, 2, 1)
# plt.hist(img.ravel(), 256, [0, 256], color='blue')
# plt.title('CS24106 Original Histogram')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')

# # Equalized image histogram
# plt.subplot(1, 2, 2)
# plt.hist(equ.ravel(), 256, [0, 256], color='green')
# plt.title('CS24106 Equalized Histogram')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')

# plt.tight_layout()
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#code9
# # Python program to illustrate
# # simple thresholding type on an image

# # organizing imports
# import cv2
# import numpy as np

# # path to input image is specified and
# # image is loaded with imread command
# image1 = cv2.imread('time.jfif.jpeg')

# # cv2.cvtColor is applied over the
# # image input with applied parameters
# # to convert the image in grayscale
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# # applying different thresholding
# # techniques on the input image
# # all pixels value above 120 will
# # be set to 255
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# # the window showing output images
# # with the corresponding thresholding
# # techniques applied to the input images
# cv2.imshow('CS24106 Binary Threshold', thresh1)
# cv2.imshow('CS24106 Binary Threshold Inverted', thresh2)
# cv2.imshow('CS24106 Truncated Threshold', thresh3)
# cv2.imshow('CS24106 Set to 0', thresh4)
# cv2.imshow('CS24106 Set to 0 Inverted', thresh5)

# # De-allocate any associated memory usage
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()