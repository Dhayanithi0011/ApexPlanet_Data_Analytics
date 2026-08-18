# 📊 ApexPlanet Data Analytics Internship Portfolio

<p align="center">

# 🚀 Data → Insights → Decisions

### End-to-End Data Analytics Internship Portfolio

**Dhayanithi M.**

B.Tech — Artificial Intelligence & Data Science

</p>

---

## About Me

I am a B.Tech student specializing in **Artificial Intelligence and Data Science**, with a strong interest in **Data Analytics, Business Intelligence, Machine Learning, and Data-Driven Decision Making**.

This repository documents my complete **ApexPlanet Data Analytics Internship journey**, covering the end-to-end analytics lifecycle — from data preparation and exploratory analysis to deep-dive analysis, interactive dashboard development, statistical validation, and business storytelling.

---

# 🎯 Internship Objective

The primary objective of this internship was to develop practical experience in solving business problems using data.

Throughout the internship, I worked through the following analytics workflow:

```text
Raw Data
   ↓
Data Preparation
   ↓
Exploratory Data Analysis
   ↓
Deep-Dive Analysis
   ↓
Interactive Dashboard
   ↓
Statistical Validation
   ↓
Business Storytelling
   ↓
Recommendations & Decisions
```

---

# 🗂️ Internship Journey

## 🔹 Task 1 — Data Preparation & Wrangling

### Objective

Prepare and understand the dataset for further analysis by performing data-wrangling and preprocessing activities.

### Key Work

* Loaded and inspected the dataset
* Examined data structure and attributes
* Performed data preparation and cleaning
* Worked with relevant data types and columns
* Prepared the dataset for downstream analytics

### Deliverable

`task1_data_wrangling.py`

📁 **Repository Location:** `Task 1/`

🔗 **[View Task 1 — Data Preparation & Wrangling](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%201)**

---

## 🔹 Task 2 — Exploratory Data Analysis

### Objective

Explore the dataset to identify trends, patterns, relationships, and important business insights.

### Key Work

* Performed exploratory data analysis
* Investigated sales and customer patterns
* Analyzed categorical and numerical variables
* Created visualizations to understand business trends
* Identified important observations for deeper analysis

### Deliverable

`Apex Planet Task 2.ipynb`

📁 **Repository Location:** `Task 2/`

🔗 **[View Task 2 — Exploratory Data Analysis](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%202)**

---

## 🔹 Task 3 — Deep-Dive Analysis & Interactive Dashboard

### Objective

Perform deeper analysis of important business areas and convert analytical findings into an interactive dashboard.

### Key Work

* Defined and analyzed key business KPIs
* Performed category, customer, product and sales analysis
* Investigated important business patterns
* Developed an interactive Power BI dashboard
* Created visual reports for business interpretation

### Deliverables

* `Dashboard.png`
* `Task3_Interactive_Dashboard_Report.pdf`
* `task 3.pbix`

📁 **Repository Location:** `Task 3/`

🔗 **[View Task 3 — Deep-Dive Analysis & Interactive Dashboard](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%203)**

---

## 🔹 Task 4 — Data Storytelling & Statistical Validation

### Objective

Transform the findings from the previous tasks into a cohesive business story and statistically validate an important business observation.

### Business Question

> **Do average sales values differ significantly across product categories?**

### Statistical Method

**Welch's ANOVA**

Welch's ANOVA was selected because the analysis compares average sales across five independent product categories while providing robustness when group variances may differ.

### Hypotheses

**Null Hypothesis (H₀):**

All product categories have the same mean transaction value.

**Alternative Hypothesis (H₁):**

At least one product category has a different mean transaction value.

### Significance Level

```text
α = 0.05
```

### Statistical Results

| Metric             |            Result |
| ------------------ | ----------------: |
| F-statistic        |            0.7842 |
| p-value            |            0.5359 |
| Significance Level |              0.05 |
| Decision           | Fail to Reject H₀ |

### Interpretation

Since:

```text
p-value > α

0.5359 > 0.05
```

there is insufficient statistical evidence to conclude that average transaction values differ significantly across product categories.

### Key Business Insight

Although the observed average transaction values differ across categories, the statistical test indicates that these differences are **not statistically significant at the 5% significance level**.

The analysis also highlighted that **Electronics' revenue leadership is primarily associated with its higher transaction volume rather than a statistically higher average transaction value**.

### Business Recommendations

1. Protect and grow Electronics transaction volume.
2. Investigate the factors driving the higher transaction count.
3. Avoid making strategic decisions based solely on observed average differences.
4. Collect larger datasets over longer periods for stronger statistical evidence.
5. Continue using statistical validation before making major business decisions.

### Deliverables

* `hypothesis_testing.py`
* `statistical_results.csv`
* `hypothesis_test.png`
* `boxplot_category_sales.png`
* `revenue_vs_volume.png`
* `data_story.md`
* `presentation.pptx`

📁 **Repository Location:** `Task 4/`

🔗 **[View Task 4 — Data Storytelling & Statistical Validation](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%204)**

# 🗂️ Internship Journey

| Task       | Focus Area                                 | GitHub                                                                                         |
| ---------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Task 1** | Data Preparation & Wrangling               | [View Project](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%201) |
| **Task 2** | Exploratory Data Analysis                  | [View Project](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%202) |
| **Task 3** | Deep-Dive Analysis & Interactive Dashboard | [View Project](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%203) |
| **Task 4** | Data Storytelling & Statistical Validation | [View Project](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics/tree/main/Task%204) |

> **Complete Internship Repository:** [ApexPlanet Data Analytics](https://github.com/Dhayanithi0011/ApexPlanet_Data_Analytics)

# 📈 Key Business Insights

The internship demonstrated how descriptive analytics and statistical validation can provide different perspectives on the same business problem.

### 1. Revenue Performance

Identified the major revenue-generating categories, products, customers, and business segments through exploratory and deep-dive analysis.

### 2. Transaction Volume Matters

The analysis demonstrated that a category generating high total revenue may be doing so because of a higher number of transactions rather than a statistically higher transaction value.

### 3. Descriptive Differences Are Not Automatically Significant

Observed differences between category averages should not automatically be treated as meaningful business differences.

Statistical testing is required before drawing strong conclusions.

### 4. Data Should Support Decisions

The final objective of analytics is not simply to produce charts, but to transform data into insights that can support better business decisions.

---

# 🧪 Statistical Validation Summary

```text
Business Observation
        ↓
Formulate Hypothesis
        ↓
Select Statistical Test
        ↓
Welch's ANOVA
        ↓
Calculate F-statistic & p-value
        ↓
Compare p-value with α = 0.05
        ↓
Interpret Statistical Evidence
        ↓
Translate Result into Business Action
```

### Final Statistical Conclusion

> The analysis did not provide sufficient statistical evidence to conclude that average transaction values differ significantly across product categories.

---

# 🛠️ Technical Skills Demonstrated

### Programming & Data Analysis

- Python
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn
- Plotly
- Power BI

### Statistical Analysis

- Hypothesis Testing
- Welch's ANOVA
- p-value interpretation
- Significance testing
- Descriptive statistics

### Development & Collaboration

- VS Code
- Jupyter Notebook
- Git
- GitHub

### Business Analytics

- KPI development
- Deep-dive analysis
- Dashboard development
- Data storytelling
- Business recommendations

---

# 📚 Key Learnings

Throughout this internship, I strengthened my ability to:

- Work with real-world datasets
- Prepare and clean data for analysis
- Perform exploratory data analysis
- Identify meaningful business patterns
- Develop and interpret KPIs
- Build interactive dashboards
- Perform statistical hypothesis testing
- Interpret p-values and statistical results
- Convert analytical findings into business insights
- Communicate data through storytelling
- Present findings to a business audience
- Organize analytical projects using Git and GitHub

---

# 🔄 End-to-End Analytics Workflow

This internship helped me understand the complete journey of a data analyst:

```text
          DATA
           │
           ▼
   ┌─────────────────┐
   │ Data Preparation│
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Data Exploration │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Deep-Dive        │
   │ Analysis         │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Dashboard        │
   │ Development      │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Statistical      │
   │ Validation       │
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Data Storytelling│
   └────────┬────────┘
            ▼
   ┌─────────────────┐
   │ Business         │
   │ Recommendations  │
   └─────────────────┘
```

---

# 📂 Project Structure

```text
ApexPlanet_Data_Analytics/
│
├── README.md
│
├── Task 1/
│   └── task1_data_wrangling.py
│
├── Task 2/
│   └── Apex Planet Task 2.ipynb
│
├── Task 3/
│   ├── Dashboard.png
│   ├── Task3_Interactive_Dashboard_Report.pdf
│   └── task 3.pbix
│
└── Task 4/
    ├── README.md
    ├── data_story.md
    ├── hypothesis_testing.py
    ├── statistical_results.csv
    ├── hypothesis_test.png
    ├── boxplot_category_sales.png
    ├── revenue_vs_volume.png
    └── presentation.pptx
```

---

# 🚀 Future Improvements

The project can be further extended by:

- Building automated ETL pipelines
- Integrating larger and continuously updated datasets
- Implementing sales forecasting
- Developing customer lifetime value models
- Applying customer churn prediction
- Building real-time dashboards
- Adding automated business reporting
- Deploying analytics applications to the cloud
- Applying machine learning for predictive decision-making

---

# 🎓 Internship Reflection

This internship provided practical exposure to the complete data analytics lifecycle.

The biggest takeaway was understanding that **data analysis is not just about finding patterns**.

A strong data analyst must be able to:

```text
Understand the Data
       ↓
Find the Pattern
       ↓
Question the Pattern
       ↓
Validate the Pattern
       ↓
Explain the Pattern
       ↓
Recommend an Action
```

The combination of **data analysis, visualization, statistical reasoning, and business storytelling** helped me develop a more structured approach to solving data-driven problems.

---

# Acknowledgement

I would like to thank **ApexPlanet** for providing this internship opportunity and hands-on exposure to practical data analytics workflows.

This experience has helped me strengthen both my technical and business-oriented analytical skills.

---

# 📌 Portfolio Repository

**ApexPlanet Data Analytics Internship**

**Author:** Dhayanithi M.

**Domain:** Data Analytics / Data Science

**Focus:** Data Preparation • EDA • Business Intelligence • Statistical Analysis • Data Storytelling

---

<p align="center">

### 🚀 Turning Data Into Insights. Turning Insights Into Decisions.

</p>