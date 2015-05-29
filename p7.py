from time import time

start = time()

prime = 0
cnt = 0

while prime != 10001:
    cnt += 1
    isprime = 1
    if cnt <= 1:
        isprime = 0
    elif cnt <= 3:
        isprime = 1
    elif cnt % 2 == 0 or cnt % 3 == 0:
        isprime = 0

    i = 5
    while i**2 <= cnt:
        if cnt % i == 0 or cnt % (i + 2) == 0:
            isprime = 0
        i += 6
    if isprime == 1:
        prime += 1
print(str(cnt))
print("--- %s seconds ---" % (time() - start))