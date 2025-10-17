# Example 11: Using Principal Component Analysis (PCA) for Dimensionality Reduction

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Perform PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualize the reduced-dimensional data
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization of Iris Dataset')
plt.show()
# In this example, we use PCA to reduce the dimensionality of the Iris dataset to two dimensions and visualize the reduced-dimensional data.

# Example 12: Hyperparameter Tuning with Grid Search

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10, 100],
              'gamma': [1, 0.1, 0.01, 0.001],
              'kernel': ['rbf', 'linear', 'poly', 'sigmoid']}

# Initialize a SVM classifier
svm_classifier = SVC()

# Perform grid search for hyperparameter tuning
grid_search = GridSearchCV(svm_classifier, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters
print("Best Parameters:", grid_search.best_params_)

# Evaluate the model with the best hyperparameters
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# Here, we use grid search with cross-validation to tune the hyperparameters of a Support Vector Machine (SVM) classifier and evaluate its performance.

# Example 13: Using Pipelines for Streamlined Model Building
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Create a pipeline with preprocessing and modeling steps
pipeline = make_pipeline(StandardScaler(), RandomForestClassifier())

# Train the model using the pipeline
pipeline.fit(X_train, y_train)

# Evaluate the model
accuracy = pipeline.score(X_test, y_test)
print("Accuracy:", accuracy)
# In this example, we use pipelines to create a streamlined workflow for preprocessing and modeling, combining standardization with a Random Forest classifier.
