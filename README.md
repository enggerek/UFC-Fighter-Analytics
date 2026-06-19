# UFC Fighter Analytics Dashboard

I built this dashboard to compare top UFC fighters from 9 countries. Win rates, finishing styles, age trends and more. Data was manually collected from ESPN.

## !!Notes!!

**About the dataset:** This is not a comprehensive analysis of all UFC fighters. The dataset is a curated sample. I picked standout star fighters from the 9 most active countries in the UFC. It's meant to compare notable names against each other, not to represent the full roster.

**Data freshness:** This is a static dataset, not a live one. The stats were collected at a specific point in time and are not automatically updated, so some figures may no longer reflect current records.


## Overview

This is a Power BI dashboard project analyzing the performance of top UFC fighters across 9 countries. All data was collected manually. Which honestly made me appreciate the dataset a lot more.

The goal was to find patterns: which countries produce the most dominant fighters, who finishes fights the most, and whether age has any effect on win rate.


## Dashboard Visuals

- **KPI Cards** - Total fighters, average win rate, most dominant country, top finisher
- **Avg Win Rate by Country** - Horizontal bar chart ranked highest to lowest
- **TKO vs Submission Wins** - Stacked bar chart for top 10 fighters
- **Age vs Win Rate**  Scatter plot showing the relationship between age and performance
- **Top 10 Finishing Rates** - Horizontal bar chart of the most clinical finishers
- **Country Slicer** - Filter all visuals by country interactively

---

## Dataset

**File:** `ufceng_revised.csv`  
**Rows:** 90 fighters  
**Source:** Manually collected from ESPN  
**Countries:** Australia, Brazil, Canada, China, England, France, Mexico, Russia, USA

| Column | Description |
|--------|-------------|
| FIGHTER | Fighter name |
| COUNTRY | Country of origin |
| TKO_WINS | Total TKO/KO wins |
| TKO_LOSSES | Total TKO/KO losses |
| SUB_WINS | Total submission wins |
| SUB_LOSSES | Total submission losses |
| PRIMARY_STYLE | Main fighting style |
| WIN_RATE | Win percentage |
| TOTAL_FIGHTS | Total professional fights |
| TOTAL_WINS | Total wins |
| TOTAL_LOSSES | Total losses |
| DRAW | Total draws |
| AGE | Fighter's age |
| FINISHING_RATE | Percentage of wins by finish |


## Tools Used

- **Power BI Desktop** — Dashboard design and visualization


