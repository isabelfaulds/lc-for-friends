# bottom up
# max(coins) for n balloons
# coins ith balloon = nums[i - 1 if i > 0 else 1] * numns[i] * nums[i + 1 if i < len(nums) - 1 else 1] ;
# i no longer available as if nums.pop(i)
# breaking len(nums) balloons in subarrays
class Solution:
    def print_dp(self, dp, nums):
        '''
        printing dp table
        '''
        n = [str(i) for i in nums]
        i = 0
        print('  ', '  '.join([str(i) for i in nums]) )
        for r in dp:
            print(n[i], r)
            i += 1

    def maxCoins(self, nums: List[int]) -> int:
        # array size is nums squared
        # add borders
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for i in nums]

        for length in range(2, n):  # increasing sub array lengths
            for i in range(n - length):
                j = i + length  # ending index
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], 
                                    dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                    
        # # Iterate the input array in reverse order to fill the dp table
        # for i in range(n-2, -1, -1):
        #     for j in range(i+2, n):
        #         # Iterate k from i+1 to j-1 to find the last balloon to burst
        #         for k in range(i+1, j):
        #             # Compute the maximum coins for subproblems
        #             dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
        
    
        # self.print_dp(dp, nums)
        return dp[0][n-1]
        