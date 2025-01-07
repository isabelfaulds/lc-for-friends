class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # if sum is < target, all pairs between p1 & p2 are valid
        nums.sort()
        count = 0
        for p in range( len(nums) - 2 ): # need at least 2

            p1 , p2 = p + 1 , len(nums) - 1

            while p1 < p2:
                summed = nums[p] + nums[p1] + nums[p2]
                
                if summed < target:
                    count += (p2 - p1)
                    p1 += 1
                else:
                    p2 -= 1
        return count