import cv2
import numpy as np


filtered = cv2.imread('filtered_median.jpg', cv2.IMREAD_GRAYSCALE)


sharpen_kernel = np.array([[0, -1,  0],
                           [-1, 5, -1],
                           [0, -1,  0]])


sharpened = cv2.filter2D(filtered, -1, sharpen_kernel)


cv2.imshow("Median Filtered", filtered)
cv2.imshow("Sharpened", sharpened)
cv2.imwrite("sharpened.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
