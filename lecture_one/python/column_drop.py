import pandas as pd
import sklearn.datasets

iris = sklearn.datasets.load_iris(as_frame=True)
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

print(data.columns)

col_to_drop = 'sepal length (cm)'
print(col_to_drop)
cols_to_drop = ['sepal length (cm)','sepal width (cm)']

new_data = data.drop(cols_to_drop, axis=1)

# or

data.drop(cols_to_drop, axis=1, inplace=True)
print('FINISHED')


