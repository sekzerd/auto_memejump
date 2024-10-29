import cv2

# 读取图片
image = cv2.imread("output.png", cv2.IMREAD_GRAYSCALE)

# 应用Canny边缘检测
image = cv2.Canny(image, threshold1=100, threshold2=200)

# 显示结果
image = cv2.resize(image, (int(1080 * 0.4), int(2400 * 0.4)))

cv2.imshow("Edges", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
