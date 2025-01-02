
# for element in the nums array it's a 2 sum problem to get the inverse

# easiest to work on sorted array
    # .sorted() preferable
        # merge sort (o n log n) or quick sort (o n log n -> o n 2) also potential options
# using a hash map not as useful due to multiple indices to track locations from


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valids = set()


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p1 , p2 = i + 1 , len(nums) - 1
            while p1 < p2:
                total = nums[i] + nums[p1] + nums[p2]
                if total == 0:
                    valids.add((nums[i], nums[p1], nums[p2]))
                  # Skip duplicates for p1
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    # Skip duplicates for p2
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    # Move both pointers after finding a valid triplet
                    p1 += 1
                    p2 -= 1
                elif total < 0:
                    p1 += 1
                elif total > 0:
                    p2 -= 1
        return list(valids)


## first attempt before optimizing so bad
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valids = set()

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            p1 , p2 = i + 1 , len(nums) - 1
            while p1 < p2:

                complement = nums[p1] + nums[p2]
                if complement < nums[i] * -1:
                    p1 += 1
                elif complement > nums[i] * -1:
                    p2 -= 1
                else:
                    if i < p1:
                        valids.add( ( nums[i], nums[p1], nums[p2] ) )
                    elif i > p2:
                        valids.add( ( nums[p1], nums[p2], nums[i] ) )
                    else:
                        valids.add( ( nums[p1], nums[i], nums[p2] ) )
                    p2 -= 1
        return list(valids)

        
        