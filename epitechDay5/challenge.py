import time
start=time.time()
bigList = []
import random

my_list = []

for i in range(1000000):
    bigList.append(random.randint(1, 100))


bigList.sort()
print(bigList)
print(time.time()-start)
