import matplotlib.pyplot as plt
import math

e = float(input())
a = float(input())#Правая граница
b = float(input())#Левая граница
arg = []
znac = []
arg1 = []
znac1 = []

def func(x):  #Уравнение функции
    y = 2**(x-2) + 5*x*math.sin(math.pi*x)
    return y

def Dih(e,a,b):  #Метод
    count = 0
    while abs(abs(func(a))-abs(func(b))) > e:
        count += 1
        h=(a+b)/2
        if func(h)>0:
            a = h
        else:
            b = h
    return h,count
print(Dih(e,a,b))

def it(e,a,b): #Функция, возвращающая количество итераций
    mass = Dih(e,a,b)
    return int(mass[1])

def graf():
    q = e
    for i in range(20):
        arg.append(q)
        znac.append(it(q,a,b))
        q+=(q/10)
    plt.plot(arg,znac)
    plt.show()
    print(arg)
    print(znac)

print(graf())

def graf1():
    a1 = a
    b1 = b
    for i in range(10):
        arg1.append(abs(abs(a1)-abs(b1)))
        znac1.append(it(e,a1,b1))
        a1-=((a1+(e/10))/50)
        b1-=(b1/50)
        print(a1, b1)
    plt.plot(arg1,znac1)
    plt.show()
    print(arg1)
    print(znac1)

print(graf1())






