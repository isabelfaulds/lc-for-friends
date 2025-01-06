# Reverse first approach
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Iniital O of n then o(1) for function calls
        # Ensures optimization in later calls by offering first objs in last indices
        self.stack = nestedList[::-1]
        
    def next(self) -> int:
        # Needs hasNext() called first
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # Flatten the top of the stack until an integer is found
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            top = self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False