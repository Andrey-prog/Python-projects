from math import log10,log
import matplotlib.pyplot as plt #Импорт графической библиотеки

e = float(input()) #Эпсилон
a = float(input()) #Начальное приближение
arg = []
znac = []
arg1 = []
znac1 = []
def func(x):  #Уравнение функции
    y = x**2-10*log10(x)-3
    return y
def diff(x):  #Уравнение производной функции
    t = 2*x -10*(1/(x*log(10)))
    return t
def Newton(e,a):  #Метод Ньютона
    count = 0
    while abs(func(a)) > e:
        a = a-((func(a))/(diff(a)))
        count+=1
    return a,count
print(Newton(e,a))

def it(e,a): #Функция, возвращающая количество итераций
    mass = Newton(e,a)
    return int(mass[1])

def graf():  #График зависимости числа итераций от эпсилон
    q = e
    for i in range(7):
        arg.append(q)
        znac.append(it(q,a))
        q*=10
    plt.plot(arg,znac)
    plt.show()
    print(arg)
    print(znac)

print(graf())

def graf1():  #График зависимости числа итераций от начального приближения
    a1 = a
    for i in range(int(a-5)):
        arg1.append(a1)
        znac1.append(it(e,a1))
        a1-=1
        print(a1)
    plt.plot(arg1,znac1)
    plt.show()
    print(arg1)
    print(znac1)

print(graf1())