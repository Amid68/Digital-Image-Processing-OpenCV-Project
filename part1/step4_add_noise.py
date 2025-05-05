import cv2
import numpy as np
import random


gray = cv2.imread('watermarked.jpg', cv2.IMREAD_GRAYSCALE)


def add_salt_pepper_noise(image, amount=0.02):
    noisy = image.copy()
    total_pixels = image.size
    num_noise = int(total_pixels * amount)

    for _ in range(num_noise):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        if random.random() < 0.5:
            noisy[i][j] = 0   # Pepper(black)
        else:
            noisy[i][j] = 255 # Salt(white)
    return noisy


noisy_img = add_salt_pepper_noise(gray, amount=0.02)


cv2.imshow("Original Grayscale", gray)
cv2.imshow("Noisy Image", noisy_img)
cv2.imwrite("noisy.jpg", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
