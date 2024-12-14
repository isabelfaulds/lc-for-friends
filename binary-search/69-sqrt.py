class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        while l <= r:
            m = (l + r ) // 2 
            if m ** 2 == x:
                return m
            print(l, r, m)
            r = (m - 1 ) if m ** 2 > x else r
            l = (m + 1) if m ** 2 < x else l

        print(m)
        return r