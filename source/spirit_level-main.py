from microbit import *

# Maximal distance
# Defines a range around the center of mass where LEDs should be affected.
MAX_DISTANCE = 1

# Accelerometer boundaries
# With smaller values (e.g. -700, 700) you can get into the corners,
# but it's more difficult to get just one spot with full brightness.
ACC_MIN = -1000
ACC_MAX = 1000

def map_val(val, min_a, max_a, min_b, max_b):
    diff_a = max_a - min_a
    diff_b = max_b - min_b
    return (val - min_a) / diff_a * diff_b + min_b

while True:
    ax = map_val(accelerometer.get_x(), ACC_MIN, ACC_MAX, 0, 4)
    ay = map_val(accelerometer.get_y(), ACC_MIN, ACC_MAX, 0, 4)
    for x in range(0, 5):
        for y in range(0, 5):
            dx = ax - x
            dy = ay - y
            d = (dx ** 2 + dy ** 2) ** .5
            b = 0
            if d < MAX_DISTANCE:
                b = 9 - d / MAX_DISTANCE * 9
            display.set_pixel(x, y, round(b))
    sleep(20)
