import pandas as pd

# Creating a simple Pandas Series from list
values_list = [1, 7, 2]
default_series = pd.Series(values_list)
print("Series with default index:\n", default_series)
print("\nFirst value:", default_series[0])

# Creating Series with custom labels
labeled_series = pd.Series(values_list, index=["x", "y", "z"])
print("\nSeries with custom labels:\n", labeled_series)
print("Value with label 'y':", labeled_series["y"])

# Creating Series from a dictionary (Key/Value object)
calories = {"day1": 420, "day2": 380, "day3": 390}
calories_series = pd.Series(calories)
print("\nSeries from dictionary:\n", calories_series)
