import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder if not exists
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales.csv")

# Create Total column
df["Total"] = df["Quantity"] * df["Price"]

print("=" * 50)
print(" SALES ANALYTICS DASHBOARD ")
print("=" * 50)

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nSummary")
print(df.describe())

print("\nTotal Revenue :", df["Total"].sum())
print("Average Revenue :", round(df["Total"].mean(),2))
print("Highest Revenue :", df["Total"].max())
print("Lowest Revenue :", df["Total"].min())

# -------------------------
# Product Analysis
# -------------------------

product_sales = df.groupby("Product")["Total"].sum()

print("\nProduct Wise Sales")
print(product_sales)

plt.figure(figsize=(7,5))
product_sales.plot(kind="bar")
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/product_sales.png")
plt.close()

# -------------------------
# Region Analysis
# -------------------------

region_sales = df.groupby("Region")["Total"].sum()

print("\nRegion Wise Sales")
print(region_sales)

plt.figure(figsize=(7,5))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/region_sales.png")
plt.close()

# -------------------------
# Monthly Sales
# -------------------------

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B")

monthly_sales = df.groupby("Month")["Total"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.close()

# -------------------------
# Pie Chart
# -------------------------

plt.figure(figsize=(6,6))
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("charts/sales_distribution.png")
plt.close()

# -------------------------
# Report
# -------------------------

with open("report.txt","w") as file:

    file.write("SALES ANALYTICS REPORT\n")
    file.write("="*40)

    file.write(f"\n\nTotal Revenue : {df['Total'].sum()}")

    file.write(f"\nAverage Revenue : {round(df['Total'].mean(),2)}")

    file.write(f"\nHighest Revenue : {df['Total'].max()}")

    file.write(f"\nLowest Revenue : {df['Total'].min()}")

    file.write("\n\nProduct Wise Sales\n")

    file.write(product_sales.to_string())

    file.write("\n\nRegion Wise Sales\n")

    file.write(region_sales.to_string())

print("\nProject Completed Successfully")
print("Charts Saved Inside charts/")
print("Report Saved : report.txt")