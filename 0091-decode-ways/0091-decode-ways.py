class Solution:
    def handleZeros(self, s: str) -> str:
        result = ''
        skip = False

        for i in s[::-1]:
            if skip:
                if i not in '12':
                    return ''
                skip = False
                continue
            if i == '0':
                skip = True
            result += i
        if skip:
            return ''
        return result[::-1]

    def numDecodings(self, s: str) -> int:
        zero_handled = self.handleZeros(s)

        if not zero_handled:
            return 0
        length = len(zero_handled)
        first, second= (1, 1)

        if length > 1 and zero_handled[0] != '0' and zero_handled[1] != '0' and int(zero_handled[0:2]) <= 26:
            second = 2

        for i in range(2, length):
            if zero_handled[i-1] != '0' and zero_handled[i] != '0' and int(zero_handled[i-1:i+1]) <= 26:
                second += first
                first = second - first
            else:
                first = second
        return second
                
