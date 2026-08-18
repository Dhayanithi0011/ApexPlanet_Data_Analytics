# Task 4: Data Storytelling & Statistical Validation

## Overview

Task 4 completes the ApexPlanet internship project by synthesizing findings from Tasks 1-3 into a cohesive business narrative and validating one key finding through rigorous statistical testing.

## Objective

Combine descriptive analysis insights with statistical validation to answer: "Why does this matter, and what should the business do?"

## Methodology

### Data Source
- **Dataset:** ApexPlanet Sales Dataset (1,000 transactions, 12 columns)
- **Period:** January 2025 - December 2025
- **Categories:** Electronics, Education, Grocery, Furniture, Fashion

### Business Question
"Do average sales values differ significantly across product categories?"

### Statistical Test
**Welch's ANOVA (Analysis of Variance)**

Chosen because:
- Comparing means across 5 independent groups (categories)
- Does not assume equal variances (more robust than standard ANOVA)
- Appropriate for real-world business data with unequal group sizes

### Hypotheses
- **H0:** u_Education = u_Electronics = u_Fashion = u_Furniture = u_Grocery (all category means are equal)
- **H1:** At least one category has a different mean sales value
- **Significance Level:** a = 0.05

## Results

### Descriptive Statistics
| Category | Count | Mean (Rs.) | Median (Rs.) | Std Dev |
|----------|-------|------------|--------------|---------|
| Grocery | 153 | 145,305 | 109,238 | 114,918 |
| Electronics | 354 | 143,442 | 114,521 | 117,602 |
| Education | 178 | 140,627 | 108,469 | 116,853 |
| Furniture | 159 | 135,356 | 99,839 | 111,049 |
| Fashion | 156 | 127,153 | 101,570 | 105,150 |

### Levene's Test (Variance Equality)
- **Statistic:** 0.9787
- **P-value:** 0.4182
- **Conclusion:** Variances are approximately equal

### Welch ANOVA Results
| Metric | Value |
|--------|-------|
| F-statistic | 0.7842 |
| P-value | 0.5359 |
| Degrees of Freedom | (4.0, 429.56) |

### Statistical Decision
**p-value (0.5359) > a (0.05) --> FAIL TO REJECT H0**

There is insufficient statistical evidence to conclude that average transaction values differ across product categories.

## Key Insight

**Electronics' revenue leadership is driven by transaction volume, not statistically higher average transaction values.**

- Electronics: 354 transactions (35.4% of all orders) generating Rs.50.78M (36.4% of total revenue)
- Average transaction value: Rs.143,442 -- not statistically different from other categories
- Revenue leadership primarily associated with receiving more transactions

## Business Recommendations

1. **Protect Electronics volume** -- maintain and grow transaction count
2. **Investigate volume drivers** -- understand why Electronics attracts more transactions
3. **Avoid over-interpreting averages** -- observed differences are not statistically significant
4. **Collect more data** -- larger datasets could provide stronger evidence
5. **Continue statistical validation** -- use hypothesis testing before major decisions

## Project Files

| File | Description |
|------|-------------|
| `hypothesis_testing.py` | Main statistical analysis script (Welch ANOVA) |
| `statistical_results.csv` | Descriptive statistics by category |
| `hypothesis_test.png` | Category mean sales bar chart with error bars |
| `boxplot_category_sales.png` | Box plot of sales distribution by category |
| `revenue_vs_volume.png` | Revenue vs transaction count comparison |
| `data_story.md` | Complete data storytelling narrative |
| `presentation.pptx` | 10-slide business presentation |
| `README.md` | This file |

## How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scipy statsmodels openpyxl

# Run hypothesis testing
cd Task-4
python hypothesis_testing.py
```

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels
- openpyxl
- python-pptx (for presentation generation)
