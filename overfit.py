
import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0, 2*math.pi, 0.5)
#x = np.linspace(0,6,10)
#x = random.randint(0,12,10)
#y = np.sin(x)+random.rand(-1,1)
#y1 =np.sin(x)
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([0,3,7,6,9,11,12,15,13,20])
#12次项式拟合n
pfit = np.polyfit(x,y,12)
y_fun = np.poly1d(pfit)
#原始
pfit1 = np.polyfit(x,y,2)
y_fun1 = np.poly1d(pfit1)
plt.scatter(x,y,label="point")
plt.plot(x, y_fun1(x),color ="b",label="rule fit")
plt.plot(x,y_fun(x),color = "r",label="over fit")
plt.legend()
plt.show()
print(y_fun1(x))
print(y_fun(x))
s=(y_fun1(x)-y_fun(x))^2
print(s)