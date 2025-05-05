import cv2
import numpy as np


noisy = cv2.imread('noisy.jpg', cv2.IMREAD_GRAYSCALE)


mean_filtered = cv2.blur(noisy, (3, 3))


median_filtered = cv2.medianBlur(noisy, 3)


cv2.imshow("Noisy", noisy)
cv2.imshow("Mean Filter", mean_filtered)
cv2.imshow("Median Filter", median_filtered)

cv2.imwrite("filtered_mean.jpg", mean_filtered)
cv2.imwrite("filtered_median.jpg", median_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
