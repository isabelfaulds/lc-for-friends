
generalized_manachers = '''
```python
       s_new = '#' + '#'.join(s) + '#'
        n = len(s_new)
        # dynamically resizing list during algorithm can add overhead in python, preallocating fixes length & ensures access
        manachers_array = [0] * n
        # Center and right boundary of the current palindrome
        center, right = 0, 0 # left is always center * 2 - right

        
        # first & last are always 1 , also helps out of bounds handling
        for i in range(1, n - 1):
            # i is i - center from the center, the mirror is equal distance away center - ( i - center )
            mirror = 2 * center - i
            
            # If we are within saved palindrome
            if i < right:
            # the starting estimate of the radius can be the mirror value radius , as long as it's still within the current palindrome boundary
                manachers_array[i] = min(  manachers_array[mirror], right - i )
            
            # if the index location + radius + buffer is less than the array length
            # & if the index location - radius - buffer is greater than array start
            while i + manachers_array[i] + 1 < n and i - manachers_array[i] - 1 >= 0:
                #then if the value outside the radius is equal on both sides 
                if s_new[i + manachers_array[i] + 1] == s_new[i - manachers_array[i] - 1]:
                    #the radius can be expanded
                    manachers_array[i] += 1
                # once a differing characters are found end
                else:
                    break
            
            # Update the center and right as the new palinddrome's if we've expanded past it
            if i + manachers_array[i] > right:
                center = i
                right = i + manachers_array[i]

        print(manachers_array)
```
'''

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        manachers_array = [0] * n  # Initialize with 1 (minimum palindrome length)
        palindrome_lengths = [1] * n
        center = 0
        right = 0
        for i in range(1, n-1):  # Skip first and last characters - default to 1
            mirror = 2 * center - i # center - ( center - i )
            
            if i < right: # if within saved palindrome
                manachers_array[i] = min(manachers_array[mirror], right - i ) # use the mirror value as initial estimate up to the boundary of the palindrome

            # while the index + radius is within the length of the array and the index - radius is within the start of the array, and values distance radius from i are symmetrical, include buffer of 1 to access radius values instead of index
            while i + 1 + manachers_array[i] < n and i - 1 - manachers_array[i] >= 0 and s[i-1-manachers_array[i] ] == s[i+1+manachers_array[i]]:
                # increase the radius
                manachers_array[i] += 1
                palindrome_lengths[i] += 2

            # if the right most of the radius is outside the saved update saved palindrome
            if right < i + manachers_array[i]:
                center = i
                right = i + manachers_array[i]
        print('manachers_array', manachers_array)
        print('palindrome_lengths' , palindrome_lengths)

# Hint 2 - After using Manacher's for each center use a line sweep from the center to the left and from the center to the right to find for each index the farthest center to it with distance ≤ palin[center]
# Hint 3 - After that, find the maximum palindrome size for each prefix in the string and for each suffix and the answer would be max(prefix[i] * suffix[i + 1])

        # Step 3: Calculate prefix and suffix arrays
        # prefix array - maximum length of a palindrome that can end at or before each index
        prefix = [0] * n
        # suffix array - maximum length of a palindrome that can start at or after each index
        suffix = [0] * n

        # Fill prefix array
        # Local optimal choices create global optimum
        # Greedy maximizer at each step retains the largest value
        # each i compares with 1 before and keeps max
        for i in range(n):
            # save the length of the largest palindrome at the right most index
            prefix[ i + manachers_array[i] ] = max( prefix[i + manachers_array[i] ], 2 * manachers_array[i]+1 )
            # save the length of the largest palindrome at the left most index
            suffix[ i - manachers_array[i] ] = max( suffix[i - manachers_array[i] ], 2 * manachers_array[i]+1  )

        # print('prefix ', prefix)
        # print('suffix ', suffix)
        
        for i in range(1, n): 
            prefix[~i] = max(prefix[~i], prefix[~i+1]-2)
            suffix[i] = max(suffix[i], suffix[i-1]-2)
        # print('prefix ', prefix)
        # print('suffix ', suffix)
        
        for i in range(1, n): 
            prefix[i] = max(prefix[i-1], prefix[i])
            suffix[~i] = max(suffix[~i], suffix[~i+1])
        # print('prefix ', prefix)
        # print('suffix ', suffix)


        return max(prefix[i-1]*suffix[i] for i in range(1, n))