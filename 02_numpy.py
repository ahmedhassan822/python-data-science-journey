"""
NumPy Basics Demonstration Script
---------------------------------
This script demonstrates fundamental operations in NumPy, including
the creation of 1-D, 2-D, and 3-D arrays, basic vectorized math,
and advanced indexing techniques.
"""

import numpy as np

def demonstrate_numpy_basics() -> None:
    """
    Executes a series of basic NumPy operations and prints the results
    to the console for educational purposes.
    """
    print("--- 1D Array Operations ---")
    num_array = np.array([1, 2, 3, 4, 5])
    print(f"Original 1D Array:\n{num_array}")

    # Vectorized operation (broadcasting)
    double_array = num_array * 2
    print(f"Doubled 1D Array (Vectorized * 2):\n{double_array}")
    print(f"Dimensions: {num_array.ndim}\n")

    print("--- 2D Array Operations ---")
    num_array2D = np.array([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ])
    print(f"2D Array:\n{num_array2D}")
    print(f"Dimensions: {num_array2D.ndim}\n")

    print("--- 3D Array Operations ---")
    num_array3D = np.array([
        [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
        [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
        [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    ])
    print(f"3D Array:\n{num_array3D}")
    print(f"Dimensions: {num_array3D.ndim}")
    print(f"Shape: {num_array3D.shape}\n")

    print("--- Array Indexing ---")
    # Searching with traditional chain indexing
    chain_index_val = num_array3D[0][2][3]
    print(f"Chain Indexing [0][2][3]: {chain_index_val}")

    # Searching with NumPy's preferred multi-indexing
    multi_index_val = num_array3D[0, 2, 3]
    print(f"Multi-indexing [0, 2, 3]: {multi_index_val}")

if __name__ == "__main__":
    # Print the NumPy version for environment verification
    print(f"System using NumPy Version: {np.__version__}\n")
    demonstrate_numpy_basics()