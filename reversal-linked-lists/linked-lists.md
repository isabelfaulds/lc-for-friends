Linked list as a data structure
- order of elements / nodes preserved
- flexible with how the elements are accessed and manipulated

```
Input: head = [1,2,3,4,5]
1-> 2 -> 3 -> 4 -> 5 -> None
```

Dummy nodes
- simplifies edge cases of list lengths
- used instead of starting prev = None

```
dummy = ListNode(0)
dummy.next = head
prev = dummy

return dummy.next
```



- A linked list can be reversed either iteratively or recursively
    - Iteratively
        - keep pointers of previous , current & next node
        - for each node reverse its pointer to point to the previous node
        - move previous & current forward
        - at end of loop head / prev will be of the previous last element
        - return previous last element as head
    - Recursively