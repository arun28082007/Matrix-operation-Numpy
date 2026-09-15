import numpy as np

def get_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    print(f"Enter the elements of Matrix {name} row by row (space-separated):")
    
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Expected {cols} values. Please re-enter Row {i + 1}:")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
        elements.append(row)
        
    return np.array(elements)

def display_matrix(title, matrix):
    print(f"\n--- {title} ---")
    print(matrix)
    print("--------------------")

def main():
    while True:
        print("\n=== MATRIX OPERATIONS TOOL ===")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Matrix Determinant")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            A = get_matrix("A")
            B = get_matrix("B")
            if A.shape == B.shape:
                display_matrix("Result (A + B)", A + B)
            else:
                print("\nError: Matrices must have identical dimensions to add.")

        elif choice == "2":
            A = get_matrix("A")
            B = get_matrix("B")
            if A.shape == B.shape:
                display_matrix("Result (A - B)", A - B)
            else:
                print("\nError: Matrices must have identical dimensions to subtract.")

        elif choice == "3":
            A = get_matrix("A")
            B = get_matrix("B")
            if A.shape[1] == B.shape[0]:
                display_matrix("Result (A x B)", np.dot(A, B))
            else:
                print(f"\nError: Columns of A ({A.shape[1]}) must match rows of B ({B.shape[0]}).")

        elif choice == "4":
            A = get_matrix("A")
            display_matrix("Transpose of A", A.T)

        elif choice == "5":
            A = get_matrix("A")
            if A.shape[0] == A.shape[1]:
                det = np.linalg.det(A)
                print(f"\nDeterminant: {det:.4f}")
            else:
                print("\nError: Determinant requires a square matrix (rows == cols).")

        elif choice == "6":
            print("Exiting tool.")
            break
        else:
            print("Invalid selection. Choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
