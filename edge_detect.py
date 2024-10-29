import cv2


def test():
    image = cv2.imread("4.png", cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    # for i in range(h):
    #     for j in range(w):
    #         if image[i, j] == 96:
    #             image[i, j] = 192

    image = cv2.Canny(image, threshold1=10, threshold2=20)
    image = cv2.rectangle(image, (0, 0), (1080, 400), (0, 0, 0), thickness=cv2.FILLED)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    mmin_y = h

    for i in range(h):
        for j in range(w):
            if image[i, j] == 255:
                if i < mmin_y:
                    mmin_y = i

    min_y = mmin_y
    min_x = w
    count_x = 0
    for i in range(h):
        for j in range(w):
            if image[i, j] == 255:
                if i < mmin_y + 10:
                    min_x += j
                    count_x += 1

    min_x = int(min_x / count_x)
    min_y = min_y + 80

    print(f"min_y: {min_y}, min_x: {min_x}  ")
    for i in range(50):
        for j in range(50):
            image[min_y - 25 + i, min_x - 25 + j] = 255

    # image = cv2.rectangle(
    #     image, (min_x, min_y), (min_x + 10, min_y + 10), (0, 255, 0), thickness=cv2.FILLED
    # )

    image = cv2.resize(image, (int(1080 * 0.4), int(2400 * 0.4)))

    cv2.imshow("Edges", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_target(input_filename):
    image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    image = cv2.Canny(image, threshold1=10, threshold2=20)
    image = cv2.rectangle(image, (0, 0), (1080, 400), (0, 0, 0), thickness=cv2.FILLED)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    mmin_y = h

    for i in range(h):
        for j in range(w):
            if image[i, j] == 255:
                if i < mmin_y:
                    mmin_y = i

    min_y = mmin_y
    min_x = w
    count_x = 0
    for i in range(h):
        for j in range(w):
            if image[i, j] == 255:
                if i < mmin_y + 10:
                    min_x += j
                    count_x += 1

    min_x = int(min_x / count_x)
    min_y = min_y + 80
    for i in range(50):
        for j in range(50):
            image[min_y - 25 + i, min_x - 25 + j] = 255

    return (min_x, min_y)


if __name__ == "__main__":
    print(get_target("4.png"))
