class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        total_element = sum([len(row) for row in mat])
        if total_element != r*c:
            return mat
        x = -1
        y = 0
        current_size = len(mat[x])
        answer = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(mat[x+1][y])
                y += 1
                if y == current_size:
                    x += 1
                    y = 0
                    current_size = len(mat[x])
            answer.append(row)
        return answer
