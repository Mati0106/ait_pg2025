import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('data.csv')
# Example 11: Filtering Rows Based on Multiple Conditions

# Filter rows based on multiple conditions
filtered_data = df[(df['Column1'] > 10) & (df['Column2'] == 'Value')]
# In this example, we filter rows based on multiple conditions using logical operators (& for AND, | for OR).

# Example 12: Handling Dates and Times

# Convert a column to datetime format
df['Date_Column'] = pd.to_datetime(df['Date_Column'])

# Extract components of dates (e.g., year, month, day)
df['Year'] = df['Date_Column'].dt.year
df['Month'] = df['Date_Column'].dt.month
df['Day'] = df['Date_Column'].dt.day
# Here, we demonstrate how to work with date and time data in DataFrame columns, including converting to datetime format and extracting components.

# Example 13: Reshaping Data with Pivot Tables

# Create a pivot table
pivot_table = df.pivot_table(index='Column1', columns='Column2', values='Value_Column', aggfunc='mean')
# In this example, we use the pivot_table function to reshape the DataFrame based on specified index, columns, values, and aggregation function.

# Example 14: Handling Categorical Data

# Convert a categorical column to dummy variables
dummy_variables = pd.get_dummies(df['Categorical_Column'], prefix='Category')

# Merge dummy variables with the original DataFrame
df = pd.concat([df, dummy_variables], axis=1)
# Here, we convert categorical data into dummy variables using one-hot encoding.

# Example 15: Combining DataFrames with Merge and Join Operations

# Merge two DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='Common_Column')

# Join two DataFrames based on index
joined_df = df1.join(df2, how='inner')
# In this example, we demonstrate how to combine DataFrames using merge and join operations based on common columns or index.

# Example 16: Handling Duplicate Data

# Drop duplicate rows based on all columns
df.drop_duplicates(inplace=True)

# Drop duplicate rows based on specific columns
df.drop_duplicates(subset=['Column1', 'Column2'], inplace=True)
# In this example, we remove duplicate rows from the DataFrame based on all columns or specific columns.

# Example 17: Working with Text Data

# Convert text data to lowercase
df['Text_Column'] = df['Text_Column'].str.lower()

# Count occurrences of a substring in text data
df['Substr_Count'] = df['Text_Column'].str.count('substring')
# Here, we manipulate text data in a DataFrame by converting it to lowercase and counting occurrences of a substring.

# Example 18: Handling Outliers

# Identify outliers using z-score
from scipy.stats import zscore
df['Z_Score'] = zscore(df['Numeric_Column'])

# Remove outliers based on z-score threshold
threshold = 3
df_filtered = df[df['Z_Score'].abs() < threshold]
# In this example, we use z-score to identify and remove outliers from numeric data in the DataFrame.

# Example 19: Grouping Data by Time Periods

# Convert datetime column to period index
df['Date_Column'] = pd.to_datetime(df['Date_Column'])
df.set_index('Date_Column', inplace=True)
df_period = df.to_period('M')

# Group data by month and calculate mean
monthly_mean = df_period.groupby(df_period.index)['Value_Column'].mean()
#Here, we convert a datetime column to a period index and group the data by month to calculate the mean value.

# Example 20: Handling Missing Values with Interpolation

# Interpolate missing values linearly
df_interpolated = df.interpolate(method='linear')

# Forward fill missing values
df_ffill = df.ffill()

# Backward fill missing values
df_bfill = df.bfill()
# In this example, we handle missing values in the DataFrame by interpolating linearly, forward filling, or backward filling.

