class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
# sorting necessary - O(n log n)
        nums.sort()
        result = float('inf')
        for p in range( len(nums) - 2): # need 2 ints
            if p > 0 and nums[p] == nums[p - 1]: # skip duplicates
                continue
            p1, p2 = p + 1 , len(nums) - 1

            while p1 < p2:
                summed= nums[p] + nums[p1] + nums[p2]
                if abs(summed - target) < abs(result - target):
                    result = summed
                if summed < target:
                    p1 += 1
                elif summed > target:
                    p2 -= 1
                else:
                    return target

        return result

