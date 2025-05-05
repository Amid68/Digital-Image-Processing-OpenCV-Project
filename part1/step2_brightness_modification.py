import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


gray = cv2.imread('grayscale.jpg', cv2.IMREAD_GRAYSCALE)


c = round(random.uniform(0.4, 2.0), 2)
print(f"Brightness multiplier (c): {c}")


brightened = np.clip(c * gray, 0, 255).astype(np.uint8)


cv2.imshow("Original Grayscale", gray)
cv2.imshow(f"Brightness Adjusted (c={c})", brightened)
cv2.imwrite("brightness_modified.jpg", brightened)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.hist(brightened.ravel(), bins=256, range=(0, 256), color='gray')
plt.title(f"Histogram After Brightness Adjustment (c={c})")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
