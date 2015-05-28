from time import time
start = time()

num = 600851475143
factor = 0

while factor != num:
    factor += 1
    if (num % factor == 0 and factor != 1):
        num = num/factor
        ans = factor
        factor = 0

print(str(ans))
print("--- %s seconds ---" % (time() - start))

