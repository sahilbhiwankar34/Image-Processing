# # TELEA and NAVIER-STOKES INPAINTING

# import cv2
# import numpy as np
# # Step 1: Read the damaged feather image
# damaged_img = cv2.imread("feather_damaged.png")

# if damaged_img is None:
#     raise FileNotFoundError(
#         "Could not find 'feather_damaged.png'."
#     )


# # Step 2: Get image height and width
# height, width = damaged_img.shape[:2]

# print("Image Width  :", width)
# print("Image Height :", height)


# # Step 3: Create an empty black mask
# mask = np.zeros(
#     (height, width),
#     dtype=np.uint8
# )


# # Step 4: Detect black/damaged pixels
# black_pixels = np.all(
#     damaged_img == [0, 0, 0],
#     axis=2
# )


# # Step 5: Make damaged pixels WHITE in the mask
# mask[black_pixels] = 255


# # Step 6: Save the generated mask
# cv2.imwrite(
#     "generated_mask.png",
#     mask
# )


# # Step 7: Restore image using TELEA
# restored_telea = cv2.inpaint(
#     damaged_img,
#     mask,
#     3,
#     cv2.INPAINT_TELEA
# )


# # ============================================================
# # PART 2: Use Predefined Mask and Restore Using
# # NAVIER-STOKES
# # ============================================================

# # Step 8: Read damaged feather image again
# img = cv2.imread("feather_damaged.png")

# if img is None:
#     raise FileNotFoundError(
#         "Could not find 'feather_damaged.png'."
#     )


# # Step 9: Load predefined mask
# mask_predefined = cv2.imread(
#     "feather_mask.png",
#     cv2.IMREAD_GRAYSCALE
# )

# if mask_predefined is None:
#     raise FileNotFoundError(
#         "Could not find 'feather_mask.png'."
#     )


# # Step 10: Check mask and image dimensions
# if mask_predefined.shape != img.shape[:2]:
#     raise ValueError(
#         "The predefined mask and damaged image "
#         "must have the same dimensions."
#     )


# # Step 11: Restore image using Navier-Stokes
# restored_ns = cv2.inpaint(
#     img,
#     mask_predefined,
#     3,
#     cv2.INPAINT_NS
# )


# # ============================================================
# # PART 3: Save Results
# # ============================================================

# cv2.imwrite(
#     "generated_mask.png",
#     mask
# )

# cv2.imwrite(
#     "restored_telea.png",
#     restored_telea
# )

# cv2.imwrite(
#     "restored_ns.png",
#     restored_ns
# )

# print("Generated mask saved as: generated_mask.png")
# print("TELEA result saved as: restored_telea.png")
# print("Navier-Stokes result saved as: restored_ns.png")


# # ============================================================
# # PART 4: Display Results
# # ============================================================

# cv2.imshow(
#     "CS24106 - Damaged Feather",
#     damaged_img
# )

# cv2.imshow(
#     "CS24106 - Generated Mask",
#     mask
# )

# cv2.imshow(
#     "CS24106 - Restored using TELEA",
#     restored_telea
# )

# cv2.imshow(
#     "CS24106 - Predefined Mask",
#     mask_predefined
# )

# cv2.imshow(
#     "CS24106 - Restored using Navier-Stokes",
#     restored_ns
# )


# # Wait until a key is pressed
# cv2.waitKey(0)

# # Close all windows
# cv2.destroyAllWindows()

# #code2
# import cv2 
# import matplotlib.pyplot as plt 
# # Read noisy image 
# img = cv2.imread("distorted.jpeg", 0)  # grayscale 
# # Apply Gaussian Blur 
# restored = cv2.GaussianBlur(img, (5, 5), 0) 
# # Show results 
# plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("CS24106 Gaussian Noisy") 
# plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("CS24106 Restored (Gaussian Blur)") 
# plt.show()

#code3
# import cv2
# import matplotlib.pyplot as plt
# # Read noisy image
# img = cv2.imread("blurred.jpeg", 0)
# # Apply Median Filter
# restored = cv2.medianBlur(img, 5)
# # Show results
# plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("CS24106 Salt & Pepper Noise")
# plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("CS24106Restored (Median Filter)")
# plt.show()

#code 4
# import cv2
# import matplotlib.pyplot as plt
# # Read noisy image
# img = cv2.imread("distorted.jpeg", 0)
# # Apply Non-local Means Denoising
# restored = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
# # Show results
# plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("CS24106 Noisy Image")
# plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("CS24106 Restored (Non-local Means)")
# plt.show()

# #code5
# import cv2

# import numpy as np

# import matplotlib.pyplot as plt

# # Read scratched/damaged image

# img = cv2.imread("scratched.jpeg", 0)

# # Create mask (white = damaged parts)

# mask = np.zeros(img.shape, np.uint8)

# # Mark the main diagonal crack
# cv2.line(mask, (285, 120), (260, 155), 255, 8)
# cv2.line(mask, (260, 155), (245, 185), 255, 8)
# cv2.line(mask, (245, 185), (220, 215), 255, 8)

# # Inpaint damaged regions

# restored = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# # Show results

# plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title("Damaged Image")

# plt.subplot(1, 3, 2), plt.imshow(mask, cmap='gray'), plt.title("Mask")

# plt.subplot(1, 3, 3), plt.imshow(restored, cmap='gray'), plt.title("CS24106 Restored (Inpainting)")

# plt.show()

#code6
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# # Base clean image (gray background + circle)
# img = np.ones((256, 256), dtype=np.uint8) * 127
# cv2.circle(img, (128, 128), 60, 200, -1)
# # Add Gaussian noise
# noise = np.random.normal(0, 25, img.shape).astype(np.int16)
# gaussian_noisy = cv2.add(img.astype(np.int16), noise, dtype=cv2.CV_8U)
# cv2.imwrite("noisy_gaussian.jpeg", gaussian_noisy)
# plt.imshow(gaussian_noisy, cmap="gray")
# plt.title("CS24106 Gaussian Noisy Image")
# plt.axis("off")
# plt.show()

# #code7
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Base clean image (gray background + rectangle)
# img = np.ones((256, 256), dtype=np.uint8) * 127
# cv2.rectangle(img, (60, 60), (200, 200), 200, -1)
# # Add Salt & Pepper noise
# s_p_img = img.copy()
# num_noise = 2000  # number of noise pixels
# # Salt
# coords = [np.random.randint(0, i-1, num_noise) for i in img.shape]
# s_p_img[coords] = 255
# # Pepper
# coords = [np.random.randint(0, i-1, num_noise) for i in img.shape]
# s_p_img[coords] = 0
# cv2.imwrite("noisy_salt_pepper.png", s_p_img)
# plt.imshow(s_p_img, cmap="gray")
# plt.title("CS24106 Salt & Pepper Noise")
# plt.axis("off")
# plt.show()

#code8
# import cv2 
# import numpy as np 
# import matplotlib.pyplot as plt 
 
# # Base clean image (gray background + text) 
# img = np.ones((256, 256), dtype=np.uint8) * 180 
# cv2.putText(img, "SAHIL", (60, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, 50, 5) 
 
# # Add mixed random noise 
# noise = np.random.randint(0, 50, img.shape, dtype=np.uint8) 
# noisy_img = cv2.add(img, noise) 
 
# cv2.imwrite("noisy_image.png", noisy_img) 
 
# plt.imshow(noisy_img, cmap="gray") 
# plt.title("CS24106 General Noisy Image") 
# plt.axis("off") 
# plt.show()

# #code9
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# # Base clean image (gray background + text)
# img = np.ones((256, 256), dtype=np.uint8) * 200
# cv2.putText(img, "CAT", (70, 140), cv2.FONT_HERSHEY_SIMPLEX, 2, 50, 5)
# # Add scratches (black lines)
# scratched = img.copy()
# cv2.line(scratched, (30, 100), (220, 120), 0, 3)
# cv2.line(scratched, (100, 30), (120, 220), 0, 3)
# cv2.imwrite("scratched.png", scratched)
# plt.imshow(scratched, cmap="gray")
# plt.title("CS24106 Scratched Image")
# plt.axis("off")
# plt.show()

# import cv2 
# import numpy as np 
# import matplotlib.pyplot as plt 
 
# # ------------------------------- 
# # Step 1: Read the damaged image 
# # ------------------------------- 
# damaged_img = cv2.imread("feather_damaged.png") 
 
# # ------------------------------- 
# # Step 2: Create mask automatically 
# # ------------------------------- 
# height, width = damaged_img.shape[0], damaged_img.shape[1] 
 
# mask_auto = np.zeros((height, width, 3), dtype=np.uint8) 
# for i in range(height): 
#     for j in range(width): 
#         if damaged_img[i, j].sum() > 0:   # non-black pixel 
#             mask_auto[i, j] = [0, 0, 0] 
#         else:  # damaged black pixel → white in mask 
#             mask_auto[i, j] = [255, 255, 255] 
 
# # Convert mask to grayscale 
# mask_auto_gray = cv2.cvtColor(mask_auto, cv2.COLOR_BGR2GRAY) 
 
# # ------------------------------- 
# # Step 3: Restore with TELEA method 
# # ------------------------------- 
# restored_telea = cv2.inpaint(damaged_img, mask_auto_gray, 3, cv2.INPAINT_TELEA) 
 
# # ------------------------------- 
# # Step 4: Restore with Predefined Mask using NS method 
# # ------------------------------- 
# mask_predefined = cv2.imread("feather_mask.png", 0)  # must exist 
# restored_ns = cv2.inpaint(damaged_img, mask_predefined, 3, cv2.INPAINT_NS) 
 
# # ------------------------------- 
# # Step 5: Plot results using Matplotlib 
# # ------------------------------- 
# images = [damaged_img, mask_auto_gray, restored_telea, restored_ns] 
# titles = ["CS24106 Original Damaged", "CS24106 Generated Mask", "CS24106 Restored (Telea)", "CS24106 Restored (Navier-Stokes)"] 
  
# plt.figure(figsize=(12, 6)) 
  
# for i in range(4): 
#     plt.subplot(2, 2, i+1) 
#     if len(images[i].shape) == 2:   # grayscale (mask) 
#         plt.imshow(images[i], cmap="gray") 
#     else: 
#         plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # convert BGR → RGB 
#     plt.title(titles[i]) 
#     plt.axis("off") 
  
# plt.tight_layout() 
# plt.show()


