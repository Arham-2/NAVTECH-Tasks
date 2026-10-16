import pandas as pd

# Check Pandas version
print("Pandas version:", pd.__version__)

# Create and display a simple DataFrame
car_data = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}
cars_df = pd.DataFrame(car_data)
print("\nDataFrame:\n", cars_df)
