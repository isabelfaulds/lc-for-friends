# non leetstream

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_s = '#' + '#'.join([y for y in s]) + '#' # processed str
        n = len(p_s)

        manachers_array = [0] * n
        center = 0
        right = 0
        max_manachers = 0
        max_palindrome_substr = None

        for i in range(1, n - 1):
            mirror = center - ( right - center )
            palindrome_substr = p_s[i]
            print(i, palindrome_substr )
            if right > i: # inital estimate , manachers array mirror up to the length of the right most boundary
                manachers_array[i] = min( manachers_array[mirror] , right - i )
            
            while i + manachers_array[i] + 1 < n and i - manachers_array[i] - 1 >= 0 and p_s[ i - 1 - manachers_array[i] ] == p_s[i + 1 + manachers_array[i] ]:
                manachers_array[i] += 1

            if i + manachers_array[i] > right:
                center = i
                right = i + manachers_array[i]

            print(manachers_array[i])
            if manachers_array[i] > max_manachers:
                print('update', manachers_array[i] )
                max_manachers = manachers_array[i]
                max_palindrome_substr = p_s[ i - manachers_array[i] + 1 : i + manachers_array[i] : 2] 
                print(max_palindrome_substr)

        return max_palindrome_substr