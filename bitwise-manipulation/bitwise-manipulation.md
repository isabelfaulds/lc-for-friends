
#### Converting
```python
bin(num1) # ie 0b101
format(num1, '030b') # format as 30 bit
```
- formatting as 30 bit ensures same lengths across numbers

#### XOR
- bitwise `exclusive or` operation comparing corresponding bits of 2 numbers
- XOR = 1 - different bits
- XOR = 0 - same bits
- Higher bits are leftmost, lower bits are right most
    - Larger differences come from deviations in higher bits
    - ie "1000" ^ "0001" > "1000" ^ "0100"
- minimizing xor means binary representations align as closely as possible 
    - can use the higest bits of a value to construct another value compared to another
    - turn on bits to create a new value
    - if have to be placed, bits placed in lower positions will create smaller change


Example
```python
num1 = bin(3) # 0011 , 2 set bits
num2 = bin(5) # 0101 , 2 set bits
xor = 3 ^ 5
result = bin(xor)

```

- set bits: number of 1s in binary


- Swapping Two Variables Without Temp
```python
a, b = 5, 7
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # Output: 7, 5
```

- Finding Unique Element
```python
nums = [1, 2, 3, 2, 1]
unique = 0
for num in nums:
    unique ^= num
```