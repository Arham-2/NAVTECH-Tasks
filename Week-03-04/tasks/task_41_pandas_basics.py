import pandas as pd

# Basic dataset
car_data = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

# Create DataFrame
df = pd.DataFrame(car_data)
print("Pandas DataFrame:")
print(df)
