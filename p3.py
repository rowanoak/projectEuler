num = 600851475143

while factor != num:
    factor += 1
    if (num % factor == 0 and factor != 1):
        print(str(factor))
        num = num/factor
        factor = 0

print(str(num/factor))
