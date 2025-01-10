# dp bottom up complexity o m * n
class Solution:
    def print_dp(self, dp, s1, s2):
        '''
        printing dp table
        ie
        # 		a	c
        #   0	∞	∞
        # a	0	1	∞
        # b	0	2	∞
        # c	0	3	2
        '''
        ls1 = ' ' + s1
        i = 0
        print('     ', '     '.join(s2))
        for r in dp:
            print(ls1[i], r)
            i += 1

    def minWindow(self, s1: str, s2: str) -> str:
        m , n = len(s1) , len(s2)
        # dp[i][j] = min( len(  s1[ :i ] containing s2[ :j+1 ] ) )
        # column range(m + 1)[0] is base case = 0
        dp = [ [0 if j == 0 else float('inf') for j in range(n + 1)] for i in range(m + 1)]
            
        # iterate through s1 , fill rows ie [skip] , [a] , [b] , [c]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: # dp table is 1 indexed, check current ie i - 1
                    if dp[i-1][j-1] != float('inf'): # if prior needed in subsequence were captured
                        dp[i][j] = dp[i-1][j-1] + 1 # extend string length by 1
                else:
                    if dp[i - 1][j] != float('inf'):  # carry forward previous value
                        dp[i][j] = dp[i - 1][j] + 1 # extend by 1
        
        # find the min length in last column
        min_length , ending_index = float('inf') , -1
        for i in range(m + 1):
            if dp[i][n] != float('inf'):
                if dp[i][n] < min_length:
                    min_length = dp[i][n]
                    ending_index = i - 1
        starting_index = ending_index - min_length + 1
        
        return s1[starting_index:ending_index+1] if min_length != float('inf') else ""
