# Example 17: Using K-Means Clustering
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate synthetic data for clustering
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='o', s=200, color='red', alpha=0.9)
plt.show()
# In this example, we use K-Means clustering to cluster data points into four clusters and visualize the result.

# Example 18: Text Classification with Naive Bayes
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load the 20 newsgroups dataset
data = fetch_20newsgroups()

# Define a pipeline with TF-IDF vectorization and Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
# This example showcases text classification using the Naive Bayes algorithm on the 20 newsgroups dataset.

# Example 19: Dimensionality Reduction with t-SNE
from sklearn.manifold import TSNE

# Apply t-SNE for dimensionality reduction
tsne = TSNE(n_components=2, random_state=0)
X_tsne = tsne.fit_transform(X)

# Visualize the reduced-dimensional data
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE Visualization of Data')
plt.show()
# Here, we use t-Distributed Stochastic Neighbor Embedding (t-SNE) for dimensionality reduction and visualize the reduced-dimensional data.
