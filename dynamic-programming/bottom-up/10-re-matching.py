# dp bottoms up :cheers:
class Solution:
    def print_dp(self, dp, s1, s2):
        '''
        printing dp table
        ie
        # 		    a	
        #   False	False
        # a	False	True
        # a	False	True
        # a	False	True
        '''
        ls1 = ' ' + s1
        i = 0
        print('     ', '     '.join(s2))
        for r in dp:
            print(ls1[i], r)
            i += 1

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for i in range(m+1) ] # always + 1 for base / empty
        dp[0][0] = True

        # self.print_dp(dp, s, p)
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        # self.print_dp(dp, s, p)


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print('i:' , i, 'J:', j)
                if ( s[i-1] == p[j-1] ) or ( p[j-1] == '.' ):
                    # print(True)
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        self.print_dp(dp, s, p)
        
        return dp[len(s)][len(p)]



