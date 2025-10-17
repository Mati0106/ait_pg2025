# Example 20: Model Interpretability with Partial Dependence Plots

from sklearn.inspection import plot_partial_dependence

# Visualize partial dependence of features on target
fig, ax = plt.subplots(figsize=(10, 6))
plot_partial_dependence(model, X_train, features=[(0, 1), (1, 3)], ax=ax)
plt.show()
