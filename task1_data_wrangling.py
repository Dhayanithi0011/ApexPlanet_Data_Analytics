

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


FILE = "ApexPlanet_DataAnalytics_Dataset.xlsx"   # keep in the same folder

df_raw = pd.read_excel(FILE, sheet_name="Sales_Dataset")
print(f"Dataset loaded  →  {df_raw.shape[0]} rows × {df_raw.shape[1]} columns\n")


data_dict = {
    "Column"            : list(df_raw.columns),
    "Data Type"         : [str(df_raw[c].dtype) for c in df_raw.columns],
    "Non-Null Count"    : [df_raw[c].notna().sum() for c in df_raw.columns],
    "Null Count"        : [df_raw[c].isna().sum()  for c in df_raw.columns],
    "Unique Values"     : [df_raw[c].nunique()      for c in df_raw.columns],
    "Sample Values"     : [df_raw[c].dropna().iloc[:3].tolist() for c in df_raw.columns],
    "Business Meaning"  : [
        "Unique order identifier (primary key)",
        "Date the order was placed (YYYY-MM-DD string)",
        "Unique customer identifier",
        "Full name of the customer",
        "Age of the customer in years",
        "Gender of the customer (Male / Female)",
        "City where the order was placed",
        "Product name purchased",
        "Product category (Grocery / Electronics / Fashion / Furniture / Education)",
        "Number of units ordered",
        "Price per unit in INR",
        "Total revenue from the order (Quantity × Unit_Price)"
    ]
}

dd = pd.DataFrame(data_dict)
print("=" * 60)
print("  DATA DICTIONARY")
print("=" * 60)
print(dd.to_string(index=False))
print()


print("=" * 60)
print("  DATA QUALITY ASSESSMENT")
print("=" * 60)

print(f"\n[1] Shape            : {df_raw.shape}")
print(f"[2] Duplicate rows   : {df_raw.duplicated().sum()}")

print("\n[3] Missing values per column:")
print(df_raw.isnull().sum().to_string())

print("\n[4] Basic statistics (numeric columns):")
print(df_raw.describe().T.to_string())

# Outlier detection via IQR
print("\n[5] Outlier detection (IQR method):")
num_cols = ["Age", "Quantity", "Unit_Price", "Total_Sales"]
for col in num_cols:
    q1, q3 = df_raw[col].quantile([0.25, 0.75])
    iqr     = q3 - q1
    lo, hi  = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    n_out   = ((df_raw[col] < lo) | (df_raw[col] > hi)).sum()
    print(f"   {col:<15}: {n_out} outliers  (bounds: {lo:.2f} – {hi:.2f})")

print("\n[6] Unique values in categorical columns:")
for col in ["Gender", "Category", "City"]:
    print(f"   {col}: {sorted(df_raw[col].dropna().unique().tolist())}")

print("\n" + "=" * 60)
print("  DATA CLEANING & TRANSFORMATION")
print("=" * 60)

df = df_raw.copy()

# --- 3a. Fix data types ---
df["Order_Date"] = pd.to_datetime(df["Order_Date"])          # string → datetime
df["Age"]        = df["Age"].astype("Int64")                  # float → nullable int
print("\n[3a] Converted Order_Date to datetime & Age to Int64")

# --- 3b. Handle missing values ---
df["Age"]  = df["Age"].fillna(df["Age"].median())             # median imputation
df["City"] = df["City"].fillna("Unknown")                     # flag unknowns
print("[3b] Filled 20 missing Age values with median; 13 missing City → 'Unknown'")

# --- 3c. Remove duplicates (none found, but always good practice) ---
before = len(df)
df.drop_duplicates(inplace=True)
print(f"[3c] Duplicates removed : {before - len(df)}")

# --- 3d. Standardise text columns ---
for col in ["Gender", "Category", "City", "Product"]:
    df[col] = df[col].str.strip().str.title()
print("[3d] Stripped whitespace & title-cased: Gender, Category, City, Product")

# --- 3e. Validate Total_Sales (flag rows where value doesn't match Qty × Price) ---
df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]
df["Sales_Mismatch"]   = ~np.isclose(df["Total_Sales"], df["Calculated_Sales"], rtol=0.01)
n_mismatch = df["Sales_Mismatch"].sum()
print(f"[3e] Total_Sales mismatch rows (>1% error): {n_mismatch}")
# Correct the mismatches
df.loc[df["Sales_Mismatch"], "Total_Sales"] = df.loc[df["Sales_Mismatch"], "Calculated_Sales"]
df.drop(columns=["Calculated_Sales", "Sales_Mismatch"], inplace=True)

# --- 3f. Feature engineering ---
# 1. Extract date parts
df["Order_Year"]  = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_Day"]   = df["Order_Date"].dt.day_name()

# 2. Age group
bins   = [0, 25, 35, 45, 55, 100]
labels = ["18-25", "26-35", "36-45", "46-55", "56+"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)

# 3. Revenue tier
df["Revenue_Tier"] = pd.cut(
    df["Total_Sales"],
    bins=[0, 50_000, 2_00_000, 5_00_000, float("inf")],
    labels=["Low", "Medium", "High", "Premium"]
)

# 4. Price per unit bucket
df["Price_Bucket"] = pd.cut(
    df["Unit_Price"],
    bins=[0, 5000, 20_000, 50_000, float("inf")],
    labels=["Budget", "Mid-range", "Premium", "Luxury"]
)

print("[3f] Feature engineering done:")
print("       + Order_Year, Order_Month, Order_Day")
print("       + Age_Group  (18-25 / 26-35 / 36-45 / 46-55 / 56+)")
print("       + Revenue_Tier (Low / Medium / High / Premium)")
print("       + Price_Bucket (Budget / Mid-range / Premium / Luxury)")

# --- 3g. Final null check ---
remaining_nulls = df.isnull().sum().sum()
print(f"\n[3g] Remaining null values in cleaned dataset: {remaining_nulls}")

print("\n" + "=" * 60)
print("  SAVING OUTPUTS")
print("=" * 60)

# Cleaned dataset
df.to_excel("ApexPlanet_Cleaned_Dataset.xlsx", index=False)
print("  Cleaned dataset  →  ApexPlanet_Cleaned_Dataset.xlsx")

# Data dictionary
dd.to_excel("ApexPlanet_Data_Dictionary.xlsx", index=False)
print(" Data dictionary  →  ApexPlanet_Data_Dictionary.xlsx")

# Cleaning summary report
summary = {
    "Metric": [
        "Original rows",
        "Cleaned rows",
        "Columns (original)",
        "Columns (final)",
        "Duplicates removed",
        "Missing Age (imputed with median)",
        "Missing City (filled → 'Unknown')",
        "Total_Sales mismatches corrected",
        "New features added",
        "Remaining nulls"
    ],
    "Value": [
        df_raw.shape[0],
        df.shape[0],
        df_raw.shape[1],
        df.shape[1],
        before - len(df),
        20,
        13,
        n_mismatch,
        "Order_Year, Order_Month, Order_Day, Age_Group, Revenue_Tier, Price_Bucket",
        remaining_nulls
    ]
}
pd.DataFrame(summary).to_excel("ApexPlanet_Cleaning_Summary.xlsx", index=False)
print(" Cleaning summary →  ApexPlanet_Cleaning_Summary.xlsx")

print("\n" + "=" * 60)
print("  CLEANED DATASET PREVIEW (first 5 rows)")
print("=" * 60)
print(df.head().to_string())
print(f"\nFinal shape: {df.shape}")
print("\nAll done! ")
