import numpy as np
from math import *

def calNGB(datay,s,n):
    val = datay[n-1][0]
    it = n-2
    for i in range(n):
        temp =s
        for j in range(i):
           temp*=s+j
        val+= (temp*datay[it-1][i])/factorial(i+1)
        it-=1
    return val
             

dataX = np.array([0.1 , 0.6, 1.1, 1.6, 2.1])

n=5
dataY = [[0 for i in range(n)] for j in range(n)]
dataY[0][0] = 1.1052
dataY[1][0] = 1.8221
dataY[2][0] = 3.0042
dataY[3][0] = 4.9530
dataY[4][0] = 8.1662
for i in range(1,n):
    for j in range(n-1,i-1,-1):
        dataY[j][i] = dataY[j][i-1] - dataY[j-1][i-1]

s = (2-dataX[4])/dataX[1]-dataX[0]
final = calNGB(dataY,s,n)
print(final)



