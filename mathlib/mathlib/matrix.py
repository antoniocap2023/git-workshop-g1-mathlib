import utils.py
import numpy as np

class Matrix:
    """
    A class to represent a matrix.
    """

    data: list[list[float]]

    def __init__(self, data: list[list[float]]):
        """
        Constructs all the necessary attributes for the matrix object.
        """
        self.data = data

    def __str__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


    def __add__(self, other):
        """
        Add two matrices together.
        """
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions to be added.")

        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])


    def __mul__(self, other):
        """
        Multiply a matrix by a scalar.
        """
        return Matrix([[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))])

    def cofactor(self, p, q):
        matrix = np.delete(self.data, p, axis=0)
        matrix = np.delete(matrix, q, axis=1)
        return Matrix(matrix)

    def determinant(self):
        n = self.shape[0]

        if n == 2:
            return self.data[0, 0] * self.data[1, 1] - self.data[0, 1] * self.data[1, 0]
        
        det = 0
        for col in range(n):
            cofactor_matrix = self.cofactor(0, col)
            det += ((-1) ** col) * self.data[0, col] * cofactor_matrix.determinant()

        return det
    
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible")

        n = self.shape[0]
        cofactor_matrix = np.zeros((n, n))

        for row in range(n):
            for col in range(n):
                minor_matrix = utils.cofactor(self.data)
                cofactor_matrix[row, col] = ((-1) ** (row + col)) * minor_matrix.determinant()

        adjugate_matrix = cofactor_matrix.T

        inverse_matrix = adjugate_matrix / det

        return inverse_matrix 



    # TODO: Person 1 - Implement matrix outer product (__matmul__)

    # TODO: Person 1 - Implement matrix transposition (transpose)

    # TODO: Person 2 - Implement determinant calculation (determinant)
    # Either code together or have one person code and the other review
    # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
    # If reviewing, leave comments on what you think can be improved

    # TODO: Person 2 - Implement inverse calculation (inverse)
    # Either code together or have one person code and the other review
    # ...

    # TODO: Person 3 - Implement a function that concatenates two matrices horizontally (hconcat)

    # TODO: Person 3 - Implement a function that concatenates two matrices vertically (vconcat)

    # TODO: Person 1 & 3 & 4 - Implement matrix eigenvalues and eigenvectors (eigen)