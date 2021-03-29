"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

---------------
Constraints
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-23^1 <= matrix[i][j] <= 23^1 - 1

"""


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    row, column = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)

    for i in row:
        for j in range(n):
            matrix[i][j] = 0

    for i in column:
        for j in range(m):
            matrix[j][i] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print(setZeroes(matrix))