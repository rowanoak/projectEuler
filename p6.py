from time import time

start = time()
squaresum = 0
sumsquare = 0

for x in range(1,101):
    sumsquare += x**2
    squaresum += x

squaresum = squaresum**2
print(str(squaresum-sumsquare))
print("--- %s seconds ---" % (time() - start))



    
