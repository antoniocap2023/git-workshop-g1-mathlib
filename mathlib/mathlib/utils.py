def validate_matrix(matrix):
    """
    Validates if the input is a well-formed matrix (2D list with consistent row lengths).
    :param matrix: 2D list representing the matrix.
    :return: True if valid, raises ValueError otherwise.
    """
    # TODO: Person 4 - Implement matrix validation logic
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("The matrix must be a list of lists.")

    # Check if all rows have the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("All rows in the matrix must have the same length.")

    return True

def check_dimensions(matrix1, matrix2):
    """
    Checks if two matrices can be added or multiplied.
    :param matrix1: First matrix (2D list).
    :param matrix2: Second matrix (2D list).
    :return: True if dimensions are compatible, raises ValueError otherwise.
    """
    # TODO: Person 4 - Implement dimension check logic
    # To be added, want the number of rows and the number of columns to match
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        return True
    if len(matrix1[0]) == len(matrix2):
        return True
    if len(matrix1) == len(matrix1[0]):
        return True
    raise ValueError("Matrices have incompatible dimensions for addition or multiplication.")


def identity_matrix(size):
    """
    Creates an identity matrix of the given size.
    :param size: The number of rows/columns for the identity matrix.
    :return: Identity matrix as a 2D list.
    """
    # TODO: Person 4 - Implement identity matrix creation
    pass

def zero_matrix(rows, cols):
    """
    Creates a zero matrix with the given dimensions.
    :param rows: Number of rows.
    :param cols: Number of columns.
    :return: Zero matrix as a 2D list.
    """
    # TODO: Person 4 - Implement zero matrix creation
    return [[0.0 for _ in range(cols)] for _ in range(rows)]

def minor(matrix, row, col):
    """
    Calculates the minor of a matrix by removing the specified row and column.
    :param matrix: 2D list representing the matrix.
    :param row: The row to remove.
    :param col: The column to remove.
    :return: The minor matrix as a 2D list.
    """
    # TODO: Person 3 & 4 - Implement minor calculation
    # Either code together or have one person code and the other review
    # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
    # If reviewing, leave comments on what you think can be improved
    pass

def cofactor(matrix):
    """
    Calculates the cofactor matrix of a given matrix.
    :param matrix: 2D list representing the matrix.
    :return: Cofactor matrix as a 2D list.
    """
    # TODO: Person 3 & Person 4 - Implement cofactor calculation
    # Either code together or have one person code and the other review
    # ...
    cofactor_mat = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix))
    

