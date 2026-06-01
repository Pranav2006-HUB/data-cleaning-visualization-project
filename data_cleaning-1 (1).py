"""
Data Cleaning & Visualization Project
======================================
Thiranex Skill Development - Project 1
Tools: Pandas, Matplotlib, Seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── CREATE OUTPUT FOLDER ───────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)

# ── RAW DATASET (intentionally dirty) ─────────────────────────────────────
raw_data = {
    "id":     [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "name":   ["Alice","Bob","Charlie","Alice","Diana","Eve","Frank","Grace",
                "Hank","Iris","Jack","Karen","Leo","Mia","Nathan","Olivia",
                "Paul","Quinn","Rachel","Sam"],
    "age":    [28, None, 35, 28, 245, 31, 29, 52, 44, 26,
               38, None, 33, 27, 41, 36, 29, 48, 32, None],
    "salary": [52000, 61000, None, 52000, 48000, 75000, 43000, 980000,
               67000, 55000, 82000, 59000, 71000, 47000, 93000, None,
               54000, 105000, 66000, 77000],
    "dept":   ["Engineering","Marketing","Engineering","Engineering","HR",
               "Engineering","Marketing","Finance","Finance","HR",
               "Engineering","Marketing","Finance","HR","Engineering",
               "Marketing","HR","Finance","Engineering","Finance"],
    "city":   ["New York","Chicago","New York","New York","Austin",
               "Seattle","Chicago","New York","Boston","Austin",
               "Seattle","Miami","Boston","Austin","New York",
               "Chicago","Miami","Boston","Seattle","New York"],
    "score":  [87, 72, 91, 87, 65, 95, None, 78, 83, 70,
               89, 76, 88, None, 92, 81, 69, 85, 90, 79],
}

df = pd.DataFrame(raw_data)

print("=" * 50)
print("STEP 0: Raw Data Overview")
print("=" * 50)
print(df.to_string(index=False))
print(f"\nShape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")


# ── STEP 1: REMOVE DUPLICATES ──────────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 1: Removing Duplicates")
print("=" * 50)

before = len(df)
df.drop_duplicates(subset=["name", "age", "salary", "dept"], inplace=True)
df.reset_index(drop=True, inplace=True)
after = len(df)

print(f"Rows before: {before}")
print(f"Rows after:  {after}")
print(f"Duplicates removed: {before - after}")


# ── STEP 2: FIX OUTLIERS ───────────────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 2: Fixing Outliers")
print("=" * 50)

# Age outlier: anyone over 100 is invalid
age_outliers = df[df["age"] > 100]
print(f"Age outliers found:\n{age_outliers[['name','age']]}")
median_age = df.loc[df["age"] <= 100, "age"].median()
df.loc[df["age"] > 100, "age"] = median_age
print(f"Fixed age outliers → replaced with median: {median_age}")

# Salary outlier: IQR method
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
salary_upper = Q3 + 1.5 * IQR
salary_outliers = df[df["salary"] > salary_upper]
print(f"\nSalary outliers (>{salary_upper:,.0f}):\n{salary_outliers[['name','salary']]}")
median_salary = df.loc[df["salary"] <= salary_upper, "salary"].median()
df.loc[df["salary"] > salary_upper, "salary"] = median_salary
print(f"Fixed salary outliers → replaced with median: {median_salary:,.0f}")


# ── STEP 3: IMPUTE MISSING VALUES ─────────────────────────────────────────
print("\n" + "=" * 50)
print("STEP 3: Imputing Missing Values")
print("=" * 50)

mean_age    = round(df["age"].mean())
mean_salary = round(df["salary"].mean())
mean_score  = round(df["score"].mean())

print(f"Filling missing 'age'    with mean: {mean_age}")
print(f"Filling missing 'salary' with mean: {mean_salary:,}")
print(f"Filling missing 'score'  with mean: {mean_score}")

df["age"].fillna(mean_age, inplace=True)
df["salary"].fillna(mean_salary, inplace=True)
df["score"].fillna(mean_score, inplace=True)

print(f"\nMissing values after imputation:\n{df.isnull().sum()}")


# ── CLEAN DATA SUMMARY ─────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("CLEAN DATASET SUMMARY")
print("=" * 50)
print(df.describe().round(2).to_string())


# ── STEP 4: VISUALIZATIONS ────────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="Set2")
COLORS = {"Engineering": "#6EE7B7", "Marketing": "#93C5FD",
          "HR": "#FCA5A5", "Finance": "#FCD34D"}

dept_stats = df.groupby("dept").agg(
    avg_salary=("salary", "mean"),
    avg_score=("score", "mean"),
    count=("name", "count")
).reset_index()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Data Cleaning & Visualization Project\nEmployee Dataset Insights",
             fontsize=16, fontweight="bold", y=1.01)

# Chart 1: Avg Salary by Department
ax1 = axes[0, 0]
bars = ax1.bar(dept_stats["dept"], dept_stats["avg_salary"],
               color=[COLORS[d] for d in dept_stats["dept"]], edgecolor="white", linewidth=0.5)
ax1.set_title("Average Salary by Department", fontweight="bold")
ax1.set_xlabel("Department")
ax1.set_ylabel("Avg Salary ($)")
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f"${bar.get_height():,.0f}", ha="center", va="bottom", fontsize=9)

# Chart 2: Avg Performance Score by Department
ax2 = axes[0, 1]
hbars = ax2.barh(dept_stats["dept"], dept_stats["avg_score"],
                  color=[COLORS[d] for d in dept_stats["dept"]], edgecolor="white", linewidth=0.5)
ax2.set_title("Avg Performance Score by Department", fontweight="bold")
ax2.set_xlabel("Avg Score")
ax2.set_xlim(0, 100)
for bar in hbars:
    ax2.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             f"{bar.get_width():.0f}", va="center", fontsize=9)

# Chart 3: City Distribution Pie
ax3 = axes[1, 0]
city_counts = df["city"].value_counts()
pie_colors = ["#6EE7B7","#93C5FD","#FCA5A5","#FCD34D","#C4B5FD","#F9A8D4"]
ax3.pie(city_counts.values, labels=city_counts.index, autopct="%1.0f%%",
        colors=pie_colors[:len(city_counts)], startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1})
ax3.set_title("Employee Distribution by City", fontweight="bold")

# Chart 4: Salary vs Score Scatter
ax4 = axes[1, 1]
for dept, grp in df.groupby("dept"):
    ax4.scatter(grp["salary"], grp["score"], label=dept,
                color=COLORS[dept], s=80, alpha=0.85, edgecolors="white", linewidths=0.5)
ax4.set_title("Salary vs Performance Score", fontweight="bold")
ax4.set_xlabel("Salary ($)")
ax4.set_ylabel("Performance Score")
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
ax4.legend(title="Department", fontsize=9)

plt.tight_layout()
plt.savefig("outputs/dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✅ Dashboard saved to outputs/dashboard.png")


# ── SAVE CLEAN CSV ─────────────────────────────────────────────────────────
df.to_csv("outputs/clean_data.csv", index=False)
print("✅ Clean dataset saved to outputs/clean_data.csv")
print("\n🎉 Project complete!")
