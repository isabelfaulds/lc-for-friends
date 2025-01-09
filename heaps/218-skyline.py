# merging overlapping intervals
# storing min x for each max y
    # zeroes at right point, not interested in max height at right, showing new min
    # could use a min heap like a max heap with negative values

# constraints -
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
    # doesnt make sense to make a complete x axis array 
# 1 <= heighti <= 2^31 - 1

import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline_result = []
        corner_points = [0] * 2 * len(buildings)
        for i, b in enumerate(buildings):
            left, right, height = b
            corner_points[i * 2] =  (left, -height, right )
            corner_points[i * 2 + 1] = (right, 0, None )
        corner_points.sort(key=lambda x: (x[0], x[1]))

        neg_heap = [(0, float('inf'))]
        for i in corner_points:
            left, neg_height, right = i
            while neg_heap[0][1] <= left:             # move past buildings with right point before / at (zeroes at @ current) corner left point
                heapq.heappop(neg_heap)
            if neg_height != 0:
                heapq.heappush(neg_heap, (neg_height, right))
            height_at_left = -1 * neg_heap[0][0] # keeping the value, not heappop
            
            if not skyline_result or skyline_result[-1][1] != height_at_left:
                skyline_result.append( [left , height_at_left])


            
        return skyline_result