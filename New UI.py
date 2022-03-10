# import sys
#
# with open('Ocr_text.txt', 'r') as f:
#     lines = f.read()
#     original_stdout = sys.stdout
#     with open('new_text', 'w') as file:
#         for key, val in enumerate(lines.split(), start=1):
#             sys.stdout = file
#             if key % 4 == 0:
#                 print(val, end='\n\n')
#             else:
#                 print(val, end=' ')
#             sys.stdout = original_stdout
#
# with open('Ocr_text.txt', 'r') as f:
#     lines = f.read()
#     original_stdout = sys.stdout
#     with open('new_text_1', 'w') as file:
#         for key, val in enumerate(lines.split(), start=1):
#             sys.stdout = file
#             if key % 3 == 0:
#                 print(val, end='\n\n')
#             else:
#                 print(val, end=' ')
#             sys.stdout = original_stdout
#
# with open('Ocr_text.txt', 'r') as f:
#     lines = f.read()
#     original_stdout = sys.stdout
#     with open('new_text_2', 'w') as file:
#         for key, val in enumerate(lines.split(), start=1):
#             sys.stdout = file
#             if key % 2 == 0:
#                 print(val, end='\n\n')
#             else:
#                 print(val, end=' ')
#             sys.stdout = original_stdout
import cv2
import numpy as np

img = cv2.imread('Captured Images/Cropped_Image1.png')

print(img.shape)  # Print image shape

cv2.imshow("original", img)


# Cropping an image

cropped_image = img[30:1640, 0:1007]

# Display cropped image

cv2.imshow("cropped", cropped_image)

# Save the cropped image

cv2.imwrite("Cropped Image.jpg", cropped_image)



cv2.waitKey(0)

cv2.destroyAllWindows()

