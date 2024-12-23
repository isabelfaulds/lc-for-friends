
# Last in First Out
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        output = True
        testy = list(s)
        
        valids = {
            "{" : "}",
            "[" : "]",
            "(" : ")",
        }

        stack = []
        while len(testy) > 0:
            current = testy.pop(0)
            print(current)
            
            if stack:
                if current == valids[stack[-1]]:
                    stack.pop(-1)
                    continue
            if current in [")", "}", "]"]:
                output = False
                break
            stack.append(current)
            # print('stack ', stack, 'testy ', testy)
        
        if len(stack) > 0:
            output = False

        return output
    


# Last in First Out
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        valids = {
            "{" : "}",
            "[" : "]",
            "(" : ")",
        }
        
        stack = []
        
        for current in s:
            if current in valids:  # Opening bracket
                stack.append(current)
            elif current in valids.values():  # Closing bracket
                if not stack or valids[stack.pop()] != current:
                    return False
        
        return len(stack) == 0  # If stack is empty, the string is valid    