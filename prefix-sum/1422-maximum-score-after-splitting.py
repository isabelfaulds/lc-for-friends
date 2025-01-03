
# first attempt
    # only nit don't make int first
# prefix sum pattern problem
    # precompute values for one side
    # update counts in iterations
    # compute score & track max
class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1') # = number of ones in right
        left_zeros = 0 # = number of zeros in left
        max_score = 0
        scores = [0] * len(s)
        for i in range(len(s) - 1):
            new_left =  int(s[i])
            if new_left == 0:
                left_zeros += 1
            else:
                total_ones -= 1
            score = left_zeros + total_ones
            max_score = max(score, max_score)
        return max_score

# this file also in dp for dp practice

# other options - two pointer, sliding window, greedy, dynamic programming
# dynamic programming, less optimal
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        prefix_zeros = [0] * n
        suffix_ones = [0] * n
        
        for i in range( n ):
            prefix_zeros[i] = prefix_zeros[i - 1] + (1 if s[i] == '0' else 0) if i > 0 else (1 if s[i] == '0' else 0)
            
        for i in range( n - 1, -1 , -1 ):
            suffix_ones[i] = suffix_ones[i + 1] + ( 1 if s[i] == '1' else 0 ) if i < n - 1 else ( 1 if s[i] == '1' else 0 )

        max_score = 0
        for i in range(n - 1):
            score = prefix_zeros[i] + suffix_ones[i + 1]
            max_score = max(max_score, score)
        
        return max_score