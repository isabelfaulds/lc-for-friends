# sliding window - 2024-12-13
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlength = 0
        count = {}
        maxcount = 0
        for i in range(len(s)):
            # add to keys that dont exist - dict.get( key, 0)
            count[s[i]] = count.get(s[i], 0) + 1
            # calculate how many characters arent maxchar
            maxchar = max(count, key=count.get)
            window_size = i - l + 1
            others = window_size - count[maxchar]
            # print(maxchar, others)
            
            while others > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                length -= 1
                l += 1
                others -= 1
                # print('maxed out')
            length = i - l + 1
            maxlength = max(length, maxlength)
            # print(maxlength)

        return maxlength
        

# o of n complexity
# o of 1 memory
    # choose up to k number of character & change to 1 other for max repeating length


# sliding window with frequency array - 2025-1-3

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_array = [0] * 26
        max_freq = 0
        l = 0
        max_length = 0

        for i in range(len(s)):
            letter_index = ord(s[i]) - ord('A')
            letter_array [ letter_index ] += 1
            max_freq = max(max_freq, letter_array[letter_index])

            while i - l + 1 - max_freq > k: # window size inclusive of i
                letter_array[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_length = max(max_length,i - l + 1)
            # print('final lengths', letter_array, 'new length', length, 'max length', max_length)
        return max_length
