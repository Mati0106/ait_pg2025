# Example 20: Lasso Regression

from sklearn.linear_model import Lasso
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Boston housing dataset
import os
import requests

# Define the URL to download the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"

# Define the directory to save the downloaded file
save_dir = "datasets"
os.makedirs(save_dir, exist_ok=True)

# Define the file path to save the downloaded file
file_path = os.path.join(save_dir, "boston.csv")

# Download the dataset file
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print("Dataset downloaded successfully.")
else:
    print("Failed to download dataset.")

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Lasso regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lasso.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# This example demonstrates Lasso regression, a linear regression technique that performs L1 regularization to encourage sparsity in the coefficient values.

# Example 21: Ridge Regression

from sklearn.linear_model import Ridge

# Initialize and train the Ridge regression model
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Make predictions on the test set
y_pred = ridge.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# Here, we use Ridge regression, which performs L2 regularization to penalize large coefficient values and reduce overfitting.

# Example 22: Elastic Net Regression

from sklearn.linear_model import ElasticNet

# Initialize and train the Elastic Net regression model
elastic_net = ElasticNet(alpha=0.5, l1_ratio=0.5)
elastic_net.fit(X_train, y_train)

# Make predictions on the test set
y_pred = elastic_net.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# This example showcases Elastic Net regression, which combines L1 and L2 regularization to balance between sparsity and smoothness in the coefficient values.

# Example 23: XGBoost
import xgboost as xgb

# Convert data into DMatrix format for XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Define parameters for XGBoost
params = {
    'max_depth': 3,
    'eta': 0.1,
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse'
}

# Train the XGBoost model
num_rounds = 100
xgb_model = xgb.train(params, dtrain, num_rounds)

# Make predictions on the test set
y_pred = xgb_model.predict(dtest)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
