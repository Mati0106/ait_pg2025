# Example 1: Loading a CSV file into a DataFrame

import pandas as pd
from pathlib import Path

# Load a CSV file into a DataFrame
path = Path(r"C:\Users\karol\git\ait_pg_2024\datasets\cars.csv")

# from pathlib import Path, PurePath
# path = PurePath(Path.cwd().parents[1].joinpath('datasets/cars.csv'))
# pd.read_csv(path)

# Display the first few rows of the DataFrame
print(df.head(1200))
pd.set_option('display.max_columns',9)
# In this example, we use the read_csv function from Pandas to load a CSV file named data.csv into a DataFrame.

# Example 2: Exploring DataFrame Information

# Display the column names and data types
print("Column Names and Data Types:")
print(df.dtypes)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Display the shape of the DataFrame
print("\nDataFrame Shape:", df.shape)
# Here, we explore information about the DataFrame, such as column names, data types, summary statistics, and the shape of the DataFrame.

# Example 3: Selecting and Filtering Data

# Select a single column
column_data = df[['mpg','displacement']].groupby('displacement').agg({"mpg":"mean"})
df.dtypes

# Select multiple columns
multiple_columns = df[['Column1', 'Column2']]

# Filter rows based on a condition
filtered_data = df[df['Column_Name'] > 10]
# In this example, we demonstrate how to select specific columns and filter rows based on conditions in the DataFrame.

# Example 4: Grouping and Aggregating Data

# Group data by a column and calculate mean
mean_by_group = df.groupby('Column_Name').mean()

# Perform multiple aggregations
agg_results = df.groupby('Column_Name').agg({'Column1': 'mean', 'Column2': 'sum'})
# Here, we group the data by a column and perform aggregations such as mean calculation and summing across multiple columns.

# Example 5: Handling Missing Values

# Drop rows with missing values
df_dropna = df.dropna()

# Fill missing values with a specified value
df_fillna = df.fillna(0)
# In this example, we demonstrate how to handle missing values by either dropping rows with missing values or filling them with a specified value.


# ex1
# Divide table length by 3,
# for first part of rows, assign value 'a'
# for secound part of rows assign value 'b'
# for thrid part of rows assign value 'c'
# create new column and name it target

# ex2
# For all numeric columns, select col and target col,
# for each of those objects use Parralel + delayed to calculate mean() on this object

# ex3
# Filter all unique elements in target column and create 3 datasets,
# for each of them run in Parralel + delayed, pandas-profiling report