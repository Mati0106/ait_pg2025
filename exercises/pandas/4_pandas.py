import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Example 21: Applying Custom Functions to DataFrame Columns

# Define a custom function
def square_root(x):
    return x ** 0.5

# Apply the custom function to a column
df['Square_Root_Column'] = df['Numeric_Column'].apply(square_root)
# In this example, we define a custom function square_root to calculate the square root of a number and apply it to a column in the DataFrame using the apply method.

# Example 22: Rolling Window Calculations

# Calculate the rolling mean
df['Rolling_Mean'] = df['Numeric_Column'].rolling(window=3).mean()

# Calculate the rolling sum
df['Rolling_Sum'] = df['Numeric_Column'].rolling(window=3).sum()
# Here, we use rolling window calculations to compute the rolling mean and sum of a numeric column in the DataFrame.

# Example 23: Resampling Time Series Data

# Resample time series data to a different frequency (e.g., monthly)
monthly_data = df.resample('M').sum()

# Resample time series data and apply aggregation functions
resampled_data = df.resample('W').agg({'Column1': 'sum', 'Column2': 'mean'})
# In this example, we resample time series data to a different frequency (e.g., monthly) and apply aggregation functions such as sum and mean.

# Example 24: Handling Categorical Data with Ordinal Encoding

# Perform ordinal encoding for categorical data
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()
df['Encoded_Column'] = encoder.fit_transform(df[['Categorical_Column']])
# Here, we use ordinal encoding to convert categorical data into numerical values while preserving the ordinal relationship.

# Example 25: Applying Element-wise Operations

# Apply element-wise operations to DataFrame columns
df['New_Column'] = df['Column1'] * df['Column2'] + df['Column3']
# In this example, we perform element-wise operations on DataFrame columns to compute a new column.