import uiautomator2 as u2
import time
from analyse import get_distance

d = u2.connect()
print(d.info)

time.sleep(5)

param = 1.8
cache_file = "output.png"

while True:
    screenshot = d.screenshot()
    screenshot.save(cache_file)
    distance = get_distance(cache_file)
    print(f"distance:{distance}")
    d.long_click(500, 1000, ((distance / 1000) * param))
    time.sleep(((distance / 1000) * param) + 1)
    # d.touch_up(1000, 500)

    # time.sleep(2)

# screenshot = d.screenshot()
# screenshot.save("t1.png")
# distance = get_distance(cache_file)
# print(distance)
# d.long_click(500, 1000, 1)
# time.sleep(1.1)
# screenshot = d.screenshot()
# screenshot.save("t2.png")
