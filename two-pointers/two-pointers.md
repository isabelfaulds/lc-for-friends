#### Fast and Slow Pointers
- move in same direction
- slow reference pointer and fast current pointer
- [linked list cycle](two-pointers/fast_slow_pointers/141-linked_list_cycle.py) ratio 2:1 moves

```python
reference_pointer = 0 
current_pointer = 1 # 0 already known

while current_pointer < len(test_array) + 1:
    current_pointer += 1 # could be 2 steps per iteration

    if reference_pointer:
        reference_pointer += 1 # could be 0-1 steps per iteration

```

#### Opposite Converging Pointers
- move in converging direction
- move pointer of preferred value inwards
- optimize by skipping duplicate start / end pointers
- [Squares Sorted Array](./977-squares-sorted-array.py)
- [3 Sum](./15-3sum.py)

Conditional logic, like if a string == a string
```python
start_pointer = 0
end_pointer = len(test_array) - 1

while start_pointer < end_pointer:
    # or i in range(n, -1, -1) etc
    if test_array[end_pointer]: # preference for left
        ...
        end_pointer -= 1

    elif test_array[start_pointer] and not test_array[end_pointer]:
        ...
        start_pointer += 1
```

Comparing against a value
- Increment p1 if too small
- Increment p2 if too large
```python
while p1 < p2:
    if result < target:
        p1 += 1
    if result > target
        p2 -= 1
```

If inclusive of a range of values
- Count up the indexes between p2 & p1
```
while p1 < p2:
    val = func(p1,p2)
    if val < target:
        count += (p2 - p1)
        p1 += 1
```



####  Reversed Comparison Pointers
```
```

#### Sliding Window
[Sliding Window](../sliding-window/sliding-window.md)



