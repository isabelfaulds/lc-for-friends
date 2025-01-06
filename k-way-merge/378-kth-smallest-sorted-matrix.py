# related paper on o(n) solution - http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf


# k way merge pattern o k log n
    # building heap - o n log n
    # extracting smallest element k - o k log n
    # insertions / deletions - o log n
    # space - o n

    # heap - tree based data structure
    # min-heap - binary heap , parent node always less than or equal to child nodes, smallest element at the root

# heap
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

# divide and conquer
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

# TODO: binary search on the value range
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

# multi pointer simple solution but not as efficient for large n^2
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pointers = [0] * n

        for _ in range(k):
            min_val = float('inf')
            min_row = -1

            for row in range(n):
                # < n for certain rows that are overly indexed
                if pointers[row] < n and matrix[row][pointers[row]] < min_val:
                    min_row = row
                    min_val = matrix[row][pointers[row]]
            pointers[min_row] += 1

        return min_val

