import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Example 26: Handling Time Zone Conversion
from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Format the current datetime as a string in the desired format
current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Convert the formatted datetime string to Pandas datetime
df['Datetime_Column'] = pd.to_datetime(current_datetime_str)

# Display the DataFrame with the new datetime column
print(df)
# Convert timezone of datetime column
df['Datetime_Column'] = df['Datetime_Column'].dt.tz_localize('UTC').dt.tz_convert('America/New_York')
# In this example, we convert the timezone of a datetime column from UTC to America/New_York.

# Example 27: Concatenating Strings in DataFrame

# Concatenate strings from multiple columns
df['Full_Name'] = df['First_Name'] + ' ' + df['Last_Name']
# Here, we concatenate strings from 'First_Name' and 'Last_Name' columns to create a new column 'Full_Name' in the DataFrame.

# Example 28: Handling Categorical Data with One-Hot Encoding

# Perform one-hot encoding for categorical data
one_hot_encoded = pd.get_dummies(df['Categorical_Column'], prefix='Category')
df = pd.concat([df, one_hot_encoded], axis=1)
# In this example, we use one-hot encoding to convert categorical data into binary vectors for each category.

# Example 29: Handling Multi-level Indexing

# Create DataFrame with multi-level index
multi_index_df = df.set_index(['Index_Column1', 'Index_Column2'])

# Access data using multi-level indexing
value = multi_index_df.loc['Index_Value1', 'Index_Value2']['Column_Name']
# Here, we create a DataFrame with a multi-level index and demonstrate how to access data using multi-level indexing.

# Example 30: Applying Group-wise Operations

# Apply group-wise operations on DataFrame
grouped_data = df.groupby('Group_Column')['Numeric_Column'].mean()
# In this example, we group the DataFrame by a column and calculate the mean of a numeric column for each group.