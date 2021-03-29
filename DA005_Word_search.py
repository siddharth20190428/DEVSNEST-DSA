"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

---------------
Constraints
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


def exist(board, word):
    m, n, p = len(board), len(board[0]), len(word)

    def helper(r, c, pos):
        if pos >= p:
            return True
        elif 0 <= r < m and 0 <= c < n and board[r][c] == word[pos]:
            temp = board[r][c]
            board[r][c] = "*"
            if (
                helper(r - 1, c, pos + 1)
                or helper(r + 1, c, pos + 1)
                or helper(r, c - 1, pos + 1)
                or helper(r, c + 1, pos + 1)
            ):
                return True
            board[r][c] = temp
        return False

    for i in range(m):
        for j in range(n):
            if helper(i, j, 0):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

print(exist(board, word))