from collections import defaultdict
# some more simple segment tree practice
class SegmentTree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def query_max(self, idx, query_start, query_end, node_start, node_end,):
        #  outside
        if node_end < query_start  or node_start > query_end:
            return 0
        #  full
        if query_start <= node_start and node_end <= query_end:
            return self.tree[idx]
        # sum partial children
        else:
            mid = ( node_start + node_end ) // 2
            # mid = node_start + (node_end - node_start) //2 
            return max (
                self.lazy[idx] ,
                # left child
                self.query_max(2 * idx , query_start, query_end, node_start, mid) ,
                # right child
                self.query_max(2 * idx + 1, query_start, query_end, mid + 1, node_end)
            )

    def update(self, idx, update_start, update_end, node_start, node_end, update_value=1 ):
        #  outside
        if update_start > node_end or update_end < node_start:
            return # return early
        #  full
        if update_start <= node_start and node_end <= update_end:
            self.tree[idx] = max(self.tree[idx], update_value)
            self.lazy[idx] = max(self.lazy[idx], update_value)
        # send partial update
        else:
            mid = ( node_start + node_end ) // 2
            # left child
            self.update(2 * idx , update_start, update_end, node_start, mid, update_value) ,
            # right child
            self.update(2 * idx + 1, update_start, update_end, mid + 1, node_end, update_value)
            self.tree[idx] = max(
                self.lazy[idx],
                self.tree[idx * 2],
                self.tree[idx * 2 + 1]
            )



# query first to get potential max
# 1 update 
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        squares_tree = SegmentTree()
        res = []
        max_height = 0
        for left, sidelength in positions:
            right = left + sidelength - 1
            height = squares_tree.query_max(1, left, right, 0, 10**9)
            # print('queried height', height)
            # print('update sidelength', sidelength)
            squares_tree.update(1, left, right, 0, 10**9, height + sidelength)
            max_height = max(max_height, height + sidelength )
            res.append(max_height)
        return res


        