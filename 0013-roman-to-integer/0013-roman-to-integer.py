roman = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        ln = len(s)
        i = 0
        while i < ln:
            if i != ln - 1 and s[i:i+2] in roman:
                num += roman[ s[i:i+2] ]
                i += 2
            else:
                num += roman[ s[i] ]
                i += 1
        return num