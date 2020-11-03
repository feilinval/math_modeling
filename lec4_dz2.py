import numpy as np

def mult_func(b):
    c = 1
    for a in b:
        c = c*a

    print(c)
mult_func(np.array([1,3,6,7]))
