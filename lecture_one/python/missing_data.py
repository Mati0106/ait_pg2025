import sklearn.datasets
import pandas as pd
import numpy as np

iris = sklearn.datasets.load_iris(as_frame=True)
data = pd.DataFrame(data= np.c_[iris['data'],
                          iris['target']],
      columns= iris['feature_names'] + ['target'])
data.isnull().sum()