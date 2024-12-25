### Exact Occurence

#### Overflow Safe
```
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2  # Safe from overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

#### Non Overflow Safe
```
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2  # No overflow protection
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

```

#### First Occurence
```
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    result = -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            result = mid  # Found the target, but continue to search left
            r = mid - 1  # Move right boundary leftward to find first occurrence
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return result
```

#### Last Occurence
```
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    result = -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            result = mid  # Found the target, but continue to search right
            l = mid + 1  # Move left boundary rightward to find last occurrence
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return result

```

### Index Search
#### Lower Bound
- smallest index where the target could be inserted to maintain sorted order

```
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2  # Overflow safe
        if arr[mid] >= target: 
            r = mid
        else:
            l = mid + 1
    return l
```

#### Upper Bound
- largest index where the target could be inserted to maintain sorted order

```
def upper_bound(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l
```


#### Approximate
```
def binary_search(arr, target, epsilon=1e-6):
    l, r = 0, len(arr) - 1
    while r - l > epsilon:  # Continue until the difference is within precision
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l  # Return the closest position
```

#### Ternary
```
def ternary_search(arr, target):
    l, r = 0, len(arr) - 1
    while r - l > 2:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif arr[mid1] > target:
            r = mid1 - 1
        elif arr[mid2] < target:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1
```