import numpy as np
from tqdm import tqdm
import random
import sys

def reduced_square(n):
    matrix = np.tile(np.arange(1, n+1), (n, 1))
    matrix = (matrix - np.arange(n).reshape(n, 1) - 1) % n + 1
    return matrix

def swap_random_columns(matrix):
    n = matrix.shape[1]
    col1, col2 = np.random.choice(n, 2, replace=False)
    # print("swapping cols:", col1, col2)
    matrix[:, [col1, col2]] = matrix[:, [col2, col1]]
    return matrix

def swap_random_rows(matrix):
    n = matrix.shape[0]
    row1, row2 = np.random.choice(n, 2, replace=False)
    # print("swapping rows:", row1, row2)
    matrix[[row1, row2], :] = matrix[[row2, row1], :]
    return matrix


def flip_along_antidiagonal(matrix):
    transposed = matrix.T
    flipped = np.flipud(transposed)
    return flipped

def transposed(matrix):
    return matrix.T

def equivalence_class_from(square):
    squareset = set()
    squareset.add(tuple(map(tuple, square)))

    for i in tqdm(range(int(sys.argv[2]))):
        case_number = random.randint(1, 4)
        if case_number == 1:
            square = swap_random_rows(square)
        elif case_number == 2:
            square = swap_random_columns(square)
        elif case_number == 3:
            square = transposed(square)
        else:
            square = flip_along_antidiagonal(square)
        squareset.add(tuple(map(tuple, square)))
    return squareset


A = reduced_square(int(sys.argv[1]))
# B = np.array([[1, 4, 3, 2],[4, 1, 2, 3],[3, 2, 1, 4],[2, 3, 4, 1]])
B = np.array([[1, 2, 3, 4, 5],[5, 1, 2, 3, 4],[4, 5, 1, 2, 3],[3, 4, 5, 1, 2],[2, 3, 4, 5, 1]])

A_class = equivalence_class_from(A)
B_class = equivalence_class_from(B)

print(len(A_class-B_class))



