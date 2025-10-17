import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('data.csv')
# Sort the DataFrame by a single column
sorted_df = df.sort_values(by='Column_Name', ascending=False)

# Sort the DataFrame by multiple columns
sorted_df_multi = df.sort_values(by=['Column1', 'Column2'], ascending=[True, False])
# In this example, we sort the DataFrame by one or multiple columns in ascending or descending order.

# Example 7: Adding and Removing Columns

# Add a new column
df['New_Column'] = df['Column1'] + df['Column2']

# Remove a column
df.drop(columns=['Column_Name'], inplace=True)
# Here, we demonstrate how to add a new column to the DataFrame and remove an existing column.

# Example 8: Merging and Concatenating DataFrames

# Merge two DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='Common_Column')

# Concatenate multiple DataFrames vertically
concatenated_df = pd.concat([df1, df2], axis=0)

# Example 9: Applying Functions to Data

# Apply a function to each element of a column
df['New_Column'] = df['Column_Name'].apply(lambda x: x**2)

# Apply a function to each row of the DataFrame
df['New_Column'] = df.apply(lambda row: row['Column1'] + row['Column2'], axis=1)
# Here, we demonstrate how to apply functions to individual elements or entire rows of a DataFrame.

# Example 10: Exporting Data

# Export DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# Export DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
# In this example, we export the DataFrame to CSV and Excel files, respectively.