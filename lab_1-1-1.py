'''
Уровень 2 задание 1.
Вычислить сумму = cos x + (cos 2x)/22 + ... + (cos nx)/n²+ ... .
Суммирование прекратить, когда очередной член суммы по модулю будет меньше в = 0,0001
'''

import math
s = 0
n = 1
eps = 0.0001
x = int(input("Введите x >> "))
cs = math.fabs(math.cos(n * x) / n ** 2)

while cs >= eps:
    cs = math.fabs(math.cos(n * x) / n ** 2)
    s += cs
    n += 1

print()
print("Результат >>", round(s, 3))
