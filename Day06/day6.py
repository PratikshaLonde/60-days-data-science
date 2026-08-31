import pandas as pd

df = pd.read_csv("SuperStoreOrders.csv")

print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

df = df.dropna()

df = df.drop_duplicates()

print("\nData types before conversion:")
print(df.dtypes)

df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="mixed",
    dayfirst=True
)

df["ship_date"] = pd.to_datetime(
    df["ship_date"],
    format="mixed",
    dayfirst=True
)

df["sales"] = df["sales"].str.replace(",", "").astype(float)

print("\nData types after conversion:")
print(df.dtypes)

df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

print("\nShipping days:")
print(df[["order_date", "ship_date", "shipping_days"]].head())

df["profit_margin"] = (df["profit"] / df["sales"]) * 100

print("\nProfit margin:")
print(df[["sales", "profit", "profit_margin"]].head())

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")

print("\nFinal dataset:")
print(df.head())

print("\nFinal shape:")
print(df.shape)

print("\nNew features:")
print(df[["shipping_days", "profit_margin"]].head())