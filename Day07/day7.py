import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nNumerical summary:")
print(df.describe())

plt.figure(figsize=(8, 5))
plt.hist(df["sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["profit"], bins=30)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
df["category"].value_counts().plot(kind="bar")
plt.title("Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")
plt.show()

plt.figure(figsize=(8, 5))
df["segment"].value_counts().plot(kind="bar")
plt.title("Orders by Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Orders")
plt.show()

print("\nTop 5 categories:")
print(df["category"].value_counts().head())

print("\nTop 5 regions:")
print(df["region"].value_counts().head())

print("\nHighest profit products:")
print(df.groupby("product_name")["profit"].sum().sort_values(ascending=False).head())

print("\nLowest profit products:")
print(df.groupby("product_name")["profit"].sum().sort_values().head())

print("\nAverage sales by category:")
print(df.groupby("category")["sales"].mean())

print("\nAverage profit by category:")
print(df.groupby("category")["profit"].mean())

print("\nEDA completed successfully!")

print("\n5 EDA Insights:")

print("1. Sales values are unevenly distributed, with most orders having relatively lower sales.")

print("2. Profit varies significantly across orders, with some orders generating negative profit.")

print("3. The Technology, Furniture, and Office Supplies categories show different order volumes.")

print("4. Customer segments have different numbers of orders, with Consumer being a major segment.")

print("5. Shipping time and profit can vary across different orders, which may affect overall business performance.")

print("\nSprint 1 Review:")

print("\nWhat I learned:")
print("1. I learned how to clean and preprocess real-world datasets.")
print("2. I learned how to explore data using Python and Pandas.")
print("3. I learned how to create graphs to understand data patterns.")
print("4. I learned how to identify trends, variations, and outliers.")
print("5. I learned how EDA helps in making better data-driven decisions.")

print("\nChallenges I faced:")
print("1. Handling different date formats.")
print("2. Converting sales values containing commas into numeric values.")
print("3. Understanding patterns from large datasets.")
print("4. Creating useful features from existing columns.")