import numpy as np

# Checking data type of an array
int_array = np.array([1, 2, 3, 4])
print("Integer array dtype:", int_array.dtype)

string_array = np.array(["apple", "banana", "cherry"])
print("String array dtype:", string_array.dtype)

# Creating arrays with a defined data type
bytes_array = np.array([1, 2, 3, 4], dtype="S")
print("\nString array:", bytes_array)
print("Data type:", bytes_array.dtype)

int32_array = np.array([1, 2, 3, 4], dtype="i4")
print("4-byte integer dtype:", int32_array.dtype)

# Converting data types using astype()
float_arr = np.array([1.1, 2.1, 3.1])
int_arr = float_arr.astype("i")
print("\nConverted to integer:", int_arr)
print("New dtype:", int_arr.dtype)

# Converting integer to boolean
bool_arr = np.array([1, 0, 3]).astype(bool)
print("Converted to boolean:", bool_arr)
