# import cv2

# template = cv2.imread("avator.png", 0)

# img = cv2.imread("output.png", 0)
# res_end = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# print(res_end)
# if cv2.minMaxLoc(res_end)[1] > 0.95:
#     print("Game over!")
# #  print('Game over!')

import cv2
import numpy as np

# 加载图像和模板
image = cv2.imread("output.png")
template = cv2.imread("avator.png")

# 执行模板匹配
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# 寻找最佳匹配位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 绘制结果
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 4)

# 显示结果
image = cv2.resize(image, (int(1080 * 0.4), int(2400 * 0.4)))
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
