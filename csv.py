import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV File
df = pd.read_csv("sales.csv")   # <-- replace with your file name
print("First 5 rows:")
display(df.head())

# 2. Basic Info
print("Shape:", df.shape)
print("\nData Info:")
print(df.info())

# 3. Check Missing Values
print("\nMissing values:")
print(df.isna().sum())

# Optional: Clean missing values
df = df.dropna()

# 4. Summary Statistics
print("\nSummary:")
display(df.describe())

# 5. Groupby Example: Total Sales per Product
if "Product" in df.columns and "Sales" in df.columns:
    sales_per_product = df.groupby("Product")["Sales"].sum()
    print("\nTotal Sales per Product:")
    display(sales_per_product)

    # Bar Chart
    sales_per_product.plot(kind='bar')
    plt.title("Total Sales per Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

# 6. Groupby Example: Sales by Month (if columns exist)
if "Month" in df.columns and "Sales" in df.columns:
    sales_per_month = df.groupby("Month")["Sales"].sum()
    print("\nTotal Sales per Month:")
    display(sales_per_month)

    # Line Chart
    sales_per_month.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

# 7. Filtering Example (Sales > 500)
if "Sales" in df.columns:
    print("\nFiltered rows where Sales > 500:")
    display(df[df["Sales"] > 500])
