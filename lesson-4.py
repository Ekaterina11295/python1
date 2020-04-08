#задача 1
def my_func(hours,rate,premium):
    salary = hours * rate + premium
    return salary

print(my_func(int(input('введите кол-во часов - ')),int(input('введите ставку - ')),int(input('введите премию - '))))
#задача 2
old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for num, el in enumerate(old) if old[num-1] < old[num]]
del new[0]
print(f'Исходный список {old}')
print(f'Новый список {new}')


#задача 3
new = {el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0}
print(new)

#задача 4
old = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in old if old.count(el) < 2]
print(f'Исходный список {old}')
print(f'Новый список {new}')

#задача 5
from functools import reduce

def my_func(num1, num2):
    return num1 * num2
print(f'Четные значения - {[num1 for num1 in range(100, 1001) if num1 % 2 == 0]}')
print(f'Результат перемножения всех элементов - {reduce(my_func, [num1 for num1 in range(100, 1001) if num1 % 2 == 0])}')


#задача 6
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

c = 0
for el in cycle([1, 2, 3]):
        print(el)
        c += 1
        if c > 8:
            break
#задача 7
from itertools import count
from math import factorial

def fact():
    for el in count(1):
         yield factorial(el)

generator = fact()
n = 0
for i in fact():
    if n < 4:
         print(i)
         n += 1
    else:
         break
