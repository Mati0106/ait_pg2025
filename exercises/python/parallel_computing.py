from time import time
from joblib import Parallel, delayed


# Function to perform a CPU-intensive task
def calculate_square(i, number):
    print(f"Iteration {i}, for number {number}")
    return number ** 100000


# List of numbers to process
numbers = list(range(1, 100))  # Adjust the range to show a more dramatic difference

# Sequential execution
start_time = time()
squares_sequential = [calculate_square(i, num) for i, num in enumerate(numbers)]
sequential_duration = time() - start_time
print(f"Sequential Execution Time: {sequential_duration:.4f} seconds")

# Parallel execution
start_time = time()
squares_parallel = Parallel(n_jobs=-1)(delayed(calculate_square)(i, num) for i, num in enumerate(numbers))
parallel_duration = time() - start_time
print(f"Parallel Execution Time: {parallel_duration:.4f} seconds ")

# Show speedup
speedup = sequential_duration / parallel_duration
print(f"Speedup using Parallel: {speedup:.2f}x faster")
