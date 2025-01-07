# order not important
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l , r = 0 , 0
        tmap = {}
        for i in t:
            if i not in tmap:
                tmap[i] = 0
            tmap[i] += 1
        slice_l = 0
        slice_r = 0
        # print('len', len(s), 'map', tmap)

        substr = ''
        while r < len(s):
            # print(r, s[r])

            if s[r] in tmap:
                tmap[s[r]] -= 1
                # print(s[r] , tmap)
            while sum([ y <= 0 for y in tmap.values()]) == len(tmap) :
                # print(substr, r , l)

                if len(substr) == 0 or r - l + 1 < len(substr):
                    substr = s[l:r + 1]
                    # print('new min - ', r , l, substr)
                if s[l] in tmap:
                    tmap[s[l]] += 1
                    # print('added back ' , s[l], tmap, sum([ y <= 0 for y in tmap.values()]) , len(tmap))
                l += 1
            
            r += 1

        return substr
