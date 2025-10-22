# Data Indicator Variables: Categorical Encoding

This branch demonstrates **indicator variable creation** using Pandas to convert categorical data into numerical format suitable for machine learning algorithms and statistical analysis.

## Key Transformations

### 1. Fuel Type Encoding
**Original Values**: "gas", "diesel"  
**Encoded Columns**:
- `fuel-type-gas`: 1 for gas vehicles, 0 otherwise
- `fuel-type-diesel`: 1 for diesel vehicles, 0 otherwise

### 2. Aspiration Type Encoding
**Original Values**: "std", "turbo"  
**Encoded Columns**:
- `aspiration-std`: 1 for standard aspiration, 0 otherwise
- `aspiration-turbo`: 1 for turbo aspiration, 0 otherwise

## Code Highlights
```python
# Create indicator variables for fuel type
dummy_variable_1 = pd.get_dummies(df["fuel-type"], dtype=int)
dummy_variable_1.rename(
    columns={"gas": "fuel-type-gas", "diesel": "fuel-type-diesel"}, inplace=True
)

# Create indicator variables for aspiration type
dummy_variable_2 = pd.get_dummies(df["aspiration"], dtype=int)
dummy_variable_2.rename(
    columns={"std": "aspiration-std", "turbo": "aspiration-turbo"}, inplace=True
)

# Integrate with main dataframe
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop("fuel-type", axis=1, inplace=True)

df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis=1, inplace=True)
```

## Technical Implementation

### Encoding Strategy
- **Method**: One-hot encoding using `pd.get_dummies()`
- **Data Type**: Integer (0/1) for clear binary representation
- **Column Naming**: Descriptive names indicating original category
- **Integration**: Concatenation with original dataframe and removal of categorical columns

### Benefits
- **Machine Learning Ready**: Converts categorical data to numerical format
- **No Ordinal Assumption**: Avoids implying order where none exists
- **Clear Interpretation**: Binary indicators are easily understandable
- **Statistical Compatibility**: Suitable for regression and classification models

### Process Flow
1. Extract categorical column
2. Apply `get_dummies()` for one-hot encoding
3. Rename columns for clarity
4. Concatenate with main dataframe
5. Remove original categorical column

### File Structure:
```
data-indicator-variable/
├── README.md
├── categorical-encoding.py
├── fuel-type-indicators.png
└── aspiration-indicators.png
```
