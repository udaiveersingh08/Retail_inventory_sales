import pandas as pd 

udaiveersingh = pd.read_csv("Retail_inventory_sales.csv")
print(udaiveersingh.shape)
print(udaiveersingh.info())
print(udaiveersingh.describe())


print(udaiveersingh.isna().sum())
print(udaiveersingh.duplicated().sum())

udaiveersingh["transaction_date"] = pd.to_datetime(udaiveersingh["transaction_date"])

udaiveersingh["unit_cost"] = pd.to_numeric(udaiveersingh["unit_cost"],errors="coerce")
udaiveersingh["unit_price"] = pd.to_numeric(udaiveersingh["unit_price"],errors="coerce")
udaiveersingh["units_sold"] = pd.to_numeric(udaiveersingh["units_sold"],errors="coerce")
udaiveersingh["stock_remaining"] = pd.to_numeric(udaiveersingh["stock_remaining"],errors="coerce")


udaiveersingh["supplier"] = (
    udaiveersingh["supplier"].fillna("Unknown")
    .str.strip()
)

udaiveersingh["unit_cost"] = (
    udaiveersingh["unit_cost"].fillna(000)
)

udaiveersingh["stock_remaining"] = (
    udaiveersingh["stock_remaining"].fillna(00)
)

udaiveersingh["Total_sales"] = udaiveersingh["units_sold"] * udaiveersingh["unit_price"]
udaiveersingh["Total_cost"] = udaiveersingh["units_sold"] * udaiveersingh["unit_cost"]
udaiveersingh["Total_Profit"] = udaiveersingh["Total_sales"] - udaiveersingh["Total_cost"]
udaiveersingh["Profit_Margin"] = (
    udaiveersingh["Total_Profit"] / udaiveersingh["Total_sales"] * 100
).round(2)
print(udaiveersingh)

Low_stock = udaiveersingh.loc[udaiveersingh["stock_remaining"] < 15]
print(Low_stock)
High_sales = udaiveersingh.loc[udaiveersingh["Total_sales"] >= 2000]
print(High_sales)
popular_items = udaiveersingh["item"].value_counts()
print(popular_items)
Store_transactions = udaiveersingh["store"].value_counts()
print(Store_transactions)
Supplier_counts = udaiveersingh["supplier"].value_counts()
print(Supplier_counts)


udaiveersingh.to_csv("retail_inventory_sales_cleaned.csv")
print(udaiveersingh)


