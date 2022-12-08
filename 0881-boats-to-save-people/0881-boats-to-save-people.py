class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        boats = 0

        while start < end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                end -= 1
            boats += 1
        
        if start == end: boats += 1
        return boats
         
