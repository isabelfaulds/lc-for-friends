Subarray Size Count
- can take r - l + 1 for index size
- l has to be able to pass r in condition for there to be -1 + 1 = 0 count

```
    while l <= r and val != k:
        func(val)
        l += 1
    count += (r - l + 1) 
```