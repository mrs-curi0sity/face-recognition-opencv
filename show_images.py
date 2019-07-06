import cv2
from math import floor

# 1 => rgb => 3 bands 
# 0 => greyscale => 1 kanal
# -1 => color + alpha (transparency => 4 Kanäle)
#
img = cv2.imread('wetteronline.jpg', 1)

print(type(img))
print(img.shape)

resized_image = cv2.resize(img, (300, 400))

resized_image_keep_proportions = cv2.resize(img, (floor(img.shape[1]/2), floor(img.shape[0]/2)))


cv2.imshow('this is a window', resized_image_keep_proportions)

cv2.imwrite('wetteronline_resized.jpg', resized_image_keep_proportions)

# wait for some time before close after button ist closed in ms
# 2000 => 2 Seunden
cv2.waitKey(4000)
cv2.destryAllWindows()