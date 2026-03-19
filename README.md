# Carbon Emissions Data Analysis Project

## Overview

This project performs exploratory data analysis (EDA) and statistical analysis on global carbon emissions data using Python. The dataset contains emissions information categorized by country, sector, and date.

The program automatically assigns a **country**, **sector**, and **year** based on a predefined seed, then computes statistics, builds aggregated matrices, generates plots, and saves results to disk.

---

## Objectives

- Load and clean real-world emissions data
- Perform statistical analysis on a filtered subset
- Identify key patterns (max, min, anomalies)
- Aggregate data into structured numerical formats (matrix)
- Visualize trends using plots
- Save outputs for reporting

---

## Technologies Used

- Python 3
- pandas
- numpy
- matplotlib

---

## Project Structure

carbon-analysis/
│
├── data/
│   └── carbonmonitor-global_datas_2025-04-21.csv
│
├── outputs/
│   ├── analysis.txt
│   ├── figures/
│   │   ├── monthly_trend.png
│   │   ├── sector_bar.png
│   │   └── time_series.png
│   └── results_seed_811.txt
│
├── src/
│   └── main.py
│
├── README.md
└── requirements.txt

---

## How It Works

### 1. Seed-Based Assignment

A fixed seed (`seed = 811`) is used to deterministically select:

- A country
- A sector
- A year

This ensures reproducibility.

---

### 2. Data Loading and Cleaning

The function `load_and_clean()`:

- Loads the CSV file using pandas
- Removes unnecessary columns
- Converts the `date` column to datetime format
- Extracts `year` and `month`
- Displays:
  - Head of dataset
  - Data info
  - Statistical summary of values

---

### 3. Subset Analysis

The function `analysis_part(df)` filters data by:

- Selected country
- Selected year
- Selected sector

It then computes:

- Mean (average emissions)
- Standard deviation
- Maximum value and corresponding date
- Minimum value and corresponding date
- "Low emission days" (values below mean - std)

---

### 4. Matrix Construction

The function `build_matrix(df)` creates a **12 × 6 matrix**:

- Rows represent months (1–12)
- Columns represent sectors
- Each cell contains the average emission value for that month-sector

It also computes:

- Column means (average per sector)
- Row sums (total per month)

From this, the program identifies:

- Sector with the highest average emissions
- Month with the highest total emissions
- Top 3 sectors by average emissions

---

### 5. Visualization

The function `plot_all(...)` generates three plots:

1. **Time Series Plot**
   - Emissions over time for the selected subset
   - Highlights maximum and minimum points

2. **Bar Chart**
   - Average emissions per sector

3. **Monthly Trend Plot**
   - Total emissions per month

All plots are saved in:

outputs/figures/

---

### 6. Saving Results

The function `save_results(...)` writes key results into:

outputs/results_seed_811.txt

Contents include:

- Seed and assigned parameters
- Mean and standard deviation
- Maximum and minimum values
- Sector with highest emissions
- Month with highest emissions

---

## How to Run

1. Install dependencies:

pip install pandas numpy matplotlib

2. Make sure the dataset exists at:

data/carbonmonitor-global_datas_2025-04-21.csv

3. Run the script:

python src/main.py

---

## Example Output

Console output includes:

- Dataset preview
- Statistical summaries
- Identified max/min values
- Sector and month insights

Generated files:

- time_series.png
- sector_bar.png
- monthly_trend.png
- results_seed_811.txt

---

## Key Concepts Demonstrated

- Data cleaning and preprocessing
- Time series analysis
- Statistical measures (mean, standard deviation)
- NumPy matrix operations
- Data aggregation
- Data visualization
- Reproducibility using seeds

---

## Possible Improvements

- Add command-line arguments instead of fixed seed
- Handle missing data more robustly
- Add interactive visualizations (e.g., Plotly)
- Normalize emissions for better comparisons
- Extend analysis across multiple countries/years

---

## Author

Alejandro Patino Rivera

---

## License

This project is for educational purposes.
