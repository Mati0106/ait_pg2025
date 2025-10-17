# Example 14: Using Neural Networks with TensorFlow
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Define a neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_accuracy)
# Here, we use TensorFlow to define and train a neural network model on the Iris dataset, and then evaluate its performance.

# Example 15: Handling Imbalanced Data with Resampling

from imblearn.over_sampling import RandomOverSampler
from collections import Counter

# Check class distribution before resampling
print("Class Distribution Before Resampling:", Counter(y_train))

# Resample the training data to address class imbalance
oversampler = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

# Check class distribution after resampling
print("Class Distribution After Resampling:", Counter(y_train_resampled))
# In this example, we address class imbalance in the training data using random oversampling with the help of the imbalanced-learn library.
