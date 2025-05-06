import cv2
import numpy as np

input_image = cv2.imread(r'C:\Users\perve\OneDrive\Desktop\pai tasks\Essa Awan.JPG')

segmentation_mask = np.zeros(input_image.shape[:2], np.uint8)
roi = (10, 10, input_image.shape[1] - 10, input_image.shape[0] - 10)

bg_model = np.zeros((1, 65), np.float64)
fg_model = np.zeros((1, 65), np.float64)
cv2.grabCut(input_image, segmentation_mask, roi, bg_model, fg_model, 5, cv2.GC_INIT_WITH_RECT)

final_mask = np.where((segmentation_mask == 2) | (segmentation_mask == 0), 0, 1).astype('uint8')
output_image = input_image * final_mask[:, :, np.newaxis]

cv2.imshow('Processed Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('processed_output.jpg', output_image)
print("Image saved as processed_output.jpg")
