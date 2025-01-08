### should only be 1 pass s , 1 pass of stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Stack to track the indices of unmatched opening parentheses
        stack = []
        result = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(len(result))  
                result.append(char)  
            elif char == ')':
                if stack:
                    stack.pop()
                    result.append(char)
                else:
                    continue
            else:
                result.append(char)

        for i in stack:
            result[i] = ''

        return ''.join(result)


### 1st attempt cleaned up
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = []
        removal = set()  # set has O(1) checking vs list for o(n)

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    removal.add(i)
                else:
                    stack.pop()

        removal.update(stack) # Add set elements from other iterable

        for i, char in enumerate(s):
            if i not in removal:
                result.append(char)

        return ''.join(result)


### 1st attempt
# stacks problem :)
# 1 pass to identify invalids, 1 to manipulate
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removal = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and not stack:
                removal.append(i)
            elif s[i] == ')' and stack:
                stack.pop()
            else:
                continue

        removal += stack
        # strings are immutable :) make a new string
        result = []
        for i,char in enumerate(s):
            if i not in removal:
                result.append(char)


        # [i for i in s if i not in removal]  O(n * m)
        return ''.join(result)
