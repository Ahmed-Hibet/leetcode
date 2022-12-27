class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # An (m+1) times (n+1) matrix
        C = [[0] * (n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    C[i+1][j+1] = C[i][j] + 1
                else:
                    C[i+1][j+1] = max(C[i+1][j], C[i][j+1])
        return C[m][n]
