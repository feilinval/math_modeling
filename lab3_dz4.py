from math import sin
A = 8
B = 7
mtx = []
for i in range(A):
    a = []
    for j in range(B):
        a.append(sin(A*(i+1) + B*(j+1)))
    mtx.append(a)
    for i in range (a):
        if mtx[i][j] < 0:
            mtx[i][j] = 0
            print("%7.0f" % mtx[i][j], end='')
        else:
            print("%7.2f" % mtx[i][j], end='')
            print(A,B) 