
# segment tree practice
from collections import defaultdict
class SegmentTree:
    def __init__(self):
        ''' initialize data objects for node data , lazy data '''
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)
        self.max_tree_count = 0

    def update(self, idx, update_val, update_start, update_end, node_range_start, node_range_end):
        if node_range_end < update_start or node_range_start > update_end: 
            # print('return early', 'index', idx, 'update start', update_start, 'update end', update_end, 
                #   node_range_start, 'node range start', node_range_end, 'node range end')
            return # return early

        if node_range_start >= update_start and node_range_end <= update_end:
            # Full overlap: Apply the update to the node

        # Full overlap: Apply the update to the node

            self.tree[idx] += update_val
            self.lazy[idx] += update_val
            # print('full update' , 'update start', update_start, 'update end', update_end, 'node range start', node_range_start, 
                #   'node_range_end', node_range_end )
            return

        # partial
        mid = node_range_start + (node_range_end - node_range_start ) // 2
        # sparse segment tree structgure will spread out the indexes
        left_child = 2 * idx
        right_child = 2 * idx + 1

        outstanding_update = self.lazy.get(idx, None)
        if outstanding_update:
            for child in [left_child, right_child]:
                  # pushing down
                self.tree[child] += outstanding_update
                self.lazy[child] += outstanding_update
            del self.lazy[idx]

        self.update(left_child, update_val, update_start, update_end, node_range_start, mid )
        self.update(right_child, update_val, update_start, update_end, mid + 1, node_range_end )

        self.tree[idx] = max(self.tree[left_child] , self.tree[right_child])
        self.max_tree_count = min(self.tree[idx], self.max_tree_count) if update_val < 0 else max(self.tree[idx], self.max_tree_count)

    def update_add(self, idx, update_start, update_end, node_range_start, node_range_end):
        self.update(idx, 1, update_start, update_end, node_range_start, node_range_end )

    def update_remove(self, idx, update_start, update_end, node_range_start, node_range_end):
        self.update(idx, -1, update_start, update_end, node_range_start, node_range_end )
   
        

class MyCalendar:

    def __init__(self):
        self.calendar_tree = SegmentTree()

    def book(self, startTime: int, endTime: int) -> bool:
        self.calendar_tree.update_add(1, startTime, endTime-1, 0, 10**9)
        keep = self.calendar_tree.max_tree_count <= 1
        if not keep:
            self.calendar_tree.update_remove(1, startTime, endTime-1, 0, 10**9)

        return keep


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)