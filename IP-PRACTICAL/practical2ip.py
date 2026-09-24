# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("icecream.JFIF")
# # Converting BGR color to RGB color format
# RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #Displaying image using plt.imshow() method
# plt.imshow(RGB_img)
# plt.axis("off")
# plt.show(block=False)
# plt.pause(10)   # Window stays open for 10 seconds
# plt.close()


# import cv2

# Read image in grayscale
# path = r'icecream.JFIF'
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# #Resize image
# img = cv2.resize(img, (600, 600))

# # # Display image
# cv2.imshow('Sahil Bhiwankar (CS24103)', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2 
# import numpy as np 
# image1 = cv2.imread('shapes.jfif') 
# image2 = cv2.imread('time.jfif')
# weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# cv2.imshow('Sahil Bhiwankar(CS24106)', weightedSum)
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows() 



# import cv2
# import numpy as np
# image1 = cv2.imread('shapes.jfif')
# image2 = cv2.imread('time.jfif')
# sub = cv2.subtract(image1, image2)
# cv2.imshow('Sahil Bhiwankar(CS24106)', sub)
# # De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# import cv2 
# import numpy as np 
# img1 = cv2.imread('shapes.jfif')  
# img2 = cv2.imread('time.jfif') 
# dest_and = cv2.bitwise_and(img2, img1, mask = None)
# cv2.imshow('Sahil bhiwankar bitwise AND (CS24106)', dest_and)
#  # De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows() 


# import cv2 
# import numpy as np 
# img1 = cv2.imread('shapes.jfif')  
# img2 = cv2.imread('time.jfif') 
# dest_or = cv2.bitwise_or(img2, img1, mask = None)
# cv2.imshow('Sahil bhiwankar (CS24106)Bitwise OR', dest_or)
#  # De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows() 

# import cv2 
# import numpy as np 
# img1 = cv2.imread('shapes.jfif')  
# img2 = cv2.imread('time.jfif') 
# dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
# cv2.imshow('Sahil Bhiwankar (CS24106) Bitwise XOR', dest_xor)
 
# # De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows() 

# import cv2 
# import numpy as np 
   
# img1 = cv2.imread('shapes.jfif')  
# img2 = cv2.imread('time.jfif') 
# dest_not1 = cv2.bitwise_not(img1, mask = None)
# dest_not2 = cv2.bitwise_not(img2, mask = None)
# cv2.imshow('Sahil bhiwankar(CS24106) Bitwise NOT on image 1', dest_not1)
# cv2.imshow('Sahil bhiwankar(CS24106)Bitwise NOT on image 2', dest_not2)
#  # De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows() 


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("icecream.jfif")
plt.imshow(img)
plt.waitforbuttonpress()
plt.pause(10)
plt.close('all')
