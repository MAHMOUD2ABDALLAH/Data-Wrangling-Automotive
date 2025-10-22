# Data Transformation: MPG to L/100km Conversion

This branch demonstrates **data transformation techniques** by converting fuel efficiency metrics from miles per gallon (MPG) to liters per 100 kilometers (L/100km) - the standard measurement used in most countries outside the United States.

## Key Transformation

### Conversion Process
**Mathematical Formula**: 
```
L/100km = 235 / MPG
```

**Columns Transformed**:
- `city-mpg` → `city-L/100km`
- `highway-mpg` → `highway-L/100km`

## Code Highlights

```python
# Convert MPG to L/100km for city fuel efficiency
if 'city-mpg' in df.columns:
    df['city-mpg'] = 235 / pd.to_numeric(df['city-mpg'], errors='coerce')
    df = df.rename(columns={'city-mpg': 'city-L/100km'})
    
# Convert MPG to L/100km for highway fuel efficiency  
if 'highway-mpg' in df.columns:
    df['highway-mpg'] = 235 / pd.to_numeric(df['highway-mpg'], errors='coerce')
    df = df.rename(columns={'highway-mpg': 'highway-L/100km'})
```

## Technical Implementation

### Conversion Strategy
- **Mathematical Accuracy**: Used precise conversion factor (235)
- **Error Handling**: Applied `errors='coerce'` to handle any invalid values
- **Data Type Safety**: Used `pd.to_numeric()` for robust type conversion
- **Column Management**: Maintained same dataframe structure with renamed columns

### Benefits of Transformation
- **Standardization**: Converts to internationally recognized metric
- **Interpretability**: Lower values now indicate better fuel efficiency
- **Analysis Ready**: Consistent units for comparative analysis
- **Global Compatibility**: Aligns with European and Asian market standards

## Data Impact

**Before Conversion** (MPG):
- Higher values = better fuel efficiency
- US standard measurement
- Example: 30 mpg = good efficiency

**After Conversion** (L/100km):
- Lower values = better fuel efficiency  
- International standard measurement
- Example: 30 mpg → 7.83 L/100km

### File Structure:
```
data-transformation/
├── README.md
├── mpg-conversion.py
└── automotive-dataset.csv
```

**Result**: Successfully transformed fuel efficiency metrics from MPG to L/100km, creating a standardized dataset suitable for global analysis and comparison across different measurement systems.
