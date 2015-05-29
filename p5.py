from time import time

start = time()

found = 0
num = 0

while found == 0:
    num += 20
    if num%20 == 0:
        if num%19 == 0:
            if num%18 == 0:
                if num%17 == 0:
                    if num%16 == 0:
                        if num%14 == 0:
                            if num%13 == 0:
                                if num%12 == 0:
                                    if num%11 == 0:
                                        found = 1
                                        print(str(num))
print("--- %s seconds ---" % (time() - start))
