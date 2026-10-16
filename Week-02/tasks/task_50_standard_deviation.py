import numpy as np

# Use speed dataset to calculate standard deviation and variance
speed = [86, 87, 88, 86, 87, 85, 86]

# Standard Deviation
speed_std = np.std(speed)
print("Standard Deviation:", speed_std)

# Variance
speed_variance = np.var(speed)
print("Variance:", speed_variance)
