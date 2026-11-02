number = 0b10110110

print("a) Rotate Left without Carry (ROL)")
print("Original number:", format(number, '08b'))

for i in range(2):
    msb = (number >> 7) & 1
    number = ((number << 1) & 255) | msb
    print("Step", i + 1, ":", format(number, '08b'))

print("Final ROL result:", format(number, '08b'))

print()

# Rotate Left with Carry (RCL)
number = 0b10110110
carry = 0

print("b) Rotate Left with Carry (RCL)")
print("Original number:", format(number, '08b'))
print("Initial carry:", carry)

for i in range(2):
    msb = (number >> 7) & 1
    number = ((number << 1) & 255) | carry
    carry = msb
    print("Step", i + 1, ":", format(number, '08b'),
          "Carry:", carry)

print("Final RCL result:", format(number, '08b'))
print("Final carry:", carry)                                               


a) Rotate Left without Carry (ROL)
Original number: 10110110
Step 1 : 01101101
Step 2 : 11011010
Final ROL result: 11011010

b) Rotate Left with Carry (RCL)
Original number: 10110110
Initial carry: 0
Step 1 : 01101100 Carry: 1
Step 2 : 11011001 Carry: 0
Final RCL result: 11011001
Final carry: 0
