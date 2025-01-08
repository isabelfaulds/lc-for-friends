# sort
# iterate through sorted and merge overlapping
    # if current overlaps with previous, merge otherwise add interval to the result

# in place with write index
# sorting o n log n
# merging o n
# space o 1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        write_index = 0  # Tracks the position to overwrite
        
        for i in range(1, len(intervals)):
            if intervals[write_index][1] >= intervals[i][0]: # current interval shares with previous
                intervals[write_index][1] = max(intervals[write_index][1], intervals[i][1]) # max end
            else:
                # able to continue moving writing
                write_index += 1
                intervals[write_index] = intervals[i]
        
        return intervals[:write_index + 1]

# with result array cleaned
# sorting o n log n
# merging o n
# space o n
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for i in intervals[:]:
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result

# first attempt with result array
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start_i = intervals[0][0]
        end_i = intervals[0][1]
        result = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= result[-1][0] or i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
                # result[-1][1] = i[1]
            else:
                result.append(i)
        return result          