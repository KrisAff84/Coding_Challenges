from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) -1):  # Iterate over the rows
            for j in range(i, len(matrix)):  # Iterate over the column of each row
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,19,19,20],[21,22,23,24,25]]
    Solution().rotate(matrix)
    print(matrix)

    # Solution should be [[7,4,1],[8,5,2],[9,6,3]]

    # After first iteration of i
    # [1,4,7],[2,5,6],[3,8,9]

    # After second iteration of i
    # [1,4,7],[2,5,8],[3,6,9]

    # After third iteration of i
    # [1,4,7],[2,5,8],[3,6,9]
