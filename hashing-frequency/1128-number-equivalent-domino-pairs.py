
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def pair_formula(n):
            return int((n*(n-1))/2)
        
        seen={}
        for a, b in dominoes:
            # could also do min max but would take 2 checks
            k = int(str(a)+str(b)) if a > b else int(str(b)+str(a))
            # print(a, b , k)
            if k not in seen:
                seen[k] = 1
                continue
            seen[k] += 1
        # print(seen)
        n = sum([pair_formula(y) for y in seen.values() if y > 1])

        return n