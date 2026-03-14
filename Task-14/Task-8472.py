from string import printable

for x in printable[:16]:
    num1 = int(f'7a{x}0123', 16)
    num2 = int(f'1ba64{x}', 16)
    num3 = int(f'{x}98012c', 16)
    num = num1 - num2 + num3
    if num % 2 == 0:
        print(num // 21)

