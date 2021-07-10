import cv2
from matplotlib import pyplot as plt

img=cv2.imread('einstein.jpg',1)
blur_gaus1 = cv2.GaussianBlur(img,(5,5),0)
blur_gaus2 = cv2.GaussianBlur(img,(9,9),0)
diff=blur_gaus1-blur_gaus2
plt.figure(),plt.title("Final image"),plt.axis("off"),plt.imshow(diff)
plt.show()
