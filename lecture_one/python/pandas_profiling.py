import sklearn.datasets
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

iris = sklearn.datasets.load_iris(as_frame=True)
data = pd.DataFrame(data= np.c_[iris['data'],
                          iris['target']],
      columns= iris['feature_names'] + ['target'])

report = ProfileReport(data, title='My Data',correlations = {
    "pearson": {"calculate": True},
    "spearman": {"calculate": True},
    "kendall": {"calculate": True}
  })
report.to_file("my_report.html")