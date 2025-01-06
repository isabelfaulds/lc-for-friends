class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        checking = s[0:10]
        spotted = {checking : 1 }
        repeated = []
        for i in range(10, len(s)):
            checking = checking[1:] + s[i]
            if checking not in spotted:
                spotted[checking] = 1
            elif spotted[checking] == 1:
                repeated.append(checking)
                spotted[checking] += 1
        return repeated