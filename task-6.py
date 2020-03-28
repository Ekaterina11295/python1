a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
i = 1
while a < b and i > 0:
    a *= 1.1
    i += 1
    if a >= b:
        break
print('На {}й день спортсмен достиг результата - не менее {} км'.format(i, b))