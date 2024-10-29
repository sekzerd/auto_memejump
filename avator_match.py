import cv2


def test():
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


def get_avator(input_file):
    image = cv2.imread(input_file)
    template = cv2.imread("avator.png")
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    return (
        int(int(top_left[0] + bottom_right[0]) / 2),
        int(int(bottom_right[1])),
    )


if __name__ == "__main__":
    print(get_avator("4.png"))
