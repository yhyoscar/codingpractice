
import time
import numpy as np

def myrand(low=0, high=1, size=100):
    if high-low <= 1:
        a = 1.23456789e99
        c = 9.87654321e99
        m = 5.55555555e99
        k = 100
        seed = time.time()
        value = []
        for i in range(k+size):
            value.append(seed/m)
            seed = (a*seed + c) % m
        return value[k:]
    else:
        return None
    
a = myrand(size=10000)
print( np.histogram(a, 10) )



