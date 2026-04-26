# Data Analysis Project Report: Global Air Pollution 

**Student Name:** [Insert Your Name Here]  
**Student ID:** [Insert Your ID Here]  
**Dataset Source:** [Kaggle - Global Air Pollution Dataset](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)

---

## 1. Introduction & Problem Definition

Air pollution is a critical global health crisis, responsible for millions of premature deaths annually. This project aims to conduct a data-driven investigation into global air pollution using Python. The objective is to apply data cleaning, feature engineering, and statistical analysis to uncover meaningful patterns across various cities and countries worldwide.

**Analytical Questions Addressed:**
1. Are there significant geographical variations in overall air quality, and which countries experience the most severe pollution levels?
2. Which specific pollutant (CO, Ozone, NO2, or PM2.5) most strongly drives the overall Air Quality Index (AQI) globally?
3. How do the levels of different pollutants correlate with each other, and what characterizes the makeup of "Hazardous" air quality zones versus "Good" zones?

---

## 2. Data Understanding

The dataset originally contained **23,463 rows and 12 columns**, well exceeding the minimum requirement of 1,000 rows and 6 columns. 
The variables included geographical text data (`Country`, `City`) and numerical pollution metrics (`AQI Value`, `CO AQI Value`, `Ozone AQI Value`, `NO2 AQI Value`, `PM2.5 AQI Value`) alongside their string-based categorical rankings (e.g., "Moderate", "Hazardous").

*   **Missing Values:** The dataset was highly complete. Only `Country` had 427 missing values (~1.8%), and `City` had 1 missing value.
*   **Summary Statistics:** The mean global AQI was approximately 72 (Moderate), but the distribution was heavily right-skewed with a maximum reaching 500 (Hazardous limit). The standard deviation for PM2.5 was notably massive (54.79), indicating extreme volatility in particulate matter compared to other stable gases like CO.

---

## 3. Data Cleaning Methodology

To ensure analytical integrity, three key cleaning steps were executed:
1.  **Handling Missing Values:** Dropped 428 rows missing `Country` or `City` data. *Justification: Imputing fake geometric identifiers would artificially distort spatial sub-grouping later in the analysis.*
2.  **Removing Duplicates:** Dropped all perfectly duplicated rows. *Justification: Exact duplicate sensor readings falsely inflate density distributions and skew summary statistics.*
3.  **Standardizing Column Names:** Converted all columns to lowercase `snake_case` (e.g., `PM2.5 AQI Category` $\rightarrow$ `pm2.5_aqi_category`). *Justification: Ensures stable, error-free programmatic access throughout the Python workflow.*

*(Post-cleaning, the dataset shape was finalized at 23,035 rows).*

---

## 4. Feature Engineering

Two derived columns were engineered to enable deeper mathematical and categorical analysis:
1.  **`primary_pollutant`**: We dynamically computed the `idxmax()` across the four pollutant columns for every city row to explicitly identify which specific chemical was driving the maximum AQI score.
2.  **`hazard_severity_score`**: We mapped the ordinal string categories ("Good", "Unhealthy", etc.) into a numerical scale (`1` to `6`). This allowed for frequency distribution tracking and numerical correlation.

---

## 5. Data Analysis Operations

The core Python analysis (`pandas`, `numpy`) involved several complex operations:
*   **Subgroup Comparisons:** Grouped the dataset by `country` to extract the Top 10 most polluted versus Top 10 cleanest countries. 
*   **Relationship Matrix:** Generated a `.corr()` matrix demonstrating that PM2.5 holds an overwhelmingly strong positive correlation with the total AQI compared to all other variables.
*   **Anomaly & Outlier Detection:** Applied Z-Score calculations to find statistical anomalies ($Z > 3$). We discovered a small cluster of isolated cities breaking the global norms, proving severe pollution is highly localized instead of a global average trend.
*   **NumPy Coefficient of Variation:** Calculated the volatility of each pollutant ($CV = \sigma / \mu$). PM2.5 proved to be the most radically unpredictable gas metric worldwide.

---

## 6. Visualizations & Insights

![Chart 1: Top 10 Most Polluted Countries](images/chart1_top10_countries.png)
**Description & Insight:** The horizontal bar chart highlights the 10 nations suffering from the most alarming long-term air pollution, heavily concentrated in the Middle East and South Asia (e.g., Bahrain, India). This validates our first analytical question regarding massive geographical disparity.

![Chart 2: Pie Chart of Primary Pollutant Distribution](images/chart2_primary_pollutant_pie.png)
**Description & Insight:** This pie chart reveals what type of pollutant causes the worst air days globally. PM2.5 dominates by a monumental margin (~50%), while Ozone dictates another ~43%. Managing AQI crises largely requires filtering these two specific elements rather than CO or NO2.

![Chart 3: Scatter Plot of PM2.5 vs Overall AQI](images/chart3_pm25_vs_aqi_scatter.png)
**Description & Insight:** Plotting individual city PM2.5 levels against total AQI reveals a massive, thick cluster trailing directly along the $x=y$ trendline. This confirms our correlation matrix: PM2.5 almost entirely dictates the maximum daily spikes for high-scoring cities.

![Chart 4: Global Distribution Histogram of Daily AQI](images/chart4_global_aqi_histogram.png)
**Description & Insight:** The global histogram outlines a massive right-skewed distribution. The enormous peak on the far left reveals that the vast majority of cities hover near 50-70 (Moderate/Good). The long right tail bleeding past the 300 Hazardous threshold proves that deadly air is highly localized in specific anomalous zones.

![Chart 5: Box Plot of AQI Distribution per Category](images/chart5_boxplot_hazard_distribution.png)
**Description & Insight:** The box-and-whisker plot visualizes the boundaries of each individual AQI category. Noticeably, categories like "Good" and "Moderate" span an extremely condensed mathematical gap. The "Hazardous" category, however, loses that tight cap, revealing massive, unpredictable outliers stretching up to score 500.

![Chart 6: Grouped Bar Chart - Good vs Hazardous Composition](images/chart6_grouped_bar_composition.png)
**Description & Insight:** Distilling the foundational cause across extreme boundaries, this comparative bar chart uncovers an alarming reality. Ambient quantities of Carbon Monoxide or Nitrogen Dioxide remain virtually flat between the cleanest and worst cities in the world. Instead, PM2.5 levels experience a catastrophic multiplier entirely on their own in Hazardous zones.

---

## 7. Findings & Limitations

### Core Findings
1. **Massive Geographic Inequality:** The Top 10 most polluted nations boast average AQIs deep into the Unhealthy range, localized heavily in arid or rapidly industrializing regions of South Asia and the Middle East.
2. **PM2.5 is the Unrivaled Danger:** Fine particulate matter (PM2.5) and Ozone overwhelmingly dictate global air quality, causing the worst air quality days in over 90% of tracked cities combined.
3. **Hazardous Zones are PM-Specific Disasters:** Our advanced analysis proved that "Hazardous" cities don't suffer from a universal rise in all toxic gases (CO and NO2 barely change). The crisis is localized exclusively to exponential spikes in PM2.5.
4. **Severe Pollution is Localized, not Global:** The numerical distribution proves the majority of the world's population tracked enjoys "Good" or "Moderate" air. Extreme pollution is restricted to statistical anomalies suffering isolated crises.
5. **High Volatility in Particulate Matter:** Driven by our NumPy Coefficient of Variation calculation, PM2.5 proves to be the most volatile and unpredictable measuring standard, experiencing violent spikes that are harder to forecast locally than stable ambient gases.

### Limitations of Analysis
*   **No Temporal / Time-Series Data:** This dataset is a cross-sectional snapshot devoid of timestamps. We cannot analyze seasonal pollution variance (e.g., winter thermal inversions vs. summer wildfires) or multi-year trends.
*   **Correlation does not equal Causation:** While we firmly correlated PM2.5 exclusively driving the total AQI, we cannot identify the explicit localized *causes* of this PM2.5 (such as industrial zoning, fossil fuel traffic, or valley geography trapping the air) using this dataset alone.
*   **Geographic Sampling Bias:** Air quality monitoring grids are expensive and typically clustered tightly within heavily urbanized or wealthy capitals. The dataset likely over-represents city-center pollution while under-representing vast rural geographies.

---

## 8. Conclusion

This comprehensive analysis successfully demonstrates that global air quality is not a universally degrading metric, but rather a profoundly unequal geographic crisis. By executing structured data cleaning, feature engineering, and NumPy/Pandas analysis, we definitively concluded that fine particulate matter (PM2.5) is the overwhelming, volatile driver of dangerous Air Quality Indexes worldwide. Future mitigating policies must hyper-target localized PM2.5 emission sources in concentrated industrial hot zones rather than treating all ambient gases equally.
