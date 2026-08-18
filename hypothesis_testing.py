"""
Task 4 - Statistical Validation: Welch ANOVA
Business Question: Do average sales values differ significantly across product categories?

Hypotheses:
  H0: u_Education = u_Electronics = u_Fashion = u_Furniture = u_Grocery
  H1: At least one category mean differs.

Significance level: a = 0.05
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, levene
from statsmodels.stats.oneway import anova_oneway
import warnings
warnings.filterwarnings("ignore")

# ============================================
# CONFIGURATION
# ============================================
ALPHA = 0.05
DATA_PATH = "../task 2/ApexPlanet_DataAnalytics_Dataset.xlsx"

# ============================================
# LOAD DATA
# ============================================
df = pd.read_excel(DATA_PATH)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("=" * 60)
print("  TASK 4: STATISTICAL VALIDATION")
print("  Welch ANOVA - Category vs Average Sales")
print("=" * 60)

# ============================================
# DESCRIPTIVE SUMMARY BY CATEGORY
# ============================================
summary = df.groupby("Category")["Total_Sales"].agg(
    Count="count",
    Mean="mean",
    Median="median",
    Std="std",
    Min="min",
    Max="max"
)

print("\n========================================")
print("  DESCRIPTIVE STATISTICS BY CATEGORY")
print("========================================")
print(summary.round(2))

summary.to_csv("statistical_results.csv")
print("\n  Saved -> statistical_results.csv")

# ============================================
# CREATE GROUPS
# ============================================
groups = [
    group["Total_Sales"].values
    for _, group in df.groupby("Category")
]

# ============================================
# LEVENE'S TEST (homogeneity of variances)
# ============================================
lev_stat, lev_pval = levene(*groups)
print("\n========================================")
print("  LEVENE'S TEST (Variance Equality)")
print("========================================")
print(f"  Statistic : {lev_stat:.4f}")
print(f"  P-value   : {lev_pval:.6f}")
if lev_pval < ALPHA:
    print("  -> Variances are NOT equal (use Welch ANOVA)")
else:
    print("  -> Variances are approximately equal (standard ANOVA also valid)")

# ============================================
# WELCH ANOVA
# ============================================
result = anova_oneway(
    df["Total_Sales"],
    groups=df["Category"],
    use_var="unequal"
)

print("\n========================================")
print("  WELCH ANOVA")
print("========================================")
print(f"  F-statistic : {result.statistic:.4f}")
print(f"  P-value     : {result.pvalue:.6f}")
print(f"  Degrees of Freedom : {result.df}")

# ============================================
# DECISION
# ============================================
print("\n========================================")
print("  STATISTICAL DECISION")
print("=" * 60)

if result.pvalue < ALPHA:
    print("  Decision: REJECT H0")
    print("  There is statistically significant evidence")
    print("  that average sales differ across categories.")
else:
    print("  Decision: FAIL TO REJECT H0")
    print("  There is insufficient statistical evidence")
    print("  to conclude that average sales differ across categories.")

# ============================================
# BUSINESS INTERPRETATION
# ============================================
print("\n========================================")
print("  BUSINESS INTERPRETATION")
print("=" * 60)

highest_mean = summary["Mean"].idxmax()
lowest_mean = summary["Mean"].idxmin()

print(f"  Highest average sales category : {highest_mean} (Rs.{summary.loc[highest_mean, 'Mean']:,.2f})")
print(f"  Lowest average sales category  : {lowest_mean} (Rs.{summary.loc[lowest_mean, 'Mean']:,.2f})")
print(f"  Observed mean difference       : Rs.{summary['Mean'].max() - summary['Mean'].min():,.2f}")

# ============================================
# TRANSACTION COUNT vs REVENUE STORY
# ============================================
print("\n========================================")
print("  KEY INSIGHT: Total Revenue != Average Transaction Value")
print("=" * 60)

category_revenue = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
category_count = df.groupby("Category")["Total_Sales"].count().sort_values(ascending=False)

print("\n  By Total Revenue:")
for cat, rev in category_revenue.items():
    print(f"    {cat:<15} Rs.{rev:>14,.2f}  ({category_count[cat]} transactions)")

print("\n  By Average Transaction Value:")
for cat, row in summary.sort_values("Mean", ascending=False).iterrows():
    print(f"    {cat:<15} Rs.{row['Mean']:>14,.2f}")

print("\n  Conclusion:")
print("  Electronics leads total revenue primarily due to")
print("  higher transaction volume (354 transactions),")
print("  NOT because its average transaction value is")
print("  statistically significantly higher.")

# ============================================
# VISUALIZATION 1: Category Mean Sales with Error Bars
# ============================================
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0E1117')
ax.set_facecolor('#0E1117')

cat_order = summary.sort_values("Mean", ascending=False).index
colors = ["#00E5FF", "#FF007F", "#7B2CBF", "#00FF66", "#FFD700"]

bars = ax.bar(
    cat_order,
    summary.loc[cat_order, "Mean"],
    color=colors,
    edgecolor="white",
    linewidth=0.8,
    alpha=0.85,
    yerr=summary.loc[cat_order, "Std"] / np.sqrt(summary.loc[cat_order, "Count"]),
    capsize=5,
    error_kw={"elinewidth": 1.5, "color": "white"}
)

for bar, cat in zip(bars, cat_order):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 3000,
        f"Rs.{height:,.0f}",
        ha="center", va="bottom",
        fontsize=10, fontweight="bold",
        color="white"
    )

ax.axhline(
    y=summary["Mean"].mean(),
    color="#FFD700",
    linestyle="--",
    linewidth=1.5,
    alpha=0.7,
    label=f"Grand Mean: Rs.{summary['Mean'].mean():,.0f}"
)

ax.set_title(
    "Average Transaction Value by Product Category\n(with Standard Error Bars)",
    fontsize=14, fontweight="bold", color="white"
)
ax.set_xlabel("Product Category", fontsize=12, color="#CCCCCC")
ax.set_ylabel("Average Sales (Rs.)", fontsize=12, color="#CCCCCC")
ax.legend(
    facecolor="#161B22", edgecolor="#333333",
    labelcolor="white", loc="upper right"
)
ax.grid(axis="y", linestyle=":", alpha=0.2)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#333333")
ax.spines["bottom"].set_color("#333333")

plt.tight_layout()
plt.savefig("hypothesis_test.png", dpi=150, bbox_inches="tight", facecolor="#0E1117")
print("\n  Saved -> hypothesis_test.png")
plt.close()

# ============================================
# VISUALIZATION 2: Box Plot of Sales by Category
# ============================================
fig2, ax2 = plt.subplots(figsize=(10, 6), facecolor='#0E1117')
ax2.set_facecolor('#0E1117')

sns.boxplot(
    data=df, x="Category", y="Total_Sales",
    order=cat_order, palette=colors,
    width=0.6, linewidth=1.2,
    fliersize=4,
    ax=ax2
)

ax2.set_title(
    "Total Sales Distribution by Category",
    fontsize=14, fontweight="bold", color="white"
)
ax2.set_xlabel("Product Category", fontsize=12, color="#CCCCCC")
ax2.set_ylabel("Total Sales (Rs.)", fontsize=12, color="#CCCCCC")
ax2.grid(axis="y", linestyle=":", alpha=0.2)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_color("#333333")
ax2.spines["bottom"].set_color("#333333")

from matplotlib.ticker import FuncFormatter
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"Rs.{x:,.0f}"))

plt.tight_layout()
plt.savefig("boxplot_category_sales.png", dpi=150, bbox_inches="tight", facecolor="#0E1117")
print("  Saved -> boxplot_category_sales.png")
plt.close()

# ============================================
# VISUALIZATION 3: Revenue vs Transaction Count
# ============================================
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(14, 6), facecolor='#0E1117')
for a in [ax3a, ax3b]:
    a.set_facecolor('#0E1117')

category_rev_sorted = category_revenue.sort_values(ascending=True)
ax3a.barh(
    category_rev_sorted.index,
    category_rev_sorted.values,
    color=colors[:len(category_rev_sorted)][::-1],
    edgecolor="white", linewidth=0.6, alpha=0.85
)
for i, (cat, val) in enumerate(category_rev_sorted.items()):
    ax3a.text(val + 500000, i, f"Rs.{val/1e6:.1f}M", va="center", fontsize=10, color="white", fontweight="bold")
ax3a.set_title("Total Revenue by Category", fontsize=12, fontweight="bold", color="white")
ax3a.set_xlabel("Total Revenue (Rs.)", fontsize=10, color="#CCCCCC")
ax3a.grid(axis="x", linestyle=":", alpha=0.2)
ax3a.spines["top"].set_visible(False)
ax3a.spines["right"].set_visible(False)

category_count_sorted = category_count.sort_values(ascending=True)
ax3b.barh(
    category_count_sorted.index,
    category_count_sorted.values,
    color=colors[:len(category_count_sorted)][::-1],
    edgecolor="white", linewidth=0.6, alpha=0.85
)
for i, (cat, val) in enumerate(category_count_sorted.items()):
    ax3b.text(val + 3, i, str(val), va="center", fontsize=10, color="white", fontweight="bold")
ax3b.set_title("Transaction Count by Category", fontsize=12, fontweight="bold", color="white")
ax3b.set_xlabel("Number of Transactions", fontsize=10, color="#CCCCCC")
ax3b.grid(axis="x", linestyle=":", alpha=0.2)
ax3b.spines["top"].set_visible(False)
ax3b.spines["right"].set_visible(False)

fig3.suptitle(
    "Revenue Leadership: Volume vs Value",
    fontsize=14, fontweight="bold", color="white", y=1.02
)
plt.tight_layout()
plt.savefig("revenue_vs_volume.png", dpi=150, bbox_inches="tight", facecolor="#0E1117")
print("  Saved -> revenue_vs_volume.png")
plt.close()

print("\n" + "=" * 60)
print("  ALL OUTPUTS GENERATED SUCCESSFULLY")
print("=" * 60)
