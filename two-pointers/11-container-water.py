class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 , p2 = 0  , len(height) - 1
        maxarea = 0
        while p1 < p2:
            w = p2 - p1
            if height[p2] < height[p1]:
                maxarea = max(height[p2] * w , maxarea)
                p2 -= 1
            else: 
                maxarea = max(height[p1] * w , maxarea)
                p1 += 1
        return maxarea