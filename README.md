# Data Binning: Horsepower Analysis

This branch demonstrates **data binning techniques** using Pandas to categorize continuous horsepower values into discrete groups for better analysis and visualization.

## Key Analysis

### 1. Original Horsepower Distribution
<img width="500" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/0a82172c-b905-4687-8749-ce14d0ea9f11" />

**Features**:  
- Continuous distribution of horsepower values  
- Raw data visualization before binning  
- Baseline for comparison with binned data

### 2. Binned Horsepower Categories
<img width="500" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/f22130c5-d245-4174-9992-7b47aa15e55d" />

**Categories**: Low, Medium, High  
**Benefits**:  
- Reduced complexity from 59 unique values to 3 categories  
- Clear segmentation for analysis and modeling  
- Improved interpretability for decision making

## Code Highlights
```python
# Convert to integer and create bins
df["horsepower"] = df["horsepower"].astype(int, copy=True)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)

# Apply binning with category labels
group_names = ["Low", "Medium", "High"]
df["horsepower-binned"] = pd.cut(
    df["horsepower"], bins, labels=group_names, include_lowest=True
)

# Visualize results
plt.bar(group_names, df["horsepower-binned"].value_counts())
```

## Technical Implementation

### Binning Strategy
- **Method**: Equal-width binning using `pd.cut()`
- **Dividers**: 4 dividers creating 3 equal intervals
- **Labels**: Descriptive category names (Low, Medium, High)
- **Data Type**: Converted to integer for consistent binning

### Visualization Comparison
- **Before**: Histogram showing continuous distribution
- **After**: Bar chart showing category counts
- **Result**: Successfully narrowed intervals from 59 to 3

### File Structure:
```
data-binning/
├── README.md
├── horsepower-binning.py
├── horsepower-histogram.png
└── horsepower-binned.png
```
