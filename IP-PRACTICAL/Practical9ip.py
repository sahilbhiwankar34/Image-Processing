# import cv2
# import numpy as np

# def detect_object(template_name, input_image_name):

#     # Read template and original image
#     template = cv2.imread(template_name, 0)
#     original_img = cv2.imread(input_image_name)

#     # Check images
#     if template is None:
#         print("Error: Template image not found!")
#         return

#     if original_img is None:
#         print("Error: Original image not found!")
#         return

#     # Convert original image to grayscale
#     gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

#     # Get template dimensions
#     h, w = template.shape

#     # Perform template matching
#     result = cv2.matchTemplate(
#         gray_img,
#         template,
#         cv2.TM_CCOEFF_NORMED
#     )

#     # Find best matching location
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#     print("Matching Score:", max_val)

#     # Set threshold
#     threshold = 0.5

#     # Copy original image
#     output = original_img.copy()

#     # Check whether object is detected
#     if max_val >= threshold:

#         # Get top-left corner
#         top_left = max_loc

#         # Get bottom-right corner
#         bottom_right = (
#             top_left[0] + w,
#             top_left[1] + h
#         )

#         # Draw rectangle
#         cv2.rectangle(
#             output,
#             top_left,
#             bottom_right,
#             (0, 255, 0),
#             4
#         )

#         print("Object detected!")

#     else:
#         print("Object not detected!")

#     # Resize for display
#     max_width = 800
#     max_height = 600

#     height, width = output.shape[:2]

#     scale = min(
#         max_width / width,
#         max_height / height
#     )

#     new_width = int(width * scale)
#     new_height = int(height * scale)

#     display_output = cv2.resize(
#         output,
#         (new_width, new_height)
#     )

#     # Display result
#     cv2.namedWindow(
#         "Detected Object",
#         cv2.WINDOW_NORMAL
#     )

#     cv2.resizeWindow(
#         "Detected Object",
#         new_width,
#         new_height
#     )

#     cv2.imshow(
#         "Detected Object",
#         display_output
#     )

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# # Enter image names only
# template_name = input("Enter template image name: ")
# input_image_name = input("Enter original image name: ")

# # Detect object
# detect_object(
#     template_name,
#     input_image_name
# )
import cv2
import numpy as np

def detect_object(template_path, input_image_path):

    # Read the template and input image
    template = cv2.imread(template_path, 0)
    img = cv2.imread(input_image_path)

    # Check if images are loaded correctly
    if template is None:
        print("Error: Template image not found!")
        return

    if img is None:
        print("Error: Input image not found!")
        return

    # Convert input image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get width and height of template
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(
        gray_img,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    # Set matching threshold
    threshold = 0.6

    # Find locations where match is above threshold
    loc = np.where(res >= threshold)

    # Count detected objects
    count = 0

    # Draw rectangles around detected objects
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            img,
            pt,
            (pt[0] + w, pt[1] + h),
            (0, 255, 255),
            2
        )
        count += 1

    # Print detected object count
    print("Number of detected objects:", count)

    # Print original image size
    height, width = img.shape[:2]
    print("Original Image Size:", width, "x", height)

    # Resize image for display
    display_width = 600
    display_height = 400

    resized_img = cv2.resize(
        img,
        (display_width, display_height)
    )

    # Display detected image
    cv2.imshow("CS24086 Detected Objects", resized_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Path to template image
template_path = "target.jpeg"

# Path to input image
input_image_path = "desk.jpeg"

# Detect object
detect_object(template_path, input_image_path)