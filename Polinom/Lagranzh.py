import math
import matplotlib.pyplot as plt  # Импорт графической библиотеки

a = 1
b = 8
sposob = input("Введите способ распределения узлов ")
n = int(input("Введите индекс последнего узла "))
arg = []
znach = []
znach1 = []
z = []
c = (b-a)/n
delta = []
def func(x): #Функция
    y = 2*abs(x**2 - 1)
    return y


def mass(n): #Узлы интерполяции
    z = []
    if sposob.find("Р") != -1 or sposob.find("р") != -1:
        for i in range(n+1):
            z.append(a+c*i)

    elif sposob.find("Ч") != -1 or sposob.find("ч") != -1:
        e = b+a
        s = b-a
        z = [a, b]
        for i in range(n-1):
            z.append(0.5*e + 0.5*s*math.cos(math.pi*(2*i + 1)/(2*(n+1))))

    else:
        for i in range(n+1):
            z.append(a+c*i)
    return(z)

g = mass(n)
print(mass(n))

def lagranzh(t): #Метод
    sum = 0
    for j in range(len(g)):
        p1 = 1
        p2 = 1
        for i in range(len(g)):
            if i == j:
                p1*=1
                p2*=1
            else:
                p1*=(t-g[i])
                p2*=(g[j]-g[i])
        sum+=((p1/p2)*func(g[j]))
    return(sum)


def graf():  #График функции+полином
    k = (b-a)/200
    for q in range(201):
        r = a + k*q #координата по x
        f = func(r) #координата по y функции
        l = lagranzh(r) #координата по y полинома лагранжа

        arg.append(r)
        znach.append(f)
        znach1.append(l)
        delta.append(abs(f-l))

    plt.plot(arg,znach)
    plt.plot(arg,znach1)
    return plt.show()

def dell():
    plt.plot(arg,delta)
    return plt.show()


print(graf())
print(dell())


