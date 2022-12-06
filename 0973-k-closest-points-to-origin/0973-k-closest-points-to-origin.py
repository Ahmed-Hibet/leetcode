class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        i = 0
        for x, y in points:
            distance.append(((x**2 + y**2)**.5, i))
            i += 1
        distance.sort()
        output = []
        for j in range(k):
            output.append(points[distance[j][1]])
        return output
