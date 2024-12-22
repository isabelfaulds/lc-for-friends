
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