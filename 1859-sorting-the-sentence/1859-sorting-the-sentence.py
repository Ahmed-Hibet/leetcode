class Solution:
    def sortSentence(self, s: str) -> str:
        words = []
        for word in s.split():
            words.append((word[-1], word[:-1]))
        words.sort()
        
        sentence = ''
        for word in words:
            sentence += word[1] + ' '
        return sentence[:-1]