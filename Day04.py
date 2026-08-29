import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Day 4 Data Science Setup")

print("NumPy: Working")
print("Pandas: Working")
print("Matplotlib: Working")
print("Seaborn: Working")

data = pd.read_csv("sales_data.csv")

print("\nSales Dataset Loaded Successfully!")
print("Rows:", len(data))
print("Columns:", len(data.columns))

print("\nFirst 5 rows:")
print(data.head())