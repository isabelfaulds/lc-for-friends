# Testing ability to coneptualize idea of randomness without using built in functions like math.random()

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.wa = [ sum(w[:i + 1]) for i in range(len(w) )]

    def pickIndex(self) -> int:
        target = random.randint(1 , self.wa[-1])
        index = self.lowerBinarySearch(target)
        return index

# Used for finding the first index where target is at least the cumulative sum at the index
    def lowerBinarySearch(self, target):
        l , r = 0, len(self.wa) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.wa[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
        
        # not suitable, isnt inclusive of the target
    # def upperBinarySearch(self, target):
    #     l , r = 0, len(self.wa) - 1
    #     while l < r:
    #         print(l , r)
    #         mid = l + (r - l) // 2
    #         if self.wa[mid] > target:
    #             r = mid
    #         else:
    #             l = mid + 1
    #     return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()