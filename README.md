# 📊 Data Cleaning & Visualization Project

**Thiranex Skill Development & Future Tech — Project 1**

## 📌 Overview
This project demonstrates data preprocessing, cleaning, and visualization using Python. It works on a raw employee dataset containing missing values, outliers, and duplicate records — then generates an insightful visual dashboard.

---

## 🛠 Tech Stack
| Library | Purpose |
|---|---|
| `pandas` | Data manipulation & cleaning |
| `numpy` | Numerical operations |
| `matplotlib` | Base plotting |
| `seaborn` | Statistical visualizations |

---

## 🔧 Cleaning Pipeline

### Step 1 — Remove Duplicates
- Detects exact duplicate rows using key columns
- Removes duplicates and resets the index

### Step 2 — Fix Outliers
- **Age**: Values > 100 replaced with column median
- **Salary**: IQR method — values above Q3 + 1.5×IQR replaced with median

### Step 3 — Impute Missing Values
- `age`, `salary`, `score` — filled with **column mean**

---

## 📈 Visualizations

The dashboard (`outputs/dashboard.png`) contains 4 charts:

1. **Bar Chart** — Average Salary by Department
2. **Horizontal Bar** — Average Performance Score by Department
3. **Pie Chart** — Employee Distribution by City
4. **Scatter Plot** — Salary vs Performance Score (colored by department)

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/data-cleaning-visualization-project.git
cd data-cleaning-visualization-project

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Run the script
python data_cleaning.py
```

**Outputs generated:**
- `outputs/dashboard.png` — Visual dashboard
- `outputs/clean_data.csv` — Cleaned dataset

---

## 📂 Project Structure
```
data-cleaning-visualization-project/
│
├── data_cleaning.py       ← Main script
├── README.md              ← This file
└── outputs/
    ├── dashboard.png      ← Generated charts
    └── clean_data.csv     ← Cleaned dataset
```

---

## 🎯 Expected Outcome
- Learn data preprocessing techniques
- Handle real-world dirty data issues
- Build visual dashboards to communicate insights

---

*Submitted for Thiranex Project 1 — Data Cleaning & Visualization*
