import pandas as pd

# Create a complex DataFrame with students' exam scores across multiple subjects
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math_Score': [85, 78, 90, 92, 88],
    'Science_Score': [89, 85, 95, 91, 87],
    'English_Score': [78, 82, 84, 79, 88],
    'Graduated': [True, False, True, True, False]
}

df = pd.DataFrame(data)

# Select students who scored above 85 in both Math and Science, and are not yet graduated
selected_students = df.loc[(df['Math_Score'] > 85) & (df['Science_Score'] > 85) & (df['Graduated'] == False)]
print(selected_students)

# ex 2
# Create a DataFrame with 10 rows and 5 columns
data = {'A': range(1, 11), 'B': range(11, 21), 'C': range(21, 31), 'D': range(31, 41), 'E': range(41, 51)}
df = pd.DataFrame(data)

# Use .iloc to select every second row and only columns B, D, and E
selected_data = df.iloc[::2, [1, 3, 4]]  # Rows with step 2 and specific column indices
print(selected_data)

# ex 3
# Create a MultiIndex DataFrame for a hierarchical structure
arrays = [
    ['Group1', 'Group1', 'Group2', 'Group2'],
    ['Alice', 'Bob', 'Charlie', 'David']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Name'))
data = {'Score': [88, 92, 85, 90]}
df = pd.DataFrame(data, index=index)

# Use .loc to select scores for students in 'Group2' only
group2_scores = df.loc['Group2']
print(group2_scores)

# Use .loc to select score for a specific student 'Alice' in 'Group1'
alice_score = df.loc[('Group1', 'Alice'), 'Score']
print(alice_score)

# ex 4
# Create a DataFrame with random values
df = pd.DataFrame({
    'A': [i for i in range(10)],
    'B': [i ** 2 for i in range(10)],
    'C': [i ** 3 for i in range(10)],
    'D': [i ** 4 for i in range(10)]
})

# Select rows 2 through 5 (exclusive of 6) and columns 1 through 3
cross_section = df.iloc[2:6, 1:4]  # Rows [2, 3, 4, 5] and columns [B, C, D]
print(cross_section)

# ex 5
# Create a DataFrame with students' grades
grades = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
          'Math': [78, 85, 67, 92],
          'Science': [83, 79, 90, 88]}

df = pd.DataFrame(grades)

# Use .loc to increase the Science score of students who scored less than 80 in Math by 5 points
df.loc[df['Math'] < 80, 'Science'] += 5
print(df)


# to create new column with value new value
df.loc[df['Math'] < 80, 'best_in_math'] = False

# create another rule that will find students about or equal 80 Math and pass True value for them 

# create option with iloc and think about other option
