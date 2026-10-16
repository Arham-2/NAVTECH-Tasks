import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Mean
mean_speed = np.mean(speed)
print("Mean:", mean_speed)

# Median
median_speed = np.median(speed)
print("Median:", median_speed)

# Mode
mode_result = stats.mode(speed, keepdims=True)
print("Mode:", mode_result.mode[0])
