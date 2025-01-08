"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# cleaned up
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flattening and sorting a nested list
        flattened = sorted(
            (timeslot for i in schedule for timeslot in i),
            key=lambda x: x.start
        )

        # merging
        write_index = 0
        for i in range(1, len(flattened)):
            if flattened[write_index].end >= flattened[i].start:
                flattened[write_index].end = max(flattened[write_index].end, flattened[i].end)
            else:
                write_index += 1
                flattened[write_index] = flattened[i]
        flattened = flattened[:write_index + 1]

        # grabbing results
        result = []
        for i in range(1, len(flattened)):
            result.append(Interval(flattened[i-1].end, flattened[i].start))
        return result


# 1 - 50 employees
# construct new interval object
# flatten, sort all intervals
# merge overlapping intervals
# identify gaps between merged intervals
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flattening and sorting a nested list
        flattened = []
        for i in schedule:
            for timeslot in i:
                flattened.append(timeslot)
        flattened = sorted(flattened, key = lambda x: x.start)

        # merging
        write_index = 0
        for i in range(1, len(flattened)):
            if flattened[write_index].end >= flattened[i].start:
                flattened[write_index].end = max(flattened[write_index].end, flattened[i].end)
            else:
                write_index += 1
                flattened[write_index] = flattened[i]
        flattened = flattened[:write_index + 1]

        # grabbing results
        result = []
        last_index = 0
        for i in range(1, len(flattened)):
            result.append( Interval(
                    flattened[last_index].end,
                    flattened[i].start)
                    )
            last_index += 1
        return result

