a = 45
b = 19

print("Expression a: 45 - (+19)")
print("First operand:", format(a & 255, '08b'))
print("Second operand:", format(b & 255, '08b'))

b_comp = (~b + 1) & 255
result = (a + b_comp) & 255

print("2's complement of second operand:", format(b_comp, '08b'))
print("Result in binary:", format(result, '08b'))
print("Result in decimal:", result)
print("Overflow: No")

print()

# Expression b: (-35) - (-12)
a = -35
b = -12

print("Expression b: (-35) - (-12)")
print("First operand:", format(a & 255, '08b'))
print("Second operand:", format(b & 255, '08b'))

b_comp = (~b + 1) & 255
result = (a + b_comp) & 255

if result >= 128:
    decimal_result = result - 256
else:
    decimal_result = result

print("2's complement of second operand:", format(b_comp, '08b'))
print("Result in binary:", format(result, '08b'))
print("Result in decimal:", decimal_result)
print("Overflow: No")

Expression a: 45 - (+19)
First operand: 00101101
Second operand: 00010011
2's complement of second operand: 11101101
Result in binary: 00111010
Result in decimal: 58
Overflow: No

Expression b: (-35) - (-12)
First operand: 11011101
Second operand: 11110100
2's complement of second operand: 00001100
Result in binary: 11101001
Result in decimal: -23
Overflow: No
