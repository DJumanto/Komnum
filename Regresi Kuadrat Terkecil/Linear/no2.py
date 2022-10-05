import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import math as mt

#take datata from text input
data = open("input2.txt", "r")
datalist = []
for i in data:
    datalist.append(int(i))
print(datalist)
data.close()
newdat = np.array(datalist)
newdat = newdat.reshape(2,10)
print(newdat)
_xmean = np.mean(newdat[0])
_ymean = np.mean(newdat[1])
print("rerata dari x adalah: ", _xmean)
print("rerata dari y adalah: ",_ymean)
up = (len(newdat[0])*np.sum(np.multiply(newdat[0],newdat[1]))) - (np.sum(newdat[0])*np.sum(newdat[1]))
down = (len(newdat[0])*np.sum(np.multiply(newdat[0],newdat[0]))) - mt.pow(np.sum(newdat[0]),2)
b = up/down
print(b)
a = _ymean - (b*_xmean)
y = []
for i in range(len(newdat[0])):
    y.append(a+(b*newdat[0][i]))
print(y)
plt.plot(newdat[0],y,'b',newdat[0],newdat[1], 'ro')
plt.show()
fungsi = f"{a:.4f}+{b:.4f}x"
output = open("output2.txt", 'w')
output.write("rerata dari x adalah: %f\n"%_xmean)
output.write("rerata dari y adalah: %f\n"%_ymean)
output.write("b: %f\n"%b)
output.write("a: %f\n"%a)
output.write("perkiraan fungsi: %s\n"%fungsi)
output.write("perkiraan y: %s\n"% str(y))
output.close()
