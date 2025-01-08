# doesnt need o n log n sort() , could do o n
# using a separate array would help with non over lapping middle intervals

# could use binary search for finding location
# could use 2 pointer for in place modification
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        result = []
        i = 0

        # half pass
        while i < len(intervals) and intervals[i][1] < newInterval[0] :
            print(i)
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            # Merge intervals by updating the newInterval's start and end
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result