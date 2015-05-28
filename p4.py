from time import time
start = time()
num = 0
for x in range(100,1000):
    for y in range(x,1000):
        if x*y < (999999):
            if (str(x*y) == (str(x*y)[::-1])):
                if num < x*y:
                    num=x*y
print(str(num))
print("--- %s seconds ---" % (time() - start))
