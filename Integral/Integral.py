import math
import matplotlib.pyplot as plt  
a = float(input())
b = float(input())
sposob = input("Введите способ вычисления")
n = int(input())
def func(x):
    y = math.exp(5*x)
    return y

def simpson(n):
    c = (b-a)/n
    r = a
    sum = 0
    for i in range(n):
        p = r
        r = p+c
        d = ((r-p)/6)*(func(p) + 4*func((p+r)/2) + func(r))
        sum += d
    return sum

def P(n,t): #Вычисление значений полинома Лежандра в каноническом виде
    if n == 0:
        return 1
    elif n == 1:
        return t
    else:
        m = n-1
        return ((2*m + 1)/(m + 1))*t*P(m,t) - (m/(m+1))*P(m-1,t)

def diff(n,t): #Вычисление производной в каноническом виде
    if n == 0:
        return 0
    else:
        return (n/(1-(t**2)))*(P(n-1,t) - t*P(n,t))

def gauss(n):
    e = 10**(-5)
    z = []
    u = []
    for i in range(1,n+1):   #Вычисление корней полинома Лежандра
        x_0 = math.cos(math.pi*(4*i - 1)/(4*n + 2))
        x_1 = x_0 - (P(n, x_0)/diff(n, x_0))
        while abs(abs(x_0) - abs(x_1)) > e:
            x_0 = x_1
            x_1 = x_0 - (P(n, x_0)/diff(n, x_0))
        z.append(0.5*(b-a)*x_1 + 0.5*(a+b))
        u.append(x_1)
    c_k = []
    for i in range(n): #Вычисление весов
        c_k.append(2/((1 - u[i]**2)*(diff(n, u[i]))**2))
    s = []
    for i in range(n): #Значения функции
        s.append(func(z[i]))
    sum = 0
    for i in range(n):
        sum += c_k[i]*s[i]
    return(0.5*(b-a)*sum)
def factorial(n):
    l = 1
    for i in range(1,n+1):
        l*=i
    return l
def ostatoks(n):
    return (625*math.exp(5)*(b-a)**5)/(2880*(n+1))
def ostatokg(n):
    return (((factorial(n)**4)*(5**(2*n))*math.exp(5))/((2*n +1)*((factorial(2*n))**3)))
    #(625*math.exp(5))/4320 #abs((((factorial(n))**4) *(5**(2*n))*((b-a)**(2*n+1)))/((2*n+1)*((factorial(2*n))**3)))

if sposob.find("G") != -1 or sposob.find("Г") != -1 or sposob.find("g") != -1:
    print(gauss(n))
    #print(1/8 - gauss(n))
else:
    print(simpson(n))
    #print(1/4 - simpson(n))

#print(abs(((math.exp(5) / 5) - (1/5)) - gauss(n)))
#print(ostatokg(n))
#print(math.exp(5)/5 - 1/5)

def graf():  #График функции
    lol = []
    kek = []
    for i in range(2,5):
        lol.append(i)
        kek.append(ostatokg(i))
    return kek

print(graf())

def runge():
    for i in range(2,9,2):
        if abs((math.exp(5)/5 - 1/5) - gauss(i)) <= abs((2**(2*i - 1)/(2**(2*i - 1) - 1))*(gauss(i) - gauss(i-1))):
            print("yes")
        else:
            print("no")
        print(abs((2 ** (2 * i - 1) / (2 ** (2 * i - 1) - 1)) * (gauss(i) - gauss(i-1))))
print(runge())

def qwertyui():
    for i in range(2,9):
        print(ostatokg(i))
        if abs(((math.exp(5) / 5) - (1 / 5)) - gauss(i)) < ostatokg(i):
            print("Yes")

def ost():
    h = []
    h1 = []
    h2 = []
    for i in range(2,5):
        h.append(abs(gauss(i) - gauss(8)))
        h1.append(abs(abs(gauss(i)) - abs(math.exp(5)/5 - 1/5)))
        h2.append(ostatokg(i))
    return (h,h1,h2)
print(ost())

def S():
    d = []
    m = []
    for i in range(1,n+1):
        d.append(abs((abs(simpson(2**i)) - abs(math.exp(5)/5 - 1/5))))
    for i in range(1,n):
        m.append(d[i-1]/d[i])
    return (d,m)
print(S())


