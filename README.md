# Interactive Matrix Operations Tool

A command-line application built in Python using the NumPy library to perform core linear algebra operations interactively.

---

## Features

- **Matrix Addition & Subtraction:** Element-wise addition and subtraction with dimension validation.
- **Matrix Multiplication:** Matrix dot product calculation with inner-dimension compatibility checks.
- **Matrix Transposition:** Computes the transpose of any custom $M \times N$ matrix.
- **Determinant Calculation:** Calculates determinants for square matrices ($N \times N$) using `numpy.linalg`.
- **Input Validation:** Enforces correct row element counts and provides descriptive error messages for dimension mismatches.

---

## Requirements

- Python 3.8 or higher
- NumPy

---

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/arun28082007/Matrix-operation-Numpy/tree/master
   cd matrix-operations-tool

 * Install the required dependencies:
   pip install numpy

Usage
Run the program using:
python matrix_tool.py

Menu Options
=== MATRIX OPERATIONS TOOL ===
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Matrix Transpose
5. Matrix Determinant
6. Exit

Example
To compute the transpose of a 2 \times 3 matrix:
 * Select option 4.
 * Enter rows (2) and columns (3).
 * Provide elements row-by-row:
   Row 1: 1 2 3
Row 2: 4 5 6

 * Output:
   --- Transpose of A ---
[[1. 4.]
 [2. 5.]
 [3. 6.]]
--------------------

