# Example 1: Loading and Exploring a Dataset

import pandas as pd

from sklearn.datasets import load_iris

# Load the Iris dataset
iris_data = load_iris()

# Extract features and target variable
X = iris_data.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris_data.target  # Target variable (species)

# Optional: If you want the feature names and target names
feature_names = iris_data.feature_names
target_names = iris_data.target_names

# Print some information about the dataset
print("Feature names:", feature_names)
print("Target names:", target_names)
print("Number of samples:", len(X))

iris_df = pd.DataFrame(X, columns=iris_data.feature_names)

# Add the target variable to the DataFrame
iris_df['species'] = y

# Display the first few rows of the DataFrame
print(iris_df.head())

# Save the DataFrame to a CSV file
iris_df.to_csv('iris.csv', index=False)
# Load a dataset (e.g., Iris dataset)
iris_df = pd.read_csv("iris.csv")

# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(iris_df.head())
# This example demonstrates how to load a dataset using pandas and display the first few rows to get a glimpse of the data.

# Example 2: Data Preprocessing

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Split the dataset into features and target variable
X = iris_df.drop("species", axis=1)
y = iris_df["species"]

# Standardize features
scaler = StandardScaler()


# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_tr_scaled = scaler.fit_transform(X_train)
X_ts_scaled = scaler.transform(X_test)


print("Number of training samples:", len(X_tr_scaled))
print("Number of test samples:", len(X_tr_scaled))
# Here, we preprocess the data by standardizing the features and splitting the dataset into training and test sets.

# Example 3: Training a Machine Learning Model


from sklearn.linear_model import LogisticRegression

# Initialize and train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_tr_scaled, y_train)

# Evaluate the model on the test set
accuracy = model.score(X_ts_scaled, y_test)
print("Model accuracy:", accuracy)
# This example illustrates how to train a simple machine learning model (logistic regression) using scikit-learn.

# Example 4: Making Predictions

# Use the trained model to make predictions on the test set
predictions = model.predict(X_ts_scaled)
model.coef_
# Display some sample predictions and corresponding true labels
print("Sample predictions:")
for i in range(5):
    print("Predicted:", predictions[i], "| Actual:", y_test.iloc[i])
# Here, we use the trained model to make predictions on the test set and compare them with the actual labels.

# Example 5: Evaluating Model Performance

from sklearn.metrics import classification_report, confusion_matrix

# Generate a classification report and confusion matrix
print("Classification Report:")
print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
# Finally, this example demonstrates how to evaluate the performance of the trained model using metrics such as classification report and confusion matrix.
