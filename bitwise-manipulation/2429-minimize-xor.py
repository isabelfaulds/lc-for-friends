def minimize_xor(num1, num2):
    # Format the binary representations as 30-bit strings for same lengths
    bin1 = format(num1, '030b')
    bin2 = format(num2, '030b')
    bits = sorted(bin2) # have 0s on head & 1s on tail , o n log n
    result = []
    for b in bin1:
        if b == '0':
            result.append(bits.pop(0)) 
        else:
            result.append(bits.pop()) # o 1
    
    return int(''.join(result), 2)

# there is only 1 integer that satisfies the conditions
# have least difference with num2
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1_str = bin(num1)[2:]
        bin2_bit_count = bin(num2).count('1')
        bin1_bit_count = bin(num1).count('1')
        if bin2_bit_count == bin1_bit_count:
            return num1

        new_str = []
        for i, s in enumerate(bin1_str):
            if bin2_bit_count > 0 and s == '1':
                new_str.append('1')
                bin2_bit_count -= 1
            else:
                new_str.append('0')

        for i in range(len(new_str) - 1 , -1 , -1 ):
            if new_str[i] == '0' and bin2_bit_count > 0:
                new_str[i] = '1'
                bin2_bit_count -= 1

        for i in range(bin2_bit_count):
            new_str.append('1')

        return int(''.join(new_str), 2)
