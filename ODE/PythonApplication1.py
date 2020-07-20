import math
import matplotlib.pyplot as plt

qwe = []
asd = []

def function(t, T, param):
    velocity = -13137.38* math.exp(t * ((-1.5) / 10)) - 450/(-1.5);
    moment = (-1.5) * velocity + 450;
    return moment * 0.01 + velocity*velocity*0.0001 + 0.1*param - 0.1*T;


def runge_kutta(time, parametr, T_nach, i, q, asd): 
    Tp = 110
    a = time[i]
    b = time[i] + 10
    time.append(b)
    h = (b - a) / 10
    n = 99
    t = []
    V1 = []
    V2 = []
    V3 = []
    V4 = []
    T = []
    t.append(time[i])
    T.append(T_nach[i])
    V1.append(0)
    V2.append(0)
    V3.append(0)
    V4.append(0)
       
    for j in range(1,10):
        t.append(a + j * h)
        V1.append(h * function(t[j - 1], T[j - 1], parametr))
        V2.append(h * function(t[j - 1] + h / 2.0, T[j - 1] + V1[j] / 2.0, parametr))
        V3.append(h * function(t[j - 1] + h / 2, T[j - 1] + V2[j] / 2, parametr))
        V4.append(h * function(t[j - 1] + h, T[j - 1] + V3[j], parametr))
        T.append(T[j - 1] + (V1[j] + 2 * V2[j] + 2 * V3[j] + V4[j]) / 6)
    T_nach.append(T[9])
    for i in range(len(t)):
        q.append(t[i])
        asd.append(T[i])
    for i in range(10): 
        if T[i] >= Tp: 
            return t[i]
    return -1;

T_nach = []
param = int(input())
timer = []
timer.append(37.14129)
T_nach.append(param + 40.688)

for i in range(35):
    r = runge_kutta(timer, param, T_nach, i, qwe ,asd)
    if r != -1:
        print(r)
        break
print(qwe)
print(asd)

plt.plot(qwe, asd)
plt.show()