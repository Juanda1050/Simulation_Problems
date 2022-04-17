import numpy as np

ranges = [0, 0.5, 1]
numbers = [(0.03991, 0.38555), (0.38555, 0.17546), (0.17546, 0.32643), (0.32643, 0.69572), (0.69572, 0.24122), (0.24122, 0.61196), (0.61196, 0.30532), (0.30532, 0.03788), (0.30532, 0.48228)]
cells = []

interval = 1 / 2
interval_x = 0
interval_y = 0

counters = []
count = 0

for x in np.arange(interval_x, 1, (interval_x + interval)):
    x_values = []
    for y in np.arange(interval_y, 1, (interval_y + interval)):
        count = 0
        for pairs in numbers:
            if interval_x <= pairs[0] < (interval_x + interval) and interval_y <= pairs[1] < (interval_y + interval):
                count += 1
        interval_y += interval
        x_values.append(count)
    interval_y = 0
    interval_x += interval
    counters.append(x_values)

print(counters)
