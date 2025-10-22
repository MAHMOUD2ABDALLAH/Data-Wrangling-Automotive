# Automotive Data Analysis Project

## Project Overview
This project focuses on comprehensive data wrangling and analysis of automotive datasets using Python. The initiative encompasses multiple data processing techniques to transform raw vehicle data into structured, analysis-ready formats suitable for statistical modeling and business intelligence applications.

## Core Data Processing Techniques

### Data Wrangling
Systematic cleaning and preparation of raw automotive data, addressing missing values, inconsistent formats, and data quality issues across multiple vehicle attributes and specifications.

### Data Standardization
Implementation of consistent measurement units and formats across the dataset, including conversion of fuel efficiency metrics and standardization of technical specifications for comparative analysis.

### Data Normalization
Scaling of numerical features to standardized ranges, particularly applied to vehicle dimensions and performance metrics to enable meaningful comparisons and machine learning applications.

### Data Binning
Categorization of continuous variables into discrete intervals, such as segmenting horsepower values into Low, Medium, and High categories for simplified analysis and visualization.

### Data Bins Visualization
Development of visual representations for binned data, including histograms and bar charts that demonstrate the distribution of categorized variables and facilitate data interpretation.

### Data Indicator Variables
Creation of binary variables for categorical data, preparing the dataset for machine learning algorithms that require numerical input features.

## Technical Scope
The project processes comprehensive automotive datasets containing vehicle specifications from multiple manufacturers, addressing real-world data challenges including missing values, inconsistent formatting, and varied measurement units. The resulting cleaned datasets support advanced analytics, predictive modeling, and business intelligence applications in the automotive industry.

## File Structure
```
data-wrangling/
├── data-cleaning.py
├── missing-values-handling.py
├── data-type-conversion.py
└── README.md

data-standardization/
├── mpg-to-l100km-conversion.py
├── unit-standardization.py
├── feature-scaling.py
└── README.md

data-normalization/
├── min-max-normalization.py
├── max-value-normalization.py
├── z-score-normalization.py
└── README.md

data-binning/
├── horsepower-binning.py
├── equal-width-bins.py
├── equal-frequency-bins.py
└── README.md

data-bins-visualization/
├── histogram-bins.py
├── bar-chart-bins.py
├── comparative-visualizations.py
└── README.md

data-indicator-variable/
├── one-hot-encoding.py
├── dummy-variables.py
├── categorical-encoding.py
└── README.md
```
## Author
Joseph Santarcangelo

## Project Outcomes
The implemented data processing pipeline transforms complex automotive data into structured formats suitable for analytical applications, providing foundations for vehicle performance analysis, pricing models, and market trend identification in the automotive sector.
