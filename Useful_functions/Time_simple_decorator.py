import random
import time



def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp

@timer
def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(len(ar)-i-1):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
    return ar

ar = [random.randint(0,100) for i in range(100)]

print(bubble_sort(ar))
