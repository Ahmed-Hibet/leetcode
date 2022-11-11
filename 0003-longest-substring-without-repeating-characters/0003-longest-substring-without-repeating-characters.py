class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        pos = 1
        min_pos = 1
        max_length = 0
        length = 0
        for i in s:
            try:
                dic[i] += 0
                if dic[i] < min_pos:
                    dic[i] = pos
                    pos += 1
                    continue
                length = pos - min_pos
                min_pos = dic[i] + 1
                dic[i] = pos
                if length > max_length:
                    max_length = length
            except:
                dic[i] = pos
            pos += 1
        length = pos - min_pos
        if length > max_length:
            max_length = length

        return max_length
