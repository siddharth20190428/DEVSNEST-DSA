"""
Given an m x n matrix, return all elements of the matrix in spiral order.

---------------
Constraints
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiralOrder(matrix):
    """
    rows, cols = len(matrix), len(matrix[0])
    x, y = 0, 0
    x_step, y_step = 1, 1
    x_min, x_max, y_min, y_max = 0, cols, 0, rows
    move_x, move_y = True, False

    result = []
    while len(result) < rows * cols:
        result.append(matrix[y][x])

        if move_x:
            x += x_step
            if (x_step > 0 and x == x_max - 1) or (x_step < 0 and x == x_min):
                move_x, move_y = False, True

                if x_step > 0:
                    x_max -= 1
                else:
                    x_min += 1
                x_step *= -1
                continue

        if move_y:
            y += y_step
            if (y_step > 0 and y == y_max - 1) or (y_step < 0 and y == y_min):
                move_x, move_y = True, False

                if y_step > 0:
                    y_min += 1
                else:
                    y_max -= 1
                y_step *= -1
                continue
    return result
    """
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        else:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        direction = (direction + 1) % 4

    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiralOrder(matrix))