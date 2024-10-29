import avator_match
import edge_detect
import math
import cv2


def get_distance(input):
    avator = avator_match.get_avator(input)
    target = edge_detect.get_target(input)

    distance = math.sqrt(
        math.pow(abs(target[0] - avator[0]), 2)
        + math.pow(abs(target[1] - avator[1]), 2)
    )
    return distance


def test(input):
    image = cv2.imread(input)
    avator = avator_match.get_avator(input)
    target = edge_detect.get_target(input)

    distance = math.sqrt(
        math.pow(abs(target[0] - avator[0]), 2)
        + math.pow(abs(target[1] - avator[1]), 2)
    )

    image = cv2.rectangle(
        image, (avator[0], avator[1]), (avator[0] + 10, avator[1] + 10), (0, 0, 255), 4
    )

    image = cv2.rectangle(
        image, (target[0], target[1]), (target[0] + 10, target[1] + 10), (0, 0, 255), 4
    )
    image = cv2.line(
        image,
        (avator[0], avator[1]),
        (target[0], target[1]),
        (0, 0, 255),
        4,
    )
    image = cv2.resize(image, (int(1080 * 0.4), int(2400 * 0.4)))

    cv2.imshow("Result", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    test("1.png")
