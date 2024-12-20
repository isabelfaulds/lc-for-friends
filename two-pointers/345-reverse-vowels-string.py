class Solution:
    # manipulating elements at opposite ends of a sequence - two pointer
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = ['a','e','i','o','u']
        newleftstr = ''
        newrightstr = ''
        if r == 0:
            return s
    
        if r == 1:
            if s[0].lower() in vowels and s[1].lower() in vowels:
                return s[1] + s[0]
            else:
                return s

        while l <= r:
            # print(s[l].lower() , s[r].lower())
            if l != r and (s[l].lower() in vowels) and (s[r].lower() in vowels):
                # print(l, r, newleftstr, newrightstr)
                newleftstr = newleftstr + s[r]
                newrightstr = s[l] + newrightstr
                l += 1
                r -= 1
                # print(l, r, newleftstr, newrightstr, 'matched')
                continue

            if s[l].lower() in vowels:
                # print(l, r, newleftstr, newrightstr, 'moved left')
                newrightstr = s[r] + newrightstr
                r -= 1
                # print(l, r, newleftstr, newrightstr, 'moved left')
                continue

            if s[r].lower() in vowels:
                # print(l, r, newleftstr, newrightstr, 'moved right')
                newleftstr = newleftstr + s[l]
                l += 1
                # print(l, r, newleftstr, newrightstr, 'moved right')
                continue

            if r == l:
                newleftstr = newleftstr + s[l]
                # print(l, r, newleftstr, newrightstr, 'last one')
                break
            
            else:
                # print(l, r, newleftstr, newrightstr, 'moved both')
                newleftstr = newleftstr + s[l]
                newrightstr = s[r] + newrightstr
                l += 1
                r -= 1
                # print(l, r, newleftstr, newrightstr, 'moved both')
                continue


        return newleftstr + newrightstr