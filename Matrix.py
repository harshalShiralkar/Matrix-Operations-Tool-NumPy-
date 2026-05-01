import numpy as np

def get_matrix_input(name):
    """Prompts user for matrix dimensions and elements."""
    print(f"\n--- Matrix {name} ---")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print("Enter elements row by row (space-separated):")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                raise ValueError(f"Error: Expected {cols} elements.")
            matrix.append(row)
        return np.array(matrix)
    except ValueError as e:
        print(e)
        return None

def main():
    print("Welcome to the Matrix Operations Tool!")
    mat_a = get_matrix_input("A")
    if mat_a is None: return

    while True:
        print("\nChoose Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant\n6. Exit")
        choice = input("Select (1-6): ")

        if choice == '1':
            mat_b = get_matrix_input("B")
            if mat_b is not None and mat_a.shape == mat_b.shape:
                print("\nResult (A + B):\n", mat_a + mat_b)
            else:
                print("Error: Dimensions must match.")

        elif choice == '2':
            mat_b = get_matrix_input("B")
            if mat_b is not None and mat_a.shape == mat_b.shape:
                print("\nResult (A - B):\n", mat_a - mat_b)

        elif choice == '3':
            mat_b = get_matrix_input("B")
            if mat_b is not None and mat_a.shape[1] == mat_b.shape[0]:
                print("\nResult (A @ B):\n", np.dot(mat_a, mat_b))
            else:
                print("Error: Columns of A must match rows of B.")

        elif choice == '4':
            print("\nTranspose (A^T):\n", mat_a.T)

        elif choice == '5':
            if mat_a.shape[0] == mat_a.shape[1]:
                print(f"\nDeterminant: {np.linalg.det(mat_a):.2f}")
            else:
                print("Error: Determinant requires a square matrix.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
