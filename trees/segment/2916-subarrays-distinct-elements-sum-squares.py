# https://cp-algorithms.com/data_structures/segment_tree.html

# TODO: will update this code & add pdf, diagramming how segment trees work
class Node:
    def __init__(self, square_sum=0, sum_=0):
        self.square_sum = square_sum
        self.sum = sum_

class SegmentTree:
    def __init__(self, n, mod):
        self.n = n
        self.MOD = mod
        self.tree = [Node() for _ in range(4 * n)]
        self.lazy = [0] * (4 * n)
        print([(i, "square sum", node.square_sum, "sum_" , node.sum )for i, node in enumerate( self.tree) ])

    def combine_node(self, a, b):
        square_sum = (a.square_sum + b.square_sum) % self.MOD
        sum_ = (a.sum + b.sum) % self.MOD
        return Node(square_sum, sum_)

    def lazy_update(self, l, r, i):
        if l != r:
            self.lazy[i * 2 + 1] += self.lazy[i]
            self.lazy[i * 2 + 2] += self.lazy[i]

        length = r - l + 1

        self.tree[i].square_sum = (
            self.tree[i].square_sum + (self.lazy[i] * self.tree[i].sum * 2) + (length * self.lazy[i] * self.lazy[i])
        ) % self.MOD
        self.tree[i].sum = (self.tree[i].sum + self.lazy[i] * length) % self.MOD

        self.lazy[i] = 0

    def add_one(self, x, y, l=0, r=None, i=0):
        if r is None:
            r = self.n - 1
        
        self.lazy_update(l, r, i)

        if r < x or l > y:
            return
        if l >= x and r <= y:
            self.lazy[i] = 1
            self.lazy_update(l, r, i)
            return

        m = (l + r) // 2
        self.add_one(x, y, l, m, i * 2 + 1)
        self.add_one(x, y, m + 1, r, i * 2 + 2)

        self.tree[i] = self.combine_node(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        MOD = int(1e9 + 7)
        MAX = int(1e5 + 1)
        prev = [-1] * MAX

        seg_tree = SegmentTree(n, MOD)
        ans = 0

        for i in range(n):
            start = prev[nums[i]] + 1
            end = i
            seg_tree.add_one(start, end)
            ans = (ans + seg_tree.tree[0].square_sum) % MOD
            prev[nums[i]] = i

        return ans

# sliding window, failed in time complexity
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        total_sum = 0
        for l in range(len(nums)):
            freq_map = {}
            distinct_count = 0
            for r in range(l, len(nums)):
                freq_map[nums[r]] = freq_map.get(nums[r], 0) + 1
                if freq_map[nums[r]] == 1:
                    distinct_count += 1
                total_sum += distinct_count ** 2
        return total_sum % (10**9 + 7)
    
