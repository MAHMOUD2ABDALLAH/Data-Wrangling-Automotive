# Data Binning: Horsepower Analysis

This branch demonstrates **data binning techniques** using Pandas to categorize continuous horsepower values into discrete groups for better analysis and visualization.

## Key Analysis

### 1. Original Horsepower Distribution
<img width="500" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/0a82172c-b905-4687-8749-ce14d0ea9f11" />

**Features**:  
- Continuous distribution of horsepower values ranging from approximately 50 to 300
- Raw data visualization showing frequency distribution across all horsepower values
- Baseline histogram for comparison with binned data

### 2. Binned Horsepower Categories
<img width="500" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/f22130c5-d245-4174-9992-7b47aa15e55d" />

**Categories**: Low, Medium, High  
**Benefits**:  
- Reduced complexity from 59 unique values to 3 categories  
- Clear segmentation for analysis and modeling  
- Improved interpretability for decision making

### 3. Binned Data Visualization on Real Dataset
<img width="500" height="500" alt="Figure_3" src="https://github.com/user-attachments/assets/fd18d75b-f26a-46f1-8410-888207659776" />
**Features**:
- Direct histogram visualization using 3 bins on the original horsepower data
- Shows the actual distribution across the three defined categories
- Provides a realistic view of how the data is segmented in practice

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

# Multiple visualization approaches
plt.bar(group_names, df["horsepower-binned"].value_counts())
plt.hist(df["horsepower"], bins=3)
```

## Technical Implementation

### Binning Strategy
- **Method**: Equal-width binning using `pd.cut()`
- **Dividers**: 4 dividers creating 3 equal intervals across the horsepower range
- **Labels**: Descriptive category names (Low, Medium, High)
- **Data Type**: Converted to integer for consistent binning

### Visualization Approaches
- **Before**: Detailed histogram showing continuous distribution (59 intervals)
- **After**: Bar chart showing category counts (3 intervals)
- **Real Data View**: Histogram with 3 bins applied directly to original data
- **Result**: Successfully narrowed intervals from 59 to 3 while maintaining data integrity

### File Structure:
```
data-binning/
├── README.md
├── horsepower-binning.py
├── original-horsepower-distribution.png
├── binned-categories-chart.png
└── real-data-binned-visualization.png
```
