import cv2


image = cv2.imread('my_image.jpg')


image = cv2.resize(image, (600, 400))


text1 = "Yahya Musmar - 12112501"
text2 = "Ameed Othman - 12220692"
cv2.putText(image, text1, (30, 360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(image, text2, (30, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


cv2.imshow("Watermarked Image", image)
cv2.imwrite("watermarked.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
