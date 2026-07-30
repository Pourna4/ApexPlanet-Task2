import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_excel("Dataset/Cleaned_Sales_Dataset.xlsx")

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns)

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())
print("\n" + "=" * 50)
print("NUMERICAL STATISTICS")
print("=" * 50)
print(df.describe())

print("\n" + "=" * 50)
print("CATEGORICAL STATISTICS")
print("=" * 50)
print(df.describe(include='object'))
# ==========================
# FREQUENCY ANALYSIS
# ==========================

print("\n" + "=" * 50)
print("CATEGORY COUNTS")
print("=" * 50)
print(df["Category"].value_counts())

print("\n" + "=" * 50)
print("CITY COUNTS")
print("=" * 50)
print(df["City"].value_counts())

print("\n" + "=" * 50)
print("GENDER COUNTS")
print("=" * 50)
print(df["Gender"].value_counts())
# ==========================
# BAR CHART - SALES BY CATEGORY
# ==========================

sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Output/Sales_by_Category.png")

plt.show(block=False)
plt.pause(2)
plt.close()
# ==========================
# HISTOGRAM - AGE DISTRIBUTION
# ==========================

plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("Output/Age_Distribution.png")
plt.show(block=False)
plt.pause(2)
plt.close()
# ==========================
# PIE CHART - GENDER
# ==========================

gender = df["Gender"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(gender,
        labels=gender.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Gender Distribution")

plt.savefig("Output/Gender_Distribution.png")
plt.show(block=False)
plt.pause(2)
plt.close()
# ==========================
# MONTHLY SALES TREND
# ==========================

df["Month"] = df["Order_Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(10,5))

plt.plot(monthly_sales.index,
         monthly_sales.values,
         marker="o")

plt.xticks(rotation=45)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("Output/Monthly_Sales_Trend.png")
plt.show(block=False)
plt.pause(2)
plt.close()
# ==========================
# TOP 10 PRODUCTS
# ==========================

top_products = (
    df.groupby("Product")["Total_Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(9,6))

top_products.plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")

plt.tight_layout()
plt.savefig("Output/Top10_Products.png")
plt.show(block=False)
plt.pause(2)
plt.close()
