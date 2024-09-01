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


    # TODO: Person 1 - Implement matrix outer product (__matmul__)
    def __matmul__(self, other):
        """
        Multiply a m x 1 column vector by a 1 x n row vector, resulting in a m x n matrix.
        """
        # vertical x horizontal 
        if len(self.data[0]) == len(other.data):
            return Matrix([[sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))) 
                            for j in range(len(other.data[0]))] 
                            for i in range(len(self.data))])
        # horizontal x vertical 
        elif len(self.data) == len(other.data[0]):
            return Matrix([[sum(self.data[k][i] * other.data[j][k] for k in range(len(self.data))) 
                            for j in range(len(other.data))] 
                            for i in range(len(self.data[0]))])
        else:
            return "Invalid sizes!"
        


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

    # TODO: Person 1, 2, 3 - Implement matrix eigenvalues and eigenvectors (eigen)