# Data Wrangling: Auto Dataset Cleaning

This branch demonstrates **comprehensive data wrangling techniques** for cleaning and preprocessing an automotive dataset, handling missing values, and correcting data formats for analysis.

## Key Data Cleaning Operations

### 1. Initial Data Assessment
**Dataset**: Auto.csv with 26 automotive features  
**Initial Issues**:  
- Missing values represented as '?'  
- Incorrect data types  
- Multiple columns requiring cleaning

### 2. Missing Value Treatment
**Strategies Applied**:  
- **Mean Imputation**: Numerical columns (normalized-losses, bore, stroke)  
- **Mode Imputation**: Categorical columns (num-of-doors)  
- **Direct Replacement**: Converted '?' to NaN systematically

## Code Highlights

```python
# Handle missing values and data type conversion
df.replace("?", np.nan, inplace=True)

# Mean imputation for numerical columns
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, int(avg_norm_loss))

# Data type correction
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
```

## Technical Implementation

### Missing Value Handling
- **Identification**: Systematic column-by-column analysis using `.value_counts()`
- **Numerical Columns**: Replaced with mean values (normalized-losses, bore, stroke)
- **Categorical Columns**: Used most frequent value (num-of-doors)
- **Validation**: Comprehensive missing data evaluation before and after treatment

### Data Type Correction
- **Original Issues**: Mixed data types, string representations of numbers
- **Conversions Applied**:
  - `normalized-losses`: string → int
  - `bore`, `stroke`: string → float
  - `price`, `peak-rpm`: string → float
- **Result**: Consistent, analysis-ready data types

### Columns Processed
- **Symboling**: Insurance risk rating
- **Normalized-losses**: Relative average loss payment
- **Technical Specs**: Bore, stroke, compression-ratio, horsepower
- **Performance Metrics**: City-mpg, highway-mpg, price
- **Vehicle Attributes**: Make, fuel-type, body-style, num-of-doors

## Final Output
**Cleansed Dataset Features**:
- Zero missing values across all 26 columns
- Proper data types for numerical analysis
- Consistent formatting for machine learning readiness
- Preserved original data structure and relationships

### File Structure:
```
data-wrangling/
├── README.md
├── auto-data-cleaning.py
├── data-assessment.png
└── missing-value-treatment.png
```

**Result**: Successfully transformed raw, messy automotive data into a clean, analysis-ready dataset suitable for statistical analysis and machine learning applications.
