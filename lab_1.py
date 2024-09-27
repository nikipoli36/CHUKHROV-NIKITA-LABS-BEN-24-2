import math

'''
Третий уровень, задача номер 1.
Вычислить сумму ѕ, прекращая суммирование,
когда очередной член суммы по абсолютной величине станет меньше 0,0001,
при изменении аргумента х в указанном диапазоне [а, b] с шагом 4.
Для сравнения в каждой точке вычислить также функцию у = f(x),
являющуюся аналитическим выражением ряда.
'''

s = 0
a = int(0.1)
b = 1
h = 0.1
i = 0
eps = 0.0001
x = a
cs = ((-1)**i) * (x**(2*i) / math.factorial(2*i))
y = math.cos(x)
for x in range(a,b):
    while cs >= eps:
        cs = ((-1) ** i) * (x ** (2 * i) / math.factorial(2 * i))
        y += math.cos(x)
        s += cs
        i += 1
        x += h

print()
print("Результат >>", s)
print("Результат для сравнения >>", round(y, 3))