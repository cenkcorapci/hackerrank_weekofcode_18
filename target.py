import sys
import math


def get_distance_to_origin(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def get_point(rad_arr, dist):
    lo = 0
    hi = len(rad_arr) - 1
    while lo < hi:
        mid = (lo + hi) / 2
        midval = rad_arr[mid]
        if midval >= dist and rad_arr[mid + 1] < dist:
            return mid + 1
        elif midval > dist:
            lo = mid + 1
        elif midval < dist:
            hi = mid
    return 0


k, n = [int(x) for x in raw_input().strip().split(' ')]
radiuses = [int(x) for x in raw_input().strip().split(' ')]
radiuses.append(-1)
shots = []
score = 0
for x_i in xrange(n):
    (x, y) = map(int, raw_input().strip().split(' '))
    dist = max(x, y)
    point = get_point(radiuses, dist)
    print point
    score += point

print score
