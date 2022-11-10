class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif not i % 3:
                answer.append("Fizz")
            elif not i % 5:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
