# Przyklad opracowany na podstawie https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('diabetes.csv')
#dataset = pd.read_csv('lecture_two/diabetes.csv')
X = dataset.iloc[:,0:7]
Y = dataset.iloc[:,7]

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

model = XGBRegressor()
model.fit(X_train, y_train)

print(model)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]


# evaluate predictions
mse = mean_squared_error(y_test, predictions)
print("MSE: {0}".format(mse))