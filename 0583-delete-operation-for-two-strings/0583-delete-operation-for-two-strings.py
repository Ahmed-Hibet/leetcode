class Solution:
    def LCS(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        # An (m+1) times (n+1) matrix
        C = [[0] * (n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    C[i+1][j+1] = C[i][j] + 1
                else:
                    C[i+1][j+1] = max(C[i+1][j], C[i][j+1])
        # return the length of LCS
        return C[m][n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.LCS(word1, word2)
        return len(word1) + len(word2) - lcs * 2

