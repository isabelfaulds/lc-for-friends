class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        start = 0
        maxlength = 0
        length = 0
        for i in range(len(s)):
            while s[i] in letters:
                # print(s[i] , 'in letters, popping' , s[start])
                letters.pop(s[start])
                length -= 1
                start += 1
            # print(s[i], 'adding')
            letters[ s[i] ] = 1
            length += 1
            # print(length, 'length')
            if length > maxlength:
                maxlength += 1
        return maxlength
            
            
                
                
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = {}
#         L = 0
#         maxSum = 0

#         for R in range(len(s)):
#             if s[R] in count and count[s[R]] >= L:
#                 L = count[s[R]] + 1
            
#             count[s[R]] = R

#             maxSum = max(maxSum, R - L + 1)
#         return maxSum
        