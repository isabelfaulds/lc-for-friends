# one stack (stack_1) to handle the push operation and the other (stack_2) to handle the pop and peek operations, simulating FIFO behavior.

# pop last is faster than pop first
# insert last is faster than insert first
# loop to achieve last index actions
# len() is an attribute of list and not a time constraint to perform

class MyQueue:

    def __init__(self):
        self.stack_1 = [] # push stack
        self.stack_2 = [] # pop peek stack

    def push(self, x: int) -> None:
        # self.stack_1 = [x] + self.stack_1 - creates a new list everytime
        # self.stack_1.insert(0, x) - causes reindexing everytime
        if self.stack_2 and not self.stack_1:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop(-1))
        self.stack_1.append(x)
        return None
                

    def pop(self) -> int:
        if self.stack_1 and not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop(-1))
            return self.stack_2.pop(-1)
        elif self.stack_2 and not self.stack_1:
            return self.stack_2.pop(-1)

    def peek(self) -> int:
        if not self.stack_2 and self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop(-1))
            return self.stack_2[-1]

        if self.stack_2 and not self.stack_1:
            return self.stack_2[-1]
        
    def empty(self) -> bool:
        return ( len(self.stack_1) + len(self.stack_2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()