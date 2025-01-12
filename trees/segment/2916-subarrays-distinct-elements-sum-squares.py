# https://cp-algorithms.com/data_structures/segment_tree.html

# TODO: add ipad pdf diagram in same folder
# # for each subarray end increase by 1 the value sum ∑(   )
# logarithmic complexity - In a segment tree, you structure the data in such a way that each node represents a range of elements (a segment). When you perform an update, you don't need to go through all the elements in that segment. Instead, you use the stored values at the nodes and propagate the update efficiently.
# adding a lazy value k to all elements in a segment looks like new sum = old sum + k * n

class SegmentTree:
    def __init__(self, arr: list[int], l: int, r: int):
        self.l, self.r = l, r
        self.lazy = 0
        if l == r: # individual leaf node
            self.left = self.right = None
            self.sum = arr[l]
            self.squareSum = self.sum ** 2
        else: # split children from mid index
            mid = (r + l) // 2
            self.left = SegmentTree(arr, l, mid) # passing the full array without slicing allows children nodes to share same object in memory
            self.right = SegmentTree(arr, mid + 1, r)
            # use children aggregate values
            self.sum = self.left.sum + self.right.sum 
            self.squareSum = self.left.squareSum + self.right.squareSum

    def queryRange(self, l: int, r: int):
        ''' queries the square sum aggregate '''
        if l <= self.l and self.r <= r:
            return self.squareSum
        elif self.l > r or self.r < l:
            return 0
        else:
            return self.left.queryRange(l, r) + self.right.queryRange(l, r)
    
    def update(self, l: int, r: int, k: int =1):
        '''
        :param l: the left boundary update range of original .update()
        :param r: the right boundary update range .update()
            - can be initial root call root.update(start , end) - 
                - partial boundary update unless root.update(self.l, self.r) - updates whole tree array
            - can be recursive node call self.update(self.l, self.r, k)
                - for updating the node aggregations using stored lazy value
            - can be call spreading out updates left_child.update(l , r) where l and r are original parent boundaries
        :param k: (standard name for a multiplier constant) , default value 1 from problem context
        add follows 3
        '''

        print(f'adding left {l}, right {r} , k {k} , selfk {self.lazy}')
        print(f'for self.l {self.l}, self.r {self.r} , k {k} , selfk {self.lazy}')

        # lazy value update
        if self.lazy > 0:
            print(f'self lazy value in {self.l , self.r} - lazy { self.lazy}')
            selfK = self.lazy
            self.lazy = 0
            print(f'self lazy value {self.l , self.r} - .update({self.l, self.r}) { self.lazy}')
            self.update(self.l, self.r, selfK)

        # current segment in update range l , r
        if l <= self.l and self.r <= r:
            print('current segment in update range')
            print(f'l {l} value <= {self.l} r value <= {self.r} - lazy { self.lazy}')
            print(f'l {l} value <= {self.l} r value <= {self.r} - calc self.squaresum')

            # o log n complexity of updates for bc not iterating through elements, leveraging self.sum , self.squaresum & k
            # explainer of calculation at bottom of code
            # self.squareSum = ( self.squareSum ) + ( 2 * k * self.sum ) + ( k**2 * (self.r - self.l + 1))
            self.squareSum += (2 * k * self.sum + k * k * (self.r - self.l + 1))
            print(f'l {l} value <= {self.l} r value <= {self.r} - add to self.sum')
            # k times size of the range of indexes
                # k, lazy value being added to each element
            self.sum += k * (self.r - self.l + 1)
            
            # increase child lazy values
            if self.left != None:
                print(f'increase left child lazy += k {k}')
                self.left.lazy += k
            if self.right != None:
                print(f'increase right child lazy += k {k}')
                self.right.lazy += k

        # segment outside update range nonevent
        elif self.l > r or self.r < l:
            print(f'l {l} value > {self.r} self.r value , r {r} value < {self.l} - outside segment, end')
            return

        # partial update event
        # segment partially overlaps range , either left boundary or right boundary outside
        # so it'll be called on both the left and right children
            # child might return early portion completely out of bounds
            # child might call children recursively downards if also partial
            # child might create lazy value for children
        else:
            self.left.update(l, r, k)  
            self.right.update(l, r, k)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum

### Printing Debugging Functions

    def printNode(self):
        '''Print node's details'''
        print(f"Node range: l {self.l} - r {self.r}")
        print(f"  sum: {self.sum}")
        print(f"  squareSum: {self.squareSum}")
        print(f"  lazy: {self.lazy}")

    def printTree(self):
        '''Recursive function to print the entire tree'''
        self._printTree(self)

    def _printTree(self, node):
        '''Helper function for traversal'''
        if node is None:
            return
        node.printNode()
        if node.left:
            self._printTree(node.left)
        if node.right:
            self._printTree(node.right)

class Solution:          
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        MOD = 10**9+7
        n = len(nums)
        root = SegmentTree([0] * n , 0 , n - 1) # Instantiate all nodes
        # root.printTree()
        prev_seen = {} # last occurance

        for i , curr_num in enumerate(nums):
            # print('\n i', i, 'curr_num', curr_num)
            start , end = prev_seen.get(curr_num , -1 ) + 1  , i
                # subarray count distinct doesnt change with addition of same number, change start window to after last of an instance or 0
            # print('\n start', start, 'end', end)
            root.update(start, end)
            # root.printTree()
            result = (result + root.queryRange(0, n - 1)) % MOD
            prev_seen[curr_num] = i

        return result


# square sum calc details
# self.squareSum = ( self.squareSum ) + ( 2 * k * self.sum ) + ( k**2 * (self.r - self.l + 1))
# from (a+b)**2 = a**2 + 2ab + b**2 
# sum of squares is n∑i=1(x_i**2)
# adding k to each element 
    # x plus k squared (x_i + k)**2 =becomes xi**2 + 2kx_i + k**2 
        # ie (a+b)**2 = a**2 + 2ab + b**2 
    # sum of every element n∑i=1( element ) , n∑i=1( x_i**2 ) becomes n∑i=1( every element with k ) , n∑i=1( x_i**2 + 2kx_i + k**2)
    # n∑i=1( x_i**2 + 2kx_i + k**2) expanded this looks like

        #  n∑i=1( x_i**2 ) +
            # a**2 in sum of squares
            # n∑i=1( x_i**2 ) - current square sum , self.squareSum
        # 2 * n∑i=1( x_i ) * k
            # 2ab in sum of squares
            # n∑i=1( x_i ) - current sum , self.sum 
        # n * k**2
            # sum of constant squared
            # k is added n times
            # n = self.r - self.l + 1
        # ( self.squareSum ) + ( 2 * k * self.sum ) + ( k**2 * (self.r - self.l + 1) )


#### 2nd attempt
# this is just barely not optimized enough
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

## 1st attempt sliding window, failed in time complexity
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


####### passes
class SegmentTree:
    def __init__(self, arr: list[int], l: int, r: int):
        self.lazy = 0
        self.l, self.r = l, r
        if l == r:
            self.left = self.right = None
            self.sum = arr[l]
            self.squareSum = arr[l] ** 2
        else:
            mid = (r + l) // 2
            self.left = SegmentTree(arr, l, mid)
            self.right = SegmentTree(arr, mid + 1, r)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum
    
    def getSquareSum(self, l: int, r: int):
        if l <= self.l and self.r <= r:
            return self.squareSum
        elif self.l > r or self.r < l:
            return 0
        else:
            return self.left.getSquareSum(l, r) + self.right.getSquareSum(l, r)
    
    def add(self, l: int, r: int, k: int =1):
        '''f
        :param l: the left boundary update range of original .add()
        :param r: the right boundary update range .add()
            - can be initial root call root.add(l , r)
            - can be recursive node call self.add(self.l, self.r, k)
            - can be call spreading out updates left_child.add(l , r) where l and r are original parent boundaries
        :param k: (standard name for a multiplier constant) , default value 1 from problem context
        '''

        print(f'adding left {l}, right {r} , k {k} , selfk {self.lazy}')
        print(f'for self.l {l}, self.r {r} , k {k} , selfk {self.lazy}')

        # pending update
        if self.lazy > 0:
            print(f'self lazy value in {self.l , self.r} - lazy { self.lazy}')
            selfK = self.lazy
            self.lazy = 0
            print(f'self lazy value {self.l , self.r} - .add({self.l, self.r}) { self.lazy}')
            self.add(self.l, self.r, selfK)

        # current segment in update range l , r
        if l <= self.l and self.r <= r:
            print(f'l {l} value <= {self.l} r value <= {self.r} - lazy { self.lazy}')
            print(f'l {l} value <= {self.l} r value <= {self.r} - calc self.squaresum')
            self.squareSum += (2 * k * self.sum + k * k * (self.r - self.l + 1))
            print(f'l {l} value <= {self.l} r value <= {self.r} - add to self.sum')
            self.sum += k * (self.r - self.l + 1)
            
            # increase child lazy values
            if self.left != None:
                print(f'increase left child lazy += k {k}')
                self.left.lazy += k
            if self.right != None:
                print(f'increase right child lazy += k {k}')
                self.right.lazy += k

        # segment outside update range
        elif self.l > r or self.r < l:
            print(f'l {l} value > {self.r} self.r value , r {r} value < {self.l} - outside segment, end')
            return
        # segment partially overlaps range , either left boundary or right boundary outside
        else:
            self.left.add(l, r, k)  
            self.right.add(l, r, k)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum
