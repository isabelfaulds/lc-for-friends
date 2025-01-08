# using import math
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log_value = math.log(n,4)
        return log_value.is_integer()

# recursive
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(n)
        if n == 1:
            return True
        if n <= 0 or (n % 4) != 0: # negative or not divisible by 4
            return False
        return self.isPowerOfFour(n // 4)


# bit manipulation
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # always positive
        # power of 2
        # power of 4 in bits - 1 bit in n is at an odd position (the number is a power of four)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
#        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0